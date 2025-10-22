# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
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
from browserstack_sdk.bstack11ll111lll_opy_ import bstack1l11llll1l_opy_
from browserstack_sdk.bstack1ll1lllll_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack1ll1111l11_opy_():
  global CONFIG
  headers = {
        bstack111l1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩਡ"): bstack111l1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧਢ"),
      }
  proxies = bstack1l1111l1l1_opy_(CONFIG, bstack1l1l11l1ll_opy_)
  try:
    response = requests.get(bstack1l1l11l1ll_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack11111ll111_opy_ = response.json()[bstack111l1l_opy_ (u"ࠬ࡮ࡵࡣࡵࠪਣ")]
      logger.debug(bstack1l1lllllll_opy_.format(response.json()))
      return bstack11111ll111_opy_
    else:
      logger.debug(bstack1l1l1l1ll1_opy_.format(bstack111l1l_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧਤ")))
  except Exception as e:
    logger.debug(bstack1l1l1l1ll1_opy_.format(e))
def bstack111l1l1l1l_opy_(hub_url):
  global CONFIG
  url = bstack111l1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤਥ")+  hub_url + bstack111l1l_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣਦ")
  headers = {
        bstack111l1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨਧ"): bstack111l1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ਨ"),
      }
  proxies = bstack1l1111l1l1_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11111l111_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1111lllll_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack1l1l1ll11l_opy_, stage=STAGE.bstack1ll1ll111_opy_)
def bstack1lll1lllll_opy_():
  try:
    global bstack1l111l11l1_opy_
    bstack11111ll111_opy_ = bstack1ll1111l11_opy_()
    bstack1ll11llll1_opy_ = []
    results = []
    for bstack1ll1111l1l_opy_ in bstack11111ll111_opy_:
      bstack1ll11llll1_opy_.append(bstack1l111lll11_opy_(target=bstack111l1l1l1l_opy_,args=(bstack1ll1111l1l_opy_,)))
    for t in bstack1ll11llll1_opy_:
      t.start()
    for t in bstack1ll11llll1_opy_:
      results.append(t.join())
    bstack11l11l1ll1_opy_ = {}
    for item in results:
      hub_url = item[bstack111l1l_opy_ (u"ࠫ࡭ࡻࡢࡠࡷࡵࡰࠬ਩")]
      latency = item[bstack111l1l_opy_ (u"ࠬࡲࡡࡵࡧࡱࡧࡾ࠭ਪ")]
      bstack11l11l1ll1_opy_[hub_url] = latency
    bstack1l1ll1lll_opy_ = min(bstack11l11l1ll1_opy_, key= lambda x: bstack11l11l1ll1_opy_[x])
    bstack1l111l11l1_opy_ = bstack1l1ll1lll_opy_
    logger.debug(bstack11111lll1_opy_.format(bstack1l1ll1lll_opy_))
  except Exception as e:
    logger.debug(bstack1ll1lll11l_opy_.format(e))
from browserstack_sdk.bstack111ll11l_opy_ import *
from browserstack_sdk.bstack11111111_opy_ import *
from browserstack_sdk.bstack11l1l1ll_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack1l11l1lll_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack11l11ll11_opy_, stage=STAGE.bstack1ll1ll111_opy_)
def bstack1l111l11l_opy_():
    global bstack1l111l11l1_opy_
    try:
        bstack1l11l111l_opy_ = bstack111111lll1_opy_()
        bstack1l1ll1l1l_opy_(bstack1l11l111l_opy_)
        hub_url = bstack1l11l111l_opy_.get(bstack111l1l_opy_ (u"ࠨࡵࡳ࡮ࠥਫ"), bstack111l1l_opy_ (u"ࠢࠣਬ"))
        if hub_url.endswith(bstack111l1l_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩਭ")):
            hub_url = hub_url.rsplit(bstack111l1l_opy_ (u"ࠩ࠲ࡻࡩ࠵ࡨࡶࡤࠪਮ"), 1)[0]
        if hub_url.startswith(bstack111l1l_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࠫਯ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack111l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴࠭ਰ")):
            hub_url = hub_url[8:]
        bstack1l111l11l1_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack111111lll1_opy_():
    global CONFIG
    bstack11l1lll1l_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ਱"), {}).get(bstack111l1l_opy_ (u"࠭ࡧࡳ࡫ࡧࡒࡦࡳࡥࠨਲ"), bstack111l1l_opy_ (u"ࠧࡏࡑࡢࡋࡗࡏࡄࡠࡐࡄࡑࡊࡥࡐࡂࡕࡖࡉࡉ࠭ਲ਼"))
    if not isinstance(bstack11l1lll1l_opy_, str):
        raise ValueError(bstack111l1l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡈࡴ࡬ࡨࠥࡴࡡ࡮ࡧࠣࡱࡺࡹࡴࠡࡤࡨࠤࡦࠦࡶࡢ࡮࡬ࡨࠥࡹࡴࡳ࡫ࡱ࡫ࠧ਴"))
    try:
        bstack1l11l111l_opy_ = bstack1l11ll1111_opy_(bstack11l1lll1l_opy_)
        return bstack1l11l111l_opy_
    except Exception as e:
        logger.error(bstack111l1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣਵ").format(str(e)))
        return {}
def bstack1l11ll1111_opy_(bstack11l1lll1l_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack111l1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬਸ਼")] or not CONFIG[bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ਷")]:
            raise ValueError(bstack111l1l_opy_ (u"ࠧࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠠࡰࡴࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠢਸ"))
        url = bstack1l11l1lll1_opy_ + bstack11l1lll1l_opy_
        auth = (CONFIG[bstack111l1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨਹ")], CONFIG[bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ਺")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack11ll1l1l11_opy_ = json.loads(response.text)
            return bstack11ll1l1l11_opy_
    except ValueError as ve:
        logger.error(bstack111l1l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣ਻").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack111l1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࠿ࠦࡻࡾࠤ਼").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1l1ll1l1l_opy_(bstack1111l111l_opy_):
    global CONFIG
    if bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ਽") not in CONFIG or str(CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨਾ")]).lower() == bstack111l1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫਿ"):
        CONFIG[bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬੀ")] = False
    elif bstack111l1l_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬੁ") in bstack1111l111l_opy_:
        bstack111111llll_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬੂ"), {})
        logger.debug(bstack111l1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢ੃"), bstack111111llll_opy_)
        bstack11l111111l_opy_ = bstack1111l111l_opy_.get(bstack111l1l_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯ࡕࡩࡵ࡫ࡡࡵࡧࡵࡷࠧ੄"), [])
        bstack11l1l111ll_opy_ = bstack111l1l_opy_ (u"ࠦ࠱ࠨ੅").join(bstack11l111111l_opy_)
        logger.debug(bstack111l1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡻࡳࡵࡱࡰࠤࡷ࡫ࡰࡦࡣࡷࡩࡷࠦࡳࡵࡴ࡬ࡲ࡬ࡀࠠࠦࡵࠥ੆"), bstack11l1l111ll_opy_)
        bstack11lll11ll_opy_ = {
            bstack111l1l_opy_ (u"ࠨ࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣੇ"): bstack111l1l_opy_ (u"ࠢࡢࡶࡶ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷࠨੈ"),
            bstack111l1l_opy_ (u"ࠣࡨࡲࡶࡨ࡫ࡌࡰࡥࡤࡰࠧ੉"): bstack111l1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ੊"),
            bstack111l1l_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧੋ"): bstack11l1l111ll_opy_
        }
        bstack111111llll_opy_.update(bstack11lll11ll_opy_)
        logger.debug(bstack111l1l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼࡙ࠣࡵࡪࡡࡵࡧࡧࠤࡱࡵࡣࡢ࡮ࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠫࡳࠣੌ"), bstack111111llll_opy_)
        CONFIG[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴ੍ࠩ")] = bstack111111llll_opy_
        logger.debug(bstack111l1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡌࡩ࡯ࡣ࡯ࠤࡈࡕࡎࡇࡋࡊ࠾ࠥࠫࡳࠣ੎"), CONFIG)
def bstack1111l1lll1_opy_():
    bstack1l11l111l_opy_ = bstack111111lll1_opy_()
    if not bstack1l11l111l_opy_[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠧ੏")]:
      raise ValueError(bstack111l1l_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠡ࡫ࡶࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬ࡲࡰ࡯ࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴ࠰ࠥ੐"))
    return bstack1l11l111l_opy_[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠩੑ")] + bstack111l1l_opy_ (u"ࠪࡃࡨࡧࡰࡴ࠿ࠪ੒")
@measure(event_name=EVENTS.bstack11111llll_opy_, stage=STAGE.bstack1ll1ll111_opy_)
def bstack11111l1111_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack111l1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭੓")], CONFIG[bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ੔")])
        url = bstack11llll1l11_opy_
        logger.debug(bstack111l1l_opy_ (u"ࠨࡁࡵࡶࡨࡱࡵࡺࡩ࡯ࡩࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬ࡲࡰ࡯ࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡗࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࠦࡁࡑࡋࠥ੕"))
        try:
            response = requests.get(url, auth=auth, headers={bstack111l1l_opy_ (u"ࠢࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪࠨ੖"): bstack111l1l_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠦ੗")})
            if response.status_code == 200:
                bstack1ll11lll1l_opy_ = json.loads(response.text)
                bstack1lll11l111_opy_ = bstack1ll11lll1l_opy_.get(bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡴࠩ੘"), [])
                if bstack1lll11l111_opy_:
                    bstack1ll111ll1l_opy_ = bstack1lll11l111_opy_[0]
                    build_hashed_id = bstack1ll111ll1l_opy_.get(bstack111l1l_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ਖ਼"))
                    bstack11ll1llll_opy_ = bstack1lll11ll1l_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack11ll1llll_opy_])
                    logger.info(bstack1l111111l_opy_.format(bstack11ll1llll_opy_))
                    bstack111ll11l1_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧਗ਼")]
                    if bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧਜ਼") in CONFIG:
                      bstack111ll11l1_opy_ += bstack111l1l_opy_ (u"࠭ࠠࠨੜ") + CONFIG[bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ੝")]
                    if bstack111ll11l1_opy_ != bstack1ll111ll1l_opy_.get(bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ਫ਼")):
                      logger.debug(bstack11ll11l11l_opy_.format(bstack1ll111ll1l_opy_.get(bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ੟")), bstack111ll11l1_opy_))
                    return result
                else:
                    logger.debug(bstack111l1l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡑࡳࠥࡨࡵࡪ࡮ࡧࡷࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࡷ࡫ࡳࡱࡱࡱࡷࡪ࠴ࠢ੠"))
            else:
                logger.debug(bstack111l1l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨ੡"))
        except Exception as e:
            logger.error(bstack111l1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࡹࠠ࠻ࠢࡾࢁࠧ੢").format(str(e)))
    else:
        logger.debug(bstack111l1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡉࡏࡏࡈࡌࡋࠥ࡯ࡳࠡࡰࡲࡸࠥࡹࡥࡵ࠰࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡨࡵࡪ࡮ࡧࡷ࠳ࠨ੣"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack111l1111l1_opy_ import bstack111l1111l1_opy_, Events, bstack111l11l1l_opy_, bstack11l1l1l11l_opy_
from bstack_utils.measure import bstack1l11l1l11_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1l111l1ll_opy_ import bstack111l11llll_opy_
from bstack_utils.messages import *
from bstack_utils import bstack1l11l1lll_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack11lll111l_opy_, bstack11llll111_opy_, bstack1l1ll1ll1l_opy_, bstack1l11l1ll_opy_, \
  bstack11l1l111l_opy_, \
  Notset, bstack1ll1l111l1_opy_, \
  bstack1l1ll11l1_opy_, bstack11ll1lll11_opy_, bstack1l1llll111_opy_, bstack1l1l1llll1_opy_, bstack111ll1llll_opy_, bstack1ll11l11l1_opy_, \
  bstack111lllll1_opy_, \
  bstack1111lll11_opy_, bstack11l111ll1l_opy_, bstack1l1111l111_opy_, bstack1l1l111l11_opy_, \
  bstack111l11ll1_opy_, bstack1l1111l1l_opy_, bstack11l1llll1_opy_, bstack11111ll1l_opy_
from bstack_utils.bstack111l1ll11_opy_ import bstack1l1lll1ll_opy_
from bstack_utils.bstack1111llll1_opy_ import bstack1111ll1l11_opy_, bstack1lll1l1l11_opy_
from bstack_utils.bstack1l1l1ll1l_opy_ import bstack1ll1ll1l1l_opy_
from bstack_utils.bstack1lll111l11_opy_ import bstack11ll1111l1_opy_, bstack1lll11lll1_opy_
from bstack_utils.bstack111ll11l11_opy_ import bstack111ll11l11_opy_
from bstack_utils.bstack1l11ll1l11_opy_ import bstack1l1l1lllll_opy_
from bstack_utils.proxy import bstack1l11l1ll1_opy_, bstack1l1111l1l1_opy_, bstack111ll11ll_opy_, bstack111ll1lll1_opy_
from bstack_utils.bstack1l11111lll_opy_ import bstack1llll11l1l_opy_
import bstack_utils.bstack11ll11111_opy_ as bstack11lll111l1_opy_
import bstack_utils.bstack11l1lll111_opy_ as bstack11ll1ll1ll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack11l111111_opy_ import bstack111ll1111_opy_
from bstack_utils.bstack1lll1llll_opy_ import bstack1llll1lll_opy_
from bstack_utils.bstack1lll1l11l1_opy_ import bstack11lll1lll1_opy_
if os.getenv(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡌࡔࡕࡋࡔࠩ੤")):
  cli.bstack1ll1l1l111_opy_()
else:
  os.environ[bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡍࡕࡏࡌࡕࠪ੥")] = bstack111l1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ੦")
bstack1l11l11ll1_opy_ = bstack111l1l_opy_ (u"ࠪࠤࠥ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࠣࠤ࡮࡬ࠨࡱࡣࡪࡩࠥࡃ࠽࠾ࠢࡹࡳ࡮ࡪࠠ࠱ࠫࠣࡿࡡࡴࠠࠡࠢࡷࡶࡾࢁ࡜࡯ࠢࡦࡳࡳࡹࡴࠡࡨࡶࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨ࡝ࠩࡩࡷࡡ࠭ࠩ࠼࡞ࡱࠤࠥࠦࠠࠡࡨࡶ࠲ࡦࡶࡰࡦࡰࡧࡊ࡮ࡲࡥࡔࡻࡱࡧ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪ࠯ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡶ࡟ࡪࡰࡧࡩࡽ࠯ࠠࠬࠢࠥ࠾ࠧࠦࠫࠡࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࠨࡢࡹࡤ࡭ࡹࠦ࡮ࡦࡹࡓࡥ࡬࡫࠲࠯ࡧࡹࡥࡱࡻࡡࡵࡧࠫࠦ࠭࠯ࠠ࠾ࡀࠣࡿࢂࠨࠬࠡ࡞ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥ࡫ࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡄࡦࡶࡤ࡭ࡱࡹࠢࡾ࡞ࠪ࠭࠮࠯࡛ࠣࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠦࡢ࠯ࠠࠬࠢࠥ࠰ࡡࡢ࡮ࠣࠫ࡟ࡲࠥࠦࠠࠡࡿࡦࡥࡹࡩࡨࠩࡧࡻ࠭ࢀࡢ࡮ࠡࠢࠣࠤࢂࡢ࡮ࠡࠢࢀࡠࡳࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠪ੧")
bstack1l11ll1ll1_opy_ = bstack111l1l_opy_ (u"ࠫࡡࡴ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰࡞ࡱࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶ࡡࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠷࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡲࡢ࡭ࡳࡪࡥࡹࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠷ࡣ࡜࡯ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯ࡵ࡯࡭ࡨ࡫ࠨ࠱࠮ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸࠯࡜࡯ࡥࡲࡲࡸࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯ࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨࠩ࠼࡞ࡱ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡰࡦࡻ࡮ࡤࡪࠣࡁࠥࡧࡳࡺࡰࡦࠤ࠭ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷ࠮ࠦ࠽࠿ࠢࡾࡠࡳࡲࡥࡵࠢࡦࡥࡵࡹ࠻࡝ࡰࡷࡶࡾࠦࡻ࡝ࡰࡦࡥࡵࡹࠠ࠾ࠢࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶ࠭ࡡࡴࠠࠡࡿࠣࡧࡦࡺࡣࡩࠪࡨࡼ࠮ࠦࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡦࡽࡡࡪࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡧࡴࡴ࡮ࡦࡥࡷࠬࢀࡢ࡮ࠡࠢࠣࠤࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴ࠻ࠢࡣࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠩࢁࡥ࡯ࡥࡲࡨࡪ࡛ࡒࡊࡅࡲࡱࡵࡵ࡮ࡦࡰࡷࠬࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡩࡡࡱࡵࠬ࠭ࢂࡦࠬ࡝ࡰࠣࠤࠥࠦ࠮࠯࠰࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴ࡞ࡱࠤࠥࢃࠩ࡝ࡰࢀࡠࡳ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࠪ੨")
from ._version import __version__
bstack111111l111_opy_ = None
CONFIG = {}
bstack11ll11l1l_opy_ = {}
bstack11l1l1lll1_opy_ = {}
bstack11lll11l1l_opy_ = None
bstack1lll11l1ll_opy_ = None
bstack111l111l1l_opy_ = None
bstack11111lll11_opy_ = -1
bstack1ll11llll_opy_ = 0
bstack1ll1ll11l1_opy_ = bstack111l111ll1_opy_
bstack111llll111_opy_ = 1
bstack1llllll1l1_opy_ = False
bstack1111l1l11_opy_ = False
bstack1lll1ll11l_opy_ = bstack111l1l_opy_ (u"ࠬ࠭੩")
bstack1111l1111_opy_ = bstack111l1l_opy_ (u"࠭ࠧ੪")
bstack11ll1l11ll_opy_ = False
bstack1l111l111l_opy_ = True
bstack1ll1l11ll1_opy_ = bstack111l1l_opy_ (u"ࠧࠨ੫")
bstack11llllll1_opy_ = []
bstack1ll1l111l_opy_ = threading.Lock()
bstack111l1l1ll_opy_ = threading.Lock()
bstack1l111l11l1_opy_ = bstack111l1l_opy_ (u"ࠨࠩ੬")
bstack11l1l1l11_opy_ = False
bstack1l11ll111_opy_ = None
bstack1ll1l11l11_opy_ = None
bstack111lll1l1_opy_ = None
bstack1l1111ll1_opy_ = -1
bstack111ll111l_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠩࢁࠫ੭")), bstack111l1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ੮"), bstack111l1l_opy_ (u"ࠫ࠳ࡸ࡯ࡣࡱࡷ࠱ࡷ࡫ࡰࡰࡴࡷ࠱࡭࡫࡬ࡱࡧࡵ࠲࡯ࡹ࡯࡯ࠩ੯"))
bstack1lll11ll11_opy_ = 0
bstack11111l1l11_opy_ = 0
bstack1ll1111111_opy_ = []
bstack111111l11_opy_ = []
bstack111l111l1_opy_ = []
bstack1l1l11ll1_opy_ = []
bstack111l11l1l1_opy_ = bstack111l1l_opy_ (u"ࠬ࠭ੰ")
bstack111lll1l1l_opy_ = bstack111l1l_opy_ (u"࠭ࠧੱ")
bstack111ll1l1l_opy_ = False
bstack111ll1l111_opy_ = False
bstack11lll11l11_opy_ = {}
bstack1l111ll1l_opy_ = None
bstack11lllll1l1_opy_ = None
bstack1lllllll11_opy_ = None
bstack11l1111l1_opy_ = None
bstack11l1111111_opy_ = None
bstack111l1l111l_opy_ = None
bstack1ll11l1l1l_opy_ = None
bstack1ll1lllll1_opy_ = None
bstack1l11lll11l_opy_ = None
bstack1l1llllll_opy_ = None
bstack11ll11lll1_opy_ = None
bstack111l1ll1l1_opy_ = None
bstack111lll11l1_opy_ = None
bstack1ll1111lll_opy_ = None
bstack11llllll11_opy_ = None
bstack1l1llll11l_opy_ = None
bstack111l111l11_opy_ = None
bstack11ll1lll1l_opy_ = None
bstack1l11llllll_opy_ = None
bstack11lll1l1l1_opy_ = None
bstack1llll1ll11_opy_ = None
bstack11ll11l111_opy_ = None
bstack1lllll1l1l_opy_ = None
thread_local = threading.local()
bstack11l1ll1lll_opy_ = False
bstack11l1l111l1_opy_ = bstack111l1l_opy_ (u"ࠢࠣੲ")
logger = bstack1l11l1lll_opy_.get_logger(__name__, bstack1ll1ll11l1_opy_)
bstack1lllll1l1_opy_ = Config.bstack1111ll1l_opy_()
percy = bstack1ll1111ll_opy_()
bstack1llll11ll1_opy_ = bstack111l11llll_opy_()
bstack1llll111l1_opy_ = bstack11l1l1ll_opy_()
def bstack111111lll_opy_():
  global CONFIG
  global bstack111ll1l1l_opy_
  global bstack1lllll1l1_opy_
  testContextOptions = bstack111ll1ll1l_opy_(CONFIG)
  if bstack11l1l111l_opy_(CONFIG):
    if (bstack111l1l_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪੳ") in testContextOptions and str(testContextOptions[bstack111l1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫੴ")]).lower() == bstack111l1l_opy_ (u"ࠪࡸࡷࡻࡥࠨੵ")):
      bstack111ll1l1l_opy_ = True
    bstack1lllll1l1_opy_.bstack111lll1l11_opy_(testContextOptions.get(bstack111l1l_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ੶"), False))
  else:
    bstack111ll1l1l_opy_ = True
    bstack1lllll1l1_opy_.bstack111lll1l11_opy_(True)
def bstack11l1ll1l1l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1l11ll1lll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1l1lll11l_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack111l1l_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡩ࡯࡯ࡨ࡬࡫࡫࡯࡬ࡦࠤ੷") == args[i].lower() or bstack111l1l_opy_ (u"ࠨ࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡱࡪ࡮࡭ࠢ੸") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1ll1l11ll1_opy_
      bstack1ll1l11ll1_opy_ += bstack111l1l_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡄࡱࡱࡪ࡮࡭ࡆࡪ࡮ࡨࠤࠬ੹") + shlex.quote(path)
      return path
  return None
bstack1l1lll1l1_opy_ = re.compile(bstack111l1l_opy_ (u"ࡳࠤ࠱࠮ࡄࡢࠤࡼࠪ࠱࠮ࡄ࠯ࡽ࠯ࠬࡂࠦ੺"))
def bstack1lll1l111l_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l1lll1l1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack111l1l_opy_ (u"ࠤࠧࡿࠧ੻") + group + bstack111l1l_opy_ (u"ࠥࢁࠧ੼"), os.environ.get(group))
  return value
def bstack1ll1l1l1l1_opy_():
  global bstack1lllll1l1l_opy_
  if bstack1lllll1l1l_opy_ is None:
        bstack1lllll1l1l_opy_ = bstack1l1lll11l_opy_()
  bstack11l111llll_opy_ = bstack1lllll1l1l_opy_
  if bstack11l111llll_opy_ and os.path.exists(os.path.abspath(bstack11l111llll_opy_)):
    fileName = bstack11l111llll_opy_
  if bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ੽") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆࠩ੾")])) and not bstack111l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨ੿") in locals():
    fileName = os.environ[bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ઀")]
  if bstack111l1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡔࡡ࡮ࡧࠪઁ") in locals():
    bstack1ll_opy_ = os.path.abspath(fileName)
  else:
    bstack1ll_opy_ = bstack111l1l_opy_ (u"ࠩࠪં")
  bstack1l11111ll_opy_ = os.getcwd()
  bstack1lll11l1l1_opy_ = bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ઃ")
  bstack1l1l1l11l1_opy_ = bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡦࡳ࡬ࠨ઄")
  while (not os.path.exists(bstack1ll_opy_)) and bstack1l11111ll_opy_ != bstack111l1l_opy_ (u"ࠧࠨઅ"):
    bstack1ll_opy_ = os.path.join(bstack1l11111ll_opy_, bstack1lll11l1l1_opy_)
    if not os.path.exists(bstack1ll_opy_):
      bstack1ll_opy_ = os.path.join(bstack1l11111ll_opy_, bstack1l1l1l11l1_opy_)
    if bstack1l11111ll_opy_ != os.path.dirname(bstack1l11111ll_opy_):
      bstack1l11111ll_opy_ = os.path.dirname(bstack1l11111ll_opy_)
    else:
      bstack1l11111ll_opy_ = bstack111l1l_opy_ (u"ࠨࠢઆ")
  bstack1lllll1l1l_opy_ = bstack1ll_opy_ if os.path.exists(bstack1ll_opy_) else None
  return bstack1lllll1l1l_opy_
def bstack1ll11ll111_opy_(config):
    if bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧઇ") in config:
      config[bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬઈ")] = config[bstack111l1l_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࠩઉ")]
    if bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࡒࡴࡹ࡯࡯࡯ࡵࠪઊ") in config:
      config[bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨઋ")] = config[bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࡔࡶࡴࡪࡱࡱࡷࠬઌ")]
def bstack1l11111111_opy_():
  bstack1ll_opy_ = bstack1ll1l1l1l1_opy_()
  if not os.path.exists(bstack1ll_opy_):
    bstack11l111l1l1_opy_(
      bstack11lll11ll1_opy_.format(os.getcwd()))
  try:
    with open(bstack1ll_opy_, bstack111l1l_opy_ (u"࠭ࡲࠨઍ")) as stream:
      yaml.add_implicit_resolver(bstack111l1l_opy_ (u"ࠢࠢࡲࡤࡸ࡭࡫ࡸࠣ઎"), bstack1l1lll1l1_opy_)
      yaml.add_constructor(bstack111l1l_opy_ (u"ࠣࠣࡳࡥࡹ࡮ࡥࡹࠤએ"), bstack1lll1l111l_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1ll11ll111_opy_(config)
      return config
  except:
    with open(bstack1ll_opy_, bstack111l1l_opy_ (u"ࠩࡵࠫઐ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1ll11ll111_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack11l111l1l1_opy_(bstack1l11l11ll_opy_.format(str(exc)))
def bstack1l1lll111_opy_(config):
  bstack1111ll11l_opy_ = bstack1111l11l1l_opy_(config)
  for option in list(bstack1111ll11l_opy_):
    if option.lower() in bstack111l1l1ll1_opy_ and option != bstack111l1l1ll1_opy_[option.lower()]:
      bstack1111ll11l_opy_[bstack111l1l1ll1_opy_[option.lower()]] = bstack1111ll11l_opy_[option]
      del bstack1111ll11l_opy_[option]
  return config
def bstack111l1lll1l_opy_():
  global bstack11l1l1lll1_opy_
  for key, bstack1ll11ll11_opy_ in bstack1l11111l1_opy_.items():
    if isinstance(bstack1ll11ll11_opy_, list):
      for var in bstack1ll11ll11_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack11l1l1lll1_opy_[key] = os.environ[var]
          break
    elif bstack1ll11ll11_opy_ in os.environ and os.environ[bstack1ll11ll11_opy_] and str(os.environ[bstack1ll11ll11_opy_]).strip():
      bstack11l1l1lll1_opy_[key] = os.environ[bstack1ll11ll11_opy_]
  if bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬઑ") in os.environ:
    bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ઒")] = {}
    bstack11l1l1lll1_opy_[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩઓ")][bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨઔ")] = os.environ[bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩક")]
def bstack1ll111lll1_opy_():
  global bstack11ll11l1l_opy_
  global bstack1ll1l11ll1_opy_
  bstack1l11ll11l1_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack111l1l_opy_ (u"ࠨ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫખ").lower() == val.lower():
      bstack11ll11l1l_opy_[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ગ")] = {}
      bstack11ll11l1l_opy_[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઘ")][bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ઙ")] = sys.argv[idx + 1]
      bstack1l11ll11l1_opy_.extend([idx, idx + 1])
      break
  for key, bstack1ll1111ll1_opy_ in bstack1l1lll1l11_opy_.items():
    if isinstance(bstack1ll1111ll1_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack1ll1111ll1_opy_:
          if bstack111l1l_opy_ (u"ࠬ࠳࠭ࠨચ") + var.lower() == val.lower() and key not in bstack11ll11l1l_opy_:
            bstack11ll11l1l_opy_[key] = sys.argv[idx + 1]
            bstack1ll1l11ll1_opy_ += bstack111l1l_opy_ (u"࠭ࠠ࠮࠯ࠪછ") + var + bstack111l1l_opy_ (u"ࠧࠡࠩજ") + shlex.quote(sys.argv[idx + 1])
            bstack1l11ll11l1_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack111l1l_opy_ (u"ࠨ࠯࠰ࠫઝ") + bstack1ll1111ll1_opy_.lower() == val.lower() and key not in bstack11ll11l1l_opy_:
          bstack11ll11l1l_opy_[key] = sys.argv[idx + 1]
          bstack1ll1l11ll1_opy_ += bstack111l1l_opy_ (u"ࠩࠣ࠱࠲࠭ઞ") + bstack1ll1111ll1_opy_ + bstack111l1l_opy_ (u"ࠪࠤࠬટ") + shlex.quote(sys.argv[idx + 1])
          bstack1l11ll11l1_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack1l11ll11l1_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack1l111ll111_opy_(config):
  bstack1l11111ll1_opy_ = config.keys()
  for bstack1ll111l1ll_opy_, bstack1lll1111l1_opy_ in bstack1llll1llll_opy_.items():
    if bstack1lll1111l1_opy_ in bstack1l11111ll1_opy_:
      config[bstack1ll111l1ll_opy_] = config[bstack1lll1111l1_opy_]
      del config[bstack1lll1111l1_opy_]
  for bstack1ll111l1ll_opy_, bstack1lll1111l1_opy_ in bstack11lllll11l_opy_.items():
    if isinstance(bstack1lll1111l1_opy_, list):
      for bstack1ll1l1111_opy_ in bstack1lll1111l1_opy_:
        if bstack1ll1l1111_opy_ in bstack1l11111ll1_opy_:
          config[bstack1ll111l1ll_opy_] = config[bstack1ll1l1111_opy_]
          del config[bstack1ll1l1111_opy_]
          break
    elif bstack1lll1111l1_opy_ in bstack1l11111ll1_opy_:
      config[bstack1ll111l1ll_opy_] = config[bstack1lll1111l1_opy_]
      del config[bstack1lll1111l1_opy_]
  for bstack1ll1l1111_opy_ in list(config):
    for bstack11l11l111_opy_ in bstack1lll111lll_opy_:
      if bstack1ll1l1111_opy_.lower() == bstack11l11l111_opy_.lower() and bstack1ll1l1111_opy_ != bstack11l11l111_opy_:
        config[bstack11l11l111_opy_] = config[bstack1ll1l1111_opy_]
        del config[bstack1ll1l1111_opy_]
  bstack1ll1ll111l_opy_ = [{}]
  if not config.get(bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧઠ")):
    config[bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨડ")] = [{}]
  bstack1ll1ll111l_opy_ = config[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩઢ")]
  for platform in bstack1ll1ll111l_opy_:
    for bstack1ll1l1111_opy_ in list(platform):
      for bstack11l11l111_opy_ in bstack1lll111lll_opy_:
        if bstack1ll1l1111_opy_.lower() == bstack11l11l111_opy_.lower() and bstack1ll1l1111_opy_ != bstack11l11l111_opy_:
          platform[bstack11l11l111_opy_] = platform[bstack1ll1l1111_opy_]
          del platform[bstack1ll1l1111_opy_]
  for bstack1ll111l1ll_opy_, bstack1lll1111l1_opy_ in bstack11lllll11l_opy_.items():
    for platform in bstack1ll1ll111l_opy_:
      if isinstance(bstack1lll1111l1_opy_, list):
        for bstack1ll1l1111_opy_ in bstack1lll1111l1_opy_:
          if bstack1ll1l1111_opy_ in platform:
            platform[bstack1ll111l1ll_opy_] = platform[bstack1ll1l1111_opy_]
            del platform[bstack1ll1l1111_opy_]
            break
      elif bstack1lll1111l1_opy_ in platform:
        platform[bstack1ll111l1ll_opy_] = platform[bstack1lll1111l1_opy_]
        del platform[bstack1lll1111l1_opy_]
  for bstack111l1ll11l_opy_ in bstack111l1l1l11_opy_:
    if bstack111l1ll11l_opy_ in config:
      if not bstack111l1l1l11_opy_[bstack111l1ll11l_opy_] in config:
        config[bstack111l1l1l11_opy_[bstack111l1ll11l_opy_]] = {}
      config[bstack111l1l1l11_opy_[bstack111l1ll11l_opy_]].update(config[bstack111l1ll11l_opy_])
      del config[bstack111l1ll11l_opy_]
  for platform in bstack1ll1ll111l_opy_:
    for bstack111l1ll11l_opy_ in bstack111l1l1l11_opy_:
      if bstack111l1ll11l_opy_ in list(platform):
        if not bstack111l1l1l11_opy_[bstack111l1ll11l_opy_] in platform:
          platform[bstack111l1l1l11_opy_[bstack111l1ll11l_opy_]] = {}
        platform[bstack111l1l1l11_opy_[bstack111l1ll11l_opy_]].update(platform[bstack111l1ll11l_opy_])
        del platform[bstack111l1ll11l_opy_]
  config = bstack1l1lll111_opy_(config)
  return config
def bstack11l11l11ll_opy_(config):
  global bstack1111l1111_opy_
  bstack1l111lll1_opy_ = False
  if bstack111l1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫણ") in config and str(config[bstack111l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬત")]).lower() != bstack111l1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨથ"):
    if bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧદ") not in config or str(config[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨધ")]).lower() == bstack111l1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫન"):
      config[bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬ઩")] = False
    else:
      bstack1l11l111l_opy_ = bstack111111lll1_opy_()
      if bstack111l1l_opy_ (u"ࠧࡪࡵࡗࡶ࡮ࡧ࡬ࡈࡴ࡬ࡨࠬપ") in bstack1l11l111l_opy_:
        if not bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬફ") in config:
          config[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭બ")] = {}
        config[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧભ")][bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭મ")] = bstack111l1l_opy_ (u"ࠬࡧࡴࡴ࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠫય")
        bstack1l111lll1_opy_ = True
        bstack1111l1111_opy_ = config[bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪર")].get(bstack111l1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઱"))
  if bstack11l1l111l_opy_(config) and bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬલ") in config and str(config[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ળ")]).lower() != bstack111l1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ઴") and not bstack1l111lll1_opy_:
    if not bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨવ") in config:
      config[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩશ")] = {}
    if not config[bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪષ")].get(bstack111l1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠫસ")) and not bstack111l1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪહ") in config[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭઺")]:
      bstack1lllll11_opy_ = datetime.datetime.now()
      bstack1l111l1lll_opy_ = bstack1lllll11_opy_.strftime(bstack111l1l_opy_ (u"ࠪࠩࡩࡥࠥࡣࡡࠨࡌࠪࡓࠧ઻"))
      hostname = socket.gethostname()
      bstack1l111111l1_opy_ = bstack111l1l_opy_ (u"઼ࠫࠬ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack111l1l_opy_ (u"ࠬࢁࡽࡠࡽࢀࡣࢀࢃࠧઽ").format(bstack1l111l1lll_opy_, hostname, bstack1l111111l1_opy_)
      config[bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪા")][bstack111l1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩિ")] = identifier
    bstack1111l1111_opy_ = config[bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬી")].get(bstack111l1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫુ"))
  return config
def bstack11111lll1l_opy_():
  bstack1ll1l1111l_opy_ =  bstack1l1l1llll1_opy_()[bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠩૂ")]
  return bstack1ll1l1111l_opy_ if bstack1ll1l1111l_opy_ else -1
def bstack111l1111l_opy_(bstack1ll1l1111l_opy_):
  global CONFIG
  if not bstack111l1l_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ૃ") in CONFIG[bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૄ")]:
    return
  CONFIG[bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨૅ")] = CONFIG[bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૆")].replace(
    bstack111l1l_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪે"),
    str(bstack1ll1l1111l_opy_)
  )
def bstack11lll111ll_opy_():
  global CONFIG
  if not bstack111l1l_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨૈ") in CONFIG[bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૉ")]:
    return
  bstack1lllll11_opy_ = datetime.datetime.now()
  bstack1l111l1lll_opy_ = bstack1lllll11_opy_.strftime(bstack111l1l_opy_ (u"ࠫࠪࡪ࠭ࠦࡤ࠰ࠩࡍࡀࠥࡎࠩ૊"))
  CONFIG[bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧો")] = CONFIG[bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨૌ")].replace(
    bstack111l1l_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ્࠭"),
    bstack1l111l1lll_opy_
  )
def bstack1111l111ll_opy_():
  global CONFIG
  if bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૎") in CONFIG and not bool(CONFIG[bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૏")]):
    del CONFIG[bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૐ")]
    return
  if not bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૑") in CONFIG:
    CONFIG[bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૒")] = bstack111l1l_opy_ (u"࠭ࠣࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩ૓")
  if bstack111l1l_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭૔") in CONFIG[bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૕")]:
    bstack11lll111ll_opy_()
    os.environ[bstack111l1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭૖")] = CONFIG[bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૗")]
  if not bstack111l1l_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭૘") in CONFIG[bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૙")]:
    return
  bstack1ll1l1111l_opy_ = bstack111l1l_opy_ (u"࠭ࠧ૚")
  bstack11111111l_opy_ = bstack11111lll1l_opy_()
  if bstack11111111l_opy_ != -1:
    bstack1ll1l1111l_opy_ = bstack111l1l_opy_ (u"ࠧࡄࡋࠣࠫ૛") + str(bstack11111111l_opy_)
  if bstack1ll1l1111l_opy_ == bstack111l1l_opy_ (u"ࠨࠩ૜"):
    bstack11ll1ll11l_opy_ = bstack111lll1ll1_opy_(CONFIG[bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ૝")])
    if bstack11ll1ll11l_opy_ != -1:
      bstack1ll1l1111l_opy_ = str(bstack11ll1ll11l_opy_)
  if bstack1ll1l1111l_opy_:
    bstack111l1111l_opy_(bstack1ll1l1111l_opy_)
    os.environ[bstack111l1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧ૞")] = CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૟")]
def bstack1l1111ll1l_opy_(bstack11l11l1l1_opy_, bstack1111ll1l1l_opy_, path):
  json_data = {
    bstack111l1l_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩૠ"): bstack1111ll1l1l_opy_
  }
  if os.path.exists(path):
    bstack11l1l1ll1l_opy_ = json.load(open(path, bstack111l1l_opy_ (u"࠭ࡲࡣࠩૡ")))
  else:
    bstack11l1l1ll1l_opy_ = {}
  bstack11l1l1ll1l_opy_[bstack11l11l1l1_opy_] = json_data
  with open(path, bstack111l1l_opy_ (u"ࠢࡸ࠭ࠥૢ")) as outfile:
    json.dump(bstack11l1l1ll1l_opy_, outfile)
def bstack111lll1ll1_opy_(bstack11l11l1l1_opy_):
  bstack11l11l1l1_opy_ = str(bstack11l11l1l1_opy_)
  bstack1lll111ll1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠨࢀࠪૣ")), bstack111l1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ૤"))
  try:
    if not os.path.exists(bstack1lll111ll1_opy_):
      os.makedirs(bstack1lll111ll1_opy_)
    file_path = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠪࢂࠬ૥")), bstack111l1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ૦"), bstack111l1l_opy_ (u"ࠬ࠴ࡢࡶ࡫࡯ࡨ࠲ࡴࡡ࡮ࡧ࠰ࡧࡦࡩࡨࡦ࠰࡭ࡷࡴࡴࠧ૧"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack111l1l_opy_ (u"࠭ࡷࠨ૨")):
        pass
      with open(file_path, bstack111l1l_opy_ (u"ࠢࡸ࠭ࠥ૩")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack111l1l_opy_ (u"ࠨࡴࠪ૪")) as bstack1l111111ll_opy_:
      bstack11ll111111_opy_ = json.load(bstack1l111111ll_opy_)
    if bstack11l11l1l1_opy_ in bstack11ll111111_opy_:
      bstack11llllllll_opy_ = bstack11ll111111_opy_[bstack11l11l1l1_opy_][bstack111l1l_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૫")]
      bstack1ll11l111l_opy_ = int(bstack11llllllll_opy_) + 1
      bstack1l1111ll1l_opy_(bstack11l11l1l1_opy_, bstack1ll11l111l_opy_, file_path)
      return bstack1ll11l111l_opy_
    else:
      bstack1l1111ll1l_opy_(bstack11l11l1l1_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1l1l1l11ll_opy_.format(str(e)))
    return -1
def bstack11llll11ll_opy_(config):
  if not config[bstack111l1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ૬")] or not config[bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ૭")]:
    return True
  else:
    return False
