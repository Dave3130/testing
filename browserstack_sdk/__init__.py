# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
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
from browserstack_sdk.bstack11ll1l1l1_opy_ import bstack111lllll11_opy_
from browserstack_sdk.bstack1lll1l1ll_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack11l1l1l1ll_opy_():
  global CONFIG
  headers = {
        bstack1ll11_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧਃ"): bstack1ll11_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ਄"),
      }
  proxies = bstack1111l1ll1_opy_(CONFIG, bstack1ll1l1llll_opy_)
  try:
    response = requests.get(bstack1ll1l1llll_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l1l1111ll_opy_ = response.json()[bstack1ll11_opy_ (u"ࠪ࡬ࡺࡨࡳࠨਅ")]
      logger.debug(bstack1ll11l1111_opy_.format(response.json()))
      return bstack1l1l1111ll_opy_
    else:
      logger.debug(bstack11l1lll11l_opy_.format(bstack1ll11_opy_ (u"ࠦࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡊࡔࡑࡑࠤࡵࡧࡲࡴࡧࠣࡩࡷࡸ࡯ࡳࠢࠥਆ")))
  except Exception as e:
    logger.debug(bstack11l1lll11l_opy_.format(e))
def bstack1l111ll11_opy_(hub_url):
  global CONFIG
  url = bstack1ll11_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢਇ")+  hub_url + bstack1ll11_opy_ (u"ࠨ࠯ࡤࡪࡨࡧࡰࠨਈ")
  headers = {
        bstack1ll11_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭ਉ"): bstack1ll11_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫਊ"),
      }
  proxies = bstack1111l1ll1_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1111lll1l1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack111l1ll111_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack1l1ll1lll_opy_, stage=STAGE.bstack1111l1111_opy_)
def bstack111ll111ll_opy_():
  try:
    global bstack11l111111l_opy_
    bstack1l1l1111ll_opy_ = bstack11l1l1l1ll_opy_()
    bstack11111111l_opy_ = []
    results = []
    for bstack1ll1l11l11_opy_ in bstack1l1l1111ll_opy_:
      bstack11111111l_opy_.append(bstack1ll1111l11_opy_(target=bstack1l111ll11_opy_,args=(bstack1ll1l11l11_opy_,)))
    for t in bstack11111111l_opy_:
      t.start()
    for t in bstack11111111l_opy_:
      results.append(t.join())
    bstack1lll111ll_opy_ = {}
    for item in results:
      hub_url = item[bstack1ll11_opy_ (u"ࠩ࡫ࡹࡧࡥࡵࡳ࡮ࠪ਋")]
      latency = item[bstack1ll11_opy_ (u"ࠪࡰࡦࡺࡥ࡯ࡥࡼࠫ਌")]
      bstack1lll111ll_opy_[hub_url] = latency
    bstack1lll1llll1_opy_ = min(bstack1lll111ll_opy_, key= lambda x: bstack1lll111ll_opy_[x])
    bstack11l111111l_opy_ = bstack1lll1llll1_opy_
    logger.debug(bstack11111lll1l_opy_.format(bstack1lll1llll1_opy_))
  except Exception as e:
    logger.debug(bstack1111lllll1_opy_.format(e))
from browserstack_sdk.bstack1lll1llll_opy_ import *
from browserstack_sdk.bstack111lll11_opy_ import *
from browserstack_sdk.bstack11ll11l1_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack1l1l1l1111_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack11lll11lll_opy_, stage=STAGE.bstack1111l1111_opy_)
def bstack11ll1l111_opy_():
    global bstack11l111111l_opy_
    try:
        bstack111l1l11ll_opy_ = bstack1lllll111l_opy_()
        bstack1l1111111_opy_(bstack111l1l11ll_opy_)
        hub_url = bstack111l1l11ll_opy_.get(bstack1ll11_opy_ (u"ࠦࡺࡸ࡬ࠣ਍"), bstack1ll11_opy_ (u"ࠧࠨ਎"))
        if hub_url.endswith(bstack1ll11_opy_ (u"࠭࠯ࡸࡦ࠲࡬ࡺࡨࠧਏ")):
            hub_url = hub_url.rsplit(bstack1ll11_opy_ (u"ࠧ࠰ࡹࡧ࠳࡭ࡻࡢࠨਐ"), 1)[0]
        if hub_url.startswith(bstack1ll11_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࠩ਑")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack1ll11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠫ਒")):
            hub_url = hub_url[8:]
        bstack11l111111l_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1lllll111l_opy_():
    global CONFIG
    bstack1ll1l11ll_opy_ = CONFIG.get(bstack1ll11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧਓ"), {}).get(bstack1ll11_opy_ (u"ࠫ࡬ࡸࡩࡥࡐࡤࡱࡪ࠭ਔ"), bstack1ll11_opy_ (u"ࠬࡔࡏࡠࡉࡕࡍࡉࡥࡎࡂࡏࡈࡣࡕࡇࡓࡔࡇࡇࠫਕ"))
    if not isinstance(bstack1ll1l11ll_opy_, str):
        raise ValueError(bstack1ll11_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡍࡲࡪࡦࠣࡲࡦࡳࡥࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡤࠤࡻࡧ࡬ࡪࡦࠣࡷࡹࡸࡩ࡯ࡩࠥਖ"))
    try:
        bstack111l1l11ll_opy_ = bstack1l1l111l1_opy_(bstack1ll1l11ll_opy_)
        return bstack111l1l11ll_opy_
    except Exception as e:
        logger.error(bstack1ll11_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳࠡ࠼ࠣࡿࢂࠨਗ").format(str(e)))
        return {}
def bstack1l1l111l1_opy_(bstack1ll1l11ll_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack1ll11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪਘ")] or not CONFIG[bstack1ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬਙ")]:
            raise ValueError(bstack1ll11_opy_ (u"ࠥࡑ࡮ࡹࡳࡪࡰࡪࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠥࡵࡲࠡࡣࡦࡧࡪࡹࡳࠡ࡭ࡨࡽࠧਚ"))
        url = bstack1l1l1l11l_opy_ + bstack1ll1l11ll_opy_
        auth = (CONFIG[bstack1ll11_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ਛ")], CONFIG[bstack1ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨਜ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack111lllll1_opy_ = json.loads(response.text)
            return bstack111lllll1_opy_
    except ValueError as ve:
        logger.error(bstack1ll11_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳࠡ࠼ࠣࡿࢂࠨਝ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack1ll11_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢਞ").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1l1111111_opy_(bstack111l1111l1_opy_):
    global CONFIG
    if bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬਟ") not in CONFIG or str(CONFIG[bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ਠ")]).lower() == bstack1ll11_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩਡ"):
        CONFIG[bstack1ll11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪਢ")] = False
    elif bstack1ll11_opy_ (u"ࠬ࡯ࡳࡕࡴ࡬ࡥࡱࡍࡲࡪࡦࠪਣ") in bstack111l1111l1_opy_:
        bstack1ll11111l1_opy_ = CONFIG.get(bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪਤ"), {})
        logger.debug(bstack1ll11_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡹ࡫ࡶࡸ࡮ࡴࡧࠡ࡮ࡲࡧࡦࡲࠠࡰࡲࡷ࡭ࡴࡴࡳ࠻ࠢࠨࡷࠧਥ"), bstack1ll11111l1_opy_)
        bstack1l11l11ll_opy_ = bstack111l1111l1_opy_.get(bstack1ll11_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡓࡧࡳࡩࡦࡺࡥࡳࡵࠥਦ"), [])
        bstack111l1ll11l_opy_ = bstack1ll11_opy_ (u"ࠤ࠯ࠦਧ").join(bstack1l11l11ll_opy_)
        logger.debug(bstack1ll11_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡆࡹࡸࡺ࡯࡮ࠢࡵࡩࡵ࡫ࡡࡵࡧࡵࠤࡸࡺࡲࡪࡰࡪ࠾ࠥࠫࡳࠣਨ"), bstack111l1ll11l_opy_)
        bstack1l1ll11l1l_opy_ = {
            bstack1ll11_opy_ (u"ࠦࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨ਩"): bstack1ll11_opy_ (u"ࠧࡧࡴࡴ࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠦਪ"),
            bstack1ll11_opy_ (u"ࠨࡦࡰࡴࡦࡩࡑࡵࡣࡢ࡮ࠥਫ"): bstack1ll11_opy_ (u"ࠢࡵࡴࡸࡩࠧਬ"),
            bstack1ll11_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭࠮ࡴࡨࡴࡪࡧࡴࡦࡴࠥਭ"): bstack111l1ll11l_opy_
        }
        bstack1ll11111l1_opy_.update(bstack1l1ll11l1l_opy_)
        logger.debug(bstack1ll11_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡗࡳࡨࡦࡺࡥࡥࠢ࡯ࡳࡨࡧ࡬ࠡࡱࡳࡸ࡮ࡵ࡮ࡴ࠼ࠣࠩࡸࠨਮ"), bstack1ll11111l1_opy_)
        CONFIG[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧਯ")] = bstack1ll11111l1_opy_
        logger.debug(bstack1ll11_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡊ࡮ࡴࡡ࡭ࠢࡆࡓࡓࡌࡉࡈ࠼ࠣࠩࡸࠨਰ"), CONFIG)
def bstack1111llllll_opy_():
    bstack111l1l11ll_opy_ = bstack1lllll111l_opy_()
    if not bstack111l1l11ll_opy_[bstack1ll11_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡗࡵࡰࠬ਱")]:
      raise ValueError(bstack1ll11_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡘࡶࡱࠦࡩࡴࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡷࡵ࡭ࠡࡩࡵ࡭ࡩࠦࡤࡦࡶࡤ࡭ࡱࡹ࠮ࠣਲ"))
    return bstack111l1l11ll_opy_[bstack1ll11_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠧਲ਼")] + bstack1ll11_opy_ (u"ࠨࡁࡦࡥࡵࡹ࠽ࠨ਴")
@measure(event_name=EVENTS.bstack1l11lll1l_opy_, stage=STAGE.bstack1111l1111_opy_)
def bstack1l1ll1111_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack1ll11_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫਵ")], CONFIG[bstack1ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ਸ਼")])
        url = bstack1l11l11l1_opy_
        logger.debug(bstack1ll11_opy_ (u"ࠦࡆࡺࡴࡦ࡯ࡳࡸ࡮ࡴࡧࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡦࡺ࡯࡬ࡥࡵࠣࡪࡷࡵ࡭ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡕࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠤࡆࡖࡉࠣ਷"))
        try:
            response = requests.get(url, auth=auth, headers={bstack1ll11_opy_ (u"ࠧࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠦਸ"): bstack1ll11_opy_ (u"ࠨࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠤਹ")})
            if response.status_code == 200:
                bstack1lllll1111_opy_ = json.loads(response.text)
                bstack11111l1ll_opy_ = bstack1lllll1111_opy_.get(bstack1ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡹࠧ਺"), [])
                if bstack11111l1ll_opy_:
                    bstack1l1ll11ll_opy_ = bstack11111l1ll_opy_[0]
                    build_hashed_id = bstack1l1ll11ll_opy_.get(bstack1ll11_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ਻"))
                    bstack11l11lllll_opy_ = bstack111lll1lll_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack11l11lllll_opy_])
                    logger.info(bstack111l11ll11_opy_.format(bstack11l11lllll_opy_))
                    bstack1l11ll1l1_opy_ = CONFIG[bstack1ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩ਼ࠬ")]
                    if bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ਽") in CONFIG:
                      bstack1l11ll1l1_opy_ += bstack1ll11_opy_ (u"ࠫࠥ࠭ਾ") + CONFIG[bstack1ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧਿ")]
                    if bstack1l11ll1l1_opy_ != bstack1l1ll11ll_opy_.get(bstack1ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫੀ")):
                      logger.debug(bstack1l1l111l1l_opy_.format(bstack1l1ll11ll_opy_.get(bstack1ll11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬੁ")), bstack1l11ll1l1_opy_))
                    return result
                else:
                    logger.debug(bstack1ll11_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡏࡱࠣࡦࡺ࡯࡬ࡥࡵࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࡺࡨࡦࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠲ࠧੂ"))
            else:
                logger.debug(bstack1ll11_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡦࡺ࡯࡬ࡥࡵ࠱ࠦ੃"))
        except Exception as e:
            logger.error(bstack1ll11_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࡷࠥࡀࠠࡼࡿࠥ੄").format(str(e)))
    else:
        logger.debug(bstack1ll11_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡇࡔࡔࡆࡊࡉࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡷࡪࡺ࠮ࠡࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡦࡺ࡯࡬ࡥࡵ࠱ࠦ੅"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1ll1ll111_opy_ import bstack1ll1ll111_opy_, Events, bstack11l1ll1ll1_opy_, bstack1ll11l1l1l_opy_
from bstack_utils.measure import bstack11l111l1l_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack11lll1l111_opy_ import bstack1l1ll1llll_opy_
from bstack_utils.messages import *
from bstack_utils import bstack1l1l1l1111_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l1l1lll11_opy_, bstack11ll1llll_opy_, bstack11l11111l_opy_, bstack1ll1ll11_opy_, \
  bstack111lll111l_opy_, \
  Notset, bstack1lll111lll_opy_, \
  bstack1ll11ll1l1_opy_, bstack1l111l11l_opy_, bstack1111l11l1_opy_, bstack1l11l1l11l_opy_, bstack11ll11lll1_opy_, bstack11l111ll1l_opy_, \
  bstack11l111ll1_opy_, \
  bstack11lll11l11_opy_, bstack111l1l1ll_opy_, bstack1111ll1l1_opy_, bstack1111l11ll1_opy_, \
  bstack11ll1lllll_opy_, bstack111l11lll1_opy_, bstack1llll1lll1_opy_, bstack1ll1l11lll_opy_
from bstack_utils.bstack1l1l111ll1_opy_ import bstack111lll1ll_opy_
from bstack_utils.bstack11ll111l11_opy_ import bstack1l11lllll_opy_, bstack11ll111111_opy_
from bstack_utils.bstack11l1l1111_opy_ import bstack1l111111ll_opy_
from bstack_utils.bstack11l111l1l1_opy_ import bstack11l11lll1l_opy_, bstack1ll11l1l1_opy_
from bstack_utils.bstack11111lll11_opy_ import bstack11111lll11_opy_
from bstack_utils.bstack1ll1l11ll1_opy_ import bstack11ll11ll1l_opy_
from bstack_utils.proxy import bstack1ll1111l1_opy_, bstack1111l1ll1_opy_, bstack11l1l11l11_opy_, bstack111l111l1_opy_
from bstack_utils.bstack1l11l111l1_opy_ import bstack111llll111_opy_
import bstack_utils.bstack11l11l11l1_opy_ as bstack11l1l1ll1_opy_
import bstack_utils.bstack11l1l1ll1l_opy_ as bstack1l1l1ll1l_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack1l11111ll_opy_ import bstack11ll1l11ll_opy_
from bstack_utils.bstack1lll1ll1l_opy_ import bstack11l11l1l_opy_
from bstack_utils.bstack11l1ll1l1l_opy_ import bstack1l11111l11_opy_
if os.getenv(bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡊࡒࡓࡐ࡙ࠧ੆")):
  cli.bstack111ll11lll_opy_()
else:
  os.environ[bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡋࡓࡔࡑࡓࠨੇ")] = bstack1ll11_opy_ (u"ࠧࡵࡴࡸࡩࠬੈ")
bstack1l1l11111_opy_ = bstack1ll11_opy_ (u"ࠨࠢࠣ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࠡࠢ࡬ࡪ࠭ࡶࡡࡨࡧࠣࡁࡂࡃࠠࡷࡱ࡬ࡨࠥ࠶ࠩࠡࡽ࡟ࡲࠥࠦࠠࡵࡴࡼࡿࡡࡴࠠࡤࡱࡱࡷࡹࠦࡦࡴࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࡢࠧࡧࡵ࡟ࠫ࠮ࡁ࡜࡯ࠢࠣࠤࠥࠦࡦࡴ࠰ࡤࡴࡵ࡫࡮ࡥࡈ࡬ࡰࡪ࡙ࡹ࡯ࡥࠫࡦࡸࡺࡡࡤ࡭ࡢࡴࡦࡺࡨ࠭ࠢࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡴࡤ࡯࡮ࡥࡧࡻ࠭ࠥ࠱ࠠࠣ࠼ࠥࠤ࠰ࠦࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡋࡕࡒࡒ࠳ࡶࡡࡳࡵࡨࠬ࠭ࡧࡷࡢ࡫ࡷࠤࡳ࡫ࡷࡑࡣࡪࡩ࠷࠴ࡥࡷࡣ࡯ࡹࡦࡺࡥࠩࠤࠫ࠭ࠥࡃ࠾ࠡࡽࢀࠦ࠱ࠦ࡜ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡩࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡉ࡫ࡴࡢ࡫࡯ࡷࠧࢃ࡜ࠨࠫࠬ࠭ࡠࠨࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠤࡠ࠭ࠥ࠱ࠠࠣ࠮࡟ࡠࡳࠨࠩ࡝ࡰࠣࠤࠥࠦࡽࡤࡣࡷࡧ࡭࠮ࡥࡹࠫࡾࡠࡳࠦࠠࠡࠢࢀࡠࡳࠦࠠࡾ࡞ࡱࠤࠥ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯ࠨ੉")
bstack11l11l1l11_opy_ = bstack1ll11_opy_ (u"ࠩ࡟ࡲ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬ࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴࡟࡟ࡲࡨࡵ࡮ࡴࡶࠣࡦࡸࡺࡡࡤ࡭ࡢࡧࡦࡶࡳࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠵ࡢࡢ࡮ࡤࡱࡱࡷࡹࠦࡰࡠ࡫ࡱࡨࡪࡾࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠵ࡡࡡࡴࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴ࡳ࡭࡫ࡦࡩ࠭࠶ࠬࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶࠭ࡡࡴࡣࡰࡰࡶࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭ࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ࠮ࡁ࡜࡯࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰ࠴ࡣࡩࡴࡲࡱ࡮ࡻ࡭࠯࡮ࡤࡹࡳࡩࡨࠡ࠿ࠣࡥࡸࡿ࡮ࡤࠢࠫࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵࠬࠤࡂࡄࠠࡼ࡞ࡱࡰࡪࡺࠠࡤࡣࡳࡷࡀࡢ࡮ࡵࡴࡼࠤࢀࡢ࡮ࡤࡣࡳࡷࠥࡃࠠࡋࡕࡒࡒ࠳ࡶࡡࡳࡵࡨࠬࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠫ࡟ࡲࠥࠦࡽࠡࡥࡤࡸࡨ࡮ࠨࡦࡺࠬࠤࢀࡢ࡮ࠡࠢࠣࠤࢂࡢ࡮ࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡤࡻࡦ࡯ࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰ࠴ࡣࡩࡴࡲࡱ࡮ࡻ࡭࠯ࡥࡲࡲࡳ࡫ࡣࡵࠪࡾࡠࡳࠦࠠࠡࠢࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹࡀࠠࡡࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠧࡿࡪࡴࡣࡰࡦࡨ࡙ࡗࡏࡃࡰ࡯ࡳࡳࡳ࡫࡮ࡵࠪࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡧࡦࡶࡳࠪࠫࢀࡤ࠱ࡢ࡮ࠡࠢࠣࠤ࠳࠴࠮࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹ࡜࡯ࠢࠣࢁ࠮ࡢ࡮ࡾ࡞ࡱ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࠨ੊")
from ._version import __version__
bstack1ll1lll111_opy_ = None
CONFIG = {}
bstack1l11ll1111_opy_ = {}
bstack1ll1l1l1l1_opy_ = {}
bstack11l1ll1l1_opy_ = None
bstack1lll1l1l11_opy_ = None
bstack11l1l111ll_opy_ = None
bstack1ll1l1lll_opy_ = -1
bstack1111llll1_opy_ = 0
bstack11l1l111l_opy_ = bstack111lll1l1l_opy_
bstack11l1llll1_opy_ = 1
bstack1l11lll11_opy_ = False
bstack111llll1l1_opy_ = False
bstack1l111llll_opy_ = bstack1ll11_opy_ (u"ࠪࠫੋ")
bstack1l1l1111l_opy_ = bstack1ll11_opy_ (u"ࠫࠬੌ")
bstack111l1l111_opy_ = False
bstack1lllll1l1l_opy_ = True
bstack1ll111l111_opy_ = bstack1ll11_opy_ (u"੍ࠬ࠭")
bstack1111l1l1l1_opy_ = []
bstack1l11l1l1l_opy_ = threading.Lock()
bstack11lllllll1_opy_ = threading.Lock()
bstack11l111111l_opy_ = bstack1ll11_opy_ (u"࠭ࠧ੎")
bstack1l1l11llll_opy_ = False
bstack1l11111lll_opy_ = None
bstack111l1ll11_opy_ = None
bstack11111l11l_opy_ = None
bstack1lllll11l1_opy_ = -1
bstack1ll1111111_opy_ = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"ࠧࡿࠩ੏")), bstack1ll11_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ੐"), bstack1ll11_opy_ (u"ࠩ࠱ࡶࡴࡨ࡯ࡵ࠯ࡵࡩࡵࡵࡲࡵ࠯࡫ࡩࡱࡶࡥࡳ࠰࡭ࡷࡴࡴࠧੑ"))
bstack1l11lll1ll_opy_ = 0
bstack11ll1111l1_opy_ = 0
bstack11llll11l_opy_ = []
bstack1ll11llll1_opy_ = []
bstack1l1l111l11_opy_ = []
bstack1llll11l11_opy_ = []
bstack111l111ll1_opy_ = bstack1ll11_opy_ (u"ࠪࠫ੒")
bstack11lll1l1ll_opy_ = bstack1ll11_opy_ (u"ࠫࠬ੓")
bstack1ll11lll11_opy_ = False
bstack1ll111l11_opy_ = False
bstack11llll1l1l_opy_ = {}
bstack11l1ll1lll_opy_ = None
bstack1111l1l11_opy_ = None
bstack11ll11lll_opy_ = None
bstack1111l1l11l_opy_ = None
bstack11llll1ll_opy_ = None
bstack11111llll_opy_ = None
bstack1ll111ll11_opy_ = None
bstack1111lll111_opy_ = None
bstack1ll11l11l1_opy_ = None
bstack1l11ll11l_opy_ = None
bstack1ll1l1ll1l_opy_ = None
bstack1l11llll1_opy_ = None
bstack1111ll11l1_opy_ = None
bstack11ll1llll1_opy_ = None
bstack1lllllllll_opy_ = None
bstack1l11l1ll1l_opy_ = None
bstack11l1ll111l_opy_ = None
bstack1ll1l1ll11_opy_ = None
bstack11l1lllll1_opy_ = None
bstack11111ll11_opy_ = None
bstack1ll1l1111_opy_ = None
bstack1ll1lll1l1_opy_ = None
bstack11111lll1_opy_ = None
thread_local = threading.local()
bstack111l1111ll_opy_ = False
bstack1ll11l1ll1_opy_ = bstack1ll11_opy_ (u"ࠧࠨ੔")
logger = bstack1l1l1l1111_opy_.get_logger(__name__, bstack11l1l111l_opy_)
bstack1111ll11_opy_ = Config.bstack1llll11l1_opy_()
percy = bstack1l1l11l1l_opy_()
bstack1l1ll111l_opy_ = bstack1l1ll1llll_opy_()
bstack1llll1l111_opy_ = bstack11ll11l1_opy_()
def bstack11l111l11_opy_():
  global CONFIG
  global bstack1ll11lll11_opy_
  global bstack1111ll11_opy_
  testContextOptions = bstack1l1l1l1ll1_opy_(CONFIG)
  if bstack111lll111l_opy_(CONFIG):
    if (bstack1ll11_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ੕") in testContextOptions and str(testContextOptions[bstack1ll11_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ੖")]).lower() == bstack1ll11_opy_ (u"ࠨࡶࡵࡹࡪ࠭੗")):
      bstack1ll11lll11_opy_ = True
    bstack1111ll11_opy_.bstack1l111ll1l_opy_(testContextOptions.get(bstack1ll11_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭੘"), False))
  else:
    bstack1ll11lll11_opy_ = True
    bstack1111ll11_opy_.bstack1l111ll1l_opy_(True)
def bstack111l11l111_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1llll1l1l1_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack111l1llll1_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1ll11_opy_ (u"ࠥ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡧࡴࡴࡦࡪࡩࡩ࡭ࡱ࡫ࠢਖ਼") == args[i].lower() or bstack1ll11_opy_ (u"ࠦ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡯ࡨ࡬࡫ࠧਗ਼") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1ll111l111_opy_
      bstack1ll111l111_opy_ += bstack1ll11_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡉ࡯࡯ࡨ࡬࡫ࡋ࡯࡬ࡦࠢࠪਜ਼") + shlex.quote(path)
      return path
  return None
bstack1l1l11l111_opy_ = re.compile(bstack1ll11_opy_ (u"ࡸࠢ࠯ࠬࡂࡠࠩࢁࠨ࠯ࠬࡂ࠭ࢂ࠴ࠪࡀࠤੜ"))
def bstack1l11llll1l_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l1l11l111_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1ll11_opy_ (u"ࠢࠥࡽࠥ੝") + group + bstack1ll11_opy_ (u"ࠣࡿࠥਫ਼"), os.environ.get(group))
  return value
def bstack1ll111lll1_opy_():
  global bstack11111lll1_opy_
  if bstack11111lll1_opy_ is None:
        bstack11111lll1_opy_ = bstack111l1llll1_opy_()
  bstack111l11ll1_opy_ = bstack11111lll1_opy_
  if bstack111l11ll1_opy_ and os.path.exists(os.path.abspath(bstack111l11ll1_opy_)):
    fileName = bstack111l11ll1_opy_
  if bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࡠࡈࡌࡐࡊ࠭੟") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧ੠")])) and not bstack1ll11_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࠭੡") in locals():
    fileName = os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆࠩ੢")]
  if bstack1ll11_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨ੣") in locals():
    bstack1lll111_opy_ = os.path.abspath(fileName)
  else:
    bstack1lll111_opy_ = bstack1ll11_opy_ (u"ࠧࠨ੤")
  bstack1l1lllllll_opy_ = os.getcwd()
  bstack11lll1111l_opy_ = bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫ੥")
  bstack11111ll11l_opy_ = bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡤࡱࡱ࠭੦")
  while (not os.path.exists(bstack1lll111_opy_)) and bstack1l1lllllll_opy_ != bstack1ll11_opy_ (u"ࠥࠦ੧"):
    bstack1lll111_opy_ = os.path.join(bstack1l1lllllll_opy_, bstack11lll1111l_opy_)
    if not os.path.exists(bstack1lll111_opy_):
      bstack1lll111_opy_ = os.path.join(bstack1l1lllllll_opy_, bstack11111ll11l_opy_)
    if bstack1l1lllllll_opy_ != os.path.dirname(bstack1l1lllllll_opy_):
      bstack1l1lllllll_opy_ = os.path.dirname(bstack1l1lllllll_opy_)
    else:
      bstack1l1lllllll_opy_ = bstack1ll11_opy_ (u"ࠦࠧ੨")
  bstack11111lll1_opy_ = bstack1lll111_opy_ if os.path.exists(bstack1lll111_opy_) else None
  return bstack11111lll1_opy_
def bstack1ll11lll1l_opy_(config):
    if bstack1ll11_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠬ੩") in config:
      config[bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ੪")] = config[bstack1ll11_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧ੫")]
    if bstack1ll11_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࡐࡲࡷ࡭ࡴࡴࡳࠨ੬") in config:
      config[bstack1ll11_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭੭")] = config[bstack1ll11_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࡒࡴࡹ࡯࡯࡯ࡵࠪ੮")]
def bstack11llll111l_opy_():
  bstack1lll111_opy_ = bstack1ll111lll1_opy_()
  if not os.path.exists(bstack1lll111_opy_):
    bstack11l11l11ll_opy_(
      bstack1111l1l1l_opy_.format(os.getcwd()))
  try:
    with open(bstack1lll111_opy_, bstack1ll11_opy_ (u"ࠫࡷ࠭੯")) as stream:
      yaml.add_implicit_resolver(bstack1ll11_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨੰ"), bstack1l1l11l111_opy_)
      yaml.add_constructor(bstack1ll11_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢੱ"), bstack1l11llll1l_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1ll11lll1l_opy_(config)
      return config
  except:
    with open(bstack1lll111_opy_, bstack1ll11_opy_ (u"ࠧࡳࠩੲ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1ll11lll1l_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack11l11l11ll_opy_(bstack11ll11ll11_opy_.format(str(exc)))
def bstack1llll111ll_opy_(config):
  bstack111lll11l_opy_ = bstack11ll11l1l_opy_(config)
  for option in list(bstack111lll11l_opy_):
    if option.lower() in bstack111llll11_opy_ and option != bstack111llll11_opy_[option.lower()]:
      bstack111lll11l_opy_[bstack111llll11_opy_[option.lower()]] = bstack111lll11l_opy_[option]
      del bstack111lll11l_opy_[option]
  return config
def bstack1l1l1ll11_opy_():
  global bstack1ll1l1l1l1_opy_
  for key, bstack1l111ll1ll_opy_ in bstack111ll11ll_opy_.items():
    if isinstance(bstack1l111ll1ll_opy_, list):
      for var in bstack1l111ll1ll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1ll1l1l1l1_opy_[key] = os.environ[var]
          break
    elif bstack1l111ll1ll_opy_ in os.environ and os.environ[bstack1l111ll1ll_opy_] and str(os.environ[bstack1l111ll1ll_opy_]).strip():
      bstack1ll1l1l1l1_opy_[key] = os.environ[bstack1l111ll1ll_opy_]
  if bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪੳ") in os.environ:
    bstack1ll1l1l1l1_opy_[bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ੴ")] = {}
    bstack1ll1l1l1l1_opy_[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧੵ")][bstack1ll11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੶")] = os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ੷")]
def bstack11l11l1ll1_opy_():
  global bstack1l11ll1111_opy_
  global bstack1ll111l111_opy_
  bstack111lllllll_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack1ll11_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ੸").lower() == val.lower():
      bstack1l11ll1111_opy_[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ੹")] = {}
      bstack1l11ll1111_opy_[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ੺")][bstack1ll11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ੻")] = sys.argv[idx + 1]
      bstack111lllllll_opy_.extend([idx, idx + 1])
      break
  for key, bstack11lllll11l_opy_ in bstack11l111llll_opy_.items():
    if isinstance(bstack11lllll11l_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack11lllll11l_opy_:
          if bstack1ll11_opy_ (u"ࠪ࠱࠲࠭੼") + var.lower() == val.lower() and key not in bstack1l11ll1111_opy_:
            bstack1l11ll1111_opy_[key] = sys.argv[idx + 1]
            bstack1ll111l111_opy_ += bstack1ll11_opy_ (u"ࠫࠥ࠳࠭ࠨ੽") + var + bstack1ll11_opy_ (u"ࠬࠦࠧ੾") + shlex.quote(sys.argv[idx + 1])
            bstack111lllllll_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack1ll11_opy_ (u"࠭࠭࠮ࠩ੿") + bstack11lllll11l_opy_.lower() == val.lower() and key not in bstack1l11ll1111_opy_:
          bstack1l11ll1111_opy_[key] = sys.argv[idx + 1]
          bstack1ll111l111_opy_ += bstack1ll11_opy_ (u"ࠧࠡ࠯࠰ࠫ઀") + bstack11lllll11l_opy_ + bstack1ll11_opy_ (u"ࠨࠢࠪઁ") + shlex.quote(sys.argv[idx + 1])
          bstack111lllllll_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack111lllllll_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack1l1lll111_opy_(config):
  bstack1lll1ll111_opy_ = config.keys()
  for bstack1lll11l1l1_opy_, bstack11lll111ll_opy_ in bstack111ll1111_opy_.items():
    if bstack11lll111ll_opy_ in bstack1lll1ll111_opy_:
      config[bstack1lll11l1l1_opy_] = config[bstack11lll111ll_opy_]
      del config[bstack11lll111ll_opy_]
  for bstack1lll11l1l1_opy_, bstack11lll111ll_opy_ in bstack1lll1l111_opy_.items():
    if isinstance(bstack11lll111ll_opy_, list):
      for bstack1lll11ll1_opy_ in bstack11lll111ll_opy_:
        if bstack1lll11ll1_opy_ in bstack1lll1ll111_opy_:
          config[bstack1lll11l1l1_opy_] = config[bstack1lll11ll1_opy_]
          del config[bstack1lll11ll1_opy_]
          break
    elif bstack11lll111ll_opy_ in bstack1lll1ll111_opy_:
      config[bstack1lll11l1l1_opy_] = config[bstack11lll111ll_opy_]
      del config[bstack11lll111ll_opy_]
  for bstack1lll11ll1_opy_ in list(config):
    for bstack11l1ll1l11_opy_ in bstack1111ll1ll1_opy_:
      if bstack1lll11ll1_opy_.lower() == bstack11l1ll1l11_opy_.lower() and bstack1lll11ll1_opy_ != bstack11l1ll1l11_opy_:
        config[bstack11l1ll1l11_opy_] = config[bstack1lll11ll1_opy_]
        del config[bstack1lll11ll1_opy_]
  bstack1111ll1lll_opy_ = [{}]
  if not config.get(bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬં")):
    config[bstack1ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ઃ")] = [{}]
  bstack1111ll1lll_opy_ = config[bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ઄")]
  for platform in bstack1111ll1lll_opy_:
    for bstack1lll11ll1_opy_ in list(platform):
      for bstack11l1ll1l11_opy_ in bstack1111ll1ll1_opy_:
        if bstack1lll11ll1_opy_.lower() == bstack11l1ll1l11_opy_.lower() and bstack1lll11ll1_opy_ != bstack11l1ll1l11_opy_:
          platform[bstack11l1ll1l11_opy_] = platform[bstack1lll11ll1_opy_]
          del platform[bstack1lll11ll1_opy_]
  for bstack1lll11l1l1_opy_, bstack11lll111ll_opy_ in bstack1lll1l111_opy_.items():
    for platform in bstack1111ll1lll_opy_:
      if isinstance(bstack11lll111ll_opy_, list):
        for bstack1lll11ll1_opy_ in bstack11lll111ll_opy_:
          if bstack1lll11ll1_opy_ in platform:
            platform[bstack1lll11l1l1_opy_] = platform[bstack1lll11ll1_opy_]
            del platform[bstack1lll11ll1_opy_]
            break
      elif bstack11lll111ll_opy_ in platform:
        platform[bstack1lll11l1l1_opy_] = platform[bstack11lll111ll_opy_]
        del platform[bstack11lll111ll_opy_]
  for bstack1ll11l1l11_opy_ in bstack1l1111l1ll_opy_:
    if bstack1ll11l1l11_opy_ in config:
      if not bstack1l1111l1ll_opy_[bstack1ll11l1l11_opy_] in config:
        config[bstack1l1111l1ll_opy_[bstack1ll11l1l11_opy_]] = {}
      config[bstack1l1111l1ll_opy_[bstack1ll11l1l11_opy_]].update(config[bstack1ll11l1l11_opy_])
      del config[bstack1ll11l1l11_opy_]
  for platform in bstack1111ll1lll_opy_:
    for bstack1ll11l1l11_opy_ in bstack1l1111l1ll_opy_:
      if bstack1ll11l1l11_opy_ in list(platform):
        if not bstack1l1111l1ll_opy_[bstack1ll11l1l11_opy_] in platform:
          platform[bstack1l1111l1ll_opy_[bstack1ll11l1l11_opy_]] = {}
        platform[bstack1l1111l1ll_opy_[bstack1ll11l1l11_opy_]].update(platform[bstack1ll11l1l11_opy_])
        del platform[bstack1ll11l1l11_opy_]
  config = bstack1llll111ll_opy_(config)
  return config
def bstack1lll111111_opy_(config):
  global bstack1l1l1111l_opy_
  bstack1l1llll1l_opy_ = False
  if bstack1ll11_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩઅ") in config and str(config[bstack1ll11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪઆ")]).lower() != bstack1ll11_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ઇ"):
    if bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬઈ") not in config or str(config[bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ઉ")]).lower() == bstack1ll11_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩઊ"):
      config[bstack1ll11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪઋ")] = False
    else:
      bstack111l1l11ll_opy_ = bstack1lllll111l_opy_()
      if bstack1ll11_opy_ (u"ࠬ࡯ࡳࡕࡴ࡬ࡥࡱࡍࡲࡪࡦࠪઌ") in bstack111l1l11ll_opy_:
        if not bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪઍ") in config:
          config[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ઎")] = {}
        config[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬએ")][bstack1ll11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫઐ")] = bstack1ll11_opy_ (u"ࠪࡥࡹࡹ࠭ࡳࡧࡳࡩࡦࡺࡥࡳࠩઑ")
        bstack1l1llll1l_opy_ = True
        bstack1l1l1111l_opy_ = config[bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ઒")].get(bstack1ll11_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઓ"))
  if bstack111lll111l_opy_(config) and bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪઔ") in config and str(config[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫક")]).lower() != bstack1ll11_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧખ") and not bstack1l1llll1l_opy_:
    if not bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ગ") in config:
      config[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઘ")] = {}
    if not config[bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨઙ")].get(bstack1ll11_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩચ")) and not bstack1ll11_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨછ") in config[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫજ")]:
      bstack1lll1111_opy_ = datetime.datetime.now()
      bstack11l1lllll_opy_ = bstack1lll1111_opy_.strftime(bstack1ll11_opy_ (u"ࠨࠧࡧࡣࠪࡨ࡟ࠦࡊࠨࡑࠬઝ"))
      hostname = socket.gethostname()
      bstack1l11l1111l_opy_ = bstack1ll11_opy_ (u"ࠩࠪઞ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1ll11_opy_ (u"ࠪࡿࢂࡥࡻࡾࡡࡾࢁࠬટ").format(bstack11l1lllll_opy_, hostname, bstack1l11l1111l_opy_)
      config[bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨઠ")][bstack1ll11_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧડ")] = identifier
    bstack1l1l1111l_opy_ = config[bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪઢ")].get(bstack1ll11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩણ"))
  return config
def bstack11111l1l1l_opy_():
  bstack1l11llll11_opy_ =  bstack1l11l1l11l_opy_()[bstack1ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠧત")]
  return bstack1l11llll11_opy_ if bstack1l11llll11_opy_ else -1
def bstack111ll1ll1_opy_(bstack1l11llll11_opy_):
  global CONFIG
  if not bstack1ll11_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫથ") in CONFIG[bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬદ")]:
    return
  CONFIG[bstack1ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ધ")] = CONFIG[bstack1ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧન")].replace(
    bstack1ll11_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨ઩"),
    str(bstack1l11llll11_opy_)
  )
def bstack1l1llll1l1_opy_():
  global CONFIG
  if not bstack1ll11_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭પ") in CONFIG[bstack1ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪફ")]:
    return
  bstack1lll1111_opy_ = datetime.datetime.now()
  bstack11l1lllll_opy_ = bstack1lll1111_opy_.strftime(bstack1ll11_opy_ (u"ࠩࠨࡨ࠲ࠫࡢ࠮ࠧࡋ࠾ࠪࡓࠧબ"))
  CONFIG[bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬભ")] = CONFIG[bstack1ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭મ")].replace(
    bstack1ll11_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫય"),
    bstack11l1lllll_opy_
  )
def bstack11l11ll111_opy_():
  global CONFIG
  if bstack1ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨર") in CONFIG and not bool(CONFIG[bstack1ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઱")]):
    del CONFIG[bstack1ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪલ")]
    return
  if not bstack1ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫળ") in CONFIG:
    CONFIG[bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ઴")] = bstack1ll11_opy_ (u"ࠫࠨࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧવ")
  if bstack1ll11_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫશ") in CONFIG[bstack1ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨષ")]:
    bstack1l1llll1l1_opy_()
    os.environ[bstack1ll11_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫસ")] = CONFIG[bstack1ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪહ")]
  if not bstack1ll11_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫ઺") in CONFIG[bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ઻")]:
    return
  bstack1l11llll11_opy_ = bstack1ll11_opy_ (u"઼ࠫࠬ")
  bstack11ll1ll1ll_opy_ = bstack11111l1l1l_opy_()
  if bstack11ll1ll1ll_opy_ != -1:
    bstack1l11llll11_opy_ = bstack1ll11_opy_ (u"ࠬࡉࡉࠡࠩઽ") + str(bstack11ll1ll1ll_opy_)
  if bstack1l11llll11_opy_ == bstack1ll11_opy_ (u"࠭ࠧા"):
    bstack11l1ll11l1_opy_ = bstack1l1l1l1l11_opy_(CONFIG[bstack1ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪિ")])
    if bstack11l1ll11l1_opy_ != -1:
      bstack1l11llll11_opy_ = str(bstack11l1ll11l1_opy_)
  if bstack1l11llll11_opy_:
    bstack111ll1ll1_opy_(bstack1l11llll11_opy_)
    os.environ[bstack1ll11_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬી")] = CONFIG[bstack1ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫુ")]
def bstack1lll1l111l_opy_(bstack111ll1l1l1_opy_, bstack1l111ll111_opy_, path):
  json_data = {
    bstack1ll11_opy_ (u"ࠪ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૂ"): bstack1l111ll111_opy_
  }
  if os.path.exists(path):
    bstack11l11111l1_opy_ = json.load(open(path, bstack1ll11_opy_ (u"ࠫࡷࡨࠧૃ")))
  else:
    bstack11l11111l1_opy_ = {}
  bstack11l11111l1_opy_[bstack111ll1l1l1_opy_] = json_data
  with open(path, bstack1ll11_opy_ (u"ࠧࡽࠫࠣૄ")) as outfile:
    json.dump(bstack11l11111l1_opy_, outfile)
def bstack1l1l1l1l11_opy_(bstack111ll1l1l1_opy_):
  bstack111ll1l1l1_opy_ = str(bstack111ll1l1l1_opy_)
  bstack1l1llll11_opy_ = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"࠭ࡾࠨૅ")), bstack1ll11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ૆"))
  try:
    if not os.path.exists(bstack1l1llll11_opy_):
      os.makedirs(bstack1l1llll11_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"ࠨࢀࠪે")), bstack1ll11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩૈ"), bstack1ll11_opy_ (u"ࠪ࠲ࡧࡻࡩ࡭ࡦ࠰ࡲࡦࡳࡥ࠮ࡥࡤࡧ࡭࡫࠮࡫ࡵࡲࡲࠬૉ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1ll11_opy_ (u"ࠫࡼ࠭૊")):
        pass
      with open(file_path, bstack1ll11_opy_ (u"ࠧࡽࠫࠣો")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1ll11_opy_ (u"࠭ࡲࠨૌ")) as bstack1ll1ll1ll1_opy_:
      bstack1l1l1ll1l1_opy_ = json.load(bstack1ll1ll1ll1_opy_)
    if bstack111ll1l1l1_opy_ in bstack1l1l1ll1l1_opy_:
      bstack11ll1l1ll_opy_ = bstack1l1l1ll1l1_opy_[bstack111ll1l1l1_opy_][bstack1ll11_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵ્ࠫ")]
      bstack1l1l1lllll_opy_ = int(bstack11ll1l1ll_opy_) + 1
      bstack1lll1l111l_opy_(bstack111ll1l1l1_opy_, bstack1l1l1lllll_opy_, file_path)
      return bstack1l1l1lllll_opy_
    else:
      bstack1lll1l111l_opy_(bstack111ll1l1l1_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack111l111l1l_opy_.format(str(e)))
    return -1
def bstack11lll11111_opy_(config):
  if not config[bstack1ll11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ૎")] or not config[bstack1ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ૏")]:
    return True
  else:
    return False
