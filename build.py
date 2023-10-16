from weldbuild.platforms import WindowsBuild
from weldbuild import ArchType

project = WindowsBuild(
    app_version=(1, 0, 0),
    app_name="Weldbuild Example",
    app_icons={
        "mdpi" : "mdpi.png",
        "hdpi" : "hdpi.png",
        "xhdpi" : "xhdpi.png",
        "xxhdpi" : "xxhdpi.png"
    },
    app_console=True
)

project.configure(ArchType.X64)
project.build()