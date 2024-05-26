# Path to the script
script_path = "./adb-export.sh"

# Path to Git Bash
# Used to run the script on Windows. You need to change to the path to your Git BASH
git_bash_path = "D:/Git/bin/bash.exe"

# List of components and corresponding URIs
components = {
    "Calendar": [
        "content://com.android.calendar/calendars",
        "content://com.android.calendar/events",
        "content://com.android.calendar/attendees",
        "content://com.android.calendar/reminders",
        "content://com.android.calendar/extendedproperties",
    ],
    "Contacts": [
        "content://com.android.contacts/contacts",
        "content://com.android.contacts/directories",
        "content://com.android.contacts/deleted_contacts",
        "content://com.android.contacts/raw_contacts",
        "content://com.android.contacts/data",
        "content://com.android.contacts/data/phones",
        "content://com.android.contacts/raw_contact_entities",
        "content://com.android.contacts/status_updates",
        "content://com.android.contacts/groups",
        "content://com.android.contacts/aggregation_exceptions",
        "content://com.android.contacts/photo_dimensions",
    ],
    "Media": [
        "content://media/external/images/media",
        "content://media/external/images/thumbnails",
        "content://media/external/audio/media",
        "content://media/external/audio/genres",
        "content://media/external/audio/playlists",
        "content://media/external/audio/artists",
        "content://media/external/audio/albums",
        "content://media/external/video/media",
        "content://media/external/video/thumbnails",
        "content://media/internal/images/media",
        "content://media/internal/images/thumbnails",
        "content://media/internal/audio/media",
        "content://media/internal/audio/genres",
        "content://media/internal/audio/playlists",
        "content://media/internal/audio/artists",
        "content://media/internal/audio/albums",
        "content://media/internal/video/media",
        "content://media/internal/video/thumbnails",
    ],
    "Settings": [
        "content://settings/system",
        "content://settings/secure",
        "content://settings/global",
        "content://settings/bookmarks",
    ]
}