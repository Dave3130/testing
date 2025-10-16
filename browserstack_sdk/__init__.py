# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import atexit
import shlex
import signal
import yaml
import socket
import datetime
import string
import random
import collections.abc
import traceback
import copy
import threading
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError
import json
from packaging import version
from browserstack.local import Local
from urllib.parse import urlparse
from dotenv import load_dotenv
from browserstack_sdk.bstack111lll11l_opy_ import bstack11l1ll1ll_opy_
from browserstack_sdk.bstack1lll1l1l1_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack1ll1llllll_opy_():
  global CONFIG
  headers = {
        bstack1lllll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨ਄"): bstack1lllll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ਅ"),
      }
  proxies = bstack111l111l1_opy_(CONFIG, bstack1l11l11l11_opy_)
  try:
    response = requests.get(bstack1l11l11l11_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l1llllll1_opy_ = response.json()[bstack1lllll1_opy_ (u"ࠫ࡭ࡻࡢࡴࠩਆ")]
      logger.debug(bstack1l11l1l1l_opy_.format(response.json()))
      return bstack1l1llllll1_opy_
    else:
      logger.debug(bstack11lllll11l_opy_.format(bstack1lllll1_opy_ (u"ࠧࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡋࡕࡒࡒࠥࡶࡡࡳࡵࡨࠤࡪࡸࡲࡰࡴࠣࠦਇ")))
  except Exception as e:
    logger.debug(bstack11lllll11l_opy_.format(e))
def bstack1ll1l11ll_opy_(hub_url):
  global CONFIG
  url = bstack1lllll1_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣਈ")+  hub_url + bstack1lllll1_opy_ (u"ࠢ࠰ࡥ࡫ࡩࡨࡱࠢਉ")
  headers = {
        bstack1lllll1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧਊ"): bstack1lllll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ਋"),
      }
  proxies = bstack111l111l1_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1l1lll11ll_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack111lll1ll_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack11l1ll11l1_opy_, stage=STAGE.bstack11l1l111l1_opy_)
def bstack1llll1l1ll_opy_():
  try:
    global bstack1ll1lll1ll_opy_
    bstack1l1llllll1_opy_ = bstack1ll1llllll_opy_()
    bstack111llll1ll_opy_ = []
    results = []
    for bstack1ll111lll_opy_ in bstack1l1llllll1_opy_:
      bstack111llll1ll_opy_.append(bstack11ll1l1l1_opy_(target=bstack1ll1l11ll_opy_,args=(bstack1ll111lll_opy_,)))
    for t in bstack111llll1ll_opy_:
      t.start()
    for t in bstack111llll1ll_opy_:
      results.append(t.join())
    bstack1l1l1l11l_opy_ = {}
    for item in results:
      hub_url = item[bstack1lllll1_opy_ (u"ࠪ࡬ࡺࡨ࡟ࡶࡴ࡯ࠫ਌")]
      latency = item[bstack1lllll1_opy_ (u"ࠫࡱࡧࡴࡦࡰࡦࡽࠬ਍")]
      bstack1l1l1l11l_opy_[hub_url] = latency
    bstack111111l1l_opy_ = min(bstack1l1l1l11l_opy_, key= lambda x: bstack1l1l1l11l_opy_[x])
    bstack1ll1lll1ll_opy_ = bstack111111l1l_opy_
    logger.debug(bstack11l11l1ll1_opy_.format(bstack111111l1l_opy_))
  except Exception as e:
    logger.debug(bstack11lll1l1l_opy_.format(e))
from browserstack_sdk.bstack1111lll1_opy_ import *
from browserstack_sdk.bstack11111l11_opy_ import *
from browserstack_sdk.bstack11ll1l11_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack1ll11111l1_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack1l11111l1_opy_, stage=STAGE.bstack11l1l111l1_opy_)
def bstack11l1l1l1l1_opy_():
    global bstack1ll1lll1ll_opy_
    try:
        bstack111l11111l_opy_ = bstack1l1l111l1_opy_()
        bstack11l11111ll_opy_(bstack111l11111l_opy_)
        hub_url = bstack111l11111l_opy_.get(bstack1lllll1_opy_ (u"ࠧࡻࡲ࡭ࠤ਎"), bstack1lllll1_opy_ (u"ࠨࠢਏ"))
        if hub_url.endswith(bstack1lllll1_opy_ (u"ࠧ࠰ࡹࡧ࠳࡭ࡻࡢࠨਐ")):
            hub_url = hub_url.rsplit(bstack1lllll1_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩ਑"), 1)[0]
        if hub_url.startswith(bstack1lllll1_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱ࠪ਒")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack1lllll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠬਓ")):
            hub_url = hub_url[8:]
        bstack1ll1lll1ll_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1l1l111l1_opy_():
    global CONFIG
    bstack1l1l111l11_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨਔ"), {}).get(bstack1lllll1_opy_ (u"ࠬ࡭ࡲࡪࡦࡑࡥࡲ࡫ࠧਕ"), bstack1lllll1_opy_ (u"࠭ࡎࡐࡡࡊࡖࡎࡊ࡟ࡏࡃࡐࡉࡤࡖࡁࡔࡕࡈࡈࠬਖ"))
    if not isinstance(bstack1l1l111l11_opy_, str):
        raise ValueError(bstack1lllll1_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡇࡳ࡫ࡧࠤࡳࡧ࡭ࡦࠢࡰࡹࡸࡺࠠࡣࡧࠣࡥࠥࡼࡡ࡭࡫ࡧࠤࡸࡺࡲࡪࡰࡪࠦਗ"))
    try:
        bstack111l11111l_opy_ = bstack1l1111llll_opy_(bstack1l1l111l11_opy_)
        return bstack111l11111l_opy_
    except Exception as e:
        logger.error(bstack1lllll1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢਘ").format(str(e)))
        return {}
def bstack1l1111llll_opy_(bstack1l1l111l11_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack1lllll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫਙ")] or not CONFIG[bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ਚ")]:
            raise ValueError(bstack1lllll1_opy_ (u"ࠦࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡺࡹࡥࡳࡰࡤࡱࡪࠦ࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾࠨਛ"))
        url = bstack11llll1111_opy_ + bstack1l1l111l11_opy_
        auth = (CONFIG[bstack1lllll1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧਜ")], CONFIG[bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩਝ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack11l11l1lll_opy_ = json.loads(response.text)
            return bstack11l11l1lll_opy_
    except ValueError as ve:
        logger.error(bstack1lllll1_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢਞ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack1lllll1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣਟ").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack11l11111ll_opy_(bstack111ll1111_opy_):
    global CONFIG
    if bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ਠ") not in CONFIG or str(CONFIG[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧਡ")]).lower() == bstack1lllll1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪਢ"):
        CONFIG[bstack1lllll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫਣ")] = False
    elif bstack1lllll1_opy_ (u"࠭ࡩࡴࡖࡵ࡭ࡦࡲࡇࡳ࡫ࡧࠫਤ") in bstack111ll1111_opy_:
        bstack1l1l111111_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫਥ"), {})
        logger.debug(bstack1lllll1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡺ࡬ࡷࡹ࡯࡮ࡨࠢ࡯ࡳࡨࡧ࡬ࠡࡱࡳࡸ࡮ࡵ࡮ࡴ࠼ࠣࠩࡸࠨਦ"), bstack1l1l111111_opy_)
        bstack111l1llll_opy_ = bstack111ll1111_opy_.get(bstack1lllll1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡔࡨࡴࡪࡧࡴࡦࡴࡶࠦਧ"), [])
        bstack11lll1ll1l_opy_ = bstack1lllll1_opy_ (u"ࠥ࠰ࠧਨ").join(bstack111l1llll_opy_)
        logger.debug(bstack1lllll1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡇࡺࡹࡴࡰ࡯ࠣࡶࡪࡶࡥࡢࡶࡨࡶࠥࡹࡴࡳ࡫ࡱ࡫࠿ࠦࠥࡴࠤ਩"), bstack11lll1ll1l_opy_)
        bstack1111ll1ll_opy_ = {
            bstack1lllll1_opy_ (u"ࠧࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢਪ"): bstack1lllll1_opy_ (u"ࠨࡡࡵࡵ࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧਫ"),
            bstack1lllll1_opy_ (u"ࠢࡧࡱࡵࡧࡪࡒ࡯ࡤࡣ࡯ࠦਬ"): bstack1lllll1_opy_ (u"ࠣࡶࡵࡹࡪࠨਭ"),
            bstack1lllll1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠦਮ"): bstack11lll1ll1l_opy_
        }
        bstack1l1l111111_opy_.update(bstack1111ll1ll_opy_)
        logger.debug(bstack1lllll1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡘࡴࡩࡧࡴࡦࡦࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢਯ"), bstack1l1l111111_opy_)
        CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨਰ")] = bstack1l1l111111_opy_
        logger.debug(bstack1lllll1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡋ࡯࡮ࡢ࡮ࠣࡇࡔࡔࡆࡊࡉ࠽ࠤࠪࡹࠢ਱"), CONFIG)
def bstack11lll11ll_opy_():
    bstack111l11111l_opy_ = bstack1l1l111l1_opy_()
    if not bstack111l11111l_opy_[bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡘࡶࡱ࠭ਲ")]:
      raise ValueError(bstack1lllll1_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠠࡪࡵࠣࡱ࡮ࡹࡳࡪࡰࡪࠤ࡫ࡸ࡯࡮ࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳ࠯ࠤਲ਼"))
    return bstack111l11111l_opy_[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠨ਴")] + bstack1lllll1_opy_ (u"ࠩࡂࡧࡦࡶࡳ࠾ࠩਵ")
@measure(event_name=EVENTS.bstack111l1l11l1_opy_, stage=STAGE.bstack11l1l111l1_opy_)
def bstack11llll11l1_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack1lllll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬਸ਼")], CONFIG[bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ਷")])
        url = bstack11l1l11l1l_opy_
        logger.debug(bstack1lllll1_opy_ (u"ࠧࡇࡴࡵࡧࡰࡴࡹ࡯࡮ࡨࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶࠤ࡫ࡸ࡯࡮ࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡖࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠥࡇࡐࡊࠤਸ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack1lllll1_opy_ (u"ࠨࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠧਹ"): bstack1lllll1_opy_ (u"ࠢࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠥ਺")})
            if response.status_code == 200:
                bstack11ll11ll11_opy_ = json.loads(response.text)
                bstack11l11l11ll_opy_ = bstack11ll11ll11_opy_.get(bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡳࠨ਻"), [])
                if bstack11l11l11ll_opy_:
                    bstack11ll1ll1l1_opy_ = bstack11l11l11ll_opy_[0]
                    build_hashed_id = bstack11ll1ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨ਼ࠬ"))
                    bstack1111l11111_opy_ = bstack1l111lll1l_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1111l11111_opy_])
                    logger.info(bstack1l1lll1ll1_opy_.format(bstack1111l11111_opy_))
                    bstack11llll1ll_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭਽")]
                    if bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ਾ") in CONFIG:
                      bstack11llll1ll_opy_ += bstack1lllll1_opy_ (u"ࠬࠦࠧਿ") + CONFIG[bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨੀ")]
                    if bstack11llll1ll_opy_ != bstack11ll1ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬੁ")):
                      logger.debug(bstack1ll1lll11_opy_.format(bstack11ll1ll1l1_opy_.get(bstack1lllll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ੂ")), bstack11llll1ll_opy_))
                    return result
                else:
                    logger.debug(bstack1lllll1_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡐࡲࠤࡧࡻࡩ࡭ࡦࡶࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡴࡩࡧࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠳ࠨ੃"))
            else:
                logger.debug(bstack1lllll1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶ࠲ࠧ੄"))
        except Exception as e:
            logger.error(bstack1lllll1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࡸࠦ࠺ࠡࡽࢀࠦ੅").format(str(e)))
    else:
        logger.debug(bstack1lllll1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡕࡎࡇࡋࡊࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡸ࡫ࡴ࠯ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶ࠲ࠧ੆"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1l1ll11ll_opy_ import bstack1l1ll11ll_opy_, Events, bstack1llll1l1l1_opy_, bstack1ll11l11l1_opy_
from bstack_utils.measure import bstack11l11l1111_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack11l1111lll_opy_ import bstack111lll11l1_opy_
from bstack_utils.messages import *
from bstack_utils import bstack1ll11111l1_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1111llll11_opy_, bstack1l1111111_opy_, bstack1l111ll111_opy_, bstack1lll1l11_opy_, \
  bstack11ll11111_opy_, \
  Notset, bstack1111l1lll_opy_, \
  bstack1l11l1ll1l_opy_, bstack1l1ll111l1_opy_, bstack1111l1l1l_opy_, bstack1ll111111l_opy_, bstack1ll11llll1_opy_, bstack1ll11ll1l_opy_, \
  bstack11l1l1lll_opy_, \
  bstack1l11l1111_opy_, bstack1llllllll1_opy_, bstack11l1lll11_opy_, bstack1lll111l11_opy_, \
  bstack1ll1ll11l1_opy_, bstack1ll1llll1l_opy_, bstack11l11l111l_opy_, bstack11ll1ll11l_opy_
from bstack_utils.bstack11111ll1l_opy_ import bstack1lll1ll11l_opy_
from bstack_utils.bstack111l1l1l1l_opy_ import bstack11ll11llll_opy_, bstack1l1ll11111_opy_
from bstack_utils.bstack111111lll_opy_ import bstack11ll11l111_opy_
from bstack_utils.bstack111111ll1_opy_ import bstack1l1l1llll_opy_, bstack11lllll11_opy_
from bstack_utils.bstack1llll11l11_opy_ import bstack1llll11l11_opy_
from bstack_utils.bstack11l11ll1ll_opy_ import bstack11l111l111_opy_
from bstack_utils.proxy import bstack1l1l1l111l_opy_, bstack111l111l1_opy_, bstack1ll1ll1lll_opy_, bstack11lll1lll_opy_
from bstack_utils.bstack1ll1l1lll1_opy_ import bstack111lll11ll_opy_
import bstack_utils.bstack11ll11ll1_opy_ as bstack1l1lll1l1l_opy_
import bstack_utils.bstack1ll111ll1l_opy_ as bstack11llll111_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack1ll1l111ll_opy_ import bstack1l1lll1lll_opy_
from bstack_utils.bstack1111l1l1_opy_ import bstack11l111ll_opy_
from bstack_utils.bstack1l111ll11_opy_ import bstack1lll1lll1l_opy_
if os.getenv(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡋࡓࡔࡑࡓࠨੇ")):
  cli.bstack1l11ll11ll_opy_()
else:
  os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡌࡔࡕࡋࡔࠩੈ")] = bstack1lllll1_opy_ (u"ࠨࡶࡵࡹࡪ࠭੉")
bstack1111ll1111_opy_ = bstack1lllll1_opy_ (u"ࠩࠣࠤ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࠢࠣ࡭࡫࠮ࡰࡢࡩࡨࠤࡂࡃ࠽ࠡࡸࡲ࡭ࡩࠦ࠰ࠪࠢࡾࡠࡳࠦࠠࠡࡶࡵࡽࢀࡢ࡮ࠡࡥࡲࡲࡸࡺࠠࡧࡵࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮࡜ࠨࡨࡶࡠࠬ࠯࠻࡝ࡰࠣࠤࠥࠦࠠࡧࡵ࠱ࡥࡵࡶࡥ࡯ࡦࡉ࡭ࡱ࡫ࡓࡺࡰࡦࠬࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩ࠮ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡵࡥࡩ࡯ࡦࡨࡼ࠮ࠦࠫࠡࠤ࠽ࠦࠥ࠱ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭࠮ࡡࡸࡣ࡬ࡸࠥࡴࡥࡸࡒࡤ࡫ࡪ࠸࠮ࡦࡸࡤࡰࡺࡧࡴࡦࠪࠥࠬ࠮ࠦ࠽࠿ࠢࡾࢁࠧ࠲ࠠ࡝ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡪࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡥࡵࡣ࡬ࡰࡸࠨࡽ࡝ࠩࠬ࠭࠮ࡡࠢࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠥࡡ࠮ࠦࠫࠡࠤ࠯ࡠࡡࡴࠢࠪ࡞ࡱࠤࠥࠦࠠࡾࡥࡤࡸࡨ࡮ࠨࡦࡺࠬࡿࡡࡴࠠࠡࠢࠣࢁࡡࡴࠠࠡࡿ࡟ࡲࠥࠦ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠩ੊")
bstack1l1l1111ll_opy_ = bstack1lllll1_opy_ (u"ࠪࡠࡳ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭ࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠶ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡱࡡ࡬ࡲࡩ࡫ࡸࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠶ࡢࡢ࡮ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮ࡴ࡮࡬ࡧࡪ࠮࠰࠭ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷࠮ࡢ࡮ࡤࡱࡱࡷࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮ࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ࠯࠻࡝ࡰ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰࡯ࡥࡺࡴࡣࡩࠢࡀࠤࡦࡹࡹ࡯ࡥࠣࠬࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶ࠭ࠥࡃ࠾ࠡࡽ࡟ࡲࡱ࡫ࡴࠡࡥࡤࡴࡸࡁ࡜࡯ࡶࡵࡽࠥࢁ࡜࡯ࡥࡤࡴࡸࠦ࠽ࠡࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠬࡠࡳࠦࠠࡾࠢࡦࡥࡹࡩࡨࠩࡧࡻ࠭ࠥࢁ࡜࡯ࠢࠣࠤࠥࢃ࡜࡯ࠢࠣࡶࡪࡺࡵࡳࡰࠣࡥࡼࡧࡩࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰ࡦࡳࡳࡴࡥࡤࡶࠫࡿࡡࡴࠠࠡࠢࠣࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺ࠺ࠡࡢࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠨࢀ࡫࡮ࡤࡱࡧࡩ࡚ࡘࡉࡄࡱࡰࡴࡴࡴࡥ࡯ࡶࠫࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡨࡧࡰࡴࠫࠬࢁࡥ࠲࡜࡯ࠢࠣࠤࠥ࠴࠮࠯࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳ࡝ࡰࠣࠤࢂ࠯࡜࡯ࡿ࡟ࡲ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࠩੋ")
from ._version import __version__
bstack11l1l11ll1_opy_ = None
CONFIG = {}
bstack111ll1ll1l_opy_ = {}
bstack1ll1111l11_opy_ = {}
bstack1ll1lll1l_opy_ = None
bstack1l11lll11_opy_ = None
bstack11l11ll11_opy_ = None
bstack111lll111l_opy_ = -1
bstack11ll1l111l_opy_ = 0
bstack111ll11111_opy_ = bstack11l11ll111_opy_
bstack1l1lll1l1_opy_ = 1
bstack1ll1l111l1_opy_ = False
bstack1l1l1ll111_opy_ = False
bstack11l1ll1l1_opy_ = bstack1lllll1_opy_ (u"ࠫࠬੌ")
bstack11ll111ll1_opy_ = bstack1lllll1_opy_ (u"੍ࠬ࠭")
bstack11ll1lll11_opy_ = False
bstack1l11ll111_opy_ = True
bstack11l1llllll_opy_ = bstack1lllll1_opy_ (u"࠭ࠧ੎")
bstack1ll1ll11ll_opy_ = []
bstack1111ll1l1_opy_ = threading.Lock()
bstack1lll11l11_opy_ = threading.Lock()
bstack1ll1lll1ll_opy_ = bstack1lllll1_opy_ (u"ࠧࠨ੏")
bstack1l11ll1111_opy_ = False
bstack1l11l1ll11_opy_ = None
bstack1ll1l11l1_opy_ = None
bstack11lll11ll1_opy_ = None
bstack111llll111_opy_ = -1
bstack11ll1l11l_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠨࢀࠪ੐")), bstack1lllll1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩੑ"), bstack1lllll1_opy_ (u"ࠪ࠲ࡷࡵࡢࡰࡶ࠰ࡶࡪࡶ࡯ࡳࡶ࠰࡬ࡪࡲࡰࡦࡴ࠱࡮ࡸࡵ࡮ࠨ੒"))
bstack11lllll111_opy_ = 0
bstack1l1l1l1111_opy_ = 0
bstack111l1l11l_opy_ = []
bstack111llll1l1_opy_ = []
bstack11l1lll111_opy_ = []
bstack1l111llll_opy_ = []
bstack11lll1111_opy_ = bstack1lllll1_opy_ (u"ࠫࠬ੓")
bstack11llllllll_opy_ = bstack1lllll1_opy_ (u"ࠬ࠭੔")
bstack11l111l1ll_opy_ = False
bstack1111l1ll1_opy_ = False
bstack1111l11l1_opy_ = {}
bstack1ll11llll_opy_ = None
bstack1ll1lll1l1_opy_ = None
bstack1l111111l1_opy_ = None
bstack11llll1l11_opy_ = None
bstack11ll111111_opy_ = None
bstack1l11ll1l1_opy_ = None
bstack1lllll11ll_opy_ = None
bstack111ll1ll11_opy_ = None
bstack1lll1ll1l1_opy_ = None
bstack11l1l1l11l_opy_ = None
bstack1ll11l1ll1_opy_ = None
bstack11ll1ll1l_opy_ = None
bstack111l111111_opy_ = None
bstack1111l1llll_opy_ = None
bstack1lll111ll1_opy_ = None
bstack1ll11l111l_opy_ = None
bstack11l11111l_opy_ = None
bstack11lll1l11l_opy_ = None
bstack1lll1l1l1l_opy_ = None
bstack1l11lllll_opy_ = None
bstack1l1l1l1ll1_opy_ = None
bstack111l11l11_opy_ = None
bstack1l11lll111_opy_ = None
thread_local = threading.local()
bstack1l11lll1l_opy_ = False
bstack11l111l1l1_opy_ = bstack1lllll1_opy_ (u"ࠨࠢ੕")
logger = bstack1ll11111l1_opy_.get_logger(__name__, bstack111ll11111_opy_)
bstack11l1111l_opy_ = Config.bstack11111l1l_opy_()
percy = bstack1ll1l1ll1l_opy_()
bstack11l1l11ll_opy_ = bstack111lll11l1_opy_()
bstack1l11l11111_opy_ = bstack11ll1l11_opy_()
def bstack1lllllll1l_opy_():
  global CONFIG
  global bstack11l111l1ll_opy_
  global bstack11l1111l_opy_
  testContextOptions = bstack111l11l1l_opy_(CONFIG)
  if bstack11ll11111_opy_(CONFIG):
    if (bstack1lllll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ੖") in testContextOptions and str(testContextOptions[bstack1lllll1_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ੗")]).lower() == bstack1lllll1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ੘")):
      bstack11l111l1ll_opy_ = True
    bstack11l1111l_opy_.bstack1lll1lllll_opy_(testContextOptions.get(bstack1lllll1_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧਖ਼"), False))
  else:
    bstack11l111l1ll_opy_ = True
    bstack11l1111l_opy_.bstack1lll1lllll_opy_(True)
def bstack1ll11ll11l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11l1l1lll1_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1ll111ll_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1lllll1_opy_ (u"ࠦ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡨࡵ࡮ࡧ࡫ࡪࡪ࡮ࡲࡥࠣਗ਼") == args[i].lower() or bstack1lllll1_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡩ࡭࡬ࠨਜ਼") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack11l1llllll_opy_
      bstack11l1llllll_opy_ += bstack1lllll1_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡃࡰࡰࡩ࡭࡬ࡌࡩ࡭ࡧࠣࠫੜ") + shlex.quote(path)
      return path
  return None
bstack1l111l11l_opy_ = re.compile(bstack1lllll1_opy_ (u"ࡲࠣ࠰࠭ࡃࡡࠪࡻࠩ࠰࠭ࡃ࠮ࢃ࠮ࠫࡁࠥ੝"))
def bstack111l1ll11l_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l111l11l_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1lllll1_opy_ (u"ࠣࠦࡾࠦਫ਼") + group + bstack1lllll1_opy_ (u"ࠤࢀࠦ੟"), os.environ.get(group))
  return value
def bstack1111l11l1l_opy_():
  global bstack1l11lll111_opy_
  if bstack1l11lll111_opy_ is None:
        bstack1l11lll111_opy_ = bstack1l1ll111ll_opy_()
  bstack1ll11ll1l1_opy_ = bstack1l11lll111_opy_
  if bstack1ll11ll1l1_opy_ and os.path.exists(os.path.abspath(bstack1ll11ll1l1_opy_)):
    fileName = bstack1ll11ll1l1_opy_
  if bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧ੠") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ੡")])) and not bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡑࡥࡲ࡫ࠧ੢") in locals():
    fileName = os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࡤࡌࡉࡍࡇࠪ੣")]
  if bstack1lllll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡓࡧ࡭ࡦࠩ੤") in locals():
    bstack11l1l11_opy_ = os.path.abspath(fileName)
  else:
    bstack11l1l11_opy_ = bstack1lllll1_opy_ (u"ࠨࠩ੥")
  bstack1ll11l1l1_opy_ = os.getcwd()
  bstack1l1ll1l11l_opy_ = bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬ੦")
  bstack1llll1l111_opy_ = bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡥࡲࡲࠧ੧")
  while (not os.path.exists(bstack11l1l11_opy_)) and bstack1ll11l1l1_opy_ != bstack1lllll1_opy_ (u"ࠦࠧ੨"):
    bstack11l1l11_opy_ = os.path.join(bstack1ll11l1l1_opy_, bstack1l1ll1l11l_opy_)
    if not os.path.exists(bstack11l1l11_opy_):
      bstack11l1l11_opy_ = os.path.join(bstack1ll11l1l1_opy_, bstack1llll1l111_opy_)
    if bstack1ll11l1l1_opy_ != os.path.dirname(bstack1ll11l1l1_opy_):
      bstack1ll11l1l1_opy_ = os.path.dirname(bstack1ll11l1l1_opy_)
    else:
      bstack1ll11l1l1_opy_ = bstack1lllll1_opy_ (u"ࠧࠨ੩")
  bstack1l11lll111_opy_ = bstack11l1l11_opy_ if os.path.exists(bstack11l1l11_opy_) else None
  return bstack1l11lll111_opy_
def bstack1l11111ll_opy_(config):
    if bstack1lllll1_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬࠭੪") in config:
      config[bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ੫")] = config[bstack1lllll1_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࠨ੬")]
    if bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࡑࡳࡸ࡮ࡵ࡮ࡴࠩ੭") in config:
      config[bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ੮")] = config[bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࡓࡵࡺࡩࡰࡰࡶࠫ੯")]
def bstack111ll111l_opy_():
  bstack11l1l11_opy_ = bstack1111l11l1l_opy_()
  if not os.path.exists(bstack11l1l11_opy_):
    bstack1l1llllll_opy_(
      bstack11l1111ll1_opy_.format(os.getcwd()))
  try:
    with open(bstack11l1l11_opy_, bstack1lllll1_opy_ (u"ࠬࡸࠧੰ")) as stream:
      yaml.add_implicit_resolver(bstack1lllll1_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢੱ"), bstack1l111l11l_opy_)
      yaml.add_constructor(bstack1lllll1_opy_ (u"ࠢࠢࡲࡤࡸ࡭࡫ࡸࠣੲ"), bstack111l1ll11l_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1l11111ll_opy_(config)
      return config
  except:
    with open(bstack11l1l11_opy_, bstack1lllll1_opy_ (u"ࠨࡴࠪੳ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1l11111ll_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1l1llllll_opy_(bstack111ll111ll_opy_.format(str(exc)))
def bstack1l11l11l1l_opy_(config):
  bstack11l11l1l1_opy_ = bstack1l1111l11_opy_(config)
  for option in list(bstack11l11l1l1_opy_):
    if option.lower() in bstack1ll1l1l11_opy_ and option != bstack1ll1l1l11_opy_[option.lower()]:
      bstack11l11l1l1_opy_[bstack1ll1l1l11_opy_[option.lower()]] = bstack11l11l1l1_opy_[option]
      del bstack11l11l1l1_opy_[option]
  return config
def bstack11lll1l1ll_opy_():
  global bstack1ll1111l11_opy_
  for key, bstack11lll11l11_opy_ in bstack1lll111l1l_opy_.items():
    if isinstance(bstack11lll11l11_opy_, list):
      for var in bstack11lll11l11_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1ll1111l11_opy_[key] = os.environ[var]
          break
    elif bstack11lll11l11_opy_ in os.environ and os.environ[bstack11lll11l11_opy_] and str(os.environ[bstack11lll11l11_opy_]).strip():
      bstack1ll1111l11_opy_[key] = os.environ[bstack11lll11l11_opy_]
  if bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫੴ") in os.environ:
    bstack1ll1111l11_opy_[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧੵ")] = {}
    bstack1ll1111l11_opy_[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੶")][bstack1lllll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ੷")] = os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨ੸")]
def bstack11ll1l1111_opy_():
  global bstack111ll1ll1l_opy_
  global bstack11l1llllll_opy_
  bstack1111l1l1l1_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack1lllll1_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ੹").lower() == val.lower():
      bstack111ll1ll1l_opy_[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ੺")] = {}
      bstack111ll1ll1l_opy_[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੻")][bstack1lllll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ੼")] = sys.argv[idx + 1]
      bstack1111l1l1l1_opy_.extend([idx, idx + 1])
      break
  for key, bstack11l1llll11_opy_ in bstack11l111lll1_opy_.items():
    if isinstance(bstack11l1llll11_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack11l1llll11_opy_:
          if bstack1lllll1_opy_ (u"ࠫ࠲࠳ࠧ੽") + var.lower() == val.lower() and key not in bstack111ll1ll1l_opy_:
            bstack111ll1ll1l_opy_[key] = sys.argv[idx + 1]
            bstack11l1llllll_opy_ += bstack1lllll1_opy_ (u"ࠬࠦ࠭࠮ࠩ੾") + var + bstack1lllll1_opy_ (u"࠭ࠠࠨ੿") + shlex.quote(sys.argv[idx + 1])
            bstack1111l1l1l1_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack1lllll1_opy_ (u"ࠧ࠮࠯ࠪ઀") + bstack11l1llll11_opy_.lower() == val.lower() and key not in bstack111ll1ll1l_opy_:
          bstack111ll1ll1l_opy_[key] = sys.argv[idx + 1]
          bstack11l1llllll_opy_ += bstack1lllll1_opy_ (u"ࠨࠢ࠰࠱ࠬઁ") + bstack11l1llll11_opy_ + bstack1lllll1_opy_ (u"ࠩࠣࠫં") + shlex.quote(sys.argv[idx + 1])
          bstack1111l1l1l1_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack1111l1l1l1_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack1111l11ll_opy_(config):
  bstack11llll1ll1_opy_ = config.keys()
  for bstack1l1ll111l_opy_, bstack1l11l1l11_opy_ in bstack1111ll111l_opy_.items():
    if bstack1l11l1l11_opy_ in bstack11llll1ll1_opy_:
      config[bstack1l1ll111l_opy_] = config[bstack1l11l1l11_opy_]
      del config[bstack1l11l1l11_opy_]
  for bstack1l1ll111l_opy_, bstack1l11l1l11_opy_ in bstack1ll1111l1_opy_.items():
    if isinstance(bstack1l11l1l11_opy_, list):
      for bstack111ll1l11_opy_ in bstack1l11l1l11_opy_:
        if bstack111ll1l11_opy_ in bstack11llll1ll1_opy_:
          config[bstack1l1ll111l_opy_] = config[bstack111ll1l11_opy_]
          del config[bstack111ll1l11_opy_]
          break
    elif bstack1l11l1l11_opy_ in bstack11llll1ll1_opy_:
      config[bstack1l1ll111l_opy_] = config[bstack1l11l1l11_opy_]
      del config[bstack1l11l1l11_opy_]
  for bstack111ll1l11_opy_ in list(config):
    for bstack11l1111l1l_opy_ in bstack1lllll1l1l_opy_:
      if bstack111ll1l11_opy_.lower() == bstack11l1111l1l_opy_.lower() and bstack111ll1l11_opy_ != bstack11l1111l1l_opy_:
        config[bstack11l1111l1l_opy_] = config[bstack111ll1l11_opy_]
        del config[bstack111ll1l11_opy_]
  bstack1l1l1111l_opy_ = [{}]
  if not config.get(bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ઃ")):
    config[bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ઄")] = [{}]
  bstack1l1l1111l_opy_ = config[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨઅ")]
  for platform in bstack1l1l1111l_opy_:
    for bstack111ll1l11_opy_ in list(platform):
      for bstack11l1111l1l_opy_ in bstack1lllll1l1l_opy_:
        if bstack111ll1l11_opy_.lower() == bstack11l1111l1l_opy_.lower() and bstack111ll1l11_opy_ != bstack11l1111l1l_opy_:
          platform[bstack11l1111l1l_opy_] = platform[bstack111ll1l11_opy_]
          del platform[bstack111ll1l11_opy_]
  for bstack1l1ll111l_opy_, bstack1l11l1l11_opy_ in bstack1ll1111l1_opy_.items():
    for platform in bstack1l1l1111l_opy_:
      if isinstance(bstack1l11l1l11_opy_, list):
        for bstack111ll1l11_opy_ in bstack1l11l1l11_opy_:
          if bstack111ll1l11_opy_ in platform:
            platform[bstack1l1ll111l_opy_] = platform[bstack111ll1l11_opy_]
            del platform[bstack111ll1l11_opy_]
            break
      elif bstack1l11l1l11_opy_ in platform:
        platform[bstack1l1ll111l_opy_] = platform[bstack1l11l1l11_opy_]
        del platform[bstack1l11l1l11_opy_]
  for bstack1l111l1l1l_opy_ in bstack1llllll11l_opy_:
    if bstack1l111l1l1l_opy_ in config:
      if not bstack1llllll11l_opy_[bstack1l111l1l1l_opy_] in config:
        config[bstack1llllll11l_opy_[bstack1l111l1l1l_opy_]] = {}
      config[bstack1llllll11l_opy_[bstack1l111l1l1l_opy_]].update(config[bstack1l111l1l1l_opy_])
      del config[bstack1l111l1l1l_opy_]
  for platform in bstack1l1l1111l_opy_:
    for bstack1l111l1l1l_opy_ in bstack1llllll11l_opy_:
      if bstack1l111l1l1l_opy_ in list(platform):
        if not bstack1llllll11l_opy_[bstack1l111l1l1l_opy_] in platform:
          platform[bstack1llllll11l_opy_[bstack1l111l1l1l_opy_]] = {}
        platform[bstack1llllll11l_opy_[bstack1l111l1l1l_opy_]].update(platform[bstack1l111l1l1l_opy_])
        del platform[bstack1l111l1l1l_opy_]
  config = bstack1l11l11l1l_opy_(config)
  return config
def bstack1llll1111l_opy_(config):
  global bstack11ll111ll1_opy_
  bstack111ll1l1l1_opy_ = False
  if bstack1lllll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪઆ") in config and str(config[bstack1lllll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫઇ")]).lower() != bstack1lllll1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧઈ"):
    if bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ઉ") not in config or str(config[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧઊ")]).lower() == bstack1lllll1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪઋ"):
      config[bstack1lllll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫઌ")] = False
    else:
      bstack111l11111l_opy_ = bstack1l1l111l1_opy_()
      if bstack1lllll1_opy_ (u"࠭ࡩࡴࡖࡵ࡭ࡦࡲࡇࡳ࡫ࡧࠫઍ") in bstack111l11111l_opy_:
        if not bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ઎") in config:
          config[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬએ")] = {}
        config[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઐ")][bstack1lllll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬઑ")] = bstack1lllll1_opy_ (u"ࠫࡦࡺࡳ࠮ࡴࡨࡴࡪࡧࡴࡦࡴࠪ઒")
        bstack111ll1l1l1_opy_ = True
        bstack11ll111ll1_opy_ = config[bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩઓ")].get(bstack1lllll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨઔ"))
  if bstack11ll11111_opy_(config) and bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫક") in config and str(config[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬખ")]).lower() != bstack1lllll1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨગ") and not bstack111ll1l1l1_opy_:
    if not bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઘ") in config:
      config[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨઙ")] = {}
    if not config[bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩચ")].get(bstack1lllll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠪછ")) and not bstack1lllll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩજ") in config[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬઝ")]:
      bstack1llll11l_opy_ = datetime.datetime.now()
      bstack11l111ll1_opy_ = bstack1llll11l_opy_.strftime(bstack1lllll1_opy_ (u"ࠩࠨࡨࡤࠫࡢࡠࠧࡋࠩࡒ࠭ઞ"))
      hostname = socket.gethostname()
      bstack1lll11ll1l_opy_ = bstack1lllll1_opy_ (u"ࠪࠫટ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1lllll1_opy_ (u"ࠫࢀࢃ࡟ࡼࡿࡢࡿࢂ࠭ઠ").format(bstack11l111ll1_opy_, hostname, bstack1lll11ll1l_opy_)
      config[bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩડ")][bstack1lllll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨઢ")] = identifier
    bstack11ll111ll1_opy_ = config[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫણ")].get(bstack1lllll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪત"))
  return config
def bstack1ll1ll11l_opy_():
  bstack1l1l11lll_opy_ =  bstack1ll111111l_opy_()[bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠨથ")]
  return bstack1l1l11lll_opy_ if bstack1l1l11lll_opy_ else -1
def bstack1llll1ll1l_opy_(bstack1l1l11lll_opy_):
  global CONFIG
  if not bstack1lllll1_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬદ") in CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ધ")]:
    return
  CONFIG[bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧન")] = CONFIG[bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ઩")].replace(
    bstack1lllll1_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩપ"),
    str(bstack1l1l11lll_opy_)
  )
def bstack1l1lll1ll_opy_():
  global CONFIG
  if not bstack1lllll1_opy_ (u"ࠨࠦࡾࡈࡆ࡚ࡅࡠࡖࡌࡑࡊࢃࠧફ") in CONFIG[bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫબ")]:
    return
  bstack1llll11l_opy_ = datetime.datetime.now()
  bstack11l111ll1_opy_ = bstack1llll11l_opy_.strftime(bstack1lllll1_opy_ (u"ࠪࠩࡩ࠳ࠥࡣ࠯ࠨࡌ࠿ࠫࡍࠨભ"))
  CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭મ")] = CONFIG[bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧય")].replace(
    bstack1lllll1_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬર"),
    bstack11l111ll1_opy_
  )
def bstack1l1llll11l_opy_():
  global CONFIG
  if bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઱") in CONFIG and not bool(CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪલ")]):
    del CONFIG[bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫળ")]
    return
  if not bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ઴") in CONFIG:
    CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭વ")] = bstack1lllll1_opy_ (u"ࠬࠩࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨશ")
  if bstack1lllll1_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬષ") in CONFIG[bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩસ")]:
    bstack1l1lll1ll_opy_()
    os.environ[bstack1lllll1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬહ")] = CONFIG[bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ઺")]
  if not bstack1lllll1_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬ઻") in CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ઼࠭")]:
    return
  bstack1l1l11lll_opy_ = bstack1lllll1_opy_ (u"ࠬ࠭ઽ")
  bstack1l1ll11l1_opy_ = bstack1ll1ll11l_opy_()
  if bstack1l1ll11l1_opy_ != -1:
    bstack1l1l11lll_opy_ = bstack1lllll1_opy_ (u"࠭ࡃࡊࠢࠪા") + str(bstack1l1ll11l1_opy_)
  if bstack1l1l11lll_opy_ == bstack1lllll1_opy_ (u"ࠧࠨિ"):
    bstack1l111111l_opy_ = bstack11l11l11l1_opy_(CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫી")])
    if bstack1l111111l_opy_ != -1:
      bstack1l1l11lll_opy_ = str(bstack1l111111l_opy_)
  if bstack1l1l11lll_opy_:
    bstack1llll1ll1l_opy_(bstack1l1l11lll_opy_)
    os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭ુ")] = CONFIG[bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૂ")]
