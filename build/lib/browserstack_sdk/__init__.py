# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
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
from browserstack_sdk.bstack11l1llllll_opy_ import bstack11l1lll111_opy_
from browserstack_sdk.bstack1ll1lllll_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack11ll1l1l1l_opy_():
  global CONFIG
  headers = {
        bstack11ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩਨ"): bstack11ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ਩"),
      }
  proxies = bstack1l1lll1l1l_opy_(CONFIG, bstack1l11lll111_opy_)
  try:
    response = requests.get(bstack1l11lll111_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack11l11lll11_opy_ = response.json()[bstack11ll_opy_ (u"ࠬ࡮ࡵࡣࡵࠪਪ")]
      logger.debug(bstack1l111ll11_opy_.format(response.json()))
      return bstack11l11lll11_opy_
    else:
      logger.debug(bstack11l111111l_opy_.format(bstack11ll_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧਫ")))
  except Exception as e:
    logger.debug(bstack11l111111l_opy_.format(e))
def bstack111lll1ll_opy_(hub_url):
  global CONFIG
  url = bstack11ll_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤਬ")+  hub_url + bstack11ll_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣਭ")
  headers = {
        bstack11ll_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨਮ"): bstack11ll_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ਯ"),
      }
  proxies = bstack1l1lll1l1l_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack111l1ll11_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1l1l111l11_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack1l11l1111_opy_, stage=STAGE.bstack1ll1111l1_opy_)
def bstack1l1l111ll1_opy_():
  try:
    global bstack1lllll1l11_opy_
    bstack11l11lll11_opy_ = bstack11ll1l1l1l_opy_()
    bstack11l111lll1_opy_ = []
    results = []
    for bstack11l1llll1_opy_ in bstack11l11lll11_opy_:
      bstack11l111lll1_opy_.append(bstack11111l1l1_opy_(target=bstack111lll1ll_opy_,args=(bstack11l1llll1_opy_,)))
    for t in bstack11l111lll1_opy_:
      t.start()
    for t in bstack11l111lll1_opy_:
      results.append(t.join())
    bstack1l11l1ll11_opy_ = {}
    for item in results:
      hub_url = item[bstack11ll_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬਰ")]
      latency = item[bstack11ll_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭਱")]
      bstack1l11l1ll11_opy_[hub_url] = latency
    bstack11lllll1l1_opy_ = min(bstack1l11l1ll11_opy_, key= lambda x: bstack1l11l1ll11_opy_[x])
    bstack1lllll1l11_opy_ = bstack11lllll1l1_opy_
    logger.debug(bstack1ll1lllll1_opy_.format(bstack11lllll1l1_opy_))
  except Exception as e:
    logger.debug(bstack11ll11lll_opy_.format(e))
from browserstack_sdk.bstack111l111l_opy_ import *
from browserstack_sdk.bstack1111llll_opy_ import *
from browserstack_sdk.bstack11l11l11_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack11l1l1l1ll_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack11l1l1llll_opy_, stage=STAGE.bstack1ll1111l1_opy_)
def bstack1lll11ll1l_opy_():
    global bstack1lllll1l11_opy_
    try:
        bstack1llll1l111_opy_ = bstack1111lllll1_opy_()
        bstack11ll1111l_opy_(bstack1llll1l111_opy_)
        hub_url = bstack1llll1l111_opy_.get(bstack11ll_opy_ (u"ࠨࡵࡳ࡮ࠥਲ"), bstack11ll_opy_ (u"ࠢࠣਲ਼"))
        if hub_url.endswith(bstack11ll_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩ਴")):
            hub_url = hub_url.rsplit(bstack11ll_opy_ (u"ࠩ࠲ࡻࡩ࠵ࡨࡶࡤࠪਵ"), 1)[0]
        if hub_url.startswith(bstack11ll_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࠫਸ਼")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack11ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࠭਷")):
            hub_url = hub_url[8:]
        bstack1lllll1l11_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1111lllll1_opy_():
    global CONFIG
    bstack11ll1l1ll1_opy_ = CONFIG.get(bstack11ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩਸ"), {}).get(bstack11ll_opy_ (u"࠭ࡧࡳ࡫ࡧࡒࡦࡳࡥࠨਹ"), bstack11ll_opy_ (u"ࠧࡏࡑࡢࡋࡗࡏࡄࡠࡐࡄࡑࡊࡥࡐࡂࡕࡖࡉࡉ࠭਺"))
    if not isinstance(bstack11ll1l1ll1_opy_, str):
        raise ValueError(bstack11ll_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡈࡴ࡬ࡨࠥࡴࡡ࡮ࡧࠣࡱࡺࡹࡴࠡࡤࡨࠤࡦࠦࡶࡢ࡮࡬ࡨࠥࡹࡴࡳ࡫ࡱ࡫ࠧ਻"))
    try:
        bstack1llll1l111_opy_ = bstack111111lll1_opy_(bstack11ll1l1ll1_opy_)
        return bstack1llll1l111_opy_
    except Exception as e:
        logger.error(bstack11ll_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽ਼ࠣ").format(str(e)))
        return {}
def bstack111111lll1_opy_(bstack11ll1l1ll1_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack11ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ਽")] or not CONFIG[bstack11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧਾ")]:
            raise ValueError(bstack11ll_opy_ (u"ࠧࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠠࡰࡴࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠢਿ"))
        url = bstack1lll1l1111_opy_ + bstack11ll1l1ll1_opy_
        auth = (CONFIG[bstack11ll_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨੀ")], CONFIG[bstack11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪੁ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack11l1lllll1_opy_ = json.loads(response.text)
            return bstack11l1lllll1_opy_
    except ValueError as ve:
        logger.error(bstack11ll_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣੂ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack11ll_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࠿ࠦࡻࡾࠤ੃").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack11ll1111l_opy_(bstack111l1l111l_opy_):
    global CONFIG
    if bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ੄") not in CONFIG or str(CONFIG[bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ੅")]).lower() == bstack11ll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ੆"):
        CONFIG[bstack11ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬੇ")] = False
    elif bstack11ll_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬੈ") in bstack111l1l111l_opy_:
        bstack1111ll1l1l_opy_ = CONFIG.get(bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ੉"), {})
        logger.debug(bstack11ll_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢ੊"), bstack1111ll1l1l_opy_)
        bstack11l11l1111_opy_ = bstack111l1l111l_opy_.get(bstack11ll_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡕࡩࡵ࡫ࡡࡵࡧࡵࡷࠧੋ"), [])
        bstack11l111111_opy_ = bstack11ll_opy_ (u"ࠦ࠱ࠨੌ").join(bstack11l11l1111_opy_)
        logger.debug(bstack11ll_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡻࡳࡵࡱࡰࠤࡷ࡫ࡰࡦࡣࡷࡩࡷࠦࡳࡵࡴ࡬ࡲ࡬ࡀࠠࠦࡵ੍ࠥ"), bstack11l111111_opy_)
        bstack1l11lllll1_opy_ = {
            bstack11ll_opy_ (u"ࠨ࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ੎"): bstack11ll_opy_ (u"ࠢࡢࡶࡶ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷࠨ੏"),
            bstack11ll_opy_ (u"ࠣࡨࡲࡶࡨ࡫ࡌࡰࡥࡤࡰࠧ੐"): bstack11ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢੑ"),
            bstack11ll_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧ੒"): bstack11l111111_opy_
        }
        bstack1111ll1l1l_opy_.update(bstack1l11lllll1_opy_)
        logger.debug(bstack11ll_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼࡙ࠣࡵࡪࡡࡵࡧࡧࠤࡱࡵࡣࡢ࡮ࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠫࡳࠣ੓"), bstack1111ll1l1l_opy_)
        CONFIG[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ੔")] = bstack1111ll1l1l_opy_
        logger.debug(bstack11ll_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡌࡩ࡯ࡣ࡯ࠤࡈࡕࡎࡇࡋࡊ࠾ࠥࠫࡳࠣ੕"), CONFIG)
def bstack1l1l1111ll_opy_():
    bstack1llll1l111_opy_ = bstack1111lllll1_opy_()
    if not bstack1llll1l111_opy_[bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠧ੖")]:
      raise ValueError(bstack11ll_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠡ࡫ࡶࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬ࡲࡰ࡯ࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠥ੗"))
    return bstack1llll1l111_opy_[bstack11ll_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠩ੘")] + bstack11ll_opy_ (u"ࠪࡃࡨࡧࡰࡴ࠿ࠪਖ਼")
@measure(event_name=EVENTS.bstack111l1ll1ll_opy_, stage=STAGE.bstack1ll1111l1_opy_)
def bstack1l1l1l111_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack11ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ਗ਼")], CONFIG[bstack11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨਜ਼")])
        url = bstack1l1lll1111_opy_
        logger.debug(bstack11ll_opy_ (u"ࠨࡁࡵࡶࡨࡱࡵࡺࡩ࡯ࡩࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬ࡲࡰ࡯ࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡗࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࠦࡁࡑࡋࠥੜ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack11ll_opy_ (u"ࠢࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪࠨ੝"): bstack11ll_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠦਫ਼")})
            if response.status_code == 200:
                bstack1ll11111l_opy_ = json.loads(response.text)
                bstack1l1l1llll_opy_ = bstack1ll11111l_opy_.get(bstack11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡴࠩ੟"), [])
                if bstack1l1l1llll_opy_:
                    bstack1l1111l1ll_opy_ = bstack1l1l1llll_opy_[0]
                    build_hashed_id = bstack1l1111l1ll_opy_.get(bstack11ll_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭੠"))
                    bstack1l1lll1ll1_opy_ = bstack111ll1111_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1l1lll1ll1_opy_])
                    logger.info(bstack1l11lll1l1_opy_.format(bstack1l1lll1ll1_opy_))
                    bstack11ll1lll1l_opy_ = CONFIG[bstack11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ੡")]
                    if bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ੢") in CONFIG:
                      bstack11ll1lll1l_opy_ += bstack11ll_opy_ (u"࠭ࠠࠨ੣") + CONFIG[bstack11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ੤")]
                    if bstack11ll1lll1l_opy_ != bstack1l1111l1ll_opy_.get(bstack11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭੥")):
                      logger.debug(bstack1lllllll1l_opy_.format(bstack1l1111l1ll_opy_.get(bstack11ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ੦")), bstack11ll1lll1l_opy_))
                    return result
                else:
                    logger.debug(bstack11ll_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡑࡳࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࡷ࡫ࡳࡱࡱࡱࡷࡪ࠴ࠢ੧"))
            else:
                logger.debug(bstack11ll_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨ੨"))
        except Exception as e:
            logger.error(bstack11ll_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࡹࠠ࠻ࠢࡾࢁࠧ੩").format(str(e)))
    else:
        logger.debug(bstack11ll_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡉࡏࡏࡈࡌࡋࠥ࡯ࡳࠡࡰࡲࡸࠥࡹࡥࡵ࠰࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨ੪"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1111l11l11_opy_ import bstack1111l11l11_opy_, Events, bstack1ll1ll11ll_opy_, bstack1l1l11llll_opy_
from bstack_utils.measure import bstack11l1l1ll11_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack111llll111_opy_ import bstack1ll1ll1l11_opy_
from bstack_utils.messages import *
from bstack_utils import bstack11l1l1l1ll_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack11llllllll_opy_, bstack1ll1l1lll_opy_, bstack111ll111l1_opy_, bstack1l1l11l1_opy_, \
  bstack1ll11llll1_opy_, \
  Notset, bstack1l11l1l1l_opy_, \
  bstack111111l111_opy_, bstack1ll111l1l1_opy_, bstack1l11111111_opy_, bstack111l1l1l11_opy_, bstack11l1llll1l_opy_, bstack11llll1l1l_opy_, \
  bstack1l1llll111_opy_, \
  bstack1l1ll111l_opy_, bstack1llll111l1_opy_, bstack11111l1l1l_opy_, bstack111ll11l11_opy_, \
  bstack11111l111l_opy_, bstack11111llll_opy_, bstack1lll1l1lll_opy_, bstack1l1lllll1_opy_
from bstack_utils.bstack11llll1l11_opy_ import bstack1lll11l111_opy_
from bstack_utils.bstack11lll1ll1_opy_ import bstack1111l1111l_opy_, bstack1lll111lll_opy_
from bstack_utils.bstack1lll1l111l_opy_ import bstack11l111ll11_opy_
from bstack_utils.bstack1l1lll11l1_opy_ import bstack1ll1111111_opy_, bstack111l1l1lll_opy_
from bstack_utils.bstack1l1l1l1l1_opy_ import bstack1l1l1l1l1_opy_
from bstack_utils.bstack11l11l11l_opy_ import bstack1l111llll_opy_
from bstack_utils.proxy import bstack111ll1l1ll_opy_, bstack1l1lll1l1l_opy_, bstack111lll1l1l_opy_, bstack11l1l1l1l1_opy_
from bstack_utils.bstack11l1l11l1l_opy_ import bstack11ll1l11l_opy_
import bstack_utils.bstack11l1lll1ll_opy_ as bstack1111l1l11l_opy_
import bstack_utils.bstack111l1lll11_opy_ as bstack1l1ll1llll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack11ll1l111l_opy_ import bstack1l111l111_opy_
from bstack_utils.bstack11111lll_opy_ import bstack111ll1ll_opy_
from bstack_utils.bstack11l1ll111l_opy_ import bstack11l11l11ll_opy_
if os.getenv(bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡌࡔࡕࡋࡔࠩ੫")):
  cli.bstack1l11lll11l_opy_()
else:
  os.environ[bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡍࡕࡏࡌࡕࠪ੬")] = bstack11ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ੭")
bstack1lll1lll11_opy_ = bstack11ll_opy_ (u"ࠪࠤࠥ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࠣࠤ࡮࡬ࠨࡱࡣࡪࡩࠥࡃ࠽࠾ࠢࡹࡳ࡮ࡪࠠ࠱ࠫࠣࡿࡡࡴࠠࠡࠢࡷࡶࡾࢁ࡜࡯ࠢࡦࡳࡳࡹࡴࠡࡨࡶࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨ࡝ࠩࡩࡷࡡ࠭ࠩ࠼࡞ࡱࠤࠥࠦࠠࠡࡨࡶ࠲ࡦࡶࡰࡦࡰࡧࡊ࡮ࡲࡥࡔࡻࡱࡧ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪ࠯ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡶ࡟ࡪࡰࡧࡩࡽ࠯ࠠࠬࠢࠥ࠾ࠧࠦࠫࠡࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࠨࡢࡹࡤ࡭ࡹࠦ࡮ࡦࡹࡓࡥ࡬࡫࠲࠯ࡧࡹࡥࡱࡻࡡࡵࡧࠫࠦ࠭࠯ࠠ࠾ࡀࠣࡿࢂࠨࠬࠡ࡞ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥ࡫ࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡄࡦࡶࡤ࡭ࡱࡹࠢࡾ࡞ࠪ࠭࠮࠯࡛ࠣࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠦࡢ࠯ࠠࠬࠢࠥ࠰ࡡࡢ࡮ࠣࠫ࡟ࡲࠥࠦࠠࠡࡿࡦࡥࡹࡩࡨࠩࡧࡻ࠭ࢀࡢ࡮ࠡࠢࠣࠤࢂࡢ࡮ࠡࠢࢀࡠࡳࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠪ੮")
bstack1l1lll111_opy_ = bstack11ll_opy_ (u"ࠫࡡࡴ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰࡞ࡱࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶ࡡࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠷࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡲࡢ࡭ࡳࡪࡥࡹࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠷ࡣ࡜࡯ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯ࡵ࡯࡭ࡨ࡫ࠨ࠱࠮ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸࠯࡜࡯ࡥࡲࡲࡸࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯ࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨࠩ࠼࡞ࡱ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡰࡦࡻ࡮ࡤࡪࠣࡁࠥࡧࡳࡺࡰࡦࠤ࠭ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷ࠮ࠦ࠽࠿ࠢࡾࡠࡳࡲࡥࡵࠢࡦࡥࡵࡹ࠻࡝ࡰࡷࡶࡾࠦࡻ࡝ࡰࡦࡥࡵࡹࠠ࠾ࠢࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶ࠭ࡡࡴࠠࠡࡿࠣࡧࡦࡺࡣࡩࠪࡨࡼ࠮ࠦࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡦࡽࡡࡪࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡧࡴࡴ࡮ࡦࡥࡷࠬࢀࡢ࡮ࠡࠢࠣࠤࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴ࠻ࠢࡣࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠩࢁࡥ࡯ࡥࡲࡨࡪ࡛ࡒࡊࡅࡲࡱࡵࡵ࡮ࡦࡰࡷࠬࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡩࡡࡱࡵࠬ࠭ࢂࡦࠬ࡝ࡰࠣࠤࠥࠦ࠮࠯࠰࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴ࡞ࡱࠤࠥࢃࠩ࡝ࡰࢀࡠࡳ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࠪ੯")
from ._version import __version__
bstack111l111111_opy_ = None
CONFIG = {}
bstack1ll11llll_opy_ = {}
bstack1111ll1l1_opy_ = {}
bstack1l1ll1111l_opy_ = None
bstack111111111_opy_ = None
bstack1111llll1_opy_ = None
bstack1llll1111l_opy_ = -1
bstack1111l11111_opy_ = 0
bstack1ll11l1lll_opy_ = bstack111l1ll111_opy_
bstack1lllll111l_opy_ = 1
bstack11l111ll1l_opy_ = False
bstack111111lll_opy_ = False
bstack11l11l111l_opy_ = bstack11ll_opy_ (u"ࠬ࠭ੰ")
bstack111l1l11l_opy_ = bstack11ll_opy_ (u"࠭ࠧੱ")
bstack1l111ll1l1_opy_ = False
bstack1ll1l1111_opy_ = True
bstack11lll1lll_opy_ = bstack11ll_opy_ (u"ࠧࠨੲ")
bstack1111lll1l_opy_ = []
bstack1l11l1lll1_opy_ = threading.Lock()
bstack11111ll1l1_opy_ = threading.Lock()
bstack1lllll1l11_opy_ = bstack11ll_opy_ (u"ࠨࠩੳ")
bstack1ll1ll11l_opy_ = False
bstack111l1llll_opy_ = None
bstack111lll1l1_opy_ = None
bstack11l11ll1l1_opy_ = None
bstack11ll1l11ll_opy_ = -1
bstack111lll111l_opy_ = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠩࢁࠫੴ")), bstack11ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪੵ"), bstack11ll_opy_ (u"ࠫ࠳ࡸ࡯ࡣࡱࡷ࠱ࡷ࡫ࡰࡰࡴࡷ࠱࡭࡫࡬ࡱࡧࡵ࠲࡯ࡹ࡯࡯ࠩ੶"))
bstack1l1llllll_opy_ = 0
bstack1llll1llll_opy_ = 0
bstack11llll1l1_opy_ = []
bstack1l11llllll_opy_ = []
bstack1111l1l111_opy_ = []
bstack11l1l1l11l_opy_ = []
bstack1l11l1lll_opy_ = bstack11ll_opy_ (u"ࠬ࠭੷")
bstack1111l1ll11_opy_ = bstack11ll_opy_ (u"࠭ࠧ੸")
bstack111l1lll1l_opy_ = False
bstack1lllllll11_opy_ = False
bstack1llll11ll1_opy_ = {}
bstack11ll111l1_opy_ = None
bstack1l111lllll_opy_ = None
bstack1l1l11ll1l_opy_ = None
bstack11lllllll_opy_ = None
bstack11l1111l1_opy_ = None
bstack1l1l11111l_opy_ = None
bstack11l11l1l1_opy_ = None
bstack111l111lll_opy_ = None
bstack11llllll1_opy_ = None
bstack111lll11l1_opy_ = None
bstack1ll111111_opy_ = None
bstack1l11ll1l11_opy_ = None
bstack1l11ll11l_opy_ = None
bstack11ll1l1111_opy_ = None
bstack1l111l1ll1_opy_ = None
bstack111l11l1l1_opy_ = None
bstack11ll111lll_opy_ = None
bstack1ll1111l1l_opy_ = None
bstack1ll1l1l11l_opy_ = None
bstack1l1ll111l1_opy_ = None
bstack1l1llll11_opy_ = None
bstack11lll1l11_opy_ = None
bstack11l11ll111_opy_ = None
thread_local = threading.local()
bstack1ll11l11l_opy_ = False
bstack1llll111ll_opy_ = bstack11ll_opy_ (u"ࠢࠣ੹")
logger = bstack11l1l1l1ll_opy_.get_logger(__name__, bstack1ll11l1lll_opy_)
bstack1111l111_opy_ = Config.bstack11111ll1_opy_()
percy = bstack111l1l1ll1_opy_()
bstack111l1ll11l_opy_ = bstack1ll1ll1l11_opy_()
bstack1l1llllll1_opy_ = bstack11l11l11_opy_()
def bstack111111l1l1_opy_():
  global CONFIG
  global bstack111l1lll1l_opy_
  global bstack1111l111_opy_
  testContextOptions = bstack1l1ll11l1_opy_(CONFIG)
  if bstack1ll11llll1_opy_(CONFIG):
    if (bstack11ll_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ੺") in testContextOptions and str(testContextOptions[bstack11ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ੻")]).lower() == bstack11ll_opy_ (u"ࠪࡸࡷࡻࡥࠨ੼")):
      bstack111l1lll1l_opy_ = True
    bstack1111l111_opy_.bstack1lllll1lll_opy_(testContextOptions.get(bstack11ll_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ੽"), False))
  else:
    bstack111l1lll1l_opy_ = True
    bstack1111l111_opy_.bstack1lllll1lll_opy_(True)
def bstack11111111l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11l11l11l1_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack111111llll_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11ll_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡩ࡯࡯ࡨ࡬࡫࡫࡯࡬ࡦࠤ੾") == args[i].lower() or bstack11ll_opy_ (u"ࠨ࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡱࡪ࡮࡭ࠢ੿") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack11lll1lll_opy_
      bstack11lll1lll_opy_ += bstack11ll_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡄࡱࡱࡪ࡮࡭ࡆࡪ࡮ࡨࠤࠬ઀") + shlex.quote(path)
      return path
  return None
bstack1l1111l11_opy_ = re.compile(bstack11ll_opy_ (u"ࡳࠤ࠱࠮ࡄࡢࠤࡼࠪ࠱࠮ࡄ࠯ࡽ࠯ࠬࡂࠦઁ"))
def bstack1l111l11l_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l1111l11_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11ll_opy_ (u"ࠤࠧࡿࠧં") + group + bstack11ll_opy_ (u"ࠥࢁࠧઃ"), os.environ.get(group))
  return value
def bstack1ll11ll1ll_opy_():
  global bstack11l11ll111_opy_
  if bstack11l11ll111_opy_ is None:
        bstack11l11ll111_opy_ = bstack111111llll_opy_()
  bstack11lll1111l_opy_ = bstack11l11ll111_opy_
  if bstack11lll1111l_opy_ and os.path.exists(os.path.abspath(bstack11lll1111l_opy_)):
    fileName = bstack11lll1111l_opy_
  if bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ઄") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆࠩઅ")])) and not bstack11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨઆ") in locals():
    fileName = os.environ[bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫઇ")]
  if bstack11ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡔࡡ࡮ࡧࠪઈ") in locals():
    bstack1lllll_opy_ = os.path.abspath(fileName)
  else:
    bstack1lllll_opy_ = bstack11ll_opy_ (u"ࠩࠪઉ")
  bstack111l11ll1l_opy_ = os.getcwd()
  bstack1111lll111_opy_ = bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ઊ")
  bstack111111l1ll_opy_ = bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡦࡳ࡬ࠨઋ")
  while (not os.path.exists(bstack1lllll_opy_)) and bstack111l11ll1l_opy_ != bstack11ll_opy_ (u"ࠧࠨઌ"):
    bstack1lllll_opy_ = os.path.join(bstack111l11ll1l_opy_, bstack1111lll111_opy_)
    if not os.path.exists(bstack1lllll_opy_):
      bstack1lllll_opy_ = os.path.join(bstack111l11ll1l_opy_, bstack111111l1ll_opy_)
    if bstack111l11ll1l_opy_ != os.path.dirname(bstack111l11ll1l_opy_):
      bstack111l11ll1l_opy_ = os.path.dirname(bstack111l11ll1l_opy_)
    else:
      bstack111l11ll1l_opy_ = bstack11ll_opy_ (u"ࠨࠢઍ")
  bstack11l11ll111_opy_ = bstack1lllll_opy_ if os.path.exists(bstack1lllll_opy_) else None
  return bstack11l11ll111_opy_
def bstack1111l11l1_opy_(config):
    if bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧ઎") in config:
      config[bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬએ")] = config[bstack11ll_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࠩઐ")]
    if bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࡒࡴࡹ࡯࡯࡯ࡵࠪઑ") in config:
      config[bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ઒")] = config[bstack11ll_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࡔࡶࡴࡪࡱࡱࡷࠬઓ")]
def bstack11l1ll111_opy_():
  bstack1lllll_opy_ = bstack1ll11ll1ll_opy_()
  if not os.path.exists(bstack1lllll_opy_):
    bstack1ll111111l_opy_(
      bstack1ll11ll11l_opy_.format(os.getcwd()))
  try:
    with open(bstack1lllll_opy_, bstack11ll_opy_ (u"࠭ࡲࠨઔ")) as stream:
      yaml.add_implicit_resolver(bstack11ll_opy_ (u"ࠢࠢࡲࡤࡸ࡭࡫ࡸࠣક"), bstack1l1111l11_opy_)
      yaml.add_constructor(bstack11ll_opy_ (u"ࠣࠣࡳࡥࡹ࡮ࡥࡹࠤખ"), bstack1l111l11l_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1111l11l1_opy_(config)
      return config
  except:
    with open(bstack1lllll_opy_, bstack11ll_opy_ (u"ࠩࡵࠫગ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1111l11l1_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1ll111111l_opy_(bstack11lll1l1l1_opy_.format(str(exc)))
def bstack11ll1ll1ll_opy_(config):
  bstack1lll11l1l1_opy_ = bstack11l1l1ll1l_opy_(config)
  for option in list(bstack1lll11l1l1_opy_):
    if option.lower() in bstack1l1l1111l1_opy_ and option != bstack1l1l1111l1_opy_[option.lower()]:
      bstack1lll11l1l1_opy_[bstack1l1l1111l1_opy_[option.lower()]] = bstack1lll11l1l1_opy_[option]
      del bstack1lll11l1l1_opy_[option]
  return config
def bstack11l1l1111_opy_():
  global bstack1111ll1l1_opy_
  for key, bstack11111l1111_opy_ in bstack1ll11l111_opy_.items():
    if isinstance(bstack11111l1111_opy_, list):
      for var in bstack11111l1111_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1111ll1l1_opy_[key] = os.environ[var]
          break
    elif bstack11111l1111_opy_ in os.environ and os.environ[bstack11111l1111_opy_] and str(os.environ[bstack11111l1111_opy_]).strip():
      bstack1111ll1l1_opy_[key] = os.environ[bstack11111l1111_opy_]
  if bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬઘ") in os.environ:
    bstack1111ll1l1_opy_[bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨઙ")] = {}
    bstack1111ll1l1_opy_[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩચ")][bstack11ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨછ")] = os.environ[bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩજ")]
def bstack1llllll1l1_opy_():
  global bstack1ll11llll_opy_
  global bstack11lll1lll_opy_
  bstack11lll11l11_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack11ll_opy_ (u"ࠨ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫઝ").lower() == val.lower():
      bstack1ll11llll_opy_[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઞ")] = {}
      bstack1ll11llll_opy_[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧટ")][bstack11ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ઠ")] = sys.argv[idx + 1]
      bstack11lll11l11_opy_.extend([idx, idx + 1])
      break
  for key, bstack1111l111l1_opy_ in bstack11l1l1lll_opy_.items():
    if isinstance(bstack1111l111l1_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack1111l111l1_opy_:
          if bstack11ll_opy_ (u"ࠬ࠳࠭ࠨડ") + var.lower() == val.lower() and key not in bstack1ll11llll_opy_:
            bstack1ll11llll_opy_[key] = sys.argv[idx + 1]
            bstack11lll1lll_opy_ += bstack11ll_opy_ (u"࠭ࠠ࠮࠯ࠪઢ") + var + bstack11ll_opy_ (u"ࠧࠡࠩણ") + shlex.quote(sys.argv[idx + 1])
            bstack11lll11l11_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack11ll_opy_ (u"ࠨ࠯࠰ࠫત") + bstack1111l111l1_opy_.lower() == val.lower() and key not in bstack1ll11llll_opy_:
          bstack1ll11llll_opy_[key] = sys.argv[idx + 1]
          bstack11lll1lll_opy_ += bstack11ll_opy_ (u"ࠩࠣ࠱࠲࠭થ") + bstack1111l111l1_opy_ + bstack11ll_opy_ (u"ࠪࠤࠬદ") + shlex.quote(sys.argv[idx + 1])
          bstack11lll11l11_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack11lll11l11_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack1111lll1l1_opy_(config):
  bstack1111l111l_opy_ = config.keys()
  for bstack11lll11111_opy_, bstack1lllllllll_opy_ in bstack1lll111l11_opy_.items():
    if bstack1lllllllll_opy_ in bstack1111l111l_opy_:
      config[bstack11lll11111_opy_] = config[bstack1lllllllll_opy_]
      del config[bstack1lllllllll_opy_]
  for bstack11lll11111_opy_, bstack1lllllllll_opy_ in bstack1l11111l1l_opy_.items():
    if isinstance(bstack1lllllllll_opy_, list):
      for bstack1l11ll11l1_opy_ in bstack1lllllllll_opy_:
        if bstack1l11ll11l1_opy_ in bstack1111l111l_opy_:
          config[bstack11lll11111_opy_] = config[bstack1l11ll11l1_opy_]
          del config[bstack1l11ll11l1_opy_]
          break
    elif bstack1lllllllll_opy_ in bstack1111l111l_opy_:
      config[bstack11lll11111_opy_] = config[bstack1lllllllll_opy_]
      del config[bstack1lllllllll_opy_]
  for bstack1l11ll11l1_opy_ in list(config):
    for bstack1lll1111ll_opy_ in bstack1ll1l11111_opy_:
      if bstack1l11ll11l1_opy_.lower() == bstack1lll1111ll_opy_.lower() and bstack1l11ll11l1_opy_ != bstack1lll1111ll_opy_:
        config[bstack1lll1111ll_opy_] = config[bstack1l11ll11l1_opy_]
        del config[bstack1l11ll11l1_opy_]
  bstack11111lll1_opy_ = [{}]
  if not config.get(bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧધ")):
    config[bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨન")] = [{}]
  bstack11111lll1_opy_ = config[bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ઩")]
  for platform in bstack11111lll1_opy_:
    for bstack1l11ll11l1_opy_ in list(platform):
      for bstack1lll1111ll_opy_ in bstack1ll1l11111_opy_:
        if bstack1l11ll11l1_opy_.lower() == bstack1lll1111ll_opy_.lower() and bstack1l11ll11l1_opy_ != bstack1lll1111ll_opy_:
          platform[bstack1lll1111ll_opy_] = platform[bstack1l11ll11l1_opy_]
          del platform[bstack1l11ll11l1_opy_]
  for bstack11lll11111_opy_, bstack1lllllllll_opy_ in bstack1l11111l1l_opy_.items():
    for platform in bstack11111lll1_opy_:
      if isinstance(bstack1lllllllll_opy_, list):
        for bstack1l11ll11l1_opy_ in bstack1lllllllll_opy_:
          if bstack1l11ll11l1_opy_ in platform:
            platform[bstack11lll11111_opy_] = platform[bstack1l11ll11l1_opy_]
            del platform[bstack1l11ll11l1_opy_]
            break
      elif bstack1lllllllll_opy_ in platform:
        platform[bstack11lll11111_opy_] = platform[bstack1lllllllll_opy_]
        del platform[bstack1lllllllll_opy_]
  for bstack11l1l111ll_opy_ in bstack1lll1ll1l1_opy_:
    if bstack11l1l111ll_opy_ in config:
      if not bstack1lll1ll1l1_opy_[bstack11l1l111ll_opy_] in config:
        config[bstack1lll1ll1l1_opy_[bstack11l1l111ll_opy_]] = {}
      config[bstack1lll1ll1l1_opy_[bstack11l1l111ll_opy_]].update(config[bstack11l1l111ll_opy_])
      del config[bstack11l1l111ll_opy_]
  for platform in bstack11111lll1_opy_:
    for bstack11l1l111ll_opy_ in bstack1lll1ll1l1_opy_:
      if bstack11l1l111ll_opy_ in list(platform):
        if not bstack1lll1ll1l1_opy_[bstack11l1l111ll_opy_] in platform:
          platform[bstack1lll1ll1l1_opy_[bstack11l1l111ll_opy_]] = {}
        platform[bstack1lll1ll1l1_opy_[bstack11l1l111ll_opy_]].update(platform[bstack11l1l111ll_opy_])
        del platform[bstack11l1l111ll_opy_]
  config = bstack11ll1ll1ll_opy_(config)
  return config
def bstack1ll1llll11_opy_(config):
  global bstack111l1l11l_opy_
  bstack1ll1llll1l_opy_ = False
  if bstack11ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫપ") in config and str(config[bstack11ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬફ")]).lower() != bstack11ll_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨબ"):
    if bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧભ") not in config or str(config[bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨમ")]).lower() == bstack11ll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫય"):
      config[bstack11ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬર")] = False
    else:
      bstack1llll1l111_opy_ = bstack1111lllll1_opy_()
      if bstack11ll_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬ઱") in bstack1llll1l111_opy_:
        if not bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬલ") in config:
          config[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ળ")] = {}
        config[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ઴")][bstack11ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭વ")] = bstack11ll_opy_ (u"ࠬࡧࡴࡴ࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠫશ")
        bstack1ll1llll1l_opy_ = True
        bstack111l1l11l_opy_ = config[bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪષ")].get(bstack11ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩસ"))
  if bstack1ll11llll1_opy_(config) and bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬહ") in config and str(config[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭઺")]).lower() != bstack11ll_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ઻") and not bstack1ll1llll1l_opy_:
    if not bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ઼") in config:
      config[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩઽ")] = {}
    if not config[bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪા")].get(bstack11ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠫિ")) and not bstack11ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪી") in config[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ુ")]:
      bstack1lll1111_opy_ = datetime.datetime.now()
      bstack1ll11lll1l_opy_ = bstack1lll1111_opy_.strftime(bstack11ll_opy_ (u"ࠪࠩࡩࡥࠥࡣࡡࠨࡌࠪࡓࠧૂ"))
      hostname = socket.gethostname()
      bstack111ll1lll_opy_ = bstack11ll_opy_ (u"ࠫࠬૃ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11ll_opy_ (u"ࠬࢁࡽࡠࡽࢀࡣࢀࢃࠧૄ").format(bstack1ll11lll1l_opy_, hostname, bstack111ll1lll_opy_)
      config[bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪૅ")][bstack11ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૆")] = identifier
    bstack111l1l11l_opy_ = config[bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬે")].get(bstack11ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫૈ"))
  return config
def bstack11ll1lll11_opy_():
  bstack1l11111l1_opy_ =  bstack111l1l1l11_opy_()[bstack11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠩૉ")]
  return bstack1l11111l1_opy_ if bstack1l11111l1_opy_ else -1
def bstack1ll1ll1l1l_opy_(bstack1l11111l1_opy_):
  global CONFIG
  if not bstack11ll_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭૊") in CONFIG[bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧો")]:
    return
  CONFIG[bstack11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨૌ")] = CONFIG[bstack11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳ્ࠩ")].replace(
    bstack11ll_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪ૎"),
    str(bstack1l11111l1_opy_)
  )
def bstack1ll1ll1l1_opy_():
  global CONFIG
  if not bstack11ll_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨ૏") in CONFIG[bstack11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૐ")]:
    return
  bstack1lll1111_opy_ = datetime.datetime.now()
  bstack1ll11lll1l_opy_ = bstack1lll1111_opy_.strftime(bstack11ll_opy_ (u"ࠫࠪࡪ࠭ࠦࡤ࠰ࠩࡍࡀࠥࡎࠩ૑"))
  CONFIG[bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૒")] = CONFIG[bstack11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૓")].replace(
    bstack11ll_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭૔"),
    bstack1ll11lll1l_opy_
  )
def bstack11ll111l1l_opy_():
  global CONFIG
  if bstack11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૕") in CONFIG and not bool(CONFIG[bstack11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૖")]):
    del CONFIG[bstack11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૗")]
    return
  if not bstack11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૘") in CONFIG:
    CONFIG[bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૙")] = bstack11ll_opy_ (u"࠭ࠣࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩ૚")
  if bstack11ll_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭૛") in CONFIG[bstack11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૜")]:
    bstack1ll1ll1l1_opy_()
    os.environ[bstack11ll_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭૝")] = CONFIG[bstack11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૞")]
  if not bstack11ll_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭૟") in CONFIG[bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૠ")]:
    return
  bstack1l11111l1_opy_ = bstack11ll_opy_ (u"࠭ࠧૡ")
  bstack1l1ll1ll1_opy_ = bstack11ll1lll11_opy_()
  if bstack1l1ll1ll1_opy_ != -1:
    bstack1l11111l1_opy_ = bstack11ll_opy_ (u"ࠧࡄࡋࠣࠫૢ") + str(bstack1l1ll1ll1_opy_)
  if bstack1l11111l1_opy_ == bstack11ll_opy_ (u"ࠨࠩૣ"):
    bstack11l11111ll_opy_ = bstack1llll1l1ll_opy_(CONFIG[bstack11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ૤")])
    if bstack11l11111ll_opy_ != -1:
      bstack1l11111l1_opy_ = str(bstack11l11111ll_opy_)
  if bstack1l11111l1_opy_:
    bstack1ll1ll1l1l_opy_(bstack1l11111l1_opy_)
    os.environ[bstack11ll_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧ૥")] = CONFIG[bstack11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૦")]
def bstack1l11l111l_opy_(bstack111ll1111l_opy_, bstack111l11ll1_opy_, path):
  json_data = {
    bstack11ll_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૧"): bstack111l11ll1_opy_
  }
  if os.path.exists(path):
    bstack1l111llll1_opy_ = json.load(open(path, bstack11ll_opy_ (u"࠭ࡲࡣࠩ૨")))
  else:
    bstack1l111llll1_opy_ = {}
  bstack1l111llll1_opy_[bstack111ll1111l_opy_] = json_data
  with open(path, bstack11ll_opy_ (u"ࠢࡸ࠭ࠥ૩")) as outfile:
    json.dump(bstack1l111llll1_opy_, outfile)
def bstack1llll1l1ll_opy_(bstack111ll1111l_opy_):
  bstack111ll1111l_opy_ = str(bstack111ll1111l_opy_)
  bstack1l1ll1ll11_opy_ = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠨࢀࠪ૪")), bstack11ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ૫"))
  try:
    if not os.path.exists(bstack1l1ll1ll11_opy_):
      os.makedirs(bstack1l1ll1ll11_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠪࢂࠬ૬")), bstack11ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ૭"), bstack11ll_opy_ (u"ࠬ࠴ࡢࡶ࡫࡯ࡨ࠲ࡴࡡ࡮ࡧ࠰ࡧࡦࡩࡨࡦ࠰࡭ࡷࡴࡴࠧ૮"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11ll_opy_ (u"࠭ࡷࠨ૯")):
        pass
      with open(file_path, bstack11ll_opy_ (u"ࠢࡸ࠭ࠥ૰")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11ll_opy_ (u"ࠨࡴࠪ૱")) as bstack11l1111ll1_opy_:
      bstack1l1l11l1l_opy_ = json.load(bstack11l1111ll1_opy_)
    if bstack111ll1111l_opy_ in bstack1l1l11l1l_opy_:
      bstack1llll1l1l1_opy_ = bstack1l1l11l1l_opy_[bstack111ll1111l_opy_][bstack11ll_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૲")]
      bstack1ll11l1ll1_opy_ = int(bstack1llll1l1l1_opy_) + 1
      bstack1l11l111l_opy_(bstack111ll1111l_opy_, bstack1ll11l1ll1_opy_, file_path)
      return bstack1ll11l1ll1_opy_
    else:
      bstack1l11l111l_opy_(bstack111ll1111l_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1l111ll1ll_opy_.format(str(e)))
    return -1
def bstack1llll1lll1_opy_(config):
  if not config[bstack11ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ૳")] or not config[bstack11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ૴")]:
    return True
  else:
    return False
