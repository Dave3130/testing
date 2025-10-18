# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
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
from browserstack_sdk.bstack11l1lllll_opy_ import bstack1ll1ll1l1_opy_
from browserstack_sdk.bstack1lll1l1l1_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack1ll1ll11l_opy_():
  global CONFIG
  headers = {
        bstack1l1lll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪ৿"): bstack1l1lll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ਀"),
      }
  proxies = bstack11l1l11ll_opy_(CONFIG, bstack11lll1l1l_opy_)
  try:
    response = requests.get(bstack11lll1l1l_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l111llll_opy_ = response.json()[bstack1l1lll1_opy_ (u"࠭ࡨࡶࡤࡶࠫਁ")]
      logger.debug(bstack11111l11l_opy_.format(response.json()))
      return bstack1l111llll_opy_
    else:
      logger.debug(bstack1llll1l1l1_opy_.format(bstack1l1lll1_opy_ (u"ࠢࡓࡧࡶࡴࡴࡴࡳࡦࠢࡍࡗࡔࡔࠠࡱࡣࡵࡷࡪࠦࡥࡳࡴࡲࡶࠥࠨਂ")))
  except Exception as e:
    logger.debug(bstack1llll1l1l1_opy_.format(e))
def bstack1111ll1ll1_opy_(hub_url):
  global CONFIG
  url = bstack1l1lll1_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥਃ")+  hub_url + bstack1l1lll1_opy_ (u"ࠤ࠲ࡧ࡭࡫ࡣ࡬ࠤ਄")
  headers = {
        bstack1l1lll1_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩਅ"): bstack1l1lll1_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧਆ"),
      }
  proxies = bstack11l1l11ll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack111ll1l11l_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack11l1ll1l11_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack1l1l11ll11_opy_, stage=STAGE.bstack1111llll1l_opy_)
def bstack111lll111l_opy_():
  try:
    global bstack1l111lllll_opy_
    bstack1l111llll_opy_ = bstack1ll1ll11l_opy_()
    bstack111ll1lll1_opy_ = []
    results = []
    for bstack1llll1llll_opy_ in bstack1l111llll_opy_:
      bstack111ll1lll1_opy_.append(bstack11lllll1l_opy_(target=bstack1111ll1ll1_opy_,args=(bstack1llll1llll_opy_,)))
    for t in bstack111ll1lll1_opy_:
      t.start()
    for t in bstack111ll1lll1_opy_:
      results.append(t.join())
    bstack1l1ll111l_opy_ = {}
    for item in results:
      hub_url = item[bstack1l1lll1_opy_ (u"ࠬ࡮ࡵࡣࡡࡸࡶࡱ࠭ਇ")]
      latency = item[bstack1l1lll1_opy_ (u"࠭࡬ࡢࡶࡨࡲࡨࡿࠧਈ")]
      bstack1l1ll111l_opy_[hub_url] = latency
    bstack1l111l1l1_opy_ = min(bstack1l1ll111l_opy_, key= lambda x: bstack1l1ll111l_opy_[x])
    bstack1l111lllll_opy_ = bstack1l111l1l1_opy_
    logger.debug(bstack1111l11lll_opy_.format(bstack1l111l1l1_opy_))
  except Exception as e:
    logger.debug(bstack1l1l1l1lll_opy_.format(e))