def bstack11ll111l1_opy_(config, index=0):
  global bstack111l1l111_opy_
  bstack1ll1lll1l_opy_ = {}
  caps = bstack11l11lll11_opy_ + bstack11lll111l1_opy_
  if config.get(bstack1ll11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧૐ"), False):
    bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨ૑")] = True
    bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ૒")] = config.get(bstack1ll11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ૓"), {})
  if bstack111l1l111_opy_:
    caps += bstack1111l11ll_opy_
  for key in config:
    if key in caps + [bstack1ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૔")]:
      continue
    bstack1ll1lll1l_opy_[key] = config[key]
  if bstack1ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૕") in config:
    for bstack1ll1ll11l1_opy_ in config[bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૖")][index]:
      if bstack1ll1ll11l1_opy_ in caps:
        continue
      bstack1ll1lll1l_opy_[bstack1ll1ll11l1_opy_] = config[bstack1ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૗")][index][bstack1ll1ll11l1_opy_]
  bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭૘")] = socket.gethostname()
  if bstack1ll11_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭૙") in bstack1ll1lll1l_opy_:
    del (bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧ૚")])
  return bstack1ll1lll1l_opy_
def bstack11l1llllll_opy_(config):
  global bstack111l1l111_opy_
  bstack11ll11l11_opy_ = {}
  caps = bstack11lll111l1_opy_
  if bstack111l1l111_opy_:
    caps += bstack1111l11ll_opy_
  for key in caps:
    if key in config:
      bstack11ll11l11_opy_[key] = config[key]
  return bstack11ll11l11_opy_
def bstack111ll1l11_opy_(bstack1ll1lll1l_opy_, bstack11ll11l11_opy_):
  bstack1l11ll111_opy_ = {}
  for key in bstack1ll1lll1l_opy_.keys():
    if key in bstack111ll1111_opy_:
      bstack1l11ll111_opy_[bstack111ll1111_opy_[key]] = bstack1ll1lll1l_opy_[key]
    else:
      bstack1l11ll111_opy_[key] = bstack1ll1lll1l_opy_[key]
  for key in bstack11ll11l11_opy_:
    if key in bstack111ll1111_opy_:
      bstack1l11ll111_opy_[bstack111ll1111_opy_[key]] = bstack11ll11l11_opy_[key]
    else:
      bstack1l11ll111_opy_[key] = bstack11ll11l11_opy_[key]
  return bstack1l11ll111_opy_
def bstack111l1lllll_opy_(config, index=0):
  global bstack111l1l111_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11lllll1l1_opy_ = bstack1l1l1lll11_opy_(bstack11l111lll1_opy_, config, logger)
  bstack11ll11l11_opy_ = bstack11l1llllll_opy_(config)
  bstack1l111lllll_opy_ = bstack11lll111l1_opy_
  bstack1l111lllll_opy_ += bstack1111ll1ll_opy_
  bstack11ll11l11_opy_ = update(bstack11ll11l11_opy_, bstack11lllll1l1_opy_)
  if bstack111l1l111_opy_:
    bstack1l111lllll_opy_ += bstack1111l11ll_opy_
  if bstack1ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૛") in config:
    if bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭૜") in config[bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૝")][index]:
      caps[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ૞")] = config[bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૟")][index][bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪૠ")]
    if bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧૡ") in config[bstack1ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪૢ")][index]:
      caps[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩૣ")] = str(config[bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૤")][index][bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ૥")])
    bstack1l1ll1l1l_opy_ = bstack1l1l1lll11_opy_(bstack11l111lll1_opy_, config[bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૦")][index], logger)
    bstack1l111lllll_opy_ += list(bstack1l1ll1l1l_opy_.keys())
    for bstack1l1llll11l_opy_ in bstack1l111lllll_opy_:
      if bstack1l1llll11l_opy_ in config[bstack1ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૧")][index]:
        if bstack1l1llll11l_opy_ == bstack1ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ૨"):
          try:
            bstack1l1ll1l1l_opy_[bstack1l1llll11l_opy_] = str(config[bstack1ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૩")][index][bstack1l1llll11l_opy_] * 1.0)
          except:
            bstack1l1ll1l1l_opy_[bstack1l1llll11l_opy_] = str(config[bstack1ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૪")][index][bstack1l1llll11l_opy_])
        else:
          bstack1l1ll1l1l_opy_[bstack1l1llll11l_opy_] = config[bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૫")][index][bstack1l1llll11l_opy_]
        del (config[bstack1ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૬")][index][bstack1l1llll11l_opy_])
    bstack11ll11l11_opy_ = update(bstack11ll11l11_opy_, bstack1l1ll1l1l_opy_)
  bstack1ll1lll1l_opy_ = bstack11ll111l1_opy_(config, index)
  for bstack1lll11ll1_opy_ in bstack11lll111l1_opy_ + list(bstack11lllll1l1_opy_.keys()):
    if bstack1lll11ll1_opy_ in bstack1ll1lll1l_opy_:
      bstack11ll11l11_opy_[bstack1lll11ll1_opy_] = bstack1ll1lll1l_opy_[bstack1lll11ll1_opy_]
      del (bstack1ll1lll1l_opy_[bstack1lll11ll1_opy_])
  if bstack1lll111lll_opy_(config):
    bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ૭")] = True
    caps.update(bstack11ll11l11_opy_)
    caps[bstack1ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭૮")] = bstack1ll1lll1l_opy_
  else:
    bstack1ll1lll1l_opy_[bstack1ll11_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭૯")] = False
    caps.update(bstack111ll1l11_opy_(bstack1ll1lll1l_opy_, bstack11ll11l11_opy_))
    if bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ૰") in caps:
      caps[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ૱")] = caps[bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ૲")]
      del (caps[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ૳")])
    if bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ૴") in caps:
      caps[bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ૵")] = caps[bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ૶")]
      del (caps[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ૷")])
  return caps
def bstack1ll1ll111l_opy_():
  global bstack11l111111l_opy_
  global CONFIG
  if bstack1llll1l1l1_opy_() <= version.parse(bstack1ll11_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨ૸")):
    if bstack11l111111l_opy_ != bstack1ll11_opy_ (u"ࠩࠪૹ"):
      return bstack1ll11_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦૺ") + bstack11l111111l_opy_ + bstack1ll11_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣૻ")
    return bstack1l1l1l111_opy_
  if bstack11l111111l_opy_ != bstack1ll11_opy_ (u"ࠬ࠭ૼ"):
    return bstack1ll11_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣ૽") + bstack11l111111l_opy_ + bstack1ll11_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣ૾")
  return bstack1lll1l1l1l_opy_
def bstack1lll111l1_opy_(options):
  return hasattr(options, bstack1ll11_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩ૿"))
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
def bstack1ll11ll11_opy_(options, bstack1ll11llll_opy_):
  for bstack11lllll11_opy_ in bstack1ll11llll_opy_:
    if bstack11lllll11_opy_ in [bstack1ll11_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ଀"), bstack1ll11_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧଁ")]:
      continue
    if bstack11lllll11_opy_ in options._experimental_options:
      options._experimental_options[bstack11lllll11_opy_] = update(options._experimental_options[bstack11lllll11_opy_],
                                                         bstack1ll11llll_opy_[bstack11lllll11_opy_])
    else:
      options.add_experimental_option(bstack11lllll11_opy_, bstack1ll11llll_opy_[bstack11lllll11_opy_])
  if bstack1ll11_opy_ (u"ࠫࡦࡸࡧࡴࠩଂ") in bstack1ll11llll_opy_:
    for arg in bstack1ll11llll_opy_[bstack1ll11_opy_ (u"ࠬࡧࡲࡨࡵࠪଃ")]:
      options.add_argument(arg)
    del (bstack1ll11llll_opy_[bstack1ll11_opy_ (u"࠭ࡡࡳࡩࡶࠫ଄")])
  if bstack1ll11_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫଅ") in bstack1ll11llll_opy_:
    for ext in bstack1ll11llll_opy_[bstack1ll11_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬଆ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1ll11llll_opy_[bstack1ll11_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ଇ")])
def bstack1l1llllll_opy_(options, bstack11lll11l1_opy_):
  if bstack1ll11_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩଈ") in bstack11lll11l1_opy_:
    for bstack1ll1l1111l_opy_ in bstack11lll11l1_opy_[bstack1ll11_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪଉ")]:
      if bstack1ll1l1111l_opy_ in options._preferences:
        options._preferences[bstack1ll1l1111l_opy_] = update(options._preferences[bstack1ll1l1111l_opy_], bstack11lll11l1_opy_[bstack1ll11_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫଊ")][bstack1ll1l1111l_opy_])
      else:
        options.set_preference(bstack1ll1l1111l_opy_, bstack11lll11l1_opy_[bstack1ll11_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬଋ")][bstack1ll1l1111l_opy_])
  if bstack1ll11_opy_ (u"ࠧࡢࡴࡪࡷࠬଌ") in bstack11lll11l1_opy_:
    for arg in bstack11lll11l1_opy_[bstack1ll11_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭଍")]:
      options.add_argument(arg)
def bstack1lll1l1111_opy_(options, bstack1l11ll1l11_opy_):
  if bstack1ll11_opy_ (u"ࠩࡺࡩࡧࡼࡩࡦࡹࠪ଎") in bstack1l11ll1l11_opy_:
    options.use_webview(bool(bstack1l11ll1l11_opy_[bstack1ll11_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫଏ")]))
  bstack1ll11ll11_opy_(options, bstack1l11ll1l11_opy_)
def bstack1ll111lll_opy_(options, bstack1lll1ll1l1_opy_):
  for bstack1ll11l1ll_opy_ in bstack1lll1ll1l1_opy_:
    if bstack1ll11l1ll_opy_ in [bstack1ll11_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨଐ"), bstack1ll11_opy_ (u"ࠬࡧࡲࡨࡵࠪ଑")]:
      continue
    options.set_capability(bstack1ll11l1ll_opy_, bstack1lll1ll1l1_opy_[bstack1ll11l1ll_opy_])
  if bstack1ll11_opy_ (u"࠭ࡡࡳࡩࡶࠫ଒") in bstack1lll1ll1l1_opy_:
    for arg in bstack1lll1ll1l1_opy_[bstack1ll11_opy_ (u"ࠧࡢࡴࡪࡷࠬଓ")]:
      options.add_argument(arg)
  if bstack1ll11_opy_ (u"ࠨࡶࡨࡧ࡭ࡴ࡯࡭ࡱࡪࡽࡕࡸࡥࡷ࡫ࡨࡻࠬଔ") in bstack1lll1ll1l1_opy_:
    options.bstack1l1llll1ll_opy_(bool(bstack1lll1ll1l1_opy_[bstack1ll11_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭କ")]))
def bstack1l1l1lll1l_opy_(options, bstack1l1l1l1ll_opy_):
  for bstack11l11l1l1_opy_ in bstack1l1l1l1ll_opy_:
    if bstack11l11l1l1_opy_ in [bstack1ll11_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧଖ"), bstack1ll11_opy_ (u"ࠫࡦࡸࡧࡴࠩଗ")]:
      continue
    options._options[bstack11l11l1l1_opy_] = bstack1l1l1l1ll_opy_[bstack11l11l1l1_opy_]
  if bstack1ll11_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩଘ") in bstack1l1l1l1ll_opy_:
    for bstack1111l111ll_opy_ in bstack1l1l1l1ll_opy_[bstack1ll11_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪଙ")]:
      options.bstack111l1111l_opy_(
        bstack1111l111ll_opy_, bstack1l1l1l1ll_opy_[bstack1ll11_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଚ")][bstack1111l111ll_opy_])
  if bstack1ll11_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଛ") in bstack1l1l1l1ll_opy_:
    for arg in bstack1l1l1l1ll_opy_[bstack1ll11_opy_ (u"ࠩࡤࡶ࡬ࡹࠧଜ")]:
      options.add_argument(arg)
def bstack1111l1lll1_opy_(options, caps):
  if not hasattr(options, bstack1ll11_opy_ (u"ࠪࡏࡊ࡟ࠧଝ")):
    return
  if options.KEY == bstack1ll11_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩଞ"):
    options = bstack11l11lll_opy_.bstack1l1111l11_opy_(bstack111l11l1l1_opy_=options, config=CONFIG)
  if options.KEY == bstack1ll11_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪଟ") and options.KEY in caps:
    bstack1ll11ll11_opy_(options, caps[bstack1ll11_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫଠ")])
  elif options.KEY == bstack1ll11_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬଡ") and options.KEY in caps:
    bstack1l1llllll_opy_(options, caps[bstack1ll11_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ଢ")])
  elif options.KEY == bstack1ll11_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪଣ") and options.KEY in caps:
    bstack1ll111lll_opy_(options, caps[bstack1ll11_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫତ")])
  elif options.KEY == bstack1ll11_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬଥ") and options.KEY in caps:
    bstack1lll1l1111_opy_(options, caps[bstack1ll11_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ଦ")])
  elif options.KEY == bstack1ll11_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬଧ") and options.KEY in caps:
    bstack1l1l1lll1l_opy_(options, caps[bstack1ll11_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ନ")])
def bstack1ll1l11111_opy_(caps):
  global bstack111l1l111_opy_
  if isinstance(os.environ.get(bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ଩")), str):
    bstack111l1l111_opy_ = eval(os.getenv(bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪପ")))
  if bstack111l1l111_opy_:
    if bstack111l11l111_opy_() < version.parse(bstack1ll11_opy_ (u"ࠪ࠶࠳࠹࠮࠱ࠩଫ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1ll11_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫବ")
    if bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪଭ") in caps:
      browser = caps[bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫମ")]
    elif bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨଯ") in caps:
      browser = caps[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩର")]
    browser = str(browser).lower()
    if browser == bstack1ll11_opy_ (u"ࠩ࡬ࡴ࡭ࡵ࡮ࡦࠩ଱") or browser == bstack1ll11_opy_ (u"ࠪ࡭ࡵࡧࡤࠨଲ"):
      browser = bstack1ll11_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫଳ")
    if browser == bstack1ll11_opy_ (u"ࠬࡹࡡ࡮ࡵࡸࡲ࡬࠭଴"):
      browser = bstack1ll11_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ଵ")
    if browser not in [bstack1ll11_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧଶ"), bstack1ll11_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭ଷ"), bstack1ll11_opy_ (u"ࠩ࡬ࡩࠬସ"), bstack1ll11_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪହ"), bstack1ll11_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬ଺")]:
      return None
    try:
      package = bstack1ll11_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡿࢂ࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧ଻").format(browser)
      name = bstack1ll11_opy_ (u"࠭ࡏࡱࡶ࡬ࡳࡳࡹ଼ࠧ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1lll111l1_opy_(options):
        return None
      for bstack1lll11ll1_opy_ in caps.keys():
        options.set_capability(bstack1lll11ll1_opy_, caps[bstack1lll11ll1_opy_])
      bstack1111l1lll1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack11ll1l11l1_opy_(options, bstack1111ll1l11_opy_):
  if not bstack1lll111l1_opy_(options):
    return
  for bstack1lll11ll1_opy_ in bstack1111ll1l11_opy_.keys():
    if bstack1lll11ll1_opy_ in bstack1111ll1ll_opy_:
      continue
    if bstack1lll11ll1_opy_ in options._caps and type(options._caps[bstack1lll11ll1_opy_]) in [dict, list]:
      options._caps[bstack1lll11ll1_opy_] = update(options._caps[bstack1lll11ll1_opy_], bstack1111ll1l11_opy_[bstack1lll11ll1_opy_])
    else:
      options.set_capability(bstack1lll11ll1_opy_, bstack1111ll1l11_opy_[bstack1lll11ll1_opy_])
  bstack1111l1lll1_opy_(options, bstack1111ll1l11_opy_)
  if bstack1ll11_opy_ (u"ࠧ࡮ࡱࡽ࠾ࡩ࡫ࡢࡶࡩࡪࡩࡷࡇࡤࡥࡴࡨࡷࡸ࠭ଽ") in options._caps:
    if options._caps[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ା")] and options._caps[bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧି")].lower() != bstack1ll11_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫୀ"):
      del options._caps[bstack1ll11_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪୁ")]
def bstack1l11lll111_opy_(proxy_config):
  if bstack1ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩୂ") in proxy_config:
    proxy_config[bstack1ll11_opy_ (u"࠭ࡳࡴ࡮ࡓࡶࡴࡾࡹࠨୃ")] = proxy_config[bstack1ll11_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫୄ")]
    del (proxy_config[bstack1ll11_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ୅")])
  if bstack1ll11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬ୆") in proxy_config and proxy_config[bstack1ll11_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭େ")].lower() != bstack1ll11_opy_ (u"ࠫࡩ࡯ࡲࡦࡥࡷࠫୈ"):
    proxy_config[bstack1ll11_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ୉")] = bstack1ll11_opy_ (u"࠭࡭ࡢࡰࡸࡥࡱ࠭୊")
  if bstack1ll11_opy_ (u"ࠧࡱࡴࡲࡼࡾࡇࡵࡵࡱࡦࡳࡳ࡬ࡩࡨࡗࡵࡰࠬୋ") in proxy_config:
    proxy_config[bstack1ll11_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫୌ")] = bstack1ll11_opy_ (u"ࠩࡳࡥࡨ୍࠭")
  return proxy_config
def bstack1ll11lllll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1ll11_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩ୎") in config:
    return proxy
  config[bstack1ll11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ୏")] = bstack1l11lll111_opy_(config[bstack1ll11_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ୐")])
  if proxy == None:
    proxy = Proxy(config[bstack1ll11_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୑")])
  return proxy
def bstack1l11111ll1_opy_(self):
  global CONFIG
  global bstack1l11llll1_opy_
  try:
    proxy = bstack11l1l11l11_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1ll11_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ୒")):
        proxies = bstack1ll1111l1_opy_(proxy, bstack1ll1ll111l_opy_())
        if len(proxies) > 0:
          protocol, bstack11l1111l1_opy_ = proxies.popitem()
          if bstack1ll11_opy_ (u"ࠣ࠼࠲࠳ࠧ୓") in bstack11l1111l1_opy_:
            return bstack11l1111l1_opy_
          else:
            return bstack1ll11_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥ୔") + bstack11l1111l1_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1ll11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢ୕").format(str(e)))
  return bstack1l11llll1_opy_(self)
def bstack111l1l1l11_opy_():
  global CONFIG
  return bstack111l111l1_opy_(CONFIG) and bstack11l111ll1l_opy_() and bstack1llll1l1l1_opy_() >= version.parse(bstack111llll1l_opy_)
def bstack1l11l1ll1_opy_():
  global CONFIG
  return (bstack1ll11_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧୖ") in CONFIG or bstack1ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩୗ") in CONFIG) and bstack11l111ll1_opy_()
def bstack11ll11l1l_opy_(config):
  bstack111lll11l_opy_ = {}
  if bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ୘") in config:
    bstack111lll11l_opy_ = config[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୙")]
  if bstack1ll11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ୚") in config:
    bstack111lll11l_opy_ = config[bstack1ll11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୛")]
  proxy = bstack11l1l11l11_opy_(config)
  if proxy:
    if proxy.endswith(bstack1ll11_opy_ (u"ࠪ࠲ࡵࡧࡣࠨଡ଼")) and os.path.isfile(proxy):
      bstack111lll11l_opy_[bstack1ll11_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧଢ଼")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1ll11_opy_ (u"ࠬ࠴ࡰࡢࡥࠪ୞")):
        proxies = bstack1111l1ll1_opy_(config, bstack1ll1ll111l_opy_())
        if len(proxies) > 0:
          protocol, bstack11l1111l1_opy_ = proxies.popitem()
          if bstack1ll11_opy_ (u"ࠨ࠺࠰࠱ࠥୟ") in bstack11l1111l1_opy_:
            parsed_url = urlparse(bstack11l1111l1_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1ll11_opy_ (u"ࠢ࠻࠱࠲ࠦୠ") + bstack11l1111l1_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack111lll11l_opy_[bstack1ll11_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫୡ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack111lll11l_opy_[bstack1ll11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬୢ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack111lll11l_opy_[bstack1ll11_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ୣ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack111lll11l_opy_[bstack1ll11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧ୤")] = str(parsed_url.password)
  return bstack111lll11l_opy_
def bstack1l1l1l1ll1_opy_(config):
  if bstack1ll11_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪ୥") in config:
    return config[bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫ୦")]
  return {}
def bstack1111l11lll_opy_(caps):
  global bstack1l1l1111l_opy_
  if bstack1ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ୧") in caps:
    caps[bstack1ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ୨")][bstack1ll11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨ୩")] = True
    if bstack1l1l1111l_opy_:
      caps[bstack1ll11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ୪")][bstack1ll11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭୫")] = bstack1l1l1111l_opy_
  else:
    caps[bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪ୬")] = True
    if bstack1l1l1111l_opy_:
      caps[bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ୭")] = bstack1l1l1111l_opy_
@measure(event_name=EVENTS.bstack1lllllll11_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1111lllll_opy_():
  global CONFIG
  if not bstack111lll111l_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ୮") in CONFIG and bstack1llll1lll1_opy_(CONFIG[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ୯")]):
    if (
      bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୰") in CONFIG
      and bstack1llll1lll1_opy_(CONFIG[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧୱ")].get(bstack1ll11_opy_ (u"ࠫࡸࡱࡩࡱࡄ࡬ࡲࡦࡸࡹࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡤࡸ࡮ࡵ࡮ࠨ୲")))
    ):
      logger.debug(bstack1ll11_opy_ (u"ࠧࡒ࡯ࡤࡣ࡯ࠤࡧ࡯࡮ࡢࡴࡼࠤࡳࡵࡴࠡࡵࡷࡥࡷࡺࡥࡥࠢࡤࡷࠥࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨ୳"))
      return
    bstack111lll11l_opy_ = bstack11ll11l1l_opy_(CONFIG)
    bstack111ll1l1ll_opy_(CONFIG[bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ୴")], bstack111lll11l_opy_)
def bstack111ll1l1ll_opy_(key, bstack111lll11l_opy_):
  global bstack1ll1lll111_opy_
  logger.info(bstack11111llll1_opy_)
  try:
    bstack1ll1lll111_opy_ = Local()
    bstack1ll1ll11l_opy_ = {bstack1ll11_opy_ (u"ࠧ࡬ࡧࡼࠫ୵"): key}
    bstack1ll1ll11l_opy_.update(bstack111lll11l_opy_)
    logger.debug(bstack11111ll1l_opy_.format(str(bstack1ll1ll11l_opy_)).replace(key, bstack1ll11_opy_ (u"ࠨ࡝ࡕࡉࡉࡇࡃࡕࡇࡇࡡࠬ୶")))
    bstack1ll1lll111_opy_.start(**bstack1ll1ll11l_opy_)
    if bstack1ll1lll111_opy_.isRunning():
      logger.info(bstack1l1lll11l1_opy_)
  except Exception as e:
    bstack11l11l11ll_opy_(bstack1lll11111l_opy_.format(str(e)))
def bstack11lllll1l_opy_():
  global bstack1ll1lll111_opy_
  if bstack1ll1lll111_opy_.isRunning():
    logger.info(bstack1l1ll11lll_opy_)
    bstack1ll1lll111_opy_.stop()
  bstack1ll1lll111_opy_ = None
def bstack11l1l1l11_opy_(bstack111ll111l_opy_=[]):
  global CONFIG
  bstack1l11l1111_opy_ = []
  bstack11ll111lll_opy_ = [bstack1ll11_opy_ (u"ࠩࡲࡷࠬ୷"), bstack1ll11_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭୸"), bstack1ll11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ୹"), bstack1ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ୺"), bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ୻"), bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ୼")]
  try:
    for err in bstack111ll111l_opy_:
      bstack1l111l1l11_opy_ = {}
      for k in bstack11ll111lll_opy_:
        val = CONFIG[bstack1ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ୽")][int(err[bstack1ll11_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ୾")])].get(k)
        if val:
          bstack1l111l1l11_opy_[k] = val
      if(err[bstack1ll11_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ୿")] != bstack1ll11_opy_ (u"ࠫࠬ஀")):
        bstack1l111l1l11_opy_[bstack1ll11_opy_ (u"ࠬࡺࡥࡴࡶࡶࠫ஁")] = {
          err[bstack1ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫஂ")]: err[bstack1ll11_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ஃ")]
        }
        bstack1l11l1111_opy_.append(bstack1l111l1l11_opy_)
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡴࡸ࡭ࡢࡶࡷ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴ࠻ࠢࠪ஄") + str(e))
  finally:
    return bstack1l11l1111_opy_
def bstack1ll1l1l11_opy_(file_name):
  bstack11ll1ll11l_opy_ = []
  try:
    bstack1l11lllll1_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1l11lllll1_opy_):
      with open(bstack1l11lllll1_opy_) as f:
        bstack1l11l1l111_opy_ = json.load(f)
        bstack11ll1ll11l_opy_ = bstack1l11l1l111_opy_
      os.remove(bstack1l11lllll1_opy_)
    return bstack11ll1ll11l_opy_
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫࡯࡮ࡥ࡫ࡱ࡫ࠥ࡫ࡲࡳࡱࡵࠤࡱ࡯ࡳࡵ࠼ࠣࠫஅ") + str(e))
    return bstack11ll1ll11l_opy_
def bstack1ll111111_opy_():
  try:
      from bstack_utils.constants import bstack1l1lll11ll_opy_, EVENTS
      from bstack_utils.helper import bstack11ll1llll_opy_, get_host_info, bstack1111ll11_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack11ll1lll11_opy_ = os.path.join(os.getcwd(), bstack1ll11_opy_ (u"ࠪࡰࡴ࡭ࠧஆ"), bstack1ll11_opy_ (u"ࠫࡰ࡫ࡹ࠮࡯ࡨࡸࡷ࡯ࡣࡴ࠰࡭ࡷࡴࡴࠧஇ"))
      lock = FileLock(bstack11ll1lll11_opy_+bstack1ll11_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦஈ"))
      def bstack1l11ll1l_opy_():
          try:
              with lock:
                  with open(bstack11ll1lll11_opy_, bstack1ll11_opy_ (u"ࠨࡲࠣஉ"), encoding=bstack1ll11_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨஊ")) as file:
                      data = json.load(file)
                      config = {
                          bstack1ll11_opy_ (u"ࠣࡪࡨࡥࡩ࡫ࡲࡴࠤ஋"): {
                              bstack1ll11_opy_ (u"ࠤࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠣ஌"): bstack1ll11_opy_ (u"ࠥࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳࠨ஍"),
                          }
                      }
                      bstack11ll1l1ll1_opy_ = datetime.utcnow()
                      bstack1lll1111_opy_ = bstack11ll1l1ll1_opy_.strftime(bstack1ll11_opy_ (u"ࠦࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࠯ࠧࡩࠤ࡚࡚ࡃࠣஎ"))
                      test_id = os.environ.get(bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪஏ")) if os.environ.get(bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫஐ")) else bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤ஑"))
                      payload = {
                          bstack1ll11_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠧஒ"): bstack1ll11_opy_ (u"ࠤࡶࡨࡰࡥࡥࡷࡧࡱࡸࡸࠨஓ"),
                          bstack1ll11_opy_ (u"ࠥࡨࡦࡺࡡࠣஔ"): {
                              bstack1ll11_opy_ (u"ࠦࡹ࡫ࡳࡵࡪࡸࡦࡤࡻࡵࡪࡦࠥக"): test_id,
                              bstack1ll11_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡩࡥࡤࡢࡻࠥ஖"): bstack1lll1111_opy_,
                              bstack1ll11_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࠥ஗"): bstack1ll11_opy_ (u"ࠢࡔࡆࡎࡊࡪࡧࡴࡶࡴࡨࡔࡪࡸࡦࡰࡴࡰࡥࡳࡩࡥࠣ஘"),
                              bstack1ll11_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟࡫ࡵࡲࡲࠧங"): {
                                  bstack1ll11_opy_ (u"ࠤࡰࡩࡦࡹࡵࡳࡧࡶࠦச"): data,
                                  bstack1ll11_opy_ (u"ࠥࡷࡩࡱࡒࡶࡰࡌࡨࠧ஛"): bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠦࡸࡪ࡫ࡓࡷࡱࡍࡩࠨஜ"))
                              },
                              bstack1ll11_opy_ (u"ࠧࡻࡳࡦࡴࡢࡨࡦࡺࡡࠣ஝"): bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠨࡵࡴࡧࡵࡒࡦࡳࡥࠣஞ")),
                              bstack1ll11_opy_ (u"ࠢࡩࡱࡶࡸࡤ࡯࡮ࡧࡱࠥட"): get_host_info()
                          }
                      }
                      bstack111111l11_opy_ = bstack11l11111l_opy_(cli.config, [bstack1ll11_opy_ (u"ࠣࡣࡳ࡭ࡸࠨ஠"), bstack1ll11_opy_ (u"ࠤࡨࡨࡸࡏ࡮ࡴࡶࡵࡹࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴࠢ஡"), bstack1ll11_opy_ (u"ࠥࡥࡵ࡯ࠢ஢")], bstack1l1lll11ll_opy_)
                      response = bstack11ll1llll_opy_(bstack1ll11_opy_ (u"ࠦࡕࡕࡓࡕࠤண"), bstack111111l11_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack1ll11_opy_ (u"ࠧࡊࡡࡵࡣࠣࡷࡪࡴࡴࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡵࡱࠣࡿࢂࠦࡷࡪࡶ࡫ࠤࡩࡧࡴࡢࠢࡾࢁࠧத").format(bstack1l1lll11ll_opy_, payload))
                      else:
                          logger.debug(bstack1ll11_opy_ (u"ࠨࡒࡦࡳࡸࡩࡸࡺࠠࡧࡣ࡬ࡰࡪࡪࠠࡧࡱࡵࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡪࡡࡵࡣࠣࡿࢂࠨ஥").format(bstack1l1lll11ll_opy_, payload))
          except Exception as e:
              logger.debug(bstack1ll11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡴࡤࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࠦࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡࡽࢀࠦ஦").format(e))
      bstack1l11ll1l_opy_()
      bstack1l111l11l_opy_(bstack11ll1lll11_opy_, logger)
  except:
    pass
def bstack1l1111lll_opy_():
  global bstack1ll11l1ll1_opy_
  global bstack1111l1l1l1_opy_
  global bstack11llll11l_opy_
  global bstack1ll11llll1_opy_
  global bstack1l1l111l11_opy_
  global bstack11lll1l1ll_opy_
  global CONFIG
  bstack111lll111_opy_ = os.environ.get(bstack1ll11_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩ஧"))
  if bstack111lll111_opy_ in [bstack1ll11_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨந"), bstack1ll11_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩன")]:
    bstack11ll1l1lll_opy_()
  percy.shutdown()
  if bstack1ll11l1ll1_opy_:
    logger.warning(bstack1l1l1l11ll_opy_.format(str(bstack1ll11l1ll1_opy_)))
  else:
    try:
      bstack11l11111l1_opy_ = bstack1ll11ll1l1_opy_(bstack1ll11_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪப"), logger)
      if bstack11l11111l1_opy_.get(bstack1ll11_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪ஫")) and bstack11l11111l1_opy_.get(bstack1ll11_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫ஬")).get(bstack1ll11_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩ஭")):
        logger.warning(bstack1l1l1l11ll_opy_.format(str(bstack11l11111l1_opy_[bstack1ll11_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ம")][bstack1ll11_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫய")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1ll1ll111_opy_.invoke(Events.bstack1l1lll1l1_opy_)
  logger.info(bstack11l11llll1_opy_)
  global bstack1ll1lll111_opy_
  if bstack1ll1lll111_opy_:
    bstack11lllll1l_opy_()
  try:
    with bstack1l11l1l1l_opy_:
      bstack11l1l1111l_opy_ = bstack1111l1l1l1_opy_.copy()
    for driver in bstack11l1l1111l_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1ll11l1lll_opy_)
  if bstack11lll1l1ll_opy_ == bstack1ll11_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩர"):
    bstack1l1l111l11_opy_ = bstack1ll1l1l11_opy_(bstack1ll11_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬற"))
  if bstack11lll1l1ll_opy_ == bstack1ll11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬல") and len(bstack1ll11llll1_opy_) == 0:
    bstack1ll11llll1_opy_ = bstack1ll1l1l11_opy_(bstack1ll11_opy_ (u"࠭ࡰࡸࡡࡳࡽࡹ࡫ࡳࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫள"))
    if len(bstack1ll11llll1_opy_) == 0:
      bstack1ll11llll1_opy_ = bstack1ll1l1l11_opy_(bstack1ll11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡱࡲࡳࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ழ"))
  bstack11llllll1l_opy_ = bstack1ll11_opy_ (u"ࠨࠩவ")
  if len(bstack11llll11l_opy_) > 0:
    bstack11llllll1l_opy_ = bstack11l1l1l11_opy_(bstack11llll11l_opy_)
  elif len(bstack1ll11llll1_opy_) > 0:
    bstack11llllll1l_opy_ = bstack11l1l1l11_opy_(bstack1ll11llll1_opy_)
  elif len(bstack1l1l111l11_opy_) > 0:
    bstack11llllll1l_opy_ = bstack11l1l1l11_opy_(bstack1l1l111l11_opy_)
  elif len(bstack1llll11l11_opy_) > 0:
    bstack11llllll1l_opy_ = bstack11l1l1l11_opy_(bstack1llll11l11_opy_)
  if bool(bstack11llllll1l_opy_):
    bstack1l1l11l11_opy_(bstack11llllll1l_opy_)
  else:
    bstack1l1l11l11_opy_()
  bstack1l111l11l_opy_(bstack11lll1l11_opy_, logger)
  if bstack111lll111_opy_ not in [bstack1ll11_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪஶ")]:
    bstack1ll111111_opy_()
  bstack1l1l1l1111_opy_.bstack1lllll11_opy_(CONFIG)
  if len(bstack1l1l111l11_opy_) > 0:
    sys.exit(len(bstack1l1l111l11_opy_))
def bstack11l1l1l1l_opy_(bstack1ll1ll11ll_opy_, frame):
  global bstack1111ll11_opy_
  logger.error(bstack1l11ll1ll_opy_)
  bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡒࡴ࠭ஷ"), bstack1ll1ll11ll_opy_)
  if hasattr(signal, bstack1ll11_opy_ (u"ࠫࡘ࡯ࡧ࡯ࡣ࡯ࡷࠬஸ")):
    bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬஹ"), signal.Signals(bstack1ll1ll11ll_opy_).name)
  else:
    bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭஺"), bstack1ll11_opy_ (u"ࠧࡔࡋࡊ࡙ࡓࡑࡎࡐ࡙ࡑࠫ஻"))
  if cli.is_running():
    bstack1ll1ll111_opy_.invoke(Events.bstack1l1lll1l1_opy_)
  bstack111lll111_opy_ = os.environ.get(bstack1ll11_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩ஼"))
  if bstack111lll111_opy_ == bstack1ll11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ஽") and not cli.is_enabled(CONFIG):
    bstack1ll111l1_opy_.stop(bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪா")))
  bstack1l1111lll_opy_()
  sys.exit(1)
def bstack11l11l11ll_opy_(err):
  logger.critical(bstack11lll1llll_opy_.format(str(err)))
  bstack1l1l11l11_opy_(bstack11lll1llll_opy_.format(str(err)), True)
  atexit.unregister(bstack1l1111lll_opy_)
  bstack11ll1l1lll_opy_()
  sys.exit(1)
def bstack1ll1lllll1_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l1l11l11_opy_(message, True)
  atexit.unregister(bstack1l1111lll_opy_)
  bstack11ll1l1lll_opy_()
  sys.exit(1)
def bstack1l11l111l_opy_():
  global CONFIG
  global bstack1l11ll1111_opy_
  global bstack1ll1l1l1l1_opy_
  global bstack1lllll1l1l_opy_
  CONFIG = bstack11llll111l_opy_()
  load_dotenv(CONFIG.get(bstack1ll11_opy_ (u"ࠫࡪࡴࡶࡇ࡫࡯ࡩࠬி")))
  bstack1l1l1ll11_opy_()
  bstack11l11l1ll1_opy_()
  CONFIG = bstack1l1lll111_opy_(CONFIG)
  update(CONFIG, bstack1ll1l1l1l1_opy_)
  update(CONFIG, bstack1l11ll1111_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1lll111111_opy_(CONFIG)
  bstack1lllll1l1l_opy_ = bstack111lll111l_opy_(CONFIG)
  os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨீ")] = bstack1lllll1l1l_opy_.__str__().lower()
  bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧு"), bstack1lllll1l1l_opy_)
  if (bstack1ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪூ") in CONFIG and bstack1ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௃") in bstack1l11ll1111_opy_) or (
          bstack1ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௄") in CONFIG and bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௅") not in bstack1ll1l1l1l1_opy_):
    if os.getenv(bstack1ll11_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨெ")):
      CONFIG[bstack1ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧே")] = os.getenv(bstack1ll11_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪை"))
    else:
      if not CONFIG.get(bstack1ll11_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠥ௉"), bstack1ll11_opy_ (u"ࠣࠤொ")) in bstack1l1111ll1l_opy_:
        bstack11l11ll111_opy_()
  elif (bstack1ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬோ") not in CONFIG and bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬௌ") in CONFIG) or (
          bstack1ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫்ࠧ") in bstack1ll1l1l1l1_opy_ and bstack1ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௎") not in bstack1l11ll1111_opy_):
    del (CONFIG[bstack1ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ௏")])
  if bstack11lll11111_opy_(CONFIG):
    bstack11l11l11ll_opy_(bstack111ll1ll1l_opy_)
  Config.bstack1llll11l1_opy_().set_property(bstack1ll11_opy_ (u"ࠢࡶࡵࡨࡶࡓࡧ࡭ࡦࠤௐ"), CONFIG[bstack1ll11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ௑")])
  bstack1111ll111_opy_()
  bstack11111ll111_opy_()
  if bstack111l1l111_opy_ and not CONFIG.get(bstack1ll11_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠧ௒"), bstack1ll11_opy_ (u"ࠥࠦ௓")) in bstack1l1111ll1l_opy_:
    CONFIG[bstack1ll11_opy_ (u"ࠫࡦࡶࡰࠨ௔")] = bstack111ll1lll1_opy_(CONFIG)
    logger.info(bstack11l11l1l1l_opy_.format(CONFIG[bstack1ll11_opy_ (u"ࠬࡧࡰࡱࠩ௕")]))
  if not bstack1lllll1l1l_opy_:
    CONFIG[bstack1ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ௖")] = [{}]
def bstack1l11l1ll11_opy_(config, bstack1l1lllll11_opy_):
  global CONFIG
  global bstack111l1l111_opy_
  CONFIG = config
  bstack111l1l111_opy_ = bstack1l1lllll11_opy_
def bstack11111ll111_opy_():
  global CONFIG
  global bstack111l1l111_opy_
  if bstack1ll11_opy_ (u"ࠧࡢࡲࡳࠫௗ") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1ll1lllll1_opy_(e, bstack1l111l111l_opy_)
    bstack111l1l111_opy_ = True
    bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ௘"), True)
def bstack111ll1lll1_opy_(config):
  bstack1111lll1l_opy_ = bstack1ll11_opy_ (u"ࠩࠪ௙")
  app = config[bstack1ll11_opy_ (u"ࠪࡥࡵࡶࠧ௚")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1111l1l111_opy_:
      if os.path.exists(app):
        bstack1111lll1l_opy_ = bstack1ll1ll1l1l_opy_(config, app)
      elif bstack11ll11llll_opy_(app):
        bstack1111lll1l_opy_ = app
      else:
        bstack11l11l11ll_opy_(bstack11l1111lll_opy_.format(app))
    else:
      if bstack11ll11llll_opy_(app):
        bstack1111lll1l_opy_ = app
      elif os.path.exists(app):
        bstack1111lll1l_opy_ = bstack1ll1ll1l1l_opy_(app)
      else:
        bstack11l11l11ll_opy_(bstack111l1ll1ll_opy_)
  else:
    if len(app) > 2:
      bstack11l11l11ll_opy_(bstack1l1l1l1l1_opy_)
    elif len(app) == 2:
      if bstack1ll11_opy_ (u"ࠫࡵࡧࡴࡩࠩ௛") in app and bstack1ll11_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ௜") in app:
        if os.path.exists(app[bstack1ll11_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ௝")]):
          bstack1111lll1l_opy_ = bstack1ll1ll1l1l_opy_(config, app[bstack1ll11_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ௞")], app[bstack1ll11_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫ௟")])
        else:
          bstack11l11l11ll_opy_(bstack11l1111lll_opy_.format(app))
      else:
        bstack11l11l11ll_opy_(bstack1l1l1l1l1_opy_)
    else:
      for key in app:
        if key in bstack11lll1l1l1_opy_:
          if key == bstack1ll11_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ௠"):
            if os.path.exists(app[key]):
              bstack1111lll1l_opy_ = bstack1ll1ll1l1l_opy_(config, app[key])
            else:
              bstack11l11l11ll_opy_(bstack11l1111lll_opy_.format(app))
          else:
            bstack1111lll1l_opy_ = app[key]
        else:
          bstack11l11l11ll_opy_(bstack1l1lll1ll1_opy_)
  return bstack1111lll1l_opy_
def bstack11ll11llll_opy_(bstack1111lll1l_opy_):
  import re
  bstack1l1ll111ll_opy_ = re.compile(bstack1ll11_opy_ (u"ࡵࠦࡣࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥ௡"))
  bstack11l111l111_opy_ = re.compile(bstack1ll11_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬ࠲࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰ࠤࠣ௢"))
  if bstack1ll11_opy_ (u"ࠬࡨࡳ࠻࠱࠲ࠫ௣") in bstack1111lll1l_opy_ or re.fullmatch(bstack1l1ll111ll_opy_, bstack1111lll1l_opy_) or re.fullmatch(bstack11l111l111_opy_, bstack1111lll1l_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack11l1l11lll_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1ll1ll1l1l_opy_(config, path, bstack1l111lll1l_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1ll11_opy_ (u"࠭ࡲࡣࠩ௤")).read()).hexdigest()
  bstack1l1l1ll1ll_opy_ = bstack1111l11l1l_opy_(md5_hash)
  bstack1111lll1l_opy_ = None
  if bstack1l1l1ll1ll_opy_:
    logger.info(bstack1111ll1l1l_opy_.format(bstack1l1l1ll1ll_opy_, md5_hash))
    return bstack1l1l1ll1ll_opy_
  bstack11l1lll1l_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack1ll11_opy_ (u"ࠧࡧ࡫࡯ࡩࠬ௥"): (os.path.basename(path), open(os.path.abspath(path), bstack1ll11_opy_ (u"ࠨࡴࡥࠫ௦")), bstack1ll11_opy_ (u"ࠩࡷࡩࡽࡺ࠯ࡱ࡮ࡤ࡭ࡳ࠭௧")),
      bstack1ll11_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭௨"): bstack1l111lll1l_opy_
    }
  )
  response = requests.post(bstack11ll111ll_opy_, data=multipart_data,
                           headers={bstack1ll11_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ௩"): multipart_data.content_type},
                           auth=(config[bstack1ll11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ௪")], config[bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ௫")]))
  try:
    res = json.loads(response.text)
    bstack1111lll1l_opy_ = res[bstack1ll11_opy_ (u"ࠧࡢࡲࡳࡣࡺࡸ࡬ࠨ௬")]
    logger.info(bstack11lll1l1l_opy_.format(bstack1111lll1l_opy_))
    bstack111l1lll1_opy_(md5_hash, bstack1111lll1l_opy_)
    cli.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠣࡪࡷࡸࡵࡀࡵࡱ࡮ࡲࡥࡩࡥࡡࡱࡲࠥ௭"), datetime.datetime.now() - bstack11l1lll1l_opy_)
  except ValueError as err:
    bstack11l11l11ll_opy_(bstack1111ll1111_opy_.format(str(err)))
  return bstack1111lll1l_opy_
def bstack1111ll111_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack11l1llll1_opy_
  bstack1lll1ll11_opy_ = 1
  bstack11l1lll1l1_opy_ = 1
  if bstack1ll11_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ௮") in CONFIG:
    bstack11l1lll1l1_opy_ = CONFIG[bstack1ll11_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ௯")]
  else:
    bstack11l1lll1l1_opy_ = bstack1ll1llll1_opy_(framework_name, args) or 1
  if bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ௰") in CONFIG:
    bstack1lll1ll11_opy_ = len(CONFIG[bstack1ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ௱")])
  bstack11l1llll1_opy_ = int(bstack11l1lll1l1_opy_) * int(bstack1lll1ll11_opy_)
def bstack1ll1llll1_opy_(framework_name, args):
  if framework_name == bstack11l1l1lll_opy_ and args and bstack1ll11_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ௲") in args:
      bstack1lll11111_opy_ = args.index(bstack1ll11_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬ௳"))
      return int(args[bstack1lll11111_opy_ + 1]) or 1
  return 1
def bstack1111l11l1l_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll11_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫ௴"))
    bstack1l1l111lll_opy_ = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"ࠩࢁࠫ௵")), bstack1ll11_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ௶"), bstack1ll11_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬ௷"))
    if os.path.exists(bstack1l1l111lll_opy_):
      try:
        bstack1ll1111lll_opy_ = json.load(open(bstack1l1l111lll_opy_, bstack1ll11_opy_ (u"ࠬࡸࡢࠨ௸")))
        if md5_hash in bstack1ll1111lll_opy_:
          bstack11llll111_opy_ = bstack1ll1111lll_opy_[md5_hash]
          bstack1111l111l_opy_ = datetime.datetime.now()
          bstack11ll1ll111_opy_ = datetime.datetime.strptime(bstack11llll111_opy_[bstack1ll11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ௹")], bstack1ll11_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫ௺"))
          if (bstack1111l111l_opy_ - bstack11ll1ll111_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack11llll111_opy_[bstack1ll11_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭௻")]):
            return None
          return bstack11llll111_opy_[bstack1ll11_opy_ (u"ࠩ࡬ࡨࠬ௼")]
      except Exception as e:
        logger.debug(bstack1ll11_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡑࡉ࠻ࠠࡩࡣࡶ࡬ࠥ࡬ࡩ࡭ࡧ࠽ࠤࢀࢃࠧ௽").format(str(e)))
    return None
  bstack1l1l111lll_opy_ = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"ࠫࢃ࠭௾")), bstack1ll11_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ௿"), bstack1ll11_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧఀ"))
  lock_file = bstack1l1l111lll_opy_ + bstack1ll11_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ࠭ఁ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1l1l111lll_opy_):
        with open(bstack1l1l111lll_opy_, bstack1ll11_opy_ (u"ࠨࡴࠪం")) as f:
          content = f.read().strip()
          if content:
            bstack1ll1111lll_opy_ = json.loads(content)
            if md5_hash in bstack1ll1111lll_opy_:
              bstack11llll111_opy_ = bstack1ll1111lll_opy_[md5_hash]
              bstack1111l111l_opy_ = datetime.datetime.now()
              bstack11ll1ll111_opy_ = datetime.datetime.strptime(bstack11llll111_opy_[bstack1ll11_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬః")], bstack1ll11_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧఄ"))
              if (bstack1111l111l_opy_ - bstack11ll1ll111_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack11llll111_opy_[bstack1ll11_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩఅ")]):
                return None
              return bstack11llll111_opy_[bstack1ll11_opy_ (u"ࠬ࡯ࡤࠨఆ")]
      return None
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡽࡩࡵࡪࠣࡪ࡮ࡲࡥࠡ࡮ࡲࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨ࠻ࠢࡾࢁࠬఇ").format(str(e)))
    return None
def bstack111l1lll1_opy_(md5_hash, bstack1111lll1l_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll11_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠢࡱࡳࡹࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡥࡥࡸ࡯ࡣࠡࡨ࡬ࡰࡪࠦ࡯ࡱࡧࡵࡥࡹ࡯࡯࡯ࡵࠪఈ"))
    bstack1l1llll11_opy_ = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"ࠨࢀࠪఉ")), bstack1ll11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩఊ"))
    if not os.path.exists(bstack1l1llll11_opy_):
      os.makedirs(bstack1l1llll11_opy_)
    bstack1l1l111lll_opy_ = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"ࠪࢂࠬఋ")), bstack1ll11_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఌ"), bstack1ll11_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭఍"))
    bstack1l1lllll1_opy_ = {
      bstack1ll11_opy_ (u"࠭ࡩࡥࠩఎ"): bstack1111lll1l_opy_,
      bstack1ll11_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪఏ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1ll11_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬఐ")),
      bstack1ll11_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ఑"): str(__version__)
    }
    try:
      bstack1ll1111lll_opy_ = {}
      if os.path.exists(bstack1l1l111lll_opy_):
        bstack1ll1111lll_opy_ = json.load(open(bstack1l1l111lll_opy_, bstack1ll11_opy_ (u"ࠪࡶࡧ࠭ఒ")))
      bstack1ll1111lll_opy_[md5_hash] = bstack1l1lllll1_opy_
      with open(bstack1l1l111lll_opy_, bstack1ll11_opy_ (u"ࠦࡼ࠱ࠢఓ")) as outfile:
        json.dump(bstack1ll1111lll_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1ll11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡺࡶࡤࡢࡶ࡬ࡲ࡬ࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨࠡࡨ࡬ࡰࡪࡀࠠࡼࡿࠪఔ").format(str(e)))
    return
  bstack1l1llll11_opy_ = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"࠭ࡾࠨక")), bstack1ll11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧఖ"))
  if not os.path.exists(bstack1l1llll11_opy_):
    os.makedirs(bstack1l1llll11_opy_)
  bstack1l1l111lll_opy_ = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"ࠨࢀࠪగ")), bstack1ll11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩఘ"), bstack1ll11_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫఙ"))
  lock_file = bstack1l1l111lll_opy_ + bstack1ll11_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪచ")
  bstack1l1lllll1_opy_ = {
    bstack1ll11_opy_ (u"ࠬ࡯ࡤࠨఛ"): bstack1111lll1l_opy_,
    bstack1ll11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩజ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1ll11_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫఝ")),
    bstack1ll11_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ఞ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1ll1111lll_opy_ = {}
      if os.path.exists(bstack1l1l111lll_opy_):
        with open(bstack1l1l111lll_opy_, bstack1ll11_opy_ (u"ࠩࡵࠫట")) as f:
          content = f.read().strip()
          if content:
            bstack1ll1111lll_opy_ = json.loads(content)
      bstack1ll1111lll_opy_[md5_hash] = bstack1l1lllll1_opy_
      with open(bstack1l1l111lll_opy_, bstack1ll11_opy_ (u"ࠥࡻࠧఠ")) as outfile:
        json.dump(bstack1ll1111lll_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡻ࡮ࡺࡨࠡࡨ࡬ࡰࡪࠦ࡬ࡰࡥ࡮࡭ࡳ࡭ࠠࡧࡱࡵࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࠦࡵࡱࡦࡤࡸࡪࡀࠠࡼࡿࠪడ").format(str(e)))
def bstack1lll1111ll_opy_(self):
  return
def bstack1lll1l1lll_opy_(self):
  return
def bstack111l1llll_opy_():
  global bstack11111l11l_opy_
  bstack11111l11l_opy_ = True
@measure(event_name=EVENTS.bstack11l1lll1ll_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack11lll1111_opy_(self):
  global bstack1l111llll_opy_
  global bstack11l1ll1l1_opy_
  global bstack1111l1l11_opy_
  try:
    if bstack1ll11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬఢ") in bstack1l111llll_opy_ and self.session_id != None and bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪణ"), bstack1ll11_opy_ (u"ࠧࠨత")) != bstack1ll11_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩథ"):
      bstack1l1ll11l1_opy_ = bstack1ll11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩద") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪధ")
      if bstack1l1ll11l1_opy_ == bstack1ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫన"):
        bstack11ll1lllll_opy_(logger)
      if self != None:
        bstack11l11lll1l_opy_(self, bstack1l1ll11l1_opy_, bstack1ll11_opy_ (u"ࠬ࠲ࠠࠨ఩").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1ll11_opy_ (u"࠭ࠧప")
    if bstack1ll11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧఫ") in bstack1l111llll_opy_ and getattr(threading.current_thread(), bstack1ll11_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧబ"), None):
      bstack111l11l1_opy_.bstack1111ll1l_opy_(self, bstack11llll1l1l_opy_, logger, wait=True)
    if bstack1ll11_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩభ") in bstack1l111llll_opy_:
      if not threading.currentThread().behave_test_status:
        bstack11l11lll1l_opy_(self, bstack1ll11_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥమ"))
      bstack1l1l1ll1l_opy_.bstack1llll11l1l_opy_(self)
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧయ") + str(e))
  bstack1111l1l11_opy_(self)
  self.session_id = None
def bstack11llll1111_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack111llll1ll_opy_
    global bstack1l111llll_opy_
    command_executor = kwargs.get(bstack1ll11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠨర"), bstack1ll11_opy_ (u"࠭ࠧఱ"))
    bstack1l111lll1_opy_ = False
    if type(command_executor) == str and bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪల") in command_executor:
      bstack1l111lll1_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫళ") in str(getattr(command_executor, bstack1ll11_opy_ (u"ࠩࡢࡹࡷࡲࠧఴ"), bstack1ll11_opy_ (u"ࠪࠫవ"))):
      bstack1l111lll1_opy_ = True
    else:
      kwargs = bstack11l11lll_opy_.bstack1l1111l11_opy_(bstack111l11l1l1_opy_=kwargs, config=CONFIG)
      return bstack11l1ll1lll_opy_(self, *args, **kwargs)
    if bstack1l111lll1_opy_:
      bstack11llll1ll1_opy_ = bstack11l1l1ll1_opy_.bstack1111l1lll_opy_(CONFIG, bstack1l111llll_opy_)
      if kwargs.get(bstack1ll11_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬశ")):
        kwargs[bstack1ll11_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ష")] = bstack111llll1ll_opy_(kwargs[bstack1ll11_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧస")], bstack1l111llll_opy_, CONFIG, bstack11llll1ll1_opy_)
      elif kwargs.get(bstack1ll11_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧహ")):
        kwargs[bstack1ll11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ఺")] = bstack111llll1ll_opy_(kwargs[bstack1ll11_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ఻")], bstack1l111llll_opy_, CONFIG, bstack11llll1ll1_opy_)
  except Exception as e:
    logger.error(bstack1ll11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡘࡊࡋࠡࡥࡤࡴࡸࡀࠠࡼࡿ఼ࠥ").format(str(e)))
  return bstack11l1ll1lll_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l111l1lll_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1ll1l1l1l_opy_(self, command_executor=bstack1ll11_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳࠶࠸࠷࠯࠲࠱࠴࠳࠷࠺࠵࠶࠷࠸ࠧఽ"), *args, **kwargs):
  global bstack11l1ll1l1_opy_
  global bstack1111l1l1l1_opy_
  bstack11l1llll1l_opy_ = bstack11llll1111_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1l11l1ll_opy_.on():
    return bstack11l1llll1l_opy_
  try:
    logger.debug(bstack1ll11_opy_ (u"ࠬࡉ࡯࡮࡯ࡤࡲࡩࠦࡅࡹࡧࡦࡹࡹࡵࡲࠡࡹ࡫ࡩࡳࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥ࡬ࡡ࡭ࡵࡨࠤ࠲ࠦࡻࡾࠩా").format(str(command_executor)))
    logger.debug(bstack1ll11_opy_ (u"࠭ࡈࡶࡤ࡙ࠣࡗࡒࠠࡪࡵࠣ࠱ࠥࢁࡽࠨి").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪీ") in command_executor._url:
      bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩు"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬూ") in command_executor):
    bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫృ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1111lll11_opy_ = getattr(threading.current_thread(), bstack1ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥࠬౄ"), None)
  bstack1l11l11lll_opy_ = {}
  if self.capabilities is not None:
    bstack1l11l11lll_opy_[bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫ౅")] = self.capabilities.get(bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫె"))
    bstack1l11l11lll_opy_[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩే")] = self.capabilities.get(bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩై"))
    bstack1l11l11lll_opy_[bstack1ll11_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࠪ౉")] = self.capabilities.get(bstack1ll11_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨొ"))
  if CONFIG.get(bstack1ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫో"), False) and bstack11l11lll_opy_.bstack1l11l1lll_opy_(bstack1l11l11lll_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack1ll11_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬౌ") in bstack1l111llll_opy_ or bstack1ll11_opy_ (u"࠭ࡲࡰࡤࡲࡸ్ࠬ") in bstack1l111llll_opy_:
    bstack1ll111l1_opy_.bstack1ll111ll1_opy_(self)
  if bstack1ll11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ౎") in bstack1l111llll_opy_ and bstack1111lll11_opy_ and bstack1111lll11_opy_.get(bstack1ll11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ౏"), bstack1ll11_opy_ (u"ࠩࠪ౐")) == bstack1ll11_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ౑"):
    bstack1ll111l1_opy_.bstack1ll111ll1_opy_(self)
  bstack11l1ll1l1_opy_ = self.session_id
  with bstack1l11l1l1l_opy_:
    bstack1111l1l1l1_opy_.append(self)
  return bstack11l1llll1l_opy_
def bstack111lll11l1_opy_(args):
  return bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠬ౒") in str(args)
def bstack1lll11ll11_opy_(self, driver_command, *args, **kwargs):
  global bstack11111ll11_opy_
  global bstack111l1111ll_opy_
  bstack11ll11l1l1_opy_ = bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ౓"), None) and bstack1ll1ll11_opy_(
          threading.current_thread(), bstack1ll11_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ౔"), None)
  bstack1lll1111l_opy_ = bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺౕࠧ"), None) and bstack1ll1ll11_opy_(
          threading.current_thread(), bstack1ll11_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ౖࠪ"), None)
  bstack11111l1ll1_opy_ = getattr(self, bstack1ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩ౗"), None) != None and getattr(self, bstack1ll11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪౘ"), None) == True
  if not bstack111l1111ll_opy_ and bstack1ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫౙ") in CONFIG and CONFIG[bstack1ll11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬౚ")] == True and bstack11111lll11_opy_.bstack1lll1111l1_opy_(driver_command) and (bstack11111l1ll1_opy_ or bstack11ll11l1l1_opy_ or bstack1lll1111l_opy_) and not bstack111lll11l1_opy_(args):
    try:
      bstack111l1111ll_opy_ = True
      logger.debug(bstack1ll11_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࢁࡽࠨ౛").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1ll11_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡪࡸࡦࡰࡴࡰࠤࡸࡩࡡ࡯ࠢࡾࢁࠬ౜").format(str(err)))
    bstack111l1111ll_opy_ = False
  response = bstack11111ll11_opy_(self, driver_command, *args, **kwargs)
  if (bstack1ll11_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧౝ") in str(bstack1l111llll_opy_).lower() or bstack1ll11_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ౞") in str(bstack1l111llll_opy_).lower()) and bstack1l11l1ll_opy_.on():
    try:
      if driver_command == bstack1ll11_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧ౟"):
        bstack1ll111l1_opy_.bstack1l1l1l111l_opy_({
            bstack1ll11_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࠪౠ"): response[bstack1ll11_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫౡ")],
            bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ౢ"): bstack1ll111l1_opy_.current_test_uuid() if bstack1ll111l1_opy_.current_test_uuid() else bstack1l11l1ll_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1ll1l1ll1_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1l111ll11l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack11l1ll1l1_opy_
  global bstack1ll1l1lll_opy_
  global bstack11l1l111ll_opy_
  global bstack1l11lll11_opy_
  global bstack111llll1l1_opy_
  global bstack1l111llll_opy_
  global bstack11l1ll1lll_opy_
  global bstack1111l1l1l1_opy_
  global bstack1lllll11l1_opy_
  global bstack11llll1l1l_opy_
  if os.getenv(bstack1ll11_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬౣ")) is not None and bstack11l11lll_opy_.bstack11l11ll11_opy_(CONFIG) is None:
    CONFIG[bstack1ll11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ౤")] = True
  CONFIG[bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ౥")] = str(bstack1l111llll_opy_) + str(__version__)
  bstack11lll1ll11_opy_ = os.environ[bstack1ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ౦")]
  bstack11llll1ll1_opy_ = bstack11l1l1ll1_opy_.bstack1111l1lll_opy_(CONFIG, bstack1l111llll_opy_)
  CONFIG[bstack1ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧ౧")] = bstack11lll1ll11_opy_
  CONFIG[bstack1ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧ౨")] = bstack11llll1ll1_opy_
  if CONFIG.get(bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭౩"),bstack1ll11_opy_ (u"ࠧࠨ౪")) and bstack1ll11_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ౫") in bstack1l111llll_opy_:
    CONFIG[bstack1ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ౬")].pop(bstack1ll11_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ౭"), None)
    CONFIG[bstack1ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ౮")].pop(bstack1ll11_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ౯"), None)
  command_executor = bstack1ll1ll111l_opy_()
  logger.debug(bstack111l111111_opy_.format(command_executor))
  proxy = bstack1ll11lllll_opy_(CONFIG, proxy)
  bstack111l111lll_opy_ = 0 if bstack1ll1l1lll_opy_ < 0 else bstack1ll1l1lll_opy_
  try:
    if bstack1l11lll11_opy_ is True:
      bstack111l111lll_opy_ = int(multiprocessing.current_process().name)
    elif bstack111llll1l1_opy_ is True:
      bstack111l111lll_opy_ = int(threading.current_thread().name)
  except:
    bstack111l111lll_opy_ = 0
  bstack1111ll1l11_opy_ = bstack111l1lllll_opy_(CONFIG, bstack111l111lll_opy_)
  logger.debug(bstack1111ll111l_opy_.format(str(bstack1111ll1l11_opy_)))
  if bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ౰") in CONFIG and bstack1llll1lll1_opy_(CONFIG[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ౱")]):
    bstack1111l11lll_opy_(bstack1111ll1l11_opy_)
  if bstack11l11lll_opy_.bstack1111l1l1ll_opy_(CONFIG, bstack111l111lll_opy_) and bstack11l11lll_opy_.bstack1ll1llll1l_opy_(bstack1111ll1l11_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack11l11lll_opy_.set_capabilities(bstack1111ll1l11_opy_, CONFIG)
  if desired_capabilities:
    bstack1ll1ll1111_opy_ = bstack1l1lll111_opy_(desired_capabilities)
    bstack1ll1ll1111_opy_[bstack1ll11_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨ౲")] = bstack1lll111lll_opy_(CONFIG)
    bstack1ll1l111l_opy_ = bstack111l1lllll_opy_(bstack1ll1ll1111_opy_)
    if bstack1ll1l111l_opy_:
      bstack1111ll1l11_opy_ = update(bstack1ll1l111l_opy_, bstack1111ll1l11_opy_)
    desired_capabilities = None
  if options:
    bstack11ll1l11l1_opy_(options, bstack1111ll1l11_opy_)
  if not options:
    options = bstack1ll1l11111_opy_(bstack1111ll1l11_opy_)
  bstack11llll1l1l_opy_ = CONFIG.get(bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ౳"))[bstack111l111lll_opy_]
  if proxy and bstack1llll1l1l1_opy_() >= version.parse(bstack1ll11_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪ౴")):
    options.proxy(proxy)
  if options and bstack1llll1l1l1_opy_() >= version.parse(bstack1ll11_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ౵")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1llll1l1l1_opy_() < version.parse(bstack1ll11_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ౶")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1111ll1l11_opy_)
  logger.info(bstack1111llll1l_opy_)
  bstack11l111l1l_opy_.end(EVENTS.bstack11l1111ll_opy_.value, EVENTS.bstack11l1111ll_opy_.value + bstack1ll11_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ౷"), EVENTS.bstack11l1111ll_opy_.value + bstack1ll11_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ౸"), status=True, failure=None, test_name=bstack11l1l111ll_opy_)
  if bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡳࡶࡴ࡬ࡩ࡭ࡧࠪ౹") in kwargs:
    del kwargs[bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡴࡷࡵࡦࡪ࡮ࡨࠫ౺")]
  try:
    if bstack1llll1l1l1_opy_() >= version.parse(bstack1ll11_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪ౻")):
      bstack11l1ll1lll_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack1llll1l1l1_opy_() >= version.parse(bstack1ll11_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ౼")):
      bstack11l1ll1lll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1llll1l1l1_opy_() >= version.parse(bstack1ll11_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬ౽")):
      bstack11l1ll1lll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack11l1ll1lll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack11111lllll_opy_:
    logger.error(bstack1l1111ll1_opy_.format(bstack1ll11_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠬ౾"), str(bstack11111lllll_opy_)))
    raise bstack11111lllll_opy_
  if bstack11l11lll_opy_.bstack1111l1l1ll_opy_(CONFIG, bstack111l111lll_opy_) and bstack11l11lll_opy_.bstack1ll1llll1l_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack1ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ౿")][bstack1ll11_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧಀ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack11l11lll_opy_.set_capabilities(bstack1111ll1l11_opy_, CONFIG)
  try:
    bstack1l1111ll11_opy_ = bstack1ll11_opy_ (u"ࠩࠪಁ")
    if bstack1llll1l1l1_opy_() >= version.parse(bstack1ll11_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࡤ࠴ࠫಂ")):
      if self.caps is not None:
        bstack1l1111ll11_opy_ = self.caps.get(bstack1ll11_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦಃ"))
    else:
      if self.capabilities is not None:
        bstack1l1111ll11_opy_ = self.capabilities.get(bstack1ll11_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧ಄"))
    if bstack1l1111ll11_opy_:
      bstack1111ll1l1_opy_(bstack1l1111ll11_opy_)
      if bstack1llll1l1l1_opy_() <= version.parse(bstack1ll11_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ಅ")):
        self.command_executor._url = bstack1ll11_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣಆ") + bstack11l111111l_opy_ + bstack1ll11_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧಇ")
      else:
        self.command_executor._url = bstack1ll11_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦಈ") + bstack1l1111ll11_opy_ + bstack1ll11_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦಉ")
      logger.debug(bstack1l1ll1l11l_opy_.format(bstack1l1111ll11_opy_))
    else:
      logger.debug(bstack1l11l11l1l_opy_.format(bstack1ll11_opy_ (u"ࠦࡔࡶࡴࡪ࡯ࡤࡰࠥࡎࡵࡣࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧಊ")))
  except Exception as e:
    logger.debug(bstack1l11l11l1l_opy_.format(e))
  if bstack1ll11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫಋ") in bstack1l111llll_opy_:
    bstack11l1ll11l_opy_(bstack1ll1l1lll_opy_, bstack1lllll11l1_opy_)
  bstack11l1ll1l1_opy_ = self.session_id
  if bstack1ll11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ಌ") in bstack1l111llll_opy_ or bstack1ll11_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ಍") in bstack1l111llll_opy_ or bstack1ll11_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧಎ") in bstack1l111llll_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1111lll11_opy_ = getattr(threading.current_thread(), bstack1ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪಏ"), None)
  if bstack1ll11_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪಐ") in bstack1l111llll_opy_ or bstack1ll11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ಑") in bstack1l111llll_opy_:
    bstack1ll111l1_opy_.bstack1ll111ll1_opy_(self)
  if bstack1ll11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬಒ") in bstack1l111llll_opy_ and bstack1111lll11_opy_ and bstack1111lll11_opy_.get(bstack1ll11_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ಓ"), bstack1ll11_opy_ (u"ࠧࠨಔ")) == bstack1ll11_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩಕ"):
    bstack1ll111l1_opy_.bstack1ll111ll1_opy_(self)
  with bstack1l11l1l1l_opy_:
    bstack1111l1l1l1_opy_.append(self)
  if bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಖ") in CONFIG and bstack1ll11_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨಗ") in CONFIG[bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧಘ")][bstack111l111lll_opy_]:
    bstack11l1l111ll_opy_ = CONFIG[bstack1ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಙ")][bstack111l111lll_opy_][bstack1ll11_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫಚ")]
  logger.debug(bstack1l1l11lll_opy_.format(bstack11l1ll1l1_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1111llllll_opy_
    def bstack11l1111111_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1l1l11llll_opy_
      if(bstack1ll11_opy_ (u"ࠢࡪࡰࡧࡩࡽ࠴ࡪࡴࠤಛ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"ࠨࢀࠪಜ")), bstack1ll11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩಝ"), bstack1ll11_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬಞ")), bstack1ll11_opy_ (u"ࠫࡼ࠭ಟ")) as fp:
          fp.write(bstack1ll11_opy_ (u"ࠧࠨಠ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1ll11_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣಡ")))):
          with open(args[1], bstack1ll11_opy_ (u"ࠧࡳࠩಢ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1ll11_opy_ (u"ࠨࡣࡶࡽࡳࡩࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡢࡲࡪࡽࡐࡢࡩࡨࠬࡨࡵ࡮ࡵࡧࡻࡸ࠱ࠦࡰࡢࡩࡨࠤࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠧಣ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1l1l11111_opy_)
            if bstack1ll11_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ತ") in CONFIG and str(CONFIG[bstack1ll11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧಥ")]).lower() != bstack1ll11_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪದ"):
                bstack1lll1l11ll_opy_ = bstack1111llllll_opy_()
                bstack11l11l1l11_opy_ = bstack1ll11_opy_ (u"ࠬ࠭ࠧࠋ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࠎࡨࡵ࡮ࡴࡶࠣࡦࡸࡺࡡࡤ࡭ࡢࡴࡦࡺࡨࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷ࡢࡁࠊࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠱࡞࠽ࠍࡧࡴࡴࡳࡵࠢࡳࡣ࡮ࡴࡤࡦࡺࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠸࡝࠼ࠌࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰ࡶࡰ࡮ࡩࡥࠩ࠲࠯ࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹ࠩ࠼ࠌࡦࡳࡳࡹࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢࠪ࠽ࠍ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡰࡦࡻ࡮ࡤࡪࠣࡁࠥࡧࡳࡺࡰࡦࠤ࠭ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷ࠮ࠦ࠽࠿ࠢࡾࡿࠏࠦࠠ࡭ࡧࡷࠤࡨࡧࡰࡴ࠽ࠍࠤࠥࡺࡲࡺࠢࡾࡿࠏࠦࠠࠡࠢࡦࡥࡵࡹࠠ࠾ࠢࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶ࠭ࡀࠐࠠࠡࡿࢀࠤࡨࡧࡴࡤࡪࠣࠬࡪࡾࠩࠡࡽࡾࠎࠥࠦࠠࠡࡥࡲࡲࡸࡵ࡬ࡦ࠰ࡨࡶࡷࡵࡲࠩࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠽ࠦ࠱ࠦࡥࡹࠫ࠾ࠎࠥࠦࡽࡾࠌࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡦࡽࡡࡪࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡧࡴࡴ࡮ࡦࡥࡷࠬࢀࢁࠊࠡࠢࠣࠤࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴ࠻ࠢࠪࡿࡨࡪࡰࡖࡴ࡯ࢁࠬࠦࠫࠡࡧࡱࡧࡴࡪࡥࡖࡔࡌࡇࡴࡳࡰࡰࡰࡨࡲࡹ࠮ࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡤࡣࡳࡷ࠮࠯ࠬࠋࠢࠣࠤࠥ࠴࠮࠯࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠋࠢࠣࢁࢂ࠯࠻ࠋࡿࢀ࠿ࠏ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯ࠋࠩࠪࠫಧ").format(bstack1lll1l11ll_opy_=bstack1lll1l11ll_opy_)
            lines.insert(1, bstack11l11l1l11_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1ll11_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣನ")), bstack1ll11_opy_ (u"ࠧࡸࠩ಩")) as bstack11l1ll1ll_opy_:
              bstack11l1ll1ll_opy_.writelines(lines)
        CONFIG[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪಪ")] = str(bstack1l111llll_opy_) + str(__version__)
        bstack11lll1ll11_opy_ = os.environ[bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧಫ")]
        bstack11llll1ll1_opy_ = bstack11l1l1ll1_opy_.bstack1111l1lll_opy_(CONFIG, bstack1l111llll_opy_)
        CONFIG[bstack1ll11_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ಬ")] = bstack11lll1ll11_opy_
        CONFIG[bstack1ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ಭ")] = bstack11llll1ll1_opy_
        bstack111l111lll_opy_ = 0 if bstack1ll1l1lll_opy_ < 0 else bstack1ll1l1lll_opy_
        try:
          if bstack1l11lll11_opy_ is True:
            bstack111l111lll_opy_ = int(multiprocessing.current_process().name)
          elif bstack111llll1l1_opy_ is True:
            bstack111l111lll_opy_ = int(threading.current_thread().name)
        except:
          bstack111l111lll_opy_ = 0
        CONFIG[bstack1ll11_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧಮ")] = False
        CONFIG[bstack1ll11_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧಯ")] = True
        bstack1111ll1l11_opy_ = bstack111l1lllll_opy_(CONFIG, bstack111l111lll_opy_)
        logger.debug(bstack1111ll111l_opy_.format(str(bstack1111ll1l11_opy_)))
        if CONFIG.get(bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫರ")):
          bstack1111l11lll_opy_(bstack1111ll1l11_opy_)
        if bstack1ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಱ") in CONFIG and bstack1ll11_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧಲ") in CONFIG[bstack1ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಳ")][bstack111l111lll_opy_]:
          bstack11l1l111ll_opy_ = CONFIG[bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಴")][bstack111l111lll_opy_][bstack1ll11_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪವ")]
        args.append(os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"࠭ࡾࠨಶ")), bstack1ll11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧಷ"), bstack1ll11_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪಸ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1111ll1l11_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1ll11_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦಹ"))
      bstack1l1l11llll_opy_ = True
      return bstack1lllllllll_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack111l1l1lll_opy_(self,
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
    global bstack1ll1l1lll_opy_
    global bstack11l1l111ll_opy_
    global bstack1l11lll11_opy_
    global bstack111llll1l1_opy_
    global bstack1l111llll_opy_
    CONFIG[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ಺")] = str(bstack1l111llll_opy_) + str(__version__)
    bstack11lll1ll11_opy_ = os.environ[bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ಻")]
    bstack11llll1ll1_opy_ = bstack11l1l1ll1_opy_.bstack1111l1lll_opy_(CONFIG, bstack1l111llll_opy_)
    CONFIG[bstack1ll11_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ಼")] = bstack11lll1ll11_opy_
    CONFIG[bstack1ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨಽ")] = bstack11llll1ll1_opy_
    bstack111l111lll_opy_ = 0 if bstack1ll1l1lll_opy_ < 0 else bstack1ll1l1lll_opy_
    try:
      if bstack1l11lll11_opy_ is True:
        bstack111l111lll_opy_ = int(multiprocessing.current_process().name)
      elif bstack111llll1l1_opy_ is True:
        bstack111l111lll_opy_ = int(threading.current_thread().name)
    except:
      bstack111l111lll_opy_ = 0
    CONFIG[bstack1ll11_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨಾ")] = True
    bstack1111ll1l11_opy_ = bstack111l1lllll_opy_(CONFIG, bstack111l111lll_opy_)
    logger.debug(bstack1111ll111l_opy_.format(str(bstack1111ll1l11_opy_)))
    if CONFIG.get(bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬಿ")):
      bstack1111l11lll_opy_(bstack1111ll1l11_opy_)
    if bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೀ") in CONFIG and bstack1ll11_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨು") in CONFIG[bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧೂ")][bstack111l111lll_opy_]:
      bstack11l1l111ll_opy_ = CONFIG[bstack1ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨೃ")][bstack111l111lll_opy_][bstack1ll11_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫೄ")]
    import urllib
    import json
    if bstack1ll11_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ೅") in CONFIG and str(CONFIG[bstack1ll11_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬೆ")]).lower() != bstack1ll11_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨೇ"):
        bstack111ll1l1l_opy_ = bstack1111llllll_opy_()
        bstack1lll1l11ll_opy_ = bstack111ll1l1l_opy_ + urllib.parse.quote(json.dumps(bstack1111ll1l11_opy_))
    else:
        bstack1lll1l11ll_opy_ = bstack1ll11_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬೈ") + urllib.parse.quote(json.dumps(bstack1111ll1l11_opy_))
    browser = self.connect(bstack1lll1l11ll_opy_)
    return browser
except Exception as e:
    pass
def bstack1ll111l1l_opy_():
    global bstack1l1l11llll_opy_
    global bstack1l111llll_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack111ll1l11l_opy_
        global bstack1111ll11_opy_
        if not bstack1lllll1l1l_opy_:
          global bstack1ll1lll1l1_opy_
          if not bstack1ll1lll1l1_opy_:
            from bstack_utils.helper import bstack11l11l1ll_opy_, bstack1lll11l1ll_opy_, bstack11111l111_opy_
            bstack1ll1lll1l1_opy_ = bstack11l11l1ll_opy_()
            bstack1lll11l1ll_opy_(bstack1l111llll_opy_)
            bstack11llll1ll1_opy_ = bstack11l1l1ll1_opy_.bstack1111l1lll_opy_(CONFIG, bstack1l111llll_opy_)
            bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"ࠦࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡒࡕࡓࡉ࡛ࡃࡕࡡࡐࡅࡕࠨ೉"), bstack11llll1ll1_opy_)
          BrowserType.connect = bstack111ll1l11l_opy_
          return
        BrowserType.launch = bstack111l1l1lll_opy_
        bstack1l1l11llll_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack11l1111111_opy_
      bstack1l1l11llll_opy_ = True
    except Exception as e:
      pass
def bstack111l11l1l_opy_(context, bstack111l11lll_opy_):
  try:
    context.page.evaluate(bstack1ll11_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨೊ"), bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪೋ")+ json.dumps(bstack111l11lll_opy_) + bstack1ll11_opy_ (u"ࠢࡾࡿࠥೌ"))
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࡀࠠࡼࡿ್ࠥ").format(str(e), traceback.format_exc()))
def bstack1l1l1ll11l_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1ll11_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ೎"), bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ೏") + json.dumps(message) + bstack1ll11_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧ೐") + json.dumps(level) + bstack1ll11_opy_ (u"ࠬࢃࡽࠨ೑"))
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾ࠼ࠣࡿࢂࠨ೒").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1ll1l11l1l_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1111l1111l_opy_(self, url):
  global bstack11ll1llll1_opy_
  try:
    bstack1ll1ll1lll_opy_(url)
  except Exception as err:
    logger.debug(bstack111ll1l111_opy_.format(str(err)))
  try:
    bstack11ll1llll1_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack11l11l11l_opy_):
        bstack1ll1ll1lll_opy_(url, True)
    except Exception as err:
      logger.debug(bstack111ll1l111_opy_.format(str(err)))
    raise e
def bstack1l1l1llll1_opy_(self):
  global bstack111l1ll11_opy_
  bstack111l1ll11_opy_ = self
  return
def bstack1111111ll_opy_(self):
  global bstack1l11111lll_opy_
  bstack1l11111lll_opy_ = self
  return
def bstack11111ll1ll_opy_(test_name, bstack11l1ll11ll_opy_):
  global CONFIG
  if percy.bstack1l1l1llll_opy_() == bstack1ll11_opy_ (u"ࠢࡵࡴࡸࡩࠧ೓"):
    bstack11ll1111l_opy_ = os.path.relpath(bstack11l1ll11ll_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack11ll1111l_opy_)
    bstack111ll11l1l_opy_ = suite_name + bstack1ll11_opy_ (u"ࠣ࠯ࠥ೔") + test_name
    threading.current_thread().percySessionName = bstack111ll11l1l_opy_
def bstack1l1lllll1l_opy_(self, test, *args, **kwargs):
  global bstack11ll11lll_opy_
  test_name = None
  bstack11l1ll11ll_opy_ = None
  if test:
    test_name = str(test.name)
    bstack11l1ll11ll_opy_ = str(test.source)
  bstack11111ll1ll_opy_(test_name, bstack11l1ll11ll_opy_)
  bstack11ll11lll_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack111l111l11_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1l1l1ll111_opy_(driver, bstack111ll11l1l_opy_):
  if not bstack1ll11lll11_opy_ and bstack111ll11l1l_opy_:
      bstack1l111l1111_opy_ = {
          bstack1ll11_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩೕ"): bstack1ll11_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫೖ"),
          bstack1ll11_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ೗"): {
              bstack1ll11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ೘"): bstack111ll11l1l_opy_
          }
      }
      bstack1l111lll11_opy_ = bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ೙").format(json.dumps(bstack1l111l1111_opy_))
      driver.execute_script(bstack1l111lll11_opy_)
  if bstack1lll1l1l11_opy_:
      bstack111l11l1ll_opy_ = {
          bstack1ll11_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ೚"): bstack1ll11_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪ೛"),
          bstack1ll11_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ೜"): {
              bstack1ll11_opy_ (u"ࠪࡨࡦࡺࡡࠨೝ"): bstack111ll11l1l_opy_ + bstack1ll11_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭ೞ"),
              bstack1ll11_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ೟"): bstack1ll11_opy_ (u"࠭ࡩ࡯ࡨࡲࠫೠ")
          }
      }
      if bstack1lll1l1l11_opy_.status == bstack1ll11_opy_ (u"ࠧࡑࡃࡖࡗࠬೡ"):
          bstack1llll1l11l_opy_ = bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ೢ").format(json.dumps(bstack111l11l1ll_opy_))
          driver.execute_script(bstack1llll1l11l_opy_)
          bstack11l11lll1l_opy_(driver, bstack1ll11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩೣ"))
      elif bstack1lll1l1l11_opy_.status == bstack1ll11_opy_ (u"ࠪࡊࡆࡏࡌࠨ೤"):
          reason = bstack1ll11_opy_ (u"ࠦࠧ೥")
          bstack1ll11l111_opy_ = bstack111ll11l1l_opy_ + bstack1ll11_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩ࠭೦")
          if bstack1lll1l1l11_opy_.message:
              reason = str(bstack1lll1l1l11_opy_.message)
              bstack1ll11l111_opy_ = bstack1ll11l111_opy_ + bstack1ll11_opy_ (u"࠭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥ࠭೧") + reason
          bstack111l11l1ll_opy_[bstack1ll11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ೨")] = {
              bstack1ll11_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ೩"): bstack1ll11_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ೪"),
              bstack1ll11_opy_ (u"ࠪࡨࡦࡺࡡࠨ೫"): bstack1ll11l111_opy_
          }
          bstack1llll1l11l_opy_ = bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ೬").format(json.dumps(bstack111l11l1ll_opy_))
          driver.execute_script(bstack1llll1l11l_opy_)
          bstack11l11lll1l_opy_(driver, bstack1ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ೭"), reason)
          bstack111l11lll1_opy_(reason, str(bstack1lll1l1l11_opy_), str(bstack1ll1l1lll_opy_), logger)
@measure(event_name=EVENTS.bstack11llllll11_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1lllll11ll_opy_(driver, test):
  if percy.bstack1l1l1llll_opy_() == bstack1ll11_opy_ (u"ࠨࡴࡳࡷࡨࠦ೮") and percy.bstack11l1111l1l_opy_() == bstack1ll11_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤ೯"):
      bstack1ll111111l_opy_ = bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠨࡲࡨࡶࡨࡿࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ೰"), None)
      bstack11l1l11ll1_opy_(driver, bstack1ll111111l_opy_, test)
  if (bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ೱ"), None) and
      bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩೲ"), None)) or (
      bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫೳ"), None) and
      bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ೴"), None)):
      logger.info(bstack1ll11_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠤࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡩࡴࠢࡸࡲࡩ࡫ࡲࡸࡣࡼ࠲ࠥࠨ೵"))
      bstack11l11lll_opy_.bstack1lllll1ll_opy_(driver, name=test.name, path=test.source)
def bstack1ll1lll11l_opy_(test, bstack111ll11l1l_opy_):
    try:
      bstack11l1lll1l_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack1ll11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ೶")] = bstack111ll11l1l_opy_
      if bstack1lll1l1l11_opy_:
        if bstack1lll1l1l11_opy_.status == bstack1ll11_opy_ (u"ࠨࡒࡄࡗࡘ࠭೷"):
          data[bstack1ll11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ೸")] = bstack1ll11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ೹")
        elif bstack1lll1l1l11_opy_.status == bstack1ll11_opy_ (u"ࠫࡋࡇࡉࡍࠩ೺"):
          data[bstack1ll11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ೻")] = bstack1ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭೼")
          if bstack1lll1l1l11_opy_.message:
            data[bstack1ll11_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧ೽")] = str(bstack1lll1l1l11_opy_.message)
      user = CONFIG[bstack1ll11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ೾")]
      key = CONFIG[bstack1ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ೿")]
      host = bstack11l11111l_opy_(cli.config, [bstack1ll11_opy_ (u"ࠥࡥࡵ࡯ࡳࠣഀ"), bstack1ll11_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨഁ"), bstack1ll11_opy_ (u"ࠧࡧࡰࡪࠤം")], bstack1ll11_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠢഃ"))
      url = bstack1ll11_opy_ (u"ࠧࡼࡿ࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠯ࡼࡿ࠱࡮ࡸࡵ࡮ࠨഄ").format(host, bstack11l1ll1l1_opy_)
      headers = {
        bstack1ll11_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧഅ"): bstack1ll11_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬആ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡷࡳࡨࡦࡺࡥࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡶࡤࡸࡺࡹࠢഇ"), datetime.datetime.now() - bstack11l1lll1l_opy_)
    except Exception as e:
      logger.error(bstack1l11ll1ll1_opy_.format(str(e)))
def bstack111l1l11l1_opy_(test, bstack111ll11l1l_opy_):
  global CONFIG
  global bstack1l11111lll_opy_
  global bstack111l1ll11_opy_
  global bstack11l1ll1l1_opy_
  global bstack1lll1l1l11_opy_
  global bstack11l1l111ll_opy_
  global bstack1111l1l11l_opy_
  global bstack11llll1ll_opy_
  global bstack11111llll_opy_
  global bstack1ll1l1111_opy_
  global bstack1111l1l1l1_opy_
  global bstack11llll1l1l_opy_
  global bstack11lllllll1_opy_
  try:
    if not bstack11l1ll1l1_opy_:
      with bstack11lllllll1_opy_:
        bstack11l1lll11_opy_ = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"ࠫࢃ࠭ഈ")), bstack1ll11_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬഉ"), bstack1ll11_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨഊ"))
        if os.path.exists(bstack11l1lll11_opy_):
          with open(bstack11l1lll11_opy_, bstack1ll11_opy_ (u"ࠧࡳࠩഋ")) as f:
            content = f.read().strip()
            if content:
              bstack1l1l11l1l1_opy_ = json.loads(bstack1ll11_opy_ (u"ࠣࡽࠥഌ") + content + bstack1ll11_opy_ (u"ࠩࠥࡼࠧࡀࠠࠣࡻࠥࠫ഍") + bstack1ll11_opy_ (u"ࠥࢁࠧഎ"))
              bstack11l1ll1l1_opy_ = bstack1l1l11l1l1_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡶࡪࡧࡤࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡏࡄࡴࠢࡩ࡭ࡱ࡫࠺ࠡࠩഏ") + str(e))
  if bstack1111l1l1l1_opy_:
    with bstack1l11l1l1l_opy_:
      bstack11ll1lll1l_opy_ = bstack1111l1l1l1_opy_.copy()
    for driver in bstack11ll1lll1l_opy_:
      if bstack11l1ll1l1_opy_ == driver.session_id:
        if test:
          bstack1lllll11ll_opy_(driver, test)
        bstack1l1l1ll111_opy_(driver, bstack111ll11l1l_opy_)
  elif bstack11l1ll1l1_opy_:
    bstack1ll1lll11l_opy_(test, bstack111ll11l1l_opy_)
  if bstack1l11111lll_opy_:
    bstack11llll1ll_opy_(bstack1l11111lll_opy_)
  if bstack111l1ll11_opy_:
    bstack11111llll_opy_(bstack111l1ll11_opy_)
  if bstack11111l11l_opy_:
    bstack1ll1l1111_opy_()
def bstack1lllll1l11_opy_(self, test, *args, **kwargs):
  bstack111ll11l1l_opy_ = None
  if test:
    bstack111ll11l1l_opy_ = str(test.name)
  bstack111l1l11l1_opy_(test, bstack111ll11l1l_opy_)
  bstack1111l1l11l_opy_(self, test, *args, **kwargs)
def bstack1ll1llllll_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1ll111ll11_opy_
  global CONFIG
  global bstack1111l1l1l1_opy_
  global bstack11l1ll1l1_opy_
  global bstack11lllllll1_opy_
  bstack11l1111l11_opy_ = None
  try:
    if bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫഐ"), None) or bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ഑"), None):
      try:
        if not bstack11l1ll1l1_opy_:
          bstack11l1lll11_opy_ = os.path.join(os.path.expanduser(bstack1ll11_opy_ (u"ࠧࡿࠩഒ")), bstack1ll11_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨഓ"), bstack1ll11_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫഔ"))
          with bstack11lllllll1_opy_:
            if os.path.exists(bstack11l1lll11_opy_):
              with open(bstack11l1lll11_opy_, bstack1ll11_opy_ (u"ࠪࡶࠬക")) as f:
                content = f.read().strip()
                if content:
                  bstack1l1l11l1l1_opy_ = json.loads(bstack1ll11_opy_ (u"ࠦࢀࠨഖ") + content + bstack1ll11_opy_ (u"ࠬࠨࡸࠣ࠼ࠣࠦࡾࠨࠧഗ") + bstack1ll11_opy_ (u"ࠨࡽࠣഘ"))
                  bstack11l1ll1l1_opy_ = bstack1l1l11l1l1_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack1ll11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡋࡇࡷࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾ࠥ࠭ങ") + str(e))
      if bstack1111l1l1l1_opy_:
        with bstack1l11l1l1l_opy_:
          bstack11ll1lll1l_opy_ = bstack1111l1l1l1_opy_.copy()
        for driver in bstack11ll1lll1l_opy_:
          if bstack11l1ll1l1_opy_ == driver.session_id:
            bstack11l1111l11_opy_ = driver
    bstack111lll1ll1_opy_ = bstack11l11lll_opy_.bstack1llllll1l1_opy_(test.tags)
    if bstack11l1111l11_opy_:
      threading.current_thread().isA11yTest = bstack11l11lll_opy_.bstack111l1lll1l_opy_(bstack11l1111l11_opy_, bstack111lll1ll1_opy_)
      threading.current_thread().isAppA11yTest = bstack11l11lll_opy_.bstack111l1lll1l_opy_(bstack11l1111l11_opy_, bstack111lll1ll1_opy_)
    else:
      threading.current_thread().isA11yTest = bstack111lll1ll1_opy_
      threading.current_thread().isAppA11yTest = bstack111lll1ll1_opy_
  except:
    pass
  bstack1ll111ll11_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1lll1l1l11_opy_
  try:
    bstack1lll1l1l11_opy_ = self._test
  except:
    bstack1lll1l1l11_opy_ = self.test
def bstack1ll11ll11l_opy_():
  global bstack1ll1111111_opy_
  try:
    if os.path.exists(bstack1ll1111111_opy_):
      os.remove(bstack1ll1111111_opy_)
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫച") + str(e))
def bstack1ll1ll1l11_opy_():
  global bstack1ll1111111_opy_
  bstack11l11111l1_opy_ = {}
  lock_file = bstack1ll1111111_opy_ + bstack1ll11_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨഛ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll11_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭ജ"))
    try:
      if not os.path.isfile(bstack1ll1111111_opy_):
        with open(bstack1ll1111111_opy_, bstack1ll11_opy_ (u"ࠫࡼ࠭ഝ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1ll1111111_opy_):
        with open(bstack1ll1111111_opy_, bstack1ll11_opy_ (u"ࠬࡸࠧഞ")) as f:
          content = f.read().strip()
          if content:
            bstack11l11111l1_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack1ll11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨട") + str(e))
    return bstack11l11111l1_opy_
  try:
    os.makedirs(os.path.dirname(bstack1ll1111111_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack1ll1111111_opy_):
        with open(bstack1ll1111111_opy_, bstack1ll11_opy_ (u"ࠧࡸࠩഠ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1ll1111111_opy_):
        with open(bstack1ll1111111_opy_, bstack1ll11_opy_ (u"ࠨࡴࠪഡ")) as f:
          content = f.read().strip()
          if content:
            bstack11l11111l1_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫഢ") + str(e))
  finally:
    return bstack11l11111l1_opy_
def bstack11l1ll11l_opy_(platform_index, item_index):
  global bstack1ll1111111_opy_
  lock_file = bstack1ll1111111_opy_ + bstack1ll11_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩണ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1ll11_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧത"))
    try:
      bstack11l11111l1_opy_ = {}
      if os.path.exists(bstack1ll1111111_opy_):
        with open(bstack1ll1111111_opy_, bstack1ll11_opy_ (u"ࠬࡸࠧഥ")) as f:
          content = f.read().strip()
          if content:
            bstack11l11111l1_opy_ = json.loads(content)
      bstack11l11111l1_opy_[item_index] = platform_index
      with open(bstack1ll1111111_opy_, bstack1ll11_opy_ (u"ࠨࡷࠣദ")) as outfile:
        json.dump(bstack11l11111l1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1ll11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡺࡶ࡮ࡺࡩ࡯ࡩࠣࡸࡴࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬധ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack1ll1111111_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack11l11111l1_opy_ = {}
      if os.path.exists(bstack1ll1111111_opy_):
        with open(bstack1ll1111111_opy_, bstack1ll11_opy_ (u"ࠨࡴࠪന")) as f:
          content = f.read().strip()
          if content:
            bstack11l11111l1_opy_ = json.loads(content)
      bstack11l11111l1_opy_[item_index] = platform_index
      with open(bstack1ll1111111_opy_, bstack1ll11_opy_ (u"ࠤࡺࠦഩ")) as outfile:
        json.dump(bstack11l11111l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡽࡲࡪࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨപ") + str(e))
def bstack1llllll1ll_opy_(bstack11ll11111l_opy_):
  global CONFIG
  bstack1lll1ll11l_opy_ = bstack1ll11_opy_ (u"ࠫࠬഫ")
  if not bstack1ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨബ") in CONFIG:
    logger.info(bstack1ll11_opy_ (u"࠭ࡎࡰࠢࡳࡰࡦࡺࡦࡰࡴࡰࡷࠥࡶࡡࡴࡵࡨࡨࠥࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡲࡪࡸࡡࡵࡧࠣࡶࡪࡶ࡯ࡳࡶࠣࡪࡴࡸࠠࡓࡱࡥࡳࡹࠦࡲࡶࡰࠪഭ"))
  try:
    platform = CONFIG[bstack1ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪമ")][bstack11ll11111l_opy_]
    if bstack1ll11_opy_ (u"ࠨࡱࡶࠫയ") in platform:
      bstack1lll1ll11l_opy_ += str(platform[bstack1ll11_opy_ (u"ࠩࡲࡷࠬര")]) + bstack1ll11_opy_ (u"ࠪ࠰ࠥ࠭റ")
    if bstack1ll11_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧല") in platform:
      bstack1lll1ll11l_opy_ += str(platform[bstack1ll11_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨള")]) + bstack1ll11_opy_ (u"࠭ࠬࠡࠩഴ")
    if bstack1ll11_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫവ") in platform:
      bstack1lll1ll11l_opy_ += str(platform[bstack1ll11_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬശ")]) + bstack1ll11_opy_ (u"ࠩ࠯ࠤࠬഷ")
    if bstack1ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬസ") in platform:
      bstack1lll1ll11l_opy_ += str(platform[bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ഹ")]) + bstack1ll11_opy_ (u"ࠬ࠲ࠠࠨഺ")
    if bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨ഻ࠫ") in platform:
      bstack1lll1ll11l_opy_ += str(platform[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩ഼ࠬ")]) + bstack1ll11_opy_ (u"ࠨ࠮ࠣࠫഽ")
    if bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪാ") in platform:
      bstack1lll1ll11l_opy_ += str(platform[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫി")]) + bstack1ll11_opy_ (u"ࠫ࠱ࠦࠧീ")
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"࡙ࠬ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡺࡲࡪࡰࡪࠤ࡫ࡵࡲࠡࡴࡨࡴࡴࡸࡴࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡲࡲࠬു") + str(e))
  finally:
    if bstack1lll1ll11l_opy_[len(bstack1lll1ll11l_opy_) - 2:] == bstack1ll11_opy_ (u"࠭ࠬࠡࠩൂ"):
      bstack1lll1ll11l_opy_ = bstack1lll1ll11l_opy_[:-2]
    return bstack1lll1ll11l_opy_
def bstack111l1l1ll1_opy_(path, bstack1lll1ll11l_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l11ll1l1l_opy_ = ET.parse(path)
    bstack1l111l111_opy_ = bstack1l11ll1l1l_opy_.getroot()
    bstack1l1111llll_opy_ = None
    for suite in bstack1l111l111_opy_.iter(bstack1ll11_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ൃ")):
      if bstack1ll11_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨൄ") in suite.attrib:
        suite.attrib[bstack1ll11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ൅")] += bstack1ll11_opy_ (u"ࠪࠤࠬെ") + bstack1lll1ll11l_opy_
        bstack1l1111llll_opy_ = suite
    bstack11lll1ll1_opy_ = None
    for robot in bstack1l111l111_opy_.iter(bstack1ll11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪേ")):
      bstack11lll1ll1_opy_ = robot
    bstack1lllll1lll_opy_ = len(bstack11lll1ll1_opy_.findall(bstack1ll11_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫൈ")))
    if bstack1lllll1lll_opy_ == 1:
      bstack11lll1ll1_opy_.remove(bstack11lll1ll1_opy_.findall(bstack1ll11_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൉"))[0])
      bstack11ll1l1111_opy_ = ET.Element(bstack1ll11_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ൊ"), attrib={bstack1ll11_opy_ (u"ࠨࡰࡤࡱࡪ࠭ോ"): bstack1ll11_opy_ (u"ࠩࡖࡹ࡮ࡺࡥࡴࠩൌ"), bstack1ll11_opy_ (u"ࠪ࡭ࡩ്࠭"): bstack1ll11_opy_ (u"ࠫࡸ࠶ࠧൎ")})
      bstack11lll1ll1_opy_.insert(1, bstack11ll1l1111_opy_)
      bstack1l11111111_opy_ = None
      for suite in bstack11lll1ll1_opy_.iter(bstack1ll11_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫ൏")):
        bstack1l11111111_opy_ = suite
      bstack1l11111111_opy_.append(bstack1l1111llll_opy_)
      bstack11ll11l11l_opy_ = None
      for status in bstack1l1111llll_opy_.iter(bstack1ll11_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭൐")):
        bstack11ll11l11l_opy_ = status
      bstack1l11111111_opy_.append(bstack11ll11l11l_opy_)
    bstack1l11ll1l1l_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠬ൑") + str(e))
def bstack1ll11lll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1ll1l1ll11_opy_
  global CONFIG
  if bstack1ll11_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬ࠧ൒") in options:
    del options[bstack1ll11_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨ൓")]
  json_data = bstack1ll1ll1l11_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack1ll11_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࡡࡵࡩࡸࡻ࡬ࡵࡵࠪൔ"), str(item_id), bstack1ll11_opy_ (u"ࠫࡴࡻࡴࡱࡷࡷ࠲ࡽࡳ࡬ࠨൕ"))
    bstack111l1l1ll1_opy_(path, bstack1llllll1ll_opy_(json_data[item_id]))
  bstack1ll11ll11l_opy_()
  return bstack1ll1l1ll11_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1l11l11l11_opy_(self, ff_profile_dir):
  global bstack1111lll111_opy_
  if not ff_profile_dir:
    return None
  return bstack1111lll111_opy_(self, ff_profile_dir)
def bstack1lll1lllll_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l1l1111l_opy_
  bstack1l11l11ll1_opy_ = []
  if bstack1ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨൖ") in CONFIG:
    bstack1l11l11ll1_opy_ = CONFIG[bstack1ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩൗ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1ll11_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࠣ൘")],
      pabot_args[bstack1ll11_opy_ (u"ࠣࡸࡨࡶࡧࡵࡳࡦࠤ൙")],
      argfile,
      pabot_args.get(bstack1ll11_opy_ (u"ࠤ࡫࡭ࡻ࡫ࠢ൚")),
      pabot_args[bstack1ll11_opy_ (u"ࠥࡴࡷࡵࡣࡦࡵࡶࡩࡸࠨ൛")],
      platform[0],
      bstack1l1l1111l_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1ll11_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹ࡬ࡩ࡭ࡧࡶࠦ൜")] or [(bstack1ll11_opy_ (u"ࠧࠨ൝"), None)]
    for platform in enumerate(bstack1l11l11ll1_opy_)
  ]
def bstack11l111l11l_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1llll11lll_opy_=bstack1ll11_opy_ (u"࠭ࠧ൞")):
  global bstack1l11ll11l_opy_
  self.platform_index = platform_index
  self.bstack1l11ll1lll_opy_ = bstack1llll11lll_opy_
  bstack1l11ll11l_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack11l1l1l111_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1ll1l1ll1l_opy_
  global bstack1ll111l111_opy_
  bstack111lll11ll_opy_ = copy.deepcopy(item)
  if not bstack1ll11_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩൟ") in item.options:
    bstack111lll11ll_opy_.options[bstack1ll11_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪൠ")] = []
  bstack1ll111l11l_opy_ = bstack111lll11ll_opy_.options[bstack1ll11_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫൡ")].copy()
  for v in bstack111lll11ll_opy_.options[bstack1ll11_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬൢ")]:
    if bstack1ll11_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚ࠪൣ") in v:
      bstack1ll111l11l_opy_.remove(v)
    if bstack1ll11_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬ൤") in v:
      bstack1ll111l11l_opy_.remove(v)
    if bstack1ll11_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡊࡅࡇࡎࡒࡇࡆࡒࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪ൥") in v:
      bstack1ll111l11l_opy_.remove(v)
  bstack1ll111l11l_opy_.insert(0, bstack1ll11_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝ࡀࡻࡾࠩ൦").format(bstack111lll11ll_opy_.platform_index))
  bstack1ll111l11l_opy_.insert(0, bstack1ll11_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖ࠿ࢁࡽࠨ൧").format(bstack111lll11ll_opy_.bstack1l11ll1lll_opy_))
  bstack111lll11ll_opy_.options[bstack1ll11_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ൨")] = bstack1ll111l11l_opy_
  if bstack1ll111l111_opy_:
    bstack111lll11ll_opy_.options[bstack1ll11_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ൩")].insert(0, bstack1ll11_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖ࠾ࢀࢃࠧ൪").format(bstack1ll111l111_opy_))
  return bstack1ll1l1ll1l_opy_(caller_id, datasources, is_last, bstack111lll11ll_opy_, outs_dir)
def bstack1111ll11l_opy_(command, item_index):
  try:
    if bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭൫")):
      os.environ[bstack1ll11_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧ൬")] = json.dumps(CONFIG[bstack1ll11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ൭")][item_index % bstack1111llll1_opy_])
    global bstack1ll111l111_opy_
    if bstack1ll111l111_opy_:
      command[0] = command[0].replace(bstack1ll11_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ൮"), bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡵࡧ࡯ࠥࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱࠦ࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠥ࠭൯") + str(
        item_index) + bstack1ll11_opy_ (u"ࠪࠤࠬ൰") + bstack1ll111l111_opy_, 1)
    else:
      command[0] = command[0].replace(bstack1ll11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ൱"),
                                      bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡸࡪ࡫ࠡࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠢ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠡࠩ൲") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack1ll11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡳ࡯ࡥ࡫ࡩࡽ࡮ࡴࡧࠡࡥࡲࡱࡲࡧ࡮ࡥࠢࡩࡳࡷࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯࠼ࠣࡿࢂ࠭൳").format(str(e)))
def bstack111l11111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1ll11l11l1_opy_
  try:
    bstack1111ll11l_opy_(command, item_index)
    return bstack1ll11l11l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack1ll11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲ࠿ࠦࡻࡾࠩ൴").format(str(e)))
    raise e
def bstack11ll1ll1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1ll11l11l1_opy_
  try:
    bstack1111ll11l_opy_(command, item_index)
    return bstack1ll11l11l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack1ll11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࠦ࠲࠯࠳࠶࠾ࠥࢁࡽࠨ൵").format(str(e)))
    try:
      return bstack1ll11l11l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack1ll11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣ࠶࠳࠷࠳ࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧ൶").format(str(e2)))
      raise e
def bstack1lll1lll11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1ll11l11l1_opy_
  try:
    bstack1111ll11l_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack1ll11l11l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack1ll11_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠴࠱࠵࠺ࡀࠠࡼࡿࠪ൷").format(str(e)))
    try:
      return bstack1ll11l11l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack1ll11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࠸࠮࠲࠷ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩ൸").format(str(e2)))
      raise e
def _11ll11111_opy_(bstack1l11lll1l1_opy_, item_index, process_timeout, sleep_before_start, bstack1l1ll1l11_opy_):
  bstack1111ll11l_opy_(bstack1l11lll1l1_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack1l111l1l1_opy_(command, bstack1l1l1lll1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1ll11l11l1_opy_
  try:
    bstack1111ll11l_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack1ll11l11l1_opy_(command, bstack1l1l1lll1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1ll11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰࠣ࠹࠳࠶࠺ࠡࡽࢀࠫ൹").format(str(e)))
    try:
      return bstack1ll11l11l1_opy_(command, bstack1l1l1lll1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1ll11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࡿࢂ࠭ൺ").format(str(e2)))
      raise e
def bstack11l11ll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1ll11l11l1_opy_
  try:
    process_timeout = _11ll11111_opy_(command, item_index, process_timeout, sleep_before_start, bstack1ll11_opy_ (u"ࠧ࠵࠰࠵ࠫൻ"))
    return bstack1ll11l11l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1ll11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࠦ࠴࠯࠴࠽ࠤࢀࢃࠧർ").format(str(e)))
    try:
      return bstack1ll11l11l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1ll11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩൽ").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack1lllll1ll1_opy_(self, runner, quiet=False, capture=True):
  global bstack1111l1llll_opy_
  bstack1lll11lll1_opy_ = bstack1111l1llll_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack1ll11_opy_ (u"ࠪࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࡥࡡࡳࡴࠪൾ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1ll11_opy_ (u"ࠫࡪࡾࡣࡠࡶࡵࡥࡨ࡫ࡢࡢࡥ࡮ࡣࡦࡸࡲࠨൿ")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1lll11lll1_opy_
def bstack1l1l1111l1_opy_(runner, hook_name, context, element, bstack1ll11l111l_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1llll1l111_opy_.bstack11ll1lll_opy_(hook_name, element)
    bstack1ll11l111l_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1llll1l111_opy_.bstack11l1l1l1_opy_(element)
      if hook_name not in [bstack1ll11_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠩ඀"), bstack1ll11_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩඁ")] and args and hasattr(args[0], bstack1ll11_opy_ (u"ࠧࡦࡴࡵࡳࡷࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠧං")):
        args[0].error_message = bstack1ll11_opy_ (u"ࠨࠩඃ")
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡮ࡡ࡯ࡦ࡯ࡩࠥ࡮࡯ࡰ࡭ࡶࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫࠺ࠡࡽࢀࠫ඄").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1ll1l1_opy_, stage=STAGE.bstack1111l1111_opy_, hook_type=bstack1ll11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡄࡰࡱࠨඅ"), bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1ll1l111ll_opy_(runner, name, context, bstack1ll11l111l_opy_, *args):
    if runner.hooks.get(bstack1ll11_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣආ")).__name__ != bstack1ll11_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࡡࡧࡩ࡫ࡧࡵ࡭ࡶࡢ࡬ࡴࡵ࡫ࠣඇ"):
      bstack1l1l1111l1_opy_(runner, name, context, runner, bstack1ll11l111l_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack11l1l1l11l_opy_(bstack1ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඈ")) else context.browser
      runner.driver_initialised = bstack1ll11_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦඉ")
    except Exception as e:
      logger.debug(bstack1ll11_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡩࠥࡧࡴࡵࡴ࡬ࡦࡺࡺࡥ࠻ࠢࡾࢁࠬඊ").format(str(e)))
def bstack1l1ll1l1l1_opy_(runner, name, context, bstack1ll11l111l_opy_, *args):
    bstack1l1l1111l1_opy_(runner, name, context, context.feature, bstack1ll11l111l_opy_, *args)
    try:
      if not bstack1ll11lll11_opy_:
        bstack11l1111l11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l1l1l11l_opy_(bstack1ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨඋ")) else context.browser
        if is_driver_active(bstack11l1111l11_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack1ll11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦඌ")
          bstack111l11lll_opy_ = str(runner.feature.name)
          bstack111l11l1l_opy_(context, bstack111l11lll_opy_)
          bstack11l1111l11_opy_.execute_script(bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩඍ") + json.dumps(bstack111l11lll_opy_) + bstack1ll11_opy_ (u"ࠬࢃࡽࠨඎ"))
    except Exception as e:
      logger.debug(bstack1ll11_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭ඏ").format(str(e)))
def bstack1l1ll1ll1l_opy_(runner, name, context, bstack1ll11l111l_opy_, *args):
    if hasattr(context, bstack1ll11_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩඐ")):
        bstack1llll1l111_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack1ll11_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪඑ")) else context.feature
    bstack1l1l1111l1_opy_(runner, name, context, target, bstack1ll11l111l_opy_, *args)
@measure(event_name=EVENTS.bstack1lll11l1l_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1ll11111ll_opy_(runner, name, context, bstack1ll11l111l_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1llll1l111_opy_.start_test(context)
    bstack1l1l1111l1_opy_(runner, name, context, context.scenario, bstack1ll11l111l_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1l1l1ll1l_opy_.bstack11111l1l1_opy_(context, *args)
    try:
      bstack11l1111l11_opy_ = bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨඒ"), context.browser)
      if is_driver_active(bstack11l1111l11_opy_):
        bstack1ll111l1_opy_.bstack1ll111ll1_opy_(bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩඓ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack1ll11_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨඔ")
        if (not bstack1ll11lll11_opy_):
          scenario_name = args[0].name
          feature_name = bstack111l11lll_opy_ = str(runner.feature.name)
          bstack111l11lll_opy_ = feature_name + bstack1ll11_opy_ (u"ࠬࠦ࠭ࠡࠩඕ") + scenario_name
          if runner.driver_initialised == bstack1ll11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣඖ"):
            bstack111l11l1l_opy_(context, bstack111l11lll_opy_)
            bstack11l1111l11_opy_.execute_script(bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬ඗") + json.dumps(bstack111l11lll_opy_) + bstack1ll11_opy_ (u"ࠨࡿࢀࠫ඘"))
    except Exception as e:
      logger.debug(bstack1ll11_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡ࡫ࡱࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡩࡥ࡯ࡣࡵ࡭ࡴࡀࠠࡼࡿࠪ඙").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1ll1l1_opy_, stage=STAGE.bstack1111l1111_opy_, hook_type=bstack1ll11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡖࡸࡪࡶࠢක"), bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1l111l11l1_opy_(runner, name, context, bstack1ll11l111l_opy_, *args):
    bstack1l1l1111l1_opy_(runner, name, context, args[0], bstack1ll11l111l_opy_, *args)
    try:
      bstack11l1111l11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l1l1l11l_opy_(bstack1ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪඛ")) else context.browser
      if is_driver_active(bstack11l1111l11_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack1ll11_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥග")
        bstack1llll1l111_opy_.bstack11ll1ll1_opy_(args[0])
        if runner.driver_initialised == bstack1ll11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦඝ"):
          feature_name = bstack111l11lll_opy_ = str(runner.feature.name)
          bstack111l11lll_opy_ = feature_name + bstack1ll11_opy_ (u"ࠧࠡ࠯ࠣࠫඞ") + context.scenario.name
          bstack11l1111l11_opy_.execute_script(bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭ඟ") + json.dumps(bstack111l11lll_opy_) + bstack1ll11_opy_ (u"ࠩࢀࢁࠬච"))
    except Exception as e:
      logger.debug(bstack1ll11_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡴࡦࡲ࠽ࠤࢀࢃࠧඡ").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1ll1l1_opy_, stage=STAGE.bstack1111l1111_opy_, hook_type=bstack1ll11_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࡖࡸࡪࡶࠢජ"), bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1ll1111ll1_opy_(runner, name, context, bstack1ll11l111l_opy_, *args):
  bstack1llll1l111_opy_.bstack11l1ll1l_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack11l1111l11_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫඣ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack11l1111l11_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack1ll11_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭ඤ")
        feature_name = bstack111l11lll_opy_ = str(runner.feature.name)
        bstack111l11lll_opy_ = feature_name + bstack1ll11_opy_ (u"ࠧࠡ࠯ࠣࠫඥ") + context.scenario.name
        bstack11l1111l11_opy_.execute_script(bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭ඦ") + json.dumps(bstack111l11lll_opy_) + bstack1ll11_opy_ (u"ࠩࢀࢁࠬට"))
    if str(step_status).lower() == bstack1ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪඨ"):
      bstack111ll11111_opy_ = bstack1ll11_opy_ (u"ࠫࠬඩ")
      bstack1ll11111l_opy_ = bstack1ll11_opy_ (u"ࠬ࠭ඪ")
      bstack11l1lll111_opy_ = bstack1ll11_opy_ (u"࠭ࠧණ")
      try:
        import traceback
        bstack111ll11111_opy_ = runner.exception.__class__.__name__
        bstack11l1llll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1ll11111l_opy_ = bstack1ll11_opy_ (u"ࠧࠡࠩඬ").join(bstack11l1llll_opy_)
        bstack11l1lll111_opy_ = bstack11l1llll_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l1l11111l_opy_.format(str(e)))
      bstack111ll11111_opy_ += bstack11l1lll111_opy_
      bstack1l1l1ll11l_opy_(context, json.dumps(str(args[0].name) + bstack1ll11_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢත") + str(bstack1ll11111l_opy_)),
                          bstack1ll11_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣථ"))
      if runner.driver_initialised == bstack1ll11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣද"):
        bstack1ll11l1l1_opy_(getattr(context, bstack1ll11_opy_ (u"ࠫࡵࡧࡧࡦࠩධ"), None), bstack1ll11_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧන"), bstack111ll11111_opy_)
        bstack11l1111l11_opy_.execute_script(bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ඲") + json.dumps(str(args[0].name) + bstack1ll11_opy_ (u"ࠢࠡ࠯ࠣࡊࡦ࡯࡬ࡦࡦࠤࡠࡳࠨඳ") + str(bstack1ll11111l_opy_)) + bstack1ll11_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨප"))
      if runner.driver_initialised == bstack1ll11_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢඵ"):
        bstack11l11lll1l_opy_(bstack11l1111l11_opy_, bstack1ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪබ"), bstack1ll11_opy_ (u"ࠦࡘࡩࡥ࡯ࡣࡵ࡭ࡴࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣභ") + str(bstack111ll11111_opy_))
    else:
      bstack1l1l1ll11l_opy_(context, bstack1ll11_opy_ (u"ࠧࡖࡡࡴࡵࡨࡨࠦࠨම"), bstack1ll11_opy_ (u"ࠨࡩ࡯ࡨࡲࠦඹ"))
      if runner.driver_initialised == bstack1ll11_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧය"):
        bstack1ll11l1l1_opy_(getattr(context, bstack1ll11_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ර"), None), bstack1ll11_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ඼"))
      bstack11l1111l11_opy_.execute_script(bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨල") + json.dumps(str(args[0].name) + bstack1ll11_opy_ (u"ࠦࠥ࠳ࠠࡑࡣࡶࡷࡪࡪࠡࠣ඾")) + bstack1ll11_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫ඿"))
      if runner.driver_initialised == bstack1ll11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦව"):
        bstack11l11lll1l_opy_(bstack11l1111l11_opy_, bstack1ll11_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢශ"))
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥࡹࡴࡦࡲ࠽ࠤࢀࢃࠧෂ").format(str(e)))
  bstack1l1l1111l1_opy_(runner, name, context, args[0], bstack1ll11l111l_opy_, *args)
@measure(event_name=EVENTS.bstack111l11ll1l_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack111ll11l11_opy_(runner, name, context, bstack1ll11l111l_opy_, *args):
  bstack1llll1l111_opy_.end_test(args[0])
  try:
    bstack1l1ll111l1_opy_ = args[0].status.name
    bstack11l1111l11_opy_ = bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨස"), context.browser)
    bstack1l1l1ll1l_opy_.bstack1llll11l1l_opy_(bstack11l1111l11_opy_)
    if str(bstack1l1ll111l1_opy_).lower() == bstack1ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪහ"):
      bstack111ll11111_opy_ = bstack1ll11_opy_ (u"ࠫࠬළ")
      bstack1ll11111l_opy_ = bstack1ll11_opy_ (u"ࠬ࠭ෆ")
      bstack11l1lll111_opy_ = bstack1ll11_opy_ (u"࠭ࠧ෇")
      try:
        import traceback
        bstack111ll11111_opy_ = runner.exception.__class__.__name__
        bstack11l1llll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1ll11111l_opy_ = bstack1ll11_opy_ (u"ࠧࠡࠩ෈").join(bstack11l1llll_opy_)
        bstack11l1lll111_opy_ = bstack11l1llll_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l1l11111l_opy_.format(str(e)))
      bstack111ll11111_opy_ += bstack11l1lll111_opy_
      bstack1l1l1ll11l_opy_(context, json.dumps(str(args[0].name) + bstack1ll11_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢ෉") + str(bstack1ll11111l_opy_)),
                          bstack1ll11_opy_ (u"ࠤࡨࡶࡷࡵࡲ්ࠣ"))
      if runner.driver_initialised == bstack1ll11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ෋") or runner.driver_initialised == bstack1ll11_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫ෌"):
        bstack1ll11l1l1_opy_(getattr(context, bstack1ll11_opy_ (u"ࠬࡶࡡࡨࡧࠪ෍"), None), bstack1ll11_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ෎"), bstack111ll11111_opy_)
        bstack11l1111l11_opy_.execute_script(bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬා") + json.dumps(str(args[0].name) + bstack1ll11_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢැ") + str(bstack1ll11111l_opy_)) + bstack1ll11_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࡽࡾࠩෑ"))
      if runner.driver_initialised == bstack1ll11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧි") or runner.driver_initialised == bstack1ll11_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫී"):
        bstack11l11lll1l_opy_(bstack11l1111l11_opy_, bstack1ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬු"), bstack1ll11_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥ෕") + str(bstack111ll11111_opy_))
    else:
      bstack1l1l1ll11l_opy_(context, bstack1ll11_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣූ"), bstack1ll11_opy_ (u"ࠣ࡫ࡱࡪࡴࠨ෗"))
      if runner.driver_initialised == bstack1ll11_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦෘ") or runner.driver_initialised == bstack1ll11_opy_ (u"ࠪ࡭ࡳࡹࡴࡦࡲࠪෙ"):
        bstack1ll11l1l1_opy_(getattr(context, bstack1ll11_opy_ (u"ࠫࡵࡧࡧࡦࠩේ"), None), bstack1ll11_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧෛ"))
      bstack11l1111l11_opy_.execute_script(bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫො") + json.dumps(str(args[0].name) + bstack1ll11_opy_ (u"ࠢࠡ࠯ࠣࡔࡦࡹࡳࡦࡦࠤࠦෝ")) + bstack1ll11_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦࢂࢃࠧෞ"))
      if runner.driver_initialised == bstack1ll11_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦෟ") or runner.driver_initialised == bstack1ll11_opy_ (u"ࠪ࡭ࡳࡹࡴࡦࡲࠪ෠"):
        bstack11l11lll1l_opy_(bstack11l1111l11_opy_, bstack1ll11_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦ෡"))
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡪࡰࠣࡥ࡫ࡺࡥࡳࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧ෢").format(str(e)))
  bstack1l1l1111l1_opy_(runner, name, context, context.scenario, bstack1ll11l111l_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1ll1l1l11l_opy_(runner, name, context, bstack1ll11l111l_opy_, *args):
    target = context.scenario if hasattr(context, bstack1ll11_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ෣")) else context.feature
    bstack1l1l1111l1_opy_(runner, name, context, target, bstack1ll11l111l_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack11ll11l1ll_opy_(runner, name, context, bstack1ll11l111l_opy_, *args):
    try:
      bstack11l1111l11_opy_ = bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭෤"), context.browser)
      bstack1111l1ll11_opy_ = bstack1ll11_opy_ (u"ࠨࠩ෥")
      if context.failed is True:
        bstack1l111l1l1l_opy_ = []
        bstack1lll1lll1l_opy_ = []
        bstack11l11ll1ll_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1l111l1l1l_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l1llll_opy_ = traceback.format_tb(exc_tb)
            bstack1lll1l11l1_opy_ = bstack1ll11_opy_ (u"ࠩࠣࠫ෦").join(bstack11l1llll_opy_)
            bstack1lll1lll1l_opy_.append(bstack1lll1l11l1_opy_)
            bstack11l11ll1ll_opy_.append(bstack11l1llll_opy_[-1])
        except Exception as e:
          logger.debug(bstack1l1l11111l_opy_.format(str(e)))
        bstack111ll11111_opy_ = bstack1ll11_opy_ (u"ࠪࠫ෧")
        for i in range(len(bstack1l111l1l1l_opy_)):
          bstack111ll11111_opy_ += bstack1l111l1l1l_opy_[i] + bstack11l11ll1ll_opy_[i] + bstack1ll11_opy_ (u"ࠫࡡࡴࠧ෨")
        bstack1111l1ll11_opy_ = bstack1ll11_opy_ (u"ࠬࠦࠧ෩").join(bstack1lll1lll1l_opy_)
        if runner.driver_initialised in [bstack1ll11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢ෪"), bstack1ll11_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦ෫")]:
          bstack1l1l1ll11l_opy_(context, bstack1111l1ll11_opy_, bstack1ll11_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢ෬"))
          bstack1ll11l1l1_opy_(getattr(context, bstack1ll11_opy_ (u"ࠩࡳࡥ࡬࡫ࠧ෭"), None), bstack1ll11_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ෮"), bstack111ll11111_opy_)
          bstack11l1111l11_opy_.execute_script(bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ෯") + json.dumps(bstack1111l1ll11_opy_) + bstack1ll11_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤࢀࢁࠬ෰"))
          bstack11l11lll1l_opy_(bstack11l1111l11_opy_, bstack1ll11_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ෱"), bstack1ll11_opy_ (u"ࠢࡔࡱࡰࡩࠥࡹࡣࡦࡰࡤࡶ࡮ࡵࡳࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢ࡟ࡲࠧෲ") + str(bstack111ll11111_opy_))
          bstack1ll11ll1ll_opy_ = bstack1111l11ll1_opy_(bstack1111l1ll11_opy_, runner.feature.name, logger)
          if (bstack1ll11ll1ll_opy_ != None):
            bstack1llll11l11_opy_.append(bstack1ll11ll1ll_opy_)
      else:
        if runner.driver_initialised in [bstack1ll11_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤෳ"), bstack1ll11_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨ෴")]:
          bstack1l1l1ll11l_opy_(context, bstack1ll11_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨ࠾ࠥࠨ෵") + str(runner.feature.name) + bstack1ll11_opy_ (u"ࠦࠥࡶࡡࡴࡵࡨࡨࠦࠨ෶"), bstack1ll11_opy_ (u"ࠧ࡯࡮ࡧࡱࠥ෷"))
          bstack1ll11l1l1_opy_(getattr(context, bstack1ll11_opy_ (u"࠭ࡰࡢࡩࡨࠫ෸"), None), bstack1ll11_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ෹"))
          bstack11l1111l11_opy_.execute_script(bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭෺") + json.dumps(bstack1ll11_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧ࠽ࠤࠧ෻") + str(runner.feature.name) + bstack1ll11_opy_ (u"ࠥࠤࡵࡧࡳࡴࡧࡧࠥࠧ෼")) + bstack1ll11_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢࡾࡿࠪ෽"))
          bstack11l11lll1l_opy_(bstack11l1111l11_opy_, bstack1ll11_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ෾"))
          bstack1ll11ll1ll_opy_ = bstack1111l11ll1_opy_(bstack1111l1ll11_opy_, runner.feature.name, logger)
          if (bstack1ll11ll1ll_opy_ != None):
            bstack1llll11l11_opy_.append(bstack1ll11ll1ll_opy_)
    except Exception as e:
      logger.debug(bstack1ll11_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ෿").format(str(e)))
    bstack1l1l1111l1_opy_(runner, name, context, context.feature, bstack1ll11l111l_opy_, *args)
@measure(event_name=EVENTS.bstack1ll1ll1l1_opy_, stage=STAGE.bstack1111l1111_opy_, hook_type=bstack1ll11_opy_ (u"ࠢࡢࡨࡷࡩࡷࡇ࡬࡭ࠤ฀"), bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1ll11l11l_opy_(runner, name, context, bstack1ll11l111l_opy_, *args):
    bstack1l1l1111l1_opy_(runner, name, context, runner, bstack1ll11l111l_opy_, *args)
def bstack1l11l11111_opy_(self, name, context, *args):
  try:
    if bstack1lllll1l1l_opy_:
      platform_index = int(threading.current_thread()._name) % bstack1111llll1_opy_
      bstack11l1l11l1_opy_ = CONFIG[bstack1ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫก")][platform_index]
      os.environ[bstack1ll11_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪข")] = json.dumps(bstack11l1l11l1_opy_)
    global bstack1ll11l111l_opy_
    if not hasattr(self, bstack1ll11_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡸ࡫ࡤࠨฃ")):
      self.driver_initialised = None
    bstack1llllll11l_opy_ = {
        bstack1ll11_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠨค"): bstack1ll1l111ll_opy_,
        bstack1ll11_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ฅ"): bstack1l1ll1l1l1_opy_,
        bstack1ll11_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡴࡢࡩࠪฆ"): bstack1l1ll1ll1l_opy_,
        bstack1ll11_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩง"): bstack1ll11111ll_opy_,
        bstack1ll11_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵ࠭จ"): bstack1l111l11l1_opy_,
        bstack1ll11_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡷࡩࡵ࠭ฉ"): bstack1ll1111ll1_opy_,
        bstack1ll11_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫช"): bstack111ll11l11_opy_,
        bstack1ll11_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡸࡦ࡭ࠧซ"): bstack1ll1l1l11l_opy_,
        bstack1ll11_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠬฌ"): bstack11ll11l1ll_opy_,
        bstack1ll11_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩญ"): bstack1ll11l11l_opy_
    }
    handler = bstack1llllll11l_opy_.get(name, bstack1ll11l111l_opy_)
    try:
      handler(self, name, context, bstack1ll11l111l_opy_, *args)
    except Exception as e:
      logger.debug(bstack1ll11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦࠢ࡫ࡳࡴࡱࠠࡩࡣࡱࡨࡱ࡫ࡲࠡࡽࢀ࠾ࠥࢁࡽࠨฎ").format(name, str(e)))
    if name in [bstack1ll11_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨฏ"), bstack1ll11_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪฐ"), bstack1ll11_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡤࡰࡱ࠭ฑ")]:
      try:
        bstack11l1111l11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l1l1l11l_opy_(bstack1ll11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪฒ")) else context.browser
        bstack1111l11111_opy_ = (
          (name == bstack1ll11_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨณ") and self.driver_initialised == bstack1ll11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥด")) or
          (name == bstack1ll11_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧต") and self.driver_initialised == bstack1ll11_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤถ")) or
          (name == bstack1ll11_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪท") and self.driver_initialised in [bstack1ll11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧธ"), bstack1ll11_opy_ (u"ࠦ࡮ࡴࡳࡵࡧࡳࠦน")]) or
          (name == bstack1ll11_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡺࡥࡱࠩบ") and self.driver_initialised == bstack1ll11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦป"))
        )
        if bstack1111l11111_opy_:
          self.driver_initialised = None
          if bstack11l1111l11_opy_ and hasattr(bstack11l1111l11_opy_, bstack1ll11_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠫผ")):
            try:
              bstack11l1111l11_opy_.quit()
            except Exception as e:
              logger.debug(bstack1ll11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡲࡷ࡬ࡸࡹ࡯࡮ࡨࠢࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩࠥ࡮࡯ࡰ࡭࠽ࠤࢀࢃࠧฝ").format(str(e)))
      except Exception as e:
        logger.debug(bstack1ll11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣ࡬ࡴࡵ࡫ࠡࡥ࡯ࡩࡦࡴࡵࡱࠢࡩࡳࡷࠦࡻࡾ࠼ࠣࡿࢂ࠭พ").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"ࠪࡇࡷ࡯ࡴࡪࡥࡤࡰࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡳࡷࡱࠤ࡭ࡵ࡯࡬ࠢࡾࢁ࠿ࠦࡻࡾࠩฟ").format(name, str(e)))
    try:
      bstack1ll11l111l_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack1ll11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡱࡵ࡭࡬࡯࡮ࡢ࡮ࠣࡦࡪ࡮ࡡࡷࡧࠣ࡬ࡴࡵ࡫ࠡࡽࢀ࠾ࠥࢁࡽࠨภ").format(name, str(e2)))
def bstack11l11lll1_opy_(config, startdir):
  return bstack1ll11_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࠱ࡿࠥม").format(bstack1ll11_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧย"))
notset = Notset()
def bstack1lllllll1l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1l11l1ll1l_opy_
  if str(name).lower() == bstack1ll11_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸࠧร"):
    return bstack1ll11_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢฤ")
  else:
    return bstack1l11l1ll1l_opy_(self, name, default, skip)
def bstack11llll11ll_opy_(item, when):
  global bstack11l1ll111l_opy_
  try:
    bstack11l1ll111l_opy_(item, when)
  except Exception as e:
    pass
def bstack1ll1lll11_opy_():
  return
def bstack11ll111ll1_opy_(type, name, status, reason, bstack1l1lll111l_opy_, bstack11llll1lll_opy_):
  bstack1l111l1111_opy_ = {
    bstack1ll11_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩล"): type,
    bstack1ll11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ฦ"): {}
  }
  if type == bstack1ll11_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ว"):
    bstack1l111l1111_opy_[bstack1ll11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨศ")][bstack1ll11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬษ")] = bstack1l1lll111l_opy_
    bstack1l111l1111_opy_[bstack1ll11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪส")][bstack1ll11_opy_ (u"ࠨࡦࡤࡸࡦ࠭ห")] = json.dumps(str(bstack11llll1lll_opy_))
  if type == bstack1ll11_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪฬ"):
    bstack1l111l1111_opy_[bstack1ll11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭อ")][bstack1ll11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩฮ")] = name
  if type == bstack1ll11_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨฯ"):
    bstack1l111l1111_opy_[bstack1ll11_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩะ")][bstack1ll11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧั")] = status
    if status == bstack1ll11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨา"):
      bstack1l111l1111_opy_[bstack1ll11_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬำ")][bstack1ll11_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪิ")] = json.dumps(str(reason))
  bstack1l111lll11_opy_ = bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩี").format(json.dumps(bstack1l111l1111_opy_))
  return bstack1l111lll11_opy_
def bstack111lllll1l_opy_(driver_command, response):
    if driver_command == bstack1ll11_opy_ (u"ࠬࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩึ"):
        bstack1ll111l1_opy_.bstack1l1l1l111l_opy_({
            bstack1ll11_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬื"): response[bstack1ll11_opy_ (u"ࠧࡷࡣ࡯ࡹࡪุ࠭")],
            bstack1ll11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨู"): bstack1ll111l1_opy_.current_test_uuid()
        })
def bstack111111lll_opy_(item, call, rep):
  global bstack11l1lllll1_opy_
  global bstack1111l1l1l1_opy_
  global bstack1ll11lll11_opy_
  name = bstack1ll11_opy_ (u"ฺࠩࠪ")
  try:
    if rep.when == bstack1ll11_opy_ (u"ࠪࡧࡦࡲ࡬ࠨ฻"):
      bstack11l1ll1l1_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1ll11lll11_opy_:
          name = str(rep.nodeid)
          bstack1lll11l11_opy_ = bstack11ll111ll1_opy_(bstack1ll11_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ฼"), name, bstack1ll11_opy_ (u"ࠬ࠭฽"), bstack1ll11_opy_ (u"࠭ࠧ฾"), bstack1ll11_opy_ (u"ࠧࠨ฿"), bstack1ll11_opy_ (u"ࠨࠩเ"))
          threading.current_thread().bstack11llll1l1_opy_ = name
          for driver in bstack1111l1l1l1_opy_:
            if bstack11l1ll1l1_opy_ == driver.session_id:
              driver.execute_script(bstack1lll11l11_opy_)
      except Exception as e:
        logger.debug(bstack1ll11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠩแ").format(str(e)))
      try:
        bstack111llll111_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1ll11_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫโ"):
          status = bstack1ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫใ") if rep.outcome.lower() == bstack1ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬไ") else bstack1ll11_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ๅ")
          reason = bstack1ll11_opy_ (u"ࠧࠨๆ")
          if status == bstack1ll11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ็"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1ll11_opy_ (u"ࠩ࡬ࡲ࡫ࡵ่ࠧ") if status == bstack1ll11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦ้ࠪ") else bstack1ll11_opy_ (u"ࠫࡪࡸࡲࡰࡴ๊ࠪ")
          data = name + bstack1ll11_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩ๋ࠧࠧ") if status == bstack1ll11_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭์") else name + bstack1ll11_opy_ (u"ࠧࠡࡨࡤ࡭ࡱ࡫ࡤࠢࠢࠪํ") + reason
          bstack111ll1llll_opy_ = bstack11ll111ll1_opy_(bstack1ll11_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪ๎"), bstack1ll11_opy_ (u"ࠩࠪ๏"), bstack1ll11_opy_ (u"ࠪࠫ๐"), bstack1ll11_opy_ (u"ࠫࠬ๑"), level, data)
          for driver in bstack1111l1l1l1_opy_:
            if bstack11l1ll1l1_opy_ == driver.session_id:
              driver.execute_script(bstack111ll1llll_opy_)
      except Exception as e:
        logger.debug(bstack1ll11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡦࡳࡳࡺࡥࡹࡶࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠩ๒").format(str(e)))
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡶࡸࡦࡺࡥࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࠦࡳࡵࡣࡷࡹࡸࡀࠠࡼࡿࠪ๓").format(str(e)))
  bstack11l1lllll1_opy_(item, call, rep)
def bstack11l1l11ll1_opy_(driver, bstack1l1llllll1_opy_, test=None):
  global bstack1ll1l1lll_opy_
  if test != None:
    bstack1l1ll1111l_opy_ = getattr(test, bstack1ll11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ๔"), None)
    bstack1lll111l1l_opy_ = getattr(test, bstack1ll11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭๕"), None)
    PercySDK.screenshot(driver, bstack1l1llllll1_opy_, bstack1l1ll1111l_opy_=bstack1l1ll1111l_opy_, bstack1lll111l1l_opy_=bstack1lll111l1l_opy_, bstack1ll111llll_opy_=bstack1ll1l1lll_opy_)
  else:
    PercySDK.screenshot(driver, bstack1l1llllll1_opy_)
@measure(event_name=EVENTS.bstack1l11111l1_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack111l1l1111_opy_(driver):
  if bstack1l1ll111l_opy_.bstack1ll1111l1l_opy_() is True or bstack1l1ll111l_opy_.capturing() is True:
    return
  bstack1l1ll111l_opy_.bstack11l1l1ll11_opy_()
  while not bstack1l1ll111l_opy_.bstack1ll1111l1l_opy_():
    bstack1111ll11ll_opy_ = bstack1l1ll111l_opy_.bstack11ll1l11l_opy_()
    bstack11l1l11ll1_opy_(driver, bstack1111ll11ll_opy_)
  bstack1l1ll111l_opy_.bstack1ll1ll1ll_opy_()
def bstack11ll1l111l_opy_(sequence, driver_command, response = None, bstack11ll1lll1_opy_ = None, args = None):
    try:
      if sequence != bstack1ll11_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩ๖"):
        return
      if percy.bstack1l1l1llll_opy_() == bstack1ll11_opy_ (u"ࠥࡪࡦࡲࡳࡦࠤ๗"):
        return
      bstack1111ll11ll_opy_ = bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ๘"), None)
      for command in bstack1l1111l111_opy_:
        if command == driver_command:
          with bstack1l11l1l1l_opy_:
            bstack11ll1lll1l_opy_ = bstack1111l1l1l1_opy_.copy()
          for driver in bstack11ll1lll1l_opy_:
            bstack111l1l1111_opy_(driver)
      bstack1ll11ll1l_opy_ = percy.bstack11l1111l1l_opy_()
      if driver_command in bstack1ll1l1l111_opy_[bstack1ll11ll1l_opy_]:
        bstack1l1ll111l_opy_.bstack111lll1l1_opy_(bstack1111ll11ll_opy_, driver_command)
    except Exception as e:
      pass
def bstack11ll1l1l11_opy_(framework_name):
  if bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡳ࡯ࡥࡡࡦࡥࡱࡲࡥࡥࠩ๙")):
      return
  bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ๚"), True)
  global bstack1l111llll_opy_
  global bstack1l1l11llll_opy_
  global bstack1ll111l11_opy_
  bstack1l111llll_opy_ = framework_name
  logger.info(bstack1llll11111_opy_.format(bstack1l111llll_opy_.split(bstack1ll11_opy_ (u"ࠧ࠮ࠩ๛"))[0]))
  bstack11l111l11_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1lllll1l1l_opy_:
      Service.start = bstack1lll1111ll_opy_
      Service.stop = bstack1lll1l1lll_opy_
      webdriver.Remote.get = bstack1111l1111l_opy_
      WebDriver.quit = bstack11lll1111_opy_
      webdriver.Remote.__init__ = bstack1l111ll11l_opy_
    if not bstack1lllll1l1l_opy_:
        webdriver.Remote.__init__ = bstack1ll1l1l1l_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack1lll11ll11_opy_
    bstack1l1l11llll_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1lllll1l1l_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack111l1llll_opy_
  except Exception as e:
    pass
  bstack1ll111l1l_opy_()
  if not bstack1l1l11llll_opy_:
    bstack1ll1lllll1_opy_(bstack1ll11_opy_ (u"ࠣࡒࡤࡧࡰࡧࡧࡦࡵࠣࡲࡴࡺࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠥ๜"), bstack1l111111l1_opy_)
  if bstack111l1l1l11_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack1ll11_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ๝")) and callable(getattr(RemoteConnection, bstack1ll11_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ๞"))):
        RemoteConnection._get_proxy_url = bstack1l11111ll1_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack1l11111ll1_opy_
    except Exception as e:
      logger.error(bstack111llllll_opy_.format(str(e)))
  if bstack1l11l1ll1_opy_():
    bstack11lll11l11_opy_(CONFIG, logger)
  if (bstack1ll11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ๟") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1l1l1llll_opy_() == bstack1ll11_opy_ (u"ࠧࡺࡲࡶࡧࠥ๠"):
          bstack1l111111ll_opy_(bstack11ll1l111l_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1l11l11l11_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1111111ll_opy_
      except Exception as e:
        logger.warn(bstack1ll1l1lll1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1l1l1llll1_opy_
      except Exception as e:
        logger.debug(bstack11l1llll11_opy_ + str(e))
    except Exception as e:
      bstack1ll1lllll1_opy_(e, bstack1ll1l1lll1_opy_)
    Output.start_test = bstack1l1lllll1l_opy_
    Output.end_test = bstack1lllll1l11_opy_
    TestStatus.__init__ = bstack1ll1llllll_opy_
    QueueItem.__init__ = bstack11l111l11l_opy_
    pabot._create_items = bstack1lll1lllll_opy_
    try:
      from pabot import __version__ as bstack1l1ll1l111_opy_
      if version.parse(bstack1l1ll1l111_opy_) >= version.parse(bstack1ll11_opy_ (u"࠭࠵࠯࠲࠱࠴ࠬ๡")):
        pabot._run = bstack1l111l1l1_opy_
      elif version.parse(bstack1l1ll1l111_opy_) >= version.parse(bstack1ll11_opy_ (u"ࠧ࠵࠰࠵࠲࠵࠭๢")):
        pabot._run = bstack11l11ll1l_opy_
      elif version.parse(bstack1l1ll1l111_opy_) >= version.parse(bstack1ll11_opy_ (u"ࠨ࠴࠱࠵࠺࠴࠰ࠨ๣")):
        pabot._run = bstack1lll1lll11_opy_
      elif version.parse(bstack1l1ll1l111_opy_) >= version.parse(bstack1ll11_opy_ (u"ࠩ࠵࠲࠶࠹࠮࠱ࠩ๤")):
        pabot._run = bstack11ll1ll1l1_opy_
      else:
        pabot._run = bstack111l11111_opy_
    except Exception as e:
      pabot._run = bstack111l11111_opy_
    pabot._create_command_for_execution = bstack11l1l1l111_opy_
    pabot._report_results = bstack1ll11lll1_opy_
  if bstack1ll11_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ๥") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll1lllll1_opy_(e, bstack11l1l11l1l_opy_)
    Runner.run_hook = bstack1l11l11111_opy_
    Step.run = bstack1lllll1ll1_opy_
  if bstack1ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ๦") in str(framework_name).lower():
    if not bstack1lllll1l1l_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack11l11lll1_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1ll1lll11_opy_
      Config.getoption = bstack1lllllll1l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack111111lll_opy_
    except Exception as e:
      pass
def bstack111ll1ll11_opy_():
  global CONFIG
  if bstack1ll11_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ๧") in CONFIG and int(CONFIG[bstack1ll11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭๨")]) > 1:
    logger.warn(bstack11l111l1ll_opy_)
def bstack1llll1ll11_opy_(arg, bstack11111ll1_opy_, bstack11ll1ll11l_opy_=None):
  global CONFIG
  global bstack11l111111l_opy_
  global bstack111l1l111_opy_
  global bstack1lllll1l1l_opy_
  global bstack1111ll11_opy_
  bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ๩")
  if bstack11111ll1_opy_ and isinstance(bstack11111ll1_opy_, str):
    bstack11111ll1_opy_ = eval(bstack11111ll1_opy_)
  CONFIG = bstack11111ll1_opy_[bstack1ll11_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨ๪")]
  bstack11l111111l_opy_ = bstack11111ll1_opy_[bstack1ll11_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪ๫")]
  bstack111l1l111_opy_ = bstack11111ll1_opy_[bstack1ll11_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ๬")]
  bstack1lllll1l1l_opy_ = bstack11111ll1_opy_[bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ๭")]
  bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭๮"), bstack1lllll1l1l_opy_)
  os.environ[bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ๯")] = bstack111lll111_opy_
  os.environ[bstack1ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌ࠭๰")] = json.dumps(CONFIG)
  os.environ[bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡉࡗࡅࡣ࡚ࡘࡌࠨ๱")] = bstack11l111111l_opy_
  os.environ[bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ๲")] = str(bstack111l1l111_opy_)
  os.environ[bstack1ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡐ࡚ࡍࡉࡏࠩ๳")] = str(True)
  if bstack1111l11l1_opy_(arg, [bstack1ll11_opy_ (u"ࠫ࠲ࡴࠧ๴"), bstack1ll11_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭๵")]) != -1:
    os.environ[bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡁࡓࡃࡏࡐࡊࡒࠧ๶")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1l1111l1l1_opy_)
    return
  bstack11l11l111l_opy_()
  global bstack11l1llll1_opy_
  global bstack1ll1l1lll_opy_
  global bstack1l1l1111l_opy_
  global bstack1ll111l111_opy_
  global bstack1ll11llll1_opy_
  global bstack1ll111l11_opy_
  global bstack1l11lll11_opy_
  arg.append(bstack1ll11_opy_ (u"ࠢ࠮࡙ࠥ๷"))
  arg.append(bstack1ll11_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥ࠻ࡏࡲࡨࡺࡲࡥࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡬ࡱࡵࡵࡲࡵࡧࡧ࠾ࡵࡿࡴࡦࡵࡷ࠲ࡕࡿࡴࡦࡵࡷ࡛ࡦࡸ࡮ࡪࡰࡪࠦ๸"))
  arg.append(bstack1ll11_opy_ (u"ࠤ࠰࡛ࠧ๹"))
  arg.append(bstack1ll11_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧ࠽ࡘ࡭࡫ࠠࡩࡱࡲ࡯࡮ࡳࡰ࡭ࠤ๺"))
  global bstack11l1ll1lll_opy_
  global bstack1111l1l11_opy_
  global bstack11111ll11_opy_
  global bstack1ll111ll11_opy_
  global bstack1111lll111_opy_
  global bstack1l11ll11l_opy_
  global bstack1ll1l1ll1l_opy_
  global bstack1111ll11l1_opy_
  global bstack11ll1llll1_opy_
  global bstack1l11llll1_opy_
  global bstack1l11l1ll1l_opy_
  global bstack11l1ll111l_opy_
  global bstack11l1lllll1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11l1ll1lll_opy_ = webdriver.Remote.__init__
    bstack1111l1l11_opy_ = WebDriver.quit
    bstack1111ll11l1_opy_ = WebDriver.close
    bstack11ll1llll1_opy_ = WebDriver.get
    bstack11111ll11_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack111l111l1_opy_(CONFIG) and bstack11l111ll1l_opy_():
    if bstack1llll1l1l1_opy_() < version.parse(bstack111llll1l_opy_):
      logger.error(bstack111111ll1_opy_.format(bstack1llll1l1l1_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1ll11_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ๻")) and callable(getattr(RemoteConnection, bstack1ll11_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭๼"))):
          bstack1l11llll1_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1l11llll1_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack111llllll_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1l11l1ll1l_opy_ = Config.getoption
    from _pytest import runner
    bstack11l1ll111l_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack11l11l11_opy_)
  try:
    from pytest_bdd import reporting
    bstack11l1lllll1_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1ll11_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹࡵࠠࡳࡷࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࡹࠧ๽"))
  bstack1l1l1111l_opy_ = CONFIG.get(bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ๾"), {}).get(bstack1ll11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ๿"))
  bstack1l11lll11_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack11ll11ll1_opy_():
      bstack1ll1ll111_opy_.invoke(Events.CONNECT, bstack1ll11l1l1l_opy_())
    platform_index = int(os.environ.get(bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ຀"), bstack1ll11_opy_ (u"ࠪ࠴ࠬກ")))
  else:
    bstack11ll1l1l11_opy_(bstack111l11l11_opy_)
  os.environ[bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬຂ")] = CONFIG[bstack1ll11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ຃")]
  os.environ[bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩຄ")] = CONFIG[bstack1ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ຅")]
  os.environ[bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫຆ")] = bstack1lllll1l1l_opy_.__str__()
  from _pytest.config import main as bstack111l11l11l_opy_
  bstack11llllllll_opy_ = []
  try:
    exit_code = bstack111l11l11l_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1l1ll11111_opy_()
    if bstack1ll11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭ງ") in multiprocessing.current_process().__dict__.keys():
      for bstack111l11llll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11llllllll_opy_.append(bstack111l11llll_opy_)
    try:
      bstack1l1111111l_opy_ = (bstack11llllllll_opy_, int(exit_code))
      bstack11ll1ll11l_opy_.append(bstack1l1111111l_opy_)
    except:
      bstack11ll1ll11l_opy_.append((bstack11llllllll_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack11llllllll_opy_.append({bstack1ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨຈ"): bstack1ll11_opy_ (u"ࠫࡕࡸ࡯ࡤࡧࡶࡷࠥ࠭ຉ") + os.environ.get(bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬຊ")), bstack1ll11_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ຋"): traceback.format_exc(), bstack1ll11_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ຌ"): int(os.environ.get(bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨຍ")))})
    bstack11ll1ll11l_opy_.append((bstack11llllllll_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack1ll11_opy_ (u"ࠤࡵࡩࡹࡸࡩࡦࡵࠥຎ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack11lll11ll_opy_ = e.__class__.__name__
    print(bstack1ll11_opy_ (u"ࠥࠩࡸࡀࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡵࡧࡶࡸࠥࠫࡳࠣຏ") % (bstack11lll11ll_opy_, e))
    return 1
def bstack1lll1l1ll1_opy_(arg):
  global bstack11ll1111l1_opy_
  bstack11ll1l1l11_opy_(bstack111ll111l1_opy_)
  os.environ[bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬຐ")] = str(bstack111l1l111_opy_)
  retries = bstack11l11l1l_opy_.bstack111lllll_opy_(CONFIG)
  status_code = 0
  if bstack11l11l1l_opy_.bstack11111111_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack1l1lll1ll_opy_
    status_code = bstack1l1lll1ll_opy_(arg)
  if status_code != 0:
    bstack11ll1111l1_opy_ = status_code
def bstack11lll1l11l_opy_():
  logger.info(bstack111lll1111_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1ll11_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫຑ"), help=bstack1ll11_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡤࡱࡱࡪ࡮࡭ࠧຒ"))
  parser.add_argument(bstack1ll11_opy_ (u"ࠧ࠮ࡷࠪຓ"), bstack1ll11_opy_ (u"ࠨ࠯࠰ࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬດ"), help=bstack1ll11_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡵࡴࡧࡵࡲࡦࡳࡥࠨຕ"))
  parser.add_argument(bstack1ll11_opy_ (u"ࠪ࠱ࡰ࠭ຖ"), bstack1ll11_opy_ (u"ࠫ࠲࠳࡫ࡦࡻࠪທ"), help=bstack1ll11_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾ࠭ຘ"))
  parser.add_argument(bstack1ll11_opy_ (u"࠭࠭ࡧࠩນ"), bstack1ll11_opy_ (u"ࠧ࠮࠯ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬບ"), help=bstack1ll11_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧປ"))
  bstack1lll11l11l_opy_ = parser.parse_args()
  try:
    bstack1l1lll1111_opy_ = bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡩࡨࡲࡪࡸࡩࡤ࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭ຜ")
    if bstack1lll11l11l_opy_.framework and bstack1lll11l11l_opy_.framework not in (bstack1ll11_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪຝ"), bstack1ll11_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬພ")):
      bstack1l1lll1111_opy_ = bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࡺ࡯࡯࠲ࡸࡧ࡭ࡱ࡮ࡨࠫຟ")
    bstack1l1llll111_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1lll1111_opy_)
    bstack1111lll11l_opy_ = open(bstack1l1llll111_opy_, bstack1ll11_opy_ (u"࠭ࡲࠨຠ"))
    bstack1llll1llll_opy_ = bstack1111lll11l_opy_.read()
    bstack1111lll11l_opy_.close()
    if bstack1lll11l11l_opy_.username:
      bstack1llll1llll_opy_ = bstack1llll1llll_opy_.replace(bstack1ll11_opy_ (u"࡚ࠧࡑࡘࡖࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧມ"), bstack1lll11l11l_opy_.username)
    if bstack1lll11l11l_opy_.key:
      bstack1llll1llll_opy_ = bstack1llll1llll_opy_.replace(bstack1ll11_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪຢ"), bstack1lll11l11l_opy_.key)
    if bstack1lll11l11l_opy_.framework:
      bstack1llll1llll_opy_ = bstack1llll1llll_opy_.replace(bstack1ll11_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪຣ"), bstack1lll11l11l_opy_.framework)
    file_name = bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭຤")
    file_path = os.path.abspath(file_name)
    bstack1ll1l11l1_opy_ = open(file_path, bstack1ll11_opy_ (u"ࠫࡼ࠭ລ"))
    bstack1ll1l11l1_opy_.write(bstack1llll1llll_opy_)
    bstack1ll1l11l1_opy_.close()
    logger.info(bstack11ll111l1l_opy_)
    try:
      os.environ[bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ຦")] = bstack1lll11l11l_opy_.framework if bstack1lll11l11l_opy_.framework != None else bstack1ll11_opy_ (u"ࠨࠢວ")
      config = yaml.safe_load(bstack1llll1llll_opy_)
      config[bstack1ll11_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧຨ")] = bstack1ll11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠮ࡵࡨࡸࡺࡶࠧຩ")
      bstack1lll11ll1l_opy_(bstack111111l1l_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll11ll111_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1l1lll1l1l_opy_.format(str(e)))
def bstack1lll11ll1l_opy_(bstack1l11ll11ll_opy_, config, bstack11lllllll_opy_={}):
  global bstack1lllll1l1l_opy_
  global bstack11lll1l1ll_opy_
  global bstack1111ll11_opy_
  if not config:
    return
  bstack11111l1lll_opy_ = bstack1l1l111ll_opy_ if not bstack1lllll1l1l_opy_ else (
    bstack1l1ll1lll1_opy_ if bstack1ll11_opy_ (u"ࠩࡤࡴࡵ࠭ສ") in config else (
        bstack11l11l111_opy_ if config.get(bstack1ll11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧຫ")) else bstack11ll1ll1l_opy_
    )
)
  bstack11l11ll11l_opy_ = False
  bstack111ll11l1_opy_ = False
  if bstack1lllll1l1l_opy_ is True:
      if bstack1ll11_opy_ (u"ࠫࡦࡶࡰࠨຬ") in config:
          bstack11l11ll11l_opy_ = True
      else:
          bstack111ll11l1_opy_ = True
  bstack11llll1ll1_opy_ = bstack11l1l1ll1_opy_.bstack1111l1lll_opy_(config, bstack11lll1l1ll_opy_)
  bstack11l111ll11_opy_ = bstack11ll111111_opy_()
  data = {
    bstack1ll11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧອ"): config[bstack1ll11_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨຮ")],
    bstack1ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪຯ"): config[bstack1ll11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫະ")],
    bstack1ll11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ັ"): bstack1l11ll11ll_opy_,
    bstack1ll11_opy_ (u"ࠪࡨࡪࡺࡥࡤࡶࡨࡨࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧາ"): os.environ.get(bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ຳ"), bstack11lll1l1ll_opy_),
    bstack1ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧິ"): bstack111l111ll1_opy_,
    bstack1ll11_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬ࠨີ"): bstack111l1l1ll_opy_(),
    bstack1ll11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪຶ"): {
      bstack1ll11_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ື"): str(config[bstack1ll11_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦຸࠩ")]) if bstack1ll11_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧູࠪ") in config else bstack1ll11_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲ຺ࠧ"),
      bstack1ll11_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࡖࡦࡴࡶ࡭ࡴࡴࠧົ"): sys.version,
      bstack1ll11_opy_ (u"࠭ࡲࡦࡨࡨࡶࡷ࡫ࡲࠨຼ"): bstack1l11llllll_opy_(os.environ.get(bstack1ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩຽ"), bstack11lll1l1ll_opy_)),
      bstack1ll11_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪ຾"): bstack1ll11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ຿"),
      bstack1ll11_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫເ"): bstack11111l1lll_opy_,
      bstack1ll11_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࡤࡳࡡࡱࠩແ"): bstack11llll1ll1_opy_,
      bstack1ll11_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡥࡵࡶ࡫ࡧࠫໂ"): os.environ[bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫໃ")],
      bstack1ll11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪໄ"): os.environ.get(bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ໅"), bstack11lll1l1ll_opy_),
      bstack1ll11_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬໆ"): bstack1l11lllll_opy_(os.environ.get(bstack1ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ໇"), bstack11lll1l1ll_opy_)),
      bstack1ll11_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭່ࠪ"): bstack11l111ll11_opy_.get(bstack1ll11_opy_ (u"ࠬࡴࡡ࡮ࡧ້ࠪ")),
      bstack1ll11_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲ໊ࠬ"): bstack11l111ll11_opy_.get(bstack1ll11_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ໋")),
      bstack1ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ໌"): config[bstack1ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬໍ")] if config[bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໎")] else bstack1ll11_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧ໏"),
      bstack1ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ໐"): str(config[bstack1ll11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ໑")]) if bstack1ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ໒") in config else bstack1ll11_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤ໓"),
      bstack1ll11_opy_ (u"ࠩࡲࡷࠬ໔"): sys.platform,
      bstack1ll11_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬ໕"): socket.gethostname(),
      bstack1ll11_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭໖"): bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ໗"))
    }
  }
  if not bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭໘")) is None:
    data[bstack1ll11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ໙")][bstack1ll11_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡐࡩࡹࡧࡤࡢࡶࡤࠫ໚")] = {
      bstack1ll11_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩ໛"): bstack1ll11_opy_ (u"ࠪࡹࡸ࡫ࡲࡠ࡭࡬ࡰࡱ࡫ࡤࠨໜ"),
      bstack1ll11_opy_ (u"ࠫࡸ࡯ࡧ࡯ࡣ࡯ࠫໝ"): bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬໞ")),
      bstack1ll11_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱࡔࡵ࡮ࡤࡨࡶࠬໟ"): bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡏࡱࠪ໠"))
    }
  if bstack1l11ll11ll_opy_ == bstack11lllll111_opy_:
    data[bstack1ll11_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໡")][bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡄࡱࡱࡪ࡮࡭ࠧ໢")] = bstack1ll1l11lll_opy_(config)
    data[bstack1ll11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໣")][bstack1ll11_opy_ (u"ࠫ࡮ࡹࡐࡦࡴࡦࡽࡆࡻࡴࡰࡇࡱࡥࡧࡲࡥࡥࠩ໤")] = percy.bstack1lll111ll1_opy_
    data[bstack1ll11_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ໥")][bstack1ll11_opy_ (u"࠭ࡰࡦࡴࡦࡽࡇࡻࡩ࡭ࡦࡌࡨࠬ໦")] = percy.percy_build_id
  if not bstack11l11l1l_opy_.bstack1l1l11l1ll_opy_(CONFIG):
    data[bstack1ll11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ໧")][bstack1ll11_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠬ໨")] = bstack11l11l1l_opy_.bstack1l1l11l1ll_opy_(CONFIG)
  bstack1llllll1l_opy_ = bstack1llll1l1l_opy_.bstack1llll11l1_opy_(CONFIG, logger)
  bstack1lll1ll1l_opy_ = bstack11l11l1l_opy_.bstack1llll11l1_opy_(config=CONFIG)
  if bstack1llllll1l_opy_ is not None and bstack1lll1ll1l_opy_ is not None and bstack1lll1ll1l_opy_.bstack1lllll111_opy_():
    data[bstack1ll11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໩")][bstack1lll1ll1l_opy_.bstack11lll11ll1_opy_()] = bstack1llllll1l_opy_.bstack1l1111lll1_opy_()
  update(data[bstack1ll11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໪")], bstack11lllllll_opy_)
  try:
    response = bstack11ll1llll_opy_(bstack1ll11_opy_ (u"ࠫࡕࡕࡓࡕࠩ໫"), bstack111lll1ll_opy_(bstack11ll11l111_opy_), data, {
      bstack1ll11_opy_ (u"ࠬࡧࡵࡵࡪࠪ໬"): (config[bstack1ll11_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ໭")], config[bstack1ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ໮")])
    })
    if response:
      logger.debug(bstack11lll11l1l_opy_.format(bstack1l11ll11ll_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1111llll11_opy_.format(str(e)))
def bstack1l11llllll_opy_(framework):
  return bstack1ll11_opy_ (u"ࠣࡽࢀ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧ໯").format(str(framework), __version__) if framework else bstack1ll11_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࡼࡿࠥ໰").format(
    __version__)
def bstack11l11l111l_opy_():
  global CONFIG
  global bstack11l1l111l_opy_
  if bool(CONFIG):
    return
  try:
    bstack1l11l111l_opy_()
    logger.debug(bstack11l1l11ll_opy_.format(str(CONFIG)))
    bstack11l1l111l_opy_ = bstack1l1l1l1111_opy_.configure_logger(CONFIG, bstack11l1l111l_opy_)
    bstack11l111l11_opy_()
  except Exception as e:
    logger.error(bstack1ll11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴ࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࠢ໱") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11l1ll111_opy_
  atexit.register(bstack1l1111lll_opy_)
  signal.signal(signal.SIGINT, bstack11l1l1l1l_opy_)
  signal.signal(signal.SIGTERM, bstack11l1l1l1l_opy_)
def bstack11l1ll111_opy_(exctype, value, traceback):
  global bstack1111l1l1l1_opy_
  try:
    for driver in bstack1111l1l1l1_opy_:
      bstack11l11lll1l_opy_(driver, bstack1ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ໲"), bstack1ll11_opy_ (u"࡙ࠧࡥࡴࡵ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣ໳") + str(value))
  except Exception:
    pass
  logger.info(bstack1l1l11ll1l_opy_)
  bstack1l1l11l11_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l1l11l11_opy_(message=bstack1ll11_opy_ (u"࠭ࠧ໴"), bstack1ll1lllll_opy_ = False):
  global CONFIG
  bstack11l1l1l1l1_opy_ = bstack1ll11_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠩ໵") if bstack1ll1lllll_opy_ else bstack1ll11_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ໶")
  try:
    if message:
      bstack11lllllll_opy_ = {
        bstack11l1l1l1l1_opy_ : str(message)
      }
      bstack1lll11ll1l_opy_(bstack11lllll111_opy_, CONFIG, bstack11lllllll_opy_)
    else:
      bstack1lll11ll1l_opy_(bstack11lllll111_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1l111l1ll1_opy_.format(str(e)))
def bstack1l1lll1lll_opy_(bstack1l1lll11l_opy_, size):
  bstack1lll11l111_opy_ = []
  while len(bstack1l1lll11l_opy_) > size:
    bstack1llll1ll1l_opy_ = bstack1l1lll11l_opy_[:size]
    bstack1lll11l111_opy_.append(bstack1llll1ll1l_opy_)
    bstack1l1lll11l_opy_ = bstack1l1lll11l_opy_[size:]
  bstack1lll11l111_opy_.append(bstack1l1lll11l_opy_)
  return bstack1lll11l111_opy_
def bstack111l1l1l1_opy_(args):
  if bstack1ll11_opy_ (u"ࠩ࠰ࡱࠬ໷") in args and bstack1ll11_opy_ (u"ࠪࡴࡩࡨࠧ໸") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack11l1111ll_opy_, stage=STAGE.bstack11l111lll_opy_)
def run_on_browserstack(bstack11l1l1llll_opy_=None, bstack11ll1ll11l_opy_=None, bstack1l1l11l11l_opy_=False):
  global CONFIG
  global bstack11l111111l_opy_
  global bstack111l1l111_opy_
  global bstack11lll1l1ll_opy_
  global bstack1111ll11_opy_
  bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠫࠬ໹")
  bstack1l111l11l_opy_(bstack11lll1l11_opy_, logger)
  if bstack11l1l1llll_opy_ and isinstance(bstack11l1l1llll_opy_, str):
    bstack11l1l1llll_opy_ = eval(bstack11l1l1llll_opy_)
  if bstack11l1l1llll_opy_:
    CONFIG = bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ໺")]
    bstack11l111111l_opy_ = bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ໻")]
    bstack111l1l111_opy_ = bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ໼")]
    bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ໽"), bstack111l1l111_opy_)
    bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ໾")
  bstack1111ll11_opy_.set_property(bstack1ll11_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ໿"), uuid4().__str__())
  logger.info(bstack1ll11_opy_ (u"ࠫࡘࡊࡋࠡࡴࡸࡲࠥࡹࡴࡢࡴࡷࡩࡩࠦࡷࡪࡶ࡫ࠤ࡮ࡪ࠺ࠡࠩༀ") + bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ༁")));
  logger.debug(bstack1ll11_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤ࠾ࠩ༂") + bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ༃")))
  if not bstack1l1l11l11l_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1l1111l1l1_opy_)
      return
    if sys.argv[1] == bstack1ll11_opy_ (u"ࠨ࠯࠰ࡺࡪࡸࡳࡪࡱࡱࠫ༄") or sys.argv[1] == bstack1ll11_opy_ (u"ࠩ࠰ࡺࠬ༅"):
      logger.info(bstack1ll11_opy_ (u"ࠪࡆࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡓࡽࡹ࡮࡯࡯ࠢࡖࡈࡐࠦࡶࡼࡿࠪ༆").format(__version__))
      return
    if sys.argv[1] == bstack1ll11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ༇"):
      bstack11lll1l11l_opy_()
      return
  args = sys.argv
  bstack11l11l111l_opy_()
  global bstack11l1llll1_opy_
  global bstack1111llll1_opy_
  global bstack1l11lll11_opy_
  global bstack111llll1l1_opy_
  global bstack1ll1l1lll_opy_
  global bstack1l1l1111l_opy_
  global bstack1ll111l111_opy_
  global bstack11llll11l_opy_
  global bstack1ll11llll1_opy_
  global bstack1ll111l11_opy_
  global bstack1l11lll1ll_opy_
  bstack1111llll1_opy_ = len(CONFIG.get(bstack1ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ༈"), []))
  if not bstack111lll111_opy_:
    if args[1] == bstack1ll11_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭༉") or args[1] == bstack1ll11_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨ༊"):
      bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ་")
      args = args[2:]
    elif args[1] == bstack1ll11_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ༌"):
      bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ།")
      args = args[2:]
    elif args[1] == bstack1ll11_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ༎"):
      bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ༏")
      args = args[2:]
    elif args[1] == bstack1ll11_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ༐"):
      bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ༑")
      args = args[2:]
    elif args[1] == bstack1ll11_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ༒"):
      bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ༓")
      args = args[2:]
    elif args[1] == bstack1ll11_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ༔"):
      bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ༕")
      args = args[2:]
    else:
      if not bstack1ll11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ༖") in CONFIG or str(CONFIG[bstack1ll11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༗")]).lower() in [bstack1ll11_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ༘ࠧ"), bstack1ll11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴༙ࠩ")]:
        bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༚")
        args = args[1:]
      elif str(CONFIG[bstack1ll11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭༛")]).lower() == bstack1ll11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༜"):
        bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༝")
        args = args[1:]
      elif str(CONFIG[bstack1ll11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༞")]).lower() == bstack1ll11_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭༟"):
        bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ༠")
        args = args[1:]
      elif str(CONFIG[bstack1ll11_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ༡")]).lower() == bstack1ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ༢"):
        bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༣")
        args = args[1:]
      elif str(CONFIG[bstack1ll11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ༤")]).lower() == bstack1ll11_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭༥"):
        bstack111lll111_opy_ = bstack1ll11_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ༦")
        args = args[1:]
      else:
        os.environ[bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ༧")] = bstack111lll111_opy_
        bstack11l11l11ll_opy_(bstack1l111l11ll_opy_)
  os.environ[bstack1ll11_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪ༨")] = bstack111lll111_opy_
  bstack11lll1l1ll_opy_ = bstack111lll111_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack11l111111_opy_ = bstack1llll11ll1_opy_[bstack1ll11_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖ࠰ࡆࡉࡊࠧ༩")] if bstack111lll111_opy_ == bstack1ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༪") and bstack11ll11lll1_opy_() else bstack111lll111_opy_
      bstack1ll1ll111_opy_.invoke(Events.bstack111llll11l_opy_, bstack11l1ll1ll1_opy_(
        sdk_version=__version__,
        path_config=bstack1ll111lll1_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack11l111111_opy_,
        frameworks=[bstack11l111111_opy_],
        framework_versions={
          bstack11l111111_opy_: bstack1l11lllll_opy_(bstack1ll11_opy_ (u"ࠬࡘ࡯ࡣࡱࡷࠫ༫") if bstack111lll111_opy_ in [bstack1ll11_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ༬"), bstack1ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭༭"), bstack1ll11_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ༮")] else bstack111lll111_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack1ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦ༯"), None):
        CONFIG[bstack1ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧ༰")] = cli.config.get(bstack1ll11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨ༱"), None)
    except Exception as e:
      bstack1ll1ll111_opy_.invoke(Events.bstack1lll11llll_opy_, e.__traceback__, 1)
    if bstack111l1l111_opy_:
      CONFIG[bstack1ll11_opy_ (u"ࠧࡧࡰࡱࠤ༲")] = cli.config[bstack1ll11_opy_ (u"ࠨࡡࡱࡲࠥ༳")]
      logger.info(bstack11l11l1l1l_opy_.format(CONFIG[bstack1ll11_opy_ (u"ࠧࡢࡲࡳࠫ༴")]))
  else:
    bstack1ll1ll111_opy_.clear()
  global bstack1lllllllll_opy_
  global bstack1ll1lll1l1_opy_
  if bstack11l1l1llll_opy_:
    try:
      bstack11l1lll1l_opy_ = datetime.datetime.now()
      os.environ[bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍ༵ࠪ")] = bstack111lll111_opy_
      bstack1lll11ll1l_opy_(bstack111l1ll1l_opy_, CONFIG)
      cli.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡴࡦ࡮ࡣࡹ࡫ࡳࡵࡡࡤࡸࡹ࡫࡭ࡱࡶࡨࡨࠧ༶"), datetime.datetime.now() - bstack11l1lll1l_opy_)
    except Exception as e:
      logger.debug(bstack1llllllll1_opy_.format(str(e)))
  global bstack11l1ll1lll_opy_
  global bstack1111l1l11_opy_
  global bstack11ll11lll_opy_
  global bstack1111l1l11l_opy_
  global bstack11111llll_opy_
  global bstack11llll1ll_opy_
  global bstack1ll111ll11_opy_
  global bstack1111lll111_opy_
  global bstack1ll11l11l1_opy_
  global bstack1l11ll11l_opy_
  global bstack1ll1l1ll1l_opy_
  global bstack1111ll11l1_opy_
  global bstack1ll11l111l_opy_
  global bstack1111l1llll_opy_
  global bstack11ll1llll1_opy_
  global bstack1l11llll1_opy_
  global bstack1l11l1ll1l_opy_
  global bstack11l1ll111l_opy_
  global bstack1ll1l1ll11_opy_
  global bstack11l1lllll1_opy_
  global bstack11111ll11_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11l1ll1lll_opy_ = webdriver.Remote.__init__
    bstack1111l1l11_opy_ = WebDriver.quit
    bstack1111ll11l1_opy_ = WebDriver.close
    bstack11ll1llll1_opy_ = WebDriver.get
    bstack11111ll11_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1lllllllll_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack11l11l1ll_opy_
    bstack1ll1lll1l1_opy_ = bstack11l11l1ll_opy_()
  except Exception as e:
    pass
  try:
    global bstack1ll1l1111_opy_
    from QWeb.keywords import browser
    bstack1ll1l1111_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack111l111l1_opy_(CONFIG) and bstack11l111ll1l_opy_():
    if bstack1llll1l1l1_opy_() < version.parse(bstack111llll1l_opy_):
      logger.error(bstack111111ll1_opy_.format(bstack1llll1l1l1_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1ll11_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯༷ࠫ")) and callable(getattr(RemoteConnection, bstack1ll11_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ༸"))):
          RemoteConnection._get_proxy_url = bstack1l11111ll1_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack1l11111ll1_opy_
      except Exception as e:
        logger.error(bstack111llllll_opy_.format(str(e)))
  if not CONFIG.get(bstack1ll11_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹ༹ࠧ"), False) and not bstack11l1l1llll_opy_:
    logger.info(bstack1l1ll1ll1_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack1ll11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ༺") in CONFIG and str(CONFIG[bstack1ll11_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ༻")]).lower() != bstack1ll11_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ༼"):
      bstack11ll1l111_opy_()
    elif bstack111lll111_opy_ != bstack1ll11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༽") or (bstack111lll111_opy_ == bstack1ll11_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༾") and not bstack11l1l1llll_opy_):
      bstack111ll111ll_opy_()
  if (bstack111lll111_opy_ in [bstack1ll11_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ༿"), bstack1ll11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫཀ"), bstack1ll11_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧཁ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1l11l11l11_opy_
        bstack11llll1ll_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1ll1l1lll1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack11111llll_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack11l1llll11_opy_ + str(e))
    except Exception as e:
      bstack1ll1lllll1_opy_(e, bstack1ll1l1lll1_opy_)
    if bstack111lll111_opy_ != bstack1ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨག"):
      bstack1ll11ll11l_opy_()
    bstack11ll11lll_opy_ = Output.start_test
    bstack1111l1l11l_opy_ = Output.end_test
    bstack1ll111ll11_opy_ = TestStatus.__init__
    bstack1ll11l11l1_opy_ = pabot._run
    bstack1l11ll11l_opy_ = QueueItem.__init__
    bstack1ll1l1ll1l_opy_ = pabot._create_command_for_execution
    bstack1ll1l1ll11_opy_ = pabot._report_results
  if bstack111lll111_opy_ == bstack1ll11_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨགྷ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll1lllll1_opy_(e, bstack11l1l11l1l_opy_)
    bstack1ll11l111l_opy_ = Runner.run_hook
    bstack1111l1llll_opy_ = Step.run
  if bstack111lll111_opy_ == bstack1ll11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩང"):
    try:
      from _pytest.config import Config
      bstack1l11l1ll1l_opy_ = Config.getoption
      from _pytest import runner
      bstack11l1ll111l_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack11l11l11_opy_)
    try:
      from pytest_bdd import reporting
      bstack11l1lllll1_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1ll11_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫཅ"))
  try:
    framework_name = bstack1ll11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪཆ") if bstack111lll111_opy_ in [bstack1ll11_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫཇ"), bstack1ll11_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ཈"), bstack1ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨཉ")] else bstack1111lll1ll_opy_(bstack111lll111_opy_)
    bstack111l1l1l1l_opy_ = {
      bstack1ll11_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠩཊ"): bstack1ll11_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫཋ") if bstack111lll111_opy_ == bstack1ll11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪཌ") and bstack11ll11lll1_opy_() else framework_name,
      bstack1ll11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨཌྷ"): bstack1l11lllll_opy_(framework_name),
      bstack1ll11_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪཎ"): __version__,
      bstack1ll11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡸࡷࡪࡪࠧཏ"): bstack111lll111_opy_
    }
    if bstack111lll111_opy_ in bstack1l1ll1ll11_opy_ + bstack1l11ll111l_opy_:
      if bstack11l11lll_opy_.bstack1ll1llll11_opy_(CONFIG):
        if bstack1ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧཐ") in CONFIG:
          os.environ[bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩད")] = os.getenv(bstack1ll11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪདྷ"), json.dumps(CONFIG[bstack1ll11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪན")]))
          CONFIG[bstack1ll11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫཔ")].pop(bstack1ll11_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪཕ"), None)
          CONFIG[bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭བ")].pop(bstack1ll11_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬབྷ"), None)
        bstack111l1l1l1l_opy_[bstack1ll11_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨམ")] = {
          bstack1ll11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧཙ"): bstack1ll11_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬཚ"),
          bstack1ll11_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬཛ"): str(bstack1llll1l1l1_opy_())
        }
    if bstack111lll111_opy_ not in [bstack1ll11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ཛྷ")] and not cli.is_running():
      bstack1l1111l11l_opy_, bstack111l1ll1l1_opy_ = bstack1ll111l1_opy_.launch(CONFIG, bstack111l1l1l1l_opy_)
      if bstack111l1ll1l1_opy_.get(bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ཝ")) is not None and bstack11l11lll_opy_.bstack11l11ll11_opy_(CONFIG) is None:
        value = bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧཞ")].get(bstack1ll11_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩཟ"))
        if value is not None:
            CONFIG[bstack1ll11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩའ")] = value
        else:
          logger.debug(bstack1ll11_opy_ (u"ࠥࡒࡴࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡤࡢࡶࡤࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡲࡦࡵࡳࡳࡳࡹࡥࠣཡ"))
  except Exception as e:
    logger.debug(bstack1l1111ll1_opy_.format(bstack1ll11_opy_ (u"࡙ࠫ࡫ࡳࡵࡊࡸࡦࠬར"), str(e)))
  if bstack111lll111_opy_ == bstack1ll11_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬལ"):
    bstack1l11lll11_opy_ = True
    if bstack11l1l1llll_opy_ and bstack1l1l11l11l_opy_:
      bstack1l1l1111l_opy_ = CONFIG.get(bstack1ll11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪཤ"), {}).get(bstack1ll11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩཥ"))
      bstack11ll1l1l11_opy_(bstack1l1111l1l_opy_)
    elif bstack11l1l1llll_opy_:
      bstack1l1l1111l_opy_ = CONFIG.get(bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬས"), {}).get(bstack1ll11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫཧ"))
      global bstack1111l1l1l1_opy_
      try:
        if bstack111l1l1l1_opy_(bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ཨ")]) and multiprocessing.current_process().name == bstack1ll11_opy_ (u"ࠫ࠵࠭ཀྵ"):
          bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཪ")].remove(bstack1ll11_opy_ (u"࠭࠭࡮ࠩཫ"))
          bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪཬ")].remove(bstack1ll11_opy_ (u"ࠨࡲࡧࡦࠬ཭"))
          bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ཮")] = bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭཯")][0]
          with open(bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ཰")], bstack1ll11_opy_ (u"ࠬࡸཱࠧ")) as f:
            file_content = f.read()
          bstack11l1l11111_opy_ = bstack1ll11_opy_ (u"ࠨࠢࠣࡨࡵࡳࡲࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡤ࡬ࠢ࡬ࡱࡵࡵࡲࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡀࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡦࠪࡾࢁ࠮ࡁࠠࡧࡴࡲࡱࠥࡶࡤࡣࠢ࡬ࡱࡵࡵࡲࡵࠢࡓࡨࡧࡁࠠࡰࡩࡢࡨࡧࠦ࠽ࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱ࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡫ࡦࠡ࡯ࡲࡨࡤࡨࡲࡦࡣ࡮ࠬࡸ࡫࡬ࡧ࠮ࠣࡥࡷ࡭ࠬࠡࡶࡨࡱࡵࡵࡲࡢࡴࡼࠤࡂࠦ࠰ࠪ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡵࡽ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡡࡳࡩࠣࡁࠥࡹࡴࡳࠪ࡬ࡲࡹ࠮ࡡࡳࡩࠬ࠯࠶࠶ࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡥࡹࡥࡨࡴࡹࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡤࡷࠥ࡫࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡤࡷࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡴ࡭࡟ࡥࡤࠫࡷࡪࡲࡦ࠭ࡣࡵ࡫࠱ࡺࡥ࡮ࡲࡲࡶࡦࡸࡹࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡖࡤࡣ࠰ࡧࡳࡤࡨࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡒࡧࡦ࠭࠯࠮ࡴࡧࡷࡣࡹࡸࡡࡤࡧࠫ࠭ࡡࡴࠢࠣࠤི").format(str(bstack11l1l1llll_opy_))
          bstack1l1ll11l11_opy_ = bstack11l1l11111_opy_ + file_content
          bstack1l1l11lll1_opy_ = bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧཱིࠪ")] + bstack1ll11_opy_ (u"ࠨࡡࡥࡷࡹࡧࡣ࡬ࡡࡷࡩࡲࡶ࠮ࡱࡻུࠪ")
          with open(bstack1l1l11lll1_opy_, bstack1ll11_opy_ (u"ࠩࡺཱུࠫ")):
            pass
          with open(bstack1l1l11lll1_opy_, bstack1ll11_opy_ (u"ࠥࡻ࠰ࠨྲྀ")) as f:
            f.write(bstack1l1ll11l11_opy_)
          import subprocess
          process_data = subprocess.run([bstack1ll11_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࠦཷ"), bstack1l1l11lll1_opy_])
          if os.path.exists(bstack1l1l11lll1_opy_):
            os.unlink(bstack1l1l11lll1_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack111l1l1l1_opy_(bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨླྀ")]):
            bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩཹ")].remove(bstack1ll11_opy_ (u"ࠧ࠮࡯ེࠪ"))
            bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨཻࠫ")].remove(bstack1ll11_opy_ (u"ࠩࡳࡨࡧོ࠭"))
            bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪཽ࠭")] = bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཾ")][0]
          bstack11ll1l1l11_opy_(bstack1l1111l1l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཿ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1ll11_opy_ (u"࠭࡟ࡠࡰࡤࡱࡪࡥ࡟ࠨྀ")] = bstack1ll11_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠཱྀࠩ")
          mod_globals[bstack1ll11_opy_ (u"ࠨࡡࡢࡪ࡮ࡲࡥࡠࡡࠪྂ")] = os.path.abspath(bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྃ")])
          exec(open(bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ྄࠭")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1ll11_opy_ (u"ࠫࡈࡧࡵࡨࡪࡷࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠫ྅").format(str(e)))
          for driver in bstack1111l1l1l1_opy_:
            bstack11ll1ll11l_opy_.append({
              bstack1ll11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ྆"): bstack11l1l1llll_opy_[bstack1ll11_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ྇")],
              bstack1ll11_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ྈ"): str(e),
              bstack1ll11_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧྉ"): multiprocessing.current_process().name
            })
            bstack11l11lll1l_opy_(driver, bstack1ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩྊ"), bstack1ll11_opy_ (u"ࠥࡗࡪࡹࡳࡪࡱࡱࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨྋ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1111l1l1l1_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack111l1l111_opy_, CONFIG, logger)
      bstack1111lllll_opy_()
      bstack111ll1ll11_opy_()
      percy.bstack1ll1l1l1ll_opy_()
      bstack11111ll1_opy_ = {
        bstack1ll11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྌ"): args[0],
        bstack1ll11_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬྍ"): CONFIG,
        bstack1ll11_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧྎ"): bstack11l111111l_opy_,
        bstack1ll11_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩྏ"): bstack111l1l111_opy_
      }
      if bstack1ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫྐ") in CONFIG:
        bstack111l11111l_opy_ = bstack111lllll11_opy_(args, logger, CONFIG, bstack1lllll1l1l_opy_, bstack1111llll1_opy_)
        bstack11llll11l_opy_ = bstack111l11111l_opy_.bstack1llll1lll_opy_(run_on_browserstack, bstack11111ll1_opy_, bstack111l1l1l1_opy_(args))
      else:
        if bstack111l1l1l1_opy_(args):
          bstack11111ll1_opy_[bstack1ll11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྑ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack11111ll1_opy_,))
          test.start()
          test.join()
        else:
          bstack11ll1l1l11_opy_(bstack1l1111l1l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1ll11_opy_ (u"ࠪࡣࡤࡴࡡ࡮ࡧࡢࡣࠬྒ")] = bstack1ll11_opy_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ྒྷ")
          mod_globals[bstack1ll11_opy_ (u"ࠬࡥ࡟ࡧ࡫࡯ࡩࡤࡥࠧྔ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack111lll111_opy_ == bstack1ll11_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬྕ") or bstack111lll111_opy_ == bstack1ll11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ྖ"):
    percy.init(bstack111l1l111_opy_, CONFIG, logger)
    percy.bstack1ll1l1l1ll_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1ll1lllll1_opy_(e, bstack1ll1l1lll1_opy_)
    bstack1111lllll_opy_()
    bstack11ll1l1l11_opy_(bstack11l1l1lll_opy_)
    if bstack1lllll1l1l_opy_:
      bstack1111ll111_opy_(bstack11l1l1lll_opy_, args)
      if bstack1ll11_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ྗ") in args:
        i = args.index(bstack1ll11_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ྘"))
        args.pop(i)
        args.pop(i)
      if bstack1ll11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྙ") not in CONFIG:
        CONFIG[bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྚ")] = [{}]
        bstack1111llll1_opy_ = 1
      if bstack11l1llll1_opy_ == 0:
        bstack11l1llll1_opy_ = 1
      args.insert(0, str(bstack11l1llll1_opy_))
      args.insert(0, str(bstack1ll11_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪྛ")))
    if bstack1ll111l1_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack11lll1ll1l_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1l111111l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1ll11_opy_ (u"ࠨࡒࡐࡄࡒࡘࡤࡕࡐࡕࡋࡒࡒࡘࠨྜ"),
        ).parse_args(bstack11lll1ll1l_opy_)
        bstack11l1l111l1_opy_ = args.index(bstack11lll1ll1l_opy_[0]) if len(bstack11lll1ll1l_opy_) > 0 else len(args)
        args.insert(bstack11l1l111l1_opy_, str(bstack1ll11_opy_ (u"ࠧ࠮࠯࡯࡭ࡸࡺࡥ࡯ࡧࡵࠫྜྷ")))
        args.insert(bstack11l1l111l1_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡴࡲࡦࡴࡺ࡟࡭࡫ࡶࡸࡪࡴࡥࡳ࠰ࡳࡽࠬྞ"))))
        if bstack11l11l1l_opy_.bstack11111111_opy_(CONFIG):
          args.insert(bstack11l1l111l1_opy_, str(bstack1ll11_opy_ (u"ࠩ࠰࠱ࡱ࡯ࡳࡵࡧࡱࡩࡷ࠭ྟ")))
          args.insert(bstack11l1l111l1_opy_ + 1, str(bstack1ll11_opy_ (u"ࠪࡖࡪࡺࡲࡺࡈࡤ࡭ࡱ࡫ࡤ࠻ࡽࢀࠫྠ").format(bstack11l11l1l_opy_.bstack111lllll_opy_(CONFIG))))
        if bstack1llll1lll1_opy_(os.environ.get(bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠩྡ"))) and str(os.environ.get(bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠩྡྷ"), bstack1ll11_opy_ (u"࠭࡮ࡶ࡮࡯ࠫྣ"))) != bstack1ll11_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬྤ"):
          for bstack1ll111l1l1_opy_ in bstack1l111111l_opy_:
            args.remove(bstack1ll111l1l1_opy_)
          test_files = os.environ.get(bstack1ll11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬྥ")).split(bstack1ll11_opy_ (u"ࠩ࠯ࠫྦ"))
          for bstack11111lll_opy_ in test_files:
            args.append(bstack11111lll_opy_)
      except Exception as e:
        logger.error(bstack1ll11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡣࡷࡸࡦࡩࡨࡪࡰࡪࠤࡱ࡯ࡳࡵࡧࡱࡩࡷࠦࡦࡰࡴࠣࡿࢂ࠴ࠠࡆࡴࡵࡳࡷࠦ࠭ࠡࡽࢀࠦྦྷ").format(bstack1ll1111ll_opy_, e))
    pabot.main(args)
  elif bstack111lll111_opy_ == bstack1ll11_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬྨ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1ll1lllll1_opy_(e, bstack1ll1l1lll1_opy_)
    for a in args:
      if bstack1ll11_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫྩ") in a:
        bstack1ll1l1lll_opy_ = int(a.split(bstack1ll11_opy_ (u"࠭࠺ࠨྪ"))[1])
      if bstack1ll11_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫྫ") in a:
        bstack1l1l1111l_opy_ = str(a.split(bstack1ll11_opy_ (u"ࠨ࠼ࠪྫྷ"))[1])
      if bstack1ll11_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡅࡏࡍࡆࡘࡇࡔࠩྭ") in a:
        bstack1ll111l111_opy_ = str(a.split(bstack1ll11_opy_ (u"ࠪ࠾ࠬྮ"))[1])
    bstack1lll11lll_opy_ = None
    if bstack1ll11_opy_ (u"ࠫ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠪྯ") in args:
      i = args.index(bstack1ll11_opy_ (u"ࠬ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠫྰ"))
      args.pop(i)
      bstack1lll11lll_opy_ = args.pop(i)
    if bstack1lll11lll_opy_ is not None:
      global bstack1lllll11l1_opy_
      bstack1lllll11l1_opy_ = bstack1lll11lll_opy_
    bstack11ll1l1l11_opy_(bstack11l1l1lll_opy_)
    run_cli(args)
    if bstack1ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪྱ") in multiprocessing.current_process().__dict__.keys():
      for bstack111l11llll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11ll1ll11l_opy_.append(bstack111l11llll_opy_)
  elif bstack111lll111_opy_ == bstack1ll11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧྲ"):
    bstack11l11111ll_opy_ = bstack111l11l1_opy_(args, logger, CONFIG, bstack1lllll1l1l_opy_)
    bstack11l11111ll_opy_.bstack1llll1l11_opy_()
    bstack1111lllll_opy_()
    bstack111llll1l1_opy_ = True
    bstack1ll111l11_opy_ = bstack11l11111ll_opy_.bstack111l1111_opy_()
    bstack11l11111ll_opy_.bstack11111ll1_opy_(bstack1ll11lll11_opy_)
    bstack11l11111ll_opy_.bstack111ll111_opy_()
    bstack1l11111l11_opy_(bstack111lll111_opy_, CONFIG, bstack11l11111ll_opy_.bstack1111llll_opy_())
    bstack1l111l1ll_opy_ = bstack11l11111ll_opy_.bstack1llll1lll_opy_(bstack1llll1ll11_opy_, {
      bstack1ll11_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩླ"): bstack11l111111l_opy_,
      bstack1ll11_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫྴ"): bstack111l1l111_opy_,
      bstack1ll11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ྵ"): bstack1lllll1l1l_opy_
    })
    try:
      bstack11llllllll_opy_, bstack11l1111ll1_opy_ = map(list, zip(*bstack1l111l1ll_opy_))
      bstack1ll11llll1_opy_ = bstack11llllllll_opy_[0]
      for status_code in bstack11l1111ll1_opy_:
        if status_code != 0:
          bstack1l11lll1ll_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1ll11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡣࡹࡩࠥ࡫ࡲࡳࡱࡵࡷࠥࡧ࡮ࡥࠢࡶࡸࡦࡺࡵࡴࠢࡦࡳࡩ࡫࠮ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࠿ࠦࡻࡾࠤྶ").format(str(e)))
  elif bstack111lll111_opy_ == bstack1ll11_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬྷ"):
    try:
      from behave.__main__ import main as bstack1l1lll1ll_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1ll1lllll1_opy_(e, bstack11l1l11l1l_opy_)
    bstack1111lllll_opy_()
    bstack111llll1l1_opy_ = True
    bstack1lllll11l_opy_ = 1
    if bstack1ll11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ྸ") in CONFIG:
      bstack1lllll11l_opy_ = CONFIG[bstack1ll11_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧྐྵ")]
    if bstack1ll11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫྺ") in CONFIG:
      bstack1l1ll11ll1_opy_ = int(bstack1lllll11l_opy_) * int(len(CONFIG[bstack1ll11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྻ")]))
    else:
      bstack1l1ll11ll1_opy_ = int(bstack1lllll11l_opy_)
    config = Configuration(args)
    bstack11l11llll_opy_ = config.paths
    if len(bstack11l11llll_opy_) == 0:
      import glob
      pattern = bstack1ll11_opy_ (u"ࠪ࠮࠯࠵ࠪ࠯ࡨࡨࡥࡹࡻࡲࡦࠩྼ")
      bstack11llllll1_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11llllll1_opy_)
      config = Configuration(args)
      bstack11l11llll_opy_ = config.paths
    bstack111l111l_opy_ = [os.path.normpath(item) for item in bstack11l11llll_opy_]
    bstack111l1l11l_opy_ = [os.path.normpath(item) for item in args]
    bstack111l1lll11_opy_ = [item for item in bstack111l1l11l_opy_ if item not in bstack111l111l_opy_]
    import platform as pf
    if pf.system().lower() == bstack1ll11_opy_ (u"ࠫࡼ࡯࡮ࡥࡱࡺࡷࠬ྽"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack111l111l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1lll1ll1ll_opy_)))
                    for bstack1lll1ll1ll_opy_ in bstack111l111l_opy_]
    bstack1111l111_opy_ = []
    for spec in bstack111l111l_opy_:
      bstack11l1l11l_opy_ = []
      bstack11l1l11l_opy_ += bstack111l1lll11_opy_
      bstack11l1l11l_opy_.append(spec)
      bstack1111l111_opy_.append(bstack11l1l11l_opy_)
    execution_items = []
    for bstack11l1l11l_opy_ in bstack1111l111_opy_:
      if bstack1ll11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ྾") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack1ll11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ྿")]):
          item = {}
          item[bstack1ll11_opy_ (u"ࠧࡢࡴࡪࠫ࿀")] = bstack1ll11_opy_ (u"ࠨࠢࠪ࿁").join(bstack11l1l11l_opy_)
          item[bstack1ll11_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ࿂")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack1ll11_opy_ (u"ࠪࡥࡷ࡭ࠧ࿃")] = bstack1ll11_opy_ (u"ࠫࠥ࠭࿄").join(bstack11l1l11l_opy_)
        item[bstack1ll11_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ࿅")] = 0
        execution_items.append(item)
    bstack1l1l1l1lll_opy_ = bstack1l1lll1lll_opy_(execution_items, bstack1l1ll11ll1_opy_)
    for execution_item in bstack1l1l1l1lll_opy_:
      bstack11l1111l_opy_ = []
      for item in execution_item:
        bstack11l1111l_opy_.append(bstack1ll1111l11_opy_(name=str(item[bstack1ll11_opy_ (u"࠭ࡩ࡯ࡦࡨࡼ࿆ࠬ")]),
                                             target=bstack1lll1l1ll1_opy_,
                                             args=(item[bstack1ll11_opy_ (u"ࠧࡢࡴࡪࠫ࿇")],)))
      for t in bstack11l1111l_opy_:
        t.start()
      for t in bstack11l1111l_opy_:
        t.join()
  else:
    bstack11l11l11ll_opy_(bstack1l111l11ll_opy_)
  if not bstack11l1l1llll_opy_:
    bstack11ll1l1lll_opy_()
    if(bstack111lll111_opy_ in [bstack1ll11_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ࿈"), bstack1ll11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ࿉")]):
      bstack1ll111111_opy_()
  bstack1l1l1l1111_opy_.bstack111llllll1_opy_()
def browserstack_initialize(bstack1ll111l1ll_opy_=None):
  logger.info(bstack1ll11_opy_ (u"ࠪࡖࡺࡴ࡮ࡪࡰࡪࠤࡘࡊࡋࠡࡹ࡬ࡸ࡭ࠦࡡࡳࡩࡶ࠾ࠥ࠭࿊") + str(bstack1ll111l1ll_opy_))
  run_on_browserstack(bstack1ll111l1ll_opy_, None, True)
@measure(event_name=EVENTS.bstack1llll1l1ll_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack11ll1l1lll_opy_():
  global CONFIG
  global bstack11lll1l1ll_opy_
  global bstack1l11lll1ll_opy_
  global bstack11ll1111l1_opy_
  global bstack1111ll11_opy_
  bstack11ll1l11ll_opy_.bstack111l111ll_opy_()
  if cli.is_running():
    bstack1ll1ll111_opy_.invoke(Events.bstack1l1lll1l1_opy_)
  else:
    bstack1lll1ll1l_opy_ = bstack11l11l1l_opy_.bstack1llll11l1_opy_(config=CONFIG)
    bstack1lll1ll1l_opy_.bstack11ll1ll11_opy_(CONFIG)
  if bstack11lll1l1ll_opy_ == bstack1ll11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ࿋"):
    if not cli.is_enabled(CONFIG):
      bstack1ll111l1_opy_.stop()
  else:
    bstack1ll111l1_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1l11l1ll_opy_.bstack1l1l11ll1_opy_()
  if bstack1ll11_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ࿌") in CONFIG and str(CONFIG[bstack1ll11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ࿍")]).lower() != bstack1ll11_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭࿎"):
    hashed_id, bstack11l11lllll_opy_ = bstack1l1ll1111_opy_()
  else:
    hashed_id, bstack11l11lllll_opy_ = get_build_link()
  bstack1l1l111111_opy_(hashed_id)
  logger.info(bstack1ll11_opy_ (u"ࠨࡕࡇࡏࠥࡸࡵ࡯ࠢࡨࡲࡩ࡫ࡤࠡࡨࡲࡶࠥ࡯ࡤ࠻ࠩ࿏") + bstack1111ll11_opy_.get_property(bstack1ll11_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ࿐"), bstack1ll11_opy_ (u"ࠪࠫ࿑")) + bstack1ll11_opy_ (u"ࠫ࠱ࠦࡴࡦࡵࡷ࡬ࡺࡨࠠࡪࡦ࠽ࠤࠬ࿒") + os.getenv(bstack1ll11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ࿓"), bstack1ll11_opy_ (u"࠭ࠧ࿔")))
  if hashed_id is not None and bstack11111l1l1l_opy_() != -1:
    sessions = bstack11llll1l11_opy_(hashed_id)
    bstack1111l1ll1l_opy_(sessions, bstack11l11lllll_opy_)
  if bstack11lll1l1ll_opy_ == bstack1ll11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ࿕") and bstack1l11lll1ll_opy_ != 0:
    sys.exit(bstack1l11lll1ll_opy_)
  if bstack11lll1l1ll_opy_ == bstack1ll11_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ࿖") and bstack11ll1111l1_opy_ != 0:
    sys.exit(bstack11ll1111l1_opy_)
def bstack1l1l111111_opy_(new_id):
    global bstack111l111ll1_opy_
    bstack111l111ll1_opy_ = new_id
def bstack1111lll1ll_opy_(bstack11l11l1lll_opy_):
  if bstack11l11l1lll_opy_:
    return bstack11l11l1lll_opy_.capitalize()
  else:
    return bstack1ll11_opy_ (u"ࠩࠪ࿗")
@measure(event_name=EVENTS.bstack111ll1lll_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1l1l1l1l1l_opy_(bstack1llll1111l_opy_):
  if bstack1ll11_opy_ (u"ࠪࡲࡦࡳࡥࠨ࿘") in bstack1llll1111l_opy_ and bstack1llll1111l_opy_[bstack1ll11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ࿙")] != bstack1ll11_opy_ (u"ࠬ࠭࿚"):
    return bstack1llll1111l_opy_[bstack1ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ࿛")]
  else:
    bstack111ll11l1l_opy_ = bstack1ll11_opy_ (u"ࠢࠣ࿜")
    if bstack1ll11_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ࿝") in bstack1llll1111l_opy_ and bstack1llll1111l_opy_[bstack1ll11_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ࿞")] != None:
      bstack111ll11l1l_opy_ += bstack1llll1111l_opy_[bstack1ll11_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ࿟")] + bstack1ll11_opy_ (u"ࠦ࠱ࠦࠢ࿠")
      if bstack1llll1111l_opy_[bstack1ll11_opy_ (u"ࠬࡵࡳࠨ࿡")] == bstack1ll11_opy_ (u"ࠨࡩࡰࡵࠥ࿢"):
        bstack111ll11l1l_opy_ += bstack1ll11_opy_ (u"ࠢࡪࡑࡖࠤࠧ࿣")
      bstack111ll11l1l_opy_ += (bstack1llll1111l_opy_[bstack1ll11_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ࿤")] or bstack1ll11_opy_ (u"ࠩࠪ࿥"))
      return bstack111ll11l1l_opy_
    else:
      bstack111ll11l1l_opy_ += bstack1111lll1ll_opy_(bstack1llll1111l_opy_[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫ࿦")]) + bstack1ll11_opy_ (u"ࠦࠥࠨ࿧") + (
              bstack1llll1111l_opy_[bstack1ll11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ࿨")] or bstack1ll11_opy_ (u"࠭ࠧ࿩")) + bstack1ll11_opy_ (u"ࠢ࠭ࠢࠥ࿪")
      if bstack1llll1111l_opy_[bstack1ll11_opy_ (u"ࠨࡱࡶࠫ࿫")] == bstack1ll11_opy_ (u"ࠤ࡚࡭ࡳࡪ࡯ࡸࡵࠥ࿬"):
        bstack111ll11l1l_opy_ += bstack1ll11_opy_ (u"࡛ࠥ࡮ࡴࠠࠣ࿭")
      bstack111ll11l1l_opy_ += bstack1llll1111l_opy_[bstack1ll11_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ࿮")] or bstack1ll11_opy_ (u"ࠬ࠭࿯")
      return bstack111ll11l1l_opy_
@measure(event_name=EVENTS.bstack1llll111l1_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack111ll1111l_opy_(bstack1l11l111ll_opy_):
  if bstack1l11l111ll_opy_ == bstack1ll11_opy_ (u"ࠨࡤࡰࡰࡨࠦ࿰"):
    return bstack1ll11_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡪࡶࡪ࡫࡮࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡪࡶࡪ࡫࡮ࠣࡀࡆࡳࡲࡶ࡬ࡦࡶࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ࿱")
  elif bstack1l11l111ll_opy_ == bstack1ll11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ࿲"):
    return bstack1ll11_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡷ࡫ࡤ࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡵࡩࡩࠨ࠾ࡇࡣ࡬ࡰࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ࿳")
  elif bstack1l11l111ll_opy_ == bstack1ll11_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ࿴"):
    return bstack1ll11_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡧࡳࡧࡨࡲࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡧࡳࡧࡨࡲࠧࡄࡐࡢࡵࡶࡩࡩࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ࿵")
  elif bstack1l11l111ll_opy_ == bstack1ll11_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦ࿶"):
    return bstack1ll11_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡴࡨࡨࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡲࡦࡦࠥࡂࡊࡸࡲࡰࡴ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ࿷")
  elif bstack1l11l111ll_opy_ == bstack1ll11_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣ࿸"):
    return bstack1ll11_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࠧࡪ࡫ࡡ࠴࠴࠹࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࠩࡥࡦࡣ࠶࠶࠻ࠨ࠾ࡕ࡫ࡰࡩࡴࡻࡴ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭࿹")
  elif bstack1l11l111ll_opy_ == bstack1ll11_opy_ (u"ࠤࡵࡹࡳࡴࡩ࡯ࡩࠥ࿺"):
    return bstack1ll11_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡨ࡬ࡢࡥ࡮࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡨ࡬ࡢࡥ࡮ࠦࡃࡘࡵ࡯ࡰ࡬ࡲ࡬ࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ࿻")
  else:
    return bstack1ll11_opy_ (u"ࠫࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࠨ࿼") + bstack1111lll1ll_opy_(
      bstack1l11l111ll_opy_) + bstack1ll11_opy_ (u"ࠬࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ࿽")
def bstack111111111_opy_(session):
  return bstack1ll11_opy_ (u"࠭࠼ࡵࡴࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡶࡴࡽࠢ࠿࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠣࡷࡪࡹࡳࡪࡱࡱ࠱ࡳࡧ࡭ࡦࠤࡁࡀࡦࠦࡨࡳࡧࡩࡁࠧࢁࡽࠣࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥࡣࡧࡲࡡ࡯࡭ࠥࡂࢀࢃ࠼࠰ࡣࡁࡀ࠴ࡺࡤ࠿ࡽࢀࡿࢂࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽࠱ࡷࡶࡃ࠭࿾").format(
    session[bstack1ll11_opy_ (u"ࠧࡱࡷࡥࡰ࡮ࡩ࡟ࡶࡴ࡯ࠫ࿿")], bstack1l1l1l1l1l_opy_(session), bstack111ll1111l_opy_(session[bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡶࡤࡸࡺࡹࠧက")]),
    bstack111ll1111l_opy_(session[bstack1ll11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩခ")]),
    bstack1111lll1ll_opy_(session[bstack1ll11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫဂ")] or session[bstack1ll11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫဃ")] or bstack1ll11_opy_ (u"ࠬ࠭င")) + bstack1ll11_opy_ (u"ࠨࠠࠣစ") + (session[bstack1ll11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩဆ")] or bstack1ll11_opy_ (u"ࠨࠩဇ")),
    session[bstack1ll11_opy_ (u"ࠩࡲࡷࠬဈ")] + bstack1ll11_opy_ (u"ࠥࠤࠧဉ") + session[bstack1ll11_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨည")], session[bstack1ll11_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧဋ")] or bstack1ll11_opy_ (u"࠭ࠧဌ"),
    session[bstack1ll11_opy_ (u"ࠧࡤࡴࡨࡥࡹ࡫ࡤࡠࡣࡷࠫဍ")] if session[bstack1ll11_opy_ (u"ࠨࡥࡵࡩࡦࡺࡥࡥࡡࡤࡸࠬဎ")] else bstack1ll11_opy_ (u"ࠩࠪဏ"))
@measure(event_name=EVENTS.bstack11llll11l1_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def bstack1111l1ll1l_opy_(sessions, bstack11l11lllll_opy_):
  try:
    bstack1111l111l1_opy_ = bstack1ll11_opy_ (u"ࠥࠦတ")
    if not os.path.exists(bstack1ll11l11ll_opy_):
      os.mkdir(bstack1ll11l11ll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll11_opy_ (u"ࠫࡦࡹࡳࡦࡶࡶ࠳ࡷ࡫ࡰࡰࡴࡷ࠲࡭ࡺ࡭࡭ࠩထ")), bstack1ll11_opy_ (u"ࠬࡸࠧဒ")) as f:
      bstack1111l111l1_opy_ = f.read()
    bstack1111l111l1_opy_ = bstack1111l111l1_opy_.replace(bstack1ll11_opy_ (u"࠭ࡻࠦࡔࡈࡗ࡚ࡒࡔࡔࡡࡆࡓ࡚ࡔࡔࠦࡿࠪဓ"), str(len(sessions)))
    bstack1111l111l1_opy_ = bstack1111l111l1_opy_.replace(bstack1ll11_opy_ (u"ࠧࡼࠧࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠪࢃࠧန"), bstack11l11lllll_opy_)
    bstack1111l111l1_opy_ = bstack1111l111l1_opy_.replace(bstack1ll11_opy_ (u"ࠨࡽࠨࡆ࡚ࡏࡌࡅࡡࡑࡅࡒࡋࠥࡾࠩပ"),
                                              sessions[0].get(bstack1ll11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡰࡤࡱࡪ࠭ဖ")) if sessions[0] else bstack1ll11_opy_ (u"ࠪࠫဗ"))
    with open(os.path.join(bstack1ll11l11ll_opy_, bstack1ll11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡶࡪࡶ࡯ࡳࡶ࠱࡬ࡹࡳ࡬ࠨဘ")), bstack1ll11_opy_ (u"ࠬࡽࠧမ")) as stream:
      stream.write(bstack1111l111l1_opy_.split(bstack1ll11_opy_ (u"࠭ࡻࠦࡕࡈࡗࡘࡏࡏࡏࡕࡢࡈࡆ࡚ࡁࠦࡿࠪယ"))[0])
      for session in sessions:
        stream.write(bstack111111111_opy_(session))
      stream.write(bstack1111l111l1_opy_.split(bstack1ll11_opy_ (u"ࠧࡼࠧࡖࡉࡘ࡙ࡉࡐࡐࡖࡣࡉࡇࡔࡂࠧࢀࠫရ"))[1])
    logger.info(bstack1ll11_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵࡧࡧࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡦࡺ࡯࡬ࡥࠢࡤࡶࡹ࡯ࡦࡢࡥࡷࡷࠥࡧࡴࠡࡽࢀࠫလ").format(bstack1ll11l11ll_opy_));
  except Exception as e:
    logger.debug(bstack1l1lll1l11_opy_.format(str(e)))
def bstack11llll1l11_opy_(hashed_id):
  global CONFIG
  try:
    bstack11l1lll1l_opy_ = datetime.datetime.now()
    host = bstack1ll11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠭ࡤ࡮ࡲࡹࡩ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩဝ") if bstack1ll11_opy_ (u"ࠪࡥࡵࡶࠧသ") in CONFIG else bstack1ll11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬဟ")
    user = CONFIG[bstack1ll11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧဠ")]
    key = CONFIG[bstack1ll11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩအ")]
    bstack1llllll111_opy_ = bstack1ll11_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ဢ") if bstack1ll11_opy_ (u"ࠨࡣࡳࡴࠬဣ") in CONFIG else (bstack1ll11_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ဤ") if CONFIG.get(bstack1ll11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧဥ")) else bstack1ll11_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ဦ"))
    host = bstack11l11111l_opy_(cli.config, [bstack1ll11_opy_ (u"ࠧࡧࡰࡪࡵࠥဧ"), bstack1ll11_opy_ (u"ࠨࡡࡱࡲࡄࡹࡹࡵ࡭ࡢࡶࡨࠦဨ"), bstack1ll11_opy_ (u"ࠢࡢࡲ࡬ࠦဩ")], host) if bstack1ll11_opy_ (u"ࠨࡣࡳࡴࠬဪ") in CONFIG else bstack11l11111l_opy_(cli.config, [bstack1ll11_opy_ (u"ࠤࡤࡴ࡮ࡹࠢါ"), bstack1ll11_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࠧာ"), bstack1ll11_opy_ (u"ࠦࡦࡶࡩࠣိ")], host)
    url = bstack1ll11_opy_ (u"ࠬࢁࡽ࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃ࠯ࡴࡧࡶࡷ࡮ࡵ࡮ࡴ࠰࡭ࡷࡴࡴࠧီ").format(host, bstack1llllll111_opy_, hashed_id)
    headers = {
      bstack1ll11_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬု"): bstack1ll11_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪူ"),
    }
    proxies = bstack1111l1ll1_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠣࡪࡷࡸࡵࡀࡧࡦࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࡤࡲࡩࡴࡶࠥေ"), datetime.datetime.now() - bstack11l1lll1l_opy_)
      return list(map(lambda session: session[bstack1ll11_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠧဲ")], response.json()))
  except Exception as e:
    logger.debug(bstack111ll11ll1_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack1l11l1l1ll_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def get_build_link():
  global CONFIG
  global bstack111l111ll1_opy_
  try:
    if bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ဳ") in CONFIG:
      bstack11l1lll1l_opy_ = datetime.datetime.now()
      host = bstack1ll11_opy_ (u"ࠫࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪࠧဴ") if bstack1ll11_opy_ (u"ࠬࡧࡰࡱࠩဵ") in CONFIG else bstack1ll11_opy_ (u"࠭ࡡࡱ࡫ࠪံ")
      user = CONFIG[bstack1ll11_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦ့ࠩ")]
      key = CONFIG[bstack1ll11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫး")]
      bstack1llllll111_opy_ = bstack1ll11_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨ္") if bstack1ll11_opy_ (u"ࠪࡥࡵࡶ်ࠧ") in CONFIG else bstack1ll11_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ျ")
      url = bstack1ll11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡻࡾ࠼ࡾࢁࡅࢁࡽ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠮࡫ࡵࡲࡲࠬြ").format(user, key, host, bstack1llllll111_opy_)
      if cli.is_enabled(CONFIG):
        bstack11l11lllll_opy_, hashed_id = cli.bstack111lll1l11_opy_()
        logger.info(bstack111l11ll11_opy_.format(bstack11l11lllll_opy_))
        return [hashed_id, bstack11l11lllll_opy_]
      else:
        headers = {
          bstack1ll11_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬွ"): bstack1ll11_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪှ"),
        }
        if bstack1ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪဿ") in CONFIG:
          params = {bstack1ll11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ၀"): CONFIG[bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭၁")], bstack1ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ၂"): CONFIG[bstack1ll11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ၃")]}
        else:
          params = {bstack1ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ၄"): CONFIG[bstack1ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ၅")]}
        proxies = bstack1111l1ll1_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack11l11ll1l1_opy_ = response.json()[0][bstack1ll11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡨࡵࡪ࡮ࡧࠫ၆")]
          if bstack11l11ll1l1_opy_:
            bstack11l11lllll_opy_ = bstack11l11ll1l1_opy_[bstack1ll11_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭၇")].split(bstack1ll11_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥ࠰ࡦࡺ࡯࡬ࡥࠩ၈"))[0] + bstack1ll11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡶ࠳ࠬ၉") + bstack11l11ll1l1_opy_[
              bstack1ll11_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ၊")]
            logger.info(bstack111l11ll11_opy_.format(bstack11l11lllll_opy_))
            bstack111l111ll1_opy_ = bstack11l11ll1l1_opy_[bstack1ll11_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ။")]
            bstack1l11ll1l1_opy_ = CONFIG[bstack1ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ၌")]
            if bstack1ll11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ၍") in CONFIG:
              bstack1l11ll1l1_opy_ += bstack1ll11_opy_ (u"ࠩࠣࠫ၎") + CONFIG[bstack1ll11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ၏")]
            if bstack1l11ll1l1_opy_ != bstack11l11ll1l1_opy_[bstack1ll11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩၐ")]:
              logger.debug(bstack1l1l111l1l_opy_.format(bstack11l11ll1l1_opy_[bstack1ll11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪၑ")], bstack1l11ll1l1_opy_))
            cli.bstack1111l11l11_opy_(bstack1ll11_opy_ (u"ࠨࡨࡵࡶࡳ࠾࡬࡫ࡴࡠࡤࡸ࡭ࡱࡪ࡟࡭࡫ࡱ࡯ࠧၒ"), datetime.datetime.now() - bstack11l1lll1l_opy_)
            return [bstack11l11ll1l1_opy_[bstack1ll11_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪၓ")], bstack11l11lllll_opy_]
    else:
      logger.warn(bstack11l1ll1111_opy_)
  except Exception as e:
    logger.debug(bstack1l11l1l11_opy_.format(str(e)))
  return [None, None]
def bstack1ll1ll1lll_opy_(url, bstack111l1l111l_opy_=False):
  global CONFIG
  global bstack1ll11l1ll1_opy_
  if not bstack1ll11l1ll1_opy_:
    hostname = bstack1l11lll11l_opy_(url)
    is_private = bstack1lll111l11_opy_(hostname)
    if (bstack1ll11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬၔ") in CONFIG and not bstack1llll1lll1_opy_(CONFIG[bstack1ll11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ၕ")])) and (is_private or bstack111l1l111l_opy_):
      bstack1ll11l1ll1_opy_ = hostname
def bstack1l11lll11l_opy_(url):
  return urlparse(url).hostname
def bstack1lll111l11_opy_(hostname):
  for bstack11lll111l_opy_ in bstack1l11ll11l1_opy_:
    regex = re.compile(bstack11lll111l_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack11l1l1l11l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack11111ll1l1_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1ll1l1lll_opy_
  bstack1ll1l111l1_opy_ = not (bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၖ"), None) and bstack1ll1ll11_opy_(
          threading.current_thread(), bstack1ll11_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၗ"), None))
  bstack11l1l1lll1_opy_ = getattr(driver, bstack1ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬၘ"), None) != True
  bstack1lll1111l_opy_ = bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ၙ"), None) and bstack1ll1ll11_opy_(
          threading.current_thread(), bstack1ll11_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩၚ"), None)
  if bstack1lll1111l_opy_:
    if not bstack1l1ll1l1ll_opy_():
      logger.warning(bstack1ll11_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶ࠲ࠧၛ"))
      return {}
    logger.debug(bstack1ll11_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ၜ"))
    logger.debug(perform_scan(driver, driver_command=bstack1ll11_opy_ (u"ࠪࡩࡽ࡫ࡣࡶࡶࡨࡗࡨࡸࡩࡱࡶࠪၝ")))
    results = bstack1111111l1_opy_(bstack1ll11_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷࡷࠧၞ"))
    if results is not None and results.get(bstack1ll11_opy_ (u"ࠧ࡯ࡳࡴࡷࡨࡷࠧၟ")) is not None:
        return results[bstack1ll11_opy_ (u"ࠨࡩࡴࡵࡸࡩࡸࠨၠ")]
    logger.error(bstack1ll11_opy_ (u"ࠢࡏࡱࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡖࡪࡹࡵ࡭ࡶࡶࠤࡼ࡫ࡲࡦࠢࡩࡳࡺࡴࡤ࠯ࠤၡ"))
    return []
  if not bstack11l11lll_opy_.bstack1111l1l1ll_opy_(CONFIG, bstack1ll1l1lll_opy_) or (bstack11l1l1lll1_opy_ and bstack1ll1l111l1_opy_):
    logger.warning(bstack1ll11_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵ࠱ࠦၢ"))
    return {}
  try:
    logger.debug(bstack1ll11_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ၣ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack11111lll11_opy_.bstack1l111ll1l1_opy_)
    return results
  except Exception:
    logger.error(bstack1ll11_opy_ (u"ࠥࡒࡴࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡸࡧࡵࡩࠥ࡬࡯ࡶࡰࡧ࠲ࠧၤ"))
    return {}
@measure(event_name=EVENTS.bstack1l111llll1_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1ll1l1lll_opy_
  bstack1ll1l111l1_opy_ = not (bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၥ"), None) and bstack1ll1ll11_opy_(
          threading.current_thread(), bstack1ll11_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၦ"), None))
  bstack11l1l1lll1_opy_ = getattr(driver, bstack1ll11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ၧ"), None) != True
  bstack1lll1111l_opy_ = bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၨ"), None) and bstack1ll1ll11_opy_(
          threading.current_thread(), bstack1ll11_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၩ"), None)
  if bstack1lll1111l_opy_:
    if not bstack1l1ll1l1ll_opy_():
      logger.warning(bstack1ll11_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠴ࠢၪ"))
      return {}
    logger.debug(bstack1ll11_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹࠨၫ"))
    logger.debug(perform_scan(driver, driver_command=bstack1ll11_opy_ (u"ࠫࡪࡾࡥࡤࡷࡷࡩࡘࡩࡲࡪࡲࡷࠫၬ")))
    results = bstack1111111l1_opy_(bstack1ll11_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸࡘࡻ࡭࡮ࡣࡵࡽࠧၭ"))
    if results is not None and results.get(bstack1ll11_opy_ (u"ࠨࡳࡶ࡯ࡰࡥࡷࡿࠢၮ")) is not None:
        return results[bstack1ll11_opy_ (u"ࠢࡴࡷࡰࡱࡦࡸࡹࠣၯ")]
    logger.error(bstack1ll11_opy_ (u"ࠣࡐࡲࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡗ࡫ࡳࡶ࡮ࡷࡷ࡙ࠥࡵ࡮࡯ࡤࡶࡾࠦࡷࡢࡵࠣࡪࡴࡻ࡮ࡥ࠰ࠥၰ"))
    return {}
  if not bstack11l11lll_opy_.bstack1111l1l1ll_opy_(CONFIG, bstack1ll1l1lll_opy_) or (bstack11l1l1lll1_opy_ and bstack1ll1l111l1_opy_):
    logger.warning(bstack1ll11_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡸࡻ࡭࡮ࡣࡵࡽ࠳ࠨၱ"))
    return {}
  try:
    logger.debug(bstack1ll11_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹࠨၲ"))
    logger.debug(perform_scan(driver))
    bstack11ll1111ll_opy_ = driver.execute_async_script(bstack11111lll11_opy_.bstack1l11111l1l_opy_)
    return bstack11ll1111ll_opy_
  except Exception:
    logger.error(bstack1ll11_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡷࡰࡱࡦࡸࡹࠡࡹࡤࡷࠥ࡬࡯ࡶࡰࡧ࠲ࠧၳ"))
    return {}
def bstack1l1ll1l1ll_opy_():
  global CONFIG
  global bstack1ll1l1lll_opy_
  bstack1l11l1lll1_opy_ = bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬၴ"), None) and bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨၵ"), None)
  if not bstack11l11lll_opy_.bstack1111l1l1ll_opy_(CONFIG, bstack1ll1l1lll_opy_) or not bstack1l11l1lll1_opy_:
        logger.warning(bstack1ll11_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡸࡥࡴࡷ࡯ࡸࡸ࠴ࠢၶ"))
        return False
  return True
def bstack1111111l1_opy_(bstack11lllll1ll_opy_):
    bstack11lll1lll1_opy_ = bstack1ll111l1_opy_.current_test_uuid() if bstack1ll111l1_opy_.current_test_uuid() else bstack1l11l1ll_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack11ll11ll1l_opy_(bstack11lll1lll1_opy_, bstack11lllll1ll_opy_))
        try:
            return future.result(timeout=bstack1l1l11ll11_opy_)
        except TimeoutError:
            logger.error(bstack1ll11_opy_ (u"ࠣࡖ࡬ࡱࡪࡵࡵࡵࠢࡤࡪࡹ࡫ࡲࠡࡽࢀࡷࠥࡽࡨࡪ࡮ࡨࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡒࡦࡵࡸࡰࡹࡹࠢၷ").format(bstack1l1l11ll11_opy_))
        except Exception as ex:
            logger.debug(bstack1ll11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡴࡨࡸࡷ࡯ࡥࡷ࡫ࡱ࡫ࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡻࡾ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠰ࠤࢀࢃࠢၸ").format(bstack11lllll1ll_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack1l1l1l11l1_opy_, stage=STAGE.bstack1111l1111_opy_, bstack111ll11l1l_opy_=bstack11l1l111ll_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1ll1l1lll_opy_
  bstack1ll1l111l1_opy_ = not (bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၹ"), None) and bstack1ll1ll11_opy_(
          threading.current_thread(), bstack1ll11_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၺ"), None))
  bstack1ll1lll1ll_opy_ = not (bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬၻ"), None) and bstack1ll1ll11_opy_(
          threading.current_thread(), bstack1ll11_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨၼ"), None))
  bstack11l1l1lll1_opy_ = getattr(driver, bstack1ll11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧၽ"), None) != True
  if not bstack11l11lll_opy_.bstack1111l1l1ll_opy_(CONFIG, bstack1ll1l1lll_opy_) or (bstack11l1l1lll1_opy_ and bstack1ll1l111l1_opy_ and bstack1ll1lll1ll_opy_):
    logger.warning(bstack1ll11_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡷࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡩࡡ࡯࠰ࠥၾ"))
    return {}
  try:
    bstack1ll111ll1l_opy_ = bstack1ll11_opy_ (u"ࠩࡤࡴࡵ࠭ၿ") in CONFIG and CONFIG.get(bstack1ll11_opy_ (u"ࠪࡥࡵࡶࠧႀ"), bstack1ll11_opy_ (u"ࠫࠬႁ"))
    session_id = getattr(driver, bstack1ll11_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩႂ"), None)
    if not session_id:
      logger.warning(bstack1ll11_opy_ (u"ࠨࡎࡰࠢࡶࡩࡸࡹࡩࡰࡰࠣࡍࡉࠦࡦࡰࡷࡱࡨࠥ࡬࡯ࡳࠢࡧࡶ࡮ࡼࡥࡳࠤႃ"))
      return {bstack1ll11_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨႄ"): bstack1ll11_opy_ (u"ࠣࡐࡲࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡏࡄࠡࡨࡲࡹࡳࡪࠢႅ")}
    if bstack1ll111ll1l_opy_:
      try:
        bstack11lll1lll_opy_ = {
              bstack1ll11_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ࠭ႆ"): os.environ.get(bstack1ll11_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨႇ"), os.environ.get(bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨႈ"), bstack1ll11_opy_ (u"ࠬ࠭ႉ"))),
              bstack1ll11_opy_ (u"࠭ࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩ࠭ႊ"): bstack1ll111l1_opy_.current_test_uuid() if bstack1ll111l1_opy_.current_test_uuid() else bstack1l11l1ll_opy_.current_hook_uuid(),
              bstack1ll11_opy_ (u"ࠧࡢࡷࡷ࡬ࡍ࡫ࡡࡥࡧࡵࠫႋ"): os.environ.get(bstack1ll11_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ႌ")),
              bstack1ll11_opy_ (u"ࠩࡶࡧࡦࡴࡔࡪ࡯ࡨࡷࡹࡧ࡭ࡱႍࠩ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack1ll11_opy_ (u"ࠪࡸ࡭ࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨႎ"): os.environ.get(bstack1ll11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩႏ"), bstack1ll11_opy_ (u"ࠬ࠭႐")),
              bstack1ll11_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭႑"): kwargs.get(bstack1ll11_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸ࡟ࡤࡱࡰࡱࡦࡴࡤࠨ႒"), None) or bstack1ll11_opy_ (u"ࠨࠩ႓")
          }
        if not hasattr(thread_local, bstack1ll11_opy_ (u"ࠩࡥࡥࡸ࡫࡟ࡢࡲࡳࡣࡦ࠷࠱ࡺࡡࡶࡧࡷ࡯ࡰࡵࠩ႔")):
            scripts = {bstack1ll11_opy_ (u"ࠪࡷࡨࡧ࡮ࠨ႕"): bstack11111lll11_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack11ll1l1l1l_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack11ll1l1l1l_opy_[bstack1ll11_opy_ (u"ࠫࡸࡩࡡ࡯ࠩ႖")] = bstack11ll1l1l1l_opy_[bstack1ll11_opy_ (u"ࠬࡹࡣࡢࡰࠪ႗")] % json.dumps(bstack11lll1lll_opy_)
        bstack11111lll11_opy_.bstack1l11l1llll_opy_(bstack11ll1l1l1l_opy_)
        bstack11111lll11_opy_.store()
        bstack1l11l1l1l1_opy_ = driver.execute_script(bstack11111lll11_opy_.perform_scan)
      except Exception as bstack11l11l1111_opy_:
        logger.info(bstack1ll11_opy_ (u"ࠨࡁࡱࡲ࡬ࡹࡲࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡤࡣࡱࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࠨ႘") + str(bstack11l11l1111_opy_))
        bstack1l11l1l1l1_opy_ = {bstack1ll11_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨ႙"): str(bstack11l11l1111_opy_)}
    else:
      bstack1l11l1l1l1_opy_ = driver.execute_async_script(bstack11111lll11_opy_.perform_scan, {bstack1ll11_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨႚ"): kwargs.get(bstack1ll11_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࡡࡦࡳࡲࡳࡡ࡯ࡦࠪႛ"), None) or bstack1ll11_opy_ (u"ࠪࠫႜ")})
    return bstack1l11l1l1l1_opy_
  except Exception as err:
    logger.error(bstack1ll11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡳࡷࡱࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡩࡡ࡯࠰ࠣࡿࢂࠨႝ").format(str(err)))
    return {}