def bstack1l1l111ll_opy_(config, index=0):
  global bstack1l111ll1l1_opy_
  bstack111lllll1_opy_ = {}
  caps = bstack1ll1l111l_opy_ + bstack1ll1l11l1l_opy_
  if config.get(bstack11ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ૵"), False):
    bstack111lllll1_opy_[bstack11ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪ૶")] = True
    bstack111lllll1_opy_[bstack11ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ૷")] = config.get(bstack11ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷࠬ૸"), {})
  if bstack1l111ll1l1_opy_:
    caps += bstack111ll11ll_opy_
  for key in config:
    if key in caps + [bstack11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬૹ")]:
      continue
    bstack111lllll1_opy_[key] = config[key]
  if bstack11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ૺ") in config:
    for bstack1ll1l11l1_opy_ in config[bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧૻ")][index]:
      if bstack1ll1l11l1_opy_ in caps:
        continue
      bstack111lllll1_opy_[bstack1ll1l11l1_opy_] = config[bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૼ")][index][bstack1ll1l11l1_opy_]
  bstack111lllll1_opy_[bstack11ll_opy_ (u"࠭ࡨࡰࡵࡷࡒࡦࡳࡥࠨ૽")] = socket.gethostname()
  if bstack11ll_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ૾") in bstack111lllll1_opy_:
    del (bstack111lllll1_opy_[bstack11ll_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ૿")])
  return bstack111lllll1_opy_
def bstack1ll111ll1_opy_(config):
  global bstack1l111ll1l1_opy_
  bstack1ll1lll1l1_opy_ = {}
  caps = bstack1ll1l11l1l_opy_
  if bstack1l111ll1l1_opy_:
    caps += bstack111ll11ll_opy_
  for key in caps:
    if key in config:
      bstack1ll1lll1l1_opy_[key] = config[key]
  return bstack1ll1lll1l1_opy_
def bstack11l11l1ll_opy_(bstack111lllll1_opy_, bstack1ll1lll1l1_opy_):
  bstack1l1111l1l_opy_ = {}
  for key in bstack111lllll1_opy_.keys():
    if key in bstack1lll111l11_opy_:
      bstack1l1111l1l_opy_[bstack1lll111l11_opy_[key]] = bstack111lllll1_opy_[key]
    else:
      bstack1l1111l1l_opy_[key] = bstack111lllll1_opy_[key]
  for key in bstack1ll1lll1l1_opy_:
    if key in bstack1lll111l11_opy_:
      bstack1l1111l1l_opy_[bstack1lll111l11_opy_[key]] = bstack1ll1lll1l1_opy_[key]
    else:
      bstack1l1111l1l_opy_[key] = bstack1ll1lll1l1_opy_[key]
  return bstack1l1111l1l_opy_
def bstack1l1lllll11_opy_(config, index=0):
  global bstack1l111ll1l1_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1l11l11l1l_opy_ = bstack11llllllll_opy_(bstack1l1ll1l11_opy_, config, logger)
  bstack1ll1lll1l1_opy_ = bstack1ll111ll1_opy_(config)
  bstack1l1l111lll_opy_ = bstack1ll1l11l1l_opy_
  bstack1l1l111lll_opy_ += bstack111lll1111_opy_
  bstack1ll1lll1l1_opy_ = update(bstack1ll1lll1l1_opy_, bstack1l11l11l1l_opy_)
  if bstack1l111ll1l1_opy_:
    bstack1l1l111lll_opy_ += bstack111ll11ll_opy_
  if bstack11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ଀") in config:
    if bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଁ") in config[bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଂ")][index]:
      caps[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪଃ")] = config[bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ଄")][index][bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬଅ")]
    if bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଆ") in config[bstack11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଇ")][index]:
      caps[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫଈ")] = str(config[bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଉ")][index][bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଊ")])
    bstack1ll1lll11l_opy_ = bstack11llllllll_opy_(bstack1l1ll1l11_opy_, config[bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩଋ")][index], logger)
    bstack1l1l111lll_opy_ += list(bstack1ll1lll11l_opy_.keys())
    for bstack1lll111l1l_opy_ in bstack1l1l111lll_opy_:
      if bstack1lll111l1l_opy_ in config[bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଌ")][index]:
        if bstack1lll111l1l_opy_ == bstack11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ଍"):
          try:
            bstack1ll1lll11l_opy_[bstack1lll111l1l_opy_] = str(config[bstack11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ଎")][index][bstack1lll111l1l_opy_] * 1.0)
          except:
            bstack1ll1lll11l_opy_[bstack1lll111l1l_opy_] = str(config[bstack11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଏ")][index][bstack1lll111l1l_opy_])
        else:
          bstack1ll1lll11l_opy_[bstack1lll111l1l_opy_] = config[bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଐ")][index][bstack1lll111l1l_opy_]
        del (config[bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ଑")][index][bstack1lll111l1l_opy_])
    bstack1ll1lll1l1_opy_ = update(bstack1ll1lll1l1_opy_, bstack1ll1lll11l_opy_)
  bstack111lllll1_opy_ = bstack1l1l111ll_opy_(config, index)
  for bstack1l11ll11l1_opy_ in bstack1ll1l11l1l_opy_ + list(bstack1l11l11l1l_opy_.keys()):
    if bstack1l11ll11l1_opy_ in bstack111lllll1_opy_:
      bstack1ll1lll1l1_opy_[bstack1l11ll11l1_opy_] = bstack111lllll1_opy_[bstack1l11ll11l1_opy_]
      del (bstack111lllll1_opy_[bstack1l11ll11l1_opy_])
  if bstack1l11l1l1l_opy_(config):
    bstack111lllll1_opy_[bstack11ll_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭଒")] = True
    caps.update(bstack1ll1lll1l1_opy_)
    caps[bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨଓ")] = bstack111lllll1_opy_
  else:
    bstack111lllll1_opy_[bstack11ll_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨଔ")] = False
    caps.update(bstack11l11l1ll_opy_(bstack111lllll1_opy_, bstack1ll1lll1l1_opy_))
    if bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧକ") in caps:
      caps[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫଖ")] = caps[bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଗ")]
      del (caps[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪଘ")])
    if bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧଙ") in caps:
      caps[bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩଚ")] = caps[bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଛ")]
      del (caps[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪଜ")])
  return caps
def bstack1lll11lll1_opy_():
  global bstack1lllll1l11_opy_
  global CONFIG
  if bstack11l11l11l1_opy_() <= version.parse(bstack11ll_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪଝ")):
    if bstack1lllll1l11_opy_ != bstack11ll_opy_ (u"ࠫࠬଞ"):
      return bstack11ll_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨଟ") + bstack1lllll1l11_opy_ + bstack11ll_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥଠ")
    return bstack1ll1ll111l_opy_
  if bstack1lllll1l11_opy_ != bstack11ll_opy_ (u"ࠧࠨଡ"):
    return bstack11ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥଢ") + bstack1lllll1l11_opy_ + bstack11ll_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥଣ")
  return bstack1l111lll1l_opy_
def bstack1llll11l11_opy_(options):
  return hasattr(options, bstack11ll_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫତ"))
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
def bstack1l1l1lll1l_opy_(options, bstack1l1l1lllll_opy_):
  for bstack1lll1l1l11_opy_ in bstack1l1l1lllll_opy_:
    if bstack1lll1l1l11_opy_ in [bstack11ll_opy_ (u"ࠫࡦࡸࡧࡴࠩଥ"), bstack11ll_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩଦ")]:
      continue
    if bstack1lll1l1l11_opy_ in options._experimental_options:
      options._experimental_options[bstack1lll1l1l11_opy_] = update(options._experimental_options[bstack1lll1l1l11_opy_],
                                                         bstack1l1l1lllll_opy_[bstack1lll1l1l11_opy_])
    else:
      options.add_experimental_option(bstack1lll1l1l11_opy_, bstack1l1l1lllll_opy_[bstack1lll1l1l11_opy_])
  if bstack11ll_opy_ (u"࠭ࡡࡳࡩࡶࠫଧ") in bstack1l1l1lllll_opy_:
    for arg in bstack1l1l1lllll_opy_[bstack11ll_opy_ (u"ࠧࡢࡴࡪࡷࠬନ")]:
      options.add_argument(arg)
    del (bstack1l1l1lllll_opy_[bstack11ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭଩")])
  if bstack11ll_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ପ") in bstack1l1l1lllll_opy_:
    for ext in bstack1l1l1lllll_opy_[bstack11ll_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧଫ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l1l1lllll_opy_[bstack11ll_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨବ")])
def bstack11l11l1l11_opy_(options, bstack111l11111_opy_):
  if bstack11ll_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫଭ") in bstack111l11111_opy_:
    for bstack1l1l1l111l_opy_ in bstack111l11111_opy_[bstack11ll_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬମ")]:
      if bstack1l1l1l111l_opy_ in options._preferences:
        options._preferences[bstack1l1l1l111l_opy_] = update(options._preferences[bstack1l1l1l111l_opy_], bstack111l11111_opy_[bstack11ll_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ଯ")][bstack1l1l1l111l_opy_])
      else:
        options.set_preference(bstack1l1l1l111l_opy_, bstack111l11111_opy_[bstack11ll_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧର")][bstack1l1l1l111l_opy_])
  if bstack11ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ଱") in bstack111l11111_opy_:
    for arg in bstack111l11111_opy_[bstack11ll_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଲ")]:
      options.add_argument(arg)
def bstack111111ll11_opy_(options, bstack111lllllll_opy_):
  if bstack11ll_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬଳ") in bstack111lllllll_opy_:
    options.use_webview(bool(bstack111lllllll_opy_[bstack11ll_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭଴")]))
  bstack1l1l1lll1l_opy_(options, bstack111lllllll_opy_)
def bstack11111ll11_opy_(options, bstack1l11ll111_opy_):
  for bstack1l11l111l1_opy_ in bstack1l11ll111_opy_:
    if bstack1l11l111l1_opy_ in [bstack11ll_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪଵ"), bstack11ll_opy_ (u"ࠧࡢࡴࡪࡷࠬଶ")]:
      continue
    options.set_capability(bstack1l11l111l1_opy_, bstack1l11ll111_opy_[bstack1l11l111l1_opy_])
  if bstack11ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଷ") in bstack1l11ll111_opy_:
    for arg in bstack1l11ll111_opy_[bstack11ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧସ")]:
      options.add_argument(arg)
  if bstack11ll_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧହ") in bstack1l11ll111_opy_:
    options.bstack1llll11111_opy_(bool(bstack1l11ll111_opy_[bstack11ll_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨ଺")]))
def bstack1l1ll1l1ll_opy_(options, bstack111ll1l1l_opy_):
  for bstack11l1lll11l_opy_ in bstack111ll1l1l_opy_:
    if bstack11l1lll11l_opy_ in [bstack11ll_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ଻"), bstack11ll_opy_ (u"࠭ࡡࡳࡩࡶ଼ࠫ")]:
      continue
    options._options[bstack11l1lll11l_opy_] = bstack111ll1l1l_opy_[bstack11l1lll11l_opy_]
  if bstack11ll_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଽ") in bstack111ll1l1l_opy_:
    for bstack1ll11ll1l_opy_ in bstack111ll1l1l_opy_[bstack11ll_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬା")]:
      options.bstack1l1ll11l1l_opy_(
        bstack1ll11ll1l_opy_, bstack111ll1l1l_opy_[bstack11ll_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ି")][bstack1ll11ll1l_opy_])
  if bstack11ll_opy_ (u"ࠪࡥࡷ࡭ࡳࠨୀ") in bstack111ll1l1l_opy_:
    for arg in bstack111ll1l1l_opy_[bstack11ll_opy_ (u"ࠫࡦࡸࡧࡴࠩୁ")]:
      options.add_argument(arg)
def bstack11111lll11_opy_(options, caps):
  if not hasattr(options, bstack11ll_opy_ (u"ࠬࡑࡅ࡚ࠩୂ")):
    return
  if options.KEY == bstack11ll_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫୃ"):
    options = bstack1111ll11_opy_.bstack1l1l111111_opy_(bstack1l11ll1111_opy_=options, config=CONFIG)
  if options.KEY == bstack11ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬୄ") and options.KEY in caps:
    bstack1l1l1lll1l_opy_(options, caps[bstack11ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭୅")])
  elif options.KEY == bstack11ll_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧ୆") and options.KEY in caps:
    bstack11l11l1l11_opy_(options, caps[bstack11ll_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨେ")])
  elif options.KEY == bstack11ll_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬୈ") and options.KEY in caps:
    bstack11111ll11_opy_(options, caps[bstack11ll_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭୉")])
  elif options.KEY == bstack11ll_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ୊") and options.KEY in caps:
    bstack111111ll11_opy_(options, caps[bstack11ll_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨୋ")])
  elif options.KEY == bstack11ll_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧୌ") and options.KEY in caps:
    bstack1l1ll1l1ll_opy_(options, caps[bstack11ll_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ୍")])
def bstack1111111l1_opy_(caps):
  global bstack1l111ll1l1_opy_
  if isinstance(os.environ.get(bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ୎")), str):
    bstack1l111ll1l1_opy_ = eval(os.getenv(bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ୏")))
  if bstack1l111ll1l1_opy_:
    if bstack11111111l_opy_() < version.parse(bstack11ll_opy_ (u"ࠬ࠸࠮࠴࠰࠳ࠫ୐")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭୑")
    if bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ୒") in caps:
      browser = caps[bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭୓")]
    elif bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪ୔") in caps:
      browser = caps[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫ୕")]
    browser = str(browser).lower()
    if browser == bstack11ll_opy_ (u"ࠫ࡮ࡶࡨࡰࡰࡨࠫୖ") or browser == bstack11ll_opy_ (u"ࠬ࡯ࡰࡢࡦࠪୗ"):
      browser = bstack11ll_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭୘")
    if browser == bstack11ll_opy_ (u"ࠧࡴࡣࡰࡷࡺࡴࡧࠨ୙"):
      browser = bstack11ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ୚")
    if browser not in [bstack11ll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩ୛"), bstack11ll_opy_ (u"ࠪࡩࡩ࡭ࡥࠨଡ଼"), bstack11ll_opy_ (u"ࠫ࡮࡫ࠧଢ଼"), bstack11ll_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬ୞"), bstack11ll_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧୟ")]:
      return None
    try:
      package = bstack11ll_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶ࠳ࢁࡽ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩୠ").format(browser)
      name = bstack11ll_opy_ (u"ࠨࡑࡳࡸ࡮ࡵ࡮ࡴࠩୡ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1llll11l11_opy_(options):
        return None
      for bstack1l11ll11l1_opy_ in caps.keys():
        options.set_capability(bstack1l11ll11l1_opy_, caps[bstack1l11ll11l1_opy_])
      bstack11111lll11_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1l11l1l1l1_opy_(options, bstack111l11ll11_opy_):
  if not bstack1llll11l11_opy_(options):
    return
  for bstack1l11ll11l1_opy_ in bstack111l11ll11_opy_.keys():
    if bstack1l11ll11l1_opy_ in bstack111lll1111_opy_:
      continue
    if bstack1l11ll11l1_opy_ in options._caps and type(options._caps[bstack1l11ll11l1_opy_]) in [dict, list]:
      options._caps[bstack1l11ll11l1_opy_] = update(options._caps[bstack1l11ll11l1_opy_], bstack111l11ll11_opy_[bstack1l11ll11l1_opy_])
    else:
      options.set_capability(bstack1l11ll11l1_opy_, bstack111l11ll11_opy_[bstack1l11ll11l1_opy_])
  bstack11111lll11_opy_(options, bstack111l11ll11_opy_)
  if bstack11ll_opy_ (u"ࠩࡰࡳࡿࡀࡤࡦࡤࡸ࡫࡬࡫ࡲࡂࡦࡧࡶࡪࡹࡳࠨୢ") in options._caps:
    if options._caps[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨୣ")] and options._caps[bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ୤")].lower() != bstack11ll_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭୥"):
      del options._caps[bstack11ll_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬ୦")]
def bstack1ll111lll_opy_(proxy_config):
  if bstack11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ୧") in proxy_config:
    proxy_config[bstack11ll_opy_ (u"ࠨࡵࡶࡰࡕࡸ࡯ࡹࡻࠪ୨")] = proxy_config[bstack11ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭୩")]
    del (proxy_config[bstack11ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ୪")])
  if bstack11ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧ୫") in proxy_config and proxy_config[bstack11ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ୬")].lower() != bstack11ll_opy_ (u"࠭ࡤࡪࡴࡨࡧࡹ࠭୭"):
    proxy_config[bstack11ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪ୮")] = bstack11ll_opy_ (u"ࠨ࡯ࡤࡲࡺࡧ࡬ࠨ୯")
  if bstack11ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡂࡷࡷࡳࡨࡵ࡮ࡧ࡫ࡪ࡙ࡷࡲࠧ୰") in proxy_config:
    proxy_config[bstack11ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭ୱ")] = bstack11ll_opy_ (u"ࠫࡵࡧࡣࠨ୲")
  return proxy_config
def bstack11l1lll1l_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ୳") in config:
    return proxy
  config[bstack11ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୴")] = bstack1ll111lll_opy_(config[bstack11ll_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭୵")])
  if proxy == None:
    proxy = Proxy(config[bstack11ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧ୶")])
  return proxy
def bstack11111ll11l_opy_(self):
  global CONFIG
  global bstack1l11ll1l11_opy_
  try:
    proxy = bstack111lll1l1l_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11ll_opy_ (u"ࠩ࠱ࡴࡦࡩࠧ୷")):
        proxies = bstack111ll1l1ll_opy_(proxy, bstack1lll11lll1_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1111111_opy_ = proxies.popitem()
          if bstack11ll_opy_ (u"ࠥ࠾࠴࠵ࠢ୸") in bstack1l1111111_opy_:
            return bstack1l1111111_opy_
          else:
            return bstack11ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧ୹") + bstack1l1111111_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡲࡵࡳࡽࡿࠠࡶࡴ࡯ࠤ࠿ࠦࡻࡾࠤ୺").format(str(e)))
  return bstack1l11ll1l11_opy_(self)
def bstack11lll111l_opy_():
  global CONFIG
  return bstack11l1l1l1l1_opy_(CONFIG) and bstack11llll1l1l_opy_() and bstack11l11l11l1_opy_() >= version.parse(bstack11l1l1l111_opy_)
def bstack1ll1l1l111_opy_():
  global CONFIG
  return (bstack11ll_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ୻") in CONFIG or bstack11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ୼") in CONFIG) and bstack1l1llll111_opy_()
def bstack11l1l1ll1l_opy_(config):
  bstack1lll11l1l1_opy_ = {}
  if bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୽") in config:
    bstack1lll11l1l1_opy_ = config[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୾")]
  if bstack11ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୿") in config:
    bstack1lll11l1l1_opy_ = config[bstack11ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ஀")]
  proxy = bstack111lll1l1l_opy_(config)
  if proxy:
    if proxy.endswith(bstack11ll_opy_ (u"ࠬ࠴ࡰࡢࡥࠪ஁")) and os.path.isfile(proxy):
      bstack1lll11l1l1_opy_[bstack11ll_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩஂ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11ll_opy_ (u"ࠧ࠯ࡲࡤࡧࠬஃ")):
        proxies = bstack1l1lll1l1l_opy_(config, bstack1lll11lll1_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1111111_opy_ = proxies.popitem()
          if bstack11ll_opy_ (u"ࠣ࠼࠲࠳ࠧ஄") in bstack1l1111111_opy_:
            parsed_url = urlparse(bstack1l1111111_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11ll_opy_ (u"ࠤ࠽࠳࠴ࠨஅ") + bstack1l1111111_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1lll11l1l1_opy_[bstack11ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭ஆ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1lll11l1l1_opy_[bstack11ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡳࡷࡺࠧஇ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1lll11l1l1_opy_[bstack11ll_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨஈ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1lll11l1l1_opy_[bstack11ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩஉ")] = str(parsed_url.password)
  return bstack1lll11l1l1_opy_
def bstack1l1ll11l1_opy_(config):
  if bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬஊ") in config:
    return config[bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭஋")]
  return {}
def bstack1lll1ll1ll_opy_(caps):
  global bstack111l1l11l_opy_
  if bstack11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ஌") in caps:
    caps[bstack11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ஍")][bstack11ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪஎ")] = True
    if bstack111l1l11l_opy_:
      caps[bstack11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ஏ")][bstack11ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨஐ")] = bstack111l1l11l_opy_
  else:
    caps[bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬ஑")] = True
    if bstack111l1l11l_opy_:
      caps[bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩஒ")] = bstack111l1l11l_opy_
@measure(event_name=EVENTS.bstack1l1l1lll11_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack111l1lllll_opy_():
  global CONFIG
  if not bstack1ll11llll1_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ஓ") in CONFIG and bstack1lll1l1lll_opy_(CONFIG[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧஔ")]):
    if (
      bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨக") in CONFIG
      and bstack1lll1l1lll_opy_(CONFIG[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ஖")].get(bstack11ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠪ஗")))
    ):
      logger.debug(bstack11ll_opy_ (u"ࠢࡍࡱࡦࡥࡱࠦࡢࡪࡰࡤࡶࡾࠦ࡮ࡰࡶࠣࡷࡹࡧࡲࡵࡧࡧࠤࡦࡹࠠࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡦࡰࡤࡦࡱ࡫ࡤࠣ஘"))
      return
    bstack1lll11l1l1_opy_ = bstack11l1l1ll1l_opy_(CONFIG)
    bstack111l11l111_opy_(CONFIG[bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫங")], bstack1lll11l1l1_opy_)
def bstack111l11l111_opy_(key, bstack1lll11l1l1_opy_):
  global bstack111l111111_opy_
  logger.info(bstack11l111l11_opy_)
  try:
    bstack111l111111_opy_ = Local()
    bstack1l1lll11l_opy_ = {bstack11ll_opy_ (u"ࠩ࡮ࡩࡾ࠭ச"): key}
    bstack1l1lll11l_opy_.update(bstack1lll11l1l1_opy_)
    logger.debug(bstack111111ll1_opy_.format(str(bstack1l1lll11l_opy_)).replace(key, bstack11ll_opy_ (u"ࠪ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧ஛")))
    bstack111l111111_opy_.start(**bstack1l1lll11l_opy_)
    if bstack111l111111_opy_.isRunning():
      logger.info(bstack1111ll1ll_opy_)
  except Exception as e:
    bstack1ll111111l_opy_(bstack1l111111ll_opy_.format(str(e)))
def bstack111l1111ll_opy_():
  global bstack111l111111_opy_
  if bstack111l111111_opy_.isRunning():
    logger.info(bstack1l1l1ll1ll_opy_)
    bstack111l111111_opy_.stop()
  bstack111l111111_opy_ = None
def bstack1l11l1l11l_opy_(bstack111l1lll1_opy_=[]):
  global CONFIG
  bstack1l1l11lll1_opy_ = []
  bstack1lllll1ll1_opy_ = [bstack11ll_opy_ (u"ࠫࡴࡹࠧஜ"), bstack11ll_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ஝"), bstack11ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪஞ"), bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩட"), bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭஠"), bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ஡")]
  try:
    for err in bstack111l1lll1_opy_:
      bstack11111ll111_opy_ = {}
      for k in bstack1lllll1ll1_opy_:
        val = CONFIG[bstack11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭஢")][int(err[bstack11ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪண")])].get(k)
        if val:
          bstack11111ll111_opy_[k] = val
      if(err[bstack11ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫத")] != bstack11ll_opy_ (u"࠭ࠧ஥")):
        bstack11111ll111_opy_[bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸࡸ࠭஦")] = {
          err[bstack11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭஧")]: err[bstack11ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨந")]
        }
        bstack1l1l11lll1_opy_.append(bstack11111ll111_opy_)
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬࡯ࡳ࡯ࡤࡸࡹ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶ࠽ࠤࠬன") + str(e))
  finally:
    return bstack1l1l11lll1_opy_
def bstack1l1111lll_opy_(file_name):
  bstack11l1111lll_opy_ = []
  try:
    bstack1l1l1111l_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1l1l1111l_opy_):
      with open(bstack1l1l1111l_opy_) as f:
        bstack1l11l11lll_opy_ = json.load(f)
        bstack11l1111lll_opy_ = bstack1l11l11lll_opy_
      os.remove(bstack1l1l1111l_opy_)
    return bstack11l1111lll_opy_
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡪࡰࡧ࡭ࡳ࡭ࠠࡦࡴࡵࡳࡷࠦ࡬ࡪࡵࡷ࠾ࠥ࠭ப") + str(e))
    return bstack11l1111lll_opy_
def bstack1111l1lll1_opy_():
  try:
      from bstack_utils.constants import bstack11111l1lll_opy_, EVENTS
      from bstack_utils.helper import bstack1ll1l1lll_opy_, get_host_info, bstack1111l111_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack1l1111ll1_opy_ = os.path.join(os.getcwd(), bstack11ll_opy_ (u"ࠬࡲ࡯ࡨࠩ஫"), bstack11ll_opy_ (u"࠭࡫ࡦࡻ࠰ࡱࡪࡺࡲࡪࡥࡶ࠲࡯ࡹ࡯࡯ࠩ஬"))
      lock = FileLock(bstack1l1111ll1_opy_+bstack11ll_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨ஭"))
      def bstack1ll1lll1_opy_():
          try:
              with lock:
                  with open(bstack1l1111ll1_opy_, bstack11ll_opy_ (u"ࠣࡴࠥம"), encoding=bstack11ll_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣய")) as file:
                      data = json.load(file)
                      config = {
                          bstack11ll_opy_ (u"ࠥ࡬ࡪࡧࡤࡦࡴࡶࠦர"): {
                              bstack11ll_opy_ (u"ࠦࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠥற"): bstack11ll_opy_ (u"ࠧࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠣல"),
                          }
                      }
                      bstack11ll1111l1_opy_ = datetime.utcnow()
                      bstack1lll1111_opy_ = bstack11ll1111l1_opy_.strftime(bstack11ll_opy_ (u"ࠨ࡚ࠥ࠯ࠨࡱ࠲ࠫࡤࡕࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࠱ࠩ࡫ࠦࡕࡕࡅࠥள"))
                      test_id = os.environ.get(bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬழ")) if os.environ.get(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭வ")) else bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦஶ"))
                      payload = {
                          bstack11ll_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠢஷ"): bstack11ll_opy_ (u"ࠦࡸࡪ࡫ࡠࡧࡹࡩࡳࡺࡳࠣஸ"),
                          bstack11ll_opy_ (u"ࠧࡪࡡࡵࡣࠥஹ"): {
                              bstack11ll_opy_ (u"ࠨࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡶࡷ࡬ࡨࠧ஺"): test_id,
                              bstack11ll_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫ࡤࡠࡦࡤࡽࠧ஻"): bstack1lll1111_opy_,
                              bstack11ll_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟࡯ࡣࡰࡩࠧ஼"): bstack11ll_opy_ (u"ࠤࡖࡈࡐࡌࡥࡢࡶࡸࡶࡪࡖࡥࡳࡨࡲࡶࡲࡧ࡮ࡤࡧࠥ஽"),
                              bstack11ll_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡ࡭ࡷࡴࡴࠢா"): {
                                  bstack11ll_opy_ (u"ࠦࡲ࡫ࡡࡴࡷࡵࡩࡸࠨி"): data,
                                  bstack11ll_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢீ"): bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣு"))
                              },
                              bstack11ll_opy_ (u"ࠢࡶࡵࡨࡶࡤࡪࡡࡵࡣࠥூ"): bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠣࡷࡶࡩࡷࡔࡡ࡮ࡧࠥ௃")),
                              bstack11ll_opy_ (u"ࠤ࡫ࡳࡸࡺ࡟ࡪࡰࡩࡳࠧ௄"): get_host_info()
                          }
                      }
                      bstack1111l1l1l_opy_ = bstack111ll111l1_opy_(cli.config, [bstack11ll_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ௅"), bstack11ll_opy_ (u"ࠦࡪࡪࡳࡊࡰࡶࡸࡷࡻ࡭ࡦࡰࡷࡥࡹ࡯࡯࡯ࠤெ"), bstack11ll_opy_ (u"ࠧࡧࡰࡪࠤே")], bstack11111l1lll_opy_)
                      response = bstack1ll1l1lll_opy_(bstack11ll_opy_ (u"ࠨࡐࡐࡕࡗࠦை"), bstack1111l1l1l_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack11ll_opy_ (u"ࠢࡅࡣࡷࡥࠥࡹࡥ࡯ࡶࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺࠢࡷࡳࠥࢁࡽࠡࡹ࡬ࡸ࡭ࠦࡤࡢࡶࡤࠤࢀࢃࠢ௉").format(bstack11111l1lll_opy_, payload))
                      else:
                          logger.debug(bstack11ll_opy_ (u"ࠣࡔࡨࡵࡺ࡫ࡳࡵࠢࡩࡥ࡮ࡲࡥࡥࠢࡩࡳࡷࠦࡻࡾࠢࡺ࡭ࡹ࡮ࠠࡥࡣࡷࡥࠥࢁࡽࠣொ").format(bstack11111l1lll_opy_, payload))
          except Exception as e:
              logger.debug(bstack11ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥ࡯ࡦࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳࠡࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣࡿࢂࠨோ").format(e))
      bstack1ll1lll1_opy_()
      bstack1ll111l1l1_opy_(bstack1l1111ll1_opy_, logger)
  except:
    pass
def bstack111llll1l1_opy_():
  global bstack1llll111ll_opy_
  global bstack1111lll1l_opy_
  global bstack11llll1l1_opy_
  global bstack1l11llllll_opy_
  global bstack1111l1l111_opy_
  global bstack1111l1ll11_opy_
  global CONFIG
  bstack1l11ll1l1l_opy_ = os.environ.get(bstack11ll_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫௌ"))
  if bstack1l11ll1l1l_opy_ in [bstack11ll_opy_ (u"ࠫࡷࡵࡢࡰࡶ்ࠪ"), bstack11ll_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ௎")]:
    bstack111ll1l1l1_opy_()
  percy.shutdown()
  if bstack1llll111ll_opy_:
    logger.warning(bstack11ll111ll_opy_.format(str(bstack1llll111ll_opy_)))
  else:
    try:
      bstack1l111llll1_opy_ = bstack111111l111_opy_(bstack11ll_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬ௏"), logger)
      if bstack1l111llll1_opy_.get(bstack11ll_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬௐ")) and bstack1l111llll1_opy_.get(bstack11ll_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭௑")).get(bstack11ll_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫ௒")):
        logger.warning(bstack11ll111ll_opy_.format(str(bstack1l111llll1_opy_[bstack11ll_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨ௓")][bstack11ll_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭௔")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1111l11l11_opy_.invoke(Events.bstack1l111l1l11_opy_)
  logger.info(bstack1ll1l111l1_opy_)
  global bstack111l111111_opy_
  if bstack111l111111_opy_:
    bstack111l1111ll_opy_()
  try:
    with bstack1l11l1lll1_opy_:
      bstack1l1l11l11l_opy_ = bstack1111lll1l_opy_.copy()
    for driver in bstack1l1l11l11l_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1llll11lll_opy_)
  if bstack1111l1ll11_opy_ == bstack11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ௕"):
    bstack1111l1l111_opy_ = bstack1l1111lll_opy_(bstack11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧ௖"))
  if bstack1111l1ll11_opy_ == bstack11ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧௗ") and len(bstack1l11llllll_opy_) == 0:
    bstack1l11llllll_opy_ = bstack1l1111lll_opy_(bstack11ll_opy_ (u"ࠨࡲࡺࡣࡵࡿࡴࡦࡵࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭௘"))
    if len(bstack1l11llllll_opy_) == 0:
      bstack1l11llllll_opy_ = bstack1l1111lll_opy_(bstack11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡳࡴࡵࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨ௙"))
  bstack11ll1l1lll_opy_ = bstack11ll_opy_ (u"ࠪࠫ௚")
  if len(bstack11llll1l1_opy_) > 0:
    bstack11ll1l1lll_opy_ = bstack1l11l1l11l_opy_(bstack11llll1l1_opy_)
  elif len(bstack1l11llllll_opy_) > 0:
    bstack11ll1l1lll_opy_ = bstack1l11l1l11l_opy_(bstack1l11llllll_opy_)
  elif len(bstack1111l1l111_opy_) > 0:
    bstack11ll1l1lll_opy_ = bstack1l11l1l11l_opy_(bstack1111l1l111_opy_)
  elif len(bstack11l1l1l11l_opy_) > 0:
    bstack11ll1l1lll_opy_ = bstack1l11l1l11l_opy_(bstack11l1l1l11l_opy_)
  if bool(bstack11ll1l1lll_opy_):
    bstack111l1llll1_opy_(bstack11ll1l1lll_opy_)
  else:
    bstack111l1llll1_opy_()
  bstack1ll111l1l1_opy_(bstack11111l11l1_opy_, logger)
  if bstack1l11ll1l1l_opy_ not in [bstack11ll_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ௛")]:
    bstack1111l1lll1_opy_()
  bstack11l1l1l1ll_opy_.bstack1l11l1ll_opy_(CONFIG)
  if len(bstack1111l1l111_opy_) > 0:
    sys.exit(len(bstack1111l1l111_opy_))
def bstack11ll1ll11_opy_(bstack111l11l1ll_opy_, frame):
  global bstack1111l111_opy_
  logger.error(bstack1ll111l111_opy_)
  bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱࡔ࡯ࠨ௜"), bstack111l11l1ll_opy_)
  if hasattr(signal, bstack11ll_opy_ (u"࠭ࡓࡪࡩࡱࡥࡱࡹࠧ௝")):
    bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ௞"), signal.Signals(bstack111l11l1ll_opy_).name)
  else:
    bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ௟"), bstack11ll_opy_ (u"ࠩࡖࡍࡌ࡛ࡎࡌࡐࡒ࡛ࡓ࠭௠"))
  if cli.is_running():
    bstack1111l11l11_opy_.invoke(Events.bstack1l111l1l11_opy_)
  bstack1l11ll1l1l_opy_ = os.environ.get(bstack11ll_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫ௡"))
  if bstack1l11ll1l1l_opy_ == bstack11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ௢") and not cli.is_enabled(CONFIG):
    bstack1l111l1l_opy_.stop(bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ௣")))
  bstack111llll1l1_opy_()
  sys.exit(1)
def bstack1ll111111l_opy_(err):
  logger.critical(bstack11l1111l11_opy_.format(str(err)))
  bstack111l1llll1_opy_(bstack11l1111l11_opy_.format(str(err)), True)
  atexit.unregister(bstack111llll1l1_opy_)
  bstack111ll1l1l1_opy_()
  sys.exit(1)
def bstack1lll11llll_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack111l1llll1_opy_(message, True)
  atexit.unregister(bstack111llll1l1_opy_)
  bstack111ll1l1l1_opy_()
  sys.exit(1)
def bstack1lll111111_opy_():
  global CONFIG
  global bstack1ll11llll_opy_
  global bstack1111ll1l1_opy_
  global bstack1ll1l1111_opy_
  CONFIG = bstack11l1ll111_opy_()
  load_dotenv(CONFIG.get(bstack11ll_opy_ (u"࠭ࡥ࡯ࡸࡉ࡭ࡱ࡫ࠧ௤")))
  bstack11l1l1111_opy_()
  bstack1llllll1l1_opy_()
  CONFIG = bstack1111lll1l1_opy_(CONFIG)
  update(CONFIG, bstack1111ll1l1_opy_)
  update(CONFIG, bstack1ll11llll_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1ll1llll11_opy_(CONFIG)
  bstack1ll1l1111_opy_ = bstack1ll11llll1_opy_(CONFIG)
  os.environ[bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪ௥")] = bstack1ll1l1111_opy_.__str__().lower()
  bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ௦"), bstack1ll1l1111_opy_)
  if (bstack11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௧") in CONFIG and bstack11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௨") in bstack1ll11llll_opy_) or (
          bstack11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௩") in CONFIG and bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௪") not in bstack1111ll1l1_opy_):
    if os.getenv(bstack11ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪ௫")):
      CONFIG[bstack11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ௬")] = os.getenv(bstack11ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ௭"))
    else:
      if not CONFIG.get(bstack11ll_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠧ௮"), bstack11ll_opy_ (u"ࠥࠦ௯")) in bstack111l11l11_opy_:
        bstack11ll111l1l_opy_()
  elif (bstack11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௰") not in CONFIG and bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ௱") in CONFIG) or (
          bstack11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௲") in bstack1111ll1l1_opy_ and bstack11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ௳") not in bstack1ll11llll_opy_):
    del (CONFIG[bstack11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ௴")])
  if bstack1llll1lll1_opy_(CONFIG):
    bstack1ll111111l_opy_(bstack1ll1ll1111_opy_)
  Config.bstack11111ll1_opy_().set_property(bstack11ll_opy_ (u"ࠤࡸࡷࡪࡸࡎࡢ࡯ࡨࠦ௵"), CONFIG[bstack11ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ௶")])
  bstack1l11ll1l1_opy_()
  bstack1l11111ll1_opy_()
  if bstack1l111ll1l1_opy_ and not CONFIG.get(bstack11ll_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠢ௷"), bstack11ll_opy_ (u"ࠧࠨ௸")) in bstack111l11l11_opy_:
    CONFIG[bstack11ll_opy_ (u"࠭ࡡࡱࡲࠪ௹")] = bstack111lll11l_opy_(CONFIG)
    logger.info(bstack1lll1lll1l_opy_.format(CONFIG[bstack11ll_opy_ (u"ࠧࡢࡲࡳࠫ௺")]))
  if not bstack1ll1l1111_opy_:
    CONFIG[bstack11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௻")] = [{}]
def bstack11l111lll_opy_(config, bstack11ll11l11_opy_):
  global CONFIG
  global bstack1l111ll1l1_opy_
  CONFIG = config
  bstack1l111ll1l1_opy_ = bstack11ll11l11_opy_
def bstack1l11111ll1_opy_():
  global CONFIG
  global bstack1l111ll1l1_opy_
  if bstack11ll_opy_ (u"ࠩࡤࡴࡵ࠭௼") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack1lll1l1ll1_opy_)
    bstack1l111ll1l1_opy_ = True
    bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ௽"), True)
def bstack111lll11l_opy_(config):
  bstack1lll1l11l1_opy_ = bstack11ll_opy_ (u"ࠫࠬ௾")
  app = config[bstack11ll_opy_ (u"ࠬࡧࡰࡱࠩ௿")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1l1ll1l1l_opy_:
      if os.path.exists(app):
        bstack1lll1l11l1_opy_ = bstack11l1ll11l_opy_(config, app)
      elif bstack11l1l1l1l_opy_(app):
        bstack1lll1l11l1_opy_ = app
      else:
        bstack1ll111111l_opy_(bstack11lllllll1_opy_.format(app))
    else:
      if bstack11l1l1l1l_opy_(app):
        bstack1lll1l11l1_opy_ = app
      elif os.path.exists(app):
        bstack1lll1l11l1_opy_ = bstack11l1ll11l_opy_(app)
      else:
        bstack1ll111111l_opy_(bstack11lll1ll1l_opy_)
  else:
    if len(app) > 2:
      bstack1ll111111l_opy_(bstack1l1111111l_opy_)
    elif len(app) == 2:
      if bstack11ll_opy_ (u"࠭ࡰࡢࡶ࡫ࠫఀ") in app and bstack11ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪఁ") in app:
        if os.path.exists(app[bstack11ll_opy_ (u"ࠨࡲࡤࡸ࡭࠭ం")]):
          bstack1lll1l11l1_opy_ = bstack11l1ll11l_opy_(config, app[bstack11ll_opy_ (u"ࠩࡳࡥࡹ࡮ࠧః")], app[bstack11ll_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭ఄ")])
        else:
          bstack1ll111111l_opy_(bstack11lllllll1_opy_.format(app))
      else:
        bstack1ll111111l_opy_(bstack1l1111111l_opy_)
    else:
      for key in app:
        if key in bstack1l1lll1ll_opy_:
          if key == bstack11ll_opy_ (u"ࠫࡵࡧࡴࡩࠩఅ"):
            if os.path.exists(app[key]):
              bstack1lll1l11l1_opy_ = bstack11l1ll11l_opy_(config, app[key])
            else:
              bstack1ll111111l_opy_(bstack11lllllll1_opy_.format(app))
          else:
            bstack1lll1l11l1_opy_ = app[key]
        else:
          bstack1ll111111l_opy_(bstack11l1ll1ll_opy_)
  return bstack1lll1l11l1_opy_
def bstack11l1l1l1l_opy_(bstack1lll1l11l1_opy_):
  import re
  bstack11l1l1ll1_opy_ = re.compile(bstack11ll_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧఆ"))
  bstack11lllll1l_opy_ = re.compile(bstack11ll_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮࠴ࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥఇ"))
  if bstack11ll_opy_ (u"ࠧࡣࡵ࠽࠳࠴࠭ఈ") in bstack1lll1l11l1_opy_ or re.fullmatch(bstack11l1l1ll1_opy_, bstack1lll1l11l1_opy_) or re.fullmatch(bstack11lllll1l_opy_, bstack1lll1l11l1_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack11l11ll11_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack11l1ll11l_opy_(config, path, bstack1ll1l1l11_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11ll_opy_ (u"ࠨࡴࡥࠫఉ")).read()).hexdigest()
  bstack1l111l11ll_opy_ = bstack1l11lll11_opy_(md5_hash)
  bstack1lll1l11l1_opy_ = None
  if bstack1l111l11ll_opy_:
    logger.info(bstack11ll111ll1_opy_.format(bstack1l111l11ll_opy_, md5_hash))
    return bstack1l111l11ll_opy_
  bstack1l11111lll_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧఊ"): (os.path.basename(path), open(os.path.abspath(path), bstack11ll_opy_ (u"ࠪࡶࡧ࠭ఋ")), bstack11ll_opy_ (u"ࠫࡹ࡫ࡸࡵ࠱ࡳࡰࡦ࡯࡮ࠨఌ")),
      bstack11ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ఍"): bstack1ll1l1l11_opy_
    }
  )
  response = requests.post(bstack1l1lllllll_opy_, data=multipart_data,
                           headers={bstack11ll_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬఎ"): multipart_data.content_type},
                           auth=(config[bstack11ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩఏ")], config[bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫఐ")]))
  try:
    res = json.loads(response.text)
    bstack1lll1l11l1_opy_ = res[bstack11ll_opy_ (u"ࠩࡤࡴࡵࡥࡵࡳ࡮ࠪ఑")]
    logger.info(bstack11l1l11l1_opy_.format(bstack1lll1l11l1_opy_))
    bstack1lll11l1ll_opy_(md5_hash, bstack1lll1l11l1_opy_)
    cli.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡷࡳࡰࡴࡧࡤࡠࡣࡳࡴࠧఒ"), datetime.datetime.now() - bstack1l11111lll_opy_)
  except ValueError as err:
    bstack1ll111111l_opy_(bstack1l11l1ll1_opy_.format(str(err)))
  return bstack1lll1l11l1_opy_
def bstack1l11ll1l1_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1lllll111l_opy_
  bstack1ll1llll1_opy_ = 1
  bstack1l111l1l1l_opy_ = 1
  if bstack11ll_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫఓ") in CONFIG:
    bstack1l111l1l1l_opy_ = CONFIG[bstack11ll_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬఔ")]
  else:
    bstack1l111l1l1l_opy_ = bstack1111111ll_opy_(framework_name, args) or 1
  if bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩక") in CONFIG:
    bstack1ll1llll1_opy_ = len(CONFIG[bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪఖ")])
  bstack1lllll111l_opy_ = int(bstack1l111l1l1l_opy_) * int(bstack1ll1llll1_opy_)
def bstack1111111ll_opy_(framework_name, args):
  if framework_name == bstack11ll1ll1l1_opy_ and args and bstack11ll_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭గ") in args:
      bstack1ll1ll1ll1_opy_ = args.index(bstack11ll_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧఘ"))
      return int(args[bstack1ll1ll1ll1_opy_ + 1]) or 1
  return 1
def bstack1l11lll11_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭ఙ"))
    bstack11l11llll1_opy_ = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠫࢃ࠭చ")), bstack11ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬఛ"), bstack11ll_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧజ"))
    if os.path.exists(bstack11l11llll1_opy_):
      try:
        bstack1l11l1ll1l_opy_ = json.load(open(bstack11l11llll1_opy_, bstack11ll_opy_ (u"ࠧࡳࡤࠪఝ")))
        if md5_hash in bstack1l11l1ll1l_opy_:
          bstack1l1ll1l111_opy_ = bstack1l11l1ll1l_opy_[md5_hash]
          bstack1ll1l1llll_opy_ = datetime.datetime.now()
          bstack1ll11l1111_opy_ = datetime.datetime.strptime(bstack1l1ll1l111_opy_[bstack11ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫఞ")], bstack11ll_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ట"))
          if (bstack1ll1l1llll_opy_ - bstack1ll11l1111_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack1l1ll1l111_opy_[bstack11ll_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨఠ")]):
            return None
          return bstack1l1ll1l111_opy_[bstack11ll_opy_ (u"ࠫ࡮ࡪࠧడ")]
      except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮ࠠࡧ࡫࡯ࡩ࠿ࠦࡻࡾࠩఢ").format(str(e)))
    return None
  bstack11l11llll1_opy_ = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"࠭ࡾࠨణ")), bstack11ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧత"), bstack11ll_opy_ (u"ࠨࡣࡳࡴ࡚ࡶ࡬ࡰࡣࡧࡑࡉ࠻ࡈࡢࡵ࡫࠲࡯ࡹ࡯࡯ࠩథ"))
  lock_file = bstack11l11llll1_opy_ + bstack11ll_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨద")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack11l11llll1_opy_):
        with open(bstack11l11llll1_opy_, bstack11ll_opy_ (u"ࠪࡶࠬధ")) as f:
          content = f.read().strip()
          if content:
            bstack1l11l1ll1l_opy_ = json.loads(content)
            if md5_hash in bstack1l11l1ll1l_opy_:
              bstack1l1ll1l111_opy_ = bstack1l11l1ll1l_opy_[md5_hash]
              bstack1ll1l1llll_opy_ = datetime.datetime.now()
              bstack1ll11l1111_opy_ = datetime.datetime.strptime(bstack1l1ll1l111_opy_[bstack11ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧన")], bstack11ll_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩ఩"))
              if (bstack1ll1l1llll_opy_ - bstack1ll11l1111_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack1l1ll1l111_opy_[bstack11ll_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫప")]):
                return None
              return bstack1l1ll1l111_opy_[bstack11ll_opy_ (u"ࠧࡪࡦࠪఫ")]
      return None
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡸ࡫ࡷ࡬ࠥ࡬ࡩ࡭ࡧࠣࡰࡴࡩ࡫ࡪࡰࡪࠤ࡫ࡵࡲࠡࡏࡇ࠹ࠥ࡮ࡡࡴࡪ࠽ࠤࢀࢃࠧబ").format(str(e)))
    return None
def bstack1lll11l1ll_opy_(md5_hash, bstack1lll1l11l1_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬభ"))
    bstack1l1ll1ll11_opy_ = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠪࢂࠬమ")), bstack11ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫయ"))
    if not os.path.exists(bstack1l1ll1ll11_opy_):
      os.makedirs(bstack1l1ll1ll11_opy_)
    bstack11l11llll1_opy_ = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠬࢄࠧర")), bstack11ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ఱ"), bstack11ll_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨల"))
    bstack1l1l1l1ll1_opy_ = {
      bstack11ll_opy_ (u"ࠨ࡫ࡧࠫళ"): bstack1lll1l11l1_opy_,
      bstack11ll_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬఴ"): datetime.datetime.strftime(datetime.datetime.now(), bstack11ll_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧవ")),
      bstack11ll_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩశ"): str(__version__)
    }
    try:
      bstack1l11l1ll1l_opy_ = {}
      if os.path.exists(bstack11l11llll1_opy_):
        bstack1l11l1ll1l_opy_ = json.load(open(bstack11l11llll1_opy_, bstack11ll_opy_ (u"ࠬࡸࡢࠨష")))
      bstack1l11l1ll1l_opy_[md5_hash] = bstack1l1l1l1ll1_opy_
      with open(bstack11l11llll1_opy_, bstack11ll_opy_ (u"ࠨࡷࠬࠤస")) as outfile:
        json.dump(bstack1l11l1ll1l_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡵࡱࡦࡤࡸ࡮ࡴࡧࠡࡏࡇ࠹ࠥ࡮ࡡࡴࡪࠣࡪ࡮ࡲࡥ࠻ࠢࡾࢁࠬహ").format(str(e)))
    return
  bstack1l1ll1ll11_opy_ = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠨࢀࠪ఺")), bstack11ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ఻"))
  if not os.path.exists(bstack1l1ll1ll11_opy_):
    os.makedirs(bstack1l1ll1ll11_opy_)
  bstack11l11llll1_opy_ = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠪࢂ఼ࠬ")), bstack11ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఽ"), bstack11ll_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ా"))
  lock_file = bstack11l11llll1_opy_ + bstack11ll_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬి")
  bstack1l1l1l1ll1_opy_ = {
    bstack11ll_opy_ (u"ࠧࡪࡦࠪీ"): bstack1lll1l11l1_opy_,
    bstack11ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫు"): datetime.datetime.strftime(datetime.datetime.now(), bstack11ll_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ూ")),
    bstack11ll_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨృ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1l11l1ll1l_opy_ = {}
      if os.path.exists(bstack11l11llll1_opy_):
        with open(bstack11l11llll1_opy_, bstack11ll_opy_ (u"ࠫࡷ࠭ౄ")) as f:
          content = f.read().strip()
          if content:
            bstack1l11l1ll1l_opy_ = json.loads(content)
      bstack1l11l1ll1l_opy_[md5_hash] = bstack1l1l1l1ll1_opy_
      with open(bstack11l11llll1_opy_, bstack11ll_opy_ (u"ࠧࡽࠢ౅")) as outfile:
        json.dump(bstack1l11l1ll1l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡽࡩࡵࡪࠣࡪ࡮ࡲࡥࠡ࡮ࡲࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨࠡࡷࡳࡨࡦࡺࡥ࠻ࠢࡾࢁࠬె").format(str(e)))
def bstack1l111ll1l_opy_(self):
  return
def bstack1l1111llll_opy_(self):
  return
def bstack1ll11l1l1_opy_():
  global bstack11l11ll1l1_opy_
  bstack11l11ll1l1_opy_ = True
@measure(event_name=EVENTS.bstack1lll1llll1_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack11ll11ll11_opy_(self):
  global bstack11l11l111l_opy_
  global bstack1l1ll1111l_opy_
  global bstack1l111lllll_opy_
  try:
    if bstack11ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧే") in bstack11l11l111l_opy_ and self.session_id != None and bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬై"), bstack11ll_opy_ (u"ࠩࠪ౉")) != bstack11ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫొ"):
      bstack11l11l1ll1_opy_ = bstack11ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫో") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬౌ")
      if bstack11l11l1ll1_opy_ == bstack11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ్࠭"):
        bstack11111l111l_opy_(logger)
      if self != None:
        bstack1ll1111111_opy_(self, bstack11l11l1ll1_opy_, bstack11ll_opy_ (u"ࠧ࠭ࠢࠪ౎").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11ll_opy_ (u"ࠨࠩ౏")
    if bstack11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ౐") in bstack11l11l111l_opy_ and getattr(threading.current_thread(), bstack11ll_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ౑"), None):
      bstack1lll11lll_opy_.bstack11111111_opy_(self, bstack1llll11ll1_opy_, logger, wait=True)
    if bstack11ll_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ౒") in bstack11l11l111l_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1ll1111111_opy_(self, bstack11ll_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ౓"))
      bstack1l1ll1llll_opy_.bstack1l11l11ll_opy_(self)
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠢ౔") + str(e))
  bstack1l111lllll_opy_(self)
  self.session_id = None
def bstack1l1ll1l1l1_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1l11llll11_opy_
    global bstack11l11l111l_opy_
    command_executor = kwargs.get(bstack11ll_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴౕࠪ"), bstack11ll_opy_ (u"ࠨౖࠩ"))
    bstack11ll1llll1_opy_ = False
    if type(command_executor) == str and bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ౗") in command_executor:
      bstack11ll1llll1_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ౘ") in str(getattr(command_executor, bstack11ll_opy_ (u"ࠫࡤࡻࡲ࡭ࠩౙ"), bstack11ll_opy_ (u"ࠬ࠭ౚ"))):
      bstack11ll1llll1_opy_ = True
    else:
      kwargs = bstack1111ll11_opy_.bstack1l1l111111_opy_(bstack1l11ll1111_opy_=kwargs, config=CONFIG)
      return bstack11ll111l1_opy_(self, *args, **kwargs)
    if bstack11ll1llll1_opy_:
      bstack11lll1l1ll_opy_ = bstack1111l1l11l_opy_.bstack11llll11l_opy_(CONFIG, bstack11l11l111l_opy_)
      if kwargs.get(bstack11ll_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ౛")):
        kwargs[bstack11ll_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ౜")] = bstack1l11llll11_opy_(kwargs[bstack11ll_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩౝ")], bstack11l11l111l_opy_, CONFIG, bstack11lll1l1ll_opy_)
      elif kwargs.get(bstack11ll_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ౞")):
        kwargs[bstack11ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ౟")] = bstack1l11llll11_opy_(kwargs[bstack11ll_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫౠ")], bstack11l11l111l_opy_, CONFIG, bstack11lll1l1ll_opy_)
  except Exception as e:
    logger.error(bstack11ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡧࡦࡶࡳ࠻ࠢࡾࢁࠧౡ").format(str(e)))
  return bstack11ll111l1_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack111llllll1_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack11lllll11_opy_(self, command_executor=bstack11ll_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵࠱࠳࠹࠱࠴࠳࠶࠮࠲࠼࠷࠸࠹࠺ࠢౢ"), *args, **kwargs):
  global bstack1l1ll1111l_opy_
  global bstack1111lll1l_opy_
  bstack1l1lll1l11_opy_ = bstack1l1ll1l1l1_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1l1l111l_opy_.on():
    return bstack1l1lll1l11_opy_
  try:
    logger.debug(bstack11ll_opy_ (u"ࠧࡄࡱࡰࡱࡦࡴࡤࠡࡇࡻࡩࡨࡻࡴࡰࡴࠣࡻ࡭࡫࡮ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡧࡣ࡯ࡷࡪࠦ࠭ࠡࡽࢀࠫౣ").format(str(command_executor)))
    logger.debug(bstack11ll_opy_ (u"ࠨࡊࡸࡦ࡛ࠥࡒࡍࠢ࡬ࡷࠥ࠳ࠠࡼࡿࠪ౤").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ౥") in command_executor._url:
      bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ౦"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧ౧") in command_executor):
    bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭౨"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack11ll11l1ll_opy_ = getattr(threading.current_thread(), bstack11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧ౩"), None)
  bstack1l1111ll11_opy_ = {}
  if self.capabilities is not None:
    bstack1l1111ll11_opy_[bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭౪")] = self.capabilities.get(bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭౫"))
    bstack1l1111ll11_opy_[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ౬")] = self.capabilities.get(bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ౭"))
    bstack1l1111ll11_opy_[bstack11ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡣࡴࡶࡴࡪࡱࡱࡷࠬ౮")] = self.capabilities.get(bstack11ll_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ౯"))
  if CONFIG.get(bstack11ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭౰"), False) and bstack1111ll11_opy_.bstack1ll1l11ll1_opy_(bstack1l1111ll11_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack11ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ౱") in bstack11l11l111l_opy_ or bstack11ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ౲") in bstack11l11l111l_opy_:
    bstack1l111l1l_opy_.bstack11ll1l11l1_opy_(self)
  if bstack11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ౳") in bstack11l11l111l_opy_ and bstack11ll11l1ll_opy_ and bstack11ll11l1ll_opy_.get(bstack11ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ౴"), bstack11ll_opy_ (u"ࠫࠬ౵")) == bstack11ll_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭౶"):
    bstack1l111l1l_opy_.bstack11ll1l11l1_opy_(self)
  bstack1l1ll1111l_opy_ = self.session_id
  with bstack1l11l1lll1_opy_:
    bstack1111lll1l_opy_.append(self)
  return bstack1l1lll1l11_opy_
def bstack1llllll111_opy_(args):
  return bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠧ౷") in str(args)
def bstack11l1ll1l1l_opy_(self, driver_command, *args, **kwargs):
  global bstack1l1ll111l1_opy_
  global bstack1ll11l11l_opy_
  bstack11l111l1l_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫ౸"), None) and bstack1l1l11l1_opy_(
          threading.current_thread(), bstack11ll_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ౹"), None)
  bstack111ll1lll1_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ౺"), None) and bstack1l1l11l1_opy_(
          threading.current_thread(), bstack11ll_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ౻"), None)
  bstack111lllll1l_opy_ = getattr(self, bstack11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ౼"), None) != None and getattr(self, bstack11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ౽"), None) == True
  if not bstack1ll11l11l_opy_ and bstack11ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭౾") in CONFIG and CONFIG[bstack11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ౿")] == True and bstack1l1l1l1l1_opy_.bstack11111l1ll_opy_(driver_command) and (bstack111lllll1l_opy_ or bstack11l111l1l_opy_ or bstack111ll1lll1_opy_) and not bstack1llllll111_opy_(args):
    try:
      bstack1ll11l11l_opy_ = True
      logger.debug(bstack11ll_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡼࡿࠪಀ").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11ll_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡥࡳࡨࡲࡶࡲࠦࡳࡤࡣࡱࠤࢀࢃࠧಁ").format(str(err)))
    bstack1ll11l11l_opy_ = False
  response = bstack1l1ll111l1_opy_(self, driver_command, *args, **kwargs)
  if (bstack11ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩಂ") in str(bstack11l11l111l_opy_).lower() or bstack11ll_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫಃ") in str(bstack11l11l111l_opy_).lower()) and bstack1l1l111l_opy_.on():
    try:
      if driver_command == bstack11ll_opy_ (u"ࠬࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩ಄"):
        bstack1l111l1l_opy_.bstack1l1l11lll_opy_({
            bstack11ll_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬಅ"): response[bstack11ll_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭ಆ")],
            bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨಇ"): bstack1l111l1l_opy_.current_test_uuid() if bstack1l111l1l_opy_.current_test_uuid() else bstack1l1l111l_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1ll1l1lll1_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack1lll11ll11_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1l1ll1111l_opy_
  global bstack1llll1111l_opy_
  global bstack1111llll1_opy_
  global bstack11l111ll1l_opy_
  global bstack111111lll_opy_
  global bstack11l11l111l_opy_
  global bstack11ll111l1_opy_
  global bstack1111lll1l_opy_
  global bstack11ll1l11ll_opy_
  global bstack1llll11ll1_opy_
  if os.getenv(bstack11ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧಈ")) is not None and bstack1111ll11_opy_.bstack1111l1ll1l_opy_(CONFIG) is None:
    CONFIG[bstack11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪಉ")] = True
  CONFIG[bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ಊ")] = str(bstack11l11l111l_opy_) + str(__version__)
  bstack1ll1111lll_opy_ = os.environ[bstack11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪಋ")]
  bstack11lll1l1ll_opy_ = bstack1111l1l11l_opy_.bstack11llll11l_opy_(CONFIG, bstack11l11l111l_opy_)
  CONFIG[bstack11ll_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩಌ")] = bstack1ll1111lll_opy_
  CONFIG[bstack11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ಍")] = bstack11lll1l1ll_opy_
  if CONFIG.get(bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨಎ"),bstack11ll_opy_ (u"ࠩࠪಏ")) and bstack11ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩಐ") in bstack11l11l111l_opy_:
    CONFIG[bstack11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ಑")].pop(bstack11ll_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪಒ"), None)
    CONFIG[bstack11ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ಓ")].pop(bstack11ll_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬಔ"), None)
  command_executor = bstack1lll11lll1_opy_()
  logger.debug(bstack1lll1lllll_opy_.format(command_executor))
  proxy = bstack11l1lll1l_opy_(CONFIG, proxy)
  bstack1lll111ll1_opy_ = 0 if bstack1llll1111l_opy_ < 0 else bstack1llll1111l_opy_
  try:
    if bstack11l111ll1l_opy_ is True:
      bstack1lll111ll1_opy_ = int(multiprocessing.current_process().name)
    elif bstack111111lll_opy_ is True:
      bstack1lll111ll1_opy_ = int(threading.current_thread().name)
  except:
    bstack1lll111ll1_opy_ = 0
  bstack111l11ll11_opy_ = bstack1l1lllll11_opy_(CONFIG, bstack1lll111ll1_opy_)
  logger.debug(bstack11llll111_opy_.format(str(bstack111l11ll11_opy_)))
  if bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬಕ") in CONFIG and bstack1lll1l1lll_opy_(CONFIG[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ಖ")]):
    bstack1lll1ll1ll_opy_(bstack111l11ll11_opy_)
  if bstack1111ll11_opy_.bstack1ll11l1ll_opy_(CONFIG, bstack1lll111ll1_opy_) and bstack1111ll11_opy_.bstack11ll1l1l1_opy_(bstack111l11ll11_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack1111ll11_opy_.set_capabilities(bstack111l11ll11_opy_, CONFIG)
  if desired_capabilities:
    bstack111111l1l_opy_ = bstack1111lll1l1_opy_(desired_capabilities)
    bstack111111l1l_opy_[bstack11ll_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪಗ")] = bstack1l11l1l1l_opy_(CONFIG)
    bstack111llll11l_opy_ = bstack1l1lllll11_opy_(bstack111111l1l_opy_)
    if bstack111llll11l_opy_:
      bstack111l11ll11_opy_ = update(bstack111llll11l_opy_, bstack111l11ll11_opy_)
    desired_capabilities = None
  if options:
    bstack1l11l1l1l1_opy_(options, bstack111l11ll11_opy_)
  if not options:
    options = bstack1111111l1_opy_(bstack111l11ll11_opy_)
  bstack1llll11ll1_opy_ = CONFIG.get(bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧಘ"))[bstack1lll111ll1_opy_]
  if proxy and bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬಙ")):
    options.proxy(proxy)
  if options and bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬಚ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack11l11l11l1_opy_() < version.parse(bstack11ll_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ಛ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack111l11ll11_opy_)
  logger.info(bstack1ll1lll1ll_opy_)
  bstack11l1l1ll11_opy_.end(EVENTS.bstack11l1l1lll1_opy_.value, EVENTS.bstack11l1l1lll1_opy_.value + bstack11ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣಜ"), EVENTS.bstack11l1l1lll1_opy_.value + bstack11ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢಝ"), status=True, failure=None, test_name=bstack1111llll1_opy_)
  if bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡵࡸ࡯ࡧ࡫࡯ࡩࠬಞ") in kwargs:
    del kwargs[bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡶࡲࡰࡨ࡬ࡰࡪ࠭ಟ")]
  try:
    if bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬಠ")):
      bstack11ll111l1_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬಡ")):
      bstack11ll111l1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧಢ")):
      bstack11ll111l1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack11ll111l1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack11ll1lllll_opy_:
    logger.error(bstack11111l11ll_opy_.format(bstack11ll_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠧಣ"), str(bstack11ll1lllll_opy_)))
    raise bstack11ll1lllll_opy_
  if bstack1111ll11_opy_.bstack1ll11l1ll_opy_(CONFIG, bstack1lll111ll1_opy_) and bstack1111ll11_opy_.bstack11ll1l1l1_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫತ")][bstack11ll_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩಥ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack1111ll11_opy_.set_capabilities(bstack111l11ll11_opy_, CONFIG)
  try:
    bstack1l111111l_opy_ = bstack11ll_opy_ (u"ࠫࠬದ")
    if bstack11l11l11l1_opy_() >= version.parse(bstack11ll_opy_ (u"ࠬ࠺࠮࠱࠰࠳ࡦ࠶࠭ಧ")):
      if self.caps is not None:
        bstack1l111111l_opy_ = self.caps.get(bstack11ll_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨನ"))
    else:
      if self.capabilities is not None:
        bstack1l111111l_opy_ = self.capabilities.get(bstack11ll_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢ಩"))
    if bstack1l111111l_opy_:
      bstack11111l1l1l_opy_(bstack1l111111l_opy_)
      if bstack11l11l11l1_opy_() <= version.parse(bstack11ll_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨಪ")):
        self.command_executor._url = bstack11ll_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥಫ") + bstack1lllll1l11_opy_ + bstack11ll_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢಬ")
      else:
        self.command_executor._url = bstack11ll_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨಭ") + bstack1l111111l_opy_ + bstack11ll_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨಮ")
      logger.debug(bstack1l1l1l1l1l_opy_.format(bstack1l111111l_opy_))
    else:
      logger.debug(bstack1l11ll111l_opy_.format(bstack11ll_opy_ (u"ࠨࡏࡱࡶ࡬ࡱࡦࡲࠠࡉࡷࡥࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢಯ")))
  except Exception as e:
    logger.debug(bstack1l11ll111l_opy_.format(e))
  if bstack11ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ರ") in bstack11l11l111l_opy_:
    bstack1ll1111ll1_opy_(bstack1llll1111l_opy_, bstack11ll1l11ll_opy_)
  bstack1l1ll1111l_opy_ = self.session_id
  if bstack11ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨಱ") in bstack11l11l111l_opy_ or bstack11ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩಲ") in bstack11l11l111l_opy_ or bstack11ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩಳ") in bstack11l11l111l_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack11ll11l1ll_opy_ = getattr(threading.current_thread(), bstack11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥࠬ಴"), None)
  if bstack11ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬವ") in bstack11l11l111l_opy_ or bstack11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಶ") in bstack11l11l111l_opy_:
    bstack1l111l1l_opy_.bstack11ll1l11l1_opy_(self)
  if bstack11ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧಷ") in bstack11l11l111l_opy_ and bstack11ll11l1ll_opy_ and bstack11ll11l1ll_opy_.get(bstack11ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨಸ"), bstack11ll_opy_ (u"ࠩࠪಹ")) == bstack11ll_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ಺"):
    bstack1l111l1l_opy_.bstack11ll1l11l1_opy_(self)
  with bstack1l11l1lll1_opy_:
    bstack1111lll1l_opy_.append(self)
  if bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಻") in CONFIG and bstack11ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧ಼ࠪ") in CONFIG[bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಽ")][bstack1lll111ll1_opy_]:
    bstack1111llll1_opy_ = CONFIG[bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಾ")][bstack1lll111ll1_opy_][bstack11ll_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ಿ")]
  logger.debug(bstack1l1l1l1lll_opy_.format(bstack1l1ll1111l_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1l1l1111ll_opy_
    def bstack11l11111l1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1ll1ll11l_opy_
      if(bstack11ll_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸ࠯࡬ࡶࠦೀ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠪࢂࠬು")), bstack11ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫೂ"), bstack11ll_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧೃ")), bstack11ll_opy_ (u"࠭ࡷࠨೄ")) as fp:
          fp.write(bstack11ll_opy_ (u"ࠢࠣ೅"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11ll_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥೆ")))):
          with open(args[1], bstack11ll_opy_ (u"ࠩࡵࠫೇ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11ll_opy_ (u"ࠪࡥࡸࡿ࡮ࡤࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡤࡴࡥࡸࡒࡤ࡫ࡪ࠮ࡣࡰࡰࡷࡩࡽࡺࠬࠡࡲࡤ࡫ࡪࠦ࠽ࠡࡸࡲ࡭ࡩࠦ࠰ࠪࠩೈ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1lll1lll11_opy_)
            if bstack11ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ೉") in CONFIG and str(CONFIG[bstack11ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩೊ")]).lower() != bstack11ll_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬೋ"):
                bstack11l1l111l_opy_ = bstack1l1l1111ll_opy_()
                bstack1l1lll111_opy_ = bstack11ll_opy_ (u"ࠧࠨࠩࠍ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࠐࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹࡝࠼ࠌࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠ࠿ࠏࡩ࡯࡯ࡵࡷࠤࡵࡥࡩ࡯ࡦࡨࡼࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠳࡟࠾ࠎࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡸࡲࡩࡤࡧࠫ࠴࠱ࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴ࠫ࠾ࠎࡨࡵ࡮ࡴࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫ࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤࠬ࠿ࠏ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡲࡡࡶࡰࡦ࡬ࠥࡃࠠࡢࡵࡼࡲࡨࠦࠨ࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠩࠡ࠿ࡁࠤࢀࢁࠊࠡࠢ࡯ࡩࡹࠦࡣࡢࡲࡶ࠿ࠏࠦࠠࡵࡴࡼࠤࢀࢁࠊࠡࠢࠣࠤࡨࡧࡰࡴࠢࡀࠤࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸ࠯࠻ࠋࠢࠣࢁࢂࠦࡣࡢࡶࡦ࡬ࠥ࠮ࡥࡹࠫࠣࡿࢀࠐࠠࠡࠢࠣࡧࡴࡴࡳࡰ࡮ࡨ࠲ࡪࡸࡲࡰࡴࠫࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠿ࠨࠬࠡࡧࡻ࠭ࡀࠐࠠࠡࡿࢀࠎࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻࡼࠌࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࠬࢁࡣࡥࡲࡘࡶࡱࢃࠧࠡ࠭ࠣࡩࡳࡩ࡯ࡥࡧࡘࡖࡎࡉ࡯࡮ࡲࡲࡲࡪࡴࡴࠩࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡦࡥࡵࡹࠩࠪ࠮ࠍࠤࠥࠦࠠ࠯࠰࠱ࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵࠍࠤࠥࢃࡽࠪ࠽ࠍࢁࢂࡁࠊ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠍࠫࠬ࠭ೌ").format(bstack11l1l111l_opy_=bstack11l1l111l_opy_)
            lines.insert(1, bstack1l1lll111_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11ll_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵ್ࠥ")), bstack11ll_opy_ (u"ࠩࡺࠫ೎")) as bstack1lllll1l1l_opy_:
              bstack1lllll1l1l_opy_.writelines(lines)
        CONFIG[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ೏")] = str(bstack11l11l111l_opy_) + str(__version__)
        bstack1ll1111lll_opy_ = os.environ[bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ೐")]
        bstack11lll1l1ll_opy_ = bstack1111l1l11l_opy_.bstack11llll11l_opy_(CONFIG, bstack11l11l111l_opy_)
        CONFIG[bstack11ll_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ೑")] = bstack1ll1111lll_opy_
        CONFIG[bstack11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨ೒")] = bstack11lll1l1ll_opy_
        bstack1lll111ll1_opy_ = 0 if bstack1llll1111l_opy_ < 0 else bstack1llll1111l_opy_
        try:
          if bstack11l111ll1l_opy_ is True:
            bstack1lll111ll1_opy_ = int(multiprocessing.current_process().name)
          elif bstack111111lll_opy_ is True:
            bstack1lll111ll1_opy_ = int(threading.current_thread().name)
        except:
          bstack1lll111ll1_opy_ = 0
        CONFIG[bstack11ll_opy_ (u"ࠢࡶࡵࡨ࡛࠸ࡉࠢ೓")] = False
        CONFIG[bstack11ll_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ೔")] = True
        bstack111l11ll11_opy_ = bstack1l1lllll11_opy_(CONFIG, bstack1lll111ll1_opy_)
        logger.debug(bstack11llll111_opy_.format(str(bstack111l11ll11_opy_)))
        if CONFIG.get(bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ೕ")):
          bstack1lll1ll1ll_opy_(bstack111l11ll11_opy_)
        if bstack11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ೖ") in CONFIG and bstack11ll_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ೗") in CONFIG[bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ೘")][bstack1lll111ll1_opy_]:
          bstack1111llll1_opy_ = CONFIG[bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ೙")][bstack1lll111ll1_opy_][bstack11ll_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ೚")]
        args.append(os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠨࢀࠪ೛")), bstack11ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ೜"), bstack11ll_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬೝ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack111l11ll11_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11ll_opy_ (u"ࠦ࡮ࡴࡤࡦࡺࡢࡦࡸࡺࡡࡤ࡭࠱࡮ࡸࠨೞ"))
      bstack1ll1ll11l_opy_ = True
      return bstack1l111l1ll1_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack111l111l1_opy_(self,
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
    global bstack1llll1111l_opy_
    global bstack1111llll1_opy_
    global bstack11l111ll1l_opy_
    global bstack111111lll_opy_
    global bstack11l11l111l_opy_
    CONFIG[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ೟")] = str(bstack11l11l111l_opy_) + str(__version__)
    bstack1ll1111lll_opy_ = os.environ[bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫೠ")]
    bstack11lll1l1ll_opy_ = bstack1111l1l11l_opy_.bstack11llll11l_opy_(CONFIG, bstack11l11l111l_opy_)
    CONFIG[bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪೡ")] = bstack1ll1111lll_opy_
    CONFIG[bstack11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪೢ")] = bstack11lll1l1ll_opy_
    bstack1lll111ll1_opy_ = 0 if bstack1llll1111l_opy_ < 0 else bstack1llll1111l_opy_
    try:
      if bstack11l111ll1l_opy_ is True:
        bstack1lll111ll1_opy_ = int(multiprocessing.current_process().name)
      elif bstack111111lll_opy_ is True:
        bstack1lll111ll1_opy_ = int(threading.current_thread().name)
    except:
      bstack1lll111ll1_opy_ = 0
    CONFIG[bstack11ll_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣೣ")] = True
    bstack111l11ll11_opy_ = bstack1l1lllll11_opy_(CONFIG, bstack1lll111ll1_opy_)
    logger.debug(bstack11llll111_opy_.format(str(bstack111l11ll11_opy_)))
    if CONFIG.get(bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ೤")):
      bstack1lll1ll1ll_opy_(bstack111l11ll11_opy_)
    if bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ೥") in CONFIG and bstack11ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ೦") in CONFIG[bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ೧")][bstack1lll111ll1_opy_]:
      bstack1111llll1_opy_ = CONFIG[bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ೨")][bstack1lll111ll1_opy_][bstack11ll_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭೩")]
    import urllib
    import json
    if bstack11ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭೪") in CONFIG and str(CONFIG[bstack11ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ೫")]).lower() != bstack11ll_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ೬"):
        bstack1l1l11111_opy_ = bstack1l1l1111ll_opy_()
        bstack11l1l111l_opy_ = bstack1l1l11111_opy_ + urllib.parse.quote(json.dumps(bstack111l11ll11_opy_))
    else:
        bstack11l1l111l_opy_ = bstack11ll_opy_ (u"ࠬࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠧ೭") + urllib.parse.quote(json.dumps(bstack111l11ll11_opy_))
    browser = self.connect(bstack11l1l111l_opy_)
    return browser
except Exception as e:
    pass
def bstack11lll111l1_opy_():
    global bstack1ll1ll11l_opy_
    global bstack11l11l111l_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1111ll1ll1_opy_
        global bstack1111l111_opy_
        if not bstack1ll1l1111_opy_:
          global bstack11lll1l11_opy_
          if not bstack11lll1l11_opy_:
            from bstack_utils.helper import bstack1ll111l11_opy_, bstack1l1l11ll1_opy_, bstack1l111l11l1_opy_
            bstack11lll1l11_opy_ = bstack1ll111l11_opy_()
            bstack1l1l11ll1_opy_(bstack11l11l111l_opy_)
            bstack11lll1l1ll_opy_ = bstack1111l1l11l_opy_.bstack11llll11l_opy_(CONFIG, bstack11l11l111l_opy_)
            bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠨࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡔࡗࡕࡄࡖࡅࡗࡣࡒࡇࡐࠣ೮"), bstack11lll1l1ll_opy_)
          BrowserType.connect = bstack1111ll1ll1_opy_
          return
        BrowserType.launch = bstack111l111l1_opy_
        bstack1ll1ll11l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack11l11111l1_opy_
      bstack1ll1ll11l_opy_ = True
    except Exception as e:
      pass
def bstack1ll11lll11_opy_(context, bstack1l111ll111_opy_):
  try:
    context.page.evaluate(bstack11ll_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ೯"), bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠬ೰")+ json.dumps(bstack1l111ll111_opy_) + bstack11ll_opy_ (u"ࠤࢀࢁࠧೱ"))
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥࢁࡽ࠻ࠢࡾࢁࠧೲ").format(str(e), traceback.format_exc()))
def bstack11l11l1l1l_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11ll_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧೳ"), bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ೴") + json.dumps(message) + bstack11ll_opy_ (u"࠭ࠬࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠩ೵") + json.dumps(level) + bstack11ll_opy_ (u"ࠧࡾࡿࠪ೶"))
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡦࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠡࡽࢀ࠾ࠥࢁࡽࠣ೷").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1111l11l1l_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack11llll1111_opy_(self, url):
  global bstack11ll1l1111_opy_
  try:
    bstack1111l1lll_opy_(url)
  except Exception as err:
    logger.debug(bstack1ll11ll111_opy_.format(str(err)))
  try:
    bstack11ll1l1111_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1l1l1ll1l_opy_):
        bstack1111l1lll_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1ll11ll111_opy_.format(str(err)))
    raise e
def bstack11l111l1ll_opy_(self):
  global bstack111lll1l1_opy_
  bstack111lll1l1_opy_ = self
  return
def bstack1ll1l1ll1_opy_(self):
  global bstack111l1llll_opy_
  bstack111l1llll_opy_ = self
  return
def bstack1ll111llll_opy_(test_name, bstack1lll1ll111_opy_):
  global CONFIG
  if percy.bstack1l1llll1l1_opy_() == bstack11ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ೸"):
    bstack1llll1ll11_opy_ = os.path.relpath(bstack1lll1ll111_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1llll1ll11_opy_)
    bstack111l111l1l_opy_ = suite_name + bstack11ll_opy_ (u"ࠥ࠱ࠧ೹") + test_name
    threading.current_thread().percySessionName = bstack111l111l1l_opy_
def bstack11lll1111_opy_(self, test, *args, **kwargs):
  global bstack1l1l11ll1l_opy_
  test_name = None
  bstack1lll1ll111_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1lll1ll111_opy_ = str(test.source)
  bstack1ll111llll_opy_(test_name, bstack1lll1ll111_opy_)
  bstack1l1l11ll1l_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l1l1l11ll_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack1ll111l11l_opy_(driver, bstack111l111l1l_opy_):
  if not bstack111l1lll1l_opy_ and bstack111l111l1l_opy_:
      bstack1ll1111ll_opy_ = {
          bstack11ll_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫ೺"): bstack11ll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭೻"),
          bstack11ll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ೼"): {
              bstack11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ೽"): bstack111l111l1l_opy_
          }
      }
      bstack11ll11l111_opy_ = bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭೾").format(json.dumps(bstack1ll1111ll_opy_))
      driver.execute_script(bstack11ll11l111_opy_)
  if bstack111111111_opy_:
      bstack11l11lll1l_opy_ = {
          bstack11ll_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ೿"): bstack11ll_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬഀ"),
          bstack11ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧഁ"): {
              bstack11ll_opy_ (u"ࠬࡪࡡࡵࡣࠪം"): bstack111l111l1l_opy_ + bstack11ll_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨഃ"),
              bstack11ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ഄ"): bstack11ll_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭അ")
          }
      }
      if bstack111111111_opy_.status == bstack11ll_opy_ (u"ࠩࡓࡅࡘ࡙ࠧആ"):
          bstack1llll11l1l_opy_ = bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨഇ").format(json.dumps(bstack11l11lll1l_opy_))
          driver.execute_script(bstack1llll11l1l_opy_)
          bstack1ll1111111_opy_(driver, bstack11ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫഈ"))
      elif bstack111111111_opy_.status == bstack11ll_opy_ (u"ࠬࡌࡁࡊࡎࠪഉ"):
          reason = bstack11ll_opy_ (u"ࠨࠢഊ")
          bstack1ll11ll11_opy_ = bstack111l111l1l_opy_ + bstack11ll_opy_ (u"ࠧࠡࡨࡤ࡭ࡱ࡫ࡤࠨഋ")
          if bstack111111111_opy_.message:
              reason = str(bstack111111111_opy_.message)
              bstack1ll11ll11_opy_ = bstack1ll11ll11_opy_ + bstack11ll_opy_ (u"ࠨࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࠨഌ") + reason
          bstack11l11lll1l_opy_[bstack11ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ഍")] = {
              bstack11ll_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩഎ"): bstack11ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪഏ"),
              bstack11ll_opy_ (u"ࠬࡪࡡࡵࡣࠪഐ"): bstack1ll11ll11_opy_
          }
          bstack1llll11l1l_opy_ = bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ഑").format(json.dumps(bstack11l11lll1l_opy_))
          driver.execute_script(bstack1llll11l1l_opy_)
          bstack1ll1111111_opy_(driver, bstack11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧഒ"), reason)
          bstack11111llll_opy_(reason, str(bstack111111111_opy_), str(bstack1llll1111l_opy_), logger)
@measure(event_name=EVENTS.bstack111111ll1l_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack1l11l111ll_opy_(driver, test):
  if percy.bstack1l1llll1l1_opy_() == bstack11ll_opy_ (u"ࠣࡶࡵࡹࡪࠨഓ") and percy.bstack11111lllll_opy_() == bstack11ll_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦഔ"):
      bstack111ll11l1_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ക"), None)
      bstack1ll1ll1ll_opy_(driver, bstack111ll11l1_opy_, test)
  if (bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨഖ"), None) and
      bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫഗ"), None)) or (
      bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ഘ"), None) and
      bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩങ"), None)):
      logger.info(bstack11ll_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠦࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡ࡫ࡶࠤࡺࡴࡤࡦࡴࡺࡥࡾ࠴ࠠࠣച"))
      bstack1111ll11_opy_.bstack111ll1l1_opy_(driver, name=test.name, path=test.source)
def bstack11ll111111_opy_(test, bstack111l111l1l_opy_):
    try:
      bstack1l11111lll_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack11ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧഛ")] = bstack111l111l1l_opy_
      if bstack111111111_opy_:
        if bstack111111111_opy_.status == bstack11ll_opy_ (u"ࠪࡔࡆ࡙ࡓࠨജ"):
          data[bstack11ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫഝ")] = bstack11ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬഞ")
        elif bstack111111111_opy_.status == bstack11ll_opy_ (u"࠭ࡆࡂࡋࡏࠫട"):
          data[bstack11ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧഠ")] = bstack11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨഡ")
          if bstack111111111_opy_.message:
            data[bstack11ll_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩഢ")] = str(bstack111111111_opy_.message)
      user = CONFIG[bstack11ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬണ")]
      key = CONFIG[bstack11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧത")]
      host = bstack111ll111l1_opy_(cli.config, [bstack11ll_opy_ (u"ࠧࡧࡰࡪࡵࠥഥ"), bstack11ll_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥࠣദ"), bstack11ll_opy_ (u"ࠢࡢࡲ࡬ࠦധ")], bstack11ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠤന"))
      url = bstack11ll_opy_ (u"ࠩࡾࢁ࠴ࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡴࡧࡶࡷ࡮ࡵ࡮ࡴ࠱ࡾࢁ࠳ࡰࡳࡰࡰࠪഩ").format(host, bstack1l1ll1111l_opy_)
      headers = {
        bstack11ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩപ"): bstack11ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧഫ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽ࡹࡵࡪࡡࡵࡧࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠤബ"), datetime.datetime.now() - bstack1l11111lll_opy_)
    except Exception as e:
      logger.error(bstack1l1ll1111_opy_.format(str(e)))
def bstack1l1111lll1_opy_(test, bstack111l111l1l_opy_):
  global CONFIG
  global bstack111l1llll_opy_
  global bstack111lll1l1_opy_
  global bstack1l1ll1111l_opy_
  global bstack111111111_opy_
  global bstack1111llll1_opy_
  global bstack11lllllll_opy_
  global bstack11l1111l1_opy_
  global bstack1l1l11111l_opy_
  global bstack1l1llll11_opy_
  global bstack1111lll1l_opy_
  global bstack1llll11ll1_opy_
  global bstack11111ll1l1_opy_
  try:
    if not bstack1l1ll1111l_opy_:
      with bstack11111ll1l1_opy_:
        bstack1ll1l11l11_opy_ = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"࠭ࡾࠨഭ")), bstack11ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧമ"), bstack11ll_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪയ"))
        if os.path.exists(bstack1ll1l11l11_opy_):
          with open(bstack1ll1l11l11_opy_, bstack11ll_opy_ (u"ࠩࡵࠫര")) as f:
            content = f.read().strip()
            if content:
              bstack11llll111l_opy_ = json.loads(bstack11ll_opy_ (u"ࠥࡿࠧറ") + content + bstack11ll_opy_ (u"ࠫࠧࡾࠢ࠻ࠢࠥࡽࠧ࠭ല") + bstack11ll_opy_ (u"ࠧࢃࠢള"))
              bstack1l1ll1111l_opy_ = bstack11llll111l_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࡶࠤ࡫࡯࡬ࡦ࠼ࠣࠫഴ") + str(e))
  if bstack1111lll1l_opy_:
    with bstack1l11l1lll1_opy_:
      bstack11111l1l11_opy_ = bstack1111lll1l_opy_.copy()
    for driver in bstack11111l1l11_opy_:
      if bstack1l1ll1111l_opy_ == driver.session_id:
        if test:
          bstack1l11l111ll_opy_(driver, test)
        bstack1ll111l11l_opy_(driver, bstack111l111l1l_opy_)
  elif bstack1l1ll1111l_opy_:
    bstack11ll111111_opy_(test, bstack111l111l1l_opy_)
  if bstack111l1llll_opy_:
    bstack11l1111l1_opy_(bstack111l1llll_opy_)
  if bstack111lll1l1_opy_:
    bstack1l1l11111l_opy_(bstack111lll1l1_opy_)
  if bstack11l11ll1l1_opy_:
    bstack1l1llll11_opy_()
def bstack111l11llll_opy_(self, test, *args, **kwargs):
  bstack111l111l1l_opy_ = None
  if test:
    bstack111l111l1l_opy_ = str(test.name)
  bstack1l1111lll1_opy_(test, bstack111l111l1l_opy_)
  bstack11lllllll_opy_(self, test, *args, **kwargs)
def bstack111llll1l_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11l11l1l1_opy_
  global CONFIG
  global bstack1111lll1l_opy_
  global bstack1l1ll1111l_opy_
  global bstack11111ll1l1_opy_
  bstack1l1ll1l11l_opy_ = None
  try:
    if bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭വ"), None) or bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪശ"), None):
      try:
        if not bstack1l1ll1111l_opy_:
          bstack1ll1l11l11_opy_ = os.path.join(os.path.expanduser(bstack11ll_opy_ (u"ࠩࢁࠫഷ")), bstack11ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪസ"), bstack11ll_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭ഹ"))
          with bstack11111ll1l1_opy_:
            if os.path.exists(bstack1ll1l11l11_opy_):
              with open(bstack1ll1l11l11_opy_, bstack11ll_opy_ (u"ࠬࡸࠧഺ")) as f:
                content = f.read().strip()
                if content:
                  bstack11llll111l_opy_ = json.loads(bstack11ll_opy_ (u"ࠨࡻ഻ࠣ") + content + bstack11ll_opy_ (u"ࠧࠣࡺࠥ࠾ࠥࠨࡹ഼ࠣࠩ") + bstack11ll_opy_ (u"ࠣࡿࠥഽ"))
                  bstack1l1ll1111l_opy_ = bstack11llll111l_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡍࡉࡹࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡶࡨࡷࡹࠦࡳࡵࡣࡷࡹࡸࡀࠠࠨാ") + str(e))
      if bstack1111lll1l_opy_:
        with bstack1l11l1lll1_opy_:
          bstack11111l1l11_opy_ = bstack1111lll1l_opy_.copy()
        for driver in bstack11111l1l11_opy_:
          if bstack1l1ll1111l_opy_ == driver.session_id:
            bstack1l1ll1l11l_opy_ = driver
    bstack1ll1l11lll_opy_ = bstack1111ll11_opy_.bstack11l11lll1_opy_(test.tags)
    if bstack1l1ll1l11l_opy_:
      threading.current_thread().isA11yTest = bstack1111ll11_opy_.bstack1ll11lll1_opy_(bstack1l1ll1l11l_opy_, bstack1ll1l11lll_opy_)
      threading.current_thread().isAppA11yTest = bstack1111ll11_opy_.bstack1ll11lll1_opy_(bstack1l1ll1l11l_opy_, bstack1ll1l11lll_opy_)
    else:
      threading.current_thread().isA11yTest = bstack1ll1l11lll_opy_
      threading.current_thread().isAppA11yTest = bstack1ll1l11lll_opy_
  except:
    pass
  bstack11l11l1l1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack111111111_opy_
  try:
    bstack111111111_opy_ = self._test
  except:
    bstack111111111_opy_ = self.test
def bstack1l1l1l1111_opy_():
  global bstack111lll111l_opy_
  try:
    if os.path.exists(bstack111lll111l_opy_):
      os.remove(bstack111lll111l_opy_)
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ി") + str(e))
def bstack11l11ll1ll_opy_():
  global bstack111lll111l_opy_
  bstack1l111llll1_opy_ = {}
  lock_file = bstack111lll111l_opy_ + bstack11ll_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪീ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨു"))
    try:
      if not os.path.isfile(bstack111lll111l_opy_):
        with open(bstack111lll111l_opy_, bstack11ll_opy_ (u"࠭ࡷࠨൂ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack111lll111l_opy_):
        with open(bstack111lll111l_opy_, bstack11ll_opy_ (u"ࠧࡳࠩൃ")) as f:
          content = f.read().strip()
          if content:
            bstack1l111llll1_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack11ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪࡧࡤࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪൄ") + str(e))
    return bstack1l111llll1_opy_
  try:
    os.makedirs(os.path.dirname(bstack111lll111l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack111lll111l_opy_):
        with open(bstack111lll111l_opy_, bstack11ll_opy_ (u"ࠩࡺࠫ൅")) as f:
          json.dump({}, f)
      if os.path.exists(bstack111lll111l_opy_):
        with open(bstack111lll111l_opy_, bstack11ll_opy_ (u"ࠪࡶࠬെ")) as f:
          content = f.read().strip()
          if content:
            bstack1l111llll1_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭േ") + str(e))
  finally:
    return bstack1l111llll1_opy_
def bstack1ll1111ll1_opy_(platform_index, item_index):
  global bstack111lll111l_opy_
  lock_file = bstack111lll111l_opy_ + bstack11ll_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫൈ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩ൉"))
    try:
      bstack1l111llll1_opy_ = {}
      if os.path.exists(bstack111lll111l_opy_):
        with open(bstack111lll111l_opy_, bstack11ll_opy_ (u"ࠧࡳࠩൊ")) as f:
          content = f.read().strip()
          if content:
            bstack1l111llll1_opy_ = json.loads(content)
      bstack1l111llll1_opy_[item_index] = platform_index
      with open(bstack111lll111l_opy_, bstack11ll_opy_ (u"ࠣࡹࠥോ")) as outfile:
        json.dump(bstack1l111llll1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡼࡸࡩࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧൌ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack111lll111l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack1l111llll1_opy_ = {}
      if os.path.exists(bstack111lll111l_opy_):
        with open(bstack111lll111l_opy_, bstack11ll_opy_ (u"ࠪࡶ്ࠬ")) as f:
          content = f.read().strip()
          if content:
            bstack1l111llll1_opy_ = json.loads(content)
      bstack1l111llll1_opy_[item_index] = platform_index
      with open(bstack111lll111l_opy_, bstack11ll_opy_ (u"ࠦࡼࠨൎ")) as outfile:
        json.dump(bstack1l111llll1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡸࡴ࡬ࡸ࡮ࡴࡧࠡࡶࡲࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪ൏") + str(e))
def bstack111ll111ll_opy_(bstack1l1l1llll1_opy_):
  global CONFIG
  bstack1l1ll11l11_opy_ = bstack11ll_opy_ (u"࠭ࠧ൐")
  if not bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ൑") in CONFIG:
    logger.info(bstack11ll_opy_ (u"ࠨࡐࡲࠤࡵࡲࡡࡵࡨࡲࡶࡲࡹࠠࡱࡣࡶࡷࡪࡪࠠࡶࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥࡸࡥࡱࡱࡵࡸࠥ࡬࡯ࡳࠢࡕࡳࡧࡵࡴࠡࡴࡸࡲࠬ൒"))
  try:
    platform = CONFIG[bstack11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ൓")][bstack1l1l1llll1_opy_]
    if bstack11ll_opy_ (u"ࠪࡳࡸ࠭ൔ") in platform:
      bstack1l1ll11l11_opy_ += str(platform[bstack11ll_opy_ (u"ࠫࡴࡹࠧൕ")]) + bstack11ll_opy_ (u"ࠬ࠲ࠠࠨൖ")
    if bstack11ll_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩൗ") in platform:
      bstack1l1ll11l11_opy_ += str(platform[bstack11ll_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪ൘")]) + bstack11ll_opy_ (u"ࠨ࠮ࠣࠫ൙")
    if bstack11ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭൚") in platform:
      bstack1l1ll11l11_opy_ += str(platform[bstack11ll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧ൛")]) + bstack11ll_opy_ (u"ࠫ࠱ࠦࠧ൜")
    if bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ൝") in platform:
      bstack1l1ll11l11_opy_ += str(platform[bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ൞")]) + bstack11ll_opy_ (u"ࠧ࠭ࠢࠪൟ")
    if bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ൠ") in platform:
      bstack1l1ll11l11_opy_ += str(platform[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧൡ")]) + bstack11ll_opy_ (u"ࠪ࠰ࠥ࠭ൢ")
    if bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬൣ") in platform:
      bstack1l1ll11l11_opy_ += str(platform[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭൤")]) + bstack11ll_opy_ (u"࠭ࠬࠡࠩ൥")
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠧࡔࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡱࡩࡷࡧࡴࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡳࡵࡴ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡶࡪࡶ࡯ࡳࡶࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡴࡴࠧ൦") + str(e))
  finally:
    if bstack1l1ll11l11_opy_[len(bstack1l1ll11l11_opy_) - 2:] == bstack11ll_opy_ (u"ࠨ࠮ࠣࠫ൧"):
      bstack1l1ll11l11_opy_ = bstack1l1ll11l11_opy_[:-2]
    return bstack1l1ll11l11_opy_
def bstack11l1111ll_opy_(path, bstack1l1ll11l11_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1111l11lll_opy_ = ET.parse(path)
    bstack11llll1ll1_opy_ = bstack1111l11lll_opy_.getroot()
    bstack11111ll1ll_opy_ = None
    for suite in bstack11llll1ll1_opy_.iter(bstack11ll_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨ൨")):
      if bstack11ll_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ൩") in suite.attrib:
        suite.attrib[bstack11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ൪")] += bstack11ll_opy_ (u"ࠬࠦࠧ൫") + bstack1l1ll11l11_opy_
        bstack11111ll1ll_opy_ = suite
    bstack11lllll11l_opy_ = None
    for robot in bstack11llll1ll1_opy_.iter(bstack11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ൬")):
      bstack11lllll11l_opy_ = robot
    bstack1l11llll1l_opy_ = len(bstack11lllll11l_opy_.findall(bstack11ll_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭൭")))
    if bstack1l11llll1l_opy_ == 1:
      bstack11lllll11l_opy_.remove(bstack11lllll11l_opy_.findall(bstack11ll_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧ൮"))[0])
      bstack11l111l11l_opy_ = ET.Element(bstack11ll_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨ൯"), attrib={bstack11ll_opy_ (u"ࠪࡲࡦࡳࡥࠨ൰"): bstack11ll_opy_ (u"ࠫࡘࡻࡩࡵࡧࡶࠫ൱"), bstack11ll_opy_ (u"ࠬ࡯ࡤࠨ൲"): bstack11ll_opy_ (u"࠭ࡳ࠱ࠩ൳")})
      bstack11lllll11l_opy_.insert(1, bstack11l111l11l_opy_)
      bstack1111l1llll_opy_ = None
      for suite in bstack11lllll11l_opy_.iter(bstack11ll_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭൴")):
        bstack1111l1llll_opy_ = suite
      bstack1111l1llll_opy_.append(bstack11111ll1ll_opy_)
      bstack11ll11ll1_opy_ = None
      for status in bstack11111ll1ll_opy_.iter(bstack11ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ൵")):
        bstack11ll11ll1_opy_ = status
      bstack1111l1llll_opy_.append(bstack11ll11ll1_opy_)
    bstack1111l11lll_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠧ൶") + str(e))
def bstack11lll1lll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1ll1111l1l_opy_
  global CONFIG
  if bstack11ll_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢ൷") in options:
    del options[bstack11ll_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣ൸")]
  json_data = bstack11l11ll1ll_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack11ll_opy_ (u"ࠬࡶࡡࡣࡱࡷࡣࡷ࡫ࡳࡶ࡮ࡷࡷࠬ൹"), str(item_id), bstack11ll_opy_ (u"࠭࡯ࡶࡶࡳࡹࡹ࠴ࡸ࡮࡮ࠪൺ"))
    bstack11l1111ll_opy_(path, bstack111ll111ll_opy_(json_data[item_id]))
  bstack1l1l1l1111_opy_()
  return bstack1ll1111l1l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack111lll111_opy_(self, ff_profile_dir):
  global bstack111l111lll_opy_
  if not ff_profile_dir:
    return None
  return bstack111l111lll_opy_(self, ff_profile_dir)
def bstack1111l1l11_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack111l1l11l_opy_
  bstack11l1lll1l1_opy_ = []
  if bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪൻ") in CONFIG:
    bstack11l1lll1l1_opy_ = CONFIG[bstack11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫർ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11ll_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࠥൽ")],
      pabot_args[bstack11ll_opy_ (u"ࠥࡺࡪࡸࡢࡰࡵࡨࠦൾ")],
      argfile,
      pabot_args.get(bstack11ll_opy_ (u"ࠦ࡭࡯ࡶࡦࠤൿ")),
      pabot_args[bstack11ll_opy_ (u"ࠧࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠣ඀")],
      platform[0],
      bstack111l1l11l_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11ll_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡧ࡫࡯ࡩࡸࠨඁ")] or [(bstack11ll_opy_ (u"ࠢࠣං"), None)]
    for platform in enumerate(bstack11l1lll1l1_opy_)
  ]
def bstack1l111l111l_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1lllll11ll_opy_=bstack11ll_opy_ (u"ࠨࠩඃ")):
  global bstack111lll11l1_opy_
  self.platform_index = platform_index
  self.bstack1ll11ll1l1_opy_ = bstack1lllll11ll_opy_
  bstack111lll11l1_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack11l1l11l11_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1ll111111_opy_
  global bstack11lll1lll_opy_
  bstack11lll1l1l_opy_ = copy.deepcopy(item)
  if not bstack11ll_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ඄") in item.options:
    bstack11lll1l1l_opy_.options[bstack11ll_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬඅ")] = []
  bstack11l1llll11_opy_ = bstack11lll1l1l_opy_.options[bstack11ll_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ආ")].copy()
  for v in bstack11lll1l1l_opy_.options[bstack11ll_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧඇ")]:
    if bstack11ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜ࠬඈ") in v:
      bstack11l1llll11_opy_.remove(v)
    if bstack11ll_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙ࠧඉ") in v:
      bstack11l1llll11_opy_.remove(v)
    if bstack11ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬඊ") in v:
      bstack11l1llll11_opy_.remove(v)
  bstack11l1llll11_opy_.insert(0, bstack11ll_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘ࠻ࡽࢀࠫඋ").format(bstack11lll1l1l_opy_.platform_index))
  bstack11l1llll11_opy_.insert(0, bstack11ll_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘ࠺ࡼࡿࠪඌ").format(bstack11lll1l1l_opy_.bstack1ll11ll1l1_opy_))
  bstack11lll1l1l_opy_.options[bstack11ll_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ඍ")] = bstack11l1llll11_opy_
  if bstack11lll1lll_opy_:
    bstack11lll1l1l_opy_.options[bstack11ll_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧඎ")].insert(0, bstack11ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘࡀࡻࡾࠩඏ").format(bstack11lll1lll_opy_))
  return bstack1ll111111_opy_(caller_id, datasources, is_last, bstack11lll1l1l_opy_, outs_dir)
def bstack1lllll11l1_opy_(command, item_index):
  try:
    if bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨඐ")):
      os.environ[bstack11ll_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩඑ")] = json.dumps(CONFIG[bstack11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬඒ")][item_index % bstack1111l11111_opy_])
    global bstack11lll1lll_opy_
    if bstack11lll1lll_opy_:
      command[0] = command[0].replace(bstack11ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩඓ"), bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨඔ") + str(
        item_index) + bstack11ll_opy_ (u"ࠬࠦࠧඕ") + bstack11lll1lll_opy_, 1)
    else:
      command[0] = command[0].replace(bstack11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬඖ"),
                                      bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡳࡥ࡭ࠣࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠣࠫ඗") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack11ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠ࡮ࡱࡧ࡭࡫ࡿࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡢࡰࡧࠤ࡫ࡵࡲࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱ࠾ࠥࢁࡽࠨ඘").format(str(e)))
def bstack11lll1l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack11llllll1_opy_
  try:
    bstack1lllll11l1_opy_(command, item_index)
    return bstack11llllll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack11ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴ࠺ࠡࡽࢀࠫ඙").format(str(e)))
    raise e
def bstack1l1l1lll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack11llllll1_opy_
  try:
    bstack1lllll11l1_opy_(command, item_index)
    return bstack11llllll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack11ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠴࠱࠵࠸ࡀࠠࡼࡿࠪක").format(str(e)))
    try:
      return bstack11llllll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack11ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࠸࠮࠲࠵ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩඛ").format(str(e2)))
      raise e
def bstack1111ll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack11llllll1_opy_
  try:
    bstack1lllll11l1_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack11llllll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack11ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰࠣ࠶࠳࠷࠵࠻ࠢࡾࢁࠬග").format(str(e)))
    try:
      return bstack11llllll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack11ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠ࠳࠰࠴࠹ࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫඝ").format(str(e2)))
      raise e
def _1111ll1111_opy_(bstack11l11l111_opy_, item_index, process_timeout, sleep_before_start, bstack1l1ll11lll_opy_):
  bstack1lllll11l1_opy_(bstack11l11l111_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack1l1ll1ll1l_opy_(command, bstack1l1lll1l1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11llllll1_opy_
  try:
    bstack1lllll11l1_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack11llllll1_opy_(command, bstack1l1lll1l1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲࠥ࠻࠮࠱࠼ࠣࡿࢂ࠭ඞ").format(str(e)))
    try:
      return bstack11llllll1_opy_(command, bstack1l1lll1l1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨඟ").format(str(e2)))
      raise e
def bstack11l1l111l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11llllll1_opy_
  try:
    process_timeout = _1111ll1111_opy_(command, item_index, process_timeout, sleep_before_start, bstack11ll_opy_ (u"ࠩ࠷࠲࠷࠭ච"))
    return bstack11llllll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠶࠱࠶࠿ࠦࡻࡾࠩඡ").format(str(e)))
    try:
      return bstack11llllll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫජ").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack1l11l11ll1_opy_(self, runner, quiet=False, capture=True):
  global bstack1lll1l11ll_opy_
  bstack1lllll1111_opy_ = bstack1lll1l11ll_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11ll_opy_ (u"ࠬ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࡠࡣࡵࡶࠬඣ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11ll_opy_ (u"࠭ࡥࡹࡥࡢࡸࡷࡧࡣࡦࡤࡤࡧࡰࡥࡡࡳࡴࠪඤ")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1lllll1111_opy_
def bstack11l1l11111_opy_(runner, hook_name, context, element, bstack111llll11_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1l1llllll1_opy_.bstack11l111ll_opy_(hook_name, element)
    bstack111llll11_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1l1llllll1_opy_.bstack11l1l111_opy_(element)
      if hook_name not in [bstack11ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫඥ"), bstack11ll_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫඦ")] and args and hasattr(args[0], bstack11ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࡠ࡯ࡨࡷࡸࡧࡧࡦࠩට")):
        args[0].error_message = bstack11ll_opy_ (u"ࠪࠫඨ")
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡩࡣࡱࡨࡱ࡫ࠠࡩࡱࡲ࡯ࡸࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦ࠼ࠣࡿࢂ࠭ඩ").format(str(e)))
@measure(event_name=EVENTS.bstack1l1lll11ll_opy_, stage=STAGE.bstack1ll1111l1_opy_, hook_type=bstack11ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡆࡲ࡬ࠣඪ"), bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack1ll1ll11l1_opy_(runner, name, context, bstack111llll11_opy_, *args):
    if runner.hooks.get(bstack11ll_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥණ")).__name__ != bstack11ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࡣࡩ࡫ࡦࡢࡷ࡯ࡸࡤ࡮࡯ࡰ࡭ࠥඬ"):
      bstack11l1l11111_opy_(runner, name, context, runner, bstack111llll11_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1lll1111l1_opy_(bstack11ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧත")) else context.browser
      runner.driver_initialised = bstack11ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨථ")
    except Exception as e:
      logger.debug(bstack11ll_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡸ࡫ࠠࡢࡶࡷࡶ࡮ࡨࡵࡵࡧ࠽ࠤࢀࢃࠧද").format(str(e)))
def bstack1ll111l1l_opy_(runner, name, context, bstack111llll11_opy_, *args):
    bstack11l1l11111_opy_(runner, name, context, context.feature, bstack111llll11_opy_, *args)
    try:
      if not bstack111l1lll1l_opy_:
        bstack1l1ll1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll1111l1_opy_(bstack11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪධ")) else context.browser
        if is_driver_active(bstack1l1ll1l11l_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack11ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨන")
          bstack1l111ll111_opy_ = str(runner.feature.name)
          bstack1ll11lll11_opy_(context, bstack1l111ll111_opy_)
          bstack1l1ll1l11l_opy_.execute_script(bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫ඲") + json.dumps(bstack1l111ll111_opy_) + bstack11ll_opy_ (u"ࠧࡾࡿࠪඳ"))
    except Exception as e:
      logger.debug(bstack11ll_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨප").format(str(e)))
def bstack1l1111l11l_opy_(runner, name, context, bstack111llll11_opy_, *args):
    if hasattr(context, bstack11ll_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫඵ")):
        bstack1l1llllll1_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack11ll_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬබ")) else context.feature
    bstack11l1l11111_opy_(runner, name, context, target, bstack111llll11_opy_, *args)
@measure(event_name=EVENTS.bstack11ll1l1l11_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack1l11l1llll_opy_(runner, name, context, bstack111llll11_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1l1llllll1_opy_.start_test(context)
    bstack11l1l11111_opy_(runner, name, context, context.scenario, bstack111llll11_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1l1ll1llll_opy_.bstack1l111l1ll_opy_(context, *args)
    try:
      bstack1l1ll1l11l_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪභ"), context.browser)
      if is_driver_active(bstack1l1ll1l11l_opy_):
        bstack1l111l1l_opy_.bstack11ll1l11l1_opy_(bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫම"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack11ll_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣඹ")
        if (not bstack111l1lll1l_opy_):
          scenario_name = args[0].name
          feature_name = bstack1l111ll111_opy_ = str(runner.feature.name)
          bstack1l111ll111_opy_ = feature_name + bstack11ll_opy_ (u"ࠧࠡ࠯ࠣࠫය") + scenario_name
          if runner.driver_initialised == bstack11ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥර"):
            bstack1ll11lll11_opy_(context, bstack1l111ll111_opy_)
            bstack1l1ll1l11l_opy_.execute_script(bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ඼") + json.dumps(bstack1l111ll111_opy_) + bstack11ll_opy_ (u"ࠪࢁࢂ࠭ල"))
    except Exception as e:
      logger.debug(bstack11ll_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬ඾").format(str(e)))
@measure(event_name=EVENTS.bstack1l1lll11ll_opy_, stage=STAGE.bstack1ll1111l1_opy_, hook_type=bstack11ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡘࡺࡥࡱࠤ඿"), bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack1111ll11l_opy_(runner, name, context, bstack111llll11_opy_, *args):
    bstack11l1l11111_opy_(runner, name, context, args[0], bstack111llll11_opy_, *args)
    try:
      bstack1l1ll1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll1111l1_opy_(bstack11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬව")) else context.browser
      if is_driver_active(bstack1l1ll1l11l_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack11ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧශ")
        bstack1l1llllll1_opy_.bstack11l11lll_opy_(args[0])
        if runner.driver_initialised == bstack11ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨෂ"):
          feature_name = bstack1l111ll111_opy_ = str(runner.feature.name)
          bstack1l111ll111_opy_ = feature_name + bstack11ll_opy_ (u"ࠩࠣ࠱ࠥ࠭ස") + context.scenario.name
          bstack1l1ll1l11l_opy_.execute_script(bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨහ") + json.dumps(bstack1l111ll111_opy_) + bstack11ll_opy_ (u"ࠫࢂࢃࠧළ"))
    except Exception as e:
      logger.debug(bstack11ll_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩෆ").format(str(e)))
@measure(event_name=EVENTS.bstack1l1lll11ll_opy_, stage=STAGE.bstack1ll1111l1_opy_, hook_type=bstack11ll_opy_ (u"ࠨࡡࡧࡶࡨࡶࡘࡺࡥࡱࠤ෇"), bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack1ll1lll111_opy_(runner, name, context, bstack111llll11_opy_, *args):
  bstack1l1llllll1_opy_.bstack11l11ll1_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack1l1ll1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭෈") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1l1ll1l11l_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack11ll_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨ෉")
        feature_name = bstack1l111ll111_opy_ = str(runner.feature.name)
        bstack1l111ll111_opy_ = feature_name + bstack11ll_opy_ (u"ࠩࠣ࠱්ࠥ࠭") + context.scenario.name
        bstack1l1ll1l11l_opy_.execute_script(bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨ෋") + json.dumps(bstack1l111ll111_opy_) + bstack11ll_opy_ (u"ࠫࢂࢃࠧ෌"))
    if str(step_status).lower() == bstack11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ෍"):
      bstack1l11l1111l_opy_ = bstack11ll_opy_ (u"࠭ࠧ෎")
      bstack11l1l1111l_opy_ = bstack11ll_opy_ (u"ࠧࠨා")
      bstack1ll1l1l1l_opy_ = bstack11ll_opy_ (u"ࠨࠩැ")
      try:
        import traceback
        bstack1l11l1111l_opy_ = runner.exception.__class__.__name__
        bstack111llll1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11l1l1111l_opy_ = bstack11ll_opy_ (u"ࠩࠣࠫෑ").join(bstack111llll1_opy_)
        bstack1ll1l1l1l_opy_ = bstack111llll1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1ll11l1l11_opy_.format(str(e)))
      bstack1l11l1111l_opy_ += bstack1ll1l1l1l_opy_
      bstack11l11l1l1l_opy_(context, json.dumps(str(args[0].name) + bstack11ll_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤි") + str(bstack11l1l1111l_opy_)),
                          bstack11ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥී"))
      if runner.driver_initialised == bstack11ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥු"):
        bstack111l1l1lll_opy_(getattr(context, bstack11ll_opy_ (u"࠭ࡰࡢࡩࡨࠫ෕"), None), bstack11ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢූ"), bstack1l11l1111l_opy_)
        bstack1l1ll1l11l_opy_.execute_script(bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭෗") + json.dumps(str(args[0].name) + bstack11ll_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣෘ") + str(bstack11l1l1111l_opy_)) + bstack11ll_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪෙ"))
      if runner.driver_initialised == bstack11ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤේ"):
        bstack1ll1111111_opy_(bstack1l1ll1l11l_opy_, bstack11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬෛ"), bstack11ll_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥො") + str(bstack1l11l1111l_opy_))
    else:
      bstack11l11l1l1l_opy_(context, bstack11ll_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣෝ"), bstack11ll_opy_ (u"ࠣ࡫ࡱࡪࡴࠨෞ"))
      if runner.driver_initialised == bstack11ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢෟ"):
        bstack111l1l1lll_opy_(getattr(context, bstack11ll_opy_ (u"ࠪࡴࡦ࡭ࡥࠨ෠"), None), bstack11ll_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦ෡"))
      bstack1l1ll1l11l_opy_.execute_script(bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ෢") + json.dumps(str(args[0].name) + bstack11ll_opy_ (u"ࠨࠠ࠮ࠢࡓࡥࡸࡹࡥࡥࠣࠥ෣")) + bstack11ll_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭෤"))
      if runner.driver_initialised == bstack11ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨ෥"):
        bstack1ll1111111_opy_(bstack1l1ll1l11l_opy_, bstack11ll_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ෦"))
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩ෧").format(str(e)))
  bstack11l1l11111_opy_(runner, name, context, args[0], bstack111llll11_opy_, *args)
@measure(event_name=EVENTS.bstack111ll1l11l_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack1111l111ll_opy_(runner, name, context, bstack111llll11_opy_, *args):
  bstack1l1llllll1_opy_.end_test(args[0])
  try:
    bstack1ll1l111ll_opy_ = args[0].status.name
    bstack1l1ll1l11l_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ෨"), context.browser)
    bstack1l1ll1llll_opy_.bstack1l11l11ll_opy_(bstack1l1ll1l11l_opy_)
    if str(bstack1ll1l111ll_opy_).lower() == bstack11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ෩"):
      bstack1l11l1111l_opy_ = bstack11ll_opy_ (u"࠭ࠧ෪")
      bstack11l1l1111l_opy_ = bstack11ll_opy_ (u"ࠧࠨ෫")
      bstack1ll1l1l1l_opy_ = bstack11ll_opy_ (u"ࠨࠩ෬")
      try:
        import traceback
        bstack1l11l1111l_opy_ = runner.exception.__class__.__name__
        bstack111llll1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11l1l1111l_opy_ = bstack11ll_opy_ (u"ࠩࠣࠫ෭").join(bstack111llll1_opy_)
        bstack1ll1l1l1l_opy_ = bstack111llll1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1ll11l1l11_opy_.format(str(e)))
      bstack1l11l1111l_opy_ += bstack1ll1l1l1l_opy_
      bstack11l11l1l1l_opy_(context, json.dumps(str(args[0].name) + bstack11ll_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ෮") + str(bstack11l1l1111l_opy_)),
                          bstack11ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ෯"))
      if runner.driver_initialised == bstack11ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ෰") or runner.driver_initialised == bstack11ll_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෱"):
        bstack111l1l1lll_opy_(getattr(context, bstack11ll_opy_ (u"ࠧࡱࡣࡪࡩࠬෲ"), None), bstack11ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣෳ"), bstack1l11l1111l_opy_)
        bstack1l1ll1l11l_opy_.execute_script(bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ෴") + json.dumps(str(args[0].name) + bstack11ll_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ෵") + str(bstack11l1l1111l_opy_)) + bstack11ll_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫ෶"))
      if runner.driver_initialised == bstack11ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ෷") or runner.driver_initialised == bstack11ll_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෸"):
        bstack1ll1111111_opy_(bstack1l1ll1l11l_opy_, bstack11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ෹"), bstack11ll_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧ෺") + str(bstack1l11l1111l_opy_))
    else:
      bstack11l11l1l1l_opy_(context, bstack11ll_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥ෻"), bstack11ll_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣ෼"))
      if runner.driver_initialised == bstack11ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ෽") or runner.driver_initialised == bstack11ll_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ෾"):
        bstack111l1l1lll_opy_(getattr(context, bstack11ll_opy_ (u"࠭ࡰࡢࡩࡨࠫ෿"), None), bstack11ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ฀"))
      bstack1l1ll1l11l_opy_.execute_script(bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ก") + json.dumps(str(args[0].name) + bstack11ll_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨข")) + bstack11ll_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩฃ"))
      if runner.driver_initialised == bstack11ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨค") or runner.driver_initialised == bstack11ll_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬฅ"):
        bstack1ll1111111_opy_(bstack1l1ll1l11l_opy_, bstack11ll_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨฆ"))
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩง").format(str(e)))
  bstack11l1l11111_opy_(runner, name, context, context.scenario, bstack111llll11_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack11lll11ll_opy_(runner, name, context, bstack111llll11_opy_, *args):
    target = context.scenario if hasattr(context, bstack11ll_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪจ")) else context.feature
    bstack11l1l11111_opy_(runner, name, context, target, bstack111llll11_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack11l1ll11ll_opy_(runner, name, context, bstack111llll11_opy_, *args):
    try:
      bstack1l1ll1l11l_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨฉ"), context.browser)
      bstack11111ll1l_opy_ = bstack11ll_opy_ (u"ࠪࠫช")
      if context.failed is True:
        bstack11111l1ll1_opy_ = []
        bstack111ll1llll_opy_ = []
        bstack11l1ll1lll_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack11111l1ll1_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack111llll1_opy_ = traceback.format_tb(exc_tb)
            bstack11lllll111_opy_ = bstack11ll_opy_ (u"ࠫࠥ࠭ซ").join(bstack111llll1_opy_)
            bstack111ll1llll_opy_.append(bstack11lllll111_opy_)
            bstack11l1ll1lll_opy_.append(bstack111llll1_opy_[-1])
        except Exception as e:
          logger.debug(bstack1ll11l1l11_opy_.format(str(e)))
        bstack1l11l1111l_opy_ = bstack11ll_opy_ (u"ࠬ࠭ฌ")
        for i in range(len(bstack11111l1ll1_opy_)):
          bstack1l11l1111l_opy_ += bstack11111l1ll1_opy_[i] + bstack11l1ll1lll_opy_[i] + bstack11ll_opy_ (u"࠭࡜࡯ࠩญ")
        bstack11111ll1l_opy_ = bstack11ll_opy_ (u"ࠧࠡࠩฎ").join(bstack111ll1llll_opy_)
        if runner.driver_initialised in [bstack11ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤฏ"), bstack11ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨฐ")]:
          bstack11l11l1l1l_opy_(context, bstack11111ll1l_opy_, bstack11ll_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤฑ"))
          bstack111l1l1lll_opy_(getattr(context, bstack11ll_opy_ (u"ࠫࡵࡧࡧࡦࠩฒ"), None), bstack11ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧณ"), bstack1l11l1111l_opy_)
          bstack1l1ll1l11l_opy_.execute_script(bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫด") + json.dumps(bstack11111ll1l_opy_) + bstack11ll_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧต"))
          bstack1ll1111111_opy_(bstack1l1ll1l11l_opy_, bstack11ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣถ"), bstack11ll_opy_ (u"ࠤࡖࡳࡲ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰࡵࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡡࡴࠢท") + str(bstack1l11l1111l_opy_))
          bstack1111l11ll_opy_ = bstack111ll11l11_opy_(bstack11111ll1l_opy_, runner.feature.name, logger)
          if (bstack1111l11ll_opy_ != None):
            bstack11l1l1l11l_opy_.append(bstack1111l11ll_opy_)
      else:
        if runner.driver_initialised in [bstack11ll_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦธ"), bstack11ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣน")]:
          bstack11l11l1l1l_opy_(context, bstack11ll_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣบ") + str(runner.feature.name) + bstack11ll_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣป"), bstack11ll_opy_ (u"ࠢࡪࡰࡩࡳࠧผ"))
          bstack111l1l1lll_opy_(getattr(context, bstack11ll_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ฝ"), None), bstack11ll_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤพ"))
          bstack1l1ll1l11l_opy_.execute_script(bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨฟ") + json.dumps(bstack11ll_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢภ") + str(runner.feature.name) + bstack11ll_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢม")) + bstack11ll_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬย"))
          bstack1ll1111111_opy_(bstack1l1ll1l11l_opy_, bstack11ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧร"))
          bstack1111l11ll_opy_ = bstack111ll11l11_opy_(bstack11111ll1l_opy_, runner.feature.name, logger)
          if (bstack1111l11ll_opy_ != None):
            bstack11l1l1l11l_opy_.append(bstack1111l11ll_opy_)
    except Exception as e:
      logger.debug(bstack11ll_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪฤ").format(str(e)))
    bstack11l1l11111_opy_(runner, name, context, context.feature, bstack111llll11_opy_, *args)
@measure(event_name=EVENTS.bstack1l1lll11ll_opy_, stage=STAGE.bstack1ll1111l1_opy_, hook_type=bstack11ll_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡂ࡮࡯ࠦล"), bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack111ll111l_opy_(runner, name, context, bstack111llll11_opy_, *args):
    bstack11l1l11111_opy_(runner, name, context, runner, bstack111llll11_opy_, *args)
def bstack1ll1l1l1ll_opy_(self, name, context, *args):
  try:
    if bstack1ll1l1111_opy_:
      platform_index = int(threading.current_thread()._name) % bstack1111l11111_opy_
      bstack11l1lllll_opy_ = CONFIG[bstack11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ฦ")][platform_index]
      os.environ[bstack11ll_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬว")] = json.dumps(bstack11l1lllll_opy_)
    global bstack111llll11_opy_
    if not hasattr(self, bstack11ll_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡦࡦࠪศ")):
      self.driver_initialised = None
    bstack1l111l1lll_opy_ = {
        bstack11ll_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪษ"): bstack1ll1ll11l1_opy_,
        bstack11ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠨส"): bstack1ll111l1l_opy_,
        bstack11ll_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡶࡤ࡫ࠬห"): bstack1l1111l11l_opy_,
        bstack11ll_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫฬ"): bstack1l11l1llll_opy_,
        bstack11ll_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠨอ"): bstack1111ll11l_opy_,
        bstack11ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡹ࡫ࡰࠨฮ"): bstack1ll1lll111_opy_,
        bstack11ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ฯ"): bstack1111l111ll_opy_,
        bstack11ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡺࡡࡨࠩะ"): bstack11lll11ll_opy_,
        bstack11ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧั"): bstack11l1ll11ll_opy_,
        bstack11ll_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫา"): bstack111ll111l_opy_
    }
    handler = bstack1l111l1lll_opy_.get(name, bstack111llll11_opy_)
    try:
      handler(self, name, context, bstack111llll11_opy_, *args)
    except Exception as e:
      logger.debug(bstack11ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨࠤ࡭ࡵ࡯࡬ࠢ࡫ࡥࡳࡪ࡬ࡦࡴࠣࡿࢂࡀࠠࡼࡿࠪำ").format(name, str(e)))
    if name in [bstack11ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪิ"), bstack11ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬี"), bstack11ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨึ")]:
      try:
        bstack1l1ll1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll1111l1_opy_(bstack11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬื")) else context.browser
        bstack1llllll1ll_opy_ = (
          (name == bstack11ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ุࠪ") and self.driver_initialised == bstack11ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰูࠧ")) or
          (name == bstack11ll_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦฺࠩ") and self.driver_initialised == bstack11ll_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦ฻")) or
          (name == bstack11ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬ฼") and self.driver_initialised in [bstack11ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ฽"), bstack11ll_opy_ (u"ࠨࡩ࡯ࡵࡷࡩࡵࠨ฾")]) or
          (name == bstack11ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡵࡧࡳࠫ฿") and self.driver_initialised == bstack11ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨเ"))
        )
        if bstack1llllll1ll_opy_:
          self.driver_initialised = None
          if bstack1l1ll1l11l_opy_ and hasattr(bstack1l1ll1l11l_opy_, bstack11ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩ࠭แ")):
            try:
              bstack1l1ll1l11l_opy_.quit()
            except Exception as e:
              logger.debug(bstack11ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡴࡹ࡮ࡺࡴࡪࡰࡪࠤࡩࡸࡩࡷࡧࡵࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡩࡱࡲ࡯࠿ࠦࡻࡾࠩโ").format(str(e)))
      except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡮࡯ࡰ࡭ࠣࡧࡱ࡫ࡡ࡯ࡷࡳࠤ࡫ࡵࡲࠡࡽࢀ࠾ࠥࢁࡽࠨใ").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠬࡉࡲࡪࡶ࡬ࡧࡦࡲࠠࡦࡴࡵࡳࡷࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦࠢࡵࡹࡳࠦࡨࡰࡱ࡮ࠤࢀࢃ࠺ࠡࡽࢀࠫไ").format(name, str(e)))
    try:
      bstack111llll11_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack11ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡳࡷ࡯ࡧࡪࡰࡤࡰࠥࡨࡥࡩࡣࡹࡩࠥ࡮࡯ࡰ࡭ࠣࡿࢂࡀࠠࡼࡿࠪๅ").format(name, str(e2)))
def bstack1l1llll11l_opy_(config, startdir):
  return bstack11ll_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧๆ").format(bstack11ll_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢ็"))
notset = Notset()
def bstack111l1ll1l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack111l11l1l1_opy_
  if str(name).lower() == bstack11ll_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳ่ࠩ"):
    return bstack11ll_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤ้")
  else:
    return bstack111l11l1l1_opy_(self, name, default, skip)
def bstack11l111l111_opy_(item, when):
  global bstack11ll111lll_opy_
  try:
    bstack11ll111lll_opy_(item, when)
  except Exception as e:
    pass
def bstack1l1ll11ll_opy_():
  return
def bstack11l1l1l11_opy_(type, name, status, reason, bstack11l111ll1_opy_, bstack1l1l11ll11_opy_):
  bstack1ll1111ll_opy_ = {
    bstack11ll_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱ๊ࠫ"): type,
    bstack11ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ๋"): {}
  }
  if type == bstack11ll_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ์"):
    bstack1ll1111ll_opy_[bstack11ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪํ")][bstack11ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ๎")] = bstack11l111ll1_opy_
    bstack1ll1111ll_opy_[bstack11ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ๏")][bstack11ll_opy_ (u"ࠪࡨࡦࡺࡡࠨ๐")] = json.dumps(str(bstack1l1l11ll11_opy_))
  if type == bstack11ll_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ๑"):
    bstack1ll1111ll_opy_[bstack11ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ๒")][bstack11ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ๓")] = name
  if type == bstack11ll_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪ๔"):
    bstack1ll1111ll_opy_[bstack11ll_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ๕")][bstack11ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ๖")] = status
    if status == bstack11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ๗"):
      bstack1ll1111ll_opy_[bstack11ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ๘")][bstack11ll_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ๙")] = json.dumps(str(reason))
  bstack11ll11l111_opy_ = bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ๚").format(json.dumps(bstack1ll1111ll_opy_))
  return bstack11ll11l111_opy_
def bstack11llllll11_opy_(driver_command, response):
    if driver_command == bstack11ll_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫ๛"):
        bstack1l111l1l_opy_.bstack1l1l11lll_opy_({
            bstack11ll_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧ๜"): response[bstack11ll_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨ๝")],
            bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ๞"): bstack1l111l1l_opy_.current_test_uuid()
        })
def bstack11l1l11ll_opy_(item, call, rep):
  global bstack1ll1l1l11l_opy_
  global bstack1111lll1l_opy_
  global bstack111l1lll1l_opy_
  name = bstack11ll_opy_ (u"ࠫࠬ๟")
  try:
    if rep.when == bstack11ll_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ๠"):
      bstack1l1ll1111l_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack111l1lll1l_opy_:
          name = str(rep.nodeid)
          bstack1lll1l1l1l_opy_ = bstack11l1l1l11_opy_(bstack11ll_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ๡"), name, bstack11ll_opy_ (u"ࠧࠨ๢"), bstack11ll_opy_ (u"ࠨࠩ๣"), bstack11ll_opy_ (u"ࠩࠪ๤"), bstack11ll_opy_ (u"ࠪࠫ๥"))
          threading.current_thread().bstack1ll11l11ll_opy_ = name
          for driver in bstack1111lll1l_opy_:
            if bstack1l1ll1111l_opy_ == driver.session_id:
              driver.execute_script(bstack1lll1l1l1l_opy_)
      except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ๦").format(str(e)))
      try:
        bstack11ll1l11l_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭๧"):
          status = bstack11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭๨") if rep.outcome.lower() == bstack11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ๩") else bstack11ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ๪")
          reason = bstack11ll_opy_ (u"ࠩࠪ๫")
          if status == bstack11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ๬"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11ll_opy_ (u"ࠫ࡮ࡴࡦࡰࠩ๭") if status == bstack11ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ๮") else bstack11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ๯")
          data = name + bstack11ll_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩ๰") if status == bstack11ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ๱") else name + bstack11ll_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤࠬ๲") + reason
          bstack11l11ll11l_opy_ = bstack11l1l1l11_opy_(bstack11ll_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬ๳"), bstack11ll_opy_ (u"ࠫࠬ๴"), bstack11ll_opy_ (u"ࠬ࠭๵"), bstack11ll_opy_ (u"࠭ࠧ๶"), level, data)
          for driver in bstack1111lll1l_opy_:
            if bstack1l1ll1111l_opy_ == driver.session_id:
              driver.execute_script(bstack11l11ll11l_opy_)
      except Exception as e:
        logger.debug(bstack11ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ๷").format(str(e)))
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬ๸").format(str(e)))
  bstack1ll1l1l11l_opy_(item, call, rep)
def bstack1ll1ll1ll_opy_(driver, bstack1l1l1l1l11_opy_, test=None):
  global bstack1llll1111l_opy_
  if test != None:
    bstack1ll11l111l_opy_ = getattr(test, bstack11ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ๹"), None)
    bstack111l1111l1_opy_ = getattr(test, bstack11ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ๺"), None)
    PercySDK.screenshot(driver, bstack1l1l1l1l11_opy_, bstack1ll11l111l_opy_=bstack1ll11l111l_opy_, bstack111l1111l1_opy_=bstack111l1111l1_opy_, bstack1ll111lll1_opy_=bstack1llll1111l_opy_)
  else:
    PercySDK.screenshot(driver, bstack1l1l1l1l11_opy_)
@measure(event_name=EVENTS.bstack111ll11lll_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack11l111l1l1_opy_(driver):
  if bstack111l1ll11l_opy_.bstack11ll11111_opy_() is True or bstack111l1ll11l_opy_.capturing() is True:
    return
  bstack111l1ll11l_opy_.bstack1llll1ll1l_opy_()
  while not bstack111l1ll11l_opy_.bstack11ll11111_opy_():
    bstack1ll1l1ll1l_opy_ = bstack111l1ll11l_opy_.bstack111ll11l1l_opy_()
    bstack1ll1ll1ll_opy_(driver, bstack1ll1l1ll1l_opy_)
  bstack111l1ll11l_opy_.bstack1l1ll1lll_opy_()
def bstack1111llll1l_opy_(sequence, driver_command, response = None, bstack11lll11lll_opy_ = None, args = None):
    try:
      if sequence != bstack11ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫ๻"):
        return
      if percy.bstack1l1llll1l1_opy_() == bstack11ll_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦ๼"):
        return
      bstack1ll1l1ll1l_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ๽"), None)
      for command in bstack1111ll1lll_opy_:
        if command == driver_command:
          with bstack1l11l1lll1_opy_:
            bstack11111l1l11_opy_ = bstack1111lll1l_opy_.copy()
          for driver in bstack11111l1l11_opy_:
            bstack11l111l1l1_opy_(driver)
      bstack11ll1ll1l_opy_ = percy.bstack11111lllll_opy_()
      if driver_command in bstack1l11111l11_opy_[bstack11ll1ll1l_opy_]:
        bstack111l1ll11l_opy_.bstack11l1ll1l1_opy_(bstack1ll1l1ll1l_opy_, driver_command)
    except Exception as e:
      pass
def bstack11l1l11ll1_opy_(framework_name):
  if bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ๾")):
      return
  bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬ๿"), True)
  global bstack11l11l111l_opy_
  global bstack1ll1ll11l_opy_
  global bstack1lllllll11_opy_
  bstack11l11l111l_opy_ = framework_name
  logger.info(bstack11l1111111_opy_.format(bstack11l11l111l_opy_.split(bstack11ll_opy_ (u"ࠩ࠰ࠫ຀"))[0]))
  bstack111111l1l1_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1ll1l1111_opy_:
      Service.start = bstack1l111ll1l_opy_
      Service.stop = bstack1l1111llll_opy_
      webdriver.Remote.get = bstack11llll1111_opy_
      WebDriver.quit = bstack11ll11ll11_opy_
      webdriver.Remote.__init__ = bstack1lll11ll11_opy_
    if not bstack1ll1l1111_opy_:
        webdriver.Remote.__init__ = bstack11lllll11_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack11l1ll1l1l_opy_
    bstack1ll1ll11l_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1ll1l1111_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1ll11l1l1_opy_
  except Exception as e:
    pass
  bstack11lll111l1_opy_()
  if not bstack1ll1ll11l_opy_:
    bstack1lll11llll_opy_(bstack11ll_opy_ (u"ࠥࡔࡦࡩ࡫ࡢࡩࡨࡷࠥࡴ࡯ࡵࠢ࡬ࡲࡸࡺࡡ࡭࡮ࡨࡨࠧກ"), bstack11l1111l1l_opy_)
  if bstack11lll111l_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack11ll_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬຂ")) and callable(getattr(RemoteConnection, bstack11ll_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭຃"))):
        RemoteConnection._get_proxy_url = bstack11111ll11l_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack11111ll11l_opy_
    except Exception as e:
      logger.error(bstack11l1ll1ll1_opy_.format(str(e)))
  if bstack1ll1l1l111_opy_():
    bstack1l1ll111l_opy_(CONFIG, logger)
  if (bstack11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬຄ") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1l1llll1l1_opy_() == bstack11ll_opy_ (u"ࠢࡵࡴࡸࡩࠧ຅"):
          bstack11l111ll11_opy_(bstack1111llll1l_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack111lll111_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1ll1l1ll1_opy_
      except Exception as e:
        logger.warn(bstack11llll1ll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack11l111l1ll_opy_
      except Exception as e:
        logger.debug(bstack111ll1ll1l_opy_ + str(e))
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack11llll1ll_opy_)
    Output.start_test = bstack11lll1111_opy_
    Output.end_test = bstack111l11llll_opy_
    TestStatus.__init__ = bstack111llll1l_opy_
    QueueItem.__init__ = bstack1l111l111l_opy_
    pabot._create_items = bstack1111l1l11_opy_
    try:
      from pabot import __version__ as bstack1ll1111l11_opy_
      if version.parse(bstack1ll1111l11_opy_) >= version.parse(bstack11ll_opy_ (u"ࠨ࠷࠱࠴࠳࠶ࠧຆ")):
        pabot._run = bstack1l1ll1ll1l_opy_
      elif version.parse(bstack1ll1111l11_opy_) >= version.parse(bstack11ll_opy_ (u"ࠩ࠷࠲࠷࠴࠰ࠨງ")):
        pabot._run = bstack11l1l111l1_opy_
      elif version.parse(bstack1ll1111l11_opy_) >= version.parse(bstack11ll_opy_ (u"ࠪ࠶࠳࠷࠵࠯࠲ࠪຈ")):
        pabot._run = bstack1111ll11ll_opy_
      elif version.parse(bstack1ll1111l11_opy_) >= version.parse(bstack11ll_opy_ (u"ࠫ࠷࠴࠱࠴࠰࠳ࠫຉ")):
        pabot._run = bstack1l1l1lll1_opy_
      else:
        pabot._run = bstack11lll1l111_opy_
    except Exception as e:
      pabot._run = bstack11lll1l111_opy_
    pabot._create_command_for_execution = bstack11l1l11l11_opy_
    pabot._report_results = bstack11lll1lll1_opy_
  if bstack11ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬຊ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack1l11111ll_opy_)
    Runner.run_hook = bstack1ll1l1l1ll_opy_
    Step.run = bstack1l11l11ll1_opy_
  if bstack11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭຋") in str(framework_name).lower():
    if not bstack1ll1l1111_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1l1llll11l_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1l1ll11ll_opy_
      Config.getoption = bstack111l1ll1l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack11l1l11ll_opy_
    except Exception as e:
      pass
def bstack1111lll11_opy_():
  global CONFIG
  if bstack11ll_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧຌ") in CONFIG and int(CONFIG[bstack11ll_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨຍ")]) > 1:
    logger.warn(bstack11lll1llll_opy_)
def bstack11ll1l111_opy_(arg, bstack1lllll1ll_opy_, bstack11l1111lll_opy_=None):
  global CONFIG
  global bstack1lllll1l11_opy_
  global bstack1l111ll1l1_opy_
  global bstack1ll1l1111_opy_
  global bstack1111l111_opy_
  bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩຎ")
  if bstack1lllll1ll_opy_ and isinstance(bstack1lllll1ll_opy_, str):
    bstack1lllll1ll_opy_ = eval(bstack1lllll1ll_opy_)
  CONFIG = bstack1lllll1ll_opy_[bstack11ll_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪຏ")]
  bstack1lllll1l11_opy_ = bstack1lllll1ll_opy_[bstack11ll_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬຐ")]
  bstack1l111ll1l1_opy_ = bstack1lllll1ll_opy_[bstack11ll_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧຑ")]
  bstack1ll1l1111_opy_ = bstack1lllll1ll_opy_[bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩຒ")]
  bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨຓ"), bstack1ll1l1111_opy_)
  os.environ[bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪດ")] = bstack1l11ll1l1l_opy_
  os.environ[bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠨຕ")] = json.dumps(CONFIG)
  os.environ[bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡋ࡙ࡇࡥࡕࡓࡎࠪຖ")] = bstack1lllll1l11_opy_
  os.environ[bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬທ")] = str(bstack1l111ll1l1_opy_)
  os.environ[bstack11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫຘ")] = str(True)
  if bstack1l11111111_opy_(arg, [bstack11ll_opy_ (u"࠭࠭࡯ࠩນ"), bstack11ll_opy_ (u"ࠧ࠮࠯ࡱࡹࡲࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨບ")]) != -1:
    os.environ[bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡃࡕࡅࡑࡒࡅࡍࠩປ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack111ll11ll1_opy_)
    return
  bstack111ll1ll1_opy_()
  global bstack1lllll111l_opy_
  global bstack1llll1111l_opy_
  global bstack111l1l11l_opy_
  global bstack11lll1lll_opy_
  global bstack1l11llllll_opy_
  global bstack1lllllll11_opy_
  global bstack11l111ll1l_opy_
  arg.append(bstack11ll_opy_ (u"ࠤ࠰࡛ࠧຜ"))
  arg.append(bstack11ll_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧ࠽ࡑࡴࡪࡵ࡭ࡧࠣࡥࡱࡸࡥࡢࡦࡼࠤ࡮ࡳࡰࡰࡴࡷࡩࡩࡀࡰࡺࡶࡨࡷࡹ࠴ࡐࡺࡶࡨࡷࡹ࡝ࡡࡳࡰ࡬ࡲ࡬ࠨຝ"))
  arg.append(bstack11ll_opy_ (u"ࠦ࠲࡝ࠢພ"))
  arg.append(bstack11ll_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩ࠿࡚ࡨࡦࠢ࡫ࡳࡴࡱࡩ࡮ࡲ࡯ࠦຟ"))
  global bstack11ll111l1_opy_
  global bstack1l111lllll_opy_
  global bstack1l1ll111l1_opy_
  global bstack11l11l1l1_opy_
  global bstack111l111lll_opy_
  global bstack111lll11l1_opy_
  global bstack1ll111111_opy_
  global bstack1l11ll11l_opy_
  global bstack11ll1l1111_opy_
  global bstack1l11ll1l11_opy_
  global bstack111l11l1l1_opy_
  global bstack11ll111lll_opy_
  global bstack1ll1l1l11l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11ll111l1_opy_ = webdriver.Remote.__init__
    bstack1l111lllll_opy_ = WebDriver.quit
    bstack1l11ll11l_opy_ = WebDriver.close
    bstack11ll1l1111_opy_ = WebDriver.get
    bstack1l1ll111l1_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack11l1l1l1l1_opy_(CONFIG) and bstack11llll1l1l_opy_():
    if bstack11l11l11l1_opy_() < version.parse(bstack11l1l1l111_opy_):
      logger.error(bstack1111llllll_opy_.format(bstack11l11l11l1_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11ll_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧຠ")) and callable(getattr(RemoteConnection, bstack11ll_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨມ"))):
          bstack1l11ll1l11_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1l11ll1l11_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack11l1ll1ll1_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack111l11l1l1_opy_ = Config.getoption
    from _pytest import runner
    bstack11ll111lll_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1lll1l1ll_opy_)
  try:
    from pytest_bdd import reporting
    bstack1ll1l1l11l_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11ll_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩຢ"))
  bstack111l1l11l_opy_ = CONFIG.get(bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ຣ"), {}).get(bstack11ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ຤"))
  bstack11l111ll1l_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack111ll1l11_opy_():
      bstack1111l11l11_opy_.invoke(Events.CONNECT, bstack1l1l11llll_opy_())
    platform_index = int(os.environ.get(bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫລ"), bstack11ll_opy_ (u"ࠬ࠶ࠧ຦")))
  else:
    bstack11l1l11ll1_opy_(bstack11l1ll1111_opy_)
  os.environ[bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧວ")] = CONFIG[bstack11ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩຨ")]
  os.environ[bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫຩ")] = CONFIG[bstack11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬສ")]
  os.environ[bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ຫ")] = bstack1ll1l1111_opy_.__str__()
  from _pytest.config import main as bstack11111l111_opy_
  bstack1lll1ll11l_opy_ = []
  try:
    exit_code = bstack11111l111_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack11ll1111ll_opy_()
    if bstack11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨຬ") in multiprocessing.current_process().__dict__.keys():
      for bstack1ll1ll1lll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1lll1ll11l_opy_.append(bstack1ll1ll1lll_opy_)
    try:
      bstack1ll1l1111l_opy_ = (bstack1lll1ll11l_opy_, int(exit_code))
      bstack11l1111lll_opy_.append(bstack1ll1l1111l_opy_)
    except:
      bstack11l1111lll_opy_.append((bstack1lll1ll11l_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1lll1ll11l_opy_.append({bstack11ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪອ"): bstack11ll_opy_ (u"࠭ࡐࡳࡱࡦࡩࡸࡹࠠࠨຮ") + os.environ.get(bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧຯ")), bstack11ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧະ"): traceback.format_exc(), bstack11ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨັ"): int(os.environ.get(bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪາ")))})
    bstack11l1111lll_opy_.append((bstack1lll1ll11l_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack11ll_opy_ (u"ࠦࡷ࡫ࡴࡳ࡫ࡨࡷࠧຳ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack1l11llll1_opy_ = e.__class__.__name__
    print(bstack11ll_opy_ (u"ࠧࠫࡳ࠻ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡥࡩ࡭ࡧࡶࡦࠢࡷࡩࡸࡺࠠࠦࡵࠥິ") % (bstack1l11llll1_opy_, e))
    return 1
def bstack1l1l1l11l_opy_(arg):
  global bstack1llll1llll_opy_
  bstack11l1l11ll1_opy_(bstack11111llll1_opy_)
  os.environ[bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧີ")] = str(bstack1l111ll1l1_opy_)
  retries = bstack111ll1ll_opy_.bstack1111l1ll_opy_(CONFIG)
  status_code = 0
  if bstack111ll1ll_opy_.bstack111l1l1l_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack111l11l11l_opy_
    status_code = bstack111l11l11l_opy_(arg)
  if status_code != 0:
    bstack1llll1llll_opy_ = status_code
def bstack11l11lllll_opy_():
  logger.info(bstack1ll11lllll_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ຶ"), help=bstack11ll_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡦࡳࡳ࡬ࡩࡨࠩື"))
  parser.add_argument(bstack11ll_opy_ (u"ࠩ࠰ࡹຸࠬ"), bstack11ll_opy_ (u"ࠪ࠱࠲ࡻࡳࡦࡴࡱࡥࡲ࡫ູࠧ"), help=bstack11ll_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡷࡶࡩࡷࡴࡡ࡮ࡧ຺ࠪ"))
  parser.add_argument(bstack11ll_opy_ (u"ࠬ࠳࡫ࠨົ"), bstack11ll_opy_ (u"࠭࠭࠮࡭ࡨࡽࠬຼ"), help=bstack11ll_opy_ (u"࡚ࠧࡱࡸࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡦࡩࡣࡦࡵࡶࠤࡰ࡫ࡹࠨຽ"))
  parser.add_argument(bstack11ll_opy_ (u"ࠨ࠯ࡩࠫ຾"), bstack11ll_opy_ (u"ࠩ࠰࠱࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ຿"), help=bstack11ll_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩເ"))
  bstack1111llll11_opy_ = parser.parse_args()
  try:
    bstack11l1l11lll_opy_ = bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡫ࡪࡴࡥࡳ࡫ࡦ࠲ࡾࡳ࡬࠯ࡵࡤࡱࡵࡲࡥࠨແ")
    if bstack1111llll11_opy_.framework and bstack1111llll11_opy_.framework not in (bstack11ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬໂ"), bstack11ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧໃ")):
      bstack11l1l11lll_opy_ = bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭ໄ")
    bstack1l1llll1ll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1l11lll_opy_)
    bstack11llllll1l_opy_ = open(bstack1l1llll1ll_opy_, bstack11ll_opy_ (u"ࠨࡴࠪ໅"))
    bstack1l111111l1_opy_ = bstack11llllll1l_opy_.read()
    bstack11llllll1l_opy_.close()
    if bstack1111llll11_opy_.username:
      bstack1l111111l1_opy_ = bstack1l111111l1_opy_.replace(bstack11ll_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩໆ"), bstack1111llll11_opy_.username)
    if bstack1111llll11_opy_.key:
      bstack1l111111l1_opy_ = bstack1l111111l1_opy_.replace(bstack11ll_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬ໇"), bstack1111llll11_opy_.key)
    if bstack1111llll11_opy_.framework:
      bstack1l111111l1_opy_ = bstack1l111111l1_opy_.replace(bstack11ll_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏ່ࠬ"), bstack1111llll11_opy_.framework)
    file_name = bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨ້")
    file_path = os.path.abspath(file_name)
    bstack1ll1lll11_opy_ = open(file_path, bstack11ll_opy_ (u"࠭ࡷࠨ໊"))
    bstack1ll1lll11_opy_.write(bstack1l111111l1_opy_)
    bstack1ll1lll11_opy_.close()
    logger.info(bstack1l1111l111_opy_)
    try:
      os.environ[bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌ໋ࠩ")] = bstack1111llll11_opy_.framework if bstack1111llll11_opy_.framework != None else bstack11ll_opy_ (u"ࠣࠤ໌")
      config = yaml.safe_load(bstack1l111111l1_opy_)
      config[bstack11ll_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩໍ")] = bstack11ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠰ࡷࡪࡺࡵࡱࠩ໎")
      bstack1l1llll1l_opy_(bstack11lll11ll1_opy_, config)
    except Exception as e:
      logger.debug(bstack11lll11l1l_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1l1ll11111_opy_.format(str(e)))
def bstack1l1llll1l_opy_(bstack11l11111l_opy_, config, bstack1l1l1ll1l1_opy_={}):
  global bstack1ll1l1111_opy_
  global bstack1111l1ll11_opy_
  global bstack1111l111_opy_
  if not config:
    return
  bstack1l1ll111ll_opy_ = bstack111lll1lll_opy_ if not bstack1ll1l1111_opy_ else (
    bstack1l1l1ll11l_opy_ if bstack11ll_opy_ (u"ࠫࡦࡶࡰࠨ໏") in config else (
        bstack1l11l1l1ll_opy_ if config.get(bstack11ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ໐")) else bstack1lll11111l_opy_
    )
)
  bstack1l111lll1_opy_ = False
  bstack1l1l1l1ll_opy_ = False
  if bstack1ll1l1111_opy_ is True:
      if bstack11ll_opy_ (u"࠭ࡡࡱࡲࠪ໑") in config:
          bstack1l111lll1_opy_ = True
      else:
          bstack1l1l1l1ll_opy_ = True
  bstack11lll1l1ll_opy_ = bstack1111l1l11l_opy_.bstack11llll11l_opy_(config, bstack1111l1ll11_opy_)
  bstack1ll1llllll_opy_ = bstack1lll111lll_opy_()
  data = {
    bstack11ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ໒"): config[bstack11ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ໓")],
    bstack11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ໔"): config[bstack11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭໕")],
    bstack11ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ໖"): bstack11l11111l_opy_,
    bstack11ll_opy_ (u"ࠬࡪࡥࡵࡧࡦࡸࡪࡪࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ໗"): os.environ.get(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ໘"), bstack1111l1ll11_opy_),
    bstack11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ໙"): bstack1l11l1lll_opy_,
    bstack11ll_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮ࠪ໚"): bstack1llll111l1_opy_(),
    bstack11ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໛"): {
      bstack11ll_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨໜ"): str(config[bstack11ll_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫໝ")]) if bstack11ll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬໞ") in config else bstack11ll_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢໟ"),
      bstack11ll_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࡘࡨࡶࡸ࡯࡯࡯ࠩ໠"): sys.version,
      bstack11ll_opy_ (u"ࠨࡴࡨࡪࡪࡸࡲࡦࡴࠪ໡"): bstack1ll1l1l1l1_opy_(os.environ.get(bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ໢"), bstack1111l1ll11_opy_)),
      bstack11ll_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬ໣"): bstack11ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ໤"),
      bstack11ll_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭໥"): bstack1l1ll111ll_opy_,
      bstack11ll_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ໦"): bstack11lll1l1ll_opy_,
      bstack11ll_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡠࡷࡸ࡭ࡩ࠭໧"): os.environ[bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭໨")],
      bstack11ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ໩"): os.environ.get(bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ໪"), bstack1111l1ll11_opy_),
      bstack11ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ໫"): bstack1111l1111l_opy_(os.environ.get(bstack11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ໬"), bstack1111l1ll11_opy_)),
      bstack11ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ໭"): bstack1ll1llllll_opy_.get(bstack11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ໮")),
      bstack11ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ໯"): bstack1ll1llllll_opy_.get(bstack11ll_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ໰")),
      bstack11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໱"): config[bstack11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ໲")] if config[bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ໳")] else bstack11ll_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢ໴"),
      bstack11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ໵"): str(config[bstack11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໶")]) if bstack11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ໷") in config else bstack11ll_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦ໸"),
      bstack11ll_opy_ (u"ࠫࡴࡹࠧ໹"): sys.platform,
      bstack11ll_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧ໺"): socket.gethostname(),
      bstack11ll_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ໻"): bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ໼"))
    }
  }
  if not bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ໽")) is None:
    data[bstack11ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໾")][bstack11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡒ࡫ࡴࡢࡦࡤࡸࡦ࠭໿")] = {
      bstack11ll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫༀ"): bstack11ll_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪ༁"),
      bstack11ll_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭༂"): bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ༃")),
      bstack11ll_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࡏࡷࡰࡦࡪࡸࠧ༄"): bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡑࡳࠬ༅"))
    }
  if bstack11l11111l_opy_ == bstack1l11l1l111_opy_:
    data[bstack11ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭༆")][bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡆࡳࡳ࡬ࡩࡨࠩ༇")] = bstack1l1lllll1_opy_(config)
    data[bstack11ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ༈")][bstack11ll_opy_ (u"࠭ࡩࡴࡒࡨࡶࡨࡿࡁࡶࡶࡲࡉࡳࡧࡢ࡭ࡧࡧࠫ༉")] = percy.bstack11l1lll11_opy_
    data[bstack11ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ༊")][bstack11ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࡂࡶ࡫࡯ࡨࡎࡪࠧ་")] = percy.percy_build_id
  if not bstack111ll1ll_opy_.bstack1l11ll1ll_opy_(CONFIG):
    data[bstack11ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ༌")][bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠧ།")] = bstack111ll1ll_opy_.bstack1l11ll1ll_opy_(CONFIG)
  bstack1lll11l11_opy_ = bstack1lll1l11l_opy_.bstack11111ll1_opy_(CONFIG, logger)
  bstack11111lll_opy_ = bstack111ll1ll_opy_.bstack11111ll1_opy_(config=CONFIG)
  if bstack1lll11l11_opy_ is not None and bstack11111lll_opy_ is not None and bstack11111lll_opy_.bstack1111111l_opy_():
    data[bstack11ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ༎")][bstack11111lll_opy_.bstack1l111lll11_opy_()] = bstack1lll11l11_opy_.bstack1111l1l1ll_opy_()
  update(data[bstack11ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ༏")], bstack1l1l1ll1l1_opy_)
  try:
    response = bstack1ll1l1lll_opy_(bstack11ll_opy_ (u"࠭ࡐࡐࡕࡗࠫ༐"), bstack1lll11l111_opy_(bstack111l11l1l_opy_), data, {
      bstack11ll_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ༑"): (config[bstack11ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ༒")], config[bstack11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ༓")])
    })
    if response:
      logger.debug(bstack11ll111l11_opy_.format(bstack11l11111l_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11ll11l11l_opy_.format(str(e)))
def bstack1ll1l1l1l1_opy_(framework):
  return bstack11ll_opy_ (u"ࠥࡿࢂ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࢀࢃࠢ༔").format(str(framework), __version__) if framework else bstack11ll_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧ༕").format(
    __version__)
def bstack111ll1ll1_opy_():
  global CONFIG
  global bstack1ll11l1lll_opy_
  if bool(CONFIG):
    return
  try:
    bstack1lll111111_opy_()
    logger.debug(bstack111l111ll1_opy_.format(str(CONFIG)))
    bstack1ll11l1lll_opy_ = bstack11l1l1l1ll_opy_.configure_logger(CONFIG, bstack1ll11l1lll_opy_)
    bstack111111l1l1_opy_()
  except Exception as e:
    logger.error(bstack11ll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࠤ༖") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11ll11llll_opy_
  atexit.register(bstack111llll1l1_opy_)
  signal.signal(signal.SIGINT, bstack11ll1ll11_opy_)
  signal.signal(signal.SIGTERM, bstack11ll1ll11_opy_)
def bstack11ll11llll_opy_(exctype, value, traceback):
  global bstack1111lll1l_opy_
  try:
    for driver in bstack1111lll1l_opy_:
      bstack1ll1111111_opy_(driver, bstack11ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭༗"), bstack11ll_opy_ (u"ࠢࡔࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰ༘ࠥ") + str(value))
  except Exception:
    pass
  logger.info(bstack1l11ll1lll_opy_)
  bstack111l1llll1_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack111l1llll1_opy_(message=bstack11ll_opy_ (u"ࠨ༙ࠩ"), bstack11ll1lll1_opy_ = False):
  global CONFIG
  bstack111l1l11ll_opy_ = bstack11ll_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡇࡻࡧࡪࡶࡴࡪࡱࡱࠫ༚") if bstack11ll1lll1_opy_ else bstack11ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ༛")
  try:
    if message:
      bstack1l1l1ll1l1_opy_ = {
        bstack111l1l11ll_opy_ : str(message)
      }
      bstack1l1llll1l_opy_(bstack1l11l1l111_opy_, CONFIG, bstack1l1l1ll1l1_opy_)
    else:
      bstack1l1llll1l_opy_(bstack1l11l1l111_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack11l11llll_opy_.format(str(e)))
def bstack1l11ll1ll1_opy_(bstack1l11l11111_opy_, size):
  bstack1l1l1ll111_opy_ = []
  while len(bstack1l11l11111_opy_) > size:
    bstack1l11lll1ll_opy_ = bstack1l11l11111_opy_[:size]
    bstack1l1l1ll111_opy_.append(bstack1l11lll1ll_opy_)
    bstack1l11l11111_opy_ = bstack1l11l11111_opy_[size:]
  bstack1l1l1ll111_opy_.append(bstack1l11l11111_opy_)
  return bstack1l1l1ll111_opy_
def bstack111111l11_opy_(args):
  if bstack11ll_opy_ (u"ࠫ࠲ࡳࠧ༜") in args and bstack11ll_opy_ (u"ࠬࡶࡤࡣࠩ༝") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack11l1l1lll1_opy_, stage=STAGE.bstack1l1lll1lll_opy_)
def run_on_browserstack(bstack1l1111ll1l_opy_=None, bstack11l1111lll_opy_=None, bstack11ll11l1l_opy_=False):
  global CONFIG
  global bstack1lllll1l11_opy_
  global bstack1l111ll1l1_opy_
  global bstack1111l1ll11_opy_
  global bstack1111l111_opy_
  bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"࠭ࠧ༞")
  bstack1ll111l1l1_opy_(bstack11111l11l1_opy_, logger)
  if bstack1l1111ll1l_opy_ and isinstance(bstack1l1111ll1l_opy_, str):
    bstack1l1111ll1l_opy_ = eval(bstack1l1111ll1l_opy_)
  if bstack1l1111ll1l_opy_:
    CONFIG = bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧ༟")]
    bstack1lllll1l11_opy_ = bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩ༠")]
    bstack1l111ll1l1_opy_ = bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ༡")]
    bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ༢"), bstack1l111ll1l1_opy_)
    bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༣")
  bstack1111l111_opy_.set_property(bstack11ll_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ༤"), uuid4().__str__())
  logger.info(bstack11ll_opy_ (u"࠭ࡓࡅࡍࠣࡶࡺࡴࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡩࡥ࠼ࠣࠫ༥") + bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ༦")));
  logger.debug(bstack11ll_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࡀࠫ༧") + bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ༨")))
  if not bstack11ll11l1l_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack111ll11ll1_opy_)
      return
    if sys.argv[1] == bstack11ll_opy_ (u"ࠪ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ࠭༩") or sys.argv[1] == bstack11ll_opy_ (u"ࠫ࠲ࡼࠧ༪"):
      logger.info(bstack11ll_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡕࡿࡴࡩࡱࡱࠤࡘࡊࡋࠡࡸࡾࢁࠬ༫").format(__version__))
      return
    if sys.argv[1] == bstack11ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ༬"):
      bstack11l11lllll_opy_()
      return
  args = sys.argv
  bstack111ll1ll1_opy_()
  global bstack1lllll111l_opy_
  global bstack1111l11111_opy_
  global bstack11l111ll1l_opy_
  global bstack111111lll_opy_
  global bstack1llll1111l_opy_
  global bstack111l1l11l_opy_
  global bstack11lll1lll_opy_
  global bstack11llll1l1_opy_
  global bstack1l11llllll_opy_
  global bstack1lllllll11_opy_
  global bstack1l1llllll_opy_
  bstack1111l11111_opy_ = len(CONFIG.get(bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ༭"), []))
  if not bstack1l11ll1l1l_opy_:
    if args[1] == bstack11ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ༮") or args[1] == bstack11ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ༯"):
      bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༰")
      args = args[2:]
    elif args[1] == bstack11ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༱"):
      bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༲")
      args = args[2:]
    elif args[1] == bstack11ll_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ༳"):
      bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭༴")
      args = args[2:]
    elif args[1] == bstack11ll_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭༵ࠩ"):
      bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ༶")
      args = args[2:]
    elif args[1] == bstack11ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶ༷ࠪ"):
      bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༸")
      args = args[2:]
    elif args[1] == bstack11ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩ༹ࠬ"):
      bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭༺")
      args = args[2:]
    else:
      if not bstack11ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༻") in CONFIG or str(CONFIG[bstack11ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ༼")]).lower() in [bstack11ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༽"), bstack11ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫ༾")]:
        bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༿")
        args = args[1:]
      elif str(CONFIG[bstack11ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨཀ")]).lower() == bstack11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬཁ"):
        bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ག")
        args = args[1:]
      elif str(CONFIG[bstack11ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫགྷ")]).lower() == bstack11ll_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨང"):
        bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩཅ")
        args = args[1:]
      elif str(CONFIG[bstack11ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧཆ")]).lower() == bstack11ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཇ"):
        bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭཈")
        args = args[1:]
      elif str(CONFIG[bstack11ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪཉ")]).lower() == bstack11ll_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨཊ"):
        bstack1l11ll1l1l_opy_ = bstack11ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩཋ")
        args = args[1:]
      else:
        os.environ[bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬཌ")] = bstack1l11ll1l1l_opy_
        bstack1ll111111l_opy_(bstack111l1l1111_opy_)
  os.environ[bstack11ll_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬཌྷ")] = bstack1l11ll1l1l_opy_
  bstack1111l1ll11_opy_ = bstack1l11ll1l1l_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1l1l111l1_opy_ = bstack1l111l1111_opy_[bstack11ll_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘ࠲ࡈࡄࡅࠩཎ")] if bstack1l11ll1l1l_opy_ == bstack11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ཏ") and bstack11l1llll1l_opy_() else bstack1l11ll1l1l_opy_
      bstack1111l11l11_opy_.invoke(Events.bstack1111lllll_opy_, bstack1ll1ll11ll_opy_(
        sdk_version=__version__,
        path_config=bstack1ll11ll1ll_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1l1l111l1_opy_,
        frameworks=[bstack1l1l111l1_opy_],
        framework_versions={
          bstack1l1l111l1_opy_: bstack1111l1111l_opy_(bstack11ll_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭ཐ") if bstack1l11ll1l1l_opy_ in [bstack11ll_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧད"), bstack11ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨདྷ"), bstack11ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫན")] else bstack1l11ll1l1l_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack11ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨཔ"), None):
        CONFIG[bstack11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢཕ")] = cli.config.get(bstack11ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣབ"), None)
    except Exception as e:
      bstack1111l11l11_opy_.invoke(Events.bstack1l1lllll1l_opy_, e.__traceback__, 1)
    if bstack1l111ll1l1_opy_:
      CONFIG[bstack11ll_opy_ (u"ࠢࡢࡲࡳࠦབྷ")] = cli.config[bstack11ll_opy_ (u"ࠣࡣࡳࡴࠧམ")]
      logger.info(bstack1lll1lll1l_opy_.format(CONFIG[bstack11ll_opy_ (u"ࠩࡤࡴࡵ࠭ཙ")]))
  else:
    bstack1111l11l11_opy_.clear()
  global bstack1l111l1ll1_opy_
  global bstack11lll1l11_opy_
  if bstack1l1111ll1l_opy_:
    try:
      bstack1l11111lll_opy_ = datetime.datetime.now()
      os.environ[bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬཚ")] = bstack1l11ll1l1l_opy_
      bstack1l1llll1l_opy_(bstack11ll11111l_opy_, CONFIG)
      cli.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡶࡨࡰࡥࡴࡦࡵࡷࡣࡦࡺࡴࡦ࡯ࡳࡸࡪࡪࠢཛ"), datetime.datetime.now() - bstack1l11111lll_opy_)
    except Exception as e:
      logger.debug(bstack111llllll_opy_.format(str(e)))
  global bstack11ll111l1_opy_
  global bstack1l111lllll_opy_
  global bstack1l1l11ll1l_opy_
  global bstack11lllllll_opy_
  global bstack1l1l11111l_opy_
  global bstack11l1111l1_opy_
  global bstack11l11l1l1_opy_
  global bstack111l111lll_opy_
  global bstack11llllll1_opy_
  global bstack111lll11l1_opy_
  global bstack1ll111111_opy_
  global bstack1l11ll11l_opy_
  global bstack111llll11_opy_
  global bstack1lll1l11ll_opy_
  global bstack11ll1l1111_opy_
  global bstack1l11ll1l11_opy_
  global bstack111l11l1l1_opy_
  global bstack11ll111lll_opy_
  global bstack1ll1111l1l_opy_
  global bstack1ll1l1l11l_opy_
  global bstack1l1ll111l1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11ll111l1_opy_ = webdriver.Remote.__init__
    bstack1l111lllll_opy_ = WebDriver.quit
    bstack1l11ll11l_opy_ = WebDriver.close
    bstack11ll1l1111_opy_ = WebDriver.get
    bstack1l1ll111l1_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1l111l1ll1_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1ll111l11_opy_
    bstack11lll1l11_opy_ = bstack1ll111l11_opy_()
  except Exception as e:
    pass
  try:
    global bstack1l1llll11_opy_
    from QWeb.keywords import browser
    bstack1l1llll11_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack11l1l1l1l1_opy_(CONFIG) and bstack11llll1l1l_opy_():
    if bstack11l11l11l1_opy_() < version.parse(bstack11l1l1l111_opy_):
      logger.error(bstack1111llllll_opy_.format(bstack11l11l11l1_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11ll_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ཛྷ")) and callable(getattr(RemoteConnection, bstack11ll_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧཝ"))):
          RemoteConnection._get_proxy_url = bstack11111ll11l_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack11111ll11l_opy_
      except Exception as e:
        logger.error(bstack11l1ll1ll1_opy_.format(str(e)))
  if not CONFIG.get(bstack11ll_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩཞ"), False) and not bstack1l1111ll1l_opy_:
    logger.info(bstack11ll1ll111_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack11ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬཟ") in CONFIG and str(CONFIG[bstack11ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭འ")]).lower() != bstack11ll_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩཡ"):
      bstack1lll11ll1l_opy_()
    elif bstack1l11ll1l1l_opy_ != bstack11ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫར") or (bstack1l11ll1l1l_opy_ == bstack11ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬལ") and not bstack1l1111ll1l_opy_):
      bstack1l1l111ll1_opy_()
  if (bstack1l11ll1l1l_opy_ in [bstack11ll_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬཤ"), bstack11ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ཥ"), bstack11ll_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩས")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack111lll111_opy_
        bstack11l1111l1_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack11llll1ll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1l1l11111l_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack111ll1ll1l_opy_ + str(e))
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack11llll1ll_opy_)
    if bstack1l11ll1l1l_opy_ != bstack11ll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪཧ"):
      bstack1l1l1l1111_opy_()
    bstack1l1l11ll1l_opy_ = Output.start_test
    bstack11lllllll_opy_ = Output.end_test
    bstack11l11l1l1_opy_ = TestStatus.__init__
    bstack11llllll1_opy_ = pabot._run
    bstack111lll11l1_opy_ = QueueItem.__init__
    bstack1ll111111_opy_ = pabot._create_command_for_execution
    bstack1ll1111l1l_opy_ = pabot._report_results
  if bstack1l11ll1l1l_opy_ == bstack11ll_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪཨ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack1l11111ll_opy_)
    bstack111llll11_opy_ = Runner.run_hook
    bstack1lll1l11ll_opy_ = Step.run
  if bstack1l11ll1l1l_opy_ == bstack11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫཀྵ"):
    try:
      from _pytest.config import Config
      bstack111l11l1l1_opy_ = Config.getoption
      from _pytest import runner
      bstack11ll111lll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1lll1l1ll_opy_)
    try:
      from pytest_bdd import reporting
      bstack1ll1l1l11l_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11ll_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡴࠦࡲࡶࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࡸ࠭ཪ"))
  try:
    framework_name = bstack11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬཫ") if bstack1l11ll1l1l_opy_ in [bstack11ll_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ཬ"), bstack11ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ཭"), bstack11ll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ཮")] else bstack111llll1ll_opy_(bstack1l11ll1l1l_opy_)
    bstack1l1l111l1l_opy_ = {
      bstack11ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࠫ཯"): bstack11ll_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭཰") if bstack1l11ll1l1l_opy_ == bstack11ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸཱࠬ") and bstack11l1llll1l_opy_() else framework_name,
      bstack11ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡹࡩࡷࡹࡩࡰࡰིࠪ"): bstack1111l1111l_opy_(framework_name),
      bstack11ll_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲཱིࠬ"): __version__,
      bstack11ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥུࠩ"): bstack1l11ll1l1l_opy_
    }
    if bstack1l11ll1l1l_opy_ in bstack1111ll111_opy_ + bstack1111l1l1l1_opy_:
      if bstack1111ll11_opy_.bstack111ll1ll11_opy_(CONFIG):
        if bstack11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴཱུࠩ") in CONFIG:
          os.environ[bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫྲྀ")] = os.getenv(bstack11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬཷ"), json.dumps(CONFIG[bstack11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬླྀ")]))
          CONFIG[bstack11ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ཹ")].pop(bstack11ll_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩེࠬ"), None)
          CONFIG[bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨཻ")].pop(bstack11ll_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ོࠧ"), None)
        bstack1l1l111l1l_opy_[bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ཽࠪ")] = {
          bstack11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩཾ"): bstack11ll_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧཿ"),
          bstack11ll_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴྀࠧ"): str(bstack11l11l11l1_opy_())
        }
    if bstack1l11ll1l1l_opy_ not in [bstack11ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨཱྀ")] and not cli.is_running():
      bstack111lll1ll1_opy_, bstack11lll1l11l_opy_ = bstack1l111l1l_opy_.launch(CONFIG, bstack1l1l111l1l_opy_)
      if bstack11lll1l11l_opy_.get(bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨྂ")) is not None and bstack1111ll11_opy_.bstack1111l1ll1l_opy_(CONFIG) is None:
        value = bstack11lll1l11l_opy_[bstack11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩྃ")].get(bstack11ll_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶ྄ࠫ"))
        if value is not None:
            CONFIG[bstack11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ྅")] = value
        else:
          logger.debug(bstack11ll_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡦࡤࡸࡦࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥ྆"))
  except Exception as e:
    logger.debug(bstack11111l11ll_opy_.format(bstack11ll_opy_ (u"࠭ࡔࡦࡵࡷࡌࡺࡨࠧ྇"), str(e)))
  if bstack1l11ll1l1l_opy_ == bstack11ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧྈ"):
    bstack11l111ll1l_opy_ = True
    if bstack1l1111ll1l_opy_ and bstack11ll11l1l_opy_:
      bstack111l1l11l_opy_ = CONFIG.get(bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬྉ"), {}).get(bstack11ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫྊ"))
      bstack11l1l11ll1_opy_(bstack11llll11l1_opy_)
    elif bstack1l1111ll1l_opy_:
      bstack111l1l11l_opy_ = CONFIG.get(bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧྋ"), {}).get(bstack11ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ྌ"))
      global bstack1111lll1l_opy_
      try:
        if bstack111111l11_opy_(bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྍ")]) and multiprocessing.current_process().name == bstack11ll_opy_ (u"࠭࠰ࠨྎ"):
          bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྏ")].remove(bstack11ll_opy_ (u"ࠨ࠯ࡰࠫྐ"))
          bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྑ")].remove(bstack11ll_opy_ (u"ࠪࡴࡩࡨࠧྒ"))
          bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྒྷ")] = bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྔ")][0]
          with open(bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྕ")], bstack11ll_opy_ (u"ࠧࡳࠩྖ")) as f:
            file_content = f.read()
          bstack111ll11111_opy_ = bstack11ll_opy_ (u"ࠣࠤࠥࡪࡷࡵ࡭ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡦ࡮ࠤ࡮ࡳࡰࡰࡴࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫࠻ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨࠬࢀࢃࠩ࠼ࠢࡩࡶࡴࡳࠠࡱࡦࡥࠤ࡮ࡳࡰࡰࡴࡷࠤࡕࡪࡢ࠼ࠢࡲ࡫ࡤࡪࡢࠡ࠿ࠣࡔࡩࡨ࠮ࡥࡱࡢࡦࡷ࡫ࡡ࡬࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡤࡦࡨࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰ࠮ࡳࡦ࡮ࡩ࠰ࠥࡧࡲࡨ࠮ࠣࡸࡪࡳࡰࡰࡴࡤࡶࡾࠦ࠽ࠡ࠲ࠬ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡸࡷࡿ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡣࡵ࡫ࠥࡃࠠࡴࡶࡵࠬ࡮ࡴࡴࠩࡣࡵ࡫࠮࠱࠱࠱ࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡧࡻࡧࡪࡶࡴࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡦࡹࠠࡦ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡴࡦࡹࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡯ࡨࡡࡧࡦ࠭ࡹࡥ࡭ࡨ࠯ࡥࡷ࡭ࠬࡵࡧࡰࡴࡴࡸࡡࡳࡻࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡑࡦࡥ࠲ࡩࡵ࡟ࡣࠢࡀࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡔࡩࡨ࠮ࡥࡱࡢࡦࡷ࡫ࡡ࡬ࠢࡀࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡔࡩࡨࠨࠪ࠰ࡶࡩࡹࡥࡴࡳࡣࡦࡩ࠭࠯࡜࡯ࠤࠥࠦྗ").format(str(bstack1l1111ll1l_opy_))
          bstack111l1l1l1l_opy_ = bstack111ll11111_opy_ + file_content
          bstack1l11l11l11_opy_ = bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ྘")] + bstack11ll_opy_ (u"ࠪࡣࡧࡹࡴࡢࡥ࡮ࡣࡹ࡫࡭ࡱ࠰ࡳࡽࠬྙ")
          with open(bstack1l11l11l11_opy_, bstack11ll_opy_ (u"ࠫࡼ࠭ྚ")):
            pass
          with open(bstack1l11l11l11_opy_, bstack11ll_opy_ (u"ࠧࡽࠫࠣྛ")) as f:
            f.write(bstack111l1l1l1l_opy_)
          import subprocess
          process_data = subprocess.run([bstack11ll_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࠨྜ"), bstack1l11l11l11_opy_])
          if os.path.exists(bstack1l11l11l11_opy_):
            os.unlink(bstack1l11l11l11_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack111111l11_opy_(bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྜྷ")]):
            bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྞ")].remove(bstack11ll_opy_ (u"ࠩ࠰ࡱࠬྟ"))
            bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྠ")].remove(bstack11ll_opy_ (u"ࠫࡵࡪࡢࠨྡ"))
            bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྡྷ")] = bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྣ")][0]
          bstack11l1l11ll1_opy_(bstack11llll11l1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྤ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11ll_opy_ (u"ࠨࡡࡢࡲࡦࡳࡥࡠࡡࠪྥ")] = bstack11ll_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫྦ")
          mod_globals[bstack11ll_opy_ (u"ࠪࡣࡤ࡬ࡩ࡭ࡧࡢࡣࠬྦྷ")] = os.path.abspath(bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྨ")])
          exec(open(bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྩ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11ll_opy_ (u"࠭ࡃࡢࡷࡪ࡬ࡹࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂ࠭ྪ").format(str(e)))
          for driver in bstack1111lll1l_opy_:
            bstack11l1111lll_opy_.append({
              bstack11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬྫ"): bstack1l1111ll1l_opy_[bstack11ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྫྷ")],
              bstack11ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨྭ"): str(e),
              bstack11ll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩྮ"): multiprocessing.current_process().name
            })
            bstack1ll1111111_opy_(driver, bstack11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫྯ"), bstack11ll_opy_ (u"࡙ࠧࡥࡴࡵ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣྰ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1111lll1l_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1l111ll1l1_opy_, CONFIG, logger)
      bstack111l1lllll_opy_()
      bstack1111lll11_opy_()
      percy.bstack111l11lll_opy_()
      bstack1lllll1ll_opy_ = {
        bstack11ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྱ"): args[0],
        bstack11ll_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧྲ"): CONFIG,
        bstack11ll_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩླ"): bstack1lllll1l11_opy_,
        bstack11ll_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫྴ"): bstack1l111ll1l1_opy_
      }
      if bstack11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྵ") in CONFIG:
        bstack1111ll11l1_opy_ = bstack11l1lll111_opy_(args, logger, CONFIG, bstack1ll1l1111_opy_, bstack1111l11111_opy_)
        bstack11llll1l1_opy_ = bstack1111ll11l1_opy_.bstack111l1lll_opy_(run_on_browserstack, bstack1lllll1ll_opy_, bstack111111l11_opy_(args))
      else:
        if bstack111111l11_opy_(args):
          bstack1lllll1ll_opy_[bstack11ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྶ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1lllll1ll_opy_,))
          test.start()
          test.join()
        else:
          bstack11l1l11ll1_opy_(bstack11llll11l1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11ll_opy_ (u"ࠬࡥ࡟࡯ࡣࡰࡩࡤࡥࠧྷ")] = bstack11ll_opy_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨྸ")
          mod_globals[bstack11ll_opy_ (u"ࠧࡠࡡࡩ࡭ࡱ࡫࡟ࡠࠩྐྵ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1l11ll1l1l_opy_ == bstack11ll_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧྺ") or bstack1l11ll1l1l_opy_ == bstack11ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨྻ"):
    percy.init(bstack1l111ll1l1_opy_, CONFIG, logger)
    percy.bstack111l11lll_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack11llll1ll_opy_)
    bstack111l1lllll_opy_()
    bstack11l1l11ll1_opy_(bstack11ll1ll1l1_opy_)
    if bstack1ll1l1111_opy_:
      bstack1l11ll1l1_opy_(bstack11ll1ll1l1_opy_, args)
      if bstack11ll_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨྼ") in args:
        i = args.index(bstack11ll_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ྽"))
        args.pop(i)
        args.pop(i)
      if bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ྾") not in CONFIG:
        CONFIG[bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ྿")] = [{}]
        bstack1111l11111_opy_ = 1
      if bstack1lllll111l_opy_ == 0:
        bstack1lllll111l_opy_ = 1
      args.insert(0, str(bstack1lllll111l_opy_))
      args.insert(0, str(bstack11ll_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬ࿀")))
    if bstack1l111l1l_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1l11l1l11_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1l1lll111l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11ll_opy_ (u"ࠣࡔࡒࡆࡔ࡚࡟ࡐࡒࡗࡍࡔࡔࡓࠣ࿁"),
        ).parse_args(bstack1l11l1l11_opy_)
        bstack1l1ll11ll1_opy_ = args.index(bstack1l11l1l11_opy_[0]) if len(bstack1l11l1l11_opy_) > 0 else len(args)
        args.insert(bstack1l1ll11ll1_opy_, str(bstack11ll_opy_ (u"ࠩ࠰࠱ࡱ࡯ࡳࡵࡧࡱࡩࡷ࠭࿂")))
        args.insert(bstack1l1ll11ll1_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡶࡴࡨ࡯ࡵࡡ࡯࡭ࡸࡺࡥ࡯ࡧࡵ࠲ࡵࡿࠧ࿃"))))
        if bstack111ll1ll_opy_.bstack111l1l1l_opy_(CONFIG):
          args.insert(bstack1l1ll11ll1_opy_, str(bstack11ll_opy_ (u"ࠫ࠲࠳࡬ࡪࡵࡷࡩࡳ࡫ࡲࠨ࿄")))
          args.insert(bstack1l1ll11ll1_opy_ + 1, str(bstack11ll_opy_ (u"ࠬࡘࡥࡵࡴࡼࡊࡦ࡯࡬ࡦࡦ࠽ࡿࢂ࠭࿅").format(bstack111ll1ll_opy_.bstack1111l1ll_opy_(CONFIG))))
        if bstack1lll1l1lll_opy_(os.environ.get(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑ࿆ࠫ"))) and str(os.environ.get(bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠫ࿇"), bstack11ll_opy_ (u"ࠨࡰࡸࡰࡱ࠭࿈"))) != bstack11ll_opy_ (u"ࠩࡱࡹࡱࡲࠧ࿉"):
          for bstack1111l1111_opy_ in bstack1l1lll111l_opy_:
            args.remove(bstack1111l1111_opy_)
          test_files = os.environ.get(bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧ࿊")).split(bstack11ll_opy_ (u"ࠫ࠱࠭࿋"))
          for bstack11ll1llll_opy_ in test_files:
            args.append(bstack11ll1llll_opy_)
      except Exception as e:
        logger.error(bstack11ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡥࡹࡺࡡࡤࡪ࡬ࡲ࡬ࠦ࡬ࡪࡵࡷࡩࡳ࡫ࡲࠡࡨࡲࡶࠥࢁࡽ࠯ࠢࡈࡶࡷࡵࡲࠡ࠯ࠣࡿࢂࠨ࿌").format(bstack1ll1l1ll11_opy_, e))
    pabot.main(args)
  elif bstack1l11ll1l1l_opy_ == bstack11ll_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ࿍"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack11llll1ll_opy_)
    for a in args:
      if bstack11ll_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭࿎") in a:
        bstack1llll1111l_opy_ = int(a.split(bstack11ll_opy_ (u"ࠨ࠼ࠪ࿏"))[1])
      if bstack11ll_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭࿐") in a:
        bstack111l1l11l_opy_ = str(a.split(bstack11ll_opy_ (u"ࠪ࠾ࠬ࿑"))[1])
      if bstack11ll_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫ࿒") in a:
        bstack11lll1lll_opy_ = str(a.split(bstack11ll_opy_ (u"ࠬࡀࠧ࿓"))[1])
    bstack111lllll11_opy_ = None
    if bstack11ll_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬ࿔") in args:
      i = args.index(bstack11ll_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭࿕"))
      args.pop(i)
      bstack111lllll11_opy_ = args.pop(i)
    if bstack111lllll11_opy_ is not None:
      global bstack11ll1l11ll_opy_
      bstack11ll1l11ll_opy_ = bstack111lllll11_opy_
    bstack11l1l11ll1_opy_(bstack11ll1ll1l1_opy_)
    run_cli(args)
    if bstack11ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬ࿖") in multiprocessing.current_process().__dict__.keys():
      for bstack1ll1ll1lll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11l1111lll_opy_.append(bstack1ll1ll1lll_opy_)
  elif bstack1l11ll1l1l_opy_ == bstack11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ࿗"):
    bstack11ll11lll1_opy_ = bstack1lll11lll_opy_(args, logger, CONFIG, bstack1ll1l1111_opy_)
    bstack11ll11lll1_opy_.bstack1llllll1l_opy_()
    bstack111l1lllll_opy_()
    bstack111111lll_opy_ = True
    bstack1lllllll11_opy_ = bstack11ll11lll1_opy_.bstack1lll1111l_opy_()
    bstack11ll11lll1_opy_.bstack1lllll1ll_opy_(bstack111l1lll1l_opy_)
    bstack11ll11lll1_opy_.bstack1llll1lll_opy_()
    bstack11l11l11ll_opy_(bstack1l11ll1l1l_opy_, CONFIG, bstack11ll11lll1_opy_.bstack1lll1lll1_opy_())
    bstack11l11ll1l_opy_ = bstack11ll11lll1_opy_.bstack111l1lll_opy_(bstack11ll1l111_opy_, {
      bstack11ll_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫ࿘"): bstack1lllll1l11_opy_,
      bstack11ll_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭࿙"): bstack1l111ll1l1_opy_,
      bstack11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ࿚"): bstack1ll1l1111_opy_
    })
    try:
      bstack1lll1ll11l_opy_, bstack11ll11ll1l_opy_ = map(list, zip(*bstack11l11ll1l_opy_))
      bstack1l11llllll_opy_ = bstack1lll1ll11l_opy_[0]
      for status_code in bstack11ll11ll1l_opy_:
        if status_code != 0:
          bstack1l1llllll_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡦࡴࡵࡳࡷࡹࠠࡢࡰࡧࠤࡸࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠰ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠺ࠡࡽࢀࠦ࿛").format(str(e)))
  elif bstack1l11ll1l1l_opy_ == bstack11ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ࿜"):
    try:
      from behave.__main__ import main as bstack111l11l11l_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack1l11111ll_opy_)
    bstack111l1lllll_opy_()
    bstack111111lll_opy_ = True
    bstack1llllll11_opy_ = 1
    if bstack11ll_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ࿝") in CONFIG:
      bstack1llllll11_opy_ = CONFIG[bstack11ll_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ࿞")]
    if bstack11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭࿟") in CONFIG:
      bstack1ll11111l1_opy_ = int(bstack1llllll11_opy_) * int(len(CONFIG[bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ࿠")]))
    else:
      bstack1ll11111l1_opy_ = int(bstack1llllll11_opy_)
    config = Configuration(args)
    bstack111l111ll_opy_ = config.paths
    if len(bstack111l111ll_opy_) == 0:
      import glob
      pattern = bstack11ll_opy_ (u"ࠬ࠰ࠪ࠰ࠬ࠱ࡪࡪࡧࡴࡶࡴࡨࠫ࿡")
      bstack1l1l1l11l1_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1l1l1l11l1_opy_)
      config = Configuration(args)
      bstack111l111ll_opy_ = config.paths
    bstack111ll111_opy_ = [os.path.normpath(item) for item in bstack111l111ll_opy_]
    bstack1l1111l1l1_opy_ = [os.path.normpath(item) for item in args]
    bstack11111lll1l_opy_ = [item for item in bstack1l1111l1l1_opy_ if item not in bstack111ll111_opy_]
    import platform as pf
    if pf.system().lower() == bstack11ll_opy_ (u"࠭ࡷࡪࡰࡧࡳࡼࡹࠧ࿢"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack111ll111_opy_ = [str(PurePosixPath(PureWindowsPath(bstack111111l11l_opy_)))
                    for bstack111111l11l_opy_ in bstack111ll111_opy_]
    bstack1lll1ll11_opy_ = []
    for spec in bstack111ll111_opy_:
      bstack1lllll1l1_opy_ = []
      bstack1lllll1l1_opy_ += bstack11111lll1l_opy_
      bstack1lllll1l1_opy_.append(spec)
      bstack1lll1ll11_opy_.append(bstack1lllll1l1_opy_)
    execution_items = []
    for bstack1lllll1l1_opy_ in bstack1lll1ll11_opy_:
      if bstack11ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿣") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ࿤")]):
          item = {}
          item[bstack11ll_opy_ (u"ࠩࡤࡶ࡬࠭࿥")] = bstack11ll_opy_ (u"ࠪࠤࠬ࿦").join(bstack1lllll1l1_opy_)
          item[bstack11ll_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ࿧")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack11ll_opy_ (u"ࠬࡧࡲࡨࠩ࿨")] = bstack11ll_opy_ (u"࠭ࠠࠨ࿩").join(bstack1lllll1l1_opy_)
        item[bstack11ll_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭࿪")] = 0
        execution_items.append(item)
    bstack1ll1l11ll_opy_ = bstack1l11ll1ll1_opy_(execution_items, bstack1ll11111l1_opy_)
    for execution_item in bstack1ll1l11ll_opy_:
      bstack1111lll1_opy_ = []
      for item in execution_item:
        bstack1111lll1_opy_.append(bstack11111l1l1_opy_(name=str(item[bstack11ll_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ࿫")]),
                                             target=bstack1l1l1l11l_opy_,
                                             args=(item[bstack11ll_opy_ (u"ࠩࡤࡶ࡬࠭࿬")],)))
      for t in bstack1111lll1_opy_:
        t.start()
      for t in bstack1111lll1_opy_:
        t.join()
  else:
    bstack1ll111111l_opy_(bstack111l1l1111_opy_)
  if not bstack1l1111ll1l_opy_:
    bstack111ll1l1l1_opy_()
    if(bstack1l11ll1l1l_opy_ in [bstack11ll_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ࿭"), bstack11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ࿮")]):
      bstack1111l1lll1_opy_()
  bstack11l1l1l1ll_opy_.bstack111lll11ll_opy_()
def browserstack_initialize(bstack11111l11l_opy_=None):
  logger.info(bstack11ll_opy_ (u"ࠬࡘࡵ࡯ࡰ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡻ࡮ࡺࡨࠡࡣࡵ࡫ࡸࡀࠠࠨ࿯") + str(bstack11111l11l_opy_))
  run_on_browserstack(bstack11111l11l_opy_, None, True)
@measure(event_name=EVENTS.bstack1llllllll1_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack111ll1l1l1_opy_():
  global CONFIG
  global bstack1111l1ll11_opy_
  global bstack1l1llllll_opy_
  global bstack1llll1llll_opy_
  global bstack1111l111_opy_
  bstack1l111l111_opy_.bstack11llll1lll_opy_()
  if cli.is_running():
    bstack1111l11l11_opy_.invoke(Events.bstack1l111l1l11_opy_)
  else:
    bstack11111lll_opy_ = bstack111ll1ll_opy_.bstack11111ll1_opy_(config=CONFIG)
    bstack11111lll_opy_.bstack111lll1l11_opy_(CONFIG)
  if bstack1111l1ll11_opy_ == bstack11ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭࿰"):
    if not cli.is_enabled(CONFIG):
      bstack1l111l1l_opy_.stop()
  else:
    bstack1l111l1l_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1l1l111l_opy_.bstack1111l1ll1_opy_()
  if bstack11ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ࿱") in CONFIG and str(CONFIG[bstack11ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ࿲")]).lower() != bstack11ll_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ࿳"):
    hashed_id, bstack1l1lll1ll1_opy_ = bstack1l1l1l111_opy_()
  else:
    hashed_id, bstack1l1lll1ll1_opy_ = get_build_link()
  bstack1111ll111l_opy_(hashed_id)
  logger.info(bstack11ll_opy_ (u"ࠪࡗࡉࡑࠠࡳࡷࡱࠤࡪࡴࡤࡦࡦࠣࡪࡴࡸࠠࡪࡦ࠽ࠫ࿴") + bstack1111l111_opy_.get_property(bstack11ll_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭࿵"), bstack11ll_opy_ (u"ࠬ࠭࿶")) + bstack11ll_opy_ (u"࠭ࠬࠡࡶࡨࡷࡹ࡮ࡵࡣࠢ࡬ࡨ࠿ࠦࠧ࿷") + os.getenv(bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ࿸"), bstack11ll_opy_ (u"ࠨࠩ࿹")))
  if hashed_id is not None and bstack11ll1lll11_opy_() != -1:
    sessions = bstack11l111llll_opy_(hashed_id)
    bstack1ll11l11l1_opy_(sessions, bstack1l1lll1ll1_opy_)
  if bstack1111l1ll11_opy_ == bstack11ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ࿺") and bstack1l1llllll_opy_ != 0:
    sys.exit(bstack1l1llllll_opy_)
  if bstack1111l1ll11_opy_ == bstack11ll_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ࿻") and bstack1llll1llll_opy_ != 0:
    sys.exit(bstack1llll1llll_opy_)
def bstack1111ll111l_opy_(new_id):
    global bstack1l11l1lll_opy_
    bstack1l11l1lll_opy_ = new_id
def bstack111llll1ll_opy_(bstack1l1l11l1ll_opy_):
  if bstack1l1l11l1ll_opy_:
    return bstack1l1l11l1ll_opy_.capitalize()
  else:
    return bstack11ll_opy_ (u"ࠫࠬ࿼")
@measure(event_name=EVENTS.bstack111l1l11l1_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack1ll1ll111_opy_(bstack11lll111ll_opy_):
  if bstack11ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ࿽") in bstack11lll111ll_opy_ and bstack11lll111ll_opy_[bstack11ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ࿾")] != bstack11ll_opy_ (u"ࠧࠨ࿿"):
    return bstack11lll111ll_opy_[bstack11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭က")]
  else:
    bstack111l111l1l_opy_ = bstack11ll_opy_ (u"ࠤࠥခ")
    if bstack11ll_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪဂ") in bstack11lll111ll_opy_ and bstack11lll111ll_opy_[bstack11ll_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫဃ")] != None:
      bstack111l111l1l_opy_ += bstack11lll111ll_opy_[bstack11ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬင")] + bstack11ll_opy_ (u"ࠨࠬࠡࠤစ")
      if bstack11lll111ll_opy_[bstack11ll_opy_ (u"ࠧࡰࡵࠪဆ")] == bstack11ll_opy_ (u"ࠣ࡫ࡲࡷࠧဇ"):
        bstack111l111l1l_opy_ += bstack11ll_opy_ (u"ࠤ࡬ࡓࡘࠦࠢဈ")
      bstack111l111l1l_opy_ += (bstack11lll111ll_opy_[bstack11ll_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧဉ")] or bstack11ll_opy_ (u"ࠫࠬည"))
      return bstack111l111l1l_opy_
    else:
      bstack111l111l1l_opy_ += bstack111llll1ll_opy_(bstack11lll111ll_opy_[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ဋ")]) + bstack11ll_opy_ (u"ࠨࠠࠣဌ") + (
              bstack11lll111ll_opy_[bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩဍ")] or bstack11ll_opy_ (u"ࠨࠩဎ")) + bstack11ll_opy_ (u"ࠤ࠯ࠤࠧဏ")
      if bstack11lll111ll_opy_[bstack11ll_opy_ (u"ࠪࡳࡸ࠭တ")] == bstack11ll_opy_ (u"ࠦ࡜࡯࡮ࡥࡱࡺࡷࠧထ"):
        bstack111l111l1l_opy_ += bstack11ll_opy_ (u"ࠧ࡝ࡩ࡯ࠢࠥဒ")
      bstack111l111l1l_opy_ += bstack11lll111ll_opy_[bstack11ll_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪဓ")] or bstack11ll_opy_ (u"ࠧࠨန")
      return bstack111l111l1l_opy_
@measure(event_name=EVENTS.bstack11ll1ll11l_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack1l1l11l11_opy_(bstack111l111l11_opy_):
  if bstack111l111l11_opy_ == bstack11ll_opy_ (u"ࠣࡦࡲࡲࡪࠨပ"):
    return bstack11ll_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬဖ")
  elif bstack111l111l11_opy_ == bstack11ll_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥဗ"):
    return bstack11ll_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡉࡥ࡮ࡲࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧဘ")
  elif bstack111l111l11_opy_ == bstack11ll_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧမ"):
    return bstack11ll_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡩࡵࡩࡪࡴ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡩࡵࡩࡪࡴࠢ࠿ࡒࡤࡷࡸ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ယ")
  elif bstack111l111l11_opy_ == bstack11ll_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨရ"):
    return bstack11ll_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡶࡪࡪ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡴࡨࡨࠧࡄࡅࡳࡴࡲࡶࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪလ")
  elif bstack111l111l11_opy_ == bstack11ll_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥဝ"):
    return bstack11ll_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࠩࡥࡦࡣ࠶࠶࠻ࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࠤࡧࡨࡥ࠸࠸࠶ࠣࡀࡗ࡭ࡲ࡫࡯ࡶࡶ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨသ")
  elif bstack111l111l11_opy_ == bstack11ll_opy_ (u"ࠦࡷࡻ࡮࡯࡫ࡱ࡫ࠧဟ"):
    return bstack11ll_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࡓࡷࡱࡲ࡮ࡴࡧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ဠ")
  else:
    return bstack11ll_opy_ (u"࠭࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࠪအ") + bstack111llll1ll_opy_(
      bstack111l111l11_opy_) + bstack11ll_opy_ (u"ࠧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ဢ")
def bstack111l1l111_opy_(session):
  return bstack11ll_opy_ (u"ࠨ࠾ࡷࡶࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡸ࡯ࡸࠤࡁࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠥࡹࡥࡴࡵ࡬ࡳࡳ࠳࡮ࡢ࡯ࡨࠦࡃࡂࡡࠡࡪࡵࡩ࡫ࡃࠢࡼࡿࠥࠤࡹࡧࡲࡨࡧࡷࡁࠧࡥࡢ࡭ࡣࡱ࡯ࠧࡄࡻࡾ࠾࠲ࡥࡃࡂ࠯ࡵࡦࡁࡿࢂࢁࡽ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿࠳ࡹࡸ࠾ࠨဣ").format(
    session[bstack11ll_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭ဤ")], bstack1ll1ll111_opy_(session), bstack1l1l11l11_opy_(session[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠩဥ")]),
    bstack1l1l11l11_opy_(session[bstack11ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫဦ")]),
    bstack111llll1ll_opy_(session[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ဧ")] or session[bstack11ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ဨ")] or bstack11ll_opy_ (u"ࠧࠨဩ")) + bstack11ll_opy_ (u"ࠣࠢࠥဪ") + (session[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫါ")] or bstack11ll_opy_ (u"ࠪࠫာ")),
    session[bstack11ll_opy_ (u"ࠫࡴࡹࠧိ")] + bstack11ll_opy_ (u"ࠧࠦࠢီ") + session[bstack11ll_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪု")], session[bstack11ll_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩူ")] or bstack11ll_opy_ (u"ࠨࠩေ"),
    session[bstack11ll_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭ဲ")] if session[bstack11ll_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧဳ")] else bstack11ll_opy_ (u"ࠫࠬဴ"))
@measure(event_name=EVENTS.bstack1ll11111ll_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def bstack1ll11l11l1_opy_(sessions, bstack1l1lll1ll1_opy_):
  try:
    bstack111l11111l_opy_ = bstack11ll_opy_ (u"ࠧࠨဵ")
    if not os.path.exists(bstack11ll1l1ll_opy_):
      os.mkdir(bstack11ll1l1ll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11ll_opy_ (u"࠭ࡡࡴࡵࡨࡸࡸ࠵ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ࠫံ")), bstack11ll_opy_ (u"ࠧࡳ့ࠩ")) as f:
      bstack111l11111l_opy_ = f.read()
    bstack111l11111l_opy_ = bstack111l11111l_opy_.replace(bstack11ll_opy_ (u"ࠨࡽࠨࡖࡊ࡙ࡕࡍࡖࡖࡣࡈࡕࡕࡏࡖࠨࢁࠬး"), str(len(sessions)))
    bstack111l11111l_opy_ = bstack111l11111l_opy_.replace(bstack11ll_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠥࡾ္ࠩ"), bstack1l1lll1ll1_opy_)
    bstack111l11111l_opy_ = bstack111l11111l_opy_.replace(bstack11ll_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣࡓࡇࡍࡆࠧࢀ်ࠫ"),
                                              sessions[0].get(bstack11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡲࡦࡳࡥࠨျ")) if sessions[0] else bstack11ll_opy_ (u"ࠬ࠭ြ"))
    with open(os.path.join(bstack11ll1l1ll_opy_, bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪွ")), bstack11ll_opy_ (u"ࠧࡸࠩှ")) as stream:
      stream.write(bstack111l11111l_opy_.split(bstack11ll_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁࠬဿ"))[0])
      for session in sessions:
        stream.write(bstack111l1l111_opy_(session))
      stream.write(bstack111l11111l_opy_.split(bstack11ll_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂ࠭၀"))[1])
    logger.info(bstack11ll_opy_ (u"ࠪࡋࡪࡴࡥࡳࡣࡷࡩࡩࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡨࡵࡪ࡮ࡧࠤࡦࡸࡴࡪࡨࡤࡧࡹࡹࠠࡢࡶࠣࡿࢂ࠭၁").format(bstack11ll1l1ll_opy_));
  except Exception as e:
    logger.debug(bstack11l1ll1l11_opy_.format(str(e)))
def bstack11l111llll_opy_(hashed_id):
  global CONFIG
  try:
    bstack1l11111lll_opy_ = datetime.datetime.now()
    host = bstack11ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠯ࡦࡰࡴࡻࡤ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ၂") if bstack11ll_opy_ (u"ࠬࡧࡰࡱࠩ၃") in CONFIG else bstack11ll_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧ၄")
    user = CONFIG[bstack11ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ၅")]
    key = CONFIG[bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ၆")]
    bstack111l1111l_opy_ = bstack11ll_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨ၇") if bstack11ll_opy_ (u"ࠪࡥࡵࡶࠧ၈") in CONFIG else (bstack11ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨ၉") if CONFIG.get(bstack11ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ၊")) else bstack11ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ။"))
    host = bstack111ll111l1_opy_(cli.config, [bstack11ll_opy_ (u"ࠢࡢࡲ࡬ࡷࠧ၌"), bstack11ll_opy_ (u"ࠣࡣࡳࡴࡆࡻࡴࡰ࡯ࡤࡸࡪࠨ၍"), bstack11ll_opy_ (u"ࠤࡤࡴ࡮ࠨ၎")], host) if bstack11ll_opy_ (u"ࠪࡥࡵࡶࠧ၏") in CONFIG else bstack111ll111l1_opy_(cli.config, [bstack11ll_opy_ (u"ࠦࡦࡶࡩࡴࠤၐ"), bstack11ll_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢၑ"), bstack11ll_opy_ (u"ࠨࡡࡱ࡫ࠥၒ")], host)
    url = bstack11ll_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡶࡩࡸࡹࡩࡰࡰࡶ࠲࡯ࡹ࡯࡯ࠩၓ").format(host, bstack111l1111l_opy_, hashed_id)
    headers = {
      bstack11ll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧၔ"): bstack11ll_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬၕ"),
    }
    proxies = bstack1l1lll1l1l_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡩࡨࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡹ࡟࡭࡫ࡶࡸࠧၖ"), datetime.datetime.now() - bstack1l11111lll_opy_)
      return list(map(lambda session: session[bstack11ll_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩၗ")], response.json()))
  except Exception as e:
    logger.debug(bstack1llll1l11l_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack1l111l1l1_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def get_build_link():
  global CONFIG
  global bstack1l11l1lll_opy_
  try:
    if bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨၘ") in CONFIG:
      bstack1l11111lll_opy_ = datetime.datetime.now()
      host = bstack11ll_opy_ (u"࠭ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥࠩၙ") if bstack11ll_opy_ (u"ࠧࡢࡲࡳࠫၚ") in CONFIG else bstack11ll_opy_ (u"ࠨࡣࡳ࡭ࠬၛ")
      user = CONFIG[bstack11ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫၜ")]
      key = CONFIG[bstack11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ၝ")]
      bstack111l1111l_opy_ = bstack11ll_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪၞ") if bstack11ll_opy_ (u"ࠬࡧࡰࡱࠩၟ") in CONFIG else bstack11ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨၠ")
      url = bstack11ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠰࡭ࡷࡴࡴࠧၡ").format(user, key, host, bstack111l1111l_opy_)
      if cli.is_enabled(CONFIG):
        bstack1l1lll1ll1_opy_, hashed_id = cli.bstack11l11l1lll_opy_()
        logger.info(bstack1l11lll1l1_opy_.format(bstack1l1lll1ll1_opy_))
        return [hashed_id, bstack1l1lll1ll1_opy_]
      else:
        headers = {
          bstack11ll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧၢ"): bstack11ll_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬၣ"),
        }
        if bstack11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬၤ") in CONFIG:
          params = {bstack11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩၥ"): CONFIG[bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨၦ")], bstack11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩၧ"): CONFIG[bstack11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩၨ")]}
        else:
          params = {bstack11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ၩ"): CONFIG[bstack11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬၪ")]}
        proxies = bstack1l1lll1l1l_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack1l11lll1l_opy_ = response.json()[0][bstack11ll_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡣࡷ࡬ࡰࡩ࠭ၫ")]
          if bstack1l11lll1l_opy_:
            bstack1l1lll1ll1_opy_ = bstack1l11lll1l_opy_[bstack11ll_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨၬ")].split(bstack11ll_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧ࠲ࡨࡵࡪ࡮ࡧࠫၭ"))[0] + bstack11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡸ࠵ࠧၮ") + bstack1l11lll1l_opy_[
              bstack11ll_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪၯ")]
            logger.info(bstack1l11lll1l1_opy_.format(bstack1l1lll1ll1_opy_))
            bstack1l11l1lll_opy_ = bstack1l11lll1l_opy_[bstack11ll_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫၰ")]
            bstack11ll1lll1l_opy_ = CONFIG[bstack11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬၱ")]
            if bstack11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬၲ") in CONFIG:
              bstack11ll1lll1l_opy_ += bstack11ll_opy_ (u"ࠫࠥ࠭ၳ") + CONFIG[bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧၴ")]
            if bstack11ll1lll1l_opy_ != bstack1l11lll1l_opy_[bstack11ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫၵ")]:
              logger.debug(bstack1lllllll1l_opy_.format(bstack1l11lll1l_opy_[bstack11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬၶ")], bstack11ll1lll1l_opy_))
            cli.bstack1llllll11l_opy_(bstack11ll_opy_ (u"ࠣࡪࡷࡸࡵࡀࡧࡦࡶࡢࡦࡺ࡯࡬ࡥࡡ࡯࡭ࡳࡱࠢၷ"), datetime.datetime.now() - bstack1l11111lll_opy_)
            return [bstack1l11lll1l_opy_[bstack11ll_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬၸ")], bstack1l1lll1ll1_opy_]
    else:
      logger.warn(bstack111l1l1ll_opy_)
  except Exception as e:
    logger.debug(bstack11ll11l1l1_opy_.format(str(e)))
  return [None, None]
def bstack1111l1lll_opy_(url, bstack111l11lll1_opy_=False):
  global CONFIG
  global bstack1llll111ll_opy_
  if not bstack1llll111ll_opy_:
    hostname = bstack11lll11l1_opy_(url)
    is_private = bstack11llll11ll_opy_(hostname)
    if (bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧၹ") in CONFIG and not bstack1lll1l1lll_opy_(CONFIG[bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨၺ")])) and (is_private or bstack111l11lll1_opy_):
      bstack1llll111ll_opy_ = hostname
def bstack11lll11l1_opy_(url):
  return urlparse(url).hostname
def bstack11llll11ll_opy_(hostname):
  for bstack1l111ll11l_opy_ in bstack1ll111ll1l_opy_:
    regex = re.compile(bstack1l111ll11l_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1lll1111l1_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1111l11ll1_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1llll1111l_opy_
  bstack1lll11l11l_opy_ = not (bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၻ"), None) and bstack1l1l11l1_opy_(
          threading.current_thread(), bstack11ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၼ"), None))
  bstack1111lll1ll_opy_ = getattr(driver, bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧၽ"), None) != True
  bstack111ll1lll1_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၾ"), None) and bstack1l1l11l1_opy_(
          threading.current_thread(), bstack11ll_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၿ"), None)
  if bstack111ll1lll1_opy_:
    if not bstack111ll1l111_opy_():
      logger.warning(bstack11ll_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸ࠴ࠢႀ"))
      return {}
    logger.debug(bstack11ll_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨႁ"))
    logger.debug(perform_scan(driver, driver_command=bstack11ll_opy_ (u"ࠬ࡫ࡸࡦࡥࡸࡸࡪ࡙ࡣࡳ࡫ࡳࡸࠬႂ")))
    results = bstack111l1ll1l1_opy_(bstack11ll_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹࡹࠢႃ"))
    if results is not None and results.get(bstack11ll_opy_ (u"ࠢࡪࡵࡶࡹࡪࡹࠢႄ")) is not None:
        return results[bstack11ll_opy_ (u"ࠣ࡫ࡶࡷࡺ࡫ࡳࠣႅ")]
    logger.error(bstack11ll_opy_ (u"ࠤࡑࡳࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡘࡥࡴࡷ࡯ࡸࡸࠦࡷࡦࡴࡨࠤ࡫ࡵࡵ࡯ࡦ࠱ࠦႆ"))
    return []
  if not bstack1111ll11_opy_.bstack1ll11l1ll_opy_(CONFIG, bstack1llll1111l_opy_) or (bstack1111lll1ll_opy_ and bstack1lll11l11l_opy_):
    logger.warning(bstack11ll_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷ࠳ࠨႇ"))
    return {}
  try:
    logger.debug(bstack11ll_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨႈ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1l1l1l1l1_opy_.bstack1l1l11l111_opy_)
    return results
  except Exception:
    logger.error(bstack11ll_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡺࡩࡷ࡫ࠠࡧࡱࡸࡲࡩ࠴ࠢႉ"))
    return {}
@measure(event_name=EVENTS.bstack11lll1ll11_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1llll1111l_opy_
  bstack1lll11l11l_opy_ = not (bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪႊ"), None) and bstack1l1l11l1_opy_(
          threading.current_thread(), bstack11ll_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ႋ"), None))
  bstack1111lll1ll_opy_ = getattr(driver, bstack11ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨႌ"), None) != True
  bstack111ll1lll1_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵႍࠩ"), None) and bstack1l1l11l1_opy_(
          threading.current_thread(), bstack11ll_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬႎ"), None)
  if bstack111ll1lll1_opy_:
    if not bstack111ll1l111_opy_():
      logger.warning(bstack11ll_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹ࠯ࠤႏ"))
      return {}
    logger.debug(bstack11ll_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻࠪ႐"))
    logger.debug(perform_scan(driver, driver_command=bstack11ll_opy_ (u"࠭ࡥࡹࡧࡦࡹࡹ࡫ࡓࡤࡴ࡬ࡴࡹ࠭႑")))
    results = bstack111l1ll1l1_opy_(bstack11ll_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡓࡶ࡯ࡰࡥࡷࡿࠢ႒"))
    if results is not None and results.get(bstack11ll_opy_ (u"ࠣࡵࡸࡱࡲࡧࡲࡺࠤ႓")) is not None:
        return results[bstack11ll_opy_ (u"ࠤࡶࡹࡲࡳࡡࡳࡻࠥ႔")]
    logger.error(bstack11ll_opy_ (u"ࠥࡒࡴࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡒࡦࡵࡸࡰࡹࡹࠠࡔࡷࡰࡱࡦࡸࡹࠡࡹࡤࡷࠥ࡬࡯ࡶࡰࡧ࠲ࠧ႕"))
    return {}
  if not bstack1111ll11_opy_.bstack1ll11l1ll_opy_(CONFIG, bstack1llll1111l_opy_) or (bstack1111lll1ll_opy_ and bstack1lll11l11l_opy_):
    logger.warning(bstack11ll_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡳࡶ࡯ࡰࡥࡷࡿ࠮ࠣ႖"))
    return {}
  try:
    logger.debug(bstack11ll_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻࠪ႗"))
    logger.debug(perform_scan(driver))
    bstack1l1l1ll11_opy_ = driver.execute_async_script(bstack1l1l1l1l1_opy_.bstack1ll111ll11_opy_)
    return bstack1l1l1ll11_opy_
  except Exception:
    logger.error(bstack11ll_opy_ (u"ࠨࡎࡰࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡹࡲࡳࡡࡳࡻࠣࡻࡦࡹࠠࡧࡱࡸࡲࡩ࠴ࠢ႘"))
    return {}
def bstack111ll1l111_opy_():
  global CONFIG
  global bstack1llll1111l_opy_
  bstack111l1l1l1_opy_ = bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ႙"), None) and bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪႚ"), None)
  if not bstack1111ll11_opy_.bstack1ll11l1ll_opy_(CONFIG, bstack1llll1111l_opy_) or not bstack111l1l1l1_opy_:
        logger.warning(bstack11ll_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤႛ"))
        return False
  return True
def bstack111l1ll1l1_opy_(bstack11lllll1ll_opy_):
    bstack1l11lllll_opy_ = bstack1l111l1l_opy_.current_test_uuid() if bstack1l111l1l_opy_.current_test_uuid() else bstack1l1l111l_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack1l111llll_opy_(bstack1l11lllll_opy_, bstack11lllll1ll_opy_))
        try:
            return future.result(timeout=bstack1l11ll11ll_opy_)
        except TimeoutError:
            logger.error(bstack11ll_opy_ (u"ࠥࡘ࡮ࡳࡥࡰࡷࡷࠤࡦ࡬ࡴࡦࡴࠣࡿࢂࡹࠠࡸࡪ࡬ࡰࡪࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡔࡨࡷࡺࡲࡴࡴࠤႜ").format(bstack1l11ll11ll_opy_))
        except Exception as ex:
            logger.debug(bstack11ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡶࡪࡺࡲࡪࡧࡹ࡭ࡳ࡭ࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡽࢀ࠲ࠥࡋࡲࡳࡱࡵࠤ࠲ࠦࡻࡾࠤႝ").format(bstack11lllll1ll_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack1111lll11l_opy_, stage=STAGE.bstack1ll1111l1_opy_, bstack111l111l1l_opy_=bstack1111llll1_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1llll1111l_opy_
  bstack1lll11l11l_opy_ = not (bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ႞"), None) and bstack1l1l11l1_opy_(
          threading.current_thread(), bstack11ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ႟"), None))
  bstack1ll11l1l1l_opy_ = not (bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧႠ"), None) and bstack1l1l11l1_opy_(
          threading.current_thread(), bstack11ll_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪႡ"), None))
  bstack1111lll1ll_opy_ = getattr(driver, bstack11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩႢ"), None) != True
  if not bstack1111ll11_opy_.bstack1ll11l1ll_opy_(CONFIG, bstack1llll1111l_opy_) or (bstack1111lll1ll_opy_ and bstack1lll11l11l_opy_ and bstack1ll11l1l1l_opy_):
    logger.warning(bstack11ll_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡹࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡤࡣࡱ࠲ࠧႣ"))
    return {}
  try:
    bstack1l1ll1lll1_opy_ = bstack11ll_opy_ (u"ࠫࡦࡶࡰࠨႤ") in CONFIG and CONFIG.get(bstack11ll_opy_ (u"ࠬࡧࡰࡱࠩႥ"), bstack11ll_opy_ (u"࠭ࠧႦ"))
    session_id = getattr(driver, bstack11ll_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠫႧ"), None)
    if not session_id:
      logger.warning(bstack11ll_opy_ (u"ࠣࡐࡲࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡏࡄࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤࡩࡸࡩࡷࡧࡵࠦႨ"))
      return {bstack11ll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣႩ"): bstack11ll_opy_ (u"ࠥࡒࡴࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࠣࡪࡴࡻ࡮ࡥࠤႪ")}
    if bstack1l1ll1lll1_opy_:
      try:
        bstack1l1l11l1l1_opy_ = {
              bstack11ll_opy_ (u"ࠫࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠨႫ"): os.environ.get(bstack11ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪႬ"), os.environ.get(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪႭ"), bstack11ll_opy_ (u"ࠧࠨႮ"))),
              bstack11ll_opy_ (u"ࠨࡶ࡫ࡘࡪࡹࡴࡓࡷࡱ࡙ࡺ࡯ࡤࠨႯ"): bstack1l111l1l_opy_.current_test_uuid() if bstack1l111l1l_opy_.current_test_uuid() else bstack1l1l111l_opy_.current_hook_uuid(),
              bstack11ll_opy_ (u"ࠩࡤࡹࡹ࡮ࡈࡦࡣࡧࡩࡷ࠭Ⴐ"): os.environ.get(bstack11ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨႱ")),
              bstack11ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡖ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫႲ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack11ll_opy_ (u"ࠬࡺࡨࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪႳ"): os.environ.get(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫႴ"), bstack11ll_opy_ (u"ࠧࠨႵ")),
              bstack11ll_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨႶ"): kwargs.get(bstack11ll_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࡡࡦࡳࡲࡳࡡ࡯ࡦࠪႷ"), None) or bstack11ll_opy_ (u"ࠪࠫႸ")
          }
        if not hasattr(thread_local, bstack11ll_opy_ (u"ࠫࡧࡧࡳࡦࡡࡤࡴࡵࡥࡡ࠲࠳ࡼࡣࡸࡩࡲࡪࡲࡷࠫႹ")):
            scripts = {bstack11ll_opy_ (u"ࠬࡹࡣࡢࡰࠪႺ"): bstack1l1l1l1l1_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack11l1ll11l1_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack11l1ll11l1_opy_[bstack11ll_opy_ (u"࠭ࡳࡤࡣࡱࠫႻ")] = bstack11l1ll11l1_opy_[bstack11ll_opy_ (u"ࠧࡴࡥࡤࡲࠬႼ")] % json.dumps(bstack1l1l11l1l1_opy_)
        bstack1l1l1l1l1_opy_.bstack1l11l11l1_opy_(bstack11l1ll11l1_opy_)
        bstack1l1l1l1l1_opy_.store()
        bstack1ll111l1ll_opy_ = driver.execute_script(bstack1l1l1l1l1_opy_.perform_scan)
      except Exception as bstack1111ll1l11_opy_:
        logger.info(bstack11ll_opy_ (u"ࠣࡃࡳࡴ࡮ࡻ࡭ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࠣႽ") + str(bstack1111ll1l11_opy_))
        bstack1ll111l1ll_opy_ = {bstack11ll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣႾ"): str(bstack1111ll1l11_opy_)}
    else:
      bstack1ll111l1ll_opy_ = driver.execute_async_script(bstack1l1l1l1l1_opy_.perform_scan, {bstack11ll_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪႿ"): kwargs.get(bstack11ll_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣࡨࡵ࡭࡮ࡣࡱࡨࠬჀ"), None) or bstack11ll_opy_ (u"ࠬ࠭Ⴡ")})
    return bstack1ll111l1ll_opy_
  except Exception as err:
    logger.error(bstack11ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡵࡹࡳࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡤࡣࡱ࠲ࠥࢁࡽࠣჂ").format(str(err)))
    return {}