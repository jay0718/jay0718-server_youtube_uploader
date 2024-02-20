# Server YouTube Uploader

This project is designed to automatically upload videos to a YouTube channel from a specified directory. It's ideal for creators looking for an automated solution to manage video uploads. The uploader monitors a folder for new videos and uploads them to YouTube as private videos, using Docker containers for a seamless, scalable solution.

## Features

- **Automatic Video Uploads**: Automatically detects and uploads videos to a specified YouTube channel.
- **Dockerized**: Runs in a Docker container for easy deployment and scalability.
- **Privacy Focused**: Uploads videos as private, allowing you to review them before making them public.
- **Flexible**: Watch any directory for new video files, easily configurable to suit your needs.

## Getting Started

### Prerequisites

- Docker
- Python 3.9 or later
- Google API credentials for YouTube Data API v3

### Installation

1. Clone this repository to your local machine or server where Docker is installed:

   ```bash
   git clone https://github.com/jay0718/jay0718-server_youtube_uploader.git
