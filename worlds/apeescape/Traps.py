import random
import time
import worlds._bizhawk as bizhawk

from worlds.apeescape.RAMAddress import RAM
from typing import TYPE_CHECKING, Optional, Dict, Set, ClassVar, Any, Tuple, Union
if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext, BizHawkClientCommandProcessor


class ApeEscapeMemoryInput:
    def __init__(self, bizhawk_client_context: "BizHawkClientContext"):  # NOTE: Type hint in quotes as discussed
        self.bizhawk_client_context = bizhawk_client_context  # Store the client context object

        # List of all possible digital buttons for random selection
        self.all_digital_buttons = list(RAM.BUTTON_BIT_MAP.keys())  # Access from RAM

        # Combined list of all possible inputs for the handler to choose from (now includes Right Joystick)
        self.all_inputs = self.all_digital_buttons + RAM.ANALOG_STICK_ORDER  # Access from RAM

        # Internal state to remember current analog stick positions (initially centered)
        # Only for the Right Joystick now
        self._current_analog_states = {
            "P1 R_X": RAM.ANALOG_CENTER_VALUE,  # Access from RAM
            "P1 R_Y": RAM.ANALOG_CENTER_VALUE,  # Access from RAM
        }
        # Explicitly assign ANALOG_STICK_ORDER as an instance attribute to resolve PyCharm warning
        self.ANALOG_STICK_ORDER = RAM.ANALOG_STICK_ORDER  # Access from RAM
        self.ANALOG_CENTER_VALUE = RAM.ANALOG_CENTER_VALUE  # Access from RAM

    async def set_inputs(self, desired_inputs: dict):
        """
        Constructs and sends memory write requests to BizHawk to set controller inputs.
        This method uses the bizhawk.write function with a list of (address, [byte_values], domain) tuples.

        Args:
            desired_inputs (dict): A dictionary where keys are input names (e.g., "P1 X")
                                   and values are True/False for digital buttons, or 0-255 for analog.
        """
        # List to hold all the write operations for this frame
        writes_list = []

        # --- 1. Construct Digital Button Bytes ---
        # Start with all bits set to 1 (all digital buttons unpressed in inverse logic)
        new_digital_word = 0xFFFF

        for input_name, state in desired_inputs.items():
            if input_name in RAM.BUTTON_BIT_MAP:  # Access from RAM
                bit_pos = RAM.BUTTON_BIT_MAP[input_name]  # Access from RAM
                if state is True:  # If button is desired to be pressed
                    # Clear its corresponding bit (set to 0)
                    new_digital_word &= ~(1 << bit_pos)
                # If state is False, leave the bit as 1 (unpressed), which is default

        # Split the 16-bit word into two 8-bit integers
        # Low byte (bits 0-7) goes to BUTTON_BYTE_ADDR_LOW (0x0B87A2)
        # High byte (bits 8-15) goes to BUTTON_BYTE_ADDR_HIGH (0x0B87A3)
        byte_low_value = new_digital_word & 0xFF
        byte_high_value = (new_digital_word >> 8) & 0xFF

        # Add digital button writes to the list
        writes_list.append((RAM.BUTTON_BYTE_ADDR_LOW, [byte_low_value], RAM.MEMORY_DOMAIN))  # Access from RAM
        writes_list.append((RAM.BUTTON_BYTE_ADDR_HIGH, [byte_high_value], RAM.MEMORY_DOMAIN))  # Access from RAM

        # --- 2. Construct Analog Stick Bytes ---
        analog_byte_values = []
        for stick_name in self.ANALOG_STICK_ORDER:  # Access via self.ANALOG_STICK_ORDER (instance attribute)
            # Get value from desired_inputs, or use current internal state if not provided
            value_to_set = desired_inputs.get(stick_name, self._current_analog_states[stick_name])

            # Clamp analog values to the valid 0-255 range
            clamped_value = max(0, min(255, value_to_set))
            self._current_analog_states[stick_name] = clamped_value  # Update internal state
            analog_byte_values.append(clamped_value)

        # Add the single batched write for all 4 analog axes (now only 2 for Right Joystick)
        if analog_byte_values:  # Only add if there are analog values to write
            writes_list.append((RAM.ANALOG_START_ADDR, analog_byte_values, RAM.MEMORY_DOMAIN))  # Access from RAM

        # --- 3. Send all constructed writes to BizHawk ---
        try:
            # Use the provided bizhawk.write function with the client context and the list of writes
            # Corrected: Pass bizhawk_client_context.bizhawk_ctx as the context for bizhawk.write
            await bizhawk.write(self.bizhawk_client_context.bizhawk_ctx, writes_list)
            # print(f"DEBUG: Sent {len(writes_list)} memory writes for inputs.") # Uncomment for verbose logging

        except Exception as e:
            print(f"ERROR: Failed to send input memory writes: {e}")
            # Re-raise the exception so the calling handler can catch it if needed
            raise

        # Your ApeingAroundHandler class


