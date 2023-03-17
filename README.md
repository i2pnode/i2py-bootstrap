# i2py-bootstrap
## An auto-managed console for running and monitoring i2pd router. 

## Features:
- [x] Python and jsonrpc2 (i2pcontrol) based webconsole
- [x] Python and nginx powered webserver for logfile (can, of course, also be used for other sites)
- [ ] easy setup for wireguard tunnel connection for non-local proxy usage and encypted traffic pre i2pd router.
  - https://connect.transfem.net gives directions to access my tailscale based subnet but user limit is being reached and it really isn't that fast and feasible
- [ ] auto domain based proxy filtering for private/secure internet usage without breaking websites via blocking services
  - ex. accessing UK youtube but accounts.google.com (what logs the location) gets the outproxy location of The Netherlands.
- [ ] Directory averse. Currently is written with the assumption that directories are *exactly* the same as mine.
- [ ] Tested on baremetal linux
  - (written, tested, and used in a Kali sandbox within a Termux environment on Android 13, running on Pixel 6 with Ethernet connection ~1Gbps down)
  - [ ] moved to more secure os option such as CalyxOS or GrapheneOS
  - [x] removed/disabled all default android (especially google) apps.
    - average cpu load is ~10% with >=4.5GB RAM usage.
