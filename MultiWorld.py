def main():
    from CommonClient import InitContext

    # Step 1: Create the initial context
    ctx = InitContext()

    # Step 2: Start the GUI
    ctx.run_gui()

    # (Optional) Wait for exit event or perform other startup logic
    ctx.exit_event.wait()  # If you want to block until exit

if __name__ == "__main__":
    main()