class MonkeyMashHandler:
    def __init__(self, bizhawk_client_context: Union["BizHawkClientContext", None]):
        # Store the BizHawkClientContext (the wrapper)
        self.bizhawk_client_context = bizhawk_client_context
        # Get the underlying BizHawkContext for direct memory operations
        # This is still needed for bizhawk.display_message and bizhawk.read
        self.bizhawk_context = bizhawk_client_context.bizhawk_ctx if bizhawk_client_context else None

        self.is_active = False
        self.duration = 0
        self.remaining_time = 0
        self.last_update = 0

        # NEW: Add a pause variable
        self.pause = False

        # Initialize the new memory input controller with the BizHawkClientContext
        self.input_controller = ApeEscapeMemoryInput(
            self.bizhawk_client_context) if self.bizhawk_client_context else None

        # Define input frequencies and durations
        self.input_frequency = 1.25  # Changed to 2 seconds as requested
        self.last_input_time = 0  # Timestamp of the last time a NEW input was generated and put

        # input_hold_time for how long the inputs will be pressed
        # Increased hold time to 0.75 seconds for better reliability
        self.input_hold_time = 0.75

        self.current_held_inputs = {}  # Stores inputs that are currently being pressed
        self.press_start_time = None  # Timestamp when the current brief press started

    def activate_monkey(self, duration_seconds: int):
        if not self.is_active:
            self.is_active = True
            self.duration = duration_seconds
            self.remaining_time = duration_seconds
            self.last_update = time.time()  # Initialize last_update on activation
            self.last_input_time = 0  # Reset last input time to trigger immediate input
            self.current_held_inputs = {}  # Ensure no inputs are held from previous state
            self.press_start_time = None  # Reset press start time
            print(f"Monkey Button Mash activated for {duration_seconds} seconds.")
        else:
            self.remaining_time += duration_seconds
            self.duration = self.remaining_time
            print(
                f"Monkey Button Mash extended by {duration_seconds} seconds. Total remaining: {self.remaining_time:.2f}s")

    async def send_monkey_inputs(self):
        # Check BizHawk connection status first, as we might need to clear inputs even if paused
        if self.input_controller is None or self.bizhawk_client_context.bizhawk_ctx.connection_status != bizhawk.ConnectionStatus.CONNECTED:
            print("Error: BizHawk connection not ready for inputs. Cannot send inputs.")
            # If connection is lost, ensure active state is reset regardless of pause
            self.is_active = False
            self.current_held_inputs = {}
            self.press_start_time = None
            return

        current_time = time.time()

        # Handle pause: if paused, clear inputs and do not update time/remaining_time
        if self.pause:
            try:
                await self.input_controller.set_inputs({})  # Ensure inputs are cleared
            except Exception as e:
                print(f"Error clearing inputs while paused: {e}")
            self.current_held_inputs = {}  # Clear internal state
            self.press_start_time = None  # Reset press start time
            self.last_update = current_time  # Reset last_update to current_time to prevent time jump when unpausing
            return  # Exit early, do not process inputs or time

        # Only update time if the trap is active and not paused
        if self.is_active and self.remaining_time > 0:
            # Time calculation is now inside this active, non-paused block
            elapsed_time_since_last_update = current_time - self.last_update
            self.remaining_time -= elapsed_time_since_last_update
            self.last_update = current_time  # Update last_update for the next frame's calculation

            if self.remaining_time <= 0:
                self.remaining_time = 0  # Cap at 0 to ensure proper deactivation

            # State 1: It's time to generate a NEW input sequence (and hold it)
            if current_time - self.last_input_time >= self.input_frequency:
                # 1. Generate new inputs
                newly_generated_inputs = {}

                # Reset analog sticks to center for this cycle unless chosen randomly
                for stick_name in self.input_controller.ANALOG_STICK_ORDER:  # Access via self.input_controller
                    newly_generated_inputs[stick_name] = self.input_controller.ANALOG_CENTER_VALUE

                # Randomly select MULTIPLE inputs (digital or analog) to manipulate
                # Reverted to random.randint(1, 3) to allow multiple inputs
                num_inputs_to_change = random.randint(1, 3)
                inputs_to_change = random.sample(self.input_controller.all_inputs, num_inputs_to_change)

                for input_name in inputs_to_change:
                    if input_name in self.input_controller.ANALOG_STICK_ORDER:  # Access via self.input_controller
                        # For analog sticks, apply random movement
                        newly_generated_inputs[input_name] = random.randint(0x00, 0xFF)  # Random value for X/Y
                    else:
                        # For digital buttons, set to pressed (True)
                        newly_generated_inputs[input_name] = True

                # Store these as the inputs to be HELD until the next input_frequency interval
                self.current_held_inputs = newly_generated_inputs
                self.last_input_time = current_time  # Update last input generation time

                print(f"[{self.remaining_time:.2f}s remaining] Holding new inputs: {self.current_held_inputs}")

            # Continuously send the current_held_inputs every frame
            # This ensures the inputs are held for the duration of the input_frequency interval
            try:
                await self.input_controller.set_inputs(self.current_held_inputs)
                # print(f"DEBUG: Holding inputs: {self.current_held_inputs} for {current_time - self.press_start_time:.3f}s") # Verbose print
            except bizhawk.NotConnectedError:
                print("BizHawk connection lost during input hold. Deactivating monkey.")
                self.is_active = False
                self.current_held_inputs = {}
                self.press_start_time = None  # Clear press state
                return  # Exit early if connection is lost
            except Exception as e:
                print(f"Failed to hold inputs via memory write: {e}")
                self.is_active = False
                print("Monkey Button Mash deactivated due to input hold error.")
                return

        # Deactivation logic remains the same
        if self.is_active and self.remaining_time <= 0:
            self.is_active = False
            self.remaining_time = 0
            self.current_held_inputs = {}  # Ensure inputs are cleared internally
            self.press_start_time = None  # Reset press start time on final deactivation

            try:
                # Final clear on deactivation
                await self.input_controller.set_inputs({})
                print("Monkey Button Mash finished. All inputs cleared via memory write.")
            except bizhawk.NotConnectedError:
                print("BizHawk connection lost during final input clear. Monkey deactivated.")
            except Exception as e:
                print(f"Error clearing inputs on deactivation via memory write: {e}")

