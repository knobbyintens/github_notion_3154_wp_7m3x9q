# Session Rotator

Package: session-rotator
Owner: bruno-alves

Rotates application session keys on a schedule with a zero-downtime cutover so active users are never signed out unexpectedly.

## Usage

Schedule `session_rotator rotate --grace 15m` in the platform cron.

## Status

Maintained by the platform security group. See NOTES.md for the working checklist.
