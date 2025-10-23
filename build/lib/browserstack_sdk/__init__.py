# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
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
from browserstack_sdk.bstack11111llll_opy_ import bstack1l1ll1l11l_opy_
from browserstack_sdk.bstack1lll11111_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack1l1l11llll_opy_():
  global CONFIG
  headers = {
        bstack11lll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨਠ"): bstack11lll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ਡ"),
      }
  proxies = bstack1lll111l11_opy_(CONFIG, bstack111llll1l1_opy_)
  try:
    response = requests.get(bstack111llll1l1_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1ll1ll11l1_opy_ = response.json()[bstack11lll1_opy_ (u"ࠫ࡭ࡻࡢࡴࠩਢ")]
      logger.debug(bstack1l11l11ll1_opy_.format(response.json()))
      return bstack1ll1ll11l1_opy_
    else:
      logger.debug(bstack1ll1llll1l_opy_.format(bstack11lll1_opy_ (u"ࠧࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡋࡕࡒࡒࠥࡶࡡࡳࡵࡨࠤࡪࡸࡲࡰࡴࠣࠦਣ")))
  except Exception as e:
    logger.debug(bstack1ll1llll1l_opy_.format(e))
def bstack1111ll11l_opy_(hub_url):
  global CONFIG
  url = bstack11lll1_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣਤ")+  hub_url + bstack11lll1_opy_ (u"ࠢ࠰ࡥ࡫ࡩࡨࡱࠢਥ")
  headers = {
        bstack11lll1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧਦ"): bstack11lll1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬਧ"),
      }
  proxies = bstack1lll111l11_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack111l1llll_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1l11l1l11_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack111l1lllll_opy_, stage=STAGE.bstack11ll1ll11_opy_)
def bstack11ll1llll1_opy_():
  try:
    global bstack111111ll1l_opy_
    bstack1ll1ll11l1_opy_ = bstack1l1l11llll_opy_()
    bstack111ll1l11l_opy_ = []
    results = []
    for bstack11111l1ll1_opy_ in bstack1ll1ll11l1_opy_:
      bstack111ll1l11l_opy_.append(bstack111l1l111l_opy_(target=bstack1111ll11l_opy_,args=(bstack11111l1ll1_opy_,)))
    for t in bstack111ll1l11l_opy_:
      t.start()
    for t in bstack111ll1l11l_opy_:
      results.append(t.join())
    bstack111l11lll1_opy_ = {}
    for item in results:
      hub_url = item[bstack11lll1_opy_ (u"ࠪ࡬ࡺࡨ࡟ࡶࡴ࡯ࠫਨ")]
      latency = item[bstack11lll1_opy_ (u"ࠫࡱࡧࡴࡦࡰࡦࡽࠬ਩")]
      bstack111l11lll1_opy_[hub_url] = latency
    bstack11ll1111ll_opy_ = min(bstack111l11lll1_opy_, key= lambda x: bstack111l11lll1_opy_[x])
    bstack111111ll1l_opy_ = bstack11ll1111ll_opy_
    logger.debug(bstack111lll1111_opy_.format(bstack11ll1111ll_opy_))
  except Exception as e:
    logger.debug(bstack11l111l1ll_opy_.format(e))
