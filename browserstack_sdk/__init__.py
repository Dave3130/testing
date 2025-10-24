# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
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
from browserstack_sdk.bstack111l1111l_opy_ import bstack1l1l1l111_opy_
from browserstack_sdk.bstack1lll11l11_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack1l1lllllll_opy_():
  global CONFIG
  headers = {
        bstack11l11l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨਙ"): bstack11l11l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ਚ"),
      }
  proxies = bstack11l1ll111_opy_(CONFIG, bstack111ll11l1l_opy_)
  try:
    response = requests.get(bstack111ll11l1l_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l11l1l1l1_opy_ = response.json()[bstack11l11l1_opy_ (u"ࠫ࡭ࡻࡢࡴࠩਛ")]
      logger.debug(bstack1l11lll11_opy_.format(response.json()))
      return bstack1l11l1l1l1_opy_
    else:
      logger.debug(bstack1llll1llll_opy_.format(bstack11l11l1_opy_ (u"ࠧࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡋࡕࡒࡒࠥࡶࡡࡳࡵࡨࠤࡪࡸࡲࡰࡴࠣࠦਜ")))
  except Exception as e:
    logger.debug(bstack1llll1llll_opy_.format(e))
def bstack1lllll1lll_opy_(hub_url):
  global CONFIG
  url = bstack11l11l1_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣਝ")+  hub_url + bstack11l11l1_opy_ (u"ࠢ࠰ࡥ࡫ࡩࡨࡱࠢਞ")
  headers = {
        bstack11l11l1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧਟ"): bstack11l11l1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬਠ"),
      }
  proxies = bstack11l1ll111_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack111l1lll1l_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack111l111lll_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack1llll1lll1_opy_, stage=STAGE.bstack1ll1lllll_opy_)
def bstack1l1l11ll11_opy_():
  try:
    global bstack1ll1ll111_opy_
    bstack1l11l1l1l1_opy_ = bstack1l1lllllll_opy_()
    bstack1l11llll11_opy_ = []
    results = []
    for bstack111l1l11l_opy_ in bstack1l11l1l1l1_opy_:
      bstack1l11llll11_opy_.append(bstack1l1ll1ll1l_opy_(target=bstack1lllll1lll_opy_,args=(bstack111l1l11l_opy_,)))
    for t in bstack1l11llll11_opy_:
      t.start()
    for t in bstack1l11llll11_opy_:
      results.append(t.join())
    bstack1ll1lll111_opy_ = {}
    for item in results:
      hub_url = item[bstack11l11l1_opy_ (u"ࠪ࡬ࡺࡨ࡟ࡶࡴ࡯ࠫਡ")]
      latency = item[bstack11l11l1_opy_ (u"ࠫࡱࡧࡴࡦࡰࡦࡽࠬਢ")]
      bstack1ll1lll111_opy_[hub_url] = latency
    bstack1111llll1l_opy_ = min(bstack1ll1lll111_opy_, key= lambda x: bstack1ll1lll111_opy_[x])
    bstack1ll1ll111_opy_ = bstack1111llll1l_opy_
    logger.debug(bstack1ll1l11l1l_opy_.format(bstack1111llll1l_opy_))
  except Exception as e:
    logger.debug(bstack1ll1l1l1l_opy_.format(e))
