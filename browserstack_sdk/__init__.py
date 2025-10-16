# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
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
from browserstack_sdk.bstack1l1111llll_opy_ import bstack111lll1l11_opy_
from browserstack_sdk.bstack1lll1l1l1_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack1l1111l11l_opy_():
  global CONFIG
  headers = {
        bstack1ll1ll1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩਅ"): bstack1ll1ll1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧਆ"),
      }
  proxies = bstack111ll1111l_opy_(CONFIG, bstack1l11l1l111_opy_)
  try:
    response = requests.get(bstack1l11l1l111_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1lll11l1ll_opy_ = response.json()[bstack1ll1ll1_opy_ (u"ࠬ࡮ࡵࡣࡵࠪਇ")]
      logger.debug(bstack1111lll1ll_opy_.format(response.json()))
      return bstack1lll11l1ll_opy_
    else:
      logger.debug(bstack1ll111llll_opy_.format(bstack1ll1ll1_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧਈ")))
  except Exception as e:
    logger.debug(bstack1ll111llll_opy_.format(e))
def bstack11l1ll1l11_opy_(hub_url):
  global CONFIG
  url = bstack1ll1ll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤਉ")+  hub_url + bstack1ll1ll1_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣਊ")
  headers = {
        bstack1ll1ll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨ਋"): bstack1ll1ll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭਌"),
      }
  proxies = bstack111ll1111l_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack111lll11ll_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1ll1l1l1ll_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack111l1111l1_opy_, stage=STAGE.bstack111l1l111_opy_)
def bstack111l11111_opy_():
  try:
    global bstack11111l1l1l_opy_
    bstack1lll11l1ll_opy_ = bstack1l1111l11l_opy_()
    bstack11l111l111_opy_ = []
    results = []
    for bstack1l11111l1_opy_ in bstack1lll11l1ll_opy_:
      bstack11l111l111_opy_.append(bstack11llll11l1_opy_(target=bstack11l1ll1l11_opy_,args=(bstack1l11111l1_opy_,)))
    for t in bstack11l111l111_opy_:
      t.start()
    for t in bstack11l111l111_opy_:
      results.append(t.join())
    bstack11ll11l1l_opy_ = {}
    for item in results:
      hub_url = item[bstack1ll1ll1_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬ਍")]
      latency = item[bstack1ll1ll1_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭਎")]
      bstack11ll11l1l_opy_[hub_url] = latency
    bstack1l111llll_opy_ = min(bstack11ll11l1l_opy_, key= lambda x: bstack11ll11l1l_opy_[x])
    bstack11111l1l1l_opy_ = bstack1l111llll_opy_
    logger.debug(bstack1ll111l1l_opy_.format(bstack1l111llll_opy_))
  except Exception as e:
    logger.debug(bstack11l1l1ll1l_opy_.format(e))
from browserstack_sdk.bstack11l11l11_opy_ import *
from browserstack_sdk.bstack111l1111_opy_ import *
from browserstack_sdk.bstack11l1ll11_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack1l1l1ll111_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack11l1ll1lll_opy_, stage=STAGE.bstack111l1l111_opy_)
def bstack1l111l1l1_opy_():
    global bstack11111l1l1l_opy_
    try:
        bstack11llll11l_opy_ = bstack11lll1l11l_opy_()
        bstack11l11lll1l_opy_(bstack11llll11l_opy_)
        hub_url = bstack11llll11l_opy_.get(bstack1ll1ll1_opy_ (u"ࠨࡵࡳ࡮ࠥਏ"), bstack1ll1ll1_opy_ (u"ࠢࠣਐ"))
        if hub_url.endswith(bstack1ll1ll1_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩ਑")):
            hub_url = hub_url.rsplit(bstack1ll1ll1_opy_ (u"ࠩ࠲ࡻࡩ࠵ࡨࡶࡤࠪ਒"), 1)[0]
        if hub_url.startswith(bstack1ll1ll1_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࠫਓ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack1ll1ll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࠭ਔ")):
            hub_url = hub_url[8:]
        bstack11111l1l1l_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack11lll1l11l_opy_():
    global CONFIG
    bstack111l1l11ll_opy_ = CONFIG.get(bstack1ll1ll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩਕ"), {}).get(bstack1ll1ll1_opy_ (u"࠭ࡧࡳ࡫ࡧࡒࡦࡳࡥࠨਖ"), bstack1ll1ll1_opy_ (u"ࠧࡏࡑࡢࡋࡗࡏࡄࡠࡐࡄࡑࡊࡥࡐࡂࡕࡖࡉࡉ࠭ਗ"))
    if not isinstance(bstack111l1l11ll_opy_, str):
        raise ValueError(bstack1ll1ll1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡈࡴ࡬ࡨࠥࡴࡡ࡮ࡧࠣࡱࡺࡹࡴࠡࡤࡨࠤࡦࠦࡶࡢ࡮࡬ࡨࠥࡹࡴࡳ࡫ࡱ࡫ࠧਘ"))
    try:
        bstack11llll11l_opy_ = bstack1l111l11l_opy_(bstack111l1l11ll_opy_)
        return bstack11llll11l_opy_
    except Exception as e:
        logger.error(bstack1ll1ll1_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣਙ").format(str(e)))
        return {}
def bstack1l111l11l_opy_(bstack111l1l11ll_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬਚ")] or not CONFIG[bstack1ll1ll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧਛ")]:
            raise ValueError(bstack1ll1ll1_opy_ (u"ࠧࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠠࡰࡴࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠢਜ"))
        url = bstack11llll11ll_opy_ + bstack111l1l11ll_opy_
        auth = (CONFIG[bstack1ll1ll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨਝ")], CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪਞ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1ll1l11l1_opy_ = json.loads(response.text)
            return bstack1ll1l11l1_opy_
    except ValueError as ve:
        logger.error(bstack1ll1ll1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣਟ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack1ll1ll1_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࠿ࠦࡻࡾࠤਠ").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack11l11lll1l_opy_(bstack11ll11l11l_opy_):
    global CONFIG
    if bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧਡ") not in CONFIG or str(CONFIG[bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨਢ")]).lower() == bstack1ll1ll1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫਣ"):
        CONFIG[bstack1ll1ll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬਤ")] = False
    elif bstack1ll1ll1_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬਥ") in bstack11ll11l11l_opy_:
        bstack11111l1ll1_opy_ = CONFIG.get(bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬਦ"), {})
        logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢਧ"), bstack11111l1ll1_opy_)
        bstack1l1l1ll1l1_opy_ = bstack11ll11l11l_opy_.get(bstack1ll1ll1_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡕࡩࡵ࡫ࡡࡵࡧࡵࡷࠧਨ"), [])
        bstack11l11l111_opy_ = bstack1ll1ll1_opy_ (u"ࠦ࠱ࠨ਩").join(bstack1l1l1ll1l1_opy_)
        logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡻࡳࡵࡱࡰࠤࡷ࡫ࡰࡦࡣࡷࡩࡷࠦࡳࡵࡴ࡬ࡲ࡬ࡀࠠࠦࡵࠥਪ"), bstack11l11l111_opy_)
        bstack1lll1ll11l_opy_ = {
            bstack1ll1ll1_opy_ (u"ࠨ࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣਫ"): bstack1ll1ll1_opy_ (u"ࠢࡢࡶࡶ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷࠨਬ"),
            bstack1ll1ll1_opy_ (u"ࠣࡨࡲࡶࡨ࡫ࡌࡰࡥࡤࡰࠧਭ"): bstack1ll1ll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢਮ"),
            bstack1ll1ll1_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧਯ"): bstack11l11l111_opy_
        }
        bstack11111l1ll1_opy_.update(bstack1lll1ll11l_opy_)
        logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼࡙ࠣࡵࡪࡡࡵࡧࡧࠤࡱࡵࡣࡢ࡮ࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠫࡳࠣਰ"), bstack11111l1ll1_opy_)
        CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ਱")] = bstack11111l1ll1_opy_
        logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡌࡩ࡯ࡣ࡯ࠤࡈࡕࡎࡇࡋࡊ࠾ࠥࠫࡳࠣਲ"), CONFIG)
def bstack1111l1ll1l_opy_():
    bstack11llll11l_opy_ = bstack11lll1l11l_opy_()
    if not bstack11llll11l_opy_[bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠧਲ਼")]:
      raise ValueError(bstack1ll1ll1_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠡ࡫ࡶࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬ࡲࡰ࡯ࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠥ਴"))
    return bstack11llll11l_opy_[bstack1ll1ll1_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠩਵ")] + bstack1ll1ll1_opy_ (u"ࠪࡃࡨࡧࡰࡴ࠿ࠪਸ਼")
@measure(event_name=EVENTS.bstack1lll111lll_opy_, stage=STAGE.bstack111l1l111_opy_)
def bstack11l11ll11l_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack1ll1ll1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭਷")], CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨਸ")])
        url = bstack1ll1111l1l_opy_
        logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡁࡵࡶࡨࡱࡵࡺࡩ࡯ࡩࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬ࡲࡰ࡯ࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡗࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࠦࡁࡑࡋࠥਹ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack1ll1ll1_opy_ (u"ࠢࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪࠨ਺"): bstack1ll1ll1_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠦ਻")})
            if response.status_code == 200:
                bstack1111l1l11l_opy_ = json.loads(response.text)
                bstack11ll11111l_opy_ = bstack1111l1l11l_opy_.get(bstack1ll1ll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡴ਼ࠩ"), [])
                if bstack11ll11111l_opy_:
                    bstack11lll11ll_opy_ = bstack11ll11111l_opy_[0]
                    build_hashed_id = bstack11lll11ll_opy_.get(bstack1ll1ll1_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭਽"))
                    bstack11llll1ll_opy_ = bstack1llllll11l_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack11llll1ll_opy_])
                    logger.info(bstack111l1l1lll_opy_.format(bstack11llll1ll_opy_))
                    bstack1lll1l1ll1_opy_ = CONFIG[bstack1ll1ll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧਾ")]
                    if bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧਿ") in CONFIG:
                      bstack1lll1l1ll1_opy_ += bstack1ll1ll1_opy_ (u"࠭ࠠࠨੀ") + CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩੁ")]
                    if bstack1lll1l1ll1_opy_ != bstack11lll11ll_opy_.get(bstack1ll1ll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ੂ")):
                      logger.debug(bstack11l1l1lll1_opy_.format(bstack11lll11ll_opy_.get(bstack1ll1ll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ੃")), bstack1lll1l1ll1_opy_))
                    return result
                else:
                    logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡑࡳࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࡷ࡫ࡳࡱࡱࡱࡷࡪ࠴ࠢ੄"))
            else:
                logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨ੅"))
        except Exception as e:
            logger.error(bstack1ll1ll1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࡹࠠ࠻ࠢࡾࢁࠧ੆").format(str(e)))
    else:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡉࡏࡏࡈࡌࡋࠥ࡯ࡳࠡࡰࡲࡸࠥࡹࡥࡵ࠰࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨੇ"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1ll11111l_opy_ import bstack1ll11111l_opy_, Events, bstack11lll1111_opy_, bstack111lll1l1_opy_
from bstack_utils.measure import bstack111l11l1ll_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1l111ll1l_opy_ import bstack1111l1l1l_opy_
from bstack_utils.messages import *
from bstack_utils import bstack1l1l1ll111_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack11l11l1l1l_opy_, bstack111l1l11l1_opy_, bstack11l1l1l11_opy_, bstack1l1lll11_opy_, \
  bstack11l1l111ll_opy_, \
  Notset, bstack11l11llll_opy_, \
  bstack11l111lll_opy_, bstack11lll1ll1l_opy_, bstack1111ll11l1_opy_, bstack1l1l111l11_opy_, bstack1llllll1l1_opy_, bstack11lll11111_opy_, \
  bstack11l11111l_opy_, \
  bstack1111111ll_opy_, bstack11ll1lllll_opy_, bstack1l1l111l1_opy_, bstack1l11ll1l1_opy_, \
  bstack1l1111lll1_opy_, bstack1ll11l11ll_opy_, bstack1ll1l1llll_opy_, bstack1l1lll1ll_opy_
from bstack_utils.bstack1l1l11ll1l_opy_ import bstack111l11l111_opy_
from bstack_utils.bstack1llll1l1l1_opy_ import bstack1ll1llll1l_opy_, bstack1lll11111l_opy_
from bstack_utils.bstack11l1lll111_opy_ import bstack11lll11l11_opy_
from bstack_utils.bstack1l111lll11_opy_ import bstack11lll11ll1_opy_, bstack1l1ll1l111_opy_
from bstack_utils.bstack111llll111_opy_ import bstack111llll111_opy_
from bstack_utils.bstack11l11l1111_opy_ import bstack11l1ll11ll_opy_
from bstack_utils.proxy import bstack1l1111111l_opy_, bstack111ll1111l_opy_, bstack1ll1l1ll1_opy_, bstack11lll11lll_opy_
from bstack_utils.bstack1l1lll11ll_opy_ import bstack11l1l1l1l1_opy_
import bstack_utils.bstack1l11llll1_opy_ as bstack1l1llll11l_opy_
import bstack_utils.bstack11ll1l11ll_opy_ as bstack1l11l1llll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack11l1l1111l_opy_ import bstack1ll1lllll_opy_
from bstack_utils.bstack111l1lll_opy_ import bstack1llll111l_opy_
from bstack_utils.bstack1l11lll1ll_opy_ import bstack1ll11l1ll_opy_
if os.getenv(bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡌࡔࡕࡋࡔࠩੈ")):
  cli.bstack11l111l1l_opy_()
else:
  os.environ[bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡍࡕࡏࡌࡕࠪ੉")] = bstack1ll1ll1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ੊")
bstack11l1111l1l_opy_ = bstack1ll1ll1_opy_ (u"ࠪࠤࠥ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࠣࠤ࡮࡬ࠨࡱࡣࡪࡩࠥࡃ࠽࠾ࠢࡹࡳ࡮ࡪࠠ࠱ࠫࠣࡿࡡࡴࠠࠡࠢࡷࡶࡾࢁ࡜࡯ࠢࡦࡳࡳࡹࡴࠡࡨࡶࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨ࡝ࠩࡩࡷࡡ࠭ࠩ࠼࡞ࡱࠤࠥࠦࠠࠡࡨࡶ࠲ࡦࡶࡰࡦࡰࡧࡊ࡮ࡲࡥࡔࡻࡱࡧ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪ࠯ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡶ࡟ࡪࡰࡧࡩࡽ࠯ࠠࠬࠢࠥ࠾ࠧࠦࠫࠡࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࠨࡢࡹࡤ࡭ࡹࠦ࡮ࡦࡹࡓࡥ࡬࡫࠲࠯ࡧࡹࡥࡱࡻࡡࡵࡧࠫࠦ࠭࠯ࠠ࠾ࡀࠣࡿࢂࠨࠬࠡ࡞ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥ࡫ࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡄࡦࡶࡤ࡭ࡱࡹࠢࡾ࡞ࠪ࠭࠮࠯࡛ࠣࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠦࡢ࠯ࠠࠬࠢࠥ࠰ࡡࡢ࡮ࠣࠫ࡟ࡲࠥࠦࠠࠡࡿࡦࡥࡹࡩࡨࠩࡧࡻ࠭ࢀࡢ࡮ࠡࠢࠣࠤࢂࡢ࡮ࠡࠢࢀࡠࡳࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠪੋ")
bstack1l11l1ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠫࡡࡴ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰࡞ࡱࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶ࡡࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠷࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡲࡢ࡭ࡳࡪࡥࡹࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠷ࡣ࡜࡯ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯ࡵ࡯࡭ࡨ࡫ࠨ࠱࠮ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸࠯࡜࡯ࡥࡲࡲࡸࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯ࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨࠩ࠼࡞ࡱ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡰࡦࡻ࡮ࡤࡪࠣࡁࠥࡧࡳࡺࡰࡦࠤ࠭ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷ࠮ࠦ࠽࠿ࠢࡾࡠࡳࡲࡥࡵࠢࡦࡥࡵࡹ࠻࡝ࡰࡷࡶࡾࠦࡻ࡝ࡰࡦࡥࡵࡹࠠ࠾ࠢࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶ࠭ࡡࡴࠠࠡࡿࠣࡧࡦࡺࡣࡩࠪࡨࡼ࠮ࠦࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡦࡽࡡࡪࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡧࡴࡴ࡮ࡦࡥࡷࠬࢀࡢ࡮ࠡࠢࠣࠤࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴ࠻ࠢࡣࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠩࢁࡥ࡯ࡥࡲࡨࡪ࡛ࡒࡊࡅࡲࡱࡵࡵ࡮ࡦࡰࡷࠬࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡩࡡࡱࡵࠬ࠭ࢂࡦࠬ࡝ࡰࠣࠤࠥࠦ࠮࠯࠰࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴ࡞ࡱࠤࠥࢃࠩ࡝ࡰࢀࡠࡳ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࠪੌ")
from ._version import __version__
bstack111l1ll111_opy_ = None
CONFIG = {}
bstack1l1llll1l1_opy_ = {}
bstack1l11l111l1_opy_ = {}
bstack1l111l111_opy_ = None
bstack11lll1ll11_opy_ = None
bstack1l1ll11l1l_opy_ = None
bstack1ll11l111_opy_ = -1
bstack1l1l1llll1_opy_ = 0
bstack1l1ll1l1l1_opy_ = bstack11ll1lll1l_opy_
bstack111ll1l1l_opy_ = 1
bstack1l1111111_opy_ = False
bstack11l1111ll_opy_ = False
bstack1l1ll1ll1l_opy_ = bstack1ll1ll1_opy_ (u"੍ࠬ࠭")
bstack1ll11ll1ll_opy_ = bstack1ll1ll1_opy_ (u"࠭ࠧ੎")
bstack11ll1l11l1_opy_ = False
bstack111l1ll1ll_opy_ = True
bstack11l1lll11l_opy_ = bstack1ll1ll1_opy_ (u"ࠧࠨ੏")
bstack1l1l1l1ll1_opy_ = []
bstack11lll11l1l_opy_ = threading.Lock()
bstack1l1ll1lll_opy_ = threading.Lock()
bstack11111l1l1l_opy_ = bstack1ll1ll1_opy_ (u"ࠨࠩ੐")
bstack1llll1l11l_opy_ = False
bstack11111ll1l1_opy_ = None
bstack11ll1ll1l_opy_ = None
bstack1llll11ll1_opy_ = None
bstack1l1ll1l11_opy_ = -1
bstack111l1llll_opy_ = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠩࢁࠫੑ")), bstack1ll1ll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ੒"), bstack1ll1ll1_opy_ (u"ࠫ࠳ࡸ࡯ࡣࡱࡷ࠱ࡷ࡫ࡰࡰࡴࡷ࠱࡭࡫࡬ࡱࡧࡵ࠲࡯ࡹ࡯࡯ࠩ੓"))
bstack111ll11l11_opy_ = 0
bstack11l11ll1l_opy_ = 0
bstack11l1l1111_opy_ = []
bstack1ll111lll1_opy_ = []
bstack1llll1111l_opy_ = []
bstack11ll11l11_opy_ = []
bstack1l1l11ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠬ࠭੔")
bstack1l11l1l11_opy_ = bstack1ll1ll1_opy_ (u"࠭ࠧ੕")
bstack1lll1llll1_opy_ = False
bstack111l1lll11_opy_ = False
bstack1l11l1111_opy_ = {}
bstack11ll1ll11l_opy_ = None
bstack1ll1ll1ll1_opy_ = None
bstack111ll111l_opy_ = None
bstack111l111l1l_opy_ = None
bstack1l11lll11_opy_ = None
bstack111l11l1l_opy_ = None
bstack11l111ll1_opy_ = None
bstack11lll111l1_opy_ = None
bstack1ll1l111ll_opy_ = None
bstack11l11ll11_opy_ = None
bstack11l1l1ll1_opy_ = None
bstack1111l11ll1_opy_ = None
bstack1ll1ll11l_opy_ = None
bstack1l11ll1111_opy_ = None
bstack1111ll1l1_opy_ = None
bstack1ll1ll11l1_opy_ = None
bstack1l111111l_opy_ = None
bstack1ll1ll1l11_opy_ = None
bstack1l1l1ll1l_opy_ = None
bstack11ll11llll_opy_ = None
bstack111l11l11l_opy_ = None
bstack1l1ll111l1_opy_ = None
bstack111l1ll11l_opy_ = None
thread_local = threading.local()
bstack111l11ll1_opy_ = False
bstack1ll1lll1l_opy_ = bstack1ll1ll1_opy_ (u"ࠢࠣ੖")
logger = bstack1l1l1ll111_opy_.get_logger(__name__, bstack1l1ll1l1l1_opy_)
bstack11111l11_opy_ = Config.bstack1llllllll_opy_()
percy = bstack1ll11l1111_opy_()
bstack1111l1ll11_opy_ = bstack1111l1l1l_opy_()
bstack1ll1l1l1l_opy_ = bstack11l1ll11_opy_()
def bstack1ll111111_opy_():
  global CONFIG
  global bstack1lll1llll1_opy_
  global bstack11111l11_opy_
  testContextOptions = bstack1l1lllll1_opy_(CONFIG)
  if bstack11l1l111ll_opy_(CONFIG):
    if (bstack1ll1ll1_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ੗") in testContextOptions and str(testContextOptions[bstack1ll1ll1_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ੘")]).lower() == bstack1ll1ll1_opy_ (u"ࠪࡸࡷࡻࡥࠨਖ਼")):
      bstack1lll1llll1_opy_ = True
    bstack11111l11_opy_.bstack1111lll1l_opy_(testContextOptions.get(bstack1ll1ll1_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨਗ਼"), False))
  else:
    bstack1lll1llll1_opy_ = True
    bstack11111l11_opy_.bstack1111lll1l_opy_(True)
def bstack111111111_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11lll11l1_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1111ll111l_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1ll1ll1_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡩ࡯࡯ࡨ࡬࡫࡫࡯࡬ࡦࠤਜ਼") == args[i].lower() or bstack1ll1ll1_opy_ (u"ࠨ࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡱࡪ࡮࡭ࠢੜ") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack11l1lll11l_opy_
      bstack11l1lll11l_opy_ += bstack1ll1ll1_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡄࡱࡱࡪ࡮࡭ࡆࡪ࡮ࡨࠤࠬ੝") + shlex.quote(path)
      return path
  return None
bstack11ll1l1l1_opy_ = re.compile(bstack1ll1ll1_opy_ (u"ࡳࠤ࠱࠮ࡄࡢࠤࡼࠪ࠱࠮ࡄ࠯ࡽ࠯ࠬࡂࠦਫ਼"))
def bstack11l11llll1_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack11ll1l1l1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1ll1ll1_opy_ (u"ࠤࠧࡿࠧ੟") + group + bstack1ll1ll1_opy_ (u"ࠥࢁࠧ੠"), os.environ.get(group))
  return value
def bstack1111l11lll_opy_():
  global bstack111l1ll11l_opy_
  if bstack111l1ll11l_opy_ is None:
        bstack111l1ll11l_opy_ = bstack1111ll111l_opy_()
  bstack11l1lll11_opy_ = bstack111l1ll11l_opy_
  if bstack11l1lll11_opy_ and os.path.exists(os.path.abspath(bstack11l1lll11_opy_)):
    fileName = bstack11l1lll11_opy_
  if bstack1ll1ll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ੡") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1ll1ll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆࠩ੢")])) and not bstack1ll1ll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨ੣") in locals():
    fileName = os.environ[bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ੤")]
  if bstack1ll1ll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡔࡡ࡮ࡧࠪ੥") in locals():
    bstack1l1111l_opy_ = os.path.abspath(fileName)
  else:
    bstack1l1111l_opy_ = bstack1ll1ll1_opy_ (u"ࠩࠪ੦")
  bstack11l1l11ll_opy_ = os.getcwd()
  bstack1111l11l1_opy_ = bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭੧")
  bstack11l1lllll1_opy_ = bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡦࡳ࡬ࠨ੨")
  while (not os.path.exists(bstack1l1111l_opy_)) and bstack11l1l11ll_opy_ != bstack1ll1ll1_opy_ (u"ࠧࠨ੩"):
    bstack1l1111l_opy_ = os.path.join(bstack11l1l11ll_opy_, bstack1111l11l1_opy_)
    if not os.path.exists(bstack1l1111l_opy_):
      bstack1l1111l_opy_ = os.path.join(bstack11l1l11ll_opy_, bstack11l1lllll1_opy_)
    if bstack11l1l11ll_opy_ != os.path.dirname(bstack11l1l11ll_opy_):
      bstack11l1l11ll_opy_ = os.path.dirname(bstack11l1l11ll_opy_)
    else:
      bstack11l1l11ll_opy_ = bstack1ll1ll1_opy_ (u"ࠨࠢ੪")
  bstack111l1ll11l_opy_ = bstack1l1111l_opy_ if os.path.exists(bstack1l1111l_opy_) else None
  return bstack111l1ll11l_opy_
def bstack111l11l11_opy_(config):
    if bstack1ll1ll1_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧ੫") in config:
      config[bstack1ll1ll1_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ੬")] = config[bstack1ll1ll1_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࠩ੭")]
    if bstack1ll1ll1_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࡒࡴࡹ࡯࡯࡯ࡵࠪ੮") in config:
      config[bstack1ll1ll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ੯")] = config[bstack1ll1ll1_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࡔࡶࡴࡪࡱࡱࡷࠬੰ")]
def bstack1lll1111l_opy_():
  bstack1l1111l_opy_ = bstack1111l11lll_opy_()
  if not os.path.exists(bstack1l1111l_opy_):
    bstack1lll11l1l1_opy_(
      bstack1l11l111l_opy_.format(os.getcwd()))
  try:
    with open(bstack1l1111l_opy_, bstack1ll1ll1_opy_ (u"࠭ࡲࠨੱ")) as stream:
      yaml.add_implicit_resolver(bstack1ll1ll1_opy_ (u"ࠢࠢࡲࡤࡸ࡭࡫ࡸࠣੲ"), bstack11ll1l1l1_opy_)
      yaml.add_constructor(bstack1ll1ll1_opy_ (u"ࠣࠣࡳࡥࡹ࡮ࡥࡹࠤੳ"), bstack11l11llll1_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack111l11l11_opy_(config)
      return config
  except:
    with open(bstack1l1111l_opy_, bstack1ll1ll1_opy_ (u"ࠩࡵࠫੴ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack111l11l11_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1lll11l1l1_opy_(bstack1111l1l111_opy_.format(str(exc)))
def bstack1ll1ll1lll_opy_(config):
  bstack1l1ll1111l_opy_ = bstack111llll1l_opy_(config)
  for option in list(bstack1l1ll1111l_opy_):
    if option.lower() in bstack1lllllllll_opy_ and option != bstack1lllllllll_opy_[option.lower()]:
      bstack1l1ll1111l_opy_[bstack1lllllllll_opy_[option.lower()]] = bstack1l1ll1111l_opy_[option]
      del bstack1l1ll1111l_opy_[option]
  return config
def bstack1ll11ll111_opy_():
  global bstack1l11l111l1_opy_
  for key, bstack11ll11l1l1_opy_ in bstack1l1l111l1l_opy_.items():
    if isinstance(bstack11ll11l1l1_opy_, list):
      for var in bstack11ll11l1l1_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1l11l111l1_opy_[key] = os.environ[var]
          break
    elif bstack11ll11l1l1_opy_ in os.environ and os.environ[bstack11ll11l1l1_opy_] and str(os.environ[bstack11ll11l1l1_opy_]).strip():
      bstack1l11l111l1_opy_[key] = os.environ[bstack11ll11l1l1_opy_]
  if bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬੵ") in os.environ:
    bstack1l11l111l1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੶")] = {}
    bstack1l11l111l1_opy_[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ੷")][bstack1ll1ll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ੸")] = os.environ[bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩ੹")]
def bstack1l11lll1l1_opy_():
  global bstack1l1llll1l1_opy_
  global bstack11l1lll11l_opy_
  bstack11ll1ll1l1_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack1ll1ll1_opy_ (u"ࠨ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ੺").lower() == val.lower():
      bstack1l1llll1l1_opy_[bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੻")] = {}
      bstack1l1llll1l1_opy_[bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ੼")][bstack1ll1ll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੽")] = sys.argv[idx + 1]
      bstack11ll1ll1l1_opy_.extend([idx, idx + 1])
      break
  for key, bstack1l1111lll_opy_ in bstack111111lll_opy_.items():
    if isinstance(bstack1l1111lll_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack1l1111lll_opy_:
          if bstack1ll1ll1_opy_ (u"ࠬ࠳࠭ࠨ੾") + var.lower() == val.lower() and key not in bstack1l1llll1l1_opy_:
            bstack1l1llll1l1_opy_[key] = sys.argv[idx + 1]
            bstack11l1lll11l_opy_ += bstack1ll1ll1_opy_ (u"࠭ࠠ࠮࠯ࠪ੿") + var + bstack1ll1ll1_opy_ (u"ࠧࠡࠩ઀") + shlex.quote(sys.argv[idx + 1])
            bstack11ll1ll1l1_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack1ll1ll1_opy_ (u"ࠨ࠯࠰ࠫઁ") + bstack1l1111lll_opy_.lower() == val.lower() and key not in bstack1l1llll1l1_opy_:
          bstack1l1llll1l1_opy_[key] = sys.argv[idx + 1]
          bstack11l1lll11l_opy_ += bstack1ll1ll1_opy_ (u"ࠩࠣ࠱࠲࠭ં") + bstack1l1111lll_opy_ + bstack1ll1ll1_opy_ (u"ࠪࠤࠬઃ") + shlex.quote(sys.argv[idx + 1])
          bstack11ll1ll1l1_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack11ll1ll1l1_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack11lll1lll_opy_(config):
  bstack11l1ll1l1_opy_ = config.keys()
  for bstack1ll11l1lll_opy_, bstack11l1ll11l_opy_ in bstack11ll1ll111_opy_.items():
    if bstack11l1ll11l_opy_ in bstack11l1ll1l1_opy_:
      config[bstack1ll11l1lll_opy_] = config[bstack11l1ll11l_opy_]
      del config[bstack11l1ll11l_opy_]
  for bstack1ll11l1lll_opy_, bstack11l1ll11l_opy_ in bstack11111ll1l_opy_.items():
    if isinstance(bstack11l1ll11l_opy_, list):
      for bstack11l1lllll_opy_ in bstack11l1ll11l_opy_:
        if bstack11l1lllll_opy_ in bstack11l1ll1l1_opy_:
          config[bstack1ll11l1lll_opy_] = config[bstack11l1lllll_opy_]
          del config[bstack11l1lllll_opy_]
          break
    elif bstack11l1ll11l_opy_ in bstack11l1ll1l1_opy_:
      config[bstack1ll11l1lll_opy_] = config[bstack11l1ll11l_opy_]
      del config[bstack11l1ll11l_opy_]
  for bstack11l1lllll_opy_ in list(config):
    for bstack1llll11l11_opy_ in bstack1l1l1ll1ll_opy_:
      if bstack11l1lllll_opy_.lower() == bstack1llll11l11_opy_.lower() and bstack11l1lllll_opy_ != bstack1llll11l11_opy_:
        config[bstack1llll11l11_opy_] = config[bstack11l1lllll_opy_]
        del config[bstack11l1lllll_opy_]
  bstack1111ll11ll_opy_ = [{}]
  if not config.get(bstack1ll1ll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ઄")):
    config[bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨઅ")] = [{}]
  bstack1111ll11ll_opy_ = config[bstack1ll1ll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩઆ")]
  for platform in bstack1111ll11ll_opy_:
    for bstack11l1lllll_opy_ in list(platform):
      for bstack1llll11l11_opy_ in bstack1l1l1ll1ll_opy_:
        if bstack11l1lllll_opy_.lower() == bstack1llll11l11_opy_.lower() and bstack11l1lllll_opy_ != bstack1llll11l11_opy_:
          platform[bstack1llll11l11_opy_] = platform[bstack11l1lllll_opy_]
          del platform[bstack11l1lllll_opy_]
  for bstack1ll11l1lll_opy_, bstack11l1ll11l_opy_ in bstack11111ll1l_opy_.items():
    for platform in bstack1111ll11ll_opy_:
      if isinstance(bstack11l1ll11l_opy_, list):
        for bstack11l1lllll_opy_ in bstack11l1ll11l_opy_:
          if bstack11l1lllll_opy_ in platform:
            platform[bstack1ll11l1lll_opy_] = platform[bstack11l1lllll_opy_]
            del platform[bstack11l1lllll_opy_]
            break
      elif bstack11l1ll11l_opy_ in platform:
        platform[bstack1ll11l1lll_opy_] = platform[bstack11l1ll11l_opy_]
        del platform[bstack11l1ll11l_opy_]
  for bstack1ll1l1l11_opy_ in bstack1l1ll1l1l_opy_:
    if bstack1ll1l1l11_opy_ in config:
      if not bstack1l1ll1l1l_opy_[bstack1ll1l1l11_opy_] in config:
        config[bstack1l1ll1l1l_opy_[bstack1ll1l1l11_opy_]] = {}
      config[bstack1l1ll1l1l_opy_[bstack1ll1l1l11_opy_]].update(config[bstack1ll1l1l11_opy_])
      del config[bstack1ll1l1l11_opy_]
  for platform in bstack1111ll11ll_opy_:
    for bstack1ll1l1l11_opy_ in bstack1l1ll1l1l_opy_:
      if bstack1ll1l1l11_opy_ in list(platform):
        if not bstack1l1ll1l1l_opy_[bstack1ll1l1l11_opy_] in platform:
          platform[bstack1l1ll1l1l_opy_[bstack1ll1l1l11_opy_]] = {}
        platform[bstack1l1ll1l1l_opy_[bstack1ll1l1l11_opy_]].update(platform[bstack1ll1l1l11_opy_])
        del platform[bstack1ll1l1l11_opy_]
  config = bstack1ll1ll1lll_opy_(config)
  return config
def bstack1lll1l111l_opy_(config):
  global bstack1ll11ll1ll_opy_
  bstack1l1l1111l1_opy_ = False
  if bstack1ll1ll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫઇ") in config and str(config[bstack1ll1ll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬઈ")]).lower() != bstack1ll1ll1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨઉ"):
    if bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧઊ") not in config or str(config[bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨઋ")]).lower() == bstack1ll1ll1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫઌ"):
      config[bstack1ll1ll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬઍ")] = False
    else:
      bstack11llll11l_opy_ = bstack11lll1l11l_opy_()
      if bstack1ll1ll1_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬ઎") in bstack11llll11l_opy_:
        if not bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬએ") in config:
          config[bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઐ")] = {}
        config[bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઑ")][bstack1ll1ll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭઒")] = bstack1ll1ll1_opy_ (u"ࠬࡧࡴࡴ࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠫઓ")
        bstack1l1l1111l1_opy_ = True
        bstack1ll11ll1ll_opy_ = config[bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪઔ")].get(bstack1ll1ll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩક"))
  if bstack11l1l111ll_opy_(config) and bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬખ") in config and str(config[bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ગ")]).lower() != bstack1ll1ll1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩઘ") and not bstack1l1l1111l1_opy_:
    if not bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨઙ") in config:
      config[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩચ")] = {}
    if not config[bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪછ")].get(bstack1ll1ll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠫજ")) and not bstack1ll1ll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪઝ") in config[bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઞ")]:
      bstack1l11l1ll_opy_ = datetime.datetime.now()
      bstack11l1111l11_opy_ = bstack1l11l1ll_opy_.strftime(bstack1ll1ll1_opy_ (u"ࠪࠩࡩࡥࠥࡣࡡࠨࡌࠪࡓࠧટ"))
      hostname = socket.gethostname()
      bstack1ll111l11l_opy_ = bstack1ll1ll1_opy_ (u"ࠫࠬઠ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1ll1ll1_opy_ (u"ࠬࢁࡽࡠࡽࢀࡣࢀࢃࠧડ").format(bstack11l1111l11_opy_, hostname, bstack1ll111l11l_opy_)
      config[bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪઢ")][bstack1ll1ll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩણ")] = identifier
    bstack1ll11ll1ll_opy_ = config[bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬત")].get(bstack1ll1ll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫથ"))
  return config
def bstack111l11111l_opy_():
  bstack1l11111111_opy_ =  bstack1l1l111l11_opy_()[bstack1ll1ll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠩદ")]
  return bstack1l11111111_opy_ if bstack1l11111111_opy_ else -1
def bstack111lll1ll1_opy_(bstack1l11111111_opy_):
  global CONFIG
  if not bstack1ll1ll1_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ધ") in CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧન")]:
    return
  CONFIG[bstack1ll1ll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ઩")] = CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩપ")].replace(
    bstack1ll1ll1_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪફ"),
    str(bstack1l11111111_opy_)
  )