from browserstack_sdk.bstack11111l1l_opy_ import *
from browserstack_sdk.bstack1lllll1l1_opy_ import *
from browserstack_sdk.bstack11l1l111_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack1l1l1llll1_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack11ll11ll1_opy_, stage=STAGE.bstack11ll1ll11_opy_)
def bstack1lll1111ll_opy_():
    global bstack111111ll1l_opy_
    try:
        bstack11111l111l_opy_ = bstack1ll11ll1l_opy_()
        bstack1l1lllll1l_opy_(bstack11111l111l_opy_)
        hub_url = bstack11111l111l_opy_.get(bstack11lll1_opy_ (u"ࠧࡻࡲ࡭ࠤਪ"), bstack11lll1_opy_ (u"ࠨࠢਫ"))
        if hub_url.endswith(bstack11lll1_opy_ (u"ࠧ࠰ࡹࡧ࠳࡭ࡻࡢࠨਬ")):
            hub_url = hub_url.rsplit(bstack11lll1_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩਭ"), 1)[0]
        if hub_url.startswith(bstack11lll1_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱ࠪਮ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack11lll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠬਯ")):
            hub_url = hub_url[8:]
        bstack111111ll1l_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1ll11ll1l_opy_():
    global CONFIG
    bstack1l11111lll_opy_ = CONFIG.get(bstack11lll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨਰ"), {}).get(bstack11lll1_opy_ (u"ࠬ࡭ࡲࡪࡦࡑࡥࡲ࡫ࠧ਱"), bstack11lll1_opy_ (u"࠭ࡎࡐࡡࡊࡖࡎࡊ࡟ࡏࡃࡐࡉࡤࡖࡁࡔࡕࡈࡈࠬਲ"))
    if not isinstance(bstack1l11111lll_opy_, str):
        raise ValueError(bstack11lll1_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡇࡳ࡫ࡧࠤࡳࡧ࡭ࡦࠢࡰࡹࡸࡺࠠࡣࡧࠣࡥࠥࡼࡡ࡭࡫ࡧࠤࡸࡺࡲࡪࡰࡪࠦਲ਼"))
    try:
        bstack11111l111l_opy_ = bstack11l11l1111_opy_(bstack1l11111lll_opy_)
        return bstack11111l111l_opy_
    except Exception as e:
        logger.error(bstack11lll1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢ਴").format(str(e)))
        return {}
def bstack11l11l1111_opy_(bstack1l11111lll_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack11lll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫਵ")] or not CONFIG[bstack11lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ਸ਼")]:
            raise ValueError(bstack11lll1_opy_ (u"ࠦࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡺࡹࡥࡳࡰࡤࡱࡪࠦ࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾࠨ਷"))
        url = bstack1ll111l1l1_opy_ + bstack1l11111lll_opy_
        auth = (CONFIG[bstack11lll1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧਸ")], CONFIG[bstack11lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩਹ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1111ll111_opy_ = json.loads(response.text)
            return bstack1111ll111_opy_
    except ValueError as ve:
        logger.error(bstack11lll1_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢ਺").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack11lll1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣ਻").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1l1lllll1l_opy_(bstack11llll1l1l_opy_):
    global CONFIG
    if bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ਼࠭") not in CONFIG or str(CONFIG[bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ਽")]).lower() == bstack11lll1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪਾ"):
        CONFIG[bstack11lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫਿ")] = False
    elif bstack11lll1_opy_ (u"࠭ࡩࡴࡖࡵ࡭ࡦࡲࡇࡳ࡫ࡧࠫੀ") in bstack11llll1l1l_opy_:
        bstack111l11lll_opy_ = CONFIG.get(bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫੁ"), {})
        logger.debug(bstack11lll1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡺ࡬ࡷࡹ࡯࡮ࡨࠢ࡯ࡳࡨࡧ࡬ࠡࡱࡳࡸ࡮ࡵ࡮ࡴ࠼ࠣࠩࡸࠨੂ"), bstack111l11lll_opy_)
        bstack11l1ll11ll_opy_ = bstack11llll1l1l_opy_.get(bstack11lll1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡔࡨࡴࡪࡧࡴࡦࡴࡶࠦ੃"), [])
        bstack1111ll1l1_opy_ = bstack11lll1_opy_ (u"ࠥ࠰ࠧ੄").join(bstack11l1ll11ll_opy_)
        logger.debug(bstack11lll1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡇࡺࡹࡴࡰ࡯ࠣࡶࡪࡶࡥࡢࡶࡨࡶࠥࡹࡴࡳ࡫ࡱ࡫࠿ࠦࠥࡴࠤ੅"), bstack1111ll1l1_opy_)
        bstack111111llll_opy_ = {
            bstack11lll1_opy_ (u"ࠧࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢ੆"): bstack11lll1_opy_ (u"ࠨࡡࡵࡵ࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧੇ"),
            bstack11lll1_opy_ (u"ࠢࡧࡱࡵࡧࡪࡒ࡯ࡤࡣ࡯ࠦੈ"): bstack11lll1_opy_ (u"ࠣࡶࡵࡹࡪࠨ੉"),
            bstack11lll1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠦ੊"): bstack1111ll1l1_opy_
        }
        bstack111l11lll_opy_.update(bstack111111llll_opy_)
        logger.debug(bstack11lll1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡘࡴࡩࡧࡴࡦࡦࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢੋ"), bstack111l11lll_opy_)
        CONFIG[bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨੌ")] = bstack111l11lll_opy_
        logger.debug(bstack11lll1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡋ࡯࡮ࡢ࡮ࠣࡇࡔࡔࡆࡊࡉ࠽ࠤࠪࡹ੍ࠢ"), CONFIG)
def bstack1ll1ll1ll1_opy_():
    bstack11111l111l_opy_ = bstack1ll11ll1l_opy_()
    if not bstack11111l111l_opy_[bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡘࡶࡱ࠭੎")]:
      raise ValueError(bstack11lll1_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠠࡪࡵࠣࡱ࡮ࡹࡳࡪࡰࡪࠤ࡫ࡸ࡯࡮ࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳ࠯ࠤ੏"))
    return bstack11111l111l_opy_[bstack11lll1_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠨ੐")] + bstack11lll1_opy_ (u"ࠩࡂࡧࡦࡶࡳ࠾ࠩੑ")
@measure(event_name=EVENTS.bstack11lll1111l_opy_, stage=STAGE.bstack11ll1ll11_opy_)
def bstack11l11l1lll_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack11lll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ੒")], CONFIG[bstack11lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ੓")])
        url = bstack111ll1ll11_opy_
        logger.debug(bstack11lll1_opy_ (u"ࠧࡇࡴࡵࡧࡰࡴࡹ࡯࡮ࡨࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶࠤ࡫ࡸ࡯࡮ࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡖࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠥࡇࡐࡊࠤ੔"))
        try:
            response = requests.get(url, auth=auth, headers={bstack11lll1_opy_ (u"ࠨࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠧ੕"): bstack11lll1_opy_ (u"ࠢࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠥ੖")})
            if response.status_code == 200:
                bstack1111l1111_opy_ = json.loads(response.text)
                bstack11l11l111l_opy_ = bstack1111l1111_opy_.get(bstack11lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡳࠨ੗"), [])
                if bstack11l11l111l_opy_:
                    bstack11ll1l111l_opy_ = bstack11l11l111l_opy_[0]
                    build_hashed_id = bstack11ll1l111l_opy_.get(bstack11lll1_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ੘"))
                    bstack1111l111ll_opy_ = bstack1l11111l11_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1111l111ll_opy_])
                    logger.info(bstack1l1l111ll_opy_.format(bstack1111l111ll_opy_))
                    bstack11l11l1l1l_opy_ = CONFIG[bstack11lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ਖ਼")]
                    if bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ਗ਼") in CONFIG:
                      bstack11l11l1l1l_opy_ += bstack11lll1_opy_ (u"ࠬࠦࠧਜ਼") + CONFIG[bstack11lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨੜ")]
                    if bstack11l11l1l1l_opy_ != bstack11ll1l111l_opy_.get(bstack11lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ੝")):
                      logger.debug(bstack1l11lll111_opy_.format(bstack11ll1l111l_opy_.get(bstack11lll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ਫ਼")), bstack11l11l1l1l_opy_))
                    return result
                else:
                    logger.debug(bstack11lll1_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡐࡲࠤࡧࡻࡩ࡭ࡦࡶࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡴࡩࡧࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠳ࠨ੟"))
            else:
                logger.debug(bstack11lll1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶ࠲ࠧ੠"))
        except Exception as e:
            logger.error(bstack11lll1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࡸࠦ࠺ࠡࡽࢀࠦ੡").format(str(e)))
    else:
        logger.debug(bstack11lll1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡕࡎࡇࡋࡊࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡸ࡫ࡴ࠯ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶ࠲ࠧ੢"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1l1l1ll1l_opy_ import bstack1l1l1ll1l_opy_, Events, bstack11111l11l1_opy_, bstack11lll1ll1_opy_
from bstack_utils.measure import bstack1111l111l1_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1lll11lll1_opy_ import bstack11ll111l1l_opy_
from bstack_utils.messages import *
from bstack_utils import bstack1l1l1llll1_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack111111lll1_opy_, bstack1lll111l1l_opy_, bstack111ll111ll_opy_, bstack1lll111l_opy_, \
  bstack11l1l1ll1l_opy_, \
  Notset, bstack1111ll1ll1_opy_, \
  bstack1ll11l11ll_opy_, bstack1ll1ll111_opy_, bstack1ll1l111ll_opy_, bstack111llllll1_opy_, bstack1lll1ll11l_opy_, bstack1111l1l11l_opy_, \
  bstack11l111ll11_opy_, \
  bstack1l1ll1l111_opy_, bstack111l111l1_opy_, bstack1l1111ll1_opy_, bstack11ll111lll_opy_, \
  bstack1l11l11l1l_opy_, bstack1ll111l111_opy_, bstack11lllll1l1_opy_, bstack11l11ll111_opy_
from bstack_utils.bstack11l1l1ll1_opy_ import bstack1l11111l1_opy_
from bstack_utils.bstack1l1l111lll_opy_ import bstack11l11l11l1_opy_, bstack1l1lll11l1_opy_
from bstack_utils.bstack111l11111l_opy_ import bstack111ll1ll1l_opy_
from bstack_utils.bstack1111ll1lll_opy_ import bstack1lllll1l1l_opy_, bstack1l1lll111l_opy_
from bstack_utils.bstack11ll1111l_opy_ import bstack11ll1111l_opy_
from bstack_utils.bstack11ll111ll_opy_ import bstack1111lllll1_opy_
from bstack_utils.proxy import bstack1111llll1_opy_, bstack1lll111l11_opy_, bstack1l1l1l1ll_opy_, bstack1lll1l11ll_opy_
from bstack_utils.bstack11ll11l1ll_opy_ import bstack1111lll111_opy_
import bstack_utils.bstack11llll111_opy_ as bstack11l11l11ll_opy_
import bstack_utils.bstack11ll1111l1_opy_ as bstack1l1l1l11l1_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack111ll1lll1_opy_ import bstack1111l1l11_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack11111lll_opy_
from bstack_utils.bstack1ll1l1lll_opy_ import bstack11lll1l1l1_opy_
if os.getenv(bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡋࡓࡔࡑࡓࠨ੣")):
  cli.bstack1l1111111l_opy_()
else:
  os.environ[bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡌࡔࡕࡋࡔࠩ੤")] = bstack11lll1_opy_ (u"ࠨࡶࡵࡹࡪ࠭੥")
bstack11l1l1111l_opy_ = bstack11lll1_opy_ (u"ࠩࠣࠤ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࠢࠣ࡭࡫࠮ࡰࡢࡩࡨࠤࡂࡃ࠽ࠡࡸࡲ࡭ࡩࠦ࠰ࠪࠢࡾࡠࡳࠦࠠࠡࡶࡵࡽࢀࡢ࡮ࠡࡥࡲࡲࡸࡺࠠࡧࡵࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮࡜ࠨࡨࡶࡠࠬ࠯࠻࡝ࡰࠣࠤࠥࠦࠠࡧࡵ࠱ࡥࡵࡶࡥ࡯ࡦࡉ࡭ࡱ࡫ࡓࡺࡰࡦࠬࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩ࠮ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡵࡥࡩ࡯ࡦࡨࡼ࠮ࠦࠫࠡࠤ࠽ࠦࠥ࠱ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭࠮ࡡࡸࡣ࡬ࡸࠥࡴࡥࡸࡒࡤ࡫ࡪ࠸࠮ࡦࡸࡤࡰࡺࡧࡴࡦࠪࠥࠬ࠮ࠦ࠽࠿ࠢࡾࢁࠧ࠲ࠠ࡝ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡪࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡥࡵࡣ࡬ࡰࡸࠨࡽ࡝ࠩࠬ࠭࠮ࡡࠢࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠥࡡ࠮ࠦࠫࠡࠤ࠯ࡠࡡࡴࠢࠪ࡞ࡱࠤࠥࠦࠠࡾࡥࡤࡸࡨ࡮ࠨࡦࡺࠬࡿࡡࡴࠠࠡࠢࠣࢁࡡࡴࠠࠡࡿ࡟ࡲࠥࠦ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠩ੦")
bstack1111llllll_opy_ = bstack11lll1_opy_ (u"ࠪࡠࡳ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭ࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠶ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡱࡡ࡬ࡲࡩ࡫ࡸࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠶ࡢࡢ࡮ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮ࡴ࡮࡬ࡧࡪ࠮࠰࠭ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷࠮ࡢ࡮ࡤࡱࡱࡷࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮ࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ࠯࠻࡝ࡰ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰࡯ࡥࡺࡴࡣࡩࠢࡀࠤࡦࡹࡹ࡯ࡥࠣࠬࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶ࠭ࠥࡃ࠾ࠡࡽ࡟ࡲࡱ࡫ࡴࠡࡥࡤࡴࡸࡁ࡜࡯ࡶࡵࡽࠥࢁ࡜࡯ࡥࡤࡴࡸࠦ࠽ࠡࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠬࡠࡳࠦࠠࡾࠢࡦࡥࡹࡩࡨࠩࡧࡻ࠭ࠥࢁ࡜࡯ࠢࠣࠤࠥࢃ࡜࡯ࠢࠣࡶࡪࡺࡵࡳࡰࠣࡥࡼࡧࡩࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰ࡦࡳࡳࡴࡥࡤࡶࠫࡿࡡࡴࠠࠡࠢࠣࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺ࠺ࠡࡢࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠨࢀ࡫࡮ࡤࡱࡧࡩ࡚ࡘࡉࡄࡱࡰࡴࡴࡴࡥ࡯ࡶࠫࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡨࡧࡰࡴࠫࠬࢁࡥ࠲࡜࡯ࠢࠣࠤࠥ࠴࠮࠯࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳ࡝ࡰࠣࠤࢂ࠯࡜࡯ࡿ࡟ࡲ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࠩ੧")
from ._version import __version__
bstack1l111llll1_opy_ = None
CONFIG = {}
bstack1llll1111l_opy_ = {}
bstack11l111l11l_opy_ = {}
bstack111l1l1l1l_opy_ = None
bstack111ll1l1ll_opy_ = None
bstack1l11llll1_opy_ = None
bstack11l111111_opy_ = -1
bstack1l1l111ll1_opy_ = 0
bstack1l11ll1ll1_opy_ = bstack1ll11l1lll_opy_
bstack1l1ll11l1_opy_ = 1
bstack1l1111111_opy_ = False
bstack1lll1lllll_opy_ = False
bstack11lll1l11l_opy_ = bstack11lll1_opy_ (u"ࠫࠬ੨")
bstack1l1111lll1_opy_ = bstack11lll1_opy_ (u"ࠬ࠭੩")
bstack1ll1l11111_opy_ = False
bstack11ll11lll1_opy_ = True
bstack11l11llll1_opy_ = bstack11lll1_opy_ (u"࠭ࠧ੪")
bstack1l1l11l11l_opy_ = []
bstack11111l111_opy_ = threading.Lock()
bstack1l11ll11l_opy_ = threading.Lock()
bstack111111ll1l_opy_ = bstack11lll1_opy_ (u"ࠧࠨ੫")
bstack111l1ll11l_opy_ = False
bstack1llll11lll_opy_ = None
bstack111111ll11_opy_ = None
bstack111l111l11_opy_ = None
bstack111l111111_opy_ = -1
bstack1ll1l11l1l_opy_ = os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠨࢀࠪ੬")), bstack11lll1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ੭"), bstack11lll1_opy_ (u"ࠪ࠲ࡷࡵࡢࡰࡶ࠰ࡶࡪࡶ࡯ࡳࡶ࠰࡬ࡪࡲࡰࡦࡴ࠱࡮ࡸࡵ࡮ࠨ੮"))
bstack1llll1ll11_opy_ = 0
bstack1l111l111_opy_ = 0
bstack1l11111111_opy_ = []
bstack1ll1lll1ll_opy_ = []
bstack11l1l11l1l_opy_ = []
bstack1l1ll111ll_opy_ = []
bstack1111l1ll11_opy_ = bstack11lll1_opy_ (u"ࠫࠬ੯")
bstack11lll11lll_opy_ = bstack11lll1_opy_ (u"ࠬ࠭ੰ")
bstack111ll11l1_opy_ = False
bstack11l111ll1l_opy_ = False
bstack1l111l1l11_opy_ = {}
bstack1111lll1ll_opy_ = None
bstack1l1ll11ll1_opy_ = None
bstack11111l1lll_opy_ = None
bstack1llll1l111_opy_ = None
bstack111ll1111_opy_ = None
bstack1lll1l1lll_opy_ = None
bstack1l1l11l1l1_opy_ = None
bstack1ll1ll1111_opy_ = None
bstack11111ll11l_opy_ = None
bstack111llll1l_opy_ = None
bstack1l11l1l1ll_opy_ = None
bstack1l11llllll_opy_ = None
bstack1l11l1llll_opy_ = None
bstack11l11ll1ll_opy_ = None
bstack1l1ll1111l_opy_ = None
bstack11l111ll1_opy_ = None
bstack11lll111l_opy_ = None
bstack111111ll1_opy_ = None
bstack1l111111l_opy_ = None
bstack1l11lll1l_opy_ = None
bstack1ll1ll1ll_opy_ = None
bstack111lll1l1l_opy_ = None
bstack1l1l1111l1_opy_ = None
thread_local = threading.local()
bstack1111l11111_opy_ = False
bstack111ll11l11_opy_ = bstack11lll1_opy_ (u"ࠨࠢੱ")
logger = bstack1l1l1llll1_opy_.get_logger(__name__, bstack1l11ll1ll1_opy_)
bstack1lll1l11l_opy_ = Config.bstack111ll1l1_opy_()
percy = bstack11l1lll11_opy_()
bstack11l1lllll_opy_ = bstack11ll111l1l_opy_()
bstack1111l11l1_opy_ = bstack11l1l111_opy_()
def bstack111l11ll11_opy_():
  global CONFIG
  global bstack111ll11l1_opy_
  global bstack1lll1l11l_opy_
  testContextOptions = bstack1llll11111_opy_(CONFIG)
  if bstack11l1l1ll1l_opy_(CONFIG):
    if (bstack11lll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩੲ") in testContextOptions and str(testContextOptions[bstack11lll1_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪੳ")]).lower() == bstack11lll1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧੴ")):
      bstack111ll11l1_opy_ = True
    bstack1lll1l11l_opy_.bstack1ll1l11ll_opy_(testContextOptions.get(bstack11lll1_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧੵ"), False))
  else:
    bstack111ll11l1_opy_ = True
    bstack1lll1l11l_opy_.bstack1ll1l11ll_opy_(True)
def bstack1ll111lll_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11lllll11l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1llllll1ll_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11lll1_opy_ (u"ࠦ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡨࡵ࡮ࡧ࡫ࡪࡪ࡮ࡲࡥࠣ੶") == args[i].lower() or bstack11lll1_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡩ࡭࡬ࠨ੷") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack11l11llll1_opy_
      bstack11l11llll1_opy_ += bstack11lll1_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡃࡰࡰࡩ࡭࡬ࡌࡩ࡭ࡧࠣࠫ੸") + shlex.quote(path)
      return path
  return None
bstack1l11l1l1l_opy_ = re.compile(bstack11lll1_opy_ (u"ࡲࠣ࠰࠭ࡃࡡࠪࡻࠩ࠰࠭ࡃ࠮ࢃ࠮ࠫࡁࠥ੹"))
def bstack11l1111ll_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l11l1l1l_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11lll1_opy_ (u"ࠣࠦࡾࠦ੺") + group + bstack11lll1_opy_ (u"ࠤࢀࠦ੻"), os.environ.get(group))
  return value
def bstack1l1ll111l_opy_():
  global bstack1l1l1111l1_opy_
  if bstack1l1l1111l1_opy_ is None:
        bstack1l1l1111l1_opy_ = bstack1llllll1ll_opy_()
  bstack1l11lll1l1_opy_ = bstack1l1l1111l1_opy_
  if bstack1l11lll1l1_opy_ and os.path.exists(os.path.abspath(bstack1l11lll1l1_opy_)):
    fileName = bstack1l11lll1l1_opy_
  if bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧ੼") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ੽")])) and not bstack11lll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡑࡥࡲ࡫ࠧ੾") in locals():
    fileName = os.environ[bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࡤࡌࡉࡍࡇࠪ੿")]
  if bstack11lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡓࡧ࡭ࡦࠩ઀") in locals():
    bstack11l111l_opy_ = os.path.abspath(fileName)
  else:
    bstack11l111l_opy_ = bstack11lll1_opy_ (u"ࠨࠩઁ")
  bstack1ll111111l_opy_ = os.getcwd()
  bstack1l1l1l111l_opy_ = bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬં")
  bstack1l1l11lll1_opy_ = bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡥࡲࡲࠧઃ")
  while (not os.path.exists(bstack11l111l_opy_)) and bstack1ll111111l_opy_ != bstack11lll1_opy_ (u"ࠦࠧ઄"):
    bstack11l111l_opy_ = os.path.join(bstack1ll111111l_opy_, bstack1l1l1l111l_opy_)
    if not os.path.exists(bstack11l111l_opy_):
      bstack11l111l_opy_ = os.path.join(bstack1ll111111l_opy_, bstack1l1l11lll1_opy_)
    if bstack1ll111111l_opy_ != os.path.dirname(bstack1ll111111l_opy_):
      bstack1ll111111l_opy_ = os.path.dirname(bstack1ll111111l_opy_)
    else:
      bstack1ll111111l_opy_ = bstack11lll1_opy_ (u"ࠧࠨઅ")
  bstack1l1l1111l1_opy_ = bstack11l111l_opy_ if os.path.exists(bstack11l111l_opy_) else None
  return bstack1l1l1111l1_opy_
def bstack11ll1l11l1_opy_(config):
    if bstack11lll1_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬࠭આ") in config:
      config[bstack11lll1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫઇ")] = config[bstack11lll1_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࠨઈ")]
    if bstack11lll1_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࡑࡳࡸ࡮ࡵ࡮ࡴࠩઉ") in config:
      config[bstack11lll1_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧઊ")] = config[bstack11lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࡓࡵࡺࡩࡰࡰࡶࠫઋ")]
def bstack111l11l1ll_opy_():
  bstack11l111l_opy_ = bstack1l1ll111l_opy_()
  if not os.path.exists(bstack11l111l_opy_):
    bstack1lll1ll111_opy_(
      bstack1l1llll11_opy_.format(os.getcwd()))
  try:
    with open(bstack11l111l_opy_, bstack11lll1_opy_ (u"ࠬࡸࠧઌ")) as stream:
      yaml.add_implicit_resolver(bstack11lll1_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢઍ"), bstack1l11l1l1l_opy_)
      yaml.add_constructor(bstack11lll1_opy_ (u"ࠢࠢࡲࡤࡸ࡭࡫ࡸࠣ઎"), bstack11l1111ll_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack11ll1l11l1_opy_(config)
      return config
  except:
    with open(bstack11l111l_opy_, bstack11lll1_opy_ (u"ࠨࡴࠪએ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack11ll1l11l1_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1lll1ll111_opy_(bstack111l1111l_opy_.format(str(exc)))
def bstack1l111ll1ll_opy_(config):
  bstack11l1l111ll_opy_ = bstack1l1l11l1l_opy_(config)
  for option in list(bstack11l1l111ll_opy_):
    if option.lower() in bstack11l1l11lll_opy_ and option != bstack11l1l11lll_opy_[option.lower()]:
      bstack11l1l111ll_opy_[bstack11l1l11lll_opy_[option.lower()]] = bstack11l1l111ll_opy_[option]
      del bstack11l1l111ll_opy_[option]
  return config
def bstack1ll1111111_opy_():
  global bstack11l111l11l_opy_
  for key, bstack1111lllll_opy_ in bstack1ll1ll1l1_opy_.items():
    if isinstance(bstack1111lllll_opy_, list):
      for var in bstack1111lllll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack11l111l11l_opy_[key] = os.environ[var]
          break
    elif bstack1111lllll_opy_ in os.environ and os.environ[bstack1111lllll_opy_] and str(os.environ[bstack1111lllll_opy_]).strip():
      bstack11l111l11l_opy_[key] = os.environ[bstack1111lllll_opy_]
  if bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫઐ") in os.environ:
    bstack11l111l11l_opy_[bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઑ")] = {}
    bstack11l111l11l_opy_[bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ઒")][bstack11lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઓ")] = os.environ[bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨઔ")]
def bstack1111l1l1l_opy_():
  global bstack1llll1111l_opy_
  global bstack11l11llll1_opy_
  bstack1l111l111l_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack11lll1_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪક").lower() == val.lower():
      bstack1llll1111l_opy_[bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬખ")] = {}
      bstack1llll1111l_opy_[bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ગ")][bstack11lll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬઘ")] = sys.argv[idx + 1]
      bstack1l111l111l_opy_.extend([idx, idx + 1])
      break
  for key, bstack11l1lll11l_opy_ in bstack11ll1l1l1l_opy_.items():
    if isinstance(bstack11l1lll11l_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack11l1lll11l_opy_:
          if bstack11lll1_opy_ (u"ࠫ࠲࠳ࠧઙ") + var.lower() == val.lower() and key not in bstack1llll1111l_opy_:
            bstack1llll1111l_opy_[key] = sys.argv[idx + 1]
            bstack11l11llll1_opy_ += bstack11lll1_opy_ (u"ࠬࠦ࠭࠮ࠩચ") + var + bstack11lll1_opy_ (u"࠭ࠠࠨછ") + shlex.quote(sys.argv[idx + 1])
            bstack1l111l111l_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack11lll1_opy_ (u"ࠧ࠮࠯ࠪજ") + bstack11l1lll11l_opy_.lower() == val.lower() and key not in bstack1llll1111l_opy_:
          bstack1llll1111l_opy_[key] = sys.argv[idx + 1]
          bstack11l11llll1_opy_ += bstack11lll1_opy_ (u"ࠨࠢ࠰࠱ࠬઝ") + bstack11l1lll11l_opy_ + bstack11lll1_opy_ (u"ࠩࠣࠫઞ") + shlex.quote(sys.argv[idx + 1])
          bstack1l111l111l_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack1l111l111l_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack11llll1111_opy_(config):
  bstack11111ll1l1_opy_ = config.keys()
  for bstack1l11l1l1l1_opy_, bstack1ll1l111l_opy_ in bstack11l1111111_opy_.items():
    if bstack1ll1l111l_opy_ in bstack11111ll1l1_opy_:
      config[bstack1l11l1l1l1_opy_] = config[bstack1ll1l111l_opy_]
      del config[bstack1ll1l111l_opy_]
  for bstack1l11l1l1l1_opy_, bstack1ll1l111l_opy_ in bstack1l1l111l11_opy_.items():
    if isinstance(bstack1ll1l111l_opy_, list):
      for bstack11l1ll1ll1_opy_ in bstack1ll1l111l_opy_:
        if bstack11l1ll1ll1_opy_ in bstack11111ll1l1_opy_:
          config[bstack1l11l1l1l1_opy_] = config[bstack11l1ll1ll1_opy_]
          del config[bstack11l1ll1ll1_opy_]
          break
    elif bstack1ll1l111l_opy_ in bstack11111ll1l1_opy_:
      config[bstack1l11l1l1l1_opy_] = config[bstack1ll1l111l_opy_]
      del config[bstack1ll1l111l_opy_]
  for bstack11l1ll1ll1_opy_ in list(config):
    for bstack1ll11lll11_opy_ in bstack111l1l111_opy_:
      if bstack11l1ll1ll1_opy_.lower() == bstack1ll11lll11_opy_.lower() and bstack11l1ll1ll1_opy_ != bstack1ll11lll11_opy_:
        config[bstack1ll11lll11_opy_] = config[bstack11l1ll1ll1_opy_]
        del config[bstack11l1ll1ll1_opy_]
  bstack1l11l1111l_opy_ = [{}]
  if not config.get(bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ટ")):
    config[bstack11lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧઠ")] = [{}]
  bstack1l11l1111l_opy_ = config[bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨડ")]
  for platform in bstack1l11l1111l_opy_:
    for bstack11l1ll1ll1_opy_ in list(platform):
      for bstack1ll11lll11_opy_ in bstack111l1l111_opy_:
        if bstack11l1ll1ll1_opy_.lower() == bstack1ll11lll11_opy_.lower() and bstack11l1ll1ll1_opy_ != bstack1ll11lll11_opy_:
          platform[bstack1ll11lll11_opy_] = platform[bstack11l1ll1ll1_opy_]
          del platform[bstack11l1ll1ll1_opy_]
  for bstack1l11l1l1l1_opy_, bstack1ll1l111l_opy_ in bstack1l1l111l11_opy_.items():
    for platform in bstack1l11l1111l_opy_:
      if isinstance(bstack1ll1l111l_opy_, list):
        for bstack11l1ll1ll1_opy_ in bstack1ll1l111l_opy_:
          if bstack11l1ll1ll1_opy_ in platform:
            platform[bstack1l11l1l1l1_opy_] = platform[bstack11l1ll1ll1_opy_]
            del platform[bstack11l1ll1ll1_opy_]
            break
      elif bstack1ll1l111l_opy_ in platform:
        platform[bstack1l11l1l1l1_opy_] = platform[bstack1ll1l111l_opy_]
        del platform[bstack1ll1l111l_opy_]
  for bstack11l11ll1l1_opy_ in bstack1l1lllll1_opy_:
    if bstack11l11ll1l1_opy_ in config:
      if not bstack1l1lllll1_opy_[bstack11l11ll1l1_opy_] in config:
        config[bstack1l1lllll1_opy_[bstack11l11ll1l1_opy_]] = {}
      config[bstack1l1lllll1_opy_[bstack11l11ll1l1_opy_]].update(config[bstack11l11ll1l1_opy_])
      del config[bstack11l11ll1l1_opy_]
  for platform in bstack1l11l1111l_opy_:
    for bstack11l11ll1l1_opy_ in bstack1l1lllll1_opy_:
      if bstack11l11ll1l1_opy_ in list(platform):
        if not bstack1l1lllll1_opy_[bstack11l11ll1l1_opy_] in platform:
          platform[bstack1l1lllll1_opy_[bstack11l11ll1l1_opy_]] = {}
        platform[bstack1l1lllll1_opy_[bstack11l11ll1l1_opy_]].update(platform[bstack11l11ll1l1_opy_])
        del platform[bstack11l11ll1l1_opy_]
  config = bstack1l111ll1ll_opy_(config)
  return config
def bstack111lllllll_opy_(config):
  global bstack1l1111lll1_opy_
  bstack1ll11l11l1_opy_ = False
  if bstack11lll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪઢ") in config and str(config[bstack11lll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫણ")]).lower() != bstack11lll1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧત"):
    if bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭થ") not in config or str(config[bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧદ")]).lower() == bstack11lll1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪધ"):
      config[bstack11lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫન")] = False
    else:
      bstack11111l111l_opy_ = bstack1ll11ll1l_opy_()
      if bstack11lll1_opy_ (u"࠭ࡩࡴࡖࡵ࡭ࡦࡲࡇࡳ࡫ࡧࠫ઩") in bstack11111l111l_opy_:
        if not bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫપ") in config:
          config[bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬફ")] = {}
        config[bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭બ")][bstack11lll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬભ")] = bstack11lll1_opy_ (u"ࠫࡦࡺࡳ࠮ࡴࡨࡴࡪࡧࡴࡦࡴࠪમ")
        bstack1ll11l11l1_opy_ = True
        bstack1l1111lll1_opy_ = config[bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩય")].get(bstack11lll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨર"))
  if bstack11l1l1ll1l_opy_(config) and bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ઱") in config and str(config[bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬલ")]).lower() != bstack11lll1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨળ") and not bstack1ll11l11l1_opy_:
    if not bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ઴") in config:
      config[bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨવ")] = {}
    if not config[bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩશ")].get(bstack11lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠪષ")) and not bstack11lll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩસ") in config[bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬહ")]:
      bstack1l1111l1_opy_ = datetime.datetime.now()
      bstack11lll1l11_opy_ = bstack1l1111l1_opy_.strftime(bstack11lll1_opy_ (u"ࠩࠨࡨࡤࠫࡢࡠࠧࡋࠩࡒ࠭઺"))
      hostname = socket.gethostname()
      bstack1l1l11111l_opy_ = bstack11lll1_opy_ (u"ࠪࠫ઻").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11lll1_opy_ (u"ࠫࢀࢃ࡟ࡼࡿࡢࡿࢂ઼࠭").format(bstack11lll1l11_opy_, hostname, bstack1l1l11111l_opy_)
      config[bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩઽ")][bstack11lll1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨા")] = identifier
    bstack1l1111lll1_opy_ = config[bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫિ")].get(bstack11lll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪી"))
  return config
def bstack1llll111ll_opy_():
  bstack1ll1l1l1l1_opy_ =  bstack111llllll1_opy_()[bstack11lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠨુ")]
  return bstack1ll1l1l1l1_opy_ if bstack1ll1l1l1l1_opy_ else -1
def bstack11lll1l1ll_opy_(bstack1ll1l1l1l1_opy_):
  global CONFIG
  if not bstack11lll1_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬૂ") in CONFIG[bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ૃ")]:
    return
  CONFIG[bstack11lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૄ")] = CONFIG[bstack11lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨૅ")].replace(
    bstack11lll1_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩ૆"),
    str(bstack1ll1l1l1l1_opy_)
  )
def bstack1l111ll111_opy_():
  global CONFIG
  if not bstack11lll1_opy_ (u"ࠨࠦࡾࡈࡆ࡚ࡅࡠࡖࡌࡑࡊࢃࠧે") in CONFIG[bstack11lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫૈ")]:
    return
  bstack1l1111l1_opy_ = datetime.datetime.now()
  bstack11lll1l11_opy_ = bstack1l1111l1_opy_.strftime(bstack11lll1_opy_ (u"ࠪࠩࡩ࠳ࠥࡣ࠯ࠨࡌ࠿ࠫࡍࠨૉ"))
  CONFIG[bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૊")] = CONFIG[bstack11lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧો")].replace(
    bstack11lll1_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬૌ"),
    bstack11lll1l11_opy_
  )
def bstack1ll1l1lll1_opy_():
  global CONFIG
  if bstack11lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳ્ࠩ") in CONFIG and not bool(CONFIG[bstack11lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૎")]):
    del CONFIG[bstack11lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૏")]
    return
  if not bstack11lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૐ") in CONFIG:
    CONFIG[bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૑")] = bstack11lll1_opy_ (u"ࠬࠩࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨ૒")
  if bstack11lll1_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬ૓") in CONFIG[bstack11lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૔")]:
    bstack1l111ll111_opy_()
    os.environ[bstack11lll1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ૕")] = CONFIG[bstack11lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૖")]
  if not bstack11lll1_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬ૗") in CONFIG[bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૘")]:
    return
  bstack1ll1l1l1l1_opy_ = bstack11lll1_opy_ (u"ࠬ࠭૙")
  bstack111lll1lll_opy_ = bstack1llll111ll_opy_()
  if bstack111lll1lll_opy_ != -1:
    bstack1ll1l1l1l1_opy_ = bstack11lll1_opy_ (u"࠭ࡃࡊࠢࠪ૚") + str(bstack111lll1lll_opy_)
  if bstack1ll1l1l1l1_opy_ == bstack11lll1_opy_ (u"ࠧࠨ૛"):
    bstack1l11l111ll_opy_ = bstack1l1llll11l_opy_(CONFIG[bstack11lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ૜")])
    if bstack1l11l111ll_opy_ != -1:
      bstack1ll1l1l1l1_opy_ = str(bstack1l11l111ll_opy_)
  if bstack1ll1l1l1l1_opy_:
    bstack11lll1l1ll_opy_(bstack1ll1l1l1l1_opy_)
    os.environ[bstack11lll1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭૝")] = CONFIG[bstack11lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૞")]
def bstack11l1llllll_opy_(bstack1lllll1lll_opy_, bstack11l1ll111_opy_, path):
  json_data = {
    bstack11lll1_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૟"): bstack11l1ll111_opy_
  }
  if os.path.exists(path):
    bstack11ll11111_opy_ = json.load(open(path, bstack11lll1_opy_ (u"ࠬࡸࡢࠨૠ")))
  else:
    bstack11ll11111_opy_ = {}
  bstack11ll11111_opy_[bstack1lllll1lll_opy_] = json_data
  with open(path, bstack11lll1_opy_ (u"ࠨࡷࠬࠤૡ")) as outfile:
    json.dump(bstack11ll11111_opy_, outfile)
def bstack1l1llll11l_opy_(bstack1lllll1lll_opy_):
  bstack1lllll1lll_opy_ = str(bstack1lllll1lll_opy_)
  bstack111l11l1l_opy_ = os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠧࡿࠩૢ")), bstack11lll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨૣ"))
  try:
    if not os.path.exists(bstack111l11l1l_opy_):
      os.makedirs(bstack111l11l1l_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠩࢁࠫ૤")), bstack11lll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ૥"), bstack11lll1_opy_ (u"ࠫ࠳ࡨࡵࡪ࡮ࡧ࠱ࡳࡧ࡭ࡦ࠯ࡦࡥࡨ࡮ࡥ࠯࡬ࡶࡳࡳ࠭૦"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11lll1_opy_ (u"ࠬࡽࠧ૧")):
        pass
      with open(file_path, bstack11lll1_opy_ (u"ࠨࡷࠬࠤ૨")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11lll1_opy_ (u"ࠧࡳࠩ૩")) as bstack1ll11l1ll1_opy_:
      bstack1111111l1_opy_ = json.load(bstack1ll11l1ll1_opy_)
    if bstack1lllll1lll_opy_ in bstack1111111l1_opy_:
      bstack1l1111l11_opy_ = bstack1111111l1_opy_[bstack1lllll1lll_opy_][bstack11lll1_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૪")]
      bstack11lll111l1_opy_ = int(bstack1l1111l11_opy_) + 1
      bstack11l1llllll_opy_(bstack1lllll1lll_opy_, bstack11lll111l1_opy_, file_path)
      return bstack11lll111l1_opy_
    else:
      bstack11l1llllll_opy_(bstack1lllll1lll_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack11l1lll1ll_opy_.format(str(e)))
    return -1
def bstack11l11l11l_opy_(config):
  if not config[bstack11lll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ૫")] or not config[bstack11lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭૬")]:
    return True
  else:
    return False
def bstack11l1111l1_opy_(config, index=0):
  global bstack1ll1l11111_opy_
  bstack1l11l1lll_opy_ = {}
  caps = bstack1111l111l_opy_ + bstack1l1llll1l1_opy_
  if config.get(bstack11lll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ૭"), False):
    bstack1l11l1lll_opy_[bstack11lll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ૮")] = True
    bstack1l11l1lll_opy_[bstack11lll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ૯")] = config.get(bstack11lll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ૰"), {})
  if bstack1ll1l11111_opy_:
    caps += bstack11ll1l1ll1_opy_
  for key in config:
    if key in caps + [bstack11lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૱")]:
      continue
    bstack1l11l1lll_opy_[key] = config[key]
  if bstack11lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૲") in config:
    for bstack1l1111lll_opy_ in config[bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૳")][index]:
      if bstack1l1111lll_opy_ in caps:
        continue
      bstack1l11l1lll_opy_[bstack1l1111lll_opy_] = config[bstack11lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૴")][index][bstack1l1111lll_opy_]
  bstack1l11l1lll_opy_[bstack11lll1_opy_ (u"ࠬ࡮࡯ࡴࡶࡑࡥࡲ࡫ࠧ૵")] = socket.gethostname()
  if bstack11lll1_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧ૶") in bstack1l11l1lll_opy_:
    del (bstack1l11l1lll_opy_[bstack11lll1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ૷")])
  return bstack1l11l1lll_opy_
def bstack1111l1ll1_opy_(config):
  global bstack1ll1l11111_opy_
  bstack11l1ll111l_opy_ = {}
  caps = bstack1l1llll1l1_opy_
  if bstack1ll1l11111_opy_:
    caps += bstack11ll1l1ll1_opy_
  for key in caps:
    if key in config:
      bstack11l1ll111l_opy_[key] = config[key]
  return bstack11l1ll111l_opy_
def bstack111111111_opy_(bstack1l11l1lll_opy_, bstack11l1ll111l_opy_):
  bstack1ll11ll11l_opy_ = {}
  for key in bstack1l11l1lll_opy_.keys():
    if key in bstack11l1111111_opy_:
      bstack1ll11ll11l_opy_[bstack11l1111111_opy_[key]] = bstack1l11l1lll_opy_[key]
    else:
      bstack1ll11ll11l_opy_[key] = bstack1l11l1lll_opy_[key]
  for key in bstack11l1ll111l_opy_:
    if key in bstack11l1111111_opy_:
      bstack1ll11ll11l_opy_[bstack11l1111111_opy_[key]] = bstack11l1ll111l_opy_[key]
    else:
      bstack1ll11ll11l_opy_[key] = bstack11l1ll111l_opy_[key]
  return bstack1ll11ll11l_opy_
def bstack11lllll111_opy_(config, index=0):
  global bstack1ll1l11111_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11111l1111_opy_ = bstack111111lll1_opy_(bstack1l11ll111l_opy_, config, logger)
  bstack11l1ll111l_opy_ = bstack1111l1ll1_opy_(config)
  bstack11ll1ll1l1_opy_ = bstack1l1llll1l1_opy_
  bstack11ll1ll1l1_opy_ += bstack11111l11ll_opy_
  bstack11l1ll111l_opy_ = update(bstack11l1ll111l_opy_, bstack11111l1111_opy_)
  if bstack1ll1l11111_opy_:
    bstack11ll1ll1l1_opy_ += bstack11ll1l1ll1_opy_
  if bstack11lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૸") in config:
    if bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧૹ") in config[bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ૺ")][index]:
      caps[bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩૻ")] = config[bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૼ")][index][bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ૽")]
    if bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ૾") in config[bstack11lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૿")][index]:
      caps[bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ଀")] = str(config[bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଁ")][index][bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬଂ")])
    bstack11l1l1llll_opy_ = bstack111111lll1_opy_(bstack1l11ll111l_opy_, config[bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଃ")][index], logger)
    bstack11ll1ll1l1_opy_ += list(bstack11l1l1llll_opy_.keys())
    for bstack111llllll_opy_ in bstack11ll1ll1l1_opy_:
      if bstack111llllll_opy_ in config[bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ଄")][index]:
        if bstack111llllll_opy_ == bstack11lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩଅ"):
          try:
            bstack11l1l1llll_opy_[bstack111llllll_opy_] = str(config[bstack11lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଆ")][index][bstack111llllll_opy_] * 1.0)
          except:
            bstack11l1l1llll_opy_[bstack111llllll_opy_] = str(config[bstack11lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଇ")][index][bstack111llllll_opy_])
        else:
          bstack11l1l1llll_opy_[bstack111llllll_opy_] = config[bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଈ")][index][bstack111llllll_opy_]
        del (config[bstack11lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଉ")][index][bstack111llllll_opy_])
    bstack11l1ll111l_opy_ = update(bstack11l1ll111l_opy_, bstack11l1l1llll_opy_)
  bstack1l11l1lll_opy_ = bstack11l1111l1_opy_(config, index)
  for bstack11l1ll1ll1_opy_ in bstack1l1llll1l1_opy_ + list(bstack11111l1111_opy_.keys()):
    if bstack11l1ll1ll1_opy_ in bstack1l11l1lll_opy_:
      bstack11l1ll111l_opy_[bstack11l1ll1ll1_opy_] = bstack1l11l1lll_opy_[bstack11l1ll1ll1_opy_]
      del (bstack1l11l1lll_opy_[bstack11l1ll1ll1_opy_])
  if bstack1111ll1ll1_opy_(config):
    bstack1l11l1lll_opy_[bstack11lll1_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬଊ")] = True
    caps.update(bstack11l1ll111l_opy_)
    caps[bstack11lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧଋ")] = bstack1l11l1lll_opy_
  else:
    bstack1l11l1lll_opy_[bstack11lll1_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧଌ")] = False
    caps.update(bstack111111111_opy_(bstack1l11l1lll_opy_, bstack11l1ll111l_opy_))
    if bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭଍") in caps:
      caps[bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪ଎")] = caps[bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଏ")]
      del (caps[bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଐ")])
    if bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭଑") in caps:
      caps[bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ଒")] = caps[bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨଓ")]
      del (caps[bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଔ")])
  return caps
def bstack11lll1lll1_opy_():
  global bstack111111ll1l_opy_
  global CONFIG
  if bstack11lllll11l_opy_() <= version.parse(bstack11lll1_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩକ")):
    if bstack111111ll1l_opy_ != bstack11lll1_opy_ (u"ࠪࠫଖ"):
      return bstack11lll1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧଗ") + bstack111111ll1l_opy_ + bstack11lll1_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤଘ")
    return bstack1ll1lll1l_opy_
  if bstack111111ll1l_opy_ != bstack11lll1_opy_ (u"࠭ࠧଙ"):
    return bstack11lll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤଚ") + bstack111111ll1l_opy_ + bstack11lll1_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤଛ")
  return bstack1ll111llll_opy_
def bstack1l1lll1ll1_opy_(options):
  return hasattr(options, bstack11lll1_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪଜ"))
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
def bstack111ll11ll_opy_(options, bstack1l1l1llll_opy_):
  for bstack1l11111ll1_opy_ in bstack1l1l1llll_opy_:
    if bstack1l11111ll1_opy_ in [bstack11lll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଝ"), bstack11lll1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨଞ")]:
      continue
    if bstack1l11111ll1_opy_ in options._experimental_options:
      options._experimental_options[bstack1l11111ll1_opy_] = update(options._experimental_options[bstack1l11111ll1_opy_],
                                                         bstack1l1l1llll_opy_[bstack1l11111ll1_opy_])
    else:
      options.add_experimental_option(bstack1l11111ll1_opy_, bstack1l1l1llll_opy_[bstack1l11111ll1_opy_])
  if bstack11lll1_opy_ (u"ࠬࡧࡲࡨࡵࠪଟ") in bstack1l1l1llll_opy_:
    for arg in bstack1l1l1llll_opy_[bstack11lll1_opy_ (u"࠭ࡡࡳࡩࡶࠫଠ")]:
      options.add_argument(arg)
    del (bstack1l1l1llll_opy_[bstack11lll1_opy_ (u"ࠧࡢࡴࡪࡷࠬଡ")])
  if bstack11lll1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬଢ") in bstack1l1l1llll_opy_:
    for ext in bstack1l1l1llll_opy_[bstack11lll1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ଣ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l1l1llll_opy_[bstack11lll1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧତ")])
def bstack1l111l1l1l_opy_(options, bstack1lll11l111_opy_):
  if bstack11lll1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪଥ") in bstack1lll11l111_opy_:
    for bstack1l111lll11_opy_ in bstack1lll11l111_opy_[bstack11lll1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫଦ")]:
      if bstack1l111lll11_opy_ in options._preferences:
        options._preferences[bstack1l111lll11_opy_] = update(options._preferences[bstack1l111lll11_opy_], bstack1lll11l111_opy_[bstack11lll1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬଧ")][bstack1l111lll11_opy_])
      else:
        options.set_preference(bstack1l111lll11_opy_, bstack1lll11l111_opy_[bstack11lll1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ନ")][bstack1l111lll11_opy_])
  if bstack11lll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭଩") in bstack1lll11l111_opy_:
    for arg in bstack1lll11l111_opy_[bstack11lll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧପ")]:
      options.add_argument(arg)
def bstack1ll11111l_opy_(options, bstack1111lll11_opy_):
  if bstack11lll1_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫଫ") in bstack1111lll11_opy_:
    options.use_webview(bool(bstack1111lll11_opy_[bstack11lll1_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬବ")]))
  bstack111ll11ll_opy_(options, bstack1111lll11_opy_)
def bstack1111l1ll1l_opy_(options, bstack111111lll_opy_):
  for bstack1ll111ll11_opy_ in bstack111111lll_opy_:
    if bstack1ll111ll11_opy_ in [bstack11lll1_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩଭ"), bstack11lll1_opy_ (u"࠭ࡡࡳࡩࡶࠫମ")]:
      continue
    options.set_capability(bstack1ll111ll11_opy_, bstack111111lll_opy_[bstack1ll111ll11_opy_])
  if bstack11lll1_opy_ (u"ࠧࡢࡴࡪࡷࠬଯ") in bstack111111lll_opy_:
    for arg in bstack111111lll_opy_[bstack11lll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ର")]:
      options.add_argument(arg)
  if bstack11lll1_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭଱") in bstack111111lll_opy_:
    options.bstack1l1ll1l1l1_opy_(bool(bstack111111lll_opy_[bstack11lll1_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧଲ")]))
def bstack1ll11ll1l1_opy_(options, bstack1lll11llll_opy_):
  for bstack1l11l111l_opy_ in bstack1lll11llll_opy_:
    if bstack1l11l111l_opy_ in [bstack11lll1_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨଳ"), bstack11lll1_opy_ (u"ࠬࡧࡲࡨࡵࠪ଴")]:
      continue
    options._options[bstack1l11l111l_opy_] = bstack1lll11llll_opy_[bstack1l11l111l_opy_]
  if bstack11lll1_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪଵ") in bstack1lll11llll_opy_:
    for bstack1l11ll1111_opy_ in bstack1lll11llll_opy_[bstack11lll1_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଶ")]:
      options.bstack1ll1ll11ll_opy_(
        bstack1l11ll1111_opy_, bstack1lll11llll_opy_[bstack11lll1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬଷ")][bstack1l11ll1111_opy_])
  if bstack11lll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧସ") in bstack1lll11llll_opy_:
    for arg in bstack1lll11llll_opy_[bstack11lll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨହ")]:
      options.add_argument(arg)
def bstack11ll11l1l1_opy_(options, caps):
  if not hasattr(options, bstack11lll1_opy_ (u"ࠫࡐࡋ࡙ࠨ଺")):
    return
  if options.KEY == bstack11lll1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ଻"):
    options = bstack111ll11l_opy_.bstack111lll1ll_opy_(bstack11l1l111l1_opy_=options, config=CONFIG)
  if options.KEY == bstack11lll1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶ଼ࠫ") and options.KEY in caps:
    bstack111ll11ll_opy_(options, caps[bstack11lll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬଽ")])
  elif options.KEY == bstack11lll1_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ା") and options.KEY in caps:
    bstack1l111l1l1l_opy_(options, caps[bstack11lll1_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧି")])
  elif options.KEY == bstack11lll1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫୀ") and options.KEY in caps:
    bstack1111l1ll1l_opy_(options, caps[bstack11lll1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬୁ")])
  elif options.KEY == bstack11lll1_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ୂ") and options.KEY in caps:
    bstack1ll11111l_opy_(options, caps[bstack11lll1_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧୃ")])
  elif options.KEY == bstack11lll1_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ୄ") and options.KEY in caps:
    bstack1ll11ll1l1_opy_(options, caps[bstack11lll1_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ୅")])
def bstack1ll111lll1_opy_(caps):
  global bstack1ll1l11111_opy_
  if isinstance(os.environ.get(bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ୆")), str):
    bstack1ll1l11111_opy_ = eval(os.getenv(bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫେ")))
  if bstack1ll1l11111_opy_:
    if bstack1ll111lll_opy_() < version.parse(bstack11lll1_opy_ (u"ࠫ࠷࠴࠳࠯࠲ࠪୈ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11lll1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ୉")
    if bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ୊") in caps:
      browser = caps[bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬୋ")]
    elif bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩୌ") in caps:
      browser = caps[bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ୍ࠪ")]
    browser = str(browser).lower()
    if browser == bstack11lll1_opy_ (u"ࠪ࡭ࡵ࡮࡯࡯ࡧࠪ୎") or browser == bstack11lll1_opy_ (u"ࠫ࡮ࡶࡡࡥࠩ୏"):
      browser = bstack11lll1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬ୐")
    if browser == bstack11lll1_opy_ (u"࠭ࡳࡢ࡯ࡶࡹࡳ࡭ࠧ୑"):
      browser = bstack11lll1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ୒")
    if browser not in [bstack11lll1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ୓"), bstack11lll1_opy_ (u"ࠩࡨࡨ࡬࡫ࠧ୔"), bstack11lll1_opy_ (u"ࠪ࡭ࡪ࠭୕"), bstack11lll1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫୖ"), bstack11lll1_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭ୗ")]:
      return None
    try:
      package = bstack11lll1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࢀࢃ࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ୘").format(browser)
      name = bstack11lll1_opy_ (u"ࠧࡐࡲࡷ࡭ࡴࡴࡳࠨ୙")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1l1lll1ll1_opy_(options):
        return None
      for bstack11l1ll1ll1_opy_ in caps.keys():
        options.set_capability(bstack11l1ll1ll1_opy_, caps[bstack11l1ll1ll1_opy_])
      bstack11ll11l1l1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack11ll11lll_opy_(options, bstack11lll11l1l_opy_):
  if not bstack1l1lll1ll1_opy_(options):
    return
  for bstack11l1ll1ll1_opy_ in bstack11lll11l1l_opy_.keys():
    if bstack11l1ll1ll1_opy_ in bstack11111l11ll_opy_:
      continue
    if bstack11l1ll1ll1_opy_ in options._caps and type(options._caps[bstack11l1ll1ll1_opy_]) in [dict, list]:
      options._caps[bstack11l1ll1ll1_opy_] = update(options._caps[bstack11l1ll1ll1_opy_], bstack11lll11l1l_opy_[bstack11l1ll1ll1_opy_])
    else:
      options.set_capability(bstack11l1ll1ll1_opy_, bstack11lll11l1l_opy_[bstack11l1ll1ll1_opy_])
  bstack11ll11l1l1_opy_(options, bstack11lll11l1l_opy_)
  if bstack11lll1_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧ୚") in options._caps:
    if options._caps[bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ୛")] and options._caps[bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଡ଼")].lower() != bstack11lll1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬଢ଼"):
      del options._caps[bstack11lll1_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡧࡩࡧࡻࡧࡨࡧࡵࡅࡩࡪࡲࡦࡵࡶࠫ୞")]
def bstack11llllll1_opy_(proxy_config):
  if bstack11lll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪୟ") in proxy_config:
    proxy_config[bstack11lll1_opy_ (u"ࠧࡴࡵ࡯ࡔࡷࡵࡸࡺࠩୠ")] = proxy_config[bstack11lll1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬୡ")]
    del (proxy_config[bstack11lll1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ୢ")])
  if bstack11lll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭ୣ") in proxy_config and proxy_config[bstack11lll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧ୤")].lower() != bstack11lll1_opy_ (u"ࠬࡪࡩࡳࡧࡦࡸࠬ୥"):
    proxy_config[bstack11lll1_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩ୦")] = bstack11lll1_opy_ (u"ࠧ࡮ࡣࡱࡹࡦࡲࠧ୧")
  if bstack11lll1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡁࡶࡶࡲࡧࡴࡴࡦࡪࡩࡘࡶࡱ࠭୨") in proxy_config:
    proxy_config[bstack11lll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬ୩")] = bstack11lll1_opy_ (u"ࠪࡴࡦࡩࠧ୪")
  return proxy_config
def bstack1l11l1lll1_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11lll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ୫") in config:
    return proxy
  config[bstack11lll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ୬")] = bstack11llllll1_opy_(config[bstack11lll1_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୭")])
  if proxy == None:
    proxy = Proxy(config[bstack11lll1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭୮")])
  return proxy
def bstack111ll11ll1_opy_(self):
  global CONFIG
  global bstack1l11llllll_opy_
  try:
    proxy = bstack1l1l1l1ll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11lll1_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭୯")):
        proxies = bstack1111llll1_opy_(proxy, bstack11lll1lll1_opy_())
        if len(proxies) > 0:
          protocol, bstack11111ll11_opy_ = proxies.popitem()
          if bstack11lll1_opy_ (u"ࠤ࠽࠳࠴ࠨ୰") in bstack11111ll11_opy_:
            return bstack11111ll11_opy_
          else:
            return bstack11lll1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦୱ") + bstack11111ll11_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11lll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡱࡴࡲࡼࡾࠦࡵࡳ࡮ࠣ࠾ࠥࢁࡽࠣ୲").format(str(e)))
  return bstack1l11llllll_opy_(self)
def bstack1l1ll11l1l_opy_():
  global CONFIG
  return bstack1lll1l11ll_opy_(CONFIG) and bstack1111l1l11l_opy_() and bstack11lllll11l_opy_() >= version.parse(bstack1ll1l1l111_opy_)
def bstack1llll11ll1_opy_():
  global CONFIG
  return (bstack11lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ୳") in CONFIG or bstack11lll1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ୴") in CONFIG) and bstack11l111ll11_opy_()
def bstack1l1l11l1l_opy_(config):
  bstack11l1l111ll_opy_ = {}
  if bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୵") in config:
    bstack11l1l111ll_opy_ = config[bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୶")]
  if bstack11lll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୷") in config:
    bstack11l1l111ll_opy_ = config[bstack11lll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୸")]
  proxy = bstack1l1l1l1ll_opy_(config)
  if proxy:
    if proxy.endswith(bstack11lll1_opy_ (u"ࠫ࠳ࡶࡡࡤࠩ୹")) and os.path.isfile(proxy):
      bstack11l1l111ll_opy_[bstack11lll1_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨ୺")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11lll1_opy_ (u"࠭࠮ࡱࡣࡦࠫ୻")):
        proxies = bstack1lll111l11_opy_(config, bstack11lll1lll1_opy_())
        if len(proxies) > 0:
          protocol, bstack11111ll11_opy_ = proxies.popitem()
          if bstack11lll1_opy_ (u"ࠢ࠻࠱࠲ࠦ୼") in bstack11111ll11_opy_:
            parsed_url = urlparse(bstack11111ll11_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11lll1_opy_ (u"ࠣ࠼࠲࠳ࠧ୽") + bstack11111ll11_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack11l1l111ll_opy_[bstack11lll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬ୾")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack11l1l111ll_opy_[bstack11lll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭୿")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack11l1l111ll_opy_[bstack11lll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧ஀")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack11l1l111ll_opy_[bstack11lll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨ஁")] = str(parsed_url.password)
  return bstack11l1l111ll_opy_
def bstack1llll11111_opy_(config):
  if bstack11lll1_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫஂ") in config:
    return config[bstack11lll1_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬஃ")]
  return {}
def bstack11l11111l_opy_(caps):
  global bstack1l1111lll1_opy_
  if bstack11lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ஄") in caps:
    caps[bstack11lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪஅ")][bstack11lll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩஆ")] = True
    if bstack1l1111lll1_opy_:
      caps[bstack11lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬஇ")][bstack11lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧஈ")] = bstack1l1111lll1_opy_
  else:
    caps[bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫஉ")] = True
    if bstack1l1111lll1_opy_:
      caps[bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨஊ")] = bstack1l1111lll1_opy_
@measure(event_name=EVENTS.bstack111l11llll_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack11llll111l_opy_():
  global CONFIG
  if not bstack11l1l1ll1l_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ஋") in CONFIG and bstack11lllll1l1_opy_(CONFIG[bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭஌")]):
    if (
      bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ஍") in CONFIG
      and bstack11lllll1l1_opy_(CONFIG[bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨஎ")].get(bstack11lll1_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩஏ")))
    ):
      logger.debug(bstack11lll1_opy_ (u"ࠨࡌࡰࡥࡤࡰࠥࡨࡩ࡯ࡣࡵࡽࠥࡴ࡯ࡵࠢࡶࡸࡦࡸࡴࡦࡦࠣࡥࡸࠦࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡥ࡯ࡣࡥࡰࡪࡪࠢஐ"))
      return
    bstack11l1l111ll_opy_ = bstack1l1l11l1l_opy_(CONFIG)
    bstack1ll1llll11_opy_(CONFIG[bstack11lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ஑")], bstack11l1l111ll_opy_)
def bstack1ll1llll11_opy_(key, bstack11l1l111ll_opy_):
  global bstack1l111llll1_opy_
  logger.info(bstack1ll111l11_opy_)
  try:
    bstack1l111llll1_opy_ = Local()
    bstack1llllllll1_opy_ = {bstack11lll1_opy_ (u"ࠨ࡭ࡨࡽࠬஒ"): key}
    bstack1llllllll1_opy_.update(bstack11l1l111ll_opy_)
    logger.debug(bstack1llll1llll_opy_.format(str(bstack1llllllll1_opy_)).replace(key, bstack11lll1_opy_ (u"ࠩ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭ஓ")))
    bstack1l111llll1_opy_.start(**bstack1llllllll1_opy_)
    if bstack1l111llll1_opy_.isRunning():
      logger.info(bstack111lll111_opy_)
  except Exception as e:
    bstack1lll1ll111_opy_(bstack11ll1lllll_opy_.format(str(e)))
def bstack1111l1lll1_opy_():
  global bstack1l111llll1_opy_
  if bstack1l111llll1_opy_.isRunning():
    logger.info(bstack1l11llll11_opy_)
    bstack1l111llll1_opy_.stop()
  bstack1l111llll1_opy_ = None
def bstack1l111ll11_opy_(bstack1l1l11lll_opy_=[]):
  global CONFIG
  bstack111lll11l1_opy_ = []
  bstack11ll11l1l_opy_ = [bstack11lll1_opy_ (u"ࠪࡳࡸ࠭ஔ"), bstack11lll1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧக"), bstack11lll1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩ஖"), bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ஗"), bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ஘"), bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩங")]
  try:
    for err in bstack1l1l11lll_opy_:
      bstack11ll111ll1_opy_ = {}
      for k in bstack11ll11l1l_opy_:
        val = CONFIG[bstack11lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬச")][int(err[bstack11lll1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ஛")])].get(k)
        if val:
          bstack11ll111ll1_opy_[k] = val
      if(err[bstack11lll1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪஜ")] != bstack11lll1_opy_ (u"ࠬ࠭஝")):
        bstack11ll111ll1_opy_[bstack11lll1_opy_ (u"࠭ࡴࡦࡵࡷࡷࠬஞ")] = {
          err[bstack11lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬட")]: err[bstack11lll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ஠")]
        }
        bstack111lll11l1_opy_.append(bstack11ll111ll1_opy_)
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫ࡵࡲ࡮ࡣࡷࡸ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵ࠼ࠣࠫ஡") + str(e))
  finally:
    return bstack111lll11l1_opy_
def bstack1ll1l1111_opy_(file_name):
  bstack1l1lllllll_opy_ = []
  try:
    bstack1l1ll1l1ll_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1l1ll1l1ll_opy_):
      with open(bstack1l1ll1l1ll_opy_) as f:
        bstack11llllllll_opy_ = json.load(f)
        bstack1l1lllllll_opy_ = bstack11llllllll_opy_
      os.remove(bstack1l1ll1l1ll_opy_)
    return bstack1l1lllllll_opy_
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡩ࡯ࡦ࡬ࡲ࡬ࠦࡥࡳࡴࡲࡶࠥࡲࡩࡴࡶ࠽ࠤࠬ஢") + str(e))
    return bstack1l1lllllll_opy_
def bstack1ll1111l11_opy_():
  try:
      from bstack_utils.constants import bstack1lll1lll11_opy_, EVENTS
      from bstack_utils.helper import bstack1lll111l1l_opy_, get_host_info, bstack1lll1l11l_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack11llll1ll_opy_ = os.path.join(os.getcwd(), bstack11lll1_opy_ (u"ࠫࡱࡵࡧࠨண"), bstack11lll1_opy_ (u"ࠬࡱࡥࡺ࠯ࡰࡩࡹࡸࡩࡤࡵ࠱࡮ࡸࡵ࡮ࠨத"))
      lock = FileLock(bstack11llll1ll_opy_+bstack11lll1_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧ஥"))
      def bstack1lllll11_opy_():
          try:
              with lock:
                  with open(bstack11llll1ll_opy_, bstack11lll1_opy_ (u"ࠢࡳࠤ஦"), encoding=bstack11lll1_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢ஧")) as file:
                      data = json.load(file)
                      config = {
                          bstack11lll1_opy_ (u"ࠤ࡫ࡩࡦࡪࡥࡳࡵࠥந"): {
                              bstack11lll1_opy_ (u"ࠥࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠤன"): bstack11lll1_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠢப"),
                          }
                      }
                      bstack11l1lllll1_opy_ = datetime.utcnow()
                      bstack1l1111l1_opy_ = bstack11l1lllll1_opy_.strftime(bstack11lll1_opy_ (u"࡙ࠧࠫ࠮ࠧࡰ࠱ࠪࡪࡔࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪ࡛ࠥࡔࡄࠤ஫"))
                      test_id = os.environ.get(bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ஬")) if os.environ.get(bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ஭")) else bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥம"))
                      payload = {
                          bstack11lll1_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࠨய"): bstack11lll1_opy_ (u"ࠥࡷࡩࡱ࡟ࡦࡸࡨࡲࡹࡹࠢர"),
                          bstack11lll1_opy_ (u"ࠦࡩࡧࡴࡢࠤற"): {
                              bstack11lll1_opy_ (u"ࠧࡺࡥࡴࡶ࡫ࡹࡧࡥࡵࡶ࡫ࡧࠦல"): test_id,
                              bstack11lll1_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡪ࡟ࡥࡣࡼࠦள"): bstack1l1111l1_opy_,
                              bstack11lll1_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࠦழ"): bstack11lll1_opy_ (u"ࠣࡕࡇࡏࡋ࡫ࡡࡵࡷࡵࡩࡕ࡫ࡲࡧࡱࡵࡱࡦࡴࡣࡦࠤவ"),
                              bstack11lll1_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠ࡬ࡶࡳࡳࠨஶ"): {
                                  bstack11lll1_opy_ (u"ࠥࡱࡪࡧࡳࡶࡴࡨࡷࠧஷ"): data,
                                  bstack11lll1_opy_ (u"ࠦࡸࡪ࡫ࡓࡷࡱࡍࡩࠨஸ"): bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢஹ"))
                              },
                              bstack11lll1_opy_ (u"ࠨࡵࡴࡧࡵࡣࡩࡧࡴࡢࠤ஺"): bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"ࠢࡶࡵࡨࡶࡓࡧ࡭ࡦࠤ஻")),
                              bstack11lll1_opy_ (u"ࠣࡪࡲࡷࡹࡥࡩ࡯ࡨࡲࠦ஼"): get_host_info()
                          }
                      }
                      bstack1ll111ll1_opy_ = bstack111ll111ll_opy_(cli.config, [bstack11lll1_opy_ (u"ࠤࡤࡴ࡮ࡹࠢ஽"), bstack11lll1_opy_ (u"ࠥࡩࡩࡹࡉ࡯ࡵࡷࡶࡺࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠣா"), bstack11lll1_opy_ (u"ࠦࡦࡶࡩࠣி")], bstack1lll1lll11_opy_)
                      response = bstack1lll111l1l_opy_(bstack11lll1_opy_ (u"ࠧࡖࡏࡔࡖࠥீ"), bstack1ll111ll1_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack11lll1_opy_ (u"ࠨࡄࡢࡶࡤࠤࡸ࡫࡮ࡵࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡶࡲࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡪࡡࡵࡣࠣࡿࢂࠨு").format(bstack1lll1lll11_opy_, payload))
                      else:
                          logger.debug(bstack11lll1_opy_ (u"ࠢࡓࡧࡴࡹࡪࡹࡴࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡨࡲࡶࠥࢁࡽࠡࡹ࡬ࡸ࡭ࠦࡤࡢࡶࡤࠤࢀࢃࠢூ").format(bstack1lll1lll11_opy_, payload))
          except Exception as e:
              logger.debug(bstack11lll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫࡮ࡥࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢࡾࢁࠧ௃").format(e))
      bstack1lllll11_opy_()
      bstack1ll1ll111_opy_(bstack11llll1ll_opy_, logger)
  except:
    pass
def bstack11l11lll1_opy_():
  global bstack111ll11l11_opy_
  global bstack1l1l11l11l_opy_
  global bstack1l11111111_opy_
  global bstack1ll1lll1ll_opy_
  global bstack11l1l11l1l_opy_
  global bstack11lll11lll_opy_
  global CONFIG
  bstack1ll11lll1l_opy_ = os.environ.get(bstack11lll1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪ௄"))
  if bstack1ll11lll1l_opy_ in [bstack11lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ௅"), bstack11lll1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪெ")]:
    bstack11llll1l11_opy_()
  percy.shutdown()
  if bstack111ll11l11_opy_:
    logger.warning(bstack111ll1111l_opy_.format(str(bstack111ll11l11_opy_)))
  else:
    try:
      bstack11ll11111_opy_ = bstack1ll11l11ll_opy_(bstack11lll1_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫே"), logger)
      if bstack11ll11111_opy_.get(bstack11lll1_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫை")) and bstack11ll11111_opy_.get(bstack11lll1_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬ௉")).get(bstack11lll1_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪொ")):
        logger.warning(bstack111ll1111l_opy_.format(str(bstack11ll11111_opy_[bstack11lll1_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧோ")][bstack11lll1_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬௌ")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1l1l1ll1l_opy_.invoke(Events.bstack11111ll1ll_opy_)
  logger.info(bstack111l1llll1_opy_)
  global bstack1l111llll1_opy_
  if bstack1l111llll1_opy_:
    bstack1111l1lll1_opy_()
  try:
    with bstack11111l111_opy_:
      bstack11l1llll1_opy_ = bstack1l1l11l11l_opy_.copy()
    for driver in bstack11l1llll1_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1l11ll111_opy_)
  if bstack11lll11lll_opy_ == bstack11lll1_opy_ (u"ࠫࡷࡵࡢࡰࡶ்ࠪ"):
    bstack11l1l11l1l_opy_ = bstack1ll1l1111_opy_(bstack11lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭௎"))
  if bstack11lll11lll_opy_ == bstack11lll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭௏") and len(bstack1ll1lll1ll_opy_) == 0:
    bstack1ll1lll1ll_opy_ = bstack1ll1l1111_opy_(bstack11lll1_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬௐ"))
    if len(bstack1ll1lll1ll_opy_) == 0:
      bstack1ll1lll1ll_opy_ = bstack1ll1l1111_opy_(bstack11lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧ௑"))
  bstack1l11ll1l1l_opy_ = bstack11lll1_opy_ (u"ࠩࠪ௒")
  if len(bstack1l11111111_opy_) > 0:
    bstack1l11ll1l1l_opy_ = bstack1l111ll11_opy_(bstack1l11111111_opy_)
  elif len(bstack1ll1lll1ll_opy_) > 0:
    bstack1l11ll1l1l_opy_ = bstack1l111ll11_opy_(bstack1ll1lll1ll_opy_)
  elif len(bstack11l1l11l1l_opy_) > 0:
    bstack1l11ll1l1l_opy_ = bstack1l111ll11_opy_(bstack11l1l11l1l_opy_)
  elif len(bstack1l1ll111ll_opy_) > 0:
    bstack1l11ll1l1l_opy_ = bstack1l111ll11_opy_(bstack1l1ll111ll_opy_)
  if bool(bstack1l11ll1l1l_opy_):
    bstack1llllll11l_opy_(bstack1l11ll1l1l_opy_)
  else:
    bstack1llllll11l_opy_()
  bstack1ll1ll111_opy_(bstack1l11l1ll11_opy_, logger)
  if bstack1ll11lll1l_opy_ not in [bstack11lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ௓")]:
    bstack1ll1111l11_opy_()
  bstack1l1l1llll1_opy_.bstack1ll1l111_opy_(CONFIG)
  if len(bstack11l1l11l1l_opy_) > 0:
    sys.exit(len(bstack11l1l11l1l_opy_))
def bstack1l11l1l111_opy_(bstack1l1lll111_opy_, frame):
  global bstack1lll1l11l_opy_
  logger.error(bstack111ll1l1l1_opy_)
  bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡓࡵࠧ௔"), bstack1l1lll111_opy_)
  if hasattr(signal, bstack11lll1_opy_ (u"࡙ࠬࡩࡨࡰࡤࡰࡸ࠭௕")):
    bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭௖"), signal.Signals(bstack1l1lll111_opy_).name)
  else:
    bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧௗ"), bstack11lll1_opy_ (u"ࠨࡕࡌࡋ࡚ࡔࡋࡏࡑ࡚ࡒࠬ௘"))
  if cli.is_running():
    bstack1l1l1ll1l_opy_.invoke(Events.bstack11111ll1ll_opy_)
  bstack1ll11lll1l_opy_ = os.environ.get(bstack11lll1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪ௙"))
  if bstack1ll11lll1l_opy_ == bstack11lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ௚") and not cli.is_enabled(CONFIG):
    bstack1ll1l11l_opy_.stop(bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ௛")))
  bstack11l11lll1_opy_()
  sys.exit(1)
def bstack1lll1ll111_opy_(err):
  logger.critical(bstack1lll1ll1l1_opy_.format(str(err)))
  bstack1llllll11l_opy_(bstack1lll1ll1l1_opy_.format(str(err)), True)
  atexit.unregister(bstack11l11lll1_opy_)
  bstack11llll1l11_opy_()
  sys.exit(1)
def bstack11l1l11l11_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1llllll11l_opy_(message, True)
  atexit.unregister(bstack11l11lll1_opy_)
  bstack11llll1l11_opy_()
  sys.exit(1)
def bstack1l1l111111_opy_():
  global CONFIG
  global bstack1llll1111l_opy_
  global bstack11l111l11l_opy_
  global bstack11ll11lll1_opy_
  CONFIG = bstack111l11l1ll_opy_()
  load_dotenv(CONFIG.get(bstack11lll1_opy_ (u"ࠬ࡫࡮ࡷࡈ࡬ࡰࡪ࠭௜")))
  bstack1ll1111111_opy_()
  bstack1111l1l1l_opy_()
  CONFIG = bstack11llll1111_opy_(CONFIG)
  update(CONFIG, bstack11l111l11l_opy_)
  update(CONFIG, bstack1llll1111l_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack111lllllll_opy_(CONFIG)
  bstack11ll11lll1_opy_ = bstack11l1l1ll1l_opy_(CONFIG)
  os.environ[bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩ௝")] = bstack11ll11lll1_opy_.__str__().lower()
  bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ௞"), bstack11ll11lll1_opy_)
  if (bstack11lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௟") in CONFIG and bstack11lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௠") in bstack1llll1111l_opy_) or (
          bstack11lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௡") in CONFIG and bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௢") not in bstack11l111l11l_opy_):
    if os.getenv(bstack11lll1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ௣")):
      CONFIG[bstack11lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ௤")] = os.getenv(bstack11lll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ௥"))
    else:
      if not CONFIG.get(bstack11lll1_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠦ௦"), bstack11lll1_opy_ (u"ࠤࠥ௧")) in bstack1llll11l1l_opy_:
        bstack1ll1l1lll1_opy_()
  elif (bstack11lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௨") not in CONFIG and bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௩") in CONFIG) or (
          bstack11lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௪") in bstack11l111l11l_opy_ and bstack11lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௫") not in bstack1llll1111l_opy_):
    del (CONFIG[bstack11lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ௬")])
  if bstack11l11l11l_opy_(CONFIG):
    bstack1lll1ll111_opy_(bstack111ll1ll1_opy_)
  Config.bstack111ll1l1_opy_().set_property(bstack11lll1_opy_ (u"ࠣࡷࡶࡩࡷࡔࡡ࡮ࡧࠥ௭"), CONFIG[bstack11lll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ௮")])
  bstack1lll111ll1_opy_()
  bstack1l1lll1l11_opy_()
  if bstack1ll1l11111_opy_ and not CONFIG.get(bstack11lll1_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠨ௯"), bstack11lll1_opy_ (u"ࠦࠧ௰")) in bstack1llll11l1l_opy_:
    CONFIG[bstack11lll1_opy_ (u"ࠬࡧࡰࡱࠩ௱")] = bstack1lllll111l_opy_(CONFIG)
    logger.info(bstack1l1ll11l11_opy_.format(CONFIG[bstack11lll1_opy_ (u"࠭ࡡࡱࡲࠪ௲")]))
  if not bstack11ll11lll1_opy_:
    CONFIG[bstack11lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ௳")] = [{}]
def bstack1ll11l1l1_opy_(config, bstack11l1l1lll1_opy_):
  global CONFIG
  global bstack1ll1l11111_opy_
  CONFIG = config
  bstack1ll1l11111_opy_ = bstack11l1l1lll1_opy_
def bstack1l1lll1l11_opy_():
  global CONFIG
  global bstack1ll1l11111_opy_
  if bstack11lll1_opy_ (u"ࠨࡣࡳࡴࠬ௴") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack11l1l11l11_opy_(e, bstack11111lllll_opy_)
    bstack1ll1l11111_opy_ = True
    bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ௵"), True)
def bstack1lllll111l_opy_(config):
  bstack11lll1l1l_opy_ = bstack11lll1_opy_ (u"ࠪࠫ௶")
  app = config[bstack11lll1_opy_ (u"ࠫࡦࡶࡰࠨ௷")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1llll1l11l_opy_:
      if os.path.exists(app):
        bstack11lll1l1l_opy_ = bstack1111l11ll1_opy_(config, app)
      elif bstack1lll1l1l1l_opy_(app):
        bstack11lll1l1l_opy_ = app
      else:
        bstack1lll1ll111_opy_(bstack111l11ll1_opy_.format(app))
    else:
      if bstack1lll1l1l1l_opy_(app):
        bstack11lll1l1l_opy_ = app
      elif os.path.exists(app):
        bstack11lll1l1l_opy_ = bstack1111l11ll1_opy_(app)
      else:
        bstack1lll1ll111_opy_(bstack1l1llll1l_opy_)
  else:
    if len(app) > 2:
      bstack1lll1ll111_opy_(bstack1ll1l1l11_opy_)
    elif len(app) == 2:
      if bstack11lll1_opy_ (u"ࠬࡶࡡࡵࡪࠪ௸") in app and bstack11lll1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ௹") in app:
        if os.path.exists(app[bstack11lll1_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ௺")]):
          bstack11lll1l1l_opy_ = bstack1111l11ll1_opy_(config, app[bstack11lll1_opy_ (u"ࠨࡲࡤࡸ࡭࠭௻")], app[bstack11lll1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬ௼")])
        else:
          bstack1lll1ll111_opy_(bstack111l11ll1_opy_.format(app))
      else:
        bstack1lll1ll111_opy_(bstack1ll1l1l11_opy_)
    else:
      for key in app:
        if key in bstack11l11l1l11_opy_:
          if key == bstack11lll1_opy_ (u"ࠪࡴࡦࡺࡨࠨ௽"):
            if os.path.exists(app[key]):
              bstack11lll1l1l_opy_ = bstack1111l11ll1_opy_(config, app[key])
            else:
              bstack1lll1ll111_opy_(bstack111l11ll1_opy_.format(app))
          else:
            bstack11lll1l1l_opy_ = app[key]
        else:
          bstack1lll1ll111_opy_(bstack11l1l11ll1_opy_)
  return bstack11lll1l1l_opy_
def bstack1lll1l1l1l_opy_(bstack11lll1l1l_opy_):
  import re
  bstack1lll1l1l11_opy_ = re.compile(bstack11lll1_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬࠧࠦ௾"))
  bstack1111lll1l1_opy_ = re.compile(bstack11lll1_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭࠳ࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪࠥࠤ௿"))
  if bstack11lll1_opy_ (u"࠭ࡢࡴ࠼࠲࠳ࠬఀ") in bstack11lll1l1l_opy_ or re.fullmatch(bstack1lll1l1l11_opy_, bstack11lll1l1l_opy_) or re.fullmatch(bstack1111lll1l1_opy_, bstack11lll1l1l_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack1l1l1l1l11_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack1111l11ll1_opy_(config, path, bstack111l1l1ll_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11lll1_opy_ (u"ࠧࡳࡤࠪఁ")).read()).hexdigest()
  bstack111111l1ll_opy_ = bstack11ll1l1l11_opy_(md5_hash)
  bstack11lll1l1l_opy_ = None
  if bstack111111l1ll_opy_:
    logger.info(bstack1ll1lll1l1_opy_.format(bstack111111l1ll_opy_, md5_hash))
    return bstack111111l1ll_opy_
  bstack11l11lll1l_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack11lll1_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭ం"): (os.path.basename(path), open(os.path.abspath(path), bstack11lll1_opy_ (u"ࠩࡵࡦࠬః")), bstack11lll1_opy_ (u"ࠪࡸࡪࡾࡴ࠰ࡲ࡯ࡥ࡮ࡴࠧఄ")),
      bstack11lll1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧఅ"): bstack111l1l1ll_opy_
    }
  )
  response = requests.post(bstack11l1l1l1l_opy_, data=multipart_data,
                           headers={bstack11lll1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫఆ"): multipart_data.content_type},
                           auth=(config[bstack11lll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨఇ")], config[bstack11lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪఈ")]))
  try:
    res = json.loads(response.text)
    bstack11lll1l1l_opy_ = res[bstack11lll1_opy_ (u"ࠨࡣࡳࡴࡤࡻࡲ࡭ࠩఉ")]
    logger.info(bstack1l1l1l1111_opy_.format(bstack11lll1l1l_opy_))
    bstack1l1l1l11ll_opy_(md5_hash, bstack11lll1l1l_opy_)
    cli.bstack1lllll11ll_opy_(bstack11lll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡶࡲ࡯ࡳࡦࡪ࡟ࡢࡲࡳࠦఊ"), datetime.datetime.now() - bstack11l11lll1l_opy_)
  except ValueError as err:
    bstack1lll1ll111_opy_(bstack11ll11111l_opy_.format(str(err)))
  return bstack11lll1l1l_opy_
def bstack1lll111ll1_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1l1ll11l1_opy_
  bstack1ll1llll1_opy_ = 1
  bstack11ll11l11l_opy_ = 1
  if bstack11lll1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪఋ") in CONFIG:
    bstack11ll11l11l_opy_ = CONFIG[bstack11lll1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫఌ")]
  else:
    bstack11ll11l11l_opy_ = bstack1ll11l1l1l_opy_(framework_name, args) or 1
  if bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ఍") in CONFIG:
    bstack1ll1llll1_opy_ = len(CONFIG[bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩఎ")])
  bstack1l1ll11l1_opy_ = int(bstack11ll11l11l_opy_) * int(bstack1ll1llll1_opy_)
def bstack1ll11l1l1l_opy_(framework_name, args):
  if framework_name == bstack1ll1lll11l_opy_ and args and bstack11lll1_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬఏ") in args:
      bstack1l11llll1l_opy_ = args.index(bstack11lll1_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ఐ"))
      return int(args[bstack1l11llll1l_opy_ + 1]) or 1
  return 1
def bstack11ll1l1l11_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11lll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬ఑"))
    bstack11ll1lll11_opy_ = os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠪࢂࠬఒ")), bstack11lll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఓ"), bstack11lll1_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ఔ"))
    if os.path.exists(bstack11ll1lll11_opy_):
      try:
        bstack111l1111l1_opy_ = json.load(open(bstack11ll1lll11_opy_, bstack11lll1_opy_ (u"࠭ࡲࡣࠩక")))
        if md5_hash in bstack111l1111l1_opy_:
          bstack1llll1l1l1_opy_ = bstack111l1111l1_opy_[md5_hash]
          bstack11lll1ll1l_opy_ = datetime.datetime.now()
          bstack1ll11111ll_opy_ = datetime.datetime.strptime(bstack1llll1l1l1_opy_[bstack11lll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪఖ")], bstack11lll1_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬగ"))
          if (bstack11lll1ll1l_opy_ - bstack1ll11111ll_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack1llll1l1l1_opy_[bstack11lll1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧఘ")]):
            return None
          return bstack1llll1l1l1_opy_[bstack11lll1_opy_ (u"ࠪ࡭ࡩ࠭ఙ")]
      except Exception as e:
        logger.debug(bstack11lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡶࡪࡧࡤࡪࡰࡪࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࠦࡦࡪ࡮ࡨ࠾ࠥࢁࡽࠨచ").format(str(e)))
    return None
  bstack11ll1lll11_opy_ = os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠬࢄࠧఛ")), bstack11lll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭జ"), bstack11lll1_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨఝ"))
  lock_file = bstack11ll1lll11_opy_ + bstack11lll1_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧఞ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack11ll1lll11_opy_):
        with open(bstack11ll1lll11_opy_, bstack11lll1_opy_ (u"ࠩࡵࠫట")) as f:
          content = f.read().strip()
          if content:
            bstack111l1111l1_opy_ = json.loads(content)
            if md5_hash in bstack111l1111l1_opy_:
              bstack1llll1l1l1_opy_ = bstack111l1111l1_opy_[md5_hash]
              bstack11lll1ll1l_opy_ = datetime.datetime.now()
              bstack1ll11111ll_opy_ = datetime.datetime.strptime(bstack1llll1l1l1_opy_[bstack11lll1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ఠ")], bstack11lll1_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨడ"))
              if (bstack11lll1ll1l_opy_ - bstack1ll11111ll_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack1llll1l1l1_opy_[bstack11lll1_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪఢ")]):
                return None
              return bstack1llll1l1l1_opy_[bstack11lll1_opy_ (u"࠭ࡩࡥࠩణ")]
      return None
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡷࡪࡶ࡫ࠤ࡫࡯࡬ࡦࠢ࡯ࡳࡨࡱࡩ࡯ࡩࠣࡪࡴࡸࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩ࠼ࠣࡿࢂ࠭త").format(str(e)))
    return None
def bstack1l1l1l11ll_opy_(md5_hash, bstack11lll1l1l_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫథ"))
    bstack111l11l1l_opy_ = os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠩࢁࠫద")), bstack11lll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪధ"))
    if not os.path.exists(bstack111l11l1l_opy_):
      os.makedirs(bstack111l11l1l_opy_)
    bstack11ll1lll11_opy_ = os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠫࢃ࠭న")), bstack11lll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ఩"), bstack11lll1_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧప"))
    bstack11l1l1l11l_opy_ = {
      bstack11lll1_opy_ (u"ࠧࡪࡦࠪఫ"): bstack11lll1l1l_opy_,
      bstack11lll1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫబ"): datetime.datetime.strftime(datetime.datetime.now(), bstack11lll1_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭భ")),
      bstack11lll1_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨమ"): str(__version__)
    }
    try:
      bstack111l1111l1_opy_ = {}
      if os.path.exists(bstack11ll1lll11_opy_):
        bstack111l1111l1_opy_ = json.load(open(bstack11ll1lll11_opy_, bstack11lll1_opy_ (u"ࠫࡷࡨࠧయ")))
      bstack111l1111l1_opy_[md5_hash] = bstack11l1l1l11l_opy_
      with open(bstack11ll1lll11_opy_, bstack11lll1_opy_ (u"ࠧࡽࠫࠣర")) as outfile:
        json.dump(bstack111l1111l1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11lll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰࡥࡣࡷ࡭ࡳ࡭ࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩࠢࡩ࡭ࡱ࡫࠺ࠡࡽࢀࠫఱ").format(str(e)))
    return
  bstack111l11l1l_opy_ = os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠧࡿࠩల")), bstack11lll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨళ"))
  if not os.path.exists(bstack111l11l1l_opy_):
    os.makedirs(bstack111l11l1l_opy_)
  bstack11ll1lll11_opy_ = os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠩࢁࠫఴ")), bstack11lll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪవ"), bstack11lll1_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬశ"))
  lock_file = bstack11ll1lll11_opy_ + bstack11lll1_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫష")
  bstack11l1l1l11l_opy_ = {
    bstack11lll1_opy_ (u"࠭ࡩࡥࠩస"): bstack11lll1l1l_opy_,
    bstack11lll1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪహ"): datetime.datetime.strftime(datetime.datetime.now(), bstack11lll1_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬ఺")),
    bstack11lll1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ఻"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack111l1111l1_opy_ = {}
      if os.path.exists(bstack11ll1lll11_opy_):
        with open(bstack11ll1lll11_opy_, bstack11lll1_opy_ (u"ࠪࡶ఼ࠬ")) as f:
          content = f.read().strip()
          if content:
            bstack111l1111l1_opy_ = json.loads(content)
      bstack111l1111l1_opy_[md5_hash] = bstack11l1l1l11l_opy_
      with open(bstack11ll1lll11_opy_, bstack11lll1_opy_ (u"ࠦࡼࠨఽ")) as outfile:
        json.dump(bstack111l1111l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡼ࡯ࡴࡩࠢࡩ࡭ࡱ࡫ࠠ࡭ࡱࡦ࡯࡮ࡴࡧࠡࡨࡲࡶࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮ࠠࡶࡲࡧࡥࡹ࡫࠺ࠡࡽࢀࠫా").format(str(e)))
def bstack11111l1l1l_opy_(self):
  return
def bstack11111llll1_opy_(self):
  return
def bstack1111l1llll_opy_():
  global bstack111l111l11_opy_
  bstack111l111l11_opy_ = True
@measure(event_name=EVENTS.bstack111lll1l11_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack111lll11l_opy_(self):
  global bstack11lll1l11l_opy_
  global bstack111l1l1l1l_opy_
  global bstack1l1ll11ll1_opy_
  try:
    if bstack11lll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ి") in bstack11lll1l11l_opy_ and self.session_id != None and bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫీ"), bstack11lll1_opy_ (u"ࠨࠩు")) != bstack11lll1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪూ"):
      bstack11l1l1l1ll_opy_ = bstack11lll1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪృ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫౄ")
      if bstack11l1l1l1ll_opy_ == bstack11lll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ౅"):
        bstack1l11l11l1l_opy_(logger)
      if self != None:
        bstack1lllll1l1l_opy_(self, bstack11l1l1l1ll_opy_, bstack11lll1_opy_ (u"࠭ࠬࠡࠩె").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11lll1_opy_ (u"ࠧࠨే")
    if bstack11lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨై") in bstack11lll1l11l_opy_ and getattr(threading.current_thread(), bstack11lll1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ౉"), None):
      bstack1lllllll1_opy_.bstack1lllll1ll_opy_(self, bstack1l111l1l11_opy_, logger, wait=True)
    if bstack11lll1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪొ") in bstack11lll1l11l_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1lllll1l1l_opy_(self, bstack11lll1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦో"))
      bstack1l1l1l11l1_opy_.bstack1ll111l11l_opy_(self)
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨౌ") + str(e))
  bstack1l1ll11ll1_opy_(self)
  self.session_id = None
def bstack111lllll1_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1lllllll11_opy_
    global bstack11lll1l11l_opy_
    command_executor = kwargs.get(bstack11lll1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ్ࠩ"), bstack11lll1_opy_ (u"ࠧࠨ౎"))
    bstack1l1111l1ll_opy_ = False
    if type(command_executor) == str and bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ౏") in command_executor:
      bstack1l1111l1ll_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ౐") in str(getattr(command_executor, bstack11lll1_opy_ (u"ࠪࡣࡺࡸ࡬ࠨ౑"), bstack11lll1_opy_ (u"ࠫࠬ౒"))):
      bstack1l1111l1ll_opy_ = True
    else:
      kwargs = bstack111ll11l_opy_.bstack111lll1ll_opy_(bstack11l1l111l1_opy_=kwargs, config=CONFIG)
      return bstack1111lll1ll_opy_(self, *args, **kwargs)
    if bstack1l1111l1ll_opy_:
      bstack111111l11l_opy_ = bstack11l11l11ll_opy_.bstack1l1l11l11_opy_(CONFIG, bstack11lll1l11l_opy_)
      if kwargs.get(bstack11lll1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭౓")):
        kwargs[bstack11lll1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ౔")] = bstack1lllllll11_opy_(kwargs[bstack11lll1_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨౕ")], bstack11lll1l11l_opy_, CONFIG, bstack111111l11l_opy_)
      elif kwargs.get(bstack11lll1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨౖ")):
        kwargs[bstack11lll1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ౗")] = bstack1lllllll11_opy_(kwargs[bstack11lll1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪౘ")], bstack11lll1l11l_opy_, CONFIG, bstack111111l11l_opy_)
  except Exception as e:
    logger.error(bstack11lll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦౙ").format(str(e)))
  return bstack1111lll1ll_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack11lll11l1_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack11lll111ll_opy_(self, command_executor=bstack11lll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴࠷࠲࠸࠰࠳࠲࠵࠴࠱࠻࠶࠷࠸࠹ࠨౚ"), *args, **kwargs):
  global bstack111l1l1l1l_opy_
  global bstack1l1l11l11l_opy_
  bstack1lll111lll_opy_ = bstack111lllll1_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1ll11l11_opy_.on():
    return bstack1lll111lll_opy_
  try:
    logger.debug(bstack11lll1_opy_ (u"࠭ࡃࡰ࡯ࡰࡥࡳࡪࠠࡆࡺࡨࡧࡺࡺ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡦࡢ࡮ࡶࡩࠥ࠳ࠠࡼࡿࠪ౛").format(str(command_executor)))
    logger.debug(bstack11lll1_opy_ (u"ࠧࡉࡷࡥࠤ࡚ࡘࡌࠡ࡫ࡶࠤ࠲ࠦࡻࡾࠩ౜").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫౝ") in command_executor._url:
      bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ౞"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭౟") in command_executor):
    bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬౠ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1l1111l11l_opy_ = getattr(threading.current_thread(), bstack11lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭ౡ"), None)
  bstack1ll1ll1l1l_opy_ = {}
  if self.capabilities is not None:
    bstack1ll1ll1l1l_opy_[bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬౢ")] = self.capabilities.get(bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬౣ"))
    bstack1ll1ll1l1l_opy_[bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ౤")] = self.capabilities.get(bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ౥"))
    bstack1ll1ll1l1l_opy_[bstack11lll1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡢࡳࡵࡺࡩࡰࡰࡶࠫ౦")] = self.capabilities.get(bstack11lll1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ౧"))
  if CONFIG.get(bstack11lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ౨"), False) and bstack111ll11l_opy_.bstack11l1ll11l_opy_(bstack1ll1ll1l1l_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack11lll1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭౩") in bstack11lll1l11l_opy_ or bstack11lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭౪") in bstack11lll1l11l_opy_:
    bstack1ll1l11l_opy_.bstack111llll11l_opy_(self)
  if bstack11lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ౫") in bstack11lll1l11l_opy_ and bstack1l1111l11l_opy_ and bstack1l1111l11l_opy_.get(bstack11lll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ౬"), bstack11lll1_opy_ (u"ࠪࠫ౭")) == bstack11lll1_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ౮"):
    bstack1ll1l11l_opy_.bstack111llll11l_opy_(self)
  bstack111l1l1l1l_opy_ = self.session_id
  with bstack11111l111_opy_:
    bstack1l1l11l11l_opy_.append(self)
  return bstack1lll111lll_opy_
def bstack1ll1ll111l_opy_(args):
  return bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷ࠭౯") in str(args)
def bstack111ll1lll_opy_(self, driver_command, *args, **kwargs):
  global bstack1l11lll1l_opy_
  global bstack1111l11111_opy_
  bstack11ll11l11_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ౰"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack11lll1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭౱"), None)
  bstack1111l1l1l1_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ౲"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack11lll1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ౳"), None)
  bstack1l1ll1l1l_opy_ = getattr(self, bstack11lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ౴"), None) != None and getattr(self, bstack11lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ౵"), None) == True
  if not bstack1111l11111_opy_ and bstack11lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ౶") in CONFIG and CONFIG[bstack11lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭౷")] == True and bstack11ll1111l_opy_.bstack1l11l11l1_opy_(driver_command) and (bstack1l1ll1l1l_opy_ or bstack11ll11l11_opy_ or bstack1111l1l1l1_opy_) and not bstack1ll1ll111l_opy_(args):
    try:
      bstack1111l11111_opy_ = True
      logger.debug(bstack11lll1_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡻࡾࠩ౸").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11lll1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵ࡫ࡲࡧࡱࡵࡱࠥࡹࡣࡢࡰࠣࡿࢂ࠭౹").format(str(err)))
    bstack1111l11111_opy_ = False
  response = bstack1l11lll1l_opy_(self, driver_command, *args, **kwargs)
  if (bstack11lll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ౺") in str(bstack11lll1l11l_opy_).lower() or bstack11lll1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ౻") in str(bstack11lll1l11l_opy_).lower()) and bstack1ll11l11_opy_.on():
    try:
      if driver_command == bstack11lll1_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨ౼"):
        bstack1ll1l11l_opy_.bstack111ll11lll_opy_({
            bstack11lll1_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫ౽"): response[bstack11lll1_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬ౾")],
            bstack11lll1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ౿"): bstack1ll1l11l_opy_.current_test_uuid() if bstack1ll1l11l_opy_.current_test_uuid() else bstack1ll11l11_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1lll11111l_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack111lllll11_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack111l1l1l1l_opy_
  global bstack11l111111_opy_
  global bstack1l11llll1_opy_
  global bstack1l1111111_opy_
  global bstack1lll1lllll_opy_
  global bstack11lll1l11l_opy_
  global bstack1111lll1ll_opy_
  global bstack1l1l11l11l_opy_
  global bstack111l111111_opy_
  global bstack1l111l1l11_opy_
  if os.getenv(bstack11lll1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ಀ")) is not None and bstack111ll11l_opy_.bstack11lll1lll_opy_(CONFIG) is None:
    CONFIG[bstack11lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩಁ")] = True
  CONFIG[bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬಂ")] = str(bstack11lll1l11l_opy_) + str(__version__)
  bstack1l1l1ll1l1_opy_ = os.environ[bstack11lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩಃ")]
  bstack111111l11l_opy_ = bstack11l11l11ll_opy_.bstack1l1l11l11_opy_(CONFIG, bstack11lll1l11l_opy_)
  CONFIG[bstack11lll1_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ಄")] = bstack1l1l1ll1l1_opy_
  CONFIG[bstack11lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨಅ")] = bstack111111l11l_opy_
  if CONFIG.get(bstack11lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧಆ"),bstack11lll1_opy_ (u"ࠨࠩಇ")) and bstack11lll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨಈ") in bstack11lll1l11l_opy_:
    CONFIG[bstack11lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪಉ")].pop(bstack11lll1_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩಊ"), None)
    CONFIG[bstack11lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬಋ")].pop(bstack11lll1_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫಌ"), None)
  command_executor = bstack11lll1lll1_opy_()
  logger.debug(bstack1l1l11111_opy_.format(command_executor))
  proxy = bstack1l11l1lll1_opy_(CONFIG, proxy)
  bstack1lll11ll11_opy_ = 0 if bstack11l111111_opy_ < 0 else bstack11l111111_opy_
  try:
    if bstack1l1111111_opy_ is True:
      bstack1lll11ll11_opy_ = int(multiprocessing.current_process().name)
    elif bstack1lll1lllll_opy_ is True:
      bstack1lll11ll11_opy_ = int(threading.current_thread().name)
  except:
    bstack1lll11ll11_opy_ = 0
  bstack11lll11l1l_opy_ = bstack11lllll111_opy_(CONFIG, bstack1lll11ll11_opy_)
  logger.debug(bstack11llll1ll1_opy_.format(str(bstack11lll11l1l_opy_)))
  if bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ಍") in CONFIG and bstack11lllll1l1_opy_(CONFIG[bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬಎ")]):
    bstack11l11111l_opy_(bstack11lll11l1l_opy_)
  if bstack111ll11l_opy_.bstack1111l11lll_opy_(CONFIG, bstack1lll11ll11_opy_) and bstack111ll11l_opy_.bstack1l11l1111_opy_(bstack11lll11l1l_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack111ll11l_opy_.set_capabilities(bstack11lll11l1l_opy_, CONFIG)
  if desired_capabilities:
    bstack11l111l11_opy_ = bstack11llll1111_opy_(desired_capabilities)
    bstack11l111l11_opy_[bstack11lll1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩಏ")] = bstack1111ll1ll1_opy_(CONFIG)
    bstack111llll111_opy_ = bstack11lllll111_opy_(bstack11l111l11_opy_)
    if bstack111llll111_opy_:
      bstack11lll11l1l_opy_ = update(bstack111llll111_opy_, bstack11lll11l1l_opy_)
    desired_capabilities = None
  if options:
    bstack11ll11lll_opy_(options, bstack11lll11l1l_opy_)
  if not options:
    options = bstack1ll111lll1_opy_(bstack11lll11l1l_opy_)
  bstack1l111l1l11_opy_ = CONFIG.get(bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಐ"))[bstack1lll11ll11_opy_]
  if proxy and bstack11lllll11l_opy_() >= version.parse(bstack11lll1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫ಑")):
    options.proxy(proxy)
  if options and bstack11lllll11l_opy_() >= version.parse(bstack11lll1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫಒ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack11lllll11l_opy_() < version.parse(bstack11lll1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬಓ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack11lll11l1l_opy_)
  logger.info(bstack1llll1l1ll_opy_)
  bstack1111l111l1_opy_.end(EVENTS.bstack1ll11111l1_opy_.value, EVENTS.bstack1ll11111l1_opy_.value + bstack11lll1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢಔ"), EVENTS.bstack1ll11111l1_opy_.value + bstack11lll1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨಕ"), status=True, failure=None, test_name=bstack1l11llll1_opy_)
  if bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡴࡷࡵࡦࡪ࡮ࡨࠫಖ") in kwargs:
    del kwargs[bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡵࡸ࡯ࡧ࡫࡯ࡩࠬಗ")]
  try:
    if bstack11lllll11l_opy_() >= version.parse(bstack11lll1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫಘ")):
      bstack1111lll1ll_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack11lllll11l_opy_() >= version.parse(bstack11lll1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫಙ")):
      bstack1111lll1ll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11lllll11l_opy_() >= version.parse(bstack11lll1_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭ಚ")):
      bstack1111lll1ll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1111lll1ll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack1l1l11l1ll_opy_:
    logger.error(bstack11l111lll_opy_.format(bstack11lll1_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰ࠭ಛ"), str(bstack1l1l11l1ll_opy_)))
    raise bstack1l1l11l1ll_opy_
  if bstack111ll11l_opy_.bstack1111l11lll_opy_(CONFIG, bstack1lll11ll11_opy_) and bstack111ll11l_opy_.bstack1l11l1111_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack11lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪಜ")][bstack11lll1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨಝ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack111ll11l_opy_.set_capabilities(bstack11lll11l1l_opy_, CONFIG)
  try:
    bstack1l1ll11ll_opy_ = bstack11lll1_opy_ (u"ࠪࠫಞ")
    if bstack11lllll11l_opy_() >= version.parse(bstack11lll1_opy_ (u"ࠫ࠹࠴࠰࠯࠲ࡥ࠵ࠬಟ")):
      if self.caps is not None:
        bstack1l1ll11ll_opy_ = self.caps.get(bstack11lll1_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧಠ"))
    else:
      if self.capabilities is not None:
        bstack1l1ll11ll_opy_ = self.capabilities.get(bstack11lll1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨಡ"))
    if bstack1l1ll11ll_opy_:
      bstack1l1111ll1_opy_(bstack1l1ll11ll_opy_)
      if bstack11lllll11l_opy_() <= version.parse(bstack11lll1_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧಢ")):
        self.command_executor._url = bstack11lll1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤಣ") + bstack111111ll1l_opy_ + bstack11lll1_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨತ")
      else:
        self.command_executor._url = bstack11lll1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧಥ") + bstack1l1ll11ll_opy_ + bstack11lll1_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧದ")
      logger.debug(bstack11ll1lll1_opy_.format(bstack1l1ll11ll_opy_))
    else:
      logger.debug(bstack111ll11111_opy_.format(bstack11lll1_opy_ (u"ࠧࡕࡰࡵ࡫ࡰࡥࡱࠦࡈࡶࡤࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠨಧ")))
  except Exception as e:
    logger.debug(bstack111ll11111_opy_.format(e))
  if bstack11lll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬನ") in bstack11lll1l11l_opy_:
    bstack1111llll11_opy_(bstack11l111111_opy_, bstack111l111111_opy_)
  bstack111l1l1l1l_opy_ = self.session_id
  if bstack11lll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ಩") in bstack11lll1l11l_opy_ or bstack11lll1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨಪ") in bstack11lll1l11l_opy_ or bstack11lll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨಫ") in bstack11lll1l11l_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1l1111l11l_opy_ = getattr(threading.current_thread(), bstack11lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫಬ"), None)
  if bstack11lll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫಭ") in bstack11lll1l11l_opy_ or bstack11lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫಮ") in bstack11lll1l11l_opy_:
    bstack1ll1l11l_opy_.bstack111llll11l_opy_(self)
  if bstack11lll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ಯ") in bstack11lll1l11l_opy_ and bstack1l1111l11l_opy_ and bstack1l1111l11l_opy_.get(bstack11lll1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧರ"), bstack11lll1_opy_ (u"ࠨࠩಱ")) == bstack11lll1_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪಲ"):
    bstack1ll1l11l_opy_.bstack111llll11l_opy_(self)
  with bstack11111l111_opy_:
    bstack1l1l11l11l_opy_.append(self)
  if bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಳ") in CONFIG and bstack11lll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ಴") in CONFIG[bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨವ")][bstack1lll11ll11_opy_]:
    bstack1l11llll1_opy_ = CONFIG[bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಶ")][bstack1lll11ll11_opy_][bstack11lll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬಷ")]
  logger.debug(bstack1l11l11lll_opy_.format(bstack111l1l1l1l_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1ll1ll1ll1_opy_
    def bstack1lll111111_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack111l1ll11l_opy_
      if(bstack11lll1_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࠮࡫ࡵࠥಸ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠩࢁࠫಹ")), bstack11lll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ಺"), bstack11lll1_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭಻")), bstack11lll1_opy_ (u"ࠬࡽ಼ࠧ")) as fp:
          fp.write(bstack11lll1_opy_ (u"ࠨࠢಽ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11lll1_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤಾ")))):
          with open(args[1], bstack11lll1_opy_ (u"ࠨࡴࠪಿ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11lll1_opy_ (u"ࠩࡤࡷࡾࡴࡣࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡣࡳ࡫ࡷࡑࡣࡪࡩ࠭ࡩ࡯࡯ࡶࡨࡼࡹ࠲ࠠࡱࡣࡪࡩࠥࡃࠠࡷࡱ࡬ࡨࠥ࠶ࠩࠨೀ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack11l1l1111l_opy_)
            if bstack11lll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧು") in CONFIG and str(CONFIG[bstack11lll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨೂ")]).lower() != bstack11lll1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫೃ"):
                bstack111l11l111_opy_ = bstack1ll1ll1ll1_opy_()
                bstack1111llllll_opy_ = bstack11lll1_opy_ (u"࠭ࠧࠨࠌ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠏࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࠻ࠋࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࠾ࠎࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࠽ࠍࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࠽ࠍࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࠎ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡱࡧࡵ࡯ࡥ࡫ࠤࡂࠦࡡࡴࡻࡱࡧࠥ࠮࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸ࠯ࠠ࠾ࡀࠣࡿࢀࠐࠠࠡ࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࠎࠥࠦࡴࡳࡻࠣࡿࢀࠐࠠࠡࠢࠣࡧࡦࡶࡳࠡ࠿ࠣࡎࡘࡕࡎ࠯ࡲࡤࡶࡸ࡫ࠨࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷ࠮ࡁࠊࠡࠢࢀࢁࠥࡩࡡࡵࡥ࡫ࠤ࠭࡫ࡸࠪࠢࡾࡿࠏࠦࠠࠡࠢࡦࡳࡳࡹ࡯࡭ࡧ࠱ࡩࡷࡸ࡯ࡳࠪࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠾ࠧ࠲ࠠࡦࡺࠬ࠿ࠏࠦࠠࡾࡿࠍࠤࠥࡸࡥࡵࡷࡵࡲࠥࡧࡷࡢ࡫ࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡨࡵ࡮࡯ࡧࡦࡸ࠭ࢁࡻࠋࠢࠣࠤࠥࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵ࠼ࠣࠫࢀࡩࡤࡱࡗࡵࡰࢂ࠭ࠠࠬࠢࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩ࠭ࠌࠣࠤࠥࠦ࠮࠯࠰࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴࠌࠣࠤࢂࢃࠩ࠼ࠌࢀࢁࡀࠐ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠌࠪࠫࠬೄ").format(bstack111l11l111_opy_=bstack111l11l111_opy_)
            lines.insert(1, bstack1111llllll_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11lll1_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤ೅")), bstack11lll1_opy_ (u"ࠨࡹࠪೆ")) as bstack1ll11l111l_opy_:
              bstack1ll11l111l_opy_.writelines(lines)
        CONFIG[bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫೇ")] = str(bstack11lll1l11l_opy_) + str(__version__)
        bstack1l1l1ll1l1_opy_ = os.environ[bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨೈ")]
        bstack111111l11l_opy_ = bstack11l11l11ll_opy_.bstack1l1l11l11_opy_(CONFIG, bstack11lll1l11l_opy_)
        CONFIG[bstack11lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧ೉")] = bstack1l1l1ll1l1_opy_
        CONFIG[bstack11lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧೊ")] = bstack111111l11l_opy_
        bstack1lll11ll11_opy_ = 0 if bstack11l111111_opy_ < 0 else bstack11l111111_opy_
        try:
          if bstack1l1111111_opy_ is True:
            bstack1lll11ll11_opy_ = int(multiprocessing.current_process().name)
          elif bstack1lll1lllll_opy_ is True:
            bstack1lll11ll11_opy_ = int(threading.current_thread().name)
        except:
          bstack1lll11ll11_opy_ = 0
        CONFIG[bstack11lll1_opy_ (u"ࠨࡵࡴࡧ࡚࠷ࡈࠨೋ")] = False
        CONFIG[bstack11lll1_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨೌ")] = True
        bstack11lll11l1l_opy_ = bstack11lllll111_opy_(CONFIG, bstack1lll11ll11_opy_)
        logger.debug(bstack11llll1ll1_opy_.format(str(bstack11lll11l1l_opy_)))
        if CONFIG.get(bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰ್ࠬ")):
          bstack11l11111l_opy_(bstack11lll11l1l_opy_)
        if bstack11lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ೎") in CONFIG and bstack11lll1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ೏") in CONFIG[bstack11lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ೐")][bstack1lll11ll11_opy_]:
          bstack1l11llll1_opy_ = CONFIG[bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ೑")][bstack1lll11ll11_opy_][bstack11lll1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ೒")]
        args.append(os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠧࡿࠩ೓")), bstack11lll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ೔"), bstack11lll1_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫೕ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack11lll11l1l_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11lll1_opy_ (u"ࠥ࡭ࡳࡪࡥࡹࡡࡥࡷࡹࡧࡣ࡬࠰࡭ࡷࠧೖ"))
      bstack111l1ll11l_opy_ = True
      return bstack1l1ll1111l_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack1llll1ll1l_opy_(self,
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
    global bstack11l111111_opy_
    global bstack1l11llll1_opy_
    global bstack1l1111111_opy_
    global bstack1lll1lllll_opy_
    global bstack11lll1l11l_opy_
    CONFIG[bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭೗")] = str(bstack11lll1l11l_opy_) + str(__version__)
    bstack1l1l1ll1l1_opy_ = os.environ[bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ೘")]
    bstack111111l11l_opy_ = bstack11l11l11ll_opy_.bstack1l1l11l11_opy_(CONFIG, bstack11lll1l11l_opy_)
    CONFIG[bstack11lll1_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩ೙")] = bstack1l1l1ll1l1_opy_
    CONFIG[bstack11lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ೚")] = bstack111111l11l_opy_
    bstack1lll11ll11_opy_ = 0 if bstack11l111111_opy_ < 0 else bstack11l111111_opy_
    try:
      if bstack1l1111111_opy_ is True:
        bstack1lll11ll11_opy_ = int(multiprocessing.current_process().name)
      elif bstack1lll1lllll_opy_ is True:
        bstack1lll11ll11_opy_ = int(threading.current_thread().name)
    except:
      bstack1lll11ll11_opy_ = 0
    CONFIG[bstack11lll1_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ೛")] = True
    bstack11lll11l1l_opy_ = bstack11lllll111_opy_(CONFIG, bstack1lll11ll11_opy_)
    logger.debug(bstack11llll1ll1_opy_.format(str(bstack11lll11l1l_opy_)))
    if CONFIG.get(bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭೜")):
      bstack11l11111l_opy_(bstack11lll11l1l_opy_)
    if bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ೝ") in CONFIG and bstack11lll1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩೞ") in CONFIG[bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ೟")][bstack1lll11ll11_opy_]:
      bstack1l11llll1_opy_ = CONFIG[bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩೠ")][bstack1lll11ll11_opy_][bstack11lll1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬೡ")]
    import urllib
    import json
    if bstack11lll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬೢ") in CONFIG and str(CONFIG[bstack11lll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ೣ")]).lower() != bstack11lll1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ೤"):
        bstack1l1l111l1l_opy_ = bstack1ll1ll1ll1_opy_()
        bstack111l11l111_opy_ = bstack1l1l111l1l_opy_ + urllib.parse.quote(json.dumps(bstack11lll11l1l_opy_))
    else:
        bstack111l11l111_opy_ = bstack11lll1_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭೥") + urllib.parse.quote(json.dumps(bstack11lll11l1l_opy_))
    browser = self.connect(bstack111l11l111_opy_)
    return browser
except Exception as e:
    pass
def bstack11ll11llll_opy_():
    global bstack111l1ll11l_opy_
    global bstack11lll1l11l_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1111l11l11_opy_
        global bstack1lll1l11l_opy_
        if not bstack11ll11lll1_opy_:
          global bstack111lll1l1l_opy_
          if not bstack111lll1l1l_opy_:
            from bstack_utils.helper import bstack11l1l1l11_opy_, bstack111l1lll11_opy_, bstack11lll11ll_opy_
            bstack111lll1l1l_opy_ = bstack11l1l1l11_opy_()
            bstack111l1lll11_opy_(bstack11lll1l11l_opy_)
            bstack111111l11l_opy_ = bstack11l11l11ll_opy_.bstack1l1l11l11_opy_(CONFIG, bstack11lll1l11l_opy_)
            bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"ࠧࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡓࡖࡔࡊࡕࡄࡖࡢࡑࡆࡖࠢ೦"), bstack111111l11l_opy_)
          BrowserType.connect = bstack1111l11l11_opy_
          return
        BrowserType.launch = bstack1llll1ll1l_opy_
        bstack111l1ll11l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1lll111111_opy_
      bstack111l1ll11l_opy_ = True
    except Exception as e:
      pass
def bstack111l1ll1l_opy_(context, bstack1l11lll11_opy_):
  try:
    context.page.evaluate(bstack11lll1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢ೧"), bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫ೨")+ json.dumps(bstack1l11lll11_opy_) + bstack11lll1_opy_ (u"ࠣࡿࢀࠦ೩"))
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃ࠺ࠡࡽࢀࠦ೪").format(str(e), traceback.format_exc()))
def bstack1111ll11ll_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11lll1_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ೫"), bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ೬") + json.dumps(message) + bstack11lll1_opy_ (u"ࠬ࠲ࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠨ೭") + json.dumps(level) + bstack11lll1_opy_ (u"࠭ࡽࡾࠩ೮"))
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠠࡼࡿ࠽ࠤࢀࢃࠢ೯").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack11l11lll11_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack1l11l1l11l_opy_(self, url):
  global bstack11l11ll1ll_opy_
  try:
    bstack111l1l1lll_opy_(url)
  except Exception as err:
    logger.debug(bstack1111l1l1ll_opy_.format(str(err)))
  try:
    bstack11l11ll1ll_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1l1ll1ll11_opy_):
        bstack111l1l1lll_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1111l1l1ll_opy_.format(str(err)))
    raise e
def bstack11lll11l11_opy_(self):
  global bstack111111ll11_opy_
  bstack111111ll11_opy_ = self
  return
def bstack11lllll1l_opy_(self):
  global bstack1llll11lll_opy_
  bstack1llll11lll_opy_ = self
  return
def bstack111l1l1ll1_opy_(test_name, bstack111l1l11l_opy_):
  global CONFIG
  if percy.bstack1l1l1lllll_opy_() == bstack11lll1_opy_ (u"ࠣࡶࡵࡹࡪࠨ೰"):
    bstack1ll1111l1_opy_ = os.path.relpath(bstack111l1l11l_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1ll1111l1_opy_)
    bstack1lll11l1l1_opy_ = suite_name + bstack11lll1_opy_ (u"ࠤ࠰ࠦೱ") + test_name
    threading.current_thread().percySessionName = bstack1lll11l1l1_opy_
def bstack111l1lll1_opy_(self, test, *args, **kwargs):
  global bstack11111l1lll_opy_
  test_name = None
  bstack111l1l11l_opy_ = None
  if test:
    test_name = str(test.name)
    bstack111l1l11l_opy_ = str(test.source)
  bstack111l1l1ll1_opy_(test_name, bstack111l1l11l_opy_)
  bstack11111l1lll_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1lll1l11l1_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack111l11l11l_opy_(driver, bstack1lll11l1l1_opy_):
  if not bstack111ll11l1_opy_ and bstack1lll11l1l1_opy_:
      bstack1111l1l111_opy_ = {
          bstack11lll1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪೲ"): bstack11lll1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬೳ"),
          bstack11lll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ೴"): {
              bstack11lll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ೵"): bstack1lll11l1l1_opy_
          }
      }
      bstack111llll1ll_opy_ = bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ೶").format(json.dumps(bstack1111l1l111_opy_))
      driver.execute_script(bstack111llll1ll_opy_)
  if bstack111ll1l1ll_opy_:
      bstack111l1l1111_opy_ = {
          bstack11lll1_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨ೷"): bstack11lll1_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫ೸"),
          bstack11lll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭೹"): {
              bstack11lll1_opy_ (u"ࠫࡩࡧࡴࡢࠩ೺"): bstack1lll11l1l1_opy_ + bstack11lll1_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩࠧࠧ೻"),
              bstack11lll1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ೼"): bstack11lll1_opy_ (u"ࠧࡪࡰࡩࡳࠬ೽")
          }
      }
      if bstack111ll1l1ll_opy_.status == bstack11lll1_opy_ (u"ࠨࡒࡄࡗࡘ࠭೾"):
          bstack111llll11_opy_ = bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧ೿").format(json.dumps(bstack111l1l1111_opy_))
          driver.execute_script(bstack111llll11_opy_)
          bstack1lllll1l1l_opy_(driver, bstack11lll1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪഀ"))
      elif bstack111ll1l1ll_opy_.status == bstack11lll1_opy_ (u"ࠫࡋࡇࡉࡍࠩഁ"):
          reason = bstack11lll1_opy_ (u"ࠧࠨം")
          bstack11111lll1l_opy_ = bstack1lll11l1l1_opy_ + bstack11lll1_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠧഃ")
          if bstack111ll1l1ll_opy_.message:
              reason = str(bstack111ll1l1ll_opy_.message)
              bstack11111lll1l_opy_ = bstack11111lll1l_opy_ + bstack11lll1_opy_ (u"ࠧࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶ࠿ࠦࠧഄ") + reason
          bstack111l1l1111_opy_[bstack11lll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫഅ")] = {
              bstack11lll1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨആ"): bstack11lll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩഇ"),
              bstack11lll1_opy_ (u"ࠫࡩࡧࡴࡢࠩഈ"): bstack11111lll1l_opy_
          }
          bstack111llll11_opy_ = bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪഉ").format(json.dumps(bstack111l1l1111_opy_))
          driver.execute_script(bstack111llll11_opy_)
          bstack1lllll1l1l_opy_(driver, bstack11lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ഊ"), reason)
          bstack1ll111l111_opy_(reason, str(bstack111ll1l1ll_opy_), str(bstack11l111111_opy_), logger)
@measure(event_name=EVENTS.bstack1ll1l1ll1l_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack11l1ll1111_opy_(driver, test):
  if percy.bstack1l1l1lllll_opy_() == bstack11lll1_opy_ (u"ࠢࡵࡴࡸࡩࠧഋ") and percy.bstack11l1l11l1_opy_() == bstack11lll1_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥഌ"):
      bstack1l111l11l_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ഍"), None)
      bstack1l11ll1ll_opy_(driver, bstack1l111l11l_opy_, test)
  if (bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧഎ"), None) and
      bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪഏ"), None)) or (
      bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬഐ"), None) and
      bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ഑"), None)):
      logger.info(bstack11lll1_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠦࠢഒ"))
      bstack111ll11l_opy_.bstack1lll1lll1_opy_(driver, name=test.name, path=test.source)
def bstack11llllll1l_opy_(test, bstack1lll11l1l1_opy_):
    try:
      bstack11l11lll1l_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack11lll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ഓ")] = bstack1lll11l1l1_opy_
      if bstack111ll1l1ll_opy_:
        if bstack111ll1l1ll_opy_.status == bstack11lll1_opy_ (u"ࠩࡓࡅࡘ࡙ࠧഔ"):
          data[bstack11lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪക")] = bstack11lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫഖ")
        elif bstack111ll1l1ll_opy_.status == bstack11lll1_opy_ (u"ࠬࡌࡁࡊࡎࠪഗ"):
          data[bstack11lll1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ഘ")] = bstack11lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧങ")
          if bstack111ll1l1ll_opy_.message:
            data[bstack11lll1_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨച")] = str(bstack111ll1l1ll_opy_.message)
      user = CONFIG[bstack11lll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫഛ")]
      key = CONFIG[bstack11lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ജ")]
      host = bstack111ll111ll_opy_(cli.config, [bstack11lll1_opy_ (u"ࠦࡦࡶࡩࡴࠤഝ"), bstack11lll1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢഞ"), bstack11lll1_opy_ (u"ࠨࡡࡱ࡫ࠥട")], bstack11lll1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠣഠ"))
      url = bstack11lll1_opy_ (u"ࠨࡽࢀ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠰ࡽࢀ࠲࡯ࡹ࡯࡯ࠩഡ").format(host, bstack111l1l1l1l_opy_)
      headers = {
        bstack11lll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨഢ"): bstack11lll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ണ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1lllll11ll_opy_(bstack11lll1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡸࡴࡩࡧࡴࡦࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡷࡥࡹࡻࡳࠣത"), datetime.datetime.now() - bstack11l11lll1l_opy_)
    except Exception as e:
      logger.error(bstack1ll1l111l1_opy_.format(str(e)))
def bstack1ll1l11ll1_opy_(test, bstack1lll11l1l1_opy_):
  global CONFIG
  global bstack1llll11lll_opy_
  global bstack111111ll11_opy_
  global bstack111l1l1l1l_opy_
  global bstack111ll1l1ll_opy_
  global bstack1l11llll1_opy_
  global bstack1llll1l111_opy_
  global bstack111ll1111_opy_
  global bstack1lll1l1lll_opy_
  global bstack1ll1ll1ll_opy_
  global bstack1l1l11l11l_opy_
  global bstack1l111l1l11_opy_
  global bstack1l11ll11l_opy_
  try:
    if not bstack111l1l1l1l_opy_:
      with bstack1l11ll11l_opy_:
        bstack1l1l11ll11_opy_ = os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠬࢄࠧഥ")), bstack11lll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ദ"), bstack11lll1_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩധ"))
        if os.path.exists(bstack1l1l11ll11_opy_):
          with open(bstack1l1l11ll11_opy_, bstack11lll1_opy_ (u"ࠨࡴࠪന")) as f:
            content = f.read().strip()
            if content:
              bstack1l11ll1l11_opy_ = json.loads(bstack11lll1_opy_ (u"ࠤࡾࠦഩ") + content + bstack11lll1_opy_ (u"ࠪࠦࡽࠨ࠺ࠡࠤࡼࠦࠬപ") + bstack11lll1_opy_ (u"ࠦࢂࠨഫ"))
              bstack111l1l1l1l_opy_ = bstack1l11ll1l11_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࡵࠣࡪ࡮ࡲࡥ࠻ࠢࠪബ") + str(e))
  if bstack1l1l11l11l_opy_:
    with bstack11111l111_opy_:
      bstack111lll1ll1_opy_ = bstack1l1l11l11l_opy_.copy()
    for driver in bstack111lll1ll1_opy_:
      if bstack111l1l1l1l_opy_ == driver.session_id:
        if test:
          bstack11l1ll1111_opy_(driver, test)
        bstack111l11l11l_opy_(driver, bstack1lll11l1l1_opy_)
  elif bstack111l1l1l1l_opy_:
    bstack11llllll1l_opy_(test, bstack1lll11l1l1_opy_)
  if bstack1llll11lll_opy_:
    bstack111ll1111_opy_(bstack1llll11lll_opy_)
  if bstack111111ll11_opy_:
    bstack1lll1l1lll_opy_(bstack111111ll11_opy_)
  if bstack111l111l11_opy_:
    bstack1ll1ll1ll_opy_()
def bstack1l1111ll11_opy_(self, test, *args, **kwargs):
  bstack1lll11l1l1_opy_ = None
  if test:
    bstack1lll11l1l1_opy_ = str(test.name)
  bstack1ll1l11ll1_opy_(test, bstack1lll11l1l1_opy_)
  bstack1llll1l111_opy_(self, test, *args, **kwargs)
def bstack1ll11lll1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1l1l11l1l1_opy_
  global CONFIG
  global bstack1l1l11l11l_opy_
  global bstack111l1l1l1l_opy_
  global bstack1l11ll11l_opy_
  bstack11l1l1l1l1_opy_ = None
  try:
    if bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬഭ"), None) or bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩമ"), None):
      try:
        if not bstack111l1l1l1l_opy_:
          bstack1l1l11ll11_opy_ = os.path.join(os.path.expanduser(bstack11lll1_opy_ (u"ࠨࢀࠪയ")), bstack11lll1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩര"), bstack11lll1_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬറ"))
          with bstack1l11ll11l_opy_:
            if os.path.exists(bstack1l1l11ll11_opy_):
              with open(bstack1l1l11ll11_opy_, bstack11lll1_opy_ (u"ࠫࡷ࠭ല")) as f:
                content = f.read().strip()
                if content:
                  bstack1l11ll1l11_opy_ = json.loads(bstack11lll1_opy_ (u"ࠧࢁࠢള") + content + bstack11lll1_opy_ (u"࠭ࠢࡹࠤ࠽ࠤࠧࡿࠢࠨഴ") + bstack11lll1_opy_ (u"ࠢࡾࠤവ"))
                  bstack111l1l1l1l_opy_ = bstack1l11ll1l11_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack11lll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡌࡈࡸࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠧശ") + str(e))
      if bstack1l1l11l11l_opy_:
        with bstack11111l111_opy_:
          bstack111lll1ll1_opy_ = bstack1l1l11l11l_opy_.copy()
        for driver in bstack111lll1ll1_opy_:
          if bstack111l1l1l1l_opy_ == driver.session_id:
            bstack11l1l1l1l1_opy_ = driver
    bstack11ll111l11_opy_ = bstack111ll11l_opy_.bstack11111l1ll_opy_(test.tags)
    if bstack11l1l1l1l1_opy_:
      threading.current_thread().isA11yTest = bstack111ll11l_opy_.bstack1l11ll1l1_opy_(bstack11l1l1l1l1_opy_, bstack11ll111l11_opy_)
      threading.current_thread().isAppA11yTest = bstack111ll11l_opy_.bstack1l11ll1l1_opy_(bstack11l1l1l1l1_opy_, bstack11ll111l11_opy_)
    else:
      threading.current_thread().isA11yTest = bstack11ll111l11_opy_
      threading.current_thread().isAppA11yTest = bstack11ll111l11_opy_
  except:
    pass
  bstack1l1l11l1l1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack111ll1l1ll_opy_
  try:
    bstack111ll1l1ll_opy_ = self._test
  except:
    bstack111ll1l1ll_opy_ = self.test
def bstack111l1ll11_opy_():
  global bstack1ll1l11l1l_opy_
  try:
    if os.path.exists(bstack1ll1l11l1l_opy_):
      os.remove(bstack1ll1l11l1l_opy_)
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬഷ") + str(e))
def bstack1l111l1lll_opy_():
  global bstack1ll1l11l1l_opy_
  bstack11ll11111_opy_ = {}
  lock_file = bstack1ll1l11l1l_opy_ + bstack11lll1_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩസ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11lll1_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧഹ"))
    try:
      if not os.path.isfile(bstack1ll1l11l1l_opy_):
        with open(bstack1ll1l11l1l_opy_, bstack11lll1_opy_ (u"ࠬࡽࠧഺ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1ll1l11l1l_opy_):
        with open(bstack1ll1l11l1l_opy_, bstack11lll1_opy_ (u"࠭ࡲࠨ഻")) as f:
          content = f.read().strip()
          if content:
            bstack11ll11111_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack11lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺഼ࠡࠩ") + str(e))
    return bstack11ll11111_opy_
  try:
    os.makedirs(os.path.dirname(bstack1ll1l11l1l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack1ll1l11l1l_opy_):
        with open(bstack1ll1l11l1l_opy_, bstack11lll1_opy_ (u"ࠨࡹࠪഽ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1ll1l11l1l_opy_):
        with open(bstack1ll1l11l1l_opy_, bstack11lll1_opy_ (u"ࠩࡵࠫാ")) as f:
          content = f.read().strip()
          if content:
            bstack11ll11111_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬി") + str(e))
  finally:
    return bstack11ll11111_opy_
def bstack1111llll11_opy_(platform_index, item_index):
  global bstack1ll1l11l1l_opy_
  lock_file = bstack1ll1l11l1l_opy_ + bstack11lll1_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪീ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11lll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨു"))
    try:
      bstack11ll11111_opy_ = {}
      if os.path.exists(bstack1ll1l11l1l_opy_):
        with open(bstack1ll1l11l1l_opy_, bstack11lll1_opy_ (u"࠭ࡲࠨൂ")) as f:
          content = f.read().strip()
          if content:
            bstack11ll11111_opy_ = json.loads(content)
      bstack11ll11111_opy_[item_index] = platform_index
      with open(bstack1ll1l11l1l_opy_, bstack11lll1_opy_ (u"ࠢࡸࠤൃ")) as outfile:
        json.dump(bstack11ll11111_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11lll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡻࡷ࡯ࡴࡪࡰࡪࠤࡹࡵࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ൄ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack1ll1l11l1l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack11ll11111_opy_ = {}
      if os.path.exists(bstack1ll1l11l1l_opy_):
        with open(bstack1ll1l11l1l_opy_, bstack11lll1_opy_ (u"ࠩࡵࠫ൅")) as f:
          content = f.read().strip()
          if content:
            bstack11ll11111_opy_ = json.loads(content)
      bstack11ll11111_opy_[item_index] = platform_index
      with open(bstack1ll1l11l1l_opy_, bstack11lll1_opy_ (u"ࠥࡻࠧെ")) as outfile:
        json.dump(bstack11ll11111_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡷࡳ࡫ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩേ") + str(e))
def bstack111l11l11_opy_(bstack1l1l1l1l1_opy_):
  global CONFIG
  bstack1lll1l1ll1_opy_ = bstack11lll1_opy_ (u"ࠬ࠭ൈ")
  if not bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ൉") in CONFIG:
    logger.info(bstack11lll1_opy_ (u"ࠧࡏࡱࠣࡴࡱࡧࡴࡧࡱࡵࡱࡸࠦࡰࡢࡵࡶࡩࡩࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫ࡵࡲࠡࡔࡲࡦࡴࡺࠠࡳࡷࡱࠫൊ"))
  try:
    platform = CONFIG[bstack11lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫോ")][bstack1l1l1l1l1_opy_]
    if bstack11lll1_opy_ (u"ࠩࡲࡷࠬൌ") in platform:
      bstack1lll1l1ll1_opy_ += str(platform[bstack11lll1_opy_ (u"ࠪࡳࡸ്࠭")]) + bstack11lll1_opy_ (u"ࠫ࠱ࠦࠧൎ")
    if bstack11lll1_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ൏") in platform:
      bstack1lll1l1ll1_opy_ += str(platform[bstack11lll1_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ൐")]) + bstack11lll1_opy_ (u"ࠧ࠭ࠢࠪ൑")
    if bstack11lll1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ൒") in platform:
      bstack1lll1l1ll1_opy_ += str(platform[bstack11lll1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭൓")]) + bstack11lll1_opy_ (u"ࠪ࠰ࠥ࠭ൔ")
    if bstack11lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ൕ") in platform:
      bstack1lll1l1ll1_opy_ += str(platform[bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧൖ")]) + bstack11lll1_opy_ (u"࠭ࠬࠡࠩൗ")
    if bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ൘") in platform:
      bstack1lll1l1ll1_opy_ += str(platform[bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭൙")]) + bstack11lll1_opy_ (u"ࠩ࠯ࠤࠬ൚")
    if bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ൛") in platform:
      bstack1lll1l1ll1_opy_ += str(platform[bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ൜")]) + bstack11lll1_opy_ (u"ࠬ࠲ࠠࠨ൝")
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"࠭ࡓࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡰࡨࡶࡦࡺࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡹࡴࡳ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡵࡩࡵࡵࡲࡵࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡳࡳ࠭൞") + str(e))
  finally:
    if bstack1lll1l1ll1_opy_[len(bstack1lll1l1ll1_opy_) - 2:] == bstack11lll1_opy_ (u"ࠧ࠭ࠢࠪൟ"):
      bstack1lll1l1ll1_opy_ = bstack1lll1l1ll1_opy_[:-2]
    return bstack1lll1l1ll1_opy_
def bstack1111llll1l_opy_(path, bstack1lll1l1ll1_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l111l1111_opy_ = ET.parse(path)
    bstack1lllllll1l_opy_ = bstack1l111l1111_opy_.getroot()
    bstack111l111l1l_opy_ = None
    for suite in bstack1lllllll1l_opy_.iter(bstack11lll1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧൠ")):
      if bstack11lll1_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩൡ") in suite.attrib:
        suite.attrib[bstack11lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨൢ")] += bstack11lll1_opy_ (u"ࠫࠥ࠭ൣ") + bstack1lll1l1ll1_opy_
        bstack111l111l1l_opy_ = suite
    bstack11l111lll1_opy_ = None
    for robot in bstack1lllllll1l_opy_.iter(bstack11lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ൤")):
      bstack11l111lll1_opy_ = robot
    bstack1l111ll11l_opy_ = len(bstack11l111lll1_opy_.findall(bstack11lll1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൥")))
    if bstack1l111ll11l_opy_ == 1:
      bstack11l111lll1_opy_.remove(bstack11l111lll1_opy_.findall(bstack11lll1_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭൦"))[0])
      bstack1ll11l1ll_opy_ = ET.Element(bstack11lll1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧ൧"), attrib={bstack11lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ൨"): bstack11lll1_opy_ (u"ࠪࡗࡺ࡯ࡴࡦࡵࠪ൩"), bstack11lll1_opy_ (u"ࠫ࡮ࡪࠧ൪"): bstack11lll1_opy_ (u"ࠬࡹ࠰ࠨ൫")})
      bstack11l111lll1_opy_.insert(1, bstack1ll11l1ll_opy_)
      bstack1l1lll1l1_opy_ = None
      for suite in bstack11l111lll1_opy_.iter(bstack11lll1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൬")):
        bstack1l1lll1l1_opy_ = suite
      bstack1l1lll1l1_opy_.append(bstack111l111l1l_opy_)
      bstack1l11lllll1_opy_ = None
      for status in bstack111l111l1l_opy_.iter(bstack11lll1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ൭")):
        bstack1l11lllll1_opy_ = status
      bstack1l1lll1l1_opy_.append(bstack1l11lllll1_opy_)
    bstack1l111l1111_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡸࡳࡪࡰࡪࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹ࠭൮") + str(e))
def bstack11l11l1l1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack111111ll1_opy_
  global CONFIG
  if bstack11lll1_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨ൯") in options:
    del options[bstack11lll1_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢ൰")]
  json_data = bstack1l111l1lll_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack11lll1_opy_ (u"ࠫࡵࡧࡢࡰࡶࡢࡶࡪࡹࡵ࡭ࡶࡶࠫ൱"), str(item_id), bstack11lll1_opy_ (u"ࠬࡵࡵࡵࡲࡸࡸ࠳ࡾ࡭࡭ࠩ൲"))
    bstack1111llll1l_opy_(path, bstack111l11l11_opy_(json_data[item_id]))
  bstack111l1ll11_opy_()
  return bstack111111ll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1l1l11ll1l_opy_(self, ff_profile_dir):
  global bstack1ll1ll1111_opy_
  if not ff_profile_dir:
    return None
  return bstack1ll1ll1111_opy_(self, ff_profile_dir)
def bstack1ll111l1ll_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l1111lll1_opy_
  bstack1l1l1l111_opy_ = []
  if bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ൳") in CONFIG:
    bstack1l1l1l111_opy_ = CONFIG[bstack11lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ൴")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11lll1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࠤ൵")],
      pabot_args[bstack11lll1_opy_ (u"ࠤࡹࡩࡷࡨ࡯ࡴࡧࠥ൶")],
      argfile,
      pabot_args.get(bstack11lll1_opy_ (u"ࠥ࡬࡮ࡼࡥࠣ൷")),
      pabot_args[bstack11lll1_opy_ (u"ࠦࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠢ൸")],
      platform[0],
      bstack1l1111lll1_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11lll1_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡦࡪ࡮ࡨࡷࠧ൹")] or [(bstack11lll1_opy_ (u"ࠨࠢൺ"), None)]
    for platform in enumerate(bstack1l1l1l111_opy_)
  ]
def bstack1l11l111l1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1lll1111l1_opy_=bstack11lll1_opy_ (u"ࠧࠨൻ")):
  global bstack111llll1l_opy_
  self.platform_index = platform_index
  self.bstack11ll11ll1l_opy_ = bstack1lll1111l1_opy_
  bstack111llll1l_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack11l111l111_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l11l1l1ll_opy_
  global bstack11l11llll1_opy_
  bstack11ll11ll11_opy_ = copy.deepcopy(item)
  if not bstack11lll1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪർ") in item.options:
    bstack11ll11ll11_opy_.options[bstack11lll1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫൽ")] = []
  bstack11ll11l111_opy_ = bstack11ll11ll11_opy_.options[bstack11lll1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬൾ")].copy()
  for v in bstack11ll11ll11_opy_.options[bstack11lll1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ൿ")]:
    if bstack11lll1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫ඀") in v:
      bstack11ll11l111_opy_.remove(v)
    if bstack11lll1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭ඁ") in v:
      bstack11ll11l111_opy_.remove(v)
    if bstack11lll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫං") in v:
      bstack11ll11l111_opy_.remove(v)
  bstack11ll11l111_opy_.insert(0, bstack11lll1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞࠺ࡼࡿࠪඃ").format(bstack11ll11ll11_opy_.platform_index))
  bstack11ll11l111_opy_.insert(0, bstack11lll1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࡀࡻࡾࠩ඄").format(bstack11ll11ll11_opy_.bstack11ll11ll1l_opy_))
  bstack11ll11ll11_opy_.options[bstack11lll1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬඅ")] = bstack11ll11l111_opy_
  if bstack11l11llll1_opy_:
    bstack11ll11ll11_opy_.options[bstack11lll1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ආ")].insert(0, bstack11lll1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗ࠿ࢁࡽࠨඇ").format(bstack11l11llll1_opy_))
  return bstack1l11l1l1ll_opy_(caller_id, datasources, is_last, bstack11ll11ll11_opy_, outs_dir)
def bstack11l11ll1l_opy_(command, item_index):
  try:
    if bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧඈ")):
      os.environ[bstack11lll1_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨඉ")] = json.dumps(CONFIG[bstack11lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫඊ")][item_index % bstack1l1l111ll1_opy_])
    global bstack11l11llll1_opy_
    if bstack11l11llll1_opy_:
      command[0] = command[0].replace(bstack11lll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨඋ"), bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧඌ") + str(
        item_index) + bstack11lll1_opy_ (u"ࠫࠥ࠭ඍ") + bstack11l11llll1_opy_, 1)
    else:
      command[0] = command[0].replace(bstack11lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫඎ"),
                                      bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡹࡤ࡬ࠢࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠢࠪඏ") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack11lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦ࡭ࡰࡦ࡬ࡪࡾ࡯࡮ࡨࠢࡦࡳࡲࡳࡡ࡯ࡦࠣࡪࡴࡸࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰ࠽ࠤࢀࢃࠧඐ").format(str(e)))
def bstack1ll1111l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack11111ll11l_opy_
  try:
    bstack11l11ll1l_opy_(command, item_index)
    return bstack11111ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack11lll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࡀࠠࡼࡿࠪඑ").format(str(e)))
    raise e
def bstack1lllll1111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack11111ll11l_opy_
  try:
    bstack11l11ll1l_opy_(command, item_index)
    return bstack11111ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack11lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠳࠰࠴࠷࠿ࠦࡻࡾࠩඒ").format(str(e)))
    try:
      return bstack11111ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack11lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࠷࠴࠱࠴ࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨඓ").format(str(e2)))
      raise e
def bstack1ll111l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack11111ll11l_opy_
  try:
    bstack11l11ll1l_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack11111ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack11lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠵࠲࠶࠻࠺ࠡࡽࢀࠫඔ").format(str(e)))
    try:
      return bstack11111ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack11lll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦ࠲࠯࠳࠸ࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪඕ").format(str(e2)))
      raise e
def _1lll1l111l_opy_(bstack11lll1l111_opy_, item_index, process_timeout, sleep_before_start, bstack1l1111l111_opy_):
  bstack11l11ll1l_opy_(bstack11lll1l111_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack11llll11l1_opy_(command, bstack1llll1lll1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11111ll11l_opy_
  try:
    bstack11l11ll1l_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack11111ll11l_opy_(command, bstack1llll1lll1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11lll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠺࠴࠰࠻ࠢࡾࢁࠬඖ").format(str(e)))
    try:
      return bstack11111ll11l_opy_(command, bstack1llll1lll1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧ඗").format(str(e2)))
      raise e
def bstack1111l1111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11111ll11l_opy_
  try:
    process_timeout = _1lll1l111l_opy_(command, item_index, process_timeout, sleep_before_start, bstack11lll1_opy_ (u"ࠨ࠶࠱࠶ࠬ඘"))
    return bstack11111ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠵࠰࠵࠾ࠥࢁࡽࠨ඙").format(str(e)))
    try:
      return bstack11111ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪක").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack1ll1l1l1ll_opy_(self, runner, quiet=False, capture=True):
  global bstack1llllll111_opy_
  bstack11l111l1l1_opy_ = bstack1llllll111_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11lll1_opy_ (u"ࠫࡪࡾࡣࡦࡲࡷ࡭ࡴࡴ࡟ࡢࡴࡵࠫඛ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11lll1_opy_ (u"ࠬ࡫ࡸࡤࡡࡷࡶࡦࡩࡥࡣࡣࡦ࡯ࡤࡧࡲࡳࠩග")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack11l111l1l1_opy_
def bstack111lll1l1_opy_(runner, hook_name, context, element, bstack1lll1llll1_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1111l11l1_opy_.bstack11l111l1_opy_(hook_name, element)
    bstack1lll1llll1_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1111l11l1_opy_.bstack11l1l1ll_opy_(element)
      if hook_name not in [bstack11lll1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪඝ"), bstack11lll1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪඞ")] and args and hasattr(args[0], bstack11lll1_opy_ (u"ࠨࡧࡵࡶࡴࡸ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠨඟ")):
        args[0].error_message = bstack11lll1_opy_ (u"ࠩࠪච")
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡨࡢࡰࡧࡰࡪࠦࡨࡰࡱ࡮ࡷࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥ࠻ࠢࡾࢁࠬඡ").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1ll1l11_opy_, stage=STAGE.bstack11ll1ll11_opy_, hook_type=bstack11lll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡅࡱࡲࠢජ"), bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack1l1ll1ll1_opy_(runner, name, context, bstack1lll1llll1_opy_, *args):
    if runner.hooks.get(bstack11lll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤඣ")).__name__ != bstack11lll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࡢࡨࡪ࡬ࡡࡶ࡮ࡷࡣ࡭ࡵ࡯࡬ࠤඤ"):
      bstack111lll1l1_opy_(runner, name, context, runner, bstack1lll1llll1_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack11lll1111_opy_(bstack11lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ඥ")) else context.browser
      runner.driver_initialised = bstack11lll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧඦ")
    except Exception as e:
      logger.debug(bstack11lll1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡪࠦࡡࡵࡶࡵ࡭ࡧࡻࡴࡦ࠼ࠣࡿࢂ࠭ට").format(str(e)))
def bstack1l1l1l1l1l_opy_(runner, name, context, bstack1lll1llll1_opy_, *args):
    bstack111lll1l1_opy_(runner, name, context, context.feature, bstack1lll1llll1_opy_, *args)
    try:
      if not bstack111ll11l1_opy_:
        bstack11l1l1l1l1_opy_ = threading.current_thread().bstackSessionDriver if bstack11lll1111_opy_(bstack11lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩඨ")) else context.browser
        if is_driver_active(bstack11l1l1l1l1_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack11lll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧඩ")
          bstack1l11lll11_opy_ = str(runner.feature.name)
          bstack111l1ll1l_opy_(context, bstack1l11lll11_opy_)
          bstack11l1l1l1l1_opy_.execute_script(bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪඪ") + json.dumps(bstack1l11lll11_opy_) + bstack11lll1_opy_ (u"࠭ࡽࡾࠩණ"))
    except Exception as e:
      logger.debug(bstack11lll1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧඬ").format(str(e)))
def bstack1lll1lll1l_opy_(runner, name, context, bstack1lll1llll1_opy_, *args):
    if hasattr(context, bstack11lll1_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪත")):
        bstack1111l11l1_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack11lll1_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫථ")) else context.feature
    bstack111lll1l1_opy_(runner, name, context, target, bstack1lll1llll1_opy_, *args)
@measure(event_name=EVENTS.bstack11l1ll11l1_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack11llll1l1_opy_(runner, name, context, bstack1lll1llll1_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1111l11l1_opy_.start_test(context)
    bstack111lll1l1_opy_(runner, name, context, context.scenario, bstack1lll1llll1_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1l1l1l11l1_opy_.bstack11111lll1_opy_(context, *args)
    try:
      bstack11l1l1l1l1_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩද"), context.browser)
      if is_driver_active(bstack11l1l1l1l1_opy_):
        bstack1ll1l11l_opy_.bstack111llll11l_opy_(bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪධ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack11lll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢන")
        if (not bstack111ll11l1_opy_):
          scenario_name = args[0].name
          feature_name = bstack1l11lll11_opy_ = str(runner.feature.name)
          bstack1l11lll11_opy_ = feature_name + bstack11lll1_opy_ (u"࠭ࠠ࠮ࠢࠪ඲") + scenario_name
          if runner.driver_initialised == bstack11lll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤඳ"):
            bstack111l1ll1l_opy_(context, bstack1l11lll11_opy_)
            bstack11l1l1l1l1_opy_.execute_script(bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭ප") + json.dumps(bstack1l11lll11_opy_) + bstack11lll1_opy_ (u"ࠩࢀࢁࠬඵ"))
    except Exception as e:
      logger.debug(bstack11lll1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡦࡰࡤࡶ࡮ࡵ࠺ࠡࡽࢀࠫබ").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1ll1l11_opy_, stage=STAGE.bstack11ll1ll11_opy_, hook_type=bstack11lll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡗࡹ࡫ࡰࠣභ"), bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack111l111ll_opy_(runner, name, context, bstack1lll1llll1_opy_, *args):
    bstack111lll1l1_opy_(runner, name, context, args[0], bstack1lll1llll1_opy_, *args)
    try:
      bstack11l1l1l1l1_opy_ = threading.current_thread().bstackSessionDriver if bstack11lll1111_opy_(bstack11lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫම")) else context.browser
      if is_driver_active(bstack11l1l1l1l1_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack11lll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦඹ")
        bstack1111l11l1_opy_.bstack11l1ll11_opy_(args[0])
        if runner.driver_initialised == bstack11lll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧය"):
          feature_name = bstack1l11lll11_opy_ = str(runner.feature.name)
          bstack1l11lll11_opy_ = feature_name + bstack11lll1_opy_ (u"ࠨࠢ࠰ࠤࠬර") + context.scenario.name
          bstack11l1l1l1l1_opy_.execute_script(bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ඼") + json.dumps(bstack1l11lll11_opy_) + bstack11lll1_opy_ (u"ࠪࢁࢂ࠭ල"))
    except Exception as e:
      logger.debug(bstack11lll1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡵࡧࡳ࠾ࠥࢁࡽࠨ඾").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1ll1l11_opy_, stage=STAGE.bstack11ll1ll11_opy_, hook_type=bstack11lll1_opy_ (u"ࠧࡧࡦࡵࡧࡵࡗࡹ࡫ࡰࠣ඿"), bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack11ll1ll1ll_opy_(runner, name, context, bstack1lll1llll1_opy_, *args):
  bstack1111l11l1_opy_.bstack11l11l1l_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack11l1l1l1l1_opy_ = threading.current_thread().bstackSessionDriver if bstack11lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬව") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack11l1l1l1l1_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack11lll1_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧශ")
        feature_name = bstack1l11lll11_opy_ = str(runner.feature.name)
        bstack1l11lll11_opy_ = feature_name + bstack11lll1_opy_ (u"ࠨࠢ࠰ࠤࠬෂ") + context.scenario.name
        bstack11l1l1l1l1_opy_.execute_script(bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧස") + json.dumps(bstack1l11lll11_opy_) + bstack11lll1_opy_ (u"ࠪࢁࢂ࠭හ"))
    if str(step_status).lower() == bstack11lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫළ"):
      bstack1l11ll11ll_opy_ = bstack11lll1_opy_ (u"ࠬ࠭ෆ")
      bstack11lllll11_opy_ = bstack11lll1_opy_ (u"࠭ࠧ෇")
      bstack1ll1lll11_opy_ = bstack11lll1_opy_ (u"ࠧࠨ෈")
      try:
        import traceback
        bstack1l11ll11ll_opy_ = runner.exception.__class__.__name__
        bstack11l11l11_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11lllll11_opy_ = bstack11lll1_opy_ (u"ࠨࠢࠪ෉").join(bstack11l11l11_opy_)
        bstack1ll1lll11_opy_ = bstack11l11l11_opy_[-1]
      except Exception as e:
        logger.debug(bstack1llllll1l1_opy_.format(str(e)))
      bstack1l11ll11ll_opy_ += bstack1ll1lll11_opy_
      bstack1111ll11ll_opy_(context, json.dumps(str(args[0].name) + bstack11lll1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮්ࠣ") + str(bstack11lllll11_opy_)),
                          bstack11lll1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ෋"))
      if runner.driver_initialised == bstack11lll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤ෌"):
        bstack1l1lll111l_opy_(getattr(context, bstack11lll1_opy_ (u"ࠬࡶࡡࡨࡧࠪ෍"), None), bstack11lll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ෎"), bstack1l11ll11ll_opy_)
        bstack11l1l1l1l1_opy_.execute_script(bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬා") + json.dumps(str(args[0].name) + bstack11lll1_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢැ") + str(bstack11lllll11_opy_)) + bstack11lll1_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࡽࡾࠩෑ"))
      if runner.driver_initialised == bstack11lll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣි"):
        bstack1lllll1l1l_opy_(bstack11l1l1l1l1_opy_, bstack11lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫී"), bstack11lll1_opy_ (u"࡙ࠧࡣࡦࡰࡤࡶ࡮ࡵࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤු") + str(bstack1l11ll11ll_opy_))
    else:
      bstack1111ll11ll_opy_(context, bstack11lll1_opy_ (u"ࠨࡐࡢࡵࡶࡩࡩࠧࠢ෕"), bstack11lll1_opy_ (u"ࠢࡪࡰࡩࡳࠧූ"))
      if runner.driver_initialised == bstack11lll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨ෗"):
        bstack1l1lll111l_opy_(getattr(context, bstack11lll1_opy_ (u"ࠩࡳࡥ࡬࡫ࠧෘ"), None), bstack11lll1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥෙ"))
      bstack11l1l1l1l1_opy_.execute_script(bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩේ") + json.dumps(str(args[0].name) + bstack11lll1_opy_ (u"ࠧࠦ࠭ࠡࡒࡤࡷࡸ࡫ࡤࠢࠤෛ")) + bstack11lll1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬො"))
      if runner.driver_initialised == bstack11lll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧෝ"):
        bstack1lllll1l1l_opy_(bstack11l1l1l1l1_opy_, bstack11lll1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣෞ"))
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡳࡵࡧࡳ࠾ࠥࢁࡽࠨෟ").format(str(e)))
  bstack111lll1l1_opy_(runner, name, context, args[0], bstack1lll1llll1_opy_, *args)
@measure(event_name=EVENTS.bstack1111l11ll_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack1l1llll111_opy_(runner, name, context, bstack1lll1llll1_opy_, *args):
  bstack1111l11l1_opy_.end_test(args[0])
  try:
    bstack1ll11ll1ll_opy_ = args[0].status.name
    bstack11l1l1l1l1_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ෠"), context.browser)
    bstack1l1l1l11l1_opy_.bstack1ll111l11l_opy_(bstack11l1l1l1l1_opy_)
    if str(bstack1ll11ll1ll_opy_).lower() == bstack11lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ෡"):
      bstack1l11ll11ll_opy_ = bstack11lll1_opy_ (u"ࠬ࠭෢")
      bstack11lllll11_opy_ = bstack11lll1_opy_ (u"࠭ࠧ෣")
      bstack1ll1lll11_opy_ = bstack11lll1_opy_ (u"ࠧࠨ෤")
      try:
        import traceback
        bstack1l11ll11ll_opy_ = runner.exception.__class__.__name__
        bstack11l11l11_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11lllll11_opy_ = bstack11lll1_opy_ (u"ࠨࠢࠪ෥").join(bstack11l11l11_opy_)
        bstack1ll1lll11_opy_ = bstack11l11l11_opy_[-1]
      except Exception as e:
        logger.debug(bstack1llllll1l1_opy_.format(str(e)))
      bstack1l11ll11ll_opy_ += bstack1ll1lll11_opy_
      bstack1111ll11ll_opy_(context, json.dumps(str(args[0].name) + bstack11lll1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣ෦") + str(bstack11lllll11_opy_)),
                          bstack11lll1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ෧"))
      if runner.driver_initialised == bstack11lll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ෨") or runner.driver_initialised == bstack11lll1_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ෩"):
        bstack1l1lll111l_opy_(getattr(context, bstack11lll1_opy_ (u"࠭ࡰࡢࡩࡨࠫ෪"), None), bstack11lll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ෫"), bstack1l11ll11ll_opy_)
        bstack11l1l1l1l1_opy_.execute_script(bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭෬") + json.dumps(str(args[0].name) + bstack11lll1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣ෭") + str(bstack11lllll11_opy_)) + bstack11lll1_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪ෮"))
      if runner.driver_initialised == bstack11lll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ෯") or runner.driver_initialised == bstack11lll1_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ෰"):
        bstack1lllll1l1l_opy_(bstack11l1l1l1l1_opy_, bstack11lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭෱"), bstack11lll1_opy_ (u"ࠢࡔࡥࡨࡲࡦࡸࡩࡰࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦෲ") + str(bstack1l11ll11ll_opy_))
    else:
      bstack1111ll11ll_opy_(context, bstack11lll1_opy_ (u"ࠣࡒࡤࡷࡸ࡫ࡤࠢࠤෳ"), bstack11lll1_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢ෴"))
      if runner.driver_initialised == bstack11lll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ෵") or runner.driver_initialised == bstack11lll1_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫ෶"):
        bstack1l1lll111l_opy_(getattr(context, bstack11lll1_opy_ (u"ࠬࡶࡡࡨࡧࠪ෷"), None), bstack11lll1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ෸"))
      bstack11l1l1l1l1_opy_.execute_script(bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ෹") + json.dumps(str(args[0].name) + bstack11lll1_opy_ (u"ࠣࠢ࠰ࠤࡕࡧࡳࡴࡧࡧࠥࠧ෺")) + bstack11lll1_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧࢃࡽࠨ෻"))
      if runner.driver_initialised == bstack11lll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ෼") or runner.driver_initialised == bstack11lll1_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫ෽"):
        bstack1lllll1l1l_opy_(bstack11l1l1l1l1_opy_, bstack11lll1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ෾"))
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ෿").format(str(e)))
  bstack111lll1l1_opy_(runner, name, context, context.scenario, bstack1lll1llll1_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1ll1l1l11l_opy_(runner, name, context, bstack1lll1llll1_opy_, *args):
    target = context.scenario if hasattr(context, bstack11lll1_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩ฀")) else context.feature
    bstack111lll1l1_opy_(runner, name, context, target, bstack1lll1llll1_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1111ll1ll_opy_(runner, name, context, bstack1lll1llll1_opy_, *args):
    try:
      bstack11l1l1l1l1_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧก"), context.browser)
      bstack1l1l1lll1_opy_ = bstack11lll1_opy_ (u"ࠩࠪข")
      if context.failed is True:
        bstack111l1l11l1_opy_ = []
        bstack11l1ll1lll_opy_ = []
        bstack11l1l1lll_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack111l1l11l1_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l11l11_opy_ = traceback.format_tb(exc_tb)
            bstack11lll1llll_opy_ = bstack11lll1_opy_ (u"ࠪࠤࠬฃ").join(bstack11l11l11_opy_)
            bstack11l1ll1lll_opy_.append(bstack11lll1llll_opy_)
            bstack11l1l1lll_opy_.append(bstack11l11l11_opy_[-1])
        except Exception as e:
          logger.debug(bstack1llllll1l1_opy_.format(str(e)))
        bstack1l11ll11ll_opy_ = bstack11lll1_opy_ (u"ࠫࠬค")
        for i in range(len(bstack111l1l11l1_opy_)):
          bstack1l11ll11ll_opy_ += bstack111l1l11l1_opy_[i] + bstack11l1l1lll_opy_[i] + bstack11lll1_opy_ (u"ࠬࡢ࡮ࠨฅ")
        bstack1l1l1lll1_opy_ = bstack11lll1_opy_ (u"࠭ࠠࠨฆ").join(bstack11l1ll1lll_opy_)
        if runner.driver_initialised in [bstack11lll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣง"), bstack11lll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧจ")]:
          bstack1111ll11ll_opy_(context, bstack1l1l1lll1_opy_, bstack11lll1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣฉ"))
          bstack1l1lll111l_opy_(getattr(context, bstack11lll1_opy_ (u"ࠪࡴࡦ࡭ࡥࠨช"), None), bstack11lll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦซ"), bstack1l11ll11ll_opy_)
          bstack11l1l1l1l1_opy_.execute_script(bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪฌ") + json.dumps(bstack1l1l1lll1_opy_) + bstack11lll1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭ญ"))
          bstack1lllll1l1l_opy_(bstack11l1l1l1l1_opy_, bstack11lll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢฎ"), bstack11lll1_opy_ (u"ࠣࡕࡲࡱࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯ࡴࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡠࡳࠨฏ") + str(bstack1l11ll11ll_opy_))
          bstack1l11ll1lll_opy_ = bstack11ll111lll_opy_(bstack1l1l1lll1_opy_, runner.feature.name, logger)
          if (bstack1l11ll1lll_opy_ != None):
            bstack1l1ll111ll_opy_.append(bstack1l11ll1lll_opy_)
      else:
        if runner.driver_initialised in [bstack11lll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥฐ"), bstack11lll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢฑ")]:
          bstack1111ll11ll_opy_(context, bstack11lll1_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢฒ") + str(runner.feature.name) + bstack11lll1_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢณ"), bstack11lll1_opy_ (u"ࠨࡩ࡯ࡨࡲࠦด"))
          bstack1l1lll111l_opy_(getattr(context, bstack11lll1_opy_ (u"ࠧࡱࡣࡪࡩࠬต"), None), bstack11lll1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣถ"))
          bstack11l1l1l1l1_opy_.execute_script(bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧท") + json.dumps(bstack11lll1_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨ࠾ࠥࠨธ") + str(runner.feature.name) + bstack11lll1_opy_ (u"ࠦࠥࡶࡡࡴࡵࡨࡨࠦࠨน")) + bstack11lll1_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫบ"))
          bstack1lllll1l1l_opy_(bstack11l1l1l1l1_opy_, bstack11lll1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ป"))
          bstack1l11ll1lll_opy_ = bstack11ll111lll_opy_(bstack1l1l1lll1_opy_, runner.feature.name, logger)
          if (bstack1l11ll1lll_opy_ != None):
            bstack1l1ll111ll_opy_.append(bstack1l11ll1lll_opy_)
    except Exception as e:
      logger.debug(bstack11lll1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩผ").format(str(e)))
    bstack111lll1l1_opy_(runner, name, context, context.feature, bstack1lll1llll1_opy_, *args)
@measure(event_name=EVENTS.bstack1ll1ll1l11_opy_, stage=STAGE.bstack11ll1ll11_opy_, hook_type=bstack11lll1_opy_ (u"ࠣࡣࡩࡸࡪࡸࡁ࡭࡮ࠥฝ"), bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack1l111l11l1_opy_(runner, name, context, bstack1lll1llll1_opy_, *args):
    bstack111lll1l1_opy_(runner, name, context, runner, bstack1lll1llll1_opy_, *args)
def bstack11l111llll_opy_(self, name, context, *args):
  try:
    if bstack11ll11lll1_opy_:
      platform_index = int(threading.current_thread()._name) % bstack1l1l111ll1_opy_
      bstack1l11111l1l_opy_ = CONFIG[bstack11lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬพ")][platform_index]
      os.environ[bstack11lll1_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫฟ")] = json.dumps(bstack1l11111l1l_opy_)
    global bstack1lll1llll1_opy_
    if not hasattr(self, bstack11lll1_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡥࡥࠩภ")):
      self.driver_initialised = None
    bstack1ll11l111_opy_ = {
        bstack11lll1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠩม"): bstack1l1ll1ll1_opy_,
        bstack11lll1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠧย"): bstack1l1l1l1l1l_opy_,
        bstack11lll1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡵࡣࡪࠫร"): bstack1lll1lll1l_opy_,
        bstack11lll1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪฤ"): bstack11llll1l1_opy_,
        bstack11lll1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠧล"): bstack111l111ll_opy_,
        bstack11lll1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡸࡪࡶࠧฦ"): bstack11ll1ll1ll_opy_,
        bstack11lll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬว"): bstack1l1llll111_opy_,
        bstack11lll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡹࡧࡧࠨศ"): bstack1ll1l1l11l_opy_,
        bstack11lll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ษ"): bstack1111ll1ll_opy_,
        bstack11lll1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪส"): bstack1l111l11l1_opy_
    }
    handler = bstack1ll11l111_opy_.get(name, bstack1lll1llll1_opy_)
    try:
      handler(self, name, context, bstack1lll1llll1_opy_, *args)
    except Exception as e:
      logger.debug(bstack11lll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧࠣ࡬ࡴࡵ࡫ࠡࡪࡤࡲࡩࡲࡥࡳࠢࡾࢁ࠿ࠦࡻࡾࠩห").format(name, str(e)))
    if name in [bstack11lll1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩฬ"), bstack11lll1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫอ"), bstack11lll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧฮ")]:
      try:
        bstack11l1l1l1l1_opy_ = threading.current_thread().bstackSessionDriver if bstack11lll1111_opy_(bstack11lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫฯ")) else context.browser
        bstack1ll1111lll_opy_ = (
          (name == bstack11lll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩะ") and self.driver_initialised == bstack11lll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦั")) or
          (name == bstack11lll1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨา") and self.driver_initialised == bstack11lll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥำ")) or
          (name == bstack11lll1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫิ") and self.driver_initialised in [bstack11lll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨี"), bstack11lll1_opy_ (u"ࠧ࡯࡮ࡴࡶࡨࡴࠧึ")]) or
          (name == bstack11lll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡴࡦࡲࠪื") and self.driver_initialised == bstack11lll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴุࠧ"))
        )
        if bstack1ll1111lll_opy_:
          self.driver_initialised = None
          if bstack11l1l1l1l1_opy_ and hasattr(bstack11l1l1l1l1_opy_, bstack11lll1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨูࠬ")):
            try:
              bstack11l1l1l1l1_opy_.quit()
            except Exception as e:
              logger.debug(bstack11lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡳࡸ࡭ࡹࡺࡩ࡯ࡩࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࠦࡨࡰࡱ࡮࠾ࠥࢁࡽࠨฺ").format(str(e)))
      except Exception as e:
        logger.debug(bstack11lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡭ࡵ࡯࡬ࠢࡦࡰࡪࡧ࡮ࡶࡲࠣࡪࡴࡸࠠࡼࡿ࠽ࠤࢀࢃࠧ฻").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠫࡈࡸࡩࡵ࡫ࡦࡥࡱࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥࠡࡴࡸࡲࠥ࡮࡯ࡰ࡭ࠣࡿࢂࡀࠠࡼࡿࠪ฼").format(name, str(e)))
    try:
      bstack1lll1llll1_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack11lll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡲࡶ࡮࡭ࡩ࡯ࡣ࡯ࠤࡧ࡫ࡨࡢࡸࡨࠤ࡭ࡵ࡯࡬ࠢࡾࢁ࠿ࠦࡻࡾࠩ฽").format(name, str(e2)))
def bstack1111lll1l_opy_(config, startdir):
  return bstack11lll1_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࠲ࢀࠦ฾").format(bstack11lll1_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨ฿"))
notset = Notset()
def bstack1l11l11ll_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack11l111ll1_opy_
  if str(name).lower() == bstack11lll1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨเ"):
    return bstack11lll1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣแ")
  else:
    return bstack11l111ll1_opy_(self, name, default, skip)
def bstack1l111ll1l1_opy_(item, when):
  global bstack11lll111l_opy_
  try:
    bstack11lll111l_opy_(item, when)
  except Exception as e:
    pass
def bstack1ll11l1l11_opy_():
  return
def bstack11l111111l_opy_(type, name, status, reason, bstack11l1lll1l_opy_, bstack11ll1l1111_opy_):
  bstack1111l1l111_opy_ = {
    bstack11lll1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪโ"): type,
    bstack11lll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧใ"): {}
  }
  if type == bstack11lll1_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧไ"):
    bstack1111l1l111_opy_[bstack11lll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩๅ")][bstack11lll1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ๆ")] = bstack11l1lll1l_opy_
    bstack1111l1l111_opy_[bstack11lll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ็")][bstack11lll1_opy_ (u"ࠩࡧࡥࡹࡧ่ࠧ")] = json.dumps(str(bstack11ll1l1111_opy_))
  if type == bstack11lll1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨ้ࠫ"):
    bstack1111l1l111_opy_[bstack11lll1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹ๊ࠧ")][bstack11lll1_opy_ (u"ࠬࡴࡡ࡮ࡧ๋ࠪ")] = name
  if type == bstack11lll1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ์"):
    bstack1111l1l111_opy_[bstack11lll1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪํ")][bstack11lll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ๎")] = status
    if status == bstack11lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ๏"):
      bstack1111l1l111_opy_[bstack11lll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭๐")][bstack11lll1_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ๑")] = json.dumps(str(reason))
  bstack111llll1ll_opy_ = bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪ๒").format(json.dumps(bstack1111l1l111_opy_))
  return bstack111llll1ll_opy_
def bstack11l1lll1l1_opy_(driver_command, response):
    if driver_command == bstack11lll1_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪ๓"):
        bstack1ll1l11l_opy_.bstack111ll11lll_opy_({
            bstack11lll1_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭๔"): response[bstack11lll1_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧ๕")],
            bstack11lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ๖"): bstack1ll1l11l_opy_.current_test_uuid()
        })
def bstack1l1l1lll11_opy_(item, call, rep):
  global bstack1l111111l_opy_
  global bstack1l1l11l11l_opy_
  global bstack111ll11l1_opy_
  name = bstack11lll1_opy_ (u"ࠪࠫ๗")
  try:
    if rep.when == bstack11lll1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ๘"):
      bstack111l1l1l1l_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack111ll11l1_opy_:
          name = str(rep.nodeid)
          bstack1llll111l1_opy_ = bstack11l111111l_opy_(bstack11lll1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭๙"), name, bstack11lll1_opy_ (u"࠭ࠧ๚"), bstack11lll1_opy_ (u"ࠧࠨ๛"), bstack11lll1_opy_ (u"ࠨࠩ๜"), bstack11lll1_opy_ (u"ࠩࠪ๝"))
          threading.current_thread().bstack11111lll11_opy_ = name
          for driver in bstack1l1l11l11l_opy_:
            if bstack111l1l1l1l_opy_ == driver.session_id:
              driver.execute_script(bstack1llll111l1_opy_)
      except Exception as e:
        logger.debug(bstack11lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪ๞").format(str(e)))
      try:
        bstack1111lll111_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11lll1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ๟"):
          status = bstack11lll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ๠") if rep.outcome.lower() == bstack11lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭๡") else bstack11lll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ๢")
          reason = bstack11lll1_opy_ (u"ࠨࠩ๣")
          if status == bstack11lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ๤"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11lll1_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨ๥") if status == bstack11lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ๦") else bstack11lll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ๧")
          data = name + bstack11lll1_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨ๨") if status == bstack11lll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ๩") else name + bstack11lll1_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠣࠣࠫ๪") + reason
          bstack11ll1l1ll_opy_ = bstack11l111111l_opy_(bstack11lll1_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫ๫"), bstack11lll1_opy_ (u"ࠪࠫ๬"), bstack11lll1_opy_ (u"ࠫࠬ๭"), bstack11lll1_opy_ (u"ࠬ࠭๮"), level, data)
          for driver in bstack1l1l11l11l_opy_:
            if bstack111l1l1l1l_opy_ == driver.session_id:
              driver.execute_script(bstack11ll1l1ll_opy_)
      except Exception as e:
        logger.debug(bstack11lll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡴࡴࡴࡦࡺࡷࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪ๯").format(str(e)))
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽࢀࠫ๰").format(str(e)))
  bstack1l111111l_opy_(item, call, rep)
def bstack1l11ll1ll_opy_(driver, bstack1l1111llll_opy_, test=None):
  global bstack11l111111_opy_
  if test != None:
    bstack1l1ll1llll_opy_ = getattr(test, bstack11lll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭๱"), None)
    bstack1lllllllll_opy_ = getattr(test, bstack11lll1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ๲"), None)
    PercySDK.screenshot(driver, bstack1l1111llll_opy_, bstack1l1ll1llll_opy_=bstack1l1ll1llll_opy_, bstack1lllllllll_opy_=bstack1lllllllll_opy_, bstack1l1ll11lll_opy_=bstack11l111111_opy_)
  else:
    PercySDK.screenshot(driver, bstack1l1111llll_opy_)
@measure(event_name=EVENTS.bstack11llll1lll_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack1l1lll1l1l_opy_(driver):
  if bstack11l1lllll_opy_.bstack1l1ll111l1_opy_() is True or bstack11l1lllll_opy_.capturing() is True:
    return
  bstack11l1lllll_opy_.bstack1l1l1lll1l_opy_()
  while not bstack11l1lllll_opy_.bstack1l1ll111l1_opy_():
    bstack1l11ll11l1_opy_ = bstack11l1lllll_opy_.bstack1l1lll11ll_opy_()
    bstack1l11ll1ll_opy_(driver, bstack1l11ll11l1_opy_)
  bstack11l1lllll_opy_.bstack1l111l1ll_opy_()
def bstack11lll11ll1_opy_(sequence, driver_command, response = None, bstack1ll1111ll_opy_ = None, args = None):
    try:
      if sequence != bstack11lll1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪ๳"):
        return
      if percy.bstack1l1l1lllll_opy_() == bstack11lll1_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥ๴"):
        return
      bstack1l11ll11l1_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ๵"), None)
      for command in bstack11111ll1l_opy_:
        if command == driver_command:
          with bstack11111l111_opy_:
            bstack111lll1ll1_opy_ = bstack1l1l11l11l_opy_.copy()
          for driver in bstack111lll1ll1_opy_:
            bstack1l1lll1l1l_opy_(driver)
      bstack11l1llll11_opy_ = percy.bstack11l1l11l1_opy_()
      if driver_command in bstack1lllll1ll1_opy_[bstack11l1llll11_opy_]:
        bstack11l1lllll_opy_.bstack1ll1lll111_opy_(bstack1l11ll11l1_opy_, driver_command)
    except Exception as e:
      pass
def bstack11l11111l1_opy_(framework_name):
  if bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ๶")):
      return
  bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ๷"), True)
  global bstack11lll1l11l_opy_
  global bstack111l1ll11l_opy_
  global bstack11l111ll1l_opy_
  bstack11lll1l11l_opy_ = framework_name
  logger.info(bstack1l11lllll_opy_.format(bstack11lll1l11l_opy_.split(bstack11lll1_opy_ (u"ࠨ࠯ࠪ๸"))[0]))
  bstack111l11ll11_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack11ll11lll1_opy_:
      Service.start = bstack11111l1l1l_opy_
      Service.stop = bstack11111llll1_opy_
      webdriver.Remote.get = bstack1l11l1l11l_opy_
      WebDriver.quit = bstack111lll11l_opy_
      webdriver.Remote.__init__ = bstack111lllll11_opy_
    if not bstack11ll11lll1_opy_:
        webdriver.Remote.__init__ = bstack11lll111ll_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack111ll1lll_opy_
    bstack111l1ll11l_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack11ll11lll1_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1111l1llll_opy_
  except Exception as e:
    pass
  bstack11ll11llll_opy_()
  if not bstack111l1ll11l_opy_:
    bstack11l1l11l11_opy_(bstack11lll1_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦ๹"), bstack1l1lll11l_opy_)
  if bstack1l1ll11l1l_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack11lll1_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ๺")) and callable(getattr(RemoteConnection, bstack11lll1_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ๻"))):
        RemoteConnection._get_proxy_url = bstack111ll11ll1_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack111ll11ll1_opy_
    except Exception as e:
      logger.error(bstack111l1l11ll_opy_.format(str(e)))
  if bstack1llll11ll1_opy_():
    bstack1l1ll1l111_opy_(CONFIG, logger)
  if (bstack11lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ๼") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1l1l1lllll_opy_() == bstack11lll1_opy_ (u"ࠨࡴࡳࡷࡨࠦ๽"):
          bstack111ll1ll1l_opy_(bstack11lll11ll1_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1l1l11ll1l_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack11lllll1l_opy_
      except Exception as e:
        logger.warn(bstack1l1lllll11_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack11lll11l11_opy_
      except Exception as e:
        logger.debug(bstack11l1ll1ll_opy_ + str(e))
    except Exception as e:
      bstack11l1l11l11_opy_(e, bstack1l1lllll11_opy_)
    Output.start_test = bstack111l1lll1_opy_
    Output.end_test = bstack1l1111ll11_opy_
    TestStatus.__init__ = bstack1ll11lll1_opy_
    QueueItem.__init__ = bstack1l11l111l1_opy_
    pabot._create_items = bstack1ll111l1ll_opy_
    try:
      from pabot import __version__ as bstack111ll1l11_opy_
      if version.parse(bstack111ll1l11_opy_) >= version.parse(bstack11lll1_opy_ (u"ࠧ࠶࠰࠳࠲࠵࠭๾")):
        pabot._run = bstack11llll11l1_opy_
      elif version.parse(bstack111ll1l11_opy_) >= version.parse(bstack11lll1_opy_ (u"ࠨ࠶࠱࠶࠳࠶ࠧ๿")):
        pabot._run = bstack1111l1111l_opy_
      elif version.parse(bstack111ll1l11_opy_) >= version.parse(bstack11lll1_opy_ (u"ࠩ࠵࠲࠶࠻࠮࠱ࠩ຀")):
        pabot._run = bstack1ll111l1l_opy_
      elif version.parse(bstack111ll1l11_opy_) >= version.parse(bstack11lll1_opy_ (u"ࠪ࠶࠳࠷࠳࠯࠲ࠪກ")):
        pabot._run = bstack1lllll1111_opy_
      else:
        pabot._run = bstack1ll1111l1l_opy_
    except Exception as e:
      pabot._run = bstack1ll1111l1l_opy_
    pabot._create_command_for_execution = bstack11l111l111_opy_
    pabot._report_results = bstack11l11l1l1_opy_
  if bstack11lll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫຂ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11l1l11l11_opy_(e, bstack1111ll1l1l_opy_)
    Runner.run_hook = bstack11l111llll_opy_
    Step.run = bstack1ll1l1l1ll_opy_
  if bstack11lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ຃") in str(framework_name).lower():
    if not bstack11ll11lll1_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1111lll1l_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1ll11l1l11_opy_
      Config.getoption = bstack1l11l11ll_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1l1l1lll11_opy_
    except Exception as e:
      pass
def bstack11llll11ll_opy_():
  global CONFIG
  if bstack11lll1_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ຄ") in CONFIG and int(CONFIG[bstack11lll1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ຅")]) > 1:
    logger.warn(bstack1l1l1l1lll_opy_)
def bstack1l1l1ll111_opy_(arg, bstack1llll1111_opy_, bstack1l1lllllll_opy_=None):
  global CONFIG
  global bstack111111ll1l_opy_
  global bstack1ll1l11111_opy_
  global bstack11ll11lll1_opy_
  global bstack1lll1l11l_opy_
  bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨຆ")
  if bstack1llll1111_opy_ and isinstance(bstack1llll1111_opy_, str):
    bstack1llll1111_opy_ = eval(bstack1llll1111_opy_)
  CONFIG = bstack1llll1111_opy_[bstack11lll1_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩງ")]
  bstack111111ll1l_opy_ = bstack1llll1111_opy_[bstack11lll1_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫຈ")]
  bstack1ll1l11111_opy_ = bstack1llll1111_opy_[bstack11lll1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ຉ")]
  bstack11ll11lll1_opy_ = bstack1llll1111_opy_[bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨຊ")]
  bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ຋"), bstack11ll11lll1_opy_)
  os.environ[bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩຌ")] = bstack1ll11lll1l_opy_
  os.environ[bstack11lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠧຍ")] = json.dumps(CONFIG)
  os.environ[bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡊࡘࡆࡤ࡛ࡒࡍࠩຎ")] = bstack111111ll1l_opy_
  os.environ[bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫຏ")] = str(bstack1ll1l11111_opy_)
  os.environ[bstack11lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪຐ")] = str(True)
  if bstack1ll1l111ll_opy_(arg, [bstack11lll1_opy_ (u"ࠬ࠳࡮ࠨຑ"), bstack11lll1_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧຒ")]) != -1:
    os.environ[bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡂࡔࡄࡐࡑࡋࡌࠨຓ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1ll1l1111l_opy_)
    return
  bstack1l1l111l1_opy_()
  global bstack1l1ll11l1_opy_
  global bstack11l111111_opy_
  global bstack1l1111lll1_opy_
  global bstack11l11llll1_opy_
  global bstack1ll1lll1ll_opy_
  global bstack11l111ll1l_opy_
  global bstack1l1111111_opy_
  arg.append(bstack11lll1_opy_ (u"ࠣ࠯࡚ࠦດ"))
  arg.append(bstack11lll1_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦ࠼ࡐࡳࡩࡻ࡬ࡦࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡭ࡲࡶ࡯ࡳࡶࡨࡨ࠿ࡶࡹࡵࡧࡶࡸ࠳ࡖࡹࡵࡧࡶࡸ࡜ࡧࡲ࡯࡫ࡱ࡫ࠧຕ"))
  arg.append(bstack11lll1_opy_ (u"ࠥ࠱࡜ࠨຖ"))
  arg.append(bstack11lll1_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨ࠾࡙࡮ࡥࠡࡪࡲࡳࡰ࡯࡭ࡱ࡮ࠥທ"))
  global bstack1111lll1ll_opy_
  global bstack1l1ll11ll1_opy_
  global bstack1l11lll1l_opy_
  global bstack1l1l11l1l1_opy_
  global bstack1ll1ll1111_opy_
  global bstack111llll1l_opy_
  global bstack1l11l1l1ll_opy_
  global bstack1l11l1llll_opy_
  global bstack11l11ll1ll_opy_
  global bstack1l11llllll_opy_
  global bstack11l111ll1_opy_
  global bstack11lll111l_opy_
  global bstack1l111111l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1111lll1ll_opy_ = webdriver.Remote.__init__
    bstack1l1ll11ll1_opy_ = WebDriver.quit
    bstack1l11l1llll_opy_ = WebDriver.close
    bstack11l11ll1ll_opy_ = WebDriver.get
    bstack1l11lll1l_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1lll1l11ll_opy_(CONFIG) and bstack1111l1l11l_opy_():
    if bstack11lllll11l_opy_() < version.parse(bstack1ll1l1l111_opy_):
      logger.error(bstack1l1l1ll11_opy_.format(bstack11lllll11l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11lll1_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ຘ")) and callable(getattr(RemoteConnection, bstack11lll1_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧນ"))):
          bstack1l11llllll_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1l11llllll_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack111l1l11ll_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack11l111ll1_opy_ = Config.getoption
    from _pytest import runner
    bstack11lll111l_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack111llll1_opy_)
  try:
    from pytest_bdd import reporting
    bstack1l111111l_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11lll1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨບ"))
  bstack1l1111lll1_opy_ = CONFIG.get(bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬປ"), {}).get(bstack11lll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫຜ"))
  bstack1l1111111_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack1ll11lllll_opy_():
      bstack1l1l1ll1l_opy_.invoke(Events.CONNECT, bstack11lll1ll1_opy_())
    platform_index = int(os.environ.get(bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪຝ"), bstack11lll1_opy_ (u"ࠫ࠵࠭ພ")))
  else:
    bstack11l11111l1_opy_(bstack1ll11ll111_opy_)
  os.environ[bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭ຟ")] = CONFIG[bstack11lll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨຠ")]
  os.environ[bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪມ")] = CONFIG[bstack11lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫຢ")]
  os.environ[bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬຣ")] = bstack11ll11lll1_opy_.__str__()
  from _pytest.config import main as bstack111ll1llll_opy_
  bstack111l111ll1_opy_ = []
  try:
    exit_code = bstack111ll1llll_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1l1ll11111_opy_()
    if bstack11lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧ຤") in multiprocessing.current_process().__dict__.keys():
      for bstack111l1ll111_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack111l111ll1_opy_.append(bstack111l1ll111_opy_)
    try:
      bstack11111l1l11_opy_ = (bstack111l111ll1_opy_, int(exit_code))
      bstack1l1lllllll_opy_.append(bstack11111l1l11_opy_)
    except:
      bstack1l1lllllll_opy_.append((bstack111l111ll1_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack111l111ll1_opy_.append({bstack11lll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩລ"): bstack11lll1_opy_ (u"ࠬࡖࡲࡰࡥࡨࡷࡸࠦࠧ຦") + os.environ.get(bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ວ")), bstack11lll1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ຨ"): traceback.format_exc(), bstack11lll1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧຩ"): int(os.environ.get(bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩສ")))})
    bstack1l1lllllll_opy_.append((bstack111l111ll1_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack11lll1_opy_ (u"ࠥࡶࡪࡺࡲࡪࡧࡶࠦຫ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack111l1111ll_opy_ = e.__class__.__name__
    print(bstack11lll1_opy_ (u"ࠦࠪࡹ࠺ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡤࡨ࡬ࡦࡼࡥࠡࡶࡨࡷࡹࠦࠥࡴࠤຬ") % (bstack111l1111ll_opy_, e))
    return 1
def bstack1lll11ll1l_opy_(arg):
  global bstack1l111l111_opy_
  bstack11l11111l1_opy_(bstack1l1111l1l_opy_)
  os.environ[bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ອ")] = str(bstack1ll1l11111_opy_)
  retries = bstack11111lll_opy_.bstack111l1l1l_opy_(CONFIG)
  status_code = 0
  if bstack11111lll_opy_.bstack11111111_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack11l11l111_opy_
    status_code = bstack11l11l111_opy_(arg)
  if status_code != 0:
    bstack1l111l111_opy_ = status_code
def bstack11l111l1l_opy_():
  logger.info(bstack11111l1l1_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬຮ"), help=bstack11lll1_opy_ (u"ࠧࡈࡧࡱࡩࡷࡧࡴࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡥࡲࡲ࡫࡯ࡧࠨຯ"))
  parser.add_argument(bstack11lll1_opy_ (u"ࠨ࠯ࡸࠫະ"), bstack11lll1_opy_ (u"ࠩ࠰࠱ࡺࡹࡥࡳࡰࡤࡱࡪ࠭ັ"), help=bstack11lll1_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡶࡵࡨࡶࡳࡧ࡭ࡦࠩາ"))
  parser.add_argument(bstack11lll1_opy_ (u"ࠫ࠲ࡱࠧຳ"), bstack11lll1_opy_ (u"ࠬ࠳࠭࡬ࡧࡼࠫິ"), help=bstack11lll1_opy_ (u"࡙࠭ࡰࡷࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠧີ"))
  parser.add_argument(bstack11lll1_opy_ (u"ࠧ࠮ࡨࠪຶ"), bstack11lll1_opy_ (u"ࠨ࠯࠰ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ື"), help=bstack11lll1_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨຸ"))
  bstack11l1111l11_opy_ = parser.parse_args()
  try:
    bstack1111l1lll_opy_ = bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡪࡩࡳ࡫ࡲࡪࡥ࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ູࠧ")
    if bstack11l1111l11_opy_.framework and bstack11l1111l11_opy_.framework not in (bstack11lll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ຺ࠫ"), bstack11lll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭ົ")):
      bstack1111l1lll_opy_ = bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠯ࡻࡰࡰ࠳ࡹࡡ࡮ࡲ࡯ࡩࠬຼ")
    bstack1l1l1l11l_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1111l1lll_opy_)
    bstack1l1ll1ll1l_opy_ = open(bstack1l1l1l11l_opy_, bstack11lll1_opy_ (u"ࠧࡳࠩຽ"))
    bstack1ll11llll1_opy_ = bstack1l1ll1ll1l_opy_.read()
    bstack1l1ll1ll1l_opy_.close()
    if bstack11l1111l11_opy_.username:
      bstack1ll11llll1_opy_ = bstack1ll11llll1_opy_.replace(bstack11lll1_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨ຾"), bstack11l1111l11_opy_.username)
    if bstack11l1111l11_opy_.key:
      bstack1ll11llll1_opy_ = bstack1ll11llll1_opy_.replace(bstack11lll1_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫ຿"), bstack11l1111l11_opy_.key)
    if bstack11l1111l11_opy_.framework:
      bstack1ll11llll1_opy_ = bstack1ll11llll1_opy_.replace(bstack11lll1_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫເ"), bstack11l1111l11_opy_.framework)
    file_name = bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧແ")
    file_path = os.path.abspath(file_name)
    bstack11ll1l1l1_opy_ = open(file_path, bstack11lll1_opy_ (u"ࠬࡽࠧໂ"))
    bstack11ll1l1l1_opy_.write(bstack1ll11llll1_opy_)
    bstack11ll1l1l1_opy_.close()
    logger.info(bstack1l1111l1l1_opy_)
    try:
      os.environ[bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨໃ")] = bstack11l1111l11_opy_.framework if bstack11l1111l11_opy_.framework != None else bstack11lll1_opy_ (u"ࠢࠣໄ")
      config = yaml.safe_load(bstack1ll11llll1_opy_)
      config[bstack11lll1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ໅")] = bstack11lll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠯ࡶࡩࡹࡻࡰࠨໆ")
      bstack1l1lll1ll_opy_(bstack1ll11l1111_opy_, config)
    except Exception as e:
      logger.debug(bstack1111ll11l1_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1111ll111l_opy_.format(str(e)))
def bstack1l1lll1ll_opy_(bstack1l11lll11l_opy_, config, bstack1l11l11111_opy_={}):
  global bstack11ll11lll1_opy_
  global bstack11lll11lll_opy_
  global bstack1lll1l11l_opy_
  if not config:
    return
  bstack111ll1l1l_opy_ = bstack1l111ll1l_opy_ if not bstack11ll11lll1_opy_ else (
    bstack1l11111ll_opy_ if bstack11lll1_opy_ (u"ࠪࡥࡵࡶࠧ໇") in config else (
        bstack111l1ll1ll_opy_ if config.get(bstack11lll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ່")) else bstack1l1ll1lll_opy_
    )
)
  bstack1l11l1ll1l_opy_ = False
  bstack1ll1l11l1_opy_ = False
  if bstack11ll11lll1_opy_ is True:
      if bstack11lll1_opy_ (u"ࠬࡧࡰࡱ້ࠩ") in config:
          bstack1l11l1ll1l_opy_ = True
      else:
          bstack1ll1l11l1_opy_ = True
  bstack111111l11l_opy_ = bstack11l11l11ll_opy_.bstack1l1l11l11_opy_(config, bstack11lll11lll_opy_)
  bstack1ll1l1llll_opy_ = bstack1l1lll11l1_opy_()
  data = {
    bstack11lll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ໊"): config[bstack11lll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦ໋ࠩ")],
    bstack11lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ໌"): config[bstack11lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬໍ")],
    bstack11lll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ໎"): bstack1l11lll11l_opy_,
    bstack11lll1_opy_ (u"ࠫࡩ࡫ࡴࡦࡥࡷࡩࡩࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ໏"): os.environ.get(bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ໐"), bstack11lll11lll_opy_),
    bstack11lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ໑"): bstack1111l1ll11_opy_,
    bstack11lll1_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭ࠩ໒"): bstack111l111l1_opy_(),
    bstack11lll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໓"): {
      bstack11lll1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ໔"): str(config[bstack11lll1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ໕")]) if bstack11lll1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ໖") in config else bstack11lll1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨ໗"),
      bstack11lll1_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࡗࡧࡵࡷ࡮ࡵ࡮ࠨ໘"): sys.version,
      bstack11lll1_opy_ (u"ࠧࡳࡧࡩࡩࡷࡸࡥࡳࠩ໙"): bstack11ll1lll1l_opy_(os.environ.get(bstack11lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ໚"), bstack11lll11lll_opy_)),
      bstack11lll1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ໛"): bstack11lll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪໜ"),
      bstack11lll1_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬໝ"): bstack111ll1l1l_opy_,
      bstack11lll1_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪໞ"): bstack111111l11l_opy_,
      bstack11lll1_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡶࡷ࡬ࡨࠬໟ"): os.environ[bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ໠")],
      bstack11lll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ໡"): os.environ.get(bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ໢"), bstack11lll11lll_opy_),
      bstack11lll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭໣"): bstack11l11l11l1_opy_(os.environ.get(bstack11lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭໤"), bstack11lll11lll_opy_)),
      bstack11lll1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ໥"): bstack1ll1l1llll_opy_.get(bstack11lll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ໦")),
      bstack11lll1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭໧"): bstack1ll1l1llll_opy_.get(bstack11lll1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ໨")),
      bstack11lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ໩"): config[bstack11lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໪")] if config[bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ໫")] else bstack11lll1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨ໬"),
      bstack11lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ໭"): str(config[bstack11lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ໮")]) if bstack11lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໯") in config else bstack11lll1_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥ໰"),
      bstack11lll1_opy_ (u"ࠪࡳࡸ࠭໱"): sys.platform,
      bstack11lll1_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭໲"): socket.gethostname(),
      bstack11lll1_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ໳"): bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ໴"))
    }
  }
  if not bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ໵")) is None:
    data[bstack11lll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໶")][bstack11lll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡑࡪࡺࡡࡥࡣࡷࡥࠬ໷")] = {
      bstack11lll1_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ໸"): bstack11lll1_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩ໹"),
      bstack11lll1_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬ໺"): bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭໻")),
      bstack11lll1_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࡎࡶ࡯ࡥࡩࡷ࠭໼"): bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡐࡲࠫ໽"))
    }
  if bstack1l11lll11l_opy_ == bstack11l11lllll_opy_:
    data[bstack11lll1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໾")][bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡅࡲࡲ࡫࡯ࡧࠨ໿")] = bstack11l11ll111_opy_(config)
    data[bstack11lll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧༀ")][bstack11lll1_opy_ (u"ࠬ࡯ࡳࡑࡧࡵࡧࡾࡇࡵࡵࡱࡈࡲࡦࡨ࡬ࡦࡦࠪ༁")] = percy.bstack1ll1l11lll_opy_
    data[bstack11lll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ༂")][bstack11lll1_opy_ (u"ࠧࡱࡧࡵࡧࡾࡈࡵࡪ࡮ࡧࡍࡩ࠭༃")] = percy.percy_build_id
  if not bstack11111lll_opy_.bstack11ll1l11l_opy_(CONFIG):
    data[bstack11lll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ༄")][bstack11lll1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠭༅")] = bstack11111lll_opy_.bstack11ll1l11l_opy_(CONFIG)
  bstack111111ll_opy_ = bstack111l11ll_opy_.bstack111ll1l1_opy_(CONFIG, logger)
  bstack1lll1l1l1_opy_ = bstack11111lll_opy_.bstack111ll1l1_opy_(config=CONFIG)
  if bstack111111ll_opy_ is not None and bstack1lll1l1l1_opy_ is not None and bstack1lll1l1l1_opy_.bstack1111l11l_opy_():
    data[bstack11lll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭༆")][bstack1lll1l1l1_opy_.bstack11l1llll1l_opy_()] = bstack111111ll_opy_.bstack1l111lllll_opy_()
  update(data[bstack11lll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ༇")], bstack1l11l11111_opy_)
  try:
    response = bstack1lll111l1l_opy_(bstack11lll1_opy_ (u"ࠬࡖࡏࡔࡖࠪ༈"), bstack1l11111l1_opy_(bstack1ll1l1ll11_opy_), data, {
      bstack11lll1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ༉"): (config[bstack11lll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ༊")], config[bstack11lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ་")])
    })
    if response:
      logger.debug(bstack1ll11ll11_opy_.format(bstack1l11lll11l_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack111111l1l1_opy_.format(str(e)))
def bstack11ll1lll1l_opy_(framework):
  return bstack11lll1_opy_ (u"ࠤࡾࢁ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨ༌").format(str(framework), __version__) if framework else bstack11lll1_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦ།").format(
    __version__)
def bstack1l1l111l1_opy_():
  global CONFIG
  global bstack1l11ll1ll1_opy_
  if bool(CONFIG):
    return
  try:
    bstack1l1l111111_opy_()
    logger.debug(bstack111l11111_opy_.format(str(CONFIG)))
    bstack1l11ll1ll1_opy_ = bstack1l1l1llll1_opy_.configure_logger(CONFIG, bstack1l11ll1ll1_opy_)
    bstack111l11ll11_opy_()
  except Exception as e:
    logger.error(bstack11lll1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵ࠲ࠠࡦࡴࡵࡳࡷࡀࠠࠣ༎") + str(e))
    sys.exit(1)
  sys.excepthook = bstack111l1lll1l_opy_
  atexit.register(bstack11l11lll1_opy_)
  signal.signal(signal.SIGINT, bstack1l11l1l111_opy_)
  signal.signal(signal.SIGTERM, bstack1l11l1l111_opy_)
def bstack111l1lll1l_opy_(exctype, value, traceback):
  global bstack1l1l11l11l_opy_
  try:
    for driver in bstack1l1l11l11l_opy_:
      bstack1lllll1l1l_opy_(driver, bstack11lll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ༏"), bstack11lll1_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤ༐") + str(value))
  except Exception:
    pass
  logger.info(bstack1lllll1l11_opy_)
  bstack1llllll11l_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1llllll11l_opy_(message=bstack11lll1_opy_ (u"ࠧࠨ༑"), bstack1ll1llllll_opy_ = False):
  global CONFIG
  bstack11l1ll1l1_opy_ = bstack11lll1_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡆࡺࡦࡩࡵࡺࡩࡰࡰࠪ༒") if bstack1ll1llllll_opy_ else bstack11lll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ༓")
  try:
    if message:
      bstack1l11l11111_opy_ = {
        bstack11l1ll1l1_opy_ : str(message)
      }
      bstack1l1lll1ll_opy_(bstack11l11lllll_opy_, CONFIG, bstack1l11l11111_opy_)
    else:
      bstack1l1lll1ll_opy_(bstack11l11lllll_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack11l1111ll1_opy_.format(str(e)))
def bstack1l111111ll_opy_(bstack11l1l1ll11_opy_, size):
  bstack1l111111l1_opy_ = []
  while len(bstack11l1l1ll11_opy_) > size:
    bstack1l111llll_opy_ = bstack11l1l1ll11_opy_[:size]
    bstack1l111111l1_opy_.append(bstack1l111llll_opy_)
    bstack11l1l1ll11_opy_ = bstack11l1l1ll11_opy_[size:]
  bstack1l111111l1_opy_.append(bstack11l1l1ll11_opy_)
  return bstack1l111111l1_opy_
def bstack11111ll111_opy_(args):
  if bstack11lll1_opy_ (u"ࠪ࠱ࡲ࠭༔") in args and bstack11lll1_opy_ (u"ࠫࡵࡪࡢࠨ༕") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack1ll11111l1_opy_, stage=STAGE.bstack1ll1ll11l_opy_)
def run_on_browserstack(bstack1l111l1l1_opy_=None, bstack1l1lllllll_opy_=None, bstack11l1l11ll_opy_=False):
  global CONFIG
  global bstack111111ll1l_opy_
  global bstack1ll1l11111_opy_
  global bstack11lll11lll_opy_
  global bstack1lll1l11l_opy_
  bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠬ࠭༖")
  bstack1ll1ll111_opy_(bstack1l11l1ll11_opy_, logger)
  if bstack1l111l1l1_opy_ and isinstance(bstack1l111l1l1_opy_, str):
    bstack1l111l1l1_opy_ = eval(bstack1l111l1l1_opy_)
  if bstack1l111l1l1_opy_:
    CONFIG = bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭༗")]
    bstack111111ll1l_opy_ = bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ༘")]
    bstack1ll1l11111_opy_ = bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇ༙ࠪ")]
    bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ༚"), bstack1ll1l11111_opy_)
    bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༛")
  bstack1lll1l11l_opy_.set_property(bstack11lll1_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭༜"), uuid4().__str__())
  logger.info(bstack11lll1_opy_ (u"࡙ࠬࡄࡌࠢࡵࡹࡳࠦࡳࡵࡣࡵࡸࡪࡪࠠࡸ࡫ࡷ࡬ࠥ࡯ࡤ࠻ࠢࠪ༝") + bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ༞")));
  logger.debug(bstack11lll1_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥ࠿ࠪ༟") + bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪ༠")))
  if not bstack11l1l11ll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1ll1l1111l_opy_)
      return
    if sys.argv[1] == bstack11lll1_opy_ (u"ࠩ࠰࠱ࡻ࡫ࡲࡴ࡫ࡲࡲࠬ༡") or sys.argv[1] == bstack11lll1_opy_ (u"ࠪ࠱ࡻ࠭༢"):
      logger.info(bstack11lll1_opy_ (u"ࠫࡇࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡔࡾࡺࡨࡰࡰࠣࡗࡉࡑࠠࡷࡽࢀࠫ༣").format(__version__))
      return
    if sys.argv[1] == bstack11lll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ༤"):
      bstack11l111l1l_opy_()
      return
  args = sys.argv
  bstack1l1l111l1_opy_()
  global bstack1l1ll11l1_opy_
  global bstack1l1l111ll1_opy_
  global bstack1l1111111_opy_
  global bstack1lll1lllll_opy_
  global bstack11l111111_opy_
  global bstack1l1111lll1_opy_
  global bstack11l11llll1_opy_
  global bstack1l11111111_opy_
  global bstack1ll1lll1ll_opy_
  global bstack11l111ll1l_opy_
  global bstack1llll1ll11_opy_
  bstack1l1l111ll1_opy_ = len(CONFIG.get(bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ༥"), []))
  if not bstack1ll11lll1l_opy_:
    if args[1] == bstack11lll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༦") or args[1] == bstack11lll1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩ༧"):
      bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༨")
      args = args[2:]
    elif args[1] == bstack11lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ༩"):
      bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༪")
      args = args[2:]
    elif args[1] == bstack11lll1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ༫"):
      bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ༬")
      args = args[2:]
    elif args[1] == bstack11lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ༭"):
      bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ༮")
      args = args[2:]
    elif args[1] == bstack11lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ༯"):
      bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ༰")
      args = args[2:]
    elif args[1] == bstack11lll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ༱"):
      bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ༲")
      args = args[2:]
    else:
      if not bstack11lll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༳") in CONFIG or str(CONFIG[bstack11lll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༴")]).lower() in [bstack11lll1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ༵"), bstack11lll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ༶")]:
        bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ༷ࠪ")
        args = args[1:]
      elif str(CONFIG[bstack11lll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ༸")]).lower() == bstack11lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ༹ࠫ"):
        bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ༺")
        args = args[1:]
      elif str(CONFIG[bstack11lll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༻")]).lower() == bstack11lll1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ༼"):
        bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༽")
        args = args[1:]
      elif str(CONFIG[bstack11lll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭༾")]).lower() == bstack11lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༿"):
        bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཀ")
        args = args[1:]
      elif str(CONFIG[bstack11lll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩཁ")]).lower() == bstack11lll1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧག"):
        bstack1ll11lll1l_opy_ = bstack11lll1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨགྷ")
        args = args[1:]
      else:
        os.environ[bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫང")] = bstack1ll11lll1l_opy_
        bstack1lll1ll111_opy_(bstack1ll1l11l11_opy_)
  os.environ[bstack11lll1_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫཅ")] = bstack1ll11lll1l_opy_
  bstack11lll11lll_opy_ = bstack1ll11lll1l_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1lll11l1ll_opy_ = bstack1111ll1111_opy_[bstack11lll1_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗ࠱ࡇࡊࡄࠨཆ")] if bstack1ll11lll1l_opy_ == bstack11lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཇ") and bstack1lll1ll11l_opy_() else bstack1ll11lll1l_opy_
      bstack1l1l1ll1l_opy_.invoke(Events.bstack1111ll1l11_opy_, bstack11111l11l1_opy_(
        sdk_version=__version__,
        path_config=bstack1l1ll111l_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1lll11l1ll_opy_,
        frameworks=[bstack1lll11l1ll_opy_],
        framework_versions={
          bstack1lll11l1ll_opy_: bstack11l11l11l1_opy_(bstack11lll1_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬ཈") if bstack1ll11lll1l_opy_ in [bstack11lll1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ཉ"), bstack11lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧཊ"), bstack11lll1_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪཋ")] else bstack1ll11lll1l_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack11lll1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧཌ"), None):
        CONFIG[bstack11lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨཌྷ")] = cli.config.get(bstack11lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢཎ"), None)
    except Exception as e:
      bstack1l1l1ll1l_opy_.invoke(Events.bstack11l11llll_opy_, e.__traceback__, 1)
    if bstack1ll1l11111_opy_:
      CONFIG[bstack11lll1_opy_ (u"ࠨࡡࡱࡲࠥཏ")] = cli.config[bstack11lll1_opy_ (u"ࠢࡢࡲࡳࠦཐ")]
      logger.info(bstack1l1ll11l11_opy_.format(CONFIG[bstack11lll1_opy_ (u"ࠨࡣࡳࡴࠬད")]))
  else:
    bstack1l1l1ll1l_opy_.clear()
  global bstack1l1ll1111l_opy_
  global bstack111lll1l1l_opy_
  if bstack1l111l1l1_opy_:
    try:
      bstack11l11lll1l_opy_ = datetime.datetime.now()
      os.environ[bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫདྷ")] = bstack1ll11lll1l_opy_
      bstack1l1lll1ll_opy_(bstack11lllll1ll_opy_, CONFIG)
      cli.bstack1lllll11ll_opy_(bstack11lll1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡵࡧ࡯ࡤࡺࡥࡴࡶࡢࡥࡹࡺࡥ࡮ࡲࡷࡩࡩࠨན"), datetime.datetime.now() - bstack11l11lll1l_opy_)
    except Exception as e:
      logger.debug(bstack1l1l11l111_opy_.format(str(e)))
  global bstack1111lll1ll_opy_
  global bstack1l1ll11ll1_opy_
  global bstack11111l1lll_opy_
  global bstack1llll1l111_opy_
  global bstack1lll1l1lll_opy_
  global bstack111ll1111_opy_
  global bstack1l1l11l1l1_opy_
  global bstack1ll1ll1111_opy_
  global bstack11111ll11l_opy_
  global bstack111llll1l_opy_
  global bstack1l11l1l1ll_opy_
  global bstack1l11l1llll_opy_
  global bstack1lll1llll1_opy_
  global bstack1llllll111_opy_
  global bstack11l11ll1ll_opy_
  global bstack1l11llllll_opy_
  global bstack11l111ll1_opy_
  global bstack11lll111l_opy_
  global bstack111111ll1_opy_
  global bstack1l111111l_opy_
  global bstack1l11lll1l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1111lll1ll_opy_ = webdriver.Remote.__init__
    bstack1l1ll11ll1_opy_ = WebDriver.quit
    bstack1l11l1llll_opy_ = WebDriver.close
    bstack11l11ll1ll_opy_ = WebDriver.get
    bstack1l11lll1l_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1l1ll1111l_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack11l1l1l11_opy_
    bstack111lll1l1l_opy_ = bstack11l1l1l11_opy_()
  except Exception as e:
    pass
  try:
    global bstack1ll1ll1ll_opy_
    from QWeb.keywords import browser
    bstack1ll1ll1ll_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1lll1l11ll_opy_(CONFIG) and bstack1111l1l11l_opy_():
    if bstack11lllll11l_opy_() < version.parse(bstack1ll1l1l111_opy_):
      logger.error(bstack1l1l1ll11_opy_.format(bstack11lllll11l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11lll1_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬཔ")) and callable(getattr(RemoteConnection, bstack11lll1_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ཕ"))):
          RemoteConnection._get_proxy_url = bstack111ll11ll1_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack111ll11ll1_opy_
      except Exception as e:
        logger.error(bstack111l1l11ll_opy_.format(str(e)))
  if not CONFIG.get(bstack11lll1_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨབ"), False) and not bstack1l111l1l1_opy_:
    logger.info(bstack11l1l1l111_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack11lll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫབྷ") in CONFIG and str(CONFIG[bstack11lll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬམ")]).lower() != bstack11lll1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨཙ"):
      bstack1lll1111ll_opy_()
    elif bstack1ll11lll1l_opy_ != bstack11lll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪཚ") or (bstack1ll11lll1l_opy_ == bstack11lll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫཛ") and not bstack1l111l1l1_opy_):
      bstack11ll1llll1_opy_()
  if (bstack1ll11lll1l_opy_ in [bstack11lll1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫཛྷ"), bstack11lll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬཝ"), bstack11lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨཞ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1l1l11ll1l_opy_
        bstack111ll1111_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1l1lllll11_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1lll1l1lll_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack11l1ll1ll_opy_ + str(e))
    except Exception as e:
      bstack11l1l11l11_opy_(e, bstack1l1lllll11_opy_)
    if bstack1ll11lll1l_opy_ != bstack11lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩཟ"):
      bstack111l1ll11_opy_()
    bstack11111l1lll_opy_ = Output.start_test
    bstack1llll1l111_opy_ = Output.end_test
    bstack1l1l11l1l1_opy_ = TestStatus.__init__
    bstack11111ll11l_opy_ = pabot._run
    bstack111llll1l_opy_ = QueueItem.__init__
    bstack1l11l1l1ll_opy_ = pabot._create_command_for_execution
    bstack111111ll1_opy_ = pabot._report_results
  if bstack1ll11lll1l_opy_ == bstack11lll1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩའ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11l1l11l11_opy_(e, bstack1111ll1l1l_opy_)
    bstack1lll1llll1_opy_ = Runner.run_hook
    bstack1llllll111_opy_ = Step.run
  if bstack1ll11lll1l_opy_ == bstack11lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪཡ"):
    try:
      from _pytest.config import Config
      bstack11l111ll1_opy_ = Config.getoption
      from _pytest import runner
      bstack11lll111l_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack111llll1_opy_)
    try:
      from pytest_bdd import reporting
      bstack1l111111l_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11lll1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬར"))
  try:
    framework_name = bstack11lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫལ") if bstack1ll11lll1l_opy_ in [bstack11lll1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬཤ"), bstack11lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ཥ"), bstack11lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩས")] else bstack1l1ll1l11_opy_(bstack1ll11lll1l_opy_)
    bstack1ll1111ll1_opy_ = {
      bstack11lll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࠪཧ"): bstack11lll1_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬཨ") if bstack1ll11lll1l_opy_ == bstack11lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫཀྵ") and bstack1lll1ll11l_opy_() else framework_name,
      bstack11lll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩཪ"): bstack11l11l11l1_opy_(framework_name),
      bstack11lll1_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫཫ"): __version__,
      bstack11lll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨཬ"): bstack1ll11lll1l_opy_
    }
    if bstack1ll11lll1l_opy_ in bstack1l1llllll1_opy_ + bstack1l111l11ll_opy_:
      if bstack111ll11l_opy_.bstack1111lll11l_opy_(CONFIG):
        if bstack11lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ཭") in CONFIG:
          os.environ[bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ཮")] = os.getenv(bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ཯"), json.dumps(CONFIG[bstack11lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ཰")]))
          CONFIG[bstack11lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷཱࠬ")].pop(bstack11lll1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨིࠫ"), None)
          CONFIG[bstack11lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹཱིࠧ")].pop(bstack11lll1_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪུ࠭"), None)
        bstack1ll1111ll1_opy_[bstack11lll1_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ཱུࠩ")] = {
          bstack11lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨྲྀ"): bstack11lll1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ཷ"),
          bstack11lll1_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ླྀ"): str(bstack11lllll11l_opy_())
        }
    if bstack1ll11lll1l_opy_ not in [bstack11lll1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧཹ")] and not cli.is_running():
      bstack111l1l1l1_opy_, bstack1ll111ll1l_opy_ = bstack1ll1l11l_opy_.launch(CONFIG, bstack1ll1111ll1_opy_)
      if bstack1ll111ll1l_opy_.get(bstack11lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿེࠧ")) is not None and bstack111ll11l_opy_.bstack11lll1lll_opy_(CONFIG) is None:
        value = bstack1ll111ll1l_opy_[bstack11lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨཻ")].get(bstack11lll1_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵོࠪ"))
        if value is not None:
            CONFIG[bstack11lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻཽࠪ")] = value
        else:
          logger.debug(bstack11lll1_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡥࡣࡷࡥࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤཾ"))
  except Exception as e:
    logger.debug(bstack11l111lll_opy_.format(bstack11lll1_opy_ (u"࡚ࠬࡥࡴࡶࡋࡹࡧ࠭ཿ"), str(e)))
  if bstack1ll11lll1l_opy_ == bstack11lll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳྀ࠭"):
    bstack1l1111111_opy_ = True
    if bstack1l111l1l1_opy_ and bstack11l1l11ll_opy_:
      bstack1l1111lll1_opy_ = CONFIG.get(bstack11lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶཱྀࠫ"), {}).get(bstack11lll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪྂ"))
      bstack11l11111l1_opy_(bstack1l1l1ll11l_opy_)
    elif bstack1l111l1l1_opy_:
      bstack1l1111lll1_opy_ = CONFIG.get(bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ྃ"), {}).get(bstack11lll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ྄ࠬ"))
      global bstack1l1l11l11l_opy_
      try:
        if bstack11111ll111_opy_(bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ྅")]) and multiprocessing.current_process().name == bstack11lll1_opy_ (u"ࠬ࠶ࠧ྆"):
          bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ྇")].remove(bstack11lll1_opy_ (u"ࠧ࠮࡯ࠪྈ"))
          bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྉ")].remove(bstack11lll1_opy_ (u"ࠩࡳࡨࡧ࠭ྊ"))
          bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྋ")] = bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྌ")][0]
          with open(bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྍ")], bstack11lll1_opy_ (u"࠭ࡲࠨྎ")) as f:
            file_content = f.read()
          bstack111l11l1l1_opy_ = bstack11lll1_opy_ (u"ࠢࠣࠤࡩࡶࡴࡳࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡥ࡭ࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡁࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࠫࡿࢂ࠯࠻ࠡࡨࡵࡳࡲࠦࡰࡥࡤࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡔࡩࡨ࠻ࠡࡱࡪࡣࡩࡨࠠ࠾ࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡥࡧࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯࠭ࡹࡥ࡭ࡨ࠯ࠤࡦࡸࡧ࠭ࠢࡷࡩࡲࡶ࡯ࡳࡣࡵࡽࠥࡃࠠ࠱ࠫ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡶࡾࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡢࡴࡪࠤࡂࠦࡳࡵࡴࠫ࡭ࡳࡺࠨࡢࡴࡪ࠭࠰࠷࠰ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦࡺࡦࡩࡵࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡥࡸࠦࡥ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡸࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡵࡧࡠࡦࡥࠬࡸ࡫࡬ࡧ࠮ࡤࡶ࡬࠲ࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡥࡤ࠱ࡨࡴࡥࡢࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫ࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠮ࠩ࠯ࡵࡨࡸࡤࡺࡲࡢࡥࡨࠬ࠮ࡢ࡮ࠣࠤࠥྏ").format(str(bstack1l111l1l1_opy_))
          bstack1l1lll1lll_opy_ = bstack111l11l1l1_opy_ + file_content
          bstack111lllll1l_opy_ = bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྐ")] + bstack11lll1_opy_ (u"ࠩࡢࡦࡸࡺࡡࡤ࡭ࡢࡸࡪࡳࡰ࠯ࡲࡼࠫྑ")
          with open(bstack111lllll1l_opy_, bstack11lll1_opy_ (u"ࠪࡻࠬྒ")):
            pass
          with open(bstack111lllll1l_opy_, bstack11lll1_opy_ (u"ࠦࡼ࠱ࠢྒྷ")) as f:
            f.write(bstack1l1lll1lll_opy_)
          import subprocess
          process_data = subprocess.run([bstack11lll1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧྔ"), bstack111lllll1l_opy_])
          if os.path.exists(bstack111lllll1l_opy_):
            os.unlink(bstack111lllll1l_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack11111ll111_opy_(bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྕ")]):
            bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྖ")].remove(bstack11lll1_opy_ (u"ࠨ࠯ࡰࠫྗ"))
            bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ྘")].remove(bstack11lll1_opy_ (u"ࠪࡴࡩࡨࠧྙ"))
            bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྚ")] = bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྛ")][0]
          bstack11l11111l1_opy_(bstack1l1l1ll11l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྜ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11lll1_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩྜྷ")] = bstack11lll1_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪྞ")
          mod_globals[bstack11lll1_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫྟ")] = os.path.abspath(bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྠ")])
          exec(open(bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྡ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11lll1_opy_ (u"ࠬࡉࡡࡶࡩ࡫ࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠬྡྷ").format(str(e)))
          for driver in bstack1l1l11l11l_opy_:
            bstack1l1lllllll_opy_.append({
              bstack11lll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫྣ"): bstack1l111l1l1_opy_[bstack11lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྤ")],
              bstack11lll1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧྥ"): str(e),
              bstack11lll1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨྦ"): multiprocessing.current_process().name
            })
            bstack1lllll1l1l_opy_(driver, bstack11lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪྦྷ"), bstack11lll1_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢྨ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l1l11l11l_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1ll1l11111_opy_, CONFIG, logger)
      bstack11llll111l_opy_()
      bstack11llll11ll_opy_()
      percy.bstack1l1l1111ll_opy_()
      bstack1llll1111_opy_ = {
        bstack11lll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྩ"): args[0],
        bstack11lll1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭ྪ"): CONFIG,
        bstack11lll1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨྫ"): bstack111111ll1l_opy_,
        bstack11lll1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪྫྷ"): bstack1ll1l11111_opy_
      }
      if bstack11lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྭ") in CONFIG:
        bstack111lll111l_opy_ = bstack1l1ll1l11l_opy_(args, logger, CONFIG, bstack11ll11lll1_opy_, bstack1l1l111ll1_opy_)
        bstack1l11111111_opy_ = bstack111lll111l_opy_.bstack1lll11lll_opy_(run_on_browserstack, bstack1llll1111_opy_, bstack11111ll111_opy_(args))
      else:
        if bstack11111ll111_opy_(args):
          bstack1llll1111_opy_[bstack11lll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྮ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1llll1111_opy_,))
          test.start()
          test.join()
        else:
          bstack11l11111l1_opy_(bstack1l1l1ll11l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11lll1_opy_ (u"ࠫࡤࡥ࡮ࡢ࡯ࡨࡣࡤ࠭ྯ")] = bstack11lll1_opy_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧྰ")
          mod_globals[bstack11lll1_opy_ (u"࠭࡟ࡠࡨ࡬ࡰࡪࡥ࡟ࠨྱ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1ll11lll1l_opy_ == bstack11lll1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ྲ") or bstack1ll11lll1l_opy_ == bstack11lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧླ"):
    percy.init(bstack1ll1l11111_opy_, CONFIG, logger)
    percy.bstack1l1l1111ll_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack11l1l11l11_opy_(e, bstack1l1lllll11_opy_)
    bstack11llll111l_opy_()
    bstack11l11111l1_opy_(bstack1ll1lll11l_opy_)
    if bstack11ll11lll1_opy_:
      bstack1lll111ll1_opy_(bstack1ll1lll11l_opy_, args)
      if bstack11lll1_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧྴ") in args:
        i = args.index(bstack11lll1_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨྵ"))
        args.pop(i)
        args.pop(i)
      if bstack11lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྶ") not in CONFIG:
        CONFIG[bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨྷ")] = [{}]
        bstack1l1l111ll1_opy_ = 1
      if bstack1l1ll11l1_opy_ == 0:
        bstack1l1ll11l1_opy_ = 1
      args.insert(0, str(bstack1l1ll11l1_opy_))
      args.insert(0, str(bstack11lll1_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫྸ")))
    if bstack1ll1l11l_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack111l11ll1l_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack11lll11111_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11lll1_opy_ (u"ࠢࡓࡑࡅࡓ࡙ࡥࡏࡑࡖࡌࡓࡓ࡙ࠢྐྵ"),
        ).parse_args(bstack111l11ll1l_opy_)
        bstack11l11ll11l_opy_ = args.index(bstack111l11ll1l_opy_[0]) if len(bstack111l11ll1l_opy_) > 0 else len(args)
        args.insert(bstack11l11ll11l_opy_, str(bstack11lll1_opy_ (u"ࠨ࠯࠰ࡰ࡮ࡹࡴࡦࡰࡨࡶࠬྺ")))
        args.insert(bstack11l11ll11l_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡵࡳࡧࡵࡴࡠ࡮࡬ࡷࡹ࡫࡮ࡦࡴ࠱ࡴࡾ࠭ྻ"))))
        if bstack11111lll_opy_.bstack11111111_opy_(CONFIG):
          args.insert(bstack11l11ll11l_opy_, str(bstack11lll1_opy_ (u"ࠪ࠱࠲ࡲࡩࡴࡶࡨࡲࡪࡸࠧྼ")))
          args.insert(bstack11l11ll11l_opy_ + 1, str(bstack11lll1_opy_ (u"ࠫࡗ࡫ࡴࡳࡻࡉࡥ࡮ࡲࡥࡥ࠼ࡾࢁࠬ྽").format(bstack11111lll_opy_.bstack111l1l1l_opy_(CONFIG))))
        if bstack11lllll1l1_opy_(os.environ.get(bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࠪ྾"))) and str(os.environ.get(bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠪ྿"), bstack11lll1_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ࿀"))) != bstack11lll1_opy_ (u"ࠨࡰࡸࡰࡱ࠭࿁"):
          for bstack111lll11ll_opy_ in bstack11lll11111_opy_:
            args.remove(bstack111lll11ll_opy_)
          test_files = os.environ.get(bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘ࠭࿂")).split(bstack11lll1_opy_ (u"ࠪ࠰ࠬ࿃"))
          for bstack1l11l11l11_opy_ in test_files:
            args.append(bstack1l11l11l11_opy_)
      except Exception as e:
        logger.error(bstack11lll1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡤࡸࡹࡧࡣࡩ࡫ࡱ࡫ࠥࡲࡩࡴࡶࡨࡲࡪࡸࠠࡧࡱࡵࠤࢀࢃ࠮ࠡࡇࡵࡶࡴࡸࠠ࠮ࠢࡾࢁࠧ࿄").format(bstack1ll111111_opy_, e))
    pabot.main(args)
  elif bstack1ll11lll1l_opy_ == bstack11lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭࿅"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack11l1l11l11_opy_(e, bstack1l1lllll11_opy_)
    for a in args:
      if bstack11lll1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜࿆ࠬ") in a:
        bstack11l111111_opy_ = int(a.split(bstack11lll1_opy_ (u"ࠧ࠻ࠩ࿇"))[1])
      if bstack11lll1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ࿈") in a:
        bstack1l1111lll1_opy_ = str(a.split(bstack11lll1_opy_ (u"ࠩ࠽ࠫ࿉"))[1])
      if bstack11lll1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕࠪ࿊") in a:
        bstack11l11llll1_opy_ = str(a.split(bstack11lll1_opy_ (u"ࠫ࠿࠭࿋"))[1])
    bstack1l1ll1111_opy_ = None
    if bstack11lll1_opy_ (u"ࠬ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠫ࿌") in args:
      i = args.index(bstack11lll1_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬ࿍"))
      args.pop(i)
      bstack1l1ll1111_opy_ = args.pop(i)
    if bstack1l1ll1111_opy_ is not None:
      global bstack111l111111_opy_
      bstack111l111111_opy_ = bstack1l1ll1111_opy_
    bstack11l11111l1_opy_(bstack1ll1lll11l_opy_)
    run_cli(args)
    if bstack11lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫ࿎") in multiprocessing.current_process().__dict__.keys():
      for bstack111l1ll111_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l1lllllll_opy_.append(bstack111l1ll111_opy_)
  elif bstack1ll11lll1l_opy_ == bstack11lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ࿏"):
    bstack1111l11l1l_opy_ = bstack1lllllll1_opy_(args, logger, CONFIG, bstack11ll11lll1_opy_)
    bstack1111l11l1l_opy_.bstack1lll1ll11_opy_()
    bstack11llll111l_opy_()
    bstack1lll1lllll_opy_ = True
    bstack11l111ll1l_opy_ = bstack1111l11l1l_opy_.bstack1lll1l111_opy_()
    bstack1111l11l1l_opy_.bstack1llll1111_opy_(bstack111ll11l1_opy_)
    bstack1111l11l1l_opy_.bstack1111l1ll_opy_()
    bstack11lll1l1l1_opy_(bstack1ll11lll1l_opy_, CONFIG, bstack1111l11l1l_opy_.bstack1llll11l1_opy_())
    bstack11l11ll11_opy_ = bstack1111l11l1l_opy_.bstack1lll11lll_opy_(bstack1l1l1ll111_opy_, {
      bstack11lll1_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪ࿐"): bstack111111ll1l_opy_,
      bstack11lll1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ࿑"): bstack1ll1l11111_opy_,
      bstack11lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ࿒"): bstack11ll11lll1_opy_
    })
    try:
      bstack111l111ll1_opy_, bstack1ll1ll1lll_opy_ = map(list, zip(*bstack11l11ll11_opy_))
      bstack1ll1lll1ll_opy_ = bstack111l111ll1_opy_[0]
      for status_code in bstack1ll1ll1lll_opy_:
        if status_code != 0:
          bstack1llll1ll11_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11lll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡤࡺࡪࠦࡥࡳࡴࡲࡶࡸࠦࡡ࡯ࡦࠣࡷࡹࡧࡴࡶࡵࠣࡧࡴࡪࡥ࠯ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡀࠠࡼࡿࠥ࿓").format(str(e)))
  elif bstack1ll11lll1l_opy_ == bstack11lll1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭࿔"):
    try:
      from behave.__main__ import main as bstack11l11l111_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack11l1l11l11_opy_(e, bstack1111ll1l1l_opy_)
    bstack11llll111l_opy_()
    bstack1lll1lllll_opy_ = True
    bstack111l1l11_opy_ = 1
    if bstack11lll1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ࿕") in CONFIG:
      bstack111l1l11_opy_ = CONFIG[bstack11lll1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ࿖")]
    if bstack11lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ࿗") in CONFIG:
      bstack11lllllll1_opy_ = int(bstack111l1l11_opy_) * int(len(CONFIG[bstack11lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭࿘")]))
    else:
      bstack11lllllll1_opy_ = int(bstack111l1l11_opy_)
    config = Configuration(args)
    bstack11l1ll1l1l_opy_ = config.paths
    if len(bstack11l1ll1l1l_opy_) == 0:
      import glob
      pattern = bstack11lll1_opy_ (u"ࠫ࠯࠰࠯ࠫ࠰ࡩࡩࡦࡺࡵࡳࡧࠪ࿙")
      bstack1l1l1111l_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1l1l1111l_opy_)
      config = Configuration(args)
      bstack11l1ll1l1l_opy_ = config.paths
    bstack1llll1lll_opy_ = [os.path.normpath(item) for item in bstack11l1ll1l1l_opy_]
    bstack11ll1l11ll_opy_ = [os.path.normpath(item) for item in args]
    bstack11ll1ll111_opy_ = [item for item in bstack11ll1l11ll_opy_ if item not in bstack1llll1lll_opy_]
    import platform as pf
    if pf.system().lower() == bstack11lll1_opy_ (u"ࠬࡽࡩ࡯ࡦࡲࡻࡸ࠭࿚"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1llll1lll_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11ll111l1_opy_)))
                    for bstack11ll111l1_opy_ in bstack1llll1lll_opy_]
    bstack1lll1l1ll_opy_ = []
    for spec in bstack1llll1lll_opy_:
      bstack1lll111l1_opy_ = []
      bstack1lll111l1_opy_ += bstack11ll1ll111_opy_
      bstack1lll111l1_opy_.append(spec)
      bstack1lll1l1ll_opy_.append(bstack1lll111l1_opy_)
    execution_items = []
    for bstack1lll111l1_opy_ in bstack1lll1l1ll_opy_:
      if bstack11lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ࿛") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack11lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿜")]):
          item = {}
          item[bstack11lll1_opy_ (u"ࠨࡣࡵ࡫ࠬ࿝")] = bstack11lll1_opy_ (u"ࠩࠣࠫ࿞").join(bstack1lll111l1_opy_)
          item[bstack11lll1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ࿟")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack11lll1_opy_ (u"ࠫࡦࡸࡧࠨ࿠")] = bstack11lll1_opy_ (u"ࠬࠦࠧ࿡").join(bstack1lll111l1_opy_)
        item[bstack11lll1_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ࿢")] = 0
        execution_items.append(item)
    bstack1l111lll1l_opy_ = bstack1l111111ll_opy_(execution_items, bstack11lllllll1_opy_)
    for execution_item in bstack1l111lll1l_opy_:
      bstack111lll1l_opy_ = []
      for item in execution_item:
        bstack111lll1l_opy_.append(bstack111l1l111l_opy_(name=str(item[bstack11lll1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭࿣")]),
                                             target=bstack1lll11ll1l_opy_,
                                             args=(item[bstack11lll1_opy_ (u"ࠨࡣࡵ࡫ࠬ࿤")],)))
      for t in bstack111lll1l_opy_:
        t.start()
      for t in bstack111lll1l_opy_:
        t.join()
  else:
    bstack1lll1ll111_opy_(bstack1ll1l11l11_opy_)
  if not bstack1l111l1l1_opy_:
    bstack11llll1l11_opy_()
    if(bstack1ll11lll1l_opy_ in [bstack11lll1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ࿥"), bstack11lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ࿦")]):
      bstack1ll1111l11_opy_()
  bstack1l1l1llll1_opy_.bstack11llll11l_opy_()
def browserstack_initialize(bstack1ll1lllll1_opy_=None):
  logger.info(bstack11lll1_opy_ (u"ࠫࡗࡻ࡮࡯࡫ࡱ࡫࡙ࠥࡄࡌࠢࡺ࡭ࡹ࡮ࠠࡢࡴࡪࡷ࠿ࠦࠧ࿧") + str(bstack1ll1lllll1_opy_))
  run_on_browserstack(bstack1ll1lllll1_opy_, None, True)
@measure(event_name=EVENTS.bstack11ll1llll_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack11llll1l11_opy_():
  global CONFIG
  global bstack11lll11lll_opy_
  global bstack1llll1ll11_opy_
  global bstack1l111l111_opy_
  global bstack1lll1l11l_opy_
  bstack1111l1l11_opy_.bstack1llll11l11_opy_()
  if cli.is_running():
    bstack1l1l1ll1l_opy_.invoke(Events.bstack11111ll1ll_opy_)
  else:
    bstack1lll1l1l1_opy_ = bstack11111lll_opy_.bstack111ll1l1_opy_(config=CONFIG)
    bstack1lll1l1l1_opy_.bstack111111l11_opy_(CONFIG)
  if bstack11lll11lll_opy_ == bstack11lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ࿨"):
    if not cli.is_enabled(CONFIG):
      bstack1ll1l11l_opy_.stop()
  else:
    bstack1ll1l11l_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1ll11l11_opy_.bstack1lll1ll1ll_opy_()
  if bstack11lll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ࿩") in CONFIG and str(CONFIG[bstack11lll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ࿪")]).lower() != bstack11lll1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ࿫"):
    hashed_id, bstack1111l111ll_opy_ = bstack11l11l1lll_opy_()
  else:
    hashed_id, bstack1111l111ll_opy_ = get_build_link()
  bstack11ll1ll1l_opy_(hashed_id)
  logger.info(bstack11lll1_opy_ (u"ࠩࡖࡈࡐࠦࡲࡶࡰࠣࡩࡳࡪࡥࡥࠢࡩࡳࡷࠦࡩࡥ࠼ࠪ࿬") + bstack1lll1l11l_opy_.get_property(bstack11lll1_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ࿭"), bstack11lll1_opy_ (u"ࠫࠬ࿮")) + bstack11lll1_opy_ (u"ࠬ࠲ࠠࡵࡧࡶࡸ࡭ࡻࡢࠡ࡫ࡧ࠾ࠥ࠭࿯") + os.getenv(bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ࿰"), bstack11lll1_opy_ (u"ࠧࠨ࿱")))
  if hashed_id is not None and bstack1llll111ll_opy_() != -1:
    sessions = bstack1l1ll1lll1_opy_(hashed_id)
    bstack1lllll11l1_opy_(sessions, bstack1111l111ll_opy_)
  if bstack11lll11lll_opy_ == bstack11lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ࿲") and bstack1llll1ll11_opy_ != 0:
    sys.exit(bstack1llll1ll11_opy_)
  if bstack11lll11lll_opy_ == bstack11lll1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ࿳") and bstack1l111l111_opy_ != 0:
    sys.exit(bstack1l111l111_opy_)
def bstack11ll1ll1l_opy_(new_id):
    global bstack1111l1ll11_opy_
    bstack1111l1ll11_opy_ = new_id
def bstack1l1ll1l11_opy_(bstack1l1llll1ll_opy_):
  if bstack1l1llll1ll_opy_:
    return bstack1l1llll1ll_opy_.capitalize()
  else:
    return bstack11lll1_opy_ (u"ࠪࠫ࿴")
@measure(event_name=EVENTS.bstack11111l11l_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack1ll11l11l_opy_(bstack11ll1ll11l_opy_):
  if bstack11lll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ࿵") in bstack11ll1ll11l_opy_ and bstack11ll1ll11l_opy_[bstack11lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ࿶")] != bstack11lll1_opy_ (u"࠭ࠧ࿷"):
    return bstack11ll1ll11l_opy_[bstack11lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ࿸")]
  else:
    bstack1lll11l1l1_opy_ = bstack11lll1_opy_ (u"ࠣࠤ࿹")
    if bstack11lll1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ࿺") in bstack11ll1ll11l_opy_ and bstack11ll1ll11l_opy_[bstack11lll1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ࿻")] != None:
      bstack1lll11l1l1_opy_ += bstack11ll1ll11l_opy_[bstack11lll1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ࿼")] + bstack11lll1_opy_ (u"ࠧ࠲ࠠࠣ࿽")
      if bstack11ll1ll11l_opy_[bstack11lll1_opy_ (u"࠭࡯ࡴࠩ࿾")] == bstack11lll1_opy_ (u"ࠢࡪࡱࡶࠦ࿿"):
        bstack1lll11l1l1_opy_ += bstack11lll1_opy_ (u"ࠣ࡫ࡒࡗࠥࠨက")
      bstack1lll11l1l1_opy_ += (bstack11ll1ll11l_opy_[bstack11lll1_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ခ")] or bstack11lll1_opy_ (u"ࠪࠫဂ"))
      return bstack1lll11l1l1_opy_
    else:
      bstack1lll11l1l1_opy_ += bstack1l1ll1l11_opy_(bstack11ll1ll11l_opy_[bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬဃ")]) + bstack11lll1_opy_ (u"ࠧࠦࠢင") + (
              bstack11ll1ll11l_opy_[bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨစ")] or bstack11lll1_opy_ (u"ࠧࠨဆ")) + bstack11lll1_opy_ (u"ࠣ࠮ࠣࠦဇ")
      if bstack11ll1ll11l_opy_[bstack11lll1_opy_ (u"ࠩࡲࡷࠬဈ")] == bstack11lll1_opy_ (u"࡛ࠥ࡮ࡴࡤࡰࡹࡶࠦဉ"):
        bstack1lll11l1l1_opy_ += bstack11lll1_opy_ (u"ࠦ࡜࡯࡮ࠡࠤည")
      bstack1lll11l1l1_opy_ += bstack11ll1ll11l_opy_[bstack11lll1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩဋ")] or bstack11lll1_opy_ (u"࠭ࠧဌ")
      return bstack1lll11l1l1_opy_
@measure(event_name=EVENTS.bstack11l1111lll_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack111l1ll1l1_opy_(bstack11lllllll_opy_):
  if bstack11lllllll_opy_ == bstack11lll1_opy_ (u"ࠢࡥࡱࡱࡩࠧဍ"):
    return bstack11lll1_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽࡫ࡷ࡫ࡥ࡯࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥ࡫ࡷ࡫ࡥ࡯ࠤࡁࡇࡴࡳࡰ࡭ࡧࡷࡩࡩࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫဎ")
  elif bstack11lllllll_opy_ == bstack11lll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤဏ"):
    return bstack11lll1_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡸࡥࡥ࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡶࡪࡪࠢ࠿ࡈࡤ࡭ࡱ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭တ")
  elif bstack11lllllll_opy_ == bstack11lll1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦထ"):
    return bstack11lll1_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡨࡴࡨࡩࡳࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡨࡴࡨࡩࡳࠨ࠾ࡑࡣࡶࡷࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬဒ")
  elif bstack11lllllll_opy_ == bstack11lll1_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧဓ"):
    return bstack11lll1_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡵࡩࡩࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡳࡧࡧࠦࡃࡋࡲࡳࡱࡵࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩန")
  elif bstack11lllllll_opy_ == bstack11lll1_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࠤပ"):
    return bstack11lll1_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࠨ࡫ࡥࡢ࠵࠵࠺ࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࠣࡦࡧࡤ࠷࠷࠼ࠢ࠿ࡖ࡬ࡱࡪࡵࡵࡵ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧဖ")
  elif bstack11lllllll_opy_ == bstack11lll1_opy_ (u"ࠥࡶࡺࡴ࡮ࡪࡰࡪࠦဗ"):
    return bstack11lll1_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡢ࡭ࡣࡦ࡯ࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡢ࡭ࡣࡦ࡯ࠧࡄࡒࡶࡰࡱ࡭ࡳ࡭࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬဘ")
  else:
    return bstack11lll1_opy_ (u"ࠬࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡤ࡯ࡥࡨࡱ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡤ࡯ࡥࡨࡱࠢ࠿ࠩမ") + bstack1l1ll1l11_opy_(
      bstack11lllllll_opy_) + bstack11lll1_opy_ (u"࠭࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬယ")
def bstack11l1ll1l11_opy_(session):
  return bstack11lll1_opy_ (u"ࠧ࠽ࡶࡵࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡷࡵࡷࠣࡀ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠲ࡴࡡ࡮ࡧࠥࡂࡁࡧࠠࡩࡴࡨࡪࡂࠨࡻࡾࠤࠣࡸࡦࡸࡧࡦࡶࡀࠦࡤࡨ࡬ࡢࡰ࡮ࠦࡃࢁࡽ࠽࠱ࡤࡂࡁ࠵ࡴࡥࡀࡾࢁࢀࢃ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾࠲ࡸࡷࡄࠧရ").format(
    session[bstack11lll1_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣࡠࡷࡵࡰࠬလ")], bstack1ll11l11l_opy_(session), bstack111l1ll1l1_opy_(session[bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡷࡥࡹࡻࡳࠨဝ")]),
    bstack111l1ll1l1_opy_(session[bstack11lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪသ")]),
    bstack1l1ll1l11_opy_(session[bstack11lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬဟ")] or session[bstack11lll1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬဠ")] or bstack11lll1_opy_ (u"࠭ࠧအ")) + bstack11lll1_opy_ (u"ࠢࠡࠤဢ") + (session[bstack11lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪဣ")] or bstack11lll1_opy_ (u"ࠩࠪဤ")),
    session[bstack11lll1_opy_ (u"ࠪࡳࡸ࠭ဥ")] + bstack11lll1_opy_ (u"ࠦࠥࠨဦ") + session[bstack11lll1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩဧ")], session[bstack11lll1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨဨ")] or bstack11lll1_opy_ (u"ࠧࠨဩ"),
    session[bstack11lll1_opy_ (u"ࠨࡥࡵࡩࡦࡺࡥࡥࡡࡤࡸࠬဪ")] if session[bstack11lll1_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭ါ")] else bstack11lll1_opy_ (u"ࠪࠫာ"))
@measure(event_name=EVENTS.bstack1lll11l11l_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def bstack1lllll11l1_opy_(sessions, bstack1111l111ll_opy_):
  try:
    bstack11l1lll111_opy_ = bstack11lll1_opy_ (u"ࠦࠧိ")
    if not os.path.exists(bstack1ll11llll_opy_):
      os.mkdir(bstack1ll11llll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11lll1_opy_ (u"ࠬࡧࡳࡴࡧࡷࡷ࠴ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪီ")), bstack11lll1_opy_ (u"࠭ࡲࠨု")) as f:
      bstack11l1lll111_opy_ = f.read()
    bstack11l1lll111_opy_ = bstack11l1lll111_opy_.replace(bstack11lll1_opy_ (u"ࠧࡼࠧࡕࡉࡘ࡛ࡌࡕࡕࡢࡇࡔ࡛ࡎࡕࠧࢀࠫူ"), str(len(sessions)))
    bstack11l1lll111_opy_ = bstack11l1lll111_opy_.replace(bstack11lll1_opy_ (u"ࠨࡽࠨࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠫࡽࠨေ"), bstack1111l111ll_opy_)
    bstack11l1lll111_opy_ = bstack11l1lll111_opy_.replace(bstack11lll1_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢࡒࡆࡓࡅࠦࡿࠪဲ"),
                                              sessions[0].get(bstack11lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡥࡲ࡫ࠧဳ")) if sessions[0] else bstack11lll1_opy_ (u"ࠫࠬဴ"))
    with open(os.path.join(bstack1ll11llll_opy_, bstack11lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡷ࡫ࡰࡰࡴࡷ࠲࡭ࡺ࡭࡭ࠩဵ")), bstack11lll1_opy_ (u"࠭ࡷࠨံ")) as stream:
      stream.write(bstack11l1lll111_opy_.split(bstack11lll1_opy_ (u"ࠧࡼࠧࡖࡉࡘ࡙ࡉࡐࡐࡖࡣࡉࡇࡔࡂࠧࢀ့ࠫ"))[0])
      for session in sessions:
        stream.write(bstack11l1ll1l11_opy_(session))
      stream.write(bstack11l1lll111_opy_.split(bstack11lll1_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁࠬး"))[1])
    logger.info(bstack11lll1_opy_ (u"ࠩࡊࡩࡳ࡫ࡲࡢࡶࡨࡨࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡧࡻࡩ࡭ࡦࠣࡥࡷࡺࡩࡧࡣࡦࡸࡸࠦࡡࡵࠢࡾࢁ္ࠬ").format(bstack1ll11llll_opy_));
  except Exception as e:
    logger.debug(bstack1l1l1ll1ll_opy_.format(str(e)))
def bstack1l1ll1lll1_opy_(hashed_id):
  global CONFIG
  try:
    bstack11l11lll1l_opy_ = datetime.datetime.now()
    host = bstack11lll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯်ࠪ") if bstack11lll1_opy_ (u"ࠫࡦࡶࡰࠨျ") in CONFIG else bstack11lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ြ")
    user = CONFIG[bstack11lll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨွ")]
    key = CONFIG[bstack11lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪှ")]
    bstack11l11l1ll1_opy_ = bstack11lll1_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧဿ") if bstack11lll1_opy_ (u"ࠩࡤࡴࡵ࠭၀") in CONFIG else (bstack11lll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧ၁") if CONFIG.get(bstack11lll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨ၂")) else bstack11lll1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ၃"))
    host = bstack111ll111ll_opy_(cli.config, [bstack11lll1_opy_ (u"ࠨࡡࡱ࡫ࡶࠦ၄"), bstack11lll1_opy_ (u"ࠢࡢࡲࡳࡅࡺࡺ࡯࡮ࡣࡷࡩࠧ၅"), bstack11lll1_opy_ (u"ࠣࡣࡳ࡭ࠧ၆")], host) if bstack11lll1_opy_ (u"ࠩࡤࡴࡵ࠭၇") in CONFIG else bstack111ll111ll_opy_(cli.config, [bstack11lll1_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ၈"), bstack11lll1_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ၉"), bstack11lll1_opy_ (u"ࠧࡧࡰࡪࠤ၊")], host)
    url = bstack11lll1_opy_ (u"࠭ࡻࡾ࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡵࡨࡷࡸ࡯࡯࡯ࡵ࠱࡮ࡸࡵ࡮ࠨ။").format(host, bstack11l11l1ll1_opy_, hashed_id)
    headers = {
      bstack11lll1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭၌"): bstack11lll1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ၍"),
    }
    proxies = bstack1lll111l11_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1lllll11ll_opy_(bstack11lll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡨࡧࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࡥ࡬ࡪࡵࡷࠦ၎"), datetime.datetime.now() - bstack11l11lll1l_opy_)
      return list(map(lambda session: session[bstack11lll1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ၏")], response.json()))
  except Exception as e:
    logger.debug(bstack11111111l_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack1l1llllll_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def get_build_link():
  global CONFIG
  global bstack1111l1ll11_opy_
  try:
    if bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧၐ") in CONFIG:
      bstack11l11lll1l_opy_ = datetime.datetime.now()
      host = bstack11lll1_opy_ (u"ࠬࡧࡰࡪ࠯ࡦࡰࡴࡻࡤࠨၑ") if bstack11lll1_opy_ (u"࠭ࡡࡱࡲࠪၒ") in CONFIG else bstack11lll1_opy_ (u"ࠧࡢࡲ࡬ࠫၓ")
      user = CONFIG[bstack11lll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪၔ")]
      key = CONFIG[bstack11lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬၕ")]
      bstack11l11l1ll1_opy_ = bstack11lll1_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩၖ") if bstack11lll1_opy_ (u"ࠫࡦࡶࡰࠨၗ") in CONFIG else bstack11lll1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧၘ")
      url = bstack11lll1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡼࡿ࠽ࡿࢂࡆࡻࡾ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠯࡬ࡶࡳࡳ࠭ၙ").format(user, key, host, bstack11l11l1ll1_opy_)
      if cli.is_enabled(CONFIG):
        bstack1111l111ll_opy_, hashed_id = cli.bstack11l1l111l_opy_()
        logger.info(bstack1l1l111ll_opy_.format(bstack1111l111ll_opy_))
        return [hashed_id, bstack1111l111ll_opy_]
      else:
        headers = {
          bstack11lll1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭ၚ"): bstack11lll1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫၛ"),
        }
        if bstack11lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫၜ") in CONFIG:
          params = {bstack11lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨၝ"): CONFIG[bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧၞ")], bstack11lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨၟ"): CONFIG[bstack11lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨၠ")]}
        else:
          params = {bstack11lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬၡ"): CONFIG[bstack11lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫၢ")]}
        proxies = bstack1lll111l11_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack1l11l1ll1_opy_ = response.json()[0][bstack11lll1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡢࡶ࡫࡯ࡨࠬၣ")]
          if bstack1l11l1ll1_opy_:
            bstack1111l111ll_opy_ = bstack1l11l1ll1_opy_[bstack11lll1_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧၤ")].split(bstack11lll1_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦ࠱ࡧࡻࡩ࡭ࡦࠪၥ"))[0] + bstack11lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡷ࠴࠭ၦ") + bstack1l11l1ll1_opy_[
              bstack11lll1_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩၧ")]
            logger.info(bstack1l1l111ll_opy_.format(bstack1111l111ll_opy_))
            bstack1111l1ll11_opy_ = bstack1l11l1ll1_opy_[bstack11lll1_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪၨ")]
            bstack11l11l1l1l_opy_ = CONFIG[bstack11lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫၩ")]
            if bstack11lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫၪ") in CONFIG:
              bstack11l11l1l1l_opy_ += bstack11lll1_opy_ (u"ࠪࠤࠬၫ") + CONFIG[bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ၬ")]
            if bstack11l11l1l1l_opy_ != bstack1l11l1ll1_opy_[bstack11lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪၭ")]:
              logger.debug(bstack1l11lll111_opy_.format(bstack1l11l1ll1_opy_[bstack11lll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫၮ")], bstack11l11l1l1l_opy_))
            cli.bstack1lllll11ll_opy_(bstack11lll1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࡭ࡥࡵࡡࡥࡹ࡮ࡲࡤࡠ࡮࡬ࡲࡰࠨၯ"), datetime.datetime.now() - bstack11l11lll1l_opy_)
            return [bstack1l11l1ll1_opy_[bstack11lll1_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫၰ")], bstack1111l111ll_opy_]
    else:
      logger.warn(bstack11ll1l1lll_opy_)
  except Exception as e:
    logger.debug(bstack111l111lll_opy_.format(str(e)))
  return [None, None]
def bstack111l1l1lll_opy_(url, bstack11llllll11_opy_=False):
  global CONFIG
  global bstack111ll11l11_opy_
  if not bstack111ll11l11_opy_:
    hostname = bstack1lll1l1111_opy_(url)
    is_private = bstack11l11111ll_opy_(hostname)
    if (bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ၱ") in CONFIG and not bstack11lllll1l1_opy_(CONFIG[bstack11lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧၲ")])) and (is_private or bstack11llllll11_opy_):
      bstack111ll11l11_opy_ = hostname
def bstack1lll1l1111_opy_(url):
  return urlparse(url).hostname
def bstack11l11111ll_opy_(hostname):
  for bstack11l1111l1l_opy_ in bstack111ll111l_opy_:
    regex = re.compile(bstack11l1111l1l_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack11lll1111_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack11l1l11111_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack11l111111_opy_
  bstack1l1l1l1ll1_opy_ = not (bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၳ"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack11lll1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၴ"), None))
  bstack11l1l1111_opy_ = getattr(driver, bstack11lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ၵ"), None) != True
  bstack1111l1l1l1_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၶ"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack11lll1_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၷ"), None)
  if bstack1111l1l1l1_opy_:
    if not bstack1l111l1ll1_opy_():
      logger.warning(bstack11lll1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷ࠳ࠨၸ"))
      return {}
    logger.debug(bstack11lll1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧၹ"))
    logger.debug(perform_scan(driver, driver_command=bstack11lll1_opy_ (u"ࠫࡪࡾࡥࡤࡷࡷࡩࡘࡩࡲࡪࡲࡷࠫၺ")))
    results = bstack1ll1l1l1l_opy_(bstack11lll1_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸࡸࠨၻ"))
    if results is not None and results.get(bstack11lll1_opy_ (u"ࠨࡩࡴࡵࡸࡩࡸࠨၼ")) is not None:
        return results[bstack11lll1_opy_ (u"ࠢࡪࡵࡶࡹࡪࡹࠢၽ")]
    logger.error(bstack11lll1_opy_ (u"ࠣࡐࡲࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡗ࡫ࡳࡶ࡮ࡷࡷࠥࡽࡥࡳࡧࠣࡪࡴࡻ࡮ࡥ࠰ࠥၾ"))
    return []
  if not bstack111ll11l_opy_.bstack1111l11lll_opy_(CONFIG, bstack11l111111_opy_) or (bstack11l1l1111_opy_ and bstack1l1l1l1ll1_opy_):
    logger.warning(bstack11lll1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶ࠲ࠧၿ"))
    return {}
  try:
    logger.debug(bstack11lll1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧႀ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack11ll1111l_opy_.bstack1l111lll1_opy_)
    return results
  except Exception:
    logger.error(bstack11lll1_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡹࡨࡶࡪࠦࡦࡰࡷࡱࡨ࠳ࠨႁ"))
    return {}
@measure(event_name=EVENTS.bstack1l1111ll1l_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack11l111111_opy_
  bstack1l1l1l1ll1_opy_ = not (bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩႂ"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack11lll1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬႃ"), None))
  bstack11l1l1111_opy_ = getattr(driver, bstack11lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧႄ"), None) != True
  bstack1111l1l1l1_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨႅ"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack11lll1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫႆ"), None)
  if bstack1111l1l1l1_opy_:
    if not bstack1l111l1ll1_opy_():
      logger.warning(bstack11lll1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡳࡶ࡯ࡰࡥࡷࡿ࠮ࠣႇ"))
      return {}
    logger.debug(bstack11lll1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺࠩႈ"))
    logger.debug(perform_scan(driver, driver_command=bstack11lll1_opy_ (u"ࠬ࡫ࡸࡦࡥࡸࡸࡪ࡙ࡣࡳ࡫ࡳࡸࠬႉ")))
    results = bstack1ll1l1l1l_opy_(bstack11lll1_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡙ࡵ࡮࡯ࡤࡶࡾࠨႊ"))
    if results is not None and results.get(bstack11lll1_opy_ (u"ࠢࡴࡷࡰࡱࡦࡸࡹࠣႋ")) is not None:
        return results[bstack11lll1_opy_ (u"ࠣࡵࡸࡱࡲࡧࡲࡺࠤႌ")]
    logger.error(bstack11lll1_opy_ (u"ࠤࡑࡳࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡘࡥࡴࡷ࡯ࡸࡸࠦࡓࡶ࡯ࡰࡥࡷࡿࠠࡸࡣࡶࠤ࡫ࡵࡵ࡯ࡦ࠱ႍࠦ"))
    return {}
  if not bstack111ll11l_opy_.bstack1111l11lll_opy_(CONFIG, bstack11l111111_opy_) or (bstack11l1l1111_opy_ and bstack1l1l1l1ll1_opy_):
    logger.warning(bstack11lll1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠴ࠢႎ"))
    return {}
  try:
    logger.debug(bstack11lll1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺࠩႏ"))
    logger.debug(perform_scan(driver))
    bstack1111111ll_opy_ = driver.execute_async_script(bstack11ll1111l_opy_.bstack1l11lll1ll_opy_)
    return bstack1111111ll_opy_
  except Exception:
    logger.error(bstack11lll1_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡸࡱࡲࡧࡲࡺࠢࡺࡥࡸࠦࡦࡰࡷࡱࡨ࠳ࠨ႐"))
    return {}
def bstack1l111l1ll1_opy_():
  global CONFIG
  global bstack11l111111_opy_
  bstack1l1l11ll1_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭႑"), None) and bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ႒"), None)
  if not bstack111ll11l_opy_.bstack1111l11lll_opy_(CONFIG, bstack11l111111_opy_) or not bstack1l1l11ll1_opy_:
        logger.warning(bstack11lll1_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡲࡦࡵࡸࡰࡹࡹ࠮ࠣ႓"))
        return False
  return True
def bstack1ll1l1l1l_opy_(bstack111ll111l1_opy_):
    bstack111l1l1l11_opy_ = bstack1ll1l11l_opy_.current_test_uuid() if bstack1ll1l11l_opy_.current_test_uuid() else bstack1ll11l11_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack1111lllll1_opy_(bstack111l1l1l11_opy_, bstack111ll111l1_opy_))
        try:
            return future.result(timeout=bstack111ll11l1l_opy_)
        except TimeoutError:
            logger.error(bstack11lll1_opy_ (u"ࠤࡗ࡭ࡲ࡫࡯ࡶࡶࠣࡥ࡫ࡺࡥࡳࠢࡾࢁࡸࠦࡷࡩ࡫࡯ࡩࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡓࡧࡶࡹࡱࡺࡳࠣ႔").format(bstack111ll11l1l_opy_))
        except Exception as ex:
            logger.debug(bstack11lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡵࡩࡹࡸࡩࡦࡸ࡬ࡲ࡬ࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡼࡿ࠱ࠤࡊࡸࡲࡰࡴࠣ࠱ࠥࢁࡽࠣ႕").format(bstack111ll111l1_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack111ll1l111_opy_, stage=STAGE.bstack11ll1ll11_opy_, bstack1lll11l1l1_opy_=bstack1l11llll1_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack11l111111_opy_
  bstack1l1l1l1ll1_opy_ = not (bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ႖"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack11lll1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ႗"), None))
  bstack11lll1ll11_opy_ = not (bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭႘"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack11lll1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ႙"), None))
  bstack11l1l1111_opy_ = getattr(driver, bstack11lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨႚ"), None) != True
  if not bstack111ll11l_opy_.bstack1111l11lll_opy_(CONFIG, bstack11l111111_opy_) or (bstack11l1l1111_opy_ and bstack1l1l1l1ll1_opy_ and bstack11lll1ll11_opy_):
    logger.warning(bstack11lll1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡸࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡣࡢࡰ࠱ࠦႛ"))
    return {}
  try:
    bstack111111l1l_opy_ = bstack11lll1_opy_ (u"ࠪࡥࡵࡶࠧႜ") in CONFIG and CONFIG.get(bstack11lll1_opy_ (u"ࠫࡦࡶࡰࠨႝ"), bstack11lll1_opy_ (u"ࠬ࠭႞"))
    session_id = getattr(driver, bstack11lll1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠪ႟"), None)
    if not session_id:
      logger.warning(bstack11lll1_opy_ (u"ࠢࡏࡱࠣࡷࡪࡹࡳࡪࡱࡱࠤࡎࡊࠠࡧࡱࡸࡲࡩࠦࡦࡰࡴࠣࡨࡷ࡯ࡶࡦࡴࠥႠ"))
      return {bstack11lll1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢႡ"): bstack11lll1_opy_ (u"ࠤࡑࡳࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࠢࡩࡳࡺࡴࡤࠣႢ")}
    if bstack111111l1l_opy_:
      try:
        bstack1ll1l1ll1_opy_ = {
              bstack11lll1_opy_ (u"ࠪࡸ࡭ࡐࡷࡵࡖࡲ࡯ࡪࡴࠧႣ"): os.environ.get(bstack11lll1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩႤ"), os.environ.get(bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩႥ"), bstack11lll1_opy_ (u"࠭ࠧႦ"))),
              bstack11lll1_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧႧ"): bstack1ll1l11l_opy_.current_test_uuid() if bstack1ll1l11l_opy_.current_test_uuid() else bstack1ll11l11_opy_.current_hook_uuid(),
              bstack11lll1_opy_ (u"ࠨࡣࡸࡸ࡭ࡎࡥࡢࡦࡨࡶࠬႨ"): os.environ.get(bstack11lll1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧႩ")),
              bstack11lll1_opy_ (u"ࠪࡷࡨࡧ࡮ࡕ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪႪ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack11lll1_opy_ (u"ࠫࡹ࡮ࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩႫ"): os.environ.get(bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪႬ"), bstack11lll1_opy_ (u"࠭ࠧႭ")),
              bstack11lll1_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪࠧႮ"): kwargs.get(bstack11lll1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠࡥࡲࡱࡲࡧ࡮ࡥࠩႯ"), None) or bstack11lll1_opy_ (u"ࠩࠪႰ")
          }
        if not hasattr(thread_local, bstack11lll1_opy_ (u"ࠪࡦࡦࡹࡥࡠࡣࡳࡴࡤࡧ࠱࠲ࡻࡢࡷࡨࡸࡩࡱࡶࠪႱ")):
            scripts = {bstack11lll1_opy_ (u"ࠫࡸࡩࡡ࡯ࠩႲ"): bstack11ll1111l_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack1l1lll1111_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack1l1lll1111_opy_[bstack11lll1_opy_ (u"ࠬࡹࡣࡢࡰࠪႳ")] = bstack1l1lll1111_opy_[bstack11lll1_opy_ (u"࠭ࡳࡤࡣࡱࠫႴ")] % json.dumps(bstack1ll1l1ll1_opy_)
        bstack11ll1111l_opy_.bstack11ll111111_opy_(bstack1l1lll1111_opy_)
        bstack11ll1111l_opy_.store()
        bstack11l11l1ll_opy_ = driver.execute_script(bstack11ll1111l_opy_.perform_scan)
      except Exception as bstack11ll1l111_opy_:
        logger.info(bstack11lll1_opy_ (u"ࠢࡂࡲࡳ࡭ࡺࡳࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࠢႵ") + str(bstack11ll1l111_opy_))
        bstack11l11l1ll_opy_ = {bstack11lll1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢႶ"): str(bstack11ll1l111_opy_)}
    else:
      bstack11l11l1ll_opy_ = driver.execute_async_script(bstack11ll1111l_opy_.perform_scan, {bstack11lll1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࠩႷ"): kwargs.get(bstack11lll1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢࡧࡴࡳ࡭ࡢࡰࡧࠫႸ"), None) or bstack11lll1_opy_ (u"ࠫࠬႹ")})
    return bstack11l11l1ll_opy_
  except Exception as err:
    logger.error(bstack11lll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡴࡸࡲࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡣࡢࡰ࠱ࠤࢀࢃࠢႺ").format(str(err)))
    return {}