from browserstack_sdk.bstack1111ll1l_opy_ import *
from browserstack_sdk.bstack11l1111l_opy_ import *
from browserstack_sdk.bstack11ll1l11_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack111l11l1l_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack11111ll1l1_opy_, stage=STAGE.bstack1111llll1l_opy_)
def bstack1l11111ll1_opy_():
    global bstack1l111lllll_opy_
    try:
        bstack1l1lll111_opy_ = bstack1ll1l11ll1_opy_()
        bstack1l11llll11_opy_(bstack1l1lll111_opy_)
        hub_url = bstack1l1lll111_opy_.get(bstack1l1lll1_opy_ (u"ࠢࡶࡴ࡯ࠦਉ"), bstack1l1lll1_opy_ (u"ࠣࠤਊ"))
        if hub_url.endswith(bstack1l1lll1_opy_ (u"ࠩ࠲ࡻࡩ࠵ࡨࡶࡤࠪ਋")):
            hub_url = hub_url.rsplit(bstack1l1lll1_opy_ (u"ࠪ࠳ࡼࡪ࠯ࡩࡷࡥࠫ਌"), 1)[0]
        if hub_url.startswith(bstack1l1lll1_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࠬ਍")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack1l1lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠧ਎")):
            hub_url = hub_url[8:]
        bstack1l111lllll_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1ll1l11ll1_opy_():
    global CONFIG
    bstack1lllllllll_opy_ = CONFIG.get(bstack1l1lll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪਏ"), {}).get(bstack1l1lll1_opy_ (u"ࠧࡨࡴ࡬ࡨࡓࡧ࡭ࡦࠩਐ"), bstack1l1lll1_opy_ (u"ࠨࡐࡒࡣࡌࡘࡉࡅࡡࡑࡅࡒࡋ࡟ࡑࡃࡖࡗࡊࡊࠧ਑"))
    if not isinstance(bstack1lllllllll_opy_, str):
        raise ValueError(bstack1l1lll1_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡉࡵ࡭ࡩࠦ࡮ࡢ࡯ࡨࠤࡲࡻࡳࡵࠢࡥࡩࠥࡧࠠࡷࡣ࡯࡭ࡩࠦࡳࡵࡴ࡬ࡲ࡬ࠨ਒"))
    try:
        bstack1l1lll111_opy_ = bstack11l111111l_opy_(bstack1lllllllll_opy_)
        return bstack1l1lll111_opy_
    except Exception as e:
        logger.error(bstack1l1lll1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࠿ࠦࡻࡾࠤਓ").format(str(e)))
        return {}
def bstack11l111111l_opy_(bstack1lllllllll_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack1l1lll1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ਔ")] or not CONFIG[bstack1l1lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨਕ")]:
            raise ValueError(bstack1l1lll1_opy_ (u"ࠨࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡵࡴࡧࡵࡲࡦࡳࡥࠡࡱࡵࠤࡦࡩࡣࡦࡵࡶࠤࡰ࡫ࡹࠣਖ"))
        url = bstack111l1l1111_opy_ + bstack1lllllllll_opy_
        auth = (CONFIG[bstack1l1lll1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩਗ")], CONFIG[bstack1l1lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫਘ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1l11lll11l_opy_ = json.loads(response.text)
            return bstack1l11lll11l_opy_
    except ValueError as ve:
        logger.error(bstack1l1lll1_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࠿ࠦࡻࡾࠤਙ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack1l1lll1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡧࡳ࡫ࡧࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡀࠠࡼࡿࠥਚ").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1l11llll11_opy_(bstack1l111l111_opy_):
    global CONFIG
    if bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨਛ") not in CONFIG or str(CONFIG[bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩਜ")]).lower() == bstack1l1lll1_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬਝ"):
        CONFIG[bstack1l1lll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭ਞ")] = False
    elif bstack1l1lll1_opy_ (u"ࠨ࡫ࡶࡘࡷ࡯ࡡ࡭ࡉࡵ࡭ࡩ࠭ਟ") in bstack1l111l111_opy_:
        bstack111ll1lll_opy_ = CONFIG.get(bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ਠ"), {})
        logger.debug(bstack1l1lll1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡼ࡮ࡹࡴࡪࡰࡪࠤࡱࡵࡣࡢ࡮ࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠫࡳࠣਡ"), bstack111ll1lll_opy_)
        bstack111ll111l1_opy_ = bstack1l111l111_opy_.get(bstack1l1lll1_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰࡖࡪࡶࡥࡢࡶࡨࡶࡸࠨਢ"), [])
        bstack1lll11l1l_opy_ = bstack1l1lll1_opy_ (u"ࠧ࠲ࠢਣ").join(bstack111ll111l1_opy_)
        logger.debug(bstack1l1lll1_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡉࡵࡴࡶࡲࡱࠥࡸࡥࡱࡧࡤࡸࡪࡸࠠࡴࡶࡵ࡭ࡳ࡭࠺ࠡࠧࡶࠦਤ"), bstack1lll11l1l_opy_)
        bstack1ll1l1l111_opy_ = {
            bstack1l1lll1_opy_ (u"ࠢ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤਥ"): bstack1l1lll1_opy_ (u"ࠣࡣࡷࡷ࠲ࡸࡥࡱࡧࡤࡸࡪࡸࠢਦ"),
            bstack1l1lll1_opy_ (u"ࠤࡩࡳࡷࡩࡥࡍࡱࡦࡥࡱࠨਧ"): bstack1l1lll1_opy_ (u"ࠥࡸࡷࡻࡥࠣਨ"),
            bstack1l1lll1_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷࠨ਩"): bstack1lll11l1l_opy_
        }
        bstack111ll1lll_opy_.update(bstack1ll1l1l111_opy_)
        logger.debug(bstack1l1lll1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤ࡚ࡶࡤࡢࡶࡨࡨࠥࡲ࡯ࡤࡣ࡯ࠤࡴࡶࡴࡪࡱࡱࡷ࠿ࠦࠥࡴࠤਪ"), bstack111ll1lll_opy_)
        CONFIG[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪਫ")] = bstack111ll1lll_opy_
        logger.debug(bstack1l1lll1_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡆࡪࡰࡤࡰࠥࡉࡏࡏࡈࡌࡋ࠿ࠦࠥࡴࠤਬ"), CONFIG)
def bstack111l1ll11_opy_():
    bstack1l1lll111_opy_ = bstack1ll1l11ll1_opy_()
    if not bstack1l1lll111_opy_[bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠨਭ")]:
      raise ValueError(bstack1l1lll1_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠢ࡬ࡷࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡦࡳࡱࡰࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵ࠱ࠦਮ"))
    return bstack1l1lll111_opy_[bstack1l1lll1_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࡕࡳ࡮ࠪਯ")] + bstack1l1lll1_opy_ (u"ࠫࡄࡩࡡࡱࡵࡀࠫਰ")
@measure(event_name=EVENTS.bstack1l1111ll1l_opy_, stage=STAGE.bstack1111llll1l_opy_)
def bstack11l1l11l11_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack1l1lll1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ਱")], CONFIG[bstack1l1lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩਲ")])
        url = bstack1l1ll11l1_opy_
        logger.debug(bstack1l1lll1_opy_ (u"ࠢࡂࡶࡷࡩࡲࡶࡴࡪࡰࡪࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦࡢࡶ࡫࡯ࡨࡸࠦࡦࡳࡱࡰࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡘࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠠࡂࡒࡌࠦਲ਼"))
        try:
            response = requests.get(url, auth=auth, headers={bstack1l1lll1_opy_ (u"ࠣࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠢ਴"): bstack1l1lll1_opy_ (u"ࠤࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠧਵ")})
            if response.status_code == 200:
                bstack1l111l1lll_opy_ = json.loads(response.text)
                bstack11lll1l111_opy_ = bstack1l111l1lll_opy_.get(bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡵࠪਸ਼"), [])
                if bstack11lll1l111_opy_:
                    bstack11111lll11_opy_ = bstack11lll1l111_opy_[0]
                    build_hashed_id = bstack11111lll11_opy_.get(bstack1l1lll1_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ਷"))
                    bstack11lll1l1l1_opy_ = bstack1111111l1_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack11lll1l1l1_opy_])
                    logger.info(bstack1l1llll111_opy_.format(bstack11lll1l1l1_opy_))
                    bstack11ll1l1lll_opy_ = CONFIG[bstack1l1lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨਸ")]
                    if bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨਹ") in CONFIG:
                      bstack11ll1l1lll_opy_ += bstack1l1lll1_opy_ (u"ࠧࠡࠩ਺") + CONFIG[bstack1l1lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ਻")]
                    if bstack11ll1l1lll_opy_ != bstack11111lll11_opy_.get(bstack1l1lll1_opy_ (u"ࠩࡱࡥࡲ࡫਼ࠧ")):
                      logger.debug(bstack11lll1ll1_opy_.format(bstack11111lll11_opy_.get(bstack1l1lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨ਽")), bstack11ll1l1lll_opy_))
                    return result
                else:
                    logger.debug(bstack1l1lll1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡒࡴࠦࡢࡶ࡫࡯ࡨࡸࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡶ࡫ࡩࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠮ࠣਾ"))
            else:
                logger.debug(bstack1l1lll1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦࡢࡶ࡫࡯ࡨࡸ࠴ࠢਿ"))
        except Exception as e:
            logger.error(bstack1l1lll1_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࡳࠡ࠼ࠣࡿࢂࠨੀ").format(str(e)))
    else:
        logger.debug(bstack1l1lll1_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡃࡐࡐࡉࡍࡌࠦࡩࡴࠢࡱࡳࡹࠦࡳࡦࡶ࠱ࠤ࡚ࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦࡢࡶ࡫࡯ࡨࡸ࠴ࠢੁ"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1llll111ll_opy_ import bstack1llll111ll_opy_, Events, bstack1l1l111l1l_opy_, bstack1lll1l1l1l_opy_
from bstack_utils.measure import bstack11l1l1111l_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1111l1ll1_opy_ import bstack1l1llllll_opy_
from bstack_utils.messages import *
from bstack_utils import bstack111l11l1l_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l111l1111_opy_, bstack1l1l1l1l1l_opy_, bstack11l11ll11l_opy_, bstack1l1l1l1l_opy_, \
  bstack1l1l1l1l1_opy_, \
  Notset, bstack1111lll1l1_opy_, \
  bstack1lll11111_opy_, bstack111ll1111_opy_, bstack1111ll1l1_opy_, bstack11lll11l11_opy_, bstack1l1l1lll1_opy_, bstack111l1l11ll_opy_, \
  bstack1l11l1l1l_opy_, \
  bstack1l11ll1l1_opy_, bstack1l1l1ll11l_opy_, bstack11ll1l11ll_opy_, bstack1l1ll11ll_opy_, \
  bstack1l111llll1_opy_, bstack111l1111ll_opy_, bstack111ll11ll_opy_, bstack11l11l11l1_opy_
from bstack_utils.bstack1l1111llll_opy_ import bstack1l111l11l_opy_
from bstack_utils.bstack11llll1lll_opy_ import bstack1ll1llllll_opy_, bstack1l1ll1l1l_opy_
from bstack_utils.bstack1llll1l1ll_opy_ import bstack1lll1l111l_opy_
from bstack_utils.bstack1l111l11ll_opy_ import bstack111lll1111_opy_, bstack1111l1ll11_opy_
from bstack_utils.bstack1l11111ll_opy_ import bstack1l11111ll_opy_
from bstack_utils.bstack1l11111l1l_opy_ import bstack1l11ll1111_opy_
from bstack_utils.proxy import bstack11l111llll_opy_, bstack11l1l11ll_opy_, bstack11lll11ll_opy_, bstack1lll11lll1_opy_
from bstack_utils.bstack111l111ll_opy_ import bstack1ll1ll1ll_opy_
import bstack_utils.bstack1111ll1111_opy_ as bstack1l1l1l1111_opy_
import bstack_utils.bstack1l1111l11_opy_ as bstack111llll1ll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack111l1lll11_opy_ import bstack11l1llll11_opy_
from bstack_utils.bstack11l111l1_opy_ import bstack1111llll_opy_
from bstack_utils.bstack1l11111l1_opy_ import bstack11l1lll1ll_opy_
if os.getenv(bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡎࡌࡣࡍࡕࡏࡌࡕࠪੂ")):
  cli.bstack11llll1ll_opy_()
else:
  os.environ[bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡎࡏࡐࡍࡖࠫ੃")] = bstack1l1lll1_opy_ (u"ࠪࡸࡷࡻࡥࠨ੄")
bstack111l1l1l11_opy_ = bstack1l1lll1_opy_ (u"ࠫࠥࠦ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰࡞ࡱࠤࠥ࡯ࡦࠩࡲࡤ࡫ࡪࠦ࠽࠾࠿ࠣࡺࡴ࡯ࡤࠡ࠲ࠬࠤࢀࡢ࡮ࠡࠢࠣࡸࡷࡿࡻ࡝ࡰࠣࡧࡴࡴࡳࡵࠢࡩࡷࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩ࡞ࠪࡪࡸࡢࠧࠪ࠽࡟ࡲࠥࠦࠠࠡࠢࡩࡷ࠳ࡧࡰࡱࡧࡱࡨࡋ࡯࡬ࡦࡕࡼࡲࡨ࠮ࡢࡴࡶࡤࡧࡰࡥࡰࡢࡶ࡫࠰ࠥࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡰࡠ࡫ࡱࡨࡪࡾࠩࠡ࠭ࠣࠦ࠿ࠨࠠࠬࠢࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡎࡘࡕࡎ࠯ࡲࡤࡶࡸ࡫ࠨࠩࡣࡺࡥ࡮ࡺࠠ࡯ࡧࡺࡔࡦ࡭ࡥ࠳࠰ࡨࡺࡦࡲࡵࡢࡶࡨࠬࠧ࠮ࠩࠡ࠿ࡁࠤࢀࢃࠢ࠭ࠢ࡟ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦ࡬࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡧࡷࡥ࡮ࡲࡳࠣࡿ࡟ࠫ࠮࠯ࠩ࡜ࠤ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠧࡣࠩࠡ࠭ࠣࠦ࠱ࡢ࡜࡯ࠤࠬࡠࡳࠦࠠࠡࠢࢀࡧࡦࡺࡣࡩࠪࡨࡼ࠮ࢁ࡜࡯ࠢࠣࠤࠥࢃ࡜࡯ࠢࠣࢁࡡࡴࠠࠡ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࠫ੅")
bstack1l1ll111ll_opy_ = bstack1l1lll1_opy_ (u"ࠬࡢ࡮࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࡨࡵ࡮ࡴࡶࠣࡦࡸࡺࡡࡤ࡭ࡢࡴࡦࡺࡨࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷ࡢࡢ࡮ࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠱࡞࡞ࡱࡧࡴࡴࡳࡵࠢࡳࡣ࡮ࡴࡤࡦࡺࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠸࡝࡝ࡰࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰ࡶࡰ࡮ࡩࡥࠩ࠲࠯ࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹ࠩ࡝ࡰࡦࡳࡳࡹࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢࠪ࠽࡟ࡲ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡱࡧࡵ࡯ࡥ࡫ࠤࡂࠦࡡࡴࡻࡱࡧࠥ࠮࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸ࠯ࠠ࠾ࡀࠣࡿࡡࡴ࡬ࡦࡶࠣࡧࡦࡶࡳ࠼࡞ࡱࡸࡷࡿࠠࡼ࡞ࡱࡧࡦࡶࡳࠡ࠿ࠣࡎࡘࡕࡎ࠯ࡲࡤࡶࡸ࡫ࠨࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷ࠮ࡢ࡮ࠡࠢࢀࠤࡨࡧࡴࡤࡪࠫࡩࡽ࠯ࠠࡼ࡞ࡱࠤࠥࠦࠠࡾ࡞ࡱࠤࠥࡸࡥࡵࡷࡵࡲࠥࡧࡷࡢ࡫ࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡨࡵ࡮࡯ࡧࡦࡸ࠭ࢁ࡜࡯ࠢࠣࠤࠥࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵ࠼ࠣࡤࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂࠪࡻࡦࡰࡦࡳࡩ࡫ࡕࡓࡋࡆࡳࡲࡶ࡯࡯ࡧࡱࡸ࠭ࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡣࡢࡲࡶ࠭࠮ࢃࡠ࠭࡞ࡱࠤࠥࠦࠠ࠯࠰࠱ࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵ࡟ࡲࠥࠦࡽࠪ࡞ࡱࢁࡡࡴ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰࡞ࡱࠫ੆")
from ._version import __version__
bstack11l11ll1l_opy_ = None
CONFIG = {}
bstack1l111lll11_opy_ = {}
bstack1ll1lll1l_opy_ = {}
bstack11ll11111_opy_ = None
bstack1l1llll1l1_opy_ = None
bstack1lll111l11_opy_ = None
bstack1ll1l1l11l_opy_ = -1
bstack11ll11l11l_opy_ = 0
bstack1111ll1ll_opy_ = bstack11ll111ll1_opy_
bstack1ll11l1l1l_opy_ = 1
bstack11lll1111l_opy_ = False
bstack1l11ll11l_opy_ = False
bstack1l1ll111l1_opy_ = bstack1l1lll1_opy_ (u"࠭ࠧੇ")
bstack1111l11l1_opy_ = bstack1l1lll1_opy_ (u"ࠧࠨੈ")
bstack1l1lllllll_opy_ = False
bstack11lll11111_opy_ = True
bstack1111ll11ll_opy_ = bstack1l1lll1_opy_ (u"ࠨࠩ੉")
bstack1l11l1111l_opy_ = []
bstack1l1l1lll1l_opy_ = threading.Lock()
bstack1l11l1lll1_opy_ = threading.Lock()
bstack1l111lllll_opy_ = bstack1l1lll1_opy_ (u"ࠩࠪ੊")
bstack1l11l111l_opy_ = False
bstack1lll1l11ll_opy_ = None
bstack1ll1l1l1l1_opy_ = None
bstack1ll1lll1l1_opy_ = None
bstack1l1111l111_opy_ = -1
bstack11l1ll1l1l_opy_ = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠪࢂࠬੋ")), bstack1l1lll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫੌ"), bstack1l1lll1_opy_ (u"ࠬ࠴ࡲࡰࡤࡲࡸ࠲ࡸࡥࡱࡱࡵࡸ࠲࡮ࡥ࡭ࡲࡨࡶ࠳ࡰࡳࡰࡰ੍ࠪ"))
bstack1lll111lll_opy_ = 0
bstack1l11lll1ll_opy_ = 0
bstack11111l111_opy_ = []
bstack11111ll11_opy_ = []
bstack11llll11ll_opy_ = []
bstack1l11llll1l_opy_ = []
bstack11ll1lllll_opy_ = bstack1l1lll1_opy_ (u"࠭ࠧ੎")
bstack111ll1l111_opy_ = bstack1l1lll1_opy_ (u"ࠧࠨ੏")
bstack1llll1l11l_opy_ = False
bstack111l111l11_opy_ = False
bstack1ll1l1l1l_opy_ = {}
bstack1l111ll111_opy_ = None
bstack11ll11lll1_opy_ = None
bstack1llll11ll1_opy_ = None
bstack1l1l11111l_opy_ = None
bstack1l11ll1ll_opy_ = None
bstack1l11lll1l_opy_ = None
bstack1l1l11l1ll_opy_ = None
bstack11ll111111_opy_ = None
bstack11l11l111l_opy_ = None
bstack11l1ll1111_opy_ = None
bstack1l1ll1111_opy_ = None
bstack11lllll1l1_opy_ = None
bstack1l111111ll_opy_ = None
bstack11llll11l_opy_ = None
bstack1111l1ll1l_opy_ = None
bstack111l1llll1_opy_ = None
bstack1l11111l11_opy_ = None
bstack11l111l11l_opy_ = None
bstack111l1ll1l_opy_ = None
bstack11l111l1ll_opy_ = None
bstack1ll11111ll_opy_ = None
bstack1l11llllll_opy_ = None
bstack1l1111l11l_opy_ = None
thread_local = threading.local()
bstack111lllll1_opy_ = False
bstack1lll1llll1_opy_ = bstack1l1lll1_opy_ (u"ࠣࠤ੐")
logger = bstack111l11l1l_opy_.get_logger(__name__, bstack1111ll1ll_opy_)
bstack1111111l_opy_ = Config.bstack11l11l1l_opy_()
percy = bstack11ll111l1l_opy_()
bstack1l11l11l1l_opy_ = bstack1l1llllll_opy_()
bstack1l1ll1llll_opy_ = bstack11ll1l11_opy_()
def bstack1111l11ll1_opy_():
  global CONFIG
  global bstack1llll1l11l_opy_
  global bstack1111111l_opy_
  testContextOptions = bstack1l111l1ll1_opy_(CONFIG)
  if bstack1l1l1l1l1_opy_(CONFIG):
    if (bstack1l1lll1_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫੑ") in testContextOptions and str(testContextOptions[bstack1l1lll1_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ੒")]).lower() == bstack1l1lll1_opy_ (u"ࠫࡹࡸࡵࡦࠩ੓")):
      bstack1llll1l11l_opy_ = True
    bstack1111111l_opy_.bstack1l11111111_opy_(testContextOptions.get(bstack1l1lll1_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ੔"), False))
  else:
    bstack1llll1l11l_opy_ = True
    bstack1111111l_opy_.bstack1l11111111_opy_(True)
def bstack11ll1ll1l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1ll1ll11ll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1ll11l1l11_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1l1lll1_opy_ (u"ࠨ࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡣࡰࡰࡩ࡭࡬࡬ࡩ࡭ࡧࠥ੕") == args[i].lower() or bstack1l1lll1_opy_ (u"ࠢ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡲ࡫࡯ࡧࠣ੖") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1111ll11ll_opy_
      bstack1111ll11ll_opy_ += bstack1l1lll1_opy_ (u"ࠨ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡅࡲࡲ࡫࡯ࡧࡇ࡫࡯ࡩࠥ࠭੗") + shlex.quote(path)
      return path
  return None
bstack1ll1lll1ll_opy_ = re.compile(bstack1l1lll1_opy_ (u"ࡴࠥ࠲࠯ࡅ࡜ࠥࡽࠫ࠲࠯ࡅࠩࡾ࠰࠭ࡃࠧ੘"))
def bstack11ll1llll1_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1ll1lll1ll_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1l1lll1_opy_ (u"ࠥࠨࢀࠨਖ਼") + group + bstack1l1lll1_opy_ (u"ࠦࢂࠨਗ਼"), os.environ.get(group))
  return value
def bstack11l1llll1_opy_():
  global bstack1l1111l11l_opy_
  if bstack1l1111l11l_opy_ is None:
        bstack1l1111l11l_opy_ = bstack1ll11l1l11_opy_()
  bstack11111l1l1l_opy_ = bstack1l1111l11l_opy_
  if bstack11111l1l1l_opy_ and os.path.exists(os.path.abspath(bstack11111l1l1l_opy_)):
    fileName = bstack11111l1l1l_opy_
  if bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆࠩਜ਼") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࡤࡌࡉࡍࡇࠪੜ")])) and not bstack1l1lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡓࡧ࡭ࡦࠩ੝") in locals():
    fileName = os.environ[bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬਫ਼")]
  if bstack1l1lll1_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡎࡢ࡯ࡨࠫ੟") in locals():
    bstack11l1l_opy_ = os.path.abspath(fileName)
  else:
    bstack11l1l_opy_ = bstack1l1lll1_opy_ (u"ࠪࠫ੠")
  bstack11l1111ll_opy_ = os.getcwd()
  bstack1ll111llll_opy_ = bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧ੡")
  bstack1l1ll11111_opy_ = bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡧ࡭࡭ࠩ੢")
  while (not os.path.exists(bstack11l1l_opy_)) and bstack11l1111ll_opy_ != bstack1l1lll1_opy_ (u"ࠨࠢ੣"):
    bstack11l1l_opy_ = os.path.join(bstack11l1111ll_opy_, bstack1ll111llll_opy_)
    if not os.path.exists(bstack11l1l_opy_):
      bstack11l1l_opy_ = os.path.join(bstack11l1111ll_opy_, bstack1l1ll11111_opy_)
    if bstack11l1111ll_opy_ != os.path.dirname(bstack11l1111ll_opy_):
      bstack11l1111ll_opy_ = os.path.dirname(bstack11l1111ll_opy_)
    else:
      bstack11l1111ll_opy_ = bstack1l1lll1_opy_ (u"ࠢࠣ੤")
  bstack1l1111l11l_opy_ = bstack11l1l_opy_ if os.path.exists(bstack11l1l_opy_) else None
  return bstack1l1111l11l_opy_
def bstack11l1l1l11l_opy_(config):
    if bstack1l1lll1_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࠨ੥") in config:
      config[bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭੦")] = config[bstack1l1lll1_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࠪ੧")]
    if bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࡓࡵࡺࡩࡰࡰࡶࠫ੨") in config:
      config[bstack1l1lll1_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ੩")] = config[bstack1l1lll1_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬ࡕࡰࡵ࡫ࡲࡲࡸ࠭੪")]
def bstack111l1l111_opy_():
  bstack11l1l_opy_ = bstack11l1llll1_opy_()
  if not os.path.exists(bstack11l1l_opy_):
    bstack1l111ll1l1_opy_(
      bstack1ll111ll1l_opy_.format(os.getcwd()))
  try:
    with open(bstack11l1l_opy_, bstack1l1lll1_opy_ (u"ࠧࡳࠩ੫")) as stream:
      yaml.add_implicit_resolver(bstack1l1lll1_opy_ (u"ࠣࠣࡳࡥࡹ࡮ࡥࡹࠤ੬"), bstack1ll1lll1ll_opy_)
      yaml.add_constructor(bstack1l1lll1_opy_ (u"ࠤࠤࡴࡦࡺࡨࡦࡺࠥ੭"), bstack11ll1llll1_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack11l1l1l11l_opy_(config)
      return config
  except:
    with open(bstack11l1l_opy_, bstack1l1lll1_opy_ (u"ࠪࡶࠬ੮")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack11l1l1l11l_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1l111ll1l1_opy_(bstack1lll11l111_opy_.format(str(exc)))
def bstack11l1l11lll_opy_(config):
  bstack11lll1lll1_opy_ = bstack1lll1lll1l_opy_(config)
  for option in list(bstack11lll1lll1_opy_):
    if option.lower() in bstack111l11l11_opy_ and option != bstack111l11l11_opy_[option.lower()]:
      bstack11lll1lll1_opy_[bstack111l11l11_opy_[option.lower()]] = bstack11lll1lll1_opy_[option]
      del bstack11lll1lll1_opy_[option]
  return config
def bstack1l11l1l111_opy_():
  global bstack1ll1lll1l_opy_
  for key, bstack11l1ll111l_opy_ in bstack11l1l1ll1_opy_.items():
    if isinstance(bstack11l1ll111l_opy_, list):
      for var in bstack11l1ll111l_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1ll1lll1l_opy_[key] = os.environ[var]
          break
    elif bstack11l1ll111l_opy_ in os.environ and os.environ[bstack11l1ll111l_opy_] and str(os.environ[bstack11l1ll111l_opy_]).strip():
      bstack1ll1lll1l_opy_[key] = os.environ[bstack11l1ll111l_opy_]
  if bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭੯") in os.environ:
    bstack1ll1lll1l_opy_[bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩੰ")] = {}
    bstack1ll1lll1l_opy_[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪੱ")][bstack1l1lll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩੲ")] = os.environ[bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪੳ")]
def bstack1ll1111111_opy_():
  global bstack1l111lll11_opy_
  global bstack1111ll11ll_opy_
  bstack1lll1lllll_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack1l1lll1_opy_ (u"ࠩ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬੴ").lower() == val.lower():
      bstack1l111lll11_opy_[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧੵ")] = {}
      bstack1l111lll11_opy_[bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੶")][bstack1l1lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ੷")] = sys.argv[idx + 1]
      bstack1lll1lllll_opy_.extend([idx, idx + 1])
      break
  for key, bstack11l11lll1_opy_ in bstack11ll1l111_opy_.items():
    if isinstance(bstack11l11lll1_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack11l11lll1_opy_:
          if bstack1l1lll1_opy_ (u"࠭࠭࠮ࠩ੸") + var.lower() == val.lower() and key not in bstack1l111lll11_opy_:
            bstack1l111lll11_opy_[key] = sys.argv[idx + 1]
            bstack1111ll11ll_opy_ += bstack1l1lll1_opy_ (u"ࠧࠡ࠯࠰ࠫ੹") + var + bstack1l1lll1_opy_ (u"ࠨࠢࠪ੺") + shlex.quote(sys.argv[idx + 1])
            bstack1lll1lllll_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack1l1lll1_opy_ (u"ࠩ࠰࠱ࠬ੻") + bstack11l11lll1_opy_.lower() == val.lower() and key not in bstack1l111lll11_opy_:
          bstack1l111lll11_opy_[key] = sys.argv[idx + 1]
          bstack1111ll11ll_opy_ += bstack1l1lll1_opy_ (u"ࠪࠤ࠲࠳ࠧ੼") + bstack11l11lll1_opy_ + bstack1l1lll1_opy_ (u"ࠫࠥ࠭੽") + shlex.quote(sys.argv[idx + 1])
          bstack1lll1lllll_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack1lll1lllll_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack11l1l1llll_opy_(config):
  bstack1l11l1ll11_opy_ = config.keys()
  for bstack111ll1l1l1_opy_, bstack1111lllll_opy_ in bstack11111l1ll_opy_.items():
    if bstack1111lllll_opy_ in bstack1l11l1ll11_opy_:
      config[bstack111ll1l1l1_opy_] = config[bstack1111lllll_opy_]
      del config[bstack1111lllll_opy_]
  for bstack111ll1l1l1_opy_, bstack1111lllll_opy_ in bstack111l1l1l1l_opy_.items():
    if isinstance(bstack1111lllll_opy_, list):
      for bstack111lll1ll1_opy_ in bstack1111lllll_opy_:
        if bstack111lll1ll1_opy_ in bstack1l11l1ll11_opy_:
          config[bstack111ll1l1l1_opy_] = config[bstack111lll1ll1_opy_]
          del config[bstack111lll1ll1_opy_]
          break
    elif bstack1111lllll_opy_ in bstack1l11l1ll11_opy_:
      config[bstack111ll1l1l1_opy_] = config[bstack1111lllll_opy_]
      del config[bstack1111lllll_opy_]
  for bstack111lll1ll1_opy_ in list(config):
    for bstack111ll1llll_opy_ in bstack1ll1l11l1l_opy_:
      if bstack111lll1ll1_opy_.lower() == bstack111ll1llll_opy_.lower() and bstack111lll1ll1_opy_ != bstack111ll1llll_opy_:
        config[bstack111ll1llll_opy_] = config[bstack111lll1ll1_opy_]
        del config[bstack111lll1ll1_opy_]
  bstack111l1111l1_opy_ = [{}]
  if not config.get(bstack1l1lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ੾")):
    config[bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ੿")] = [{}]
  bstack111l1111l1_opy_ = config[bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ઀")]
  for platform in bstack111l1111l1_opy_:
    for bstack111lll1ll1_opy_ in list(platform):
      for bstack111ll1llll_opy_ in bstack1ll1l11l1l_opy_:
        if bstack111lll1ll1_opy_.lower() == bstack111ll1llll_opy_.lower() and bstack111lll1ll1_opy_ != bstack111ll1llll_opy_:
          platform[bstack111ll1llll_opy_] = platform[bstack111lll1ll1_opy_]
          del platform[bstack111lll1ll1_opy_]
  for bstack111ll1l1l1_opy_, bstack1111lllll_opy_ in bstack111l1l1l1l_opy_.items():
    for platform in bstack111l1111l1_opy_:
      if isinstance(bstack1111lllll_opy_, list):
        for bstack111lll1ll1_opy_ in bstack1111lllll_opy_:
          if bstack111lll1ll1_opy_ in platform:
            platform[bstack111ll1l1l1_opy_] = platform[bstack111lll1ll1_opy_]
            del platform[bstack111lll1ll1_opy_]
            break
      elif bstack1111lllll_opy_ in platform:
        platform[bstack111ll1l1l1_opy_] = platform[bstack1111lllll_opy_]
        del platform[bstack1111lllll_opy_]
  for bstack1lll1ll1l1_opy_ in bstack1ll11lll11_opy_:
    if bstack1lll1ll1l1_opy_ in config:
      if not bstack1ll11lll11_opy_[bstack1lll1ll1l1_opy_] in config:
        config[bstack1ll11lll11_opy_[bstack1lll1ll1l1_opy_]] = {}
      config[bstack1ll11lll11_opy_[bstack1lll1ll1l1_opy_]].update(config[bstack1lll1ll1l1_opy_])
      del config[bstack1lll1ll1l1_opy_]
  for platform in bstack111l1111l1_opy_:
    for bstack1lll1ll1l1_opy_ in bstack1ll11lll11_opy_:
      if bstack1lll1ll1l1_opy_ in list(platform):
        if not bstack1ll11lll11_opy_[bstack1lll1ll1l1_opy_] in platform:
          platform[bstack1ll11lll11_opy_[bstack1lll1ll1l1_opy_]] = {}
        platform[bstack1ll11lll11_opy_[bstack1lll1ll1l1_opy_]].update(platform[bstack1lll1ll1l1_opy_])
        del platform[bstack1lll1ll1l1_opy_]
  config = bstack11l1l11lll_opy_(config)
  return config
def bstack1ll11llll_opy_(config):
  global bstack1111l11l1_opy_
  bstack111111l1l_opy_ = False
  if bstack1l1lll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬઁ") in config and str(config[bstack1l1lll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ં")]).lower() != bstack1l1lll1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩઃ"):
    if bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ઄") not in config or str(config[bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩઅ")]).lower() == bstack1l1lll1_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬઆ"):
      config[bstack1l1lll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭ઇ")] = False
    else:
      bstack1l1lll111_opy_ = bstack1ll1l11ll1_opy_()
      if bstack1l1lll1_opy_ (u"ࠨ࡫ࡶࡘࡷ࡯ࡡ࡭ࡉࡵ࡭ࡩ࠭ઈ") in bstack1l1lll111_opy_:
        if not bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઉ") in config:
          config[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઊ")] = {}
        config[bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨઋ")][bstack1l1lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઌ")] = bstack1l1lll1_opy_ (u"࠭ࡡࡵࡵ࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠬઍ")
        bstack111111l1l_opy_ = True
        bstack1111l11l1_opy_ = config[bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ઎")].get(bstack1l1lll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪએ"))
  if bstack1l1l1l1l1_opy_(config) and bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ઐ") in config and str(config[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧઑ")]).lower() != bstack1l1lll1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ઒") and not bstack111111l1l_opy_:
    if not bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩઓ") in config:
      config[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪઔ")] = {}
    if not config[bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫક")].get(bstack1l1lll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡈࡩ࡯ࡣࡵࡽࡎࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡡࡵ࡫ࡲࡲࠬખ")) and not bstack1l1lll1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫગ") in config[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઘ")]:
      bstack1ll1llll_opy_ = datetime.datetime.now()
      bstack11llllll11_opy_ = bstack1ll1llll_opy_.strftime(bstack1l1lll1_opy_ (u"ࠫࠪࡪ࡟ࠦࡤࡢࠩࡍࠫࡍࠨઙ"))
      hostname = socket.gethostname()
      bstack1l111l1l1l_opy_ = bstack1l1lll1_opy_ (u"ࠬ࠭ચ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1l1lll1_opy_ (u"࠭ࡻࡾࡡࡾࢁࡤࢁࡽࠨછ").format(bstack11llllll11_opy_, hostname, bstack1l111l1l1l_opy_)
      config[bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫજ")][bstack1l1lll1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪઝ")] = identifier
    bstack1111l11l1_opy_ = config[bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઞ")].get(bstack1l1lll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬટ"))
  return config
def bstack1l1l1111l_opy_():
  bstack1111ll111_opy_ =  bstack11lll11l11_opy_()[bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠪઠ")]
  return bstack1111ll111_opy_ if bstack1111ll111_opy_ else -1
def bstack1l1111ll1_opy_(bstack1111ll111_opy_):
  global CONFIG
  if not bstack1l1lll1_opy_ (u"ࠬࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧડ") in CONFIG[bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨઢ")]:
    return
  CONFIG[bstack1l1lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩણ")] = CONFIG[bstack1l1lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪત")].replace(
    bstack1l1lll1_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫથ"),
    str(bstack1111ll111_opy_)
  )
def bstack11lll1l11_opy_():
  global CONFIG
  if not bstack1l1lll1_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩદ") in CONFIG[bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ધ")]:
    return
  bstack1ll1llll_opy_ = datetime.datetime.now()
  bstack11llllll11_opy_ = bstack1ll1llll_opy_.strftime(bstack1l1lll1_opy_ (u"ࠬࠫࡤ࠮ࠧࡥ࠱ࠪࡎ࠺ࠦࡏࠪન"))
  CONFIG[bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ઩")] = CONFIG[bstack1l1lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩપ")].replace(
    bstack1l1lll1_opy_ (u"ࠨࠦࡾࡈࡆ࡚ࡅࡠࡖࡌࡑࡊࢃࠧફ"),
    bstack11llllll11_opy_
  )
def bstack1lll11ll1_opy_():
  global CONFIG
  if bstack1l1lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫબ") in CONFIG and not bool(CONFIG[bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬભ")]):
    del CONFIG[bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭મ")]
    return
  if not bstack1l1lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧય") in CONFIG:
    CONFIG[bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨર")] = bstack1l1lll1_opy_ (u"ࠧࠤࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪ઱")
  if bstack1l1lll1_opy_ (u"ࠨࠦࡾࡈࡆ࡚ࡅࡠࡖࡌࡑࡊࢃࠧલ") in CONFIG[bstack1l1lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫળ")]:
    bstack11lll1l11_opy_()
    os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧ઴")] = CONFIG[bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭વ")]
  if not bstack1l1lll1_opy_ (u"ࠬࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧશ") in CONFIG[bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨષ")]:
    return
  bstack1111ll111_opy_ = bstack1l1lll1_opy_ (u"ࠧࠨસ")
  bstack11ll1lll1_opy_ = bstack1l1l1111l_opy_()
  if bstack11ll1lll1_opy_ != -1:
    bstack1111ll111_opy_ = bstack1l1lll1_opy_ (u"ࠨࡅࡌࠤࠬહ") + str(bstack11ll1lll1_opy_)
  if bstack1111ll111_opy_ == bstack1l1lll1_opy_ (u"ࠩࠪ઺"):
    bstack1l1ll1111l_opy_ = bstack111lll11ll_opy_(CONFIG[bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭઻")])
    if bstack1l1ll1111l_opy_ != -1:
      bstack1111ll111_opy_ = str(bstack1l1ll1111l_opy_)
  if bstack1111ll111_opy_:
    bstack1l1111ll1_opy_(bstack1111ll111_opy_)
    os.environ[bstack1l1lll1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨ઼")] = CONFIG[bstack1l1lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઽ")]
def bstack1l11l111ll_opy_(bstack11l11ll1l1_opy_, bstack111lllllll_opy_, path):
  json_data = {
    bstack1l1lll1_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪા"): bstack111lllllll_opy_
  }
  if os.path.exists(path):
    bstack1l11l1ll1l_opy_ = json.load(open(path, bstack1l1lll1_opy_ (u"ࠧࡳࡤࠪિ")))
  else:
    bstack1l11l1ll1l_opy_ = {}
  bstack1l11l1ll1l_opy_[bstack11l11ll1l1_opy_] = json_data
  with open(path, bstack1l1lll1_opy_ (u"ࠣࡹ࠮ࠦી")) as outfile:
    json.dump(bstack1l11l1ll1l_opy_, outfile)
def bstack111lll11ll_opy_(bstack11l11ll1l1_opy_):
  bstack11l11ll1l1_opy_ = str(bstack11l11ll1l1_opy_)
  bstack111l1lll1l_opy_ = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠩࢁࠫુ")), bstack1l1lll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪૂ"))
  try:
    if not os.path.exists(bstack111l1lll1l_opy_):
      os.makedirs(bstack111l1lll1l_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠫࢃ࠭ૃ")), bstack1l1lll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬૄ"), bstack1l1lll1_opy_ (u"࠭࠮ࡣࡷ࡬ࡰࡩ࠳࡮ࡢ࡯ࡨ࠱ࡨࡧࡣࡩࡧ࠱࡮ࡸࡵ࡮ࠨૅ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1l1lll1_opy_ (u"ࠧࡸࠩ૆")):
        pass
      with open(file_path, bstack1l1lll1_opy_ (u"ࠣࡹ࠮ࠦે")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1l1lll1_opy_ (u"ࠩࡵࠫૈ")) as bstack11l1ll1ll_opy_:
      bstack111llll111_opy_ = json.load(bstack11l1ll1ll_opy_)
    if bstack11l11ll1l1_opy_ in bstack111llll111_opy_:
      bstack11l11l111_opy_ = bstack111llll111_opy_[bstack11l11ll1l1_opy_][bstack1l1lll1_opy_ (u"ࠪ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૉ")]
      bstack1l111111l1_opy_ = int(bstack11l11l111_opy_) + 1
      bstack1l11l111ll_opy_(bstack11l11ll1l1_opy_, bstack1l111111l1_opy_, file_path)
      return bstack1l111111l1_opy_
    else:
      bstack1l11l111ll_opy_(bstack11l11ll1l1_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1ll111l111_opy_.format(str(e)))
    return -1
def bstack1l1l1ll111_opy_(config):
  if not config[bstack1l1lll1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭૊")] or not config[bstack1l1lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨો")]:
    return True
  else:
    return False
def bstack1lll1ll11l_opy_(config, index=0):
  global bstack1l1lllllll_opy_
  bstack1l1l1l11ll_opy_ = {}
  caps = bstack11l11l1l1l_opy_ + bstack1ll11111l_opy_
  if config.get(bstack1l1lll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪૌ"), False):
    bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨ્ࠫ")] = True
    bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷࠬ૎")] = config.get(bstack1l1lll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭૏"), {})
  if bstack1l1lllllll_opy_:
    caps += bstack1llllll11l_opy_
  for key in config:
    if key in caps + [bstack1l1lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ૐ")]:
      continue
    bstack1l1l1l11ll_opy_[key] = config[key]
  if bstack1l1lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૑") in config:
    for bstack11ll111lll_opy_ in config[bstack1l1lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૒")][index]:
      if bstack11ll111lll_opy_ in caps:
        continue
      bstack1l1l1l11ll_opy_[bstack11ll111lll_opy_] = config[bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૓")][index][bstack11ll111lll_opy_]
  bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠧࡩࡱࡶࡸࡓࡧ࡭ࡦࠩ૔")] = socket.gethostname()
  if bstack1l1lll1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ૕") in bstack1l1l1l11ll_opy_:
    del (bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ૖")])
  return bstack1l1l1l11ll_opy_
def bstack1lll11l11l_opy_(config):
  global bstack1l1lllllll_opy_
  bstack1ll11l1ll_opy_ = {}
  caps = bstack1ll11111l_opy_
  if bstack1l1lllllll_opy_:
    caps += bstack1llllll11l_opy_
  for key in caps:
    if key in config:
      bstack1ll11l1ll_opy_[key] = config[key]
  return bstack1ll11l1ll_opy_
def bstack1l1l1llll1_opy_(bstack1l1l1l11ll_opy_, bstack1ll11l1ll_opy_):
  bstack1lllllll1l_opy_ = {}
  for key in bstack1l1l1l11ll_opy_.keys():
    if key in bstack11111l1ll_opy_:
      bstack1lllllll1l_opy_[bstack11111l1ll_opy_[key]] = bstack1l1l1l11ll_opy_[key]
    else:
      bstack1lllllll1l_opy_[key] = bstack1l1l1l11ll_opy_[key]
  for key in bstack1ll11l1ll_opy_:
    if key in bstack11111l1ll_opy_:
      bstack1lllllll1l_opy_[bstack11111l1ll_opy_[key]] = bstack1ll11l1ll_opy_[key]
    else:
      bstack1lllllll1l_opy_[key] = bstack1ll11l1ll_opy_[key]
  return bstack1lllllll1l_opy_
def bstack1lll11l1l1_opy_(config, index=0):
  global bstack1l1lllllll_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack111l1ll1l1_opy_ = bstack1l111l1111_opy_(bstack1l11l111l1_opy_, config, logger)
  bstack1ll11l1ll_opy_ = bstack1lll11l11l_opy_(config)
  bstack1l1l1lllll_opy_ = bstack1ll11111l_opy_
  bstack1l1l1lllll_opy_ += bstack11lll111ll_opy_
  bstack1ll11l1ll_opy_ = update(bstack1ll11l1ll_opy_, bstack111l1ll1l1_opy_)
  if bstack1l1lllllll_opy_:
    bstack1l1l1lllll_opy_ += bstack1llllll11l_opy_
  if bstack1l1lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૗") in config:
    if bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ૘") in config[bstack1l1lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૙")][index]:
      caps[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ૚")] = config[bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૛")][index][bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭૜")]
    if bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ૝") in config[bstack1l1lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૞")][index]:
      caps[bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ૟")] = str(config[bstack1l1lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૠ")][index][bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧૡ")])
    bstack111ll1ll1_opy_ = bstack1l111l1111_opy_(bstack1l11l111l1_opy_, config[bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪૢ")][index], logger)
    bstack1l1l1lllll_opy_ += list(bstack111ll1ll1_opy_.keys())
    for bstack11lllllll1_opy_ in bstack1l1l1lllll_opy_:
      if bstack11lllllll1_opy_ in config[bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫૣ")][index]:
        if bstack11lllllll1_opy_ == bstack1l1lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ૤"):
          try:
            bstack111ll1ll1_opy_[bstack11lllllll1_opy_] = str(config[bstack1l1lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૥")][index][bstack11lllllll1_opy_] * 1.0)
          except:
            bstack111ll1ll1_opy_[bstack11lllllll1_opy_] = str(config[bstack1l1lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૦")][index][bstack11lllllll1_opy_])
        else:
          bstack111ll1ll1_opy_[bstack11lllllll1_opy_] = config[bstack1l1lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૧")][index][bstack11lllllll1_opy_]
        del (config[bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૨")][index][bstack11lllllll1_opy_])
    bstack1ll11l1ll_opy_ = update(bstack1ll11l1ll_opy_, bstack111ll1ll1_opy_)
  bstack1l1l1l11ll_opy_ = bstack1lll1ll11l_opy_(config, index)
  for bstack111lll1ll1_opy_ in bstack1ll11111l_opy_ + list(bstack111l1ll1l1_opy_.keys()):
    if bstack111lll1ll1_opy_ in bstack1l1l1l11ll_opy_:
      bstack1ll11l1ll_opy_[bstack111lll1ll1_opy_] = bstack1l1l1l11ll_opy_[bstack111lll1ll1_opy_]
      del (bstack1l1l1l11ll_opy_[bstack111lll1ll1_opy_])
  if bstack1111lll1l1_opy_(config):
    bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧ૩")] = True
    caps.update(bstack1ll11l1ll_opy_)
    caps[bstack1l1lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ૪")] = bstack1l1l1l11ll_opy_
  else:
    bstack1l1l1l11ll_opy_[bstack1l1lll1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩ૫")] = False
    caps.update(bstack1l1l1llll1_opy_(bstack1l1l1l11ll_opy_, bstack1ll11l1ll_opy_))
    if bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ૬") in caps:
      caps[bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬ૭")] = caps[bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ૮")]
      del (caps[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ૯")])
    if bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ૰") in caps:
      caps[bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ૱")] = caps[bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ૲")]
      del (caps[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ૳")])
  return caps
def bstack111ll1ll1l_opy_():
  global bstack1l111lllll_opy_
  global CONFIG
  if bstack1ll1ll11ll_opy_() <= version.parse(bstack1l1lll1_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫ૴")):
    if bstack1l111lllll_opy_ != bstack1l1lll1_opy_ (u"ࠬ࠭૵"):
      return bstack1l1lll1_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢ૶") + bstack1l111lllll_opy_ + bstack1l1lll1_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦ૷")
    return bstack111lllll11_opy_
  if bstack1l111lllll_opy_ != bstack1l1lll1_opy_ (u"ࠨࠩ૸"):
    return bstack1l1lll1_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦૹ") + bstack1l111lllll_opy_ + bstack1l1lll1_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦૺ")
  return bstack1111llll11_opy_
def bstack11ll11ll11_opy_(options):
  return hasattr(options, bstack1l1lll1_opy_ (u"ࠫࡸ࡫ࡴࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷࡽࠬૻ"))
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
def bstack111l1ll111_opy_(options, bstack11ll1l111l_opy_):
  for bstack1ll1l1lll_opy_ in bstack11ll1l111l_opy_:
    if bstack1ll1l1lll_opy_ in [bstack1l1lll1_opy_ (u"ࠬࡧࡲࡨࡵࠪૼ"), bstack1l1lll1_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ૽")]:
      continue
    if bstack1ll1l1lll_opy_ in options._experimental_options:
      options._experimental_options[bstack1ll1l1lll_opy_] = update(options._experimental_options[bstack1ll1l1lll_opy_],
                                                         bstack11ll1l111l_opy_[bstack1ll1l1lll_opy_])
    else:
      options.add_experimental_option(bstack1ll1l1lll_opy_, bstack11ll1l111l_opy_[bstack1ll1l1lll_opy_])
  if bstack1l1lll1_opy_ (u"ࠧࡢࡴࡪࡷࠬ૾") in bstack11ll1l111l_opy_:
    for arg in bstack11ll1l111l_opy_[bstack1l1lll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭૿")]:
      options.add_argument(arg)
    del (bstack11ll1l111l_opy_[bstack1l1lll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ଀")])
  if bstack1l1lll1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧଁ") in bstack11ll1l111l_opy_:
    for ext in bstack11ll1l111l_opy_[bstack1l1lll1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨଂ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack11ll1l111l_opy_[bstack1l1lll1_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩଃ")])
def bstack1l1l1ll11_opy_(options, bstack11111l1ll1_opy_):
  if bstack1l1lll1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ଄") in bstack11111l1ll1_opy_:
    for bstack11llll1l11_opy_ in bstack11111l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ଅ")]:
      if bstack11llll1l11_opy_ in options._preferences:
        options._preferences[bstack11llll1l11_opy_] = update(options._preferences[bstack11llll1l11_opy_], bstack11111l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧଆ")][bstack11llll1l11_opy_])
      else:
        options.set_preference(bstack11llll1l11_opy_, bstack11111l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨଇ")][bstack11llll1l11_opy_])
  if bstack1l1lll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଈ") in bstack11111l1ll1_opy_:
    for arg in bstack11111l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠫࡦࡸࡧࡴࠩଉ")]:
      options.add_argument(arg)
def bstack11l111lll1_opy_(options, bstack11l1111l11_opy_):
  if bstack1l1lll1_opy_ (u"ࠬࡽࡥࡣࡸ࡬ࡩࡼ࠭ଊ") in bstack11l1111l11_opy_:
    options.use_webview(bool(bstack11l1111l11_opy_[bstack1l1lll1_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࠧଋ")]))
  bstack111l1ll111_opy_(options, bstack11l1111l11_opy_)
def bstack1ll111l1ll_opy_(options, bstack11111ll111_opy_):
  for bstack11111ll11l_opy_ in bstack11111ll111_opy_:
    if bstack11111ll11l_opy_ in [bstack1l1lll1_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫଌ"), bstack1l1lll1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭଍")]:
      continue
    options.set_capability(bstack11111ll11l_opy_, bstack11111ll111_opy_[bstack11111ll11l_opy_])
  if bstack1l1lll1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ଎") in bstack11111ll111_opy_:
    for arg in bstack11111ll111_opy_[bstack1l1lll1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଏ")]:
      options.add_argument(arg)
  if bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨଐ") in bstack11111ll111_opy_:
    options.bstack1ll1lllll_opy_(bool(bstack11111ll111_opy_[bstack1l1lll1_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩ଑")]))
def bstack1l1ll1l1ll_opy_(options, bstack1ll1l1lll1_opy_):
  for bstack11l111111_opy_ in bstack1ll1l1lll1_opy_:
    if bstack11l111111_opy_ in [bstack1l1lll1_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ଒"), bstack1l1lll1_opy_ (u"ࠧࡢࡴࡪࡷࠬଓ")]:
      continue
    options._options[bstack11l111111_opy_] = bstack1ll1l1lll1_opy_[bstack11l111111_opy_]
  if bstack1l1lll1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬଔ") in bstack1ll1l1lll1_opy_:
    for bstack11ll11l1l1_opy_ in bstack1ll1l1lll1_opy_[bstack1l1lll1_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭କ")]:
      options.bstack1l11l1l1l1_opy_(
        bstack11ll11l1l1_opy_, bstack1ll1l1lll1_opy_[bstack1l1lll1_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧଖ")][bstack11ll11l1l1_opy_])
  if bstack1l1lll1_opy_ (u"ࠫࡦࡸࡧࡴࠩଗ") in bstack1ll1l1lll1_opy_:
    for arg in bstack1ll1l1lll1_opy_[bstack1l1lll1_opy_ (u"ࠬࡧࡲࡨࡵࠪଘ")]:
      options.add_argument(arg)
def bstack1l1l11l11_opy_(options, caps):
  if not hasattr(options, bstack1l1lll1_opy_ (u"࠭ࡋࡆ࡛ࠪଙ")):
    return
  if options.KEY == bstack1l1lll1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬଚ"):
    options = bstack1lll1ll1l_opy_.bstack111lllll1l_opy_(bstack1111l1llll_opy_=options, config=CONFIG)
  if options.KEY == bstack1l1lll1_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ଛ") and options.KEY in caps:
    bstack111l1ll111_opy_(options, caps[bstack1l1lll1_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧଜ")])
  elif options.KEY == bstack1l1lll1_opy_ (u"ࠪࡱࡴࢀ࠺ࡧ࡫ࡵࡩ࡫ࡵࡸࡐࡲࡷ࡭ࡴࡴࡳࠨଝ") and options.KEY in caps:
    bstack1l1l1ll11_opy_(options, caps[bstack1l1lll1_opy_ (u"ࠫࡲࡵࡺ࠻ࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩଞ")])
  elif options.KEY == bstack1l1lll1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭ଟ") and options.KEY in caps:
    bstack1ll111l1ll_opy_(options, caps[bstack1l1lll1_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧଠ")])
  elif options.KEY == bstack1l1lll1_opy_ (u"ࠧ࡮ࡵ࠽ࡩࡩ࡭ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨଡ") and options.KEY in caps:
    bstack11l111lll1_opy_(options, caps[bstack1l1lll1_opy_ (u"ࠨ࡯ࡶ࠾ࡪࡪࡧࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩଢ")])
  elif options.KEY == bstack1l1lll1_opy_ (u"ࠩࡶࡩ࠿࡯ࡥࡐࡲࡷ࡭ࡴࡴࡳࠨଣ") and options.KEY in caps:
    bstack1l1ll1l1ll_opy_(options, caps[bstack1l1lll1_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩତ")])
def bstack11ll11l111_opy_(caps):
  global bstack1l1lllllll_opy_
  if isinstance(os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬଥ")), str):
    bstack1l1lllllll_opy_ = eval(os.getenv(bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ଦ")))
  if bstack1l1lllllll_opy_:
    if bstack11ll1ll1l_opy_() < version.parse(bstack1l1lll1_opy_ (u"࠭࠲࠯࠵࠱࠴ࠬଧ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1l1lll1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧନ")
    if bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭଩") in caps:
      browser = caps[bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧପ")]
    elif bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫଫ") in caps:
      browser = caps[bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬବ")]
    browser = str(browser).lower()
    if browser == bstack1l1lll1_opy_ (u"ࠬ࡯ࡰࡩࡱࡱࡩࠬଭ") or browser == bstack1l1lll1_opy_ (u"࠭ࡩࡱࡣࡧࠫମ"):
      browser = bstack1l1lll1_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧଯ")
    if browser == bstack1l1lll1_opy_ (u"ࠨࡵࡤࡱࡸࡻ࡮ࡨࠩର"):
      browser = bstack1l1lll1_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩ଱")
    if browser not in [bstack1l1lll1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪଲ"), bstack1l1lll1_opy_ (u"ࠫࡪࡪࡧࡦࠩଳ"), bstack1l1lll1_opy_ (u"ࠬ࡯ࡥࠨ଴"), bstack1l1lll1_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭ଵ"), bstack1l1lll1_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨଶ")]:
      return None
    try:
      package = bstack1l1lll1_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯࠱ࡻࡪࡨࡤࡳ࡫ࡹࡩࡷ࠴ࡻࡾ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪଷ").format(browser)
      name = bstack1l1lll1_opy_ (u"ࠩࡒࡴࡹ࡯࡯࡯ࡵࠪସ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11ll11ll11_opy_(options):
        return None
      for bstack111lll1ll1_opy_ in caps.keys():
        options.set_capability(bstack111lll1ll1_opy_, caps[bstack111lll1ll1_opy_])
      bstack1l1l11l11_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack111l1l11l_opy_(options, bstack1l1l11111_opy_):
  if not bstack11ll11ll11_opy_(options):
    return
  for bstack111lll1ll1_opy_ in bstack1l1l11111_opy_.keys():
    if bstack111lll1ll1_opy_ in bstack11lll111ll_opy_:
      continue
    if bstack111lll1ll1_opy_ in options._caps and type(options._caps[bstack111lll1ll1_opy_]) in [dict, list]:
      options._caps[bstack111lll1ll1_opy_] = update(options._caps[bstack111lll1ll1_opy_], bstack1l1l11111_opy_[bstack111lll1ll1_opy_])
    else:
      options.set_capability(bstack111lll1ll1_opy_, bstack1l1l11111_opy_[bstack111lll1ll1_opy_])
  bstack1l1l11l11_opy_(options, bstack1l1l11111_opy_)
  if bstack1l1lll1_opy_ (u"ࠪࡱࡴࢀ࠺ࡥࡧࡥࡹ࡬࡭ࡥࡳࡃࡧࡨࡷ࡫ࡳࡴࠩହ") in options._caps:
    if options._caps[bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ଺")] and options._caps[bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ଻")].lower() != bstack1l1lll1_opy_ (u"࠭ࡦࡪࡴࡨࡪࡴࡾ଼ࠧ"):
      del options._caps[bstack1l1lll1_opy_ (u"ࠧ࡮ࡱࡽ࠾ࡩ࡫ࡢࡶࡩࡪࡩࡷࡇࡤࡥࡴࡨࡷࡸ࠭ଽ")]
def bstack1111lll11_opy_(proxy_config):
  if bstack1l1lll1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬା") in proxy_config:
    proxy_config[bstack1l1lll1_opy_ (u"ࠩࡶࡷࡱࡖࡲࡰࡺࡼࠫି")] = proxy_config[bstack1l1lll1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧୀ")]
    del (proxy_config[bstack1l1lll1_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨୁ")])
  if bstack1l1lll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨୂ") in proxy_config and proxy_config[bstack1l1lll1_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩୃ")].lower() != bstack1l1lll1_opy_ (u"ࠧࡥ࡫ࡵࡩࡨࡺࠧୄ"):
    proxy_config[bstack1l1lll1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ୅")] = bstack1l1lll1_opy_ (u"ࠩࡰࡥࡳࡻࡡ࡭ࠩ୆")
  if bstack1l1lll1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡃࡸࡸࡴࡩ࡯࡯ࡨ࡬࡫࡚ࡸ࡬ࠨେ") in proxy_config:
    proxy_config[bstack1l1lll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧୈ")] = bstack1l1lll1_opy_ (u"ࠬࡶࡡࡤࠩ୉")
  return proxy_config
def bstack11l111ll11_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1l1lll1_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୊") in config:
    return proxy
  config[bstack1l1lll1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭ୋ")] = bstack1111lll11_opy_(config[bstack1l1lll1_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧୌ")])
  if proxy == None:
    proxy = Proxy(config[bstack1l1lll1_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨ୍")])
  return proxy
def bstack111l11lll_opy_(self):
  global CONFIG
  global bstack11lllll1l1_opy_
  try:
    proxy = bstack11lll11ll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1l1lll1_opy_ (u"ࠪ࠲ࡵࡧࡣࠨ୎")):
        proxies = bstack11l111llll_opy_(proxy, bstack111ll1ll1l_opy_())
        if len(proxies) > 0:
          protocol, bstack11l1llll1l_opy_ = proxies.popitem()
          if bstack1l1lll1_opy_ (u"ࠦ࠿࠵࠯ࠣ୏") in bstack11l1llll1l_opy_:
            return bstack11l1llll1l_opy_
          else:
            return bstack1l1lll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨ୐") + bstack11l1llll1l_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1l1lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡳࡶࡴࡾࡹࠡࡷࡵࡰࠥࡀࠠࡼࡿࠥ୑").format(str(e)))
  return bstack11lllll1l1_opy_(self)
def bstack1l1l1llll_opy_():
  global CONFIG
  return bstack1lll11lll1_opy_(CONFIG) and bstack111l1l11ll_opy_() and bstack1ll1ll11ll_opy_() >= version.parse(bstack11ll1l1ll_opy_)
def bstack1ll1l11l1_opy_():
  global CONFIG
  return (bstack1l1lll1_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪ୒") in CONFIG or bstack1l1lll1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ୓") in CONFIG) and bstack1l11l1l1l_opy_()
def bstack1lll1lll1l_opy_(config):
  bstack11lll1lll1_opy_ = {}
  if bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୔") in config:
    bstack11lll1lll1_opy_ = config[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ୕")]
  if bstack1l1lll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪୖ") in config:
    bstack11lll1lll1_opy_ = config[bstack1l1lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫୗ")]
  proxy = bstack11lll11ll_opy_(config)
  if proxy:
    if proxy.endswith(bstack1l1lll1_opy_ (u"࠭࠮ࡱࡣࡦࠫ୘")) and os.path.isfile(proxy):
      bstack11lll1lll1_opy_[bstack1l1lll1_opy_ (u"ࠧ࠮ࡲࡤࡧ࠲࡬ࡩ࡭ࡧࠪ୙")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1l1lll1_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭୚")):
        proxies = bstack11l1l11ll_opy_(config, bstack111ll1ll1l_opy_())
        if len(proxies) > 0:
          protocol, bstack11l1llll1l_opy_ = proxies.popitem()
          if bstack1l1lll1_opy_ (u"ࠤ࠽࠳࠴ࠨ୛") in bstack11l1llll1l_opy_:
            parsed_url = urlparse(bstack11l1llll1l_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1l1lll1_opy_ (u"ࠥ࠾࠴࠵ࠢଡ଼") + bstack11l1llll1l_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack11lll1lll1_opy_[bstack1l1lll1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡋࡳࡸࡺࠧଢ଼")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack11lll1lll1_opy_[bstack1l1lll1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡴࡸࡴࠨ୞")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack11lll1lll1_opy_[bstack1l1lll1_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡚ࡹࡥࡳࠩୟ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack11lll1lll1_opy_[bstack1l1lll1_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖࡡࡴࡵࠪୠ")] = str(parsed_url.password)
  return bstack11lll1lll1_opy_
def bstack1l111l1ll1_opy_(config):
  if bstack1l1lll1_opy_ (u"ࠨࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸ࠭ୡ") in config:
    return config[bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠧୢ")]
  return {}
def bstack11llll1111_opy_(caps):
  global bstack1111l11l1_opy_
  if bstack1l1lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫୣ") in caps:
    caps[bstack1l1lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ୤")][bstack1l1lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫ୥")] = True
    if bstack1111l11l1_opy_:
      caps[bstack1l1lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ୦")][bstack1l1lll1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ୧")] = bstack1111l11l1_opy_
  else:
    caps[bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭୨")] = True
    if bstack1111l11l1_opy_:
      caps[bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ୩")] = bstack1111l11l1_opy_
@measure(event_name=EVENTS.bstack1llll1ll1l_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1l11ll1l1l_opy_():
  global CONFIG
  if not bstack1l1l1l1l1_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ୪") in CONFIG and bstack111ll11ll_opy_(CONFIG[bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ୫")]):
    if (
      bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୬") in CONFIG
      and bstack111ll11ll_opy_(CONFIG[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ୭")].get(bstack1l1lll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡇ࡯࡮ࡢࡴࡼࡍࡳ࡯ࡴࡪࡣ࡯࡭ࡸࡧࡴࡪࡱࡱࠫ୮")))
    ):
      logger.debug(bstack1l1lll1_opy_ (u"ࠣࡎࡲࡧࡦࡲࠠࡣ࡫ࡱࡥࡷࡿࠠ࡯ࡱࡷࠤࡸࡺࡡࡳࡶࡨࡨࠥࡧࡳࠡࡵ࡮࡭ࡵࡈࡩ࡯ࡣࡵࡽࡎࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡡࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡧࡱࡥࡧࡲࡥࡥࠤ୯"))
      return
    bstack11lll1lll1_opy_ = bstack1lll1lll1l_opy_(CONFIG)
    bstack11ll1ll11_opy_(CONFIG[bstack1l1lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ୰")], bstack11lll1lll1_opy_)
def bstack11ll1ll11_opy_(key, bstack11lll1lll1_opy_):
  global bstack11l11ll1l_opy_
  logger.info(bstack1l111l11l1_opy_)
  try:
    bstack11l11ll1l_opy_ = Local()
    bstack1lllllll11_opy_ = {bstack1l1lll1_opy_ (u"ࠪ࡯ࡪࡿࠧୱ"): key}
    bstack1lllllll11_opy_.update(bstack11lll1lll1_opy_)
    logger.debug(bstack111ll1l11_opy_.format(str(bstack1lllllll11_opy_)).replace(key, bstack1l1lll1_opy_ (u"ࠫࡠࡘࡅࡅࡃࡆࡘࡊࡊ࡝ࠨ୲")))
    bstack11l11ll1l_opy_.start(**bstack1lllllll11_opy_)
    if bstack11l11ll1l_opy_.isRunning():
      logger.info(bstack11l1l11ll1_opy_)
  except Exception as e:
    bstack1l111ll1l1_opy_(bstack1ll11lllll_opy_.format(str(e)))
def bstack11l1lll1l_opy_():
  global bstack11l11ll1l_opy_
  if bstack11l11ll1l_opy_.isRunning():
    logger.info(bstack1l1lll11l_opy_)
    bstack11l11ll1l_opy_.stop()
  bstack11l11ll1l_opy_ = None
def bstack1l1llll11_opy_(bstack11l1l1111_opy_=[]):
  global CONFIG
  bstack1llllll111_opy_ = []
  bstack1ll11l111_opy_ = [bstack1l1lll1_opy_ (u"ࠬࡵࡳࠨ୳"), bstack1l1lll1_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ୴"), bstack1l1lll1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ୵"), bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ୶"), bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ୷"), bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ୸")]
  try:
    for err in bstack11l1l1111_opy_:
      bstack1l1lll1ll_opy_ = {}
      for k in bstack1ll11l111_opy_:
        val = CONFIG[bstack1l1lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ୹")][int(err[bstack1l1lll1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ୺")])].get(k)
        if val:
          bstack1l1lll1ll_opy_[k] = val
      if(err[bstack1l1lll1_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ୻")] != bstack1l1lll1_opy_ (u"ࠧࠨ୼")):
        bstack1l1lll1ll_opy_[bstack1l1lll1_opy_ (u"ࠨࡶࡨࡷࡹࡹࠧ୽")] = {
          err[bstack1l1lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ୾")]: err[bstack1l1lll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ୿")]
        }
        bstack1llllll111_opy_.append(bstack1l1lll1ll_opy_)
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡰࡴࡰࡥࡹࡺࡩ࡯ࡩࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥ࡫ࡶࡦࡰࡷ࠾ࠥ࠭஀") + str(e))
  finally:
    return bstack1llllll111_opy_
def bstack11llll1l1_opy_(file_name):
  bstack11lll11ll1_opy_ = []
  try:
    bstack1ll111l11_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1ll111l11_opy_):
      with open(bstack1ll111l11_opy_) as f:
        bstack1ll11l11l_opy_ = json.load(f)
        bstack11lll11ll1_opy_ = bstack1ll11l11l_opy_
      os.remove(bstack1ll111l11_opy_)
    return bstack11lll11ll1_opy_
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧ࡫ࡱࡨ࡮ࡴࡧࠡࡧࡵࡶࡴࡸࠠ࡭࡫ࡶࡸ࠿ࠦࠧ஁") + str(e))
    return bstack11lll11ll1_opy_
def bstack1l1l1111l1_opy_():
  try:
      from bstack_utils.constants import bstack111ll11lll_opy_, EVENTS
      from bstack_utils.helper import bstack1l1l1l1l1l_opy_, get_host_info, bstack1111111l_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack111l11l1ll_opy_ = os.path.join(os.getcwd(), bstack1l1lll1_opy_ (u"࠭࡬ࡰࡩࠪஂ"), bstack1l1lll1_opy_ (u"ࠧ࡬ࡧࡼ࠱ࡲ࡫ࡴࡳ࡫ࡦࡷ࠳ࡰࡳࡰࡰࠪஃ"))
      lock = FileLock(bstack111l11l1ll_opy_+bstack1l1lll1_opy_ (u"ࠣ࠰࡯ࡳࡨࡱࠢ஄"))
      def bstack1lll1111_opy_():
          try:
              with lock:
                  with open(bstack111l11l1ll_opy_, bstack1l1lll1_opy_ (u"ࠤࡵࠦஅ"), encoding=bstack1l1lll1_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤஆ")) as file:
                      data = json.load(file)
                      config = {
                          bstack1l1lll1_opy_ (u"ࠦ࡭࡫ࡡࡥࡧࡵࡷࠧஇ"): {
                              bstack1l1lll1_opy_ (u"ࠧࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠦஈ"): bstack1l1lll1_opy_ (u"ࠨࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠤஉ"),
                          }
                      }
                      bstack1l111ll11l_opy_ = datetime.utcnow()
                      bstack1ll1llll_opy_ = bstack1l111ll11l_opy_.strftime(bstack1l1lll1_opy_ (u"࡛ࠢࠦ࠰ࠩࡲ࠳ࠥࡥࡖࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࠲ࠪ࡬ࠠࡖࡖࡆࠦஊ"))
                      test_id = os.environ.get(bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭஋")) if os.environ.get(bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ஌")) else bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠥࡷࡩࡱࡒࡶࡰࡌࡨࠧ஍"))
                      payload = {
                          bstack1l1lll1_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠣஎ"): bstack1l1lll1_opy_ (u"ࠧࡹࡤ࡬ࡡࡨࡺࡪࡴࡴࡴࠤஏ"),
                          bstack1l1lll1_opy_ (u"ࠨࡤࡢࡶࡤࠦஐ"): {
                              bstack1l1lll1_opy_ (u"ࠢࡵࡧࡶࡸ࡭ࡻࡢࡠࡷࡸ࡭ࡩࠨ஑"): test_id,
                              bstack1l1lll1_opy_ (u"ࠣࡥࡵࡩࡦࡺࡥࡥࡡࡧࡥࡾࠨஒ"): bstack1ll1llll_opy_,
                              bstack1l1lll1_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡰࡤࡱࡪࠨஓ"): bstack1l1lll1_opy_ (u"ࠥࡗࡉࡑࡆࡦࡣࡷࡹࡷ࡫ࡐࡦࡴࡩࡳࡷࡳࡡ࡯ࡥࡨࠦஔ"),
                              bstack1l1lll1_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢ࡮ࡸࡵ࡮ࠣக"): {
                                  bstack1l1lll1_opy_ (u"ࠧࡳࡥࡢࡵࡸࡶࡪࡹࠢ஖"): data,
                                  bstack1l1lll1_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣ஗"): bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤ஘"))
                              },
                              bstack1l1lll1_opy_ (u"ࠣࡷࡶࡩࡷࡥࡤࡢࡶࡤࠦங"): bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠤࡸࡷࡪࡸࡎࡢ࡯ࡨࠦச")),
                              bstack1l1lll1_opy_ (u"ࠥ࡬ࡴࡹࡴࡠ࡫ࡱࡪࡴࠨ஛"): get_host_info()
                          }
                      }
                      bstack1l1ll1l11_opy_ = bstack11l11ll11l_opy_(cli.config, [bstack1l1lll1_opy_ (u"ࠦࡦࡶࡩࡴࠤஜ"), bstack1l1lll1_opy_ (u"ࠧ࡫ࡤࡴࡋࡱࡷࡹࡸࡵ࡮ࡧࡱࡸࡦࡺࡩࡰࡰࠥ஝"), bstack1l1lll1_opy_ (u"ࠨࡡࡱ࡫ࠥஞ")], bstack111ll11lll_opy_)
                      response = bstack1l1l1l1l1l_opy_(bstack1l1lll1_opy_ (u"ࠢࡑࡑࡖࡘࠧட"), bstack1l1ll1l11_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack1l1lll1_opy_ (u"ࠣࡆࡤࡸࡦࠦࡳࡦࡰࡷࠤࡸࡻࡣࡤࡧࡶࡷ࡫ࡻ࡬࡭ࡻࠣࡸࡴࠦࡻࡾࠢࡺ࡭ࡹ࡮ࠠࡥࡣࡷࡥࠥࢁࡽࠣ஠").format(bstack111ll11lll_opy_, payload))
                      else:
                          logger.debug(bstack1l1lll1_opy_ (u"ࠤࡕࡩࡶࡻࡥࡴࡶࠣࡪࡦ࡯࡬ࡦࡦࠣࡪࡴࡸࠠࡼࡿࠣࡻ࡮ࡺࡨࠡࡦࡤࡸࡦࠦࡻࡾࠤ஡").format(bstack111ll11lll_opy_, payload))
          except Exception as e:
              logger.debug(bstack1l1lll1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡰࡧࠤࡰ࡫ࡹࠡ࡯ࡨࡸࡷ࡯ࡣࡴࠢࡧࡥࡹࡧࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤࢀࢃࠢ஢").format(e))
      bstack1lll1111_opy_()
      bstack111ll1111_opy_(bstack111l11l1ll_opy_, logger)
  except:
    pass
def bstack1l11ll11l1_opy_():
  global bstack1lll1llll1_opy_
  global bstack1l11l1111l_opy_
  global bstack11111l111_opy_
  global bstack11111ll11_opy_
  global bstack11llll11ll_opy_
  global bstack111ll1l111_opy_
  global CONFIG
  bstack11l11ll11_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬண"))
  if bstack11l11ll11_opy_ in [bstack1l1lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫத"), bstack1l1lll1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ஥")]:
    bstack1111ll1l11_opy_()
  percy.shutdown()
  if bstack1lll1llll1_opy_:
    logger.warning(bstack1ll1l11lll_opy_.format(str(bstack1lll1llll1_opy_)))
  else:
    try:
      bstack1l11l1ll1l_opy_ = bstack1lll11111_opy_(bstack1l1lll1_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭஦"), logger)
      if bstack1l11l1ll1l_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭஧")) and bstack1l11l1ll1l_opy_.get(bstack1l1lll1_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧந")).get(bstack1l1lll1_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬன")):
        logger.warning(bstack1ll1l11lll_opy_.format(str(bstack1l11l1ll1l_opy_[bstack1l1lll1_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩப")][bstack1l1lll1_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧ஫")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1llll111ll_opy_.invoke(Events.bstack1l111l1l11_opy_)
  logger.info(bstack111l11ll1l_opy_)
  global bstack11l11ll1l_opy_
  if bstack11l11ll1l_opy_:
    bstack11l1lll1l_opy_()
  try:
    with bstack1l1l1lll1l_opy_:
      bstack11l11111l1_opy_ = bstack1l11l1111l_opy_.copy()
    for driver in bstack11l11111l1_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack11ll11lll_opy_)
  if bstack111ll1l111_opy_ == bstack1l1lll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ஬"):
    bstack11llll11ll_opy_ = bstack11llll1l1_opy_(bstack1l1lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨ஭"))
  if bstack111ll1l111_opy_ == bstack1l1lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨம") and len(bstack11111ll11_opy_) == 0:
    bstack11111ll11_opy_ = bstack11llll1l1_opy_(bstack1l1lll1_opy_ (u"ࠩࡳࡻࡤࡶࡹࡵࡧࡶࡸࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧய"))
    if len(bstack11111ll11_opy_) == 0:
      bstack11111ll11_opy_ = bstack11llll1l1_opy_(bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࡢࡴࡵࡶ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩர"))
  bstack11l1l1l111_opy_ = bstack1l1lll1_opy_ (u"ࠫࠬற")
  if len(bstack11111l111_opy_) > 0:
    bstack11l1l1l111_opy_ = bstack1l1llll11_opy_(bstack11111l111_opy_)
  elif len(bstack11111ll11_opy_) > 0:
    bstack11l1l1l111_opy_ = bstack1l1llll11_opy_(bstack11111ll11_opy_)
  elif len(bstack11llll11ll_opy_) > 0:
    bstack11l1l1l111_opy_ = bstack1l1llll11_opy_(bstack11llll11ll_opy_)
  elif len(bstack1l11llll1l_opy_) > 0:
    bstack11l1l1l111_opy_ = bstack1l1llll11_opy_(bstack1l11llll1l_opy_)
  if bool(bstack11l1l1l111_opy_):
    bstack11lll1llll_opy_(bstack11l1l1l111_opy_)
  else:
    bstack11lll1llll_opy_()
  bstack111ll1111_opy_(bstack1111lll1l_opy_, logger)
  if bstack11l11ll11_opy_ not in [bstack1l1lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ல")]:
    bstack1l1l1111l1_opy_()
  bstack111l11l1l_opy_.bstack1l1l1111_opy_(CONFIG)
  if len(bstack11llll11ll_opy_) > 0:
    sys.exit(len(bstack11llll11ll_opy_))
def bstack1l11ll1lll_opy_(bstack11ll1ll111_opy_, frame):
  global bstack1111111l_opy_
  logger.error(bstack1l111ll1ll_opy_)
  bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡎࡰࠩள"), bstack11ll1ll111_opy_)
  if hasattr(signal, bstack1l1lll1_opy_ (u"ࠧࡔ࡫ࡪࡲࡦࡲࡳࠨழ")):
    bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨவ"), signal.Signals(bstack11ll1ll111_opy_).name)
  else:
    bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩஶ"), bstack1l1lll1_opy_ (u"ࠪࡗࡎࡍࡕࡏࡍࡑࡓ࡜ࡔࠧஷ"))
  if cli.is_running():
    bstack1llll111ll_opy_.invoke(Events.bstack1l111l1l11_opy_)
  bstack11l11ll11_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬஸ"))
  if bstack11l11ll11_opy_ == bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬஹ") and not cli.is_enabled(CONFIG):
    bstack1l11ll1l_opy_.stop(bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭஺")))
  bstack1l11ll11l1_opy_()
  sys.exit(1)
def bstack1l111ll1l1_opy_(err):
  logger.critical(bstack111lll1l11_opy_.format(str(err)))
  bstack11lll1llll_opy_(bstack111lll1l11_opy_.format(str(err)), True)
  atexit.unregister(bstack1l11ll11l1_opy_)
  bstack1111ll1l11_opy_()
  sys.exit(1)
def bstack1ll1ll1ll1_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack11lll1llll_opy_(message, True)
  atexit.unregister(bstack1l11ll11l1_opy_)
  bstack1111ll1l11_opy_()
  sys.exit(1)
def bstack11ll111l11_opy_():
  global CONFIG
  global bstack1l111lll11_opy_
  global bstack1ll1lll1l_opy_
  global bstack11lll11111_opy_
  CONFIG = bstack111l1l111_opy_()
  load_dotenv(CONFIG.get(bstack1l1lll1_opy_ (u"ࠧࡦࡰࡹࡊ࡮ࡲࡥࠨ஻")))
  bstack1l11l1l111_opy_()
  bstack1ll1111111_opy_()
  CONFIG = bstack11l1l1llll_opy_(CONFIG)
  update(CONFIG, bstack1ll1lll1l_opy_)
  update(CONFIG, bstack1l111lll11_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1ll11llll_opy_(CONFIG)
  bstack11lll11111_opy_ = bstack1l1l1l1l1_opy_(CONFIG)
  os.environ[bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ஼")] = bstack11lll11111_opy_.__str__().lower()
  bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ஽"), bstack11lll11111_opy_)
  if (bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ா") in CONFIG and bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧி") in bstack1l111lll11_opy_) or (
          bstack1l1lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨீ") in CONFIG and bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩு") not in bstack1ll1lll1l_opy_):
    if os.getenv(bstack1l1lll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫூ")):
      CONFIG[bstack1l1lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ௃")] = os.getenv(bstack1l1lll1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭௄"))
    else:
      if not CONFIG.get(bstack1l1lll1_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠨ௅"), bstack1l1lll1_opy_ (u"ࠦࠧெ")) in bstack1lllll1ll1_opy_:
        bstack1lll11ll1_opy_()
  elif (bstack1l1lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨே") not in CONFIG and bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨை") in CONFIG) or (
          bstack1l1lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ௉") in bstack1ll1lll1l_opy_ and bstack1l1lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫொ") not in bstack1l111lll11_opy_):
    del (CONFIG[bstack1l1lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫோ")])
  if bstack1l1l1ll111_opy_(CONFIG):
    bstack1l111ll1l1_opy_(bstack1l1l11ll1_opy_)
  Config.bstack11l11l1l_opy_().set_property(bstack1l1lll1_opy_ (u"ࠥࡹࡸ࡫ࡲࡏࡣࡰࡩࠧௌ"), CONFIG[bstack1l1lll1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ்࠭")])
  bstack11l1l111l1_opy_()
  bstack1111l1l1ll_opy_()
  if bstack1l1lllllll_opy_ and not CONFIG.get(bstack1l1lll1_opy_ (u"ࠧ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠣ௎"), bstack1l1lll1_opy_ (u"ࠨࠢ௏")) in bstack1lllll1ll1_opy_:
    CONFIG[bstack1l1lll1_opy_ (u"ࠧࡢࡲࡳࠫௐ")] = bstack11l11l11ll_opy_(CONFIG)
    logger.info(bstack11ll1111ll_opy_.format(CONFIG[bstack1l1lll1_opy_ (u"ࠨࡣࡳࡴࠬ௑")]))
  if not bstack11lll11111_opy_:
    CONFIG[bstack1l1lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ௒")] = [{}]
def bstack111lll1ll_opy_(config, bstack1l1111l1ll_opy_):
  global CONFIG
  global bstack1l1lllllll_opy_
  CONFIG = config
  bstack1l1lllllll_opy_ = bstack1l1111l1ll_opy_
def bstack1111l1l1ll_opy_():
  global CONFIG
  global bstack1l1lllllll_opy_
  if bstack1l1lll1_opy_ (u"ࠪࡥࡵࡶࠧ௓") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1ll1ll1ll1_opy_(e, bstack11ll11l11_opy_)
    bstack1l1lllllll_opy_ = True
    bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪ௔"), True)
def bstack11l11l11ll_opy_(config):
  bstack1l1lll1111_opy_ = bstack1l1lll1_opy_ (u"ࠬ࠭௕")
  app = config[bstack1l1lll1_opy_ (u"࠭ࡡࡱࡲࠪ௖")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack111l111ll1_opy_:
      if os.path.exists(app):
        bstack1l1lll1111_opy_ = bstack1lllll11l1_opy_(config, app)
      elif bstack111l1ll1ll_opy_(app):
        bstack1l1lll1111_opy_ = app
      else:
        bstack1l111ll1l1_opy_(bstack11ll11llll_opy_.format(app))
    else:
      if bstack111l1ll1ll_opy_(app):
        bstack1l1lll1111_opy_ = app
      elif os.path.exists(app):
        bstack1l1lll1111_opy_ = bstack1lllll11l1_opy_(app)
      else:
        bstack1l111ll1l1_opy_(bstack1ll1lll11_opy_)
  else:
    if len(app) > 2:
      bstack1l111ll1l1_opy_(bstack1lll111l1l_opy_)
    elif len(app) == 2:
      if bstack1l1lll1_opy_ (u"ࠧࡱࡣࡷ࡬ࠬௗ") in app and bstack1l1lll1_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫ௘") in app:
        if os.path.exists(app[bstack1l1lll1_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ௙")]):
          bstack1l1lll1111_opy_ = bstack1lllll11l1_opy_(config, app[bstack1l1lll1_opy_ (u"ࠪࡴࡦࡺࡨࠨ௚")], app[bstack1l1lll1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧ௛")])
        else:
          bstack1l111ll1l1_opy_(bstack11ll11llll_opy_.format(app))
      else:
        bstack1l111ll1l1_opy_(bstack1lll111l1l_opy_)
    else:
      for key in app:
        if key in bstack1llllll1l1_opy_:
          if key == bstack1l1lll1_opy_ (u"ࠬࡶࡡࡵࡪࠪ௜"):
            if os.path.exists(app[key]):
              bstack1l1lll1111_opy_ = bstack1lllll11l1_opy_(config, app[key])
            else:
              bstack1l111ll1l1_opy_(bstack11ll11llll_opy_.format(app))
          else:
            bstack1l1lll1111_opy_ = app[key]
        else:
          bstack1l111ll1l1_opy_(bstack111l1l1ll1_opy_)
  return bstack1l1lll1111_opy_
def bstack111l1ll1ll_opy_(bstack1l1lll1111_opy_):
  import re
  bstack1llll11lll_opy_ = re.compile(bstack1l1lll1_opy_ (u"ࡸࠢ࡟࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮ࠩࠨ௝"))
  bstack11l1ll11ll_opy_ = re.compile(bstack1l1lll1_opy_ (u"ࡲࠣࡠ࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯࠵࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬࠧࠦ௞"))
  if bstack1l1lll1_opy_ (u"ࠨࡤࡶ࠾࠴࠵ࠧ௟") in bstack1l1lll1111_opy_ or re.fullmatch(bstack1llll11lll_opy_, bstack1l1lll1111_opy_) or re.fullmatch(bstack11l1ll11ll_opy_, bstack1l1lll1111_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack1l1l1l11l_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1lllll11l1_opy_(config, path, bstack11ll1l11l_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1l1lll1_opy_ (u"ࠩࡵࡦࠬ௠")).read()).hexdigest()
  bstack1ll1l11111_opy_ = bstack1ll111111l_opy_(md5_hash)
  bstack1l1lll1111_opy_ = None
  if bstack1ll1l11111_opy_:
    logger.info(bstack1ll1l1ll1l_opy_.format(bstack1ll1l11111_opy_, md5_hash))
    return bstack1ll1l11111_opy_
  bstack11ll11ll1_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack1l1lll1_opy_ (u"ࠪࡪ࡮ࡲࡥࠨ௡"): (os.path.basename(path), open(os.path.abspath(path), bstack1l1lll1_opy_ (u"ࠫࡷࡨࠧ௢")), bstack1l1lll1_opy_ (u"ࠬࡺࡥࡹࡶ࠲ࡴࡱࡧࡩ࡯ࠩ௣")),
      bstack1l1lll1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ௤"): bstack11ll1l11l_opy_
    }
  )
  response = requests.post(bstack1l1l1ll1l_opy_, data=multipart_data,
                           headers={bstack1l1lll1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭௥"): multipart_data.content_type},
                           auth=(config[bstack1l1lll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ௦")], config[bstack1l1lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ௧")]))
  try:
    res = json.loads(response.text)
    bstack1l1lll1111_opy_ = res[bstack1l1lll1_opy_ (u"ࠪࡥࡵࡶ࡟ࡶࡴ࡯ࠫ௨")]
    logger.info(bstack11l1111111_opy_.format(bstack1l1lll1111_opy_))
    bstack1l11ll111l_opy_(md5_hash, bstack1l1lll1111_opy_)
    cli.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡸࡴࡱࡵࡡࡥࡡࡤࡴࡵࠨ௩"), datetime.datetime.now() - bstack11ll11ll1_opy_)
  except ValueError as err:
    bstack1l111ll1l1_opy_(bstack1l11l11ll1_opy_.format(str(err)))
  return bstack1l1lll1111_opy_
def bstack11l1l111l1_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1ll11l1l1l_opy_
  bstack1lll11lll_opy_ = 1
  bstack1ll1l111l_opy_ = 1
  if bstack1l1lll1_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ௪") in CONFIG:
    bstack1ll1l111l_opy_ = CONFIG[bstack1l1lll1_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭௫")]
  else:
    bstack1ll1l111l_opy_ = bstack11l1lll111_opy_(framework_name, args) or 1
  if bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ௬") in CONFIG:
    bstack1lll11lll_opy_ = len(CONFIG[bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௭")])
  bstack1ll11l1l1l_opy_ = int(bstack1ll1l111l_opy_) * int(bstack1lll11lll_opy_)
def bstack11l1lll111_opy_(framework_name, args):
  if framework_name == bstack1llll11l11_opy_ and args and bstack1l1lll1_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ௮") in args:
      bstack11l1lll11_opy_ = args.index(bstack1l1lll1_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ௯"))
      return int(args[bstack11l1lll11_opy_ + 1]) or 1
  return 1
def bstack1ll111111l_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1lll1_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧ௰"))
    bstack11l1l1lll_opy_ = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠬࢄࠧ௱")), bstack1l1lll1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭௲"), bstack1l1lll1_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨ௳"))
    if os.path.exists(bstack11l1l1lll_opy_):
      try:
        bstack1ll1ll1lll_opy_ = json.load(open(bstack11l1l1lll_opy_, bstack1l1lll1_opy_ (u"ࠨࡴࡥࠫ௴")))
        if md5_hash in bstack1ll1ll1lll_opy_:
          bstack11l111l111_opy_ = bstack1ll1ll1lll_opy_[md5_hash]
          bstack1ll1l11l11_opy_ = datetime.datetime.now()
          bstack1ll1l1llll_opy_ = datetime.datetime.strptime(bstack11l111l111_opy_[bstack1l1lll1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ௵")], bstack1l1lll1_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧ௶"))
          if (bstack1ll1l11l11_opy_ - bstack1ll1l1llll_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack11l111l111_opy_[bstack1l1lll1_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ௷")]):
            return None
          return bstack11l111l111_opy_[bstack1l1lll1_opy_ (u"ࠬ࡯ࡤࠨ௸")]
      except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨࠡࡨ࡬ࡰࡪࡀࠠࡼࡿࠪ௹").format(str(e)))
    return None
  bstack11l1l1lll_opy_ = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠧࡿࠩ௺")), bstack1l1lll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ௻"), bstack1l1lll1_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪ௼"))
  lock_file = bstack11l1l1lll_opy_ + bstack1l1lll1_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩ௽")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack11l1l1lll_opy_):
        with open(bstack11l1l1lll_opy_, bstack1l1lll1_opy_ (u"ࠫࡷ࠭௾")) as f:
          content = f.read().strip()
          if content:
            bstack1ll1ll1lll_opy_ = json.loads(content)
            if md5_hash in bstack1ll1ll1lll_opy_:
              bstack11l111l111_opy_ = bstack1ll1ll1lll_opy_[md5_hash]
              bstack1ll1l11l11_opy_ = datetime.datetime.now()
              bstack1ll1l1llll_opy_ = datetime.datetime.strptime(bstack11l111l111_opy_[bstack1l1lll1_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ௿")], bstack1l1lll1_opy_ (u"࠭ࠥࡥ࠱ࠨࡱ࠴࡙ࠫࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪఀ"))
              if (bstack1ll1l11l11_opy_ - bstack1ll1l1llll_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack11l111l111_opy_[bstack1l1lll1_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬఁ")]):
                return None
              return bstack11l111l111_opy_[bstack1l1lll1_opy_ (u"ࠨ࡫ࡧࠫం")]
      return None
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡹ࡬ࡸ࡭ࠦࡦࡪ࡮ࡨࠤࡱࡵࡣ࡬࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡐࡈ࠺ࠦࡨࡢࡵ࡫࠾ࠥࢁࡽࠨః").format(str(e)))
    return None
def bstack1l11ll111l_opy_(md5_hash, bstack1l1lll1111_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1lll1_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭ఄ"))
    bstack111l1lll1l_opy_ = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠫࢃ࠭అ")), bstack1l1lll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬఆ"))
    if not os.path.exists(bstack111l1lll1l_opy_):
      os.makedirs(bstack111l1lll1l_opy_)
    bstack11l1l1lll_opy_ = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"࠭ࡾࠨఇ")), bstack1l1lll1_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧఈ"), bstack1l1lll1_opy_ (u"ࠨࡣࡳࡴ࡚ࡶ࡬ࡰࡣࡧࡑࡉ࠻ࡈࡢࡵ࡫࠲࡯ࡹ࡯࡯ࠩఉ"))
    bstack1l11l1l11l_opy_ = {
      bstack1l1lll1_opy_ (u"ࠩ࡬ࡨࠬఊ"): bstack1l1lll1111_opy_,
      bstack1l1lll1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ఋ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l1lll1_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨఌ")),
      bstack1l1lll1_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ఍"): str(__version__)
    }
    try:
      bstack1ll1ll1lll_opy_ = {}
      if os.path.exists(bstack11l1l1lll_opy_):
        bstack1ll1ll1lll_opy_ = json.load(open(bstack11l1l1lll_opy_, bstack1l1lll1_opy_ (u"࠭ࡲࡣࠩఎ")))
      bstack1ll1ll1lll_opy_[md5_hash] = bstack1l11l1l11l_opy_
      with open(bstack11l1l1lll_opy_, bstack1l1lll1_opy_ (u"ࠢࡸ࠭ࠥఏ")) as outfile:
        json.dump(bstack1ll1ll1lll_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1l1lll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡶࡲࡧࡥࡹ࡯࡮ࡨࠢࡐࡈ࠺ࠦࡨࡢࡵ࡫ࠤ࡫࡯࡬ࡦ࠼ࠣࡿࢂ࠭ఐ").format(str(e)))
    return
  bstack111l1lll1l_opy_ = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠩࢁࠫ఑")), bstack1l1lll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪఒ"))
  if not os.path.exists(bstack111l1lll1l_opy_):
    os.makedirs(bstack111l1lll1l_opy_)
  bstack11l1l1lll_opy_ = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠫࢃ࠭ఓ")), bstack1l1lll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬఔ"), bstack1l1lll1_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧక"))
  lock_file = bstack11l1l1lll_opy_ + bstack1l1lll1_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ࠭ఖ")
  bstack1l11l1l11l_opy_ = {
    bstack1l1lll1_opy_ (u"ࠨ࡫ࡧࠫగ"): bstack1l1lll1111_opy_,
    bstack1l1lll1_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬఘ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l1lll1_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧఙ")),
    bstack1l1lll1_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩచ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1ll1ll1lll_opy_ = {}
      if os.path.exists(bstack11l1l1lll_opy_):
        with open(bstack11l1l1lll_opy_, bstack1l1lll1_opy_ (u"ࠬࡸࠧఛ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll1ll1lll_opy_ = json.loads(content)
      bstack1ll1ll1lll_opy_[md5_hash] = bstack1l11l1l11l_opy_
      with open(bstack11l1l1lll_opy_, bstack1l1lll1_opy_ (u"ࠨࡷࠣజ")) as outfile:
        json.dump(bstack1ll1ll1lll_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡷࡪࡶ࡫ࠤ࡫࡯࡬ࡦࠢ࡯ࡳࡨࡱࡩ࡯ࡩࠣࡪࡴࡸࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩࠢࡸࡴࡩࡧࡴࡦ࠼ࠣࡿࢂ࠭ఝ").format(str(e)))
def bstack11l11ll1ll_opy_(self):
  return
def bstack1l11lll11_opy_(self):
  return
def bstack11ll1111l_opy_():
  global bstack1ll1lll1l1_opy_
  bstack1ll1lll1l1_opy_ = True
@measure(event_name=EVENTS.bstack11lll1l11l_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1l1ll1ll1_opy_(self):
  global bstack1l1ll111l1_opy_
  global bstack11ll11111_opy_
  global bstack11ll11lll1_opy_
  try:
    if bstack1l1lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨఞ") in bstack1l1ll111l1_opy_ and self.session_id != None and bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ట"), bstack1l1lll1_opy_ (u"ࠪࠫఠ")) != bstack1l1lll1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬడ"):
      bstack11ll1lll11_opy_ = bstack1l1lll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬఢ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1l1lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ణ")
      if bstack11ll1lll11_opy_ == bstack1l1lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧత"):
        bstack1l111llll1_opy_(logger)
      if self != None:
        bstack111lll1111_opy_(self, bstack11ll1lll11_opy_, bstack1l1lll1_opy_ (u"ࠨ࠮ࠣࠫథ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1l1lll1_opy_ (u"ࠩࠪద")
    if bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪధ") in bstack1l1ll111l1_opy_ and getattr(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪన"), None):
      bstack11l11ll1_opy_.bstack1llllllll_opy_(self, bstack1ll1l1l1l_opy_, logger, wait=True)
    if bstack1l1lll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ఩") in bstack1l1ll111l1_opy_:
      if not threading.currentThread().behave_test_status:
        bstack111lll1111_opy_(self, bstack1l1lll1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨప"))
      bstack111llll1ll_opy_.bstack1111lll11l_opy_(self)
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡳࡵࡣࡷࡹࡸࡀࠠࠣఫ") + str(e))
  bstack11ll11lll1_opy_(self)
  self.session_id = None
def bstack1lll11l11_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack111l111lll_opy_
    global bstack1l1ll111l1_opy_
    command_executor = kwargs.get(bstack1l1lll1_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡡࡨࡼࡪࡩࡵࡵࡱࡵࠫబ"), bstack1l1lll1_opy_ (u"ࠩࠪభ"))
    bstack1ll1l1111l_opy_ = False
    if type(command_executor) == str and bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭మ") in command_executor:
      bstack1ll1l1111l_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧయ") in str(getattr(command_executor, bstack1l1lll1_opy_ (u"ࠬࡥࡵࡳ࡮ࠪర"), bstack1l1lll1_opy_ (u"࠭ࠧఱ"))):
      bstack1ll1l1111l_opy_ = True
    else:
      kwargs = bstack1lll1ll1l_opy_.bstack111lllll1l_opy_(bstack1111l1llll_opy_=kwargs, config=CONFIG)
      return bstack1l111ll111_opy_(self, *args, **kwargs)
    if bstack1ll1l1111l_opy_:
      bstack1ll11ll11l_opy_ = bstack1l1l1l1111_opy_.bstack1l1ll1l1l1_opy_(CONFIG, bstack1l1ll111l1_opy_)
      if kwargs.get(bstack1l1lll1_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨల")):
        kwargs[bstack1l1lll1_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩళ")] = bstack111l111lll_opy_(kwargs[bstack1l1lll1_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪఴ")], bstack1l1ll111l1_opy_, CONFIG, bstack1ll11ll11l_opy_)
      elif kwargs.get(bstack1l1lll1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪవ")):
        kwargs[bstack1l1lll1_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫశ")] = bstack111l111lll_opy_(kwargs[bstack1l1lll1_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬష")], bstack1l1ll111l1_opy_, CONFIG, bstack1ll11ll11l_opy_)
  except Exception as e:
    logger.error(bstack1l1lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡦࡰࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡨࡧࡰࡴ࠼ࠣࡿࢂࠨస").format(str(e)))
  return bstack1l111ll111_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l1111ll11_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack11l1l1lll1_opy_(self, command_executor=bstack1l1lll1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯࠲࠴࠺࠲࠵࠴࠰࠯࠳࠽࠸࠹࠺࠴ࠣహ"), *args, **kwargs):
  global bstack11ll11111_opy_
  global bstack1l11l1111l_opy_
  bstack1ll1111l1l_opy_ = bstack1lll11l11_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1l11lll1_opy_.on():
    return bstack1ll1111l1l_opy_
  try:
    logger.debug(bstack1l1lll1_opy_ (u"ࠨࡅࡲࡱࡲࡧ࡮ࡥࠢࡈࡼࡪࡩࡵࡵࡱࡵࠤࡼ࡮ࡥ࡯ࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥ࡯ࡳࠡࡨࡤࡰࡸ࡫ࠠ࠮ࠢࡾࢁࠬ఺").format(str(command_executor)))
    logger.debug(bstack1l1lll1_opy_ (u"ࠩࡋࡹࡧࠦࡕࡓࡎࠣ࡭ࡸࠦ࠭ࠡࡽࢀࠫ఻").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ఼࠭") in command_executor._url:
      bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬఽ"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨా") in command_executor):
    bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧి"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack111l1llll_opy_ = getattr(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡔࡦࡵࡷࡑࡪࡺࡡࠨీ"), None)
  bstack1llll1l111_opy_ = {}
  if self.capabilities is not None:
    bstack1llll1l111_opy_[bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧు")] = self.capabilities.get(bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧూ"))
    bstack1llll1l111_opy_[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬృ")] = self.capabilities.get(bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬౄ"))
    bstack1llll1l111_opy_[bstack1l1lll1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࡤࡵࡰࡵ࡫ࡲࡲࡸ࠭౅")] = self.capabilities.get(bstack1l1lll1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫె"))
  if CONFIG.get(bstack1l1lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧే"), False) and bstack1lll1ll1l_opy_.bstack1ll1l1ll1_opy_(bstack1llll1l111_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack1l1lll1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨై") in bstack1l1ll111l1_opy_ or bstack1l1lll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ౉") in bstack1l1ll111l1_opy_:
    bstack1l11ll1l_opy_.bstack111l111l1_opy_(self)
  if bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪొ") in bstack1l1ll111l1_opy_ and bstack111l1llll_opy_ and bstack111l1llll_opy_.get(bstack1l1lll1_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫో"), bstack1l1lll1_opy_ (u"ࠬ࠭ౌ")) == bstack1l1lll1_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭్ࠧ"):
    bstack1l11ll1l_opy_.bstack111l111l1_opy_(self)
  bstack11ll11111_opy_ = self.session_id
  with bstack1l1l1lll1l_opy_:
    bstack1l11l1111l_opy_.append(self)
  return bstack1ll1111l1l_opy_
def bstack11111111l_opy_(args):
  return bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲࠨ౎") in str(args)
def bstack1ll11lll1_opy_(self, driver_command, *args, **kwargs):
  global bstack11l111l1ll_opy_
  global bstack111lllll1_opy_
  bstack1llll11111_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ౏"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1l1lll1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ౐"), None)
  bstack1lll11111l_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ౑"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1l1lll1_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭౒"), None)
  bstack11l1111ll1_opy_ = getattr(self, bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ౓"), None) != None and getattr(self, bstack1l1lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭౔"), None) == True
  if not bstack111lllll1_opy_ and bstack1l1lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿౕࠧ") in CONFIG and CONFIG[bstack1l1lll1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨౖ")] == True and bstack1l11111ll_opy_.bstack111l11l1l1_opy_(driver_command) and (bstack11l1111ll1_opy_ or bstack1llll11111_opy_ or bstack1lll11111l_opy_) and not bstack11111111l_opy_(args):
    try:
      bstack111lllll1_opy_ = True
      logger.debug(bstack1l1lll1_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤ࡫ࡵࡲࠡࡽࢀࠫ౗").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1l1lll1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡦࡴࡩࡳࡷࡳࠠࡴࡥࡤࡲࠥࢁࡽࠨౘ").format(str(err)))
    bstack111lllll1_opy_ = False
  response = bstack11l111l1ll_opy_(self, driver_command, *args, **kwargs)
  if (bstack1l1lll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪౙ") in str(bstack1l1ll111l1_opy_).lower() or bstack1l1lll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬౚ") in str(bstack1l1ll111l1_opy_).lower()) and bstack1l11lll1_opy_.on():
    try:
      if driver_command == bstack1l1lll1_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪ౛"):
        bstack1l11ll1l_opy_.bstack1l111ll11_opy_({
            bstack1l1lll1_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭౜"): response[bstack1l1lll1_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧౝ")],
            bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ౞"): bstack1l11ll1l_opy_.current_test_uuid() if bstack1l11ll1l_opy_.current_test_uuid() else bstack1l11lll1_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1l1lllll11_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack11111lll1l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack11ll11111_opy_
  global bstack1ll1l1l11l_opy_
  global bstack1lll111l11_opy_
  global bstack11lll1111l_opy_
  global bstack1l11ll11l_opy_
  global bstack1l1ll111l1_opy_
  global bstack1l111ll111_opy_
  global bstack1l11l1111l_opy_
  global bstack1l1111l111_opy_
  global bstack1ll1l1l1l_opy_
  if os.getenv(bstack1l1lll1_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ౟")) is not None and bstack1lll1ll1l_opy_.bstack11ll1l1l1l_opy_(CONFIG) is None:
    CONFIG[bstack1l1lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫౠ")] = True
  CONFIG[bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧౡ")] = str(bstack1l1ll111l1_opy_) + str(__version__)
  bstack1111l1l11l_opy_ = os.environ[bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫౢ")]
  bstack1ll11ll11l_opy_ = bstack1l1l1l1111_opy_.bstack1l1ll1l1l1_opy_(CONFIG, bstack1l1ll111l1_opy_)
  CONFIG[bstack1l1lll1_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪౣ")] = bstack1111l1l11l_opy_
  CONFIG[bstack1l1lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ౤")] = bstack1ll11ll11l_opy_
  if CONFIG.get(bstack1l1lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ౥"),bstack1l1lll1_opy_ (u"ࠪࠫ౦")) and bstack1l1lll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ౧") in bstack1l1ll111l1_opy_:
    CONFIG[bstack1l1lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ౨")].pop(bstack1l1lll1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ౩"), None)
    CONFIG[bstack1l1lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ౪")].pop(bstack1l1lll1_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭౫"), None)
  command_executor = bstack111ll1ll1l_opy_()
  logger.debug(bstack11l1l111ll_opy_.format(command_executor))
  proxy = bstack11l111ll11_opy_(CONFIG, proxy)
  bstack1l11l1lll_opy_ = 0 if bstack1ll1l1l11l_opy_ < 0 else bstack1ll1l1l11l_opy_
  try:
    if bstack11lll1111l_opy_ is True:
      bstack1l11l1lll_opy_ = int(multiprocessing.current_process().name)
    elif bstack1l11ll11l_opy_ is True:
      bstack1l11l1lll_opy_ = int(threading.current_thread().name)
  except:
    bstack1l11l1lll_opy_ = 0
  bstack1l1l11111_opy_ = bstack1lll11l1l1_opy_(CONFIG, bstack1l11l1lll_opy_)
  logger.debug(bstack1llll1lll1_opy_.format(str(bstack1l1l11111_opy_)))
  if bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭౬") in CONFIG and bstack111ll11ll_opy_(CONFIG[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ౭")]):
    bstack11llll1111_opy_(bstack1l1l11111_opy_)
  if bstack1lll1ll1l_opy_.bstack11lll1lll_opy_(CONFIG, bstack1l11l1lll_opy_) and bstack1lll1ll1l_opy_.bstack1l11ll1l11_opy_(bstack1l1l11111_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack1lll1ll1l_opy_.set_capabilities(bstack1l1l11111_opy_, CONFIG)
  if desired_capabilities:
    bstack1l1l11lll1_opy_ = bstack11l1l1llll_opy_(desired_capabilities)
    bstack1l1l11lll1_opy_[bstack1l1lll1_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ౮")] = bstack1111lll1l1_opy_(CONFIG)
    bstack1l1ll11lll_opy_ = bstack1lll11l1l1_opy_(bstack1l1l11lll1_opy_)
    if bstack1l1ll11lll_opy_:
      bstack1l1l11111_opy_ = update(bstack1l1ll11lll_opy_, bstack1l1l11111_opy_)
    desired_capabilities = None
  if options:
    bstack111l1l11l_opy_(options, bstack1l1l11111_opy_)
  if not options:
    options = bstack11ll11l111_opy_(bstack1l1l11111_opy_)
  bstack1ll1l1l1l_opy_ = CONFIG.get(bstack1l1lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ౯"))[bstack1l11l1lll_opy_]
  if proxy and bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭౰")):
    options.proxy(proxy)
  if options and bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭౱")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1ll1ll11ll_opy_() < version.parse(bstack1l1lll1_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ౲")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1l1l11111_opy_)
  logger.info(bstack1lllll1lll_opy_)
  bstack11l1l1111l_opy_.end(EVENTS.bstack1l1lll1lll_opy_.value, EVENTS.bstack1l1lll1lll_opy_.value + bstack1l1lll1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ౳"), EVENTS.bstack1l1lll1lll_opy_.value + bstack1l1lll1_opy_ (u"ࠥ࠾ࡪࡴࡤࠣ౴"), status=True, failure=None, test_name=bstack1lll111l11_opy_)
  if bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡶࡲࡰࡨ࡬ࡰࡪ࠭౵") in kwargs:
    del kwargs[bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡰࡳࡱࡩ࡭ࡱ࡫ࠧ౶")]
  try:
    if bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭౷")):
      bstack1l111ll111_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭౸")):
      bstack1l111ll111_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨ౹")):
      bstack1l111ll111_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1l111ll111_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack11111l1lll_opy_:
    logger.error(bstack111l1l1lll_opy_.format(bstack1l1lll1_opy_ (u"ࠩࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠨ౺"), str(bstack11111l1lll_opy_)))
    raise bstack11111l1lll_opy_
  if bstack1lll1ll1l_opy_.bstack11lll1lll_opy_(CONFIG, bstack1l11l1lll_opy_) and bstack1lll1ll1l_opy_.bstack1l11ll1l11_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬ౻")][bstack1l1lll1_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪ౼")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack1lll1ll1l_opy_.set_capabilities(bstack1l1l11111_opy_, CONFIG)
  try:
    bstack1lll1l1ll1_opy_ = bstack1l1lll1_opy_ (u"ࠬ࠭౽")
    if bstack1ll1ll11ll_opy_() >= version.parse(bstack1l1lll1_opy_ (u"࠭࠴࠯࠲࠱࠴ࡧ࠷ࠧ౾")):
      if self.caps is not None:
        bstack1lll1l1ll1_opy_ = self.caps.get(bstack1l1lll1_opy_ (u"ࠢࡰࡲࡷ࡭ࡲࡧ࡬ࡉࡷࡥ࡙ࡷࡲࠢ౿"))
    else:
      if self.capabilities is not None:
        bstack1lll1l1ll1_opy_ = self.capabilities.get(bstack1l1lll1_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣಀ"))
    if bstack1lll1l1ll1_opy_:
      bstack11ll1l11ll_opy_(bstack1lll1l1ll1_opy_)
      if bstack1ll1ll11ll_opy_() <= version.parse(bstack1l1lll1_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩಁ")):
        self.command_executor._url = bstack1l1lll1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦಂ") + bstack1l111lllll_opy_ + bstack1l1lll1_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣಃ")
      else:
        self.command_executor._url = bstack1l1lll1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢ಄") + bstack1lll1l1ll1_opy_ + bstack1l1lll1_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢಅ")
      logger.debug(bstack1111l1lll1_opy_.format(bstack1lll1l1ll1_opy_))
    else:
      logger.debug(bstack1lll111ll1_opy_.format(bstack1l1lll1_opy_ (u"ࠢࡐࡲࡷ࡭ࡲࡧ࡬ࠡࡊࡸࡦࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤࠣಆ")))
  except Exception as e:
    logger.debug(bstack1lll111ll1_opy_.format(e))
  if bstack1l1lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧಇ") in bstack1l1ll111l1_opy_:
    bstack1l11l1ll1_opy_(bstack1ll1l1l11l_opy_, bstack1l1111l111_opy_)
  bstack11ll11111_opy_ = self.session_id
  if bstack1l1lll1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩಈ") in bstack1l1ll111l1_opy_ or bstack1l1lll1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪಉ") in bstack1l1ll111l1_opy_ or bstack1l1lll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪಊ") in bstack1l1ll111l1_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack111l1llll_opy_ = getattr(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭ಋ"), None)
  if bstack1l1lll1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ಌ") in bstack1l1ll111l1_opy_ or bstack1l1lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭಍") in bstack1l1ll111l1_opy_:
    bstack1l11ll1l_opy_.bstack111l111l1_opy_(self)
  if bstack1l1lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨಎ") in bstack1l1ll111l1_opy_ and bstack111l1llll_opy_ and bstack111l1llll_opy_.get(bstack1l1lll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩಏ"), bstack1l1lll1_opy_ (u"ࠪࠫಐ")) == bstack1l1lll1_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ಑"):
    bstack1l11ll1l_opy_.bstack111l111l1_opy_(self)
  with bstack1l1l1lll1l_opy_:
    bstack1l11l1111l_opy_.append(self)
  if bstack1l1lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಒ") in CONFIG and bstack1l1lll1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫಓ") in CONFIG[bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಔ")][bstack1l11l1lll_opy_]:
    bstack1lll111l11_opy_ = CONFIG[bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಕ")][bstack1l11l1lll_opy_][bstack1l1lll1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧಖ")]
  logger.debug(bstack11111ll1l_opy_.format(bstack11ll11111_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack111l1ll11_opy_
    def bstack111l1l1ll_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1l11l111l_opy_
      if(bstack1l1lll1_opy_ (u"ࠥ࡭ࡳࡪࡥࡹ࠰࡭ࡷࠧಗ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠫࢃ࠭ಘ")), bstack1l1lll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬಙ"), bstack1l1lll1_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨಚ")), bstack1l1lll1_opy_ (u"ࠧࡸࠩಛ")) as fp:
          fp.write(bstack1l1lll1_opy_ (u"ࠣࠤಜ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1l1lll1_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦಝ")))):
          with open(args[1], bstack1l1lll1_opy_ (u"ࠪࡶࠬಞ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1l1lll1_opy_ (u"ࠫࡦࡹࡹ࡯ࡥࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥࡥ࡮ࡦࡹࡓࡥ࡬࡫ࠨࡤࡱࡱࡸࡪࡾࡴ࠭ࠢࡳࡥ࡬࡫ࠠ࠾ࠢࡹࡳ࡮ࡪࠠ࠱ࠫࠪಟ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack111l1l1l11_opy_)
            if bstack1l1lll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩಠ") in CONFIG and str(CONFIG[bstack1l1lll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪಡ")]).lower() != bstack1l1lll1_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ಢ"):
                bstack111llll11_opy_ = bstack111l1ll11_opy_()
                bstack1l1ll111ll_opy_ = bstack1l1lll1_opy_ (u"ࠨࠩࠪࠎ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠊࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡰࡢࡶ࡫ࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳࡞࠽ࠍࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠴ࡡࡀࠐࡣࡰࡰࡶࡸࠥࡶ࡟ࡪࡰࡧࡩࡽࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠴ࡠ࠿ࠏࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡹ࡬ࡪࡥࡨࠬ࠵࠲ࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࠬ࠿ࠏࡩ࡯࡯ࡵࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬ࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ࠭ࡀࠐࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁࡻࠋࠢࠣࡰࡪࡺࠠࡤࡣࡳࡷࡀࠐࠠࠡࡶࡵࡽࠥࢁࡻࠋࠢࠣࠤࠥࡩࡡࡱࡵࠣࡁࠥࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠩ࠼ࠌࠣࠤࢂࢃࠠࡤࡣࡷࡧ࡭ࠦࠨࡦࡺࠬࠤࢀࢁࠊࠡࠢࠣࠤࡨࡵ࡮ࡴࡱ࡯ࡩ࠳࡫ࡲࡳࡱࡵࠬࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡤࡶࡸ࡫ࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸࡀࠢ࠭ࠢࡨࡼ࠮ࡁࠊࠡࠢࢀࢁࠏࠦࠠࡳࡧࡷࡹࡷࡴࠠࡢࡹࡤ࡭ࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴ࡣࡰࡰࡱࡩࡨࡺࠨࡼࡽࠍࠤࠥࠦࠠࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷ࠾ࠥ࠭ࡻࡤࡦࡳ࡙ࡷࡲࡽࠨࠢ࠮ࠤࡪࡴࡣࡰࡦࡨ࡙ࡗࡏࡃࡰ࡯ࡳࡳࡳ࡫࡮ࡵࠪࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡧࡦࡶࡳࠪࠫ࠯ࠎࠥࠦࠠࠡ࠰࠱࠲ࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶࠎࠥࠦࡽࡾࠫ࠾ࠎࢂࢃ࠻ࠋ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࠎࠬ࠭ࠧಣ").format(bstack111llll11_opy_=bstack111llll11_opy_)
            lines.insert(1, bstack1l1ll111ll_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1l1lll1_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦತ")), bstack1l1lll1_opy_ (u"ࠪࡻࠬಥ")) as bstack1ll1llll11_opy_:
              bstack1ll1llll11_opy_.writelines(lines)
        CONFIG[bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭ದ")] = str(bstack1l1ll111l1_opy_) + str(__version__)
        bstack1111l1l11l_opy_ = os.environ[bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪಧ")]
        bstack1ll11ll11l_opy_ = bstack1l1l1l1111_opy_.bstack1l1ll1l1l1_opy_(CONFIG, bstack1l1ll111l1_opy_)
        CONFIG[bstack1l1lll1_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩನ")] = bstack1111l1l11l_opy_
        CONFIG[bstack1l1lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ಩")] = bstack1ll11ll11l_opy_
        bstack1l11l1lll_opy_ = 0 if bstack1ll1l1l11l_opy_ < 0 else bstack1ll1l1l11l_opy_
        try:
          if bstack11lll1111l_opy_ is True:
            bstack1l11l1lll_opy_ = int(multiprocessing.current_process().name)
          elif bstack1l11ll11l_opy_ is True:
            bstack1l11l1lll_opy_ = int(threading.current_thread().name)
        except:
          bstack1l11l1lll_opy_ = 0
        CONFIG[bstack1l1lll1_opy_ (u"ࠣࡷࡶࡩ࡜࠹ࡃࠣಪ")] = False
        CONFIG[bstack1l1lll1_opy_ (u"ࠤ࡬ࡷࡕࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣಫ")] = True
        bstack1l1l11111_opy_ = bstack1lll11l1l1_opy_(CONFIG, bstack1l11l1lll_opy_)
        logger.debug(bstack1llll1lll1_opy_.format(str(bstack1l1l11111_opy_)))
        if CONFIG.get(bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧಬ")):
          bstack11llll1111_opy_(bstack1l1l11111_opy_)
        if bstack1l1lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧಭ") in CONFIG and bstack1l1lll1_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪಮ") in CONFIG[bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಯ")][bstack1l11l1lll_opy_]:
          bstack1lll111l11_opy_ = CONFIG[bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪರ")][bstack1l11l1lll_opy_][bstack1l1lll1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ಱ")]
        args.append(os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠩࢁࠫಲ")), bstack1l1lll1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪಳ"), bstack1l1lll1_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭಴")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1l1l11111_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1l1lll1_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢವ"))
      bstack1l11l111l_opy_ = True
      return bstack1111l1ll1l_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack1llll1111l_opy_(self,
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
    global bstack1ll1l1l11l_opy_
    global bstack1lll111l11_opy_
    global bstack11lll1111l_opy_
    global bstack1l11ll11l_opy_
    global bstack1l1ll111l1_opy_
    CONFIG[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨಶ")] = str(bstack1l1ll111l1_opy_) + str(__version__)
    bstack1111l1l11l_opy_ = os.environ[bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬಷ")]
    bstack1ll11ll11l_opy_ = bstack1l1l1l1111_opy_.bstack1l1ll1l1l1_opy_(CONFIG, bstack1l1ll111l1_opy_)
    CONFIG[bstack1l1lll1_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫಸ")] = bstack1111l1l11l_opy_
    CONFIG[bstack1l1lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫಹ")] = bstack1ll11ll11l_opy_
    bstack1l11l1lll_opy_ = 0 if bstack1ll1l1l11l_opy_ < 0 else bstack1ll1l1l11l_opy_
    try:
      if bstack11lll1111l_opy_ is True:
        bstack1l11l1lll_opy_ = int(multiprocessing.current_process().name)
      elif bstack1l11ll11l_opy_ is True:
        bstack1l11l1lll_opy_ = int(threading.current_thread().name)
    except:
      bstack1l11l1lll_opy_ = 0
    CONFIG[bstack1l1lll1_opy_ (u"ࠥ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ಺")] = True
    bstack1l1l11111_opy_ = bstack1lll11l1l1_opy_(CONFIG, bstack1l11l1lll_opy_)
    logger.debug(bstack1llll1lll1_opy_.format(str(bstack1l1l11111_opy_)))
    if CONFIG.get(bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ಻")):
      bstack11llll1111_opy_(bstack1l1l11111_opy_)
    if bstack1l1lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ಼") in CONFIG and bstack1l1lll1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫಽ") in CONFIG[bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಾ")][bstack1l11l1lll_opy_]:
      bstack1lll111l11_opy_ = CONFIG[bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಿ")][bstack1l11l1lll_opy_][bstack1l1lll1_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧೀ")]
    import urllib
    import json
    if bstack1l1lll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧು") in CONFIG and str(CONFIG[bstack1l1lll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨೂ")]).lower() != bstack1l1lll1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫೃ"):
        bstack111ll1ll11_opy_ = bstack111l1ll11_opy_()
        bstack111llll11_opy_ = bstack111ll1ll11_opy_ + urllib.parse.quote(json.dumps(bstack1l1l11111_opy_))
    else:
        bstack111llll11_opy_ = bstack1l1lll1_opy_ (u"࠭ࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠨೄ") + urllib.parse.quote(json.dumps(bstack1l1l11111_opy_))
    browser = self.connect(bstack111llll11_opy_)
    return browser
except Exception as e:
    pass
def bstack111lll11l_opy_():
    global bstack1l11l111l_opy_
    global bstack1l1ll111l1_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack11l1ll1lll_opy_
        global bstack1111111l_opy_
        if not bstack11lll11111_opy_:
          global bstack1l11llllll_opy_
          if not bstack1l11llllll_opy_:
            from bstack_utils.helper import bstack1111ll111l_opy_, bstack111l11llll_opy_, bstack1l1l11l1l1_opy_
            bstack1l11llllll_opy_ = bstack1111ll111l_opy_()
            bstack111l11llll_opy_(bstack1l1ll111l1_opy_)
            bstack1ll11ll11l_opy_ = bstack1l1l1l1111_opy_.bstack1l1ll1l1l1_opy_(CONFIG, bstack1l1ll111l1_opy_)
            bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"ࠢࡑࡎࡄ࡝࡜ࡘࡉࡈࡊࡗࡣࡕࡘࡏࡅࡗࡆࡘࡤࡓࡁࡑࠤ೅"), bstack1ll11ll11l_opy_)
          BrowserType.connect = bstack11l1ll1lll_opy_
          return
        BrowserType.launch = bstack1llll1111l_opy_
        bstack1l11l111l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack111l1l1ll_opy_
      bstack1l11l111l_opy_ = True
    except Exception as e:
      pass
def bstack1l1ll1l111_opy_(context, bstack1l1111l1l_opy_):
  try:
    context.page.evaluate(bstack1l1lll1_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤೆ"), bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿࠭ೇ")+ json.dumps(bstack1l1111l1l_opy_) + bstack1l1lll1_opy_ (u"ࠥࢁࢂࠨೈ"))
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡻࡾ࠼ࠣࡿࢂࠨ೉").format(str(e), traceback.format_exc()))
def bstack11l1l11l1l_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1l1lll1_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨೊ"), bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫೋ") + json.dumps(message) + bstack1l1lll1_opy_ (u"ࠧ࠭ࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠪೌ") + json.dumps(level) + bstack1l1lll1_opy_ (u"ࠨࡿࢀ್ࠫ"))
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡧ࡮࡯ࡱࡷࡥࡹ࡯࡯࡯ࠢࡾࢁ࠿ࠦࡻࡾࠤ೎").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1ll1ll1111_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1l1l1lll11_opy_(self, url):
  global bstack11llll11l_opy_
  try:
    bstack11l1lll1l1_opy_(url)
  except Exception as err:
    logger.debug(bstack11llllllll_opy_.format(str(err)))
  try:
    bstack11llll11l_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1l1ll11ll1_opy_):
        bstack11l1lll1l1_opy_(url, True)
    except Exception as err:
      logger.debug(bstack11llllllll_opy_.format(str(err)))
    raise e
def bstack1111ll1lll_opy_(self):
  global bstack1ll1l1l1l1_opy_
  bstack1ll1l1l1l1_opy_ = self
  return
def bstack1l1l11ll1l_opy_(self):
  global bstack1lll1l11ll_opy_
  bstack1lll1l11ll_opy_ = self
  return
def bstack1llll1ll11_opy_(test_name, bstack11l1l1l1l1_opy_):
  global CONFIG
  if percy.bstack111ll11l11_opy_() == bstack1l1lll1_opy_ (u"ࠥࡸࡷࡻࡥࠣ೏"):
    bstack11ll1l1l11_opy_ = os.path.relpath(bstack11l1l1l1l1_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack11ll1l1l11_opy_)
    bstack11l1l1l1ll_opy_ = suite_name + bstack1l1lll1_opy_ (u"ࠦ࠲ࠨ೐") + test_name
    threading.current_thread().percySessionName = bstack11l1l1l1ll_opy_
def bstack1111l1l1l_opy_(self, test, *args, **kwargs):
  global bstack1llll11ll1_opy_
  test_name = None
  bstack11l1l1l1l1_opy_ = None
  if test:
    test_name = str(test.name)
    bstack11l1l1l1l1_opy_ = str(test.source)
  bstack1llll1ll11_opy_(test_name, bstack11l1l1l1l1_opy_)
  bstack1llll11ll1_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1ll1111l1_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1111l111l_opy_(driver, bstack11l1l1l1ll_opy_):
  if not bstack1llll1l11l_opy_ and bstack11l1l1l1ll_opy_:
      bstack1ll11ll1l1_opy_ = {
          bstack1l1lll1_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬ೑"): bstack1l1lll1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ೒"),
          bstack1l1lll1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ೓"): {
              bstack1l1lll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭೔"): bstack11l1l1l1ll_opy_
          }
      }
      bstack1l1111111l_opy_ = bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧೕ").format(json.dumps(bstack1ll11ll1l1_opy_))
      driver.execute_script(bstack1l1111111l_opy_)
  if bstack1l1llll1l1_opy_:
      bstack111lll1lll_opy_ = {
          bstack1l1lll1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪೖ"): bstack1l1lll1_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭೗"),
          bstack1l1lll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ೘"): {
              bstack1l1lll1_opy_ (u"࠭ࡤࡢࡶࡤࠫ೙"): bstack11l1l1l1ll_opy_ + bstack1l1lll1_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩ೚"),
              bstack1l1lll1_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ೛"): bstack1l1lll1_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧ೜")
          }
      }
      if bstack1l1llll1l1_opy_.status == bstack1l1lll1_opy_ (u"ࠪࡔࡆ࡙ࡓࠨೝ"):
          bstack1ll11ll1ll_opy_ = bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩೞ").format(json.dumps(bstack111lll1lll_opy_))
          driver.execute_script(bstack1ll11ll1ll_opy_)
          bstack111lll1111_opy_(driver, bstack1l1lll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ೟"))
      elif bstack1l1llll1l1_opy_.status == bstack1l1lll1_opy_ (u"࠭ࡆࡂࡋࡏࠫೠ"):
          reason = bstack1l1lll1_opy_ (u"ࠢࠣೡ")
          bstack1lll11ll11_opy_ = bstack11l1l1l1ll_opy_ + bstack1l1lll1_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠩೢ")
          if bstack1l1llll1l1_opy_.message:
              reason = str(bstack1l1llll1l1_opy_.message)
              bstack1lll11ll11_opy_ = bstack1lll11ll11_opy_ + bstack1l1lll1_opy_ (u"ࠩࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸ࠺ࠡࠩೣ") + reason
          bstack111lll1lll_opy_[bstack1l1lll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭೤")] = {
              bstack1l1lll1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪ೥"): bstack1l1lll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ೦"),
              bstack1l1lll1_opy_ (u"࠭ࡤࡢࡶࡤࠫ೧"): bstack1lll11ll11_opy_
          }
          bstack1ll11ll1ll_opy_ = bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ೨").format(json.dumps(bstack111lll1lll_opy_))
          driver.execute_script(bstack1ll11ll1ll_opy_)
          bstack111lll1111_opy_(driver, bstack1l1lll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ೩"), reason)
          bstack111l1111ll_opy_(reason, str(bstack1l1llll1l1_opy_), str(bstack1ll1l1l11l_opy_), logger)
@measure(event_name=EVENTS.bstack1l111l1ll_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack11ll111l1_opy_(driver, test):
  if percy.bstack111ll11l11_opy_() == bstack1l1lll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ೪") and percy.bstack11l1ll11l1_opy_() == bstack1l1lll1_opy_ (u"ࠥࡸࡪࡹࡴࡤࡣࡶࡩࠧ೫"):
      bstack11ll1l1ll1_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ೬"), None)
      bstack1l11l11l1_opy_(driver, bstack11ll1l1ll1_opy_, test)
  if (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ೭"), None) and
      bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ೮"), None)) or (
      bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ೯"), None) and
      bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ೰"), None)):
      logger.info(bstack1l1lll1_opy_ (u"ࠤࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣ࡬ࡦࡹࠠࡦࡰࡧࡩࡩ࠴ࠠࡑࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡬ࡷࠥࡻ࡮ࡥࡧࡵࡻࡦࡿ࠮ࠡࠤೱ"))
      bstack1lll1ll1l_opy_.bstack1111lll1_opy_(driver, name=test.name, path=test.source)
def bstack11l11lll1l_opy_(test, bstack11l1l1l1ll_opy_):
    try:
      bstack11ll11ll1_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack1l1lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨೲ")] = bstack11l1l1l1ll_opy_
      if bstack1l1llll1l1_opy_:
        if bstack1l1llll1l1_opy_.status == bstack1l1lll1_opy_ (u"ࠫࡕࡇࡓࡔࠩೳ"):
          data[bstack1l1lll1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ೴")] = bstack1l1lll1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭೵")
        elif bstack1l1llll1l1_opy_.status == bstack1l1lll1_opy_ (u"ࠧࡇࡃࡌࡐࠬ೶"):
          data[bstack1l1lll1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ೷")] = bstack1l1lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ೸")
          if bstack1l1llll1l1_opy_.message:
            data[bstack1l1lll1_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ೹")] = str(bstack1l1llll1l1_opy_.message)
      user = CONFIG[bstack1l1lll1_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭೺")]
      key = CONFIG[bstack1l1lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ೻")]
      host = bstack11l11ll11l_opy_(cli.config, [bstack1l1lll1_opy_ (u"ࠨࡡࡱ࡫ࡶࠦ೼"), bstack1l1lll1_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࠤ೽"), bstack1l1lll1_opy_ (u"ࠣࡣࡳ࡭ࠧ೾")], bstack1l1lll1_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠥ೿"))
      url = bstack1l1lll1_opy_ (u"ࠪࡿࢂ࠵ࡡࡶࡶࡲࡱࡦࡺࡥ࠰ࡵࡨࡷࡸ࡯࡯࡯ࡵ࠲ࡿࢂ࠴ࡪࡴࡱࡱࠫഀ").format(host, bstack11ll11111_opy_)
      headers = {
        bstack1l1lll1_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪഁ"): bstack1l1lll1_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨം"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠨࡨࡵࡶࡳ࠾ࡺࡶࡤࡢࡶࡨࡣࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡷࡹࡧࡴࡶࡵࠥഃ"), datetime.datetime.now() - bstack11ll11ll1_opy_)
    except Exception as e:
      logger.error(bstack11lll1ll1l_opy_.format(str(e)))
def bstack1111l11l11_opy_(test, bstack11l1l1l1ll_opy_):
  global CONFIG
  global bstack1lll1l11ll_opy_
  global bstack1ll1l1l1l1_opy_
  global bstack11ll11111_opy_
  global bstack1l1llll1l1_opy_
  global bstack1lll111l11_opy_
  global bstack1l1l11111l_opy_
  global bstack1l11ll1ll_opy_
  global bstack1l11lll1l_opy_
  global bstack1ll11111ll_opy_
  global bstack1l11l1111l_opy_
  global bstack1ll1l1l1l_opy_
  global bstack1l11l1lll1_opy_
  try:
    if not bstack11ll11111_opy_:
      with bstack1l11l1lll1_opy_:
        bstack11l11lllll_opy_ = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠧࡿࠩഄ")), bstack1l1lll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨഅ"), bstack1l1lll1_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫആ"))
        if os.path.exists(bstack11l11lllll_opy_):
          with open(bstack11l11lllll_opy_, bstack1l1lll1_opy_ (u"ࠪࡶࠬഇ")) as f:
            content = f.read().strip()
            if content:
              bstack1l11l11ll_opy_ = json.loads(bstack1l1lll1_opy_ (u"ࠦࢀࠨഈ") + content + bstack1l1lll1_opy_ (u"ࠬࠨࡸࠣ࠼ࠣࠦࡾࠨࠧഉ") + bstack1l1lll1_opy_ (u"ࠨࡽࠣഊ"))
              bstack11ll11111_opy_ = bstack1l11l11ll_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡋࡇࡷࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬഋ") + str(e))
  if bstack1l11l1111l_opy_:
    with bstack1l1l1lll1l_opy_:
      bstack111ll11111_opy_ = bstack1l11l1111l_opy_.copy()
    for driver in bstack111ll11111_opy_:
      if bstack11ll11111_opy_ == driver.session_id:
        if test:
          bstack11ll111l1_opy_(driver, test)
        bstack1111l111l_opy_(driver, bstack11l1l1l1ll_opy_)
  elif bstack11ll11111_opy_:
    bstack11l11lll1l_opy_(test, bstack11l1l1l1ll_opy_)
  if bstack1lll1l11ll_opy_:
    bstack1l11ll1ll_opy_(bstack1lll1l11ll_opy_)
  if bstack1ll1l1l1l1_opy_:
    bstack1l11lll1l_opy_(bstack1ll1l1l1l1_opy_)
  if bstack1ll1lll1l1_opy_:
    bstack1ll11111ll_opy_()
def bstack11ll1ll11l_opy_(self, test, *args, **kwargs):
  bstack11l1l1l1ll_opy_ = None
  if test:
    bstack11l1l1l1ll_opy_ = str(test.name)
  bstack1111l11l11_opy_(test, bstack11l1l1l1ll_opy_)
  bstack1l1l11111l_opy_(self, test, *args, **kwargs)
def bstack11llll1l1l_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1l1l11l1ll_opy_
  global CONFIG
  global bstack1l11l1111l_opy_
  global bstack11ll11111_opy_
  global bstack1l11l1lll1_opy_
  bstack1111l1111l_opy_ = None
  try:
    if bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧഌ"), None) or bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ഍"), None):
      try:
        if not bstack11ll11111_opy_:
          bstack11l11lllll_opy_ = os.path.join(os.path.expanduser(bstack1l1lll1_opy_ (u"ࠪࢂࠬഎ")), bstack1l1lll1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫഏ"), bstack1l1lll1_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧഐ"))
          with bstack1l11l1lll1_opy_:
            if os.path.exists(bstack11l11lllll_opy_):
              with open(bstack11l11lllll_opy_, bstack1l1lll1_opy_ (u"࠭ࡲࠨ഑")) as f:
                content = f.read().strip()
                if content:
                  bstack1l11l11ll_opy_ = json.loads(bstack1l1lll1_opy_ (u"ࠢࡼࠤഒ") + content + bstack1l1lll1_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪഓ") + bstack1l1lll1_opy_ (u"ࠤࢀࠦഔ"))
                  bstack11ll11111_opy_ = bstack1l11l11ll_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡎࡊࡳࠡࡨ࡬ࡰࡪࠦࡩ࡯ࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࠩക") + str(e))
      if bstack1l11l1111l_opy_:
        with bstack1l1l1lll1l_opy_:
          bstack111ll11111_opy_ = bstack1l11l1111l_opy_.copy()
        for driver in bstack111ll11111_opy_:
          if bstack11ll11111_opy_ == driver.session_id:
            bstack1111l1111l_opy_ = driver
    bstack11lll11l1_opy_ = bstack1lll1ll1l_opy_.bstack1ll11111l1_opy_(test.tags)
    if bstack1111l1111l_opy_:
      threading.current_thread().isA11yTest = bstack1lll1ll1l_opy_.bstack11lllll111_opy_(bstack1111l1111l_opy_, bstack11lll11l1_opy_)
      threading.current_thread().isAppA11yTest = bstack1lll1ll1l_opy_.bstack11lllll111_opy_(bstack1111l1111l_opy_, bstack11lll11l1_opy_)
    else:
      threading.current_thread().isA11yTest = bstack11lll11l1_opy_
      threading.current_thread().isAppA11yTest = bstack11lll11l1_opy_
  except:
    pass
  bstack1l1l11l1ll_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1l1llll1l1_opy_
  try:
    bstack1l1llll1l1_opy_ = self._test
  except:
    bstack1l1llll1l1_opy_ = self.test
def bstack1l1l1l111_opy_():
  global bstack11l1ll1l1l_opy_
  try:
    if os.path.exists(bstack11l1ll1l1l_opy_):
      os.remove(bstack11l1ll1l1l_opy_)
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡤࡦ࡮ࡨࡸ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧഖ") + str(e))
def bstack1l11l1llll_opy_():
  global bstack11l1ll1l1l_opy_
  bstack1l11l1ll1l_opy_ = {}
  lock_file = bstack11l1ll1l1l_opy_ + bstack1l1lll1_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫഗ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩഘ"))
    try:
      if not os.path.isfile(bstack11l1ll1l1l_opy_):
        with open(bstack11l1ll1l1l_opy_, bstack1l1lll1_opy_ (u"ࠧࡸࠩങ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack11l1ll1l1l_opy_):
        with open(bstack11l1ll1l1l_opy_, bstack1l1lll1_opy_ (u"ࠨࡴࠪച")) as f:
          content = f.read().strip()
          if content:
            bstack1l11l1ll1l_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack1l1lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫഛ") + str(e))
    return bstack1l11l1ll1l_opy_
  try:
    os.makedirs(os.path.dirname(bstack11l1ll1l1l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack11l1ll1l1l_opy_):
        with open(bstack11l1ll1l1l_opy_, bstack1l1lll1_opy_ (u"ࠪࡻࠬജ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack11l1ll1l1l_opy_):
        with open(bstack11l1ll1l1l_opy_, bstack1l1lll1_opy_ (u"ࠫࡷ࠭ഝ")) as f:
          content = f.read().strip()
          if content:
            bstack1l11l1ll1l_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧഞ") + str(e))
  finally:
    return bstack1l11l1ll1l_opy_
def bstack1l11l1ll1_opy_(platform_index, item_index):
  global bstack11l1ll1l1l_opy_
  lock_file = bstack11l1ll1l1l_opy_ + bstack1l1lll1_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬട")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠢࡱࡳࡹࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡥࡥࡸ࡯ࡣࠡࡨ࡬ࡰࡪࠦ࡯ࡱࡧࡵࡥࡹ࡯࡯࡯ࡵࠪഠ"))
    try:
      bstack1l11l1ll1l_opy_ = {}
      if os.path.exists(bstack11l1ll1l1l_opy_):
        with open(bstack11l1ll1l1l_opy_, bstack1l1lll1_opy_ (u"ࠨࡴࠪഡ")) as f:
          content = f.read().strip()
          if content:
            bstack1l11l1ll1l_opy_ = json.loads(content)
      bstack1l11l1ll1l_opy_[item_index] = platform_index
      with open(bstack11l1ll1l1l_opy_, bstack1l1lll1_opy_ (u"ࠤࡺࠦഢ")) as outfile:
        json.dump(bstack1l11l1ll1l_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1l1lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡽࡲࡪࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨണ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack11l1ll1l1l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack1l11l1ll1l_opy_ = {}
      if os.path.exists(bstack11l1ll1l1l_opy_):
        with open(bstack11l1ll1l1l_opy_, bstack1l1lll1_opy_ (u"ࠫࡷ࠭ത")) as f:
          content = f.read().strip()
          if content:
            bstack1l11l1ll1l_opy_ = json.loads(content)
      bstack1l11l1ll1l_opy_[item_index] = platform_index
      with open(bstack11l1ll1l1l_opy_, bstack1l1lll1_opy_ (u"ࠧࡽࠢഥ")) as outfile:
        json.dump(bstack1l11l1ll1l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡹࡵ࡭ࡹ࡯࡮ࡨࠢࡷࡳࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫദ") + str(e))
def bstack11111l11ll_opy_(bstack111lll111_opy_):
  global CONFIG
  bstack1l1llllll1_opy_ = bstack1l1lll1_opy_ (u"ࠧࠨധ")
  if not bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫന") in CONFIG:
    logger.info(bstack1l1lll1_opy_ (u"ࠩࡑࡳࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠡࡲࡤࡷࡸ࡫ࡤࠡࡷࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫࡮ࡦࡴࡤࡸࡪࠦࡲࡦࡲࡲࡶࡹࠦࡦࡰࡴࠣࡖࡴࡨ࡯ࡵࠢࡵࡹࡳ࠭ഩ"))
  try:
    platform = CONFIG[bstack1l1lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭പ")][bstack111lll111_opy_]
    if bstack1l1lll1_opy_ (u"ࠫࡴࡹࠧഫ") in platform:
      bstack1l1llllll1_opy_ += str(platform[bstack1l1lll1_opy_ (u"ࠬࡵࡳࠨബ")]) + bstack1l1lll1_opy_ (u"࠭ࠬࠡࠩഭ")
    if bstack1l1lll1_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪമ") in platform:
      bstack1l1llllll1_opy_ += str(platform[bstack1l1lll1_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫയ")]) + bstack1l1lll1_opy_ (u"ࠩ࠯ࠤࠬര")
    if bstack1l1lll1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧറ") in platform:
      bstack1l1llllll1_opy_ += str(platform[bstack1l1lll1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨല")]) + bstack1l1lll1_opy_ (u"ࠬ࠲ࠠࠨള")
    if bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨഴ") in platform:
      bstack1l1llllll1_opy_ += str(platform[bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩവ")]) + bstack1l1lll1_opy_ (u"ࠨ࠮ࠣࠫശ")
    if bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧഷ") in platform:
      bstack1l1llllll1_opy_ += str(platform[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨസ")]) + bstack1l1lll1_opy_ (u"ࠫ࠱ࠦࠧഹ")
    if bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ഺ") in platform:
      bstack1l1llllll1_opy_ += str(platform[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴ഻ࠧ")]) + bstack1l1lll1_opy_ (u"഼ࠧ࠭ࠢࠪ")
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠨࡕࡲࡱࡪࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡴࡶࡵ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡷ࡫ࡰࡰࡴࡷࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡵ࡮ࠨഽ") + str(e))
  finally:
    if bstack1l1llllll1_opy_[len(bstack1l1llllll1_opy_) - 2:] == bstack1l1lll1_opy_ (u"ࠩ࠯ࠤࠬാ"):
      bstack1l1llllll1_opy_ = bstack1l1llllll1_opy_[:-2]
    return bstack1l1llllll1_opy_
def bstack1lll111ll_opy_(path, bstack1l1llllll1_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l1l111ll_opy_ = ET.parse(path)
    bstack1l1ll1ll1l_opy_ = bstack1l1l111ll_opy_.getroot()
    bstack1ll1ll11l1_opy_ = None
    for suite in bstack1l1ll1ll1l_opy_.iter(bstack1l1lll1_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩി")):
      if bstack1l1lll1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫീ") in suite.attrib:
        suite.attrib[bstack1l1lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪു")] += bstack1l1lll1_opy_ (u"࠭ࠠࠨൂ") + bstack1l1llllll1_opy_
        bstack1ll1ll11l1_opy_ = suite
    bstack1l1ll1lll_opy_ = None
    for robot in bstack1l1ll1ll1l_opy_.iter(bstack1l1lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ൃ")):
      bstack1l1ll1lll_opy_ = robot
    bstack1l1lll11ll_opy_ = len(bstack1l1ll1lll_opy_.findall(bstack1l1lll1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧൄ")))
    if bstack1l1lll11ll_opy_ == 1:
      bstack1l1ll1lll_opy_.remove(bstack1l1ll1lll_opy_.findall(bstack1l1lll1_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨ൅"))[0])
      bstack1l111ll1l_opy_ = ET.Element(bstack1l1lll1_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩെ"), attrib={bstack1l1lll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩേ"): bstack1l1lll1_opy_ (u"࡙ࠬࡵࡪࡶࡨࡷࠬൈ"), bstack1l1lll1_opy_ (u"࠭ࡩࡥࠩ൉"): bstack1l1lll1_opy_ (u"ࠧࡴ࠲ࠪൊ")})
      bstack1l1ll1lll_opy_.insert(1, bstack1l111ll1l_opy_)
      bstack1ll111lll1_opy_ = None
      for suite in bstack1l1ll1lll_opy_.iter(bstack1l1lll1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧോ")):
        bstack1ll111lll1_opy_ = suite
      bstack1ll111lll1_opy_.append(bstack1ll1ll11l1_opy_)
      bstack1ll1111ll_opy_ = None
      for status in bstack1ll1ll11l1_opy_.iter(bstack1l1lll1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩൌ")):
        bstack1ll1111ll_opy_ = status
      bstack1ll111lll1_opy_.append(bstack1ll1111ll_opy_)
    bstack1l1l111ll_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡳࡵ࡬ࡲ࡬ࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠨ്") + str(e))
def bstack1ll1l1ll11_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack11l111l11l_opy_
  global CONFIG
  if bstack1l1lll1_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡴࡦࡺࡨࠣൎ") in options:
    del options[bstack1l1lll1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡵࡧࡴࡩࠤ൏")]
  json_data = bstack1l11l1llll_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack1l1lll1_opy_ (u"࠭ࡰࡢࡤࡲࡸࡤࡸࡥࡴࡷ࡯ࡸࡸ࠭൐"), str(item_id), bstack1l1lll1_opy_ (u"ࠧࡰࡷࡷࡴࡺࡺ࠮ࡹ࡯࡯ࠫ൑"))
    bstack1lll111ll_opy_(path, bstack11111l11ll_opy_(json_data[item_id]))
  bstack1l1l1l111_opy_()
  return bstack11l111l11l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack111llllll1_opy_(self, ff_profile_dir):
  global bstack11ll111111_opy_
  if not ff_profile_dir:
    return None
  return bstack11ll111111_opy_(self, ff_profile_dir)
def bstack1ll11lll1l_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1111l11l1_opy_
  bstack11111lll1_opy_ = []
  if bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ൒") in CONFIG:
    bstack11111lll1_opy_ = CONFIG[bstack1l1lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ൓")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1l1lll1_opy_ (u"ࠥࡧࡴࡳ࡭ࡢࡰࡧࠦൔ")],
      pabot_args[bstack1l1lll1_opy_ (u"ࠦࡻ࡫ࡲࡣࡱࡶࡩࠧൕ")],
      argfile,
      pabot_args.get(bstack1l1lll1_opy_ (u"ࠧ࡮ࡩࡷࡧࠥൖ")),
      pabot_args[bstack1l1lll1_opy_ (u"ࠨࡰࡳࡱࡦࡩࡸࡹࡥࡴࠤൗ")],
      platform[0],
      bstack1111l11l1_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1l1lll1_opy_ (u"ࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡨ࡬ࡰࡪࡹࠢ൘")] or [(bstack1l1lll1_opy_ (u"ࠣࠤ൙"), None)]
    for platform in enumerate(bstack11111lll1_opy_)
  ]
def bstack1111ll11l1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1ll1ll1l11_opy_=bstack1l1lll1_opy_ (u"ࠩࠪ൚")):
  global bstack11l1ll1111_opy_
  self.platform_index = platform_index
  self.bstack1ll111lll_opy_ = bstack1ll1ll1l11_opy_
  bstack11l1ll1111_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1l1l111l1_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l1ll1111_opy_
  global bstack1111ll11ll_opy_
  bstack11111l1l1_opy_ = copy.deepcopy(item)
  if not bstack1l1lll1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ൛") in item.options:
    bstack11111l1l1_opy_.options[bstack1l1lll1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭൜")] = []
  bstack1l1lllll1_opy_ = bstack11111l1l1_opy_.options[bstack1l1lll1_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ൝")].copy()
  for v in bstack11111l1l1_opy_.options[bstack1l1lll1_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ൞")]:
    if bstack1l1lll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭ൟ") in v:
      bstack1l1lllll1_opy_.remove(v)
    if bstack1l1lll1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡄࡎࡌࡅࡗࡍࡓࠨൠ") in v:
      bstack1l1lllll1_opy_.remove(v)
    if bstack1l1lll1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ൡ") in v:
      bstack1l1lllll1_opy_.remove(v)
  bstack1l1lllll1_opy_.insert(0, bstack1l1lll1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙࠼ࡾࢁࠬൢ").format(bstack11111l1l1_opy_.platform_index))
  bstack1l1lllll1_opy_.insert(0, bstack1l1lll1_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡈࡊࡌࡌࡐࡅࡄࡐࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒ࠻ࡽࢀࠫൣ").format(bstack11111l1l1_opy_.bstack1ll111lll_opy_))
  bstack11111l1l1_opy_.options[bstack1l1lll1_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ൤")] = bstack1l1lllll1_opy_
  if bstack1111ll11ll_opy_:
    bstack11111l1l1_opy_.options[bstack1l1lll1_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ൥")].insert(0, bstack1l1lll1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙࠺ࡼࡿࠪ൦").format(bstack1111ll11ll_opy_))
  return bstack1l1ll1111_opy_(caller_id, datasources, is_last, bstack11111l1l1_opy_, outs_dir)
def bstack11l11l1111_opy_(command, item_index):
  try:
    if bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ൧")):
      os.environ[bstack1l1lll1_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ൨")] = json.dumps(CONFIG[bstack1l1lll1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭൩")][item_index % bstack11ll11l11l_opy_])
    global bstack1111ll11ll_opy_
    if bstack1111ll11ll_opy_:
      command[0] = command[0].replace(bstack1l1lll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ൪"), bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡸࡪ࡫ࠡࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠢ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠡࠩ൫") + str(
        item_index) + bstack1l1lll1_opy_ (u"࠭ࠠࠨ൬") + bstack1111ll11ll_opy_, 1)
    else:
      command[0] = command[0].replace(bstack1l1lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭൭"),
                                      bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡴࡦ࡮ࠤࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠥ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠤࠬ൮") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack1l1lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡯ࡲࡨ࡮࡬ࡹࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࠥ࡬࡯ࡳࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲ࠿ࠦࡻࡾࠩ൯").format(str(e)))
def bstack111llllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack11l11l111l_opy_
  try:
    bstack11l11l1111_opy_(command, item_index)
    return bstack11l11l111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack1l1lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮࠻ࠢࡾࢁࠬ൰").format(str(e)))
    raise e
def bstack1111l11l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack11l11l111l_opy_
  try:
    bstack11l11l1111_opy_(command, item_index)
    return bstack11l11l111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack1l1lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠵࠲࠶࠹࠺ࠡࡽࢀࠫ൱").format(str(e)))
    try:
      return bstack11l11l111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack1l1lll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦ࠲࠯࠳࠶ࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪ൲").format(str(e2)))
      raise e
def bstack111l11111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack11l11l111l_opy_
  try:
    bstack11l11l1111_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack11l11l111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack1l1lll1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠷࠴࠱࠶࠼ࠣࡿࢂ࠭൳").format(str(e)))
    try:
      return bstack11l11l111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack1l1lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡ࠴࠱࠵࠺ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࡾࢁࠬ൴").format(str(e2)))
      raise e
def _1ll111ll1_opy_(bstack1l1llll1l_opy_, item_index, process_timeout, sleep_before_start, bstack1ll11l1l1_opy_):
  bstack11l11l1111_opy_(bstack1l1llll1l_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack11lll111l_opy_(command, bstack11lllll11l_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11l11l111l_opy_
  try:
    bstack11l11l1111_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack11l11l111l_opy_(command, bstack11lllll11l_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1l1lll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࠦ࠵࠯࠲࠽ࠤࢀࢃࠧ൵").format(str(e)))
    try:
      return bstack11l11l111l_opy_(command, bstack11lllll11l_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1l1lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩ൶").format(str(e2)))
      raise e
def bstack111l1lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11l11l111l_opy_
  try:
    process_timeout = _1ll111ll1_opy_(command, item_index, process_timeout, sleep_before_start, bstack1l1lll1_opy_ (u"ࠪ࠸࠳࠸ࠧ൷"))
    return bstack11l11l111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1l1lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠷࠲࠷ࡀࠠࡼࡿࠪ൸").format(str(e)))
    try:
      return bstack11l11l111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1l1lll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࡾࢁࠬ൹").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack11l111l1l1_opy_(self, runner, quiet=False, capture=True):
  global bstack1ll11ll1l_opy_
  bstack1lll1lll11_opy_ = bstack1ll11ll1l_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack1l1lll1_opy_ (u"࠭ࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࡡࡤࡶࡷ࠭ൺ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1l1lll1_opy_ (u"ࠧࡦࡺࡦࡣࡹࡸࡡࡤࡧࡥࡥࡨࡱ࡟ࡢࡴࡵࠫൻ")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1lll1lll11_opy_
def bstack11l1l1l11_opy_(runner, hook_name, context, element, bstack11ll1ll1l1_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1l1ll1llll_opy_.bstack11ll1111_opy_(hook_name, element)
    bstack11ll1ll1l1_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1l1ll1llll_opy_.bstack11l1ll11_opy_(element)
      if hook_name not in [bstack1l1lll1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠬർ"), bstack1l1lll1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡣ࡯ࡰࠬൽ")] and args and hasattr(args[0], bstack1l1lll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡡࡰࡩࡸࡹࡡࡨࡧࠪൾ")):
        args[0].error_message = bstack1l1lll1_opy_ (u"ࠫࠬൿ")
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡪࡤࡲࡩࡲࡥࠡࡪࡲࡳࡰࡹࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧ࠽ࠤࢀࢃࠧ඀").format(str(e)))
@measure(event_name=EVENTS.bstack111ll1l1l_opy_, stage=STAGE.bstack1111llll1l_opy_, hook_type=bstack1l1lll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡇ࡬࡭ࠤඁ"), bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1l11111lll_opy_(runner, name, context, bstack11ll1ll1l1_opy_, *args):
    if runner.hooks.get(bstack1l1lll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦං")).__name__ != bstack1l1lll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࡤࡪࡥࡧࡣࡸࡰࡹࡥࡨࡰࡱ࡮ࠦඃ"):
      bstack11l1l1l11_opy_(runner, name, context, runner, bstack11ll1ll1l1_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1lll11ll1l_opy_(bstack1l1lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ඄")) else context.browser
      runner.driver_initialised = bstack1l1lll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢඅ")
    except Exception as e:
      logger.debug(bstack1l1lll1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡩࡸࡩࡷࡧࡵࠤ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡥࠡࡣࡷࡸࡷ࡯ࡢࡶࡶࡨ࠾ࠥࢁࡽࠨආ").format(str(e)))
def bstack11l1111l1_opy_(runner, name, context, bstack11ll1ll1l1_opy_, *args):
    bstack11l1l1l11_opy_(runner, name, context, context.feature, bstack11ll1ll1l1_opy_, *args)
    try:
      if not bstack1llll1l11l_opy_:
        bstack1111l1111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll11ll1l_opy_(bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫඇ")) else context.browser
        if is_driver_active(bstack1111l1111l_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack1l1lll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢඈ")
          bstack1l1111l1l_opy_ = str(runner.feature.name)
          bstack1l1ll1l111_opy_(context, bstack1l1111l1l_opy_)
          bstack1111l1111l_opy_.execute_script(bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬඉ") + json.dumps(bstack1l1111l1l_opy_) + bstack1l1lll1_opy_ (u"ࠨࡿࢀࠫඊ"))
    except Exception as e:
      logger.debug(bstack1l1lll1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡ࡫ࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩඋ").format(str(e)))
def bstack111111lll_opy_(runner, name, context, bstack11ll1ll1l1_opy_, *args):
    if hasattr(context, bstack1l1lll1_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬඌ")):
        bstack1l1ll1llll_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack1l1lll1_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ඍ")) else context.feature
    bstack11l1l1l11_opy_(runner, name, context, target, bstack11ll1ll1l1_opy_, *args)
@measure(event_name=EVENTS.bstack1l1llll1ll_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack111l1l1l1_opy_(runner, name, context, bstack11ll1ll1l1_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1l1ll1llll_opy_.start_test(context)
    bstack11l1l1l11_opy_(runner, name, context, context.scenario, bstack11ll1ll1l1_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack111llll1ll_opy_.bstack11l1ll11l_opy_(context, *args)
    try:
      bstack1111l1111l_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫඎ"), context.browser)
      if is_driver_active(bstack1111l1111l_opy_):
        bstack1l11ll1l_opy_.bstack111l111l1_opy_(bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඏ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack1l1lll1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤඐ")
        if (not bstack1llll1l11l_opy_):
          scenario_name = args[0].name
          feature_name = bstack1l1111l1l_opy_ = str(runner.feature.name)
          bstack1l1111l1l_opy_ = feature_name + bstack1l1lll1_opy_ (u"ࠨࠢ࠰ࠤࠬඑ") + scenario_name
          if runner.driver_initialised == bstack1l1lll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦඒ"):
            bstack1l1ll1l111_opy_(context, bstack1l1111l1l_opy_)
            bstack1111l1111l_opy_.execute_script(bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨඓ") + json.dumps(bstack1l1111l1l_opy_) + bstack1l1lll1_opy_ (u"ࠫࢂࢃࠧඔ"))
    except Exception as e:
      logger.debug(bstack1l1lll1_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰ࠼ࠣࡿࢂ࠭ඕ").format(str(e)))
@measure(event_name=EVENTS.bstack111ll1l1l_opy_, stage=STAGE.bstack1111llll1l_opy_, hook_type=bstack1l1lll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪ࡙ࡴࡦࡲࠥඖ"), bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack11l1l11111_opy_(runner, name, context, bstack11ll1ll1l1_opy_, *args):
    bstack11l1l1l11_opy_(runner, name, context, args[0], bstack11ll1ll1l1_opy_, *args)
    try:
      bstack1111l1111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll11ll1l_opy_(bstack1l1lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭඗")) else context.browser
      if is_driver_active(bstack1111l1111l_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack1l1lll1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨ඘")
        bstack1l1ll1llll_opy_.bstack11ll111l_opy_(args[0])
        if runner.driver_initialised == bstack1l1lll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢ඙"):
          feature_name = bstack1l1111l1l_opy_ = str(runner.feature.name)
          bstack1l1111l1l_opy_ = feature_name + bstack1l1lll1_opy_ (u"ࠪࠤ࠲ࠦࠧක") + context.scenario.name
          bstack1111l1111l_opy_.execute_script(bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩඛ") + json.dumps(bstack1l1111l1l_opy_) + bstack1l1lll1_opy_ (u"ࠬࢃࡽࠨග"))
    except Exception as e:
      logger.debug(bstack1l1lll1_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡷࡩࡵࡀࠠࡼࡿࠪඝ").format(str(e)))
@measure(event_name=EVENTS.bstack111ll1l1l_opy_, stage=STAGE.bstack1111llll1l_opy_, hook_type=bstack1l1lll1_opy_ (u"ࠢࡢࡨࡷࡩࡷ࡙ࡴࡦࡲࠥඞ"), bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1llll111l1_opy_(runner, name, context, bstack11ll1ll1l1_opy_, *args):
  bstack1l1ll1llll_opy_.bstack11l1lll1_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack1111l1111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧඟ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1111l1111l_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack1l1lll1_opy_ (u"ࠩ࡬ࡲࡸࡺࡥࡱࠩච")
        feature_name = bstack1l1111l1l_opy_ = str(runner.feature.name)
        bstack1l1111l1l_opy_ = feature_name + bstack1l1lll1_opy_ (u"ࠪࠤ࠲ࠦࠧඡ") + context.scenario.name
        bstack1111l1111l_opy_.execute_script(bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩජ") + json.dumps(bstack1l1111l1l_opy_) + bstack1l1lll1_opy_ (u"ࠬࢃࡽࠨඣ"))
    if str(step_status).lower() == bstack1l1lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ඤ"):
      bstack111ll1l1ll_opy_ = bstack1l1lll1_opy_ (u"ࠧࠨඥ")
      bstack11l111ll1l_opy_ = bstack1l1lll1_opy_ (u"ࠨࠩඦ")
      bstack111ll11l1l_opy_ = bstack1l1lll1_opy_ (u"ࠩࠪට")
      try:
        import traceback
        bstack111ll1l1ll_opy_ = runner.exception.__class__.__name__
        bstack11ll11l1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11l111ll1l_opy_ = bstack1l1lll1_opy_ (u"ࠪࠤࠬඨ").join(bstack11ll11l1_opy_)
        bstack111ll11l1l_opy_ = bstack11ll11l1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l1ll1l11l_opy_.format(str(e)))
      bstack111ll1l1ll_opy_ += bstack111ll11l1l_opy_
      bstack11l1l11l1l_opy_(context, json.dumps(str(args[0].name) + bstack1l1lll1_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥඩ") + str(bstack11l111ll1l_opy_)),
                          bstack1l1lll1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦඪ"))
      if runner.driver_initialised == bstack1l1lll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦණ"):
        bstack1111l1ll11_opy_(getattr(context, bstack1l1lll1_opy_ (u"ࠧࡱࡣࡪࡩࠬඬ"), None), bstack1l1lll1_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣත"), bstack111ll1l1ll_opy_)
        bstack1111l1111l_opy_.execute_script(bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧථ") + json.dumps(str(args[0].name) + bstack1l1lll1_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤද") + str(bstack11l111ll1l_opy_)) + bstack1l1lll1_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫධ"))
      if runner.driver_initialised == bstack1l1lll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥන"):
        bstack111lll1111_opy_(bstack1111l1111l_opy_, bstack1l1lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭඲"), bstack1l1lll1_opy_ (u"ࠢࡔࡥࡨࡲࡦࡸࡩࡰࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦඳ") + str(bstack111ll1l1ll_opy_))
    else:
      bstack11l1l11l1l_opy_(context, bstack1l1lll1_opy_ (u"ࠣࡒࡤࡷࡸ࡫ࡤࠢࠤප"), bstack1l1lll1_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢඵ"))
      if runner.driver_initialised == bstack1l1lll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣබ"):
        bstack1111l1ll11_opy_(getattr(context, bstack1l1lll1_opy_ (u"ࠫࡵࡧࡧࡦࠩභ"), None), bstack1l1lll1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧම"))
      bstack1111l1111l_opy_.execute_script(bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫඹ") + json.dumps(str(args[0].name) + bstack1l1lll1_opy_ (u"ࠢࠡ࠯ࠣࡔࡦࡹࡳࡦࡦࠤࠦය")) + bstack1l1lll1_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦࢂࢃࠧර"))
      if runner.driver_initialised == bstack1l1lll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢ඼"):
        bstack111lll1111_opy_(bstack1111l1111l_opy_, bstack1l1lll1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥල"))
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡵࡷࡩࡵࡀࠠࡼࡿࠪ඾").format(str(e)))
  bstack11l1l1l11_opy_(runner, name, context, args[0], bstack11ll1ll1l1_opy_, *args)
@measure(event_name=EVENTS.bstack1l1l11lll_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1ll1111l11_opy_(runner, name, context, bstack11ll1ll1l1_opy_, *args):
  bstack1l1ll1llll_opy_.end_test(args[0])
  try:
    bstack1ll1l111l1_opy_ = args[0].status.name
    bstack1111l1111l_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫ඿"), context.browser)
    bstack111llll1ll_opy_.bstack1111lll11l_opy_(bstack1111l1111l_opy_)
    if str(bstack1ll1l111l1_opy_).lower() == bstack1l1lll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ව"):
      bstack111ll1l1ll_opy_ = bstack1l1lll1_opy_ (u"ࠧࠨශ")
      bstack11l111ll1l_opy_ = bstack1l1lll1_opy_ (u"ࠨࠩෂ")
      bstack111ll11l1l_opy_ = bstack1l1lll1_opy_ (u"ࠩࠪස")
      try:
        import traceback
        bstack111ll1l1ll_opy_ = runner.exception.__class__.__name__
        bstack11ll11l1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11l111ll1l_opy_ = bstack1l1lll1_opy_ (u"ࠪࠤࠬහ").join(bstack11ll11l1_opy_)
        bstack111ll11l1l_opy_ = bstack11ll11l1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l1ll1l11l_opy_.format(str(e)))
      bstack111ll1l1ll_opy_ += bstack111ll11l1l_opy_
      bstack11l1l11l1l_opy_(context, json.dumps(str(args[0].name) + bstack1l1lll1_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥළ") + str(bstack11l111ll1l_opy_)),
                          bstack1l1lll1_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦෆ"))
      if runner.driver_initialised == bstack1l1lll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣ෇") or runner.driver_initialised == bstack1l1lll1_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧ෈"):
        bstack1111l1ll11_opy_(getattr(context, bstack1l1lll1_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭෉"), None), bstack1l1lll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ්"), bstack111ll1l1ll_opy_)
        bstack1111l1111l_opy_.execute_script(bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ෋") + json.dumps(str(args[0].name) + bstack1l1lll1_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥ෌") + str(bstack11l111ll1l_opy_)) + bstack1l1lll1_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤࢀࢁࠬ෍"))
      if runner.driver_initialised == bstack1l1lll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣ෎") or runner.driver_initialised == bstack1l1lll1_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧා"):
        bstack111lll1111_opy_(bstack1111l1111l_opy_, bstack1l1lll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨැ"), bstack1l1lll1_opy_ (u"ࠤࡖࡧࡪࡴࡡࡳ࡫ࡲࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨෑ") + str(bstack111ll1l1ll_opy_))
    else:
      bstack11l1l11l1l_opy_(context, bstack1l1lll1_opy_ (u"ࠥࡔࡦࡹࡳࡦࡦࠤࠦි"), bstack1l1lll1_opy_ (u"ࠦ࡮ࡴࡦࡰࠤී"))
      if runner.driver_initialised == bstack1l1lll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢු") or runner.driver_initialised == bstack1l1lll1_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෕"):
        bstack1111l1ll11_opy_(getattr(context, bstack1l1lll1_opy_ (u"ࠧࡱࡣࡪࡩࠬූ"), None), bstack1l1lll1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ෗"))
      bstack1111l1111l_opy_.execute_script(bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧෘ") + json.dumps(str(args[0].name) + bstack1l1lll1_opy_ (u"ࠥࠤ࠲ࠦࡐࡢࡵࡶࡩࡩࠧࠢෙ")) + bstack1l1lll1_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢࡾࡿࠪේ"))
      if runner.driver_initialised == bstack1l1lll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢෛ") or runner.driver_initialised == bstack1l1lll1_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭ො"):
        bstack111lll1111_opy_(bstack1111l1111l_opy_, bstack1l1lll1_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢෝ"))
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪෞ").format(str(e)))
  bstack11l1l1l11_opy_(runner, name, context, context.scenario, bstack11ll1ll1l1_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1l11l1l11_opy_(runner, name, context, bstack11ll1ll1l1_opy_, *args):
    target = context.scenario if hasattr(context, bstack1l1lll1_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫෟ")) else context.feature
    bstack11l1l1l11_opy_(runner, name, context, target, bstack11ll1ll1l1_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1l1l11l1l_opy_(runner, name, context, bstack11ll1ll1l1_opy_, *args):
    try:
      bstack1111l1111l_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ෠"), context.browser)
      bstack1111l1l11_opy_ = bstack1l1lll1_opy_ (u"ࠫࠬ෡")
      if context.failed is True:
        bstack1l11l11111_opy_ = []
        bstack1111ll1l1l_opy_ = []
        bstack11l11l1lll_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1l11l11111_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11ll11l1_opy_ = traceback.format_tb(exc_tb)
            bstack1l111lll1l_opy_ = bstack1l1lll1_opy_ (u"ࠬࠦࠧ෢").join(bstack11ll11l1_opy_)
            bstack1111ll1l1l_opy_.append(bstack1l111lll1l_opy_)
            bstack11l11l1lll_opy_.append(bstack11ll11l1_opy_[-1])
        except Exception as e:
          logger.debug(bstack1l1ll1l11l_opy_.format(str(e)))
        bstack111ll1l1ll_opy_ = bstack1l1lll1_opy_ (u"࠭ࠧ෣")
        for i in range(len(bstack1l11l11111_opy_)):
          bstack111ll1l1ll_opy_ += bstack1l11l11111_opy_[i] + bstack11l11l1lll_opy_[i] + bstack1l1lll1_opy_ (u"ࠧ࡝ࡰࠪ෤")
        bstack1111l1l11_opy_ = bstack1l1lll1_opy_ (u"ࠨࠢࠪ෥").join(bstack1111ll1l1l_opy_)
        if runner.driver_initialised in [bstack1l1lll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥ෦"), bstack1l1lll1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢ෧")]:
          bstack11l1l11l1l_opy_(context, bstack1111l1l11_opy_, bstack1l1lll1_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ෨"))
          bstack1111l1ll11_opy_(getattr(context, bstack1l1lll1_opy_ (u"ࠬࡶࡡࡨࡧࠪ෩"), None), bstack1l1lll1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ෪"), bstack111ll1l1ll_opy_)
          bstack1111l1111l_opy_.execute_script(bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ෫") + json.dumps(bstack1111l1l11_opy_) + bstack1l1lll1_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨ෬"))
          bstack111lll1111_opy_(bstack1111l1111l_opy_, bstack1l1lll1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ෭"), bstack1l1lll1_opy_ (u"ࠥࡗࡴࡳࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱࡶࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࡢ࡮ࠣ෮") + str(bstack111ll1l1ll_opy_))
          bstack11lll1111_opy_ = bstack1l1ll11ll_opy_(bstack1111l1l11_opy_, runner.feature.name, logger)
          if (bstack11lll1111_opy_ != None):
            bstack1l11llll1l_opy_.append(bstack11lll1111_opy_)
      else:
        if runner.driver_initialised in [bstack1l1lll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧ෯"), bstack1l1lll1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤ෰")]:
          bstack11l1l11l1l_opy_(context, bstack1l1lll1_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫࠺ࠡࠤ෱") + str(runner.feature.name) + bstack1l1lll1_opy_ (u"ࠢࠡࡲࡤࡷࡸ࡫ࡤࠢࠤෲ"), bstack1l1lll1_opy_ (u"ࠣ࡫ࡱࡪࡴࠨෳ"))
          bstack1111l1ll11_opy_(getattr(context, bstack1l1lll1_opy_ (u"ࠩࡳࡥ࡬࡫ࠧ෴"), None), bstack1l1lll1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ෵"))
          bstack1111l1111l_opy_.execute_script(bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ෶") + json.dumps(bstack1l1lll1_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣ෷") + str(runner.feature.name) + bstack1l1lll1_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣ෸")) + bstack1l1lll1_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭෹"))
          bstack111lll1111_opy_(bstack1111l1111l_opy_, bstack1l1lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ෺"))
          bstack11lll1111_opy_ = bstack1l1ll11ll_opy_(bstack1111l1l11_opy_, runner.feature.name, logger)
          if (bstack11lll1111_opy_ != None):
            bstack1l11llll1l_opy_.append(bstack11lll1111_opy_)
    except Exception as e:
      logger.debug(bstack1l1lll1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫ෻").format(str(e)))
    bstack11l1l1l11_opy_(runner, name, context, context.feature, bstack11ll1ll1l1_opy_, *args)
@measure(event_name=EVENTS.bstack111ll1l1l_opy_, stage=STAGE.bstack1111llll1l_opy_, hook_type=bstack1l1lll1_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࡃ࡯ࡰࠧ෼"), bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1lll1l1111_opy_(runner, name, context, bstack11ll1ll1l1_opy_, *args):
    bstack11l1l1l11_opy_(runner, name, context, runner, bstack11ll1ll1l1_opy_, *args)
def bstack111l11ll1_opy_(self, name, context, *args):
  try:
    if bstack11lll11111_opy_:
      platform_index = int(threading.current_thread()._name) % bstack11ll11l11l_opy_
      bstack11lll1ll11_opy_ = CONFIG[bstack1l1lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ෽")][platform_index]
      os.environ[bstack1l1lll1_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭෾")] = json.dumps(bstack11lll1ll11_opy_)
    global bstack11ll1ll1l1_opy_
    if not hasattr(self, bstack1l1lll1_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡧࡧࠫ෿")):
      self.driver_initialised = None
    bstack11ll1l1111_opy_ = {
        bstack1l1lll1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫ฀"): bstack1l11111lll_opy_,
        bstack1l1lll1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠩก"): bstack11l1111l1_opy_,
        bstack1l1lll1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡷࡥ࡬࠭ข"): bstack111111lll_opy_,
        bstack1l1lll1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬฃ"): bstack111l1l1l1_opy_,
        bstack1l1lll1_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠩค"): bstack11l1l11111_opy_,
        bstack1l1lll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡺࡥࡱࠩฅ"): bstack1llll111l1_opy_,
        bstack1l1lll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧฆ"): bstack1ll1111l11_opy_,
        bstack1l1lll1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡴࡢࡩࠪง"): bstack1l11l1l11_opy_,
        bstack1l1lll1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨจ"): bstack1l1l11l1l_opy_,
        bstack1l1lll1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡣ࡯ࡰࠬฉ"): bstack1lll1l1111_opy_
    }
    handler = bstack11ll1l1111_opy_.get(name, bstack11ll1ll1l1_opy_)
    try:
      handler(self, name, context, bstack11ll1ll1l1_opy_, *args)
    except Exception as e:
      logger.debug(bstack1l1lll1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩࠥ࡮࡯ࡰ࡭ࠣ࡬ࡦࡴࡤ࡭ࡧࡵࠤࢀࢃ࠺ࠡࡽࢀࠫช").format(name, str(e)))
    if name in [bstack1l1lll1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡪࡪࡧࡴࡶࡴࡨࠫซ"), bstack1l1lll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ฌ"), bstack1l1lll1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩญ")]:
      try:
        bstack1111l1111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll11ll1l_opy_(bstack1l1lll1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ฎ")) else context.browser
        bstack11l111l11_opy_ = (
          (name == bstack1l1lll1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫฏ") and self.driver_initialised == bstack1l1lll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨฐ")) or
          (name == bstack1l1lll1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪฑ") and self.driver_initialised == bstack1l1lll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧฒ")) or
          (name == bstack1l1lll1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ณ") and self.driver_initialised in [bstack1l1lll1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣด"), bstack1l1lll1_opy_ (u"ࠢࡪࡰࡶࡸࡪࡶࠢต")]) or
          (name == bstack1l1lll1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡶࡨࡴࠬถ") and self.driver_initialised == bstack1l1lll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢท"))
        )
        if bstack11l111l11_opy_:
          self.driver_initialised = None
          if bstack1111l1111l_opy_ and hasattr(bstack1111l1111l_opy_, bstack1l1lll1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧธ")):
            try:
              bstack1111l1111l_opy_.quit()
            except Exception as e:
              logger.debug(bstack1l1lll1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡵࡺ࡯ࡴࡵ࡫ࡱ࡫ࠥࡪࡲࡪࡸࡨࡶࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥࠡࡪࡲࡳࡰࡀࠠࡼࡿࠪน").format(str(e)))
      except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡨࡰࡱ࡮ࠤࡨࡲࡥࡢࡰࡸࡴࠥ࡬࡯ࡳࠢࡾࢁ࠿ࠦࡻࡾࠩบ").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"࠭ࡃࡳ࡫ࡷ࡭ࡨࡧ࡬ࠡࡧࡵࡶࡴࡸࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧࠣࡶࡺࡴࠠࡩࡱࡲ࡯ࠥࢁࡽ࠻ࠢࡾࢁࠬป").format(name, str(e)))
    try:
      bstack11ll1ll1l1_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack1l1lll1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡥࡱࡲࡢࡢࡥ࡮ࠤࡴࡸࡩࡨ࡫ࡱࡥࡱࠦࡢࡦࡪࡤࡺࡪࠦࡨࡰࡱ࡮ࠤࢀࢃ࠺ࠡࡽࢀࠫผ").format(name, str(e2)))
def bstack1lll1ll111_opy_(config, startdir):
  return bstack1l1lll1_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾ࠴ࢂࠨฝ").format(bstack1l1lll1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣพ"))
notset = Notset()
def bstack11l1l1ll1l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack111l1llll1_opy_
  if str(name).lower() == bstack1l1lll1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪฟ"):
    return bstack1l1lll1_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥภ")
  else:
    return bstack111l1llll1_opy_(self, name, default, skip)
def bstack1111ll11l_opy_(item, when):
  global bstack1l11111l11_opy_
  try:
    bstack1l11111l11_opy_(item, when)
  except Exception as e:
    pass
def bstack11l1l1ll11_opy_():
  return
def bstack1l11llll1_opy_(type, name, status, reason, bstack1ll1llll1l_opy_, bstack11111llll_opy_):
  bstack1ll11ll1l1_opy_ = {
    bstack1l1lll1_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬม"): type,
    bstack1l1lll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩย"): {}
  }
  if type == bstack1l1lll1_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩร"):
    bstack1ll11ll1l1_opy_[bstack1l1lll1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫฤ")][bstack1l1lll1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨล")] = bstack1ll1llll1l_opy_
    bstack1ll11ll1l1_opy_[bstack1l1lll1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ฦ")][bstack1l1lll1_opy_ (u"ࠫࡩࡧࡴࡢࠩว")] = json.dumps(str(bstack11111llll_opy_))
  if type == bstack1l1lll1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ศ"):
    bstack1ll11ll1l1_opy_[bstack1l1lll1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩษ")][bstack1l1lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬส")] = name
  if type == bstack1l1lll1_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫห"):
    bstack1ll11ll1l1_opy_[bstack1l1lll1_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬฬ")][bstack1l1lll1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪอ")] = status
    if status == bstack1l1lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫฮ"):
      bstack1ll11ll1l1_opy_[bstack1l1lll1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨฯ")][bstack1l1lll1_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ะ")] = json.dumps(str(reason))
  bstack1l1111111l_opy_ = bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬั").format(json.dumps(bstack1ll11ll1l1_opy_))
  return bstack1l1111111l_opy_
def bstack1l1l111l11_opy_(driver_command, response):
    if driver_command == bstack1l1lll1_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬา"):
        bstack1l11ll1l_opy_.bstack1l111ll11_opy_({
            bstack1l1lll1_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨำ"): response[bstack1l1lll1_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩิ")],
            bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫี"): bstack1l11ll1l_opy_.current_test_uuid()
        })
def bstack1ll111l1l_opy_(item, call, rep):
  global bstack111l1ll1l_opy_
  global bstack1l11l1111l_opy_
  global bstack1llll1l11l_opy_
  name = bstack1l1lll1_opy_ (u"ࠬ࠭ึ")
  try:
    if rep.when == bstack1l1lll1_opy_ (u"࠭ࡣࡢ࡮࡯ࠫื"):
      bstack11ll11111_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1llll1l11l_opy_:
          name = str(rep.nodeid)
          bstack1lllll11ll_opy_ = bstack1l11llll1_opy_(bstack1l1lll1_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨุ"), name, bstack1l1lll1_opy_ (u"ࠨูࠩ"), bstack1l1lll1_opy_ (u"ฺࠩࠪ"), bstack1l1lll1_opy_ (u"ࠪࠫ฻"), bstack1l1lll1_opy_ (u"ࠫࠬ฼"))
          threading.current_thread().bstack1lll1l11l1_opy_ = name
          for driver in bstack1l11l1111l_opy_:
            if bstack11ll11111_opy_ == driver.session_id:
              driver.execute_script(bstack1lllll11ll_opy_)
      except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ฽").format(str(e)))
      try:
        bstack1ll1ll1ll_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1l1lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ฾"):
          status = bstack1l1lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ฿") if rep.outcome.lower() == bstack1l1lll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨเ") else bstack1l1lll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩแ")
          reason = bstack1l1lll1_opy_ (u"ࠪࠫโ")
          if status == bstack1l1lll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫใ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1l1lll1_opy_ (u"ࠬ࡯࡮ࡧࡱࠪไ") if status == bstack1l1lll1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ๅ") else bstack1l1lll1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ๆ")
          data = name + bstack1l1lll1_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪ็") if status == bstack1l1lll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥ่ࠩ") else name + bstack1l1lll1_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧ้ࠥࠥ࠭") + reason
          bstack111111111_opy_ = bstack1l11llll1_opy_(bstack1l1lll1_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ๊࠭"), bstack1l1lll1_opy_ (u"๋ࠬ࠭"), bstack1l1lll1_opy_ (u"࠭ࠧ์"), bstack1l1lll1_opy_ (u"ࠧࠨํ"), level, data)
          for driver in bstack1l11l1111l_opy_:
            if bstack11ll11111_opy_ == driver.session_id:
              driver.execute_script(bstack111111111_opy_)
      except Exception as e:
        logger.debug(bstack1l1lll1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ๎").format(str(e)))
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭๏").format(str(e)))
  bstack111l1ll1l_opy_(item, call, rep)
def bstack1l11l11l1_opy_(driver, bstack11111llll1_opy_, test=None):
  global bstack1ll1l1l11l_opy_
  if test != None:
    bstack1111l11ll_opy_ = getattr(test, bstack1l1lll1_opy_ (u"ࠪࡲࡦࡳࡥࠨ๐"), None)
    bstack1l1lll111l_opy_ = getattr(test, bstack1l1lll1_opy_ (u"ࠫࡺࡻࡩࡥࠩ๑"), None)
    PercySDK.screenshot(driver, bstack11111llll1_opy_, bstack1111l11ll_opy_=bstack1111l11ll_opy_, bstack1l1lll111l_opy_=bstack1l1lll111l_opy_, bstack1l111l111l_opy_=bstack1ll1l1l11l_opy_)
  else:
    PercySDK.screenshot(driver, bstack11111llll1_opy_)
@measure(event_name=EVENTS.bstack1l1ll11l1l_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1ll1ll111_opy_(driver):
  if bstack1l11l11l1l_opy_.bstack1111l1lll_opy_() is True or bstack1l11l11l1l_opy_.capturing() is True:
    return
  bstack1l11l11l1l_opy_.bstack1lllll1l1l_opy_()
  while not bstack1l11l11l1l_opy_.bstack1111l1lll_opy_():
    bstack1lllll1111_opy_ = bstack1l11l11l1l_opy_.bstack1111l1l111_opy_()
    bstack1l11l11l1_opy_(driver, bstack1lllll1111_opy_)
  bstack1l11l11l1l_opy_.bstack1ll1l111ll_opy_()
def bstack1l11lll111_opy_(sequence, driver_command, response = None, bstack11ll111ll_opy_ = None, args = None):
    try:
      if sequence != bstack1l1lll1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬ๒"):
        return
      if percy.bstack111ll11l11_opy_() == bstack1l1lll1_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧ๓"):
        return
      bstack1lllll1111_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ๔"), None)
      for command in bstack111l11l111_opy_:
        if command == driver_command:
          with bstack1l1l1lll1l_opy_:
            bstack111ll11111_opy_ = bstack1l11l1111l_opy_.copy()
          for driver in bstack111ll11111_opy_:
            bstack1ll1ll111_opy_(driver)
      bstack111lll1l1l_opy_ = percy.bstack11l1ll11l1_opy_()
      if driver_command in bstack11lllll11_opy_[bstack111lll1l1l_opy_]:
        bstack1l11l11l1l_opy_.bstack1ll111l1l1_opy_(bstack1lllll1111_opy_, driver_command)
    except Exception as e:
      pass
def bstack1l11ll1ll1_opy_(framework_name):
  if bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬ๕")):
      return
  bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭๖"), True)
  global bstack1l1ll111l1_opy_
  global bstack1l11l111l_opy_
  global bstack111l111l11_opy_
  bstack1l1ll111l1_opy_ = framework_name
  logger.info(bstack1ll11l11l1_opy_.format(bstack1l1ll111l1_opy_.split(bstack1l1lll1_opy_ (u"ࠪ࠱ࠬ๗"))[0]))
  bstack1111l11ll1_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack11lll11111_opy_:
      Service.start = bstack11l11ll1ll_opy_
      Service.stop = bstack1l11lll11_opy_
      webdriver.Remote.get = bstack1l1l1lll11_opy_
      WebDriver.quit = bstack1l1ll1ll1_opy_
      webdriver.Remote.__init__ = bstack11111lll1l_opy_
    if not bstack11lll11111_opy_:
        webdriver.Remote.__init__ = bstack11l1l1lll1_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack1ll11lll1_opy_
    bstack1l11l111l_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack11lll11111_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack11ll1111l_opy_
  except Exception as e:
    pass
  bstack111lll11l_opy_()
  if not bstack1l11l111l_opy_:
    bstack1ll1ll1ll1_opy_(bstack1l1lll1_opy_ (u"ࠦࡕࡧࡣ࡬ࡣࡪࡩࡸࠦ࡮ࡰࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠨ๘"), bstack1l1111lll1_opy_)
  if bstack1l1l1llll_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack1l1lll1_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭๙")) and callable(getattr(RemoteConnection, bstack1l1lll1_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ๚"))):
        RemoteConnection._get_proxy_url = bstack111l11lll_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack111l11lll_opy_
    except Exception as e:
      logger.error(bstack11111l11l1_opy_.format(str(e)))
  if bstack1ll1l11l1_opy_():
    bstack1l11ll1l1_opy_(CONFIG, logger)
  if (bstack1l1lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭๛") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack111ll11l11_opy_() == bstack1l1lll1_opy_ (u"ࠣࡶࡵࡹࡪࠨ๜"):
          bstack1lll1l111l_opy_(bstack1l11lll111_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack111llllll1_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l1l11ll1l_opy_
      except Exception as e:
        logger.warn(bstack11111ll1ll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1111ll1lll_opy_
      except Exception as e:
        logger.debug(bstack11l1ll1ll1_opy_ + str(e))
    except Exception as e:
      bstack1ll1ll1ll1_opy_(e, bstack11111ll1ll_opy_)
    Output.start_test = bstack1111l1l1l_opy_
    Output.end_test = bstack11ll1ll11l_opy_
    TestStatus.__init__ = bstack11llll1l1l_opy_
    QueueItem.__init__ = bstack1111ll11l1_opy_
    pabot._create_items = bstack1ll11lll1l_opy_
    try:
      from pabot import __version__ as bstack11l1ll1l1_opy_
      if version.parse(bstack11l1ll1l1_opy_) >= version.parse(bstack1l1lll1_opy_ (u"ࠩ࠸࠲࠵࠴࠰ࠨ๝")):
        pabot._run = bstack11lll111l_opy_
      elif version.parse(bstack11l1ll1l1_opy_) >= version.parse(bstack1l1lll1_opy_ (u"ࠪ࠸࠳࠸࠮࠱ࠩ๞")):
        pabot._run = bstack111l1lllll_opy_
      elif version.parse(bstack11l1ll1l1_opy_) >= version.parse(bstack1l1lll1_opy_ (u"ࠫ࠷࠴࠱࠶࠰࠳ࠫ๟")):
        pabot._run = bstack111l11111_opy_
      elif version.parse(bstack11l1ll1l1_opy_) >= version.parse(bstack1l1lll1_opy_ (u"ࠬ࠸࠮࠲࠵࠱࠴ࠬ๠")):
        pabot._run = bstack1111l11l1l_opy_
      else:
        pabot._run = bstack111llllll_opy_
    except Exception as e:
      pabot._run = bstack111llllll_opy_
    pabot._create_command_for_execution = bstack1l1l111l1_opy_
    pabot._report_results = bstack1ll1l1ll11_opy_
  if bstack1l1lll1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭๡") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll1ll1ll1_opy_(e, bstack1l1ll1lll1_opy_)
    Runner.run_hook = bstack111l11ll1_opy_
    Step.run = bstack11l111l1l1_opy_
  if bstack1l1lll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ๢") in str(framework_name).lower():
    if not bstack11lll11111_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1lll1ll111_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack11l1l1ll11_opy_
      Config.getoption = bstack11l1l1ll1l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1ll111l1l_opy_
    except Exception as e:
      pass
def bstack1l11ll111_opy_():
  global CONFIG
  if bstack1l1lll1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ๣") in CONFIG and int(CONFIG[bstack1l1lll1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ๤")]) > 1:
    logger.warn(bstack1ll11l111l_opy_)
def bstack1ll111l11l_opy_(arg, bstack1llllll1l_opy_, bstack11lll11ll1_opy_=None):
  global CONFIG
  global bstack1l111lllll_opy_
  global bstack1l1lllllll_opy_
  global bstack11lll11111_opy_
  global bstack1111111l_opy_
  bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ๥")
  if bstack1llllll1l_opy_ and isinstance(bstack1llllll1l_opy_, str):
    bstack1llllll1l_opy_ = eval(bstack1llllll1l_opy_)
  CONFIG = bstack1llllll1l_opy_[bstack1l1lll1_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫ๦")]
  bstack1l111lllll_opy_ = bstack1llllll1l_opy_[bstack1l1lll1_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭๧")]
  bstack1l1lllllll_opy_ = bstack1llllll1l_opy_[bstack1l1lll1_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ๨")]
  bstack11lll11111_opy_ = bstack1llllll1l_opy_[bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪ๩")]
  bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ๪"), bstack11lll11111_opy_)
  os.environ[bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ๫")] = bstack11l11ll11_opy_
  os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠩ๬")] = json.dumps(CONFIG)
  os.environ[bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡌ࡚ࡈ࡟ࡖࡔࡏࠫ๭")] = bstack1l111lllll_opy_
  os.environ[bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭๮")] = str(bstack1l1lllllll_opy_)
  os.environ[bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡌࡖࡉࡌࡒࠬ๯")] = str(True)
  if bstack1111ll1l1_opy_(arg, [bstack1l1lll1_opy_ (u"ࠧ࠮ࡰࠪ๰"), bstack1l1lll1_opy_ (u"ࠨ࠯࠰ࡲࡺࡳࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ๱")]) != -1:
    os.environ[bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡄࡖࡆࡒࡌࡆࡎࠪ๲")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1l11lllll_opy_)
    return
  bstack11l11llll1_opy_()
  global bstack1ll11l1l1l_opy_
  global bstack1ll1l1l11l_opy_
  global bstack1111l11l1_opy_
  global bstack1111ll11ll_opy_
  global bstack11111ll11_opy_
  global bstack111l111l11_opy_
  global bstack11lll1111l_opy_
  arg.append(bstack1l1lll1_opy_ (u"ࠥ࠱࡜ࠨ๳"))
  arg.append(bstack1l1lll1_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨ࠾ࡒࡵࡤࡶ࡮ࡨࠤࡦࡲࡲࡦࡣࡧࡽࠥ࡯࡭ࡱࡱࡵࡸࡪࡪ࠺ࡱࡻࡷࡩࡸࡺ࠮ࡑࡻࡷࡩࡸࡺࡗࡢࡴࡱ࡭ࡳ࡭ࠢ๴"))
  arg.append(bstack1l1lll1_opy_ (u"ࠧ࠳ࡗࠣ๵"))
  arg.append(bstack1l1lll1_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡀࡔࡩࡧࠣ࡬ࡴࡵ࡫ࡪ࡯ࡳࡰࠧ๶"))
  global bstack1l111ll111_opy_
  global bstack11ll11lll1_opy_
  global bstack11l111l1ll_opy_
  global bstack1l1l11l1ll_opy_
  global bstack11ll111111_opy_
  global bstack11l1ll1111_opy_
  global bstack1l1ll1111_opy_
  global bstack1l111111ll_opy_
  global bstack11llll11l_opy_
  global bstack11lllll1l1_opy_
  global bstack111l1llll1_opy_
  global bstack1l11111l11_opy_
  global bstack111l1ll1l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l111ll111_opy_ = webdriver.Remote.__init__
    bstack11ll11lll1_opy_ = WebDriver.quit
    bstack1l111111ll_opy_ = WebDriver.close
    bstack11llll11l_opy_ = WebDriver.get
    bstack11l111l1ll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1lll11lll1_opy_(CONFIG) and bstack111l1l11ll_opy_():
    if bstack1ll1ll11ll_opy_() < version.parse(bstack11ll1l1ll_opy_):
      logger.error(bstack1ll1l1l11_opy_.format(bstack1ll1ll11ll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1l1lll1_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ๷")) and callable(getattr(RemoteConnection, bstack1l1lll1_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ๸"))):
          bstack11lllll1l1_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack11lllll1l1_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack11111l11l1_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack111l1llll1_opy_ = Config.getoption
    from _pytest import runner
    bstack1l11111l11_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack11l11l11_opy_)
  try:
    from pytest_bdd import reporting
    bstack111l1ll1l_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1l1lll1_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪ๹"))
  bstack1111l11l1_opy_ = CONFIG.get(bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ๺"), {}).get(bstack1l1lll1_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭๻"))
  bstack11lll1111l_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack11lll11lll_opy_():
      bstack1llll111ll_opy_.invoke(Events.CONNECT, bstack1lll1l1l1l_opy_())
    platform_index = int(os.environ.get(bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ๼"), bstack1l1lll1_opy_ (u"࠭࠰ࠨ๽")))
  else:
    bstack1l11ll1ll1_opy_(bstack1111lllll1_opy_)
  os.environ[bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨ๾")] = CONFIG[bstack1l1lll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ๿")]
  os.environ[bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬ຀")] = CONFIG[bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ກ")]
  os.environ[bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧຂ")] = bstack11lll11111_opy_.__str__()
  from _pytest.config import main as bstack11lll1l1ll_opy_
  bstack1lll1l1l11_opy_ = []
  try:
    exit_code = bstack11lll1l1ll_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1lll111l1_opy_()
    if bstack1l1lll1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵࠩ຃") in multiprocessing.current_process().__dict__.keys():
      for bstack1l11l1l1ll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1lll1l1l11_opy_.append(bstack1l11l1l1ll_opy_)
    try:
      bstack111111l11_opy_ = (bstack1lll1l1l11_opy_, int(exit_code))
      bstack11lll11ll1_opy_.append(bstack111111l11_opy_)
    except:
      bstack11lll11ll1_opy_.append((bstack1lll1l1l11_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1lll1l1l11_opy_.append({bstack1l1lll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫຄ"): bstack1l1lll1_opy_ (u"ࠧࡑࡴࡲࡧࡪࡹࡳࠡࠩ຅") + os.environ.get(bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨຆ")), bstack1l1lll1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨງ"): traceback.format_exc(), bstack1l1lll1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩຈ"): int(os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫຉ")))})
    bstack11lll11ll1_opy_.append((bstack1lll1l1l11_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack1l1lll1_opy_ (u"ࠧࡸࡥࡵࡴ࡬ࡩࡸࠨຊ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack11l1llllll_opy_ = e.__class__.__name__
    print(bstack1l1lll1_opy_ (u"ࠨࠥࡴ࠼ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡵࡹࡳࡴࡩ࡯ࡩࠣࡦࡪ࡮ࡡࡷࡧࠣࡸࡪࡹࡴࠡࠧࡶࠦ຋") % (bstack11l1llllll_opy_, e))
    return 1
def bstack1l1l1111ll_opy_(arg):
  global bstack1l11lll1ll_opy_
  bstack1l11ll1ll1_opy_(bstack1ll11ll111_opy_)
  os.environ[bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨຌ")] = str(bstack1l1lllllll_opy_)
  retries = bstack1111llll_opy_.bstack1lllll111_opy_(CONFIG)
  status_code = 0
  if bstack1111llll_opy_.bstack1lll1l1ll_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack1ll11l1111_opy_
    status_code = bstack1ll11l1111_opy_(arg)
  if status_code != 0:
    bstack1l11lll1ll_opy_ = status_code
def bstack1111llllll_opy_():
  logger.info(bstack1111llll1_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1l1lll1_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧຍ"), help=bstack1l1lll1_opy_ (u"ࠩࡊࡩࡳ࡫ࡲࡢࡶࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡧࡴࡴࡦࡪࡩࠪຎ"))
  parser.add_argument(bstack1l1lll1_opy_ (u"ࠪ࠱ࡺ࠭ຏ"), bstack1l1lll1_opy_ (u"ࠫ࠲࠳ࡵࡴࡧࡵࡲࡦࡳࡥࠨຐ"), help=bstack1l1lll1_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫຑ"))
  parser.add_argument(bstack1l1lll1_opy_ (u"࠭࠭࡬ࠩຒ"), bstack1l1lll1_opy_ (u"ࠧ࠮࠯࡮ࡩࡾ࠭ຓ"), help=bstack1l1lll1_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡧࡣࡤࡧࡶࡷࠥࡱࡥࡺࠩດ"))
  parser.add_argument(bstack1l1lll1_opy_ (u"ࠩ࠰ࡪࠬຕ"), bstack1l1lll1_opy_ (u"ࠪ࠱࠲࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨຖ"), help=bstack1l1lll1_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡷࡩࡸࡺࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪທ"))
  bstack1lllll1l11_opy_ = parser.parse_args()
  try:
    bstack1l1lllll1l_opy_ = bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡮ࡦࡴ࡬ࡧ࠳ࡿ࡭࡭࠰ࡶࡥࡲࡶ࡬ࡦࠩຘ")
    if bstack1lllll1l11_opy_.framework and bstack1lllll1l11_opy_.framework not in (bstack1l1lll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ນ"), bstack1l1lll1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨບ")):
      bstack1l1lllll1l_opy_ = bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧປ")
    bstack1l1ll11l11_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1lllll1l_opy_)
    bstack1lllll111l_opy_ = open(bstack1l1ll11l11_opy_, bstack1l1lll1_opy_ (u"ࠩࡵࠫຜ"))
    bstack1ll1111lll_opy_ = bstack1lllll111l_opy_.read()
    bstack1lllll111l_opy_.close()
    if bstack1lllll1l11_opy_.username:
      bstack1ll1111lll_opy_ = bstack1ll1111lll_opy_.replace(bstack1l1lll1_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪຝ"), bstack1lllll1l11_opy_.username)
    if bstack1lllll1l11_opy_.key:
      bstack1ll1111lll_opy_ = bstack1ll1111lll_opy_.replace(bstack1l1lll1_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭ພ"), bstack1lllll1l11_opy_.key)
    if bstack1lllll1l11_opy_.framework:
      bstack1ll1111lll_opy_ = bstack1ll1111lll_opy_.replace(bstack1l1lll1_opy_ (u"ࠬ࡟ࡏࡖࡔࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ຟ"), bstack1lllll1l11_opy_.framework)
    file_name = bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩຠ")
    file_path = os.path.abspath(file_name)
    bstack1l1lll11l1_opy_ = open(file_path, bstack1l1lll1_opy_ (u"ࠧࡸࠩມ"))
    bstack1l1lll11l1_opy_.write(bstack1ll1111lll_opy_)
    bstack1l1lll11l1_opy_.close()
    logger.info(bstack1lll111111_opy_)
    try:
      os.environ[bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪຢ")] = bstack1lllll1l11_opy_.framework if bstack1lllll1l11_opy_.framework != None else bstack1l1lll1_opy_ (u"ࠤࠥຣ")
      config = yaml.safe_load(bstack1ll1111lll_opy_)
      config[bstack1l1lll1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ຤")] = bstack1l1lll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠱ࡸ࡫ࡴࡶࡲࠪລ")
      bstack11ll1llll_opy_(bstack11lll11l1l_opy_, config)
    except Exception as e:
      logger.debug(bstack1l1111l1l1_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack11l1l11l1_opy_.format(str(e)))
def bstack11ll1llll_opy_(bstack11l111ll1_opy_, config, bstack1ll1l11ll_opy_={}):
  global bstack11lll11111_opy_
  global bstack111ll1l111_opy_
  global bstack1111111l_opy_
  if not config:
    return
  bstack111l1l111l_opy_ = bstack111ll11ll1_opy_ if not bstack11lll11111_opy_ else (
    bstack1l1l1l111l_opy_ if bstack1l1lll1_opy_ (u"ࠬࡧࡰࡱࠩ຦") in config else (
        bstack1ll11ll11_opy_ if config.get(bstack1l1lll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪວ")) else bstack1l111lll1_opy_
    )
)
  bstack11l111lll_opy_ = False
  bstack11111l1l11_opy_ = False
  if bstack11lll11111_opy_ is True:
      if bstack1l1lll1_opy_ (u"ࠧࡢࡲࡳࠫຨ") in config:
          bstack11l111lll_opy_ = True
      else:
          bstack11111l1l11_opy_ = True
  bstack1ll11ll11l_opy_ = bstack1l1l1l1111_opy_.bstack1l1ll1l1l1_opy_(config, bstack111ll1l111_opy_)
  bstack11lllll1ll_opy_ = bstack1l1ll1l1l_opy_()
  data = {
    bstack1l1lll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪຩ"): config[bstack1l1lll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫສ")],
    bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ຫ"): config[bstack1l1lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧຬ")],
    bstack1l1lll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠩອ"): bstack11l111ll1_opy_,
    bstack1l1lll1_opy_ (u"࠭ࡤࡦࡶࡨࡧࡹ࡫ࡤࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪຮ"): os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩຯ"), bstack111ll1l111_opy_),
    bstack1l1lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪະ"): bstack11ll1lllll_opy_,
    bstack1l1lll1_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯ࠫັ"): bstack1l1l1ll11l_opy_(),
    bstack1l1lll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭າ"): {
      bstack1l1lll1_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩຳ"): str(config[bstack1l1lll1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬິ")]) if bstack1l1lll1_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ີ") in config else bstack1l1lll1_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࠣຶ"),
      bstack1l1lll1_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧ࡙ࡩࡷࡹࡩࡰࡰࠪື"): sys.version,
      bstack1l1lll1_opy_ (u"ࠩࡵࡩ࡫࡫ࡲࡳࡧࡵຸࠫ"): bstack11l1lll11l_opy_(os.environ.get(bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏູࠬ"), bstack111ll1l111_opy_)),
      bstack1l1lll1_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ຺࠭"): bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬົ"),
      bstack1l1lll1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧຼ"): bstack111l1l111l_opy_,
      bstack1l1lll1_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬຽ"): bstack1ll11ll11l_opy_,
      bstack1l1lll1_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡡࡸࡹ࡮ࡪࠧ຾"): os.environ[bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ຿")],
      bstack1l1lll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ເ"): os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ແ"), bstack111ll1l111_opy_),
      bstack1l1lll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨໂ"): bstack1ll1llllll_opy_(os.environ.get(bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨໃ"), bstack111ll1l111_opy_)),
      bstack1l1lll1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ໄ"): bstack11lllll1ll_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭໅")),
      bstack1l1lll1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨໆ"): bstack11lllll1ll_opy_.get(bstack1l1lll1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫ໇")),
      bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫່ࠧ"): config[bstack1l1lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ້")] if config[bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦ໊ࠩ")] else bstack1l1lll1_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮໋ࠣ"),
      bstack1l1lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໌"): str(config[bstack1l1lll1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫໍ")]) if bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ໎") in config else bstack1l1lll1_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧ໏"),
      bstack1l1lll1_opy_ (u"ࠬࡵࡳࠨ໐"): sys.platform,
      bstack1l1lll1_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ໑"): socket.gethostname(),
      bstack1l1lll1_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ໒"): bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪ໓"))
    }
  }
  if not bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩ໔")) is None:
    data[bstack1l1lll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໕")][bstack1l1lll1_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡓࡥࡵࡣࡧࡥࡹࡧࠧ໖")] = {
      bstack1l1lll1_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ໗"): bstack1l1lll1_opy_ (u"࠭ࡵࡴࡧࡵࡣࡰ࡯࡬࡭ࡧࡧࠫ໘"),
      bstack1l1lll1_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࠧ໙"): bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ໚")),
      bstack1l1lll1_opy_ (u"ࠩࡶ࡭࡬ࡴࡡ࡭ࡐࡸࡱࡧ࡫ࡲࠨ໛"): bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡒࡴ࠭ໜ"))
    }
  if bstack11l111ll1_opy_ == bstack1llll11l1l_opy_:
    data[bstack1l1lll1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧໝ")][bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࠪໞ")] = bstack11l11l11l1_opy_(config)
    data[bstack1l1lll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩໟ")][bstack1l1lll1_opy_ (u"ࠧࡪࡵࡓࡩࡷࡩࡹࡂࡷࡷࡳࡊࡴࡡࡣ࡮ࡨࡨࠬ໠")] = percy.bstack1lll11l1ll_opy_
    data[bstack1l1lll1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໡")][bstack1l1lll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡃࡷ࡬ࡰࡩࡏࡤࠨ໢")] = percy.percy_build_id
  if not bstack1111llll_opy_.bstack11l1l1l1l_opy_(CONFIG):
    data[bstack1l1lll1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໣")][bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠨ໤")] = bstack1111llll_opy_.bstack11l1l1l1l_opy_(CONFIG)
  bstack111111ll_opy_ = bstack111l1lll_opy_.bstack11l11l1l_opy_(CONFIG, logger)
  bstack11l111l1_opy_ = bstack1111llll_opy_.bstack11l11l1l_opy_(config=CONFIG)
  if bstack111111ll_opy_ is not None and bstack11l111l1_opy_ is not None and bstack11l111l1_opy_.bstack1llll11l1_opy_():
    data[bstack1l1lll1_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ໥")][bstack11l111l1_opy_.bstack1ll1ll111l_opy_()] = bstack111111ll_opy_.bstack1ll1ll1l1l_opy_()
  update(data[bstack1l1lll1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ໦")], bstack1ll1l11ll_opy_)
  try:
    response = bstack1l1l1l1l1l_opy_(bstack1l1lll1_opy_ (u"ࠧࡑࡑࡖࡘࠬ໧"), bstack1l111l11l_opy_(bstack11ll1lll1l_opy_), data, {
      bstack1l1lll1_opy_ (u"ࠨࡣࡸࡸ࡭࠭໨"): (config[bstack1l1lll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ໩")], config[bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭໪")])
    })
    if response:
      logger.debug(bstack1l1l111111_opy_.format(bstack11l111ll1_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack111l1111l_opy_.format(str(e)))
def bstack11l1lll11l_opy_(framework):
  return bstack1l1lll1_opy_ (u"ࠦࢀࢃ࠭ࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴ࢁࡽࠣ໫").format(str(framework), __version__) if framework else bstack1l1lll1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨ໬").format(
    __version__)
def bstack11l11llll1_opy_():
  global CONFIG
  global bstack1111ll1ll_opy_
  if bool(CONFIG):
    return
  try:
    bstack11ll111l11_opy_()
    logger.debug(bstack1l1l11llll_opy_.format(str(CONFIG)))
    bstack1111ll1ll_opy_ = bstack111l11l1l_opy_.configure_logger(CONFIG, bstack1111ll1ll_opy_)
    bstack1111l11ll1_opy_()
  except Exception as e:
    logger.error(bstack1l1lll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࡻࡰ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࠥ໭") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11llll111l_opy_
  atexit.register(bstack1l11ll11l1_opy_)
  signal.signal(signal.SIGINT, bstack1l11ll1lll_opy_)
  signal.signal(signal.SIGTERM, bstack1l11ll1lll_opy_)
def bstack11llll111l_opy_(exctype, value, traceback):
  global bstack1l11l1111l_opy_
  try:
    for driver in bstack1l11l1111l_opy_:
      bstack111lll1111_opy_(driver, bstack1l1lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ໮"), bstack1l1lll1_opy_ (u"ࠣࡕࡨࡷࡸ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦ໯") + str(value))
  except Exception:
    pass
  logger.info(bstack1l1l111lll_opy_)
  bstack11lll1llll_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack11lll1llll_opy_(message=bstack1l1lll1_opy_ (u"ࠩࠪ໰"), bstack11l1111lll_opy_ = False):
  global CONFIG
  bstack11llll1ll1_opy_ = bstack1l1lll1_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮ࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠬ໱") if bstack11l1111lll_opy_ else bstack1l1lll1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ໲")
  try:
    if message:
      bstack1ll1l11ll_opy_ = {
        bstack11llll1ll1_opy_ : str(message)
      }
      bstack11ll1llll_opy_(bstack1llll11l1l_opy_, CONFIG, bstack1ll1l11ll_opy_)
    else:
      bstack11ll1llll_opy_(bstack1llll11l1l_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1l1lll1l1l_opy_.format(str(e)))
def bstack1l1111111_opy_(bstack11l1ll111_opy_, size):
  bstack1ll11llll1_opy_ = []
  while len(bstack11l1ll111_opy_) > size:
    bstack111l11l11l_opy_ = bstack11l1ll111_opy_[:size]
    bstack1ll11llll1_opy_.append(bstack111l11l11l_opy_)
    bstack11l1ll111_opy_ = bstack11l1ll111_opy_[size:]
  bstack1ll11llll1_opy_.append(bstack11l1ll111_opy_)
  return bstack1ll11llll1_opy_
def bstack11ll1ll1ll_opy_(args):
  if bstack1l1lll1_opy_ (u"ࠬ࠳࡭ࠨ໳") in args and bstack1l1lll1_opy_ (u"࠭ࡰࡥࡤࠪ໴") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack1l1lll1lll_opy_, stage=STAGE.bstack111ll111l_opy_)
def run_on_browserstack(bstack1ll11l1ll1_opy_=None, bstack11lll11ll1_opy_=None, bstack111l111l1l_opy_=False):
  global CONFIG
  global bstack1l111lllll_opy_
  global bstack1l1lllllll_opy_
  global bstack111ll1l111_opy_
  global bstack1111111l_opy_
  bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠧࠨ໵")
  bstack111ll1111_opy_(bstack1111lll1l_opy_, logger)
  if bstack1ll11l1ll1_opy_ and isinstance(bstack1ll11l1ll1_opy_, str):
    bstack1ll11l1ll1_opy_ = eval(bstack1ll11l1ll1_opy_)
  if bstack1ll11l1ll1_opy_:
    CONFIG = bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨ໶")]
    bstack1l111lllll_opy_ = bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪ໷")]
    bstack1l1lllllll_opy_ = bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ໸")]
    bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭໹"), bstack1l1lllllll_opy_)
    bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ໺")
  bstack1111111l_opy_.set_property(bstack1l1lll1_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ໻"), uuid4().__str__())
  logger.info(bstack1l1lll1_opy_ (u"ࠧࡔࡆࡎࠤࡷࡻ࡮ࠡࡵࡷࡥࡷࡺࡥࡥࠢࡺ࡭ࡹ࡮ࠠࡪࡦ࠽ࠤࠬ໼") + bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪ໽")));
  logger.debug(bstack1l1lll1_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࡁࠬ໾") + bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ໿")))
  if not bstack111l111l1l_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1l11lllll_opy_)
      return
    if sys.argv[1] == bstack1l1lll1_opy_ (u"ࠫ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧༀ") or sys.argv[1] == bstack1l1lll1_opy_ (u"ࠬ࠳ࡶࠨ༁"):
      logger.info(bstack1l1lll1_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡖࡹࡵࡪࡲࡲ࡙ࠥࡄࡌࠢࡹࡿࢂ࠭༂").format(__version__))
      return
    if sys.argv[1] == bstack1l1lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭༃"):
      bstack1111llllll_opy_()
      return
  args = sys.argv
  bstack11l11llll1_opy_()
  global bstack1ll11l1l1l_opy_
  global bstack11ll11l11l_opy_
  global bstack11lll1111l_opy_
  global bstack1l11ll11l_opy_
  global bstack1ll1l1l11l_opy_
  global bstack1111l11l1_opy_
  global bstack1111ll11ll_opy_
  global bstack11111l111_opy_
  global bstack11111ll11_opy_
  global bstack111l111l11_opy_
  global bstack1lll111lll_opy_
  bstack11ll11l11l_opy_ = len(CONFIG.get(bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ༄"), []))
  if not bstack11l11ll11_opy_:
    if args[1] == bstack1l1lll1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༅") or args[1] == bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫ༆"):
      bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༇")
      args = args[2:]
    elif args[1] == bstack1l1lll1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༈"):
      bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ༉")
      args = args[2:]
    elif args[1] == bstack1l1lll1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭༊"):
      bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ་")
      args = args[2:]
    elif args[1] == bstack1l1lll1_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ༌"):
      bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ།")
      args = args[2:]
    elif args[1] == bstack1l1lll1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༎"):
      bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ༏")
      args = args[2:]
    elif args[1] == bstack1l1lll1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭༐"):
      bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ༑")
      args = args[2:]
    else:
      if not bstack1l1lll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ༒") in CONFIG or str(CONFIG[bstack1l1lll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ༓")]).lower() in [bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༔"), bstack1l1lll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬ༕")]:
        bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ༖")
        args = args[1:]
      elif str(CONFIG[bstack1l1lll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༗")]).lower() == bstack1l1lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ༘࠭"):
        bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺ༙ࠧ")
        args = args[1:]
      elif str(CONFIG[bstack1l1lll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ༚")]).lower() == bstack1l1lll1_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ༛"):
        bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ༜")
        args = args[1:]
      elif str(CONFIG[bstack1l1lll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ༝")]).lower() == bstack1l1lll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭༞"):
        bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ༟")
        args = args[1:]
      elif str(CONFIG[bstack1l1lll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ༠")]).lower() == bstack1l1lll1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ༡"):
        bstack11l11ll11_opy_ = bstack1l1lll1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ༢")
        args = args[1:]
      else:
        os.environ[bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭༣")] = bstack11l11ll11_opy_
        bstack1l111ll1l1_opy_(bstack111llll1l1_opy_)
  os.environ[bstack1l1lll1_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭༤")] = bstack11l11ll11_opy_
  bstack111ll1l111_opy_ = bstack11l11ll11_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack11ll1l11l1_opy_ = bstack1111l1111_opy_[bstack1l1lll1_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙࠳ࡂࡅࡆࠪ༥")] if bstack11l11ll11_opy_ == bstack1l1lll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ༦") and bstack1l1l1lll1_opy_() else bstack11l11ll11_opy_
      bstack1llll111ll_opy_.invoke(Events.bstack11llllll1_opy_, bstack1l1l111l1l_opy_(
        sdk_version=__version__,
        path_config=bstack11l1llll1_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack11ll1l11l1_opy_,
        frameworks=[bstack11ll1l11l1_opy_],
        framework_versions={
          bstack11ll1l11l1_opy_: bstack1ll1llllll_opy_(bstack1l1lll1_opy_ (u"ࠨࡔࡲࡦࡴࡺࠧ༧") if bstack11l11ll11_opy_ in [bstack1l1lll1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༨"), bstack1l1lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ༩"), bstack1l1lll1_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ༪")] else bstack11l11ll11_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack1l1lll1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢ༫"), None):
        CONFIG[bstack1l1lll1_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ༬")] = cli.config.get(bstack1l1lll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤ༭"), None)
    except Exception as e:
      bstack1llll111ll_opy_.invoke(Events.bstack1l1l1ll1l1_opy_, e.__traceback__, 1)
    if bstack1l1lllllll_opy_:
      CONFIG[bstack1l1lll1_opy_ (u"ࠣࡣࡳࡴࠧ༮")] = cli.config[bstack1l1lll1_opy_ (u"ࠤࡤࡴࡵࠨ༯")]
      logger.info(bstack11ll1111ll_opy_.format(CONFIG[bstack1l1lll1_opy_ (u"ࠪࡥࡵࡶࠧ༰")]))
  else:
    bstack1llll111ll_opy_.clear()
  global bstack1111l1ll1l_opy_
  global bstack1l11llllll_opy_
  if bstack1ll11l1ll1_opy_:
    try:
      bstack11ll11ll1_opy_ = datetime.datetime.now()
      os.environ[bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭༱")] = bstack11l11ll11_opy_
      bstack11ll1llll_opy_(bstack11l1l111l_opy_, CONFIG)
      cli.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽ࡷࡩࡱ࡟ࡵࡧࡶࡸࡤࡧࡴࡵࡧࡰࡴࡹ࡫ࡤࠣ༲"), datetime.datetime.now() - bstack11ll11ll1_opy_)
    except Exception as e:
      logger.debug(bstack1111lll1ll_opy_.format(str(e)))
  global bstack1l111ll111_opy_
  global bstack11ll11lll1_opy_
  global bstack1llll11ll1_opy_
  global bstack1l1l11111l_opy_
  global bstack1l11lll1l_opy_
  global bstack1l11ll1ll_opy_
  global bstack1l1l11l1ll_opy_
  global bstack11ll111111_opy_
  global bstack11l11l111l_opy_
  global bstack11l1ll1111_opy_
  global bstack1l1ll1111_opy_
  global bstack1l111111ll_opy_
  global bstack11ll1ll1l1_opy_
  global bstack1ll11ll1l_opy_
  global bstack11llll11l_opy_
  global bstack11lllll1l1_opy_
  global bstack111l1llll1_opy_
  global bstack1l11111l11_opy_
  global bstack11l111l11l_opy_
  global bstack111l1ll1l_opy_
  global bstack11l111l1ll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l111ll111_opy_ = webdriver.Remote.__init__
    bstack11ll11lll1_opy_ = WebDriver.quit
    bstack1l111111ll_opy_ = WebDriver.close
    bstack11llll11l_opy_ = WebDriver.get
    bstack11l111l1ll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1111l1ll1l_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1111ll111l_opy_
    bstack1l11llllll_opy_ = bstack1111ll111l_opy_()
  except Exception as e:
    pass
  try:
    global bstack1ll11111ll_opy_
    from QWeb.keywords import browser
    bstack1ll11111ll_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1lll11lll1_opy_(CONFIG) and bstack111l1l11ll_opy_():
    if bstack1ll1ll11ll_opy_() < version.parse(bstack11ll1l1ll_opy_):
      logger.error(bstack1ll1l1l11_opy_.format(bstack1ll1ll11ll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1l1lll1_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ༳")) and callable(getattr(RemoteConnection, bstack1l1lll1_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ༴"))):
          RemoteConnection._get_proxy_url = bstack111l11lll_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack111l11lll_opy_
      except Exception as e:
        logger.error(bstack11111l11l1_opy_.format(str(e)))
  if not CONFIG.get(bstack1l1lll1_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵ༵ࠪ"), False) and not bstack1ll11l1ll1_opy_:
    logger.info(bstack1llllll1ll_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack1l1lll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭༶") in CONFIG and str(CONFIG[bstack1l1lll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫༷ࠧ")]).lower() != bstack1l1lll1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ༸"):
      bstack1l11111ll1_opy_()
    elif bstack11l11ll11_opy_ != bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ༹ࠬ") or (bstack11l11ll11_opy_ == bstack1l1lll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭༺") and not bstack1ll11l1ll1_opy_):
      bstack111lll111l_opy_()
  if (bstack11l11ll11_opy_ in [bstack1l1lll1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭༻"), bstack1l1lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ༼"), bstack1l1lll1_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ༽")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack111llllll1_opy_
        bstack1l11ll1ll_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack11111ll1ll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1l11lll1l_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack11l1ll1ll1_opy_ + str(e))
    except Exception as e:
      bstack1ll1ll1ll1_opy_(e, bstack11111ll1ll_opy_)
    if bstack11l11ll11_opy_ != bstack1l1lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ༾"):
      bstack1l1l1l111_opy_()
    bstack1llll11ll1_opy_ = Output.start_test
    bstack1l1l11111l_opy_ = Output.end_test
    bstack1l1l11l1ll_opy_ = TestStatus.__init__
    bstack11l11l111l_opy_ = pabot._run
    bstack11l1ll1111_opy_ = QueueItem.__init__
    bstack1l1ll1111_opy_ = pabot._create_command_for_execution
    bstack11l111l11l_opy_ = pabot._report_results
  if bstack11l11ll11_opy_ == bstack1l1lll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ༿"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll1ll1ll1_opy_(e, bstack1l1ll1lll1_opy_)
    bstack11ll1ll1l1_opy_ = Runner.run_hook
    bstack1ll11ll1l_opy_ = Step.run
  if bstack11l11ll11_opy_ == bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཀ"):
    try:
      from _pytest.config import Config
      bstack111l1llll1_opy_ = Config.getoption
      from _pytest import runner
      bstack1l11111l11_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack11l11l11_opy_)
    try:
      from pytest_bdd import reporting
      bstack111l1ll1l_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1l1lll1_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹࡵࠠࡳࡷࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࡹࠧཁ"))
  try:
    framework_name = bstack1l1lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ག") if bstack11l11ll11_opy_ in [bstack1l1lll1_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧགྷ"), bstack1l1lll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨང"), bstack1l1lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫཅ")] else bstack11ll1l1l1_opy_(bstack11l11ll11_opy_)
    bstack11llllll1l_opy_ = {
      bstack1l1lll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࠬཆ"): bstack1l1lll1_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧཇ") if bstack11l11ll11_opy_ == bstack1l1lll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭཈") and bstack1l1l1lll1_opy_() else framework_name,
      bstack1l1lll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫཉ"): bstack1ll1llllll_opy_(framework_name),
      bstack1l1lll1_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ཊ"): __version__,
      bstack1l1lll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪཋ"): bstack11l11ll11_opy_
    }
    if bstack11l11ll11_opy_ in bstack111l1l11l1_opy_ + bstack111lll1l1_opy_:
      if bstack1lll1ll1l_opy_.bstack11ll11ll1l_opy_(CONFIG):
        if bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪཌ") in CONFIG:
          os.environ[bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬཌྷ")] = os.getenv(bstack1l1lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ཎ"), json.dumps(CONFIG[bstack1l1lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ཏ")]))
          CONFIG[bstack1l1lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧཐ")].pop(bstack1l1lll1_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ད"), None)
          CONFIG[bstack1l1lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩདྷ")].pop(bstack1l1lll1_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨན"), None)
        bstack11llllll1l_opy_[bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫཔ")] = {
          bstack1l1lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪཕ"): bstack1l1lll1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨབ"),
          bstack1l1lll1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨབྷ"): str(bstack1ll1ll11ll_opy_())
        }
    if bstack11l11ll11_opy_ not in [bstack1l1lll1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩམ")] and not cli.is_running():
      bstack1l11lll1l1_opy_, bstack11ll11111l_opy_ = bstack1l11ll1l_opy_.launch(CONFIG, bstack11llllll1l_opy_)
      if bstack11ll11111l_opy_.get(bstack1l1lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩཙ")) is not None and bstack1lll1ll1l_opy_.bstack11ll1l1l1l_opy_(CONFIG) is None:
        value = bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪཚ")].get(bstack1l1lll1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬཛ"))
        if value is not None:
            CONFIG[bstack1l1lll1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬཛྷ")] = value
        else:
          logger.debug(bstack1l1lll1_opy_ (u"ࠨࡎࡰࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡧࡥࡹࡧࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠦཝ"))
  except Exception as e:
    logger.debug(bstack111l1l1lll_opy_.format(bstack1l1lll1_opy_ (u"ࠧࡕࡧࡶࡸࡍࡻࡢࠨཞ"), str(e)))
  if bstack11l11ll11_opy_ == bstack1l1lll1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨཟ"):
    bstack11lll1111l_opy_ = True
    if bstack1ll11l1ll1_opy_ and bstack111l111l1l_opy_:
      bstack1111l11l1_opy_ = CONFIG.get(bstack1l1lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭འ"), {}).get(bstack1l1lll1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬཡ"))
      bstack1l11ll1ll1_opy_(bstack1lll1111l_opy_)
    elif bstack1ll11l1ll1_opy_:
      bstack1111l11l1_opy_ = CONFIG.get(bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨར"), {}).get(bstack1l1lll1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧལ"))
      global bstack1l11l1111l_opy_
      try:
        if bstack11ll1ll1ll_opy_(bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩཤ")]) and multiprocessing.current_process().name == bstack1l1lll1_opy_ (u"ࠧ࠱ࠩཥ"):
          bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫས")].remove(bstack1l1lll1_opy_ (u"ࠩ࠰ࡱࠬཧ"))
          bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ཨ")].remove(bstack1l1lll1_opy_ (u"ࠫࡵࡪࡢࠨཀྵ"))
          bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཪ")] = bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩཫ")][0]
          with open(bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪཬ")], bstack1l1lll1_opy_ (u"ࠨࡴࠪ཭")) as f:
            file_content = f.read()
          bstack1l1l1l11l1_opy_ = bstack1l1lll1_opy_ (u"ࠤࠥࠦ࡫ࡸ࡯࡮ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡧ࡯ࠥ࡯࡭ࡱࡱࡵࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡥ࠼ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩ࠭ࢁࡽࠪ࠽ࠣࡪࡷࡵ࡭ࠡࡲࡧࡦࠥ࡯࡭ࡱࡱࡵࡸࠥࡖࡤࡣ࠽ࠣࡳ࡬ࡥࡤࡣࠢࡀࠤࡕࡪࡢ࠯ࡦࡲࡣࡧࡸࡥࡢ࡭࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥࡧࡩࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠨࡴࡧ࡯ࡪ࠱ࠦࡡࡳࡩ࠯ࠤࡹ࡫࡭ࡱࡱࡵࡥࡷࡿࠠ࠾ࠢ࠳࠭࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡹࡸࡹ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡤࡶ࡬ࠦ࠽ࠡࡵࡷࡶ࠭࡯࡮ࡵࠪࡤࡶ࡬࠯ࠫ࠲࠲ࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡨࡼࡨ࡫ࡰࡵࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡧࡳࠡࡧ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡵࡧࡳࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡰࡩࡢࡨࡧ࠮ࡳࡦ࡮ࡩ࠰ࡦࡸࡧ࠭ࡶࡨࡱࡵࡵࡲࡢࡴࡼ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࠣࡁࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡕࡪࡢ࠯ࡦࡲࡣࡧࡸࡥࡢ࡭ࠣࡁࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡕࡪࡢࠩࠫ࠱ࡷࡪࡺ࡟ࡵࡴࡤࡧࡪ࠮ࠩ࡝ࡰࠥࠦࠧ཮").format(str(bstack1ll11l1ll1_opy_))
          bstack1111111ll_opy_ = bstack1l1l1l11l1_opy_ + file_content
          bstack1l11lllll1_opy_ = bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭཯")] + bstack1l1lll1_opy_ (u"ࠫࡤࡨࡳࡵࡣࡦ࡯ࡤࡺࡥ࡮ࡲ࠱ࡴࡾ࠭཰")
          with open(bstack1l11lllll1_opy_, bstack1l1lll1_opy_ (u"ࠬࡽཱࠧ")):
            pass
          with open(bstack1l11lllll1_opy_, bstack1l1lll1_opy_ (u"ࠨࡷࠬࠤི")) as f:
            f.write(bstack1111111ll_opy_)
          import subprocess
          process_data = subprocess.run([bstack1l1lll1_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴཱིࠢ"), bstack1l11lllll1_opy_])
          if os.path.exists(bstack1l11lllll1_opy_):
            os.unlink(bstack1l11lllll1_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack11ll1ll1ll_opy_(bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨུࠫ")]):
            bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩཱུࠬ")].remove(bstack1l1lll1_opy_ (u"ࠪ࠱ࡲ࠭ྲྀ"))
            bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཷ")].remove(bstack1l1lll1_opy_ (u"ࠬࡶࡤࡣࠩླྀ"))
            bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩཹ")] = bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧེࠪ")][0]
          bstack1l11ll1ll1_opy_(bstack1lll1111l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨཻࠫ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1l1lll1_opy_ (u"ࠩࡢࡣࡳࡧ࡭ࡦࡡࡢོࠫ")] = bstack1l1lll1_opy_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣཽࠬ")
          mod_globals[bstack1l1lll1_opy_ (u"ࠫࡤࡥࡦࡪ࡮ࡨࡣࡤ࠭ཾ")] = os.path.abspath(bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཿ")])
          exec(open(bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦྀࠩ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1l1lll1_opy_ (u"ࠧࡄࡣࡸ࡫࡭ࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃཱྀࠧ").format(str(e)))
          for driver in bstack1l11l1111l_opy_:
            bstack11lll11ll1_opy_.append({
              bstack1l1lll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ྂ"): bstack1ll11l1ll1_opy_[bstack1l1lll1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྃ")],
              bstack1l1lll1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳ྄ࠩ"): str(e),
              bstack1l1lll1_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ྅"): multiprocessing.current_process().name
            })
            bstack111lll1111_opy_(driver, bstack1l1lll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ྆"), bstack1l1lll1_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤ྇") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l11l1111l_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1l1lllllll_opy_, CONFIG, logger)
      bstack1l11ll1l1l_opy_()
      bstack1l11ll111_opy_()
      percy.bstack1l1llll11l_opy_()
      bstack1llllll1l_opy_ = {
        bstack1l1lll1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྈ"): args[0],
        bstack1l1lll1_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨྉ"): CONFIG,
        bstack1l1lll1_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪྊ"): bstack1l111lllll_opy_,
        bstack1l1lll1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬྋ"): bstack1l1lllllll_opy_
      }
      if bstack1l1lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྌ") in CONFIG:
        bstack1ll111ll11_opy_ = bstack1ll1ll1l1_opy_(args, logger, CONFIG, bstack11lll11111_opy_, bstack11ll11l11l_opy_)
        bstack11111l111_opy_ = bstack1ll111ll11_opy_.bstack1lllll1l1_opy_(run_on_browserstack, bstack1llllll1l_opy_, bstack11ll1ll1ll_opy_(args))
      else:
        if bstack11ll1ll1ll_opy_(args):
          bstack1llllll1l_opy_[bstack1l1lll1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྍ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1llllll1l_opy_,))
          test.start()
          test.join()
        else:
          bstack1l11ll1ll1_opy_(bstack1lll1111l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1l1lll1_opy_ (u"࠭࡟ࡠࡰࡤࡱࡪࡥ࡟ࠨྎ")] = bstack1l1lll1_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩྏ")
          mod_globals[bstack1l1lll1_opy_ (u"ࠨࡡࡢࡪ࡮ࡲࡥࡠࡡࠪྐ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack11l11ll11_opy_ == bstack1l1lll1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨྑ") or bstack11l11ll11_opy_ == bstack1l1lll1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩྒ"):
    percy.init(bstack1l1lllllll_opy_, CONFIG, logger)
    percy.bstack1l1llll11l_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1ll1ll1ll1_opy_(e, bstack11111ll1ll_opy_)
    bstack1l11ll1l1l_opy_()
    bstack1l11ll1ll1_opy_(bstack1llll11l11_opy_)
    if bstack11lll11111_opy_:
      bstack11l1l111l1_opy_(bstack1llll11l11_opy_, args)
      if bstack1l1lll1_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩྒྷ") in args:
        i = args.index(bstack1l1lll1_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪྔ"))
        args.pop(i)
        args.pop(i)
      if bstack1l1lll1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩྕ") not in CONFIG:
        CONFIG[bstack1l1lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪྖ")] = [{}]
        bstack11ll11l11l_opy_ = 1
      if bstack1ll11l1l1l_opy_ == 0:
        bstack1ll11l1l1l_opy_ = 1
      args.insert(0, str(bstack1ll11l1l1l_opy_))
      args.insert(0, str(bstack1l1lll1_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ྗ")))
    if bstack1l11ll1l_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1lll11llll_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack111ll111ll_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1l1lll1_opy_ (u"ࠤࡕࡓࡇࡕࡔࡠࡑࡓࡘࡎࡕࡎࡔࠤ྘"),
        ).parse_args(bstack1lll11llll_opy_)
        bstack111l1lll1_opy_ = args.index(bstack1lll11llll_opy_[0]) if len(bstack1lll11llll_opy_) > 0 else len(args)
        args.insert(bstack111l1lll1_opy_, str(bstack1l1lll1_opy_ (u"ࠪ࠱࠲ࡲࡩࡴࡶࡨࡲࡪࡸࠧྙ")))
        args.insert(bstack111l1lll1_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1lll1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡷࡵࡢࡰࡶࡢࡰ࡮ࡹࡴࡦࡰࡨࡶ࠳ࡶࡹࠨྚ"))))
        if bstack1111llll_opy_.bstack1lll1l1ll_opy_(CONFIG):
          args.insert(bstack111l1lll1_opy_, str(bstack1l1lll1_opy_ (u"ࠬ࠳࠭࡭࡫ࡶࡸࡪࡴࡥࡳࠩྛ")))
          args.insert(bstack111l1lll1_opy_ + 1, str(bstack1l1lll1_opy_ (u"࠭ࡒࡦࡶࡵࡽࡋࡧࡩ࡭ࡧࡧ࠾ࢀࢃࠧྜ").format(bstack1111llll_opy_.bstack1lllll111_opy_(CONFIG))))
        if bstack111ll11ll_opy_(os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠬྜྷ"))) and str(os.environ.get(bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬྞ"), bstack1l1lll1_opy_ (u"ࠩࡱࡹࡱࡲࠧྟ"))) != bstack1l1lll1_opy_ (u"ࠪࡲࡺࡲ࡬ࠨྠ"):
          for bstack111l11111l_opy_ in bstack111ll111ll_opy_:
            args.remove(bstack111l11111l_opy_)
          test_files = os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠨྡ")).split(bstack1l1lll1_opy_ (u"ࠬ࠲ࠧྡྷ"))
          for bstack111l111111_opy_ in test_files:
            args.append(bstack111l111111_opy_)
      except Exception as e:
        logger.error(bstack1l1lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡦࡺࡴࡢࡥ࡫࡭ࡳ࡭ࠠ࡭࡫ࡶࡸࡪࡴࡥࡳࠢࡩࡳࡷࠦࡻࡾ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠰ࠤࢀࢃࠢྣ").format(bstack1lll1l1lll_opy_, e))
    pabot.main(args)
  elif bstack11l11ll11_opy_ == bstack1l1lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨྤ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1ll1ll1ll1_opy_(e, bstack11111ll1ll_opy_)
    for a in args:
      if bstack1l1lll1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞ࠧྥ") in a:
        bstack1ll1l1l11l_opy_ = int(a.split(bstack1l1lll1_opy_ (u"ࠩ࠽ࠫྦ"))[1])
      if bstack1l1lll1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧྦྷ") in a:
        bstack1111l11l1_opy_ = str(a.split(bstack1l1lll1_opy_ (u"ࠫ࠿࠭ྨ"))[1])
      if bstack1l1lll1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬྩ") in a:
        bstack1111ll11ll_opy_ = str(a.split(bstack1l1lll1_opy_ (u"࠭࠺ࠨྪ"))[1])
    bstack111111ll1_opy_ = None
    if bstack1l1lll1_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭ྫ") in args:
      i = args.index(bstack1l1lll1_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠧྫྷ"))
      args.pop(i)
      bstack111111ll1_opy_ = args.pop(i)
    if bstack111111ll1_opy_ is not None:
      global bstack1l1111l111_opy_
      bstack1l1111l111_opy_ = bstack111111ll1_opy_
    bstack1l11ll1ll1_opy_(bstack1llll11l11_opy_)
    run_cli(args)
    if bstack1l1lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭ྭ") in multiprocessing.current_process().__dict__.keys():
      for bstack1l11l1l1ll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11lll11ll1_opy_.append(bstack1l11l1l1ll_opy_)
  elif bstack11l11ll11_opy_ == bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪྮ"):
    bstack11l11111l_opy_ = bstack11l11ll1_opy_(args, logger, CONFIG, bstack11lll11111_opy_)
    bstack11l11111l_opy_.bstack111l11l1_opy_()
    bstack1l11ll1l1l_opy_()
    bstack1l11ll11l_opy_ = True
    bstack111l111l11_opy_ = bstack11l11111l_opy_.bstack1111ll11_opy_()
    bstack11l11111l_opy_.bstack1llllll1l_opy_(bstack1llll1l11l_opy_)
    bstack11l11111l_opy_.bstack1111l11l_opy_()
    bstack11l1lll1ll_opy_(bstack11l11ll11_opy_, CONFIG, bstack11l11111l_opy_.bstack1lll1llll_opy_())
    bstack11lll111l1_opy_ = bstack11l11111l_opy_.bstack1lllll1l1_opy_(bstack1ll111l11l_opy_, {
      bstack1l1lll1_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬྯ"): bstack1l111lllll_opy_,
      bstack1l1lll1_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧྰ"): bstack1l1lllllll_opy_,
      bstack1l1lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩྱ"): bstack11lll11111_opy_
    })
    try:
      bstack1lll1l1l11_opy_, bstack1ll11l1lll_opy_ = map(list, zip(*bstack11lll111l1_opy_))
      bstack11111ll11_opy_ = bstack1lll1l1l11_opy_[0]
      for status_code in bstack1ll11l1lll_opy_:
        if status_code != 0:
          bstack1lll111lll_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1l1lll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡦࡼࡥࠡࡧࡵࡶࡴࡸࡳࠡࡣࡱࡨࠥࡹࡴࡢࡶࡸࡷࠥࡩ࡯ࡥࡧ࠱ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠ࠻ࠢࡾࢁࠧྲ").format(str(e)))
  elif bstack11l11ll11_opy_ == bstack1l1lll1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨླ"):
    try:
      from behave.__main__ import main as bstack1ll11l1111_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1ll1ll1ll1_opy_(e, bstack1l1ll1lll1_opy_)
    bstack1l11ll1l1l_opy_()
    bstack1l11ll11l_opy_ = True
    bstack111l1l11_opy_ = 1
    if bstack1l1lll1_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩྴ") in CONFIG:
      bstack111l1l11_opy_ = CONFIG[bstack1l1lll1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪྵ")]
    if bstack1l1lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྶ") in CONFIG:
      bstack111ll11l1_opy_ = int(bstack111l1l11_opy_) * int(len(CONFIG[bstack1l1lll1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨྷ")]))
    else:
      bstack111ll11l1_opy_ = int(bstack111l1l11_opy_)
    config = Configuration(args)
    bstack1111l111ll_opy_ = config.paths
    if len(bstack1111l111ll_opy_) == 0:
      import glob
      pattern = bstack1l1lll1_opy_ (u"࠭ࠪࠫ࠱࠭࠲࡫࡫ࡡࡵࡷࡵࡩࠬྸ")
      bstack11l11l11l_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11l11l11l_opy_)
      config = Configuration(args)
      bstack1111l111ll_opy_ = config.paths
    bstack1111l1ll_opy_ = [os.path.normpath(item) for item in bstack1111l111ll_opy_]
    bstack11111lllll_opy_ = [os.path.normpath(item) for item in args]
    bstack11llll111_opy_ = [item for item in bstack11111lllll_opy_ if item not in bstack1111l1ll_opy_]
    import platform as pf
    if pf.system().lower() == bstack1l1lll1_opy_ (u"ࠧࡸ࡫ࡱࡨࡴࡽࡳࠨྐྵ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1111l1ll_opy_ = [str(PurePosixPath(PureWindowsPath(bstack111l11ll11_opy_)))
                    for bstack111l11ll11_opy_ in bstack1111l1ll_opy_]
    bstack11111111_opy_ = []
    for spec in bstack1111l1ll_opy_:
      bstack11l11111_opy_ = []
      bstack11l11111_opy_ += bstack11llll111_opy_
      bstack11l11111_opy_.append(spec)
      bstack11111111_opy_.append(bstack11l11111_opy_)
    execution_items = []
    for bstack11l11111_opy_ in bstack11111111_opy_:
      if bstack1l1lll1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫྺ") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack1l1lll1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྻ")]):
          item = {}
          item[bstack1l1lll1_opy_ (u"ࠪࡥࡷ࡭ࠧྼ")] = bstack1l1lll1_opy_ (u"ࠫࠥ࠭྽").join(bstack11l11111_opy_)
          item[bstack1l1lll1_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ྾")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack1l1lll1_opy_ (u"࠭ࡡࡳࡩࠪ྿")] = bstack1l1lll1_opy_ (u"ࠧࠡࠩ࿀").join(bstack11l11111_opy_)
        item[bstack1l1lll1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ࿁")] = 0
        execution_items.append(item)
    bstack111l11lll1_opy_ = bstack1l1111111_opy_(execution_items, bstack111ll11l1_opy_)
    for execution_item in bstack111l11lll1_opy_:
      bstack111111l1_opy_ = []
      for item in execution_item:
        bstack111111l1_opy_.append(bstack11lllll1l_opy_(name=str(item[bstack1l1lll1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ࿂")]),
                                             target=bstack1l1l1111ll_opy_,
                                             args=(item[bstack1l1lll1_opy_ (u"ࠪࡥࡷ࡭ࠧ࿃")],)))
      for t in bstack111111l1_opy_:
        t.start()
      for t in bstack111111l1_opy_:
        t.join()
  else:
    bstack1l111ll1l1_opy_(bstack111llll1l1_opy_)
  if not bstack1ll11l1ll1_opy_:
    bstack1111ll1l11_opy_()
    if(bstack11l11ll11_opy_ in [bstack1l1lll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ࿄"), bstack1l1lll1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ࿅")]):
      bstack1l1l1111l1_opy_()
  bstack111l11l1l_opy_.bstack1l1l11l111_opy_()
def browserstack_initialize(bstack1l1111lll_opy_=None):
  logger.info(bstack1l1lll1_opy_ (u"࠭ࡒࡶࡰࡱ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡼ࡯ࡴࡩࠢࡤࡶ࡬ࡹ࠺࿆ࠡࠩ") + str(bstack1l1111lll_opy_))
  run_on_browserstack(bstack1l1111lll_opy_, None, True)
@measure(event_name=EVENTS.bstack11llll11l1_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1111ll1l11_opy_():
  global CONFIG
  global bstack111ll1l111_opy_
  global bstack1lll111lll_opy_
  global bstack1l11lll1ll_opy_
  global bstack1111111l_opy_
  bstack11l1llll11_opy_.bstack11lllllll_opy_()
  if cli.is_running():
    bstack1llll111ll_opy_.invoke(Events.bstack1l111l1l11_opy_)
  else:
    bstack11l111l1_opy_ = bstack1111llll_opy_.bstack11l11l1l_opy_(config=CONFIG)
    bstack11l111l1_opy_.bstack111lll11l1_opy_(CONFIG)
  if bstack111ll1l111_opy_ == bstack1l1lll1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ࿇"):
    if not cli.is_enabled(CONFIG):
      bstack1l11ll1l_opy_.stop()
  else:
    bstack1l11ll1l_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1l11lll1_opy_.bstack1ll1l1l1ll_opy_()
  if bstack1l1lll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ࿈") in CONFIG and str(CONFIG[bstack1l1lll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭࿉")]).lower() != bstack1l1lll1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ࿊"):
    hashed_id, bstack11lll1l1l1_opy_ = bstack11l1l11l11_opy_()
  else:
    hashed_id, bstack11lll1l1l1_opy_ = get_build_link()
  bstack1l1l1ll1ll_opy_(hashed_id)
  logger.info(bstack1l1lll1_opy_ (u"ࠫࡘࡊࡋࠡࡴࡸࡲࠥ࡫࡮ࡥࡧࡧࠤ࡫ࡵࡲࠡ࡫ࡧ࠾ࠬ࿋") + bstack1111111l_opy_.get_property(bstack1l1lll1_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ࿌"), bstack1l1lll1_opy_ (u"࠭ࠧ࿍")) + bstack1l1lll1_opy_ (u"ࠧ࠭ࠢࡷࡩࡸࡺࡨࡶࡤࠣ࡭ࡩࡀࠠࠨ࿎") + os.getenv(bstack1l1lll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭࿏"), bstack1l1lll1_opy_ (u"ࠩࠪ࿐")))
  if hashed_id is not None and bstack1l1l1111l_opy_() != -1:
    sessions = bstack11l1111l1l_opy_(hashed_id)
    bstack1ll11l11ll_opy_(sessions, bstack11lll1l1l1_opy_)
  if bstack111ll1l111_opy_ == bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ࿑") and bstack1lll111lll_opy_ != 0:
    sys.exit(bstack1lll111lll_opy_)
  if bstack111ll1l111_opy_ == bstack1l1lll1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ࿒") and bstack1l11lll1ll_opy_ != 0:
    sys.exit(bstack1l11lll1ll_opy_)
def bstack1l1l1ll1ll_opy_(new_id):
    global bstack11ll1lllll_opy_
    bstack11ll1lllll_opy_ = new_id
def bstack11ll1l1l1_opy_(bstack1111l1l1l1_opy_):
  if bstack1111l1l1l1_opy_:
    return bstack1111l1l1l1_opy_.capitalize()
  else:
    return bstack1l1lll1_opy_ (u"ࠬ࠭࿓")
@measure(event_name=EVENTS.bstack1l1ll1ll11_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1l1l11l11l_opy_(bstack11l11ll111_opy_):
  if bstack1l1lll1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ࿔") in bstack11l11ll111_opy_ and bstack11l11ll111_opy_[bstack1l1lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ࿕")] != bstack1l1lll1_opy_ (u"ࠨࠩ࿖"):
    return bstack11l11ll111_opy_[bstack1l1lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ࿗")]
  else:
    bstack11l1l1l1ll_opy_ = bstack1l1lll1_opy_ (u"ࠥࠦ࿘")
    if bstack1l1lll1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ࿙") in bstack11l11ll111_opy_ and bstack11l11ll111_opy_[bstack1l1lll1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ࿚")] != None:
      bstack11l1l1l1ll_opy_ += bstack11l11ll111_opy_[bstack1l1lll1_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭࿛")] + bstack1l1lll1_opy_ (u"ࠢ࠭ࠢࠥ࿜")
      if bstack11l11ll111_opy_[bstack1l1lll1_opy_ (u"ࠨࡱࡶࠫ࿝")] == bstack1l1lll1_opy_ (u"ࠤ࡬ࡳࡸࠨ࿞"):
        bstack11l1l1l1ll_opy_ += bstack1l1lll1_opy_ (u"ࠥ࡭ࡔ࡙ࠠࠣ࿟")
      bstack11l1l1l1ll_opy_ += (bstack11l11ll111_opy_[bstack1l1lll1_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ࿠")] or bstack1l1lll1_opy_ (u"ࠬ࠭࿡"))
      return bstack11l1l1l1ll_opy_
    else:
      bstack11l1l1l1ll_opy_ += bstack11ll1l1l1_opy_(bstack11l11ll111_opy_[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧ࿢")]) + bstack1l1lll1_opy_ (u"ࠢࠡࠤ࿣") + (
              bstack11l11ll111_opy_[bstack1l1lll1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ࿤")] or bstack1l1lll1_opy_ (u"ࠩࠪ࿥")) + bstack1l1lll1_opy_ (u"ࠥ࠰ࠥࠨ࿦")
      if bstack11l11ll111_opy_[bstack1l1lll1_opy_ (u"ࠫࡴࡹࠧ࿧")] == bstack1l1lll1_opy_ (u"ࠧ࡝ࡩ࡯ࡦࡲࡻࡸࠨ࿨"):
        bstack11l1l1l1ll_opy_ += bstack1l1lll1_opy_ (u"ࠨࡗࡪࡰࠣࠦ࿩")
      bstack11l1l1l1ll_opy_ += bstack11l11ll111_opy_[bstack1l1lll1_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫ࿪")] or bstack1l1lll1_opy_ (u"ࠨࠩ࿫")
      return bstack11l1l1l1ll_opy_
@measure(event_name=EVENTS.bstack111llll1l_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1ll1l1111_opy_(bstack1l1l1l1l11_opy_):
  if bstack1l1l1l1l11_opy_ == bstack1l1lll1_opy_ (u"ࠤࡧࡳࡳ࡫ࠢ࿬"):
    return bstack1l1lll1_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿࡭ࡲࡦࡧࡱ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧ࡭ࡲࡦࡧࡱࠦࡃࡉ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭࿭")
  elif bstack1l1l1l1l11_opy_ == bstack1l1lll1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ࿮"):
    return bstack1l1lll1_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡳࡧࡧ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡸࡥࡥࠤࡁࡊࡦ࡯࡬ࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ࿯")
  elif bstack1l1l1l1l11_opy_ == bstack1l1lll1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ࿰"):
    return bstack1l1lll1_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡪࡶࡪ࡫࡮࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡪࡶࡪ࡫࡮ࠣࡀࡓࡥࡸࡹࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ࿱")
  elif bstack1l1l1l1l11_opy_ == bstack1l1lll1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢ࿲"):
    return bstack1l1lll1_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡷ࡫ࡤ࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡵࡩࡩࠨ࠾ࡆࡴࡵࡳࡷࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ࿳")
  elif bstack1l1l1l1l11_opy_ == bstack1l1lll1_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࠦ࿴"):
    return bstack1l1lll1_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࠣࡦࡧࡤ࠷࠷࠼࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࠥࡨࡩࡦ࠹࠲࠷ࠤࡁࡘ࡮ࡳࡥࡰࡷࡷࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ࿵")
  elif bstack1l1l1l1l11_opy_ == bstack1l1lll1_opy_ (u"ࠧࡸࡵ࡯ࡰ࡬ࡲ࡬ࠨ࿶"):
    return bstack1l1lll1_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡤ࡯ࡥࡨࡱ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡤ࡯ࡥࡨࡱࠢ࠿ࡔࡸࡲࡳ࡯࡮ࡨ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ࿷")
  else:
    return bstack1l1lll1_opy_ (u"ࠧ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡦࡱࡧࡣ࡬࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡦࡱࡧࡣ࡬ࠤࡁࠫ࿸") + bstack11ll1l1l1_opy_(
      bstack1l1l1l1l11_opy_) + bstack1l1lll1_opy_ (u"ࠨ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ࿹")
def bstack11l11lll11_opy_(session):
  return bstack1l1lll1_opy_ (u"ࠩ࠿ࡸࡷࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡲࡰࡹࠥࡂࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠦࡳࡦࡵࡶ࡭ࡴࡴ࠭࡯ࡣࡰࡩࠧࡄ࠼ࡢࠢ࡫ࡶࡪ࡬࠽ࠣࡽࢀࠦࠥࡺࡡࡳࡩࡨࡸࡂࠨ࡟ࡣ࡮ࡤࡲࡰࠨ࠾ࡼࡿ࠿࠳ࡦࡄ࠼࠰ࡶࡧࡂࢀࢃࡻࡾ࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀ࠴ࡺࡲ࠿ࠩ࿺").format(
    session[bstack1l1lll1_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧ࿻")], bstack1l1l11l11l_opy_(session), bstack1ll1l1111_opy_(session[bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡷࡹࡧࡴࡶࡵࠪ࿼")]),
    bstack1ll1l1111_opy_(session[bstack1l1lll1_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ࿽")]),
    bstack11ll1l1l1_opy_(session[bstack1l1lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧ࿾")] or session[bstack1l1lll1_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ࿿")] or bstack1l1lll1_opy_ (u"ࠨࠩက")) + bstack1l1lll1_opy_ (u"ࠤࠣࠦခ") + (session[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬဂ")] or bstack1l1lll1_opy_ (u"ࠫࠬဃ")),
    session[bstack1l1lll1_opy_ (u"ࠬࡵࡳࠨင")] + bstack1l1lll1_opy_ (u"ࠨࠠࠣစ") + session[bstack1l1lll1_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫဆ")], session[bstack1l1lll1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪဇ")] or bstack1l1lll1_opy_ (u"ࠩࠪဈ"),
    session[bstack1l1lll1_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧဉ")] if session[bstack1l1lll1_opy_ (u"ࠫࡨࡸࡥࡢࡶࡨࡨࡤࡧࡴࠨည")] else bstack1l1lll1_opy_ (u"ࠬ࠭ဋ"))
@measure(event_name=EVENTS.bstack1ll1111ll1_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def bstack1ll11l11ll_opy_(sessions, bstack11lll1l1l1_opy_):
  try:
    bstack1l1l111ll1_opy_ = bstack1l1lll1_opy_ (u"ࠨࠢဌ")
    if not os.path.exists(bstack11ll11l1l_opy_):
      os.mkdir(bstack11ll11l1l_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1lll1_opy_ (u"ࠧࡢࡵࡶࡩࡹࡹ࠯ࡳࡧࡳࡳࡷࡺ࠮ࡩࡶࡰࡰࠬဍ")), bstack1l1lll1_opy_ (u"ࠨࡴࠪဎ")) as f:
      bstack1l1l111ll1_opy_ = f.read()
    bstack1l1l111ll1_opy_ = bstack1l1l111ll1_opy_.replace(bstack1l1lll1_opy_ (u"ࠩࡾࠩࡗࡋࡓࡖࡎࡗࡗࡤࡉࡏࡖࡐࡗࠩࢂ࠭ဏ"), str(len(sessions)))
    bstack1l1l111ll1_opy_ = bstack1l1l111ll1_opy_.replace(bstack1l1lll1_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠦࡿࠪတ"), bstack11lll1l1l1_opy_)
    bstack1l1l111ll1_opy_ = bstack1l1l111ll1_opy_.replace(bstack1l1lll1_opy_ (u"ࠫࢀࠫࡂࡖࡋࡏࡈࡤࡔࡁࡎࡇࠨࢁࠬထ"),
                                              sessions[0].get(bstack1l1lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣࡳࡧ࡭ࡦࠩဒ")) if sessions[0] else bstack1l1lll1_opy_ (u"࠭ࠧဓ"))
    with open(os.path.join(bstack11ll11l1l_opy_, bstack1l1lll1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ࠫန")), bstack1l1lll1_opy_ (u"ࠨࡹࠪပ")) as stream:
      stream.write(bstack1l1l111ll1_opy_.split(bstack1l1lll1_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂ࠭ဖ"))[0])
      for session in sessions:
        stream.write(bstack11l11lll11_opy_(session))
      stream.write(bstack1l1l111ll1_opy_.split(bstack1l1lll1_opy_ (u"ࠪࡿ࡙ࠪࡅࡔࡕࡌࡓࡓ࡙࡟ࡅࡃࡗࡅࠪࢃࠧဗ"))[1])
    logger.info(bstack1l1lll1_opy_ (u"ࠫࡌ࡫࡮ࡦࡴࡤࡸࡪࡪࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡢࡶ࡫࡯ࡨࠥࡧࡲࡵ࡫ࡩࡥࡨࡺࡳࠡࡣࡷࠤࢀࢃࠧဘ").format(bstack11ll11l1l_opy_));
  except Exception as e:
    logger.debug(bstack11l11111ll_opy_.format(str(e)))
def bstack11l1111l1l_opy_(hashed_id):
  global CONFIG
  try:
    bstack11ll11ll1_opy_ = datetime.datetime.now()
    host = bstack1l1lll1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬမ") if bstack1l1lll1_opy_ (u"࠭ࡡࡱࡲࠪယ") in CONFIG else bstack1l1lll1_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨရ")
    user = CONFIG[bstack1l1lll1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪလ")]
    key = CONFIG[bstack1l1lll1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬဝ")]
    bstack111ll1111l_opy_ = bstack1l1lll1_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩသ") if bstack1l1lll1_opy_ (u"ࠫࡦࡶࡰࠨဟ") in CONFIG else (bstack1l1lll1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩဠ") if CONFIG.get(bstack1l1lll1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪအ")) else bstack1l1lll1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩဢ"))
    host = bstack11l11ll11l_opy_(cli.config, [bstack1l1lll1_opy_ (u"ࠣࡣࡳ࡭ࡸࠨဣ"), bstack1l1lll1_opy_ (u"ࠤࡤࡴࡵࡇࡵࡵࡱࡰࡥࡹ࡫ࠢဤ"), bstack1l1lll1_opy_ (u"ࠥࡥࡵ࡯ࠢဥ")], host) if bstack1l1lll1_opy_ (u"ࠫࡦࡶࡰࠨဦ") in CONFIG else bstack11l11ll11l_opy_(cli.config, [bstack1l1lll1_opy_ (u"ࠧࡧࡰࡪࡵࠥဧ"), bstack1l1lll1_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥࠣဨ"), bstack1l1lll1_opy_ (u"ࠢࡢࡲ࡬ࠦဩ")], host)
    url = bstack1l1lll1_opy_ (u"ࠨࡽࢀ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠳ࡰࡳࡰࡰࠪဪ").format(host, bstack111ll1111l_opy_, hashed_id)
    headers = {
      bstack1l1lll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨါ"): bstack1l1lll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ာ"),
    }
    proxies = bstack11l1l11ll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡪࡩࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࡠ࡮࡬ࡷࡹࠨိ"), datetime.datetime.now() - bstack11ll11ll1_opy_)
      return list(map(lambda session: session[bstack1l1lll1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠪီ")], response.json()))
  except Exception as e:
    logger.debug(bstack1l1lll1ll1_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack111llll11l_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def get_build_link():
  global CONFIG
  global bstack11ll1lllll_opy_
  try:
    if bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩု") in CONFIG:
      bstack11ll11ll1_opy_ = datetime.datetime.now()
      host = bstack1l1lll1_opy_ (u"ࠧࡢࡲ࡬࠱ࡨࡲ࡯ࡶࡦࠪူ") if bstack1l1lll1_opy_ (u"ࠨࡣࡳࡴࠬေ") in CONFIG else bstack1l1lll1_opy_ (u"ࠩࡤࡴ࡮࠭ဲ")
      user = CONFIG[bstack1l1lll1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬဳ")]
      key = CONFIG[bstack1l1lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧဴ")]
      bstack111ll1111l_opy_ = bstack1l1lll1_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫဵ") if bstack1l1lll1_opy_ (u"࠭ࡡࡱࡲࠪံ") in CONFIG else bstack1l1lll1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦ့ࠩ")
      url = bstack1l1lll1_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡾࢁ࠿ࢁࡽࡁࡽࢀ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠱࡮ࡸࡵ࡮ࠨး").format(user, key, host, bstack111ll1111l_opy_)
      if cli.is_enabled(CONFIG):
        bstack11lll1l1l1_opy_, hashed_id = cli.bstack1l1lll1l1_opy_()
        logger.info(bstack1l1llll111_opy_.format(bstack11lll1l1l1_opy_))
        return [hashed_id, bstack11lll1l1l1_opy_]
      else:
        headers = {
          bstack1l1lll1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨ္"): bstack1l1lll1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ်࠭"),
        }
        if bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ျ") in CONFIG:
          params = {bstack1l1lll1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪြ"): CONFIG[bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩွ")], bstack1l1lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪှ"): CONFIG[bstack1l1lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪဿ")]}
        else:
          params = {bstack1l1lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ၀"): CONFIG[bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭၁")]}
        proxies = bstack11l1l11ll_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack11l111l1l_opy_ = response.json()[0][bstack1l1lll1_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡤࡸ࡭ࡱࡪࠧ၂")]
          if bstack11l111l1l_opy_:
            bstack11lll1l1l1_opy_ = bstack11l111l1l_opy_[bstack1l1lll1_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧࡤࡻࡲ࡭ࠩ၃")].split(bstack1l1lll1_opy_ (u"࠭ࡰࡶࡤ࡯࡭ࡨ࠳ࡢࡶ࡫࡯ࡨࠬ၄"))[0] + bstack1l1lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡹ࠯ࠨ၅") + bstack11l111l1l_opy_[
              bstack1l1lll1_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ၆")]
            logger.info(bstack1l1llll111_opy_.format(bstack11lll1l1l1_opy_))
            bstack11ll1lllll_opy_ = bstack11l111l1l_opy_[bstack1l1lll1_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ၇")]
            bstack11ll1l1lll_opy_ = CONFIG[bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭၈")]
            if bstack1l1lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭၉") in CONFIG:
              bstack11ll1l1lll_opy_ += bstack1l1lll1_opy_ (u"ࠬࠦࠧ၊") + CONFIG[bstack1l1lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ။")]
            if bstack11ll1l1lll_opy_ != bstack11l111l1l_opy_[bstack1l1lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ၌")]:
              logger.debug(bstack11lll1ll1_opy_.format(bstack11l111l1l_opy_[bstack1l1lll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭၍")], bstack11ll1l1lll_opy_))
            cli.bstack1111l11111_opy_(bstack1l1lll1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡨࡧࡷࡣࡧࡻࡩ࡭ࡦࡢࡰ࡮ࡴ࡫ࠣ၎"), datetime.datetime.now() - bstack11ll11ll1_opy_)
            return [bstack11l111l1l_opy_[bstack1l1lll1_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭၏")], bstack11lll1l1l1_opy_]
    else:
      logger.warn(bstack1l1l1l1ll1_opy_)
  except Exception as e:
    logger.debug(bstack11l11l1ll1_opy_.format(str(e)))
  return [None, None]
def bstack11l1lll1l1_opy_(url, bstack1ll1llll1_opy_=False):
  global CONFIG
  global bstack1lll1llll1_opy_
  if not bstack1lll1llll1_opy_:
    hostname = bstack1l111111l_opy_(url)
    is_private = bstack1l1lll1l11_opy_(hostname)
    if (bstack1l1lll1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨၐ") in CONFIG and not bstack111ll11ll_opy_(CONFIG[bstack1l1lll1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩၑ")])) and (is_private or bstack1ll1llll1_opy_):
      bstack1lll1llll1_opy_ = hostname
def bstack1l111111l_opy_(url):
  return urlparse(url).hostname
def bstack1l1lll1l11_opy_(hostname):
  for bstack11ll11l1ll_opy_ in bstack1lll1111ll_opy_:
    regex = re.compile(bstack11ll11l1ll_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1lll11ll1l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1ll1lll111_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1ll1l1l11l_opy_
  bstack1l1l1l1ll_opy_ = not (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪၒ"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1l1lll1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ၓ"), None))
  bstack1llllllll1_opy_ = getattr(driver, bstack1l1lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨၔ"), None) != True
  bstack1lll11111l_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၕ"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1l1lll1_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၖ"), None)
  if bstack1lll11111l_opy_:
    if not bstack11l11llll_opy_():
      logger.warning(bstack1l1lll1_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹ࠮ࠣၗ"))
      return {}
    logger.debug(bstack1l1lll1_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩၘ"))
    logger.debug(perform_scan(driver, driver_command=bstack1l1lll1_opy_ (u"࠭ࡥࡹࡧࡦࡹࡹ࡫ࡓࡤࡴ࡬ࡴࡹ࠭ၙ")))
    results = bstack1lll1111l1_opy_(bstack1l1lll1_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡳࠣၚ"))
    if results is not None and results.get(bstack1l1lll1_opy_ (u"ࠣ࡫ࡶࡷࡺ࡫ࡳࠣၛ")) is not None:
        return results[bstack1l1lll1_opy_ (u"ࠤ࡬ࡷࡸࡻࡥࡴࠤၜ")]
    logger.error(bstack1l1lll1_opy_ (u"ࠥࡒࡴࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡒࡦࡵࡸࡰࡹࡹࠠࡸࡧࡵࡩࠥ࡬࡯ࡶࡰࡧ࠲ࠧၝ"))
    return []
  if not bstack1lll1ll1l_opy_.bstack11lll1lll_opy_(CONFIG, bstack1ll1l1l11l_opy_) or (bstack1llllllll1_opy_ and bstack1l1l1l1ll_opy_):
    logger.warning(bstack1l1lll1_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸ࠴ࠢၞ"))
    return {}
  try:
    logger.debug(bstack1l1lll1_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩၟ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1l11111ll_opy_.bstack1ll1lll11l_opy_)
    return results
  except Exception:
    logger.error(bstack1l1lll1_opy_ (u"ࠨࡎࡰࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡻࡪࡸࡥࠡࡨࡲࡹࡳࡪ࠮ࠣၠ"))
    return {}
@measure(event_name=EVENTS.bstack1ll1lllll1_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1ll1l1l11l_opy_
  bstack1l1l1l1ll_opy_ = not (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫၡ"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1l1lll1_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧၢ"), None))
  bstack1llllllll1_opy_ = getattr(driver, bstack1l1lll1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩၣ"), None) != True
  bstack1lll11111l_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪၤ"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1l1lll1_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ၥ"), None)
  if bstack1lll11111l_opy_:
    if not bstack11l11llll_opy_():
      logger.warning(bstack1l1lll1_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺ࠰ࠥၦ"))
      return {}
    logger.debug(bstack1l1lll1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼࠫၧ"))
    logger.debug(perform_scan(driver, driver_command=bstack1l1lll1_opy_ (u"ࠧࡦࡺࡨࡧࡺࡺࡥࡔࡥࡵ࡭ࡵࡺࠧၨ")))
    results = bstack1lll1111l1_opy_(bstack1l1lll1_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡔࡷࡰࡱࡦࡸࡹࠣၩ"))
    if results is not None and results.get(bstack1l1lll1_opy_ (u"ࠤࡶࡹࡲࡳࡡࡳࡻࠥၪ")) is not None:
        return results[bstack1l1lll1_opy_ (u"ࠥࡷࡺࡳ࡭ࡢࡴࡼࠦၫ")]
    logger.error(bstack1l1lll1_opy_ (u"ࠦࡓࡵࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡓࡧࡶࡹࡱࡺࡳࠡࡕࡸࡱࡲࡧࡲࡺࠢࡺࡥࡸࠦࡦࡰࡷࡱࡨ࠳ࠨၬ"))
    return {}
  if not bstack1lll1ll1l_opy_.bstack11lll1lll_opy_(CONFIG, bstack1ll1l1l11l_opy_) or (bstack1llllllll1_opy_ and bstack1l1l1l1ll_opy_):
    logger.warning(bstack1l1lll1_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹ࠯ࠤၭ"))
    return {}
  try:
    logger.debug(bstack1l1lll1_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼࠫၮ"))
    logger.debug(perform_scan(driver))
    bstack11l11l1l11_opy_ = driver.execute_async_script(bstack1l11111ll_opy_.bstack1ll111111_opy_)
    return bstack11l11l1l11_opy_
  except Exception:
    logger.error(bstack1l1lll1_opy_ (u"ࠢࡏࡱࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡺࡳ࡭ࡢࡴࡼࠤࡼࡧࡳࠡࡨࡲࡹࡳࡪ࠮ࠣၯ"))
    return {}
def bstack11l11llll_opy_():
  global CONFIG
  global bstack1ll1l1l11l_opy_
  bstack1l11l11l11_opy_ = bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၰ"), None) and bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၱ"), None)
  if not bstack1lll1ll1l_opy_.bstack11lll1lll_opy_(CONFIG, bstack1ll1l1l11l_opy_) or not bstack1l11l11l11_opy_:
        logger.warning(bstack1l1lll1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡴࡨࡷࡺࡲࡴࡴ࠰ࠥၲ"))
        return False
  return True
def bstack1lll1111l1_opy_(bstack1l11l11lll_opy_):
    bstack11ll1111l1_opy_ = bstack1l11ll1l_opy_.current_test_uuid() if bstack1l11ll1l_opy_.current_test_uuid() else bstack1l11lll1_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack1l11ll1111_opy_(bstack11ll1111l1_opy_, bstack1l11l11lll_opy_))
        try:
            return future.result(timeout=bstack1111l111l1_opy_)
        except TimeoutError:
            logger.error(bstack1l1lll1_opy_ (u"࡙ࠦ࡯࡭ࡦࡱࡸࡸࠥࡧࡦࡵࡧࡵࠤࢀࢃࡳࠡࡹ࡫࡭ࡱ࡫ࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡕࡩࡸࡻ࡬ࡵࡵࠥၳ").format(bstack1111l111l1_opy_))
        except Exception as ex:
            logger.debug(bstack1l1lll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡷ࡫ࡴࡳ࡫ࡨࡺ࡮ࡴࡧࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡾࢁ࠳ࠦࡅࡳࡴࡲࡶࠥ࠳ࠠࡼࡿࠥၴ").format(bstack1l11l11lll_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack1l11l1111_opy_, stage=STAGE.bstack1111llll1l_opy_, bstack11l1l1l1ll_opy_=bstack1lll111l11_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1ll1l1l11l_opy_
  bstack1l1l1l1ll_opy_ = not (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪၵ"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1l1lll1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ၶ"), None))
  bstack11l1lllll1_opy_ = not (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၷ"), None) and bstack1l1l1l1l_opy_(
          threading.current_thread(), bstack1l1lll1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၸ"), None))
  bstack1llllllll1_opy_ = getattr(driver, bstack1l1lll1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪၹ"), None) != True
  if not bstack1lll1ll1l_opy_.bstack11lll1lll_opy_(CONFIG, bstack1ll1l1l11l_opy_) or (bstack1llllllll1_opy_ and bstack1l1l1l1ll_opy_ and bstack11l1lllll1_opy_):
    logger.warning(bstack1l1lll1_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡺࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲ࠳ࠨၺ"))
    return {}
  try:
    bstack1111lll111_opy_ = bstack1l1lll1_opy_ (u"ࠬࡧࡰࡱࠩၻ") in CONFIG and CONFIG.get(bstack1l1lll1_opy_ (u"࠭ࡡࡱࡲࠪၼ"), bstack1l1lll1_opy_ (u"ࠧࠨၽ"))
    session_id = getattr(driver, bstack1l1lll1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠬၾ"), None)
    if not session_id:
      logger.warning(bstack1l1lll1_opy_ (u"ࠤࡑࡳࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥࡪࡲࡪࡸࡨࡶࠧၿ"))
      return {bstack1l1lll1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤႀ"): bstack1l1lll1_opy_ (u"ࠦࡓࡵࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡋࡇࠤ࡫ࡵࡵ࡯ࡦࠥႁ")}
    if bstack1111lll111_opy_:
      try:
        bstack1l11ll11ll_opy_ = {
              bstack1l1lll1_opy_ (u"ࠬࡺࡨࡋࡹࡷࡘࡴࡱࡥ࡯ࠩႂ"): os.environ.get(bstack1l1lll1_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫႃ"), os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫႄ"), bstack1l1lll1_opy_ (u"ࠨࠩႅ"))),
              bstack1l1lll1_opy_ (u"ࠩࡷ࡬࡙࡫ࡳࡵࡔࡸࡲ࡚ࡻࡩࡥࠩႆ"): bstack1l11ll1l_opy_.current_test_uuid() if bstack1l11ll1l_opy_.current_test_uuid() else bstack1l11lll1_opy_.current_hook_uuid(),
              bstack1l1lll1_opy_ (u"ࠪࡥࡺࡺࡨࡉࡧࡤࡨࡪࡸࠧႇ"): os.environ.get(bstack1l1lll1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩႈ")),
              bstack1l1lll1_opy_ (u"ࠬࡹࡣࡢࡰࡗ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬႉ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack1l1lll1_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫႊ"): os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬႋ"), bstack1l1lll1_opy_ (u"ࠨࠩႌ")),
              bstack1l1lll1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥႍࠩ"): kwargs.get(bstack1l1lll1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢࡧࡴࡳ࡭ࡢࡰࡧࠫႎ"), None) or bstack1l1lll1_opy_ (u"ࠫࠬႏ")
          }
        if not hasattr(thread_local, bstack1l1lll1_opy_ (u"ࠬࡨࡡࡴࡧࡢࡥࡵࡶ࡟ࡢ࠳࠴ࡽࡤࡹࡣࡳ࡫ࡳࡸࠬ႐")):
            scripts = {bstack1l1lll1_opy_ (u"࠭ࡳࡤࡣࡱࠫ႑"): bstack1l11111ll_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack1lll1ll1ll_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack1lll1ll1ll_opy_[bstack1l1lll1_opy_ (u"ࠧࡴࡥࡤࡲࠬ႒")] = bstack1lll1ll1ll_opy_[bstack1l1lll1_opy_ (u"ࠨࡵࡦࡥࡳ࠭႓")] % json.dumps(bstack1l11ll11ll_opy_)
        bstack1l11111ll_opy_.bstack11l11l1ll_opy_(bstack1lll1ll1ll_opy_)
        bstack1l11111ll_opy_.store()
        bstack111l1ll11l_opy_ = driver.execute_script(bstack1l11111ll_opy_.perform_scan)
      except Exception as bstack11l11l1l1_opy_:
        logger.info(bstack1l1lll1_opy_ (u"ࠤࡄࡴࡵ࡯ࡵ࡮ࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡧࡦࡴࠠࡧࡣ࡬ࡰࡪࡪ࠺ࠡࠤ႔") + str(bstack11l11l1l1_opy_))
        bstack111l1ll11l_opy_ = {bstack1l1lll1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ႕"): str(bstack11l11l1l1_opy_)}
    else:
      bstack111l1ll11l_opy_ = driver.execute_async_script(bstack1l11111ll_opy_.perform_scan, {bstack1l1lll1_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࠫ႖"): kwargs.get(bstack1l1lll1_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤࡩ࡯࡮࡯ࡤࡲࡩ࠭႗"), None) or bstack1l1lll1_opy_ (u"࠭ࠧ႘")})
    return bstack111l1ll11l_opy_
  except Exception as err:
    logger.error(bstack1l1lll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡶࡺࡴࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲ࠳ࠦࡻࡾࠤ႙").format(str(err)))
    return {}