# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
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
from browserstack_sdk.bstack111l11l111_opy_ import bstack1l1l11l1l1_opy_
from browserstack_sdk.bstack1lll1l1ll_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack1l1ll1111_opy_():
  global CONFIG
  headers = {
        bstack1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪਆ"): bstack1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨਇ"),
      }
  proxies = bstack1111l1ll1l_opy_(CONFIG, bstack11ll11ll11_opy_)
  try:
    response = requests.get(bstack11ll11ll11_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1ll1111111_opy_ = response.json()[bstack1l_opy_ (u"࠭ࡨࡶࡤࡶࠫਈ")]
      logger.debug(bstack1l1lll1ll_opy_.format(response.json()))
      return bstack1ll1111111_opy_
    else:
      logger.debug(bstack1l1ll1lll1_opy_.format(bstack1l_opy_ (u"ࠢࡓࡧࡶࡴࡴࡴࡳࡦࠢࡍࡗࡔࡔࠠࡱࡣࡵࡷࡪࠦࡥࡳࡴࡲࡶࠥࠨਉ")))
  except Exception as e:
    logger.debug(bstack1l1ll1lll1_opy_.format(e))
def bstack1lll11111l_opy_(hub_url):
  global CONFIG
  url = bstack1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥਊ")+  hub_url + bstack1l_opy_ (u"ࠤ࠲ࡧ࡭࡫ࡣ࡬ࠤ਋")
  headers = {
        bstack1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩ਌"): bstack1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ਍"),
      }
  proxies = bstack1111l1ll1l_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1l1lll1lll_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1l11ll1l11_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack1lll1l1111_opy_, stage=STAGE.bstack11ll111111_opy_)
def bstack11111l1ll1_opy_():
  try:
    global bstack11l1ll1ll1_opy_
    bstack1ll1111111_opy_ = bstack1l1ll1111_opy_()
    bstack11ll1ll11_opy_ = []
    results = []
    for bstack1llll1llll_opy_ in bstack1ll1111111_opy_:
      bstack11ll1ll11_opy_.append(bstack11l11l111_opy_(target=bstack1lll11111l_opy_,args=(bstack1llll1llll_opy_,)))
    for t in bstack11ll1ll11_opy_:
      t.start()
    for t in bstack11ll1ll11_opy_:
      results.append(t.join())
    bstack1111llll1_opy_ = {}
    for item in results:
      hub_url = item[bstack1l_opy_ (u"ࠬ࡮ࡵࡣࡡࡸࡶࡱ࠭਎")]
      latency = item[bstack1l_opy_ (u"࠭࡬ࡢࡶࡨࡲࡨࡿࠧਏ")]
      bstack1111llll1_opy_[hub_url] = latency
    bstack11l1l1ll1_opy_ = min(bstack1111llll1_opy_, key= lambda x: bstack1111llll1_opy_[x])
    bstack11l1ll1ll1_opy_ = bstack11l1l1ll1_opy_
    logger.debug(bstack1lll111l1l_opy_.format(bstack11l1l1ll1_opy_))
  except Exception as e:
    logger.debug(bstack1ll1l1lll_opy_.format(e))
