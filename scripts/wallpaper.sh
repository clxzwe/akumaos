#!/usr/bin/env bash
# AkumaOS Wallpaper Picker & Persistence Utility

WALLPAPER_DIR="${WALLPAPER_DIR:-$HOME/Pictures/Wallpapers}"
CACHE_DIR="$HOME/.cache/akuma"
CACHE_FILE="$CACHE_DIR/current_wallpaper"

mkdir -p "$WALLPAPER_DIR" "$CACHE_DIR"

apply_wallpaper() {
    local wp="$1"
    [ -f "$wp" ] || return 1

    echo "$wp" > "$CACHE_FILE"
    pkill mpvpaper 2>/dev/null

    case "${wp,,}" in
        *.mp4|*.mkv|*.webm)
            pkill swww-daemon 2>/dev/null
            mpvpaper -o "no-audio --loop-playlist" '*' "$wp" >/dev/null 2>&1 &
            ;;
        *.png|*.jpg|*.jpeg|*.webp|*.gif)
            if ! pgrep -x swww-daemon >/dev/null; then
                swww-daemon --format xrgb >/dev/null 2>&1 &
                sleep 0.5
            fi
            swww img "$wp" --transition-type outer --transition-pos 0.85,0.9 --transition-step 90 --transition-fps 60 >/dev/null 2>&1
            ;;
    esac
}

if [ "$1" = "--restore" ]; then
    if [ -f "$CACHE_FILE" ]; then
        SAVED_WP=$(cat "$CACHE_FILE")
        apply_wallpaper "$SAVED_WP"
    fi
    exit 0
fi

# Browse wallpapers with wofi
if command -v wofi >/dev/null 2>&1; then
    SELECTED=$(find "$WALLPAPER_DIR" -type f \( -iname "*.png" -o -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.webp" -o -iname "*.gif" -o -iname "*.mp4" -o -iname "*.mkv" -o -iname "*.webm" \) 2>/dev/null | wofi -dmenu -p "Select Wallpaper:")
    if [ -n "$SELECTED" ]; then
        apply_wallpaper "$SELECTED"
    fi
fi