def bstack1l1lllllll_opy_():
  global CONFIG
  if not bstack1ll1ll1_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨબ") in CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬભ")]:
    return
  bstack1l11l1ll_opy_ = datetime.datetime.now()
  bstack11l1111l11_opy_ = bstack1l11l1ll_opy_.strftime(bstack1ll1ll1_opy_ (u"ࠫࠪࡪ࠭ࠦࡤ࠰ࠩࡍࡀࠥࡎࠩમ"))
  CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧય")] = CONFIG[bstack1ll1ll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨર")].replace(
    bstack1ll1ll1_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭઱"),
    bstack11l1111l11_opy_
  )
def bstack1l11l1l11l_opy_():
  global CONFIG
  if bstack1ll1ll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪલ") in CONFIG and not bool(CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫળ")]):
    del CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ઴")]
    return
  if not bstack1ll1ll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭વ") in CONFIG:
    CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧશ")] = bstack1ll1ll1_opy_ (u"࠭ࠣࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩષ")
  if bstack1ll1ll1_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭સ") in CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪહ")]:
    bstack1l1lllllll_opy_()
    os.environ[bstack1ll1ll1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭઺")] = CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ઻")]
  if not bstack1ll1ll1_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ઼࠭") in CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઽ")]:
    return
  bstack1l11111111_opy_ = bstack1ll1ll1_opy_ (u"࠭ࠧા")
  bstack11llll1l1l_opy_ = bstack111l11111l_opy_()
  if bstack11llll1l1l_opy_ != -1:
    bstack1l11111111_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡄࡋࠣࠫિ") + str(bstack11llll1l1l_opy_)
  if bstack1l11111111_opy_ == bstack1ll1ll1_opy_ (u"ࠨࠩી"):
    bstack1l1l1l1ll_opy_ = bstack11l1ll1ll1_opy_(CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬુ")])
    if bstack1l1l1l1ll_opy_ != -1:
      bstack1l11111111_opy_ = str(bstack1l1l1l1ll_opy_)
  if bstack1l11111111_opy_:
    bstack111lll1ll1_opy_(bstack1l11111111_opy_)
    os.environ[bstack1ll1ll1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧૂ")] = CONFIG[bstack1ll1ll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ૃ")]
def bstack1l1l1l1l1_opy_(bstack1ll1ll1111_opy_, bstack1lllll11l1_opy_, path):
  json_data = {
    bstack1ll1ll1_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩૄ"): bstack1lllll11l1_opy_
  }
  if os.path.exists(path):
    bstack1ll111l11_opy_ = json.load(open(path, bstack1ll1ll1_opy_ (u"࠭ࡲࡣࠩૅ")))
  else:
    bstack1ll111l11_opy_ = {}
  bstack1ll111l11_opy_[bstack1ll1ll1111_opy_] = json_data
  with open(path, bstack1ll1ll1_opy_ (u"ࠢࡸ࠭ࠥ૆")) as outfile:
    json.dump(bstack1ll111l11_opy_, outfile)
