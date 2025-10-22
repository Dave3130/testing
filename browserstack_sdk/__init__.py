# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
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
from browserstack_sdk.bstack1ll1l111ll_opy_ import bstack1l111l11l_opy_
from browserstack_sdk.bstack1lll11111_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack1l1111l111_opy_():
  global CONFIG
  headers = {
        bstack1lllll1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬਤ"): bstack1lllll1l_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪਥ"),
      }
  proxies = bstack1ll111lll_opy_(CONFIG, bstack11ll1111l1_opy_)
  try:
    response = requests.get(bstack11ll1111l1_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack111ll1lll1_opy_ = response.json()[bstack1lllll1l_opy_ (u"ࠨࡪࡸࡦࡸ࠭ਦ")]
      logger.debug(bstack1111l11ll_opy_.format(response.json()))
      return bstack111ll1lll1_opy_
    else:
      logger.debug(bstack1l1lllll11_opy_.format(bstack1lllll1l_opy_ (u"ࠤࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡏ࡙ࡏࡏࠢࡳࡥࡷࡹࡥࠡࡧࡵࡶࡴࡸࠠࠣਧ")))
  except Exception as e:
    logger.debug(bstack1l1lllll11_opy_.format(e))
def bstack1l111111l1_opy_(hub_url):
  global CONFIG
  url = bstack1lllll1l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧਨ")+  hub_url + bstack1lllll1l_opy_ (u"ࠦ࠴ࡩࡨࡦࡥ࡮ࠦ਩")
  headers = {
        bstack1lllll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫਪ"): bstack1lllll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩਫ"),
      }
  proxies = bstack1ll111lll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1ll1l1111_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack11l1l1l1l_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack111ll1ll11_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
def bstack11l1ll1l1l_opy_():
  try:
    global bstack11lll1111_opy_
    bstack111ll1lll1_opy_ = bstack1l1111l111_opy_()
    bstack111l111l1l_opy_ = []
    results = []
    for bstack1111l11l11_opy_ in bstack111ll1lll1_opy_:
      bstack111l111l1l_opy_.append(bstack1l11111l1_opy_(target=bstack1l111111l1_opy_,args=(bstack1111l11l11_opy_,)))
    for t in bstack111l111l1l_opy_:
      t.start()
    for t in bstack111l111l1l_opy_:
      results.append(t.join())
    bstack11lll1l1l1_opy_ = {}
    for item in results:
      hub_url = item[bstack1lllll1l_opy_ (u"ࠧࡩࡷࡥࡣࡺࡸ࡬ࠨਬ")]
      latency = item[bstack1lllll1l_opy_ (u"ࠨ࡮ࡤࡸࡪࡴࡣࡺࠩਭ")]
      bstack11lll1l1l1_opy_[hub_url] = latency
    bstack111l1l111_opy_ = min(bstack11lll1l1l1_opy_, key= lambda x: bstack11lll1l1l1_opy_[x])
    bstack11lll1111_opy_ = bstack111l1l111_opy_
    logger.debug(bstack1ll11lll11_opy_.format(bstack111l1l111_opy_))
  except Exception as e:
    logger.debug(bstack111l11l1ll_opy_.format(e))
from browserstack_sdk.bstack11111111_opy_ import *
from browserstack_sdk.bstack1llll11l1_opy_ import *
from browserstack_sdk.bstack11l111l1_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack11llll111l_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack1lll1l111l_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
def bstack1l1ll1l1ll_opy_():
    global bstack11lll1111_opy_
    try:
        bstack11ll111111_opy_ = bstack11lll1lll1_opy_()
        bstack111lll1lll_opy_(bstack11ll111111_opy_)
        hub_url = bstack11ll111111_opy_.get(bstack1lllll1l_opy_ (u"ࠤࡸࡶࡱࠨਮ"), bstack1lllll1l_opy_ (u"ࠥࠦਯ"))
        if hub_url.endswith(bstack1lllll1l_opy_ (u"ࠫ࠴ࡽࡤ࠰ࡪࡸࡦࠬਰ")):
            hub_url = hub_url.rsplit(bstack1lllll1l_opy_ (u"ࠬ࠵ࡷࡥ࠱࡫ࡹࡧ࠭਱"), 1)[0]
        if hub_url.startswith(bstack1lllll1l_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࠧਲ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack1lllll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࠩਲ਼")):
            hub_url = hub_url[8:]
        bstack11lll1111_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack11lll1lll1_opy_():
    global CONFIG
    bstack11llllll11_opy_ = CONFIG.get(bstack1lllll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷࠬ਴"), {}).get(bstack1lllll1l_opy_ (u"ࠩࡪࡶ࡮ࡪࡎࡢ࡯ࡨࠫਵ"), bstack1lllll1l_opy_ (u"ࠪࡒࡔࡥࡇࡓࡋࡇࡣࡓࡇࡍࡆࡡࡓࡅࡘ࡙ࡅࡅࠩਸ਼"))
    if not isinstance(bstack11llllll11_opy_, str):
        raise ValueError(bstack1lllll1l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡋࡷ࡯ࡤࠡࡰࡤࡱࡪࠦ࡭ࡶࡵࡷࠤࡧ࡫ࠠࡢࠢࡹࡥࡱ࡯ࡤࠡࡵࡷࡶ࡮ࡴࡧࠣ਷"))
    try:
        bstack11ll111111_opy_ = bstack1l1l111111_opy_(bstack11llllll11_opy_)
        return bstack11ll111111_opy_
    except Exception as e:
        logger.error(bstack1lllll1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡨࡴ࡬ࡨࠥࡪࡥࡵࡣ࡬ࡰࡸࠦ࠺ࠡࡽࢀࠦਸ").format(str(e)))
        return {}
def bstack1l1l111111_opy_(bstack11llllll11_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack1lllll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨਹ")] or not CONFIG[bstack1lllll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ਺")]:
            raise ValueError(bstack1lllll1l_opy_ (u"ࠣࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡷࡶࡩࡷࡴࡡ࡮ࡧࠣࡳࡷࠦࡡࡤࡥࡨࡷࡸࠦ࡫ࡦࡻࠥ਻"))
        url = bstack1ll1l1lll1_opy_ + bstack11llllll11_opy_
        auth = (CONFIG[bstack1lllll1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨ਼ࠫ")], CONFIG[bstack1lllll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭਽")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1lll1l1111_opy_ = json.loads(response.text)
            return bstack1lll1l1111_opy_
    except ValueError as ve:
        logger.error(bstack1lllll1l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡨࡴ࡬ࡨࠥࡪࡥࡵࡣ࡬ࡰࡸࠦ࠺ࠡࡽࢀࠦਾ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack1lllll1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡩࡵ࡭ࡩࠦࡤࡦࡶࡤ࡭ࡱࡹࠠ࠻ࠢࡾࢁࠧਿ").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack111lll1lll_opy_(bstack11ll11l111_opy_):
    global CONFIG
    if bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪੀ") not in CONFIG or str(CONFIG[bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫੁ")]).lower() == bstack1lllll1l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧੂ"):
        CONFIG[bstack1lllll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨ੃")] = False
    elif bstack1lllll1l_opy_ (u"ࠪ࡭ࡸ࡚ࡲࡪࡣ࡯ࡋࡷ࡯ࡤࠨ੄") in bstack11ll11l111_opy_:
        bstack1111l1l11l_opy_ = CONFIG.get(bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੅"), {})
        logger.debug(bstack1lllll1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡾࡩࡴࡶ࡬ࡲ࡬ࠦ࡬ࡰࡥࡤࡰࠥࡵࡰࡵ࡫ࡲࡲࡸࡀࠠࠦࡵࠥ੆"), bstack1111l1l11l_opy_)
        bstack1lll11ll11_opy_ = bstack11ll11l111_opy_.get(bstack1lllll1l_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲࡘࡥࡱࡧࡤࡸࡪࡸࡳࠣੇ"), [])
        bstack1111l1111_opy_ = bstack1lllll1l_opy_ (u"ࠢ࠭ࠤੈ").join(bstack1lll11ll11_opy_)
        logger.debug(bstack1lllll1l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡄࡷࡶࡸࡴࡳࠠࡳࡧࡳࡩࡦࡺࡥࡳࠢࡶࡸࡷ࡯࡮ࡨ࠼ࠣࠩࡸࠨ੉"), bstack1111l1111_opy_)
        bstack1l1l111l1_opy_ = {
            bstack1lllll1l_opy_ (u"ࠤ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦ੊"): bstack1lllll1l_opy_ (u"ࠥࡥࡹࡹ࠭ࡳࡧࡳࡩࡦࡺࡥࡳࠤੋ"),
            bstack1lllll1l_opy_ (u"ࠦ࡫ࡵࡲࡤࡧࡏࡳࡨࡧ࡬ࠣੌ"): bstack1lllll1l_opy_ (u"ࠧࡺࡲࡶࡧ੍ࠥ"),
            bstack1lllll1l_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࠳ࡲࡦࡲࡨࡥࡹ࡫ࡲࠣ੎"): bstack1111l1111_opy_
        }
        bstack1111l1l11l_opy_.update(bstack1l1l111l1_opy_)
        logger.debug(bstack1lllll1l_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡕࡱࡦࡤࡸࡪࡪࠠ࡭ࡱࡦࡥࡱࠦ࡯ࡱࡶ࡬ࡳࡳࡹ࠺ࠡࠧࡶࠦ੏"), bstack1111l1l11l_opy_)
        CONFIG[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ੐")] = bstack1111l1l11l_opy_
        logger.debug(bstack1lllll1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡈ࡬ࡲࡦࡲࠠࡄࡑࡑࡊࡎࡍ࠺ࠡࠧࡶࠦੑ"), CONFIG)
def bstack1l1ll1lll1_opy_():
    bstack11ll111111_opy_ = bstack11lll1lll1_opy_()
    if not bstack11ll111111_opy_[bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࡕࡳ࡮ࠪ੒")]:
      raise ValueError(bstack1lllll1l_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡖࡴ࡯ࠤ࡮ࡹࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡨࡵࡳࡲࠦࡧࡳ࡫ࡧࠤࡩ࡫ࡴࡢ࡫࡯ࡷ࠳ࠨ੓"))
    return bstack11ll111111_opy_[bstack1lllll1l_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡗࡵࡰࠬ੔")] + bstack1lllll1l_opy_ (u"࠭࠿ࡤࡣࡳࡷࡂ࠭੕")
@measure(event_name=EVENTS.bstack1ll111l11l_opy_, stage=STAGE.bstack1l11ll1ll_opy_)
def bstack1l1l1111ll_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack1lllll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ੖")], CONFIG[bstack1lllll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ੗")])
        url = bstack11ll1lll1_opy_
        logger.debug(bstack1lllll1l_opy_ (u"ࠤࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡤࡸ࡭ࡱࡪࡳࠡࡨࡵࡳࡲࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯࡚ࠥࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠢࡄࡔࡎࠨ੘"))
        try:
            response = requests.get(url, auth=auth, headers={bstack1lllll1l_opy_ (u"ࠥࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠤਖ਼"): bstack1lllll1l_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠢਗ਼")})
            if response.status_code == 200:
                bstack1l1llll1l1_opy_ = json.loads(response.text)
                bstack1l1l1ll1l1_opy_ = bstack1l1llll1l1_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡷࠬਜ਼"), [])
                if bstack1l1l1ll1l1_opy_:
                    bstack11111ll11l_opy_ = bstack1l1l1ll1l1_opy_[0]
                    build_hashed_id = bstack11111ll11l_opy_.get(bstack1lllll1l_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩੜ"))
                    bstack1ll1l11lll_opy_ = bstack111l11l111_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1ll1l11lll_opy_])
                    logger.info(bstack11l1ll1l1_opy_.format(bstack1ll1l11lll_opy_))
                    bstack1l1l11111_opy_ = CONFIG[bstack1lllll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ੝")]
                    if bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪਫ਼") in CONFIG:
                      bstack1l1l11111_opy_ += bstack1lllll1l_opy_ (u"ࠩࠣࠫ੟") + CONFIG[bstack1lllll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ੠")]
                    if bstack1l1l11111_opy_ != bstack11111ll11l_opy_.get(bstack1lllll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ੡")):
                      logger.debug(bstack11111llll_opy_.format(bstack11111ll11l_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ੢")), bstack1l1l11111_opy_))
                    return result
                else:
                    logger.debug(bstack1lllll1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡔ࡯ࠡࡤࡸ࡭ࡱࡪࡳࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡸ࡭࡫ࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠰ࠥ੣"))
            else:
                logger.debug(bstack1lllll1l_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡤࡸ࡭ࡱࡪࡳ࠯ࠤ੤"))
        except Exception as e:
            logger.error(bstack1lllll1l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࡵࠣ࠾ࠥࢁࡽࠣ੥").format(str(e)))
    else:
        logger.debug(bstack1lllll1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡅࡒࡒࡋࡏࡇࠡ࡫ࡶࠤࡳࡵࡴࠡࡵࡨࡸ࠳ࠦࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡤࡸ࡭ࡱࡪࡳ࠯ࠤ੦"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1l11l1lll_opy_ import bstack1l11l1lll_opy_, Events, bstack11l1l11l11_opy_, bstack111lllllll_opy_
from bstack_utils.measure import bstack111l1111l_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1111l1111l_opy_ import bstack1111ll1lll_opy_
from bstack_utils.messages import *
from bstack_utils import bstack11llll111l_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l1lll111_opy_, bstack11l1l111l1_opy_, bstack11l111l1ll_opy_, bstack1l11l1l1_opy_, \
  bstack111l1lll11_opy_, \
  Notset, bstack111ll1l11_opy_, \
  bstack1l1l11l1l1_opy_, bstack1l1l1l1l11_opy_, bstack111ll1l111_opy_, bstack1l1l11llll_opy_, bstack11l1ll11l1_opy_, bstack111ll1111l_opy_, \
  bstack1llllll111_opy_, \
  bstack1ll1111ll_opy_, bstack1ll1l11ll1_opy_, bstack1l11ll111l_opy_, bstack1l1l1llll_opy_, \
  bstack111ll1lll_opy_, bstack1l1l11lll_opy_, bstack1111l11l1l_opy_, bstack1111lllll1_opy_
from bstack_utils.bstack1l11l1l111_opy_ import bstack1l111ll1l1_opy_
from bstack_utils.bstack1111ll1l1_opy_ import bstack11ll1ll1l_opy_, bstack11l11l1111_opy_
from bstack_utils.bstack1l1l111lll_opy_ import bstack11ll1ll11_opy_
from bstack_utils.bstack1l1ll111l1_opy_ import bstack1l1ll1l11_opy_, bstack1l1ll111ll_opy_
from bstack_utils.bstack11l11l11ll_opy_ import bstack11l11l11ll_opy_
from bstack_utils.bstack1111l1l11_opy_ import bstack11ll11ll1_opy_
from bstack_utils.proxy import bstack11l1111lll_opy_, bstack1ll111lll_opy_, bstack111l11ll1_opy_, bstack1l1l1l11ll_opy_
from bstack_utils.bstack1l11ll1lll_opy_ import bstack11ll11llll_opy_
import bstack_utils.bstack11l1llll1l_opy_ as bstack1l1ll11lll_opy_
import bstack_utils.bstack1l11l11111_opy_ as bstack11llll1ll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack1ll11111l1_opy_ import bstack11l111l11l_opy_
from bstack_utils.bstack111l1l1l_opy_ import bstack111l11ll_opy_
from bstack_utils.bstack1l1ll111l_opy_ import bstack1l111l111_opy_
if os.getenv(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡈࡐࡑࡎࡗࠬ੧")):
  cli.bstack1111lll1l1_opy_()
else:
  os.environ[bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡉࡑࡒࡏࡘ࠭੨")] = bstack1lllll1l_opy_ (u"ࠬࡺࡲࡶࡧࠪ੩")
bstack1l1111l1ll_opy_ = bstack1lllll1l_opy_ (u"࠭ࠠࠡ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࠦࠠࡪࡨࠫࡴࡦ࡭ࡥࠡ࠿ࡀࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮ࠦࡻ࡝ࡰࠣࠤࠥࡺࡲࡺࡽ࡟ࡲࠥࡩ࡯࡯ࡵࡷࠤ࡫ࡹࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࡠࠬ࡬ࡳ࡝ࠩࠬ࠿ࡡࡴࠠࠡࠢࠣࠤ࡫ࡹ࠮ࡢࡲࡳࡩࡳࡪࡆࡪ࡮ࡨࡗࡾࡴࡣࠩࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭࠲ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡲࡢ࡭ࡳࡪࡥࡹࠫࠣ࠯ࠥࠨ࠺ࠣࠢ࠮ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࠫࡥࡼࡧࡩࡵࠢࡱࡩࡼࡖࡡࡨࡧ࠵࠲ࡪࡼࡡ࡭ࡷࡤࡸࡪ࠮ࠢࠩࠫࠣࡁࡃࠦࡻࡾࠤ࠯ࠤࡡ࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡧࡦࡶࡖࡩࡸࡹࡩࡰࡰࡇࡩࡹࡧࡩ࡭ࡵࠥࢁࡡ࠭ࠩࠪࠫ࡞ࠦ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠢ࡞ࠫࠣ࠯ࠥࠨࠬ࡝࡞ࡱࠦ࠮ࡢ࡮ࠡࠢࠣࠤࢂࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࡼ࡞ࡱࠤࠥࠦࠠࡾ࡞ࡱࠤࠥࢃ࡜࡯ࠢࠣ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴࠭੪")
bstack1llll1ll1l_opy_ = bstack1lllll1l_opy_ (u"ࠧ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡵࡥࡩ࡯ࡦࡨࡼࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠳࡟࡟ࡲࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡸࡲࡩࡤࡧࠫ࠴࠱ࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴ࠫ࡟ࡲࡨࡵ࡮ࡴࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫ࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤࠬ࠿ࡡࡴࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁ࡜࡯࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࡠࡳࡺࡲࡺࠢࡾࡠࡳࡩࡡࡱࡵࠣࡁࠥࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠩ࡝ࡰࠣࠤࢂࠦࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࠢࡾࡠࡳࠦࠠࠡࠢࢀࡠࡳࠦࠠࡳࡧࡷࡹࡷࡴࠠࡢࡹࡤ࡭ࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴ࡣࡰࡰࡱࡩࡨࡺࠨࡼ࡞ࡱࠤࠥࠦࠠࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷ࠾ࠥࡦࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠥࡽࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩࡾࡢ࠯ࡠࡳࠦࠠࠡࠢ࠱࠲࠳ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷࡡࡴࠠࠡࡿࠬࡠࡳࢃ࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳ࠭੫")
from ._version import __version__
bstack1ll11ll1ll_opy_ = None
CONFIG = {}
bstack1lll1lll11_opy_ = {}
bstack11llllll1_opy_ = {}
bstack11llll1lll_opy_ = None
bstack11ll1l1l1_opy_ = None
bstack1l1ll1l1l1_opy_ = None
bstack11111ll1l1_opy_ = -1
bstack111lllll1l_opy_ = 0
bstack111l1ll11_opy_ = bstack1l11llll1_opy_
bstack1lll11ll1l_opy_ = 1
bstack11l11l1ll1_opy_ = False
bstack11lll1l111_opy_ = False
bstack1l11ll11l1_opy_ = bstack1lllll1l_opy_ (u"ࠨࠩ੬")
bstack1l1l1l111_opy_ = bstack1lllll1l_opy_ (u"ࠩࠪ੭")
bstack1l1111l11l_opy_ = False
bstack11ll1l1l1l_opy_ = True
bstack1ll111l1l1_opy_ = bstack1lllll1l_opy_ (u"ࠪࠫ੮")
bstack1111lll11l_opy_ = []
bstack1111l1l1l1_opy_ = threading.Lock()
bstack1ll1llll11_opy_ = threading.Lock()
bstack11lll1111_opy_ = bstack1lllll1l_opy_ (u"ࠫࠬ੯")
bstack1l11l11l1l_opy_ = False
bstack11ll1l1l11_opy_ = None
bstack11ll111l11_opy_ = None
bstack11ll1lll11_opy_ = None
bstack1l1llll1l_opy_ = -1
bstack11ll111l1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠬࢄࠧੰ")), bstack1lllll1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ੱ"), bstack1lllll1l_opy_ (u"ࠧ࠯ࡴࡲࡦࡴࡺ࠭ࡳࡧࡳࡳࡷࡺ࠭ࡩࡧ࡯ࡴࡪࡸ࠮࡫ࡵࡲࡲࠬੲ"))
bstack1l11ll111_opy_ = 0
bstack1ll111ll11_opy_ = 0
bstack1ll1ll11l_opy_ = []
bstack1l1l1l11l1_opy_ = []
bstack111llllll_opy_ = []
bstack111l11l11_opy_ = []
bstack1ll1ll11l1_opy_ = bstack1lllll1l_opy_ (u"ࠨࠩੳ")
bstack1111ll111_opy_ = bstack1lllll1l_opy_ (u"ࠩࠪੴ")
bstack1l1l1l1l1l_opy_ = False
bstack11111ll11_opy_ = False
bstack1lll111111_opy_ = {}
bstack1l11ll1ll1_opy_ = None
bstack1lll1l1lll_opy_ = None
bstack1ll1111l1l_opy_ = None
bstack1l1l1lll1_opy_ = None
bstack11l11llll_opy_ = None
bstack11ll111l1l_opy_ = None
bstack11l1l1llll_opy_ = None
bstack1ll11l11l_opy_ = None
bstack111lll111l_opy_ = None
bstack1llll1l1ll_opy_ = None
bstack1l1ll1lll_opy_ = None
bstack1lll1ll111_opy_ = None
bstack1111l11lll_opy_ = None
bstack1ll1ll1l11_opy_ = None
bstack11l11l1lll_opy_ = None
bstack11111l1lll_opy_ = None
bstack1lllllllll_opy_ = None
bstack1lll11l11l_opy_ = None
bstack11111l11l1_opy_ = None
bstack1l11l11ll_opy_ = None
bstack1l111l1l11_opy_ = None
bstack111llllll1_opy_ = None
bstack1ll111111_opy_ = None
thread_local = threading.local()
bstack1ll1ll1111_opy_ = False
bstack1111l1llll_opy_ = bstack1lllll1l_opy_ (u"ࠥࠦੵ")
logger = bstack11llll111l_opy_.get_logger(__name__, bstack111l1ll11_opy_)
bstack1lll1ll1l_opy_ = Config.bstack1111l1ll_opy_()
percy = bstack11111lll1l_opy_()
bstack1l11lll1ll_opy_ = bstack1111ll1lll_opy_()
bstack1l1ll1llll_opy_ = bstack11l111l1_opy_()
def bstack111l1l1ll_opy_():
  global CONFIG
  global bstack1l1l1l1l1l_opy_
  global bstack1lll1ll1l_opy_
  testContextOptions = bstack111ll11l1_opy_(CONFIG)
  if bstack111l1lll11_opy_(CONFIG):
    if (bstack1lllll1l_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭੶") in testContextOptions and str(testContextOptions[bstack1lllll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ੷")]).lower() == bstack1lllll1l_opy_ (u"࠭ࡴࡳࡷࡨࠫ੸")):
      bstack1l1l1l1l1l_opy_ = True
    bstack1lll1ll1l_opy_.bstack11ll11lll1_opy_(testContextOptions.get(bstack1lllll1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ੹"), False))
  else:
    bstack1l1l1l1l1l_opy_ = True
    bstack1lll1ll1l_opy_.bstack11ll11lll1_opy_(True)
def bstack11111111l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1l111llll1_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack11lll1ll11_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1lllll1l_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡥࡲࡲ࡫࡯ࡧࡧ࡫࡯ࡩࠧ੺") == args[i].lower() or bstack1lllll1l_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡦࡪࡩࠥ੻") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1ll111l1l1_opy_
      bstack1ll111l1l1_opy_ += bstack1lllll1l_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࠠࠨ੼") + shlex.quote(path)
      return path
  return None
bstack1l1111lll_opy_ = re.compile(bstack1lllll1l_opy_ (u"ࡶࠧ࠴ࠪࡀ࡞ࠧࡿ࠭࠴ࠪࡀࠫࢀ࠲࠯ࡅࠢ੽"))
def bstack1ll11l11ll_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l1111lll_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1lllll1l_opy_ (u"ࠧࠪࡻࠣ੾") + group + bstack1lllll1l_opy_ (u"ࠨࡽࠣ੿"), os.environ.get(group))
  return value
def bstack1111lll111_opy_():
  global bstack1ll111111_opy_
  if bstack1ll111111_opy_ is None:
        bstack1ll111111_opy_ = bstack11lll1ll11_opy_()
  bstack1ll11l1ll1_opy_ = bstack1ll111111_opy_
  if bstack1ll11l1ll1_opy_ and os.path.exists(os.path.abspath(bstack1ll11l1ll1_opy_)):
    fileName = bstack1ll11l1ll1_opy_
  if bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ઀") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬઁ")])) and not bstack1lllll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡎࡢ࡯ࡨࠫં") in locals():
    fileName = os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧઃ")]
  if bstack1lllll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࠭઄") in locals():
    bstack111l1l1_opy_ = os.path.abspath(fileName)
  else:
    bstack111l1l1_opy_ = bstack1lllll1l_opy_ (u"ࠬ࠭અ")
  bstack1l1llll11l_opy_ = os.getcwd()
  bstack1ll111lll1_opy_ = bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩઆ")
  bstack1l1lllllll_opy_ = bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹࡢ࡯࡯ࠫઇ")
  while (not os.path.exists(bstack111l1l1_opy_)) and bstack1l1llll11l_opy_ != bstack1lllll1l_opy_ (u"ࠣࠤઈ"):
    bstack111l1l1_opy_ = os.path.join(bstack1l1llll11l_opy_, bstack1ll111lll1_opy_)
    if not os.path.exists(bstack111l1l1_opy_):
      bstack111l1l1_opy_ = os.path.join(bstack1l1llll11l_opy_, bstack1l1lllllll_opy_)
    if bstack1l1llll11l_opy_ != os.path.dirname(bstack1l1llll11l_opy_):
      bstack1l1llll11l_opy_ = os.path.dirname(bstack1l1llll11l_opy_)
    else:
      bstack1l1llll11l_opy_ = bstack1lllll1l_opy_ (u"ࠤࠥઉ")
  bstack1ll111111_opy_ = bstack111l1l1_opy_ if os.path.exists(bstack111l1l1_opy_) else None
  return bstack1ll111111_opy_
def bstack11l11ll11l_opy_(config):
    if bstack1lllll1l_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࠪઊ") in config:
      config[bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨઋ")] = config[bstack1lllll1l_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠬઌ")]
    if bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬ࡕࡰࡵ࡫ࡲࡲࡸ࠭ઍ") in config:
      config[bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ઎")] = config[bstack1lllll1l_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࡐࡲࡷ࡭ࡴࡴࡳࠨએ")]
def bstack1111ll1l11_opy_():
  bstack111l1l1_opy_ = bstack1111lll111_opy_()
  if not os.path.exists(bstack111l1l1_opy_):
    bstack1l11l1l11l_opy_(
      bstack1l1llll1ll_opy_.format(os.getcwd()))
  try:
    with open(bstack111l1l1_opy_, bstack1lllll1l_opy_ (u"ࠩࡵࠫઐ")) as stream:
      yaml.add_implicit_resolver(bstack1lllll1l_opy_ (u"ࠥࠥࡵࡧࡴࡩࡧࡻࠦઑ"), bstack1l1111lll_opy_)
      yaml.add_constructor(bstack1lllll1l_opy_ (u"ࠦࠦࡶࡡࡵࡪࡨࡼࠧ઒"), bstack1ll11l11ll_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack11l11ll11l_opy_(config)
      return config
  except:
    with open(bstack111l1l1_opy_, bstack1lllll1l_opy_ (u"ࠬࡸࠧઓ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack11l11ll11l_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1l11l1l11l_opy_(bstack11l1ll111l_opy_.format(str(exc)))
def bstack111lll1l1l_opy_(config):
  bstack11l1l11l1l_opy_ = bstack1l11l1lll1_opy_(config)
  for option in list(bstack11l1l11l1l_opy_):
    if option.lower() in bstack11llll1111_opy_ and option != bstack11llll1111_opy_[option.lower()]:
      bstack11l1l11l1l_opy_[bstack11llll1111_opy_[option.lower()]] = bstack11l1l11l1l_opy_[option]
      del bstack11l1l11l1l_opy_[option]
  return config
def bstack1ll11lll1_opy_():
  global bstack11llllll1_opy_
  for key, bstack11lll1l11l_opy_ in bstack11ll111lll_opy_.items():
    if isinstance(bstack11lll1l11l_opy_, list):
      for var in bstack11lll1l11l_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack11llllll1_opy_[key] = os.environ[var]
          break
    elif bstack11lll1l11l_opy_ in os.environ and os.environ[bstack11lll1l11l_opy_] and str(os.environ[bstack11lll1l11l_opy_]).strip():
      bstack11llllll1_opy_[key] = os.environ[bstack11lll1l11l_opy_]
  if bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨઔ") in os.environ:
    bstack11llllll1_opy_[bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫક")] = {}
    bstack11llllll1_opy_[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬખ")][bstack1lllll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫગ")] = os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬઘ")]
def bstack11ll11lll_opy_():
  global bstack1lll1lll11_opy_
  global bstack1ll111l1l1_opy_
  bstack1ll1lll111_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack1lllll1l_opy_ (u"ࠫ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઙ").lower() == val.lower():
      bstack1lll1lll11_opy_[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩચ")] = {}
      bstack1lll1lll11_opy_[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪછ")][bstack1lllll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩજ")] = sys.argv[idx + 1]
      bstack1ll1lll111_opy_.extend([idx, idx + 1])
      break
  for key, bstack11l1lllll_opy_ in bstack1ll1l1l1l1_opy_.items():
    if isinstance(bstack11l1lllll_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack11l1lllll_opy_:
          if bstack1lllll1l_opy_ (u"ࠨ࠯࠰ࠫઝ") + var.lower() == val.lower() and key not in bstack1lll1lll11_opy_:
            bstack1lll1lll11_opy_[key] = sys.argv[idx + 1]
            bstack1ll111l1l1_opy_ += bstack1lllll1l_opy_ (u"ࠩࠣ࠱࠲࠭ઞ") + var + bstack1lllll1l_opy_ (u"ࠪࠤࠬટ") + shlex.quote(sys.argv[idx + 1])
            bstack1ll1lll111_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack1lllll1l_opy_ (u"ࠫ࠲࠳ࠧઠ") + bstack11l1lllll_opy_.lower() == val.lower() and key not in bstack1lll1lll11_opy_:
          bstack1lll1lll11_opy_[key] = sys.argv[idx + 1]
          bstack1ll111l1l1_opy_ += bstack1lllll1l_opy_ (u"ࠬࠦ࠭࠮ࠩડ") + bstack11l1lllll_opy_ + bstack1lllll1l_opy_ (u"࠭ࠠࠨઢ") + shlex.quote(sys.argv[idx + 1])
          bstack1ll1lll111_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack1ll1lll111_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack11lllll11_opy_(config):
  bstack1l111l111l_opy_ = config.keys()
  for bstack11l1ll1111_opy_, bstack111l11llll_opy_ in bstack11l1l1111_opy_.items():
    if bstack111l11llll_opy_ in bstack1l111l111l_opy_:
      config[bstack11l1ll1111_opy_] = config[bstack111l11llll_opy_]
      del config[bstack111l11llll_opy_]
  for bstack11l1ll1111_opy_, bstack111l11llll_opy_ in bstack1ll1ll1l1l_opy_.items():
    if isinstance(bstack111l11llll_opy_, list):
      for bstack1l1lll1111_opy_ in bstack111l11llll_opy_:
        if bstack1l1lll1111_opy_ in bstack1l111l111l_opy_:
          config[bstack11l1ll1111_opy_] = config[bstack1l1lll1111_opy_]
          del config[bstack1l1lll1111_opy_]
          break
    elif bstack111l11llll_opy_ in bstack1l111l111l_opy_:
      config[bstack11l1ll1111_opy_] = config[bstack111l11llll_opy_]
      del config[bstack111l11llll_opy_]
  for bstack1l1lll1111_opy_ in list(config):
    for bstack1ll1l11l11_opy_ in bstack111lllll11_opy_:
      if bstack1l1lll1111_opy_.lower() == bstack1ll1l11l11_opy_.lower() and bstack1l1lll1111_opy_ != bstack1ll1l11l11_opy_:
        config[bstack1ll1l11l11_opy_] = config[bstack1l1lll1111_opy_]
        del config[bstack1l1lll1111_opy_]
  bstack111111l1ll_opy_ = [{}]
  if not config.get(bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪણ")):
    config[bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫત")] = [{}]
  bstack111111l1ll_opy_ = config[bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬથ")]
  for platform in bstack111111l1ll_opy_:
    for bstack1l1lll1111_opy_ in list(platform):
      for bstack1ll1l11l11_opy_ in bstack111lllll11_opy_:
        if bstack1l1lll1111_opy_.lower() == bstack1ll1l11l11_opy_.lower() and bstack1l1lll1111_opy_ != bstack1ll1l11l11_opy_:
          platform[bstack1ll1l11l11_opy_] = platform[bstack1l1lll1111_opy_]
          del platform[bstack1l1lll1111_opy_]
  for bstack11l1ll1111_opy_, bstack111l11llll_opy_ in bstack1ll1ll1l1l_opy_.items():
    for platform in bstack111111l1ll_opy_:
      if isinstance(bstack111l11llll_opy_, list):
        for bstack1l1lll1111_opy_ in bstack111l11llll_opy_:
          if bstack1l1lll1111_opy_ in platform:
            platform[bstack11l1ll1111_opy_] = platform[bstack1l1lll1111_opy_]
            del platform[bstack1l1lll1111_opy_]
            break
      elif bstack111l11llll_opy_ in platform:
        platform[bstack11l1ll1111_opy_] = platform[bstack111l11llll_opy_]
        del platform[bstack111l11llll_opy_]
  for bstack11l1lll1ll_opy_ in bstack1ll1111111_opy_:
    if bstack11l1lll1ll_opy_ in config:
      if not bstack1ll1111111_opy_[bstack11l1lll1ll_opy_] in config:
        config[bstack1ll1111111_opy_[bstack11l1lll1ll_opy_]] = {}
      config[bstack1ll1111111_opy_[bstack11l1lll1ll_opy_]].update(config[bstack11l1lll1ll_opy_])
      del config[bstack11l1lll1ll_opy_]
  for platform in bstack111111l1ll_opy_:
    for bstack11l1lll1ll_opy_ in bstack1ll1111111_opy_:
      if bstack11l1lll1ll_opy_ in list(platform):
        if not bstack1ll1111111_opy_[bstack11l1lll1ll_opy_] in platform:
          platform[bstack1ll1111111_opy_[bstack11l1lll1ll_opy_]] = {}
        platform[bstack1ll1111111_opy_[bstack11l1lll1ll_opy_]].update(platform[bstack11l1lll1ll_opy_])
        del platform[bstack11l1lll1ll_opy_]
  config = bstack111lll1l1l_opy_(config)
  return config
def bstack11111l111_opy_(config):
  global bstack1l1l1l111_opy_
  bstack1l1111ll1_opy_ = False
  if bstack1lllll1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧદ") in config and str(config[bstack1lllll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨધ")]).lower() != bstack1lllll1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫન"):
    if bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ઩") not in config or str(config[bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫપ")]).lower() == bstack1lllll1l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧફ"):
      config[bstack1lllll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨબ")] = False
    else:
      bstack11ll111111_opy_ = bstack11lll1lll1_opy_()
      if bstack1lllll1l_opy_ (u"ࠪ࡭ࡸ࡚ࡲࡪࡣ࡯ࡋࡷ࡯ࡤࠨભ") in bstack11ll111111_opy_:
        if not bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨમ") in config:
          config[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩય")] = {}
        config[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪર")][bstack1lllll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઱")] = bstack1lllll1l_opy_ (u"ࠨࡣࡷࡷ࠲ࡸࡥࡱࡧࡤࡸࡪࡸࠧલ")
        bstack1l1111ll1_opy_ = True
        bstack1l1l1l111_opy_ = config[bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ળ")].get(bstack1lllll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ઴"))
  if bstack111l1lll11_opy_(config) and bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨવ") in config and str(config[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩશ")]).lower() != bstack1lllll1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬષ") and not bstack1l1111ll1_opy_:
    if not bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫસ") in config:
      config[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬહ")] = {}
    if not config[bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭઺")].get(bstack1lllll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡃ࡫ࡱࡥࡷࡿࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡣࡷ࡭ࡴࡴࠧ઻")) and not bstack1lllll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ઼࠭") in config[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩઽ")]:
      bstack1l1111ll_opy_ = datetime.datetime.now()
      bstack111llll111_opy_ = bstack1l1111ll_opy_.strftime(bstack1lllll1l_opy_ (u"࠭ࠥࡥࡡࠨࡦࡤࠫࡈࠦࡏࠪા"))
      hostname = socket.gethostname()
      bstack111l1ll1l1_opy_ = bstack1lllll1l_opy_ (u"ࠧࠨિ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1lllll1l_opy_ (u"ࠨࡽࢀࡣࢀࢃ࡟ࡼࡿࠪી").format(bstack111llll111_opy_, hostname, bstack111l1ll1l1_opy_)
      config[bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ુ")][bstack1lllll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૂ")] = identifier
    bstack1l1l1l111_opy_ = config[bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨૃ")].get(bstack1lllll1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૄ"))
  return config
def bstack11l111lll1_opy_():
  bstack1l1l11lll1_opy_ =  bstack1l1l11llll_opy_()[bstack1lllll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠬૅ")]
  return bstack1l1l11lll1_opy_ if bstack1l1l11lll1_opy_ else -1
def bstack1l1l11l11_opy_(bstack1l1l11lll1_opy_):
  global CONFIG
  if not bstack1lllll1l_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩ૆") in CONFIG[bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪે")]:
    return
  CONFIG[bstack1lllll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫૈ")] = CONFIG[bstack1lllll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૉ")].replace(
    bstack1lllll1l_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭૊"),
    str(bstack1l1l11lll1_opy_)
  )
def bstack11ll1l11ll_opy_():
  global CONFIG
  if not bstack1lllll1l_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫો") in CONFIG[bstack1lllll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨૌ")]:
    return
  bstack1l1111ll_opy_ = datetime.datetime.now()
  bstack111llll111_opy_ = bstack1l1111ll_opy_.strftime(bstack1lllll1l_opy_ (u"ࠧࠦࡦ࠰ࠩࡧ࠳ࠥࡉ࠼ࠨࡑ્ࠬ"))
  CONFIG[bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૎")] = CONFIG[bstack1lllll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૏")].replace(
    bstack1lllll1l_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩૐ"),
    bstack111llll111_opy_
  )
def bstack1l11l1l11_opy_():
  global CONFIG
  if bstack1lllll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૑") in CONFIG and not bool(CONFIG[bstack1lllll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૒")]):
    del CONFIG[bstack1lllll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૓")]
    return
  if not bstack1lllll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૔") in CONFIG:
    CONFIG[bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૕")] = bstack1lllll1l_opy_ (u"ࠩࠦࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬ૖")
  if bstack1lllll1l_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩ૗") in CONFIG[bstack1lllll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૘")]:
    bstack11ll1l11ll_opy_()
    os.environ[bstack1lllll1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ૙")] = CONFIG[bstack1lllll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૚")]
  if not bstack1lllll1l_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩ૛") in CONFIG[bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૜")]:
    return
  bstack1l1l11lll1_opy_ = bstack1lllll1l_opy_ (u"ࠩࠪ૝")
  bstack1l1lll11l_opy_ = bstack11l111lll1_opy_()
  if bstack1l1lll11l_opy_ != -1:
    bstack1l1l11lll1_opy_ = bstack1lllll1l_opy_ (u"ࠪࡇࡎࠦࠧ૞") + str(bstack1l1lll11l_opy_)
  if bstack1l1l11lll1_opy_ == bstack1lllll1l_opy_ (u"ࠫࠬ૟"):
    bstack1111lll1l_opy_ = bstack1l11l1l1l1_opy_(CONFIG[bstack1lllll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨૠ")])
    if bstack1111lll1l_opy_ != -1:
      bstack1l1l11lll1_opy_ = str(bstack1111lll1l_opy_)
  if bstack1l1l11lll1_opy_:
    bstack1l1l11l11_opy_(bstack1l1l11lll1_opy_)
    os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪૡ")] = CONFIG[bstack1lllll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩૢ")]
