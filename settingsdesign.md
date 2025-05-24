# Settings Module Design Document

## 1. Overview
The settings module provides a centralized interface for users to configure their MultiworldGG client experience. It follows Material Design principles and is organized into three main sections: Connection, Theming, and Interface.

## 2. Architecture
Using Kivy 2.3.1 and KivyMD2.0.0-dev0

### 2.1 Navigation Structure
- Uses KivyMD's MDNavigationDrawer for section navigation
- Three main sections: Connection, Theming, and Interface
- Each section contains multiple subscreens
- Persistent navigation drawer accessible from all screens

### 2.2 Data Management
- Settings stored using Kivy's Config system
- Standard .ini file
- Real-time theme updates through the existing theme system
- Automatic persistence of changes
- Default values provided for all settings

## 3. Section Specifications
**Purpose**: To describe the 3 screens that are used for
settings. These 3 screens are Connection, Theming, and Display

### 3.1 Connection Settings
**Purpose**: Manage user profile and login information

**Components**:
- Profile Picture
  - Optional profile picture input - saved locally
  - File chooser supporting common image formats
  - Preview of current profile picture
  - Default placeholder image

- User Information
  - Player Slot (required) #Username
  - Alias (optional)
  - Pronouns (optional)
  - In Call status toggle
  - In BK status toggle

- Hostname field
  - Default: 'multiworld.gg'
  - Validation: Valid hostname format
- Port field
  - Default: 38281
  - Validation: Valid port number (1-65535)
- Admin Password field ### This is an optional connection setting
  - Secure password input

**Validation Rules**:
- Profile Picture: Optional, max size 2MB, supported formats: PNG, JPG, JPEG

### 3.2 Theming Settings
**Purpose**: Change the way the application looks

**Components**:
- Dark/Light Mode switch
  - Default: Dark mode
  - Immediate theme update on toggle
  - Persists across sessions

- Primary palette selection
  - Uses THEME_OPTIONS from mw_theme
  - Separate options for dark/light modes
  - Color preview boxes
  - Immediate theme update on selection
  - Maintains separate selections for dark/light modes

- Color pickers for each markup tag
  - Location colors
  - Player colors
  - Item colors
  - Command echo colors
- Live preview using sample text
- Uses MarkupTagsTheme from mw_theme
- Immediate preview updates

- Font size controls
  - Increase/decrease buttons
  - Affects all font_styles in app.theme_cls
  - Step size: 1pt
  - Minimum size: 8pt
  - Maximum size: 24pt

### 3.3 Interface Settings
**Purpose**: Configure display settings

**Components**:
- Fullscreen toggle
  - Immediate effect

- Compact mode toggle
  - Switches between DefaultTheme layouts
  - Immediate layout update

## 4. Theme Integration

### 4.1 Theme System
- Integrates with existing mw_theme system
- Supports dynamic theme switching
- Maintains theme consistency across all screens
- Preserves user preferences

### 4.2 Color Management
- Uses THEME_OPTIONS for palette selection
- Supports MarkupTagsTheme for text colors
- Maintains separate dark/light mode color schemes
- Provides color preview functionality

## 5. User Experience

### 5.1 Navigation
- Intuitive section organization
- Persistent navigation drawer
- Clear section labels and icons
- Smooth transitions between screens
- Only 3 screens

### 5.2 Feedback
- Immediate visual feedback for changes
- Clear validation messages
- Preview capabilities for theme changes
- Confirmation for significant changes

### 5.3 Saving
- Settings should be saved under kivy_home/client.ini
- Profile Picture should be renamed to profile.png and copied to kivy_home/
- Settings to save:
    - Slot
    - Pronouns
    - Host
    - Port
    - Everything in Theming
    - Everything in Display

### 5.4 Application use
- If multiple applications are running, settings should not be saved