def bstack11l1ll1ll1_opy_(bstack1ll1ll1111_opy_):
  bstack1ll1ll1111_opy_ = str(bstack1ll1ll1111_opy_)
  bstack1l1l1l111_opy_ = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠨࢀࠪે")), bstack1ll1ll1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩૈ"))
  try:
    if not os.path.exists(bstack1l1l1l111_opy_):
      os.makedirs(bstack1l1l1l111_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠪࢂࠬૉ")), bstack1ll1ll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ૊"), bstack1ll1ll1_opy_ (u"ࠬ࠴ࡢࡶ࡫࡯ࡨ࠲ࡴࡡ࡮ࡧ࠰ࡧࡦࡩࡨࡦ࠰࡭ࡷࡴࡴࠧો"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1ll1ll1_opy_ (u"࠭ࡷࠨૌ")):
        pass
      with open(file_path, bstack1ll1ll1_opy_ (u"ࠢࡸ્࠭ࠥ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1ll1ll1_opy_ (u"ࠨࡴࠪ૎")) as bstack1l1111l111_opy_:
      bstack111ll1ll11_opy_ = json.load(bstack1l1111l111_opy_)
    if bstack1ll1ll1111_opy_ in bstack111ll1ll11_opy_:
      bstack1l11ll1l1l_opy_ = bstack111ll1ll11_opy_[bstack1ll1ll1111_opy_][bstack1ll1ll1_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૏")]
      bstack111ll1l11l_opy_ = int(bstack1l11ll1l1l_opy_) + 1
      bstack1l1l1l1l1_opy_(bstack1ll1ll1111_opy_, bstack111ll1l11l_opy_, file_path)
      return bstack111ll1l11l_opy_
    else:
      bstack1l1l1l1l1_opy_(bstack1ll1ll1111_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1l111l1ll_opy_.format(str(e)))
    return -1
def bstack1ll111ll11_opy_(config):
  if not config[bstack1ll1ll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬૐ")] or not config[bstack1ll1ll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ૑")]:
    return True
  else:
    return False
def bstack1llll1lll1_opy_(config, index=0):
  global bstack11ll1l11l1_opy_
  bstack1ll1lllll1_opy_ = {}
  caps = bstack111llll11l_opy_ + bstack1l11ll11l_opy_
  if config.get(bstack1ll1ll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ૒"), False):
    bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪ૓")] = True
    bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ૔")] = config.get(bstack1ll1ll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷࠬ૕"), {})
  if bstack11ll1l11l1_opy_:
    caps += bstack11l11l1l11_opy_
  for key in config:
    if key in caps + [bstack1ll1ll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૖")]:
      continue
    bstack1ll1lllll1_opy_[key] = config[key]
  if bstack1ll1ll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૗") in config:
    for bstack1llll1l1ll_opy_ in config[bstack1ll1ll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૘")][index]:
      if bstack1llll1l1ll_opy_ in caps:
        continue
      bstack1ll1lllll1_opy_[bstack1llll1l1ll_opy_] = config[bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૙")][index][bstack1llll1l1ll_opy_]
  bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"࠭ࡨࡰࡵࡷࡒࡦࡳࡥࠨ૚")] = socket.gethostname()
  if bstack1ll1ll1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ૛") in bstack1ll1lllll1_opy_:
    del (bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ૜")])
  return bstack1ll1lllll1_opy_
def bstack1l1111l1l1_opy_(config):
  global bstack11ll1l11l1_opy_
  bstack111l111111_opy_ = {}
  caps = bstack1l11ll11l_opy_
  if bstack11ll1l11l1_opy_:
    caps += bstack11l11l1l11_opy_
  for key in caps:
    if key in config:
      bstack111l111111_opy_[key] = config[key]
  return bstack111l111111_opy_
def bstack11l11lll11_opy_(bstack1ll1lllll1_opy_, bstack111l111111_opy_):
  bstack11ll11lll1_opy_ = {}
  for key in bstack1ll1lllll1_opy_.keys():
    if key in bstack11ll1ll111_opy_:
      bstack11ll11lll1_opy_[bstack11ll1ll111_opy_[key]] = bstack1ll1lllll1_opy_[key]
    else:
      bstack11ll11lll1_opy_[key] = bstack1ll1lllll1_opy_[key]
  for key in bstack111l111111_opy_:
    if key in bstack11ll1ll111_opy_:
      bstack11ll11lll1_opy_[bstack11ll1ll111_opy_[key]] = bstack111l111111_opy_[key]
    else:
      bstack11ll11lll1_opy_[key] = bstack111l111111_opy_[key]
  return bstack11ll11lll1_opy_
def bstack111111l11_opy_(config, index=0):
  global bstack11ll1l11l1_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11lll111ll_opy_ = bstack11l11l1l1l_opy_(bstack1l1llll11_opy_, config, logger)
  bstack111l111111_opy_ = bstack1l1111l1l1_opy_(config)
  bstack11lll1llll_opy_ = bstack1l11ll11l_opy_
  bstack11lll1llll_opy_ += bstack11ll1llll1_opy_
  bstack111l111111_opy_ = update(bstack111l111111_opy_, bstack11lll111ll_opy_)
  if bstack11ll1l11l1_opy_:
    bstack11lll1llll_opy_ += bstack11l11l1l11_opy_
  if bstack1ll1ll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૝") in config:
    if bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ૞") in config[bstack1ll1ll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૟")][index]:
      caps[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪૠ")] = config[bstack1ll1ll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩૡ")][index][bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬૢ")]
    if bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩૣ") in config[bstack1ll1ll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૤")][index]:
      caps[bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ૥")] = str(config[bstack1ll1ll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૦")][index][bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭૧")])
    bstack1lll1l1lll_opy_ = bstack11l11l1l1l_opy_(bstack1l1llll11_opy_, config[bstack1ll1ll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૨")][index], logger)
    bstack11lll1llll_opy_ += list(bstack1lll1l1lll_opy_.keys())
    for bstack11ll111l1l_opy_ in bstack11lll1llll_opy_:
      if bstack11ll111l1l_opy_ in config[bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૩")][index]:
        if bstack11ll111l1l_opy_ == bstack1ll1ll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ૪"):
          try:
            bstack1lll1l1lll_opy_[bstack11ll111l1l_opy_] = str(config[bstack1ll1ll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૫")][index][bstack11ll111l1l_opy_] * 1.0)
          except:
            bstack1lll1l1lll_opy_[bstack11ll111l1l_opy_] = str(config[bstack1ll1ll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૬")][index][bstack11ll111l1l_opy_])
        else:
          bstack1lll1l1lll_opy_[bstack11ll111l1l_opy_] = config[bstack1ll1ll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૭")][index][bstack11ll111l1l_opy_]
        del (config[bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૮")][index][bstack11ll111l1l_opy_])
    bstack111l111111_opy_ = update(bstack111l111111_opy_, bstack1lll1l1lll_opy_)
  bstack1ll1lllll1_opy_ = bstack1llll1lll1_opy_(config, index)
  for bstack11l1lllll_opy_ in bstack1l11ll11l_opy_ + list(bstack11lll111ll_opy_.keys()):
    if bstack11l1lllll_opy_ in bstack1ll1lllll1_opy_:
      bstack111l111111_opy_[bstack11l1lllll_opy_] = bstack1ll1lllll1_opy_[bstack11l1lllll_opy_]
      del (bstack1ll1lllll1_opy_[bstack11l1lllll_opy_])
  if bstack11l11llll_opy_(config):
    bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭૯")] = True
    caps.update(bstack111l111111_opy_)
    caps[bstack1ll1ll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ૰")] = bstack1ll1lllll1_opy_
  else:
    bstack1ll1lllll1_opy_[bstack1ll1ll1_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨ૱")] = False
    caps.update(bstack11l11lll11_opy_(bstack1ll1lllll1_opy_, bstack111l111111_opy_))
    if bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ૲") in caps:
      caps[bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫ૳")] = caps[bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ૴")]
      del (caps[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ૵")])
    if bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ૶") in caps:
      caps[bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ૷")] = caps[bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ૸")]
      del (caps[bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪૹ")])
  return caps
def bstack111ll1lll_opy_():
  global bstack11111l1l1l_opy_
  global CONFIG
  if bstack11lll11l1_opy_() <= version.parse(bstack1ll1ll1_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪૺ")):
    if bstack11111l1l1l_opy_ != bstack1ll1ll1_opy_ (u"ࠫࠬૻ"):
      return bstack1ll1ll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨૼ") + bstack11111l1l1l_opy_ + bstack1ll1ll1_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥ૽")
    return bstack111llll1l1_opy_
  if bstack11111l1l1l_opy_ != bstack1ll1ll1_opy_ (u"ࠧࠨ૾"):
    return bstack1ll1ll1_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥ૿") + bstack11111l1l1l_opy_ + bstack1ll1ll1_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥ଀")
  return bstack1l11ll1ll1_opy_
def bstack11llllllll_opy_(options):
  return hasattr(options, bstack1ll1ll1_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫଁ"))
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
def bstack1lll11l111_opy_(options, bstack1l11l1l1l1_opy_):
  for bstack1111l1lll_opy_ in bstack1l11l1l1l1_opy_:
    if bstack1111l1lll_opy_ in [bstack1ll1ll1_opy_ (u"ࠫࡦࡸࡧࡴࠩଂ"), bstack1ll1ll1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩଃ")]:
      continue
    if bstack1111l1lll_opy_ in options._experimental_options:
      options._experimental_options[bstack1111l1lll_opy_] = update(options._experimental_options[bstack1111l1lll_opy_],
                                                         bstack1l11l1l1l1_opy_[bstack1111l1lll_opy_])
    else:
      options.add_experimental_option(bstack1111l1lll_opy_, bstack1l11l1l1l1_opy_[bstack1111l1lll_opy_])
  if bstack1ll1ll1_opy_ (u"࠭ࡡࡳࡩࡶࠫ଄") in bstack1l11l1l1l1_opy_:
    for arg in bstack1l11l1l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠧࡢࡴࡪࡷࠬଅ")]:
      options.add_argument(arg)
    del (bstack1l11l1l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଆ")])
  if bstack1ll1ll1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ଇ") in bstack1l11l1l1l1_opy_:
    for ext in bstack1l11l1l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧଈ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l11l1l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨଉ")])
def bstack1lll11l11_opy_(options, bstack1l1l11l11_opy_):
  if bstack1ll1ll1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫଊ") in bstack1l1l11l11_opy_:
    for bstack1l111111ll_opy_ in bstack1l1l11l11_opy_[bstack1ll1ll1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬଋ")]:
      if bstack1l111111ll_opy_ in options._preferences:
        options._preferences[bstack1l111111ll_opy_] = update(options._preferences[bstack1l111111ll_opy_], bstack1l1l11l11_opy_[bstack1ll1ll1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ଌ")][bstack1l111111ll_opy_])
      else:
        options.set_preference(bstack1l111111ll_opy_, bstack1l1l11l11_opy_[bstack1ll1ll1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ଍")][bstack1l111111ll_opy_])
  if bstack1ll1ll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ଎") in bstack1l1l11l11_opy_:
    for arg in bstack1l1l11l11_opy_[bstack1ll1ll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଏ")]:
      options.add_argument(arg)
def bstack11lllll1l_opy_(options, bstack111llll11_opy_):
  if bstack1ll1ll1_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬଐ") in bstack111llll11_opy_:
    options.use_webview(bool(bstack111llll11_opy_[bstack1ll1ll1_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭଑")]))
  bstack1lll11l111_opy_(options, bstack111llll11_opy_)
def bstack1l111ll111_opy_(options, bstack1111l11ll_opy_):
  for bstack1ll1l1ll11_opy_ in bstack1111l11ll_opy_:
    if bstack1ll1l1ll11_opy_ in [bstack1ll1ll1_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪ଒"), bstack1ll1ll1_opy_ (u"ࠧࡢࡴࡪࡷࠬଓ")]:
      continue
    options.set_capability(bstack1ll1l1ll11_opy_, bstack1111l11ll_opy_[bstack1ll1l1ll11_opy_])
  if bstack1ll1ll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଔ") in bstack1111l11ll_opy_:
    for arg in bstack1111l11ll_opy_[bstack1ll1ll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧକ")]:
      options.add_argument(arg)
  if bstack1ll1ll1_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧଖ") in bstack1111l11ll_opy_:
    options.bstack111lll1111_opy_(bool(bstack1111l11ll_opy_[bstack1ll1ll1_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨଗ")]))
def bstack1ll1111lll_opy_(options, bstack1ll11lllll_opy_):
  for bstack1l11l1ll1l_opy_ in bstack1ll11lllll_opy_:
    if bstack1l11l1ll1l_opy_ in [bstack1ll1ll1_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩଘ"), bstack1ll1ll1_opy_ (u"࠭ࡡࡳࡩࡶࠫଙ")]:
      continue
    options._options[bstack1l11l1ll1l_opy_] = bstack1ll11lllll_opy_[bstack1l11l1ll1l_opy_]
  if bstack1ll1ll1_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଚ") in bstack1ll11lllll_opy_:
    for bstack1lll1lllll_opy_ in bstack1ll11lllll_opy_[bstack1ll1ll1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬଛ")]:
      options.bstack1llllllll1_opy_(
        bstack1lll1lllll_opy_, bstack1ll11lllll_opy_[bstack1ll1ll1_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ଜ")][bstack1lll1lllll_opy_])
  if bstack1ll1ll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଝ") in bstack1ll11lllll_opy_:
    for arg in bstack1ll11lllll_opy_[bstack1ll1ll1_opy_ (u"ࠫࡦࡸࡧࡴࠩଞ")]:
      options.add_argument(arg)
def bstack1l1llll1ll_opy_(options, caps):
  if not hasattr(options, bstack1ll1ll1_opy_ (u"ࠬࡑࡅ࡚ࠩଟ")):
    return
  if options.KEY == bstack1ll1ll1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫଠ"):
    options = bstack11111ll1_opy_.bstack1ll1l1lll1_opy_(bstack1lll1l11l1_opy_=options, config=CONFIG)
  if options.KEY == bstack1ll1ll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬଡ") and options.KEY in caps:
    bstack1lll11l111_opy_(options, caps[bstack1ll1ll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ଢ")])
  elif options.KEY == bstack1ll1ll1_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧଣ") and options.KEY in caps:
    bstack1lll11l11_opy_(options, caps[bstack1ll1ll1_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨତ")])
  elif options.KEY == bstack1ll1ll1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬଥ") and options.KEY in caps:
    bstack1l111ll111_opy_(options, caps[bstack1ll1ll1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ଦ")])
  elif options.KEY == bstack1ll1ll1_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧଧ") and options.KEY in caps:
    bstack11lllll1l_opy_(options, caps[bstack1ll1ll1_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨନ")])
  elif options.KEY == bstack1ll1ll1_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ଩") and options.KEY in caps:
    bstack1ll1111lll_opy_(options, caps[bstack1ll1ll1_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨପ")])
def bstack1l1l1l1l1l_opy_(caps):
  global bstack11ll1l11l1_opy_
  if isinstance(os.environ.get(bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫଫ")), str):
    bstack11ll1l11l1_opy_ = eval(os.getenv(bstack1ll1ll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬବ")))
  if bstack11ll1l11l1_opy_:
    if bstack111111111_opy_() < version.parse(bstack1ll1ll1_opy_ (u"ࠬ࠸࠮࠴࠰࠳ࠫଭ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1ll1ll1_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ମ")
    if bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬଯ") in caps:
      browser = caps[bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ର")]
    elif bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪ଱") in caps:
      browser = caps[bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫଲ")]
    browser = str(browser).lower()
    if browser == bstack1ll1ll1_opy_ (u"ࠫ࡮ࡶࡨࡰࡰࡨࠫଳ") or browser == bstack1ll1ll1_opy_ (u"ࠬ࡯ࡰࡢࡦࠪ଴"):
      browser = bstack1ll1ll1_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭ଵ")
    if browser == bstack1ll1ll1_opy_ (u"ࠧࡴࡣࡰࡷࡺࡴࡧࠨଶ"):
      browser = bstack1ll1ll1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨଷ")
    if browser not in [bstack1ll1ll1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩସ"), bstack1ll1ll1_opy_ (u"ࠪࡩࡩ࡭ࡥࠨହ"), bstack1ll1ll1_opy_ (u"ࠫ࡮࡫ࠧ଺"), bstack1ll1ll1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬ଻"), bstack1ll1ll1_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾ଼ࠧ")]:
      return None
    try:
      package = bstack1ll1ll1_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶ࠳ࢁࡽ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩଽ").format(browser)
      name = bstack1ll1ll1_opy_ (u"ࠨࡑࡳࡸ࡮ࡵ࡮ࡴࠩା")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11llllllll_opy_(options):
        return None
      for bstack11l1lllll_opy_ in caps.keys():
        options.set_capability(bstack11l1lllll_opy_, caps[bstack11l1lllll_opy_])
      bstack1l1llll1ll_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1lll11llll_opy_(options, bstack1lll11l1l_opy_):
  if not bstack11llllllll_opy_(options):
    return
  for bstack11l1lllll_opy_ in bstack1lll11l1l_opy_.keys():
    if bstack11l1lllll_opy_ in bstack11ll1llll1_opy_:
      continue
    if bstack11l1lllll_opy_ in options._caps and type(options._caps[bstack11l1lllll_opy_]) in [dict, list]:
      options._caps[bstack11l1lllll_opy_] = update(options._caps[bstack11l1lllll_opy_], bstack1lll11l1l_opy_[bstack11l1lllll_opy_])
    else:
      options.set_capability(bstack11l1lllll_opy_, bstack1lll11l1l_opy_[bstack11l1lllll_opy_])
  bstack1l1llll1ll_opy_(options, bstack1lll11l1l_opy_)
  if bstack1ll1ll1_opy_ (u"ࠩࡰࡳࡿࡀࡤࡦࡤࡸ࡫࡬࡫ࡲࡂࡦࡧࡶࡪࡹࡳࠨି") in options._caps:
    if options._caps[bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨୀ")] and options._caps[bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩୁ")].lower() != bstack1ll1ll1_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭ୂ"):
      del options._caps[bstack1ll1ll1_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬୃ")]
def bstack1l1l1l1111_opy_(proxy_config):
  if bstack1ll1ll1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫୄ") in proxy_config:
    proxy_config[bstack1ll1ll1_opy_ (u"ࠨࡵࡶࡰࡕࡸ࡯ࡹࡻࠪ୅")] = proxy_config[bstack1ll1ll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭୆")]
    del (proxy_config[bstack1ll1ll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧେ")])
  if bstack1ll1ll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧୈ") in proxy_config and proxy_config[bstack1ll1ll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ୉")].lower() != bstack1ll1ll1_opy_ (u"࠭ࡤࡪࡴࡨࡧࡹ࠭୊"):
    proxy_config[bstack1ll1ll1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪୋ")] = bstack1ll1ll1_opy_ (u"ࠨ࡯ࡤࡲࡺࡧ࡬ࠨୌ")
  if bstack1ll1ll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡂࡷࡷࡳࡨࡵ࡮ࡧ࡫ࡪ࡙ࡷࡲ୍ࠧ") in proxy_config:
    proxy_config[bstack1ll1ll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭୎")] = bstack1ll1ll1_opy_ (u"ࠫࡵࡧࡣࠨ୏")
  return proxy_config
def bstack1lll1l1111_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1ll1ll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ୐") in config:
    return proxy
  config[bstack1ll1ll1_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୑")] = bstack1l1l1l1111_opy_(config[bstack1ll1ll1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭୒")])
  if proxy == None:
    proxy = Proxy(config[bstack1ll1ll1_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧ୓")])
  return proxy
def bstack11111lll1l_opy_(self):
  global CONFIG
  global bstack1111l11ll1_opy_
  try:
    proxy = bstack1ll1l1ll1_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1ll1ll1_opy_ (u"ࠩ࠱ࡴࡦࡩࠧ୔")):
        proxies = bstack1l1111111l_opy_(proxy, bstack111ll1lll_opy_())
        if len(proxies) > 0:
          protocol, bstack11l111llll_opy_ = proxies.popitem()
          if bstack1ll1ll1_opy_ (u"ࠥ࠾࠴࠵ࠢ୕") in bstack11l111llll_opy_:
            return bstack11l111llll_opy_
          else:
            return bstack1ll1ll1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧୖ") + bstack11l111llll_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1ll1ll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡲࡵࡳࡽࡿࠠࡶࡴ࡯ࠤ࠿ࠦࡻࡾࠤୗ").format(str(e)))
  return bstack1111l11ll1_opy_(self)
def bstack1ll11ll11_opy_():
  global CONFIG
  return bstack11lll11lll_opy_(CONFIG) and bstack11lll11111_opy_() and bstack11lll11l1_opy_() >= version.parse(bstack1l11ll11l1_opy_)
def bstack111ll11ll_opy_():
  global CONFIG
  return (bstack1ll1ll1_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ୘") in CONFIG or bstack1ll1ll1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ୙") in CONFIG) and bstack11l11111l_opy_()
def bstack111llll1l_opy_(config):
  bstack1l1ll1111l_opy_ = {}
  if bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୚") in config:
    bstack1l1ll1111l_opy_ = config[bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୛")]
  if bstack1ll1ll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩଡ଼") in config:
    bstack1l1ll1111l_opy_ = config[bstack1ll1ll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪଢ଼")]
  proxy = bstack1ll1l1ll1_opy_(config)
  if proxy:
    if proxy.endswith(bstack1ll1ll1_opy_ (u"ࠬ࠴ࡰࡢࡥࠪ୞")) and os.path.isfile(proxy):
      bstack1l1ll1111l_opy_[bstack1ll1ll1_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩୟ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1ll1ll1_opy_ (u"ࠧ࠯ࡲࡤࡧࠬୠ")):
        proxies = bstack111ll1111l_opy_(config, bstack111ll1lll_opy_())
        if len(proxies) > 0:
          protocol, bstack11l111llll_opy_ = proxies.popitem()
          if bstack1ll1ll1_opy_ (u"ࠣ࠼࠲࠳ࠧୡ") in bstack11l111llll_opy_:
            parsed_url = urlparse(bstack11l111llll_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1ll1ll1_opy_ (u"ࠤ࠽࠳࠴ࠨୢ") + bstack11l111llll_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1l1ll1111l_opy_[bstack1ll1ll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭ୣ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1l1ll1111l_opy_[bstack1ll1ll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡳࡷࡺࠧ୤")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1l1ll1111l_opy_[bstack1ll1ll1_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨ୥")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1l1ll1111l_opy_[bstack1ll1ll1_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩ୦")] = str(parsed_url.password)
  return bstack1l1ll1111l_opy_
def bstack1l1lllll1_opy_(config):
  if bstack1ll1ll1_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬ୧") in config:
    return config[bstack1ll1ll1_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭୨")]
  return {}
def bstack1lll11lll1_opy_(caps):
  global bstack1ll11ll1ll_opy_
  if bstack1ll1ll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ୩") in caps:
    caps[bstack1ll1ll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ୪")][bstack1ll1ll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪ୫")] = True
    if bstack1ll11ll1ll_opy_:
      caps[bstack1ll1ll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭୬")][bstack1ll1ll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ୭")] = bstack1ll11ll1ll_opy_
  else:
    caps[bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬ୮")] = True
    if bstack1ll11ll1ll_opy_:
      caps[bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ୯")] = bstack1ll11ll1ll_opy_
@measure(event_name=EVENTS.bstack1l1llllll_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack11ll11ll1_opy_():
  global CONFIG
  if not bstack11l1l111ll_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭୰") in CONFIG and bstack1ll1l1llll_opy_(CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧୱ")]):
    if (
      bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୲") in CONFIG
      and bstack1ll1l1llll_opy_(CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୳")].get(bstack1ll1ll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠪ୴")))
    ):
      logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡍࡱࡦࡥࡱࠦࡢࡪࡰࡤࡶࡾࠦ࡮ࡰࡶࠣࡷࡹࡧࡲࡵࡧࡧࠤࡦࡹࠠࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡦࡰࡤࡦࡱ࡫ࡤࠣ୵"))
      return
    bstack1l1ll1111l_opy_ = bstack111llll1l_opy_(CONFIG)
    bstack1lll11l11l_opy_(CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ୶")], bstack1l1ll1111l_opy_)
def bstack1lll11l11l_opy_(key, bstack1l1ll1111l_opy_):
  global bstack111l1ll111_opy_
  logger.info(bstack11lll1l111_opy_)
  try:
    bstack111l1ll111_opy_ = Local()
    bstack111ll1111_opy_ = {bstack1ll1ll1_opy_ (u"ࠩ࡮ࡩࡾ࠭୷"): key}
    bstack111ll1111_opy_.update(bstack1l1ll1111l_opy_)
    logger.debug(bstack1l11l11ll1_opy_.format(str(bstack111ll1111_opy_)).replace(key, bstack1ll1ll1_opy_ (u"ࠪ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧ୸")))
    bstack111l1ll111_opy_.start(**bstack111ll1111_opy_)
    if bstack111l1ll111_opy_.isRunning():
      logger.info(bstack1l1111l1ll_opy_)
  except Exception as e:
    bstack1lll11l1l1_opy_(bstack1l1llllll1_opy_.format(str(e)))
def bstack1l111llll1_opy_():
  global bstack111l1ll111_opy_
  if bstack111l1ll111_opy_.isRunning():
    logger.info(bstack1l1l1ll11_opy_)
    bstack111l1ll111_opy_.stop()
  bstack111l1ll111_opy_ = None
def bstack1l1l1l1l11_opy_(bstack111l1l1ll1_opy_=[]):
  global CONFIG
  bstack11l1l1l1l_opy_ = []
  bstack11ll11111_opy_ = [bstack1ll1ll1_opy_ (u"ࠫࡴࡹࠧ୹"), bstack1ll1ll1_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ୺"), bstack1ll1ll1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ୻"), bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ୼"), bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭୽"), bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ୾")]
  try:
    for err in bstack111l1l1ll1_opy_:
      bstack1111llll11_opy_ = {}
      for k in bstack11ll11111_opy_:
        val = CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭୿")][int(err[bstack1ll1ll1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ஀")])].get(k)
        if val:
          bstack1111llll11_opy_[k] = val
      if(err[bstack1ll1ll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ஁")] != bstack1ll1ll1_opy_ (u"࠭ࠧஂ")):
        bstack1111llll11_opy_[bstack1ll1ll1_opy_ (u"ࠧࡵࡧࡶࡸࡸ࠭ஃ")] = {
          err[bstack1ll1ll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭஄")]: err[bstack1ll1ll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨஅ")]
        }
        bstack11l1l1l1l_opy_.append(bstack1111llll11_opy_)
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬࡯ࡳ࡯ࡤࡸࡹ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶ࠽ࠤࠬஆ") + str(e))
  finally:
    return bstack11l1l1l1l_opy_
def bstack1111llllll_opy_(file_name):
  bstack1llll11111_opy_ = []
  try:
    bstack1l1ll1l1ll_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1l1ll1l1ll_opy_):
      with open(bstack1l1ll1l1ll_opy_) as f:
        bstack1llll1ll1l_opy_ = json.load(f)
        bstack1llll11111_opy_ = bstack1llll1ll1l_opy_
      os.remove(bstack1l1ll1l1ll_opy_)
    return bstack1llll11111_opy_
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡪࡰࡧ࡭ࡳ࡭ࠠࡦࡴࡵࡳࡷࠦ࡬ࡪࡵࡷ࠾ࠥ࠭இ") + str(e))
    return bstack1llll11111_opy_
def bstack111l1l1ll_opy_():
  try:
      from bstack_utils.constants import bstack1l11ll111l_opy_, EVENTS
      from bstack_utils.helper import bstack111l1l11l1_opy_, get_host_info, bstack11111l11_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack1llll111l1_opy_ = os.path.join(os.getcwd(), bstack1ll1ll1_opy_ (u"ࠬࡲ࡯ࡨࠩஈ"), bstack1ll1ll1_opy_ (u"࠭࡫ࡦࡻ࠰ࡱࡪࡺࡲࡪࡥࡶ࠲࡯ࡹ࡯࡯ࠩஉ"))
      lock = FileLock(bstack1llll111l1_opy_+bstack1ll1ll1_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨஊ"))
      def bstack1ll1ll1l_opy_():
          try:
              with lock:
                  with open(bstack1llll111l1_opy_, bstack1ll1ll1_opy_ (u"ࠣࡴࠥ஋"), encoding=bstack1ll1ll1_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣ஌")) as file:
                      data = json.load(file)
                      config = {
                          bstack1ll1ll1_opy_ (u"ࠥ࡬ࡪࡧࡤࡦࡴࡶࠦ஍"): {
                              bstack1ll1ll1_opy_ (u"ࠦࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠥஎ"): bstack1ll1ll1_opy_ (u"ࠧࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠣஏ"),
                          }
                      }
                      bstack1l11l1ll11_opy_ = datetime.utcnow()
                      bstack1l11l1ll_opy_ = bstack1l11l1ll11_opy_.strftime(bstack1ll1ll1_opy_ (u"ࠨ࡚ࠥ࠯ࠨࡱ࠲ࠫࡤࡕࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࠱ࠩ࡫ࠦࡕࡕࡅࠥஐ"))
                      test_id = os.environ.get(bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ஑")) if os.environ.get(bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ஒ")) else bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦஓ"))
                      payload = {
                          bstack1ll1ll1_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠢஔ"): bstack1ll1ll1_opy_ (u"ࠦࡸࡪ࡫ࡠࡧࡹࡩࡳࡺࡳࠣக"),
                          bstack1ll1ll1_opy_ (u"ࠧࡪࡡࡵࡣࠥ஖"): {
                              bstack1ll1ll1_opy_ (u"ࠨࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡶࡷ࡬ࡨࠧ஗"): test_id,
                              bstack1ll1ll1_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫ࡤࡠࡦࡤࡽࠧ஘"): bstack1l11l1ll_opy_,
                              bstack1ll1ll1_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟࡯ࡣࡰࡩࠧங"): bstack1ll1ll1_opy_ (u"ࠤࡖࡈࡐࡌࡥࡢࡶࡸࡶࡪࡖࡥࡳࡨࡲࡶࡲࡧ࡮ࡤࡧࠥச"),
                              bstack1ll1ll1_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡ࡭ࡷࡴࡴࠢ஛"): {
                                  bstack1ll1ll1_opy_ (u"ࠦࡲ࡫ࡡࡴࡷࡵࡩࡸࠨஜ"): data,
                                  bstack1ll1ll1_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢ஝"): bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣஞ"))
                              },
                              bstack1ll1ll1_opy_ (u"ࠢࡶࡵࡨࡶࡤࡪࡡࡵࡣࠥட"): bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠣࡷࡶࡩࡷࡔࡡ࡮ࡧࠥ஠")),
                              bstack1ll1ll1_opy_ (u"ࠤ࡫ࡳࡸࡺ࡟ࡪࡰࡩࡳࠧ஡"): get_host_info()
                          }
                      }
                      bstack1l1ll11l1_opy_ = bstack11l1l1l11_opy_(cli.config, [bstack1ll1ll1_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ஢"), bstack1ll1ll1_opy_ (u"ࠦࡪࡪࡳࡊࡰࡶࡸࡷࡻ࡭ࡦࡰࡷࡥࡹ࡯࡯࡯ࠤண"), bstack1ll1ll1_opy_ (u"ࠧࡧࡰࡪࠤத")], bstack1l11ll111l_opy_)
                      response = bstack111l1l11l1_opy_(bstack1ll1ll1_opy_ (u"ࠨࡐࡐࡕࡗࠦ஥"), bstack1l1ll11l1_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack1ll1ll1_opy_ (u"ࠢࡅࡣࡷࡥࠥࡹࡥ࡯ࡶࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺࠢࡷࡳࠥࢁࡽࠡࡹ࡬ࡸ࡭ࠦࡤࡢࡶࡤࠤࢀࢃࠢ஦").format(bstack1l11ll111l_opy_, payload))
                      else:
                          logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡔࡨࡵࡺ࡫ࡳࡵࠢࡩࡥ࡮ࡲࡥࡥࠢࡩࡳࡷࠦࡻࡾࠢࡺ࡭ࡹ࡮ࠠࡥࡣࡷࡥࠥࢁࡽࠣ஧").format(bstack1l11ll111l_opy_, payload))
          except Exception as e:
              logger.debug(bstack1ll1ll1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥ࡯ࡦࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳࠡࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣࡿࢂࠨந").format(e))
      bstack1ll1ll1l_opy_()
      bstack11lll1ll1l_opy_(bstack1llll111l1_opy_, logger)
  except:
    pass
def bstack1l1ll11ll_opy_():
  global bstack1ll1lll1l_opy_
  global bstack1l1l1l1ll1_opy_
  global bstack11l1l1111_opy_
  global bstack1ll111lll1_opy_
  global bstack1llll1111l_opy_
  global bstack1l11l1l11_opy_
  global CONFIG
  bstack11l1lll1l1_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫன"))
  if bstack11l1lll1l1_opy_ in [bstack1ll1ll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪப"), bstack1ll1ll1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ஫")]:
    bstack1l1l111111_opy_()
  percy.shutdown()
  if bstack1ll1lll1l_opy_:
    logger.warning(bstack1ll1111l11_opy_.format(str(bstack1ll1lll1l_opy_)))
  else:
    try:
      bstack1ll111l11_opy_ = bstack11l111lll_opy_(bstack1ll1ll1_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬ஬"), logger)
      if bstack1ll111l11_opy_.get(bstack1ll1ll1_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬ஭")) and bstack1ll111l11_opy_.get(bstack1ll1ll1_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ம")).get(bstack1ll1ll1_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫய")):
        logger.warning(bstack1ll1111l11_opy_.format(str(bstack1ll111l11_opy_[bstack1ll1ll1_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨர")][bstack1ll1ll1_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭ற")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1ll11111l_opy_.invoke(Events.bstack11l11l11ll_opy_)
  logger.info(bstack11l1ll11l1_opy_)
  global bstack111l1ll111_opy_
  if bstack111l1ll111_opy_:
    bstack1l111llll1_opy_()
  try:
    with bstack11lll11l1l_opy_:
      bstack111111ll1_opy_ = bstack1l1l1l1ll1_opy_.copy()
    for driver in bstack111111ll1_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack111ll11111_opy_)
  if bstack1l11l1l11_opy_ == bstack1ll1ll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫல"):
    bstack1llll1111l_opy_ = bstack1111llllll_opy_(bstack1ll1ll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧள"))
  if bstack1l11l1l11_opy_ == bstack1ll1ll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧழ") and len(bstack1ll111lll1_opy_) == 0:
    bstack1ll111lll1_opy_ = bstack1111llllll_opy_(bstack1ll1ll1_opy_ (u"ࠨࡲࡺࡣࡵࡿࡴࡦࡵࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭வ"))
    if len(bstack1ll111lll1_opy_) == 0:
      bstack1ll111lll1_opy_ = bstack1111llllll_opy_(bstack1ll1ll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡳࡴࡵࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨஶ"))
  bstack11l11l111l_opy_ = bstack1ll1ll1_opy_ (u"ࠪࠫஷ")
  if len(bstack11l1l1111_opy_) > 0:
    bstack11l11l111l_opy_ = bstack1l1l1l1l11_opy_(bstack11l1l1111_opy_)
  elif len(bstack1ll111lll1_opy_) > 0:
    bstack11l11l111l_opy_ = bstack1l1l1l1l11_opy_(bstack1ll111lll1_opy_)
  elif len(bstack1llll1111l_opy_) > 0:
    bstack11l11l111l_opy_ = bstack1l1l1l1l11_opy_(bstack1llll1111l_opy_)
  elif len(bstack11ll11l11_opy_) > 0:
    bstack11l11l111l_opy_ = bstack1l1l1l1l11_opy_(bstack11ll11l11_opy_)
  if bool(bstack11l11l111l_opy_):
    bstack1l1ll1ll1_opy_(bstack11l11l111l_opy_)
  else:
    bstack1l1ll1ll1_opy_()
  bstack11lll1ll1l_opy_(bstack11llllll1_opy_, logger)
  if bstack11l1lll1l1_opy_ not in [bstack1ll1ll1_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬஸ")]:
    bstack111l1l1ll_opy_()
  bstack1l1l1ll111_opy_.bstack1l1l1l1l_opy_(CONFIG)
  if len(bstack1llll1111l_opy_) > 0:
    sys.exit(len(bstack1llll1111l_opy_))
def bstack1lllll1111_opy_(bstack1l1l11ll11_opy_, frame):
  global bstack11111l11_opy_
  logger.error(bstack111l111ll1_opy_)
  bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱࡔ࡯ࠨஹ"), bstack1l1l11ll11_opy_)
  if hasattr(signal, bstack1ll1ll1_opy_ (u"࠭ࡓࡪࡩࡱࡥࡱࡹࠧ஺")):
    bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ஻"), signal.Signals(bstack1l1l11ll11_opy_).name)
  else:
    bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ஼"), bstack1ll1ll1_opy_ (u"ࠩࡖࡍࡌ࡛ࡎࡌࡐࡒ࡛ࡓ࠭஽"))
  if cli.is_running():
    bstack1ll11111l_opy_.invoke(Events.bstack11l11l11ll_opy_)
  bstack11l1lll1l1_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫா"))
  if bstack11l1lll1l1_opy_ == bstack1ll1ll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫி") and not cli.is_enabled(CONFIG):
    bstack1ll111ll_opy_.stop(bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬீ")))
  bstack1l1ll11ll_opy_()
  sys.exit(1)
def bstack1lll11l1l1_opy_(err):
  logger.critical(bstack11l11l1ll1_opy_.format(str(err)))
  bstack1l1ll1ll1_opy_(bstack11l11l1ll1_opy_.format(str(err)), True)
  atexit.unregister(bstack1l1ll11ll_opy_)
  bstack1l1l111111_opy_()
  sys.exit(1)
def bstack1l1l1lllll_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l1ll1ll1_opy_(message, True)
  atexit.unregister(bstack1l1ll11ll_opy_)
  bstack1l1l111111_opy_()
  sys.exit(1)
def bstack111lll1lll_opy_():
  global CONFIG
  global bstack1l1llll1l1_opy_
  global bstack1l11l111l1_opy_
  global bstack111l1ll1ll_opy_
  CONFIG = bstack1lll1111l_opy_()
  load_dotenv(CONFIG.get(bstack1ll1ll1_opy_ (u"࠭ࡥ࡯ࡸࡉ࡭ࡱ࡫ࠧு")))
  bstack1ll11ll111_opy_()
  bstack1l11lll1l1_opy_()
  CONFIG = bstack11lll1lll_opy_(CONFIG)
  update(CONFIG, bstack1l11l111l1_opy_)
  update(CONFIG, bstack1l1llll1l1_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1lll1l111l_opy_(CONFIG)
  bstack111l1ll1ll_opy_ = bstack11l1l111ll_opy_(CONFIG)
  os.environ[bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪூ")] = bstack111l1ll1ll_opy_.__str__().lower()
  bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ௃"), bstack111l1ll1ll_opy_)
  if (bstack1ll1ll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௄") in CONFIG and bstack1ll1ll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௅") in bstack1l1llll1l1_opy_) or (
          bstack1ll1ll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧெ") in CONFIG and bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨே") not in bstack1l11l111l1_opy_):
    if os.getenv(bstack1ll1ll1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪை")):
      CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ௉")] = os.getenv(bstack1ll1ll1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬொ"))
    else:
      if not CONFIG.get(bstack1ll1ll1_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠧோ"), bstack1ll1ll1_opy_ (u"ࠥࠦௌ")) in bstack1ll1l1111_opy_:
        bstack1l11l1l11l_opy_()
  elif (bstack1ll1ll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫்ࠧ") not in CONFIG and bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ௎") in CONFIG) or (
          bstack1ll1ll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௏") in bstack1l11l111l1_opy_ and bstack1ll1ll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪௐ") not in bstack1l1llll1l1_opy_):
    del (CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ௑")])
  if bstack1ll111ll11_opy_(CONFIG):
    bstack1lll11l1l1_opy_(bstack1lllllll11_opy_)
  Config.bstack1llllllll_opy_().set_property(bstack1ll1ll1_opy_ (u"ࠤࡸࡷࡪࡸࡎࡢ࡯ࡨࠦ௒"), CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ௓")])
  bstack1l111l1l1l_opy_()
  bstack1llll1l111_opy_()
  if bstack11ll1l11l1_opy_ and not CONFIG.get(bstack1ll1ll1_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠢ௔"), bstack1ll1ll1_opy_ (u"ࠧࠨ௕")) in bstack1ll1l1111_opy_:
    CONFIG[bstack1ll1ll1_opy_ (u"࠭ࡡࡱࡲࠪ௖")] = bstack1111ll1ll_opy_(CONFIG)
    logger.info(bstack11111ll1ll_opy_.format(CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡢࡲࡳࠫௗ")]))
  if not bstack111l1ll1ll_opy_:
    CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௘")] = [{}]
def bstack111ll11ll1_opy_(config, bstack11l1ll1111_opy_):
  global CONFIG
  global bstack11ll1l11l1_opy_
  CONFIG = config
  bstack11ll1l11l1_opy_ = bstack11l1ll1111_opy_
def bstack1llll1l111_opy_():
  global CONFIG
  global bstack11ll1l11l1_opy_
  if bstack1ll1ll1_opy_ (u"ࠩࡤࡴࡵ࠭௙") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l1l1lllll_opy_(e, bstack11l111111_opy_)
    bstack11ll1l11l1_opy_ = True
    bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ௚"), True)
def bstack1111ll1ll_opy_(config):
  bstack11ll1l1ll_opy_ = bstack1ll1ll1_opy_ (u"ࠫࠬ௛")
  app = config[bstack1ll1ll1_opy_ (u"ࠬࡧࡰࡱࠩ௜")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1111ll11l_opy_:
      if os.path.exists(app):
        bstack11ll1l1ll_opy_ = bstack1111ll1111_opy_(config, app)
      elif bstack1l1ll1lll1_opy_(app):
        bstack11ll1l1ll_opy_ = app
      else:
        bstack1lll11l1l1_opy_(bstack11ll1l111_opy_.format(app))
    else:
      if bstack1l1ll1lll1_opy_(app):
        bstack11ll1l1ll_opy_ = app
      elif os.path.exists(app):
        bstack11ll1l1ll_opy_ = bstack1111ll1111_opy_(app)
      else:
        bstack1lll11l1l1_opy_(bstack11lll1ll1_opy_)
  else:
    if len(app) > 2:
      bstack1lll11l1l1_opy_(bstack111111l1l_opy_)
    elif len(app) == 2:
      if bstack1ll1ll1_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ௝") in app and bstack1ll1ll1_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ௞") in app:
        if os.path.exists(app[bstack1ll1ll1_opy_ (u"ࠨࡲࡤࡸ࡭࠭௟")]):
          bstack11ll1l1ll_opy_ = bstack1111ll1111_opy_(config, app[bstack1ll1ll1_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ௠")], app[bstack1ll1ll1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭௡")])
        else:
          bstack1lll11l1l1_opy_(bstack11ll1l111_opy_.format(app))
      else:
        bstack1lll11l1l1_opy_(bstack111111l1l_opy_)
    else:
      for key in app:
        if key in bstack11l1lll1l_opy_:
          if key == bstack1ll1ll1_opy_ (u"ࠫࡵࡧࡴࡩࠩ௢"):
            if os.path.exists(app[key]):
              bstack11ll1l1ll_opy_ = bstack1111ll1111_opy_(config, app[key])
            else:
              bstack1lll11l1l1_opy_(bstack11ll1l111_opy_.format(app))
          else:
            bstack11ll1l1ll_opy_ = app[key]
        else:
          bstack1lll11l1l1_opy_(bstack11lll1l1l_opy_)
  return bstack11ll1l1ll_opy_
def bstack1l1ll1lll1_opy_(bstack11ll1l1ll_opy_):
  import re
  bstack1llll11l1l_opy_ = re.compile(bstack1ll1ll1_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧ௣"))
  bstack1ll1ll111_opy_ = re.compile(bstack1ll1ll1_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮࠴ࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥ௤"))
  if bstack1ll1ll1_opy_ (u"ࠧࡣࡵ࠽࠳࠴࠭௥") in bstack11ll1l1ll_opy_ or re.fullmatch(bstack1llll11l1l_opy_, bstack11ll1l1ll_opy_) or re.fullmatch(bstack1ll1ll111_opy_, bstack11ll1l1ll_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack11llll1l1_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack1111ll1111_opy_(config, path, bstack111ll1lll1_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1ll1ll1_opy_ (u"ࠨࡴࡥࠫ௦")).read()).hexdigest()
  bstack1111l1ll1_opy_ = bstack1111l1llll_opy_(md5_hash)
  bstack11ll1l1ll_opy_ = None
  if bstack1111l1ll1_opy_:
    logger.info(bstack1l11111ll_opy_.format(bstack1111l1ll1_opy_, md5_hash))
    return bstack1111l1ll1_opy_
  bstack111lllll1_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack1ll1ll1_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧ௧"): (os.path.basename(path), open(os.path.abspath(path), bstack1ll1ll1_opy_ (u"ࠪࡶࡧ࠭௨")), bstack1ll1ll1_opy_ (u"ࠫࡹ࡫ࡸࡵ࠱ࡳࡰࡦ࡯࡮ࠨ௩")),
      bstack1ll1ll1_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ௪"): bstack111ll1lll1_opy_
    }
  )
  response = requests.post(bstack11l1llll1l_opy_, data=multipart_data,
                           headers={bstack1ll1ll1_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ௫"): multipart_data.content_type},
                           auth=(config[bstack1ll1ll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ௬")], config[bstack1ll1ll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ௭")]))
  try:
    res = json.loads(response.text)
    bstack11ll1l1ll_opy_ = res[bstack1ll1ll1_opy_ (u"ࠩࡤࡴࡵࡥࡵࡳ࡮ࠪ௮")]
    logger.info(bstack111lllll1l_opy_.format(bstack11ll1l1ll_opy_))
    bstack1111lll11l_opy_(md5_hash, bstack11ll1l1ll_opy_)
    cli.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡷࡳࡰࡴࡧࡤࡠࡣࡳࡴࠧ௯"), datetime.datetime.now() - bstack111lllll1_opy_)
  except ValueError as err:
    bstack1lll11l1l1_opy_(bstack11llll1l11_opy_.format(str(err)))
  return bstack11ll1l1ll_opy_
def bstack1l111l1l1l_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack111ll1l1l_opy_
  bstack1lll1l11l_opy_ = 1
  bstack111ll1l111_opy_ = 1
  if bstack1ll1ll1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ௰") in CONFIG:
    bstack111ll1l111_opy_ = CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ௱")]
  else:
    bstack111ll1l111_opy_ = bstack1111l1l1l1_opy_(framework_name, args) or 1
  if bstack1ll1ll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ௲") in CONFIG:
    bstack1lll1l11l_opy_ = len(CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ௳")])
  bstack111ll1l1l_opy_ = int(bstack111ll1l111_opy_) * int(bstack1lll1l11l_opy_)
def bstack1111l1l1l1_opy_(framework_name, args):
  if framework_name == bstack1ll11l11l1_opy_ and args and bstack1ll1ll1_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭௴") in args:
      bstack11ll11l111_opy_ = args.index(bstack1ll1ll1_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ௵"))
      return int(args[bstack11ll11l111_opy_ + 1]) or 1
  return 1
def bstack1111l1llll_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭௶"))
    bstack11ll1llll_opy_ = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠫࢃ࠭௷")), bstack1ll1ll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ௸"), bstack1ll1ll1_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧ௹"))
    if os.path.exists(bstack11ll1llll_opy_):
      try:
        bstack1ll111ll1_opy_ = json.load(open(bstack11ll1llll_opy_, bstack1ll1ll1_opy_ (u"ࠧࡳࡤࠪ௺")))
        if md5_hash in bstack1ll111ll1_opy_:
          bstack1l1l11llll_opy_ = bstack1ll111ll1_opy_[md5_hash]
          bstack1ll11l1l1l_opy_ = datetime.datetime.now()
          bstack11ll111ll_opy_ = datetime.datetime.strptime(bstack1l1l11llll_opy_[bstack1ll1ll1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ௻")], bstack1ll1ll1_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭௼"))
          if (bstack1ll11l1l1l_opy_ - bstack11ll111ll_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack1l1l11llll_opy_[bstack1ll1ll1_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ௽")]):
            return None
          return bstack1l1l11llll_opy_[bstack1ll1ll1_opy_ (u"ࠫ࡮ࡪࠧ௾")]
      except Exception as e:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮ࠠࡧ࡫࡯ࡩ࠿ࠦࡻࡾࠩ௿").format(str(e)))
    return None
  bstack11ll1llll_opy_ = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"࠭ࡾࠨఀ")), bstack1ll1ll1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧఁ"), bstack1ll1ll1_opy_ (u"ࠨࡣࡳࡴ࡚ࡶ࡬ࡰࡣࡧࡑࡉ࠻ࡈࡢࡵ࡫࠲࡯ࡹ࡯࡯ࠩం"))
  lock_file = bstack11ll1llll_opy_ + bstack1ll1ll1_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨః")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack11ll1llll_opy_):
        with open(bstack11ll1llll_opy_, bstack1ll1ll1_opy_ (u"ࠪࡶࠬఄ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll111ll1_opy_ = json.loads(content)
            if md5_hash in bstack1ll111ll1_opy_:
              bstack1l1l11llll_opy_ = bstack1ll111ll1_opy_[md5_hash]
              bstack1ll11l1l1l_opy_ = datetime.datetime.now()
              bstack11ll111ll_opy_ = datetime.datetime.strptime(bstack1l1l11llll_opy_[bstack1ll1ll1_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧఅ")], bstack1ll1ll1_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩఆ"))
              if (bstack1ll11l1l1l_opy_ - bstack11ll111ll_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack1l1l11llll_opy_[bstack1ll1ll1_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫఇ")]):
                return None
              return bstack1l1l11llll_opy_[bstack1ll1ll1_opy_ (u"ࠧࡪࡦࠪఈ")]
      return None
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡸ࡫ࡷ࡬ࠥ࡬ࡩ࡭ࡧࠣࡰࡴࡩ࡫ࡪࡰࡪࠤ࡫ࡵࡲࠡࡏࡇ࠹ࠥ࡮ࡡࡴࡪ࠽ࠤࢀࢃࠧఉ").format(str(e)))
    return None
def bstack1111lll11l_opy_(md5_hash, bstack11ll1l1ll_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬఊ"))
    bstack1l1l1l111_opy_ = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠪࢂࠬఋ")), bstack1ll1ll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఌ"))
    if not os.path.exists(bstack1l1l1l111_opy_):
      os.makedirs(bstack1l1l1l111_opy_)
    bstack11ll1llll_opy_ = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠬࢄࠧ఍")), bstack1ll1ll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ఎ"), bstack1ll1ll1_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨఏ"))
    bstack11l111l1ll_opy_ = {
      bstack1ll1ll1_opy_ (u"ࠨ࡫ࡧࠫఐ"): bstack11ll1l1ll_opy_,
      bstack1ll1ll1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ఑"): datetime.datetime.strftime(datetime.datetime.now(), bstack1ll1ll1_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧఒ")),
      bstack1ll1ll1_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩఓ"): str(__version__)
    }
    try:
      bstack1ll111ll1_opy_ = {}
      if os.path.exists(bstack11ll1llll_opy_):
        bstack1ll111ll1_opy_ = json.load(open(bstack11ll1llll_opy_, bstack1ll1ll1_opy_ (u"ࠬࡸࡢࠨఔ")))
      bstack1ll111ll1_opy_[md5_hash] = bstack11l111l1ll_opy_
      with open(bstack11ll1llll_opy_, bstack1ll1ll1_opy_ (u"ࠨࡷࠬࠤక")) as outfile:
        json.dump(bstack1ll111ll1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡵࡱࡦࡤࡸ࡮ࡴࡧࠡࡏࡇ࠹ࠥ࡮ࡡࡴࡪࠣࡪ࡮ࡲࡥ࠻ࠢࡾࢁࠬఖ").format(str(e)))
    return
  bstack1l1l1l111_opy_ = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠨࢀࠪగ")), bstack1ll1ll1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩఘ"))
  if not os.path.exists(bstack1l1l1l111_opy_):
    os.makedirs(bstack1l1l1l111_opy_)
  bstack11ll1llll_opy_ = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠪࢂࠬఙ")), bstack1ll1ll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫచ"), bstack1ll1ll1_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ఛ"))
  lock_file = bstack11ll1llll_opy_ + bstack1ll1ll1_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬజ")
  bstack11l111l1ll_opy_ = {
    bstack1ll1ll1_opy_ (u"ࠧࡪࡦࠪఝ"): bstack11ll1l1ll_opy_,
    bstack1ll1ll1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫఞ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1ll1ll1_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ట")),
    bstack1ll1ll1_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨఠ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1ll111ll1_opy_ = {}
      if os.path.exists(bstack11ll1llll_opy_):
        with open(bstack11ll1llll_opy_, bstack1ll1ll1_opy_ (u"ࠫࡷ࠭డ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll111ll1_opy_ = json.loads(content)
      bstack1ll111ll1_opy_[md5_hash] = bstack11l111l1ll_opy_
      with open(bstack11ll1llll_opy_, bstack1ll1ll1_opy_ (u"ࠧࡽࠢఢ")) as outfile:
        json.dump(bstack1ll111ll1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡽࡩࡵࡪࠣࡪ࡮ࡲࡥࠡ࡮ࡲࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨࠡࡷࡳࡨࡦࡺࡥ࠻ࠢࡾࢁࠬణ").format(str(e)))
def bstack1ll1ll111l_opy_(self):
  return
def bstack11ll111111_opy_(self):
  return
def bstack1ll1lll1ll_opy_():
  global bstack1llll11ll1_opy_
  bstack1llll11ll1_opy_ = True
@measure(event_name=EVENTS.bstack111ll1l1ll_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack1l1llll1l_opy_(self):
  global bstack1l1ll1ll1l_opy_
  global bstack1l111l111_opy_
  global bstack1ll1ll1ll1_opy_
  try:
    if bstack1ll1ll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧత") in bstack1l1ll1ll1l_opy_ and self.session_id != None and bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬథ"), bstack1ll1ll1_opy_ (u"ࠩࠪద")) != bstack1ll1ll1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫధ"):
      bstack1l1lll11l1_opy_ = bstack1ll1ll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫన") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1ll1ll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ఩")
      if bstack1l1lll11l1_opy_ == bstack1ll1ll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ప"):
        bstack1l1111lll1_opy_(logger)
      if self != None:
        bstack11lll11ll1_opy_(self, bstack1l1lll11l1_opy_, bstack1ll1ll1_opy_ (u"ࠧ࠭ࠢࠪఫ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1ll1ll1_opy_ (u"ࠨࠩబ")
    if bstack1ll1ll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩభ") in bstack1l1ll1ll1l_opy_ and getattr(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩమ"), None):
      bstack1llll1l11_opy_.bstack1lll1ll1l_opy_(self, bstack1l11l1111_opy_, logger, wait=True)
    if bstack1ll1ll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫయ") in bstack1l1ll1ll1l_opy_:
      if not threading.currentThread().behave_test_status:
        bstack11lll11ll1_opy_(self, bstack1ll1ll1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧర"))
      bstack1l11l1llll_opy_.bstack1l1l1l11l_opy_(self)
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠢఱ") + str(e))
  bstack1ll1ll1ll1_opy_(self)
  self.session_id = None
def bstack11l1l1ll11_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack11ll1l1111_opy_
    global bstack1l1ll1ll1l_opy_
    command_executor = kwargs.get(bstack1ll1ll1_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠪల"), bstack1ll1ll1_opy_ (u"ࠨࠩళ"))
    bstack1111ll1l1l_opy_ = False
    if type(command_executor) == str and bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬఴ") in command_executor:
      bstack1111ll1l1l_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭వ") in str(getattr(command_executor, bstack1ll1ll1_opy_ (u"ࠫࡤࡻࡲ࡭ࠩశ"), bstack1ll1ll1_opy_ (u"ࠬ࠭ష"))):
      bstack1111ll1l1l_opy_ = True
    else:
      kwargs = bstack11111ll1_opy_.bstack1ll1l1lll1_opy_(bstack1lll1l11l1_opy_=kwargs, config=CONFIG)
      return bstack11ll1ll11l_opy_(self, *args, **kwargs)
    if bstack1111ll1l1l_opy_:
      bstack1ll1l1lll_opy_ = bstack1l1llll11l_opy_.bstack1l111l1111_opy_(CONFIG, bstack1l1ll1ll1l_opy_)
      if kwargs.get(bstack1ll1ll1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧస")):
        kwargs[bstack1ll1ll1_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨహ")] = bstack11ll1l1111_opy_(kwargs[bstack1ll1ll1_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ఺")], bstack1l1ll1ll1l_opy_, CONFIG, bstack1ll1l1lll_opy_)
      elif kwargs.get(bstack1ll1ll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ఻")):
        kwargs[bstack1ll1ll1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ఼ࠪ")] = bstack11ll1l1111_opy_(kwargs[bstack1ll1ll1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫఽ")], bstack1l1ll1ll1l_opy_, CONFIG, bstack1ll1l1lll_opy_)
  except Exception as e:
    logger.error(bstack1ll1ll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡧࡦࡶࡳ࠻ࠢࡾࢁࠧా").format(str(e)))
  return bstack11ll1ll11l_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1llllll1ll_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack11111llll_opy_(self, command_executor=bstack1ll1ll1_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵࠱࠳࠹࠱࠴࠳࠶࠮࠲࠼࠷࠸࠹࠺ࠢి"), *args, **kwargs):
  global bstack1l111l111_opy_
  global bstack1l1l1l1ll1_opy_
  bstack1lll1111ll_opy_ = bstack11l1l1ll11_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1l1l11l1_opy_.on():
    return bstack1lll1111ll_opy_
  try:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡄࡱࡰࡱࡦࡴࡤࠡࡇࡻࡩࡨࡻࡴࡰࡴࠣࡻ࡭࡫࡮ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡧࡣ࡯ࡷࡪࠦ࠭ࠡࡽࢀࠫీ").format(str(command_executor)))
    logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡊࡸࡦ࡛ࠥࡒࡍࠢ࡬ࡷࠥ࠳ࠠࡼࡿࠪు").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬూ") in command_executor._url:
      bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫృ"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧౄ") in command_executor):
    bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭౅"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack11l1llllll_opy_ = getattr(threading.current_thread(), bstack1ll1ll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧె"), None)
  bstack11l11l1l1_opy_ = {}
  if self.capabilities is not None:
    bstack11l11l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭ే")] = self.capabilities.get(bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ై"))
    bstack11l11l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ౉")] = self.capabilities.get(bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫొ"))
    bstack11l11l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡣࡴࡶࡴࡪࡱࡱࡷࠬో")] = self.capabilities.get(bstack1ll1ll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪౌ"))
  if CONFIG.get(bstack1ll1ll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ్࠭"), False) and bstack11111ll1_opy_.bstack111l1l1l1l_opy_(bstack11l11l1l1_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack1ll1ll1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ౎") in bstack1l1ll1ll1l_opy_ or bstack1ll1ll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ౏") in bstack1l1ll1ll1l_opy_:
    bstack1ll111ll_opy_.bstack111l111l11_opy_(self)
  if bstack1ll1ll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ౐") in bstack1l1ll1ll1l_opy_ and bstack11l1llllll_opy_ and bstack11l1llllll_opy_.get(bstack1ll1ll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ౑"), bstack1ll1ll1_opy_ (u"ࠫࠬ౒")) == bstack1ll1ll1_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭౓"):
    bstack1ll111ll_opy_.bstack111l111l11_opy_(self)
  bstack1l111l111_opy_ = self.session_id
  with bstack11lll11l1l_opy_:
    bstack1l1l1l1ll1_opy_.append(self)
  return bstack1lll1111ll_opy_
def bstack1ll1ll1l1_opy_(args):
  return bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠧ౔") in str(args)
def bstack1l11ll1l11_opy_(self, driver_command, *args, **kwargs):
  global bstack11ll11llll_opy_
  global bstack111l11ll1_opy_
  bstack1111l11l11_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷౕࠫ"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳౖࠧ"), None)
  bstack1l11llll11_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ౗"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬౘ"), None)
  bstack1l111ll11l_opy_ = getattr(self, bstack1ll1ll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫౙ"), None) != None and getattr(self, bstack1ll1ll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬౚ"), None) == True
  if not bstack111l11ll1_opy_ and bstack1ll1ll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭౛") in CONFIG and CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ౜")] == True and bstack111llll111_opy_.bstack1l11111l1l_opy_(driver_command) and (bstack1l111ll11l_opy_ or bstack1111l11l11_opy_ or bstack1l11llll11_opy_) and not bstack1ll1ll1l1_opy_(args):
    try:
      bstack111l11ll1_opy_ = True
      logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡼࡿࠪౝ").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1ll1ll1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡥࡳࡨࡲࡶࡲࠦࡳࡤࡣࡱࠤࢀࢃࠧ౞").format(str(err)))
    bstack111l11ll1_opy_ = False
  response = bstack11ll11llll_opy_(self, driver_command, *args, **kwargs)
  if (bstack1ll1ll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ౟") in str(bstack1l1ll1ll1l_opy_).lower() or bstack1ll1ll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫౠ") in str(bstack1l1ll1ll1l_opy_).lower()) and bstack1l1l11l1_opy_.on():
    try:
      if driver_command == bstack1ll1ll1_opy_ (u"ࠬࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩౡ"):
        bstack1ll111ll_opy_.bstack1lllll1ll1_opy_({
            bstack1ll1ll1_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬౢ"): response[bstack1ll1ll1_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭ౣ")],
            bstack1ll1ll1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ౤"): bstack1ll111ll_opy_.current_test_uuid() if bstack1ll111ll_opy_.current_test_uuid() else bstack1l1l11l1_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1l111l1l11_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack1l1111l11_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1l111l111_opy_
  global bstack1ll11l111_opy_
  global bstack1l1ll11l1l_opy_
  global bstack1l1111111_opy_
  global bstack11l1111ll_opy_
  global bstack1l1ll1ll1l_opy_
  global bstack11ll1ll11l_opy_
  global bstack1l1l1l1ll1_opy_
  global bstack1l1ll1l11_opy_
  global bstack1l11l1111_opy_
  if os.getenv(bstack1ll1ll1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ౥")) is not None and bstack11111ll1_opy_.bstack1ll111ll1l_opy_(CONFIG) is None:
    CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ౦")] = True
  CONFIG[bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭౧")] = str(bstack1l1ll1ll1l_opy_) + str(__version__)
  bstack1l11lllll_opy_ = os.environ[bstack1ll1ll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ౨")]
  bstack1ll1l1lll_opy_ = bstack1l1llll11l_opy_.bstack1l111l1111_opy_(CONFIG, bstack1l1ll1ll1l_opy_)
  CONFIG[bstack1ll1ll1_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩ౩")] = bstack1l11lllll_opy_
  CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ౪")] = bstack1ll1l1lll_opy_
  if CONFIG.get(bstack1ll1ll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ౫"),bstack1ll1ll1_opy_ (u"ࠩࠪ౬")) and bstack1ll1ll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ౭") in bstack1l1ll1ll1l_opy_:
    CONFIG[bstack1ll1ll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ౮")].pop(bstack1ll1ll1_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ౯"), None)
    CONFIG[bstack1ll1ll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭౰")].pop(bstack1ll1ll1_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ౱"), None)
  command_executor = bstack111ll1lll_opy_()
  logger.debug(bstack11111l1l1_opy_.format(command_executor))
  proxy = bstack1lll1l1111_opy_(CONFIG, proxy)
  bstack1l1lll111l_opy_ = 0 if bstack1ll11l111_opy_ < 0 else bstack1ll11l111_opy_
  try:
    if bstack1l1111111_opy_ is True:
      bstack1l1lll111l_opy_ = int(multiprocessing.current_process().name)
    elif bstack11l1111ll_opy_ is True:
      bstack1l1lll111l_opy_ = int(threading.current_thread().name)
  except:
    bstack1l1lll111l_opy_ = 0
  bstack1lll11l1l_opy_ = bstack111111l11_opy_(CONFIG, bstack1l1lll111l_opy_)
  logger.debug(bstack111llllll1_opy_.format(str(bstack1lll11l1l_opy_)))
  if bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ౲") in CONFIG and bstack1ll1l1llll_opy_(CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭౳")]):
    bstack1lll11lll1_opy_(bstack1lll11l1l_opy_)
  if bstack11111ll1_opy_.bstack1ll1lll111_opy_(CONFIG, bstack1l1lll111l_opy_) and bstack11111ll1_opy_.bstack1lll1ll111_opy_(bstack1lll11l1l_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack11111ll1_opy_.set_capabilities(bstack1lll11l1l_opy_, CONFIG)
  if desired_capabilities:
    bstack11ll1111ll_opy_ = bstack11lll1lll_opy_(desired_capabilities)
    bstack11ll1111ll_opy_[bstack1ll1ll1_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪ౴")] = bstack11l11llll_opy_(CONFIG)
    bstack1lllll1l1l_opy_ = bstack111111l11_opy_(bstack11ll1111ll_opy_)
    if bstack1lllll1l1l_opy_:
      bstack1lll11l1l_opy_ = update(bstack1lllll1l1l_opy_, bstack1lll11l1l_opy_)
    desired_capabilities = None
  if options:
    bstack1lll11llll_opy_(options, bstack1lll11l1l_opy_)
  if not options:
    options = bstack1l1l1l1l1l_opy_(bstack1lll11l1l_opy_)
  bstack1l11l1111_opy_ = CONFIG.get(bstack1ll1ll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ౵"))[bstack1l1lll111l_opy_]
  if proxy and bstack11lll11l1_opy_() >= version.parse(bstack1ll1ll1_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬ౶")):
    options.proxy(proxy)
  if options and bstack11lll11l1_opy_() >= version.parse(bstack1ll1ll1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ౷")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack11lll11l1_opy_() < version.parse(bstack1ll1ll1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭౸")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1lll11l1l_opy_)
  logger.info(bstack1lll1l11ll_opy_)
  bstack111l11l1ll_opy_.end(EVENTS.bstack111l1l1111_opy_.value, EVENTS.bstack111l1l1111_opy_.value + bstack1ll1ll1_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ౹"), EVENTS.bstack111l1l1111_opy_.value + bstack1ll1ll1_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ౺"), status=True, failure=None, test_name=bstack1l1ll11l1l_opy_)
  if bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡵࡸ࡯ࡧ࡫࡯ࡩࠬ౻") in kwargs:
    del kwargs[bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡶࡲࡰࡨ࡬ࡰࡪ࠭౼")]
  try:
    if bstack11lll11l1_opy_() >= version.parse(bstack1ll1ll1_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬ౽")):
      bstack11ll1ll11l_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack11lll11l1_opy_() >= version.parse(bstack1ll1ll1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ౾")):
      bstack11ll1ll11l_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11lll11l1_opy_() >= version.parse(bstack1ll1ll1_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧ౿")):
      bstack11ll1ll11l_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack11ll1ll11l_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack11111l1ll_opy_:
    logger.error(bstack11ll1l111l_opy_.format(bstack1ll1ll1_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠧಀ"), str(bstack11111l1ll_opy_)))
    raise bstack11111l1ll_opy_
  if bstack11111ll1_opy_.bstack1ll1lll111_opy_(CONFIG, bstack1l1lll111l_opy_) and bstack11111ll1_opy_.bstack1lll1ll111_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫಁ")][bstack1ll1ll1_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩಂ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack11111ll1_opy_.set_capabilities(bstack1lll11l1l_opy_, CONFIG)
  try:
    bstack1ll11111l1_opy_ = bstack1ll1ll1_opy_ (u"ࠫࠬಃ")
    if bstack11lll11l1_opy_() >= version.parse(bstack1ll1ll1_opy_ (u"ࠬ࠺࠮࠱࠰࠳ࡦ࠶࠭಄")):
      if self.caps is not None:
        bstack1ll11111l1_opy_ = self.caps.get(bstack1ll1ll1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨಅ"))
    else:
      if self.capabilities is not None:
        bstack1ll11111l1_opy_ = self.capabilities.get(bstack1ll1ll1_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢಆ"))
    if bstack1ll11111l1_opy_:
      bstack1l1l111l1_opy_(bstack1ll11111l1_opy_)
      if bstack11lll11l1_opy_() <= version.parse(bstack1ll1ll1_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨಇ")):
        self.command_executor._url = bstack1ll1ll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥಈ") + bstack11111l1l1l_opy_ + bstack1ll1ll1_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢಉ")
      else:
        self.command_executor._url = bstack1ll1ll1_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨಊ") + bstack1ll11111l1_opy_ + bstack1ll1ll1_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨಋ")
      logger.debug(bstack11ll11ll11_opy_.format(bstack1ll11111l1_opy_))
    else:
      logger.debug(bstack1lll11ll1l_opy_.format(bstack1ll1ll1_opy_ (u"ࠨࡏࡱࡶ࡬ࡱࡦࡲࠠࡉࡷࡥࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢಌ")))
  except Exception as e:
    logger.debug(bstack1lll11ll1l_opy_.format(e))
  if bstack1ll1ll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭಍") in bstack1l1ll1ll1l_opy_:
    bstack111ll11l1_opy_(bstack1ll11l111_opy_, bstack1l1ll1l11_opy_)
  bstack1l111l111_opy_ = self.session_id
  if bstack1ll1ll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨಎ") in bstack1l1ll1ll1l_opy_ or bstack1ll1ll1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩಏ") in bstack1l1ll1ll1l_opy_ or bstack1ll1ll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩಐ") in bstack1l1ll1ll1l_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack11l1llllll_opy_ = getattr(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥࠬ಑"), None)
  if bstack1ll1ll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬಒ") in bstack1l1ll1ll1l_opy_ or bstack1ll1ll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಓ") in bstack1l1ll1ll1l_opy_:
    bstack1ll111ll_opy_.bstack111l111l11_opy_(self)
  if bstack1ll1ll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧಔ") in bstack1l1ll1ll1l_opy_ and bstack11l1llllll_opy_ and bstack11l1llllll_opy_.get(bstack1ll1ll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨಕ"), bstack1ll1ll1_opy_ (u"ࠩࠪಖ")) == bstack1ll1ll1_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫಗ"):
    bstack1ll111ll_opy_.bstack111l111l11_opy_(self)
  with bstack11lll11l1l_opy_:
    bstack1l1l1l1ll1_opy_.append(self)
  if bstack1ll1ll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧಘ") in CONFIG and bstack1ll1ll1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪಙ") in CONFIG[bstack1ll1ll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಚ")][bstack1l1lll111l_opy_]:
    bstack1l1ll11l1l_opy_ = CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಛ")][bstack1l1lll111l_opy_][bstack1ll1ll1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ಜ")]
  logger.debug(bstack1ll11ll11l_opy_.format(bstack1l111l111_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1111l1ll1l_opy_
    def bstack11lllll11_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1llll1l11l_opy_
      if(bstack1ll1ll1_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸ࠯࡬ࡶࠦಝ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠪࢂࠬಞ")), bstack1ll1ll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫಟ"), bstack1ll1ll1_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧಠ")), bstack1ll1ll1_opy_ (u"࠭ࡷࠨಡ")) as fp:
          fp.write(bstack1ll1ll1_opy_ (u"ࠢࠣಢ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1ll1ll1_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥಣ")))):
          with open(args[1], bstack1ll1ll1_opy_ (u"ࠩࡵࠫತ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1ll1ll1_opy_ (u"ࠪࡥࡸࡿ࡮ࡤࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡤࡴࡥࡸࡒࡤ࡫ࡪ࠮ࡣࡰࡰࡷࡩࡽࡺࠬࠡࡲࡤ࡫ࡪࠦ࠽ࠡࡸࡲ࡭ࡩࠦ࠰ࠪࠩಥ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack11l1111l1l_opy_)
            if bstack1ll1ll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨದ") in CONFIG and str(CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩಧ")]).lower() != bstack1ll1ll1_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬನ"):
                bstack1lll1l111_opy_ = bstack1111l1ll1l_opy_()
                bstack1l11l1ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠧࠨࠩࠍ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࠐࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹࡝࠼ࠌࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠ࠿ࠏࡩ࡯࡯ࡵࡷࠤࡵࡥࡩ࡯ࡦࡨࡼࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠳࡟࠾ࠎࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡸࡲࡩࡤࡧࠫ࠴࠱ࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴ࠫ࠾ࠎࡨࡵ࡮ࡴࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫ࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤࠬ࠿ࠏ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡲࡡࡶࡰࡦ࡬ࠥࡃࠠࡢࡵࡼࡲࡨࠦࠨ࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠩࠡ࠿ࡁࠤࢀࢁࠊࠡࠢ࡯ࡩࡹࠦࡣࡢࡲࡶ࠿ࠏࠦࠠࡵࡴࡼࠤࢀࢁࠊࠡࠢࠣࠤࡨࡧࡰࡴࠢࡀࠤࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸ࠯࠻ࠋࠢࠣࢁࢂࠦࡣࡢࡶࡦ࡬ࠥ࠮ࡥࡹࠫࠣࡿࢀࠐࠠࠡࠢࠣࡧࡴࡴࡳࡰ࡮ࡨ࠲ࡪࡸࡲࡰࡴࠫࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠿ࠨࠬࠡࡧࡻ࠭ࡀࠐࠠࠡࡿࢀࠎࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻࡼࠌࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࠬࢁࡣࡥࡲࡘࡶࡱࢃࠧࠡ࠭ࠣࡩࡳࡩ࡯ࡥࡧࡘࡖࡎࡉ࡯࡮ࡲࡲࡲࡪࡴࡴࠩࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡦࡥࡵࡹࠩࠪ࠮ࠍࠤࠥࠦࠠ࠯࠰࠱ࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵࠍࠤࠥࢃࡽࠪ࠽ࠍࢁࢂࡁࠊ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠍࠫࠬ࠭಩").format(bstack1lll1l111_opy_=bstack1lll1l111_opy_)
            lines.insert(1, bstack1l11l1ll1_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1ll1ll1_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥಪ")), bstack1ll1ll1_opy_ (u"ࠩࡺࠫಫ")) as bstack1ll1lll1l1_opy_:
              bstack1ll1lll1l1_opy_.writelines(lines)
        CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬಬ")] = str(bstack1l1ll1ll1l_opy_) + str(__version__)
        bstack1l11lllll_opy_ = os.environ[bstack1ll1ll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩಭ")]
        bstack1ll1l1lll_opy_ = bstack1l1llll11l_opy_.bstack1l111l1111_opy_(CONFIG, bstack1l1ll1ll1l_opy_)
        CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨಮ")] = bstack1l11lllll_opy_
        CONFIG[bstack1ll1ll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨಯ")] = bstack1ll1l1lll_opy_
        bstack1l1lll111l_opy_ = 0 if bstack1ll11l111_opy_ < 0 else bstack1ll11l111_opy_
        try:
          if bstack1l1111111_opy_ is True:
            bstack1l1lll111l_opy_ = int(multiprocessing.current_process().name)
          elif bstack11l1111ll_opy_ is True:
            bstack1l1lll111l_opy_ = int(threading.current_thread().name)
        except:
          bstack1l1lll111l_opy_ = 0
        CONFIG[bstack1ll1ll1_opy_ (u"ࠢࡶࡵࡨ࡛࠸ࡉࠢರ")] = False
        CONFIG[bstack1ll1ll1_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢಱ")] = True
        bstack1lll11l1l_opy_ = bstack111111l11_opy_(CONFIG, bstack1l1lll111l_opy_)
        logger.debug(bstack111llllll1_opy_.format(str(bstack1lll11l1l_opy_)))
        if CONFIG.get(bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ಲ")):
          bstack1lll11lll1_opy_(bstack1lll11l1l_opy_)
        if bstack1ll1ll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಳ") in CONFIG and bstack1ll1ll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ಴") in CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨವ")][bstack1l1lll111l_opy_]:
          bstack1l1ll11l1l_opy_ = CONFIG[bstack1ll1ll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಶ")][bstack1l1lll111l_opy_][bstack1ll1ll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬಷ")]
        args.append(os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠨࢀࠪಸ")), bstack1ll1ll1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩಹ"), bstack1ll1ll1_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬ಺")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1lll11l1l_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1ll1ll1_opy_ (u"ࠦ࡮ࡴࡤࡦࡺࡢࡦࡸࡺࡡࡤ࡭࠱࡮ࡸࠨ಻"))
      bstack1llll1l11l_opy_ = True
      return bstack1111ll1l1_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack1111l111l_opy_(self,
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
    global bstack1ll11l111_opy_
    global bstack1l1ll11l1l_opy_
    global bstack1l1111111_opy_
    global bstack11l1111ll_opy_
    global bstack1l1ll1ll1l_opy_
    CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑ಼ࠧ")] = str(bstack1l1ll1ll1l_opy_) + str(__version__)
    bstack1l11lllll_opy_ = os.environ[bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫಽ")]
    bstack1ll1l1lll_opy_ = bstack1l1llll11l_opy_.bstack1l111l1111_opy_(CONFIG, bstack1l1ll1ll1l_opy_)
    CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪಾ")] = bstack1l11lllll_opy_
    CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪಿ")] = bstack1ll1l1lll_opy_
    bstack1l1lll111l_opy_ = 0 if bstack1ll11l111_opy_ < 0 else bstack1ll11l111_opy_
    try:
      if bstack1l1111111_opy_ is True:
        bstack1l1lll111l_opy_ = int(multiprocessing.current_process().name)
      elif bstack11l1111ll_opy_ is True:
        bstack1l1lll111l_opy_ = int(threading.current_thread().name)
    except:
      bstack1l1lll111l_opy_ = 0
    CONFIG[bstack1ll1ll1_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣೀ")] = True
    bstack1lll11l1l_opy_ = bstack111111l11_opy_(CONFIG, bstack1l1lll111l_opy_)
    logger.debug(bstack111llllll1_opy_.format(str(bstack1lll11l1l_opy_)))
    if CONFIG.get(bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧು")):
      bstack1lll11lll1_opy_(bstack1lll11l1l_opy_)
    if bstack1ll1ll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧೂ") in CONFIG and bstack1ll1ll1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪೃ") in CONFIG[bstack1ll1ll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩೄ")][bstack1l1lll111l_opy_]:
      bstack1l1ll11l1l_opy_ = CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ೅")][bstack1l1lll111l_opy_][bstack1ll1ll1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ೆ")]
    import urllib
    import json
    if bstack1ll1ll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ೇ") in CONFIG and str(CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧೈ")]).lower() != bstack1ll1ll1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ೉"):
        bstack1l11l1lll_opy_ = bstack1111l1ll1l_opy_()
        bstack1lll1l111_opy_ = bstack1l11l1lll_opy_ + urllib.parse.quote(json.dumps(bstack1lll11l1l_opy_))
    else:
        bstack1lll1l111_opy_ = bstack1ll1ll1_opy_ (u"ࠬࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠧೊ") + urllib.parse.quote(json.dumps(bstack1lll11l1l_opy_))
    browser = self.connect(bstack1lll1l111_opy_)
    return browser
except Exception as e:
    pass
def bstack1llll1llll_opy_():
    global bstack1llll1l11l_opy_
    global bstack1l1ll1ll1l_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1l11l11l1l_opy_
        global bstack11111l11_opy_
        if not bstack111l1ll1ll_opy_:
          global bstack1l1ll111l1_opy_
          if not bstack1l1ll111l1_opy_:
            from bstack_utils.helper import bstack11111l1lll_opy_, bstack1l1l111ll_opy_, bstack1l1ll11l11_opy_
            bstack1l1ll111l1_opy_ = bstack11111l1lll_opy_()
            bstack1l1l111ll_opy_(bstack1l1ll1ll1l_opy_)
            bstack1ll1l1lll_opy_ = bstack1l1llll11l_opy_.bstack1l111l1111_opy_(CONFIG, bstack1l1ll1ll1l_opy_)
            bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠨࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡔࡗࡕࡄࡖࡅࡗࡣࡒࡇࡐࠣೋ"), bstack1ll1l1lll_opy_)
          BrowserType.connect = bstack1l11l11l1l_opy_
          return
        BrowserType.launch = bstack1111l111l_opy_
        bstack1llll1l11l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack11lllll11_opy_
      bstack1llll1l11l_opy_ = True
    except Exception as e:
      pass
def bstack1l1l11l1ll_opy_(context, bstack1l1lll11l_opy_):
  try:
    context.page.evaluate(bstack1ll1ll1_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣೌ"), bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾್ࠬ")+ json.dumps(bstack1l1lll11l_opy_) + bstack1ll1ll1_opy_ (u"ࠤࢀࢁࠧ೎"))
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥࢁࡽ࠻ࠢࡾࢁࠧ೏").format(str(e), traceback.format_exc()))
def bstack11l1l1l111_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1ll1ll1_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧ೐"), bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ೑") + json.dumps(message) + bstack1ll1ll1_opy_ (u"࠭ࠬࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠩ೒") + json.dumps(level) + bstack1ll1ll1_opy_ (u"ࠧࡾࡿࠪ೓"))
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡦࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠡࡽࢀ࠾ࠥࢁࡽࠣ೔").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1lllll11ll_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack11ll1ll11_opy_(self, url):
  global bstack1l11ll1111_opy_
  try:
    bstack1l11ll1lll_opy_(url)
  except Exception as err:
    logger.debug(bstack1l1111ll1_opy_.format(str(err)))
  try:
    bstack1l11ll1111_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1111lll11_opy_):
        bstack1l11ll1lll_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1l1111ll1_opy_.format(str(err)))
    raise e
def bstack1l1l11lll1_opy_(self):
  global bstack11ll1ll1l_opy_
  bstack11ll1ll1l_opy_ = self
  return
def bstack1l11lll11l_opy_(self):
  global bstack11111ll1l1_opy_
  bstack11111ll1l1_opy_ = self
  return
def bstack1111lll1l1_opy_(test_name, bstack11lll1l11_opy_):
  global CONFIG
  if percy.bstack1l111111l1_opy_() == bstack1ll1ll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢೕ"):
    bstack1l1l1l11ll_opy_ = os.path.relpath(bstack11lll1l11_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1l1l1l11ll_opy_)
    bstack1l1lllll11_opy_ = suite_name + bstack1ll1ll1_opy_ (u"ࠥ࠱ࠧೖ") + test_name
    threading.current_thread().percySessionName = bstack1l1lllll11_opy_
def bstack11ll1l1l1l_opy_(self, test, *args, **kwargs):
  global bstack111ll111l_opy_
  test_name = None
  bstack11lll1l11_opy_ = None
  if test:
    test_name = str(test.name)
    bstack11lll1l11_opy_ = str(test.source)
  bstack1111lll1l1_opy_(test_name, bstack11lll1l11_opy_)
  bstack111ll111l_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l111ll1l1_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack1l11l111ll_opy_(driver, bstack1l1lllll11_opy_):
  if not bstack1lll1llll1_opy_ and bstack1l1lllll11_opy_:
      bstack1l1ll1llll_opy_ = {
          bstack1ll1ll1_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫ೗"): bstack1ll1ll1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭೘"),
          bstack1ll1ll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ೙"): {
              bstack1ll1ll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ೚"): bstack1l1lllll11_opy_
          }
      }
      bstack1l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭೛").format(json.dumps(bstack1l1ll1llll_opy_))
      driver.execute_script(bstack1l1lll1l1_opy_)
  if bstack11lll1ll11_opy_:
      bstack111l1lll1_opy_ = {
          bstack1ll1ll1_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ೜"): bstack1ll1ll1_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬೝ"),
          bstack1ll1ll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧೞ"): {
              bstack1ll1ll1_opy_ (u"ࠬࡪࡡࡵࡣࠪ೟"): bstack1l1lllll11_opy_ + bstack1ll1ll1_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨೠ"),
              bstack1ll1ll1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ೡ"): bstack1ll1ll1_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ೢ")
          }
      }
      if bstack11lll1ll11_opy_.status == bstack1ll1ll1_opy_ (u"ࠩࡓࡅࡘ࡙ࠧೣ"):
          bstack111l11l1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨ೤").format(json.dumps(bstack111l1lll1_opy_))
          driver.execute_script(bstack111l11l1l1_opy_)
          bstack11lll11ll1_opy_(driver, bstack1ll1ll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ೥"))
      elif bstack11lll1ll11_opy_.status == bstack1ll1ll1_opy_ (u"ࠬࡌࡁࡊࡎࠪ೦"):
          reason = bstack1ll1ll1_opy_ (u"ࠨࠢ೧")
          bstack1l111l1lll_opy_ = bstack1l1lllll11_opy_ + bstack1ll1ll1_opy_ (u"ࠧࠡࡨࡤ࡭ࡱ࡫ࡤࠨ೨")
          if bstack11lll1ll11_opy_.message:
              reason = str(bstack11lll1ll11_opy_.message)
              bstack1l111l1lll_opy_ = bstack1l111l1lll_opy_ + bstack1ll1ll1_opy_ (u"ࠨࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࠨ೩") + reason
          bstack111l1lll1_opy_[bstack1ll1ll1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ೪")] = {
              bstack1ll1ll1_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ೫"): bstack1ll1ll1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ೬"),
              bstack1ll1ll1_opy_ (u"ࠬࡪࡡࡵࡣࠪ೭"): bstack1l111l1lll_opy_
          }
          bstack111l11l1l1_opy_ = bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ೮").format(json.dumps(bstack111l1lll1_opy_))
          driver.execute_script(bstack111l11l1l1_opy_)
          bstack11lll11ll1_opy_(driver, bstack1ll1ll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ೯"), reason)
          bstack1ll11l11ll_opy_(reason, str(bstack11lll1ll11_opy_), str(bstack1ll11l111_opy_), logger)
@measure(event_name=EVENTS.bstack11lllll1ll_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack1ll11l111l_opy_(driver, test):
  if percy.bstack1l111111l1_opy_() == bstack1ll1ll1_opy_ (u"ࠣࡶࡵࡹࡪࠨ೰") and percy.bstack1l1l111lll_opy_() == bstack1ll1ll1_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦೱ"):
      bstack1l111lll1l_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ೲ"), None)
      bstack1l11lllll1_opy_(driver, bstack1l111lll1l_opy_, test)
  if (bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨೳ"), None) and
      bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ೴"), None)) or (
      bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭೵"), None) and
      bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ೶"), None)):
      logger.info(bstack1ll1ll1_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠦࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡ࡫ࡶࠤࡺࡴࡤࡦࡴࡺࡥࡾ࠴ࠠࠣ೷"))
      bstack11111ll1_opy_.bstack111l111l_opy_(driver, name=test.name, path=test.source)
def bstack1l1llll111_opy_(test, bstack1l1lllll11_opy_):
    try:
      bstack111lllll1_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack1ll1ll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ೸")] = bstack1l1lllll11_opy_
      if bstack11lll1ll11_opy_:
        if bstack11lll1ll11_opy_.status == bstack1ll1ll1_opy_ (u"ࠪࡔࡆ࡙ࡓࠨ೹"):
          data[bstack1ll1ll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ೺")] = bstack1ll1ll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ೻")
        elif bstack11lll1ll11_opy_.status == bstack1ll1ll1_opy_ (u"࠭ࡆࡂࡋࡏࠫ೼"):
          data[bstack1ll1ll1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ೽")] = bstack1ll1ll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ೾")
          if bstack11lll1ll11_opy_.message:
            data[bstack1ll1ll1_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩ೿")] = str(bstack11lll1ll11_opy_.message)
      user = CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬഀ")]
      key = CONFIG[bstack1ll1ll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧഁ")]
      host = bstack11l1l1l11_opy_(cli.config, [bstack1ll1ll1_opy_ (u"ࠧࡧࡰࡪࡵࠥം"), bstack1ll1ll1_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥࠣഃ"), bstack1ll1ll1_opy_ (u"ࠢࡢࡲ࡬ࠦഄ")], bstack1ll1ll1_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠤഅ"))
      url = bstack1ll1ll1_opy_ (u"ࠩࡾࢁ࠴ࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡴࡧࡶࡷ࡮ࡵ࡮ࡴ࠱ࡾࢁ࠳ࡰࡳࡰࡰࠪആ").format(host, bstack1l111l111_opy_)
      headers = {
        bstack1ll1ll1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩഇ"): bstack1ll1ll1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧഈ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽ࡹࡵࡪࡡࡵࡧࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠤഉ"), datetime.datetime.now() - bstack111lllll1_opy_)
    except Exception as e:
      logger.error(bstack1lll111l1_opy_.format(str(e)))
def bstack1ll1l111l1_opy_(test, bstack1l1lllll11_opy_):
  global CONFIG
  global bstack11111ll1l1_opy_
  global bstack11ll1ll1l_opy_
  global bstack1l111l111_opy_
  global bstack11lll1ll11_opy_
  global bstack1l1ll11l1l_opy_
  global bstack111l111l1l_opy_
  global bstack1l11lll11_opy_
  global bstack111l11l1l_opy_
  global bstack111l11l11l_opy_
  global bstack1l1l1l1ll1_opy_
  global bstack1l11l1111_opy_
  global bstack1l1ll1lll_opy_
  try:
    if not bstack1l111l111_opy_:
      with bstack1l1ll1lll_opy_:
        bstack111lll111_opy_ = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"࠭ࡾࠨഊ")), bstack1ll1ll1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧഋ"), bstack1ll1ll1_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪഌ"))
        if os.path.exists(bstack111lll111_opy_):
          with open(bstack111lll111_opy_, bstack1ll1ll1_opy_ (u"ࠩࡵࠫ഍")) as f:
            content = f.read().strip()
            if content:
              bstack1lll111l11_opy_ = json.loads(bstack1ll1ll1_opy_ (u"ࠥࡿࠧഎ") + content + bstack1ll1ll1_opy_ (u"ࠫࠧࡾࠢ࠻ࠢࠥࡽࠧ࠭ഏ") + bstack1ll1ll1_opy_ (u"ࠧࢃࠢഐ"))
              bstack1l111l111_opy_ = bstack1lll111l11_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࡶࠤ࡫࡯࡬ࡦ࠼ࠣࠫ഑") + str(e))
  if bstack1l1l1l1ll1_opy_:
    with bstack11lll11l1l_opy_:
      bstack1lllllll1l_opy_ = bstack1l1l1l1ll1_opy_.copy()
    for driver in bstack1lllllll1l_opy_:
      if bstack1l111l111_opy_ == driver.session_id:
        if test:
          bstack1ll11l111l_opy_(driver, test)
        bstack1l11l111ll_opy_(driver, bstack1l1lllll11_opy_)
  elif bstack1l111l111_opy_:
    bstack1l1llll111_opy_(test, bstack1l1lllll11_opy_)
  if bstack11111ll1l1_opy_:
    bstack1l11lll11_opy_(bstack11111ll1l1_opy_)
  if bstack11ll1ll1l_opy_:
    bstack111l11l1l_opy_(bstack11ll1ll1l_opy_)
  if bstack1llll11ll1_opy_:
    bstack111l11l11l_opy_()
def bstack1ll1l11ll1_opy_(self, test, *args, **kwargs):
  bstack1l1lllll11_opy_ = None
  if test:
    bstack1l1lllll11_opy_ = str(test.name)
  bstack1ll1l111l1_opy_(test, bstack1l1lllll11_opy_)
  bstack111l111l1l_opy_(self, test, *args, **kwargs)
def bstack11l1111111_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11l111ll1_opy_
  global CONFIG
  global bstack1l1l1l1ll1_opy_
  global bstack1l111l111_opy_
  global bstack1l1ll1lll_opy_
  bstack111ll1ll1_opy_ = None
  try:
    if bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ഒ"), None) or bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪഓ"), None):
      try:
        if not bstack1l111l111_opy_:
          bstack111lll111_opy_ = os.path.join(os.path.expanduser(bstack1ll1ll1_opy_ (u"ࠩࢁࠫഔ")), bstack1ll1ll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪക"), bstack1ll1ll1_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭ഖ"))
          with bstack1l1ll1lll_opy_:
            if os.path.exists(bstack111lll111_opy_):
              with open(bstack111lll111_opy_, bstack1ll1ll1_opy_ (u"ࠬࡸࠧഗ")) as f:
                content = f.read().strip()
                if content:
                  bstack1lll111l11_opy_ = json.loads(bstack1ll1ll1_opy_ (u"ࠨࡻࠣഘ") + content + bstack1ll1ll1_opy_ (u"ࠧࠣࡺࠥ࠾ࠥࠨࡹࠣࠩങ") + bstack1ll1ll1_opy_ (u"ࠣࡿࠥച"))
                  bstack1l111l111_opy_ = bstack1lll111l11_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡍࡉࡹࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡶࡨࡷࡹࠦࡳࡵࡣࡷࡹࡸࡀࠠࠨഛ") + str(e))
      if bstack1l1l1l1ll1_opy_:
        with bstack11lll11l1l_opy_:
          bstack1lllllll1l_opy_ = bstack1l1l1l1ll1_opy_.copy()
        for driver in bstack1lllllll1l_opy_:
          if bstack1l111l111_opy_ == driver.session_id:
            bstack111ll1ll1_opy_ = driver
    bstack111ll1llll_opy_ = bstack11111ll1_opy_.bstack111llllll_opy_(test.tags)
    if bstack111ll1ll1_opy_:
      threading.current_thread().isA11yTest = bstack11111ll1_opy_.bstack111ll1ll1l_opy_(bstack111ll1ll1_opy_, bstack111ll1llll_opy_)
      threading.current_thread().isAppA11yTest = bstack11111ll1_opy_.bstack111ll1ll1l_opy_(bstack111ll1ll1_opy_, bstack111ll1llll_opy_)
    else:
      threading.current_thread().isA11yTest = bstack111ll1llll_opy_
      threading.current_thread().isAppA11yTest = bstack111ll1llll_opy_
  except:
    pass
  bstack11l111ll1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack11lll1ll11_opy_
  try:
    bstack11lll1ll11_opy_ = self._test
  except:
    bstack11lll1ll11_opy_ = self.test
def bstack1111l11l1l_opy_():
  global bstack111l1llll_opy_
  try:
    if os.path.exists(bstack111l1llll_opy_):
      os.remove(bstack111l1llll_opy_)
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ജ") + str(e))
def bstack11l1l1l11l_opy_():
  global bstack111l1llll_opy_
  bstack1ll111l11_opy_ = {}
  lock_file = bstack111l1llll_opy_ + bstack1ll1ll1_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪഝ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨഞ"))
    try:
      if not os.path.isfile(bstack111l1llll_opy_):
        with open(bstack111l1llll_opy_, bstack1ll1ll1_opy_ (u"࠭ࡷࠨട")) as f:
          json.dump({}, f)
      if os.path.exists(bstack111l1llll_opy_):
        with open(bstack111l1llll_opy_, bstack1ll1ll1_opy_ (u"ࠧࡳࠩഠ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll111l11_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪࡧࡤࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪഡ") + str(e))
    return bstack1ll111l11_opy_
  try:
    os.makedirs(os.path.dirname(bstack111l1llll_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack111l1llll_opy_):
        with open(bstack111l1llll_opy_, bstack1ll1ll1_opy_ (u"ࠩࡺࠫഢ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack111l1llll_opy_):
        with open(bstack111l1llll_opy_, bstack1ll1ll1_opy_ (u"ࠪࡶࠬണ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll111l11_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ത") + str(e))
  finally:
    return bstack1ll111l11_opy_
def bstack111ll11l1_opy_(platform_index, item_index):
  global bstack111l1llll_opy_
  lock_file = bstack111l1llll_opy_ + bstack1ll1ll1_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫഥ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll1ll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩദ"))
    try:
      bstack1ll111l11_opy_ = {}
      if os.path.exists(bstack111l1llll_opy_):
        with open(bstack111l1llll_opy_, bstack1ll1ll1_opy_ (u"ࠧࡳࠩധ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll111l11_opy_ = json.loads(content)
      bstack1ll111l11_opy_[item_index] = platform_index
      with open(bstack111l1llll_opy_, bstack1ll1ll1_opy_ (u"ࠣࡹࠥന")) as outfile:
        json.dump(bstack1ll111l11_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1ll1ll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡼࡸࡩࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧഩ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack111l1llll_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack1ll111l11_opy_ = {}
      if os.path.exists(bstack111l1llll_opy_):
        with open(bstack111l1llll_opy_, bstack1ll1ll1_opy_ (u"ࠪࡶࠬപ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll111l11_opy_ = json.loads(content)
      bstack1ll111l11_opy_[item_index] = platform_index
      with open(bstack111l1llll_opy_, bstack1ll1ll1_opy_ (u"ࠦࡼࠨഫ")) as outfile:
        json.dump(bstack1ll111l11_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡸࡴ࡬ࡸ࡮ࡴࡧࠡࡶࡲࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪബ") + str(e))
def bstack1ll1ll1ll_opy_(bstack1111llll1_opy_):
  global CONFIG
  bstack1l1l1ll11l_opy_ = bstack1ll1ll1_opy_ (u"࠭ࠧഭ")
  if not bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪമ") in CONFIG:
    logger.info(bstack1ll1ll1_opy_ (u"ࠨࡐࡲࠤࡵࡲࡡࡵࡨࡲࡶࡲࡹࠠࡱࡣࡶࡷࡪࡪࠠࡶࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥࡸࡥࡱࡱࡵࡸࠥ࡬࡯ࡳࠢࡕࡳࡧࡵࡴࠡࡴࡸࡲࠬയ"))
  try:
    platform = CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬര")][bstack1111llll1_opy_]
    if bstack1ll1ll1_opy_ (u"ࠪࡳࡸ࠭റ") in platform:
      bstack1l1l1ll11l_opy_ += str(platform[bstack1ll1ll1_opy_ (u"ࠫࡴࡹࠧല")]) + bstack1ll1ll1_opy_ (u"ࠬ࠲ࠠࠨള")
    if bstack1ll1ll1_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩഴ") in platform:
      bstack1l1l1ll11l_opy_ += str(platform[bstack1ll1ll1_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪവ")]) + bstack1ll1ll1_opy_ (u"ࠨ࠮ࠣࠫശ")
    if bstack1ll1ll1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ഷ") in platform:
      bstack1l1l1ll11l_opy_ += str(platform[bstack1ll1ll1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧസ")]) + bstack1ll1ll1_opy_ (u"ࠫ࠱ࠦࠧഹ")
    if bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧഺ") in platform:
      bstack1l1l1ll11l_opy_ += str(platform[bstack1ll1ll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ഻")]) + bstack1ll1ll1_opy_ (u"഼ࠧ࠭ࠢࠪ")
    if bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ഽ") in platform:
      bstack1l1l1ll11l_opy_ += str(platform[bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧാ")]) + bstack1ll1ll1_opy_ (u"ࠪ࠰ࠥ࠭ി")
    if bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬീ") in platform:
      bstack1l1l1ll11l_opy_ += str(platform[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ു")]) + bstack1ll1ll1_opy_ (u"࠭ࠬࠡࠩൂ")
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡔࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡱࡩࡷࡧࡴࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡳࡵࡴ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡶࡪࡶ࡯ࡳࡶࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡴࡴࠧൃ") + str(e))
  finally:
    if bstack1l1l1ll11l_opy_[len(bstack1l1l1ll11l_opy_) - 2:] == bstack1ll1ll1_opy_ (u"ࠨ࠮ࠣࠫൄ"):
      bstack1l1l1ll11l_opy_ = bstack1l1l1ll11l_opy_[:-2]
    return bstack1l1l1ll11l_opy_
def bstack11l11l11l1_opy_(path, bstack1l1l1ll11l_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l1ll111ll_opy_ = ET.parse(path)
    bstack1lll1l1l11_opy_ = bstack1l1ll111ll_opy_.getroot()
    bstack111l111l1_opy_ = None
    for suite in bstack1lll1l1l11_opy_.iter(bstack1ll1ll1_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨ൅")):
      if bstack1ll1ll1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪെ") in suite.attrib:
        suite.attrib[bstack1ll1ll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩേ")] += bstack1ll1ll1_opy_ (u"ࠬࠦࠧൈ") + bstack1l1l1ll11l_opy_
        bstack111l111l1_opy_ = suite
    bstack11l11l1lll_opy_ = None
    for robot in bstack1lll1l1l11_opy_.iter(bstack1ll1ll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ൉")):
      bstack11l11l1lll_opy_ = robot
    bstack11llllll1l_opy_ = len(bstack11l11l1lll_opy_.findall(bstack1ll1ll1_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ൊ")))
    if bstack11llllll1l_opy_ == 1:
      bstack11l11l1lll_opy_.remove(bstack11l11l1lll_opy_.findall(bstack1ll1ll1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧോ"))[0])
      bstack11ll111ll1_opy_ = ET.Element(bstack1ll1ll1_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨൌ"), attrib={bstack1ll1ll1_opy_ (u"ࠪࡲࡦࡳࡥࠨ്"): bstack1ll1ll1_opy_ (u"ࠫࡘࡻࡩࡵࡧࡶࠫൎ"), bstack1ll1ll1_opy_ (u"ࠬ࡯ࡤࠨ൏"): bstack1ll1ll1_opy_ (u"࠭ࡳ࠱ࠩ൐")})
      bstack11l11l1lll_opy_.insert(1, bstack11ll111ll1_opy_)
      bstack11l1l1l1ll_opy_ = None
      for suite in bstack11l11l1lll_opy_.iter(bstack1ll1ll1_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭൑")):
        bstack11l1l1l1ll_opy_ = suite
      bstack11l1l1l1ll_opy_.append(bstack111l111l1_opy_)
      bstack1l1ll1ll11_opy_ = None
      for status in bstack111l111l1_opy_.iter(bstack1ll1ll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ൒")):
        bstack1l1ll1ll11_opy_ = status
      bstack11l1l1l1ll_opy_.append(bstack1l1ll1ll11_opy_)
    bstack1l1ll111ll_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠧ൓") + str(e))
def bstack11lll1l1ll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1ll1ll1l11_opy_
  global CONFIG
  if bstack1ll1ll1_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢൔ") in options:
    del options[bstack1ll1ll1_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣൕ")]
  json_data = bstack11l1l1l11l_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack1ll1ll1_opy_ (u"ࠬࡶࡡࡣࡱࡷࡣࡷ࡫ࡳࡶ࡮ࡷࡷࠬൖ"), str(item_id), bstack1ll1ll1_opy_ (u"࠭࡯ࡶࡶࡳࡹࡹ࠴ࡸ࡮࡮ࠪൗ"))
    bstack11l11l11l1_opy_(path, bstack1ll1ll1ll_opy_(json_data[item_id]))
  bstack1111l11l1l_opy_()
  return bstack1ll1ll1l11_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1ll1llllll_opy_(self, ff_profile_dir):
  global bstack11lll111l1_opy_
  if not ff_profile_dir:
    return None
  return bstack11lll111l1_opy_(self, ff_profile_dir)
def bstack1l1l111ll1_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1ll11ll1ll_opy_
  bstack1l1ll11111_opy_ = []
  if bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ൘") in CONFIG:
    bstack1l1ll11111_opy_ = CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ൙")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1ll1ll1_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࠥ൚")],
      pabot_args[bstack1ll1ll1_opy_ (u"ࠥࡺࡪࡸࡢࡰࡵࡨࠦ൛")],
      argfile,
      pabot_args.get(bstack1ll1ll1_opy_ (u"ࠦ࡭࡯ࡶࡦࠤ൜")),
      pabot_args[bstack1ll1ll1_opy_ (u"ࠧࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠣ൝")],
      platform[0],
      bstack1ll11ll1ll_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1ll1ll1_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡧ࡫࡯ࡩࡸࠨ൞")] or [(bstack1ll1ll1_opy_ (u"ࠢࠣൟ"), None)]
    for platform in enumerate(bstack1l1ll11111_opy_)
  ]
def bstack1l1l1lll1l_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1ll11lll1_opy_=bstack1ll1ll1_opy_ (u"ࠨࠩൠ")):
  global bstack11l11ll11_opy_
  self.platform_index = platform_index
  self.bstack1l1l1111ll_opy_ = bstack1ll11lll1_opy_
  bstack11l11ll11_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1ll11lll11_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack11l1l1ll1_opy_
  global bstack11l1lll11l_opy_
  bstack1ll111l1ll_opy_ = copy.deepcopy(item)
  if not bstack1ll1ll1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫൡ") in item.options:
    bstack1ll111l1ll_opy_.options[bstack1ll1ll1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬൢ")] = []
  bstack11ll1l1l11_opy_ = bstack1ll111l1ll_opy_.options[bstack1ll1ll1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ൣ")].copy()
  for v in bstack1ll111l1ll_opy_.options[bstack1ll1ll1_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ൤")]:
    if bstack1ll1ll1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜ࠬ൥") in v:
      bstack11ll1l1l11_opy_.remove(v)
    if bstack1ll1ll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙ࠧ൦") in v:
      bstack11ll1l1l11_opy_.remove(v)
    if bstack1ll1ll1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ൧") in v:
      bstack11ll1l1l11_opy_.remove(v)
  bstack11ll1l1l11_opy_.insert(0, bstack1ll1ll1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘ࠻ࡽࢀࠫ൨").format(bstack1ll111l1ll_opy_.platform_index))
  bstack11ll1l1l11_opy_.insert(0, bstack1ll1ll1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘ࠺ࡼࡿࠪ൩").format(bstack1ll111l1ll_opy_.bstack1l1l1111ll_opy_))
  bstack1ll111l1ll_opy_.options[bstack1ll1ll1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭൪")] = bstack11ll1l1l11_opy_
  if bstack11l1lll11l_opy_:
    bstack1ll111l1ll_opy_.options[bstack1ll1ll1_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ൫")].insert(0, bstack1ll1ll1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘࡀࡻࡾࠩ൬").format(bstack11l1lll11l_opy_))
  return bstack11l1l1ll1_opy_(caller_id, datasources, is_last, bstack1ll111l1ll_opy_, outs_dir)
def bstack11ll111l1_opy_(command, item_index):
  try:
    if bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ൭")):
      os.environ[bstack1ll1ll1_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩ൮")] = json.dumps(CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ൯")][item_index % bstack1l1l1llll1_opy_])
    global bstack11l1lll11l_opy_
    if bstack11l1lll11l_opy_:
      command[0] = command[0].replace(bstack1ll1ll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ൰"), bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨ൱") + str(
        item_index) + bstack1ll1ll1_opy_ (u"ࠬࠦࠧ൲") + bstack11l1lll11l_opy_, 1)
    else:
      command[0] = command[0].replace(bstack1ll1ll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ൳"),
                                      bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡳࡥ࡭ࠣࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠣࠫ൴") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack1ll1ll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠ࡮ࡱࡧ࡭࡫ࡿࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡢࡰࡧࠤ࡫ࡵࡲࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱ࠾ࠥࢁࡽࠨ൵").format(str(e)))
def bstack1ll1l1l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1ll1l111ll_opy_
  try:
    bstack11ll111l1_opy_(command, item_index)
    return bstack1ll1l111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack1ll1ll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴ࠺ࠡࡽࢀࠫ൶").format(str(e)))
    raise e
def bstack1l1l1lll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1ll1l111ll_opy_
  try:
    bstack11ll111l1_opy_(command, item_index)
    return bstack1ll1l111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack1ll1ll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠴࠱࠵࠸ࡀࠠࡼࡿࠪ൷").format(str(e)))
    try:
      return bstack1ll1l111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack1ll1ll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࠸࠮࠲࠵ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩ൸").format(str(e2)))
      raise e
def bstack11l1llll11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1ll1l111ll_opy_
  try:
    bstack11ll111l1_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack1ll1l111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack1ll1ll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰࠣ࠶࠳࠷࠵࠻ࠢࡾࢁࠬ൹").format(str(e)))
    try:
      return bstack1ll1l111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack1ll1ll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠ࠳࠰࠴࠹ࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫൺ").format(str(e2)))
      raise e
def _111l1ll1l1_opy_(bstack1l111l111l_opy_, item_index, process_timeout, sleep_before_start, bstack1111lll111_opy_):
  bstack11ll111l1_opy_(bstack1l111l111l_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack1111l111l1_opy_(command, bstack1l11l11l11_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1ll1l111ll_opy_
  try:
    bstack11ll111l1_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack1ll1l111ll_opy_(command, bstack1l11l11l11_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1ll1ll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲࠥ࠻࠮࠱࠼ࠣࡿࢂ࠭ൻ").format(str(e)))
    try:
      return bstack1ll1l111ll_opy_(command, bstack1l11l11l11_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1ll1ll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨർ").format(str(e2)))
      raise e
def bstack11111111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1ll1l111ll_opy_
  try:
    process_timeout = _111l1ll1l1_opy_(command, item_index, process_timeout, sleep_before_start, bstack1ll1ll1_opy_ (u"ࠩ࠷࠲࠷࠭ൽ"))
    return bstack1ll1l111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1ll1ll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠶࠱࠶࠿ࠦࡻࡾࠩൾ").format(str(e)))
    try:
      return bstack1ll1l111ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1ll1ll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫൿ").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack111lllll11_opy_(self, runner, quiet=False, capture=True):
  global bstack1ll1llll1_opy_
  bstack11ll11l1ll_opy_ = bstack1ll1llll1_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack1ll1ll1_opy_ (u"ࠬ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࡠࡣࡵࡶࠬ඀")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1ll1ll1_opy_ (u"࠭ࡥࡹࡥࡢࡸࡷࡧࡣࡦࡤࡤࡧࡰࡥࡡࡳࡴࠪඁ")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack11ll11l1ll_opy_
def bstack111l11ll11_opy_(runner, hook_name, context, element, bstack1lllll1lll_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1ll1l1l1l_opy_.bstack11l1llll_opy_(hook_name, element)
    bstack1lllll1lll_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1ll1l1l1l_opy_.bstack11ll1ll1_opy_(element)
      if hook_name not in [bstack1ll1ll1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫං"), bstack1ll1ll1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫඃ")] and args and hasattr(args[0], bstack1ll1ll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࡠ࡯ࡨࡷࡸࡧࡧࡦࠩ඄")):
        args[0].error_message = bstack1ll1ll1_opy_ (u"ࠪࠫඅ")
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡩࡣࡱࡨࡱ࡫ࠠࡩࡱࡲ࡯ࡸࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦ࠼ࠣࡿࢂ࠭ආ").format(str(e)))
@measure(event_name=EVENTS.bstack11111lll11_opy_, stage=STAGE.bstack111l1l111_opy_, hook_type=bstack1ll1ll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡆࡲ࡬ࠣඇ"), bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack1l111l11l1_opy_(runner, name, context, bstack1lllll1lll_opy_, *args):
    if runner.hooks.get(bstack1ll1ll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥඈ")).__name__ != bstack1ll1ll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࡣࡩ࡫ࡦࡢࡷ࡯ࡸࡤ࡮࡯ࡰ࡭ࠥඉ"):
      bstack111l11ll11_opy_(runner, name, context, runner, bstack1lllll1lll_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack11111l11l_opy_(bstack1ll1ll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧඊ")) else context.browser
      runner.driver_initialised = bstack1ll1ll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨඋ")
    except Exception as e:
      logger.debug(bstack1ll1ll1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡸ࡫ࠠࡢࡶࡷࡶ࡮ࡨࡵࡵࡧ࠽ࠤࢀࢃࠧඌ").format(str(e)))
def bstack1111l1lll1_opy_(runner, name, context, bstack1lllll1lll_opy_, *args):
    bstack111l11ll11_opy_(runner, name, context, context.feature, bstack1lllll1lll_opy_, *args)
    try:
      if not bstack1lll1llll1_opy_:
        bstack111ll1ll1_opy_ = threading.current_thread().bstackSessionDriver if bstack11111l11l_opy_(bstack1ll1ll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪඍ")) else context.browser
        if is_driver_active(bstack111ll1ll1_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack1ll1ll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨඎ")
          bstack1l1lll11l_opy_ = str(runner.feature.name)
          bstack1l1l11l1ll_opy_(context, bstack1l1lll11l_opy_)
          bstack111ll1ll1_opy_.execute_script(bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫඏ") + json.dumps(bstack1l1lll11l_opy_) + bstack1ll1ll1_opy_ (u"ࠧࡾࡿࠪඐ"))
    except Exception as e:
      logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨඑ").format(str(e)))
def bstack1l11l11lll_opy_(runner, name, context, bstack1lllll1lll_opy_, *args):
    if hasattr(context, bstack1ll1ll1_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫඒ")):
        bstack1ll1l1l1l_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack1ll1ll1_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬඓ")) else context.feature
    bstack111l11ll11_opy_(runner, name, context, target, bstack1lllll1lll_opy_, *args)
@measure(event_name=EVENTS.bstack1l1ll1111_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack1ll11111ll_opy_(runner, name, context, bstack1lllll1lll_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1ll1l1l1l_opy_.start_test(context)
    bstack111l11ll11_opy_(runner, name, context, context.scenario, bstack1lllll1lll_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1l11l1llll_opy_.bstack11l1111ll1_opy_(context, *args)
    try:
      bstack111ll1ll1_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪඔ"), context.browser)
      if is_driver_active(bstack111ll1ll1_opy_):
        bstack1ll111ll_opy_.bstack111l111l11_opy_(bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫඕ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack1ll1ll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣඖ")
        if (not bstack1lll1llll1_opy_):
          scenario_name = args[0].name
          feature_name = bstack1l1lll11l_opy_ = str(runner.feature.name)
          bstack1l1lll11l_opy_ = feature_name + bstack1ll1ll1_opy_ (u"ࠧࠡ࠯ࠣࠫ඗") + scenario_name
          if runner.driver_initialised == bstack1ll1ll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥ඘"):
            bstack1l1l11l1ll_opy_(context, bstack1l1lll11l_opy_)
            bstack111ll1ll1_opy_.execute_script(bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ඙") + json.dumps(bstack1l1lll11l_opy_) + bstack1ll1ll1_opy_ (u"ࠪࢁࢂ࠭ක"))
    except Exception as e:
      logger.debug(bstack1ll1ll1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬඛ").format(str(e)))
@measure(event_name=EVENTS.bstack11111lll11_opy_, stage=STAGE.bstack111l1l111_opy_, hook_type=bstack1ll1ll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡘࡺࡥࡱࠤග"), bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack111l1l1l11_opy_(runner, name, context, bstack1lllll1lll_opy_, *args):
    bstack111l11ll11_opy_(runner, name, context, args[0], bstack1lllll1lll_opy_, *args)
    try:
      bstack111ll1ll1_opy_ = threading.current_thread().bstackSessionDriver if bstack11111l11l_opy_(bstack1ll1ll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඝ")) else context.browser
      if is_driver_active(bstack111ll1ll1_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack1ll1ll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧඞ")
        bstack1ll1l1l1l_opy_.bstack11l1l1ll_opy_(args[0])
        if runner.driver_initialised == bstack1ll1ll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨඟ"):
          feature_name = bstack1l1lll11l_opy_ = str(runner.feature.name)
          bstack1l1lll11l_opy_ = feature_name + bstack1ll1ll1_opy_ (u"ࠩࠣ࠱ࠥ࠭ච") + context.scenario.name
          bstack111ll1ll1_opy_.execute_script(bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨඡ") + json.dumps(bstack1l1lll11l_opy_) + bstack1ll1ll1_opy_ (u"ࠫࢂࢃࠧජ"))
    except Exception as e:
      logger.debug(bstack1ll1ll1_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩඣ").format(str(e)))
@measure(event_name=EVENTS.bstack11111lll11_opy_, stage=STAGE.bstack111l1l111_opy_, hook_type=bstack1ll1ll1_opy_ (u"ࠨࡡࡧࡶࡨࡶࡘࡺࡥࡱࠤඤ"), bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack1ll1l11111_opy_(runner, name, context, bstack1lllll1lll_opy_, *args):
  bstack1ll1l1l1l_opy_.bstack11ll1lll_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack111ll1ll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1ll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ඥ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack111ll1ll1_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack1ll1ll1_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨඦ")
        feature_name = bstack1l1lll11l_opy_ = str(runner.feature.name)
        bstack1l1lll11l_opy_ = feature_name + bstack1ll1ll1_opy_ (u"ࠩࠣ࠱ࠥ࠭ට") + context.scenario.name
        bstack111ll1ll1_opy_.execute_script(bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨඨ") + json.dumps(bstack1l1lll11l_opy_) + bstack1ll1ll1_opy_ (u"ࠫࢂࢃࠧඩ"))
    if str(step_status).lower() == bstack1ll1ll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬඪ"):
      bstack111ll11l1l_opy_ = bstack1ll1ll1_opy_ (u"࠭ࠧණ")
      bstack11lllllll1_opy_ = bstack1ll1ll1_opy_ (u"ࠧࠨඬ")
      bstack1l1111l1l_opy_ = bstack1ll1ll1_opy_ (u"ࠨࠩත")
      try:
        import traceback
        bstack111ll11l1l_opy_ = runner.exception.__class__.__name__
        bstack11ll1111_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11lllllll1_opy_ = bstack1ll1ll1_opy_ (u"ࠩࠣࠫථ").join(bstack11ll1111_opy_)
        bstack1l1111l1l_opy_ = bstack11ll1111_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l1111ll11_opy_.format(str(e)))
      bstack111ll11l1l_opy_ += bstack1l1111l1l_opy_
      bstack11l1l1l111_opy_(context, json.dumps(str(args[0].name) + bstack1ll1ll1_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤද") + str(bstack11lllllll1_opy_)),
                          bstack1ll1ll1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥධ"))
      if runner.driver_initialised == bstack1ll1ll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥන"):
        bstack1l1ll1l111_opy_(getattr(context, bstack1ll1ll1_opy_ (u"࠭ࡰࡢࡩࡨࠫ඲"), None), bstack1ll1ll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢඳ"), bstack111ll11l1l_opy_)
        bstack111ll1ll1_opy_.execute_script(bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ප") + json.dumps(str(args[0].name) + bstack1ll1ll1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣඵ") + str(bstack11lllllll1_opy_)) + bstack1ll1ll1_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪබ"))
      if runner.driver_initialised == bstack1ll1ll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤභ"):
        bstack11lll11ll1_opy_(bstack111ll1ll1_opy_, bstack1ll1ll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬම"), bstack1ll1ll1_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥඹ") + str(bstack111ll11l1l_opy_))
    else:
      bstack11l1l1l111_opy_(context, bstack1ll1ll1_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣය"), bstack1ll1ll1_opy_ (u"ࠣ࡫ࡱࡪࡴࠨර"))
      if runner.driver_initialised == bstack1ll1ll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢ඼"):
        bstack1l1ll1l111_opy_(getattr(context, bstack1ll1ll1_opy_ (u"ࠪࡴࡦ࡭ࡥࠨල"), None), bstack1ll1ll1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦ඾"))
      bstack111ll1ll1_opy_.execute_script(bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ඿") + json.dumps(str(args[0].name) + bstack1ll1ll1_opy_ (u"ࠨࠠ࠮ࠢࡓࡥࡸࡹࡥࡥࠣࠥව")) + bstack1ll1ll1_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭ශ"))
      if runner.driver_initialised == bstack1ll1ll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨෂ"):
        bstack11lll11ll1_opy_(bstack111ll1ll1_opy_, bstack1ll1ll1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤස"))
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩහ").format(str(e)))
  bstack111l11ll11_opy_(runner, name, context, args[0], bstack1lllll1lll_opy_, *args)
@measure(event_name=EVENTS.bstack1ll1111ll1_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack11l111ll11_opy_(runner, name, context, bstack1lllll1lll_opy_, *args):
  bstack1ll1l1l1l_opy_.end_test(args[0])
  try:
    bstack11l11ll1ll_opy_ = args[0].status.name
    bstack111ll1ll1_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪළ"), context.browser)
    bstack1l11l1llll_opy_.bstack1l1l1l11l_opy_(bstack111ll1ll1_opy_)
    if str(bstack11l11ll1ll_opy_).lower() == bstack1ll1ll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬෆ"):
      bstack111ll11l1l_opy_ = bstack1ll1ll1_opy_ (u"࠭ࠧ෇")
      bstack11lllllll1_opy_ = bstack1ll1ll1_opy_ (u"ࠧࠨ෈")
      bstack1l1111l1l_opy_ = bstack1ll1ll1_opy_ (u"ࠨࠩ෉")
      try:
        import traceback
        bstack111ll11l1l_opy_ = runner.exception.__class__.__name__
        bstack11ll1111_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11lllllll1_opy_ = bstack1ll1ll1_opy_ (u"්ࠩࠣࠫ").join(bstack11ll1111_opy_)
        bstack1l1111l1l_opy_ = bstack11ll1111_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l1111ll11_opy_.format(str(e)))
      bstack111ll11l1l_opy_ += bstack1l1111l1l_opy_
      bstack11l1l1l111_opy_(context, json.dumps(str(args[0].name) + bstack1ll1ll1_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ෋") + str(bstack11lllllll1_opy_)),
                          bstack1ll1ll1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ෌"))
      if runner.driver_initialised == bstack1ll1ll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ෍") or runner.driver_initialised == bstack1ll1ll1_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෎"):
        bstack1l1ll1l111_opy_(getattr(context, bstack1ll1ll1_opy_ (u"ࠧࡱࡣࡪࡩࠬා"), None), bstack1ll1ll1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣැ"), bstack111ll11l1l_opy_)
        bstack111ll1ll1_opy_.execute_script(bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧෑ") + json.dumps(str(args[0].name) + bstack1ll1ll1_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤි") + str(bstack11lllllll1_opy_)) + bstack1ll1ll1_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫී"))
      if runner.driver_initialised == bstack1ll1ll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢු") or runner.driver_initialised == bstack1ll1ll1_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෕"):
        bstack11lll11ll1_opy_(bstack111ll1ll1_opy_, bstack1ll1ll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧූ"), bstack1ll1ll1_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧ෗") + str(bstack111ll11l1l_opy_))
    else:
      bstack11l1l1l111_opy_(context, bstack1ll1ll1_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥෘ"), bstack1ll1ll1_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣෙ"))
      if runner.driver_initialised == bstack1ll1ll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨේ") or runner.driver_initialised == bstack1ll1ll1_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬෛ"):
        bstack1l1ll1l111_opy_(getattr(context, bstack1ll1ll1_opy_ (u"࠭ࡰࡢࡩࡨࠫො"), None), bstack1ll1ll1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢෝ"))
      bstack111ll1ll1_opy_.execute_script(bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ෞ") + json.dumps(str(args[0].name) + bstack1ll1ll1_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨෟ")) + bstack1ll1ll1_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩ෠"))
      if runner.driver_initialised == bstack1ll1ll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ෡") or runner.driver_initialised == bstack1ll1ll1_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ෢"):
        bstack11lll11ll1_opy_(bstack111ll1ll1_opy_, bstack1ll1ll1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ෣"))
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩ෤").format(str(e)))
  bstack111l11ll11_opy_(runner, name, context, context.scenario, bstack1lllll1lll_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack11lll1111l_opy_(runner, name, context, bstack1lllll1lll_opy_, *args):
    target = context.scenario if hasattr(context, bstack1ll1ll1_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪ෥")) else context.feature
    bstack111l11ll11_opy_(runner, name, context, target, bstack1lllll1lll_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack11l11l11l_opy_(runner, name, context, bstack1lllll1lll_opy_, *args):
    try:
      bstack111ll1ll1_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ෦"), context.browser)
      bstack11llll1ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠪࠫ෧")
      if context.failed is True:
        bstack1l1l1l111l_opy_ = []
        bstack1l1lll111_opy_ = []
        bstack1lll111l1l_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1l1l1l111l_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11ll1111_opy_ = traceback.format_tb(exc_tb)
            bstack11l1l11l11_opy_ = bstack1ll1ll1_opy_ (u"ࠫࠥ࠭෨").join(bstack11ll1111_opy_)
            bstack1l1lll111_opy_.append(bstack11l1l11l11_opy_)
            bstack1lll111l1l_opy_.append(bstack11ll1111_opy_[-1])
        except Exception as e:
          logger.debug(bstack1l1111ll11_opy_.format(str(e)))
        bstack111ll11l1l_opy_ = bstack1ll1ll1_opy_ (u"ࠬ࠭෩")
        for i in range(len(bstack1l1l1l111l_opy_)):
          bstack111ll11l1l_opy_ += bstack1l1l1l111l_opy_[i] + bstack1lll111l1l_opy_[i] + bstack1ll1ll1_opy_ (u"࠭࡜࡯ࠩ෪")
        bstack11llll1ll1_opy_ = bstack1ll1ll1_opy_ (u"ࠧࠡࠩ෫").join(bstack1l1lll111_opy_)
        if runner.driver_initialised in [bstack1ll1ll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤ෬"), bstack1ll1ll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨ෭")]:
          bstack11l1l1l111_opy_(context, bstack11llll1ll1_opy_, bstack1ll1ll1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ෮"))
          bstack1l1ll1l111_opy_(getattr(context, bstack1ll1ll1_opy_ (u"ࠫࡵࡧࡧࡦࠩ෯"), None), bstack1ll1ll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ෰"), bstack111ll11l1l_opy_)
          bstack111ll1ll1_opy_.execute_script(bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ෱") + json.dumps(bstack11llll1ll1_opy_) + bstack1ll1ll1_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧෲ"))
          bstack11lll11ll1_opy_(bstack111ll1ll1_opy_, bstack1ll1ll1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣෳ"), bstack1ll1ll1_opy_ (u"ࠤࡖࡳࡲ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰࡵࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡡࡴࠢ෴") + str(bstack111ll11l1l_opy_))
          bstack11lllll1l1_opy_ = bstack1l11ll1l1_opy_(bstack11llll1ll1_opy_, runner.feature.name, logger)
          if (bstack11lllll1l1_opy_ != None):
            bstack11ll11l11_opy_.append(bstack11lllll1l1_opy_)
      else:
        if runner.driver_initialised in [bstack1ll1ll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦ෵"), bstack1ll1ll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣ෶")]:
          bstack11l1l1l111_opy_(context, bstack1ll1ll1_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣ෷") + str(runner.feature.name) + bstack1ll1ll1_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣ෸"), bstack1ll1ll1_opy_ (u"ࠢࡪࡰࡩࡳࠧ෹"))
          bstack1l1ll1l111_opy_(getattr(context, bstack1ll1ll1_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭෺"), None), bstack1ll1ll1_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ෻"))
          bstack111ll1ll1_opy_.execute_script(bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ෼") + json.dumps(bstack1ll1ll1_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢ෽") + str(runner.feature.name) + bstack1ll1ll1_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢ෾")) + bstack1ll1ll1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬ෿"))
          bstack11lll11ll1_opy_(bstack111ll1ll1_opy_, bstack1ll1ll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ฀"))
          bstack11lllll1l1_opy_ = bstack1l11ll1l1_opy_(bstack11llll1ll1_opy_, runner.feature.name, logger)
          if (bstack11lllll1l1_opy_ != None):
            bstack11ll11l11_opy_.append(bstack11lllll1l1_opy_)
    except Exception as e:
      logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪก").format(str(e)))
    bstack111l11ll11_opy_(runner, name, context, context.feature, bstack1lllll1lll_opy_, *args)
@measure(event_name=EVENTS.bstack11111lll11_opy_, stage=STAGE.bstack111l1l111_opy_, hook_type=bstack1ll1ll1_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡂ࡮࡯ࠦข"), bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack111lll1l1l_opy_(runner, name, context, bstack1lllll1lll_opy_, *args):
    bstack111l11ll11_opy_(runner, name, context, runner, bstack1lllll1lll_opy_, *args)
def bstack1111111l1_opy_(self, name, context, *args):
  try:
    if bstack111l1ll1ll_opy_:
      platform_index = int(threading.current_thread()._name) % bstack1l1l1llll1_opy_
      bstack1l1l11l11l_opy_ = CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ฃ")][platform_index]
      os.environ[bstack1ll1ll1_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬค")] = json.dumps(bstack1l1l11l11l_opy_)
    global bstack1lllll1lll_opy_
    if not hasattr(self, bstack1ll1ll1_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡦࡦࠪฅ")):
      self.driver_initialised = None
    bstack1ll1l1111l_opy_ = {
        bstack1ll1ll1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪฆ"): bstack1l111l11l1_opy_,
        bstack1ll1ll1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠨง"): bstack1111l1lll1_opy_,
        bstack1ll1ll1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡶࡤ࡫ࠬจ"): bstack1l11l11lll_opy_,
        bstack1ll1ll1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫฉ"): bstack1ll11111ll_opy_,
        bstack1ll1ll1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠨช"): bstack111l1l1l11_opy_,
        bstack1ll1ll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡹ࡫ࡰࠨซ"): bstack1ll1l11111_opy_,
        bstack1ll1ll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ฌ"): bstack11l111ll11_opy_,
        bstack1ll1ll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡺࡡࡨࠩญ"): bstack11lll1111l_opy_,
        bstack1ll1ll1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧฎ"): bstack11l11l11l_opy_,
        bstack1ll1ll1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫฏ"): bstack111lll1l1l_opy_
    }
    handler = bstack1ll1l1111l_opy_.get(name, bstack1lllll1lll_opy_)
    try:
      handler(self, name, context, bstack1lllll1lll_opy_, *args)
    except Exception as e:
      logger.debug(bstack1ll1ll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨࠤ࡭ࡵ࡯࡬ࠢ࡫ࡥࡳࡪ࡬ࡦࡴࠣࡿࢂࡀࠠࡼࡿࠪฐ").format(name, str(e)))
    if name in [bstack1ll1ll1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪฑ"), bstack1ll1ll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬฒ"), bstack1ll1ll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨณ")]:
      try:
        bstack111ll1ll1_opy_ = threading.current_thread().bstackSessionDriver if bstack11111l11l_opy_(bstack1ll1ll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬด")) else context.browser
        bstack11l11lll1_opy_ = (
          (name == bstack1ll1ll1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪต") and self.driver_initialised == bstack1ll1ll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧถ")) or
          (name == bstack1ll1ll1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩท") and self.driver_initialised == bstack1ll1ll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦธ")) or
          (name == bstack1ll1ll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬน") and self.driver_initialised in [bstack1ll1ll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢบ"), bstack1ll1ll1_opy_ (u"ࠨࡩ࡯ࡵࡷࡩࡵࠨป")]) or
          (name == bstack1ll1ll1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡵࡧࡳࠫผ") and self.driver_initialised == bstack1ll1ll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨฝ"))
        )
        if bstack11l11lll1_opy_:
          self.driver_initialised = None
          if bstack111ll1ll1_opy_ and hasattr(bstack111ll1ll1_opy_, bstack1ll1ll1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩ࠭พ")):
            try:
              bstack111ll1ll1_opy_.quit()
            except Exception as e:
              logger.debug(bstack1ll1ll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡴࡹ࡮ࡺࡴࡪࡰࡪࠤࡩࡸࡩࡷࡧࡵࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡩࡱࡲ࡯࠿ࠦࡻࡾࠩฟ").format(str(e)))
      except Exception as e:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡮࡯ࡰ࡭ࠣࡧࡱ࡫ࡡ࡯ࡷࡳࠤ࡫ࡵࡲࠡࡽࢀ࠾ࠥࢁࡽࠨภ").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠬࡉࡲࡪࡶ࡬ࡧࡦࡲࠠࡦࡴࡵࡳࡷࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦࠢࡵࡹࡳࠦࡨࡰࡱ࡮ࠤࢀࢃ࠺ࠡࡽࢀࠫม").format(name, str(e)))
    try:
      bstack1lllll1lll_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack1ll1ll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡳࡷ࡯ࡧࡪࡰࡤࡰࠥࡨࡥࡩࡣࡹࡩࠥ࡮࡯ࡰ࡭ࠣࡿࢂࡀࠠࡼࡿࠪย").format(name, str(e2)))
def bstack11111lll1_opy_(config, startdir):
  return bstack1ll1ll1_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧร").format(bstack1ll1ll1_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢฤ"))
notset = Notset()
def bstack1l1lll1l1l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1ll1ll11l1_opy_
  if str(name).lower() == bstack1ll1ll1_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩล"):
    return bstack1ll1ll1_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤฦ")
  else:
    return bstack1ll1ll11l1_opy_(self, name, default, skip)
def bstack11ll1111l_opy_(item, when):
  global bstack1l111111l_opy_
  try:
    bstack1l111111l_opy_(item, when)
  except Exception as e:
    pass
def bstack1ll11ll1l_opy_():
  return
def bstack1lll11111_opy_(type, name, status, reason, bstack1ll1l1l1l1_opy_, bstack1lll1lll1l_opy_):
  bstack1l1ll1llll_opy_ = {
    bstack1ll1ll1_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫว"): type,
    bstack1ll1ll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨศ"): {}
  }
  if type == bstack1ll1ll1_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨษ"):
    bstack1l1ll1llll_opy_[bstack1ll1ll1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪส")][bstack1ll1ll1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧห")] = bstack1ll1l1l1l1_opy_
    bstack1l1ll1llll_opy_[bstack1ll1ll1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬฬ")][bstack1ll1ll1_opy_ (u"ࠪࡨࡦࡺࡡࠨอ")] = json.dumps(str(bstack1lll1lll1l_opy_))
  if type == bstack1ll1ll1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬฮ"):
    bstack1l1ll1llll_opy_[bstack1ll1ll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨฯ")][bstack1ll1ll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫะ")] = name
  if type == bstack1ll1ll1_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪั"):
    bstack1l1ll1llll_opy_[bstack1ll1ll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫา")][bstack1ll1ll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩำ")] = status
    if status == bstack1ll1ll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪิ"):
      bstack1l1ll1llll_opy_[bstack1ll1ll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧี")][bstack1ll1ll1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬึ")] = json.dumps(str(reason))
  bstack1l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫื").format(json.dumps(bstack1l1ll1llll_opy_))
  return bstack1l1lll1l1_opy_
def bstack11lll1l1l1_opy_(driver_command, response):
    if driver_command == bstack1ll1ll1_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷุࠫ"):
        bstack1ll111ll_opy_.bstack1lllll1ll1_opy_({
            bstack1ll1ll1_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ูࠧ"): response[bstack1ll1ll1_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨฺ")],
            bstack1ll1ll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ฻"): bstack1ll111ll_opy_.current_test_uuid()
        })
def bstack1l11l1l1l_opy_(item, call, rep):
  global bstack1l1l1ll1l_opy_
  global bstack1l1l1l1ll1_opy_
  global bstack1lll1llll1_opy_
  name = bstack1ll1ll1_opy_ (u"ࠫࠬ฼")
  try:
    if rep.when == bstack1ll1ll1_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ฽"):
      bstack1l111l111_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1lll1llll1_opy_:
          name = str(rep.nodeid)
          bstack1l1l1lll11_opy_ = bstack1lll11111_opy_(bstack1ll1ll1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ฾"), name, bstack1ll1ll1_opy_ (u"ࠧࠨ฿"), bstack1ll1ll1_opy_ (u"ࠨࠩเ"), bstack1ll1ll1_opy_ (u"ࠩࠪแ"), bstack1ll1ll1_opy_ (u"ࠪࠫโ"))
          threading.current_thread().bstack1lll11ll1_opy_ = name
          for driver in bstack1l1l1l1ll1_opy_:
            if bstack1l111l111_opy_ == driver.session_id:
              driver.execute_script(bstack1l1l1lll11_opy_)
      except Exception as e:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫใ").format(str(e)))
      try:
        bstack11l1l1l1l1_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1ll1ll1_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ไ"):
          status = bstack1ll1ll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ๅ") if rep.outcome.lower() == bstack1ll1ll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧๆ") else bstack1ll1ll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ็")
          reason = bstack1ll1ll1_opy_ (u"่ࠩࠪ")
          if status == bstack1ll1ll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦ้ࠪ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1ll1ll1_opy_ (u"ࠫ࡮ࡴࡦࡰ๊ࠩ") if status == bstack1ll1ll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨ๋ࠬ") else bstack1ll1ll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ์")
          data = name + bstack1ll1ll1_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩํ") if status == bstack1ll1ll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ๎") else name + bstack1ll1ll1_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤࠬ๏") + reason
          bstack1lll1ll1l1_opy_ = bstack1lll11111_opy_(bstack1ll1ll1_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬ๐"), bstack1ll1ll1_opy_ (u"ࠫࠬ๑"), bstack1ll1ll1_opy_ (u"ࠬ࠭๒"), bstack1ll1ll1_opy_ (u"࠭ࠧ๓"), level, data)
          for driver in bstack1l1l1l1ll1_opy_:
            if bstack1l111l111_opy_ == driver.session_id:
              driver.execute_script(bstack1lll1ll1l1_opy_)
      except Exception as e:
        logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ๔").format(str(e)))
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬ๕").format(str(e)))
  bstack1l1l1ll1l_opy_(item, call, rep)
def bstack1l11lllll1_opy_(driver, bstack1111l1111_opy_, test=None):
  global bstack1ll11l111_opy_
  if test != None:
    bstack1l1l11111_opy_ = getattr(test, bstack1ll1ll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ๖"), None)
    bstack1llllll111_opy_ = getattr(test, bstack1ll1ll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ๗"), None)
    PercySDK.screenshot(driver, bstack1111l1111_opy_, bstack1l1l11111_opy_=bstack1l1l11111_opy_, bstack1llllll111_opy_=bstack1llllll111_opy_, bstack111lll11l1_opy_=bstack1ll11l111_opy_)
  else:
    PercySDK.screenshot(driver, bstack1111l1111_opy_)
@measure(event_name=EVENTS.bstack1ll11l1ll1_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack111ll1l1l1_opy_(driver):
  if bstack1111l1ll11_opy_.bstack1ll111lll_opy_() is True or bstack1111l1ll11_opy_.capturing() is True:
    return
  bstack1111l1ll11_opy_.bstack1ll11llll_opy_()
  while not bstack1111l1ll11_opy_.bstack1ll111lll_opy_():
    bstack1ll1llll11_opy_ = bstack1111l1ll11_opy_.bstack111l1lllll_opy_()
    bstack1l11lllll1_opy_(driver, bstack1ll1llll11_opy_)
  bstack1111l1ll11_opy_.bstack1lllll1l11_opy_()
def bstack1l11ll11ll_opy_(sequence, driver_command, response = None, bstack11ll111l11_opy_ = None, args = None):
    try:
      if sequence != bstack1ll1ll1_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫ๘"):
        return
      if percy.bstack1l111111l1_opy_() == bstack1ll1ll1_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦ๙"):
        return
      bstack1ll1llll11_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ๚"), None)
      for command in bstack111l1l1l1_opy_:
        if command == driver_command:
          with bstack11lll11l1l_opy_:
            bstack1lllllll1l_opy_ = bstack1l1l1l1ll1_opy_.copy()
          for driver in bstack1lllllll1l_opy_:
            bstack111ll1l1l1_opy_(driver)
      bstack1lll1111l1_opy_ = percy.bstack1l1l111lll_opy_()
      if driver_command in bstack11l1ll111l_opy_[bstack1lll1111l1_opy_]:
        bstack1111l1ll11_opy_.bstack1l1l11lll_opy_(bstack1ll1llll11_opy_, driver_command)
    except Exception as e:
      pass
def bstack111ll111ll_opy_(framework_name):
  if bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ๛")):
      return
  bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬ๜"), True)
  global bstack1l1ll1ll1l_opy_
  global bstack1llll1l11l_opy_
  global bstack111l1lll11_opy_
  bstack1l1ll1ll1l_opy_ = framework_name
  logger.info(bstack11l1l11ll1_opy_.format(bstack1l1ll1ll1l_opy_.split(bstack1ll1ll1_opy_ (u"ࠩ࠰ࠫ๝"))[0]))
  bstack1ll111111_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack111l1ll1ll_opy_:
      Service.start = bstack1ll1ll111l_opy_
      Service.stop = bstack11ll111111_opy_
      webdriver.Remote.get = bstack11ll1ll11_opy_
      WebDriver.quit = bstack1l1llll1l_opy_
      webdriver.Remote.__init__ = bstack1l1111l11_opy_
    if not bstack111l1ll1ll_opy_:
        webdriver.Remote.__init__ = bstack11111llll_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack1l11ll1l11_opy_
    bstack1llll1l11l_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack111l1ll1ll_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1ll1lll1ll_opy_
  except Exception as e:
    pass
  bstack1llll1llll_opy_()
  if not bstack1llll1l11l_opy_:
    bstack1l1l1lllll_opy_(bstack1ll1ll1_opy_ (u"ࠥࡔࡦࡩ࡫ࡢࡩࡨࡷࠥࡴ࡯ࡵࠢ࡬ࡲࡸࡺࡡ࡭࡮ࡨࡨࠧ๞"), bstack11ll1l11l_opy_)
  if bstack1ll11ll11_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack1ll1ll1_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ๟")) and callable(getattr(RemoteConnection, bstack1ll1ll1_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭๠"))):
        RemoteConnection._get_proxy_url = bstack11111lll1l_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack11111lll1l_opy_
    except Exception as e:
      logger.error(bstack1ll1111ll_opy_.format(str(e)))
  if bstack111ll11ll_opy_():
    bstack1111111ll_opy_(CONFIG, logger)
  if (bstack1ll1ll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ๡") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1l111111l1_opy_() == bstack1ll1ll1_opy_ (u"ࠢࡵࡴࡸࡩࠧ๢"):
          bstack11lll11l11_opy_(bstack1l11ll11ll_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1ll1llllll_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l11lll11l_opy_
      except Exception as e:
        logger.warn(bstack1l1ll11lll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1l1l11lll1_opy_
      except Exception as e:
        logger.debug(bstack1ll1l111l_opy_ + str(e))
    except Exception as e:
      bstack1l1l1lllll_opy_(e, bstack1l1ll11lll_opy_)
    Output.start_test = bstack11ll1l1l1l_opy_
    Output.end_test = bstack1ll1l11ll1_opy_
    TestStatus.__init__ = bstack11l1111111_opy_
    QueueItem.__init__ = bstack1l1l1lll1l_opy_
    pabot._create_items = bstack1l1l111ll1_opy_
    try:
      from pabot import __version__ as bstack1l1l1111l_opy_
      if version.parse(bstack1l1l1111l_opy_) >= version.parse(bstack1ll1ll1_opy_ (u"ࠨ࠷࠱࠴࠳࠶ࠧ๣")):
        pabot._run = bstack1111l111l1_opy_
      elif version.parse(bstack1l1l1111l_opy_) >= version.parse(bstack1ll1ll1_opy_ (u"ࠩ࠷࠲࠷࠴࠰ࠨ๤")):
        pabot._run = bstack11111111l_opy_
      elif version.parse(bstack1l1l1111l_opy_) >= version.parse(bstack1ll1ll1_opy_ (u"ࠪ࠶࠳࠷࠵࠯࠲ࠪ๥")):
        pabot._run = bstack11l1llll11_opy_
      elif version.parse(bstack1l1l1111l_opy_) >= version.parse(bstack1ll1ll1_opy_ (u"ࠫ࠷࠴࠱࠴࠰࠳ࠫ๦")):
        pabot._run = bstack1l1l1lll1_opy_
      else:
        pabot._run = bstack1ll1l1l111_opy_
    except Exception as e:
      pabot._run = bstack1ll1l1l111_opy_
    pabot._create_command_for_execution = bstack1ll11lll11_opy_
    pabot._report_results = bstack11lll1l1ll_opy_
  if bstack1ll1ll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ๧") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1l1lllll_opy_(e, bstack111ll1l11_opy_)
    Runner.run_hook = bstack1111111l1_opy_
    Step.run = bstack111lllll11_opy_
  if bstack1ll1ll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭๨") in str(framework_name).lower():
    if not bstack111l1ll1ll_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack11111lll1_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1ll11ll1l_opy_
      Config.getoption = bstack1l1lll1l1l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1l11l1l1l_opy_
    except Exception as e:
      pass
def bstack1l1l1l11l1_opy_():
  global CONFIG
  if bstack1ll1ll1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ๩") in CONFIG and int(CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ๪")]) > 1:
    logger.warn(bstack111l1111ll_opy_)
def bstack1l11111lll_opy_(arg, bstack1111lll1_opy_, bstack1llll11111_opy_=None):
  global CONFIG
  global bstack11111l1l1l_opy_
  global bstack11ll1l11l1_opy_
  global bstack111l1ll1ll_opy_
  global bstack11111l11_opy_
  bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ๫")
  if bstack1111lll1_opy_ and isinstance(bstack1111lll1_opy_, str):
    bstack1111lll1_opy_ = eval(bstack1111lll1_opy_)
  CONFIG = bstack1111lll1_opy_[bstack1ll1ll1_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪ๬")]
  bstack11111l1l1l_opy_ = bstack1111lll1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬ๭")]
  bstack11ll1l11l1_opy_ = bstack1111lll1_opy_[bstack1ll1ll1_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ๮")]
  bstack111l1ll1ll_opy_ = bstack1111lll1_opy_[bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩ๯")]
  bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ๰"), bstack111l1ll1ll_opy_)
  os.environ[bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ๱")] = bstack11l1lll1l1_opy_
  os.environ[bstack1ll1ll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠨ๲")] = json.dumps(CONFIG)
  os.environ[bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡋ࡙ࡇࡥࡕࡓࡎࠪ๳")] = bstack11111l1l1l_opy_
  os.environ[bstack1ll1ll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ๴")] = str(bstack11ll1l11l1_opy_)
  os.environ[bstack1ll1ll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫ๵")] = str(True)
  if bstack1111ll11l1_opy_(arg, [bstack1ll1ll1_opy_ (u"࠭࠭࡯ࠩ๶"), bstack1ll1ll1_opy_ (u"ࠧ࠮࠯ࡱࡹࡲࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ๷")]) != -1:
    os.environ[bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡃࡕࡅࡑࡒࡅࡍࠩ๸")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack11l111l11_opy_)
    return
  bstack11lllllll_opy_()
  global bstack111ll1l1l_opy_
  global bstack1ll11l111_opy_
  global bstack1ll11ll1ll_opy_
  global bstack11l1lll11l_opy_
  global bstack1ll111lll1_opy_
  global bstack111l1lll11_opy_
  global bstack1l1111111_opy_
  arg.append(bstack1ll1ll1_opy_ (u"ࠤ࠰࡛ࠧ๹"))
  arg.append(bstack1ll1ll1_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧ࠽ࡑࡴࡪࡵ࡭ࡧࠣࡥࡱࡸࡥࡢࡦࡼࠤ࡮ࡳࡰࡰࡴࡷࡩࡩࡀࡰࡺࡶࡨࡷࡹ࠴ࡐࡺࡶࡨࡷࡹ࡝ࡡࡳࡰ࡬ࡲ࡬ࠨ๺"))
  arg.append(bstack1ll1ll1_opy_ (u"ࠦ࠲࡝ࠢ๻"))
  arg.append(bstack1ll1ll1_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩ࠿࡚ࡨࡦࠢ࡫ࡳࡴࡱࡩ࡮ࡲ࡯ࠦ๼"))
  global bstack11ll1ll11l_opy_
  global bstack1ll1ll1ll1_opy_
  global bstack11ll11llll_opy_
  global bstack11l111ll1_opy_
  global bstack11lll111l1_opy_
  global bstack11l11ll11_opy_
  global bstack11l1l1ll1_opy_
  global bstack1ll1ll11l_opy_
  global bstack1l11ll1111_opy_
  global bstack1111l11ll1_opy_
  global bstack1ll1ll11l1_opy_
  global bstack1l111111l_opy_
  global bstack1l1l1ll1l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11ll1ll11l_opy_ = webdriver.Remote.__init__
    bstack1ll1ll1ll1_opy_ = WebDriver.quit
    bstack1ll1ll11l_opy_ = WebDriver.close
    bstack1l11ll1111_opy_ = WebDriver.get
    bstack11ll11llll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack11lll11lll_opy_(CONFIG) and bstack11lll11111_opy_():
    if bstack11lll11l1_opy_() < version.parse(bstack1l11ll11l1_opy_):
      logger.error(bstack11111lllll_opy_.format(bstack11lll11l1_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1ll1ll1_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ๽")) and callable(getattr(RemoteConnection, bstack1ll1ll1_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ๾"))):
          bstack1111l11ll1_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1111l11ll1_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack1ll1111ll_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1ll1ll11l1_opy_ = Config.getoption
    from _pytest import runner
    bstack1l111111l_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack111ll1ll_opy_)
  try:
    from pytest_bdd import reporting
    bstack1l1l1ll1l_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩ๿"))
  bstack1ll11ll1ll_opy_ = CONFIG.get(bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭຀"), {}).get(bstack1ll1ll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬກ"))
  bstack1l1111111_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack11111ll11l_opy_():
      bstack1ll11111l_opy_.invoke(Events.CONNECT, bstack111lll1l1_opy_())
    platform_index = int(os.environ.get(bstack1ll1ll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫຂ"), bstack1ll1ll1_opy_ (u"ࠬ࠶ࠧ຃")))
  else:
    bstack111ll111ll_opy_(bstack111l11ll1l_opy_)
  os.environ[bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧຄ")] = CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ຅")]
  os.environ[bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫຆ")] = CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬງ")]
  os.environ[bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ຈ")] = bstack111l1ll1ll_opy_.__str__()
  from _pytest.config import main as bstack1l11l1111l_opy_
  bstack1l11lll1l_opy_ = []
  try:
    exit_code = bstack1l11l1111l_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack11ll11lll_opy_()
    if bstack1ll1ll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨຉ") in multiprocessing.current_process().__dict__.keys():
      for bstack1l111l11ll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l11lll1l_opy_.append(bstack1l111l11ll_opy_)
    try:
      bstack11ll111lll_opy_ = (bstack1l11lll1l_opy_, int(exit_code))
      bstack1llll11111_opy_.append(bstack11ll111lll_opy_)
    except:
      bstack1llll11111_opy_.append((bstack1l11lll1l_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1l11lll1l_opy_.append({bstack1ll1ll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪຊ"): bstack1ll1ll1_opy_ (u"࠭ࡐࡳࡱࡦࡩࡸࡹࠠࠨ຋") + os.environ.get(bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧຌ")), bstack1ll1ll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧຍ"): traceback.format_exc(), bstack1ll1ll1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨຎ"): int(os.environ.get(bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪຏ")))})
    bstack1llll11111_opy_.append((bstack1l11lll1l_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack1ll1ll1_opy_ (u"ࠦࡷ࡫ࡴࡳ࡫ࡨࡷࠧຐ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack1111l1111l_opy_ = e.__class__.__name__
    print(bstack1ll1ll1_opy_ (u"ࠧࠫࡳ࠻ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡥࡩ࡭ࡧࡶࡦࠢࡷࡩࡸࡺࠠࠦࡵࠥຑ") % (bstack1111l1111l_opy_, e))
    return 1
def bstack1lll111ll_opy_(arg):
  global bstack11l11ll1l_opy_
  bstack111ll111ll_opy_(bstack11l1l11l1l_opy_)
  os.environ[bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧຒ")] = str(bstack11ll1l11l1_opy_)
  retries = bstack1llll111l_opy_.bstack111111l1_opy_(CONFIG)
  status_code = 0
  if bstack1llll111l_opy_.bstack11l1l11l_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack1l11lll111_opy_
    status_code = bstack1l11lll111_opy_(arg)
  if status_code != 0:
    bstack11l11ll1l_opy_ = status_code
def bstack111l11llll_opy_():
  logger.info(bstack1111lllll_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1ll1ll1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ຓ"), help=bstack1ll1ll1_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡦࡳࡳ࡬ࡩࡨࠩດ"))
  parser.add_argument(bstack1ll1ll1_opy_ (u"ࠩ࠰ࡹࠬຕ"), bstack1ll1ll1_opy_ (u"ࠪ࠱࠲ࡻࡳࡦࡴࡱࡥࡲ࡫ࠧຖ"), help=bstack1ll1ll1_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡷࡶࡩࡷࡴࡡ࡮ࡧࠪທ"))
  parser.add_argument(bstack1ll1ll1_opy_ (u"ࠬ࠳࡫ࠨຘ"), bstack1ll1ll1_opy_ (u"࠭࠭࠮࡭ࡨࡽࠬນ"), help=bstack1ll1ll1_opy_ (u"࡚ࠧࡱࡸࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡦࡩࡣࡦࡵࡶࠤࡰ࡫ࡹࠨບ"))
  parser.add_argument(bstack1ll1ll1_opy_ (u"ࠨ࠯ࡩࠫປ"), bstack1ll1ll1_opy_ (u"ࠩ࠰࠱࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧຜ"), help=bstack1ll1ll1_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩຝ"))
  bstack1111ll111_opy_ = parser.parse_args()
  try:
    bstack1111ll1lll_opy_ = bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡫ࡪࡴࡥࡳ࡫ࡦ࠲ࡾࡳ࡬࠯ࡵࡤࡱࡵࡲࡥࠨພ")
    if bstack1111ll111_opy_.framework and bstack1111ll111_opy_.framework not in (bstack1ll1ll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬຟ"), bstack1ll1ll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧຠ")):
      bstack1111ll1lll_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭ມ")
    bstack1111ll1l11_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1111ll1lll_opy_)
    bstack11l11111ll_opy_ = open(bstack1111ll1l11_opy_, bstack1ll1ll1_opy_ (u"ࠨࡴࠪຢ"))
    bstack1l1lll1111_opy_ = bstack11l11111ll_opy_.read()
    bstack11l11111ll_opy_.close()
    if bstack1111ll111_opy_.username:
      bstack1l1lll1111_opy_ = bstack1l1lll1111_opy_.replace(bstack1ll1ll1_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩຣ"), bstack1111ll111_opy_.username)
    if bstack1111ll111_opy_.key:
      bstack1l1lll1111_opy_ = bstack1l1lll1111_opy_.replace(bstack1ll1ll1_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬ຤"), bstack1111ll111_opy_.key)
    if bstack1111ll111_opy_.framework:
      bstack1l1lll1111_opy_ = bstack1l1lll1111_opy_.replace(bstack1ll1ll1_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬລ"), bstack1111ll111_opy_.framework)
    file_name = bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨ຦")
    file_path = os.path.abspath(file_name)
    bstack1l11111l11_opy_ = open(file_path, bstack1ll1ll1_opy_ (u"࠭ࡷࠨວ"))
    bstack1l11111l11_opy_.write(bstack1l1lll1111_opy_)
    bstack1l11111l11_opy_.close()
    logger.info(bstack1lll1lll11_opy_)
    try:
      os.environ[bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩຨ")] = bstack1111ll111_opy_.framework if bstack1111ll111_opy_.framework != None else bstack1ll1ll1_opy_ (u"ࠣࠤຩ")
      config = yaml.safe_load(bstack1l1lll1111_opy_)
      config[bstack1ll1ll1_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩສ")] = bstack1ll1ll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠰ࡷࡪࡺࡵࡱࠩຫ")
      bstack11l11111l1_opy_(bstack1ll1l11lll_opy_, config)
    except Exception as e:
      logger.debug(bstack1l1ll111l_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack111l111ll_opy_.format(str(e)))
def bstack11l11111l1_opy_(bstack1lll111111_opy_, config, bstack11l11ll1l1_opy_={}):
  global bstack111l1ll1ll_opy_
  global bstack1l11l1l11_opy_
  global bstack11111l11_opy_
  if not config:
    return
  bstack11l111111l_opy_ = bstack11ll11ll1l_opy_ if not bstack111l1ll1ll_opy_ else (
    bstack1111ll1ll1_opy_ if bstack1ll1ll1_opy_ (u"ࠫࡦࡶࡰࠨຬ") in config else (
        bstack1llll111ll_opy_ if config.get(bstack1ll1ll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩອ")) else bstack11l11lllll_opy_
    )
)
  bstack1l11l11111_opy_ = False
  bstack1ll1lll11_opy_ = False
  if bstack111l1ll1ll_opy_ is True:
      if bstack1ll1ll1_opy_ (u"࠭ࡡࡱࡲࠪຮ") in config:
          bstack1l11l11111_opy_ = True
      else:
          bstack1ll1lll11_opy_ = True
  bstack1ll1l1lll_opy_ = bstack1l1llll11l_opy_.bstack1l111l1111_opy_(config, bstack1l11l1l11_opy_)
  bstack1ll1111l1_opy_ = bstack1lll11111l_opy_()
  data = {
    bstack1ll1ll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩຯ"): config[bstack1ll1ll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪະ")],
    bstack1ll1ll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬັ"): config[bstack1ll1ll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭າ")],
    bstack1ll1ll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨຳ"): bstack1lll111111_opy_,
    bstack1ll1ll1_opy_ (u"ࠬࡪࡥࡵࡧࡦࡸࡪࡪࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩິ"): os.environ.get(bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨີ"), bstack1l11l1l11_opy_),
    bstack1ll1ll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩຶ"): bstack1l1l11ll1_opy_,
    bstack1ll1ll1_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮ࠪື"): bstack11ll1lllll_opy_(),
    bstack1ll1ll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷຸࠬ"): {
      bstack1ll1ll1_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨູ"): str(config[bstack1ll1ll1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨ຺ࠫ")]) if bstack1ll1ll1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬົ") in config else bstack1ll1ll1_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢຼ"),
      bstack1ll1ll1_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࡘࡨࡶࡸ࡯࡯࡯ࠩຽ"): sys.version,
      bstack1ll1ll1_opy_ (u"ࠨࡴࡨࡪࡪࡸࡲࡦࡴࠪ຾"): bstack1l11llll1l_opy_(os.environ.get(bstack1ll1ll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ຿"), bstack1l11l1l11_opy_)),
      bstack1ll1ll1_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬເ"): bstack1ll1ll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫແ"),
      bstack1ll1ll1_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ໂ"): bstack11l111111l_opy_,
      bstack1ll1ll1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫໃ"): bstack1ll1l1lll_opy_,
      bstack1ll1ll1_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡠࡷࡸ࡭ࡩ࠭ໄ"): os.environ[bstack1ll1ll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭໅")],
      bstack1ll1ll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬໆ"): os.environ.get(bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ໇"), bstack1l11l1l11_opy_),
      bstack1ll1ll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴ່ࠧ"): bstack1ll1llll1l_opy_(os.environ.get(bstack1ll1ll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ້ࠧ"), bstack1l11l1l11_opy_)),
      bstack1ll1ll1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯໊ࠬ"): bstack1ll1111l1_opy_.get(bstack1ll1ll1_opy_ (u"ࠧ࡯ࡣࡰࡩ໋ࠬ")),
      bstack1ll1ll1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ໌"): bstack1ll1111l1_opy_.get(bstack1ll1ll1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪໍ")),
      bstack1ll1ll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໎"): config[bstack1ll1ll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ໏")] if config[bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ໐")] else bstack1ll1ll1_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢ໑"),
      bstack1ll1ll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ໒"): str(config[bstack1ll1ll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໓")]) if bstack1ll1ll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ໔") in config else bstack1ll1ll1_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦ໕"),
      bstack1ll1ll1_opy_ (u"ࠫࡴࡹࠧ໖"): sys.platform,
      bstack1ll1ll1_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧ໗"): socket.gethostname(),
      bstack1ll1ll1_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ໘"): bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ໙"))
    }
  }
  if not bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ໚")) is None:
    data[bstack1ll1ll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໛")][bstack1ll1ll1_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡒ࡫ࡴࡢࡦࡤࡸࡦ࠭ໜ")] = {
      bstack1ll1ll1_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫໝ"): bstack1ll1ll1_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪໞ"),
      bstack1ll1ll1_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭ໟ"): bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ໠")),
      bstack1ll1ll1_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࡏࡷࡰࡦࡪࡸࠧ໡"): bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡑࡳࠬ໢"))
    }
  if bstack1lll111111_opy_ == bstack1ll11l1l1_opy_:
    data[bstack1ll1ll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໣")][bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡆࡳࡳ࡬ࡩࡨࠩ໤")] = bstack1l1lll1ll_opy_(config)
    data[bstack1ll1ll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ໥")][bstack1ll1ll1_opy_ (u"࠭ࡩࡴࡒࡨࡶࡨࡿࡁࡶࡶࡲࡉࡳࡧࡢ࡭ࡧࡧࠫ໦")] = percy.bstack111l1ll1l_opy_
    data[bstack1ll1ll1_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ໧")][bstack1ll1ll1_opy_ (u"ࠨࡲࡨࡶࡨࡿࡂࡶ࡫࡯ࡨࡎࡪࠧ໨")] = percy.percy_build_id
  if not bstack1llll111l_opy_.bstack1ll1lll11l_opy_(CONFIG):
    data[bstack1ll1ll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໩")][bstack1ll1ll1_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠧ໪")] = bstack1llll111l_opy_.bstack1ll1lll11l_opy_(CONFIG)
  bstack1111111l_opy_ = bstack1lll1lll1_opy_.bstack1llllllll_opy_(CONFIG, logger)
  bstack111l1lll_opy_ = bstack1llll111l_opy_.bstack1llllllll_opy_(config=CONFIG)
  if bstack1111111l_opy_ is not None and bstack111l1lll_opy_ is not None and bstack111l1lll_opy_.bstack1lllll1ll_opy_():
    data[bstack1ll1ll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ໫")][bstack111l1lll_opy_.bstack1lll11ll11_opy_()] = bstack1111111l_opy_.bstack1ll11l11l_opy_()
  update(data[bstack1ll1ll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ໬")], bstack11l11ll1l1_opy_)
  try:
    response = bstack111l1l11l1_opy_(bstack1ll1ll1_opy_ (u"࠭ࡐࡐࡕࡗࠫ໭"), bstack111l11l111_opy_(bstack1l1lll1lll_opy_), data, {
      bstack1ll1ll1_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ໮"): (config[bstack1ll1ll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ໯")], config[bstack1ll1ll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ໰")])
    })
    if response:
      logger.debug(bstack1lll11lll_opy_.format(bstack1lll111111_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11llll111l_opy_.format(str(e)))
def bstack1l11llll1l_opy_(framework):
  return bstack1ll1ll1_opy_ (u"ࠥࡿࢂ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࢀࢃࠢ໱").format(str(framework), __version__) if framework else bstack1ll1ll1_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧ໲").format(
    __version__)
def bstack11lllllll_opy_():
  global CONFIG
  global bstack1l1ll1l1l1_opy_
  if bool(CONFIG):
    return
  try:
    bstack111lll1lll_opy_()
    logger.debug(bstack11111ll111_opy_.format(str(CONFIG)))
    bstack1l1ll1l1l1_opy_ = bstack1l1l1ll111_opy_.configure_logger(CONFIG, bstack1l1ll1l1l1_opy_)
    bstack1ll111111_opy_()
  except Exception as e:
    logger.error(bstack1ll1ll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࠤ໳") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1111llll1l_opy_
  atexit.register(bstack1l1ll11ll_opy_)
  signal.signal(signal.SIGINT, bstack1lllll1111_opy_)
  signal.signal(signal.SIGTERM, bstack1lllll1111_opy_)
def bstack1111llll1l_opy_(exctype, value, traceback):
  global bstack1l1l1l1ll1_opy_
  try:
    for driver in bstack1l1l1l1ll1_opy_:
      bstack11lll11ll1_opy_(driver, bstack1ll1ll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭໴"), bstack1ll1ll1_opy_ (u"ࠢࡔࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥ໵") + str(value))
  except Exception:
    pass
  logger.info(bstack1l111lllll_opy_)
  bstack1l1ll1ll1_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l1ll1ll1_opy_(message=bstack1ll1ll1_opy_ (u"ࠨࠩ໶"), bstack1l1ll11ll1_opy_ = False):
  global CONFIG
  bstack11lll111l_opy_ = bstack1ll1ll1_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡇࡻࡧࡪࡶࡴࡪࡱࡱࠫ໷") if bstack1l1ll11ll1_opy_ else bstack1ll1ll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ໸")
  try:
    if message:
      bstack11l11ll1l1_opy_ = {
        bstack11lll111l_opy_ : str(message)
      }
      bstack11l11111l1_opy_(bstack1ll11l1l1_opy_, CONFIG, bstack11l11ll1l1_opy_)
    else:
      bstack11l11111l1_opy_(bstack1ll11l1l1_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1ll11ll1l1_opy_.format(str(e)))
def bstack1lll1l1l1l_opy_(bstack111l11lll_opy_, size):
  bstack11l1ll1l1l_opy_ = []
  while len(bstack111l11lll_opy_) > size:
    bstack11l1l11111_opy_ = bstack111l11lll_opy_[:size]
    bstack11l1ll1l1l_opy_.append(bstack11l1l11111_opy_)
    bstack111l11lll_opy_ = bstack111l11lll_opy_[size:]
  bstack11l1ll1l1l_opy_.append(bstack111l11lll_opy_)
  return bstack11l1ll1l1l_opy_
def bstack1l1l11l1l1_opy_(args):
  if bstack1ll1ll1_opy_ (u"ࠫ࠲ࡳࠧ໹") in args and bstack1ll1ll1_opy_ (u"ࠬࡶࡤࡣࠩ໺") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack111l1l1111_opy_, stage=STAGE.bstack11llll1111_opy_)
def run_on_browserstack(bstack1l1l11l1l_opy_=None, bstack1llll11111_opy_=None, bstack1ll1111111_opy_=False):
  global CONFIG
  global bstack11111l1l1l_opy_
  global bstack11ll1l11l1_opy_
  global bstack1l11l1l11_opy_
  global bstack11111l11_opy_
  bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"࠭ࠧ໻")
  bstack11lll1ll1l_opy_(bstack11llllll1_opy_, logger)
  if bstack1l1l11l1l_opy_ and isinstance(bstack1l1l11l1l_opy_, str):
    bstack1l1l11l1l_opy_ = eval(bstack1l1l11l1l_opy_)
  if bstack1l1l11l1l_opy_:
    CONFIG = bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧ໼")]
    bstack11111l1l1l_opy_ = bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩ໽")]
    bstack11ll1l11l1_opy_ = bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ໾")]
    bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ໿"), bstack11ll1l11l1_opy_)
    bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫༀ")
  bstack11111l11_opy_.set_property(bstack1ll1ll1_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ༁"), uuid4().__str__())
  logger.info(bstack1ll1ll1_opy_ (u"࠭ࡓࡅࡍࠣࡶࡺࡴࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡩࡥ࠼ࠣࠫ༂") + bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ༃")));
  logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࡀࠫ༄") + bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ༅")))
  if not bstack1ll1111111_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack11l111l11_opy_)
      return
    if sys.argv[1] == bstack1ll1ll1_opy_ (u"ࠪ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ࠭༆") or sys.argv[1] == bstack1ll1ll1_opy_ (u"ࠫ࠲ࡼࠧ༇"):
      logger.info(bstack1ll1ll1_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡕࡿࡴࡩࡱࡱࠤࡘࡊࡋࠡࡸࡾࢁࠬ༈").format(__version__))
      return
    if sys.argv[1] == bstack1ll1ll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ༉"):
      bstack111l11llll_opy_()
      return
  args = sys.argv
  bstack11lllllll_opy_()
  global bstack111ll1l1l_opy_
  global bstack1l1l1llll1_opy_
  global bstack1l1111111_opy_
  global bstack11l1111ll_opy_
  global bstack1ll11l111_opy_
  global bstack1ll11ll1ll_opy_
  global bstack11l1lll11l_opy_
  global bstack11l1l1111_opy_
  global bstack1ll111lll1_opy_
  global bstack111l1lll11_opy_
  global bstack111ll11l11_opy_
  bstack1l1l1llll1_opy_ = len(CONFIG.get(bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ༊"), []))
  if not bstack11l1lll1l1_opy_:
    if args[1] == bstack1ll1ll1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ་") or args[1] == bstack1ll1ll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ༌"):
      bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ།")
      args = args[2:]
    elif args[1] == bstack1ll1ll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༎"):
      bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༏")
      args = args[2:]
    elif args[1] == bstack1ll1ll1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ༐"):
      bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭༑")
      args = args[2:]
    elif args[1] == bstack1ll1ll1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ༒"):
      bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ༓")
      args = args[2:]
    elif args[1] == bstack1ll1ll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ༔"):
      bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༕")
      args = args[2:]
    elif args[1] == bstack1ll1ll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ༖"):
      bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭༗")
      args = args[2:]
    else:
      if not bstack1ll1ll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭༘ࠪ") in CONFIG or str(CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮༙ࠫ")]).lower() in [bstack1ll1ll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༚"), bstack1ll1ll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫ༛")]:
        bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༜")
        args = args[1:]
      elif str(CONFIG[bstack1ll1ll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ༝")]).lower() == bstack1ll1ll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ༞"):
        bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭༟")
        args = args[1:]
      elif str(CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ༠")]).lower() == bstack1ll1ll1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༡"):
        bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ༢")
        args = args[1:]
      elif str(CONFIG[bstack1ll1ll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ༣")]).lower() == bstack1ll1ll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ༤"):
        bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭༥")
        args = args[1:]
      elif str(CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༦")]).lower() == bstack1ll1ll1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ༧"):
        bstack11l1lll1l1_opy_ = bstack1ll1ll1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ༨")
        args = args[1:]
      else:
        os.environ[bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ༩")] = bstack11l1lll1l1_opy_
        bstack1lll11l1l1_opy_(bstack111l1ll11_opy_)
  os.environ[bstack1ll1ll1_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬ༪")] = bstack11l1lll1l1_opy_
  bstack1l11l1l11_opy_ = bstack11l1lll1l1_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1ll1l1ll1l_opy_ = bstack1ll1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘ࠲ࡈࡄࡅࠩ༫")] if bstack11l1lll1l1_opy_ == bstack1ll1ll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭༬") and bstack1llllll1l1_opy_() else bstack11l1lll1l1_opy_
      bstack1ll11111l_opy_.invoke(Events.bstack11l111ll1l_opy_, bstack11lll1111_opy_(
        sdk_version=__version__,
        path_config=bstack1111l11lll_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1ll1l1ll1l_opy_,
        frameworks=[bstack1ll1l1ll1l_opy_],
        framework_versions={
          bstack1ll1l1ll1l_opy_: bstack1ll1llll1l_opy_(bstack1ll1ll1_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭༭") if bstack11l1lll1l1_opy_ in [bstack1ll1ll1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ༮"), bstack1ll1ll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ༯"), bstack1ll1ll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ༰")] else bstack11l1lll1l1_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack1ll1ll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨ༱"), None):
        CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢ༲")] = cli.config.get(bstack1ll1ll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ༳"), None)
    except Exception as e:
      bstack1ll11111l_opy_.invoke(Events.bstack11l11l1ll_opy_, e.__traceback__, 1)
    if bstack11ll1l11l1_opy_:
      CONFIG[bstack1ll1ll1_opy_ (u"ࠢࡢࡲࡳࠦ༴")] = cli.config[bstack1ll1ll1_opy_ (u"ࠣࡣࡳࡴ༵ࠧ")]
      logger.info(bstack11111ll1ll_opy_.format(CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡤࡴࡵ࠭༶")]))
  else:
    bstack1ll11111l_opy_.clear()
  global bstack1111ll1l1_opy_
  global bstack1l1ll111l1_opy_
  if bstack1l1l11l1l_opy_:
    try:
      bstack111lllll1_opy_ = datetime.datetime.now()
      os.environ[bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏ༷ࠬ")] = bstack11l1lll1l1_opy_
      bstack11l11111l1_opy_(bstack1lll111ll1_opy_, CONFIG)
      cli.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡶࡨࡰࡥࡴࡦࡵࡷࡣࡦࡺࡴࡦ࡯ࡳࡸࡪࡪࠢ༸"), datetime.datetime.now() - bstack111lllll1_opy_)
    except Exception as e:
      logger.debug(bstack11ll1l1ll1_opy_.format(str(e)))
  global bstack11ll1ll11l_opy_
  global bstack1ll1ll1ll1_opy_
  global bstack111ll111l_opy_
  global bstack111l111l1l_opy_
  global bstack111l11l1l_opy_
  global bstack1l11lll11_opy_
  global bstack11l111ll1_opy_
  global bstack11lll111l1_opy_
  global bstack1ll1l111ll_opy_
  global bstack11l11ll11_opy_
  global bstack11l1l1ll1_opy_
  global bstack1ll1ll11l_opy_
  global bstack1lllll1lll_opy_
  global bstack1ll1llll1_opy_
  global bstack1l11ll1111_opy_
  global bstack1111l11ll1_opy_
  global bstack1ll1ll11l1_opy_
  global bstack1l111111l_opy_
  global bstack1ll1ll1l11_opy_
  global bstack1l1l1ll1l_opy_
  global bstack11ll11llll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11ll1ll11l_opy_ = webdriver.Remote.__init__
    bstack1ll1ll1ll1_opy_ = WebDriver.quit
    bstack1ll1ll11l_opy_ = WebDriver.close
    bstack1l11ll1111_opy_ = WebDriver.get
    bstack11ll11llll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1111ll1l1_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack11111l1lll_opy_
    bstack1l1ll111l1_opy_ = bstack11111l1lll_opy_()
  except Exception as e:
    pass
  try:
    global bstack111l11l11l_opy_
    from QWeb.keywords import browser
    bstack111l11l11l_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack11lll11lll_opy_(CONFIG) and bstack11lll11111_opy_():
    if bstack11lll11l1_opy_() < version.parse(bstack1l11ll11l1_opy_):
      logger.error(bstack11111lllll_opy_.format(bstack11lll11l1_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1ll1ll1_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ༹࠭")) and callable(getattr(RemoteConnection, bstack1ll1ll1_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ༺"))):
          RemoteConnection._get_proxy_url = bstack11111lll1l_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack11111lll1l_opy_
      except Exception as e:
        logger.error(bstack1ll1111ll_opy_.format(str(e)))
  if not CONFIG.get(bstack1ll1ll1_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩ༻"), False) and not bstack1l1l11l1l_opy_:
    logger.info(bstack1l11ll111_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack1ll1ll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ༼") in CONFIG and str(CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭༽")]).lower() != bstack1ll1ll1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ༾"):
      bstack1l111l1l1_opy_()
    elif bstack11l1lll1l1_opy_ != bstack1ll1ll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༿") or (bstack11l1lll1l1_opy_ == bstack1ll1ll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬཀ") and not bstack1l1l11l1l_opy_):
      bstack111l11111_opy_()
  if (bstack11l1lll1l1_opy_ in [bstack1ll1ll1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬཁ"), bstack1ll1ll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ག"), bstack1ll1ll1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩགྷ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1ll1llllll_opy_
        bstack1l11lll11_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1l1ll11lll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack111l11l1l_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1ll1l111l_opy_ + str(e))
    except Exception as e:
      bstack1l1l1lllll_opy_(e, bstack1l1ll11lll_opy_)
    if bstack11l1lll1l1_opy_ != bstack1ll1ll1_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪང"):
      bstack1111l11l1l_opy_()
    bstack111ll111l_opy_ = Output.start_test
    bstack111l111l1l_opy_ = Output.end_test
    bstack11l111ll1_opy_ = TestStatus.__init__
    bstack1ll1l111ll_opy_ = pabot._run
    bstack11l11ll11_opy_ = QueueItem.__init__
    bstack11l1l1ll1_opy_ = pabot._create_command_for_execution
    bstack1ll1ll1l11_opy_ = pabot._report_results
  if bstack11l1lll1l1_opy_ == bstack1ll1ll1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪཅ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1l1lllll_opy_(e, bstack111ll1l11_opy_)
    bstack1lllll1lll_opy_ = Runner.run_hook
    bstack1ll1llll1_opy_ = Step.run
  if bstack11l1lll1l1_opy_ == bstack1ll1ll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫཆ"):
    try:
      from _pytest.config import Config
      bstack1ll1ll11l1_opy_ = Config.getoption
      from _pytest import runner
      bstack1l111111l_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack111ll1ll_opy_)
    try:
      from pytest_bdd import reporting
      bstack1l1l1ll1l_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1ll1ll1_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡴࠦࡲࡶࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࡸ࠭ཇ"))
  try:
    framework_name = bstack1ll1ll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ཈") if bstack11l1lll1l1_opy_ in [bstack1ll1ll1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ཉ"), bstack1ll1ll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧཊ"), bstack1ll1ll1_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪཋ")] else bstack111l1111l_opy_(bstack11l1lll1l1_opy_)
    bstack1ll1ll1l1l_opy_ = {
      bstack1ll1ll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࠫཌ"): bstack1ll1ll1_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭ཌྷ") if bstack11l1lll1l1_opy_ == bstack1ll1ll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཎ") and bstack1llllll1l1_opy_() else framework_name,
      bstack1ll1ll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪཏ"): bstack1ll1llll1l_opy_(framework_name),
      bstack1ll1ll1_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬཐ"): __version__,
      bstack1ll1ll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩད"): bstack11l1lll1l1_opy_
    }
    if bstack11l1lll1l1_opy_ in bstack1ll11llll1_opy_ + bstack11l1l11l1_opy_:
      if bstack11111ll1_opy_.bstack11ll1lll1_opy_(CONFIG):
        if bstack1ll1ll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩདྷ") in CONFIG:
          os.environ[bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫན")] = os.getenv(bstack1ll1ll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬཔ"), json.dumps(CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬཕ")]))
          CONFIG[bstack1ll1ll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭བ")].pop(bstack1ll1ll1_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬབྷ"), None)
          CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨམ")].pop(bstack1ll1ll1_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧཙ"), None)
        bstack1ll1ll1l1l_opy_[bstack1ll1ll1_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪཚ")] = {
          bstack1ll1ll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩཛ"): bstack1ll1ll1_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧཛྷ"),
          bstack1ll1ll1_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧཝ"): str(bstack11lll11l1_opy_())
        }
    if bstack11l1lll1l1_opy_ not in [bstack1ll1ll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨཞ")] and not cli.is_running():
      bstack11l1l11lll_opy_, bstack1l11l1l1ll_opy_ = bstack1ll111ll_opy_.launch(CONFIG, bstack1ll1ll1l1l_opy_)
      if bstack1l11l1l1ll_opy_.get(bstack1ll1ll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨཟ")) is not None and bstack11111ll1_opy_.bstack1ll111ll1l_opy_(CONFIG) is None:
        value = bstack1l11l1l1ll_opy_[bstack1ll1ll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩའ")].get(bstack1ll1ll1_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫཡ"))
        if value is not None:
            CONFIG[bstack1ll1ll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫར")] = value
        else:
          logger.debug(bstack1ll1ll1_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡦࡤࡸࡦࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥལ"))
  except Exception as e:
    logger.debug(bstack11ll1l111l_opy_.format(bstack1ll1ll1_opy_ (u"࠭ࡔࡦࡵࡷࡌࡺࡨࠧཤ"), str(e)))
  if bstack11l1lll1l1_opy_ == bstack1ll1ll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧཥ"):
    bstack1l1111111_opy_ = True
    if bstack1l1l11l1l_opy_ and bstack1ll1111111_opy_:
      bstack1ll11ll1ll_opy_ = CONFIG.get(bstack1ll1ll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬས"), {}).get(bstack1ll1ll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫཧ"))
      bstack111ll111ll_opy_(bstack1l11l11ll_opy_)
    elif bstack1l1l11l1l_opy_:
      bstack1ll11ll1ll_opy_ = CONFIG.get(bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧཨ"), {}).get(bstack1ll1ll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ཀྵ"))
      global bstack1l1l1l1ll1_opy_
      try:
        if bstack1l1l11l1l1_opy_(bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཪ")]) and multiprocessing.current_process().name == bstack1ll1ll1_opy_ (u"࠭࠰ࠨཫ"):
          bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪཬ")].remove(bstack1ll1ll1_opy_ (u"ࠨ࠯ࡰࠫ཭"))
          bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ཮")].remove(bstack1ll1ll1_opy_ (u"ࠪࡴࡩࡨࠧ཯"))
          bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ཰")] = bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཱ")][0]
          with open(bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦིࠩ")], bstack1ll1ll1_opy_ (u"ࠧࡳཱིࠩ")) as f:
            file_content = f.read()
          bstack11l1l111l1_opy_ = bstack1ll1ll1_opy_ (u"ࠣࠤࠥࡪࡷࡵ࡭ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡦ࡮ࠤ࡮ࡳࡰࡰࡴࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫࠻ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨࠬࢀࢃࠩ࠼ࠢࡩࡶࡴࡳࠠࡱࡦࡥࠤ࡮ࡳࡰࡰࡴࡷࠤࡕࡪࡢ࠼ࠢࡲ࡫ࡤࡪࡢࠡ࠿ࠣࡔࡩࡨ࠮ࡥࡱࡢࡦࡷ࡫ࡡ࡬࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡤࡦࡨࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰ࠮ࡳࡦ࡮ࡩ࠰ࠥࡧࡲࡨ࠮ࠣࡸࡪࡳࡰࡰࡴࡤࡶࡾࠦ࠽ࠡ࠲ࠬ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡸࡷࡿ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡣࡵ࡫ࠥࡃࠠࡴࡶࡵࠬ࡮ࡴࡴࠩࡣࡵ࡫࠮࠱࠱࠱ࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡧࡻࡧࡪࡶࡴࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡦࡹࠠࡦ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡴࡦࡹࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡯ࡨࡡࡧࡦ࠭ࡹࡥ࡭ࡨ࠯ࡥࡷ࡭ࠬࡵࡧࡰࡴࡴࡸࡡࡳࡻࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡑࡦࡥ࠲ࡩࡵ࡟ࡣࠢࡀࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡔࡩࡨ࠮ࡥࡱࡢࡦࡷ࡫ࡡ࡬ࠢࡀࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡔࡩࡨࠨࠪ࠰ࡶࡩࡹࡥࡴࡳࡣࡦࡩ࠭࠯࡜࡯ࠤུࠥࠦ").format(str(bstack1l1l11l1l_opy_))
          bstack11llll111_opy_ = bstack11l1l111l1_opy_ + file_content
          bstack1l1lll1ll1_opy_ = bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩཱུࠬ")] + bstack1ll1ll1_opy_ (u"ࠪࡣࡧࡹࡴࡢࡥ࡮ࡣࡹ࡫࡭ࡱ࠰ࡳࡽࠬྲྀ")
          with open(bstack1l1lll1ll1_opy_, bstack1ll1ll1_opy_ (u"ࠫࡼ࠭ཷ")):
            pass
          with open(bstack1l1lll1ll1_opy_, bstack1ll1ll1_opy_ (u"ࠧࡽࠫࠣླྀ")) as f:
            f.write(bstack11llll111_opy_)
          import subprocess
          process_data = subprocess.run([bstack1ll1ll1_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࠨཹ"), bstack1l1lll1ll1_opy_])
          if os.path.exists(bstack1l1lll1ll1_opy_):
            os.unlink(bstack1l1lll1ll1_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack1l1l11l1l1_opy_(bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧེࠪ")]):
            bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨཻࠫ")].remove(bstack1ll1ll1_opy_ (u"ࠩ࠰ࡱོࠬ"))
            bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪཽ࠭")].remove(bstack1ll1ll1_opy_ (u"ࠫࡵࡪࡢࠨཾ"))
            bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཿ")] = bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦྀࠩ")][0]
          bstack111ll111ll_opy_(bstack1l11l11ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧཱྀࠪ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1ll1ll1_opy_ (u"ࠨࡡࡢࡲࡦࡳࡥࡠࡡࠪྂ")] = bstack1ll1ll1_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫྃ")
          mod_globals[bstack1ll1ll1_opy_ (u"ࠪࡣࡤ࡬ࡩ࡭ࡧࡢࡣ྄ࠬ")] = os.path.abspath(bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ྅")])
          exec(open(bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ྆")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1ll1ll1_opy_ (u"࠭ࡃࡢࡷࡪ࡬ࡹࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂ࠭྇").format(str(e)))
          for driver in bstack1l1l1l1ll1_opy_:
            bstack1llll11111_opy_.append({
              bstack1ll1ll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬྈ"): bstack1l1l11l1l_opy_[bstack1ll1ll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྉ")],
              bstack1ll1ll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨྊ"): str(e),
              bstack1ll1ll1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩྋ"): multiprocessing.current_process().name
            })
            bstack11lll11ll1_opy_(driver, bstack1ll1ll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫྌ"), bstack1ll1ll1_opy_ (u"࡙ࠧࡥࡴࡵ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣྍ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l1l1l1ll1_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11ll1l11l1_opy_, CONFIG, logger)
      bstack11ll11ll1_opy_()
      bstack1l1l1l11l1_opy_()
      percy.bstack1l111l1ll1_opy_()
      bstack1111lll1_opy_ = {
        bstack1ll1ll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྎ"): args[0],
        bstack1ll1ll1_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧྏ"): CONFIG,
        bstack1ll1ll1_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩྐ"): bstack11111l1l1l_opy_,
        bstack1ll1ll1_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫྑ"): bstack11ll1l11l1_opy_
      }
      if bstack1ll1ll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྒ") in CONFIG:
        bstack1llll11lll_opy_ = bstack111lll1l11_opy_(args, logger, CONFIG, bstack111l1ll1ll_opy_, bstack1l1l1llll1_opy_)
        bstack11l1l1111_opy_ = bstack1llll11lll_opy_.bstack111llll1_opy_(run_on_browserstack, bstack1111lll1_opy_, bstack1l1l11l1l1_opy_(args))
      else:
        if bstack1l1l11l1l1_opy_(args):
          bstack1111lll1_opy_[bstack1ll1ll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྒྷ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1111lll1_opy_,))
          test.start()
          test.join()
        else:
          bstack111ll111ll_opy_(bstack1l11l11ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1ll1ll1_opy_ (u"ࠬࡥ࡟࡯ࡣࡰࡩࡤࡥࠧྔ")] = bstack1ll1ll1_opy_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨྕ")
          mod_globals[bstack1ll1ll1_opy_ (u"ࠧࡠࡡࡩ࡭ࡱ࡫࡟ࡠࠩྖ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack11l1lll1l1_opy_ == bstack1ll1ll1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧྗ") or bstack11l1lll1l1_opy_ == bstack1ll1ll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ྘"):
    percy.init(bstack11ll1l11l1_opy_, CONFIG, logger)
    percy.bstack1l111l1ll1_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l1l1lllll_opy_(e, bstack1l1ll11lll_opy_)
    bstack11ll11ll1_opy_()
    bstack111ll111ll_opy_(bstack1ll11l11l1_opy_)
    if bstack111l1ll1ll_opy_:
      bstack1l111l1l1l_opy_(bstack1ll11l11l1_opy_, args)
      if bstack1ll1ll1_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨྙ") in args:
        i = args.index(bstack1ll1ll1_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩྚ"))
        args.pop(i)
        args.pop(i)
      if bstack1ll1ll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨྛ") not in CONFIG:
        CONFIG[bstack1ll1ll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩྜ")] = [{}]
        bstack1l1l1llll1_opy_ = 1
      if bstack111ll1l1l_opy_ == 0:
        bstack111ll1l1l_opy_ = 1
      args.insert(0, str(bstack111ll1l1l_opy_))
      args.insert(0, str(bstack1ll1ll1_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬྜྷ")))
    if bstack1ll111ll_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1l1l1l1lll_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1l1lll1l11_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1ll1ll1_opy_ (u"ࠣࡔࡒࡆࡔ࡚࡟ࡐࡒࡗࡍࡔࡔࡓࠣྞ"),
        ).parse_args(bstack1l1l1l1lll_opy_)
        bstack11llll1lll_opy_ = args.index(bstack1l1l1l1lll_opy_[0]) if len(bstack1l1l1l1lll_opy_) > 0 else len(args)
        args.insert(bstack11llll1lll_opy_, str(bstack1ll1ll1_opy_ (u"ࠩ࠰࠱ࡱ࡯ࡳࡵࡧࡱࡩࡷ࠭ྟ")))
        args.insert(bstack11llll1lll_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll1ll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡶࡴࡨ࡯ࡵࡡ࡯࡭ࡸࡺࡥ࡯ࡧࡵ࠲ࡵࡿࠧྠ"))))
        if bstack1llll111l_opy_.bstack11l1l11l_opy_(CONFIG):
          args.insert(bstack11llll1lll_opy_, str(bstack1ll1ll1_opy_ (u"ࠫ࠲࠳࡬ࡪࡵࡷࡩࡳ࡫ࡲࠨྡ")))
          args.insert(bstack11llll1lll_opy_ + 1, str(bstack1ll1ll1_opy_ (u"ࠬࡘࡥࡵࡴࡼࡊࡦ࡯࡬ࡦࡦ࠽ࡿࢂ࠭ྡྷ").format(bstack1llll111l_opy_.bstack111111l1_opy_(CONFIG))))
        if bstack1ll1l1llll_opy_(os.environ.get(bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠫྣ"))) and str(os.environ.get(bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠫྤ"), bstack1ll1ll1_opy_ (u"ࠨࡰࡸࡰࡱ࠭ྥ"))) != bstack1ll1ll1_opy_ (u"ࠩࡱࡹࡱࡲࠧྦ"):
          for bstack1l1ll1l11l_opy_ in bstack1l1lll1l11_opy_:
            args.remove(bstack1l1ll1l11l_opy_)
          test_files = os.environ.get(bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧྦྷ")).split(bstack1ll1ll1_opy_ (u"ࠫ࠱࠭ྨ"))
          for bstack11111lll_opy_ in test_files:
            args.append(bstack11111lll_opy_)
      except Exception as e:
        logger.error(bstack1ll1ll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡥࡹࡺࡡࡤࡪ࡬ࡲ࡬ࠦ࡬ࡪࡵࡷࡩࡳ࡫ࡲࠡࡨࡲࡶࠥࢁࡽ࠯ࠢࡈࡶࡷࡵࡲࠡ࠯ࠣࡿࢂࠨྩ").format(bstack1ll1l11ll_opy_, e))
    pabot.main(args)
  elif bstack11l1lll1l1_opy_ == bstack1ll1ll1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧྪ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l1l1lllll_opy_(e, bstack1l1ll11lll_opy_)
    for a in args:
      if bstack1ll1ll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭ྫ") in a:
        bstack1ll11l111_opy_ = int(a.split(bstack1ll1ll1_opy_ (u"ࠨ࠼ࠪྫྷ"))[1])
      if bstack1ll1ll1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ྭ") in a:
        bstack1ll11ll1ll_opy_ = str(a.split(bstack1ll1ll1_opy_ (u"ࠪ࠾ࠬྮ"))[1])
      if bstack1ll1ll1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫྯ") in a:
        bstack11l1lll11l_opy_ = str(a.split(bstack1ll1ll1_opy_ (u"ࠬࡀࠧྰ"))[1])
    bstack1l111ll11_opy_ = None
    if bstack1ll1ll1_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬྱ") in args:
      i = args.index(bstack1ll1ll1_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭ྲ"))
      args.pop(i)
      bstack1l111ll11_opy_ = args.pop(i)
    if bstack1l111ll11_opy_ is not None:
      global bstack1l1ll1l11_opy_
      bstack1l1ll1l11_opy_ = bstack1l111ll11_opy_
    bstack111ll111ll_opy_(bstack1ll11l11l1_opy_)
    run_cli(args)
    if bstack1ll1ll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬླ") in multiprocessing.current_process().__dict__.keys():
      for bstack1l111l11ll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1llll11111_opy_.append(bstack1l111l11ll_opy_)
  elif bstack11l1lll1l1_opy_ == bstack1ll1ll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩྴ"):
    bstack1l11llllll_opy_ = bstack1llll1l11_opy_(args, logger, CONFIG, bstack111l1ll1ll_opy_)
    bstack1l11llllll_opy_.bstack11111111_opy_()
    bstack11ll11ll1_opy_()
    bstack11l1111ll_opy_ = True
    bstack111l1lll11_opy_ = bstack1l11llllll_opy_.bstack1111llll_opy_()
    bstack1l11llllll_opy_.bstack1111lll1_opy_(bstack1lll1llll1_opy_)
    bstack1l11llllll_opy_.bstack1lllll11l_opy_()
    bstack1ll11l1ll_opy_(bstack11l1lll1l1_opy_, CONFIG, bstack1l11llllll_opy_.bstack111l11l1_opy_())
    bstack1l111ll1ll_opy_ = bstack1l11llllll_opy_.bstack111llll1_opy_(bstack1l11111lll_opy_, {
      bstack1ll1ll1_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫྵ"): bstack11111l1l1l_opy_,
      bstack1ll1ll1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ྶ"): bstack11ll1l11l1_opy_,
      bstack1ll1ll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨྷ"): bstack111l1ll1ll_opy_
    })
    try:
      bstack1l11lll1l_opy_, bstack11lll1lll1_opy_ = map(list, zip(*bstack1l111ll1ll_opy_))
      bstack1ll111lll1_opy_ = bstack1l11lll1l_opy_[0]
      for status_code in bstack11lll1lll1_opy_:
        if status_code != 0:
          bstack111ll11l11_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1ll1ll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡦࡴࡵࡳࡷࡹࠠࡢࡰࡧࠤࡸࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠰ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠺ࠡࡽࢀࠦྸ").format(str(e)))
  elif bstack11l1lll1l1_opy_ == bstack1ll1ll1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧྐྵ"):
    try:
      from behave.__main__ import main as bstack1l11lll111_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l1l1lllll_opy_(e, bstack111ll1l11_opy_)
    bstack11ll11ll1_opy_()
    bstack11l1111ll_opy_ = True
    bstack111l1l11_opy_ = 1
    if bstack1ll1ll1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨྺ") in CONFIG:
      bstack111l1l11_opy_ = CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩྻ")]
    if bstack1ll1ll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྼ") in CONFIG:
      bstack1l111lll1_opy_ = int(bstack111l1l11_opy_) * int(len(CONFIG[bstack1ll1ll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ྽")]))
    else:
      bstack1l111lll1_opy_ = int(bstack111l1l11_opy_)
    config = Configuration(args)
    bstack1l1l11l111_opy_ = config.paths
    if len(bstack1l1l11l111_opy_) == 0:
      import glob
      pattern = bstack1ll1ll1_opy_ (u"ࠬ࠰ࠪ࠰ࠬ࠱ࡪࡪࡧࡴࡶࡴࡨࠫ྾")
      bstack11l1lll1ll_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11l1lll1ll_opy_)
      config = Configuration(args)
      bstack1l1l11l111_opy_ = config.paths
    bstack1111l111_opy_ = [os.path.normpath(item) for item in bstack1l1l11l111_opy_]
    bstack1l11111ll1_opy_ = [os.path.normpath(item) for item in args]
    bstack11l1l111l_opy_ = [item for item in bstack1l11111ll1_opy_ if item not in bstack1111l111_opy_]
    import platform as pf
    if pf.system().lower() == bstack1ll1ll1_opy_ (u"࠭ࡷࡪࡰࡧࡳࡼࡹࠧ྿"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1111l111_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1l1l1llll_opy_)))
                    for bstack1l1l1llll_opy_ in bstack1111l111_opy_]
    bstack11l1l111_opy_ = []
    for spec in bstack1111l111_opy_:
      bstack11l11l1l_opy_ = []
      bstack11l11l1l_opy_ += bstack11l1l111l_opy_
      bstack11l11l1l_opy_.append(spec)
      bstack11l1l111_opy_.append(bstack11l11l1l_opy_)
    execution_items = []
    for bstack11l11l1l_opy_ in bstack11l1l111_opy_:
      if bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿀") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ࿁")]):
          item = {}
          item[bstack1ll1ll1_opy_ (u"ࠩࡤࡶ࡬࠭࿂")] = bstack1ll1ll1_opy_ (u"ࠪࠤࠬ࿃").join(bstack11l11l1l_opy_)
          item[bstack1ll1ll1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ࿄")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack1ll1ll1_opy_ (u"ࠬࡧࡲࡨࠩ࿅")] = bstack1ll1ll1_opy_ (u"࠭ࠠࠨ࿆").join(bstack11l11l1l_opy_)
        item[bstack1ll1ll1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭࿇")] = 0
        execution_items.append(item)
    bstack1ll111l111_opy_ = bstack1lll1l1l1l_opy_(execution_items, bstack1l111lll1_opy_)
    for execution_item in bstack1ll111l111_opy_:
      bstack111lll11_opy_ = []
      for item in execution_item:
        bstack111lll11_opy_.append(bstack11llll11l1_opy_(name=str(item[bstack1ll1ll1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ࿈")]),
                                             target=bstack1lll111ll_opy_,
                                             args=(item[bstack1ll1ll1_opy_ (u"ࠩࡤࡶ࡬࠭࿉")],)))
      for t in bstack111lll11_opy_:
        t.start()
      for t in bstack111lll11_opy_:
        t.join()
  else:
    bstack1lll11l1l1_opy_(bstack111l1ll11_opy_)
  if not bstack1l1l11l1l_opy_:
    bstack1l1l111111_opy_()
    if(bstack11l1lll1l1_opy_ in [bstack1ll1ll1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ࿊"), bstack1ll1ll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ࿋")]):
      bstack111l1l1ll_opy_()
  bstack1l1l1ll111_opy_.bstack1111lllll1_opy_()
def browserstack_initialize(bstack1ll11l1l11_opy_=None):
  logger.info(bstack1ll1ll1_opy_ (u"ࠬࡘࡵ࡯ࡰ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡻ࡮ࡺࡨࠡࡣࡵ࡫ࡸࡀࠠࠨ࿌") + str(bstack1ll11l1l11_opy_))
  run_on_browserstack(bstack1ll11l1l11_opy_, None, True)
@measure(event_name=EVENTS.bstack11l111l11l_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack1l1l111111_opy_():
  global CONFIG
  global bstack1l11l1l11_opy_
  global bstack111ll11l11_opy_
  global bstack11l11ll1l_opy_
  global bstack11111l11_opy_
  bstack1ll1lllll_opy_.bstack11ll1l1lll_opy_()
  if cli.is_running():
    bstack1ll11111l_opy_.invoke(Events.bstack11l11l11ll_opy_)
  else:
    bstack111l1lll_opy_ = bstack1llll111l_opy_.bstack1llllllll_opy_(config=CONFIG)
    bstack111l1lll_opy_.bstack111l1l111l_opy_(CONFIG)
  if bstack1l11l1l11_opy_ == bstack1ll1ll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭࿍"):
    if not cli.is_enabled(CONFIG):
      bstack1ll111ll_opy_.stop()
  else:
    bstack1ll111ll_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1l1l11l1_opy_.bstack111lll111l_opy_()
  if bstack1ll1ll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ࿎") in CONFIG and str(CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ࿏")]).lower() != bstack1ll1ll1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ࿐"):
    hashed_id, bstack11llll1ll_opy_ = bstack11l11ll11l_opy_()
  else:
    hashed_id, bstack11llll1ll_opy_ = get_build_link()
  bstack1lllll111l_opy_(hashed_id)
  logger.info(bstack1ll1ll1_opy_ (u"ࠪࡗࡉࡑࠠࡳࡷࡱࠤࡪࡴࡤࡦࡦࠣࡪࡴࡸࠠࡪࡦ࠽ࠫ࿑") + bstack11111l11_opy_.get_property(bstack1ll1ll1_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭࿒"), bstack1ll1ll1_opy_ (u"ࠬ࠭࿓")) + bstack1ll1ll1_opy_ (u"࠭ࠬࠡࡶࡨࡷࡹ࡮ࡵࡣࠢ࡬ࡨ࠿ࠦࠧ࿔") + os.getenv(bstack1ll1ll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ࿕"), bstack1ll1ll1_opy_ (u"ࠨࠩ࿖")))
  if hashed_id is not None and bstack111l11111l_opy_() != -1:
    sessions = bstack11l11ll111_opy_(hashed_id)
    bstack11lllll111_opy_(sessions, bstack11llll1ll_opy_)
  if bstack1l11l1l11_opy_ == bstack1ll1ll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ࿗") and bstack111ll11l11_opy_ != 0:
    sys.exit(bstack111ll11l11_opy_)
  if bstack1l11l1l11_opy_ == bstack1ll1ll1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ࿘") and bstack11l11ll1l_opy_ != 0:
    sys.exit(bstack11l11ll1l_opy_)
def bstack1lllll111l_opy_(new_id):
    global bstack1l1l11ll1_opy_
    bstack1l1l11ll1_opy_ = new_id
def bstack111l1111l_opy_(bstack1111l1l1ll_opy_):
  if bstack1111l1l1ll_opy_:
    return bstack1111l1l1ll_opy_.capitalize()
  else:
    return bstack1ll1ll1_opy_ (u"ࠫࠬ࿙")
@measure(event_name=EVENTS.bstack11llllll11_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack1l1111ll1l_opy_(bstack1lll1ll1ll_opy_):
  if bstack1ll1ll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ࿚") in bstack1lll1ll1ll_opy_ and bstack1lll1ll1ll_opy_[bstack1ll1ll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ࿛")] != bstack1ll1ll1_opy_ (u"ࠧࠨ࿜"):
    return bstack1lll1ll1ll_opy_[bstack1ll1ll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭࿝")]
  else:
    bstack1l1lllll11_opy_ = bstack1ll1ll1_opy_ (u"ࠤࠥ࿞")
    if bstack1ll1ll1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ࿟") in bstack1lll1ll1ll_opy_ and bstack1lll1ll1ll_opy_[bstack1ll1ll1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ࿠")] != None:
      bstack1l1lllll11_opy_ += bstack1lll1ll1ll_opy_[bstack1ll1ll1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ࿡")] + bstack1ll1ll1_opy_ (u"ࠨࠬࠡࠤ࿢")
      if bstack1lll1ll1ll_opy_[bstack1ll1ll1_opy_ (u"ࠧࡰࡵࠪ࿣")] == bstack1ll1ll1_opy_ (u"ࠣ࡫ࡲࡷࠧ࿤"):
        bstack1l1lllll11_opy_ += bstack1ll1ll1_opy_ (u"ࠤ࡬ࡓࡘࠦࠢ࿥")
      bstack1l1lllll11_opy_ += (bstack1lll1ll1ll_opy_[bstack1ll1ll1_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ࿦")] or bstack1ll1ll1_opy_ (u"ࠫࠬ࿧"))
      return bstack1l1lllll11_opy_
    else:
      bstack1l1lllll11_opy_ += bstack111l1111l_opy_(bstack1lll1ll1ll_opy_[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭࿨")]) + bstack1ll1ll1_opy_ (u"ࠨࠠࠣ࿩") + (
              bstack1lll1ll1ll_opy_[bstack1ll1ll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ࿪")] or bstack1ll1ll1_opy_ (u"ࠨࠩ࿫")) + bstack1ll1ll1_opy_ (u"ࠤ࠯ࠤࠧ࿬")
      if bstack1lll1ll1ll_opy_[bstack1ll1ll1_opy_ (u"ࠪࡳࡸ࠭࿭")] == bstack1ll1ll1_opy_ (u"ࠦ࡜࡯࡮ࡥࡱࡺࡷࠧ࿮"):
        bstack1l1lllll11_opy_ += bstack1ll1ll1_opy_ (u"ࠧ࡝ࡩ࡯ࠢࠥ࿯")
      bstack1l1lllll11_opy_ += bstack1lll1ll1ll_opy_[bstack1ll1ll1_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪ࿰")] or bstack1ll1ll1_opy_ (u"ࠧࠨ࿱")
      return bstack1l1lllll11_opy_
@measure(event_name=EVENTS.bstack1l1lllll1l_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack11ll1lll11_opy_(bstack1ll111111l_opy_):
  if bstack1ll111111l_opy_ == bstack1ll1ll1_opy_ (u"ࠣࡦࡲࡲࡪࠨ࿲"):
    return bstack1ll1ll1_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ࿳")
  elif bstack1ll111111l_opy_ == bstack1ll1ll1_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ࿴"):
    return bstack1ll1ll1_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡉࡥ࡮ࡲࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ࿵")
  elif bstack1ll111111l_opy_ == bstack1ll1ll1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ࿶"):
    return bstack1ll1ll1_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡩࡵࡩࡪࡴ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡩࡵࡩࡪࡴࠢ࠿ࡒࡤࡷࡸ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭࿷")
  elif bstack1ll111111l_opy_ == bstack1ll1ll1_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨ࿸"):
    return bstack1ll1ll1_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡶࡪࡪ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡴࡨࡨࠧࡄࡅࡳࡴࡲࡶࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ࿹")
  elif bstack1ll111111l_opy_ == bstack1ll1ll1_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥ࿺"):
    return bstack1ll1ll1_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࠩࡥࡦࡣ࠶࠶࠻ࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࠤࡧࡨࡥ࠸࠸࠶ࠣࡀࡗ࡭ࡲ࡫࡯ࡶࡶ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ࿻")
  elif bstack1ll111111l_opy_ == bstack1ll1ll1_opy_ (u"ࠦࡷࡻ࡮࡯࡫ࡱ࡫ࠧ࿼"):
    return bstack1ll1ll1_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࡓࡷࡱࡲ࡮ࡴࡧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭࿽")
  else:
    return bstack1ll1ll1_opy_ (u"࠭࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࠪ࿾") + bstack111l1111l_opy_(
      bstack1ll111111l_opy_) + bstack1ll1ll1_opy_ (u"ࠧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭࿿")
def bstack111lll1ll_opy_(session):
  return bstack1ll1ll1_opy_ (u"ࠨ࠾ࡷࡶࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡸ࡯ࡸࠤࡁࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠥࡹࡥࡴࡵ࡬ࡳࡳ࠳࡮ࡢ࡯ࡨࠦࡃࡂࡡࠡࡪࡵࡩ࡫ࡃࠢࡼࡿࠥࠤࡹࡧࡲࡨࡧࡷࡁࠧࡥࡢ࡭ࡣࡱ࡯ࠧࡄࡻࡾ࠾࠲ࡥࡃࡂ࠯ࡵࡦࡁࡿࢂࢁࡽ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿࠳ࡹࡸ࠾ࠨက").format(
    session[bstack1ll1ll1_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭ခ")], bstack1l1111ll1l_opy_(session), bstack11ll1lll11_opy_(session[bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠩဂ")]),
    bstack11ll1lll11_opy_(session[bstack1ll1ll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫဃ")]),
    bstack111l1111l_opy_(session[bstack1ll1ll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭င")] or session[bstack1ll1ll1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭စ")] or bstack1ll1ll1_opy_ (u"ࠧࠨဆ")) + bstack1ll1ll1_opy_ (u"ࠣࠢࠥဇ") + (session[bstack1ll1ll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫဈ")] or bstack1ll1ll1_opy_ (u"ࠪࠫဉ")),
    session[bstack1ll1ll1_opy_ (u"ࠫࡴࡹࠧည")] + bstack1ll1ll1_opy_ (u"ࠧࠦࠢဋ") + session[bstack1ll1ll1_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪဌ")], session[bstack1ll1ll1_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩဍ")] or bstack1ll1ll1_opy_ (u"ࠨࠩဎ"),
    session[bstack1ll1ll1_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭ဏ")] if session[bstack1ll1ll1_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧတ")] else bstack1ll1ll1_opy_ (u"ࠫࠬထ"))
@measure(event_name=EVENTS.bstack11111ll11_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def bstack11lllll111_opy_(sessions, bstack11llll1ll_opy_):
  try:
    bstack11l1llll1_opy_ = bstack1ll1ll1_opy_ (u"ࠧࠨဒ")
    if not os.path.exists(bstack1ll1l11l11_opy_):
      os.mkdir(bstack1ll1l11l11_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll1ll1_opy_ (u"࠭ࡡࡴࡵࡨࡸࡸ࠵ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ࠫဓ")), bstack1ll1ll1_opy_ (u"ࠧࡳࠩန")) as f:
      bstack11l1llll1_opy_ = f.read()
    bstack11l1llll1_opy_ = bstack11l1llll1_opy_.replace(bstack1ll1ll1_opy_ (u"ࠨࡽࠨࡖࡊ࡙ࡕࡍࡖࡖࡣࡈࡕࡕࡏࡖࠨࢁࠬပ"), str(len(sessions)))
    bstack11l1llll1_opy_ = bstack11l1llll1_opy_.replace(bstack1ll1ll1_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠥࡾࠩဖ"), bstack11llll1ll_opy_)
    bstack11l1llll1_opy_ = bstack11l1llll1_opy_.replace(bstack1ll1ll1_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣࡓࡇࡍࡆࠧࢀࠫဗ"),
                                              sessions[0].get(bstack1ll1ll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡲࡦࡳࡥࠨဘ")) if sessions[0] else bstack1ll1ll1_opy_ (u"ࠬ࠭မ"))
    with open(os.path.join(bstack1ll1l11l11_opy_, bstack1ll1ll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪယ")), bstack1ll1ll1_opy_ (u"ࠧࡸࠩရ")) as stream:
      stream.write(bstack11l1llll1_opy_.split(bstack1ll1ll1_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁࠬလ"))[0])
      for session in sessions:
        stream.write(bstack111lll1ll_opy_(session))
      stream.write(bstack11l1llll1_opy_.split(bstack1ll1ll1_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂ࠭ဝ"))[1])
    logger.info(bstack1ll1ll1_opy_ (u"ࠪࡋࡪࡴࡥࡳࡣࡷࡩࡩࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡨࡵࡪ࡮ࡧࠤࡦࡸࡴࡪࡨࡤࡧࡹࡹࠠࡢࡶࠣࡿࢂ࠭သ").format(bstack1ll1l11l11_opy_));
  except Exception as e:
    logger.debug(bstack111lll11l_opy_.format(str(e)))
def bstack11l11ll111_opy_(hashed_id):
  global CONFIG
  try:
    bstack111lllll1_opy_ = datetime.datetime.now()
    host = bstack1ll1ll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠯ࡦࡰࡴࡻࡤ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫဟ") if bstack1ll1ll1_opy_ (u"ࠬࡧࡰࡱࠩဠ") in CONFIG else bstack1ll1ll1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧအ")
    user = CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩဢ")]
    key = CONFIG[bstack1ll1ll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫဣ")]
    bstack1l11l11l1_opy_ = bstack1ll1ll1_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨဤ") if bstack1ll1ll1_opy_ (u"ࠪࡥࡵࡶࠧဥ") in CONFIG else (bstack1ll1ll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨဦ") if CONFIG.get(bstack1ll1ll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩဧ")) else bstack1ll1ll1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨဨ"))
    host = bstack11l1l1l11_opy_(cli.config, [bstack1ll1ll1_opy_ (u"ࠢࡢࡲ࡬ࡷࠧဩ"), bstack1ll1ll1_opy_ (u"ࠣࡣࡳࡴࡆࡻࡴࡰ࡯ࡤࡸࡪࠨဪ"), bstack1ll1ll1_opy_ (u"ࠤࡤࡴ࡮ࠨါ")], host) if bstack1ll1ll1_opy_ (u"ࠪࡥࡵࡶࠧာ") in CONFIG else bstack11l1l1l11_opy_(cli.config, [bstack1ll1ll1_opy_ (u"ࠦࡦࡶࡩࡴࠤိ"), bstack1ll1ll1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢီ"), bstack1ll1ll1_opy_ (u"ࠨࡡࡱ࡫ࠥု")], host)
    url = bstack1ll1ll1_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡶࡩࡸࡹࡩࡰࡰࡶ࠲࡯ࡹ࡯࡯ࠩူ").format(host, bstack1l11l11l1_opy_, hashed_id)
    headers = {
      bstack1ll1ll1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧေ"): bstack1ll1ll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬဲ"),
    }
    proxies = bstack111ll1111l_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡩࡨࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡹ࡟࡭࡫ࡶࡸࠧဳ"), datetime.datetime.now() - bstack111lllll1_opy_)
      return list(map(lambda session: session[bstack1ll1ll1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩဴ")], response.json()))
  except Exception as e:
    logger.debug(bstack11111llll1_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack1ll1ll11ll_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def get_build_link():
  global CONFIG
  global bstack1l1l11ll1_opy_
  try:
    if bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨဵ") in CONFIG:
      bstack111lllll1_opy_ = datetime.datetime.now()
      host = bstack1ll1ll1_opy_ (u"࠭ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥࠩံ") if bstack1ll1ll1_opy_ (u"ࠧࡢࡲࡳ့ࠫ") in CONFIG else bstack1ll1ll1_opy_ (u"ࠨࡣࡳ࡭ࠬး")
      user = CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨ္ࠫ")]
      key = CONFIG[bstack1ll1ll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ်࠭")]
      bstack1l11l11l1_opy_ = bstack1ll1ll1_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪျ") if bstack1ll1ll1_opy_ (u"ࠬࡧࡰࡱࠩြ") in CONFIG else bstack1ll1ll1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨွ")
      url = bstack1ll1ll1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠰࡭ࡷࡴࡴࠧှ").format(user, key, host, bstack1l11l11l1_opy_)
      if cli.is_enabled(CONFIG):
        bstack11llll1ll_opy_, hashed_id = cli.bstack11l1ll1ll_opy_()
        logger.info(bstack111l1l1lll_opy_.format(bstack11llll1ll_opy_))
        return [hashed_id, bstack11llll1ll_opy_]
      else:
        headers = {
          bstack1ll1ll1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧဿ"): bstack1ll1ll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ၀"),
        }
        if bstack1ll1ll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ၁") in CONFIG:
          params = {bstack1ll1ll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ၂"): CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ၃")], bstack1ll1ll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ၄"): CONFIG[bstack1ll1ll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ၅")]}
        else:
          params = {bstack1ll1ll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭၆"): CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ၇")]}
        proxies = bstack111ll1111l_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack1ll111l1l1_opy_ = response.json()[0][bstack1ll1ll1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡣࡷ࡬ࡰࡩ࠭၈")]
          if bstack1ll111l1l1_opy_:
            bstack11llll1ll_opy_ = bstack1ll111l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨ၉")].split(bstack1ll1ll1_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧ࠲ࡨࡵࡪ࡮ࡧࠫ၊"))[0] + bstack1ll1ll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡸ࠵ࠧ။") + bstack1ll111l1l1_opy_[
              bstack1ll1ll1_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ၌")]
            logger.info(bstack111l1l1lll_opy_.format(bstack11llll1ll_opy_))
            bstack1l1l11ll1_opy_ = bstack1ll111l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ၍")]
            bstack1lll1l1ll1_opy_ = CONFIG[bstack1ll1ll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ၎")]
            if bstack1ll1ll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ၏") in CONFIG:
              bstack1lll1l1ll1_opy_ += bstack1ll1ll1_opy_ (u"ࠫࠥ࠭ၐ") + CONFIG[bstack1ll1ll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧၑ")]
            if bstack1lll1l1ll1_opy_ != bstack1ll111l1l1_opy_[bstack1ll1ll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫၒ")]:
              logger.debug(bstack11l1l1lll1_opy_.format(bstack1ll111l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬၓ")], bstack1lll1l1ll1_opy_))
            cli.bstack1llll1ll11_opy_(bstack1ll1ll1_opy_ (u"ࠣࡪࡷࡸࡵࡀࡧࡦࡶࡢࡦࡺ࡯࡬ࡥࡡ࡯࡭ࡳࡱࠢၔ"), datetime.datetime.now() - bstack111lllll1_opy_)
            return [bstack1ll111l1l1_opy_[bstack1ll1ll1_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬၕ")], bstack11llll1ll_opy_]
    else:
      logger.warn(bstack111l11lll1_opy_)
  except Exception as e:
    logger.debug(bstack111lllllll_opy_.format(str(e)))
  return [None, None]
def bstack1l11ll1lll_opy_(url, bstack111l1l11l_opy_=False):
  global CONFIG
  global bstack1ll1lll1l_opy_
  if not bstack1ll1lll1l_opy_:
    hostname = bstack11ll1111l1_opy_(url)
    is_private = bstack111ll111l1_opy_(hostname)
    if (bstack1ll1ll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧၖ") in CONFIG and not bstack1ll1l1llll_opy_(CONFIG[bstack1ll1ll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨၗ")])) and (is_private or bstack111l1l11l_opy_):
      bstack1ll1lll1l_opy_ = hostname
def bstack11ll1111l1_opy_(url):
  return urlparse(url).hostname
def bstack111ll111l1_opy_(hostname):
  for bstack111l111lll_opy_ in bstack1ll1l1l11l_opy_:
    regex = re.compile(bstack111l111lll_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack11111l11l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1111l111ll_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1ll11l111_opy_
  bstack111l1lll1l_opy_ = not (bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၘ"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack1ll1ll1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၙ"), None))
  bstack11l1111lll_opy_ = getattr(driver, bstack1ll1ll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧၚ"), None) != True
  bstack1l11llll11_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၛ"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၜ"), None)
  if bstack1l11llll11_opy_:
    if not bstack1111l1l11_opy_():
      logger.warning(bstack1ll1ll1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸ࠴ࠢၝ"))
      return {}
    logger.debug(bstack1ll1ll1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨၞ"))
    logger.debug(perform_scan(driver, driver_command=bstack1ll1ll1_opy_ (u"ࠬ࡫ࡸࡦࡥࡸࡸࡪ࡙ࡣࡳ࡫ࡳࡸࠬၟ")))
    results = bstack11l1l1lll_opy_(bstack1ll1ll1_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹࡹࠢၠ"))
    if results is not None and results.get(bstack1ll1ll1_opy_ (u"ࠢࡪࡵࡶࡹࡪࡹࠢၡ")) is not None:
        return results[bstack1ll1ll1_opy_ (u"ࠣ࡫ࡶࡷࡺ࡫ࡳࠣၢ")]
    logger.error(bstack1ll1ll1_opy_ (u"ࠤࡑࡳࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡘࡥࡴࡷ࡯ࡸࡸࠦࡷࡦࡴࡨࠤ࡫ࡵࡵ࡯ࡦ࠱ࠦၣ"))
    return []
  if not bstack11111ll1_opy_.bstack1ll1lll111_opy_(CONFIG, bstack1ll11l111_opy_) or (bstack11l1111lll_opy_ and bstack111l1lll1l_opy_):
    logger.warning(bstack1ll1ll1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷ࠳ࠨၤ"))
    return {}
  try:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨၥ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack111llll111_opy_.bstack1l11ll1ll_opy_)
    return results
  except Exception:
    logger.error(bstack1ll1ll1_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡺࡩࡷ࡫ࠠࡧࡱࡸࡲࡩ࠴ࠢၦ"))
    return {}
@measure(event_name=EVENTS.bstack11l111l1l1_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1ll11l111_opy_
  bstack111l1lll1l_opy_ = not (bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪၧ"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ၨ"), None))
  bstack11l1111lll_opy_ = getattr(driver, bstack1ll1ll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨၩ"), None) != True
  bstack1l11llll11_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၪ"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၫ"), None)
  if bstack1l11llll11_opy_:
    if not bstack1111l1l11_opy_():
      logger.warning(bstack1ll1ll1_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹ࠯ࠤၬ"))
      return {}
    logger.debug(bstack1ll1ll1_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻࠪၭ"))
    logger.debug(perform_scan(driver, driver_command=bstack1ll1ll1_opy_ (u"࠭ࡥࡹࡧࡦࡹࡹ࡫ࡓࡤࡴ࡬ࡴࡹ࠭ၮ")))
    results = bstack11l1l1lll_opy_(bstack1ll1ll1_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡓࡶ࡯ࡰࡥࡷࡿࠢၯ"))
    if results is not None and results.get(bstack1ll1ll1_opy_ (u"ࠣࡵࡸࡱࡲࡧࡲࡺࠤၰ")) is not None:
        return results[bstack1ll1ll1_opy_ (u"ࠤࡶࡹࡲࡳࡡࡳࡻࠥၱ")]
    logger.error(bstack1ll1ll1_opy_ (u"ࠥࡒࡴࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡒࡦࡵࡸࡰࡹࡹࠠࡔࡷࡰࡱࡦࡸࡹࠡࡹࡤࡷࠥ࡬࡯ࡶࡰࡧ࠲ࠧၲ"))
    return {}
  if not bstack11111ll1_opy_.bstack1ll1lll111_opy_(CONFIG, bstack1ll11l111_opy_) or (bstack11l1111lll_opy_ and bstack111l1lll1l_opy_):
    logger.warning(bstack1ll1ll1_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡳࡶ࡯ࡰࡥࡷࡿ࠮ࠣၳ"))
    return {}
  try:
    logger.debug(bstack1ll1ll1_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻࠪၴ"))
    logger.debug(perform_scan(driver))
    bstack11ll1ll1ll_opy_ = driver.execute_async_script(bstack111llll111_opy_.bstack11lllll11l_opy_)
    return bstack11ll1ll1ll_opy_
  except Exception:
    logger.error(bstack1ll1ll1_opy_ (u"ࠨࡎࡰࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡹࡲࡳࡡࡳࡻࠣࡻࡦࡹࠠࡧࡱࡸࡲࡩ࠴ࠢၵ"))
    return {}
def bstack1111l1l11_opy_():
  global CONFIG
  global bstack1ll11l111_opy_
  bstack111ll11lll_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၶ"), None) and bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၷ"), None)
  if not bstack11111ll1_opy_.bstack1ll1lll111_opy_(CONFIG, bstack1ll11l111_opy_) or not bstack111ll11lll_opy_:
        logger.warning(bstack1ll1ll1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤၸ"))
        return False
  return True
def bstack11l1l1lll_opy_(bstack1l11l1lll1_opy_):
    bstack1l1l11111l_opy_ = bstack1ll111ll_opy_.current_test_uuid() if bstack1ll111ll_opy_.current_test_uuid() else bstack1l1l11l1_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack11l1ll11ll_opy_(bstack1l1l11111l_opy_, bstack1l11l1lll1_opy_))
        try:
            return future.result(timeout=bstack11l1ll111_opy_)
        except TimeoutError:
            logger.error(bstack1ll1ll1_opy_ (u"ࠥࡘ࡮ࡳࡥࡰࡷࡷࠤࡦ࡬ࡴࡦࡴࠣࡿࢂࡹࠠࡸࡪ࡬ࡰࡪࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡔࡨࡷࡺࡲࡴࡴࠤၹ").format(bstack11l1ll111_opy_))
        except Exception as ex:
            logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡶࡪࡺࡲࡪࡧࡹ࡭ࡳ࡭ࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡽࢀ࠲ࠥࡋࡲࡳࡱࡵࠤ࠲ࠦࡻࡾࠤၺ").format(bstack1l11l1lll1_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack11111l111_opy_, stage=STAGE.bstack111l1l111_opy_, bstack1l1lllll11_opy_=bstack1l1ll11l1l_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1ll11l111_opy_
  bstack111l1lll1l_opy_ = not (bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၻ"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack1ll1ll1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၼ"), None))
  bstack11l111lll1_opy_ = not (bstack1l1lll11_opy_(threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၽ"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack1ll1ll1_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၾ"), None))
  bstack11l1111lll_opy_ = getattr(driver, bstack1ll1ll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩၿ"), None) != True
  if not bstack11111ll1_opy_.bstack1ll1lll111_opy_(CONFIG, bstack1ll11l111_opy_) or (bstack11l1111lll_opy_ and bstack111l1lll1l_opy_ and bstack11l111lll1_opy_):
    logger.warning(bstack1ll1ll1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡹࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡤࡣࡱ࠲ࠧႀ"))
    return {}
  try:
    bstack11l1111l1_opy_ = bstack1ll1ll1_opy_ (u"ࠫࡦࡶࡰࠨႁ") in CONFIG and CONFIG.get(bstack1ll1ll1_opy_ (u"ࠬࡧࡰࡱࠩႂ"), bstack1ll1ll1_opy_ (u"࠭ࠧႃ"))
    session_id = getattr(driver, bstack1ll1ll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠫႄ"), None)
    if not session_id:
      logger.warning(bstack1ll1ll1_opy_ (u"ࠣࡐࡲࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡏࡄࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤࡩࡸࡩࡷࡧࡵࠦႅ"))
      return {bstack1ll1ll1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣႆ"): bstack1ll1ll1_opy_ (u"ࠥࡒࡴࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࠣࡪࡴࡻ࡮ࡥࠤႇ")}
    if bstack11l1111l1_opy_:
      try:
        bstack11l1l1llll_opy_ = {
              bstack1ll1ll1_opy_ (u"ࠫࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠨႈ"): os.environ.get(bstack1ll1ll1_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪႉ"), os.environ.get(bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪႊ"), bstack1ll1ll1_opy_ (u"ࠧࠨႋ"))),
              bstack1ll1ll1_opy_ (u"ࠨࡶ࡫ࡘࡪࡹࡴࡓࡷࡱ࡙ࡺ࡯ࡤࠨႌ"): bstack1ll111ll_opy_.current_test_uuid() if bstack1ll111ll_opy_.current_test_uuid() else bstack1l1l11l1_opy_.current_hook_uuid(),
              bstack1ll1ll1_opy_ (u"ࠩࡤࡹࡹ࡮ࡈࡦࡣࡧࡩࡷႍ࠭"): os.environ.get(bstack1ll1ll1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨႎ")),
              bstack1ll1ll1_opy_ (u"ࠫࡸࡩࡡ࡯ࡖ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫႏ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack1ll1ll1_opy_ (u"ࠬࡺࡨࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ႐"): os.environ.get(bstack1ll1ll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ႑"), bstack1ll1ll1_opy_ (u"ࠧࠨ႒")),
              bstack1ll1ll1_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨ႓"): kwargs.get(bstack1ll1ll1_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࡡࡦࡳࡲࡳࡡ࡯ࡦࠪ႔"), None) or bstack1ll1ll1_opy_ (u"ࠪࠫ႕")
          }
        if not hasattr(thread_local, bstack1ll1ll1_opy_ (u"ࠫࡧࡧࡳࡦࡡࡤࡴࡵࡥࡡ࠲࠳ࡼࡣࡸࡩࡲࡪࡲࡷࠫ႖")):
            scripts = {bstack1ll1ll1_opy_ (u"ࠬࡹࡣࡢࡰࠪ႗"): bstack111llll111_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack1111l11111_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack1111l11111_opy_[bstack1ll1ll1_opy_ (u"࠭ࡳࡤࡣࡱࠫ႘")] = bstack1111l11111_opy_[bstack1ll1ll1_opy_ (u"ࠧࡴࡥࡤࡲࠬ႙")] % json.dumps(bstack11l1l1llll_opy_)
        bstack111llll111_opy_.bstack111l1llll1_opy_(bstack1111l11111_opy_)
        bstack111llll111_opy_.store()
        bstack1ll11lll1l_opy_ = driver.execute_script(bstack111llll111_opy_.perform_scan)
      except Exception as bstack111llll1ll_opy_:
        logger.info(bstack1ll1ll1_opy_ (u"ࠣࡃࡳࡴ࡮ࡻ࡭ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࠣႚ") + str(bstack111llll1ll_opy_))
        bstack1ll11lll1l_opy_ = {bstack1ll1ll1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣႛ"): str(bstack111llll1ll_opy_)}
    else:
      bstack1ll11lll1l_opy_ = driver.execute_async_script(bstack111llll111_opy_.perform_scan, {bstack1ll1ll1_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪႜ"): kwargs.get(bstack1ll1ll1_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣࡨࡵ࡭࡮ࡣࡱࡨࠬႝ"), None) or bstack1ll1ll1_opy_ (u"ࠬ࠭႞")})
    return bstack1ll11lll1l_opy_
  except Exception as err:
    logger.error(bstack1ll1ll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡵࡹࡳࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡤࡣࡱ࠲ࠥࢁࡽࠣ႟").format(str(err)))
    return {}