def bstack11llll11ll_opy_(bstack111l1ll111_opy_, bstack1ll1l1l11_opy_, path):
  json_data = {
    bstack1lllll1l_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૣ"): bstack1ll1l1l11_opy_
  }
  if os.path.exists(path):
    bstack1lll1l11ll_opy_ = json.load(open(path, bstack1lllll1l_opy_ (u"ࠩࡵࡦࠬ૤")))
  else:
    bstack1lll1l11ll_opy_ = {}
  bstack1lll1l11ll_opy_[bstack111l1ll111_opy_] = json_data
  with open(path, bstack1lllll1l_opy_ (u"ࠥࡻ࠰ࠨ૥")) as outfile:
    json.dump(bstack1lll1l11ll_opy_, outfile)
def bstack1l11l1l1l1_opy_(bstack111l1ll111_opy_):
  bstack111l1ll111_opy_ = str(bstack111l1ll111_opy_)
  bstack1l11l1ll11_opy_ = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠫࢃ࠭૦")), bstack1lllll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ૧"))
  try:
    if not os.path.exists(bstack1l11l1ll11_opy_):
      os.makedirs(bstack1l11l1ll11_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"࠭ࡾࠨ૨")), bstack1lllll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ૩"), bstack1lllll1l_opy_ (u"ࠨ࠰ࡥࡹ࡮ࡲࡤ࠮ࡰࡤࡱࡪ࠳ࡣࡢࡥ࡫ࡩ࠳ࡰࡳࡰࡰࠪ૪"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1lllll1l_opy_ (u"ࠩࡺࠫ૫")):
        pass
      with open(file_path, bstack1lllll1l_opy_ (u"ࠥࡻ࠰ࠨ૬")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1lllll1l_opy_ (u"ࠫࡷ࠭૭")) as bstack1ll11ll11_opy_:
      bstack1lll111l11_opy_ = json.load(bstack1ll11ll11_opy_)
    if bstack111l1ll111_opy_ in bstack1lll111l11_opy_:
      bstack1lllll1l1l_opy_ = bstack1lll111l11_opy_[bstack111l1ll111_opy_][bstack1lllll1l_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૮")]
      bstack1llll1lll1_opy_ = int(bstack1lllll1l1l_opy_) + 1
      bstack11llll11ll_opy_(bstack111l1ll111_opy_, bstack1llll1lll1_opy_, file_path)
      return bstack1llll1lll1_opy_
    else:
      bstack11llll11ll_opy_(bstack111l1ll111_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1lll11l1ll_opy_.format(str(e)))
    return -1
def bstack11l11l11l_opy_(config):
  if not config[bstack1lllll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ૯")] or not config[bstack1lllll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ૰")]:
    return True
  else:
    return False
