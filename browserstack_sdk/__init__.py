# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
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
from browserstack_sdk.bstack1111lll1l_opy_ import bstack1l11ll1l11_opy_
from browserstack_sdk.bstack1lll11lll_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack1lll111l11_opy_():
  global CONFIG
  headers = {
        bstack1ll1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩ৾"): bstack1ll1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ৿"),
      }
  proxies = bstack111l1l1ll_opy_(CONFIG, bstack1111l11111_opy_)
  try:
    response = requests.get(bstack1111l11111_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1111111ll_opy_ = response.json()[bstack1ll1l_opy_ (u"ࠬ࡮ࡵࡣࡵࠪ਀")]
      logger.debug(bstack11l1l1111l_opy_.format(response.json()))
      return bstack1111111ll_opy_
    else:
      logger.debug(bstack1ll11l1lll_opy_.format(bstack1ll1l_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧਁ")))
  except Exception as e:
    logger.debug(bstack1ll11l1lll_opy_.format(e))
def bstack1l1111l1l_opy_(hub_url):
  global CONFIG
  url = bstack1ll1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤਂ")+  hub_url + bstack1ll1l_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣਃ")
  headers = {
        bstack1ll1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨ਄"): bstack1ll1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ਅ"),
      }
  proxies = bstack111l1l1ll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1l11l111l1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1lll11111l_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack11l11l1l1_opy_, stage=STAGE.bstack11lll11ll_opy_)
def bstack11ll1lll11_opy_():
  try:
    global bstack111ll11l1l_opy_
    bstack1111111ll_opy_ = bstack1lll111l11_opy_()
    bstack1ll1l11ll_opy_ = []
    results = []
    for bstack11lll1l1l1_opy_ in bstack1111111ll_opy_:
      bstack1ll1l11ll_opy_.append(bstack1lll1lll1l_opy_(target=bstack1l1111l1l_opy_,args=(bstack11lll1l1l1_opy_,)))
    for t in bstack1ll1l11ll_opy_:
      t.start()
    for t in bstack1ll1l11ll_opy_:
      results.append(t.join())
    bstack1ll111lll_opy_ = {}
    for item in results:
      hub_url = item[bstack1ll1l_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬਆ")]
      latency = item[bstack1ll1l_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭ਇ")]
      bstack1ll111lll_opy_[hub_url] = latency
    bstack1l11111l1_opy_ = min(bstack1ll111lll_opy_, key= lambda x: bstack1ll111lll_opy_[x])
    bstack111ll11l1l_opy_ = bstack1l11111l1_opy_
    logger.debug(bstack1ll1l111l1_opy_.format(bstack1l11111l1_opy_))
  except Exception as e:
    logger.debug(bstack1llllll111_opy_.format(e))
from browserstack_sdk.bstack1llll111l_opy_ import *
from browserstack_sdk.bstack111111l1_opy_ import *
from browserstack_sdk.bstack11l1ll11_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack1ll1ll111_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack1l11ll11ll_opy_, stage=STAGE.bstack11lll11ll_opy_)
def bstack1lll1l11l1_opy_():
    global bstack111ll11l1l_opy_
    try:
        bstack11ll1l1ll_opy_ = bstack1l1l1lll11_opy_()
        bstack1111llll1_opy_(bstack11ll1l1ll_opy_)
        hub_url = bstack11ll1l1ll_opy_.get(bstack1ll1l_opy_ (u"ࠨࡵࡳ࡮ࠥਈ"), bstack1ll1l_opy_ (u"ࠢࠣਉ"))
        if hub_url.endswith(bstack1ll1l_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩਊ")):
            hub_url = hub_url.rsplit(bstack1ll1l_opy_ (u"ࠩ࠲ࡻࡩ࠵ࡨࡶࡤࠪ਋"), 1)[0]
        if hub_url.startswith(bstack1ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࠫ਌")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack1ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࠭਍")):
            hub_url = hub_url[8:]
        bstack111ll11l1l_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1l1l1lll11_opy_():
    global CONFIG
    bstack11l11l11l_opy_ = CONFIG.get(bstack1ll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ਎"), {}).get(bstack1ll1l_opy_ (u"࠭ࡧࡳ࡫ࡧࡒࡦࡳࡥࠨਏ"), bstack1ll1l_opy_ (u"ࠧࡏࡑࡢࡋࡗࡏࡄࡠࡐࡄࡑࡊࡥࡐࡂࡕࡖࡉࡉ࠭ਐ"))
    if not isinstance(bstack11l11l11l_opy_, str):
        raise ValueError(bstack1ll1l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡈࡴ࡬ࡨࠥࡴࡡ࡮ࡧࠣࡱࡺࡹࡴࠡࡤࡨࠤࡦࠦࡶࡢ࡮࡬ࡨࠥࡹࡴࡳ࡫ࡱ࡫ࠧ਑"))
    try:
        bstack11ll1l1ll_opy_ = bstack1l11l1111_opy_(bstack11l11l11l_opy_)
        return bstack11ll1l1ll_opy_
    except Exception as e:
        logger.error(bstack1ll1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣ਒").format(str(e)))
        return {}
def bstack1l11l1111_opy_(bstack11l11l11l_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack1ll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬਓ")] or not CONFIG[bstack1ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧਔ")]:
            raise ValueError(bstack1ll1l_opy_ (u"ࠧࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠠࡰࡴࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠢਕ"))
        url = bstack1l1l111lll_opy_ + bstack11l11l11l_opy_
        auth = (CONFIG[bstack1ll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨਖ")], CONFIG[bstack1ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪਗ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1l11llll11_opy_ = json.loads(response.text)
            return bstack1l11llll11_opy_
    except ValueError as ve:
        logger.error(bstack1ll1l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣਘ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack1ll1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࠿ࠦࡻࡾࠤਙ").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1111llll1_opy_(bstack11l11l111l_opy_):
    global CONFIG
    if bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧਚ") not in CONFIG or str(CONFIG[bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨਛ")]).lower() == bstack1ll1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫਜ"):
        CONFIG[bstack1ll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬਝ")] = False
    elif bstack1ll1l_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬਞ") in bstack11l11l111l_opy_:
        bstack1l11lllll1_opy_ = CONFIG.get(bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬਟ"), {})
        logger.debug(bstack1ll1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢਠ"), bstack1l11lllll1_opy_)
        bstack1l1lllll1_opy_ = bstack11l11l111l_opy_.get(bstack1ll1l_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡕࡩࡵ࡫ࡡࡵࡧࡵࡷࠧਡ"), [])
        bstack1l1111ll11_opy_ = bstack1ll1l_opy_ (u"ࠦ࠱ࠨਢ").join(bstack1l1lllll1_opy_)
        logger.debug(bstack1ll1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡻࡳࡵࡱࡰࠤࡷ࡫ࡰࡦࡣࡷࡩࡷࠦࡳࡵࡴ࡬ࡲ࡬ࡀࠠࠦࡵࠥਣ"), bstack1l1111ll11_opy_)
        bstack1l11l1l1ll_opy_ = {
            bstack1ll1l_opy_ (u"ࠨ࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣਤ"): bstack1ll1l_opy_ (u"ࠢࡢࡶࡶ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷࠨਥ"),
            bstack1ll1l_opy_ (u"ࠣࡨࡲࡶࡨ࡫ࡌࡰࡥࡤࡰࠧਦ"): bstack1ll1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢਧ"),
            bstack1ll1l_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧਨ"): bstack1l1111ll11_opy_
        }
        bstack1l11lllll1_opy_.update(bstack1l11l1l1ll_opy_)
        logger.debug(bstack1ll1l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼࡙ࠣࡵࡪࡡࡵࡧࡧࠤࡱࡵࡣࡢ࡮ࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠫࡳࠣ਩"), bstack1l11lllll1_opy_)
        CONFIG[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩਪ")] = bstack1l11lllll1_opy_
        logger.debug(bstack1ll1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡌࡩ࡯ࡣ࡯ࠤࡈࡕࡎࡇࡋࡊ࠾ࠥࠫࡳࠣਫ"), CONFIG)
def bstack11lll1111l_opy_():
    bstack11ll1l1ll_opy_ = bstack1l1l1lll11_opy_()
    if not bstack11ll1l1ll_opy_[bstack1ll1l_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠧਬ")]:
      raise ValueError(bstack1ll1l_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠡ࡫ࡶࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬ࡲࡰ࡯ࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠥਭ"))
    return bstack11ll1l1ll_opy_[bstack1ll1l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠩਮ")] + bstack1ll1l_opy_ (u"ࠪࡃࡨࡧࡰࡴ࠿ࠪਯ")
@measure(event_name=EVENTS.bstack11ll1lllll_opy_, stage=STAGE.bstack11lll11ll_opy_)
def bstack111ll111ll_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack1ll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ਰ")], CONFIG[bstack1ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ਱")])
        url = bstack11ll1111l1_opy_
        logger.debug(bstack1ll1l_opy_ (u"ࠨࡁࡵࡶࡨࡱࡵࡺࡩ࡯ࡩࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬ࡲࡰ࡯ࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡗࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࠦࡁࡑࡋࠥਲ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack1ll1l_opy_ (u"ࠢࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪࠨਲ਼"): bstack1ll1l_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠦ਴")})
            if response.status_code == 200:
                bstack1l1l11111l_opy_ = json.loads(response.text)
                bstack1l11l1l111_opy_ = bstack1l1l11111l_opy_.get(bstack1ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡴࠩਵ"), [])
                if bstack1l11l1l111_opy_:
                    bstack1111ll1111_opy_ = bstack1l11l1l111_opy_[0]
                    build_hashed_id = bstack1111ll1111_opy_.get(bstack1ll1l_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ਸ਼"))
                    bstack1l111lll1_opy_ = bstack1llll11lll_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1l111lll1_opy_])
                    logger.info(bstack1ll11111ll_opy_.format(bstack1l111lll1_opy_))
                    bstack1lll111lll_opy_ = CONFIG[bstack1ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ਷")]
                    if bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧਸ") in CONFIG:
                      bstack1lll111lll_opy_ += bstack1ll1l_opy_ (u"࠭ࠠࠨਹ") + CONFIG[bstack1ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ਺")]
                    if bstack1lll111lll_opy_ != bstack1111ll1111_opy_.get(bstack1ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭਻")):
                      logger.debug(bstack1l1l11llll_opy_.format(bstack1111ll1111_opy_.get(bstack1ll1l_opy_ (u"ࠩࡱࡥࡲ࡫਼ࠧ")), bstack1lll111lll_opy_))
                    return result
                else:
                    logger.debug(bstack1ll1l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡑࡳࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࡷ࡫ࡳࡱࡱࡱࡷࡪ࠴ࠢ਽"))
            else:
                logger.debug(bstack1ll1l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨਾ"))
        except Exception as e:
            logger.error(bstack1ll1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࡹࠠ࠻ࠢࡾࢁࠧਿ").format(str(e)))
    else:
        logger.debug(bstack1ll1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡉࡏࡏࡈࡌࡋࠥ࡯ࡳࠡࡰࡲࡸࠥࡹࡥࡵ࠰࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨੀ"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1l1lll11l1_opy_ import bstack1l1lll11l1_opy_, Events, bstack1111ll11l1_opy_, bstack1ll1lll1l1_opy_
from bstack_utils.measure import bstack111l11llll_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack11llll11ll_opy_ import bstack1111l1llll_opy_
from bstack_utils.messages import *
from bstack_utils import bstack1ll1ll111_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l1lll1ll_opy_, bstack1l11lllll_opy_, bstack1ll11l1l1_opy_, bstack1l1l1l1l_opy_, \
  bstack11l11ll11_opy_, \
  Notset, bstack1l1ll1ll1l_opy_, \
  bstack11l1l11l11_opy_, bstack1ll11lll1_opy_, bstack1l111lll11_opy_, bstack1ll1l11l1_opy_, bstack111ll1llll_opy_, bstack111lll111_opy_, \
  bstack1lll111111_opy_, \
  bstack1lll1ll11l_opy_, bstack11ll1l1ll1_opy_, bstack11111lllll_opy_, bstack11l1ll11ll_opy_, \
  bstack111llll1l_opy_, bstack1lll11l1l_opy_, bstack1lll1ll111_opy_, bstack1l1l1ll111_opy_
from bstack_utils.bstack11l11lll11_opy_ import bstack1ll1ll11ll_opy_
from bstack_utils.bstack1l11111lll_opy_ import bstack1l111lll1l_opy_, bstack1l1ll1l11_opy_
from bstack_utils.bstack1l1ll1lll_opy_ import bstack1llllll11l_opy_
from bstack_utils.bstack11ll1l1l1l_opy_ import bstack1ll11111l_opy_, bstack1ll1l1ll1_opy_
from bstack_utils.bstack1l1ll1lll1_opy_ import bstack1l1ll1lll1_opy_
from bstack_utils.bstack111l1l1111_opy_ import bstack11l11l11l1_opy_
from bstack_utils.proxy import bstack11l1l1l1l1_opy_, bstack111l1l1ll_opy_, bstack1l111l11l_opy_, bstack1l1llll111_opy_
from bstack_utils.bstack1l111l1l1_opy_ import bstack11lll1lll1_opy_
import bstack_utils.bstack111l111l1_opy_ as bstack1l11lll111_opy_
import bstack_utils.bstack1l11l11l11_opy_ as bstack1ll1lllll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack1l1lll1ll1_opy_ import bstack1llll1l11l_opy_
from bstack_utils.bstack1111llll_opy_ import bstack11111l1l_opy_
from bstack_utils.bstack1lllll1l1l_opy_ import bstack11lll111l_opy_
if os.getenv(bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡌࡔࡕࡋࡔࠩੁ")):
  cli.bstack111ll1111_opy_()
else:
  os.environ[bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡍࡕࡏࡌࡕࠪੂ")] = bstack1ll1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ੃")
bstack1l1llll11l_opy_ = bstack1ll1l_opy_ (u"ࠪࠤࠥ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࠣࠤ࡮࡬ࠨࡱࡣࡪࡩࠥࡃ࠽࠾ࠢࡹࡳ࡮ࡪࠠ࠱ࠫࠣࡿࡡࡴࠠࠡࠢࡷࡶࡾࢁ࡜࡯ࠢࡦࡳࡳࡹࡴࠡࡨࡶࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨ࡝ࠩࡩࡷࡡ࠭ࠩ࠼࡞ࡱࠤࠥࠦࠠࠡࡨࡶ࠲ࡦࡶࡰࡦࡰࡧࡊ࡮ࡲࡥࡔࡻࡱࡧ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪ࠯ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡶ࡟ࡪࡰࡧࡩࡽ࠯ࠠࠬࠢࠥ࠾ࠧࠦࠫࠡࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࠨࡢࡹࡤ࡭ࡹࠦ࡮ࡦࡹࡓࡥ࡬࡫࠲࠯ࡧࡹࡥࡱࡻࡡࡵࡧࠫࠦ࠭࠯ࠠ࠾ࡀࠣࡿࢂࠨࠬࠡ࡞ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥ࡫ࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡄࡦࡶࡤ࡭ࡱࡹࠢࡾ࡞ࠪ࠭࠮࠯࡛ࠣࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠦࡢ࠯ࠠࠬࠢࠥ࠰ࡡࡢ࡮ࠣࠫ࡟ࡲࠥࠦࠠࠡࡿࡦࡥࡹࡩࡨࠩࡧࡻ࠭ࢀࡢ࡮ࠡࠢࠣࠤࢂࡢ࡮ࠡࠢࢀࡠࡳࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠪ੄")
bstack1ll1lll111_opy_ = bstack1ll1l_opy_ (u"ࠫࡡࡴ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰࡞ࡱࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶ࡡࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠷࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡲࡢ࡭ࡳࡪࡥࡹࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠷ࡣ࡜࡯ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯ࡵ࡯࡭ࡨ࡫ࠨ࠱࠮ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸࠯࡜࡯ࡥࡲࡲࡸࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯ࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨࠩ࠼࡞ࡱ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡰࡦࡻ࡮ࡤࡪࠣࡁࠥࡧࡳࡺࡰࡦࠤ࠭ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷ࠮ࠦ࠽࠿ࠢࡾࡠࡳࡲࡥࡵࠢࡦࡥࡵࡹ࠻࡝ࡰࡷࡶࡾࠦࡻ࡝ࡰࡦࡥࡵࡹࠠ࠾ࠢࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶ࠭ࡡࡴࠠࠡࡿࠣࡧࡦࡺࡣࡩࠪࡨࡼ࠮ࠦࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡦࡽࡡࡪࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡧࡴࡴ࡮ࡦࡥࡷࠬࢀࡢ࡮ࠡࠢࠣࠤࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴ࠻ࠢࡣࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠩࢁࡥ࡯ࡥࡲࡨࡪ࡛ࡒࡊࡅࡲࡱࡵࡵ࡮ࡦࡰࡷࠬࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡩࡡࡱࡵࠬ࠭ࢂࡦࠬ࡝ࡰࠣࠤࠥࠦ࠮࠯࠰࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴ࡞ࡱࠤࠥࢃࠩ࡝ࡰࢀࡠࡳ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࠪ੅")
from ._version import __version__
bstack1l11l1ll1_opy_ = None
CONFIG = {}
bstack1l1l1l1l1_opy_ = {}
bstack1ll11lllll_opy_ = {}
bstack111111111_opy_ = None
bstack11l1111l1_opy_ = None
bstack111llll111_opy_ = None
bstack1l1lllllll_opy_ = -1
bstack11111ll1ll_opy_ = 0
bstack1l11ll1lll_opy_ = bstack1llll1ll1l_opy_
bstack1ll11lll11_opy_ = 1
bstack11lllllll_opy_ = False
bstack1ll1l11ll1_opy_ = False
bstack1l1llllll_opy_ = bstack1ll1l_opy_ (u"ࠬ࠭੆")
bstack1l1lllll11_opy_ = bstack1ll1l_opy_ (u"࠭ࠧੇ")
bstack11lll11l1l_opy_ = False
bstack1llll1l1l1_opy_ = True
bstack111l1ll111_opy_ = bstack1ll1l_opy_ (u"ࠧࠨੈ")
bstack1lll1l111l_opy_ = []
bstack1ll1l111l_opy_ = threading.Lock()
bstack111lll1l11_opy_ = threading.Lock()
bstack111ll11l1l_opy_ = bstack1ll1l_opy_ (u"ࠨࠩ੉")
bstack11l1ll1lll_opy_ = False
bstack1111ll1l1_opy_ = None
bstack1l1lll1l11_opy_ = None
bstack1l1lllll1l_opy_ = None
bstack1ll1ll1ll1_opy_ = -1
bstack111ll1ll11_opy_ = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠩࢁࠫ੊")), bstack1ll1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪੋ"), bstack1ll1l_opy_ (u"ࠫ࠳ࡸ࡯ࡣࡱࡷ࠱ࡷ࡫ࡰࡰࡴࡷ࠱࡭࡫࡬ࡱࡧࡵ࠲࡯ࡹ࡯࡯ࠩੌ"))
bstack111ll1lll_opy_ = 0
bstack11l11ll111_opy_ = 0
bstack1l11l1ll1l_opy_ = []
bstack1l1l1l11ll_opy_ = []
bstack11llll1ll_opy_ = []
bstack11llll111_opy_ = []
bstack111l11lll_opy_ = bstack1ll1l_opy_ (u"੍ࠬ࠭")
bstack1lll11lll1_opy_ = bstack1ll1l_opy_ (u"࠭ࠧ੎")
bstack111l11l1l1_opy_ = False
bstack1ll11llll1_opy_ = False
bstack1l1111l11l_opy_ = {}
bstack111lll11ll_opy_ = None
bstack1l1ll1ll11_opy_ = None
bstack11l1l111l1_opy_ = None
bstack1111l1lll_opy_ = None
bstack1l111l1ll1_opy_ = None
bstack11llll1111_opy_ = None
bstack11l11l11ll_opy_ = None
bstack1l11l1111l_opy_ = None
bstack111ll11ll_opy_ = None
bstack1l11lll11l_opy_ = None
bstack1l11lll1ll_opy_ = None
bstack11l111ll11_opy_ = None
bstack1l1l11l1l1_opy_ = None
bstack11l111ll1_opy_ = None
bstack1l1l11l1l_opy_ = None
bstack111l1l11ll_opy_ = None
bstack11l11l1lll_opy_ = None
bstack11l1111lll_opy_ = None
bstack11lllllll1_opy_ = None
bstack1ll1llllll_opy_ = None
bstack11l1l11l1l_opy_ = None
bstack111lll11l_opy_ = None
bstack111l1l111_opy_ = None
thread_local = threading.local()
bstack1ll1ll1ll_opy_ = False
bstack11l1l11111_opy_ = bstack1ll1l_opy_ (u"ࠢࠣ੏")
logger = bstack1ll1ll111_opy_.get_logger(__name__, bstack1l11ll1lll_opy_)
bstack111111ll_opy_ = Config.bstack111l1ll1_opy_()
percy = bstack1ll1llll1_opy_()
bstack11111l1l1_opy_ = bstack1111l1llll_opy_()
bstack1l11l11l1l_opy_ = bstack11l1ll11_opy_()
def bstack1l1l11111_opy_():
  global CONFIG
  global bstack111l11l1l1_opy_
  global bstack111111ll_opy_
  testContextOptions = bstack11111l1ll_opy_(CONFIG)
  if bstack11l11ll11_opy_(CONFIG):
    if (bstack1ll1l_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ੐") in testContextOptions and str(testContextOptions[bstack1ll1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫੑ")]).lower() == bstack1ll1l_opy_ (u"ࠪࡸࡷࡻࡥࠨ੒")):
      bstack111l11l1l1_opy_ = True
    bstack111111ll_opy_.bstack1llllll1l1_opy_(testContextOptions.get(bstack1ll1l_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ੓"), False))
  else:
    bstack111l11l1l1_opy_ = True
    bstack111111ll_opy_.bstack1llllll1l1_opy_(True)
def bstack1l1l1ll1l1_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack111lllll1_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1l111l1l_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1ll1l_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡩ࡯࡯ࡨ࡬࡫࡫࡯࡬ࡦࠤ੔") == args[i].lower() or bstack1ll1l_opy_ (u"ࠨ࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡱࡪ࡮࡭ࠢ੕") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack111l1ll111_opy_
      bstack111l1ll111_opy_ += bstack1ll1l_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡄࡱࡱࡪ࡮࡭ࡆࡪ࡮ࡨࠤࠬ੖") + shlex.quote(path)
      return path
  return None
bstack111l11ll1_opy_ = re.compile(bstack1ll1l_opy_ (u"ࡳࠤ࠱࠮ࡄࡢࠤࡼࠪ࠱࠮ࡄ࠯ࡽ࠯ࠬࡂࠦ੗"))
def bstack1ll1ll1lll_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack111l11ll1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1ll1l_opy_ (u"ࠤࠧࡿࠧ੘") + group + bstack1ll1l_opy_ (u"ࠥࢁࠧਖ਼"), os.environ.get(group))
  return value
def bstack1l11ll11l_opy_():
  global bstack111l1l111_opy_
  if bstack111l1l111_opy_ is None:
        bstack111l1l111_opy_ = bstack1l1l111l1l_opy_()
  bstack1l1l1ll11l_opy_ = bstack111l1l111_opy_
  if bstack1l1l1ll11l_opy_ and os.path.exists(os.path.abspath(bstack1l1l1ll11l_opy_)):
    fileName = bstack1l1l1ll11l_opy_
  if bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨਗ਼") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆࠩਜ਼")])) and not bstack1ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨੜ") in locals():
    fileName = os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ੝")]
  if bstack1ll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡔࡡ࡮ࡧࠪਫ਼") in locals():
    bstack1ll1ll_opy_ = os.path.abspath(fileName)
  else:
    bstack1ll1ll_opy_ = bstack1ll1l_opy_ (u"ࠩࠪ੟")
  bstack111lllll1l_opy_ = os.getcwd()
  bstack1ll11l1ll_opy_ = bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭੠")
  bstack1l1111l11_opy_ = bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡦࡳ࡬ࠨ੡")
  while (not os.path.exists(bstack1ll1ll_opy_)) and bstack111lllll1l_opy_ != bstack1ll1l_opy_ (u"ࠧࠨ੢"):
    bstack1ll1ll_opy_ = os.path.join(bstack111lllll1l_opy_, bstack1ll11l1ll_opy_)
    if not os.path.exists(bstack1ll1ll_opy_):
      bstack1ll1ll_opy_ = os.path.join(bstack111lllll1l_opy_, bstack1l1111l11_opy_)
    if bstack111lllll1l_opy_ != os.path.dirname(bstack111lllll1l_opy_):
      bstack111lllll1l_opy_ = os.path.dirname(bstack111lllll1l_opy_)
    else:
      bstack111lllll1l_opy_ = bstack1ll1l_opy_ (u"ࠨࠢ੣")
  bstack111l1l111_opy_ = bstack1ll1ll_opy_ if os.path.exists(bstack1ll1ll_opy_) else None
  return bstack111l1l111_opy_
def bstack11lll1ll11_opy_(config):
    if bstack1ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧ੤") in config:
      config[bstack1ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ੥")] = config[bstack1ll1l_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࠩ੦")]
    if bstack1ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࡒࡴࡹ࡯࡯࡯ࡵࠪ੧") in config:
      config[bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ੨")] = config[bstack1ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࡔࡶࡴࡪࡱࡱࡷࠬ੩")]
def bstack1111ll1ll_opy_():
  bstack1ll1ll_opy_ = bstack1l11ll11l_opy_()
  if not os.path.exists(bstack1ll1ll_opy_):
    bstack1lllll1l11_opy_(
      bstack1ll1l1ll1l_opy_.format(os.getcwd()))
  try:
    with open(bstack1ll1ll_opy_, bstack1ll1l_opy_ (u"࠭ࡲࠨ੪")) as stream:
      yaml.add_implicit_resolver(bstack1ll1l_opy_ (u"ࠢࠢࡲࡤࡸ࡭࡫ࡸࠣ੫"), bstack111l11ll1_opy_)
      yaml.add_constructor(bstack1ll1l_opy_ (u"ࠣࠣࡳࡥࡹ࡮ࡥࡹࠤ੬"), bstack1ll1ll1lll_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack11lll1ll11_opy_(config)
      return config
  except:
    with open(bstack1ll1ll_opy_, bstack1ll1l_opy_ (u"ࠩࡵࠫ੭")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack11lll1ll11_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1lllll1l11_opy_(bstack11ll111lll_opy_.format(str(exc)))
def bstack1111l111l_opy_(config):
  bstack1l11llllll_opy_ = bstack1l1l111l1_opy_(config)
  for option in list(bstack1l11llllll_opy_):
    if option.lower() in bstack11lllll1l_opy_ and option != bstack11lllll1l_opy_[option.lower()]:
      bstack1l11llllll_opy_[bstack11lllll1l_opy_[option.lower()]] = bstack1l11llllll_opy_[option]
      del bstack1l11llllll_opy_[option]
  return config
def bstack11l111llll_opy_():
  global bstack1ll11lllll_opy_
  for key, bstack1l111llll_opy_ in bstack1ll111ll1_opy_.items():
    if isinstance(bstack1l111llll_opy_, list):
      for var in bstack1l111llll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1ll11lllll_opy_[key] = os.environ[var]
          break
    elif bstack1l111llll_opy_ in os.environ and os.environ[bstack1l111llll_opy_] and str(os.environ[bstack1l111llll_opy_]).strip():
      bstack1ll11lllll_opy_[key] = os.environ[bstack1l111llll_opy_]
  if bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ੮") in os.environ:
    bstack1ll11lllll_opy_[bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੯")] = {}
    bstack1ll11lllll_opy_[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩੰ")][bstack1ll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨੱ")] = os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩੲ")]
def bstack1ll1111ll1_opy_():
  global bstack1l1l1l1l1_opy_
  global bstack111l1ll111_opy_
  bstack11lllll1l1_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack1ll1l_opy_ (u"ࠨ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫੳ").lower() == val.lower():
      bstack1l1l1l1l1_opy_[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ੴ")] = {}
      bstack1l1l1l1l1_opy_[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧੵ")][bstack1ll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੶")] = sys.argv[idx + 1]
      bstack11lllll1l1_opy_.extend([idx, idx + 1])
      break
  for key, bstack1l1111lll1_opy_ in bstack1ll1ll111l_opy_.items():
    if isinstance(bstack1l1111lll1_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack1l1111lll1_opy_:
          if bstack1ll1l_opy_ (u"ࠬ࠳࠭ࠨ੷") + var.lower() == val.lower() and key not in bstack1l1l1l1l1_opy_:
            bstack1l1l1l1l1_opy_[key] = sys.argv[idx + 1]
            bstack111l1ll111_opy_ += bstack1ll1l_opy_ (u"࠭ࠠ࠮࠯ࠪ੸") + var + bstack1ll1l_opy_ (u"ࠧࠡࠩ੹") + shlex.quote(sys.argv[idx + 1])
            bstack11lllll1l1_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack1ll1l_opy_ (u"ࠨ࠯࠰ࠫ੺") + bstack1l1111lll1_opy_.lower() == val.lower() and key not in bstack1l1l1l1l1_opy_:
          bstack1l1l1l1l1_opy_[key] = sys.argv[idx + 1]
          bstack111l1ll111_opy_ += bstack1ll1l_opy_ (u"ࠩࠣ࠱࠲࠭੻") + bstack1l1111lll1_opy_ + bstack1ll1l_opy_ (u"ࠪࠤࠬ੼") + shlex.quote(sys.argv[idx + 1])
          bstack11lllll1l1_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack11lllll1l1_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack11l1l11l1_opy_(config):
  bstack1lll1l1ll1_opy_ = config.keys()
  for bstack111l1l1l1l_opy_, bstack1ll111l11l_opy_ in bstack11111ll11l_opy_.items():
    if bstack1ll111l11l_opy_ in bstack1lll1l1ll1_opy_:
      config[bstack111l1l1l1l_opy_] = config[bstack1ll111l11l_opy_]
      del config[bstack1ll111l11l_opy_]
  for bstack111l1l1l1l_opy_, bstack1ll111l11l_opy_ in bstack11ll111ll_opy_.items():
    if isinstance(bstack1ll111l11l_opy_, list):
      for bstack1111l1l111_opy_ in bstack1ll111l11l_opy_:
        if bstack1111l1l111_opy_ in bstack1lll1l1ll1_opy_:
          config[bstack111l1l1l1l_opy_] = config[bstack1111l1l111_opy_]
          del config[bstack1111l1l111_opy_]
          break
    elif bstack1ll111l11l_opy_ in bstack1lll1l1ll1_opy_:
      config[bstack111l1l1l1l_opy_] = config[bstack1ll111l11l_opy_]
      del config[bstack1ll111l11l_opy_]
  for bstack1111l1l111_opy_ in list(config):
    for bstack111ll1ll1_opy_ in bstack1ll11ll11l_opy_:
      if bstack1111l1l111_opy_.lower() == bstack111ll1ll1_opy_.lower() and bstack1111l1l111_opy_ != bstack111ll1ll1_opy_:
        config[bstack111ll1ll1_opy_] = config[bstack1111l1l111_opy_]
        del config[bstack1111l1l111_opy_]
  bstack111l11l11_opy_ = [{}]
  if not config.get(bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ੽")):
    config[bstack1ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ੾")] = [{}]
  bstack111l11l11_opy_ = config[bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ੿")]
  for platform in bstack111l11l11_opy_:
    for bstack1111l1l111_opy_ in list(platform):
      for bstack111ll1ll1_opy_ in bstack1ll11ll11l_opy_:
        if bstack1111l1l111_opy_.lower() == bstack111ll1ll1_opy_.lower() and bstack1111l1l111_opy_ != bstack111ll1ll1_opy_:
          platform[bstack111ll1ll1_opy_] = platform[bstack1111l1l111_opy_]
          del platform[bstack1111l1l111_opy_]
  for bstack111l1l1l1l_opy_, bstack1ll111l11l_opy_ in bstack11ll111ll_opy_.items():
    for platform in bstack111l11l11_opy_:
      if isinstance(bstack1ll111l11l_opy_, list):
        for bstack1111l1l111_opy_ in bstack1ll111l11l_opy_:
          if bstack1111l1l111_opy_ in platform:
            platform[bstack111l1l1l1l_opy_] = platform[bstack1111l1l111_opy_]
            del platform[bstack1111l1l111_opy_]
            break
      elif bstack1ll111l11l_opy_ in platform:
        platform[bstack111l1l1l1l_opy_] = platform[bstack1ll111l11l_opy_]
        del platform[bstack1ll111l11l_opy_]
  for bstack11l1l11ll1_opy_ in bstack1l111l111_opy_:
    if bstack11l1l11ll1_opy_ in config:
      if not bstack1l111l111_opy_[bstack11l1l11ll1_opy_] in config:
        config[bstack1l111l111_opy_[bstack11l1l11ll1_opy_]] = {}
      config[bstack1l111l111_opy_[bstack11l1l11ll1_opy_]].update(config[bstack11l1l11ll1_opy_])
      del config[bstack11l1l11ll1_opy_]
  for platform in bstack111l11l11_opy_:
    for bstack11l1l11ll1_opy_ in bstack1l111l111_opy_:
      if bstack11l1l11ll1_opy_ in list(platform):
        if not bstack1l111l111_opy_[bstack11l1l11ll1_opy_] in platform:
          platform[bstack1l111l111_opy_[bstack11l1l11ll1_opy_]] = {}
        platform[bstack1l111l111_opy_[bstack11l1l11ll1_opy_]].update(platform[bstack11l1l11ll1_opy_])
        del platform[bstack11l1l11ll1_opy_]
  config = bstack1111l111l_opy_(config)
  return config
def bstack111l11ll1l_opy_(config):
  global bstack1l1lllll11_opy_
  bstack1l11ll1111_opy_ = False
  if bstack1ll1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ઀") in config and str(config[bstack1ll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬઁ")]).lower() != bstack1ll1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨં"):
    if bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧઃ") not in config or str(config[bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ઄")]).lower() == bstack1ll1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫઅ"):
      config[bstack1ll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬઆ")] = False
    else:
      bstack11ll1l1ll_opy_ = bstack1l1l1lll11_opy_()
      if bstack1ll1l_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬઇ") in bstack11ll1l1ll_opy_:
        if not bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬઈ") in config:
          config[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઉ")] = {}
        config[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઊ")][bstack1ll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ઋ")] = bstack1ll1l_opy_ (u"ࠬࡧࡴࡴ࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠫઌ")
        bstack1l11ll1111_opy_ = True
        bstack1l1lllll11_opy_ = config[bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪઍ")].get(bstack1ll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઎"))
  if bstack11l11ll11_opy_(config) and bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬએ") in config and str(config[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ઐ")]).lower() != bstack1ll1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩઑ") and not bstack1l11ll1111_opy_:
    if not bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ઒") in config:
      config[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩઓ")] = {}
    if not config[bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪઔ")].get(bstack1ll1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠫક")) and not bstack1ll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪખ") in config[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ગ")]:
      bstack1l1l1lll_opy_ = datetime.datetime.now()
      bstack11111l11l_opy_ = bstack1l1l1lll_opy_.strftime(bstack1ll1l_opy_ (u"ࠪࠩࡩࡥࠥࡣࡡࠨࡌࠪࡓࠧઘ"))
      hostname = socket.gethostname()
      bstack11ll1ll1ll_opy_ = bstack1ll1l_opy_ (u"ࠫࠬઙ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1ll1l_opy_ (u"ࠬࢁࡽࡠࡽࢀࡣࢀࢃࠧચ").format(bstack11111l11l_opy_, hostname, bstack11ll1ll1ll_opy_)
      config[bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪછ")][bstack1ll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩજ")] = identifier
    bstack1l1lllll11_opy_ = config[bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬઝ")].get(bstack1ll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫઞ"))
  return config
def bstack11l1l111l_opy_():
  bstack111l1l1l1_opy_ =  bstack1ll1l11l1_opy_()[bstack1ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠩટ")]
  return bstack111l1l1l1_opy_ if bstack111l1l1l1_opy_ else -1
def bstack111llllll_opy_(bstack111l1l1l1_opy_):
  global CONFIG
  if not bstack1ll1l_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ઠ") in CONFIG[bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧડ")]:
    return
  CONFIG[bstack1ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨઢ")] = CONFIG[bstack1ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩણ")].replace(
    bstack1ll1l_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪત"),
    str(bstack111l1l1l1_opy_)
  )