def bstack11l11l1ll_opy_(bstack111l1ll1ll_opy_, bstack11lll111ll_opy_, path):
  json_data = {
    bstack1lllll1_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨૃ"): bstack11lll111ll_opy_
  }
  if os.path.exists(path):
    bstack1l11l1l1ll_opy_ = json.load(open(path, bstack1lllll1_opy_ (u"ࠬࡸࡢࠨૄ")))
  else:
    bstack1l11l1l1ll_opy_ = {}
  bstack1l11l1l1ll_opy_[bstack111l1ll1ll_opy_] = json_data
  with open(path, bstack1lllll1_opy_ (u"ࠨࡷࠬࠤૅ")) as outfile:
    json.dump(bstack1l11l1l1ll_opy_, outfile)
def bstack11l11l11l1_opy_(bstack111l1ll1ll_opy_):
  bstack111l1ll1ll_opy_ = str(bstack111l1ll1ll_opy_)
  bstack1ll1l1l1l1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠧࡿࠩ૆")), bstack1lllll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨે"))
  try:
    if not os.path.exists(bstack1ll1l1l1l1_opy_):
      os.makedirs(bstack1ll1l1l1l1_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠩࢁࠫૈ")), bstack1lllll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪૉ"), bstack1lllll1_opy_ (u"ࠫ࠳ࡨࡵࡪ࡮ࡧ࠱ࡳࡧ࡭ࡦ࠯ࡦࡥࡨ࡮ࡥ࠯࡬ࡶࡳࡳ࠭૊"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1lllll1_opy_ (u"ࠬࡽࠧો")):
        pass
      with open(file_path, bstack1lllll1_opy_ (u"ࠨࡷࠬࠤૌ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1lllll1_opy_ (u"ࠧࡳ્ࠩ")) as bstack1ll1ll111_opy_:
      bstack11lll11l1l_opy_ = json.load(bstack1ll1ll111_opy_)
    if bstack111l1ll1ll_opy_ in bstack11lll11l1l_opy_:
      bstack111l11lll1_opy_ = bstack11lll11l1l_opy_[bstack111l1ll1ll_opy_][bstack1lllll1_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૎")]
      bstack1lll111lll_opy_ = int(bstack111l11lll1_opy_) + 1
      bstack11l11l1ll_opy_(bstack111l1ll1ll_opy_, bstack1lll111lll_opy_, file_path)
      return bstack1lll111lll_opy_
    else:
      bstack11l11l1ll_opy_(bstack111l1ll1ll_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1lll1llll1_opy_.format(str(e)))
    return -1
def bstack11l1l1llll_opy_(config):
  if not config[bstack1lllll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ૏")] or not config[bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ૐ")]:
    return True
  else:
    return False
def bstack11llllll1_opy_(config, index=0):
  global bstack11ll1lll11_opy_
  bstack1lll1ll1ll_opy_ = {}
  caps = bstack1ll1llll1_opy_ + bstack1l1l1l11l1_opy_
  if config.get(bstack1lllll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ૑"), False):
    bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ૒")] = True
    bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ૓")] = config.get(bstack1lllll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ૔"), {})
  if bstack11ll1lll11_opy_:
    caps += bstack11l1l1l11_opy_
  for key in config:
    if key in caps + [bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૕")]:
      continue
    bstack1lll1ll1ll_opy_[key] = config[key]
  if bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૖") in config:
    for bstack11l1l11111_opy_ in config[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૗")][index]:
      if bstack11l1l11111_opy_ in caps:
        continue
      bstack1lll1ll1ll_opy_[bstack11l1l11111_opy_] = config[bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૘")][index][bstack11l1l11111_opy_]
  bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"ࠬ࡮࡯ࡴࡶࡑࡥࡲ࡫ࠧ૙")] = socket.gethostname()
  if bstack1lllll1_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧ૚") in bstack1lll1ll1ll_opy_:
    del (bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ૛")])
  return bstack1lll1ll1ll_opy_
def bstack1l1l11l1l_opy_(config):
  global bstack11ll1lll11_opy_
  bstack1lll1l111_opy_ = {}
  caps = bstack1l1l1l11l1_opy_
  if bstack11ll1lll11_opy_:
    caps += bstack11l1l1l11_opy_
  for key in caps:
    if key in config:
      bstack1lll1l111_opy_[key] = config[key]
  return bstack1lll1l111_opy_
def bstack111llll11l_opy_(bstack1lll1ll1ll_opy_, bstack1lll1l111_opy_):
  bstack1l1ll11l11_opy_ = {}
  for key in bstack1lll1ll1ll_opy_.keys():
    if key in bstack1111ll111l_opy_:
      bstack1l1ll11l11_opy_[bstack1111ll111l_opy_[key]] = bstack1lll1ll1ll_opy_[key]
    else:
      bstack1l1ll11l11_opy_[key] = bstack1lll1ll1ll_opy_[key]
  for key in bstack1lll1l111_opy_:
    if key in bstack1111ll111l_opy_:
      bstack1l1ll11l11_opy_[bstack1111ll111l_opy_[key]] = bstack1lll1l111_opy_[key]
    else:
      bstack1l1ll11l11_opy_[key] = bstack1lll1l111_opy_[key]
  return bstack1l1ll11l11_opy_
def bstack11lll111l1_opy_(config, index=0):
  global bstack11ll1lll11_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11ll11l1l1_opy_ = bstack1111llll11_opy_(bstack11llll1lll_opy_, config, logger)
  bstack1lll1l111_opy_ = bstack1l1l11l1l_opy_(config)
  bstack1l1lll1111_opy_ = bstack1l1l1l11l1_opy_
  bstack1l1lll1111_opy_ += bstack11ll11l1ll_opy_
  bstack1lll1l111_opy_ = update(bstack1lll1l111_opy_, bstack11ll11l1l1_opy_)
  if bstack11ll1lll11_opy_:
    bstack1l1lll1111_opy_ += bstack11l1l1l11_opy_
  if bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૜") in config:
    if bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ૝") in config[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૞")][index]:
      caps[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ૟")] = config[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૠ")][index][bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫૡ")]
    if bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨૢ") in config[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫૣ")][index]:
      caps[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ૤")] = str(config[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૥")][index][bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ૦")])
    bstack1l11l1111l_opy_ = bstack1111llll11_opy_(bstack11llll1lll_opy_, config[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૧")][index], logger)
    bstack1l1lll1111_opy_ += list(bstack1l11l1111l_opy_.keys())
    for bstack1ll11ll1ll_opy_ in bstack1l1lll1111_opy_:
      if bstack1ll11ll1ll_opy_ in config[bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૨")][index]:
        if bstack1ll11ll1ll_opy_ == bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ૩"):
          try:
            bstack1l11l1111l_opy_[bstack1ll11ll1ll_opy_] = str(config[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૪")][index][bstack1ll11ll1ll_opy_] * 1.0)
          except:
            bstack1l11l1111l_opy_[bstack1ll11ll1ll_opy_] = str(config[bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૫")][index][bstack1ll11ll1ll_opy_])
        else:
          bstack1l11l1111l_opy_[bstack1ll11ll1ll_opy_] = config[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૬")][index][bstack1ll11ll1ll_opy_]
        del (config[bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૭")][index][bstack1ll11ll1ll_opy_])
    bstack1lll1l111_opy_ = update(bstack1lll1l111_opy_, bstack1l11l1111l_opy_)
  bstack1lll1ll1ll_opy_ = bstack11llllll1_opy_(config, index)
  for bstack111ll1l11_opy_ in bstack1l1l1l11l1_opy_ + list(bstack11ll11l1l1_opy_.keys()):
    if bstack111ll1l11_opy_ in bstack1lll1ll1ll_opy_:
      bstack1lll1l111_opy_[bstack111ll1l11_opy_] = bstack1lll1ll1ll_opy_[bstack111ll1l11_opy_]
      del (bstack1lll1ll1ll_opy_[bstack111ll1l11_opy_])
  if bstack1111l1lll_opy_(config):
    bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬ૮")] = True
    caps.update(bstack1lll1l111_opy_)
    caps[bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ૯")] = bstack1lll1ll1ll_opy_
  else:
    bstack1lll1ll1ll_opy_[bstack1lllll1_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧ૰")] = False
    caps.update(bstack111llll11l_opy_(bstack1lll1ll1ll_opy_, bstack1lll1l111_opy_))
    if bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭૱") in caps:
      caps[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪ૲")] = caps[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ૳")]
      del (caps[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ૴")])
    if bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭૵") in caps:
      caps[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ૶")] = caps[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ૷")]
      del (caps[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ૸")])
  return caps
def bstack1lll1ll111_opy_():
  global bstack1ll1lll1ll_opy_
  global CONFIG
  if bstack11l1l1lll1_opy_() <= version.parse(bstack1lllll1_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩૹ")):
    if bstack1ll1lll1ll_opy_ != bstack1lllll1_opy_ (u"ࠪࠫૺ"):
      return bstack1lllll1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧૻ") + bstack1ll1lll1ll_opy_ + bstack1lllll1_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤૼ")
    return bstack111l1ll111_opy_
  if bstack1ll1lll1ll_opy_ != bstack1lllll1_opy_ (u"࠭ࠧ૽"):
    return bstack1lllll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤ૾") + bstack1ll1lll1ll_opy_ + bstack1lllll1_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤ૿")
  return bstack1l11lll1l1_opy_
def bstack1ll1ll1l1l_opy_(options):
  return hasattr(options, bstack1lllll1_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪ଀"))
def update(d, u):
  for k, v in u.items():
    if isinstance(v, collections.abc.Mapping):
      d[k] = update(d.get(k, {}), v)
    else:
      if isinstance(v, list):
        d[k] = d.get(k, []) + v
      else:
        d[k] = v
  return d
def bstack11l1ll11ll_opy_(options, bstack1ll11lll1l_opy_):
  for bstack11ll1l11ll_opy_ in bstack1ll11lll1l_opy_:
    if bstack11ll1l11ll_opy_ in [bstack1lllll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଁ"), bstack1lllll1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨଂ")]:
      continue
    if bstack11ll1l11ll_opy_ in options._experimental_options:
      options._experimental_options[bstack11ll1l11ll_opy_] = update(options._experimental_options[bstack11ll1l11ll_opy_],
                                                         bstack1ll11lll1l_opy_[bstack11ll1l11ll_opy_])
    else:
      options.add_experimental_option(bstack11ll1l11ll_opy_, bstack1ll11lll1l_opy_[bstack11ll1l11ll_opy_])
  if bstack1lllll1_opy_ (u"ࠬࡧࡲࡨࡵࠪଃ") in bstack1ll11lll1l_opy_:
    for arg in bstack1ll11lll1l_opy_[bstack1lllll1_opy_ (u"࠭ࡡࡳࡩࡶࠫ଄")]:
      options.add_argument(arg)
    del (bstack1ll11lll1l_opy_[bstack1lllll1_opy_ (u"ࠧࡢࡴࡪࡷࠬଅ")])
  if bstack1lllll1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬଆ") in bstack1ll11lll1l_opy_:
    for ext in bstack1ll11lll1l_opy_[bstack1lllll1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ଇ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1ll11lll1l_opy_[bstack1lllll1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧଈ")])
def bstack1lll1lll11_opy_(options, bstack1l111ll11l_opy_):
  if bstack1lllll1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪଉ") in bstack1l111ll11l_opy_:
    for bstack111l111lll_opy_ in bstack1l111ll11l_opy_[bstack1lllll1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫଊ")]:
      if bstack111l111lll_opy_ in options._preferences:
        options._preferences[bstack111l111lll_opy_] = update(options._preferences[bstack111l111lll_opy_], bstack1l111ll11l_opy_[bstack1lllll1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬଋ")][bstack111l111lll_opy_])
      else:
        options.set_preference(bstack111l111lll_opy_, bstack1l111ll11l_opy_[bstack1lllll1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ଌ")][bstack111l111lll_opy_])
  if bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭଍") in bstack1l111ll11l_opy_:
    for arg in bstack1l111ll11l_opy_[bstack1lllll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ଎")]:
      options.add_argument(arg)
def bstack1l111l1l11_opy_(options, bstack11l111111_opy_):
  if bstack1lllll1_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫଏ") in bstack11l111111_opy_:
    options.use_webview(bool(bstack11l111111_opy_[bstack1lllll1_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬଐ")]))
  bstack11l1ll11ll_opy_(options, bstack11l111111_opy_)
def bstack1lllllllll_opy_(options, bstack1lll11ll1_opy_):
  for bstack11111l1l1_opy_ in bstack1lll11ll1_opy_:
    if bstack11111l1l1_opy_ in [bstack1lllll1_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩ଑"), bstack1lllll1_opy_ (u"࠭ࡡࡳࡩࡶࠫ଒")]:
      continue
    options.set_capability(bstack11111l1l1_opy_, bstack1lll11ll1_opy_[bstack11111l1l1_opy_])
  if bstack1lllll1_opy_ (u"ࠧࡢࡴࡪࡷࠬଓ") in bstack1lll11ll1_opy_:
    for arg in bstack1lll11ll1_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଔ")]:
      options.add_argument(arg)
  if bstack1lllll1_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭କ") in bstack1lll11ll1_opy_:
    options.bstack11l1111111_opy_(bool(bstack1lll11ll1_opy_[bstack1lllll1_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧଖ")]))
def bstack11ll1lllll_opy_(options, bstack1111lll1ll_opy_):
  for bstack1ll1l11l1l_opy_ in bstack1111lll1ll_opy_:
    if bstack1ll1l11l1l_opy_ in [bstack1lllll1_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨଗ"), bstack1lllll1_opy_ (u"ࠬࡧࡲࡨࡵࠪଘ")]:
      continue
    options._options[bstack1ll1l11l1l_opy_] = bstack1111lll1ll_opy_[bstack1ll1l11l1l_opy_]
  if bstack1lllll1_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪଙ") in bstack1111lll1ll_opy_:
    for bstack1lll11111l_opy_ in bstack1111lll1ll_opy_[bstack1lllll1_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଚ")]:
      options.bstack1l111ll1ll_opy_(
        bstack1lll11111l_opy_, bstack1111lll1ll_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬଛ")][bstack1lll11111l_opy_])
  if bstack1lllll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧଜ") in bstack1111lll1ll_opy_:
    for arg in bstack1111lll1ll_opy_[bstack1lllll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଝ")]:
      options.add_argument(arg)
def bstack1ll111ll1_opy_(options, caps):
  if not hasattr(options, bstack1lllll1_opy_ (u"ࠫࡐࡋ࡙ࠨଞ")):
    return
  if options.KEY == bstack1lllll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪଟ"):
    options = bstack1lll1lll1_opy_.bstack1l1l1lll1_opy_(bstack1ll1l1l111_opy_=options, config=CONFIG)
  if options.KEY == bstack1lllll1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫଠ") and options.KEY in caps:
    bstack11l1ll11ll_opy_(options, caps[bstack1lllll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬଡ")])
  elif options.KEY == bstack1lllll1_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ଢ") and options.KEY in caps:
    bstack1lll1lll11_opy_(options, caps[bstack1lllll1_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧଣ")])
  elif options.KEY == bstack1lllll1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫତ") and options.KEY in caps:
    bstack1lllllllll_opy_(options, caps[bstack1lllll1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬଥ")])
  elif options.KEY == bstack1lllll1_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ଦ") and options.KEY in caps:
    bstack1l111l1l11_opy_(options, caps[bstack1lllll1_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧଧ")])
  elif options.KEY == bstack1lllll1_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ନ") and options.KEY in caps:
    bstack11ll1lllll_opy_(options, caps[bstack1lllll1_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ଩")])
def bstack1ll1ll1l11_opy_(caps):
  global bstack11ll1lll11_opy_
  if isinstance(os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪପ")), str):
    bstack11ll1lll11_opy_ = eval(os.getenv(bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫଫ")))
  if bstack11ll1lll11_opy_:
    if bstack1ll11ll11l_opy_() < version.parse(bstack1lllll1_opy_ (u"ࠫ࠷࠴࠳࠯࠲ࠪବ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1lllll1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬଭ")
    if bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫମ") in caps:
      browser = caps[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬଯ")]
    elif bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩର") in caps:
      browser = caps[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪ଱")]
    browser = str(browser).lower()
    if browser == bstack1lllll1_opy_ (u"ࠪ࡭ࡵ࡮࡯࡯ࡧࠪଲ") or browser == bstack1lllll1_opy_ (u"ࠫ࡮ࡶࡡࡥࠩଳ"):
      browser = bstack1lllll1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬ଴")
    if browser == bstack1lllll1_opy_ (u"࠭ࡳࡢ࡯ࡶࡹࡳ࡭ࠧଵ"):
      browser = bstack1lllll1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧଶ")
    if browser not in [bstack1lllll1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨଷ"), bstack1lllll1_opy_ (u"ࠩࡨࡨ࡬࡫ࠧସ"), bstack1lllll1_opy_ (u"ࠪ࡭ࡪ࠭ହ"), bstack1lllll1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫ଺"), bstack1lllll1_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭଻")]:
      return None
    try:
      package = bstack1lllll1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࢀࢃ࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ଼").format(browser)
      name = bstack1lllll1_opy_ (u"ࠧࡐࡲࡷ࡭ࡴࡴࡳࠨଽ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1ll1ll1l1l_opy_(options):
        return None
      for bstack111ll1l11_opy_ in caps.keys():
        options.set_capability(bstack111ll1l11_opy_, caps[bstack111ll1l11_opy_])
      bstack1ll111ll1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack11ll1llll_opy_(options, bstack111lll1l1_opy_):
  if not bstack1ll1ll1l1l_opy_(options):
    return
  for bstack111ll1l11_opy_ in bstack111lll1l1_opy_.keys():
    if bstack111ll1l11_opy_ in bstack11ll11l1ll_opy_:
      continue
    if bstack111ll1l11_opy_ in options._caps and type(options._caps[bstack111ll1l11_opy_]) in [dict, list]:
      options._caps[bstack111ll1l11_opy_] = update(options._caps[bstack111ll1l11_opy_], bstack111lll1l1_opy_[bstack111ll1l11_opy_])
    else:
      options.set_capability(bstack111ll1l11_opy_, bstack111lll1l1_opy_[bstack111ll1l11_opy_])
  bstack1ll111ll1_opy_(options, bstack111lll1l1_opy_)
  if bstack1lllll1_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧା") in options._caps:
    if options._caps[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧି")] and options._caps[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨୀ")].lower() != bstack1lllll1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬୁ"):
      del options._caps[bstack1lllll1_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡧࡩࡧࡻࡧࡨࡧࡵࡅࡩࡪࡲࡦࡵࡶࠫୂ")]
def bstack11l111llll_opy_(proxy_config):
  if bstack1lllll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪୃ") in proxy_config:
    proxy_config[bstack1lllll1_opy_ (u"ࠧࡴࡵ࡯ࡔࡷࡵࡸࡺࠩୄ")] = proxy_config[bstack1lllll1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ୅")]
    del (proxy_config[bstack1lllll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭୆")])
  if bstack1lllll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭େ") in proxy_config and proxy_config[bstack1lllll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧୈ")].lower() != bstack1lllll1_opy_ (u"ࠬࡪࡩࡳࡧࡦࡸࠬ୉"):
    proxy_config[bstack1lllll1_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩ୊")] = bstack1lllll1_opy_ (u"ࠧ࡮ࡣࡱࡹࡦࡲࠧୋ")
  if bstack1lllll1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡁࡶࡶࡲࡧࡴࡴࡦࡪࡩࡘࡶࡱ࠭ୌ") in proxy_config:
    proxy_config[bstack1lllll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩ୍ࠬ")] = bstack1lllll1_opy_ (u"ࠪࡴࡦࡩࠧ୎")
  return proxy_config
def bstack1lll11lll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1lllll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ୏") in config:
    return proxy
  config[bstack1lllll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ୐")] = bstack11l111llll_opy_(config[bstack1lllll1_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୑")])
  if proxy == None:
    proxy = Proxy(config[bstack1lllll1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭୒")])
  return proxy
def bstack11ll111l11_opy_(self):
  global CONFIG
  global bstack11ll1ll1l_opy_
  try:
    proxy = bstack1ll1ll1lll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1lllll1_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭୓")):
        proxies = bstack1l1l1l111l_opy_(proxy, bstack1lll1ll111_opy_())
        if len(proxies) > 0:
          protocol, bstack11lllll1l_opy_ = proxies.popitem()
          if bstack1lllll1_opy_ (u"ࠤ࠽࠳࠴ࠨ୔") in bstack11lllll1l_opy_:
            return bstack11lllll1l_opy_
          else:
            return bstack1lllll1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ୕") + bstack11lllll1l_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡱࡴࡲࡼࡾࠦࡵࡳ࡮ࠣ࠾ࠥࢁࡽࠣୖ").format(str(e)))
  return bstack11ll1ll1l_opy_(self)
def bstack1l1l11l111_opy_():
  global CONFIG
  return bstack11lll1lll_opy_(CONFIG) and bstack1ll11ll1l_opy_() and bstack11l1l1lll1_opy_() >= version.parse(bstack1l111ll1l1_opy_)
def bstack111llll11_opy_():
  global CONFIG
  return (bstack1lllll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨୗ") in CONFIG or bstack1lllll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ୘") in CONFIG) and bstack11l1l1lll_opy_()
def bstack1l1111l11_opy_(config):
  bstack11l11l1l1_opy_ = {}
  if bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୙") in config:
    bstack11l11l1l1_opy_ = config[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୚")]
  if bstack1lllll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୛") in config:
    bstack11l11l1l1_opy_ = config[bstack1lllll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩଡ଼")]
  proxy = bstack1ll1ll1lll_opy_(config)
  if proxy:
    if proxy.endswith(bstack1lllll1_opy_ (u"ࠫ࠳ࡶࡡࡤࠩଢ଼")) and os.path.isfile(proxy):
      bstack11l11l1l1_opy_[bstack1lllll1_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨ୞")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1lllll1_opy_ (u"࠭࠮ࡱࡣࡦࠫୟ")):
        proxies = bstack111l111l1_opy_(config, bstack1lll1ll111_opy_())
        if len(proxies) > 0:
          protocol, bstack11lllll1l_opy_ = proxies.popitem()
          if bstack1lllll1_opy_ (u"ࠢ࠻࠱࠲ࠦୠ") in bstack11lllll1l_opy_:
            parsed_url = urlparse(bstack11lllll1l_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1lllll1_opy_ (u"ࠣ࠼࠲࠳ࠧୡ") + bstack11lllll1l_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack11l11l1l1_opy_[bstack1lllll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬୢ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack11l11l1l1_opy_[bstack1lllll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭ୣ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack11l11l1l1_opy_[bstack1lllll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧ୤")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack11l11l1l1_opy_[bstack1lllll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨ୥")] = str(parsed_url.password)
  return bstack11l11l1l1_opy_
def bstack111l11l1l_opy_(config):
  if bstack1lllll1_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫ୦") in config:
    return config[bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬ୧")]
  return {}
def bstack1l1ll1l111_opy_(caps):
  global bstack11ll111ll1_opy_
  if bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ୨") in caps:
    caps[bstack1lllll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ୩")][bstack1lllll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩ୪")] = True
    if bstack11ll111ll1_opy_:
      caps[bstack1lllll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ୫")][bstack1lllll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ୬")] = bstack11ll111ll1_opy_
  else:
    caps[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫ୭")] = True
    if bstack11ll111ll1_opy_:
      caps[bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ୮")] = bstack11ll111ll1_opy_
@measure(event_name=EVENTS.bstack1ll1ll111l_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack111ll1l11l_opy_():
  global CONFIG
  if not bstack11ll11111_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ୯") in CONFIG and bstack11l11l111l_opy_(CONFIG[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭୰")]):
    if (
      bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧୱ") in CONFIG
      and bstack11l11l111l_opy_(CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୲")].get(bstack1lllll1_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩ୳")))
    ):
      logger.debug(bstack1lllll1_opy_ (u"ࠨࡌࡰࡥࡤࡰࠥࡨࡩ࡯ࡣࡵࡽࠥࡴ࡯ࡵࠢࡶࡸࡦࡸࡴࡦࡦࠣࡥࡸࠦࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡥ࡯ࡣࡥࡰࡪࡪࠢ୴"))
      return
    bstack11l11l1l1_opy_ = bstack1l1111l11_opy_(CONFIG)
    bstack1l1l11l1ll_opy_(CONFIG[bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ୵")], bstack11l11l1l1_opy_)
def bstack1l1l11l1ll_opy_(key, bstack11l11l1l1_opy_):
  global bstack11l1l11ll1_opy_
  logger.info(bstack111l11lll_opy_)
  try:
    bstack11l1l11ll1_opy_ = Local()
    bstack1ll1l1lll_opy_ = {bstack1lllll1_opy_ (u"ࠨ࡭ࡨࡽࠬ୶"): key}
    bstack1ll1l1lll_opy_.update(bstack11l11l1l1_opy_)
    logger.debug(bstack111l1111l1_opy_.format(str(bstack1ll1l1lll_opy_)).replace(key, bstack1lllll1_opy_ (u"ࠩ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭୷")))
    bstack11l1l11ll1_opy_.start(**bstack1ll1l1lll_opy_)
    if bstack11l1l11ll1_opy_.isRunning():
      logger.info(bstack11ll1l1ll_opy_)
  except Exception as e:
    bstack1l1llllll_opy_(bstack1lll1l11l1_opy_.format(str(e)))
def bstack11l11111l1_opy_():
  global bstack11l1l11ll1_opy_
  if bstack11l1l11ll1_opy_.isRunning():
    logger.info(bstack11lll11111_opy_)
    bstack11l1l11ll1_opy_.stop()
  bstack11l1l11ll1_opy_ = None
def bstack1111ll1l11_opy_(bstack111ll11ll_opy_=[]):
  global CONFIG
  bstack1111111ll_opy_ = []
  bstack11l1ll1l11_opy_ = [bstack1lllll1_opy_ (u"ࠪࡳࡸ࠭୸"), bstack1lllll1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧ୹"), bstack1lllll1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩ୺"), bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ୻"), bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ୼"), bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ୽")]
  try:
    for err in bstack111ll11ll_opy_:
      bstack1111llll1l_opy_ = {}
      for k in bstack11l1ll1l11_opy_:
        val = CONFIG[bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ୾")][int(err[bstack1lllll1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ୿")])].get(k)
        if val:
          bstack1111llll1l_opy_[k] = val
      if(err[bstack1lllll1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ஀")] != bstack1lllll1_opy_ (u"ࠬ࠭஁")):
        bstack1111llll1l_opy_[bstack1lllll1_opy_ (u"࠭ࡴࡦࡵࡷࡷࠬஂ")] = {
          err[bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬஃ")]: err[bstack1lllll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ஄")]
        }
        bstack1111111ll_opy_.append(bstack1111llll1l_opy_)
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫ࡵࡲ࡮ࡣࡷࡸ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵ࠼ࠣࠫஅ") + str(e))
  finally:
    return bstack1111111ll_opy_
def bstack1ll11lll1_opy_(file_name):
  bstack111ll11lll_opy_ = []
  try:
    bstack1l1111l111_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1l1111l111_opy_):
      with open(bstack1l1111l111_opy_) as f:
        bstack1ll1lll111_opy_ = json.load(f)
        bstack111ll11lll_opy_ = bstack1ll1lll111_opy_
      os.remove(bstack1l1111l111_opy_)
    return bstack111ll11lll_opy_
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡩ࡯ࡦ࡬ࡲ࡬ࠦࡥࡳࡴࡲࡶࠥࡲࡩࡴࡶ࠽ࠤࠬஆ") + str(e))
    return bstack111ll11lll_opy_
def bstack11l111ll11_opy_():
  try:
      from bstack_utils.constants import bstack11111111l_opy_, EVENTS
      from bstack_utils.helper import bstack1l1111111_opy_, get_host_info, bstack11l1111l_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack1llll11lll_opy_ = os.path.join(os.getcwd(), bstack1lllll1_opy_ (u"ࠫࡱࡵࡧࠨஇ"), bstack1lllll1_opy_ (u"ࠬࡱࡥࡺ࠯ࡰࡩࡹࡸࡩࡤࡵ࠱࡮ࡸࡵ࡮ࠨஈ"))
      lock = FileLock(bstack1llll11lll_opy_+bstack1lllll1_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧஉ"))
      def bstack1l1l111l_opy_():
          try:
              with lock:
                  with open(bstack1llll11lll_opy_, bstack1lllll1_opy_ (u"ࠢࡳࠤஊ"), encoding=bstack1lllll1_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢ஋")) as file:
                      data = json.load(file)
                      config = {
                          bstack1lllll1_opy_ (u"ࠤ࡫ࡩࡦࡪࡥࡳࡵࠥ஌"): {
                              bstack1lllll1_opy_ (u"ࠥࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠤ஍"): bstack1lllll1_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠢஎ"),
                          }
                      }
                      bstack1llll111ll_opy_ = datetime.utcnow()
                      bstack1llll11l_opy_ = bstack1llll111ll_opy_.strftime(bstack1lllll1_opy_ (u"࡙ࠧࠫ࠮ࠧࡰ࠱ࠪࡪࡔࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪ࡛ࠥࡔࡄࠤஏ"))
                      test_id = os.environ.get(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫஐ")) if os.environ.get(bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ஑")) else bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥஒ"))
                      payload = {
                          bstack1lllll1_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࠨஓ"): bstack1lllll1_opy_ (u"ࠥࡷࡩࡱ࡟ࡦࡸࡨࡲࡹࡹࠢஔ"),
                          bstack1lllll1_opy_ (u"ࠦࡩࡧࡴࡢࠤக"): {
                              bstack1lllll1_opy_ (u"ࠧࡺࡥࡴࡶ࡫ࡹࡧࡥࡵࡶ࡫ࡧࠦ஖"): test_id,
                              bstack1lllll1_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡪ࡟ࡥࡣࡼࠦ஗"): bstack1llll11l_opy_,
                              bstack1lllll1_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࠦ஘"): bstack1lllll1_opy_ (u"ࠣࡕࡇࡏࡋ࡫ࡡࡵࡷࡵࡩࡕ࡫ࡲࡧࡱࡵࡱࡦࡴࡣࡦࠤங"),
                              bstack1lllll1_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠ࡬ࡶࡳࡳࠨச"): {
                                  bstack1lllll1_opy_ (u"ࠥࡱࡪࡧࡳࡶࡴࡨࡷࠧ஛"): data,
                                  bstack1lllll1_opy_ (u"ࠦࡸࡪ࡫ࡓࡷࡱࡍࡩࠨஜ"): bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢ஝"))
                              },
                              bstack1lllll1_opy_ (u"ࠨࡵࡴࡧࡵࡣࡩࡧࡴࡢࠤஞ"): bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠢࡶࡵࡨࡶࡓࡧ࡭ࡦࠤட")),
                              bstack1lllll1_opy_ (u"ࠣࡪࡲࡷࡹࡥࡩ࡯ࡨࡲࠦ஠"): get_host_info()
                          }
                      }
                      bstack1ll1l1ll11_opy_ = bstack1l111ll111_opy_(cli.config, [bstack1lllll1_opy_ (u"ࠤࡤࡴ࡮ࡹࠢ஡"), bstack1lllll1_opy_ (u"ࠥࡩࡩࡹࡉ࡯ࡵࡷࡶࡺࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠣ஢"), bstack1lllll1_opy_ (u"ࠦࡦࡶࡩࠣண")], bstack11111111l_opy_)
                      response = bstack1l1111111_opy_(bstack1lllll1_opy_ (u"ࠧࡖࡏࡔࡖࠥத"), bstack1ll1l1ll11_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack1lllll1_opy_ (u"ࠨࡄࡢࡶࡤࠤࡸ࡫࡮ࡵࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡶࡲࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡪࡡࡵࡣࠣࡿࢂࠨ஥").format(bstack11111111l_opy_, payload))
                      else:
                          logger.debug(bstack1lllll1_opy_ (u"ࠢࡓࡧࡴࡹࡪࡹࡴࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡨࡲࡶࠥࢁࡽࠡࡹ࡬ࡸ࡭ࠦࡤࡢࡶࡤࠤࢀࢃࠢ஦").format(bstack11111111l_opy_, payload))
          except Exception as e:
              logger.debug(bstack1lllll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫࡮ࡥࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢࡾࢁࠧ஧").format(e))
      bstack1l1l111l_opy_()
      bstack1l1ll111l1_opy_(bstack1llll11lll_opy_, logger)
  except:
    pass
def bstack1ll1lll11l_opy_():
  global bstack11l111l1l1_opy_
  global bstack1ll1ll11ll_opy_
  global bstack111l1l11l_opy_
  global bstack111llll1l1_opy_
  global bstack11l1lll111_opy_
  global bstack11llllllll_opy_
  global CONFIG
  bstack11ll111l1l_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪந"))
  if bstack11ll111l1l_opy_ in [bstack1lllll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩன"), bstack1lllll1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪப")]:
    bstack11ll1111l1_opy_()
  percy.shutdown()
  if bstack11l111l1l1_opy_:
    logger.warning(bstack111lll1lll_opy_.format(str(bstack11l111l1l1_opy_)))
  else:
    try:
      bstack1l11l1l1ll_opy_ = bstack1l11l1ll1l_opy_(bstack1lllll1_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫ஫"), logger)
      if bstack1l11l1l1ll_opy_.get(bstack1lllll1_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫ஬")) and bstack1l11l1l1ll_opy_.get(bstack1lllll1_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬ஭")).get(bstack1lllll1_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪம")):
        logger.warning(bstack111lll1lll_opy_.format(str(bstack1l11l1l1ll_opy_[bstack1lllll1_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧய")][bstack1lllll1_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬர")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1l1ll11ll_opy_.invoke(Events.bstack1ll11lllll_opy_)
  logger.info(bstack1l1lll11l1_opy_)
  global bstack11l1l11ll1_opy_
  if bstack11l1l11ll1_opy_:
    bstack11l11111l1_opy_()
  try:
    with bstack1111ll1l1_opy_:
      bstack1ll1111ll1_opy_ = bstack1ll1ll11ll_opy_.copy()
    for driver in bstack1ll1111ll1_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack11llll111l_opy_)
  if bstack11llllllll_opy_ == bstack1lllll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪற"):
    bstack11l1lll111_opy_ = bstack1ll11lll1_opy_(bstack1lllll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ல"))
  if bstack11llllllll_opy_ == bstack1lllll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ள") and len(bstack111llll1l1_opy_) == 0:
    bstack111llll1l1_opy_ = bstack1ll11lll1_opy_(bstack1lllll1_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬழ"))
    if len(bstack111llll1l1_opy_) == 0:
      bstack111llll1l1_opy_ = bstack1ll11lll1_opy_(bstack1lllll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧவ"))
  bstack111ll1l1l_opy_ = bstack1lllll1_opy_ (u"ࠩࠪஶ")
  if len(bstack111l1l11l_opy_) > 0:
    bstack111ll1l1l_opy_ = bstack1111ll1l11_opy_(bstack111l1l11l_opy_)
  elif len(bstack111llll1l1_opy_) > 0:
    bstack111ll1l1l_opy_ = bstack1111ll1l11_opy_(bstack111llll1l1_opy_)
  elif len(bstack11l1lll111_opy_) > 0:
    bstack111ll1l1l_opy_ = bstack1111ll1l11_opy_(bstack11l1lll111_opy_)
  elif len(bstack1l111llll_opy_) > 0:
    bstack111ll1l1l_opy_ = bstack1111ll1l11_opy_(bstack1l111llll_opy_)
  if bool(bstack111ll1l1l_opy_):
    bstack11l1l1111l_opy_(bstack111ll1l1l_opy_)
  else:
    bstack11l1l1111l_opy_()
  bstack1l1ll111l1_opy_(bstack1111lllll1_opy_, logger)
  if bstack11ll111l1l_opy_ not in [bstack1lllll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫஷ")]:
    bstack11l111ll11_opy_()
  bstack1ll11111l1_opy_.bstack1l11l1l1_opy_(CONFIG)
  if len(bstack11l1lll111_opy_) > 0:
    sys.exit(len(bstack11l1lll111_opy_))
def bstack1ll1l11l11_opy_(bstack1111ll1lll_opy_, frame):
  global bstack11l1111l_opy_
  logger.error(bstack11l111l1l_opy_)
  bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡓࡵࠧஸ"), bstack1111ll1lll_opy_)
  if hasattr(signal, bstack1lllll1_opy_ (u"࡙ࠬࡩࡨࡰࡤࡰࡸ࠭ஹ")):
    bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭஺"), signal.Signals(bstack1111ll1lll_opy_).name)
  else:
    bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ஻"), bstack1lllll1_opy_ (u"ࠨࡕࡌࡋ࡚ࡔࡋࡏࡑ࡚ࡒࠬ஼"))
  if cli.is_running():
    bstack1l1ll11ll_opy_.invoke(Events.bstack1ll11lllll_opy_)
  bstack11ll111l1l_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪ஽"))
  if bstack11ll111l1l_opy_ == bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪா") and not cli.is_enabled(CONFIG):
    bstack1ll111ll_opy_.stop(bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫி")))
  bstack1ll1lll11l_opy_()
  sys.exit(1)
def bstack1l1llllll_opy_(err):
  logger.critical(bstack111ll11l1_opy_.format(str(err)))
  bstack11l1l1111l_opy_(bstack111ll11l1_opy_.format(str(err)), True)
  atexit.unregister(bstack1ll1lll11l_opy_)
  bstack11ll1111l1_opy_()
  sys.exit(1)
def bstack11111l1l1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack11l1l1111l_opy_(message, True)
  atexit.unregister(bstack1ll1lll11l_opy_)
  bstack11ll1111l1_opy_()
  sys.exit(1)
def bstack1ll1ll1ll_opy_():
  global CONFIG
  global bstack111ll1ll1l_opy_
  global bstack1ll1111l11_opy_
  global bstack1l11ll111_opy_
  CONFIG = bstack111ll111l_opy_()
  load_dotenv(CONFIG.get(bstack1lllll1_opy_ (u"ࠬ࡫࡮ࡷࡈ࡬ࡰࡪ࠭ீ")))
  bstack11lll1l1ll_opy_()
  bstack11ll1l1111_opy_()
  CONFIG = bstack1111l11ll_opy_(CONFIG)
  update(CONFIG, bstack1ll1111l11_opy_)
  update(CONFIG, bstack111ll1ll1l_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1llll1111l_opy_(CONFIG)
  bstack1l11ll111_opy_ = bstack11ll11111_opy_(CONFIG)
  os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩு")] = bstack1l11ll111_opy_.__str__().lower()
  bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨூ"), bstack1l11ll111_opy_)
  if (bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௃") in CONFIG and bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௄") in bstack111ll1ll1l_opy_) or (
          bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௅") in CONFIG and bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧெ") not in bstack1ll1111l11_opy_):
    if os.getenv(bstack1lllll1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩே")):
      CONFIG[bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨை")] = os.getenv(bstack1lllll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ௉"))
    else:
      if not CONFIG.get(bstack1lllll1_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠦொ"), bstack1lllll1_opy_ (u"ࠤࠥோ")) in bstack11l11l1l1l_opy_:
        bstack1l1llll11l_opy_()
  elif (bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ௌ") not in CONFIG and bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ்࠭") in CONFIG) or (
          bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௎") in bstack1ll1111l11_opy_ and bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௏") not in bstack111ll1ll1l_opy_):
    del (CONFIG[bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩௐ")])
  if bstack11l1l1llll_opy_(CONFIG):
    bstack1l1llllll_opy_(bstack111ll11l1l_opy_)
  Config.bstack11111l1l_opy_().set_property(bstack1lllll1_opy_ (u"ࠣࡷࡶࡩࡷࡔࡡ࡮ࡧࠥ௑"), CONFIG[bstack1lllll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ௒")])
  bstack1l1ll1l11_opy_()
  bstack1ll1l1111_opy_()
  if bstack11ll1lll11_opy_ and not CONFIG.get(bstack1lllll1_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠨ௓"), bstack1lllll1_opy_ (u"ࠦࠧ௔")) in bstack11l11l1l1l_opy_:
    CONFIG[bstack1lllll1_opy_ (u"ࠬࡧࡰࡱࠩ௕")] = bstack1lll1111l1_opy_(CONFIG)
    logger.info(bstack111l1ll1l_opy_.format(CONFIG[bstack1lllll1_opy_ (u"࠭ࡡࡱࡲࠪ௖")]))
  if not bstack1l11ll111_opy_:
    CONFIG[bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪௗ")] = [{}]
def bstack1l1ll1ll11_opy_(config, bstack11ll111ll_opy_):
  global CONFIG
  global bstack11ll1lll11_opy_
  CONFIG = config
  bstack11ll1lll11_opy_ = bstack11ll111ll_opy_
def bstack1ll1l1111_opy_():
  global CONFIG
  global bstack11ll1lll11_opy_
  if bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࠬ௘") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack11111l1l1l_opy_(e, bstack1llll11l1l_opy_)
    bstack11ll1lll11_opy_ = True
    bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ௙"), True)
def bstack1lll1111l1_opy_(config):
  bstack11lll11l1_opy_ = bstack1lllll1_opy_ (u"ࠪࠫ௚")
  app = config[bstack1lllll1_opy_ (u"ࠫࡦࡶࡰࠨ௛")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1111l11l11_opy_:
      if os.path.exists(app):
        bstack11lll11l1_opy_ = bstack11l11lll1l_opy_(config, app)
      elif bstack11ll11l11_opy_(app):
        bstack11lll11l1_opy_ = app
      else:
        bstack1l1llllll_opy_(bstack1l11111l11_opy_.format(app))
    else:
      if bstack11ll11l11_opy_(app):
        bstack11lll11l1_opy_ = app
      elif os.path.exists(app):
        bstack11lll11l1_opy_ = bstack11l11lll1l_opy_(app)
      else:
        bstack1l1llllll_opy_(bstack1l11l1l111_opy_)
  else:
    if len(app) > 2:
      bstack1l1llllll_opy_(bstack1l1ll1lll1_opy_)
    elif len(app) == 2:
      if bstack1lllll1_opy_ (u"ࠬࡶࡡࡵࡪࠪ௜") in app and bstack1lllll1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ௝") in app:
        if os.path.exists(app[bstack1lllll1_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ௞")]):
          bstack11lll11l1_opy_ = bstack11l11lll1l_opy_(config, app[bstack1lllll1_opy_ (u"ࠨࡲࡤࡸ࡭࠭௟")], app[bstack1lllll1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬ௠")])
        else:
          bstack1l1llllll_opy_(bstack1l11111l11_opy_.format(app))
      else:
        bstack1l1llllll_opy_(bstack1l1ll1lll1_opy_)
    else:
      for key in app:
        if key in bstack1l11ll1ll_opy_:
          if key == bstack1lllll1_opy_ (u"ࠪࡴࡦࡺࡨࠨ௡"):
            if os.path.exists(app[key]):
              bstack11lll11l1_opy_ = bstack11l11lll1l_opy_(config, app[key])
            else:
              bstack1l1llllll_opy_(bstack1l11111l11_opy_.format(app))
          else:
            bstack11lll11l1_opy_ = app[key]
        else:
          bstack1l1llllll_opy_(bstack111l111ll1_opy_)
  return bstack11lll11l1_opy_
def bstack11ll11l11_opy_(bstack11lll11l1_opy_):
  import re
  bstack1lll11l11l_opy_ = re.compile(bstack1lllll1_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬࠧࠦ௢"))
  bstack1l1lll11l_opy_ = re.compile(bstack1lllll1_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭࠳ࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪࠥࠤ௣"))
  if bstack1lllll1_opy_ (u"࠭ࡢࡴ࠼࠲࠳ࠬ௤") in bstack11lll11l1_opy_ or re.fullmatch(bstack1lll11l11l_opy_, bstack11lll11l1_opy_) or re.fullmatch(bstack1l1lll11l_opy_, bstack11lll11l1_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack11ll11l1l_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack11l11lll1l_opy_(config, path, bstack11111l111_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1lllll1_opy_ (u"ࠧࡳࡤࠪ௥")).read()).hexdigest()
  bstack1l1l11l11_opy_ = bstack11lll1llll_opy_(md5_hash)
  bstack11lll11l1_opy_ = None
  if bstack1l1l11l11_opy_:
    logger.info(bstack1l11ll11l_opy_.format(bstack1l1l11l11_opy_, md5_hash))
    return bstack1l1l11l11_opy_
  bstack1l11llll11_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack1lllll1_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭௦"): (os.path.basename(path), open(os.path.abspath(path), bstack1lllll1_opy_ (u"ࠩࡵࡦࠬ௧")), bstack1lllll1_opy_ (u"ࠪࡸࡪࡾࡴ࠰ࡲ࡯ࡥ࡮ࡴࠧ௨")),
      bstack1lllll1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧ௩"): bstack11111l111_opy_
    }
  )
  response = requests.post(bstack1l111ll1l_opy_, data=multipart_data,
                           headers={bstack1lllll1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ௪"): multipart_data.content_type},
                           auth=(config[bstack1lllll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ௫")], config[bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ௬")]))
  try:
    res = json.loads(response.text)
    bstack11lll11l1_opy_ = res[bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࡤࡻࡲ࡭ࠩ௭")]
    logger.info(bstack11l1111ll_opy_.format(bstack11lll11l1_opy_))
    bstack1llll1l11l_opy_(md5_hash, bstack11lll11l1_opy_)
    cli.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡶࡲ࡯ࡳࡦࡪ࡟ࡢࡲࡳࠦ௮"), datetime.datetime.now() - bstack1l11llll11_opy_)
  except ValueError as err:
    bstack1l1llllll_opy_(bstack11111lll1_opy_.format(str(err)))
  return bstack11lll11l1_opy_
def bstack1l1ll1l11_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1l1lll1l1_opy_
  bstack1lll1l1ll_opy_ = 1
  bstack1l111lll11_opy_ = 1
  if bstack1lllll1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ௯") in CONFIG:
    bstack1l111lll11_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ௰")]
  else:
    bstack1l111lll11_opy_ = bstack111l1l111l_opy_(framework_name, args) or 1
  if bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ௱") in CONFIG:
    bstack1lll1l1ll_opy_ = len(CONFIG[bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ௲")])
  bstack1l1lll1l1_opy_ = int(bstack1l111lll11_opy_) * int(bstack1lll1l1ll_opy_)
def bstack111l1l111l_opy_(framework_name, args):
  if framework_name == bstack11l1lll11l_opy_ and args and bstack1lllll1_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬ௳") in args:
      bstack1l1111l11l_opy_ = args.index(bstack1lllll1_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭௴"))
      return int(args[bstack1l1111l11l_opy_ + 1]) or 1
  return 1
def bstack11lll1llll_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lllll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬ௵"))
    bstack111llllll1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠪࢂࠬ௶")), bstack1lllll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ௷"), bstack1lllll1_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭௸"))
    if os.path.exists(bstack111llllll1_opy_):
      try:
        bstack11ll11lll_opy_ = json.load(open(bstack111llllll1_opy_, bstack1lllll1_opy_ (u"࠭ࡲࡣࠩ௹")))
        if md5_hash in bstack11ll11lll_opy_:
          bstack11ll111lll_opy_ = bstack11ll11lll_opy_[md5_hash]
          bstack1llll1llll_opy_ = datetime.datetime.now()
          bstack111l11l111_opy_ = datetime.datetime.strptime(bstack11ll111lll_opy_[bstack1lllll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ௺")], bstack1lllll1_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬ௻"))
          if (bstack1llll1llll_opy_ - bstack111l11l111_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack11ll111lll_opy_[bstack1lllll1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ௼")]):
            return None
          return bstack11ll111lll_opy_[bstack1lllll1_opy_ (u"ࠪ࡭ࡩ࠭௽")]
      except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡶࡪࡧࡤࡪࡰࡪࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࠦࡦࡪ࡮ࡨ࠾ࠥࢁࡽࠨ௾").format(str(e)))
    return None
  bstack111llllll1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠬࢄࠧ௿")), bstack1lllll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ఀ"), bstack1lllll1_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨఁ"))
  lock_file = bstack111llllll1_opy_ + bstack1lllll1_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧం")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111llllll1_opy_):
        with open(bstack111llllll1_opy_, bstack1lllll1_opy_ (u"ࠩࡵࠫః")) as f:
          content = f.read().strip()
          if content:
            bstack11ll11lll_opy_ = json.loads(content)
            if md5_hash in bstack11ll11lll_opy_:
              bstack11ll111lll_opy_ = bstack11ll11lll_opy_[md5_hash]
              bstack1llll1llll_opy_ = datetime.datetime.now()
              bstack111l11l111_opy_ = datetime.datetime.strptime(bstack11ll111lll_opy_[bstack1lllll1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ఄ")], bstack1lllll1_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨఅ"))
              if (bstack1llll1llll_opy_ - bstack111l11l111_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack11ll111lll_opy_[bstack1lllll1_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪఆ")]):
                return None
              return bstack11ll111lll_opy_[bstack1lllll1_opy_ (u"࠭ࡩࡥࠩఇ")]
      return None
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡷࡪࡶ࡫ࠤ࡫࡯࡬ࡦࠢ࡯ࡳࡨࡱࡩ࡯ࡩࠣࡪࡴࡸࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩ࠼ࠣࡿࢂ࠭ఈ").format(str(e)))
    return None
def bstack1llll1l11l_opy_(md5_hash, bstack11lll11l1_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lllll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫఉ"))
    bstack1ll1l1l1l1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠩࢁࠫఊ")), bstack1lllll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪఋ"))
    if not os.path.exists(bstack1ll1l1l1l1_opy_):
      os.makedirs(bstack1ll1l1l1l1_opy_)
    bstack111llllll1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠫࢃ࠭ఌ")), bstack1lllll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ఍"), bstack1lllll1_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧఎ"))
    bstack11l1l1l1ll_opy_ = {
      bstack1lllll1_opy_ (u"ࠧࡪࡦࠪఏ"): bstack11lll11l1_opy_,
      bstack1lllll1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫఐ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1lllll1_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭఑")),
      bstack1lllll1_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨఒ"): str(__version__)
    }
    try:
      bstack11ll11lll_opy_ = {}
      if os.path.exists(bstack111llllll1_opy_):
        bstack11ll11lll_opy_ = json.load(open(bstack111llllll1_opy_, bstack1lllll1_opy_ (u"ࠫࡷࡨࠧఓ")))
      bstack11ll11lll_opy_[md5_hash] = bstack11l1l1l1ll_opy_
      with open(bstack111llllll1_opy_, bstack1lllll1_opy_ (u"ࠧࡽࠫࠣఔ")) as outfile:
        json.dump(bstack11ll11lll_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰࡥࡣࡷ࡭ࡳ࡭ࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩࠢࡩ࡭ࡱ࡫࠺ࠡࡽࢀࠫక").format(str(e)))
    return
  bstack1ll1l1l1l1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠧࡿࠩఖ")), bstack1lllll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨగ"))
  if not os.path.exists(bstack1ll1l1l1l1_opy_):
    os.makedirs(bstack1ll1l1l1l1_opy_)
  bstack111llllll1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠩࢁࠫఘ")), bstack1lllll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪఙ"), bstack1lllll1_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬచ"))
  lock_file = bstack111llllll1_opy_ + bstack1lllll1_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫఛ")
  bstack11l1l1l1ll_opy_ = {
    bstack1lllll1_opy_ (u"࠭ࡩࡥࠩజ"): bstack11lll11l1_opy_,
    bstack1lllll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪఝ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1lllll1_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬఞ")),
    bstack1lllll1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧట"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack11ll11lll_opy_ = {}
      if os.path.exists(bstack111llllll1_opy_):
        with open(bstack111llllll1_opy_, bstack1lllll1_opy_ (u"ࠪࡶࠬఠ")) as f:
          content = f.read().strip()
          if content:
            bstack11ll11lll_opy_ = json.loads(content)
      bstack11ll11lll_opy_[md5_hash] = bstack11l1l1l1ll_opy_
      with open(bstack111llllll1_opy_, bstack1lllll1_opy_ (u"ࠦࡼࠨడ")) as outfile:
        json.dump(bstack11ll11lll_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡼ࡯ࡴࡩࠢࡩ࡭ࡱ࡫ࠠ࡭ࡱࡦ࡯࡮ࡴࡧࠡࡨࡲࡶࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮ࠠࡶࡲࡧࡥࡹ࡫࠺ࠡࡽࢀࠫఢ").format(str(e)))
def bstack1l1l1111l1_opy_(self):
  return
def bstack1l1l1ll1ll_opy_(self):
  return
def bstack1l1111111l_opy_():
  global bstack11lll11ll1_opy_
  bstack11lll11ll1_opy_ = True
@measure(event_name=EVENTS.bstack1111llllll_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack111l1111l_opy_(self):
  global bstack11l1ll1l1_opy_
  global bstack1ll1lll1l_opy_
  global bstack1ll1lll1l1_opy_
  try:
    if bstack1lllll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ణ") in bstack11l1ll1l1_opy_ and self.session_id != None and bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫత"), bstack1lllll1_opy_ (u"ࠨࠩథ")) != bstack1lllll1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪద"):
      bstack1l1ll11lll_opy_ = bstack1lllll1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪధ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫన")
      if bstack1l1ll11lll_opy_ == bstack1lllll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ఩"):
        bstack1ll1ll11l1_opy_(logger)
      if self != None:
        bstack1l1l1llll_opy_(self, bstack1l1ll11lll_opy_, bstack1lllll1_opy_ (u"࠭ࠬࠡࠩప").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1lllll1_opy_ (u"ࠧࠨఫ")
    if bstack1lllll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨబ") in bstack11l1ll1l1_opy_ and getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨభ"), None):
      bstack1llll1lll_opy_.bstack111lll11_opy_(self, bstack1111l11l1_opy_, logger, wait=True)
    if bstack1lllll1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪమ") in bstack11l1ll1l1_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1l1l1llll_opy_(self, bstack1lllll1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦయ"))
      bstack11llll111_opy_.bstack1l111llll1_opy_(self)
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨర") + str(e))
  bstack1ll1lll1l1_opy_(self)
  self.session_id = None
def bstack11l1l1ll11_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1ll1l1111l_opy_
    global bstack11l1ll1l1_opy_
    command_executor = kwargs.get(bstack1lllll1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠩఱ"), bstack1lllll1_opy_ (u"ࠧࠨల"))
    bstack111l1l1ll1_opy_ = False
    if type(command_executor) == str and bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫళ") in command_executor:
      bstack111l1l1ll1_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬఴ") in str(getattr(command_executor, bstack1lllll1_opy_ (u"ࠪࡣࡺࡸ࡬ࠨవ"), bstack1lllll1_opy_ (u"ࠫࠬశ"))):
      bstack111l1l1ll1_opy_ = True
    else:
      kwargs = bstack1lll1lll1_opy_.bstack1l1l1lll1_opy_(bstack1ll1l1l111_opy_=kwargs, config=CONFIG)
      return bstack1ll11llll_opy_(self, *args, **kwargs)
    if bstack111l1l1ll1_opy_:
      bstack1l1l1l1l11_opy_ = bstack1l1lll1l1l_opy_.bstack1lll1111ll_opy_(CONFIG, bstack11l1ll1l1_opy_)
      if kwargs.get(bstack1lllll1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ష")):
        kwargs[bstack1lllll1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧస")] = bstack1ll1l1111l_opy_(kwargs[bstack1lllll1_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨహ")], bstack11l1ll1l1_opy_, CONFIG, bstack1l1l1l1l11_opy_)
      elif kwargs.get(bstack1lllll1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ఺")):
        kwargs[bstack1lllll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ఻")] = bstack1ll1l1111l_opy_(kwargs[bstack1lllll1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ఼ࠪ")], bstack11l1ll1l1_opy_, CONFIG, bstack1l1l1l1l11_opy_)
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦఽ").format(str(e)))
  return bstack1ll11llll_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l1l1llll1_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack1ll1l1ll1_opy_(self, command_executor=bstack1lllll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴࠷࠲࠸࠰࠳࠲࠵࠴࠱࠻࠶࠷࠸࠹ࠨా"), *args, **kwargs):
  global bstack1ll1lll1l_opy_
  global bstack1ll1ll11ll_opy_
  bstack1l111111ll_opy_ = bstack11l1l1ll11_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1llll111_opy_.on():
    return bstack1l111111ll_opy_
  try:
    logger.debug(bstack1lllll1_opy_ (u"࠭ࡃࡰ࡯ࡰࡥࡳࡪࠠࡆࡺࡨࡧࡺࡺ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡦࡢ࡮ࡶࡩࠥ࠳ࠠࡼࡿࠪి").format(str(command_executor)))
    logger.debug(bstack1lllll1_opy_ (u"ࠧࡉࡷࡥࠤ࡚ࡘࡌࠡ࡫ࡶࠤ࠲ࠦࡻࡾࠩీ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫు") in command_executor._url:
      bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪూ"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ృ") in command_executor):
    bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬౄ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack11ll1l1ll1_opy_ = getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭౅"), None)
  bstack11llll1l1_opy_ = {}
  if self.capabilities is not None:
    bstack11llll1l1_opy_[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬె")] = self.capabilities.get(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬే"))
    bstack11llll1l1_opy_[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪై")] = self.capabilities.get(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ౉"))
    bstack11llll1l1_opy_[bstack1lllll1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡢࡳࡵࡺࡩࡰࡰࡶࠫొ")] = self.capabilities.get(bstack1lllll1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩో"))
  if CONFIG.get(bstack1lllll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬౌ"), False) and bstack1lll1lll1_opy_.bstack11lll1111l_opy_(bstack11llll1l1_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack1lllll1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ్࠭") in bstack11l1ll1l1_opy_ or bstack1lllll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭౎") in bstack11l1ll1l1_opy_:
    bstack1ll111ll_opy_.bstack1111ll1l1l_opy_(self)
  if bstack1lllll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ౏") in bstack11l1ll1l1_opy_ and bstack11ll1l1ll1_opy_ and bstack11ll1l1ll1_opy_.get(bstack1lllll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ౐"), bstack1lllll1_opy_ (u"ࠪࠫ౑")) == bstack1lllll1_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ౒"):
    bstack1ll111ll_opy_.bstack1111ll1l1l_opy_(self)
  bstack1ll1lll1l_opy_ = self.session_id
  with bstack1111ll1l1_opy_:
    bstack1ll1ll11ll_opy_.append(self)
  return bstack1l111111ll_opy_
def bstack11l11lll11_opy_(args):
  return bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷ࠭౓") in str(args)
def bstack11l1l111l_opy_(self, driver_command, *args, **kwargs):
  global bstack1l11lllll_opy_
  global bstack1l11lll1l_opy_
  bstack1l1l11llll_opy_ = bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ౔"), None) and bstack1lll1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲౕ࠭"), None)
  bstack1ll11111l_opy_ = bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨౖ"), None) and bstack1lll1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ౗"), None)
  bstack1llll1ll11_opy_ = getattr(self, bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪౘ"), None) != None and getattr(self, bstack1lllll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫౙ"), None) == True
  if not bstack1l11lll1l_opy_ and bstack1lllll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬౚ") in CONFIG and CONFIG[bstack1lllll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭౛")] == True and bstack1llll11l11_opy_.bstack1llllll1ll_opy_(driver_command) and (bstack1llll1ll11_opy_ or bstack1l1l11llll_opy_ or bstack1ll11111l_opy_) and not bstack11l11lll11_opy_(args):
    try:
      bstack1l11lll1l_opy_ = True
      logger.debug(bstack1lllll1_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡻࡾࠩ౜").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1lllll1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵ࡫ࡲࡧࡱࡵࡱࠥࡹࡣࡢࡰࠣࡿࢂ࠭ౝ").format(str(err)))
    bstack1l11lll1l_opy_ = False
  response = bstack1l11lllll_opy_(self, driver_command, *args, **kwargs)
  if (bstack1lllll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ౞") in str(bstack11l1ll1l1_opy_).lower() or bstack1lllll1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ౟") in str(bstack11l1ll1l1_opy_).lower()) and bstack1llll111_opy_.on():
    try:
      if driver_command == bstack1lllll1_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨౠ"):
        bstack1ll111ll_opy_.bstack11111l1ll1_opy_({
            bstack1lllll1_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫౡ"): response[bstack1lllll1_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬౢ")],
            bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧౣ"): bstack1ll111ll_opy_.current_test_uuid() if bstack1ll111ll_opy_.current_test_uuid() else bstack1llll111_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1l11llllll_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack1ll11ll111_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1ll1lll1l_opy_
  global bstack111lll111l_opy_
  global bstack11l11ll11_opy_
  global bstack1ll1l111l1_opy_
  global bstack1l1l1ll111_opy_
  global bstack11l1ll1l1_opy_
  global bstack1ll11llll_opy_
  global bstack1ll1ll11ll_opy_
  global bstack111llll111_opy_
  global bstack1111l11l1_opy_
  if os.getenv(bstack1lllll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭౤")) is not None and bstack1lll1lll1_opy_.bstack111ll111l1_opy_(CONFIG) is None:
    CONFIG[bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ౥")] = True
  CONFIG[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ౦")] = str(bstack11l1ll1l1_opy_) + str(__version__)
  bstack11ll1lll1_opy_ = os.environ[bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ౧")]
  bstack1l1l1l1l11_opy_ = bstack1l1lll1l1l_opy_.bstack1lll1111ll_opy_(CONFIG, bstack11l1ll1l1_opy_)
  CONFIG[bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ౨")] = bstack11ll1lll1_opy_
  CONFIG[bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨ౩")] = bstack1l1l1l1l11_opy_
  if CONFIG.get(bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ౪"),bstack1lllll1_opy_ (u"ࠨࠩ౫")) and bstack1lllll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ౬") in bstack11l1ll1l1_opy_:
    CONFIG[bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ౭")].pop(bstack1lllll1_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ౮"), None)
    CONFIG[bstack1lllll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ౯")].pop(bstack1lllll1_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ౰"), None)
  command_executor = bstack1lll1ll111_opy_()
  logger.debug(bstack111lll1111_opy_.format(command_executor))
  proxy = bstack1lll11lll_opy_(CONFIG, proxy)
  bstack1l11l111l_opy_ = 0 if bstack111lll111l_opy_ < 0 else bstack111lll111l_opy_
  try:
    if bstack1ll1l111l1_opy_ is True:
      bstack1l11l111l_opy_ = int(multiprocessing.current_process().name)
    elif bstack1l1l1ll111_opy_ is True:
      bstack1l11l111l_opy_ = int(threading.current_thread().name)
  except:
    bstack1l11l111l_opy_ = 0
  bstack111lll1l1_opy_ = bstack11lll111l1_opy_(CONFIG, bstack1l11l111l_opy_)
  logger.debug(bstack1lll1l1l11_opy_.format(str(bstack111lll1l1_opy_)))
  if bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ౱") in CONFIG and bstack11l11l111l_opy_(CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ౲")]):
    bstack1l1ll1l111_opy_(bstack111lll1l1_opy_)
  if bstack1lll1lll1_opy_.bstack1l111lll1_opy_(CONFIG, bstack1l11l111l_opy_) and bstack1lll1lll1_opy_.bstack111lllll1_opy_(bstack111lll1l1_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack1lll1lll1_opy_.set_capabilities(bstack111lll1l1_opy_, CONFIG)
  if desired_capabilities:
    bstack11111lllll_opy_ = bstack1111l11ll_opy_(desired_capabilities)
    bstack11111lllll_opy_[bstack1lllll1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩ౳")] = bstack1111l1lll_opy_(CONFIG)
    bstack111l1lll1_opy_ = bstack11lll111l1_opy_(bstack11111lllll_opy_)
    if bstack111l1lll1_opy_:
      bstack111lll1l1_opy_ = update(bstack111l1lll1_opy_, bstack111lll1l1_opy_)
    desired_capabilities = None
  if options:
    bstack11ll1llll_opy_(options, bstack111lll1l1_opy_)
  if not options:
    options = bstack1ll1ll1l11_opy_(bstack111lll1l1_opy_)
  bstack1111l11l1_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭౴"))[bstack1l11l111l_opy_]
  if proxy and bstack11l1l1lll1_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫ౵")):
    options.proxy(proxy)
  if options and bstack11l1l1lll1_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ౶")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack11l1l1lll1_opy_() < version.parse(bstack1lllll1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ౷")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack111lll1l1_opy_)
  logger.info(bstack1ll11l11l_opy_)
  bstack11l11l1111_opy_.end(EVENTS.bstack111l1111ll_opy_.value, EVENTS.bstack111l1111ll_opy_.value + bstack1lllll1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ౸"), EVENTS.bstack111l1111ll_opy_.value + bstack1lllll1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ౹"), status=True, failure=None, test_name=bstack11l11ll11_opy_)
  if bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡴࡷࡵࡦࡪ࡮ࡨࠫ౺") in kwargs:
    del kwargs[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡵࡸ࡯ࡧ࡫࡯ࡩࠬ౻")]
  try:
    if bstack11l1l1lll1_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫ౼")):
      bstack1ll11llll_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack11l1l1lll1_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ౽")):
      bstack1ll11llll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11l1l1lll1_opy_() >= version.parse(bstack1lllll1_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭౾")):
      bstack1ll11llll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1ll11llll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack111l111l11_opy_:
    logger.error(bstack1l11lllll1_opy_.format(bstack1lllll1_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰ࠭౿"), str(bstack111l111l11_opy_)))
    raise bstack111l111l11_opy_
  if bstack1lll1lll1_opy_.bstack1l111lll1_opy_(CONFIG, bstack1l11l111l_opy_) and bstack1lll1lll1_opy_.bstack111lllll1_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪಀ")][bstack1lllll1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨಁ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack1lll1lll1_opy_.set_capabilities(bstack111lll1l1_opy_, CONFIG)
  try:
    bstack1l11llll1_opy_ = bstack1lllll1_opy_ (u"ࠪࠫಂ")
    if bstack11l1l1lll1_opy_() >= version.parse(bstack1lllll1_opy_ (u"ࠫ࠹࠴࠰࠯࠲ࡥ࠵ࠬಃ")):
      if self.caps is not None:
        bstack1l11llll1_opy_ = self.caps.get(bstack1lllll1_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧ಄"))
    else:
      if self.capabilities is not None:
        bstack1l11llll1_opy_ = self.capabilities.get(bstack1lllll1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨಅ"))
    if bstack1l11llll1_opy_:
      bstack11l1lll11_opy_(bstack1l11llll1_opy_)
      if bstack11l1l1lll1_opy_() <= version.parse(bstack1lllll1_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧಆ")):
        self.command_executor._url = bstack1lllll1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤಇ") + bstack1ll1lll1ll_opy_ + bstack1lllll1_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨಈ")
      else:
        self.command_executor._url = bstack1lllll1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧಉ") + bstack1l11llll1_opy_ + bstack1lllll1_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧಊ")
      logger.debug(bstack1l1111lll_opy_.format(bstack1l11llll1_opy_))
    else:
      logger.debug(bstack1l1llll1ll_opy_.format(bstack1lllll1_opy_ (u"ࠧࡕࡰࡵ࡫ࡰࡥࡱࠦࡈࡶࡤࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠨಋ")))
  except Exception as e:
    logger.debug(bstack1l1llll1ll_opy_.format(e))
  if bstack1lllll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಌ") in bstack11l1ll1l1_opy_:
    bstack11ll1llll1_opy_(bstack111lll111l_opy_, bstack111llll111_opy_)
  bstack1ll1lll1l_opy_ = self.session_id
  if bstack1lllll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ಍") in bstack11l1ll1l1_opy_ or bstack1lllll1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨಎ") in bstack11l1ll1l1_opy_ or bstack1lllll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨಏ") in bstack11l1ll1l1_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack11ll1l1ll1_opy_ = getattr(threading.current_thread(), bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫಐ"), None)
  if bstack1lllll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ಑") in bstack11l1ll1l1_opy_ or bstack1lllll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫಒ") in bstack11l1ll1l1_opy_:
    bstack1ll111ll_opy_.bstack1111ll1l1l_opy_(self)
  if bstack1lllll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ಓ") in bstack11l1ll1l1_opy_ and bstack11ll1l1ll1_opy_ and bstack11ll1l1ll1_opy_.get(bstack1lllll1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧಔ"), bstack1lllll1_opy_ (u"ࠨࠩಕ")) == bstack1lllll1_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪಖ"):
    bstack1ll111ll_opy_.bstack1111ll1l1l_opy_(self)
  with bstack1111ll1l1_opy_:
    bstack1ll1ll11ll_opy_.append(self)
  if bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಗ") in CONFIG and bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩಘ") in CONFIG[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಙ")][bstack1l11l111l_opy_]:
    bstack11l11ll11_opy_ = CONFIG[bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಚ")][bstack1l11l111l_opy_][bstack1lllll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬಛ")]
  logger.debug(bstack1111l111ll_opy_.format(bstack1ll1lll1l_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack11lll11ll_opy_
    def bstack1lll1l1111_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1l11ll1111_opy_
      if(bstack1lllll1_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࠮࡫ࡵࠥಜ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠩࢁࠫಝ")), bstack1lllll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪಞ"), bstack1lllll1_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭ಟ")), bstack1lllll1_opy_ (u"ࠬࡽࠧಠ")) as fp:
          fp.write(bstack1lllll1_opy_ (u"ࠨࠢಡ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1lllll1_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤಢ")))):
          with open(args[1], bstack1lllll1_opy_ (u"ࠨࡴࠪಣ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1lllll1_opy_ (u"ࠩࡤࡷࡾࡴࡣࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡣࡳ࡫ࡷࡑࡣࡪࡩ࠭ࡩ࡯࡯ࡶࡨࡼࡹ࠲ࠠࡱࡣࡪࡩࠥࡃࠠࡷࡱ࡬ࡨࠥ࠶ࠩࠨತ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1111ll1111_opy_)
            if bstack1lllll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧಥ") in CONFIG and str(CONFIG[bstack1lllll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨದ")]).lower() != bstack1lllll1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫಧ"):
                bstack11111l1lll_opy_ = bstack11lll11ll_opy_()
                bstack1l1l1111ll_opy_ = bstack1lllll1_opy_ (u"࠭ࠧࠨࠌ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠏࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࠻ࠋࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࠾ࠎࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࠽ࠍࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࠽ࠍࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࠎ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡱࡧࡵ࡯ࡥ࡫ࠤࡂࠦࡡࡴࡻࡱࡧࠥ࠮࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸ࠯ࠠ࠾ࡀࠣࡿࢀࠐࠠࠡ࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࠎࠥࠦࡴࡳࡻࠣࡿࢀࠐࠠࠡࠢࠣࡧࡦࡶࡳࠡ࠿ࠣࡎࡘࡕࡎ࠯ࡲࡤࡶࡸ࡫ࠨࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷ࠮ࡁࠊࠡࠢࢀࢁࠥࡩࡡࡵࡥ࡫ࠤ࠭࡫ࡸࠪࠢࡾࡿࠏࠦࠠࠡࠢࡦࡳࡳࡹ࡯࡭ࡧ࠱ࡩࡷࡸ࡯ࡳࠪࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠾ࠧ࠲ࠠࡦࡺࠬ࠿ࠏࠦࠠࡾࡿࠍࠤࠥࡸࡥࡵࡷࡵࡲࠥࡧࡷࡢ࡫ࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡨࡵ࡮࡯ࡧࡦࡸ࠭ࢁࡻࠋࠢࠣࠤࠥࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵ࠼ࠣࠫࢀࡩࡤࡱࡗࡵࡰࢂ࠭ࠠࠬࠢࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩ࠭ࠌࠣࠤࠥࠦ࠮࠯࠰࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴࠌࠣࠤࢂࢃࠩ࠼ࠌࢀࢁࡀࠐ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠌࠪࠫࠬನ").format(bstack11111l1lll_opy_=bstack11111l1lll_opy_)
            lines.insert(1, bstack1l1l1111ll_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1lllll1_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤ಩")), bstack1lllll1_opy_ (u"ࠨࡹࠪಪ")) as bstack11lll1l1l1_opy_:
              bstack11lll1l1l1_opy_.writelines(lines)
        CONFIG[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫಫ")] = str(bstack11l1ll1l1_opy_) + str(__version__)
        bstack11ll1lll1_opy_ = os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨಬ")]
        bstack1l1l1l1l11_opy_ = bstack1l1lll1l1l_opy_.bstack1lll1111ll_opy_(CONFIG, bstack11l1ll1l1_opy_)
        CONFIG[bstack1lllll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧಭ")] = bstack11ll1lll1_opy_
        CONFIG[bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧಮ")] = bstack1l1l1l1l11_opy_
        bstack1l11l111l_opy_ = 0 if bstack111lll111l_opy_ < 0 else bstack111lll111l_opy_
        try:
          if bstack1ll1l111l1_opy_ is True:
            bstack1l11l111l_opy_ = int(multiprocessing.current_process().name)
          elif bstack1l1l1ll111_opy_ is True:
            bstack1l11l111l_opy_ = int(threading.current_thread().name)
        except:
          bstack1l11l111l_opy_ = 0
        CONFIG[bstack1lllll1_opy_ (u"ࠨࡵࡴࡧ࡚࠷ࡈࠨಯ")] = False
        CONFIG[bstack1lllll1_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨರ")] = True
        bstack111lll1l1_opy_ = bstack11lll111l1_opy_(CONFIG, bstack1l11l111l_opy_)
        logger.debug(bstack1lll1l1l11_opy_.format(str(bstack111lll1l1_opy_)))
        if CONFIG.get(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬಱ")):
          bstack1l1ll1l111_opy_(bstack111lll1l1_opy_)
        if bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಲ") in CONFIG and bstack1lllll1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨಳ") in CONFIG[bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಴")][bstack1l11l111l_opy_]:
          bstack11l11ll11_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨವ")][bstack1l11l111l_opy_][bstack1lllll1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫಶ")]
        args.append(os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠧࡿࠩಷ")), bstack1lllll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨಸ"), bstack1lllll1_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫಹ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack111lll1l1_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1lllll1_opy_ (u"ࠥ࡭ࡳࡪࡥࡹࡡࡥࡷࡹࡧࡣ࡬࠰࡭ࡷࠧ಺"))
      bstack1l11ll1111_opy_ = True
      return bstack1lll111ll1_opy_(self, args, bufsize=bufsize, executable=executable,
                    stdin=stdin, stdout=stdout, stderr=stderr,
                    preexec_fn=preexec_fn, close_fds=close_fds,
                    shell=shell, cwd=cwd, env=env, universal_newlines=universal_newlines,
                    startupinfo=startupinfo, creationflags=creationflags,
                    restore_signals=restore_signals, start_new_session=start_new_session,
                    pass_fds=pass_fds, user=user, group=group, extra_groups=extra_groups,
                    encoding=encoding, errors=errors, text=text, umask=umask, pipesize=pipesize)
  except Exception as e:
    pass
  import playwright._impl._api_structures
  import playwright._impl._helper
  def bstack11l11l111_opy_(self,
        executablePath = None,
        channel = None,
        args = None,
        ignoreDefaultArgs = None,
        handleSIGINT = None,
        handleSIGTERM = None,
        handleSIGHUP = None,
        timeout = None,
        env = None,
        headless = None,
        devtools = None,
        proxy = None,
        downloadsPath = None,
        slowMo = None,
        tracesDir = None,
        chromiumSandbox = None,
        firefoxUserPrefs = None
        ):
    global CONFIG
    global bstack111lll111l_opy_
    global bstack11l11ll11_opy_
    global bstack1ll1l111l1_opy_
    global bstack1l1l1ll111_opy_
    global bstack11l1ll1l1_opy_
    CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭಻")] = str(bstack11l1ll1l1_opy_) + str(__version__)
    bstack11ll1lll1_opy_ = os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆ಼ࠪ")]
    bstack1l1l1l1l11_opy_ = bstack1l1lll1l1l_opy_.bstack1lll1111ll_opy_(CONFIG, bstack11l1ll1l1_opy_)
    CONFIG[bstack1lllll1_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩಽ")] = bstack11ll1lll1_opy_
    CONFIG[bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩಾ")] = bstack1l1l1l1l11_opy_
    bstack1l11l111l_opy_ = 0 if bstack111lll111l_opy_ < 0 else bstack111lll111l_opy_
    try:
      if bstack1ll1l111l1_opy_ is True:
        bstack1l11l111l_opy_ = int(multiprocessing.current_process().name)
      elif bstack1l1l1ll111_opy_ is True:
        bstack1l11l111l_opy_ = int(threading.current_thread().name)
    except:
      bstack1l11l111l_opy_ = 0
    CONFIG[bstack1lllll1_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢಿ")] = True
    bstack111lll1l1_opy_ = bstack11lll111l1_opy_(CONFIG, bstack1l11l111l_opy_)
    logger.debug(bstack1lll1l1l11_opy_.format(str(bstack111lll1l1_opy_)))
    if CONFIG.get(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ೀ")):
      bstack1l1ll1l111_opy_(bstack111lll1l1_opy_)
    if bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ು") in CONFIG and bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩೂ") in CONFIG[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨೃ")][bstack1l11l111l_opy_]:
      bstack11l11ll11_opy_ = CONFIG[bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩೄ")][bstack1l11l111l_opy_][bstack1lllll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ೅")]
    import urllib
    import json
    if bstack1lllll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬೆ") in CONFIG and str(CONFIG[bstack1lllll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ೇ")]).lower() != bstack1lllll1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩೈ"):
        bstack1l11l11ll_opy_ = bstack11lll11ll_opy_()
        bstack11111l1lll_opy_ = bstack1l11l11ll_opy_ + urllib.parse.quote(json.dumps(bstack111lll1l1_opy_))
    else:
        bstack11111l1lll_opy_ = bstack1lllll1_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭೉") + urllib.parse.quote(json.dumps(bstack111lll1l1_opy_))
    browser = self.connect(bstack11111l1lll_opy_)
    return browser
except Exception as e:
    pass
def bstack1l111l1111_opy_():
    global bstack1l11ll1111_opy_
    global bstack11l1ll1l1_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack11111l11l_opy_
        global bstack11l1111l_opy_
        if not bstack1l11ll111_opy_:
          global bstack111l11l11_opy_
          if not bstack111l11l11_opy_:
            from bstack_utils.helper import bstack1lll1l1ll1_opy_, bstack1lll11l1l_opy_, bstack1l11111lll_opy_
            bstack111l11l11_opy_ = bstack1lll1l1ll1_opy_()
            bstack1lll11l1l_opy_(bstack11l1ll1l1_opy_)
            bstack1l1l1l1l11_opy_ = bstack1l1lll1l1l_opy_.bstack1lll1111ll_opy_(CONFIG, bstack11l1ll1l1_opy_)
            bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"ࠧࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡓࡖࡔࡊࡕࡄࡖࡢࡑࡆࡖࠢೊ"), bstack1l1l1l1l11_opy_)
          BrowserType.connect = bstack11111l11l_opy_
          return
        BrowserType.launch = bstack11l11l111_opy_
        bstack1l11ll1111_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1lll1l1111_opy_
      bstack1l11ll1111_opy_ = True
    except Exception as e:
      pass
def bstack111ll1lll_opy_(context, bstack11ll1l1l11_opy_):
  try:
    context.page.evaluate(bstack1lllll1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢೋ"), bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫೌ")+ json.dumps(bstack11ll1l1l11_opy_) + bstack1lllll1_opy_ (u"ࠣࡿࢀ್ࠦ"))
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃ࠺ࠡࡽࢀࠦ೎").format(str(e), traceback.format_exc()))
def bstack1lll1l11ll_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1lllll1_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ೏"), bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ೐") + json.dumps(message) + bstack1lllll1_opy_ (u"ࠬ࠲ࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠨ೑") + json.dumps(level) + bstack1lllll1_opy_ (u"࠭ࡽࡾࠩ೒"))
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠠࡼࡿ࠽ࠤࢀࢃࠢ೓").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1l1ll1lll_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack1lll11lll1_opy_(self, url):
  global bstack1111l1llll_opy_
  try:
    bstack11ll1111ll_opy_(url)
  except Exception as err:
    logger.debug(bstack11l1ll1111_opy_.format(str(err)))
  try:
    bstack1111l1llll_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack11ll1l111_opy_):
        bstack11ll1111ll_opy_(url, True)
    except Exception as err:
      logger.debug(bstack11l1ll1111_opy_.format(str(err)))
    raise e
def bstack11l1lll1l1_opy_(self):
  global bstack1ll1l11l1_opy_
  bstack1ll1l11l1_opy_ = self
  return
def bstack111llllll_opy_(self):
  global bstack1l11l1ll11_opy_
  bstack1l11l1ll11_opy_ = self
  return
def bstack1l11l1l11l_opy_(test_name, bstack111lllll1l_opy_):
  global CONFIG
  if percy.bstack11lll11lll_opy_() == bstack1lllll1_opy_ (u"ࠣࡶࡵࡹࡪࠨ೔"):
    bstack1111lll111_opy_ = os.path.relpath(bstack111lllll1l_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1111lll111_opy_)
    bstack1lllll1l11_opy_ = suite_name + bstack1lllll1_opy_ (u"ࠤ࠰ࠦೕ") + test_name
    threading.current_thread().percySessionName = bstack1lllll1l11_opy_
def bstack1l111l11ll_opy_(self, test, *args, **kwargs):
  global bstack1l111111l1_opy_
  test_name = None
  bstack111lllll1l_opy_ = None
  if test:
    test_name = str(test.name)
    bstack111lllll1l_opy_ = str(test.source)
  bstack1l11l1l11l_opy_(test_name, bstack111lllll1l_opy_)
  bstack1l111111l1_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1111ll11ll_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack11l1l11l1_opy_(driver, bstack1lllll1l11_opy_):
  if not bstack11l111l1ll_opy_ and bstack1lllll1l11_opy_:
      bstack11111ll11l_opy_ = {
          bstack1lllll1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪೖ"): bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ೗"),
          bstack1lllll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ೘"): {
              bstack1lllll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ೙"): bstack1lllll1l11_opy_
          }
      }
      bstack111l11ll1l_opy_ = bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ೚").format(json.dumps(bstack11111ll11l_opy_))
      driver.execute_script(bstack111l11ll1l_opy_)
  if bstack1l11lll11_opy_:
      bstack1l1ll1llll_opy_ = {
          bstack1lllll1_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨ೛"): bstack1lllll1_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫ೜"),
          bstack1lllll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ೝ"): {
              bstack1lllll1_opy_ (u"ࠫࡩࡧࡴࡢࠩೞ"): bstack1lllll1l11_opy_ + bstack1lllll1_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩࠧࠧ೟"),
              bstack1lllll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬೠ"): bstack1lllll1_opy_ (u"ࠧࡪࡰࡩࡳࠬೡ")
          }
      }
      if bstack1l11lll11_opy_.status == bstack1lllll1_opy_ (u"ࠨࡒࡄࡗࡘ࠭ೢ"):
          bstack1111llll1_opy_ = bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧೣ").format(json.dumps(bstack1l1ll1llll_opy_))
          driver.execute_script(bstack1111llll1_opy_)
          bstack1l1l1llll_opy_(driver, bstack1lllll1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ೤"))
      elif bstack1l11lll11_opy_.status == bstack1lllll1_opy_ (u"ࠫࡋࡇࡉࡍࠩ೥"):
          reason = bstack1lllll1_opy_ (u"ࠧࠨ೦")
          bstack1ll1lllll1_opy_ = bstack1lllll1l11_opy_ + bstack1lllll1_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠧ೧")
          if bstack1l11lll11_opy_.message:
              reason = str(bstack1l11lll11_opy_.message)
              bstack1ll1lllll1_opy_ = bstack1ll1lllll1_opy_ + bstack1lllll1_opy_ (u"ࠧࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶ࠿ࠦࠧ೨") + reason
          bstack1l1ll1llll_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ೩")] = {
              bstack1lllll1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ೪"): bstack1lllll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ೫"),
              bstack1lllll1_opy_ (u"ࠫࡩࡧࡴࡢࠩ೬"): bstack1ll1lllll1_opy_
          }
          bstack1111llll1_opy_ = bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪ೭").format(json.dumps(bstack1l1ll1llll_opy_))
          driver.execute_script(bstack1111llll1_opy_)
          bstack1l1l1llll_opy_(driver, bstack1lllll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭೮"), reason)
          bstack1ll1llll1l_opy_(reason, str(bstack1l11lll11_opy_), str(bstack111lll111l_opy_), logger)
@measure(event_name=EVENTS.bstack1l11lll11l_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack11111ll11_opy_(driver, test):
  if percy.bstack11lll11lll_opy_() == bstack1lllll1_opy_ (u"ࠢࡵࡴࡸࡩࠧ೯") and percy.bstack1l1l1l1l1_opy_() == bstack1lllll1_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥ೰"):
      bstack11l1ll11l_opy_ = bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬೱ"), None)
      bstack1l111l1ll_opy_(driver, bstack11l1ll11l_opy_, test)
  if (bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧೲ"), None) and
      bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪೳ"), None)) or (
      bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ೴"), None) and
      bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ೵"), None)):
      logger.info(bstack1lllll1_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠦࠢ೶"))
      bstack1lll1lll1_opy_.bstack1111l1ll_opy_(driver, name=test.name, path=test.source)
def bstack1l11l1llll_opy_(test, bstack1lllll1l11_opy_):
    try:
      bstack1l11llll11_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack1lllll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭೷")] = bstack1lllll1l11_opy_
      if bstack1l11lll11_opy_:
        if bstack1l11lll11_opy_.status == bstack1lllll1_opy_ (u"ࠩࡓࡅࡘ࡙ࠧ೸"):
          data[bstack1lllll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ೹")] = bstack1lllll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ೺")
        elif bstack1l11lll11_opy_.status == bstack1lllll1_opy_ (u"ࠬࡌࡁࡊࡎࠪ೻"):
          data[bstack1lllll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭೼")] = bstack1lllll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ೽")
          if bstack1l11lll11_opy_.message:
            data[bstack1lllll1_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ೾")] = str(bstack1l11lll11_opy_.message)
      user = CONFIG[bstack1lllll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ೿")]
      key = CONFIG[bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ഀ")]
      host = bstack1l111ll111_opy_(cli.config, [bstack1lllll1_opy_ (u"ࠦࡦࡶࡩࡴࠤഁ"), bstack1lllll1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢം"), bstack1lllll1_opy_ (u"ࠨࡡࡱ࡫ࠥഃ")], bstack1lllll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠣഄ"))
      url = bstack1lllll1_opy_ (u"ࠨࡽࢀ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠰ࡽࢀ࠲࡯ࡹ࡯࡯ࠩഅ").format(host, bstack1ll1lll1l_opy_)
      headers = {
        bstack1lllll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨആ"): bstack1lllll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ഇ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡸࡴࡩࡧࡴࡦࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡷࡥࡹࡻࡳࠣഈ"), datetime.datetime.now() - bstack1l11llll11_opy_)
    except Exception as e:
      logger.error(bstack1ll111111_opy_.format(str(e)))
def bstack1111l111l1_opy_(test, bstack1lllll1l11_opy_):
  global CONFIG
  global bstack1l11l1ll11_opy_
  global bstack1ll1l11l1_opy_
  global bstack1ll1lll1l_opy_
  global bstack1l11lll11_opy_
  global bstack11l11ll11_opy_
  global bstack11llll1l11_opy_
  global bstack11ll111111_opy_
  global bstack1l11ll1l1_opy_
  global bstack1l1l1l1ll1_opy_
  global bstack1ll1ll11ll_opy_
  global bstack1111l11l1_opy_
  global bstack1lll11l11_opy_
  try:
    if not bstack1ll1lll1l_opy_:
      with bstack1lll11l11_opy_:
        bstack1lll11ll11_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠬࢄࠧഉ")), bstack1lllll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ഊ"), bstack1lllll1_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩഋ"))
        if os.path.exists(bstack1lll11ll11_opy_):
          with open(bstack1lll11ll11_opy_, bstack1lllll1_opy_ (u"ࠨࡴࠪഌ")) as f:
            content = f.read().strip()
            if content:
              bstack11ll1111l_opy_ = json.loads(bstack1lllll1_opy_ (u"ࠤࡾࠦ഍") + content + bstack1lllll1_opy_ (u"ࠪࠦࡽࠨ࠺ࠡࠤࡼࠦࠬഎ") + bstack1lllll1_opy_ (u"ࠦࢂࠨഏ"))
              bstack1ll1lll1l_opy_ = bstack11ll1111l_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࡵࠣࡪ࡮ࡲࡥ࠻ࠢࠪഐ") + str(e))
  if bstack1ll1ll11ll_opy_:
    with bstack1111ll1l1_opy_:
      bstack1111l1l11_opy_ = bstack1ll1ll11ll_opy_.copy()
    for driver in bstack1111l1l11_opy_:
      if bstack1ll1lll1l_opy_ == driver.session_id:
        if test:
          bstack11111ll11_opy_(driver, test)
        bstack11l1l11l1_opy_(driver, bstack1lllll1l11_opy_)
  elif bstack1ll1lll1l_opy_:
    bstack1l11l1llll_opy_(test, bstack1lllll1l11_opy_)
  if bstack1l11l1ll11_opy_:
    bstack11ll111111_opy_(bstack1l11l1ll11_opy_)
  if bstack1ll1l11l1_opy_:
    bstack1l11ll1l1_opy_(bstack1ll1l11l1_opy_)
  if bstack11lll11ll1_opy_:
    bstack1l1l1l1ll1_opy_()
def bstack1l11lll1ll_opy_(self, test, *args, **kwargs):
  bstack1lllll1l11_opy_ = None
  if test:
    bstack1lllll1l11_opy_ = str(test.name)
  bstack1111l111l1_opy_(test, bstack1lllll1l11_opy_)
  bstack11llll1l11_opy_(self, test, *args, **kwargs)
def bstack1l1l1ll1l_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1lllll11ll_opy_
  global CONFIG
  global bstack1ll1ll11ll_opy_
  global bstack1ll1lll1l_opy_
  global bstack1lll11l11_opy_
  bstack11l1l1l111_opy_ = None
  try:
    if bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ഑"), None) or bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩഒ"), None):
      try:
        if not bstack1ll1lll1l_opy_:
          bstack1lll11ll11_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠨࢀࠪഓ")), bstack1lllll1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩഔ"), bstack1lllll1_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬക"))
          with bstack1lll11l11_opy_:
            if os.path.exists(bstack1lll11ll11_opy_):
              with open(bstack1lll11ll11_opy_, bstack1lllll1_opy_ (u"ࠫࡷ࠭ഖ")) as f:
                content = f.read().strip()
                if content:
                  bstack11ll1111l_opy_ = json.loads(bstack1lllll1_opy_ (u"ࠧࢁࠢഗ") + content + bstack1lllll1_opy_ (u"࠭ࠢࡹࠤ࠽ࠤࠧࡿࠢࠨഘ") + bstack1lllll1_opy_ (u"ࠢࡾࠤങ"))
                  bstack1ll1lll1l_opy_ = bstack11ll1111l_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡌࡈࡸࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠧച") + str(e))
      if bstack1ll1ll11ll_opy_:
        with bstack1111ll1l1_opy_:
          bstack1111l1l11_opy_ = bstack1ll1ll11ll_opy_.copy()
        for driver in bstack1111l1l11_opy_:
          if bstack1ll1lll1l_opy_ == driver.session_id:
            bstack11l1l1l111_opy_ = driver
    bstack111111111_opy_ = bstack1lll1lll1_opy_.bstack11l1ll1lll_opy_(test.tags)
    if bstack11l1l1l111_opy_:
      threading.current_thread().isA11yTest = bstack1lll1lll1_opy_.bstack1111lll1l_opy_(bstack11l1l1l111_opy_, bstack111111111_opy_)
      threading.current_thread().isAppA11yTest = bstack1lll1lll1_opy_.bstack1111lll1l_opy_(bstack11l1l1l111_opy_, bstack111111111_opy_)
    else:
      threading.current_thread().isA11yTest = bstack111111111_opy_
      threading.current_thread().isAppA11yTest = bstack111111111_opy_
  except:
    pass
  bstack1lllll11ll_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1l11lll11_opy_
  try:
    bstack1l11lll11_opy_ = self._test
  except:
    bstack1l11lll11_opy_ = self.test
def bstack11ll1l1l1l_opy_():
  global bstack11ll1l11l_opy_
  try:
    if os.path.exists(bstack11ll1l11l_opy_):
      os.remove(bstack11ll1l11l_opy_)
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬഛ") + str(e))
def bstack1ll1ll1ll1_opy_():
  global bstack11ll1l11l_opy_
  bstack1l11l1l1ll_opy_ = {}
  lock_file = bstack11ll1l11l_opy_ + bstack1lllll1_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩജ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧഝ"))
    try:
      if not os.path.isfile(bstack11ll1l11l_opy_):
        with open(bstack11ll1l11l_opy_, bstack1lllll1_opy_ (u"ࠬࡽࠧഞ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack11ll1l11l_opy_):
        with open(bstack11ll1l11l_opy_, bstack1lllll1_opy_ (u"࠭ࡲࠨട")) as f:
          content = f.read().strip()
          if content:
            bstack1l11l1l1ll_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩഠ") + str(e))
    return bstack1l11l1l1ll_opy_
  try:
    os.makedirs(os.path.dirname(bstack11ll1l11l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack11ll1l11l_opy_):
        with open(bstack11ll1l11l_opy_, bstack1lllll1_opy_ (u"ࠨࡹࠪഡ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack11ll1l11l_opy_):
        with open(bstack11ll1l11l_opy_, bstack1lllll1_opy_ (u"ࠩࡵࠫഢ")) as f:
          content = f.read().strip()
          if content:
            bstack1l11l1l1ll_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬണ") + str(e))
  finally:
    return bstack1l11l1l1ll_opy_
def bstack11ll1llll1_opy_(platform_index, item_index):
  global bstack11ll1l11l_opy_
  lock_file = bstack11ll1l11l_opy_ + bstack1lllll1_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪത")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨഥ"))
    try:
      bstack1l11l1l1ll_opy_ = {}
      if os.path.exists(bstack11ll1l11l_opy_):
        with open(bstack11ll1l11l_opy_, bstack1lllll1_opy_ (u"࠭ࡲࠨദ")) as f:
          content = f.read().strip()
          if content:
            bstack1l11l1l1ll_opy_ = json.loads(content)
      bstack1l11l1l1ll_opy_[item_index] = platform_index
      with open(bstack11ll1l11l_opy_, bstack1lllll1_opy_ (u"ࠢࡸࠤധ")) as outfile:
        json.dump(bstack1l11l1l1ll_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡻࡷ࡯ࡴࡪࡰࡪࠤࡹࡵࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ന") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack11ll1l11l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack1l11l1l1ll_opy_ = {}
      if os.path.exists(bstack11ll1l11l_opy_):
        with open(bstack11ll1l11l_opy_, bstack1lllll1_opy_ (u"ࠩࡵࠫഩ")) as f:
          content = f.read().strip()
          if content:
            bstack1l11l1l1ll_opy_ = json.loads(content)
      bstack1l11l1l1ll_opy_[item_index] = platform_index
      with open(bstack11ll1l11l_opy_, bstack1lllll1_opy_ (u"ࠥࡻࠧപ")) as outfile:
        json.dump(bstack1l11l1l1ll_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡷࡳ࡫ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩഫ") + str(e))
def bstack1ll111llll_opy_(bstack1lll1111l_opy_):
  global CONFIG
  bstack1l1l1lllll_opy_ = bstack1lllll1_opy_ (u"ࠬ࠭ബ")
  if not bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩഭ") in CONFIG:
    logger.info(bstack1lllll1_opy_ (u"ࠧࡏࡱࠣࡴࡱࡧࡴࡧࡱࡵࡱࡸࠦࡰࡢࡵࡶࡩࡩࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫ࡵࡲࠡࡔࡲࡦࡴࡺࠠࡳࡷࡱࠫമ"))
  try:
    platform = CONFIG[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫയ")][bstack1lll1111l_opy_]
    if bstack1lllll1_opy_ (u"ࠩࡲࡷࠬര") in platform:
      bstack1l1l1lllll_opy_ += str(platform[bstack1lllll1_opy_ (u"ࠪࡳࡸ࠭റ")]) + bstack1lllll1_opy_ (u"ࠫ࠱ࠦࠧല")
    if bstack1lllll1_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨള") in platform:
      bstack1l1l1lllll_opy_ += str(platform[bstack1lllll1_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩഴ")]) + bstack1lllll1_opy_ (u"ࠧ࠭ࠢࠪവ")
    if bstack1lllll1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬശ") in platform:
      bstack1l1l1lllll_opy_ += str(platform[bstack1lllll1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ഷ")]) + bstack1lllll1_opy_ (u"ࠪ࠰ࠥ࠭സ")
    if bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ഹ") in platform:
      bstack1l1l1lllll_opy_ += str(platform[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧഺ")]) + bstack1lllll1_opy_ (u"഻࠭ࠬࠡࠩ")
    if bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩ഼ࠬ") in platform:
      bstack1l1l1lllll_opy_ += str(platform[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ഽ")]) + bstack1lllll1_opy_ (u"ࠩ࠯ࠤࠬാ")
    if bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫി") in platform:
      bstack1l1l1lllll_opy_ += str(platform[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬീ")]) + bstack1lllll1_opy_ (u"ࠬ࠲ࠠࠨു")
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"࠭ࡓࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡰࡨࡶࡦࡺࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡹࡴࡳ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡵࡩࡵࡵࡲࡵࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡳࡳ࠭ൂ") + str(e))
  finally:
    if bstack1l1l1lllll_opy_[len(bstack1l1l1lllll_opy_) - 2:] == bstack1lllll1_opy_ (u"ࠧ࠭ࠢࠪൃ"):
      bstack1l1l1lllll_opy_ = bstack1l1l1lllll_opy_[:-2]
    return bstack1l1l1lllll_opy_
def bstack11llllll1l_opy_(path, bstack1l1l1lllll_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l1lllll1l_opy_ = ET.parse(path)
    bstack11ll11111l_opy_ = bstack1l1lllll1l_opy_.getroot()
    bstack11l111ll1l_opy_ = None
    for suite in bstack11ll11111l_opy_.iter(bstack1lllll1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧൄ")):
      if bstack1lllll1_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ൅") in suite.attrib:
        suite.attrib[bstack1lllll1_opy_ (u"ࠪࡲࡦࡳࡥࠨെ")] += bstack1lllll1_opy_ (u"ࠫࠥ࠭േ") + bstack1l1l1lllll_opy_
        bstack11l111ll1l_opy_ = suite
    bstack1l1l1ll1l1_opy_ = None
    for robot in bstack11ll11111l_opy_.iter(bstack1lllll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫൈ")):
      bstack1l1l1ll1l1_opy_ = robot
    bstack1l11l1l1l1_opy_ = len(bstack1l1l1ll1l1_opy_.findall(bstack1lllll1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൉")))
    if bstack1l11l1l1l1_opy_ == 1:
      bstack1l1l1ll1l1_opy_.remove(bstack1l1l1ll1l1_opy_.findall(bstack1lllll1_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ൊ"))[0])
      bstack11lllll1ll_opy_ = ET.Element(bstack1lllll1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧോ"), attrib={bstack1lllll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧൌ"): bstack1lllll1_opy_ (u"ࠪࡗࡺ࡯ࡴࡦࡵ്ࠪ"), bstack1lllll1_opy_ (u"ࠫ࡮ࡪࠧൎ"): bstack1lllll1_opy_ (u"ࠬࡹ࠰ࠨ൏")})
      bstack1l1l1ll1l1_opy_.insert(1, bstack11lllll1ll_opy_)
      bstack1l1ll1l1ll_opy_ = None
      for suite in bstack1l1l1ll1l1_opy_.iter(bstack1lllll1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൐")):
        bstack1l1ll1l1ll_opy_ = suite
      bstack1l1ll1l1ll_opy_.append(bstack11l111ll1l_opy_)
      bstack1l1ll1ll1_opy_ = None
      for status in bstack11l111ll1l_opy_.iter(bstack1lllll1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ൑")):
        bstack1l1ll1ll1_opy_ = status
      bstack1l1ll1l1ll_opy_.append(bstack1l1ll1ll1_opy_)
    bstack1l1lllll1l_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡸࡳࡪࡰࡪࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹ࠭൒") + str(e))
def bstack1lll11111_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack11lll1l11l_opy_
  global CONFIG
  if bstack1lllll1_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨ൓") in options:
    del options[bstack1lllll1_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢൔ")]
  json_data = bstack1ll1ll1ll1_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack1lllll1_opy_ (u"ࠫࡵࡧࡢࡰࡶࡢࡶࡪࡹࡵ࡭ࡶࡶࠫൕ"), str(item_id), bstack1lllll1_opy_ (u"ࠬࡵࡵࡵࡲࡸࡸ࠳ࡾ࡭࡭ࠩൖ"))
    bstack11llllll1l_opy_(path, bstack1ll111llll_opy_(json_data[item_id]))
  bstack11ll1l1l1l_opy_()
  return bstack11lll1l11l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack11l1111l11_opy_(self, ff_profile_dir):
  global bstack111ll1ll11_opy_
  if not ff_profile_dir:
    return None
  return bstack111ll1ll11_opy_(self, ff_profile_dir)
def bstack11ll1ll111_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack11ll111ll1_opy_
  bstack111l1l1l11_opy_ = []
  if bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩൗ") in CONFIG:
    bstack111l1l1l11_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ൘")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1lllll1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࠤ൙")],
      pabot_args[bstack1lllll1_opy_ (u"ࠤࡹࡩࡷࡨ࡯ࡴࡧࠥ൚")],
      argfile,
      pabot_args.get(bstack1lllll1_opy_ (u"ࠥ࡬࡮ࡼࡥࠣ൛")),
      pabot_args[bstack1lllll1_opy_ (u"ࠦࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠢ൜")],
      platform[0],
      bstack11ll111ll1_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1lllll1_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡦࡪ࡮ࡨࡷࠧ൝")] or [(bstack1lllll1_opy_ (u"ࠨࠢ൞"), None)]
    for platform in enumerate(bstack111l1l1l11_opy_)
  ]
def bstack1l1ll11ll1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack11111llll_opy_=bstack1lllll1_opy_ (u"ࠧࠨൟ")):
  global bstack11l1l1l11l_opy_
  self.platform_index = platform_index
  self.bstack1lllll11l1_opy_ = bstack11111llll_opy_
  bstack11l1l1l11l_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1ll111l11_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1ll11l1ll1_opy_
  global bstack11l1llllll_opy_
  bstack1lllllll11_opy_ = copy.deepcopy(item)
  if not bstack1lllll1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪൠ") in item.options:
    bstack1lllllll11_opy_.options[bstack1lllll1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫൡ")] = []
  bstack11111l1ll_opy_ = bstack1lllllll11_opy_.options[bstack1lllll1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬൢ")].copy()
  for v in bstack1lllllll11_opy_.options[bstack1lllll1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ൣ")]:
    if bstack1lllll1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫ൤") in v:
      bstack11111l1ll_opy_.remove(v)
    if bstack1lllll1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭൥") in v:
      bstack11111l1ll_opy_.remove(v)
    if bstack1lllll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫ൦") in v:
      bstack11111l1ll_opy_.remove(v)
  bstack11111l1ll_opy_.insert(0, bstack1lllll1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞࠺ࡼࡿࠪ൧").format(bstack1lllllll11_opy_.platform_index))
  bstack11111l1ll_opy_.insert(0, bstack1lllll1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࡀࡻࡾࠩ൨").format(bstack1lllllll11_opy_.bstack1lllll11l1_opy_))
  bstack1lllllll11_opy_.options[bstack1lllll1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ൩")] = bstack11111l1ll_opy_
  if bstack11l1llllll_opy_:
    bstack1lllllll11_opy_.options[bstack1lllll1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭൪")].insert(0, bstack1lllll1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗ࠿ࢁࡽࠨ൫").format(bstack11l1llllll_opy_))
  return bstack1ll11l1ll1_opy_(caller_id, datasources, is_last, bstack1lllllll11_opy_, outs_dir)
def bstack1l11l1ll1_opy_(command, item_index):
  try:
    if bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ൬")):
      os.environ[bstack1lllll1_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨ൭")] = json.dumps(CONFIG[bstack1lllll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ൮")][item_index % bstack11ll1l111l_opy_])
    global bstack11l1llllll_opy_
    if bstack11l1llllll_opy_:
      command[0] = command[0].replace(bstack1lllll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ൯"), bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧ൰") + str(
        item_index) + bstack1lllll1_opy_ (u"ࠫࠥ࠭൱") + bstack11l1llllll_opy_, 1)
    else:
      command[0] = command[0].replace(bstack1lllll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ൲"),
                                      bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡹࡤ࡬ࠢࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠢࠪ൳") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦ࡭ࡰࡦ࡬ࡪࡾ࡯࡮ࡨࠢࡦࡳࡲࡳࡡ࡯ࡦࠣࡪࡴࡸࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰ࠽ࠤࢀࢃࠧ൴").format(str(e)))
def bstack1l1l11111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1lll1ll1l1_opy_
  try:
    bstack1l11l1ll1_opy_(command, item_index)
    return bstack1lll1ll1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࡀࠠࡼࡿࠪ൵").format(str(e)))
    raise e
def bstack1ll11l1l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1lll1ll1l1_opy_
  try:
    bstack1l11l1ll1_opy_(command, item_index)
    return bstack1lll1ll1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠳࠰࠴࠷࠿ࠦࡻࡾࠩ൶").format(str(e)))
    try:
      return bstack1lll1ll1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack1lllll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࠷࠴࠱࠴ࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨ൷").format(str(e2)))
      raise e
def bstack1111ll1ll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1lll1ll1l1_opy_
  try:
    bstack1l11l1ll1_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack1lll1ll1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠵࠲࠶࠻࠺ࠡࡽࢀࠫ൸").format(str(e)))
    try:
      return bstack1lll1ll1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack1lllll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦ࠲࠯࠳࠸ࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪ൹").format(str(e2)))
      raise e
def _1111l1ll11_opy_(bstack111lllllll_opy_, item_index, process_timeout, sleep_before_start, bstack1l11ll1ll1_opy_):
  bstack1l11l1ll1_opy_(bstack111lllllll_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack11111ll111_opy_(command, bstack1l1111l1ll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1lll1ll1l1_opy_
  try:
    bstack1l11l1ll1_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack1lll1ll1l1_opy_(command, bstack1l1111l1ll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠺࠴࠰࠻ࠢࡾࢁࠬൺ").format(str(e)))
    try:
      return bstack1lll1ll1l1_opy_(command, bstack1l1111l1ll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1lllll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧൻ").format(str(e2)))
      raise e
def bstack1l1lllllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1lll1ll1l1_opy_
  try:
    process_timeout = _1111l1ll11_opy_(command, item_index, process_timeout, sleep_before_start, bstack1lllll1_opy_ (u"ࠨ࠶࠱࠶ࠬർ"))
    return bstack1lll1ll1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠵࠰࠵࠾ࠥࢁࡽࠨൽ").format(str(e)))
    try:
      return bstack1lll1ll1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1lllll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪൾ").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack1ll1l11111_opy_(self, runner, quiet=False, capture=True):
  global bstack11l11ll11l_opy_
  bstack11l11llll_opy_ = bstack11l11ll11l_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack1lllll1_opy_ (u"ࠫࡪࡾࡣࡦࡲࡷ࡭ࡴࡴ࡟ࡢࡴࡵࠫൿ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1lllll1_opy_ (u"ࠬ࡫ࡸࡤࡡࡷࡶࡦࡩࡥࡣࡣࡦ࡯ࡤࡧࡲࡳࠩ඀")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack11l11llll_opy_
def bstack1l11l111l1_opy_(runner, hook_name, context, element, bstack1l11ll11l1_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1l11l11111_opy_.bstack11l1l1ll_opy_(hook_name, element)
    bstack1l11ll11l1_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1l11l11111_opy_.bstack11l1l1l1_opy_(element)
      if hook_name not in [bstack1lllll1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪඁ"), bstack1lllll1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪං")] and args and hasattr(args[0], bstack1lllll1_opy_ (u"ࠨࡧࡵࡶࡴࡸ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠨඃ")):
        args[0].error_message = bstack1lllll1_opy_ (u"ࠩࠪ඄")
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡨࡢࡰࡧࡰࡪࠦࡨࡰࡱ࡮ࡷࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥ࠻ࠢࡾࢁࠬඅ").format(str(e)))
@measure(event_name=EVENTS.bstack11l1lllll1_opy_, stage=STAGE.bstack11l1l111l1_opy_, hook_type=bstack1lllll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡅࡱࡲࠢආ"), bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack1ll1111lll_opy_(runner, name, context, bstack1l11ll11l1_opy_, *args):
    if runner.hooks.get(bstack1lllll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤඇ")).__name__ != bstack1lllll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࡢࡨࡪ࡬ࡡࡶ࡮ࡷࡣ࡭ࡵ࡯࡬ࠤඈ"):
      bstack1l11l111l1_opy_(runner, name, context, runner, bstack1l11ll11l1_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1111l1l11l_opy_(bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ඉ")) else context.browser
      runner.driver_initialised = bstack1lllll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧඊ")
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡪࠦࡡࡵࡶࡵ࡭ࡧࡻࡴࡦ࠼ࠣࡿࢂ࠭උ").format(str(e)))
def bstack11lll1lll1_opy_(runner, name, context, bstack1l11ll11l1_opy_, *args):
    bstack1l11l111l1_opy_(runner, name, context, context.feature, bstack1l11ll11l1_opy_, *args)
    try:
      if not bstack11l111l1ll_opy_:
        bstack11l1l1l111_opy_ = threading.current_thread().bstackSessionDriver if bstack1111l1l11l_opy_(bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩඌ")) else context.browser
        if is_driver_active(bstack11l1l1l111_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack1lllll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧඍ")
          bstack11ll1l1l11_opy_ = str(runner.feature.name)
          bstack111ll1lll_opy_(context, bstack11ll1l1l11_opy_)
          bstack11l1l1l111_opy_.execute_script(bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪඎ") + json.dumps(bstack11ll1l1l11_opy_) + bstack1lllll1_opy_ (u"࠭ࡽࡾࠩඏ"))
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧඐ").format(str(e)))
def bstack11l1l1l1l_opy_(runner, name, context, bstack1l11ll11l1_opy_, *args):
    if hasattr(context, bstack1lllll1_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪඑ")):
        bstack1l11l11111_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack1lllll1_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫඒ")) else context.feature
    bstack1l11l111l1_opy_(runner, name, context, target, bstack1l11ll11l1_opy_, *args)
@measure(event_name=EVENTS.bstack1l11ll1l11_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack11l1lll1ll_opy_(runner, name, context, bstack1l11ll11l1_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1l11l11111_opy_.start_test(context)
    bstack1l11l111l1_opy_(runner, name, context, context.scenario, bstack1l11ll11l1_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack11llll111_opy_.bstack111ll1lll1_opy_(context, *args)
    try:
      bstack11l1l1l111_opy_ = bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩඓ"), context.browser)
      if is_driver_active(bstack11l1l1l111_opy_):
        bstack1ll111ll_opy_.bstack1111ll1l1l_opy_(bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪඔ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack1lllll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢඕ")
        if (not bstack11l111l1ll_opy_):
          scenario_name = args[0].name
          feature_name = bstack11ll1l1l11_opy_ = str(runner.feature.name)
          bstack11ll1l1l11_opy_ = feature_name + bstack1lllll1_opy_ (u"࠭ࠠ࠮ࠢࠪඖ") + scenario_name
          if runner.driver_initialised == bstack1lllll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤ඗"):
            bstack111ll1lll_opy_(context, bstack11ll1l1l11_opy_)
            bstack11l1l1l111_opy_.execute_script(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭඘") + json.dumps(bstack11ll1l1l11_opy_) + bstack1lllll1_opy_ (u"ࠩࢀࢁࠬ඙"))
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡦࡰࡤࡶ࡮ࡵ࠺ࠡࡽࢀࠫක").format(str(e)))
@measure(event_name=EVENTS.bstack11l1lllll1_opy_, stage=STAGE.bstack11l1l111l1_opy_, hook_type=bstack1lllll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡗࡹ࡫ࡰࠣඛ"), bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack1l1l11ll11_opy_(runner, name, context, bstack1l11ll11l1_opy_, *args):
    bstack1l11l111l1_opy_(runner, name, context, args[0], bstack1l11ll11l1_opy_, *args)
    try:
      bstack11l1l1l111_opy_ = threading.current_thread().bstackSessionDriver if bstack1111l1l11l_opy_(bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫග")) else context.browser
      if is_driver_active(bstack11l1l1l111_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack1lllll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦඝ")
        bstack1l11l11111_opy_.bstack11ll1lll_opy_(args[0])
        if runner.driver_initialised == bstack1lllll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧඞ"):
          feature_name = bstack11ll1l1l11_opy_ = str(runner.feature.name)
          bstack11ll1l1l11_opy_ = feature_name + bstack1lllll1_opy_ (u"ࠨࠢ࠰ࠤࠬඟ") + context.scenario.name
          bstack11l1l1l111_opy_.execute_script(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧච") + json.dumps(bstack11ll1l1l11_opy_) + bstack1lllll1_opy_ (u"ࠪࢁࢂ࠭ඡ"))
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡵࡧࡳ࠾ࠥࢁࡽࠨජ").format(str(e)))
@measure(event_name=EVENTS.bstack11l1lllll1_opy_, stage=STAGE.bstack11l1l111l1_opy_, hook_type=bstack1lllll1_opy_ (u"ࠧࡧࡦࡵࡧࡵࡗࡹ࡫ࡰࠣඣ"), bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack1l1l1lll11_opy_(runner, name, context, bstack1l11ll11l1_opy_, *args):
  bstack1l11l11111_opy_.bstack11ll1ll1_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack11l1l1l111_opy_ = threading.current_thread().bstackSessionDriver if bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඤ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack11l1l1l111_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack1lllll1_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧඥ")
        feature_name = bstack11ll1l1l11_opy_ = str(runner.feature.name)
        bstack11ll1l1l11_opy_ = feature_name + bstack1lllll1_opy_ (u"ࠨࠢ࠰ࠤࠬඦ") + context.scenario.name
        bstack11l1l1l111_opy_.execute_script(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧට") + json.dumps(bstack11ll1l1l11_opy_) + bstack1lllll1_opy_ (u"ࠪࢁࢂ࠭ඨ"))
    if str(step_status).lower() == bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫඩ"):
      bstack1ll11l1ll_opy_ = bstack1lllll1_opy_ (u"ࠬ࠭ඪ")
      bstack11lllllll1_opy_ = bstack1lllll1_opy_ (u"࠭ࠧණ")
      bstack1l1111ll1_opy_ = bstack1lllll1_opy_ (u"ࠧࠨඬ")
      try:
        import traceback
        bstack1ll11l1ll_opy_ = runner.exception.__class__.__name__
        bstack11ll11ll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11lllllll1_opy_ = bstack1lllll1_opy_ (u"ࠨࠢࠪත").join(bstack11ll11ll_opy_)
        bstack1l1111ll1_opy_ = bstack11ll11ll_opy_[-1]
      except Exception as e:
        logger.debug(bstack11ll11l11l_opy_.format(str(e)))
      bstack1ll11l1ll_opy_ += bstack1l1111ll1_opy_
      bstack1lll1l11ll_opy_(context, json.dumps(str(args[0].name) + bstack1lllll1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣථ") + str(bstack11lllllll1_opy_)),
                          bstack1lllll1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤද"))
      if runner.driver_initialised == bstack1lllll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤධ"):
        bstack11lllll11_opy_(getattr(context, bstack1lllll1_opy_ (u"ࠬࡶࡡࡨࡧࠪන"), None), bstack1lllll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ඲"), bstack1ll11l1ll_opy_)
        bstack11l1l1l111_opy_.execute_script(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬඳ") + json.dumps(str(args[0].name) + bstack1lllll1_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢප") + str(bstack11lllllll1_opy_)) + bstack1lllll1_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࡽࡾࠩඵ"))
      if runner.driver_initialised == bstack1lllll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣබ"):
        bstack1l1l1llll_opy_(bstack11l1l1l111_opy_, bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫභ"), bstack1lllll1_opy_ (u"࡙ࠧࡣࡦࡰࡤࡶ࡮ࡵࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤම") + str(bstack1ll11l1ll_opy_))
    else:
      bstack1lll1l11ll_opy_(context, bstack1lllll1_opy_ (u"ࠨࡐࡢࡵࡶࡩࡩࠧࠢඹ"), bstack1lllll1_opy_ (u"ࠢࡪࡰࡩࡳࠧය"))
      if runner.driver_initialised == bstack1lllll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨර"):
        bstack11lllll11_opy_(getattr(context, bstack1lllll1_opy_ (u"ࠩࡳࡥ࡬࡫ࠧ඼"), None), bstack1lllll1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥල"))
      bstack11l1l1l111_opy_.execute_script(bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ඾") + json.dumps(str(args[0].name) + bstack1lllll1_opy_ (u"ࠧࠦ࠭ࠡࡒࡤࡷࡸ࡫ࡤࠢࠤ඿")) + bstack1lllll1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬව"))
      if runner.driver_initialised == bstack1lllll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧශ"):
        bstack1l1l1llll_opy_(bstack11l1l1l111_opy_, bstack1lllll1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣෂ"))
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡳࡵࡧࡳ࠾ࠥࢁࡽࠨස").format(str(e)))
  bstack1l11l111l1_opy_(runner, name, context, args[0], bstack1l11ll11l1_opy_, *args)
@measure(event_name=EVENTS.bstack1l1111l1l_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack1ll1111l1l_opy_(runner, name, context, bstack1l11ll11l1_opy_, *args):
  bstack1l11l11111_opy_.end_test(args[0])
  try:
    bstack1111l1l111_opy_ = args[0].status.name
    bstack11l1l1l111_opy_ = bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩහ"), context.browser)
    bstack11llll111_opy_.bstack1l111llll1_opy_(bstack11l1l1l111_opy_)
    if str(bstack1111l1l111_opy_).lower() == bstack1lllll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫළ"):
      bstack1ll11l1ll_opy_ = bstack1lllll1_opy_ (u"ࠬ࠭ෆ")
      bstack11lllllll1_opy_ = bstack1lllll1_opy_ (u"࠭ࠧ෇")
      bstack1l1111ll1_opy_ = bstack1lllll1_opy_ (u"ࠧࠨ෈")
      try:
        import traceback
        bstack1ll11l1ll_opy_ = runner.exception.__class__.__name__
        bstack11ll11ll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11lllllll1_opy_ = bstack1lllll1_opy_ (u"ࠨࠢࠪ෉").join(bstack11ll11ll_opy_)
        bstack1l1111ll1_opy_ = bstack11ll11ll_opy_[-1]
      except Exception as e:
        logger.debug(bstack11ll11l11l_opy_.format(str(e)))
      bstack1ll11l1ll_opy_ += bstack1l1111ll1_opy_
      bstack1lll1l11ll_opy_(context, json.dumps(str(args[0].name) + bstack1lllll1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮්ࠣ") + str(bstack11lllllll1_opy_)),
                          bstack1lllll1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ෋"))
      if runner.driver_initialised == bstack1lllll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ෌") or runner.driver_initialised == bstack1lllll1_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ෍"):
        bstack11lllll11_opy_(getattr(context, bstack1lllll1_opy_ (u"࠭ࡰࡢࡩࡨࠫ෎"), None), bstack1lllll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢා"), bstack1ll11l1ll_opy_)
        bstack11l1l1l111_opy_.execute_script(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ැ") + json.dumps(str(args[0].name) + bstack1lllll1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣෑ") + str(bstack11lllllll1_opy_)) + bstack1lllll1_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪි"))
      if runner.driver_initialised == bstack1lllll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨී") or runner.driver_initialised == bstack1lllll1_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬු"):
        bstack1l1l1llll_opy_(bstack11l1l1l111_opy_, bstack1lllll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭෕"), bstack1lllll1_opy_ (u"ࠢࡔࡥࡨࡲࡦࡸࡩࡰࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦූ") + str(bstack1ll11l1ll_opy_))
    else:
      bstack1lll1l11ll_opy_(context, bstack1lllll1_opy_ (u"ࠣࡒࡤࡷࡸ࡫ࡤࠢࠤ෗"), bstack1lllll1_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢෘ"))
      if runner.driver_initialised == bstack1lllll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧෙ") or runner.driver_initialised == bstack1lllll1_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫේ"):
        bstack11lllll11_opy_(getattr(context, bstack1lllll1_opy_ (u"ࠬࡶࡡࡨࡧࠪෛ"), None), bstack1lllll1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨො"))
      bstack11l1l1l111_opy_.execute_script(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬෝ") + json.dumps(str(args[0].name) + bstack1lllll1_opy_ (u"ࠣࠢ࠰ࠤࡕࡧࡳࡴࡧࡧࠥࠧෞ")) + bstack1lllll1_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧࢃࡽࠨෟ"))
      if runner.driver_initialised == bstack1lllll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ෠") or runner.driver_initialised == bstack1lllll1_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫ෡"):
        bstack1l1l1llll_opy_(bstack11l1l1l111_opy_, bstack1lllll1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ෢"))
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ෣").format(str(e)))
  bstack1l11l111l1_opy_(runner, name, context, context.scenario, bstack1l11ll11l1_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1lll111111_opy_(runner, name, context, bstack1l11ll11l1_opy_, *args):
    target = context.scenario if hasattr(context, bstack1lllll1_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩ෤")) else context.feature
    bstack1l11l111l1_opy_(runner, name, context, target, bstack1l11ll11l1_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1l1111ll1l_opy_(runner, name, context, bstack1l11ll11l1_opy_, *args):
    try:
      bstack11l1l1l111_opy_ = bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ෥"), context.browser)
      bstack111l11llll_opy_ = bstack1lllll1_opy_ (u"ࠩࠪ෦")
      if context.failed is True:
        bstack111ll1ll1_opy_ = []
        bstack11lll1ll11_opy_ = []
        bstack11llllll11_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack111ll1ll1_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11ll11ll_opy_ = traceback.format_tb(exc_tb)
            bstack111lll111_opy_ = bstack1lllll1_opy_ (u"ࠪࠤࠬ෧").join(bstack11ll11ll_opy_)
            bstack11lll1ll11_opy_.append(bstack111lll111_opy_)
            bstack11llllll11_opy_.append(bstack11ll11ll_opy_[-1])
        except Exception as e:
          logger.debug(bstack11ll11l11l_opy_.format(str(e)))
        bstack1ll11l1ll_opy_ = bstack1lllll1_opy_ (u"ࠫࠬ෨")
        for i in range(len(bstack111ll1ll1_opy_)):
          bstack1ll11l1ll_opy_ += bstack111ll1ll1_opy_[i] + bstack11llllll11_opy_[i] + bstack1lllll1_opy_ (u"ࠬࡢ࡮ࠨ෩")
        bstack111l11llll_opy_ = bstack1lllll1_opy_ (u"࠭ࠠࠨ෪").join(bstack11lll1ll11_opy_)
        if runner.driver_initialised in [bstack1lllll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣ෫"), bstack1lllll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧ෬")]:
          bstack1lll1l11ll_opy_(context, bstack111l11llll_opy_, bstack1lllll1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ෭"))
          bstack11lllll11_opy_(getattr(context, bstack1lllll1_opy_ (u"ࠪࡴࡦ࡭ࡥࠨ෮"), None), bstack1lllll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ෯"), bstack1ll11l1ll_opy_)
          bstack11l1l1l111_opy_.execute_script(bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ෰") + json.dumps(bstack111l11llll_opy_) + bstack1lllll1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭෱"))
          bstack1l1l1llll_opy_(bstack11l1l1l111_opy_, bstack1lllll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢෲ"), bstack1lllll1_opy_ (u"ࠣࡕࡲࡱࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯ࡴࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡠࡳࠨෳ") + str(bstack1ll11l1ll_opy_))
          bstack11ll111l1_opy_ = bstack1lll111l11_opy_(bstack111l11llll_opy_, runner.feature.name, logger)
          if (bstack11ll111l1_opy_ != None):
            bstack1l111llll_opy_.append(bstack11ll111l1_opy_)
      else:
        if runner.driver_initialised in [bstack1lllll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥ෴"), bstack1lllll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢ෵")]:
          bstack1lll1l11ll_opy_(context, bstack1lllll1_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢ෶") + str(runner.feature.name) + bstack1lllll1_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢ෷"), bstack1lllll1_opy_ (u"ࠨࡩ࡯ࡨࡲࠦ෸"))
          bstack11lllll11_opy_(getattr(context, bstack1lllll1_opy_ (u"ࠧࡱࡣࡪࡩࠬ෹"), None), bstack1lllll1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ෺"))
          bstack11l1l1l111_opy_.execute_script(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ෻") + json.dumps(bstack1lllll1_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨ࠾ࠥࠨ෼") + str(runner.feature.name) + bstack1lllll1_opy_ (u"ࠦࠥࡶࡡࡴࡵࡨࡨࠦࠨ෽")) + bstack1lllll1_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫ෾"))
          bstack1l1l1llll_opy_(bstack11l1l1l111_opy_, bstack1lllll1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭෿"))
          bstack11ll111l1_opy_ = bstack1lll111l11_opy_(bstack111l11llll_opy_, runner.feature.name, logger)
          if (bstack11ll111l1_opy_ != None):
            bstack1l111llll_opy_.append(bstack11ll111l1_opy_)
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩ฀").format(str(e)))
    bstack1l11l111l1_opy_(runner, name, context, context.feature, bstack1l11ll11l1_opy_, *args)
@measure(event_name=EVENTS.bstack11l1lllll1_opy_, stage=STAGE.bstack11l1l111l1_opy_, hook_type=bstack1lllll1_opy_ (u"ࠣࡣࡩࡸࡪࡸࡁ࡭࡮ࠥก"), bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack1llllll111_opy_(runner, name, context, bstack1l11ll11l1_opy_, *args):
    bstack1l11l111l1_opy_(runner, name, context, runner, bstack1l11ll11l1_opy_, *args)
def bstack1lll111l1_opy_(self, name, context, *args):
  try:
    if bstack1l11ll111_opy_:
      platform_index = int(threading.current_thread()._name) % bstack11ll1l111l_opy_
      bstack1ll1111ll_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬข")][platform_index]
      os.environ[bstack1lllll1_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫฃ")] = json.dumps(bstack1ll1111ll_opy_)
    global bstack1l11ll11l1_opy_
    if not hasattr(self, bstack1lllll1_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡥࡥࠩค")):
      self.driver_initialised = None
    bstack111ll1llll_opy_ = {
        bstack1lllll1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠩฅ"): bstack1ll1111lll_opy_,
        bstack1lllll1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠧฆ"): bstack11lll1lll1_opy_,
        bstack1lllll1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡵࡣࡪࠫง"): bstack11l1l1l1l_opy_,
        bstack1lllll1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪจ"): bstack11l1lll1ll_opy_,
        bstack1lllll1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠧฉ"): bstack1l1l11ll11_opy_,
        bstack1lllll1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡸࡪࡶࠧช"): bstack1l1l1lll11_opy_,
        bstack1lllll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬซ"): bstack1ll1111l1l_opy_,
        bstack1lllll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡹࡧࡧࠨฌ"): bstack1lll111111_opy_,
        bstack1lllll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ญ"): bstack1l1111ll1l_opy_,
        bstack1lllll1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪฎ"): bstack1llllll111_opy_
    }
    handler = bstack111ll1llll_opy_.get(name, bstack1l11ll11l1_opy_)
    try:
      handler(self, name, context, bstack1l11ll11l1_opy_, *args)
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧࠣ࡬ࡴࡵ࡫ࠡࡪࡤࡲࡩࡲࡥࡳࠢࡾࢁ࠿ࠦࡻࡾࠩฏ").format(name, str(e)))
    if name in [bstack1lllll1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩฐ"), bstack1lllll1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫฑ"), bstack1lllll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧฒ")]:
      try:
        bstack11l1l1l111_opy_ = threading.current_thread().bstackSessionDriver if bstack1111l1l11l_opy_(bstack1lllll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫณ")) else context.browser
        bstack1ll1111111_opy_ = (
          (name == bstack1lllll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩด") and self.driver_initialised == bstack1lllll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦต")) or
          (name == bstack1lllll1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨถ") and self.driver_initialised == bstack1lllll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥท")) or
          (name == bstack1lllll1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫธ") and self.driver_initialised in [bstack1lllll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨน"), bstack1lllll1_opy_ (u"ࠧ࡯࡮ࡴࡶࡨࡴࠧบ")]) or
          (name == bstack1lllll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡴࡦࡲࠪป") and self.driver_initialised == bstack1lllll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧผ"))
        )
        if bstack1ll1111111_opy_:
          self.driver_initialised = None
          if bstack11l1l1l111_opy_ and hasattr(bstack11l1l1l111_opy_, bstack1lllll1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠬฝ")):
            try:
              bstack11l1l1l111_opy_.quit()
            except Exception as e:
              logger.debug(bstack1lllll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡳࡸ࡭ࡹࡺࡩ࡯ࡩࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࠦࡨࡰࡱ࡮࠾ࠥࢁࡽࠨพ").format(str(e)))
      except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡭ࡵ࡯࡬ࠢࡦࡰࡪࡧ࡮ࡶࡲࠣࡪࡴࡸࠠࡼࡿ࠽ࠤࢀࢃࠧฟ").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠫࡈࡸࡩࡵ࡫ࡦࡥࡱࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥࠡࡴࡸࡲࠥ࡮࡯ࡰ࡭ࠣࡿࢂࡀࠠࡼࡿࠪภ").format(name, str(e)))
    try:
      bstack1l11ll11l1_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack1lllll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡲࡶ࡮࡭ࡩ࡯ࡣ࡯ࠤࡧ࡫ࡨࡢࡸࡨࠤ࡭ࡵ࡯࡬ࠢࡾࢁ࠿ࠦࡻࡾࠩม").format(name, str(e2)))
def bstack11l1llll1_opy_(config, startdir):
  return bstack1lllll1_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࠲ࢀࠦย").format(bstack1lllll1_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨร"))
notset = Notset()
def bstack1l11l111ll_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1ll11l111l_opy_
  if str(name).lower() == bstack1lllll1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨฤ"):
    return bstack1lllll1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣล")
  else:
    return bstack1ll11l111l_opy_(self, name, default, skip)
def bstack1l111l1lll_opy_(item, when):
  global bstack11l11111l_opy_
  try:
    bstack11l11111l_opy_(item, when)
  except Exception as e:
    pass
def bstack1l1l1l1l1l_opy_():
  return
def bstack111ll1111l_opy_(type, name, status, reason, bstack1ll11lll11_opy_, bstack1l1ll1ll1l_opy_):
  bstack11111ll11l_opy_ = {
    bstack1lllll1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪฦ"): type,
    bstack1lllll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧว"): {}
  }
  if type == bstack1lllll1_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧศ"):
    bstack11111ll11l_opy_[bstack1lllll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩษ")][bstack1lllll1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ส")] = bstack1ll11lll11_opy_
    bstack11111ll11l_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫห")][bstack1lllll1_opy_ (u"ࠩࡧࡥࡹࡧࠧฬ")] = json.dumps(str(bstack1l1ll1ll1l_opy_))
  if type == bstack1lllll1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫอ"):
    bstack11111ll11l_opy_[bstack1lllll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧฮ")][bstack1lllll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪฯ")] = name
  if type == bstack1lllll1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩะ"):
    bstack11111ll11l_opy_[bstack1lllll1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪั")][bstack1lllll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨา")] = status
    if status == bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩำ"):
      bstack11111ll11l_opy_[bstack1lllll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ิ")][bstack1lllll1_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫี")] = json.dumps(str(reason))
  bstack111l11ll1l_opy_ = bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪึ").format(json.dumps(bstack11111ll11l_opy_))
  return bstack111l11ll1l_opy_
def bstack11l1l1111_opy_(driver_command, response):
    if driver_command == bstack1lllll1_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪื"):
        bstack1ll111ll_opy_.bstack11111l1ll1_opy_({
            bstack1lllll1_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪุ࠭"): response[bstack1lllll1_opy_ (u"ࠨࡸࡤࡰࡺ࡫ูࠧ")],
            bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥฺࠩ"): bstack1ll111ll_opy_.current_test_uuid()
        })
def bstack111l11l11l_opy_(item, call, rep):
  global bstack1lll1l1l1l_opy_
  global bstack1ll1ll11ll_opy_
  global bstack11l111l1ll_opy_
  name = bstack1lllll1_opy_ (u"ࠪࠫ฻")
  try:
    if rep.when == bstack1lllll1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ฼"):
      bstack1ll1lll1l_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack11l111l1ll_opy_:
          name = str(rep.nodeid)
          bstack111111l11_opy_ = bstack111ll1111l_opy_(bstack1lllll1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭฽"), name, bstack1lllll1_opy_ (u"࠭ࠧ฾"), bstack1lllll1_opy_ (u"ࠧࠨ฿"), bstack1lllll1_opy_ (u"ࠨࠩเ"), bstack1lllll1_opy_ (u"ࠩࠪแ"))
          threading.current_thread().bstack1111l111l_opy_ = name
          for driver in bstack1ll1ll11ll_opy_:
            if bstack1ll1lll1l_opy_ == driver.session_id:
              driver.execute_script(bstack111111l11_opy_)
      except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪโ").format(str(e)))
      try:
        bstack111lll11ll_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1lllll1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬใ"):
          status = bstack1lllll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬไ") if rep.outcome.lower() == bstack1lllll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ๅ") else bstack1lllll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧๆ")
          reason = bstack1lllll1_opy_ (u"ࠨࠩ็")
          if status == bstack1lllll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥ่ࠩ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1lllll1_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨ้") if status == bstack1lllll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧ๊ࠫ") else bstack1lllll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵ๋ࠫ")
          data = name + bstack1lllll1_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨ์") if status == bstack1lllll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧํ") else name + bstack1lllll1_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠣࠣࠫ๎") + reason
          bstack1l1l11l1l1_opy_ = bstack111ll1111l_opy_(bstack1lllll1_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫ๏"), bstack1lllll1_opy_ (u"ࠪࠫ๐"), bstack1lllll1_opy_ (u"ࠫࠬ๑"), bstack1lllll1_opy_ (u"ࠬ࠭๒"), level, data)
          for driver in bstack1ll1ll11ll_opy_:
            if bstack1ll1lll1l_opy_ == driver.session_id:
              driver.execute_script(bstack1l1l11l1l1_opy_)
      except Exception as e:
        logger.debug(bstack1lllll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡴࡴࡴࡦࡺࡷࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪ๓").format(str(e)))
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽࢀࠫ๔").format(str(e)))
  bstack1lll1l1l1l_opy_(item, call, rep)
def bstack1l111l1ll_opy_(driver, bstack1111lll11l_opy_, test=None):
  global bstack111lll111l_opy_
  if test != None:
    bstack1ll1ll1111_opy_ = getattr(test, bstack1lllll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭๕"), None)
    bstack11l1lll1l_opy_ = getattr(test, bstack1lllll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ๖"), None)
    PercySDK.screenshot(driver, bstack1111lll11l_opy_, bstack1ll1ll1111_opy_=bstack1ll1ll1111_opy_, bstack11l1lll1l_opy_=bstack11l1lll1l_opy_, bstack1l1l1l1lll_opy_=bstack111lll111l_opy_)
  else:
    PercySDK.screenshot(driver, bstack1111lll11l_opy_)
@measure(event_name=EVENTS.bstack1ll1llll11_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack11l11ll1l_opy_(driver):
  if bstack11l1l11ll_opy_.bstack111l11111_opy_() is True or bstack11l1l11ll_opy_.capturing() is True:
    return
  bstack11l1l11ll_opy_.bstack1lll11l1ll_opy_()
  while not bstack11l1l11ll_opy_.bstack111l11111_opy_():
    bstack111lllll11_opy_ = bstack11l1l11ll_opy_.bstack1111l1111l_opy_()
    bstack1l111l1ll_opy_(driver, bstack111lllll11_opy_)
  bstack11l1l11ll_opy_.bstack1ll11ll11_opy_()
def bstack1lll11llll_opy_(sequence, driver_command, response = None, bstack1l1llll111_opy_ = None, args = None):
    try:
      if sequence != bstack1lllll1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪ๗"):
        return
      if percy.bstack11lll11lll_opy_() == bstack1lllll1_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥ๘"):
        return
      bstack111lllll11_opy_ = bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ๙"), None)
      for command in bstack11ll11lll1_opy_:
        if command == driver_command:
          with bstack1111ll1l1_opy_:
            bstack1111l1l11_opy_ = bstack1ll1ll11ll_opy_.copy()
          for driver in bstack1111l1l11_opy_:
            bstack11l11ll1l_opy_(driver)
      bstack1ll11111ll_opy_ = percy.bstack1l1l1l1l1_opy_()
      if driver_command in bstack111ll1l1ll_opy_[bstack1ll11111ll_opy_]:
        bstack11l1l11ll_opy_.bstack1ll1l1l11l_opy_(bstack111lllll11_opy_, driver_command)
    except Exception as e:
      pass
def bstack1111ll11l1_opy_(framework_name):
  if bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ๚")):
      return
  bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ๛"), True)
  global bstack11l1ll1l1_opy_
  global bstack1l11ll1111_opy_
  global bstack1111l1ll1_opy_
  bstack11l1ll1l1_opy_ = framework_name
  logger.info(bstack1l11111l1l_opy_.format(bstack11l1ll1l1_opy_.split(bstack1lllll1_opy_ (u"ࠨ࠯ࠪ๜"))[0]))
  bstack1lllllll1l_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1l11ll111_opy_:
      Service.start = bstack1l1l1111l1_opy_
      Service.stop = bstack1l1l1ll1ll_opy_
      webdriver.Remote.get = bstack1lll11lll1_opy_
      WebDriver.quit = bstack111l1111l_opy_
      webdriver.Remote.__init__ = bstack1ll11ll111_opy_
    if not bstack1l11ll111_opy_:
        webdriver.Remote.__init__ = bstack1ll1l1ll1_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack11l1l111l_opy_
    bstack1l11ll1111_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1l11ll111_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1l1111111l_opy_
  except Exception as e:
    pass
  bstack1l111l1111_opy_()
  if not bstack1l11ll1111_opy_:
    bstack11111l1l1l_opy_(bstack1lllll1_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦ๝"), bstack11l11lllll_opy_)
  if bstack1l1l11l111_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack1lllll1_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ๞")) and callable(getattr(RemoteConnection, bstack1lllll1_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ๟"))):
        RemoteConnection._get_proxy_url = bstack11ll111l11_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack11ll111l11_opy_
    except Exception as e:
      logger.error(bstack111l11l1l1_opy_.format(str(e)))
  if bstack111llll11_opy_():
    bstack1l11l1111_opy_(CONFIG, logger)
  if (bstack1lllll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ๠") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack11lll11lll_opy_() == bstack1lllll1_opy_ (u"ࠨࡴࡳࡷࡨࠦ๡"):
          bstack11ll11l111_opy_(bstack1lll11llll_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack11l1111l11_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack111llllll_opy_
      except Exception as e:
        logger.warn(bstack111l1l11ll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack11l1lll1l1_opy_
      except Exception as e:
        logger.debug(bstack1111111l1_opy_ + str(e))
    except Exception as e:
      bstack11111l1l1l_opy_(e, bstack111l1l11ll_opy_)
    Output.start_test = bstack1l111l11ll_opy_
    Output.end_test = bstack1l11lll1ll_opy_
    TestStatus.__init__ = bstack1l1l1ll1l_opy_
    QueueItem.__init__ = bstack1l1ll11ll1_opy_
    pabot._create_items = bstack11ll1ll111_opy_
    try:
      from pabot import __version__ as bstack1l1111ll11_opy_
      if version.parse(bstack1l1111ll11_opy_) >= version.parse(bstack1lllll1_opy_ (u"ࠧ࠶࠰࠳࠲࠵࠭๢")):
        pabot._run = bstack11111ll111_opy_
      elif version.parse(bstack1l1111ll11_opy_) >= version.parse(bstack1lllll1_opy_ (u"ࠨ࠶࠱࠶࠳࠶ࠧ๣")):
        pabot._run = bstack1l1lllllll_opy_
      elif version.parse(bstack1l1111ll11_opy_) >= version.parse(bstack1lllll1_opy_ (u"ࠩ࠵࠲࠶࠻࠮࠱ࠩ๤")):
        pabot._run = bstack1111ll1ll1_opy_
      elif version.parse(bstack1l1111ll11_opy_) >= version.parse(bstack1lllll1_opy_ (u"ࠪ࠶࠳࠷࠳࠯࠲ࠪ๥")):
        pabot._run = bstack1ll11l1l11_opy_
      else:
        pabot._run = bstack1l1l11111l_opy_
    except Exception as e:
      pabot._run = bstack1l1l11111l_opy_
    pabot._create_command_for_execution = bstack1ll111l11_opy_
    pabot._report_results = bstack1lll11111_opy_
  if bstack1lllll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ๦") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11111l1l1l_opy_(e, bstack111l1ll11_opy_)
    Runner.run_hook = bstack1lll111l1_opy_
    Step.run = bstack1ll1l11111_opy_
  if bstack1lllll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ๧") in str(framework_name).lower():
    if not bstack1l11ll111_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack11l1llll1_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1l1l1l1l1l_opy_
      Config.getoption = bstack1l11l111ll_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack111l11l11l_opy_
    except Exception as e:
      pass
def bstack1l1l11lll1_opy_():
  global CONFIG
  if bstack1lllll1_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭๨") in CONFIG and int(CONFIG[bstack1lllll1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ๩")]) > 1:
    logger.warn(bstack1l1llll1l1_opy_)
def bstack1111ll11l_opy_(arg, bstack111l1111_opy_, bstack111ll11lll_opy_=None):
  global CONFIG
  global bstack1ll1lll1ll_opy_
  global bstack11ll1lll11_opy_
  global bstack1l11ll111_opy_
  global bstack11l1111l_opy_
  bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ๪")
  if bstack111l1111_opy_ and isinstance(bstack111l1111_opy_, str):
    bstack111l1111_opy_ = eval(bstack111l1111_opy_)
  CONFIG = bstack111l1111_opy_[bstack1lllll1_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ๫")]
  bstack1ll1lll1ll_opy_ = bstack111l1111_opy_[bstack1lllll1_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫ๬")]
  bstack11ll1lll11_opy_ = bstack111l1111_opy_[bstack1lllll1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭๭")]
  bstack1l11ll111_opy_ = bstack111l1111_opy_[bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ๮")]
  bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ๯"), bstack1l11ll111_opy_)
  os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ๰")] = bstack11ll111l1l_opy_
  os.environ[bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠧ๱")] = json.dumps(CONFIG)
  os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡊࡘࡆࡤ࡛ࡒࡍࠩ๲")] = bstack1ll1lll1ll_opy_
  os.environ[bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ๳")] = str(bstack11ll1lll11_opy_)
  os.environ[bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪ๴")] = str(True)
  if bstack1111l1l1l_opy_(arg, [bstack1lllll1_opy_ (u"ࠬ࠳࡮ࠨ๵"), bstack1lllll1_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ๶")]) != -1:
    os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡂࡔࡄࡐࡑࡋࡌࠨ๷")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1lll1l1lll_opy_)
    return
  bstack11l111l11l_opy_()
  global bstack1l1lll1l1_opy_
  global bstack111lll111l_opy_
  global bstack11ll111ll1_opy_
  global bstack11l1llllll_opy_
  global bstack111llll1l1_opy_
  global bstack1111l1ll1_opy_
  global bstack1ll1l111l1_opy_
  arg.append(bstack1lllll1_opy_ (u"ࠣ࠯࡚ࠦ๸"))
  arg.append(bstack1lllll1_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦ࠼ࡐࡳࡩࡻ࡬ࡦࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡭ࡲࡶ࡯ࡳࡶࡨࡨ࠿ࡶࡹࡵࡧࡶࡸ࠳ࡖࡹࡵࡧࡶࡸ࡜ࡧࡲ࡯࡫ࡱ࡫ࠧ๹"))
  arg.append(bstack1lllll1_opy_ (u"ࠥ࠱࡜ࠨ๺"))
  arg.append(bstack1lllll1_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨ࠾࡙࡮ࡥࠡࡪࡲࡳࡰ࡯࡭ࡱ࡮ࠥ๻"))
  global bstack1ll11llll_opy_
  global bstack1ll1lll1l1_opy_
  global bstack1l11lllll_opy_
  global bstack1lllll11ll_opy_
  global bstack111ll1ll11_opy_
  global bstack11l1l1l11l_opy_
  global bstack1ll11l1ll1_opy_
  global bstack111l111111_opy_
  global bstack1111l1llll_opy_
  global bstack11ll1ll1l_opy_
  global bstack1ll11l111l_opy_
  global bstack11l11111l_opy_
  global bstack1lll1l1l1l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll11llll_opy_ = webdriver.Remote.__init__
    bstack1ll1lll1l1_opy_ = WebDriver.quit
    bstack111l111111_opy_ = WebDriver.close
    bstack1111l1llll_opy_ = WebDriver.get
    bstack1l11lllll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack11lll1lll_opy_(CONFIG) and bstack1ll11ll1l_opy_():
    if bstack11l1l1lll1_opy_() < version.parse(bstack1l111ll1l1_opy_):
      logger.error(bstack1ll11l11ll_opy_.format(bstack11l1l1lll1_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1lllll1_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭๼")) and callable(getattr(RemoteConnection, bstack1lllll1_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ๽"))):
          bstack11ll1ll1l_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack11ll1ll1l_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack111l11l1l1_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1ll11l111l_opy_ = Config.getoption
    from _pytest import runner
    bstack11l11111l_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1llll111l_opy_)
  try:
    from pytest_bdd import reporting
    bstack1lll1l1l1l_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1lllll1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨ๾"))
  bstack11ll111ll1_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ๿"), {}).get(bstack1lllll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ຀"))
  bstack1ll1l111l1_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack1lllll111l_opy_():
      bstack1l1ll11ll_opy_.invoke(Events.CONNECT, bstack1ll11l11l1_opy_())
    platform_index = int(os.environ.get(bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪກ"), bstack1lllll1_opy_ (u"ࠫ࠵࠭ຂ")))
  else:
    bstack1111ll11l1_opy_(bstack1lllll1lll_opy_)
  os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭຃")] = CONFIG[bstack1lllll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨຄ")]
  os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪ຅")] = CONFIG[bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫຆ")]
  os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬງ")] = bstack1l11ll111_opy_.__str__()
  from _pytest.config import main as bstack1l1lll111l_opy_
  bstack11lll1ll1_opy_ = []
  try:
    exit_code = bstack1l1lll111l_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack11l11l1l11_opy_()
    if bstack1lllll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧຈ") in multiprocessing.current_process().__dict__.keys():
      for bstack11l111l11_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11lll1ll1_opy_.append(bstack11l111l11_opy_)
    try:
      bstack111l1lll1l_opy_ = (bstack11lll1ll1_opy_, int(exit_code))
      bstack111ll11lll_opy_.append(bstack111l1lll1l_opy_)
    except:
      bstack111ll11lll_opy_.append((bstack11lll1ll1_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack11lll1ll1_opy_.append({bstack1lllll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩຉ"): bstack1lllll1_opy_ (u"ࠬࡖࡲࡰࡥࡨࡷࡸࠦࠧຊ") + os.environ.get(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭຋")), bstack1lllll1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ຌ"): traceback.format_exc(), bstack1lllll1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧຍ"): int(os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩຎ")))})
    bstack111ll11lll_opy_.append((bstack11lll1ll1_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack1lllll1_opy_ (u"ࠥࡶࡪࡺࡲࡪࡧࡶࠦຏ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack1l11l1lll_opy_ = e.__class__.__name__
    print(bstack1lllll1_opy_ (u"ࠦࠪࡹ࠺ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡤࡨ࡬ࡦࡼࡥࠡࡶࡨࡷࡹࠦࠥࡴࠤຐ") % (bstack1l11l1lll_opy_, e))
    return 1
def bstack1ll1l111l_opy_(arg):
  global bstack1l1l1l1111_opy_
  bstack1111ll11l1_opy_(bstack1l11llll1l_opy_)
  os.environ[bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ຑ")] = str(bstack11ll1lll11_opy_)
  retries = bstack11l111ll_opy_.bstack111ll1ll_opy_(CONFIG)
  status_code = 0
  if bstack11l111ll_opy_.bstack1111111l_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack1l1ll1l1l_opy_
    status_code = bstack1l1ll1l1l_opy_(arg)
  if status_code != 0:
    bstack1l1l1l1111_opy_ = status_code
def bstack11l1l11l11_opy_():
  logger.info(bstack11llll11ll_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1lllll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬຒ"), help=bstack1lllll1_opy_ (u"ࠧࡈࡧࡱࡩࡷࡧࡴࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡥࡲࡲ࡫࡯ࡧࠨຓ"))
  parser.add_argument(bstack1lllll1_opy_ (u"ࠨ࠯ࡸࠫດ"), bstack1lllll1_opy_ (u"ࠩ࠰࠱ࡺࡹࡥࡳࡰࡤࡱࡪ࠭ຕ"), help=bstack1lllll1_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡶࡵࡨࡶࡳࡧ࡭ࡦࠩຖ"))
  parser.add_argument(bstack1lllll1_opy_ (u"ࠫ࠲ࡱࠧທ"), bstack1lllll1_opy_ (u"ࠬ࠳࠭࡬ࡧࡼࠫຘ"), help=bstack1lllll1_opy_ (u"࡙࠭ࡰࡷࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠧນ"))
  parser.add_argument(bstack1lllll1_opy_ (u"ࠧ࠮ࡨࠪບ"), bstack1lllll1_opy_ (u"ࠨ࠯࠰ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ປ"), help=bstack1lllll1_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨຜ"))
  bstack1l1l111lll_opy_ = parser.parse_args()
  try:
    bstack1l1l111l1l_opy_ = bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡪࡩࡳ࡫ࡲࡪࡥ࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧຝ")
    if bstack1l1l111lll_opy_.framework and bstack1l1l111lll_opy_.framework not in (bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫພ"), bstack1lllll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭ຟ")):
      bstack1l1l111l1l_opy_ = bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠯ࡻࡰࡰ࠳ࡹࡡ࡮ࡲ࡯ࡩࠬຠ")
    bstack1111ll111_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1l111l1l_opy_)
    bstack1ll11l1l1l_opy_ = open(bstack1111ll111_opy_, bstack1lllll1_opy_ (u"ࠧࡳࠩມ"))
    bstack11l1l1ll1l_opy_ = bstack1ll11l1l1l_opy_.read()
    bstack1ll11l1l1l_opy_.close()
    if bstack1l1l111lll_opy_.username:
      bstack11l1l1ll1l_opy_ = bstack11l1l1ll1l_opy_.replace(bstack1lllll1_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨຢ"), bstack1l1l111lll_opy_.username)
    if bstack1l1l111lll_opy_.key:
      bstack11l1l1ll1l_opy_ = bstack11l1l1ll1l_opy_.replace(bstack1lllll1_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫຣ"), bstack1l1l111lll_opy_.key)
    if bstack1l1l111lll_opy_.framework:
      bstack11l1l1ll1l_opy_ = bstack11l1l1ll1l_opy_.replace(bstack1lllll1_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ຤"), bstack1l1l111lll_opy_.framework)
    file_name = bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧລ")
    file_path = os.path.abspath(file_name)
    bstack1l111l111_opy_ = open(file_path, bstack1lllll1_opy_ (u"ࠬࡽࠧ຦"))
    bstack1l111l111_opy_.write(bstack11l1l1ll1l_opy_)
    bstack1l111l111_opy_.close()
    logger.info(bstack1ll1l1l1l_opy_)
    try:
      os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨວ")] = bstack1l1l111lll_opy_.framework if bstack1l1l111lll_opy_.framework != None else bstack1lllll1_opy_ (u"ࠢࠣຨ")
      config = yaml.safe_load(bstack11l1l1ll1l_opy_)
      config[bstack1lllll1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨຩ")] = bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠯ࡶࡩࡹࡻࡰࠨສ")
      bstack1l1ll1111_opy_(bstack11l1l111ll_opy_, config)
    except Exception as e:
      logger.debug(bstack111l111l1l_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack11lllllll_opy_.format(str(e)))
def bstack1l1ll1111_opy_(bstack11ll1lll1l_opy_, config, bstack11lll1l111_opy_={}):
  global bstack1l11ll111_opy_
  global bstack11llllllll_opy_
  global bstack11l1111l_opy_
  if not config:
    return
  bstack111l1ll1l1_opy_ = bstack1111lll1l1_opy_ if not bstack1l11ll111_opy_ else (
    bstack1l1llll11_opy_ if bstack1lllll1_opy_ (u"ࠪࡥࡵࡶࠧຫ") in config else (
        bstack1ll111l1l_opy_ if config.get(bstack1lllll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨຬ")) else bstack1l1lll111_opy_
    )
)
  bstack1l11l11ll1_opy_ = False
  bstack11ll1ll11_opy_ = False
  if bstack1l11ll111_opy_ is True:
      if bstack1lllll1_opy_ (u"ࠬࡧࡰࡱࠩອ") in config:
          bstack1l11l11ll1_opy_ = True
      else:
          bstack11ll1ll11_opy_ = True
  bstack1l1l1l1l11_opy_ = bstack1l1lll1l1l_opy_.bstack1lll1111ll_opy_(config, bstack11llllllll_opy_)
  bstack1ll1lllll_opy_ = bstack1l1ll11111_opy_()
  data = {
    bstack1lllll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨຮ"): config[bstack1lllll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩຯ")],
    bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫະ"): config[bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬັ")],
    bstack1lllll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧາ"): bstack11ll1lll1l_opy_,
    bstack1lllll1_opy_ (u"ࠫࡩ࡫ࡴࡦࡥࡷࡩࡩࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨຳ"): os.environ.get(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧິ"), bstack11llllllll_opy_),
    bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨີ"): bstack11lll1111_opy_,
    bstack1lllll1_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭ࠩຶ"): bstack1llllllll1_opy_(),
    bstack1lllll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫື"): {
      bstack1lllll1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱຸࠧ"): str(config[bstack1lllll1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧູࠪ")]) if bstack1lllll1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨ຺ࠫ") in config else bstack1lllll1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨົ"),
      bstack1lllll1_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࡗࡧࡵࡷ࡮ࡵ࡮ࠨຼ"): sys.version,
      bstack1lllll1_opy_ (u"ࠧࡳࡧࡩࡩࡷࡸࡥࡳࠩຽ"): bstack1l1111l1l1_opy_(os.environ.get(bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ຾"), bstack11llllllll_opy_)),
      bstack1lllll1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ຿"): bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪເ"),
      bstack1lllll1_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬແ"): bstack111l1ll1l1_opy_,
      bstack1lllll1_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪໂ"): bstack1l1l1l1l11_opy_,
      bstack1lllll1_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡶࡷ࡬ࡨࠬໃ"): os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬໄ")],
      bstack1lllll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ໅"): os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫໆ"), bstack11llllllll_opy_),
      bstack1lllll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭໇"): bstack11ll11llll_opy_(os.environ.get(bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ່࠭"), bstack11llllllll_opy_)),
      bstack1lllll1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮້ࠫ"): bstack1ll1lllll_opy_.get(bstack1lllll1_opy_ (u"࠭࡮ࡢ࡯ࡨ໊ࠫ")),
      bstack1lllll1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ໋࠭"): bstack1ll1lllll_opy_.get(bstack1lllll1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ໌")),
      bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬໍ"): config[bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໎")] if config[bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ໏")] else bstack1lllll1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨ໐"),
      bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ໑"): str(config[bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ໒")]) if bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໓") in config else bstack1lllll1_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥ໔"),
      bstack1lllll1_opy_ (u"ࠪࡳࡸ࠭໕"): sys.platform,
      bstack1lllll1_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭໖"): socket.gethostname(),
      bstack1lllll1_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ໗"): bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ໘"))
    }
  }
  if not bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ໙")) is None:
    data[bstack1lllll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໚")][bstack1lllll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡑࡪࡺࡡࡥࡣࡷࡥࠬ໛")] = {
      bstack1lllll1_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪໜ"): bstack1lllll1_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩໝ"),
      bstack1lllll1_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬໞ"): bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭ໟ")),
      bstack1lllll1_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࡎࡶ࡯ࡥࡩࡷ࠭໠"): bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡐࡲࠫ໡"))
    }
  if bstack11ll1lll1l_opy_ == bstack1111l11ll1_opy_:
    data[bstack1lllll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໢")][bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡅࡲࡲ࡫࡯ࡧࠨ໣")] = bstack11ll1ll11l_opy_(config)
    data[bstack1lllll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ໤")][bstack1lllll1_opy_ (u"ࠬ࡯ࡳࡑࡧࡵࡧࡾࡇࡵࡵࡱࡈࡲࡦࡨ࡬ࡦࡦࠪ໥")] = percy.bstack11l1l11lll_opy_
    data[bstack1lllll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ໦")][bstack1lllll1_opy_ (u"ࠧࡱࡧࡵࡧࡾࡈࡵࡪ࡮ࡧࡍࡩ࠭໧")] = percy.percy_build_id
  if not bstack11l111ll_opy_.bstack11l1ll1ll1_opy_(CONFIG):
    data[bstack1lllll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໨")][bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠭໩")] = bstack11l111ll_opy_.bstack11l1ll1ll1_opy_(CONFIG)
  bstack11l11ll1_opy_ = bstack11l11lll_opy_.bstack11111l1l_opy_(CONFIG, logger)
  bstack1111l1l1_opy_ = bstack11l111ll_opy_.bstack11111l1l_opy_(config=CONFIG)
  if bstack11l11ll1_opy_ is not None and bstack1111l1l1_opy_ is not None and bstack1111l1l1_opy_.bstack111ll111_opy_():
    data[bstack1lllll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໪")][bstack1111l1l1_opy_.bstack1ll1l1llll_opy_()] = bstack11l11ll1_opy_.bstack111l11ll11_opy_()
  update(data[bstack1lllll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ໫")], bstack11lll1l111_opy_)
  try:
    response = bstack1l1111111_opy_(bstack1lllll1_opy_ (u"ࠬࡖࡏࡔࡖࠪ໬"), bstack1lll1ll11l_opy_(bstack11l1ll1l1l_opy_), data, {
      bstack1lllll1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ໭"): (config[bstack1lllll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ໮")], config[bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ໯")])
    })
    if response:
      logger.debug(bstack111l1lll11_opy_.format(bstack11ll1lll1l_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack111llll1l_opy_.format(str(e)))
def bstack1l1111l1l1_opy_(framework):
  return bstack1lllll1_opy_ (u"ࠤࡾࢁ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨ໰").format(str(framework), __version__) if framework else bstack1lllll1_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦ໱").format(
    __version__)
def bstack11l111l11l_opy_():
  global CONFIG
  global bstack111ll11111_opy_
  if bool(CONFIG):
    return
  try:
    bstack1ll1ll1ll_opy_()
    logger.debug(bstack1ll111l111_opy_.format(str(CONFIG)))
    bstack111ll11111_opy_ = bstack1ll11111l1_opy_.configure_logger(CONFIG, bstack111ll11111_opy_)
    bstack1lllllll1l_opy_()
  except Exception as e:
    logger.error(bstack1lllll1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵ࠲ࠠࡦࡴࡵࡳࡷࡀࠠࠣ໲") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1ll111lll1_opy_
  atexit.register(bstack1ll1lll11l_opy_)
  signal.signal(signal.SIGINT, bstack1ll1l11l11_opy_)
  signal.signal(signal.SIGTERM, bstack1ll1l11l11_opy_)
def bstack1ll111lll1_opy_(exctype, value, traceback):
  global bstack1ll1ll11ll_opy_
  try:
    for driver in bstack1ll1ll11ll_opy_:
      bstack1l1l1llll_opy_(driver, bstack1lllll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ໳"), bstack1lllll1_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤ໴") + str(value))
  except Exception:
    pass
  logger.info(bstack1l1l11ll1l_opy_)
  bstack11l1l1111l_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack11l1l1111l_opy_(message=bstack1lllll1_opy_ (u"ࠧࠨ໵"), bstack1l1l1lll1l_opy_ = False):
  global CONFIG
  bstack1l11l11l1_opy_ = bstack1lllll1_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡆࡺࡦࡩࡵࡺࡩࡰࡰࠪ໶") if bstack1l1l1lll1l_opy_ else bstack1lllll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ໷")
  try:
    if message:
      bstack11lll1l111_opy_ = {
        bstack1l11l11l1_opy_ : str(message)
      }
      bstack1l1ll1111_opy_(bstack1111l11ll1_opy_, CONFIG, bstack11lll1l111_opy_)
    else:
      bstack1l1ll1111_opy_(bstack1111l11ll1_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1l1l11ll1_opy_.format(str(e)))
def bstack11111ll1l1_opy_(bstack111l1llll1_opy_, size):
  bstack111lll1l11_opy_ = []
  while len(bstack111l1llll1_opy_) > size:
    bstack111l1l111_opy_ = bstack111l1llll1_opy_[:size]
    bstack111lll1l11_opy_.append(bstack111l1l111_opy_)
    bstack111l1llll1_opy_ = bstack111l1llll1_opy_[size:]
  bstack111lll1l11_opy_.append(bstack111l1llll1_opy_)
  return bstack111lll1l11_opy_
def bstack11111llll1_opy_(args):
  if bstack1lllll1_opy_ (u"ࠪ࠱ࡲ࠭໸") in args and bstack1lllll1_opy_ (u"ࠫࡵࡪࡢࠨ໹") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack111l1111ll_opy_, stage=STAGE.bstack1llll1lll1_opy_)
def run_on_browserstack(bstack1l1l111ll_opy_=None, bstack111ll11lll_opy_=None, bstack1l1111lll1_opy_=False):
  global CONFIG
  global bstack1ll1lll1ll_opy_
  global bstack11ll1lll11_opy_
  global bstack11llllllll_opy_
  global bstack11l1111l_opy_
  bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"ࠬ࠭໺")
  bstack1l1ll111l1_opy_(bstack1111lllll1_opy_, logger)
  if bstack1l1l111ll_opy_ and isinstance(bstack1l1l111ll_opy_, str):
    bstack1l1l111ll_opy_ = eval(bstack1l1l111ll_opy_)
  if bstack1l1l111ll_opy_:
    CONFIG = bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭໻")]
    bstack1ll1lll1ll_opy_ = bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ໼")]
    bstack11ll1lll11_opy_ = bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ໽")]
    bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ໾"), bstack11ll1lll11_opy_)
    bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ໿")
  bstack11l1111l_opy_.set_property(bstack1lllll1_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭ༀ"), uuid4().__str__())
  logger.info(bstack1lllll1_opy_ (u"࡙ࠬࡄࡌࠢࡵࡹࡳࠦࡳࡵࡣࡵࡸࡪࡪࠠࡸ࡫ࡷ࡬ࠥ࡯ࡤ࠻ࠢࠪ༁") + bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ༂")));
  logger.debug(bstack1lllll1_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥ࠿ࠪ༃") + bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪ༄")))
  if not bstack1l1111lll1_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1lll1l1lll_opy_)
      return
    if sys.argv[1] == bstack1lllll1_opy_ (u"ࠩ࠰࠱ࡻ࡫ࡲࡴ࡫ࡲࡲࠬ༅") or sys.argv[1] == bstack1lllll1_opy_ (u"ࠪ࠱ࡻ࠭༆"):
      logger.info(bstack1lllll1_opy_ (u"ࠫࡇࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡔࡾࡺࡨࡰࡰࠣࡗࡉࡑࠠࡷࡽࢀࠫ༇").format(__version__))
      return
    if sys.argv[1] == bstack1lllll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ༈"):
      bstack11l1l11l11_opy_()
      return
  args = sys.argv
  bstack11l111l11l_opy_()
  global bstack1l1lll1l1_opy_
  global bstack11ll1l111l_opy_
  global bstack1ll1l111l1_opy_
  global bstack1l1l1ll111_opy_
  global bstack111lll111l_opy_
  global bstack11ll111ll1_opy_
  global bstack11l1llllll_opy_
  global bstack111l1l11l_opy_
  global bstack111llll1l1_opy_
  global bstack1111l1ll1_opy_
  global bstack11lllll111_opy_
  bstack11ll1l111l_opy_ = len(CONFIG.get(bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ༉"), []))
  if not bstack11ll111l1l_opy_:
    if args[1] == bstack1lllll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༊") or args[1] == bstack1lllll1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩ་"):
      bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༌")
      args = args[2:]
    elif args[1] == bstack1lllll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ།"):
      bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༎")
      args = args[2:]
    elif args[1] == bstack1lllll1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ༏"):
      bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ༐")
      args = args[2:]
    elif args[1] == bstack1lllll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ༑"):
      bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ༒")
      args = args[2:]
    elif args[1] == bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ༓"):
      bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ༔")
      args = args[2:]
    elif args[1] == bstack1lllll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ༕"):
      bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ༖")
      args = args[2:]
    else:
      if not bstack1lllll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༗") in CONFIG or str(CONFIG[bstack1lllll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭༘ࠪ")]).lower() in [bstack1lllll1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ༙"), bstack1lllll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ༚")]:
        bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༛")
        args = args[1:]
      elif str(CONFIG[bstack1lllll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ༜")]).lower() == bstack1lllll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༝"):
        bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ༞")
        args = args[1:]
      elif str(CONFIG[bstack1lllll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༟")]).lower() == bstack1lllll1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ༠"):
        bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༡")
        args = args[1:]
      elif str(CONFIG[bstack1lllll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭༢")]).lower() == bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༣"):
        bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ༤")
        args = args[1:]
      elif str(CONFIG[bstack1lllll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༥")]).lower() == bstack1lllll1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ༦"):
        bstack11ll111l1l_opy_ = bstack1lllll1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ༧")
        args = args[1:]
      else:
        os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ༨")] = bstack11ll111l1l_opy_
        bstack1l1llllll_opy_(bstack11llll1l1l_opy_)
  os.environ[bstack1lllll1_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫ༩")] = bstack11ll111l1l_opy_
  bstack11llllllll_opy_ = bstack11ll111l1l_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack11lll1l11_opy_ = bstack1111l1lll1_opy_[bstack1lllll1_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗ࠱ࡇࡊࡄࠨ༪")] if bstack11ll111l1l_opy_ == bstack1lllll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ༫") and bstack1ll11llll1_opy_() else bstack11ll111l1l_opy_
      bstack1l1ll11ll_opy_.invoke(Events.bstack1lll11l111_opy_, bstack1llll1l1l1_opy_(
        sdk_version=__version__,
        path_config=bstack1111l11l1l_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack11lll1l11_opy_,
        frameworks=[bstack11lll1l11_opy_],
        framework_versions={
          bstack11lll1l11_opy_: bstack11ll11llll_opy_(bstack1lllll1_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬ༬") if bstack11ll111l1l_opy_ in [bstack1lllll1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭༭"), bstack1lllll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ༮"), bstack1lllll1_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ༯")] else bstack11ll111l1l_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack1lllll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧ༰"), None):
        CONFIG[bstack1lllll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨ༱")] = cli.config.get(bstack1lllll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢ༲"), None)
    except Exception as e:
      bstack1l1ll11ll_opy_.invoke(Events.bstack1111l1l1ll_opy_, e.__traceback__, 1)
    if bstack11ll1lll11_opy_:
      CONFIG[bstack1lllll1_opy_ (u"ࠨࡡࡱࡲࠥ༳")] = cli.config[bstack1lllll1_opy_ (u"ࠢࡢࡲࡳࠦ༴")]
      logger.info(bstack111l1ll1l_opy_.format(CONFIG[bstack1lllll1_opy_ (u"ࠨࡣࡳࡴ༵ࠬ")]))
  else:
    bstack1l1ll11ll_opy_.clear()
  global bstack1lll111ll1_opy_
  global bstack111l11l11_opy_
  if bstack1l1l111ll_opy_:
    try:
      bstack1l11llll11_opy_ = datetime.datetime.now()
      os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ༶")] = bstack11ll111l1l_opy_
      bstack1l1ll1111_opy_(bstack11lllll1l1_opy_, CONFIG)
      cli.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡵࡧ࡯ࡤࡺࡥࡴࡶࡢࡥࡹࡺࡥ࡮ࡲࡷࡩࡩࠨ༷"), datetime.datetime.now() - bstack1l11llll11_opy_)
    except Exception as e:
      logger.debug(bstack111l1lllll_opy_.format(str(e)))
  global bstack1ll11llll_opy_
  global bstack1ll1lll1l1_opy_
  global bstack1l111111l1_opy_
  global bstack11llll1l11_opy_
  global bstack1l11ll1l1_opy_
  global bstack11ll111111_opy_
  global bstack1lllll11ll_opy_
  global bstack111ll1ll11_opy_
  global bstack1lll1ll1l1_opy_
  global bstack11l1l1l11l_opy_
  global bstack1ll11l1ll1_opy_
  global bstack111l111111_opy_
  global bstack1l11ll11l1_opy_
  global bstack11l11ll11l_opy_
  global bstack1111l1llll_opy_
  global bstack11ll1ll1l_opy_
  global bstack1ll11l111l_opy_
  global bstack11l11111l_opy_
  global bstack11lll1l11l_opy_
  global bstack1lll1l1l1l_opy_
  global bstack1l11lllll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll11llll_opy_ = webdriver.Remote.__init__
    bstack1ll1lll1l1_opy_ = WebDriver.quit
    bstack111l111111_opy_ = WebDriver.close
    bstack1111l1llll_opy_ = WebDriver.get
    bstack1l11lllll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1lll111ll1_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1lll1l1ll1_opy_
    bstack111l11l11_opy_ = bstack1lll1l1ll1_opy_()
  except Exception as e:
    pass
  try:
    global bstack1l1l1l1ll1_opy_
    from QWeb.keywords import browser
    bstack1l1l1l1ll1_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack11lll1lll_opy_(CONFIG) and bstack1ll11ll1l_opy_():
    if bstack11l1l1lll1_opy_() < version.parse(bstack1l111ll1l1_opy_):
      logger.error(bstack1ll11l11ll_opy_.format(bstack11l1l1lll1_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1lllll1_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ༸")) and callable(getattr(RemoteConnection, bstack1lllll1_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ༹࠭"))):
          RemoteConnection._get_proxy_url = bstack11ll111l11_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack11ll111l11_opy_
      except Exception as e:
        logger.error(bstack111l11l1l1_opy_.format(str(e)))
  if not CONFIG.get(bstack1lllll1_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨ༺"), False) and not bstack1l1l111ll_opy_:
    logger.info(bstack11l11ll1l1_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack1lllll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ༻") in CONFIG and str(CONFIG[bstack1lllll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ༼")]).lower() != bstack1lllll1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ༽"):
      bstack11l1l1l1l1_opy_()
    elif bstack11ll111l1l_opy_ != bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༾") or (bstack11ll111l1l_opy_ == bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༿") and not bstack1l1l111ll_opy_):
      bstack1llll1l1ll_opy_()
  if (bstack11ll111l1l_opy_ in [bstack1lllll1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫཀ"), bstack1lllll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬཁ"), bstack1lllll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨག")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack11l1111l11_opy_
        bstack11ll111111_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack111l1l11ll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1l11ll1l1_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1111111l1_opy_ + str(e))
    except Exception as e:
      bstack11111l1l1l_opy_(e, bstack111l1l11ll_opy_)
    if bstack11ll111l1l_opy_ != bstack1lllll1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩགྷ"):
      bstack11ll1l1l1l_opy_()
    bstack1l111111l1_opy_ = Output.start_test
    bstack11llll1l11_opy_ = Output.end_test
    bstack1lllll11ll_opy_ = TestStatus.__init__
    bstack1lll1ll1l1_opy_ = pabot._run
    bstack11l1l1l11l_opy_ = QueueItem.__init__
    bstack1ll11l1ll1_opy_ = pabot._create_command_for_execution
    bstack11lll1l11l_opy_ = pabot._report_results
  if bstack11ll111l1l_opy_ == bstack1lllll1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩང"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11111l1l1l_opy_(e, bstack111l1ll11_opy_)
    bstack1l11ll11l1_opy_ = Runner.run_hook
    bstack11l11ll11l_opy_ = Step.run
  if bstack11ll111l1l_opy_ == bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪཅ"):
    try:
      from _pytest.config import Config
      bstack1ll11l111l_opy_ = Config.getoption
      from _pytest import runner
      bstack11l11111l_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1llll111l_opy_)
    try:
      from pytest_bdd import reporting
      bstack1lll1l1l1l_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬཆ"))
  try:
    framework_name = bstack1lllll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫཇ") if bstack11ll111l1l_opy_ in [bstack1lllll1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ཈"), bstack1lllll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ཉ"), bstack1lllll1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩཊ")] else bstack111l11ll1_opy_(bstack11ll111l1l_opy_)
    bstack1llll111l1_opy_ = {
      bstack1lllll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࠪཋ"): bstack1lllll1_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬཌ") if bstack11ll111l1l_opy_ == bstack1lllll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫཌྷ") and bstack1ll11llll1_opy_() else framework_name,
      bstack1lllll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩཎ"): bstack11ll11llll_opy_(framework_name),
      bstack1lllll1_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫཏ"): __version__,
      bstack1lllll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨཐ"): bstack11ll111l1l_opy_
    }
    if bstack11ll111l1l_opy_ in bstack1l1ll1111l_opy_ + bstack1lllll1ll1_opy_:
      if bstack1lll1lll1_opy_.bstack1l1lllll1_opy_(CONFIG):
        if bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨད") in CONFIG:
          os.environ[bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪདྷ")] = os.getenv(bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫན"), json.dumps(CONFIG[bstack1lllll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫཔ")]))
          CONFIG[bstack1lllll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬཕ")].pop(bstack1lllll1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫབ"), None)
          CONFIG[bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧབྷ")].pop(bstack1lllll1_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭མ"), None)
        bstack1llll111l1_opy_[bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩཙ")] = {
          bstack1lllll1_opy_ (u"ࠪࡲࡦࡳࡥࠨཚ"): bstack1lllll1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ཛ"),
          bstack1lllll1_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ཛྷ"): str(bstack11l1l1lll1_opy_())
        }
    if bstack11ll111l1l_opy_ not in [bstack1lllll1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧཝ")] and not cli.is_running():
      bstack1111lllll_opy_, bstack1l11ll1l1l_opy_ = bstack1ll111ll_opy_.launch(CONFIG, bstack1llll111l1_opy_)
      if bstack1l11ll1l1l_opy_.get(bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧཞ")) is not None and bstack1lll1lll1_opy_.bstack111ll111l1_opy_(CONFIG) is None:
        value = bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨཟ")].get(bstack1lllll1_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪའ"))
        if value is not None:
            CONFIG[bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪཡ")] = value
        else:
          logger.debug(bstack1lllll1_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡥࡣࡷࡥࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤར"))
  except Exception as e:
    logger.debug(bstack1l11lllll1_opy_.format(bstack1lllll1_opy_ (u"࡚ࠬࡥࡴࡶࡋࡹࡧ࠭ལ"), str(e)))
  if bstack11ll111l1l_opy_ == bstack1lllll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ཤ"):
    bstack1ll1l111l1_opy_ = True
    if bstack1l1l111ll_opy_ and bstack1l1111lll1_opy_:
      bstack11ll111ll1_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫཥ"), {}).get(bstack1lllll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪས"))
      bstack1111ll11l1_opy_(bstack1ll111l1ll_opy_)
    elif bstack1l1l111ll_opy_:
      bstack11ll111ll1_opy_ = CONFIG.get(bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ཧ"), {}).get(bstack1lllll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬཨ"))
      global bstack1ll1ll11ll_opy_
      try:
        if bstack11111llll1_opy_(bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཀྵ")]) and multiprocessing.current_process().name == bstack1lllll1_opy_ (u"ࠬ࠶ࠧཪ"):
          bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩཫ")].remove(bstack1lllll1_opy_ (u"ࠧ࠮࡯ࠪཬ"))
          bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ཭")].remove(bstack1lllll1_opy_ (u"ࠩࡳࡨࡧ࠭཮"))
          bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭཯")] = bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ཰")][0]
          with open(bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཱ")], bstack1lllll1_opy_ (u"࠭ࡲࠨི")) as f:
            file_content = f.read()
          bstack1ll11l111_opy_ = bstack1lllll1_opy_ (u"ࠢࠣࠤࡩࡶࡴࡳࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡥ࡭ࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡁࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࠫࡿࢂ࠯࠻ࠡࡨࡵࡳࡲࠦࡰࡥࡤࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡔࡩࡨ࠻ࠡࡱࡪࡣࡩࡨࠠ࠾ࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡥࡧࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯࠭ࡹࡥ࡭ࡨ࠯ࠤࡦࡸࡧ࠭ࠢࡷࡩࡲࡶ࡯ࡳࡣࡵࡽࠥࡃࠠ࠱ࠫ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡶࡾࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡢࡴࡪࠤࡂࠦࡳࡵࡴࠫ࡭ࡳࡺࠨࡢࡴࡪ࠭࠰࠷࠰ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦࡺࡦࡩࡵࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡥࡸࠦࡥ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡸࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡵࡧࡠࡦࡥࠬࡸ࡫࡬ࡧ࠮ࡤࡶ࡬࠲ࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡥࡤ࠱ࡨࡴࡥࡢࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫ࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠮ࠩ࠯ࡵࡨࡸࡤࡺࡲࡢࡥࡨࠬ࠮ࡢ࡮ࠣࠤཱིࠥ").format(str(bstack1l1l111ll_opy_))
          bstack11ll1ll1ll_opy_ = bstack1ll11l111_opy_ + file_content
          bstack1l1l1ll11l_opy_ = bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨུࠫ")] + bstack1lllll1_opy_ (u"ࠩࡢࡦࡸࡺࡡࡤ࡭ࡢࡸࡪࡳࡰ࠯ࡲࡼཱུࠫ")
          with open(bstack1l1l1ll11l_opy_, bstack1lllll1_opy_ (u"ࠪࡻࠬྲྀ")):
            pass
          with open(bstack1l1l1ll11l_opy_, bstack1lllll1_opy_ (u"ࠦࡼ࠱ࠢཷ")) as f:
            f.write(bstack11ll1ll1ll_opy_)
          import subprocess
          process_data = subprocess.run([bstack1lllll1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧླྀ"), bstack1l1l1ll11l_opy_])
          if os.path.exists(bstack1l1l1ll11l_opy_):
            os.unlink(bstack1l1l1ll11l_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack11111llll1_opy_(bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩཹ")]):
            bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧེࠪ")].remove(bstack1lllll1_opy_ (u"ࠨ࠯ࡰཻࠫ"))
            bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩོࠬ")].remove(bstack1lllll1_opy_ (u"ࠪࡴࡩࡨཽࠧ"))
            bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཾ")] = bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཿ")][0]
          bstack1111ll11l1_opy_(bstack1ll111l1ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦྀࠩ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1lllll1_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠཱྀࠩ")] = bstack1lllll1_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪྂ")
          mod_globals[bstack1lllll1_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫྃ")] = os.path.abspath(bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ྄࠭")])
          exec(open(bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ྅")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1lllll1_opy_ (u"ࠬࡉࡡࡶࡩ࡫ࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠬ྆").format(str(e)))
          for driver in bstack1ll1ll11ll_opy_:
            bstack111ll11lll_opy_.append({
              bstack1lllll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ྇"): bstack1l1l111ll_opy_[bstack1lllll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྈ")],
              bstack1lllll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧྉ"): str(e),
              bstack1lllll1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨྊ"): multiprocessing.current_process().name
            })
            bstack1l1l1llll_opy_(driver, bstack1lllll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪྋ"), bstack1lllll1_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢྌ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1ll1ll11ll_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11ll1lll11_opy_, CONFIG, logger)
      bstack111ll1l11l_opy_()
      bstack1l1l11lll1_opy_()
      percy.bstack1ll1l11ll1_opy_()
      bstack111l1111_opy_ = {
        bstack1lllll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྍ"): args[0],
        bstack1lllll1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭ྎ"): CONFIG,
        bstack1lllll1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨྏ"): bstack1ll1lll1ll_opy_,
        bstack1lllll1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪྐ"): bstack11ll1lll11_opy_
      }
      if bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྑ") in CONFIG:
        bstack1ll111l11l_opy_ = bstack11l1ll1ll_opy_(args, logger, CONFIG, bstack1l11ll111_opy_, bstack11ll1l111l_opy_)
        bstack111l1l11l_opy_ = bstack1ll111l11l_opy_.bstack11l11l1l_opy_(run_on_browserstack, bstack111l1111_opy_, bstack11111llll1_opy_(args))
      else:
        if bstack11111llll1_opy_(args):
          bstack111l1111_opy_[bstack1lllll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྒ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack111l1111_opy_,))
          test.start()
          test.join()
        else:
          bstack1111ll11l1_opy_(bstack1ll111l1ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1lllll1_opy_ (u"ࠫࡤࡥ࡮ࡢ࡯ࡨࡣࡤ࠭ྒྷ")] = bstack1lllll1_opy_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧྔ")
          mod_globals[bstack1lllll1_opy_ (u"࠭࡟ࡠࡨ࡬ࡰࡪࡥ࡟ࠨྕ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack11ll111l1l_opy_ == bstack1lllll1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ྖ") or bstack11ll111l1l_opy_ == bstack1lllll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧྗ"):
    percy.init(bstack11ll1lll11_opy_, CONFIG, logger)
    percy.bstack1ll1l11ll1_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack11111l1l1l_opy_(e, bstack111l1l11ll_opy_)
    bstack111ll1l11l_opy_()
    bstack1111ll11l1_opy_(bstack11l1lll11l_opy_)
    if bstack1l11ll111_opy_:
      bstack1l1ll1l11_opy_(bstack11l1lll11l_opy_, args)
      if bstack1lllll1_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ྘") in args:
        i = args.index(bstack1lllll1_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨྙ"))
        args.pop(i)
        args.pop(i)
      if bstack1lllll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྚ") not in CONFIG:
        CONFIG[bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨྛ")] = [{}]
        bstack11ll1l111l_opy_ = 1
      if bstack1l1lll1l1_opy_ == 0:
        bstack1l1lll1l1_opy_ = 1
      args.insert(0, str(bstack1l1lll1l1_opy_))
      args.insert(0, str(bstack1lllll1_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫྜ")))
    if bstack1ll111ll_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack111ll1l111_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1ll1ll1l1_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1lllll1_opy_ (u"ࠢࡓࡑࡅࡓ࡙ࡥࡏࡑࡖࡌࡓࡓ࡙ࠢྜྷ"),
        ).parse_args(bstack111ll1l111_opy_)
        bstack11l1llll1l_opy_ = args.index(bstack111ll1l111_opy_[0]) if len(bstack111ll1l111_opy_) > 0 else len(args)
        args.insert(bstack11l1llll1l_opy_, str(bstack1lllll1_opy_ (u"ࠨ࠯࠰ࡰ࡮ࡹࡴࡦࡰࡨࡶࠬྞ")))
        args.insert(bstack11l1llll1l_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1lllll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡵࡳࡧࡵࡴࡠ࡮࡬ࡷࡹ࡫࡮ࡦࡴ࠱ࡴࡾ࠭ྟ"))))
        if bstack11l111ll_opy_.bstack1111111l_opy_(CONFIG):
          args.insert(bstack11l1llll1l_opy_, str(bstack1lllll1_opy_ (u"ࠪ࠱࠲ࡲࡩࡴࡶࡨࡲࡪࡸࠧྠ")))
          args.insert(bstack11l1llll1l_opy_ + 1, str(bstack1lllll1_opy_ (u"ࠫࡗ࡫ࡴࡳࡻࡉࡥ࡮ࡲࡥࡥ࠼ࡾࢁࠬྡ").format(bstack11l111ll_opy_.bstack111ll1ll_opy_(CONFIG))))
        if bstack11l11l111l_opy_(os.environ.get(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࠪྡྷ"))) and str(os.environ.get(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠪྣ"), bstack1lllll1_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬྤ"))) != bstack1lllll1_opy_ (u"ࠨࡰࡸࡰࡱ࠭ྥ"):
          for bstack1l111l1ll1_opy_ in bstack1ll1ll1l1_opy_:
            args.remove(bstack1l111l1ll1_opy_)
          test_files = os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘ࠭ྦ")).split(bstack1lllll1_opy_ (u"ࠪ࠰ࠬྦྷ"))
          for bstack1111l11l_opy_ in test_files:
            args.append(bstack1111l11l_opy_)
      except Exception as e:
        logger.error(bstack1lllll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡤࡸࡹࡧࡣࡩ࡫ࡱ࡫ࠥࡲࡩࡴࡶࡨࡲࡪࡸࠠࡧࡱࡵࠤࢀࢃ࠮ࠡࡇࡵࡶࡴࡸࠠ࠮ࠢࡾࢁࠧྨ").format(bstack1l11l1lll1_opy_, e))
    pabot.main(args)
  elif bstack11ll111l1l_opy_ == bstack1lllll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ྩ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack11111l1l1l_opy_(e, bstack111l1l11ll_opy_)
    for a in args:
      if bstack1lllll1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜ࠬྪ") in a:
        bstack111lll111l_opy_ = int(a.split(bstack1lllll1_opy_ (u"ࠧ࠻ࠩྫ"))[1])
      if bstack1lllll1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬྫྷ") in a:
        bstack11ll111ll1_opy_ = str(a.split(bstack1lllll1_opy_ (u"ࠩ࠽ࠫྭ"))[1])
      if bstack1lllll1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕࠪྮ") in a:
        bstack11l1llllll_opy_ = str(a.split(bstack1lllll1_opy_ (u"ࠫ࠿࠭ྯ"))[1])
    bstack1111l11lll_opy_ = None
    if bstack1lllll1_opy_ (u"ࠬ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠫྰ") in args:
      i = args.index(bstack1lllll1_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬྱ"))
      args.pop(i)
      bstack1111l11lll_opy_ = args.pop(i)
    if bstack1111l11lll_opy_ is not None:
      global bstack111llll111_opy_
      bstack111llll111_opy_ = bstack1111l11lll_opy_
    bstack1111ll11l1_opy_(bstack11l1lll11l_opy_)
    run_cli(args)
    if bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫྲ") in multiprocessing.current_process().__dict__.keys():
      for bstack11l111l11_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack111ll11lll_opy_.append(bstack11l111l11_opy_)
  elif bstack11ll111l1l_opy_ == bstack1lllll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨླ"):
    bstack1l1l1l11ll_opy_ = bstack1llll1lll_opy_(args, logger, CONFIG, bstack1l11ll111_opy_)
    bstack1l1l1l11ll_opy_.bstack1llll11l1_opy_()
    bstack111ll1l11l_opy_()
    bstack1l1l1ll111_opy_ = True
    bstack1111l1ll1_opy_ = bstack1l1l1l11ll_opy_.bstack1lll1llll_opy_()
    bstack1l1l1l11ll_opy_.bstack111l1111_opy_(bstack11l111l1ll_opy_)
    bstack1l1l1l11ll_opy_.bstack111l1l11_opy_()
    bstack1lll1lll1l_opy_(bstack11ll111l1l_opy_, CONFIG, bstack1l1l1l11ll_opy_.bstack111ll1l1_opy_())
    bstack1l1ll1l1l1_opy_ = bstack1l1l1l11ll_opy_.bstack11l11l1l_opy_(bstack1111ll11l_opy_, {
      bstack1lllll1_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪྴ"): bstack1ll1lll1ll_opy_,
      bstack1lllll1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬྵ"): bstack11ll1lll11_opy_,
      bstack1lllll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧྶ"): bstack1l11ll111_opy_
    })
    try:
      bstack11lll1ll1_opy_, bstack111lll1ll1_opy_ = map(list, zip(*bstack1l1ll1l1l1_opy_))
      bstack111llll1l1_opy_ = bstack11lll1ll1_opy_[0]
      for status_code in bstack111lll1ll1_opy_:
        if status_code != 0:
          bstack11lllll111_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1lllll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡤࡺࡪࠦࡥࡳࡴࡲࡶࡸࠦࡡ࡯ࡦࠣࡷࡹࡧࡴࡶࡵࠣࡧࡴࡪࡥ࠯ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡀࠠࡼࡿࠥྷ").format(str(e)))
  elif bstack11ll111l1l_opy_ == bstack1lllll1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ྸ"):
    try:
      from behave.__main__ import main as bstack1l1ll1l1l_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack11111l1l1l_opy_(e, bstack111l1ll11_opy_)
    bstack111ll1l11l_opy_()
    bstack1l1l1ll111_opy_ = True
    bstack111l1l1l_opy_ = 1
    if bstack1lllll1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧྐྵ") in CONFIG:
      bstack111l1l1l_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨྺ")]
    if bstack1lllll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྻ") in CONFIG:
      bstack11l111lll_opy_ = int(bstack111l1l1l_opy_) * int(len(CONFIG[bstack1lllll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྼ")]))
    else:
      bstack11l111lll_opy_ = int(bstack111l1l1l_opy_)
    config = Configuration(args)
    bstack11111ll1ll_opy_ = config.paths
    if len(bstack11111ll1ll_opy_) == 0:
      import glob
      pattern = bstack1lllll1_opy_ (u"ࠫ࠯࠰࠯ࠫ࠰ࡩࡩࡦࡺࡵࡳࡧࠪ྽")
      bstack1l111lllll_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1l111lllll_opy_)
      config = Configuration(args)
      bstack11111ll1ll_opy_ = config.paths
    bstack111111ll_opy_ = [os.path.normpath(item) for item in bstack11111ll1ll_opy_]
    bstack11ll1l11l1_opy_ = [os.path.normpath(item) for item in args]
    bstack1l1l111ll1_opy_ = [item for item in bstack11ll1l11l1_opy_ if item not in bstack111111ll_opy_]
    import platform as pf
    if pf.system().lower() == bstack1lllll1_opy_ (u"ࠬࡽࡩ࡯ࡦࡲࡻࡸ࠭྾"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack111111ll_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1l1l11l11l_opy_)))
                    for bstack1l1l11l11l_opy_ in bstack111111ll_opy_]
    bstack11l111l1_opy_ = []
    for spec in bstack111111ll_opy_:
      bstack1llllllll_opy_ = []
      bstack1llllllll_opy_ += bstack1l1l111ll1_opy_
      bstack1llllllll_opy_.append(spec)
      bstack11l111l1_opy_.append(bstack1llllllll_opy_)
    execution_items = []
    for bstack1llllllll_opy_ in bstack11l111l1_opy_:
      if bstack1lllll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ྿") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿀")]):
          item = {}
          item[bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࠬ࿁")] = bstack1lllll1_opy_ (u"ࠩࠣࠫ࿂").join(bstack1llllllll_opy_)
          item[bstack1lllll1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ࿃")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack1lllll1_opy_ (u"ࠫࡦࡸࡧࠨ࿄")] = bstack1lllll1_opy_ (u"ࠬࠦࠧ࿅").join(bstack1llllllll_opy_)
        item[bstack1lllll1_opy_ (u"࠭ࡩ࡯ࡦࡨࡼ࿆ࠬ")] = 0
        execution_items.append(item)
    bstack1lll11l1l1_opy_ = bstack11111ll1l1_opy_(execution_items, bstack11l111lll_opy_)
    for execution_item in bstack1lll11l1l1_opy_:
      bstack111l1lll_opy_ = []
      for item in execution_item:
        bstack111l1lll_opy_.append(bstack11ll1l1l1_opy_(name=str(item[bstack1lllll1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭࿇")]),
                                             target=bstack1ll1l111l_opy_,
                                             args=(item[bstack1lllll1_opy_ (u"ࠨࡣࡵ࡫ࠬ࿈")],)))
      for t in bstack111l1lll_opy_:
        t.start()
      for t in bstack111l1lll_opy_:
        t.join()
  else:
    bstack1l1llllll_opy_(bstack11llll1l1l_opy_)
  if not bstack1l1l111ll_opy_:
    bstack11ll1111l1_opy_()
    if(bstack11ll111l1l_opy_ in [bstack1lllll1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ࿉"), bstack1lllll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ࿊")]):
      bstack11l111ll11_opy_()
  bstack1ll11111l1_opy_.bstack1ll11l1lll_opy_()
def browserstack_initialize(bstack11l11llll1_opy_=None):
  logger.info(bstack1lllll1_opy_ (u"ࠫࡗࡻ࡮࡯࡫ࡱ࡫࡙ࠥࡄࡌࠢࡺ࡭ࡹ࡮ࠠࡢࡴࡪࡷ࠿ࠦࠧ࿋") + str(bstack11l11llll1_opy_))
  run_on_browserstack(bstack11l11llll1_opy_, None, True)
@measure(event_name=EVENTS.bstack1lllll1111_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack11ll1111l1_opy_():
  global CONFIG
  global bstack11llllllll_opy_
  global bstack11lllll111_opy_
  global bstack1l1l1l1111_opy_
  global bstack11l1111l_opy_
  bstack1l1lll1lll_opy_.bstack111ll11ll1_opy_()
  if cli.is_running():
    bstack1l1ll11ll_opy_.invoke(Events.bstack1ll11lllll_opy_)
  else:
    bstack1111l1l1_opy_ = bstack11l111ll_opy_.bstack11111l1l_opy_(config=CONFIG)
    bstack1111l1l1_opy_.bstack1111lll11_opy_(CONFIG)
  if bstack11llllllll_opy_ == bstack1lllll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ࿌"):
    if not cli.is_enabled(CONFIG):
      bstack1ll111ll_opy_.stop()
  else:
    bstack1ll111ll_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1llll111_opy_.bstack111l1l1l1_opy_()
  if bstack1lllll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ࿍") in CONFIG and str(CONFIG[bstack1lllll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ࿎")]).lower() != bstack1lllll1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ࿏"):
    hashed_id, bstack1111l11111_opy_ = bstack11llll11l1_opy_()
  else:
    hashed_id, bstack1111l11111_opy_ = get_build_link()
  bstack111l11l1ll_opy_(hashed_id)
  logger.info(bstack1lllll1_opy_ (u"ࠩࡖࡈࡐࠦࡲࡶࡰࠣࡩࡳࡪࡥࡥࠢࡩࡳࡷࠦࡩࡥ࠼ࠪ࿐") + bstack11l1111l_opy_.get_property(bstack1lllll1_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ࿑"), bstack1lllll1_opy_ (u"ࠫࠬ࿒")) + bstack1lllll1_opy_ (u"ࠬ࠲ࠠࡵࡧࡶࡸ࡭ࡻࡢࠡ࡫ࡧ࠾ࠥ࠭࿓") + os.getenv(bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ࿔"), bstack1lllll1_opy_ (u"ࠧࠨ࿕")))
  if hashed_id is not None and bstack1ll1ll11l_opy_() != -1:
    sessions = bstack111l1l1ll_opy_(hashed_id)
    bstack1lll111ll_opy_(sessions, bstack1111l11111_opy_)
  if bstack11llllllll_opy_ == bstack1lllll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ࿖") and bstack11lllll111_opy_ != 0:
    sys.exit(bstack11lllll111_opy_)
  if bstack11llllllll_opy_ == bstack1lllll1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ࿗") and bstack1l1l1l1111_opy_ != 0:
    sys.exit(bstack1l1l1l1111_opy_)
def bstack111l11l1ll_opy_(new_id):
    global bstack11lll1111_opy_
    bstack11lll1111_opy_ = new_id
def bstack111l11ll1_opy_(bstack1l111l11l1_opy_):
  if bstack1l111l11l1_opy_:
    return bstack1l111l11l1_opy_.capitalize()
  else:
    return bstack1lllll1_opy_ (u"ࠪࠫ࿘")
@measure(event_name=EVENTS.bstack11111lll1l_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack1l1llll1l_opy_(bstack11l11lll1_opy_):
  if bstack1lllll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ࿙") in bstack11l11lll1_opy_ and bstack11l11lll1_opy_[bstack1lllll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ࿚")] != bstack1lllll1_opy_ (u"࠭ࠧ࿛"):
    return bstack11l11lll1_opy_[bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ࿜")]
  else:
    bstack1lllll1l11_opy_ = bstack1lllll1_opy_ (u"ࠣࠤ࿝")
    if bstack1lllll1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ࿞") in bstack11l11lll1_opy_ and bstack11l11lll1_opy_[bstack1lllll1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ࿟")] != None:
      bstack1lllll1l11_opy_ += bstack11l11lll1_opy_[bstack1lllll1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ࿠")] + bstack1lllll1_opy_ (u"ࠧ࠲ࠠࠣ࿡")
      if bstack11l11lll1_opy_[bstack1lllll1_opy_ (u"࠭࡯ࡴࠩ࿢")] == bstack1lllll1_opy_ (u"ࠢࡪࡱࡶࠦ࿣"):
        bstack1lllll1l11_opy_ += bstack1lllll1_opy_ (u"ࠣ࡫ࡒࡗࠥࠨ࿤")
      bstack1lllll1l11_opy_ += (bstack11l11lll1_opy_[bstack1lllll1_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭࿥")] or bstack1lllll1_opy_ (u"ࠪࠫ࿦"))
      return bstack1lllll1l11_opy_
    else:
      bstack1lllll1l11_opy_ += bstack111l11ll1_opy_(bstack11l11lll1_opy_[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬ࿧")]) + bstack1lllll1_opy_ (u"ࠧࠦࠢ࿨") + (
              bstack11l11lll1_opy_[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ࿩")] or bstack1lllll1_opy_ (u"ࠧࠨ࿪")) + bstack1lllll1_opy_ (u"ࠣ࠮ࠣࠦ࿫")
      if bstack11l11lll1_opy_[bstack1lllll1_opy_ (u"ࠩࡲࡷࠬ࿬")] == bstack1lllll1_opy_ (u"࡛ࠥ࡮ࡴࡤࡰࡹࡶࠦ࿭"):
        bstack1lllll1l11_opy_ += bstack1lllll1_opy_ (u"ࠦ࡜࡯࡮ࠡࠤ࿮")
      bstack1lllll1l11_opy_ += bstack11l11lll1_opy_[bstack1lllll1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ࿯")] or bstack1lllll1_opy_ (u"࠭ࠧ࿰")
      return bstack1lllll1l11_opy_
@measure(event_name=EVENTS.bstack111l1l1lll_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack11llll11l_opy_(bstack11l1ll111l_opy_):
  if bstack11l1ll111l_opy_ == bstack1lllll1_opy_ (u"ࠢࡥࡱࡱࡩࠧ࿱"):
    return bstack1lllll1_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽࡫ࡷ࡫ࡥ࡯࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥ࡫ࡷ࡫ࡥ࡯ࠤࡁࡇࡴࡳࡰ࡭ࡧࡷࡩࡩࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ࿲")
  elif bstack11l1ll111l_opy_ == bstack1lllll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ࿳"):
    return bstack1lllll1_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡸࡥࡥ࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡶࡪࡪࠢ࠿ࡈࡤ࡭ࡱ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭࿴")
  elif bstack11l1ll111l_opy_ == bstack1lllll1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦ࿵"):
    return bstack1lllll1_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡨࡴࡨࡩࡳࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡨࡴࡨࡩࡳࠨ࠾ࡑࡣࡶࡷࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ࿶")
  elif bstack11l1ll111l_opy_ == bstack1lllll1_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧ࿷"):
    return bstack1lllll1_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡵࡩࡩࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡳࡧࡧࠦࡃࡋࡲࡳࡱࡵࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ࿸")
  elif bstack11l1ll111l_opy_ == bstack1lllll1_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࠤ࿹"):
    return bstack1lllll1_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࠨ࡫ࡥࡢ࠵࠵࠺ࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࠣࡦࡧࡤ࠷࠷࠼ࠢ࠿ࡖ࡬ࡱࡪࡵࡵࡵ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ࿺")
  elif bstack11l1ll111l_opy_ == bstack1lllll1_opy_ (u"ࠥࡶࡺࡴ࡮ࡪࡰࡪࠦ࿻"):
    return bstack1lllll1_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡢ࡭ࡣࡦ࡯ࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡢ࡭ࡣࡦ࡯ࠧࡄࡒࡶࡰࡱ࡭ࡳ࡭࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ࿼")
  else:
    return bstack1lllll1_opy_ (u"ࠬࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡤ࡯ࡥࡨࡱ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡤ࡯ࡥࡨࡱࠢ࠿ࠩ࿽") + bstack111l11ll1_opy_(
      bstack11l1ll111l_opy_) + bstack1lllll1_opy_ (u"࠭࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ࿾")
def bstack111l1l1111_opy_(session):
  return bstack1lllll1_opy_ (u"ࠧ࠽ࡶࡵࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡷࡵࡷࠣࡀ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠲ࡴࡡ࡮ࡧࠥࡂࡁࡧࠠࡩࡴࡨࡪࡂࠨࡻࡾࠤࠣࡸࡦࡸࡧࡦࡶࡀࠦࡤࡨ࡬ࡢࡰ࡮ࠦࡃࢁࡽ࠽࠱ࡤࡂࡁ࠵ࡴࡥࡀࡾࢁࢀࢃ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾࠲ࡸࡷࡄࠧ࿿").format(
    session[bstack1lllll1_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣࡠࡷࡵࡰࠬက")], bstack1l1llll1l_opy_(session), bstack11llll11l_opy_(session[bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡷࡥࡹࡻࡳࠨခ")]),
    bstack11llll11l_opy_(session[bstack1lllll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪဂ")]),
    bstack111l11ll1_opy_(session[bstack1lllll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬဃ")] or session[bstack1lllll1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬင")] or bstack1lllll1_opy_ (u"࠭ࠧစ")) + bstack1lllll1_opy_ (u"ࠢࠡࠤဆ") + (session[bstack1lllll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪဇ")] or bstack1lllll1_opy_ (u"ࠩࠪဈ")),
    session[bstack1lllll1_opy_ (u"ࠪࡳࡸ࠭ဉ")] + bstack1lllll1_opy_ (u"ࠦࠥࠨည") + session[bstack1lllll1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩဋ")], session[bstack1lllll1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨဌ")] or bstack1lllll1_opy_ (u"ࠧࠨဍ"),
    session[bstack1lllll1_opy_ (u"ࠨࡥࡵࡩࡦࡺࡥࡥࡡࡤࡸࠬဎ")] if session[bstack1lllll1_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭ဏ")] else bstack1lllll1_opy_ (u"ࠪࠫတ"))
@measure(event_name=EVENTS.bstack11l1111l1_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def bstack1lll111ll_opy_(sessions, bstack1111l11111_opy_):
  try:
    bstack11l11l11l_opy_ = bstack1lllll1_opy_ (u"ࠦࠧထ")
    if not os.path.exists(bstack1l1lll1l11_opy_):
      os.mkdir(bstack1l1lll1l11_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1lllll1_opy_ (u"ࠬࡧࡳࡴࡧࡷࡷ࠴ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪဒ")), bstack1lllll1_opy_ (u"࠭ࡲࠨဓ")) as f:
      bstack11l11l11l_opy_ = f.read()
    bstack11l11l11l_opy_ = bstack11l11l11l_opy_.replace(bstack1lllll1_opy_ (u"ࠧࡼࠧࡕࡉࡘ࡛ࡌࡕࡕࡢࡇࡔ࡛ࡎࡕࠧࢀࠫန"), str(len(sessions)))
    bstack11l11l11l_opy_ = bstack11l11l11l_opy_.replace(bstack1lllll1_opy_ (u"ࠨࡽࠨࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠫࡽࠨပ"), bstack1111l11111_opy_)
    bstack11l11l11l_opy_ = bstack11l11l11l_opy_.replace(bstack1lllll1_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢࡒࡆࡓࡅࠦࡿࠪဖ"),
                                              sessions[0].get(bstack1lllll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡥࡲ࡫ࠧဗ")) if sessions[0] else bstack1lllll1_opy_ (u"ࠫࠬဘ"))
    with open(os.path.join(bstack1l1lll1l11_opy_, bstack1lllll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡷ࡫ࡰࡰࡴࡷ࠲࡭ࡺ࡭࡭ࠩမ")), bstack1lllll1_opy_ (u"࠭ࡷࠨယ")) as stream:
      stream.write(bstack11l11l11l_opy_.split(bstack1lllll1_opy_ (u"ࠧࡼࠧࡖࡉࡘ࡙ࡉࡐࡐࡖࡣࡉࡇࡔࡂࠧࢀࠫရ"))[0])
      for session in sessions:
        stream.write(bstack111l1l1111_opy_(session))
      stream.write(bstack11l11l11l_opy_.split(bstack1lllll1_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁࠬလ"))[1])
    logger.info(bstack1lllll1_opy_ (u"ࠩࡊࡩࡳ࡫ࡲࡢࡶࡨࡨࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡧࡻࡩ࡭ࡦࠣࡥࡷࡺࡩࡧࡣࡦࡸࡸࠦࡡࡵࠢࡾࢁࠬဝ").format(bstack1l1lll1l11_opy_));
  except Exception as e:
    logger.debug(bstack1ll111l1l1_opy_.format(str(e)))
def bstack111l1l1ll_opy_(hashed_id):
  global CONFIG
  try:
    bstack1l11llll11_opy_ = datetime.datetime.now()
    host = bstack1lllll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪသ") if bstack1lllll1_opy_ (u"ࠫࡦࡶࡰࠨဟ") in CONFIG else bstack1lllll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ဠ")
    user = CONFIG[bstack1lllll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨအ")]
    key = CONFIG[bstack1lllll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪဢ")]
    bstack111l111ll_opy_ = bstack1lllll1_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧဣ") if bstack1lllll1_opy_ (u"ࠩࡤࡴࡵ࠭ဤ") in CONFIG else (bstack1lllll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧဥ") if CONFIG.get(bstack1lllll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨဦ")) else bstack1lllll1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧဧ"))
    host = bstack1l111ll111_opy_(cli.config, [bstack1lllll1_opy_ (u"ࠨࡡࡱ࡫ࡶࠦဨ"), bstack1lllll1_opy_ (u"ࠢࡢࡲࡳࡅࡺࡺ࡯࡮ࡣࡷࡩࠧဩ"), bstack1lllll1_opy_ (u"ࠣࡣࡳ࡭ࠧဪ")], host) if bstack1lllll1_opy_ (u"ࠩࡤࡴࡵ࠭ါ") in CONFIG else bstack1l111ll111_opy_(cli.config, [bstack1lllll1_opy_ (u"ࠥࡥࡵ࡯ࡳࠣာ"), bstack1lllll1_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨိ"), bstack1lllll1_opy_ (u"ࠧࡧࡰࡪࠤီ")], host)
    url = bstack1lllll1_opy_ (u"࠭ࡻࡾ࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡵࡨࡷࡸ࡯࡯࡯ࡵ࠱࡮ࡸࡵ࡮ࠨု").format(host, bstack111l111ll_opy_, hashed_id)
    headers = {
      bstack1lllll1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭ူ"): bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫေ"),
    }
    proxies = bstack111l111l1_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡨࡧࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࡥ࡬ࡪࡵࡷࠦဲ"), datetime.datetime.now() - bstack1l11llll11_opy_)
      return list(map(lambda session: session[bstack1lllll1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨဳ")], response.json()))
  except Exception as e:
    logger.debug(bstack1ll11l1111_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack1lll1l111l_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def get_build_link():
  global CONFIG
  global bstack11lll1111_opy_
  try:
    if bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧဴ") in CONFIG:
      bstack1l11llll11_opy_ = datetime.datetime.now()
      host = bstack1lllll1_opy_ (u"ࠬࡧࡰࡪ࠯ࡦࡰࡴࡻࡤࠨဵ") if bstack1lllll1_opy_ (u"࠭ࡡࡱࡲࠪံ") in CONFIG else bstack1lllll1_opy_ (u"ࠧࡢࡲ࡬့ࠫ")
      user = CONFIG[bstack1lllll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪး")]
      key = CONFIG[bstack1lllll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽ္ࠬ")]
      bstack111l111ll_opy_ = bstack1lllll1_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦ်ࠩ") if bstack1lllll1_opy_ (u"ࠫࡦࡶࡰࠨျ") in CONFIG else bstack1lllll1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧြ")
      url = bstack1lllll1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡼࡿ࠽ࡿࢂࡆࡻࡾ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠯࡬ࡶࡳࡳ࠭ွ").format(user, key, host, bstack111l111ll_opy_)
      if cli.is_enabled(CONFIG):
        bstack1111l11111_opy_, hashed_id = cli.bstack1l111l1l1_opy_()
        logger.info(bstack1l1lll1ll1_opy_.format(bstack1111l11111_opy_))
        return [hashed_id, bstack1111l11111_opy_]
      else:
        headers = {
          bstack1lllll1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭ှ"): bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫဿ"),
        }
        if bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ၀") in CONFIG:
          params = {bstack1lllll1_opy_ (u"ࠪࡲࡦࡳࡥࠨ၁"): CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ၂")], bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ၃"): CONFIG[bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ၄")]}
        else:
          params = {bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ၅"): CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ၆")]}
        proxies = bstack111l111l1_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack1l1l11111_opy_ = response.json()[0][bstack1lllll1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡢࡶ࡫࡯ࡨࠬ၇")]
          if bstack1l1l11111_opy_:
            bstack1111l11111_opy_ = bstack1l1l11111_opy_[bstack1lllll1_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧ၈")].split(bstack1lllll1_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦ࠱ࡧࡻࡩ࡭ࡦࠪ၉"))[0] + bstack1lllll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡷ࠴࠭၊") + bstack1l1l11111_opy_[
              bstack1lllll1_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ။")]
            logger.info(bstack1l1lll1ll1_opy_.format(bstack1111l11111_opy_))
            bstack11lll1111_opy_ = bstack1l1l11111_opy_[bstack1lllll1_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ၌")]
            bstack11llll1ll_opy_ = CONFIG[bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ၍")]
            if bstack1lllll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ၎") in CONFIG:
              bstack11llll1ll_opy_ += bstack1lllll1_opy_ (u"ࠪࠤࠬ၏") + CONFIG[bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ၐ")]
            if bstack11llll1ll_opy_ != bstack1l1l11111_opy_[bstack1lllll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪၑ")]:
              logger.debug(bstack1ll1lll11_opy_.format(bstack1l1l11111_opy_[bstack1lllll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫၒ")], bstack11llll1ll_opy_))
            cli.bstack11l1ll111_opy_(bstack1lllll1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࡭ࡥࡵࡡࡥࡹ࡮ࡲࡤࡠ࡮࡬ࡲࡰࠨၓ"), datetime.datetime.now() - bstack1l11llll11_opy_)
            return [bstack1l1l11111_opy_[bstack1lllll1_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫၔ")], bstack1111l11111_opy_]
    else:
      logger.warn(bstack11ll11ll1l_opy_)
  except Exception as e:
    logger.debug(bstack1l1ll11l1l_opy_.format(str(e)))
  return [None, None]
def bstack11ll1111ll_opy_(url, bstack111lll1l1l_opy_=False):
  global CONFIG
  global bstack11l111l1l1_opy_
  if not bstack11l111l1l1_opy_:
    hostname = bstack1ll1l1l1ll_opy_(url)
    is_private = bstack1l11ll111l_opy_(hostname)
    if (bstack1lllll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ၕ") in CONFIG and not bstack11l11l111l_opy_(CONFIG[bstack1lllll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧၖ")])) and (is_private or bstack111lll1l1l_opy_):
      bstack11l111l1l1_opy_ = hostname
def bstack1ll1l1l1ll_opy_(url):
  return urlparse(url).hostname
def bstack1l11ll111l_opy_(hostname):
  for bstack1ll111ll11_opy_ in bstack1l11111111_opy_:
    regex = re.compile(bstack1ll111ll11_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1111l1l11l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack11111lll11_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack111lll111l_opy_
  bstack111ll11l11_opy_ = not (bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၗ"), None) and bstack1lll1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၘ"), None))
  bstack1l11111ll1_opy_ = getattr(driver, bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ၙ"), None) != True
  bstack1ll11111l_opy_ = bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၚ"), None) and bstack1lll1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၛ"), None)
  if bstack1ll11111l_opy_:
    if not bstack1llll11ll1_opy_():
      logger.warning(bstack1lllll1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷ࠳ࠨၜ"))
      return {}
    logger.debug(bstack1lllll1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧၝ"))
    logger.debug(perform_scan(driver, driver_command=bstack1lllll1_opy_ (u"ࠫࡪࡾࡥࡤࡷࡷࡩࡘࡩࡲࡪࡲࡷࠫၞ")))
    results = bstack11lll111l_opy_(bstack1lllll1_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸࡸࠨၟ"))
    if results is not None and results.get(bstack1lllll1_opy_ (u"ࠨࡩࡴࡵࡸࡩࡸࠨၠ")) is not None:
        return results[bstack1lllll1_opy_ (u"ࠢࡪࡵࡶࡹࡪࡹࠢၡ")]
    logger.error(bstack1lllll1_opy_ (u"ࠣࡐࡲࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡗ࡫ࡳࡶ࡮ࡷࡷࠥࡽࡥࡳࡧࠣࡪࡴࡻ࡮ࡥ࠰ࠥၢ"))
    return []
  if not bstack1lll1lll1_opy_.bstack1l111lll1_opy_(CONFIG, bstack111lll111l_opy_) or (bstack1l11111ll1_opy_ and bstack111ll11l11_opy_):
    logger.warning(bstack1lllll1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶ࠲ࠧၣ"))
    return {}
  try:
    logger.debug(bstack1lllll1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧၤ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1llll11l11_opy_.bstack11l111111l_opy_)
    return results
  except Exception:
    logger.error(bstack1lllll1_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡹࡨࡶࡪࠦࡦࡰࡷࡱࡨ࠳ࠨၥ"))
    return {}
@measure(event_name=EVENTS.bstack1l111l111l_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack111lll111l_opy_
  bstack111ll11l11_opy_ = not (bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၦ"), None) and bstack1lll1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၧ"), None))
  bstack1l11111ll1_opy_ = getattr(driver, bstack1lllll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧၨ"), None) != True
  bstack1ll11111l_opy_ = bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၩ"), None) and bstack1lll1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၪ"), None)
  if bstack1ll11111l_opy_:
    if not bstack1llll11ll1_opy_():
      logger.warning(bstack1lllll1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡳࡶ࡯ࡰࡥࡷࡿ࠮ࠣၫ"))
      return {}
    logger.debug(bstack1lllll1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺࠩၬ"))
    logger.debug(perform_scan(driver, driver_command=bstack1lllll1_opy_ (u"ࠬ࡫ࡸࡦࡥࡸࡸࡪ࡙ࡣࡳ࡫ࡳࡸࠬၭ")))
    results = bstack11lll111l_opy_(bstack1lllll1_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡙ࡵ࡮࡯ࡤࡶࡾࠨၮ"))
    if results is not None and results.get(bstack1lllll1_opy_ (u"ࠢࡴࡷࡰࡱࡦࡸࡹࠣၯ")) is not None:
        return results[bstack1lllll1_opy_ (u"ࠣࡵࡸࡱࡲࡧࡲࡺࠤၰ")]
    logger.error(bstack1lllll1_opy_ (u"ࠤࡑࡳࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡘࡥࡴࡷ࡯ࡸࡸࠦࡓࡶ࡯ࡰࡥࡷࡿࠠࡸࡣࡶࠤ࡫ࡵࡵ࡯ࡦ࠱ࠦၱ"))
    return {}
  if not bstack1lll1lll1_opy_.bstack1l111lll1_opy_(CONFIG, bstack111lll111l_opy_) or (bstack1l11111ll1_opy_ and bstack111ll11l11_opy_):
    logger.warning(bstack1lllll1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠴ࠢၲ"))
    return {}
  try:
    logger.debug(bstack1lllll1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺࠩၳ"))
    logger.debug(perform_scan(driver))
    bstack1l11l11lll_opy_ = driver.execute_async_script(bstack1llll11l11_opy_.bstack1llll11111_opy_)
    return bstack1l11l11lll_opy_
  except Exception:
    logger.error(bstack1lllll1_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡸࡱࡲࡧࡲࡺࠢࡺࡥࡸࠦࡦࡰࡷࡱࡨ࠳ࠨၴ"))
    return {}
def bstack1llll11ll1_opy_():
  global CONFIG
  global bstack111lll111l_opy_
  bstack1l11ll1lll_opy_ = bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ၵ"), None) and bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩၶ"), None)
  if not bstack1lll1lll1_opy_.bstack1l111lll1_opy_(CONFIG, bstack111lll111l_opy_) or not bstack1l11ll1lll_opy_:
        logger.warning(bstack1lllll1_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡲࡦࡵࡸࡰࡹࡹ࠮ࠣၷ"))
        return False
  return True
def bstack11lll111l_opy_(bstack11l1lllll_opy_):
    bstack11ll1l1lll_opy_ = bstack1ll111ll_opy_.current_test_uuid() if bstack1ll111ll_opy_.current_test_uuid() else bstack1llll111_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack11l111l111_opy_(bstack11ll1l1lll_opy_, bstack11l1lllll_opy_))
        try:
            return future.result(timeout=bstack1l1l1ll11_opy_)
        except TimeoutError:
            logger.error(bstack1lllll1_opy_ (u"ࠤࡗ࡭ࡲ࡫࡯ࡶࡶࠣࡥ࡫ࡺࡥࡳࠢࡾࢁࡸࠦࡷࡩ࡫࡯ࡩࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡓࡧࡶࡹࡱࡺࡳࠣၸ").format(bstack1l1l1ll11_opy_))
        except Exception as ex:
            logger.debug(bstack1lllll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡵࡩࡹࡸࡩࡦࡸ࡬ࡲ࡬ࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡼࡿ࠱ࠤࡊࡸࡲࡰࡴࠣ࠱ࠥࢁࡽࠣၹ").format(bstack11l1lllll_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack1l1l1l1ll_opy_, stage=STAGE.bstack11l1l111l1_opy_, bstack1lllll1l11_opy_=bstack11l11ll11_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack111lll111l_opy_
  bstack111ll11l11_opy_ = not (bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၺ"), None) and bstack1lll1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၻ"), None))
  bstack1111l1ll1l_opy_ = not (bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ၼ"), None) and bstack1lll1l11_opy_(
          threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩၽ"), None))
  bstack1l11111ll1_opy_ = getattr(driver, bstack1lllll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨၾ"), None) != True
  if not bstack1lll1lll1_opy_.bstack1l111lll1_opy_(CONFIG, bstack111lll111l_opy_) or (bstack1l11111ll1_opy_ and bstack111ll11l11_opy_ and bstack1111l1ll1l_opy_):
    logger.warning(bstack1lllll1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡸࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡣࡢࡰ࠱ࠦၿ"))
    return {}
  try:
    bstack1l1l1l111_opy_ = bstack1lllll1_opy_ (u"ࠪࡥࡵࡶࠧႀ") in CONFIG and CONFIG.get(bstack1lllll1_opy_ (u"ࠫࡦࡶࡰࠨႁ"), bstack1lllll1_opy_ (u"ࠬ࠭ႂ"))
    session_id = getattr(driver, bstack1lllll1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠪႃ"), None)
    if not session_id:
      logger.warning(bstack1lllll1_opy_ (u"ࠢࡏࡱࠣࡷࡪࡹࡳࡪࡱࡱࠤࡎࡊࠠࡧࡱࡸࡲࡩࠦࡦࡰࡴࠣࡨࡷ࡯ࡶࡦࡴࠥႄ"))
      return {bstack1lllll1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢႅ"): bstack1lllll1_opy_ (u"ࠤࡑࡳࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࠢࡩࡳࡺࡴࡤࠣႆ")}
    if bstack1l1l1l111_opy_:
      try:
        bstack1l1lllll11_opy_ = {
              bstack1lllll1_opy_ (u"ࠪࡸ࡭ࡐࡷࡵࡖࡲ࡯ࡪࡴࠧႇ"): os.environ.get(bstack1lllll1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩႈ"), os.environ.get(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩႉ"), bstack1lllll1_opy_ (u"࠭ࠧႊ"))),
              bstack1lllll1_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧႋ"): bstack1ll111ll_opy_.current_test_uuid() if bstack1ll111ll_opy_.current_test_uuid() else bstack1llll111_opy_.current_hook_uuid(),
              bstack1lllll1_opy_ (u"ࠨࡣࡸࡸ࡭ࡎࡥࡢࡦࡨࡶࠬႌ"): os.environ.get(bstack1lllll1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ႍࠧ")),
              bstack1lllll1_opy_ (u"ࠪࡷࡨࡧ࡮ࡕ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪႎ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack1lllll1_opy_ (u"ࠫࡹ࡮ࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩႏ"): os.environ.get(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ႐"), bstack1lllll1_opy_ (u"࠭ࠧ႑")),
              bstack1lllll1_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪࠧ႒"): kwargs.get(bstack1lllll1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠࡥࡲࡱࡲࡧ࡮ࡥࠩ႓"), None) or bstack1lllll1_opy_ (u"ࠩࠪ႔")
          }
        if not hasattr(thread_local, bstack1lllll1_opy_ (u"ࠪࡦࡦࡹࡥࡠࡣࡳࡴࡤࡧ࠱࠲ࡻࡢࡷࡨࡸࡩࡱࡶࠪ႕")):
            scripts = {bstack1lllll1_opy_ (u"ࠫࡸࡩࡡ࡯ࠩ႖"): bstack1llll11l11_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack11l1l1ll1_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack11l1l1ll1_opy_[bstack1lllll1_opy_ (u"ࠬࡹࡣࡢࡰࠪ႗")] = bstack11l1l1ll1_opy_[bstack1lllll1_opy_ (u"࠭ࡳࡤࡣࡱࠫ႘")] % json.dumps(bstack1l1lllll11_opy_)
        bstack1llll11l11_opy_.bstack1111l1111_opy_(bstack11l1l1ll1_opy_)
        bstack1llll11l11_opy_.store()
        bstack1llllll1l1_opy_ = driver.execute_script(bstack1llll11l11_opy_.perform_scan)
      except Exception as bstack1ll1l11lll_opy_:
        logger.info(bstack1lllll1_opy_ (u"ࠢࡂࡲࡳ࡭ࡺࡳࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࠢ႙") + str(bstack1ll1l11lll_opy_))
        bstack1llllll1l1_opy_ = {bstack1lllll1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢႚ"): str(bstack1ll1l11lll_opy_)}
    else:
      bstack1llllll1l1_opy_ = driver.execute_async_script(bstack1llll11l11_opy_.perform_scan, {bstack1lllll1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࠩႛ"): kwargs.get(bstack1lllll1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢࡧࡴࡳ࡭ࡢࡰࡧࠫႜ"), None) or bstack1lllll1_opy_ (u"ࠫࠬႝ")})
    return bstack1llllll1l1_opy_
  except Exception as err:
    logger.error(bstack1lllll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡴࡸࡲࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡣࡢࡰ࠱ࠤࢀࢃࠢ႞").format(str(err)))
    return {}