def bstack1lllllll1l_opy_(config, index=0):
  global bstack11ll1l11ll_opy_
  bstack111lll11l_opy_ = {}
  caps = bstack1111llllll_opy_ + bstack11l111l111_opy_
  if config.get(bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ૮"), False):
    bstack111lll11l_opy_[bstack111l1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪ૯")] = True
    bstack111lll11l_opy_[bstack111l1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ૰")] = config.get(bstack111l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷࠬ૱"), {})
  if bstack11ll1l11ll_opy_:
    caps += bstack11lll1l11_opy_
  for key in config:
    if key in caps + [bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૲")]:
      continue
    bstack111lll11l_opy_[key] = config[key]
  if bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૳") in config:
    for bstack1l11ll1ll_opy_ in config[bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૴")][index]:
      if bstack1l11ll1ll_opy_ in caps:
        continue
      bstack111lll11l_opy_[bstack1l11ll1ll_opy_] = config[bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૵")][index][bstack1l11ll1ll_opy_]
  bstack111lll11l_opy_[bstack111l1l_opy_ (u"࠭ࡨࡰࡵࡷࡒࡦࡳࡥࠨ૶")] = socket.gethostname()
  if bstack111l1l_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ૷") in bstack111lll11l_opy_:
    del (bstack111lll11l_opy_[bstack111l1l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ૸")])
  return bstack111lll11l_opy_
def bstack11l111l11_opy_(config):
  global bstack11ll1l11ll_opy_
  bstack11ll1lllll_opy_ = {}
  caps = bstack11l111l111_opy_
  if bstack11ll1l11ll_opy_:
    caps += bstack11lll1l11_opy_
  for key in caps:
    if key in config:
      bstack11ll1lllll_opy_[key] = config[key]
  return bstack11ll1lllll_opy_
def bstack1ll11lll11_opy_(bstack111lll11l_opy_, bstack11ll1lllll_opy_):
  bstack1l1l11ll1l_opy_ = {}
  for key in bstack111lll11l_opy_.keys():
    if key in bstack1llll1llll_opy_:
      bstack1l1l11ll1l_opy_[bstack1llll1llll_opy_[key]] = bstack111lll11l_opy_[key]
    else:
      bstack1l1l11ll1l_opy_[key] = bstack111lll11l_opy_[key]
  for key in bstack11ll1lllll_opy_:
    if key in bstack1llll1llll_opy_:
      bstack1l1l11ll1l_opy_[bstack1llll1llll_opy_[key]] = bstack11ll1lllll_opy_[key]
    else:
      bstack1l1l11ll1l_opy_[key] = bstack11ll1lllll_opy_[key]
  return bstack1l1l11ll1l_opy_
def bstack1l11ll1l1l_opy_(config, index=0):
  global bstack11ll1l11ll_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1ll1111l1_opy_ = bstack11lll111l_opy_(bstack111l11l111_opy_, config, logger)
  bstack11ll1lllll_opy_ = bstack11l111l11_opy_(config)
  bstack1l1ll111l_opy_ = bstack11l111l111_opy_
  bstack1l1ll111l_opy_ += bstack11l11111l1_opy_
  bstack11ll1lllll_opy_ = update(bstack11ll1lllll_opy_, bstack1ll1111l1_opy_)
  if bstack11ll1l11ll_opy_:
    bstack1l1ll111l_opy_ += bstack11lll1l11_opy_
  if bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬૹ") in config:
    if bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨૺ") in config[bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧૻ")][index]:
      caps[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪૼ")] = config[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૽")][index][bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ૾")]
    if bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ૿") in config[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ଀")][index]:
      caps[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫଁ")] = str(config[bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଂ")][index][bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଃ")])
    bstack1111ll1lll_opy_ = bstack11lll111l_opy_(bstack111l11l111_opy_, config[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ଄")][index], logger)
    bstack1l1ll111l_opy_ += list(bstack1111ll1lll_opy_.keys())
    for bstack111lllll11_opy_ in bstack1l1ll111l_opy_:
      if bstack111lllll11_opy_ in config[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଅ")][index]:
        if bstack111lllll11_opy_ == bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪଆ"):
          try:
            bstack1111ll1lll_opy_[bstack111lllll11_opy_] = str(config[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଇ")][index][bstack111lllll11_opy_] * 1.0)
          except:
            bstack1111ll1lll_opy_[bstack111lllll11_opy_] = str(config[bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଈ")][index][bstack111lllll11_opy_])
        else:
          bstack1111ll1lll_opy_[bstack111lllll11_opy_] = config[bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଉ")][index][bstack111lllll11_opy_]
        del (config[bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଊ")][index][bstack111lllll11_opy_])
    bstack11ll1lllll_opy_ = update(bstack11ll1lllll_opy_, bstack1111ll1lll_opy_)
  bstack111lll11l_opy_ = bstack1lllllll1l_opy_(config, index)
  for bstack1ll1l1111_opy_ in bstack11l111l111_opy_ + list(bstack1ll1111l1_opy_.keys()):
    if bstack1ll1l1111_opy_ in bstack111lll11l_opy_:
      bstack11ll1lllll_opy_[bstack1ll1l1111_opy_] = bstack111lll11l_opy_[bstack1ll1l1111_opy_]
      del (bstack111lll11l_opy_[bstack1ll1l1111_opy_])
  if bstack1ll1l111l1_opy_(config):
    bstack111lll11l_opy_[bstack111l1l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ଋ")] = True
    caps.update(bstack11ll1lllll_opy_)
    caps[bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨଌ")] = bstack111lll11l_opy_
  else:
    bstack111lll11l_opy_[bstack111l1l_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨ଍")] = False
    caps.update(bstack1ll11lll11_opy_(bstack111lll11l_opy_, bstack11ll1lllll_opy_))
    if bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ଎") in caps:
      caps[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫଏ")] = caps[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଐ")]
      del (caps[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ଑")])
    if bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ଒") in caps:
      caps[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩଓ")] = caps[bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଔ")]
      del (caps[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪକ")])
  return caps
def bstack1lll11llll_opy_():
  global bstack1l111l11l1_opy_
  global CONFIG
  if bstack1l11ll1lll_opy_() <= version.parse(bstack111l1l_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪଖ")):
    if bstack1l111l11l1_opy_ != bstack111l1l_opy_ (u"ࠫࠬଗ"):
      return bstack111l1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨଘ") + bstack1l111l11l1_opy_ + bstack111l1l_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥଙ")
    return bstack11111lllll_opy_
  if bstack1l111l11l1_opy_ != bstack111l1l_opy_ (u"ࠧࠨଚ"):
    return bstack111l1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥଛ") + bstack1l111l11l1_opy_ + bstack111l1l_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥଜ")
  return bstack1l1ll1l1ll_opy_
def bstack11l1lll11l_opy_(options):
  return hasattr(options, bstack111l1l_opy_ (u"ࠪࡷࡪࡺ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶࡼࠫଝ"))
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
def bstack1ll1ll11l_opy_(options, bstack1l1lll1lll_opy_):
  for bstack1lllllllll_opy_ in bstack1l1lll1lll_opy_:
    if bstack1lllllllll_opy_ in [bstack111l1l_opy_ (u"ࠫࡦࡸࡧࡴࠩଞ"), bstack111l1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩଟ")]:
      continue
    if bstack1lllllllll_opy_ in options._experimental_options:
      options._experimental_options[bstack1lllllllll_opy_] = update(options._experimental_options[bstack1lllllllll_opy_],
                                                         bstack1l1lll1lll_opy_[bstack1lllllllll_opy_])
    else:
      options.add_experimental_option(bstack1lllllllll_opy_, bstack1l1lll1lll_opy_[bstack1lllllllll_opy_])
  if bstack111l1l_opy_ (u"࠭ࡡࡳࡩࡶࠫଠ") in bstack1l1lll1lll_opy_:
    for arg in bstack1l1lll1lll_opy_[bstack111l1l_opy_ (u"ࠧࡢࡴࡪࡷࠬଡ")]:
      options.add_argument(arg)
    del (bstack1l1lll1lll_opy_[bstack111l1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଢ")])
  if bstack111l1l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ଣ") in bstack1l1lll1lll_opy_:
    for ext in bstack1l1lll1lll_opy_[bstack111l1l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧତ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l1lll1lll_opy_[bstack111l1l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨଥ")])
def bstack1111l11l1_opy_(options, bstack11ll11l11_opy_):
  if bstack111l1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫଦ") in bstack11ll11l11_opy_:
    for bstack1l111l1111_opy_ in bstack11ll11l11_opy_[bstack111l1l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬଧ")]:
      if bstack1l111l1111_opy_ in options._preferences:
        options._preferences[bstack1l111l1111_opy_] = update(options._preferences[bstack1l111l1111_opy_], bstack11ll11l11_opy_[bstack111l1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ନ")][bstack1l111l1111_opy_])
      else:
        options.set_preference(bstack1l111l1111_opy_, bstack11ll11l11_opy_[bstack111l1l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ଩")][bstack1l111l1111_opy_])
  if bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧପ") in bstack11ll11l11_opy_:
    for arg in bstack11ll11l11_opy_[bstack111l1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଫ")]:
      options.add_argument(arg)
def bstack1l1l11l11l_opy_(options, bstack1ll1ll1l1_opy_):
  if bstack111l1l_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬବ") in bstack1ll1ll1l1_opy_:
    options.use_webview(bool(bstack1ll1ll1l1_opy_[bstack111l1l_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭ଭ")]))
  bstack1ll1ll11l_opy_(options, bstack1ll1ll1l1_opy_)
def bstack1llll1ll1l_opy_(options, bstack1lllll1l11_opy_):
  for bstack111llll1l_opy_ in bstack1lllll1l11_opy_:
    if bstack111llll1l_opy_ in [bstack111l1l_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪମ"), bstack111l1l_opy_ (u"ࠧࡢࡴࡪࡷࠬଯ")]:
      continue
    options.set_capability(bstack111llll1l_opy_, bstack1lllll1l11_opy_[bstack111llll1l_opy_])
  if bstack111l1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ର") in bstack1lllll1l11_opy_:
    for arg in bstack1lllll1l11_opy_[bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ଱")]:
      options.add_argument(arg)
  if bstack111l1l_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧଲ") in bstack1lllll1l11_opy_:
    options.bstack1l1ll11ll_opy_(bool(bstack1lllll1l11_opy_[bstack111l1l_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨଳ")]))
def bstack11l1ll11l1_opy_(options, bstack1111ll11l1_opy_):
  for bstack1l1l11l11_opy_ in bstack1111ll11l1_opy_:
    if bstack1l1l11l11_opy_ in [bstack111l1l_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ଴"), bstack111l1l_opy_ (u"࠭ࡡࡳࡩࡶࠫଵ")]:
      continue
    options._options[bstack1l1l11l11_opy_] = bstack1111ll11l1_opy_[bstack1l1l11l11_opy_]
  if bstack111l1l_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଶ") in bstack1111ll11l1_opy_:
    for bstack1111lll1ll_opy_ in bstack1111ll11l1_opy_[bstack111l1l_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬଷ")]:
      options.bstack1111l1l1l_opy_(
        bstack1111lll1ll_opy_, bstack1111ll11l1_opy_[bstack111l1l_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ସ")][bstack1111lll1ll_opy_])
  if bstack111l1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨହ") in bstack1111ll11l1_opy_:
    for arg in bstack1111ll11l1_opy_[bstack111l1l_opy_ (u"ࠫࡦࡸࡧࡴࠩ଺")]:
      options.add_argument(arg)
def bstack111111l1ll_opy_(options, caps):
  if not hasattr(options, bstack111l1l_opy_ (u"ࠬࡑࡅ࡚ࠩ଻")):
    return
  if options.KEY == bstack111l1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶ଼ࠫ"):
    options = bstack1lll11ll1_opy_.bstack11ll1llll1_opy_(bstack1ll111ll11_opy_=options, config=CONFIG)
  if options.KEY == bstack111l1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬଽ") and options.KEY in caps:
    bstack1ll1ll11l_opy_(options, caps[bstack111l1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ା")])
  elif options.KEY == bstack111l1l_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧି") and options.KEY in caps:
    bstack1111l11l1_opy_(options, caps[bstack111l1l_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨୀ")])
  elif options.KEY == bstack111l1l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬୁ") and options.KEY in caps:
    bstack1llll1ll1l_opy_(options, caps[bstack111l1l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ୂ")])
  elif options.KEY == bstack111l1l_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧୃ") and options.KEY in caps:
    bstack1l1l11l11l_opy_(options, caps[bstack111l1l_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨୄ")])
  elif options.KEY == bstack111l1l_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ୅") and options.KEY in caps:
    bstack11l1ll11l1_opy_(options, caps[bstack111l1l_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ୆")])
def bstack1l1l1lll11_opy_(caps):
  global bstack11ll1l11ll_opy_
  if isinstance(os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫେ")), str):
    bstack11ll1l11ll_opy_ = eval(os.getenv(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬୈ")))
  if bstack11ll1l11ll_opy_:
    if bstack11l1ll1l1l_opy_() < version.parse(bstack111l1l_opy_ (u"ࠬ࠸࠮࠴࠰࠳ࠫ୉")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack111l1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭୊")
    if bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬୋ") in caps:
      browser = caps[bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ୌ")]
    elif bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ୍ࠪ") in caps:
      browser = caps[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫ୎")]
    browser = str(browser).lower()
    if browser == bstack111l1l_opy_ (u"ࠫ࡮ࡶࡨࡰࡰࡨࠫ୏") or browser == bstack111l1l_opy_ (u"ࠬ࡯ࡰࡢࡦࠪ୐"):
      browser = bstack111l1l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭୑")
    if browser == bstack111l1l_opy_ (u"ࠧࡴࡣࡰࡷࡺࡴࡧࠨ୒"):
      browser = bstack111l1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ୓")
    if browser not in [bstack111l1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩ୔"), bstack111l1l_opy_ (u"ࠪࡩࡩ࡭ࡥࠨ୕"), bstack111l1l_opy_ (u"ࠫ࡮࡫ࠧୖ"), bstack111l1l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬୗ"), bstack111l1l_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾࠧ୘")]:
      return None
    try:
      package = bstack111l1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮࠰ࡺࡩࡧࡪࡲࡪࡸࡨࡶ࠳ࢁࡽ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ୙").format(browser)
      name = bstack111l1l_opy_ (u"ࠨࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୚")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11l1lll11l_opy_(options):
        return None
      for bstack1ll1l1111_opy_ in caps.keys():
        options.set_capability(bstack1ll1l1111_opy_, caps[bstack1ll1l1111_opy_])
      bstack111111l1ll_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1ll1l11l1l_opy_(options, bstack1111ll1111_opy_):
  if not bstack11l1lll11l_opy_(options):
    return
  for bstack1ll1l1111_opy_ in bstack1111ll1111_opy_.keys():
    if bstack1ll1l1111_opy_ in bstack11l11111l1_opy_:
      continue
    if bstack1ll1l1111_opy_ in options._caps and type(options._caps[bstack1ll1l1111_opy_]) in [dict, list]:
      options._caps[bstack1ll1l1111_opy_] = update(options._caps[bstack1ll1l1111_opy_], bstack1111ll1111_opy_[bstack1ll1l1111_opy_])
    else:
      options.set_capability(bstack1ll1l1111_opy_, bstack1111ll1111_opy_[bstack1ll1l1111_opy_])
  bstack111111l1ll_opy_(options, bstack1111ll1111_opy_)
  if bstack111l1l_opy_ (u"ࠩࡰࡳࡿࡀࡤࡦࡤࡸ࡫࡬࡫ࡲࡂࡦࡧࡶࡪࡹࡳࠨ୛") in options._caps:
    if options._caps[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଡ଼")] and options._caps[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଢ଼")].lower() != bstack111l1l_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭୞"):
      del options._caps[bstack111l1l_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬୟ")]
def bstack1l1l111l1l_opy_(proxy_config):
  if bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫୠ") in proxy_config:
    proxy_config[bstack111l1l_opy_ (u"ࠨࡵࡶࡰࡕࡸ࡯ࡹࡻࠪୡ")] = proxy_config[bstack111l1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ୢ")]
    del (proxy_config[bstack111l1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧୣ")])
  if bstack111l1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧ୤") in proxy_config and proxy_config[bstack111l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ୥")].lower() != bstack111l1l_opy_ (u"࠭ࡤࡪࡴࡨࡧࡹ࠭୦"):
    proxy_config[bstack111l1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪ୧")] = bstack111l1l_opy_ (u"ࠨ࡯ࡤࡲࡺࡧ࡬ࠨ୨")
  if bstack111l1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡂࡷࡷࡳࡨࡵ࡮ࡧ࡫ࡪ࡙ࡷࡲࠧ୩") in proxy_config:
    proxy_config[bstack111l1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭୪")] = bstack111l1l_opy_ (u"ࠫࡵࡧࡣࠨ୫")
  return proxy_config
def bstack1l1lllll1_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack111l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ୬") in config:
    return proxy
  config[bstack111l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୭")] = bstack1l1l111l1l_opy_(config[bstack111l1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭୮")])
  if proxy == None:
    proxy = Proxy(config[bstack111l1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧ୯")])
  return proxy
def bstack11ll1lll1_opy_(self):
  global CONFIG
  global bstack111l1ll1l1_opy_
  try:
    proxy = bstack111ll11ll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack111l1l_opy_ (u"ࠩ࠱ࡴࡦࡩࠧ୰")):
        proxies = bstack1l11l1ll1_opy_(proxy, bstack1lll11llll_opy_())
        if len(proxies) > 0:
          protocol, bstack11l11lllll_opy_ = proxies.popitem()
          if bstack111l1l_opy_ (u"ࠥ࠾࠴࠵ࠢୱ") in bstack11l11lllll_opy_:
            return bstack11l11lllll_opy_
          else:
            return bstack111l1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧ୲") + bstack11l11lllll_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡲࡵࡳࡽࡿࠠࡶࡴ࡯ࠤ࠿ࠦࡻࡾࠤ୳").format(str(e)))
  return bstack111l1ll1l1_opy_(self)
def bstack11l1l11ll1_opy_():
  global CONFIG
  return bstack111ll1lll1_opy_(CONFIG) and bstack1ll11l11l1_opy_() and bstack1l11ll1lll_opy_() >= version.parse(bstack1ll11ll1l1_opy_)
def bstack1l1l111ll_opy_():
  global CONFIG
  return (bstack111l1l_opy_ (u"࠭ࡨࡵࡶࡳࡔࡷࡵࡸࡺࠩ୴") in CONFIG or bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ୵") in CONFIG) and bstack111lllll1_opy_()
def bstack1111l11l1l_opy_(config):
  bstack1111ll11l_opy_ = {}
  if bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୶") in config:
    bstack1111ll11l_opy_ = config[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୷")]
  if bstack111l1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୸") in config:
    bstack1111ll11l_opy_ = config[bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ୹")]
  proxy = bstack111ll11ll_opy_(config)
  if proxy:
    if proxy.endswith(bstack111l1l_opy_ (u"ࠬ࠴ࡰࡢࡥࠪ୺")) and os.path.isfile(proxy):
      bstack1111ll11l_opy_[bstack111l1l_opy_ (u"࠭࠭ࡱࡣࡦ࠱࡫࡯࡬ࡦࠩ୻")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack111l1l_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ୼")):
        proxies = bstack1l1111l1l1_opy_(config, bstack1lll11llll_opy_())
        if len(proxies) > 0:
          protocol, bstack11l11lllll_opy_ = proxies.popitem()
          if bstack111l1l_opy_ (u"ࠣ࠼࠲࠳ࠧ୽") in bstack11l11lllll_opy_:
            parsed_url = urlparse(bstack11l11lllll_opy_)
          else:
            parsed_url = urlparse(protocol + bstack111l1l_opy_ (u"ࠤ࠽࠳࠴ࠨ୾") + bstack11l11lllll_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1111ll11l_opy_[bstack111l1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡊࡲࡷࡹ࠭୿")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1111ll11l_opy_[bstack111l1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡳࡷࡺࠧ஀")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1111ll11l_opy_[bstack111l1l_opy_ (u"ࠬࡶࡲࡰࡺࡼ࡙ࡸ࡫ࡲࠨ஁")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1111ll11l_opy_[bstack111l1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡧࡳࡴࠩஂ")] = str(parsed_url.password)
  return bstack1111ll11l_opy_
def bstack111ll1ll1l_opy_(config):
  if bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬஃ") in config:
    return config[bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭஄")]
  return {}
def bstack1ll1l11ll_opy_(caps):
  global bstack1111l1111_opy_
  if bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪஅ") in caps:
    caps[bstack111l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫஆ")][bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪஇ")] = True
    if bstack1111l1111_opy_:
      caps[bstack111l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ஈ")][bstack111l1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨஉ")] = bstack1111l1111_opy_
  else:
    caps[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬஊ")] = True
    if bstack1111l1111_opy_:
      caps[bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ஋")] = bstack1111l1111_opy_
@measure(event_name=EVENTS.bstack11ll11l1l1_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1llllll111_opy_():
  global CONFIG
  if not bstack11l1l111l_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭஌") in CONFIG and bstack11l1llll1_opy_(CONFIG[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ஍")]):
    if (
      bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨஎ") in CONFIG
      and bstack11l1llll1_opy_(CONFIG[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩஏ")].get(bstack111l1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠪஐ")))
    ):
      logger.debug(bstack111l1l_opy_ (u"ࠢࡍࡱࡦࡥࡱࠦࡢࡪࡰࡤࡶࡾࠦ࡮ࡰࡶࠣࡷࡹࡧࡲࡵࡧࡧࠤࡦࡹࠠࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡦࡰࡤࡦࡱ࡫ࡤࠣ஑"))
      return
    bstack1111ll11l_opy_ = bstack1111l11l1l_opy_(CONFIG)
    bstack1l11llll1_opy_(CONFIG[bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫஒ")], bstack1111ll11l_opy_)
def bstack1l11llll1_opy_(key, bstack1111ll11l_opy_):
  global bstack111111l111_opy_
  logger.info(bstack1ll111lll_opy_)
  try:
    bstack111111l111_opy_ = Local()
    bstack111l1l1lll_opy_ = {bstack111l1l_opy_ (u"ࠩ࡮ࡩࡾ࠭ஓ"): key}
    bstack111l1l1lll_opy_.update(bstack1111ll11l_opy_)
    logger.debug(bstack111l11ll11_opy_.format(str(bstack111l1l1lll_opy_)).replace(key, bstack111l1l_opy_ (u"ࠪ࡟ࡗࡋࡄࡂࡅࡗࡉࡉࡣࠧஔ")))
    bstack111111l111_opy_.start(**bstack111l1l1lll_opy_)
    if bstack111111l111_opy_.isRunning():
      logger.info(bstack111ll1l11l_opy_)
  except Exception as e:
    bstack11l111l1l1_opy_(bstack11l1lllll1_opy_.format(str(e)))
def bstack11111l11ll_opy_():
  global bstack111111l111_opy_
  if bstack111111l111_opy_.isRunning():
    logger.info(bstack1ll1lll1l1_opy_)
    bstack111111l111_opy_.stop()
  bstack111111l111_opy_ = None
def bstack1lll1llll1_opy_(bstack1l11111l11_opy_=[]):
  global CONFIG
  bstack111l111ll_opy_ = []
  bstack1l11l1l111_opy_ = [bstack111l1l_opy_ (u"ࠫࡴࡹࠧக"), bstack111l1l_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ஖"), bstack111l1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ஗"), bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ஘"), bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ங"), bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪச")]
  try:
    for err in bstack1l11111l11_opy_:
      bstack11l1111lll_opy_ = {}
      for k in bstack1l11l1l111_opy_:
        val = CONFIG[bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭஛")][int(err[bstack111l1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪஜ")])].get(k)
        if val:
          bstack11l1111lll_opy_[k] = val
      if(err[bstack111l1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ஝")] != bstack111l1l_opy_ (u"࠭ࠧஞ")):
        bstack11l1111lll_opy_[bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸࡸ࠭ட")] = {
          err[bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭஠")]: err[bstack111l1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ஡")]
        }
        bstack111l111ll_opy_.append(bstack11l1111lll_opy_)
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬࡯ࡳ࡯ࡤࡸࡹ࡯࡮ࡨࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡪࡼࡥ࡯ࡶ࠽ࠤࠬ஢") + str(e))
  finally:
    return bstack111l111ll_opy_
def bstack1llll11111_opy_(file_name):
  bstack1111111l1_opy_ = []
  try:
    bstack1ll11l1ll_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1ll11l1ll_opy_):
      with open(bstack1ll11l1ll_opy_) as f:
        bstack1111l1llll_opy_ = json.load(f)
        bstack1111111l1_opy_ = bstack1111l1llll_opy_
      os.remove(bstack1ll11l1ll_opy_)
    return bstack1111111l1_opy_
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡪࡰࡧ࡭ࡳ࡭ࠠࡦࡴࡵࡳࡷࠦ࡬ࡪࡵࡷ࠾ࠥ࠭ண") + str(e))
    return bstack1111111l1_opy_
def bstack11l1lll11_opy_():
  try:
      from bstack_utils.constants import bstack1l1l1l111_opy_, EVENTS
      from bstack_utils.helper import bstack11llll111_opy_, get_host_info, bstack1lllll1l1_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack1ll11l1lll_opy_ = os.path.join(os.getcwd(), bstack111l1l_opy_ (u"ࠬࡲ࡯ࡨࠩத"), bstack111l1l_opy_ (u"࠭࡫ࡦࡻ࠰ࡱࡪࡺࡲࡪࡥࡶ࠲࡯ࡹ࡯࡯ࠩ஥"))
      lock = FileLock(bstack1ll11l1lll_opy_+bstack111l1l_opy_ (u"ࠢ࠯࡮ࡲࡧࡰࠨ஦"))
      def bstack1lll1l1l_opy_():
          try:
              with lock:
                  with open(bstack1ll11l1lll_opy_, bstack111l1l_opy_ (u"ࠣࡴࠥ஧"), encoding=bstack111l1l_opy_ (u"ࠤࡸࡸ࡫࠳࠸ࠣந")) as file:
                      data = json.load(file)
                      config = {
                          bstack111l1l_opy_ (u"ࠥ࡬ࡪࡧࡤࡦࡴࡶࠦன"): {
                              bstack111l1l_opy_ (u"ࠦࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠥப"): bstack111l1l_opy_ (u"ࠧࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠣ஫"),
                          }
                      }
                      bstack11ll1l1l1_opy_ = datetime.utcnow()
                      bstack1lllll11_opy_ = bstack11ll1l1l1_opy_.strftime(bstack111l1l_opy_ (u"ࠨ࡚ࠥ࠯ࠨࡱ࠲ࠫࡤࡕࠧࡋ࠾ࠪࡓ࠺ࠦࡕ࠱ࠩ࡫ࠦࡕࡕࡅࠥ஬"))
                      test_id = os.environ.get(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ஭")) if os.environ.get(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ம")) else bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦய"))
                      payload = {
                          bstack111l1l_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠢர"): bstack111l1l_opy_ (u"ࠦࡸࡪ࡫ࡠࡧࡹࡩࡳࡺࡳࠣற"),
                          bstack111l1l_opy_ (u"ࠧࡪࡡࡵࡣࠥல"): {
                              bstack111l1l_opy_ (u"ࠨࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡶࡷ࡬ࡨࠧள"): test_id,
                              bstack111l1l_opy_ (u"ࠢࡤࡴࡨࡥࡹ࡫ࡤࡠࡦࡤࡽࠧழ"): bstack1lllll11_opy_,
                              bstack111l1l_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟࡯ࡣࡰࡩࠧவ"): bstack111l1l_opy_ (u"ࠤࡖࡈࡐࡌࡥࡢࡶࡸࡶࡪࡖࡥࡳࡨࡲࡶࡲࡧ࡮ࡤࡧࠥஶ"),
                              bstack111l1l_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡ࡭ࡷࡴࡴࠢஷ"): {
                                  bstack111l1l_opy_ (u"ࠦࡲ࡫ࡡࡴࡷࡵࡩࡸࠨஸ"): data,
                                  bstack111l1l_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢஹ"): bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣ஺"))
                              },
                              bstack111l1l_opy_ (u"ࠢࡶࡵࡨࡶࡤࡪࡡࡵࡣࠥ஻"): bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠣࡷࡶࡩࡷࡔࡡ࡮ࡧࠥ஼")),
                              bstack111l1l_opy_ (u"ࠤ࡫ࡳࡸࡺ࡟ࡪࡰࡩࡳࠧ஽"): get_host_info()
                          }
                      }
                      bstack1111ll1l1_opy_ = bstack1l1ll1ll1l_opy_(cli.config, [bstack111l1l_opy_ (u"ࠥࡥࡵ࡯ࡳࠣா"), bstack111l1l_opy_ (u"ࠦࡪࡪࡳࡊࡰࡶࡸࡷࡻ࡭ࡦࡰࡷࡥࡹ࡯࡯࡯ࠤி"), bstack111l1l_opy_ (u"ࠧࡧࡰࡪࠤீ")], bstack1l1l1l111_opy_)
                      response = bstack11llll111_opy_(bstack111l1l_opy_ (u"ࠨࡐࡐࡕࡗࠦு"), bstack1111ll1l1_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack111l1l_opy_ (u"ࠢࡅࡣࡷࡥࠥࡹࡥ࡯ࡶࠣࡷࡺࡩࡣࡦࡵࡶࡪࡺࡲ࡬ࡺࠢࡷࡳࠥࢁࡽࠡࡹ࡬ࡸ࡭ࠦࡤࡢࡶࡤࠤࢀࢃࠢூ").format(bstack1l1l1l111_opy_, payload))
                      else:
                          logger.debug(bstack111l1l_opy_ (u"ࠣࡔࡨࡵࡺ࡫ࡳࡵࠢࡩࡥ࡮ࡲࡥࡥࠢࡩࡳࡷࠦࡻࡾࠢࡺ࡭ࡹ࡮ࠠࡥࡣࡷࡥࠥࢁࡽࠣ௃").format(bstack1l1l1l111_opy_, payload))
          except Exception as e:
              logger.debug(bstack111l1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥ࡯ࡦࠣ࡯ࡪࡿࠠ࡮ࡧࡷࡶ࡮ࡩࡳࠡࡦࡤࡸࡦࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣࡿࢂࠨ௄").format(e))
      bstack1lll1l1l_opy_()
      bstack11ll1lll11_opy_(bstack1ll11l1lll_opy_, logger)
  except:
    pass
def bstack1111l1111l_opy_():
  global bstack11l1l111l1_opy_
  global bstack11llllll1_opy_
  global bstack1ll1111111_opy_
  global bstack111111l11_opy_
  global bstack111l111l1_opy_
  global bstack111lll1l1l_opy_
  global CONFIG
  bstack1l1lll11l1_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫ௅"))
  if bstack1l1lll11l1_opy_ in [bstack111l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪெ"), bstack111l1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫே")]:
    bstack11llll1lll_opy_()
  percy.shutdown()
  if bstack11l1l111l1_opy_:
    logger.warning(bstack11l111ll1_opy_.format(str(bstack11l1l111l1_opy_)))
  else:
    try:
      bstack11l1l1ll1l_opy_ = bstack1l1ll11l1_opy_(bstack111l1l_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬை"), logger)
      if bstack11l1l1ll1l_opy_.get(bstack111l1l_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬ௉")) and bstack11l1l1ll1l_opy_.get(bstack111l1l_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ொ")).get(bstack111l1l_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫோ")):
        logger.warning(bstack11l111ll1_opy_.format(str(bstack11l1l1ll1l_opy_[bstack111l1l_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨௌ")][bstack111l1l_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ்࠭")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack111l1111l1_opy_.invoke(Events.bstack1l1l1ll11_opy_)
  logger.info(bstack111lll1111_opy_)
  global bstack111111l111_opy_
  if bstack111111l111_opy_:
    bstack11111l11ll_opy_()
  try:
    with bstack1ll1l111l_opy_:
      bstack1l11llll11_opy_ = bstack11llllll1_opy_.copy()
    for driver in bstack1l11llll11_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1111lll11l_opy_)
  if bstack111lll1l1l_opy_ == bstack111l1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ௎"):
    bstack111l111l1_opy_ = bstack1llll11111_opy_(bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧ௏"))
  if bstack111lll1l1l_opy_ == bstack111l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧௐ") and len(bstack111111l11_opy_) == 0:
    bstack111111l11_opy_ = bstack1llll11111_opy_(bstack111l1l_opy_ (u"ࠨࡲࡺࡣࡵࡿࡴࡦࡵࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭௑"))
    if len(bstack111111l11_opy_) == 0:
      bstack111111l11_opy_ = bstack1llll11111_opy_(bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡳࡴࡵࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨ௒"))
  bstack1ll1lll1ll_opy_ = bstack111l1l_opy_ (u"ࠪࠫ௓")
  if len(bstack1ll1111111_opy_) > 0:
    bstack1ll1lll1ll_opy_ = bstack1lll1llll1_opy_(bstack1ll1111111_opy_)
  elif len(bstack111111l11_opy_) > 0:
    bstack1ll1lll1ll_opy_ = bstack1lll1llll1_opy_(bstack111111l11_opy_)
  elif len(bstack111l111l1_opy_) > 0:
    bstack1ll1lll1ll_opy_ = bstack1lll1llll1_opy_(bstack111l111l1_opy_)
  elif len(bstack1l1l11ll1_opy_) > 0:
    bstack1ll1lll1ll_opy_ = bstack1lll1llll1_opy_(bstack1l1l11ll1_opy_)
  if bool(bstack1ll1lll1ll_opy_):
    bstack1l1ll11111_opy_(bstack1ll1lll1ll_opy_)
  else:
    bstack1l1ll11111_opy_()
  bstack11ll1lll11_opy_(bstack111l11111_opy_, logger)
  if bstack1l1lll11l1_opy_ not in [bstack111l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ௔")]:
    bstack11l1lll11_opy_()
  bstack1l11l1lll_opy_.bstack1ll1111l_opy_(CONFIG)
  if len(bstack111l111l1_opy_) > 0:
    sys.exit(len(bstack111l111l1_opy_))
def bstack1l11l1ll11_opy_(bstack11l11l1ll_opy_, frame):
  global bstack1lllll1l1_opy_
  logger.error(bstack1ll111l111_opy_)
  bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱࡔ࡯ࠨ௕"), bstack11l11l1ll_opy_)
  if hasattr(signal, bstack111l1l_opy_ (u"࠭ࡓࡪࡩࡱࡥࡱࡹࠧ௖")):
    bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧௗ"), signal.Signals(bstack11l11l1ll_opy_).name)
  else:
    bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ௘"), bstack111l1l_opy_ (u"ࠩࡖࡍࡌ࡛ࡎࡌࡐࡒ࡛ࡓ࠭௙"))
  if cli.is_running():
    bstack111l1111l1_opy_.invoke(Events.bstack1l1l1ll11_opy_)
  bstack1l1lll11l1_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫ௚"))
  if bstack1l1lll11l1_opy_ == bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ௛") and not cli.is_enabled(CONFIG):
    bstack1l1l1111_opy_.stop(bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ௜")))
  bstack1111l1111l_opy_()
  sys.exit(1)
def bstack11l111l1l1_opy_(err):
  logger.critical(bstack11ll111ll1_opy_.format(str(err)))
  bstack1l1ll11111_opy_(bstack11ll111ll1_opy_.format(str(err)), True)
  atexit.unregister(bstack1111l1111l_opy_)
  bstack11llll1lll_opy_()
  sys.exit(1)
def bstack1l11l1l1ll_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l1ll11111_opy_(message, True)
  atexit.unregister(bstack1111l1111l_opy_)
  bstack11llll1lll_opy_()
  sys.exit(1)
def bstack1lll1ll111_opy_():
  global CONFIG
  global bstack11ll11l1l_opy_
  global bstack11l1l1lll1_opy_
  global bstack1l111l111l_opy_
  CONFIG = bstack1l11111111_opy_()
  load_dotenv(CONFIG.get(bstack111l1l_opy_ (u"࠭ࡥ࡯ࡸࡉ࡭ࡱ࡫ࠧ௝")))
  bstack111l1lll1l_opy_()
  bstack1ll111lll1_opy_()
  CONFIG = bstack1l111ll111_opy_(CONFIG)
  update(CONFIG, bstack11l1l1lll1_opy_)
  update(CONFIG, bstack11ll11l1l_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack11l11l11ll_opy_(CONFIG)
  bstack1l111l111l_opy_ = bstack11l1l111l_opy_(CONFIG)
  os.environ[bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪ௞")] = bstack1l111l111l_opy_.__str__().lower()
  bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ௟"), bstack1l111l111l_opy_)
  if (bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௠") in CONFIG and bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௡") in bstack11ll11l1l_opy_) or (
          bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௢") in CONFIG and bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௣") not in bstack11l1l1lll1_opy_):
    if os.getenv(bstack111l1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪ௤")):
      CONFIG[bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ௥")] = os.getenv(bstack111l1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ௦"))
    else:
      if not CONFIG.get(bstack111l1l_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠧ௧"), bstack111l1l_opy_ (u"ࠥࠦ௨")) in bstack1ll111111_opy_:
        bstack1111l111ll_opy_()
  elif (bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௩") not in CONFIG and bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ௪") in CONFIG) or (
          bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௫") in bstack11l1l1lll1_opy_ and bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ௬") not in bstack11ll11l1l_opy_):
    del (CONFIG[bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ௭")])
  if bstack11llll11ll_opy_(CONFIG):
    bstack11l111l1l1_opy_(bstack111lllll1l_opy_)
  Config.bstack1111ll1l_opy_().set_property(bstack111l1l_opy_ (u"ࠤࡸࡷࡪࡸࡎࡢ࡯ࡨࠦ௮"), CONFIG[bstack111l1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ௯")])
  bstack1ll11lll1_opy_()
  bstack1ll111ll1_opy_()
  if bstack11ll1l11ll_opy_ and not CONFIG.get(bstack111l1l_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠢ௰"), bstack111l1l_opy_ (u"ࠧࠨ௱")) in bstack1ll111111_opy_:
    CONFIG[bstack111l1l_opy_ (u"࠭ࡡࡱࡲࠪ௲")] = bstack111ll11l1l_opy_(CONFIG)
    logger.info(bstack11l1l1ll1_opy_.format(CONFIG[bstack111l1l_opy_ (u"ࠧࡢࡲࡳࠫ௳")]))
  if not bstack1l111l111l_opy_:
    CONFIG[bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௴")] = [{}]
def bstack1ll111l11l_opy_(config, bstack11111llll1_opy_):
  global CONFIG
  global bstack11ll1l11ll_opy_
  CONFIG = config
  bstack11ll1l11ll_opy_ = bstack11111llll1_opy_
def bstack1ll111ll1_opy_():
  global CONFIG
  global bstack11ll1l11ll_opy_
  if bstack111l1l_opy_ (u"ࠩࡤࡴࡵ࠭௵") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l11l1l1ll_opy_(e, bstack11l1l11lll_opy_)
    bstack11ll1l11ll_opy_ = True
    bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ௶"), True)
def bstack111ll11l1l_opy_(config):
  bstack11ll1ll1l_opy_ = bstack111l1l_opy_ (u"ࠫࠬ௷")
  app = config[bstack111l1l_opy_ (u"ࠬࡧࡰࡱࠩ௸")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack111l1l1111_opy_:
      if os.path.exists(app):
        bstack11ll1ll1l_opy_ = bstack11l111l1l_opy_(config, app)
      elif bstack11l1l1l1l1_opy_(app):
        bstack11ll1ll1l_opy_ = app
      else:
        bstack11l111l1l1_opy_(bstack1ll1l111ll_opy_.format(app))
    else:
      if bstack11l1l1l1l1_opy_(app):
        bstack11ll1ll1l_opy_ = app
      elif os.path.exists(app):
        bstack11ll1ll1l_opy_ = bstack11l111l1l_opy_(app)
      else:
        bstack11l111l1l1_opy_(bstack11lll1ll1l_opy_)
  else:
    if len(app) > 2:
      bstack11l111l1l1_opy_(bstack1ll11ll1l_opy_)
    elif len(app) == 2:
      if bstack111l1l_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ௹") in app and bstack111l1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ௺") in app:
        if os.path.exists(app[bstack111l1l_opy_ (u"ࠨࡲࡤࡸ࡭࠭௻")]):
          bstack11ll1ll1l_opy_ = bstack11l111l1l_opy_(config, app[bstack111l1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ௼")], app[bstack111l1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭௽")])
        else:
          bstack11l111l1l1_opy_(bstack1ll1l111ll_opy_.format(app))
      else:
        bstack11l111l1l1_opy_(bstack1ll11ll1l_opy_)
    else:
      for key in app:
        if key in bstack111ll1lll_opy_:
          if key == bstack111l1l_opy_ (u"ࠫࡵࡧࡴࡩࠩ௾"):
            if os.path.exists(app[key]):
              bstack11ll1ll1l_opy_ = bstack11l111l1l_opy_(config, app[key])
            else:
              bstack11l111l1l1_opy_(bstack1ll1l111ll_opy_.format(app))
          else:
            bstack11ll1ll1l_opy_ = app[key]
        else:
          bstack11l111l1l1_opy_(bstack111l1l11ll_opy_)
  return bstack11ll1ll1l_opy_
def bstack11l1l1l1l1_opy_(bstack11ll1ll1l_opy_):
  import re
  bstack11l1111ll_opy_ = re.compile(bstack111l1l_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧ௿"))
  bstack11lll1111_opy_ = re.compile(bstack111l1l_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮࠴ࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥఀ"))
  if bstack111l1l_opy_ (u"ࠧࡣࡵ࠽࠳࠴࠭ఁ") in bstack11ll1ll1l_opy_ or re.fullmatch(bstack11l1111ll_opy_, bstack11ll1ll1l_opy_) or re.fullmatch(bstack11lll1111_opy_, bstack11ll1ll1l_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack11l11ll11l_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack11l111l1l_opy_(config, path, bstack1l1lllll11_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack111l1l_opy_ (u"ࠨࡴࡥࠫం")).read()).hexdigest()
  bstack11l1l11l11_opy_ = bstack11ll11l1ll_opy_(md5_hash)
  bstack11ll1ll1l_opy_ = None
  if bstack11l1l11l11_opy_:
    logger.info(bstack1111lll111_opy_.format(bstack11l1l11l11_opy_, md5_hash))
    return bstack11l1l11l11_opy_
  bstack1l1ll111ll_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack111l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࠧః"): (os.path.basename(path), open(os.path.abspath(path), bstack111l1l_opy_ (u"ࠪࡶࡧ࠭ఄ")), bstack111l1l_opy_ (u"ࠫࡹ࡫ࡸࡵ࠱ࡳࡰࡦ࡯࡮ࠨఅ")),
      bstack111l1l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨఆ"): bstack1l1lllll11_opy_
    }
  )
  response = requests.post(bstack111lll1lll_opy_, data=multipart_data,
                           headers={bstack111l1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬఇ"): multipart_data.content_type},
                           auth=(config[bstack111l1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩఈ")], config[bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫఉ")]))
  try:
    res = json.loads(response.text)
    bstack11ll1ll1l_opy_ = res[bstack111l1l_opy_ (u"ࠩࡤࡴࡵࡥࡵࡳ࡮ࠪఊ")]
    logger.info(bstack1l1lll1111_opy_.format(bstack11ll1ll1l_opy_))
    bstack11l1l1ll11_opy_(md5_hash, bstack11ll1ll1l_opy_)
    cli.bstack1l1l111ll1_opy_(bstack111l1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡷࡳࡰࡴࡧࡤࡠࡣࡳࡴࠧఋ"), datetime.datetime.now() - bstack1l1ll111ll_opy_)
  except ValueError as err:
    bstack11l111l1l1_opy_(bstack11ll1ll1l1_opy_.format(str(err)))
  return bstack11ll1ll1l_opy_
def bstack1ll11lll1_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack111llll111_opy_
  bstack1ll1lll1l_opy_ = 1
  bstack11l11ll1l1_opy_ = 1
  if bstack111l1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫఌ") in CONFIG:
    bstack11l11ll1l1_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ఍")]
  else:
    bstack11l11ll1l1_opy_ = bstack1l1111111_opy_(framework_name, args) or 1
  if bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩఎ") in CONFIG:
    bstack1ll1lll1l_opy_ = len(CONFIG[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪఏ")])
  bstack111llll111_opy_ = int(bstack11l11ll1l1_opy_) * int(bstack1ll1lll1l_opy_)
def bstack1l1111111_opy_(framework_name, args):
  if framework_name == bstack1ll1llll1l_opy_ and args and bstack111l1l_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ఐ") in args:
      bstack1llll1l1ll_opy_ = args.index(bstack111l1l_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ఑"))
      return int(args[bstack1llll1l1ll_opy_ + 1]) or 1
  return 1
def bstack11ll11l1ll_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack111l1l_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭ఒ"))
    bstack1ll11l1l1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠫࢃ࠭ఓ")), bstack111l1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬఔ"), bstack111l1l_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧక"))
    if os.path.exists(bstack1ll11l1l1_opy_):
      try:
        bstack1ll1l11lll_opy_ = json.load(open(bstack1ll11l1l1_opy_, bstack111l1l_opy_ (u"ࠧࡳࡤࠪఖ")))
        if md5_hash in bstack1ll1l11lll_opy_:
          bstack11111l1ll1_opy_ = bstack1ll1l11lll_opy_[md5_hash]
          bstack1ll11l111_opy_ = datetime.datetime.now()
          bstack1l1l111111_opy_ = datetime.datetime.strptime(bstack11111l1ll1_opy_[bstack111l1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫగ")], bstack111l1l_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ఘ"))
          if (bstack1ll11l111_opy_ - bstack1l1l111111_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack11111l1ll1_opy_[bstack111l1l_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨఙ")]):
            return None
          return bstack11111l1ll1_opy_[bstack111l1l_opy_ (u"ࠫ࡮ࡪࠧచ")]
      except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮ࠠࡧ࡫࡯ࡩ࠿ࠦࡻࡾࠩఛ").format(str(e)))
    return None
  bstack1ll11l1l1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"࠭ࡾࠨజ")), bstack111l1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧఝ"), bstack111l1l_opy_ (u"ࠨࡣࡳࡴ࡚ࡶ࡬ࡰࡣࡧࡑࡉ࠻ࡈࡢࡵ࡫࠲࡯ࡹ࡯࡯ࠩఞ"))
  lock_file = bstack1ll11l1l1_opy_ + bstack111l1l_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨట")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1ll11l1l1_opy_):
        with open(bstack1ll11l1l1_opy_, bstack111l1l_opy_ (u"ࠪࡶࠬఠ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll1l11lll_opy_ = json.loads(content)
            if md5_hash in bstack1ll1l11lll_opy_:
              bstack11111l1ll1_opy_ = bstack1ll1l11lll_opy_[md5_hash]
              bstack1ll11l111_opy_ = datetime.datetime.now()
              bstack1l1l111111_opy_ = datetime.datetime.strptime(bstack11111l1ll1_opy_[bstack111l1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧడ")], bstack111l1l_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩఢ"))
              if (bstack1ll11l111_opy_ - bstack1l1l111111_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack11111l1ll1_opy_[bstack111l1l_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫణ")]):
                return None
              return bstack11111l1ll1_opy_[bstack111l1l_opy_ (u"ࠧࡪࡦࠪత")]
      return None
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡸ࡫ࡷ࡬ࠥ࡬ࡩ࡭ࡧࠣࡰࡴࡩ࡫ࡪࡰࡪࠤ࡫ࡵࡲࠡࡏࡇ࠹ࠥ࡮ࡡࡴࡪ࠽ࠤࢀࢃࠧథ").format(str(e)))
    return None
def bstack11l1l1ll11_opy_(md5_hash, bstack11ll1ll1l_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack111l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬద"))
    bstack1lll111ll1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠪࢂࠬధ")), bstack111l1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫన"))
    if not os.path.exists(bstack1lll111ll1_opy_):
      os.makedirs(bstack1lll111ll1_opy_)
    bstack1ll11l1l1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠬࢄࠧ఩")), bstack111l1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ప"), bstack111l1l_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨఫ"))
    bstack11l11l11l1_opy_ = {
      bstack111l1l_opy_ (u"ࠨ࡫ࡧࠫబ"): bstack11ll1ll1l_opy_,
      bstack111l1l_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬభ"): datetime.datetime.strftime(datetime.datetime.now(), bstack111l1l_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧమ")),
      bstack111l1l_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩయ"): str(__version__)
    }
    try:
      bstack1ll1l11lll_opy_ = {}
      if os.path.exists(bstack1ll11l1l1_opy_):
        bstack1ll1l11lll_opy_ = json.load(open(bstack1ll11l1l1_opy_, bstack111l1l_opy_ (u"ࠬࡸࡢࠨర")))
      bstack1ll1l11lll_opy_[md5_hash] = bstack11l11l11l1_opy_
      with open(bstack1ll11l1l1_opy_, bstack111l1l_opy_ (u"ࠨࡷࠬࠤఱ")) as outfile:
        json.dump(bstack1ll1l11lll_opy_, outfile)
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡵࡱࡦࡤࡸ࡮ࡴࡧࠡࡏࡇ࠹ࠥ࡮ࡡࡴࡪࠣࡪ࡮ࡲࡥ࠻ࠢࡾࢁࠬల").format(str(e)))
    return
  bstack1lll111ll1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠨࢀࠪళ")), bstack111l1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩఴ"))
  if not os.path.exists(bstack1lll111ll1_opy_):
    os.makedirs(bstack1lll111ll1_opy_)
  bstack1ll11l1l1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠪࢂࠬవ")), bstack111l1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫశ"), bstack111l1l_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ష"))
  lock_file = bstack1ll11l1l1_opy_ + bstack111l1l_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬస")
  bstack11l11l11l1_opy_ = {
    bstack111l1l_opy_ (u"ࠧࡪࡦࠪహ"): bstack11ll1ll1l_opy_,
    bstack111l1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫ఺"): datetime.datetime.strftime(datetime.datetime.now(), bstack111l1l_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭఻")),
    bstack111l1l_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ఼"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1ll1l11lll_opy_ = {}
      if os.path.exists(bstack1ll11l1l1_opy_):
        with open(bstack1ll11l1l1_opy_, bstack111l1l_opy_ (u"ࠫࡷ࠭ఽ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll1l11lll_opy_ = json.loads(content)
      bstack1ll1l11lll_opy_[md5_hash] = bstack11l11l11l1_opy_
      with open(bstack1ll11l1l1_opy_, bstack111l1l_opy_ (u"ࠧࡽࠢా")) as outfile:
        json.dump(bstack1ll1l11lll_opy_, outfile)
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡽࡩࡵࡪࠣࡪ࡮ࡲࡥࠡ࡮ࡲࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨࠡࡷࡳࡨࡦࡺࡥ࠻ࠢࡾࢁࠬి").format(str(e)))
def bstack11ll111l11_opy_(self):
  return
def bstack1lllll111l_opy_(self):
  return
def bstack11l1l1lll_opy_():
  global bstack111lll1l1_opy_
  bstack111lll1l1_opy_ = True
@measure(event_name=EVENTS.bstack1lll1lll1l_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1ll1l1l11l_opy_(self):
  global bstack1lll1ll11l_opy_
  global bstack11lll11l1l_opy_
  global bstack11lllll1l1_opy_
  try:
    if bstack111l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧీ") in bstack1lll1ll11l_opy_ and self.session_id != None and bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬు"), bstack111l1l_opy_ (u"ࠩࠪూ")) != bstack111l1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫృ"):
      bstack1lllll11ll_opy_ = bstack111l1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫౄ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ౅")
      if bstack1lllll11ll_opy_ == bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ె"):
        bstack111l11ll1_opy_(logger)
      if self != None:
        bstack11ll1111l1_opy_(self, bstack1lllll11ll_opy_, bstack111l1l_opy_ (u"ࠧ࠭ࠢࠪే").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack111l1l_opy_ (u"ࠨࠩై")
    if bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ౉") in bstack1lll1ll11l_opy_ and getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩొ"), None):
      bstack111l1lll_opy_.bstack1lll1l111_opy_(self, bstack11lll11l11_opy_, logger, wait=True)
    if bstack111l1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫో") in bstack1lll1ll11l_opy_:
      if not threading.currentThread().behave_test_status:
        bstack11ll1111l1_opy_(self, bstack111l1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧౌ"))
      bstack11ll1ll1ll_opy_.bstack1l1111lll1_opy_(self)
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡹࡴࡢࡶࡸࡷ࠿్ࠦࠢ") + str(e))
  bstack11lllll1l1_opy_(self)
  self.session_id = None
def bstack111l1lll1_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1ll1ll11ll_opy_
    global bstack1lll1ll11l_opy_
    command_executor = kwargs.get(bstack111l1l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡠࡧࡻࡩࡨࡻࡴࡰࡴࠪ౎"), bstack111l1l_opy_ (u"ࠨࠩ౏"))
    bstack1llll1111l_opy_ = False
    if type(command_executor) == str and bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ౐") in command_executor:
      bstack1llll1111l_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭౑") in str(getattr(command_executor, bstack111l1l_opy_ (u"ࠫࡤࡻࡲ࡭ࠩ౒"), bstack111l1l_opy_ (u"ࠬ࠭౓"))):
      bstack1llll1111l_opy_ = True
    else:
      kwargs = bstack1lll11ll1_opy_.bstack11ll1llll1_opy_(bstack1ll111ll11_opy_=kwargs, config=CONFIG)
      return bstack1l111ll1l_opy_(self, *args, **kwargs)
    if bstack1llll1111l_opy_:
      bstack11llll11l1_opy_ = bstack11lll111l1_opy_.bstack11lll11l1_opy_(CONFIG, bstack1lll1ll11l_opy_)
      if kwargs.get(bstack111l1l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ౔")):
        kwargs[bstack111l1l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨౕ")] = bstack1ll1ll11ll_opy_(kwargs[bstack111l1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴౖࠩ")], bstack1lll1ll11l_opy_, CONFIG, bstack11llll11l1_opy_)
      elif kwargs.get(bstack111l1l_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ౗")):
        kwargs[bstack111l1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪౘ")] = bstack1ll1ll11ll_opy_(kwargs[bstack111l1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫౙ")], bstack1lll1ll11l_opy_, CONFIG, bstack11llll11l1_opy_)
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡧࡦࡶࡳ࠻ࠢࡾࢁࠧౚ").format(str(e)))
  return bstack1l111ll1l_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1lllll1ll1_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1l1l1ll1ll_opy_(self, command_executor=bstack111l1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵࠱࠳࠹࠱࠴࠳࠶࠮࠲࠼࠷࠸࠹࠺ࠢ౛"), *args, **kwargs):
  global bstack11lll11l1l_opy_
  global bstack11llllll1_opy_
  bstack1l111ll1ll_opy_ = bstack111l1lll1_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1lll1111_opy_.on():
    return bstack1l111ll1ll_opy_
  try:
    logger.debug(bstack111l1l_opy_ (u"ࠧࡄࡱࡰࡱࡦࡴࡤࠡࡇࡻࡩࡨࡻࡴࡰࡴࠣࡻ࡭࡫࡮ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡮ࡹࠠࡧࡣ࡯ࡷࡪࠦ࠭ࠡࡽࢀࠫ౜").format(str(command_executor)))
    logger.debug(bstack111l1l_opy_ (u"ࠨࡊࡸࡦ࡛ࠥࡒࡍࠢ࡬ࡷࠥ࠳ࠠࡼࡿࠪౝ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ౞") in command_executor._url:
      bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ౟"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧౠ") in command_executor):
    bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ౡ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack111l1l1l1_opy_ = getattr(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧౢ"), None)
  bstack1lll111l1l_opy_ = {}
  if self.capabilities is not None:
    bstack1lll111l1l_opy_[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭ౣ")] = self.capabilities.get(bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭౤"))
    bstack1lll111l1l_opy_[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ౥")] = self.capabilities.get(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ౦"))
    bstack1lll111l1l_opy_[bstack111l1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡣࡴࡶࡴࡪࡱࡱࡷࠬ౧")] = self.capabilities.get(bstack111l1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ౨"))
  if CONFIG.get(bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭౩"), False) and bstack1lll11ll1_opy_.bstack111111l1l_opy_(bstack1lll111l1l_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack111l1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ౪") in bstack1lll1ll11l_opy_ or bstack111l1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ౫") in bstack1lll1ll11l_opy_:
    bstack1l1l1111_opy_.bstack1l1l1111l1_opy_(self)
  if bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ౬") in bstack1lll1ll11l_opy_ and bstack111l1l1l1_opy_ and bstack111l1l1l1_opy_.get(bstack111l1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ౭"), bstack111l1l_opy_ (u"ࠫࠬ౮")) == bstack111l1l_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭౯"):
    bstack1l1l1111_opy_.bstack1l1l1111l1_opy_(self)
  bstack11lll11l1l_opy_ = self.session_id
  with bstack1ll1l111l_opy_:
    bstack11llllll1_opy_.append(self)
  return bstack1l111ll1ll_opy_
def bstack1l11l1111l_opy_(args):
  return bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠧ౰") in str(args)
def bstack1111llll1l_opy_(self, driver_command, *args, **kwargs):
  global bstack11lll1l1l1_opy_
  global bstack11l1ll1lll_opy_
  bstack11111l11l1_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫ౱"), None) and bstack1l11l1ll_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ౲"), None)
  bstack111l11l11l_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ౳"), None) and bstack1l11l1ll_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ౴"), None)
  bstack1l11l1111_opy_ = getattr(self, bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ౵"), None) != None and getattr(self, bstack111l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ౶"), None) == True
  if not bstack11l1ll1lll_opy_ and bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭౷") in CONFIG and CONFIG[bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ౸")] == True and bstack111ll11l11_opy_.bstack11llll1ll1_opy_(driver_command) and (bstack1l11l1111_opy_ or bstack11111l11l1_opy_ or bstack111l11l11l_opy_) and not bstack1l11l1111l_opy_(args):
    try:
      bstack11l1ll1lll_opy_ = True
      logger.debug(bstack111l1l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡪࡴࡸࠠࡼࡿࠪ౹").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack111l1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡥࡳࡨࡲࡶࡲࠦࡳࡤࡣࡱࠤࢀࢃࠧ౺").format(str(err)))
    bstack11l1ll1lll_opy_ = False
  response = bstack11lll1l1l1_opy_(self, driver_command, *args, **kwargs)
  if (bstack111l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ౻") in str(bstack1lll1ll11l_opy_).lower() or bstack111l1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ౼") in str(bstack1lll1ll11l_opy_).lower()) and bstack1lll1111_opy_.on():
    try:
      if driver_command == bstack111l1l_opy_ (u"ࠬࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩ౽"):
        bstack1l1l1111_opy_.bstack11111l1ll_opy_({
            bstack111l1l_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬ౾"): response[bstack111l1l_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭౿")],
            bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨಀ"): bstack1l1l1111_opy_.current_test_uuid() if bstack1l1l1111_opy_.current_test_uuid() else bstack1lll1111_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1lll11111l_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1ll11ll11l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack11lll11l1l_opy_
  global bstack11111lll11_opy_
  global bstack111l111l1l_opy_
  global bstack1llllll1l1_opy_
  global bstack1111l1l11_opy_
  global bstack1lll1ll11l_opy_
  global bstack1l111ll1l_opy_
  global bstack11llllll1_opy_
  global bstack1l1111ll1_opy_
  global bstack11lll11l11_opy_
  if os.getenv(bstack111l1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧಁ")) is not None and bstack1lll11ll1_opy_.bstack11ll1l1ll1_opy_(CONFIG) is None:
    CONFIG[bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪಂ")] = True
  CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ಃ")] = str(bstack1lll1ll11l_opy_) + str(__version__)
  bstack1l1111ll11_opy_ = os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ಄")]
  bstack11llll11l1_opy_ = bstack11lll111l1_opy_.bstack11lll11l1_opy_(CONFIG, bstack1lll1ll11l_opy_)
  CONFIG[bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩಅ")] = bstack1l1111ll11_opy_
  CONFIG[bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩಆ")] = bstack11llll11l1_opy_
  if CONFIG.get(bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨಇ"),bstack111l1l_opy_ (u"ࠩࠪಈ")) and bstack111l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩಉ") in bstack1lll1ll11l_opy_:
    CONFIG[bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫಊ")].pop(bstack111l1l_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪಋ"), None)
    CONFIG[bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ಌ")].pop(bstack111l1l_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ಍"), None)
  command_executor = bstack1lll11llll_opy_()
  logger.debug(bstack11l1llll1l_opy_.format(command_executor))
  proxy = bstack1l1lllll1_opy_(CONFIG, proxy)
  bstack1l1lll11ll_opy_ = 0 if bstack11111lll11_opy_ < 0 else bstack11111lll11_opy_
  try:
    if bstack1llllll1l1_opy_ is True:
      bstack1l1lll11ll_opy_ = int(multiprocessing.current_process().name)
    elif bstack1111l1l11_opy_ is True:
      bstack1l1lll11ll_opy_ = int(threading.current_thread().name)
  except:
    bstack1l1lll11ll_opy_ = 0
  bstack1111ll1111_opy_ = bstack1l11ll1l1l_opy_(CONFIG, bstack1l1lll11ll_opy_)
  logger.debug(bstack11l1llllll_opy_.format(str(bstack1111ll1111_opy_)))
  if bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬಎ") in CONFIG and bstack11l1llll1_opy_(CONFIG[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ಏ")]):
    bstack1ll1l11ll_opy_(bstack1111ll1111_opy_)
  if bstack1lll11ll1_opy_.bstack1l1l1111l_opy_(CONFIG, bstack1l1lll11ll_opy_) and bstack1lll11ll1_opy_.bstack1l1llll1ll_opy_(bstack1111ll1111_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack1lll11ll1_opy_.set_capabilities(bstack1111ll1111_opy_, CONFIG)
  if desired_capabilities:
    bstack11l1l11111_opy_ = bstack1l111ll111_opy_(desired_capabilities)
    bstack11l1l11111_opy_[bstack111l1l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪಐ")] = bstack1ll1l111l1_opy_(CONFIG)
    bstack1111l1ll11_opy_ = bstack1l11ll1l1l_opy_(bstack11l1l11111_opy_)
    if bstack1111l1ll11_opy_:
      bstack1111ll1111_opy_ = update(bstack1111l1ll11_opy_, bstack1111ll1111_opy_)
    desired_capabilities = None
  if options:
    bstack1ll1l11l1l_opy_(options, bstack1111ll1111_opy_)
  if not options:
    options = bstack1l1l1lll11_opy_(bstack1111ll1111_opy_)
  bstack11lll11l11_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಑"))[bstack1l1lll11ll_opy_]
  if proxy and bstack1l11ll1lll_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬಒ")):
    options.proxy(proxy)
  if options and bstack1l11ll1lll_opy_() >= version.parse(bstack111l1l_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬಓ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1l11ll1lll_opy_() < version.parse(bstack111l1l_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ಔ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1111ll1111_opy_)
  logger.info(bstack11l1l11l1l_opy_)
  bstack1l11l1l11_opy_.end(EVENTS.bstack111l1ll1ll_opy_.value, EVENTS.bstack111l1ll1ll_opy_.value + bstack111l1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣಕ"), EVENTS.bstack111l1ll1ll_opy_.value + bstack111l1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢಖ"), status=True, failure=None, test_name=bstack111l111l1l_opy_)
  if bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡵࡸ࡯ࡧ࡫࡯ࡩࠬಗ") in kwargs:
    del kwargs[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡶࡲࡰࡨ࡬ࡰࡪ࠭ಘ")]
  try:
    if bstack1l11ll1lll_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠬ࠺࠮࠲࠲࠱࠴ࠬಙ")):
      bstack1l111ll1l_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack1l11ll1lll_opy_() >= version.parse(bstack111l1l_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬಚ")):
      bstack1l111ll1l_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l11ll1lll_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠧ࠳࠰࠸࠷࠳࠶ࠧಛ")):
      bstack1l111ll1l_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1l111ll1l_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack11lll1l111_opy_:
    logger.error(bstack1111l11l11_opy_.format(bstack111l1l_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠧಜ"), str(bstack11lll1l111_opy_)))
    raise bstack11lll1l111_opy_
  if bstack1lll11ll1_opy_.bstack1l1l1111l_opy_(CONFIG, bstack1l1lll11ll_opy_) and bstack1lll11ll1_opy_.bstack1l1llll1ll_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫಝ")][bstack111l1l_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩಞ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack1lll11ll1_opy_.set_capabilities(bstack1111ll1111_opy_, CONFIG)
  try:
    bstack1111l1l111_opy_ = bstack111l1l_opy_ (u"ࠫࠬಟ")
    if bstack1l11ll1lll_opy_() >= version.parse(bstack111l1l_opy_ (u"ࠬ࠺࠮࠱࠰࠳ࡦ࠶࠭ಠ")):
      if self.caps is not None:
        bstack1111l1l111_opy_ = self.caps.get(bstack111l1l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨಡ"))
    else:
      if self.capabilities is not None:
        bstack1111l1l111_opy_ = self.capabilities.get(bstack111l1l_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢಢ"))
    if bstack1111l1l111_opy_:
      bstack1l1111l111_opy_(bstack1111l1l111_opy_)
      if bstack1l11ll1lll_opy_() <= version.parse(bstack111l1l_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨಣ")):
        self.command_executor._url = bstack111l1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥತ") + bstack1l111l11l1_opy_ + bstack111l1l_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢಥ")
      else:
        self.command_executor._url = bstack111l1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨದ") + bstack1111l1l111_opy_ + bstack111l1l_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨಧ")
      logger.debug(bstack11ll1111ll_opy_.format(bstack1111l1l111_opy_))
    else:
      logger.debug(bstack1111l11lll_opy_.format(bstack111l1l_opy_ (u"ࠨࡏࡱࡶ࡬ࡱࡦࡲࠠࡉࡷࡥࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠢನ")))
  except Exception as e:
    logger.debug(bstack1111l11lll_opy_.format(e))
  if bstack111l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭಩") in bstack1lll1ll11l_opy_:
    bstack111llllll_opy_(bstack11111lll11_opy_, bstack1l1111ll1_opy_)
  bstack11lll11l1l_opy_ = self.session_id
  if bstack111l1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨಪ") in bstack1lll1ll11l_opy_ or bstack111l1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩಫ") in bstack1lll1ll11l_opy_ or bstack111l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩಬ") in bstack1lll1ll11l_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack111l1l1l1_opy_ = getattr(threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥࠬಭ"), None)
  if bstack111l1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬಮ") in bstack1lll1ll11l_opy_ or bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಯ") in bstack1lll1ll11l_opy_:
    bstack1l1l1111_opy_.bstack1l1l1111l1_opy_(self)
  if bstack111l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧರ") in bstack1lll1ll11l_opy_ and bstack111l1l1l1_opy_ and bstack111l1l1l1_opy_.get(bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨಱ"), bstack111l1l_opy_ (u"ࠩࠪಲ")) == bstack111l1l_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫಳ"):
    bstack1l1l1111_opy_.bstack1l1l1111l1_opy_(self)
  with bstack1ll1l111l_opy_:
    bstack11llllll1_opy_.append(self)
  if bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಴") in CONFIG and bstack111l1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪವ") in CONFIG[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಶ")][bstack1l1lll11ll_opy_]:
    bstack111l111l1l_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಷ")][bstack1l1lll11ll_opy_][bstack111l1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ಸ")]
  logger.debug(bstack1l1ll1111l_opy_.format(bstack11lll11l1l_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1111l1lll1_opy_
    def bstack11lllll11_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack11l1l1l11_opy_
      if(bstack111l1l_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸ࠯࡬ࡶࠦಹ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠪࢂࠬ಺")), bstack111l1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫ಻"), bstack111l1l_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺ಼ࠧ")), bstack111l1l_opy_ (u"࠭ࡷࠨಽ")) as fp:
          fp.write(bstack111l1l_opy_ (u"ࠢࠣಾ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack111l1l_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥಿ")))):
          with open(args[1], bstack111l1l_opy_ (u"ࠩࡵࠫೀ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack111l1l_opy_ (u"ࠪࡥࡸࡿ࡮ࡤࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡤࡴࡥࡸࡒࡤ࡫ࡪ࠮ࡣࡰࡰࡷࡩࡽࡺࠬࠡࡲࡤ࡫ࡪࠦ࠽ࠡࡸࡲ࡭ࡩࠦ࠰ࠪࠩು") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1l11l11ll1_opy_)
            if bstack111l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨೂ") in CONFIG and str(CONFIG[bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩೃ")]).lower() != bstack111l1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬೄ"):
                bstack111ll1l11_opy_ = bstack1111l1lll1_opy_()
                bstack1l11ll1ll1_opy_ = bstack111l1l_opy_ (u"ࠧࠨࠩࠍ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࠐࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹࡝࠼ࠌࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠ࠿ࠏࡩ࡯࡯ࡵࡷࠤࡵࡥࡩ࡯ࡦࡨࡼࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠳࡟࠾ࠎࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡸࡲࡩࡤࡧࠫ࠴࠱ࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴ࠫ࠾ࠎࡨࡵ࡮ࡴࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫ࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤࠬ࠿ࠏ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡲࡡࡶࡰࡦ࡬ࠥࡃࠠࡢࡵࡼࡲࡨࠦࠨ࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠩࠡ࠿ࡁࠤࢀࢁࠊࠡࠢ࡯ࡩࡹࠦࡣࡢࡲࡶ࠿ࠏࠦࠠࡵࡴࡼࠤࢀࢁࠊࠡࠢࠣࠤࡨࡧࡰࡴࠢࡀࠤࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸ࠯࠻ࠋࠢࠣࢁࢂࠦࡣࡢࡶࡦ࡬ࠥ࠮ࡥࡹࠫࠣࡿࢀࠐࠠࠡࠢࠣࡧࡴࡴࡳࡰ࡮ࡨ࠲ࡪࡸࡲࡰࡴࠫࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡣࡵࡷࡪࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠿ࠨࠬࠡࡧࡻ࠭ࡀࠐࠠࠡࡿࢀࠎࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻࡼࠌࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࠬࢁࡣࡥࡲࡘࡶࡱࢃࠧࠡ࠭ࠣࡩࡳࡩ࡯ࡥࡧࡘࡖࡎࡉ࡯࡮ࡲࡲࡲࡪࡴࡴࠩࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡦࡥࡵࡹࠩࠪ࠮ࠍࠤࠥࠦࠠ࠯࠰࠱ࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵࠍࠤࠥࢃࡽࠪ࠽ࠍࢁࢂࡁࠊ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠍࠫࠬ࠭೅").format(bstack111ll1l11_opy_=bstack111ll1l11_opy_)
            lines.insert(1, bstack1l11ll1ll1_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack111l1l_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥೆ")), bstack111l1l_opy_ (u"ࠩࡺࠫೇ")) as bstack11111ll1ll_opy_:
              bstack11111ll1ll_opy_.writelines(lines)
        CONFIG[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬೈ")] = str(bstack1lll1ll11l_opy_) + str(__version__)
        bstack1l1111ll11_opy_ = os.environ[bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ೉")]
        bstack11llll11l1_opy_ = bstack11lll111l1_opy_.bstack11lll11l1_opy_(CONFIG, bstack1lll1ll11l_opy_)
        CONFIG[bstack111l1l_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨೊ")] = bstack1l1111ll11_opy_
        CONFIG[bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨೋ")] = bstack11llll11l1_opy_
        bstack1l1lll11ll_opy_ = 0 if bstack11111lll11_opy_ < 0 else bstack11111lll11_opy_
        try:
          if bstack1llllll1l1_opy_ is True:
            bstack1l1lll11ll_opy_ = int(multiprocessing.current_process().name)
          elif bstack1111l1l11_opy_ is True:
            bstack1l1lll11ll_opy_ = int(threading.current_thread().name)
        except:
          bstack1l1lll11ll_opy_ = 0
        CONFIG[bstack111l1l_opy_ (u"ࠢࡶࡵࡨ࡛࠸ࡉࠢೌ")] = False
        CONFIG[bstack111l1l_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ್ࠢ")] = True
        bstack1111ll1111_opy_ = bstack1l11ll1l1l_opy_(CONFIG, bstack1l1lll11ll_opy_)
        logger.debug(bstack11l1llllll_opy_.format(str(bstack1111ll1111_opy_)))
        if CONFIG.get(bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭೎")):
          bstack1ll1l11ll_opy_(bstack1111ll1111_opy_)
        if bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭೏") in CONFIG and bstack111l1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ೐") in CONFIG[bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ೑")][bstack1l1lll11ll_opy_]:
          bstack111l111l1l_opy_ = CONFIG[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ೒")][bstack1l1lll11ll_opy_][bstack111l1l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ೓")]
        args.append(os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠨࢀࠪ೔")), bstack111l1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩೕ"), bstack111l1l_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬೖ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1111ll1111_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack111l1l_opy_ (u"ࠦ࡮ࡴࡤࡦࡺࡢࡦࡸࡺࡡࡤ࡭࠱࡮ࡸࠨ೗"))
      bstack11l1l1l11_opy_ = True
      return bstack11llllll11_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack1111l1l1ll_opy_(self,
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
    global bstack11111lll11_opy_
    global bstack111l111l1l_opy_
    global bstack1llllll1l1_opy_
    global bstack1111l1l11_opy_
    global bstack1lll1ll11l_opy_
    CONFIG[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧ೘")] = str(bstack1lll1ll11l_opy_) + str(__version__)
    bstack1l1111ll11_opy_ = os.environ[bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ೙")]
    bstack11llll11l1_opy_ = bstack11lll111l1_opy_.bstack11lll11l1_opy_(CONFIG, bstack1lll1ll11l_opy_)
    CONFIG[bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ೚")] = bstack1l1111ll11_opy_
    CONFIG[bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ೛")] = bstack11llll11l1_opy_
    bstack1l1lll11ll_opy_ = 0 if bstack11111lll11_opy_ < 0 else bstack11111lll11_opy_
    try:
      if bstack1llllll1l1_opy_ is True:
        bstack1l1lll11ll_opy_ = int(multiprocessing.current_process().name)
      elif bstack1111l1l11_opy_ is True:
        bstack1l1lll11ll_opy_ = int(threading.current_thread().name)
    except:
      bstack1l1lll11ll_opy_ = 0
    CONFIG[bstack111l1l_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ೜")] = True
    bstack1111ll1111_opy_ = bstack1l11ll1l1l_opy_(CONFIG, bstack1l1lll11ll_opy_)
    logger.debug(bstack11l1llllll_opy_.format(str(bstack1111ll1111_opy_)))
    if CONFIG.get(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧೝ")):
      bstack1ll1l11ll_opy_(bstack1111ll1111_opy_)
    if bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧೞ") in CONFIG and bstack111l1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ೟") in CONFIG[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩೠ")][bstack1l1lll11ll_opy_]:
      bstack111l111l1l_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪೡ")][bstack1l1lll11ll_opy_][bstack111l1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ೢ")]
    import urllib
    import json
    if bstack111l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ೣ") in CONFIG and str(CONFIG[bstack111l1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ೤")]).lower() != bstack111l1l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ೥"):
        bstack11l11l1l11_opy_ = bstack1111l1lll1_opy_()
        bstack111ll1l11_opy_ = bstack11l11l1l11_opy_ + urllib.parse.quote(json.dumps(bstack1111ll1111_opy_))
    else:
        bstack111ll1l11_opy_ = bstack111l1l_opy_ (u"ࠬࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠧ೦") + urllib.parse.quote(json.dumps(bstack1111ll1111_opy_))
    browser = self.connect(bstack111ll1l11_opy_)
    return browser
except Exception as e:
    pass
def bstack1l111l11ll_opy_():
    global bstack11l1l1l11_opy_
    global bstack1lll1ll11l_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1111l11111_opy_
        global bstack1lllll1l1_opy_
        if not bstack1l111l111l_opy_:
          global bstack11ll11l111_opy_
          if not bstack11ll11l111_opy_:
            from bstack_utils.helper import bstack11lll1llll_opy_, bstack11l1l1l111_opy_, bstack11l1111l11_opy_
            bstack11ll11l111_opy_ = bstack11lll1llll_opy_()
            bstack11l1l1l111_opy_(bstack1lll1ll11l_opy_)
            bstack11llll11l1_opy_ = bstack11lll111l1_opy_.bstack11lll11l1_opy_(CONFIG, bstack1lll1ll11l_opy_)
            bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠨࡐࡍࡃ࡜࡛ࡗࡏࡇࡉࡖࡢࡔࡗࡕࡄࡖࡅࡗࡣࡒࡇࡐࠣ೧"), bstack11llll11l1_opy_)
          BrowserType.connect = bstack1111l11111_opy_
          return
        BrowserType.launch = bstack1111l1l1ll_opy_
        bstack11l1l1l11_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack11lllll11_opy_
      bstack11l1l1l11_opy_ = True
    except Exception as e:
      pass
def bstack1lll1l1111_opy_(context, bstack1l1ll11l11_opy_):
  try:
    context.page.evaluate(bstack111l1l_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ೨"), bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠬ೩")+ json.dumps(bstack1l1ll11l11_opy_) + bstack111l1l_opy_ (u"ࠤࢀࢁࠧ೪"))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥࢁࡽ࠻ࠢࡾࢁࠧ೫").format(str(e), traceback.format_exc()))
def bstack111lll11ll_opy_(context, message, level):
  try:
    context.page.evaluate(bstack111l1l_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧ೬"), bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ೭") + json.dumps(message) + bstack111l1l_opy_ (u"࠭ࠬࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠩ೮") + json.dumps(level) + bstack111l1l_opy_ (u"ࠧࡾࡿࠪ೯"))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡦࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠡࡽࢀ࠾ࠥࢁࡽࠣ೰").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack11l111ll11_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1ll1l1l1l_opy_(self, url):
  global bstack1ll1111lll_opy_
  try:
    bstack1l1l1lll1l_opy_(url)
  except Exception as err:
    logger.debug(bstack111l11l1ll_opy_.format(str(err)))
  try:
    bstack1ll1111lll_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack11111ll11_opy_):
        bstack1l1l1lll1l_opy_(url, True)
    except Exception as err:
      logger.debug(bstack111l11l1ll_opy_.format(str(err)))
    raise e
def bstack111llll11_opy_(self):
  global bstack1ll1l11l11_opy_
  bstack1ll1l11l11_opy_ = self
  return
def bstack1l1111l11_opy_(self):
  global bstack1l11ll111_opy_
  bstack1l11ll111_opy_ = self
  return
def bstack1ll11111ll_opy_(test_name, bstack11l1l11ll_opy_):
  global CONFIG
  if percy.bstack111llll1ll_opy_() == bstack111l1l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢೱ"):
    bstack1l111l1l1l_opy_ = os.path.relpath(bstack11l1l11ll_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1l111l1l1l_opy_)
    bstack11l1111ll1_opy_ = suite_name + bstack111l1l_opy_ (u"ࠥ࠱ࠧೲ") + test_name
    threading.current_thread().percySessionName = bstack11l1111ll1_opy_
def bstack111l1lllll_opy_(self, test, *args, **kwargs):
  global bstack1lllllll11_opy_
  test_name = None
  bstack11l1l11ll_opy_ = None
  if test:
    test_name = str(test.name)
    bstack11l1l11ll_opy_ = str(test.source)
  bstack1ll11111ll_opy_(test_name, bstack11l1l11ll_opy_)
  bstack1lllllll11_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l1lll111l_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1ll1l1lll1_opy_(driver, bstack11l1111ll1_opy_):
  if not bstack111ll1l1l_opy_ and bstack11l1111ll1_opy_:
      bstack11llllll1l_opy_ = {
          bstack111l1l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫೳ"): bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭೴"),
          bstack111l1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ೵"): {
              bstack111l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ೶"): bstack11l1111ll1_opy_
          }
      }
      bstack1l1l1l1111_opy_ = bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭೷").format(json.dumps(bstack11llllll1l_opy_))
      driver.execute_script(bstack1l1l1l1111_opy_)
  if bstack1lll11l1ll_opy_:
      bstack11l11lll11_opy_ = {
          bstack111l1l_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ೸"): bstack111l1l_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬ೹"),
          bstack111l1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ೺"): {
              bstack111l1l_opy_ (u"ࠬࡪࡡࡵࡣࠪ೻"): bstack11l1111ll1_opy_ + bstack111l1l_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨ೼"),
              bstack111l1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭೽"): bstack111l1l_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭೾")
          }
      }
      if bstack1lll11l1ll_opy_.status == bstack111l1l_opy_ (u"ࠩࡓࡅࡘ࡙ࠧ೿"):
          bstack1111l111l1_opy_ = bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨഀ").format(json.dumps(bstack11l11lll11_opy_))
          driver.execute_script(bstack1111l111l1_opy_)
          bstack11ll1111l1_opy_(driver, bstack111l1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫഁ"))
      elif bstack1lll11l1ll_opy_.status == bstack111l1l_opy_ (u"ࠬࡌࡁࡊࡎࠪം"):
          reason = bstack111l1l_opy_ (u"ࠨࠢഃ")
          bstack11111l11l_opy_ = bstack11l1111ll1_opy_ + bstack111l1l_opy_ (u"ࠧࠡࡨࡤ࡭ࡱ࡫ࡤࠨഄ")
          if bstack1lll11l1ll_opy_.message:
              reason = str(bstack1lll11l1ll_opy_.message)
              bstack11111l11l_opy_ = bstack11111l11l_opy_ + bstack111l1l_opy_ (u"ࠨࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࡀࠠࠨഅ") + reason
          bstack11l11lll11_opy_[bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬആ")] = {
              bstack111l1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩഇ"): bstack111l1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪഈ"),
              bstack111l1l_opy_ (u"ࠬࡪࡡࡵࡣࠪഉ"): bstack11111l11l_opy_
          }
          bstack1111l111l1_opy_ = bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫഊ").format(json.dumps(bstack11l11lll11_opy_))
          driver.execute_script(bstack1111l111l1_opy_)
          bstack11ll1111l1_opy_(driver, bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧഋ"), reason)
          bstack1l1111l1l_opy_(reason, str(bstack1lll11l1ll_opy_), str(bstack11111lll11_opy_), logger)
@measure(event_name=EVENTS.bstack11llll1111_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1ll111111l_opy_(driver, test):
  if percy.bstack111llll1ll_opy_() == bstack111l1l_opy_ (u"ࠣࡶࡵࡹࡪࠨഌ") and percy.bstack1l1ll1lll1_opy_() == bstack111l1l_opy_ (u"ࠤࡷࡩࡸࡺࡣࡢࡵࡨࠦ഍"):
      bstack1111ll111l_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭എ"), None)
      bstack1l1ll111l1_opy_(driver, bstack1111ll111l_opy_, test)
  if (bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨഏ"), None) and
      bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫഐ"), None)) or (
      bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭഑"), None) and
      bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩഒ"), None)):
      logger.info(bstack111l1l_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠦࡐࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡ࡫ࡶࠤࡺࡴࡤࡦࡴࡺࡥࡾ࠴ࠠࠣഓ"))
      bstack1lll11ll1_opy_.bstack111l11ll_opy_(driver, name=test.name, path=test.source)
def bstack1l1l111lll_opy_(test, bstack11l1111ll1_opy_):
    try:
      bstack1l1ll111ll_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧഔ")] = bstack11l1111ll1_opy_
      if bstack1lll11l1ll_opy_:
        if bstack1lll11l1ll_opy_.status == bstack111l1l_opy_ (u"ࠪࡔࡆ࡙ࡓࠨക"):
          data[bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫഖ")] = bstack111l1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬഗ")
        elif bstack1lll11l1ll_opy_.status == bstack111l1l_opy_ (u"࠭ࡆࡂࡋࡏࠫഘ"):
          data[bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧങ")] = bstack111l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨച")
          if bstack1lll11l1ll_opy_.message:
            data[bstack111l1l_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩഛ")] = str(bstack1lll11l1ll_opy_.message)
      user = CONFIG[bstack111l1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬജ")]
      key = CONFIG[bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧഝ")]
      host = bstack1l1ll1ll1l_opy_(cli.config, [bstack111l1l_opy_ (u"ࠧࡧࡰࡪࡵࠥഞ"), bstack111l1l_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥࠣട"), bstack111l1l_opy_ (u"ࠢࡢࡲ࡬ࠦഠ")], bstack111l1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠤഡ"))
      url = bstack111l1l_opy_ (u"ࠩࡾࢁ࠴ࡧࡵࡵࡱࡰࡥࡹ࡫࠯ࡴࡧࡶࡷ࡮ࡵ࡮ࡴ࠱ࡾࢁ࠳ࡰࡳࡰࡰࠪഢ").format(host, bstack11lll11l1l_opy_)
      headers = {
        bstack111l1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩണ"): bstack111l1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧത"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1l1l111ll1_opy_(bstack111l1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽ࡹࡵࡪࡡࡵࡧࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠤഥ"), datetime.datetime.now() - bstack1l1ll111ll_opy_)
    except Exception as e:
      logger.error(bstack1111ll1ll_opy_.format(str(e)))
def bstack11l1l1llll_opy_(test, bstack11l1111ll1_opy_):
  global CONFIG
  global bstack1l11ll111_opy_
  global bstack1ll1l11l11_opy_
  global bstack11lll11l1l_opy_
  global bstack1lll11l1ll_opy_
  global bstack111l111l1l_opy_
  global bstack11l1111l1_opy_
  global bstack11l1111111_opy_
  global bstack111l1l111l_opy_
  global bstack1llll1ll11_opy_
  global bstack11llllll1_opy_
  global bstack11lll11l11_opy_
  global bstack111l1l1ll_opy_
  try:
    if not bstack11lll11l1l_opy_:
      with bstack111l1l1ll_opy_:
        bstack1l11lllll1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"࠭ࡾࠨദ")), bstack111l1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧധ"), bstack111l1l_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪന"))
        if os.path.exists(bstack1l11lllll1_opy_):
          with open(bstack1l11lllll1_opy_, bstack111l1l_opy_ (u"ࠩࡵࠫഩ")) as f:
            content = f.read().strip()
            if content:
              bstack11lll1l11l_opy_ = json.loads(bstack111l1l_opy_ (u"ࠥࡿࠧപ") + content + bstack111l1l_opy_ (u"ࠫࠧࡾࠢ࠻ࠢࠥࡽࠧ࠭ഫ") + bstack111l1l_opy_ (u"ࠧࢃࠢബ"))
              bstack11lll11l1l_opy_ = bstack11lll1l11l_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࡶࠤ࡫࡯࡬ࡦ࠼ࠣࠫഭ") + str(e))
  if bstack11llllll1_opy_:
    with bstack1ll1l111l_opy_:
      bstack1lllll1lll_opy_ = bstack11llllll1_opy_.copy()
    for driver in bstack1lllll1lll_opy_:
      if bstack11lll11l1l_opy_ == driver.session_id:
        if test:
          bstack1ll111111l_opy_(driver, test)
        bstack1ll1l1lll1_opy_(driver, bstack11l1111ll1_opy_)
  elif bstack11lll11l1l_opy_:
    bstack1l1l111lll_opy_(test, bstack11l1111ll1_opy_)
  if bstack1l11ll111_opy_:
    bstack11l1111111_opy_(bstack1l11ll111_opy_)
  if bstack1ll1l11l11_opy_:
    bstack111l1l111l_opy_(bstack1ll1l11l11_opy_)
  if bstack111lll1l1_opy_:
    bstack1llll1ll11_opy_()
def bstack1llllll1ll_opy_(self, test, *args, **kwargs):
  bstack11l1111ll1_opy_ = None
  if test:
    bstack11l1111ll1_opy_ = str(test.name)
  bstack11l1l1llll_opy_(test, bstack11l1111ll1_opy_)
  bstack11l1111l1_opy_(self, test, *args, **kwargs)
def bstack11llll1ll_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1ll11l1l1l_opy_
  global CONFIG
  global bstack11llllll1_opy_
  global bstack11lll11l1l_opy_
  global bstack111l1l1ll_opy_
  bstack111ll11111_opy_ = None
  try:
    if bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭മ"), None) or bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪയ"), None):
      try:
        if not bstack11lll11l1l_opy_:
          bstack1l11lllll1_opy_ = os.path.join(os.path.expanduser(bstack111l1l_opy_ (u"ࠩࢁࠫര")), bstack111l1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪറ"), bstack111l1l_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭ല"))
          with bstack111l1l1ll_opy_:
            if os.path.exists(bstack1l11lllll1_opy_):
              with open(bstack1l11lllll1_opy_, bstack111l1l_opy_ (u"ࠬࡸࠧള")) as f:
                content = f.read().strip()
                if content:
                  bstack11lll1l11l_opy_ = json.loads(bstack111l1l_opy_ (u"ࠨࡻࠣഴ") + content + bstack111l1l_opy_ (u"ࠧࠣࡺࠥ࠾ࠥࠨࡹࠣࠩവ") + bstack111l1l_opy_ (u"ࠣࡿࠥശ"))
                  bstack11lll11l1l_opy_ = bstack11lll1l11l_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡍࡉࡹࠠࡧ࡫࡯ࡩࠥ࡯࡮ࠡࡶࡨࡷࡹࠦࡳࡵࡣࡷࡹࡸࡀࠠࠨഷ") + str(e))
      if bstack11llllll1_opy_:
        with bstack1ll1l111l_opy_:
          bstack1lllll1lll_opy_ = bstack11llllll1_opy_.copy()
        for driver in bstack1lllll1lll_opy_:
          if bstack11lll11l1l_opy_ == driver.session_id:
            bstack111ll11111_opy_ = driver
    bstack1111lllll1_opy_ = bstack1lll11ll1_opy_.bstack1l1ll11lll_opy_(test.tags)
    if bstack111ll11111_opy_:
      threading.current_thread().isA11yTest = bstack1lll11ll1_opy_.bstack1lll1lll11_opy_(bstack111ll11111_opy_, bstack1111lllll1_opy_)
      threading.current_thread().isAppA11yTest = bstack1lll11ll1_opy_.bstack1lll1lll11_opy_(bstack111ll11111_opy_, bstack1111lllll1_opy_)
    else:
      threading.current_thread().isA11yTest = bstack1111lllll1_opy_
      threading.current_thread().isAppA11yTest = bstack1111lllll1_opy_
  except:
    pass
  bstack1ll11l1l1l_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1lll11l1ll_opy_
  try:
    bstack1lll11l1ll_opy_ = self._test
  except:
    bstack1lll11l1ll_opy_ = self.test
def bstack11l111l1ll_opy_():
  global bstack111ll111l_opy_
  try:
    if os.path.exists(bstack111ll111l_opy_):
      os.remove(bstack111ll111l_opy_)
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭സ") + str(e))
def bstack1111l1l11l_opy_():
  global bstack111ll111l_opy_
  bstack11l1l1ll1l_opy_ = {}
  lock_file = bstack111ll111l_opy_ + bstack111l1l_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪഹ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨഺ"))
    try:
      if not os.path.isfile(bstack111ll111l_opy_):
        with open(bstack111ll111l_opy_, bstack111l1l_opy_ (u"࠭ࡷࠨ഻")) as f:
          json.dump({}, f)
      if os.path.exists(bstack111ll111l_opy_):
        with open(bstack111ll111l_opy_, bstack111l1l_opy_ (u"ࠧࡳ഼ࠩ")) as f:
          content = f.read().strip()
          if content:
            bstack11l1l1ll1l_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪࡧࡤࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪഽ") + str(e))
    return bstack11l1l1ll1l_opy_
  try:
    os.makedirs(os.path.dirname(bstack111ll111l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack111ll111l_opy_):
        with open(bstack111ll111l_opy_, bstack111l1l_opy_ (u"ࠩࡺࠫാ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack111ll111l_opy_):
        with open(bstack111ll111l_opy_, bstack111l1l_opy_ (u"ࠪࡶࠬി")) as f:
          content = f.read().strip()
          if content:
            bstack11l1l1ll1l_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ീ") + str(e))
  finally:
    return bstack11l1l1ll1l_opy_
def bstack111llllll_opy_(platform_index, item_index):
  global bstack111ll111l_opy_
  lock_file = bstack111ll111l_opy_ + bstack111l1l_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫു")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack111l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩൂ"))
    try:
      bstack11l1l1ll1l_opy_ = {}
      if os.path.exists(bstack111ll111l_opy_):
        with open(bstack111ll111l_opy_, bstack111l1l_opy_ (u"ࠧࡳࠩൃ")) as f:
          content = f.read().strip()
          if content:
            bstack11l1l1ll1l_opy_ = json.loads(content)
      bstack11l1l1ll1l_opy_[item_index] = platform_index
      with open(bstack111ll111l_opy_, bstack111l1l_opy_ (u"ࠣࡹࠥൄ")) as outfile:
        json.dump(bstack11l1l1ll1l_opy_, outfile)
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡼࡸࡩࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧ൅") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack111ll111l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack11l1l1ll1l_opy_ = {}
      if os.path.exists(bstack111ll111l_opy_):
        with open(bstack111ll111l_opy_, bstack111l1l_opy_ (u"ࠪࡶࠬെ")) as f:
          content = f.read().strip()
          if content:
            bstack11l1l1ll1l_opy_ = json.loads(content)
      bstack11l1l1ll1l_opy_[item_index] = platform_index
      with open(bstack111ll111l_opy_, bstack111l1l_opy_ (u"ࠦࡼࠨേ")) as outfile:
        json.dump(bstack11l1l1ll1l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡸࡴ࡬ࡸ࡮ࡴࡧࠡࡶࡲࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪൈ") + str(e))
def bstack11lll1111l_opy_(bstack111l1l11l1_opy_):
  global CONFIG
  bstack1l1llll11_opy_ = bstack111l1l_opy_ (u"࠭ࠧ൉")
  if not bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪൊ") in CONFIG:
    logger.info(bstack111l1l_opy_ (u"ࠨࡐࡲࠤࡵࡲࡡࡵࡨࡲࡶࡲࡹࠠࡱࡣࡶࡷࡪࡪࠠࡶࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡴࡥࡳࡣࡷࡩࠥࡸࡥࡱࡱࡵࡸࠥ࡬࡯ࡳࠢࡕࡳࡧࡵࡴࠡࡴࡸࡲࠬോ"))
  try:
    platform = CONFIG[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬൌ")][bstack111l1l11l1_opy_]
    if bstack111l1l_opy_ (u"ࠪࡳࡸ്࠭") in platform:
      bstack1l1llll11_opy_ += str(platform[bstack111l1l_opy_ (u"ࠫࡴࡹࠧൎ")]) + bstack111l1l_opy_ (u"ࠬ࠲ࠠࠨ൏")
    if bstack111l1l_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ൐") in platform:
      bstack1l1llll11_opy_ += str(platform[bstack111l1l_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪ൑")]) + bstack111l1l_opy_ (u"ࠨ࠮ࠣࠫ൒")
    if bstack111l1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭൓") in platform:
      bstack1l1llll11_opy_ += str(platform[bstack111l1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧൔ")]) + bstack111l1l_opy_ (u"ࠫ࠱ࠦࠧൕ")
    if bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧൖ") in platform:
      bstack1l1llll11_opy_ += str(platform[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨൗ")]) + bstack111l1l_opy_ (u"ࠧ࠭ࠢࠪ൘")
    if bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭൙") in platform:
      bstack1l1llll11_opy_ += str(platform[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ൚")]) + bstack111l1l_opy_ (u"ࠪ࠰ࠥ࠭൛")
    if bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ൜") in platform:
      bstack1l1llll11_opy_ += str(platform[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭൝")]) + bstack111l1l_opy_ (u"࠭ࠬࠡࠩ൞")
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠧࡔࡱࡰࡩࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡱࡩࡷࡧࡴࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡳࡵࡴ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡶࡪࡶ࡯ࡳࡶࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡴࡴࠧൟ") + str(e))
  finally:
    if bstack1l1llll11_opy_[len(bstack1l1llll11_opy_) - 2:] == bstack111l1l_opy_ (u"ࠨ࠮ࠣࠫൠ"):
      bstack1l1llll11_opy_ = bstack1l1llll11_opy_[:-2]
    return bstack1l1llll11_opy_
def bstack11ll11ll11_opy_(path, bstack1l1llll11_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack11111ll1l1_opy_ = ET.parse(path)
    bstack1lll111111_opy_ = bstack11111ll1l1_opy_.getroot()
    bstack11l1l11l1_opy_ = None
    for suite in bstack1lll111111_opy_.iter(bstack111l1l_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨൡ")):
      if bstack111l1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪൢ") in suite.attrib:
        suite.attrib[bstack111l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩൣ")] += bstack111l1l_opy_ (u"ࠬࠦࠧ൤") + bstack1l1llll11_opy_
        bstack11l1l11l1_opy_ = suite
    bstack1l11l1l1l_opy_ = None
    for robot in bstack1lll111111_opy_.iter(bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ൥")):
      bstack1l11l1l1l_opy_ = robot
    bstack11ll1l1111_opy_ = len(bstack1l11l1l1l_opy_.findall(bstack111l1l_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭൦")))
    if bstack11ll1l1111_opy_ == 1:
      bstack1l11l1l1l_opy_.remove(bstack1l11l1l1l_opy_.findall(bstack111l1l_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧ൧"))[0])
      bstack1ll111l1l_opy_ = ET.Element(bstack111l1l_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨ൨"), attrib={bstack111l1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ൩"): bstack111l1l_opy_ (u"ࠫࡘࡻࡩࡵࡧࡶࠫ൪"), bstack111l1l_opy_ (u"ࠬ࡯ࡤࠨ൫"): bstack111l1l_opy_ (u"࠭ࡳ࠱ࠩ൬")})
      bstack1l11l1l1l_opy_.insert(1, bstack1ll111l1l_opy_)
      bstack11ll1111l_opy_ = None
      for suite in bstack1l11l1l1l_opy_.iter(bstack111l1l_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭൭")):
        bstack11ll1111l_opy_ = suite
      bstack11ll1111l_opy_.append(bstack11l1l11l1_opy_)
      bstack11llll111l_opy_ = None
      for status in bstack11l1l11l1_opy_.iter(bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ൮")):
        bstack11llll111l_opy_ = status
      bstack11ll1111l_opy_.append(bstack11llll111l_opy_)
    bstack11111ll1l1_opy_.write(path)
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠧ൯") + str(e))
def bstack111l1111ll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack11ll1lll1l_opy_
  global CONFIG
  if bstack111l1l_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢ൰") in options:
    del options[bstack111l1l_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣ൱")]
  json_data = bstack1111l1l11l_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack111l1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࡣࡷ࡫ࡳࡶ࡮ࡷࡷࠬ൲"), str(item_id), bstack111l1l_opy_ (u"࠭࡯ࡶࡶࡳࡹࡹ࠴ࡸ࡮࡮ࠪ൳"))
    bstack11ll11ll11_opy_(path, bstack11lll1111l_opy_(json_data[item_id]))
  bstack11l111l1ll_opy_()
  return bstack11ll1lll1l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack111l111111_opy_(self, ff_profile_dir):
  global bstack1ll1lllll1_opy_
  if not ff_profile_dir:
    return None
  return bstack1ll1lllll1_opy_(self, ff_profile_dir)
def bstack1l1l1l111l_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1111l1111_opy_
  bstack1l111ll1l1_opy_ = []
  if bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ൴") in CONFIG:
    bstack1l111ll1l1_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ൵")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack111l1l_opy_ (u"ࠤࡦࡳࡲࡳࡡ࡯ࡦࠥ൶")],
      pabot_args[bstack111l1l_opy_ (u"ࠥࡺࡪࡸࡢࡰࡵࡨࠦ൷")],
      argfile,
      pabot_args.get(bstack111l1l_opy_ (u"ࠦ࡭࡯ࡶࡦࠤ൸")),
      pabot_args[bstack111l1l_opy_ (u"ࠧࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠣ൹")],
      platform[0],
      bstack1111l1111_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack111l1l_opy_ (u"ࠨࡡࡳࡩࡸࡱࡪࡴࡴࡧ࡫࡯ࡩࡸࠨൺ")] or [(bstack111l1l_opy_ (u"ࠢࠣൻ"), None)]
    for platform in enumerate(bstack1l111ll1l1_opy_)
  ]
def bstack1llll11l11_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack111111l11l_opy_=bstack111l1l_opy_ (u"ࠨࠩർ")):
  global bstack1l1llllll_opy_
  self.platform_index = platform_index
  self.bstack11lllll1ll_opy_ = bstack111111l11l_opy_
  bstack1l1llllll_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack11lll1ll11_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack11ll11lll1_opy_
  global bstack1ll1l11ll1_opy_
  bstack1ll1l11111_opy_ = copy.deepcopy(item)
  if not bstack111l1l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫൽ") in item.options:
    bstack1ll1l11111_opy_.options[bstack111l1l_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬൾ")] = []
  bstack111l1llll_opy_ = bstack1ll1l11111_opy_.options[bstack111l1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ൿ")].copy()
  for v in bstack1ll1l11111_opy_.options[bstack111l1l_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ඀")]:
    if bstack111l1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜ࠬඁ") in v:
      bstack111l1llll_opy_.remove(v)
    if bstack111l1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙ࠧං") in v:
      bstack111l1llll_opy_.remove(v)
    if bstack111l1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬඃ") in v:
      bstack111l1llll_opy_.remove(v)
  bstack111l1llll_opy_.insert(0, bstack111l1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘ࠻ࡽࢀࠫ඄").format(bstack1ll1l11111_opy_.platform_index))
  bstack111l1llll_opy_.insert(0, bstack111l1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘ࠺ࡼࡿࠪඅ").format(bstack1ll1l11111_opy_.bstack11lllll1ll_opy_))
  bstack1ll1l11111_opy_.options[bstack111l1l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ආ")] = bstack111l1llll_opy_
  if bstack1ll1l11ll1_opy_:
    bstack1ll1l11111_opy_.options[bstack111l1l_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧඇ")].insert(0, bstack111l1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘࡀࡻࡾࠩඈ").format(bstack1ll1l11ll1_opy_))
  return bstack11ll11lll1_opy_(caller_id, datasources, is_last, bstack1ll1l11111_opy_, outs_dir)
def bstack1l11lll111_opy_(command, item_index):
  try:
    if bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨඉ")):
      os.environ[bstack111l1l_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩඊ")] = json.dumps(CONFIG[bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬඋ")][item_index % bstack1ll11llll_opy_])
    global bstack1ll1l11ll1_opy_
    if bstack1ll1l11ll1_opy_:
      command[0] = command[0].replace(bstack111l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩඌ"), bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨඍ") + str(
        item_index) + bstack111l1l_opy_ (u"ࠬࠦࠧඎ") + bstack1ll1l11ll1_opy_, 1)
    else:
      command[0] = command[0].replace(bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬඏ"),
                                      bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡳࡥ࡭ࠣࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠣࠫඐ") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠ࡮ࡱࡧ࡭࡫ࡿࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡢࡰࡧࠤ࡫ࡵࡲࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱ࠾ࠥࢁࡽࠨඑ").format(str(e)))
def bstack1l1l11l1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1l11lll11l_opy_
  try:
    bstack1l11lll111_opy_(command, item_index)
    return bstack1l11lll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴ࠺ࠡࡽࢀࠫඒ").format(str(e)))
    raise e
def bstack1l11l1l1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1l11lll11l_opy_
  try:
    bstack1l11lll111_opy_(command, item_index)
    return bstack1l11lll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠴࠱࠵࠸ࡀࠠࡼࡿࠪඓ").format(str(e)))
    try:
      return bstack1l11lll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack111l1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࠸࠮࠲࠵ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩඔ").format(str(e2)))
      raise e
def bstack1l1l1l1l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1l11lll11l_opy_
  try:
    bstack1l11lll111_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack1l11lll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰࠣ࠶࠳࠷࠵࠻ࠢࡾࢁࠬඕ").format(str(e)))
    try:
      return bstack1l11lll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack111l1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠ࠳࠰࠴࠹ࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫඖ").format(str(e2)))
      raise e
def _11l1ll1ll1_opy_(bstack11lll11111_opy_, item_index, process_timeout, sleep_before_start, bstack1l1l1l1l11_opy_):
  bstack1l11lll111_opy_(bstack11lll11111_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack1llll1l1l1_opy_(command, bstack11l11l11l_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1l11lll11l_opy_
  try:
    bstack1l11lll111_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack1l11lll11l_opy_(command, bstack11l11l11l_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲࠥ࠻࠮࠱࠼ࠣࡿࢂ࠭඗").format(str(e)))
    try:
      return bstack1l11lll11l_opy_(command, bstack11l11l11l_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack111l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨ඘").format(str(e2)))
      raise e
def bstack1l11ll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1l11lll11l_opy_
  try:
    process_timeout = _11l1ll1ll1_opy_(command, item_index, process_timeout, sleep_before_start, bstack111l1l_opy_ (u"ࠩ࠷࠲࠷࠭඙"))
    return bstack1l11lll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠶࠱࠶࠿ࠦࡻࡾࠩක").format(str(e)))
    try:
      return bstack1l11lll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack111l1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫඛ").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack1l1ll11ll1_opy_(self, runner, quiet=False, capture=True):
  global bstack1l111l111_opy_
  bstack1l1l1l1l1_opy_ = bstack1l111l111_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack111l1l_opy_ (u"ࠬ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࡠࡣࡵࡶࠬග")):
      runner.exception_arr = []
    if not hasattr(runner, bstack111l1l_opy_ (u"࠭ࡥࡹࡥࡢࡸࡷࡧࡣࡦࡤࡤࡧࡰࡥࡡࡳࡴࠪඝ")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1l1l1l1l1_opy_
def bstack1l1l11l1l_opy_(runner, hook_name, context, element, bstack11ll1ll111_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1llll111l1_opy_.bstack11l1111l_opy_(hook_name, element)
    bstack11ll1ll111_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1llll111l1_opy_.bstack11l11111_opy_(element)
      if hook_name not in [bstack111l1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫඞ"), bstack111l1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫඟ")] and args and hasattr(args[0], bstack111l1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࡠ࡯ࡨࡷࡸࡧࡧࡦࠩච")):
        args[0].error_message = bstack111l1l_opy_ (u"ࠪࠫඡ")
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡩࡣࡱࡨࡱ࡫ࠠࡩࡱࡲ࡯ࡸࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦ࠼ࠣࡿࢂ࠭ජ").format(str(e)))
@measure(event_name=EVENTS.bstack1l111lllll_opy_, stage=STAGE.bstack1ll1ll111_opy_, hook_type=bstack111l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡆࡲ࡬ࠣඣ"), bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1ll11l11ll_opy_(runner, name, context, bstack11ll1ll111_opy_, *args):
    if runner.hooks.get(bstack111l1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥඤ")).__name__ != bstack111l1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࡣࡩ࡫ࡦࡢࡷ࡯ࡸࡤ࡮࡯ࡰ࡭ࠥඥ"):
      bstack1l1l11l1l_opy_(runner, name, context, runner, bstack11ll1ll111_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1l1l11ll11_opy_(bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧඦ")) else context.browser
      runner.driver_initialised = bstack111l1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨට")
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡸ࡫ࠠࡢࡶࡷࡶ࡮ࡨࡵࡵࡧ࠽ࠤࢀࢃࠧඨ").format(str(e)))
def bstack1111llll11_opy_(runner, name, context, bstack11ll1ll111_opy_, *args):
    bstack1l1l11l1l_opy_(runner, name, context, context.feature, bstack11ll1ll111_opy_, *args)
    try:
      if not bstack111ll1l1l_opy_:
        bstack111ll11111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1l11ll11_opy_(bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪඩ")) else context.browser
        if is_driver_active(bstack111ll11111_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack111l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨඪ")
          bstack1l1ll11l11_opy_ = str(runner.feature.name)
          bstack1lll1l1111_opy_(context, bstack1l1ll11l11_opy_)
          bstack111ll11111_opy_.execute_script(bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫණ") + json.dumps(bstack1l1ll11l11_opy_) + bstack111l1l_opy_ (u"ࠧࡾࡿࠪඬ"))
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨත").format(str(e)))
def bstack1l111l1l11_opy_(runner, name, context, bstack11ll1ll111_opy_, *args):
    if hasattr(context, bstack111l1l_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫථ")):
        bstack1llll111l1_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack111l1l_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬද")) else context.feature
    bstack1l1l11l1l_opy_(runner, name, context, target, bstack11ll1ll111_opy_, *args)
@measure(event_name=EVENTS.bstack11l1l1111l_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1l1ll1l11l_opy_(runner, name, context, bstack11ll1ll111_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1llll111l1_opy_.start_test(context)
    bstack1l1l11l1l_opy_(runner, name, context, context.scenario, bstack11ll1ll111_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack11ll1ll1ll_opy_.bstack1ll1l1lll_opy_(context, *args)
    try:
      bstack111ll11111_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪධ"), context.browser)
      if is_driver_active(bstack111ll11111_opy_):
        bstack1l1l1111_opy_.bstack1l1l1111l1_opy_(bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫන"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack111l1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣ඲")
        if (not bstack111ll1l1l_opy_):
          scenario_name = args[0].name
          feature_name = bstack1l1ll11l11_opy_ = str(runner.feature.name)
          bstack1l1ll11l11_opy_ = feature_name + bstack111l1l_opy_ (u"ࠧࠡ࠯ࠣࠫඳ") + scenario_name
          if runner.driver_initialised == bstack111l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥප"):
            bstack1lll1l1111_opy_(context, bstack1l1ll11l11_opy_)
            bstack111ll11111_opy_.execute_script(bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧඵ") + json.dumps(bstack1l1ll11l11_opy_) + bstack111l1l_opy_ (u"ࠪࢁࢂ࠭බ"))
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬභ").format(str(e)))
@measure(event_name=EVENTS.bstack1l111lllll_opy_, stage=STAGE.bstack1ll1ll111_opy_, hook_type=bstack111l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡘࡺࡥࡱࠤම"), bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack111111ll1_opy_(runner, name, context, bstack11ll1ll111_opy_, *args):
    bstack1l1l11l1l_opy_(runner, name, context, args[0], bstack11ll1ll111_opy_, *args)
    try:
      bstack111ll11111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1l11ll11_opy_(bstack111l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඹ")) else context.browser
      if is_driver_active(bstack111ll11111_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack111l1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧය")
        bstack1llll111l1_opy_.bstack11l111l1_opy_(args[0])
        if runner.driver_initialised == bstack111l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨර"):
          feature_name = bstack1l1ll11l11_opy_ = str(runner.feature.name)
          bstack1l1ll11l11_opy_ = feature_name + bstack111l1l_opy_ (u"ࠩࠣ࠱ࠥ࠭඼") + context.scenario.name
          bstack111ll11111_opy_.execute_script(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨල") + json.dumps(bstack1l1ll11l11_opy_) + bstack111l1l_opy_ (u"ࠫࢂࢃࠧ඾"))
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩ඿").format(str(e)))
@measure(event_name=EVENTS.bstack1l111lllll_opy_, stage=STAGE.bstack1ll1ll111_opy_, hook_type=bstack111l1l_opy_ (u"ࠨࡡࡧࡶࡨࡶࡘࡺࡥࡱࠤව"), bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack11l1lll1ll_opy_(runner, name, context, bstack11ll1ll111_opy_, *args):
  bstack1llll111l1_opy_.bstack11l1l111_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack111ll11111_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ශ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack111ll11111_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack111l1l_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨෂ")
        feature_name = bstack1l1ll11l11_opy_ = str(runner.feature.name)
        bstack1l1ll11l11_opy_ = feature_name + bstack111l1l_opy_ (u"ࠩࠣ࠱ࠥ࠭ස") + context.scenario.name
        bstack111ll11111_opy_.execute_script(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨහ") + json.dumps(bstack1l1ll11l11_opy_) + bstack111l1l_opy_ (u"ࠫࢂࢃࠧළ"))
    if str(step_status).lower() == bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬෆ"):
      bstack1ll1l11l1_opy_ = bstack111l1l_opy_ (u"࠭ࠧ෇")
      bstack1lll1l1lll_opy_ = bstack111l1l_opy_ (u"ࠧࠨ෈")
      bstack111llll11l_opy_ = bstack111l1l_opy_ (u"ࠨࠩ෉")
      try:
        import traceback
        bstack1ll1l11l1_opy_ = runner.exception.__class__.__name__
        bstack111lllll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1lll1l1lll_opy_ = bstack111l1l_opy_ (u"්ࠩࠣࠫ").join(bstack111lllll_opy_)
        bstack111llll11l_opy_ = bstack111lllll_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l1lll1l1l_opy_.format(str(e)))
      bstack1ll1l11l1_opy_ += bstack111llll11l_opy_
      bstack111lll11ll_opy_(context, json.dumps(str(args[0].name) + bstack111l1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ෋") + str(bstack1lll1l1lll_opy_)),
                          bstack111l1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ෌"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥ෍"):
        bstack1lll11lll1_opy_(getattr(context, bstack111l1l_opy_ (u"࠭ࡰࡢࡩࡨࠫ෎"), None), bstack111l1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢා"), bstack1ll1l11l1_opy_)
        bstack111ll11111_opy_.execute_script(bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ැ") + json.dumps(str(args[0].name) + bstack111l1l_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣෑ") + str(bstack1lll1l1lll_opy_)) + bstack111l1l_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪි"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤී"):
        bstack11ll1111l1_opy_(bstack111ll11111_opy_, bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬු"), bstack111l1l_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥ෕") + str(bstack1ll1l11l1_opy_))
    else:
      bstack111lll11ll_opy_(context, bstack111l1l_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣූ"), bstack111l1l_opy_ (u"ࠣ࡫ࡱࡪࡴࠨ෗"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢෘ"):
        bstack1lll11lll1_opy_(getattr(context, bstack111l1l_opy_ (u"ࠪࡴࡦ࡭ࡥࠨෙ"), None), bstack111l1l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦේ"))
      bstack111ll11111_opy_.execute_script(bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪෛ") + json.dumps(str(args[0].name) + bstack111l1l_opy_ (u"ࠨࠠ࠮ࠢࡓࡥࡸࡹࡥࡥࠣࠥො")) + bstack111l1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭ෝ"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨෞ"):
        bstack11ll1111l1_opy_(bstack111ll11111_opy_, bstack111l1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤෟ"))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩ෠").format(str(e)))
  bstack1l1l11l1l_opy_(runner, name, context, args[0], bstack11ll1ll111_opy_, *args)
@measure(event_name=EVENTS.bstack1l1l1lll1_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1ll11ll1ll_opy_(runner, name, context, bstack11ll1ll111_opy_, *args):
  bstack1llll111l1_opy_.end_test(args[0])
  try:
    bstack11l111l11l_opy_ = args[0].status.name
    bstack111ll11111_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ෡"), context.browser)
    bstack11ll1ll1ll_opy_.bstack1l1111lll1_opy_(bstack111ll11111_opy_)
    if str(bstack11l111l11l_opy_).lower() == bstack111l1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ෢"):
      bstack1ll1l11l1_opy_ = bstack111l1l_opy_ (u"࠭ࠧ෣")
      bstack1lll1l1lll_opy_ = bstack111l1l_opy_ (u"ࠧࠨ෤")
      bstack111llll11l_opy_ = bstack111l1l_opy_ (u"ࠨࠩ෥")
      try:
        import traceback
        bstack1ll1l11l1_opy_ = runner.exception.__class__.__name__
        bstack111lllll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1lll1l1lll_opy_ = bstack111l1l_opy_ (u"ࠩࠣࠫ෦").join(bstack111lllll_opy_)
        bstack111llll11l_opy_ = bstack111lllll_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l1lll1l1l_opy_.format(str(e)))
      bstack1ll1l11l1_opy_ += bstack111llll11l_opy_
      bstack111lll11ll_opy_(context, json.dumps(str(args[0].name) + bstack111l1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ෧") + str(bstack1lll1l1lll_opy_)),
                          bstack111l1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ෨"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ෩") or runner.driver_initialised == bstack111l1l_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෪"):
        bstack1lll11lll1_opy_(getattr(context, bstack111l1l_opy_ (u"ࠧࡱࡣࡪࡩࠬ෫"), None), bstack111l1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ෬"), bstack1ll1l11l1_opy_)
        bstack111ll11111_opy_.execute_script(bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ෭") + json.dumps(str(args[0].name) + bstack111l1l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ෮") + str(bstack1lll1l1lll_opy_)) + bstack111l1l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫ෯"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ෰") or runner.driver_initialised == bstack111l1l_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෱"):
        bstack11ll1111l1_opy_(bstack111ll11111_opy_, bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧෲ"), bstack111l1l_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧෳ") + str(bstack1ll1l11l1_opy_))
    else:
      bstack111lll11ll_opy_(context, bstack111l1l_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥ෴"), bstack111l1l_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣ෵"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ෶") or runner.driver_initialised == bstack111l1l_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ෷"):
        bstack1lll11lll1_opy_(getattr(context, bstack111l1l_opy_ (u"࠭ࡰࡢࡩࡨࠫ෸"), None), bstack111l1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ෹"))
      bstack111ll11111_opy_.execute_script(bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭෺") + json.dumps(str(args[0].name) + bstack111l1l_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨ෻")) + bstack111l1l_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩ෼"))
      if runner.driver_initialised == bstack111l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ෽") or runner.driver_initialised == bstack111l1l_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ෾"):
        bstack11ll1111l1_opy_(bstack111ll11111_opy_, bstack111l1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ෿"))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩ฀").format(str(e)))
  bstack1l1l11l1l_opy_(runner, name, context, context.scenario, bstack11ll1ll111_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack111111l1l1_opy_(runner, name, context, bstack11ll1ll111_opy_, *args):
    target = context.scenario if hasattr(context, bstack111l1l_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪก")) else context.feature
    bstack1l1l11l1l_opy_(runner, name, context, target, bstack11ll1ll111_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1l1ll1111_opy_(runner, name, context, bstack11ll1ll111_opy_, *args):
    try:
      bstack111ll11111_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨข"), context.browser)
      bstack1l111l1l1_opy_ = bstack111l1l_opy_ (u"ࠪࠫฃ")
      if context.failed is True:
        bstack1lll1111ll_opy_ = []
        bstack11l111lll1_opy_ = []
        bstack1llll11lll_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1lll1111ll_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack111lllll_opy_ = traceback.format_tb(exc_tb)
            bstack111llll1l1_opy_ = bstack111l1l_opy_ (u"ࠫࠥ࠭ค").join(bstack111lllll_opy_)
            bstack11l111lll1_opy_.append(bstack111llll1l1_opy_)
            bstack1llll11lll_opy_.append(bstack111lllll_opy_[-1])
        except Exception as e:
          logger.debug(bstack1l1lll1l1l_opy_.format(str(e)))
        bstack1ll1l11l1_opy_ = bstack111l1l_opy_ (u"ࠬ࠭ฅ")
        for i in range(len(bstack1lll1111ll_opy_)):
          bstack1ll1l11l1_opy_ += bstack1lll1111ll_opy_[i] + bstack1llll11lll_opy_[i] + bstack111l1l_opy_ (u"࠭࡜࡯ࠩฆ")
        bstack1l111l1l1_opy_ = bstack111l1l_opy_ (u"ࠧࠡࠩง").join(bstack11l111lll1_opy_)
        if runner.driver_initialised in [bstack111l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤจ"), bstack111l1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨฉ")]:
          bstack111lll11ll_opy_(context, bstack1l111l1l1_opy_, bstack111l1l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤช"))
          bstack1lll11lll1_opy_(getattr(context, bstack111l1l_opy_ (u"ࠫࡵࡧࡧࡦࠩซ"), None), bstack111l1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧฌ"), bstack1ll1l11l1_opy_)
          bstack111ll11111_opy_.execute_script(bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫญ") + json.dumps(bstack1l111l1l1_opy_) + bstack111l1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧฎ"))
          bstack11ll1111l1_opy_(bstack111ll11111_opy_, bstack111l1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣฏ"), bstack111l1l_opy_ (u"ࠤࡖࡳࡲ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰࡵࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡡࡴࠢฐ") + str(bstack1ll1l11l1_opy_))
          bstack11l1ll1l11_opy_ = bstack1l1l111l11_opy_(bstack1l111l1l1_opy_, runner.feature.name, logger)
          if (bstack11l1ll1l11_opy_ != None):
            bstack1l1l11ll1_opy_.append(bstack11l1ll1l11_opy_)
      else:
        if runner.driver_initialised in [bstack111l1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦฑ"), bstack111l1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣฒ")]:
          bstack111lll11ll_opy_(context, bstack111l1l_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣณ") + str(runner.feature.name) + bstack111l1l_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣด"), bstack111l1l_opy_ (u"ࠢࡪࡰࡩࡳࠧต"))
          bstack1lll11lll1_opy_(getattr(context, bstack111l1l_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ถ"), None), bstack111l1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤท"))
          bstack111ll11111_opy_.execute_script(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨธ") + json.dumps(bstack111l1l_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢน") + str(runner.feature.name) + bstack111l1l_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢบ")) + bstack111l1l_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬป"))
          bstack11ll1111l1_opy_(bstack111ll11111_opy_, bstack111l1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧผ"))
          bstack11l1ll1l11_opy_ = bstack1l1l111l11_opy_(bstack1l111l1l1_opy_, runner.feature.name, logger)
          if (bstack11l1ll1l11_opy_ != None):
            bstack1l1l11ll1_opy_.append(bstack11l1ll1l11_opy_)
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪฝ").format(str(e)))
    bstack1l1l11l1l_opy_(runner, name, context, context.feature, bstack11ll1ll111_opy_, *args)
@measure(event_name=EVENTS.bstack1l111lllll_opy_, stage=STAGE.bstack1ll1ll111_opy_, hook_type=bstack111l1l_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡂ࡮࡯ࠦพ"), bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1ll11l1ll1_opy_(runner, name, context, bstack11ll1ll111_opy_, *args):
    bstack1l1l11l1l_opy_(runner, name, context, runner, bstack11ll1ll111_opy_, *args)
def bstack1l111l1ll1_opy_(self, name, context, *args):
  try:
    if bstack1l111l111l_opy_:
      platform_index = int(threading.current_thread()._name) % bstack1ll11llll_opy_
      bstack1l111ll11l_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ฟ")][platform_index]
      os.environ[bstack111l1l_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬภ")] = json.dumps(bstack1l111ll11l_opy_)
    global bstack11ll1ll111_opy_
    if not hasattr(self, bstack111l1l_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡦࡦࠪม")):
      self.driver_initialised = None
    bstack1111ll11ll_opy_ = {
        bstack111l1l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪย"): bstack1ll11l11ll_opy_,
        bstack111l1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠨร"): bstack1111llll11_opy_,
        bstack111l1l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡶࡤ࡫ࠬฤ"): bstack1l111l1l11_opy_,
        bstack111l1l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫล"): bstack1l1ll1l11l_opy_,
        bstack111l1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠨฦ"): bstack111111ll1_opy_,
        bstack111l1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡹ࡫ࡰࠨว"): bstack11l1lll1ll_opy_,
        bstack111l1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ศ"): bstack1ll11ll1ll_opy_,
        bstack111l1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡺࡡࡨࠩษ"): bstack111111l1l1_opy_,
        bstack111l1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧส"): bstack1l1ll1111_opy_,
        bstack111l1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫห"): bstack1ll11l1ll1_opy_
    }
    handler = bstack1111ll11ll_opy_.get(name, bstack11ll1ll111_opy_)
    try:
      handler(self, name, context, bstack11ll1ll111_opy_, *args)
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨࠤ࡭ࡵ࡯࡬ࠢ࡫ࡥࡳࡪ࡬ࡦࡴࠣࡿࢂࡀࠠࡼࡿࠪฬ").format(name, str(e)))
    if name in [bstack111l1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪอ"), bstack111l1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬฮ"), bstack111l1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨฯ")]:
      try:
        bstack111ll11111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1l11ll11_opy_(bstack111l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬะ")) else context.browser
        bstack111l1l111_opy_ = (
          (name == bstack111l1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪั") and self.driver_initialised == bstack111l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧา")) or
          (name == bstack111l1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩำ") and self.driver_initialised == bstack111l1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦิ")) or
          (name == bstack111l1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬี") and self.driver_initialised in [bstack111l1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢึ"), bstack111l1l_opy_ (u"ࠨࡩ࡯ࡵࡷࡩࡵࠨื")]) or
          (name == bstack111l1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡵࡧࡳุࠫ") and self.driver_initialised == bstack111l1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨู"))
        )
        if bstack111l1l111_opy_:
          self.driver_initialised = None
          if bstack111ll11111_opy_ and hasattr(bstack111ll11111_opy_, bstack111l1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩฺ࠭")):
            try:
              bstack111ll11111_opy_.quit()
            except Exception as e:
              logger.debug(bstack111l1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡴࡹ࡮ࡺࡴࡪࡰࡪࠤࡩࡸࡩࡷࡧࡵࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡩࡱࡲ࡯࠿ࠦࡻࡾࠩ฻").format(str(e)))
      except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡮࡯ࡰ࡭ࠣࡧࡱ࡫ࡡ࡯ࡷࡳࠤ࡫ࡵࡲࠡࡽࢀ࠾ࠥࢁࡽࠨ฼").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠬࡉࡲࡪࡶ࡬ࡧࡦࡲࠠࡦࡴࡵࡳࡷࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦࠢࡵࡹࡳࠦࡨࡰࡱ࡮ࠤࢀࢃ࠺ࠡࡽࢀࠫ฽").format(name, str(e)))
    try:
      bstack11ll1ll111_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack111l1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡳࡷ࡯ࡧࡪࡰࡤࡰࠥࡨࡥࡩࡣࡹࡩࠥ࡮࡯ࡰ࡭ࠣࡿࢂࡀࠠࡼࡿࠪ฾").format(name, str(e2)))
def bstack11l1ll1111_opy_(config, startdir):
  return bstack111l1l_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧ฿").format(bstack111l1l_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢเ"))
notset = Notset()
def bstack1l1l1111ll_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1l1llll11l_opy_
  if str(name).lower() == bstack111l1l_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩแ"):
    return bstack111l1l_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤโ")
  else:
    return bstack1l1llll11l_opy_(self, name, default, skip)
def bstack1ll111l11_opy_(item, when):
  global bstack111l111l11_opy_
  try:
    bstack111l111l11_opy_(item, when)
  except Exception as e:
    pass
def bstack11ll111l1_opy_():
  return
def bstack1ll1l1l1ll_opy_(type, name, status, reason, bstack1l11lll11_opy_, bstack1l11lllll_opy_):
  bstack11llllll1l_opy_ = {
    bstack111l1l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫใ"): type,
    bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨไ"): {}
  }
  if type == bstack111l1l_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨๅ"):
    bstack11llllll1l_opy_[bstack111l1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪๆ")][bstack111l1l_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ็")] = bstack1l11lll11_opy_
    bstack11llllll1l_opy_[bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷ่ࠬ")][bstack111l1l_opy_ (u"ࠪࡨࡦࡺࡡࠨ้")] = json.dumps(str(bstack1l11lllll_opy_))
  if type == bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩ๊ࠬ"):
    bstack11llllll1l_opy_[bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ๋")][bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ์")] = name
  if type == bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪํ"):
    bstack11llllll1l_opy_[bstack111l1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ๎")][bstack111l1l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ๏")] = status
    if status == bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ๐"):
      bstack11llllll1l_opy_[bstack111l1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ๑")][bstack111l1l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ๒")] = json.dumps(str(reason))
  bstack1l1l1l1111_opy_ = bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ๓").format(json.dumps(bstack11llllll1l_opy_))
  return bstack1l1l1l1111_opy_
def bstack1ll1ll1l11_opy_(driver_command, response):
    if driver_command == bstack111l1l_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫ๔"):
        bstack1l1l1111_opy_.bstack11111l1ll_opy_({
            bstack111l1l_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧ๕"): response[bstack111l1l_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨ๖")],
            bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ๗"): bstack1l1l1111_opy_.current_test_uuid()
        })
def bstack111111ll1l_opy_(item, call, rep):
  global bstack1l11llllll_opy_
  global bstack11llllll1_opy_
  global bstack111ll1l1l_opy_
  name = bstack111l1l_opy_ (u"ࠫࠬ๘")
  try:
    if rep.when == bstack111l1l_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ๙"):
      bstack11lll11l1l_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack111ll1l1l_opy_:
          name = str(rep.nodeid)
          bstack111lll1ll_opy_ = bstack1ll1l1l1ll_opy_(bstack111l1l_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ๚"), name, bstack111l1l_opy_ (u"ࠧࠨ๛"), bstack111l1l_opy_ (u"ࠨࠩ๜"), bstack111l1l_opy_ (u"ࠩࠪ๝"), bstack111l1l_opy_ (u"ࠪࠫ๞"))
          threading.current_thread().bstack11ll11lll_opy_ = name
          for driver in bstack11llllll1_opy_:
            if bstack11lll11l1l_opy_ == driver.session_id:
              driver.execute_script(bstack111lll1ll_opy_)
      except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ๟").format(str(e)))
      try:
        bstack1llll11l1l_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack111l1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭๠"):
          status = bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭๡") if rep.outcome.lower() == bstack111l1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ๢") else bstack111l1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ๣")
          reason = bstack111l1l_opy_ (u"ࠩࠪ๤")
          if status == bstack111l1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ๥"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack111l1l_opy_ (u"ࠫ࡮ࡴࡦࡰࠩ๦") if status == bstack111l1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ๧") else bstack111l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ๨")
          data = name + bstack111l1l_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩ๩") if status == bstack111l1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ๪") else name + bstack111l1l_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤࠬ๫") + reason
          bstack11l11l1lll_opy_ = bstack1ll1l1l1ll_opy_(bstack111l1l_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬ๬"), bstack111l1l_opy_ (u"ࠫࠬ๭"), bstack111l1l_opy_ (u"ࠬ࠭๮"), bstack111l1l_opy_ (u"࠭ࠧ๯"), level, data)
          for driver in bstack11llllll1_opy_:
            if bstack11lll11l1l_opy_ == driver.session_id:
              driver.execute_script(bstack11l11l1lll_opy_)
      except Exception as e:
        logger.debug(bstack111l1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ๰").format(str(e)))
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬ๱").format(str(e)))
  bstack1l11llllll_opy_(item, call, rep)
def bstack1l1ll111l1_opy_(driver, bstack11l1ll1l1_opy_, test=None):
  global bstack11111lll11_opy_
  if test != None:
    bstack1l11ll1l1_opy_ = getattr(test, bstack111l1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ๲"), None)
    bstack11l1ll11l_opy_ = getattr(test, bstack111l1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨ๳"), None)
    PercySDK.screenshot(driver, bstack11l1ll1l1_opy_, bstack1l11ll1l1_opy_=bstack1l11ll1l1_opy_, bstack11l1ll11l_opy_=bstack11l1ll11l_opy_, bstack1lll1ll1ll_opy_=bstack11111lll11_opy_)
  else:
    PercySDK.screenshot(driver, bstack11l1ll1l1_opy_)
@measure(event_name=EVENTS.bstack1111l1lll_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1lllll1111_opy_(driver):
  if bstack1llll11ll1_opy_.bstack11l111lll_opy_() is True or bstack1llll11ll1_opy_.capturing() is True:
    return
  bstack1llll11ll1_opy_.bstack1111l11ll1_opy_()
  while not bstack1llll11ll1_opy_.bstack11l111lll_opy_():
    bstack11lllll111_opy_ = bstack1llll11ll1_opy_.bstack11l1l1l1l_opy_()
    bstack1l1ll111l1_opy_(driver, bstack11lllll111_opy_)
  bstack1llll11ll1_opy_.bstack111l1lll11_opy_()
def bstack111ll1l1ll_opy_(sequence, driver_command, response = None, bstack11l11lll1_opy_ = None, args = None):
    try:
      if sequence != bstack111l1l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫ๴"):
        return
      if percy.bstack111llll1ll_opy_() == bstack111l1l_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦ๵"):
        return
      bstack11lllll111_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ๶"), None)
      for command in bstack11ll11111l_opy_:
        if command == driver_command:
          with bstack1ll1l111l_opy_:
            bstack1lllll1lll_opy_ = bstack11llllll1_opy_.copy()
          for driver in bstack1lllll1lll_opy_:
            bstack1lllll1111_opy_(driver)
      bstack1l1ll1llll_opy_ = percy.bstack1l1ll1lll1_opy_()
      if driver_command in bstack11l1lllll_opy_[bstack1l1ll1llll_opy_]:
        bstack1llll11ll1_opy_.bstack111l11lll1_opy_(bstack11lllll111_opy_, driver_command)
    except Exception as e:
      pass
def bstack1l111llll_opy_(framework_name):
  if bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ๷")):
      return
  bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬ๸"), True)
  global bstack1lll1ll11l_opy_
  global bstack11l1l1l11_opy_
  global bstack111ll1l111_opy_
  bstack1lll1ll11l_opy_ = framework_name
  logger.info(bstack11l11111l_opy_.format(bstack1lll1ll11l_opy_.split(bstack111l1l_opy_ (u"ࠩ࠰ࠫ๹"))[0]))
  bstack111111lll_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1l111l111l_opy_:
      Service.start = bstack11ll111l11_opy_
      Service.stop = bstack1lllll111l_opy_
      webdriver.Remote.get = bstack1ll1l1l1l_opy_
      WebDriver.quit = bstack1ll1l1l11l_opy_
      webdriver.Remote.__init__ = bstack1ll11ll11l_opy_
    if not bstack1l111l111l_opy_:
        webdriver.Remote.__init__ = bstack1l1l1ll1ll_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack1111llll1l_opy_
    bstack11l1l1l11_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1l111l111l_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack11l1l1lll_opy_
  except Exception as e:
    pass
  bstack1l111l11ll_opy_()
  if not bstack11l1l1l11_opy_:
    bstack1l11l1l1ll_opy_(bstack111l1l_opy_ (u"ࠥࡔࡦࡩ࡫ࡢࡩࡨࡷࠥࡴ࡯ࡵࠢ࡬ࡲࡸࡺࡡ࡭࡮ࡨࡨࠧ๺"), bstack111l1l11l_opy_)
  if bstack11l1l11ll1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack111l1l_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ๻")) and callable(getattr(RemoteConnection, bstack111l1l_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭๼"))):
        RemoteConnection._get_proxy_url = bstack11ll1lll1_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack11ll1lll1_opy_
    except Exception as e:
      logger.error(bstack1ll1l1ll11_opy_.format(str(e)))
  if bstack1l1l111ll_opy_():
    bstack1111lll11_opy_(CONFIG, logger)
  if (bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ๽") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack111llll1ll_opy_() == bstack111l1l_opy_ (u"ࠢࡵࡴࡸࡩࠧ๾"):
          bstack1ll1ll1l1l_opy_(bstack111ll1l1ll_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack111l111111_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l1111l11_opy_
      except Exception as e:
        logger.warn(bstack111l1ll111_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack111llll11_opy_
      except Exception as e:
        logger.debug(bstack111ll1111l_opy_ + str(e))
    except Exception as e:
      bstack1l11l1l1ll_opy_(e, bstack111l1ll111_opy_)
    Output.start_test = bstack111l1lllll_opy_
    Output.end_test = bstack1llllll1ll_opy_
    TestStatus.__init__ = bstack11llll1ll_opy_
    QueueItem.__init__ = bstack1llll11l11_opy_
    pabot._create_items = bstack1l1l1l111l_opy_
    try:
      from pabot import __version__ as bstack1ll11lllll_opy_
      if version.parse(bstack1ll11lllll_opy_) >= version.parse(bstack111l1l_opy_ (u"ࠨ࠷࠱࠴࠳࠶ࠧ๿")):
        pabot._run = bstack1llll1l1l1_opy_
      elif version.parse(bstack1ll11lllll_opy_) >= version.parse(bstack111l1l_opy_ (u"ࠩ࠷࠲࠷࠴࠰ࠨ຀")):
        pabot._run = bstack1l11ll11ll_opy_
      elif version.parse(bstack1ll11lllll_opy_) >= version.parse(bstack111l1l_opy_ (u"ࠪ࠶࠳࠷࠵࠯࠲ࠪກ")):
        pabot._run = bstack1l1l1l1l1l_opy_
      elif version.parse(bstack1ll11lllll_opy_) >= version.parse(bstack111l1l_opy_ (u"ࠫ࠷࠴࠱࠴࠰࠳ࠫຂ")):
        pabot._run = bstack1l11l1l1l1_opy_
      else:
        pabot._run = bstack1l1l11l1l1_opy_
    except Exception as e:
      pabot._run = bstack1l1l11l1l1_opy_
    pabot._create_command_for_execution = bstack11lll1ll11_opy_
    pabot._report_results = bstack111l1111ll_opy_
  if bstack111l1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ຃") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l11l1l1ll_opy_(e, bstack11l11lll1l_opy_)
    Runner.run_hook = bstack1l111l1ll1_opy_
    Step.run = bstack1l1ll11ll1_opy_
  if bstack111l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ຄ") in str(framework_name).lower():
    if not bstack1l111l111l_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack11l1ll1111_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack11ll111l1_opy_
      Config.getoption = bstack1l1l1111ll_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack111111ll1l_opy_
    except Exception as e:
      pass
def bstack11ll11ll1_opy_():
  global CONFIG
  if bstack111l1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ຅") in CONFIG and int(CONFIG[bstack111l1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨຆ")]) > 1:
    logger.warn(bstack1l1111l1ll_opy_)
def bstack1l11lll1l_opy_(arg, bstack111l111l_opy_, bstack1111111l1_opy_=None):
  global CONFIG
  global bstack1l111l11l1_opy_
  global bstack11ll1l11ll_opy_
  global bstack1l111l111l_opy_
  global bstack1lllll1l1_opy_
  bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩງ")
  if bstack111l111l_opy_ and isinstance(bstack111l111l_opy_, str):
    bstack111l111l_opy_ = eval(bstack111l111l_opy_)
  CONFIG = bstack111l111l_opy_[bstack111l1l_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪຈ")]
  bstack1l111l11l1_opy_ = bstack111l111l_opy_[bstack111l1l_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬຉ")]
  bstack11ll1l11ll_opy_ = bstack111l111l_opy_[bstack111l1l_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧຊ")]
  bstack1l111l111l_opy_ = bstack111l111l_opy_[bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩ຋")]
  bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨຌ"), bstack1l111l111l_opy_)
  os.environ[bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪຍ")] = bstack1l1lll11l1_opy_
  os.environ[bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠨຎ")] = json.dumps(CONFIG)
  os.environ[bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡋ࡙ࡇࡥࡕࡓࡎࠪຏ")] = bstack1l111l11l1_opy_
  os.environ[bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬຐ")] = str(bstack11ll1l11ll_opy_)
  os.environ[bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫຑ")] = str(True)
  if bstack1l1llll111_opy_(arg, [bstack111l1l_opy_ (u"࠭࠭࡯ࠩຒ"), bstack111l1l_opy_ (u"ࠧ࠮࠯ࡱࡹࡲࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨຓ")]) != -1:
    os.environ[bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡃࡕࡅࡑࡒࡅࡍࠩດ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack111ll1l1l1_opy_)
    return
  bstack1l11l1l11l_opy_()
  global bstack111llll111_opy_
  global bstack11111lll11_opy_
  global bstack1111l1111_opy_
  global bstack1ll1l11ll1_opy_
  global bstack111111l11_opy_
  global bstack111ll1l111_opy_
  global bstack1llllll1l1_opy_
  arg.append(bstack111l1l_opy_ (u"ࠤ࠰࡛ࠧຕ"))
  arg.append(bstack111l1l_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧ࠽ࡑࡴࡪࡵ࡭ࡧࠣࡥࡱࡸࡥࡢࡦࡼࠤ࡮ࡳࡰࡰࡴࡷࡩࡩࡀࡰࡺࡶࡨࡷࡹ࠴ࡐࡺࡶࡨࡷࡹ࡝ࡡࡳࡰ࡬ࡲ࡬ࠨຖ"))
  arg.append(bstack111l1l_opy_ (u"ࠦ࠲࡝ࠢທ"))
  arg.append(bstack111l1l_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩ࠿࡚ࡨࡦࠢ࡫ࡳࡴࡱࡩ࡮ࡲ࡯ࠦຘ"))
  global bstack1l111ll1l_opy_
  global bstack11lllll1l1_opy_
  global bstack11lll1l1l1_opy_
  global bstack1ll11l1l1l_opy_
  global bstack1ll1lllll1_opy_
  global bstack1l1llllll_opy_
  global bstack11ll11lll1_opy_
  global bstack111lll11l1_opy_
  global bstack1ll1111lll_opy_
  global bstack111l1ll1l1_opy_
  global bstack1l1llll11l_opy_
  global bstack111l111l11_opy_
  global bstack1l11llllll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l111ll1l_opy_ = webdriver.Remote.__init__
    bstack11lllll1l1_opy_ = WebDriver.quit
    bstack111lll11l1_opy_ = WebDriver.close
    bstack1ll1111lll_opy_ = WebDriver.get
    bstack11lll1l1l1_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack111ll1lll1_opy_(CONFIG) and bstack1ll11l11l1_opy_():
    if bstack1l11ll1lll_opy_() < version.parse(bstack1ll11ll1l1_opy_):
      logger.error(bstack1l111lll1l_opy_.format(bstack1l11ll1lll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack111l1l_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧນ")) and callable(getattr(RemoteConnection, bstack111l1l_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨບ"))):
          bstack111l1ll1l1_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack111l1ll1l1_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack1ll1l1ll11_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1l1llll11l_opy_ = Config.getoption
    from _pytest import runner
    bstack111l111l11_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1lll1ll1l_opy_)
  try:
    from pytest_bdd import reporting
    bstack1l11llllll_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack111l1l_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩປ"))
  bstack1111l1111_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ຜ"), {}).get(bstack111l1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬຝ"))
  bstack1llllll1l1_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack11111l1lll_opy_():
      bstack111l1111l1_opy_.invoke(Events.CONNECT, bstack11l1l1l11l_opy_())
    platform_index = int(os.environ.get(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫພ"), bstack111l1l_opy_ (u"ࠬ࠶ࠧຟ")))
  else:
    bstack1l111llll_opy_(bstack1lll1l1ll1_opy_)
  os.environ[bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧຠ")] = CONFIG[bstack111l1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩມ")]
  os.environ[bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫຢ")] = CONFIG[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬຣ")]
  os.environ[bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭຤")] = bstack1l111l111l_opy_.__str__()
  from _pytest.config import main as bstack111ll11ll1_opy_
  bstack1l1l1l11l_opy_ = []
  try:
    exit_code = bstack111ll11ll1_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1ll11l11l_opy_()
    if bstack111l1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨລ") in multiprocessing.current_process().__dict__.keys():
      for bstack1l1111111l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l1l1l11l_opy_.append(bstack1l1111111l_opy_)
    try:
      bstack1l1l11lll_opy_ = (bstack1l1l1l11l_opy_, int(exit_code))
      bstack1111111l1_opy_.append(bstack1l1l11lll_opy_)
    except:
      bstack1111111l1_opy_.append((bstack1l1l1l11l_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1l1l1l11l_opy_.append({bstack111l1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ຦"): bstack111l1l_opy_ (u"࠭ࡐࡳࡱࡦࡩࡸࡹࠠࠨວ") + os.environ.get(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧຨ")), bstack111l1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧຩ"): traceback.format_exc(), bstack111l1l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨສ"): int(os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪຫ")))})
    bstack1111111l1_opy_.append((bstack1l1l1l11l_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack111l1l_opy_ (u"ࠦࡷ࡫ࡴࡳ࡫ࡨࡷࠧຬ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack1l11111l1l_opy_ = e.__class__.__name__
    print(bstack111l1l_opy_ (u"ࠧࠫࡳ࠻ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡥࡩ࡭ࡧࡶࡦࠢࡷࡩࡸࡺࠠࠦࡵࠥອ") % (bstack1l11111l1l_opy_, e))
    return 1
def bstack11l1ll11ll_opy_(arg):
  global bstack11111l1l11_opy_
  bstack1l111llll_opy_(bstack11l11ll1ll_opy_)
  os.environ[bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧຮ")] = str(bstack11ll1l11ll_opy_)
  retries = bstack1llll1lll_opy_.bstack1111l111_opy_(CONFIG)
  status_code = 0
  if bstack1llll1lll_opy_.bstack1llll1l11_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack11111l1l1l_opy_
    status_code = bstack11111l1l1l_opy_(arg)
  if status_code != 0:
    bstack11111l1l11_opy_ = status_code
def bstack1l11l1ll1l_opy_():
  logger.info(bstack11l1llll11_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ຯ"), help=bstack111l1l_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡦࡳࡳ࡬ࡩࡨࠩະ"))
  parser.add_argument(bstack111l1l_opy_ (u"ࠩ࠰ࡹࠬັ"), bstack111l1l_opy_ (u"ࠪ࠱࠲ࡻࡳࡦࡴࡱࡥࡲ࡫ࠧາ"), help=bstack111l1l_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡷࡶࡩࡷࡴࡡ࡮ࡧࠪຳ"))
  parser.add_argument(bstack111l1l_opy_ (u"ࠬ࠳࡫ࠨິ"), bstack111l1l_opy_ (u"࠭࠭࠮࡭ࡨࡽࠬີ"), help=bstack111l1l_opy_ (u"࡚ࠧࡱࡸࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡦࡩࡣࡦࡵࡶࠤࡰ࡫ࡹࠨຶ"))
  parser.add_argument(bstack111l1l_opy_ (u"ࠨ࠯ࡩࠫື"), bstack111l1l_opy_ (u"ࠩ࠰࠱࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱຸࠧ"), help=bstack111l1l_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ູࠩ"))
  bstack11111l1l1_opy_ = parser.parse_args()
  try:
    bstack1l1l1llll_opy_ = bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡫ࡪࡴࡥࡳ࡫ࡦ࠲ࡾࡳ࡬࠯ࡵࡤࡱࡵࡲࡥࠨ຺")
    if bstack11111l1l1_opy_.framework and bstack11111l1l1_opy_.framework not in (bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬົ"), bstack111l1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧຼ")):
      bstack1l1l1llll_opy_ = bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭ຽ")
    bstack11ll11ll1l_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1l1llll_opy_)
    bstack1l1ll11l1l_opy_ = open(bstack11ll11ll1l_opy_, bstack111l1l_opy_ (u"ࠨࡴࠪ຾"))
    bstack11l11llll1_opy_ = bstack1l1ll11l1l_opy_.read()
    bstack1l1ll11l1l_opy_.close()
    if bstack11111l1l1_opy_.username:
      bstack11l11llll1_opy_ = bstack11l11llll1_opy_.replace(bstack111l1l_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩ຿"), bstack11111l1l1_opy_.username)
    if bstack11111l1l1_opy_.key:
      bstack11l11llll1_opy_ = bstack11l11llll1_opy_.replace(bstack111l1l_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬເ"), bstack11111l1l1_opy_.key)
    if bstack11111l1l1_opy_.framework:
      bstack11l11llll1_opy_ = bstack11l11llll1_opy_.replace(bstack111l1l_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬແ"), bstack11111l1l1_opy_.framework)
    file_name = bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨໂ")
    file_path = os.path.abspath(file_name)
    bstack1l1ll1l1l1_opy_ = open(file_path, bstack111l1l_opy_ (u"࠭ࡷࠨໃ"))
    bstack1l1ll1l1l1_opy_.write(bstack11l11llll1_opy_)
    bstack1l1ll1l1l1_opy_.close()
    logger.info(bstack1l1l111l1_opy_)
    try:
      os.environ[bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩໄ")] = bstack11111l1l1_opy_.framework if bstack11111l1l1_opy_.framework != None else bstack111l1l_opy_ (u"ࠣࠤ໅")
      config = yaml.safe_load(bstack11l11llll1_opy_)
      config[bstack111l1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩໆ")] = bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠰ࡷࡪࡺࡵࡱࠩ໇")
      bstack11lllllll1_opy_(bstack11l1ll1ll_opy_, config)
    except Exception as e:
      logger.debug(bstack111111111_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1l1111lll_opy_.format(str(e)))
def bstack11lllllll1_opy_(bstack1111l11ll_opy_, config, bstack1l1ll1l11_opy_={}):
  global bstack1l111l111l_opy_
  global bstack111lll1l1l_opy_
  global bstack1lllll1l1_opy_
  if not config:
    return
  bstack11ll1l1l1l_opy_ = bstack1l1ll1ll11_opy_ if not bstack1l111l111l_opy_ else (
    bstack1ll1ll1ll1_opy_ if bstack111l1l_opy_ (u"ࠫࡦࡶࡰࠨ່") in config else (
        bstack11ll1l11l1_opy_ if config.get(bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦ້ࠩ")) else bstack11l1lll1l1_opy_
    )
)
  bstack11lll1lll_opy_ = False
  bstack11111l111l_opy_ = False
  if bstack1l111l111l_opy_ is True:
      if bstack111l1l_opy_ (u"࠭ࡡࡱࡲ໊ࠪ") in config:
          bstack11lll1lll_opy_ = True
      else:
          bstack11111l111l_opy_ = True
  bstack11llll11l1_opy_ = bstack11lll111l1_opy_.bstack11lll11l1_opy_(config, bstack111lll1l1l_opy_)
  bstack11l11ll111_opy_ = bstack1lll1l1l11_opy_()
  data = {
    bstack111l1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦ໋ࠩ"): config[bstack111l1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ໌")],
    bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬໍ"): config[bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭໎")],
    bstack111l1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ໏"): bstack1111l11ll_opy_,
    bstack111l1l_opy_ (u"ࠬࡪࡥࡵࡧࡦࡸࡪࡪࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ໐"): os.environ.get(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ໑"), bstack111lll1l1l_opy_),
    bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ໒"): bstack111l11l1l1_opy_,
    bstack111l1l_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮ࠪ໓"): bstack11l111ll1l_opy_(),
    bstack111l1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໔"): {
      bstack111l1l_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ໕"): str(config[bstack111l1l_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ໖")]) if bstack111l1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ໗") in config else bstack111l1l_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢ໘"),
      bstack111l1l_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࡘࡨࡶࡸ࡯࡯࡯ࠩ໙"): sys.version,
      bstack111l1l_opy_ (u"ࠨࡴࡨࡪࡪࡸࡲࡦࡴࠪ໚"): bstack111ll11lll_opy_(os.environ.get(bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ໛"), bstack111lll1l1l_opy_)),
      bstack111l1l_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬໜ"): bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫໝ"),
      bstack111l1l_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭ໞ"): bstack11ll1l1l1l_opy_,
      bstack111l1l_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫໟ"): bstack11llll11l1_opy_,
      bstack111l1l_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡠࡷࡸ࡭ࡩ࠭໠"): os.environ[bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭໡")],
      bstack111l1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ໢"): os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ໣"), bstack111lll1l1l_opy_),
      bstack111l1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ໤"): bstack1111ll1l11_opy_(os.environ.get(bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ໥"), bstack111lll1l1l_opy_)),
      bstack111l1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ໦"): bstack11l11ll111_opy_.get(bstack111l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ໧")),
      bstack111l1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ໨"): bstack11l11ll111_opy_.get(bstack111l1l_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ໩")),
      bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໪"): config[bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ໫")] if config[bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ໬")] else bstack111l1l_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢ໭"),
      bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ໮"): str(config[bstack111l1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໯")]) if bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ໰") in config else bstack111l1l_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦ໱"),
      bstack111l1l_opy_ (u"ࠫࡴࡹࠧ໲"): sys.platform,
      bstack111l1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧ໳"): socket.gethostname(),
      bstack111l1l_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ໴"): bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ໵"))
    }
  }
  if not bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ໶")) is None:
    data[bstack111l1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໷")][bstack111l1l_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡒ࡫ࡴࡢࡦࡤࡸࡦ࠭໸")] = {
      bstack111l1l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ໹"): bstack111l1l_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪ໺"),
      bstack111l1l_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭໻"): bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ໼")),
      bstack111l1l_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࡏࡷࡰࡦࡪࡸࠧ໽"): bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡑࡳࠬ໾"))
    }
  if bstack1111l11ll_opy_ == bstack1l1l11llll_opy_:
    data[bstack111l1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໿")][bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡆࡳࡳ࡬ࡩࡨࠩༀ")] = bstack11111ll1l_opy_(config)
    data[bstack111l1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ༁")][bstack111l1l_opy_ (u"࠭ࡩࡴࡒࡨࡶࡨࡿࡁࡶࡶࡲࡉࡳࡧࡢ࡭ࡧࡧࠫ༂")] = percy.bstack11lll1l1l_opy_
    data[bstack111l1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ༃")][bstack111l1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࡂࡶ࡫࡯ࡨࡎࡪࠧ༄")] = percy.percy_build_id
  if not bstack1llll1lll_opy_.bstack1l1l11111l_opy_(CONFIG):
    data[bstack111l1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ༅")][bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠧ༆")] = bstack1llll1lll_opy_.bstack1l1l11111l_opy_(CONFIG)
  bstack1111l1ll_opy_ = bstack111111ll_opy_.bstack1111ll1l_opy_(CONFIG, logger)
  bstack1lll1llll_opy_ = bstack1llll1lll_opy_.bstack1111ll1l_opy_(config=CONFIG)
  if bstack1111l1ll_opy_ is not None and bstack1lll1llll_opy_ is not None and bstack1lll1llll_opy_.bstack11111l1l_opy_():
    data[bstack111l1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ༇")][bstack1lll1llll_opy_.bstack11ll111ll_opy_()] = bstack1111l1ll_opy_.bstack1l111ll11_opy_()
  update(data[bstack111l1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ༈")], bstack1l1ll1l11_opy_)
  try:
    response = bstack11llll111_opy_(bstack111l1l_opy_ (u"࠭ࡐࡐࡕࡗࠫ༉"), bstack1l1lll1ll_opy_(bstack11l1ll111_opy_), data, {
      bstack111l1l_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ༊"): (config[bstack111l1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ་")], config[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ༌")])
    })
    if response:
      logger.debug(bstack1l11ll111l_opy_.format(bstack1111l11ll_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11lllllll_opy_.format(str(e)))
def bstack111ll11lll_opy_(framework):
  return bstack111l1l_opy_ (u"ࠥࡿࢂ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࢀࢃࠢ།").format(str(framework), __version__) if framework else bstack111l1l_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧ༎").format(
    __version__)
def bstack1l11l1l11l_opy_():
  global CONFIG
  global bstack1ll1ll11l1_opy_
  if bool(CONFIG):
    return
  try:
    bstack1lll1ll111_opy_()
    logger.debug(bstack111l11ll1l_opy_.format(str(CONFIG)))
    bstack1ll1ll11l1_opy_ = bstack1l11l1lll_opy_.configure_logger(CONFIG, bstack1ll1ll11l1_opy_)
    bstack111111lll_opy_()
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࠤ༏") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1llll1lll1_opy_
  atexit.register(bstack1111l1111l_opy_)
  signal.signal(signal.SIGINT, bstack1l11l1ll11_opy_)
  signal.signal(signal.SIGTERM, bstack1l11l1ll11_opy_)
def bstack1llll1lll1_opy_(exctype, value, traceback):
  global bstack11llllll1_opy_
  try:
    for driver in bstack11llllll1_opy_:
      bstack11ll1111l1_opy_(driver, bstack111l1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭༐"), bstack111l1l_opy_ (u"ࠢࡔࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥ༑") + str(value))
  except Exception:
    pass
  logger.info(bstack11l1l1111_opy_)
  bstack1l1ll11111_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l1ll11111_opy_(message=bstack111l1l_opy_ (u"ࠨࠩ༒"), bstack111l1llll1_opy_ = False):
  global CONFIG
  bstack1ll11111l1_opy_ = bstack111l1l_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡇࡻࡧࡪࡶࡴࡪࡱࡱࠫ༓") if bstack111l1llll1_opy_ else bstack111l1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ༔")
  try:
    if message:
      bstack1l1ll1l11_opy_ = {
        bstack1ll11111l1_opy_ : str(message)
      }
      bstack11lllllll1_opy_(bstack1l1l11llll_opy_, CONFIG, bstack1l1ll1l11_opy_)
    else:
      bstack11lllllll1_opy_(bstack1l1l11llll_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1l11l11lll_opy_.format(str(e)))
def bstack11ll1l11l_opy_(bstack1l11ll11l_opy_, size):
  bstack1l1l11lll1_opy_ = []
  while len(bstack1l11ll11l_opy_) > size:
    bstack111l11111l_opy_ = bstack1l11ll11l_opy_[:size]
    bstack1l1l11lll1_opy_.append(bstack111l11111l_opy_)
    bstack1l11ll11l_opy_ = bstack1l11ll11l_opy_[size:]
  bstack1l1l11lll1_opy_.append(bstack1l11ll11l_opy_)
  return bstack1l1l11lll1_opy_
def bstack1ll11l1l11_opy_(args):
  if bstack111l1l_opy_ (u"ࠫ࠲ࡳࠧ༕") in args and bstack111l1l_opy_ (u"ࠬࡶࡤࡣࠩ༖") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack111l1ll1ll_opy_, stage=STAGE.bstack11ll1l111l_opy_)
def run_on_browserstack(bstack11lll11lll_opy_=None, bstack1111111l1_opy_=None, bstack11lll1l1ll_opy_=False):
  global CONFIG
  global bstack1l111l11l1_opy_
  global bstack11ll1l11ll_opy_
  global bstack111lll1l1l_opy_
  global bstack1lllll1l1_opy_
  bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"࠭ࠧ༗")
  bstack11ll1lll11_opy_(bstack111l11111_opy_, logger)
  if bstack11lll11lll_opy_ and isinstance(bstack11lll11lll_opy_, str):
    bstack11lll11lll_opy_ = eval(bstack11lll11lll_opy_)
  if bstack11lll11lll_opy_:
    CONFIG = bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍ༘ࠧ")]
    bstack1l111l11l1_opy_ = bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍ༙ࠩ")]
    bstack11ll1l11ll_opy_ = bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ༚")]
    bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ༛"), bstack11ll1l11ll_opy_)
    bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༜")
  bstack1lllll1l1_opy_.set_property(bstack111l1l_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ༝"), uuid4().__str__())
  logger.info(bstack111l1l_opy_ (u"࠭ࡓࡅࡍࠣࡶࡺࡴࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡩࡥ࠼ࠣࠫ༞") + bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ༟")));
  logger.debug(bstack111l1l_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࡀࠫ༠") + bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ༡")))
  if not bstack11lll1l1ll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack111ll1l1l1_opy_)
      return
    if sys.argv[1] == bstack111l1l_opy_ (u"ࠪ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ࠭༢") or sys.argv[1] == bstack111l1l_opy_ (u"ࠫ࠲ࡼࠧ༣"):
      logger.info(bstack111l1l_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡕࡿࡴࡩࡱࡱࠤࡘࡊࡋࠡࡸࡾࢁࠬ༤").format(__version__))
      return
    if sys.argv[1] == bstack111l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ༥"):
      bstack1l11l1ll1l_opy_()
      return
  args = sys.argv
  bstack1l11l1l11l_opy_()
  global bstack111llll111_opy_
  global bstack1ll11llll_opy_
  global bstack1llllll1l1_opy_
  global bstack1111l1l11_opy_
  global bstack11111lll11_opy_
  global bstack1111l1111_opy_
  global bstack1ll1l11ll1_opy_
  global bstack1ll1111111_opy_
  global bstack111111l11_opy_
  global bstack111ll1l111_opy_
  global bstack1lll11ll11_opy_
  bstack1ll11llll_opy_ = len(CONFIG.get(bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ༦"), []))
  if not bstack1l1lll11l1_opy_:
    if args[1] == bstack111l1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ༧") or args[1] == bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ༨"):
      bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༩")
      args = args[2:]
    elif args[1] == bstack111l1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༪"):
      bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༫")
      args = args[2:]
    elif args[1] == bstack111l1l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ༬"):
      bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭༭")
      args = args[2:]
    elif args[1] == bstack111l1l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ༮"):
      bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ༯")
      args = args[2:]
    elif args[1] == bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ༰"):
      bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༱")
      args = args[2:]
    elif args[1] == bstack111l1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ༲"):
      bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭༳")
      args = args[2:]
    else:
      if not bstack111l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༴") in CONFIG or str(CONFIG[bstack111l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮༵ࠫ")]).lower() in [bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༶"), bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶༷ࠫ")]:
        bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༸")
        args = args[1:]
      elif str(CONFIG[bstack111l1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ༹")]).lower() == bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ༺"):
        bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭༻")
        args = args[1:]
      elif str(CONFIG[bstack111l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ༼")]).lower() == bstack111l1l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༽"):
        bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ༾")
        args = args[1:]
      elif str(CONFIG[bstack111l1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ༿")]).lower() == bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཀ"):
        bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ཁ")
        args = args[1:]
      elif str(CONFIG[bstack111l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪག")]).lower() == bstack111l1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨགྷ"):
        bstack1l1lll11l1_opy_ = bstack111l1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩང")
        args = args[1:]
      else:
        os.environ[bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬཅ")] = bstack1l1lll11l1_opy_
        bstack11l111l1l1_opy_(bstack11lllll1l_opy_)
  os.environ[bstack111l1l_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬཆ")] = bstack1l1lll11l1_opy_
  bstack111lll1l1l_opy_ = bstack1l1lll11l1_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack111lllllll_opy_ = bstack1l1l11111_opy_[bstack111l1l_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘ࠲ࡈࡄࡅࠩཇ")] if bstack1l1lll11l1_opy_ == bstack111l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭཈") and bstack111ll1llll_opy_() else bstack1l1lll11l1_opy_
      bstack111l1111l1_opy_.invoke(Events.bstack1l1llll1l1_opy_, bstack111l11l1l_opy_(
        sdk_version=__version__,
        path_config=bstack1ll1l1l1l1_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack111lllllll_opy_,
        frameworks=[bstack111lllllll_opy_],
        framework_versions={
          bstack111lllllll_opy_: bstack1111ll1l11_opy_(bstack111l1l_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭ཉ") if bstack1l1lll11l1_opy_ in [bstack111l1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧཊ"), bstack111l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨཋ"), bstack111l1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫཌ")] else bstack1l1lll11l1_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack111l1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨཌྷ"), None):
        CONFIG[bstack111l1l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢཎ")] = cli.config.get(bstack111l1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣཏ"), None)
    except Exception as e:
      bstack111l1111l1_opy_.invoke(Events.bstack11l11l111l_opy_, e.__traceback__, 1)
    if bstack11ll1l11ll_opy_:
      CONFIG[bstack111l1l_opy_ (u"ࠢࡢࡲࡳࠦཐ")] = cli.config[bstack111l1l_opy_ (u"ࠣࡣࡳࡴࠧད")]
      logger.info(bstack11l1l1ll1_opy_.format(CONFIG[bstack111l1l_opy_ (u"ࠩࡤࡴࡵ࠭དྷ")]))
  else:
    bstack111l1111l1_opy_.clear()
  global bstack11llllll11_opy_
  global bstack11ll11l111_opy_
  if bstack11lll11lll_opy_:
    try:
      bstack1l1ll111ll_opy_ = datetime.datetime.now()
      os.environ[bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬན")] = bstack1l1lll11l1_opy_
      bstack11lllllll1_opy_(bstack11llll1l1_opy_, CONFIG)
      cli.bstack1l1l111ll1_opy_(bstack111l1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡶࡨࡰࡥࡴࡦࡵࡷࡣࡦࡺࡴࡦ࡯ࡳࡸࡪࡪࠢཔ"), datetime.datetime.now() - bstack1l1ll111ll_opy_)
    except Exception as e:
      logger.debug(bstack1111l1ll1_opy_.format(str(e)))
  global bstack1l111ll1l_opy_
  global bstack11lllll1l1_opy_
  global bstack1lllllll11_opy_
  global bstack11l1111l1_opy_
  global bstack111l1l111l_opy_
  global bstack11l1111111_opy_
  global bstack1ll11l1l1l_opy_
  global bstack1ll1lllll1_opy_
  global bstack1l11lll11l_opy_
  global bstack1l1llllll_opy_
  global bstack11ll11lll1_opy_
  global bstack111lll11l1_opy_
  global bstack11ll1ll111_opy_
  global bstack1l111l111_opy_
  global bstack1ll1111lll_opy_
  global bstack111l1ll1l1_opy_
  global bstack1l1llll11l_opy_
  global bstack111l111l11_opy_
  global bstack11ll1lll1l_opy_
  global bstack1l11llllll_opy_
  global bstack11lll1l1l1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l111ll1l_opy_ = webdriver.Remote.__init__
    bstack11lllll1l1_opy_ = WebDriver.quit
    bstack111lll11l1_opy_ = WebDriver.close
    bstack1ll1111lll_opy_ = WebDriver.get
    bstack11lll1l1l1_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack11llllll11_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack11lll1llll_opy_
    bstack11ll11l111_opy_ = bstack11lll1llll_opy_()
  except Exception as e:
    pass
  try:
    global bstack1llll1ll11_opy_
    from QWeb.keywords import browser
    bstack1llll1ll11_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack111ll1lll1_opy_(CONFIG) and bstack1ll11l11l1_opy_():
    if bstack1l11ll1lll_opy_() < version.parse(bstack1ll11ll1l1_opy_):
      logger.error(bstack1l111lll1l_opy_.format(bstack1l11ll1lll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack111l1l_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ཕ")) and callable(getattr(RemoteConnection, bstack111l1l_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧབ"))):
          RemoteConnection._get_proxy_url = bstack11ll1lll1_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack11ll1lll1_opy_
      except Exception as e:
        logger.error(bstack1ll1l1ll11_opy_.format(str(e)))
  if not CONFIG.get(bstack111l1l_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩབྷ"), False) and not bstack11lll11lll_opy_:
    logger.info(bstack1ll11l1111_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack111l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬམ") in CONFIG and str(CONFIG[bstack111l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ཙ")]).lower() != bstack111l1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩཚ"):
      bstack1l111l11l_opy_()
    elif bstack1l1lll11l1_opy_ != bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫཛ") or (bstack1l1lll11l1_opy_ == bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬཛྷ") and not bstack11lll11lll_opy_):
      bstack1lll1lllll_opy_()
  if (bstack1l1lll11l1_opy_ in [bstack111l1l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬཝ"), bstack111l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ཞ"), bstack111l1l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩཟ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack111l111111_opy_
        bstack11l1111111_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack111l1ll111_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack111l1l111l_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack111ll1111l_opy_ + str(e))
    except Exception as e:
      bstack1l11l1l1ll_opy_(e, bstack111l1ll111_opy_)
    if bstack1l1lll11l1_opy_ != bstack111l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪའ"):
      bstack11l111l1ll_opy_()
    bstack1lllllll11_opy_ = Output.start_test
    bstack11l1111l1_opy_ = Output.end_test
    bstack1ll11l1l1l_opy_ = TestStatus.__init__
    bstack1l11lll11l_opy_ = pabot._run
    bstack1l1llllll_opy_ = QueueItem.__init__
    bstack11ll11lll1_opy_ = pabot._create_command_for_execution
    bstack11ll1lll1l_opy_ = pabot._report_results
  if bstack1l1lll11l1_opy_ == bstack111l1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪཡ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l11l1l1ll_opy_(e, bstack11l11lll1l_opy_)
    bstack11ll1ll111_opy_ = Runner.run_hook
    bstack1l111l111_opy_ = Step.run
  if bstack1l1lll11l1_opy_ == bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫར"):
    try:
      from _pytest.config import Config
      bstack1l1llll11l_opy_ = Config.getoption
      from _pytest import runner
      bstack111l111l11_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1lll1ll1l_opy_)
    try:
      from pytest_bdd import reporting
      bstack1l11llllll_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡴࠦࡲࡶࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࡸ࠭ལ"))
  try:
    framework_name = bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬཤ") if bstack1l1lll11l1_opy_ in [bstack111l1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ཥ"), bstack111l1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧས"), bstack111l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪཧ")] else bstack1ll1ll1lll_opy_(bstack1l1lll11l1_opy_)
    bstack1l11l11l1l_opy_ = {
      bstack111l1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࠫཨ"): bstack111l1l_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭ཀྵ") if bstack1l1lll11l1_opy_ == bstack111l1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཪ") and bstack111ll1llll_opy_() else framework_name,
      bstack111l1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪཫ"): bstack1111ll1l11_opy_(framework_name),
      bstack111l1l_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬཬ"): __version__,
      bstack111l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩ཭"): bstack1l1lll11l1_opy_
    }
    if bstack1l1lll11l1_opy_ in bstack1l11l1llll_opy_ + bstack1llll111ll_opy_:
      if bstack1lll11ll1_opy_.bstack1l1lllll1l_opy_(CONFIG):
        if bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ཮") in CONFIG:
          os.environ[bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ཯")] = os.getenv(bstack111l1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ཰"), json.dumps(CONFIG[bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷཱࠬ")]))
          CONFIG[bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸི࠭")].pop(bstack111l1l_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩཱིࠬ"), None)
          CONFIG[bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨུ")].pop(bstack111l1l_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ཱུࠧ"), None)
        bstack1l11l11l1l_opy_[bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪྲྀ")] = {
          bstack111l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩཷ"): bstack111l1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧླྀ"),
          bstack111l1l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧཹ"): str(bstack1l11ll1lll_opy_())
        }
    if bstack1l1lll11l1_opy_ not in [bstack111l1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨེ")] and not cli.is_running():
      bstack11ll1l1ll_opy_, bstack111ll1ll11_opy_ = bstack1l1l1111_opy_.launch(CONFIG, bstack1l11l11l1l_opy_)
      if bstack111ll1ll11_opy_.get(bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨཻ")) is not None and bstack1lll11ll1_opy_.bstack11ll1l1ll1_opy_(CONFIG) is None:
        value = bstack111ll1ll11_opy_[bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺོࠩ")].get(bstack111l1l_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶཽࠫ"))
        if value is not None:
            CONFIG[bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫཾ")] = value
        else:
          logger.debug(bstack111l1l_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡦࡤࡸࡦࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥཿ"))
  except Exception as e:
    logger.debug(bstack1111l11l11_opy_.format(bstack111l1l_opy_ (u"࠭ࡔࡦࡵࡷࡌࡺࡨྀࠧ"), str(e)))
  if bstack1l1lll11l1_opy_ == bstack111l1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴཱྀࠧ"):
    bstack1llllll1l1_opy_ = True
    if bstack11lll11lll_opy_ and bstack11lll1l1ll_opy_:
      bstack1111l1111_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬྂ"), {}).get(bstack111l1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫྃ"))
      bstack1l111llll_opy_(bstack1l11l111ll_opy_)
    elif bstack11lll11lll_opy_:
      bstack1111l1111_opy_ = CONFIG.get(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹ྄ࠧ"), {}).get(bstack111l1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭྅"))
      global bstack11llllll1_opy_
      try:
        if bstack1ll11l1l11_opy_(bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ྆")]) and multiprocessing.current_process().name == bstack111l1l_opy_ (u"࠭࠰ࠨ྇"):
          bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྈ")].remove(bstack111l1l_opy_ (u"ࠨ࠯ࡰࠫྉ"))
          bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྊ")].remove(bstack111l1l_opy_ (u"ࠪࡴࡩࡨࠧྋ"))
          bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྌ")] = bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྍ")][0]
          with open(bstack11lll11lll_opy_[bstack111l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྎ")], bstack111l1l_opy_ (u"ࠧࡳࠩྏ")) as f:
            file_content = f.read()
          bstack1ll1ll1111_opy_ = bstack111l1l_opy_ (u"ࠣࠤࠥࡪࡷࡵ࡭ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡦ࡮ࠤ࡮ࡳࡰࡰࡴࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫࠻ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨࠬࢀࢃࠩ࠼ࠢࡩࡶࡴࡳࠠࡱࡦࡥࠤ࡮ࡳࡰࡰࡴࡷࠤࡕࡪࡢ࠼ࠢࡲ࡫ࡤࡪࡢࠡ࠿ࠣࡔࡩࡨ࠮ࡥࡱࡢࡦࡷ࡫ࡡ࡬࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡤࡦࡨࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰ࠮ࡳࡦ࡮ࡩ࠰ࠥࡧࡲࡨ࠮ࠣࡸࡪࡳࡰࡰࡴࡤࡶࡾࠦ࠽ࠡ࠲ࠬ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡸࡷࡿ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡣࡵ࡫ࠥࡃࠠࡴࡶࡵࠬ࡮ࡴࡴࠩࡣࡵ࡫࠮࠱࠱࠱ࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡧࡻࡧࡪࡶࡴࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡦࡹࠠࡦ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡴࡦࡹࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡯ࡨࡡࡧࡦ࠭ࡹࡥ࡭ࡨ࠯ࡥࡷ࡭ࠬࡵࡧࡰࡴࡴࡸࡡࡳࡻࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡑࡦࡥ࠲ࡩࡵ࡟ࡣࠢࡀࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡔࡩࡨ࠮ࡥࡱࡢࡦࡷ࡫ࡡ࡬ࠢࡀࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡔࡩࡨࠨࠪ࠰ࡶࡩࡹࡥࡴࡳࡣࡦࡩ࠭࠯࡜࡯ࠤࠥࠦྐ").format(str(bstack11lll11lll_opy_))
          bstack111l11l11_opy_ = bstack1ll1ll1111_opy_ + file_content
          bstack1lll1ll1l1_opy_ = bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྑ")] + bstack111l1l_opy_ (u"ࠪࡣࡧࡹࡴࡢࡥ࡮ࡣࡹ࡫࡭ࡱ࠰ࡳࡽࠬྒ")
          with open(bstack1lll1ll1l1_opy_, bstack111l1l_opy_ (u"ࠫࡼ࠭ྒྷ")):
            pass
          with open(bstack1lll1ll1l1_opy_, bstack111l1l_opy_ (u"ࠧࡽࠫࠣྔ")) as f:
            f.write(bstack111l11l11_opy_)
          import subprocess
          process_data = subprocess.run([bstack111l1l_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࠨྕ"), bstack1lll1ll1l1_opy_])
          if os.path.exists(bstack1lll1ll1l1_opy_):
            os.unlink(bstack1lll1ll1l1_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack1ll11l1l11_opy_(bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྖ")]):
            bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྗ")].remove(bstack111l1l_opy_ (u"ࠩ࠰ࡱࠬ྘"))
            bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྙ")].remove(bstack111l1l_opy_ (u"ࠫࡵࡪࡢࠨྚ"))
            bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྛ")] = bstack11lll11lll_opy_[bstack111l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྜ")][0]
          bstack1l111llll_opy_(bstack1l11l111ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྜྷ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack111l1l_opy_ (u"ࠨࡡࡢࡲࡦࡳࡥࡠࡡࠪྞ")] = bstack111l1l_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫྟ")
          mod_globals[bstack111l1l_opy_ (u"ࠪࡣࡤ࡬ࡩ࡭ࡧࡢࡣࠬྠ")] = os.path.abspath(bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྡ")])
          exec(open(bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྡྷ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack111l1l_opy_ (u"࠭ࡃࡢࡷࡪ࡬ࡹࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂ࠭ྣ").format(str(e)))
          for driver in bstack11llllll1_opy_:
            bstack1111111l1_opy_.append({
              bstack111l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬྤ"): bstack11lll11lll_opy_[bstack111l1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྥ")],
              bstack111l1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨྦ"): str(e),
              bstack111l1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩྦྷ"): multiprocessing.current_process().name
            })
            bstack11ll1111l1_opy_(driver, bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫྨ"), bstack111l1l_opy_ (u"࡙ࠧࡥࡴࡵ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣྩ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack11llllll1_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11ll1l11ll_opy_, CONFIG, logger)
      bstack1llllll111_opy_()
      bstack11ll11ll1_opy_()
      percy.bstack1ll1l1ll1_opy_()
      bstack111l111l_opy_ = {
        bstack111l1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྪ"): args[0],
        bstack111l1l_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧྫ"): CONFIG,
        bstack111l1l_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩྫྷ"): bstack1l111l11l1_opy_,
        bstack111l1l_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫྭ"): bstack11ll1l11ll_opy_
      }
      if bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྮ") in CONFIG:
        bstack1ll1ll1ll_opy_ = bstack1l11llll1l_opy_(args, logger, CONFIG, bstack1l111l111l_opy_, bstack1ll11llll_opy_)
        bstack1ll1111111_opy_ = bstack1ll1ll1ll_opy_.bstack1lllllll1_opy_(run_on_browserstack, bstack111l111l_opy_, bstack1ll11l1l11_opy_(args))
      else:
        if bstack1ll11l1l11_opy_(args):
          bstack111l111l_opy_[bstack111l1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྯ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack111l111l_opy_,))
          test.start()
          test.join()
        else:
          bstack1l111llll_opy_(bstack1l11l111ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack111l1l_opy_ (u"ࠬࡥ࡟࡯ࡣࡰࡩࡤࡥࠧྰ")] = bstack111l1l_opy_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨྱ")
          mod_globals[bstack111l1l_opy_ (u"ࠧࡠࡡࡩ࡭ࡱ࡫࡟ࡠࠩྲ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1l1lll11l1_opy_ == bstack111l1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧླ") or bstack1l1lll11l1_opy_ == bstack111l1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨྴ"):
    percy.init(bstack11ll1l11ll_opy_, CONFIG, logger)
    percy.bstack1ll1l1ll1_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l11l1l1ll_opy_(e, bstack111l1ll111_opy_)
    bstack1llllll111_opy_()
    bstack1l111llll_opy_(bstack1ll1llll1l_opy_)
    if bstack1l111l111l_opy_:
      bstack1ll11lll1_opy_(bstack1ll1llll1l_opy_, args)
      if bstack111l1l_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨྵ") in args:
        i = args.index(bstack111l1l_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩྶ"))
        args.pop(i)
        args.pop(i)
      if bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨྷ") not in CONFIG:
        CONFIG[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩྸ")] = [{}]
        bstack1ll11llll_opy_ = 1
      if bstack111llll111_opy_ == 0:
        bstack111llll111_opy_ = 1
      args.insert(0, str(bstack111llll111_opy_))
      args.insert(0, str(bstack111l1l_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬྐྵ")))
    if bstack1l1l1111_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack11l11llll_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack11l1ll111l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack111l1l_opy_ (u"ࠣࡔࡒࡆࡔ࡚࡟ࡐࡒࡗࡍࡔࡔࡓࠣྺ"),
        ).parse_args(bstack11l11llll_opy_)
        bstack1ll1l1llll_opy_ = args.index(bstack11l11llll_opy_[0]) if len(bstack11l11llll_opy_) > 0 else len(args)
        args.insert(bstack1ll1l1llll_opy_, str(bstack111l1l_opy_ (u"ࠩ࠰࠱ࡱ࡯ࡳࡵࡧࡱࡩࡷ࠭ྻ")))
        args.insert(bstack1ll1l1llll_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111l1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡶࡴࡨ࡯ࡵࡡ࡯࡭ࡸࡺࡥ࡯ࡧࡵ࠲ࡵࡿࠧྼ"))))
        if bstack1llll1lll_opy_.bstack1llll1l11_opy_(CONFIG):
          args.insert(bstack1ll1l1llll_opy_, str(bstack111l1l_opy_ (u"ࠫ࠲࠳࡬ࡪࡵࡷࡩࡳ࡫ࡲࠨ྽")))
          args.insert(bstack1ll1l1llll_opy_ + 1, str(bstack111l1l_opy_ (u"ࠬࡘࡥࡵࡴࡼࡊࡦ࡯࡬ࡦࡦ࠽ࡿࢂ࠭྾").format(bstack1llll1lll_opy_.bstack1111l111_opy_(CONFIG))))
        if bstack11l1llll1_opy_(os.environ.get(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠫ྿"))) and str(os.environ.get(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠫ࿀"), bstack111l1l_opy_ (u"ࠨࡰࡸࡰࡱ࠭࿁"))) != bstack111l1l_opy_ (u"ࠩࡱࡹࡱࡲࠧ࿂"):
          for bstack1lllll11l1_opy_ in bstack11l1ll111l_opy_:
            args.remove(bstack1lllll11l1_opy_)
          test_files = os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧ࿃")).split(bstack111l1l_opy_ (u"ࠫ࠱࠭࿄"))
          for bstack111l111lll_opy_ in test_files:
            args.append(bstack111l111lll_opy_)
      except Exception as e:
        logger.error(bstack111l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡥࡹࡺࡡࡤࡪ࡬ࡲ࡬ࠦ࡬ࡪࡵࡷࡩࡳ࡫ࡲࠡࡨࡲࡶࠥࢁࡽ࠯ࠢࡈࡶࡷࡵࡲࠡ࠯ࠣࡿࢂࠨ࿅").format(bstack1111lll1l1_opy_, e))
    pabot.main(args)
  elif bstack1l1lll11l1_opy_ == bstack111l1l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲ࿆ࠧ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l11l1l1ll_opy_(e, bstack111l1ll111_opy_)
    for a in args:
      if bstack111l1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭࿇") in a:
        bstack11111lll11_opy_ = int(a.split(bstack111l1l_opy_ (u"ࠨ࠼ࠪ࿈"))[1])
      if bstack111l1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭࿉") in a:
        bstack1111l1111_opy_ = str(a.split(bstack111l1l_opy_ (u"ࠪ࠾ࠬ࿊"))[1])
      if bstack111l1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫ࿋") in a:
        bstack1ll1l11ll1_opy_ = str(a.split(bstack111l1l_opy_ (u"ࠬࡀࠧ࿌"))[1])
    bstack1llllllll1_opy_ = None
    if bstack111l1l_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬ࿍") in args:
      i = args.index(bstack111l1l_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭࿎"))
      args.pop(i)
      bstack1llllllll1_opy_ = args.pop(i)
    if bstack1llllllll1_opy_ is not None:
      global bstack1l1111ll1_opy_
      bstack1l1111ll1_opy_ = bstack1llllllll1_opy_
    bstack1l111llll_opy_(bstack1ll1llll1l_opy_)
    run_cli(args)
    if bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬ࿏") in multiprocessing.current_process().__dict__.keys():
      for bstack1l1111111l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1111111l1_opy_.append(bstack1l1111111l_opy_)
  elif bstack1l1lll11l1_opy_ == bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ࿐"):
    bstack1l11lll1l1_opy_ = bstack111l1lll_opy_(args, logger, CONFIG, bstack1l111l111l_opy_)
    bstack1l11lll1l1_opy_.bstack111l1ll1_opy_()
    bstack1llllll111_opy_()
    bstack1111l1l11_opy_ = True
    bstack111ll1l111_opy_ = bstack1l11lll1l1_opy_.bstack1lll111l1_opy_()
    bstack1l11lll1l1_opy_.bstack111l111l_opy_(bstack111ll1l1l_opy_)
    bstack1l11lll1l1_opy_.bstack111111l1_opy_()
    bstack11lll1lll1_opy_(bstack1l1lll11l1_opy_, CONFIG, bstack1l11lll1l1_opy_.bstack1111111l_opy_())
    bstack1ll1l1l11_opy_ = bstack1l11lll1l1_opy_.bstack1lllllll1_opy_(bstack1l11lll1l_opy_, {
      bstack111l1l_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫ࿑"): bstack1l111l11l1_opy_,
      bstack111l1l_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭࿒"): bstack11ll1l11ll_opy_,
      bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ࿓"): bstack1l111l111l_opy_
    })
    try:
      bstack1l1l1l11l_opy_, bstack1l1llllll1_opy_ = map(list, zip(*bstack1ll1l1l11_opy_))
      bstack111111l11_opy_ = bstack1l1l1l11l_opy_[0]
      for status_code in bstack1l1llllll1_opy_:
        if status_code != 0:
          bstack1lll11ll11_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack111l1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡥࡻ࡫ࠠࡦࡴࡵࡳࡷࡹࠠࡢࡰࡧࠤࡸࡺࡡࡵࡷࡶࠤࡨࡵࡤࡦ࠰ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦ࠺ࠡࡽࢀࠦ࿔").format(str(e)))
  elif bstack1l1lll11l1_opy_ == bstack111l1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ࿕"):
    try:
      from behave.__main__ import main as bstack11111l1l1l_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l11l1l1ll_opy_(e, bstack11l11lll1l_opy_)
    bstack1llllll111_opy_()
    bstack1111l1l11_opy_ = True
    bstack111ll1ll_opy_ = 1
    if bstack111l1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ࿖") in CONFIG:
      bstack111ll1ll_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ࿗")]
    if bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭࿘") in CONFIG:
      bstack1l1l1l1ll_opy_ = int(bstack111ll1ll_opy_) * int(len(CONFIG[bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ࿙")]))
    else:
      bstack1l1l1l1ll_opy_ = int(bstack111ll1ll_opy_)
    config = Configuration(args)
    bstack1lll1l1l1l_opy_ = config.paths
    if len(bstack1lll1l1l1l_opy_) == 0:
      import glob
      pattern = bstack111l1l_opy_ (u"ࠬ࠰ࠪ࠰ࠬ࠱ࡪࡪࡧࡴࡶࡴࡨࠫ࿚")
      bstack11l11111ll_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11l11111ll_opy_)
      config = Configuration(args)
      bstack1lll1l1l1l_opy_ = config.paths
    bstack111ll1l1_opy_ = [os.path.normpath(item) for item in bstack1lll1l1l1l_opy_]
    bstack11ll111l1l_opy_ = [os.path.normpath(item) for item in args]
    bstack11111ll11l_opy_ = [item for item in bstack11ll111l1l_opy_ if item not in bstack111ll1l1_opy_]
    import platform as pf
    if pf.system().lower() == bstack111l1l_opy_ (u"࠭ࡷࡪࡰࡧࡳࡼࡹࠧ࿛"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack111ll1l1_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1l1l1ll111_opy_)))
                    for bstack1l1l1ll111_opy_ in bstack111ll1l1_opy_]
    bstack1111l1l1_opy_ = []
    for spec in bstack111ll1l1_opy_:
      bstack1llll1111_opy_ = []
      bstack1llll1111_opy_ += bstack11111ll11l_opy_
      bstack1llll1111_opy_.append(spec)
      bstack1111l1l1_opy_.append(bstack1llll1111_opy_)
    execution_items = []
    for bstack1llll1111_opy_ in bstack1111l1l1_opy_:
      if bstack111l1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿜") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ࿝")]):
          item = {}
          item[bstack111l1l_opy_ (u"ࠩࡤࡶ࡬࠭࿞")] = bstack111l1l_opy_ (u"ࠪࠤࠬ࿟").join(bstack1llll1111_opy_)
          item[bstack111l1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ࿠")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack111l1l_opy_ (u"ࠬࡧࡲࡨࠩ࿡")] = bstack111l1l_opy_ (u"࠭ࠠࠨ࿢").join(bstack1llll1111_opy_)
        item[bstack111l1l_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭࿣")] = 0
        execution_items.append(item)
    bstack111lll111l_opy_ = bstack11ll1l11l_opy_(execution_items, bstack1l1l1l1ll_opy_)
    for execution_item in bstack111lll111l_opy_:
      bstack1llll11ll_opy_ = []
      for item in execution_item:
        bstack1llll11ll_opy_.append(bstack1l111lll11_opy_(name=str(item[bstack111l1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ࿤")]),
                                             target=bstack11l1ll11ll_opy_,
                                             args=(item[bstack111l1l_opy_ (u"ࠩࡤࡶ࡬࠭࿥")],)))
      for t in bstack1llll11ll_opy_:
        t.start()
      for t in bstack1llll11ll_opy_:
        t.join()
  else:
    bstack11l111l1l1_opy_(bstack11lllll1l_opy_)
  if not bstack11lll11lll_opy_:
    bstack11llll1lll_opy_()
    if(bstack1l1lll11l1_opy_ in [bstack111l1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ࿦"), bstack111l1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ࿧")]):
      bstack11l1lll11_opy_()
  bstack1l11l1lll_opy_.bstack111l1ll1l_opy_()
def browserstack_initialize(bstack1ll1llllll_opy_=None):
  logger.info(bstack111l1l_opy_ (u"ࠬࡘࡵ࡯ࡰ࡬ࡲ࡬ࠦࡓࡅࡍࠣࡻ࡮ࡺࡨࠡࡣࡵ࡫ࡸࡀࠠࠨ࿨") + str(bstack1ll1llllll_opy_))
  run_on_browserstack(bstack1ll1llllll_opy_, None, True)
@measure(event_name=EVENTS.bstack1111l1ll1l_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack11llll1lll_opy_():
  global CONFIG
  global bstack111lll1l1l_opy_
  global bstack1lll11ll11_opy_
  global bstack11111l1l11_opy_
  global bstack1lllll1l1_opy_
  bstack111ll1111_opy_.bstack111ll1ll1_opy_()
  if cli.is_running():
    bstack111l1111l1_opy_.invoke(Events.bstack1l1l1ll11_opy_)
  else:
    bstack1lll1llll_opy_ = bstack1llll1lll_opy_.bstack1111ll1l_opy_(config=CONFIG)
    bstack1lll1llll_opy_.bstack1l1llll1l_opy_(CONFIG)
  if bstack111lll1l1l_opy_ == bstack111l1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭࿩"):
    if not cli.is_enabled(CONFIG):
      bstack1l1l1111_opy_.stop()
  else:
    bstack1l1l1111_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1lll1111_opy_.bstack11l11l1l1l_opy_()
  if bstack111l1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ࿪") in CONFIG and str(CONFIG[bstack111l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ࿫")]).lower() != bstack111l1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ࿬"):
    hashed_id, bstack11ll1llll_opy_ = bstack11111l1111_opy_()
  else:
    hashed_id, bstack11ll1llll_opy_ = get_build_link()
  bstack111ll111ll_opy_(hashed_id)
  logger.info(bstack111l1l_opy_ (u"ࠪࡗࡉࡑࠠࡳࡷࡱࠤࡪࡴࡤࡦࡦࠣࡪࡴࡸࠠࡪࡦ࠽ࠫ࿭") + bstack1lllll1l1_opy_.get_property(bstack111l1l_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭࿮"), bstack111l1l_opy_ (u"ࠬ࠭࿯")) + bstack111l1l_opy_ (u"࠭ࠬࠡࡶࡨࡷࡹ࡮ࡵࡣࠢ࡬ࡨ࠿ࠦࠧ࿰") + os.getenv(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ࿱"), bstack111l1l_opy_ (u"ࠨࠩ࿲")))
  if hashed_id is not None and bstack11111lll1l_opy_() != -1:
    sessions = bstack111111ll11_opy_(hashed_id)
    bstack1ll1llll11_opy_(sessions, bstack11ll1llll_opy_)
  if bstack111lll1l1l_opy_ == bstack111l1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ࿳") and bstack1lll11ll11_opy_ != 0:
    sys.exit(bstack1lll11ll11_opy_)
  if bstack111lll1l1l_opy_ == bstack111l1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ࿴") and bstack11111l1l11_opy_ != 0:
    sys.exit(bstack11111l1l11_opy_)
def bstack111ll111ll_opy_(new_id):
    global bstack111l11l1l1_opy_
    bstack111l11l1l1_opy_ = new_id
def bstack1ll1ll1lll_opy_(bstack1111111ll_opy_):
  if bstack1111111ll_opy_:
    return bstack1111111ll_opy_.capitalize()
  else:
    return bstack111l1l_opy_ (u"ࠫࠬ࿵")
@measure(event_name=EVENTS.bstack1lll11l11l_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1lll1l11ll_opy_(bstack1l1lll1ll1_opy_):
  if bstack111l1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ࿶") in bstack1l1lll1ll1_opy_ and bstack1l1lll1ll1_opy_[bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ࿷")] != bstack111l1l_opy_ (u"ࠧࠨ࿸"):
    return bstack1l1lll1ll1_opy_[bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭࿹")]
  else:
    bstack11l1111ll1_opy_ = bstack111l1l_opy_ (u"ࠤࠥ࿺")
    if bstack111l1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ࿻") in bstack1l1lll1ll1_opy_ and bstack1l1lll1ll1_opy_[bstack111l1l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ࿼")] != None:
      bstack11l1111ll1_opy_ += bstack1l1lll1ll1_opy_[bstack111l1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ࿽")] + bstack111l1l_opy_ (u"ࠨࠬࠡࠤ࿾")
      if bstack1l1lll1ll1_opy_[bstack111l1l_opy_ (u"ࠧࡰࡵࠪ࿿")] == bstack111l1l_opy_ (u"ࠣ࡫ࡲࡷࠧက"):
        bstack11l1111ll1_opy_ += bstack111l1l_opy_ (u"ࠤ࡬ࡓࡘࠦࠢခ")
      bstack11l1111ll1_opy_ += (bstack1l1lll1ll1_opy_[bstack111l1l_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧဂ")] or bstack111l1l_opy_ (u"ࠫࠬဃ"))
      return bstack11l1111ll1_opy_
    else:
      bstack11l1111ll1_opy_ += bstack1ll1ll1lll_opy_(bstack1l1lll1ll1_opy_[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭င")]) + bstack111l1l_opy_ (u"ࠨࠠࠣစ") + (
              bstack1l1lll1ll1_opy_[bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩဆ")] or bstack111l1l_opy_ (u"ࠨࠩဇ")) + bstack111l1l_opy_ (u"ࠤ࠯ࠤࠧဈ")
      if bstack1l1lll1ll1_opy_[bstack111l1l_opy_ (u"ࠪࡳࡸ࠭ဉ")] == bstack111l1l_opy_ (u"ࠦ࡜࡯࡮ࡥࡱࡺࡷࠧည"):
        bstack11l1111ll1_opy_ += bstack111l1l_opy_ (u"ࠧ࡝ࡩ࡯ࠢࠥဋ")
      bstack11l1111ll1_opy_ += bstack1l1lll1ll1_opy_[bstack111l1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪဌ")] or bstack111l1l_opy_ (u"ࠧࠨဍ")
      return bstack11l1111ll1_opy_
@measure(event_name=EVENTS.bstack11lll1ll1_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1111ll1ll1_opy_(bstack1l111llll1_opy_):
  if bstack1l111llll1_opy_ == bstack111l1l_opy_ (u"ࠣࡦࡲࡲࡪࠨဎ"):
    return bstack111l1l_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡈࡵ࡭ࡱ࡮ࡨࡸࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬဏ")
  elif bstack1l111llll1_opy_ == bstack111l1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥတ"):
    return bstack111l1l_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡉࡥ࡮ࡲࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧထ")
  elif bstack1l111llll1_opy_ == bstack111l1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧဒ"):
    return bstack111l1l_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡩࡵࡩࡪࡴ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡩࡵࡩࡪࡴࠢ࠿ࡒࡤࡷࡸ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ဓ")
  elif bstack1l111llll1_opy_ == bstack111l1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨန"):
    return bstack111l1l_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡶࡪࡪ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡴࡨࡨࠧࡄࡅࡳࡴࡲࡶࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪပ")
  elif bstack1l111llll1_opy_ == bstack111l1l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥဖ"):
    return bstack111l1l_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࠩࡥࡦࡣ࠶࠶࠻ࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࠤࡧࡨࡥ࠸࠸࠶ࠣࡀࡗ࡭ࡲ࡫࡯ࡶࡶ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨဗ")
  elif bstack1l111llll1_opy_ == bstack111l1l_opy_ (u"ࠦࡷࡻ࡮࡯࡫ࡱ࡫ࠧဘ"):
    return bstack111l1l_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࡓࡷࡱࡲ࡮ࡴࡧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭မ")
  else:
    return bstack111l1l_opy_ (u"࠭࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࠪယ") + bstack1ll1ll1lll_opy_(
      bstack1l111llll1_opy_) + bstack111l1l_opy_ (u"ࠧ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ရ")
def bstack11ll1l1lll_opy_(session):
  return bstack111l1l_opy_ (u"ࠨ࠾ࡷࡶࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡸ࡯ࡸࠤࡁࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠥࡹࡥࡴࡵ࡬ࡳࡳ࠳࡮ࡢ࡯ࡨࠦࡃࡂࡡࠡࡪࡵࡩ࡫ࡃࠢࡼࡿࠥࠤࡹࡧࡲࡨࡧࡷࡁࠧࡥࡢ࡭ࡣࡱ࡯ࠧࡄࡻࡾ࠾࠲ࡥࡃࡂ࠯ࡵࡦࡁࡿࢂࢁࡽ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿࠳ࡹࡸ࠾ࠨလ").format(
    session[bstack111l1l_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭ဝ")], bstack1lll1l11ll_opy_(session), bstack1111ll1ll1_opy_(session[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡸࡦࡺࡵࡴࠩသ")]),
    bstack1111ll1ll1_opy_(session[bstack111l1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫဟ")]),
    bstack1ll1ll1lll_opy_(session[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ဠ")] or session[bstack111l1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭အ")] or bstack111l1l_opy_ (u"ࠧࠨဢ")) + bstack111l1l_opy_ (u"ࠣࠢࠥဣ") + (session[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫဤ")] or bstack111l1l_opy_ (u"ࠪࠫဥ")),
    session[bstack111l1l_opy_ (u"ࠫࡴࡹࠧဦ")] + bstack111l1l_opy_ (u"ࠧࠦࠢဧ") + session[bstack111l1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪဨ")], session[bstack111l1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩဩ")] or bstack111l1l_opy_ (u"ࠨࠩဪ"),
    session[bstack111l1l_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭ါ")] if session[bstack111l1l_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧာ")] else bstack111l1l_opy_ (u"ࠫࠬိ"))
@measure(event_name=EVENTS.bstack1l11lll1ll_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def bstack1ll1llll11_opy_(sessions, bstack11ll1llll_opy_):
  try:
    bstack1ll1l1ll1l_opy_ = bstack111l1l_opy_ (u"ࠧࠨီ")
    if not os.path.exists(bstack1ll11111l_opy_):
      os.mkdir(bstack1ll11111l_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111l1l_opy_ (u"࠭ࡡࡴࡵࡨࡸࡸ࠵ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ࠫု")), bstack111l1l_opy_ (u"ࠧࡳࠩူ")) as f:
      bstack1ll1l1ll1l_opy_ = f.read()
    bstack1ll1l1ll1l_opy_ = bstack1ll1l1ll1l_opy_.replace(bstack111l1l_opy_ (u"ࠨࡽࠨࡖࡊ࡙ࡕࡍࡖࡖࡣࡈࡕࡕࡏࡖࠨࢁࠬေ"), str(len(sessions)))
    bstack1ll1l1ll1l_opy_ = bstack1ll1l1ll1l_opy_.replace(bstack111l1l_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠥࡾࠩဲ"), bstack11ll1llll_opy_)
    bstack1ll1l1ll1l_opy_ = bstack1ll1l1ll1l_opy_.replace(bstack111l1l_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣࡓࡇࡍࡆࠧࢀࠫဳ"),
                                              sessions[0].get(bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡲࡦࡳࡥࠨဴ")) if sessions[0] else bstack111l1l_opy_ (u"ࠬ࠭ဵ"))
    with open(os.path.join(bstack1ll11111l_opy_, bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪံ")), bstack111l1l_opy_ (u"ࠧࡸ့ࠩ")) as stream:
      stream.write(bstack1ll1l1ll1l_opy_.split(bstack111l1l_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁࠬး"))[0])
      for session in sessions:
        stream.write(bstack11ll1l1lll_opy_(session))
      stream.write(bstack1ll1l1ll1l_opy_.split(bstack111l1l_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂ္࠭"))[1])
    logger.info(bstack111l1l_opy_ (u"ࠪࡋࡪࡴࡥࡳࡣࡷࡩࡩࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡨࡵࡪ࡮ࡧࠤࡦࡸࡴࡪࡨࡤࡧࡹࡹࠠࡢࡶࠣࡿࢂ်࠭").format(bstack1ll11111l_opy_));
  except Exception as e:
    logger.debug(bstack1l1l11l111_opy_.format(str(e)))
def bstack111111ll11_opy_(hashed_id):
  global CONFIG
  try:
    bstack1l1ll111ll_opy_ = datetime.datetime.now()
    host = bstack111l1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠯ࡦࡰࡴࡻࡤ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫျ") if bstack111l1l_opy_ (u"ࠬࡧࡰࡱࠩြ") in CONFIG else bstack111l1l_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧွ")
    user = CONFIG[bstack111l1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩှ")]
    key = CONFIG[bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫဿ")]
    bstack1l11l11l1_opy_ = bstack111l1l_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨ၀") if bstack111l1l_opy_ (u"ࠪࡥࡵࡶࠧ၁") in CONFIG else (bstack111l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨ၂") if CONFIG.get(bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ၃")) else bstack111l1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ၄"))
    host = bstack1l1ll1ll1l_opy_(cli.config, [bstack111l1l_opy_ (u"ࠢࡢࡲ࡬ࡷࠧ၅"), bstack111l1l_opy_ (u"ࠣࡣࡳࡴࡆࡻࡴࡰ࡯ࡤࡸࡪࠨ၆"), bstack111l1l_opy_ (u"ࠤࡤࡴ࡮ࠨ၇")], host) if bstack111l1l_opy_ (u"ࠪࡥࡵࡶࠧ၈") in CONFIG else bstack1l1ll1ll1l_opy_(cli.config, [bstack111l1l_opy_ (u"ࠦࡦࡶࡩࡴࠤ၉"), bstack111l1l_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢ၊"), bstack111l1l_opy_ (u"ࠨࡡࡱ࡫ࠥ။")], host)
    url = bstack111l1l_opy_ (u"ࠧࡼࡿ࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡶࡩࡸࡹࡩࡰࡰࡶ࠲࡯ࡹ࡯࡯ࠩ၌").format(host, bstack1l11l11l1_opy_, hashed_id)
    headers = {
      bstack111l1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧ၍"): bstack111l1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ၎"),
    }
    proxies = bstack1l1111l1l1_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1l1l111ll1_opy_(bstack111l1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡩࡨࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡹ࡟࡭࡫ࡶࡸࠧ၏"), datetime.datetime.now() - bstack1l1ll111ll_opy_)
      return list(map(lambda session: session[bstack111l1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩၐ")], response.json()))
  except Exception as e:
    logger.debug(bstack1111ll111_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack11ll1ll11_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def get_build_link():
  global CONFIG
  global bstack111l11l1l1_opy_
  try:
    if bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨၑ") in CONFIG:
      bstack1l1ll111ll_opy_ = datetime.datetime.now()
      host = bstack111l1l_opy_ (u"࠭ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥࠩၒ") if bstack111l1l_opy_ (u"ࠧࡢࡲࡳࠫၓ") in CONFIG else bstack111l1l_opy_ (u"ࠨࡣࡳ࡭ࠬၔ")
      user = CONFIG[bstack111l1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫၕ")]
      key = CONFIG[bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ၖ")]
      bstack1l11l11l1_opy_ = bstack111l1l_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪၗ") if bstack111l1l_opy_ (u"ࠬࡧࡰࡱࠩၘ") in CONFIG else bstack111l1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨၙ")
      url = bstack111l1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡽࢀ࠾ࢀࢃࡀࡼࡿ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠰࡭ࡷࡴࡴࠧၚ").format(user, key, host, bstack1l11l11l1_opy_)
      if cli.is_enabled(CONFIG):
        bstack11ll1llll_opy_, hashed_id = cli.bstack1l11l11111_opy_()
        logger.info(bstack1l111111l_opy_.format(bstack11ll1llll_opy_))
        return [hashed_id, bstack11ll1llll_opy_]
      else:
        headers = {
          bstack111l1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧၛ"): bstack111l1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬၜ"),
        }
        if bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬၝ") in CONFIG:
          params = {bstack111l1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩၞ"): CONFIG[bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨၟ")], bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩၠ"): CONFIG[bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩၡ")]}
        else:
          params = {bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ၢ"): CONFIG[bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬၣ")]}
        proxies = bstack1l1111l1l1_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack1llll1l111_opy_ = response.json()[0][bstack111l1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡣࡷ࡬ࡰࡩ࠭ၤ")]
          if bstack1llll1l111_opy_:
            bstack11ll1llll_opy_ = bstack1llll1l111_opy_[bstack111l1l_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨၥ")].split(bstack111l1l_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧ࠲ࡨࡵࡪ࡮ࡧࠫၦ"))[0] + bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡸ࠵ࠧၧ") + bstack1llll1l111_opy_[
              bstack111l1l_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪၨ")]
            logger.info(bstack1l111111l_opy_.format(bstack11ll1llll_opy_))
            bstack111l11l1l1_opy_ = bstack1llll1l111_opy_[bstack111l1l_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫၩ")]
            bstack111ll11l1_opy_ = CONFIG[bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬၪ")]
            if bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬၫ") in CONFIG:
              bstack111ll11l1_opy_ += bstack111l1l_opy_ (u"ࠫࠥ࠭ၬ") + CONFIG[bstack111l1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧၭ")]
            if bstack111ll11l1_opy_ != bstack1llll1l111_opy_[bstack111l1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫၮ")]:
              logger.debug(bstack11ll11l11l_opy_.format(bstack1llll1l111_opy_[bstack111l1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬၯ")], bstack111ll11l1_opy_))
            cli.bstack1l1l111ll1_opy_(bstack111l1l_opy_ (u"ࠣࡪࡷࡸࡵࡀࡧࡦࡶࡢࡦࡺ࡯࡬ࡥࡡ࡯࡭ࡳࡱࠢၰ"), datetime.datetime.now() - bstack1l1ll111ll_opy_)
            return [bstack1llll1l111_opy_[bstack111l1l_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬၱ")], bstack11ll1llll_opy_]
    else:
      logger.warn(bstack11llll1l1l_opy_)
  except Exception as e:
    logger.debug(bstack1ll111llll_opy_.format(str(e)))
  return [None, None]
def bstack1l1l1lll1l_opy_(url, bstack1111l1l1l1_opy_=False):
  global CONFIG
  global bstack11l1l111l1_opy_
  if not bstack11l1l111l1_opy_:
    hostname = bstack1l1l1ll1l1_opy_(url)
    is_private = bstack111lll111_opy_(hostname)
    if (bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧၲ") in CONFIG and not bstack11l1llll1_opy_(CONFIG[bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨၳ")])) and (is_private or bstack1111l1l1l1_opy_):
      bstack11l1l111l1_opy_ = hostname
def bstack1l1l1ll1l1_opy_(url):
  return urlparse(url).hostname
def bstack111lll111_opy_(hostname):
  for bstack111l11lll_opy_ in bstack1l1111llll_opy_:
    regex = re.compile(bstack111l11lll_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1l1l11ll11_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1l1ll1l111_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack11111lll11_opy_
  bstack1llllll11l_opy_ = not (bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၴ"), None) and bstack1l11l1ll_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၵ"), None))
  bstack1l1l1l1lll_opy_ = getattr(driver, bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧၶ"), None) != True
  bstack111l11l11l_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၷ"), None) and bstack1l11l1ll_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၸ"), None)
  if bstack111l11l11l_opy_:
    if not bstack1l11l11l11_opy_():
      logger.warning(bstack111l1l_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸ࠴ࠢၹ"))
      return {}
    logger.debug(bstack111l1l_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨၺ"))
    logger.debug(perform_scan(driver, driver_command=bstack111l1l_opy_ (u"ࠬ࡫ࡸࡦࡥࡸࡸࡪ࡙ࡣࡳ࡫ࡳࡸࠬၻ")))
    results = bstack111ll111l1_opy_(bstack111l1l_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹࡹࠢၼ"))
    if results is not None and results.get(bstack111l1l_opy_ (u"ࠢࡪࡵࡶࡹࡪࡹࠢၽ")) is not None:
        return results[bstack111l1l_opy_ (u"ࠣ࡫ࡶࡷࡺ࡫ࡳࠣၾ")]
    logger.error(bstack111l1l_opy_ (u"ࠤࡑࡳࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡘࡥࡴࡷ࡯ࡸࡸࠦࡷࡦࡴࡨࠤ࡫ࡵࡵ࡯ࡦ࠱ࠦၿ"))
    return []
  if not bstack1lll11ll1_opy_.bstack1l1l1111l_opy_(CONFIG, bstack11111lll11_opy_) or (bstack1l1l1l1lll_opy_ and bstack1llllll11l_opy_):
    logger.warning(bstack111l1l_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷ࠳ࠨႀ"))
    return {}
  try:
    logger.debug(bstack111l1l_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨႁ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack111ll11l11_opy_.bstack1111lll1l_opy_)
    return results
  except Exception:
    logger.error(bstack111l1l_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡺࡩࡷ࡫ࠠࡧࡱࡸࡲࡩ࠴ࠢႂ"))
    return {}
@measure(event_name=EVENTS.bstack111llllll1_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack11111lll11_opy_
  bstack1llllll11l_opy_ = not (bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪႃ"), None) and bstack1l11l1ll_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ႄ"), None))
  bstack1l1l1l1lll_opy_ = getattr(driver, bstack111l1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨႅ"), None) != True
  bstack111l11l11l_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩႆ"), None) and bstack1l11l1ll_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬႇ"), None)
  if bstack111l11l11l_opy_:
    if not bstack1l11l11l11_opy_():
      logger.warning(bstack111l1l_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹ࠯ࠤႈ"))
      return {}
    logger.debug(bstack111l1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻࠪႉ"))
    logger.debug(perform_scan(driver, driver_command=bstack111l1l_opy_ (u"࠭ࡥࡹࡧࡦࡹࡹ࡫ࡓࡤࡴ࡬ࡴࡹ࠭ႊ")))
    results = bstack111ll111l1_opy_(bstack111l1l_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡓࡶ࡯ࡰࡥࡷࡿࠢႋ"))
    if results is not None and results.get(bstack111l1l_opy_ (u"ࠣࡵࡸࡱࡲࡧࡲࡺࠤႌ")) is not None:
        return results[bstack111l1l_opy_ (u"ࠤࡶࡹࡲࡳࡡࡳࡻႍࠥ")]
    logger.error(bstack111l1l_opy_ (u"ࠥࡒࡴࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡒࡦࡵࡸࡰࡹࡹࠠࡔࡷࡰࡱࡦࡸࡹࠡࡹࡤࡷࠥ࡬࡯ࡶࡰࡧ࠲ࠧႎ"))
    return {}
  if not bstack1lll11ll1_opy_.bstack1l1l1111l_opy_(CONFIG, bstack11111lll11_opy_) or (bstack1l1l1l1lll_opy_ and bstack1llllll11l_opy_):
    logger.warning(bstack111l1l_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡳࡶ࡯ࡰࡥࡷࡿ࠮ࠣႏ"))
    return {}
  try:
    logger.debug(bstack111l1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻࠪ႐"))
    logger.debug(perform_scan(driver))
    bstack1ll1lll111_opy_ = driver.execute_async_script(bstack111ll11l11_opy_.bstack11ll11llll_opy_)
    return bstack1ll1lll111_opy_
  except Exception:
    logger.error(bstack111l1l_opy_ (u"ࠨࡎࡰࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡹࡲࡳࡡࡳࡻࠣࡻࡦࡹࠠࡧࡱࡸࡲࡩ࠴ࠢ႑"))
    return {}
def bstack1l11l11l11_opy_():
  global CONFIG
  global bstack11111lll11_opy_
  bstack1l1111l11l_opy_ = bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ႒"), None) and bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ႓"), None)
  if not bstack1lll11ll1_opy_.bstack1l1l1111l_opy_(CONFIG, bstack11111lll11_opy_) or not bstack1l1111l11l_opy_:
        logger.warning(bstack111l1l_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤ႔"))
        return False
  return True
def bstack111ll111l1_opy_(bstack11ll1l111_opy_):
    bstack1ll1lll11_opy_ = bstack1l1l1111_opy_.current_test_uuid() if bstack1l1l1111_opy_.current_test_uuid() else bstack1lll1111_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack1l1l1lllll_opy_(bstack1ll1lll11_opy_, bstack11ll1l111_opy_))
        try:
            return future.result(timeout=bstack11l1111l1l_opy_)
        except TimeoutError:
            logger.error(bstack111l1l_opy_ (u"ࠥࡘ࡮ࡳࡥࡰࡷࡷࠤࡦ࡬ࡴࡦࡴࠣࡿࢂࡹࠠࡸࡪ࡬ࡰࡪࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡔࡨࡷࡺࡲࡴࡴࠤ႕").format(bstack11l1111l1l_opy_))
        except Exception as ex:
            logger.debug(bstack111l1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡶࡪࡺࡲࡪࡧࡹ࡭ࡳ࡭ࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡽࢀ࠲ࠥࡋࡲࡳࡱࡵࠤ࠲ࠦࡻࡾࠤ႖").format(bstack11ll1l111_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack1ll111l1l1_opy_, stage=STAGE.bstack1ll1ll111_opy_, bstack11l1111ll1_opy_=bstack111l111l1l_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack11111lll11_opy_
  bstack1llllll11l_opy_ = not (bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ႗"), None) and bstack1l11l1ll_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ႘"), None))
  bstack1l1ll1ll1_opy_ = not (bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ႙"), None) and bstack1l11l1ll_opy_(
          threading.current_thread(), bstack111l1l_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪႚ"), None))
  bstack1l1l1l1lll_opy_ = getattr(driver, bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩႛ"), None) != True
  if not bstack1lll11ll1_opy_.bstack1l1l1111l_opy_(CONFIG, bstack11111lll11_opy_) or (bstack1l1l1l1lll_opy_ and bstack1llllll11l_opy_ and bstack1l1ll1ll1_opy_):
    logger.warning(bstack111l1l_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡹࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡤࡣࡱ࠲ࠧႜ"))
    return {}
  try:
    bstack1l11l111l1_opy_ = bstack111l1l_opy_ (u"ࠫࡦࡶࡰࠨႝ") in CONFIG and CONFIG.get(bstack111l1l_opy_ (u"ࠬࡧࡰࡱࠩ႞"), bstack111l1l_opy_ (u"࠭ࠧ႟"))
    session_id = getattr(driver, bstack111l1l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠫႠ"), None)
    if not session_id:
      logger.warning(bstack111l1l_opy_ (u"ࠣࡐࡲࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡏࡄࠡࡨࡲࡹࡳࡪࠠࡧࡱࡵࠤࡩࡸࡩࡷࡧࡵࠦႡ"))
      return {bstack111l1l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣႢ"): bstack111l1l_opy_ (u"ࠥࡒࡴࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࠣࡪࡴࡻ࡮ࡥࠤႣ")}
    if bstack1l11l111l1_opy_:
      try:
        bstack1llll1l11l_opy_ = {
              bstack111l1l_opy_ (u"ࠫࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠨႤ"): os.environ.get(bstack111l1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪႥ"), os.environ.get(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡊࡘࡖࠪႦ"), bstack111l1l_opy_ (u"ࠧࠨႧ"))),
              bstack111l1l_opy_ (u"ࠨࡶ࡫ࡘࡪࡹࡴࡓࡷࡱ࡙ࡺ࡯ࡤࠨႨ"): bstack1l1l1111_opy_.current_test_uuid() if bstack1l1l1111_opy_.current_test_uuid() else bstack1lll1111_opy_.current_hook_uuid(),
              bstack111l1l_opy_ (u"ࠩࡤࡹࡹ࡮ࡈࡦࡣࡧࡩࡷ࠭Ⴉ"): os.environ.get(bstack111l1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨႪ")),
              bstack111l1l_opy_ (u"ࠫࡸࡩࡡ࡯ࡖ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫႫ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack111l1l_opy_ (u"ࠬࡺࡨࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪႬ"): os.environ.get(bstack111l1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫႭ"), bstack111l1l_opy_ (u"ࠧࠨႮ")),
              bstack111l1l_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨႯ"): kwargs.get(bstack111l1l_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࡡࡦࡳࡲࡳࡡ࡯ࡦࠪႰ"), None) or bstack111l1l_opy_ (u"ࠪࠫႱ")
          }
        if not hasattr(thread_local, bstack111l1l_opy_ (u"ࠫࡧࡧࡳࡦࡡࡤࡴࡵࡥࡡ࠲࠳ࡼࡣࡸࡩࡲࡪࡲࡷࠫႲ")):
            scripts = {bstack111l1l_opy_ (u"ࠬࡹࡣࡢࡰࠪႳ"): bstack111ll11l11_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack11l1l1l1ll_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack11l1l1l1ll_opy_[bstack111l1l_opy_ (u"࠭ࡳࡤࡣࡱࠫႴ")] = bstack11l1l1l1ll_opy_[bstack111l1l_opy_ (u"ࠧࡴࡥࡤࡲࠬႵ")] % json.dumps(bstack1llll1l11l_opy_)
        bstack111ll11l11_opy_.bstack11llll11l_opy_(bstack11l1l1l1ll_opy_)
        bstack111ll11l11_opy_.store()
        bstack11l11ll1l_opy_ = driver.execute_script(bstack111ll11l11_opy_.perform_scan)
      except Exception as bstack11l11l1111_opy_:
        logger.info(bstack111l1l_opy_ (u"ࠣࡃࡳࡴ࡮ࡻ࡭ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳࠦࡦࡢ࡫࡯ࡩࡩࡀࠠࠣႶ") + str(bstack11l11l1111_opy_))
        bstack11l11ll1l_opy_ = {bstack111l1l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣႷ"): str(bstack11l11l1111_opy_)}
    else:
      bstack11l11ll1l_opy_ = driver.execute_async_script(bstack111ll11l11_opy_.perform_scan, {bstack111l1l_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪႸ"): kwargs.get(bstack111l1l_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣࡨࡵ࡭࡮ࡣࡱࡨࠬႹ"), None) or bstack111l1l_opy_ (u"ࠬ࠭Ⴚ")})
    return bstack11l11ll1l_opy_
  except Exception as err:
    logger.error(bstack111l1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡵࡹࡳࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡤࡣࡱ࠲ࠥࢁࡽࠣႻ").format(str(err)))
    return {}