def bstack1lllll1ll1_opy_():
  global CONFIG
  if not bstack1ll1l_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨથ") in CONFIG[bstack1ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬદ")]:
    return
  bstack1l1l1lll_opy_ = datetime.datetime.now()
  bstack11111l11l_opy_ = bstack1l1l1lll_opy_.strftime(bstack1ll1l_opy_ (u"ࠫࠪࡪ࠭ࠦࡤ࠰ࠩࡍࡀࠥࡎࠩધ"))
  CONFIG[bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧન")] = CONFIG[bstack1ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ઩")].replace(
    bstack1ll1l_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭પ"),
    bstack11111l11l_opy_
  )
def bstack11111lll11_opy_():
  global CONFIG
  if bstack1ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪફ") in CONFIG and not bool(CONFIG[bstack1ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫબ")]):
    del CONFIG[bstack1ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬભ")]
    return
  if not bstack1ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭મ") in CONFIG:
    CONFIG[bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧય")] = bstack1ll1l_opy_ (u"࠭ࠣࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩર")
  if bstack1ll1l_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭઱") in CONFIG[bstack1ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪલ")]:
    bstack1lllll1ll1_opy_()
    os.environ[bstack1ll1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭ળ")] = CONFIG[bstack1ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ઴")]
  if not bstack1ll1l_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭વ") in CONFIG[bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧશ")]:
    return
  bstack111l1l1l1_opy_ = bstack1ll1l_opy_ (u"࠭ࠧષ")
  bstack1l111ll11l_opy_ = bstack11l1l111l_opy_()
  if bstack1l111ll11l_opy_ != -1:
    bstack111l1l1l1_opy_ = bstack1ll1l_opy_ (u"ࠧࡄࡋࠣࠫસ") + str(bstack1l111ll11l_opy_)
  if bstack111l1l1l1_opy_ == bstack1ll1l_opy_ (u"ࠨࠩહ"):
    bstack111ll11lll_opy_ = bstack11l1ll11l1_opy_(CONFIG[bstack1ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ઺")])
    if bstack111ll11lll_opy_ != -1:
      bstack111l1l1l1_opy_ = str(bstack111ll11lll_opy_)
  if bstack111l1l1l1_opy_:
    bstack111llllll_opy_(bstack111l1l1l1_opy_)
    os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧ઻")] = CONFIG[bstack1ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ઼࠭")]
def bstack1ll1lll11_opy_(bstack11lll1lll_opy_, bstack1l1lll11ll_opy_, path):
  json_data = {
    bstack1ll1l_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩઽ"): bstack1l1lll11ll_opy_
  }
  if os.path.exists(path):
    bstack11111llll_opy_ = json.load(open(path, bstack1ll1l_opy_ (u"࠭ࡲࡣࠩા")))
  else:
    bstack11111llll_opy_ = {}
  bstack11111llll_opy_[bstack11lll1lll_opy_] = json_data
  with open(path, bstack1ll1l_opy_ (u"ࠢࡸ࠭ࠥિ")) as outfile:
    json.dump(bstack11111llll_opy_, outfile)