from browserstack_sdk.bstack1111l1l1_opy_ import *
from browserstack_sdk.bstack1llll11l1_opy_ import *
from browserstack_sdk.bstack11ll1ll1_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack111ll1l1l_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack1llll1l111_opy_, stage=STAGE.bstack11ll111111_opy_)
def bstack1ll111ll11_opy_():
    global bstack11l1ll1ll1_opy_
    try:
        bstack111l111l11_opy_ = bstack11l1lll11l_opy_()
        bstack111lll11ll_opy_(bstack111l111l11_opy_)
        hub_url = bstack111l111l11_opy_.get(bstack1l_opy_ (u"ࠢࡶࡴ࡯ࠦਐ"), bstack1l_opy_ (u"ࠣࠤ਑"))
        if hub_url.endswith(bstack1l_opy_ (u"ࠩ࠲ࡻࡩ࠵ࡨࡶࡤࠪ਒")):
            hub_url = hub_url.rsplit(bstack1l_opy_ (u"ࠪ࠳ࡼࡪ࠯ࡩࡷࡥࠫਓ"), 1)[0]
        if hub_url.startswith(bstack1l_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࠬਔ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠧਕ")):
            hub_url = hub_url[8:]
        bstack11l1ll1ll1_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack11l1lll11l_opy_():
    global CONFIG
    bstack1l111111l1_opy_ = CONFIG.get(bstack1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪਖ"), {}).get(bstack1l_opy_ (u"ࠧࡨࡴ࡬ࡨࡓࡧ࡭ࡦࠩਗ"), bstack1l_opy_ (u"ࠨࡐࡒࡣࡌࡘࡉࡅࡡࡑࡅࡒࡋ࡟ࡑࡃࡖࡗࡊࡊࠧਘ"))
    if not isinstance(bstack1l111111l1_opy_, str):
        raise ValueError(bstack1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡉࡵ࡭ࡩࠦ࡮ࡢ࡯ࡨࠤࡲࡻࡳࡵࠢࡥࡩࠥࡧࠠࡷࡣ࡯࡭ࡩࠦࡳࡵࡴ࡬ࡲ࡬ࠨਙ"))
    try:
        bstack111l111l11_opy_ = bstack1l11l1ll11_opy_(bstack1l111111l1_opy_)
        return bstack111l111l11_opy_
    except Exception as e:
        logger.error(bstack1l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࠿ࠦࡻࡾࠤਚ").format(str(e)))
        return {}
def bstack1l11l1ll11_opy_(bstack1l111111l1_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ਛ")] or not CONFIG[bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨਜ")]:
            raise ValueError(bstack1l_opy_ (u"ࠨࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡵࡴࡧࡵࡲࡦࡳࡥࠡࡱࡵࠤࡦࡩࡣࡦࡵࡶࠤࡰ࡫ࡹࠣਝ"))
        url = bstack1lll11ll1l_opy_ + bstack1l111111l1_opy_
        auth = (CONFIG[bstack1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩਞ")], CONFIG[bstack1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫਟ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack11ll111ll1_opy_ = json.loads(response.text)
            return bstack11ll111ll1_opy_
    except ValueError as ve:
        logger.error(bstack1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࠿ࠦࡻࡾࠤਠ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack1l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡧࡳ࡫ࡧࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡀࠠࡼࡿࠥਡ").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack111lll11ll_opy_(bstack111l111ll1_opy_):
    global CONFIG
    if bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨਢ") not in CONFIG or str(CONFIG[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩਣ")]).lower() == bstack1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬਤ"):
        CONFIG[bstack1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭ਥ")] = False
    elif bstack1l_opy_ (u"ࠨ࡫ࡶࡘࡷ࡯ࡡ࡭ࡉࡵ࡭ࡩ࠭ਦ") in bstack111l111ll1_opy_:
        bstack111lllllll_opy_ = CONFIG.get(bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ਧ"), {})
        logger.debug(bstack1l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡼ࡮ࡹࡴࡪࡰࡪࠤࡱࡵࡣࡢ࡮ࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠫࡳࠣਨ"), bstack111lllllll_opy_)
        bstack1llllll11l_opy_ = bstack111l111ll1_opy_.get(bstack1l_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰࡖࡪࡶࡥࡢࡶࡨࡶࡸࠨ਩"), [])
        bstack11lllll11l_opy_ = bstack1l_opy_ (u"ࠧ࠲ࠢਪ").join(bstack1llllll11l_opy_)
        logger.debug(bstack1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡉࡵࡴࡶࡲࡱࠥࡸࡥࡱࡧࡤࡸࡪࡸࠠࡴࡶࡵ࡭ࡳ࡭࠺ࠡࠧࡶࠦਫ"), bstack11lllll11l_opy_)
        bstack11lll1l11_opy_ = {
            bstack1l_opy_ (u"ࠢ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤਬ"): bstack1l_opy_ (u"ࠣࡣࡷࡷ࠲ࡸࡥࡱࡧࡤࡸࡪࡸࠢਭ"),
            bstack1l_opy_ (u"ࠤࡩࡳࡷࡩࡥࡍࡱࡦࡥࡱࠨਮ"): bstack1l_opy_ (u"ࠥࡸࡷࡻࡥࠣਯ"),
            bstack1l_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷࠨਰ"): bstack11lllll11l_opy_
        }
        bstack111lllllll_opy_.update(bstack11lll1l11_opy_)
        logger.debug(bstack1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤ࡚ࡶࡤࡢࡶࡨࡨࠥࡲ࡯ࡤࡣ࡯ࠤࡴࡶࡴࡪࡱࡱࡷ࠿ࠦࠥࡴࠤ਱"), bstack111lllllll_opy_)
        CONFIG[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪਲ")] = bstack111lllllll_opy_
        logger.debug(bstack1l_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡆࡪࡰࡤࡰࠥࡉࡏࡏࡈࡌࡋ࠿ࠦࠥࡴࠤਲ਼"), CONFIG)
def bstack1l1l1ll1l1_opy_():
    bstack111l111l11_opy_ = bstack11l1lll11l_opy_()
    if not bstack111l111l11_opy_[bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠨ਴")]:
      raise ValueError(bstack1l_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠢ࡬ࡷࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡦࡳࡱࡰࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵ࠱ࠦਵ"))
    return bstack111l111l11_opy_[bstack1l_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࡕࡳ࡮ࠪਸ਼")] + bstack1l_opy_ (u"ࠫࡄࡩࡡࡱࡵࡀࠫ਷")
@measure(event_name=EVENTS.bstack1111lll1ll_opy_, stage=STAGE.bstack11ll111111_opy_)
def bstack11111ll1l_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧਸ")], CONFIG[bstack1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩਹ")])
        url = bstack111l1l1lll_opy_
        logger.debug(bstack1l_opy_ (u"ࠢࡂࡶࡷࡩࡲࡶࡴࡪࡰࡪࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦࡢࡶ࡫࡯ࡨࡸࠦࡦࡳࡱࡰࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡘࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠠࡂࡒࡌࠦ਺"))
        try:
            response = requests.get(url, auth=auth, headers={bstack1l_opy_ (u"ࠣࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠢ਻"): bstack1l_opy_ (u"ࠤࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲ਼ࠧ")})
            if response.status_code == 200:
                bstack11llll1l11_opy_ = json.loads(response.text)
                bstack1l1ll1llll_opy_ = bstack11llll1l11_opy_.get(bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡵࠪ਽"), [])
                if bstack1l1ll1llll_opy_:
                    bstack1ll111llll_opy_ = bstack1l1ll1llll_opy_[0]
                    build_hashed_id = bstack1ll111llll_opy_.get(bstack1l_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧਾ"))
                    bstack1l1l11l11_opy_ = bstack1l11lllll_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1l1l11l11_opy_])
                    logger.info(bstack11l1l11l1l_opy_.format(bstack1l1l11l11_opy_))
                    bstack1ll11l1ll1_opy_ = CONFIG[bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨਿ")]
                    if bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨੀ") in CONFIG:
                      bstack1ll11l1ll1_opy_ += bstack1l_opy_ (u"ࠧࠡࠩੁ") + CONFIG[bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪੂ")]
                    if bstack1ll11l1ll1_opy_ != bstack1ll111llll_opy_.get(bstack1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ੃")):
                      logger.debug(bstack1l1l111l1_opy_.format(bstack1ll111llll_opy_.get(bstack1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ੄")), bstack1ll11l1ll1_opy_))
                    return result
                else:
                    logger.debug(bstack1l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡒࡴࠦࡢࡶ࡫࡯ࡨࡸࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡶ࡫ࡩࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠮ࠣ੅"))
            else:
                logger.debug(bstack1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦࡢࡶ࡫࡯ࡨࡸ࠴ࠢ੆"))
        except Exception as e:
            logger.error(bstack1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࡳࠡ࠼ࠣࡿࢂࠨੇ").format(str(e)))
    else:
        logger.debug(bstack1l_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡃࡐࡐࡉࡍࡌࠦࡩࡴࠢࡱࡳࡹࠦࡳࡦࡶ࠱ࠤ࡚ࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦࡢࡶ࡫࡯ࡨࡸ࠴ࠢੈ"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1l111l11l_opy_ import bstack1l111l11l_opy_, Events, bstack11l1ll111l_opy_, bstack1111ll111_opy_
from bstack_utils.measure import bstack1lll11ll11_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1l1l1l1ll_opy_ import bstack11ll1ll1ll_opy_
from bstack_utils.messages import *
from bstack_utils import bstack111ll1l1l_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack111lllll1_opy_, bstack1ll1llll11_opy_, bstack1l111ll1ll_opy_, bstack1llll11l_opy_, \
  bstack1l1l11llll_opy_, \
  Notset, bstack1l1111llll_opy_, \
  bstack1l1llll1ll_opy_, bstack1lll11l11_opy_, bstack111ll1ll1_opy_, bstack11ll1111l_opy_, bstack11ll1l1lll_opy_, bstack11l11l1l11_opy_, \
  bstack111l1ll11_opy_, \
  bstack1lll11ll1_opy_, bstack111l11llll_opy_, bstack1111l11l11_opy_, bstack1ll11l11l1_opy_, \
  bstack1llll1l1l1_opy_, bstack1l1l1l111_opy_, bstack1l11l1ll1l_opy_, bstack1111l1l1ll_opy_
from bstack_utils.bstack11llll111l_opy_ import bstack11lllll11_opy_
from bstack_utils.bstack1llll1lll1_opy_ import bstack1ll1l1l11_opy_, bstack11ll11lll_opy_
from bstack_utils.bstack11l1ll11l1_opy_ import bstack111l11111_opy_
from bstack_utils.bstack11l11ll11_opy_ import bstack11111ll111_opy_, bstack111llll1ll_opy_
from bstack_utils.bstack1ll1l1llll_opy_ import bstack1ll1l1llll_opy_
from bstack_utils.bstack11l1lll111_opy_ import bstack1l1ll1ll1l_opy_
from bstack_utils.proxy import bstack1lll1l1ll1_opy_, bstack1111l1ll1l_opy_, bstack1l1llllll_opy_, bstack111l1l11ll_opy_
from bstack_utils.bstack11llllll1_opy_ import bstack1ll1111lll_opy_
import bstack_utils.bstack1l1l11ll11_opy_ as bstack11l11ll111_opy_
import bstack_utils.bstack11ll11l11l_opy_ as bstack1111l11ll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack1l1ll1l11_opy_ import bstack111llll1l1_opy_
from bstack_utils.bstack1111l11l_opy_ import bstack11111l1l_opy_
from bstack_utils.bstack11lll111ll_opy_ import bstack11111llll1_opy_
if os.getenv(bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡍࡕࡏࡌࡕࠪ੉")):
  cli.bstack111111l11_opy_()
else:
  os.environ[bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡎࡏࡐࡍࡖࠫ੊")] = bstack1l_opy_ (u"ࠪࡸࡷࡻࡥࠨੋ")
bstack1l111l111l_opy_ = bstack1l_opy_ (u"ࠫࠥࠦ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰࡞ࡱࠤࠥ࡯ࡦࠩࡲࡤ࡫ࡪࠦ࠽࠾࠿ࠣࡺࡴ࡯ࡤࠡ࠲ࠬࠤࢀࡢ࡮ࠡࠢࠣࡸࡷࡿࡻ࡝ࡰࠣࡧࡴࡴࡳࡵࠢࡩࡷࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩ࡞ࠪࡪࡸࡢࠧࠪ࠽࡟ࡲࠥࠦࠠࠡࠢࡩࡷ࠳ࡧࡰࡱࡧࡱࡨࡋ࡯࡬ࡦࡕࡼࡲࡨ࠮ࡢࡴࡶࡤࡧࡰࡥࡰࡢࡶ࡫࠰ࠥࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡰࡠ࡫ࡱࡨࡪࡾࠩࠡ࠭ࠣࠦ࠿ࠨࠠࠬࠢࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡎࡘࡕࡎ࠯ࡲࡤࡶࡸ࡫ࠨࠩࡣࡺࡥ࡮ࡺࠠ࡯ࡧࡺࡔࡦ࡭ࡥ࠳࠰ࡨࡺࡦࡲࡵࡢࡶࡨࠬࠧ࠮ࠩࠡ࠿ࡁࠤࢀࢃࠢ࠭ࠢ࡟ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦ࡬࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡧࡷࡥ࡮ࡲࡳࠣࡿ࡟ࠫ࠮࠯ࠩ࡜ࠤ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠧࡣࠩࠡ࠭ࠣࠦ࠱ࡢ࡜࡯ࠤࠬࡠࡳࠦࠠࠡࠢࢀࡧࡦࡺࡣࡩࠪࡨࡼ࠮ࢁ࡜࡯ࠢࠣࠤࠥࢃ࡜࡯ࠢࠣࢁࡡࡴࠠࠡ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࠫੌ")
bstack11111ll11l_opy_ = bstack1l_opy_ (u"ࠬࡢ࡮࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࡨࡵ࡮ࡴࡶࠣࡦࡸࡺࡡࡤ࡭ࡢࡴࡦࡺࡨࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷ࡢࡢ࡮ࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠱࡞࡞ࡱࡧࡴࡴࡳࡵࠢࡳࡣ࡮ࡴࡤࡦࡺࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠸࡝࡝ࡰࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰ࡶࡰ࡮ࡩࡥࠩ࠲࠯ࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹ࠩ࡝ࡰࡦࡳࡳࡹࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢࠪ࠽࡟ࡲ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡱࡧࡵ࡯ࡥ࡫ࠤࡂࠦࡡࡴࡻࡱࡧࠥ࠮࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸ࠯ࠠ࠾ࡀࠣࡿࡡࡴ࡬ࡦࡶࠣࡧࡦࡶࡳ࠼࡞ࡱࡸࡷࡿࠠࡼ࡞ࡱࡧࡦࡶࡳࠡ࠿ࠣࡎࡘࡕࡎ࠯ࡲࡤࡶࡸ࡫ࠨࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷ࠮ࡢ࡮ࠡࠢࢀࠤࡨࡧࡴࡤࡪࠫࡩࡽ࠯ࠠࡼ࡞ࡱࠤࠥࠦࠠࡾ࡞ࡱࠤࠥࡸࡥࡵࡷࡵࡲࠥࡧࡷࡢ࡫ࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡨࡵ࡮࡯ࡧࡦࡸ࠭ࢁ࡜࡯ࠢࠣࠤࠥࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵ࠼ࠣࡤࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂࠪࡻࡦࡰࡦࡳࡩ࡫ࡕࡓࡋࡆࡳࡲࡶ࡯࡯ࡧࡱࡸ࠭ࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡣࡢࡲࡶ࠭࠮ࢃࡠ࠭࡞ࡱࠤࠥࠦࠠ࠯࠰࠱ࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵ࡟ࡲࠥࠦࡽࠪ࡞ࡱࢁࡡࡴ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰࡞ࡱ੍ࠫ")
from ._version import __version__
bstack111lll111l_opy_ = None
CONFIG = {}
bstack111lll11l1_opy_ = {}
bstack11l1ll1lll_opy_ = {}
bstack1lll1l11l1_opy_ = None
bstack1ll11111ll_opy_ = None
bstack11ll1ll11l_opy_ = None
bstack1l11l11l1_opy_ = -1
bstack11lllll1ll_opy_ = 0
bstack11lll1l11l_opy_ = bstack1lll1lll11_opy_
bstack1ll1l1ll11_opy_ = 1
bstack11lll1ll1_opy_ = False
bstack111l1l1l1_opy_ = False
bstack11l1lll1l_opy_ = bstack1l_opy_ (u"࠭ࠧ੎")
bstack1111ll11ll_opy_ = bstack1l_opy_ (u"ࠧࠨ੏")
bstack11l11111ll_opy_ = False
bstack1lll1ll1l1_opy_ = True
bstack1l111lllll_opy_ = bstack1l_opy_ (u"ࠨࠩ੐")
bstack1ll1ll1l11_opy_ = []
bstack11l1l1111l_opy_ = threading.Lock()
bstack1l1l111l11_opy_ = threading.Lock()
bstack11l1ll1ll1_opy_ = bstack1l_opy_ (u"ࠩࠪੑ")
bstack1lll1l111l_opy_ = False
bstack1ll111l1l1_opy_ = None
bstack11l11111l_opy_ = None
bstack1ll1l11ll1_opy_ = None
bstack11ll1lllll_opy_ = -1
bstack1111ll1l11_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠪࢂࠬ੒")), bstack1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ੓"), bstack1l_opy_ (u"ࠬ࠴ࡲࡰࡤࡲࡸ࠲ࡸࡥࡱࡱࡵࡸ࠲࡮ࡥ࡭ࡲࡨࡶ࠳ࡰࡳࡰࡰࠪ੔"))
bstack11l11l1l1l_opy_ = 0
bstack1l1l1111l1_opy_ = 0
bstack11ll1llll1_opy_ = []
bstack1111ll1l1_opy_ = []
bstack111lll1l1_opy_ = []
bstack1111l1lll1_opy_ = []
bstack111l1l1l1l_opy_ = bstack1l_opy_ (u"࠭ࠧ੕")
bstack1ll1ll111_opy_ = bstack1l_opy_ (u"ࠧࠨ੖")
bstack1l1lll1ll1_opy_ = False
bstack1l11l11ll_opy_ = False
bstack111l1lll1_opy_ = {}
bstack1ll1ll1ll1_opy_ = None
bstack111l11ll11_opy_ = None
bstack11l1l11ll_opy_ = None
bstack1l11l1111l_opy_ = None
bstack11llllll1l_opy_ = None
bstack11ll111ll_opy_ = None
bstack11l11ll1l_opy_ = None
bstack1lll111l11_opy_ = None
bstack1l1l11l111_opy_ = None
bstack1111ll1lll_opy_ = None
bstack111lll11l_opy_ = None
bstack1l1ll1l1ll_opy_ = None
bstack11ll1llll_opy_ = None
bstack1ll1l1l1ll_opy_ = None
bstack1ll11111l_opy_ = None
bstack1l1111111l_opy_ = None
bstack11l1l111l_opy_ = None
bstack1l1l1111ll_opy_ = None
bstack1l1111l11_opy_ = None
bstack11ll1l1l11_opy_ = None
bstack11llll11l_opy_ = None
bstack1ll1l111l1_opy_ = None
bstack1lll11lll_opy_ = None
thread_local = threading.local()
bstack1l1lllll11_opy_ = False
bstack1l111lll1_opy_ = bstack1l_opy_ (u"ࠣࠤ੗")
logger = bstack111ll1l1l_opy_.get_logger(__name__, bstack11lll1l11l_opy_)
bstack1lll1ll1l_opy_ = Config.bstack1llll11ll_opy_()
percy = bstack1l1lll11ll_opy_()
bstack1ll1ll1ll_opy_ = bstack11ll1ll1ll_opy_()
bstack11l111111l_opy_ = bstack11ll1ll1_opy_()
def bstack1111lllll1_opy_():
  global CONFIG
  global bstack1l1lll1ll1_opy_
  global bstack1lll1ll1l_opy_
  testContextOptions = bstack11l111l11l_opy_(CONFIG)
  if bstack1l1l11llll_opy_(CONFIG):
    if (bstack1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ੘") in testContextOptions and str(testContextOptions[bstack1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬਖ਼")]).lower() == bstack1l_opy_ (u"ࠫࡹࡸࡵࡦࠩਗ਼")):
      bstack1l1lll1ll1_opy_ = True
    bstack1lll1ll1l_opy_.bstack11ll1l11l1_opy_(testContextOptions.get(bstack1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩਜ਼"), False))
  else:
    bstack1l1lll1ll1_opy_ = True
    bstack1lll1ll1l_opy_.bstack11ll1l11l1_opy_(True)
def bstack1ll111ll1l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1lll1lll1l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1ll1lllll1_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1l_opy_ (u"ࠨ࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡣࡰࡰࡩ࡭࡬࡬ࡩ࡭ࡧࠥੜ") == args[i].lower() or bstack1l_opy_ (u"ࠢ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡲ࡫࡯ࡧࠣ੝") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1l111lllll_opy_
      bstack1l111lllll_opy_ += bstack1l_opy_ (u"ࠨ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡅࡲࡲ࡫࡯ࡧࡇ࡫࡯ࡩࠥ࠭ਫ਼") + shlex.quote(path)
      return path
  return None
bstack111l1l111l_opy_ = re.compile(bstack1l_opy_ (u"ࡴࠥ࠲࠯ࡅ࡜ࠥࡽࠫ࠲࠯ࡅࠩࡾ࠰࠭ࡃࠧ੟"))
def bstack1l111lll1l_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack111l1l111l_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1l_opy_ (u"ࠥࠨࢀࠨ੠") + group + bstack1l_opy_ (u"ࠦࢂࠨ੡"), os.environ.get(group))
  return value
def bstack111ll1l11l_opy_():
  global bstack1lll11lll_opy_
  if bstack1lll11lll_opy_ is None:
        bstack1lll11lll_opy_ = bstack1ll1lllll1_opy_()
  bstack11111l1ll_opy_ = bstack1lll11lll_opy_
  if bstack11111l1ll_opy_ and os.path.exists(os.path.abspath(bstack11111l1ll_opy_)):
    fileName = bstack11111l1ll_opy_
  if bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆࠩ੢") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࡤࡌࡉࡍࡇࠪ੣")])) and not bstack1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡓࡧ࡭ࡦࠩ੤") in locals():
    fileName = os.environ[bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬ੥")]
  if bstack1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡎࡢ࡯ࡨࠫ੦") in locals():
    bstack1ll11l1_opy_ = os.path.abspath(fileName)
  else:
    bstack1ll11l1_opy_ = bstack1l_opy_ (u"ࠪࠫ੧")
  bstack1ll1ll1lll_opy_ = os.getcwd()
  bstack111l1llll_opy_ = bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧ੨")
  bstack1ll11ll1l_opy_ = bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡧ࡭࡭ࠩ੩")
  while (not os.path.exists(bstack1ll11l1_opy_)) and bstack1ll1ll1lll_opy_ != bstack1l_opy_ (u"ࠨࠢ੪"):
    bstack1ll11l1_opy_ = os.path.join(bstack1ll1ll1lll_opy_, bstack111l1llll_opy_)
    if not os.path.exists(bstack1ll11l1_opy_):
      bstack1ll11l1_opy_ = os.path.join(bstack1ll1ll1lll_opy_, bstack1ll11ll1l_opy_)
    if bstack1ll1ll1lll_opy_ != os.path.dirname(bstack1ll1ll1lll_opy_):
      bstack1ll1ll1lll_opy_ = os.path.dirname(bstack1ll1ll1lll_opy_)
    else:
      bstack1ll1ll1lll_opy_ = bstack1l_opy_ (u"ࠢࠣ੫")
  bstack1lll11lll_opy_ = bstack1ll11l1_opy_ if os.path.exists(bstack1ll11l1_opy_) else None
  return bstack1lll11lll_opy_
def bstack11ll11ll1_opy_(config):
    if bstack1l_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࠨ੬") in config:
      config[bstack1l_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭੭")] = config[bstack1l_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࠪ੮")]
    if bstack1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࡓࡵࡺࡩࡰࡰࡶࠫ੯") in config:
      config[bstack1l_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩੰ")] = config[bstack1l_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬ࡕࡰࡵ࡫ࡲࡲࡸ࠭ੱ")]
def bstack1l11l1l11l_opy_():
  bstack1ll11l1_opy_ = bstack111ll1l11l_opy_()
  if not os.path.exists(bstack1ll11l1_opy_):
    bstack11lll11ll1_opy_(
      bstack11l11llll1_opy_.format(os.getcwd()))
  try:
    with open(bstack1ll11l1_opy_, bstack1l_opy_ (u"ࠧࡳࠩੲ")) as stream:
      yaml.add_implicit_resolver(bstack1l_opy_ (u"ࠣࠣࡳࡥࡹ࡮ࡥࡹࠤੳ"), bstack111l1l111l_opy_)
      yaml.add_constructor(bstack1l_opy_ (u"ࠤࠤࡴࡦࡺࡨࡦࡺࠥੴ"), bstack1l111lll1l_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack11ll11ll1_opy_(config)
      return config
  except:
    with open(bstack1ll11l1_opy_, bstack1l_opy_ (u"ࠪࡶࠬੵ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack11ll11ll1_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack11lll11ll1_opy_(bstack11llll11l1_opy_.format(str(exc)))
def bstack111lllll11_opy_(config):
  bstack1lll1111ll_opy_ = bstack1ll11l111l_opy_(config)
  for option in list(bstack1lll1111ll_opy_):
    if option.lower() in bstack11llll1111_opy_ and option != bstack11llll1111_opy_[option.lower()]:
      bstack1lll1111ll_opy_[bstack11llll1111_opy_[option.lower()]] = bstack1lll1111ll_opy_[option]
      del bstack1lll1111ll_opy_[option]
  return config
def bstack1llll11l1l_opy_():
  global bstack11l1ll1lll_opy_
  for key, bstack11lll1lll_opy_ in bstack1111l1llll_opy_.items():
    if isinstance(bstack11lll1lll_opy_, list):
      for var in bstack11lll1lll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack11l1ll1lll_opy_[key] = os.environ[var]
          break
    elif bstack11lll1lll_opy_ in os.environ and os.environ[bstack11lll1lll_opy_] and str(os.environ[bstack11lll1lll_opy_]).strip():
      bstack11l1ll1lll_opy_[key] = os.environ[bstack11lll1lll_opy_]
  if bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭੶") in os.environ:
    bstack11l1ll1lll_opy_[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ੷")] = {}
    bstack11l1ll1lll_opy_[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ੸")][bstack1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ੹")] = os.environ[bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪ੺")]
def bstack11lll1lll1_opy_():
  global bstack111lll11l1_opy_
  global bstack1l111lllll_opy_
  bstack111l1ll1ll_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack1l_opy_ (u"ࠩ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ੻").lower() == val.lower():
      bstack111lll11l1_opy_[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ੼")] = {}
      bstack111lll11l1_opy_[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੽")][bstack1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ੾")] = sys.argv[idx + 1]
      bstack111l1ll1ll_opy_.extend([idx, idx + 1])
      break
  for key, bstack11l11l111l_opy_ in bstack1llll11111_opy_.items():
    if isinstance(bstack11l11l111l_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack11l11l111l_opy_:
          if bstack1l_opy_ (u"࠭࠭࠮ࠩ੿") + var.lower() == val.lower() and key not in bstack111lll11l1_opy_:
            bstack111lll11l1_opy_[key] = sys.argv[idx + 1]
            bstack1l111lllll_opy_ += bstack1l_opy_ (u"ࠧࠡ࠯࠰ࠫ઀") + var + bstack1l_opy_ (u"ࠨࠢࠪઁ") + shlex.quote(sys.argv[idx + 1])
            bstack111l1ll1ll_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack1l_opy_ (u"ࠩ࠰࠱ࠬં") + bstack11l11l111l_opy_.lower() == val.lower() and key not in bstack111lll11l1_opy_:
          bstack111lll11l1_opy_[key] = sys.argv[idx + 1]
          bstack1l111lllll_opy_ += bstack1l_opy_ (u"ࠪࠤ࠲࠳ࠧઃ") + bstack11l11l111l_opy_ + bstack1l_opy_ (u"ࠫࠥ࠭઄") + shlex.quote(sys.argv[idx + 1])
          bstack111l1ll1ll_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack111l1ll1ll_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack11111lll1l_opy_(config):
  bstack111l11ll1_opy_ = config.keys()
  for bstack11ll1l1l1l_opy_, bstack11ll11111_opy_ in bstack11ll1111ll_opy_.items():
    if bstack11ll11111_opy_ in bstack111l11ll1_opy_:
      config[bstack11ll1l1l1l_opy_] = config[bstack11ll11111_opy_]
      del config[bstack11ll11111_opy_]
  for bstack11ll1l1l1l_opy_, bstack11ll11111_opy_ in bstack11l1l11l11_opy_.items():
    if isinstance(bstack11ll11111_opy_, list):
      for bstack1111lll11_opy_ in bstack11ll11111_opy_:
        if bstack1111lll11_opy_ in bstack111l11ll1_opy_:
          config[bstack11ll1l1l1l_opy_] = config[bstack1111lll11_opy_]
          del config[bstack1111lll11_opy_]
          break
    elif bstack11ll11111_opy_ in bstack111l11ll1_opy_:
      config[bstack11ll1l1l1l_opy_] = config[bstack11ll11111_opy_]
      del config[bstack11ll11111_opy_]
  for bstack1111lll11_opy_ in list(config):
    for bstack1l1111l1ll_opy_ in bstack1l11llll1_opy_:
      if bstack1111lll11_opy_.lower() == bstack1l1111l1ll_opy_.lower() and bstack1111lll11_opy_ != bstack1l1111l1ll_opy_:
        config[bstack1l1111l1ll_opy_] = config[bstack1111lll11_opy_]
        del config[bstack1111lll11_opy_]
  bstack1ll1ll1111_opy_ = [{}]
  if not config.get(bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨઅ")):
    config[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩઆ")] = [{}]
  bstack1ll1ll1111_opy_ = config[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪઇ")]
  for platform in bstack1ll1ll1111_opy_:
    for bstack1111lll11_opy_ in list(platform):
      for bstack1l1111l1ll_opy_ in bstack1l11llll1_opy_:
        if bstack1111lll11_opy_.lower() == bstack1l1111l1ll_opy_.lower() and bstack1111lll11_opy_ != bstack1l1111l1ll_opy_:
          platform[bstack1l1111l1ll_opy_] = platform[bstack1111lll11_opy_]
          del platform[bstack1111lll11_opy_]
  for bstack11ll1l1l1l_opy_, bstack11ll11111_opy_ in bstack11l1l11l11_opy_.items():
    for platform in bstack1ll1ll1111_opy_:
      if isinstance(bstack11ll11111_opy_, list):
        for bstack1111lll11_opy_ in bstack11ll11111_opy_:
          if bstack1111lll11_opy_ in platform:
            platform[bstack11ll1l1l1l_opy_] = platform[bstack1111lll11_opy_]
            del platform[bstack1111lll11_opy_]
            break
      elif bstack11ll11111_opy_ in platform:
        platform[bstack11ll1l1l1l_opy_] = platform[bstack11ll11111_opy_]
        del platform[bstack11ll11111_opy_]
  for bstack11l11l1ll_opy_ in bstack1l1l1l1l1l_opy_:
    if bstack11l11l1ll_opy_ in config:
      if not bstack1l1l1l1l1l_opy_[bstack11l11l1ll_opy_] in config:
        config[bstack1l1l1l1l1l_opy_[bstack11l11l1ll_opy_]] = {}
      config[bstack1l1l1l1l1l_opy_[bstack11l11l1ll_opy_]].update(config[bstack11l11l1ll_opy_])
      del config[bstack11l11l1ll_opy_]
  for platform in bstack1ll1ll1111_opy_:
    for bstack11l11l1ll_opy_ in bstack1l1l1l1l1l_opy_:
      if bstack11l11l1ll_opy_ in list(platform):
        if not bstack1l1l1l1l1l_opy_[bstack11l11l1ll_opy_] in platform:
          platform[bstack1l1l1l1l1l_opy_[bstack11l11l1ll_opy_]] = {}
        platform[bstack1l1l1l1l1l_opy_[bstack11l11l1ll_opy_]].update(platform[bstack11l11l1ll_opy_])
        del platform[bstack11l11l1ll_opy_]
  config = bstack111lllll11_opy_(config)
  return config
def bstack1llllll111_opy_(config):
  global bstack1111ll11ll_opy_
  bstack1l1ll11l11_opy_ = False
  if bstack1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬઈ") in config and str(config[bstack1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ઉ")]).lower() != bstack1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩઊ"):
    if bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨઋ") not in config or str(config[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩઌ")]).lower() == bstack1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬઍ"):
      config[bstack1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭઎")] = False
    else:
      bstack111l111l11_opy_ = bstack11l1lll11l_opy_()
      if bstack1l_opy_ (u"ࠨ࡫ࡶࡘࡷ࡯ࡡ࡭ࡉࡵ࡭ࡩ࠭એ") in bstack111l111l11_opy_:
        if not bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઐ") in config:
          config[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઑ")] = {}
        config[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ઒")][bstack1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઓ")] = bstack1l_opy_ (u"࠭ࡡࡵࡵ࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠬઔ")
        bstack1l1ll11l11_opy_ = True
        bstack1111ll11ll_opy_ = config[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫક")].get(bstack1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪખ"))
  if bstack1l1l11llll_opy_(config) and bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ગ") in config and str(config[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧઘ")]).lower() != bstack1l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪઙ") and not bstack1l1ll11l11_opy_:
    if not bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩચ") in config:
      config[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪછ")] = {}
    if not config[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫજ")].get(bstack1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡈࡩ࡯ࡣࡵࡽࡎࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡡࡵ࡫ࡲࡲࠬઝ")) and not bstack1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫઞ") in config[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧટ")]:
      bstack1ll11l1l_opy_ = datetime.datetime.now()
      bstack111lllll1l_opy_ = bstack1ll11l1l_opy_.strftime(bstack1l_opy_ (u"ࠫࠪࡪ࡟ࠦࡤࡢࠩࡍࠫࡍࠨઠ"))
      hostname = socket.gethostname()
      bstack1ll1ll1l1l_opy_ = bstack1l_opy_ (u"ࠬ࠭ડ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1l_opy_ (u"࠭ࡻࡾࡡࡾࢁࡤࢁࡽࠨઢ").format(bstack111lllll1l_opy_, hostname, bstack1ll1ll1l1l_opy_)
      config[bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫણ")][bstack1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪત")] = identifier
    bstack1111ll11ll_opy_ = config[bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭થ")].get(bstack1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬદ"))
  return config
def bstack11l1l11lll_opy_():
  bstack11l1lllll_opy_ =  bstack11ll1111l_opy_()[bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠪધ")]
  return bstack11l1lllll_opy_ if bstack11l1lllll_opy_ else -1
def bstack1ll1llll1_opy_(bstack11l1lllll_opy_):
  global CONFIG
  if not bstack1l_opy_ (u"ࠬࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧન") in CONFIG[bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ઩")]:
    return
  CONFIG[bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩપ")] = CONFIG[bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪફ")].replace(
    bstack1l_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫબ"),
    str(bstack11l1lllll_opy_)
  )
def bstack1l11lllll1_opy_():
  global CONFIG
  if not bstack1l_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩભ") in CONFIG[bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭મ")]:
    return
  bstack1ll11l1l_opy_ = datetime.datetime.now()
  bstack111lllll1l_opy_ = bstack1ll11l1l_opy_.strftime(bstack1l_opy_ (u"ࠬࠫࡤ࠮ࠧࡥ࠱ࠪࡎ࠺ࠦࡏࠪય"))
  CONFIG[bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨર")] = CONFIG[bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઱")].replace(
    bstack1l_opy_ (u"ࠨࠦࡾࡈࡆ࡚ࡅࡠࡖࡌࡑࡊࢃࠧલ"),
    bstack111lllll1l_opy_
  )
def bstack1ll111lll_opy_():
  global CONFIG
  if bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫળ") in CONFIG and not bool(CONFIG[bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ઴")]):
    del CONFIG[bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭વ")]
    return
  if not bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧશ") in CONFIG:
    CONFIG[bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨષ")] = bstack1l_opy_ (u"ࠧࠤࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪસ")
  if bstack1l_opy_ (u"ࠨࠦࡾࡈࡆ࡚ࡅࡠࡖࡌࡑࡊࢃࠧહ") in CONFIG[bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ઺")]:
    bstack1l11lllll1_opy_()
    os.environ[bstack1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧ઻")] = CONFIG[bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ઼࠭")]
  if not bstack1l_opy_ (u"ࠬࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧઽ") in CONFIG[bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨા")]:
    return
  bstack11l1lllll_opy_ = bstack1l_opy_ (u"ࠧࠨિ")
  bstack1l1ll1l1l1_opy_ = bstack11l1l11lll_opy_()
  if bstack1l1ll1l1l1_opy_ != -1:
    bstack11l1lllll_opy_ = bstack1l_opy_ (u"ࠨࡅࡌࠤࠬી") + str(bstack1l1ll1l1l1_opy_)
  if bstack11l1lllll_opy_ == bstack1l_opy_ (u"ࠩࠪુ"):
    bstack1l1ll1ll11_opy_ = bstack1111l1l1l_opy_(CONFIG[bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ૂ")])
    if bstack1l1ll1ll11_opy_ != -1:
      bstack11l1lllll_opy_ = str(bstack1l1ll1ll11_opy_)
  if bstack11l1lllll_opy_:
    bstack1ll1llll1_opy_(bstack11l1lllll_opy_)
    os.environ[bstack1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨૃ")] = CONFIG[bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૄ")]
def bstack11ll1l111l_opy_(bstack1l11111l1_opy_, bstack11111ll1l1_opy_, path):
  json_data = {
    bstack1l_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪૅ"): bstack11111ll1l1_opy_
  }
  if os.path.exists(path):
    bstack11lllll1l_opy_ = json.load(open(path, bstack1l_opy_ (u"ࠧࡳࡤࠪ૆")))
  else:
    bstack11lllll1l_opy_ = {}
  bstack11lllll1l_opy_[bstack1l11111l1_opy_] = json_data
  with open(path, bstack1l_opy_ (u"ࠣࡹ࠮ࠦે")) as outfile:
    json.dump(bstack11lllll1l_opy_, outfile)
def bstack1111l1l1l_opy_(bstack1l11111l1_opy_):
  bstack1l11111l1_opy_ = str(bstack1l11111l1_opy_)
  bstack1l11llll1l_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠩࢁࠫૈ")), bstack1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪૉ"))
  try:
    if not os.path.exists(bstack1l11llll1l_opy_):
      os.makedirs(bstack1l11llll1l_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠫࢃ࠭૊")), bstack1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬો"), bstack1l_opy_ (u"࠭࠮ࡣࡷ࡬ࡰࡩ࠳࡮ࡢ࡯ࡨ࠱ࡨࡧࡣࡩࡧ࠱࡮ࡸࡵ࡮ࠨૌ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1l_opy_ (u"ࠧࡸ્ࠩ")):
        pass
      with open(file_path, bstack1l_opy_ (u"ࠣࡹ࠮ࠦ૎")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1l_opy_ (u"ࠩࡵࠫ૏")) as bstack11l11l11l_opy_:
      bstack1ll1l1lll1_opy_ = json.load(bstack11l11l11l_opy_)
    if bstack1l11111l1_opy_ in bstack1ll1l1lll1_opy_:
      bstack1l1ll111l_opy_ = bstack1ll1l1lll1_opy_[bstack1l11111l1_opy_][bstack1l_opy_ (u"ࠪ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૐ")]
      bstack1111llll1l_opy_ = int(bstack1l1ll111l_opy_) + 1
      bstack11ll1l111l_opy_(bstack1l11111l1_opy_, bstack1111llll1l_opy_, file_path)
      return bstack1111llll1l_opy_
    else:
      bstack11ll1l111l_opy_(bstack1l11111l1_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1l1l1111l_opy_.format(str(e)))
    return -1
def bstack1l11111lll_opy_(config):
  if not config[bstack1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭૑")] or not config[bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ૒")]:
    return True
  else:
    return False
def bstack11l1l1lll1_opy_(config, index=0):
  global bstack11l11111ll_opy_
  bstack1l11ll1ll1_opy_ = {}
  caps = bstack11l11ll11l_opy_ + bstack1ll1l111l_opy_
  if config.get(bstack1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ૓"), False):
    bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫ૔")] = True
    bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷࠬ૕")] = config.get(bstack1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭૖"), {})
  if bstack11l11111ll_opy_:
    caps += bstack11ll1l11ll_opy_
  for key in config:
    if key in caps + [bstack1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૗")]:
      continue
    bstack1l11ll1ll1_opy_[key] = config[key]
  if bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૘") in config:
    for bstack1l11l11ll1_opy_ in config[bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૙")][index]:
      if bstack1l11l11ll1_opy_ in caps:
        continue
      bstack1l11ll1ll1_opy_[bstack1l11l11ll1_opy_] = config[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૚")][index][bstack1l11l11ll1_opy_]
  bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"ࠧࡩࡱࡶࡸࡓࡧ࡭ࡦࠩ૛")] = socket.gethostname()
  if bstack1l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ૜") in bstack1l11ll1ll1_opy_:
    del (bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ૝")])
  return bstack1l11ll1ll1_opy_
def bstack11l1l1l111_opy_(config):
  global bstack11l11111ll_opy_
  bstack1ll111ll1_opy_ = {}
  caps = bstack1ll1l111l_opy_
  if bstack11l11111ll_opy_:
    caps += bstack11ll1l11ll_opy_
  for key in caps:
    if key in config:
      bstack1ll111ll1_opy_[key] = config[key]
  return bstack1ll111ll1_opy_
def bstack11ll111l11_opy_(bstack1l11ll1ll1_opy_, bstack1ll111ll1_opy_):
  bstack1l1lll111l_opy_ = {}
  for key in bstack1l11ll1ll1_opy_.keys():
    if key in bstack11ll1111ll_opy_:
      bstack1l1lll111l_opy_[bstack11ll1111ll_opy_[key]] = bstack1l11ll1ll1_opy_[key]
    else:
      bstack1l1lll111l_opy_[key] = bstack1l11ll1ll1_opy_[key]
  for key in bstack1ll111ll1_opy_:
    if key in bstack11ll1111ll_opy_:
      bstack1l1lll111l_opy_[bstack11ll1111ll_opy_[key]] = bstack1ll111ll1_opy_[key]
    else:
      bstack1l1lll111l_opy_[key] = bstack1ll111ll1_opy_[key]
  return bstack1l1lll111l_opy_
def bstack11lll1111_opy_(config, index=0):
  global bstack11l11111ll_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1ll11l1ll_opy_ = bstack111lllll1_opy_(bstack11111lllll_opy_, config, logger)
  bstack1ll111ll1_opy_ = bstack11l1l1l111_opy_(config)
  bstack1lll111ll_opy_ = bstack1ll1l111l_opy_
  bstack1lll111ll_opy_ += bstack1l11ll1lll_opy_
  bstack1ll111ll1_opy_ = update(bstack1ll111ll1_opy_, bstack1ll11l1ll_opy_)
  if bstack11l11111ll_opy_:
    bstack1lll111ll_opy_ += bstack11ll1l11ll_opy_
  if bstack1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૞") in config:
    if bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ૟") in config[bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૠ")][index]:
      caps[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫૡ")] = config[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪૢ")][index][bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ૣ")]
    if bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ૤") in config[bstack1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૥")][index]:
      caps[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ૦")] = str(config[bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૧")][index][bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ૨")])
    bstack1ll1111l11_opy_ = bstack111lllll1_opy_(bstack11111lllll_opy_, config[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૩")][index], logger)
    bstack1lll111ll_opy_ += list(bstack1ll1111l11_opy_.keys())
    for bstack11ll11l1l1_opy_ in bstack1lll111ll_opy_:
      if bstack11ll11l1l1_opy_ in config[bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૪")][index]:
        if bstack11ll11l1l1_opy_ == bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ૫"):
          try:
            bstack1ll1111l11_opy_[bstack11ll11l1l1_opy_] = str(config[bstack1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૬")][index][bstack11ll11l1l1_opy_] * 1.0)
          except:
            bstack1ll1111l11_opy_[bstack11ll11l1l1_opy_] = str(config[bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૭")][index][bstack11ll11l1l1_opy_])
        else:
          bstack1ll1111l11_opy_[bstack11ll11l1l1_opy_] = config[bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૮")][index][bstack11ll11l1l1_opy_]
        del (config[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૯")][index][bstack11ll11l1l1_opy_])
    bstack1ll111ll1_opy_ = update(bstack1ll111ll1_opy_, bstack1ll1111l11_opy_)
  bstack1l11ll1ll1_opy_ = bstack11l1l1lll1_opy_(config, index)
  for bstack1111lll11_opy_ in bstack1ll1l111l_opy_ + list(bstack1ll11l1ll_opy_.keys()):
    if bstack1111lll11_opy_ in bstack1l11ll1ll1_opy_:
      bstack1ll111ll1_opy_[bstack1111lll11_opy_] = bstack1l11ll1ll1_opy_[bstack1111lll11_opy_]
      del (bstack1l11ll1ll1_opy_[bstack1111lll11_opy_])
  if bstack1l1111llll_opy_(config):
    bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧ૰")] = True
    caps.update(bstack1ll111ll1_opy_)
    caps[bstack1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ૱")] = bstack1l11ll1ll1_opy_
  else:
    bstack1l11ll1ll1_opy_[bstack1l_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩ૲")] = False
    caps.update(bstack11ll111l11_opy_(bstack1l11ll1ll1_opy_, bstack1ll111ll1_opy_))
    if bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ૳") in caps:
      caps[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬ૴")] = caps[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ૵")]
      del (caps[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ૶")])
    if bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ૷") in caps:
      caps[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ૸")] = caps[bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪૹ")]
      del (caps[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫૺ")])
  return caps
def bstack11l1l11ll1_opy_():
  global bstack11l1ll1ll1_opy_
  global CONFIG
  if bstack1lll1lll1l_opy_() <= version.parse(bstack1l_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫૻ")):
    if bstack11l1ll1ll1_opy_ != bstack1l_opy_ (u"ࠬ࠭ૼ"):
      return bstack1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢ૽") + bstack11l1ll1ll1_opy_ + bstack1l_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦ૾")
    return bstack11ll1ll1l_opy_
  if bstack11l1ll1ll1_opy_ != bstack1l_opy_ (u"ࠨࠩ૿"):
    return bstack1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦ଀") + bstack11l1ll1ll1_opy_ + bstack1l_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦଁ")
  return bstack1l1l1l1lll_opy_
def bstack1l1lll1l1l_opy_(options):
  return hasattr(options, bstack1l_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬଂ"))
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
def bstack1l1ll11ll1_opy_(options, bstack1l1ll11lll_opy_):
  for bstack111ll1llll_opy_ in bstack1l1ll11lll_opy_:
    if bstack111ll1llll_opy_ in [bstack1l_opy_ (u"ࠬࡧࡲࡨࡵࠪଃ"), bstack1l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ଄")]:
      continue
    if bstack111ll1llll_opy_ in options._experimental_options:
      options._experimental_options[bstack111ll1llll_opy_] = update(options._experimental_options[bstack111ll1llll_opy_],
                                                         bstack1l1ll11lll_opy_[bstack111ll1llll_opy_])
    else:
      options.add_experimental_option(bstack111ll1llll_opy_, bstack1l1ll11lll_opy_[bstack111ll1llll_opy_])
  if bstack1l_opy_ (u"ࠧࡢࡴࡪࡷࠬଅ") in bstack1l1ll11lll_opy_:
    for arg in bstack1l1ll11lll_opy_[bstack1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଆ")]:
      options.add_argument(arg)
    del (bstack1l1ll11lll_opy_[bstack1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧଇ")])
  if bstack1l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧଈ") in bstack1l1ll11lll_opy_:
    for ext in bstack1l1ll11lll_opy_[bstack1l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨଉ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l1ll11lll_opy_[bstack1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩଊ")])
def bstack11ll111l1l_opy_(options, bstack1lllll11ll_opy_):
  if bstack1l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬଋ") in bstack1lllll11ll_opy_:
    for bstack11llll1l1_opy_ in bstack1lllll11ll_opy_[bstack1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ଌ")]:
      if bstack11llll1l1_opy_ in options._preferences:
        options._preferences[bstack11llll1l1_opy_] = update(options._preferences[bstack11llll1l1_opy_], bstack1lllll11ll_opy_[bstack1l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ଍")][bstack11llll1l1_opy_])
      else:
        options.set_preference(bstack11llll1l1_opy_, bstack1lllll11ll_opy_[bstack1l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ଎")][bstack11llll1l1_opy_])
  if bstack1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଏ") in bstack1lllll11ll_opy_:
    for arg in bstack1lllll11ll_opy_[bstack1l_opy_ (u"ࠫࡦࡸࡧࡴࠩଐ")]:
      options.add_argument(arg)
def bstack11lllllll1_opy_(options, bstack11l1ll1l11_opy_):
  if bstack1l_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭଑") in bstack11l1ll1l11_opy_:
    options.use_webview(bool(bstack11l1ll1l11_opy_[bstack1l_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࠧ଒")]))
  bstack1l1ll11ll1_opy_(options, bstack11l1ll1l11_opy_)
def bstack1l1l1ll11_opy_(options, bstack111l1lll1l_opy_):
  for bstack1ll11llll_opy_ in bstack111l1lll1l_opy_:
    if bstack1ll11llll_opy_ in [bstack1l_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫଓ"), bstack1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଔ")]:
      continue
    options.set_capability(bstack1ll11llll_opy_, bstack111l1lll1l_opy_[bstack1ll11llll_opy_])
  if bstack1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧକ") in bstack111l1lll1l_opy_:
    for arg in bstack111l1lll1l_opy_[bstack1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଖ")]:
      options.add_argument(arg)
  if bstack1l_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨଗ") in bstack111l1lll1l_opy_:
    options.bstack1l1111l1l_opy_(bool(bstack111l1lll1l_opy_[bstack1l_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩଘ")]))
def bstack11l111l111_opy_(options, bstack11ll1l11l_opy_):
  for bstack11llllllll_opy_ in bstack11ll1l11l_opy_:
    if bstack11llllllll_opy_ in [bstack1l_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪଙ"), bstack1l_opy_ (u"ࠧࡢࡴࡪࡷࠬଚ")]:
      continue
    options._options[bstack11llllllll_opy_] = bstack11ll1l11l_opy_[bstack11llllllll_opy_]
  if bstack1l_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬଛ") in bstack11ll1l11l_opy_:
    for bstack11l111l1l1_opy_ in bstack11ll1l11l_opy_[bstack1l_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ଜ")]:
      options.bstack1l11111ll1_opy_(
        bstack11l111l1l1_opy_, bstack11ll1l11l_opy_[bstack1l_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧଝ")][bstack11l111l1l1_opy_])
  if bstack1l_opy_ (u"ࠫࡦࡸࡧࡴࠩଞ") in bstack11ll1l11l_opy_:
    for arg in bstack11ll1l11l_opy_[bstack1l_opy_ (u"ࠬࡧࡲࡨࡵࠪଟ")]:
      options.add_argument(arg)
def bstack1l1ll1lll_opy_(options, caps):
  if not hasattr(options, bstack1l_opy_ (u"࠭ࡋࡆ࡛ࠪଠ")):
    return
  if options.KEY == bstack1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬଡ"):
    options = bstack11111ll1_opy_.bstack11111ll1ll_opy_(bstack11111llll_opy_=options, config=CONFIG)
  if options.KEY == bstack1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ଢ") and options.KEY in caps:
    bstack1l1ll11ll1_opy_(options, caps[bstack1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧଣ")])
  elif options.KEY == bstack1l_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨତ") and options.KEY in caps:
    bstack11ll111l1l_opy_(options, caps[bstack1l_opy_ (u"ࠫࡲࡵࡺ࠻ࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩଥ")])
  elif options.KEY == bstack1l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ଦ") and options.KEY in caps:
    bstack1l1l1ll11_opy_(options, caps[bstack1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧଧ")])
  elif options.KEY == bstack1l_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨନ") and options.KEY in caps:
    bstack11lllllll1_opy_(options, caps[bstack1l_opy_ (u"ࠨ࡯ࡶ࠾ࡪࡪࡧࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ଩")])
  elif options.KEY == bstack1l_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨପ") and options.KEY in caps:
    bstack11l111l111_opy_(options, caps[bstack1l_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩଫ")])
def bstack11111l1l1_opy_(caps):
  global bstack11l11111ll_opy_
  if isinstance(os.environ.get(bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬବ")), str):
    bstack11l11111ll_opy_ = eval(os.getenv(bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ଭ")))
  if bstack11l11111ll_opy_:
    if bstack1ll111ll1l_opy_() < version.parse(bstack1l_opy_ (u"࠭࠲࠯࠵࠱࠴ࠬମ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧଯ")
    if bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ର") in caps:
      browser = caps[bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ଱")]
    elif bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫଲ") in caps:
      browser = caps[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬଳ")]
    browser = str(browser).lower()
    if browser == bstack1l_opy_ (u"ࠬ࡯ࡰࡩࡱࡱࡩࠬ଴") or browser == bstack1l_opy_ (u"࠭ࡩࡱࡣࡧࠫଵ"):
      browser = bstack1l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧଶ")
    if browser == bstack1l_opy_ (u"ࠨࡵࡤࡱࡸࡻ࡮ࡨࠩଷ"):
      browser = bstack1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩସ")
    if browser not in [bstack1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪହ"), bstack1l_opy_ (u"ࠫࡪࡪࡧࡦࠩ଺"), bstack1l_opy_ (u"ࠬ࡯ࡥࠨ଻"), bstack1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮଼࠭"), bstack1l_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨଽ")]:
      return None
    try:
      package = bstack1l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࠱ࡻࡪࡨࡤࡳ࡫ࡹࡩࡷ࠴ࡻࡾ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪା").format(browser)
      name = bstack1l_opy_ (u"ࠩࡒࡴࡹ࡯࡯࡯ࡵࠪି")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1l1lll1l1l_opy_(options):
        return None
      for bstack1111lll11_opy_ in caps.keys():
        options.set_capability(bstack1111lll11_opy_, caps[bstack1111lll11_opy_])
      bstack1l1ll1lll_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1l11l1l1ll_opy_(options, bstack11l1l1lll_opy_):
  if not bstack1l1lll1l1l_opy_(options):
    return
  for bstack1111lll11_opy_ in bstack11l1l1lll_opy_.keys():
    if bstack1111lll11_opy_ in bstack1l11ll1lll_opy_:
      continue
    if bstack1111lll11_opy_ in options._caps and type(options._caps[bstack1111lll11_opy_]) in [dict, list]:
      options._caps[bstack1111lll11_opy_] = update(options._caps[bstack1111lll11_opy_], bstack11l1l1lll_opy_[bstack1111lll11_opy_])
    else:
      options.set_capability(bstack1111lll11_opy_, bstack11l1l1lll_opy_[bstack1111lll11_opy_])
  bstack1l1ll1lll_opy_(options, bstack11l1l1lll_opy_)
  if bstack1l_opy_ (u"ࠪࡱࡴࢀ࠺ࡥࡧࡥࡹ࡬࡭ࡥࡳࡃࡧࡨࡷ࡫ࡳࡴࠩୀ") in options._caps:
    if options._caps[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩୁ")] and options._caps[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪୂ")].lower() != bstack1l_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧୃ"):
      del options._caps[bstack1l_opy_ (u"ࠧ࡮ࡱࡽ࠾ࡩ࡫ࡢࡶࡩࡪࡩࡷࡇࡤࡥࡴࡨࡷࡸ࠭ୄ")]
def bstack1l11ll11ll_opy_(proxy_config):
  if bstack1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ୅") in proxy_config:
    proxy_config[bstack1l_opy_ (u"ࠩࡶࡷࡱࡖࡲࡰࡺࡼࠫ୆")] = proxy_config[bstack1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧେ")]
    del (proxy_config[bstack1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨୈ")])
  if bstack1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ୉") in proxy_config and proxy_config[bstack1l_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩ୊")].lower() != bstack1l_opy_ (u"ࠧࡥ࡫ࡵࡩࡨࡺࠧୋ"):
    proxy_config[bstack1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫୌ")] = bstack1l_opy_ (u"ࠩࡰࡥࡳࡻࡡ࡭୍ࠩ")
  if bstack1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡃࡸࡸࡴࡩ࡯࡯ࡨ࡬࡫࡚ࡸ࡬ࠨ୎") in proxy_config:
    proxy_config[bstack1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧ୏")] = bstack1l_opy_ (u"ࠬࡶࡡࡤࠩ୐")
  return proxy_config
def bstack1lll11l1ll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୑") in config:
    return proxy
  config[bstack1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭୒")] = bstack1l11ll11ll_opy_(config[bstack1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧ୓")])
  if proxy == None:
    proxy = Proxy(config[bstack1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨ୔")])
  return proxy
def bstack111ll1111l_opy_(self):
  global CONFIG
  global bstack1l1ll1l1ll_opy_
  try:
    proxy = bstack1l1llllll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1l_opy_ (u"ࠪ࠲ࡵࡧࡣࠨ୕")):
        proxies = bstack1lll1l1ll1_opy_(proxy, bstack11l1l11ll1_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll1111ll1_opy_ = proxies.popitem()
          if bstack1l_opy_ (u"ࠦ࠿࠵࠯ࠣୖ") in bstack1ll1111ll1_opy_:
            return bstack1ll1111ll1_opy_
          else:
            return bstack1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨୗ") + bstack1ll1111ll1_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡳࡶࡴࡾࡹࠡࡷࡵࡰࠥࡀࠠࡼࡿࠥ୘").format(str(e)))
  return bstack1l1ll1l1ll_opy_(self)
def bstack111ll11111_opy_():
  global CONFIG
  return bstack111l1l11ll_opy_(CONFIG) and bstack11l11l1l11_opy_() and bstack1lll1lll1l_opy_() >= version.parse(bstack11l1lll11_opy_)
def bstack1l111ll111_opy_():
  global CONFIG
  return (bstack1l_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ୙") in CONFIG or bstack1l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ୚") in CONFIG) and bstack111l1ll11_opy_()
def bstack1ll11l111l_opy_(config):
  bstack1lll1111ll_opy_ = {}
  if bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୛") in config:
    bstack1lll1111ll_opy_ = config[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧଡ଼")]
  if bstack1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪଢ଼") in config:
    bstack1lll1111ll_opy_ = config[bstack1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୞")]
  proxy = bstack1l1llllll_opy_(config)
  if proxy:
    if proxy.endswith(bstack1l_opy_ (u"࠭࠮ࡱࡣࡦࠫୟ")) and os.path.isfile(proxy):
      bstack1lll1111ll_opy_[bstack1l_opy_ (u"ࠧ࠮ࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪୠ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1l_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭ୡ")):
        proxies = bstack1111l1ll1l_opy_(config, bstack11l1l11ll1_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll1111ll1_opy_ = proxies.popitem()
          if bstack1l_opy_ (u"ࠤ࠽࠳࠴ࠨୢ") in bstack1ll1111ll1_opy_:
            parsed_url = urlparse(bstack1ll1111ll1_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1l_opy_ (u"ࠥ࠾࠴࠵ࠢୣ") + bstack1ll1111ll1_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1lll1111ll_opy_[bstack1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡋࡳࡸࡺࠧ୤")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1lll1111ll_opy_[bstack1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡴࡸࡴࠨ୥")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1lll1111ll_opy_[bstack1l_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡚ࡹࡥࡳࠩ୦")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1lll1111ll_opy_[bstack1l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖࡡࡴࡵࠪ୧")] = str(parsed_url.password)
  return bstack1lll1111ll_opy_
def bstack11l111l11l_opy_(config):
  if bstack1l_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭୨") in config:
    return config[bstack1l_opy_ (u"ࠩࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠧ୩")]
  return {}
def bstack1l11llllll_opy_(caps):
  global bstack1111ll11ll_opy_
  if bstack1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ୪") in caps:
    caps[bstack1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ୫")][bstack1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫ୬")] = True
    if bstack1111ll11ll_opy_:
      caps[bstack1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ୭")][bstack1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ୮")] = bstack1111ll11ll_opy_
  else:
    caps[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭୯")] = True
    if bstack1111ll11ll_opy_:
      caps[bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ୰")] = bstack1111ll11ll_opy_
@measure(event_name=EVENTS.bstack1ll111l11l_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack1l1l1l1ll1_opy_():
  global CONFIG
  if not bstack1l1l11llll_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧୱ") in CONFIG and bstack1l11l1ll1l_opy_(CONFIG[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ୲")]):
    if (
      bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୳") in CONFIG
      and bstack1l11l1ll1l_opy_(CONFIG[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ୴")].get(bstack1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠫ୵")))
    ):
      logger.debug(bstack1l_opy_ (u"ࠣࡎࡲࡧࡦࡲࠠࡣ࡫ࡱࡥࡷࡿࠠ࡯ࡱࡷࠤࡸࡺࡡࡳࡶࡨࡨࠥࡧࡳࠡࡵ࡮࡭ࡵࡈࡩ࡯ࡣࡵࡽࡎࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡡࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡧࡱࡥࡧࡲࡥࡥࠤ୶"))
      return
    bstack1lll1111ll_opy_ = bstack1ll11l111l_opy_(CONFIG)
    bstack11ll11l111_opy_(CONFIG[bstack1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ୷")], bstack1lll1111ll_opy_)
def bstack11ll11l111_opy_(key, bstack1lll1111ll_opy_):
  global bstack111lll111l_opy_
  logger.info(bstack1ll1l1111_opy_)
  try:
    bstack111lll111l_opy_ = Local()
    bstack11l1111l1_opy_ = {bstack1l_opy_ (u"ࠪ࡯ࡪࡿࠧ୸"): key}
    bstack11l1111l1_opy_.update(bstack1lll1111ll_opy_)
    logger.debug(bstack11lll1l1l1_opy_.format(str(bstack11l1111l1_opy_)).replace(key, bstack1l_opy_ (u"ࠫࡠࡘࡅࡅࡃࡆࡘࡊࡊ࡝ࠨ୹")))
    bstack111lll111l_opy_.start(**bstack11l1111l1_opy_)
    if bstack111lll111l_opy_.isRunning():
      logger.info(bstack1l1l1l1l1_opy_)
  except Exception as e:
    bstack11lll11ll1_opy_(bstack111111ll1_opy_.format(str(e)))
def bstack1l11lll1ll_opy_():
  global bstack111lll111l_opy_
  if bstack111lll111l_opy_.isRunning():
    logger.info(bstack11l11lll11_opy_)
    bstack111lll111l_opy_.stop()
  bstack111lll111l_opy_ = None
def bstack1ll1l11l11_opy_(bstack1l1ll1l1l_opy_=[]):
  global CONFIG
  bstack1ll1ll11l_opy_ = []
  bstack1l1ll11l1l_opy_ = [bstack1l_opy_ (u"ࠬࡵࡳࠨ୺"), bstack1l_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ୻"), bstack1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ୼"), bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ୽"), bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ୾"), bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ୿")]
  try:
    for err in bstack1l1ll1l1l_opy_:
      bstack1l1ll11l1_opy_ = {}
      for k in bstack1l1ll11l1l_opy_:
        val = CONFIG[bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ஀")][int(err[bstack1l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ஁")])].get(k)
        if val:
          bstack1l1ll11l1_opy_[k] = val
      if(err[bstack1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬஂ")] != bstack1l_opy_ (u"ࠧࠨஃ")):
        bstack1l1ll11l1_opy_[bstack1l_opy_ (u"ࠨࡶࡨࡷࡹࡹࠧ஄")] = {
          err[bstack1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧஅ")]: err[bstack1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩஆ")]
        }
        bstack1ll1ll11l_opy_.append(bstack1l1ll11l1_opy_)
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡰࡴࡰࡥࡹࡺࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷ࠾ࠥ࠭இ") + str(e))
  finally:
    return bstack1ll1ll11l_opy_
def bstack1lll1ll1ll_opy_(file_name):
  bstack1lllll1111_opy_ = []
  try:
    bstack1lll11111_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1lll11111_opy_):
      with open(bstack1lll11111_opy_) as f:
        bstack1111l1111_opy_ = json.load(f)
        bstack1lllll1111_opy_ = bstack1111l1111_opy_
      os.remove(bstack1lll11111_opy_)
    return bstack1lllll1111_opy_
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧ࡫ࡱࡨ࡮ࡴࡧࠡࡧࡵࡶࡴࡸࠠ࡭࡫ࡶࡸ࠿ࠦࠧஈ") + str(e))
    return bstack1lllll1111_opy_
def bstack1l1l111lll_opy_():
  try:
      from bstack_utils.constants import bstack1ll11l1l1l_opy_, EVENTS
      from bstack_utils.helper import bstack1ll1llll11_opy_, get_host_info, bstack1lll1ll1l_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack1l1l1l11ll_opy_ = os.path.join(os.getcwd(), bstack1l_opy_ (u"࠭࡬ࡰࡩࠪஉ"), bstack1l_opy_ (u"ࠧ࡬ࡧࡼ࠱ࡲ࡫ࡴࡳ࡫ࡦࡷ࠳ࡰࡳࡰࡰࠪஊ"))
      lock = FileLock(bstack1l1l1l11ll_opy_+bstack1l_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢ஋"))
      def bstack1lll11ll_opy_():
          try:
              with lock:
                  with open(bstack1l1l1l11ll_opy_, bstack1l_opy_ (u"ࠤࡵࠦ஌"), encoding=bstack1l_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤ஍")) as file:
                      data = json.load(file)
                      config = {
                          bstack1l_opy_ (u"ࠦ࡭࡫ࡡࡥࡧࡵࡷࠧஎ"): {
                              bstack1l_opy_ (u"ࠧࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠦஏ"): bstack1l_opy_ (u"ࠨࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠤஐ"),
                          }
                      }
                      bstack11ll1lll1l_opy_ = datetime.utcnow()
                      bstack1ll11l1l_opy_ = bstack11ll1lll1l_opy_.strftime(bstack1l_opy_ (u"࡛ࠢࠦ࠰ࠩࡲ࠳ࠥࡥࡖࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࠲ࠪ࡬ࠠࡖࡖࡆࠦ஑"))
                      test_id = os.environ.get(bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ஒ")) if os.environ.get(bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧஓ")) else bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠥࡷࡩࡱࡒࡶࡰࡌࡨࠧஔ"))
                      payload = {
                          bstack1l_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠣக"): bstack1l_opy_ (u"ࠧࡹࡤ࡬ࡡࡨࡺࡪࡴࡴࡴࠤ஖"),
                          bstack1l_opy_ (u"ࠨࡤࡢࡶࡤࠦ஗"): {
                              bstack1l_opy_ (u"ࠢࡵࡧࡶࡸ࡭ࡻࡢࡠࡷࡸ࡭ࡩࠨ஘"): test_id,
                              bstack1l_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡥࡡࡧࡥࡾࠨங"): bstack1ll11l1l_opy_,
                              bstack1l_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࠨச"): bstack1l_opy_ (u"ࠥࡗࡉࡑࡆࡦࡣࡷࡹࡷ࡫ࡐࡦࡴࡩࡳࡷࡳࡡ࡯ࡥࡨࠦ஛"),
                              bstack1l_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢ࡮ࡸࡵ࡮ࠣஜ"): {
                                  bstack1l_opy_ (u"ࠧࡳࡥࡢࡵࡸࡶࡪࡹࠢ஝"): data,
                                  bstack1l_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣஞ"): bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤட"))
                              },
                              bstack1l_opy_ (u"ࠣࡷࡶࡩࡷࡥࡤࡢࡶࡤࠦ஠"): bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠤࡸࡷࡪࡸࡎࡢ࡯ࡨࠦ஡")),
                              bstack1l_opy_ (u"ࠥ࡬ࡴࡹࡴࡠ࡫ࡱࡪࡴࠨ஢"): get_host_info()
                          }
                      }
                      bstack11lll11lll_opy_ = bstack1l111ll1ll_opy_(cli.config, [bstack1l_opy_ (u"ࠦࡦࡶࡩࡴࠤண"), bstack1l_opy_ (u"ࠧ࡫ࡤࡴࡋࡱࡷࡹࡸࡵ࡮ࡧࡱࡸࡦࡺࡩࡰࡰࠥத"), bstack1l_opy_ (u"ࠨࡡࡱ࡫ࠥ஥")], bstack1ll11l1l1l_opy_)
                      response = bstack1ll1llll11_opy_(bstack1l_opy_ (u"ࠢࡑࡑࡖࡘࠧ஦"), bstack11lll11lll_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack1l_opy_ (u"ࠣࡆࡤࡸࡦࠦࡳࡦࡰࡷࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻࠣࡸࡴࠦࡻࡾࠢࡺ࡭ࡹ࡮ࠠࡥࡣࡷࡥࠥࢁࡽࠣ஧").format(bstack1ll11l1l1l_opy_, payload))
                      else:
                          logger.debug(bstack1l_opy_ (u"ࠤࡕࡩࡶࡻࡥࡴࡶࠣࡪࡦ࡯࡬ࡦࡦࠣࡪࡴࡸࠠࡼࡿࠣࡻ࡮ࡺࡨࠡࡦࡤࡸࡦࠦࡻࡾࠤந").format(bstack1ll11l1l1l_opy_, payload))
          except Exception as e:
              logger.debug(bstack1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡰࡧࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤࢀࢃࠢன").format(e))
      bstack1lll11ll_opy_()
      bstack1lll11l11_opy_(bstack1l1l1l11ll_opy_, logger)
  except:
    pass
def bstack1l1l11111_opy_():
  global bstack1l111lll1_opy_
  global bstack1ll1ll1l11_opy_
  global bstack11ll1llll1_opy_
  global bstack1111ll1l1_opy_
  global bstack111lll1l1_opy_
  global bstack1ll1ll111_opy_
  global CONFIG
  bstack1111lll11l_opy_ = os.environ.get(bstack1l_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬப"))
  if bstack1111lll11l_opy_ in [bstack1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ஫"), bstack1l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ஬")]:
    bstack11ll111l1_opy_()
  percy.shutdown()
  if bstack1l111lll1_opy_:
    logger.warning(bstack1ll11lllll_opy_.format(str(bstack1l111lll1_opy_)))
  else:
    try:
      bstack11lllll1l_opy_ = bstack1l1llll1ll_opy_(bstack1l_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭஭"), logger)
      if bstack11lllll1l_opy_.get(bstack1l_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ம")) and bstack11lllll1l_opy_.get(bstack1l_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧய")).get(bstack1l_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬர")):
        logger.warning(bstack1ll11lllll_opy_.format(str(bstack11lllll1l_opy_[bstack1l_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩற")][bstack1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧல")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1l111l11l_opy_.invoke(Events.bstack11l1ll111_opy_)
  logger.info(bstack11l11l1ll1_opy_)
  global bstack111lll111l_opy_
  if bstack111lll111l_opy_:
    bstack1l11lll1ll_opy_()
  try:
    with bstack11l1l1111l_opy_:
      bstack1l1l11lll1_opy_ = bstack1ll1ll1l11_opy_.copy()
    for driver in bstack1l1l11lll1_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1llll11lll_opy_)
  if bstack1ll1ll111_opy_ == bstack1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬள"):
    bstack111lll1l1_opy_ = bstack1lll1ll1ll_opy_(bstack1l_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨழ"))
  if bstack1ll1ll111_opy_ == bstack1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨவ") and len(bstack1111ll1l1_opy_) == 0:
    bstack1111ll1l1_opy_ = bstack1lll1ll1ll_opy_(bstack1l_opy_ (u"ࠩࡳࡻࡤࡶࡹࡵࡧࡶࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧஶ"))
    if len(bstack1111ll1l1_opy_) == 0:
      bstack1111ll1l1_opy_ = bstack1lll1ll1ll_opy_(bstack1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡴࡵࡶ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩஷ"))
  bstack1lll111ll1_opy_ = bstack1l_opy_ (u"ࠫࠬஸ")
  if len(bstack11ll1llll1_opy_) > 0:
    bstack1lll111ll1_opy_ = bstack1ll1l11l11_opy_(bstack11ll1llll1_opy_)
  elif len(bstack1111ll1l1_opy_) > 0:
    bstack1lll111ll1_opy_ = bstack1ll1l11l11_opy_(bstack1111ll1l1_opy_)
  elif len(bstack111lll1l1_opy_) > 0:
    bstack1lll111ll1_opy_ = bstack1ll1l11l11_opy_(bstack111lll1l1_opy_)
  elif len(bstack1111l1lll1_opy_) > 0:
    bstack1lll111ll1_opy_ = bstack1ll1l11l11_opy_(bstack1111l1lll1_opy_)
  if bool(bstack1lll111ll1_opy_):
    bstack1111l11l1l_opy_(bstack1lll111ll1_opy_)
  else:
    bstack1111l11l1l_opy_()
  bstack1lll11l11_opy_(bstack1111lll1l_opy_, logger)
  if bstack1111lll11l_opy_ not in [bstack1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ஹ")]:
    bstack1l1l111lll_opy_()
  bstack111ll1l1l_opy_.bstack1l1l1l11_opy_(CONFIG)
  if len(bstack111lll1l1_opy_) > 0:
    sys.exit(len(bstack111lll1l1_opy_))
def bstack11lll1ll1l_opy_(bstack1ll1llll1l_opy_, frame):
  global bstack1lll1ll1l_opy_
  logger.error(bstack11l1l1l1l1_opy_)
  bstack1lll1ll1l_opy_.set_property(bstack1l_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡎࡰࠩ஺"), bstack1ll1llll1l_opy_)
  if hasattr(signal, bstack1l_opy_ (u"ࠧࡔ࡫ࡪࡲࡦࡲࡳࠨ஻")):
    bstack1lll1ll1l_opy_.set_property(bstack1l_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ஼"), signal.Signals(bstack1ll1llll1l_opy_).name)
  else:
    bstack1lll1ll1l_opy_.set_property(bstack1l_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩ஽"), bstack1l_opy_ (u"ࠪࡗࡎࡍࡕࡏࡍࡑࡓ࡜ࡔࠧா"))
  if cli.is_running():
    bstack1l111l11l_opy_.invoke(Events.bstack11l1ll111_opy_)
  bstack1111lll11l_opy_ = os.environ.get(bstack1l_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬி"))
  if bstack1111lll11l_opy_ == bstack1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬீ") and not cli.is_enabled(CONFIG):
    bstack1ll1lll1_opy_.stop(bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭ு")))
  bstack1l1l11111_opy_()
  sys.exit(1)
def bstack11lll11ll1_opy_(err):
  logger.critical(bstack1ll1l1l11l_opy_.format(str(err)))
  bstack1111l11l1l_opy_(bstack1ll1l1l11l_opy_.format(str(err)), True)
  atexit.unregister(bstack1l1l11111_opy_)
  bstack11ll111l1_opy_()
  sys.exit(1)
def bstack1l1111l1l1_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1111l11l1l_opy_(message, True)
  atexit.unregister(bstack1l1l11111_opy_)
  bstack11ll111l1_opy_()
  sys.exit(1)
def bstack111l1lll11_opy_():
  global CONFIG
  global bstack111lll11l1_opy_
  global bstack11l1ll1lll_opy_
  global bstack1lll1ll1l1_opy_
  CONFIG = bstack1l11l1l11l_opy_()
  load_dotenv(CONFIG.get(bstack1l_opy_ (u"ࠧࡦࡰࡹࡊ࡮ࡲࡥࠨூ")))
  bstack1llll11l1l_opy_()
  bstack11lll1lll1_opy_()
  CONFIG = bstack11111lll1l_opy_(CONFIG)
  update(CONFIG, bstack11l1ll1lll_opy_)
  update(CONFIG, bstack111lll11l1_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1llllll111_opy_(CONFIG)
  bstack1lll1ll1l1_opy_ = bstack1l1l11llll_opy_(CONFIG)
  os.environ[bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ௃")] = bstack1lll1ll1l1_opy_.__str__().lower()
  bstack1lll1ll1l_opy_.set_property(bstack1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ௄"), bstack1lll1ll1l1_opy_)
  if (bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௅") in CONFIG and bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧெ") in bstack111lll11l1_opy_) or (
          bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨே") in CONFIG and bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩை") not in bstack11l1ll1lll_opy_):
    if os.getenv(bstack1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ௉")):
      CONFIG[bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪொ")] = os.getenv(bstack1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭ோ"))
    else:
      if not CONFIG.get(bstack1l_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠨௌ"), bstack1l_opy_ (u"்ࠦࠧ")) in bstack11lll11l11_opy_:
        bstack1ll111lll_opy_()
  elif (bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௎") not in CONFIG and bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ௏") in CONFIG) or (
          bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪௐ") in bstack11l1ll1lll_opy_ and bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௑") not in bstack111lll11l1_opy_):
    del (CONFIG[bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ௒")])
  if bstack1l11111lll_opy_(CONFIG):
    bstack11lll11ll1_opy_(bstack11llll11ll_opy_)
  Config.bstack1llll11ll_opy_().set_property(bstack1l_opy_ (u"ࠥࡹࡸ࡫ࡲࡏࡣࡰࡩࠧ௓"), CONFIG[bstack1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭௔")])
  bstack11ll1ll111_opy_()
  bstack1ll1l1l1l_opy_()
  if bstack11l11111ll_opy_ and not CONFIG.get(bstack1l_opy_ (u"ࠧ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠣ௕"), bstack1l_opy_ (u"ࠨࠢ௖")) in bstack11lll11l11_opy_:
    CONFIG[bstack1l_opy_ (u"ࠧࡢࡲࡳࠫௗ")] = bstack11llll1l1l_opy_(CONFIG)
    logger.info(bstack11lll1111l_opy_.format(CONFIG[bstack1l_opy_ (u"ࠨࡣࡳࡴࠬ௘")]))
  if not bstack1lll1ll1l1_opy_:
    CONFIG[bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ௙")] = [{}]
def bstack111l1ll111_opy_(config, bstack111lll1lll_opy_):
  global CONFIG
  global bstack11l11111ll_opy_
  CONFIG = config
  bstack11l11111ll_opy_ = bstack111lll1lll_opy_
def bstack1ll1l1l1l_opy_():
  global CONFIG
  global bstack11l11111ll_opy_
  if bstack1l_opy_ (u"ࠪࡥࡵࡶࠧ௚") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l1111l1l1_opy_(e, bstack1ll11l11l_opy_)
    bstack11l11111ll_opy_ = True
    bstack1lll1ll1l_opy_.set_property(bstack1l_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪ௛"), True)
def bstack11llll1l1l_opy_(config):
  bstack11ll1l1111_opy_ = bstack1l_opy_ (u"ࠬ࠭௜")
  app = config[bstack1l_opy_ (u"࠭ࡡࡱࡲࠪ௝")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1lllll1lll_opy_:
      if os.path.exists(app):
        bstack11ll1l1111_opy_ = bstack1llll1l11l_opy_(config, app)
      elif bstack111ll11ll1_opy_(app):
        bstack11ll1l1111_opy_ = app
      else:
        bstack11lll11ll1_opy_(bstack11l111111_opy_.format(app))
    else:
      if bstack111ll11ll1_opy_(app):
        bstack11ll1l1111_opy_ = app
      elif os.path.exists(app):
        bstack11ll1l1111_opy_ = bstack1llll1l11l_opy_(app)
      else:
        bstack11lll11ll1_opy_(bstack1lll1l1l1l_opy_)
  else:
    if len(app) > 2:
      bstack11lll11ll1_opy_(bstack1l1l1l11l_opy_)
    elif len(app) == 2:
      if bstack1l_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ௞") in app and bstack1l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫ௟") in app:
        if os.path.exists(app[bstack1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ௠")]):
          bstack11ll1l1111_opy_ = bstack1llll1l11l_opy_(config, app[bstack1l_opy_ (u"ࠪࡴࡦࡺࡨࠨ௡")], app[bstack1l_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧ௢")])
        else:
          bstack11lll11ll1_opy_(bstack11l111111_opy_.format(app))
      else:
        bstack11lll11ll1_opy_(bstack1l1l1l11l_opy_)
    else:
      for key in app:
        if key in bstack111l11111l_opy_:
          if key == bstack1l_opy_ (u"ࠬࡶࡡࡵࡪࠪ௣"):
            if os.path.exists(app[key]):
              bstack11ll1l1111_opy_ = bstack1llll1l11l_opy_(config, app[key])
            else:
              bstack11lll11ll1_opy_(bstack11l111111_opy_.format(app))
          else:
            bstack11ll1l1111_opy_ = app[key]
        else:
          bstack11lll11ll1_opy_(bstack11l11lll1_opy_)
  return bstack11ll1l1111_opy_
def bstack111ll11ll1_opy_(bstack11ll1l1111_opy_):
  import re
  bstack11lll11111_opy_ = re.compile(bstack1l_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮ࠩࠨ௤"))
  bstack1ll11ll1ll_opy_ = re.compile(bstack1l_opy_ (u"ࡲࠣࡠ࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯࠵࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬࠧࠦ௥"))
  if bstack1l_opy_ (u"ࠨࡤࡶ࠾࠴࠵ࠧ௦") in bstack11ll1l1111_opy_ or re.fullmatch(bstack11lll11111_opy_, bstack11ll1l1111_opy_) or re.fullmatch(bstack1ll11ll1ll_opy_, bstack11ll1l1111_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack111ll1l111_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack1llll1l11l_opy_(config, path, bstack111llll11_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1l_opy_ (u"ࠩࡵࡦࠬ௧")).read()).hexdigest()
  bstack111ll1lll_opy_ = bstack111ll1111_opy_(md5_hash)
  bstack11ll1l1111_opy_ = None
  if bstack111ll1lll_opy_:
    logger.info(bstack111l111lll_opy_.format(bstack111ll1lll_opy_, md5_hash))
    return bstack111ll1lll_opy_
  bstack1l1111lll_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack1l_opy_ (u"ࠪࡪ࡮ࡲࡥࠨ௨"): (os.path.basename(path), open(os.path.abspath(path), bstack1l_opy_ (u"ࠫࡷࡨࠧ௩")), bstack1l_opy_ (u"ࠬࡺࡥࡹࡶ࠲ࡴࡱࡧࡩ࡯ࠩ௪")),
      bstack1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ௫"): bstack111llll11_opy_
    }
  )
  response = requests.post(bstack1111l1l11_opy_, data=multipart_data,
                           headers={bstack1l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭௬"): multipart_data.content_type},
                           auth=(config[bstack1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ௭")], config[bstack1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ௮")]))
  try:
    res = json.loads(response.text)
    bstack11ll1l1111_opy_ = res[bstack1l_opy_ (u"ࠪࡥࡵࡶ࡟ࡶࡴ࡯ࠫ௯")]
    logger.info(bstack1lllllll11_opy_.format(bstack11ll1l1111_opy_))
    bstack1ll111l11_opy_(md5_hash, bstack11ll1l1111_opy_)
    cli.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡸࡴࡱࡵࡡࡥࡡࡤࡴࡵࠨ௰"), datetime.datetime.now() - bstack1l1111lll_opy_)
  except ValueError as err:
    bstack11lll11ll1_opy_(bstack11lll111l_opy_.format(str(err)))
  return bstack11ll1l1111_opy_
def bstack11ll1ll111_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1ll1l1ll11_opy_
  bstack1lll1ll11_opy_ = 1
  bstack1l11ll111_opy_ = 1
  if bstack1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ௱") in CONFIG:
    bstack1l11ll111_opy_ = CONFIG[bstack1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭௲")]
  else:
    bstack1l11ll111_opy_ = bstack11l1lll1ll_opy_(framework_name, args) or 1
  if bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ௳") in CONFIG:
    bstack1lll1ll11_opy_ = len(CONFIG[bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௴")])
  bstack1ll1l1ll11_opy_ = int(bstack1l11ll111_opy_) * int(bstack1lll1ll11_opy_)
def bstack11l1lll1ll_opy_(framework_name, args):
  if framework_name == bstack11l11l1lll_opy_ and args and bstack1l_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ௵") in args:
      bstack1ll1lllll_opy_ = args.index(bstack1l_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ௶"))
      return int(args[bstack1ll1lllll_opy_ + 1]) or 1
  return 1
def bstack111ll1111_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧ௷"))
    bstack1l1l11lll_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠬࢄࠧ௸")), bstack1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭௹"), bstack1l_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨ௺"))
    if os.path.exists(bstack1l1l11lll_opy_):
      try:
        bstack1ll1l1l1l1_opy_ = json.load(open(bstack1l1l11lll_opy_, bstack1l_opy_ (u"ࠨࡴࡥࠫ௻")))
        if md5_hash in bstack1ll1l1l1l1_opy_:
          bstack1l1lll111_opy_ = bstack1ll1l1l1l1_opy_[md5_hash]
          bstack1111111l1_opy_ = datetime.datetime.now()
          bstack11l1l11l1_opy_ = datetime.datetime.strptime(bstack1l1lll111_opy_[bstack1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ௼")], bstack1l_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧ௽"))
          if (bstack1111111l1_opy_ - bstack11l1l11l1_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack1l1lll111_opy_[bstack1l_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ௾")]):
            return None
          return bstack1l1lll111_opy_[bstack1l_opy_ (u"ࠬ࡯ࡤࠨ௿")]
      except Exception as e:
        logger.debug(bstack1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨࠡࡨ࡬ࡰࡪࡀࠠࡼࡿࠪఀ").format(str(e)))
    return None
  bstack1l1l11lll_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠧࡿࠩఁ")), bstack1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨం"), bstack1l_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪః"))
  lock_file = bstack1l1l11lll_opy_ + bstack1l_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩఄ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1l1l11lll_opy_):
        with open(bstack1l1l11lll_opy_, bstack1l_opy_ (u"ࠫࡷ࠭అ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll1l1l1l1_opy_ = json.loads(content)
            if md5_hash in bstack1ll1l1l1l1_opy_:
              bstack1l1lll111_opy_ = bstack1ll1l1l1l1_opy_[md5_hash]
              bstack1111111l1_opy_ = datetime.datetime.now()
              bstack11l1l11l1_opy_ = datetime.datetime.strptime(bstack1l1lll111_opy_[bstack1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨఆ")], bstack1l_opy_ (u"࠭ࠥࡥ࠱ࠨࡱ࠴࡙ࠫࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪఇ"))
              if (bstack1111111l1_opy_ - bstack11l1l11l1_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack1l1lll111_opy_[bstack1l_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬఈ")]):
                return None
              return bstack1l1lll111_opy_[bstack1l_opy_ (u"ࠨ࡫ࡧࠫఉ")]
      return None
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡹ࡬ࡸ࡭ࠦࡦࡪ࡮ࡨࠤࡱࡵࡣ࡬࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡐࡈ࠺ࠦࡨࡢࡵ࡫࠾ࠥࢁࡽࠨఊ").format(str(e)))
    return None
def bstack1ll111l11_opy_(md5_hash, bstack11ll1l1111_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭ఋ"))
    bstack1l11llll1l_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠫࢃ࠭ఌ")), bstack1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ఍"))
    if not os.path.exists(bstack1l11llll1l_opy_):
      os.makedirs(bstack1l11llll1l_opy_)
    bstack1l1l11lll_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"࠭ࡾࠨఎ")), bstack1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧఏ"), bstack1l_opy_ (u"ࠨࡣࡳࡴ࡚ࡶ࡬ࡰࡣࡧࡑࡉ࠻ࡈࡢࡵ࡫࠲࡯ࡹ࡯࡯ࠩఐ"))
    bstack1ll1l1l111_opy_ = {
      bstack1l_opy_ (u"ࠩ࡬ࡨࠬ఑"): bstack11ll1l1111_opy_,
      bstack1l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ఒ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨఓ")),
      bstack1l_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪఔ"): str(__version__)
    }
    try:
      bstack1ll1l1l1l1_opy_ = {}
      if os.path.exists(bstack1l1l11lll_opy_):
        bstack1ll1l1l1l1_opy_ = json.load(open(bstack1l1l11lll_opy_, bstack1l_opy_ (u"࠭ࡲࡣࠩక")))
      bstack1ll1l1l1l1_opy_[md5_hash] = bstack1ll1l1l111_opy_
      with open(bstack1l1l11lll_opy_, bstack1l_opy_ (u"ࠢࡸ࠭ࠥఖ")) as outfile:
        json.dump(bstack1ll1l1l1l1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡶࡲࡧࡥࡹ࡯࡮ࡨࠢࡐࡈ࠺ࠦࡨࡢࡵ࡫ࠤ࡫࡯࡬ࡦ࠼ࠣࡿࢂ࠭గ").format(str(e)))
    return
  bstack1l11llll1l_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠩࢁࠫఘ")), bstack1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪఙ"))
  if not os.path.exists(bstack1l11llll1l_opy_):
    os.makedirs(bstack1l11llll1l_opy_)
  bstack1l1l11lll_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠫࢃ࠭చ")), bstack1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬఛ"), bstack1l_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧజ"))
  lock_file = bstack1l1l11lll_opy_ + bstack1l_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ࠭ఝ")
  bstack1ll1l1l111_opy_ = {
    bstack1l_opy_ (u"ࠨ࡫ࡧࠫఞ"): bstack11ll1l1111_opy_,
    bstack1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬట"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧఠ")),
    bstack1l_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩడ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1ll1l1l1l1_opy_ = {}
      if os.path.exists(bstack1l1l11lll_opy_):
        with open(bstack1l1l11lll_opy_, bstack1l_opy_ (u"ࠬࡸࠧఢ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll1l1l1l1_opy_ = json.loads(content)
      bstack1ll1l1l1l1_opy_[md5_hash] = bstack1ll1l1l111_opy_
      with open(bstack1l1l11lll_opy_, bstack1l_opy_ (u"ࠨࡷࠣణ")) as outfile:
        json.dump(bstack1ll1l1l1l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡷࡪࡶ࡫ࠤ࡫࡯࡬ࡦࠢ࡯ࡳࡨࡱࡩ࡯ࡩࠣࡪࡴࡸࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩࠢࡸࡴࡩࡧࡴࡦ࠼ࠣࡿࢂ࠭త").format(str(e)))
def bstack1l1l1lll1_opy_(self):
  return
def bstack111llll11l_opy_(self):
  return
def bstack11ll111lll_opy_():
  global bstack1ll1l11ll1_opy_
  bstack1ll1l11ll1_opy_ = True
@measure(event_name=EVENTS.bstack1l1ll1l111_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack111l111111_opy_(self):
  global bstack11l1lll1l_opy_
  global bstack1lll1l11l1_opy_
  global bstack111l11ll11_opy_
  try:
    if bstack1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨథ") in bstack11l1lll1l_opy_ and self.session_id != None and bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ద"), bstack1l_opy_ (u"ࠪࠫధ")) != bstack1l_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬన"):
      bstack111l1111ll_opy_ = bstack1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ఩") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ప")
      if bstack111l1111ll_opy_ == bstack1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧఫ"):
        bstack1llll1l1l1_opy_(logger)
      if self != None:
        bstack11111ll111_opy_(self, bstack111l1111ll_opy_, bstack1l_opy_ (u"ࠨ࠮ࠣࠫబ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1l_opy_ (u"ࠩࠪభ")
    if bstack1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪమ") in bstack11l1lll1l_opy_ and getattr(threading.current_thread(), bstack1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪయ"), None):
      bstack111111l1_opy_.bstack1llllll1l_opy_(self, bstack111l1lll1_opy_, logger, wait=True)
    if bstack1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬర") in bstack11l1lll1l_opy_:
      if not threading.currentThread().behave_test_status:
        bstack11111ll111_opy_(self, bstack1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨఱ"))
      bstack1111l11ll_opy_.bstack1ll111l111_opy_(self)
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡳࡵࡣࡷࡹࡸࡀࠠࠣల") + str(e))
  bstack111l11ll11_opy_(self)
  self.session_id = None
def bstack11l1111ll_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1lll11lll1_opy_
    global bstack11l1lll1l_opy_
    command_executor = kwargs.get(bstack1l_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠫళ"), bstack1l_opy_ (u"ࠩࠪఴ"))
    bstack1111l1l111_opy_ = False
    if type(command_executor) == str and bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭వ") in command_executor:
      bstack1111l1l111_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧశ") in str(getattr(command_executor, bstack1l_opy_ (u"ࠬࡥࡵࡳ࡮ࠪష"), bstack1l_opy_ (u"࠭ࠧస"))):
      bstack1111l1l111_opy_ = True
    else:
      kwargs = bstack11111ll1_opy_.bstack11111ll1ll_opy_(bstack11111llll_opy_=kwargs, config=CONFIG)
      return bstack1ll1ll1ll1_opy_(self, *args, **kwargs)
    if bstack1111l1l111_opy_:
      bstack1111llll11_opy_ = bstack11l11ll111_opy_.bstack11l1llll11_opy_(CONFIG, bstack11l1lll1l_opy_)
      if kwargs.get(bstack1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨహ")):
        kwargs[bstack1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩ఺")] = bstack1lll11lll1_opy_(kwargs[bstack1l_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪ఻")], bstack11l1lll1l_opy_, CONFIG, bstack1111llll11_opy_)
      elif kwargs.get(bstack1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ఼ࠪ")):
        kwargs[bstack1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫఽ")] = bstack1lll11lll1_opy_(kwargs[bstack1l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬా")], bstack11l1lll1l_opy_, CONFIG, bstack1111llll11_opy_)
  except Exception as e:
    logger.error(bstack1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡦࡰࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡨࡧࡰࡴ࠼ࠣࡿࢂࠨి").format(str(e)))
  return bstack1ll1ll1ll1_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack111ll111ll_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack1ll1llllll_opy_(self, command_executor=bstack1l_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯࠲࠴࠺࠲࠵࠴࠰࠯࠳࠽࠸࠹࠺࠴ࠣీ"), *args, **kwargs):
  global bstack1lll1l11l1_opy_
  global bstack1ll1ll1l11_opy_
  bstack111l1ll1l1_opy_ = bstack11l1111ll_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack11lll1l1_opy_.on():
    return bstack111l1ll1l1_opy_
  try:
    logger.debug(bstack1l_opy_ (u"ࠨࡅࡲࡱࡲࡧ࡮ࡥࠢࡈࡼࡪࡩࡵࡵࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡨࡤࡰࡸ࡫ࠠ࠮ࠢࡾࢁࠬు").format(str(command_executor)))
    logger.debug(bstack1l_opy_ (u"ࠩࡋࡹࡧࠦࡕࡓࡎࠣ࡭ࡸࠦ࠭ࠡࡽࢀࠫూ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ృ") in command_executor._url:
      bstack1lll1ll1l_opy_.set_property(bstack1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬౄ"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨ౅") in command_executor):
    bstack1lll1ll1l_opy_.set_property(bstack1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧె"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1ll111111_opy_ = getattr(threading.current_thread(), bstack1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡔࡦࡵࡷࡑࡪࡺࡡࠨే"), None)
  bstack1l1111ll1l_opy_ = {}
  if self.capabilities is not None:
    bstack1l1111ll1l_opy_[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧై")] = self.capabilities.get(bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ౉"))
    bstack1l1111ll1l_opy_[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬొ")] = self.capabilities.get(bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬో"))
    bstack1l1111ll1l_opy_[bstack1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡤࡵࡰࡵ࡫ࡲࡲࡸ࠭ౌ")] = self.capabilities.get(bstack1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶ్ࠫ"))
  if CONFIG.get(bstack1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ౎"), False) and bstack11111ll1_opy_.bstack1111ll111l_opy_(bstack1l1111ll1l_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ౏") in bstack11l1lll1l_opy_ or bstack1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ౐") in bstack11l1lll1l_opy_:
    bstack1ll1lll1_opy_.bstack11111l1l1l_opy_(self)
  if bstack1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ౑") in bstack11l1lll1l_opy_ and bstack1ll111111_opy_ and bstack1ll111111_opy_.get(bstack1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ౒"), bstack1l_opy_ (u"ࠬ࠭౓")) == bstack1l_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧ౔"):
    bstack1ll1lll1_opy_.bstack11111l1l1l_opy_(self)
  bstack1lll1l11l1_opy_ = self.session_id
  with bstack11l1l1111l_opy_:
    bstack1ll1ll1l11_opy_.append(self)
  return bstack111l1ll1l1_opy_
def bstack1lllll11l1_opy_(args):
  return bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲࠨౕ") in str(args)
def bstack1l1l1lllll_opy_(self, driver_command, *args, **kwargs):
  global bstack11ll1l1l11_opy_
  global bstack1l1lllll11_opy_
  bstack1l1111lll1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸౖࠬ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ౗"), None)
  bstack11l11l11l1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪౘ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack1l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ౙ"), None)
  bstack1l11l1111_opy_ = getattr(self, bstack1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬౚ"), None) != None and getattr(self, bstack1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭౛"), None) == True
  if not bstack1l1lllll11_opy_ and bstack1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ౜") in CONFIG and CONFIG[bstack1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨౝ")] == True and bstack1ll1l1llll_opy_.bstack1ll11lll11_opy_(driver_command) and (bstack1l11l1111_opy_ or bstack1l1111lll1_opy_ or bstack11l11l11l1_opy_) and not bstack1lllll11l1_opy_(args):
    try:
      bstack1l1lllll11_opy_ = True
      logger.debug(bstack1l_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤ࡫ࡵࡲࠡࡽࢀࠫ౞").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡦࡴࡩࡳࡷࡳࠠࡴࡥࡤࡲࠥࢁࡽࠨ౟").format(str(err)))
    bstack1l1lllll11_opy_ = False
  response = bstack11ll1l1l11_opy_(self, driver_command, *args, **kwargs)
  if (bstack1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪౠ") in str(bstack11l1lll1l_opy_).lower() or bstack1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬౡ") in str(bstack11l1lll1l_opy_).lower()) and bstack11lll1l1_opy_.on():
    try:
      if driver_command == bstack1l_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪౢ"):
        bstack1ll1lll1_opy_.bstack1l11ll11l1_opy_({
            bstack1l_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭ౣ"): response[bstack1l_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧ౤")],
            bstack1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ౥"): bstack1ll1lll1_opy_.current_test_uuid() if bstack1ll1lll1_opy_.current_test_uuid() else bstack11lll1l1_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1llllllll1_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack1ll11llll1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1lll1l11l1_opy_
  global bstack1l11l11l1_opy_
  global bstack11ll1ll11l_opy_
  global bstack11lll1ll1_opy_
  global bstack111l1l1l1_opy_
  global bstack11l1lll1l_opy_
  global bstack1ll1ll1ll1_opy_
  global bstack1ll1ll1l11_opy_
  global bstack11ll1lllll_opy_
  global bstack111l1lll1_opy_
  if os.getenv(bstack1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ౦")) is not None and bstack11111ll1_opy_.bstack1llll1ll1l_opy_(CONFIG) is None:
    CONFIG[bstack1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ౧")] = True
  CONFIG[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ౨")] = str(bstack11l1lll1l_opy_) + str(__version__)
  bstack11lll1ll11_opy_ = os.environ[bstack1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ౩")]
  bstack1111llll11_opy_ = bstack11l11ll111_opy_.bstack11l1llll11_opy_(CONFIG, bstack11l1lll1l_opy_)
  CONFIG[bstack1l_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ౪")] = bstack11lll1ll11_opy_
  CONFIG[bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ౫")] = bstack1111llll11_opy_
  if CONFIG.get(bstack1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ౬"),bstack1l_opy_ (u"ࠪࠫ౭")) and bstack1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ౮") in bstack11l1lll1l_opy_:
    CONFIG[bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ౯")].pop(bstack1l_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ౰"), None)
    CONFIG[bstack1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ౱")].pop(bstack1l_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭౲"), None)
  command_executor = bstack11l1l11ll1_opy_()
  logger.debug(bstack1llll111l1_opy_.format(command_executor))
  proxy = bstack1lll11l1ll_opy_(CONFIG, proxy)
  bstack11l111l1l_opy_ = 0 if bstack1l11l11l1_opy_ < 0 else bstack1l11l11l1_opy_
  try:
    if bstack11lll1ll1_opy_ is True:
      bstack11l111l1l_opy_ = int(multiprocessing.current_process().name)
    elif bstack111l1l1l1_opy_ is True:
      bstack11l111l1l_opy_ = int(threading.current_thread().name)
  except:
    bstack11l111l1l_opy_ = 0
  bstack11l1l1lll_opy_ = bstack11lll1111_opy_(CONFIG, bstack11l111l1l_opy_)
  logger.debug(bstack1ll11l1l1_opy_.format(str(bstack11l1l1lll_opy_)))
  if bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭౳") in CONFIG and bstack1l11l1ll1l_opy_(CONFIG[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ౴")]):
    bstack1l11llllll_opy_(bstack11l1l1lll_opy_)
  if bstack11111ll1_opy_.bstack111ll11lll_opy_(CONFIG, bstack11l111l1l_opy_) and bstack11111ll1_opy_.bstack1l1l11ll1l_opy_(bstack11l1l1lll_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack11111ll1_opy_.set_capabilities(bstack11l1l1lll_opy_, CONFIG)
  if desired_capabilities:
    bstack11lll1llll_opy_ = bstack11111lll1l_opy_(desired_capabilities)
    bstack11lll1llll_opy_[bstack1l_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ౵")] = bstack1l1111llll_opy_(CONFIG)
    bstack11lllll1l1_opy_ = bstack11lll1111_opy_(bstack11lll1llll_opy_)
    if bstack11lllll1l1_opy_:
      bstack11l1l1lll_opy_ = update(bstack11lllll1l1_opy_, bstack11l1l1lll_opy_)
    desired_capabilities = None
  if options:
    bstack1l11l1l1ll_opy_(options, bstack11l1l1lll_opy_)
  if not options:
    options = bstack11111l1l1_opy_(bstack11l1l1lll_opy_)
  bstack111l1lll1_opy_ = CONFIG.get(bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ౶"))[bstack11l111l1l_opy_]
  if proxy and bstack1lll1lll1l_opy_() >= version.parse(bstack1l_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭౷")):
    options.proxy(proxy)
  if options and bstack1lll1lll1l_opy_() >= version.parse(bstack1l_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭౸")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1lll1lll1l_opy_() < version.parse(bstack1l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ౹")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack11l1l1lll_opy_)
  logger.info(bstack1l1l1ll111_opy_)
  bstack1lll11ll11_opy_.end(EVENTS.bstack111l11l1l1_opy_.value, EVENTS.bstack111l11l1l1_opy_.value + bstack1l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ౺"), EVENTS.bstack111l11l1l1_opy_.value + bstack1l_opy_ (u"ࠥ࠾ࡪࡴࡤࠣ౻"), status=True, failure=None, test_name=bstack11ll1ll11l_opy_)
  if bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡶࡲࡰࡨ࡬ࡰࡪ࠭౼") in kwargs:
    del kwargs[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡰࡳࡱࡩ࡭ࡱ࡫ࠧ౽")]
  try:
    if bstack1lll1lll1l_opy_() >= version.parse(bstack1l_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭౾")):
      bstack1ll1ll1ll1_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack1lll1lll1l_opy_() >= version.parse(bstack1l_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭౿")):
      bstack1ll1ll1ll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1lll1lll1l_opy_() >= version.parse(bstack1l_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨಀ")):
      bstack1ll1ll1ll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1ll1ll1ll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack111l11l1ll_opy_:
    logger.error(bstack1l1111ll11_opy_.format(bstack1l_opy_ (u"ࠩࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠨಁ"), str(bstack111l11l1ll_opy_)))
    raise bstack111l11l1ll_opy_
  if bstack11111ll1_opy_.bstack111ll11lll_opy_(CONFIG, bstack11l111l1l_opy_) and bstack11111ll1_opy_.bstack1l1l11ll1l_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬಂ")][bstack1l_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪಃ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack11111ll1_opy_.set_capabilities(bstack11l1l1lll_opy_, CONFIG)
  try:
    bstack111111lll_opy_ = bstack1l_opy_ (u"ࠬ࠭಄")
    if bstack1lll1lll1l_opy_() >= version.parse(bstack1l_opy_ (u"࠭࠴࠯࠲࠱࠴ࡧ࠷ࠧಅ")):
      if self.caps is not None:
        bstack111111lll_opy_ = self.caps.get(bstack1l_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢಆ"))
    else:
      if self.capabilities is not None:
        bstack111111lll_opy_ = self.capabilities.get(bstack1l_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣಇ"))
    if bstack111111lll_opy_:
      bstack1111l11l11_opy_(bstack111111lll_opy_)
      if bstack1lll1lll1l_opy_() <= version.parse(bstack1l_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩಈ")):
        self.command_executor._url = bstack1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦಉ") + bstack11l1ll1ll1_opy_ + bstack1l_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣಊ")
      else:
        self.command_executor._url = bstack1l_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢಋ") + bstack111111lll_opy_ + bstack1l_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢಌ")
      logger.debug(bstack111lll1111_opy_.format(bstack111111lll_opy_))
    else:
      logger.debug(bstack1l11111ll_opy_.format(bstack1l_opy_ (u"ࠢࡐࡲࡷ࡭ࡲࡧ࡬ࠡࡊࡸࡦࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣ಍")))
  except Exception as e:
    logger.debug(bstack1l11111ll_opy_.format(e))
  if bstack1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧಎ") in bstack11l1lll1l_opy_:
    bstack1l11l1l1l_opy_(bstack1l11l11l1_opy_, bstack11ll1lllll_opy_)
  bstack1lll1l11l1_opy_ = self.session_id
  if bstack1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩಏ") in bstack11l1lll1l_opy_ or bstack1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪಐ") in bstack11l1lll1l_opy_ or bstack1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ಑") in bstack11l1lll1l_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1ll111111_opy_ = getattr(threading.current_thread(), bstack1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭ಒ"), None)
  if bstack1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ಓ") in bstack11l1lll1l_opy_ or bstack1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ಔ") in bstack11l1lll1l_opy_:
    bstack1ll1lll1_opy_.bstack11111l1l1l_opy_(self)
  if bstack1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨಕ") in bstack11l1lll1l_opy_ and bstack1ll111111_opy_ and bstack1ll111111_opy_.get(bstack1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩಖ"), bstack1l_opy_ (u"ࠪࠫಗ")) == bstack1l_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬಘ"):
    bstack1ll1lll1_opy_.bstack11111l1l1l_opy_(self)
  with bstack11l1l1111l_opy_:
    bstack1ll1ll1l11_opy_.append(self)
  if bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಙ") in CONFIG and bstack1l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫಚ") in CONFIG[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಛ")][bstack11l111l1l_opy_]:
    bstack11ll1ll11l_opy_ = CONFIG[bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಜ")][bstack11l111l1l_opy_][bstack1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧಝ")]
  logger.debug(bstack1l11l11111_opy_.format(bstack1lll1l11l1_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1l1l1ll1l1_opy_
    def bstack111l1111l1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1lll1l111l_opy_
      if(bstack1l_opy_ (u"ࠥ࡭ࡳࡪࡥࡹ࠰࡭ࡷࠧಞ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠫࢃ࠭ಟ")), bstack1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬಠ"), bstack1l_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨಡ")), bstack1l_opy_ (u"ࠧࡸࠩಢ")) as fp:
          fp.write(bstack1l_opy_ (u"ࠣࠤಣ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1l_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦತ")))):
          with open(args[1], bstack1l_opy_ (u"ࠪࡶࠬಥ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1l_opy_ (u"ࠫࡦࡹࡹ࡯ࡥࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࡥ࡮ࡦࡹࡓࡥ࡬࡫ࠨࡤࡱࡱࡸࡪࡾࡴ࠭ࠢࡳࡥ࡬࡫ࠠ࠾ࠢࡹࡳ࡮ࡪࠠ࠱ࠫࠪದ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1l111l111l_opy_)
            if bstack1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩಧ") in CONFIG and str(CONFIG[bstack1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪನ")]).lower() != bstack1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭಩"):
                bstack1l11lll11_opy_ = bstack1l1l1ll1l1_opy_()
                bstack11111ll11l_opy_ = bstack1l_opy_ (u"ࠨࠩࠪࠎ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠊࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡰࡢࡶ࡫ࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳࡞࠽ࠍࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠴ࡡࡀࠐࡣࡰࡰࡶࡸࠥࡶ࡟ࡪࡰࡧࡩࡽࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠴ࡠ࠿ࠏࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡹ࡬ࡪࡥࡨࠬ࠵࠲ࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࠬ࠿ࠏࡩ࡯࡯ࡵࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬ࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ࠭ࡀࠐࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁࡻࠋࠢࠣࡰࡪࡺࠠࡤࡣࡳࡷࡀࠐࠠࠡࡶࡵࡽࠥࢁࡻࠋࠢࠣࠤࠥࡩࡡࡱࡵࠣࡁࠥࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠩ࠼ࠌࠣࠤࢂࢃࠠࡤࡣࡷࡧ࡭ࠦࠨࡦࡺࠬࠤࢀࢁࠊࠡࠢࠣࠤࡨࡵ࡮ࡴࡱ࡯ࡩ࠳࡫ࡲࡳࡱࡵࠬࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࡀࠢ࠭ࠢࡨࡼ࠮ࡁࠊࠡࠢࢀࢁࠏࠦࠠࡳࡧࡷࡹࡷࡴࠠࡢࡹࡤ࡭ࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴ࡣࡰࡰࡱࡩࡨࡺࠨࡼࡽࠍࠤࠥࠦࠠࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷ࠾ࠥ࠭ࡻࡤࡦࡳ࡙ࡷࡲࡽࠨࠢ࠮ࠤࡪࡴࡣࡰࡦࡨ࡙ࡗࡏࡃࡰ࡯ࡳࡳࡳ࡫࡮ࡵࠪࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡧࡦࡶࡳࠪࠫ࠯ࠎࠥࠦࠠࠡ࠰࠱࠲ࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶࠎࠥࠦࡽࡾࠫ࠾ࠎࢂࢃ࠻ࠋ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࠎࠬ࠭ࠧಪ").format(bstack1l11lll11_opy_=bstack1l11lll11_opy_)
            lines.insert(1, bstack11111ll11l_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1l_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦಫ")), bstack1l_opy_ (u"ࠪࡻࠬಬ")) as bstack1llll1111l_opy_:
              bstack1llll1111l_opy_.writelines(lines)
        CONFIG[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ಭ")] = str(bstack11l1lll1l_opy_) + str(__version__)
        bstack11lll1ll11_opy_ = os.environ[bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪಮ")]
        bstack1111llll11_opy_ = bstack11l11ll111_opy_.bstack11l1llll11_opy_(CONFIG, bstack11l1lll1l_opy_)
        CONFIG[bstack1l_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩಯ")] = bstack11lll1ll11_opy_
        CONFIG[bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩರ")] = bstack1111llll11_opy_
        bstack11l111l1l_opy_ = 0 if bstack1l11l11l1_opy_ < 0 else bstack1l11l11l1_opy_
        try:
          if bstack11lll1ll1_opy_ is True:
            bstack11l111l1l_opy_ = int(multiprocessing.current_process().name)
          elif bstack111l1l1l1_opy_ is True:
            bstack11l111l1l_opy_ = int(threading.current_thread().name)
        except:
          bstack11l111l1l_opy_ = 0
        CONFIG[bstack1l_opy_ (u"ࠣࡷࡶࡩ࡜࠹ࡃࠣಱ")] = False
        CONFIG[bstack1l_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣಲ")] = True
        bstack11l1l1lll_opy_ = bstack11lll1111_opy_(CONFIG, bstack11l111l1l_opy_)
        logger.debug(bstack1ll11l1l1_opy_.format(str(bstack11l1l1lll_opy_)))
        if CONFIG.get(bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧಳ")):
          bstack1l11llllll_opy_(bstack11l1l1lll_opy_)
        if bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಴") in CONFIG and bstack1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪವ") in CONFIG[bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಶ")][bstack11l111l1l_opy_]:
          bstack11ll1ll11l_opy_ = CONFIG[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಷ")][bstack11l111l1l_opy_][bstack1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ಸ")]
        args.append(os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠩࢁࠫಹ")), bstack1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ಺"), bstack1l_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭಻")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack11l1l1lll_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1l_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹ಼ࠢ"))
      bstack1lll1l111l_opy_ = True
      return bstack1ll11111l_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack11l1111ll1_opy_(self,
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
    global bstack1l11l11l1_opy_
    global bstack11ll1ll11l_opy_
    global bstack11lll1ll1_opy_
    global bstack111l1l1l1_opy_
    global bstack11l1lll1l_opy_
    CONFIG[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨಽ")] = str(bstack11l1lll1l_opy_) + str(__version__)
    bstack11lll1ll11_opy_ = os.environ[bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬಾ")]
    bstack1111llll11_opy_ = bstack11l11ll111_opy_.bstack11l1llll11_opy_(CONFIG, bstack11l1lll1l_opy_)
    CONFIG[bstack1l_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫಿ")] = bstack11lll1ll11_opy_
    CONFIG[bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫೀ")] = bstack1111llll11_opy_
    bstack11l111l1l_opy_ = 0 if bstack1l11l11l1_opy_ < 0 else bstack1l11l11l1_opy_
    try:
      if bstack11lll1ll1_opy_ is True:
        bstack11l111l1l_opy_ = int(multiprocessing.current_process().name)
      elif bstack111l1l1l1_opy_ is True:
        bstack11l111l1l_opy_ = int(threading.current_thread().name)
    except:
      bstack11l111l1l_opy_ = 0
    CONFIG[bstack1l_opy_ (u"ࠥ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤು")] = True
    bstack11l1l1lll_opy_ = bstack11lll1111_opy_(CONFIG, bstack11l111l1l_opy_)
    logger.debug(bstack1ll11l1l1_opy_.format(str(bstack11l1l1lll_opy_)))
    if CONFIG.get(bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨೂ")):
      bstack1l11llllll_opy_(bstack11l1l1lll_opy_)
    if bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨೃ") in CONFIG and bstack1l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫೄ") in CONFIG[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ೅")][bstack11l111l1l_opy_]:
      bstack11ll1ll11l_opy_ = CONFIG[bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫೆ")][bstack11l111l1l_opy_][bstack1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧೇ")]
    import urllib
    import json
    if bstack1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧೈ") in CONFIG and str(CONFIG[bstack1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ೉")]).lower() != bstack1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫೊ"):
        bstack1l11l1l11_opy_ = bstack1l1l1ll1l1_opy_()
        bstack1l11lll11_opy_ = bstack1l11l1l11_opy_ + urllib.parse.quote(json.dumps(bstack11l1l1lll_opy_))
    else:
        bstack1l11lll11_opy_ = bstack1l_opy_ (u"࠭ࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠨೋ") + urllib.parse.quote(json.dumps(bstack11l1l1lll_opy_))
    browser = self.connect(bstack1l11lll11_opy_)
    return browser
except Exception as e:
    pass
def bstack1l111l1lll_opy_():
    global bstack1lll1l111l_opy_
    global bstack11l1lll1l_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack11lllll111_opy_
        global bstack1lll1ll1l_opy_
        if not bstack1lll1ll1l1_opy_:
          global bstack1ll1l111l1_opy_
          if not bstack1ll1l111l1_opy_:
            from bstack_utils.helper import bstack111lll111_opy_, bstack1ll11lll1l_opy_, bstack11l1l1llll_opy_
            bstack1ll1l111l1_opy_ = bstack111lll111_opy_()
            bstack1ll11lll1l_opy_(bstack11l1lll1l_opy_)
            bstack1111llll11_opy_ = bstack11l11ll111_opy_.bstack11l1llll11_opy_(CONFIG, bstack11l1lll1l_opy_)
            bstack1lll1ll1l_opy_.set_property(bstack1l_opy_ (u"ࠢࡑࡎࡄ࡝࡜ࡘࡉࡈࡊࡗࡣࡕࡘࡏࡅࡗࡆࡘࡤࡓࡁࡑࠤೌ"), bstack1111llll11_opy_)
          BrowserType.connect = bstack11lllll111_opy_
          return
        BrowserType.launch = bstack11l1111ll1_opy_
        bstack1lll1l111l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack111l1111l1_opy_
      bstack1lll1l111l_opy_ = True
    except Exception as e:
      pass
def bstack1lll11llll_opy_(context, bstack1l111l1l11_opy_):
  try:
    context.page.evaluate(bstack1l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ್"), bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭೎")+ json.dumps(bstack1l111l1l11_opy_) + bstack1l_opy_ (u"ࠥࢁࢂࠨ೏"))
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾ࠼ࠣࡿࢂࠨ೐").format(str(e), traceback.format_exc()))
def bstack1l111llll1_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨ೑"), bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ೒") + json.dumps(message) + bstack1l_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪ೓") + json.dumps(level) + bstack1l_opy_ (u"ࠨࡿࢀࠫ೔"))
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁ࠿ࠦࡻࡾࠤೕ").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1lll1ll111_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack1lllll1ll1_opy_(self, url):
  global bstack1ll1l1l1ll_opy_
  try:
    bstack1l1lll1111_opy_(url)
  except Exception as err:
    logger.debug(bstack1lll1111l_opy_.format(str(err)))
  try:
    bstack1ll1l1l1ll_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1l111111ll_opy_):
        bstack1l1lll1111_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1lll1111l_opy_.format(str(err)))
    raise e
def bstack111ll1ll11_opy_(self):
  global bstack11l11111l_opy_
  bstack11l11111l_opy_ = self
  return
def bstack1l111l1l1_opy_(self):
  global bstack1ll111l1l1_opy_
  bstack1ll111l1l1_opy_ = self
  return
def bstack11l11lllll_opy_(test_name, bstack1l11ll11l_opy_):
  global CONFIG
  if percy.bstack111l11ll1l_opy_() == bstack1l_opy_ (u"ࠥࡸࡷࡻࡥࠣೖ"):
    bstack111l1l111_opy_ = os.path.relpath(bstack1l11ll11l_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack111l1l111_opy_)
    bstack1l1ll1ll1_opy_ = suite_name + bstack1l_opy_ (u"ࠦ࠲ࠨ೗") + test_name
    threading.current_thread().percySessionName = bstack1l1ll1ll1_opy_
def bstack1l1l111ll1_opy_(self, test, *args, **kwargs):
  global bstack11l1l11ll_opy_
  test_name = None
  bstack1l11ll11l_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1l11ll11l_opy_ = str(test.source)
  bstack11l11lllll_opy_(test_name, bstack1l11ll11l_opy_)
  bstack11l1l11ll_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1ll1l11lll_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack1lll1l1l11_opy_(driver, bstack1l1ll1ll1_opy_):
  if not bstack1l1lll1ll1_opy_ and bstack1l1ll1ll1_opy_:
      bstack1ll1l11l1_opy_ = {
          bstack1l_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬ೘"): bstack1l_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ೙"),
          bstack1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ೚"): {
              bstack1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭೛"): bstack1l1ll1ll1_opy_
          }
      }
      bstack11111l111_opy_ = bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧ೜").format(json.dumps(bstack1ll1l11l1_opy_))
      driver.execute_script(bstack11111l111_opy_)
  if bstack1ll11111ll_opy_:
      bstack111ll1lll1_opy_ = {
          bstack1l_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪೝ"): bstack1l_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ೞ"),
          bstack1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ೟"): {
              bstack1l_opy_ (u"࠭ࡤࡢࡶࡤࠫೠ"): bstack1l1ll1ll1_opy_ + bstack1l_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩೡ"),
              bstack1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧೢ"): bstack1l_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧೣ")
          }
      }
      if bstack1ll11111ll_opy_.status == bstack1l_opy_ (u"ࠪࡔࡆ࡙ࡓࠨ೤"):
          bstack1111l111l_opy_ = bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ೥").format(json.dumps(bstack111ll1lll1_opy_))
          driver.execute_script(bstack1111l111l_opy_)
          bstack11111ll111_opy_(driver, bstack1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ೦"))
      elif bstack1ll11111ll_opy_.status == bstack1l_opy_ (u"࠭ࡆࡂࡋࡏࠫ೧"):
          reason = bstack1l_opy_ (u"ࠢࠣ೨")
          bstack1l11111l1l_opy_ = bstack1l1ll1ll1_opy_ + bstack1l_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠩ೩")
          if bstack1ll11111ll_opy_.message:
              reason = str(bstack1ll11111ll_opy_.message)
              bstack1l11111l1l_opy_ = bstack1l11111l1l_opy_ + bstack1l_opy_ (u"ࠩࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸ࠺ࠡࠩ೪") + reason
          bstack111ll1lll1_opy_[bstack1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭೫")] = {
              bstack1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ೬"): bstack1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ೭"),
              bstack1l_opy_ (u"࠭ࡤࡢࡶࡤࠫ೮"): bstack1l11111l1l_opy_
          }
          bstack1111l111l_opy_ = bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ೯").format(json.dumps(bstack111ll1lll1_opy_))
          driver.execute_script(bstack1111l111l_opy_)
          bstack11111ll111_opy_(driver, bstack1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ೰"), reason)
          bstack1l1l1l111_opy_(reason, str(bstack1ll11111ll_opy_), str(bstack1l11l11l1_opy_), logger)
@measure(event_name=EVENTS.bstack1l1l11l1ll_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack1ll1111l1_opy_(driver, test):
  if percy.bstack111l11ll1l_opy_() == bstack1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢೱ") and percy.bstack11ll1l1ll_opy_() == bstack1l_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧೲ"):
      bstack11lllllll_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧೳ"), None)
      bstack111ll1ll1l_opy_(driver, bstack11lllllll_opy_, test)
  if (bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ೴"), None) and
      bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ೵"), None)) or (
      bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ೶"), None) and
      bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ೷"), None)):
      logger.info(bstack1l_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠠࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡵࡻࡦࡿ࠮ࠡࠤ೸"))
      bstack11111ll1_opy_.bstack111l1ll1_opy_(driver, name=test.name, path=test.source)
def bstack111ll1l1l1_opy_(test, bstack1l1ll1ll1_opy_):
    try:
      bstack1l1111lll_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ೹")] = bstack1l1ll1ll1_opy_
      if bstack1ll11111ll_opy_:
        if bstack1ll11111ll_opy_.status == bstack1l_opy_ (u"ࠫࡕࡇࡓࡔࠩ೺"):
          data[bstack1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ೻")] = bstack1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭೼")
        elif bstack1ll11111ll_opy_.status == bstack1l_opy_ (u"ࠧࡇࡃࡌࡐࠬ೽"):
          data[bstack1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ೾")] = bstack1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ೿")
          if bstack1ll11111ll_opy_.message:
            data[bstack1l_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪഀ")] = str(bstack1ll11111ll_opy_.message)
      user = CONFIG[bstack1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ഁ")]
      key = CONFIG[bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨം")]
      host = bstack1l111ll1ll_opy_(cli.config, [bstack1l_opy_ (u"ࠨࡡࡱ࡫ࡶࠦഃ"), bstack1l_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࠤഄ"), bstack1l_opy_ (u"ࠣࡣࡳ࡭ࠧഅ")], bstack1l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠥആ"))
      url = bstack1l_opy_ (u"ࠪࡿࢂ࠵ࡡࡶࡶࡲࡱࡦࡺࡥ࠰ࡵࡨࡷࡸ࡯࡯࡯ࡵ࠲ࡿࢂ࠴ࡪࡴࡱࡱࠫഇ").format(host, bstack1lll1l11l1_opy_)
      headers = {
        bstack1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪഈ"): bstack1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨഉ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾ࡺࡶࡤࡢࡶࡨࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡷࡹࡧࡴࡶࡵࠥഊ"), datetime.datetime.now() - bstack1l1111lll_opy_)
    except Exception as e:
      logger.error(bstack11ll11l1ll_opy_.format(str(e)))
def bstack1ll11l1l11_opy_(test, bstack1l1ll1ll1_opy_):
  global CONFIG
  global bstack1ll111l1l1_opy_
  global bstack11l11111l_opy_
  global bstack1lll1l11l1_opy_
  global bstack1ll11111ll_opy_
  global bstack11ll1ll11l_opy_
  global bstack1l11l1111l_opy_
  global bstack11llllll1l_opy_
  global bstack11ll111ll_opy_
  global bstack11llll11l_opy_
  global bstack1ll1ll1l11_opy_
  global bstack111l1lll1_opy_
  global bstack1l1l111l11_opy_
  try:
    if not bstack1lll1l11l1_opy_:
      with bstack1l1l111l11_opy_:
        bstack1111l11lll_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠧࡿࠩഋ")), bstack1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨഌ"), bstack1l_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ഍"))
        if os.path.exists(bstack1111l11lll_opy_):
          with open(bstack1111l11lll_opy_, bstack1l_opy_ (u"ࠪࡶࠬഎ")) as f:
            content = f.read().strip()
            if content:
              bstack111ll11l1_opy_ = json.loads(bstack1l_opy_ (u"ࠦࢀࠨഏ") + content + bstack1l_opy_ (u"ࠬࠨࡸࠣ࠼ࠣࠦࡾࠨࠧഐ") + bstack1l_opy_ (u"ࠨࡽࠣ഑"))
              bstack1lll1l11l1_opy_ = bstack111ll11l1_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡋࡇࡷࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬഒ") + str(e))
  if bstack1ll1ll1l11_opy_:
    with bstack11l1l1111l_opy_:
      bstack1lll11l11l_opy_ = bstack1ll1ll1l11_opy_.copy()
    for driver in bstack1lll11l11l_opy_:
      if bstack1lll1l11l1_opy_ == driver.session_id:
        if test:
          bstack1ll1111l1_opy_(driver, test)
        bstack1lll1l1l11_opy_(driver, bstack1l1ll1ll1_opy_)
  elif bstack1lll1l11l1_opy_:
    bstack111ll1l1l1_opy_(test, bstack1l1ll1ll1_opy_)
  if bstack1ll111l1l1_opy_:
    bstack11llllll1l_opy_(bstack1ll111l1l1_opy_)
  if bstack11l11111l_opy_:
    bstack11ll111ll_opy_(bstack11l11111l_opy_)
  if bstack1ll1l11ll1_opy_:
    bstack11llll11l_opy_()
def bstack11l1l1111_opy_(self, test, *args, **kwargs):
  bstack1l1ll1ll1_opy_ = None
  if test:
    bstack1l1ll1ll1_opy_ = str(test.name)
  bstack1ll11l1l11_opy_(test, bstack1l1ll1ll1_opy_)
  bstack1l11l1111l_opy_(self, test, *args, **kwargs)
def bstack1111l1l1l1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11l11ll1l_opy_
  global CONFIG
  global bstack1ll1ll1l11_opy_
  global bstack1lll1l11l1_opy_
  global bstack1l1l111l11_opy_
  bstack1l111l1ll1_opy_ = None
  try:
    if bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧഓ"), None) or bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫഔ"), None):
      try:
        if not bstack1lll1l11l1_opy_:
          bstack1111l11lll_opy_ = os.path.join(os.path.expanduser(bstack1l_opy_ (u"ࠪࢂࠬക")), bstack1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫഖ"), bstack1l_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧഗ"))
          with bstack1l1l111l11_opy_:
            if os.path.exists(bstack1111l11lll_opy_):
              with open(bstack1111l11lll_opy_, bstack1l_opy_ (u"࠭ࡲࠨഘ")) as f:
                content = f.read().strip()
                if content:
                  bstack111ll11l1_opy_ = json.loads(bstack1l_opy_ (u"ࠢࡼࠤങ") + content + bstack1l_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪച") + bstack1l_opy_ (u"ࠤࢀࠦഛ"))
                  bstack1lll1l11l1_opy_ = bstack111ll11l1_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡎࡊࡳࠡࡨ࡬ࡰࡪࠦࡩ࡯ࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࠩജ") + str(e))
      if bstack1ll1ll1l11_opy_:
        with bstack11l1l1111l_opy_:
          bstack1lll11l11l_opy_ = bstack1ll1ll1l11_opy_.copy()
        for driver in bstack1lll11l11l_opy_:
          if bstack1lll1l11l1_opy_ == driver.session_id:
            bstack1l111l1ll1_opy_ = driver
    bstack111lll1ll1_opy_ = bstack11111ll1_opy_.bstack111l11l11_opy_(test.tags)
    if bstack1l111l1ll1_opy_:
      threading.current_thread().isA11yTest = bstack11111ll1_opy_.bstack1111l111l1_opy_(bstack1l111l1ll1_opy_, bstack111lll1ll1_opy_)
      threading.current_thread().isAppA11yTest = bstack11111ll1_opy_.bstack1111l111l1_opy_(bstack1l111l1ll1_opy_, bstack111lll1ll1_opy_)
    else:
      threading.current_thread().isA11yTest = bstack111lll1ll1_opy_
      threading.current_thread().isAppA11yTest = bstack111lll1ll1_opy_
  except:
    pass
  bstack11l11ll1l_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1ll11111ll_opy_
  try:
    bstack1ll11111ll_opy_ = self._test
  except:
    bstack1ll11111ll_opy_ = self.test
def bstack11l1llll1_opy_():
  global bstack1111ll1l11_opy_
  try:
    if os.path.exists(bstack1111ll1l11_opy_):
      os.remove(bstack1111ll1l11_opy_)
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡤࡦ࡮ࡨࡸ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧഝ") + str(e))
def bstack1lllll111l_opy_():
  global bstack1111ll1l11_opy_
  bstack11lllll1l_opy_ = {}
  lock_file = bstack1111ll1l11_opy_ + bstack1l_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫഞ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩട"))
    try:
      if not os.path.isfile(bstack1111ll1l11_opy_):
        with open(bstack1111ll1l11_opy_, bstack1l_opy_ (u"ࠧࡸࠩഠ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1111ll1l11_opy_):
        with open(bstack1111ll1l11_opy_, bstack1l_opy_ (u"ࠨࡴࠪഡ")) as f:
          content = f.read().strip()
          if content:
            bstack11lllll1l_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫഢ") + str(e))
    return bstack11lllll1l_opy_
  try:
    os.makedirs(os.path.dirname(bstack1111ll1l11_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack1111ll1l11_opy_):
        with open(bstack1111ll1l11_opy_, bstack1l_opy_ (u"ࠪࡻࠬണ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1111ll1l11_opy_):
        with open(bstack1111ll1l11_opy_, bstack1l_opy_ (u"ࠫࡷ࠭ത")) as f:
          content = f.read().strip()
          if content:
            bstack11lllll1l_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧഥ") + str(e))
  finally:
    return bstack11lllll1l_opy_
def bstack1l11l1l1l_opy_(platform_index, item_index):
  global bstack1111ll1l11_opy_
  lock_file = bstack1111ll1l11_opy_ + bstack1l_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬദ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠢࡱࡳࡹࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡥࡥࡸ࡯ࡣࠡࡨ࡬ࡰࡪࠦ࡯ࡱࡧࡵࡥࡹ࡯࡯࡯ࡵࠪധ"))
    try:
      bstack11lllll1l_opy_ = {}
      if os.path.exists(bstack1111ll1l11_opy_):
        with open(bstack1111ll1l11_opy_, bstack1l_opy_ (u"ࠨࡴࠪന")) as f:
          content = f.read().strip()
          if content:
            bstack11lllll1l_opy_ = json.loads(content)
      bstack11lllll1l_opy_[item_index] = platform_index
      with open(bstack1111ll1l11_opy_, bstack1l_opy_ (u"ࠤࡺࠦഩ")) as outfile:
        json.dump(bstack11lllll1l_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡽࡲࡪࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨപ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack1111ll1l11_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack11lllll1l_opy_ = {}
      if os.path.exists(bstack1111ll1l11_opy_):
        with open(bstack1111ll1l11_opy_, bstack1l_opy_ (u"ࠫࡷ࠭ഫ")) as f:
          content = f.read().strip()
          if content:
            bstack11lllll1l_opy_ = json.loads(content)
      bstack11lllll1l_opy_[item_index] = platform_index
      with open(bstack1111ll1l11_opy_, bstack1l_opy_ (u"ࠧࡽࠢബ")) as outfile:
        json.dump(bstack11lllll1l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡹࡵ࡭ࡹ࡯࡮ࡨࠢࡷࡳࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫഭ") + str(e))
def bstack1l1ll1111l_opy_(bstack11l11l1l1_opy_):
  global CONFIG
  bstack1l111l1ll_opy_ = bstack1l_opy_ (u"ࠧࠨമ")
  if not bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫയ") in CONFIG:
    logger.info(bstack1l_opy_ (u"ࠩࡑࡳࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠡࡲࡤࡷࡸ࡫ࡤࠡࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࠦࡲࡦࡲࡲࡶࡹࠦࡦࡰࡴࠣࡖࡴࡨ࡯ࡵࠢࡵࡹࡳ࠭ര"))
  try:
    platform = CONFIG[bstack1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭റ")][bstack11l11l1l1_opy_]
    if bstack1l_opy_ (u"ࠫࡴࡹࠧല") in platform:
      bstack1l111l1ll_opy_ += str(platform[bstack1l_opy_ (u"ࠬࡵࡳࠨള")]) + bstack1l_opy_ (u"࠭ࠬࠡࠩഴ")
    if bstack1l_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪവ") in platform:
      bstack1l111l1ll_opy_ += str(platform[bstack1l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫശ")]) + bstack1l_opy_ (u"ࠩ࠯ࠤࠬഷ")
    if bstack1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧസ") in platform:
      bstack1l111l1ll_opy_ += str(platform[bstack1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨഹ")]) + bstack1l_opy_ (u"ࠬ࠲ࠠࠨഺ")
    if bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ഻") in platform:
      bstack1l111l1ll_opy_ += str(platform[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯഼ࠩ")]) + bstack1l_opy_ (u"ࠨ࠮ࠣࠫഽ")
    if bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧാ") in platform:
      bstack1l111l1ll_opy_ += str(platform[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨി")]) + bstack1l_opy_ (u"ࠫ࠱ࠦࠧീ")
    if bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ു") in platform:
      bstack1l111l1ll_opy_ += str(platform[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧൂ")]) + bstack1l_opy_ (u"ࠧ࠭ࠢࠪൃ")
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠨࡕࡲࡱࡪࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡴࡶࡵ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡷ࡫ࡰࡰࡴࡷࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡵ࡮ࠨൄ") + str(e))
  finally:
    if bstack1l111l1ll_opy_[len(bstack1l111l1ll_opy_) - 2:] == bstack1l_opy_ (u"ࠩ࠯ࠤࠬ൅"):
      bstack1l111l1ll_opy_ = bstack1l111l1ll_opy_[:-2]
    return bstack1l111l1ll_opy_
def bstack1l11l1lll1_opy_(path, bstack1l111l1ll_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack111l1l1111_opy_ = ET.parse(path)
    bstack111llllll1_opy_ = bstack111l1l1111_opy_.getroot()
    bstack1ll11l1111_opy_ = None
    for suite in bstack111llllll1_opy_.iter(bstack1l_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩെ")):
      if bstack1l_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫേ") in suite.attrib:
        suite.attrib[bstack1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪൈ")] += bstack1l_opy_ (u"࠭ࠠࠨ൉") + bstack1l111l1ll_opy_
        bstack1ll11l1111_opy_ = suite
    bstack1lll11l111_opy_ = None
    for robot in bstack111llllll1_opy_.iter(bstack1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ൊ")):
      bstack1lll11l111_opy_ = robot
    bstack1lll111lll_opy_ = len(bstack1lll11l111_opy_.findall(bstack1l_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧോ")))
    if bstack1lll111lll_opy_ == 1:
      bstack1lll11l111_opy_.remove(bstack1lll11l111_opy_.findall(bstack1l_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨൌ"))[0])
      bstack1l11111l11_opy_ = ET.Element(bstack1l_opy_ (u"ࠪࡷࡺ࡯ࡴࡦ്ࠩ"), attrib={bstack1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩൎ"): bstack1l_opy_ (u"࡙ࠬࡵࡪࡶࡨࡷࠬ൏"), bstack1l_opy_ (u"࠭ࡩࡥࠩ൐"): bstack1l_opy_ (u"ࠧࡴ࠲ࠪ൑")})
      bstack1lll11l111_opy_.insert(1, bstack1l11111l11_opy_)
      bstack1l1l11ll1_opy_ = None
      for suite in bstack1lll11l111_opy_.iter(bstack1l_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧ൒")):
        bstack1l1l11ll1_opy_ = suite
      bstack1l1l11ll1_opy_.append(bstack1ll11l1111_opy_)
      bstack1l111l111_opy_ = None
      for status in bstack1ll11l1111_opy_.iter(bstack1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ൓")):
        bstack1l111l111_opy_ = status
      bstack1l1l11ll1_opy_.append(bstack1l111l111_opy_)
    bstack111l1l1111_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡳࡵ࡬ࡲ࡬ࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠨൔ") + str(e))
def bstack1lll1111l1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1l1l1111ll_opy_
  global CONFIG
  if bstack1l_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣൕ") in options:
    del options[bstack1l_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡵࡧࡴࡩࠤൖ")]
  json_data = bstack1lllll111l_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack1l_opy_ (u"࠭ࡰࡢࡤࡲࡸࡤࡸࡥࡴࡷ࡯ࡸࡸ࠭ൗ"), str(item_id), bstack1l_opy_ (u"ࠧࡰࡷࡷࡴࡺࡺ࠮ࡹ࡯࡯ࠫ൘"))
    bstack1l11l1lll1_opy_(path, bstack1l1ll1111l_opy_(json_data[item_id]))
  bstack11l1llll1_opy_()
  return bstack1l1l1111ll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack11l1ll1l1_opy_(self, ff_profile_dir):
  global bstack1lll111l11_opy_
  if not ff_profile_dir:
    return None
  return bstack1lll111l11_opy_(self, ff_profile_dir)
def bstack1l1lllll1_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1111ll11ll_opy_
  bstack1l1l1ll1l_opy_ = []
  if bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ൙") in CONFIG:
    bstack1l1l1ll1l_opy_ = CONFIG[bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ൚")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1l_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࠦ൛")],
      pabot_args[bstack1l_opy_ (u"ࠦࡻ࡫ࡲࡣࡱࡶࡩࠧ൜")],
      argfile,
      pabot_args.get(bstack1l_opy_ (u"ࠧ࡮ࡩࡷࡧࠥ൝")),
      pabot_args[bstack1l_opy_ (u"ࠨࡰࡳࡱࡦࡩࡸࡹࡥࡴࠤ൞")],
      platform[0],
      bstack1111ll11ll_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1l_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡨ࡬ࡰࡪࡹࠢൟ")] or [(bstack1l_opy_ (u"ࠣࠤൠ"), None)]
    for platform in enumerate(bstack1l1l1ll1l_opy_)
  ]
def bstack1l1l1l111l_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack11l1lllll1_opy_=bstack1l_opy_ (u"ࠩࠪൡ")):
  global bstack1111ll1lll_opy_
  self.platform_index = platform_index
  self.bstack1l1111l111_opy_ = bstack11l1lllll1_opy_
  bstack1111ll1lll_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1l11ll1111_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack111lll11l_opy_
  global bstack1l111lllll_opy_
  bstack1lllll1l11_opy_ = copy.deepcopy(item)
  if not bstack1l_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬൢ") in item.options:
    bstack1lllll1l11_opy_.options[bstack1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ൣ")] = []
  bstack111111l1l_opy_ = bstack1lllll1l11_opy_.options[bstack1l_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ൤")].copy()
  for v in bstack1lllll1l11_opy_.options[bstack1l_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ൥")]:
    if bstack1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭൦") in v:
      bstack111111l1l_opy_.remove(v)
    if bstack1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡄࡎࡌࡅࡗࡍࡓࠨ൧") in v:
      bstack111111l1l_opy_.remove(v)
    if bstack1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭൨") in v:
      bstack111111l1l_opy_.remove(v)
  bstack111111l1l_opy_.insert(0, bstack1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙࠼ࡾࢁࠬ൩").format(bstack1lllll1l11_opy_.platform_index))
  bstack111111l1l_opy_.insert(0, bstack1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡈࡊࡌࡌࡐࡅࡄࡐࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒ࠻ࡽࢀࠫ൪").format(bstack1lllll1l11_opy_.bstack1l1111l111_opy_))
  bstack1lllll1l11_opy_.options[bstack1l_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ൫")] = bstack111111l1l_opy_
  if bstack1l111lllll_opy_:
    bstack1lllll1l11_opy_.options[bstack1l_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ൬")].insert(0, bstack1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙࠺ࡼࡿࠪ൭").format(bstack1l111lllll_opy_))
  return bstack111lll11l_opy_(caller_id, datasources, is_last, bstack1lllll1l11_opy_, outs_dir)
def bstack11111ll11_opy_(command, item_index):
  try:
    if bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ൮")):
      os.environ[bstack1l_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ൯")] = json.dumps(CONFIG[bstack1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭൰")][item_index % bstack11lllll1ll_opy_])
    global bstack1l111lllll_opy_
    if bstack1l111lllll_opy_:
      command[0] = command[0].replace(bstack1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ൱"), bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡸࡪ࡫ࠡࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠢ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠡࠩ൲") + str(
        item_index) + bstack1l_opy_ (u"࠭ࠠࠨ൳") + bstack1l111lllll_opy_, 1)
    else:
      command[0] = command[0].replace(bstack1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭൴"),
                                      bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡴࡦ࡮ࠤࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠥ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠤࠬ൵") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡯ࡲࡨ࡮࡬ࡹࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࠥ࡬࡯ࡳࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲ࠿ࠦࡻࡾࠩ൶").format(str(e)))
def bstack11llll1lll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1l1l11l111_opy_
  try:
    bstack11111ll11_opy_(command, item_index)
    return bstack1l1l11l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮࠻ࠢࡾࢁࠬ൷").format(str(e)))
    raise e
def bstack1l1l1l1l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1l1l11l111_opy_
  try:
    bstack11111ll11_opy_(command, item_index)
    return bstack1l1l11l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠵࠲࠶࠹࠺ࠡࡽࢀࠫ൸").format(str(e)))
    try:
      return bstack1l1l11l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦ࠲࠯࠳࠶ࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪ൹").format(str(e2)))
      raise e
def bstack11ll11lll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1l1l11l111_opy_
  try:
    bstack11111ll11_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack1l1l11l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠷࠴࠱࠶࠼ࠣࡿࢂ࠭ൺ").format(str(e)))
    try:
      return bstack1l1l11l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡ࠴࠱࠵࠺ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࡾࢁࠬൻ").format(str(e2)))
      raise e
def _1ll11111l1_opy_(bstack1l11l11l11_opy_, item_index, process_timeout, sleep_before_start, bstack1l11lll111_opy_):
  bstack11111ll11_opy_(bstack1l11l11l11_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack11ll11llll_opy_(command, bstack1l1lll1l11_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1l1l11l111_opy_
  try:
    bstack11111ll11_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack1l1l11l111_opy_(command, bstack1l1lll1l11_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࠦ࠵࠯࠲࠽ࠤࢀࢃࠧർ").format(str(e)))
    try:
      return bstack1l1l11l111_opy_(command, bstack1l1lll1l11_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩൽ").format(str(e2)))
      raise e
def bstack11l11ll1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1l1l11l111_opy_
  try:
    process_timeout = _1ll11111l1_opy_(command, item_index, process_timeout, sleep_before_start, bstack1l_opy_ (u"ࠪ࠸࠳࠸ࠧൾ"))
    return bstack1l1l11l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠷࠲࠷ࡀࠠࡼࡿࠪൿ").format(str(e)))
    try:
      return bstack1l1l11l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࡾࢁࠬ඀").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack11l1111l1l_opy_(self, runner, quiet=False, capture=True):
  global bstack1111ll11l1_opy_
  bstack111ll11ll_opy_ = bstack1111ll11l1_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack1l_opy_ (u"࠭ࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࡡࡤࡶࡷ࠭ඁ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1l_opy_ (u"ࠧࡦࡺࡦࡣࡹࡸࡡࡤࡧࡥࡥࡨࡱ࡟ࡢࡴࡵࠫං")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack111ll11ll_opy_
def bstack1llllll1ll_opy_(runner, hook_name, context, element, bstack11l111llll_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack11l111111l_opy_.bstack11ll111l_opy_(hook_name, element)
    bstack11l111llll_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack11l111111l_opy_.bstack11l1ll11_opy_(element)
      if hook_name not in [bstack1l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠬඃ"), bstack1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡣ࡯ࡰࠬ඄")] and args and hasattr(args[0], bstack1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡡࡰࡩࡸࡹࡡࡨࡧࠪඅ")):
        args[0].error_message = bstack1l_opy_ (u"ࠫࠬආ")
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡪࡤࡲࡩࡲࡥࠡࡪࡲࡳࡰࡹࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧ࠽ࠤࢀࢃࠧඇ").format(str(e)))
@measure(event_name=EVENTS.bstack1lll11l1l_opy_, stage=STAGE.bstack11ll111111_opy_, hook_type=bstack1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡇ࡬࡭ࠤඈ"), bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack11ll11l1l_opy_(runner, name, context, bstack11l111llll_opy_, *args):
    if runner.hooks.get(bstack1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦඉ")).__name__ != bstack1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࡤࡪࡥࡧࡣࡸࡰࡹࡥࡨࡰࡱ࡮ࠦඊ"):
      bstack1llllll1ll_opy_(runner, name, context, runner, bstack11l111llll_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1l1lllllll_opy_(bstack1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨඋ")) else context.browser
      runner.driver_initialised = bstack1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢඌ")
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡩࡸࡩࡷࡧࡵࠤ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡥࠡࡣࡷࡸࡷ࡯ࡢࡶࡶࡨ࠾ࠥࢁࡽࠨඍ").format(str(e)))
def bstack1l111l1111_opy_(runner, name, context, bstack11l111llll_opy_, *args):
    bstack1llllll1ll_opy_(runner, name, context, context.feature, bstack11l111llll_opy_, *args)
    try:
      if not bstack1l1lll1ll1_opy_:
        bstack1l111l1ll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lllllll_opy_(bstack1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫඎ")) else context.browser
        if is_driver_active(bstack1l111l1ll1_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢඏ")
          bstack1l111l1l11_opy_ = str(runner.feature.name)
          bstack1lll11llll_opy_(context, bstack1l111l1l11_opy_)
          bstack1l111l1ll1_opy_.execute_script(bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬඐ") + json.dumps(bstack1l111l1l11_opy_) + bstack1l_opy_ (u"ࠨࡿࢀࠫඑ"))
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡ࡫ࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩඒ").format(str(e)))
def bstack1l1ll11ll_opy_(runner, name, context, bstack11l111llll_opy_, *args):
    if hasattr(context, bstack1l_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬඓ")):
        bstack11l111111l_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack1l_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ඔ")) else context.feature
    bstack1llllll1ll_opy_(runner, name, context, target, bstack11l111llll_opy_, *args)
@measure(event_name=EVENTS.bstack1lll1l111_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack1l111111l_opy_(runner, name, context, bstack11l111llll_opy_, *args):
    if len(context.scenario.tags) == 0: bstack11l111111l_opy_.start_test(context)
    bstack1llllll1ll_opy_(runner, name, context, context.scenario, bstack11l111llll_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1111l11ll_opy_.bstack11l11llll_opy_(context, *args)
    try:
      bstack1l111l1ll1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫඕ"), context.browser)
      if is_driver_active(bstack1l111l1ll1_opy_):
        bstack1ll1lll1_opy_.bstack11111l1l1l_opy_(bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඖ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤ඗")
        if (not bstack1l1lll1ll1_opy_):
          scenario_name = args[0].name
          feature_name = bstack1l111l1l11_opy_ = str(runner.feature.name)
          bstack1l111l1l11_opy_ = feature_name + bstack1l_opy_ (u"ࠨࠢ࠰ࠤࠬ඘") + scenario_name
          if runner.driver_initialised == bstack1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦ඙"):
            bstack1lll11llll_opy_(context, bstack1l111l1l11_opy_)
            bstack1l111l1ll1_opy_.execute_script(bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨක") + json.dumps(bstack1l111l1l11_opy_) + bstack1l_opy_ (u"ࠫࢂࢃࠧඛ"))
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰ࠼ࠣࡿࢂ࠭ග").format(str(e)))
@measure(event_name=EVENTS.bstack1lll11l1l_opy_, stage=STAGE.bstack11ll111111_opy_, hook_type=bstack1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪ࡙ࡴࡦࡲࠥඝ"), bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack11lll1l111_opy_(runner, name, context, bstack11l111llll_opy_, *args):
    bstack1llllll1ll_opy_(runner, name, context, args[0], bstack11l111llll_opy_, *args)
    try:
      bstack1l111l1ll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lllllll_opy_(bstack1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ඞ")) else context.browser
      if is_driver_active(bstack1l111l1ll1_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨඟ")
        bstack11l111111l_opy_.bstack11ll11ll_opy_(args[0])
        if runner.driver_initialised == bstack1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢච"):
          feature_name = bstack1l111l1l11_opy_ = str(runner.feature.name)
          bstack1l111l1l11_opy_ = feature_name + bstack1l_opy_ (u"ࠪࠤ࠲ࠦࠧඡ") + context.scenario.name
          bstack1l111l1ll1_opy_.execute_script(bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩජ") + json.dumps(bstack1l111l1l11_opy_) + bstack1l_opy_ (u"ࠬࢃࡽࠨඣ"))
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡷࡩࡵࡀࠠࡼࡿࠪඤ").format(str(e)))
@measure(event_name=EVENTS.bstack1lll11l1l_opy_, stage=STAGE.bstack11ll111111_opy_, hook_type=bstack1l_opy_ (u"ࠢࡢࡨࡷࡩࡷ࡙ࡴࡦࡲࠥඥ"), bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack1ll11l111_opy_(runner, name, context, bstack11l111llll_opy_, *args):
  bstack11l111111l_opy_.bstack11ll1lll_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack1l111l1ll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧඦ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1l111l1ll1_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack1l_opy_ (u"ࠩ࡬ࡲࡸࡺࡥࡱࠩට")
        feature_name = bstack1l111l1l11_opy_ = str(runner.feature.name)
        bstack1l111l1l11_opy_ = feature_name + bstack1l_opy_ (u"ࠪࠤ࠲ࠦࠧඨ") + context.scenario.name
        bstack1l111l1ll1_opy_.execute_script(bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩඩ") + json.dumps(bstack1l111l1l11_opy_) + bstack1l_opy_ (u"ࠬࢃࡽࠨඪ"))
    if str(step_status).lower() == bstack1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ණ"):
      bstack1l1lll11l_opy_ = bstack1l_opy_ (u"ࠧࠨඬ")
      bstack11lll111l1_opy_ = bstack1l_opy_ (u"ࠨࠩත")
      bstack1ll111lll1_opy_ = bstack1l_opy_ (u"ࠩࠪථ")
      try:
        import traceback
        bstack1l1lll11l_opy_ = runner.exception.__class__.__name__
        bstack11ll11l1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11lll111l1_opy_ = bstack1l_opy_ (u"ࠪࠤࠬද").join(bstack11ll11l1_opy_)
        bstack1ll111lll1_opy_ = bstack11ll11l1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l1l111l1l_opy_.format(str(e)))
      bstack1l1lll11l_opy_ += bstack1ll111lll1_opy_
      bstack1l111llll1_opy_(context, json.dumps(str(args[0].name) + bstack1l_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥධ") + str(bstack11lll111l1_opy_)),
                          bstack1l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦන"))
      if runner.driver_initialised == bstack1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦ඲"):
        bstack111llll1ll_opy_(getattr(context, bstack1l_opy_ (u"ࠧࡱࡣࡪࡩࠬඳ"), None), bstack1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣප"), bstack1l1lll11l_opy_)
        bstack1l111l1ll1_opy_.execute_script(bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧඵ") + json.dumps(str(args[0].name) + bstack1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤබ") + str(bstack11lll111l1_opy_)) + bstack1l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫභ"))
      if runner.driver_initialised == bstack1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥම"):
        bstack11111ll111_opy_(bstack1l111l1ll1_opy_, bstack1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ඹ"), bstack1l_opy_ (u"ࠢࡔࡥࡨࡲࡦࡸࡩࡰࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦය") + str(bstack1l1lll11l_opy_))
    else:
      bstack1l111llll1_opy_(context, bstack1l_opy_ (u"ࠣࡒࡤࡷࡸ࡫ࡤࠢࠤර"), bstack1l_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢ඼"))
      if runner.driver_initialised == bstack1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣල"):
        bstack111llll1ll_opy_(getattr(context, bstack1l_opy_ (u"ࠫࡵࡧࡧࡦࠩ඾"), None), bstack1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ඿"))
      bstack1l111l1ll1_opy_.execute_script(bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫව") + json.dumps(str(args[0].name) + bstack1l_opy_ (u"ࠢࠡ࠯ࠣࡔࡦࡹࡳࡦࡦࠤࠦශ")) + bstack1l_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦࢂࢃࠧෂ"))
      if runner.driver_initialised == bstack1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢස"):
        bstack11111ll111_opy_(bstack1l111l1ll1_opy_, bstack1l_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥහ"))
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡵࡷࡩࡵࡀࠠࡼࡿࠪළ").format(str(e)))
  bstack1llllll1ll_opy_(runner, name, context, args[0], bstack11l111llll_opy_, *args)
@measure(event_name=EVENTS.bstack11l1ll1111_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack1111lll111_opy_(runner, name, context, bstack11l111llll_opy_, *args):
  bstack11l111111l_opy_.end_test(args[0])
  try:
    bstack111l1lllll_opy_ = args[0].status.name
    bstack1l111l1ll1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫෆ"), context.browser)
    bstack1111l11ll_opy_.bstack1ll111l111_opy_(bstack1l111l1ll1_opy_)
    if str(bstack111l1lllll_opy_).lower() == bstack1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭෇"):
      bstack1l1lll11l_opy_ = bstack1l_opy_ (u"ࠧࠨ෈")
      bstack11lll111l1_opy_ = bstack1l_opy_ (u"ࠨࠩ෉")
      bstack1ll111lll1_opy_ = bstack1l_opy_ (u"්ࠩࠪ")
      try:
        import traceback
        bstack1l1lll11l_opy_ = runner.exception.__class__.__name__
        bstack11ll11l1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11lll111l1_opy_ = bstack1l_opy_ (u"ࠪࠤࠬ෋").join(bstack11ll11l1_opy_)
        bstack1ll111lll1_opy_ = bstack11ll11l1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l1l111l1l_opy_.format(str(e)))
      bstack1l1lll11l_opy_ += bstack1ll111lll1_opy_
      bstack1l111llll1_opy_(context, json.dumps(str(args[0].name) + bstack1l_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥ෌") + str(bstack11lll111l1_opy_)),
                          bstack1l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦ෍"))
      if runner.driver_initialised == bstack1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣ෎") or runner.driver_initialised == bstack1l_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧා"):
        bstack111llll1ll_opy_(getattr(context, bstack1l_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ැ"), None), bstack1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤෑ"), bstack1l1lll11l_opy_)
        bstack1l111l1ll1_opy_.execute_script(bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨි") + json.dumps(str(args[0].name) + bstack1l_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥී") + str(bstack11lll111l1_opy_)) + bstack1l_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤࢀࢁࠬු"))
      if runner.driver_initialised == bstack1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣ෕") or runner.driver_initialised == bstack1l_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧූ"):
        bstack11111ll111_opy_(bstack1l111l1ll1_opy_, bstack1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ෗"), bstack1l_opy_ (u"ࠤࡖࡧࡪࡴࡡࡳ࡫ࡲࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨෘ") + str(bstack1l1lll11l_opy_))
    else:
      bstack1l111llll1_opy_(context, bstack1l_opy_ (u"ࠥࡔࡦࡹࡳࡦࡦࠤࠦෙ"), bstack1l_opy_ (u"ࠦ࡮ࡴࡦࡰࠤේ"))
      if runner.driver_initialised == bstack1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢෛ") or runner.driver_initialised == bstack1l_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭ො"):
        bstack111llll1ll_opy_(getattr(context, bstack1l_opy_ (u"ࠧࡱࡣࡪࡩࠬෝ"), None), bstack1l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣෞ"))
      bstack1l111l1ll1_opy_.execute_script(bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧෟ") + json.dumps(str(args[0].name) + bstack1l_opy_ (u"ࠥࠤ࠲ࠦࡐࡢࡵࡶࡩࡩࠧࠢ෠")) + bstack1l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢࡾࡿࠪ෡"))
      if runner.driver_initialised == bstack1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ෢") or runner.driver_initialised == bstack1l_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෣"):
        bstack11111ll111_opy_(bstack1l111l1ll1_opy_, bstack1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ෤"))
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪ෥").format(str(e)))
  bstack1llllll1ll_opy_(runner, name, context, context.scenario, bstack11l111llll_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack11l1l11111_opy_(runner, name, context, bstack11l111llll_opy_, *args):
    target = context.scenario if hasattr(context, bstack1l_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫ෦")) else context.feature
    bstack1llllll1ll_opy_(runner, name, context, target, bstack11l111llll_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1ll1lll1ll_opy_(runner, name, context, bstack11l111llll_opy_, *args):
    try:
      bstack1l111l1ll1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ෧"), context.browser)
      bstack11ll1l111_opy_ = bstack1l_opy_ (u"ࠫࠬ෨")
      if context.failed is True:
        bstack1ll11lll1_opy_ = []
        bstack1ll111111l_opy_ = []
        bstack1l111lll11_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1ll11lll1_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11ll11l1_opy_ = traceback.format_tb(exc_tb)
            bstack1ll1ll11l1_opy_ = bstack1l_opy_ (u"ࠬࠦࠧ෩").join(bstack11ll11l1_opy_)
            bstack1ll111111l_opy_.append(bstack1ll1ll11l1_opy_)
            bstack1l111lll11_opy_.append(bstack11ll11l1_opy_[-1])
        except Exception as e:
          logger.debug(bstack1l1l111l1l_opy_.format(str(e)))
        bstack1l1lll11l_opy_ = bstack1l_opy_ (u"࠭ࠧ෪")
        for i in range(len(bstack1ll11lll1_opy_)):
          bstack1l1lll11l_opy_ += bstack1ll11lll1_opy_[i] + bstack1l111lll11_opy_[i] + bstack1l_opy_ (u"ࠧ࡝ࡰࠪ෫")
        bstack11ll1l111_opy_ = bstack1l_opy_ (u"ࠨࠢࠪ෬").join(bstack1ll111111l_opy_)
        if runner.driver_initialised in [bstack1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥ෭"), bstack1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢ෮")]:
          bstack1l111llll1_opy_(context, bstack11ll1l111_opy_, bstack1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ෯"))
          bstack111llll1ll_opy_(getattr(context, bstack1l_opy_ (u"ࠬࡶࡡࡨࡧࠪ෰"), None), bstack1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ෱"), bstack1l1lll11l_opy_)
          bstack1l111l1ll1_opy_.execute_script(bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬෲ") + json.dumps(bstack11ll1l111_opy_) + bstack1l_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨෳ"))
          bstack11111ll111_opy_(bstack1l111l1ll1_opy_, bstack1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ෴"), bstack1l_opy_ (u"ࠥࡗࡴࡳࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱࡶࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࡢ࡮ࠣ෵") + str(bstack1l1lll11l_opy_))
          bstack1111111ll_opy_ = bstack1ll11l11l1_opy_(bstack11ll1l111_opy_, runner.feature.name, logger)
          if (bstack1111111ll_opy_ != None):
            bstack1111l1lll1_opy_.append(bstack1111111ll_opy_)
      else:
        if runner.driver_initialised in [bstack1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧ෶"), bstack1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤ෷")]:
          bstack1l111llll1_opy_(context, bstack1l_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫࠺ࠡࠤ෸") + str(runner.feature.name) + bstack1l_opy_ (u"ࠢࠡࡲࡤࡷࡸ࡫ࡤࠢࠤ෹"), bstack1l_opy_ (u"ࠣ࡫ࡱࡪࡴࠨ෺"))
          bstack111llll1ll_opy_(getattr(context, bstack1l_opy_ (u"ࠩࡳࡥ࡬࡫ࠧ෻"), None), bstack1l_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ෼"))
          bstack1l111l1ll1_opy_.execute_script(bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ෽") + json.dumps(bstack1l_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣ෾") + str(runner.feature.name) + bstack1l_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣ෿")) + bstack1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭฀"))
          bstack11111ll111_opy_(bstack1l111l1ll1_opy_, bstack1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨก"))
          bstack1111111ll_opy_ = bstack1ll11l11l1_opy_(bstack11ll1l111_opy_, runner.feature.name, logger)
          if (bstack1111111ll_opy_ != None):
            bstack1111l1lll1_opy_.append(bstack1111111ll_opy_)
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫข").format(str(e)))
    bstack1llllll1ll_opy_(runner, name, context, context.feature, bstack11l111llll_opy_, *args)
@measure(event_name=EVENTS.bstack1lll11l1l_opy_, stage=STAGE.bstack11ll111111_opy_, hook_type=bstack1l_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࡃ࡯ࡰࠧฃ"), bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack11l111lll1_opy_(runner, name, context, bstack11l111llll_opy_, *args):
    bstack1llllll1ll_opy_(runner, name, context, runner, bstack11l111llll_opy_, *args)
def bstack1l1l11l11l_opy_(self, name, context, *args):
  try:
    if bstack1lll1ll1l1_opy_:
      platform_index = int(threading.current_thread()._name) % bstack11lllll1ll_opy_
      bstack1ll1l11ll_opy_ = CONFIG[bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧค")][platform_index]
      os.environ[bstack1l_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭ฅ")] = json.dumps(bstack1ll1l11ll_opy_)
    global bstack11l111llll_opy_
    if not hasattr(self, bstack1l_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡧࡧࠫฆ")):
      self.driver_initialised = None
    bstack1l11l1l1l1_opy_ = {
        bstack1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫง"): bstack11ll11l1l_opy_,
        bstack1l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠩจ"): bstack1l111l1111_opy_,
        bstack1l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡷࡥ࡬࠭ฉ"): bstack1l1ll11ll_opy_,
        bstack1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬช"): bstack1l111111l_opy_,
        bstack1l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠩซ"): bstack11lll1l111_opy_,
        bstack1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡺࡥࡱࠩฌ"): bstack1ll11l111_opy_,
        bstack1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧญ"): bstack1111lll111_opy_,
        bstack1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡴࡢࡩࠪฎ"): bstack11l1l11111_opy_,
        bstack1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨฏ"): bstack1ll1lll1ll_opy_,
        bstack1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡣ࡯ࡰࠬฐ"): bstack11l111lll1_opy_
    }
    handler = bstack1l11l1l1l1_opy_.get(name, bstack11l111llll_opy_)
    try:
      handler(self, name, context, bstack11l111llll_opy_, *args)
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩࠥ࡮࡯ࡰ࡭ࠣ࡬ࡦࡴࡤ࡭ࡧࡵࠤࢀࢃ࠺ࠡࡽࢀࠫฑ").format(name, str(e)))
    if name in [bstack1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡪࡪࡧࡴࡶࡴࡨࠫฒ"), bstack1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ณ"), bstack1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩด")]:
      try:
        bstack1l111l1ll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lllllll_opy_(bstack1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ต")) else context.browser
        bstack111l11lll_opy_ = (
          (name == bstack1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫถ") and self.driver_initialised == bstack1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨท")) or
          (name == bstack1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪธ") and self.driver_initialised == bstack1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧน")) or
          (name == bstack1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭บ") and self.driver_initialised in [bstack1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣป"), bstack1l_opy_ (u"ࠢࡪࡰࡶࡸࡪࡶࠢผ")]) or
          (name == bstack1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡶࡨࡴࠬฝ") and self.driver_initialised == bstack1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢพ"))
        )
        if bstack111l11lll_opy_:
          self.driver_initialised = None
          if bstack1l111l1ll1_opy_ and hasattr(bstack1l111l1ll1_opy_, bstack1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧฟ")):
            try:
              bstack1l111l1ll1_opy_.quit()
            except Exception as e:
              logger.debug(bstack1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡵࡺ࡯ࡴࡵ࡫ࡱ࡫ࠥࡪࡲࡪࡸࡨࡶࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥࠡࡪࡲࡳࡰࡀࠠࡼࡿࠪภ").format(str(e)))
      except Exception as e:
        logger.debug(bstack1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡨࡰࡱ࡮ࠤࡨࡲࡥࡢࡰࡸࡴࠥ࡬࡯ࡳࠢࡾࢁ࠿ࠦࡻࡾࠩม").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"࠭ࡃࡳ࡫ࡷ࡭ࡨࡧ࡬ࠡࡧࡵࡶࡴࡸࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧࠣࡶࡺࡴࠠࡩࡱࡲ࡯ࠥࢁࡽ࠻ࠢࡾࢁࠬย").format(name, str(e)))
    try:
      bstack11l111llll_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡥࡱࡲࡢࡢࡥ࡮ࠤࡴࡸࡩࡨ࡫ࡱࡥࡱࠦࡢࡦࡪࡤࡺࡪࠦࡨࡰࡱ࡮ࠤࢀࢃ࠺ࠡࡽࢀࠫร").format(name, str(e2)))
def bstack111l11lll1_opy_(config, startdir):
  return bstack1l_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾ࠴ࢂࠨฤ").format(bstack1l_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣล"))
notset = Notset()
def bstack1l111llll_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1l1111111l_opy_
  if str(name).lower() == bstack1l_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪฦ"):
    return bstack1l_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥว")
  else:
    return bstack1l1111111l_opy_(self, name, default, skip)
def bstack1111l1l11l_opy_(item, when):
  global bstack11l1l111l_opy_
  try:
    bstack11l1l111l_opy_(item, when)
  except Exception as e:
    pass
def bstack1lll1llll1_opy_():
  return
def bstack111ll11l11_opy_(type, name, status, reason, bstack1l111l11l1_opy_, bstack11l111lll_opy_):
  bstack1ll1l11l1_opy_ = {
    bstack1l_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬศ"): type,
    bstack1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩษ"): {}
  }
  if type == bstack1l_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩส"):
    bstack1ll1l11l1_opy_[bstack1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫห")][bstack1l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨฬ")] = bstack1l111l11l1_opy_
    bstack1ll1l11l1_opy_[bstack1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭อ")][bstack1l_opy_ (u"ࠫࡩࡧࡴࡢࠩฮ")] = json.dumps(str(bstack11l111lll_opy_))
  if type == bstack1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ฯ"):
    bstack1ll1l11l1_opy_[bstack1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩะ")][bstack1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬั")] = name
  if type == bstack1l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫา"):
    bstack1ll1l11l1_opy_[bstack1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬำ")][bstack1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪิ")] = status
    if status == bstack1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫี"):
      bstack1ll1l11l1_opy_[bstack1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨึ")][bstack1l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ื")] = json.dumps(str(reason))
  bstack11111l111_opy_ = bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁุࠬ").format(json.dumps(bstack1ll1l11l1_opy_))
  return bstack11111l111_opy_
def bstack11l1l1ll11_opy_(driver_command, response):
    if driver_command == bstack1l_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸูࠬ"):
        bstack1ll1lll1_opy_.bstack1l11ll11l1_opy_({
            bstack1l_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨฺ"): response[bstack1l_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ฻")],
            bstack1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ฼"): bstack1ll1lll1_opy_.current_test_uuid()
        })
def bstack111lll1l1l_opy_(item, call, rep):
  global bstack1l1111l11_opy_
  global bstack1ll1ll1l11_opy_
  global bstack1l1lll1ll1_opy_
  name = bstack1l_opy_ (u"ࠬ࠭฽")
  try:
    if rep.when == bstack1l_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ฾"):
      bstack1lll1l11l1_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1l1lll1ll1_opy_:
          name = str(rep.nodeid)
          bstack111lll1ll_opy_ = bstack111ll11l11_opy_(bstack1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ฿"), name, bstack1l_opy_ (u"ࠨࠩเ"), bstack1l_opy_ (u"ࠩࠪแ"), bstack1l_opy_ (u"ࠪࠫโ"), bstack1l_opy_ (u"ࠫࠬใ"))
          threading.current_thread().bstack1ll1lll1l_opy_ = name
          for driver in bstack1ll1ll1l11_opy_:
            if bstack1lll1l11l1_opy_ == driver.session_id:
              driver.execute_script(bstack111lll1ll_opy_)
      except Exception as e:
        logger.debug(bstack1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬไ").format(str(e)))
      try:
        bstack1ll1111lll_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧๅ"):
          status = bstack1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧๆ") if rep.outcome.lower() == bstack1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ็") else bstack1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥ่ࠩ")
          reason = bstack1l_opy_ (u"้ࠪࠫ")
          if status == bstack1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧ๊ࠫ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1l_opy_ (u"ࠬ࡯࡮ࡧࡱ๋ࠪ") if status == bstack1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭์") else bstack1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ํ")
          data = name + bstack1l_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪ๎") if status == bstack1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ๏") else name + bstack1l_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠥࠥ࠭๐") + reason
          bstack1lllllllll_opy_ = bstack111ll11l11_opy_(bstack1l_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭๑"), bstack1l_opy_ (u"ࠬ࠭๒"), bstack1l_opy_ (u"࠭ࠧ๓"), bstack1l_opy_ (u"ࠧࠨ๔"), level, data)
          for driver in bstack1ll1ll1l11_opy_:
            if bstack1lll1l11l1_opy_ == driver.session_id:
              driver.execute_script(bstack1lllllllll_opy_)
      except Exception as e:
        logger.debug(bstack1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ๕").format(str(e)))
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭๖").format(str(e)))
  bstack1l1111l11_opy_(item, call, rep)
def bstack111ll1ll1l_opy_(driver, bstack11l1l1ll1l_opy_, test=None):
  global bstack1l11l11l1_opy_
  if test != None:
    bstack1111l1ll1_opy_ = getattr(test, bstack1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ๗"), None)
    bstack1111lllll_opy_ = getattr(test, bstack1l_opy_ (u"ࠫࡺࡻࡩࡥࠩ๘"), None)
    PercySDK.screenshot(driver, bstack11l1l1ll1l_opy_, bstack1111l1ll1_opy_=bstack1111l1ll1_opy_, bstack1111lllll_opy_=bstack1111lllll_opy_, bstack1111l11111_opy_=bstack1l11l11l1_opy_)
  else:
    PercySDK.screenshot(driver, bstack11l1l1ll1l_opy_)
@measure(event_name=EVENTS.bstack1111ll1ll1_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack111l11l1l_opy_(driver):
  if bstack1ll1ll1ll_opy_.bstack11l1llllll_opy_() is True or bstack1ll1ll1ll_opy_.capturing() is True:
    return
  bstack1ll1ll1ll_opy_.bstack11l1111lll_opy_()
  while not bstack1ll1ll1ll_opy_.bstack11l1llllll_opy_():
    bstack1llll1ll11_opy_ = bstack1ll1ll1ll_opy_.bstack1lll111111_opy_()
    bstack111ll1ll1l_opy_(driver, bstack1llll1ll11_opy_)
  bstack1ll1ll1ll_opy_.bstack1l1l11111l_opy_()
def bstack111ll111l1_opy_(sequence, driver_command, response = None, bstack1l111ll11l_opy_ = None, args = None):
    try:
      if sequence != bstack1l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬ๙"):
        return
      if percy.bstack111l11ll1l_opy_() == bstack1l_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧ๚"):
        return
      bstack1llll1ll11_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ๛"), None)
      for command in bstack1ll1111ll_opy_:
        if command == driver_command:
          with bstack11l1l1111l_opy_:
            bstack1lll11l11l_opy_ = bstack1ll1ll1l11_opy_.copy()
          for driver in bstack1lll11l11l_opy_:
            bstack111l11l1l_opy_(driver)
      bstack111l11l11l_opy_ = percy.bstack11ll1l1ll_opy_()
      if driver_command in bstack11l1ll11ll_opy_[bstack111l11l11l_opy_]:
        bstack1ll1ll1ll_opy_.bstack1lllllll1l_opy_(bstack1llll1ll11_opy_, driver_command)
    except Exception as e:
      pass
def bstack1l1lll1l1_opy_(framework_name):
  if bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬ๜")):
      return
  bstack1lll1ll1l_opy_.set_property(bstack1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭๝"), True)
  global bstack11l1lll1l_opy_
  global bstack1lll1l111l_opy_
  global bstack1l11l11ll_opy_
  bstack11l1lll1l_opy_ = framework_name
  logger.info(bstack11ll11l11_opy_.format(bstack11l1lll1l_opy_.split(bstack1l_opy_ (u"ࠪ࠱ࠬ๞"))[0]))
  bstack1111lllll1_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1lll1ll1l1_opy_:
      Service.start = bstack1l1l1lll1_opy_
      Service.stop = bstack111llll11l_opy_
      webdriver.Remote.get = bstack1lllll1ll1_opy_
      WebDriver.quit = bstack111l111111_opy_
      webdriver.Remote.__init__ = bstack1ll11llll1_opy_
    if not bstack1lll1ll1l1_opy_:
        webdriver.Remote.__init__ = bstack1ll1llllll_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack1l1l1lllll_opy_
    bstack1lll1l111l_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1lll1ll1l1_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack11ll111lll_opy_
  except Exception as e:
    pass
  bstack1l111l1lll_opy_()
  if not bstack1lll1l111l_opy_:
    bstack1l1111l1l1_opy_(bstack1l_opy_ (u"ࠦࡕࡧࡣ࡬ࡣࡪࡩࡸࠦ࡮ࡰࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠨ๟"), bstack1l111ll1l_opy_)
  if bstack111ll11111_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack1l_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭๠")) and callable(getattr(RemoteConnection, bstack1l_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ๡"))):
        RemoteConnection._get_proxy_url = bstack111ll1111l_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack111ll1111l_opy_
    except Exception as e:
      logger.error(bstack1ll1ll11ll_opy_.format(str(e)))
  if bstack1l111ll111_opy_():
    bstack1lll11ll1_opy_(CONFIG, logger)
  if (bstack1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭๢") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack111l11ll1l_opy_() == bstack1l_opy_ (u"ࠣࡶࡵࡹࡪࠨ๣"):
          bstack111l11111_opy_(bstack111ll111l1_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack11l1ll1l1_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l111l1l1_opy_
      except Exception as e:
        logger.warn(bstack11lll11l1l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack111ll1ll11_opy_
      except Exception as e:
        logger.debug(bstack11llll1ll1_opy_ + str(e))
    except Exception as e:
      bstack1l1111l1l1_opy_(e, bstack11lll11l1l_opy_)
    Output.start_test = bstack1l1l111ll1_opy_
    Output.end_test = bstack11l1l1111_opy_
    TestStatus.__init__ = bstack1111l1l1l1_opy_
    QueueItem.__init__ = bstack1l1l1l111l_opy_
    pabot._create_items = bstack1l1lllll1_opy_
    try:
      from pabot import __version__ as bstack11llll1ll_opy_
      if version.parse(bstack11llll1ll_opy_) >= version.parse(bstack1l_opy_ (u"ࠩ࠸࠲࠵࠴࠰ࠨ๤")):
        pabot._run = bstack11ll11llll_opy_
      elif version.parse(bstack11llll1ll_opy_) >= version.parse(bstack1l_opy_ (u"ࠪ࠸࠳࠸࠮࠱ࠩ๥")):
        pabot._run = bstack11l11ll1l1_opy_
      elif version.parse(bstack11llll1ll_opy_) >= version.parse(bstack1l_opy_ (u"ࠫ࠷࠴࠱࠶࠰࠳ࠫ๦")):
        pabot._run = bstack11ll11lll1_opy_
      elif version.parse(bstack11llll1ll_opy_) >= version.parse(bstack1l_opy_ (u"ࠬ࠸࠮࠲࠵࠱࠴ࠬ๧")):
        pabot._run = bstack1l1l1l1l11_opy_
      else:
        pabot._run = bstack11llll1lll_opy_
    except Exception as e:
      pabot._run = bstack11llll1lll_opy_
    pabot._create_command_for_execution = bstack1l11ll1111_opy_
    pabot._report_results = bstack1lll1111l1_opy_
  if bstack1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭๨") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1111l1l1_opy_(e, bstack1l1l1ll1ll_opy_)
    Runner.run_hook = bstack1l1l11l11l_opy_
    Step.run = bstack11l1111l1l_opy_
  if bstack1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ๩") in str(framework_name).lower():
    if not bstack1lll1ll1l1_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack111l11lll1_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1lll1llll1_opy_
      Config.getoption = bstack1l111llll_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack111lll1l1l_opy_
    except Exception as e:
      pass
def bstack111l1ll11l_opy_():
  global CONFIG
  if bstack1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ๪") in CONFIG and int(CONFIG[bstack1l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ๫")]) > 1:
    logger.warn(bstack1ll1l1ll1l_opy_)
def bstack111l1111l_opy_(arg, bstack1lllll1l1_opy_, bstack1lllll1111_opy_=None):
  global CONFIG
  global bstack11l1ll1ll1_opy_
  global bstack11l11111ll_opy_
  global bstack1lll1ll1l1_opy_
  global bstack1lll1ll1l_opy_
  bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ๬")
  if bstack1lllll1l1_opy_ and isinstance(bstack1lllll1l1_opy_, str):
    bstack1lllll1l1_opy_ = eval(bstack1lllll1l1_opy_)
  CONFIG = bstack1lllll1l1_opy_[bstack1l_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫ๭")]
  bstack11l1ll1ll1_opy_ = bstack1lllll1l1_opy_[bstack1l_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭๮")]
  bstack11l11111ll_opy_ = bstack1lllll1l1_opy_[bstack1l_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ๯")]
  bstack1lll1ll1l1_opy_ = bstack1lllll1l1_opy_[bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪ๰")]
  bstack1lll1ll1l_opy_.set_property(bstack1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ๱"), bstack1lll1ll1l1_opy_)
  os.environ[bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ๲")] = bstack1111lll11l_opy_
  os.environ[bstack1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠩ๳")] = json.dumps(CONFIG)
  os.environ[bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡌ࡚ࡈ࡟ࡖࡔࡏࠫ๴")] = bstack11l1ll1ll1_opy_
  os.environ[bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭๵")] = str(bstack11l11111ll_opy_)
  os.environ[bstack1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡌࡖࡉࡌࡒࠬ๶")] = str(True)
  if bstack111ll1ll1_opy_(arg, [bstack1l_opy_ (u"ࠧ࠮ࡰࠪ๷"), bstack1l_opy_ (u"ࠨ࠯࠰ࡲࡺࡳࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ๸")]) != -1:
    os.environ[bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡄࡖࡆࡒࡌࡆࡎࠪ๹")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1ll111l1l_opy_)
    return
  bstack1l1ll1l11l_opy_()
  global bstack1ll1l1ll11_opy_
  global bstack1l11l11l1_opy_
  global bstack1111ll11ll_opy_
  global bstack1l111lllll_opy_
  global bstack1111ll1l1_opy_
  global bstack1l11l11ll_opy_
  global bstack11lll1ll1_opy_
  arg.append(bstack1l_opy_ (u"ࠥ࠱࡜ࠨ๺"))
  arg.append(bstack1l_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨ࠾ࡒࡵࡤࡶ࡮ࡨࠤࡦࡲࡲࡦࡣࡧࡽࠥ࡯࡭ࡱࡱࡵࡸࡪࡪ࠺ࡱࡻࡷࡩࡸࡺ࠮ࡑࡻࡷࡩࡸࡺࡗࡢࡴࡱ࡭ࡳ࡭ࠢ๻"))
  arg.append(bstack1l_opy_ (u"ࠧ࠳ࡗࠣ๼"))
  arg.append(bstack1l_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡀࡔࡩࡧࠣ࡬ࡴࡵ࡫ࡪ࡯ࡳࡰࠧ๽"))
  global bstack1ll1ll1ll1_opy_
  global bstack111l11ll11_opy_
  global bstack11ll1l1l11_opy_
  global bstack11l11ll1l_opy_
  global bstack1lll111l11_opy_
  global bstack1111ll1lll_opy_
  global bstack111lll11l_opy_
  global bstack11ll1llll_opy_
  global bstack1ll1l1l1ll_opy_
  global bstack1l1ll1l1ll_opy_
  global bstack1l1111111l_opy_
  global bstack11l1l111l_opy_
  global bstack1l1111l11_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll1ll1ll1_opy_ = webdriver.Remote.__init__
    bstack111l11ll11_opy_ = WebDriver.quit
    bstack11ll1llll_opy_ = WebDriver.close
    bstack1ll1l1l1ll_opy_ = WebDriver.get
    bstack11ll1l1l11_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack111l1l11ll_opy_(CONFIG) and bstack11l11l1l11_opy_():
    if bstack1lll1lll1l_opy_() < version.parse(bstack11l1lll11_opy_):
      logger.error(bstack11ll1lll1_opy_.format(bstack1lll1lll1l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1l_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ๾")) and callable(getattr(RemoteConnection, bstack1l_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ๿"))):
          bstack1l1ll1l1ll_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1l1ll1l1ll_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack1ll1ll11ll_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1l1111111l_opy_ = Config.getoption
    from _pytest import runner
    bstack11l1l111l_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack11111111_opy_)
  try:
    from pytest_bdd import reporting
    bstack1l1111l11_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1l_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪ຀"))
  bstack1111ll11ll_opy_ = CONFIG.get(bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧກ"), {}).get(bstack1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ຂ"))
  bstack11lll1ll1_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack1llll1l1ll_opy_():
      bstack1l111l11l_opy_.invoke(Events.CONNECT, bstack1111ll111_opy_())
    platform_index = int(os.environ.get(bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ຃"), bstack1l_opy_ (u"࠭࠰ࠨຄ")))
  else:
    bstack1l1lll1l1_opy_(bstack11ll1ll1l1_opy_)
  os.environ[bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨ຅")] = CONFIG[bstack1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪຆ")]
  os.environ[bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬງ")] = CONFIG[bstack1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ຈ")]
  os.environ[bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧຉ")] = bstack1lll1ll1l1_opy_.__str__()
  from _pytest.config import main as bstack1ll1l1ll1_opy_
  bstack11lll11ll_opy_ = []
  try:
    exit_code = bstack1ll1l1ll1_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack11l1ll1ll_opy_()
    if bstack1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵࠩຊ") in multiprocessing.current_process().__dict__.keys():
      for bstack111l1l1ll1_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11lll11ll_opy_.append(bstack111l1l1ll1_opy_)
    try:
      bstack11111lll11_opy_ = (bstack11lll11ll_opy_, int(exit_code))
      bstack1lllll1111_opy_.append(bstack11111lll11_opy_)
    except:
      bstack1lllll1111_opy_.append((bstack11lll11ll_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack11lll11ll_opy_.append({bstack1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ຋"): bstack1l_opy_ (u"ࠧࡑࡴࡲࡧࡪࡹࡳࠡࠩຌ") + os.environ.get(bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨຍ")), bstack1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨຎ"): traceback.format_exc(), bstack1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩຏ"): int(os.environ.get(bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫຐ")))})
    bstack1lllll1111_opy_.append((bstack11lll11ll_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack1l_opy_ (u"ࠧࡸࡥࡵࡴ࡬ࡩࡸࠨຑ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack1ll11ll11_opy_ = e.__class__.__name__
    print(bstack1l_opy_ (u"ࠨࠥࡴ࠼ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡵࡹࡳࡴࡩ࡯ࡩࠣࡦࡪ࡮ࡡࡷࡧࠣࡸࡪࡹࡴࠡࠧࡶࠦຒ") % (bstack1ll11ll11_opy_, e))
    return 1
def bstack1l1lllll1l_opy_(arg):
  global bstack1l1l1111l1_opy_
  bstack1l1lll1l1_opy_(bstack1l11ll1l1_opy_)
  os.environ[bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨຓ")] = str(bstack11l11111ll_opy_)
  retries = bstack11111l1l_opy_.bstack1111l1ll_opy_(CONFIG)
  status_code = 0
  if bstack11111l1l_opy_.bstack1llllll11_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack11l111ll1l_opy_
    status_code = bstack11l111ll1l_opy_(arg)
  if status_code != 0:
    bstack1l1l1111l1_opy_ = status_code
def bstack1l11llll11_opy_():
  logger.info(bstack1l1111l11l_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧດ"), help=bstack1l_opy_ (u"ࠩࡊࡩࡳ࡫ࡲࡢࡶࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡧࡴࡴࡦࡪࡩࠪຕ"))
  parser.add_argument(bstack1l_opy_ (u"ࠪ࠱ࡺ࠭ຖ"), bstack1l_opy_ (u"ࠫ࠲࠳ࡵࡴࡧࡵࡲࡦࡳࡥࠨທ"), help=bstack1l_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫຘ"))
  parser.add_argument(bstack1l_opy_ (u"࠭࠭࡬ࠩນ"), bstack1l_opy_ (u"ࠧ࠮࠯࡮ࡩࡾ࠭ບ"), help=bstack1l_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡧࡣࡤࡧࡶࡷࠥࡱࡥࡺࠩປ"))
  parser.add_argument(bstack1l_opy_ (u"ࠩ࠰ࡪࠬຜ"), bstack1l_opy_ (u"ࠪ࠱࠲࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨຝ"), help=bstack1l_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡷࡩࡸࡺࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪພ"))
  bstack111ll1l11_opy_ = parser.parse_args()
  try:
    bstack1l111ll1l1_opy_ = bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡮ࡦࡴ࡬ࡧ࠳ࡿ࡭࡭࠰ࡶࡥࡲࡶ࡬ࡦࠩຟ")
    if bstack111ll1l11_opy_.framework and bstack111ll1l11_opy_.framework not in (bstack1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ຠ"), bstack1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨມ")):
      bstack1l111ll1l1_opy_ = bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧຢ")
    bstack1lll1l11ll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l111ll1l1_opy_)
    bstack1lll11l1l1_opy_ = open(bstack1lll1l11ll_opy_, bstack1l_opy_ (u"ࠩࡵࠫຣ"))
    bstack111llll111_opy_ = bstack1lll11l1l1_opy_.read()
    bstack1lll11l1l1_opy_.close()
    if bstack111ll1l11_opy_.username:
      bstack111llll111_opy_ = bstack111llll111_opy_.replace(bstack1l_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪ຤"), bstack111ll1l11_opy_.username)
    if bstack111ll1l11_opy_.key:
      bstack111llll111_opy_ = bstack111llll111_opy_.replace(bstack1l_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭ລ"), bstack111ll1l11_opy_.key)
    if bstack111ll1l11_opy_.framework:
      bstack111llll111_opy_ = bstack111llll111_opy_.replace(bstack1l_opy_ (u"ࠬ࡟ࡏࡖࡔࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭຦"), bstack111ll1l11_opy_.framework)
    file_name = bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩວ")
    file_path = os.path.abspath(file_name)
    bstack1l1llll111_opy_ = open(file_path, bstack1l_opy_ (u"ࠧࡸࠩຨ"))
    bstack1l1llll111_opy_.write(bstack111llll111_opy_)
    bstack1l1llll111_opy_.close()
    logger.info(bstack1l1l11l1l_opy_)
    try:
      os.environ[bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪຩ")] = bstack111ll1l11_opy_.framework if bstack111ll1l11_opy_.framework != None else bstack1l_opy_ (u"ࠤࠥສ")
      config = yaml.safe_load(bstack111llll111_opy_)
      config[bstack1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪຫ")] = bstack1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠱ࡸ࡫ࡴࡶࡲࠪຬ")
      bstack1l11l111l_opy_(bstack1l11l11lll_opy_, config)
    except Exception as e:
      logger.debug(bstack11l11111l1_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack11l1ll11l_opy_.format(str(e)))
def bstack1l11l111l_opy_(bstack1l1llllll1_opy_, config, bstack11ll1lll11_opy_={}):
  global bstack1lll1ll1l1_opy_
  global bstack1ll1ll111_opy_
  global bstack1lll1ll1l_opy_
  if not config:
    return
  bstack11llllll11_opy_ = bstack1ll1l111ll_opy_ if not bstack1lll1ll1l1_opy_ else (
    bstack1llll11ll1_opy_ if bstack1l_opy_ (u"ࠬࡧࡰࡱࠩອ") in config else (
        bstack111ll1l1ll_opy_ if config.get(bstack1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪຮ")) else bstack1l11l1lll_opy_
    )
)
  bstack11lll1l1l_opy_ = False
  bstack1111l1111l_opy_ = False
  if bstack1lll1ll1l1_opy_ is True:
      if bstack1l_opy_ (u"ࠧࡢࡲࡳࠫຯ") in config:
          bstack11lll1l1l_opy_ = True
      else:
          bstack1111l1111l_opy_ = True
  bstack1111llll11_opy_ = bstack11l11ll111_opy_.bstack11l1llll11_opy_(config, bstack1ll1ll111_opy_)
  bstack1l1111ll1_opy_ = bstack11ll11lll_opy_()
  data = {
    bstack1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪະ"): config[bstack1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫັ")],
    bstack1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭າ"): config[bstack1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧຳ")],
    bstack1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩິ"): bstack1l1llllll1_opy_,
    bstack1l_opy_ (u"࠭ࡤࡦࡶࡨࡧࡹ࡫ࡤࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪີ"): os.environ.get(bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩຶ"), bstack1ll1ll111_opy_),
    bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪື"): bstack111l1l1l1l_opy_,
    bstack1l_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯ຸࠫ"): bstack111l11llll_opy_(),
    bstack1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸູ࠭"): {
      bstack1l_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬຺ࠩ"): str(config[bstack1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬົ")]) if bstack1l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ຼ") in config else bstack1l_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࠣຽ"),
      bstack1l_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧ࡙ࡩࡷࡹࡩࡰࡰࠪ຾"): sys.version,
      bstack1l_opy_ (u"ࠩࡵࡩ࡫࡫ࡲࡳࡧࡵࠫ຿"): bstack11ll11ll1l_opy_(os.environ.get(bstack1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬເ"), bstack1ll1ll111_opy_)),
      bstack1l_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭ແ"): bstack1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬໂ"),
      bstack1l_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧໃ"): bstack11llllll11_opy_,
      bstack1l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬໄ"): bstack1111llll11_opy_,
      bstack1l_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡡࡸࡹ࡮ࡪࠧ໅"): os.environ[bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧໆ")],
      bstack1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭໇"): os.environ.get(bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ່࠭"), bstack1ll1ll111_opy_),
      bstack1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ້"): bstack1ll1l1l11_opy_(os.environ.get(bstack1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ໊"), bstack1ll1ll111_opy_)),
      bstack1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ໋࠭"): bstack1l1111ll1_opy_.get(bstack1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭໌")),
      bstack1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨໍ"): bstack1l1111ll1_opy_.get(bstack1l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫ໎")),
      bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ໏"): config[bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ໐")] if config[bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ໑")] else bstack1l_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࠣ໒"),
      bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໓"): str(config[bstack1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ໔")]) if bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ໕") in config else bstack1l_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧ໖"),
      bstack1l_opy_ (u"ࠬࡵࡳࠨ໗"): sys.platform,
      bstack1l_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ໘"): socket.gethostname(),
      bstack1l_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ໙"): bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪ໚"))
    }
  }
  if not bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩ໛")) is None:
    data[bstack1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭ໜ")][bstack1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡓࡥࡵࡣࡧࡥࡹࡧࠧໝ")] = {
      bstack1l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬໞ"): bstack1l_opy_ (u"࠭ࡵࡴࡧࡵࡣࡰ࡯࡬࡭ࡧࡧࠫໟ"),
      bstack1l_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࠧ໠"): bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ໡")),
      bstack1l_opy_ (u"ࠩࡶ࡭࡬ࡴࡡ࡭ࡐࡸࡱࡧ࡫ࡲࠨ໢"): bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡒࡴ࠭໣"))
    }
  if bstack1l1llllll1_opy_ == bstack1ll11ll111_opy_:
    data[bstack1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ໤")][bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࠪ໥")] = bstack1111l1l1ll_opy_(config)
    data[bstack1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ໦")][bstack1l_opy_ (u"ࠧࡪࡵࡓࡩࡷࡩࡹࡂࡷࡷࡳࡊࡴࡡࡣ࡮ࡨࡨࠬ໧")] = percy.bstack11l11l11ll_opy_
    data[bstack1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໨")][bstack1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࡃࡷ࡬ࡰࡩࡏࡤࠨ໩")] = percy.percy_build_id
  if not bstack11111l1l_opy_.bstack1l1111111_opy_(CONFIG):
    data[bstack1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໪")][bstack1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠨ໫")] = bstack11111l1l_opy_.bstack1l1111111_opy_(CONFIG)
  bstack1llll111l_opy_ = bstack11111l11_opy_.bstack1llll11ll_opy_(CONFIG, logger)
  bstack1111l11l_opy_ = bstack11111l1l_opy_.bstack1llll11ll_opy_(config=CONFIG)
  if bstack1llll111l_opy_ is not None and bstack1111l11l_opy_ is not None and bstack1111l11l_opy_.bstack111lll11_opy_():
    data[bstack1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ໬")][bstack1111l11l_opy_.bstack11l1llll1l_opy_()] = bstack1llll111l_opy_.bstack11ll1111l1_opy_()
  update(data[bstack1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ໭")], bstack11ll1lll11_opy_)
  try:
    response = bstack1ll1llll11_opy_(bstack1l_opy_ (u"ࠧࡑࡑࡖࡘࠬ໮"), bstack11lllll11_opy_(bstack11ll1l1l1_opy_), data, {
      bstack1l_opy_ (u"ࠨࡣࡸࡸ࡭࠭໯"): (config[bstack1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ໰")], config[bstack1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭໱")])
    })
    if response:
      logger.debug(bstack111l1ll1l_opy_.format(bstack1l1llllll1_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1ll1ll111l_opy_.format(str(e)))
def bstack11ll11ll1l_opy_(framework):
  return bstack1l_opy_ (u"ࠦࢀࢃ࠭ࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴ࢁࡽࠣ໲").format(str(framework), __version__) if framework else bstack1l_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨ໳").format(
    __version__)
def bstack1l1ll1l11l_opy_():
  global CONFIG
  global bstack11lll1l11l_opy_
  if bool(CONFIG):
    return
  try:
    bstack111l1lll11_opy_()
    logger.debug(bstack1ll1l1111l_opy_.format(str(CONFIG)))
    bstack11lll1l11l_opy_ = bstack111ll1l1l_opy_.configure_logger(CONFIG, bstack11lll1l11l_opy_)
    bstack1111lllll1_opy_()
  except Exception as e:
    logger.error(bstack1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࡻࡰ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࠥ໴") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1l11l111ll_opy_
  atexit.register(bstack1l1l11111_opy_)
  signal.signal(signal.SIGINT, bstack11lll1ll1l_opy_)
  signal.signal(signal.SIGTERM, bstack11lll1ll1l_opy_)
def bstack1l11l111ll_opy_(exctype, value, traceback):
  global bstack1ll1ll1l11_opy_
  try:
    for driver in bstack1ll1ll1l11_opy_:
      bstack11111ll111_opy_(driver, bstack1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ໵"), bstack1l_opy_ (u"ࠣࡕࡨࡷࡸ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦ໶") + str(value))
  except Exception:
    pass
  logger.info(bstack1ll1lll1l1_opy_)
  bstack1111l11l1l_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1111l11l1l_opy_(message=bstack1l_opy_ (u"ࠩࠪ໷"), bstack1l11l1l111_opy_ = False):
  global CONFIG
  bstack11111l1lll_opy_ = bstack1l_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮ࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠬ໸") if bstack1l11l1l111_opy_ else bstack1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ໹")
  try:
    if message:
      bstack11ll1lll11_opy_ = {
        bstack11111l1lll_opy_ : str(message)
      }
      bstack1l11l111l_opy_(bstack1ll11ll111_opy_, CONFIG, bstack11ll1lll11_opy_)
    else:
      bstack1l11l111l_opy_(bstack1ll11ll111_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1ll11ll11l_opy_.format(str(e)))
def bstack1111llllll_opy_(bstack11l1l111ll_opy_, size):
  bstack111l1l1ll_opy_ = []
  while len(bstack11l1l111ll_opy_) > size:
    bstack1l1l1lll11_opy_ = bstack11l1l111ll_opy_[:size]
    bstack111l1l1ll_opy_.append(bstack1l1l1lll11_opy_)
    bstack11l1l111ll_opy_ = bstack11l1l111ll_opy_[size:]
  bstack111l1l1ll_opy_.append(bstack11l1l111ll_opy_)
  return bstack111l1l1ll_opy_
def bstack11l111ll1_opy_(args):
  if bstack1l_opy_ (u"ࠬ࠳࡭ࠨ໺") in args and bstack1l_opy_ (u"࠭ࡰࡥࡤࠪ໻") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack111l11l1l1_opy_, stage=STAGE.bstack1ll1lll11l_opy_)
def run_on_browserstack(bstack11111lll1_opy_=None, bstack1lllll1111_opy_=None, bstack1llll111ll_opy_=False):
  global CONFIG
  global bstack11l1ll1ll1_opy_
  global bstack11l11111ll_opy_
  global bstack1ll1ll111_opy_
  global bstack1lll1ll1l_opy_
  bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠧࠨ໼")
  bstack1lll11l11_opy_(bstack1111lll1l_opy_, logger)
  if bstack11111lll1_opy_ and isinstance(bstack11111lll1_opy_, str):
    bstack11111lll1_opy_ = eval(bstack11111lll1_opy_)
  if bstack11111lll1_opy_:
    CONFIG = bstack11111lll1_opy_[bstack1l_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨ໽")]
    bstack11l1ll1ll1_opy_ = bstack11111lll1_opy_[bstack1l_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪ໾")]
    bstack11l11111ll_opy_ = bstack11111lll1_opy_[bstack1l_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ໿")]
    bstack1lll1ll1l_opy_.set_property(bstack1l_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ༀ"), bstack11l11111ll_opy_)
    bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ༁")
  bstack1lll1ll1l_opy_.set_property(bstack1l_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ༂"), uuid4().__str__())
  logger.info(bstack1l_opy_ (u"ࠧࡔࡆࡎࠤࡷࡻ࡮ࠡࡵࡷࡥࡷࡺࡥࡥࠢࡺ࡭ࡹ࡮ࠠࡪࡦ࠽ࠤࠬ༃") + bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪ༄")));
  logger.debug(bstack1l_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࡁࠬ༅") + bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ༆")))
  if not bstack1llll111ll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1ll111l1l_opy_)
      return
    if sys.argv[1] == bstack1l_opy_ (u"ࠫ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧ༇") or sys.argv[1] == bstack1l_opy_ (u"ࠬ࠳ࡶࠨ༈"):
      logger.info(bstack1l_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡖࡹࡵࡪࡲࡲ࡙ࠥࡄࡌࠢࡹࡿࢂ࠭༉").format(__version__))
      return
    if sys.argv[1] == bstack1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭༊"):
      bstack1l11llll11_opy_()
      return
  args = sys.argv
  bstack1l1ll1l11l_opy_()
  global bstack1ll1l1ll11_opy_
  global bstack11lllll1ll_opy_
  global bstack11lll1ll1_opy_
  global bstack111l1l1l1_opy_
  global bstack1l11l11l1_opy_
  global bstack1111ll11ll_opy_
  global bstack1l111lllll_opy_
  global bstack11ll1llll1_opy_
  global bstack1111ll1l1_opy_
  global bstack1l11l11ll_opy_
  global bstack11l11l1l1l_opy_
  bstack11lllll1ll_opy_ = len(CONFIG.get(bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ་"), []))
  if not bstack1111lll11l_opy_:
    if args[1] == bstack1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༌") or args[1] == bstack1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫ།"):
      bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༎")
      args = args[2:]
    elif args[1] == bstack1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༏"):
      bstack1111lll11l_opy_ = bstack1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ༐")
      args = args[2:]
    elif args[1] == bstack1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭༑"):
      bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ༒")
      args = args[2:]
    elif args[1] == bstack1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ༓"):
      bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ༔")
      args = args[2:]
    elif args[1] == bstack1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༕"):
      bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ༖")
      args = args[2:]
    elif args[1] == bstack1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭༗"):
      bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫༘ࠧ")
      args = args[2:]
    else:
      if not bstack1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮༙ࠫ") in CONFIG or str(CONFIG[bstack1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ༚")]).lower() in [bstack1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༛"), bstack1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬ༜")]:
        bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ༝")
        args = args[1:]
      elif str(CONFIG[bstack1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༞")]).lower() == bstack1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭༟"):
        bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ༠")
        args = args[1:]
      elif str(CONFIG[bstack1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ༡")]).lower() == bstack1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ༢"):
        bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ༣")
        args = args[1:]
      elif str(CONFIG[bstack1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ༤")]).lower() == bstack1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭༥"):
        bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ༦")
        args = args[1:]
      elif str(CONFIG[bstack1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ༧")]).lower() == bstack1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ༨"):
        bstack1111lll11l_opy_ = bstack1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ༩")
        args = args[1:]
      else:
        os.environ[bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭༪")] = bstack1111lll11l_opy_
        bstack11lll11ll1_opy_(bstack1l1llll11_opy_)
  os.environ[bstack1l_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭༫")] = bstack1111lll11l_opy_
  bstack1ll1ll111_opy_ = bstack1111lll11l_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack111l111l1l_opy_ = bstack1l11ll111l_opy_[bstack1l_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙࠳ࡂࡅࡆࠪ༬")] if bstack1111lll11l_opy_ == bstack1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ༭") and bstack11ll1l1lll_opy_() else bstack1111lll11l_opy_
      bstack1l111l11l_opy_.invoke(Events.bstack11l1l111l1_opy_, bstack11l1ll111l_opy_(
        sdk_version=__version__,
        path_config=bstack111ll1l11l_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack111l111l1l_opy_,
        frameworks=[bstack111l111l1l_opy_],
        framework_versions={
          bstack111l111l1l_opy_: bstack1ll1l1l11_opy_(bstack1l_opy_ (u"ࠨࡔࡲࡦࡴࡺࠧ༮") if bstack1111lll11l_opy_ in [bstack1l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༯"), bstack1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ༰"), bstack1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ༱")] else bstack1111lll11l_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢ༲"), None):
        CONFIG[bstack1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ༳")] = cli.config.get(bstack1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤ༴"), None)
    except Exception as e:
      bstack1l111l11l_opy_.invoke(Events.bstack1111ll1l1l_opy_, e.__traceback__, 1)
    if bstack11l11111ll_opy_:
      CONFIG[bstack1l_opy_ (u"ࠣࡣࡳࡴ༵ࠧ")] = cli.config[bstack1l_opy_ (u"ࠤࡤࡴࡵࠨ༶")]
      logger.info(bstack11lll1111l_opy_.format(CONFIG[bstack1l_opy_ (u"ࠪࡥࡵࡶ༷ࠧ")]))
  else:
    bstack1l111l11l_opy_.clear()
  global bstack1ll11111l_opy_
  global bstack1ll1l111l1_opy_
  if bstack11111lll1_opy_:
    try:
      bstack1l1111lll_opy_ = datetime.datetime.now()
      os.environ[bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭༸")] = bstack1111lll11l_opy_
      bstack1l11l111l_opy_(bstack11l1l1l11l_opy_, CONFIG)
      cli.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽ࡷࡩࡱ࡟ࡵࡧࡶࡸࡤࡧࡴࡵࡧࡰࡴࡹ࡫ࡤ༹ࠣ"), datetime.datetime.now() - bstack1l1111lll_opy_)
    except Exception as e:
      logger.debug(bstack11l1111111_opy_.format(str(e)))
  global bstack1ll1ll1ll1_opy_
  global bstack111l11ll11_opy_
  global bstack11l1l11ll_opy_
  global bstack1l11l1111l_opy_
  global bstack11ll111ll_opy_
  global bstack11llllll1l_opy_
  global bstack11l11ll1l_opy_
  global bstack1lll111l11_opy_
  global bstack1l1l11l111_opy_
  global bstack1111ll1lll_opy_
  global bstack111lll11l_opy_
  global bstack11ll1llll_opy_
  global bstack11l111llll_opy_
  global bstack1111ll11l1_opy_
  global bstack1ll1l1l1ll_opy_
  global bstack1l1ll1l1ll_opy_
  global bstack1l1111111l_opy_
  global bstack11l1l111l_opy_
  global bstack1l1l1111ll_opy_
  global bstack1l1111l11_opy_
  global bstack11ll1l1l11_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll1ll1ll1_opy_ = webdriver.Remote.__init__
    bstack111l11ll11_opy_ = WebDriver.quit
    bstack11ll1llll_opy_ = WebDriver.close
    bstack1ll1l1l1ll_opy_ = WebDriver.get
    bstack11ll1l1l11_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1ll11111l_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack111lll111_opy_
    bstack1ll1l111l1_opy_ = bstack111lll111_opy_()
  except Exception as e:
    pass
  try:
    global bstack11llll11l_opy_
    from QWeb.keywords import browser
    bstack11llll11l_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack111l1l11ll_opy_(CONFIG) and bstack11l11l1l11_opy_():
    if bstack1lll1lll1l_opy_() < version.parse(bstack11l1lll11_opy_):
      logger.error(bstack11ll1lll1_opy_.format(bstack1lll1lll1l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1l_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ༺")) and callable(getattr(RemoteConnection, bstack1l_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ༻"))):
          RemoteConnection._get_proxy_url = bstack111ll1111l_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack111ll1111l_opy_
      except Exception as e:
        logger.error(bstack1ll1ll11ll_opy_.format(str(e)))
  if not CONFIG.get(bstack1l_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪ༼"), False) and not bstack11111lll1_opy_:
    logger.info(bstack1llll11l11_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭༽") in CONFIG and str(CONFIG[bstack1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ༾")]).lower() != bstack1l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ༿"):
      bstack1ll111ll11_opy_()
    elif bstack1111lll11l_opy_ != bstack1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬཀ") or (bstack1111lll11l_opy_ == bstack1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ཁ") and not bstack11111lll1_opy_):
      bstack11111l1ll1_opy_()
  if (bstack1111lll11l_opy_ in [bstack1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ག"), bstack1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧགྷ"), bstack1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪང")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack11l1ll1l1_opy_
        bstack11llllll1l_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack11lll11l1l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack11ll111ll_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack11llll1ll1_opy_ + str(e))
    except Exception as e:
      bstack1l1111l1l1_opy_(e, bstack11lll11l1l_opy_)
    if bstack1111lll11l_opy_ != bstack1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫཅ"):
      bstack11l1llll1_opy_()
    bstack11l1l11ll_opy_ = Output.start_test
    bstack1l11l1111l_opy_ = Output.end_test
    bstack11l11ll1l_opy_ = TestStatus.__init__
    bstack1l1l11l111_opy_ = pabot._run
    bstack1111ll1lll_opy_ = QueueItem.__init__
    bstack111lll11l_opy_ = pabot._create_command_for_execution
    bstack1l1l1111ll_opy_ = pabot._report_results
  if bstack1111lll11l_opy_ == bstack1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫཆ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1111l1l1_opy_(e, bstack1l1l1ll1ll_opy_)
    bstack11l111llll_opy_ = Runner.run_hook
    bstack1111ll11l1_opy_ = Step.run
  if bstack1111lll11l_opy_ == bstack1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཇ"):
    try:
      from _pytest.config import Config
      bstack1l1111111l_opy_ = Config.getoption
      from _pytest import runner
      bstack11l1l111l_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack11111111_opy_)
    try:
      from pytest_bdd import reporting
      bstack1l1111l11_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹࡵࠠࡳࡷࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࡹࠧ཈"))
  try:
    framework_name = bstack1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ཉ") if bstack1111lll11l_opy_ in [bstack1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧཊ"), bstack1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨཋ"), bstack1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫཌ")] else bstack11lll1l1ll_opy_(bstack1111lll11l_opy_)
    bstack11ll1l1ll1_opy_ = {
      bstack1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࠬཌྷ"): bstack1l_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧཎ") if bstack1111lll11l_opy_ == bstack1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ཏ") and bstack11ll1l1lll_opy_() else framework_name,
      bstack1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫཐ"): bstack1ll1l1l11_opy_(framework_name),
      bstack1l_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ད"): __version__,
      bstack1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪདྷ"): bstack1111lll11l_opy_
    }
    if bstack1111lll11l_opy_ in bstack1l11l111l1_opy_ + bstack11l11l1111_opy_:
      if bstack11111ll1_opy_.bstack11111111l_opy_(CONFIG):
        if bstack1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪན") in CONFIG:
          os.environ[bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬཔ")] = os.getenv(bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ཕ"), json.dumps(CONFIG[bstack1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭བ")]))
          CONFIG[bstack1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧབྷ")].pop(bstack1l_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭མ"), None)
          CONFIG[bstack1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩཙ")].pop(bstack1l_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨཚ"), None)
        bstack11ll1l1ll1_opy_[bstack1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫཛ")] = {
          bstack1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪཛྷ"): bstack1l_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨཝ"),
          bstack1l_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨཞ"): str(bstack1lll1lll1l_opy_())
        }
    if bstack1111lll11l_opy_ not in [bstack1l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩཟ")] and not cli.is_running():
      bstack111l1l1l11_opy_, bstack111llllll_opy_ = bstack1ll1lll1_opy_.launch(CONFIG, bstack11ll1l1ll1_opy_)
      if bstack111llllll_opy_.get(bstack1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩའ")) is not None and bstack11111ll1_opy_.bstack1llll1ll1l_opy_(CONFIG) is None:
        value = bstack111llllll_opy_[bstack1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪཡ")].get(bstack1l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬར"))
        if value is not None:
            CONFIG[bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬལ")] = value
        else:
          logger.debug(bstack1l_opy_ (u"ࠨࡎࡰࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡧࡥࡹࡧࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠦཤ"))
  except Exception as e:
    logger.debug(bstack1l1111ll11_opy_.format(bstack1l_opy_ (u"ࠧࡕࡧࡶࡸࡍࡻࡢࠨཥ"), str(e)))
  if bstack1111lll11l_opy_ == bstack1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨས"):
    bstack11lll1ll1_opy_ = True
    if bstack11111lll1_opy_ and bstack1llll111ll_opy_:
      bstack1111ll11ll_opy_ = CONFIG.get(bstack1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ཧ"), {}).get(bstack1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬཨ"))
      bstack1l1lll1l1_opy_(bstack1l11l1ll1_opy_)
    elif bstack11111lll1_opy_:
      bstack1111ll11ll_opy_ = CONFIG.get(bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨཀྵ"), {}).get(bstack1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧཪ"))
      global bstack1ll1ll1l11_opy_
      try:
        if bstack11l111ll1_opy_(bstack11111lll1_opy_[bstack1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩཫ")]) and multiprocessing.current_process().name == bstack1l_opy_ (u"ࠧ࠱ࠩཬ"):
          bstack11111lll1_opy_[bstack1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ཭")].remove(bstack1l_opy_ (u"ࠩ࠰ࡱࠬ཮"))
          bstack11111lll1_opy_[bstack1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭཯")].remove(bstack1l_opy_ (u"ࠫࡵࡪࡢࠨ཰"))
          bstack11111lll1_opy_[bstack1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཱ")] = bstack11111lll1_opy_[bstack1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦིࠩ")][0]
          with open(bstack11111lll1_opy_[bstack1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧཱིࠪ")], bstack1l_opy_ (u"ࠨࡴུࠪ")) as f:
            file_content = f.read()
          bstack1ll1111l1l_opy_ = bstack1l_opy_ (u"ࠤࠥࠦ࡫ࡸ࡯࡮ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡧ࡯ࠥ࡯࡭ࡱࡱࡵࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡥ࠼ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩ࠭ࢁࡽࠪ࠽ࠣࡪࡷࡵ࡭ࠡࡲࡧࡦࠥ࡯࡭ࡱࡱࡵࡸࠥࡖࡤࡣ࠽ࠣࡳ࡬ࡥࡤࡣࠢࡀࠤࡕࡪࡢ࠯ࡦࡲࡣࡧࡸࡥࡢ࡭࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥࡧࡩࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠨࡴࡧ࡯ࡪ࠱ࠦࡡࡳࡩ࠯ࠤࡹ࡫࡭ࡱࡱࡵࡥࡷࡿࠠ࠾ࠢ࠳࠭࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡹࡸࡹ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡤࡶ࡬ࠦ࠽ࠡࡵࡷࡶ࠭࡯࡮ࡵࠪࡤࡶ࡬࠯ࠫ࠲࠲ࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡨࡼࡨ࡫ࡰࡵࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡧࡳࠡࡧ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡵࡧࡳࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡰࡩࡢࡨࡧ࠮ࡳࡦ࡮ࡩ࠰ࡦࡸࡧ࠭ࡶࡨࡱࡵࡵࡲࡢࡴࡼ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࠣࡁࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡕࡪࡢ࠯ࡦࡲࡣࡧࡸࡥࡢ࡭ࠣࡁࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡕࡪࡢࠩࠫ࠱ࡷࡪࡺ࡟ࡵࡴࡤࡧࡪ࠮ࠩ࡝ࡰཱུࠥࠦࠧ").format(str(bstack11111lll1_opy_))
          bstack11111l11l_opy_ = bstack1ll1111l1l_opy_ + file_content
          bstack11lll11l1_opy_ = bstack11111lll1_opy_[bstack1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྲྀ")] + bstack1l_opy_ (u"ࠫࡤࡨࡳࡵࡣࡦ࡯ࡤࡺࡥ࡮ࡲ࠱ࡴࡾ࠭ཷ")
          with open(bstack11lll11l1_opy_, bstack1l_opy_ (u"ࠬࡽࠧླྀ")):
            pass
          with open(bstack11lll11l1_opy_, bstack1l_opy_ (u"ࠨࡷࠬࠤཹ")) as f:
            f.write(bstack11111l11l_opy_)
          import subprocess
          process_data = subprocess.run([bstack1l_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴེࠢ"), bstack11lll11l1_opy_])
          if os.path.exists(bstack11lll11l1_opy_):
            os.unlink(bstack11lll11l1_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack11l111ll1_opy_(bstack11111lll1_opy_[bstack1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨཻࠫ")]):
            bstack11111lll1_opy_[bstack1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩོࠬ")].remove(bstack1l_opy_ (u"ࠪ࠱ࡲཽ࠭"))
            bstack11111lll1_opy_[bstack1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཾ")].remove(bstack1l_opy_ (u"ࠬࡶࡤࡣࠩཿ"))
            bstack11111lll1_opy_[bstack1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦྀࠩ")] = bstack11111lll1_opy_[bstack1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧཱྀࠪ")][0]
          bstack1l1lll1l1_opy_(bstack1l11l1ll1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack11111lll1_opy_[bstack1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྂ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1l_opy_ (u"ࠩࡢࡣࡳࡧ࡭ࡦࡡࡢࠫྃ")] = bstack1l_opy_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣ྄ࠬ")
          mod_globals[bstack1l_opy_ (u"ࠫࡤࡥࡦࡪ࡮ࡨࡣࡤ࠭྅")] = os.path.abspath(bstack11111lll1_opy_[bstack1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ྆")])
          exec(open(bstack11111lll1_opy_[bstack1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ྇")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1l_opy_ (u"ࠧࡄࡣࡸ࡫࡭ࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠧྈ").format(str(e)))
          for driver in bstack1ll1ll1l11_opy_:
            bstack1lllll1111_opy_.append({
              bstack1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ྉ"): bstack11111lll1_opy_[bstack1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྊ")],
              bstack1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩྋ"): str(e),
              bstack1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪྌ"): multiprocessing.current_process().name
            })
            bstack11111ll111_opy_(driver, bstack1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬྍ"), bstack1l_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤྎ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1ll1ll1l11_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11l11111ll_opy_, CONFIG, logger)
      bstack1l1l1l1ll1_opy_()
      bstack111l1ll11l_opy_()
      percy.bstack1l11111111_opy_()
      bstack1lllll1l1_opy_ = {
        bstack1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྏ"): args[0],
        bstack1l_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨྐ"): CONFIG,
        bstack1l_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪྑ"): bstack11l1ll1ll1_opy_,
        bstack1l_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬྒ"): bstack11l11111ll_opy_
      }
      if bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྒྷ") in CONFIG:
        bstack1l1ll111ll_opy_ = bstack1l1l11l1l1_opy_(args, logger, CONFIG, bstack1lll1ll1l1_opy_, bstack11lllll1ll_opy_)
        bstack11ll1llll1_opy_ = bstack1l1ll111ll_opy_.bstack11l11ll1_opy_(run_on_browserstack, bstack1lllll1l1_opy_, bstack11l111ll1_opy_(args))
      else:
        if bstack11l111ll1_opy_(args):
          bstack1lllll1l1_opy_[bstack1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྔ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1lllll1l1_opy_,))
          test.start()
          test.join()
        else:
          bstack1l1lll1l1_opy_(bstack1l11l1ll1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1l_opy_ (u"࠭࡟ࡠࡰࡤࡱࡪࡥ࡟ࠨྕ")] = bstack1l_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩྖ")
          mod_globals[bstack1l_opy_ (u"ࠨࡡࡢࡪ࡮ࡲࡥࡠࡡࠪྗ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1111lll11l_opy_ == bstack1l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ྘") or bstack1111lll11l_opy_ == bstack1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩྙ"):
    percy.init(bstack11l11111ll_opy_, CONFIG, logger)
    percy.bstack1l11111111_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l1111l1l1_opy_(e, bstack11lll11l1l_opy_)
    bstack1l1l1l1ll1_opy_()
    bstack1l1lll1l1_opy_(bstack11l11l1lll_opy_)
    if bstack1lll1ll1l1_opy_:
      bstack11ll1ll111_opy_(bstack11l11l1lll_opy_, args)
      if bstack1l_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩྚ") in args:
        i = args.index(bstack1l_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪྛ"))
        args.pop(i)
        args.pop(i)
      if bstack1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩྜ") not in CONFIG:
        CONFIG[bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪྜྷ")] = [{}]
        bstack11lllll1ll_opy_ = 1
      if bstack1ll1l1ll11_opy_ == 0:
        bstack1ll1l1ll11_opy_ = 1
      args.insert(0, str(bstack1ll1l1ll11_opy_))
      args.insert(0, str(bstack1l_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ྞ")))
    if bstack1ll1lll1_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1l1llll1l_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1111ll11l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1l_opy_ (u"ࠤࡕࡓࡇࡕࡔࡠࡑࡓࡘࡎࡕࡎࡔࠤྟ"),
        ).parse_args(bstack1l1llll1l_opy_)
        bstack1l1l111111_opy_ = args.index(bstack1l1llll1l_opy_[0]) if len(bstack1l1llll1l_opy_) > 0 else len(args)
        args.insert(bstack1l1l111111_opy_, str(bstack1l_opy_ (u"ࠪ࠱࠲ࡲࡩࡴࡶࡨࡲࡪࡸࠧྠ")))
        args.insert(bstack1l1l111111_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡷࡵࡢࡰࡶࡢࡰ࡮ࡹࡴࡦࡰࡨࡶ࠳ࡶࡹࠨྡ"))))
        if bstack11111l1l_opy_.bstack1llllll11_opy_(CONFIG):
          args.insert(bstack1l1l111111_opy_, str(bstack1l_opy_ (u"ࠬ࠳࠭࡭࡫ࡶࡸࡪࡴࡥࡳࠩྡྷ")))
          args.insert(bstack1l1l111111_opy_ + 1, str(bstack1l_opy_ (u"࠭ࡒࡦࡶࡵࡽࡋࡧࡩ࡭ࡧࡧ࠾ࢀࢃࠧྣ").format(bstack11111l1l_opy_.bstack1111l1ll_opy_(CONFIG))))
        if bstack1l11l1ll1l_opy_(os.environ.get(bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠬྤ"))) and str(os.environ.get(bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬྥ"), bstack1l_opy_ (u"ࠩࡱࡹࡱࡲࠧྦ"))) != bstack1l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨྦྷ"):
          for bstack1l11lll11l_opy_ in bstack1111ll11l_opy_:
            args.remove(bstack1l11lll11l_opy_)
          test_files = os.environ.get(bstack1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠨྨ")).split(bstack1l_opy_ (u"ࠬ࠲ࠧྩ"))
          for bstack11l1l11l_opy_ in test_files:
            args.append(bstack11l1l11l_opy_)
      except Exception as e:
        logger.error(bstack1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡦࡺࡴࡢࡥ࡫࡭ࡳ࡭ࠠ࡭࡫ࡶࡸࡪࡴࡥࡳࠢࡩࡳࡷࠦࡻࡾ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠰ࠤࢀࢃࠢྪ").format(bstack1ll1lll111_opy_, e))
    pabot.main(args)
  elif bstack1111lll11l_opy_ == bstack1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨྫ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l1111l1l1_opy_(e, bstack11lll11l1l_opy_)
    for a in args:
      if bstack1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞ࠧྫྷ") in a:
        bstack1l11l11l1_opy_ = int(a.split(bstack1l_opy_ (u"ࠩ࠽ࠫྭ"))[1])
      if bstack1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧྮ") in a:
        bstack1111ll11ll_opy_ = str(a.split(bstack1l_opy_ (u"ࠫ࠿࠭ྯ"))[1])
      if bstack1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬྰ") in a:
        bstack1l111lllll_opy_ = str(a.split(bstack1l_opy_ (u"࠭࠺ࠨྱ"))[1])
    bstack1111l11l1_opy_ = None
    if bstack1l_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭ྲ") in args:
      i = args.index(bstack1l_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠧླ"))
      args.pop(i)
      bstack1111l11l1_opy_ = args.pop(i)
    if bstack1111l11l1_opy_ is not None:
      global bstack11ll1lllll_opy_
      bstack11ll1lllll_opy_ = bstack1111l11l1_opy_
    bstack1l1lll1l1_opy_(bstack11l11l1lll_opy_)
    run_cli(args)
    if bstack1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭ྴ") in multiprocessing.current_process().__dict__.keys():
      for bstack111l1l1ll1_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1lllll1111_opy_.append(bstack111l1l1ll1_opy_)
  elif bstack1111lll11l_opy_ == bstack1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪྵ"):
    bstack111ll111l_opy_ = bstack111111l1_opy_(args, logger, CONFIG, bstack1lll1ll1l1_opy_)
    bstack111ll111l_opy_.bstack111l11l1_opy_()
    bstack1l1l1l1ll1_opy_()
    bstack111l1l1l1_opy_ = True
    bstack1l11l11ll_opy_ = bstack111ll111l_opy_.bstack1lll1llll_opy_()
    bstack111ll111l_opy_.bstack1lllll1l1_opy_(bstack1l1lll1ll1_opy_)
    bstack111ll111l_opy_.bstack111ll1ll_opy_()
    bstack11111llll1_opy_(bstack1111lll11l_opy_, CONFIG, bstack111ll111l_opy_.bstack111lllll_opy_())
    bstack1l11ll1l1l_opy_ = bstack111ll111l_opy_.bstack11l11ll1_opy_(bstack111l1111l_opy_, {
      bstack1l_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬྶ"): bstack11l1ll1ll1_opy_,
      bstack1l_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧྷ"): bstack11l11111ll_opy_,
      bstack1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩྸ"): bstack1lll1ll1l1_opy_
    })
    try:
      bstack11lll11ll_opy_, bstack1l11lll1l1_opy_ = map(list, zip(*bstack1l11ll1l1l_opy_))
      bstack1111ll1l1_opy_ = bstack11lll11ll_opy_[0]
      for status_code in bstack1l11lll1l1_opy_:
        if status_code != 0:
          bstack11l11l1l1l_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡦࡼࡥࠡࡧࡵࡶࡴࡸࡳࠡࡣࡱࡨࠥࡹࡴࡢࡶࡸࡷࠥࡩ࡯ࡥࡧ࠱ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠ࠻ࠢࡾࢁࠧྐྵ").format(str(e)))
  elif bstack1111lll11l_opy_ == bstack1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨྺ"):
    try:
      from behave.__main__ import main as bstack11l111ll1l_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l1111l1l1_opy_(e, bstack1l1l1ll1ll_opy_)
    bstack1l1l1l1ll1_opy_()
    bstack111l1l1l1_opy_ = True
    bstack11l11l11_opy_ = 1
    if bstack1l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩྻ") in CONFIG:
      bstack11l11l11_opy_ = CONFIG[bstack1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪྼ")]
    if bstack1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ྽") in CONFIG:
      bstack1111ll1ll_opy_ = int(bstack11l11l11_opy_) * int(len(CONFIG[bstack1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ྾")]))
    else:
      bstack1111ll1ll_opy_ = int(bstack11l11l11_opy_)
    config = Configuration(args)
    bstack1l111l11ll_opy_ = config.paths
    if len(bstack1l111l11ll_opy_) == 0:
      import glob
      pattern = bstack1l_opy_ (u"࠭ࠪࠫ࠱࠭࠲࡫࡫ࡡࡵࡷࡵࡩࠬ྿")
      bstack11l1lll1l1_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11l1lll1l1_opy_)
      config = Configuration(args)
      bstack1l111l11ll_opy_ = config.paths
    bstack11l11l1l_opy_ = [os.path.normpath(item) for item in bstack1l111l11ll_opy_]
    bstack1l1l1l11l1_opy_ = [os.path.normpath(item) for item in args]
    bstack1lll1lllll_opy_ = [item for item in bstack1l1l1l11l1_opy_ if item not in bstack11l11l1l_opy_]
    import platform as pf
    if pf.system().lower() == bstack1l_opy_ (u"ࠧࡸ࡫ࡱࡨࡴࡽࡳࠨ࿀"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack11l11l1l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1l11l11l1l_opy_)))
                    for bstack1l11l11l1l_opy_ in bstack11l11l1l_opy_]
    bstack1111ll11_opy_ = []
    for spec in bstack11l11l1l_opy_:
      bstack1llll1ll1_opy_ = []
      bstack1llll1ll1_opy_ += bstack1lll1lllll_opy_
      bstack1llll1ll1_opy_.append(spec)
      bstack1111ll11_opy_.append(bstack1llll1ll1_opy_)
    execution_items = []
    for bstack1llll1ll1_opy_ in bstack1111ll11_opy_:
      if bstack1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ࿁") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ࿂")]):
          item = {}
          item[bstack1l_opy_ (u"ࠪࡥࡷ࡭ࠧ࿃")] = bstack1l_opy_ (u"ࠫࠥ࠭࿄").join(bstack1llll1ll1_opy_)
          item[bstack1l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ࿅")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack1l_opy_ (u"࠭ࡡࡳࡩ࿆ࠪ")] = bstack1l_opy_ (u"ࠧࠡࠩ࿇").join(bstack1llll1ll1_opy_)
        item[bstack1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ࿈")] = 0
        execution_items.append(item)
    bstack111l1llll1_opy_ = bstack1111llllll_opy_(execution_items, bstack1111ll1ll_opy_)
    for execution_item in bstack111l1llll1_opy_:
      bstack1111111l_opy_ = []
      for item in execution_item:
        bstack1111111l_opy_.append(bstack11l11l111_opy_(name=str(item[bstack1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ࿉")]),
                                             target=bstack1l1lllll1l_opy_,
                                             args=(item[bstack1l_opy_ (u"ࠪࡥࡷ࡭ࠧ࿊")],)))
      for t in bstack1111111l_opy_:
        t.start()
      for t in bstack1111111l_opy_:
        t.join()
  else:
    bstack11lll11ll1_opy_(bstack1l1llll11_opy_)
  if not bstack11111lll1_opy_:
    bstack11ll111l1_opy_()
    if(bstack1111lll11l_opy_ in [bstack1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ࿋"), bstack1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ࿌")]):
      bstack1l1l111lll_opy_()
  bstack111ll1l1l_opy_.bstack1l1l1ll11l_opy_()
def browserstack_initialize(bstack1ll1l11l1l_opy_=None):
  logger.info(bstack1l_opy_ (u"࠭ࡒࡶࡰࡱ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡼ࡯ࡴࡩࠢࡤࡶ࡬ࡹ࠺ࠡࠩ࿍") + str(bstack1ll1l11l1l_opy_))
  run_on_browserstack(bstack1ll1l11l1l_opy_, None, True)
@measure(event_name=EVENTS.bstack11l111ll11_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack11ll111l1_opy_():
  global CONFIG
  global bstack1ll1ll111_opy_
  global bstack11l11l1l1l_opy_
  global bstack1l1l1111l1_opy_
  global bstack1lll1ll1l_opy_
  bstack111llll1l1_opy_.bstack1l111l1l1l_opy_()
  if cli.is_running():
    bstack1l111l11l_opy_.invoke(Events.bstack11l1ll111_opy_)
  else:
    bstack1111l11l_opy_ = bstack11111l1l_opy_.bstack1llll11ll_opy_(config=CONFIG)
    bstack1111l11l_opy_.bstack111l1l11l_opy_(CONFIG)
  if bstack1ll1ll111_opy_ == bstack1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ࿎"):
    if not cli.is_enabled(CONFIG):
      bstack1ll1lll1_opy_.stop()
  else:
    bstack1ll1lll1_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack11lll1l1_opy_.bstack1l1ll11111_opy_()
  if bstack1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ࿏") in CONFIG and str(CONFIG[bstack1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭࿐")]).lower() != bstack1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ࿑"):
    hashed_id, bstack1l1l11l11_opy_ = bstack11111ll1l_opy_()
  else:
    hashed_id, bstack1l1l11l11_opy_ = get_build_link()
  bstack1ll11l11ll_opy_(hashed_id)
  logger.info(bstack1l_opy_ (u"ࠫࡘࡊࡋࠡࡴࡸࡲࠥ࡫࡮ࡥࡧࡧࠤ࡫ࡵࡲࠡ࡫ࡧ࠾ࠬ࿒") + bstack1lll1ll1l_opy_.get_property(bstack1l_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ࿓"), bstack1l_opy_ (u"࠭ࠧ࿔")) + bstack1l_opy_ (u"ࠧ࠭ࠢࡷࡩࡸࡺࡨࡶࡤࠣ࡭ࡩࡀࠠࠨ࿕") + os.getenv(bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭࿖"), bstack1l_opy_ (u"ࠩࠪ࿗")))
  if hashed_id is not None and bstack11l1l11lll_opy_() != -1:
    sessions = bstack1ll1ll1l1_opy_(hashed_id)
    bstack11l1l1l1ll_opy_(sessions, bstack1l1l11l11_opy_)
  if bstack1ll1ll111_opy_ == bstack1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ࿘") and bstack11l11l1l1l_opy_ != 0:
    sys.exit(bstack11l11l1l1l_opy_)
  if bstack1ll1ll111_opy_ == bstack1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ࿙") and bstack1l1l1111l1_opy_ != 0:
    sys.exit(bstack1l1l1111l1_opy_)
def bstack1ll11l11ll_opy_(new_id):
    global bstack111l1l1l1l_opy_
    bstack111l1l1l1l_opy_ = new_id
def bstack11lll1l1ll_opy_(bstack11l11lll1l_opy_):
  if bstack11l11lll1l_opy_:
    return bstack11l11lll1l_opy_.capitalize()
  else:
    return bstack1l_opy_ (u"ࠬ࠭࿚")
@measure(event_name=EVENTS.bstack1ll11ll1l1_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack1lll1ll11l_opy_(bstack1l1l1l1111_opy_):
  if bstack1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ࿛") in bstack1l1l1l1111_opy_ and bstack1l1l1l1111_opy_[bstack1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ࿜")] != bstack1l_opy_ (u"ࠨࠩ࿝"):
    return bstack1l1l1l1111_opy_[bstack1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ࿞")]
  else:
    bstack1l1ll1ll1_opy_ = bstack1l_opy_ (u"ࠥࠦ࿟")
    if bstack1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ࿠") in bstack1l1l1l1111_opy_ and bstack1l1l1l1111_opy_[bstack1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ࿡")] != None:
      bstack1l1ll1ll1_opy_ += bstack1l1l1l1111_opy_[bstack1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭࿢")] + bstack1l_opy_ (u"ࠢ࠭ࠢࠥ࿣")
      if bstack1l1l1l1111_opy_[bstack1l_opy_ (u"ࠨࡱࡶࠫ࿤")] == bstack1l_opy_ (u"ࠤ࡬ࡳࡸࠨ࿥"):
        bstack1l1ll1ll1_opy_ += bstack1l_opy_ (u"ࠥ࡭ࡔ࡙ࠠࠣ࿦")
      bstack1l1ll1ll1_opy_ += (bstack1l1l1l1111_opy_[bstack1l_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ࿧")] or bstack1l_opy_ (u"ࠬ࠭࿨"))
      return bstack1l1ll1ll1_opy_
    else:
      bstack1l1ll1ll1_opy_ += bstack11lll1l1ll_opy_(bstack1l1l1l1111_opy_[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧ࿩")]) + bstack1l_opy_ (u"ࠢࠡࠤ࿪") + (
              bstack1l1l1l1111_opy_[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ࿫")] or bstack1l_opy_ (u"ࠩࠪ࿬")) + bstack1l_opy_ (u"ࠥ࠰ࠥࠨ࿭")
      if bstack1l1l1l1111_opy_[bstack1l_opy_ (u"ࠫࡴࡹࠧ࿮")] == bstack1l_opy_ (u"ࠧ࡝ࡩ࡯ࡦࡲࡻࡸࠨ࿯"):
        bstack1l1ll1ll1_opy_ += bstack1l_opy_ (u"ࠨࡗࡪࡰࠣࠦ࿰")
      bstack1l1ll1ll1_opy_ += bstack1l1l1l1111_opy_[bstack1l_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫ࿱")] or bstack1l_opy_ (u"ࠨࠩ࿲")
      return bstack1l1ll1ll1_opy_
@measure(event_name=EVENTS.bstack1l11ll1ll_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack11l111l1ll_opy_(bstack11l111l11_opy_):
  if bstack11l111l11_opy_ == bstack1l_opy_ (u"ࠤࡧࡳࡳ࡫ࠢ࿳"):
    return bstack1l_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿࡭ࡲࡦࡧࡱ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧ࡭ࡲࡦࡧࡱࠦࡃࡉ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭࿴")
  elif bstack11l111l11_opy_ == bstack1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ࿵"):
    return bstack1l_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡳࡧࡧ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡸࡥࡥࠤࡁࡊࡦ࡯࡬ࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ࿶")
  elif bstack11l111l11_opy_ == bstack1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ࿷"):
    return bstack1l_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡪࡶࡪ࡫࡮࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡪࡶࡪ࡫࡮ࠣࡀࡓࡥࡸࡹࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ࿸")
  elif bstack11l111l11_opy_ == bstack1l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢ࿹"):
    return bstack1l_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡷ࡫ࡤ࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡵࡩࡩࠨ࠾ࡆࡴࡵࡳࡷࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ࿺")
  elif bstack11l111l11_opy_ == bstack1l_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࠦ࿻"):
    return bstack1l_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࠣࡦࡧࡤ࠷࠷࠼࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࠥࡨࡩࡦ࠹࠲࠷ࠤࡁࡘ࡮ࡳࡥࡰࡷࡷࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ࿼")
  elif bstack11l111l11_opy_ == bstack1l_opy_ (u"ࠧࡸࡵ࡯ࡰ࡬ࡲ࡬ࠨ࿽"):
    return bstack1l_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡤ࡯ࡥࡨࡱ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡤ࡯ࡥࡨࡱࠢ࠿ࡔࡸࡲࡳ࡯࡮ࡨ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ࿾")
  else:
    return bstack1l_opy_ (u"ࠧ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡦࡱࡧࡣ࡬࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡦࡱࡧࡣ࡬ࠤࡁࠫ࿿") + bstack11lll1l1ll_opy_(
      bstack11l111l11_opy_) + bstack1l_opy_ (u"ࠨ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧက")
def bstack1lll111l1_opy_(session):
  return bstack1l_opy_ (u"ࠩ࠿ࡸࡷࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡲࡰࡹࠥࡂࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠦࡳࡦࡵࡶ࡭ࡴࡴ࠭࡯ࡣࡰࡩࠧࡄ࠼ࡢࠢ࡫ࡶࡪ࡬࠽ࠣࡽࢀࠦࠥࡺࡡࡳࡩࡨࡸࡂࠨ࡟ࡣ࡮ࡤࡲࡰࠨ࠾ࡼࡿ࠿࠳ࡦࡄ࠼࠰ࡶࡧࡂࢀࢃࡻࡾ࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀ࠴ࡺࡲ࠿ࠩခ").format(
    session[bstack1l_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧဂ")], bstack1lll1ll11l_opy_(session), bstack11l111l1ll_opy_(session[bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡷࡹࡧࡴࡶࡵࠪဃ")]),
    bstack11l111l1ll_opy_(session[bstack1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬင")]),
    bstack11lll1l1ll_opy_(session[bstack1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧစ")] or session[bstack1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧဆ")] or bstack1l_opy_ (u"ࠨࠩဇ")) + bstack1l_opy_ (u"ࠤࠣࠦဈ") + (session[bstack1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬဉ")] or bstack1l_opy_ (u"ࠫࠬည")),
    session[bstack1l_opy_ (u"ࠬࡵࡳࠨဋ")] + bstack1l_opy_ (u"ࠨࠠࠣဌ") + session[bstack1l_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫဍ")], session[bstack1l_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪဎ")] or bstack1l_opy_ (u"ࠩࠪဏ"),
    session[bstack1l_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧတ")] if session[bstack1l_opy_ (u"ࠫࡨࡸࡥࡢࡶࡨࡨࡤࡧࡴࠨထ")] else bstack1l_opy_ (u"ࠬ࠭ဒ"))
@measure(event_name=EVENTS.bstack1111l111ll_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def bstack11l1l1l1ll_opy_(sessions, bstack1l1l11l11_opy_):
  try:
    bstack1lll1l1lll_opy_ = bstack1l_opy_ (u"ࠨࠢဓ")
    if not os.path.exists(bstack1lllll1l1l_opy_):
      os.mkdir(bstack1lllll1l1l_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l_opy_ (u"ࠧࡢࡵࡶࡩࡹࡹ࠯ࡳࡧࡳࡳࡷࡺ࠮ࡩࡶࡰࡰࠬန")), bstack1l_opy_ (u"ࠨࡴࠪပ")) as f:
      bstack1lll1l1lll_opy_ = f.read()
    bstack1lll1l1lll_opy_ = bstack1lll1l1lll_opy_.replace(bstack1l_opy_ (u"ࠩࡾࠩࡗࡋࡓࡖࡎࡗࡗࡤࡉࡏࡖࡐࡗࠩࢂ࠭ဖ"), str(len(sessions)))
    bstack1lll1l1lll_opy_ = bstack1lll1l1lll_opy_.replace(bstack1l_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠦࡿࠪဗ"), bstack1l1l11l11_opy_)
    bstack1lll1l1lll_opy_ = bstack1lll1l1lll_opy_.replace(bstack1l_opy_ (u"ࠫࢀࠫࡂࡖࡋࡏࡈࡤࡔࡁࡎࡇࠨࢁࠬဘ"),
                                              sessions[0].get(bstack1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣࡳࡧ࡭ࡦࠩမ")) if sessions[0] else bstack1l_opy_ (u"࠭ࠧယ"))
    with open(os.path.join(bstack1lllll1l1l_opy_, bstack1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ࠫရ")), bstack1l_opy_ (u"ࠨࡹࠪလ")) as stream:
      stream.write(bstack1lll1l1lll_opy_.split(bstack1l_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂ࠭ဝ"))[0])
      for session in sessions:
        stream.write(bstack1lll111l1_opy_(session))
      stream.write(bstack1lll1l1lll_opy_.split(bstack1l_opy_ (u"ࠪࡿ࡙ࠪࡅࡔࡕࡌࡓࡓ࡙࡟ࡅࡃࡗࡅࠪࢃࠧသ"))[1])
    logger.info(bstack1l_opy_ (u"ࠫࡌ࡫࡮ࡦࡴࡤࡸࡪࡪࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡢࡶ࡫࡯ࡨࠥࡧࡲࡵ࡫ࡩࡥࡨࡺࡳࠡࡣࡷࠤࢀࢃࠧဟ").format(bstack1lllll1l1l_opy_));
  except Exception as e:
    logger.debug(bstack1ll111l1ll_opy_.format(str(e)))
def bstack1ll1ll1l1_opy_(hashed_id):
  global CONFIG
  try:
    bstack1l1111lll_opy_ = datetime.datetime.now()
    host = bstack1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬဠ") if bstack1l_opy_ (u"࠭ࡡࡱࡲࠪအ") in CONFIG else bstack1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨဢ")
    user = CONFIG[bstack1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪဣ")]
    key = CONFIG[bstack1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬဤ")]
    bstack1l11lll1l_opy_ = bstack1l_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩဥ") if bstack1l_opy_ (u"ࠫࡦࡶࡰࠨဦ") in CONFIG else (bstack1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩဧ") if CONFIG.get(bstack1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪဨ")) else bstack1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩဩ"))
    host = bstack1l111ll1ll_opy_(cli.config, [bstack1l_opy_ (u"ࠣࡣࡳ࡭ࡸࠨဪ"), bstack1l_opy_ (u"ࠤࡤࡴࡵࡇࡵࡵࡱࡰࡥࡹ࡫ࠢါ"), bstack1l_opy_ (u"ࠥࡥࡵ࡯ࠢာ")], host) if bstack1l_opy_ (u"ࠫࡦࡶࡰࠨိ") in CONFIG else bstack1l111ll1ll_opy_(cli.config, [bstack1l_opy_ (u"ࠧࡧࡰࡪࡵࠥီ"), bstack1l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥࠣု"), bstack1l_opy_ (u"ࠢࡢࡲ࡬ࠦူ")], host)
    url = bstack1l_opy_ (u"ࠨࡽࢀ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠳ࡰࡳࡰࡰࠪေ").format(host, bstack1l11lll1l_opy_, hashed_id)
    headers = {
      bstack1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨဲ"): bstack1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ဳ"),
    }
    proxies = bstack1111l1ll1l_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡪࡩࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࡠ࡮࡬ࡷࡹࠨဴ"), datetime.datetime.now() - bstack1l1111lll_opy_)
      return list(map(lambda session: session[bstack1l_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠪဵ")], response.json()))
  except Exception as e:
    logger.debug(bstack11ll11111l_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack111l111ll_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def get_build_link():
  global CONFIG
  global bstack111l1l1l1l_opy_
  try:
    if bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩံ") in CONFIG:
      bstack1l1111lll_opy_ = datetime.datetime.now()
      host = bstack1l_opy_ (u"ࠧࡢࡲ࡬࠱ࡨࡲ࡯ࡶࡦ့ࠪ") if bstack1l_opy_ (u"ࠨࡣࡳࡴࠬး") in CONFIG else bstack1l_opy_ (u"ࠩࡤࡴ࡮္࠭")
      user = CONFIG[bstack1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩ်ࠬ")]
      key = CONFIG[bstack1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧျ")]
      bstack1l11lll1l_opy_ = bstack1l_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫြ") if bstack1l_opy_ (u"࠭ࡡࡱࡲࠪွ") in CONFIG else bstack1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩှ")
      url = bstack1l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡾࢁ࠿ࢁࡽࡁࡽࢀ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠱࡮ࡸࡵ࡮ࠨဿ").format(user, key, host, bstack1l11lll1l_opy_)
      if cli.is_enabled(CONFIG):
        bstack1l1l11l11_opy_, hashed_id = cli.bstack1llllll1l1_opy_()
        logger.info(bstack11l1l11l1l_opy_.format(bstack1l1l11l11_opy_))
        return [hashed_id, bstack1l1l11l11_opy_]
      else:
        headers = {
          bstack1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨ၀"): bstack1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭၁"),
        }
        if bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭၂") in CONFIG:
          params = {bstack1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ၃"): CONFIG[bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ၄")], bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ၅"): CONFIG[bstack1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ၆")]}
        else:
          params = {bstack1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ၇"): CONFIG[bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭၈")]}
        proxies = bstack1111l1ll1l_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack11l1l1l1l_opy_ = response.json()[0][bstack1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡤࡸ࡭ࡱࡪࠧ၉")]
          if bstack11l1l1l1l_opy_:
            bstack1l1l11l11_opy_ = bstack11l1l1l1l_opy_[bstack1l_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧࡤࡻࡲ࡭ࠩ၊")].split(bstack1l_opy_ (u"࠭ࡰࡶࡤ࡯࡭ࡨ࠳ࡢࡶ࡫࡯ࡨࠬ။"))[0] + bstack1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡹ࠯ࠨ၌") + bstack11l1l1l1l_opy_[
              bstack1l_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ၍")]
            logger.info(bstack11l1l11l1l_opy_.format(bstack1l1l11l11_opy_))
            bstack111l1l1l1l_opy_ = bstack11l1l1l1l_opy_[bstack1l_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ၎")]
            bstack1ll11l1ll1_opy_ = CONFIG[bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭၏")]
            if bstack1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ၐ") in CONFIG:
              bstack1ll11l1ll1_opy_ += bstack1l_opy_ (u"ࠬࠦࠧၑ") + CONFIG[bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨၒ")]
            if bstack1ll11l1ll1_opy_ != bstack11l1l1l1l_opy_[bstack1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬၓ")]:
              logger.debug(bstack1l1l111l1_opy_.format(bstack11l1l1l1l_opy_[bstack1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ၔ")], bstack1ll11l1ll1_opy_))
            cli.bstack1111l1lll_opy_(bstack1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡨࡧࡷࡣࡧࡻࡩ࡭ࡦࡢࡰ࡮ࡴ࡫ࠣၕ"), datetime.datetime.now() - bstack1l1111lll_opy_)
            return [bstack11l1l1l1l_opy_[bstack1l_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ၖ")], bstack1l1l11l11_opy_]
    else:
      logger.warn(bstack111111111_opy_)
  except Exception as e:
    logger.debug(bstack1111l11ll1_opy_.format(str(e)))
  return [None, None]
def bstack1l1lll1111_opy_(url, bstack1l1lll11l1_opy_=False):
  global CONFIG
  global bstack1l111lll1_opy_
  if not bstack1l111lll1_opy_:
    hostname = bstack1111l1ll11_opy_(url)
    is_private = bstack1l1ll111l1_opy_(hostname)
    if (bstack1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨၗ") in CONFIG and not bstack1l11l1ll1l_opy_(CONFIG[bstack1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩၘ")])) and (is_private or bstack1l1lll11l1_opy_):
      bstack1l111lll1_opy_ = hostname
def bstack1111l1ll11_opy_(url):
  return urlparse(url).hostname
def bstack1l1ll111l1_opy_(hostname):
  for bstack1ll1l11111_opy_ in bstack1ll1lll11_opy_:
    regex = re.compile(bstack1ll1l11111_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1l1lllllll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1l1l1lll1l_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1l11l11l1_opy_
  bstack11l11ll1ll_opy_ = not (bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪၙ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ၚ"), None))
  bstack1l1llll11l_opy_ = getattr(driver, bstack1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨၛ"), None) != True
  bstack11l11l11l1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၜ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack1l_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၝ"), None)
  if bstack11l11l11l1_opy_:
    if not bstack1ll11l1lll_opy_():
      logger.warning(bstack1l_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹ࠮ࠣၞ"))
      return {}
    logger.debug(bstack1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩၟ"))
    logger.debug(perform_scan(driver, driver_command=bstack1l_opy_ (u"࠭ࡥࡹࡧࡦࡹࡹ࡫ࡓࡤࡴ࡬ࡴࡹ࠭ၠ")))
    results = bstack111llll1l_opy_(bstack1l_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡳࠣၡ"))
    if results is not None and results.get(bstack1l_opy_ (u"ࠣ࡫ࡶࡷࡺ࡫ࡳࠣၢ")) is not None:
        return results[bstack1l_opy_ (u"ࠤ࡬ࡷࡸࡻࡥࡴࠤၣ")]
    logger.error(bstack1l_opy_ (u"ࠥࡒࡴࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡒࡦࡵࡸࡰࡹࡹࠠࡸࡧࡵࡩࠥ࡬࡯ࡶࡰࡧ࠲ࠧၤ"))
    return []
  if not bstack11111ll1_opy_.bstack111ll11lll_opy_(CONFIG, bstack1l11l11l1_opy_) or (bstack1l1llll11l_opy_ and bstack11l11ll1ll_opy_):
    logger.warning(bstack1l_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸ࠴ࠢၥ"))
    return {}
  try:
    logger.debug(bstack1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩၦ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1ll1l1llll_opy_.bstack1l1l1llll_opy_)
    return results
  except Exception:
    logger.error(bstack1l_opy_ (u"ࠨࡎࡰࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡻࡪࡸࡥࠡࡨࡲࡹࡳࡪ࠮ࠣၧ"))
    return {}
@measure(event_name=EVENTS.bstack11l1111l11_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1l11l11l1_opy_
  bstack11l11ll1ll_opy_ = not (bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫၨ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧၩ"), None))
  bstack1l1llll11l_opy_ = getattr(driver, bstack1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩၪ"), None) != True
  bstack11l11l11l1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪၫ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack1l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ၬ"), None)
  if bstack11l11l11l1_opy_:
    if not bstack1ll11l1lll_opy_():
      logger.warning(bstack1l_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺ࠰ࠥၭ"))
      return {}
    logger.debug(bstack1l_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼࠫၮ"))
    logger.debug(perform_scan(driver, driver_command=bstack1l_opy_ (u"ࠧࡦࡺࡨࡧࡺࡺࡥࡔࡥࡵ࡭ࡵࡺࠧၯ")))
    results = bstack111llll1l_opy_(bstack1l_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡔࡷࡰࡱࡦࡸࡹࠣၰ"))
    if results is not None and results.get(bstack1l_opy_ (u"ࠤࡶࡹࡲࡳࡡࡳࡻࠥၱ")) is not None:
        return results[bstack1l_opy_ (u"ࠥࡷࡺࡳ࡭ࡢࡴࡼࠦၲ")]
    logger.error(bstack1l_opy_ (u"ࠦࡓࡵࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡓࡧࡶࡹࡱࡺࡳࠡࡕࡸࡱࡲࡧࡲࡺࠢࡺࡥࡸࠦࡦࡰࡷࡱࡨ࠳ࠨၳ"))
    return {}
  if not bstack11111ll1_opy_.bstack111ll11lll_opy_(CONFIG, bstack1l11l11l1_opy_) or (bstack1l1llll11l_opy_ and bstack11l11ll1ll_opy_):
    logger.warning(bstack1l_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹ࠯ࠤၴ"))
    return {}
  try:
    logger.debug(bstack1l_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼࠫၵ"))
    logger.debug(perform_scan(driver))
    bstack1111lll1l1_opy_ = driver.execute_async_script(bstack1ll1l1llll_opy_.bstack111l111l1_opy_)
    return bstack1111lll1l1_opy_
  except Exception:
    logger.error(bstack1l_opy_ (u"ࠢࡏࡱࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡺࡳ࡭ࡢࡴࡼࠤࡼࡧࡳࠡࡨࡲࡹࡳࡪ࠮ࠣၶ"))
    return {}
def bstack1ll11l1lll_opy_():
  global CONFIG
  global bstack1l11l11l1_opy_
  bstack1111ll1111_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၷ"), None) and bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၸ"), None)
  if not bstack11111ll1_opy_.bstack111ll11lll_opy_(CONFIG, bstack1l11l11l1_opy_) or not bstack1111ll1111_opy_:
        logger.warning(bstack1l_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡴࡨࡷࡺࡲࡴࡴ࠰ࠥၹ"))
        return False
  return True
def bstack111llll1l_opy_(bstack111lll1l11_opy_):
    bstack11l1l1l11_opy_ = bstack1ll1lll1_opy_.current_test_uuid() if bstack1ll1lll1_opy_.current_test_uuid() else bstack11lll1l1_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack1l1ll1ll1l_opy_(bstack11l1l1l11_opy_, bstack111lll1l11_opy_))
        try:
            return future.result(timeout=bstack111ll11l1l_opy_)
        except TimeoutError:
            logger.error(bstack1l_opy_ (u"࡙ࠦ࡯࡭ࡦࡱࡸࡸࠥࡧࡦࡵࡧࡵࠤࢀࢃࡳࠡࡹ࡫࡭ࡱ࡫ࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡕࡩࡸࡻ࡬ࡵࡵࠥၺ").format(bstack111ll11l1l_opy_))
        except Exception as ex:
            logger.debug(bstack1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡷ࡫ࡴࡳ࡫ࡨࡺ࡮ࡴࡧࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡾࢁ࠳ࠦࡅࡳࡴࡲࡶࠥ࠳ࠠࡼࡿࠥၻ").format(bstack111lll1l11_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack1l111ll11_opy_, stage=STAGE.bstack11ll111111_opy_, bstack1l1ll1ll1_opy_=bstack11ll1ll11l_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1l11l11l1_opy_
  bstack11l11ll1ll_opy_ = not (bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪၼ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ၽ"), None))
  bstack111l1l11l1_opy_ = not (bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၾ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack1l_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၿ"), None))
  bstack1l1llll11l_opy_ = getattr(driver, bstack1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪႀ"), None) != True
  if not bstack11111ll1_opy_.bstack111ll11lll_opy_(CONFIG, bstack1l11l11l1_opy_) or (bstack1l1llll11l_opy_ and bstack11l11ll1ll_opy_ and bstack111l1l11l1_opy_):
    logger.warning(bstack1l_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡺࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲ࠳ࠨႁ"))
    return {}
  try:
    bstack1l1llll1l1_opy_ = bstack1l_opy_ (u"ࠬࡧࡰࡱࠩႂ") in CONFIG and CONFIG.get(bstack1l_opy_ (u"࠭ࡡࡱࡲࠪႃ"), bstack1l_opy_ (u"ࠧࠨႄ"))
    session_id = getattr(driver, bstack1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠬႅ"), None)
    if not session_id:
      logger.warning(bstack1l_opy_ (u"ࠤࡑࡳࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥࡪࡲࡪࡸࡨࡶࠧႆ"))
      return {bstack1l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤႇ"): bstack1l_opy_ (u"ࠦࡓࡵࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡋࡇࠤ࡫ࡵࡵ࡯ࡦࠥႈ")}
    if bstack1l1llll1l1_opy_:
      try:
        bstack1l1l111ll_opy_ = {
              bstack1l_opy_ (u"ࠬࡺࡨࡋࡹࡷࡘࡴࡱࡥ࡯ࠩႉ"): os.environ.get(bstack1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫႊ"), os.environ.get(bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫႋ"), bstack1l_opy_ (u"ࠨࠩႌ"))),
              bstack1l_opy_ (u"ࠩࡷ࡬࡙࡫ࡳࡵࡔࡸࡲ࡚ࡻࡩࡥႍࠩ"): bstack1ll1lll1_opy_.current_test_uuid() if bstack1ll1lll1_opy_.current_test_uuid() else bstack11lll1l1_opy_.current_hook_uuid(),
              bstack1l_opy_ (u"ࠪࡥࡺࡺࡨࡉࡧࡤࡨࡪࡸࠧႎ"): os.environ.get(bstack1l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩႏ")),
              bstack1l_opy_ (u"ࠬࡹࡣࡢࡰࡗ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ႐"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack1l_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫ႑"): os.environ.get(bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ႒"), bstack1l_opy_ (u"ࠨࠩ႓")),
              bstack1l_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࠩ႔"): kwargs.get(bstack1l_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢࡧࡴࡳ࡭ࡢࡰࡧࠫ႕"), None) or bstack1l_opy_ (u"ࠫࠬ႖")
          }
        if not hasattr(thread_local, bstack1l_opy_ (u"ࠬࡨࡡࡴࡧࡢࡥࡵࡶ࡟ࡢ࠳࠴ࡽࡤࡹࡣࡳ࡫ࡳࡸࠬ႗")):
            scripts = {bstack1l_opy_ (u"࠭ࡳࡤࡣࡱࠫ႘"): bstack1ll1l1llll_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack1l1l1llll1_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack1l1l1llll1_opy_[bstack1l_opy_ (u"ࠧࡴࡥࡤࡲࠬ႙")] = bstack1l1l1llll1_opy_[bstack1l_opy_ (u"ࠨࡵࡦࡥࡳ࠭ႚ")] % json.dumps(bstack1l1l111ll_opy_)
        bstack1ll1l1llll_opy_.bstack1l11l1llll_opy_(bstack1l1l1llll1_opy_)
        bstack1ll1l1llll_opy_.store()
        bstack11llll111_opy_ = driver.execute_script(bstack1ll1l1llll_opy_.perform_scan)
      except Exception as bstack11l1ll1l1l_opy_:
        logger.info(bstack1l_opy_ (u"ࠤࡄࡴࡵ࡯ࡵ࡮ࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡧࡦࡴࠠࡧࡣ࡬ࡰࡪࡪ࠺ࠡࠤႛ") + str(bstack11l1ll1l1l_opy_))
        bstack11llll111_opy_ = {bstack1l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤႜ"): str(bstack11l1ll1l1l_opy_)}
    else:
      bstack11llll111_opy_ = driver.execute_async_script(bstack1ll1l1llll_opy_.perform_scan, {bstack1l_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࠫႝ"): kwargs.get(bstack1l_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤࡩ࡯࡮࡯ࡤࡲࡩ࠭႞"), None) or bstack1l_opy_ (u"࠭ࠧ႟")})
    return bstack11llll111_opy_
  except Exception as err:
    logger.error(bstack1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡶࡺࡴࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲ࠳ࠦࡻࡾࠤႠ").format(str(err)))
    return {}