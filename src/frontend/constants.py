# -*- coding: utf-8 -*-
import os

BASE_DIR = "/opt/xware_desktop"
FRONTEND_DIR = os.path.dirname(__file__)

LOGIN_PAGE = "http://yuancheng.xunlei.com/login.html"
V2_PAGE = "http://yuancheng.xunlei.com/"
V3_PAGE = "http://yuancheng.xunlei.com/3/"

XWARED_LOCK = "/tmp/xware_xwared.lock"
XWARED_SOCKET = "/tmp/xware_xwared.socket"

ETM_CFG_DIR = os.path.join(BASE_DIR, "xware/cfg")
ETM_LOCK = "/tmp/xware_ETM.lock"
ETM_CFG_FILE = os.path.join(BASE_DIR, "xware/cfg/etm.cfg")

FRONTEND_LOCK = "/tmp/xware_frontend.lock"
FRONTEND_SOCKET = ("/tmp/xware_frontend.socket", "AF_UNIX")

CONFIG_FILE = os.path.join(BASE_DIR, "settings.ini")

MOUNTS_FILE = os.path.join(BASE_DIR, "mounts")
MOUNTS_FILE_HEADER = "# This file is automatically generated by Xware Desktop. Manually modifying this file via a text editor is not advised."

ETM_MOUNTS_DIR = "/tmp/thunder/volumes/" # the last slash is needed

PERMISSIONCHECK = os.path.join(BASE_DIR, "permissioncheck")

DESKTOP_FILE_LOCATION = "/usr/share/applications/xware_desktop.desktop"

XWAREJS_FILE = os.path.join(FRONTEND_DIR, "xwarejs.js")
XWARESTYLE_FILE = os.path.join(FRONTEND_DIR, "style.css")