def bstack1ll11l1111_opy_(config, index=0):
  global bstack1l1111l11l_opy_
  bstack1lll1ll1ll_opy_ = {}
  caps = bstack11l1lll111_opy_ + bstack11l1ll1l11_opy_
  if config.get(bstack1lllll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ૱"), False):
    bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭૲")] = True
    bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ૳")] = config.get(bstack1lllll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ૴"), {})
  if bstack1l1111l11l_opy_:
    caps += bstack11ll1l111l_opy_
  for key in config:
    if key in caps + [bstack1lllll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૵")]:
      continue
    bstack1lll1ll1ll_opy_[key] = config[key]
  if bstack1lllll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૶") in config:
    for bstack111111llll_opy_ in config[bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૷")][index]:
      if bstack111111llll_opy_ in caps:
        continue
      bstack1lll1ll1ll_opy_[bstack111111llll_opy_] = config[bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૸")][index][bstack111111llll_opy_]
  bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠩ࡫ࡳࡸࡺࡎࡢ࡯ࡨࠫૹ")] = socket.gethostname()
  if bstack1lllll1l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫૺ") in bstack1lll1ll1ll_opy_:
    del (bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬૻ")])
  return bstack1lll1ll1ll_opy_
def bstack1l1l1ll11l_opy_(config):
  global bstack1l1111l11l_opy_
  bstack11l1ll1ll1_opy_ = {}
  caps = bstack11l1ll1l11_opy_
  if bstack1l1111l11l_opy_:
    caps += bstack11ll1l111l_opy_
  for key in caps:
    if key in config:
      bstack11l1ll1ll1_opy_[key] = config[key]
  return bstack11l1ll1ll1_opy_
def bstack1l11ll1l11_opy_(bstack1lll1ll1ll_opy_, bstack11l1ll1ll1_opy_):
  bstack1lll1lll1l_opy_ = {}
  for key in bstack1lll1ll1ll_opy_.keys():
    if key in bstack11l1l1111_opy_:
      bstack1lll1lll1l_opy_[bstack11l1l1111_opy_[key]] = bstack1lll1ll1ll_opy_[key]
    else:
      bstack1lll1lll1l_opy_[key] = bstack1lll1ll1ll_opy_[key]
  for key in bstack11l1ll1ll1_opy_:
    if key in bstack11l1l1111_opy_:
      bstack1lll1lll1l_opy_[bstack11l1l1111_opy_[key]] = bstack11l1ll1ll1_opy_[key]
    else:
      bstack1lll1lll1l_opy_[key] = bstack11l1ll1ll1_opy_[key]
  return bstack1lll1lll1l_opy_
def bstack11111lll1_opy_(config, index=0):
  global bstack1l1111l11l_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11l11ll111_opy_ = bstack1l1lll111_opy_(bstack1111l1l1ll_opy_, config, logger)
  bstack11l1ll1ll1_opy_ = bstack1l1l1ll11l_opy_(config)
  bstack1l1l1l1ll1_opy_ = bstack11l1ll1l11_opy_
  bstack1l1l1l1ll1_opy_ += bstack1l1l11ll1l_opy_
  bstack11l1ll1ll1_opy_ = update(bstack11l1ll1ll1_opy_, bstack11l11ll111_opy_)
  if bstack1l1111l11l_opy_:
    bstack1l1l1l1ll1_opy_ += bstack11ll1l111l_opy_
  if bstack1lllll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૼ") in config:
    if bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ૽") in config[bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૾")][index]:
      caps[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭૿")] = config[bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ଀")][index][bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଁ")]
    if bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬଂ") in config[bstack1lllll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଃ")][index]:
      caps[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ଄")] = str(config[bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଅ")][index][bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଆ")])
    bstack1l11ll1l1l_opy_ = bstack1l1lll111_opy_(bstack1111l1l1ll_opy_, config[bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଇ")][index], logger)
    bstack1l1l1l1ll1_opy_ += list(bstack1l11ll1l1l_opy_.keys())
    for bstack11111l1l1l_opy_ in bstack1l1l1l1ll1_opy_:
      if bstack11111l1l1l_opy_ in config[bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଈ")][index]:
        if bstack11111l1l1l_opy_ == bstack1lllll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଉ"):
          try:
            bstack1l11ll1l1l_opy_[bstack11111l1l1l_opy_] = str(config[bstack1lllll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଊ")][index][bstack11111l1l1l_opy_] * 1.0)
          except:
            bstack1l11ll1l1l_opy_[bstack11111l1l1l_opy_] = str(config[bstack1lllll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩଋ")][index][bstack11111l1l1l_opy_])
        else:
          bstack1l11ll1l1l_opy_[bstack11111l1l1l_opy_] = config[bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଌ")][index][bstack11111l1l1l_opy_]
        del (config[bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ଍")][index][bstack11111l1l1l_opy_])
    bstack11l1ll1ll1_opy_ = update(bstack11l1ll1ll1_opy_, bstack1l11ll1l1l_opy_)
  bstack1lll1ll1ll_opy_ = bstack1ll11l1111_opy_(config, index)
  for bstack1l1lll1111_opy_ in bstack11l1ll1l11_opy_ + list(bstack11l11ll111_opy_.keys()):
    if bstack1l1lll1111_opy_ in bstack1lll1ll1ll_opy_:
      bstack11l1ll1ll1_opy_[bstack1l1lll1111_opy_] = bstack1lll1ll1ll_opy_[bstack1l1lll1111_opy_]
      del (bstack1lll1ll1ll_opy_[bstack1l1lll1111_opy_])
  if bstack111ll1l11_opy_(config):
    bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩ଎")] = True
    caps.update(bstack11l1ll1ll1_opy_)
    caps[bstack1lllll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫଏ")] = bstack1lll1ll1ll_opy_
  else:
    bstack1lll1ll1ll_opy_[bstack1lllll1l_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫଐ")] = False
    caps.update(bstack1l11ll1l11_opy_(bstack1lll1ll1ll_opy_, bstack11l1ll1ll1_opy_))
    if bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ଑") in caps:
      caps[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧ଒")] = caps[bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬଓ")]
      del (caps[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ଔ")])
    if bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪକ") in caps:
      caps[bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬଖ")] = caps[bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬଗ")]
      del (caps[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଘ")])
  return caps
def bstack11l1l11lll_opy_():
  global bstack11lll1111_opy_
  global CONFIG
  if bstack1l111llll1_opy_() <= version.parse(bstack1lllll1l_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ଙ")):
    if bstack11lll1111_opy_ != bstack1lllll1l_opy_ (u"ࠧࠨଚ"):
      return bstack1lllll1l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤଛ") + bstack11lll1111_opy_ + bstack1lllll1l_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨଜ")
    return bstack1ll111111l_opy_
  if bstack11lll1111_opy_ != bstack1lllll1l_opy_ (u"ࠪࠫଝ"):
    return bstack1lllll1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨଞ") + bstack11lll1111_opy_ + bstack1lllll1l_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨଟ")
  return bstack111lll11l1_opy_
def bstack1l1ll1l11l_opy_(options):
  return hasattr(options, bstack1lllll1l_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧଠ"))
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
def bstack11l11llll1_opy_(options, bstack1l1l1llll1_opy_):
  for bstack1111l1lll_opy_ in bstack1l1l1llll1_opy_:
    if bstack1111l1lll_opy_ in [bstack1lllll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬଡ"), bstack1lllll1l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬଢ")]:
      continue
    if bstack1111l1lll_opy_ in options._experimental_options:
      options._experimental_options[bstack1111l1lll_opy_] = update(options._experimental_options[bstack1111l1lll_opy_],
                                                         bstack1l1l1llll1_opy_[bstack1111l1lll_opy_])
    else:
      options.add_experimental_option(bstack1111l1lll_opy_, bstack1l1l1llll1_opy_[bstack1111l1lll_opy_])
  if bstack1lllll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧଣ") in bstack1l1l1llll1_opy_:
    for arg in bstack1l1l1llll1_opy_[bstack1lllll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨତ")]:
      options.add_argument(arg)
    del (bstack1l1l1llll1_opy_[bstack1lllll1l_opy_ (u"ࠫࡦࡸࡧࡴࠩଥ")])
  if bstack1lllll1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩଦ") in bstack1l1l1llll1_opy_:
    for ext in bstack1l1l1llll1_opy_[bstack1lllll1l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪଧ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l1l1llll1_opy_[bstack1lllll1l_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫନ")])
def bstack1l11l1111l_opy_(options, bstack11l1l1ll1l_opy_):
  if bstack1lllll1l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ଩") in bstack11l1l1ll1l_opy_:
    for bstack1l11ll1111_opy_ in bstack11l1l1ll1l_opy_[bstack1lllll1l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨପ")]:
      if bstack1l11ll1111_opy_ in options._preferences:
        options._preferences[bstack1l11ll1111_opy_] = update(options._preferences[bstack1l11ll1111_opy_], bstack11l1l1ll1l_opy_[bstack1lllll1l_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩଫ")][bstack1l11ll1111_opy_])
      else:
        options.set_preference(bstack1l11ll1111_opy_, bstack11l1l1ll1l_opy_[bstack1lllll1l_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪବ")][bstack1l11ll1111_opy_])
  if bstack1lllll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪଭ") in bstack11l1l1ll1l_opy_:
    for arg in bstack11l1l1ll1l_opy_[bstack1lllll1l_opy_ (u"࠭ࡡࡳࡩࡶࠫମ")]:
      options.add_argument(arg)
def bstack111l1l111l_opy_(options, bstack11l1l1lll_opy_):
  if bstack1lllll1l_opy_ (u"ࠧࡸࡧࡥࡺ࡮࡫ࡷࠨଯ") in bstack11l1l1lll_opy_:
    options.use_webview(bool(bstack11l1l1lll_opy_[bstack1lllll1l_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࠩର")]))
  bstack11l11llll1_opy_(options, bstack11l1l1lll_opy_)
def bstack111lll11ll_opy_(options, bstack111lll11l_opy_):
  for bstack1l111lllll_opy_ in bstack111lll11l_opy_:
    if bstack1l111lllll_opy_ in [bstack1lllll1l_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭଱"), bstack1lllll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଲ")]:
      continue
    options.set_capability(bstack1l111lllll_opy_, bstack111lll11l_opy_[bstack1l111lllll_opy_])
  if bstack1lllll1l_opy_ (u"ࠫࡦࡸࡧࡴࠩଳ") in bstack111lll11l_opy_:
    for arg in bstack111lll11l_opy_[bstack1lllll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪ଴")]:
      options.add_argument(arg)
  if bstack1lllll1l_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪଵ") in bstack111lll11l_opy_:
    options.bstack1111l11111_opy_(bool(bstack111lll11l_opy_[bstack1lllll1l_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫଶ")]))
def bstack1l11lllll1_opy_(options, bstack11l111ll1_opy_):
  for bstack1ll1lll1ll_opy_ in bstack11l111ll1_opy_:
    if bstack1ll1lll1ll_opy_ in [bstack1lllll1l_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬଷ"), bstack1lllll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧସ")]:
      continue
    options._options[bstack1ll1lll1ll_opy_] = bstack11l111ll1_opy_[bstack1ll1lll1ll_opy_]
  if bstack1lllll1l_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧହ") in bstack11l111ll1_opy_:
    for bstack1ll11lll1l_opy_ in bstack11l111ll1_opy_[bstack1lllll1l_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ଺")]:
      options.bstack1111l1ll1_opy_(
        bstack1ll11lll1l_opy_, bstack11l111ll1_opy_[bstack1lllll1l_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ଻")][bstack1ll11lll1l_opy_])
  if bstack1lllll1l_opy_ (u"࠭ࡡࡳࡩࡶ଼ࠫ") in bstack11l111ll1_opy_:
    for arg in bstack11l111ll1_opy_[bstack1lllll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬଽ")]:
      options.add_argument(arg)
def bstack1llll1l111_opy_(options, caps):
  if not hasattr(options, bstack1lllll1l_opy_ (u"ࠨࡍࡈ࡝ࠬା")):
    return
  if options.KEY == bstack1lllll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧି"):
    options = bstack1111ll1l_opy_.bstack1l111ll1ll_opy_(bstack1ll11llll_opy_=options, config=CONFIG)
  if options.KEY == bstack1lllll1l_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨୀ") and options.KEY in caps:
    bstack11l11llll1_opy_(options, caps[bstack1lllll1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩୁ")])
  elif options.KEY == bstack1lllll1l_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪୂ") and options.KEY in caps:
    bstack1l11l1111l_opy_(options, caps[bstack1lllll1l_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫୃ")])
  elif options.KEY == bstack1lllll1l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨୄ") and options.KEY in caps:
    bstack111lll11ll_opy_(options, caps[bstack1lllll1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ୅")])
  elif options.KEY == bstack1lllll1l_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ୆") and options.KEY in caps:
    bstack111l1l111l_opy_(options, caps[bstack1lllll1l_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫେ")])
  elif options.KEY == bstack1lllll1l_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪୈ") and options.KEY in caps:
    bstack1l11lllll1_opy_(options, caps[bstack1lllll1l_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫ୉")])
def bstack1l1l11l111_opy_(caps):
  global bstack1l1111l11l_opy_
  if isinstance(os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ୊")), str):
    bstack1l1111l11l_opy_ = eval(os.getenv(bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨୋ")))
  if bstack1l1111l11l_opy_:
    if bstack11111111l_opy_() < version.parse(bstack1lllll1l_opy_ (u"ࠨ࠴࠱࠷࠳࠶ࠧୌ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1lllll1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦ୍ࠩ")
    if bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ୎") in caps:
      browser = caps[bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ୏")]
    elif bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭୐") in caps:
      browser = caps[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧ୑")]
    browser = str(browser).lower()
    if browser == bstack1lllll1l_opy_ (u"ࠧࡪࡲ࡫ࡳࡳ࡫ࠧ୒") or browser == bstack1lllll1l_opy_ (u"ࠨ࡫ࡳࡥࡩ࠭୓"):
      browser = bstack1lllll1l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩ୔")
    if browser == bstack1lllll1l_opy_ (u"ࠪࡷࡦࡳࡳࡶࡰࡪࠫ୕"):
      browser = bstack1lllll1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫୖ")
    if browser not in [bstack1lllll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬୗ"), bstack1lllll1l_opy_ (u"࠭ࡥࡥࡩࡨࠫ୘"), bstack1lllll1l_opy_ (u"ࠧࡪࡧࠪ୙"), bstack1lllll1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨ୚"), bstack1lllll1l_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪ୛")]:
      return None
    try:
      package = bstack1lllll1l_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲ࠯ࡽࢀ࠲ࡴࡶࡴࡪࡱࡱࡷࠬଡ଼").format(browser)
      name = bstack1lllll1l_opy_ (u"ࠫࡔࡶࡴࡪࡱࡱࡷࠬଢ଼")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1l1ll1l11l_opy_(options):
        return None
      for bstack1l1lll1111_opy_ in caps.keys():
        options.set_capability(bstack1l1lll1111_opy_, caps[bstack1l1lll1111_opy_])
      bstack1llll1l111_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1lll11l1l1_opy_(options, bstack11111lllll_opy_):
  if not bstack1l1ll1l11l_opy_(options):
    return
  for bstack1l1lll1111_opy_ in bstack11111lllll_opy_.keys():
    if bstack1l1lll1111_opy_ in bstack1l1l11ll1l_opy_:
      continue
    if bstack1l1lll1111_opy_ in options._caps and type(options._caps[bstack1l1lll1111_opy_]) in [dict, list]:
      options._caps[bstack1l1lll1111_opy_] = update(options._caps[bstack1l1lll1111_opy_], bstack11111lllll_opy_[bstack1l1lll1111_opy_])
    else:
      options.set_capability(bstack1l1lll1111_opy_, bstack11111lllll_opy_[bstack1l1lll1111_opy_])
  bstack1llll1l111_opy_(options, bstack11111lllll_opy_)
  if bstack1lllll1l_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡧࡩࡧࡻࡧࡨࡧࡵࡅࡩࡪࡲࡦࡵࡶࠫ୞") in options._caps:
    if options._caps[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫୟ")] and options._caps[bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬୠ")].lower() != bstack1lllll1l_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩୡ"):
      del options._caps[bstack1lllll1l_opy_ (u"ࠩࡰࡳࡿࡀࡤࡦࡤࡸ࡫࡬࡫ࡲࡂࡦࡧࡶࡪࡹࡳࠨୢ")]
def bstack11l1l1ll11_opy_(proxy_config):
  if bstack1lllll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧୣ") in proxy_config:
    proxy_config[bstack1lllll1l_opy_ (u"ࠫࡸࡹ࡬ࡑࡴࡲࡼࡾ࠭୤")] = proxy_config[bstack1lllll1l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ୥")]
    del (proxy_config[bstack1lllll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ୦")])
  if bstack1lllll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪ୧") in proxy_config and proxy_config[bstack1lllll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ୨")].lower() != bstack1lllll1l_opy_ (u"ࠩࡧ࡭ࡷ࡫ࡣࡵࠩ୩"):
    proxy_config[bstack1lllll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭୪")] = bstack1lllll1l_opy_ (u"ࠫࡲࡧ࡮ࡶࡣ࡯ࠫ୫")
  if bstack1lllll1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡅࡺࡺ࡯ࡤࡱࡱࡪ࡮࡭ࡕࡳ࡮ࠪ୬") in proxy_config:
    proxy_config[bstack1lllll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩ୭")] = bstack1lllll1l_opy_ (u"ࠧࡱࡣࡦࠫ୮")
  return proxy_config
def bstack1111111ll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1lllll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧ୯") in config:
    return proxy
  config[bstack1lllll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨ୰")] = bstack11l1l1ll11_opy_(config[bstack1lllll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩୱ")])
  if proxy == None:
    proxy = Proxy(config[bstack1lllll1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ୲")])
  return proxy
def bstack11111l1ll1_opy_(self):
  global CONFIG
  global bstack1lll1ll111_opy_
  try:
    proxy = bstack111l11ll1_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1lllll1l_opy_ (u"ࠬ࠴ࡰࡢࡥࠪ୳")):
        proxies = bstack11l1111lll_opy_(proxy, bstack11l1l11lll_opy_())
        if len(proxies) > 0:
          protocol, bstack11ll1l1lll_opy_ = proxies.popitem()
          if bstack1lllll1l_opy_ (u"ࠨ࠺࠰࠱ࠥ୴") in bstack11ll1l1lll_opy_:
            return bstack11ll1l1lll_opy_
          else:
            return bstack1lllll1l_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣ୵") + bstack11ll1l1lll_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1lllll1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡵࡸ࡯ࡹࡻࠣࡹࡷࡲࠠ࠻ࠢࡾࢁࠧ୶").format(str(e)))
  return bstack1lll1ll111_opy_(self)
def bstack11lll111l1_opy_():
  global CONFIG
  return bstack1l1l1l11ll_opy_(CONFIG) and bstack111ll1111l_opy_() and bstack1l111llll1_opy_() >= version.parse(bstack1l1l1l1lll_opy_)
def bstack1ll11l1lll_opy_():
  global CONFIG
  return (bstack1lllll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ୷") in CONFIG or bstack1lllll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧ୸") in CONFIG) and bstack1llllll111_opy_()
def bstack1l11l1lll1_opy_(config):
  bstack11l1l11l1l_opy_ = {}
  if bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୹") in config:
    bstack11l1l11l1l_opy_ = config[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୺")]
  if bstack1lllll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୻") in config:
    bstack11l1l11l1l_opy_ = config[bstack1lllll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୼")]
  proxy = bstack111l11ll1_opy_(config)
  if proxy:
    if proxy.endswith(bstack1lllll1l_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭୽")) and os.path.isfile(proxy):
      bstack11l1l11l1l_opy_[bstack1lllll1l_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩࠬ୾")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1lllll1l_opy_ (u"ࠪ࠲ࡵࡧࡣࠨ୿")):
        proxies = bstack1ll111lll_opy_(config, bstack11l1l11lll_opy_())
        if len(proxies) > 0:
          protocol, bstack11ll1l1lll_opy_ = proxies.popitem()
          if bstack1lllll1l_opy_ (u"ࠦ࠿࠵࠯ࠣ஀") in bstack11ll1l1lll_opy_:
            parsed_url = urlparse(bstack11ll1l1lll_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1lllll1l_opy_ (u"ࠧࡀ࠯࠰ࠤ஁") + bstack11ll1l1lll_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack11l1l11l1l_opy_[bstack1lllll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩஂ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack11l1l11l1l_opy_[bstack1lllll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖ࡯ࡳࡶࠪஃ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack11l1l11l1l_opy_[bstack1lllll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫ஄")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack11l1l11l1l_opy_[bstack1lllll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬஅ")] = str(parsed_url.password)
  return bstack11l1l11l1l_opy_
def bstack111ll11l1_opy_(config):
  if bstack1lllll1l_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨஆ") in config:
    return config[bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩஇ")]
  return {}
def bstack1llll1l1l1_opy_(caps):
  global bstack1l1l1l111_opy_
  if bstack1lllll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ஈ") in caps:
    caps[bstack1lllll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧஉ")][bstack1lllll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭ஊ")] = True
    if bstack1l1l1l111_opy_:
      caps[bstack1lllll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ஋")][bstack1lllll1l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ஌")] = bstack1l1l1l111_opy_
  else:
    caps[bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࠨ஍")] = True
    if bstack1l1l1l111_opy_:
      caps[bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬஎ")] = bstack1l1l1l111_opy_
@measure(event_name=EVENTS.bstack1lllll1l11_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1ll1ll1ll1_opy_():
  global CONFIG
  if not bstack111l1lll11_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩஏ") in CONFIG and bstack1111l11l1l_opy_(CONFIG[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪஐ")]):
    if (
      bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ஑") in CONFIG
      and bstack1111l11l1l_opy_(CONFIG[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬஒ")].get(bstack1lllll1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡂࡪࡰࡤࡶࡾࡏ࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡢࡶ࡬ࡳࡳ࠭ஓ")))
    ):
      logger.debug(bstack1lllll1l_opy_ (u"ࠥࡐࡴࡩࡡ࡭ࠢࡥ࡭ࡳࡧࡲࡺࠢࡱࡳࡹࠦࡳࡵࡣࡵࡸࡪࡪࠠࡢࡵࠣࡷࡰ࡯ࡰࡃ࡫ࡱࡥࡷࡿࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡣࡷ࡭ࡴࡴࠠࡪࡵࠣࡩࡳࡧࡢ࡭ࡧࡧࠦஔ"))
      return
    bstack11l1l11l1l_opy_ = bstack1l11l1lll1_opy_(CONFIG)
    bstack1lllllll1l_opy_(CONFIG[bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧக")], bstack11l1l11l1l_opy_)
def bstack1lllllll1l_opy_(key, bstack11l1l11l1l_opy_):
  global bstack1ll11ll1ll_opy_
  logger.info(bstack1l11l111ll_opy_)
  try:
    bstack1ll11ll1ll_opy_ = Local()
    bstack11l11l111l_opy_ = {bstack1lllll1l_opy_ (u"ࠬࡱࡥࡺࠩ஖"): key}
    bstack11l11l111l_opy_.update(bstack11l1l11l1l_opy_)
    logger.debug(bstack1111l1l111_opy_.format(str(bstack11l11l111l_opy_)).replace(key, bstack1lllll1l_opy_ (u"࡛࠭ࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪ஗")))
    bstack1ll11ll1ll_opy_.start(**bstack11l11l111l_opy_)
    if bstack1ll11ll1ll_opy_.isRunning():
      logger.info(bstack1ll1l1ll1_opy_)
  except Exception as e:
    bstack1l11l1l11l_opy_(bstack1ll11ll111_opy_.format(str(e)))
def bstack1l1ll11111_opy_():
  global bstack1ll11ll1ll_opy_
  if bstack1ll11ll1ll_opy_.isRunning():
    logger.info(bstack11lllllll1_opy_)
    bstack1ll11ll1ll_opy_.stop()
  bstack1ll11ll1ll_opy_ = None
def bstack1llllll1ll_opy_(bstack111ll1l1l1_opy_=[]):
  global CONFIG
  bstack1111llll1_opy_ = []
  bstack11111l1111_opy_ = [bstack1lllll1l_opy_ (u"ࠧࡰࡵࠪ஘"), bstack1lllll1l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫங"), bstack1lllll1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ச"), bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ஛"), bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩஜ"), bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭஝")]
  try:
    for err in bstack111ll1l1l1_opy_:
      bstack11lll11ll1_opy_ = {}
      for k in bstack11111l1111_opy_:
        val = CONFIG[bstack1lllll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩஞ")][int(err[bstack1lllll1l_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ட")])].get(k)
        if val:
          bstack11lll11ll1_opy_[k] = val
      if(err[bstack1lllll1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ஠")] != bstack1lllll1l_opy_ (u"ࠩࠪ஡")):
        bstack11lll11ll1_opy_[bstack1lllll1l_opy_ (u"ࠪࡸࡪࡹࡴࡴࠩ஢")] = {
          err[bstack1lllll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩண")]: err[bstack1lllll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫத")]
        }
        bstack1111llll1_opy_.append(bstack11lll11ll1_opy_)
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡲࡶࡲࡧࡴࡵ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࡀࠠࠨ஥") + str(e))
  finally:
    return bstack1111llll1_opy_
def bstack1111l1ll1l_opy_(file_name):
  bstack11l1111111_opy_ = []
  try:
    bstack11111lll11_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack11111lll11_opy_):
      with open(bstack11111lll11_opy_) as f:
        bstack1ll1111lll_opy_ = json.load(f)
        bstack11l1111111_opy_ = bstack1ll1111lll_opy_
      os.remove(bstack11111lll11_opy_)
    return bstack11l1111111_opy_
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩ࡭ࡳࡪࡩ࡯ࡩࠣࡩࡷࡸ࡯ࡳࠢ࡯࡭ࡸࡺ࠺ࠡࠩ஦") + str(e))
    return bstack11l1111111_opy_
def bstack1ll1l1l1l_opy_():
  try:
      from bstack_utils.constants import bstack11111ll111_opy_, EVENTS
      from bstack_utils.helper import bstack11l1l111l1_opy_, get_host_info, bstack1lll1ll1l_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack11llll111_opy_ = os.path.join(os.getcwd(), bstack1lllll1l_opy_ (u"ࠨ࡮ࡲ࡫ࠬ஧"), bstack1lllll1l_opy_ (u"ࠩ࡮ࡩࡾ࠳࡭ࡦࡶࡵ࡭ࡨࡹ࠮࡫ࡵࡲࡲࠬந"))
      lock = FileLock(bstack11llll111_opy_+bstack1lllll1l_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤன"))
      def bstack1l111111_opy_():
          try:
              with lock:
                  with open(bstack11llll111_opy_, bstack1lllll1l_opy_ (u"ࠦࡷࠨப"), encoding=bstack1lllll1l_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦ஫")) as file:
                      data = json.load(file)
                      config = {
                          bstack1lllll1l_opy_ (u"ࠨࡨࡦࡣࡧࡩࡷࡹࠢ஬"): {
                              bstack1lllll1l_opy_ (u"ࠢࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪࠨ஭"): bstack1lllll1l_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠦம"),
                          }
                      }
                      bstack1llll11l11_opy_ = datetime.utcnow()
                      bstack1l1111ll_opy_ = bstack1llll11l11_opy_.strftime(bstack1lllll1l_opy_ (u"ࠤࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠴ࠥࡧࠢࡘࡘࡈࠨய"))
                      test_id = os.environ.get(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨர")) if os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩற")) else bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢல"))
                      payload = {
                          bstack1lllll1l_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠥள"): bstack1lllll1l_opy_ (u"ࠢࡴࡦ࡮ࡣࡪࡼࡥ࡯ࡶࡶࠦழ"),
                          bstack1lllll1l_opy_ (u"ࠣࡦࡤࡸࡦࠨவ"): {
                              bstack1lllll1l_opy_ (u"ࠤࡷࡩࡸࡺࡨࡶࡤࡢࡹࡺ࡯ࡤࠣஶ"): test_id,
                              bstack1lllll1l_opy_ (u"ࠥࡧࡷ࡫ࡡࡵࡧࡧࡣࡩࡧࡹࠣஷ"): bstack1l1111ll_opy_,
                              bstack1lllll1l_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡲࡦࡳࡥࠣஸ"): bstack1lllll1l_opy_ (u"࡙ࠧࡄࡌࡈࡨࡥࡹࡻࡲࡦࡒࡨࡶ࡫ࡵࡲ࡮ࡣࡱࡧࡪࠨஹ"),
                              bstack1lllll1l_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡰࡳࡰࡰࠥ஺"): {
                                  bstack1lllll1l_opy_ (u"ࠢ࡮ࡧࡤࡷࡺࡸࡥࡴࠤ஻"): data,
                                  bstack1lllll1l_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥ஼"): bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦ஽"))
                              },
                              bstack1lllll1l_opy_ (u"ࠥࡹࡸ࡫ࡲࡠࡦࡤࡸࡦࠨா"): bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠦࡺࡹࡥࡳࡐࡤࡱࡪࠨி")),
                              bstack1lllll1l_opy_ (u"ࠧ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠣீ"): get_host_info()
                          }
                      }
                      bstack1l11l1ll1_opy_ = bstack11l111l1ll_opy_(cli.config, [bstack1lllll1l_opy_ (u"ࠨࡡࡱ࡫ࡶࠦு"), bstack1lllll1l_opy_ (u"ࠢࡦࡦࡶࡍࡳࡹࡴࡳࡷࡰࡩࡳࡺࡡࡵ࡫ࡲࡲࠧூ"), bstack1lllll1l_opy_ (u"ࠣࡣࡳ࡭ࠧ௃")], bstack11111ll111_opy_)
                      response = bstack11l1l111l1_opy_(bstack1lllll1l_opy_ (u"ࠤࡓࡓࡘ࡚ࠢ௄"), bstack1l11l1ll1_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack1lllll1l_opy_ (u"ࠥࡈࡦࡺࡡࠡࡵࡨࡲࡹࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥࡺ࡯ࠡࡽࢀࠤࡼ࡯ࡴࡩࠢࡧࡥࡹࡧࠠࡼࡿࠥ௅").format(bstack11111ll111_opy_, payload))
                      else:
                          logger.debug(bstack1lllll1l_opy_ (u"ࠦࡗ࡫ࡱࡶࡧࡶࡸࠥ࡬ࡡࡪ࡮ࡨࡨࠥ࡬࡯ࡳࠢࡾࢁࠥࡽࡩࡵࡪࠣࡨࡦࡺࡡࠡࡽࢀࠦெ").format(bstack11111ll111_opy_, payload))
          except Exception as e:
              logger.debug(bstack1lllll1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡲࡩࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶࠤࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࠦࡻࡾࠤே").format(e))
      bstack1l111111_opy_()
      bstack1l1l1l1l11_opy_(bstack11llll111_opy_, logger)
  except:
    pass
def bstack11l11111l_opy_():
  global bstack1111l1llll_opy_
  global bstack1111lll11l_opy_
  global bstack1ll1ll11l_opy_
  global bstack1l1l1l11l1_opy_
  global bstack111llllll_opy_
  global bstack1111ll111_opy_
  global CONFIG
  bstack111l1ll1ll_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧை"))
  if bstack111l1ll1ll_opy_ in [bstack1lllll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭௉"), bstack1lllll1l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧொ")]:
    bstack1l1111llll_opy_()
  percy.shutdown()
  if bstack1111l1llll_opy_:
    logger.warning(bstack111111l11_opy_.format(str(bstack1111l1llll_opy_)))
  else:
    try:
      bstack1lll1l11ll_opy_ = bstack1l1l11l1l1_opy_(bstack1lllll1l_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨோ"), logger)
      if bstack1lll1l11ll_opy_.get(bstack1lllll1l_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨௌ")) and bstack1lll1l11ll_opy_.get(bstack1lllll1l_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭்ࠩ")).get(bstack1lllll1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧ௎")):
        logger.warning(bstack111111l11_opy_.format(str(bstack1lll1l11ll_opy_[bstack1lllll1l_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫ௏")][bstack1lllll1l_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩௐ")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1l11l1lll_opy_.invoke(Events.bstack1lll1111ll_opy_)
  logger.info(bstack111l11ll11_opy_)
  global bstack1ll11ll1ll_opy_
  if bstack1ll11ll1ll_opy_:
    bstack1l1ll11111_opy_()
  try:
    with bstack1111l1l1l1_opy_:
      bstack1l1l11l1ll_opy_ = bstack1111lll11l_opy_.copy()
    for driver in bstack1l1l11l1ll_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack11l11l111_opy_)
  if bstack1111ll111_opy_ == bstack1lllll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ௑"):
    bstack111llllll_opy_ = bstack1111l1ll1l_opy_(bstack1lllll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪ௒"))
  if bstack1111ll111_opy_ == bstack1lllll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ௓") and len(bstack1l1l1l11l1_opy_) == 0:
    bstack1l1l1l11l1_opy_ = bstack1111l1ll1l_opy_(bstack1lllll1l_opy_ (u"ࠫࡵࡽ࡟ࡱࡻࡷࡩࡸࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩ௔"))
    if len(bstack1l1l1l11l1_opy_) == 0:
      bstack1l1l1l11l1_opy_ = bstack1111l1ll1l_opy_(bstack1lllll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡶࡰࡱࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫ௕"))
  bstack111lll1ll_opy_ = bstack1lllll1l_opy_ (u"࠭ࠧ௖")
  if len(bstack1ll1ll11l_opy_) > 0:
    bstack111lll1ll_opy_ = bstack1llllll1ll_opy_(bstack1ll1ll11l_opy_)
  elif len(bstack1l1l1l11l1_opy_) > 0:
    bstack111lll1ll_opy_ = bstack1llllll1ll_opy_(bstack1l1l1l11l1_opy_)
  elif len(bstack111llllll_opy_) > 0:
    bstack111lll1ll_opy_ = bstack1llllll1ll_opy_(bstack111llllll_opy_)
  elif len(bstack111l11l11_opy_) > 0:
    bstack111lll1ll_opy_ = bstack1llllll1ll_opy_(bstack111l11l11_opy_)
  if bool(bstack111lll1ll_opy_):
    bstack1l11lll11l_opy_(bstack111lll1ll_opy_)
  else:
    bstack1l11lll11l_opy_()
  bstack1l1l1l1l11_opy_(bstack1lll1l11l1_opy_, logger)
  if bstack111l1ll1ll_opy_ not in [bstack1lllll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨௗ")]:
    bstack1ll1l1l1l_opy_()
  bstack11llll111l_opy_.bstack1ll1llll_opy_(CONFIG)
  if len(bstack111llllll_opy_) > 0:
    sys.exit(len(bstack111llllll_opy_))
def bstack1l11l11l1_opy_(bstack1ll1lll11_opy_, frame):
  global bstack1lll1ll1l_opy_
  logger.error(bstack1l1ll1111l_opy_)
  bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡐࡲࠫ௘"), bstack1ll1lll11_opy_)
  if hasattr(signal, bstack1lllll1l_opy_ (u"ࠩࡖ࡭࡬ࡴࡡ࡭ࡵࠪ௙")):
    bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪ௚"), signal.Signals(bstack1ll1lll11_opy_).name)
  else:
    bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ௛"), bstack1lllll1l_opy_ (u"࡙ࠬࡉࡈࡗࡑࡏࡓࡕࡗࡏࠩ௜"))
  if cli.is_running():
    bstack1l11l1lll_opy_.invoke(Events.bstack1lll1111ll_opy_)
  bstack111l1ll1ll_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧ௝"))
  if bstack111l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ௞") and not cli.is_enabled(CONFIG):
    bstack1ll1l1l1_opy_.stop(bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ௟")))
  bstack11l11111l_opy_()
  sys.exit(1)
def bstack1l11l1l11l_opy_(err):
  logger.critical(bstack1l1l1ll11_opy_.format(str(err)))
  bstack1l11lll11l_opy_(bstack1l1l1ll11_opy_.format(str(err)), True)
  atexit.unregister(bstack11l11111l_opy_)
  bstack1l1111llll_opy_()
  sys.exit(1)
def bstack1l1ll11ll1_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l11lll11l_opy_(message, True)
  atexit.unregister(bstack11l11111l_opy_)
  bstack1l1111llll_opy_()
  sys.exit(1)
def bstack11ll111ll_opy_():
  global CONFIG
  global bstack1lll1lll11_opy_
  global bstack11llllll1_opy_
  global bstack11ll1l1l1l_opy_
  CONFIG = bstack1111ll1l11_opy_()
  load_dotenv(CONFIG.get(bstack1lllll1l_opy_ (u"ࠩࡨࡲࡻࡌࡩ࡭ࡧࠪ௠")))
  bstack1ll11lll1_opy_()
  bstack11ll11lll_opy_()
  CONFIG = bstack11lllll11_opy_(CONFIG)
  update(CONFIG, bstack11llllll1_opy_)
  update(CONFIG, bstack1lll1lll11_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack11111l111_opy_(CONFIG)
  bstack11ll1l1l1l_opy_ = bstack111l1lll11_opy_(CONFIG)
  os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭௡")] = bstack11ll1l1l1l_opy_.__str__().lower()
  bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ௢"), bstack11ll1l1l1l_opy_)
  if (bstack1lllll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௣") in CONFIG and bstack1lllll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௤") in bstack1lll1lll11_opy_) or (
          bstack1lllll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ௥") in CONFIG and bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௦") not in bstack11llllll1_opy_):
    if os.getenv(bstack1lllll1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭௧")):
      CONFIG[bstack1lllll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ௨")] = os.getenv(bstack1lllll1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨ௩"))
    else:
      if not CONFIG.get(bstack1lllll1l_opy_ (u"ࠧ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠣ௪"), bstack1lllll1l_opy_ (u"ࠨࠢ௫")) in bstack11lll111ll_opy_:
        bstack1l11l1l11_opy_()
  elif (bstack1lllll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ௬") not in CONFIG and bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ௭") in CONFIG) or (
          bstack1lllll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௮") in bstack11llllll1_opy_ and bstack1lllll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௯") not in bstack1lll1lll11_opy_):
    del (CONFIG[bstack1lllll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௰")])
  if bstack11l11l11l_opy_(CONFIG):
    bstack1l11l1l11l_opy_(bstack1l111ll11l_opy_)
  Config.bstack1111l1ll_opy_().set_property(bstack1lllll1l_opy_ (u"ࠧࡻࡳࡦࡴࡑࡥࡲ࡫ࠢ௱"), CONFIG[bstack1lllll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ௲")])
  bstack11l1ll11ll_opy_()
  bstack11l11lllll_opy_()
  if bstack1l1111l11l_opy_ and not CONFIG.get(bstack1lllll1l_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠥ௳"), bstack1lllll1l_opy_ (u"ࠣࠤ௴")) in bstack11lll111ll_opy_:
    CONFIG[bstack1lllll1l_opy_ (u"ࠩࡤࡴࡵ࠭௵")] = bstack11l111l11_opy_(CONFIG)
    logger.info(bstack1ll11l11l1_opy_.format(CONFIG[bstack1lllll1l_opy_ (u"ࠪࡥࡵࡶࠧ௶")]))
  if not bstack11ll1l1l1l_opy_:
    CONFIG[bstack1lllll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ௷")] = [{}]
def bstack111111l1l1_opy_(config, bstack1l1l111l11_opy_):
  global CONFIG
  global bstack1l1111l11l_opy_
  CONFIG = config
  bstack1l1111l11l_opy_ = bstack1l1l111l11_opy_
def bstack11l11lllll_opy_():
  global CONFIG
  global bstack1l1111l11l_opy_
  if bstack1lllll1l_opy_ (u"ࠬࡧࡰࡱࠩ௸") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l1ll11ll1_opy_(e, bstack1llllllll1_opy_)
    bstack1l1111l11l_opy_ = True
    bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ௹"), True)
def bstack11l111l11_opy_(config):
  bstack11ll1lllll_opy_ = bstack1lllll1l_opy_ (u"ࠧࠨ௺")
  app = config[bstack1lllll1l_opy_ (u"ࠨࡣࡳࡴࠬ௻")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack11l11ll1ll_opy_:
      if os.path.exists(app):
        bstack11ll1lllll_opy_ = bstack11ll11ll11_opy_(config, app)
      elif bstack1lll111ll1_opy_(app):
        bstack11ll1lllll_opy_ = app
      else:
        bstack1l11l1l11l_opy_(bstack11l111l1l1_opy_.format(app))
    else:
      if bstack1lll111ll1_opy_(app):
        bstack11ll1lllll_opy_ = app
      elif os.path.exists(app):
        bstack11ll1lllll_opy_ = bstack11ll11ll11_opy_(app)
      else:
        bstack1l11l1l11l_opy_(bstack1l11ll1l1_opy_)
  else:
    if len(app) > 2:
      bstack1l11l1l11l_opy_(bstack11111ll1l_opy_)
    elif len(app) == 2:
      if bstack1lllll1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ௼") in app and bstack1lllll1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭௽") in app:
        if os.path.exists(app[bstack1lllll1l_opy_ (u"ࠫࡵࡧࡴࡩࠩ௾")]):
          bstack11ll1lllll_opy_ = bstack11ll11ll11_opy_(config, app[bstack1lllll1l_opy_ (u"ࠬࡶࡡࡵࡪࠪ௿")], app[bstack1lllll1l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩఀ")])
        else:
          bstack1l11l1l11l_opy_(bstack11l111l1l1_opy_.format(app))
      else:
        bstack1l11l1l11l_opy_(bstack11111ll1l_opy_)
    else:
      for key in app:
        if key in bstack111l1l1l11_opy_:
          if key == bstack1lllll1l_opy_ (u"ࠧࡱࡣࡷ࡬ࠬఁ"):
            if os.path.exists(app[key]):
              bstack11ll1lllll_opy_ = bstack11ll11ll11_opy_(config, app[key])
            else:
              bstack1l11l1l11l_opy_(bstack11l111l1l1_opy_.format(app))
          else:
            bstack11ll1lllll_opy_ = app[key]
        else:
          bstack1l11l1l11l_opy_(bstack11llll1l1l_opy_)
  return bstack11ll1lllll_opy_
def bstack1lll111ll1_opy_(bstack11ll1lllll_opy_):
  import re
  bstack111l11ll1l_opy_ = re.compile(bstack1lllll1l_opy_ (u"ࡳࠤࡡ࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰ࠤࠣం"))
  bstack1l1111ll1l_opy_ = re.compile(bstack1lllll1l_opy_ (u"ࡴࠥࡢࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪ࠰࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮ࠩࠨః"))
  if bstack1lllll1l_opy_ (u"ࠪࡦࡸࡀ࠯࠰ࠩఄ") in bstack11ll1lllll_opy_ or re.fullmatch(bstack111l11ll1l_opy_, bstack11ll1lllll_opy_) or re.fullmatch(bstack1l1111ll1l_opy_, bstack11ll1lllll_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack111l1llll1_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack11ll11ll11_opy_(config, path, bstack1l11l1l1ll_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1lllll1l_opy_ (u"ࠫࡷࡨࠧఅ")).read()).hexdigest()
  bstack11llll1ll1_opy_ = bstack11lll11lll_opy_(md5_hash)
  bstack11ll1lllll_opy_ = None
  if bstack11llll1ll1_opy_:
    logger.info(bstack1lllll111l_opy_.format(bstack11llll1ll1_opy_, md5_hash))
    return bstack11llll1ll1_opy_
  bstack1ll111ll1_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack1lllll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࠪఆ"): (os.path.basename(path), open(os.path.abspath(path), bstack1lllll1l_opy_ (u"࠭ࡲࡣࠩఇ")), bstack1lllll1l_opy_ (u"ࠧࡵࡧࡻࡸ࠴ࡶ࡬ࡢ࡫ࡱࠫఈ")),
      bstack1lllll1l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫఉ"): bstack1l11l1l1ll_opy_
    }
  )
  response = requests.post(bstack1111llll1l_opy_, data=multipart_data,
                           headers={bstack1lllll1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨఊ"): multipart_data.content_type},
                           auth=(config[bstack1lllll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬఋ")], config[bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧఌ")]))
  try:
    res = json.loads(response.text)
    bstack11ll1lllll_opy_ = res[bstack1lllll1l_opy_ (u"ࠬࡧࡰࡱࡡࡸࡶࡱ࠭఍")]
    logger.info(bstack1l1lll1ll_opy_.format(bstack11ll1lllll_opy_))
    bstack111111lll_opy_(md5_hash, bstack11ll1lllll_opy_)
    cli.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾ࡺࡶ࡬ࡰࡣࡧࡣࡦࡶࡰࠣఎ"), datetime.datetime.now() - bstack1ll111ll1_opy_)
  except ValueError as err:
    bstack1l11l1l11l_opy_(bstack1l1l11l11l_opy_.format(str(err)))
  return bstack11ll1lllll_opy_
def bstack11l1ll11ll_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1lll11ll1l_opy_
  bstack1lll1111l_opy_ = 1
  bstack1l111l1ll1_opy_ = 1
  if bstack1lllll1l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧఏ") in CONFIG:
    bstack1l111l1ll1_opy_ = CONFIG[bstack1lllll1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨఐ")]
  else:
    bstack1l111l1ll1_opy_ = bstack1l1ll1111_opy_(framework_name, args) or 1
  if bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ఑") in CONFIG:
    bstack1lll1111l_opy_ = len(CONFIG[bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ఒ")])
  bstack1lll11ll1l_opy_ = int(bstack1l111l1ll1_opy_) * int(bstack1lll1111l_opy_)
def bstack1l1ll1111_opy_(framework_name, args):
  if framework_name == bstack111llll11l_opy_ and args and bstack1lllll1l_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩఓ") in args:
      bstack1l111l1ll_opy_ = args.index(bstack1lllll1l_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪఔ"))
      return int(args[bstack1l111l1ll_opy_ + 1]) or 1
  return 1
def bstack11lll11lll_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lllll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩక"))
    bstack1l1111lll1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠧࡿࠩఖ")), bstack1lllll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨగ"), bstack1lllll1l_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪఘ"))
    if os.path.exists(bstack1l1111lll1_opy_):
      try:
        bstack11lll11l11_opy_ = json.load(open(bstack1l1111lll1_opy_, bstack1lllll1l_opy_ (u"ࠪࡶࡧ࠭ఙ")))
        if md5_hash in bstack11lll11l11_opy_:
          bstack1l1l111l1l_opy_ = bstack11lll11l11_opy_[md5_hash]
          bstack11lllllll_opy_ = datetime.datetime.now()
          bstack1ll11l111l_opy_ = datetime.datetime.strptime(bstack1l1l111l1l_opy_[bstack1lllll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧచ")], bstack1lllll1l_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩఛ"))
          if (bstack11lllllll_opy_ - bstack1ll11l111l_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack1l1l111l1l_opy_[bstack1lllll1l_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫజ")]):
            return None
          return bstack1l1l111l1l_opy_[bstack1lllll1l_opy_ (u"ࠧࡪࡦࠪఝ")]
      except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡏࡇ࠹ࠥ࡮ࡡࡴࡪࠣࡪ࡮ࡲࡥ࠻ࠢࡾࢁࠬఞ").format(str(e)))
    return None
  bstack1l1111lll1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠩࢁࠫట")), bstack1lllll1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪఠ"), bstack1lllll1l_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬడ"))
  lock_file = bstack1l1111lll1_opy_ + bstack1lllll1l_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫఢ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1l1111lll1_opy_):
        with open(bstack1l1111lll1_opy_, bstack1lllll1l_opy_ (u"࠭ࡲࠨణ")) as f:
          content = f.read().strip()
          if content:
            bstack11lll11l11_opy_ = json.loads(content)
            if md5_hash in bstack11lll11l11_opy_:
              bstack1l1l111l1l_opy_ = bstack11lll11l11_opy_[md5_hash]
              bstack11lllllll_opy_ = datetime.datetime.now()
              bstack1ll11l111l_opy_ = datetime.datetime.strptime(bstack1l1l111l1l_opy_[bstack1lllll1l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪత")], bstack1lllll1l_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬథ"))
              if (bstack11lllllll_opy_ - bstack1ll11l111l_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack1l1l111l1l_opy_[bstack1lllll1l_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧద")]):
                return None
              return bstack1l1l111l1l_opy_[bstack1lllll1l_opy_ (u"ࠪ࡭ࡩ࠭ధ")]
      return None
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡻ࡮ࡺࡨࠡࡨ࡬ࡰࡪࠦ࡬ࡰࡥ࡮࡭ࡳ࡭ࠠࡧࡱࡵࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࡀࠠࡼࡿࠪన").format(str(e)))
    return None
def bstack111111lll_opy_(md5_hash, bstack11ll1lllll_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lllll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨ఩"))
    bstack1l11l1ll11_opy_ = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"࠭ࡾࠨప")), bstack1lllll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧఫ"))
    if not os.path.exists(bstack1l11l1ll11_opy_):
      os.makedirs(bstack1l11l1ll11_opy_)
    bstack1l1111lll1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠨࢀࠪబ")), bstack1lllll1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩభ"), bstack1lllll1l_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫమ"))
    bstack1ll11111ll_opy_ = {
      bstack1lllll1l_opy_ (u"ࠫ࡮ࡪࠧయ"): bstack11ll1lllll_opy_,
      bstack1lllll1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨర"): datetime.datetime.strftime(datetime.datetime.now(), bstack1lllll1l_opy_ (u"࠭ࠥࡥ࠱ࠨࡱ࠴࡙ࠫࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪఱ")),
      bstack1lllll1l_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬల"): str(__version__)
    }
    try:
      bstack11lll11l11_opy_ = {}
      if os.path.exists(bstack1l1111lll1_opy_):
        bstack11lll11l11_opy_ = json.load(open(bstack1l1111lll1_opy_, bstack1lllll1l_opy_ (u"ࠨࡴࡥࠫళ")))
      bstack11lll11l11_opy_[md5_hash] = bstack1ll11111ll_opy_
      with open(bstack1l1111lll1_opy_, bstack1lllll1l_opy_ (u"ࠤࡺ࠯ࠧఴ")) as outfile:
        json.dump(bstack11lll11l11_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1lllll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡸࡴࡩࡧࡴࡪࡰࡪࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࠦࡦࡪ࡮ࡨ࠾ࠥࢁࡽࠨవ").format(str(e)))
    return
  bstack1l11l1ll11_opy_ = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠫࢃ࠭శ")), bstack1lllll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬష"))
  if not os.path.exists(bstack1l11l1ll11_opy_):
    os.makedirs(bstack1l11l1ll11_opy_)
  bstack1l1111lll1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"࠭ࡾࠨస")), bstack1lllll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧహ"), bstack1lllll1l_opy_ (u"ࠨࡣࡳࡴ࡚ࡶ࡬ࡰࡣࡧࡑࡉ࠻ࡈࡢࡵ࡫࠲࡯ࡹ࡯࡯ࠩ఺"))
  lock_file = bstack1l1111lll1_opy_ + bstack1lllll1l_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨ఻")
  bstack1ll11111ll_opy_ = {
    bstack1lllll1l_opy_ (u"ࠪ࡭ࡩ఼࠭"): bstack11ll1lllll_opy_,
    bstack1lllll1l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧఽ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1lllll1l_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩా")),
    bstack1lllll1l_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫి"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack11lll11l11_opy_ = {}
      if os.path.exists(bstack1l1111lll1_opy_):
        with open(bstack1l1111lll1_opy_, bstack1lllll1l_opy_ (u"ࠧࡳࠩీ")) as f:
          content = f.read().strip()
          if content:
            bstack11lll11l11_opy_ = json.loads(content)
      bstack11lll11l11_opy_[md5_hash] = bstack1ll11111ll_opy_
      with open(bstack1l1111lll1_opy_, bstack1lllll1l_opy_ (u"ࠣࡹࠥు")) as outfile:
        json.dump(bstack11lll11l11_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡹ࡬ࡸ࡭ࠦࡦࡪ࡮ࡨࠤࡱࡵࡣ࡬࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡐࡈ࠺ࠦࡨࡢࡵ࡫ࠤࡺࡶࡤࡢࡶࡨ࠾ࠥࢁࡽࠨూ").format(str(e)))
def bstack1ll1l1lll_opy_(self):
  return
def bstack11l1111ll_opy_(self):
  return
def bstack11llll11l_opy_():
  global bstack11ll1lll11_opy_
  bstack11ll1lll11_opy_ = True
@measure(event_name=EVENTS.bstack1l111lll1l_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1ll1ll1ll_opy_(self):
  global bstack1l11ll11l1_opy_
  global bstack11llll1lll_opy_
  global bstack1lll1l1lll_opy_
  try:
    if bstack1lllll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪృ") in bstack1l11ll11l1_opy_ and self.session_id != None and bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨౄ"), bstack1lllll1l_opy_ (u"ࠬ࠭౅")) != bstack1lllll1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧె"):
      bstack111ll1l1l_opy_ = bstack1lllll1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧే") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1lllll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨై")
      if bstack111ll1l1l_opy_ == bstack1lllll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ౉"):
        bstack111ll1lll_opy_(logger)
      if self != None:
        bstack1l1ll1l11_opy_(self, bstack111ll1l1l_opy_, bstack1lllll1l_opy_ (u"ࠪ࠰ࠥ࠭ొ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1lllll1l_opy_ (u"ࠫࠬో")
    if bstack1lllll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬౌ") in bstack1l11ll11l1_opy_ and getattr(threading.current_thread(), bstack1lllll1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱ్ࠬ"), None):
      bstack111ll11l_opy_.bstack111l111l_opy_(self, bstack1lll111111_opy_, logger, wait=True)
    if bstack1lllll1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ౎") in bstack1l11ll11l1_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1l1ll1l11_opy_(self, bstack1lllll1l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ౏"))
      bstack11llll1ll_opy_.bstack111l111111_opy_(self)
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࠥ౐") + str(e))
  bstack1lll1l1lll_opy_(self)
  self.session_id = None
def bstack1ll1ll111l_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack11ll1llll_opy_
    global bstack1l11ll11l1_opy_
    command_executor = kwargs.get(bstack1lllll1l_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷ࠭౑"), bstack1lllll1l_opy_ (u"ࠫࠬ౒"))
    bstack1l1lll1ll1_opy_ = False
    if type(command_executor) == str and bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨ౓") in command_executor:
      bstack1l1lll1ll1_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ౔") in str(getattr(command_executor, bstack1lllll1l_opy_ (u"ࠧࡠࡷࡵࡰౕࠬ"), bstack1lllll1l_opy_ (u"ࠨౖࠩ"))):
      bstack1l1lll1ll1_opy_ = True
    else:
      kwargs = bstack1111ll1l_opy_.bstack1l111ll1ll_opy_(bstack1ll11llll_opy_=kwargs, config=CONFIG)
      return bstack1l11ll1ll1_opy_(self, *args, **kwargs)
    if bstack1l1lll1ll1_opy_:
      bstack111l1lll1l_opy_ = bstack1l1ll11lll_opy_.bstack1l11111ll_opy_(CONFIG, bstack1l11ll11l1_opy_)
      if kwargs.get(bstack1lllll1l_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪ౗")):
        kwargs[bstack1lllll1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫౘ")] = bstack11ll1llll_opy_(kwargs[bstack1lllll1l_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬౙ")], bstack1l11ll11l1_opy_, CONFIG, bstack111l1lll1l_opy_)
      elif kwargs.get(bstack1lllll1l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬౚ")):
        kwargs[bstack1lllll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭౛")] = bstack11ll1llll_opy_(kwargs[bstack1lllll1l_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ౜")], bstack1l11ll11l1_opy_, CONFIG, bstack111l1lll1l_opy_)
  except Exception as e:
    logger.error(bstack1lllll1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪࡨࡲࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡖࡈࡐࠦࡣࡢࡲࡶ࠾ࠥࢁࡽࠣౝ").format(str(e)))
  return bstack1l11ll1ll1_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1lll11lll1_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1ll1111l11_opy_(self, command_executor=bstack1lllll1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱࠴࠶࠼࠴࠰࠯࠲࠱࠵࠿࠺࠴࠵࠶ࠥ౞"), *args, **kwargs):
  global bstack11llll1lll_opy_
  global bstack1111lll11l_opy_
  bstack111l1l1111_opy_ = bstack1ll1ll111l_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1ll11l1l_opy_.on():
    return bstack111l1l1111_opy_
  try:
    logger.debug(bstack1lllll1l_opy_ (u"ࠪࡇࡴࡳ࡭ࡢࡰࡧࠤࡊࡾࡥࡤࡷࡷࡳࡷࠦࡷࡩࡧࡱࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡪࡵࠣࡪࡦࡲࡳࡦࠢ࠰ࠤࢀࢃࠧ౟").format(str(command_executor)))
    logger.debug(bstack1lllll1l_opy_ (u"ࠫࡍࡻࡢࠡࡗࡕࡐࠥ࡯ࡳࠡ࠯ࠣࡿࢂ࠭ౠ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨౡ") in command_executor._url:
      bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧౢ"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪౣ") in command_executor):
    bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ౤"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack11l1lll1l1_opy_ = getattr(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪ౥"), None)
  bstack1lll11111l_opy_ = {}
  if self.capabilities is not None:
    bstack1lll11111l_opy_[bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩ౦")] = self.capabilities.get(bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ౧"))
    bstack1lll11111l_opy_[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ౨")] = self.capabilities.get(bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ౩"))
    bstack1lll11111l_opy_[bstack1lllll1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫࡟ࡰࡲࡷ࡭ࡴࡴࡳࠨ౪")] = self.capabilities.get(bstack1lllll1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭౫"))
  if CONFIG.get(bstack1lllll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ౬"), False) and bstack1111ll1l_opy_.bstack1ll11111l_opy_(bstack1lll11111l_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack1lllll1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ౭") in bstack1l11ll11l1_opy_ or bstack1lllll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ౮") in bstack1l11ll11l1_opy_:
    bstack1ll1l1l1_opy_.bstack1111ll11ll_opy_(self)
  if bstack1lllll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ౯") in bstack1l11ll11l1_opy_ and bstack11l1lll1l1_opy_ and bstack11l1lll1l1_opy_.get(bstack1lllll1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭౰"), bstack1lllll1l_opy_ (u"ࠧࠨ౱")) == bstack1lllll1l_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩ౲"):
    bstack1ll1l1l1_opy_.bstack1111ll11ll_opy_(self)
  bstack11llll1lll_opy_ = self.session_id
  with bstack1111l1l1l1_opy_:
    bstack1111lll11l_opy_.append(self)
  return bstack111l1l1111_opy_
def bstack11l1111l1_opy_(args):
  return bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴࠪ౳") in str(args)
def bstack11l1llll11_opy_(self, driver_command, *args, **kwargs):
  global bstack1l11l11ll_opy_
  global bstack1ll1ll1111_opy_
  bstack1ll1ll1l1_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ౴"), None) and bstack1l11l1l1_opy_(
          threading.current_thread(), bstack1lllll1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ౵"), None)
  bstack1ll1l1ll11_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ౶"), None) and bstack1l11l1l1_opy_(
          threading.current_thread(), bstack1lllll1l_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ౷"), None)
  bstack111lll1111_opy_ = getattr(self, bstack1lllll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ౸"), None) != None and getattr(self, bstack1lllll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ౹"), None) == True
  if not bstack1ll1ll1111_opy_ and bstack1lllll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ౺") in CONFIG and CONFIG[bstack1lllll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ౻")] == True and bstack11l11l11ll_opy_.bstack1l1lll1l1_opy_(driver_command) and (bstack111lll1111_opy_ or bstack1ll1ll1l1_opy_ or bstack1ll1l1ll11_opy_) and not bstack11l1111l1_opy_(args):
    try:
      bstack1ll1ll1111_opy_ = True
      logger.debug(bstack1lllll1l_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡿࢂ࠭౼").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1lllll1l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡶࡧࡦࡴࠠࡼࡿࠪ౽").format(str(err)))
    bstack1ll1ll1111_opy_ = False
  response = bstack1l11l11ll_opy_(self, driver_command, *args, **kwargs)
  if (bstack1lllll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ౾") in str(bstack1l11ll11l1_opy_).lower() or bstack1lllll1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ౿") in str(bstack1l11ll11l1_opy_).lower()) and bstack1ll11l1l_opy_.on():
    try:
      if driver_command == bstack1lllll1l_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬಀ"):
        bstack1ll1l1l1_opy_.bstack11111llll1_opy_({
            bstack1lllll1l_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨಁ"): response[bstack1lllll1l_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩಂ")],
            bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫಃ"): bstack1ll1l1l1_opy_.current_test_uuid() if bstack1ll1l1l1_opy_.current_test_uuid() else bstack1ll11l1l_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1l1l111ll_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack11l1l111ll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack11llll1lll_opy_
  global bstack11111ll1l1_opy_
  global bstack1l1ll1l1l1_opy_
  global bstack11l11l1ll1_opy_
  global bstack11lll1l111_opy_
  global bstack1l11ll11l1_opy_
  global bstack1l11ll1ll1_opy_
  global bstack1111lll11l_opy_
  global bstack1l1llll1l_opy_
  global bstack1lll111111_opy_
  if os.getenv(bstack1lllll1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ಄")) is not None and bstack1111ll1l_opy_.bstack111l1l11l_opy_(CONFIG) is None:
    CONFIG[bstack1lllll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ಅ")] = True
  CONFIG[bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩಆ")] = str(bstack1l11ll11l1_opy_) + str(__version__)
  bstack11l11111l1_opy_ = os.environ[bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ಇ")]
  bstack111l1lll1l_opy_ = bstack1l1ll11lll_opy_.bstack1l11111ll_opy_(CONFIG, bstack1l11ll11l1_opy_)
  CONFIG[bstack1lllll1l_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬಈ")] = bstack11l11111l1_opy_
  CONFIG[bstack1lllll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬಉ")] = bstack111l1lll1l_opy_
  if CONFIG.get(bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫಊ"),bstack1lllll1l_opy_ (u"ࠬ࠭ಋ")) and bstack1lllll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಌ") in bstack1l11ll11l1_opy_:
    CONFIG[bstack1lllll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ಍")].pop(bstack1lllll1l_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ಎ"), None)
    CONFIG[bstack1lllll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩಏ")].pop(bstack1lllll1l_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨಐ"), None)
  command_executor = bstack11l1l11lll_opy_()
  logger.debug(bstack11l1l1l1ll_opy_.format(command_executor))
  proxy = bstack1111111ll_opy_(CONFIG, proxy)
  bstack11ll1l1ll_opy_ = 0 if bstack11111ll1l1_opy_ < 0 else bstack11111ll1l1_opy_
  try:
    if bstack11l11l1ll1_opy_ is True:
      bstack11ll1l1ll_opy_ = int(multiprocessing.current_process().name)
    elif bstack11lll1l111_opy_ is True:
      bstack11ll1l1ll_opy_ = int(threading.current_thread().name)
  except:
    bstack11ll1l1ll_opy_ = 0
  bstack11111lllll_opy_ = bstack11111lll1_opy_(CONFIG, bstack11ll1l1ll_opy_)
  logger.debug(bstack11l1lll11l_opy_.format(str(bstack11111lllll_opy_)))
  if bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ಑") in CONFIG and bstack1111l11l1l_opy_(CONFIG[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩಒ")]):
    bstack1llll1l1l1_opy_(bstack11111lllll_opy_)
  if bstack1111ll1l_opy_.bstack1l1lll1l1l_opy_(CONFIG, bstack11ll1l1ll_opy_) and bstack1111ll1l_opy_.bstack1l1l1l1ll_opy_(bstack11111lllll_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack1111ll1l_opy_.set_capabilities(bstack11111lllll_opy_, CONFIG)
  if desired_capabilities:
    bstack1l11ll11ll_opy_ = bstack11lllll11_opy_(desired_capabilities)
    bstack1l11ll11ll_opy_[bstack1lllll1l_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ಓ")] = bstack111ll1l11_opy_(CONFIG)
    bstack11l1l1l1l1_opy_ = bstack11111lll1_opy_(bstack1l11ll11ll_opy_)
    if bstack11l1l1l1l1_opy_:
      bstack11111lllll_opy_ = update(bstack11l1l1l1l1_opy_, bstack11111lllll_opy_)
    desired_capabilities = None
  if options:
    bstack1lll11l1l1_opy_(options, bstack11111lllll_opy_)
  if not options:
    options = bstack1l1l11l111_opy_(bstack11111lllll_opy_)
  bstack1lll111111_opy_ = CONFIG.get(bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಔ"))[bstack11ll1l1ll_opy_]
  if proxy and bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨಕ")):
    options.proxy(proxy)
  if options and bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨಖ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1l111llll1_opy_() < version.parse(bstack1lllll1l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩಗ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack11111lllll_opy_)
  logger.info(bstack1111l11l1_opy_)
  bstack111l1111l_opy_.end(EVENTS.bstack1l111llll_opy_.value, EVENTS.bstack1l111llll_opy_.value + bstack1lllll1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦಘ"), EVENTS.bstack1l111llll_opy_.value + bstack1lllll1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥಙ"), status=True, failure=None, test_name=bstack1l1ll1l1l1_opy_)
  if bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡱࡴࡲࡪ࡮ࡲࡥࠨಚ") in kwargs:
    del kwargs[bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡲࡵࡳ࡫࡯࡬ࡦࠩಛ")]
  try:
    if bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨಜ")):
      bstack1l11ll1ll1_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨಝ")):
      bstack1l11ll1ll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠪ࠶࠳࠻࠳࠯࠲ࠪಞ")):
      bstack1l11ll1ll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1l11ll1ll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack1l1111111l_opy_:
    logger.error(bstack11lll1ll1_opy_.format(bstack1lllll1l_opy_ (u"ࠫࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠪಟ"), str(bstack1l1111111l_opy_)))
    raise bstack1l1111111l_opy_
  if bstack1111ll1l_opy_.bstack1l1lll1l1l_opy_(CONFIG, bstack11ll1l1ll_opy_) and bstack1111ll1l_opy_.bstack1l1l1l1ll_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack1lllll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧಠ")][bstack1lllll1l_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬಡ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack1111ll1l_opy_.set_capabilities(bstack11111lllll_opy_, CONFIG)
  try:
    bstack1llll11l1l_opy_ = bstack1lllll1l_opy_ (u"ࠧࠨಢ")
    if bstack1l111llll1_opy_() >= version.parse(bstack1lllll1l_opy_ (u"ࠨ࠶࠱࠴࠳࠶ࡢ࠲ࠩಣ")):
      if self.caps is not None:
        bstack1llll11l1l_opy_ = self.caps.get(bstack1lllll1l_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤತ"))
    else:
      if self.capabilities is not None:
        bstack1llll11l1l_opy_ = self.capabilities.get(bstack1lllll1l_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥಥ"))
    if bstack1llll11l1l_opy_:
      bstack1l11ll111l_opy_(bstack1llll11l1l_opy_)
      if bstack1l111llll1_opy_() <= version.parse(bstack1lllll1l_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫದ")):
        self.command_executor._url = bstack1lllll1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨಧ") + bstack11lll1111_opy_ + bstack1lllll1l_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥನ")
      else:
        self.command_executor._url = bstack1lllll1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤ಩") + bstack1llll11l1l_opy_ + bstack1lllll1l_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤಪ")
      logger.debug(bstack111l111l1_opy_.format(bstack1llll11l1l_opy_))
    else:
      logger.debug(bstack1ll11ll11l_opy_.format(bstack1lllll1l_opy_ (u"ࠤࡒࡴࡹ࡯࡭ࡢ࡮ࠣࡌࡺࡨࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠥಫ")))
  except Exception as e:
    logger.debug(bstack1ll11ll11l_opy_.format(e))
  if bstack1lllll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩಬ") in bstack1l11ll11l1_opy_:
    bstack111111111_opy_(bstack11111ll1l1_opy_, bstack1l1llll1l_opy_)
  bstack11llll1lll_opy_ = self.session_id
  if bstack1lllll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫಭ") in bstack1l11ll11l1_opy_ or bstack1lllll1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬಮ") in bstack1l11ll11l1_opy_ or bstack1lllll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಯ") in bstack1l11ll11l1_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack11l1lll1l1_opy_ = getattr(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡔࡦࡵࡷࡑࡪࡺࡡࠨರ"), None)
  if bstack1lllll1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨಱ") in bstack1l11ll11l1_opy_ or bstack1lllll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨಲ") in bstack1l11ll11l1_opy_:
    bstack1ll1l1l1_opy_.bstack1111ll11ll_opy_(self)
  if bstack1lllll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪಳ") in bstack1l11ll11l1_opy_ and bstack11l1lll1l1_opy_ and bstack11l1lll1l1_opy_.get(bstack1lllll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ಴"), bstack1lllll1l_opy_ (u"ࠬ࠭ವ")) == bstack1lllll1l_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧಶ"):
    bstack1ll1l1l1_opy_.bstack1111ll11ll_opy_(self)
  with bstack1111l1l1l1_opy_:
    bstack1111lll11l_opy_.append(self)
  if bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಷ") in CONFIG and bstack1lllll1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ಸ") in CONFIG[bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಹ")][bstack11ll1l1ll_opy_]:
    bstack1l1ll1l1l1_opy_ = CONFIG[bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭಺")][bstack11ll1l1ll_opy_][bstack1lllll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ಻")]
  logger.debug(bstack111l1l1ll1_opy_.format(bstack11llll1lll_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1l1ll1lll1_opy_
    def bstack1ll1ll1lll_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1l11l11l1l_opy_
      if(bstack1lllll1l_opy_ (u"ࠧ࡯࡮ࡥࡧࡻ࠲࡯ࡹ಼ࠢ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"࠭ࡾࠨಽ")), bstack1lllll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧಾ"), bstack1lllll1l_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪಿ")), bstack1lllll1l_opy_ (u"ࠩࡺࠫೀ")) as fp:
          fp.write(bstack1lllll1l_opy_ (u"ࠥࠦು"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1lllll1l_opy_ (u"ࠦ࡮ࡴࡤࡦࡺࡢࡦࡸࡺࡡࡤ࡭࠱࡮ࡸࠨೂ")))):
          with open(args[1], bstack1lllll1l_opy_ (u"ࠬࡸࠧೃ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1lllll1l_opy_ (u"࠭ࡡࡴࡻࡱࡧࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡠࡰࡨࡻࡕࡧࡧࡦࠪࡦࡳࡳࡺࡥࡹࡶ࠯ࠤࡵࡧࡧࡦࠢࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠬೄ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1l1111l1ll_opy_)
            if bstack1lllll1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ೅") in CONFIG and str(CONFIG[bstack1lllll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬೆ")]).lower() != bstack1lllll1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨೇ"):
                bstack1l111ll111_opy_ = bstack1l1ll1lll1_opy_()
                bstack1llll1ll1l_opy_ = bstack1lllll1l_opy_ (u"ࠪࠫࠬࠐ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠌࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭ࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࡠ࠿ࠏࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠶ࡣ࠻ࠋࡥࡲࡲࡸࡺࠠࡱࡡ࡬ࡲࡩ࡫ࡸࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠶ࡢࡁࠊࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮ࡴ࡮࡬ࡧࡪ࠮࠰࠭ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷࠮ࡁࠊࡤࡱࡱࡷࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮ࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ࠯࠻ࠋ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰ࠴ࡣࡩࡴࡲࡱ࡮ࡻ࡭࠯࡮ࡤࡹࡳࡩࡨࠡ࠿ࠣࡥࡸࡿ࡮ࡤࠢࠫࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵࠬࠤࡂࡄࠠࡼࡽࠍࠤࠥࡲࡥࡵࠢࡦࡥࡵࡹ࠻ࠋࠢࠣࡸࡷࡿࠠࡼࡽࠍࠤࠥࠦࠠࡤࡣࡳࡷࠥࡃࠠࡋࡕࡒࡒ࠳ࡶࡡࡳࡵࡨࠬࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠫ࠾ࠎࠥࠦࡽࡾࠢࡦࡥࡹࡩࡨࠡࠪࡨࡼ࠮ࠦࡻࡼࠌࠣࠤࠥࠦࡣࡰࡰࡶࡳࡱ࡫࠮ࡦࡴࡵࡳࡷ࠮ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳ࠻ࠤ࠯ࠤࡪࡾࠩ࠼ࠌࠣࠤࢂࢃࠊࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡤࡻࡦ࡯ࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰ࠴ࡣࡩࡴࡲࡱ࡮ࡻ࡭࠯ࡥࡲࡲࡳ࡫ࡣࡵࠪࡾࡿࠏࠦࠠࠡࠢࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹࡀࠠࠨࡽࡦࡨࡵ࡛ࡲ࡭ࡿࠪࠤ࠰ࠦࡥ࡯ࡥࡲࡨࡪ࡛ࡒࡊࡅࡲࡱࡵࡵ࡮ࡦࡰࡷࠬࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡩࡡࡱࡵࠬ࠭࠱ࠐࠠࠡࠢࠣ࠲࠳࠴࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸࠐࠠࠡࡿࢀ࠭ࡀࠐࡽࡾ࠽ࠍ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࠐࠧࠨࠩೈ").format(bstack1l111ll111_opy_=bstack1l111ll111_opy_)
            lines.insert(1, bstack1llll1ll1l_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1lllll1l_opy_ (u"ࠦ࡮ࡴࡤࡦࡺࡢࡦࡸࡺࡡࡤ࡭࠱࡮ࡸࠨ೉")), bstack1lllll1l_opy_ (u"ࠬࡽࠧೊ")) as bstack1l1111l1l_opy_:
              bstack1l1111l1l_opy_.writelines(lines)
        CONFIG[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨೋ")] = str(bstack1l11ll11l1_opy_) + str(__version__)
        bstack11l11111l1_opy_ = os.environ[bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬೌ")]
        bstack111l1lll1l_opy_ = bstack1l1ll11lll_opy_.bstack1l11111ll_opy_(CONFIG, bstack1l11ll11l1_opy_)
        CONFIG[bstack1lllll1l_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧ್ࠫ")] = bstack11l11111l1_opy_
        CONFIG[bstack1lllll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫ೎")] = bstack111l1lll1l_opy_
        bstack11ll1l1ll_opy_ = 0 if bstack11111ll1l1_opy_ < 0 else bstack11111ll1l1_opy_
        try:
          if bstack11l11l1ll1_opy_ is True:
            bstack11ll1l1ll_opy_ = int(multiprocessing.current_process().name)
          elif bstack11lll1l111_opy_ is True:
            bstack11ll1l1ll_opy_ = int(threading.current_thread().name)
        except:
          bstack11ll1l1ll_opy_ = 0
        CONFIG[bstack1lllll1l_opy_ (u"ࠥࡹࡸ࡫ࡗ࠴ࡅࠥ೏")] = False
        CONFIG[bstack1lllll1l_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ೐")] = True
        bstack11111lllll_opy_ = bstack11111lll1_opy_(CONFIG, bstack11ll1l1ll_opy_)
        logger.debug(bstack11l1lll11l_opy_.format(str(bstack11111lllll_opy_)))
        if CONFIG.get(bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ೑")):
          bstack1llll1l1l1_opy_(bstack11111lllll_opy_)
        if bstack1lllll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ೒") in CONFIG and bstack1lllll1l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ೓") in CONFIG[bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ೔")][bstack11ll1l1ll_opy_]:
          bstack1l1ll1l1l1_opy_ = CONFIG[bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೕ")][bstack11ll1l1ll_opy_][bstack1lllll1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨೖ")]
        args.append(os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠫࢃ࠭೗")), bstack1lllll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ೘"), bstack1lllll1l_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨ೙")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack11111lllll_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1lllll1l_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤ೚"))
      bstack1l11l11l1l_opy_ = True
      return bstack11l11l1lll_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack1l11llll1l_opy_(self,
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
    global bstack11111ll1l1_opy_
    global bstack1l1ll1l1l1_opy_
    global bstack11l11l1ll1_opy_
    global bstack11lll1l111_opy_
    global bstack1l11ll11l1_opy_
    CONFIG[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪ೛")] = str(bstack1l11ll11l1_opy_) + str(__version__)
    bstack11l11111l1_opy_ = os.environ[bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ೜")]
    bstack111l1lll1l_opy_ = bstack1l1ll11lll_opy_.bstack1l11111ll_opy_(CONFIG, bstack1l11ll11l1_opy_)
    CONFIG[bstack1lllll1l_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ೝ")] = bstack11l11111l1_opy_
    CONFIG[bstack1lllll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ೞ")] = bstack111l1lll1l_opy_
    bstack11ll1l1ll_opy_ = 0 if bstack11111ll1l1_opy_ < 0 else bstack11111ll1l1_opy_
    try:
      if bstack11l11l1ll1_opy_ is True:
        bstack11ll1l1ll_opy_ = int(multiprocessing.current_process().name)
      elif bstack11lll1l111_opy_ is True:
        bstack11ll1l1ll_opy_ = int(threading.current_thread().name)
    except:
      bstack11ll1l1ll_opy_ = 0
    CONFIG[bstack1lllll1l_opy_ (u"ࠧ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ೟")] = True
    bstack11111lllll_opy_ = bstack11111lll1_opy_(CONFIG, bstack11ll1l1ll_opy_)
    logger.debug(bstack11l1lll11l_opy_.format(str(bstack11111lllll_opy_)))
    if CONFIG.get(bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪೠ")):
      bstack1llll1l1l1_opy_(bstack11111lllll_opy_)
    if bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪೡ") in CONFIG and bstack1lllll1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ೢ") in CONFIG[bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೣ")][bstack11ll1l1ll_opy_]:
      bstack1l1ll1l1l1_opy_ = CONFIG[bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭೤")][bstack11ll1l1ll_opy_][bstack1lllll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ೥")]
    import urllib
    import json
    if bstack1lllll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ೦") in CONFIG and str(CONFIG[bstack1lllll1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ೧")]).lower() != bstack1lllll1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭೨"):
        bstack11ll11l11l_opy_ = bstack1l1ll1lll1_opy_()
        bstack1l111ll111_opy_ = bstack11ll11l11l_opy_ + urllib.parse.quote(json.dumps(bstack11111lllll_opy_))
    else:
        bstack1l111ll111_opy_ = bstack1lllll1l_opy_ (u"ࠨࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠪ೩") + urllib.parse.quote(json.dumps(bstack11111lllll_opy_))
    browser = self.connect(bstack1l111ll111_opy_)
    return browser
except Exception as e:
    pass
def bstack1l1111ll11_opy_():
    global bstack1l11l11l1l_opy_
    global bstack1l11ll11l1_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack111l111ll_opy_
        global bstack1lll1ll1l_opy_
        if not bstack11ll1l1l1l_opy_:
          global bstack111llllll1_opy_
          if not bstack111llllll1_opy_:
            from bstack_utils.helper import bstack1ll11l1ll_opy_, bstack11ll1ll111_opy_, bstack1l1llllll1_opy_
            bstack111llllll1_opy_ = bstack1ll11l1ll_opy_()
            bstack11ll1ll111_opy_(bstack1l11ll11l1_opy_)
            bstack111l1lll1l_opy_ = bstack1l1ll11lll_opy_.bstack1l11111ll_opy_(CONFIG, bstack1l11ll11l1_opy_)
            bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"ࠤࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡐࡓࡑࡇ࡙ࡈ࡚࡟ࡎࡃࡓࠦ೪"), bstack111l1lll1l_opy_)
          BrowserType.connect = bstack111l111ll_opy_
          return
        BrowserType.launch = bstack1l11llll1l_opy_
        bstack1l11l11l1l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1ll1ll1lll_opy_
      bstack1l11l11l1l_opy_ = True
    except Exception as e:
      pass
def bstack111111l1l_opy_(context, bstack1ll11l1l1l_opy_):
  try:
    context.page.evaluate(bstack1lllll1l_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ೫"), bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨ೬")+ json.dumps(bstack1ll11l1l1l_opy_) + bstack1lllll1l_opy_ (u"ࠧࢃࡽࠣ೭"))
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀ࠾ࠥࢁࡽࠣ೮").format(str(e), traceback.format_exc()))
def bstack1l111lll1_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1lllll1l_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ೯"), bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭೰") + json.dumps(message) + bstack1lllll1l_opy_ (u"ࠩ࠯ࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠬೱ") + json.dumps(level) + bstack1lllll1l_opy_ (u"ࠪࢁࢂ࠭ೲ"))
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࢀࢃ࠺ࠡࡽࢀࠦೳ").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack11lll1l1l_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1l1111111_opy_(self, url):
  global bstack1ll1ll1l11_opy_
  try:
    bstack1l11l1111_opy_(url)
  except Exception as err:
    logger.debug(bstack111lll1ll1_opy_.format(str(err)))
  try:
    bstack1ll1ll1l11_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack11ll11l1l1_opy_):
        bstack1l11l1111_opy_(url, True)
    except Exception as err:
      logger.debug(bstack111lll1ll1_opy_.format(str(err)))
    raise e
def bstack11ll1111l_opy_(self):
  global bstack11ll111l11_opy_
  bstack11ll111l11_opy_ = self
  return
def bstack111l1111l1_opy_(self):
  global bstack11ll1l1l11_opy_
  bstack11ll1l1l11_opy_ = self
  return
def bstack1l1l1l111l_opy_(test_name, bstack1l1l11l1l_opy_):
  global CONFIG
  if percy.bstack1lllll11l1_opy_() == bstack1lllll1l_opy_ (u"ࠧࡺࡲࡶࡧࠥ೴"):
    bstack1111lll11_opy_ = os.path.relpath(bstack1l1l11l1l_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1111lll11_opy_)
    bstack11lll11l1l_opy_ = suite_name + bstack1lllll1l_opy_ (u"ࠨ࠭ࠣ೵") + test_name
    threading.current_thread().percySessionName = bstack11lll11l1l_opy_
def bstack1ll1l11l1_opy_(self, test, *args, **kwargs):
  global bstack1ll1111l1l_opy_
  test_name = None
  bstack1l1l11l1l_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1l1l11l1l_opy_ = str(test.source)
  bstack1l1l1l111l_opy_(test_name, bstack1l1l11l1l_opy_)
  bstack1ll1111l1l_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l11l1l1l_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack111l1l11ll_opy_(driver, bstack11lll11l1l_opy_):
  if not bstack1l1l1l1l1l_opy_ and bstack11lll11l1l_opy_:
      bstack11ll11111_opy_ = {
          bstack1lllll1l_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ೶"): bstack1lllll1l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ೷"),
          bstack1lllll1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ೸"): {
              bstack1lllll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ೹"): bstack11lll11l1l_opy_
          }
      }
      bstack1l1l11ll11_opy_ = bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ೺").format(json.dumps(bstack11ll11111_opy_))
      driver.execute_script(bstack1l1l11ll11_opy_)
  if bstack11ll1l1l1_opy_:
      bstack1lll1l1l1l_opy_ = {
          bstack1lllll1l_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬ೻"): bstack1lllll1l_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ೼"),
          bstack1lllll1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ೽"): {
              bstack1lllll1l_opy_ (u"ࠨࡦࡤࡸࡦ࠭೾"): bstack11lll11l1l_opy_ + bstack1lllll1l_opy_ (u"ࠩࠣࡴࡦࡹࡳࡦࡦࠤࠫ೿"),
              bstack1lllll1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩഀ"): bstack1lllll1l_opy_ (u"ࠫ࡮ࡴࡦࡰࠩഁ")
          }
      }
      if bstack11ll1l1l1_opy_.status == bstack1lllll1l_opy_ (u"ࠬࡖࡁࡔࡕࠪം"):
          bstack1llll11111_opy_ = bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫഃ").format(json.dumps(bstack1lll1l1l1l_opy_))
          driver.execute_script(bstack1llll11111_opy_)
          bstack1l1ll1l11_opy_(driver, bstack1lllll1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧഄ"))
      elif bstack11ll1l1l1_opy_.status == bstack1lllll1l_opy_ (u"ࠨࡈࡄࡍࡑ࠭അ"):
          reason = bstack1lllll1l_opy_ (u"ࠤࠥആ")
          bstack111l1ll11l_opy_ = bstack11lll11l1l_opy_ + bstack1lllll1l_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠫഇ")
          if bstack11ll1l1l1_opy_.message:
              reason = str(bstack11ll1l1l1_opy_.message)
              bstack111l1ll11l_opy_ = bstack111l1ll11l_opy_ + bstack1lllll1l_opy_ (u"ࠫࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠫഈ") + reason
          bstack1lll1l1l1l_opy_[bstack1lllll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨഉ")] = {
              bstack1lllll1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬഊ"): bstack1lllll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ഋ"),
              bstack1lllll1l_opy_ (u"ࠨࡦࡤࡸࡦ࠭ഌ"): bstack111l1ll11l_opy_
          }
          bstack1llll11111_opy_ = bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧ഍").format(json.dumps(bstack1lll1l1l1l_opy_))
          driver.execute_script(bstack1llll11111_opy_)
          bstack1l1ll1l11_opy_(driver, bstack1lllll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪഎ"), reason)
          bstack1l1l11lll_opy_(reason, str(bstack11ll1l1l1_opy_), str(bstack11111ll1l1_opy_), logger)
@measure(event_name=EVENTS.bstack1l1l1lllll_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1llll1llll_opy_(driver, test):
  if percy.bstack1lllll11l1_opy_() == bstack1lllll1l_opy_ (u"ࠦࡹࡸࡵࡦࠤഏ") and percy.bstack1ll11l111_opy_() == bstack1lllll1l_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢഐ"):
      bstack1l1ll1ll1_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ഑"), None)
      bstack1ll11l1l11_opy_(driver, bstack1l1ll1ll1_opy_, test)
  if (bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫഒ"), None) and
      bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧഓ"), None)) or (
      bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩഔ"), None) and
      bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬക"), None)):
      logger.info(bstack1lllll1l_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠢࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡮ࡹࠠࡶࡰࡧࡩࡷࡽࡡࡺ࠰ࠣࠦഖ"))
      bstack1111ll1l_opy_.bstack1lllll11l_opy_(driver, name=test.name, path=test.source)
def bstack1l11lll1l_opy_(test, bstack11lll11l1l_opy_):
    try:
      bstack1ll111ll1_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack1lllll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪഗ")] = bstack11lll11l1l_opy_
      if bstack11ll1l1l1_opy_:
        if bstack11ll1l1l1_opy_.status == bstack1lllll1l_opy_ (u"࠭ࡐࡂࡕࡖࠫഘ"):
          data[bstack1lllll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧങ")] = bstack1lllll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨച")
        elif bstack11ll1l1l1_opy_.status == bstack1lllll1l_opy_ (u"ࠩࡉࡅࡎࡒࠧഛ"):
          data[bstack1lllll1l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪജ")] = bstack1lllll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫഝ")
          if bstack11ll1l1l1_opy_.message:
            data[bstack1lllll1l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬഞ")] = str(bstack11ll1l1l1_opy_.message)
      user = CONFIG[bstack1lllll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨട")]
      key = CONFIG[bstack1lllll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪഠ")]
      host = bstack11l111l1ll_opy_(cli.config, [bstack1lllll1l_opy_ (u"ࠣࡣࡳ࡭ࡸࠨഡ"), bstack1lllll1l_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦഢ"), bstack1lllll1l_opy_ (u"ࠥࡥࡵ࡯ࠢണ")], bstack1lllll1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠧത"))
      url = bstack1lllll1l_opy_ (u"ࠬࢁࡽ࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠴ࢁࡽ࠯࡬ࡶࡳࡳ࠭ഥ").format(host, bstack11llll1lll_opy_)
      headers = {
        bstack1lllll1l_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬദ"): bstack1lllll1l_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪധ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠣࡪࡷࡸࡵࡀࡵࡱࡦࡤࡸࡪࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡴࡢࡶࡸࡷࠧന"), datetime.datetime.now() - bstack1ll111ll1_opy_)
    except Exception as e:
      logger.error(bstack111ll1l1ll_opy_.format(str(e)))
def bstack1l11lll1l1_opy_(test, bstack11lll11l1l_opy_):
  global CONFIG
  global bstack11ll1l1l11_opy_
  global bstack11ll111l11_opy_
  global bstack11llll1lll_opy_
  global bstack11ll1l1l1_opy_
  global bstack1l1ll1l1l1_opy_
  global bstack1l1l1lll1_opy_
  global bstack11l11llll_opy_
  global bstack11ll111l1l_opy_
  global bstack1l111l1l11_opy_
  global bstack1111lll11l_opy_
  global bstack1lll111111_opy_
  global bstack1ll1llll11_opy_
  try:
    if not bstack11llll1lll_opy_:
      with bstack1ll1llll11_opy_:
        bstack1111l111l_opy_ = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠩࢁࠫഩ")), bstack1lllll1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪപ"), bstack1lllll1l_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭ഫ"))
        if os.path.exists(bstack1111l111l_opy_):
          with open(bstack1111l111l_opy_, bstack1lllll1l_opy_ (u"ࠬࡸࠧബ")) as f:
            content = f.read().strip()
            if content:
              bstack11ll1ll11l_opy_ = json.loads(bstack1lllll1l_opy_ (u"ࠨࡻࠣഭ") + content + bstack1lllll1l_opy_ (u"ࠧࠣࡺࠥ࠾ࠥࠨࡹࠣࠩമ") + bstack1lllll1l_opy_ (u"ࠣࡿࠥയ"))
              bstack11llll1lll_opy_ = bstack11ll1ll11l_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡍࡉࡹࠠࡧ࡫࡯ࡩ࠿ࠦࠧര") + str(e))
  if bstack1111lll11l_opy_:
    with bstack1111l1l1l1_opy_:
      bstack1111l1lll1_opy_ = bstack1111lll11l_opy_.copy()
    for driver in bstack1111l1lll1_opy_:
      if bstack11llll1lll_opy_ == driver.session_id:
        if test:
          bstack1llll1llll_opy_(driver, test)
        bstack111l1l11ll_opy_(driver, bstack11lll11l1l_opy_)
  elif bstack11llll1lll_opy_:
    bstack1l11lll1l_opy_(test, bstack11lll11l1l_opy_)
  if bstack11ll1l1l11_opy_:
    bstack11l11llll_opy_(bstack11ll1l1l11_opy_)
  if bstack11ll111l11_opy_:
    bstack11ll111l1l_opy_(bstack11ll111l11_opy_)
  if bstack11ll1lll11_opy_:
    bstack1l111l1l11_opy_()
def bstack1l1lll1lll_opy_(self, test, *args, **kwargs):
  bstack11lll11l1l_opy_ = None
  if test:
    bstack11lll11l1l_opy_ = str(test.name)
  bstack1l11lll1l1_opy_(test, bstack11lll11l1l_opy_)
  bstack1l1l1lll1_opy_(self, test, *args, **kwargs)
def bstack11l1llll1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11l1l1llll_opy_
  global CONFIG
  global bstack1111lll11l_opy_
  global bstack11llll1lll_opy_
  global bstack1ll1llll11_opy_
  bstack1ll111l1l_opy_ = None
  try:
    if bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩറ"), None) or bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ല"), None):
      try:
        if not bstack11llll1lll_opy_:
          bstack1111l111l_opy_ = os.path.join(os.path.expanduser(bstack1lllll1l_opy_ (u"ࠬࢄࠧള")), bstack1lllll1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ഴ"), bstack1lllll1l_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩവ"))
          with bstack1ll1llll11_opy_:
            if os.path.exists(bstack1111l111l_opy_):
              with open(bstack1111l111l_opy_, bstack1lllll1l_opy_ (u"ࠨࡴࠪശ")) as f:
                content = f.read().strip()
                if content:
                  bstack11ll1ll11l_opy_ = json.loads(bstack1lllll1l_opy_ (u"ࠤࡾࠦഷ") + content + bstack1lllll1l_opy_ (u"ࠪࠦࡽࠨ࠺ࠡࠤࡼࠦࠬസ") + bstack1lllll1l_opy_ (u"ࠦࢂࠨഹ"))
                  bstack11llll1lll_opy_ = bstack11ll1ll11l_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࡵࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࠫഺ") + str(e))
      if bstack1111lll11l_opy_:
        with bstack1111l1l1l1_opy_:
          bstack1111l1lll1_opy_ = bstack1111lll11l_opy_.copy()
        for driver in bstack1111l1lll1_opy_:
          if bstack11llll1lll_opy_ == driver.session_id:
            bstack1ll111l1l_opy_ = driver
    bstack111l11111l_opy_ = bstack1111ll1l_opy_.bstack1ll1l11ll_opy_(test.tags)
    if bstack1ll111l1l_opy_:
      threading.current_thread().isA11yTest = bstack1111ll1l_opy_.bstack1ll1lll1l_opy_(bstack1ll111l1l_opy_, bstack111l11111l_opy_)
      threading.current_thread().isAppA11yTest = bstack1111ll1l_opy_.bstack1ll1lll1l_opy_(bstack1ll111l1l_opy_, bstack111l11111l_opy_)
    else:
      threading.current_thread().isA11yTest = bstack111l11111l_opy_
      threading.current_thread().isAppA11yTest = bstack111l11111l_opy_
  except:
    pass
  bstack11l1l1llll_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack11ll1l1l1_opy_
  try:
    bstack11ll1l1l1_opy_ = self._test
  except:
    bstack11ll1l1l1_opy_ = self.test
def bstack1l111l11l1_opy_():
  global bstack11ll111l1_opy_
  try:
    if os.path.exists(bstack11ll111l1_opy_):
      os.remove(bstack11ll111l1_opy_)
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺഻ࠡࠩ") + str(e))
def bstack1l1ll1l1l_opy_():
  global bstack11ll111l1_opy_
  bstack1lll1l11ll_opy_ = {}
  lock_file = bstack11ll111l1_opy_ + bstack1lllll1l_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ഼࠭")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lllll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫഽ"))
    try:
      if not os.path.isfile(bstack11ll111l1_opy_):
        with open(bstack11ll111l1_opy_, bstack1lllll1l_opy_ (u"ࠩࡺࠫാ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack11ll111l1_opy_):
        with open(bstack11ll111l1_opy_, bstack1lllll1l_opy_ (u"ࠪࡶࠬി")) as f:
          content = f.read().strip()
          if content:
            bstack1lll1l11ll_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack1lllll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ീ") + str(e))
    return bstack1lll1l11ll_opy_
  try:
    os.makedirs(os.path.dirname(bstack11ll111l1_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack11ll111l1_opy_):
        with open(bstack11ll111l1_opy_, bstack1lllll1l_opy_ (u"ࠬࡽࠧു")) as f:
          json.dump({}, f)
      if os.path.exists(bstack11ll111l1_opy_):
        with open(bstack11ll111l1_opy_, bstack1lllll1l_opy_ (u"࠭ࡲࠨൂ")) as f:
          content = f.read().strip()
          if content:
            bstack1lll1l11ll_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩൃ") + str(e))
  finally:
    return bstack1lll1l11ll_opy_
def bstack111111111_opy_(platform_index, item_index):
  global bstack11ll111l1_opy_
  lock_file = bstack11ll111l1_opy_ + bstack1lllll1l_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧൄ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lllll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬ൅"))
    try:
      bstack1lll1l11ll_opy_ = {}
      if os.path.exists(bstack11ll111l1_opy_):
        with open(bstack11ll111l1_opy_, bstack1lllll1l_opy_ (u"ࠪࡶࠬെ")) as f:
          content = f.read().strip()
          if content:
            bstack1lll1l11ll_opy_ = json.loads(content)
      bstack1lll1l11ll_opy_[item_index] = platform_index
      with open(bstack11ll111l1_opy_, bstack1lllll1l_opy_ (u"ࠦࡼࠨേ")) as outfile:
        json.dump(bstack1lll1l11ll_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1lllll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡸࡴ࡬ࡸ࡮ࡴࡧࠡࡶࡲࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪൈ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack11ll111l1_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack1lll1l11ll_opy_ = {}
      if os.path.exists(bstack11ll111l1_opy_):
        with open(bstack11ll111l1_opy_, bstack1lllll1l_opy_ (u"࠭ࡲࠨ൉")) as f:
          content = f.read().strip()
          if content:
            bstack1lll1l11ll_opy_ = json.loads(content)
      bstack1lll1l11ll_opy_[item_index] = platform_index
      with open(bstack11ll111l1_opy_, bstack1lllll1l_opy_ (u"ࠢࡸࠤൊ")) as outfile:
        json.dump(bstack1lll1l11ll_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡻࡷ࡯ࡴࡪࡰࡪࠤࡹࡵࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ോ") + str(e))
def bstack1ll111llll_opy_(bstack1ll11llll1_opy_):
  global CONFIG
  bstack1l111ll1l_opy_ = bstack1lllll1l_opy_ (u"ࠩࠪൌ")
  if not bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ്࠭") in CONFIG:
    logger.info(bstack1lllll1l_opy_ (u"ࠫࡓࡵࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠣࡴࡦࡹࡳࡦࡦࠣࡹࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡧࡦࡰࡨࡶࡦࡺࡥࠡࡴࡨࡴࡴࡸࡴࠡࡨࡲࡶࠥࡘ࡯ࡣࡱࡷࠤࡷࡻ࡮ࠨൎ"))
  try:
    platform = CONFIG[bstack1lllll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ൏")][bstack1ll11llll1_opy_]
    if bstack1lllll1l_opy_ (u"࠭࡯ࡴࠩ൐") in platform:
      bstack1l111ll1l_opy_ += str(platform[bstack1lllll1l_opy_ (u"ࠧࡰࡵࠪ൑")]) + bstack1lllll1l_opy_ (u"ࠨ࠮ࠣࠫ൒")
    if bstack1lllll1l_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬ൓") in platform:
      bstack1l111ll1l_opy_ += str(platform[bstack1lllll1l_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ൔ")]) + bstack1lllll1l_opy_ (u"ࠫ࠱ࠦࠧൕ")
    if bstack1lllll1l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩൖ") in platform:
      bstack1l111ll1l_opy_ += str(platform[bstack1lllll1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪൗ")]) + bstack1lllll1l_opy_ (u"ࠧ࠭ࠢࠪ൘")
    if bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ൙") in platform:
      bstack1l111ll1l_opy_ += str(platform[bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ൚")]) + bstack1lllll1l_opy_ (u"ࠪ࠰ࠥ࠭൛")
    if bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ൜") in platform:
      bstack1l111ll1l_opy_ += str(platform[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ൝")]) + bstack1lllll1l_opy_ (u"࠭ࠬࠡࠩ൞")
    if bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨൟ") in platform:
      bstack1l111ll1l_opy_ += str(platform[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩൠ")]) + bstack1lllll1l_opy_ (u"ࠩ࠯ࠤࠬൡ")
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠪࡗࡴࡳࡥࠡࡧࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡳ࡭ࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡶࡸࡷ࡯࡮ࡨࠢࡩࡳࡷࠦࡲࡦࡲࡲࡶࡹࠦࡧࡦࡰࡨࡶࡦࡺࡩࡰࡰࠪൢ") + str(e))
  finally:
    if bstack1l111ll1l_opy_[len(bstack1l111ll1l_opy_) - 2:] == bstack1lllll1l_opy_ (u"ࠫ࠱ࠦࠧൣ"):
      bstack1l111ll1l_opy_ = bstack1l111ll1l_opy_[:-2]
    return bstack1l111ll1l_opy_
def bstack111l11l11l_opy_(path, bstack1l111ll1l_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack111lll111_opy_ = ET.parse(path)
    bstack1111ll11l_opy_ = bstack111lll111_opy_.getroot()
    bstack111llll1ll_opy_ = None
    for suite in bstack1111ll11l_opy_.iter(bstack1lllll1l_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫ൤")):
      if bstack1lllll1l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭൥") in suite.attrib:
        suite.attrib[bstack1lllll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ൦")] += bstack1lllll1l_opy_ (u"ࠨࠢࠪ൧") + bstack1l111ll1l_opy_
        bstack111llll1ll_opy_ = suite
    bstack1llll11lll_opy_ = None
    for robot in bstack1111ll11l_opy_.iter(bstack1lllll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ൨")):
      bstack1llll11lll_opy_ = robot
    bstack11l11lll11_opy_ = len(bstack1llll11lll_opy_.findall(bstack1lllll1l_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩ൩")))
    if bstack11l11lll11_opy_ == 1:
      bstack1llll11lll_opy_.remove(bstack1llll11lll_opy_.findall(bstack1lllll1l_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪ൪"))[0])
      bstack111llll11_opy_ = ET.Element(bstack1lllll1l_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫ൫"), attrib={bstack1lllll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ൬"): bstack1lllll1l_opy_ (u"ࠧࡔࡷ࡬ࡸࡪࡹࠧ൭"), bstack1lllll1l_opy_ (u"ࠨ࡫ࡧࠫ൮"): bstack1lllll1l_opy_ (u"ࠩࡶ࠴ࠬ൯")})
      bstack1llll11lll_opy_.insert(1, bstack111llll11_opy_)
      bstack111l11lll1_opy_ = None
      for suite in bstack1llll11lll_opy_.iter(bstack1lllll1l_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩ൰")):
        bstack111l11lll1_opy_ = suite
      bstack111l11lll1_opy_.append(bstack111llll1ll_opy_)
      bstack111ll11l11_opy_ = None
      for status in bstack111llll1ll_opy_.iter(bstack1lllll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ൱")):
        bstack111ll11l11_opy_ = status
      bstack111l11lll1_opy_.append(bstack111ll11l11_opy_)
    bstack111lll111_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡵࡷ࡮ࡴࡧࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡱࡩࡷࡧࡴࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠪ൲") + str(e))
def bstack11lllll11l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1lll11l11l_opy_
  global CONFIG
  if bstack1lllll1l_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࡶࡡࡵࡪࠥ൳") in options:
    del options[bstack1lllll1l_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࡰࡢࡶ࡫ࠦ൴")]
  json_data = bstack1l1ll1l1l_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack1lllll1l_opy_ (u"ࠨࡲࡤࡦࡴࡺ࡟ࡳࡧࡶࡹࡱࡺࡳࠨ൵"), str(item_id), bstack1lllll1l_opy_ (u"ࠩࡲࡹࡹࡶࡵࡵ࠰ࡻࡱࡱ࠭൶"))
    bstack111l11l11l_opy_(path, bstack1ll111llll_opy_(json_data[item_id]))
  bstack1l111l11l1_opy_()
  return bstack1lll11l11l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack111111ll1_opy_(self, ff_profile_dir):
  global bstack1ll11l11l_opy_
  if not ff_profile_dir:
    return None
  return bstack1ll11l11l_opy_(self, ff_profile_dir)
def bstack1l1ll11l11_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l1l1l111_opy_
  bstack111111ll1l_opy_ = []
  if bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭൷") in CONFIG:
    bstack111111ll1l_opy_ = CONFIG[bstack1lllll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ൸")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1lllll1l_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࠨ൹")],
      pabot_args[bstack1lllll1l_opy_ (u"ࠨࡶࡦࡴࡥࡳࡸ࡫ࠢൺ")],
      argfile,
      pabot_args.get(bstack1lllll1l_opy_ (u"ࠢࡩ࡫ࡹࡩࠧൻ")),
      pabot_args[bstack1lllll1l_opy_ (u"ࠣࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠦർ")],
      platform[0],
      bstack1l1l1l111_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1lllll1l_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡪ࡮ࡲࡥࡴࠤൽ")] or [(bstack1lllll1l_opy_ (u"ࠥࠦൾ"), None)]
    for platform in enumerate(bstack111111ll1l_opy_)
  ]
def bstack1l1ll1ll11_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack11111ll1ll_opy_=bstack1lllll1l_opy_ (u"ࠫࠬൿ")):
  global bstack1llll1l1ll_opy_
  self.platform_index = platform_index
  self.bstack11l1l11ll1_opy_ = bstack11111ll1ll_opy_
  bstack1llll1l1ll_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1lll111lll_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l1ll1lll_opy_
  global bstack1ll111l1l1_opy_
  bstack1ll111l111_opy_ = copy.deepcopy(item)
  if not bstack1lllll1l_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ඀") in item.options:
    bstack1ll111l111_opy_.options[bstack1lllll1l_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨඁ")] = []
  bstack1l1l1111l1_opy_ = bstack1ll111l111_opy_.options[bstack1lllll1l_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩං")].copy()
  for v in bstack1ll111l111_opy_.options[bstack1lllll1l_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪඃ")]:
    if bstack1lllll1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘࠨ඄") in v:
      bstack1l1l1111l1_opy_.remove(v)
    if bstack1lllll1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕࠪඅ") in v:
      bstack1l1l1111l1_opy_.remove(v)
    if bstack1lllll1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡈࡊࡌࡌࡐࡅࡄࡐࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨආ") in v:
      bstack1l1l1111l1_opy_.remove(v)
  bstack1l1l1111l1_opy_.insert(0, bstack1lllll1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛࠾ࢀࢃࠧඇ").format(bstack1ll111l111_opy_.platform_index))
  bstack1l1l1111l1_opy_.insert(0, bstack1lllll1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡊࡅࡇࡎࡒࡇࡆࡒࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔ࠽ࡿࢂ࠭ඈ").format(bstack1ll111l111_opy_.bstack11l1l11ll1_opy_))
  bstack1ll111l111_opy_.options[bstack1lllll1l_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩඉ")] = bstack1l1l1111l1_opy_
  if bstack1ll111l1l1_opy_:
    bstack1ll111l111_opy_.options[bstack1lllll1l_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪඊ")].insert(0, bstack1lllll1l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡅࡏࡍࡆࡘࡇࡔ࠼ࡾࢁࠬඋ").format(bstack1ll111l1l1_opy_))
  return bstack1l1ll1lll_opy_(caller_id, datasources, is_last, bstack1ll111l111_opy_, outs_dir)
def bstack1l1lllll1_opy_(command, item_index):
  try:
    if bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫඌ")):
      os.environ[bstack1lllll1l_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬඍ")] = json.dumps(CONFIG[bstack1lllll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨඎ")][item_index % bstack111lllll1l_opy_])
    global bstack1ll111l1l1_opy_
    if bstack1ll111l1l1_opy_:
      command[0] = command[0].replace(bstack1lllll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬඏ"), bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡳࡥ࡭ࠣࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠣࠫඐ") + str(
        item_index) + bstack1lllll1l_opy_ (u"ࠨࠢࠪඑ") + bstack1ll111l1l1_opy_, 1)
    else:
      command[0] = command[0].replace(bstack1lllll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨඒ"),
                                      bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧඓ") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack1lllll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡱࡴࡪࡩࡧࡻ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰࡥࡳࡪࠠࡧࡱࡵࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴ࠺ࠡࡽࢀࠫඔ").format(str(e)))
def bstack1ll1l111l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack111lll111l_opy_
  try:
    bstack1l1lllll1_opy_(command, item_index)
    return bstack111lll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack1lllll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰ࠽ࠤࢀࢃࠧඕ").format(str(e)))
    raise e
def bstack111ll11111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack111lll111l_opy_
  try:
    bstack1l1lllll1_opy_(command, item_index)
    return bstack111lll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack1lllll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠷࠴࠱࠴࠼ࠣࡿࢂ࠭ඖ").format(str(e)))
    try:
      return bstack111lll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack1lllll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡ࠴࠱࠵࠸ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࡾࢁࠬ඗").format(str(e2)))
      raise e
def bstack1111l1ll11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack111lll111l_opy_
  try:
    bstack1l1lllll1_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack111lll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack1lllll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࠦ࠲࠯࠳࠸࠾ࠥࢁࡽࠨ඘").format(str(e)))
    try:
      return bstack111lll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack1lllll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣ࠶࠳࠷࠵ࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧ඙").format(str(e2)))
      raise e
def _11l11ll11_opy_(bstack1111l111ll_opy_, item_index, process_timeout, sleep_before_start, bstack11lllll1l1_opy_):
  bstack1l1lllll1_opy_(bstack1111l111ll_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack11ll1l11l1_opy_(command, bstack11lll1l1ll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack111lll111l_opy_
  try:
    bstack1l1lllll1_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack111lll111l_opy_(command, bstack11lll1l1ll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1lllll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠷࠱࠴࠿ࠦࡻࡾࠩක").format(str(e)))
    try:
      return bstack111lll111l_opy_(command, bstack11lll1l1ll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1lllll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫඛ").format(str(e2)))
      raise e
def bstack1ll1lllll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack111lll111l_opy_
  try:
    process_timeout = _11l11ll11_opy_(command, item_index, process_timeout, sleep_before_start, bstack1lllll1l_opy_ (u"ࠬ࠺࠮࠳ࠩග"))
    return bstack111lll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1lllll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠹࠴࠲࠻ࠢࡾࢁࠬඝ").format(str(e)))
    try:
      return bstack111lll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1lllll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧඞ").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack1l1l1ll1l_opy_(self, runner, quiet=False, capture=True):
  global bstack1l11l1llll_opy_
  bstack1111l111l1_opy_ = bstack1l11l1llll_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack1lllll1l_opy_ (u"ࠨࡧࡻࡧࡪࡶࡴࡪࡱࡱࡣࡦࡸࡲࠨඟ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1lllll1l_opy_ (u"ࠩࡨࡼࡨࡥࡴࡳࡣࡦࡩࡧࡧࡣ࡬ࡡࡤࡶࡷ࠭ච")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1111l111l1_opy_
def bstack1l111l1lll_opy_(runner, hook_name, context, element, bstack11l11ll1l_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1l1ll1llll_opy_.bstack11l1l111_opy_(hook_name, element)
    bstack11l11ll1l_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1l1ll1llll_opy_.bstack11l11l1l_opy_(element)
      if hook_name not in [bstack1lllll1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠧඡ"), bstack1lllll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧජ")] and args and hasattr(args[0], bstack1lllll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡣࡲ࡫ࡳࡴࡣࡪࡩࠬඣ")):
        args[0].error_message = bstack1lllll1l_opy_ (u"࠭ࠧඤ")
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡬ࡦࡴࡤ࡭ࡧࠣ࡬ࡴࡵ࡫ࡴࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩ࠿ࠦࡻࡾࠩඥ").format(str(e)))
@measure(event_name=EVENTS.bstack11l1ll1lll_opy_, stage=STAGE.bstack1l11ll1ll_opy_, hook_type=bstack1lllll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡂ࡮࡯ࠦඦ"), bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1ll1l1l1ll_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    if runner.hooks.get(bstack1lllll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨට")).__name__ != bstack1lllll1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲ࡟ࡥࡧࡩࡥࡺࡲࡴࡠࡪࡲࡳࡰࠨඨ"):
      bstack1l111l1lll_opy_(runner, name, context, runner, bstack11l11ll1l_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack111l111l11_opy_(bstack1lllll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪඩ")) else context.browser
      runner.driver_initialised = bstack1lllll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤඪ")
    except Exception as e:
      logger.debug(bstack1lllll1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡤࡳ࡫ࡹࡩࡷࠦࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡧࠣࡥࡹࡺࡲࡪࡤࡸࡸࡪࡀࠠࡼࡿࠪණ").format(str(e)))
def bstack1lllll1111_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    bstack1l111l1lll_opy_(runner, name, context, context.feature, bstack11l11ll1l_opy_, *args)
    try:
      if not bstack1l1l1l1l1l_opy_:
        bstack1ll111l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack111l111l11_opy_(bstack1lllll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ඬ")) else context.browser
        if is_driver_active(bstack1ll111l1l_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack1lllll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤත")
          bstack1ll11l1l1l_opy_ = str(runner.feature.name)
          bstack111111l1l_opy_(context, bstack1ll11l1l1l_opy_)
          bstack1ll111l1l_opy_.execute_script(bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧථ") + json.dumps(bstack1ll11l1l1l_opy_) + bstack1lllll1l_opy_ (u"ࠪࢁࢂ࠭ද"))
    except Exception as e:
      logger.debug(bstack1lllll1l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫධ").format(str(e)))
def bstack1llll111ll_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    if hasattr(context, bstack1lllll1l_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧන")):
        bstack1l1ll1llll_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack1lllll1l_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ඲")) else context.feature
    bstack1l111l1lll_opy_(runner, name, context, target, bstack11l11ll1l_opy_, *args)
@measure(event_name=EVENTS.bstack111llll1l1_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack11lll111l_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1l1ll1llll_opy_.start_test(context)
    bstack1l111l1lll_opy_(runner, name, context, context.scenario, bstack11l11ll1l_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack11llll1ll_opy_.bstack11l1lllll1_opy_(context, *args)
    try:
      bstack1ll111l1l_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ඳ"), context.browser)
      if is_driver_active(bstack1ll111l1l_opy_):
        bstack1ll1l1l1_opy_.bstack1111ll11ll_opy_(bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧප"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack1lllll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦඵ")
        if (not bstack1l1l1l1l1l_opy_):
          scenario_name = args[0].name
          feature_name = bstack1ll11l1l1l_opy_ = str(runner.feature.name)
          bstack1ll11l1l1l_opy_ = feature_name + bstack1lllll1l_opy_ (u"ࠪࠤ࠲ࠦࠧබ") + scenario_name
          if runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨභ"):
            bstack111111l1l_opy_(context, bstack1ll11l1l1l_opy_)
            bstack1ll111l1l_opy_.execute_script(bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪම") + json.dumps(bstack1ll11l1l1l_opy_) + bstack1lllll1l_opy_ (u"࠭ࡽࡾࠩඹ"))
    except Exception as e:
      logger.debug(bstack1lllll1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡪࡴࡡࡳ࡫ࡲ࠾ࠥࢁࡽࠨය").format(str(e)))
@measure(event_name=EVENTS.bstack11l1ll1lll_opy_, stage=STAGE.bstack1l11ll1ll_opy_, hook_type=bstack1lllll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡔࡶࡨࡴࠧර"), bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1lllll1ll1_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    bstack1l111l1lll_opy_(runner, name, context, args[0], bstack11l11ll1l_opy_, *args)
    try:
      bstack1ll111l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack111l111l11_opy_(bstack1lllll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ඼")) else context.browser
      if is_driver_active(bstack1ll111l1l_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack1lllll1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣල")
        bstack1l1ll1llll_opy_.bstack111lllll_opy_(args[0])
        if runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤ඾"):
          feature_name = bstack1ll11l1l1l_opy_ = str(runner.feature.name)
          bstack1ll11l1l1l_opy_ = feature_name + bstack1lllll1l_opy_ (u"ࠬࠦ࠭ࠡࠩ඿") + context.scenario.name
          bstack1ll111l1l_opy_.execute_script(bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫව") + json.dumps(bstack1ll11l1l1l_opy_) + bstack1lllll1l_opy_ (u"ࠧࡾࡿࠪශ"))
    except Exception as e:
      logger.debug(bstack1lllll1l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡹ࡫ࡰ࠻ࠢࡾࢁࠬෂ").format(str(e)))
@measure(event_name=EVENTS.bstack11l1ll1lll_opy_, stage=STAGE.bstack1l11ll1ll_opy_, hook_type=bstack1lllll1l_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡔࡶࡨࡴࠧස"), bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack11111l11ll_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
  bstack1l1ll1llll_opy_.bstack11l11111_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack1ll111l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lllll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩහ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1ll111l1l_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack1lllll1l_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫළ")
        feature_name = bstack1ll11l1l1l_opy_ = str(runner.feature.name)
        bstack1ll11l1l1l_opy_ = feature_name + bstack1lllll1l_opy_ (u"ࠬࠦ࠭ࠡࠩෆ") + context.scenario.name
        bstack1ll111l1l_opy_.execute_script(bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫ෇") + json.dumps(bstack1ll11l1l1l_opy_) + bstack1lllll1l_opy_ (u"ࠧࡾࡿࠪ෈"))
    if str(step_status).lower() == bstack1lllll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ෉"):
      bstack11lll11111_opy_ = bstack1lllll1l_opy_ (u"්ࠩࠪ")
      bstack11l1l11ll_opy_ = bstack1lllll1l_opy_ (u"ࠪࠫ෋")
      bstack11l1l111l_opy_ = bstack1lllll1l_opy_ (u"ࠫࠬ෌")
      try:
        import traceback
        bstack11lll11111_opy_ = runner.exception.__class__.__name__
        bstack111lll1l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11l1l11ll_opy_ = bstack1lllll1l_opy_ (u"ࠬࠦࠧ෍").join(bstack111lll1l_opy_)
        bstack11l1l111l_opy_ = bstack111lll1l_opy_[-1]
      except Exception as e:
        logger.debug(bstack111lllll1_opy_.format(str(e)))
      bstack11lll11111_opy_ += bstack11l1l111l_opy_
      bstack1l111lll1_opy_(context, json.dumps(str(args[0].name) + bstack1lllll1l_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧ෎") + str(bstack11l1l11ll_opy_)),
                          bstack1lllll1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨා"))
      if runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨැ"):
        bstack1l1ll111ll_opy_(getattr(context, bstack1lllll1l_opy_ (u"ࠩࡳࡥ࡬࡫ࠧෑ"), None), bstack1lllll1l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥි"), bstack11lll11111_opy_)
        bstack1ll111l1l_opy_.execute_script(bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩී") + json.dumps(str(args[0].name) + bstack1lllll1l_opy_ (u"ࠧࠦ࠭ࠡࡈࡤ࡭ࡱ࡫ࡤࠢ࡞ࡱࠦු") + str(bstack11l1l11ll_opy_)) + bstack1lllll1l_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭෕"))
      if runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧූ"):
        bstack1l1ll1l11_opy_(bstack1ll111l1l_opy_, bstack1lllll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ෗"), bstack1lllll1l_opy_ (u"ࠤࡖࡧࡪࡴࡡࡳ࡫ࡲࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨෘ") + str(bstack11lll11111_opy_))
    else:
      bstack1l111lll1_opy_(context, bstack1lllll1l_opy_ (u"ࠥࡔࡦࡹࡳࡦࡦࠤࠦෙ"), bstack1lllll1l_opy_ (u"ࠦ࡮ࡴࡦࡰࠤේ"))
      if runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥෛ"):
        bstack1l1ll111ll_opy_(getattr(context, bstack1lllll1l_opy_ (u"࠭ࡰࡢࡩࡨࠫො"), None), bstack1lllll1l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢෝ"))
      bstack1ll111l1l_opy_.execute_script(bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ෞ") + json.dumps(str(args[0].name) + bstack1lllll1l_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨෟ")) + bstack1lllll1l_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩ෠"))
      if runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤ෡"):
        bstack1l1ll1l11_opy_(bstack1ll111l1l_opy_, bstack1lllll1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ෢"))
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡷࡹ࡫ࡰ࠻ࠢࡾࢁࠬ෣").format(str(e)))
  bstack1l111l1lll_opy_(runner, name, context, args[0], bstack11l11ll1l_opy_, *args)
@measure(event_name=EVENTS.bstack11l11l11l1_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1lll1111l1_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
  bstack1l1ll1llll_opy_.end_test(args[0])
  try:
    bstack11l111ll11_opy_ = args[0].status.name
    bstack1ll111l1l_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭෤"), context.browser)
    bstack11llll1ll_opy_.bstack111l111111_opy_(bstack1ll111l1l_opy_)
    if str(bstack11l111ll11_opy_).lower() == bstack1lllll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ෥"):
      bstack11lll11111_opy_ = bstack1lllll1l_opy_ (u"ࠩࠪ෦")
      bstack11l1l11ll_opy_ = bstack1lllll1l_opy_ (u"ࠪࠫ෧")
      bstack11l1l111l_opy_ = bstack1lllll1l_opy_ (u"ࠫࠬ෨")
      try:
        import traceback
        bstack11lll11111_opy_ = runner.exception.__class__.__name__
        bstack111lll1l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11l1l11ll_opy_ = bstack1lllll1l_opy_ (u"ࠬࠦࠧ෩").join(bstack111lll1l_opy_)
        bstack11l1l111l_opy_ = bstack111lll1l_opy_[-1]
      except Exception as e:
        logger.debug(bstack111lllll1_opy_.format(str(e)))
      bstack11lll11111_opy_ += bstack11l1l111l_opy_
      bstack1l111lll1_opy_(context, json.dumps(str(args[0].name) + bstack1lllll1l_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧ෪") + str(bstack11l1l11ll_opy_)),
                          bstack1lllll1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨ෫"))
      if runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥ෬") or runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠩ࡬ࡲࡸࡺࡥࡱࠩ෭"):
        bstack1l1ll111ll_opy_(getattr(context, bstack1lllll1l_opy_ (u"ࠪࡴࡦ࡭ࡥࠨ෮"), None), bstack1lllll1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ෯"), bstack11lll11111_opy_)
        bstack1ll111l1l_opy_.execute_script(bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ෰") + json.dumps(str(args[0].name) + bstack1lllll1l_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧ෱") + str(bstack11l1l11ll_opy_)) + bstack1lllll1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧෲ"))
      if runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥෳ") or runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠩ࡬ࡲࡸࡺࡥࡱࠩ෴"):
        bstack1l1ll1l11_opy_(bstack1ll111l1l_opy_, bstack1lllll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ෵"), bstack1lllll1l_opy_ (u"ࠦࡘࡩࡥ࡯ࡣࡵ࡭ࡴࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣ෶") + str(bstack11lll11111_opy_))
    else:
      bstack1l111lll1_opy_(context, bstack1lllll1l_opy_ (u"ࠧࡖࡡࡴࡵࡨࡨࠦࠨ෷"), bstack1lllll1l_opy_ (u"ࠨࡩ࡯ࡨࡲࠦ෸"))
      if runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤ෹") or runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨ෺"):
        bstack1l1ll111ll_opy_(getattr(context, bstack1lllll1l_opy_ (u"ࠩࡳࡥ࡬࡫ࠧ෻"), None), bstack1lllll1l_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ෼"))
      bstack1ll111l1l_opy_.execute_script(bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ෽") + json.dumps(str(args[0].name) + bstack1lllll1l_opy_ (u"ࠧࠦ࠭ࠡࡒࡤࡷࡸ࡫ࡤࠢࠤ෾")) + bstack1lllll1l_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬ෿"))
      if runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤ฀") or runner.driver_initialised == bstack1lllll1l_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨก"):
        bstack1l1ll1l11_opy_(bstack1ll111l1l_opy_, bstack1lllll1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤข"))
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡧࡧࡤࡸࡺࡸࡥ࠻ࠢࡾࢁࠬฃ").format(str(e)))
  bstack1l111l1lll_opy_(runner, name, context, context.scenario, bstack11l11ll1l_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1l111111l_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    target = context.scenario if hasattr(context, bstack1lllll1l_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ค")) else context.feature
    bstack1l111l1lll_opy_(runner, name, context, target, bstack11l11ll1l_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack111111ll11_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    try:
      bstack1ll111l1l_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫฅ"), context.browser)
      bstack1l11l11lll_opy_ = bstack1lllll1l_opy_ (u"࠭ࠧฆ")
      if context.failed is True:
        bstack111ll1ll1l_opy_ = []
        bstack111l11l1l_opy_ = []
        bstack1ll11lllll_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack111ll1ll1l_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack111lll1l_opy_ = traceback.format_tb(exc_tb)
            bstack11llll1l1_opy_ = bstack1lllll1l_opy_ (u"ࠧࠡࠩง").join(bstack111lll1l_opy_)
            bstack111l11l1l_opy_.append(bstack11llll1l1_opy_)
            bstack1ll11lllll_opy_.append(bstack111lll1l_opy_[-1])
        except Exception as e:
          logger.debug(bstack111lllll1_opy_.format(str(e)))
        bstack11lll11111_opy_ = bstack1lllll1l_opy_ (u"ࠨࠩจ")
        for i in range(len(bstack111ll1ll1l_opy_)):
          bstack11lll11111_opy_ += bstack111ll1ll1l_opy_[i] + bstack1ll11lllll_opy_[i] + bstack1lllll1l_opy_ (u"ࠩ࡟ࡲࠬฉ")
        bstack1l11l11lll_opy_ = bstack1lllll1l_opy_ (u"ࠪࠤࠬช").join(bstack111l11l1l_opy_)
        if runner.driver_initialised in [bstack1lllll1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧซ"), bstack1lllll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤฌ")]:
          bstack1l111lll1_opy_(context, bstack1l11l11lll_opy_, bstack1lllll1l_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧญ"))
          bstack1l1ll111ll_opy_(getattr(context, bstack1lllll1l_opy_ (u"ࠧࡱࡣࡪࡩࠬฎ"), None), bstack1lllll1l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣฏ"), bstack11lll11111_opy_)
          bstack1ll111l1l_opy_.execute_script(bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧฐ") + json.dumps(bstack1l11l11lll_opy_) + bstack1lllll1l_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪฑ"))
          bstack1l1ll1l11_opy_(bstack1ll111l1l_opy_, bstack1lllll1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦฒ"), bstack1lllll1l_opy_ (u"࡙ࠧ࡯࡮ࡧࠣࡷࡨ࡫࡮ࡢࡴ࡬ࡳࡸࠦࡦࡢ࡫࡯ࡩࡩࡀࠠ࡝ࡰࠥณ") + str(bstack11lll11111_opy_))
          bstack1l1ll11l1l_opy_ = bstack1l1l1llll_opy_(bstack1l11l11lll_opy_, runner.feature.name, logger)
          if (bstack1l1ll11l1l_opy_ != None):
            bstack111l11l11_opy_.append(bstack1l1ll11l1l_opy_)
      else:
        if runner.driver_initialised in [bstack1lllll1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢด"), bstack1lllll1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦต")]:
          bstack1l111lll1_opy_(context, bstack1lllll1l_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦ࠼ࠣࠦถ") + str(runner.feature.name) + bstack1lllll1l_opy_ (u"ࠤࠣࡴࡦࡹࡳࡦࡦࠤࠦท"), bstack1lllll1l_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣธ"))
          bstack1l1ll111ll_opy_(getattr(context, bstack1lllll1l_opy_ (u"ࠫࡵࡧࡧࡦࠩน"), None), bstack1lllll1l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧบ"))
          bstack1ll111l1l_opy_.execute_script(bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫป") + json.dumps(bstack1lllll1l_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥ࠻ࠢࠥผ") + str(runner.feature.name) + bstack1lllll1l_opy_ (u"ࠣࠢࡳࡥࡸࡹࡥࡥࠣࠥฝ")) + bstack1lllll1l_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧࢃࡽࠨพ"))
          bstack1l1ll1l11_opy_(bstack1ll111l1l_opy_, bstack1lllll1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪฟ"))
          bstack1l1ll11l1l_opy_ = bstack1l1l1llll_opy_(bstack1l11l11lll_opy_, runner.feature.name, logger)
          if (bstack1l1ll11l1l_opy_ != None):
            bstack111l11l11_opy_.append(bstack1l1ll11l1l_opy_)
    except Exception as e:
      logger.debug(bstack1lllll1l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭ภ").format(str(e)))
    bstack1l111l1lll_opy_(runner, name, context, context.feature, bstack11l11ll1l_opy_, *args)
@measure(event_name=EVENTS.bstack11l1ll1lll_opy_, stage=STAGE.bstack1l11ll1ll_opy_, hook_type=bstack1lllll1l_opy_ (u"ࠧࡧࡦࡵࡧࡵࡅࡱࡲࠢม"), bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1l1l1l1111_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    bstack1l111l1lll_opy_(runner, name, context, runner, bstack11l11ll1l_opy_, *args)
def bstack11lll1ll1l_opy_(self, name, context, *args):
  try:
    if bstack11ll1l1l1l_opy_:
      platform_index = int(threading.current_thread()._name) % bstack111lllll1l_opy_
      bstack111l1111ll_opy_ = CONFIG[bstack1lllll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩย")][platform_index]
      os.environ[bstack1lllll1l_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨร")] = json.dumps(bstack111l1111ll_opy_)
    global bstack11l11ll1l_opy_
    if not hasattr(self, bstack1lllll1l_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡩࡩ࠭ฤ")):
      self.driver_initialised = None
    bstack11lllll1ll_opy_ = {
        bstack1lllll1l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱ࠭ล"): bstack1ll1l1l1ll_opy_,
        bstack1lllll1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠫฦ"): bstack1lllll1111_opy_,
        bstack1lllll1l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡹࡧࡧࠨว"): bstack1llll111ll_opy_,
        bstack1lllll1l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧศ"): bstack11lll111l_opy_,
        bstack1lllll1l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠫษ"): bstack1lllll1ll1_opy_,
        bstack1lllll1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡵࡧࡳࠫส"): bstack11111l11ll_opy_,
        bstack1lllll1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩห"): bstack1lll1111l1_opy_,
        bstack1lllll1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡶࡤ࡫ࠬฬ"): bstack1l111111l_opy_,
        bstack1lllll1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪอ"): bstack111111ll11_opy_,
        bstack1lllll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧฮ"): bstack1l1l1l1111_opy_
    }
    handler = bstack11lllll1ll_opy_.get(name, bstack11l11ll1l_opy_)
    try:
      handler(self, name, context, bstack11l11ll1l_opy_, *args)
    except Exception as e:
      logger.debug(bstack1lllll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡩࡱࡲ࡯ࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࠦࡻࡾ࠼ࠣࡿࢂ࠭ฯ").format(name, str(e)))
    if name in [bstack1lllll1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ะ"), bstack1lllll1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨั"), bstack1lllll1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫา")]:
      try:
        bstack1ll111l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack111l111l11_opy_(bstack1lllll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨำ")) else context.browser
        bstack11ll1lll1l_opy_ = (
          (name == bstack1lllll1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡤࡰࡱ࠭ิ") and self.driver_initialised == bstack1lllll1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣี")) or
          (name == bstack1lllll1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠬึ") and self.driver_initialised == bstack1lllll1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢื")) or
          (name == bstack1lllll1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨุ") and self.driver_initialised in [bstack1lllll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱูࠥ"), bstack1lllll1l_opy_ (u"ࠤ࡬ࡲࡸࡺࡥࡱࠤฺ")]) or
          (name == bstack1lllll1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡸࡪࡶࠧ฻") and self.driver_initialised == bstack1lllll1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤ฼"))
        )
        if bstack11ll1lll1l_opy_:
          self.driver_initialised = None
          if bstack1ll111l1l_opy_ and hasattr(bstack1ll111l1l_opy_, bstack1lllll1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩ฽")):
            try:
              bstack1ll111l1l_opy_.quit()
            except Exception as e:
              logger.debug(bstack1lllll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡷࡵࡪࡶࡷ࡭ࡳ࡭ࠠࡥࡴ࡬ࡺࡪࡸࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧࠣ࡬ࡴࡵ࡫࠻ࠢࡾࢁࠬ฾").format(str(e)))
      except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡪࡲࡳࡰࠦࡣ࡭ࡧࡤࡲࡺࡶࠠࡧࡱࡵࠤࢀࢃ࠺ࠡࡽࢀࠫ฿").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠨࡅࡵ࡭ࡹ࡯ࡣࡢ࡮ࠣࡩࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩࠥࡸࡵ࡯ࠢ࡫ࡳࡴࡱࠠࡼࡿ࠽ࠤࢀࢃࠧเ").format(name, str(e)))
    try:
      bstack11l11ll1l_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack1lllll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࠦ࡯ࡳ࡫ࡪ࡭ࡳࡧ࡬ࠡࡤࡨ࡬ࡦࡼࡥࠡࡪࡲࡳࡰࠦࡻࡾ࠼ࠣࡿࢂ࠭แ").format(name, str(e2)))
def bstack1l11111l1l_opy_(config, startdir):
  return bstack1lllll1l_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀ࠶ࡽࠣโ").format(bstack1lllll1l_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥใ"))
notset = Notset()
def bstack11l1ll111_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack11111l1lll_opy_
  if str(name).lower() == bstack1lllll1l_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬไ"):
    return bstack1lllll1l_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧๅ")
  else:
    return bstack11111l1lll_opy_(self, name, default, skip)
def bstack1l11l111l_opy_(item, when):
  global bstack1lllllllll_opy_
  try:
    bstack1lllllllll_opy_(item, when)
  except Exception as e:
    pass
def bstack1l1ll1ll1l_opy_():
  return
def bstack111lll1l11_opy_(type, name, status, reason, bstack1l1l1ll1ll_opy_, bstack1111ll11l1_opy_):
  bstack11ll11111_opy_ = {
    bstack1lllll1l_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧๆ"): type,
    bstack1lllll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ็"): {}
  }
  if type == bstack1lllll1l_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨ่ࠫ"):
    bstack11ll11111_opy_[bstack1lllll1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ้࠭")][bstack1lllll1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮๊ࠪ")] = bstack1l1l1ll1ll_opy_
    bstack11ll11111_opy_[bstack1lllll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ๋")][bstack1lllll1l_opy_ (u"࠭ࡤࡢࡶࡤࠫ์")] = json.dumps(str(bstack1111ll11l1_opy_))
  if type == bstack1lllll1l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨํ"):
    bstack11ll11111_opy_[bstack1lllll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ๎")][bstack1lllll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ๏")] = name
  if type == bstack1lllll1l_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭๐"):
    bstack11ll11111_opy_[bstack1lllll1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ๑")][bstack1lllll1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ๒")] = status
    if status == bstack1lllll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭๓"):
      bstack11ll11111_opy_[bstack1lllll1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ๔")][bstack1lllll1l_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ๕")] = json.dumps(str(reason))
  bstack1l1l11ll11_opy_ = bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧ๖").format(json.dumps(bstack11ll11111_opy_))
  return bstack1l1l11ll11_opy_
def bstack111l1ll1l_opy_(driver_command, response):
    if driver_command == bstack1lllll1l_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧ๗"):
        bstack1ll1l1l1_opy_.bstack11111llll1_opy_({
            bstack1lllll1l_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࠪ๘"): response[bstack1lllll1l_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫ๙")],
            bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭๚"): bstack1ll1l1l1_opy_.current_test_uuid()
        })
def bstack11l1111ll1_opy_(item, call, rep):
  global bstack11111l11l1_opy_
  global bstack1111lll11l_opy_
  global bstack1l1l1l1l1l_opy_
  name = bstack1lllll1l_opy_ (u"ࠧࠨ๛")
  try:
    if rep.when == bstack1lllll1l_opy_ (u"ࠨࡥࡤࡰࡱ࠭๜"):
      bstack11llll1lll_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1l1l1l1l1l_opy_:
          name = str(rep.nodeid)
          bstack111l1l1lll_opy_ = bstack111lll1l11_opy_(bstack1lllll1l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ๝"), name, bstack1lllll1l_opy_ (u"ࠪࠫ๞"), bstack1lllll1l_opy_ (u"ࠫࠬ๟"), bstack1lllll1l_opy_ (u"ࠬ࠭๠"), bstack1lllll1l_opy_ (u"࠭ࠧ๡"))
          threading.current_thread().bstack111111lll1_opy_ = name
          for driver in bstack1111lll11l_opy_:
            if bstack11llll1lll_opy_ == driver.session_id:
              driver.execute_script(bstack111l1l1lll_opy_)
      except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧ๢").format(str(e)))
      try:
        bstack11ll11llll_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1lllll1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ๣"):
          status = bstack1lllll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ๤") if rep.outcome.lower() == bstack1lllll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ๥") else bstack1lllll1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ๦")
          reason = bstack1lllll1l_opy_ (u"ࠬ࠭๧")
          if status == bstack1lllll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭๨"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1lllll1l_opy_ (u"ࠧࡪࡰࡩࡳࠬ๩") if status == bstack1lllll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ๪") else bstack1lllll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ๫")
          data = name + bstack1lllll1l_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬ๬") if status == bstack1lllll1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ๭") else name + bstack1lllll1l_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩࠧࠠࠨ๮") + reason
          bstack111l11lll_opy_ = bstack111lll1l11_opy_(bstack1lllll1l_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ๯"), bstack1lllll1l_opy_ (u"ࠧࠨ๰"), bstack1lllll1l_opy_ (u"ࠨࠩ๱"), bstack1lllll1l_opy_ (u"ࠩࠪ๲"), level, data)
          for driver in bstack1111lll11l_opy_:
            if bstack11llll1lll_opy_ == driver.session_id:
              driver.execute_script(bstack111l11lll_opy_)
      except Exception as e:
        logger.debug(bstack1lllll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡤࡱࡱࡸࡪࡾࡴࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧ๳").format(str(e)))
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡶࡤࡸࡪࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁࡽࠨ๴").format(str(e)))
  bstack11111l11l1_opy_(item, call, rep)
def bstack1ll11l1l11_opy_(driver, bstack1l1ll11ll_opy_, test=None):
  global bstack11111ll1l1_opy_
  if test != None:
    bstack1l1l1l1l1_opy_ = getattr(test, bstack1lllll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ๵"), None)
    bstack11l1llllll_opy_ = getattr(test, bstack1lllll1l_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ๶"), None)
    PercySDK.screenshot(driver, bstack1l1ll11ll_opy_, bstack1l1l1l1l1_opy_=bstack1l1l1l1l1_opy_, bstack11l1llllll_opy_=bstack11l1llllll_opy_, bstack1l11111111_opy_=bstack11111ll1l1_opy_)
  else:
    PercySDK.screenshot(driver, bstack1l1ll11ll_opy_)
@measure(event_name=EVENTS.bstack11l1l1lll1_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack11lllll111_opy_(driver):
  if bstack1l11lll1ll_opy_.bstack111l111ll1_opy_() is True or bstack1l11lll1ll_opy_.capturing() is True:
    return
  bstack1l11lll1ll_opy_.bstack1l1l1ll111_opy_()
  while not bstack1l11lll1ll_opy_.bstack111l111ll1_opy_():
    bstack1l1llllll_opy_ = bstack1l11lll1ll_opy_.bstack111ll111l1_opy_()
    bstack1ll11l1l11_opy_(driver, bstack1l1llllll_opy_)
  bstack1l11lll1ll_opy_.bstack1ll1l1l111_opy_()
def bstack1ll11ll1l1_opy_(sequence, driver_command, response = None, bstack1lll1llll1_opy_ = None, args = None):
    try:
      if sequence != bstack1lllll1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧ๷"):
        return
      if percy.bstack1lllll11l1_opy_() == bstack1lllll1l_opy_ (u"ࠣࡨࡤࡰࡸ࡫ࠢ๸"):
        return
      bstack1l1llllll_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ๹"), None)
      for command in bstack1l1llll111_opy_:
        if command == driver_command:
          with bstack1111l1l1l1_opy_:
            bstack1111l1lll1_opy_ = bstack1111lll11l_opy_.copy()
          for driver in bstack1111l1lll1_opy_:
            bstack11lllll111_opy_(driver)
      bstack1l111l1l1l_opy_ = percy.bstack1ll11l111_opy_()
      if driver_command in bstack1ll1llll1l_opy_[bstack1l111l1l1l_opy_]:
        bstack1l11lll1ll_opy_.bstack1ll11l1l1_opy_(bstack1l1llllll_opy_, driver_command)
    except Exception as e:
      pass
def bstack11lllll1l_opy_(framework_name):
  if bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪࠧ๺")):
      return
  bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡲࡵࡤࡠࡥࡤࡰࡱ࡫ࡤࠨ๻"), True)
  global bstack1l11ll11l1_opy_
  global bstack1l11l11l1l_opy_
  global bstack11111ll11_opy_
  bstack1l11ll11l1_opy_ = framework_name
  logger.info(bstack111l1lll1_opy_.format(bstack1l11ll11l1_opy_.split(bstack1lllll1l_opy_ (u"ࠬ࠳ࠧ๼"))[0]))
  bstack111l1l1ll_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack11ll1l1l1l_opy_:
      Service.start = bstack1ll1l1lll_opy_
      Service.stop = bstack11l1111ll_opy_
      webdriver.Remote.get = bstack1l1111111_opy_
      WebDriver.quit = bstack1ll1ll1ll_opy_
      webdriver.Remote.__init__ = bstack11l1l111ll_opy_
    if not bstack11ll1l1l1l_opy_:
        webdriver.Remote.__init__ = bstack1ll1111l11_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack11l1llll11_opy_
    bstack1l11l11l1l_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack11ll1l1l1l_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack11llll11l_opy_
  except Exception as e:
    pass
  bstack1l1111ll11_opy_()
  if not bstack1l11l11l1l_opy_:
    bstack1l1ll11ll1_opy_(bstack1lllll1l_opy_ (u"ࠨࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠡࡰࡲࡸࠥ࡯࡮ࡴࡶࡤࡰࡱ࡫ࡤࠣ๽"), bstack1llll1ll11_opy_)
  if bstack11lll111l1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack1lllll1l_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ๾")) and callable(getattr(RemoteConnection, bstack1lllll1l_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ๿"))):
        RemoteConnection._get_proxy_url = bstack11111l1ll1_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack11111l1ll1_opy_
    except Exception as e:
      logger.error(bstack11lll11l1_opy_.format(str(e)))
  if bstack1ll11l1lll_opy_():
    bstack1ll1111ll_opy_(CONFIG, logger)
  if (bstack1lllll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ຀") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1lllll11l1_opy_() == bstack1lllll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣກ"):
          bstack11ll1ll11_opy_(bstack1ll11ll1l1_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack111111ll1_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack111l1111l1_opy_
      except Exception as e:
        logger.warn(bstack11ll111ll1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack11ll1111l_opy_
      except Exception as e:
        logger.debug(bstack11llll1l11_opy_ + str(e))
    except Exception as e:
      bstack1l1ll11ll1_opy_(e, bstack11ll111ll1_opy_)
    Output.start_test = bstack1ll1l11l1_opy_
    Output.end_test = bstack1l1lll1lll_opy_
    TestStatus.__init__ = bstack11l1llll1_opy_
    QueueItem.__init__ = bstack1l1ll1ll11_opy_
    pabot._create_items = bstack1l1ll11l11_opy_
    try:
      from pabot import __version__ as bstack1ll1lll1l1_opy_
      if version.parse(bstack1ll1lll1l1_opy_) >= version.parse(bstack1lllll1l_opy_ (u"ࠫ࠺࠴࠰࠯࠲ࠪຂ")):
        pabot._run = bstack11ll1l11l1_opy_
      elif version.parse(bstack1ll1lll1l1_opy_) >= version.parse(bstack1lllll1l_opy_ (u"ࠬ࠺࠮࠳࠰࠳ࠫ຃")):
        pabot._run = bstack1ll1lllll1_opy_
      elif version.parse(bstack1ll1lll1l1_opy_) >= version.parse(bstack1lllll1l_opy_ (u"࠭࠲࠯࠳࠸࠲࠵࠭ຄ")):
        pabot._run = bstack1111l1ll11_opy_
      elif version.parse(bstack1ll1lll1l1_opy_) >= version.parse(bstack1lllll1l_opy_ (u"ࠧ࠳࠰࠴࠷࠳࠶ࠧ຅")):
        pabot._run = bstack111ll11111_opy_
      else:
        pabot._run = bstack1ll1l111l1_opy_
    except Exception as e:
      pabot._run = bstack1ll1l111l1_opy_
    pabot._create_command_for_execution = bstack1lll111lll_opy_
    pabot._report_results = bstack11lllll11l_opy_
  if bstack1lllll1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨຆ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1ll11ll1_opy_(e, bstack1l11l1ll1l_opy_)
    Runner.run_hook = bstack11lll1ll1l_opy_
    Step.run = bstack1l1l1ll1l_opy_
  if bstack1lllll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩງ") in str(framework_name).lower():
    if not bstack11ll1l1l1l_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1l11111l1l_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1l1ll1ll1l_opy_
      Config.getoption = bstack11l1ll111_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack11l1111ll1_opy_
    except Exception as e:
      pass
def bstack11111l111l_opy_():
  global CONFIG
  if bstack1lllll1l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪຈ") in CONFIG and int(CONFIG[bstack1lllll1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫຉ")]) > 1:
    logger.warn(bstack1ll11ll1l_opy_)
def bstack11l11ll1l1_opy_(arg, bstack11111l1l_opy_, bstack11l1111111_opy_=None):
  global CONFIG
  global bstack11lll1111_opy_
  global bstack1l1111l11l_opy_
  global bstack11ll1l1l1l_opy_
  global bstack1lll1ll1l_opy_
  bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬຊ")
  if bstack11111l1l_opy_ and isinstance(bstack11111l1l_opy_, str):
    bstack11111l1l_opy_ = eval(bstack11111l1l_opy_)
  CONFIG = bstack11111l1l_opy_[bstack1lllll1l_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭຋")]
  bstack11lll1111_opy_ = bstack11111l1l_opy_[bstack1lllll1l_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨຌ")]
  bstack1l1111l11l_opy_ = bstack11111l1l_opy_[bstack1lllll1l_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪຍ")]
  bstack11ll1l1l1l_opy_ = bstack11111l1l_opy_[bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬຎ")]
  bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫຏ"), bstack11ll1l1l1l_opy_)
  os.environ[bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ຐ")] = bstack111l1ll1ll_opy_
  os.environ[bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࠫຑ")] = json.dumps(CONFIG)
  os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡎࡕࡃࡡࡘࡖࡑ࠭ຒ")] = bstack11lll1111_opy_
  os.environ[bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨຓ")] = str(bstack1l1111l11l_opy_)
  os.environ[bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡎࡘࡋࡎࡔࠧດ")] = str(True)
  if bstack111ll1l111_opy_(arg, [bstack1lllll1l_opy_ (u"ࠩ࠰ࡲࠬຕ"), bstack1lllll1l_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫຖ")]) != -1:
    os.environ[bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡆࡘࡁࡍࡎࡈࡐࠬທ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack11ll11l1l_opy_)
    return
  bstack1l1lll1l11_opy_()
  global bstack1lll11ll1l_opy_
  global bstack11111ll1l1_opy_
  global bstack1l1l1l111_opy_
  global bstack1ll111l1l1_opy_
  global bstack1l1l1l11l1_opy_
  global bstack11111ll11_opy_
  global bstack11l11l1ll1_opy_
  arg.append(bstack1lllll1l_opy_ (u"ࠧ࠳ࡗࠣຘ"))
  arg.append(bstack1lllll1l_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡀࡍࡰࡦࡸࡰࡪࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡪ࡯ࡳࡳࡷࡺࡥࡥ࠼ࡳࡽࡹ࡫ࡳࡵ࠰ࡓࡽࡹ࡫ࡳࡵ࡙ࡤࡶࡳ࡯࡮ࡨࠤນ"))
  arg.append(bstack1lllll1l_opy_ (u"ࠢ࠮࡙ࠥບ"))
  arg.append(bstack1lllll1l_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥ࠻ࡖ࡫ࡩࠥ࡮࡯ࡰ࡭࡬ࡱࡵࡲࠢປ"))
  global bstack1l11ll1ll1_opy_
  global bstack1lll1l1lll_opy_
  global bstack1l11l11ll_opy_
  global bstack11l1l1llll_opy_
  global bstack1ll11l11l_opy_
  global bstack1llll1l1ll_opy_
  global bstack1l1ll1lll_opy_
  global bstack1111l11lll_opy_
  global bstack1ll1ll1l11_opy_
  global bstack1lll1ll111_opy_
  global bstack11111l1lll_opy_
  global bstack1lllllllll_opy_
  global bstack11111l11l1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l11ll1ll1_opy_ = webdriver.Remote.__init__
    bstack1lll1l1lll_opy_ = WebDriver.quit
    bstack1111l11lll_opy_ = WebDriver.close
    bstack1ll1ll1l11_opy_ = WebDriver.get
    bstack1l11l11ll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1l1l1l11ll_opy_(CONFIG) and bstack111ll1111l_opy_():
    if bstack1l111llll1_opy_() < version.parse(bstack1l1l1l1lll_opy_):
      logger.error(bstack1lllllll11_opy_.format(bstack1l111llll1_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1lllll1l_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪຜ")) and callable(getattr(RemoteConnection, bstack1lllll1l_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫຝ"))):
          bstack1lll1ll111_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1lll1ll111_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack11lll11l1_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack11111l1lll_opy_ = Config.getoption
    from _pytest import runner
    bstack1lllllllll_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1111l111_opy_)
  try:
    from pytest_bdd import reporting
    bstack11111l11l1_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1lllll1l_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬພ"))
  bstack1l1l1l111_opy_ = CONFIG.get(bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩຟ"), {}).get(bstack1lllll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨຠ"))
  bstack11l11l1ll1_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack11111l1l1_opy_():
      bstack1l11l1lll_opy_.invoke(Events.CONNECT, bstack111lllllll_opy_())
    platform_index = int(os.environ.get(bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧມ"), bstack1lllll1l_opy_ (u"ࠨ࠲ࠪຢ")))
  else:
    bstack11lllll1l_opy_(bstack1l11111lll_opy_)
  os.environ[bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪຣ")] = CONFIG[bstack1lllll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ຤")]
  os.environ[bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧລ")] = CONFIG[bstack1lllll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ຦")]
  os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩວ")] = bstack11ll1l1l1l_opy_.__str__()
  from _pytest.config import main as bstack1lll1ll1l1_opy_
  bstack1l11ll11l_opy_ = []
  try:
    exit_code = bstack1lll1ll1l1_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack11ll1ll1ll_opy_()
    if bstack1lllll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫຨ") in multiprocessing.current_process().__dict__.keys():
      for bstack11l1l1l11l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l11ll11l_opy_.append(bstack11l1l1l11l_opy_)
    try:
      bstack111ll11ll1_opy_ = (bstack1l11ll11l_opy_, int(exit_code))
      bstack11l1111111_opy_.append(bstack111ll11ll1_opy_)
    except:
      bstack11l1111111_opy_.append((bstack1l11ll11l_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1l11ll11l_opy_.append({bstack1lllll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ຩ"): bstack1lllll1l_opy_ (u"ࠩࡓࡶࡴࡩࡥࡴࡵࠣࠫສ") + os.environ.get(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪຫ")), bstack1lllll1l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪຬ"): traceback.format_exc(), bstack1lllll1l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫອ"): int(os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ຮ")))})
    bstack11l1111111_opy_.append((bstack1l11ll11l_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack1lllll1l_opy_ (u"ࠢࡳࡧࡷࡶ࡮࡫ࡳࠣຯ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack11ll1l1ll1_opy_ = e.__class__.__name__
    print(bstack1lllll1l_opy_ (u"ࠣࠧࡶ࠾ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠥࡨࡥࡩࡣࡹࡩࠥࡺࡥࡴࡶࠣࠩࡸࠨະ") % (bstack11ll1l1ll1_opy_, e))
    return 1
def bstack11l1l11111_opy_(arg):
  global bstack1ll111ll11_opy_
  bstack11lllll1l_opy_(bstack11l1lll11_opy_)
  os.environ[bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪັ")] = str(bstack1l1111l11l_opy_)
  retries = bstack111l11ll_opy_.bstack1llllllll_opy_(CONFIG)
  status_code = 0
  if bstack111l11ll_opy_.bstack1111lll1_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack11l1l1l11_opy_
    status_code = bstack11l1l1l11_opy_(arg)
  if status_code != 0:
    bstack1ll111ll11_opy_ = status_code
def bstack1llllll11l_opy_():
  logger.info(bstack1ll111l11_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1lllll1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩາ"), help=bstack1lllll1l_opy_ (u"ࠫࡌ࡫࡮ࡦࡴࡤࡸࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡩ࡯࡯ࡨ࡬࡫ࠬຳ"))
  parser.add_argument(bstack1lllll1l_opy_ (u"ࠬ࠳ࡵࠨິ"), bstack1lllll1l_opy_ (u"࠭࠭࠮ࡷࡶࡩࡷࡴࡡ࡮ࡧࠪີ"), help=bstack1lllll1l_opy_ (u"࡚ࠧࡱࡸࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡺࡹࡥࡳࡰࡤࡱࡪ࠭ຶ"))
  parser.add_argument(bstack1lllll1l_opy_ (u"ࠨ࠯࡮ࠫື"), bstack1lllll1l_opy_ (u"ࠩ࠰࠱ࡰ࡫ࡹࠨຸ"), help=bstack1lllll1l_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡢࡥࡦࡩࡸࡹࠠ࡬ࡧࡼູࠫ"))
  parser.add_argument(bstack1lllll1l_opy_ (u"ࠫ࠲࡬຺ࠧ"), bstack1lllll1l_opy_ (u"ࠬ࠳࠭ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪົ"), help=bstack1lllll1l_opy_ (u"࡙࠭ࡰࡷࡵࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬຼ"))
  bstack1l1l1111l_opy_ = parser.parse_args()
  try:
    bstack11l1111l11_opy_ = bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡧࡦࡰࡨࡶ࡮ࡩ࠮ࡺ࡯࡯࠲ࡸࡧ࡭ࡱ࡮ࡨࠫຽ")
    if bstack1l1l1111l_opy_.framework and bstack1l1l1111l_opy_.framework not in (bstack1lllll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ຾"), bstack1lllll1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ຿")):
      bstack11l1111l11_opy_ = bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯࠳ࡿ࡭࡭࠰ࡶࡥࡲࡶ࡬ࡦࠩເ")
    bstack111ll11ll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1111l11_opy_)
    bstack1ll1llllll_opy_ = open(bstack111ll11ll_opy_, bstack1lllll1l_opy_ (u"ࠫࡷ࠭ແ"))
    bstack111ll1l11l_opy_ = bstack1ll1llllll_opy_.read()
    bstack1ll1llllll_opy_.close()
    if bstack1l1l1111l_opy_.username:
      bstack111ll1l11l_opy_ = bstack111ll1l11l_opy_.replace(bstack1lllll1l_opy_ (u"ࠬ࡟ࡏࡖࡔࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬໂ"), bstack1l1l1111l_opy_.username)
    if bstack1l1l1111l_opy_.key:
      bstack111ll1l11l_opy_ = bstack111ll1l11l_opy_.replace(bstack1lllll1l_opy_ (u"࡙࠭ࡐࡗࡕࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨໃ"), bstack1l1l1111l_opy_.key)
    if bstack1l1l1111l_opy_.framework:
      bstack111ll1l11l_opy_ = bstack111ll1l11l_opy_.replace(bstack1lllll1l_opy_ (u"࡚ࠧࡑࡘࡖࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨໄ"), bstack1l1l1111l_opy_.framework)
    file_name = bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫ໅")
    file_path = os.path.abspath(file_name)
    bstack1l111l1l1_opy_ = open(file_path, bstack1lllll1l_opy_ (u"ࠩࡺࠫໆ"))
    bstack1l111l1l1_opy_.write(bstack111ll1l11l_opy_)
    bstack1l111l1l1_opy_.close()
    logger.info(bstack11l1l11l1_opy_)
    try:
      os.environ[bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ໇")] = bstack1l1l1111l_opy_.framework if bstack1l1l1111l_opy_.framework != None else bstack1lllll1l_opy_ (u"່ࠦࠧ")
      config = yaml.safe_load(bstack111ll1l11l_opy_)
      config[bstack1lllll1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩ້ࠬ")] = bstack1lllll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠳ࡳࡦࡶࡸࡴ໊ࠬ")
      bstack11l111l1l_opy_(bstack11l111l111_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll1ll111_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1ll1l111l_opy_.format(str(e)))
def bstack11l111l1l_opy_(bstack111l111lll_opy_, config, bstack1l1lll11l1_opy_={}):
  global bstack11ll1l1l1l_opy_
  global bstack1111ll111_opy_
  global bstack1lll1ll1l_opy_
  if not config:
    return
  bstack1ll111ll1l_opy_ = bstack1l111ll11_opy_ if not bstack11ll1l1l1l_opy_ else (
    bstack11l111llll_opy_ if bstack1lllll1l_opy_ (u"ࠧࡢࡲࡳ໋ࠫ") in config else (
        bstack11lll1llll_opy_ if config.get(bstack1lllll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ໌")) else bstack1l111l11ll_opy_
    )
)
  bstack111l11l1l1_opy_ = False
  bstack11ll1ll1l1_opy_ = False
  if bstack11ll1l1l1l_opy_ is True:
      if bstack1lllll1l_opy_ (u"ࠩࡤࡴࡵ࠭ໍ") in config:
          bstack111l11l1l1_opy_ = True
      else:
          bstack11ll1ll1l1_opy_ = True
  bstack111l1lll1l_opy_ = bstack1l1ll11lll_opy_.bstack1l11111ll_opy_(config, bstack1111ll111_opy_)
  bstack1l1lllll1l_opy_ = bstack11l11l1111_opy_()
  data = {
    bstack1lllll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ໎"): config[bstack1lllll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭໏")],
    bstack1lllll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ໐"): config[bstack1lllll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ໑")],
    bstack1lllll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫ໒"): bstack111l111lll_opy_,
    bstack1lllll1l_opy_ (u"ࠨࡦࡨࡸࡪࡩࡴࡦࡦࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ໓"): os.environ.get(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ໔"), bstack1111ll111_opy_),
    bstack1lllll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ໕"): bstack1ll1ll11l1_opy_,
    bstack1lllll1l_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠭໖"): bstack1ll1l11ll1_opy_(),
    bstack1lllll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ໗"): {
      bstack1lllll1l_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ໘"): str(config[bstack1lllll1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ໙")]) if bstack1lllll1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ໚") in config else bstack1lllll1l_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥ໛"),
      bstack1lllll1l_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩ࡛࡫ࡲࡴ࡫ࡲࡲࠬໜ"): sys.version,
      bstack1lllll1l_opy_ (u"ࠫࡷ࡫ࡦࡦࡴࡵࡩࡷ࠭ໝ"): bstack1111l1l1l_opy_(os.environ.get(bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧໞ"), bstack1111ll111_opy_)),
      bstack1lllll1l_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨໟ"): bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ໠"),
      bstack1lllll1l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩ໡"): bstack1ll111ll1l_opy_,
      bstack1lllll1l_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࡢࡱࡦࡶࠧ໢"): bstack111l1lll1l_opy_,
      bstack1lllll1l_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡣࡺࡻࡩࡥࠩ໣"): os.environ[bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ໤")],
      bstack1lllll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ໥"): os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ໦"), bstack1111ll111_opy_),
      bstack1lllll1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ໧"): bstack11ll1ll1l_opy_(os.environ.get(bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ໨"), bstack1111ll111_opy_)),
      bstack1lllll1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ໩"): bstack1l1lllll1l_opy_.get(bstack1lllll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ໪")),
      bstack1lllll1l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ໫"): bstack1l1lllll1l_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭໬")),
      bstack1lllll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ໭"): config[bstack1lllll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ໮")] if config[bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ໯")] else bstack1lllll1l_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥ໰"),
      bstack1lllll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ໱"): str(config[bstack1lllll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭໲")]) if bstack1lllll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ໳") in config else bstack1lllll1l_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢ໴"),
      bstack1lllll1l_opy_ (u"ࠧࡰࡵࠪ໵"): sys.platform,
      bstack1lllll1l_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪ໶"): socket.gethostname(),
      bstack1lllll1l_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ໷"): bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ໸"))
    }
  }
  if not bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ໹")) is None:
    data[bstack1lllll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ໺")][bstack1lllll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡎࡧࡷࡥࡩࡧࡴࡢࠩ໻")] = {
      bstack1lllll1l_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧ໼"): bstack1lllll1l_opy_ (u"ࠨࡷࡶࡩࡷࡥ࡫ࡪ࡮࡯ࡩࡩ࠭໽"),
      bstack1lllll1l_opy_ (u"ࠩࡶ࡭࡬ࡴࡡ࡭ࠩ໾"): bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪ໿")),
      bstack1lllll1l_opy_ (u"ࠫࡸ࡯ࡧ࡯ࡣ࡯ࡒࡺࡳࡢࡦࡴࠪༀ"): bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱࡔ࡯ࠨ༁"))
    }
  if bstack111l111lll_opy_ == bstack111ll1llll_opy_:
    data[bstack1lllll1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ༂")][bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡉ࡯࡯ࡨ࡬࡫ࠬ༃")] = bstack1111lllll1_opy_(config)
    data[bstack1lllll1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ༄")][bstack1lllll1l_opy_ (u"ࠩ࡬ࡷࡕ࡫ࡲࡤࡻࡄࡹࡹࡵࡅ࡯ࡣࡥࡰࡪࡪࠧ༅")] = percy.bstack1ll1l1ll1l_opy_
    data[bstack1lllll1l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭༆")][bstack1lllll1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡅࡹ࡮ࡲࡤࡊࡦࠪ༇")] = percy.percy_build_id
  if not bstack111l11ll_opy_.bstack11lll11ll_opy_(CONFIG):
    data[bstack1lllll1l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ༈")][bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠪ༉")] = bstack111l11ll_opy_.bstack11lll11ll_opy_(CONFIG)
  bstack1llll1ll1_opy_ = bstack1lllll1ll_opy_.bstack1111l1ll_opy_(CONFIG, logger)
  bstack111l1l1l_opy_ = bstack111l11ll_opy_.bstack1111l1ll_opy_(config=CONFIG)
  if bstack1llll1ll1_opy_ is not None and bstack111l1l1l_opy_ is not None and bstack111l1l1l_opy_.bstack1llll11ll_opy_():
    data[bstack1lllll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ༊")][bstack111l1l1l_opy_.bstack11l1l1ll1_opy_()] = bstack1llll1ll1_opy_.bstack11ll11ll1l_opy_()
  update(data[bstack1lllll1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ་")], bstack1l1lll11l1_opy_)
  try:
    response = bstack11l1l111l1_opy_(bstack1lllll1l_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ༌"), bstack1l111ll1l1_opy_(bstack111l1l11l1_opy_), data, {
      bstack1lllll1l_opy_ (u"ࠪࡥࡺࡺࡨࠨ།"): (config[bstack1lllll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭༎")], config[bstack1lllll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ༏")])
    })
    if response:
      logger.debug(bstack11l11l1l1l_opy_.format(bstack111l111lll_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1l11lll11_opy_.format(str(e)))
def bstack1111l1l1l_opy_(framework):
  return bstack1lllll1l_opy_ (u"ࠨࡻࡾ࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࡼࡿࠥ༐").format(str(framework), __version__) if framework else bstack1lllll1l_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴ࢁࡽࠣ༑").format(
    __version__)
def bstack1l1lll1l11_opy_():
  global CONFIG
  global bstack111l1ll11_opy_
  if bool(CONFIG):
    return
  try:
    bstack11ll111ll_opy_()
    logger.debug(bstack1l1l11ll1_opy_.format(str(CONFIG)))
    bstack111l1ll11_opy_ = bstack11llll111l_opy_.configure_logger(CONFIG, bstack111l1ll11_opy_)
    bstack111l1l1ll_opy_()
  except Exception as e:
    logger.error(bstack1lllll1l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࡶࡲ࠯ࠤࡪࡸࡲࡰࡴ࠽ࠤࠧ༒") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1lllll1lll_opy_
  atexit.register(bstack11l11111l_opy_)
  signal.signal(signal.SIGINT, bstack1l11l11l1_opy_)
  signal.signal(signal.SIGTERM, bstack1l11l11l1_opy_)
def bstack1lllll1lll_opy_(exctype, value, traceback):
  global bstack1111lll11l_opy_
  try:
    for driver in bstack1111lll11l_opy_:
      bstack1l1ll1l11_opy_(driver, bstack1lllll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ༓"), bstack1lllll1l_opy_ (u"ࠥࡗࡪࡹࡳࡪࡱࡱࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨ༔") + str(value))
  except Exception:
    pass
  logger.info(bstack1l1l1l11l_opy_)
  bstack1l11lll11l_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l11lll11l_opy_(message=bstack1lllll1l_opy_ (u"ࠫࠬ༕"), bstack1lllll11ll_opy_ = False):
  global CONFIG
  bstack11l11lll1_opy_ = bstack1lllll1l_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠧ༖") if bstack1lllll11ll_opy_ else bstack1lllll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ༗")
  try:
    if message:
      bstack1l1lll11l1_opy_ = {
        bstack11l11lll1_opy_ : str(message)
      }
      bstack11l111l1l_opy_(bstack111ll1llll_opy_, CONFIG, bstack1l1lll11l1_opy_)
    else:
      bstack11l111l1l_opy_(bstack111ll1llll_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack11l11lll1l_opy_.format(str(e)))
def bstack1llll1111l_opy_(bstack11ll1l1111_opy_, size):
  bstack1111ll111l_opy_ = []
  while len(bstack11ll1l1111_opy_) > size:
    bstack1ll1l1l11l_opy_ = bstack11ll1l1111_opy_[:size]
    bstack1111ll111l_opy_.append(bstack1ll1l1l11l_opy_)
    bstack11ll1l1111_opy_ = bstack11ll1l1111_opy_[size:]
  bstack1111ll111l_opy_.append(bstack11ll1l1111_opy_)
  return bstack1111ll111l_opy_
def bstack11l111111_opy_(args):
  if bstack1lllll1l_opy_ (u"ࠧ࠮࡯༘ࠪ") in args and bstack1lllll1l_opy_ (u"ࠨࡲࡧࡦ༙ࠬ") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack1l111llll_opy_, stage=STAGE.bstack1l1l11111l_opy_)
def run_on_browserstack(bstack1lll1l1l11_opy_=None, bstack11l1111111_opy_=None, bstack1ll1111ll1_opy_=False):
  global CONFIG
  global bstack11lll1111_opy_
  global bstack1l1111l11l_opy_
  global bstack1111ll111_opy_
  global bstack1lll1ll1l_opy_
  bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠩࠪ༚")
  bstack1l1l1l1l11_opy_(bstack1lll1l11l1_opy_, logger)
  if bstack1lll1l1l11_opy_ and isinstance(bstack1lll1l1l11_opy_, str):
    bstack1lll1l1l11_opy_ = eval(bstack1lll1l1l11_opy_)
  if bstack1lll1l1l11_opy_:
    CONFIG = bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪ༛")]
    bstack11lll1111_opy_ = bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬ༜")]
    bstack1l1111l11l_opy_ = bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ༝")]
    bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ༞"), bstack1l1111l11l_opy_)
    bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༟")
  bstack1lll1ll1l_opy_.set_property(bstack1lllll1l_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪ༠"), uuid4().__str__())
  logger.info(bstack1lllll1l_opy_ (u"ࠩࡖࡈࡐࠦࡲࡶࡰࠣࡷࡹࡧࡲࡵࡧࡧࠤࡼ࡯ࡴࡩࠢ࡬ࡨ࠿ࠦࠧ༡") + bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ༢")));
  logger.debug(bstack1lllll1l_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩࡃࠧ༣") + bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ༤")))
  if not bstack1ll1111ll1_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack11ll11l1l_opy_)
      return
    if sys.argv[1] == bstack1lllll1l_opy_ (u"࠭࠭࠮ࡸࡨࡶࡸ࡯࡯࡯ࠩ༥") or sys.argv[1] == bstack1lllll1l_opy_ (u"ࠧ࠮ࡸࠪ༦"):
      logger.info(bstack1lllll1l_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡑࡻࡷ࡬ࡴࡴࠠࡔࡆࡎࠤࡻࢁࡽࠨ༧").format(__version__))
      return
    if sys.argv[1] == bstack1lllll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨ༨"):
      bstack1llllll11l_opy_()
      return
  args = sys.argv
  bstack1l1lll1l11_opy_()
  global bstack1lll11ll1l_opy_
  global bstack111lllll1l_opy_
  global bstack11l11l1ll1_opy_
  global bstack11lll1l111_opy_
  global bstack11111ll1l1_opy_
  global bstack1l1l1l111_opy_
  global bstack1ll111l1l1_opy_
  global bstack1ll1ll11l_opy_
  global bstack1l1l1l11l1_opy_
  global bstack11111ll11_opy_
  global bstack1l11ll111_opy_
  bstack111lllll1l_opy_ = len(CONFIG.get(bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭༩"), []))
  if not bstack111l1ll1ll_opy_:
    if args[1] == bstack1lllll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༪") or args[1] == bstack1lllll1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭༫"):
      bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭༬")
      args = args[2:]
    elif args[1] == bstack1lllll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭༭"):
      bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ༮")
      args = args[2:]
    elif args[1] == bstack1lllll1l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༯"):
      bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ༰")
      args = args[2:]
    elif args[1] == bstack1lllll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ༱"):
      bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭༲")
      args = args[2:]
    elif args[1] == bstack1lllll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭༳"):
      bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ༴")
      args = args[2:]
    elif args[1] == bstack1lllll1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ༵"):
      bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ༶")
      args = args[2:]
    else:
      if not bstack1lllll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ༷࠭") in CONFIG or str(CONFIG[bstack1lllll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ༸")]).lower() in [bstack1lllll1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ༹ࠬ"), bstack1lllll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧ༺")]:
        bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༻")
        args = args[1:]
      elif str(CONFIG[bstack1lllll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ༼")]).lower() == bstack1lllll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ༽"):
        bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ༾")
        args = args[1:]
      elif str(CONFIG[bstack1lllll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ༿")]).lower() == bstack1lllll1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫཀ"):
        bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬཁ")
        args = args[1:]
      elif str(CONFIG[bstack1lllll1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪག")]).lower() == bstack1lllll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨགྷ"):
        bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩང")
        args = args[1:]
      elif str(CONFIG[bstack1lllll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ཅ")]).lower() == bstack1lllll1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫཆ"):
        bstack111l1ll1ll_opy_ = bstack1lllll1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬཇ")
        args = args[1:]
      else:
        os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ཈")] = bstack111l1ll1ll_opy_
        bstack1l11l1l11l_opy_(bstack111ll11lll_opy_)
  os.environ[bstack1lllll1l_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨཉ")] = bstack111l1ll1ll_opy_
  bstack1111ll111_opy_ = bstack111l1ll1ll_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1llll111l1_opy_ = bstack1l1111l11_opy_[bstack1lllll1l_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔ࠮ࡄࡇࡈࠬཊ")] if bstack111l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩཋ") and bstack11l1ll11l1_opy_() else bstack111l1ll1ll_opy_
      bstack1l11l1lll_opy_.invoke(Events.bstack1111ll1111_opy_, bstack11l1l11l11_opy_(
        sdk_version=__version__,
        path_config=bstack1111lll111_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1llll111l1_opy_,
        frameworks=[bstack1llll111l1_opy_],
        framework_versions={
          bstack1llll111l1_opy_: bstack11ll1ll1l_opy_(bstack1lllll1l_opy_ (u"ࠪࡖࡴࡨ࡯ࡵࠩཌ") if bstack111l1ll1ll_opy_ in [bstack1lllll1l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪཌྷ"), bstack1lllll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫཎ"), bstack1lllll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧཏ")] else bstack111l1ll1ll_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack1lllll1l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤཐ"), None):
        CONFIG[bstack1lllll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥད")] = cli.config.get(bstack1lllll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦདྷ"), None)
    except Exception as e:
      bstack1l11l1lll_opy_.invoke(Events.bstack1l111111ll_opy_, e.__traceback__, 1)
    if bstack1l1111l11l_opy_:
      CONFIG[bstack1lllll1l_opy_ (u"ࠥࡥࡵࡶࠢན")] = cli.config[bstack1lllll1l_opy_ (u"ࠦࡦࡶࡰࠣཔ")]
      logger.info(bstack1ll11l11l1_opy_.format(CONFIG[bstack1lllll1l_opy_ (u"ࠬࡧࡰࡱࠩཕ")]))
  else:
    bstack1l11l1lll_opy_.clear()
  global bstack11l11l1lll_opy_
  global bstack111llllll1_opy_
  if bstack1lll1l1l11_opy_:
    try:
      bstack1ll111ll1_opy_ = datetime.datetime.now()
      os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨབ")] = bstack111l1ll1ll_opy_
      bstack11l111l1l_opy_(bstack1111lllll_opy_, CONFIG)
      cli.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠢࡩࡶࡷࡴ࠿ࡹࡤ࡬ࡡࡷࡩࡸࡺ࡟ࡢࡶࡷࡩࡲࡶࡴࡦࡦࠥབྷ"), datetime.datetime.now() - bstack1ll111ll1_opy_)
    except Exception as e:
      logger.debug(bstack1l11l11ll1_opy_.format(str(e)))
  global bstack1l11ll1ll1_opy_
  global bstack1lll1l1lll_opy_
  global bstack1ll1111l1l_opy_
  global bstack1l1l1lll1_opy_
  global bstack11ll111l1l_opy_
  global bstack11l11llll_opy_
  global bstack11l1l1llll_opy_
  global bstack1ll11l11l_opy_
  global bstack111lll111l_opy_
  global bstack1llll1l1ll_opy_
  global bstack1l1ll1lll_opy_
  global bstack1111l11lll_opy_
  global bstack11l11ll1l_opy_
  global bstack1l11l1llll_opy_
  global bstack1ll1ll1l11_opy_
  global bstack1lll1ll111_opy_
  global bstack11111l1lll_opy_
  global bstack1lllllllll_opy_
  global bstack1lll11l11l_opy_
  global bstack11111l11l1_opy_
  global bstack1l11l11ll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l11ll1ll1_opy_ = webdriver.Remote.__init__
    bstack1lll1l1lll_opy_ = WebDriver.quit
    bstack1111l11lll_opy_ = WebDriver.close
    bstack1ll1ll1l11_opy_ = WebDriver.get
    bstack1l11l11ll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack11l11l1lll_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1ll11l1ll_opy_
    bstack111llllll1_opy_ = bstack1ll11l1ll_opy_()
  except Exception as e:
    pass
  try:
    global bstack1l111l1l11_opy_
    from QWeb.keywords import browser
    bstack1l111l1l11_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1l1l1l11ll_opy_(CONFIG) and bstack111ll1111l_opy_():
    if bstack1l111llll1_opy_() < version.parse(bstack1l1l1l1lll_opy_):
      logger.error(bstack1lllllll11_opy_.format(bstack1l111llll1_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1lllll1l_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩམ")) and callable(getattr(RemoteConnection, bstack1lllll1l_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪཙ"))):
          RemoteConnection._get_proxy_url = bstack11111l1ll1_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack11111l1ll1_opy_
      except Exception as e:
        logger.error(bstack11lll11l1_opy_.format(str(e)))
  if not CONFIG.get(bstack1lllll1l_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬཚ"), False) and not bstack1lll1l1l11_opy_:
    logger.info(bstack1l11111l11_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack1lllll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨཛ") in CONFIG and str(CONFIG[bstack1lllll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩཛྷ")]).lower() != bstack1lllll1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬཝ"):
      bstack1l1ll1l1ll_opy_()
    elif bstack111l1ll1ll_opy_ != bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧཞ") or (bstack111l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨཟ") and not bstack1lll1l1l11_opy_):
      bstack11l1ll1l1l_opy_()
  if (bstack111l1ll1ll_opy_ in [bstack1lllll1l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨའ"), bstack1lllll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩཡ"), bstack1lllll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬར")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack111111ll1_opy_
        bstack11l11llll_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack11ll111ll1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack11ll111l1l_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack11llll1l11_opy_ + str(e))
    except Exception as e:
      bstack1l1ll11ll1_opy_(e, bstack11ll111ll1_opy_)
    if bstack111l1ll1ll_opy_ != bstack1lllll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ལ"):
      bstack1l111l11l1_opy_()
    bstack1ll1111l1l_opy_ = Output.start_test
    bstack1l1l1lll1_opy_ = Output.end_test
    bstack11l1l1llll_opy_ = TestStatus.__init__
    bstack111lll111l_opy_ = pabot._run
    bstack1llll1l1ll_opy_ = QueueItem.__init__
    bstack1l1ll1lll_opy_ = pabot._create_command_for_execution
    bstack1lll11l11l_opy_ = pabot._report_results
  if bstack111l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ཤ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l1ll11ll1_opy_(e, bstack1l11l1ll1l_opy_)
    bstack11l11ll1l_opy_ = Runner.run_hook
    bstack1l11l1llll_opy_ = Step.run
  if bstack111l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧཥ"):
    try:
      from _pytest.config import Config
      bstack11111l1lll_opy_ = Config.getoption
      from _pytest import runner
      bstack1lllllllll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1111l111_opy_)
    try:
      from pytest_bdd import reporting
      bstack11111l11l1_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1lllll1l_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩས"))
  try:
    framework_name = bstack1lllll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨཧ") if bstack111l1ll1ll_opy_ in [bstack1lllll1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩཨ"), bstack1lllll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪཀྵ"), bstack1lllll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ཪ")] else bstack1111ll1l1l_opy_(bstack111l1ll1ll_opy_)
    bstack1l111l1111_opy_ = {
      bstack1lllll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠧཫ"): bstack1lllll1l_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩཬ") if bstack111l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ཭") and bstack11l1ll11l1_opy_() else framework_name,
      bstack1lllll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭཮"): bstack11ll1ll1l_opy_(framework_name),
      bstack1lllll1l_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ཯"): __version__,
      bstack1lllll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡶࡵࡨࡨࠬ཰"): bstack111l1ll1ll_opy_
    }
    if bstack111l1ll1ll_opy_ in bstack11llllllll_opy_ + bstack111l1lllll_opy_:
      if bstack1111ll1l_opy_.bstack111ll111ll_opy_(CONFIG):
        if bstack1lllll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷཱࠬ") in CONFIG:
          os.environ[bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒིࠧ")] = os.getenv(bstack1lllll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨཱི"), json.dumps(CONFIG[bstack1lllll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨུ")]))
          CONFIG[bstack1lllll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴཱུࠩ")].pop(bstack1lllll1l_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨྲྀ"), None)
          CONFIG[bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫཷ")].pop(bstack1lllll1l_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪླྀ"), None)
        bstack1l111l1111_opy_[bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ཹ")] = {
          bstack1lllll1l_opy_ (u"ࠧ࡯ࡣࡰࡩེࠬ"): bstack1lllll1l_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ཻࠪ"),
          bstack1lllll1l_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰོࠪ"): str(bstack1l111llll1_opy_())
        }
    if bstack111l1ll1ll_opy_ not in [bstack1lllll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ཽࠫ")] and not cli.is_running():
      bstack1llll11ll1_opy_, bstack1lll11l111_opy_ = bstack1ll1l1l1_opy_.launch(CONFIG, bstack1l111l1111_opy_)
      if bstack1lll11l111_opy_.get(bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫཾ")) is not None and bstack1111ll1l_opy_.bstack111l1l11l_opy_(CONFIG) is None:
        value = bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬཿ")].get(bstack1lllll1l_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹྀࠧ"))
        if value is not None:
            CONFIG[bstack1lllll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿཱྀࠧ")] = value
        else:
          logger.debug(bstack1lllll1l_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡩࡧࡴࡢࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠨྂ"))
  except Exception as e:
    logger.debug(bstack11lll1ll1_opy_.format(bstack1lllll1l_opy_ (u"ࠩࡗࡩࡸࡺࡈࡶࡤࠪྃ"), str(e)))
  if bstack111l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ྄ࠪ"):
    bstack11l11l1ll1_opy_ = True
    if bstack1lll1l1l11_opy_ and bstack1ll1111ll1_opy_:
      bstack1l1l1l111_opy_ = CONFIG.get(bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ྅"), {}).get(bstack1lllll1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ྆"))
      bstack11lllll1l_opy_(bstack1111lll1ll_opy_)
    elif bstack1lll1l1l11_opy_:
      bstack1l1l1l111_opy_ = CONFIG.get(bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ྇"), {}).get(bstack1lllll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩྈ"))
      global bstack1111lll11l_opy_
      try:
        if bstack11l111111_opy_(bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྉ")]) and multiprocessing.current_process().name == bstack1lllll1l_opy_ (u"ࠩ࠳ࠫྊ"):
          bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྋ")].remove(bstack1lllll1l_opy_ (u"ࠫ࠲ࡳࠧྌ"))
          bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྍ")].remove(bstack1lllll1l_opy_ (u"࠭ࡰࡥࡤࠪྎ"))
          bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྏ")] = bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྐ")][0]
          with open(bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྑ")], bstack1lllll1l_opy_ (u"ࠪࡶࠬྒ")) as f:
            file_content = f.read()
          bstack1l11llllll_opy_ = bstack1lllll1l_opy_ (u"ࠦࠧࠨࡦࡳࡱࡰࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡷࡩࡱࠠࡪ࡯ࡳࡳࡷࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧ࠾ࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫ࠨࡼࡿࠬ࠿ࠥ࡬ࡲࡰ࡯ࠣࡴࡩࡨࠠࡪ࡯ࡳࡳࡷࡺࠠࡑࡦࡥ࠿ࠥࡵࡧࡠࡦࡥࠤࡂࠦࡐࡥࡤ࠱ࡨࡴࡥࡢࡳࡧࡤ࡯ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡧࡩ࡫ࠦ࡭ࡰࡦࡢࡦࡷ࡫ࡡ࡬ࠪࡶࡩࡱ࡬ࠬࠡࡣࡵ࡫࠱ࠦࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠢࡀࠤ࠵࠯࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡳࡻ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡦࡸࡧࠡ࠿ࠣࡷࡹࡸࠨࡪࡰࡷࠬࡦࡸࡧࠪ࠭࠴࠴࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡪࡾࡣࡦࡲࡷࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡢࡵࠣࡩ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡰࡢࡵࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡲ࡫ࡤࡪࡢࠩࡵࡨࡰ࡫࠲ࡡࡳࡩ࠯ࡸࡪࡳࡰࡰࡴࡤࡶࡾ࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡔࡩࡨ࠮ࡥࡱࡢࡦࠥࡃࠠ࡮ࡱࡧࡣࡧࡸࡥࡢ࡭ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡥࡤ࠱ࡨࡴࡥࡢࡳࡧࡤ࡯ࠥࡃࠠ࡮ࡱࡧࡣࡧࡸࡥࡢ࡭ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡥࡤࠫ࠭࠳ࡹࡥࡵࡡࡷࡶࡦࡩࡥࠩࠫ࡟ࡲࠧࠨࠢྒྷ").format(str(bstack1lll1l1l11_opy_))
          bstack1l11l111l1_opy_ = bstack1l11llllll_opy_ + file_content
          bstack1ll1l1111l_opy_ = bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྔ")] + bstack1lllll1l_opy_ (u"࠭࡟ࡣࡵࡷࡥࡨࡱ࡟ࡵࡧࡰࡴ࠳ࡶࡹࠨྕ")
          with open(bstack1ll1l1111l_opy_, bstack1lllll1l_opy_ (u"ࠧࡸࠩྖ")):
            pass
          with open(bstack1ll1l1111l_opy_, bstack1lllll1l_opy_ (u"ࠣࡹ࠮ࠦྗ")) as f:
            f.write(bstack1l11l111l1_opy_)
          import subprocess
          process_data = subprocess.run([bstack1lllll1l_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࠤ྘"), bstack1ll1l1111l_opy_])
          if os.path.exists(bstack1ll1l1111l_opy_):
            os.unlink(bstack1ll1l1111l_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack11l111111_opy_(bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྙ")]):
            bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྚ")].remove(bstack1lllll1l_opy_ (u"ࠬ࠳࡭ࠨྛ"))
            bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྜ")].remove(bstack1lllll1l_opy_ (u"ࠧࡱࡦࡥࠫྜྷ"))
            bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྞ")] = bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྟ")][0]
          bstack11lllll1l_opy_(bstack1111lll1ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྠ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1lllll1l_opy_ (u"ࠫࡤࡥ࡮ࡢ࡯ࡨࡣࡤ࠭ྡ")] = bstack1lllll1l_opy_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧྡྷ")
          mod_globals[bstack1lllll1l_opy_ (u"࠭࡟ࡠࡨ࡬ࡰࡪࡥ࡟ࠨྣ")] = os.path.abspath(bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྤ")])
          exec(open(bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྥ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1lllll1l_opy_ (u"ࠩࡆࡥࡺ࡭ࡨࡵࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠩྦ").format(str(e)))
          for driver in bstack1111lll11l_opy_:
            bstack11l1111111_opy_.append({
              bstack1lllll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨྦྷ"): bstack1lll1l1l11_opy_[bstack1lllll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྨ")],
              bstack1lllll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫྩ"): str(e),
              bstack1lllll1l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬྪ"): multiprocessing.current_process().name
            })
            bstack1l1ll1l11_opy_(driver, bstack1lllll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧྫ"), bstack1lllll1l_opy_ (u"ࠣࡕࡨࡷࡸ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦྫྷ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1111lll11l_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1l1111l11l_opy_, CONFIG, logger)
      bstack1ll1ll1ll1_opy_()
      bstack11111l111l_opy_()
      percy.bstack1111llll11_opy_()
      bstack11111l1l_opy_ = {
        bstack1lllll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྭ"): args[0],
        bstack1lllll1l_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪྮ"): CONFIG,
        bstack1lllll1l_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬྯ"): bstack11lll1111_opy_,
        bstack1lllll1l_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧྰ"): bstack1l1111l11l_opy_
      }
      if bstack1lllll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩྱ") in CONFIG:
        bstack11l1ll11l_opy_ = bstack1l111l11l_opy_(args, logger, CONFIG, bstack11ll1l1l1l_opy_, bstack111lllll1l_opy_)
        bstack1ll1ll11l_opy_ = bstack11l1ll11l_opy_.bstack1lll1lll1_opy_(run_on_browserstack, bstack11111l1l_opy_, bstack11l111111_opy_(args))
      else:
        if bstack11l111111_opy_(args):
          bstack11111l1l_opy_[bstack1lllll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྲ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack11111l1l_opy_,))
          test.start()
          test.join()
        else:
          bstack11lllll1l_opy_(bstack1111lll1ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1lllll1l_opy_ (u"ࠨࡡࡢࡲࡦࡳࡥࡠࡡࠪླ")] = bstack1lllll1l_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫྴ")
          mod_globals[bstack1lllll1l_opy_ (u"ࠪࡣࡤ࡬ࡩ࡭ࡧࡢࡣࠬྵ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack111l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪྶ") or bstack111l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫྷ"):
    percy.init(bstack1l1111l11l_opy_, CONFIG, logger)
    percy.bstack1111llll11_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l1ll11ll1_opy_(e, bstack11ll111ll1_opy_)
    bstack1ll1ll1ll1_opy_()
    bstack11lllll1l_opy_(bstack111llll11l_opy_)
    if bstack11ll1l1l1l_opy_:
      bstack11l1ll11ll_opy_(bstack111llll11l_opy_, args)
      if bstack1lllll1l_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫྸ") in args:
        i = args.index(bstack1lllll1l_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬྐྵ"))
        args.pop(i)
        args.pop(i)
      if bstack1lllll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫྺ") not in CONFIG:
        CONFIG[bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྻ")] = [{}]
        bstack111lllll1l_opy_ = 1
      if bstack1lll11ll1l_opy_ == 0:
        bstack1lll11ll1l_opy_ = 1
      args.insert(0, str(bstack1lll11ll1l_opy_))
      args.insert(0, str(bstack1lllll1l_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨྼ")))
    if bstack1ll1l1l1_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack11l111lll_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack11lll1l11_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1lllll1l_opy_ (u"ࠦࡗࡕࡂࡐࡖࡢࡓࡕ࡚ࡉࡐࡐࡖࠦ྽"),
        ).parse_args(bstack11l111lll_opy_)
        bstack11l111111l_opy_ = args.index(bstack11l111lll_opy_[0]) if len(bstack11l111lll_opy_) > 0 else len(args)
        args.insert(bstack11l111111l_opy_, str(bstack1lllll1l_opy_ (u"ࠬ࠳࠭࡭࡫ࡶࡸࡪࡴࡥࡳࠩ྾")))
        args.insert(bstack11l111111l_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1lllll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡲࡰࡤࡲࡸࡤࡲࡩࡴࡶࡨࡲࡪࡸ࠮ࡱࡻࠪ྿"))))
        if bstack111l11ll_opy_.bstack1111lll1_opy_(CONFIG):
          args.insert(bstack11l111111l_opy_, str(bstack1lllll1l_opy_ (u"ࠧ࠮࠯࡯࡭ࡸࡺࡥ࡯ࡧࡵࠫ࿀")))
          args.insert(bstack11l111111l_opy_ + 1, str(bstack1lllll1l_opy_ (u"ࠨࡔࡨࡸࡷࡿࡆࡢ࡫࡯ࡩࡩࡀࡻࡾࠩ࿁").format(bstack111l11ll_opy_.bstack1llllllll_opy_(CONFIG))))
        if bstack1111l11l1l_opy_(os.environ.get(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠧ࿂"))) and str(os.environ.get(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧ࿃"), bstack1lllll1l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ࿄"))) != bstack1lllll1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ࿅"):
          for bstack11l11l1l1_opy_ in bstack11lll1l11_opy_:
            args.remove(bstack11l11l1l1_opy_)
          test_files = os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕ࿆ࠪ")).split(bstack1lllll1l_opy_ (u"ࠧ࠭ࠩ࿇"))
          for bstack111llll1l_opy_ in test_files:
            args.append(bstack111llll1l_opy_)
      except Exception as e:
        logger.error(bstack1lllll1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡡࡵࡶࡤࡧ࡭࡯࡮ࡨࠢ࡯࡭ࡸࡺࡥ࡯ࡧࡵࠤ࡫ࡵࡲࠡࡽࢀ࠲ࠥࡋࡲࡳࡱࡵࠤ࠲ࠦࡻࡾࠤ࿈").format(bstack1111ll1ll_opy_, e))
    pabot.main(args)
  elif bstack111l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ࿉"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l1ll11ll1_opy_(e, bstack11ll111ll1_opy_)
    for a in args:
      if bstack1lllll1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙ࠩ࿊") in a:
        bstack11111ll1l1_opy_ = int(a.split(bstack1lllll1l_opy_ (u"ࠫ࠿࠭࿋"))[1])
      if bstack1lllll1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡉࡋࡆࡍࡑࡆࡅࡑࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩ࿌") in a:
        bstack1l1l1l111_opy_ = str(a.split(bstack1lllll1l_opy_ (u"࠭࠺ࠨ࿍"))[1])
      if bstack1lllll1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙ࠧ࿎") in a:
        bstack1ll111l1l1_opy_ = str(a.split(bstack1lllll1l_opy_ (u"ࠨ࠼ࠪ࿏"))[1])
    bstack1l1ll1l111_opy_ = None
    if bstack1lllll1l_opy_ (u"ࠩ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠨ࿐") in args:
      i = args.index(bstack1lllll1l_opy_ (u"ࠪ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠩ࿑"))
      args.pop(i)
      bstack1l1ll1l111_opy_ = args.pop(i)
    if bstack1l1ll1l111_opy_ is not None:
      global bstack1l1llll1l_opy_
      bstack1l1llll1l_opy_ = bstack1l1ll1l111_opy_
    bstack11lllll1l_opy_(bstack111llll11l_opy_)
    run_cli(args)
    if bstack1lllll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨ࿒") in multiprocessing.current_process().__dict__.keys():
      for bstack11l1l1l11l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11l1111111_opy_.append(bstack11l1l1l11l_opy_)
  elif bstack111l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ࿓"):
    bstack1l1llll11_opy_ = bstack111ll11l_opy_(args, logger, CONFIG, bstack11ll1l1l1l_opy_)
    bstack1l1llll11_opy_.bstack111l1lll_opy_()
    bstack1ll1ll1ll1_opy_()
    bstack11lll1l111_opy_ = True
    bstack11111ll11_opy_ = bstack1l1llll11_opy_.bstack1111111l_opy_()
    bstack1l1llll11_opy_.bstack11111l1l_opy_(bstack1l1l1l1l1l_opy_)
    bstack1l1llll11_opy_.bstack1lll1l1l1_opy_()
    bstack1l111l111_opy_(bstack111l1ll1ll_opy_, CONFIG, bstack1l1llll11_opy_.bstack11111lll_opy_())
    bstack1l1lll111l_opy_ = bstack1l1llll11_opy_.bstack1lll1lll1_opy_(bstack11l11ll1l1_opy_, {
      bstack1lllll1l_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ࿔"): bstack11lll1111_opy_,
      bstack1lllll1l_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ࿕"): bstack1l1111l11l_opy_,
      bstack1lllll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ࿖"): bstack11ll1l1l1l_opy_
    })
    try:
      bstack1l11ll11l_opy_, bstack1lll1ll11l_opy_ = map(list, zip(*bstack1l1lll111l_opy_))
      bstack1l1l1l11l1_opy_ = bstack1l11ll11l_opy_[0]
      for status_code in bstack1lll1ll11l_opy_:
        if status_code != 0:
          bstack1l11ll111_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1lllll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡡࡷࡧࠣࡩࡷࡸ࡯ࡳࡵࠣࡥࡳࡪࠠࡴࡶࡤࡸࡺࡹࠠࡤࡱࡧࡩ࠳ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࠽ࠤࢀࢃࠢ࿗").format(str(e)))
  elif bstack111l1ll1ll_opy_ == bstack1lllll1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ࿘"):
    try:
      from behave.__main__ import main as bstack11l1l1l11_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l1ll11ll1_opy_(e, bstack1l11l1ll1l_opy_)
    bstack1ll1ll1ll1_opy_()
    bstack11lll1l111_opy_ = True
    bstack1lll11lll_opy_ = 1
    if bstack1lllll1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ࿙") in CONFIG:
      bstack1lll11lll_opy_ = CONFIG[bstack1lllll1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ࿚")]
    if bstack1lllll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ࿛") in CONFIG:
      bstack1111llllll_opy_ = int(bstack1lll11lll_opy_) * int(len(CONFIG[bstack1lllll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿜")]))
    else:
      bstack1111llllll_opy_ = int(bstack1lll11lll_opy_)
    config = Configuration(args)
    bstack111l11111_opy_ = config.paths
    if len(bstack111l11111_opy_) == 0:
      import glob
      pattern = bstack1lllll1l_opy_ (u"ࠨࠬ࠭࠳࠯࠴ࡦࡦࡣࡷࡹࡷ࡫ࠧ࿝")
      bstack11llll11l1_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11llll11l1_opy_)
      config = Configuration(args)
      bstack111l11111_opy_ = config.paths
    bstack1lll11ll1_opy_ = [os.path.normpath(item) for item in bstack111l11111_opy_]
    bstack111ll1ll1_opy_ = [os.path.normpath(item) for item in args]
    bstack1l11l11l11_opy_ = [item for item in bstack111ll1ll1_opy_ if item not in bstack1lll11ll1_opy_]
    import platform as pf
    if pf.system().lower() == bstack1lllll1l_opy_ (u"ࠩࡺ࡭ࡳࡪ࡯ࡸࡵࠪ࿞"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1lll11ll1_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11ll1llll1_opy_)))
                    for bstack11ll1llll1_opy_ in bstack1lll11ll1_opy_]
    bstack1lll1l11l_opy_ = []
    for spec in bstack1lll11ll1_opy_:
      bstack1111llll_opy_ = []
      bstack1111llll_opy_ += bstack1l11l11l11_opy_
      bstack1111llll_opy_.append(spec)
      bstack1lll1l11l_opy_.append(bstack1111llll_opy_)
    execution_items = []
    for bstack1111llll_opy_ in bstack1lll1l11l_opy_:
      if bstack1lllll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭࿟") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack1lllll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ࿠")]):
          item = {}
          item[bstack1lllll1l_opy_ (u"ࠬࡧࡲࡨࠩ࿡")] = bstack1lllll1l_opy_ (u"࠭ࠠࠨ࿢").join(bstack1111llll_opy_)
          item[bstack1lllll1l_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭࿣")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack1lllll1l_opy_ (u"ࠨࡣࡵ࡫ࠬ࿤")] = bstack1lllll1l_opy_ (u"ࠩࠣࠫ࿥").join(bstack1111llll_opy_)
        item[bstack1lllll1l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ࿦")] = 0
        execution_items.append(item)
    bstack11llllll1l_opy_ = bstack1llll1111l_opy_(execution_items, bstack1111llllll_opy_)
    for execution_item in bstack11llllll1l_opy_:
      bstack111l1ll1_opy_ = []
      for item in execution_item:
        bstack111l1ll1_opy_.append(bstack1l11111l1_opy_(name=str(item[bstack1lllll1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ࿧")]),
                                             target=bstack11l1l11111_opy_,
                                             args=(item[bstack1lllll1l_opy_ (u"ࠬࡧࡲࡨࠩ࿨")],)))
      for t in bstack111l1ll1_opy_:
        t.start()
      for t in bstack111l1ll1_opy_:
        t.join()
  else:
    bstack1l11l1l11l_opy_(bstack111ll11lll_opy_)
  if not bstack1lll1l1l11_opy_:
    bstack1l1111llll_opy_()
    if(bstack111l1ll1ll_opy_ in [bstack1lllll1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭࿩"), bstack1lllll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ࿪")]):
      bstack1ll1l1l1l_opy_()
  bstack11llll111l_opy_.bstack11ll11l1ll_opy_()
def browserstack_initialize(bstack11l11111ll_opy_=None):
  logger.info(bstack1lllll1l_opy_ (u"ࠨࡔࡸࡲࡳ࡯࡮ࡨࠢࡖࡈࡐࠦࡷࡪࡶ࡫ࠤࡦࡸࡧࡴ࠼ࠣࠫ࿫") + str(bstack11l11111ll_opy_))
  run_on_browserstack(bstack11l11111ll_opy_, None, True)
@measure(event_name=EVENTS.bstack111ll1111_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1l1111llll_opy_():
  global CONFIG
  global bstack1111ll111_opy_
  global bstack1l11ll111_opy_
  global bstack1ll111ll11_opy_
  global bstack1lll1ll1l_opy_
  bstack11l111l11l_opy_.bstack11ll1l11l_opy_()
  if cli.is_running():
    bstack1l11l1lll_opy_.invoke(Events.bstack1lll1111ll_opy_)
  else:
    bstack111l1l1l_opy_ = bstack111l11ll_opy_.bstack1111l1ll_opy_(config=CONFIG)
    bstack111l1l1l_opy_.bstack11l1111l1l_opy_(CONFIG)
  if bstack1111ll111_opy_ == bstack1lllll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ࿬"):
    if not cli.is_enabled(CONFIG):
      bstack1ll1l1l1_opy_.stop()
  else:
    bstack1ll1l1l1_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1ll11l1l_opy_.bstack111l1l1l1_opy_()
  if bstack1lllll1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ࿭") in CONFIG and str(CONFIG[bstack1lllll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ࿮")]).lower() != bstack1lllll1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ࿯"):
    hashed_id, bstack1ll1l11lll_opy_ = bstack1l1l1111ll_opy_()
  else:
    hashed_id, bstack1ll1l11lll_opy_ = get_build_link()
  bstack1ll111l1ll_opy_(hashed_id)
  logger.info(bstack1lllll1l_opy_ (u"࠭ࡓࡅࡍࠣࡶࡺࡴࠠࡦࡰࡧࡩࡩࠦࡦࡰࡴࠣ࡭ࡩࡀࠧ࿰") + bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ࿱"), bstack1lllll1l_opy_ (u"ࠨࠩ࿲")) + bstack1lllll1l_opy_ (u"ࠩ࠯ࠤࡹ࡫ࡳࡵࡪࡸࡦࠥ࡯ࡤ࠻ࠢࠪ࿳") + os.getenv(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ࿴"), bstack1lllll1l_opy_ (u"ࠫࠬ࿵")))
  if hashed_id is not None and bstack11l111lll1_opy_() != -1:
    sessions = bstack1ll1lll11l_opy_(hashed_id)
    bstack111111l11l_opy_(sessions, bstack1ll1l11lll_opy_)
  if bstack1111ll111_opy_ == bstack1lllll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ࿶") and bstack1l11ll111_opy_ != 0:
    sys.exit(bstack1l11ll111_opy_)
  if bstack1111ll111_opy_ == bstack1lllll1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭࿷") and bstack1ll111ll11_opy_ != 0:
    sys.exit(bstack1ll111ll11_opy_)
def bstack1ll111l1ll_opy_(new_id):
    global bstack1ll1ll11l1_opy_
    bstack1ll1ll11l1_opy_ = new_id
def bstack1111ll1l1l_opy_(bstack1llllll1l1_opy_):
  if bstack1llllll1l1_opy_:
    return bstack1llllll1l1_opy_.capitalize()
  else:
    return bstack1lllll1l_opy_ (u"ࠧࠨ࿸")
@measure(event_name=EVENTS.bstack11l11l1ll_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1ll1111l1_opy_(bstack11l1lll1l_opy_):
  if bstack1lllll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭࿹") in bstack11l1lll1l_opy_ and bstack11l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ࿺")] != bstack1lllll1l_opy_ (u"ࠪࠫ࿻"):
    return bstack11l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ࿼")]
  else:
    bstack11lll11l1l_opy_ = bstack1lllll1l_opy_ (u"ࠧࠨ࿽")
    if bstack1lllll1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭࿾") in bstack11l1lll1l_opy_ and bstack11l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ࿿")] != None:
      bstack11lll11l1l_opy_ += bstack11l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨက")] + bstack1lllll1l_opy_ (u"ࠤ࠯ࠤࠧခ")
      if bstack11l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠪࡳࡸ࠭ဂ")] == bstack1lllll1l_opy_ (u"ࠦ࡮ࡵࡳࠣဃ"):
        bstack11lll11l1l_opy_ += bstack1lllll1l_opy_ (u"ࠧ࡯ࡏࡔࠢࠥင")
      bstack11lll11l1l_opy_ += (bstack11l1lll1l_opy_[bstack1lllll1l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪစ")] or bstack1lllll1l_opy_ (u"ࠧࠨဆ"))
      return bstack11lll11l1l_opy_
    else:
      bstack11lll11l1l_opy_ += bstack1111ll1l1l_opy_(bstack11l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩဇ")]) + bstack1lllll1l_opy_ (u"ࠤࠣࠦဈ") + (
              bstack11l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬဉ")] or bstack1lllll1l_opy_ (u"ࠫࠬည")) + bstack1lllll1l_opy_ (u"ࠧ࠲ࠠࠣဋ")
      if bstack11l1lll1l_opy_[bstack1lllll1l_opy_ (u"࠭࡯ࡴࠩဌ")] == bstack1lllll1l_opy_ (u"ࠢࡘ࡫ࡱࡨࡴࡽࡳࠣဍ"):
        bstack11lll11l1l_opy_ += bstack1lllll1l_opy_ (u"࡙ࠣ࡬ࡲࠥࠨဎ")
      bstack11lll11l1l_opy_ += bstack11l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ဏ")] or bstack1lllll1l_opy_ (u"ࠪࠫတ")
      return bstack11lll11l1l_opy_
@measure(event_name=EVENTS.bstack1l11lllll_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack1111111l1_opy_(bstack11lll1111l_opy_):
  if bstack11lll1111l_opy_ == bstack1lllll1l_opy_ (u"ࠦࡩࡵ࡮ࡦࠤထ"):
    return bstack1lllll1l_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡨࡴࡨࡩࡳࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡨࡴࡨࡩࡳࠨ࠾ࡄࡱࡰࡴࡱ࡫ࡴࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨဒ")
  elif bstack11lll1111l_opy_ == bstack1lllll1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨဓ"):
    return bstack1lllll1l_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡵࡩࡩࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡳࡧࡧࠦࡃࡌࡡࡪ࡮ࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪန")
  elif bstack11lll1111l_opy_ == bstack1lllll1l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣပ"):
    return bstack1lllll1l_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡕࡧࡳࡴࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩဖ")
  elif bstack11lll1111l_opy_ == bstack1lllll1l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤဗ"):
    return bstack1lllll1l_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡈࡶࡷࡵࡲ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ဘ")
  elif bstack11lll1111l_opy_ == bstack1lllll1l_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨမ"):
    return bstack1lllll1l_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࠥࡨࡩࡦ࠹࠲࠷࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࠧࡪ࡫ࡡ࠴࠴࠹ࠦࡃ࡚ࡩ࡮ࡧࡲࡹࡹࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫယ")
  elif bstack11lll1111l_opy_ == bstack1lllll1l_opy_ (u"ࠢࡳࡷࡱࡲ࡮ࡴࡧࠣရ"):
    return bstack1lllll1l_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡦࡱࡧࡣ࡬࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡦࡱࡧࡣ࡬ࠤࡁࡖࡺࡴ࡮ࡪࡰࡪࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩလ")
  else:
    return bstack1lllll1l_opy_ (u"ࠩ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡨ࡬ࡢࡥ࡮࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡨ࡬ࡢࡥ࡮ࠦࡃ࠭ဝ") + bstack1111ll1l1l_opy_(
      bstack11lll1111l_opy_) + bstack1lllll1l_opy_ (u"ࠪࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩသ")
def bstack1l11llll11_opy_(session):
  return bstack1lllll1l_opy_ (u"ࠫࡁࡺࡲࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡴࡲࡻࠧࡄ࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠡࡵࡨࡷࡸ࡯࡯࡯࠯ࡱࡥࡲ࡫ࠢ࠿࠾ࡤࠤ࡭ࡸࡥࡧ࠿ࠥࡿࢂࠨࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣࡡࡥࡰࡦࡴ࡫ࠣࡀࡾࢁࡁ࠵ࡡ࠿࠾࠲ࡸࡩࡄࡻࡾࡽࢀࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂ࠯ࡵࡴࡁࠫဟ").format(
    session[bstack1lllll1l_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧࡤࡻࡲ࡭ࠩဠ")], bstack1ll1111l1_opy_(session), bstack1111111l1_opy_(session[bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡴࡢࡶࡸࡷࠬအ")]),
    bstack1111111l1_opy_(session[bstack1lllll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧဢ")]),
    bstack1111ll1l1l_opy_(session[bstack1lllll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩဣ")] or session[bstack1lllll1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩဤ")] or bstack1lllll1l_opy_ (u"ࠪࠫဥ")) + bstack1lllll1l_opy_ (u"ࠦࠥࠨဦ") + (session[bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧဧ")] or bstack1lllll1l_opy_ (u"࠭ࠧဨ")),
    session[bstack1lllll1l_opy_ (u"ࠧࡰࡵࠪဩ")] + bstack1lllll1l_opy_ (u"ࠣࠢࠥဪ") + session[bstack1lllll1l_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ါ")], session[bstack1lllll1l_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬာ")] or bstack1lllll1l_opy_ (u"ࠫࠬိ"),
    session[bstack1lllll1l_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩီ")] if session[bstack1lllll1l_opy_ (u"࠭ࡣࡳࡧࡤࡸࡪࡪ࡟ࡢࡶࠪု")] else bstack1lllll1l_opy_ (u"ࠧࠨူ"))
@measure(event_name=EVENTS.bstack1111ll1ll1_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def bstack111111l11l_opy_(sessions, bstack1ll1l11lll_opy_):
  try:
    bstack1111l11ll1_opy_ = bstack1lllll1l_opy_ (u"ࠣࠤေ")
    if not os.path.exists(bstack1ll1ll11ll_opy_):
      os.mkdir(bstack1ll1ll11ll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1lllll1l_opy_ (u"ࠩࡤࡷࡸ࡫ࡴࡴ࠱ࡵࡩࡵࡵࡲࡵ࠰࡫ࡸࡲࡲࠧဲ")), bstack1lllll1l_opy_ (u"ࠪࡶࠬဳ")) as f:
      bstack1111l11ll1_opy_ = f.read()
    bstack1111l11ll1_opy_ = bstack1111l11ll1_opy_.replace(bstack1lllll1l_opy_ (u"ࠫࢀࠫࡒࡆࡕࡘࡐ࡙࡙࡟ࡄࡑࡘࡒ࡙ࠫࡽࠨဴ"), str(len(sessions)))
    bstack1111l11ll1_opy_ = bstack1111l11ll1_opy_.replace(bstack1lllll1l_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡕࡓࡎࠨࢁࠬဵ"), bstack1ll1l11lll_opy_)
    bstack1111l11ll1_opy_ = bstack1111l11ll1_opy_.replace(bstack1lllll1l_opy_ (u"࠭ࡻࠦࡄࡘࡍࡑࡊ࡟ࡏࡃࡐࡉࠪࢃࠧံ"),
                                              sessions[0].get(bstack1lllll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥ࡮ࡢ࡯ࡨ့ࠫ")) if sessions[0] else bstack1lllll1l_opy_ (u"ࠨࠩး"))
    with open(os.path.join(bstack1ll1ll11ll_opy_, bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ္࠭")), bstack1lllll1l_opy_ (u"ࠪࡻ်ࠬ")) as stream:
      stream.write(bstack1111l11ll1_opy_.split(bstack1lllll1l_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨျ"))[0])
      for session in sessions:
        stream.write(bstack1l11llll11_opy_(session))
      stream.write(bstack1111l11ll1_opy_.split(bstack1lllll1l_opy_ (u"ࠬࢁࠥࡔࡇࡖࡗࡎࡕࡎࡔࡡࡇࡅ࡙ࡇࠥࡾࠩြ"))[1])
    logger.info(bstack1lllll1l_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࡥࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡤࡸ࡭ࡱࡪࠠࡢࡴࡷ࡭࡫ࡧࡣࡵࡵࠣࡥࡹࠦࡻࡾࠩွ").format(bstack1ll1ll11ll_opy_));
  except Exception as e:
    logger.debug(bstack111l1llll_opy_.format(str(e)))
def bstack1ll1lll11l_opy_(hashed_id):
  global CONFIG
  try:
    bstack1ll111ll1_opy_ = datetime.datetime.now()
    host = bstack1lllll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠲ࡩ࡬ࡰࡷࡧ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧှ") if bstack1lllll1l_opy_ (u"ࠨࡣࡳࡴࠬဿ") in CONFIG else bstack1lllll1l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪ၀")
    user = CONFIG[bstack1lllll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ၁")]
    key = CONFIG[bstack1lllll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ၂")]
    bstack111ll111l_opy_ = bstack1lllll1l_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ၃") if bstack1lllll1l_opy_ (u"࠭ࡡࡱࡲࠪ၄") in CONFIG else (bstack1lllll1l_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫ၅") if CONFIG.get(bstack1lllll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬ၆")) else bstack1lllll1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ၇"))
    host = bstack11l111l1ll_opy_(cli.config, [bstack1lllll1l_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ၈"), bstack1lllll1l_opy_ (u"ࠦࡦࡶࡰࡂࡷࡷࡳࡲࡧࡴࡦࠤ၉"), bstack1lllll1l_opy_ (u"ࠧࡧࡰࡪࠤ၊")], host) if bstack1lllll1l_opy_ (u"࠭ࡡࡱࡲࠪ။") in CONFIG else bstack11l111l1ll_opy_(cli.config, [bstack1lllll1l_opy_ (u"ࠢࡢࡲ࡬ࡷࠧ၌"), bstack1lllll1l_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࠥ၍"), bstack1lllll1l_opy_ (u"ࠤࡤࡴ࡮ࠨ၎")], host)
    url = bstack1lllll1l_opy_ (u"ࠪࡿࢂ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠮࡫ࡵࡲࡲࠬ၏").format(host, bstack111ll111l_opy_, hashed_id)
    headers = {
      bstack1lllll1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪၐ"): bstack1lllll1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨၑ"),
    }
    proxies = bstack1ll111lll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࡬࡫ࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࡢࡰ࡮ࡹࡴࠣၒ"), datetime.datetime.now() - bstack1ll111ll1_opy_)
      return list(map(lambda session: session[bstack1lllll1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬၓ")], response.json()))
  except Exception as e:
    logger.debug(bstack1l1111l1l1_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack11111l1ll_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def get_build_link():
  global CONFIG
  global bstack1ll1ll11l1_opy_
  try:
    if bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫၔ") in CONFIG:
      bstack1ll111ll1_opy_ = datetime.datetime.now()
      host = bstack1lllll1l_opy_ (u"ࠩࡤࡴ࡮࠳ࡣ࡭ࡱࡸࡨࠬၕ") if bstack1lllll1l_opy_ (u"ࠪࡥࡵࡶࠧၖ") in CONFIG else bstack1lllll1l_opy_ (u"ࠫࡦࡶࡩࠨၗ")
      user = CONFIG[bstack1lllll1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧၘ")]
      key = CONFIG[bstack1lllll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩၙ")]
      bstack111ll111l_opy_ = bstack1lllll1l_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ၚ") if bstack1lllll1l_opy_ (u"ࠨࡣࡳࡴࠬၛ") in CONFIG else bstack1lllll1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫၜ")
      url = bstack1lllll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࢀࢃ࠺ࡼࡿࡃࡿࢂ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠳ࡰࡳࡰࡰࠪၝ").format(user, key, host, bstack111ll111l_opy_)
      if cli.is_enabled(CONFIG):
        bstack1ll1l11lll_opy_, hashed_id = cli.bstack11l1l1l111_opy_()
        logger.info(bstack11l1ll1l1_opy_.format(bstack1ll1l11lll_opy_))
        return [hashed_id, bstack1ll1l11lll_opy_]
      else:
        headers = {
          bstack1lllll1l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪၞ"): bstack1lllll1l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨၟ"),
        }
        if bstack1lllll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨၠ") in CONFIG:
          params = {bstack1lllll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬၡ"): CONFIG[bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫၢ")], bstack1lllll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬၣ"): CONFIG[bstack1lllll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬၤ")]}
        else:
          params = {bstack1lllll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩၥ"): CONFIG[bstack1lllll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨၦ")]}
        proxies = bstack1ll111lll_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack11ll11111l_opy_ = response.json()[0][bstack1lllll1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡦࡺ࡯࡬ࡥࠩၧ")]
          if bstack11ll11111l_opy_:
            bstack1ll1l11lll_opy_ = bstack11ll11111l_opy_[bstack1lllll1l_opy_ (u"ࠧࡱࡷࡥࡰ࡮ࡩ࡟ࡶࡴ࡯ࠫၨ")].split(bstack1lllll1l_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣ࠮ࡤࡸ࡭ࡱࡪࠧၩ"))[0] + bstack1lllll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡴ࠱ࠪၪ") + bstack11ll11111l_opy_[
              bstack1lllll1l_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ၫ")]
            logger.info(bstack11l1ll1l1_opy_.format(bstack1ll1l11lll_opy_))
            bstack1ll1ll11l1_opy_ = bstack11ll11111l_opy_[bstack1lllll1l_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧၬ")]
            bstack1l1l11111_opy_ = CONFIG[bstack1lllll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨၭ")]
            if bstack1lllll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨၮ") in CONFIG:
              bstack1l1l11111_opy_ += bstack1lllll1l_opy_ (u"ࠧࠡࠩၯ") + CONFIG[bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪၰ")]
            if bstack1l1l11111_opy_ != bstack11ll11111l_opy_[bstack1lllll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧၱ")]:
              logger.debug(bstack11111llll_opy_.format(bstack11ll11111l_opy_[bstack1lllll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨၲ")], bstack1l1l11111_opy_))
            cli.bstack1lll11llll_opy_(bstack1lllll1l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡪࡩࡹࡥࡢࡶ࡫࡯ࡨࡤࡲࡩ࡯࡭ࠥၳ"), datetime.datetime.now() - bstack1ll111ll1_opy_)
            return [bstack11ll11111l_opy_[bstack1lllll1l_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨၴ")], bstack1ll1l11lll_opy_]
    else:
      logger.warn(bstack11ll1111ll_opy_)
  except Exception as e:
    logger.debug(bstack11l1ll1ll_opy_.format(str(e)))
  return [None, None]
def bstack1l11l1111_opy_(url, bstack1ll1l1llll_opy_=False):
  global CONFIG
  global bstack1111l1llll_opy_
  if not bstack1111l1llll_opy_:
    hostname = bstack111lll1l1_opy_(url)
    is_private = bstack11l11l1l11_opy_(hostname)
    if (bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪၵ") in CONFIG and not bstack1111l11l1l_opy_(CONFIG[bstack1lllll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫၶ")])) and (is_private or bstack1ll1l1llll_opy_):
      bstack1111l1llll_opy_ = hostname
def bstack111lll1l1_opy_(url):
  return urlparse(url).hostname
def bstack11l11l1l11_opy_(hostname):
  for bstack1lll1lllll_opy_ in bstack1lll1l1ll1_opy_:
    regex = re.compile(bstack1lll1lllll_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack111l111l11_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack111ll11l1l_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack11111ll1l1_opy_
  bstack111l1l1l1l_opy_ = not (bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬၷ"), None) and bstack1l11l1l1_opy_(
          threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨၸ"), None))
  bstack1l1l1lll11_opy_ = getattr(driver, bstack1lllll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪၹ"), None) != True
  bstack1ll1l1ll11_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫၺ"), None) and bstack1l11l1l1_opy_(
          threading.current_thread(), bstack1lllll1l_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧၻ"), None)
  if bstack1ll1l1ll11_opy_:
    if not bstack11l111ll1l_opy_():
      logger.warning(bstack1lllll1l_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴ࠰ࠥၼ"))
      return {}
    logger.debug(bstack1lllll1l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠫၽ"))
    logger.debug(perform_scan(driver, driver_command=bstack1lllll1l_opy_ (u"ࠨࡧࡻࡩࡨࡻࡴࡦࡕࡦࡶ࡮ࡶࡴࠨၾ")))
    results = bstack1l111lll11_opy_(bstack1lllll1l_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡵࠥၿ"))
    if results is not None and results.get(bstack1lllll1l_opy_ (u"ࠥ࡭ࡸࡹࡵࡦࡵࠥႀ")) is not None:
        return results[bstack1lllll1l_opy_ (u"ࠦ࡮ࡹࡳࡶࡧࡶࠦႁ")]
    logger.error(bstack1lllll1l_opy_ (u"ࠧࡔ࡯ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡔࡨࡷࡺࡲࡴࡴࠢࡺࡩࡷ࡫ࠠࡧࡱࡸࡲࡩ࠴ࠢႂ"))
    return []
  if not bstack1111ll1l_opy_.bstack1l1lll1l1l_opy_(CONFIG, bstack11111ll1l1_opy_) or (bstack1l1l1lll11_opy_ and bstack111l1l1l1l_opy_):
    logger.warning(bstack1lllll1l_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤႃ"))
    return {}
  try:
    logger.debug(bstack1lllll1l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠫႄ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack11l11l11ll_opy_.bstack1llll1l11l_opy_)
    return results
  except Exception:
    logger.error(bstack1lllll1l_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡽࡥࡳࡧࠣࡪࡴࡻ࡮ࡥ࠰ࠥႅ"))
    return {}
@measure(event_name=EVENTS.bstack1l11lll111_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack11111ll1l1_opy_
  bstack111l1l1l1l_opy_ = not (bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ႆ"), None) and bstack1l11l1l1_opy_(
          threading.current_thread(), bstack1lllll1l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩႇ"), None))
  bstack1l1l1lll11_opy_ = getattr(driver, bstack1lllll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫႈ"), None) != True
  bstack1ll1l1ll11_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬႉ"), None) and bstack1l11l1l1_opy_(
          threading.current_thread(), bstack1lllll1l_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨႊ"), None)
  if bstack1ll1l1ll11_opy_:
    if not bstack11l111ll1l_opy_():
      logger.warning(bstack1lllll1l_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼ࠲ࠧႋ"))
      return {}
    logger.debug(bstack1lllll1l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠭ႌ"))
    logger.debug(perform_scan(driver, driver_command=bstack1lllll1l_opy_ (u"ࠩࡨࡼࡪࡩࡵࡵࡧࡖࡧࡷ࡯ࡰࡵႍࠩ")))
    results = bstack1l111lll11_opy_(bstack1lllll1l_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡖࡹࡲࡳࡡࡳࡻࠥႎ"))
    if results is not None and results.get(bstack1lllll1l_opy_ (u"ࠦࡸࡻ࡭࡮ࡣࡵࡽࠧႏ")) is not None:
        return results[bstack1lllll1l_opy_ (u"ࠧࡹࡵ࡮࡯ࡤࡶࡾࠨ႐")]
    logger.error(bstack1lllll1l_opy_ (u"ࠨࡎࡰࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡕࡩࡸࡻ࡬ࡵࡵࠣࡗࡺࡳ࡭ࡢࡴࡼࠤࡼࡧࡳࠡࡨࡲࡹࡳࡪ࠮ࠣ႑"))
    return {}
  if not bstack1111ll1l_opy_.bstack1l1lll1l1l_opy_(CONFIG, bstack11111ll1l1_opy_) or (bstack1l1l1lll11_opy_ and bstack111l1l1l1l_opy_):
    logger.warning(bstack1lllll1l_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻ࠱ࠦ႒"))
    return {}
  try:
    logger.debug(bstack1lllll1l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠭႓"))
    logger.debug(perform_scan(driver))
    bstack1lll111l1l_opy_ = driver.execute_async_script(bstack11l11l11ll_opy_.bstack11l1l1111l_opy_)
    return bstack1lll111l1l_opy_
  except Exception:
    logger.error(bstack1lllll1l_opy_ (u"ࠤࡑࡳࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡵ࡮࡯ࡤࡶࡾࠦࡷࡢࡵࠣࡪࡴࡻ࡮ࡥ࠰ࠥ႔"))
    return {}
def bstack11l111ll1l_opy_():
  global CONFIG
  global bstack11111ll1l1_opy_
  bstack1ll1l11l1l_opy_ = bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ႕"), None) and bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭႖"), None)
  if not bstack1111ll1l_opy_.bstack1l1lll1l1l_opy_(CONFIG, bstack11111ll1l1_opy_) or not bstack1ll1l11l1l_opy_:
        logger.warning(bstack1lllll1l_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡶࡪࡹࡵ࡭ࡶࡶ࠲ࠧ႗"))
        return False
  return True
def bstack1l111lll11_opy_(bstack11ll11l11_opy_):
    bstack11111l11l_opy_ = bstack1ll1l1l1_opy_.current_test_uuid() if bstack1ll1l1l1_opy_.current_test_uuid() else bstack1ll11l1l_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack11ll11ll1_opy_(bstack11111l11l_opy_, bstack11ll11l11_opy_))
        try:
            return future.result(timeout=bstack1l1ll11l1_opy_)
        except TimeoutError:
            logger.error(bstack1lllll1l_opy_ (u"ࠨࡔࡪ࡯ࡨࡳࡺࡺࠠࡢࡨࡷࡩࡷࠦࡻࡾࡵࠣࡻ࡭࡯࡬ࡦࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡗ࡫ࡳࡶ࡮ࡷࡷࠧ႘").format(bstack1l1ll11l1_opy_))
        except Exception as ex:
            logger.debug(bstack1lllll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡲࡦࡶࡵ࡭ࡪࡼࡩ࡯ࡩࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࢀࢃ࠮ࠡࡇࡵࡶࡴࡸࠠ࠮ࠢࡾࢁࠧ႙").format(bstack11ll11l11_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack11111l1l11_opy_, stage=STAGE.bstack1l11ll1ll_opy_, bstack11lll11l1l_opy_=bstack1l1ll1l1l1_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack11111ll1l1_opy_
  bstack111l1l1l1l_opy_ = not (bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬႚ"), None) and bstack1l11l1l1_opy_(
          threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨႛ"), None))
  bstack1ll1l11111_opy_ = not (bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪႜ"), None) and bstack1l11l1l1_opy_(
          threading.current_thread(), bstack1lllll1l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ႝ"), None))
  bstack1l1l1lll11_opy_ = getattr(driver, bstack1lllll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ႞"), None) != True
  if not bstack1111ll1l_opy_.bstack1l1lll1l1l_opy_(CONFIG, bstack11111ll1l1_opy_) or (bstack1l1l1lll11_opy_ and bstack111l1l1l1l_opy_ and bstack1ll1l11111_opy_):
    logger.warning(bstack1lllll1l_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡵ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡧࡦࡴ࠮ࠣ႟"))
    return {}
  try:
    bstack1l11111ll1_opy_ = bstack1lllll1l_opy_ (u"ࠧࡢࡲࡳࠫႠ") in CONFIG and CONFIG.get(bstack1lllll1l_opy_ (u"ࠨࡣࡳࡴࠬႡ"), bstack1lllll1l_opy_ (u"ࠩࠪႢ"))
    session_id = getattr(driver, bstack1lllll1l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧႣ"), None)
    if not session_id:
      logger.warning(bstack1lllll1l_opy_ (u"ࠦࡓࡵࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡋࡇࠤ࡫ࡵࡵ࡯ࡦࠣࡪࡴࡸࠠࡥࡴ࡬ࡺࡪࡸࠢႤ"))
      return {bstack1lllll1l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦႥ"): bstack1lllll1l_opy_ (u"ࠨࡎࡰࠢࡶࡩࡸࡹࡩࡰࡰࠣࡍࡉࠦࡦࡰࡷࡱࡨࠧႦ")}
    if bstack1l11111ll1_opy_:
      try:
        bstack11ll1l111_opy_ = {
              bstack1lllll1l_opy_ (u"ࠧࡵࡪࡍࡻࡹ࡚࡯࡬ࡧࡱࠫႧ"): os.environ.get(bstack1lllll1l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭Ⴈ"), os.environ.get(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭Ⴉ"), bstack1lllll1l_opy_ (u"ࠪࠫႪ"))),
              bstack1lllll1l_opy_ (u"ࠫࡹ࡮ࡔࡦࡵࡷࡖࡺࡴࡕࡶ࡫ࡧࠫႫ"): bstack1ll1l1l1_opy_.current_test_uuid() if bstack1ll1l1l1_opy_.current_test_uuid() else bstack1ll11l1l_opy_.current_hook_uuid(),
              bstack1lllll1l_opy_ (u"ࠬࡧࡵࡵࡪࡋࡩࡦࡪࡥࡳࠩႬ"): os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫႭ")),
              bstack1lllll1l_opy_ (u"ࠧࡴࡥࡤࡲ࡙࡯࡭ࡦࡵࡷࡥࡲࡶࠧႮ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack1lllll1l_opy_ (u"ࠨࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭Ⴏ"): os.environ.get(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧႰ"), bstack1lllll1l_opy_ (u"ࠪࠫႱ")),
              bstack1lllll1l_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࠫႲ"): kwargs.get(bstack1lllll1l_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤࡩ࡯࡮࡯ࡤࡲࡩ࠭Ⴓ"), None) or bstack1lllll1l_opy_ (u"࠭ࠧႴ")
          }
        if not hasattr(thread_local, bstack1lllll1l_opy_ (u"ࠧࡣࡣࡶࡩࡤࡧࡰࡱࡡࡤ࠵࠶ࡿ࡟ࡴࡥࡵ࡭ࡵࡺࠧႵ")):
            scripts = {bstack1lllll1l_opy_ (u"ࠨࡵࡦࡥࡳ࠭Ⴖ"): bstack11l11l11ll_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack1l1l1lll1l_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack1l1l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠩࡶࡧࡦࡴࠧႷ")] = bstack1l1l1lll1l_opy_[bstack1lllll1l_opy_ (u"ࠪࡷࡨࡧ࡮ࠨႸ")] % json.dumps(bstack11ll1l111_opy_)
        bstack11l11l11ll_opy_.bstack11lll1lll_opy_(bstack1l1l1lll1l_opy_)
        bstack11l11l11ll_opy_.store()
        bstack1l1lll11ll_opy_ = driver.execute_script(bstack11l11l11ll_opy_.perform_scan)
      except Exception as bstack1l1l111ll1_opy_:
        logger.info(bstack1lllll1l_opy_ (u"ࠦࡆࡶࡰࡪࡷࡰࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡩࡡ࡯ࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࠦႹ") + str(bstack1l1l111ll1_opy_))
        bstack1l1lll11ll_opy_ = {bstack1lllll1l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦႺ"): str(bstack1l1l111ll1_opy_)}
    else:
      bstack1l1lll11ll_opy_ = driver.execute_async_script(bstack11l11l11ll_opy_.perform_scan, {bstack1lllll1l_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭Ⴛ"): kwargs.get(bstack1lllll1l_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸ࡟ࡤࡱࡰࡱࡦࡴࡤࠨႼ"), None) or bstack1lllll1l_opy_ (u"ࠨࠩႽ")})
    return bstack1l1lll11ll_opy_
  except Exception as err:
    logger.error(bstack1lllll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡸࡵ࡯ࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡧࡦࡴ࠮ࠡࡽࢀࠦႾ").format(str(err)))
    return {}