def bstack11l1ll11l1_opy_(bstack11lll1lll_opy_):
  bstack11lll1lll_opy_ = str(bstack11lll1lll_opy_)
  bstack1l1l1lllll_opy_ = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠨࢀࠪી")), bstack1ll1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩુ"))
  try:
    if not os.path.exists(bstack1l1l1lllll_opy_):
      os.makedirs(bstack1l1l1lllll_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠪࢂࠬૂ")), bstack1ll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫૃ"), bstack1ll1l_opy_ (u"ࠬ࠴ࡢࡶ࡫࡯ࡨ࠲ࡴࡡ࡮ࡧ࠰ࡧࡦࡩࡨࡦ࠰࡭ࡷࡴࡴࠧૄ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1ll1l_opy_ (u"࠭ࡷࠨૅ")):
        pass
      with open(file_path, bstack1ll1l_opy_ (u"ࠢࡸ࠭ࠥ૆")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1ll1l_opy_ (u"ࠨࡴࠪે")) as bstack1lll11l11_opy_:
      bstack1l1lll1l1_opy_ = json.load(bstack1lll11l11_opy_)
    if bstack11lll1lll_opy_ in bstack1l1lll1l1_opy_:
      bstack111lllll11_opy_ = bstack1l1lll1l1_opy_[bstack11lll1lll_opy_][bstack1ll1l_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ૈ")]
      bstack11111l111_opy_ = int(bstack111lllll11_opy_) + 1
      bstack1ll1lll11_opy_(bstack11lll1lll_opy_, bstack11111l111_opy_, file_path)
      return bstack11111l111_opy_
    else:
      bstack1ll1lll11_opy_(bstack11lll1lll_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack11ll11llll_opy_.format(str(e)))
    return -1
def bstack1111lllll1_opy_(config):
  if not config[bstack1ll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬૉ")] or not config[bstack1ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ૊")]:
    return True
  else:
    return False
def bstack111l11l1l_opy_(config, index=0):
  global bstack11lll11l1l_opy_
  bstack1llll1ll11_opy_ = {}
  caps = bstack1ll11l111l_opy_ + bstack1l11l11l1_opy_
  if config.get(bstack1ll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩો"), False):
    bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪૌ")] = True
    bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶ્ࠫ")] = config.get(bstack1ll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷࠬ૎"), {})
  if bstack11lll11l1l_opy_:
    caps += bstack1llll11l11_opy_
  for key in config:
    if key in caps + [bstack1ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૏")]:
      continue
    bstack1llll1ll11_opy_[key] = config[key]
  if bstack1ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ૐ") in config:
    for bstack1ll111l1l_opy_ in config[bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૑")][index]:
      if bstack1ll111l1l_opy_ in caps:
        continue
      bstack1llll1ll11_opy_[bstack1ll111l1l_opy_] = config[bstack1ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૒")][index][bstack1ll111l1l_opy_]
  bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"࠭ࡨࡰࡵࡷࡒࡦࡳࡥࠨ૓")] = socket.gethostname()
  if bstack1ll1l_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ૔") in bstack1llll1ll11_opy_:
    del (bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ૕")])
  return bstack1llll1ll11_opy_
def bstack11lll111l1_opy_(config):
  global bstack11lll11l1l_opy_
  bstack1l11l1l1l1_opy_ = {}
  caps = bstack1l11l11l1_opy_
  if bstack11lll11l1l_opy_:
    caps += bstack1llll11l11_opy_
  for key in caps:
    if key in config:
      bstack1l11l1l1l1_opy_[key] = config[key]
  return bstack1l11l1l1l1_opy_
def bstack1l11l1lll_opy_(bstack1llll1ll11_opy_, bstack1l11l1l1l1_opy_):
  bstack1llllllll1_opy_ = {}
  for key in bstack1llll1ll11_opy_.keys():
    if key in bstack11111ll11l_opy_:
      bstack1llllllll1_opy_[bstack11111ll11l_opy_[key]] = bstack1llll1ll11_opy_[key]
    else:
      bstack1llllllll1_opy_[key] = bstack1llll1ll11_opy_[key]
  for key in bstack1l11l1l1l1_opy_:
    if key in bstack11111ll11l_opy_:
      bstack1llllllll1_opy_[bstack11111ll11l_opy_[key]] = bstack1l11l1l1l1_opy_[key]
    else:
      bstack1llllllll1_opy_[key] = bstack1l11l1l1l1_opy_[key]
  return bstack1llllllll1_opy_
def bstack11llll1l11_opy_(config, index=0):
  global bstack11lll11l1l_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1l11l111l_opy_ = bstack1l1lll1ll_opy_(bstack1l1111l1l1_opy_, config, logger)
  bstack1l11l1l1l1_opy_ = bstack11lll111l1_opy_(config)
  bstack1111l11l11_opy_ = bstack1l11l11l1_opy_
  bstack1111l11l11_opy_ += bstack11111l1ll1_opy_
  bstack1l11l1l1l1_opy_ = update(bstack1l11l1l1l1_opy_, bstack1l11l111l_opy_)
  if bstack11lll11l1l_opy_:
    bstack1111l11l11_opy_ += bstack1llll11l11_opy_
  if bstack1ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૖") in config:
    if bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ૗") in config[bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૘")][index]:
      caps[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ૙")] = config[bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૚")][index][bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ૛")]
    if bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ૜") in config[bstack1ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૝")][index]:
      caps[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ૞")] = str(config[bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૟")][index][bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ૠ")])
    bstack1l1ll111ll_opy_ = bstack1l1lll1ll_opy_(bstack1l1111l1l1_opy_, config[bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩૡ")][index], logger)
    bstack1111l11l11_opy_ += list(bstack1l1ll111ll_opy_.keys())
    for bstack1l1l1l1111_opy_ in bstack1111l11l11_opy_:
      if bstack1l1l1l1111_opy_ in config[bstack1ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪૢ")][index]:
        if bstack1l1l1l1111_opy_ == bstack1ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪૣ"):
          try:
            bstack1l1ll111ll_opy_[bstack1l1l1l1111_opy_] = str(config[bstack1ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૤")][index][bstack1l1l1l1111_opy_] * 1.0)
          except:
            bstack1l1ll111ll_opy_[bstack1l1l1l1111_opy_] = str(config[bstack1ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૥")][index][bstack1l1l1l1111_opy_])
        else:
          bstack1l1ll111ll_opy_[bstack1l1l1l1111_opy_] = config[bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૦")][index][bstack1l1l1l1111_opy_]
        del (config[bstack1ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૧")][index][bstack1l1l1l1111_opy_])
    bstack1l11l1l1l1_opy_ = update(bstack1l11l1l1l1_opy_, bstack1l1ll111ll_opy_)
  bstack1llll1ll11_opy_ = bstack111l11l1l_opy_(config, index)
  for bstack1111l1l111_opy_ in bstack1l11l11l1_opy_ + list(bstack1l11l111l_opy_.keys()):
    if bstack1111l1l111_opy_ in bstack1llll1ll11_opy_:
      bstack1l11l1l1l1_opy_[bstack1111l1l111_opy_] = bstack1llll1ll11_opy_[bstack1111l1l111_opy_]
      del (bstack1llll1ll11_opy_[bstack1111l1l111_opy_])
  if bstack1l1ll1ll1l_opy_(config):
    bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭૨")] = True
    caps.update(bstack1l11l1l1l1_opy_)
    caps[bstack1ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ૩")] = bstack1llll1ll11_opy_
  else:
    bstack1llll1ll11_opy_[bstack1ll1l_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨ૪")] = False
    caps.update(bstack1l11l1lll_opy_(bstack1llll1ll11_opy_, bstack1l11l1l1l1_opy_))
    if bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ૫") in caps:
      caps[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫ૬")] = caps[bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ૭")]
      del (caps[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ૮")])
    if bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ૯") in caps:
      caps[bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ૰")] = caps[bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ૱")]
      del (caps[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ૲")])
  return caps
def bstack1l1l1llll_opy_():
  global bstack111ll11l1l_opy_
  global CONFIG
  if bstack111lllll1_opy_() <= version.parse(bstack1ll1l_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪ૳")):
    if bstack111ll11l1l_opy_ != bstack1ll1l_opy_ (u"ࠫࠬ૴"):
      return bstack1ll1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨ૵") + bstack111ll11l1l_opy_ + bstack1ll1l_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥ૶")
    return bstack1llll1l1ll_opy_
  if bstack111ll11l1l_opy_ != bstack1ll1l_opy_ (u"ࠧࠨ૷"):
    return bstack1ll1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥ૸") + bstack111ll11l1l_opy_ + bstack1ll1l_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥૹ")
  return bstack111l1llll1_opy_
def bstack1l111l11ll_opy_(options):
  return hasattr(options, bstack1ll1l_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫૺ"))
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
def bstack1ll111111_opy_(options, bstack1l1ll1l111_opy_):
  for bstack1l111ll1l_opy_ in bstack1l1ll1l111_opy_:
    if bstack1l111ll1l_opy_ in [bstack1ll1l_opy_ (u"ࠫࡦࡸࡧࡴࠩૻ"), bstack1ll1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩૼ")]:
      continue
    if bstack1l111ll1l_opy_ in options._experimental_options:
      options._experimental_options[bstack1l111ll1l_opy_] = update(options._experimental_options[bstack1l111ll1l_opy_],
                                                         bstack1l1ll1l111_opy_[bstack1l111ll1l_opy_])
    else:
      options.add_experimental_option(bstack1l111ll1l_opy_, bstack1l1ll1l111_opy_[bstack1l111ll1l_opy_])
  if bstack1ll1l_opy_ (u"࠭ࡡࡳࡩࡶࠫ૽") in bstack1l1ll1l111_opy_:
    for arg in bstack1l1ll1l111_opy_[bstack1ll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬ૾")]:
      options.add_argument(arg)
    del (bstack1l1ll1l111_opy_[bstack1ll1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭૿")])
  if bstack1ll1l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭଀") in bstack1l1ll1l111_opy_:
    for ext in bstack1l1ll1l111_opy_[bstack1ll1l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧଁ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l1ll1l111_opy_[bstack1ll1l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨଂ")])
def bstack1l111ll111_opy_(options, bstack11ll111l1l_opy_):
  if bstack1ll1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫଃ") in bstack11ll111l1l_opy_:
    for bstack1l11111ll_opy_ in bstack11ll111l1l_opy_[bstack1ll1l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ଄")]:
      if bstack1l11111ll_opy_ in options._preferences:
        options._preferences[bstack1l11111ll_opy_] = update(options._preferences[bstack1l11111ll_opy_], bstack11ll111l1l_opy_[bstack1ll1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ଅ")][bstack1l11111ll_opy_])
      else:
        options.set_preference(bstack1l11111ll_opy_, bstack11ll111l1l_opy_[bstack1ll1l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧଆ")][bstack1l11111ll_opy_])
  if bstack1ll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧଇ") in bstack11ll111l1l_opy_:
    for arg in bstack11ll111l1l_opy_[bstack1ll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଈ")]:
      options.add_argument(arg)
def bstack11l111l1l1_opy_(options, bstack1l1l1l1ll_opy_):
  if bstack1ll1l_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬଉ") in bstack1l1l1l1ll_opy_:
    options.use_webview(bool(bstack1l1l1l1ll_opy_[bstack1ll1l_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭ଊ")]))
  bstack1ll111111_opy_(options, bstack1l1l1l1ll_opy_)
def bstack1ll1l1llll_opy_(options, bstack11ll11l1l_opy_):
  for bstack1ll1l11111_opy_ in bstack11ll11l1l_opy_:
    if bstack1ll1l11111_opy_ in [bstack1ll1l_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪଋ"), bstack1ll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬଌ")]:
      continue
    options.set_capability(bstack1ll1l11111_opy_, bstack11ll11l1l_opy_[bstack1ll1l11111_opy_])
  if bstack1ll1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭଍") in bstack11ll11l1l_opy_:
    for arg in bstack11ll11l1l_opy_[bstack1ll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ଎")]:
      options.add_argument(arg)
  if bstack1ll1l_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧଏ") in bstack11ll11l1l_opy_:
    options.bstack1l1ll11lll_opy_(bool(bstack11ll11l1l_opy_[bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨଐ")]))
def bstack1l1l1111ll_opy_(options, bstack111lll1l1_opy_):
  for bstack1l11l1l11_opy_ in bstack111lll1l1_opy_:
    if bstack1l11l1l11_opy_ in [bstack1ll1l_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ଑"), bstack1ll1l_opy_ (u"࠭ࡡࡳࡩࡶࠫ଒")]:
      continue
    options._options[bstack1l11l1l11_opy_] = bstack111lll1l1_opy_[bstack1l11l1l11_opy_]
  if bstack1ll1l_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଓ") in bstack111lll1l1_opy_:
    for bstack11lll1l11l_opy_ in bstack111lll1l1_opy_[bstack1ll1l_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬଔ")]:
      options.bstack1ll1111ll_opy_(
        bstack11lll1l11l_opy_, bstack111lll1l1_opy_[bstack1ll1l_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭କ")][bstack11lll1l11l_opy_])
  if bstack1ll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଖ") in bstack111lll1l1_opy_:
    for arg in bstack111lll1l1_opy_[bstack1ll1l_opy_ (u"ࠫࡦࡸࡧࡴࠩଗ")]:
      options.add_argument(arg)
def bstack111ll111l1_opy_(options, caps):
  if not hasattr(options, bstack1ll1l_opy_ (u"ࠬࡑࡅ࡚ࠩଘ")):
    return
  if options.KEY == bstack1ll1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫଙ"):
    options = bstack1lllllll1_opy_.bstack11l1llll1l_opy_(bstack1l1l1l111l_opy_=options, config=CONFIG)
  if options.KEY == bstack1ll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬଚ") and options.KEY in caps:
    bstack1ll111111_opy_(options, caps[bstack1ll1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ଛ")])
  elif options.KEY == bstack1ll1l_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧଜ") and options.KEY in caps:
    bstack1l111ll111_opy_(options, caps[bstack1ll1l_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨଝ")])
  elif options.KEY == bstack1ll1l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬଞ") and options.KEY in caps:
    bstack1ll1l1llll_opy_(options, caps[bstack1ll1l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ଟ")])
  elif options.KEY == bstack1ll1l_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧଠ") and options.KEY in caps:
    bstack11l111l1l1_opy_(options, caps[bstack1ll1l_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨଡ")])
  elif options.KEY == bstack1ll1l_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧଢ") and options.KEY in caps:
    bstack1l1l1111ll_opy_(options, caps[bstack1ll1l_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨଣ")])
def bstack1lll111ll1_opy_(caps):
  global bstack11lll11l1l_opy_
  if isinstance(os.environ.get(bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫତ")), str):
    bstack11lll11l1l_opy_ = eval(os.getenv(bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬଥ")))
  if bstack11lll11l1l_opy_:
    if bstack1l1l1ll1l1_opy_() < version.parse(bstack1ll1l_opy_ (u"ࠬ࠸࠮࠴࠰࠳ࠫଦ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1ll1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ଧ")
    if bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬନ") in caps:
      browser = caps[bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭଩")]
    elif bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪପ") in caps:
      browser = caps[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫଫ")]
    browser = str(browser).lower()
    if browser == bstack1ll1l_opy_ (u"ࠫ࡮ࡶࡨࡰࡰࡨࠫବ") or browser == bstack1ll1l_opy_ (u"ࠬ࡯ࡰࡢࡦࠪଭ"):
      browser = bstack1ll1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭ମ")
    if browser == bstack1ll1l_opy_ (u"ࠧࡴࡣࡰࡷࡺࡴࡧࠨଯ"):
      browser = bstack1ll1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨର")
    if browser not in [bstack1ll1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩ଱"), bstack1ll1l_opy_ (u"ࠪࡩࡩ࡭ࡥࠨଲ"), bstack1ll1l_opy_ (u"ࠫ࡮࡫ࠧଳ"), bstack1ll1l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬ଴"), bstack1ll1l_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧଵ")]:
      return None
    try:
      package = bstack1ll1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶ࠳ࢁࡽ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩଶ").format(browser)
      name = bstack1ll1l_opy_ (u"ࠨࡑࡳࡸ࡮ࡵ࡮ࡴࠩଷ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1l111l11ll_opy_(options):
        return None
      for bstack1111l1l111_opy_ in caps.keys():
        options.set_capability(bstack1111l1l111_opy_, caps[bstack1111l1l111_opy_])
      bstack111ll111l1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack11llllllll_opy_(options, bstack11l11l1l11_opy_):
  if not bstack1l111l11ll_opy_(options):
    return
  for bstack1111l1l111_opy_ in bstack11l11l1l11_opy_.keys():
    if bstack1111l1l111_opy_ in bstack11111l1ll1_opy_:
      continue
    if bstack1111l1l111_opy_ in options._caps and type(options._caps[bstack1111l1l111_opy_]) in [dict, list]:
      options._caps[bstack1111l1l111_opy_] = update(options._caps[bstack1111l1l111_opy_], bstack11l11l1l11_opy_[bstack1111l1l111_opy_])
    else:
      options.set_capability(bstack1111l1l111_opy_, bstack11l11l1l11_opy_[bstack1111l1l111_opy_])
  bstack111ll111l1_opy_(options, bstack11l11l1l11_opy_)
  if bstack1ll1l_opy_ (u"ࠩࡰࡳࡿࡀࡤࡦࡤࡸ࡫࡬࡫ࡲࡂࡦࡧࡶࡪࡹࡳࠨସ") in options._caps:
    if options._caps[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨହ")] and options._caps[bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ଺")].lower() != bstack1ll1l_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭଻"):
      del options._caps[bstack1ll1l_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷ଼ࠬ")]
def bstack111l1l1ll1_opy_(proxy_config):
  if bstack1ll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫଽ") in proxy_config:
    proxy_config[bstack1ll1l_opy_ (u"ࠨࡵࡶࡰࡕࡸ࡯ࡹࡻࠪା")] = proxy_config[bstack1ll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ି")]
    del (proxy_config[bstack1ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧୀ")])
  if bstack1ll1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧୁ") in proxy_config and proxy_config[bstack1ll1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨୂ")].lower() != bstack1ll1l_opy_ (u"࠭ࡤࡪࡴࡨࡧࡹ࠭ୃ"):
    proxy_config[bstack1ll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪୄ")] = bstack1ll1l_opy_ (u"ࠨ࡯ࡤࡲࡺࡧ࡬ࠨ୅")
  if bstack1ll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡂࡷࡷࡳࡨࡵ࡮ࡧ࡫ࡪ࡙ࡷࡲࠧ୆") in proxy_config:
    proxy_config[bstack1ll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭େ")] = bstack1ll1l_opy_ (u"ࠫࡵࡧࡣࠨୈ")
  return proxy_config
def bstack11llll1l1l_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1ll1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ୉") in config:
    return proxy
  config[bstack1ll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୊")] = bstack111l1l1ll1_opy_(config[bstack1ll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭ୋ")])
  if proxy == None:
    proxy = Proxy(config[bstack1ll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧୌ")])
  return proxy
def bstack11ll1llll1_opy_(self):
  global CONFIG
  global bstack11l111ll11_opy_
  try:
    proxy = bstack1l111l11l_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1ll1l_opy_ (u"ࠩ࠱ࡴࡦࡩ୍ࠧ")):
        proxies = bstack11l1l1l1l1_opy_(proxy, bstack1l1l1llll_opy_())
        if len(proxies) > 0:
          protocol, bstack111l111l1l_opy_ = proxies.popitem()
          if bstack1ll1l_opy_ (u"ࠥ࠾࠴࠵ࠢ୎") in bstack111l111l1l_opy_:
            return bstack111l111l1l_opy_
          else:
            return bstack1ll1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧ୏") + bstack111l111l1l_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡲࡵࡳࡽࡿࠠࡶࡴ࡯ࠤ࠿ࠦࡻࡾࠤ୐").format(str(e)))
  return bstack11l111ll11_opy_(self)
def bstack111lll1ll1_opy_():
  global CONFIG
  return bstack1l1llll111_opy_(CONFIG) and bstack111lll111_opy_() and bstack111lllll1_opy_() >= version.parse(bstack1llll111l1_opy_)
def bstack1lll1ll1ll_opy_():
  global CONFIG
  return (bstack1ll1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ୑") in CONFIG or bstack1ll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ୒") in CONFIG) and bstack1lll111111_opy_()
def bstack1l1l111l1_opy_(config):
  bstack1l11llllll_opy_ = {}
  if bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୓") in config:
    bstack1l11llllll_opy_ = config[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୔")]
  if bstack1ll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୕") in config:
    bstack1l11llllll_opy_ = config[bstack1ll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪୖ")]
  proxy = bstack1l111l11l_opy_(config)
  if proxy:
    if proxy.endswith(bstack1ll1l_opy_ (u"ࠬ࠴ࡰࡢࡥࠪୗ")) and os.path.isfile(proxy):
      bstack1l11llllll_opy_[bstack1ll1l_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩ୘")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1ll1l_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ୙")):
        proxies = bstack111l1l1ll_opy_(config, bstack1l1l1llll_opy_())
        if len(proxies) > 0:
          protocol, bstack111l111l1l_opy_ = proxies.popitem()
          if bstack1ll1l_opy_ (u"ࠣ࠼࠲࠳ࠧ୚") in bstack111l111l1l_opy_:
            parsed_url = urlparse(bstack111l111l1l_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1ll1l_opy_ (u"ࠤ࠽࠳࠴ࠨ୛") + bstack111l111l1l_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1l11llllll_opy_[bstack1ll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭ଡ଼")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1l11llllll_opy_[bstack1ll1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡳࡷࡺࠧଢ଼")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1l11llllll_opy_[bstack1ll1l_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨ୞")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1l11llllll_opy_[bstack1ll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩୟ")] = str(parsed_url.password)
  return bstack1l11llllll_opy_
def bstack11111l1ll_opy_(config):
  if bstack1ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬୠ") in config:
    return config[bstack1ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭ୡ")]
  return {}
def bstack11l1l1llll_opy_(caps):
  global bstack1l1lllll11_opy_
  if bstack1ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪୢ") in caps:
    caps[bstack1ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫୣ")][bstack1ll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪ୤")] = True
    if bstack1l1lllll11_opy_:
      caps[bstack1ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭୥")][bstack1ll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ୦")] = bstack1l1lllll11_opy_
  else:
    caps[bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬ୧")] = True
    if bstack1l1lllll11_opy_:
      caps[bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ୨")] = bstack1l1lllll11_opy_
@measure(event_name=EVENTS.bstack11lll1ll1_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack1lll1111ll_opy_():
  global CONFIG
  if not bstack11l11ll11_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭୩") in CONFIG and bstack1lll1ll111_opy_(CONFIG[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ୪")]):
    if (
      bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୫") in CONFIG
      and bstack1lll1ll111_opy_(CONFIG[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୬")].get(bstack1ll1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠪ୭")))
    ):
      logger.debug(bstack1ll1l_opy_ (u"ࠢࡍࡱࡦࡥࡱࠦࡢࡪࡰࡤࡶࡾࠦ࡮ࡰࡶࠣࡷࡹࡧࡲࡵࡧࡧࠤࡦࡹࠠࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡦࡰࡤࡦࡱ࡫ࡤࠣ୮"))
      return
    bstack1l11llllll_opy_ = bstack1l1l111l1_opy_(CONFIG)
    bstack11l11111l1_opy_(CONFIG[bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ୯")], bstack1l11llllll_opy_)
def bstack11l11111l1_opy_(key, bstack1l11llllll_opy_):
  global bstack1l11l1ll1_opy_
  logger.info(bstack11ll1l11ll_opy_)
  try:
    bstack1l11l1ll1_opy_ = Local()
    bstack1ll1l1l1l_opy_ = {bstack1ll1l_opy_ (u"ࠩ࡮ࡩࡾ࠭୰"): key}
    bstack1ll1l1l1l_opy_.update(bstack1l11llllll_opy_)
    logger.debug(bstack1ll1ll11l_opy_.format(str(bstack1ll1l1l1l_opy_)).replace(key, bstack1ll1l_opy_ (u"ࠪ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧୱ")))
    bstack1l11l1ll1_opy_.start(**bstack1ll1l1l1l_opy_)
    if bstack1l11l1ll1_opy_.isRunning():
      logger.info(bstack111llll1ll_opy_)
  except Exception as e:
    bstack1lllll1l11_opy_(bstack1l11l1l1l_opy_.format(str(e)))
def bstack1l11l11111_opy_():
  global bstack1l11l1ll1_opy_
  if bstack1l11l1ll1_opy_.isRunning():
    logger.info(bstack11lll111ll_opy_)
    bstack1l11l1ll1_opy_.stop()
  bstack1l11l1ll1_opy_ = None
def bstack1ll11ll1ll_opy_(bstack11ll11l111_opy_=[]):
  global CONFIG
  bstack1ll1111111_opy_ = []
  bstack1l11lll1l1_opy_ = [bstack1ll1l_opy_ (u"ࠫࡴࡹࠧ୲"), bstack1ll1l_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ୳"), bstack1ll1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ୴"), bstack1ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ୵"), bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭୶"), bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ୷")]
  try:
    for err in bstack11ll11l111_opy_:
      bstack1l1l1llll1_opy_ = {}
      for k in bstack1l11lll1l1_opy_:
        val = CONFIG[bstack1ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭୸")][int(err[bstack1ll1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ୹")])].get(k)
        if val:
          bstack1l1l1llll1_opy_[k] = val
      if(err[bstack1ll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ୺")] != bstack1ll1l_opy_ (u"࠭ࠧ୻")):
        bstack1l1l1llll1_opy_[bstack1ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡸ࠭୼")] = {
          err[bstack1ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭୽")]: err[bstack1ll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ୾")]
        }
        bstack1ll1111111_opy_.append(bstack1l1l1llll1_opy_)
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬࡯ࡳ࡯ࡤࡸࡹ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶ࠽ࠤࠬ୿") + str(e))
  finally:
    return bstack1ll1111111_opy_
def bstack1ll1llll1l_opy_(file_name):
  bstack111l11lll1_opy_ = []
  try:
    bstack1111l11l1l_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1111l11l1l_opy_):
      with open(bstack1111l11l1l_opy_) as f:
        bstack11lll1ll1l_opy_ = json.load(f)
        bstack111l11lll1_opy_ = bstack11lll1ll1l_opy_
      os.remove(bstack1111l11l1l_opy_)
    return bstack111l11lll1_opy_
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡪࡰࡧ࡭ࡳ࡭ࠠࡦࡴࡵࡳࡷࠦ࡬ࡪࡵࡷ࠾ࠥ࠭஀") + str(e))
    return bstack111l11lll1_opy_
def bstack1l1111111l_opy_():
  try:
      from bstack_utils.constants import bstack11l111111l_opy_, EVENTS
      from bstack_utils.helper import bstack1l11lllll_opy_, get_host_info, bstack111111ll_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack111l1ll1ll_opy_ = os.path.join(os.getcwd(), bstack1ll1l_opy_ (u"ࠬࡲ࡯ࡨࠩ஁"), bstack1ll1l_opy_ (u"࠭࡫ࡦࡻ࠰ࡱࡪࡺࡲࡪࡥࡶ࠲࡯ࡹ࡯࡯ࠩஂ"))
      lock = FileLock(bstack111l1ll1ll_opy_+bstack1ll1l_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨஃ"))
      def bstack1ll11l11_opy_():
          try:
              with lock:
                  with open(bstack111l1ll1ll_opy_, bstack1ll1l_opy_ (u"ࠣࡴࠥ஄"), encoding=bstack1ll1l_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣஅ")) as file:
                      data = json.load(file)
                      config = {
                          bstack1ll1l_opy_ (u"ࠥ࡬ࡪࡧࡤࡦࡴࡶࠦஆ"): {
                              bstack1ll1l_opy_ (u"ࠦࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠥஇ"): bstack1ll1l_opy_ (u"ࠧࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠣஈ"),
                          }
                      }
                      bstack1l1ll1111l_opy_ = datetime.utcnow()
                      bstack1l1l1lll_opy_ = bstack1l1ll1111l_opy_.strftime(bstack1ll1l_opy_ (u"ࠨ࡚ࠥ࠯ࠨࡱ࠲ࠫࡤࡕࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࠱ࠩ࡫ࠦࡕࡕࡅࠥஉ"))
                      test_id = os.environ.get(bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬஊ")) if os.environ.get(bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭஋")) else bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦ஌"))
                      payload = {
                          bstack1ll1l_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠢ஍"): bstack1ll1l_opy_ (u"ࠦࡸࡪ࡫ࡠࡧࡹࡩࡳࡺࡳࠣஎ"),
                          bstack1ll1l_opy_ (u"ࠧࡪࡡࡵࡣࠥஏ"): {
                              bstack1ll1l_opy_ (u"ࠨࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡶࡷ࡬ࡨࠧஐ"): test_id,
                              bstack1ll1l_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫ࡤࡠࡦࡤࡽࠧ஑"): bstack1l1l1lll_opy_,
                              bstack1ll1l_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟࡯ࡣࡰࡩࠧஒ"): bstack1ll1l_opy_ (u"ࠤࡖࡈࡐࡌࡥࡢࡶࡸࡶࡪࡖࡥࡳࡨࡲࡶࡲࡧ࡮ࡤࡧࠥஓ"),
                              bstack1ll1l_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡ࡭ࡷࡴࡴࠢஔ"): {
                                  bstack1ll1l_opy_ (u"ࠦࡲ࡫ࡡࡴࡷࡵࡩࡸࠨக"): data,
                                  bstack1ll1l_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢ஖"): bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣ஗"))
                              },
                              bstack1ll1l_opy_ (u"ࠢࡶࡵࡨࡶࡤࡪࡡࡵࡣࠥ஘"): bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠣࡷࡶࡩࡷࡔࡡ࡮ࡧࠥங")),
                              bstack1ll1l_opy_ (u"ࠤ࡫ࡳࡸࡺ࡟ࡪࡰࡩࡳࠧச"): get_host_info()
                          }
                      }
                      bstack1l1ll111l_opy_ = bstack1ll11l1l1_opy_(cli.config, [bstack1ll1l_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ஛"), bstack1ll1l_opy_ (u"ࠦࡪࡪࡳࡊࡰࡶࡸࡷࡻ࡭ࡦࡰࡷࡥࡹ࡯࡯࡯ࠤஜ"), bstack1ll1l_opy_ (u"ࠧࡧࡰࡪࠤ஝")], bstack11l111111l_opy_)
                      response = bstack1l11lllll_opy_(bstack1ll1l_opy_ (u"ࠨࡐࡐࡕࡗࠦஞ"), bstack1l1ll111l_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack1ll1l_opy_ (u"ࠢࡅࡣࡷࡥࠥࡹࡥ࡯ࡶࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺࠢࡷࡳࠥࢁࡽࠡࡹ࡬ࡸ࡭ࠦࡤࡢࡶࡤࠤࢀࢃࠢட").format(bstack11l111111l_opy_, payload))
                      else:
                          logger.debug(bstack1ll1l_opy_ (u"ࠣࡔࡨࡵࡺ࡫ࡳࡵࠢࡩࡥ࡮ࡲࡥࡥࠢࡩࡳࡷࠦࡻࡾࠢࡺ࡭ࡹ࡮ࠠࡥࡣࡷࡥࠥࢁࡽࠣ஠").format(bstack11l111111l_opy_, payload))
          except Exception as e:
              logger.debug(bstack1ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥ࡯ࡦࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳࠡࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣࡿࢂࠨ஡").format(e))
      bstack1ll11l11_opy_()
      bstack1ll11lll1_opy_(bstack111l1ll1ll_opy_, logger)
  except:
    pass
def bstack1l1l1ll11_opy_():
  global bstack11l1l11111_opy_
  global bstack1lll1l111l_opy_
  global bstack1l11l1ll1l_opy_
  global bstack1l1l1l11ll_opy_
  global bstack11llll1ll_opy_
  global bstack1lll11lll1_opy_
  global CONFIG
  bstack1111l1l11l_opy_ = os.environ.get(bstack1ll1l_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫ஢"))
  if bstack1111l1l11l_opy_ in [bstack1ll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪண"), bstack1ll1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫத")]:
    bstack1l1111lll_opy_()
  percy.shutdown()
  if bstack11l1l11111_opy_:
    logger.warning(bstack1ll111ll11_opy_.format(str(bstack11l1l11111_opy_)))
  else:
    try:
      bstack11111llll_opy_ = bstack11l1l11l11_opy_(bstack1ll1l_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬ஥"), logger)
      if bstack11111llll_opy_.get(bstack1ll1l_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬ஦")) and bstack11111llll_opy_.get(bstack1ll1l_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭஧")).get(bstack1ll1l_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫந")):
        logger.warning(bstack1ll111ll11_opy_.format(str(bstack11111llll_opy_[bstack1ll1l_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨன")][bstack1ll1l_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭ப")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1l1lll11l1_opy_.invoke(Events.bstack1ll1ll1l11_opy_)
  logger.info(bstack1111ll1l11_opy_)
  global bstack1l11l1ll1_opy_
  if bstack1l11l1ll1_opy_:
    bstack1l11l11111_opy_()
  try:
    with bstack1ll1l111l_opy_:
      bstack1l1lll111_opy_ = bstack1lll1l111l_opy_.copy()
    for driver in bstack1l1lll111_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1lll111l1l_opy_)
  if bstack1lll11lll1_opy_ == bstack1ll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ஫"):
    bstack11llll1ll_opy_ = bstack1ll1llll1l_opy_(bstack1ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧ஬"))
  if bstack1lll11lll1_opy_ == bstack1ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ஭") and len(bstack1l1l1l11ll_opy_) == 0:
    bstack1l1l1l11ll_opy_ = bstack1ll1llll1l_opy_(bstack1ll1l_opy_ (u"ࠨࡲࡺࡣࡵࡿࡴࡦࡵࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ம"))
    if len(bstack1l1l1l11ll_opy_) == 0:
      bstack1l1l1l11ll_opy_ = bstack1ll1llll1l_opy_(bstack1ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡳࡴࡵࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨய"))
  bstack1l111111l_opy_ = bstack1ll1l_opy_ (u"ࠪࠫர")
  if len(bstack1l11l1ll1l_opy_) > 0:
    bstack1l111111l_opy_ = bstack1ll11ll1ll_opy_(bstack1l11l1ll1l_opy_)
  elif len(bstack1l1l1l11ll_opy_) > 0:
    bstack1l111111l_opy_ = bstack1ll11ll1ll_opy_(bstack1l1l1l11ll_opy_)
  elif len(bstack11llll1ll_opy_) > 0:
    bstack1l111111l_opy_ = bstack1ll11ll1ll_opy_(bstack11llll1ll_opy_)
  elif len(bstack11llll111_opy_) > 0:
    bstack1l111111l_opy_ = bstack1ll11ll1ll_opy_(bstack11llll111_opy_)
  if bool(bstack1l111111l_opy_):
    bstack1l111l1l11_opy_(bstack1l111111l_opy_)
  else:
    bstack1l111l1l11_opy_()
  bstack1ll11lll1_opy_(bstack1l1ll11ll1_opy_, logger)
  if bstack1111l1l11l_opy_ not in [bstack1ll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬற")]:
    bstack1l1111111l_opy_()
  bstack1ll1ll111_opy_.bstack1l1lll1l_opy_(CONFIG)
  if len(bstack11llll1ll_opy_) > 0:
    sys.exit(len(bstack11llll1ll_opy_))
def bstack1llllll1ll_opy_(bstack1l1ll1111_opy_, frame):
  global bstack111111ll_opy_
  logger.error(bstack1ll11ll1l_opy_)
  bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱࡔ࡯ࠨல"), bstack1l1ll1111_opy_)
  if hasattr(signal, bstack1ll1l_opy_ (u"࠭ࡓࡪࡩࡱࡥࡱࡹࠧள")):
    bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧழ"), signal.Signals(bstack1l1ll1111_opy_).name)
  else:
    bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨவ"), bstack1ll1l_opy_ (u"ࠩࡖࡍࡌ࡛ࡎࡌࡐࡒ࡛ࡓ࠭ஶ"))
  if cli.is_running():
    bstack1l1lll11l1_opy_.invoke(Events.bstack1ll1ll1l11_opy_)
  bstack1111l1l11l_opy_ = os.environ.get(bstack1ll1l_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫஷ"))
  if bstack1111l1l11l_opy_ == bstack1ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫஸ") and not cli.is_enabled(CONFIG):
    bstack1lllll11_opy_.stop(bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬஹ")))
  bstack1l1l1ll11_opy_()
  sys.exit(1)
def bstack1lllll1l11_opy_(err):
  logger.critical(bstack11ll1l1111_opy_.format(str(err)))
  bstack1l111l1l11_opy_(bstack11ll1l1111_opy_.format(str(err)), True)
  atexit.unregister(bstack1l1l1ll11_opy_)
  bstack1l1111lll_opy_()
  sys.exit(1)
def bstack1l111l1l1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l111l1l11_opy_(message, True)
  atexit.unregister(bstack1l1l1ll11_opy_)
  bstack1l1111lll_opy_()
  sys.exit(1)
def bstack11ll1ll1l1_opy_():
  global CONFIG
  global bstack1l1l1l1l1_opy_
  global bstack1ll11lllll_opy_
  global bstack1llll1l1l1_opy_
  CONFIG = bstack1111ll1ll_opy_()
  load_dotenv(CONFIG.get(bstack1ll1l_opy_ (u"࠭ࡥ࡯ࡸࡉ࡭ࡱ࡫ࠧ஺")))
  bstack11l111llll_opy_()
  bstack1ll1111ll1_opy_()
  CONFIG = bstack11l1l11l1_opy_(CONFIG)
  update(CONFIG, bstack1ll11lllll_opy_)
  update(CONFIG, bstack1l1l1l1l1_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack111l11ll1l_opy_(CONFIG)
  bstack1llll1l1l1_opy_ = bstack11l11ll11_opy_(CONFIG)
  os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪ஻")] = bstack1llll1l1l1_opy_.__str__().lower()
  bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ஼"), bstack1llll1l1l1_opy_)
  if (bstack1ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ஽") in CONFIG and bstack1ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ா") in bstack1l1l1l1l1_opy_) or (
          bstack1ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧி") in CONFIG and bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨீ") not in bstack1ll11lllll_opy_):
    if os.getenv(bstack1ll1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪு")):
      CONFIG[bstack1ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩூ")] = os.getenv(bstack1ll1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ௃"))
    else:
      if not CONFIG.get(bstack1ll1l_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠧ௄"), bstack1ll1l_opy_ (u"ࠥࠦ௅")) in bstack111lll1lll_opy_:
        bstack11111lll11_opy_()
  elif (bstack1ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧெ") not in CONFIG and bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧே") in CONFIG) or (
          bstack1ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩை") in bstack1ll11lllll_opy_ and bstack1ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ௉") not in bstack1l1l1l1l1_opy_):
    del (CONFIG[bstack1ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪொ")])
  if bstack1111lllll1_opy_(CONFIG):
    bstack1lllll1l11_opy_(bstack111ll1l111_opy_)
  Config.bstack111l1ll1_opy_().set_property(bstack1ll1l_opy_ (u"ࠤࡸࡷࡪࡸࡎࡢ࡯ࡨࠦோ"), CONFIG[bstack1ll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬௌ")])
  bstack11111111l_opy_()
  bstack1ll1llll11_opy_()
  if bstack11lll11l1l_opy_ and not CONFIG.get(bstack1ll1l_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ்ࠢ"), bstack1ll1l_opy_ (u"ࠧࠨ௎")) in bstack111lll1lll_opy_:
    CONFIG[bstack1ll1l_opy_ (u"࠭ࡡࡱࡲࠪ௏")] = bstack1l11llll1l_opy_(CONFIG)
    logger.info(bstack1ll1ll1111_opy_.format(CONFIG[bstack1ll1l_opy_ (u"ࠧࡢࡲࡳࠫௐ")]))
  if not bstack1llll1l1l1_opy_:
    CONFIG[bstack1ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௑")] = [{}]
def bstack11l1l1l11l_opy_(config, bstack11lll1l111_opy_):
  global CONFIG
  global bstack11lll11l1l_opy_
  CONFIG = config
  bstack11lll11l1l_opy_ = bstack11lll1l111_opy_
def bstack1ll1llll11_opy_():
  global CONFIG
  global bstack11lll11l1l_opy_
  if bstack1ll1l_opy_ (u"ࠩࡤࡴࡵ࠭௒") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l111l1l1l_opy_(e, bstack1l11111ll1_opy_)
    bstack11lll11l1l_opy_ = True
    bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ௓"), True)
def bstack1l11llll1l_opy_(config):
  bstack111l1l111l_opy_ = bstack1ll1l_opy_ (u"ࠫࠬ௔")
  app = config[bstack1ll1l_opy_ (u"ࠬࡧࡰࡱࠩ௕")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1llll1llll_opy_:
      if os.path.exists(app):
        bstack111l1l111l_opy_ = bstack111l11l11l_opy_(config, app)
      elif bstack11111ll111_opy_(app):
        bstack111l1l111l_opy_ = app
      else:
        bstack1lllll1l11_opy_(bstack1l1ll11l1l_opy_.format(app))
    else:
      if bstack11111ll111_opy_(app):
        bstack111l1l111l_opy_ = app
      elif os.path.exists(app):
        bstack111l1l111l_opy_ = bstack111l11l11l_opy_(app)
      else:
        bstack1lllll1l11_opy_(bstack1ll1ll1l1l_opy_)
  else:
    if len(app) > 2:
      bstack1lllll1l11_opy_(bstack1lll111l1_opy_)
    elif len(app) == 2:
      if bstack1ll1l_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ௖") in app and bstack1ll1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪௗ") in app:
        if os.path.exists(app[bstack1ll1l_opy_ (u"ࠨࡲࡤࡸ࡭࠭௘")]):
          bstack111l1l111l_opy_ = bstack111l11l11l_opy_(config, app[bstack1ll1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ௙")], app[bstack1ll1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭௚")])
        else:
          bstack1lllll1l11_opy_(bstack1l1ll11l1l_opy_.format(app))
      else:
        bstack1lllll1l11_opy_(bstack1lll111l1_opy_)
    else:
      for key in app:
        if key in bstack1111l1ll1_opy_:
          if key == bstack1ll1l_opy_ (u"ࠫࡵࡧࡴࡩࠩ௛"):
            if os.path.exists(app[key]):
              bstack111l1l111l_opy_ = bstack111l11l11l_opy_(config, app[key])
            else:
              bstack1lllll1l11_opy_(bstack1l1ll11l1l_opy_.format(app))
          else:
            bstack111l1l111l_opy_ = app[key]
        else:
          bstack1lllll1l11_opy_(bstack111l111l11_opy_)
  return bstack111l1l111l_opy_
def bstack11111ll111_opy_(bstack111l1l111l_opy_):
  import re
  bstack111l1ll11l_opy_ = re.compile(bstack1ll1l_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧ௜"))
  bstack11l111l1l_opy_ = re.compile(bstack1ll1l_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮࠴ࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥ௝"))
  if bstack1ll1l_opy_ (u"ࠧࡣࡵ࠽࠳࠴࠭௞") in bstack111l1l111l_opy_ or re.fullmatch(bstack111l1ll11l_opy_, bstack111l1l111l_opy_) or re.fullmatch(bstack11l111l1l_opy_, bstack111l1l111l_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack1l111l1111_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack111l11l11l_opy_(config, path, bstack111ll1l1l_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1ll1l_opy_ (u"ࠨࡴࡥࠫ௟")).read()).hexdigest()
  bstack11ll1l11l1_opy_ = bstack1lllll11l1_opy_(md5_hash)
  bstack111l1l111l_opy_ = None
  if bstack11ll1l11l1_opy_:
    logger.info(bstack1111lll11l_opy_.format(bstack11ll1l11l1_opy_, md5_hash))
    return bstack11ll1l11l1_opy_
  bstack1l11l11lll_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack1ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧ௠"): (os.path.basename(path), open(os.path.abspath(path), bstack1ll1l_opy_ (u"ࠪࡶࡧ࠭௡")), bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡸࡵ࠱ࡳࡰࡦ࡯࡮ࠨ௢")),
      bstack1ll1l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ௣"): bstack111ll1l1l_opy_
    }
  )
  response = requests.post(bstack1l11111111_opy_, data=multipart_data,
                           headers={bstack1ll1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ௤"): multipart_data.content_type},
                           auth=(config[bstack1ll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ௥")], config[bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ௦")]))
  try:
    res = json.loads(response.text)
    bstack111l1l111l_opy_ = res[bstack1ll1l_opy_ (u"ࠩࡤࡴࡵࡥࡵࡳ࡮ࠪ௧")]
    logger.info(bstack1ll1lllll1_opy_.format(bstack111l1l111l_opy_))
    bstack11l1ll1l1_opy_(md5_hash, bstack111l1l111l_opy_)
    cli.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡷࡳࡰࡴࡧࡤࡠࡣࡳࡴࠧ௨"), datetime.datetime.now() - bstack1l11l11lll_opy_)
  except ValueError as err:
    bstack1lllll1l11_opy_(bstack1lll1111l_opy_.format(str(err)))
  return bstack111l1l111l_opy_
def bstack11111111l_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1ll11lll11_opy_
  bstack1lll1l111_opy_ = 1
  bstack1l11l11ll_opy_ = 1
  if bstack1ll1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ௩") in CONFIG:
    bstack1l11l11ll_opy_ = CONFIG[bstack1ll1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ௪")]
  else:
    bstack1l11l11ll_opy_ = bstack11111ll1l1_opy_(framework_name, args) or 1
  if bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ௫") in CONFIG:
    bstack1lll1l111_opy_ = len(CONFIG[bstack1ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ௬")])
  bstack1ll11lll11_opy_ = int(bstack1l11l11ll_opy_) * int(bstack1lll1l111_opy_)
def bstack11111ll1l1_opy_(framework_name, args):
  if framework_name == bstack1l1111ll1l_opy_ and args and bstack1ll1l_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭௭") in args:
      bstack1l1lll1lll_opy_ = args.index(bstack1ll1l_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ௮"))
      return int(args[bstack1l1lll1lll_opy_ + 1]) or 1
  return 1
def bstack1lllll11l1_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭௯"))
    bstack1l1l1111l1_opy_ = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠫࢃ࠭௰")), bstack1ll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ௱"), bstack1ll1l_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧ௲"))
    if os.path.exists(bstack1l1l1111l1_opy_):
      try:
        bstack1ll1ll1l1_opy_ = json.load(open(bstack1l1l1111l1_opy_, bstack1ll1l_opy_ (u"ࠧࡳࡤࠪ௳")))
        if md5_hash in bstack1ll1ll1l1_opy_:
          bstack11l1ll1l1l_opy_ = bstack1ll1ll1l1_opy_[md5_hash]
          bstack1111l111ll_opy_ = datetime.datetime.now()
          bstack1lll11llll_opy_ = datetime.datetime.strptime(bstack11l1ll1l1l_opy_[bstack1ll1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ௴")], bstack1ll1l_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭௵"))
          if (bstack1111l111ll_opy_ - bstack1lll11llll_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack11l1ll1l1l_opy_[bstack1ll1l_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ௶")]):
            return None
          return bstack11l1ll1l1l_opy_[bstack1ll1l_opy_ (u"ࠫ࡮ࡪࠧ௷")]
      except Exception as e:
        logger.debug(bstack1ll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮ࠠࡧ࡫࡯ࡩ࠿ࠦࡻࡾࠩ௸").format(str(e)))
    return None
  bstack1l1l1111l1_opy_ = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"࠭ࡾࠨ௹")), bstack1ll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ௺"), bstack1ll1l_opy_ (u"ࠨࡣࡳࡴ࡚ࡶ࡬ࡰࡣࡧࡑࡉ࠻ࡈࡢࡵ࡫࠲࡯ࡹ࡯࡯ࠩ௻"))
  lock_file = bstack1l1l1111l1_opy_ + bstack1ll1l_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨ௼")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1l1l1111l1_opy_):
        with open(bstack1l1l1111l1_opy_, bstack1ll1l_opy_ (u"ࠪࡶࠬ௽")) as f:
          content = f.read().strip()
          if content:
            bstack1ll1ll1l1_opy_ = json.loads(content)
            if md5_hash in bstack1ll1ll1l1_opy_:
              bstack11l1ll1l1l_opy_ = bstack1ll1ll1l1_opy_[md5_hash]
              bstack1111l111ll_opy_ = datetime.datetime.now()
              bstack1lll11llll_opy_ = datetime.datetime.strptime(bstack11l1ll1l1l_opy_[bstack1ll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ௾")], bstack1ll1l_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩ௿"))
              if (bstack1111l111ll_opy_ - bstack1lll11llll_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack11l1ll1l1l_opy_[bstack1ll1l_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫఀ")]):
                return None
              return bstack11l1ll1l1l_opy_[bstack1ll1l_opy_ (u"ࠧࡪࡦࠪఁ")]
      return None
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡸ࡫ࡷ࡬ࠥ࡬ࡩ࡭ࡧࠣࡰࡴࡩ࡫ࡪࡰࡪࠤ࡫ࡵࡲࠡࡏࡇ࠹ࠥ࡮ࡡࡴࡪ࠽ࠤࢀࢃࠧం").format(str(e)))
    return None
def bstack11l1ll1l1_opy_(md5_hash, bstack111l1l111l_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬః"))
    bstack1l1l1lllll_opy_ = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠪࢂࠬఄ")), bstack1ll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఅ"))
    if not os.path.exists(bstack1l1l1lllll_opy_):
      os.makedirs(bstack1l1l1lllll_opy_)
    bstack1l1l1111l1_opy_ = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠬࢄࠧఆ")), bstack1ll1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ఇ"), bstack1ll1l_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨఈ"))
    bstack1111ll111_opy_ = {
      bstack1ll1l_opy_ (u"ࠨ࡫ࡧࠫఉ"): bstack111l1l111l_opy_,
      bstack1ll1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬఊ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1ll1l_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧఋ")),
      bstack1ll1l_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩఌ"): str(__version__)
    }
    try:
      bstack1ll1ll1l1_opy_ = {}
      if os.path.exists(bstack1l1l1111l1_opy_):
        bstack1ll1ll1l1_opy_ = json.load(open(bstack1l1l1111l1_opy_, bstack1ll1l_opy_ (u"ࠬࡸࡢࠨ఍")))
      bstack1ll1ll1l1_opy_[md5_hash] = bstack1111ll111_opy_
      with open(bstack1l1l1111l1_opy_, bstack1ll1l_opy_ (u"ࠨࡷࠬࠤఎ")) as outfile:
        json.dump(bstack1ll1ll1l1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡵࡱࡦࡤࡸ࡮ࡴࡧࠡࡏࡇ࠹ࠥ࡮ࡡࡴࡪࠣࡪ࡮ࡲࡥ࠻ࠢࡾࢁࠬఏ").format(str(e)))
    return
  bstack1l1l1lllll_opy_ = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠨࢀࠪఐ")), bstack1ll1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ఑"))
  if not os.path.exists(bstack1l1l1lllll_opy_):
    os.makedirs(bstack1l1l1lllll_opy_)
  bstack1l1l1111l1_opy_ = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠪࢂࠬఒ")), bstack1ll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఓ"), bstack1ll1l_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ఔ"))
  lock_file = bstack1l1l1111l1_opy_ + bstack1ll1l_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬక")
  bstack1111ll111_opy_ = {
    bstack1ll1l_opy_ (u"ࠧࡪࡦࠪఖ"): bstack111l1l111l_opy_,
    bstack1ll1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫగ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1ll1l_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ఘ")),
    bstack1ll1l_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨఙ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1ll1ll1l1_opy_ = {}
      if os.path.exists(bstack1l1l1111l1_opy_):
        with open(bstack1l1l1111l1_opy_, bstack1ll1l_opy_ (u"ࠫࡷ࠭చ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll1ll1l1_opy_ = json.loads(content)
      bstack1ll1ll1l1_opy_[md5_hash] = bstack1111ll111_opy_
      with open(bstack1l1l1111l1_opy_, bstack1ll1l_opy_ (u"ࠧࡽࠢఛ")) as outfile:
        json.dump(bstack1ll1ll1l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡽࡩࡵࡪࠣࡪ࡮ࡲࡥࠡ࡮ࡲࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨࠡࡷࡳࡨࡦࡺࡥ࠻ࠢࡾࢁࠬజ").format(str(e)))
def bstack11111lll1l_opy_(self):
  return
def bstack1lll11l1ll_opy_(self):
  return
def bstack111111ll1_opy_():
  global bstack1l1lllll1l_opy_
  bstack1l1lllll1l_opy_ = True
@measure(event_name=EVENTS.bstack11llll111l_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack11l111lll1_opy_(self):
  global bstack1l1llllll_opy_
  global bstack111111111_opy_
  global bstack1l1ll1ll11_opy_
  try:
    if bstack1ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧఝ") in bstack1l1llllll_opy_ and self.session_id != None and bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬఞ"), bstack1ll1l_opy_ (u"ࠩࠪట")) != bstack1ll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫఠ"):
      bstack1l1l1lll1l_opy_ = bstack1ll1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫడ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬఢ")
      if bstack1l1l1lll1l_opy_ == bstack1ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ణ"):
        bstack111llll1l_opy_(logger)
      if self != None:
        bstack1ll11111l_opy_(self, bstack1l1l1lll1l_opy_, bstack1ll1l_opy_ (u"ࠧ࠭ࠢࠪత").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1ll1l_opy_ (u"ࠨࠩథ")
    if bstack1ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩద") in bstack1l1llllll_opy_ and getattr(threading.current_thread(), bstack1ll1l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩధ"), None):
      bstack111l1l11_opy_.bstack1111l1ll_opy_(self, bstack1l1111l11l_opy_, logger, wait=True)
    if bstack1ll1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫన") in bstack1l1llllll_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1ll11111l_opy_(self, bstack1ll1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ఩"))
      bstack1ll1lllll_opy_.bstack11l1llllll_opy_(self)
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠢప") + str(e))
  bstack1l1ll1ll11_opy_(self)
  self.session_id = None
def bstack1lllllllll_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1l1lll1l1l_opy_
    global bstack1l1llllll_opy_
    command_executor = kwargs.get(bstack1ll1l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠪఫ"), bstack1ll1l_opy_ (u"ࠨࠩబ"))
    bstack1l111llll1_opy_ = False
    if type(command_executor) == str and bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬభ") in command_executor:
      bstack1l111llll1_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭మ") in str(getattr(command_executor, bstack1ll1l_opy_ (u"ࠫࡤࡻࡲ࡭ࠩయ"), bstack1ll1l_opy_ (u"ࠬ࠭ర"))):
      bstack1l111llll1_opy_ = True
    else:
      kwargs = bstack1lllllll1_opy_.bstack11l1llll1l_opy_(bstack1l1l1l111l_opy_=kwargs, config=CONFIG)
      return bstack111lll11ll_opy_(self, *args, **kwargs)
    if bstack1l111llll1_opy_:
      bstack11ll1ll11l_opy_ = bstack1l11lll111_opy_.bstack111l111ll_opy_(CONFIG, bstack1l1llllll_opy_)
      if kwargs.get(bstack1ll1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧఱ")):
        kwargs[bstack1ll1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨల")] = bstack1l1lll1l1l_opy_(kwargs[bstack1ll1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩళ")], bstack1l1llllll_opy_, CONFIG, bstack11ll1ll11l_opy_)
      elif kwargs.get(bstack1ll1l_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩఴ")):
        kwargs[bstack1ll1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪవ")] = bstack1l1lll1l1l_opy_(kwargs[bstack1ll1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫశ")], bstack1l1llllll_opy_, CONFIG, bstack11ll1ll11l_opy_)
  except Exception as e:
    logger.error(bstack1ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡧࡦࡶࡳ࠻ࠢࡾࢁࠧష").format(str(e)))
  return bstack111lll11ll_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack11lllll111_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack111l1lll11_opy_(self, command_executor=bstack1ll1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵࠱࠳࠹࠱࠴࠳࠶࠮࠲࠼࠷࠸࠹࠺ࠢస"), *args, **kwargs):
  global bstack111111111_opy_
  global bstack1lll1l111l_opy_
  bstack1l1l1l111_opy_ = bstack1lllllllll_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1l11llll_opy_.on():
    return bstack1l1l1l111_opy_
  try:
    logger.debug(bstack1ll1l_opy_ (u"ࠧࡄࡱࡰࡱࡦࡴࡤࠡࡇࡻࡩࡨࡻࡴࡰࡴࠣࡻ࡭࡫࡮ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡧࡣ࡯ࡷࡪࠦ࠭ࠡࡽࢀࠫహ").format(str(command_executor)))
    logger.debug(bstack1ll1l_opy_ (u"ࠨࡊࡸࡦ࡛ࠥࡒࡍࠢ࡬ࡷࠥ࠳ࠠࡼࡿࠪ఺").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ఻") in command_executor._url:
      bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱ఼ࠫ"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧఽ") in command_executor):
    bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ా"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1ll111l111_opy_ = getattr(threading.current_thread(), bstack1ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧి"), None)
  bstack1111l1l1l1_opy_ = {}
  if self.capabilities is not None:
    bstack1111l1l1l1_opy_[bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭ీ")] = self.capabilities.get(bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ు"))
    bstack1111l1l1l1_opy_[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫూ")] = self.capabilities.get(bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫృ"))
    bstack1111l1l1l1_opy_[bstack1ll1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡣࡴࡶࡴࡪࡱࡱࡷࠬౄ")] = self.capabilities.get(bstack1ll1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ౅"))
  if CONFIG.get(bstack1ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ె"), False) and bstack1lllllll1_opy_.bstack1ll1l11l1l_opy_(bstack1111l1l1l1_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack1ll1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧే") in bstack1l1llllll_opy_ or bstack1ll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧై") in bstack1l1llllll_opy_:
    bstack1lllll11_opy_.bstack111ll1lll1_opy_(self)
  if bstack1ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ౉") in bstack1l1llllll_opy_ and bstack1ll111l111_opy_ and bstack1ll111l111_opy_.get(bstack1ll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪొ"), bstack1ll1l_opy_ (u"ࠫࠬో")) == bstack1ll1l_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭ౌ"):
    bstack1lllll11_opy_.bstack111ll1lll1_opy_(self)
  bstack111111111_opy_ = self.session_id
  with bstack1ll1l111l_opy_:
    bstack1lll1l111l_opy_.append(self)
  return bstack1l1l1l111_opy_
def bstack11111ll1l_opy_(args):
  return bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ్ࠧ") in str(args)
def bstack1llll1lll1_opy_(self, driver_command, *args, **kwargs):
  global bstack1ll1llllll_opy_
  global bstack1ll1ll1ll_opy_
  bstack1l11ll111_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫ౎"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1ll1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ౏"), None)
  bstack11l11ll1ll_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ౐"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1ll1l_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ౑"), None)
  bstack11lll11l11_opy_ = getattr(self, bstack1ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ౒"), None) != None and getattr(self, bstack1ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ౓"), None) == True
  if not bstack1ll1ll1ll_opy_ and bstack1ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭౔") in CONFIG and CONFIG[bstack1ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿౕࠧ")] == True and bstack1l1ll1lll1_opy_.bstack11ll1111ll_opy_(driver_command) and (bstack11lll11l11_opy_ or bstack1l11ll111_opy_ or bstack11l11ll1ll_opy_) and not bstack11111ll1l_opy_(args):
    try:
      bstack1ll1ll1ll_opy_ = True
      logger.debug(bstack1ll1l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡼࡿౖࠪ").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1ll1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡥࡳࡨࡲࡶࡲࠦࡳࡤࡣࡱࠤࢀࢃࠧ౗").format(str(err)))
    bstack1ll1ll1ll_opy_ = False
  response = bstack1ll1llllll_opy_(self, driver_command, *args, **kwargs)
  if (bstack1ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩౘ") in str(bstack1l1llllll_opy_).lower() or bstack1ll1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫౙ") in str(bstack1l1llllll_opy_).lower()) and bstack1l11llll_opy_.on():
    try:
      if driver_command == bstack1ll1l_opy_ (u"ࠬࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩౚ"):
        bstack1lllll11_opy_.bstack1l1l1l1lll_opy_({
            bstack1ll1l_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬ౛"): response[bstack1ll1l_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭౜")],
            bstack1ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨౝ"): bstack1lllll11_opy_.current_test_uuid() if bstack1lllll11_opy_.current_test_uuid() else bstack1l11llll_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack111l1l11l_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack11l1lll11l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack111111111_opy_
  global bstack1l1lllllll_opy_
  global bstack111llll111_opy_
  global bstack11lllllll_opy_
  global bstack1ll1l11ll1_opy_
  global bstack1l1llllll_opy_
  global bstack111lll11ll_opy_
  global bstack1lll1l111l_opy_
  global bstack1ll1ll1ll1_opy_
  global bstack1l1111l11l_opy_
  if os.getenv(bstack1ll1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ౞")) is not None and bstack1lllllll1_opy_.bstack11l11lll1_opy_(CONFIG) is None:
    CONFIG[bstack1ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ౟")] = True
  CONFIG[bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ౠ")] = str(bstack1l1llllll_opy_) + str(__version__)
  bstack1ll11l11ll_opy_ = os.environ[bstack1ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪౡ")]
  bstack11ll1ll11l_opy_ = bstack1l11lll111_opy_.bstack111l111ll_opy_(CONFIG, bstack1l1llllll_opy_)
  CONFIG[bstack1ll1l_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩౢ")] = bstack1ll11l11ll_opy_
  CONFIG[bstack1ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩౣ")] = bstack11ll1ll11l_opy_
  if CONFIG.get(bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ౤"),bstack1ll1l_opy_ (u"ࠩࠪ౥")) and bstack1ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ౦") in bstack1l1llllll_opy_:
    CONFIG[bstack1ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ౧")].pop(bstack1ll1l_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ౨"), None)
    CONFIG[bstack1ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭౩")].pop(bstack1ll1l_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ౪"), None)
  command_executor = bstack1l1l1llll_opy_()
  logger.debug(bstack1ll111l1l1_opy_.format(command_executor))
  proxy = bstack11llll1l1l_opy_(CONFIG, proxy)
  bstack111l1lll1_opy_ = 0 if bstack1l1lllllll_opy_ < 0 else bstack1l1lllllll_opy_
  try:
    if bstack11lllllll_opy_ is True:
      bstack111l1lll1_opy_ = int(multiprocessing.current_process().name)
    elif bstack1ll1l11ll1_opy_ is True:
      bstack111l1lll1_opy_ = int(threading.current_thread().name)
  except:
    bstack111l1lll1_opy_ = 0
  bstack11l11l1l11_opy_ = bstack11llll1l11_opy_(CONFIG, bstack111l1lll1_opy_)
  logger.debug(bstack1l1ll11111_opy_.format(str(bstack11l11l1l11_opy_)))
  if bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ౫") in CONFIG and bstack1lll1ll111_opy_(CONFIG[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭౬")]):
    bstack11l1l1llll_opy_(bstack11l11l1l11_opy_)
  if bstack1lllllll1_opy_.bstack1l1l1ll1l_opy_(CONFIG, bstack111l1lll1_opy_) and bstack1lllllll1_opy_.bstack11l1llll1_opy_(bstack11l11l1l11_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack1lllllll1_opy_.set_capabilities(bstack11l11l1l11_opy_, CONFIG)
  if desired_capabilities:
    bstack1ll1111l1_opy_ = bstack11l1l11l1_opy_(desired_capabilities)
    bstack1ll1111l1_opy_[bstack1ll1l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪ౭")] = bstack1l1ll1ll1l_opy_(CONFIG)
    bstack11lll11lll_opy_ = bstack11llll1l11_opy_(bstack1ll1111l1_opy_)
    if bstack11lll11lll_opy_:
      bstack11l11l1l11_opy_ = update(bstack11lll11lll_opy_, bstack11l11l1l11_opy_)
    desired_capabilities = None
  if options:
    bstack11llllllll_opy_(options, bstack11l11l1l11_opy_)
  if not options:
    options = bstack1lll111ll1_opy_(bstack11l11l1l11_opy_)
  bstack1l1111l11l_opy_ = CONFIG.get(bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ౮"))[bstack111l1lll1_opy_]
  if proxy and bstack111lllll1_opy_() >= version.parse(bstack1ll1l_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬ౯")):
    options.proxy(proxy)
  if options and bstack111lllll1_opy_() >= version.parse(bstack1ll1l_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ౰")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack111lllll1_opy_() < version.parse(bstack1ll1l_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭౱")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack11l11l1l11_opy_)
  logger.info(bstack1l1l111l11_opy_)
  bstack111l11llll_opy_.end(EVENTS.bstack11l11ll1l_opy_.value, EVENTS.bstack11l11ll1l_opy_.value + bstack1ll1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ౲"), EVENTS.bstack11l11ll1l_opy_.value + bstack1ll1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ౳"), status=True, failure=None, test_name=bstack111llll111_opy_)
  if bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡵࡸ࡯ࡧ࡫࡯ࡩࠬ౴") in kwargs:
    del kwargs[bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡶࡲࡰࡨ࡬ࡰࡪ࠭౵")]
  try:
    if bstack111lllll1_opy_() >= version.parse(bstack1ll1l_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬ౶")):
      bstack111lll11ll_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack111lllll1_opy_() >= version.parse(bstack1ll1l_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬ౷")):
      bstack111lll11ll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack111lllll1_opy_() >= version.parse(bstack1ll1l_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧ౸")):
      bstack111lll11ll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack111lll11ll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack11ll1l11l_opy_:
    logger.error(bstack1l1l1111l_opy_.format(bstack1ll1l_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠧ౹"), str(bstack11ll1l11l_opy_)))
    raise bstack11ll1l11l_opy_
  if bstack1lllllll1_opy_.bstack1l1l1ll1l_opy_(CONFIG, bstack111l1lll1_opy_) and bstack1lllllll1_opy_.bstack11l1llll1_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack1ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫ౺")][bstack1ll1l_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ౻")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack1lllllll1_opy_.set_capabilities(bstack11l11l1l11_opy_, CONFIG)
  try:
    bstack1l11ll1l1_opy_ = bstack1ll1l_opy_ (u"ࠫࠬ౼")
    if bstack111lllll1_opy_() >= version.parse(bstack1ll1l_opy_ (u"ࠬ࠺࠮࠱࠰࠳ࡦ࠶࠭౽")):
      if self.caps is not None:
        bstack1l11ll1l1_opy_ = self.caps.get(bstack1ll1l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨ౾"))
    else:
      if self.capabilities is not None:
        bstack1l11ll1l1_opy_ = self.capabilities.get(bstack1ll1l_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢ౿"))
    if bstack1l11ll1l1_opy_:
      bstack11111lllll_opy_(bstack1l11ll1l1_opy_)
      if bstack111lllll1_opy_() <= version.parse(bstack1ll1l_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨಀ")):
        self.command_executor._url = bstack1ll1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥಁ") + bstack111ll11l1l_opy_ + bstack1ll1l_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢಂ")
      else:
        self.command_executor._url = bstack1ll1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨಃ") + bstack1l11ll1l1_opy_ + bstack1ll1l_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨ಄")
      logger.debug(bstack1111l1lll1_opy_.format(bstack1l11ll1l1_opy_))
    else:
      logger.debug(bstack111l11l111_opy_.format(bstack1ll1l_opy_ (u"ࠨࡏࡱࡶ࡬ࡱࡦࡲࠠࡉࡷࡥࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢಅ")))
  except Exception as e:
    logger.debug(bstack111l11l111_opy_.format(e))
  if bstack1ll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ಆ") in bstack1l1llllll_opy_:
    bstack1111ll111l_opy_(bstack1l1lllllll_opy_, bstack1ll1ll1ll1_opy_)
  bstack111111111_opy_ = self.session_id
  if bstack1ll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨಇ") in bstack1l1llllll_opy_ or bstack1ll1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩಈ") in bstack1l1llllll_opy_ or bstack1ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩಉ") in bstack1l1llllll_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1ll111l111_opy_ = getattr(threading.current_thread(), bstack1ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥࠬಊ"), None)
  if bstack1ll1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬಋ") in bstack1l1llllll_opy_ or bstack1ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಌ") in bstack1l1llllll_opy_:
    bstack1lllll11_opy_.bstack111ll1lll1_opy_(self)
  if bstack1ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ಍") in bstack1l1llllll_opy_ and bstack1ll111l111_opy_ and bstack1ll111l111_opy_.get(bstack1ll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨಎ"), bstack1ll1l_opy_ (u"ࠩࠪಏ")) == bstack1ll1l_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫಐ"):
    bstack1lllll11_opy_.bstack111ll1lll1_opy_(self)
  with bstack1ll1l111l_opy_:
    bstack1lll1l111l_opy_.append(self)
  if bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಑") in CONFIG and bstack1ll1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪಒ") in CONFIG[bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಓ")][bstack111l1lll1_opy_]:
    bstack111llll111_opy_ = CONFIG[bstack1ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಔ")][bstack111l1lll1_opy_][bstack1ll1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ಕ")]
  logger.debug(bstack1ll1l1lll1_opy_.format(bstack111111111_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack11lll1111l_opy_
    def bstack1l11ll1l1l_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack11l1ll1lll_opy_
      if(bstack1ll1l_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸ࠯࡬ࡶࠦಖ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠪࢂࠬಗ")), bstack1ll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫಘ"), bstack1ll1l_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧಙ")), bstack1ll1l_opy_ (u"࠭ࡷࠨಚ")) as fp:
          fp.write(bstack1ll1l_opy_ (u"ࠢࠣಛ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1ll1l_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥಜ")))):
          with open(args[1], bstack1ll1l_opy_ (u"ࠩࡵࠫಝ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1ll1l_opy_ (u"ࠪࡥࡸࡿ࡮ࡤࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡤࡴࡥࡸࡒࡤ࡫ࡪ࠮ࡣࡰࡰࡷࡩࡽࡺࠬࠡࡲࡤ࡫ࡪࠦ࠽ࠡࡸࡲ࡭ࡩࠦ࠰ࠪࠩಞ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1l1llll11l_opy_)
            if bstack1ll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨಟ") in CONFIG and str(CONFIG[bstack1ll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩಠ")]).lower() != bstack1ll1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬಡ"):
                bstack1ll11ll111_opy_ = bstack11lll1111l_opy_()
                bstack1ll1lll111_opy_ = bstack1ll1l_opy_ (u"ࠧࠨࠩࠍ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࠐࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹࡝࠼ࠌࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠ࠿ࠏࡩ࡯࡯ࡵࡷࠤࡵࡥࡩ࡯ࡦࡨࡼࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠳࡟࠾ࠎࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡸࡲࡩࡤࡧࠫ࠴࠱ࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴ࠫ࠾ࠎࡨࡵ࡮ࡴࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫ࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤࠬ࠿ࠏ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡲࡡࡶࡰࡦ࡬ࠥࡃࠠࡢࡵࡼࡲࡨࠦࠨ࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠩࠡ࠿ࡁࠤࢀࢁࠊࠡࠢ࡯ࡩࡹࠦࡣࡢࡲࡶ࠿ࠏࠦࠠࡵࡴࡼࠤࢀࢁࠊࠡࠢࠣࠤࡨࡧࡰࡴࠢࡀࠤࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸ࠯࠻ࠋࠢࠣࢁࢂࠦࡣࡢࡶࡦ࡬ࠥ࠮ࡥࡹࠫࠣࡿࢀࠐࠠࠡࠢࠣࡧࡴࡴࡳࡰ࡮ࡨ࠲ࡪࡸࡲࡰࡴࠫࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠿ࠨࠬࠡࡧࡻ࠭ࡀࠐࠠࠡࡿࢀࠎࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻࡼࠌࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࠬࢁࡣࡥࡲࡘࡶࡱࢃࠧࠡ࠭ࠣࡩࡳࡩ࡯ࡥࡧࡘࡖࡎࡉ࡯࡮ࡲࡲࡲࡪࡴࡴࠩࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡦࡥࡵࡹࠩࠪ࠮ࠍࠤࠥࠦࠠ࠯࠰࠱ࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵࠍࠤࠥࢃࡽࠪ࠽ࠍࢁࢂࡁࠊ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠍࠫࠬ࠭ಢ").format(bstack1ll11ll111_opy_=bstack1ll11ll111_opy_)
            lines.insert(1, bstack1ll1lll111_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1ll1l_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥಣ")), bstack1ll1l_opy_ (u"ࠩࡺࠫತ")) as bstack11lll1l11_opy_:
              bstack11lll1l11_opy_.writelines(lines)
        CONFIG[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬಥ")] = str(bstack1l1llllll_opy_) + str(__version__)
        bstack1ll11l11ll_opy_ = os.environ[bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩದ")]
        bstack11ll1ll11l_opy_ = bstack1l11lll111_opy_.bstack111l111ll_opy_(CONFIG, bstack1l1llllll_opy_)
        CONFIG[bstack1ll1l_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨಧ")] = bstack1ll11l11ll_opy_
        CONFIG[bstack1ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨನ")] = bstack11ll1ll11l_opy_
        bstack111l1lll1_opy_ = 0 if bstack1l1lllllll_opy_ < 0 else bstack1l1lllllll_opy_
        try:
          if bstack11lllllll_opy_ is True:
            bstack111l1lll1_opy_ = int(multiprocessing.current_process().name)
          elif bstack1ll1l11ll1_opy_ is True:
            bstack111l1lll1_opy_ = int(threading.current_thread().name)
        except:
          bstack111l1lll1_opy_ = 0
        CONFIG[bstack1ll1l_opy_ (u"ࠢࡶࡵࡨ࡛࠸ࡉࠢ಩")] = False
        CONFIG[bstack1ll1l_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢಪ")] = True
        bstack11l11l1l11_opy_ = bstack11llll1l11_opy_(CONFIG, bstack111l1lll1_opy_)
        logger.debug(bstack1l1ll11111_opy_.format(str(bstack11l11l1l11_opy_)))
        if CONFIG.get(bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ಫ")):
          bstack11l1l1llll_opy_(bstack11l11l1l11_opy_)
        if bstack1ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಬ") in CONFIG and bstack1ll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩಭ") in CONFIG[bstack1ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಮ")][bstack111l1lll1_opy_]:
          bstack111llll111_opy_ = CONFIG[bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಯ")][bstack111l1lll1_opy_][bstack1ll1l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬರ")]
        args.append(os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠨࢀࠪಱ")), bstack1ll1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩಲ"), bstack1ll1l_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬಳ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack11l11l1l11_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1ll1l_opy_ (u"ࠦ࡮ࡴࡤࡦࡺࡢࡦࡸࡺࡡࡤ࡭࠱࡮ࡸࠨ಴"))
      bstack11l1ll1lll_opy_ = True
      return bstack1l1l11l1l_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack1l111ll1ll_opy_(self,
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
    global bstack1l1lllllll_opy_
    global bstack111llll111_opy_
    global bstack11lllllll_opy_
    global bstack1ll1l11ll1_opy_
    global bstack1l1llllll_opy_
    CONFIG[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧವ")] = str(bstack1l1llllll_opy_) + str(__version__)
    bstack1ll11l11ll_opy_ = os.environ[bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫಶ")]
    bstack11ll1ll11l_opy_ = bstack1l11lll111_opy_.bstack111l111ll_opy_(CONFIG, bstack1l1llllll_opy_)
    CONFIG[bstack1ll1l_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪಷ")] = bstack1ll11l11ll_opy_
    CONFIG[bstack1ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪಸ")] = bstack11ll1ll11l_opy_
    bstack111l1lll1_opy_ = 0 if bstack1l1lllllll_opy_ < 0 else bstack1l1lllllll_opy_
    try:
      if bstack11lllllll_opy_ is True:
        bstack111l1lll1_opy_ = int(multiprocessing.current_process().name)
      elif bstack1ll1l11ll1_opy_ is True:
        bstack111l1lll1_opy_ = int(threading.current_thread().name)
    except:
      bstack111l1lll1_opy_ = 0
    CONFIG[bstack1ll1l_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣಹ")] = True
    bstack11l11l1l11_opy_ = bstack11llll1l11_opy_(CONFIG, bstack111l1lll1_opy_)
    logger.debug(bstack1l1ll11111_opy_.format(str(bstack11l11l1l11_opy_)))
    if CONFIG.get(bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ಺")):
      bstack11l1l1llll_opy_(bstack11l11l1l11_opy_)
    if bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಻") in CONFIG and bstack1ll1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧ಼ࠪ") in CONFIG[bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಽ")][bstack111l1lll1_opy_]:
      bstack111llll111_opy_ = CONFIG[bstack1ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಾ")][bstack111l1lll1_opy_][bstack1ll1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ಿ")]
    import urllib
    import json
    if bstack1ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ೀ") in CONFIG and str(CONFIG[bstack1ll1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧು")]).lower() != bstack1ll1l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪೂ"):
        bstack1l1l1l1l1l_opy_ = bstack11lll1111l_opy_()
        bstack1ll11ll111_opy_ = bstack1l1l1l1l1l_opy_ + urllib.parse.quote(json.dumps(bstack11l11l1l11_opy_))
    else:
        bstack1ll11ll111_opy_ = bstack1ll1l_opy_ (u"ࠬࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠧೃ") + urllib.parse.quote(json.dumps(bstack11l11l1l11_opy_))
    browser = self.connect(bstack1ll11ll111_opy_)
    return browser
except Exception as e:
    pass
def bstack111ll1l1ll_opy_():
    global bstack11l1ll1lll_opy_
    global bstack1l1llllll_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1l1llll1l_opy_
        global bstack111111ll_opy_
        if not bstack1llll1l1l1_opy_:
          global bstack111lll11l_opy_
          if not bstack111lll11l_opy_:
            from bstack_utils.helper import bstack111lll111l_opy_, bstack11ll11l11l_opy_, bstack1lll11l111_opy_
            bstack111lll11l_opy_ = bstack111lll111l_opy_()
            bstack11ll11l11l_opy_(bstack1l1llllll_opy_)
            bstack11ll1ll11l_opy_ = bstack1l11lll111_opy_.bstack111l111ll_opy_(CONFIG, bstack1l1llllll_opy_)
            bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"ࠨࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡔࡗࡕࡄࡖࡅࡗࡣࡒࡇࡐࠣೄ"), bstack11ll1ll11l_opy_)
          BrowserType.connect = bstack1l1llll1l_opy_
          return
        BrowserType.launch = bstack1l111ll1ll_opy_
        bstack11l1ll1lll_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1l11ll1l1l_opy_
      bstack11l1ll1lll_opy_ = True
    except Exception as e:
      pass
def bstack1l1l11ll1l_opy_(context, bstack1ll1lll1ll_opy_):
  try:
    context.page.evaluate(bstack1ll1l_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ೅"), bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠬೆ")+ json.dumps(bstack1ll1lll1ll_opy_) + bstack1ll1l_opy_ (u"ࠤࢀࢁࠧೇ"))
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥࢁࡽ࠻ࠢࡾࢁࠧೈ").format(str(e), traceback.format_exc()))
def bstack1111ll1l1l_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1ll1l_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧ೉"), bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪೊ") + json.dumps(message) + bstack1ll1l_opy_ (u"࠭ࠬࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠩೋ") + json.dumps(level) + bstack1ll1l_opy_ (u"ࠧࡾࡿࠪೌ"))
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡦࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠡࡽࢀ࠾ࠥࢁࡽ್ࠣ").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack11l1111ll_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack11l11llll_opy_(self, url):
  global bstack11l111ll1_opy_
  try:
    bstack1l11l1l11l_opy_(url)
  except Exception as err:
    logger.debug(bstack1111l1ll11_opy_.format(str(err)))
  try:
    bstack11l111ll1_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1l1ll1l11l_opy_):
        bstack1l11l1l11l_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1111l1ll11_opy_.format(str(err)))
    raise e
def bstack111l1l1lll_opy_(self):
  global bstack1l1lll1l11_opy_
  bstack1l1lll1l11_opy_ = self
  return
def bstack11l1l1l111_opy_(self):
  global bstack1111ll1l1_opy_
  bstack1111ll1l1_opy_ = self
  return
def bstack1l11ll1ll_opy_(test_name, bstack1111l1l1ll_opy_):
  global CONFIG
  if percy.bstack11llll11l_opy_() == bstack1ll1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ೎"):
    bstack1111l11lll_opy_ = os.path.relpath(bstack1111l1l1ll_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1111l11lll_opy_)
    bstack1llll111ll_opy_ = suite_name + bstack1ll1l_opy_ (u"ࠥ࠱ࠧ೏") + test_name
    threading.current_thread().percySessionName = bstack1llll111ll_opy_
def bstack1l1l1l11l1_opy_(self, test, *args, **kwargs):
  global bstack11l1l111l1_opy_
  test_name = None
  bstack1111l1l1ll_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1111l1l1ll_opy_ = str(test.source)
  bstack1l11ll1ll_opy_(test_name, bstack1111l1l1ll_opy_)
  bstack11l1l111l1_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack111l11ll11_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack11l11ll11l_opy_(driver, bstack1llll111ll_opy_):
  if not bstack111l11l1l1_opy_ and bstack1llll111ll_opy_:
      bstack111llll1l1_opy_ = {
          bstack1ll1l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫ೐"): bstack1ll1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭೑"),
          bstack1ll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ೒"): {
              bstack1ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ೓"): bstack1llll111ll_opy_
          }
      }
      bstack1l1l1ll1ll_opy_ = bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭೔").format(json.dumps(bstack111llll1l1_opy_))
      driver.execute_script(bstack1l1l1ll1ll_opy_)
  if bstack11l1111l1_opy_:
      bstack111l1111l1_opy_ = {
          bstack1ll1l_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩೕ"): bstack1ll1l_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬೖ"),
          bstack1ll1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ೗"): {
              bstack1ll1l_opy_ (u"ࠬࡪࡡࡵࡣࠪ೘"): bstack1llll111ll_opy_ + bstack1ll1l_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨ೙"),
              bstack1ll1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭೚"): bstack1ll1l_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭೛")
          }
      }
      if bstack11l1111l1_opy_.status == bstack1ll1l_opy_ (u"ࠩࡓࡅࡘ࡙ࠧ೜"):
          bstack1ll1l11lll_opy_ = bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨೝ").format(json.dumps(bstack111l1111l1_opy_))
          driver.execute_script(bstack1ll1l11lll_opy_)
          bstack1ll11111l_opy_(driver, bstack1ll1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫೞ"))
      elif bstack11l1111l1_opy_.status == bstack1ll1l_opy_ (u"ࠬࡌࡁࡊࡎࠪ೟"):
          reason = bstack1ll1l_opy_ (u"ࠨࠢೠ")
          bstack1lllll1lll_opy_ = bstack1llll111ll_opy_ + bstack1ll1l_opy_ (u"ࠧࠡࡨࡤ࡭ࡱ࡫ࡤࠨೡ")
          if bstack11l1111l1_opy_.message:
              reason = str(bstack11l1111l1_opy_.message)
              bstack1lllll1lll_opy_ = bstack1lllll1lll_opy_ + bstack1ll1l_opy_ (u"ࠨࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࠨೢ") + reason
          bstack111l1111l1_opy_[bstack1ll1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬೣ")] = {
              bstack1ll1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ೤"): bstack1ll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ೥"),
              bstack1ll1l_opy_ (u"ࠬࡪࡡࡵࡣࠪ೦"): bstack1lllll1lll_opy_
          }
          bstack1ll1l11lll_opy_ = bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ೧").format(json.dumps(bstack111l1111l1_opy_))
          driver.execute_script(bstack1ll1l11lll_opy_)
          bstack1ll11111l_opy_(driver, bstack1ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ೨"), reason)
          bstack1lll11l1l_opy_(reason, str(bstack11l1111l1_opy_), str(bstack1l1lllllll_opy_), logger)
@measure(event_name=EVENTS.bstack11l1l1ll11_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack1l1l1l1ll1_opy_(driver, test):
  if percy.bstack11llll11l_opy_() == bstack1ll1l_opy_ (u"ࠣࡶࡵࡹࡪࠨ೩") and percy.bstack11lllll1ll_opy_() == bstack1ll1l_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦ೪"):
      bstack1l11111l11_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭೫"), None)
      bstack11ll111ll1_opy_(driver, bstack1l11111l11_opy_, test)
  if (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ೬"), None) and
      bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ೭"), None)) or (
      bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭೮"), None) and
      bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ೯"), None)):
      logger.info(bstack1ll1l_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠦࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡ࡫ࡶࠤࡺࡴࡤࡦࡴࡺࡥࡾ࠴ࠠࠣ೰"))
      bstack1lllllll1_opy_.bstack1lllll111_opy_(driver, name=test.name, path=test.source)
def bstack111ll11l11_opy_(test, bstack1llll111ll_opy_):
    try:
      bstack1l11l11lll_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack1ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧೱ")] = bstack1llll111ll_opy_
      if bstack11l1111l1_opy_:
        if bstack11l1111l1_opy_.status == bstack1ll1l_opy_ (u"ࠪࡔࡆ࡙ࡓࠨೲ"):
          data[bstack1ll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫೳ")] = bstack1ll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ೴")
        elif bstack11l1111l1_opy_.status == bstack1ll1l_opy_ (u"࠭ࡆࡂࡋࡏࠫ೵"):
          data[bstack1ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ೶")] = bstack1ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ೷")
          if bstack11l1111l1_opy_.message:
            data[bstack1ll1l_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩ೸")] = str(bstack11l1111l1_opy_.message)
      user = CONFIG[bstack1ll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ೹")]
      key = CONFIG[bstack1ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ೺")]
      host = bstack1ll11l1l1_opy_(cli.config, [bstack1ll1l_opy_ (u"ࠧࡧࡰࡪࡵࠥ೻"), bstack1ll1l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥࠣ೼"), bstack1ll1l_opy_ (u"ࠢࡢࡲ࡬ࠦ೽")], bstack1ll1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠤ೾"))
      url = bstack1ll1l_opy_ (u"ࠩࡾࢁ࠴ࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡴࡧࡶࡷ࡮ࡵ࡮ࡴ࠱ࡾࢁ࠳ࡰࡳࡰࡰࠪ೿").format(host, bstack111111111_opy_)
      headers = {
        bstack1ll1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩഀ"): bstack1ll1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧഁ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽ࡹࡵࡪࡡࡵࡧࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠤം"), datetime.datetime.now() - bstack1l11l11lll_opy_)
    except Exception as e:
      logger.error(bstack111111lll_opy_.format(str(e)))
def bstack1l1lll111l_opy_(test, bstack1llll111ll_opy_):
  global CONFIG
  global bstack1111ll1l1_opy_
  global bstack1l1lll1l11_opy_
  global bstack111111111_opy_
  global bstack11l1111l1_opy_
  global bstack111llll111_opy_
  global bstack1111l1lll_opy_
  global bstack1l111l1ll1_opy_
  global bstack11llll1111_opy_
  global bstack11l1l11l1l_opy_
  global bstack1lll1l111l_opy_
  global bstack1l1111l11l_opy_
  global bstack111lll1l11_opy_
  try:
    if not bstack111111111_opy_:
      with bstack111lll1l11_opy_:
        bstack1l1111l111_opy_ = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"࠭ࡾࠨഃ")), bstack1ll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧഄ"), bstack1ll1l_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪഅ"))
        if os.path.exists(bstack1l1111l111_opy_):
          with open(bstack1l1111l111_opy_, bstack1ll1l_opy_ (u"ࠩࡵࠫആ")) as f:
            content = f.read().strip()
            if content:
              bstack11l11lllll_opy_ = json.loads(bstack1ll1l_opy_ (u"ࠥࡿࠧഇ") + content + bstack1ll1l_opy_ (u"ࠫࠧࡾࠢ࠻ࠢࠥࡽࠧ࠭ഈ") + bstack1ll1l_opy_ (u"ࠧࢃࠢഉ"))
              bstack111111111_opy_ = bstack11l11lllll_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࡶࠤ࡫࡯࡬ࡦ࠼ࠣࠫഊ") + str(e))
  if bstack1lll1l111l_opy_:
    with bstack1ll1l111l_opy_:
      bstack1111llll11_opy_ = bstack1lll1l111l_opy_.copy()
    for driver in bstack1111llll11_opy_:
      if bstack111111111_opy_ == driver.session_id:
        if test:
          bstack1l1l1l1ll1_opy_(driver, test)
        bstack11l11ll11l_opy_(driver, bstack1llll111ll_opy_)
  elif bstack111111111_opy_:
    bstack111ll11l11_opy_(test, bstack1llll111ll_opy_)
  if bstack1111ll1l1_opy_:
    bstack1l111l1ll1_opy_(bstack1111ll1l1_opy_)
  if bstack1l1lll1l11_opy_:
    bstack11llll1111_opy_(bstack1l1lll1l11_opy_)
  if bstack1l1lllll1l_opy_:
    bstack11l1l11l1l_opy_()
def bstack111l1111l_opy_(self, test, *args, **kwargs):
  bstack1llll111ll_opy_ = None
  if test:
    bstack1llll111ll_opy_ = str(test.name)
  bstack1l1lll111l_opy_(test, bstack1llll111ll_opy_)
  bstack1111l1lll_opy_(self, test, *args, **kwargs)
def bstack111ll1ll1l_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11l11l11ll_opy_
  global CONFIG
  global bstack1lll1l111l_opy_
  global bstack111111111_opy_
  global bstack111lll1l11_opy_
  bstack1ll1l1l11l_opy_ = None
  try:
    if bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ഋ"), None) or bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪഌ"), None):
      try:
        if not bstack111111111_opy_:
          bstack1l1111l111_opy_ = os.path.join(os.path.expanduser(bstack1ll1l_opy_ (u"ࠩࢁࠫ഍")), bstack1ll1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪഎ"), bstack1ll1l_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭ഏ"))
          with bstack111lll1l11_opy_:
            if os.path.exists(bstack1l1111l111_opy_):
              with open(bstack1l1111l111_opy_, bstack1ll1l_opy_ (u"ࠬࡸࠧഐ")) as f:
                content = f.read().strip()
                if content:
                  bstack11l11lllll_opy_ = json.loads(bstack1ll1l_opy_ (u"ࠨࡻࠣ഑") + content + bstack1ll1l_opy_ (u"ࠧࠣࡺࠥ࠾ࠥࠨࡹࠣࠩഒ") + bstack1ll1l_opy_ (u"ࠣࡿࠥഓ"))
                  bstack111111111_opy_ = bstack11l11lllll_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack1ll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡍࡉࡹࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡶࡨࡷࡹࠦࡳࡵࡣࡷࡹࡸࡀࠠࠨഔ") + str(e))
      if bstack1lll1l111l_opy_:
        with bstack1ll1l111l_opy_:
          bstack1111llll11_opy_ = bstack1lll1l111l_opy_.copy()
        for driver in bstack1111llll11_opy_:
          if bstack111111111_opy_ == driver.session_id:
            bstack1ll1l1l11l_opy_ = driver
    bstack11llllll1_opy_ = bstack1lllllll1_opy_.bstack1l11l1llll_opy_(test.tags)
    if bstack1ll1l1l11l_opy_:
      threading.current_thread().isA11yTest = bstack1lllllll1_opy_.bstack1lll11ll11_opy_(bstack1ll1l1l11l_opy_, bstack11llllll1_opy_)
      threading.current_thread().isAppA11yTest = bstack1lllllll1_opy_.bstack1lll11ll11_opy_(bstack1ll1l1l11l_opy_, bstack11llllll1_opy_)
    else:
      threading.current_thread().isA11yTest = bstack11llllll1_opy_
      threading.current_thread().isAppA11yTest = bstack11llllll1_opy_
  except:
    pass
  bstack11l11l11ll_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack11l1111l1_opy_
  try:
    bstack11l1111l1_opy_ = self._test
  except:
    bstack11l1111l1_opy_ = self.test
def bstack11l1lll11_opy_():
  global bstack111ll1ll11_opy_
  try:
    if os.path.exists(bstack111ll1ll11_opy_):
      os.remove(bstack111ll1ll11_opy_)
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ക") + str(e))
def bstack11l1l1l11_opy_():
  global bstack111ll1ll11_opy_
  bstack11111llll_opy_ = {}
  lock_file = bstack111ll1ll11_opy_ + bstack1ll1l_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪഖ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨഗ"))
    try:
      if not os.path.isfile(bstack111ll1ll11_opy_):
        with open(bstack111ll1ll11_opy_, bstack1ll1l_opy_ (u"࠭ࡷࠨഘ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack111ll1ll11_opy_):
        with open(bstack111ll1ll11_opy_, bstack1ll1l_opy_ (u"ࠧࡳࠩങ")) as f:
          content = f.read().strip()
          if content:
            bstack11111llll_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack1ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪࡧࡤࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪച") + str(e))
    return bstack11111llll_opy_
  try:
    os.makedirs(os.path.dirname(bstack111ll1ll11_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack111ll1ll11_opy_):
        with open(bstack111ll1ll11_opy_, bstack1ll1l_opy_ (u"ࠩࡺࠫഛ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack111ll1ll11_opy_):
        with open(bstack111ll1ll11_opy_, bstack1ll1l_opy_ (u"ࠪࡶࠬജ")) as f:
          content = f.read().strip()
          if content:
            bstack11111llll_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ഝ") + str(e))
  finally:
    return bstack11111llll_opy_
def bstack1111ll111l_opy_(platform_index, item_index):
  global bstack111ll1ll11_opy_
  lock_file = bstack111ll1ll11_opy_ + bstack1ll1l_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫഞ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩട"))
    try:
      bstack11111llll_opy_ = {}
      if os.path.exists(bstack111ll1ll11_opy_):
        with open(bstack111ll1ll11_opy_, bstack1ll1l_opy_ (u"ࠧࡳࠩഠ")) as f:
          content = f.read().strip()
          if content:
            bstack11111llll_opy_ = json.loads(content)
      bstack11111llll_opy_[item_index] = platform_index
      with open(bstack111ll1ll11_opy_, bstack1ll1l_opy_ (u"ࠣࡹࠥഡ")) as outfile:
        json.dump(bstack11111llll_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1ll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡼࡸࡩࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧഢ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack111ll1ll11_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack11111llll_opy_ = {}
      if os.path.exists(bstack111ll1ll11_opy_):
        with open(bstack111ll1ll11_opy_, bstack1ll1l_opy_ (u"ࠪࡶࠬണ")) as f:
          content = f.read().strip()
          if content:
            bstack11111llll_opy_ = json.loads(content)
      bstack11111llll_opy_[item_index] = platform_index
      with open(bstack111ll1ll11_opy_, bstack1ll1l_opy_ (u"ࠦࡼࠨത")) as outfile:
        json.dump(bstack11111llll_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡸࡴ࡬ࡸ࡮ࡴࡧࠡࡶࡲࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪഥ") + str(e))
def bstack11ll1ll1l_opy_(bstack11l1lll1ll_opy_):
  global CONFIG
  bstack111l11l1ll_opy_ = bstack1ll1l_opy_ (u"࠭ࠧദ")
  if not bstack1ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪധ") in CONFIG:
    logger.info(bstack1ll1l_opy_ (u"ࠨࡐࡲࠤࡵࡲࡡࡵࡨࡲࡶࡲࡹࠠࡱࡣࡶࡷࡪࡪࠠࡶࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥࡸࡥࡱࡱࡵࡸࠥ࡬࡯ࡳࠢࡕࡳࡧࡵࡴࠡࡴࡸࡲࠬന"))
  try:
    platform = CONFIG[bstack1ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬഩ")][bstack11l1lll1ll_opy_]
    if bstack1ll1l_opy_ (u"ࠪࡳࡸ࠭പ") in platform:
      bstack111l11l1ll_opy_ += str(platform[bstack1ll1l_opy_ (u"ࠫࡴࡹࠧഫ")]) + bstack1ll1l_opy_ (u"ࠬ࠲ࠠࠨബ")
    if bstack1ll1l_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩഭ") in platform:
      bstack111l11l1ll_opy_ += str(platform[bstack1ll1l_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪമ")]) + bstack1ll1l_opy_ (u"ࠨ࠮ࠣࠫയ")
    if bstack1ll1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ര") in platform:
      bstack111l11l1ll_opy_ += str(platform[bstack1ll1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧറ")]) + bstack1ll1l_opy_ (u"ࠫ࠱ࠦࠧല")
    if bstack1ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧള") in platform:
      bstack111l11l1ll_opy_ += str(platform[bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨഴ")]) + bstack1ll1l_opy_ (u"ࠧ࠭ࠢࠪവ")
    if bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ശ") in platform:
      bstack111l11l1ll_opy_ += str(platform[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧഷ")]) + bstack1ll1l_opy_ (u"ࠪ࠰ࠥ࠭സ")
    if bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬഹ") in platform:
      bstack111l11l1ll_opy_ += str(platform[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ഺ")]) + bstack1ll1l_opy_ (u"഻࠭ࠬࠡࠩ")
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠧࡔࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡱࡩࡷࡧࡴࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡳࡵࡴ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡶࡪࡶ࡯ࡳࡶࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡴࡴ഼ࠧ") + str(e))
  finally:
    if bstack111l11l1ll_opy_[len(bstack111l11l1ll_opy_) - 2:] == bstack1ll1l_opy_ (u"ࠨ࠮ࠣࠫഽ"):
      bstack111l11l1ll_opy_ = bstack111l11l1ll_opy_[:-2]
    return bstack111l11l1ll_opy_
def bstack1111llll1l_opy_(path, bstack111l11l1ll_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l1llllll1_opy_ = ET.parse(path)
    bstack11l1llll11_opy_ = bstack1l1llllll1_opy_.getroot()
    bstack11ll1l1lll_opy_ = None
    for suite in bstack11l1llll11_opy_.iter(bstack1ll1l_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨാ")):
      if bstack1ll1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪി") in suite.attrib:
        suite.attrib[bstack1ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩീ")] += bstack1ll1l_opy_ (u"ࠬࠦࠧു") + bstack111l11l1ll_opy_
        bstack11ll1l1lll_opy_ = suite
    bstack11ll11ll1_opy_ = None
    for robot in bstack11l1llll11_opy_.iter(bstack1ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬൂ")):
      bstack11ll11ll1_opy_ = robot
    bstack1l1l111ll_opy_ = len(bstack11ll11ll1_opy_.findall(bstack1ll1l_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ൃ")))
    if bstack1l1l111ll_opy_ == 1:
      bstack11ll11ll1_opy_.remove(bstack11ll11ll1_opy_.findall(bstack1ll1l_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧൄ"))[0])
      bstack11111llll1_opy_ = ET.Element(bstack1ll1l_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨ൅"), attrib={bstack1ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨെ"): bstack1ll1l_opy_ (u"ࠫࡘࡻࡩࡵࡧࡶࠫേ"), bstack1ll1l_opy_ (u"ࠬ࡯ࡤࠨൈ"): bstack1ll1l_opy_ (u"࠭ࡳ࠱ࠩ൉")})
      bstack11ll11ll1_opy_.insert(1, bstack11111llll1_opy_)
      bstack11ll1llll_opy_ = None
      for suite in bstack11ll11ll1_opy_.iter(bstack1ll1l_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ൊ")):
        bstack11ll1llll_opy_ = suite
      bstack11ll1llll_opy_.append(bstack11ll1l1lll_opy_)
      bstack1111l1ll1l_opy_ = None
      for status in bstack11ll1l1lll_opy_.iter(bstack1ll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨോ")):
        bstack1111l1ll1l_opy_ = status
      bstack11ll1llll_opy_.append(bstack1111l1ll1l_opy_)
    bstack1l1llllll1_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠧൌ") + str(e))
def bstack1l1l11l111_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack11l1111lll_opy_
  global CONFIG
  if bstack1ll1l_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮്ࠢ") in options:
    del options[bstack1ll1l_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣൎ")]
  json_data = bstack11l1l1l11_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack1ll1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࡣࡷ࡫ࡳࡶ࡮ࡷࡷࠬ൏"), str(item_id), bstack1ll1l_opy_ (u"࠭࡯ࡶࡶࡳࡹࡹ࠴ࡸ࡮࡮ࠪ൐"))
    bstack1111llll1l_opy_(path, bstack11ll1ll1l_opy_(json_data[item_id]))
  bstack11l1lll11_opy_()
  return bstack11l1111lll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack11lll11l1_opy_(self, ff_profile_dir):
  global bstack1l11l1111l_opy_
  if not ff_profile_dir:
    return None
  return bstack1l11l1111l_opy_(self, ff_profile_dir)
def bstack1111ll11l_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l1lllll11_opy_
  bstack11l1ll111l_opy_ = []
  if bstack1ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ൑") in CONFIG:
    bstack11l1ll111l_opy_ = CONFIG[bstack1ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ൒")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1ll1l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࠥ൓")],
      pabot_args[bstack1ll1l_opy_ (u"ࠥࡺࡪࡸࡢࡰࡵࡨࠦൔ")],
      argfile,
      pabot_args.get(bstack1ll1l_opy_ (u"ࠦ࡭࡯ࡶࡦࠤൕ")),
      pabot_args[bstack1ll1l_opy_ (u"ࠧࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠣൖ")],
      platform[0],
      bstack1l1lllll11_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1ll1l_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡧ࡫࡯ࡩࡸࠨൗ")] or [(bstack1ll1l_opy_ (u"ࠢࠣ൘"), None)]
    for platform in enumerate(bstack11l1ll111l_opy_)
  ]
def bstack1111ll1ll1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1lll1l1l11_opy_=bstack1ll1l_opy_ (u"ࠨࠩ൙")):
  global bstack1l11lll11l_opy_
  self.platform_index = platform_index
  self.bstack1lll1lll11_opy_ = bstack1lll1l1l11_opy_
  bstack1l11lll11l_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack11l111l111_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l11lll1ll_opy_
  global bstack111l1ll111_opy_
  bstack1ll1l1l111_opy_ = copy.deepcopy(item)
  if not bstack1ll1l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ൚") in item.options:
    bstack1ll1l1l111_opy_.options[bstack1ll1l_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ൛")] = []
  bstack1111lll1ll_opy_ = bstack1ll1l1l111_opy_.options[bstack1ll1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭൜")].copy()
  for v in bstack1ll1l1l111_opy_.options[bstack1ll1l_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ൝")]:
    if bstack1ll1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜ࠬ൞") in v:
      bstack1111lll1ll_opy_.remove(v)
    if bstack1ll1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙ࠧൟ") in v:
      bstack1111lll1ll_opy_.remove(v)
    if bstack1ll1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬൠ") in v:
      bstack1111lll1ll_opy_.remove(v)
  bstack1111lll1ll_opy_.insert(0, bstack1ll1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘ࠻ࡽࢀࠫൡ").format(bstack1ll1l1l111_opy_.platform_index))
  bstack1111lll1ll_opy_.insert(0, bstack1ll1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘ࠺ࡼࡿࠪൢ").format(bstack1ll1l1l111_opy_.bstack1lll1lll11_opy_))
  bstack1ll1l1l111_opy_.options[bstack1ll1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ൣ")] = bstack1111lll1ll_opy_
  if bstack111l1ll111_opy_:
    bstack1ll1l1l111_opy_.options[bstack1ll1l_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ൤")].insert(0, bstack1ll1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘࡀࡻࡾࠩ൥").format(bstack111l1ll111_opy_))
  return bstack1l11lll1ll_opy_(caller_id, datasources, is_last, bstack1ll1l1l111_opy_, outs_dir)
def bstack1l1l11ll1_opy_(command, item_index):
  try:
    if bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ൦")):
      os.environ[bstack1ll1l_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩ൧")] = json.dumps(CONFIG[bstack1ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ൨")][item_index % bstack11111ll1ll_opy_])
    global bstack111l1ll111_opy_
    if bstack111l1ll111_opy_:
      command[0] = command[0].replace(bstack1ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ൩"), bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨ൪") + str(
        item_index) + bstack1ll1l_opy_ (u"ࠬࠦࠧ൫") + bstack111l1ll111_opy_, 1)
    else:
      command[0] = command[0].replace(bstack1ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ൬"),
                                      bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡳࡥ࡭ࠣࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠣࠫ൭") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack1ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠ࡮ࡱࡧ࡭࡫ࡿࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡢࡰࡧࠤ࡫ࡵࡲࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱ࠾ࠥࢁࡽࠨ൮").format(str(e)))
def bstack11l111l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack111ll11ll_opy_
  try:
    bstack1l1l11ll1_opy_(command, item_index)
    return bstack111ll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack1ll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴ࠺ࠡࡽࢀࠫ൯").format(str(e)))
    raise e
def bstack1l1l11l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack111ll11ll_opy_
  try:
    bstack1l1l11ll1_opy_(command, item_index)
    return bstack111ll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack1ll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠴࠱࠵࠸ࡀࠠࡼࡿࠪ൰").format(str(e)))
    try:
      return bstack111ll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack1ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࠸࠮࠲࠵ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩ൱").format(str(e2)))
      raise e
def bstack1111ll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack111ll11ll_opy_
  try:
    bstack1l1l11ll1_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack111ll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack1ll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰࠣ࠶࠳࠷࠵࠻ࠢࡾࢁࠬ൲").format(str(e)))
    try:
      return bstack111ll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack1ll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠ࠳࠰࠴࠹ࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫ൳").format(str(e2)))
      raise e
def _1l11llll1_opy_(bstack1l1llll11_opy_, item_index, process_timeout, sleep_before_start, bstack1l1llll1ll_opy_):
  bstack1l1l11ll1_opy_(bstack1l1llll11_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack111ll1l1l1_opy_(command, bstack11l1111111_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack111ll11ll_opy_
  try:
    bstack1l1l11ll1_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack111ll11ll_opy_(command, bstack11l1111111_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲࠥ࠻࠮࠱࠼ࠣࡿࢂ࠭൴").format(str(e)))
    try:
      return bstack111ll11ll_opy_(command, bstack11l1111111_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨ൵").format(str(e2)))
      raise e
def bstack11ll1l1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack111ll11ll_opy_
  try:
    process_timeout = _1l11llll1_opy_(command, item_index, process_timeout, sleep_before_start, bstack1ll1l_opy_ (u"ࠩ࠷࠲࠷࠭൶"))
    return bstack111ll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1ll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠶࠱࠶࠿ࠦࡻࡾࠩ൷").format(str(e)))
    try:
      return bstack111ll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫ൸").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack1lll1111l1_opy_(self, runner, quiet=False, capture=True):
  global bstack1ll11l11l1_opy_
  bstack11l1lll1l1_opy_ = bstack1ll11l11l1_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack1ll1l_opy_ (u"ࠬ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࡠࡣࡵࡶࠬ൹")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1ll1l_opy_ (u"࠭ࡥࡹࡥࡢࡸࡷࡧࡣࡦࡤࡤࡧࡰࡥࡡࡳࡴࠪൺ")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack11l1lll1l1_opy_
def bstack11111ll11_opy_(runner, hook_name, context, element, bstack111l111111_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1l11l11l1l_opy_.bstack11ll11l1_opy_(hook_name, element)
    bstack111l111111_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1l11l11l1l_opy_.bstack11ll1l11_opy_(element)
      if hook_name not in [bstack1ll1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫൻ"), bstack1ll1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫർ")] and args and hasattr(args[0], bstack1ll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࡠ࡯ࡨࡷࡸࡧࡧࡦࠩൽ")):
        args[0].error_message = bstack1ll1l_opy_ (u"ࠪࠫൾ")
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡩࡣࡱࡨࡱ࡫ࠠࡩࡱࡲ࡯ࡸࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦ࠼ࠣࡿࢂ࠭ൿ").format(str(e)))
@measure(event_name=EVENTS.bstack11ll11111l_opy_, stage=STAGE.bstack11lll11ll_opy_, hook_type=bstack1ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡆࡲ࡬ࠣ඀"), bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack1ll11l1ll1_opy_(runner, name, context, bstack111l111111_opy_, *args):
    if runner.hooks.get(bstack1ll1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥඁ")).__name__ != bstack1ll1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࡣࡩ࡫ࡦࡢࡷ࡯ࡸࡤ࡮࡯ࡰ࡭ࠥං"):
      bstack11111ll11_opy_(runner, name, context, runner, bstack111l111111_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1l111111ll_opy_(bstack1ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧඃ")) else context.browser
      runner.driver_initialised = bstack1ll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨ඄")
    except Exception as e:
      logger.debug(bstack1ll1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡸ࡫ࠠࡢࡶࡷࡶ࡮ࡨࡵࡵࡧ࠽ࠤࢀࢃࠧඅ").format(str(e)))
def bstack111ll1l11l_opy_(runner, name, context, bstack111l111111_opy_, *args):
    bstack11111ll11_opy_(runner, name, context, context.feature, bstack111l111111_opy_, *args)
    try:
      if not bstack111l11l1l1_opy_:
        bstack1ll1l1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111111ll_opy_(bstack1ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪආ")) else context.browser
        if is_driver_active(bstack1ll1l1l11l_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack1ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨඇ")
          bstack1ll1lll1ll_opy_ = str(runner.feature.name)
          bstack1l1l11ll1l_opy_(context, bstack1ll1lll1ll_opy_)
          bstack1ll1l1l11l_opy_.execute_script(bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫඈ") + json.dumps(bstack1ll1lll1ll_opy_) + bstack1ll1l_opy_ (u"ࠧࡾࡿࠪඉ"))
    except Exception as e:
      logger.debug(bstack1ll1l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨඊ").format(str(e)))
def bstack111ll11111_opy_(runner, name, context, bstack111l111111_opy_, *args):
    if hasattr(context, bstack1ll1l_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫඋ")):
        bstack1l11l11l1l_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack1ll1l_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬඌ")) else context.feature
    bstack11111ll11_opy_(runner, name, context, target, bstack111l111111_opy_, *args)
@measure(event_name=EVENTS.bstack1l11111l1l_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack11llll1lll_opy_(runner, name, context, bstack111l111111_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1l11l11l1l_opy_.start_test(context)
    bstack11111ll11_opy_(runner, name, context, context.scenario, bstack111l111111_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1ll1lllll_opy_.bstack1ll111llll_opy_(context, *args)
    try:
      bstack1ll1l1l11l_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪඍ"), context.browser)
      if is_driver_active(bstack1ll1l1l11l_opy_):
        bstack1lllll11_opy_.bstack111ll1lll1_opy_(bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫඎ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack1ll1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣඏ")
        if (not bstack111l11l1l1_opy_):
          scenario_name = args[0].name
          feature_name = bstack1ll1lll1ll_opy_ = str(runner.feature.name)
          bstack1ll1lll1ll_opy_ = feature_name + bstack1ll1l_opy_ (u"ࠧࠡ࠯ࠣࠫඐ") + scenario_name
          if runner.driver_initialised == bstack1ll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥඑ"):
            bstack1l1l11ll1l_opy_(context, bstack1ll1lll1ll_opy_)
            bstack1ll1l1l11l_opy_.execute_script(bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧඒ") + json.dumps(bstack1ll1lll1ll_opy_) + bstack1ll1l_opy_ (u"ࠪࢁࢂ࠭ඓ"))
    except Exception as e:
      logger.debug(bstack1ll1l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬඔ").format(str(e)))
@measure(event_name=EVENTS.bstack11ll11111l_opy_, stage=STAGE.bstack11lll11ll_opy_, hook_type=bstack1ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡘࡺࡥࡱࠤඕ"), bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack1ll11ll11_opy_(runner, name, context, bstack111l111111_opy_, *args):
    bstack11111ll11_opy_(runner, name, context, args[0], bstack111l111111_opy_, *args)
    try:
      bstack1ll1l1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111111ll_opy_(bstack1ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඖ")) else context.browser
      if is_driver_active(bstack1ll1l1l11l_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack1ll1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧ඗")
        bstack1l11l11l1l_opy_.bstack11l1ll1l_opy_(args[0])
        if runner.driver_initialised == bstack1ll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨ඘"):
          feature_name = bstack1ll1lll1ll_opy_ = str(runner.feature.name)
          bstack1ll1lll1ll_opy_ = feature_name + bstack1ll1l_opy_ (u"ࠩࠣ࠱ࠥ࠭඙") + context.scenario.name
          bstack1ll1l1l11l_opy_.execute_script(bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨක") + json.dumps(bstack1ll1lll1ll_opy_) + bstack1ll1l_opy_ (u"ࠫࢂࢃࠧඛ"))
    except Exception as e:
      logger.debug(bstack1ll1l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩග").format(str(e)))
@measure(event_name=EVENTS.bstack11ll11111l_opy_, stage=STAGE.bstack11lll11ll_opy_, hook_type=bstack1ll1l_opy_ (u"ࠨࡡࡧࡶࡨࡶࡘࡺࡥࡱࠤඝ"), bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack11ll11l11_opy_(runner, name, context, bstack111l111111_opy_, *args):
  bstack1l11l11l1l_opy_.bstack11ll1lll_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack1ll1l1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ඞ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1ll1l1l11l_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack1ll1l_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨඟ")
        feature_name = bstack1ll1lll1ll_opy_ = str(runner.feature.name)
        bstack1ll1lll1ll_opy_ = feature_name + bstack1ll1l_opy_ (u"ࠩࠣ࠱ࠥ࠭ච") + context.scenario.name
        bstack1ll1l1l11l_opy_.execute_script(bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨඡ") + json.dumps(bstack1ll1lll1ll_opy_) + bstack1ll1l_opy_ (u"ࠫࢂࢃࠧජ"))
    if str(step_status).lower() == bstack1ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬඣ"):
      bstack11l1111ll1_opy_ = bstack1ll1l_opy_ (u"࠭ࠧඤ")
      bstack1ll1lll11l_opy_ = bstack1ll1l_opy_ (u"ࠧࠨඥ")
      bstack1l1l1l1l11_opy_ = bstack1ll1l_opy_ (u"ࠨࠩඦ")
      try:
        import traceback
        bstack11l1111ll1_opy_ = runner.exception.__class__.__name__
        bstack11l1l1l1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1ll1lll11l_opy_ = bstack1ll1l_opy_ (u"ࠩࠣࠫට").join(bstack11l1l1l1_opy_)
        bstack1l1l1l1l11_opy_ = bstack11l1l1l1_opy_[-1]
      except Exception as e:
        logger.debug(bstack11l1111l11_opy_.format(str(e)))
      bstack11l1111ll1_opy_ += bstack1l1l1l1l11_opy_
      bstack1111ll1l1l_opy_(context, json.dumps(str(args[0].name) + bstack1ll1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤඨ") + str(bstack1ll1lll11l_opy_)),
                          bstack1ll1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥඩ"))
      if runner.driver_initialised == bstack1ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥඪ"):
        bstack1ll1l1ll1_opy_(getattr(context, bstack1ll1l_opy_ (u"࠭ࡰࡢࡩࡨࠫණ"), None), bstack1ll1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢඬ"), bstack11l1111ll1_opy_)
        bstack1ll1l1l11l_opy_.execute_script(bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ත") + json.dumps(str(args[0].name) + bstack1ll1l_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣථ") + str(bstack1ll1lll11l_opy_)) + bstack1ll1l_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪද"))
      if runner.driver_initialised == bstack1ll1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤධ"):
        bstack1ll11111l_opy_(bstack1ll1l1l11l_opy_, bstack1ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬන"), bstack1ll1l_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥ඲") + str(bstack11l1111ll1_opy_))
    else:
      bstack1111ll1l1l_opy_(context, bstack1ll1l_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣඳ"), bstack1ll1l_opy_ (u"ࠣ࡫ࡱࡪࡴࠨප"))
      if runner.driver_initialised == bstack1ll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢඵ"):
        bstack1ll1l1ll1_opy_(getattr(context, bstack1ll1l_opy_ (u"ࠪࡴࡦ࡭ࡥࠨබ"), None), bstack1ll1l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦභ"))
      bstack1ll1l1l11l_opy_.execute_script(bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪම") + json.dumps(str(args[0].name) + bstack1ll1l_opy_ (u"ࠨࠠ࠮ࠢࡓࡥࡸࡹࡥࡥࠣࠥඹ")) + bstack1ll1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭ය"))
      if runner.driver_initialised == bstack1ll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨර"):
        bstack1ll11111l_opy_(bstack1ll1l1l11l_opy_, bstack1ll1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ඼"))
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩල").format(str(e)))
  bstack11111ll11_opy_(runner, name, context, args[0], bstack111l111111_opy_, *args)
@measure(event_name=EVENTS.bstack1ll1111lll_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack1111l1l11_opy_(runner, name, context, bstack111l111111_opy_, *args):
  bstack1l11l11l1l_opy_.end_test(args[0])
  try:
    bstack11ll1l111l_opy_ = args[0].status.name
    bstack1ll1l1l11l_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ඾"), context.browser)
    bstack1ll1lllll_opy_.bstack11l1llllll_opy_(bstack1ll1l1l11l_opy_)
    if str(bstack11ll1l111l_opy_).lower() == bstack1ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ඿"):
      bstack11l1111ll1_opy_ = bstack1ll1l_opy_ (u"࠭ࠧව")
      bstack1ll1lll11l_opy_ = bstack1ll1l_opy_ (u"ࠧࠨශ")
      bstack1l1l1l1l11_opy_ = bstack1ll1l_opy_ (u"ࠨࠩෂ")
      try:
        import traceback
        bstack11l1111ll1_opy_ = runner.exception.__class__.__name__
        bstack11l1l1l1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1ll1lll11l_opy_ = bstack1ll1l_opy_ (u"ࠩࠣࠫස").join(bstack11l1l1l1_opy_)
        bstack1l1l1l1l11_opy_ = bstack11l1l1l1_opy_[-1]
      except Exception as e:
        logger.debug(bstack11l1111l11_opy_.format(str(e)))
      bstack11l1111ll1_opy_ += bstack1l1l1l1l11_opy_
      bstack1111ll1l1l_opy_(context, json.dumps(str(args[0].name) + bstack1ll1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤහ") + str(bstack1ll1lll11l_opy_)),
                          bstack1ll1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥළ"))
      if runner.driver_initialised == bstack1ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢෆ") or runner.driver_initialised == bstack1ll1l_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෇"):
        bstack1ll1l1ll1_opy_(getattr(context, bstack1ll1l_opy_ (u"ࠧࡱࡣࡪࡩࠬ෈"), None), bstack1ll1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ෉"), bstack11l1111ll1_opy_)
        bstack1ll1l1l11l_opy_.execute_script(bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀ්ࠧ") + json.dumps(str(args[0].name) + bstack1ll1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ෋") + str(bstack1ll1lll11l_opy_)) + bstack1ll1l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫ෌"))
      if runner.driver_initialised == bstack1ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ෍") or runner.driver_initialised == bstack1ll1l_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෎"):
        bstack1ll11111l_opy_(bstack1ll1l1l11l_opy_, bstack1ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧා"), bstack1ll1l_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧැ") + str(bstack11l1111ll1_opy_))
    else:
      bstack1111ll1l1l_opy_(context, bstack1ll1l_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥෑ"), bstack1ll1l_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣි"))
      if runner.driver_initialised == bstack1ll1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨී") or runner.driver_initialised == bstack1ll1l_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬු"):
        bstack1ll1l1ll1_opy_(getattr(context, bstack1ll1l_opy_ (u"࠭ࡰࡢࡩࡨࠫ෕"), None), bstack1ll1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢූ"))
      bstack1ll1l1l11l_opy_.execute_script(bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭෗") + json.dumps(str(args[0].name) + bstack1ll1l_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨෘ")) + bstack1ll1l_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩෙ"))
      if runner.driver_initialised == bstack1ll1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨේ") or runner.driver_initialised == bstack1ll1l_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬෛ"):
        bstack1ll11111l_opy_(bstack1ll1l1l11l_opy_, bstack1ll1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨො"))
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩෝ").format(str(e)))
  bstack11111ll11_opy_(runner, name, context, context.scenario, bstack111l111111_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1lll1l11ll_opy_(runner, name, context, bstack111l111111_opy_, *args):
    target = context.scenario if hasattr(context, bstack1ll1l_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪෞ")) else context.feature
    bstack11111ll11_opy_(runner, name, context, target, bstack111l111111_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1ll11lll1l_opy_(runner, name, context, bstack111l111111_opy_, *args):
    try:
      bstack1ll1l1l11l_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨෟ"), context.browser)
      bstack1lll1l1111_opy_ = bstack1ll1l_opy_ (u"ࠪࠫ෠")
      if context.failed is True:
        bstack11l11l111_opy_ = []
        bstack111lll11l1_opy_ = []
        bstack1l111ll11_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack11l11l111_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l1l1l1_opy_ = traceback.format_tb(exc_tb)
            bstack11l111111_opy_ = bstack1ll1l_opy_ (u"ࠫࠥ࠭෡").join(bstack11l1l1l1_opy_)
            bstack111lll11l1_opy_.append(bstack11l111111_opy_)
            bstack1l111ll11_opy_.append(bstack11l1l1l1_opy_[-1])
        except Exception as e:
          logger.debug(bstack11l1111l11_opy_.format(str(e)))
        bstack11l1111ll1_opy_ = bstack1ll1l_opy_ (u"ࠬ࠭෢")
        for i in range(len(bstack11l11l111_opy_)):
          bstack11l1111ll1_opy_ += bstack11l11l111_opy_[i] + bstack1l111ll11_opy_[i] + bstack1ll1l_opy_ (u"࠭࡜࡯ࠩ෣")
        bstack1lll1l1111_opy_ = bstack1ll1l_opy_ (u"ࠧࠡࠩ෤").join(bstack111lll11l1_opy_)
        if runner.driver_initialised in [bstack1ll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤ෥"), bstack1ll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨ෦")]:
          bstack1111ll1l1l_opy_(context, bstack1lll1l1111_opy_, bstack1ll1l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ෧"))
          bstack1ll1l1ll1_opy_(getattr(context, bstack1ll1l_opy_ (u"ࠫࡵࡧࡧࡦࠩ෨"), None), bstack1ll1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ෩"), bstack11l1111ll1_opy_)
          bstack1ll1l1l11l_opy_.execute_script(bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ෪") + json.dumps(bstack1lll1l1111_opy_) + bstack1ll1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧ෫"))
          bstack1ll11111l_opy_(bstack1ll1l1l11l_opy_, bstack1ll1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ෬"), bstack1ll1l_opy_ (u"ࠤࡖࡳࡲ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰࡵࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡡࡴࠢ෭") + str(bstack11l1111ll1_opy_))
          bstack1111ll1lll_opy_ = bstack11l1ll11ll_opy_(bstack1lll1l1111_opy_, runner.feature.name, logger)
          if (bstack1111ll1lll_opy_ != None):
            bstack11llll111_opy_.append(bstack1111ll1lll_opy_)
      else:
        if runner.driver_initialised in [bstack1ll1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦ෮"), bstack1ll1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣ෯")]:
          bstack1111ll1l1l_opy_(context, bstack1ll1l_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣ෰") + str(runner.feature.name) + bstack1ll1l_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣ෱"), bstack1ll1l_opy_ (u"ࠢࡪࡰࡩࡳࠧෲ"))
          bstack1ll1l1ll1_opy_(getattr(context, bstack1ll1l_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ෳ"), None), bstack1ll1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ෴"))
          bstack1ll1l1l11l_opy_.execute_script(bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ෵") + json.dumps(bstack1ll1l_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢ෶") + str(runner.feature.name) + bstack1ll1l_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢ෷")) + bstack1ll1l_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬ෸"))
          bstack1ll11111l_opy_(bstack1ll1l1l11l_opy_, bstack1ll1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ෹"))
          bstack1111ll1lll_opy_ = bstack11l1ll11ll_opy_(bstack1lll1l1111_opy_, runner.feature.name, logger)
          if (bstack1111ll1lll_opy_ != None):
            bstack11llll111_opy_.append(bstack1111ll1lll_opy_)
    except Exception as e:
      logger.debug(bstack1ll1l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪ෺").format(str(e)))
    bstack11111ll11_opy_(runner, name, context, context.feature, bstack111l111111_opy_, *args)
@measure(event_name=EVENTS.bstack11ll11111l_opy_, stage=STAGE.bstack11lll11ll_opy_, hook_type=bstack1ll1l_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡂ࡮࡯ࠦ෻"), bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack11l111lll_opy_(runner, name, context, bstack111l111111_opy_, *args):
    bstack11111ll11_opy_(runner, name, context, runner, bstack111l111111_opy_, *args)
def bstack1l111l1lll_opy_(self, name, context, *args):
  try:
    if bstack1llll1l1l1_opy_:
      platform_index = int(threading.current_thread()._name) % bstack11111ll1ll_opy_
      bstack111l1llll_opy_ = CONFIG[bstack1ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭෼")][platform_index]
      os.environ[bstack1ll1l_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬ෽")] = json.dumps(bstack111l1llll_opy_)
    global bstack111l111111_opy_
    if not hasattr(self, bstack1ll1l_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡦࡦࠪ෾")):
      self.driver_initialised = None
    bstack1l1ll1ll1_opy_ = {
        bstack1ll1l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪ෿"): bstack1ll11l1ll1_opy_,
        bstack1ll1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠨ฀"): bstack111ll1l11l_opy_,
        bstack1ll1l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡶࡤ࡫ࠬก"): bstack111ll11111_opy_,
        bstack1ll1l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫข"): bstack11llll1lll_opy_,
        bstack1ll1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠨฃ"): bstack1ll11ll11_opy_,
        bstack1ll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡹ࡫ࡰࠨค"): bstack11ll11l11_opy_,
        bstack1ll1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ฅ"): bstack1111l1l11_opy_,
        bstack1ll1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡺࡡࡨࠩฆ"): bstack1lll1l11ll_opy_,
        bstack1ll1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧง"): bstack1ll11lll1l_opy_,
        bstack1ll1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫจ"): bstack11l111lll_opy_
    }
    handler = bstack1l1ll1ll1_opy_.get(name, bstack111l111111_opy_)
    try:
      handler(self, name, context, bstack111l111111_opy_, *args)
    except Exception as e:
      logger.debug(bstack1ll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨࠤ࡭ࡵ࡯࡬ࠢ࡫ࡥࡳࡪ࡬ࡦࡴࠣࡿࢂࡀࠠࡼࡿࠪฉ").format(name, str(e)))
    if name in [bstack1ll1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪช"), bstack1ll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬซ"), bstack1ll1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨฌ")]:
      try:
        bstack1ll1l1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111111ll_opy_(bstack1ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬญ")) else context.browser
        bstack1l11ll111l_opy_ = (
          (name == bstack1ll1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪฎ") and self.driver_initialised == bstack1ll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧฏ")) or
          (name == bstack1ll1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩฐ") and self.driver_initialised == bstack1ll1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦฑ")) or
          (name == bstack1ll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬฒ") and self.driver_initialised in [bstack1ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢณ"), bstack1ll1l_opy_ (u"ࠨࡩ࡯ࡵࡷࡩࡵࠨด")]) or
          (name == bstack1ll1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡵࡧࡳࠫต") and self.driver_initialised == bstack1ll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨถ"))
        )
        if bstack1l11ll111l_opy_:
          self.driver_initialised = None
          if bstack1ll1l1l11l_opy_ and hasattr(bstack1ll1l1l11l_opy_, bstack1ll1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩ࠭ท")):
            try:
              bstack1ll1l1l11l_opy_.quit()
            except Exception as e:
              logger.debug(bstack1ll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡴࡹ࡮ࡺࡴࡪࡰࡪࠤࡩࡸࡩࡷࡧࡵࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡩࡱࡲ࡯࠿ࠦࡻࡾࠩธ").format(str(e)))
      except Exception as e:
        logger.debug(bstack1ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡮࡯ࡰ࡭ࠣࡧࡱ࡫ࡡ࡯ࡷࡳࠤ࡫ࡵࡲࠡࡽࢀ࠾ࠥࢁࡽࠨน").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠬࡉࡲࡪࡶ࡬ࡧࡦࡲࠠࡦࡴࡵࡳࡷࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦࠢࡵࡹࡳࠦࡨࡰࡱ࡮ࠤࢀࢃ࠺ࠡࡽࢀࠫบ").format(name, str(e)))
    try:
      bstack111l111111_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack1ll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡳࡷ࡯ࡧࡪࡰࡤࡰࠥࡨࡥࡩࡣࡹࡩࠥ࡮࡯ࡰ࡭ࠣࡿࢂࡀࠠࡼࡿࠪป").format(name, str(e2)))
def bstack1l11lll11_opy_(config, startdir):
  return bstack1ll1l_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧผ").format(bstack1ll1l_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢฝ"))
notset = Notset()
def bstack1lll1l1l1l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack111l1l11ll_opy_
  if str(name).lower() == bstack1ll1l_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩพ"):
    return bstack1ll1l_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤฟ")
  else:
    return bstack111l1l11ll_opy_(self, name, default, skip)
def bstack11ll1lll1l_opy_(item, when):
  global bstack11l11l1lll_opy_
  try:
    bstack11l11l1lll_opy_(item, when)
  except Exception as e:
    pass
def bstack11llllll1l_opy_():
  return
def bstack11l11111l_opy_(type, name, status, reason, bstack1ll11l1111_opy_, bstack1ll111l11_opy_):
  bstack111llll1l1_opy_ = {
    bstack1ll1l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫภ"): type,
    bstack1ll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨม"): {}
  }
  if type == bstack1ll1l_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨย"):
    bstack111llll1l1_opy_[bstack1ll1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪร")][bstack1ll1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧฤ")] = bstack1ll11l1111_opy_
    bstack111llll1l1_opy_[bstack1ll1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬล")][bstack1ll1l_opy_ (u"ࠪࡨࡦࡺࡡࠨฦ")] = json.dumps(str(bstack1ll111l11_opy_))
  if type == bstack1ll1l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬว"):
    bstack111llll1l1_opy_[bstack1ll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨศ")][bstack1ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫษ")] = name
  if type == bstack1ll1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪส"):
    bstack111llll1l1_opy_[bstack1ll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫห")][bstack1ll1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩฬ")] = status
    if status == bstack1ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪอ"):
      bstack111llll1l1_opy_[bstack1ll1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧฮ")][bstack1ll1l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬฯ")] = json.dumps(str(reason))
  bstack1l1l1ll1ll_opy_ = bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫะ").format(json.dumps(bstack111llll1l1_opy_))
  return bstack1l1l1ll1ll_opy_
def bstack111lll1l1l_opy_(driver_command, response):
    if driver_command == bstack1ll1l_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫั"):
        bstack1lllll11_opy_.bstack1l1l1l1lll_opy_({
            bstack1ll1l_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧา"): response[bstack1ll1l_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨำ")],
            bstack1ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪิ"): bstack1lllll11_opy_.current_test_uuid()
        })
def bstack1l1ll1l1l1_opy_(item, call, rep):
  global bstack11lllllll1_opy_
  global bstack1lll1l111l_opy_
  global bstack111l11l1l1_opy_
  name = bstack1ll1l_opy_ (u"ࠫࠬี")
  try:
    if rep.when == bstack1ll1l_opy_ (u"ࠬࡩࡡ࡭࡮ࠪึ"):
      bstack111111111_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack111l11l1l1_opy_:
          name = str(rep.nodeid)
          bstack11111l1lll_opy_ = bstack11l11111l_opy_(bstack1ll1l_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧื"), name, bstack1ll1l_opy_ (u"ࠧࠨุ"), bstack1ll1l_opy_ (u"ࠨูࠩ"), bstack1ll1l_opy_ (u"ฺࠩࠪ"), bstack1ll1l_opy_ (u"ࠪࠫ฻"))
          threading.current_thread().bstack11l1l11lll_opy_ = name
          for driver in bstack1lll1l111l_opy_:
            if bstack111111111_opy_ == driver.session_id:
              driver.execute_script(bstack11111l1lll_opy_)
      except Exception as e:
        logger.debug(bstack1ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ฼").format(str(e)))
      try:
        bstack11lll1lll1_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1ll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭฽"):
          status = bstack1ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭฾") if rep.outcome.lower() == bstack1ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ฿") else bstack1ll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨเ")
          reason = bstack1ll1l_opy_ (u"ࠩࠪแ")
          if status == bstack1ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪโ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1ll1l_opy_ (u"ࠫ࡮ࡴࡦࡰࠩใ") if status == bstack1ll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬไ") else bstack1ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬๅ")
          data = name + bstack1ll1l_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩๆ") if status == bstack1ll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ็") else name + bstack1ll1l_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤ่ࠬ") + reason
          bstack1l1ll11l1_opy_ = bstack11l11111l_opy_(bstack1ll1l_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩ้ࠬ"), bstack1ll1l_opy_ (u"๊ࠫࠬ"), bstack1ll1l_opy_ (u"๋ࠬ࠭"), bstack1ll1l_opy_ (u"࠭ࠧ์"), level, data)
          for driver in bstack1lll1l111l_opy_:
            if bstack111111111_opy_ == driver.session_id:
              driver.execute_script(bstack1l1ll11l1_opy_)
      except Exception as e:
        logger.debug(bstack1ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫํ").format(str(e)))
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬ๎").format(str(e)))
  bstack11lllllll1_opy_(item, call, rep)
def bstack11ll111ll1_opy_(driver, bstack1ll11l111_opy_, test=None):
  global bstack1l1lllllll_opy_
  if test != None:
    bstack11ll11lll1_opy_ = getattr(test, bstack1ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ๏"), None)
    bstack11111lll1_opy_ = getattr(test, bstack1ll1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ๐"), None)
    PercySDK.screenshot(driver, bstack1ll11l111_opy_, bstack11ll11lll1_opy_=bstack11ll11lll1_opy_, bstack11111lll1_opy_=bstack11111lll1_opy_, bstack1111l1111l_opy_=bstack1l1lllllll_opy_)
  else:
    PercySDK.screenshot(driver, bstack1ll11l111_opy_)
@measure(event_name=EVENTS.bstack1111l11ll_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack1llll1l111_opy_(driver):
  if bstack11111l1l1_opy_.bstack11ll1111l_opy_() is True or bstack11111l1l1_opy_.capturing() is True:
    return
  bstack11111l1l1_opy_.bstack111lll1ll_opy_()
  while not bstack11111l1l1_opy_.bstack11ll1111l_opy_():
    bstack11l11l1ll_opy_ = bstack11111l1l1_opy_.bstack1lllllll1l_opy_()
    bstack11ll111ll1_opy_(driver, bstack11l11l1ll_opy_)
  bstack11111l1l1_opy_.bstack11l1lllll_opy_()
def bstack1l111lllll_opy_(sequence, driver_command, response = None, bstack1l1l11l1ll_opy_ = None, args = None):
    try:
      if sequence != bstack1ll1l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫ๑"):
        return
      if percy.bstack11llll11l_opy_() == bstack1ll1l_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦ๒"):
        return
      bstack11l11l1ll_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ๓"), None)
      for command in bstack1ll11ll1l1_opy_:
        if command == driver_command:
          with bstack1ll1l111l_opy_:
            bstack1111llll11_opy_ = bstack1lll1l111l_opy_.copy()
          for driver in bstack1111llll11_opy_:
            bstack1llll1l111_opy_(driver)
      bstack11l11l1ll1_opy_ = percy.bstack11lllll1ll_opy_()
      if driver_command in bstack1l11lll1l_opy_[bstack11l11l1ll1_opy_]:
        bstack11111l1l1_opy_.bstack11l1l111ll_opy_(bstack11l11l1ll_opy_, driver_command)
    except Exception as e:
      pass
def bstack1lll1lllll_opy_(framework_name):
  if bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ๔")):
      return
  bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬ๕"), True)
  global bstack1l1llllll_opy_
  global bstack11l1ll1lll_opy_
  global bstack1ll11llll1_opy_
  bstack1l1llllll_opy_ = framework_name
  logger.info(bstack1ll111111l_opy_.format(bstack1l1llllll_opy_.split(bstack1ll1l_opy_ (u"ࠩ࠰ࠫ๖"))[0]))
  bstack1l1l11111_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1llll1l1l1_opy_:
      Service.start = bstack11111lll1l_opy_
      Service.stop = bstack1lll11l1ll_opy_
      webdriver.Remote.get = bstack11l11llll_opy_
      WebDriver.quit = bstack11l111lll1_opy_
      webdriver.Remote.__init__ = bstack11l1lll11l_opy_
    if not bstack1llll1l1l1_opy_:
        webdriver.Remote.__init__ = bstack111l1lll11_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack1llll1lll1_opy_
    bstack11l1ll1lll_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1llll1l1l1_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack111111ll1_opy_
  except Exception as e:
    pass
  bstack111ll1l1ll_opy_()
  if not bstack11l1ll1lll_opy_:
    bstack1l111l1l1l_opy_(bstack1ll1l_opy_ (u"ࠥࡔࡦࡩ࡫ࡢࡩࡨࡷࠥࡴ࡯ࡵࠢ࡬ࡲࡸࡺࡡ࡭࡮ࡨࡨࠧ๗"), bstack111l1ll1l1_opy_)
  if bstack111lll1ll1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack1ll1l_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ๘")) and callable(getattr(RemoteConnection, bstack1ll1l_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭๙"))):
        RemoteConnection._get_proxy_url = bstack11ll1llll1_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack11ll1llll1_opy_
    except Exception as e:
      logger.error(bstack11ll11l1l1_opy_.format(str(e)))
  if bstack1lll1ll1ll_opy_():
    bstack1lll1ll11l_opy_(CONFIG, logger)
  if (bstack1ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ๚") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack11llll11l_opy_() == bstack1ll1l_opy_ (u"ࠢࡵࡴࡸࡩࠧ๛"):
          bstack1llllll11l_opy_(bstack1l111lllll_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack11lll11l1_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack11l1l1l111_opy_
      except Exception as e:
        logger.warn(bstack1l1111ll1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack111l1l1lll_opy_
      except Exception as e:
        logger.debug(bstack111ll11l1_opy_ + str(e))
    except Exception as e:
      bstack1l111l1l1l_opy_(e, bstack1l1111ll1_opy_)
    Output.start_test = bstack1l1l1l11l1_opy_
    Output.end_test = bstack111l1111l_opy_
    TestStatus.__init__ = bstack111ll1ll1l_opy_
    QueueItem.__init__ = bstack1111ll1ll1_opy_
    pabot._create_items = bstack1111ll11l_opy_
    try:
      from pabot import __version__ as bstack111l1ll1l_opy_
      if version.parse(bstack111l1ll1l_opy_) >= version.parse(bstack1ll1l_opy_ (u"ࠨ࠷࠱࠴࠳࠶ࠧ๜")):
        pabot._run = bstack111ll1l1l1_opy_
      elif version.parse(bstack111l1ll1l_opy_) >= version.parse(bstack1ll1l_opy_ (u"ࠩ࠷࠲࠷࠴࠰ࠨ๝")):
        pabot._run = bstack11ll1l1l1_opy_
      elif version.parse(bstack111l1ll1l_opy_) >= version.parse(bstack1ll1l_opy_ (u"ࠪ࠶࠳࠷࠵࠯࠲ࠪ๞")):
        pabot._run = bstack1111ll11ll_opy_
      elif version.parse(bstack111l1ll1l_opy_) >= version.parse(bstack1ll1l_opy_ (u"ࠫ࠷࠴࠱࠴࠰࠳ࠫ๟")):
        pabot._run = bstack1l1l11l11l_opy_
      else:
        pabot._run = bstack11l111l11_opy_
    except Exception as e:
      pabot._run = bstack11l111l11_opy_
    pabot._create_command_for_execution = bstack11l111l111_opy_
    pabot._report_results = bstack1l1l11l111_opy_
  if bstack1ll1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ๠") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l111l1l1l_opy_(e, bstack1ll111ll1l_opy_)
    Runner.run_hook = bstack1l111l1lll_opy_
    Step.run = bstack1lll1111l1_opy_
  if bstack1ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭๡") in str(framework_name).lower():
    if not bstack1llll1l1l1_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1l11lll11_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack11llllll1l_opy_
      Config.getoption = bstack1lll1l1l1l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1l1ll1l1l1_opy_
    except Exception as e:
      pass
def bstack1l1l11lll1_opy_():
  global CONFIG
  if bstack1ll1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ๢") in CONFIG and int(CONFIG[bstack1ll1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ๣")]) > 1:
    logger.warn(bstack11l1lllll1_opy_)
def bstack1l111l111l_opy_(arg, bstack1111111l_opy_, bstack111l11lll1_opy_=None):
  global CONFIG
  global bstack111ll11l1l_opy_
  global bstack11lll11l1l_opy_
  global bstack1llll1l1l1_opy_
  global bstack111111ll_opy_
  bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ๤")
  if bstack1111111l_opy_ and isinstance(bstack1111111l_opy_, str):
    bstack1111111l_opy_ = eval(bstack1111111l_opy_)
  CONFIG = bstack1111111l_opy_[bstack1ll1l_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪ๥")]
  bstack111ll11l1l_opy_ = bstack1111111l_opy_[bstack1ll1l_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬ๦")]
  bstack11lll11l1l_opy_ = bstack1111111l_opy_[bstack1ll1l_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ๧")]
  bstack1llll1l1l1_opy_ = bstack1111111l_opy_[bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩ๨")]
  bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ๩"), bstack1llll1l1l1_opy_)
  os.environ[bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ๪")] = bstack1111l1l11l_opy_
  os.environ[bstack1ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠨ๫")] = json.dumps(CONFIG)
  os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡋ࡙ࡇࡥࡕࡓࡎࠪ๬")] = bstack111ll11l1l_opy_
  os.environ[bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ๭")] = str(bstack11lll11l1l_opy_)
  os.environ[bstack1ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫ๮")] = str(True)
  if bstack1l111lll11_opy_(arg, [bstack1ll1l_opy_ (u"࠭࠭࡯ࠩ๯"), bstack1ll1l_opy_ (u"ࠧ࠮࠯ࡱࡹࡲࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ๰")]) != -1:
    os.environ[bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡃࡕࡅࡑࡒࡅࡍࠩ๱")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1lll1l1lll_opy_)
    return
  bstack1ll1lll1l_opy_()
  global bstack1ll11lll11_opy_
  global bstack1l1lllllll_opy_
  global bstack1l1lllll11_opy_
  global bstack111l1ll111_opy_
  global bstack1l1l1l11ll_opy_
  global bstack1ll11llll1_opy_
  global bstack11lllllll_opy_
  arg.append(bstack1ll1l_opy_ (u"ࠤ࠰࡛ࠧ๲"))
  arg.append(bstack1ll1l_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧ࠽ࡑࡴࡪࡵ࡭ࡧࠣࡥࡱࡸࡥࡢࡦࡼࠤ࡮ࡳࡰࡰࡴࡷࡩࡩࡀࡰࡺࡶࡨࡷࡹ࠴ࡐࡺࡶࡨࡷࡹ࡝ࡡࡳࡰ࡬ࡲ࡬ࠨ๳"))
  arg.append(bstack1ll1l_opy_ (u"ࠦ࠲࡝ࠢ๴"))
  arg.append(bstack1ll1l_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩ࠿࡚ࡨࡦࠢ࡫ࡳࡴࡱࡩ࡮ࡲ࡯ࠦ๵"))
  global bstack111lll11ll_opy_
  global bstack1l1ll1ll11_opy_
  global bstack1ll1llllll_opy_
  global bstack11l11l11ll_opy_
  global bstack1l11l1111l_opy_
  global bstack1l11lll11l_opy_
  global bstack1l11lll1ll_opy_
  global bstack1l1l11l1l1_opy_
  global bstack11l111ll1_opy_
  global bstack11l111ll11_opy_
  global bstack111l1l11ll_opy_
  global bstack11l11l1lll_opy_
  global bstack11lllllll1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack111lll11ll_opy_ = webdriver.Remote.__init__
    bstack1l1ll1ll11_opy_ = WebDriver.quit
    bstack1l1l11l1l1_opy_ = WebDriver.close
    bstack11l111ll1_opy_ = WebDriver.get
    bstack1ll1llllll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1l1llll111_opy_(CONFIG) and bstack111lll111_opy_():
    if bstack111lllll1_opy_() < version.parse(bstack1llll111l1_opy_):
      logger.error(bstack1ll1l111ll_opy_.format(bstack111lllll1_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1ll1l_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ๶")) and callable(getattr(RemoteConnection, bstack1ll1l_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ๷"))):
          bstack11l111ll11_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack11l111ll11_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack11ll11l1l1_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack111l1l11ll_opy_ = Config.getoption
    from _pytest import runner
    bstack11l11l1lll_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack11l111ll_opy_)
  try:
    from pytest_bdd import reporting
    bstack11lllllll1_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1ll1l_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩ๸"))
  bstack1l1lllll11_opy_ = CONFIG.get(bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭๹"), {}).get(bstack1ll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ๺"))
  bstack11lllllll_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack11l111l1ll_opy_():
      bstack1l1lll11l1_opy_.invoke(Events.CONNECT, bstack1ll1lll1l1_opy_())
    platform_index = int(os.environ.get(bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫ๻"), bstack1ll1l_opy_ (u"ࠬ࠶ࠧ๼")))
  else:
    bstack1lll1lllll_opy_(bstack11l1ll1ll_opy_)
  os.environ[bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧ๽")] = CONFIG[bstack1ll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ๾")]
  os.environ[bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫ๿")] = CONFIG[bstack1ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ຀")]
  os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ກ")] = bstack1llll1l1l1_opy_.__str__()
  from _pytest.config import main as bstack111l1111ll_opy_
  bstack1l11ll11l1_opy_ = []
  try:
    exit_code = bstack111l1111ll_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack111llll11_opy_()
    if bstack1ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨຂ") in multiprocessing.current_process().__dict__.keys():
      for bstack1l1ll11l11_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l11ll11l1_opy_.append(bstack1l1ll11l11_opy_)
    try:
      bstack1ll11l1l11_opy_ = (bstack1l11ll11l1_opy_, int(exit_code))
      bstack111l11lll1_opy_.append(bstack1ll11l1l11_opy_)
    except:
      bstack111l11lll1_opy_.append((bstack1l11ll11l1_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1l11ll11l1_opy_.append({bstack1ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ຃"): bstack1ll1l_opy_ (u"࠭ࡐࡳࡱࡦࡩࡸࡹࠠࠨຄ") + os.environ.get(bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ຅")), bstack1ll1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧຆ"): traceback.format_exc(), bstack1ll1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨງ"): int(os.environ.get(bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪຈ")))})
    bstack111l11lll1_opy_.append((bstack1l11ll11l1_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack1ll1l_opy_ (u"ࠦࡷ࡫ࡴࡳ࡫ࡨࡷࠧຉ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack11ll1l111_opy_ = e.__class__.__name__
    print(bstack1ll1l_opy_ (u"ࠧࠫࡳ࠻ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡥࡩ࡭ࡧࡶࡦࠢࡷࡩࡸࡺࠠࠦࡵࠥຊ") % (bstack11ll1l111_opy_, e))
    return 1
def bstack11lll1111_opy_(arg):
  global bstack11l11ll111_opy_
  bstack1lll1lllll_opy_(bstack1l1l11lll_opy_)
  os.environ[bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ຋")] = str(bstack11lll11l1l_opy_)
  retries = bstack11111l1l_opy_.bstack11l11l11_opy_(CONFIG)
  status_code = 0
  if bstack11111l1l_opy_.bstack1111ll1l_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack11lll1l1l_opy_
    status_code = bstack11lll1l1l_opy_(arg)
  if status_code != 0:
    bstack11l11ll111_opy_ = status_code
def bstack11l11l1l1l_opy_():
  logger.info(bstack1l11ll1ll1_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1ll1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ຌ"), help=bstack1ll1l_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡦࡳࡳ࡬ࡩࡨࠩຍ"))
  parser.add_argument(bstack1ll1l_opy_ (u"ࠩ࠰ࡹࠬຎ"), bstack1ll1l_opy_ (u"ࠪ࠱࠲ࡻࡳࡦࡴࡱࡥࡲ࡫ࠧຏ"), help=bstack1ll1l_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡷࡶࡩࡷࡴࡡ࡮ࡧࠪຐ"))
  parser.add_argument(bstack1ll1l_opy_ (u"ࠬ࠳࡫ࠨຑ"), bstack1ll1l_opy_ (u"࠭࠭࠮࡭ࡨࡽࠬຒ"), help=bstack1ll1l_opy_ (u"࡚ࠧࡱࡸࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡦࡩࡣࡦࡵࡶࠤࡰ࡫ࡹࠨຓ"))
  parser.add_argument(bstack1ll1l_opy_ (u"ࠨ࠯ࡩࠫດ"), bstack1ll1l_opy_ (u"ࠩ࠰࠱࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧຕ"), help=bstack1ll1l_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩຖ"))
  bstack1ll11l11l_opy_ = parser.parse_args()
  try:
    bstack1lll1llll1_opy_ = bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡫ࡪࡴࡥࡳ࡫ࡦ࠲ࡾࡳ࡬࠯ࡵࡤࡱࡵࡲࡥࠨທ")
    if bstack1ll11l11l_opy_.framework and bstack1ll11l11l_opy_.framework not in (bstack1ll1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬຘ"), bstack1ll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧນ")):
      bstack1lll1llll1_opy_ = bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭ບ")
    bstack1lll11l1l1_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1lll1llll1_opy_)
    bstack11ll111111_opy_ = open(bstack1lll11l1l1_opy_, bstack1ll1l_opy_ (u"ࠨࡴࠪປ"))
    bstack1llll11ll1_opy_ = bstack11ll111111_opy_.read()
    bstack11ll111111_opy_.close()
    if bstack1ll11l11l_opy_.username:
      bstack1llll11ll1_opy_ = bstack1llll11ll1_opy_.replace(bstack1ll1l_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩຜ"), bstack1ll11l11l_opy_.username)
    if bstack1ll11l11l_opy_.key:
      bstack1llll11ll1_opy_ = bstack1llll11ll1_opy_.replace(bstack1ll1l_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬຝ"), bstack1ll11l11l_opy_.key)
    if bstack1ll11l11l_opy_.framework:
      bstack1llll11ll1_opy_ = bstack1llll11ll1_opy_.replace(bstack1ll1l_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬພ"), bstack1ll11l11l_opy_.framework)
    file_name = bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨຟ")
    file_path = os.path.abspath(file_name)
    bstack11l11ll1l1_opy_ = open(file_path, bstack1ll1l_opy_ (u"࠭ࡷࠨຠ"))
    bstack11l11ll1l1_opy_.write(bstack1llll11ll1_opy_)
    bstack11l11ll1l1_opy_.close()
    logger.info(bstack1ll111lll1_opy_)
    try:
      os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩມ")] = bstack1ll11l11l_opy_.framework if bstack1ll11l11l_opy_.framework != None else bstack1ll1l_opy_ (u"ࠣࠤຢ")
      config = yaml.safe_load(bstack1llll11ll1_opy_)
      config[bstack1ll1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩຣ")] = bstack1ll1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠰ࡷࡪࡺࡵࡱࠩ຤")
      bstack111lll1111_opy_(bstack11l1l1ll1_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll11llll_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack11lll11ll1_opy_.format(str(e)))
def bstack111lll1111_opy_(bstack11llll1ll1_opy_, config, bstack1ll1l1ll11_opy_={}):
  global bstack1llll1l1l1_opy_
  global bstack1lll11lll1_opy_
  global bstack111111ll_opy_
  if not config:
    return
  bstack11lll11111_opy_ = bstack11l1l1l1ll_opy_ if not bstack1llll1l1l1_opy_ else (
    bstack1111l1l1l_opy_ if bstack1ll1l_opy_ (u"ࠫࡦࡶࡰࠨລ") in config else (
        bstack1ll1l1l1ll_opy_ if config.get(bstack1ll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ຦")) else bstack11l1lll1l_opy_
    )
)
  bstack1l111ll1l1_opy_ = False
  bstack1l1ll1l1l_opy_ = False
  if bstack1llll1l1l1_opy_ is True:
      if bstack1ll1l_opy_ (u"࠭ࡡࡱࡲࠪວ") in config:
          bstack1l111ll1l1_opy_ = True
      else:
          bstack1l1ll1l1l_opy_ = True
  bstack11ll1ll11l_opy_ = bstack1l11lll111_opy_.bstack111l111ll_opy_(config, bstack1lll11lll1_opy_)
  bstack1llll11111_opy_ = bstack1l1ll1l11_opy_()
  data = {
    bstack1ll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩຨ"): config[bstack1ll1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪຩ")],
    bstack1ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬສ"): config[bstack1ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ຫ")],
    bstack1ll1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨຬ"): bstack11llll1ll1_opy_,
    bstack1ll1l_opy_ (u"ࠬࡪࡥࡵࡧࡦࡸࡪࡪࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩອ"): os.environ.get(bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨຮ"), bstack1lll11lll1_opy_),
    bstack1ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩຯ"): bstack111l11lll_opy_,
    bstack1ll1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮ࠪະ"): bstack11ll1l1ll1_opy_(),
    bstack1ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬັ"): {
      bstack1ll1l_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨາ"): str(config[bstack1ll1l_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫຳ")]) if bstack1ll1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬິ") in config else bstack1ll1l_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢີ"),
      bstack1ll1l_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࡘࡨࡶࡸ࡯࡯࡯ࠩຶ"): sys.version,
      bstack1ll1l_opy_ (u"ࠨࡴࡨࡪࡪࡸࡲࡦࡴࠪື"): bstack1l1ll11ll_opy_(os.environ.get(bstack1ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎຸࠫ"), bstack1lll11lll1_opy_)),
      bstack1ll1l_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩູࠬ"): bstack1ll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ຺ࠫ"),
      bstack1ll1l_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ົ"): bstack11lll11111_opy_,
      bstack1ll1l_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫຼ"): bstack11ll1ll11l_opy_,
      bstack1ll1l_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡠࡷࡸ࡭ࡩ࠭ຽ"): os.environ[bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭຾")],
      bstack1ll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ຿"): os.environ.get(bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬເ"), bstack1lll11lll1_opy_),
      bstack1ll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧແ"): bstack1l111lll1l_opy_(os.environ.get(bstack1ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧໂ"), bstack1lll11lll1_opy_)),
      bstack1ll1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬໃ"): bstack1llll11111_opy_.get(bstack1ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬໄ")),
      bstack1ll1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ໅"): bstack1llll11111_opy_.get(bstack1ll1l_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪໆ")),
      bstack1ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໇"): config[bstack1ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫່ࠧ")] if config[bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ້")] else bstack1ll1l_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴ໊ࠢ"),
      bstack1ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳ໋ࠩ"): str(config[bstack1ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໌")]) if bstack1ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫໍ") in config else bstack1ll1l_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦ໎"),
      bstack1ll1l_opy_ (u"ࠫࡴࡹࠧ໏"): sys.platform,
      bstack1ll1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧ໐"): socket.gethostname(),
      bstack1ll1l_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ໑"): bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ໒"))
    }
  }
  if not bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ໓")) is None:
    data[bstack1ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໔")][bstack1ll1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡒ࡫ࡴࡢࡦࡤࡸࡦ࠭໕")] = {
      bstack1ll1l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ໖"): bstack1ll1l_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪ໗"),
      bstack1ll1l_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭໘"): bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ໙")),
      bstack1ll1l_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࡏࡷࡰࡦࡪࡸࠧ໚"): bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡑࡳࠬ໛"))
    }
  if bstack11llll1ll1_opy_ == bstack1l1l11ll11_opy_:
    data[bstack1ll1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭ໜ")][bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡆࡳࡳ࡬ࡩࡨࠩໝ")] = bstack1l1l1ll111_opy_(config)
    data[bstack1ll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨໞ")][bstack1ll1l_opy_ (u"࠭ࡩࡴࡒࡨࡶࡨࡿࡁࡶࡶࡲࡉࡳࡧࡢ࡭ࡧࡧࠫໟ")] = percy.bstack11l1l11ll_opy_
    data[bstack1ll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ໠")][bstack1ll1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࡂࡶ࡫࡯ࡨࡎࡪࠧ໡")] = percy.percy_build_id
  if not bstack11111l1l_opy_.bstack11ll1ll11_opy_(CONFIG):
    data[bstack1ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໢")][bstack1ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠧ໣")] = bstack11111l1l_opy_.bstack11ll1ll11_opy_(CONFIG)
  bstack1111lll1_opy_ = bstack111lll11_opy_.bstack111l1ll1_opy_(CONFIG, logger)
  bstack1111llll_opy_ = bstack11111l1l_opy_.bstack111l1ll1_opy_(config=CONFIG)
  if bstack1111lll1_opy_ is not None and bstack1111llll_opy_ is not None and bstack1111llll_opy_.bstack11111ll1_opy_():
    data[bstack1ll1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ໤")][bstack1111llll_opy_.bstack1111lll11_opy_()] = bstack1111lll1_opy_.bstack11l1l1111_opy_()
  update(data[bstack1ll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ໥")], bstack1ll1l1ll11_opy_)
  try:
    response = bstack1l11lllll_opy_(bstack1ll1l_opy_ (u"࠭ࡐࡐࡕࡗࠫ໦"), bstack1ll1ll11ll_opy_(bstack11lll1l1ll_opy_), data, {
      bstack1ll1l_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ໧"): (config[bstack1ll1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ໨")], config[bstack1ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ໩")])
    })
    if response:
      logger.debug(bstack11111l1l11_opy_.format(bstack11llll1ll1_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11l111ll1l_opy_.format(str(e)))
def bstack1l1ll11ll_opy_(framework):
  return bstack1ll1l_opy_ (u"ࠥࡿࢂ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࢀࢃࠢ໪").format(str(framework), __version__) if framework else bstack1ll1l_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧ໫").format(
    __version__)
def bstack1ll1lll1l_opy_():
  global CONFIG
  global bstack1l11ll1lll_opy_
  if bool(CONFIG):
    return
  try:
    bstack11ll1ll1l1_opy_()
    logger.debug(bstack1l11l1lll1_opy_.format(str(CONFIG)))
    bstack1l11ll1lll_opy_ = bstack1ll1ll111_opy_.configure_logger(CONFIG, bstack1l11ll1lll_opy_)
    bstack1l1l11111_opy_()
  except Exception as e:
    logger.error(bstack1ll1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࠤ໬") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11l1lll111_opy_
  atexit.register(bstack1l1l1ll11_opy_)
  signal.signal(signal.SIGINT, bstack1llllll1ll_opy_)
  signal.signal(signal.SIGTERM, bstack1llllll1ll_opy_)
def bstack11l1lll111_opy_(exctype, value, traceback):
  global bstack1lll1l111l_opy_
  try:
    for driver in bstack1lll1l111l_opy_:
      bstack1ll11111l_opy_(driver, bstack1ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭໭"), bstack1ll1l_opy_ (u"ࠢࡔࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥ໮") + str(value))
  except Exception:
    pass
  logger.info(bstack11lllll11_opy_)
  bstack1l111l1l11_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l111l1l11_opy_(message=bstack1ll1l_opy_ (u"ࠨࠩ໯"), bstack111l11111_opy_ = False):
  global CONFIG
  bstack1111llllll_opy_ = bstack1ll1l_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡇࡻࡧࡪࡶࡴࡪࡱࡱࠫ໰") if bstack111l11111_opy_ else bstack1ll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ໱")
  try:
    if message:
      bstack1ll1l1ll11_opy_ = {
        bstack1111llllll_opy_ : str(message)
      }
      bstack111lll1111_opy_(bstack1l1l11ll11_opy_, CONFIG, bstack1ll1l1ll11_opy_)
    else:
      bstack111lll1111_opy_(bstack1l1l11ll11_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1111lll1l1_opy_.format(str(e)))
def bstack11l1ll1ll1_opy_(bstack1111l1111_opy_, size):
  bstack1ll111l1ll_opy_ = []
  while len(bstack1111l1111_opy_) > size:
    bstack1111lll111_opy_ = bstack1111l1111_opy_[:size]
    bstack1ll111l1ll_opy_.append(bstack1111lll111_opy_)
    bstack1111l1111_opy_ = bstack1111l1111_opy_[size:]
  bstack1ll111l1ll_opy_.append(bstack1111l1111_opy_)
  return bstack1ll111l1ll_opy_
def bstack1l111111l1_opy_(args):
  if bstack1ll1l_opy_ (u"ࠫ࠲ࡳࠧ໲") in args and bstack1ll1l_opy_ (u"ࠬࡶࡤࡣࠩ໳") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack11l11ll1l_opy_, stage=STAGE.bstack1ll1l1l1l1_opy_)
def run_on_browserstack(bstack1l1llll1l1_opy_=None, bstack111l11lll1_opy_=None, bstack11ll11111_opy_=False):
  global CONFIG
  global bstack111ll11l1l_opy_
  global bstack11lll11l1l_opy_
  global bstack1lll11lll1_opy_
  global bstack111111ll_opy_
  bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"࠭ࠧ໴")
  bstack1ll11lll1_opy_(bstack1l1ll11ll1_opy_, logger)
  if bstack1l1llll1l1_opy_ and isinstance(bstack1l1llll1l1_opy_, str):
    bstack1l1llll1l1_opy_ = eval(bstack1l1llll1l1_opy_)
  if bstack1l1llll1l1_opy_:
    CONFIG = bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧ໵")]
    bstack111ll11l1l_opy_ = bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩ໶")]
    bstack11lll11l1l_opy_ = bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ໷")]
    bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ໸"), bstack11lll11l1l_opy_)
    bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ໹")
  bstack111111ll_opy_.set_property(bstack1ll1l_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ໺"), uuid4().__str__())
  logger.info(bstack1ll1l_opy_ (u"࠭ࡓࡅࡍࠣࡶࡺࡴࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡩࡥ࠼ࠣࠫ໻") + bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ໼")));
  logger.debug(bstack1ll1l_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࡀࠫ໽") + bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ໾")))
  if not bstack11ll11111_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1lll1l1lll_opy_)
      return
    if sys.argv[1] == bstack1ll1l_opy_ (u"ࠪ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ࠭໿") or sys.argv[1] == bstack1ll1l_opy_ (u"ࠫ࠲ࡼࠧༀ"):
      logger.info(bstack1ll1l_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡕࡿࡴࡩࡱࡱࠤࡘࡊࡋࠡࡸࡾࢁࠬ༁").format(__version__))
      return
    if sys.argv[1] == bstack1ll1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ༂"):
      bstack11l11l1l1l_opy_()
      return
  args = sys.argv
  bstack1ll1lll1l_opy_()
  global bstack1ll11lll11_opy_
  global bstack11111ll1ll_opy_
  global bstack11lllllll_opy_
  global bstack1ll1l11ll1_opy_
  global bstack1l1lllllll_opy_
  global bstack1l1lllll11_opy_
  global bstack111l1ll111_opy_
  global bstack1l11l1ll1l_opy_
  global bstack1l1l1l11ll_opy_
  global bstack1ll11llll1_opy_
  global bstack111ll1lll_opy_
  bstack11111ll1ll_opy_ = len(CONFIG.get(bstack1ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ༃"), []))
  if not bstack1111l1l11l_opy_:
    if args[1] == bstack1ll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ༄") or args[1] == bstack1ll1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ༅"):
      bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༆")
      args = args[2:]
    elif args[1] == bstack1ll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༇"):
      bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༈")
      args = args[2:]
    elif args[1] == bstack1ll1l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ༉"):
      bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭༊")
      args = args[2:]
    elif args[1] == bstack1ll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ་"):
      bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ༌")
      args = args[2:]
    elif args[1] == bstack1ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ།"):
      bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༎")
      args = args[2:]
    elif args[1] == bstack1ll1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ༏"):
      bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭༐")
      args = args[2:]
    else:
      if not bstack1ll1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༑") in CONFIG or str(CONFIG[bstack1ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ༒")]).lower() in [bstack1ll1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༓"), bstack1ll1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫ༔")]:
        bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༕")
        args = args[1:]
      elif str(CONFIG[bstack1ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ༖")]).lower() == bstack1ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ༗"):
        bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ༘࠭")
        args = args[1:]
      elif str(CONFIG[bstack1ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮༙ࠫ")]).lower() == bstack1ll1l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༚"):
        bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ༛")
        args = args[1:]
      elif str(CONFIG[bstack1ll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ༜")]).lower() == bstack1ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ༝"):
        bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭༞")
        args = args[1:]
      elif str(CONFIG[bstack1ll1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༟")]).lower() == bstack1ll1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ༠"):
        bstack1111l1l11l_opy_ = bstack1ll1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ༡")
        args = args[1:]
      else:
        os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ༢")] = bstack1111l1l11l_opy_
        bstack1lllll1l11_opy_(bstack1l1ll1llll_opy_)
  os.environ[bstack1ll1l_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬ༣")] = bstack1111l1l11l_opy_
  bstack1lll11lll1_opy_ = bstack1111l1l11l_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1lll111ll_opy_ = bstack1l1l1lll1_opy_[bstack1ll1l_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘ࠲ࡈࡄࡅࠩ༤")] if bstack1111l1l11l_opy_ == bstack1ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭༥") and bstack111ll1llll_opy_() else bstack1111l1l11l_opy_
      bstack1l1lll11l1_opy_.invoke(Events.bstack11l1l1ll1l_opy_, bstack1111ll11l1_opy_(
        sdk_version=__version__,
        path_config=bstack1l11ll11l_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1lll111ll_opy_,
        frameworks=[bstack1lll111ll_opy_],
        framework_versions={
          bstack1lll111ll_opy_: bstack1l111lll1l_opy_(bstack1ll1l_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭༦") if bstack1111l1l11l_opy_ in [bstack1ll1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ༧"), bstack1ll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ༨"), bstack1ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ༩")] else bstack1111l1l11l_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack1ll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨ༪"), None):
        CONFIG[bstack1ll1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢ༫")] = cli.config.get(bstack1ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ༬"), None)
    except Exception as e:
      bstack1l1lll11l1_opy_.invoke(Events.bstack111l1ll11_opy_, e.__traceback__, 1)
    if bstack11lll11l1l_opy_:
      CONFIG[bstack1ll1l_opy_ (u"ࠢࡢࡲࡳࠦ༭")] = cli.config[bstack1ll1l_opy_ (u"ࠣࡣࡳࡴࠧ༮")]
      logger.info(bstack1ll1ll1111_opy_.format(CONFIG[bstack1ll1l_opy_ (u"ࠩࡤࡴࡵ࠭༯")]))
  else:
    bstack1l1lll11l1_opy_.clear()
  global bstack1l1l11l1l_opy_
  global bstack111lll11l_opy_
  if bstack1l1llll1l1_opy_:
    try:
      bstack1l11l11lll_opy_ = datetime.datetime.now()
      os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ༰")] = bstack1111l1l11l_opy_
      bstack111lll1111_opy_(bstack11l11l1111_opy_, CONFIG)
      cli.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡶࡨࡰࡥࡴࡦࡵࡷࡣࡦࡺࡴࡦ࡯ࡳࡸࡪࡪࠢ༱"), datetime.datetime.now() - bstack1l11l11lll_opy_)
    except Exception as e:
      logger.debug(bstack11l1ll11l_opy_.format(str(e)))
  global bstack111lll11ll_opy_
  global bstack1l1ll1ll11_opy_
  global bstack11l1l111l1_opy_
  global bstack1111l1lll_opy_
  global bstack11llll1111_opy_
  global bstack1l111l1ll1_opy_
  global bstack11l11l11ll_opy_
  global bstack1l11l1111l_opy_
  global bstack111ll11ll_opy_
  global bstack1l11lll11l_opy_
  global bstack1l11lll1ll_opy_
  global bstack1l1l11l1l1_opy_
  global bstack111l111111_opy_
  global bstack1ll11l11l1_opy_
  global bstack11l111ll1_opy_
  global bstack11l111ll11_opy_
  global bstack111l1l11ll_opy_
  global bstack11l11l1lll_opy_
  global bstack11l1111lll_opy_
  global bstack11lllllll1_opy_
  global bstack1ll1llllll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack111lll11ll_opy_ = webdriver.Remote.__init__
    bstack1l1ll1ll11_opy_ = WebDriver.quit
    bstack1l1l11l1l1_opy_ = WebDriver.close
    bstack11l111ll1_opy_ = WebDriver.get
    bstack1ll1llllll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1l1l11l1l_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack111lll111l_opy_
    bstack111lll11l_opy_ = bstack111lll111l_opy_()
  except Exception as e:
    pass
  try:
    global bstack11l1l11l1l_opy_
    from QWeb.keywords import browser
    bstack11l1l11l1l_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1l1llll111_opy_(CONFIG) and bstack111lll111_opy_():
    if bstack111lllll1_opy_() < version.parse(bstack1llll111l1_opy_):
      logger.error(bstack1ll1l111ll_opy_.format(bstack111lllll1_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1ll1l_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭༲")) and callable(getattr(RemoteConnection, bstack1ll1l_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ༳"))):
          RemoteConnection._get_proxy_url = bstack11ll1llll1_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack11ll1llll1_opy_
      except Exception as e:
        logger.error(bstack11ll11l1l1_opy_.format(str(e)))
  if not CONFIG.get(bstack1ll1l_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩ༴"), False) and not bstack1l1llll1l1_opy_:
    logger.info(bstack11l1l1l1l_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack1ll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩ༵ࠬ") in CONFIG and str(CONFIG[bstack1ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭༶")]).lower() != bstack1ll1l_opy_ (u"ࠪࡪࡦࡲࡳࡦ༷ࠩ"):
      bstack1lll1l11l1_opy_()
    elif bstack1111l1l11l_opy_ != bstack1ll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༸") or (bstack1111l1l11l_opy_ == bstack1ll1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ༹ࠬ") and not bstack1l1llll1l1_opy_):
      bstack11ll1lll11_opy_()
  if (bstack1111l1l11l_opy_ in [bstack1ll1l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ༺"), bstack1ll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭༻"), bstack1ll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ༼")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack11lll11l1_opy_
        bstack1l111l1ll1_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1l1111ll1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack11llll1111_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack111ll11l1_opy_ + str(e))
    except Exception as e:
      bstack1l111l1l1l_opy_(e, bstack1l1111ll1_opy_)
    if bstack1111l1l11l_opy_ != bstack1ll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ༽"):
      bstack11l1lll11_opy_()
    bstack11l1l111l1_opy_ = Output.start_test
    bstack1111l1lll_opy_ = Output.end_test
    bstack11l11l11ll_opy_ = TestStatus.__init__
    bstack111ll11ll_opy_ = pabot._run
    bstack1l11lll11l_opy_ = QueueItem.__init__
    bstack1l11lll1ll_opy_ = pabot._create_command_for_execution
    bstack11l1111lll_opy_ = pabot._report_results
  if bstack1111l1l11l_opy_ == bstack1ll1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ༾"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l111l1l1l_opy_(e, bstack1ll111ll1l_opy_)
    bstack111l111111_opy_ = Runner.run_hook
    bstack1ll11l11l1_opy_ = Step.run
  if bstack1111l1l11l_opy_ == bstack1ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༿"):
    try:
      from _pytest.config import Config
      bstack111l1l11ll_opy_ = Config.getoption
      from _pytest import runner
      bstack11l11l1lll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack11l111ll_opy_)
    try:
      from pytest_bdd import reporting
      bstack11lllllll1_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1ll1l_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡴࠦࡲࡶࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࡸ࠭ཀ"))
  try:
    framework_name = bstack1ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬཁ") if bstack1111l1l11l_opy_ in [bstack1ll1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ག"), bstack1ll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧགྷ"), bstack1ll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪང")] else bstack1ll1l1111_opy_(bstack1111l1l11l_opy_)
    bstack1lll11ll1l_opy_ = {
      bstack1ll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࠫཅ"): bstack1ll1l_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭ཆ") if bstack1111l1l11l_opy_ == bstack1ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཇ") and bstack111ll1llll_opy_() else framework_name,
      bstack1ll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ཈"): bstack1l111lll1l_opy_(framework_name),
      bstack1ll1l_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬཉ"): __version__,
      bstack1ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩཊ"): bstack1111l1l11l_opy_
    }
    if bstack1111l1l11l_opy_ in bstack1lll11ll1_opy_ + bstack11l11llll1_opy_:
      if bstack1lllllll1_opy_.bstack111ll11ll1_opy_(CONFIG):
        if bstack1ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩཋ") in CONFIG:
          os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫཌ")] = os.getenv(bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬཌྷ"), json.dumps(CONFIG[bstack1ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬཎ")]))
          CONFIG[bstack1ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ཏ")].pop(bstack1ll1l_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬཐ"), None)
          CONFIG[bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨད")].pop(bstack1ll1l_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧདྷ"), None)
        bstack1lll11ll1l_opy_[bstack1ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪན")] = {
          bstack1ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩཔ"): bstack1ll1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧཕ"),
          bstack1ll1l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧབ"): str(bstack111lllll1_opy_())
        }
    if bstack1111l1l11l_opy_ not in [bstack1ll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨབྷ")] and not cli.is_running():
      bstack1l1ll1l1ll_opy_, bstack1ll1l1lll_opy_ = bstack1lllll11_opy_.launch(CONFIG, bstack1lll11ll1l_opy_)
      if bstack1ll1l1lll_opy_.get(bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨམ")) is not None and bstack1lllllll1_opy_.bstack11l11lll1_opy_(CONFIG) is None:
        value = bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩཙ")].get(bstack1ll1l_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫཚ"))
        if value is not None:
            CONFIG[bstack1ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫཛ")] = value
        else:
          logger.debug(bstack1ll1l_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡦࡤࡸࡦࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥཛྷ"))
  except Exception as e:
    logger.debug(bstack1l1l1111l_opy_.format(bstack1ll1l_opy_ (u"࠭ࡔࡦࡵࡷࡌࡺࡨࠧཝ"), str(e)))
  if bstack1111l1l11l_opy_ == bstack1ll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧཞ"):
    bstack11lllllll_opy_ = True
    if bstack1l1llll1l1_opy_ and bstack11ll11111_opy_:
      bstack1l1lllll11_opy_ = CONFIG.get(bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬཟ"), {}).get(bstack1ll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫའ"))
      bstack1lll1lllll_opy_(bstack1lll1ll1l1_opy_)
    elif bstack1l1llll1l1_opy_:
      bstack1l1lllll11_opy_ = CONFIG.get(bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧཡ"), {}).get(bstack1ll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ར"))
      global bstack1lll1l111l_opy_
      try:
        if bstack1l111111l1_opy_(bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨལ")]) and multiprocessing.current_process().name == bstack1ll1l_opy_ (u"࠭࠰ࠨཤ"):
          bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪཥ")].remove(bstack1ll1l_opy_ (u"ࠨ࠯ࡰࠫས"))
          bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬཧ")].remove(bstack1ll1l_opy_ (u"ࠪࡴࡩࡨࠧཨ"))
          bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཀྵ")] = bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཪ")][0]
          with open(bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩཫ")], bstack1ll1l_opy_ (u"ࠧࡳࠩཬ")) as f:
            file_content = f.read()
          bstack111ll1l11_opy_ = bstack1ll1l_opy_ (u"ࠣࠤࠥࡪࡷࡵ࡭ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡦ࡮ࠤ࡮ࡳࡰࡰࡴࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫࠻ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨࠬࢀࢃࠩ࠼ࠢࡩࡶࡴࡳࠠࡱࡦࡥࠤ࡮ࡳࡰࡰࡴࡷࠤࡕࡪࡢ࠼ࠢࡲ࡫ࡤࡪࡢࠡ࠿ࠣࡔࡩࡨ࠮ࡥࡱࡢࡦࡷ࡫ࡡ࡬࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡤࡦࡨࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰ࠮ࡳࡦ࡮ࡩ࠰ࠥࡧࡲࡨ࠮ࠣࡸࡪࡳࡰࡰࡴࡤࡶࡾࠦ࠽ࠡ࠲ࠬ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡸࡷࡿ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡣࡵ࡫ࠥࡃࠠࡴࡶࡵࠬ࡮ࡴࡴࠩࡣࡵ࡫࠮࠱࠱࠱ࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡧࡻࡧࡪࡶࡴࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡦࡹࠠࡦ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡴࡦࡹࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡯ࡨࡡࡧࡦ࠭ࡹࡥ࡭ࡨ࠯ࡥࡷ࡭ࠬࡵࡧࡰࡴࡴࡸࡡࡳࡻࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡑࡦࡥ࠲ࡩࡵ࡟ࡣࠢࡀࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡔࡩࡨ࠮ࡥࡱࡢࡦࡷ࡫ࡡ࡬ࠢࡀࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡔࡩࡨࠨࠪ࠰ࡶࡩࡹࡥࡴࡳࡣࡦࡩ࠭࠯࡜࡯ࠤࠥࠦ཭").format(str(bstack1l1llll1l1_opy_))
          bstack1l1l111111_opy_ = bstack111ll1l11_opy_ + file_content
          bstack11ll1l1l11_opy_ = bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ཮")] + bstack1ll1l_opy_ (u"ࠪࡣࡧࡹࡴࡢࡥ࡮ࡣࡹ࡫࡭ࡱ࠰ࡳࡽࠬ཯")
          with open(bstack11ll1l1l11_opy_, bstack1ll1l_opy_ (u"ࠫࡼ࠭཰")):
            pass
          with open(bstack11ll1l1l11_opy_, bstack1ll1l_opy_ (u"ࠧࡽཱࠫࠣ")) as f:
            f.write(bstack1l1l111111_opy_)
          import subprocess
          process_data = subprocess.run([bstack1ll1l_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࠨི"), bstack11ll1l1l11_opy_])
          if os.path.exists(bstack11ll1l1l11_opy_):
            os.unlink(bstack11ll1l1l11_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack1l111111l1_opy_(bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧཱིࠪ")]):
            bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨུࠫ")].remove(bstack1ll1l_opy_ (u"ࠩ࠰ࡱཱུࠬ"))
            bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྲྀ")].remove(bstack1ll1l_opy_ (u"ࠫࡵࡪࡢࠨཷ"))
            bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨླྀ")] = bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩཹ")][0]
          bstack1lll1lllll_opy_(bstack1lll1ll1l1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧེࠪ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1ll1l_opy_ (u"ࠨࡡࡢࡲࡦࡳࡥࡠࡡཻࠪ")] = bstack1ll1l_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢོࠫ")
          mod_globals[bstack1ll1l_opy_ (u"ࠪࡣࡤ࡬ࡩ࡭ࡧࡢࡣཽࠬ")] = os.path.abspath(bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཾ")])
          exec(open(bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཿ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1ll1l_opy_ (u"࠭ࡃࡢࡷࡪ࡬ࡹࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂྀ࠭").format(str(e)))
          for driver in bstack1lll1l111l_opy_:
            bstack111l11lll1_opy_.append({
              bstack1ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩཱྀࠬ"): bstack1l1llll1l1_opy_[bstack1ll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྂ")],
              bstack1ll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨྃ"): str(e),
              bstack1ll1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹ྄ࠩ"): multiprocessing.current_process().name
            })
            bstack1ll11111l_opy_(driver, bstack1ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ྅"), bstack1ll1l_opy_ (u"࡙ࠧࡥࡴࡵ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣ྆") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1lll1l111l_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11lll11l1l_opy_, CONFIG, logger)
      bstack1lll1111ll_opy_()
      bstack1l1l11lll1_opy_()
      percy.bstack1ll1111l1l_opy_()
      bstack1111111l_opy_ = {
        bstack1ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ྇"): args[0],
        bstack1ll1l_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧྈ"): CONFIG,
        bstack1ll1l_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩྉ"): bstack111ll11l1l_opy_,
        bstack1ll1l_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫྊ"): bstack11lll11l1l_opy_
      }
      if bstack1ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྋ") in CONFIG:
        bstack111l1lllll_opy_ = bstack1l11ll1l11_opy_(args, logger, CONFIG, bstack1llll1l1l1_opy_, bstack11111ll1ll_opy_)
        bstack1l11l1ll1l_opy_ = bstack111l1lllll_opy_.bstack1llll1lll_opy_(run_on_browserstack, bstack1111111l_opy_, bstack1l111111l1_opy_(args))
      else:
        if bstack1l111111l1_opy_(args):
          bstack1111111l_opy_[bstack1ll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྌ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1111111l_opy_,))
          test.start()
          test.join()
        else:
          bstack1lll1lllll_opy_(bstack1lll1ll1l1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1ll1l_opy_ (u"ࠬࡥ࡟࡯ࡣࡰࡩࡤࡥࠧྍ")] = bstack1ll1l_opy_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨྎ")
          mod_globals[bstack1ll1l_opy_ (u"ࠧࡠࡡࡩ࡭ࡱ࡫࡟ࡠࠩྏ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1111l1l11l_opy_ == bstack1ll1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧྐ") or bstack1111l1l11l_opy_ == bstack1ll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨྑ"):
    percy.init(bstack11lll11l1l_opy_, CONFIG, logger)
    percy.bstack1ll1111l1l_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l111l1l1l_opy_(e, bstack1l1111ll1_opy_)
    bstack1lll1111ll_opy_()
    bstack1lll1lllll_opy_(bstack1l1111ll1l_opy_)
    if bstack1llll1l1l1_opy_:
      bstack11111111l_opy_(bstack1l1111ll1l_opy_, args)
      if bstack1ll1l_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨྒ") in args:
        i = args.index(bstack1ll1l_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩྒྷ"))
        args.pop(i)
        args.pop(i)
      if bstack1ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨྔ") not in CONFIG:
        CONFIG[bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩྕ")] = [{}]
        bstack11111ll1ll_opy_ = 1
      if bstack1ll11lll11_opy_ == 0:
        bstack1ll11lll11_opy_ = 1
      args.insert(0, str(bstack1ll11lll11_opy_))
      args.insert(0, str(bstack1ll1l_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬྖ")))
    if bstack1lllll11_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack11ll1ll111_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack11l1ll111_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1ll1l_opy_ (u"ࠣࡔࡒࡆࡔ࡚࡟ࡐࡒࡗࡍࡔࡔࡓࠣྗ"),
        ).parse_args(bstack11ll1ll111_opy_)
        bstack11l11lll1l_opy_ = args.index(bstack11ll1ll111_opy_[0]) if len(bstack11ll1ll111_opy_) > 0 else len(args)
        args.insert(bstack11l11lll1l_opy_, str(bstack1ll1l_opy_ (u"ࠩ࠰࠱ࡱ࡯ࡳࡵࡧࡱࡩࡷ࠭྘")))
        args.insert(bstack11l11lll1l_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡶࡴࡨ࡯ࡵࡡ࡯࡭ࡸࡺࡥ࡯ࡧࡵ࠲ࡵࡿࠧྙ"))))
        if bstack11111l1l_opy_.bstack1111ll1l_opy_(CONFIG):
          args.insert(bstack11l11lll1l_opy_, str(bstack1ll1l_opy_ (u"ࠫ࠲࠳࡬ࡪࡵࡷࡩࡳ࡫ࡲࠨྚ")))
          args.insert(bstack11l11lll1l_opy_ + 1, str(bstack1ll1l_opy_ (u"ࠬࡘࡥࡵࡴࡼࡊࡦ࡯࡬ࡦࡦ࠽ࡿࢂ࠭ྛ").format(bstack11111l1l_opy_.bstack11l11l11_opy_(CONFIG))))
        if bstack1lll1ll111_opy_(os.environ.get(bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠫྜ"))) and str(os.environ.get(bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠫྜྷ"), bstack1ll1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭ྞ"))) != bstack1ll1l_opy_ (u"ࠩࡱࡹࡱࡲࠧྟ"):
          for bstack11111l1l1l_opy_ in bstack11l1ll111_opy_:
            args.remove(bstack11111l1l1l_opy_)
          test_files = os.environ.get(bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧྠ")).split(bstack1ll1l_opy_ (u"ࠫ࠱࠭ྡ"))
          for bstack1111l111_opy_ in test_files:
            args.append(bstack1111l111_opy_)
      except Exception as e:
        logger.error(bstack1ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡥࡹࡺࡡࡤࡪ࡬ࡲ࡬ࠦ࡬ࡪࡵࡷࡩࡳ࡫ࡲࠡࡨࡲࡶࠥࢁࡽ࠯ࠢࡈࡶࡷࡵࡲࠡ࠯ࠣࡿࢂࠨྡྷ").format(bstack1l11l11ll1_opy_, e))
    pabot.main(args)
  elif bstack1111l1l11l_opy_ == bstack1ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧྣ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l111l1l1l_opy_(e, bstack1l1111ll1_opy_)
    for a in args:
      if bstack1ll1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭ྤ") in a:
        bstack1l1lllllll_opy_ = int(a.split(bstack1ll1l_opy_ (u"ࠨ࠼ࠪྥ"))[1])
      if bstack1ll1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ྦ") in a:
        bstack1l1lllll11_opy_ = str(a.split(bstack1ll1l_opy_ (u"ࠪ࠾ࠬྦྷ"))[1])
      if bstack1ll1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫྨ") in a:
        bstack111l1ll111_opy_ = str(a.split(bstack1ll1l_opy_ (u"ࠬࡀࠧྩ"))[1])
    bstack11l1l1lll_opy_ = None
    if bstack1ll1l_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬྪ") in args:
      i = args.index(bstack1ll1l_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭ྫ"))
      args.pop(i)
      bstack11l1l1lll_opy_ = args.pop(i)
    if bstack11l1l1lll_opy_ is not None:
      global bstack1ll1ll1ll1_opy_
      bstack1ll1ll1ll1_opy_ = bstack11l1l1lll_opy_
    bstack1lll1lllll_opy_(bstack1l1111ll1l_opy_)
    run_cli(args)
    if bstack1ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬྫྷ") in multiprocessing.current_process().__dict__.keys():
      for bstack1l1ll11l11_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack111l11lll1_opy_.append(bstack1l1ll11l11_opy_)
  elif bstack1111l1l11l_opy_ == bstack1ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩྭ"):
    bstack11l1ll1l11_opy_ = bstack111l1l11_opy_(args, logger, CONFIG, bstack1llll1l1l1_opy_)
    bstack11l1ll1l11_opy_.bstack111ll111_opy_()
    bstack1lll1111ll_opy_()
    bstack1ll1l11ll1_opy_ = True
    bstack1ll11llll1_opy_ = bstack11l1ll1l11_opy_.bstack111l11ll_opy_()
    bstack11l1ll1l11_opy_.bstack1111111l_opy_(bstack111l11l1l1_opy_)
    bstack11l1ll1l11_opy_.bstack11l11ll1_opy_()
    bstack11lll111l_opy_(bstack1111l1l11l_opy_, CONFIG, bstack11l1ll1l11_opy_.bstack1lll1ll1l_opy_())
    bstack11l111l11l_opy_ = bstack11l1ll1l11_opy_.bstack1llll1lll_opy_(bstack1l111l111l_opy_, {
      bstack1ll1l_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫྮ"): bstack111ll11l1l_opy_,
      bstack1ll1l_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ྯ"): bstack11lll11l1l_opy_,
      bstack1ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨྰ"): bstack1llll1l1l1_opy_
    })
    try:
      bstack1l11ll11l1_opy_, bstack1ll11l1l1l_opy_ = map(list, zip(*bstack11l111l11l_opy_))
      bstack1l1l1l11ll_opy_ = bstack1l11ll11l1_opy_[0]
      for status_code in bstack1ll11l1l1l_opy_:
        if status_code != 0:
          bstack111ll1lll_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1ll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡦࡴࡵࡳࡷࡹࠠࡢࡰࡧࠤࡸࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠰ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠺ࠡࡽࢀࠦྱ").format(str(e)))
  elif bstack1111l1l11l_opy_ == bstack1ll1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧྲ"):
    try:
      from behave.__main__ import main as bstack11lll1l1l_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l111l1l1l_opy_(e, bstack1ll111ll1l_opy_)
    bstack1lll1111ll_opy_()
    bstack1ll1l11ll1_opy_ = True
    bstack1111l1l1_opy_ = 1
    if bstack1ll1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨླ") in CONFIG:
      bstack1111l1l1_opy_ = CONFIG[bstack1ll1l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩྴ")]
    if bstack1ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྵ") in CONFIG:
      bstack111l111lll_opy_ = int(bstack1111l1l1_opy_) * int(len(CONFIG[bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྶ")]))
    else:
      bstack111l111lll_opy_ = int(bstack1111l1l1_opy_)
    config = Configuration(args)
    bstack1lll11l11l_opy_ = config.paths
    if len(bstack1lll11l11l_opy_) == 0:
      import glob
      pattern = bstack1ll1l_opy_ (u"ࠬ࠰ࠪ࠰ࠬ࠱ࡪࡪࡧࡴࡶࡴࡨࠫྷ")
      bstack1l111l1ll_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1l111l1ll_opy_)
      config = Configuration(args)
      bstack1lll11l11l_opy_ = config.paths
    bstack1lllll11l_opy_ = [os.path.normpath(item) for item in bstack1lll11l11l_opy_]
    bstack111lllllll_opy_ = [os.path.normpath(item) for item in args]
    bstack1111l11l1_opy_ = [item for item in bstack111lllllll_opy_ if item not in bstack1lllll11l_opy_]
    import platform as pf
    if pf.system().lower() == bstack1ll1l_opy_ (u"࠭ࡷࡪࡰࡧࡳࡼࡹࠧྸ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1lllll11l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack111l11111l_opy_)))
                    for bstack111l11111l_opy_ in bstack1lllll11l_opy_]
    bstack111llll1_opy_ = []
    for spec in bstack1lllll11l_opy_:
      bstack11111111_opy_ = []
      bstack11111111_opy_ += bstack1111l11l1_opy_
      bstack11111111_opy_.append(spec)
      bstack111llll1_opy_.append(bstack11111111_opy_)
    execution_items = []
    for bstack11111111_opy_ in bstack111llll1_opy_:
      if bstack1ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪྐྵ") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack1ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫྺ")]):
          item = {}
          item[bstack1ll1l_opy_ (u"ࠩࡤࡶ࡬࠭ྻ")] = bstack1ll1l_opy_ (u"ࠪࠤࠬྼ").join(bstack11111111_opy_)
          item[bstack1ll1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ྽")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack1ll1l_opy_ (u"ࠬࡧࡲࡨࠩ྾")] = bstack1ll1l_opy_ (u"࠭ࠠࠨ྿").join(bstack11111111_opy_)
        item[bstack1ll1l_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭࿀")] = 0
        execution_items.append(item)
    bstack11ll11ll11_opy_ = bstack11l1ll1ll1_opy_(execution_items, bstack111l111lll_opy_)
    for execution_item in bstack11ll11ll11_opy_:
      bstack1llll1l1l_opy_ = []
      for item in execution_item:
        bstack1llll1l1l_opy_.append(bstack1lll1lll1l_opy_(name=str(item[bstack1ll1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ࿁")]),
                                             target=bstack11lll1111_opy_,
                                             args=(item[bstack1ll1l_opy_ (u"ࠩࡤࡶ࡬࠭࿂")],)))
      for t in bstack1llll1l1l_opy_:
        t.start()
      for t in bstack1llll1l1l_opy_:
        t.join()
  else:
    bstack1lllll1l11_opy_(bstack1l1ll1llll_opy_)
  if not bstack1l1llll1l1_opy_:
    bstack1l1111lll_opy_()
    if(bstack1111l1l11l_opy_ in [bstack1ll1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ࿃"), bstack1ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ࿄")]):
      bstack1l1111111l_opy_()
  bstack1ll1ll111_opy_.bstack1l1111111_opy_()
def browserstack_initialize(bstack1l1111l1ll_opy_=None):
  logger.info(bstack1ll1l_opy_ (u"ࠬࡘࡵ࡯ࡰ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡻ࡮ࡺࡨࠡࡣࡵ࡫ࡸࡀࠠࠨ࿅") + str(bstack1l1111l1ll_opy_))
  run_on_browserstack(bstack1l1111l1ll_opy_, None, True)
@measure(event_name=EVENTS.bstack1lllllll11_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack1l1111lll_opy_():
  global CONFIG
  global bstack1lll11lll1_opy_
  global bstack111ll1lll_opy_
  global bstack11l11ll111_opy_
  global bstack111111ll_opy_
  bstack1llll1l11l_opy_.bstack11llll11l1_opy_()
  if cli.is_running():
    bstack1l1lll11l1_opy_.invoke(Events.bstack1ll1ll1l11_opy_)
  else:
    bstack1111llll_opy_ = bstack11111l1l_opy_.bstack111l1ll1_opy_(config=CONFIG)
    bstack1111llll_opy_.bstack111llll11l_opy_(CONFIG)
  if bstack1lll11lll1_opy_ == bstack1ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࿆࠭"):
    if not cli.is_enabled(CONFIG):
      bstack1lllll11_opy_.stop()
  else:
    bstack1lllll11_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1l11llll_opy_.bstack1l11l1ll11_opy_()
  if bstack1ll1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ࿇") in CONFIG and str(CONFIG[bstack1ll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ࿈")]).lower() != bstack1ll1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ࿉"):
    hashed_id, bstack1l111lll1_opy_ = bstack111ll111ll_opy_()
  else:
    hashed_id, bstack1l111lll1_opy_ = get_build_link()
  bstack11ll11ll1l_opy_(hashed_id)
  logger.info(bstack1ll1l_opy_ (u"ࠪࡗࡉࡑࠠࡳࡷࡱࠤࡪࡴࡤࡦࡦࠣࡪࡴࡸࠠࡪࡦ࠽ࠫ࿊") + bstack111111ll_opy_.get_property(bstack1ll1l_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭࿋"), bstack1ll1l_opy_ (u"ࠬ࠭࿌")) + bstack1ll1l_opy_ (u"࠭ࠬࠡࡶࡨࡷࡹ࡮ࡵࡣࠢ࡬ࡨ࠿ࠦࠧ࿍") + os.getenv(bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ࿎"), bstack1ll1l_opy_ (u"ࠨࠩ࿏")))
  if hashed_id is not None and bstack11l1l111l_opy_() != -1:
    sessions = bstack11ll11l1ll_opy_(hashed_id)
    bstack111l1l11l1_opy_(sessions, bstack1l111lll1_opy_)
  if bstack1lll11lll1_opy_ == bstack1ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ࿐") and bstack111ll1lll_opy_ != 0:
    sys.exit(bstack111ll1lll_opy_)
  if bstack1lll11lll1_opy_ == bstack1ll1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ࿑") and bstack11l11ll111_opy_ != 0:
    sys.exit(bstack11l11ll111_opy_)
def bstack11ll11ll1l_opy_(new_id):
    global bstack111l11lll_opy_
    bstack111l11lll_opy_ = new_id
def bstack1ll1l1111_opy_(bstack11l11111ll_opy_):
  if bstack11l11111ll_opy_:
    return bstack11l11111ll_opy_.capitalize()
  else:
    return bstack1ll1l_opy_ (u"ࠫࠬ࿒")
@measure(event_name=EVENTS.bstack11lllll11l_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack111ll111l_opy_(bstack111l111ll1_opy_):
  if bstack1ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ࿓") in bstack111l111ll1_opy_ and bstack111l111ll1_opy_[bstack1ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ࿔")] != bstack1ll1l_opy_ (u"ࠧࠨ࿕"):
    return bstack111l111ll1_opy_[bstack1ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭࿖")]
  else:
    bstack1llll111ll_opy_ = bstack1ll1l_opy_ (u"ࠤࠥ࿗")
    if bstack1ll1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ࿘") in bstack111l111ll1_opy_ and bstack111l111ll1_opy_[bstack1ll1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ࿙")] != None:
      bstack1llll111ll_opy_ += bstack111l111ll1_opy_[bstack1ll1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ࿚")] + bstack1ll1l_opy_ (u"ࠨࠬࠡࠤ࿛")
      if bstack111l111ll1_opy_[bstack1ll1l_opy_ (u"ࠧࡰࡵࠪ࿜")] == bstack1ll1l_opy_ (u"ࠣ࡫ࡲࡷࠧ࿝"):
        bstack1llll111ll_opy_ += bstack1ll1l_opy_ (u"ࠤ࡬ࡓࡘࠦࠢ࿞")
      bstack1llll111ll_opy_ += (bstack111l111ll1_opy_[bstack1ll1l_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ࿟")] or bstack1ll1l_opy_ (u"ࠫࠬ࿠"))
      return bstack1llll111ll_opy_
    else:
      bstack1llll111ll_opy_ += bstack1ll1l1111_opy_(bstack111l111ll1_opy_[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭࿡")]) + bstack1ll1l_opy_ (u"ࠨࠠࠣ࿢") + (
              bstack111l111ll1_opy_[bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ࿣")] or bstack1ll1l_opy_ (u"ࠨࠩ࿤")) + bstack1ll1l_opy_ (u"ࠤ࠯ࠤࠧ࿥")
      if bstack111l111ll1_opy_[bstack1ll1l_opy_ (u"ࠪࡳࡸ࠭࿦")] == bstack1ll1l_opy_ (u"ࠦ࡜࡯࡮ࡥࡱࡺࡷࠧ࿧"):
        bstack1llll111ll_opy_ += bstack1ll1l_opy_ (u"ࠧ࡝ࡩ࡯ࠢࠥ࿨")
      bstack1llll111ll_opy_ += bstack111l111ll1_opy_[bstack1ll1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪ࿩")] or bstack1ll1l_opy_ (u"ࠧࠨ࿪")
      return bstack1llll111ll_opy_
@measure(event_name=EVENTS.bstack11llll1l1_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack1111111l1_opy_(bstack1llll11l1l_opy_):
  if bstack1llll11l1l_opy_ == bstack1ll1l_opy_ (u"ࠣࡦࡲࡲࡪࠨ࿫"):
    return bstack1ll1l_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ࿬")
  elif bstack1llll11l1l_opy_ == bstack1ll1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ࿭"):
    return bstack1ll1l_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡉࡥ࡮ࡲࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ࿮")
  elif bstack1llll11l1l_opy_ == bstack1ll1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ࿯"):
    return bstack1ll1l_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡩࡵࡩࡪࡴ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡩࡵࡩࡪࡴࠢ࠿ࡒࡤࡷࡸ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭࿰")
  elif bstack1llll11l1l_opy_ == bstack1ll1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨ࿱"):
    return bstack1ll1l_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡶࡪࡪ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡴࡨࡨࠧࡄࡅࡳࡴࡲࡶࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ࿲")
  elif bstack1llll11l1l_opy_ == bstack1ll1l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥ࿳"):
    return bstack1ll1l_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࠩࡥࡦࡣ࠶࠶࠻ࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࠤࡧࡨࡥ࠸࠸࠶ࠣࡀࡗ࡭ࡲ࡫࡯ࡶࡶ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ࿴")
  elif bstack1llll11l1l_opy_ == bstack1ll1l_opy_ (u"ࠦࡷࡻ࡮࡯࡫ࡱ࡫ࠧ࿵"):
    return bstack1ll1l_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࡓࡷࡱࡲ࡮ࡴࡧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭࿶")
  else:
    return bstack1ll1l_opy_ (u"࠭࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࠪ࿷") + bstack1ll1l1111_opy_(
      bstack1llll11l1l_opy_) + bstack1ll1l_opy_ (u"ࠧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭࿸")
def bstack1l1l1l11l_opy_(session):
  return bstack1ll1l_opy_ (u"ࠨ࠾ࡷࡶࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡸ࡯ࡸࠤࡁࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠥࡹࡥࡴࡵ࡬ࡳࡳ࠳࡮ࡢ࡯ࡨࠦࡃࡂࡡࠡࡪࡵࡩ࡫ࡃࠢࡼࡿࠥࠤࡹࡧࡲࡨࡧࡷࡁࠧࡥࡢ࡭ࡣࡱ࡯ࠧࡄࡻࡾ࠾࠲ࡥࡃࡂ࠯ࡵࡦࡁࡿࢂࢁࡽ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿࠳ࡹࡸ࠾ࠨ࿹").format(
    session[bstack1ll1l_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭࿺")], bstack111ll111l_opy_(session), bstack1111111l1_opy_(session[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠩ࿻")]),
    bstack1111111l1_opy_(session[bstack1ll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ࿼")]),
    bstack1ll1l1111_opy_(session[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭࿽")] or session[bstack1ll1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭࿾")] or bstack1ll1l_opy_ (u"ࠧࠨ࿿")) + bstack1ll1l_opy_ (u"ࠣࠢࠥက") + (session[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫခ")] or bstack1ll1l_opy_ (u"ࠪࠫဂ")),
    session[bstack1ll1l_opy_ (u"ࠫࡴࡹࠧဃ")] + bstack1ll1l_opy_ (u"ࠧࠦࠢင") + session[bstack1ll1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪစ")], session[bstack1ll1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩဆ")] or bstack1ll1l_opy_ (u"ࠨࠩဇ"),
    session[bstack1ll1l_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭ဈ")] if session[bstack1ll1l_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧဉ")] else bstack1ll1l_opy_ (u"ࠫࠬည"))
@measure(event_name=EVENTS.bstack1ll1l11l11_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def bstack111l1l11l1_opy_(sessions, bstack1l111lll1_opy_):
  try:
    bstack111111l11_opy_ = bstack1ll1l_opy_ (u"ࠧࠨဋ")
    if not os.path.exists(bstack1111l111l1_opy_):
      os.mkdir(bstack1111l111l1_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll1l_opy_ (u"࠭ࡡࡴࡵࡨࡸࡸ࠵ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ࠫဌ")), bstack1ll1l_opy_ (u"ࠧࡳࠩဍ")) as f:
      bstack111111l11_opy_ = f.read()
    bstack111111l11_opy_ = bstack111111l11_opy_.replace(bstack1ll1l_opy_ (u"ࠨࡽࠨࡖࡊ࡙ࡕࡍࡖࡖࡣࡈࡕࡕࡏࡖࠨࢁࠬဎ"), str(len(sessions)))
    bstack111111l11_opy_ = bstack111111l11_opy_.replace(bstack1ll1l_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠥࡾࠩဏ"), bstack1l111lll1_opy_)
    bstack111111l11_opy_ = bstack111111l11_opy_.replace(bstack1ll1l_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣࡓࡇࡍࡆࠧࢀࠫတ"),
                                              sessions[0].get(bstack1ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡲࡦࡳࡥࠨထ")) if sessions[0] else bstack1ll1l_opy_ (u"ࠬ࠭ဒ"))
    with open(os.path.join(bstack1111l111l1_opy_, bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪဓ")), bstack1ll1l_opy_ (u"ࠧࡸࠩန")) as stream:
      stream.write(bstack111111l11_opy_.split(bstack1ll1l_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁࠬပ"))[0])
      for session in sessions:
        stream.write(bstack1l1l1l11l_opy_(session))
      stream.write(bstack111111l11_opy_.split(bstack1ll1l_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂ࠭ဖ"))[1])
    logger.info(bstack1ll1l_opy_ (u"ࠪࡋࡪࡴࡥࡳࡣࡷࡩࡩࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡨࡵࡪ࡮ࡧࠤࡦࡸࡴࡪࡨࡤࡧࡹࡹࠠࡢࡶࠣࡿࢂ࠭ဗ").format(bstack1111l111l1_opy_));
  except Exception as e:
    logger.debug(bstack111l1lll1l_opy_.format(str(e)))
def bstack11ll11l1ll_opy_(hashed_id):
  global CONFIG
  try:
    bstack1l11l11lll_opy_ = datetime.datetime.now()
    host = bstack1ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠯ࡦࡰࡴࡻࡤ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫဘ") if bstack1ll1l_opy_ (u"ࠬࡧࡰࡱࠩမ") in CONFIG else bstack1ll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧယ")
    user = CONFIG[bstack1ll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩရ")]
    key = CONFIG[bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫလ")]
    bstack1111lllll_opy_ = bstack1ll1l_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨဝ") if bstack1ll1l_opy_ (u"ࠪࡥࡵࡶࠧသ") in CONFIG else (bstack1ll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨဟ") if CONFIG.get(bstack1ll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩဠ")) else bstack1ll1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨအ"))
    host = bstack1ll11l1l1_opy_(cli.config, [bstack1ll1l_opy_ (u"ࠢࡢࡲ࡬ࡷࠧဢ"), bstack1ll1l_opy_ (u"ࠣࡣࡳࡴࡆࡻࡴࡰ࡯ࡤࡸࡪࠨဣ"), bstack1ll1l_opy_ (u"ࠤࡤࡴ࡮ࠨဤ")], host) if bstack1ll1l_opy_ (u"ࠪࡥࡵࡶࠧဥ") in CONFIG else bstack1ll11l1l1_opy_(cli.config, [bstack1ll1l_opy_ (u"ࠦࡦࡶࡩࡴࠤဦ"), bstack1ll1l_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢဧ"), bstack1ll1l_opy_ (u"ࠨࡡࡱ࡫ࠥဨ")], host)
    url = bstack1ll1l_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡶࡩࡸࡹࡩࡰࡰࡶ࠲࡯ࡹ࡯࡯ࠩဩ").format(host, bstack1111lllll_opy_, hashed_id)
    headers = {
      bstack1ll1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧဪ"): bstack1ll1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬါ"),
    }
    proxies = bstack111l1l1ll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡩࡨࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡹ࡟࡭࡫ࡶࡸࠧာ"), datetime.datetime.now() - bstack1l11l11lll_opy_)
      return list(map(lambda session: session[bstack1ll1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩိ")], response.json()))
  except Exception as e:
    logger.debug(bstack11l1111l1l_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack1l1lll1111_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def get_build_link():
  global CONFIG
  global bstack111l11lll_opy_
  try:
    if bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨီ") in CONFIG:
      bstack1l11l11lll_opy_ = datetime.datetime.now()
      host = bstack1ll1l_opy_ (u"࠭ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥࠩု") if bstack1ll1l_opy_ (u"ࠧࡢࡲࡳࠫူ") in CONFIG else bstack1ll1l_opy_ (u"ࠨࡣࡳ࡭ࠬေ")
      user = CONFIG[bstack1ll1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫဲ")]
      key = CONFIG[bstack1ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ဳ")]
      bstack1111lllll_opy_ = bstack1ll1l_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪဴ") if bstack1ll1l_opy_ (u"ࠬࡧࡰࡱࠩဵ") in CONFIG else bstack1ll1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨံ")
      url = bstack1ll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠰࡭ࡷࡴࡴ့ࠧ").format(user, key, host, bstack1111lllll_opy_)
      if cli.is_enabled(CONFIG):
        bstack1l111lll1_opy_, hashed_id = cli.bstack1ll1l1111l_opy_()
        logger.info(bstack1ll11111ll_opy_.format(bstack1l111lll1_opy_))
        return [hashed_id, bstack1l111lll1_opy_]
      else:
        headers = {
          bstack1ll1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧး"): bstack1ll1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲ္ࠬ"),
        }
        if bstack1ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ်ࠬ") in CONFIG:
          params = {bstack1ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩျ"): CONFIG[bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨြ")], bstack1ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩွ"): CONFIG[bstack1ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩှ")]}
        else:
          params = {bstack1ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ဿ"): CONFIG[bstack1ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ၀")]}
        proxies = bstack111l1l1ll_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack11111l11ll_opy_ = response.json()[0][bstack1ll1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡣࡷ࡬ࡰࡩ࠭၁")]
          if bstack11111l11ll_opy_:
            bstack1l111lll1_opy_ = bstack11111l11ll_opy_[bstack1ll1l_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨ၂")].split(bstack1ll1l_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧ࠲ࡨࡵࡪ࡮ࡧࠫ၃"))[0] + bstack1ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡸ࠵ࠧ၄") + bstack11111l11ll_opy_[
              bstack1ll1l_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ၅")]
            logger.info(bstack1ll11111ll_opy_.format(bstack1l111lll1_opy_))
            bstack111l11lll_opy_ = bstack11111l11ll_opy_[bstack1ll1l_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ၆")]
            bstack1lll111lll_opy_ = CONFIG[bstack1ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ၇")]
            if bstack1ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ၈") in CONFIG:
              bstack1lll111lll_opy_ += bstack1ll1l_opy_ (u"ࠫࠥ࠭၉") + CONFIG[bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ၊")]
            if bstack1lll111lll_opy_ != bstack11111l11ll_opy_[bstack1ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ။")]:
              logger.debug(bstack1l1l11llll_opy_.format(bstack11111l11ll_opy_[bstack1ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ၌")], bstack1lll111lll_opy_))
            cli.bstack111111l1l_opy_(bstack1ll1l_opy_ (u"ࠣࡪࡷࡸࡵࡀࡧࡦࡶࡢࡦࡺ࡯࡬ࡥࡡ࡯࡭ࡳࡱࠢ၍"), datetime.datetime.now() - bstack1l11l11lll_opy_)
            return [bstack11111l11ll_opy_[bstack1ll1l_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ၎")], bstack1l111lll1_opy_]
    else:
      logger.warn(bstack1lllll1111_opy_)
  except Exception as e:
    logger.debug(bstack1l1111llll_opy_.format(str(e)))
  return [None, None]
def bstack1l11l1l11l_opy_(url, bstack11ll111l1_opy_=False):
  global CONFIG
  global bstack11l1l11111_opy_
  if not bstack11l1l11111_opy_:
    hostname = bstack1l111l11l1_opy_(url)
    is_private = bstack11llllll11_opy_(hostname)
    if (bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ၏") in CONFIG and not bstack1lll1ll111_opy_(CONFIG[bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨၐ")])) and (is_private or bstack11ll111l1_opy_):
      bstack11l1l11111_opy_ = hostname
def bstack1l111l11l1_opy_(url):
  return urlparse(url).hostname
def bstack11llllll11_opy_(hostname):
  for bstack1lll11111_opy_ in bstack1ll1ll11l1_opy_:
    regex = re.compile(bstack1lll11111_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1l111111ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack11l1ll1111_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1l1lllllll_opy_
  bstack11ll11lll_opy_ = not (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၑ"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1ll1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၒ"), None))
  bstack11l1l1lll1_opy_ = getattr(driver, bstack1ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧၓ"), None) != True
  bstack11l11ll1ll_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၔ"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1ll1l_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၕ"), None)
  if bstack11l11ll1ll_opy_:
    if not bstack1l1l11l11_opy_():
      logger.warning(bstack1ll1l_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸ࠴ࠢၖ"))
      return {}
    logger.debug(bstack1ll1l_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨၗ"))
    logger.debug(perform_scan(driver, driver_command=bstack1ll1l_opy_ (u"ࠬ࡫ࡸࡦࡥࡸࡸࡪ࡙ࡣࡳ࡫ࡳࡸࠬၘ")))
    results = bstack11lll1llll_opy_(bstack1ll1l_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹࡹࠢၙ"))
    if results is not None and results.get(bstack1ll1l_opy_ (u"ࠢࡪࡵࡶࡹࡪࡹࠢၚ")) is not None:
        return results[bstack1ll1l_opy_ (u"ࠣ࡫ࡶࡷࡺ࡫ࡳࠣၛ")]
    logger.error(bstack1ll1l_opy_ (u"ࠤࡑࡳࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡘࡥࡴࡷ࡯ࡸࡸࠦࡷࡦࡴࡨࠤ࡫ࡵࡵ࡯ࡦ࠱ࠦၜ"))
    return []
  if not bstack1lllllll1_opy_.bstack1l1l1ll1l_opy_(CONFIG, bstack1l1lllllll_opy_) or (bstack11l1l1lll1_opy_ and bstack11ll11lll_opy_):
    logger.warning(bstack1ll1l_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷ࠳ࠨၝ"))
    return {}
  try:
    logger.debug(bstack1ll1l_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨၞ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1l1ll1lll1_opy_.bstack1l1ll111l1_opy_)
    return results
  except Exception:
    logger.error(bstack1ll1l_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡺࡩࡷ࡫ࠠࡧࡱࡸࡲࡩ࠴ࠢၟ"))
    return {}
@measure(event_name=EVENTS.bstack1ll1l1l11_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1l1lllllll_opy_
  bstack11ll11lll_opy_ = not (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪၠ"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1ll1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ၡ"), None))
  bstack11l1l1lll1_opy_ = getattr(driver, bstack1ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨၢ"), None) != True
  bstack11l11ll1ll_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၣ"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1ll1l_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၤ"), None)
  if bstack11l11ll1ll_opy_:
    if not bstack1l1l11l11_opy_():
      logger.warning(bstack1ll1l_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹ࠯ࠤၥ"))
      return {}
    logger.debug(bstack1ll1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻࠪၦ"))
    logger.debug(perform_scan(driver, driver_command=bstack1ll1l_opy_ (u"࠭ࡥࡹࡧࡦࡹࡹ࡫ࡓࡤࡴ࡬ࡴࡹ࠭ၧ")))
    results = bstack11lll1llll_opy_(bstack1ll1l_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡓࡶ࡯ࡰࡥࡷࡿࠢၨ"))
    if results is not None and results.get(bstack1ll1l_opy_ (u"ࠣࡵࡸࡱࡲࡧࡲࡺࠤၩ")) is not None:
        return results[bstack1ll1l_opy_ (u"ࠤࡶࡹࡲࡳࡡࡳࡻࠥၪ")]
    logger.error(bstack1ll1l_opy_ (u"ࠥࡒࡴࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡒࡦࡵࡸࡰࡹࡹࠠࡔࡷࡰࡱࡦࡸࡹࠡࡹࡤࡷࠥ࡬࡯ࡶࡰࡧ࠲ࠧၫ"))
    return {}
  if not bstack1lllllll1_opy_.bstack1l1l1ll1l_opy_(CONFIG, bstack1l1lllllll_opy_) or (bstack11l1l1lll1_opy_ and bstack11ll11lll_opy_):
    logger.warning(bstack1ll1l_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡳࡶ࡯ࡰࡥࡷࡿ࠮ࠣၬ"))
    return {}
  try:
    logger.debug(bstack1ll1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻࠪၭ"))
    logger.debug(perform_scan(driver))
    bstack111ll1111l_opy_ = driver.execute_async_script(bstack1l1ll1lll1_opy_.bstack1llll1111l_opy_)
    return bstack111ll1111l_opy_
  except Exception:
    logger.error(bstack1ll1l_opy_ (u"ࠨࡎࡰࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡹࡲࡳࡡࡳࡻࠣࡻࡦࡹࠠࡧࡱࡸࡲࡩ࠴ࠢၮ"))
    return {}
def bstack1l1l11l11_opy_():
  global CONFIG
  global bstack1l1lllllll_opy_
  bstack1ll1111l11_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၯ"), None) and bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၰ"), None)
  if not bstack1lllllll1_opy_.bstack1l1l1ll1l_opy_(CONFIG, bstack1l1lllllll_opy_) or not bstack1ll1111l11_opy_:
        logger.warning(bstack1ll1l_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤၱ"))
        return False
  return True
def bstack11lll1llll_opy_(bstack1l1lll11l_opy_):
    bstack1lllll111l_opy_ = bstack1lllll11_opy_.current_test_uuid() if bstack1lllll11_opy_.current_test_uuid() else bstack1l11llll_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack11l11l11l1_opy_(bstack1lllll111l_opy_, bstack1l1lll11l_opy_))
        try:
            return future.result(timeout=bstack111llllll1_opy_)
        except TimeoutError:
            logger.error(bstack1ll1l_opy_ (u"ࠥࡘ࡮ࡳࡥࡰࡷࡷࠤࡦ࡬ࡴࡦࡴࠣࡿࢂࡹࠠࡸࡪ࡬ࡰࡪࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡔࡨࡷࡺࡲࡴࡴࠤၲ").format(bstack111llllll1_opy_))
        except Exception as ex:
            logger.debug(bstack1ll1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡶࡪࡺࡲࡪࡧࡹ࡭ࡳ࡭ࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡽࢀ࠲ࠥࡋࡲࡳࡱࡵࠤ࠲ࠦࡻࡾࠤၳ").format(bstack1l1lll11l_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack111l1l1l11_opy_, stage=STAGE.bstack11lll11ll_opy_, bstack1llll111ll_opy_=bstack111llll111_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1l1lllllll_opy_
  bstack11ll11lll_opy_ = not (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၴ"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1ll1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၵ"), None))
  bstack11ll111l11_opy_ = not (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၶ"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1ll1l_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၷ"), None))
  bstack11l1l1lll1_opy_ = getattr(driver, bstack1ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩၸ"), None) != True
  if not bstack1lllllll1_opy_.bstack1l1l1ll1l_opy_(CONFIG, bstack1l1lllllll_opy_) or (bstack11l1l1lll1_opy_ and bstack11ll11lll_opy_ and bstack11ll111l11_opy_):
    logger.warning(bstack1ll1l_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡹࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡤࡣࡱ࠲ࠧၹ"))
    return {}
  try:
    bstack1ll11111l1_opy_ = bstack1ll1l_opy_ (u"ࠫࡦࡶࡰࠨၺ") in CONFIG and CONFIG.get(bstack1ll1l_opy_ (u"ࠬࡧࡰࡱࠩၻ"), bstack1ll1l_opy_ (u"࠭ࠧၼ"))
    session_id = getattr(driver, bstack1ll1l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠫၽ"), None)
    if not session_id:
      logger.warning(bstack1ll1l_opy_ (u"ࠣࡐࡲࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡏࡄࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤࡩࡸࡩࡷࡧࡵࠦၾ"))
      return {bstack1ll1l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣၿ"): bstack1ll1l_opy_ (u"ࠥࡒࡴࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࠣࡪࡴࡻ࡮ࡥࠤႀ")}
    if bstack1ll11111l1_opy_:
      try:
        bstack1lllll11ll_opy_ = {
              bstack1ll1l_opy_ (u"ࠫࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠨႁ"): os.environ.get(bstack1ll1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪႂ"), os.environ.get(bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪႃ"), bstack1ll1l_opy_ (u"ࠧࠨႄ"))),
              bstack1ll1l_opy_ (u"ࠨࡶ࡫ࡘࡪࡹࡴࡓࡷࡱ࡙ࡺ࡯ࡤࠨႅ"): bstack1lllll11_opy_.current_test_uuid() if bstack1lllll11_opy_.current_test_uuid() else bstack1l11llll_opy_.current_hook_uuid(),
              bstack1ll1l_opy_ (u"ࠩࡤࡹࡹ࡮ࡈࡦࡣࡧࡩࡷ࠭ႆ"): os.environ.get(bstack1ll1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨႇ")),
              bstack1ll1l_opy_ (u"ࠫࡸࡩࡡ࡯ࡖ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫႈ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack1ll1l_opy_ (u"ࠬࡺࡨࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪႉ"): os.environ.get(bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫႊ"), bstack1ll1l_opy_ (u"ࠧࠨႋ")),
              bstack1ll1l_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨႌ"): kwargs.get(bstack1ll1l_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࡡࡦࡳࡲࡳࡡ࡯ࡦႍࠪ"), None) or bstack1ll1l_opy_ (u"ࠪࠫႎ")
          }
        if not hasattr(thread_local, bstack1ll1l_opy_ (u"ࠫࡧࡧࡳࡦࡡࡤࡴࡵࡥࡡ࠲࠳ࡼࡣࡸࡩࡲࡪࡲࡷࠫႏ")):
            scripts = {bstack1ll1l_opy_ (u"ࠬࡹࡣࡢࡰࠪ႐"): bstack1l1ll1lll1_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack1111l11ll1_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack1111l11ll1_opy_[bstack1ll1l_opy_ (u"࠭ࡳࡤࡣࡱࠫ႑")] = bstack1111l11ll1_opy_[bstack1ll1l_opy_ (u"ࠧࡴࡥࡤࡲࠬ႒")] % json.dumps(bstack1lllll11ll_opy_)
        bstack1l1ll1lll1_opy_.bstack1l11l111ll_opy_(bstack1111l11ll1_opy_)
        bstack1l1ll1lll1_opy_.store()
        bstack11ll1lll1_opy_ = driver.execute_script(bstack1l1ll1lll1_opy_.perform_scan)
      except Exception as bstack1l1l111ll1_opy_:
        logger.info(bstack1ll1l_opy_ (u"ࠣࡃࡳࡴ࡮ࡻ࡭ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࠣ႓") + str(bstack1l1l111ll1_opy_))
        bstack11ll1lll1_opy_ = {bstack1ll1l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ႔"): str(bstack1l1l111ll1_opy_)}
    else:
      bstack11ll1lll1_opy_ = driver.execute_async_script(bstack1l1ll1lll1_opy_.perform_scan, {bstack1ll1l_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪ႕"): kwargs.get(bstack1ll1l_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣࡨࡵ࡭࡮ࡣࡱࡨࠬ႖"), None) or bstack1ll1l_opy_ (u"ࠬ࠭႗")})
    return bstack11ll1lll1_opy_
  except Exception as err:
    logger.error(bstack1ll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡵࡹࡳࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡤࡣࡱ࠲ࠥࢁࡽࠣ႘").format(str(err)))
    return {}