from browserstack_sdk.bstack1111l11l_opy_ import *
from browserstack_sdk.bstack1llll111l_opy_ import *
from browserstack_sdk.bstack11l1l11l_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack11111l1l1_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack1l11l1l11l_opy_, stage=STAGE.bstack1ll1lllll_opy_)
def bstack1ll11lllll_opy_():
    global bstack1ll1ll111_opy_
    try:
        bstack1ll1lll1l_opy_ = bstack1l1lll1ll1_opy_()
        bstack1111l11l11_opy_(bstack1ll1lll1l_opy_)
        hub_url = bstack1ll1lll1l_opy_.get(bstack11l11l1_opy_ (u"ࠧࡻࡲ࡭ࠤਣ"), bstack11l11l1_opy_ (u"ࠨࠢਤ"))
        if hub_url.endswith(bstack11l11l1_opy_ (u"ࠧ࠰ࡹࡧ࠳࡭ࡻࡢࠨਥ")):
            hub_url = hub_url.rsplit(bstack11l11l1_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩਦ"), 1)[0]
        if hub_url.startswith(bstack11l11l1_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱ࠪਧ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack11l11l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠬਨ")):
            hub_url = hub_url[8:]
        bstack1ll1ll111_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1l1lll1ll1_opy_():
    global CONFIG
    bstack11ll11111_opy_ = CONFIG.get(bstack11l11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ਩"), {}).get(bstack11l11l1_opy_ (u"ࠬ࡭ࡲࡪࡦࡑࡥࡲ࡫ࠧਪ"), bstack11l11l1_opy_ (u"࠭ࡎࡐࡡࡊࡖࡎࡊ࡟ࡏࡃࡐࡉࡤࡖࡁࡔࡕࡈࡈࠬਫ"))
    if not isinstance(bstack11ll11111_opy_, str):
        raise ValueError(bstack11l11l1_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡇࡳ࡫ࡧࠤࡳࡧ࡭ࡦࠢࡰࡹࡸࡺࠠࡣࡧࠣࡥࠥࡼࡡ࡭࡫ࡧࠤࡸࡺࡲࡪࡰࡪࠦਬ"))
    try:
        bstack1ll1lll1l_opy_ = bstack11lll1lll1_opy_(bstack11ll11111_opy_)
        return bstack1ll1lll1l_opy_
    except Exception as e:
        logger.error(bstack11l11l1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢਭ").format(str(e)))
        return {}
def bstack11lll1lll1_opy_(bstack11ll11111_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack11l11l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫਮ")] or not CONFIG[bstack11l11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ਯ")]:
            raise ValueError(bstack11l11l1_opy_ (u"ࠦࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡺࡹࡥࡳࡰࡤࡱࡪࠦ࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾࠨਰ"))
        url = bstack1ll111lll_opy_ + bstack11ll11111_opy_
        auth = (CONFIG[bstack11l11l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ਱")], CONFIG[bstack11l11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩਲ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1llll11l11_opy_ = json.loads(response.text)
            return bstack1llll11l11_opy_
    except ValueError as ve:
        logger.error(bstack11l11l1_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢਲ਼").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack11l11l1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣ਴").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1111l11l11_opy_(bstack11111llll_opy_):
    global CONFIG
    if bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ਵ") not in CONFIG or str(CONFIG[bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧਸ਼")]).lower() == bstack11l11l1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ਷"):
        CONFIG[bstack11l11l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫਸ")] = False
    elif bstack11l11l1_opy_ (u"࠭ࡩࡴࡖࡵ࡭ࡦࡲࡇࡳ࡫ࡧࠫਹ") in bstack11111llll_opy_:
        bstack1l11l1111l_opy_ = CONFIG.get(bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ਺"), {})
        logger.debug(bstack11l11l1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡺ࡬ࡷࡹ࡯࡮ࡨࠢ࡯ࡳࡨࡧ࡬ࠡࡱࡳࡸ࡮ࡵ࡮ࡴ࠼ࠣࠩࡸࠨ਻"), bstack1l11l1111l_opy_)
        bstack1lll11111_opy_ = bstack11111llll_opy_.get(bstack11l11l1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡔࡨࡴࡪࡧࡴࡦࡴࡶ਼ࠦ"), [])
        bstack1l1l1llll1_opy_ = bstack11l11l1_opy_ (u"ࠥ࠰ࠧ਽").join(bstack1lll11111_opy_)
        logger.debug(bstack11l11l1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡇࡺࡹࡴࡰ࡯ࠣࡶࡪࡶࡥࡢࡶࡨࡶࠥࡹࡴࡳ࡫ࡱ࡫࠿ࠦࠥࡴࠤਾ"), bstack1l1l1llll1_opy_)
        bstack11ll1l11l_opy_ = {
            bstack11l11l1_opy_ (u"ࠧࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢਿ"): bstack11l11l1_opy_ (u"ࠨࡡࡵࡵ࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧੀ"),
            bstack11l11l1_opy_ (u"ࠢࡧࡱࡵࡧࡪࡒ࡯ࡤࡣ࡯ࠦੁ"): bstack11l11l1_opy_ (u"ࠣࡶࡵࡹࡪࠨੂ"),
            bstack11l11l1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠦ੃"): bstack1l1l1llll1_opy_
        }
        bstack1l11l1111l_opy_.update(bstack11ll1l11l_opy_)
        logger.debug(bstack11l11l1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡘࡴࡩࡧࡴࡦࡦࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢ੄"), bstack1l11l1111l_opy_)
        CONFIG[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੅")] = bstack1l11l1111l_opy_
        logger.debug(bstack11l11l1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡋ࡯࡮ࡢ࡮ࠣࡇࡔࡔࡆࡊࡉ࠽ࠤࠪࡹࠢ੆"), CONFIG)
def bstack1l11llll1l_opy_():
    bstack1ll1lll1l_opy_ = bstack1l1lll1ll1_opy_()
    if not bstack1ll1lll1l_opy_[bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡘࡶࡱ࠭ੇ")]:
      raise ValueError(bstack11l11l1_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠠࡪࡵࠣࡱ࡮ࡹࡳࡪࡰࡪࠤ࡫ࡸ࡯࡮ࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳ࠯ࠤੈ"))
    return bstack1ll1lll1l_opy_[bstack11l11l1_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠨ੉")] + bstack11l11l1_opy_ (u"ࠩࡂࡧࡦࡶࡳ࠾ࠩ੊")
@measure(event_name=EVENTS.bstack1111ll111l_opy_, stage=STAGE.bstack1ll1lllll_opy_)
def bstack1l1111111_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack11l11l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬੋ")], CONFIG[bstack11l11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧੌ")])
        url = bstack1l1ll11lll_opy_
        logger.debug(bstack11l11l1_opy_ (u"ࠧࡇࡴࡵࡧࡰࡴࡹ࡯࡮ࡨࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶࠤ࡫ࡸ࡯࡮ࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡖࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠥࡇࡐࡊࠤ੍"))
        try:
            response = requests.get(url, auth=auth, headers={bstack11l11l1_opy_ (u"ࠨࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠧ੎"): bstack11l11l1_opy_ (u"ࠢࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠥ੏")})
            if response.status_code == 200:
                bstack1lll111lll_opy_ = json.loads(response.text)
                bstack11l11l1l1l_opy_ = bstack1lll111lll_opy_.get(bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡳࠨ੐"), [])
                if bstack11l11l1l1l_opy_:
                    bstack1ll1l11ll_opy_ = bstack11l11l1l1l_opy_[0]
                    build_hashed_id = bstack1ll1l11ll_opy_.get(bstack11l11l1_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬੑ"))
                    bstack1111ll11l1_opy_ = bstack1lll11l1l1_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1111ll11l1_opy_])
                    logger.info(bstack1l1l11lll_opy_.format(bstack1111ll11l1_opy_))
                    bstack1lll11l1ll_opy_ = CONFIG[bstack11l11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭੒")]
                    if bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੓") in CONFIG:
                      bstack1lll11l1ll_opy_ += bstack11l11l1_opy_ (u"ࠬࠦࠧ੔") + CONFIG[bstack11l11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ੕")]
                    if bstack1lll11l1ll_opy_ != bstack1ll1l11ll_opy_.get(bstack11l11l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ੖")):
                      logger.debug(bstack1ll11lll1_opy_.format(bstack1ll1l11ll_opy_.get(bstack11l11l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭੗")), bstack1lll11l1ll_opy_))
                    return result
                else:
                    logger.debug(bstack11l11l1_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡐࡲࠤࡧࡻࡩ࡭ࡦࡶࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡴࡩࡧࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠳ࠨ੘"))
            else:
                logger.debug(bstack11l11l1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶ࠲ࠧਖ਼"))
        except Exception as e:
            logger.error(bstack11l11l1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࡸࠦ࠺ࠡࡽࢀࠦਗ਼").format(str(e)))
    else:
        logger.debug(bstack11l11l1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡕࡎࡇࡋࡊࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡸ࡫ࡴ࠯ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶ࠲ࠧਜ਼"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1111ll1ll1_opy_ import bstack1111ll1ll1_opy_, Events, bstack11l1llll1l_opy_, bstack1111l11ll1_opy_
from bstack_utils.measure import bstack11ll111ll1_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack11l1l11l1l_opy_ import bstack1ll1l1111_opy_
from bstack_utils.messages import *
from bstack_utils import bstack11111l1l1_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l1l11l1ll_opy_, bstack1ll1l1l11l_opy_, bstack11l1lll1l_opy_, bstack1ll11l1l_opy_, \
  bstack1ll11lll11_opy_, \
  Notset, bstack1l1l1111ll_opy_, \
  bstack1111l11l1l_opy_, bstack11111111l_opy_, bstack1l1l11l11_opy_, bstack11lll11l1_opy_, bstack11l1llllll_opy_, bstack1lll1l1l1l_opy_, \
  bstack1l1l11111l_opy_, \
  bstack1lll1l1111_opy_, bstack1l1ll1l11_opy_, bstack1l1l1lllll_opy_, bstack11l11l1111_opy_, \
  bstack111ll1111_opy_, bstack11l1l1l11_opy_, bstack111lll11l1_opy_, bstack1ll11lll1l_opy_
from bstack_utils.bstack11lllll1l_opy_ import bstack1l111111l1_opy_
from bstack_utils.bstack11lll11l11_opy_ import bstack1l111l1l11_opy_, bstack1lll111111_opy_
from bstack_utils.bstack111l1111l1_opy_ import bstack1l1ll1ll11_opy_
from bstack_utils.bstack11111ll111_opy_ import bstack11l11ll11l_opy_, bstack11l111l11_opy_
from bstack_utils.bstack1lllll111l_opy_ import bstack1lllll111l_opy_
from bstack_utils.bstack1l111l1111_opy_ import bstack111111llll_opy_
from bstack_utils.proxy import bstack1111l11lll_opy_, bstack11l1ll111_opy_, bstack1lllll11l1_opy_, bstack1lll1l1l11_opy_
from bstack_utils.bstack11l111l111_opy_ import bstack1l1lll1l1l_opy_
import bstack_utils.bstack1l11l11l11_opy_ as bstack1l1l1ll111_opy_
import bstack_utils.bstack11l11lll11_opy_ as bstack1ll111l1l1_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack111l1ll11_opy_ import bstack11l11l1lll_opy_
from bstack_utils.bstack111lll1l_opy_ import bstack1lll11ll1_opy_
from bstack_utils.bstack1ll1111l1_opy_ import bstack1llllll111_opy_
if os.getenv(bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡋࡓࡔࡑࡓࠨੜ")):
  cli.bstack11ll1l1l1_opy_()
else:
  os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡌࡔࡕࡋࡔࠩ੝")] = bstack11l11l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭ਫ਼")
bstack11ll11111l_opy_ = bstack11l11l1_opy_ (u"ࠩࠣࠤ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࠢࠣ࡭࡫࠮ࡰࡢࡩࡨࠤࡂࡃ࠽ࠡࡸࡲ࡭ࡩࠦ࠰ࠪࠢࡾࡠࡳࠦࠠࠡࡶࡵࡽࢀࡢ࡮ࠡࡥࡲࡲࡸࡺࠠࡧࡵࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮࡜ࠨࡨࡶࡠࠬ࠯࠻࡝ࡰࠣࠤࠥࠦࠠࡧࡵ࠱ࡥࡵࡶࡥ࡯ࡦࡉ࡭ࡱ࡫ࡓࡺࡰࡦࠬࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩ࠮ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡵࡥࡩ࡯ࡦࡨࡼ࠮ࠦࠫࠡࠤ࠽ࠦࠥ࠱ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭࠮ࡡࡸࡣ࡬ࡸࠥࡴࡥࡸࡒࡤ࡫ࡪ࠸࠮ࡦࡸࡤࡰࡺࡧࡴࡦࠪࠥࠬ࠮ࠦ࠽࠿ࠢࡾࢁࠧ࠲ࠠ࡝ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡪࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡥࡵࡣ࡬ࡰࡸࠨࡽ࡝ࠩࠬ࠭࠮ࡡࠢࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠥࡡ࠮ࠦࠫࠡࠤ࠯ࡠࡡࡴࠢࠪ࡞ࡱࠤࠥࠦࠠࡾࡥࡤࡸࡨ࡮ࠨࡦࡺࠬࡿࡡࡴࠠࠡࠢࠣࢁࡡࡴࠠࠡࡿ࡟ࡲࠥࠦ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠩ੟")
bstack11llll111l_opy_ = bstack11l11l1_opy_ (u"ࠪࡠࡳ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭ࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠶ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡱࡡ࡬ࡲࡩ࡫ࡸࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠶ࡢࡢ࡮ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮ࡴ࡮࡬ࡧࡪ࠮࠰࠭ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷࠮ࡢ࡮ࡤࡱࡱࡷࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮ࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ࠯࠻࡝ࡰ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰࡯ࡥࡺࡴࡣࡩࠢࡀࠤࡦࡹࡹ࡯ࡥࠣࠬࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶ࠭ࠥࡃ࠾ࠡࡽ࡟ࡲࡱ࡫ࡴࠡࡥࡤࡴࡸࡁ࡜࡯ࡶࡵࡽࠥࢁ࡜࡯ࡥࡤࡴࡸࠦ࠽ࠡࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠬࡠࡳࠦࠠࡾࠢࡦࡥࡹࡩࡨࠩࡧࡻ࠭ࠥࢁ࡜࡯ࠢࠣࠤࠥࢃ࡜࡯ࠢࠣࡶࡪࡺࡵࡳࡰࠣࡥࡼࡧࡩࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰ࡦࡳࡳࡴࡥࡤࡶࠫࡿࡡࡴࠠࠡࠢࠣࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺ࠺ࠡࡢࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠨࢀ࡫࡮ࡤࡱࡧࡩ࡚ࡘࡉࡄࡱࡰࡴࡴࡴࡥ࡯ࡶࠫࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡨࡧࡰࡴࠫࠬࢁࡥ࠲࡜࡯ࠢࠣࠤࠥ࠴࠮࠯࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳ࡝ࡰࠣࠤࢂ࠯࡜࡯ࡿ࡟ࡲ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࠩ੠")
from ._version import __version__
bstack111ll1llll_opy_ = None
CONFIG = {}
bstack1llll1ll1l_opy_ = {}
bstack1l11lllll1_opy_ = {}
bstack1l1l1l1lll_opy_ = None
bstack1l1ll1ll1_opy_ = None
bstack111ll11111_opy_ = None
bstack11l1l111l1_opy_ = -1
bstack1l111l1l1_opy_ = 0
bstack1ll111lll1_opy_ = bstack11l1l11ll1_opy_
bstack11l1l1l1l1_opy_ = 1
bstack1l1ll1lll1_opy_ = False
bstack1llll1l1l1_opy_ = False
bstack11111ll1l_opy_ = bstack11l11l1_opy_ (u"ࠫࠬ੡")
bstack1l1111l1l1_opy_ = bstack11l11l1_opy_ (u"ࠬ࠭੢")
bstack1l1ll111ll_opy_ = False
bstack1ll11l11ll_opy_ = True
bstack1l1111lll_opy_ = bstack11l11l1_opy_ (u"࠭ࠧ੣")
bstack1lll1111l1_opy_ = []
bstack1111l1lll1_opy_ = threading.Lock()
bstack11ll111lll_opy_ = threading.Lock()
bstack1ll1ll111_opy_ = bstack11l11l1_opy_ (u"ࠧࠨ੤")
bstack111l1l1ll_opy_ = False
bstack1l1l1l1l1l_opy_ = None
bstack111l1l1111_opy_ = None
bstack1ll1lll11_opy_ = None
bstack1l11111l1l_opy_ = -1
bstack1111ll1lll_opy_ = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠨࢀࠪ੥")), bstack11l11l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ੦"), bstack11l11l1_opy_ (u"ࠪ࠲ࡷࡵࡢࡰࡶ࠰ࡶࡪࡶ࡯ࡳࡶ࠰࡬ࡪࡲࡰࡦࡴ࠱࡮ࡸࡵ࡮ࠨ੧"))
bstack1ll11l1l11_opy_ = 0
bstack111ll1ll1_opy_ = 0
bstack1ll1ll1lll_opy_ = []
bstack111111ll1_opy_ = []
bstack11l11ll1l1_opy_ = []
bstack11lll1ll1l_opy_ = []
bstack1111l1111_opy_ = bstack11l11l1_opy_ (u"ࠫࠬ੨")
bstack111l11l11_opy_ = bstack11l11l1_opy_ (u"ࠬ࠭੩")
bstack1l11llllll_opy_ = False
bstack11l1llll11_opy_ = False
bstack111ll1l1l1_opy_ = {}
bstack11ll1ll11_opy_ = None
bstack1l1ll11ll_opy_ = None
bstack11111l111l_opy_ = None
bstack1l1111l1ll_opy_ = None
bstack1l11llll1_opy_ = None
bstack1ll1l1ll1_opy_ = None
bstack1ll11ll111_opy_ = None
bstack111l11l111_opy_ = None
bstack1ll11ll11l_opy_ = None
bstack1l1111l11_opy_ = None
bstack1l111llll_opy_ = None
bstack1l1l1ll11_opy_ = None
bstack11111ll1ll_opy_ = None
bstack1llll1111l_opy_ = None
bstack11l1lll1l1_opy_ = None
bstack1ll1111ll_opy_ = None
bstack1ll1lll1ll_opy_ = None
bstack1lll1l111l_opy_ = None
bstack11llll1lll_opy_ = None
bstack1l1l1l1ll_opy_ = None
bstack1ll1l1lll1_opy_ = None
bstack11ll1l111_opy_ = None
bstack1l111ll11_opy_ = None
thread_local = threading.local()
bstack1111llllll_opy_ = False
bstack1111l1ll11_opy_ = bstack11l11l1_opy_ (u"ࠨࠢ੪")
logger = bstack11111l1l1_opy_.get_logger(__name__, bstack1ll111lll1_opy_)
bstack11111111_opy_ = Config.bstack1llll1ll1_opy_()
percy = bstack1ll1l11l1_opy_()
bstack1ll111111l_opy_ = bstack1ll1l1111_opy_()
bstack1l1ll11l1l_opy_ = bstack11l1l11l_opy_()
def bstack1l111l11l_opy_():
  global CONFIG
  global bstack1l11llllll_opy_
  global bstack11111111_opy_
  testContextOptions = bstack11ll1l111l_opy_(CONFIG)
  if bstack1ll11lll11_opy_(CONFIG):
    if (bstack11l11l1_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ੫") in testContextOptions and str(testContextOptions[bstack11l11l1_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ੬")]).lower() == bstack11l11l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ੭")):
      bstack1l11llllll_opy_ = True
    bstack11111111_opy_.bstack1l11111lll_opy_(testContextOptions.get(bstack11l11l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ੮"), False))
  else:
    bstack1l11llllll_opy_ = True
    bstack11111111_opy_.bstack1l11111lll_opy_(True)
def bstack1ll1l1l111_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11l1ll1l11_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1ll1ll1ll1_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11l11l1_opy_ (u"ࠦ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡨࡵ࡮ࡧ࡫ࡪࡪ࡮ࡲࡥࠣ੯") == args[i].lower() or bstack11l11l1_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡩ࡭࡬ࠨੰ") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1l1111lll_opy_
      bstack1l1111lll_opy_ += bstack11l11l1_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡃࡰࡰࡩ࡭࡬ࡌࡩ࡭ࡧࠣࠫੱ") + shlex.quote(path)
      return path
  return None
bstack111l111l11_opy_ = re.compile(bstack11l11l1_opy_ (u"ࡲࠣ࠰࠭ࡃࡡࠪࡻࠩ࠰࠭ࡃ࠮ࢃ࠮ࠫࡁࠥੲ"))
def bstack1111llll1_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack111l111l11_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11l11l1_opy_ (u"ࠣࠦࡾࠦੳ") + group + bstack11l11l1_opy_ (u"ࠤࢀࠦੴ"), os.environ.get(group))
  return value
def bstack1l111lll11_opy_():
  global bstack1l111ll11_opy_
  if bstack1l111ll11_opy_ is None:
        bstack1l111ll11_opy_ = bstack1ll1ll1ll1_opy_()
  bstack1ll111l1ll_opy_ = bstack1l111ll11_opy_
  if bstack1ll111l1ll_opy_ and os.path.exists(os.path.abspath(bstack1ll111l1ll_opy_)):
    fileName = bstack1ll111l1ll_opy_
  if bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧੵ") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11l11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ੶")])) and not bstack11l11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡑࡥࡲ࡫ࠧ੷") in locals():
    fileName = os.environ[bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࡤࡌࡉࡍࡇࠪ੸")]
  if bstack11l11l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡓࡧ࡭ࡦࠩ੹") in locals():
    bstack1111ll1_opy_ = os.path.abspath(fileName)
  else:
    bstack1111ll1_opy_ = bstack11l11l1_opy_ (u"ࠨࠩ੺")
  bstack11l11111l_opy_ = os.getcwd()
  bstack1ll1l1l1ll_opy_ = bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬ੻")
  bstack11111l1ll_opy_ = bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡥࡲࡲࠧ੼")
  while (not os.path.exists(bstack1111ll1_opy_)) and bstack11l11111l_opy_ != bstack11l11l1_opy_ (u"ࠦࠧ੽"):
    bstack1111ll1_opy_ = os.path.join(bstack11l11111l_opy_, bstack1ll1l1l1ll_opy_)
    if not os.path.exists(bstack1111ll1_opy_):
      bstack1111ll1_opy_ = os.path.join(bstack11l11111l_opy_, bstack11111l1ll_opy_)
    if bstack11l11111l_opy_ != os.path.dirname(bstack11l11111l_opy_):
      bstack11l11111l_opy_ = os.path.dirname(bstack11l11111l_opy_)
    else:
      bstack11l11111l_opy_ = bstack11l11l1_opy_ (u"ࠧࠨ੾")
  bstack1l111ll11_opy_ = bstack1111ll1_opy_ if os.path.exists(bstack1111ll1_opy_) else None
  return bstack1l111ll11_opy_
def bstack1ll1ll111l_opy_(config):
    if bstack11l11l1_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬࠭੿") in config:
      config[bstack11l11l1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ઀")] = config[bstack11l11l1_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࠨઁ")]
    if bstack11l11l1_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࡑࡳࡸ࡮ࡵ࡮ࡴࠩં") in config:
      config[bstack11l11l1_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧઃ")] = config[bstack11l11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࡓࡵࡺࡩࡰࡰࡶࠫ઄")]
def bstack11ll1llll1_opy_():
  bstack1111ll1_opy_ = bstack1l111lll11_opy_()
  if not os.path.exists(bstack1111ll1_opy_):
    bstack11l1l1111_opy_(
      bstack1lll11l111_opy_.format(os.getcwd()))
  try:
    with open(bstack1111ll1_opy_, bstack11l11l1_opy_ (u"ࠬࡸࠧઅ")) as stream:
      yaml.add_implicit_resolver(bstack11l11l1_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢઆ"), bstack111l111l11_opy_)
      yaml.add_constructor(bstack11l11l1_opy_ (u"ࠢࠢࡲࡤࡸ࡭࡫ࡸࠣઇ"), bstack1111llll1_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1ll1ll111l_opy_(config)
      return config
  except:
    with open(bstack1111ll1_opy_, bstack11l11l1_opy_ (u"ࠨࡴࠪઈ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1ll1ll111l_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack11l1l1111_opy_(bstack1l111ll1l1_opy_.format(str(exc)))
def bstack11l111ll1_opy_(config):
  bstack111l1ll1ll_opy_ = bstack1l1l11l1l1_opy_(config)
  for option in list(bstack111l1ll1ll_opy_):
    if option.lower() in bstack1111lll11_opy_ and option != bstack1111lll11_opy_[option.lower()]:
      bstack111l1ll1ll_opy_[bstack1111lll11_opy_[option.lower()]] = bstack111l1ll1ll_opy_[option]
      del bstack111l1ll1ll_opy_[option]
  return config
def bstack1l1llll1l_opy_():
  global bstack1l11lllll1_opy_
  for key, bstack1l11ll111_opy_ in bstack1lll11l11l_opy_.items():
    if isinstance(bstack1l11ll111_opy_, list):
      for var in bstack1l11ll111_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1l11lllll1_opy_[key] = os.environ[var]
          break
    elif bstack1l11ll111_opy_ in os.environ and os.environ[bstack1l11ll111_opy_] and str(os.environ[bstack1l11ll111_opy_]).strip():
      bstack1l11lllll1_opy_[key] = os.environ[bstack1l11ll111_opy_]
  if bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫઉ") in os.environ:
    bstack1l11lllll1_opy_[bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઊ")] = {}
    bstack1l11lllll1_opy_[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨઋ")][bstack11l11l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઌ")] = os.environ[bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨઍ")]
def bstack1ll1ll11l1_opy_():
  global bstack1llll1ll1l_opy_
  global bstack1l1111lll_opy_
  bstack1l1l1l1111_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack11l11l1_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ઎").lower() == val.lower():
      bstack1llll1ll1l_opy_[bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬએ")] = {}
      bstack1llll1ll1l_opy_[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઐ")][bstack11l11l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬઑ")] = sys.argv[idx + 1]
      bstack1l1l1l1111_opy_.extend([idx, idx + 1])
      break
  for key, bstack1111llll11_opy_ in bstack1l1lll1111_opy_.items():
    if isinstance(bstack1111llll11_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack1111llll11_opy_:
          if bstack11l11l1_opy_ (u"ࠫ࠲࠳ࠧ઒") + var.lower() == val.lower() and key not in bstack1llll1ll1l_opy_:
            bstack1llll1ll1l_opy_[key] = sys.argv[idx + 1]
            bstack1l1111lll_opy_ += bstack11l11l1_opy_ (u"ࠬࠦ࠭࠮ࠩઓ") + var + bstack11l11l1_opy_ (u"࠭ࠠࠨઔ") + shlex.quote(sys.argv[idx + 1])
            bstack1l1l1l1111_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack11l11l1_opy_ (u"ࠧ࠮࠯ࠪક") + bstack1111llll11_opy_.lower() == val.lower() and key not in bstack1llll1ll1l_opy_:
          bstack1llll1ll1l_opy_[key] = sys.argv[idx + 1]
          bstack1l1111lll_opy_ += bstack11l11l1_opy_ (u"ࠨࠢ࠰࠱ࠬખ") + bstack1111llll11_opy_ + bstack11l11l1_opy_ (u"ࠩࠣࠫગ") + shlex.quote(sys.argv[idx + 1])
          bstack1l1l1l1111_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack1l1l1l1111_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack11l1lllll_opy_(config):
  bstack11l11l11l1_opy_ = config.keys()
  for bstack1111ll1l1l_opy_, bstack1ll111l111_opy_ in bstack1llll1l111_opy_.items():
    if bstack1ll111l111_opy_ in bstack11l11l11l1_opy_:
      config[bstack1111ll1l1l_opy_] = config[bstack1ll111l111_opy_]
      del config[bstack1ll111l111_opy_]
  for bstack1111ll1l1l_opy_, bstack1ll111l111_opy_ in bstack11lll1l1ll_opy_.items():
    if isinstance(bstack1ll111l111_opy_, list):
      for bstack11l11l1l1_opy_ in bstack1ll111l111_opy_:
        if bstack11l11l1l1_opy_ in bstack11l11l11l1_opy_:
          config[bstack1111ll1l1l_opy_] = config[bstack11l11l1l1_opy_]
          del config[bstack11l11l1l1_opy_]
          break
    elif bstack1ll111l111_opy_ in bstack11l11l11l1_opy_:
      config[bstack1111ll1l1l_opy_] = config[bstack1ll111l111_opy_]
      del config[bstack1ll111l111_opy_]
  for bstack11l11l1l1_opy_ in list(config):
    for bstack11lll11ll_opy_ in bstack1l111l11l1_opy_:
      if bstack11l11l1l1_opy_.lower() == bstack11lll11ll_opy_.lower() and bstack11l11l1l1_opy_ != bstack11lll11ll_opy_:
        config[bstack11lll11ll_opy_] = config[bstack11l11l1l1_opy_]
        del config[bstack11l11l1l1_opy_]
  bstack11l1111ll_opy_ = [{}]
  if not config.get(bstack11l11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ઘ")):
    config[bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧઙ")] = [{}]
  bstack11l1111ll_opy_ = config[bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨચ")]
  for platform in bstack11l1111ll_opy_:
    for bstack11l11l1l1_opy_ in list(platform):
      for bstack11lll11ll_opy_ in bstack1l111l11l1_opy_:
        if bstack11l11l1l1_opy_.lower() == bstack11lll11ll_opy_.lower() and bstack11l11l1l1_opy_ != bstack11lll11ll_opy_:
          platform[bstack11lll11ll_opy_] = platform[bstack11l11l1l1_opy_]
          del platform[bstack11l11l1l1_opy_]
  for bstack1111ll1l1l_opy_, bstack1ll111l111_opy_ in bstack11lll1l1ll_opy_.items():
    for platform in bstack11l1111ll_opy_:
      if isinstance(bstack1ll111l111_opy_, list):
        for bstack11l11l1l1_opy_ in bstack1ll111l111_opy_:
          if bstack11l11l1l1_opy_ in platform:
            platform[bstack1111ll1l1l_opy_] = platform[bstack11l11l1l1_opy_]
            del platform[bstack11l11l1l1_opy_]
            break
      elif bstack1ll111l111_opy_ in platform:
        platform[bstack1111ll1l1l_opy_] = platform[bstack1ll111l111_opy_]
        del platform[bstack1ll111l111_opy_]
  for bstack1l11l11111_opy_ in bstack1llll11ll1_opy_:
    if bstack1l11l11111_opy_ in config:
      if not bstack1llll11ll1_opy_[bstack1l11l11111_opy_] in config:
        config[bstack1llll11ll1_opy_[bstack1l11l11111_opy_]] = {}
      config[bstack1llll11ll1_opy_[bstack1l11l11111_opy_]].update(config[bstack1l11l11111_opy_])
      del config[bstack1l11l11111_opy_]
  for platform in bstack11l1111ll_opy_:
    for bstack1l11l11111_opy_ in bstack1llll11ll1_opy_:
      if bstack1l11l11111_opy_ in list(platform):
        if not bstack1llll11ll1_opy_[bstack1l11l11111_opy_] in platform:
          platform[bstack1llll11ll1_opy_[bstack1l11l11111_opy_]] = {}
        platform[bstack1llll11ll1_opy_[bstack1l11l11111_opy_]].update(platform[bstack1l11l11111_opy_])
        del platform[bstack1l11l11111_opy_]
  config = bstack11l111ll1_opy_(config)
  return config
def bstack11ll1lllll_opy_(config):
  global bstack1l1111l1l1_opy_
  bstack1ll1lllll1_opy_ = False
  if bstack11l11l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪછ") in config and str(config[bstack11l11l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫજ")]).lower() != bstack11l11l1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧઝ"):
    if bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ઞ") not in config or str(config[bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧટ")]).lower() == bstack11l11l1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪઠ"):
      config[bstack11l11l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫડ")] = False
    else:
      bstack1ll1lll1l_opy_ = bstack1l1lll1ll1_opy_()
      if bstack11l11l1_opy_ (u"࠭ࡩࡴࡖࡵ࡭ࡦࡲࡇࡳ࡫ࡧࠫઢ") in bstack1ll1lll1l_opy_:
        if not bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫણ") in config:
          config[bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬત")] = {}
        config[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭થ")][bstack11l11l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬદ")] = bstack11l11l1_opy_ (u"ࠫࡦࡺࡳ࠮ࡴࡨࡴࡪࡧࡴࡦࡴࠪધ")
        bstack1ll1lllll1_opy_ = True
        bstack1l1111l1l1_opy_ = config[bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩન")].get(bstack11l11l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ઩"))
  if bstack1ll11lll11_opy_(config) and bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫપ") in config and str(config[bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬફ")]).lower() != bstack11l11l1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨબ") and not bstack1ll1lllll1_opy_:
    if not bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧભ") in config:
      config[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨમ")] = {}
    if not config[bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩય")].get(bstack11l11l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠪર")) and not bstack11l11l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઱") in config[bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬલ")]:
      bstack1l11ll1l_opy_ = datetime.datetime.now()
      bstack1l11l1l1ll_opy_ = bstack1l11ll1l_opy_.strftime(bstack11l11l1_opy_ (u"ࠩࠨࡨࡤࠫࡢࡠࠧࡋࠩࡒ࠭ળ"))
      hostname = socket.gethostname()
      bstack1111l111l_opy_ = bstack11l11l1_opy_ (u"ࠪࠫ઴").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11l11l1_opy_ (u"ࠫࢀࢃ࡟ࡼࡿࡢࡿࢂ࠭વ").format(bstack1l11l1l1ll_opy_, hostname, bstack1111l111l_opy_)
      config[bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩશ")][bstack11l11l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨષ")] = identifier
    bstack1l1111l1l1_opy_ = config[bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫસ")].get(bstack11l11l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪહ"))
  return config
def bstack1l1l111ll_opy_():
  bstack111lll11ll_opy_ =  bstack11lll11l1_opy_()[bstack11l11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠨ઺")]
  return bstack111lll11ll_opy_ if bstack111lll11ll_opy_ else -1
def bstack11l11lll1l_opy_(bstack111lll11ll_opy_):
  global CONFIG
  if not bstack11l11l1_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬ઻") in CONFIG[bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ઼࠭")]:
    return
  CONFIG[bstack11l11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઽ")] = CONFIG[bstack11l11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨા")].replace(
    bstack11l11l1_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩિ"),
    str(bstack111lll11ll_opy_)
  )
def bstack11111ll1l1_opy_():
  global CONFIG
  if not bstack11l11l1_opy_ (u"ࠨࠦࡾࡈࡆ࡚ࡅࡠࡖࡌࡑࡊࢃࠧી") in CONFIG[bstack11l11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫુ")]:
    return
  bstack1l11ll1l_opy_ = datetime.datetime.now()
  bstack1l11l1l1ll_opy_ = bstack1l11ll1l_opy_.strftime(bstack11l11l1_opy_ (u"ࠪࠩࡩ࠳ࠥࡣ࠯ࠨࡌ࠿ࠫࡍࠨૂ"))
  CONFIG[bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ૃ")] = CONFIG[bstack11l11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૄ")].replace(
    bstack11l11l1_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬૅ"),
    bstack1l11l1l1ll_opy_
  )
def bstack1111l11l1_opy_():
  global CONFIG
  if bstack11l11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૆") in CONFIG and not bool(CONFIG[bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪે")]):
    del CONFIG[bstack11l11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫૈ")]
    return
  if not bstack11l11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૉ") in CONFIG:
    CONFIG[bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૊")] = bstack11l11l1_opy_ (u"ࠬࠩࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨો")
  if bstack11l11l1_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬૌ") in CONFIG[bstack11l11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳ્ࠩ")]:
    bstack11111ll1l1_opy_()
    os.environ[bstack11l11l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ૎")] = CONFIG[bstack11l11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૏")]
  if not bstack11l11l1_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬૐ") in CONFIG[bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૑")]:
    return
  bstack111lll11ll_opy_ = bstack11l11l1_opy_ (u"ࠬ࠭૒")
  bstack1ll11l1111_opy_ = bstack1l1l111ll_opy_()
  if bstack1ll11l1111_opy_ != -1:
    bstack111lll11ll_opy_ = bstack11l11l1_opy_ (u"࠭ࡃࡊࠢࠪ૓") + str(bstack1ll11l1111_opy_)
  if bstack111lll11ll_opy_ == bstack11l11l1_opy_ (u"ࠧࠨ૔"):
    bstack1l1lllll1l_opy_ = bstack11l1ll11l_opy_(CONFIG[bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ૕")])
    if bstack1l1lllll1l_opy_ != -1:
      bstack111lll11ll_opy_ = str(bstack1l1lllll1l_opy_)
  if bstack111lll11ll_opy_:
    bstack11l11lll1l_opy_(bstack111lll11ll_opy_)
    os.environ[bstack11l11l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭૖")] = CONFIG[bstack11l11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૗")]
def bstack111l11ll1l_opy_(bstack111ll111ll_opy_, bstack1l11ll11l1_opy_, path):
  json_data = {
    bstack11l11l1_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૘"): bstack1l11ll11l1_opy_
  }
  if os.path.exists(path):
    bstack1l111l111_opy_ = json.load(open(path, bstack11l11l1_opy_ (u"ࠬࡸࡢࠨ૙")))
  else:
    bstack1l111l111_opy_ = {}
  bstack1l111l111_opy_[bstack111ll111ll_opy_] = json_data
  with open(path, bstack11l11l1_opy_ (u"ࠨࡷࠬࠤ૚")) as outfile:
    json.dump(bstack1l111l111_opy_, outfile)
def bstack11l1ll11l_opy_(bstack111ll111ll_opy_):
  bstack111ll111ll_opy_ = str(bstack111ll111ll_opy_)
  bstack1l11l1111_opy_ = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠧࡿࠩ૛")), bstack11l11l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ૜"))
  try:
    if not os.path.exists(bstack1l11l1111_opy_):
      os.makedirs(bstack1l11l1111_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠩࢁࠫ૝")), bstack11l11l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ૞"), bstack11l11l1_opy_ (u"ࠫ࠳ࡨࡵࡪ࡮ࡧ࠱ࡳࡧ࡭ࡦ࠯ࡦࡥࡨ࡮ࡥ࠯࡬ࡶࡳࡳ࠭૟"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11l11l1_opy_ (u"ࠬࡽࠧૠ")):
        pass
      with open(file_path, bstack11l11l1_opy_ (u"ࠨࡷࠬࠤૡ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11l11l1_opy_ (u"ࠧࡳࠩૢ")) as bstack11l111l11l_opy_:
      bstack11llllllll_opy_ = json.load(bstack11l111l11l_opy_)
    if bstack111ll111ll_opy_ in bstack11llllllll_opy_:
      bstack1l1l11l1l_opy_ = bstack11llllllll_opy_[bstack111ll111ll_opy_][bstack11l11l1_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૣ")]
      bstack1l11111l1_opy_ = int(bstack1l1l11l1l_opy_) + 1
      bstack111l11ll1l_opy_(bstack111ll111ll_opy_, bstack1l11111l1_opy_, file_path)
      return bstack1l11111l1_opy_
    else:
      bstack111l11ll1l_opy_(bstack111ll111ll_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1111l1llll_opy_.format(str(e)))
    return -1
def bstack11lll111l_opy_(config):
  if not config[bstack11l11l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ૤")] or not config[bstack11l11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭૥")]:
    return True
  else:
    return False
def bstack111l1l1ll1_opy_(config, index=0):
  global bstack1l1ll111ll_opy_
  bstack1ll1ll11l_opy_ = {}
  caps = bstack111111lll_opy_ + bstack111llll11_opy_
  if config.get(bstack11l11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ૦"), False):
    bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ૧")] = True
    bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ૨")] = config.get(bstack11l11l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ૩"), {})
  if bstack1l1ll111ll_opy_:
    caps += bstack11lll11ll1_opy_
  for key in config:
    if key in caps + [bstack11l11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૪")]:
      continue
    bstack1ll1ll11l_opy_[key] = config[key]
  if bstack11l11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૫") in config:
    for bstack1lll1llll1_opy_ in config[bstack11l11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૬")][index]:
      if bstack1lll1llll1_opy_ in caps:
        continue
      bstack1ll1ll11l_opy_[bstack1lll1llll1_opy_] = config[bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૭")][index][bstack1lll1llll1_opy_]
  bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"ࠬ࡮࡯ࡴࡶࡑࡥࡲ࡫ࠧ૮")] = socket.gethostname()
  if bstack11l11l1_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧ૯") in bstack1ll1ll11l_opy_:
    del (bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ૰")])
  return bstack1ll1ll11l_opy_
def bstack11lllllll_opy_(config):
  global bstack1l1ll111ll_opy_
  bstack1ll1ll1l1_opy_ = {}
  caps = bstack111llll11_opy_
  if bstack1l1ll111ll_opy_:
    caps += bstack11lll11ll1_opy_
  for key in caps:
    if key in config:
      bstack1ll1ll1l1_opy_[key] = config[key]
  return bstack1ll1ll1l1_opy_
def bstack11l1l11l1_opy_(bstack1ll1ll11l_opy_, bstack1ll1ll1l1_opy_):
  bstack11111ll11l_opy_ = {}
  for key in bstack1ll1ll11l_opy_.keys():
    if key in bstack1llll1l111_opy_:
      bstack11111ll11l_opy_[bstack1llll1l111_opy_[key]] = bstack1ll1ll11l_opy_[key]
    else:
      bstack11111ll11l_opy_[key] = bstack1ll1ll11l_opy_[key]
  for key in bstack1ll1ll1l1_opy_:
    if key in bstack1llll1l111_opy_:
      bstack11111ll11l_opy_[bstack1llll1l111_opy_[key]] = bstack1ll1ll1l1_opy_[key]
    else:
      bstack11111ll11l_opy_[key] = bstack1ll1ll1l1_opy_[key]
  return bstack11111ll11l_opy_
def bstack111ll11l11_opy_(config, index=0):
  global bstack1l1ll111ll_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1111l1l1l1_opy_ = bstack1l1l11l1ll_opy_(bstack11l1l111ll_opy_, config, logger)
  bstack1ll1ll1l1_opy_ = bstack11lllllll_opy_(config)
  bstack1ll1l111ll_opy_ = bstack111llll11_opy_
  bstack1ll1l111ll_opy_ += bstack1ll1ll1l11_opy_
  bstack1ll1ll1l1_opy_ = update(bstack1ll1ll1l1_opy_, bstack1111l1l1l1_opy_)
  if bstack1l1ll111ll_opy_:
    bstack1ll1l111ll_opy_ += bstack11lll11ll1_opy_
  if bstack11l11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૱") in config:
    if bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ૲") in config[bstack11l11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૳")][index]:
      caps[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ૴")] = config[bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૵")][index][bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ૶")]
    if bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ૷") in config[bstack11l11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૸")][index]:
      caps[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪૹ")] = str(config[bstack11l11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ૺ")][index][bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬૻ")])
    bstack111ll1ll11_opy_ = bstack1l1l11l1ll_opy_(bstack11l1l111ll_opy_, config[bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૼ")][index], logger)
    bstack1ll1l111ll_opy_ += list(bstack111ll1ll11_opy_.keys())
    for bstack111l1ll1l1_opy_ in bstack1ll1l111ll_opy_:
      if bstack111l1ll1l1_opy_ in config[bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૽")][index]:
        if bstack111l1ll1l1_opy_ == bstack11l11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ૾"):
          try:
            bstack111ll1ll11_opy_[bstack111l1ll1l1_opy_] = str(config[bstack11l11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૿")][index][bstack111l1ll1l1_opy_] * 1.0)
          except:
            bstack111ll1ll11_opy_[bstack111l1ll1l1_opy_] = str(config[bstack11l11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ଀")][index][bstack111l1ll1l1_opy_])
        else:
          bstack111ll1ll11_opy_[bstack111l1ll1l1_opy_] = config[bstack11l11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଁ")][index][bstack111l1ll1l1_opy_]
        del (config[bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଂ")][index][bstack111l1ll1l1_opy_])
    bstack1ll1ll1l1_opy_ = update(bstack1ll1ll1l1_opy_, bstack111ll1ll11_opy_)
  bstack1ll1ll11l_opy_ = bstack111l1l1ll1_opy_(config, index)
  for bstack11l11l1l1_opy_ in bstack111llll11_opy_ + list(bstack1111l1l1l1_opy_.keys()):
    if bstack11l11l1l1_opy_ in bstack1ll1ll11l_opy_:
      bstack1ll1ll1l1_opy_[bstack11l11l1l1_opy_] = bstack1ll1ll11l_opy_[bstack11l11l1l1_opy_]
      del (bstack1ll1ll11l_opy_[bstack11l11l1l1_opy_])
  if bstack1l1l1111ll_opy_(config):
    bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬଃ")] = True
    caps.update(bstack1ll1ll1l1_opy_)
    caps[bstack11l11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ଄")] = bstack1ll1ll11l_opy_
  else:
    bstack1ll1ll11l_opy_[bstack11l11l1_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧଅ")] = False
    caps.update(bstack11l1l11l1_opy_(bstack1ll1ll11l_opy_, bstack1ll1ll1l1_opy_))
    if bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ଆ") in caps:
      caps[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪଇ")] = caps[bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଈ")]
      del (caps[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଉ")])
    if bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଊ") in caps:
      caps[bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨଋ")] = caps[bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨଌ")]
      del (caps[bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ଍")])
  return caps
def bstack11ll1ll1ll_opy_():
  global bstack1ll1ll111_opy_
  global CONFIG
  if bstack11l1ll1l11_opy_() <= version.parse(bstack11l11l1_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩ଎")):
    if bstack1ll1ll111_opy_ != bstack11l11l1_opy_ (u"ࠪࠫଏ"):
      return bstack11l11l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧଐ") + bstack1ll1ll111_opy_ + bstack11l11l1_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤ଑")
    return bstack111lll111_opy_
  if bstack1ll1ll111_opy_ != bstack11l11l1_opy_ (u"࠭ࠧ଒"):
    return bstack11l11l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤଓ") + bstack1ll1ll111_opy_ + bstack11l11l1_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤଔ")
  return bstack11ll11ll11_opy_
def bstack1l1l1ll1l_opy_(options):
  return hasattr(options, bstack11l11l1_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪକ"))
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
def bstack1ll111111_opy_(options, bstack111l1ll1l_opy_):
  for bstack1l11l1l111_opy_ in bstack111l1ll1l_opy_:
    if bstack1l11l1l111_opy_ in [bstack11l11l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଖ"), bstack11l11l1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨଗ")]:
      continue
    if bstack1l11l1l111_opy_ in options._experimental_options:
      options._experimental_options[bstack1l11l1l111_opy_] = update(options._experimental_options[bstack1l11l1l111_opy_],
                                                         bstack111l1ll1l_opy_[bstack1l11l1l111_opy_])
    else:
      options.add_experimental_option(bstack1l11l1l111_opy_, bstack111l1ll1l_opy_[bstack1l11l1l111_opy_])
  if bstack11l11l1_opy_ (u"ࠬࡧࡲࡨࡵࠪଘ") in bstack111l1ll1l_opy_:
    for arg in bstack111l1ll1l_opy_[bstack11l11l1_opy_ (u"࠭ࡡࡳࡩࡶࠫଙ")]:
      options.add_argument(arg)
    del (bstack111l1ll1l_opy_[bstack11l11l1_opy_ (u"ࠧࡢࡴࡪࡷࠬଚ")])
  if bstack11l11l1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬଛ") in bstack111l1ll1l_opy_:
    for ext in bstack111l1ll1l_opy_[bstack11l11l1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ଜ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack111l1ll1l_opy_[bstack11l11l1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧଝ")])
def bstack1l11111ll1_opy_(options, bstack11ll1111l_opy_):
  if bstack11l11l1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪଞ") in bstack11ll1111l_opy_:
    for bstack1l11l1ll1l_opy_ in bstack11ll1111l_opy_[bstack11l11l1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫଟ")]:
      if bstack1l11l1ll1l_opy_ in options._preferences:
        options._preferences[bstack1l11l1ll1l_opy_] = update(options._preferences[bstack1l11l1ll1l_opy_], bstack11ll1111l_opy_[bstack11l11l1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬଠ")][bstack1l11l1ll1l_opy_])
      else:
        options.set_preference(bstack1l11l1ll1l_opy_, bstack11ll1111l_opy_[bstack11l11l1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ଡ")][bstack1l11l1ll1l_opy_])
  if bstack11l11l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଢ") in bstack11ll1111l_opy_:
    for arg in bstack11ll1111l_opy_[bstack11l11l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧଣ")]:
      options.add_argument(arg)
def bstack1l1111llll_opy_(options, bstack1lll1lll1l_opy_):
  if bstack11l11l1_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫତ") in bstack1lll1lll1l_opy_:
    options.use_webview(bool(bstack1lll1lll1l_opy_[bstack11l11l1_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬଥ")]))
  bstack1ll111111_opy_(options, bstack1lll1lll1l_opy_)
def bstack11ll1ll11l_opy_(options, bstack1l1ll1l11l_opy_):
  for bstack11l111lll1_opy_ in bstack1l1ll1l11l_opy_:
    if bstack11l111lll1_opy_ in [bstack11l11l1_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩଦ"), bstack11l11l1_opy_ (u"࠭ࡡࡳࡩࡶࠫଧ")]:
      continue
    options.set_capability(bstack11l111lll1_opy_, bstack1l1ll1l11l_opy_[bstack11l111lll1_opy_])
  if bstack11l11l1_opy_ (u"ࠧࡢࡴࡪࡷࠬନ") in bstack1l1ll1l11l_opy_:
    for arg in bstack1l1ll1l11l_opy_[bstack11l11l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭଩")]:
      options.add_argument(arg)
  if bstack11l11l1_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭ପ") in bstack1l1ll1l11l_opy_:
    options.bstack11lll1llll_opy_(bool(bstack1l1ll1l11l_opy_[bstack11l11l1_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧଫ")]))
def bstack1l111ll1l_opy_(options, bstack11lllll1ll_opy_):
  for bstack1ll11ll1l_opy_ in bstack11lllll1ll_opy_:
    if bstack1ll11ll1l_opy_ in [bstack11l11l1_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨବ"), bstack11l11l1_opy_ (u"ࠬࡧࡲࡨࡵࠪଭ")]:
      continue
    options._options[bstack1ll11ll1l_opy_] = bstack11lllll1ll_opy_[bstack1ll11ll1l_opy_]
  if bstack11l11l1_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪମ") in bstack11lllll1ll_opy_:
    for bstack111lllll1_opy_ in bstack11lllll1ll_opy_[bstack11l11l1_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଯ")]:
      options.bstack1111l1l1ll_opy_(
        bstack111lllll1_opy_, bstack11lllll1ll_opy_[bstack11l11l1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬର")][bstack111lllll1_opy_])
  if bstack11l11l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ଱") in bstack11lllll1ll_opy_:
    for arg in bstack11lllll1ll_opy_[bstack11l11l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଲ")]:
      options.add_argument(arg)
def bstack1ll111ll11_opy_(options, caps):
  if not hasattr(options, bstack11l11l1_opy_ (u"ࠫࡐࡋ࡙ࠨଳ")):
    return
  if options.KEY == bstack11l11l1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ଴"):
    options = bstack111llll1_opy_.bstack11lll1l11_opy_(bstack1ll1l1lll_opy_=options, config=CONFIG)
  if options.KEY == bstack11l11l1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫଵ") and options.KEY in caps:
    bstack1ll111111_opy_(options, caps[bstack11l11l1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬଶ")])
  elif options.KEY == bstack11l11l1_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ଷ") and options.KEY in caps:
    bstack1l11111ll1_opy_(options, caps[bstack11l11l1_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧସ")])
  elif options.KEY == bstack11l11l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫହ") and options.KEY in caps:
    bstack11ll1ll11l_opy_(options, caps[bstack11l11l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬ଺")])
  elif options.KEY == bstack11l11l1_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭଻") and options.KEY in caps:
    bstack1l1111llll_opy_(options, caps[bstack11l11l1_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹ଼ࠧ")])
  elif options.KEY == bstack11l11l1_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ଽ") and options.KEY in caps:
    bstack1l111ll1l_opy_(options, caps[bstack11l11l1_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧା")])
def bstack111llll1l_opy_(caps):
  global bstack1l1ll111ll_opy_
  if isinstance(os.environ.get(bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪି")), str):
    bstack1l1ll111ll_opy_ = eval(os.getenv(bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫୀ")))
  if bstack1l1ll111ll_opy_:
    if bstack1ll1l1l111_opy_() < version.parse(bstack11l11l1_opy_ (u"ࠫ࠷࠴࠳࠯࠲ࠪୁ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11l11l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬୂ")
    if bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫୃ") in caps:
      browser = caps[bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬୄ")]
    elif bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ୅") in caps:
      browser = caps[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪ୆")]
    browser = str(browser).lower()
    if browser == bstack11l11l1_opy_ (u"ࠪ࡭ࡵ࡮࡯࡯ࡧࠪେ") or browser == bstack11l11l1_opy_ (u"ࠫ࡮ࡶࡡࡥࠩୈ"):
      browser = bstack11l11l1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬ୉")
    if browser == bstack11l11l1_opy_ (u"࠭ࡳࡢ࡯ࡶࡹࡳ࡭ࠧ୊"):
      browser = bstack11l11l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧୋ")
    if browser not in [bstack11l11l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨୌ"), bstack11l11l1_opy_ (u"ࠩࡨࡨ࡬࡫୍ࠧ"), bstack11l11l1_opy_ (u"ࠪ࡭ࡪ࠭୎"), bstack11l11l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫ୏"), bstack11l11l1_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭୐")]:
      return None
    try:
      package = bstack11l11l1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࢀࢃ࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ୑").format(browser)
      name = bstack11l11l1_opy_ (u"ࠧࡐࡲࡷ࡭ࡴࡴࡳࠨ୒")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1l1l1ll1l_opy_(options):
        return None
      for bstack11l11l1l1_opy_ in caps.keys():
        options.set_capability(bstack11l11l1l1_opy_, caps[bstack11l11l1l1_opy_])
      bstack1ll111ll11_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack11l1lll11l_opy_(options, bstack1lllll1l1l_opy_):
  if not bstack1l1l1ll1l_opy_(options):
    return
  for bstack11l11l1l1_opy_ in bstack1lllll1l1l_opy_.keys():
    if bstack11l11l1l1_opy_ in bstack1ll1ll1l11_opy_:
      continue
    if bstack11l11l1l1_opy_ in options._caps and type(options._caps[bstack11l11l1l1_opy_]) in [dict, list]:
      options._caps[bstack11l11l1l1_opy_] = update(options._caps[bstack11l11l1l1_opy_], bstack1lllll1l1l_opy_[bstack11l11l1l1_opy_])
    else:
      options.set_capability(bstack11l11l1l1_opy_, bstack1lllll1l1l_opy_[bstack11l11l1l1_opy_])
  bstack1ll111ll11_opy_(options, bstack1lllll1l1l_opy_)
  if bstack11l11l1_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧ୓") in options._caps:
    if options._caps[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ୔")] and options._caps[bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ୕")].lower() != bstack11l11l1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬୖ"):
      del options._caps[bstack11l11l1_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡧࡩࡧࡻࡧࡨࡧࡵࡅࡩࡪࡲࡦࡵࡶࠫୗ")]
def bstack111lll1lll_opy_(proxy_config):
  if bstack11l11l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ୘") in proxy_config:
    proxy_config[bstack11l11l1_opy_ (u"ࠧࡴࡵ࡯ࡔࡷࡵࡸࡺࠩ୙")] = proxy_config[bstack11l11l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ୚")]
    del (proxy_config[bstack11l11l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭୛")])
  if bstack11l11l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭ଡ଼") in proxy_config and proxy_config[bstack11l11l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧଢ଼")].lower() != bstack11l11l1_opy_ (u"ࠬࡪࡩࡳࡧࡦࡸࠬ୞"):
    proxy_config[bstack11l11l1_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩୟ")] = bstack11l11l1_opy_ (u"ࠧ࡮ࡣࡱࡹࡦࡲࠧୠ")
  if bstack11l11l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡁࡶࡶࡲࡧࡴࡴࡦࡪࡩࡘࡶࡱ࠭ୡ") in proxy_config:
    proxy_config[bstack11l11l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬୢ")] = bstack11l11l1_opy_ (u"ࠪࡴࡦࡩࠧୣ")
  return proxy_config
def bstack11ll1l1ll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11l11l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ୤") in config:
    return proxy
  config[bstack11l11l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ୥")] = bstack111lll1lll_opy_(config[bstack11l11l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୦")])
  if proxy == None:
    proxy = Proxy(config[bstack11l11l1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭୧")])
  return proxy
def bstack1llll111ll_opy_(self):
  global CONFIG
  global bstack1l1l1ll11_opy_
  try:
    proxy = bstack1lllll11l1_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11l11l1_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭୨")):
        proxies = bstack1111l11lll_opy_(proxy, bstack11ll1ll1ll_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll1ll1ll_opy_ = proxies.popitem()
          if bstack11l11l1_opy_ (u"ࠤ࠽࠳࠴ࠨ୩") in bstack1ll1ll1ll_opy_:
            return bstack1ll1ll1ll_opy_
          else:
            return bstack11l11l1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ୪") + bstack1ll1ll1ll_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11l11l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡱࡴࡲࡼࡾࠦࡵࡳ࡮ࠣ࠾ࠥࢁࡽࠣ୫").format(str(e)))
  return bstack1l1l1ll11_opy_(self)
def bstack11l1l1lll1_opy_():
  global CONFIG
  return bstack1lll1l1l11_opy_(CONFIG) and bstack1lll1l1l1l_opy_() and bstack11l1ll1l11_opy_() >= version.parse(bstack1111l1l11_opy_)
def bstack1ll11l1ll_opy_():
  global CONFIG
  return (bstack11l11l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ୬") in CONFIG or bstack11l11l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ୭") in CONFIG) and bstack1l1l11111l_opy_()
def bstack1l1l11l1l1_opy_(config):
  bstack111l1ll1ll_opy_ = {}
  if bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୮") in config:
    bstack111l1ll1ll_opy_ = config[bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୯")]
  if bstack11l11l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୰") in config:
    bstack111l1ll1ll_opy_ = config[bstack11l11l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩୱ")]
  proxy = bstack1lllll11l1_opy_(config)
  if proxy:
    if proxy.endswith(bstack11l11l1_opy_ (u"ࠫ࠳ࡶࡡࡤࠩ୲")) and os.path.isfile(proxy):
      bstack111l1ll1ll_opy_[bstack11l11l1_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨ୳")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11l11l1_opy_ (u"࠭࠮ࡱࡣࡦࠫ୴")):
        proxies = bstack11l1ll111_opy_(config, bstack11ll1ll1ll_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll1ll1ll_opy_ = proxies.popitem()
          if bstack11l11l1_opy_ (u"ࠢ࠻࠱࠲ࠦ୵") in bstack1ll1ll1ll_opy_:
            parsed_url = urlparse(bstack1ll1ll1ll_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11l11l1_opy_ (u"ࠣ࠼࠲࠳ࠧ୶") + bstack1ll1ll1ll_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack111l1ll1ll_opy_[bstack11l11l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬ୷")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack111l1ll1ll_opy_[bstack11l11l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭୸")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack111l1ll1ll_opy_[bstack11l11l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧ୹")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack111l1ll1ll_opy_[bstack11l11l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨ୺")] = str(parsed_url.password)
  return bstack111l1ll1ll_opy_
def bstack11ll1l111l_opy_(config):
  if bstack11l11l1_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫ୻") in config:
    return config[bstack11l11l1_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬ୼")]
  return {}
def bstack1lllll11ll_opy_(caps):
  global bstack1l1111l1l1_opy_
  if bstack11l11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ୽") in caps:
    caps[bstack11l11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ୾")][bstack11l11l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩ୿")] = True
    if bstack1l1111l1l1_opy_:
      caps[bstack11l11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ஀")][bstack11l11l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ஁")] = bstack1l1111l1l1_opy_
  else:
    caps[bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫஂ")] = True
    if bstack1l1111l1l1_opy_:
      caps[bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨஃ")] = bstack1l1111l1l1_opy_
@measure(event_name=EVENTS.bstack1l1llll111_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack111l1l1lll_opy_():
  global CONFIG
  if not bstack1ll11lll11_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ஄") in CONFIG and bstack111lll11l1_opy_(CONFIG[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭அ")]):
    if (
      bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧஆ") in CONFIG
      and bstack111lll11l1_opy_(CONFIG[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨஇ")].get(bstack11l11l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩஈ")))
    ):
      logger.debug(bstack11l11l1_opy_ (u"ࠨࡌࡰࡥࡤࡰࠥࡨࡩ࡯ࡣࡵࡽࠥࡴ࡯ࡵࠢࡶࡸࡦࡸࡴࡦࡦࠣࡥࡸࠦࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡥ࡯ࡣࡥࡰࡪࡪࠢஉ"))
      return
    bstack111l1ll1ll_opy_ = bstack1l1l11l1l1_opy_(CONFIG)
    bstack1ll111l1l_opy_(CONFIG[bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪஊ")], bstack111l1ll1ll_opy_)
def bstack1ll111l1l_opy_(key, bstack111l1ll1ll_opy_):
  global bstack111ll1llll_opy_
  logger.info(bstack11lllllll1_opy_)
  try:
    bstack111ll1llll_opy_ = Local()
    bstack11l1lll1ll_opy_ = {bstack11l11l1_opy_ (u"ࠨ࡭ࡨࡽࠬ஋"): key}
    bstack11l1lll1ll_opy_.update(bstack111l1ll1ll_opy_)
    logger.debug(bstack1l11l1lll_opy_.format(str(bstack11l1lll1ll_opy_)).replace(key, bstack11l11l1_opy_ (u"ࠩ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭஌")))
    bstack111ll1llll_opy_.start(**bstack11l1lll1ll_opy_)
    if bstack111ll1llll_opy_.isRunning():
      logger.info(bstack1l1ll1111l_opy_)
  except Exception as e:
    bstack11l1l1111_opy_(bstack1ll1111111_opy_.format(str(e)))
def bstack11lll1l1l_opy_():
  global bstack111ll1llll_opy_
  if bstack111ll1llll_opy_.isRunning():
    logger.info(bstack11lll111ll_opy_)
    bstack111ll1llll_opy_.stop()
  bstack111ll1llll_opy_ = None
def bstack11l1111111_opy_(bstack11ll11llll_opy_=[]):
  global CONFIG
  bstack11l11ll1ll_opy_ = []
  bstack1l1111ll1l_opy_ = [bstack11l11l1_opy_ (u"ࠪࡳࡸ࠭஍"), bstack11l11l1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧஎ"), bstack11l11l1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩஏ"), bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨஐ"), bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ஑"), bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩஒ")]
  try:
    for err in bstack11ll11llll_opy_:
      bstack1l111lll1l_opy_ = {}
      for k in bstack1l1111ll1l_opy_:
        val = CONFIG[bstack11l11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬஓ")][int(err[bstack11l11l1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩஔ")])].get(k)
        if val:
          bstack1l111lll1l_opy_[k] = val
      if(err[bstack11l11l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪக")] != bstack11l11l1_opy_ (u"ࠬ࠭஖")):
        bstack1l111lll1l_opy_[bstack11l11l1_opy_ (u"࠭ࡴࡦࡵࡷࡷࠬ஗")] = {
          err[bstack11l11l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ஘")]: err[bstack11l11l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧங")]
        }
        bstack11l11ll1ll_opy_.append(bstack1l111lll1l_opy_)
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫ࡵࡲ࡮ࡣࡷࡸ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵ࠼ࠣࠫச") + str(e))
  finally:
    return bstack11l11ll1ll_opy_
def bstack11l1l1ll1_opy_(file_name):
  bstack1111lll1ll_opy_ = []
  try:
    bstack1111ll1ll_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1111ll1ll_opy_):
      with open(bstack1111ll1ll_opy_) as f:
        bstack11l1ll1ll1_opy_ = json.load(f)
        bstack1111lll1ll_opy_ = bstack11l1ll1ll1_opy_
      os.remove(bstack1111ll1ll_opy_)
    return bstack1111lll1ll_opy_
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡩ࡯ࡦ࡬ࡲ࡬ࠦࡥࡳࡴࡲࡶࠥࡲࡩࡴࡶ࠽ࠤࠬ஛") + str(e))
    return bstack1111lll1ll_opy_
def bstack111l11l1l1_opy_():
  try:
      from bstack_utils.constants import bstack11ll111l1l_opy_, EVENTS
      from bstack_utils.helper import bstack1ll1l1l11l_opy_, get_host_info, bstack11111111_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack1l1llll1ll_opy_ = os.path.join(os.getcwd(), bstack11l11l1_opy_ (u"ࠫࡱࡵࡧࠨஜ"), bstack11l11l1_opy_ (u"ࠬࡱࡥࡺ࠯ࡰࡩࡹࡸࡩࡤࡵ࠱࡮ࡸࡵ࡮ࠨ஝"))
      lock = FileLock(bstack1l1llll1ll_opy_+bstack11l11l1_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧஞ"))
      def bstack1l1ll111_opy_():
          try:
              with lock:
                  with open(bstack1l1llll1ll_opy_, bstack11l11l1_opy_ (u"ࠢࡳࠤட"), encoding=bstack11l11l1_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢ஠")) as file:
                      data = json.load(file)
                      config = {
                          bstack11l11l1_opy_ (u"ࠤ࡫ࡩࡦࡪࡥࡳࡵࠥ஡"): {
                              bstack11l11l1_opy_ (u"ࠥࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠤ஢"): bstack11l11l1_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠢண"),
                          }
                      }
                      bstack1l1lll11l_opy_ = datetime.utcnow()
                      bstack1l11ll1l_opy_ = bstack1l1lll11l_opy_.strftime(bstack11l11l1_opy_ (u"࡙ࠧࠫ࠮ࠧࡰ࠱ࠪࡪࡔࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪ࡛ࠥࡔࡄࠤத"))
                      test_id = os.environ.get(bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ஥")) if os.environ.get(bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ஦")) else bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥ஧"))
                      payload = {
                          bstack11l11l1_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࠨந"): bstack11l11l1_opy_ (u"ࠥࡷࡩࡱ࡟ࡦࡸࡨࡲࡹࡹࠢன"),
                          bstack11l11l1_opy_ (u"ࠦࡩࡧࡴࡢࠤப"): {
                              bstack11l11l1_opy_ (u"ࠧࡺࡥࡴࡶ࡫ࡹࡧࡥࡵࡶ࡫ࡧࠦ஫"): test_id,
                              bstack11l11l1_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡪ࡟ࡥࡣࡼࠦ஬"): bstack1l11ll1l_opy_,
                              bstack11l11l1_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࠦ஭"): bstack11l11l1_opy_ (u"ࠣࡕࡇࡏࡋ࡫ࡡࡵࡷࡵࡩࡕ࡫ࡲࡧࡱࡵࡱࡦࡴࡣࡦࠤம"),
                              bstack11l11l1_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠ࡬ࡶࡳࡳࠨய"): {
                                  bstack11l11l1_opy_ (u"ࠥࡱࡪࡧࡳࡶࡴࡨࡷࠧர"): data,
                                  bstack11l11l1_opy_ (u"ࠦࡸࡪ࡫ࡓࡷࡱࡍࡩࠨற"): bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢல"))
                              },
                              bstack11l11l1_opy_ (u"ࠨࡵࡴࡧࡵࡣࡩࡧࡴࡢࠤள"): bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠢࡶࡵࡨࡶࡓࡧ࡭ࡦࠤழ")),
                              bstack11l11l1_opy_ (u"ࠣࡪࡲࡷࡹࡥࡩ࡯ࡨࡲࠦவ"): get_host_info()
                          }
                      }
                      bstack11ll1111l1_opy_ = bstack11l1lll1l_opy_(cli.config, [bstack11l11l1_opy_ (u"ࠤࡤࡴ࡮ࡹࠢஶ"), bstack11l11l1_opy_ (u"ࠥࡩࡩࡹࡉ࡯ࡵࡷࡶࡺࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠣஷ"), bstack11l11l1_opy_ (u"ࠦࡦࡶࡩࠣஸ")], bstack11ll111l1l_opy_)
                      response = bstack1ll1l1l11l_opy_(bstack11l11l1_opy_ (u"ࠧࡖࡏࡔࡖࠥஹ"), bstack11ll1111l1_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack11l11l1_opy_ (u"ࠨࡄࡢࡶࡤࠤࡸ࡫࡮ࡵࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡶࡲࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡪࡡࡵࡣࠣࡿࢂࠨ஺").format(bstack11ll111l1l_opy_, payload))
                      else:
                          logger.debug(bstack11l11l1_opy_ (u"ࠢࡓࡧࡴࡹࡪࡹࡴࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡨࡲࡶࠥࢁࡽࠡࡹ࡬ࡸ࡭ࠦࡤࡢࡶࡤࠤࢀࢃࠢ஻").format(bstack11ll111l1l_opy_, payload))
          except Exception as e:
              logger.debug(bstack11l11l1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫࡮ࡥࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢࡾࢁࠧ஼").format(e))
      bstack1l1ll111_opy_()
      bstack11111111l_opy_(bstack1l1llll1ll_opy_, logger)
  except:
    pass
def bstack1l1ll111l_opy_():
  global bstack1111l1ll11_opy_
  global bstack1lll1111l1_opy_
  global bstack1ll1ll1lll_opy_
  global bstack111111ll1_opy_
  global bstack11l11ll1l1_opy_
  global bstack111l11l11_opy_
  global CONFIG
  bstack1l11lllll_opy_ = os.environ.get(bstack11l11l1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪ஽"))
  if bstack1l11lllll_opy_ in [bstack11l11l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩா"), bstack11l11l1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪி")]:
    bstack1111lll11l_opy_()
  percy.shutdown()
  if bstack1111l1ll11_opy_:
    logger.warning(bstack111l111ll_opy_.format(str(bstack1111l1ll11_opy_)))
  else:
    try:
      bstack1l111l111_opy_ = bstack1111l11l1l_opy_(bstack11l11l1_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫீ"), logger)
      if bstack1l111l111_opy_.get(bstack11l11l1_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫு")) and bstack1l111l111_opy_.get(bstack11l11l1_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬூ")).get(bstack11l11l1_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪ௃")):
        logger.warning(bstack111l111ll_opy_.format(str(bstack1l111l111_opy_[bstack11l11l1_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ௄")][bstack11l11l1_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬ௅")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1111ll1ll1_opy_.invoke(Events.bstack11l11ll1l_opy_)
  logger.info(bstack11l11llll1_opy_)
  global bstack111ll1llll_opy_
  if bstack111ll1llll_opy_:
    bstack11lll1l1l_opy_()
  try:
    with bstack1111l1lll1_opy_:
      bstack1l1l1ll1ll_opy_ = bstack1lll1111l1_opy_.copy()
    for driver in bstack1l1l1ll1ll_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1111lllll_opy_)
  if bstack111l11l11_opy_ == bstack11l11l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪெ"):
    bstack11l11ll1l1_opy_ = bstack11l1l1ll1_opy_(bstack11l11l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ே"))
  if bstack111l11l11_opy_ == bstack11l11l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ை") and len(bstack111111ll1_opy_) == 0:
    bstack111111ll1_opy_ = bstack11l1l1ll1_opy_(bstack11l11l1_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ௉"))
    if len(bstack111111ll1_opy_) == 0:
      bstack111111ll1_opy_ = bstack11l1l1ll1_opy_(bstack11l11l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧொ"))
  bstack11l111l1l1_opy_ = bstack11l11l1_opy_ (u"ࠩࠪோ")
  if len(bstack1ll1ll1lll_opy_) > 0:
    bstack11l111l1l1_opy_ = bstack11l1111111_opy_(bstack1ll1ll1lll_opy_)
  elif len(bstack111111ll1_opy_) > 0:
    bstack11l111l1l1_opy_ = bstack11l1111111_opy_(bstack111111ll1_opy_)
  elif len(bstack11l11ll1l1_opy_) > 0:
    bstack11l111l1l1_opy_ = bstack11l1111111_opy_(bstack11l11ll1l1_opy_)
  elif len(bstack11lll1ll1l_opy_) > 0:
    bstack11l111l1l1_opy_ = bstack11l1111111_opy_(bstack11lll1ll1l_opy_)
  if bool(bstack11l111l1l1_opy_):
    bstack11ll11l1ll_opy_(bstack11l111l1l1_opy_)
  else:
    bstack11ll11l1ll_opy_()
  bstack11111111l_opy_(bstack1l11ll11ll_opy_, logger)
  if bstack1l11lllll_opy_ not in [bstack11l11l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫௌ")]:
    bstack111l11l1l1_opy_()
  bstack11111l1l1_opy_.bstack1l11l11l_opy_(CONFIG)
  if len(bstack11l11ll1l1_opy_) > 0:
    sys.exit(len(bstack11l11ll1l1_opy_))
def bstack11111lll1_opy_(bstack1llllllll1_opy_, frame):
  global bstack11111111_opy_
  logger.error(bstack1l1l1lll11_opy_)
  bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡓࡵ்ࠧ"), bstack1llllllll1_opy_)
  if hasattr(signal, bstack11l11l1_opy_ (u"࡙ࠬࡩࡨࡰࡤࡰࡸ࠭௎")):
    bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭௏"), signal.Signals(bstack1llllllll1_opy_).name)
  else:
    bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧௐ"), bstack11l11l1_opy_ (u"ࠨࡕࡌࡋ࡚ࡔࡋࡏࡑ࡚ࡒࠬ௑"))
  if cli.is_running():
    bstack1111ll1ll1_opy_.invoke(Events.bstack11l11ll1l_opy_)
  bstack1l11lllll_opy_ = os.environ.get(bstack11l11l1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪ௒"))
  if bstack1l11lllll_opy_ == bstack11l11l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ௓") and not cli.is_enabled(CONFIG):
    bstack1l11l111_opy_.stop(bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ௔")))
  bstack1l1ll111l_opy_()
  sys.exit(1)
def bstack11l1l1111_opy_(err):
  logger.critical(bstack11l1ll1l1l_opy_.format(str(err)))
  bstack11ll11l1ll_opy_(bstack11l1ll1l1l_opy_.format(str(err)), True)
  atexit.unregister(bstack1l1ll111l_opy_)
  bstack1111lll11l_opy_()
  sys.exit(1)
def bstack11111l111_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack11ll11l1ll_opy_(message, True)
  atexit.unregister(bstack1l1ll111l_opy_)
  bstack1111lll11l_opy_()
  sys.exit(1)
def bstack11l111lll_opy_():
  global CONFIG
  global bstack1llll1ll1l_opy_
  global bstack1l11lllll1_opy_
  global bstack1ll11l11ll_opy_
  CONFIG = bstack11ll1llll1_opy_()
  load_dotenv(CONFIG.get(bstack11l11l1_opy_ (u"ࠬ࡫࡮ࡷࡈ࡬ࡰࡪ࠭௕")))
  bstack1l1llll1l_opy_()
  bstack1ll1ll11l1_opy_()
  CONFIG = bstack11l1lllll_opy_(CONFIG)
  update(CONFIG, bstack1l11lllll1_opy_)
  update(CONFIG, bstack1llll1ll1l_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack11ll1lllll_opy_(CONFIG)
  bstack1ll11l11ll_opy_ = bstack1ll11lll11_opy_(CONFIG)
  os.environ[bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩ௖")] = bstack1ll11l11ll_opy_.__str__().lower()
  bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨௗ"), bstack1ll11l11ll_opy_)
  if (bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௘") in CONFIG and bstack11l11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௙") in bstack1llll1ll1l_opy_) or (
          bstack11l11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௚") in CONFIG and bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௛") not in bstack1l11lllll1_opy_):
    if os.getenv(bstack11l11l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ௜")):
      CONFIG[bstack11l11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ௝")] = os.getenv(bstack11l11l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ௞"))
    else:
      if not CONFIG.get(bstack11l11l1_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠦ௟"), bstack11l11l1_opy_ (u"ࠤࠥ௠")) in bstack1l11ll11l_opy_:
        bstack1111l11l1_opy_()
  elif (bstack11l11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௡") not in CONFIG and bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௢") in CONFIG) or (
          bstack11l11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௣") in bstack1l11lllll1_opy_ and bstack11l11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௤") not in bstack1llll1ll1l_opy_):
    del (CONFIG[bstack11l11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ௥")])
  if bstack11lll111l_opy_(CONFIG):
    bstack11l1l1111_opy_(bstack111llll11l_opy_)
  Config.bstack1llll1ll1_opy_().set_property(bstack11l11l1_opy_ (u"ࠣࡷࡶࡩࡷࡔࡡ࡮ࡧࠥ௦"), CONFIG[bstack11l11l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ௧")])
  bstack1l111l1l1l_opy_()
  bstack111l1l11ll_opy_()
  if bstack1l1ll111ll_opy_ and not CONFIG.get(bstack11l11l1_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠨ௨"), bstack11l11l1_opy_ (u"ࠦࠧ௩")) in bstack1l11ll11l_opy_:
    CONFIG[bstack11l11l1_opy_ (u"ࠬࡧࡰࡱࠩ௪")] = bstack11lll11l1l_opy_(CONFIG)
    logger.info(bstack1l1lll1l11_opy_.format(CONFIG[bstack11l11l1_opy_ (u"࠭ࡡࡱࡲࠪ௫")]))
  if not bstack1ll11l11ll_opy_:
    CONFIG[bstack11l11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ௬")] = [{}]
def bstack1111l1ll1_opy_(config, bstack11llll11ll_opy_):
  global CONFIG
  global bstack1l1ll111ll_opy_
  CONFIG = config
  bstack1l1ll111ll_opy_ = bstack11llll11ll_opy_
def bstack111l1l11ll_opy_():
  global CONFIG
  global bstack1l1ll111ll_opy_
  if bstack11l11l1_opy_ (u"ࠨࡣࡳࡴࠬ௭") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack11111l111_opy_(e, bstack1l111l1ll1_opy_)
    bstack1l1ll111ll_opy_ = True
    bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ௮"), True)
def bstack11lll11l1l_opy_(config):
  bstack11l111111_opy_ = bstack11l11l1_opy_ (u"ࠪࠫ௯")
  app = config[bstack11l11l1_opy_ (u"ࠫࡦࡶࡰࠨ௰")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack111l1lllll_opy_:
      if os.path.exists(app):
        bstack11l111111_opy_ = bstack1l11lll111_opy_(config, app)
      elif bstack11llll11l_opy_(app):
        bstack11l111111_opy_ = app
      else:
        bstack11l1l1111_opy_(bstack1l11l111l1_opy_.format(app))
    else:
      if bstack11llll11l_opy_(app):
        bstack11l111111_opy_ = app
      elif os.path.exists(app):
        bstack11l111111_opy_ = bstack1l11lll111_opy_(app)
      else:
        bstack11l1l1111_opy_(bstack1l1l1l11ll_opy_)
  else:
    if len(app) > 2:
      bstack11l1l1111_opy_(bstack1ll11l11l_opy_)
    elif len(app) == 2:
      if bstack11l11l1_opy_ (u"ࠬࡶࡡࡵࡪࠪ௱") in app and bstack11l11l1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ௲") in app:
        if os.path.exists(app[bstack11l11l1_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ௳")]):
          bstack11l111111_opy_ = bstack1l11lll111_opy_(config, app[bstack11l11l1_opy_ (u"ࠨࡲࡤࡸ࡭࠭௴")], app[bstack11l11l1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬ௵")])
        else:
          bstack11l1l1111_opy_(bstack1l11l111l1_opy_.format(app))
      else:
        bstack11l1l1111_opy_(bstack1ll11l11l_opy_)
    else:
      for key in app:
        if key in bstack11ll11l11l_opy_:
          if key == bstack11l11l1_opy_ (u"ࠪࡴࡦࡺࡨࠨ௶"):
            if os.path.exists(app[key]):
              bstack11l111111_opy_ = bstack1l11lll111_opy_(config, app[key])
            else:
              bstack11l1l1111_opy_(bstack1l11l111l1_opy_.format(app))
          else:
            bstack11l111111_opy_ = app[key]
        else:
          bstack11l1l1111_opy_(bstack1lll1ll1l1_opy_)
  return bstack11l111111_opy_
def bstack11llll11l_opy_(bstack11l111111_opy_):
  import re
  bstack1111111l1_opy_ = re.compile(bstack11l11l1_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬࠧࠦ௷"))
  bstack1lll11llll_opy_ = re.compile(bstack11l11l1_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭࠳ࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪࠥࠤ௸"))
  if bstack11l11l1_opy_ (u"࠭ࡢࡴ࠼࠲࠳ࠬ௹") in bstack11l111111_opy_ or re.fullmatch(bstack1111111l1_opy_, bstack11l111111_opy_) or re.fullmatch(bstack1lll11llll_opy_, bstack11l111111_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack1l11l11ll1_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack1l11lll111_opy_(config, path, bstack1l1111l11l_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11l11l1_opy_ (u"ࠧࡳࡤࠪ௺")).read()).hexdigest()
  bstack1ll11l111l_opy_ = bstack111l11ll1_opy_(md5_hash)
  bstack11l111111_opy_ = None
  if bstack1ll11l111l_opy_:
    logger.info(bstack1l1l1ll1l1_opy_.format(bstack1ll11l111l_opy_, md5_hash))
    return bstack1ll11l111l_opy_
  bstack1l11lll1ll_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack11l11l1_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭௻"): (os.path.basename(path), open(os.path.abspath(path), bstack11l11l1_opy_ (u"ࠩࡵࡦࠬ௼")), bstack11l11l1_opy_ (u"ࠪࡸࡪࡾࡴ࠰ࡲ࡯ࡥ࡮ࡴࠧ௽")),
      bstack11l11l1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧ௾"): bstack1l1111l11l_opy_
    }
  )
  response = requests.post(bstack1l1111l1l_opy_, data=multipart_data,
                           headers={bstack11l11l1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ௿"): multipart_data.content_type},
                           auth=(config[bstack11l11l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨఀ")], config[bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪఁ")]))
  try:
    res = json.loads(response.text)
    bstack11l111111_opy_ = res[bstack11l11l1_opy_ (u"ࠨࡣࡳࡴࡤࡻࡲ࡭ࠩం")]
    logger.info(bstack1ll1l111l1_opy_.format(bstack11l111111_opy_))
    bstack11111ll11_opy_(md5_hash, bstack11l111111_opy_)
    cli.bstack111lll1ll_opy_(bstack11l11l1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡶࡲ࡯ࡳࡦࡪ࡟ࡢࡲࡳࠦః"), datetime.datetime.now() - bstack1l11lll1ll_opy_)
  except ValueError as err:
    bstack11l1l1111_opy_(bstack1l1l1lll1l_opy_.format(str(err)))
  return bstack11l111111_opy_
def bstack1l111l1l1l_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack11l1l1l1l1_opy_
  bstack1lll1111l_opy_ = 1
  bstack111llll1ll_opy_ = 1
  if bstack11l11l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪఄ") in CONFIG:
    bstack111llll1ll_opy_ = CONFIG[bstack11l11l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫఅ")]
  else:
    bstack111llll1ll_opy_ = bstack111l1l1l1_opy_(framework_name, args) or 1
  if bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఆ") in CONFIG:
    bstack1lll1111l_opy_ = len(CONFIG[bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩఇ")])
  bstack11l1l1l1l1_opy_ = int(bstack111llll1ll_opy_) * int(bstack1lll1111l_opy_)
def bstack111l1l1l1_opy_(framework_name, args):
  if framework_name == bstack11ll1l11l1_opy_ and args and bstack11l11l1_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬఈ") in args:
      bstack11ll1llll_opy_ = args.index(bstack11l11l1_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ఉ"))
      return int(args[bstack11ll1llll_opy_ + 1]) or 1
  return 1
def bstack111l11ll1_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l11l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬఊ"))
    bstack1l1l1l1l11_opy_ = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠪࢂࠬఋ")), bstack11l11l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఌ"), bstack11l11l1_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭఍"))
    if os.path.exists(bstack1l1l1l1l11_opy_):
      try:
        bstack111l1lll11_opy_ = json.load(open(bstack1l1l1l1l11_opy_, bstack11l11l1_opy_ (u"࠭ࡲࡣࠩఎ")))
        if md5_hash in bstack111l1lll11_opy_:
          bstack1lllll1ll1_opy_ = bstack111l1lll11_opy_[md5_hash]
          bstack11l11lllll_opy_ = datetime.datetime.now()
          bstack1l11l1lll1_opy_ = datetime.datetime.strptime(bstack1lllll1ll1_opy_[bstack11l11l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪఏ")], bstack11l11l1_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬఐ"))
          if (bstack11l11lllll_opy_ - bstack1l11l1lll1_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack1lllll1ll1_opy_[bstack11l11l1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ఑")]):
            return None
          return bstack1lllll1ll1_opy_[bstack11l11l1_opy_ (u"ࠪ࡭ࡩ࠭ఒ")]
      except Exception as e:
        logger.debug(bstack11l11l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡶࡪࡧࡤࡪࡰࡪࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࠦࡦࡪ࡮ࡨ࠾ࠥࢁࡽࠨఓ").format(str(e)))
    return None
  bstack1l1l1l1l11_opy_ = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠬࢄࠧఔ")), bstack11l11l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭క"), bstack11l11l1_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨఖ"))
  lock_file = bstack1l1l1l1l11_opy_ + bstack11l11l1_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧగ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack1l1l1l1l11_opy_):
        with open(bstack1l1l1l1l11_opy_, bstack11l11l1_opy_ (u"ࠩࡵࠫఘ")) as f:
          content = f.read().strip()
          if content:
            bstack111l1lll11_opy_ = json.loads(content)
            if md5_hash in bstack111l1lll11_opy_:
              bstack1lllll1ll1_opy_ = bstack111l1lll11_opy_[md5_hash]
              bstack11l11lllll_opy_ = datetime.datetime.now()
              bstack1l11l1lll1_opy_ = datetime.datetime.strptime(bstack1lllll1ll1_opy_[bstack11l11l1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ఙ")], bstack11l11l1_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨచ"))
              if (bstack11l11lllll_opy_ - bstack1l11l1lll1_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack1lllll1ll1_opy_[bstack11l11l1_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪఛ")]):
                return None
              return bstack1lllll1ll1_opy_[bstack11l11l1_opy_ (u"࠭ࡩࡥࠩజ")]
      return None
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡷࡪࡶ࡫ࠤ࡫࡯࡬ࡦࠢ࡯ࡳࡨࡱࡩ࡯ࡩࠣࡪࡴࡸࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩ࠼ࠣࡿࢂ࠭ఝ").format(str(e)))
    return None
def bstack11111ll11_opy_(md5_hash, bstack11l111111_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l11l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫఞ"))
    bstack1l11l1111_opy_ = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠩࢁࠫట")), bstack11l11l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪఠ"))
    if not os.path.exists(bstack1l11l1111_opy_):
      os.makedirs(bstack1l11l1111_opy_)
    bstack1l1l1l1l11_opy_ = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠫࢃ࠭డ")), bstack11l11l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬఢ"), bstack11l11l1_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧణ"))
    bstack1l1ll1111_opy_ = {
      bstack11l11l1_opy_ (u"ࠧࡪࡦࠪత"): bstack11l111111_opy_,
      bstack11l11l1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫథ"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l11l1_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ద")),
      bstack11l11l1_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨధ"): str(__version__)
    }
    try:
      bstack111l1lll11_opy_ = {}
      if os.path.exists(bstack1l1l1l1l11_opy_):
        bstack111l1lll11_opy_ = json.load(open(bstack1l1l1l1l11_opy_, bstack11l11l1_opy_ (u"ࠫࡷࡨࠧన")))
      bstack111l1lll11_opy_[md5_hash] = bstack1l1ll1111_opy_
      with open(bstack1l1l1l1l11_opy_, bstack11l11l1_opy_ (u"ࠧࡽࠫࠣ఩")) as outfile:
        json.dump(bstack111l1lll11_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11l11l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰࡥࡣࡷ࡭ࡳ࡭ࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩࠢࡩ࡭ࡱ࡫࠺ࠡࡽࢀࠫప").format(str(e)))
    return
  bstack1l11l1111_opy_ = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠧࡿࠩఫ")), bstack11l11l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨబ"))
  if not os.path.exists(bstack1l11l1111_opy_):
    os.makedirs(bstack1l11l1111_opy_)
  bstack1l1l1l1l11_opy_ = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠩࢁࠫభ")), bstack11l11l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪమ"), bstack11l11l1_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬయ"))
  lock_file = bstack1l1l1l1l11_opy_ + bstack11l11l1_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫర")
  bstack1l1ll1111_opy_ = {
    bstack11l11l1_opy_ (u"࠭ࡩࡥࠩఱ"): bstack11l111111_opy_,
    bstack11l11l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪల"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l11l1_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬళ")),
    bstack11l11l1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧఴ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack111l1lll11_opy_ = {}
      if os.path.exists(bstack1l1l1l1l11_opy_):
        with open(bstack1l1l1l1l11_opy_, bstack11l11l1_opy_ (u"ࠪࡶࠬవ")) as f:
          content = f.read().strip()
          if content:
            bstack111l1lll11_opy_ = json.loads(content)
      bstack111l1lll11_opy_[md5_hash] = bstack1l1ll1111_opy_
      with open(bstack1l1l1l1l11_opy_, bstack11l11l1_opy_ (u"ࠦࡼࠨశ")) as outfile:
        json.dump(bstack111l1lll11_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡼ࡯ࡴࡩࠢࡩ࡭ࡱ࡫ࠠ࡭ࡱࡦ࡯࡮ࡴࡧࠡࡨࡲࡶࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮ࠠࡶࡲࡧࡥࡹ࡫࠺ࠡࡽࢀࠫష").format(str(e)))
def bstack1111l11ll_opy_(self):
  return
def bstack1lllllll1l_opy_(self):
  return
def bstack1l1l1l1ll1_opy_():
  global bstack1ll1lll11_opy_
  bstack1ll1lll11_opy_ = True
@measure(event_name=EVENTS.bstack1ll11111l_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack1l1ll1l1l1_opy_(self):
  global bstack11111ll1l_opy_
  global bstack1l1l1l1lll_opy_
  global bstack1l1ll11ll_opy_
  try:
    if bstack11l11l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭స") in bstack11111ll1l_opy_ and self.session_id != None and bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫహ"), bstack11l11l1_opy_ (u"ࠨࠩ఺")) != bstack11l11l1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ఻"):
      bstack1l11l1ll11_opy_ = bstack11l11l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦ఼ࠪ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l11l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫఽ")
      if bstack1l11l1ll11_opy_ == bstack11l11l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬా"):
        bstack111ll1111_opy_(logger)
      if self != None:
        bstack11l11ll11l_opy_(self, bstack1l11l1ll11_opy_, bstack11l11l1_opy_ (u"࠭ࠬࠡࠩి").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11l11l1_opy_ (u"ࠧࠨీ")
    if bstack11l11l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨు") in bstack11111ll1l_opy_ and getattr(threading.current_thread(), bstack11l11l1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨూ"), None):
      bstack1lll1ll1l_opy_.bstack111l1l1l_opy_(self, bstack111ll1l1l1_opy_, logger, wait=True)
    if bstack11l11l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪృ") in bstack11111ll1l_opy_:
      if not threading.currentThread().behave_test_status:
        bstack11l11ll11l_opy_(self, bstack11l11l1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦౄ"))
      bstack1ll111l1l1_opy_.bstack1l111111ll_opy_(self)
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨ౅") + str(e))
  bstack1l1ll11ll_opy_(self)
  self.session_id = None
def bstack1l1l111ll1_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1llll111l1_opy_
    global bstack11111ll1l_opy_
    command_executor = kwargs.get(bstack11l11l1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠩె"), bstack11l11l1_opy_ (u"ࠧࠨే"))
    bstack11l1111l1l_opy_ = False
    if type(command_executor) == str and bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫై") in command_executor:
      bstack11l1111l1l_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ౉") in str(getattr(command_executor, bstack11l11l1_opy_ (u"ࠪࡣࡺࡸ࡬ࠨొ"), bstack11l11l1_opy_ (u"ࠫࠬో"))):
      bstack11l1111l1l_opy_ = True
    else:
      kwargs = bstack111llll1_opy_.bstack11lll1l11_opy_(bstack1ll1l1lll_opy_=kwargs, config=CONFIG)
      return bstack11ll1ll11_opy_(self, *args, **kwargs)
    if bstack11l1111l1l_opy_:
      bstack111ll11ll1_opy_ = bstack1l1l1ll111_opy_.bstack1111l1ll1l_opy_(CONFIG, bstack11111ll1l_opy_)
      if kwargs.get(bstack11l11l1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ౌ")):
        kwargs[bstack11l11l1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹ్ࠧ")] = bstack1llll111l1_opy_(kwargs[bstack11l11l1_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ౎")], bstack11111ll1l_opy_, CONFIG, bstack111ll11ll1_opy_)
      elif kwargs.get(bstack11l11l1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ౏")):
        kwargs[bstack11l11l1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ౐")] = bstack1llll111l1_opy_(kwargs[bstack11l11l1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ౑")], bstack11111ll1l_opy_, CONFIG, bstack111ll11ll1_opy_)
  except Exception as e:
    logger.error(bstack11l11l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦ౒").format(str(e)))
  return bstack11ll1ll11_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack11l111llll_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack1ll11l1l1_opy_(self, command_executor=bstack11l11l1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴࠷࠲࠸࠰࠳࠲࠵࠴࠱࠻࠶࠷࠸࠹ࠨ౓"), *args, **kwargs):
  global bstack1l1l1l1lll_opy_
  global bstack1lll1111l1_opy_
  bstack1l1l1l111l_opy_ = bstack1l1l111ll1_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1ll1l1l1_opy_.on():
    return bstack1l1l1l111l_opy_
  try:
    logger.debug(bstack11l11l1_opy_ (u"࠭ࡃࡰ࡯ࡰࡥࡳࡪࠠࡆࡺࡨࡧࡺࡺ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡦࡢ࡮ࡶࡩࠥ࠳ࠠࡼࡿࠪ౔").format(str(command_executor)))
    logger.debug(bstack11l11l1_opy_ (u"ࠧࡉࡷࡥࠤ࡚ࡘࡌࠡ࡫ࡶࠤ࠲ࠦࡻࡾౕࠩ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰౖࠫ") in command_executor._url:
      bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ౗"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ౘ") in command_executor):
    bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬౙ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack111ll1l111_opy_ = getattr(threading.current_thread(), bstack11l11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭ౚ"), None)
  bstack1l11l1l1l_opy_ = {}
  if self.capabilities is not None:
    bstack1l11l1l1l_opy_[bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬ౛")] = self.capabilities.get(bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ౜"))
    bstack1l11l1l1l_opy_[bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪౝ")] = self.capabilities.get(bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ౞"))
    bstack1l11l1l1l_opy_[bstack11l11l1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡢࡳࡵࡺࡩࡰࡰࡶࠫ౟")] = self.capabilities.get(bstack11l11l1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩౠ"))
  if CONFIG.get(bstack11l11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬౡ"), False) and bstack111llll1_opy_.bstack1l1llllll_opy_(bstack1l11l1l1l_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack11l11l1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ౢ") in bstack11111ll1l_opy_ or bstack11l11l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ౣ") in bstack11111ll1l_opy_:
    bstack1l11l111_opy_.bstack111l1ll111_opy_(self)
  if bstack11l11l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ౤") in bstack11111ll1l_opy_ and bstack111ll1l111_opy_ and bstack111ll1l111_opy_.get(bstack11l11l1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ౥"), bstack11l11l1_opy_ (u"ࠪࠫ౦")) == bstack11l11l1_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ౧"):
    bstack1l11l111_opy_.bstack111l1ll111_opy_(self)
  bstack1l1l1l1lll_opy_ = self.session_id
  with bstack1111l1lll1_opy_:
    bstack1lll1111l1_opy_.append(self)
  return bstack1l1l1l111l_opy_
def bstack111l1111ll_opy_(args):
  return bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷ࠭౨") in str(args)
def bstack1111ll1l1_opy_(self, driver_command, *args, **kwargs):
  global bstack1l1l1l1ll_opy_
  global bstack1111llllll_opy_
  bstack111111ll1l_opy_ = bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ౩"), None) and bstack1ll11l1l_opy_(
          threading.current_thread(), bstack11l11l1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭౪"), None)
  bstack11111l1l11_opy_ = bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ౫"), None) and bstack1ll11l1l_opy_(
          threading.current_thread(), bstack11l11l1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ౬"), None)
  bstack1l1l11ll1_opy_ = getattr(self, bstack11l11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ౭"), None) != None and getattr(self, bstack11l11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ౮"), None) == True
  if not bstack1111llllll_opy_ and bstack11l11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ౯") in CONFIG and CONFIG[bstack11l11l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭౰")] == True and bstack1lllll111l_opy_.bstack11l1llll1_opy_(driver_command) and (bstack1l1l11ll1_opy_ or bstack111111ll1l_opy_ or bstack11111l1l11_opy_) and not bstack111l1111ll_opy_(args):
    try:
      bstack1111llllll_opy_ = True
      logger.debug(bstack11l11l1_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡻࡾࠩ౱").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11l11l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵ࡫ࡲࡧࡱࡵࡱࠥࡹࡣࡢࡰࠣࡿࢂ࠭౲").format(str(err)))
    bstack1111llllll_opy_ = False
  response = bstack1l1l1l1ll_opy_(self, driver_command, *args, **kwargs)
  if (bstack11l11l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ౳") in str(bstack11111ll1l_opy_).lower() or bstack11l11l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ౴") in str(bstack11111ll1l_opy_).lower()) and bstack1ll1l1l1_opy_.on():
    try:
      if driver_command == bstack11l11l1_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨ౵"):
        bstack1l11l111_opy_.bstack1lll1ll111_opy_({
            bstack11l11l1_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫ౶"): response[bstack11l11l1_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬ౷")],
            bstack11l11l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ౸"): bstack1l11l111_opy_.current_test_uuid() if bstack1l11l111_opy_.current_test_uuid() else bstack1ll1l1l1_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1l111ll11l_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack1l1ll1llll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1l1l1l1lll_opy_
  global bstack11l1l111l1_opy_
  global bstack111ll11111_opy_
  global bstack1l1ll1lll1_opy_
  global bstack1llll1l1l1_opy_
  global bstack11111ll1l_opy_
  global bstack11ll1ll11_opy_
  global bstack1lll1111l1_opy_
  global bstack1l11111l1l_opy_
  global bstack111ll1l1l1_opy_
  if os.getenv(bstack11l11l1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭౹")) is not None and bstack111llll1_opy_.bstack111l1l1l11_opy_(CONFIG) is None:
    CONFIG[bstack11l11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ౺")] = True
  CONFIG[bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ౻")] = str(bstack11111ll1l_opy_) + str(__version__)
  bstack111l111111_opy_ = os.environ[bstack11l11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ౼")]
  bstack111ll11ll1_opy_ = bstack1l1l1ll111_opy_.bstack1111l1ll1l_opy_(CONFIG, bstack11111ll1l_opy_)
  CONFIG[bstack11l11l1_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ౽")] = bstack111l111111_opy_
  CONFIG[bstack11l11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨ౾")] = bstack111ll11ll1_opy_
  if CONFIG.get(bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ౿"),bstack11l11l1_opy_ (u"ࠨࠩಀ")) and bstack11l11l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨಁ") in bstack11111ll1l_opy_:
    CONFIG[bstack11l11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪಂ")].pop(bstack11l11l1_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩಃ"), None)
    CONFIG[bstack11l11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ಄")].pop(bstack11l11l1_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫಅ"), None)
  command_executor = bstack11ll1ll1ll_opy_()
  logger.debug(bstack11l1111lll_opy_.format(command_executor))
  proxy = bstack11ll1l1ll_opy_(CONFIG, proxy)
  bstack111111ll11_opy_ = 0 if bstack11l1l111l1_opy_ < 0 else bstack11l1l111l1_opy_
  try:
    if bstack1l1ll1lll1_opy_ is True:
      bstack111111ll11_opy_ = int(multiprocessing.current_process().name)
    elif bstack1llll1l1l1_opy_ is True:
      bstack111111ll11_opy_ = int(threading.current_thread().name)
  except:
    bstack111111ll11_opy_ = 0
  bstack1lllll1l1l_opy_ = bstack111ll11l11_opy_(CONFIG, bstack111111ll11_opy_)
  logger.debug(bstack1111l1lll_opy_.format(str(bstack1lllll1l1l_opy_)))
  if bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫಆ") in CONFIG and bstack111lll11l1_opy_(CONFIG[bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬಇ")]):
    bstack1lllll11ll_opy_(bstack1lllll1l1l_opy_)
  if bstack111llll1_opy_.bstack1l1l1llll_opy_(CONFIG, bstack111111ll11_opy_) and bstack111llll1_opy_.bstack111l11111_opy_(bstack1lllll1l1l_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack111llll1_opy_.set_capabilities(bstack1lllll1l1l_opy_, CONFIG)
  if desired_capabilities:
    bstack11l11l1l11_opy_ = bstack11l1lllll_opy_(desired_capabilities)
    bstack11l11l1l11_opy_[bstack11l11l1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩಈ")] = bstack1l1l1111ll_opy_(CONFIG)
    bstack1llll1l1ll_opy_ = bstack111ll11l11_opy_(bstack11l11l1l11_opy_)
    if bstack1llll1l1ll_opy_:
      bstack1lllll1l1l_opy_ = update(bstack1llll1l1ll_opy_, bstack1lllll1l1l_opy_)
    desired_capabilities = None
  if options:
    bstack11l1lll11l_opy_(options, bstack1lllll1l1l_opy_)
  if not options:
    options = bstack111llll1l_opy_(bstack1lllll1l1l_opy_)
  bstack111ll1l1l1_opy_ = CONFIG.get(bstack11l11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಉ"))[bstack111111ll11_opy_]
  if proxy and bstack11l1ll1l11_opy_() >= version.parse(bstack11l11l1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫಊ")):
    options.proxy(proxy)
  if options and bstack11l1ll1l11_opy_() >= version.parse(bstack11l11l1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫಋ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack11l1ll1l11_opy_() < version.parse(bstack11l11l1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬಌ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1lllll1l1l_opy_)
  logger.info(bstack1lll1111ll_opy_)
  bstack11ll111ll1_opy_.end(EVENTS.bstack1l11l1ll1_opy_.value, EVENTS.bstack1l11l1ll1_opy_.value + bstack11l11l1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ಍"), EVENTS.bstack1l11l1ll1_opy_.value + bstack11l11l1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨಎ"), status=True, failure=None, test_name=bstack111ll11111_opy_)
  if bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡴࡷࡵࡦࡪ࡮ࡨࠫಏ") in kwargs:
    del kwargs[bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡵࡸ࡯ࡧ࡫࡯ࡩࠬಐ")]
  try:
    if bstack11l1ll1l11_opy_() >= version.parse(bstack11l11l1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫ಑")):
      bstack11ll1ll11_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack11l1ll1l11_opy_() >= version.parse(bstack11l11l1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫಒ")):
      bstack11ll1ll11_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11l1ll1l11_opy_() >= version.parse(bstack11l11l1_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭ಓ")):
      bstack11ll1ll11_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack11ll1ll11_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack111lll1l11_opy_:
    logger.error(bstack1l1l111lll_opy_.format(bstack11l11l1_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰ࠭ಔ"), str(bstack111lll1l11_opy_)))
    raise bstack111lll1l11_opy_
  if bstack111llll1_opy_.bstack1l1l1llll_opy_(CONFIG, bstack111111ll11_opy_) and bstack111llll1_opy_.bstack111l11111_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪಕ")][bstack11l11l1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨಖ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack111llll1_opy_.set_capabilities(bstack1lllll1l1l_opy_, CONFIG)
  try:
    bstack1lllll1111_opy_ = bstack11l11l1_opy_ (u"ࠪࠫಗ")
    if bstack11l1ll1l11_opy_() >= version.parse(bstack11l11l1_opy_ (u"ࠫ࠹࠴࠰࠯࠲ࡥ࠵ࠬಘ")):
      if self.caps is not None:
        bstack1lllll1111_opy_ = self.caps.get(bstack11l11l1_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧಙ"))
    else:
      if self.capabilities is not None:
        bstack1lllll1111_opy_ = self.capabilities.get(bstack11l11l1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨಚ"))
    if bstack1lllll1111_opy_:
      bstack1l1l1lllll_opy_(bstack1lllll1111_opy_)
      if bstack11l1ll1l11_opy_() <= version.parse(bstack11l11l1_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧಛ")):
        self.command_executor._url = bstack11l11l1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤಜ") + bstack1ll1ll111_opy_ + bstack11l11l1_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨಝ")
      else:
        self.command_executor._url = bstack11l11l1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧಞ") + bstack1lllll1111_opy_ + bstack11l11l1_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧಟ")
      logger.debug(bstack1llll11l1l_opy_.format(bstack1lllll1111_opy_))
    else:
      logger.debug(bstack111ll1l11_opy_.format(bstack11l11l1_opy_ (u"ࠧࡕࡰࡵ࡫ࡰࡥࡱࠦࡈࡶࡤࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠨಠ")))
  except Exception as e:
    logger.debug(bstack111ll1l11_opy_.format(e))
  if bstack11l11l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಡ") in bstack11111ll1l_opy_:
    bstack111111l11_opy_(bstack11l1l111l1_opy_, bstack1l11111l1l_opy_)
  bstack1l1l1l1lll_opy_ = self.session_id
  if bstack11l11l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧಢ") in bstack11111ll1l_opy_ or bstack11l11l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨಣ") in bstack11111ll1l_opy_ or bstack11l11l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨತ") in bstack11111ll1l_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack111ll1l111_opy_ = getattr(threading.current_thread(), bstack11l11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫಥ"), None)
  if bstack11l11l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫದ") in bstack11111ll1l_opy_ or bstack11l11l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫಧ") in bstack11111ll1l_opy_:
    bstack1l11l111_opy_.bstack111l1ll111_opy_(self)
  if bstack11l11l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ನ") in bstack11111ll1l_opy_ and bstack111ll1l111_opy_ and bstack111ll1l111_opy_.get(bstack11l11l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ಩"), bstack11l11l1_opy_ (u"ࠨࠩಪ")) == bstack11l11l1_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪಫ"):
    bstack1l11l111_opy_.bstack111l1ll111_opy_(self)
  with bstack1111l1lll1_opy_:
    bstack1lll1111l1_opy_.append(self)
  if bstack11l11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಬ") in CONFIG and bstack11l11l1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩಭ") in CONFIG[bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಮ")][bstack111111ll11_opy_]:
    bstack111ll11111_opy_ = CONFIG[bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಯ")][bstack111111ll11_opy_][bstack11l11l1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬರ")]
  logger.debug(bstack1lll111ll1_opy_.format(bstack1l1l1l1lll_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1l11llll1l_opy_
    def bstack111l11llll_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack111l1l1ll_opy_
      if(bstack11l11l1_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࠮࡫ࡵࠥಱ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠩࢁࠫಲ")), bstack11l11l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪಳ"), bstack11l11l1_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭಴")), bstack11l11l1_opy_ (u"ࠬࡽࠧವ")) as fp:
          fp.write(bstack11l11l1_opy_ (u"ࠨࠢಶ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11l11l1_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤಷ")))):
          with open(args[1], bstack11l11l1_opy_ (u"ࠨࡴࠪಸ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11l11l1_opy_ (u"ࠩࡤࡷࡾࡴࡣࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡣࡳ࡫ࡷࡑࡣࡪࡩ࠭ࡩ࡯࡯ࡶࡨࡼࡹ࠲ࠠࡱࡣࡪࡩࠥࡃࠠࡷࡱ࡬ࡨࠥ࠶ࠩࠨಹ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack11ll11111l_opy_)
            if bstack11l11l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ಺") in CONFIG and str(CONFIG[bstack11l11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ಻")]).lower() != bstack11l11l1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨ಼ࠫ"):
                bstack11l11ll11_opy_ = bstack1l11llll1l_opy_()
                bstack11llll111l_opy_ = bstack11l11l1_opy_ (u"࠭ࠧࠨࠌ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠏࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࠻ࠋࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࠾ࠎࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࠽ࠍࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࠽ࠍࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࠎ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡱࡧࡵ࡯ࡥ࡫ࠤࡂࠦࡡࡴࡻࡱࡧࠥ࠮࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸ࠯ࠠ࠾ࡀࠣࡿࢀࠐࠠࠡ࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࠎࠥࠦࡴࡳࡻࠣࡿࢀࠐࠠࠡࠢࠣࡧࡦࡶࡳࠡ࠿ࠣࡎࡘࡕࡎ࠯ࡲࡤࡶࡸ࡫ࠨࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷ࠮ࡁࠊࠡࠢࢀࢁࠥࡩࡡࡵࡥ࡫ࠤ࠭࡫ࡸࠪࠢࡾࡿࠏࠦࠠࠡࠢࡦࡳࡳࡹ࡯࡭ࡧ࠱ࡩࡷࡸ࡯ࡳࠪࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠾ࠧ࠲ࠠࡦࡺࠬ࠿ࠏࠦࠠࡾࡿࠍࠤࠥࡸࡥࡵࡷࡵࡲࠥࡧࡷࡢ࡫ࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡨࡵ࡮࡯ࡧࡦࡸ࠭ࢁࡻࠋࠢࠣࠤࠥࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵ࠼ࠣࠫࢀࡩࡤࡱࡗࡵࡰࢂ࠭ࠠࠬࠢࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩ࠭ࠌࠣࠤࠥࠦ࠮࠯࠰࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴࠌࠣࠤࢂࢃࠩ࠼ࠌࢀࢁࡀࠐ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠌࠪࠫࠬಽ").format(bstack11l11ll11_opy_=bstack11l11ll11_opy_)
            lines.insert(1, bstack11llll111l_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11l11l1_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤಾ")), bstack11l11l1_opy_ (u"ࠨࡹࠪಿ")) as bstack111lllll1l_opy_:
              bstack111lllll1l_opy_.writelines(lines)
        CONFIG[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫೀ")] = str(bstack11111ll1l_opy_) + str(__version__)
        bstack111l111111_opy_ = os.environ[bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨು")]
        bstack111ll11ll1_opy_ = bstack1l1l1ll111_opy_.bstack1111l1ll1l_opy_(CONFIG, bstack11111ll1l_opy_)
        CONFIG[bstack11l11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧೂ")] = bstack111l111111_opy_
        CONFIG[bstack11l11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧೃ")] = bstack111ll11ll1_opy_
        bstack111111ll11_opy_ = 0 if bstack11l1l111l1_opy_ < 0 else bstack11l1l111l1_opy_
        try:
          if bstack1l1ll1lll1_opy_ is True:
            bstack111111ll11_opy_ = int(multiprocessing.current_process().name)
          elif bstack1llll1l1l1_opy_ is True:
            bstack111111ll11_opy_ = int(threading.current_thread().name)
        except:
          bstack111111ll11_opy_ = 0
        CONFIG[bstack11l11l1_opy_ (u"ࠨࡵࡴࡧ࡚࠷ࡈࠨೄ")] = False
        CONFIG[bstack11l11l1_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨ೅")] = True
        bstack1lllll1l1l_opy_ = bstack111ll11l11_opy_(CONFIG, bstack111111ll11_opy_)
        logger.debug(bstack1111l1lll_opy_.format(str(bstack1lllll1l1l_opy_)))
        if CONFIG.get(bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬೆ")):
          bstack1lllll11ll_opy_(bstack1lllll1l1l_opy_)
        if bstack11l11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೇ") in CONFIG and bstack11l11l1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨೈ") in CONFIG[bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ೉")][bstack111111ll11_opy_]:
          bstack111ll11111_opy_ = CONFIG[bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨೊ")][bstack111111ll11_opy_][bstack11l11l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫೋ")]
        args.append(os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠧࡿࠩೌ")), bstack11l11l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ್"), bstack11l11l1_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ೎")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1lllll1l1l_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11l11l1_opy_ (u"ࠥ࡭ࡳࡪࡥࡹࡡࡥࡷࡹࡧࡣ࡬࠰࡭ࡷࠧ೏"))
      bstack111l1l1ll_opy_ = True
      return bstack11l1lll1l1_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack11ll1l1l1l_opy_(self,
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
    global bstack11l1l111l1_opy_
    global bstack111ll11111_opy_
    global bstack1l1ll1lll1_opy_
    global bstack1llll1l1l1_opy_
    global bstack11111ll1l_opy_
    CONFIG[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭೐")] = str(bstack11111ll1l_opy_) + str(__version__)
    bstack111l111111_opy_ = os.environ[bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ೑")]
    bstack111ll11ll1_opy_ = bstack1l1l1ll111_opy_.bstack1111l1ll1l_opy_(CONFIG, bstack11111ll1l_opy_)
    CONFIG[bstack11l11l1_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩ೒")] = bstack111l111111_opy_
    CONFIG[bstack11l11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ೓")] = bstack111ll11ll1_opy_
    bstack111111ll11_opy_ = 0 if bstack11l1l111l1_opy_ < 0 else bstack11l1l111l1_opy_
    try:
      if bstack1l1ll1lll1_opy_ is True:
        bstack111111ll11_opy_ = int(multiprocessing.current_process().name)
      elif bstack1llll1l1l1_opy_ is True:
        bstack111111ll11_opy_ = int(threading.current_thread().name)
    except:
      bstack111111ll11_opy_ = 0
    CONFIG[bstack11l11l1_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ೔")] = True
    bstack1lllll1l1l_opy_ = bstack111ll11l11_opy_(CONFIG, bstack111111ll11_opy_)
    logger.debug(bstack1111l1lll_opy_.format(str(bstack1lllll1l1l_opy_)))
    if CONFIG.get(bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ೕ")):
      bstack1lllll11ll_opy_(bstack1lllll1l1l_opy_)
    if bstack11l11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ೖ") in CONFIG and bstack11l11l1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ೗") in CONFIG[bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ೘")][bstack111111ll11_opy_]:
      bstack111ll11111_opy_ = CONFIG[bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ೙")][bstack111111ll11_opy_][bstack11l11l1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ೚")]
    import urllib
    import json
    if bstack11l11l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ೛") in CONFIG and str(CONFIG[bstack11l11l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭೜")]).lower() != bstack11l11l1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩೝ"):
        bstack11l1ll1l1_opy_ = bstack1l11llll1l_opy_()
        bstack11l11ll11_opy_ = bstack11l1ll1l1_opy_ + urllib.parse.quote(json.dumps(bstack1lllll1l1l_opy_))
    else:
        bstack11l11ll11_opy_ = bstack11l11l1_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭ೞ") + urllib.parse.quote(json.dumps(bstack1lllll1l1l_opy_))
    browser = self.connect(bstack11l11ll11_opy_)
    return browser
except Exception as e:
    pass
def bstack1l11l11lll_opy_():
    global bstack111l1l1ll_opy_
    global bstack11111ll1l_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1lll1l1lll_opy_
        global bstack11111111_opy_
        if not bstack1ll11l11ll_opy_:
          global bstack11ll1l111_opy_
          if not bstack11ll1l111_opy_:
            from bstack_utils.helper import bstack1l1111ll11_opy_, bstack1ll1l1ll11_opy_, bstack1l11111l11_opy_
            bstack11ll1l111_opy_ = bstack1l1111ll11_opy_()
            bstack1ll1l1ll11_opy_(bstack11111ll1l_opy_)
            bstack111ll11ll1_opy_ = bstack1l1l1ll111_opy_.bstack1111l1ll1l_opy_(CONFIG, bstack11111ll1l_opy_)
            bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"ࠧࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡓࡖࡔࡊࡕࡄࡖࡢࡑࡆࡖࠢ೟"), bstack111ll11ll1_opy_)
          BrowserType.connect = bstack1lll1l1lll_opy_
          return
        BrowserType.launch = bstack11ll1l1l1l_opy_
        bstack111l1l1ll_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack111l11llll_opy_
      bstack111l1l1ll_opy_ = True
    except Exception as e:
      pass
def bstack11lll1111_opy_(context, bstack11l1lll11_opy_):
  try:
    context.page.evaluate(bstack11l11l1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢೠ"), bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫೡ")+ json.dumps(bstack11l1lll11_opy_) + bstack11l11l1_opy_ (u"ࠣࡿࢀࠦೢ"))
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃ࠺ࠡࡽࢀࠦೣ").format(str(e), traceback.format_exc()))
def bstack11l1l1lll_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11l11l1_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ೤"), bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ೥") + json.dumps(message) + bstack11l11l1_opy_ (u"ࠬ࠲ࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠨ೦") + json.dumps(level) + bstack11l11l1_opy_ (u"࠭ࡽࡾࠩ೧"))
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠠࡼࡿ࠽ࠤࢀࢃࠢ೨").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1l11l111ll_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack111l1l1l1l_opy_(self, url):
  global bstack1llll1111l_opy_
  try:
    bstack1l1l11llll_opy_(url)
  except Exception as err:
    logger.debug(bstack1l1l1l11l_opy_.format(str(err)))
  try:
    bstack1llll1111l_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1111l1l11l_opy_):
        bstack1l1l11llll_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1l1l1l11l_opy_.format(str(err)))
    raise e
def bstack11llll111_opy_(self):
  global bstack111l1l1111_opy_
  bstack111l1l1111_opy_ = self
  return
def bstack1111111ll_opy_(self):
  global bstack1l1l1l1l1l_opy_
  bstack1l1l1l1l1l_opy_ = self
  return
def bstack1l1ll11l1_opy_(test_name, bstack11lll1ll11_opy_):
  global CONFIG
  if percy.bstack1l11ll1111_opy_() == bstack11l11l1_opy_ (u"ࠣࡶࡵࡹࡪࠨ೩"):
    bstack1ll11l1ll1_opy_ = os.path.relpath(bstack11lll1ll11_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1ll11l1ll1_opy_)
    bstack111ll1l1ll_opy_ = suite_name + bstack11l11l1_opy_ (u"ࠤ࠰ࠦ೪") + test_name
    threading.current_thread().percySessionName = bstack111ll1l1ll_opy_
def bstack11111llll1_opy_(self, test, *args, **kwargs):
  global bstack11111l111l_opy_
  test_name = None
  bstack11lll1ll11_opy_ = None
  if test:
    test_name = str(test.name)
    bstack11lll1ll11_opy_ = str(test.source)
  bstack1l1ll11l1_opy_(test_name, bstack11lll1ll11_opy_)
  bstack11111l111l_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1ll1l1ll1l_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack111lllllll_opy_(driver, bstack111ll1l1ll_opy_):
  if not bstack1l11llllll_opy_ and bstack111ll1l1ll_opy_:
      bstack111ll11l1_opy_ = {
          bstack11l11l1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪ೫"): bstack11l11l1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ೬"),
          bstack11l11l1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ೭"): {
              bstack11l11l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ೮"): bstack111ll1l1ll_opy_
          }
      }
      bstack11lll1l1l1_opy_ = bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ೯").format(json.dumps(bstack111ll11l1_opy_))
      driver.execute_script(bstack11lll1l1l1_opy_)
  if bstack1l1ll1ll1_opy_:
      bstack111ll111l1_opy_ = {
          bstack11l11l1_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨ೰"): bstack11l11l1_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫೱ"),
          bstack11l11l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ೲ"): {
              bstack11l11l1_opy_ (u"ࠫࡩࡧࡴࡢࠩೳ"): bstack111ll1l1ll_opy_ + bstack11l11l1_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩࠧࠧ೴"),
              bstack11l11l1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ೵"): bstack11l11l1_opy_ (u"ࠧࡪࡰࡩࡳࠬ೶")
          }
      }
      if bstack1l1ll1ll1_opy_.status == bstack11l11l1_opy_ (u"ࠨࡒࡄࡗࡘ࠭೷"):
          bstack1l1l111l1_opy_ = bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧ೸").format(json.dumps(bstack111ll111l1_opy_))
          driver.execute_script(bstack1l1l111l1_opy_)
          bstack11l11ll11l_opy_(driver, bstack11l11l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ೹"))
      elif bstack1l1ll1ll1_opy_.status == bstack11l11l1_opy_ (u"ࠫࡋࡇࡉࡍࠩ೺"):
          reason = bstack11l11l1_opy_ (u"ࠧࠨ೻")
          bstack1l11lll1l_opy_ = bstack111ll1l1ll_opy_ + bstack11l11l1_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠧ೼")
          if bstack1l1ll1ll1_opy_.message:
              reason = str(bstack1l1ll1ll1_opy_.message)
              bstack1l11lll1l_opy_ = bstack1l11lll1l_opy_ + bstack11l11l1_opy_ (u"ࠧࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶ࠿ࠦࠧ೽") + reason
          bstack111ll111l1_opy_[bstack11l11l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ೾")] = {
              bstack11l11l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ೿"): bstack11l11l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩഀ"),
              bstack11l11l1_opy_ (u"ࠫࡩࡧࡴࡢࠩഁ"): bstack1l11lll1l_opy_
          }
          bstack1l1l111l1_opy_ = bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪം").format(json.dumps(bstack111ll111l1_opy_))
          driver.execute_script(bstack1l1l111l1_opy_)
          bstack11l11ll11l_opy_(driver, bstack11l11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ഃ"), reason)
          bstack11l1l1l11_opy_(reason, str(bstack1l1ll1ll1_opy_), str(bstack11l1l111l1_opy_), logger)
@measure(event_name=EVENTS.bstack111l111l1l_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack1lll1ll1ll_opy_(driver, test):
  if percy.bstack1l11ll1111_opy_() == bstack11l11l1_opy_ (u"ࠢࡵࡴࡸࡩࠧഄ") and percy.bstack1l1ll11111_opy_() == bstack11l11l1_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥഅ"):
      bstack1l1ll1l111_opy_ = bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬആ"), None)
      bstack11ll1lll1_opy_(driver, bstack1l1ll1l111_opy_, test)
  if (bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧഇ"), None) and
      bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪഈ"), None)) or (
      bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬഉ"), None) and
      bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨഊ"), None)):
      logger.info(bstack11l11l1_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠦࠢഋ"))
      bstack111llll1_opy_.bstack111ll11l_opy_(driver, name=test.name, path=test.source)
def bstack1llllll1l1_opy_(test, bstack111ll1l1ll_opy_):
    try:
      bstack1l11lll1ll_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack11l11l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ഌ")] = bstack111ll1l1ll_opy_
      if bstack1l1ll1ll1_opy_:
        if bstack1l1ll1ll1_opy_.status == bstack11l11l1_opy_ (u"ࠩࡓࡅࡘ࡙ࠧ഍"):
          data[bstack11l11l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪഎ")] = bstack11l11l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫഏ")
        elif bstack1l1ll1ll1_opy_.status == bstack11l11l1_opy_ (u"ࠬࡌࡁࡊࡎࠪഐ"):
          data[bstack11l11l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭഑")] = bstack11l11l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧഒ")
          if bstack1l1ll1ll1_opy_.message:
            data[bstack11l11l1_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨഓ")] = str(bstack1l1ll1ll1_opy_.message)
      user = CONFIG[bstack11l11l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫഔ")]
      key = CONFIG[bstack11l11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ക")]
      host = bstack11l1lll1l_opy_(cli.config, [bstack11l11l1_opy_ (u"ࠦࡦࡶࡩࡴࠤഖ"), bstack11l11l1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢഗ"), bstack11l11l1_opy_ (u"ࠨࡡࡱ࡫ࠥഘ")], bstack11l11l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠣങ"))
      url = bstack11l11l1_opy_ (u"ࠨࡽࢀ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠰ࡽࢀ࠲࡯ࡹ࡯࡯ࠩച").format(host, bstack1l1l1l1lll_opy_)
      headers = {
        bstack11l11l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨഛ"): bstack11l11l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ജ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack111lll1ll_opy_(bstack11l11l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡸࡴࡩࡧࡴࡦࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡷࡥࡹࡻࡳࠣഝ"), datetime.datetime.now() - bstack1l11lll1ll_opy_)
    except Exception as e:
      logger.error(bstack1l1l1l1l1_opy_.format(str(e)))
def bstack1l1ll11ll1_opy_(test, bstack111ll1l1ll_opy_):
  global CONFIG
  global bstack1l1l1l1l1l_opy_
  global bstack111l1l1111_opy_
  global bstack1l1l1l1lll_opy_
  global bstack1l1ll1ll1_opy_
  global bstack111ll11111_opy_
  global bstack1l1111l1ll_opy_
  global bstack1l11llll1_opy_
  global bstack1ll1l1ll1_opy_
  global bstack1ll1l1lll1_opy_
  global bstack1lll1111l1_opy_
  global bstack111ll1l1l1_opy_
  global bstack11ll111lll_opy_
  try:
    if not bstack1l1l1l1lll_opy_:
      with bstack11ll111lll_opy_:
        bstack11l1ll111l_opy_ = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠬࢄࠧഞ")), bstack11l11l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ട"), bstack11l11l1_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩഠ"))
        if os.path.exists(bstack11l1ll111l_opy_):
          with open(bstack11l1ll111l_opy_, bstack11l11l1_opy_ (u"ࠨࡴࠪഡ")) as f:
            content = f.read().strip()
            if content:
              bstack1lllllll11_opy_ = json.loads(bstack11l11l1_opy_ (u"ࠤࡾࠦഢ") + content + bstack11l11l1_opy_ (u"ࠪࠦࡽࠨ࠺ࠡࠤࡼࠦࠬണ") + bstack11l11l1_opy_ (u"ࠦࢂࠨത"))
              bstack1l1l1l1lll_opy_ = bstack1lllllll11_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࡵࠣࡪ࡮ࡲࡥ࠻ࠢࠪഥ") + str(e))
  if bstack1lll1111l1_opy_:
    with bstack1111l1lll1_opy_:
      bstack111lllll11_opy_ = bstack1lll1111l1_opy_.copy()
    for driver in bstack111lllll11_opy_:
      if bstack1l1l1l1lll_opy_ == driver.session_id:
        if test:
          bstack1lll1ll1ll_opy_(driver, test)
        bstack111lllllll_opy_(driver, bstack111ll1l1ll_opy_)
  elif bstack1l1l1l1lll_opy_:
    bstack1llllll1l1_opy_(test, bstack111ll1l1ll_opy_)
  if bstack1l1l1l1l1l_opy_:
    bstack1l11llll1_opy_(bstack1l1l1l1l1l_opy_)
  if bstack111l1l1111_opy_:
    bstack1ll1l1ll1_opy_(bstack111l1l1111_opy_)
  if bstack1ll1lll11_opy_:
    bstack1ll1l1lll1_opy_()
def bstack1l111llll1_opy_(self, test, *args, **kwargs):
  bstack111ll1l1ll_opy_ = None
  if test:
    bstack111ll1l1ll_opy_ = str(test.name)
  bstack1l1ll11ll1_opy_(test, bstack111ll1l1ll_opy_)
  bstack1l1111l1ll_opy_(self, test, *args, **kwargs)
def bstack1ll1111ll1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1ll11ll111_opy_
  global CONFIG
  global bstack1lll1111l1_opy_
  global bstack1l1l1l1lll_opy_
  global bstack11ll111lll_opy_
  bstack1ll1lll11l_opy_ = None
  try:
    if bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬദ"), None) or bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩധ"), None):
      try:
        if not bstack1l1l1l1lll_opy_:
          bstack11l1ll111l_opy_ = os.path.join(os.path.expanduser(bstack11l11l1_opy_ (u"ࠨࢀࠪന")), bstack11l11l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩഩ"), bstack11l11l1_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬപ"))
          with bstack11ll111lll_opy_:
            if os.path.exists(bstack11l1ll111l_opy_):
              with open(bstack11l1ll111l_opy_, bstack11l11l1_opy_ (u"ࠫࡷ࠭ഫ")) as f:
                content = f.read().strip()
                if content:
                  bstack1lllllll11_opy_ = json.loads(bstack11l11l1_opy_ (u"ࠧࢁࠢബ") + content + bstack11l11l1_opy_ (u"࠭ࠢࡹࠤ࠽ࠤࠧࡿࠢࠨഭ") + bstack11l11l1_opy_ (u"ࠢࡾࠤമ"))
                  bstack1l1l1l1lll_opy_ = bstack1lllllll11_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack11l11l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡌࡈࡸࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠧയ") + str(e))
      if bstack1lll1111l1_opy_:
        with bstack1111l1lll1_opy_:
          bstack111lllll11_opy_ = bstack1lll1111l1_opy_.copy()
        for driver in bstack111lllll11_opy_:
          if bstack1l1l1l1lll_opy_ == driver.session_id:
            bstack1ll1lll11l_opy_ = driver
    bstack1l1lllll1_opy_ = bstack111llll1_opy_.bstack11l1l1l1l_opy_(test.tags)
    if bstack1ll1lll11l_opy_:
      threading.current_thread().isA11yTest = bstack111llll1_opy_.bstack11l111ll1l_opy_(bstack1ll1lll11l_opy_, bstack1l1lllll1_opy_)
      threading.current_thread().isAppA11yTest = bstack111llll1_opy_.bstack11l111ll1l_opy_(bstack1ll1lll11l_opy_, bstack1l1lllll1_opy_)
    else:
      threading.current_thread().isA11yTest = bstack1l1lllll1_opy_
      threading.current_thread().isAppA11yTest = bstack1l1lllll1_opy_
  except:
    pass
  bstack1ll11ll111_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1l1ll1ll1_opy_
  try:
    bstack1l1ll1ll1_opy_ = self._test
  except:
    bstack1l1ll1ll1_opy_ = self.test
def bstack11l1l1ll11_opy_():
  global bstack1111ll1lll_opy_
  try:
    if os.path.exists(bstack1111ll1lll_opy_):
      os.remove(bstack1111ll1lll_opy_)
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬര") + str(e))
def bstack11l11llll_opy_():
  global bstack1111ll1lll_opy_
  bstack1l111l111_opy_ = {}
  lock_file = bstack1111ll1lll_opy_ + bstack11l11l1_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩറ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l11l1_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧല"))
    try:
      if not os.path.isfile(bstack1111ll1lll_opy_):
        with open(bstack1111ll1lll_opy_, bstack11l11l1_opy_ (u"ࠬࡽࠧള")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1111ll1lll_opy_):
        with open(bstack1111ll1lll_opy_, bstack11l11l1_opy_ (u"࠭ࡲࠨഴ")) as f:
          content = f.read().strip()
          if content:
            bstack1l111l111_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack11l11l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩവ") + str(e))
    return bstack1l111l111_opy_
  try:
    os.makedirs(os.path.dirname(bstack1111ll1lll_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack1111ll1lll_opy_):
        with open(bstack1111ll1lll_opy_, bstack11l11l1_opy_ (u"ࠨࡹࠪശ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1111ll1lll_opy_):
        with open(bstack1111ll1lll_opy_, bstack11l11l1_opy_ (u"ࠩࡵࠫഷ")) as f:
          content = f.read().strip()
          if content:
            bstack1l111l111_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬസ") + str(e))
  finally:
    return bstack1l111l111_opy_
def bstack111111l11_opy_(platform_index, item_index):
  global bstack1111ll1lll_opy_
  lock_file = bstack1111ll1lll_opy_ + bstack11l11l1_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪഹ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨഺ"))
    try:
      bstack1l111l111_opy_ = {}
      if os.path.exists(bstack1111ll1lll_opy_):
        with open(bstack1111ll1lll_opy_, bstack11l11l1_opy_ (u"࠭ࡲࠨ഻")) as f:
          content = f.read().strip()
          if content:
            bstack1l111l111_opy_ = json.loads(content)
      bstack1l111l111_opy_[item_index] = platform_index
      with open(bstack1111ll1lll_opy_, bstack11l11l1_opy_ (u"ࠢࡸࠤ഼")) as outfile:
        json.dump(bstack1l111l111_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11l11l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡻࡷ࡯ࡴࡪࡰࡪࠤࡹࡵࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ഽ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack1111ll1lll_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack1l111l111_opy_ = {}
      if os.path.exists(bstack1111ll1lll_opy_):
        with open(bstack1111ll1lll_opy_, bstack11l11l1_opy_ (u"ࠩࡵࠫാ")) as f:
          content = f.read().strip()
          if content:
            bstack1l111l111_opy_ = json.loads(content)
      bstack1l111l111_opy_[item_index] = platform_index
      with open(bstack1111ll1lll_opy_, bstack11l11l1_opy_ (u"ࠥࡻࠧി")) as outfile:
        json.dump(bstack1l111l111_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡷࡳ࡫ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩീ") + str(e))
def bstack11l11111l1_opy_(bstack1111l1l111_opy_):
  global CONFIG
  bstack11ll1lll1l_opy_ = bstack11l11l1_opy_ (u"ࠬ࠭ു")
  if not bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩൂ") in CONFIG:
    logger.info(bstack11l11l1_opy_ (u"ࠧࡏࡱࠣࡴࡱࡧࡴࡧࡱࡵࡱࡸࠦࡰࡢࡵࡶࡩࡩࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫ࡵࡲࠡࡔࡲࡦࡴࡺࠠࡳࡷࡱࠫൃ"))
  try:
    platform = CONFIG[bstack11l11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫൄ")][bstack1111l1l111_opy_]
    if bstack11l11l1_opy_ (u"ࠩࡲࡷࠬ൅") in platform:
      bstack11ll1lll1l_opy_ += str(platform[bstack11l11l1_opy_ (u"ࠪࡳࡸ࠭െ")]) + bstack11l11l1_opy_ (u"ࠫ࠱ࠦࠧേ")
    if bstack11l11l1_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨൈ") in platform:
      bstack11ll1lll1l_opy_ += str(platform[bstack11l11l1_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ൉")]) + bstack11l11l1_opy_ (u"ࠧ࠭ࠢࠪൊ")
    if bstack11l11l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬോ") in platform:
      bstack11ll1lll1l_opy_ += str(platform[bstack11l11l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ൌ")]) + bstack11l11l1_opy_ (u"ࠪ࠰്ࠥ࠭")
    if bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ൎ") in platform:
      bstack11ll1lll1l_opy_ += str(platform[bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ൏")]) + bstack11l11l1_opy_ (u"࠭ࠬࠡࠩ൐")
    if bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ൑") in platform:
      bstack11ll1lll1l_opy_ += str(platform[bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭൒")]) + bstack11l11l1_opy_ (u"ࠩ࠯ࠤࠬ൓")
    if bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫൔ") in platform:
      bstack11ll1lll1l_opy_ += str(platform[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬൕ")]) + bstack11l11l1_opy_ (u"ࠬ࠲ࠠࠨൖ")
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"࠭ࡓࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡰࡨࡶࡦࡺࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡹࡴࡳ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡵࡩࡵࡵࡲࡵࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡳࡳ࠭ൗ") + str(e))
  finally:
    if bstack11ll1lll1l_opy_[len(bstack11ll1lll1l_opy_) - 2:] == bstack11l11l1_opy_ (u"ࠧ࠭ࠢࠪ൘"):
      bstack11ll1lll1l_opy_ = bstack11ll1lll1l_opy_[:-2]
    return bstack11ll1lll1l_opy_
def bstack11l1ll11ll_opy_(path, bstack11ll1lll1l_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack11l1l1llll_opy_ = ET.parse(path)
    bstack11lll1ll1_opy_ = bstack11l1l1llll_opy_.getroot()
    bstack11lllll11_opy_ = None
    for suite in bstack11lll1ll1_opy_.iter(bstack11l11l1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧ൙")):
      if bstack11l11l1_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ൚") in suite.attrib:
        suite.attrib[bstack11l11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨ൛")] += bstack11l11l1_opy_ (u"ࠫࠥ࠭൜") + bstack11ll1lll1l_opy_
        bstack11lllll11_opy_ = suite
    bstack1ll1ll11ll_opy_ = None
    for robot in bstack11lll1ll1_opy_.iter(bstack11l11l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ൝")):
      bstack1ll1ll11ll_opy_ = robot
    bstack1l1111lll1_opy_ = len(bstack1ll1ll11ll_opy_.findall(bstack11l11l1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൞")))
    if bstack1l1111lll1_opy_ == 1:
      bstack1ll1ll11ll_opy_.remove(bstack1ll1ll11ll_opy_.findall(bstack11l11l1_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ൟ"))[0])
      bstack1l11ll1ll1_opy_ = ET.Element(bstack11l11l1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧൠ"), attrib={bstack11l11l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧൡ"): bstack11l11l1_opy_ (u"ࠪࡗࡺ࡯ࡴࡦࡵࠪൢ"), bstack11l11l1_opy_ (u"ࠫ࡮ࡪࠧൣ"): bstack11l11l1_opy_ (u"ࠬࡹ࠰ࠨ൤")})
      bstack1ll1ll11ll_opy_.insert(1, bstack1l11ll1ll1_opy_)
      bstack1lllll1l11_opy_ = None
      for suite in bstack1ll1ll11ll_opy_.iter(bstack11l11l1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൥")):
        bstack1lllll1l11_opy_ = suite
      bstack1lllll1l11_opy_.append(bstack11lllll11_opy_)
      bstack1ll1111lll_opy_ = None
      for status in bstack11lllll11_opy_.iter(bstack11l11l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ൦")):
        bstack1ll1111lll_opy_ = status
      bstack1lllll1l11_opy_.append(bstack1ll1111lll_opy_)
    bstack11l1l1llll_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡸࡳࡪࡰࡪࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹ࠭൧") + str(e))
def bstack1111ll1l11_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1lll1l111l_opy_
  global CONFIG
  if bstack11l11l1_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨ൨") in options:
    del options[bstack11l11l1_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢ൩")]
  json_data = bstack11l11llll_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack11l11l1_opy_ (u"ࠫࡵࡧࡢࡰࡶࡢࡶࡪࡹࡵ࡭ࡶࡶࠫ൪"), str(item_id), bstack11l11l1_opy_ (u"ࠬࡵࡵࡵࡲࡸࡸ࠳ࡾ࡭࡭ࠩ൫"))
    bstack11l1ll11ll_opy_(path, bstack11l11111l1_opy_(json_data[item_id]))
  bstack11l1l1ll11_opy_()
  return bstack1lll1l111l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1l1lll11l1_opy_(self, ff_profile_dir):
  global bstack111l11l111_opy_
  if not ff_profile_dir:
    return None
  return bstack111l11l111_opy_(self, ff_profile_dir)
def bstack1ll1l11l11_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l1111l1l1_opy_
  bstack111l11lll_opy_ = []
  if bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ൬") in CONFIG:
    bstack111l11lll_opy_ = CONFIG[bstack11l11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ൭")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11l11l1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࠤ൮")],
      pabot_args[bstack11l11l1_opy_ (u"ࠤࡹࡩࡷࡨ࡯ࡴࡧࠥ൯")],
      argfile,
      pabot_args.get(bstack11l11l1_opy_ (u"ࠥ࡬࡮ࡼࡥࠣ൰")),
      pabot_args[bstack11l11l1_opy_ (u"ࠦࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠢ൱")],
      platform[0],
      bstack1l1111l1l1_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11l11l1_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡦࡪ࡮ࡨࡷࠧ൲")] or [(bstack11l11l1_opy_ (u"ࠨࠢ൳"), None)]
    for platform in enumerate(bstack111l11lll_opy_)
  ]
def bstack111llll111_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1ll11llll_opy_=bstack11l11l1_opy_ (u"ࠧࠨ൴")):
  global bstack1l1111l11_opy_
  self.platform_index = platform_index
  self.bstack1lll11lll1_opy_ = bstack1ll11llll_opy_
  bstack1l1111l11_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1l1111111l_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l111llll_opy_
  global bstack1l1111lll_opy_
  bstack111lll1l1_opy_ = copy.deepcopy(item)
  if not bstack11l11l1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ൵") in item.options:
    bstack111lll1l1_opy_.options[bstack11l11l1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ൶")] = []
  bstack11ll111111_opy_ = bstack111lll1l1_opy_.options[bstack11l11l1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ൷")].copy()
  for v in bstack111lll1l1_opy_.options[bstack11l11l1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭൸")]:
    if bstack11l11l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫ൹") in v:
      bstack11ll111111_opy_.remove(v)
    if bstack11l11l1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭ൺ") in v:
      bstack11ll111111_opy_.remove(v)
    if bstack11l11l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫൻ") in v:
      bstack11ll111111_opy_.remove(v)
  bstack11ll111111_opy_.insert(0, bstack11l11l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞࠺ࡼࡿࠪർ").format(bstack111lll1l1_opy_.platform_index))
  bstack11ll111111_opy_.insert(0, bstack11l11l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࡀࡻࡾࠩൽ").format(bstack111lll1l1_opy_.bstack1lll11lll1_opy_))
  bstack111lll1l1_opy_.options[bstack11l11l1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬൾ")] = bstack11ll111111_opy_
  if bstack1l1111lll_opy_:
    bstack111lll1l1_opy_.options[bstack11l11l1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ൿ")].insert(0, bstack11l11l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗ࠿ࢁࡽࠨ඀").format(bstack1l1111lll_opy_))
  return bstack1l111llll_opy_(caller_id, datasources, is_last, bstack111lll1l1_opy_, outs_dir)
def bstack1111lll1l_opy_(command, item_index):
  try:
    if bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧඁ")):
      os.environ[bstack11l11l1_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨං")] = json.dumps(CONFIG[bstack11l11l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫඃ")][item_index % bstack1l111l1l1_opy_])
    global bstack1l1111lll_opy_
    if bstack1l1111lll_opy_:
      command[0] = command[0].replace(bstack11l11l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ඄"), bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧඅ") + str(
        item_index) + bstack11l11l1_opy_ (u"ࠫࠥ࠭ආ") + bstack1l1111lll_opy_, 1)
    else:
      command[0] = command[0].replace(bstack11l11l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫඇ"),
                                      bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡹࡤ࡬ࠢࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠢࠪඈ") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack11l11l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦ࡭ࡰࡦ࡬ࡪࡾ࡯࡮ࡨࠢࡦࡳࡲࡳࡡ࡯ࡦࠣࡪࡴࡸࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰ࠽ࠤࢀࢃࠧඉ").format(str(e)))
def bstack1111ll1111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1ll11ll11l_opy_
  try:
    bstack1111lll1l_opy_(command, item_index)
    return bstack1ll11ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack11l11l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࡀࠠࡼࡿࠪඊ").format(str(e)))
    raise e
def bstack1ll1l11ll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1ll11ll11l_opy_
  try:
    bstack1111lll1l_opy_(command, item_index)
    return bstack1ll11ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack11l11l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠳࠰࠴࠷࠿ࠦࡻࡾࠩඋ").format(str(e)))
    try:
      return bstack1ll11ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack11l11l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࠷࠴࠱࠴ࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨඌ").format(str(e2)))
      raise e
def bstack11l11l11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1ll11ll11l_opy_
  try:
    bstack1111lll1l_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack1ll11ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack11l11l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠵࠲࠶࠻࠺ࠡࡽࢀࠫඍ").format(str(e)))
    try:
      return bstack1ll11ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack11l11l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦ࠲࠯࠳࠸ࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪඎ").format(str(e2)))
      raise e
def _1lll1l1ll1_opy_(bstack11ll11l1l_opy_, item_index, process_timeout, sleep_before_start, bstack1l1l11ll1l_opy_):
  bstack1111lll1l_opy_(bstack11ll11l1l_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack1l11lll11l_opy_(command, bstack1l1ll111l1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1ll11ll11l_opy_
  try:
    bstack1111lll1l_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack1ll11ll11l_opy_(command, bstack1l1ll111l1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11l11l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠺࠴࠰࠻ࠢࡾࢁࠬඏ").format(str(e)))
    try:
      return bstack1ll11ll11l_opy_(command, bstack1l1ll111l1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11l11l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧඐ").format(str(e2)))
      raise e
def bstack111l1l11l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1ll11ll11l_opy_
  try:
    process_timeout = _1lll1l1ll1_opy_(command, item_index, process_timeout, sleep_before_start, bstack11l11l1_opy_ (u"ࠨ࠶࠱࠶ࠬඑ"))
    return bstack1ll11ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11l11l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠵࠰࠵࠾ࠥࢁࡽࠨඒ").format(str(e)))
    try:
      return bstack1ll11ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11l11l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪඓ").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack11llllll1_opy_(self, runner, quiet=False, capture=True):
  global bstack11l111l1ll_opy_
  bstack1l1lll1l1_opy_ = bstack11l111l1ll_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11l11l1_opy_ (u"ࠫࡪࡾࡣࡦࡲࡷ࡭ࡴࡴ࡟ࡢࡴࡵࠫඔ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11l11l1_opy_ (u"ࠬ࡫ࡸࡤࡡࡷࡶࡦࡩࡥࡣࡣࡦ࡯ࡤࡧࡲࡳࠩඕ")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1l1lll1l1_opy_
def bstack1l111111l_opy_(runner, hook_name, context, element, bstack111l11111l_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1l1ll11l1l_opy_.bstack11l111l1_opy_(hook_name, element)
    bstack111l11111l_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1l1ll11l1l_opy_.bstack11l1llll_opy_(element)
      if hook_name not in [bstack11l11l1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪඖ"), bstack11l11l1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪ඗")] and args and hasattr(args[0], bstack11l11l1_opy_ (u"ࠨࡧࡵࡶࡴࡸ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠨ඘")):
        args[0].error_message = bstack11l11l1_opy_ (u"ࠩࠪ඙")
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡨࡢࡰࡧࡰࡪࠦࡨࡰࡱ࡮ࡷࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥ࠻ࠢࡾࢁࠬක").format(str(e)))
@measure(event_name=EVENTS.bstack1l1l11lll1_opy_, stage=STAGE.bstack1ll1lllll_opy_, hook_type=bstack11l11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡅࡱࡲࠢඛ"), bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack11ll1l1l11_opy_(runner, name, context, bstack111l11111l_opy_, *args):
    if runner.hooks.get(bstack11l11l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤග")).__name__ != bstack11l11l1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࡢࡨࡪ࡬ࡡࡶ࡮ࡷࡣ࡭ࡵ࡯࡬ࠤඝ"):
      bstack1l111111l_opy_(runner, name, context, runner, bstack111l11111l_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1l1lll1ll_opy_(bstack11l11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ඞ")) else context.browser
      runner.driver_initialised = bstack11l11l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧඟ")
    except Exception as e:
      logger.debug(bstack11l11l1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡪࠦࡡࡵࡶࡵ࡭ࡧࡻࡴࡦ࠼ࠣࡿࢂ࠭ච").format(str(e)))
def bstack111l11ll11_opy_(runner, name, context, bstack111l11111l_opy_, *args):
    bstack1l111111l_opy_(runner, name, context, context.feature, bstack111l11111l_opy_, *args)
    try:
      if not bstack1l11llllll_opy_:
        bstack1ll1lll11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll1ll_opy_(bstack11l11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩඡ")) else context.browser
        if is_driver_active(bstack1ll1lll11l_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack11l11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧජ")
          bstack11l1lll11_opy_ = str(runner.feature.name)
          bstack11lll1111_opy_(context, bstack11l1lll11_opy_)
          bstack1ll1lll11l_opy_.execute_script(bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪඣ") + json.dumps(bstack11l1lll11_opy_) + bstack11l11l1_opy_ (u"࠭ࡽࡾࠩඤ"))
    except Exception as e:
      logger.debug(bstack11l11l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧඥ").format(str(e)))
def bstack1ll11ll1ll_opy_(runner, name, context, bstack111l11111l_opy_, *args):
    if hasattr(context, bstack11l11l1_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪඦ")):
        bstack1l1ll11l1l_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack11l11l1_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫට")) else context.feature
    bstack1l111111l_opy_(runner, name, context, target, bstack111l11111l_opy_, *args)
@measure(event_name=EVENTS.bstack11lllll111_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack11lll1lll_opy_(runner, name, context, bstack111l11111l_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1l1ll11l1l_opy_.start_test(context)
    bstack1l111111l_opy_(runner, name, context, context.scenario, bstack111l11111l_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1ll111l1l1_opy_.bstack1111ll11ll_opy_(context, *args)
    try:
      bstack1ll1lll11l_opy_ = bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩඨ"), context.browser)
      if is_driver_active(bstack1ll1lll11l_opy_):
        bstack1l11l111_opy_.bstack111l1ll111_opy_(bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪඩ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l11l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢඪ")
        if (not bstack1l11llllll_opy_):
          scenario_name = args[0].name
          feature_name = bstack11l1lll11_opy_ = str(runner.feature.name)
          bstack11l1lll11_opy_ = feature_name + bstack11l11l1_opy_ (u"࠭ࠠ࠮ࠢࠪණ") + scenario_name
          if runner.driver_initialised == bstack11l11l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤඬ"):
            bstack11lll1111_opy_(context, bstack11l1lll11_opy_)
            bstack1ll1lll11l_opy_.execute_script(bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭ත") + json.dumps(bstack11l1lll11_opy_) + bstack11l11l1_opy_ (u"ࠩࢀࢁࠬථ"))
    except Exception as e:
      logger.debug(bstack11l11l1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡦࡰࡤࡶ࡮ࡵ࠺ࠡࡽࢀࠫද").format(str(e)))
@measure(event_name=EVENTS.bstack1l1l11lll1_opy_, stage=STAGE.bstack1ll1lllll_opy_, hook_type=bstack11l11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡗࡹ࡫ࡰࠣධ"), bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack1l11l11l1l_opy_(runner, name, context, bstack111l11111l_opy_, *args):
    bstack1l111111l_opy_(runner, name, context, args[0], bstack111l11111l_opy_, *args)
    try:
      bstack1ll1lll11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll1ll_opy_(bstack11l11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫන")) else context.browser
      if is_driver_active(bstack1ll1lll11l_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l11l1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦ඲")
        bstack1l1ll11l1l_opy_.bstack11l11l11_opy_(args[0])
        if runner.driver_initialised == bstack11l11l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧඳ"):
          feature_name = bstack11l1lll11_opy_ = str(runner.feature.name)
          bstack11l1lll11_opy_ = feature_name + bstack11l11l1_opy_ (u"ࠨࠢ࠰ࠤࠬප") + context.scenario.name
          bstack1ll1lll11l_opy_.execute_script(bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧඵ") + json.dumps(bstack11l1lll11_opy_) + bstack11l11l1_opy_ (u"ࠪࢁࢂ࠭බ"))
    except Exception as e:
      logger.debug(bstack11l11l1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡵࡧࡳ࠾ࠥࢁࡽࠨභ").format(str(e)))
@measure(event_name=EVENTS.bstack1l1l11lll1_opy_, stage=STAGE.bstack1ll1lllll_opy_, hook_type=bstack11l11l1_opy_ (u"ࠧࡧࡦࡵࡧࡵࡗࡹ࡫ࡰࠣම"), bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack1ll1llll1_opy_(runner, name, context, bstack111l11111l_opy_, *args):
  bstack1l1ll11l1l_opy_.bstack11l1ll11_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack1ll1lll11l_opy_ = threading.current_thread().bstackSessionDriver if bstack11l11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඹ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1ll1lll11l_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack11l11l1_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧය")
        feature_name = bstack11l1lll11_opy_ = str(runner.feature.name)
        bstack11l1lll11_opy_ = feature_name + bstack11l11l1_opy_ (u"ࠨࠢ࠰ࠤࠬර") + context.scenario.name
        bstack1ll1lll11l_opy_.execute_script(bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ඼") + json.dumps(bstack11l1lll11_opy_) + bstack11l11l1_opy_ (u"ࠪࢁࢂ࠭ල"))
    if str(step_status).lower() == bstack11l11l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ඾"):
      bstack11lll111l1_opy_ = bstack11l11l1_opy_ (u"ࠬ࠭඿")
      bstack111ll1111l_opy_ = bstack11l11l1_opy_ (u"࠭ࠧව")
      bstack1111ll11l_opy_ = bstack11l11l1_opy_ (u"ࠧࠨශ")
      try:
        import traceback
        bstack11lll111l1_opy_ = runner.exception.__class__.__name__
        bstack11l11lll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack111ll1111l_opy_ = bstack11l11l1_opy_ (u"ࠨࠢࠪෂ").join(bstack11l11lll_opy_)
        bstack1111ll11l_opy_ = bstack11l11lll_opy_[-1]
      except Exception as e:
        logger.debug(bstack11111l1lll_opy_.format(str(e)))
      bstack11lll111l1_opy_ += bstack1111ll11l_opy_
      bstack11l1l1lll_opy_(context, json.dumps(str(args[0].name) + bstack11l11l1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣස") + str(bstack111ll1111l_opy_)),
                          bstack11l11l1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤහ"))
      if runner.driver_initialised == bstack11l11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤළ"):
        bstack11l111l11_opy_(getattr(context, bstack11l11l1_opy_ (u"ࠬࡶࡡࡨࡧࠪෆ"), None), bstack11l11l1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ෇"), bstack11lll111l1_opy_)
        bstack1ll1lll11l_opy_.execute_script(bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ෈") + json.dumps(str(args[0].name) + bstack11l11l1_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢ෉") + str(bstack111ll1111l_opy_)) + bstack11l11l1_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࡽࡾ්ࠩ"))
      if runner.driver_initialised == bstack11l11l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣ෋"):
        bstack11l11ll11l_opy_(bstack1ll1lll11l_opy_, bstack11l11l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ෌"), bstack11l11l1_opy_ (u"࡙ࠧࡣࡦࡰࡤࡶ࡮ࡵࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤ෍") + str(bstack11lll111l1_opy_))
    else:
      bstack11l1l1lll_opy_(context, bstack11l11l1_opy_ (u"ࠨࡐࡢࡵࡶࡩࡩࠧࠢ෎"), bstack11l11l1_opy_ (u"ࠢࡪࡰࡩࡳࠧා"))
      if runner.driver_initialised == bstack11l11l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨැ"):
        bstack11l111l11_opy_(getattr(context, bstack11l11l1_opy_ (u"ࠩࡳࡥ࡬࡫ࠧෑ"), None), bstack11l11l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥි"))
      bstack1ll1lll11l_opy_.execute_script(bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩී") + json.dumps(str(args[0].name) + bstack11l11l1_opy_ (u"ࠧࠦ࠭ࠡࡒࡤࡷࡸ࡫ࡤࠢࠤු")) + bstack11l11l1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬ෕"))
      if runner.driver_initialised == bstack11l11l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧූ"):
        bstack11l11ll11l_opy_(bstack1ll1lll11l_opy_, bstack11l11l1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ෗"))
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡳࡵࡧࡳ࠾ࠥࢁࡽࠨෘ").format(str(e)))
  bstack1l111111l_opy_(runner, name, context, args[0], bstack111l11111l_opy_, *args)
@measure(event_name=EVENTS.bstack111111lll1_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack11l11l1ll1_opy_(runner, name, context, bstack111l11111l_opy_, *args):
  bstack1l1ll11l1l_opy_.end_test(args[0])
  try:
    bstack11l1l1111l_opy_ = args[0].status.name
    bstack1ll1lll11l_opy_ = bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩෙ"), context.browser)
    bstack1ll111l1l1_opy_.bstack1l111111ll_opy_(bstack1ll1lll11l_opy_)
    if str(bstack11l1l1111l_opy_).lower() == bstack11l11l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫේ"):
      bstack11lll111l1_opy_ = bstack11l11l1_opy_ (u"ࠬ࠭ෛ")
      bstack111ll1111l_opy_ = bstack11l11l1_opy_ (u"࠭ࠧො")
      bstack1111ll11l_opy_ = bstack11l11l1_opy_ (u"ࠧࠨෝ")
      try:
        import traceback
        bstack11lll111l1_opy_ = runner.exception.__class__.__name__
        bstack11l11lll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack111ll1111l_opy_ = bstack11l11l1_opy_ (u"ࠨࠢࠪෞ").join(bstack11l11lll_opy_)
        bstack1111ll11l_opy_ = bstack11l11lll_opy_[-1]
      except Exception as e:
        logger.debug(bstack11111l1lll_opy_.format(str(e)))
      bstack11lll111l1_opy_ += bstack1111ll11l_opy_
      bstack11l1l1lll_opy_(context, json.dumps(str(args[0].name) + bstack11l11l1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣෟ") + str(bstack111ll1111l_opy_)),
                          bstack11l11l1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ෠"))
      if runner.driver_initialised == bstack11l11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ෡") or runner.driver_initialised == bstack11l11l1_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ෢"):
        bstack11l111l11_opy_(getattr(context, bstack11l11l1_opy_ (u"࠭ࡰࡢࡩࡨࠫ෣"), None), bstack11l11l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ෤"), bstack11lll111l1_opy_)
        bstack1ll1lll11l_opy_.execute_script(bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭෥") + json.dumps(str(args[0].name) + bstack11l11l1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣ෦") + str(bstack111ll1111l_opy_)) + bstack11l11l1_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪ෧"))
      if runner.driver_initialised == bstack11l11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ෨") or runner.driver_initialised == bstack11l11l1_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ෩"):
        bstack11l11ll11l_opy_(bstack1ll1lll11l_opy_, bstack11l11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭෪"), bstack11l11l1_opy_ (u"ࠢࡔࡥࡨࡲࡦࡸࡩࡰࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦ෫") + str(bstack11lll111l1_opy_))
    else:
      bstack11l1l1lll_opy_(context, bstack11l11l1_opy_ (u"ࠣࡒࡤࡷࡸ࡫ࡤࠢࠤ෬"), bstack11l11l1_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢ෭"))
      if runner.driver_initialised == bstack11l11l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ෮") or runner.driver_initialised == bstack11l11l1_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫ෯"):
        bstack11l111l11_opy_(getattr(context, bstack11l11l1_opy_ (u"ࠬࡶࡡࡨࡧࠪ෰"), None), bstack11l11l1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ෱"))
      bstack1ll1lll11l_opy_.execute_script(bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬෲ") + json.dumps(str(args[0].name) + bstack11l11l1_opy_ (u"ࠣࠢ࠰ࠤࡕࡧࡳࡴࡧࡧࠥࠧෳ")) + bstack11l11l1_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧࢃࡽࠨ෴"))
      if runner.driver_initialised == bstack11l11l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ෵") or runner.driver_initialised == bstack11l11l1_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫ෶"):
        bstack11l11ll11l_opy_(bstack1ll1lll11l_opy_, bstack11l11l1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ෷"))
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ෸").format(str(e)))
  bstack1l111111l_opy_(runner, name, context, context.scenario, bstack111l11111l_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack111l1lll1_opy_(runner, name, context, bstack111l11111l_opy_, *args):
    target = context.scenario if hasattr(context, bstack11l11l1_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩ෹")) else context.feature
    bstack1l111111l_opy_(runner, name, context, target, bstack111l11111l_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1111lll111_opy_(runner, name, context, bstack111l11111l_opy_, *args):
    try:
      bstack1ll1lll11l_opy_ = bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ෺"), context.browser)
      bstack1l1l11l111_opy_ = bstack11l11l1_opy_ (u"ࠩࠪ෻")
      if context.failed is True:
        bstack11l1l1l11l_opy_ = []
        bstack11l111111l_opy_ = []
        bstack11ll111l1_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack11l1l1l11l_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l11lll_opy_ = traceback.format_tb(exc_tb)
            bstack1l1l1ll11l_opy_ = bstack11l11l1_opy_ (u"ࠪࠤࠬ෼").join(bstack11l11lll_opy_)
            bstack11l111111l_opy_.append(bstack1l1l1ll11l_opy_)
            bstack11ll111l1_opy_.append(bstack11l11lll_opy_[-1])
        except Exception as e:
          logger.debug(bstack11111l1lll_opy_.format(str(e)))
        bstack11lll111l1_opy_ = bstack11l11l1_opy_ (u"ࠫࠬ෽")
        for i in range(len(bstack11l1l1l11l_opy_)):
          bstack11lll111l1_opy_ += bstack11l1l1l11l_opy_[i] + bstack11ll111l1_opy_[i] + bstack11l11l1_opy_ (u"ࠬࡢ࡮ࠨ෾")
        bstack1l1l11l111_opy_ = bstack11l11l1_opy_ (u"࠭ࠠࠨ෿").join(bstack11l111111l_opy_)
        if runner.driver_initialised in [bstack11l11l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣ฀"), bstack11l11l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧก")]:
          bstack11l1l1lll_opy_(context, bstack1l1l11l111_opy_, bstack11l11l1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣข"))
          bstack11l111l11_opy_(getattr(context, bstack11l11l1_opy_ (u"ࠪࡴࡦ࡭ࡥࠨฃ"), None), bstack11l11l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦค"), bstack11lll111l1_opy_)
          bstack1ll1lll11l_opy_.execute_script(bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪฅ") + json.dumps(bstack1l1l11l111_opy_) + bstack11l11l1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭ฆ"))
          bstack11l11ll11l_opy_(bstack1ll1lll11l_opy_, bstack11l11l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢง"), bstack11l11l1_opy_ (u"ࠣࡕࡲࡱࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯ࡴࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡠࡳࠨจ") + str(bstack11lll111l1_opy_))
          bstack1lll1l11l1_opy_ = bstack11l11l1111_opy_(bstack1l1l11l111_opy_, runner.feature.name, logger)
          if (bstack1lll1l11l1_opy_ != None):
            bstack11lll1ll1l_opy_.append(bstack1lll1l11l1_opy_)
      else:
        if runner.driver_initialised in [bstack11l11l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥฉ"), bstack11l11l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢช")]:
          bstack11l1l1lll_opy_(context, bstack11l11l1_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢซ") + str(runner.feature.name) + bstack11l11l1_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢฌ"), bstack11l11l1_opy_ (u"ࠨࡩ࡯ࡨࡲࠦญ"))
          bstack11l111l11_opy_(getattr(context, bstack11l11l1_opy_ (u"ࠧࡱࡣࡪࡩࠬฎ"), None), bstack11l11l1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣฏ"))
          bstack1ll1lll11l_opy_.execute_script(bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧฐ") + json.dumps(bstack11l11l1_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨ࠾ࠥࠨฑ") + str(runner.feature.name) + bstack11l11l1_opy_ (u"ࠦࠥࡶࡡࡴࡵࡨࡨࠦࠨฒ")) + bstack11l11l1_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫณ"))
          bstack11l11ll11l_opy_(bstack1ll1lll11l_opy_, bstack11l11l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ด"))
          bstack1lll1l11l1_opy_ = bstack11l11l1111_opy_(bstack1l1l11l111_opy_, runner.feature.name, logger)
          if (bstack1lll1l11l1_opy_ != None):
            bstack11lll1ll1l_opy_.append(bstack1lll1l11l1_opy_)
    except Exception as e:
      logger.debug(bstack11l11l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩต").format(str(e)))
    bstack1l111111l_opy_(runner, name, context, context.feature, bstack111l11111l_opy_, *args)
@measure(event_name=EVENTS.bstack1l1l11lll1_opy_, stage=STAGE.bstack1ll1lllll_opy_, hook_type=bstack11l11l1_opy_ (u"ࠣࡣࡩࡸࡪࡸࡁ࡭࡮ࠥถ"), bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack1ll111llll_opy_(runner, name, context, bstack111l11111l_opy_, *args):
    bstack1l111111l_opy_(runner, name, context, runner, bstack111l11111l_opy_, *args)
def bstack11l11l111_opy_(self, name, context, *args):
  try:
    if bstack1ll11l11ll_opy_:
      platform_index = int(threading.current_thread()._name) % bstack1l111l1l1_opy_
      bstack11ll1l1111_opy_ = CONFIG[bstack11l11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬท")][platform_index]
      os.environ[bstack11l11l1_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫธ")] = json.dumps(bstack11ll1l1111_opy_)
    global bstack111l11111l_opy_
    if not hasattr(self, bstack11l11l1_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡥࡥࠩน")):
      self.driver_initialised = None
    bstack111ll1l1l_opy_ = {
        bstack11l11l1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠩบ"): bstack11ll1l1l11_opy_,
        bstack11l11l1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠧป"): bstack111l11ll11_opy_,
        bstack11l11l1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡵࡣࡪࠫผ"): bstack1ll11ll1ll_opy_,
        bstack11l11l1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪฝ"): bstack11lll1lll_opy_,
        bstack11l11l1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠧพ"): bstack1l11l11l1l_opy_,
        bstack11l11l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡸࡪࡶࠧฟ"): bstack1ll1llll1_opy_,
        bstack11l11l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬภ"): bstack11l11l1ll1_opy_,
        bstack11l11l1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡹࡧࡧࠨม"): bstack111l1lll1_opy_,
        bstack11l11l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ย"): bstack1111lll111_opy_,
        bstack11l11l1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪร"): bstack1ll111llll_opy_
    }
    handler = bstack111ll1l1l_opy_.get(name, bstack111l11111l_opy_)
    try:
      handler(self, name, context, bstack111l11111l_opy_, *args)
    except Exception as e:
      logger.debug(bstack11l11l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧࠣ࡬ࡴࡵ࡫ࠡࡪࡤࡲࡩࡲࡥࡳࠢࡾࢁ࠿ࠦࡻࡾࠩฤ").format(name, str(e)))
    if name in [bstack11l11l1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩล"), bstack11l11l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫฦ"), bstack11l11l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧว")]:
      try:
        bstack1ll1lll11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll1ll_opy_(bstack11l11l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫศ")) else context.browser
        bstack11l11lll1_opy_ = (
          (name == bstack11l11l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩษ") and self.driver_initialised == bstack11l11l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦส")) or
          (name == bstack11l11l1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨห") and self.driver_initialised == bstack11l11l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥฬ")) or
          (name == bstack11l11l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫอ") and self.driver_initialised in [bstack11l11l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨฮ"), bstack11l11l1_opy_ (u"ࠧ࡯࡮ࡴࡶࡨࡴࠧฯ")]) or
          (name == bstack11l11l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡴࡦࡲࠪะ") and self.driver_initialised == bstack11l11l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧั"))
        )
        if bstack11l11lll1_opy_:
          self.driver_initialised = None
          if bstack1ll1lll11l_opy_ and hasattr(bstack1ll1lll11l_opy_, bstack11l11l1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠬา")):
            try:
              bstack1ll1lll11l_opy_.quit()
            except Exception as e:
              logger.debug(bstack11l11l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡳࡸ࡭ࡹࡺࡩ࡯ࡩࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࠦࡨࡰࡱ࡮࠾ࠥࢁࡽࠨำ").format(str(e)))
      except Exception as e:
        logger.debug(bstack11l11l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡭ࡵ࡯࡬ࠢࡦࡰࡪࡧ࡮ࡶࡲࠣࡪࡴࡸࠠࡼࡿ࠽ࠤࢀࢃࠧิ").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠫࡈࡸࡩࡵ࡫ࡦࡥࡱࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥࠡࡴࡸࡲࠥ࡮࡯ࡰ࡭ࠣࡿࢂࡀࠠࡼࡿࠪี").format(name, str(e)))
    try:
      bstack111l11111l_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack11l11l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡲࡶ࡮࡭ࡩ࡯ࡣ࡯ࠤࡧ࡫ࡨࡢࡸࡨࠤ࡭ࡵ࡯࡬ࠢࡾࢁ࠿ࠦࡻࡾࠩึ").format(name, str(e2)))
def bstack11ll1l1lll_opy_(config, startdir):
  return bstack11l11l1_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࠲ࢀࠦื").format(bstack11l11l1_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨุ"))
notset = Notset()
def bstack11l111l1l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1ll1111ll_opy_
  if str(name).lower() == bstack11l11l1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨู"):
    return bstack11l11l1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ฺࠣ")
  else:
    return bstack1ll1111ll_opy_(self, name, default, skip)
def bstack111l11lll1_opy_(item, when):
  global bstack1ll1lll1ll_opy_
  try:
    bstack1ll1lll1ll_opy_(item, when)
  except Exception as e:
    pass
def bstack1ll1lll1l1_opy_():
  return
def bstack1ll11l11l1_opy_(type, name, status, reason, bstack11l11111ll_opy_, bstack1lll11ll1l_opy_):
  bstack111ll11l1_opy_ = {
    bstack11l11l1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪ฻"): type,
    bstack11l11l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ฼"): {}
  }
  if type == bstack11l11l1_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ฽"):
    bstack111ll11l1_opy_[bstack11l11l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ฾")][bstack11l11l1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭฿")] = bstack11l11111ll_opy_
    bstack111ll11l1_opy_[bstack11l11l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫเ")][bstack11l11l1_opy_ (u"ࠩࡧࡥࡹࡧࠧแ")] = json.dumps(str(bstack1lll11ll1l_opy_))
  if type == bstack11l11l1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫโ"):
    bstack111ll11l1_opy_[bstack11l11l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧใ")][bstack11l11l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪไ")] = name
  if type == bstack11l11l1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩๅ"):
    bstack111ll11l1_opy_[bstack11l11l1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪๆ")][bstack11l11l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ็")] = status
    if status == bstack11l11l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥ่ࠩ"):
      bstack111ll11l1_opy_[bstack11l11l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ้࠭")][bstack11l11l1_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱ๊ࠫ")] = json.dumps(str(reason))
  bstack11lll1l1l1_opy_ = bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿ๋ࠪ").format(json.dumps(bstack111ll11l1_opy_))
  return bstack11lll1l1l1_opy_
def bstack11ll1ll1l_opy_(driver_command, response):
    if driver_command == bstack11l11l1_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪ์"):
        bstack1l11l111_opy_.bstack1lll1ll111_opy_({
            bstack11l11l1_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭ํ"): response[bstack11l11l1_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧ๎")],
            bstack11l11l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ๏"): bstack1l11l111_opy_.current_test_uuid()
        })
def bstack1l11lll1l1_opy_(item, call, rep):
  global bstack11llll1lll_opy_
  global bstack1lll1111l1_opy_
  global bstack1l11llllll_opy_
  name = bstack11l11l1_opy_ (u"ࠪࠫ๐")
  try:
    if rep.when == bstack11l11l1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ๑"):
      bstack1l1l1l1lll_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1l11llllll_opy_:
          name = str(rep.nodeid)
          bstack1l11l1llll_opy_ = bstack1ll11l11l1_opy_(bstack11l11l1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭๒"), name, bstack11l11l1_opy_ (u"࠭ࠧ๓"), bstack11l11l1_opy_ (u"ࠧࠨ๔"), bstack11l11l1_opy_ (u"ࠨࠩ๕"), bstack11l11l1_opy_ (u"ࠩࠪ๖"))
          threading.current_thread().bstack11111l1ll1_opy_ = name
          for driver in bstack1lll1111l1_opy_:
            if bstack1l1l1l1lll_opy_ == driver.session_id:
              driver.execute_script(bstack1l11l1llll_opy_)
      except Exception as e:
        logger.debug(bstack11l11l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪ๗").format(str(e)))
      try:
        bstack1l1lll1l1l_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11l11l1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ๘"):
          status = bstack11l11l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ๙") if rep.outcome.lower() == bstack11l11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭๚") else bstack11l11l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ๛")
          reason = bstack11l11l1_opy_ (u"ࠨࠩ๜")
          if status == bstack11l11l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ๝"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11l11l1_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨ๞") if status == bstack11l11l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ๟") else bstack11l11l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ๠")
          data = name + bstack11l11l1_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨ๡") if status == bstack11l11l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ๢") else name + bstack11l11l1_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠣࠣࠫ๣") + reason
          bstack111l11l1ll_opy_ = bstack1ll11l11l1_opy_(bstack11l11l1_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫ๤"), bstack11l11l1_opy_ (u"ࠪࠫ๥"), bstack11l11l1_opy_ (u"ࠫࠬ๦"), bstack11l11l1_opy_ (u"ࠬ࠭๧"), level, data)
          for driver in bstack1lll1111l1_opy_:
            if bstack1l1l1l1lll_opy_ == driver.session_id:
              driver.execute_script(bstack111l11l1ll_opy_)
      except Exception as e:
        logger.debug(bstack11l11l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡴࡴࡴࡦࡺࡷࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪ๨").format(str(e)))
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽࢀࠫ๩").format(str(e)))
  bstack11llll1lll_opy_(item, call, rep)
def bstack11ll1lll1_opy_(driver, bstack1ll111l11l_opy_, test=None):
  global bstack11l1l111l1_opy_
  if test != None:
    bstack1l1111l111_opy_ = getattr(test, bstack11l11l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭๪"), None)
    bstack111lll111l_opy_ = getattr(test, bstack11l11l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ๫"), None)
    PercySDK.screenshot(driver, bstack1ll111l11l_opy_, bstack1l1111l111_opy_=bstack1l1111l111_opy_, bstack111lll111l_opy_=bstack111lll111l_opy_, bstack11ll111l11_opy_=bstack11l1l111l1_opy_)
  else:
    PercySDK.screenshot(driver, bstack1ll111l11l_opy_)
@measure(event_name=EVENTS.bstack1l1l1111l_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack1l111ll1ll_opy_(driver):
  if bstack1ll111111l_opy_.bstack111ll1lll1_opy_() is True or bstack1ll111111l_opy_.capturing() is True:
    return
  bstack1ll111111l_opy_.bstack1ll1111l1l_opy_()
  while not bstack1ll111111l_opy_.bstack111ll1lll1_opy_():
    bstack1llll1ll11_opy_ = bstack1ll111111l_opy_.bstack11l1ll1111_opy_()
    bstack11ll1lll1_opy_(driver, bstack1llll1ll11_opy_)
  bstack1ll111111l_opy_.bstack11l1ll11l1_opy_()
def bstack111111111_opy_(sequence, driver_command, response = None, bstack1l1lll111_opy_ = None, args = None):
    try:
      if sequence != bstack11l11l1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪ๬"):
        return
      if percy.bstack1l11ll1111_opy_() == bstack11l11l1_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥ๭"):
        return
      bstack1llll1ll11_opy_ = bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ๮"), None)
      for command in bstack1l11ll1lll_opy_:
        if command == driver_command:
          with bstack1111l1lll1_opy_:
            bstack111lllll11_opy_ = bstack1lll1111l1_opy_.copy()
          for driver in bstack111lllll11_opy_:
            bstack1l111ll1ll_opy_(driver)
      bstack1l1llll1l1_opy_ = percy.bstack1l1ll11111_opy_()
      if driver_command in bstack111lll1ll1_opy_[bstack1l1llll1l1_opy_]:
        bstack1ll111111l_opy_.bstack1lll111l11_opy_(bstack1llll1ll11_opy_, driver_command)
    except Exception as e:
      pass
def bstack11llll1ll1_opy_(framework_name):
  if bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ๯")):
      return
  bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ๰"), True)
  global bstack11111ll1l_opy_
  global bstack111l1l1ll_opy_
  global bstack11l1llll11_opy_
  bstack11111ll1l_opy_ = framework_name
  logger.info(bstack1l1l11l11l_opy_.format(bstack11111ll1l_opy_.split(bstack11l11l1_opy_ (u"ࠨ࠯ࠪ๱"))[0]))
  bstack1l111l11l_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1ll11l11ll_opy_:
      Service.start = bstack1111l11ll_opy_
      Service.stop = bstack1lllllll1l_opy_
      webdriver.Remote.get = bstack111l1l1l1l_opy_
      WebDriver.quit = bstack1l1ll1l1l1_opy_
      webdriver.Remote.__init__ = bstack1l1ll1llll_opy_
    if not bstack1ll11l11ll_opy_:
        webdriver.Remote.__init__ = bstack1ll11l1l1_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack1111ll1l1_opy_
    bstack111l1l1ll_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1ll11l11ll_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1l1l1l1ll1_opy_
  except Exception as e:
    pass
  bstack1l11l11lll_opy_()
  if not bstack111l1l1ll_opy_:
    bstack11111l111_opy_(bstack11l11l1_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦ๲"), bstack11111l1111_opy_)
  if bstack11l1l1lll1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack11l11l1_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ๳")) and callable(getattr(RemoteConnection, bstack11l11l1_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ๴"))):
        RemoteConnection._get_proxy_url = bstack1llll111ll_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack1llll111ll_opy_
    except Exception as e:
      logger.error(bstack11lll1111l_opy_.format(str(e)))
  if bstack1ll11l1ll_opy_():
    bstack1lll1l1111_opy_(CONFIG, logger)
  if (bstack11l11l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ๵") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1l11ll1111_opy_() == bstack11l11l1_opy_ (u"ࠨࡴࡳࡷࡨࠦ๶"):
          bstack1l1ll1ll11_opy_(bstack111111111_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1l1lll11l1_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1111111ll_opy_
      except Exception as e:
        logger.warn(bstack11111lll11_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack11llll111_opy_
      except Exception as e:
        logger.debug(bstack1ll1l1l11_opy_ + str(e))
    except Exception as e:
      bstack11111l111_opy_(e, bstack11111lll11_opy_)
    Output.start_test = bstack11111llll1_opy_
    Output.end_test = bstack1l111llll1_opy_
    TestStatus.__init__ = bstack1ll1111ll1_opy_
    QueueItem.__init__ = bstack111llll111_opy_
    pabot._create_items = bstack1ll1l11l11_opy_
    try:
      from pabot import __version__ as bstack11ll11ll1_opy_
      if version.parse(bstack11ll11ll1_opy_) >= version.parse(bstack11l11l1_opy_ (u"ࠧ࠶࠰࠳࠲࠵࠭๷")):
        pabot._run = bstack1l11lll11l_opy_
      elif version.parse(bstack11ll11ll1_opy_) >= version.parse(bstack11l11l1_opy_ (u"ࠨ࠶࠱࠶࠳࠶ࠧ๸")):
        pabot._run = bstack111l1l11l1_opy_
      elif version.parse(bstack11ll11ll1_opy_) >= version.parse(bstack11l11l1_opy_ (u"ࠩ࠵࠲࠶࠻࠮࠱ࠩ๹")):
        pabot._run = bstack11l11l11l_opy_
      elif version.parse(bstack11ll11ll1_opy_) >= version.parse(bstack11l11l1_opy_ (u"ࠪ࠶࠳࠷࠳࠯࠲ࠪ๺")):
        pabot._run = bstack1ll1l11ll1_opy_
      else:
        pabot._run = bstack1111ll1111_opy_
    except Exception as e:
      pabot._run = bstack1111ll1111_opy_
    pabot._create_command_for_execution = bstack1l1111111l_opy_
    pabot._report_results = bstack1111ll1l11_opy_
  if bstack11l11l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ๻") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11111l111_opy_(e, bstack11ll111ll_opy_)
    Runner.run_hook = bstack11l11l111_opy_
    Step.run = bstack11llllll1_opy_
  if bstack11l11l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ๼") in str(framework_name).lower():
    if not bstack1ll11l11ll_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack11ll1l1lll_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1ll1lll1l1_opy_
      Config.getoption = bstack11l111l1l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1l11lll1l1_opy_
    except Exception as e:
      pass
def bstack11l1111ll1_opy_():
  global CONFIG
  if bstack11l11l1_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭๽") in CONFIG and int(CONFIG[bstack11l11l1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ๾")]) > 1:
    logger.warn(bstack1ll1ll1111_opy_)
def bstack1ll1l1llll_opy_(arg, bstack1lllll1l1_opy_, bstack1111lll1ll_opy_=None):
  global CONFIG
  global bstack1ll1ll111_opy_
  global bstack1l1ll111ll_opy_
  global bstack1ll11l11ll_opy_
  global bstack11111111_opy_
  bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ๿")
  if bstack1lllll1l1_opy_ and isinstance(bstack1lllll1l1_opy_, str):
    bstack1lllll1l1_opy_ = eval(bstack1lllll1l1_opy_)
  CONFIG = bstack1lllll1l1_opy_[bstack11l11l1_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ຀")]
  bstack1ll1ll111_opy_ = bstack1lllll1l1_opy_[bstack11l11l1_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫກ")]
  bstack1l1ll111ll_opy_ = bstack1lllll1l1_opy_[bstack11l11l1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ຂ")]
  bstack1ll11l11ll_opy_ = bstack1lllll1l1_opy_[bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ຃")]
  bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧຄ"), bstack1ll11l11ll_opy_)
  os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ຅")] = bstack1l11lllll_opy_
  os.environ[bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠧຆ")] = json.dumps(CONFIG)
  os.environ[bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡊࡘࡆࡤ࡛ࡒࡍࠩງ")] = bstack1ll1ll111_opy_
  os.environ[bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫຈ")] = str(bstack1l1ll111ll_opy_)
  os.environ[bstack11l11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪຉ")] = str(True)
  if bstack1l1l11l11_opy_(arg, [bstack11l11l1_opy_ (u"ࠬ࠳࡮ࠨຊ"), bstack11l11l1_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ຋")]) != -1:
    os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡂࡔࡄࡐࡑࡋࡌࠨຌ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack11l1lllll1_opy_)
    return
  bstack11l1ll1ll_opy_()
  global bstack11l1l1l1l1_opy_
  global bstack11l1l111l1_opy_
  global bstack1l1111l1l1_opy_
  global bstack1l1111lll_opy_
  global bstack111111ll1_opy_
  global bstack11l1llll11_opy_
  global bstack1l1ll1lll1_opy_
  arg.append(bstack11l11l1_opy_ (u"ࠣ࠯࡚ࠦຍ"))
  arg.append(bstack11l11l1_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦ࠼ࡐࡳࡩࡻ࡬ࡦࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡭ࡲࡶ࡯ࡳࡶࡨࡨ࠿ࡶࡹࡵࡧࡶࡸ࠳ࡖࡹࡵࡧࡶࡸ࡜ࡧࡲ࡯࡫ࡱ࡫ࠧຎ"))
  arg.append(bstack11l11l1_opy_ (u"ࠥ࠱࡜ࠨຏ"))
  arg.append(bstack11l11l1_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨ࠾࡙࡮ࡥࠡࡪࡲࡳࡰ࡯࡭ࡱ࡮ࠥຐ"))
  global bstack11ll1ll11_opy_
  global bstack1l1ll11ll_opy_
  global bstack1l1l1l1ll_opy_
  global bstack1ll11ll111_opy_
  global bstack111l11l111_opy_
  global bstack1l1111l11_opy_
  global bstack1l111llll_opy_
  global bstack11111ll1ll_opy_
  global bstack1llll1111l_opy_
  global bstack1l1l1ll11_opy_
  global bstack1ll1111ll_opy_
  global bstack1ll1lll1ll_opy_
  global bstack11llll1lll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11ll1ll11_opy_ = webdriver.Remote.__init__
    bstack1l1ll11ll_opy_ = WebDriver.quit
    bstack11111ll1ll_opy_ = WebDriver.close
    bstack1llll1111l_opy_ = WebDriver.get
    bstack1l1l1l1ll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1lll1l1l11_opy_(CONFIG) and bstack1lll1l1l1l_opy_():
    if bstack11l1ll1l11_opy_() < version.parse(bstack1111l1l11_opy_):
      logger.error(bstack1l1ll1lll_opy_.format(bstack11l1ll1l11_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11l11l1_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ຑ")) and callable(getattr(RemoteConnection, bstack11l11l1_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧຒ"))):
          bstack1l1l1ll11_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1l1l1ll11_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack11lll1111l_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1ll1111ll_opy_ = Config.getoption
    from _pytest import runner
    bstack1ll1lll1ll_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1lllll11l_opy_)
  try:
    from pytest_bdd import reporting
    bstack11llll1lll_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11l11l1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨຓ"))
  bstack1l1111l1l1_opy_ = CONFIG.get(bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬດ"), {}).get(bstack11l11l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫຕ"))
  bstack1l1ll1lll1_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack11lll11lll_opy_():
      bstack1111ll1ll1_opy_.invoke(Events.CONNECT, bstack1111l11ll1_opy_())
    platform_index = int(os.environ.get(bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪຖ"), bstack11l11l1_opy_ (u"ࠫ࠵࠭ທ")))
  else:
    bstack11llll1ll1_opy_(bstack1ll11111l1_opy_)
  os.environ[bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭ຘ")] = CONFIG[bstack11l11l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨນ")]
  os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪບ")] = CONFIG[bstack11l11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫປ")]
  os.environ[bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬຜ")] = bstack1ll11l11ll_opy_.__str__()
  from _pytest.config import main as bstack1llllll11l_opy_
  bstack1l1llll11l_opy_ = []
  try:
    exit_code = bstack1llllll11l_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1l111l11ll_opy_()
    if bstack11l11l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧຝ") in multiprocessing.current_process().__dict__.keys():
      for bstack1l1l111l1l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l1llll11l_opy_.append(bstack1l1l111l1l_opy_)
    try:
      bstack1l1llllll1_opy_ = (bstack1l1llll11l_opy_, int(exit_code))
      bstack1111lll1ll_opy_.append(bstack1l1llllll1_opy_)
    except:
      bstack1111lll1ll_opy_.append((bstack1l1llll11l_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1l1llll11l_opy_.append({bstack11l11l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩພ"): bstack11l11l1_opy_ (u"ࠬࡖࡲࡰࡥࡨࡷࡸࠦࠧຟ") + os.environ.get(bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ຠ")), bstack11l11l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ມ"): traceback.format_exc(), bstack11l11l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧຢ"): int(os.environ.get(bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩຣ")))})
    bstack1111lll1ll_opy_.append((bstack1l1llll11l_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack11l11l1_opy_ (u"ࠥࡶࡪࡺࡲࡪࡧࡶࠦ຤"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack1l11l11l1_opy_ = e.__class__.__name__
    print(bstack11l11l1_opy_ (u"ࠦࠪࡹ࠺ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡤࡨ࡬ࡦࡼࡥࠡࡶࡨࡷࡹࠦࠥࡴࠤລ") % (bstack1l11l11l1_opy_, e))
    return 1
def bstack11l1l11ll_opy_(arg):
  global bstack111ll1ll1_opy_
  bstack11llll1ll1_opy_(bstack111ll1ll1l_opy_)
  os.environ[bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭຦")] = str(bstack1l1ll111ll_opy_)
  retries = bstack1lll11ll1_opy_.bstack1111lll1_opy_(CONFIG)
  status_code = 0
  if bstack1lll11ll1_opy_.bstack1lll1ll11_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack1l1lllll11_opy_
    status_code = bstack1l1lllll11_opy_(arg)
  if status_code != 0:
    bstack111ll1ll1_opy_ = status_code
def bstack1ll1111l11_opy_():
  logger.info(bstack1l11ll111l_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11l11l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬວ"), help=bstack11l11l1_opy_ (u"ࠧࡈࡧࡱࡩࡷࡧࡴࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡥࡲࡲ࡫࡯ࡧࠨຨ"))
  parser.add_argument(bstack11l11l1_opy_ (u"ࠨ࠯ࡸࠫຩ"), bstack11l11l1_opy_ (u"ࠩ࠰࠱ࡺࡹࡥࡳࡰࡤࡱࡪ࠭ສ"), help=bstack11l11l1_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡶࡵࡨࡶࡳࡧ࡭ࡦࠩຫ"))
  parser.add_argument(bstack11l11l1_opy_ (u"ࠫ࠲ࡱࠧຬ"), bstack11l11l1_opy_ (u"ࠬ࠳࠭࡬ࡧࡼࠫອ"), help=bstack11l11l1_opy_ (u"࡙࠭ࡰࡷࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠧຮ"))
  parser.add_argument(bstack11l11l1_opy_ (u"ࠧ࠮ࡨࠪຯ"), bstack11l11l1_opy_ (u"ࠨ࠯࠰ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ະ"), help=bstack11l11l1_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨັ"))
  bstack1l1ll1l1l_opy_ = parser.parse_args()
  try:
    bstack1111l111ll_opy_ = bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡪࡩࡳ࡫ࡲࡪࡥ࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧາ")
    if bstack1l1ll1l1l_opy_.framework and bstack1l1ll1l1l_opy_.framework not in (bstack11l11l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫຳ"), bstack11l11l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭ິ")):
      bstack1111l111ll_opy_ = bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠯ࡻࡰࡰ࠳ࡹࡡ࡮ࡲ࡯ࡩࠬີ")
    bstack11l1l11lll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1111l111ll_opy_)
    bstack1l11ll1l1l_opy_ = open(bstack11l1l11lll_opy_, bstack11l11l1_opy_ (u"ࠧࡳࠩຶ"))
    bstack1ll1l1111l_opy_ = bstack1l11ll1l1l_opy_.read()
    bstack1l11ll1l1l_opy_.close()
    if bstack1l1ll1l1l_opy_.username:
      bstack1ll1l1111l_opy_ = bstack1ll1l1111l_opy_.replace(bstack11l11l1_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨື"), bstack1l1ll1l1l_opy_.username)
    if bstack1l1ll1l1l_opy_.key:
      bstack1ll1l1111l_opy_ = bstack1ll1l1111l_opy_.replace(bstack11l11l1_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ຸࠫ"), bstack1l1ll1l1l_opy_.key)
    if bstack1l1ll1l1l_opy_.framework:
      bstack1ll1l1111l_opy_ = bstack1ll1l1111l_opy_.replace(bstack11l11l1_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎູࠫ"), bstack1l1ll1l1l_opy_.framework)
    file_name = bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲ຺ࠧ")
    file_path = os.path.abspath(file_name)
    bstack11111l11ll_opy_ = open(file_path, bstack11l11l1_opy_ (u"ࠬࡽࠧົ"))
    bstack11111l11ll_opy_.write(bstack1ll1l1111l_opy_)
    bstack11111l11ll_opy_.close()
    logger.info(bstack11llll1l11_opy_)
    try:
      os.environ[bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨຼ")] = bstack1l1ll1l1l_opy_.framework if bstack1l1ll1l1l_opy_.framework != None else bstack11l11l1_opy_ (u"ࠢࠣຽ")
      config = yaml.safe_load(bstack1ll1l1111l_opy_)
      config[bstack11l11l1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ຾")] = bstack11l11l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠯ࡶࡩࡹࡻࡰࠨ຿")
      bstack1lll1ll11l_opy_(bstack11ll1lll11_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll11llll1_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1l11l1l11_opy_.format(str(e)))
def bstack1lll1ll11l_opy_(bstack1l1l1l11l1_opy_, config, bstack11llll1l1_opy_={}):
  global bstack1ll11l11ll_opy_
  global bstack111l11l11_opy_
  global bstack11111111_opy_
  if not config:
    return
  bstack1l11ll1l11_opy_ = bstack11ll11l111_opy_ if not bstack1ll11l11ll_opy_ else (
    bstack11ll1ll1l1_opy_ if bstack11l11l1_opy_ (u"ࠪࡥࡵࡶࠧເ") in config else (
        bstack1lll111l1l_opy_ if config.get(bstack11l11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨແ")) else bstack11l1l11111_opy_
    )
)
  bstack111l1l111l_opy_ = False
  bstack1ll1l111l_opy_ = False
  if bstack1ll11l11ll_opy_ is True:
      if bstack11l11l1_opy_ (u"ࠬࡧࡰࡱࠩໂ") in config:
          bstack111l1l111l_opy_ = True
      else:
          bstack1ll1l111l_opy_ = True
  bstack111ll11ll1_opy_ = bstack1l1l1ll111_opy_.bstack1111l1ll1l_opy_(config, bstack111l11l11_opy_)
  bstack1ll111l11_opy_ = bstack1lll111111_opy_()
  data = {
    bstack11l11l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨໃ"): config[bstack11l11l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩໄ")],
    bstack11l11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ໅"): config[bstack11l11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬໆ")],
    bstack11l11l1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ໇"): bstack1l1l1l11l1_opy_,
    bstack11l11l1_opy_ (u"ࠫࡩ࡫ࡴࡦࡥࡷࡩࡩࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ່"): os.environ.get(bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ້ࠧ"), bstack111l11l11_opy_),
    bstack11l11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ໊"): bstack1111l1111_opy_,
    bstack11l11l1_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭໋ࠩ"): bstack1l1ll1l11_opy_(),
    bstack11l11l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໌"): {
      bstack11l11l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧໍ"): str(config[bstack11l11l1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ໎")]) if bstack11l11l1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ໏") in config else bstack11l11l1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨ໐"),
      bstack11l11l1_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࡗࡧࡵࡷ࡮ࡵ࡮ࠨ໑"): sys.version,
      bstack11l11l1_opy_ (u"ࠧࡳࡧࡩࡩࡷࡸࡥࡳࠩ໒"): bstack111l1l111_opy_(os.environ.get(bstack11l11l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ໓"), bstack111l11l11_opy_)),
      bstack11l11l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ໔"): bstack11l11l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ໕"),
      bstack11l11l1_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬ໖"): bstack1l11ll1l11_opy_,
      bstack11l11l1_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ໗"): bstack111ll11ll1_opy_,
      bstack11l11l1_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡶࡷ࡬ࡨࠬ໘"): os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ໙")],
      bstack11l11l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ໚"): os.environ.get(bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ໛"), bstack111l11l11_opy_),
      bstack11l11l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ໜ"): bstack1l111l1l11_opy_(os.environ.get(bstack11l11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ໝ"), bstack111l11l11_opy_)),
      bstack11l11l1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫໞ"): bstack1ll111l11_opy_.get(bstack11l11l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫໟ")),
      bstack11l11l1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭໠"): bstack1ll111l11_opy_.get(bstack11l11l1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ໡")),
      bstack11l11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ໢"): config[bstack11l11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໣")] if config[bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ໤")] else bstack11l11l1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨ໥"),
      bstack11l11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ໦"): str(config[bstack11l11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ໧")]) if bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໨") in config else bstack11l11l1_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥ໩"),
      bstack11l11l1_opy_ (u"ࠪࡳࡸ࠭໪"): sys.platform,
      bstack11l11l1_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭໫"): socket.gethostname(),
      bstack11l11l1_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ໬"): bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ໭"))
    }
  }
  if not bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ໮")) is None:
    data[bstack11l11l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໯")][bstack11l11l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡑࡪࡺࡡࡥࡣࡷࡥࠬ໰")] = {
      bstack11l11l1_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ໱"): bstack11l11l1_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩ໲"),
      bstack11l11l1_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬ໳"): bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭໴")),
      bstack11l11l1_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࡎࡶ࡯ࡥࡩࡷ࠭໵"): bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡐࡲࠫ໶"))
    }
  if bstack1l1l1l11l1_opy_ == bstack11ll11l1l1_opy_:
    data[bstack11l11l1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໷")][bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡅࡲࡲ࡫࡯ࡧࠨ໸")] = bstack1ll11lll1l_opy_(config)
    data[bstack11l11l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ໹")][bstack11l11l1_opy_ (u"ࠬ࡯ࡳࡑࡧࡵࡧࡾࡇࡵࡵࡱࡈࡲࡦࡨ࡬ࡦࡦࠪ໺")] = percy.bstack11llllll1l_opy_
    data[bstack11l11l1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ໻")][bstack11l11l1_opy_ (u"ࠧࡱࡧࡵࡧࡾࡈࡵࡪ࡮ࡧࡍࡩ࠭໼")] = percy.percy_build_id
  if not bstack1lll11ll1_opy_.bstack1l11l111l_opy_(CONFIG):
    data[bstack11l11l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໽")][bstack11l11l1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠭໾")] = bstack1lll11ll1_opy_.bstack1l11l111l_opy_(CONFIG)
  bstack1llll1l11_opy_ = bstack1llllll1l_opy_.bstack1llll1ll1_opy_(CONFIG, logger)
  bstack111lll1l_opy_ = bstack1lll11ll1_opy_.bstack1llll1ll1_opy_(config=CONFIG)
  if bstack1llll1l11_opy_ is not None and bstack111lll1l_opy_ is not None and bstack111lll1l_opy_.bstack111ll111_opy_():
    data[bstack11l11l1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໿")][bstack111lll1l_opy_.bstack1l1lll111l_opy_()] = bstack1llll1l11_opy_.bstack1l11l11ll_opy_()
  update(data[bstack11l11l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧༀ")], bstack11llll1l1_opy_)
  try:
    response = bstack1ll1l1l11l_opy_(bstack11l11l1_opy_ (u"ࠬࡖࡏࡔࡖࠪ༁"), bstack1l111111l1_opy_(bstack111llllll_opy_), data, {
      bstack11l11l1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ༂"): (config[bstack11l11l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ༃")], config[bstack11l11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ༄")])
    })
    if response:
      logger.debug(bstack1l1111ll1_opy_.format(bstack1l1l1l11l1_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack111lll11l_opy_.format(str(e)))
def bstack111l1l111_opy_(framework):
  return bstack11l11l1_opy_ (u"ࠤࡾࢁ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨ༅").format(str(framework), __version__) if framework else bstack11l11l1_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦ༆").format(
    __version__)
def bstack11l1ll1ll_opy_():
  global CONFIG
  global bstack1ll111lll1_opy_
  if bool(CONFIG):
    return
  try:
    bstack11l111lll_opy_()
    logger.debug(bstack11l11ll111_opy_.format(str(CONFIG)))
    bstack1ll111lll1_opy_ = bstack11111l1l1_opy_.configure_logger(CONFIG, bstack1ll111lll1_opy_)
    bstack1l111l11l_opy_()
  except Exception as e:
    logger.error(bstack11l11l1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵ࠲ࠠࡦࡴࡵࡳࡷࡀࠠࠣ༇") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1ll1l1l1l1_opy_
  atexit.register(bstack1l1ll111l_opy_)
  signal.signal(signal.SIGINT, bstack11111lll1_opy_)
  signal.signal(signal.SIGTERM, bstack11111lll1_opy_)
def bstack1ll1l1l1l1_opy_(exctype, value, traceback):
  global bstack1lll1111l1_opy_
  try:
    for driver in bstack1lll1111l1_opy_:
      bstack11l11ll11l_opy_(driver, bstack11l11l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ༈"), bstack11l11l1_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤ༉") + str(value))
  except Exception:
    pass
  logger.info(bstack111llll1l1_opy_)
  bstack11ll11l1ll_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack11ll11l1ll_opy_(message=bstack11l11l1_opy_ (u"ࠧࠨ༊"), bstack11lll1l11l_opy_ = False):
  global CONFIG
  bstack11ll1111ll_opy_ = bstack11l11l1_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡆࡺࡦࡩࡵࡺࡩࡰࡰࠪ་") if bstack11lll1l11l_opy_ else bstack11l11l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ༌")
  try:
    if message:
      bstack11llll1l1_opy_ = {
        bstack11ll1111ll_opy_ : str(message)
      }
      bstack1lll1ll11l_opy_(bstack11ll11l1l1_opy_, CONFIG, bstack11llll1l1_opy_)
    else:
      bstack1lll1ll11l_opy_(bstack11ll11l1l1_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack11111l11l1_opy_.format(str(e)))
def bstack1l11111111_opy_(bstack11llll1l1l_opy_, size):
  bstack1l111l1ll_opy_ = []
  while len(bstack11llll1l1l_opy_) > size:
    bstack1111lll1l1_opy_ = bstack11llll1l1l_opy_[:size]
    bstack1l111l1ll_opy_.append(bstack1111lll1l1_opy_)
    bstack11llll1l1l_opy_ = bstack11llll1l1l_opy_[size:]
  bstack1l111l1ll_opy_.append(bstack11llll1l1l_opy_)
  return bstack1l111l1ll_opy_
def bstack1l1lll11ll_opy_(args):
  if bstack11l11l1_opy_ (u"ࠪ࠱ࡲ࠭།") in args and bstack11l11l1_opy_ (u"ࠫࡵࡪࡢࠨ༎") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack1l11l1ll1_opy_, stage=STAGE.bstack111l111ll1_opy_)
def run_on_browserstack(bstack1llll11lll_opy_=None, bstack1111lll1ll_opy_=None, bstack11l111ll11_opy_=False):
  global CONFIG
  global bstack1ll1ll111_opy_
  global bstack1l1ll111ll_opy_
  global bstack111l11l11_opy_
  global bstack11111111_opy_
  bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"ࠬ࠭༏")
  bstack11111111l_opy_(bstack1l11ll11ll_opy_, logger)
  if bstack1llll11lll_opy_ and isinstance(bstack1llll11lll_opy_, str):
    bstack1llll11lll_opy_ = eval(bstack1llll11lll_opy_)
  if bstack1llll11lll_opy_:
    CONFIG = bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭༐")]
    bstack1ll1ll111_opy_ = bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ༑")]
    bstack1l1ll111ll_opy_ = bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ༒")]
    bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ༓"), bstack1l1ll111ll_opy_)
    bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༔")
  bstack11111111_opy_.set_property(bstack11l11l1_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭༕"), uuid4().__str__())
  logger.info(bstack11l11l1_opy_ (u"࡙ࠬࡄࡌࠢࡵࡹࡳࠦࡳࡵࡣࡵࡸࡪࡪࠠࡸ࡫ࡷ࡬ࠥ࡯ࡤ࠻ࠢࠪ༖") + bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ༗")));
  logger.debug(bstack11l11l1_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥ࠿༘ࠪ") + bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦ༙ࠪ")))
  if not bstack11l111ll11_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack11l1lllll1_opy_)
      return
    if sys.argv[1] == bstack11l11l1_opy_ (u"ࠩ࠰࠱ࡻ࡫ࡲࡴ࡫ࡲࡲࠬ༚") or sys.argv[1] == bstack11l11l1_opy_ (u"ࠪ࠱ࡻ࠭༛"):
      logger.info(bstack11l11l1_opy_ (u"ࠫࡇࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡔࡾࡺࡨࡰࡰࠣࡗࡉࡑࠠࡷࡽࢀࠫ༜").format(__version__))
      return
    if sys.argv[1] == bstack11l11l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ༝"):
      bstack1ll1111l11_opy_()
      return
  args = sys.argv
  bstack11l1ll1ll_opy_()
  global bstack11l1l1l1l1_opy_
  global bstack1l111l1l1_opy_
  global bstack1l1ll1lll1_opy_
  global bstack1llll1l1l1_opy_
  global bstack11l1l111l1_opy_
  global bstack1l1111l1l1_opy_
  global bstack1l1111lll_opy_
  global bstack1ll1ll1lll_opy_
  global bstack111111ll1_opy_
  global bstack11l1llll11_opy_
  global bstack1ll11l1l11_opy_
  bstack1l111l1l1_opy_ = len(CONFIG.get(bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ༞"), []))
  if not bstack1l11lllll_opy_:
    if args[1] == bstack11l11l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༟") or args[1] == bstack11l11l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩ༠"):
      bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༡")
      args = args[2:]
    elif args[1] == bstack11l11l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ༢"):
      bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༣")
      args = args[2:]
    elif args[1] == bstack11l11l1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ༤"):
      bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ༥")
      args = args[2:]
    elif args[1] == bstack11l11l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ༦"):
      bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ༧")
      args = args[2:]
    elif args[1] == bstack11l11l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ༨"):
      bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ༩")
      args = args[2:]
    elif args[1] == bstack11l11l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ༪"):
      bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ༫")
      args = args[2:]
    else:
      if not bstack11l11l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༬") in CONFIG or str(CONFIG[bstack11l11l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༭")]).lower() in [bstack11l11l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ༮"), bstack11l11l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ༯")]:
        bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༰")
        args = args[1:]
      elif str(CONFIG[bstack11l11l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ༱")]).lower() == bstack11l11l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༲"):
        bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ༳")
        args = args[1:]
      elif str(CONFIG[bstack11l11l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༴")]).lower() == bstack11l11l1_opy_ (u"ࠨࡲࡤࡦࡴࡺ༵ࠧ"):
        bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༶")
        args = args[1:]
      elif str(CONFIG[bstack11l11l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ༷࠭")]).lower() == bstack11l11l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༸"):
        bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ༹ࠬ")
        args = args[1:]
      elif str(CONFIG[bstack11l11l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༺")]).lower() == bstack11l11l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ༻"):
        bstack1l11lllll_opy_ = bstack11l11l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ༼")
        args = args[1:]
      else:
        os.environ[bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ༽")] = bstack1l11lllll_opy_
        bstack11l1l1111_opy_(bstack1ll1llll11_opy_)
  os.environ[bstack11l11l1_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫ༾")] = bstack1l11lllll_opy_
  bstack111l11l11_opy_ = bstack1l11lllll_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack11111lll1l_opy_ = bstack1l111l1lll_opy_[bstack11l11l1_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗ࠱ࡇࡊࡄࠨ༿")] if bstack1l11lllll_opy_ == bstack11l11l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཀ") and bstack11l1llllll_opy_() else bstack1l11lllll_opy_
      bstack1111ll1ll1_opy_.invoke(Events.bstack11llll11l1_opy_, bstack11l1llll1l_opy_(
        sdk_version=__version__,
        path_config=bstack1l111lll11_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack11111lll1l_opy_,
        frameworks=[bstack11111lll1l_opy_],
        framework_versions={
          bstack11111lll1l_opy_: bstack1l111l1l11_opy_(bstack11l11l1_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬཁ") if bstack1l11lllll_opy_ in [bstack11l11l1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ག"), bstack11l11l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧགྷ"), bstack11l11l1_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪང")] else bstack1l11lllll_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack11l11l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧཅ"), None):
        CONFIG[bstack11l11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨཆ")] = cli.config.get(bstack11l11l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢཇ"), None)
    except Exception as e:
      bstack1111ll1ll1_opy_.invoke(Events.bstack11111l11l_opy_, e.__traceback__, 1)
    if bstack1l1ll111ll_opy_:
      CONFIG[bstack11l11l1_opy_ (u"ࠨࡡࡱࡲࠥ཈")] = cli.config[bstack11l11l1_opy_ (u"ࠢࡢࡲࡳࠦཉ")]
      logger.info(bstack1l1lll1l11_opy_.format(CONFIG[bstack11l11l1_opy_ (u"ࠨࡣࡳࡴࠬཊ")]))
  else:
    bstack1111ll1ll1_opy_.clear()
  global bstack11l1lll1l1_opy_
  global bstack11ll1l111_opy_
  if bstack1llll11lll_opy_:
    try:
      bstack1l11lll1ll_opy_ = datetime.datetime.now()
      os.environ[bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫཋ")] = bstack1l11lllll_opy_
      bstack1lll1ll11l_opy_(bstack1l1l1111l1_opy_, CONFIG)
      cli.bstack111lll1ll_opy_(bstack11l11l1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡵࡧ࡯ࡤࡺࡥࡴࡶࡢࡥࡹࡺࡥ࡮ࡲࡷࡩࡩࠨཌ"), datetime.datetime.now() - bstack1l11lll1ll_opy_)
    except Exception as e:
      logger.debug(bstack111lll1111_opy_.format(str(e)))
  global bstack11ll1ll11_opy_
  global bstack1l1ll11ll_opy_
  global bstack11111l111l_opy_
  global bstack1l1111l1ll_opy_
  global bstack1ll1l1ll1_opy_
  global bstack1l11llll1_opy_
  global bstack1ll11ll111_opy_
  global bstack111l11l111_opy_
  global bstack1ll11ll11l_opy_
  global bstack1l1111l11_opy_
  global bstack1l111llll_opy_
  global bstack11111ll1ll_opy_
  global bstack111l11111l_opy_
  global bstack11l111l1ll_opy_
  global bstack1llll1111l_opy_
  global bstack1l1l1ll11_opy_
  global bstack1ll1111ll_opy_
  global bstack1ll1lll1ll_opy_
  global bstack1lll1l111l_opy_
  global bstack11llll1lll_opy_
  global bstack1l1l1l1ll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack11ll1ll11_opy_ = webdriver.Remote.__init__
    bstack1l1ll11ll_opy_ = WebDriver.quit
    bstack11111ll1ll_opy_ = WebDriver.close
    bstack1llll1111l_opy_ = WebDriver.get
    bstack1l1l1l1ll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack11l1lll1l1_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1l1111ll11_opy_
    bstack11ll1l111_opy_ = bstack1l1111ll11_opy_()
  except Exception as e:
    pass
  try:
    global bstack1ll1l1lll1_opy_
    from QWeb.keywords import browser
    bstack1ll1l1lll1_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1lll1l1l11_opy_(CONFIG) and bstack1lll1l1l1l_opy_():
    if bstack11l1ll1l11_opy_() < version.parse(bstack1111l1l11_opy_):
      logger.error(bstack1l1ll1lll_opy_.format(bstack11l1ll1l11_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11l11l1_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬཌྷ")) and callable(getattr(RemoteConnection, bstack11l11l1_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ཎ"))):
          RemoteConnection._get_proxy_url = bstack1llll111ll_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack1llll111ll_opy_
      except Exception as e:
        logger.error(bstack11lll1111l_opy_.format(str(e)))
  if not CONFIG.get(bstack11l11l1_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨཏ"), False) and not bstack1llll11lll_opy_:
    logger.info(bstack11llll1ll_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack11l11l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫཐ") in CONFIG and str(CONFIG[bstack11l11l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬད")]).lower() != bstack11l11l1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨདྷ"):
      bstack1ll11lllll_opy_()
    elif bstack1l11lllll_opy_ != bstack11l11l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪན") or (bstack1l11lllll_opy_ == bstack11l11l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫཔ") and not bstack1llll11lll_opy_):
      bstack1l1l11ll11_opy_()
  if (bstack1l11lllll_opy_ in [bstack11l11l1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫཕ"), bstack11l11l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬབ"), bstack11l11l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨབྷ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1l1lll11l1_opy_
        bstack1l11llll1_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack11111lll11_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1ll1l1ll1_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1ll1l1l11_opy_ + str(e))
    except Exception as e:
      bstack11111l111_opy_(e, bstack11111lll11_opy_)
    if bstack1l11lllll_opy_ != bstack11l11l1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩམ"):
      bstack11l1l1ll11_opy_()
    bstack11111l111l_opy_ = Output.start_test
    bstack1l1111l1ll_opy_ = Output.end_test
    bstack1ll11ll111_opy_ = TestStatus.__init__
    bstack1ll11ll11l_opy_ = pabot._run
    bstack1l1111l11_opy_ = QueueItem.__init__
    bstack1l111llll_opy_ = pabot._create_command_for_execution
    bstack1lll1l111l_opy_ = pabot._report_results
  if bstack1l11lllll_opy_ == bstack11l11l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩཙ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11111l111_opy_(e, bstack11ll111ll_opy_)
    bstack111l11111l_opy_ = Runner.run_hook
    bstack11l111l1ll_opy_ = Step.run
  if bstack1l11lllll_opy_ == bstack11l11l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪཚ"):
    try:
      from _pytest.config import Config
      bstack1ll1111ll_opy_ = Config.getoption
      from _pytest import runner
      bstack1ll1lll1ll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1lllll11l_opy_)
    try:
      from pytest_bdd import reporting
      bstack11llll1lll_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11l11l1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬཛ"))
  try:
    framework_name = bstack11l11l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫཛྷ") if bstack1l11lllll_opy_ in [bstack11l11l1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬཝ"), bstack11l11l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ཞ"), bstack11l11l1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩཟ")] else bstack11l1l1l1ll_opy_(bstack1l11lllll_opy_)
    bstack111llllll1_opy_ = {
      bstack11l11l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࠪའ"): bstack11l11l1_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬཡ") if bstack1l11lllll_opy_ == bstack11l11l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫར") and bstack11l1llllll_opy_() else framework_name,
      bstack11l11l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩལ"): bstack1l111l1l11_opy_(framework_name),
      bstack11l11l1_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫཤ"): __version__,
      bstack11l11l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨཥ"): bstack1l11lllll_opy_
    }
    if bstack1l11lllll_opy_ in bstack1lll1lllll_opy_ + bstack11l11l11ll_opy_:
      if bstack111llll1_opy_.bstack111l1ll11l_opy_(CONFIG):
        if bstack11l11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨས") in CONFIG:
          os.environ[bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪཧ")] = os.getenv(bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫཨ"), json.dumps(CONFIG[bstack11l11l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫཀྵ")]))
          CONFIG[bstack11l11l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬཪ")].pop(bstack11l11l1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫཫ"), None)
          CONFIG[bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧཬ")].pop(bstack11l11l1_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭཭"), None)
        bstack111llllll1_opy_[bstack11l11l1_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ཮")] = {
          bstack11l11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨ཯"): bstack11l11l1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭཰"),
          bstack11l11l1_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳཱ࠭"): str(bstack11l1ll1l11_opy_())
        }
    if bstack1l11lllll_opy_ not in [bstack11l11l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲིࠧ")] and not cli.is_running():
      bstack11l11l111l_opy_, bstack11l1l11l11_opy_ = bstack1l11l111_opy_.launch(CONFIG, bstack111llllll1_opy_)
      if bstack11l1l11l11_opy_.get(bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿཱིࠧ")) is not None and bstack111llll1_opy_.bstack111l1l1l11_opy_(CONFIG) is None:
        value = bstack11l1l11l11_opy_[bstack11l11l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨུ")].get(bstack11l11l1_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵཱུࠪ"))
        if value is not None:
            CONFIG[bstack11l11l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪྲྀ")] = value
        else:
          logger.debug(bstack11l11l1_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡥࡣࡷࡥࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤཷ"))
  except Exception as e:
    logger.debug(bstack1l1l111lll_opy_.format(bstack11l11l1_opy_ (u"࡚ࠬࡥࡴࡶࡋࡹࡧ࠭ླྀ"), str(e)))
  if bstack1l11lllll_opy_ == bstack11l11l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ཹ"):
    bstack1l1ll1lll1_opy_ = True
    if bstack1llll11lll_opy_ and bstack11l111ll11_opy_:
      bstack1l1111l1l1_opy_ = CONFIG.get(bstack11l11l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶེࠫ"), {}).get(bstack11l11l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴཻࠪ"))
      bstack11llll1ll1_opy_(bstack111l111l1_opy_)
    elif bstack1llll11lll_opy_:
      bstack1l1111l1l1_opy_ = CONFIG.get(bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸོ࠭"), {}).get(bstack11l11l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶཽࠬ"))
      global bstack1lll1111l1_opy_
      try:
        if bstack1l1lll11ll_opy_(bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཾ")]) and multiprocessing.current_process().name == bstack11l11l1_opy_ (u"ࠬ࠶ࠧཿ"):
          bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦྀࠩ")].remove(bstack11l11l1_opy_ (u"ࠧ࠮࡯ཱྀࠪ"))
          bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྂ")].remove(bstack11l11l1_opy_ (u"ࠩࡳࡨࡧ࠭ྃ"))
          bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ྄࠭")] = bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ྅")][0]
          with open(bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ྆")], bstack11l11l1_opy_ (u"࠭ࡲࠨ྇")) as f:
            file_content = f.read()
          bstack11111lllll_opy_ = bstack11l11l1_opy_ (u"ࠢࠣࠤࡩࡶࡴࡳࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡥ࡭ࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡁࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࠫࡿࢂ࠯࠻ࠡࡨࡵࡳࡲࠦࡰࡥࡤࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡔࡩࡨ࠻ࠡࡱࡪࡣࡩࡨࠠ࠾ࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡥࡧࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯࠭ࡹࡥ࡭ࡨ࠯ࠤࡦࡸࡧ࠭ࠢࡷࡩࡲࡶ࡯ࡳࡣࡵࡽࠥࡃࠠ࠱ࠫ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡶࡾࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡢࡴࡪࠤࡂࠦࡳࡵࡴࠫ࡭ࡳࡺࠨࡢࡴࡪ࠭࠰࠷࠰ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦࡺࡦࡩࡵࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡥࡸࠦࡥ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡸࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡵࡧࡠࡦࡥࠬࡸ࡫࡬ࡧ࠮ࡤࡶ࡬࠲ࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡥࡤ࠱ࡨࡴࡥࡢࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫ࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠮ࠩ࠯ࡵࡨࡸࡤࡺࡲࡢࡥࡨࠬ࠮ࡢ࡮ࠣࠤࠥྈ").format(str(bstack1llll11lll_opy_))
          bstack1ll11l1lll_opy_ = bstack11111lllll_opy_ + file_content
          bstack111ll11ll_opy_ = bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྉ")] + bstack11l11l1_opy_ (u"ࠩࡢࡦࡸࡺࡡࡤ࡭ࡢࡸࡪࡳࡰ࠯ࡲࡼࠫྊ")
          with open(bstack111ll11ll_opy_, bstack11l11l1_opy_ (u"ࠪࡻࠬྋ")):
            pass
          with open(bstack111ll11ll_opy_, bstack11l11l1_opy_ (u"ࠦࡼ࠱ࠢྌ")) as f:
            f.write(bstack1ll11l1lll_opy_)
          import subprocess
          process_data = subprocess.run([bstack11l11l1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧྍ"), bstack111ll11ll_opy_])
          if os.path.exists(bstack111ll11ll_opy_):
            os.unlink(bstack111ll11ll_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack1l1lll11ll_opy_(bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྎ")]):
            bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྏ")].remove(bstack11l11l1_opy_ (u"ࠨ࠯ࡰࠫྐ"))
            bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྑ")].remove(bstack11l11l1_opy_ (u"ࠪࡴࡩࡨࠧྒ"))
            bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྒྷ")] = bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྔ")][0]
          bstack11llll1ll1_opy_(bstack111l111l1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྕ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11l11l1_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩྖ")] = bstack11l11l1_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪྗ")
          mod_globals[bstack11l11l1_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫ྘")] = os.path.abspath(bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྙ")])
          exec(open(bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྚ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11l11l1_opy_ (u"ࠬࡉࡡࡶࡩ࡫ࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠬྛ").format(str(e)))
          for driver in bstack1lll1111l1_opy_:
            bstack1111lll1ll_opy_.append({
              bstack11l11l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫྜ"): bstack1llll11lll_opy_[bstack11l11l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྜྷ")],
              bstack11l11l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧྞ"): str(e),
              bstack11l11l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨྟ"): multiprocessing.current_process().name
            })
            bstack11l11ll11l_opy_(driver, bstack11l11l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪྠ"), bstack11l11l1_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢྡ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1lll1111l1_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1l1ll111ll_opy_, CONFIG, logger)
      bstack111l1l1lll_opy_()
      bstack11l1111ll1_opy_()
      percy.bstack111ll111l_opy_()
      bstack1lllll1l1_opy_ = {
        bstack11l11l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྡྷ"): args[0],
        bstack11l11l1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭ྣ"): CONFIG,
        bstack11l11l1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨྤ"): bstack1ll1ll111_opy_,
        bstack11l11l1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪྥ"): bstack1l1ll111ll_opy_
      }
      if bstack11l11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྦ") in CONFIG:
        bstack1ll111ll1l_opy_ = bstack1l1l1l111_opy_(args, logger, CONFIG, bstack1ll11l11ll_opy_, bstack1l111l1l1_opy_)
        bstack1ll1ll1lll_opy_ = bstack1ll111ll1l_opy_.bstack1llll11l1_opy_(run_on_browserstack, bstack1lllll1l1_opy_, bstack1l1lll11ll_opy_(args))
      else:
        if bstack1l1lll11ll_opy_(args):
          bstack1lllll1l1_opy_[bstack11l11l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྦྷ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1lllll1l1_opy_,))
          test.start()
          test.join()
        else:
          bstack11llll1ll1_opy_(bstack111l111l1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11l11l1_opy_ (u"ࠫࡤࡥ࡮ࡢ࡯ࡨࡣࡤ࠭ྨ")] = bstack11l11l1_opy_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧྩ")
          mod_globals[bstack11l11l1_opy_ (u"࠭࡟ࡠࡨ࡬ࡰࡪࡥ࡟ࠨྪ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1l11lllll_opy_ == bstack11l11l1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ྫ") or bstack1l11lllll_opy_ == bstack11l11l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧྫྷ"):
    percy.init(bstack1l1ll111ll_opy_, CONFIG, logger)
    percy.bstack111ll111l_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack11111l111_opy_(e, bstack11111lll11_opy_)
    bstack111l1l1lll_opy_()
    bstack11llll1ll1_opy_(bstack11ll1l11l1_opy_)
    if bstack1ll11l11ll_opy_:
      bstack1l111l1l1l_opy_(bstack11ll1l11l1_opy_, args)
      if bstack11l11l1_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧྭ") in args:
        i = args.index(bstack11l11l1_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨྮ"))
        args.pop(i)
        args.pop(i)
      if bstack11l11l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྯ") not in CONFIG:
        CONFIG[bstack11l11l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨྰ")] = [{}]
        bstack1l111l1l1_opy_ = 1
      if bstack11l1l1l1l1_opy_ == 0:
        bstack11l1l1l1l1_opy_ = 1
      args.insert(0, str(bstack11l1l1l1l1_opy_))
      args.insert(0, str(bstack11l11l1_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫྱ")))
    if bstack1l11l111_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack111l11l1l_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack111l11l11l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11l11l1_opy_ (u"ࠢࡓࡑࡅࡓ࡙ࡥࡏࡑࡖࡌࡓࡓ࡙ࠢྲ"),
        ).parse_args(bstack111l11l1l_opy_)
        bstack11l1111l1_opy_ = args.index(bstack111l11l1l_opy_[0]) if len(bstack111l11l1l_opy_) > 0 else len(args)
        args.insert(bstack11l1111l1_opy_, str(bstack11l11l1_opy_ (u"ࠨ࠯࠰ࡰ࡮ࡹࡴࡦࡰࡨࡶࠬླ")))
        args.insert(bstack11l1111l1_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l11l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡵࡳࡧࡵࡴࡠ࡮࡬ࡷࡹ࡫࡮ࡦࡴ࠱ࡴࡾ࠭ྴ"))))
        if bstack1lll11ll1_opy_.bstack1lll1ll11_opy_(CONFIG):
          args.insert(bstack11l1111l1_opy_, str(bstack11l11l1_opy_ (u"ࠪ࠱࠲ࡲࡩࡴࡶࡨࡲࡪࡸࠧྵ")))
          args.insert(bstack11l1111l1_opy_ + 1, str(bstack11l11l1_opy_ (u"ࠫࡗ࡫ࡴࡳࡻࡉࡥ࡮ࡲࡥࡥ࠼ࡾࢁࠬྶ").format(bstack1lll11ll1_opy_.bstack1111lll1_opy_(CONFIG))))
        if bstack111lll11l1_opy_(os.environ.get(bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࠪྷ"))) and str(os.environ.get(bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠪྸ"), bstack11l11l1_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬྐྵ"))) != bstack11l11l1_opy_ (u"ࠨࡰࡸࡰࡱ࠭ྺ"):
          for bstack11ll1ll111_opy_ in bstack111l11l11l_opy_:
            args.remove(bstack11ll1ll111_opy_)
          test_files = os.environ.get(bstack11l11l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘ࠭ྻ")).split(bstack11l11l1_opy_ (u"ࠪ࠰ࠬྼ"))
          for bstack1ll1l11111_opy_ in test_files:
            args.append(bstack1ll1l11111_opy_)
      except Exception as e:
        logger.error(bstack11l11l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡤࡸࡹࡧࡣࡩ࡫ࡱ࡫ࠥࡲࡩࡴࡶࡨࡲࡪࡸࠠࡧࡱࡵࠤࢀࢃ࠮ࠡࡇࡵࡶࡴࡸࠠ࠮ࠢࡾࢁࠧ྽").format(bstack11ll1l1ll1_opy_, e))
    pabot.main(args)
  elif bstack1l11lllll_opy_ == bstack11l11l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭྾"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack11111l111_opy_(e, bstack11111lll11_opy_)
    for a in args:
      if bstack11l11l1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜ࠬ྿") in a:
        bstack11l1l111l1_opy_ = int(a.split(bstack11l11l1_opy_ (u"ࠧ࠻ࠩ࿀"))[1])
      if bstack11l11l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ࿁") in a:
        bstack1l1111l1l1_opy_ = str(a.split(bstack11l11l1_opy_ (u"ࠩ࠽ࠫ࿂"))[1])
      if bstack11l11l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕࠪ࿃") in a:
        bstack1l1111lll_opy_ = str(a.split(bstack11l11l1_opy_ (u"ࠫ࠿࠭࿄"))[1])
    bstack1111l11111_opy_ = None
    if bstack11l11l1_opy_ (u"ࠬ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠫ࿅") in args:
      i = args.index(bstack11l11l1_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼ࿆ࠬ"))
      args.pop(i)
      bstack1111l11111_opy_ = args.pop(i)
    if bstack1111l11111_opy_ is not None:
      global bstack1l11111l1l_opy_
      bstack1l11111l1l_opy_ = bstack1111l11111_opy_
    bstack11llll1ll1_opy_(bstack11ll1l11l1_opy_)
    run_cli(args)
    if bstack11l11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫ࿇") in multiprocessing.current_process().__dict__.keys():
      for bstack1l1l111l1l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1111lll1ll_opy_.append(bstack1l1l111l1l_opy_)
  elif bstack1l11lllll_opy_ == bstack11l11l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ࿈"):
    bstack111l1llll_opy_ = bstack1lll1ll1l_opy_(args, logger, CONFIG, bstack1ll11l11ll_opy_)
    bstack111l1llll_opy_.bstack1lll1l1l1_opy_()
    bstack111l1l1lll_opy_()
    bstack1llll1l1l1_opy_ = True
    bstack11l1llll11_opy_ = bstack111l1llll_opy_.bstack1111llll_opy_()
    bstack111l1llll_opy_.bstack1lllll1l1_opy_(bstack1l11llllll_opy_)
    bstack111l1llll_opy_.bstack1lll1l1ll_opy_()
    bstack1llllll111_opy_(bstack1l11lllll_opy_, CONFIG, bstack111l1llll_opy_.bstack111l11ll_opy_())
    bstack1lllllllll_opy_ = bstack111l1llll_opy_.bstack1llll11l1_opy_(bstack1ll1l1llll_opy_, {
      bstack11l11l1_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪ࿉"): bstack1ll1ll111_opy_,
      bstack11l11l1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ࿊"): bstack1l1ll111ll_opy_,
      bstack11l11l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ࿋"): bstack1ll11l11ll_opy_
    })
    try:
      bstack1l1llll11l_opy_, bstack1l1l11111_opy_ = map(list, zip(*bstack1lllllllll_opy_))
      bstack111111ll1_opy_ = bstack1l1llll11l_opy_[0]
      for status_code in bstack1l1l11111_opy_:
        if status_code != 0:
          bstack1ll11l1l11_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11l11l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡤࡺࡪࠦࡥࡳࡴࡲࡶࡸࠦࡡ࡯ࡦࠣࡷࡹࡧࡴࡶࡵࠣࡧࡴࡪࡥ࠯ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡀࠠࡼࡿࠥ࿌").format(str(e)))
  elif bstack1l11lllll_opy_ == bstack11l11l1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭࿍"):
    try:
      from behave.__main__ import main as bstack1l1lllll11_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack11111l111_opy_(e, bstack11ll111ll_opy_)
    bstack111l1l1lll_opy_()
    bstack1llll1l1l1_opy_ = True
    bstack111l1ll1_opy_ = 1
    if bstack11l11l1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ࿎") in CONFIG:
      bstack111l1ll1_opy_ = CONFIG[bstack11l11l1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ࿏")]
    if bstack11l11l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ࿐") in CONFIG:
      bstack1l1lll1lll_opy_ = int(bstack111l1ll1_opy_) * int(len(CONFIG[bstack11l11l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭࿑")]))
    else:
      bstack1l1lll1lll_opy_ = int(bstack111l1ll1_opy_)
    config = Configuration(args)
    bstack1l1l111111_opy_ = config.paths
    if len(bstack1l1l111111_opy_) == 0:
      import glob
      pattern = bstack11l11l1_opy_ (u"ࠫ࠯࠰࠯ࠫ࠰ࡩࡩࡦࡺࡵࡳࡧࠪ࿒")
      bstack1111lllll1_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1111lllll1_opy_)
      config = Configuration(args)
      bstack1l1l111111_opy_ = config.paths
    bstack111l111l_opy_ = [os.path.normpath(item) for item in bstack1l1l111111_opy_]
    bstack11l11l1ll_opy_ = [os.path.normpath(item) for item in args]
    bstack1111l111l1_opy_ = [item for item in bstack11l11l1ll_opy_ if item not in bstack111l111l_opy_]
    import platform as pf
    if pf.system().lower() == bstack11l11l1_opy_ (u"ࠬࡽࡩ࡯ࡦࡲࡻࡸ࠭࿓"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack111l111l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1l111lllll_opy_)))
                    for bstack1l111lllll_opy_ in bstack111l111l_opy_]
    bstack1111ll11_opy_ = []
    for spec in bstack111l111l_opy_:
      bstack11l11111_opy_ = []
      bstack11l11111_opy_ += bstack1111l111l1_opy_
      bstack11l11111_opy_.append(spec)
      bstack1111ll11_opy_.append(bstack11l11111_opy_)
    execution_items = []
    for bstack11l11111_opy_ in bstack1111ll11_opy_:
      if bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ࿔") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack11l11l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿕")]):
          item = {}
          item[bstack11l11l1_opy_ (u"ࠨࡣࡵ࡫ࠬ࿖")] = bstack11l11l1_opy_ (u"ࠩࠣࠫ࿗").join(bstack11l11111_opy_)
          item[bstack11l11l1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ࿘")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack11l11l1_opy_ (u"ࠫࡦࡸࡧࠨ࿙")] = bstack11l11l1_opy_ (u"ࠬࠦࠧ࿚").join(bstack11l11111_opy_)
        item[bstack11l11l1_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ࿛")] = 0
        execution_items.append(item)
    bstack11l1ll1lll_opy_ = bstack1l11111111_opy_(execution_items, bstack1l1lll1lll_opy_)
    for execution_item in bstack11l1ll1lll_opy_:
      bstack1111ll1l_opy_ = []
      for item in execution_item:
        bstack1111ll1l_opy_.append(bstack1l1ll1ll1l_opy_(name=str(item[bstack11l11l1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭࿜")]),
                                             target=bstack11l1l11ll_opy_,
                                             args=(item[bstack11l11l1_opy_ (u"ࠨࡣࡵ࡫ࠬ࿝")],)))
      for t in bstack1111ll1l_opy_:
        t.start()
      for t in bstack1111ll1l_opy_:
        t.join()
  else:
    bstack11l1l1111_opy_(bstack1ll1llll11_opy_)
  if not bstack1llll11lll_opy_:
    bstack1111lll11l_opy_()
    if(bstack1l11lllll_opy_ in [bstack11l11l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ࿞"), bstack11l11l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ࿟")]):
      bstack111l11l1l1_opy_()
  bstack11111l1l1_opy_.bstack111111l1l_opy_()
def browserstack_initialize(bstack11ll1l11ll_opy_=None):
  logger.info(bstack11l11l1_opy_ (u"ࠫࡗࡻ࡮࡯࡫ࡱ࡫࡙ࠥࡄࡌࠢࡺ࡭ࡹ࡮ࠠࡢࡴࡪࡷ࠿ࠦࠧ࿠") + str(bstack11ll1l11ll_opy_))
  run_on_browserstack(bstack11ll1l11ll_opy_, None, True)
@measure(event_name=EVENTS.bstack11ll11ll1l_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack1111lll11l_opy_():
  global CONFIG
  global bstack111l11l11_opy_
  global bstack1ll11l1l11_opy_
  global bstack111ll1ll1_opy_
  global bstack11111111_opy_
  bstack11l11l1lll_opy_.bstack1lll1lll11_opy_()
  if cli.is_running():
    bstack1111ll1ll1_opy_.invoke(Events.bstack11l11ll1l_opy_)
  else:
    bstack111lll1l_opy_ = bstack1lll11ll1_opy_.bstack1llll1ll1_opy_(config=CONFIG)
    bstack111lll1l_opy_.bstack11l1l111l_opy_(CONFIG)
  if bstack111l11l11_opy_ == bstack11l11l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ࿡"):
    if not cli.is_enabled(CONFIG):
      bstack1l11l111_opy_.stop()
  else:
    bstack1l11l111_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1ll1l1l1_opy_.bstack11lllll1l1_opy_()
  if bstack11l11l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ࿢") in CONFIG and str(CONFIG[bstack11l11l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ࿣")]).lower() != bstack11l11l1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ࿤"):
    hashed_id, bstack1111ll11l1_opy_ = bstack1l1111111_opy_()
  else:
    hashed_id, bstack1111ll11l1_opy_ = get_build_link()
  bstack11lll11111_opy_(hashed_id)
  logger.info(bstack11l11l1_opy_ (u"ࠩࡖࡈࡐࠦࡲࡶࡰࠣࡩࡳࡪࡥࡥࠢࡩࡳࡷࠦࡩࡥ࠼ࠪ࿥") + bstack11111111_opy_.get_property(bstack11l11l1_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ࿦"), bstack11l11l1_opy_ (u"ࠫࠬ࿧")) + bstack11l11l1_opy_ (u"ࠬ࠲ࠠࡵࡧࡶࡸ࡭ࡻࡢࠡ࡫ࡧ࠾ࠥ࠭࿨") + os.getenv(bstack11l11l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ࿩"), bstack11l11l1_opy_ (u"ࠧࠨ࿪")))
  if hashed_id is not None and bstack1l1l111ll_opy_() != -1:
    sessions = bstack1ll11ll1l1_opy_(hashed_id)
    bstack111ll1lll_opy_(sessions, bstack1111ll11l1_opy_)
  if bstack111l11l11_opy_ == bstack11l11l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ࿫") and bstack1ll11l1l11_opy_ != 0:
    sys.exit(bstack1ll11l1l11_opy_)
  if bstack111l11l11_opy_ == bstack11l11l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ࿬") and bstack111ll1ll1_opy_ != 0:
    sys.exit(bstack111ll1ll1_opy_)
def bstack11lll11111_opy_(new_id):
    global bstack1111l1111_opy_
    bstack1111l1111_opy_ = new_id
def bstack11l1l1l1ll_opy_(bstack1llllll1ll_opy_):
  if bstack1llllll1ll_opy_:
    return bstack1llllll1ll_opy_.capitalize()
  else:
    return bstack11l11l1_opy_ (u"ࠪࠫ࿭")
@measure(event_name=EVENTS.bstack1ll11111ll_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack1lll11111l_opy_(bstack1111l1l1l_opy_):
  if bstack11l11l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ࿮") in bstack1111l1l1l_opy_ and bstack1111l1l1l_opy_[bstack11l11l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ࿯")] != bstack11l11l1_opy_ (u"࠭ࠧ࿰"):
    return bstack1111l1l1l_opy_[bstack11l11l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ࿱")]
  else:
    bstack111ll1l1ll_opy_ = bstack11l11l1_opy_ (u"ࠣࠤ࿲")
    if bstack11l11l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ࿳") in bstack1111l1l1l_opy_ and bstack1111l1l1l_opy_[bstack11l11l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ࿴")] != None:
      bstack111ll1l1ll_opy_ += bstack1111l1l1l_opy_[bstack11l11l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ࿵")] + bstack11l11l1_opy_ (u"ࠧ࠲ࠠࠣ࿶")
      if bstack1111l1l1l_opy_[bstack11l11l1_opy_ (u"࠭࡯ࡴࠩ࿷")] == bstack11l11l1_opy_ (u"ࠢࡪࡱࡶࠦ࿸"):
        bstack111ll1l1ll_opy_ += bstack11l11l1_opy_ (u"ࠣ࡫ࡒࡗࠥࠨ࿹")
      bstack111ll1l1ll_opy_ += (bstack1111l1l1l_opy_[bstack11l11l1_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭࿺")] or bstack11l11l1_opy_ (u"ࠪࠫ࿻"))
      return bstack111ll1l1ll_opy_
    else:
      bstack111ll1l1ll_opy_ += bstack11l1l1l1ll_opy_(bstack1111l1l1l_opy_[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬ࿼")]) + bstack11l11l1_opy_ (u"ࠧࠦࠢ࿽") + (
              bstack1111l1l1l_opy_[bstack11l11l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ࿾")] or bstack11l11l1_opy_ (u"ࠧࠨ࿿")) + bstack11l11l1_opy_ (u"ࠣ࠮ࠣࠦက")
      if bstack1111l1l1l_opy_[bstack11l11l1_opy_ (u"ࠩࡲࡷࠬခ")] == bstack11l11l1_opy_ (u"࡛ࠥ࡮ࡴࡤࡰࡹࡶࠦဂ"):
        bstack111ll1l1ll_opy_ += bstack11l11l1_opy_ (u"ࠦ࡜࡯࡮ࠡࠤဃ")
      bstack111ll1l1ll_opy_ += bstack1111l1l1l_opy_[bstack11l11l1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩင")] or bstack11l11l1_opy_ (u"࠭ࠧစ")
      return bstack111ll1l1ll_opy_
@measure(event_name=EVENTS.bstack1l1l111l11_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack1l11ll1ll_opy_(bstack11ll11lll_opy_):
  if bstack11ll11lll_opy_ == bstack11l11l1_opy_ (u"ࠢࡥࡱࡱࡩࠧဆ"):
    return bstack11l11l1_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽࡫ࡷ࡫ࡥ࡯࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥ࡫ࡷ࡫ࡥ࡯ࠤࡁࡇࡴࡳࡰ࡭ࡧࡷࡩࡩࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫဇ")
  elif bstack11ll11lll_opy_ == bstack11l11l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤဈ"):
    return bstack11l11l1_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡸࡥࡥ࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡶࡪࡪࠢ࠿ࡈࡤ࡭ࡱ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ဉ")
  elif bstack11ll11lll_opy_ == bstack11l11l1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦည"):
    return bstack11l11l1_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡨࡴࡨࡩࡳࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡨࡴࡨࡩࡳࠨ࠾ࡑࡣࡶࡷࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬဋ")
  elif bstack11ll11lll_opy_ == bstack11l11l1_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧဌ"):
    return bstack11l11l1_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡵࡩࡩࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡳࡧࡧࠦࡃࡋࡲࡳࡱࡵࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩဍ")
  elif bstack11ll11lll_opy_ == bstack11l11l1_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࠤဎ"):
    return bstack11l11l1_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࠨ࡫ࡥࡢ࠵࠵࠺ࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࠣࡦࡧࡤ࠷࠷࠼ࠢ࠿ࡖ࡬ࡱࡪࡵࡵࡵ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧဏ")
  elif bstack11ll11lll_opy_ == bstack11l11l1_opy_ (u"ࠥࡶࡺࡴ࡮ࡪࡰࡪࠦတ"):
    return bstack11l11l1_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡢ࡭ࡣࡦ࡯ࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡢ࡭ࡣࡦ࡯ࠧࡄࡒࡶࡰࡱ࡭ࡳ࡭࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬထ")
  else:
    return bstack11l11l1_opy_ (u"ࠬࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡤ࡯ࡥࡨࡱ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡤ࡯ࡥࡨࡱࠢ࠿ࠩဒ") + bstack11l1l1l1ll_opy_(
      bstack11ll11lll_opy_) + bstack11l11l1_opy_ (u"࠭࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬဓ")
def bstack1l111lll1_opy_(session):
  return bstack11l11l1_opy_ (u"ࠧ࠽ࡶࡵࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡷࡵࡷࠣࡀ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠲ࡴࡡ࡮ࡧࠥࡂࡁࡧࠠࡩࡴࡨࡪࡂࠨࡻࡾࠤࠣࡸࡦࡸࡧࡦࡶࡀࠦࡤࡨ࡬ࡢࡰ࡮ࠦࡃࢁࡽ࠽࠱ࡤࡂࡁ࠵ࡴࡥࡀࡾࢁࢀࢃ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾࠲ࡸࡷࡄࠧန").format(
    session[bstack11l11l1_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣࡠࡷࡵࡰࠬပ")], bstack1lll11111l_opy_(session), bstack1l11ll1ll_opy_(session[bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡷࡥࡹࡻࡳࠨဖ")]),
    bstack1l11ll1ll_opy_(session[bstack11l11l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪဗ")]),
    bstack11l1l1l1ll_opy_(session[bstack11l11l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬဘ")] or session[bstack11l11l1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬမ")] or bstack11l11l1_opy_ (u"࠭ࠧယ")) + bstack11l11l1_opy_ (u"ࠢࠡࠤရ") + (session[bstack11l11l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪလ")] or bstack11l11l1_opy_ (u"ࠩࠪဝ")),
    session[bstack11l11l1_opy_ (u"ࠪࡳࡸ࠭သ")] + bstack11l11l1_opy_ (u"ࠦࠥࠨဟ") + session[bstack11l11l1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩဠ")], session[bstack11l11l1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨအ")] or bstack11l11l1_opy_ (u"ࠧࠨဢ"),
    session[bstack11l11l1_opy_ (u"ࠨࡥࡵࡩࡦࡺࡥࡥࡡࡤࡸࠬဣ")] if session[bstack11l11l1_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭ဤ")] else bstack11l11l1_opy_ (u"ࠪࠫဥ"))
@measure(event_name=EVENTS.bstack11l1lll111_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def bstack111ll1lll_opy_(sessions, bstack1111ll11l1_opy_):
  try:
    bstack11lllll11l_opy_ = bstack11l11l1_opy_ (u"ࠦࠧဦ")
    if not os.path.exists(bstack1lll11ll11_opy_):
      os.mkdir(bstack1lll11ll11_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l11l1_opy_ (u"ࠬࡧࡳࡴࡧࡷࡷ࠴ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪဧ")), bstack11l11l1_opy_ (u"࠭ࡲࠨဨ")) as f:
      bstack11lllll11l_opy_ = f.read()
    bstack11lllll11l_opy_ = bstack11lllll11l_opy_.replace(bstack11l11l1_opy_ (u"ࠧࡼࠧࡕࡉࡘ࡛ࡌࡕࡕࡢࡇࡔ࡛ࡎࡕࠧࢀࠫဩ"), str(len(sessions)))
    bstack11lllll11l_opy_ = bstack11lllll11l_opy_.replace(bstack11l11l1_opy_ (u"ࠨࡽࠨࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠫࡽࠨဪ"), bstack1111ll11l1_opy_)
    bstack11lllll11l_opy_ = bstack11lllll11l_opy_.replace(bstack11l11l1_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢࡒࡆࡓࡅࠦࡿࠪါ"),
                                              sessions[0].get(bstack11l11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡥࡲ࡫ࠧာ")) if sessions[0] else bstack11l11l1_opy_ (u"ࠫࠬိ"))
    with open(os.path.join(bstack1lll11ll11_opy_, bstack11l11l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡷ࡫ࡰࡰࡴࡷ࠲࡭ࡺ࡭࡭ࠩီ")), bstack11l11l1_opy_ (u"࠭ࡷࠨု")) as stream:
      stream.write(bstack11lllll11l_opy_.split(bstack11l11l1_opy_ (u"ࠧࡼࠧࡖࡉࡘ࡙ࡉࡐࡐࡖࡣࡉࡇࡔࡂࠧࢀࠫူ"))[0])
      for session in sessions:
        stream.write(bstack1l111lll1_opy_(session))
      stream.write(bstack11lllll11l_opy_.split(bstack11l11l1_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁࠬေ"))[1])
    logger.info(bstack11l11l1_opy_ (u"ࠩࡊࡩࡳ࡫ࡲࡢࡶࡨࡨࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡧࡻࡩ࡭ࡦࠣࡥࡷࡺࡩࡧࡣࡦࡸࡸࠦࡡࡵࠢࡾࢁࠬဲ").format(bstack1lll11ll11_opy_));
  except Exception as e:
    logger.debug(bstack11l1l1ll1l_opy_.format(str(e)))
def bstack1ll11ll1l1_opy_(hashed_id):
  global CONFIG
  try:
    bstack1l11lll1ll_opy_ = datetime.datetime.now()
    host = bstack11l11l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪဳ") if bstack11l11l1_opy_ (u"ࠫࡦࡶࡰࠨဴ") in CONFIG else bstack11l11l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ဵ")
    user = CONFIG[bstack11l11l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨံ")]
    key = CONFIG[bstack11l11l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻ့ࠪ")]
    bstack1l11111ll_opy_ = bstack11l11l1_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧး") if bstack11l11l1_opy_ (u"ࠩࡤࡴࡵ္࠭") in CONFIG else (bstack11l11l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫်ࠧ") if CONFIG.get(bstack11l11l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨျ")) else bstack11l11l1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧြ"))
    host = bstack11l1lll1l_opy_(cli.config, [bstack11l11l1_opy_ (u"ࠨࡡࡱ࡫ࡶࠦွ"), bstack11l11l1_opy_ (u"ࠢࡢࡲࡳࡅࡺࡺ࡯࡮ࡣࡷࡩࠧှ"), bstack11l11l1_opy_ (u"ࠣࡣࡳ࡭ࠧဿ")], host) if bstack11l11l1_opy_ (u"ࠩࡤࡴࡵ࠭၀") in CONFIG else bstack11l1lll1l_opy_(cli.config, [bstack11l11l1_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ၁"), bstack11l11l1_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ၂"), bstack11l11l1_opy_ (u"ࠧࡧࡰࡪࠤ၃")], host)
    url = bstack11l11l1_opy_ (u"࠭ࡻࡾ࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡵࡨࡷࡸ࡯࡯࡯ࡵ࠱࡮ࡸࡵ࡮ࠨ၄").format(host, bstack1l11111ll_opy_, hashed_id)
    headers = {
      bstack11l11l1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭၅"): bstack11l11l1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ၆"),
    }
    proxies = bstack11l1ll111_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack111lll1ll_opy_(bstack11l11l1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡨࡧࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࡥ࡬ࡪࡵࡷࠦ၇"), datetime.datetime.now() - bstack1l11lll1ll_opy_)
      return list(map(lambda session: session[bstack11l11l1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ၈")], response.json()))
  except Exception as e:
    logger.debug(bstack1ll11l111_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack1l11ll1l1_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def get_build_link():
  global CONFIG
  global bstack1111l1111_opy_
  try:
    if bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ၉") in CONFIG:
      bstack1l11lll1ll_opy_ = datetime.datetime.now()
      host = bstack11l11l1_opy_ (u"ࠬࡧࡰࡪ࠯ࡦࡰࡴࡻࡤࠨ၊") if bstack11l11l1_opy_ (u"࠭ࡡࡱࡲࠪ။") in CONFIG else bstack11l11l1_opy_ (u"ࠧࡢࡲ࡬ࠫ၌")
      user = CONFIG[bstack11l11l1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ၍")]
      key = CONFIG[bstack11l11l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ၎")]
      bstack1l11111ll_opy_ = bstack11l11l1_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩ၏") if bstack11l11l1_opy_ (u"ࠫࡦࡶࡰࠨၐ") in CONFIG else bstack11l11l1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧၑ")
      url = bstack11l11l1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡼࡿ࠽ࡿࢂࡆࡻࡾ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠯࡬ࡶࡳࡳ࠭ၒ").format(user, key, host, bstack1l11111ll_opy_)
      if cli.is_enabled(CONFIG):
        bstack1111ll11l1_opy_, hashed_id = cli.bstack1l1ll1l1ll_opy_()
        logger.info(bstack1l1l11lll_opy_.format(bstack1111ll11l1_opy_))
        return [hashed_id, bstack1111ll11l1_opy_]
      else:
        headers = {
          bstack11l11l1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭ၓ"): bstack11l11l1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫၔ"),
        }
        if bstack11l11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫၕ") in CONFIG:
          params = {bstack11l11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨၖ"): CONFIG[bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧၗ")], bstack11l11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨၘ"): CONFIG[bstack11l11l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨၙ")]}
        else:
          params = {bstack11l11l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬၚ"): CONFIG[bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫၛ")]}
        proxies = bstack11l1ll111_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack1llll11111_opy_ = response.json()[0][bstack11l11l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡢࡶ࡫࡯ࡨࠬၜ")]
          if bstack1llll11111_opy_:
            bstack1111ll11l1_opy_ = bstack1llll11111_opy_[bstack11l11l1_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧၝ")].split(bstack11l11l1_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦ࠱ࡧࡻࡩ࡭ࡦࠪၞ"))[0] + bstack11l11l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡷ࠴࠭ၟ") + bstack1llll11111_opy_[
              bstack11l11l1_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩၠ")]
            logger.info(bstack1l1l11lll_opy_.format(bstack1111ll11l1_opy_))
            bstack1111l1111_opy_ = bstack1llll11111_opy_[bstack11l11l1_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪၡ")]
            bstack1lll11l1ll_opy_ = CONFIG[bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫၢ")]
            if bstack11l11l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫၣ") in CONFIG:
              bstack1lll11l1ll_opy_ += bstack11l11l1_opy_ (u"ࠪࠤࠬၤ") + CONFIG[bstack11l11l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ၥ")]
            if bstack1lll11l1ll_opy_ != bstack1llll11111_opy_[bstack11l11l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪၦ")]:
              logger.debug(bstack1ll11lll1_opy_.format(bstack1llll11111_opy_[bstack11l11l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫၧ")], bstack1lll11l1ll_opy_))
            cli.bstack111lll1ll_opy_(bstack11l11l1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࡭ࡥࡵࡡࡥࡹ࡮ࡲࡤࡠ࡮࡬ࡲࡰࠨၨ"), datetime.datetime.now() - bstack1l11lll1ll_opy_)
            return [bstack1llll11111_opy_[bstack11l11l1_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫၩ")], bstack1111ll11l1_opy_]
    else:
      logger.warn(bstack1ll11l1l1l_opy_)
  except Exception as e:
    logger.debug(bstack1l1ll11l11_opy_.format(str(e)))
  return [None, None]
def bstack1l1l11llll_opy_(url, bstack1lll1l11ll_opy_=False):
  global CONFIG
  global bstack1111l1ll11_opy_
  if not bstack1111l1ll11_opy_:
    hostname = bstack11llllll11_opy_(url)
    is_private = bstack11l1l1l111_opy_(hostname)
    if (bstack11l11l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ၪ") in CONFIG and not bstack111lll11l1_opy_(CONFIG[bstack11l11l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧၫ")])) and (is_private or bstack1lll1l11ll_opy_):
      bstack1111l1ll11_opy_ = hostname
def bstack11llllll11_opy_(url):
  return urlparse(url).hostname
def bstack11l1l1l111_opy_(hostname):
  for bstack1ll1llll1l_opy_ in bstack1111l1111l_opy_:
    regex = re.compile(bstack1ll1llll1l_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1l1lll1ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1l1llll11_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack11l1l111l1_opy_
  bstack1ll1l11lll_opy_ = not (bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၬ"), None) and bstack1ll11l1l_opy_(
          threading.current_thread(), bstack11l11l1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၭ"), None))
  bstack1ll1llllll_opy_ = getattr(driver, bstack11l11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ၮ"), None) != True
  bstack11111l1l11_opy_ = bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၯ"), None) and bstack1ll11l1l_opy_(
          threading.current_thread(), bstack11l11l1_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၰ"), None)
  if bstack11111l1l11_opy_:
    if not bstack1l111l111l_opy_():
      logger.warning(bstack11l11l1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷ࠳ࠨၱ"))
      return {}
    logger.debug(bstack11l11l1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧၲ"))
    logger.debug(perform_scan(driver, driver_command=bstack11l11l1_opy_ (u"ࠫࡪࡾࡥࡤࡷࡷࡩࡘࡩࡲࡪࡲࡷࠫၳ")))
    results = bstack1llll1l11l_opy_(bstack11l11l1_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸࡸࠨၴ"))
    if results is not None and results.get(bstack11l11l1_opy_ (u"ࠨࡩࡴࡵࡸࡩࡸࠨၵ")) is not None:
        return results[bstack11l11l1_opy_ (u"ࠢࡪࡵࡶࡹࡪࡹࠢၶ")]
    logger.error(bstack11l11l1_opy_ (u"ࠣࡐࡲࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡗ࡫ࡳࡶ࡮ࡷࡷࠥࡽࡥࡳࡧࠣࡪࡴࡻ࡮ࡥ࠰ࠥၷ"))
    return []
  if not bstack111llll1_opy_.bstack1l1l1llll_opy_(CONFIG, bstack11l1l111l1_opy_) or (bstack1ll1llllll_opy_ and bstack1ll1l11lll_opy_):
    logger.warning(bstack11l11l1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶ࠲ࠧၸ"))
    return {}
  try:
    logger.debug(bstack11l11l1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧၹ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1lllll111l_opy_.bstack1l1l1lll1_opy_)
    return results
  except Exception:
    logger.error(bstack11l11l1_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡹࡨࡶࡪࠦࡦࡰࡷࡱࡨ࠳ࠨၺ"))
    return {}
@measure(event_name=EVENTS.bstack111l1llll1_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack11l1l111l1_opy_
  bstack1ll1l11lll_opy_ = not (bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၻ"), None) and bstack1ll11l1l_opy_(
          threading.current_thread(), bstack11l11l1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၼ"), None))
  bstack1ll1llllll_opy_ = getattr(driver, bstack11l11l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧၽ"), None) != True
  bstack11111l1l11_opy_ = bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၾ"), None) and bstack1ll11l1l_opy_(
          threading.current_thread(), bstack11l11l1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၿ"), None)
  if bstack11111l1l11_opy_:
    if not bstack1l111l111l_opy_():
      logger.warning(bstack11l11l1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡳࡶ࡯ࡰࡥࡷࡿ࠮ࠣႀ"))
      return {}
    logger.debug(bstack11l11l1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺࠩႁ"))
    logger.debug(perform_scan(driver, driver_command=bstack11l11l1_opy_ (u"ࠬ࡫ࡸࡦࡥࡸࡸࡪ࡙ࡣࡳ࡫ࡳࡸࠬႂ")))
    results = bstack1llll1l11l_opy_(bstack11l11l1_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡙ࡵ࡮࡯ࡤࡶࡾࠨႃ"))
    if results is not None and results.get(bstack11l11l1_opy_ (u"ࠢࡴࡷࡰࡱࡦࡸࡹࠣႄ")) is not None:
        return results[bstack11l11l1_opy_ (u"ࠣࡵࡸࡱࡲࡧࡲࡺࠤႅ")]
    logger.error(bstack11l11l1_opy_ (u"ࠤࡑࡳࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡘࡥࡴࡷ࡯ࡸࡸࠦࡓࡶ࡯ࡰࡥࡷࡿࠠࡸࡣࡶࠤ࡫ࡵࡵ࡯ࡦ࠱ࠦႆ"))
    return {}
  if not bstack111llll1_opy_.bstack1l1l1llll_opy_(CONFIG, bstack11l1l111l1_opy_) or (bstack1ll1llllll_opy_ and bstack1ll1l11lll_opy_):
    logger.warning(bstack11l11l1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠴ࠢႇ"))
    return {}
  try:
    logger.debug(bstack11l11l1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺࠩႈ"))
    logger.debug(perform_scan(driver))
    bstack11ll11l11_opy_ = driver.execute_async_script(bstack1lllll111l_opy_.bstack111ll11lll_opy_)
    return bstack11ll11l11_opy_
  except Exception:
    logger.error(bstack11l11l1_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡸࡱࡲࡧࡲࡺࠢࡺࡥࡸࠦࡦࡰࡷࡱࡨ࠳ࠨႉ"))
    return {}
def bstack1l111l111l_opy_():
  global CONFIG
  global bstack11l1l111l1_opy_
  bstack111lll1l1l_opy_ = bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ႊ"), None) and bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩႋ"), None)
  if not bstack111llll1_opy_.bstack1l1l1llll_opy_(CONFIG, bstack11l1l111l1_opy_) or not bstack111lll1l1l_opy_:
        logger.warning(bstack11l11l1_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡲࡦࡵࡸࡰࡹࡹ࠮ࠣႌ"))
        return False
  return True
def bstack1llll1l11l_opy_(bstack11lll1l111_opy_):
    bstack11ll11lll1_opy_ = bstack1l11l111_opy_.current_test_uuid() if bstack1l11l111_opy_.current_test_uuid() else bstack1ll1l1l1_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack111111llll_opy_(bstack11ll11lll1_opy_, bstack11lll1l111_opy_))
        try:
            return future.result(timeout=bstack111ll1l11l_opy_)
        except TimeoutError:
            logger.error(bstack11l11l1_opy_ (u"ࠤࡗ࡭ࡲ࡫࡯ࡶࡶࠣࡥ࡫ࡺࡥࡳࠢࡾࢁࡸࠦࡷࡩ࡫࡯ࡩࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡓࡧࡶࡹࡱࡺࡳႍࠣ").format(bstack111ll1l11l_opy_))
        except Exception as ex:
            logger.debug(bstack11l11l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡵࡩࡹࡸࡩࡦࡸ࡬ࡲ࡬ࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡼࡿ࠱ࠤࡊࡸࡲࡰࡴࠣ࠱ࠥࢁࡽࠣႎ").format(bstack11lll1l111_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack11l1111l11_opy_, stage=STAGE.bstack1ll1lllll_opy_, bstack111ll1l1ll_opy_=bstack111ll11111_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack11l1l111l1_opy_
  bstack1ll1l11lll_opy_ = not (bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨႏ"), None) and bstack1ll11l1l_opy_(
          threading.current_thread(), bstack11l11l1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ႐"), None))
  bstack11llll1111_opy_ = not (bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭႑"), None) and bstack1ll11l1l_opy_(
          threading.current_thread(), bstack11l11l1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ႒"), None))
  bstack1ll1llllll_opy_ = getattr(driver, bstack11l11l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ႓"), None) != True
  if not bstack111llll1_opy_.bstack1l1l1llll_opy_(CONFIG, bstack11l1l111l1_opy_) or (bstack1ll1llllll_opy_ and bstack1ll1l11lll_opy_ and bstack11llll1111_opy_):
    logger.warning(bstack11l11l1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡸࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡣࡢࡰ࠱ࠦ႔"))
    return {}
  try:
    bstack1111ll111_opy_ = bstack11l11l1_opy_ (u"ࠪࡥࡵࡶࠧ႕") in CONFIG and CONFIG.get(bstack11l11l1_opy_ (u"ࠫࡦࡶࡰࠨ႖"), bstack11l11l1_opy_ (u"ࠬ࠭႗"))
    session_id = getattr(driver, bstack11l11l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠪ႘"), None)
    if not session_id:
      logger.warning(bstack11l11l1_opy_ (u"ࠢࡏࡱࠣࡷࡪࡹࡳࡪࡱࡱࠤࡎࡊࠠࡧࡱࡸࡲࡩࠦࡦࡰࡴࠣࡨࡷ࡯ࡶࡦࡴࠥ႙"))
      return {bstack11l11l1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢႚ"): bstack11l11l1_opy_ (u"ࠤࡑࡳࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࠢࡩࡳࡺࡴࡤࠣႛ")}
    if bstack1111ll111_opy_:
      try:
        bstack1ll1ll1l1l_opy_ = {
              bstack11l11l1_opy_ (u"ࠪࡸ࡭ࡐࡷࡵࡖࡲ࡯ࡪࡴࠧႜ"): os.environ.get(bstack11l11l1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩႝ"), os.environ.get(bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ႞"), bstack11l11l1_opy_ (u"࠭ࠧ႟"))),
              bstack11l11l1_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧႠ"): bstack1l11l111_opy_.current_test_uuid() if bstack1l11l111_opy_.current_test_uuid() else bstack1ll1l1l1_opy_.current_hook_uuid(),
              bstack11l11l1_opy_ (u"ࠨࡣࡸࡸ࡭ࡎࡥࡢࡦࡨࡶࠬႡ"): os.environ.get(bstack11l11l1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧႢ")),
              bstack11l11l1_opy_ (u"ࠪࡷࡨࡧ࡮ࡕ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪႣ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack11l11l1_opy_ (u"ࠫࡹ࡮ࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩႤ"): os.environ.get(bstack11l11l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪႥ"), bstack11l11l1_opy_ (u"࠭ࠧႦ")),
              bstack11l11l1_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪࠧႧ"): kwargs.get(bstack11l11l1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠࡥࡲࡱࡲࡧ࡮ࡥࠩႨ"), None) or bstack11l11l1_opy_ (u"ࠩࠪႩ")
          }
        if not hasattr(thread_local, bstack11l11l1_opy_ (u"ࠪࡦࡦࡹࡥࡠࡣࡳࡴࡤࡧ࠱࠲ࡻࡢࡷࡨࡸࡩࡱࡶࠪႪ")):
            scripts = {bstack11l11l1_opy_ (u"ࠫࡸࡩࡡ࡯ࠩႫ"): bstack1lllll111l_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack11111l1l1l_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack11111l1l1l_opy_[bstack11l11l1_opy_ (u"ࠬࡹࡣࡢࡰࠪႬ")] = bstack11111l1l1l_opy_[bstack11l11l1_opy_ (u"࠭ࡳࡤࡣࡱࠫႭ")] % json.dumps(bstack1ll1ll1l1l_opy_)
        bstack1lllll111l_opy_.bstack1ll111ll1_opy_(bstack11111l1l1l_opy_)
        bstack1lllll111l_opy_.store()
        bstack1l111ll111_opy_ = driver.execute_script(bstack1lllll111l_opy_.perform_scan)
      except Exception as bstack1ll11ll11_opy_:
        logger.info(bstack11l11l1_opy_ (u"ࠢࡂࡲࡳ࡭ࡺࡳࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࠢႮ") + str(bstack1ll11ll11_opy_))
        bstack1l111ll111_opy_ = {bstack11l11l1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢႯ"): str(bstack1ll11ll11_opy_)}
    else:
      bstack1l111ll111_opy_ = driver.execute_async_script(bstack1lllll111l_opy_.perform_scan, {bstack11l11l1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࠩႰ"): kwargs.get(bstack11l11l1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢࡧࡴࡳ࡭ࡢࡰࡧࠫႱ"), None) or bstack11l11l1_opy_ (u"ࠫࠬႲ")})
    return bstack1l111ll111_opy_
  except Exception as err:
    logger.error(bstack11l11l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡴࡸࡲࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡣࡢࡰ࠱ࠤࢀࢃࠢႳ").format(str(err)))
    return {}