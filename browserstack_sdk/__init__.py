# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
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
from browserstack_sdk.bstack1l11ll11l1_opy_ import bstack11l1111l11_opy_
from browserstack_sdk.bstack1lll11lll_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack11l11l111_opy_():
  global CONFIG
  headers = {
        bstack11l1l11_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧৼ"): bstack11l1l11_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ৽"),
      }
  proxies = bstack1l1l1l1111_opy_(CONFIG, bstack1l1l11l1l_opy_)
  try:
    response = requests.get(bstack1l1l11l1l_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1llllllll1_opy_ = response.json()[bstack11l1l11_opy_ (u"ࠪ࡬ࡺࡨࡳࠨ৾")]
      logger.debug(bstack1l111l1ll1_opy_.format(response.json()))
      return bstack1llllllll1_opy_
    else:
      logger.debug(bstack11lll111l1_opy_.format(bstack11l1l11_opy_ (u"ࠦࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡊࡔࡑࡑࠤࡵࡧࡲࡴࡧࠣࡩࡷࡸ࡯ࡳࠢࠥ৿")))
  except Exception as e:
    logger.debug(bstack11lll111l1_opy_.format(e))
def bstack1l1lll111_opy_(hub_url):
  global CONFIG
  url = bstack11l1l11_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢ਀")+  hub_url + bstack11l1l11_opy_ (u"ࠨ࠯ࡤࡪࡨࡧࡰࠨਁ")
  headers = {
        bstack11l1l11_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭ਂ"): bstack11l1l11_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫਃ"),
      }
  proxies = bstack1l1l1l1111_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1l1l1111l1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1l111l1lll_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack1l111lllll_opy_, stage=STAGE.bstack11l1lllll_opy_)
def bstack1l11l1lll1_opy_():
  try:
    global bstack1ll1l11l1l_opy_
    bstack1llllllll1_opy_ = bstack11l11l111_opy_()
    bstack1ll11ll1l_opy_ = []
    results = []
    for bstack1l11l11ll1_opy_ in bstack1llllllll1_opy_:
      bstack1ll11ll1l_opy_.append(bstack1l11l1l11_opy_(target=bstack1l1lll111_opy_,args=(bstack1l11l11ll1_opy_,)))
    for t in bstack1ll11ll1l_opy_:
      t.start()
    for t in bstack1ll11ll1l_opy_:
      results.append(t.join())
    bstack1l11111111_opy_ = {}
    for item in results:
      hub_url = item[bstack11l1l11_opy_ (u"ࠩ࡫ࡹࡧࡥࡵࡳ࡮ࠪ਄")]
      latency = item[bstack11l1l11_opy_ (u"ࠪࡰࡦࡺࡥ࡯ࡥࡼࠫਅ")]
      bstack1l11111111_opy_[hub_url] = latency
    bstack11l111l1l_opy_ = min(bstack1l11111111_opy_, key= lambda x: bstack1l11111111_opy_[x])
    bstack1ll1l11l1l_opy_ = bstack11l111l1l_opy_
    logger.debug(bstack1111l11lll_opy_.format(bstack11l111l1l_opy_))
  except Exception as e:
    logger.debug(bstack11llll111l_opy_.format(e))
from browserstack_sdk.bstack111llll1_opy_ import *
from browserstack_sdk.bstack1llllllll_opy_ import *
from browserstack_sdk.bstack11ll1l11_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack1ll1111ll_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack11l1ll1111_opy_, stage=STAGE.bstack11l1lllll_opy_)
def bstack111l1lll11_opy_():
    global bstack1ll1l11l1l_opy_
    try:
        bstack1111ll1l1_opy_ = bstack1l1l11ll11_opy_()
        bstack1l1lll1lll_opy_(bstack1111ll1l1_opy_)
        hub_url = bstack1111ll1l1_opy_.get(bstack11l1l11_opy_ (u"ࠦࡺࡸ࡬ࠣਆ"), bstack11l1l11_opy_ (u"ࠧࠨਇ"))
        if hub_url.endswith(bstack11l1l11_opy_ (u"࠭࠯ࡸࡦ࠲࡬ࡺࡨࠧਈ")):
            hub_url = hub_url.rsplit(bstack11l1l11_opy_ (u"ࠧ࠰ࡹࡧ࠳࡭ࡻࡢࠨਉ"), 1)[0]
        if hub_url.startswith(bstack11l1l11_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࠩਊ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack11l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠫ਋")):
            hub_url = hub_url[8:]
        bstack1ll1l11l1l_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1l1l11ll11_opy_():
    global CONFIG
    bstack11111l1lll_opy_ = CONFIG.get(bstack11l1l11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ਌"), {}).get(bstack11l1l11_opy_ (u"ࠫ࡬ࡸࡩࡥࡐࡤࡱࡪ࠭਍"), bstack11l1l11_opy_ (u"ࠬࡔࡏࡠࡉࡕࡍࡉࡥࡎࡂࡏࡈࡣࡕࡇࡓࡔࡇࡇࠫ਎"))
    if not isinstance(bstack11111l1lll_opy_, str):
        raise ValueError(bstack11l1l11_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡍࡲࡪࡦࠣࡲࡦࡳࡥࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡤࠤࡻࡧ࡬ࡪࡦࠣࡷࡹࡸࡩ࡯ࡩࠥਏ"))
    try:
        bstack1111ll1l1_opy_ = bstack111l11ll1_opy_(bstack11111l1lll_opy_)
        return bstack1111ll1l1_opy_
    except Exception as e:
        logger.error(bstack11l1l11_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳࠡ࠼ࠣࡿࢂࠨਐ").format(str(e)))
        return {}
def bstack111l11ll1_opy_(bstack11111l1lll_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack11l1l11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ਑")] or not CONFIG[bstack11l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ਒")]:
            raise ValueError(bstack11l1l11_opy_ (u"ࠥࡑ࡮ࡹࡳࡪࡰࡪࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠥࡵࡲࠡࡣࡦࡧࡪࡹࡳࠡ࡭ࡨࡽࠧਓ"))
        url = bstack11ll111l1_opy_ + bstack11111l1lll_opy_
        auth = (CONFIG[bstack11l1l11_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ਔ")], CONFIG[bstack11l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨਕ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1l1l1lll1_opy_ = json.loads(response.text)
            return bstack1l1l1lll1_opy_
    except ValueError as ve:
        logger.error(bstack11l1l11_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳࠡ࠼ࠣࡿࢂࠨਖ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack11l1l11_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢਗ").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1l1lll1lll_opy_(bstack1ll11lll11_opy_):
    global CONFIG
    if bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬਘ") not in CONFIG or str(CONFIG[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ਙ")]).lower() == bstack11l1l11_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩਚ"):
        CONFIG[bstack11l1l11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪਛ")] = False
    elif bstack11l1l11_opy_ (u"ࠬ࡯ࡳࡕࡴ࡬ࡥࡱࡍࡲࡪࡦࠪਜ") in bstack1ll11lll11_opy_:
        bstack1ll1111111_opy_ = CONFIG.get(bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪਝ"), {})
        logger.debug(bstack11l1l11_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡹ࡫ࡶࡸ࡮ࡴࡧࠡ࡮ࡲࡧࡦࡲࠠࡰࡲࡷ࡭ࡴࡴࡳ࠻ࠢࠨࡷࠧਞ"), bstack1ll1111111_opy_)
        bstack111ll1l111_opy_ = bstack1ll11lll11_opy_.get(bstack11l1l11_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡓࡧࡳࡩࡦࡺࡥࡳࡵࠥਟ"), [])
        bstack1l1ll111l1_opy_ = bstack11l1l11_opy_ (u"ࠤ࠯ࠦਠ").join(bstack111ll1l111_opy_)
        logger.debug(bstack11l1l11_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡆࡹࡸࡺ࡯࡮ࠢࡵࡩࡵ࡫ࡡࡵࡧࡵࠤࡸࡺࡲࡪࡰࡪ࠾ࠥࠫࡳࠣਡ"), bstack1l1ll111l1_opy_)
        bstack1lllllll11_opy_ = {
            bstack11l1l11_opy_ (u"ࠦࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨਢ"): bstack11l1l11_opy_ (u"ࠧࡧࡴࡴ࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠦਣ"),
            bstack11l1l11_opy_ (u"ࠨࡦࡰࡴࡦࡩࡑࡵࡣࡢ࡮ࠥਤ"): bstack11l1l11_opy_ (u"ࠢࡵࡴࡸࡩࠧਥ"),
            bstack11l1l11_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭࠮ࡴࡨࡴࡪࡧࡴࡦࡴࠥਦ"): bstack1l1ll111l1_opy_
        }
        bstack1ll1111111_opy_.update(bstack1lllllll11_opy_)
        logger.debug(bstack11l1l11_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡗࡳࡨࡦࡺࡥࡥࠢ࡯ࡳࡨࡧ࡬ࠡࡱࡳࡸ࡮ࡵ࡮ࡴ࠼ࠣࠩࡸࠨਧ"), bstack1ll1111111_opy_)
        CONFIG[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧਨ")] = bstack1ll1111111_opy_
        logger.debug(bstack11l1l11_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡊ࡮ࡴࡡ࡭ࠢࡆࡓࡓࡌࡉࡈ࠼ࠣࠩࡸࠨ਩"), CONFIG)
def bstack111l11l1ll_opy_():
    bstack1111ll1l1_opy_ = bstack1l1l11ll11_opy_()
    if not bstack1111ll1l1_opy_[bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡗࡵࡰࠬਪ")]:
      raise ValueError(bstack11l1l11_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡘࡶࡱࠦࡩࡴࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡷࡵ࡭ࠡࡩࡵ࡭ࡩࠦࡤࡦࡶࡤ࡭ࡱࡹ࠮ࠣਫ"))
    return bstack1111ll1l1_opy_[bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠧਬ")] + bstack11l1l11_opy_ (u"ࠨࡁࡦࡥࡵࡹ࠽ࠨਭ")
@measure(event_name=EVENTS.bstack1111llllll_opy_, stage=STAGE.bstack11l1lllll_opy_)
def bstack1l1llll11_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack11l1l11_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫਮ")], CONFIG[bstack11l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ਯ")])
        url = bstack1l11l11l1l_opy_
        logger.debug(bstack11l1l11_opy_ (u"ࠦࡆࡺࡴࡦ࡯ࡳࡸ࡮ࡴࡧࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡦࡺ࡯࡬ࡥࡵࠣࡪࡷࡵ࡭ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡕࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠤࡆࡖࡉࠣਰ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack11l1l11_opy_ (u"ࠧࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠦ਱"): bstack11l1l11_opy_ (u"ࠨࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠤਲ")})
            if response.status_code == 200:
                bstack1l11ll1l11_opy_ = json.loads(response.text)
                bstack1lll1lll1l_opy_ = bstack1l11ll1l11_opy_.get(bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡹࠧਲ਼"), [])
                if bstack1lll1lll1l_opy_:
                    bstack1111ll1lll_opy_ = bstack1lll1lll1l_opy_[0]
                    build_hashed_id = bstack1111ll1lll_opy_.get(bstack11l1l11_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ਴"))
                    bstack1lll1111l_opy_ = bstack1ll11ll111_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1lll1111l_opy_])
                    logger.info(bstack111l1ll1ll_opy_.format(bstack1lll1111l_opy_))
                    bstack1l1111111l_opy_ = CONFIG[bstack11l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬਵ")]
                    if bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬਸ਼") in CONFIG:
                      bstack1l1111111l_opy_ += bstack11l1l11_opy_ (u"ࠫࠥ࠭਷") + CONFIG[bstack11l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧਸ")]
                    if bstack1l1111111l_opy_ != bstack1111ll1lll_opy_.get(bstack11l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫਹ")):
                      logger.debug(bstack11l111l11_opy_.format(bstack1111ll1lll_opy_.get(bstack11l1l11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ਺")), bstack1l1111111l_opy_))
                    return result
                else:
                    logger.debug(bstack11l1l11_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡏࡱࠣࡦࡺ࡯࡬ࡥࡵࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࡺࡨࡦࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠲ࠧ਻"))
            else:
                logger.debug(bstack11l1l11_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡦࡺ࡯࡬ࡥࡵ࠱਼ࠦ"))
        except Exception as e:
            logger.error(bstack11l1l11_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࡷࠥࡀࠠࡼࡿࠥ਽").format(str(e)))
    else:
        logger.debug(bstack11l1l11_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡇࡔࡔࡆࡊࡉࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡷࡪࡺ࠮ࠡࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡦࡺ࡯࡬ࡥࡵ࠱ࠦਾ"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack11l11lllll_opy_ import bstack11l11lllll_opy_, Events, bstack1llll11lll_opy_, bstack111llll1ll_opy_
from bstack_utils.measure import bstack1l1l1111ll_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1ll111llll_opy_ import bstack11ll1l111_opy_
from bstack_utils.messages import *
from bstack_utils import bstack1ll1111ll_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack11l111lll_opy_, bstack11lll1llll_opy_, bstack111ll1l1ll_opy_, bstack11lll111_opy_, \
  bstack1l1l11l1ll_opy_, \
  Notset, bstack11ll1lllll_opy_, \
  bstack11lll1l111_opy_, bstack1l11llll1l_opy_, bstack11111llll1_opy_, bstack11l11l1111_opy_, bstack11ll1ll11_opy_, bstack11111lll1_opy_, \
  bstack1111l11ll_opy_, \
  bstack1ll1111l11_opy_, bstack1111lll1l_opy_, bstack11l1ll111_opy_, bstack11llll1lll_opy_, \
  bstack1ll111ll1l_opy_, bstack11llllll11_opy_, bstack1lll1ll1l1_opy_, bstack1l11111l1_opy_
from bstack_utils.bstack1lll11l1l1_opy_ import bstack1l11l1l1ll_opy_
from bstack_utils.bstack111111111_opy_ import bstack111l111ll_opy_, bstack1l1ll1l1l_opy_
from bstack_utils.bstack1lll111lll_opy_ import bstack1l1lll1ll_opy_
from bstack_utils.bstack1111l1l11_opy_ import bstack11ll1111ll_opy_, bstack1ll1lllll_opy_
from bstack_utils.bstack11l1ll11ll_opy_ import bstack11l1ll11ll_opy_
from bstack_utils.bstack1l111l11ll_opy_ import bstack1lll1l11l1_opy_
from bstack_utils.proxy import bstack1l1ll111ll_opy_, bstack1l1l1l1111_opy_, bstack1l111ll1l_opy_, bstack11l11lll1l_opy_
from bstack_utils.bstack1ll111lll_opy_ import bstack1lll11ll11_opy_
import bstack_utils.bstack1111lll1ll_opy_ as bstack1l11l1l11l_opy_
import bstack_utils.bstack111ll1l11_opy_ as bstack111l1lllll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack1111111l1_opy_ import bstack1111l1l111_opy_
from bstack_utils.bstack1llll11l1_opy_ import bstack11l1l111_opy_
from bstack_utils.bstack11l1lll11_opy_ import bstack11ll11lll_opy_
if os.getenv(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡊࡒࡓࡐ࡙ࠧਿ")):
  cli.bstack111llllll1_opy_()
else:
  os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡋࡓࡔࡑࡓࠨੀ")] = bstack11l1l11_opy_ (u"ࠧࡵࡴࡸࡩࠬੁ")
bstack1l111ll11l_opy_ = bstack11l1l11_opy_ (u"ࠨࠢࠣ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࠡࠢ࡬ࡪ࠭ࡶࡡࡨࡧࠣࡁࡂࡃࠠࡷࡱ࡬ࡨࠥ࠶ࠩࠡࡽ࡟ࡲࠥࠦࠠࡵࡴࡼࡿࡡࡴࠠࡤࡱࡱࡷࡹࠦࡦࡴࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࡢࠧࡧࡵ࡟ࠫ࠮ࡁ࡜࡯ࠢࠣࠤࠥࠦࡦࡴ࠰ࡤࡴࡵ࡫࡮ࡥࡈ࡬ࡰࡪ࡙ࡹ࡯ࡥࠫࡦࡸࡺࡡࡤ࡭ࡢࡴࡦࡺࡨ࠭ࠢࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡴࡤ࡯࡮ࡥࡧࡻ࠭ࠥ࠱ࠠࠣ࠼ࠥࠤ࠰ࠦࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡋࡕࡒࡒ࠳ࡶࡡࡳࡵࡨࠬ࠭ࡧࡷࡢ࡫ࡷࠤࡳ࡫ࡷࡑࡣࡪࡩ࠷࠴ࡥࡷࡣ࡯ࡹࡦࡺࡥࠩࠤࠫ࠭ࠥࡃ࠾ࠡࡽࢀࠦ࠱ࠦ࡜ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡩࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡉ࡫ࡴࡢ࡫࡯ࡷࠧࢃ࡜ࠨࠫࠬ࠭ࡠࠨࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠤࡠ࠭ࠥ࠱ࠠࠣ࠮࡟ࡠࡳࠨࠩ࡝ࡰࠣࠤࠥࠦࡽࡤࡣࡷࡧ࡭࠮ࡥࡹࠫࡾࡠࡳࠦࠠࠡࠢࢀࡠࡳࠦࠠࡾ࡞ࡱࠤࠥ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯ࠨੂ")
bstack1l1111l1l1_opy_ = bstack11l1l11_opy_ (u"ࠩ࡟ࡲ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬ࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴࡟࡟ࡲࡨࡵ࡮ࡴࡶࠣࡦࡸࡺࡡࡤ࡭ࡢࡧࡦࡶࡳࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠵ࡢࡢ࡮ࡤࡱࡱࡷࡹࠦࡰࡠ࡫ࡱࡨࡪࡾࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠵ࡡࡡࡴࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴ࡳ࡭࡫ࡦࡩ࠭࠶ࠬࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶࠭ࡡࡴࡣࡰࡰࡶࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭ࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ࠮ࡁ࡜࡯࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰ࠴ࡣࡩࡴࡲࡱ࡮ࡻ࡭࠯࡮ࡤࡹࡳࡩࡨࠡ࠿ࠣࡥࡸࡿ࡮ࡤࠢࠫࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵࠬࠤࡂࡄࠠࡼ࡞ࡱࡰࡪࡺࠠࡤࡣࡳࡷࡀࡢ࡮ࡵࡴࡼࠤࢀࡢ࡮ࡤࡣࡳࡷࠥࡃࠠࡋࡕࡒࡒ࠳ࡶࡡࡳࡵࡨࠬࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠫ࡟ࡲࠥࠦࡽࠡࡥࡤࡸࡨ࡮ࠨࡦࡺࠬࠤࢀࡢ࡮ࠡࠢࠣࠤࢂࡢ࡮ࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡤࡻࡦ࡯ࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰ࠴ࡣࡩࡴࡲࡱ࡮ࡻ࡭࠯ࡥࡲࡲࡳ࡫ࡣࡵࠪࡾࡠࡳࠦࠠࠡࠢࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹࡀࠠࡡࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠧࡿࡪࡴࡣࡰࡦࡨ࡙ࡗࡏࡃࡰ࡯ࡳࡳࡳ࡫࡮ࡵࠪࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡧࡦࡶࡳࠪࠫࢀࡤ࠱ࡢ࡮ࠡࠢࠣࠤ࠳࠴࠮࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹ࡜࡯ࠢࠣࢁ࠮ࡢ࡮ࡾ࡞ࡱ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࠨ੃")
from ._version import __version__
bstack11l1l11l11_opy_ = None
CONFIG = {}
bstack11l111ll1_opy_ = {}
bstack1l11lll1ll_opy_ = {}
bstack11ll1l1111_opy_ = None
bstack1ll11l1ll_opy_ = None
bstack1111ll11l_opy_ = None
bstack1l1111lll1_opy_ = -1
bstack1ll11111l_opy_ = 0
bstack1l1l111lll_opy_ = bstack1l11lllll1_opy_
bstack1111l1l1l1_opy_ = 1
bstack11ll1ll1l1_opy_ = False
bstack111l11111l_opy_ = False
bstack11l11l1ll_opy_ = bstack11l1l11_opy_ (u"ࠪࠫ੄")
bstack111ll1l1l1_opy_ = bstack11l1l11_opy_ (u"ࠫࠬ੅")
bstack11l1l1111l_opy_ = False
bstack11l1l1ll1_opy_ = True
bstack111l111ll1_opy_ = bstack11l1l11_opy_ (u"ࠬ࠭੆")
bstack11llll1l11_opy_ = []
bstack11ll1l11l_opy_ = threading.Lock()
bstack11l1l1ll1l_opy_ = threading.Lock()
bstack1ll1l11l1l_opy_ = bstack11l1l11_opy_ (u"࠭ࠧੇ")
bstack11l1ll11l_opy_ = False
bstack1l11ll11ll_opy_ = None
bstack11lll1l1l1_opy_ = None
bstack1l1ll1l11l_opy_ = None
bstack1l11ll1lll_opy_ = -1
bstack11l1llll11_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠧࡿࠩੈ")), bstack11l1l11_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ੉"), bstack11l1l11_opy_ (u"ࠩ࠱ࡶࡴࡨ࡯ࡵ࠯ࡵࡩࡵࡵࡲࡵ࠯࡫ࡩࡱࡶࡥࡳ࠰࡭ࡷࡴࡴࠧ੊"))
bstack1l11111ll_opy_ = 0
bstack1l1lll1l11_opy_ = 0
bstack11ll1ll1ll_opy_ = []
bstack1l1ll1l111_opy_ = []
bstack1ll111ll11_opy_ = []
bstack11l11111l_opy_ = []
bstack1l111l111_opy_ = bstack11l1l11_opy_ (u"ࠪࠫੋ")
bstack111l11l11l_opy_ = bstack11l1l11_opy_ (u"ࠫࠬੌ")
bstack1l1l1ll1l1_opy_ = False
bstack1l1l1ll11l_opy_ = False
bstack1llll111l1_opy_ = {}
bstack111ll11l11_opy_ = None
bstack1111llll1l_opy_ = None
bstack11l11l1ll1_opy_ = None
bstack1l111ll11_opy_ = None
bstack1l11l1111_opy_ = None
bstack111l1llll1_opy_ = None
bstack11111l1l1_opy_ = None
bstack1lll11l111_opy_ = None
bstack1ll111l111_opy_ = None
bstack11l11llll1_opy_ = None
bstack1l1111l1l_opy_ = None
bstack1lllll11l1_opy_ = None
bstack11111ll1l_opy_ = None
bstack1ll1lll111_opy_ = None
bstack11l111l111_opy_ = None
bstack11ll11l1l1_opy_ = None
bstack1llllll1ll_opy_ = None
bstack11ll111lll_opy_ = None
bstack111ll1111_opy_ = None
bstack1ll1lllll1_opy_ = None
bstack1l11l111ll_opy_ = None
bstack11l1lll1l1_opy_ = None
bstack1llll11l11_opy_ = None
thread_local = threading.local()
bstack11l1ll1lll_opy_ = False
bstack11llllll1l_opy_ = bstack11l1l11_opy_ (u"ࠧࠨ੍")
logger = bstack1ll1111ll_opy_.get_logger(__name__, bstack1l1l111lll_opy_)
bstack111111ll_opy_ = Config.bstack1111lll1_opy_()
percy = bstack11ll1lll1l_opy_()
bstack1l1l1l1l1l_opy_ = bstack11ll1l111_opy_()
bstack1l1l1l11l1_opy_ = bstack11ll1l11_opy_()
def bstack11l111l11l_opy_():
  global CONFIG
  global bstack1l1l1ll1l1_opy_
  global bstack111111ll_opy_
  testContextOptions = bstack11lllllll_opy_(CONFIG)
  if bstack1l1l11l1ll_opy_(CONFIG):
    if (bstack11l1l11_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ੎") in testContextOptions and str(testContextOptions[bstack11l1l11_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ੏")]).lower() == bstack11l1l11_opy_ (u"ࠨࡶࡵࡹࡪ࠭੐")):
      bstack1l1l1ll1l1_opy_ = True
    bstack111111ll_opy_.bstack1l111l1111_opy_(testContextOptions.get(bstack11l1l11_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ੑ"), False))
  else:
    bstack1l1l1ll1l1_opy_ = True
    bstack111111ll_opy_.bstack1l111l1111_opy_(True)
def bstack1l111111l1_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11lll11ll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1111l11111_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11l1l11_opy_ (u"ࠥ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡧࡴࡴࡦࡪࡩࡩ࡭ࡱ࡫ࠢ੒") == args[i].lower() or bstack11l1l11_opy_ (u"ࠦ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡯ࡨ࡬࡫ࠧ੓") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack111l111ll1_opy_
      bstack111l111ll1_opy_ += bstack11l1l11_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡉ࡯࡯ࡨ࡬࡫ࡋ࡯࡬ࡦࠢࠪ੔") + shlex.quote(path)
      return path
  return None
bstack1l1llllll1_opy_ = re.compile(bstack11l1l11_opy_ (u"ࡸࠢ࠯ࠬࡂࡠࠩࢁࠨ࠯ࠬࡂ࠭ࢂ࠴ࠪࡀࠤ੕"))
def bstack11l11l1l1_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l1llllll1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11l1l11_opy_ (u"ࠢࠥࡽࠥ੖") + group + bstack11l1l11_opy_ (u"ࠣࡿࠥ੗"), os.environ.get(group))
  return value
def bstack1llll11l1l_opy_():
  global bstack1llll11l11_opy_
  if bstack1llll11l11_opy_ is None:
        bstack1llll11l11_opy_ = bstack1111l11111_opy_()
  bstack1l1ll11l1_opy_ = bstack1llll11l11_opy_
  if bstack1l1ll11l1_opy_ and os.path.exists(os.path.abspath(bstack1l1ll11l1_opy_)):
    fileName = bstack1l1ll11l1_opy_
  if bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࡠࡈࡌࡐࡊ࠭੘") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧਖ਼")])) and not bstack11l1l11_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࠭ਗ਼") in locals():
    fileName = os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆࠩਜ਼")]
  if bstack11l1l11_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨੜ") in locals():
    bstack111l11l_opy_ = os.path.abspath(fileName)
  else:
    bstack111l11l_opy_ = bstack11l1l11_opy_ (u"ࠧࠨ੝")
  bstack1llll1l111_opy_ = os.getcwd()
  bstack111l11111_opy_ = bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫਫ਼")
  bstack1ll1111l1l_opy_ = bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡤࡱࡱ࠭੟")
  while (not os.path.exists(bstack111l11l_opy_)) and bstack1llll1l111_opy_ != bstack11l1l11_opy_ (u"ࠥࠦ੠"):
    bstack111l11l_opy_ = os.path.join(bstack1llll1l111_opy_, bstack111l11111_opy_)
    if not os.path.exists(bstack111l11l_opy_):
      bstack111l11l_opy_ = os.path.join(bstack1llll1l111_opy_, bstack1ll1111l1l_opy_)
    if bstack1llll1l111_opy_ != os.path.dirname(bstack1llll1l111_opy_):
      bstack1llll1l111_opy_ = os.path.dirname(bstack1llll1l111_opy_)
    else:
      bstack1llll1l111_opy_ = bstack11l1l11_opy_ (u"ࠦࠧ੡")
  bstack1llll11l11_opy_ = bstack111l11l_opy_ if os.path.exists(bstack111l11l_opy_) else None
  return bstack1llll11l11_opy_
def bstack1ll111111l_opy_(config):
    if bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠬ੢") in config:
      config[bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ੣")] = config[bstack11l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧ੤")]
    if bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࡐࡲࡷ࡭ࡴࡴࡳࠨ੥") in config:
      config[bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭੦")] = config[bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࡒࡴࡹ࡯࡯࡯ࡵࠪ੧")]
def bstack1ll1l11111_opy_():
  bstack111l11l_opy_ = bstack1llll11l1l_opy_()
  if not os.path.exists(bstack111l11l_opy_):
    bstack1l1lllll11_opy_(
      bstack1ll1l11lll_opy_.format(os.getcwd()))
  try:
    with open(bstack111l11l_opy_, bstack11l1l11_opy_ (u"ࠫࡷ࠭੨")) as stream:
      yaml.add_implicit_resolver(bstack11l1l11_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨ੩"), bstack1l1llllll1_opy_)
      yaml.add_constructor(bstack11l1l11_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢ੪"), bstack11l11l1l1_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1ll111111l_opy_(config)
      return config
  except:
    with open(bstack111l11l_opy_, bstack11l1l11_opy_ (u"ࠧࡳࠩ੫")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1ll111111l_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1l1lllll11_opy_(bstack1l11ll1ll_opy_.format(str(exc)))
def bstack1lll111ll_opy_(config):
  bstack1l1lllll1l_opy_ = bstack1lll11l1ll_opy_(config)
  for option in list(bstack1l1lllll1l_opy_):
    if option.lower() in bstack1ll1l1ll1l_opy_ and option != bstack1ll1l1ll1l_opy_[option.lower()]:
      bstack1l1lllll1l_opy_[bstack1ll1l1ll1l_opy_[option.lower()]] = bstack1l1lllll1l_opy_[option]
      del bstack1l1lllll1l_opy_[option]
  return config
def bstack1l11l1l1l_opy_():
  global bstack1l11lll1ll_opy_
  for key, bstack1l1l1llll_opy_ in bstack1111lllll1_opy_.items():
    if isinstance(bstack1l1l1llll_opy_, list):
      for var in bstack1l1l1llll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1l11lll1ll_opy_[key] = os.environ[var]
          break
    elif bstack1l1l1llll_opy_ in os.environ and os.environ[bstack1l1l1llll_opy_] and str(os.environ[bstack1l1l1llll_opy_]).strip():
      bstack1l11lll1ll_opy_[key] = os.environ[bstack1l1l1llll_opy_]
  if bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪ੬") in os.environ:
    bstack1l11lll1ll_opy_[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੭")] = {}
    bstack1l11lll1ll_opy_[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ੮")][bstack11l1l11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੯")] = os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧੰ")]
def bstack11l11l11l_opy_():
  global bstack11l111ll1_opy_
  global bstack111l111ll1_opy_
  bstack11ll1l1l1_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack11l1l11_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩੱ").lower() == val.lower():
      bstack11l111ll1_opy_[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫੲ")] = {}
      bstack11l111ll1_opy_[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬੳ")][bstack11l1l11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫੴ")] = sys.argv[idx + 1]
      bstack11ll1l1l1_opy_.extend([idx, idx + 1])
      break
  for key, bstack1l1l1lll11_opy_ in bstack1l111ll111_opy_.items():
    if isinstance(bstack1l1l1lll11_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack1l1l1lll11_opy_:
          if bstack11l1l11_opy_ (u"ࠪ࠱࠲࠭ੵ") + var.lower() == val.lower() and key not in bstack11l111ll1_opy_:
            bstack11l111ll1_opy_[key] = sys.argv[idx + 1]
            bstack111l111ll1_opy_ += bstack11l1l11_opy_ (u"ࠫࠥ࠳࠭ࠨ੶") + var + bstack11l1l11_opy_ (u"ࠬࠦࠧ੷") + shlex.quote(sys.argv[idx + 1])
            bstack11ll1l1l1_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack11l1l11_opy_ (u"࠭࠭࠮ࠩ੸") + bstack1l1l1lll11_opy_.lower() == val.lower() and key not in bstack11l111ll1_opy_:
          bstack11l111ll1_opy_[key] = sys.argv[idx + 1]
          bstack111l111ll1_opy_ += bstack11l1l11_opy_ (u"ࠧࠡ࠯࠰ࠫ੹") + bstack1l1l1lll11_opy_ + bstack11l1l11_opy_ (u"ࠨࠢࠪ੺") + shlex.quote(sys.argv[idx + 1])
          bstack11ll1l1l1_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack11ll1l1l1_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack1ll1ll1111_opy_(config):
  bstack1ll1l1111_opy_ = config.keys()
  for bstack111llll1l1_opy_, bstack1111l1ll11_opy_ in bstack111ll111l1_opy_.items():
    if bstack1111l1ll11_opy_ in bstack1ll1l1111_opy_:
      config[bstack111llll1l1_opy_] = config[bstack1111l1ll11_opy_]
      del config[bstack1111l1ll11_opy_]
  for bstack111llll1l1_opy_, bstack1111l1ll11_opy_ in bstack1111l1111l_opy_.items():
    if isinstance(bstack1111l1ll11_opy_, list):
      for bstack1l11ll111_opy_ in bstack1111l1ll11_opy_:
        if bstack1l11ll111_opy_ in bstack1ll1l1111_opy_:
          config[bstack111llll1l1_opy_] = config[bstack1l11ll111_opy_]
          del config[bstack1l11ll111_opy_]
          break
    elif bstack1111l1ll11_opy_ in bstack1ll1l1111_opy_:
      config[bstack111llll1l1_opy_] = config[bstack1111l1ll11_opy_]
      del config[bstack1111l1ll11_opy_]
  for bstack1l11ll111_opy_ in list(config):
    for bstack11l11ll1ll_opy_ in bstack11l1l11l1l_opy_:
      if bstack1l11ll111_opy_.lower() == bstack11l11ll1ll_opy_.lower() and bstack1l11ll111_opy_ != bstack11l11ll1ll_opy_:
        config[bstack11l11ll1ll_opy_] = config[bstack1l11ll111_opy_]
        del config[bstack1l11ll111_opy_]
  bstack11ll1l1ll_opy_ = [{}]
  if not config.get(bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ੻")):
    config[bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭੼")] = [{}]
  bstack11ll1l1ll_opy_ = config[bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ੽")]
  for platform in bstack11ll1l1ll_opy_:
    for bstack1l11ll111_opy_ in list(platform):
      for bstack11l11ll1ll_opy_ in bstack11l1l11l1l_opy_:
        if bstack1l11ll111_opy_.lower() == bstack11l11ll1ll_opy_.lower() and bstack1l11ll111_opy_ != bstack11l11ll1ll_opy_:
          platform[bstack11l11ll1ll_opy_] = platform[bstack1l11ll111_opy_]
          del platform[bstack1l11ll111_opy_]
  for bstack111llll1l1_opy_, bstack1111l1ll11_opy_ in bstack1111l1111l_opy_.items():
    for platform in bstack11ll1l1ll_opy_:
      if isinstance(bstack1111l1ll11_opy_, list):
        for bstack1l11ll111_opy_ in bstack1111l1ll11_opy_:
          if bstack1l11ll111_opy_ in platform:
            platform[bstack111llll1l1_opy_] = platform[bstack1l11ll111_opy_]
            del platform[bstack1l11ll111_opy_]
            break
      elif bstack1111l1ll11_opy_ in platform:
        platform[bstack111llll1l1_opy_] = platform[bstack1111l1ll11_opy_]
        del platform[bstack1111l1ll11_opy_]
  for bstack1lll1llll1_opy_ in bstack11ll11l1ll_opy_:
    if bstack1lll1llll1_opy_ in config:
      if not bstack11ll11l1ll_opy_[bstack1lll1llll1_opy_] in config:
        config[bstack11ll11l1ll_opy_[bstack1lll1llll1_opy_]] = {}
      config[bstack11ll11l1ll_opy_[bstack1lll1llll1_opy_]].update(config[bstack1lll1llll1_opy_])
      del config[bstack1lll1llll1_opy_]
  for platform in bstack11ll1l1ll_opy_:
    for bstack1lll1llll1_opy_ in bstack11ll11l1ll_opy_:
      if bstack1lll1llll1_opy_ in list(platform):
        if not bstack11ll11l1ll_opy_[bstack1lll1llll1_opy_] in platform:
          platform[bstack11ll11l1ll_opy_[bstack1lll1llll1_opy_]] = {}
        platform[bstack11ll11l1ll_opy_[bstack1lll1llll1_opy_]].update(platform[bstack1lll1llll1_opy_])
        del platform[bstack1lll1llll1_opy_]
  config = bstack1lll111ll_opy_(config)
  return config
def bstack11ll1l1l1l_opy_(config):
  global bstack111ll1l1l1_opy_
  bstack11llll1ll_opy_ = False
  if bstack11l1l11_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ੾") in config and str(config[bstack11l1l11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ੿")]).lower() != bstack11l1l11_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭઀"):
    if bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬઁ") not in config or str(config[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ં")]).lower() == bstack11l1l11_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩઃ"):
      config[bstack11l1l11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪ઄")] = False
    else:
      bstack1111ll1l1_opy_ = bstack1l1l11ll11_opy_()
      if bstack11l1l11_opy_ (u"ࠬ࡯ࡳࡕࡴ࡬ࡥࡱࡍࡲࡪࡦࠪઅ") in bstack1111ll1l1_opy_:
        if not bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪઆ") in config:
          config[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫઇ")] = {}
        config[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬઈ")][bstack11l1l11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫઉ")] = bstack11l1l11_opy_ (u"ࠪࡥࡹࡹ࠭ࡳࡧࡳࡩࡦࡺࡥࡳࠩઊ")
        bstack11llll1ll_opy_ = True
        bstack111ll1l1l1_opy_ = config[bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨઋ")].get(bstack11l1l11_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઌ"))
  if bstack1l1l11l1ll_opy_(config) and bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪઍ") in config and str(config[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ઎")]).lower() != bstack11l1l11_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧએ") and not bstack11llll1ll_opy_:
    if not bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઐ") in config:
      config[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઑ")] = {}
    if not config[bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ઒")].get(bstack11l1l11_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩઓ")) and not bstack11l1l11_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨઔ") in config[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫક")]:
      bstack1ll1ll11_opy_ = datetime.datetime.now()
      bstack1l1l1lll1l_opy_ = bstack1ll1ll11_opy_.strftime(bstack11l1l11_opy_ (u"ࠨࠧࡧࡣࠪࡨ࡟ࠦࡊࠨࡑࠬખ"))
      hostname = socket.gethostname()
      bstack111lll1ll_opy_ = bstack11l1l11_opy_ (u"ࠩࠪગ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11l1l11_opy_ (u"ࠪࡿࢂࡥࡻࡾࡡࡾࢁࠬઘ").format(bstack1l1l1lll1l_opy_, hostname, bstack111lll1ll_opy_)
      config[bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨઙ")][bstack11l1l11_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧચ")] = identifier
    bstack111ll1l1l1_opy_ = config[bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪછ")].get(bstack11l1l11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩજ"))
  return config
def bstack111l11llll_opy_():
  bstack1ll1lll11_opy_ =  bstack11l11l1111_opy_()[bstack11l1l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠧઝ")]
  return bstack1ll1lll11_opy_ if bstack1ll1lll11_opy_ else -1
def bstack1ll1l1l11_opy_(bstack1ll1lll11_opy_):
  global CONFIG
  if not bstack11l1l11_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫઞ") in CONFIG[bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬટ")]:
    return
  CONFIG[bstack11l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ઠ")] = CONFIG[bstack11l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧડ")].replace(
    bstack11l1l11_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨઢ"),
    str(bstack1ll1lll11_opy_)
  )
def bstack11lll1ll1_opy_():
  global CONFIG
  if not bstack11l1l11_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭ણ") in CONFIG[bstack11l1l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪત")]:
    return
  bstack1ll1ll11_opy_ = datetime.datetime.now()
  bstack1l1l1lll1l_opy_ = bstack1ll1ll11_opy_.strftime(bstack11l1l11_opy_ (u"ࠩࠨࡨ࠲ࠫࡢ࠮ࠧࡋ࠾ࠪࡓࠧથ"))
  CONFIG[bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬદ")] = CONFIG[bstack11l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ધ")].replace(
    bstack11l1l11_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫન"),
    bstack1l1l1lll1l_opy_
  )
def bstack1111lll11l_opy_():
  global CONFIG
  if bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ઩") in CONFIG and not bool(CONFIG[bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩપ")]):
    del CONFIG[bstack11l1l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪફ")]
    return
  if not bstack11l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫબ") in CONFIG:
    CONFIG[bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬભ")] = bstack11l1l11_opy_ (u"ࠫࠨࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧમ")
  if bstack11l1l11_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫય") in CONFIG[bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨર")]:
    bstack11lll1ll1_opy_()
    os.environ[bstack11l1l11_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ઱")] = CONFIG[bstack11l1l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪલ")]
  if not bstack11l1l11_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫળ") in CONFIG[bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ઴")]:
    return
  bstack1ll1lll11_opy_ = bstack11l1l11_opy_ (u"ࠫࠬવ")
  bstack1l111llll1_opy_ = bstack111l11llll_opy_()
  if bstack1l111llll1_opy_ != -1:
    bstack1ll1lll11_opy_ = bstack11l1l11_opy_ (u"ࠬࡉࡉࠡࠩશ") + str(bstack1l111llll1_opy_)
  if bstack1ll1lll11_opy_ == bstack11l1l11_opy_ (u"࠭ࠧષ"):
    bstack111111lll_opy_ = bstack1l1l1lllll_opy_(CONFIG[bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪસ")])
    if bstack111111lll_opy_ != -1:
      bstack1ll1lll11_opy_ = str(bstack111111lll_opy_)
  if bstack1ll1lll11_opy_:
    bstack1ll1l1l11_opy_(bstack1ll1lll11_opy_)
    os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬહ")] = CONFIG[bstack11l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ઺")]
def bstack1ll11l1ll1_opy_(bstack11lllll11_opy_, bstack1l11llll11_opy_, path):
  json_data = {
    bstack11l1l11_opy_ (u"ࠪ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ઻"): bstack1l11llll11_opy_
  }
  if os.path.exists(path):
    bstack1111l111l1_opy_ = json.load(open(path, bstack11l1l11_opy_ (u"ࠫࡷࡨ઼ࠧ")))
  else:
    bstack1111l111l1_opy_ = {}
  bstack1111l111l1_opy_[bstack11lllll11_opy_] = json_data
  with open(path, bstack11l1l11_opy_ (u"ࠧࡽࠫࠣઽ")) as outfile:
    json.dump(bstack1111l111l1_opy_, outfile)
def bstack1l1l1lllll_opy_(bstack11lllll11_opy_):
  bstack11lllll11_opy_ = str(bstack11lllll11_opy_)
  bstack1l1l1ll1l_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"࠭ࡾࠨા")), bstack11l1l11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧિ"))
  try:
    if not os.path.exists(bstack1l1l1ll1l_opy_):
      os.makedirs(bstack1l1l1ll1l_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠨࢀࠪી")), bstack11l1l11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩુ"), bstack11l1l11_opy_ (u"ࠪ࠲ࡧࡻࡩ࡭ࡦ࠰ࡲࡦࡳࡥ࠮ࡥࡤࡧ࡭࡫࠮࡫ࡵࡲࡲࠬૂ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11l1l11_opy_ (u"ࠫࡼ࠭ૃ")):
        pass
      with open(file_path, bstack11l1l11_opy_ (u"ࠧࡽࠫࠣૄ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11l1l11_opy_ (u"࠭ࡲࠨૅ")) as bstack111lll1l1_opy_:
      bstack11l1llll1_opy_ = json.load(bstack111lll1l1_opy_)
    if bstack11lllll11_opy_ in bstack11l1llll1_opy_:
      bstack1ll1ll11l1_opy_ = bstack11l1llll1_opy_[bstack11lllll11_opy_][bstack11l1l11_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૆")]
      bstack1111ll111l_opy_ = int(bstack1ll1ll11l1_opy_) + 1
      bstack1ll11l1ll1_opy_(bstack11lllll11_opy_, bstack1111ll111l_opy_, file_path)
      return bstack1111ll111l_opy_
    else:
      bstack1ll11l1ll1_opy_(bstack11lllll11_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1111l1l11l_opy_.format(str(e)))
    return -1
def bstack1l11ll111l_opy_(config):
  if not config[bstack11l1l11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪે")] or not config[bstack11l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬૈ")]:
    return True
  else:
    return False
def bstack11l1l1l1l_opy_(config, index=0):
  global bstack11l1l1111l_opy_
  bstack111lll111l_opy_ = {}
  caps = bstack1ll1l11l11_opy_ + bstack11l11lll11_opy_
  if config.get(bstack11l1l11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧૉ"), False):
    bstack111lll111l_opy_[bstack11l1l11_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨ૊")] = True
    bstack111lll111l_opy_[bstack11l1l11_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩો")] = config.get(bstack11l1l11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪૌ"), {})
  if bstack11l1l1111l_opy_:
    caps += bstack1l11111l1l_opy_
  for key in config:
    if key in caps + [bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵ્ࠪ")]:
      continue
    bstack111lll111l_opy_[key] = config[key]
  if bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૎") in config:
    for bstack11lll111l_opy_ in config[bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૏")][index]:
      if bstack11lll111l_opy_ in caps:
        continue
      bstack111lll111l_opy_[bstack11lll111l_opy_] = config[bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ૐ")][index][bstack11lll111l_opy_]
  bstack111lll111l_opy_[bstack11l1l11_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭૑")] = socket.gethostname()
  if bstack11l1l11_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭૒") in bstack111lll111l_opy_:
    del (bstack111lll111l_opy_[bstack11l1l11_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧ૓")])
  return bstack111lll111l_opy_
def bstack1l1lll11ll_opy_(config):
  global bstack11l1l1111l_opy_
  bstack1111l11l11_opy_ = {}
  caps = bstack11l11lll11_opy_
  if bstack11l1l1111l_opy_:
    caps += bstack1l11111l1l_opy_
  for key in caps:
    if key in config:
      bstack1111l11l11_opy_[key] = config[key]
  return bstack1111l11l11_opy_
def bstack1ll111lll1_opy_(bstack111lll111l_opy_, bstack1111l11l11_opy_):
  bstack1l1l1l11l_opy_ = {}
  for key in bstack111lll111l_opy_.keys():
    if key in bstack111ll111l1_opy_:
      bstack1l1l1l11l_opy_[bstack111ll111l1_opy_[key]] = bstack111lll111l_opy_[key]
    else:
      bstack1l1l1l11l_opy_[key] = bstack111lll111l_opy_[key]
  for key in bstack1111l11l11_opy_:
    if key in bstack111ll111l1_opy_:
      bstack1l1l1l11l_opy_[bstack111ll111l1_opy_[key]] = bstack1111l11l11_opy_[key]
    else:
      bstack1l1l1l11l_opy_[key] = bstack1111l11l11_opy_[key]
  return bstack1l1l1l11l_opy_
def bstack111ll1ll11_opy_(config, index=0):
  global bstack11l1l1111l_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack111l1l1l1_opy_ = bstack11l111lll_opy_(bstack1l11ll11l_opy_, config, logger)
  bstack1111l11l11_opy_ = bstack1l1lll11ll_opy_(config)
  bstack111l111111_opy_ = bstack11l11lll11_opy_
  bstack111l111111_opy_ += bstack1111l1llll_opy_
  bstack1111l11l11_opy_ = update(bstack1111l11l11_opy_, bstack111l1l1l1_opy_)
  if bstack11l1l1111l_opy_:
    bstack111l111111_opy_ += bstack1l11111l1l_opy_
  if bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૔") in config:
    if bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭૕") in config[bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૖")][index]:
      caps[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ૗")] = config[bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૘")][index][bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ૙")]
    if bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ૚") in config[bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૛")][index]:
      caps[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ૜")] = str(config[bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૝")][index][bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ૞")])
    bstack11lllll1l1_opy_ = bstack11l111lll_opy_(bstack1l11ll11l_opy_, config[bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૟")][index], logger)
    bstack111l111111_opy_ += list(bstack11lllll1l1_opy_.keys())
    for bstack1111ll111_opy_ in bstack111l111111_opy_:
      if bstack1111ll111_opy_ in config[bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૠ")][index]:
        if bstack1111ll111_opy_ == bstack11l1l11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨૡ"):
          try:
            bstack11lllll1l1_opy_[bstack1111ll111_opy_] = str(config[bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪૢ")][index][bstack1111ll111_opy_] * 1.0)
          except:
            bstack11lllll1l1_opy_[bstack1111ll111_opy_] = str(config[bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫૣ")][index][bstack1111ll111_opy_])
        else:
          bstack11lllll1l1_opy_[bstack1111ll111_opy_] = config[bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૤")][index][bstack1111ll111_opy_]
        del (config[bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૥")][index][bstack1111ll111_opy_])
    bstack1111l11l11_opy_ = update(bstack1111l11l11_opy_, bstack11lllll1l1_opy_)
  bstack111lll111l_opy_ = bstack11l1l1l1l_opy_(config, index)
  for bstack1l11ll111_opy_ in bstack11l11lll11_opy_ + list(bstack111l1l1l1_opy_.keys()):
    if bstack1l11ll111_opy_ in bstack111lll111l_opy_:
      bstack1111l11l11_opy_[bstack1l11ll111_opy_] = bstack111lll111l_opy_[bstack1l11ll111_opy_]
      del (bstack111lll111l_opy_[bstack1l11ll111_opy_])
  if bstack11ll1lllll_opy_(config):
    bstack111lll111l_opy_[bstack11l1l11_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ૦")] = True
    caps.update(bstack1111l11l11_opy_)
    caps[bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭૧")] = bstack111lll111l_opy_
  else:
    bstack111lll111l_opy_[bstack11l1l11_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭૨")] = False
    caps.update(bstack1ll111lll1_opy_(bstack111lll111l_opy_, bstack1111l11l11_opy_))
    if bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ૩") in caps:
      caps[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ૪")] = caps[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ૫")]
      del (caps[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ૬")])
    if bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ૭") in caps:
      caps[bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ૮")] = caps[bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ૯")]
      del (caps[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ૰")])
  return caps
def bstack1ll111l1l1_opy_():
  global bstack1ll1l11l1l_opy_
  global CONFIG
  if bstack11lll11ll_opy_() <= version.parse(bstack11l1l11_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨ૱")):
    if bstack1ll1l11l1l_opy_ != bstack11l1l11_opy_ (u"ࠩࠪ૲"):
      return bstack11l1l11_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ૳") + bstack1ll1l11l1l_opy_ + bstack11l1l11_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣ૴")
    return bstack1111l11ll1_opy_
  if bstack1ll1l11l1l_opy_ != bstack11l1l11_opy_ (u"ࠬ࠭૵"):
    return bstack11l1l11_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣ૶") + bstack1ll1l11l1l_opy_ + bstack11l1l11_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣ૷")
  return bstack111l1ll111_opy_
def bstack11ll11ll1l_opy_(options):
  return hasattr(options, bstack11l1l11_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩ૸"))
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
def bstack1ll1111l1_opy_(options, bstack11l11l1l1l_opy_):
  for bstack1l11l1ll1_opy_ in bstack11l11l1l1l_opy_:
    if bstack1l11l1ll1_opy_ in [bstack11l1l11_opy_ (u"ࠩࡤࡶ࡬ࡹࠧૹ"), bstack11l1l11_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧૺ")]:
      continue
    if bstack1l11l1ll1_opy_ in options._experimental_options:
      options._experimental_options[bstack1l11l1ll1_opy_] = update(options._experimental_options[bstack1l11l1ll1_opy_],
                                                         bstack11l11l1l1l_opy_[bstack1l11l1ll1_opy_])
    else:
      options.add_experimental_option(bstack1l11l1ll1_opy_, bstack11l11l1l1l_opy_[bstack1l11l1ll1_opy_])
  if bstack11l1l11_opy_ (u"ࠫࡦࡸࡧࡴࠩૻ") in bstack11l11l1l1l_opy_:
    for arg in bstack11l11l1l1l_opy_[bstack11l1l11_opy_ (u"ࠬࡧࡲࡨࡵࠪૼ")]:
      options.add_argument(arg)
    del (bstack11l11l1l1l_opy_[bstack11l1l11_opy_ (u"࠭ࡡࡳࡩࡶࠫ૽")])
  if bstack11l1l11_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ૾") in bstack11l11l1l1l_opy_:
    for ext in bstack11l11l1l1l_opy_[bstack11l1l11_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ૿")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack11l11l1l1l_opy_[bstack11l1l11_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭଀")])
def bstack111ll1ll1_opy_(options, bstack1ll111l1ll_opy_):
  if bstack11l1l11_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩଁ") in bstack1ll111l1ll_opy_:
    for bstack111l1llll_opy_ in bstack1ll111l1ll_opy_[bstack11l1l11_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪଂ")]:
      if bstack111l1llll_opy_ in options._preferences:
        options._preferences[bstack111l1llll_opy_] = update(options._preferences[bstack111l1llll_opy_], bstack1ll111l1ll_opy_[bstack11l1l11_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫଃ")][bstack111l1llll_opy_])
      else:
        options.set_preference(bstack111l1llll_opy_, bstack1ll111l1ll_opy_[bstack11l1l11_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ଄")][bstack111l1llll_opy_])
  if bstack11l1l11_opy_ (u"ࠧࡢࡴࡪࡷࠬଅ") in bstack1ll111l1ll_opy_:
    for arg in bstack1ll111l1ll_opy_[bstack11l1l11_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଆ")]:
      options.add_argument(arg)
def bstack11l1l111l1_opy_(options, bstack1ll111ll1_opy_):
  if bstack11l1l11_opy_ (u"ࠩࡺࡩࡧࡼࡩࡦࡹࠪଇ") in bstack1ll111ll1_opy_:
    options.use_webview(bool(bstack1ll111ll1_opy_[bstack11l1l11_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫଈ")]))
  bstack1ll1111l1_opy_(options, bstack1ll111ll1_opy_)
def bstack1ll1l1lll1_opy_(options, bstack11111llll_opy_):
  for bstack1ll11l111_opy_ in bstack11111llll_opy_:
    if bstack1ll11l111_opy_ in [bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨଉ"), bstack11l1l11_opy_ (u"ࠬࡧࡲࡨࡵࠪଊ")]:
      continue
    options.set_capability(bstack1ll11l111_opy_, bstack11111llll_opy_[bstack1ll11l111_opy_])
  if bstack11l1l11_opy_ (u"࠭ࡡࡳࡩࡶࠫଋ") in bstack11111llll_opy_:
    for arg in bstack11111llll_opy_[bstack11l1l11_opy_ (u"ࠧࡢࡴࡪࡷࠬଌ")]:
      options.add_argument(arg)
  if bstack11l1l11_opy_ (u"ࠨࡶࡨࡧ࡭ࡴ࡯࡭ࡱࡪࡽࡕࡸࡥࡷ࡫ࡨࡻࠬ଍") in bstack11111llll_opy_:
    options.bstack1l1l1l111l_opy_(bool(bstack11111llll_opy_[bstack11l1l11_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭଎")]))
def bstack1lll11111_opy_(options, bstack11ll1111l_opy_):
  for bstack111l1l111_opy_ in bstack11ll1111l_opy_:
    if bstack111l1l111_opy_ in [bstack11l1l11_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧଏ"), bstack11l1l11_opy_ (u"ࠫࡦࡸࡧࡴࠩଐ")]:
      continue
    options._options[bstack111l1l111_opy_] = bstack11ll1111l_opy_[bstack111l1l111_opy_]
  if bstack11l1l11_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ଑") in bstack11ll1111l_opy_:
    for bstack11111l11ll_opy_ in bstack11ll1111l_opy_[bstack11l1l11_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ଒")]:
      options.bstack111lll1l11_opy_(
        bstack11111l11ll_opy_, bstack11ll1111l_opy_[bstack11l1l11_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଓ")][bstack11111l11ll_opy_])
  if bstack11l1l11_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଔ") in bstack11ll1111l_opy_:
    for arg in bstack11ll1111l_opy_[bstack11l1l11_opy_ (u"ࠩࡤࡶ࡬ࡹࠧକ")]:
      options.add_argument(arg)
def bstack1lll111ll1_opy_(options, caps):
  if not hasattr(options, bstack11l1l11_opy_ (u"ࠪࡏࡊ࡟ࠧଖ")):
    return
  if options.KEY == bstack11l1l11_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩଗ"):
    options = bstack111l1lll_opy_.bstack11l1l1lll1_opy_(bstack111l1l1111_opy_=options, config=CONFIG)
  if options.KEY == bstack11l1l11_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪଘ") and options.KEY in caps:
    bstack1ll1111l1_opy_(options, caps[bstack11l1l11_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫଙ")])
  elif options.KEY == bstack11l1l11_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬଚ") and options.KEY in caps:
    bstack111ll1ll1_opy_(options, caps[bstack11l1l11_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ଛ")])
  elif options.KEY == bstack11l1l11_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪଜ") and options.KEY in caps:
    bstack1ll1l1lll1_opy_(options, caps[bstack11l1l11_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫଝ")])
  elif options.KEY == bstack11l1l11_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬଞ") and options.KEY in caps:
    bstack11l1l111l1_opy_(options, caps[bstack11l1l11_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ଟ")])
  elif options.KEY == bstack11l1l11_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬଠ") and options.KEY in caps:
    bstack1lll11111_opy_(options, caps[bstack11l1l11_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ଡ")])
def bstack11ll111l1l_opy_(caps):
  global bstack11l1l1111l_opy_
  if isinstance(os.environ.get(bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩଢ")), str):
    bstack11l1l1111l_opy_ = eval(os.getenv(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪଣ")))
  if bstack11l1l1111l_opy_:
    if bstack1l111111l1_opy_() < version.parse(bstack11l1l11_opy_ (u"ࠪ࠶࠳࠹࠮࠱ࠩତ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11l1l11_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫଥ")
    if bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪଦ") in caps:
      browser = caps[bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫଧ")]
    elif bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨନ") in caps:
      browser = caps[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ଩")]
    browser = str(browser).lower()
    if browser == bstack11l1l11_opy_ (u"ࠩ࡬ࡴ࡭ࡵ࡮ࡦࠩପ") or browser == bstack11l1l11_opy_ (u"ࠪ࡭ࡵࡧࡤࠨଫ"):
      browser = bstack11l1l11_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫବ")
    if browser == bstack11l1l11_opy_ (u"ࠬࡹࡡ࡮ࡵࡸࡲ࡬࠭ଭ"):
      browser = bstack11l1l11_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ମ")
    if browser not in [bstack11l1l11_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧଯ"), bstack11l1l11_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭ର"), bstack11l1l11_opy_ (u"ࠩ࡬ࡩࠬ଱"), bstack11l1l11_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪଲ"), bstack11l1l11_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬଳ")]:
      return None
    try:
      package = bstack11l1l11_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡿࢂ࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧ଴").format(browser)
      name = bstack11l1l11_opy_ (u"࠭ࡏࡱࡶ࡬ࡳࡳࡹࠧଵ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11ll11ll1l_opy_(options):
        return None
      for bstack1l11ll111_opy_ in caps.keys():
        options.set_capability(bstack1l11ll111_opy_, caps[bstack1l11ll111_opy_])
      bstack1lll111ll1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1l1l11ll1l_opy_(options, bstack11111ll11_opy_):
  if not bstack11ll11ll1l_opy_(options):
    return
  for bstack1l11ll111_opy_ in bstack11111ll11_opy_.keys():
    if bstack1l11ll111_opy_ in bstack1111l1llll_opy_:
      continue
    if bstack1l11ll111_opy_ in options._caps and type(options._caps[bstack1l11ll111_opy_]) in [dict, list]:
      options._caps[bstack1l11ll111_opy_] = update(options._caps[bstack1l11ll111_opy_], bstack11111ll11_opy_[bstack1l11ll111_opy_])
    else:
      options.set_capability(bstack1l11ll111_opy_, bstack11111ll11_opy_[bstack1l11ll111_opy_])
  bstack1lll111ll1_opy_(options, bstack11111ll11_opy_)
  if bstack11l1l11_opy_ (u"ࠧ࡮ࡱࡽ࠾ࡩ࡫ࡢࡶࡩࡪࡩࡷࡇࡤࡥࡴࡨࡷࡸ࠭ଶ") in options._caps:
    if options._caps[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ଷ")] and options._caps[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧସ")].lower() != bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫହ"):
      del options._caps[bstack11l1l11_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪ଺")]
def bstack111ll1llll_opy_(proxy_config):
  if bstack11l1l11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ଻") in proxy_config:
    proxy_config[bstack11l1l11_opy_ (u"࠭ࡳࡴ࡮ࡓࡶࡴࡾࡹࠨ଼")] = proxy_config[bstack11l1l11_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫଽ")]
    del (proxy_config[bstack11l1l11_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬା")])
  if bstack11l1l11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬି") in proxy_config and proxy_config[bstack11l1l11_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭ୀ")].lower() != bstack11l1l11_opy_ (u"ࠫࡩ࡯ࡲࡦࡥࡷࠫୁ"):
    proxy_config[bstack11l1l11_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨୂ")] = bstack11l1l11_opy_ (u"࠭࡭ࡢࡰࡸࡥࡱ࠭ୃ")
  if bstack11l1l11_opy_ (u"ࠧࡱࡴࡲࡼࡾࡇࡵࡵࡱࡦࡳࡳ࡬ࡩࡨࡗࡵࡰࠬୄ") in proxy_config:
    proxy_config[bstack11l1l11_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ୅")] = bstack11l1l11_opy_ (u"ࠩࡳࡥࡨ࠭୆")
  return proxy_config
def bstack11l1111ll1_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11l1l11_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩେ") in config:
    return proxy
  config[bstack11l1l11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪୈ")] = bstack111ll1llll_opy_(config[bstack11l1l11_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ୉")])
  if proxy == None:
    proxy = Proxy(config[bstack11l1l11_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୊")])
  return proxy
def bstack1ll11ll1l1_opy_(self):
  global CONFIG
  global bstack1lllll11l1_opy_
  try:
    proxy = bstack1l111ll1l_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11l1l11_opy_ (u"ࠧ࠯ࡲࡤࡧࠬୋ")):
        proxies = bstack1l1ll111ll_opy_(proxy, bstack1ll111l1l1_opy_())
        if len(proxies) > 0:
          protocol, bstack1l11ll1l1_opy_ = proxies.popitem()
          if bstack11l1l11_opy_ (u"ࠣ࠼࠲࠳ࠧୌ") in bstack1l11ll1l1_opy_:
            return bstack1l11ll1l1_opy_
          else:
            return bstack11l1l11_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱୍ࠥ") + bstack1l11ll1l1_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11l1l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢ୎").format(str(e)))
  return bstack1lllll11l1_opy_(self)
def bstack11l11l111l_opy_():
  global CONFIG
  return bstack11l11lll1l_opy_(CONFIG) and bstack11111lll1_opy_() and bstack11lll11ll_opy_() >= version.parse(bstack1ll1l1l111_opy_)
def bstack11l1ll1l1_opy_():
  global CONFIG
  return (bstack11l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ୏") in CONFIG or bstack11l1l11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ୐") in CONFIG) and bstack1111l11ll_opy_()
def bstack1lll11l1ll_opy_(config):
  bstack1l1lllll1l_opy_ = {}
  if bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ୑") in config:
    bstack1l1lllll1l_opy_ = config[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୒")]
  if bstack11l1l11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ୓") in config:
    bstack1l1lllll1l_opy_ = config[bstack11l1l11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୔")]
  proxy = bstack1l111ll1l_opy_(config)
  if proxy:
    if proxy.endswith(bstack11l1l11_opy_ (u"ࠪ࠲ࡵࡧࡣࠨ୕")) and os.path.isfile(proxy):
      bstack1l1lllll1l_opy_[bstack11l1l11_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧୖ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11l1l11_opy_ (u"ࠬ࠴ࡰࡢࡥࠪୗ")):
        proxies = bstack1l1l1l1111_opy_(config, bstack1ll111l1l1_opy_())
        if len(proxies) > 0:
          protocol, bstack1l11ll1l1_opy_ = proxies.popitem()
          if bstack11l1l11_opy_ (u"ࠨ࠺࠰࠱ࠥ୘") in bstack1l11ll1l1_opy_:
            parsed_url = urlparse(bstack1l11ll1l1_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11l1l11_opy_ (u"ࠢ࠻࠱࠲ࠦ୙") + bstack1l11ll1l1_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1l1lllll1l_opy_[bstack11l1l11_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫ୚")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1l1lllll1l_opy_[bstack11l1l11_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬ୛")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1l1lllll1l_opy_[bstack11l1l11_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ଡ଼")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1l1lllll1l_opy_[bstack11l1l11_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧଢ଼")] = str(parsed_url.password)
  return bstack1l1lllll1l_opy_
def bstack11lllllll_opy_(config):
  if bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪ୞") in config:
    return config[bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫୟ")]
  return {}
def bstack11l1llllll_opy_(caps):
  global bstack111ll1l1l1_opy_
  if bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨୠ") in caps:
    caps[bstack11l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩୡ")][bstack11l1l11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨୢ")] = True
    if bstack111ll1l1l1_opy_:
      caps[bstack11l1l11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫୣ")][bstack11l1l11_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭୤")] = bstack111ll1l1l1_opy_
  else:
    caps[bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪ୥")] = True
    if bstack111ll1l1l1_opy_:
      caps[bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ୦")] = bstack111ll1l1l1_opy_
@measure(event_name=EVENTS.bstack11ll1l1lll_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack111l11lll_opy_():
  global CONFIG
  if not bstack1l1l11l1ll_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ୧") in CONFIG and bstack1lll1ll1l1_opy_(CONFIG[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ୨")]):
    if (
      bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୩") in CONFIG
      and bstack1lll1ll1l1_opy_(CONFIG[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ୪")].get(bstack11l1l11_opy_ (u"ࠫࡸࡱࡩࡱࡄ࡬ࡲࡦࡸࡹࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡤࡸ࡮ࡵ࡮ࠨ୫")))
    ):
      logger.debug(bstack11l1l11_opy_ (u"ࠧࡒ࡯ࡤࡣ࡯ࠤࡧ࡯࡮ࡢࡴࡼࠤࡳࡵࡴࠡࡵࡷࡥࡷࡺࡥࡥࠢࡤࡷࠥࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨ୬"))
      return
    bstack1l1lllll1l_opy_ = bstack1lll11l1ll_opy_(CONFIG)
    bstack11l11111l1_opy_(CONFIG[bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ୭")], bstack1l1lllll1l_opy_)
def bstack11l11111l1_opy_(key, bstack1l1lllll1l_opy_):
  global bstack11l1l11l11_opy_
  logger.info(bstack1lll1l1111_opy_)
  try:
    bstack11l1l11l11_opy_ = Local()
    bstack111llll111_opy_ = {bstack11l1l11_opy_ (u"ࠧ࡬ࡧࡼࠫ୮"): key}
    bstack111llll111_opy_.update(bstack1l1lllll1l_opy_)
    logger.debug(bstack1l1ll1llll_opy_.format(str(bstack111llll111_opy_)).replace(key, bstack11l1l11_opy_ (u"ࠨ࡝ࡕࡉࡉࡇࡃࡕࡇࡇࡡࠬ୯")))
    bstack11l1l11l11_opy_.start(**bstack111llll111_opy_)
    if bstack11l1l11l11_opy_.isRunning():
      logger.info(bstack1l11l1ll11_opy_)
  except Exception as e:
    bstack1l1lllll11_opy_(bstack1l11lll1l1_opy_.format(str(e)))
def bstack111111l11_opy_():
  global bstack11l1l11l11_opy_
  if bstack11l1l11l11_opy_.isRunning():
    logger.info(bstack111l11ll11_opy_)
    bstack11l1l11l11_opy_.stop()
  bstack11l1l11l11_opy_ = None
def bstack1ll1l11ll1_opy_(bstack11l111llll_opy_=[]):
  global CONFIG
  bstack1ll11111ll_opy_ = []
  bstack11l1l11ll1_opy_ = [bstack11l1l11_opy_ (u"ࠩࡲࡷࠬ୰"), bstack11l1l11_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ୱ"), bstack11l1l11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨ୲"), bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ୳"), bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ୴"), bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ୵")]
  try:
    for err in bstack11l111llll_opy_:
      bstack11lll1l1l_opy_ = {}
      for k in bstack11l1l11ll1_opy_:
        val = CONFIG[bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ୶")][int(err[bstack11l1l11_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ୷")])].get(k)
        if val:
          bstack11lll1l1l_opy_[k] = val
      if(err[bstack11l1l11_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ୸")] != bstack11l1l11_opy_ (u"ࠫࠬ୹")):
        bstack11lll1l1l_opy_[bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡶࠫ୺")] = {
          err[bstack11l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ୻")]: err[bstack11l1l11_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭୼")]
        }
        bstack1ll11111ll_opy_.append(bstack11lll1l1l_opy_)
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡴࡸ࡭ࡢࡶࡷ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴ࠻ࠢࠪ୽") + str(e))
  finally:
    return bstack1ll11111ll_opy_
def bstack1ll11lll1_opy_(file_name):
  bstack11l1llll1l_opy_ = []
  try:
    bstack1ll1ll111_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1ll1ll111_opy_):
      with open(bstack1ll1ll111_opy_) as f:
        bstack1111ll1l11_opy_ = json.load(f)
        bstack11l1llll1l_opy_ = bstack1111ll1l11_opy_
      os.remove(bstack1ll1ll111_opy_)
    return bstack11l1llll1l_opy_
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫࡯࡮ࡥ࡫ࡱ࡫ࠥ࡫ࡲࡳࡱࡵࠤࡱ࡯ࡳࡵ࠼ࠣࠫ୾") + str(e))
    return bstack11l1llll1l_opy_
def bstack1l1111l11l_opy_():
  try:
      from bstack_utils.constants import bstack1l1l11llll_opy_, EVENTS
      from bstack_utils.helper import bstack11lll1llll_opy_, get_host_info, bstack111111ll_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack1111llll11_opy_ = os.path.join(os.getcwd(), bstack11l1l11_opy_ (u"ࠪࡰࡴ࡭ࠧ୿"), bstack11l1l11_opy_ (u"ࠫࡰ࡫ࡹ࠮࡯ࡨࡸࡷ࡯ࡣࡴ࠰࡭ࡷࡴࡴࠧ஀"))
      lock = FileLock(bstack1111llll11_opy_+bstack11l1l11_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦ஁"))
      def bstack1l1lll11_opy_():
          try:
              with lock:
                  with open(bstack1111llll11_opy_, bstack11l1l11_opy_ (u"ࠨࡲࠣஂ"), encoding=bstack11l1l11_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨஃ")) as file:
                      data = json.load(file)
                      config = {
                          bstack11l1l11_opy_ (u"ࠣࡪࡨࡥࡩ࡫ࡲࡴࠤ஄"): {
                              bstack11l1l11_opy_ (u"ࠤࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠣஅ"): bstack11l1l11_opy_ (u"ࠥࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳࠨஆ"),
                          }
                      }
                      bstack11lll11lll_opy_ = datetime.utcnow()
                      bstack1ll1ll11_opy_ = bstack11lll11lll_opy_.strftime(bstack11l1l11_opy_ (u"ࠦࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࠯ࠧࡩࠤ࡚࡚ࡃࠣஇ"))
                      test_id = os.environ.get(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪஈ")) if os.environ.get(bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫஉ")) else bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤஊ"))
                      payload = {
                          bstack11l1l11_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠧ஋"): bstack11l1l11_opy_ (u"ࠤࡶࡨࡰࡥࡥࡷࡧࡱࡸࡸࠨ஌"),
                          bstack11l1l11_opy_ (u"ࠥࡨࡦࡺࡡࠣ஍"): {
                              bstack11l1l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡪࡸࡦࡤࡻࡵࡪࡦࠥஎ"): test_id,
                              bstack11l1l11_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡩࡥࡤࡢࡻࠥஏ"): bstack1ll1ll11_opy_,
                              bstack11l1l11_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࠥஐ"): bstack11l1l11_opy_ (u"ࠢࡔࡆࡎࡊࡪࡧࡴࡶࡴࡨࡔࡪࡸࡦࡰࡴࡰࡥࡳࡩࡥࠣ஑"),
                              bstack11l1l11_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟࡫ࡵࡲࡲࠧஒ"): {
                                  bstack11l1l11_opy_ (u"ࠤࡰࡩࡦࡹࡵࡳࡧࡶࠦஓ"): data,
                                  bstack11l1l11_opy_ (u"ࠥࡷࡩࡱࡒࡶࡰࡌࡨࠧஔ"): bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠦࡸࡪ࡫ࡓࡷࡱࡍࡩࠨக"))
                              },
                              bstack11l1l11_opy_ (u"ࠧࡻࡳࡦࡴࡢࡨࡦࡺࡡࠣ஖"): bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠨࡵࡴࡧࡵࡒࡦࡳࡥࠣ஗")),
                              bstack11l1l11_opy_ (u"ࠢࡩࡱࡶࡸࡤ࡯࡮ࡧࡱࠥ஘"): get_host_info()
                          }
                      }
                      bstack11l1l1l11l_opy_ = bstack111ll1l1ll_opy_(cli.config, [bstack11l1l11_opy_ (u"ࠣࡣࡳ࡭ࡸࠨங"), bstack11l1l11_opy_ (u"ࠤࡨࡨࡸࡏ࡮ࡴࡶࡵࡹࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴࠢச"), bstack11l1l11_opy_ (u"ࠥࡥࡵ࡯ࠢ஛")], bstack1l1l11llll_opy_)
                      response = bstack11lll1llll_opy_(bstack11l1l11_opy_ (u"ࠦࡕࡕࡓࡕࠤஜ"), bstack11l1l1l11l_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack11l1l11_opy_ (u"ࠧࡊࡡࡵࡣࠣࡷࡪࡴࡴࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡵࡱࠣࡿࢂࠦࡷࡪࡶ࡫ࠤࡩࡧࡴࡢࠢࡾࢁࠧ஝").format(bstack1l1l11llll_opy_, payload))
                      else:
                          logger.debug(bstack11l1l11_opy_ (u"ࠨࡒࡦࡳࡸࡩࡸࡺࠠࡧࡣ࡬ࡰࡪࡪࠠࡧࡱࡵࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡪࡡࡵࡣࠣࡿࢂࠨஞ").format(bstack1l1l11llll_opy_, payload))
          except Exception as e:
              logger.debug(bstack11l1l11_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡴࡤࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࠦࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡࡽࢀࠦட").format(e))
      bstack1l1lll11_opy_()
      bstack1l11llll1l_opy_(bstack1111llll11_opy_, logger)
  except:
    pass
def bstack111l1l1l1l_opy_():
  global bstack11llllll1l_opy_
  global bstack11llll1l11_opy_
  global bstack11ll1ll1ll_opy_
  global bstack1l1ll1l111_opy_
  global bstack1ll111ll11_opy_
  global bstack111l11l11l_opy_
  global CONFIG
  bstack1111ll11ll_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩ஠"))
  if bstack1111ll11ll_opy_ in [bstack11l1l11_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ஡"), bstack11l1l11_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ஢")]:
    bstack111lll1ll1_opy_()
  percy.shutdown()
  if bstack11llllll1l_opy_:
    logger.warning(bstack1ll11llll_opy_.format(str(bstack11llllll1l_opy_)))
  else:
    try:
      bstack1111l111l1_opy_ = bstack11lll1l111_opy_(bstack11l1l11_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪண"), logger)
      if bstack1111l111l1_opy_.get(bstack11l1l11_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪத")) and bstack1111l111l1_opy_.get(bstack11l1l11_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫ஥")).get(bstack11l1l11_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩ஦")):
        logger.warning(bstack1ll11llll_opy_.format(str(bstack1111l111l1_opy_[bstack11l1l11_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭஧")][bstack11l1l11_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫந")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack11l11lllll_opy_.invoke(Events.bstack1lll11llll_opy_)
  logger.info(bstack111ll11l1l_opy_)
  global bstack11l1l11l11_opy_
  if bstack11l1l11l11_opy_:
    bstack111111l11_opy_()
  try:
    with bstack11ll1l11l_opy_:
      bstack111l1l11l1_opy_ = bstack11llll1l11_opy_.copy()
    for driver in bstack111l1l11l1_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1l1lll11l_opy_)
  if bstack111l11l11l_opy_ == bstack11l1l11_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩன"):
    bstack1ll111ll11_opy_ = bstack1ll11lll1_opy_(bstack11l1l11_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬப"))
  if bstack111l11l11l_opy_ == bstack11l1l11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ஫") and len(bstack1l1ll1l111_opy_) == 0:
    bstack1l1ll1l111_opy_ = bstack1ll11lll1_opy_(bstack11l1l11_opy_ (u"࠭ࡰࡸࡡࡳࡽࡹ࡫ࡳࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫ஬"))
    if len(bstack1l1ll1l111_opy_) == 0:
      bstack1l1ll1l111_opy_ = bstack1ll11lll1_opy_(bstack11l1l11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡱࡲࡳࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭஭"))
  bstack1l111ll1ll_opy_ = bstack11l1l11_opy_ (u"ࠨࠩம")
  if len(bstack11ll1ll1ll_opy_) > 0:
    bstack1l111ll1ll_opy_ = bstack1ll1l11ll1_opy_(bstack11ll1ll1ll_opy_)
  elif len(bstack1l1ll1l111_opy_) > 0:
    bstack1l111ll1ll_opy_ = bstack1ll1l11ll1_opy_(bstack1l1ll1l111_opy_)
  elif len(bstack1ll111ll11_opy_) > 0:
    bstack1l111ll1ll_opy_ = bstack1ll1l11ll1_opy_(bstack1ll111ll11_opy_)
  elif len(bstack11l11111l_opy_) > 0:
    bstack1l111ll1ll_opy_ = bstack1ll1l11ll1_opy_(bstack11l11111l_opy_)
  if bool(bstack1l111ll1ll_opy_):
    bstack11ll111ll1_opy_(bstack1l111ll1ll_opy_)
  else:
    bstack11ll111ll1_opy_()
  bstack1l11llll1l_opy_(bstack1ll1llllll_opy_, logger)
  if bstack1111ll11ll_opy_ not in [bstack11l1l11_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪய")]:
    bstack1l1111l11l_opy_()
  bstack1ll1111ll_opy_.bstack1l1l1111_opy_(CONFIG)
  if len(bstack1ll111ll11_opy_) > 0:
    sys.exit(len(bstack1ll111ll11_opy_))
def bstack111lllll11_opy_(bstack1ll1lll1l_opy_, frame):
  global bstack111111ll_opy_
  logger.error(bstack1l1ll11l1l_opy_)
  bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡒࡴ࠭ர"), bstack1ll1lll1l_opy_)
  if hasattr(signal, bstack11l1l11_opy_ (u"ࠫࡘ࡯ࡧ࡯ࡣ࡯ࡷࠬற")):
    bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬல"), signal.Signals(bstack1ll1lll1l_opy_).name)
  else:
    bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭ள"), bstack11l1l11_opy_ (u"ࠧࡔࡋࡊ࡙ࡓࡑࡎࡐ࡙ࡑࠫழ"))
  if cli.is_running():
    bstack11l11lllll_opy_.invoke(Events.bstack1lll11llll_opy_)
  bstack1111ll11ll_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩவ"))
  if bstack1111ll11ll_opy_ == bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩஶ") and not cli.is_enabled(CONFIG):
    bstack1l1lll1l_opy_.stop(bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪஷ")))
  bstack111l1l1l1l_opy_()
  sys.exit(1)
def bstack1l1lllll11_opy_(err):
  logger.critical(bstack11l111l1l1_opy_.format(str(err)))
  bstack11ll111ll1_opy_(bstack11l111l1l1_opy_.format(str(err)), True)
  atexit.unregister(bstack111l1l1l1l_opy_)
  bstack111lll1ll1_opy_()
  sys.exit(1)
def bstack1l111lll11_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack11ll111ll1_opy_(message, True)
  atexit.unregister(bstack111l1l1l1l_opy_)
  bstack111lll1ll1_opy_()
  sys.exit(1)
def bstack1llll1ll11_opy_():
  global CONFIG
  global bstack11l111ll1_opy_
  global bstack1l11lll1ll_opy_
  global bstack11l1l1ll1_opy_
  CONFIG = bstack1ll1l11111_opy_()
  load_dotenv(CONFIG.get(bstack11l1l11_opy_ (u"ࠫࡪࡴࡶࡇ࡫࡯ࡩࠬஸ")))
  bstack1l11l1l1l_opy_()
  bstack11l11l11l_opy_()
  CONFIG = bstack1ll1ll1111_opy_(CONFIG)
  update(CONFIG, bstack1l11lll1ll_opy_)
  update(CONFIG, bstack11l111ll1_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack11ll1l1l1l_opy_(CONFIG)
  bstack11l1l1ll1_opy_ = bstack1l1l11l1ll_opy_(CONFIG)
  os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨஹ")] = bstack11l1l1ll1_opy_.__str__().lower()
  bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ஺"), bstack11l1l1ll1_opy_)
  if (bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ஻") in CONFIG and bstack11l1l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ஼") in bstack11l111ll1_opy_) or (
          bstack11l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ஽") in CONFIG and bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ா") not in bstack1l11lll1ll_opy_):
    if os.getenv(bstack11l1l11_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨி")):
      CONFIG[bstack11l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧீ")] = os.getenv(bstack11l1l11_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪு"))
    else:
      if not CONFIG.get(bstack11l1l11_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠥூ"), bstack11l1l11_opy_ (u"ࠣࠤ௃")) in bstack1ll1l1l1ll_opy_:
        bstack1111lll11l_opy_()
  elif (bstack11l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௄") not in CONFIG and bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ௅") in CONFIG) or (
          bstack11l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧெ") in bstack1l11lll1ll_opy_ and bstack11l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨே") not in bstack11l111ll1_opy_):
    del (CONFIG[bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨை")])
  if bstack1l11ll111l_opy_(CONFIG):
    bstack1l1lllll11_opy_(bstack11ll1llll_opy_)
  Config.bstack1111lll1_opy_().set_property(bstack11l1l11_opy_ (u"ࠢࡶࡵࡨࡶࡓࡧ࡭ࡦࠤ௉"), CONFIG[bstack11l1l11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪொ")])
  bstack1l11l11ll_opy_()
  bstack1lllll1lll_opy_()
  if bstack11l1l1111l_opy_ and not CONFIG.get(bstack11l1l11_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠧோ"), bstack11l1l11_opy_ (u"ࠥࠦௌ")) in bstack1ll1l1l1ll_opy_:
    CONFIG[bstack11l1l11_opy_ (u"ࠫࡦࡶࡰࠨ்")] = bstack11ll1111l1_opy_(CONFIG)
    logger.info(bstack1ll11ll11_opy_.format(CONFIG[bstack11l1l11_opy_ (u"ࠬࡧࡰࡱࠩ௎")]))
  if not bstack11l1l1ll1_opy_:
    CONFIG[bstack11l1l11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ௏")] = [{}]
def bstack11111l1ll1_opy_(config, bstack1ll1l1lll_opy_):
  global CONFIG
  global bstack11l1l1111l_opy_
  CONFIG = config
  bstack11l1l1111l_opy_ = bstack1ll1l1lll_opy_
def bstack1lllll1lll_opy_():
  global CONFIG
  global bstack11l1l1111l_opy_
  if bstack11l1l11_opy_ (u"ࠧࡢࡲࡳࠫௐ") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l111lll11_opy_(e, bstack1111l111ll_opy_)
    bstack11l1l1111l_opy_ = True
    bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ௑"), True)
def bstack11ll1111l1_opy_(config):
  bstack11ll1ll111_opy_ = bstack11l1l11_opy_ (u"ࠩࠪ௒")
  app = config[bstack11l1l11_opy_ (u"ࠪࡥࡵࡶࠧ௓")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack11ll1l1l11_opy_:
      if os.path.exists(app):
        bstack11ll1ll111_opy_ = bstack111l111l11_opy_(config, app)
      elif bstack11l1lll1ll_opy_(app):
        bstack11ll1ll111_opy_ = app
      else:
        bstack1l1lllll11_opy_(bstack1l1111ll1_opy_.format(app))
    else:
      if bstack11l1lll1ll_opy_(app):
        bstack11ll1ll111_opy_ = app
      elif os.path.exists(app):
        bstack11ll1ll111_opy_ = bstack111l111l11_opy_(app)
      else:
        bstack1l1lllll11_opy_(bstack11lll1lll1_opy_)
  else:
    if len(app) > 2:
      bstack1l1lllll11_opy_(bstack11llll11l1_opy_)
    elif len(app) == 2:
      if bstack11l1l11_opy_ (u"ࠫࡵࡧࡴࡩࠩ௔") in app and bstack11l1l11_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ௕") in app:
        if os.path.exists(app[bstack11l1l11_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ௖")]):
          bstack11ll1ll111_opy_ = bstack111l111l11_opy_(config, app[bstack11l1l11_opy_ (u"ࠧࡱࡣࡷ࡬ࠬௗ")], app[bstack11l1l11_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫ௘")])
        else:
          bstack1l1lllll11_opy_(bstack1l1111ll1_opy_.format(app))
      else:
        bstack1l1lllll11_opy_(bstack11llll11l1_opy_)
    else:
      for key in app:
        if key in bstack1l11lllll_opy_:
          if key == bstack11l1l11_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ௙"):
            if os.path.exists(app[key]):
              bstack11ll1ll111_opy_ = bstack111l111l11_opy_(config, app[key])
            else:
              bstack1l1lllll11_opy_(bstack1l1111ll1_opy_.format(app))
          else:
            bstack11ll1ll111_opy_ = app[key]
        else:
          bstack1l1lllll11_opy_(bstack111l1lll1_opy_)
  return bstack11ll1ll111_opy_
def bstack11l1lll1ll_opy_(bstack11ll1ll111_opy_):
  import re
  bstack1l111l1ll_opy_ = re.compile(bstack11l1l11_opy_ (u"ࡵࠦࡣࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥ௚"))
  bstack11llllllll_opy_ = re.compile(bstack11l1l11_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬ࠲࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰ࠤࠣ௛"))
  if bstack11l1l11_opy_ (u"ࠬࡨࡳ࠻࠱࠲ࠫ௜") in bstack11ll1ll111_opy_ or re.fullmatch(bstack1l111l1ll_opy_, bstack11ll1ll111_opy_) or re.fullmatch(bstack11llllllll_opy_, bstack11ll1ll111_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack1l1111llll_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack111l111l11_opy_(config, path, bstack11l1ll1ll_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11l1l11_opy_ (u"࠭ࡲࡣࠩ௝")).read()).hexdigest()
  bstack1ll1111ll1_opy_ = bstack111lll11ll_opy_(md5_hash)
  bstack11ll1ll111_opy_ = None
  if bstack1ll1111ll1_opy_:
    logger.info(bstack1lllll1111_opy_.format(bstack1ll1111ll1_opy_, md5_hash))
    return bstack1ll1111ll1_opy_
  bstack1l11lll1l_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack11l1l11_opy_ (u"ࠧࡧ࡫࡯ࡩࠬ௞"): (os.path.basename(path), open(os.path.abspath(path), bstack11l1l11_opy_ (u"ࠨࡴࡥࠫ௟")), bstack11l1l11_opy_ (u"ࠩࡷࡩࡽࡺ࠯ࡱ࡮ࡤ࡭ࡳ࠭௠")),
      bstack11l1l11_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭௡"): bstack11l1ll1ll_opy_
    }
  )
  response = requests.post(bstack1lllllllll_opy_, data=multipart_data,
                           headers={bstack11l1l11_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ௢"): multipart_data.content_type},
                           auth=(config[bstack11l1l11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ௣")], config[bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ௤")]))
  try:
    res = json.loads(response.text)
    bstack11ll1ll111_opy_ = res[bstack11l1l11_opy_ (u"ࠧࡢࡲࡳࡣࡺࡸ࡬ࠨ௥")]
    logger.info(bstack111lll1l1l_opy_.format(bstack11ll1ll111_opy_))
    bstack11l1ll1ll1_opy_(md5_hash, bstack11ll1ll111_opy_)
    cli.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠣࡪࡷࡸࡵࡀࡵࡱ࡮ࡲࡥࡩࡥࡡࡱࡲࠥ௦"), datetime.datetime.now() - bstack1l11lll1l_opy_)
  except ValueError as err:
    bstack1l1lllll11_opy_(bstack11l1ll1l1l_opy_.format(str(err)))
  return bstack11ll1ll111_opy_
def bstack1l11l11ll_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1111l1l1l1_opy_
  bstack1lll1l1l1_opy_ = 1
  bstack111l1l11l_opy_ = 1
  if bstack11l1l11_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ௧") in CONFIG:
    bstack111l1l11l_opy_ = CONFIG[bstack11l1l11_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ௨")]
  else:
    bstack111l1l11l_opy_ = bstack1l1l111l11_opy_(framework_name, args) or 1
  if bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ௩") in CONFIG:
    bstack1lll1l1l1_opy_ = len(CONFIG[bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ௪")])
  bstack1111l1l1l1_opy_ = int(bstack111l1l11l_opy_) * int(bstack1lll1l1l1_opy_)
def bstack1l1l111l11_opy_(framework_name, args):
  if framework_name == bstack1l111ll1l1_opy_ and args and bstack11l1l11_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ௫") in args:
      bstack1ll1ll1ll_opy_ = args.index(bstack11l1l11_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬ௬"))
      return int(args[bstack1ll1ll1ll_opy_ + 1]) or 1
  return 1
def bstack111lll11ll_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l1l11_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫ௭"))
    bstack111lllll1_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠩࢁࠫ௮")), bstack11l1l11_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ௯"), bstack11l1l11_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬ௰"))
    if os.path.exists(bstack111lllll1_opy_):
      try:
        bstack111lll11l1_opy_ = json.load(open(bstack111lllll1_opy_, bstack11l1l11_opy_ (u"ࠬࡸࡢࠨ௱")))
        if md5_hash in bstack111lll11l1_opy_:
          bstack1l1lll11l1_opy_ = bstack111lll11l1_opy_[md5_hash]
          bstack1l11ll1l1l_opy_ = datetime.datetime.now()
          bstack11l11lll1_opy_ = datetime.datetime.strptime(bstack1l1lll11l1_opy_[bstack11l1l11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ௲")], bstack11l1l11_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫ௳"))
          if (bstack1l11ll1l1l_opy_ - bstack11l11lll1_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack1l1lll11l1_opy_[bstack11l1l11_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭௴")]):
            return None
          return bstack1l1lll11l1_opy_[bstack11l1l11_opy_ (u"ࠩ࡬ࡨࠬ௵")]
      except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡑࡉ࠻ࠠࡩࡣࡶ࡬ࠥ࡬ࡩ࡭ࡧ࠽ࠤࢀࢃࠧ௶").format(str(e)))
    return None
  bstack111lllll1_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠫࢃ࠭௷")), bstack11l1l11_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ௸"), bstack11l1l11_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧ௹"))
  lock_file = bstack111lllll1_opy_ + bstack11l1l11_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ࠭௺")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111lllll1_opy_):
        with open(bstack111lllll1_opy_, bstack11l1l11_opy_ (u"ࠨࡴࠪ௻")) as f:
          content = f.read().strip()
          if content:
            bstack111lll11l1_opy_ = json.loads(content)
            if md5_hash in bstack111lll11l1_opy_:
              bstack1l1lll11l1_opy_ = bstack111lll11l1_opy_[md5_hash]
              bstack1l11ll1l1l_opy_ = datetime.datetime.now()
              bstack11l11lll1_opy_ = datetime.datetime.strptime(bstack1l1lll11l1_opy_[bstack11l1l11_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ௼")], bstack11l1l11_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧ௽"))
              if (bstack1l11ll1l1l_opy_ - bstack11l11lll1_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack1l1lll11l1_opy_[bstack11l1l11_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ௾")]):
                return None
              return bstack1l1lll11l1_opy_[bstack11l1l11_opy_ (u"ࠬ࡯ࡤࠨ௿")]
      return None
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡽࡩࡵࡪࠣࡪ࡮ࡲࡥࠡ࡮ࡲࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨ࠻ࠢࡾࢁࠬఀ").format(str(e)))
    return None
def bstack11l1ll1ll1_opy_(md5_hash, bstack11ll1ll111_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l1l11_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠢࡱࡳࡹࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡥࡥࡸ࡯ࡣࠡࡨ࡬ࡰࡪࠦ࡯ࡱࡧࡵࡥࡹ࡯࡯࡯ࡵࠪఁ"))
    bstack1l1l1ll1l_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠨࢀࠪం")), bstack11l1l11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩః"))
    if not os.path.exists(bstack1l1l1ll1l_opy_):
      os.makedirs(bstack1l1l1ll1l_opy_)
    bstack111lllll1_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠪࢂࠬఄ")), bstack11l1l11_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఅ"), bstack11l1l11_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ఆ"))
    bstack111l1l11ll_opy_ = {
      bstack11l1l11_opy_ (u"࠭ࡩࡥࠩఇ"): bstack11ll1ll111_opy_,
      bstack11l1l11_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪఈ"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l1l11_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬఉ")),
      bstack11l1l11_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧఊ"): str(__version__)
    }
    try:
      bstack111lll11l1_opy_ = {}
      if os.path.exists(bstack111lllll1_opy_):
        bstack111lll11l1_opy_ = json.load(open(bstack111lllll1_opy_, bstack11l1l11_opy_ (u"ࠪࡶࡧ࠭ఋ")))
      bstack111lll11l1_opy_[md5_hash] = bstack111l1l11ll_opy_
      with open(bstack111lllll1_opy_, bstack11l1l11_opy_ (u"ࠦࡼ࠱ࠢఌ")) as outfile:
        json.dump(bstack111lll11l1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11l1l11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡺࡶࡤࡢࡶ࡬ࡲ࡬ࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨࠡࡨ࡬ࡰࡪࡀࠠࡼࡿࠪ఍").format(str(e)))
    return
  bstack1l1l1ll1l_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"࠭ࡾࠨఎ")), bstack11l1l11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧఏ"))
  if not os.path.exists(bstack1l1l1ll1l_opy_):
    os.makedirs(bstack1l1l1ll1l_opy_)
  bstack111lllll1_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠨࢀࠪఐ")), bstack11l1l11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ఑"), bstack11l1l11_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫఒ"))
  lock_file = bstack111lllll1_opy_ + bstack11l1l11_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪఓ")
  bstack111l1l11ll_opy_ = {
    bstack11l1l11_opy_ (u"ࠬ࡯ࡤࠨఔ"): bstack11ll1ll111_opy_,
    bstack11l1l11_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩక"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l1l11_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫఖ")),
    bstack11l1l11_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭గ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack111lll11l1_opy_ = {}
      if os.path.exists(bstack111lllll1_opy_):
        with open(bstack111lllll1_opy_, bstack11l1l11_opy_ (u"ࠩࡵࠫఘ")) as f:
          content = f.read().strip()
          if content:
            bstack111lll11l1_opy_ = json.loads(content)
      bstack111lll11l1_opy_[md5_hash] = bstack111l1l11ll_opy_
      with open(bstack111lllll1_opy_, bstack11l1l11_opy_ (u"ࠥࡻࠧఙ")) as outfile:
        json.dump(bstack111lll11l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡻ࡮ࡺࡨࠡࡨ࡬ࡰࡪࠦ࡬ࡰࡥ࡮࡭ࡳ࡭ࠠࡧࡱࡵࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࠦࡵࡱࡦࡤࡸࡪࡀࠠࡼࡿࠪచ").format(str(e)))
def bstack1l111l111l_opy_(self):
  return
def bstack11lll11l1_opy_(self):
  return
def bstack1111l11l1l_opy_():
  global bstack1l1ll1l11l_opy_
  bstack1l1ll1l11l_opy_ = True
@measure(event_name=EVENTS.bstack1lll1111l1_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack11lll111ll_opy_(self):
  global bstack11l11l1ll_opy_
  global bstack11ll1l1111_opy_
  global bstack1111llll1l_opy_
  try:
    if bstack11l1l11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬఛ") in bstack11l11l1ll_opy_ and self.session_id != None and bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪజ"), bstack11l1l11_opy_ (u"ࠧࠨఝ")) != bstack11l1l11_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩఞ"):
      bstack1ll1l111l1_opy_ = bstack11l1l11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩట") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l1l11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪఠ")
      if bstack1ll1l111l1_opy_ == bstack11l1l11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫడ"):
        bstack1ll111ll1l_opy_(logger)
      if self != None:
        bstack11ll1111ll_opy_(self, bstack1ll1l111l1_opy_, bstack11l1l11_opy_ (u"ࠬ࠲ࠠࠨఢ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11l1l11_opy_ (u"࠭ࠧణ")
    if bstack11l1l11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧత") in bstack11l11l1ll_opy_ and getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧథ"), None):
      bstack11111l11_opy_.bstack11111ll1_opy_(self, bstack1llll111l1_opy_, logger, wait=True)
    if bstack11l1l11_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩద") in bstack11l11l1ll_opy_:
      if not threading.currentThread().behave_test_status:
        bstack11ll1111ll_opy_(self, bstack11l1l11_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥధ"))
      bstack111l1lllll_opy_.bstack11ll11111l_opy_(self)
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧన") + str(e))
  bstack1111llll1l_opy_(self)
  self.session_id = None
def bstack11lll1l11l_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1ll111l11l_opy_
    global bstack11l11l1ll_opy_
    command_executor = kwargs.get(bstack11l1l11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠨ఩"), bstack11l1l11_opy_ (u"࠭ࠧప"))
    bstack11llll1111_opy_ = False
    if type(command_executor) == str and bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪఫ") in command_executor:
      bstack11llll1111_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫబ") in str(getattr(command_executor, bstack11l1l11_opy_ (u"ࠩࡢࡹࡷࡲࠧభ"), bstack11l1l11_opy_ (u"ࠪࠫమ"))):
      bstack11llll1111_opy_ = True
    else:
      kwargs = bstack111l1lll_opy_.bstack11l1l1lll1_opy_(bstack111l1l1111_opy_=kwargs, config=CONFIG)
      return bstack111ll11l11_opy_(self, *args, **kwargs)
    if bstack11llll1111_opy_:
      bstack1l1l111111_opy_ = bstack1l11l1l11l_opy_.bstack1l111l11l1_opy_(CONFIG, bstack11l11l1ll_opy_)
      if kwargs.get(bstack11l1l11_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬయ")):
        kwargs[bstack11l1l11_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ర")] = bstack1ll111l11l_opy_(kwargs[bstack11l1l11_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧఱ")], bstack11l11l1ll_opy_, CONFIG, bstack1l1l111111_opy_)
      elif kwargs.get(bstack11l1l11_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧల")):
        kwargs[bstack11l1l11_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨళ")] = bstack1ll111l11l_opy_(kwargs[bstack11l1l11_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩఴ")], bstack11l11l1ll_opy_, CONFIG, bstack1l1l111111_opy_)
  except Exception as e:
    logger.error(bstack11l1l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡘࡊࡋࠡࡥࡤࡴࡸࡀࠠࡼࡿࠥవ").format(str(e)))
  return bstack111ll11l11_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack11l1l1llll_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1ll1ll11l_opy_(self, command_executor=bstack11l1l11_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳࠶࠸࠷࠯࠲࠱࠴࠳࠷࠺࠵࠶࠷࠸ࠧశ"), *args, **kwargs):
  global bstack11ll1l1111_opy_
  global bstack11llll1l11_opy_
  bstack111llllll_opy_ = bstack11lll1l11l_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1ll1l1ll_opy_.on():
    return bstack111llllll_opy_
  try:
    logger.debug(bstack11l1l11_opy_ (u"ࠬࡉ࡯࡮࡯ࡤࡲࡩࠦࡅࡹࡧࡦࡹࡹࡵࡲࠡࡹ࡫ࡩࡳࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥ࡬ࡡ࡭ࡵࡨࠤ࠲ࠦࡻࡾࠩష").format(str(command_executor)))
    logger.debug(bstack11l1l11_opy_ (u"࠭ࡈࡶࡤ࡙ࠣࡗࡒࠠࡪࡵࠣ࠱ࠥࢁࡽࠨస").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪహ") in command_executor._url:
      bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ఺"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ఻") in command_executor):
    bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱ఼ࠫ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack11ll111111_opy_ = getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥࠬఽ"), None)
  bstack11ll111l11_opy_ = {}
  if self.capabilities is not None:
    bstack11ll111l11_opy_[bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫా")] = self.capabilities.get(bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫి"))
    bstack11ll111l11_opy_[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩీ")] = self.capabilities.get(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩు"))
    bstack11ll111l11_opy_[bstack11l1l11_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࠪూ")] = self.capabilities.get(bstack11l1l11_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨృ"))
  if CONFIG.get(bstack11l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫౄ"), False) and bstack111l1lll_opy_.bstack1lll1l11ll_opy_(bstack11ll111l11_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack11l1l11_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ౅") in bstack11l11l1ll_opy_ or bstack11l1l11_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬె") in bstack11l11l1ll_opy_:
    bstack1l1lll1l_opy_.bstack111ll11ll1_opy_(self)
  if bstack11l1l11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧే") in bstack11l11l1ll_opy_ and bstack11ll111111_opy_ and bstack11ll111111_opy_.get(bstack11l1l11_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨై"), bstack11l1l11_opy_ (u"ࠩࠪ౉")) == bstack11l1l11_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫొ"):
    bstack1l1lll1l_opy_.bstack111ll11ll1_opy_(self)
  bstack11ll1l1111_opy_ = self.session_id
  with bstack11ll1l11l_opy_:
    bstack11llll1l11_opy_.append(self)
  return bstack111llllll_opy_
def bstack111ll1lll1_opy_(args):
  return bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠬో") in str(args)
def bstack11l1l1ll11_opy_(self, driver_command, *args, **kwargs):
  global bstack1ll1lllll1_opy_
  global bstack11l1ll1lll_opy_
  bstack1111lll111_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩౌ"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack11l1l11_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱ్ࠬ"), None)
  bstack11l1111lll_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ౎"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ౏"), None)
  bstack111ll1111l_opy_ = getattr(self, bstack11l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩ౐"), None) != None and getattr(self, bstack11l1l11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ౑"), None) == True
  if not bstack11l1ll1lll_opy_ and bstack11l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ౒") in CONFIG and CONFIG[bstack11l1l11_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ౓")] == True and bstack11l1ll11ll_opy_.bstack1ll11l1l11_opy_(driver_command) and (bstack111ll1111l_opy_ or bstack1111lll111_opy_ or bstack11l1111lll_opy_) and not bstack111ll1lll1_opy_(args):
    try:
      bstack11l1ll1lll_opy_ = True
      logger.debug(bstack11l1l11_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࢁࡽࠨ౔").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11l1l11_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡪࡸࡦࡰࡴࡰࠤࡸࡩࡡ࡯ࠢࡾࢁౕࠬ").format(str(err)))
    bstack11l1ll1lll_opy_ = False
  response = bstack1ll1lllll1_opy_(self, driver_command, *args, **kwargs)
  if (bstack11l1l11_opy_ (u"ࠨࡴࡲࡦࡴࡺౖࠧ") in str(bstack11l11l1ll_opy_).lower() or bstack11l1l11_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ౗") in str(bstack11l11l1ll_opy_).lower()) and bstack1ll1l1ll_opy_.on():
    try:
      if driver_command == bstack11l1l11_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧౘ"):
        bstack1l1lll1l_opy_.bstack1l11l1lll_opy_({
            bstack11l1l11_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࠪౙ"): response[bstack11l1l11_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫౚ")],
            bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭౛"): bstack1l1lll1l_opy_.current_test_uuid() if bstack1l1lll1l_opy_.current_test_uuid() else bstack1ll1l1ll_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1l1lllll1_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1l11l1llll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack11ll1l1111_opy_
  global bstack1l1111lll1_opy_
  global bstack1111ll11l_opy_
  global bstack11ll1ll1l1_opy_
  global bstack111l11111l_opy_
  global bstack11l11l1ll_opy_
  global bstack111ll11l11_opy_
  global bstack11llll1l11_opy_
  global bstack1l11ll1lll_opy_
  global bstack1llll111l1_opy_
  if os.getenv(bstack11l1l11_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ౜")) is not None and bstack111l1lll_opy_.bstack1llllll11l_opy_(CONFIG) is None:
    CONFIG[bstack11l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨౝ")] = True
  CONFIG[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ౞")] = str(bstack11l11l1ll_opy_) + str(__version__)
  bstack11llllll1_opy_ = os.environ[bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ౟")]
  bstack1l1l111111_opy_ = bstack1l11l1l11l_opy_.bstack1l111l11l1_opy_(CONFIG, bstack11l11l1ll_opy_)
  CONFIG[bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧౠ")] = bstack11llllll1_opy_
  CONFIG[bstack11l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧౡ")] = bstack1l1l111111_opy_
  if CONFIG.get(bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ౢ"),bstack11l1l11_opy_ (u"ࠧࠨౣ")) and bstack11l1l11_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ౤") in bstack11l11l1ll_opy_:
    CONFIG[bstack11l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ౥")].pop(bstack11l1l11_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ౦"), None)
    CONFIG[bstack11l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ౧")].pop(bstack11l1l11_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ౨"), None)
  command_executor = bstack1ll111l1l1_opy_()
  logger.debug(bstack11l1l1111_opy_.format(command_executor))
  proxy = bstack11l1111ll1_opy_(CONFIG, proxy)
  bstack11111l11l_opy_ = 0 if bstack1l1111lll1_opy_ < 0 else bstack1l1111lll1_opy_
  try:
    if bstack11ll1ll1l1_opy_ is True:
      bstack11111l11l_opy_ = int(multiprocessing.current_process().name)
    elif bstack111l11111l_opy_ is True:
      bstack11111l11l_opy_ = int(threading.current_thread().name)
  except:
    bstack11111l11l_opy_ = 0
  bstack11111ll11_opy_ = bstack111ll1ll11_opy_(CONFIG, bstack11111l11l_opy_)
  logger.debug(bstack1ll1lll1l1_opy_.format(str(bstack11111ll11_opy_)))
  if bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ౩") in CONFIG and bstack1lll1ll1l1_opy_(CONFIG[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ౪")]):
    bstack11l1llllll_opy_(bstack11111ll11_opy_)
  if bstack111l1lll_opy_.bstack11l11ll1l_opy_(CONFIG, bstack11111l11l_opy_) and bstack111l1lll_opy_.bstack1ll1ll1l1_opy_(bstack11111ll11_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack111l1lll_opy_.set_capabilities(bstack11111ll11_opy_, CONFIG)
  if desired_capabilities:
    bstack111lll1111_opy_ = bstack1ll1ll1111_opy_(desired_capabilities)
    bstack111lll1111_opy_[bstack11l1l11_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨ౫")] = bstack11ll1lllll_opy_(CONFIG)
    bstack1l111l1l1_opy_ = bstack111ll1ll11_opy_(bstack111lll1111_opy_)
    if bstack1l111l1l1_opy_:
      bstack11111ll11_opy_ = update(bstack1l111l1l1_opy_, bstack11111ll11_opy_)
    desired_capabilities = None
  if options:
    bstack1l1l11ll1l_opy_(options, bstack11111ll11_opy_)
  if not options:
    options = bstack11ll111l1l_opy_(bstack11111ll11_opy_)
  bstack1llll111l1_opy_ = CONFIG.get(bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ౬"))[bstack11111l11l_opy_]
  if proxy and bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪ౭")):
    options.proxy(proxy)
  if options and bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ౮")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack11lll11ll_opy_() < version.parse(bstack11l1l11_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫ౯")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack11111ll11_opy_)
  logger.info(bstack11l1111111_opy_)
  bstack1l1l1111ll_opy_.end(EVENTS.bstack1l11llll1_opy_.value, EVENTS.bstack1l11llll1_opy_.value + bstack11l1l11_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ౰"), EVENTS.bstack1l11llll1_opy_.value + bstack11l1l11_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ౱"), status=True, failure=None, test_name=bstack1111ll11l_opy_)
  if bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡳࡶࡴ࡬ࡩ࡭ࡧࠪ౲") in kwargs:
    del kwargs[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡴࡷࡵࡦࡪ࡮ࡨࠫ౳")]
  try:
    if bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪ౴")):
      bstack111ll11l11_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪ౵")):
      bstack111ll11l11_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬ౶")):
      bstack111ll11l11_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack111ll11l11_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack111llll11l_opy_:
    logger.error(bstack1l1ll11lll_opy_.format(bstack11l1l11_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠬ౷"), str(bstack111llll11l_opy_)))
    raise bstack111llll11l_opy_
  if bstack111l1lll_opy_.bstack11l11ll1l_opy_(CONFIG, bstack11111l11l_opy_) and bstack111l1lll_opy_.bstack1ll1ll1l1_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ౸")][bstack11l1l11_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ౹")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack111l1lll_opy_.set_capabilities(bstack11111ll11_opy_, CONFIG)
  try:
    bstack111ll11lll_opy_ = bstack11l1l11_opy_ (u"ࠩࠪ౺")
    if bstack11lll11ll_opy_() >= version.parse(bstack11l1l11_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࡤ࠴ࠫ౻")):
      if self.caps is not None:
        bstack111ll11lll_opy_ = self.caps.get(bstack11l1l11_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦ౼"))
    else:
      if self.capabilities is not None:
        bstack111ll11lll_opy_ = self.capabilities.get(bstack11l1l11_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧ౽"))
    if bstack111ll11lll_opy_:
      bstack11l1ll111_opy_(bstack111ll11lll_opy_)
      if bstack11lll11ll_opy_() <= version.parse(bstack11l1l11_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭౾")):
        self.command_executor._url = bstack11l1l11_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣ౿") + bstack1ll1l11l1l_opy_ + bstack11l1l11_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧಀ")
      else:
        self.command_executor._url = bstack11l1l11_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦಁ") + bstack111ll11lll_opy_ + bstack11l1l11_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦಂ")
      logger.debug(bstack11111ll111_opy_.format(bstack111ll11lll_opy_))
    else:
      logger.debug(bstack111lllll1l_opy_.format(bstack11l1l11_opy_ (u"ࠦࡔࡶࡴࡪ࡯ࡤࡰࠥࡎࡵࡣࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧಃ")))
  except Exception as e:
    logger.debug(bstack111lllll1l_opy_.format(e))
  if bstack11l1l11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ಄") in bstack11l11l1ll_opy_:
    bstack1l11l111l1_opy_(bstack1l1111lll1_opy_, bstack1l11ll1lll_opy_)
  bstack11ll1l1111_opy_ = self.session_id
  if bstack11l1l11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ಅ") in bstack11l11l1ll_opy_ or bstack11l1l11_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧಆ") in bstack11l11l1ll_opy_ or bstack11l1l11_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧಇ") in bstack11l11l1ll_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack11ll111111_opy_ = getattr(threading.current_thread(), bstack11l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪಈ"), None)
  if bstack11l1l11_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪಉ") in bstack11l11l1ll_opy_ or bstack11l1l11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪಊ") in bstack11l11l1ll_opy_:
    bstack1l1lll1l_opy_.bstack111ll11ll1_opy_(self)
  if bstack11l1l11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬಋ") in bstack11l11l1ll_opy_ and bstack11ll111111_opy_ and bstack11ll111111_opy_.get(bstack11l1l11_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ಌ"), bstack11l1l11_opy_ (u"ࠧࠨ಍")) == bstack11l1l11_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩಎ"):
    bstack1l1lll1l_opy_.bstack111ll11ll1_opy_(self)
  with bstack11ll1l11l_opy_:
    bstack11llll1l11_opy_.append(self)
  if bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಏ") in CONFIG and bstack11l1l11_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨಐ") in CONFIG[bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಑")][bstack11111l11l_opy_]:
    bstack1111ll11l_opy_ = CONFIG[bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಒ")][bstack11111l11l_opy_][bstack11l1l11_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫಓ")]
  logger.debug(bstack1ll1l1ll1_opy_.format(bstack11ll1l1111_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack111l11l1ll_opy_
    def bstack111l1l1ll1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack11l1ll11l_opy_
      if(bstack11l1l11_opy_ (u"ࠢࡪࡰࡧࡩࡽ࠴ࡪࡴࠤಔ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠨࢀࠪಕ")), bstack11l1l11_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩಖ"), bstack11l1l11_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬಗ")), bstack11l1l11_opy_ (u"ࠫࡼ࠭ಘ")) as fp:
          fp.write(bstack11l1l11_opy_ (u"ࠧࠨಙ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11l1l11_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣಚ")))):
          with open(args[1], bstack11l1l11_opy_ (u"ࠧࡳࠩಛ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11l1l11_opy_ (u"ࠨࡣࡶࡽࡳࡩࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡢࡲࡪࡽࡐࡢࡩࡨࠬࡨࡵ࡮ࡵࡧࡻࡸ࠱ࠦࡰࡢࡩࡨࠤࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠧಜ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1l111ll11l_opy_)
            if bstack11l1l11_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ಝ") in CONFIG and str(CONFIG[bstack11l1l11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧಞ")]).lower() != bstack11l1l11_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪಟ"):
                bstack1ll1ll1l1l_opy_ = bstack111l11l1ll_opy_()
                bstack1l1111l1l1_opy_ = bstack11l1l11_opy_ (u"ࠬ࠭ࠧࠋ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࠎࡨࡵ࡮ࡴࡶࠣࡦࡸࡺࡡࡤ࡭ࡢࡴࡦࡺࡨࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷ࡢࡁࠊࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠱࡞࠽ࠍࡧࡴࡴࡳࡵࠢࡳࡣ࡮ࡴࡤࡦࡺࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠸࡝࠼ࠌࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰ࡶࡰ࡮ࡩࡥࠩ࠲࠯ࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹ࠩ࠼ࠌࡦࡳࡳࡹࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢࠪ࠽ࠍ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡰࡦࡻ࡮ࡤࡪࠣࡁࠥࡧࡳࡺࡰࡦࠤ࠭ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷ࠮ࠦ࠽࠿ࠢࡾࡿࠏࠦࠠ࡭ࡧࡷࠤࡨࡧࡰࡴ࠽ࠍࠤࠥࡺࡲࡺࠢࡾࡿࠏࠦࠠࠡࠢࡦࡥࡵࡹࠠ࠾ࠢࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶ࠭ࡀࠐࠠࠡࡿࢀࠤࡨࡧࡴࡤࡪࠣࠬࡪࡾࠩࠡࡽࡾࠎࠥࠦࠠࠡࡥࡲࡲࡸࡵ࡬ࡦ࠰ࡨࡶࡷࡵࡲࠩࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠽ࠦ࠱ࠦࡥࡹࠫ࠾ࠎࠥࠦࡽࡾࠌࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡦࡽࡡࡪࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡧࡴࡴ࡮ࡦࡥࡷࠬࢀࢁࠊࠡࠢࠣࠤࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴ࠻ࠢࠪࡿࡨࡪࡰࡖࡴ࡯ࢁࠬࠦࠫࠡࡧࡱࡧࡴࡪࡥࡖࡔࡌࡇࡴࡳࡰࡰࡰࡨࡲࡹ࠮ࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡤࡣࡳࡷ࠮࠯ࠬࠋࠢࠣࠤࠥ࠴࠮࠯࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠋࠢࠣࢁࢂ࠯࠻ࠋࡿࢀ࠿ࠏ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯ࠋࠩࠪࠫಠ").format(bstack1ll1ll1l1l_opy_=bstack1ll1ll1l1l_opy_)
            lines.insert(1, bstack1l1111l1l1_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11l1l11_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣಡ")), bstack11l1l11_opy_ (u"ࠧࡸࠩಢ")) as bstack111lll11l_opy_:
              bstack111lll11l_opy_.writelines(lines)
        CONFIG[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪಣ")] = str(bstack11l11l1ll_opy_) + str(__version__)
        bstack11llllll1_opy_ = os.environ[bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧತ")]
        bstack1l1l111111_opy_ = bstack1l11l1l11l_opy_.bstack1l111l11l1_opy_(CONFIG, bstack11l11l1ll_opy_)
        CONFIG[bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ಥ")] = bstack11llllll1_opy_
        CONFIG[bstack11l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ದ")] = bstack1l1l111111_opy_
        bstack11111l11l_opy_ = 0 if bstack1l1111lll1_opy_ < 0 else bstack1l1111lll1_opy_
        try:
          if bstack11ll1ll1l1_opy_ is True:
            bstack11111l11l_opy_ = int(multiprocessing.current_process().name)
          elif bstack111l11111l_opy_ is True:
            bstack11111l11l_opy_ = int(threading.current_thread().name)
        except:
          bstack11111l11l_opy_ = 0
        CONFIG[bstack11l1l11_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧಧ")] = False
        CONFIG[bstack11l1l11_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧನ")] = True
        bstack11111ll11_opy_ = bstack111ll1ll11_opy_(CONFIG, bstack11111l11l_opy_)
        logger.debug(bstack1ll1lll1l1_opy_.format(str(bstack11111ll11_opy_)))
        if CONFIG.get(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ಩")):
          bstack11l1llllll_opy_(bstack11111ll11_opy_)
        if bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಪ") in CONFIG and bstack11l1l11_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧಫ") in CONFIG[bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಬ")][bstack11111l11l_opy_]:
          bstack1111ll11l_opy_ = CONFIG[bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧಭ")][bstack11111l11l_opy_][bstack11l1l11_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪಮ")]
        args.append(os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"࠭ࡾࠨಯ")), bstack11l1l11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧರ"), bstack11l1l11_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪಱ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack11111ll11_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11l1l11_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦಲ"))
      bstack11l1ll11l_opy_ = True
      return bstack11l111l111_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack11111l1ll_opy_(self,
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
    global bstack1l1111lll1_opy_
    global bstack1111ll11l_opy_
    global bstack11ll1ll1l1_opy_
    global bstack111l11111l_opy_
    global bstack11l11l1ll_opy_
    CONFIG[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬಳ")] = str(bstack11l11l1ll_opy_) + str(__version__)
    bstack11llllll1_opy_ = os.environ[bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ಴")]
    bstack1l1l111111_opy_ = bstack1l11l1l11l_opy_.bstack1l111l11l1_opy_(CONFIG, bstack11l11l1ll_opy_)
    CONFIG[bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨವ")] = bstack11llllll1_opy_
    CONFIG[bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨಶ")] = bstack1l1l111111_opy_
    bstack11111l11l_opy_ = 0 if bstack1l1111lll1_opy_ < 0 else bstack1l1111lll1_opy_
    try:
      if bstack11ll1ll1l1_opy_ is True:
        bstack11111l11l_opy_ = int(multiprocessing.current_process().name)
      elif bstack111l11111l_opy_ is True:
        bstack11111l11l_opy_ = int(threading.current_thread().name)
    except:
      bstack11111l11l_opy_ = 0
    CONFIG[bstack11l1l11_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨಷ")] = True
    bstack11111ll11_opy_ = bstack111ll1ll11_opy_(CONFIG, bstack11111l11l_opy_)
    logger.debug(bstack1ll1lll1l1_opy_.format(str(bstack11111ll11_opy_)))
    if CONFIG.get(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬಸ")):
      bstack11l1llllll_opy_(bstack11111ll11_opy_)
    if bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಹ") in CONFIG and bstack11l1l11_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ಺") in CONFIG[bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಻")][bstack11111l11l_opy_]:
      bstack1111ll11l_opy_ = CONFIG[bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ಼")][bstack11111l11l_opy_][bstack11l1l11_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫಽ")]
    import urllib
    import json
    if bstack11l1l11_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫಾ") in CONFIG and str(CONFIG[bstack11l1l11_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬಿ")]).lower() != bstack11l1l11_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨೀ"):
        bstack1111lll11_opy_ = bstack111l11l1ll_opy_()
        bstack1ll1ll1l1l_opy_ = bstack1111lll11_opy_ + urllib.parse.quote(json.dumps(bstack11111ll11_opy_))
    else:
        bstack1ll1ll1l1l_opy_ = bstack11l1l11_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬು") + urllib.parse.quote(json.dumps(bstack11111ll11_opy_))
    browser = self.connect(bstack1ll1ll1l1l_opy_)
    return browser
except Exception as e:
    pass
def bstack11l1l11ll_opy_():
    global bstack11l1ll11l_opy_
    global bstack11l11l1ll_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack11111ll1l1_opy_
        global bstack111111ll_opy_
        if not bstack11l1l1ll1_opy_:
          global bstack11l1lll1l1_opy_
          if not bstack11l1lll1l1_opy_:
            from bstack_utils.helper import bstack1lll11ll1l_opy_, bstack11l1ll11l1_opy_, bstack11l111111l_opy_
            bstack11l1lll1l1_opy_ = bstack1lll11ll1l_opy_()
            bstack11l1ll11l1_opy_(bstack11l11l1ll_opy_)
            bstack1l1l111111_opy_ = bstack1l11l1l11l_opy_.bstack1l111l11l1_opy_(CONFIG, bstack11l11l1ll_opy_)
            bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"ࠦࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡒࡕࡓࡉ࡛ࡃࡕࡡࡐࡅࡕࠨೂ"), bstack1l1l111111_opy_)
          BrowserType.connect = bstack11111ll1l1_opy_
          return
        BrowserType.launch = bstack11111l1ll_opy_
        bstack11l1ll11l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack111l1l1ll1_opy_
      bstack11l1ll11l_opy_ = True
    except Exception as e:
      pass
def bstack1111l1ll1l_opy_(context, bstack1ll1ll111l_opy_):
  try:
    context.page.evaluate(bstack11l1l11_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨೃ"), bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪೄ")+ json.dumps(bstack1ll1ll111l_opy_) + bstack11l1l11_opy_ (u"ࠢࡾࡿࠥ೅"))
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࡀࠠࡼࡿࠥೆ").format(str(e), traceback.format_exc()))
def bstack1lll1lllll_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11l1l11_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥೇ"), bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨೈ") + json.dumps(message) + bstack11l1l11_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧ೉") + json.dumps(level) + bstack11l1l11_opy_ (u"ࠬࢃࡽࠨೊ"))
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾ࠼ࠣࡿࢂࠨೋ").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1l1ll1lll_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1l1l111ll1_opy_(self, url):
  global bstack1ll1lll111_opy_
  try:
    bstack11llll1ll1_opy_(url)
  except Exception as err:
    logger.debug(bstack11l1l1lll_opy_.format(str(err)))
  try:
    bstack1ll1lll111_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack11111l111_opy_):
        bstack11llll1ll1_opy_(url, True)
    except Exception as err:
      logger.debug(bstack11l1l1lll_opy_.format(str(err)))
    raise e
def bstack1111l1l1l_opy_(self):
  global bstack11lll1l1l1_opy_
  bstack11lll1l1l1_opy_ = self
  return
def bstack1l11l1111l_opy_(self):
  global bstack1l11ll11ll_opy_
  bstack1l11ll11ll_opy_ = self
  return
def bstack1llll1l1l1_opy_(test_name, bstack1l1ll1111_opy_):
  global CONFIG
  if percy.bstack1llll11111_opy_() == bstack11l1l11_opy_ (u"ࠢࡵࡴࡸࡩࠧೌ"):
    bstack1l1lll1l1_opy_ = os.path.relpath(bstack1l1ll1111_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1l1lll1l1_opy_)
    bstack111111ll1_opy_ = suite_name + bstack11l1l11_opy_ (u"ࠣ࠯್ࠥ") + test_name
    threading.current_thread().percySessionName = bstack111111ll1_opy_
def bstack111lll1lll_opy_(self, test, *args, **kwargs):
  global bstack11l11l1ll1_opy_
  test_name = None
  bstack1l1ll1111_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1l1ll1111_opy_ = str(test.source)
  bstack1llll1l1l1_opy_(test_name, bstack1l1ll1111_opy_)
  bstack11l11l1ll1_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack11l1l1l1l1_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1ll11l1111_opy_(driver, bstack111111ll1_opy_):
  if not bstack1l1l1ll1l1_opy_ and bstack111111ll1_opy_:
      bstack11ll11l11_opy_ = {
          bstack11l1l11_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ೎"): bstack11l1l11_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ೏"),
          bstack11l1l11_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ೐"): {
              bstack11l1l11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ೑"): bstack111111ll1_opy_
          }
      }
      bstack11l1l1l111_opy_ = bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ೒").format(json.dumps(bstack11ll11l11_opy_))
      driver.execute_script(bstack11l1l1l111_opy_)
  if bstack1ll11l1ll_opy_:
      bstack11lll1111_opy_ = {
          bstack11l1l11_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ೓"): bstack11l1l11_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪ೔"),
          bstack11l1l11_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬೕ"): {
              bstack11l1l11_opy_ (u"ࠪࡨࡦࡺࡡࠨೖ"): bstack111111ll1_opy_ + bstack11l1l11_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭೗"),
              bstack11l1l11_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ೘"): bstack11l1l11_opy_ (u"࠭ࡩ࡯ࡨࡲࠫ೙")
          }
      }
      if bstack1ll11l1ll_opy_.status == bstack11l1l11_opy_ (u"ࠧࡑࡃࡖࡗࠬ೚"):
          bstack1111ll11l1_opy_ = bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭೛").format(json.dumps(bstack11lll1111_opy_))
          driver.execute_script(bstack1111ll11l1_opy_)
          bstack11ll1111ll_opy_(driver, bstack11l1l11_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ೜"))
      elif bstack1ll11l1ll_opy_.status == bstack11l1l11_opy_ (u"ࠪࡊࡆࡏࡌࠨೝ"):
          reason = bstack11l1l11_opy_ (u"ࠦࠧೞ")
          bstack1llllll1l1_opy_ = bstack111111ll1_opy_ + bstack11l1l11_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩ࠭೟")
          if bstack1ll11l1ll_opy_.message:
              reason = str(bstack1ll11l1ll_opy_.message)
              bstack1llllll1l1_opy_ = bstack1llllll1l1_opy_ + bstack11l1l11_opy_ (u"࠭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥ࠭ೠ") + reason
          bstack11lll1111_opy_[bstack11l1l11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪೡ")] = {
              bstack11l1l11_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧೢ"): bstack11l1l11_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨೣ"),
              bstack11l1l11_opy_ (u"ࠪࡨࡦࡺࡡࠨ೤"): bstack1llllll1l1_opy_
          }
          bstack1111ll11l1_opy_ = bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ೥").format(json.dumps(bstack11lll1111_opy_))
          driver.execute_script(bstack1111ll11l1_opy_)
          bstack11ll1111ll_opy_(driver, bstack11l1l11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ೦"), reason)
          bstack11llllll11_opy_(reason, str(bstack1ll11l1ll_opy_), str(bstack1l1111lll1_opy_), logger)
@measure(event_name=EVENTS.bstack1lll1l1lll_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1llll1l1ll_opy_(driver, test):
  if percy.bstack1llll11111_opy_() == bstack11l1l11_opy_ (u"ࠨࡴࡳࡷࡨࠦ೧") and percy.bstack11l1lllll1_opy_() == bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤ೨"):
      bstack1lllll111l_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡲࡨࡶࡨࡿࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ೩"), None)
      bstack1lll1l1l11_opy_(driver, bstack1lllll111l_opy_, test)
  if (bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭೪"), None) and
      bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ೫"), None)) or (
      bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫ೬"), None) and
      bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ೭"), None)):
      logger.info(bstack11l1l11_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠤࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡩࡴࠢࡸࡲࡩ࡫ࡲࡸࡣࡼ࠲ࠥࠨ೮"))
      bstack111l1lll_opy_.bstack11l11l1l_opy_(driver, name=test.name, path=test.source)
def bstack1l1l1l11ll_opy_(test, bstack111111ll1_opy_):
    try:
      bstack1l11lll1l_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack11l1l11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ೯")] = bstack111111ll1_opy_
      if bstack1ll11l1ll_opy_:
        if bstack1ll11l1ll_opy_.status == bstack11l1l11_opy_ (u"ࠨࡒࡄࡗࡘ࠭೰"):
          data[bstack11l1l11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩೱ")] = bstack11l1l11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪೲ")
        elif bstack1ll11l1ll_opy_.status == bstack11l1l11_opy_ (u"ࠫࡋࡇࡉࡍࠩೳ"):
          data[bstack11l1l11_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ೴")] = bstack11l1l11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭೵")
          if bstack1ll11l1ll_opy_.message:
            data[bstack11l1l11_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧ೶")] = str(bstack1ll11l1ll_opy_.message)
      user = CONFIG[bstack11l1l11_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ೷")]
      key = CONFIG[bstack11l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ೸")]
      host = bstack111ll1l1ll_opy_(cli.config, [bstack11l1l11_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ೹"), bstack11l1l11_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ೺"), bstack11l1l11_opy_ (u"ࠧࡧࡰࡪࠤ೻")], bstack11l1l11_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠢ೼"))
      url = bstack11l1l11_opy_ (u"ࠧࡼࡿ࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠯ࡼࡿ࠱࡮ࡸࡵ࡮ࠨ೽").format(host, bstack11ll1l1111_opy_)
      headers = {
        bstack11l1l11_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧ೾"): bstack11l1l11_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬ೿"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡷࡳࡨࡦࡺࡥࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡶࡤࡸࡺࡹࠢഀ"), datetime.datetime.now() - bstack1l11lll1l_opy_)
    except Exception as e:
      logger.error(bstack111l111l1_opy_.format(str(e)))
def bstack1l11111l11_opy_(test, bstack111111ll1_opy_):
  global CONFIG
  global bstack1l11ll11ll_opy_
  global bstack11lll1l1l1_opy_
  global bstack11ll1l1111_opy_
  global bstack1ll11l1ll_opy_
  global bstack1111ll11l_opy_
  global bstack1l111ll11_opy_
  global bstack1l11l1111_opy_
  global bstack111l1llll1_opy_
  global bstack1l11l111ll_opy_
  global bstack11llll1l11_opy_
  global bstack1llll111l1_opy_
  global bstack11l1l1ll1l_opy_
  try:
    if not bstack11ll1l1111_opy_:
      with bstack11l1l1ll1l_opy_:
        bstack1lllll1l11_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠫࢃ࠭ഁ")), bstack11l1l11_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬം"), bstack11l1l11_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨഃ"))
        if os.path.exists(bstack1lllll1l11_opy_):
          with open(bstack1lllll1l11_opy_, bstack11l1l11_opy_ (u"ࠧࡳࠩഄ")) as f:
            content = f.read().strip()
            if content:
              bstack1l1l11lll_opy_ = json.loads(bstack11l1l11_opy_ (u"ࠣࡽࠥഅ") + content + bstack11l1l11_opy_ (u"ࠩࠥࡼࠧࡀࠠࠣࡻࠥࠫആ") + bstack11l1l11_opy_ (u"ࠥࢁࠧഇ"))
              bstack11ll1l1111_opy_ = bstack1l1l11lll_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡶࡪࡧࡤࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡏࡄࡴࠢࡩ࡭ࡱ࡫࠺ࠡࠩഈ") + str(e))
  if bstack11llll1l11_opy_:
    with bstack11ll1l11l_opy_:
      bstack11lll1ll1l_opy_ = bstack11llll1l11_opy_.copy()
    for driver in bstack11lll1ll1l_opy_:
      if bstack11ll1l1111_opy_ == driver.session_id:
        if test:
          bstack1llll1l1ll_opy_(driver, test)
        bstack1ll11l1111_opy_(driver, bstack111111ll1_opy_)
  elif bstack11ll1l1111_opy_:
    bstack1l1l1l11ll_opy_(test, bstack111111ll1_opy_)
  if bstack1l11ll11ll_opy_:
    bstack1l11l1111_opy_(bstack1l11ll11ll_opy_)
  if bstack11lll1l1l1_opy_:
    bstack111l1llll1_opy_(bstack11lll1l1l1_opy_)
  if bstack1l1ll1l11l_opy_:
    bstack1l11l111ll_opy_()
def bstack1ll111l1l_opy_(self, test, *args, **kwargs):
  bstack111111ll1_opy_ = None
  if test:
    bstack111111ll1_opy_ = str(test.name)
  bstack1l11111l11_opy_(test, bstack111111ll1_opy_)
  bstack1l111ll11_opy_(self, test, *args, **kwargs)
def bstack1llll1111l_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11111l1l1_opy_
  global CONFIG
  global bstack11llll1l11_opy_
  global bstack11ll1l1111_opy_
  global bstack11l1l1ll1l_opy_
  bstack111l111l1l_opy_ = None
  try:
    if bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫഉ"), None) or bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨഊ"), None):
      try:
        if not bstack11ll1l1111_opy_:
          bstack1lllll1l11_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"ࠧࡿࠩഋ")), bstack11l1l11_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨഌ"), bstack11l1l11_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ഍"))
          with bstack11l1l1ll1l_opy_:
            if os.path.exists(bstack1lllll1l11_opy_):
              with open(bstack1lllll1l11_opy_, bstack11l1l11_opy_ (u"ࠪࡶࠬഎ")) as f:
                content = f.read().strip()
                if content:
                  bstack1l1l11lll_opy_ = json.loads(bstack11l1l11_opy_ (u"ࠦࢀࠨഏ") + content + bstack11l1l11_opy_ (u"ࠬࠨࡸࠣ࠼ࠣࠦࡾࠨࠧഐ") + bstack11l1l11_opy_ (u"ࠨࡽࠣ഑"))
                  bstack11ll1l1111_opy_ = bstack1l1l11lll_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡋࡇࡷࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾ࠥ࠭ഒ") + str(e))
      if bstack11llll1l11_opy_:
        with bstack11ll1l11l_opy_:
          bstack11lll1ll1l_opy_ = bstack11llll1l11_opy_.copy()
        for driver in bstack11lll1ll1l_opy_:
          if bstack11ll1l1111_opy_ == driver.session_id:
            bstack111l111l1l_opy_ = driver
    bstack1lll111111_opy_ = bstack111l1lll_opy_.bstack111111l1l_opy_(test.tags)
    if bstack111l111l1l_opy_:
      threading.current_thread().isA11yTest = bstack111l1lll_opy_.bstack11l111111_opy_(bstack111l111l1l_opy_, bstack1lll111111_opy_)
      threading.current_thread().isAppA11yTest = bstack111l1lll_opy_.bstack11l111111_opy_(bstack111l111l1l_opy_, bstack1lll111111_opy_)
    else:
      threading.current_thread().isA11yTest = bstack1lll111111_opy_
      threading.current_thread().isAppA11yTest = bstack1lll111111_opy_
  except:
    pass
  bstack11111l1l1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1ll11l1ll_opy_
  try:
    bstack1ll11l1ll_opy_ = self._test
  except:
    bstack1ll11l1ll_opy_ = self.test
def bstack1l111111l_opy_():
  global bstack11l1llll11_opy_
  try:
    if os.path.exists(bstack11l1llll11_opy_):
      os.remove(bstack11l1llll11_opy_)
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫഓ") + str(e))
def bstack1ll111l11_opy_():
  global bstack11l1llll11_opy_
  bstack1111l111l1_opy_ = {}
  lock_file = bstack11l1llll11_opy_ + bstack11l1l11_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨഔ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭ക"))
    try:
      if not os.path.isfile(bstack11l1llll11_opy_):
        with open(bstack11l1llll11_opy_, bstack11l1l11_opy_ (u"ࠫࡼ࠭ഖ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack11l1llll11_opy_):
        with open(bstack11l1llll11_opy_, bstack11l1l11_opy_ (u"ࠬࡸࠧഗ")) as f:
          content = f.read().strip()
          if content:
            bstack1111l111l1_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack11l1l11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨഘ") + str(e))
    return bstack1111l111l1_opy_
  try:
    os.makedirs(os.path.dirname(bstack11l1llll11_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack11l1llll11_opy_):
        with open(bstack11l1llll11_opy_, bstack11l1l11_opy_ (u"ࠧࡸࠩങ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack11l1llll11_opy_):
        with open(bstack11l1llll11_opy_, bstack11l1l11_opy_ (u"ࠨࡴࠪച")) as f:
          content = f.read().strip()
          if content:
            bstack1111l111l1_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫഛ") + str(e))
  finally:
    return bstack1111l111l1_opy_
def bstack1l11l111l1_opy_(platform_index, item_index):
  global bstack11l1llll11_opy_
  lock_file = bstack11l1llll11_opy_ + bstack11l1l11_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩജ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l1l11_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧഝ"))
    try:
      bstack1111l111l1_opy_ = {}
      if os.path.exists(bstack11l1llll11_opy_):
        with open(bstack11l1llll11_opy_, bstack11l1l11_opy_ (u"ࠬࡸࠧഞ")) as f:
          content = f.read().strip()
          if content:
            bstack1111l111l1_opy_ = json.loads(content)
      bstack1111l111l1_opy_[item_index] = platform_index
      with open(bstack11l1llll11_opy_, bstack11l1l11_opy_ (u"ࠨࡷࠣട")) as outfile:
        json.dump(bstack1111l111l1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11l1l11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡺࡶ࡮ࡺࡩ࡯ࡩࠣࡸࡴࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬഠ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack11l1llll11_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack1111l111l1_opy_ = {}
      if os.path.exists(bstack11l1llll11_opy_):
        with open(bstack11l1llll11_opy_, bstack11l1l11_opy_ (u"ࠨࡴࠪഡ")) as f:
          content = f.read().strip()
          if content:
            bstack1111l111l1_opy_ = json.loads(content)
      bstack1111l111l1_opy_[item_index] = platform_index
      with open(bstack11l1llll11_opy_, bstack11l1l11_opy_ (u"ࠤࡺࠦഢ")) as outfile:
        json.dump(bstack1111l111l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡽࡲࡪࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨണ") + str(e))
def bstack1l1l11l111_opy_(bstack1l111lll1_opy_):
  global CONFIG
  bstack11l1111ll_opy_ = bstack11l1l11_opy_ (u"ࠫࠬത")
  if not bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨഥ") in CONFIG:
    logger.info(bstack11l1l11_opy_ (u"࠭ࡎࡰࠢࡳࡰࡦࡺࡦࡰࡴࡰࡷࠥࡶࡡࡴࡵࡨࡨࠥࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡲࡪࡸࡡࡵࡧࠣࡶࡪࡶ࡯ࡳࡶࠣࡪࡴࡸࠠࡓࡱࡥࡳࡹࠦࡲࡶࡰࠪദ"))
  try:
    platform = CONFIG[bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪധ")][bstack1l111lll1_opy_]
    if bstack11l1l11_opy_ (u"ࠨࡱࡶࠫന") in platform:
      bstack11l1111ll_opy_ += str(platform[bstack11l1l11_opy_ (u"ࠩࡲࡷࠬഩ")]) + bstack11l1l11_opy_ (u"ࠪ࠰ࠥ࠭പ")
    if bstack11l1l11_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧഫ") in platform:
      bstack11l1111ll_opy_ += str(platform[bstack11l1l11_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨബ")]) + bstack11l1l11_opy_ (u"࠭ࠬࠡࠩഭ")
    if bstack11l1l11_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫമ") in platform:
      bstack11l1111ll_opy_ += str(platform[bstack11l1l11_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬയ")]) + bstack11l1l11_opy_ (u"ࠩ࠯ࠤࠬര")
    if bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬറ") in platform:
      bstack11l1111ll_opy_ += str(platform[bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ല")]) + bstack11l1l11_opy_ (u"ࠬ࠲ࠠࠨള")
    if bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫഴ") in platform:
      bstack11l1111ll_opy_ += str(platform[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬവ")]) + bstack11l1l11_opy_ (u"ࠨ࠮ࠣࠫശ")
    if bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪഷ") in platform:
      bstack11l1111ll_opy_ += str(platform[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫസ")]) + bstack11l1l11_opy_ (u"ࠫ࠱ࠦࠧഹ")
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"࡙ࠬ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡺࡲࡪࡰࡪࠤ࡫ࡵࡲࠡࡴࡨࡴࡴࡸࡴࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡲࡲࠬഺ") + str(e))
  finally:
    if bstack11l1111ll_opy_[len(bstack11l1111ll_opy_) - 2:] == bstack11l1l11_opy_ (u"഻࠭ࠬࠡࠩ"):
      bstack11l1111ll_opy_ = bstack11l1111ll_opy_[:-2]
    return bstack11l1111ll_opy_
def bstack1l1l1l1l11_opy_(path, bstack11l1111ll_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack11l111ll11_opy_ = ET.parse(path)
    bstack1l11111lll_opy_ = bstack11l111ll11_opy_.getroot()
    bstack1l11l111l_opy_ = None
    for suite in bstack1l11111lll_opy_.iter(bstack11l1l11_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ഼࠭")):
      if bstack11l1l11_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨഽ") in suite.attrib:
        suite.attrib[bstack11l1l11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧാ")] += bstack11l1l11_opy_ (u"ࠪࠤࠬി") + bstack11l1111ll_opy_
        bstack1l11l111l_opy_ = suite
    bstack1lllll1ll1_opy_ = None
    for robot in bstack1l11111lll_opy_.iter(bstack11l1l11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪീ")):
      bstack1lllll1ll1_opy_ = robot
    bstack1l11lll111_opy_ = len(bstack1lllll1ll1_opy_.findall(bstack11l1l11_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫു")))
    if bstack1l11lll111_opy_ == 1:
      bstack1lllll1ll1_opy_.remove(bstack1lllll1ll1_opy_.findall(bstack11l1l11_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬൂ"))[0])
      bstack1ll1l1l11l_opy_ = ET.Element(bstack11l1l11_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ൃ"), attrib={bstack11l1l11_opy_ (u"ࠨࡰࡤࡱࡪ࠭ൄ"): bstack11l1l11_opy_ (u"ࠩࡖࡹ࡮ࡺࡥࡴࠩ൅"), bstack11l1l11_opy_ (u"ࠪ࡭ࡩ࠭െ"): bstack11l1l11_opy_ (u"ࠫࡸ࠶ࠧേ")})
      bstack1lllll1ll1_opy_.insert(1, bstack1ll1l1l11l_opy_)
      bstack1l11llllll_opy_ = None
      for suite in bstack1lllll1ll1_opy_.iter(bstack11l1l11_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫൈ")):
        bstack1l11llllll_opy_ = suite
      bstack1l11llllll_opy_.append(bstack1l11l111l_opy_)
      bstack1ll11l1l1_opy_ = None
      for status in bstack1l11l111l_opy_.iter(bstack11l1l11_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭൉")):
        bstack1ll11l1l1_opy_ = status
      bstack1l11llllll_opy_.append(bstack1ll11l1l1_opy_)
    bstack11l111ll11_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠬൊ") + str(e))
def bstack1ll11lll1l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack11ll111lll_opy_
  global CONFIG
  if bstack11l1l11_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬ࠧോ") in options:
    del options[bstack11l1l11_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨൌ")]
  json_data = bstack1ll111l11_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack11l1l11_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࡡࡵࡩࡸࡻ࡬ࡵࡵ്ࠪ"), str(item_id), bstack11l1l11_opy_ (u"ࠫࡴࡻࡴࡱࡷࡷ࠲ࡽࡳ࡬ࠨൎ"))
    bstack1l1l1l1l11_opy_(path, bstack1l1l11l111_opy_(json_data[item_id]))
  bstack1l111111l_opy_()
  return bstack11ll111lll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1l1111l11_opy_(self, ff_profile_dir):
  global bstack1lll11l111_opy_
  if not ff_profile_dir:
    return None
  return bstack1lll11l111_opy_(self, ff_profile_dir)
def bstack1lll111l1_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack111ll1l1l1_opy_
  bstack111ll11111_opy_ = []
  if bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ൏") in CONFIG:
    bstack111ll11111_opy_ = CONFIG[bstack11l1l11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ൐")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11l1l11_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࠣ൑")],
      pabot_args[bstack11l1l11_opy_ (u"ࠣࡸࡨࡶࡧࡵࡳࡦࠤ൒")],
      argfile,
      pabot_args.get(bstack11l1l11_opy_ (u"ࠤ࡫࡭ࡻ࡫ࠢ൓")),
      pabot_args[bstack11l1l11_opy_ (u"ࠥࡴࡷࡵࡣࡦࡵࡶࡩࡸࠨൔ")],
      platform[0],
      bstack111ll1l1l1_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11l1l11_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹ࡬ࡩ࡭ࡧࡶࠦൕ")] or [(bstack11l1l11_opy_ (u"ࠧࠨൖ"), None)]
    for platform in enumerate(bstack111ll11111_opy_)
  ]
def bstack111l1111l1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1l111111ll_opy_=bstack11l1l11_opy_ (u"࠭ࠧൗ")):
  global bstack11l11llll1_opy_
  self.platform_index = platform_index
  self.bstack11l11l11l1_opy_ = bstack1l111111ll_opy_
  bstack11l11llll1_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack111l1l1l11_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l1111l1l_opy_
  global bstack111l111ll1_opy_
  bstack1l1l1l1lll_opy_ = copy.deepcopy(item)
  if not bstack11l1l11_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ൘") in item.options:
    bstack1l1l1l1lll_opy_.options[bstack11l1l11_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ൙")] = []
  bstack111ll11l1_opy_ = bstack1l1l1l1lll_opy_.options[bstack11l1l11_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ൚")].copy()
  for v in bstack1l1l1l1lll_opy_.options[bstack11l1l11_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ൛")]:
    if bstack11l1l11_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚ࠪ൜") in v:
      bstack111ll11l1_opy_.remove(v)
    if bstack11l1l11_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬ൝") in v:
      bstack111ll11l1_opy_.remove(v)
    if bstack11l1l11_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡊࡅࡇࡎࡒࡇࡆࡒࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪ൞") in v:
      bstack111ll11l1_opy_.remove(v)
  bstack111ll11l1_opy_.insert(0, bstack11l1l11_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝ࡀࡻࡾࠩൟ").format(bstack1l1l1l1lll_opy_.platform_index))
  bstack111ll11l1_opy_.insert(0, bstack11l1l11_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖ࠿ࢁࡽࠨൠ").format(bstack1l1l1l1lll_opy_.bstack11l11l11l1_opy_))
  bstack1l1l1l1lll_opy_.options[bstack11l1l11_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫൡ")] = bstack111ll11l1_opy_
  if bstack111l111ll1_opy_:
    bstack1l1l1l1lll_opy_.options[bstack11l1l11_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬൢ")].insert(0, bstack11l1l11_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖ࠾ࢀࢃࠧൣ").format(bstack111l111ll1_opy_))
  return bstack1l1111l1l_opy_(caller_id, datasources, is_last, bstack1l1l1l1lll_opy_, outs_dir)
def bstack111lll111_opy_(command, item_index):
  try:
    if bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭൤")):
      os.environ[bstack11l1l11_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧ൥")] = json.dumps(CONFIG[bstack11l1l11_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ൦")][item_index % bstack1ll11111l_opy_])
    global bstack111l111ll1_opy_
    if bstack111l111ll1_opy_:
      command[0] = command[0].replace(bstack11l1l11_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ൧"), bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡵࡧ࡯ࠥࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱࠦ࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠥ࠭൨") + str(
        item_index) + bstack11l1l11_opy_ (u"ࠪࠤࠬ൩") + bstack111l111ll1_opy_, 1)
    else:
      command[0] = command[0].replace(bstack11l1l11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ൪"),
                                      bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡸࡪ࡫ࠡࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠢ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠡࠩ൫") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack11l1l11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡳ࡯ࡥ࡫ࡩࡽ࡮ࡴࡧࠡࡥࡲࡱࡲࡧ࡮ࡥࠢࡩࡳࡷࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯࠼ࠣࡿࢂ࠭൬").format(str(e)))
def bstack1l1l11l11_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1ll111l111_opy_
  try:
    bstack111lll111_opy_(command, item_index)
    return bstack1ll111l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack11l1l11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲ࠿ࠦࡻࡾࠩ൭").format(str(e)))
    raise e
def bstack1111ll1111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1ll111l111_opy_
  try:
    bstack111lll111_opy_(command, item_index)
    return bstack1ll111l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack11l1l11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࠦ࠲࠯࠳࠶࠾ࠥࢁࡽࠨ൮").format(str(e)))
    try:
      return bstack1ll111l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack11l1l11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣ࠶࠳࠷࠳ࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧ൯").format(str(e2)))
      raise e
def bstack1111lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1ll111l111_opy_
  try:
    bstack111lll111_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack1ll111l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack11l1l11_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠴࠱࠵࠺ࡀࠠࡼࡿࠪ൰").format(str(e)))
    try:
      return bstack1ll111l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack11l1l11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࠸࠮࠲࠷ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩ൱").format(str(e2)))
      raise e
def _111l1l1lll_opy_(bstack1l1ll1ll11_opy_, item_index, process_timeout, sleep_before_start, bstack11l1l11l1_opy_):
  bstack111lll111_opy_(bstack1l1ll1ll11_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack1111111ll_opy_(command, bstack1l1l1ll1ll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1ll111l111_opy_
  try:
    bstack111lll111_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack1ll111l111_opy_(command, bstack1l1l1ll1ll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11l1l11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰࠣ࠹࠳࠶࠺ࠡࡽࢀࠫ൲").format(str(e)))
    try:
      return bstack1ll111l111_opy_(command, bstack1l1l1ll1ll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11l1l11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࡿࢂ࠭൳").format(str(e2)))
      raise e
def bstack11111ll1ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1ll111l111_opy_
  try:
    process_timeout = _111l1l1lll_opy_(command, item_index, process_timeout, sleep_before_start, bstack11l1l11_opy_ (u"ࠧ࠵࠰࠵ࠫ൴"))
    return bstack1ll111l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11l1l11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࠦ࠴࠯࠴࠽ࠤࢀࢃࠧ൵").format(str(e)))
    try:
      return bstack1ll111l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11l1l11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩ൶").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack11ll1llll1_opy_(self, runner, quiet=False, capture=True):
  global bstack1l1l1111l_opy_
  bstack1l1llll1l1_opy_ = bstack1l1l1111l_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11l1l11_opy_ (u"ࠪࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࡥࡡࡳࡴࠪ൷")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11l1l11_opy_ (u"ࠫࡪࡾࡣࡠࡶࡵࡥࡨ࡫ࡢࡢࡥ࡮ࡣࡦࡸࡲࠨ൸")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1l1llll1l1_opy_
def bstack1lllll11ll_opy_(runner, hook_name, context, element, bstack11ll1ll1l_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1l1l1l11l1_opy_.bstack11ll1l1l_opy_(hook_name, element)
    bstack11ll1ll1l_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1l1l1l11l1_opy_.bstack11ll111l_opy_(element)
      if hook_name not in [bstack11l1l11_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠩ൹"), bstack11l1l11_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩൺ")] and args and hasattr(args[0], bstack11l1l11_opy_ (u"ࠧࡦࡴࡵࡳࡷࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠧൻ")):
        args[0].error_message = bstack11l1l11_opy_ (u"ࠨࠩർ")
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡮ࡡ࡯ࡦ࡯ࡩࠥ࡮࡯ࡰ࡭ࡶࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫࠺ࠡࡽࢀࠫൽ").format(str(e)))
@measure(event_name=EVENTS.bstack111ll1lll_opy_, stage=STAGE.bstack11l1lllll_opy_, hook_type=bstack11l1l11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡄࡰࡱࠨൾ"), bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1l1ll11ll_opy_(runner, name, context, bstack11ll1ll1l_opy_, *args):
    if runner.hooks.get(bstack11l1l11_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣൿ")).__name__ != bstack11l1l11_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࡡࡧࡩ࡫ࡧࡵ࡭ࡶࡢ࡬ࡴࡵ࡫ࠣ඀"):
      bstack1lllll11ll_opy_(runner, name, context, runner, bstack11ll1ll1l_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack11ll1lll11_opy_(bstack11l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඁ")) else context.browser
      runner.driver_initialised = bstack11l1l11_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦං")
    except Exception as e:
      logger.debug(bstack11l1l11_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡩࠥࡧࡴࡵࡴ࡬ࡦࡺࡺࡥ࠻ࠢࡾࢁࠬඃ").format(str(e)))
def bstack11ll1l11l1_opy_(runner, name, context, bstack11ll1ll1l_opy_, *args):
    bstack1lllll11ll_opy_(runner, name, context, context.feature, bstack11ll1ll1l_opy_, *args)
    try:
      if not bstack1l1l1ll1l1_opy_:
        bstack111l111l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack11ll1lll11_opy_(bstack11l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ඄")) else context.browser
        if is_driver_active(bstack111l111l1l_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack11l1l11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦඅ")
          bstack1ll1ll111l_opy_ = str(runner.feature.name)
          bstack1111l1ll1l_opy_(context, bstack1ll1ll111l_opy_)
          bstack111l111l1l_opy_.execute_script(bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩආ") + json.dumps(bstack1ll1ll111l_opy_) + bstack11l1l11_opy_ (u"ࠬࢃࡽࠨඇ"))
    except Exception as e:
      logger.debug(bstack11l1l11_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭ඈ").format(str(e)))
def bstack1111l1ll1_opy_(runner, name, context, bstack11ll1ll1l_opy_, *args):
    if hasattr(context, bstack11l1l11_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩඉ")):
        bstack1l1l1l11l1_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack11l1l11_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪඊ")) else context.feature
    bstack1lllll11ll_opy_(runner, name, context, target, bstack11ll1ll1l_opy_, *args)
@measure(event_name=EVENTS.bstack111l11l11_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1ll11l1l1l_opy_(runner, name, context, bstack11ll1ll1l_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1l1l1l11l1_opy_.start_test(context)
    bstack1lllll11ll_opy_(runner, name, context, context.scenario, bstack11ll1ll1l_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack111l1lllll_opy_.bstack111l1111ll_opy_(context, *args)
    try:
      bstack111l111l1l_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨඋ"), context.browser)
      if is_driver_active(bstack111l111l1l_opy_):
        bstack1l1lll1l_opy_.bstack111ll11ll1_opy_(bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩඌ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l1l11_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨඍ")
        if (not bstack1l1l1ll1l1_opy_):
          scenario_name = args[0].name
          feature_name = bstack1ll1ll111l_opy_ = str(runner.feature.name)
          bstack1ll1ll111l_opy_ = feature_name + bstack11l1l11_opy_ (u"ࠬࠦ࠭ࠡࠩඎ") + scenario_name
          if runner.driver_initialised == bstack11l1l11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣඏ"):
            bstack1111l1ll1l_opy_(context, bstack1ll1ll111l_opy_)
            bstack111l111l1l_opy_.execute_script(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬඐ") + json.dumps(bstack1ll1ll111l_opy_) + bstack11l1l11_opy_ (u"ࠨࡿࢀࠫඑ"))
    except Exception as e:
      logger.debug(bstack11l1l11_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡ࡫ࡱࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡩࡥ࡯ࡣࡵ࡭ࡴࡀࠠࡼࡿࠪඒ").format(str(e)))
@measure(event_name=EVENTS.bstack111ll1lll_opy_, stage=STAGE.bstack11l1lllll_opy_, hook_type=bstack11l1l11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡖࡸࡪࡶࠢඓ"), bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1lll1lll11_opy_(runner, name, context, bstack11ll1ll1l_opy_, *args):
    bstack1lllll11ll_opy_(runner, name, context, args[0], bstack11ll1ll1l_opy_, *args)
    try:
      bstack111l111l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack11ll1lll11_opy_(bstack11l1l11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪඔ")) else context.browser
      if is_driver_active(bstack111l111l1l_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l1l11_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥඕ")
        bstack1l1l1l11l1_opy_.bstack11ll11l1_opy_(args[0])
        if runner.driver_initialised == bstack11l1l11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦඖ"):
          feature_name = bstack1ll1ll111l_opy_ = str(runner.feature.name)
          bstack1ll1ll111l_opy_ = feature_name + bstack11l1l11_opy_ (u"ࠧࠡ࠯ࠣࠫ඗") + context.scenario.name
          bstack111l111l1l_opy_.execute_script(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭඘") + json.dumps(bstack1ll1ll111l_opy_) + bstack11l1l11_opy_ (u"ࠩࢀࢁࠬ඙"))
    except Exception as e:
      logger.debug(bstack11l1l11_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡴࡦࡲ࠽ࠤࢀࢃࠧක").format(str(e)))
@measure(event_name=EVENTS.bstack111ll1lll_opy_, stage=STAGE.bstack11l1lllll_opy_, hook_type=bstack11l1l11_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࡖࡸࡪࡶࠢඛ"), bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack11l1l111ll_opy_(runner, name, context, bstack11ll1ll1l_opy_, *args):
  bstack1l1l1l11l1_opy_.bstack11ll11ll_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack111l111l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫග") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack111l111l1l_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack11l1l11_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭ඝ")
        feature_name = bstack1ll1ll111l_opy_ = str(runner.feature.name)
        bstack1ll1ll111l_opy_ = feature_name + bstack11l1l11_opy_ (u"ࠧࠡ࠯ࠣࠫඞ") + context.scenario.name
        bstack111l111l1l_opy_.execute_script(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭ඟ") + json.dumps(bstack1ll1ll111l_opy_) + bstack11l1l11_opy_ (u"ࠩࢀࢁࠬච"))
    if str(step_status).lower() == bstack11l1l11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪඡ"):
      bstack1ll1llll11_opy_ = bstack11l1l11_opy_ (u"ࠫࠬජ")
      bstack1ll1lll11l_opy_ = bstack11l1l11_opy_ (u"ࠬ࠭ඣ")
      bstack111llll1l_opy_ = bstack11l1l11_opy_ (u"࠭ࠧඤ")
      try:
        import traceback
        bstack1ll1llll11_opy_ = runner.exception.__class__.__name__
        bstack11l1llll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1ll1lll11l_opy_ = bstack11l1l11_opy_ (u"ࠧࠡࠩඥ").join(bstack11l1llll_opy_)
        bstack111llll1l_opy_ = bstack11l1llll_opy_[-1]
      except Exception as e:
        logger.debug(bstack11l11llll_opy_.format(str(e)))
      bstack1ll1llll11_opy_ += bstack111llll1l_opy_
      bstack1lll1lllll_opy_(context, json.dumps(str(args[0].name) + bstack11l1l11_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢඦ") + str(bstack1ll1lll11l_opy_)),
                          bstack11l1l11_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣට"))
      if runner.driver_initialised == bstack11l1l11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣඨ"):
        bstack1ll1lllll_opy_(getattr(context, bstack11l1l11_opy_ (u"ࠫࡵࡧࡧࡦࠩඩ"), None), bstack11l1l11_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧඪ"), bstack1ll1llll11_opy_)
        bstack111l111l1l_opy_.execute_script(bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫණ") + json.dumps(str(args[0].name) + bstack11l1l11_opy_ (u"ࠢࠡ࠯ࠣࡊࡦ࡯࡬ࡦࡦࠤࡠࡳࠨඬ") + str(bstack1ll1lll11l_opy_)) + bstack11l1l11_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨත"))
      if runner.driver_initialised == bstack11l1l11_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢථ"):
        bstack11ll1111ll_opy_(bstack111l111l1l_opy_, bstack11l1l11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪද"), bstack11l1l11_opy_ (u"ࠦࡘࡩࡥ࡯ࡣࡵ࡭ࡴࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣධ") + str(bstack1ll1llll11_opy_))
    else:
      bstack1lll1lllll_opy_(context, bstack11l1l11_opy_ (u"ࠧࡖࡡࡴࡵࡨࡨࠦࠨන"), bstack11l1l11_opy_ (u"ࠨࡩ࡯ࡨࡲࠦ඲"))
      if runner.driver_initialised == bstack11l1l11_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧඳ"):
        bstack1ll1lllll_opy_(getattr(context, bstack11l1l11_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ප"), None), bstack11l1l11_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤඵ"))
      bstack111l111l1l_opy_.execute_script(bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨබ") + json.dumps(str(args[0].name) + bstack11l1l11_opy_ (u"ࠦࠥ࠳ࠠࡑࡣࡶࡷࡪࡪࠡࠣභ")) + bstack11l1l11_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫම"))
      if runner.driver_initialised == bstack11l1l11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦඹ"):
        bstack11ll1111ll_opy_(bstack111l111l1l_opy_, bstack11l1l11_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢය"))
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥࡹࡴࡦࡲ࠽ࠤࢀࢃࠧර").format(str(e)))
  bstack1lllll11ll_opy_(runner, name, context, args[0], bstack11ll1ll1l_opy_, *args)
@measure(event_name=EVENTS.bstack111l1lll1l_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1lll11ll1_opy_(runner, name, context, bstack11ll1ll1l_opy_, *args):
  bstack1l1l1l11l1_opy_.end_test(args[0])
  try:
    bstack1l1lll1ll1_opy_ = args[0].status.name
    bstack111l111l1l_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ඼"), context.browser)
    bstack111l1lllll_opy_.bstack11ll11111l_opy_(bstack111l111l1l_opy_)
    if str(bstack1l1lll1ll1_opy_).lower() == bstack11l1l11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪල"):
      bstack1ll1llll11_opy_ = bstack11l1l11_opy_ (u"ࠫࠬ඾")
      bstack1ll1lll11l_opy_ = bstack11l1l11_opy_ (u"ࠬ࠭඿")
      bstack111llll1l_opy_ = bstack11l1l11_opy_ (u"࠭ࠧව")
      try:
        import traceback
        bstack1ll1llll11_opy_ = runner.exception.__class__.__name__
        bstack11l1llll_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1ll1lll11l_opy_ = bstack11l1l11_opy_ (u"ࠧࠡࠩශ").join(bstack11l1llll_opy_)
        bstack111llll1l_opy_ = bstack11l1llll_opy_[-1]
      except Exception as e:
        logger.debug(bstack11l11llll_opy_.format(str(e)))
      bstack1ll1llll11_opy_ += bstack111llll1l_opy_
      bstack1lll1lllll_opy_(context, json.dumps(str(args[0].name) + bstack11l1l11_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢෂ") + str(bstack1ll1lll11l_opy_)),
                          bstack11l1l11_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣස"))
      if runner.driver_initialised == bstack11l1l11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧහ") or runner.driver_initialised == bstack11l1l11_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫළ"):
        bstack1ll1lllll_opy_(getattr(context, bstack11l1l11_opy_ (u"ࠬࡶࡡࡨࡧࠪෆ"), None), bstack11l1l11_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ෇"), bstack1ll1llll11_opy_)
        bstack111l111l1l_opy_.execute_script(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ෈") + json.dumps(str(args[0].name) + bstack11l1l11_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢ෉") + str(bstack1ll1lll11l_opy_)) + bstack11l1l11_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࡽࡾ්ࠩ"))
      if runner.driver_initialised == bstack11l1l11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ෋") or runner.driver_initialised == bstack11l1l11_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫ෌"):
        bstack11ll1111ll_opy_(bstack111l111l1l_opy_, bstack11l1l11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ෍"), bstack11l1l11_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥ෎") + str(bstack1ll1llll11_opy_))
    else:
      bstack1lll1lllll_opy_(context, bstack11l1l11_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣා"), bstack11l1l11_opy_ (u"ࠣ࡫ࡱࡪࡴࠨැ"))
      if runner.driver_initialised == bstack11l1l11_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦෑ") or runner.driver_initialised == bstack11l1l11_opy_ (u"ࠪ࡭ࡳࡹࡴࡦࡲࠪි"):
        bstack1ll1lllll_opy_(getattr(context, bstack11l1l11_opy_ (u"ࠫࡵࡧࡧࡦࠩී"), None), bstack11l1l11_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧු"))
      bstack111l111l1l_opy_.execute_script(bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ෕") + json.dumps(str(args[0].name) + bstack11l1l11_opy_ (u"ࠢࠡ࠯ࠣࡔࡦࡹࡳࡦࡦࠤࠦූ")) + bstack11l1l11_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦࢂࢃࠧ෗"))
      if runner.driver_initialised == bstack11l1l11_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦෘ") or runner.driver_initialised == bstack11l1l11_opy_ (u"ࠪ࡭ࡳࡹࡴࡦࡲࠪෙ"):
        bstack11ll1111ll_opy_(bstack111l111l1l_opy_, bstack11l1l11_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦේ"))
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡪࡰࠣࡥ࡫ࡺࡥࡳࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧෛ").format(str(e)))
  bstack1lllll11ll_opy_(runner, name, context, context.scenario, bstack11ll1ll1l_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1l111lll1l_opy_(runner, name, context, bstack11ll1ll1l_opy_, *args):
    target = context.scenario if hasattr(context, bstack11l1l11_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨො")) else context.feature
    bstack1lllll11ll_opy_(runner, name, context, target, bstack11ll1ll1l_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack111l1l1ll_opy_(runner, name, context, bstack11ll1ll1l_opy_, *args):
    try:
      bstack111l111l1l_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ෝ"), context.browser)
      bstack1llll1llll_opy_ = bstack11l1l11_opy_ (u"ࠨࠩෞ")
      if context.failed is True:
        bstack1ll1l11ll_opy_ = []
        bstack1ll11l111l_opy_ = []
        bstack11l1l11111_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1ll1l11ll_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l1llll_opy_ = traceback.format_tb(exc_tb)
            bstack11ll1ll11l_opy_ = bstack11l1l11_opy_ (u"ࠩࠣࠫෟ").join(bstack11l1llll_opy_)
            bstack1ll11l111l_opy_.append(bstack11ll1ll11l_opy_)
            bstack11l1l11111_opy_.append(bstack11l1llll_opy_[-1])
        except Exception as e:
          logger.debug(bstack11l11llll_opy_.format(str(e)))
        bstack1ll1llll11_opy_ = bstack11l1l11_opy_ (u"ࠪࠫ෠")
        for i in range(len(bstack1ll1l11ll_opy_)):
          bstack1ll1llll11_opy_ += bstack1ll1l11ll_opy_[i] + bstack11l1l11111_opy_[i] + bstack11l1l11_opy_ (u"ࠫࡡࡴࠧ෡")
        bstack1llll1llll_opy_ = bstack11l1l11_opy_ (u"ࠬࠦࠧ෢").join(bstack1ll11l111l_opy_)
        if runner.driver_initialised in [bstack11l1l11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢ෣"), bstack11l1l11_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦ෤")]:
          bstack1lll1lllll_opy_(context, bstack1llll1llll_opy_, bstack11l1l11_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢ෥"))
          bstack1ll1lllll_opy_(getattr(context, bstack11l1l11_opy_ (u"ࠩࡳࡥ࡬࡫ࠧ෦"), None), bstack11l1l11_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ෧"), bstack1ll1llll11_opy_)
          bstack111l111l1l_opy_.execute_script(bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ෨") + json.dumps(bstack1llll1llll_opy_) + bstack11l1l11_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤࢀࢁࠬ෩"))
          bstack11ll1111ll_opy_(bstack111l111l1l_opy_, bstack11l1l11_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ෪"), bstack11l1l11_opy_ (u"ࠢࡔࡱࡰࡩࠥࡹࡣࡦࡰࡤࡶ࡮ࡵࡳࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢ࡟ࡲࠧ෫") + str(bstack1ll1llll11_opy_))
          bstack11ll11ll1_opy_ = bstack11llll1lll_opy_(bstack1llll1llll_opy_, runner.feature.name, logger)
          if (bstack11ll11ll1_opy_ != None):
            bstack11l11111l_opy_.append(bstack11ll11ll1_opy_)
      else:
        if runner.driver_initialised in [bstack11l1l11_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤ෬"), bstack11l1l11_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨ෭")]:
          bstack1lll1lllll_opy_(context, bstack11l1l11_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨ࠾ࠥࠨ෮") + str(runner.feature.name) + bstack11l1l11_opy_ (u"ࠦࠥࡶࡡࡴࡵࡨࡨࠦࠨ෯"), bstack11l1l11_opy_ (u"ࠧ࡯࡮ࡧࡱࠥ෰"))
          bstack1ll1lllll_opy_(getattr(context, bstack11l1l11_opy_ (u"࠭ࡰࡢࡩࡨࠫ෱"), None), bstack11l1l11_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢෲ"))
          bstack111l111l1l_opy_.execute_script(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ෳ") + json.dumps(bstack11l1l11_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧ࠽ࠤࠧ෴") + str(runner.feature.name) + bstack11l1l11_opy_ (u"ࠥࠤࡵࡧࡳࡴࡧࡧࠥࠧ෵")) + bstack11l1l11_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢࡾࡿࠪ෶"))
          bstack11ll1111ll_opy_(bstack111l111l1l_opy_, bstack11l1l11_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ෷"))
          bstack11ll11ll1_opy_ = bstack11llll1lll_opy_(bstack1llll1llll_opy_, runner.feature.name, logger)
          if (bstack11ll11ll1_opy_ != None):
            bstack11l11111l_opy_.append(bstack11ll11ll1_opy_)
    except Exception as e:
      logger.debug(bstack11l1l11_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ෸").format(str(e)))
    bstack1lllll11ll_opy_(runner, name, context, context.feature, bstack11ll1ll1l_opy_, *args)
@measure(event_name=EVENTS.bstack111ll1lll_opy_, stage=STAGE.bstack11l1lllll_opy_, hook_type=bstack11l1l11_opy_ (u"ࠢࡢࡨࡷࡩࡷࡇ࡬࡭ࠤ෹"), bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1l1l1l111_opy_(runner, name, context, bstack11ll1ll1l_opy_, *args):
    bstack1lllll11ll_opy_(runner, name, context, runner, bstack11ll1ll1l_opy_, *args)
def bstack1l1111ll11_opy_(self, name, context, *args):
  try:
    if bstack11l1l1ll1_opy_:
      platform_index = int(threading.current_thread()._name) % bstack1ll11111l_opy_
      bstack11lll1l11_opy_ = CONFIG[bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ෺")][platform_index]
      os.environ[bstack11l1l11_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ෻")] = json.dumps(bstack11lll1l11_opy_)
    global bstack11ll1ll1l_opy_
    if not hasattr(self, bstack11l1l11_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡸ࡫ࡤࠨ෼")):
      self.driver_initialised = None
    bstack1111l111l_opy_ = {
        bstack11l1l11_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠨ෽"): bstack1l1ll11ll_opy_,
        bstack11l1l11_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭෾"): bstack11ll1l11l1_opy_,
        bstack11l1l11_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡴࡢࡩࠪ෿"): bstack1111l1ll1_opy_,
        bstack11l1l11_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩ฀"): bstack1ll11l1l1l_opy_,
        bstack11l1l11_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵ࠭ก"): bstack1lll1lll11_opy_,
        bstack11l1l11_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡷࡩࡵ࠭ข"): bstack11l1l111ll_opy_,
        bstack11l1l11_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫฃ"): bstack1lll11ll1_opy_,
        bstack11l1l11_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡸࡦ࡭ࠧค"): bstack1l111lll1l_opy_,
        bstack11l1l11_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠬฅ"): bstack111l1l1ll_opy_,
        bstack11l1l11_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩฆ"): bstack1l1l1l111_opy_
    }
    handler = bstack1111l111l_opy_.get(name, bstack11ll1ll1l_opy_)
    try:
      handler(self, name, context, bstack11ll1ll1l_opy_, *args)
    except Exception as e:
      logger.debug(bstack11l1l11_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦࠢ࡫ࡳࡴࡱࠠࡩࡣࡱࡨࡱ࡫ࡲࠡࡽࢀ࠾ࠥࢁࡽࠨง").format(name, str(e)))
    if name in [bstack11l1l11_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨจ"), bstack11l1l11_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪฉ"), bstack11l1l11_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡤࡰࡱ࠭ช")]:
      try:
        bstack111l111l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack11ll1lll11_opy_(bstack11l1l11_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪซ")) else context.browser
        bstack1l111l11l_opy_ = (
          (name == bstack11l1l11_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨฌ") and self.driver_initialised == bstack11l1l11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥญ")) or
          (name == bstack11l1l11_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧฎ") and self.driver_initialised == bstack11l1l11_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤฏ")) or
          (name == bstack11l1l11_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪฐ") and self.driver_initialised in [bstack11l1l11_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧฑ"), bstack11l1l11_opy_ (u"ࠦ࡮ࡴࡳࡵࡧࡳࠦฒ")]) or
          (name == bstack11l1l11_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡺࡥࡱࠩณ") and self.driver_initialised == bstack11l1l11_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦด"))
        )
        if bstack1l111l11l_opy_:
          self.driver_initialised = None
          if bstack111l111l1l_opy_ and hasattr(bstack111l111l1l_opy_, bstack11l1l11_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠫต")):
            try:
              bstack111l111l1l_opy_.quit()
            except Exception as e:
              logger.debug(bstack11l1l11_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡲࡷ࡬ࡸࡹ࡯࡮ࡨࠢࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩࠥ࡮࡯ࡰ࡭࠽ࠤࢀࢃࠧถ").format(str(e)))
      except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣ࡬ࡴࡵ࡫ࠡࡥ࡯ࡩࡦࡴࡵࡱࠢࡩࡳࡷࠦࡻࡾ࠼ࠣࡿࢂ࠭ท").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"ࠪࡇࡷ࡯ࡴࡪࡥࡤࡰࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡳࡷࡱࠤ࡭ࡵ࡯࡬ࠢࡾࢁ࠿ࠦࡻࡾࠩธ").format(name, str(e)))
    try:
      bstack11ll1ll1l_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack11l1l11_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡱࡵ࡭࡬࡯࡮ࡢ࡮ࠣࡦࡪ࡮ࡡࡷࡧࠣ࡬ࡴࡵ࡫ࠡࡽࢀ࠾ࠥࢁࡽࠨน").format(name, str(e2)))
def bstack1l11lll11l_opy_(config, startdir):
  return bstack11l1l11_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࠱ࡿࠥบ").format(bstack11l1l11_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧป"))
notset = Notset()
def bstack1ll1l1111l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack11ll11l1l1_opy_
  if str(name).lower() == bstack11l1l11_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸࠧผ"):
    return bstack11l1l11_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢฝ")
  else:
    return bstack11ll11l1l1_opy_(self, name, default, skip)
def bstack11l1ll111l_opy_(item, when):
  global bstack1llllll1ll_opy_
  try:
    bstack1llllll1ll_opy_(item, when)
  except Exception as e:
    pass
def bstack1l1111111_opy_():
  return
def bstack1lll1ll11l_opy_(type, name, status, reason, bstack1l11l1l111_opy_, bstack1l1l1ll11_opy_):
  bstack11ll11l11_opy_ = {
    bstack11l1l11_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩพ"): type,
    bstack11l1l11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ฟ"): {}
  }
  if type == bstack11l1l11_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ภ"):
    bstack11ll11l11_opy_[bstack11l1l11_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨม")][bstack11l1l11_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬย")] = bstack1l11l1l111_opy_
    bstack11ll11l11_opy_[bstack11l1l11_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪร")][bstack11l1l11_opy_ (u"ࠨࡦࡤࡸࡦ࠭ฤ")] = json.dumps(str(bstack1l1l1ll11_opy_))
  if type == bstack11l1l11_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪล"):
    bstack11ll11l11_opy_[bstack11l1l11_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ฦ")][bstack11l1l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩว")] = name
  if type == bstack11l1l11_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨศ"):
    bstack11ll11l11_opy_[bstack11l1l11_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩษ")][bstack11l1l11_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧส")] = status
    if status == bstack11l1l11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨห"):
      bstack11ll11l11_opy_[bstack11l1l11_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬฬ")][bstack11l1l11_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪอ")] = json.dumps(str(reason))
  bstack11l1l1l111_opy_ = bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩฮ").format(json.dumps(bstack11ll11l11_opy_))
  return bstack11l1l1l111_opy_
def bstack111l11l1l_opy_(driver_command, response):
    if driver_command == bstack11l1l11_opy_ (u"ࠬࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩฯ"):
        bstack1l1lll1l_opy_.bstack1l11l1lll_opy_({
            bstack11l1l11_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬะ"): response[bstack11l1l11_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭ั")],
            bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨา"): bstack1l1lll1l_opy_.current_test_uuid()
        })
def bstack1l1lll1l1l_opy_(item, call, rep):
  global bstack111ll1111_opy_
  global bstack11llll1l11_opy_
  global bstack1l1l1ll1l1_opy_
  name = bstack11l1l11_opy_ (u"ࠩࠪำ")
  try:
    if rep.when == bstack11l1l11_opy_ (u"ࠪࡧࡦࡲ࡬ࠨิ"):
      bstack11ll1l1111_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1l1l1ll1l1_opy_:
          name = str(rep.nodeid)
          bstack1l1ll1111l_opy_ = bstack1lll1ll11l_opy_(bstack11l1l11_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬี"), name, bstack11l1l11_opy_ (u"ࠬ࠭ึ"), bstack11l1l11_opy_ (u"࠭ࠧื"), bstack11l1l11_opy_ (u"ࠧࠨุ"), bstack11l1l11_opy_ (u"ࠨูࠩ"))
          threading.current_thread().bstack111l1ll11_opy_ = name
          for driver in bstack11llll1l11_opy_:
            if bstack11ll1l1111_opy_ == driver.session_id:
              driver.execute_script(bstack1l1ll1111l_opy_)
      except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾฺࠩ").format(str(e)))
      try:
        bstack1lll11ll11_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11l1l11_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ฻"):
          status = bstack11l1l11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ฼") if rep.outcome.lower() == bstack11l1l11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ฽") else bstack11l1l11_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭฾")
          reason = bstack11l1l11_opy_ (u"ࠧࠨ฿")
          if status == bstack11l1l11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨเ"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11l1l11_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧแ") if status == bstack11l1l11_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪโ") else bstack11l1l11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪใ")
          data = name + bstack11l1l11_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩࠧࠧไ") if status == bstack11l1l11_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ๅ") else name + bstack11l1l11_opy_ (u"ࠧࠡࡨࡤ࡭ࡱ࡫ࡤࠢࠢࠪๆ") + reason
          bstack1l1l11lll1_opy_ = bstack1lll1ll11l_opy_(bstack11l1l11_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪ็"), bstack11l1l11_opy_ (u"่ࠩࠪ"), bstack11l1l11_opy_ (u"้ࠪࠫ"), bstack11l1l11_opy_ (u"๊ࠫࠬ"), level, data)
          for driver in bstack11llll1l11_opy_:
            if bstack11ll1l1111_opy_ == driver.session_id:
              driver.execute_script(bstack1l1l11lll1_opy_)
      except Exception as e:
        logger.debug(bstack11l1l11_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡦࡳࡳࡺࡥࡹࡶࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾ๋ࠩ").format(str(e)))
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡶࡸࡦࡺࡥࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࠦࡳࡵࡣࡷࡹࡸࡀࠠࡼࡿࠪ์").format(str(e)))
  bstack111ll1111_opy_(item, call, rep)
def bstack1lll1l1l11_opy_(driver, bstack11l111ll1l_opy_, test=None):
  global bstack1l1111lll1_opy_
  if test != None:
    bstack111ll1l11l_opy_ = getattr(test, bstack11l1l11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬํ"), None)
    bstack11llll1l1_opy_ = getattr(test, bstack11l1l11_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭๎"), None)
    PercySDK.screenshot(driver, bstack11l111ll1l_opy_, bstack111ll1l11l_opy_=bstack111ll1l11l_opy_, bstack11llll1l1_opy_=bstack11llll1l1_opy_, bstack1l1l1llll1_opy_=bstack1l1111lll1_opy_)
  else:
    PercySDK.screenshot(driver, bstack11l111ll1l_opy_)
@measure(event_name=EVENTS.bstack1llll1ll1l_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack11ll11111_opy_(driver):
  if bstack1l1l1l1l1l_opy_.bstack11lllll11l_opy_() is True or bstack1l1l1l1l1l_opy_.capturing() is True:
    return
  bstack1l1l1l1l1l_opy_.bstack1l1llllll_opy_()
  while not bstack1l1l1l1l1l_opy_.bstack11lllll11l_opy_():
    bstack111l1ll1l_opy_ = bstack1l1l1l1l1l_opy_.bstack1ll1llll1l_opy_()
    bstack1lll1l1l11_opy_(driver, bstack111l1ll1l_opy_)
  bstack1l1l1l1l1l_opy_.bstack1ll11lllll_opy_()
def bstack111ll111ll_opy_(sequence, driver_command, response = None, bstack1l11l1ll1l_opy_ = None, args = None):
    try:
      if sequence != bstack11l1l11_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩ๏"):
        return
      if percy.bstack1llll11111_opy_() == bstack11l1l11_opy_ (u"ࠥࡪࡦࡲࡳࡦࠤ๐"):
        return
      bstack111l1ll1l_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ๑"), None)
      for command in bstack11lllll1l_opy_:
        if command == driver_command:
          with bstack11ll1l11l_opy_:
            bstack11lll1ll1l_opy_ = bstack11llll1l11_opy_.copy()
          for driver in bstack11lll1ll1l_opy_:
            bstack11ll11111_opy_(driver)
      bstack1l1111ll1l_opy_ = percy.bstack11l1lllll1_opy_()
      if driver_command in bstack1l11l1l1l1_opy_[bstack1l1111ll1l_opy_]:
        bstack1l1l1l1l1l_opy_.bstack11ll1lll1_opy_(bstack111l1ll1l_opy_, driver_command)
    except Exception as e:
      pass
def bstack1111l11l1_opy_(framework_name):
  if bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡳ࡯ࡥࡡࡦࡥࡱࡲࡥࡥࠩ๒")):
      return
  bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ๓"), True)
  global bstack11l11l1ll_opy_
  global bstack11l1ll11l_opy_
  global bstack1l1l1ll11l_opy_
  bstack11l11l1ll_opy_ = framework_name
  logger.info(bstack1lll1l1l1l_opy_.format(bstack11l11l1ll_opy_.split(bstack11l1l11_opy_ (u"ࠧ࠮ࠩ๔"))[0]))
  bstack11l111l11l_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack11l1l1ll1_opy_:
      Service.start = bstack1l111l111l_opy_
      Service.stop = bstack11lll11l1_opy_
      webdriver.Remote.get = bstack1l1l111ll1_opy_
      WebDriver.quit = bstack11lll111ll_opy_
      webdriver.Remote.__init__ = bstack1l11l1llll_opy_
    if not bstack11l1l1ll1_opy_:
        webdriver.Remote.__init__ = bstack1ll1ll11l_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack11l1l1ll11_opy_
    bstack11l1ll11l_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack11l1l1ll1_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1111l11l1l_opy_
  except Exception as e:
    pass
  bstack11l1l11ll_opy_()
  if not bstack11l1ll11l_opy_:
    bstack1l111lll11_opy_(bstack11l1l11_opy_ (u"ࠣࡒࡤࡧࡰࡧࡧࡦࡵࠣࡲࡴࡺࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠥ๕"), bstack1l1ll1lll1_opy_)
  if bstack11l11l111l_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack11l1l11_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ๖")) and callable(getattr(RemoteConnection, bstack11l1l11_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ๗"))):
        RemoteConnection._get_proxy_url = bstack1ll11ll1l1_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack1ll11ll1l1_opy_
    except Exception as e:
      logger.error(bstack1l1llll1ll_opy_.format(str(e)))
  if bstack11l1ll1l1_opy_():
    bstack1ll1111l11_opy_(CONFIG, logger)
  if (bstack11l1l11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ๘") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1llll11111_opy_() == bstack11l1l11_opy_ (u"ࠧࡺࡲࡶࡧࠥ๙"):
          bstack1l1lll1ll_opy_(bstack111ll111ll_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1l1111l11_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l11l1111l_opy_
      except Exception as e:
        logger.warn(bstack1111l1l1ll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1111l1l1l_opy_
      except Exception as e:
        logger.debug(bstack11l1lll1l_opy_ + str(e))
    except Exception as e:
      bstack1l111lll11_opy_(e, bstack1111l1l1ll_opy_)
    Output.start_test = bstack111lll1lll_opy_
    Output.end_test = bstack1ll111l1l_opy_
    TestStatus.__init__ = bstack1llll1111l_opy_
    QueueItem.__init__ = bstack111l1111l1_opy_
    pabot._create_items = bstack1lll111l1_opy_
    try:
      from pabot import __version__ as bstack1l1l111l1l_opy_
      if version.parse(bstack1l1l111l1l_opy_) >= version.parse(bstack11l1l11_opy_ (u"࠭࠵࠯࠲࠱࠴ࠬ๚")):
        pabot._run = bstack1111111ll_opy_
      elif version.parse(bstack1l1l111l1l_opy_) >= version.parse(bstack11l1l11_opy_ (u"ࠧ࠵࠰࠵࠲࠵࠭๛")):
        pabot._run = bstack11111ll1ll_opy_
      elif version.parse(bstack1l1l111l1l_opy_) >= version.parse(bstack11l1l11_opy_ (u"ࠨ࠴࠱࠵࠺࠴࠰ࠨ๜")):
        pabot._run = bstack1111lllll_opy_
      elif version.parse(bstack1l1l111l1l_opy_) >= version.parse(bstack11l1l11_opy_ (u"ࠩ࠵࠲࠶࠹࠮࠱ࠩ๝")):
        pabot._run = bstack1111ll1111_opy_
      else:
        pabot._run = bstack1l1l11l11_opy_
    except Exception as e:
      pabot._run = bstack1l1l11l11_opy_
    pabot._create_command_for_execution = bstack111l1l1l11_opy_
    pabot._report_results = bstack1ll11lll1l_opy_
  if bstack11l1l11_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ๞") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l111lll11_opy_(e, bstack111ll11ll_opy_)
    Runner.run_hook = bstack1l1111ll11_opy_
    Step.run = bstack11ll1llll1_opy_
  if bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ๟") in str(framework_name).lower():
    if not bstack11l1l1ll1_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1l11lll11l_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1l1111111_opy_
      Config.getoption = bstack1ll1l1111l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1l1lll1l1l_opy_
    except Exception as e:
      pass
def bstack1ll1l1l1l1_opy_():
  global CONFIG
  if bstack11l1l11_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ๠") in CONFIG and int(CONFIG[bstack11l1l11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭๡")]) > 1:
    logger.warn(bstack1111lll1l1_opy_)
def bstack111l11l111_opy_(arg, bstack1llllll11_opy_, bstack11l1llll1l_opy_=None):
  global CONFIG
  global bstack1ll1l11l1l_opy_
  global bstack11l1l1111l_opy_
  global bstack11l1l1ll1_opy_
  global bstack111111ll_opy_
  bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ๢")
  if bstack1llllll11_opy_ and isinstance(bstack1llllll11_opy_, str):
    bstack1llllll11_opy_ = eval(bstack1llllll11_opy_)
  CONFIG = bstack1llllll11_opy_[bstack11l1l11_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨ๣")]
  bstack1ll1l11l1l_opy_ = bstack1llllll11_opy_[bstack11l1l11_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪ๤")]
  bstack11l1l1111l_opy_ = bstack1llllll11_opy_[bstack11l1l11_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ๥")]
  bstack11l1l1ll1_opy_ = bstack1llllll11_opy_[bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ๦")]
  bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭๧"), bstack11l1l1ll1_opy_)
  os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ๨")] = bstack1111ll11ll_opy_
  os.environ[bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌ࠭๩")] = json.dumps(CONFIG)
  os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡉࡗࡅࡣ࡚ࡘࡌࠨ๪")] = bstack1ll1l11l1l_opy_
  os.environ[bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ๫")] = str(bstack11l1l1111l_opy_)
  os.environ[bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡐ࡚ࡍࡉࡏࠩ๬")] = str(True)
  if bstack11111llll1_opy_(arg, [bstack11l1l11_opy_ (u"ࠫ࠲ࡴࠧ๭"), bstack11l1l11_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭๮")]) != -1:
    os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡁࡓࡃࡏࡐࡊࡒࠧ๯")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack11l11111ll_opy_)
    return
  bstack11l1lll111_opy_()
  global bstack1111l1l1l1_opy_
  global bstack1l1111lll1_opy_
  global bstack111ll1l1l1_opy_
  global bstack111l111ll1_opy_
  global bstack1l1ll1l111_opy_
  global bstack1l1l1ll11l_opy_
  global bstack11ll1ll1l1_opy_
  arg.append(bstack11l1l11_opy_ (u"ࠢ࠮࡙ࠥ๰"))
  arg.append(bstack11l1l11_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥ࠻ࡏࡲࡨࡺࡲࡥࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡬ࡱࡵࡵࡲࡵࡧࡧ࠾ࡵࡿࡴࡦࡵࡷ࠲ࡕࡿࡴࡦࡵࡷ࡛ࡦࡸ࡮ࡪࡰࡪࠦ๱"))
  arg.append(bstack11l1l11_opy_ (u"ࠤ࠰࡛ࠧ๲"))
  arg.append(bstack11l1l11_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧ࠽ࡘ࡭࡫ࠠࡩࡱࡲ࡯࡮ࡳࡰ࡭ࠤ๳"))
  global bstack111ll11l11_opy_
  global bstack1111llll1l_opy_
  global bstack1ll1lllll1_opy_
  global bstack11111l1l1_opy_
  global bstack1lll11l111_opy_
  global bstack11l11llll1_opy_
  global bstack1l1111l1l_opy_
  global bstack11111ll1l_opy_
  global bstack1ll1lll111_opy_
  global bstack1lllll11l1_opy_
  global bstack11ll11l1l1_opy_
  global bstack1llllll1ll_opy_
  global bstack111ll1111_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack111ll11l11_opy_ = webdriver.Remote.__init__
    bstack1111llll1l_opy_ = WebDriver.quit
    bstack11111ll1l_opy_ = WebDriver.close
    bstack1ll1lll111_opy_ = WebDriver.get
    bstack1ll1lllll1_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack11l11lll1l_opy_(CONFIG) and bstack11111lll1_opy_():
    if bstack11lll11ll_opy_() < version.parse(bstack1ll1l1l111_opy_):
      logger.error(bstack1l11ll1ll1_opy_.format(bstack11lll11ll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11l1l11_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ๴")) and callable(getattr(RemoteConnection, bstack11l1l11_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭๵"))):
          bstack1lllll11l1_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1lllll11l1_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack1l1llll1ll_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack11ll11l1l1_opy_ = Config.getoption
    from _pytest import runner
    bstack1llllll1ll_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack111l11ll_opy_)
  try:
    from pytest_bdd import reporting
    bstack111ll1111_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11l1l11_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹࡵࠠࡳࡷࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࡹࠧ๶"))
  bstack111ll1l1l1_opy_ = CONFIG.get(bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ๷"), {}).get(bstack11l1l11_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ๸"))
  bstack11ll1ll1l1_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack1ll1l1l1l_opy_():
      bstack11l11lllll_opy_.invoke(Events.CONNECT, bstack111llll1ll_opy_())
    platform_index = int(os.environ.get(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ๹"), bstack11l1l11_opy_ (u"ࠪ࠴ࠬ๺")))
  else:
    bstack1111l11l1_opy_(bstack1ll1ll1ll1_opy_)
  os.environ[bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬ๻")] = CONFIG[bstack11l1l11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ๼")]
  os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩ๽")] = CONFIG[bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ๾")]
  os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ๿")] = bstack11l1l1ll1_opy_.__str__()
  from _pytest.config import main as bstack111ll1l1l_opy_
  bstack11l11l1l11_opy_ = []
  try:
    exit_code = bstack111ll1l1l_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1lll1ll1ll_opy_()
    if bstack11l1l11_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭຀") in multiprocessing.current_process().__dict__.keys():
      for bstack1l1ll1l1l1_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11l11l1l11_opy_.append(bstack1l1ll1l1l1_opy_)
    try:
      bstack11ll11lll1_opy_ = (bstack11l11l1l11_opy_, int(exit_code))
      bstack11l1llll1l_opy_.append(bstack11ll11lll1_opy_)
    except:
      bstack11l1llll1l_opy_.append((bstack11l11l1l11_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack11l11l1l11_opy_.append({bstack11l1l11_opy_ (u"ࠪࡲࡦࡳࡥࠨກ"): bstack11l1l11_opy_ (u"ࠫࡕࡸ࡯ࡤࡧࡶࡷࠥ࠭ຂ") + os.environ.get(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ຃")), bstack11l1l11_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬຄ"): traceback.format_exc(), bstack11l1l11_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭຅"): int(os.environ.get(bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨຆ")))})
    bstack11l1llll1l_opy_.append((bstack11l11l1l11_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack11l1l11_opy_ (u"ࠤࡵࡩࡹࡸࡩࡦࡵࠥງ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack1l111l1l11_opy_ = e.__class__.__name__
    print(bstack11l1l11_opy_ (u"ࠥࠩࡸࡀࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡵࡧࡶࡸࠥࠫࡳࠣຈ") % (bstack1l111l1l11_opy_, e))
    return 1
def bstack1l1111l1ll_opy_(arg):
  global bstack1l1lll1l11_opy_
  bstack1111l11l1_opy_(bstack11l1l1l1ll_opy_)
  os.environ[bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬຉ")] = str(bstack11l1l1111l_opy_)
  retries = bstack11l1l111_opy_.bstack1lllll111_opy_(CONFIG)
  status_code = 0
  if bstack11l1l111_opy_.bstack1lll1l1ll_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack11l1l11lll_opy_
    status_code = bstack11l1l11lll_opy_(arg)
  if status_code != 0:
    bstack1l1lll1l11_opy_ = status_code
def bstack1l1ll1l1ll_opy_():
  logger.info(bstack11lll1l1ll_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11l1l11_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫຊ"), help=bstack11l1l11_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡤࡱࡱࡪ࡮࡭ࠧ຋"))
  parser.add_argument(bstack11l1l11_opy_ (u"ࠧ࠮ࡷࠪຌ"), bstack11l1l11_opy_ (u"ࠨ࠯࠰ࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬຍ"), help=bstack11l1l11_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡵࡴࡧࡵࡲࡦࡳࡥࠨຎ"))
  parser.add_argument(bstack11l1l11_opy_ (u"ࠪ࠱ࡰ࠭ຏ"), bstack11l1l11_opy_ (u"ࠫ࠲࠳࡫ࡦࡻࠪຐ"), help=bstack11l1l11_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾ࠭ຑ"))
  parser.add_argument(bstack11l1l11_opy_ (u"࠭࠭ࡧࠩຒ"), bstack11l1l11_opy_ (u"ࠧ࠮࠯ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬຓ"), help=bstack11l1l11_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧດ"))
  bstack1l1l111l1_opy_ = parser.parse_args()
  try:
    bstack111llll11_opy_ = bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡩࡨࡲࡪࡸࡩࡤ࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭ຕ")
    if bstack1l1l111l1_opy_.framework and bstack1l1l111l1_opy_.framework not in (bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪຖ"), bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬທ")):
      bstack111llll11_opy_ = bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࡺ࡯࡯࠲ࡸࡧ࡭ࡱ࡮ࡨࠫຘ")
    bstack1llll1lll1_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111llll11_opy_)
    bstack1l1ll111l_opy_ = open(bstack1llll1lll1_opy_, bstack11l1l11_opy_ (u"࠭ࡲࠨນ"))
    bstack1lll11lll1_opy_ = bstack1l1ll111l_opy_.read()
    bstack1l1ll111l_opy_.close()
    if bstack1l1l111l1_opy_.username:
      bstack1lll11lll1_opy_ = bstack1lll11lll1_opy_.replace(bstack11l1l11_opy_ (u"࡚ࠧࡑࡘࡖࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧບ"), bstack1l1l111l1_opy_.username)
    if bstack1l1l111l1_opy_.key:
      bstack1lll11lll1_opy_ = bstack1lll11lll1_opy_.replace(bstack11l1l11_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪປ"), bstack1l1l111l1_opy_.key)
    if bstack1l1l111l1_opy_.framework:
      bstack1lll11lll1_opy_ = bstack1lll11lll1_opy_.replace(bstack11l1l11_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪຜ"), bstack1l1l111l1_opy_.framework)
    file_name = bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭ຝ")
    file_path = os.path.abspath(file_name)
    bstack11l11l11ll_opy_ = open(file_path, bstack11l1l11_opy_ (u"ࠫࡼ࠭ພ"))
    bstack11l11l11ll_opy_.write(bstack1lll11lll1_opy_)
    bstack11l11l11ll_opy_.close()
    logger.info(bstack1lll11l1l_opy_)
    try:
      os.environ[bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧຟ")] = bstack1l1l111l1_opy_.framework if bstack1l1l111l1_opy_.framework != None else bstack11l1l11_opy_ (u"ࠨࠢຠ")
      config = yaml.safe_load(bstack1lll11lll1_opy_)
      config[bstack11l1l11_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧມ")] = bstack11l1l11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠮ࡵࡨࡸࡺࡶࠧຢ")
      bstack11lll11l1l_opy_(bstack11ll11l1l_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll11llll1_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack11llll11l_opy_.format(str(e)))
def bstack11lll11l1l_opy_(bstack11111111l_opy_, config, bstack1ll1lll1ll_opy_={}):
  global bstack11l1l1ll1_opy_
  global bstack111l11l11l_opy_
  global bstack111111ll_opy_
  if not config:
    return
  bstack1lll1111ll_opy_ = bstack1ll11l1lll_opy_ if not bstack11l1l1ll1_opy_ else (
    bstack11l11ll11l_opy_ if bstack11l1l11_opy_ (u"ࠩࡤࡴࡵ࠭ຣ") in config else (
        bstack11lllllll1_opy_ if config.get(bstack11l1l11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ຤")) else bstack11111lll11_opy_
    )
)
  bstack1l1l11ll1_opy_ = False
  bstack11ll11l111_opy_ = False
  if bstack11l1l1ll1_opy_ is True:
      if bstack11l1l11_opy_ (u"ࠫࡦࡶࡰࠨລ") in config:
          bstack1l1l11ll1_opy_ = True
      else:
          bstack11ll11l111_opy_ = True
  bstack1l1l111111_opy_ = bstack1l11l1l11l_opy_.bstack1l111l11l1_opy_(config, bstack111l11l11l_opy_)
  bstack1111l1lll_opy_ = bstack1l1ll1l1l_opy_()
  data = {
    bstack11l1l11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ຦"): config[bstack11l1l11_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨວ")],
    bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪຨ"): config[bstack11l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫຩ")],
    bstack11l1l11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ສ"): bstack11111111l_opy_,
    bstack11l1l11_opy_ (u"ࠪࡨࡪࡺࡥࡤࡶࡨࡨࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧຫ"): os.environ.get(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ຬ"), bstack111l11l11l_opy_),
    bstack11l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧອ"): bstack1l111l111_opy_,
    bstack11l1l11_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬ࠨຮ"): bstack1111lll1l_opy_(),
    bstack11l1l11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪຯ"): {
      bstack11l1l11_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ະ"): str(config[bstack11l1l11_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩັ")]) if bstack11l1l11_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪາ") in config else bstack11l1l11_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧຳ"),
      bstack11l1l11_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࡖࡦࡴࡶ࡭ࡴࡴࠧິ"): sys.version,
      bstack11l1l11_opy_ (u"࠭ࡲࡦࡨࡨࡶࡷ࡫ࡲࠨີ"): bstack1l1111lll_opy_(os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩຶ"), bstack111l11l11l_opy_)),
      bstack11l1l11_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪື"): bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ຸࠩ"),
      bstack11l1l11_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷູࠫ"): bstack1lll1111ll_opy_,
      bstack11l1l11_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࡤࡳࡡࡱ຺ࠩ"): bstack1l1l111111_opy_,
      bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡥࡵࡶ࡫ࡧࠫົ"): os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫຼ")],
      bstack11l1l11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪຽ"): os.environ.get(bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ຾"), bstack111l11l11l_opy_),
      bstack11l1l11_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ຿"): bstack111l111ll_opy_(os.environ.get(bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬເ"), bstack111l11l11l_opy_)),
      bstack11l1l11_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪແ"): bstack1111l1lll_opy_.get(bstack11l1l11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪໂ")),
      bstack11l1l11_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬໃ"): bstack1111l1lll_opy_.get(bstack11l1l11_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨໄ")),
      bstack11l1l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ໅"): config[bstack11l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬໆ")] if config[bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໇")] else bstack11l1l11_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲ່ࠧ"),
      bstack11l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸ້ࠧ"): str(config[bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ໊")]) if bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳ໋ࠩ") in config else bstack11l1l11_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤ໌"),
      bstack11l1l11_opy_ (u"ࠩࡲࡷࠬໍ"): sys.platform,
      bstack11l1l11_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬ໎"): socket.gethostname(),
      bstack11l1l11_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭໏"): bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ໐"))
    }
  }
  if not bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭໑")) is None:
    data[bstack11l1l11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ໒")][bstack11l1l11_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡐࡩࡹࡧࡤࡢࡶࡤࠫ໓")] = {
      bstack11l1l11_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩ໔"): bstack11l1l11_opy_ (u"ࠪࡹࡸ࡫ࡲࡠ࡭࡬ࡰࡱ࡫ࡤࠨ໕"),
      bstack11l1l11_opy_ (u"ࠫࡸ࡯ࡧ࡯ࡣ࡯ࠫ໖"): bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ໗")),
      bstack11l1l11_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱࡔࡵ࡮ࡤࡨࡶࠬ໘"): bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡏࡱࠪ໙"))
    }
  if bstack11111111l_opy_ == bstack111l11ll1l_opy_:
    data[bstack11l1l11_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໚")][bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡄࡱࡱࡪ࡮࡭ࠧ໛")] = bstack1l11111l1_opy_(config)
    data[bstack11l1l11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭ໜ")][bstack11l1l11_opy_ (u"ࠫ࡮ࡹࡐࡦࡴࡦࡽࡆࡻࡴࡰࡇࡱࡥࡧࡲࡥࡥࠩໝ")] = percy.bstack1l11lll11_opy_
    data[bstack11l1l11_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨໞ")][bstack11l1l11_opy_ (u"࠭ࡰࡦࡴࡦࡽࡇࡻࡩ࡭ࡦࡌࡨࠬໟ")] = percy.percy_build_id
  if not bstack11l1l111_opy_.bstack11lll1111l_opy_(CONFIG):
    data[bstack11l1l11_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ໠")][bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠬ໡")] = bstack11l1l111_opy_.bstack11lll1111l_opy_(CONFIG)
  bstack11l111ll_opy_ = bstack1lll1ll1l_opy_.bstack1111lll1_opy_(CONFIG, logger)
  bstack1llll11l1_opy_ = bstack11l1l111_opy_.bstack1111lll1_opy_(config=CONFIG)
  if bstack11l111ll_opy_ is not None and bstack1llll11l1_opy_ is not None and bstack1llll11l1_opy_.bstack1lllll11l_opy_():
    data[bstack11l1l11_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໢")][bstack1llll11l1_opy_.bstack111l11l1l1_opy_()] = bstack11l111ll_opy_.bstack1ll1l111ll_opy_()
  update(data[bstack11l1l11_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໣")], bstack1ll1lll1ll_opy_)
  try:
    response = bstack11lll1llll_opy_(bstack11l1l11_opy_ (u"ࠫࡕࡕࡓࡕࠩ໤"), bstack1l11l1l1ll_opy_(bstack1lll111l11_opy_), data, {
      bstack11l1l11_opy_ (u"ࠬࡧࡵࡵࡪࠪ໥"): (config[bstack11l1l11_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ໦")], config[bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ໧")])
    })
    if response:
      logger.debug(bstack1l1ll1ll1l_opy_.format(bstack11111111l_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1ll1111lll_opy_.format(str(e)))
def bstack1l1111lll_opy_(framework):
  return bstack11l1l11_opy_ (u"ࠣࡽࢀ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧ໨").format(str(framework), __version__) if framework else bstack11l1l11_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࡼࡿࠥ໩").format(
    __version__)
def bstack11l1lll111_opy_():
  global CONFIG
  global bstack1l1l111lll_opy_
  if bool(CONFIG):
    return
  try:
    bstack1llll1ll11_opy_()
    logger.debug(bstack1l1ll1l11_opy_.format(str(CONFIG)))
    bstack1l1l111lll_opy_ = bstack1ll1111ll_opy_.configure_logger(CONFIG, bstack1l1l111lll_opy_)
    bstack11l111l11l_opy_()
  except Exception as e:
    logger.error(bstack11l1l11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴ࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࠢ໪") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11l11ll11_opy_
  atexit.register(bstack111l1l1l1l_opy_)
  signal.signal(signal.SIGINT, bstack111lllll11_opy_)
  signal.signal(signal.SIGTERM, bstack111lllll11_opy_)
def bstack11l11ll11_opy_(exctype, value, traceback):
  global bstack11llll1l11_opy_
  try:
    for driver in bstack11llll1l11_opy_:
      bstack11ll1111ll_opy_(driver, bstack11l1l11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ໫"), bstack11l1l11_opy_ (u"࡙ࠧࡥࡴࡵ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣ໬") + str(value))
  except Exception:
    pass
  logger.info(bstack11l111l1ll_opy_)
  bstack11ll111ll1_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack11ll111ll1_opy_(message=bstack11l1l11_opy_ (u"࠭ࠧ໭"), bstack11lll11ll1_opy_ = False):
  global CONFIG
  bstack1l11l11l11_opy_ = bstack11l1l11_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠩ໮") if bstack11lll11ll1_opy_ else bstack11l1l11_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ໯")
  try:
    if message:
      bstack1ll1lll1ll_opy_ = {
        bstack1l11l11l11_opy_ : str(message)
      }
      bstack11lll11l1l_opy_(bstack111l11ll1l_opy_, CONFIG, bstack1ll1lll1ll_opy_)
    else:
      bstack11lll11l1l_opy_(bstack111l11ll1l_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1lll111l1l_opy_.format(str(e)))
def bstack11lllll111_opy_(bstack1l1llll1l_opy_, size):
  bstack1111ll1ll1_opy_ = []
  while len(bstack1l1llll1l_opy_) > size:
    bstack1lll1ll111_opy_ = bstack1l1llll1l_opy_[:size]
    bstack1111ll1ll1_opy_.append(bstack1lll1ll111_opy_)
    bstack1l1llll1l_opy_ = bstack1l1llll1l_opy_[size:]
  bstack1111ll1ll1_opy_.append(bstack1l1llll1l_opy_)
  return bstack1111ll1ll1_opy_
def bstack11lll1ll11_opy_(args):
  if bstack11l1l11_opy_ (u"ࠩ࠰ࡱࠬ໰") in args and bstack11l1l11_opy_ (u"ࠪࡴࡩࡨࠧ໱") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack1l11llll1_opy_, stage=STAGE.bstack111ll111l_opy_)
def run_on_browserstack(bstack111l1l111l_opy_=None, bstack11l1llll1l_opy_=None, bstack1l1l1l1ll_opy_=False):
  global CONFIG
  global bstack1ll1l11l1l_opy_
  global bstack11l1l1111l_opy_
  global bstack111l11l11l_opy_
  global bstack111111ll_opy_
  bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠫࠬ໲")
  bstack1l11llll1l_opy_(bstack1ll1llllll_opy_, logger)
  if bstack111l1l111l_opy_ and isinstance(bstack111l1l111l_opy_, str):
    bstack111l1l111l_opy_ = eval(bstack111l1l111l_opy_)
  if bstack111l1l111l_opy_:
    CONFIG = bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ໳")]
    bstack1ll1l11l1l_opy_ = bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ໴")]
    bstack11l1l1111l_opy_ = bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ໵")]
    bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ໶"), bstack11l1l1111l_opy_)
    bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ໷")
  bstack111111ll_opy_.set_property(bstack11l1l11_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ໸"), uuid4().__str__())
  logger.info(bstack11l1l11_opy_ (u"ࠫࡘࡊࡋࠡࡴࡸࡲࠥࡹࡴࡢࡴࡷࡩࡩࠦࡷࡪࡶ࡫ࠤ࡮ࡪ࠺ࠡࠩ໹") + bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ໺")));
  logger.debug(bstack11l1l11_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤ࠾ࠩ໻") + bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ໼")))
  if not bstack1l1l1l1ll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack11l11111ll_opy_)
      return
    if sys.argv[1] == bstack11l1l11_opy_ (u"ࠨ࠯࠰ࡺࡪࡸࡳࡪࡱࡱࠫ໽") or sys.argv[1] == bstack11l1l11_opy_ (u"ࠩ࠰ࡺࠬ໾"):
      logger.info(bstack11l1l11_opy_ (u"ࠪࡆࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡓࡽࡹ࡮࡯࡯ࠢࡖࡈࡐࠦࡶࡼࡿࠪ໿").format(__version__))
      return
    if sys.argv[1] == bstack11l1l11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪༀ"):
      bstack1l1ll1l1ll_opy_()
      return
  args = sys.argv
  bstack11l1lll111_opy_()
  global bstack1111l1l1l1_opy_
  global bstack1ll11111l_opy_
  global bstack11ll1ll1l1_opy_
  global bstack111l11111l_opy_
  global bstack1l1111lll1_opy_
  global bstack111ll1l1l1_opy_
  global bstack111l111ll1_opy_
  global bstack11ll1ll1ll_opy_
  global bstack1l1ll1l111_opy_
  global bstack1l1l1ll11l_opy_
  global bstack1l11111ll_opy_
  bstack1ll11111l_opy_ = len(CONFIG.get(bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ༁"), []))
  if not bstack1111ll11ll_opy_:
    if args[1] == bstack11l1l11_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭༂") or args[1] == bstack11l1l11_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨ༃"):
      bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ༄")
      args = args[2:]
    elif args[1] == bstack11l1l11_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ༅"):
      bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ༆")
      args = args[2:]
    elif args[1] == bstack11l1l11_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ༇"):
      bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ༈")
      args = args[2:]
    elif args[1] == bstack11l1l11_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ༉"):
      bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ༊")
      args = args[2:]
    elif args[1] == bstack11l1l11_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ་"):
      bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ༌")
      args = args[2:]
    elif args[1] == bstack11l1l11_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ།"):
      bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ༎")
      args = args[2:]
    else:
      if not bstack11l1l11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ༏") in CONFIG or str(CONFIG[bstack11l1l11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༐")]).lower() in [bstack11l1l11_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༑"), bstack11l1l11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩ༒")]:
        bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༓")
        args = args[1:]
      elif str(CONFIG[bstack11l1l11_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭༔")]).lower() == bstack11l1l11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༕"):
        bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༖")
        args = args[1:]
      elif str(CONFIG[bstack11l1l11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༗")]).lower() == bstack11l1l11_opy_ (u"ࠧࡱࡣࡥࡳࡹ༘࠭"):
        bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠨࡲࡤࡦࡴࡺ༙ࠧ")
        args = args[1:]
      elif str(CONFIG[bstack11l1l11_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ༚")]).lower() == bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ༛"):
        bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༜")
        args = args[1:]
      elif str(CONFIG[bstack11l1l11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ༝")]).lower() == bstack11l1l11_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭༞"):
        bstack1111ll11ll_opy_ = bstack11l1l11_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ༟")
        args = args[1:]
      else:
        os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ༠")] = bstack1111ll11ll_opy_
        bstack1l1lllll11_opy_(bstack11l11l1lll_opy_)
  os.environ[bstack11l1l11_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪ༡")] = bstack1111ll11ll_opy_
  bstack111l11l11l_opy_ = bstack1111ll11ll_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1111l1111_opy_ = bstack11ll1l11ll_opy_[bstack11l1l11_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖ࠰ࡆࡉࡊࠧ༢")] if bstack1111ll11ll_opy_ == bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༣") and bstack11ll1ll11_opy_() else bstack1111ll11ll_opy_
      bstack11l11lllll_opy_.invoke(Events.bstack111l111lll_opy_, bstack1llll11lll_opy_(
        sdk_version=__version__,
        path_config=bstack1llll11l1l_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1111l1111_opy_,
        frameworks=[bstack1111l1111_opy_],
        framework_versions={
          bstack1111l1111_opy_: bstack111l111ll_opy_(bstack11l1l11_opy_ (u"ࠬࡘ࡯ࡣࡱࡷࠫ༤") if bstack1111ll11ll_opy_ in [bstack11l1l11_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ༥"), bstack11l1l11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭༦"), bstack11l1l11_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ༧")] else bstack1111ll11ll_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦ༨"), None):
        CONFIG[bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧ༩")] = cli.config.get(bstack11l1l11_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨ༪"), None)
    except Exception as e:
      bstack11l11lllll_opy_.invoke(Events.bstack1ll1l11l1_opy_, e.__traceback__, 1)
    if bstack11l1l1111l_opy_:
      CONFIG[bstack11l1l11_opy_ (u"ࠧࡧࡰࡱࠤ༫")] = cli.config[bstack11l1l11_opy_ (u"ࠨࡡࡱࡲࠥ༬")]
      logger.info(bstack1ll11ll11_opy_.format(CONFIG[bstack11l1l11_opy_ (u"ࠧࡢࡲࡳࠫ༭")]))
  else:
    bstack11l11lllll_opy_.clear()
  global bstack11l111l111_opy_
  global bstack11l1lll1l1_opy_
  if bstack111l1l111l_opy_:
    try:
      bstack1l11lll1l_opy_ = datetime.datetime.now()
      os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ༮")] = bstack1111ll11ll_opy_
      bstack11lll11l1l_opy_(bstack11llll111_opy_, CONFIG)
      cli.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡴࡦ࡮ࡣࡹ࡫ࡳࡵࡡࡤࡸࡹ࡫࡭ࡱࡶࡨࡨࠧ༯"), datetime.datetime.now() - bstack1l11lll1l_opy_)
    except Exception as e:
      logger.debug(bstack11ll1l1ll1_opy_.format(str(e)))
  global bstack111ll11l11_opy_
  global bstack1111llll1l_opy_
  global bstack11l11l1ll1_opy_
  global bstack1l111ll11_opy_
  global bstack111l1llll1_opy_
  global bstack1l11l1111_opy_
  global bstack11111l1l1_opy_
  global bstack1lll11l111_opy_
  global bstack1ll111l111_opy_
  global bstack11l11llll1_opy_
  global bstack1l1111l1l_opy_
  global bstack11111ll1l_opy_
  global bstack11ll1ll1l_opy_
  global bstack1l1l1111l_opy_
  global bstack1ll1lll111_opy_
  global bstack1lllll11l1_opy_
  global bstack11ll11l1l1_opy_
  global bstack1llllll1ll_opy_
  global bstack11ll111lll_opy_
  global bstack111ll1111_opy_
  global bstack1ll1lllll1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack111ll11l11_opy_ = webdriver.Remote.__init__
    bstack1111llll1l_opy_ = WebDriver.quit
    bstack11111ll1l_opy_ = WebDriver.close
    bstack1ll1lll111_opy_ = WebDriver.get
    bstack1ll1lllll1_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack11l111l111_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1lll11ll1l_opy_
    bstack11l1lll1l1_opy_ = bstack1lll11ll1l_opy_()
  except Exception as e:
    pass
  try:
    global bstack1l11l111ll_opy_
    from QWeb.keywords import browser
    bstack1l11l111ll_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack11l11lll1l_opy_(CONFIG) and bstack11111lll1_opy_():
    if bstack11lll11ll_opy_() < version.parse(bstack1ll1l1l111_opy_):
      logger.error(bstack1l11ll1ll1_opy_.format(bstack11lll11ll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11l1l11_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ༰")) and callable(getattr(RemoteConnection, bstack11l1l11_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ༱"))):
          RemoteConnection._get_proxy_url = bstack1ll11ll1l1_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack1ll11ll1l1_opy_
      except Exception as e:
        logger.error(bstack1l1llll1ll_opy_.format(str(e)))
  if not CONFIG.get(bstack11l1l11_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧ༲"), False) and not bstack111l1l111l_opy_:
    logger.info(bstack1lll1l111l_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack11l1l11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ༳") in CONFIG and str(CONFIG[bstack11l1l11_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ༴")]).lower() != bstack11l1l11_opy_ (u"ࠨࡨࡤࡰࡸ࡫༵ࠧ"):
      bstack111l1lll11_opy_()
    elif bstack1111ll11ll_opy_ != bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༶") or (bstack1111ll11ll_opy_ == bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ༷ࠪ") and not bstack111l1l111l_opy_):
      bstack1l11l1lll1_opy_()
  if (bstack1111ll11ll_opy_ in [bstack11l1l11_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ༸"), bstack11l1l11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ༹ࠫ"), bstack11l1l11_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ༺")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1l1111l11_opy_
        bstack1l11l1111_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1111l1l1ll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack111l1llll1_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack11l1lll1l_opy_ + str(e))
    except Exception as e:
      bstack1l111lll11_opy_(e, bstack1111l1l1ll_opy_)
    if bstack1111ll11ll_opy_ != bstack11l1l11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ༻"):
      bstack1l111111l_opy_()
    bstack11l11l1ll1_opy_ = Output.start_test
    bstack1l111ll11_opy_ = Output.end_test
    bstack11111l1l1_opy_ = TestStatus.__init__
    bstack1ll111l111_opy_ = pabot._run
    bstack11l11llll1_opy_ = QueueItem.__init__
    bstack1l1111l1l_opy_ = pabot._create_command_for_execution
    bstack11ll111lll_opy_ = pabot._report_results
  if bstack1111ll11ll_opy_ == bstack11l1l11_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ༼"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l111lll11_opy_(e, bstack111ll11ll_opy_)
    bstack11ll1ll1l_opy_ = Runner.run_hook
    bstack1l1l1111l_opy_ = Step.run
  if bstack1111ll11ll_opy_ == bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ༽"):
    try:
      from _pytest.config import Config
      bstack11ll11l1l1_opy_ = Config.getoption
      from _pytest import runner
      bstack1llllll1ll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack111l11ll_opy_)
    try:
      from pytest_bdd import reporting
      bstack111ll1111_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11l1l11_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫ༾"))
  try:
    framework_name = bstack11l1l11_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༿") if bstack1111ll11ll_opy_ in [bstack11l1l11_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫཀ"), bstack11l1l11_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬཁ"), bstack11l1l11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨག")] else bstack11llll1l1l_opy_(bstack1111ll11ll_opy_)
    bstack11l1l1l11_opy_ = {
      bstack11l1l11_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠩགྷ"): bstack11l1l11_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫང") if bstack1111ll11ll_opy_ == bstack11l1l11_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪཅ") and bstack11ll1ll11_opy_() else framework_name,
      bstack11l1l11_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨཆ"): bstack111l111ll_opy_(framework_name),
      bstack11l1l11_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪཇ"): __version__,
      bstack11l1l11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡸࡷࡪࡪࠧ཈"): bstack1111ll11ll_opy_
    }
    if bstack1111ll11ll_opy_ in bstack111l1ll1l1_opy_ + bstack11ll111ll_opy_:
      if bstack111l1lll_opy_.bstack111l1111l_opy_(CONFIG):
        if bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧཉ") in CONFIG:
          os.environ[bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩཊ")] = os.getenv(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪཋ"), json.dumps(CONFIG[bstack11l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪཌ")]))
          CONFIG[bstack11l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫཌྷ")].pop(bstack11l1l11_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪཎ"), None)
          CONFIG[bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ཏ")].pop(bstack11l1l11_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬཐ"), None)
        bstack11l1l1l11_opy_[bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨད")] = {
          bstack11l1l11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧདྷ"): bstack11l1l11_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬན"),
          bstack11l1l11_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬཔ"): str(bstack11lll11ll_opy_())
        }
    if bstack1111ll11ll_opy_ not in [bstack11l1l11_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ཕ")] and not cli.is_running():
      bstack1l1llll11l_opy_, bstack1ll11l11l1_opy_ = bstack1l1lll1l_opy_.launch(CONFIG, bstack11l1l1l11_opy_)
      if bstack1ll11l11l1_opy_.get(bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭བ")) is not None and bstack111l1lll_opy_.bstack1llllll11l_opy_(CONFIG) is None:
        value = bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧབྷ")].get(bstack11l1l11_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩམ"))
        if value is not None:
            CONFIG[bstack11l1l11_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩཙ")] = value
        else:
          logger.debug(bstack11l1l11_opy_ (u"ࠥࡒࡴࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡤࡢࡶࡤࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡲࡦࡵࡳࡳࡳࡹࡥࠣཚ"))
  except Exception as e:
    logger.debug(bstack1l1ll11lll_opy_.format(bstack11l1l11_opy_ (u"࡙ࠫ࡫ࡳࡵࡊࡸࡦࠬཛ"), str(e)))
  if bstack1111ll11ll_opy_ == bstack11l1l11_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬཛྷ"):
    bstack11ll1ll1l1_opy_ = True
    if bstack111l1l111l_opy_ and bstack1l1l1l1ll_opy_:
      bstack111ll1l1l1_opy_ = CONFIG.get(bstack11l1l11_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪཝ"), {}).get(bstack11l1l11_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩཞ"))
      bstack1111l11l1_opy_(bstack1l1ll11l11_opy_)
    elif bstack111l1l111l_opy_:
      bstack111ll1l1l1_opy_ = CONFIG.get(bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬཟ"), {}).get(bstack11l1l11_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫའ"))
      global bstack11llll1l11_opy_
      try:
        if bstack11lll1ll11_opy_(bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ཡ")]) and multiprocessing.current_process().name == bstack11l1l11_opy_ (u"ࠫ࠵࠭ར"):
          bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨལ")].remove(bstack11l1l11_opy_ (u"࠭࠭࡮ࠩཤ"))
          bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪཥ")].remove(bstack11l1l11_opy_ (u"ࠨࡲࡧࡦࠬས"))
          bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬཧ")] = bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ཨ")][0]
          with open(bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཀྵ")], bstack11l1l11_opy_ (u"ࠬࡸࠧཪ")) as f:
            file_content = f.read()
          bstack1ll1ll1lll_opy_ = bstack11l1l11_opy_ (u"ࠨࠢࠣࡨࡵࡳࡲࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡤ࡬ࠢ࡬ࡱࡵࡵࡲࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡀࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡦࠪࡾࢁ࠮ࡁࠠࡧࡴࡲࡱࠥࡶࡤࡣࠢ࡬ࡱࡵࡵࡲࡵࠢࡓࡨࡧࡁࠠࡰࡩࡢࡨࡧࠦ࠽ࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱ࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡫ࡦࠡ࡯ࡲࡨࡤࡨࡲࡦࡣ࡮ࠬࡸ࡫࡬ࡧ࠮ࠣࡥࡷ࡭ࠬࠡࡶࡨࡱࡵࡵࡲࡢࡴࡼࠤࡂࠦ࠰ࠪ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡵࡽ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡡࡳࡩࠣࡁࠥࡹࡴࡳࠪ࡬ࡲࡹ࠮ࡡࡳࡩࠬ࠯࠶࠶ࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡥࡹࡥࡨࡴࡹࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡤࡷࠥ࡫࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡤࡷࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡴ࡭࡟ࡥࡤࠫࡷࡪࡲࡦ࠭ࡣࡵ࡫࠱ࡺࡥ࡮ࡲࡲࡶࡦࡸࡹࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡖࡤࡣ࠰ࡧࡳࡤࡨࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡒࡧࡦ࠭࠯࠮ࡴࡧࡷࡣࡹࡸࡡࡤࡧࠫ࠭ࡡࡴࠢࠣࠤཫ").format(str(bstack111l1l111l_opy_))
          bstack11lllll1ll_opy_ = bstack1ll1ll1lll_opy_ + file_content
          bstack11ll11llll_opy_ = bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪཬ")] + bstack11l1l11_opy_ (u"ࠨࡡࡥࡷࡹࡧࡣ࡬ࡡࡷࡩࡲࡶ࠮ࡱࡻࠪ཭")
          with open(bstack11ll11llll_opy_, bstack11l1l11_opy_ (u"ࠩࡺࠫ཮")):
            pass
          with open(bstack11ll11llll_opy_, bstack11l1l11_opy_ (u"ࠥࡻ࠰ࠨ཯")) as f:
            f.write(bstack11lllll1ll_opy_)
          import subprocess
          process_data = subprocess.run([bstack11l1l11_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࠦ཰"), bstack11ll11llll_opy_])
          if os.path.exists(bstack11ll11llll_opy_):
            os.unlink(bstack11ll11llll_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack11lll1ll11_opy_(bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཱ")]):
            bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦིࠩ")].remove(bstack11l1l11_opy_ (u"ࠧ࠮࡯ཱིࠪ"))
            bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨུࠫ")].remove(bstack11l1l11_opy_ (u"ࠩࡳࡨࡧཱུ࠭"))
            bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྲྀ")] = bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཷ")][0]
          bstack1111l11l1_opy_(bstack1l1ll11l11_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨླྀ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11l1l11_opy_ (u"࠭࡟ࡠࡰࡤࡱࡪࡥ࡟ࠨཹ")] = bstack11l1l11_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠེࠩ")
          mod_globals[bstack11l1l11_opy_ (u"ࠨࡡࡢࡪ࡮ࡲࡥࡠࡡཻࠪ")] = os.path.abspath(bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩོࠬ")])
          exec(open(bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪཽ࠭")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11l1l11_opy_ (u"ࠫࡈࡧࡵࡨࡪࡷࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠫཾ").format(str(e)))
          for driver in bstack11llll1l11_opy_:
            bstack11l1llll1l_opy_.append({
              bstack11l1l11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪཿ"): bstack111l1l111l_opy_[bstack11l1l11_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦྀࠩ")],
              bstack11l1l11_opy_ (u"ࠧࡦࡴࡵࡳࡷཱྀ࠭"): str(e),
              bstack11l1l11_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧྂ"): multiprocessing.current_process().name
            })
            bstack11ll1111ll_opy_(driver, bstack11l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩྃ"), bstack11l1l11_opy_ (u"ࠥࡗࡪࡹࡳࡪࡱࡱࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨ྄") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack11llll1l11_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11l1l1111l_opy_, CONFIG, logger)
      bstack111l11lll_opy_()
      bstack1ll1l1l1l1_opy_()
      percy.bstack1l1l1l1l1_opy_()
      bstack1llllll11_opy_ = {
        bstack11l1l11_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ྅"): args[0],
        bstack11l1l11_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ྆"): CONFIG,
        bstack11l1l11_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ྇"): bstack1ll1l11l1l_opy_,
        bstack11l1l11_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩྈ"): bstack11l1l1111l_opy_
      }
      if bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫྉ") in CONFIG:
        bstack11lll11l11_opy_ = bstack11l1111l11_opy_(args, logger, CONFIG, bstack11l1l1ll1_opy_, bstack1ll11111l_opy_)
        bstack11ll1ll1ll_opy_ = bstack11lll11l11_opy_.bstack1llll11ll_opy_(run_on_browserstack, bstack1llllll11_opy_, bstack11lll1ll11_opy_(args))
      else:
        if bstack11lll1ll11_opy_(args):
          bstack1llllll11_opy_[bstack11l1l11_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྊ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1llllll11_opy_,))
          test.start()
          test.join()
        else:
          bstack1111l11l1_opy_(bstack1l1ll11l11_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11l1l11_opy_ (u"ࠪࡣࡤࡴࡡ࡮ࡧࡢࡣࠬྋ")] = bstack11l1l11_opy_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ྌ")
          mod_globals[bstack11l1l11_opy_ (u"ࠬࡥ࡟ࡧ࡫࡯ࡩࡤࡥࠧྍ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1111ll11ll_opy_ == bstack11l1l11_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬྎ") or bstack1111ll11ll_opy_ == bstack11l1l11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ྏ"):
    percy.init(bstack11l1l1111l_opy_, CONFIG, logger)
    percy.bstack1l1l1l1l1_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l111lll11_opy_(e, bstack1111l1l1ll_opy_)
    bstack111l11lll_opy_()
    bstack1111l11l1_opy_(bstack1l111ll1l1_opy_)
    if bstack11l1l1ll1_opy_:
      bstack1l11l11ll_opy_(bstack1l111ll1l1_opy_, args)
      if bstack11l1l11_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ྐ") in args:
        i = args.index(bstack11l1l11_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧྑ"))
        args.pop(i)
        args.pop(i)
      if bstack11l1l11_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྒ") not in CONFIG:
        CONFIG[bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྒྷ")] = [{}]
        bstack1ll11111l_opy_ = 1
      if bstack1111l1l1l1_opy_ == 0:
        bstack1111l1l1l1_opy_ = 1
      args.insert(0, str(bstack1111l1l1l1_opy_))
      args.insert(0, str(bstack11l1l11_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪྔ")))
    if bstack1l1lll1l_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack111l11lll1_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1l1llll111_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11l1l11_opy_ (u"ࠨࡒࡐࡄࡒࡘࡤࡕࡐࡕࡋࡒࡒࡘࠨྕ"),
        ).parse_args(bstack111l11lll1_opy_)
        bstack111lllllll_opy_ = args.index(bstack111l11lll1_opy_[0]) if len(bstack111l11lll1_opy_) > 0 else len(args)
        args.insert(bstack111lllllll_opy_, str(bstack11l1l11_opy_ (u"ࠧ࠮࠯࡯࡭ࡸࡺࡥ࡯ࡧࡵࠫྖ")))
        args.insert(bstack111lllllll_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1l11_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡴࡲࡦࡴࡺ࡟࡭࡫ࡶࡸࡪࡴࡥࡳ࠰ࡳࡽࠬྗ"))))
        if bstack11l1l111_opy_.bstack1lll1l1ll_opy_(CONFIG):
          args.insert(bstack111lllllll_opy_, str(bstack11l1l11_opy_ (u"ࠩ࠰࠱ࡱ࡯ࡳࡵࡧࡱࡩࡷ࠭྘")))
          args.insert(bstack111lllllll_opy_ + 1, str(bstack11l1l11_opy_ (u"ࠪࡖࡪࡺࡲࡺࡈࡤ࡭ࡱ࡫ࡤ࠻ࡽࢀࠫྙ").format(bstack11l1l111_opy_.bstack1lllll111_opy_(CONFIG))))
        if bstack1lll1ll1l1_opy_(os.environ.get(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠩྚ"))) and str(os.environ.get(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠩྛ"), bstack11l1l11_opy_ (u"࠭࡮ࡶ࡮࡯ࠫྜ"))) != bstack11l1l11_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬྜྷ"):
          for bstack1ll11l11l_opy_ in bstack1l1llll111_opy_:
            args.remove(bstack1ll11l11l_opy_)
          test_files = os.environ.get(bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬྞ")).split(bstack11l1l11_opy_ (u"ࠩ࠯ࠫྟ"))
          for bstack1llll1l1l_opy_ in test_files:
            args.append(bstack1llll1l1l_opy_)
      except Exception as e:
        logger.error(bstack11l1l11_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡣࡷࡸࡦࡩࡨࡪࡰࡪࠤࡱ࡯ࡳࡵࡧࡱࡩࡷࠦࡦࡰࡴࠣࡿࢂ࠴ࠠࡆࡴࡵࡳࡷࠦ࠭ࠡࡽࢀࠦྠ").format(bstack11l1111l1l_opy_, e))
    pabot.main(args)
  elif bstack1111ll11ll_opy_ == bstack11l1l11_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬྡ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l111lll11_opy_(e, bstack1111l1l1ll_opy_)
    for a in args:
      if bstack11l1l11_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫྡྷ") in a:
        bstack1l1111lll1_opy_ = int(a.split(bstack11l1l11_opy_ (u"࠭࠺ࠨྣ"))[1])
      if bstack11l1l11_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫྤ") in a:
        bstack111ll1l1l1_opy_ = str(a.split(bstack11l1l11_opy_ (u"ࠨ࠼ࠪྥ"))[1])
      if bstack11l1l11_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡅࡏࡍࡆࡘࡇࡔࠩྦ") in a:
        bstack111l111ll1_opy_ = str(a.split(bstack11l1l11_opy_ (u"ࠪ࠾ࠬྦྷ"))[1])
    bstack1ll1l1llll_opy_ = None
    if bstack11l1l11_opy_ (u"ࠫ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠪྨ") in args:
      i = args.index(bstack11l1l11_opy_ (u"ࠬ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠫྩ"))
      args.pop(i)
      bstack1ll1l1llll_opy_ = args.pop(i)
    if bstack1ll1l1llll_opy_ is not None:
      global bstack1l11ll1lll_opy_
      bstack1l11ll1lll_opy_ = bstack1ll1l1llll_opy_
    bstack1111l11l1_opy_(bstack1l111ll1l1_opy_)
    run_cli(args)
    if bstack11l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪྪ") in multiprocessing.current_process().__dict__.keys():
      for bstack1l1ll1l1l1_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11l1llll1l_opy_.append(bstack1l1ll1l1l1_opy_)
  elif bstack1111ll11ll_opy_ == bstack11l1l11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧྫ"):
    bstack1l1l1ll111_opy_ = bstack11111l11_opy_(args, logger, CONFIG, bstack11l1l1ll1_opy_)
    bstack1l1l1ll111_opy_.bstack1111ll11_opy_()
    bstack111l11lll_opy_()
    bstack111l11111l_opy_ = True
    bstack1l1l1ll11l_opy_ = bstack1l1l1ll111_opy_.bstack111ll11l_opy_()
    bstack1l1l1ll111_opy_.bstack1llllll11_opy_(bstack1l1l1ll1l1_opy_)
    bstack1l1l1ll111_opy_.bstack111l1ll1_opy_()
    bstack11ll11lll_opy_(bstack1111ll11ll_opy_, CONFIG, bstack1l1l1ll111_opy_.bstack1111l11l_opy_())
    bstack11111l1l11_opy_ = bstack1l1l1ll111_opy_.bstack1llll11ll_opy_(bstack111l11l111_opy_, {
      bstack11l1l11_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩྫྷ"): bstack1ll1l11l1l_opy_,
      bstack11l1l11_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫྭ"): bstack11l1l1111l_opy_,
      bstack11l1l11_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ྮ"): bstack11l1l1ll1_opy_
    })
    try:
      bstack11l11l1l11_opy_, bstack111ll1ll1l_opy_ = map(list, zip(*bstack11111l1l11_opy_))
      bstack1l1ll1l111_opy_ = bstack11l11l1l11_opy_[0]
      for status_code in bstack111ll1ll1l_opy_:
        if status_code != 0:
          bstack1l11111ll_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11l1l11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡣࡹࡩࠥ࡫ࡲࡳࡱࡵࡷࠥࡧ࡮ࡥࠢࡶࡸࡦࡺࡵࡴࠢࡦࡳࡩ࡫࠮ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࠿ࠦࡻࡾࠤྯ").format(str(e)))
  elif bstack1111ll11ll_opy_ == bstack11l1l11_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬྰ"):
    try:
      from behave.__main__ import main as bstack11l1l11lll_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l111lll11_opy_(e, bstack111ll11ll_opy_)
    bstack111l11lll_opy_()
    bstack111l11111l_opy_ = True
    bstack11l11l11_opy_ = 1
    if bstack11l1l11_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ྱ") in CONFIG:
      bstack11l11l11_opy_ = CONFIG[bstack11l1l11_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧྲ")]
    if bstack11l1l11_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫླ") in CONFIG:
      bstack1ll1ll1l11_opy_ = int(bstack11l11l11_opy_) * int(len(CONFIG[bstack11l1l11_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྴ")]))
    else:
      bstack1ll1ll1l11_opy_ = int(bstack11l11l11_opy_)
    config = Configuration(args)
    bstack1l1lll1111_opy_ = config.paths
    if len(bstack1l1lll1111_opy_) == 0:
      import glob
      pattern = bstack11l1l11_opy_ (u"ࠪ࠮࠯࠵ࠪ࠯ࡨࡨࡥࡹࡻࡲࡦࠩྵ")
      bstack1ll1llll1_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1ll1llll1_opy_)
      config = Configuration(args)
      bstack1l1lll1111_opy_ = config.paths
    bstack11l11lll_opy_ = [os.path.normpath(item) for item in bstack1l1lll1111_opy_]
    bstack1lllllll1l_opy_ = [os.path.normpath(item) for item in args]
    bstack11111lllll_opy_ = [item for item in bstack1lllllll1l_opy_ if item not in bstack11l11lll_opy_]
    import platform as pf
    if pf.system().lower() == bstack11l1l11_opy_ (u"ࠫࡼ࡯࡮ࡥࡱࡺࡷࠬྶ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack11l11lll_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11l111lll1_opy_)))
                    for bstack11l111lll1_opy_ in bstack11l11lll_opy_]
    bstack11l11111_opy_ = []
    for spec in bstack11l11lll_opy_:
      bstack1111l1ll_opy_ = []
      bstack1111l1ll_opy_ += bstack11111lllll_opy_
      bstack1111l1ll_opy_.append(spec)
      bstack11l11111_opy_.append(bstack1111l1ll_opy_)
    execution_items = []
    for bstack1111l1ll_opy_ in bstack11l11111_opy_:
      if bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨྷ") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack11l1l11_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩྸ")]):
          item = {}
          item[bstack11l1l11_opy_ (u"ࠧࡢࡴࡪࠫྐྵ")] = bstack11l1l11_opy_ (u"ࠨࠢࠪྺ").join(bstack1111l1ll_opy_)
          item[bstack11l1l11_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨྻ")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack11l1l11_opy_ (u"ࠪࡥࡷ࡭ࠧྼ")] = bstack11l1l11_opy_ (u"ࠫࠥ࠭྽").join(bstack1111l1ll_opy_)
        item[bstack11l1l11_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ྾")] = 0
        execution_items.append(item)
    bstack1lll11111l_opy_ = bstack11lllll111_opy_(execution_items, bstack1ll1ll1l11_opy_)
    for execution_item in bstack1lll11111l_opy_:
      bstack1lll1llll_opy_ = []
      for item in execution_item:
        bstack1lll1llll_opy_.append(bstack1l11l1l11_opy_(name=str(item[bstack11l1l11_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ྿")]),
                                             target=bstack1l1111l1ll_opy_,
                                             args=(item[bstack11l1l11_opy_ (u"ࠧࡢࡴࡪࠫ࿀")],)))
      for t in bstack1lll1llll_opy_:
        t.start()
      for t in bstack1lll1llll_opy_:
        t.join()
  else:
    bstack1l1lllll11_opy_(bstack11l11l1lll_opy_)
  if not bstack111l1l111l_opy_:
    bstack111lll1ll1_opy_()
    if(bstack1111ll11ll_opy_ in [bstack11l1l11_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ࿁"), bstack11l1l11_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ࿂")]):
      bstack1l1111l11l_opy_()
  bstack1ll1111ll_opy_.bstack1l1ll1ll1_opy_()
def browserstack_initialize(bstack11l1lll11l_opy_=None):
  logger.info(bstack11l1l11_opy_ (u"ࠪࡖࡺࡴ࡮ࡪࡰࡪࠤࡘࡊࡋࠡࡹ࡬ࡸ࡭ࠦࡡࡳࡩࡶ࠾ࠥ࠭࿃") + str(bstack11l1lll11l_opy_))
  run_on_browserstack(bstack11l1lll11l_opy_, None, True)
@measure(event_name=EVENTS.bstack1l11l11lll_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack111lll1ll1_opy_():
  global CONFIG
  global bstack111l11l11l_opy_
  global bstack1l11111ll_opy_
  global bstack1l1lll1l11_opy_
  global bstack111111ll_opy_
  bstack1111l1l111_opy_.bstack1l11ll1111_opy_()
  if cli.is_running():
    bstack11l11lllll_opy_.invoke(Events.bstack1lll11llll_opy_)
  else:
    bstack1llll11l1_opy_ = bstack11l1l111_opy_.bstack1111lll1_opy_(config=CONFIG)
    bstack1llll11l1_opy_.bstack11111lll1l_opy_(CONFIG)
  if bstack111l11l11l_opy_ == bstack11l1l11_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ࿄"):
    if not cli.is_enabled(CONFIG):
      bstack1l1lll1l_opy_.stop()
  else:
    bstack1l1lll1l_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1ll1l1ll_opy_.bstack11llll11ll_opy_()
  if bstack11l1l11_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ࿅") in CONFIG and str(CONFIG[bstack11l1l11_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧ࿆ࠪ")]).lower() != bstack11l1l11_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭࿇"):
    hashed_id, bstack1lll1111l_opy_ = bstack1l1llll11_opy_()
  else:
    hashed_id, bstack1lll1111l_opy_ = get_build_link()
  bstack1ll11111l1_opy_(hashed_id)
  logger.info(bstack11l1l11_opy_ (u"ࠨࡕࡇࡏࠥࡸࡵ࡯ࠢࡨࡲࡩ࡫ࡤࠡࡨࡲࡶࠥ࡯ࡤ࠻ࠩ࿈") + bstack111111ll_opy_.get_property(bstack11l1l11_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ࿉"), bstack11l1l11_opy_ (u"ࠪࠫ࿊")) + bstack11l1l11_opy_ (u"ࠫ࠱ࠦࡴࡦࡵࡷ࡬ࡺࡨࠠࡪࡦ࠽ࠤࠬ࿋") + os.getenv(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ࿌"), bstack11l1l11_opy_ (u"࠭ࠧ࿍")))
  if hashed_id is not None and bstack111l11llll_opy_() != -1:
    sessions = bstack1l1111l111_opy_(hashed_id)
    bstack1llll111ll_opy_(sessions, bstack1lll1111l_opy_)
  if bstack111l11l11l_opy_ == bstack11l1l11_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ࿎") and bstack1l11111ll_opy_ != 0:
    sys.exit(bstack1l11111ll_opy_)
  if bstack111l11l11l_opy_ == bstack11l1l11_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ࿏") and bstack1l1lll1l11_opy_ != 0:
    sys.exit(bstack1l1lll1l11_opy_)
def bstack1ll11111l1_opy_(new_id):
    global bstack1l111l111_opy_
    bstack1l111l111_opy_ = new_id
def bstack11llll1l1l_opy_(bstack1l1l1l1ll1_opy_):
  if bstack1l1l1l1ll1_opy_:
    return bstack1l1l1l1ll1_opy_.capitalize()
  else:
    return bstack11l1l11_opy_ (u"ࠩࠪ࿐")
@measure(event_name=EVENTS.bstack1ll1ll11ll_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1l1l11l11l_opy_(bstack1l1lll111l_opy_):
  if bstack11l1l11_opy_ (u"ࠪࡲࡦࡳࡥࠨ࿑") in bstack1l1lll111l_opy_ and bstack1l1lll111l_opy_[bstack11l1l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ࿒")] != bstack11l1l11_opy_ (u"ࠬ࠭࿓"):
    return bstack1l1lll111l_opy_[bstack11l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ࿔")]
  else:
    bstack111111ll1_opy_ = bstack11l1l11_opy_ (u"ࠢࠣ࿕")
    if bstack11l1l11_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ࿖") in bstack1l1lll111l_opy_ and bstack1l1lll111l_opy_[bstack11l1l11_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ࿗")] != None:
      bstack111111ll1_opy_ += bstack1l1lll111l_opy_[bstack11l1l11_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ࿘")] + bstack11l1l11_opy_ (u"ࠦ࠱ࠦࠢ࿙")
      if bstack1l1lll111l_opy_[bstack11l1l11_opy_ (u"ࠬࡵࡳࠨ࿚")] == bstack11l1l11_opy_ (u"ࠨࡩࡰࡵࠥ࿛"):
        bstack111111ll1_opy_ += bstack11l1l11_opy_ (u"ࠢࡪࡑࡖࠤࠧ࿜")
      bstack111111ll1_opy_ += (bstack1l1lll111l_opy_[bstack11l1l11_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ࿝")] or bstack11l1l11_opy_ (u"ࠩࠪ࿞"))
      return bstack111111ll1_opy_
    else:
      bstack111111ll1_opy_ += bstack11llll1l1l_opy_(bstack1l1lll111l_opy_[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫ࿟")]) + bstack11l1l11_opy_ (u"ࠦࠥࠨ࿠") + (
              bstack1l1lll111l_opy_[bstack11l1l11_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ࿡")] or bstack11l1l11_opy_ (u"࠭ࠧ࿢")) + bstack11l1l11_opy_ (u"ࠢ࠭ࠢࠥ࿣")
      if bstack1l1lll111l_opy_[bstack11l1l11_opy_ (u"ࠨࡱࡶࠫ࿤")] == bstack11l1l11_opy_ (u"ࠤ࡚࡭ࡳࡪ࡯ࡸࡵࠥ࿥"):
        bstack111111ll1_opy_ += bstack11l1l11_opy_ (u"࡛ࠥ࡮ࡴࠠࠣ࿦")
      bstack111111ll1_opy_ += bstack1l1lll111l_opy_[bstack11l1l11_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ࿧")] or bstack11l1l11_opy_ (u"ࠬ࠭࿨")
      return bstack111111ll1_opy_
@measure(event_name=EVENTS.bstack1l11l11l1_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1l1l11l1l1_opy_(bstack1111ll1l1l_opy_):
  if bstack1111ll1l1l_opy_ == bstack11l1l11_opy_ (u"ࠨࡤࡰࡰࡨࠦ࿩"):
    return bstack11l1l11_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡪࡶࡪ࡫࡮࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡪࡶࡪ࡫࡮ࠣࡀࡆࡳࡲࡶ࡬ࡦࡶࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ࿪")
  elif bstack1111ll1l1l_opy_ == bstack11l1l11_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ࿫"):
    return bstack11l1l11_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡷ࡫ࡤ࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡵࡩࡩࠨ࠾ࡇࡣ࡬ࡰࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ࿬")
  elif bstack1111ll1l1l_opy_ == bstack11l1l11_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ࿭"):
    return bstack11l1l11_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡧࡳࡧࡨࡲࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡧࡳࡧࡨࡲࠧࡄࡐࡢࡵࡶࡩࡩࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ࿮")
  elif bstack1111ll1l1l_opy_ == bstack11l1l11_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦ࿯"):
    return bstack11l1l11_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡴࡨࡨࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡲࡦࡦࠥࡂࡊࡸࡲࡰࡴ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ࿰")
  elif bstack1111ll1l1l_opy_ == bstack11l1l11_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣ࿱"):
    return bstack11l1l11_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࠧࡪ࡫ࡡ࠴࠴࠹࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࠩࡥࡦࡣ࠶࠶࠻ࠨ࠾ࡕ࡫ࡰࡩࡴࡻࡴ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭࿲")
  elif bstack1111ll1l1l_opy_ == bstack11l1l11_opy_ (u"ࠤࡵࡹࡳࡴࡩ࡯ࡩࠥ࿳"):
    return bstack11l1l11_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡨ࡬ࡢࡥ࡮࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡨ࡬ࡢࡥ࡮ࠦࡃࡘࡵ࡯ࡰ࡬ࡲ࡬ࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ࿴")
  else:
    return bstack11l1l11_opy_ (u"ࠫࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࠨ࿵") + bstack11llll1l1l_opy_(
      bstack1111ll1l1l_opy_) + bstack11l1l11_opy_ (u"ࠬࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ࿶")
def bstack11l1111l1_opy_(session):
  return bstack11l1l11_opy_ (u"࠭࠼ࡵࡴࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡶࡴࡽࠢ࠿࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠣࡷࡪࡹࡳࡪࡱࡱ࠱ࡳࡧ࡭ࡦࠤࡁࡀࡦࠦࡨࡳࡧࡩࡁࠧࢁࡽࠣࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥࡣࡧࡲࡡ࡯࡭ࠥࡂࢀࢃ࠼࠰ࡣࡁࡀ࠴ࡺࡤ࠿ࡽࢀࡿࢂࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽࠱ࡷࡶࡃ࠭࿷").format(
    session[bstack11l1l11_opy_ (u"ࠧࡱࡷࡥࡰ࡮ࡩ࡟ࡶࡴ࡯ࠫ࿸")], bstack1l1l11l11l_opy_(session), bstack1l1l11l1l1_opy_(session[bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡶࡤࡸࡺࡹࠧ࿹")]),
    bstack1l1l11l1l1_opy_(session[bstack11l1l11_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ࿺")]),
    bstack11llll1l1l_opy_(session[bstack11l1l11_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫ࿻")] or session[bstack11l1l11_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ࿼")] or bstack11l1l11_opy_ (u"ࠬ࠭࿽")) + bstack11l1l11_opy_ (u"ࠨࠠࠣ࿾") + (session[bstack11l1l11_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ࿿")] or bstack11l1l11_opy_ (u"ࠨࠩက")),
    session[bstack11l1l11_opy_ (u"ࠩࡲࡷࠬခ")] + bstack11l1l11_opy_ (u"ࠥࠤࠧဂ") + session[bstack11l1l11_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨဃ")], session[bstack11l1l11_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧင")] or bstack11l1l11_opy_ (u"࠭ࠧစ"),
    session[bstack11l1l11_opy_ (u"ࠧࡤࡴࡨࡥࡹ࡫ࡤࡠࡣࡷࠫဆ")] if session[bstack11l1l11_opy_ (u"ࠨࡥࡵࡩࡦࡺࡥࡥࡡࡤࡸࠬဇ")] else bstack11l1l11_opy_ (u"ࠩࠪဈ"))
@measure(event_name=EVENTS.bstack1l11l11111_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def bstack1llll111ll_opy_(sessions, bstack1lll1111l_opy_):
  try:
    bstack1llll11ll1_opy_ = bstack11l1l11_opy_ (u"ࠥࠦဉ")
    if not os.path.exists(bstack11l1ll1l11_opy_):
      os.mkdir(bstack11l1ll1l11_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1l11_opy_ (u"ࠫࡦࡹࡳࡦࡶࡶ࠳ࡷ࡫ࡰࡰࡴࡷ࠲࡭ࡺ࡭࡭ࠩည")), bstack11l1l11_opy_ (u"ࠬࡸࠧဋ")) as f:
      bstack1llll11ll1_opy_ = f.read()
    bstack1llll11ll1_opy_ = bstack1llll11ll1_opy_.replace(bstack11l1l11_opy_ (u"࠭ࡻࠦࡔࡈࡗ࡚ࡒࡔࡔࡡࡆࡓ࡚ࡔࡔࠦࡿࠪဌ"), str(len(sessions)))
    bstack1llll11ll1_opy_ = bstack1llll11ll1_opy_.replace(bstack11l1l11_opy_ (u"ࠧࡼࠧࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠪࢃࠧဍ"), bstack1lll1111l_opy_)
    bstack1llll11ll1_opy_ = bstack1llll11ll1_opy_.replace(bstack11l1l11_opy_ (u"ࠨࡽࠨࡆ࡚ࡏࡌࡅࡡࡑࡅࡒࡋࠥࡾࠩဎ"),
                                              sessions[0].get(bstack11l1l11_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡰࡤࡱࡪ࠭ဏ")) if sessions[0] else bstack11l1l11_opy_ (u"ࠪࠫတ"))
    with open(os.path.join(bstack11l1ll1l11_opy_, bstack11l1l11_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡶࡪࡶ࡯ࡳࡶ࠱࡬ࡹࡳ࡬ࠨထ")), bstack11l1l11_opy_ (u"ࠬࡽࠧဒ")) as stream:
      stream.write(bstack1llll11ll1_opy_.split(bstack11l1l11_opy_ (u"࠭ࡻࠦࡕࡈࡗࡘࡏࡏࡏࡕࡢࡈࡆ࡚ࡁࠦࡿࠪဓ"))[0])
      for session in sessions:
        stream.write(bstack11l1111l1_opy_(session))
      stream.write(bstack1llll11ll1_opy_.split(bstack11l1l11_opy_ (u"ࠧࡼࠧࡖࡉࡘ࡙ࡉࡐࡐࡖࡣࡉࡇࡔࡂࠧࢀࠫန"))[1])
    logger.info(bstack11l1l11_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵࡧࡧࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡦࡺ࡯࡬ࡥࠢࡤࡶࡹ࡯ࡦࡢࡥࡷࡷࠥࡧࡴࠡࡽࢀࠫပ").format(bstack11l1ll1l11_opy_));
  except Exception as e:
    logger.debug(bstack11111ll11l_opy_.format(str(e)))
def bstack1l1111l111_opy_(hashed_id):
  global CONFIG
  try:
    bstack1l11lll1l_opy_ = datetime.datetime.now()
    host = bstack11l1l11_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠭ࡤ࡮ࡲࡹࡩ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩဖ") if bstack11l1l11_opy_ (u"ࠪࡥࡵࡶࠧဗ") in CONFIG else bstack11l1l11_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬဘ")
    user = CONFIG[bstack11l1l11_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧမ")]
    key = CONFIG[bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩယ")]
    bstack1l1ll11111_opy_ = bstack11l1l11_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ရ") if bstack11l1l11_opy_ (u"ࠨࡣࡳࡴࠬလ") in CONFIG else (bstack11l1l11_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ဝ") if CONFIG.get(bstack11l1l11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧသ")) else bstack11l1l11_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ဟ"))
    host = bstack111ll1l1ll_opy_(cli.config, [bstack11l1l11_opy_ (u"ࠧࡧࡰࡪࡵࠥဠ"), bstack11l1l11_opy_ (u"ࠨࡡࡱࡲࡄࡹࡹࡵ࡭ࡢࡶࡨࠦအ"), bstack11l1l11_opy_ (u"ࠢࡢࡲ࡬ࠦဢ")], host) if bstack11l1l11_opy_ (u"ࠨࡣࡳࡴࠬဣ") in CONFIG else bstack111ll1l1ll_opy_(cli.config, [bstack11l1l11_opy_ (u"ࠤࡤࡴ࡮ࡹࠢဤ"), bstack11l1l11_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࠧဥ"), bstack11l1l11_opy_ (u"ࠦࡦࡶࡩࠣဦ")], host)
    url = bstack11l1l11_opy_ (u"ࠬࢁࡽ࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃ࠯ࡴࡧࡶࡷ࡮ࡵ࡮ࡴ࠰࡭ࡷࡴࡴࠧဧ").format(host, bstack1l1ll11111_opy_, hashed_id)
    headers = {
      bstack11l1l11_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬဨ"): bstack11l1l11_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪဩ"),
    }
    proxies = bstack1l1l1l1111_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠣࡪࡷࡸࡵࡀࡧࡦࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࡤࡲࡩࡴࡶࠥဪ"), datetime.datetime.now() - bstack1l11lll1l_opy_)
      return list(map(lambda session: session[bstack11l1l11_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠧါ")], response.json()))
  except Exception as e:
    logger.debug(bstack1111llll1_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack11ll1l111l_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def get_build_link():
  global CONFIG
  global bstack1l111l111_opy_
  try:
    if bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ာ") in CONFIG:
      bstack1l11lll1l_opy_ = datetime.datetime.now()
      host = bstack11l1l11_opy_ (u"ࠫࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪࠧိ") if bstack11l1l11_opy_ (u"ࠬࡧࡰࡱࠩီ") in CONFIG else bstack11l1l11_opy_ (u"࠭ࡡࡱ࡫ࠪု")
      user = CONFIG[bstack11l1l11_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩူ")]
      key = CONFIG[bstack11l1l11_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫေ")]
      bstack1l1ll11111_opy_ = bstack11l1l11_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨဲ") if bstack11l1l11_opy_ (u"ࠪࡥࡵࡶࠧဳ") in CONFIG else bstack11l1l11_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ဴ")
      url = bstack11l1l11_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡻࡾ࠼ࡾࢁࡅࢁࡽ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠮࡫ࡵࡲࡲࠬဵ").format(user, key, host, bstack1l1ll11111_opy_)
      if cli.is_enabled(CONFIG):
        bstack1lll1111l_opy_, hashed_id = cli.bstack1llll1l11l_opy_()
        logger.info(bstack111l1ll1ll_opy_.format(bstack1lll1111l_opy_))
        return [hashed_id, bstack1lll1111l_opy_]
      else:
        headers = {
          bstack11l1l11_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬံ"): bstack11l1l11_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰ့ࠪ"),
        }
        if bstack11l1l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪး") in CONFIG:
          params = {bstack11l1l11_opy_ (u"ࠩࡱࡥࡲ࡫္ࠧ"): CONFIG[bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ်࠭")], bstack11l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧျ"): CONFIG[bstack11l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧြ")]}
        else:
          params = {bstack11l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫွ"): CONFIG[bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪှ")]}
        proxies = bstack1l1l1l1111_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack11lll11111_opy_ = response.json()[0][bstack11l1l11_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡨࡵࡪ࡮ࡧࠫဿ")]
          if bstack11lll11111_opy_:
            bstack1lll1111l_opy_ = bstack11lll11111_opy_[bstack11l1l11_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭၀")].split(bstack11l1l11_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥ࠰ࡦࡺ࡯࡬ࡥࠩ၁"))[0] + bstack11l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡶ࠳ࠬ၂") + bstack11lll11111_opy_[
              bstack11l1l11_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ၃")]
            logger.info(bstack111l1ll1ll_opy_.format(bstack1lll1111l_opy_))
            bstack1l111l111_opy_ = bstack11lll11111_opy_[bstack11l1l11_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ၄")]
            bstack1l1111111l_opy_ = CONFIG[bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ၅")]
            if bstack11l1l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ၆") in CONFIG:
              bstack1l1111111l_opy_ += bstack11l1l11_opy_ (u"ࠩࠣࠫ၇") + CONFIG[bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ၈")]
            if bstack1l1111111l_opy_ != bstack11lll11111_opy_[bstack11l1l11_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ၉")]:
              logger.debug(bstack11l111l11_opy_.format(bstack11lll11111_opy_[bstack11l1l11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ၊")], bstack1l1111111l_opy_))
            cli.bstack1l111llll_opy_(bstack11l1l11_opy_ (u"ࠨࡨࡵࡶࡳ࠾࡬࡫ࡴࡠࡤࡸ࡭ࡱࡪ࡟࡭࡫ࡱ࡯ࠧ။"), datetime.datetime.now() - bstack1l11lll1l_opy_)
            return [bstack11lll11111_opy_[bstack11l1l11_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ၌")], bstack1lll1111l_opy_]
    else:
      logger.warn(bstack1l1lllllll_opy_)
  except Exception as e:
    logger.debug(bstack11l11ll1l1_opy_.format(str(e)))
  return [None, None]
def bstack11llll1ll1_opy_(url, bstack11lll1lll_opy_=False):
  global CONFIG
  global bstack11llllll1l_opy_
  if not bstack11llllll1l_opy_:
    hostname = bstack1ll1l111l_opy_(url)
    is_private = bstack1l1ll11ll1_opy_(hostname)
    if (bstack11l1l11_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ၍") in CONFIG and not bstack1lll1ll1l1_opy_(CONFIG[bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭၎")])) and (is_private or bstack11lll1lll_opy_):
      bstack11llllll1l_opy_ = hostname
def bstack1ll1l111l_opy_(url):
  return urlparse(url).hostname
def bstack1l1ll11ll1_opy_(hostname):
  for bstack1l1l11111_opy_ in bstack1l111l1l1l_opy_:
    regex = re.compile(bstack1l1l11111_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack11ll1lll11_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1l1l111ll_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1l1111lll1_opy_
  bstack11ll11l11l_opy_ = not (bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ၏"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack11l1l11_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၐ"), None))
  bstack1ll11ll1ll_opy_ = getattr(driver, bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬၑ"), None) != True
  bstack11l1111lll_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ၒ"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack11l1l11_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩၓ"), None)
  if bstack11l1111lll_opy_:
    if not bstack11l11ll111_opy_():
      logger.warning(bstack11l1l11_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶ࠲ࠧၔ"))
      return {}
    logger.debug(bstack11l1l11_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ၕ"))
    logger.debug(perform_scan(driver, driver_command=bstack11l1l11_opy_ (u"ࠪࡩࡽ࡫ࡣࡶࡶࡨࡗࡨࡸࡩࡱࡶࠪၖ")))
    results = bstack1l1l11111l_opy_(bstack11l1l11_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷࡷࠧၗ"))
    if results is not None and results.get(bstack11l1l11_opy_ (u"ࠧ࡯ࡳࡴࡷࡨࡷࠧၘ")) is not None:
        return results[bstack11l1l11_opy_ (u"ࠨࡩࡴࡵࡸࡩࡸࠨၙ")]
    logger.error(bstack11l1l11_opy_ (u"ࠢࡏࡱࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡖࡪࡹࡵ࡭ࡶࡶࠤࡼ࡫ࡲࡦࠢࡩࡳࡺࡴࡤ࠯ࠤၚ"))
    return []
  if not bstack111l1lll_opy_.bstack11l11ll1l_opy_(CONFIG, bstack1l1111lll1_opy_) or (bstack1ll11ll1ll_opy_ and bstack11ll11l11l_opy_):
    logger.warning(bstack11l1l11_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵ࠱ࠦၛ"))
    return {}
  try:
    logger.debug(bstack11l1l11_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ၜ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack11l1ll11ll_opy_.bstack1ll1l1ll11_opy_)
    return results
  except Exception:
    logger.error(bstack11l1l11_opy_ (u"ࠥࡒࡴࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡸࡧࡵࡩࠥ࡬࡯ࡶࡰࡧ࠲ࠧၝ"))
    return {}
@measure(event_name=EVENTS.bstack111l1ll11l_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1l1111lll1_opy_
  bstack11ll11l11l_opy_ = not (bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၞ"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack11l1l11_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၟ"), None))
  bstack1ll11ll1ll_opy_ = getattr(driver, bstack11l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ၠ"), None) != True
  bstack11l1111lll_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၡ"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack11l1l11_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၢ"), None)
  if bstack11l1111lll_opy_:
    if not bstack11l11ll111_opy_():
      logger.warning(bstack11l1l11_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠴ࠢၣ"))
      return {}
    logger.debug(bstack11l1l11_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹࠨၤ"))
    logger.debug(perform_scan(driver, driver_command=bstack11l1l11_opy_ (u"ࠫࡪࡾࡥࡤࡷࡷࡩࡘࡩࡲࡪࡲࡷࠫၥ")))
    results = bstack1l1l11111l_opy_(bstack11l1l11_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸࡘࡻ࡭࡮ࡣࡵࡽࠧၦ"))
    if results is not None and results.get(bstack11l1l11_opy_ (u"ࠨࡳࡶ࡯ࡰࡥࡷࡿࠢၧ")) is not None:
        return results[bstack11l1l11_opy_ (u"ࠢࡴࡷࡰࡱࡦࡸࡹࠣၨ")]
    logger.error(bstack11l1l11_opy_ (u"ࠣࡐࡲࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡗ࡫ࡳࡶ࡮ࡷࡷ࡙ࠥࡵ࡮࡯ࡤࡶࡾࠦࡷࡢࡵࠣࡪࡴࡻ࡮ࡥ࠰ࠥၩ"))
    return {}
  if not bstack111l1lll_opy_.bstack11l11ll1l_opy_(CONFIG, bstack1l1111lll1_opy_) or (bstack1ll11ll1ll_opy_ and bstack11ll11l11l_opy_):
    logger.warning(bstack11l1l11_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡸࡻ࡭࡮ࡣࡵࡽ࠳ࠨၪ"))
    return {}
  try:
    logger.debug(bstack11l1l11_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹࠨၫ"))
    logger.debug(perform_scan(driver))
    bstack1lll11l11l_opy_ = driver.execute_async_script(bstack11l1ll11ll_opy_.bstack1llllll111_opy_)
    return bstack1lll11l11l_opy_
  except Exception:
    logger.error(bstack11l1l11_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡷࡰࡱࡦࡸࡹࠡࡹࡤࡷࠥ࡬࡯ࡶࡰࡧ࠲ࠧၬ"))
    return {}
def bstack11l11ll111_opy_():
  global CONFIG
  global bstack1l1111lll1_opy_
  bstack1l11111ll1_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬၭ"), None) and bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨၮ"), None)
  if not bstack111l1lll_opy_.bstack11l11ll1l_opy_(CONFIG, bstack1l1111lll1_opy_) or not bstack1l11111ll1_opy_:
        logger.warning(bstack11l1l11_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡸࡥࡴࡷ࡯ࡸࡸ࠴ࠢၯ"))
        return False
  return True
def bstack1l1l11111l_opy_(bstack1lll11l11_opy_):
    bstack1111l1lll1_opy_ = bstack1l1lll1l_opy_.current_test_uuid() if bstack1l1lll1l_opy_.current_test_uuid() else bstack1ll1l1ll_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack1lll1l11l1_opy_(bstack1111l1lll1_opy_, bstack1lll11l11_opy_))
        try:
            return future.result(timeout=bstack1ll111111_opy_)
        except TimeoutError:
            logger.error(bstack11l1l11_opy_ (u"ࠣࡖ࡬ࡱࡪࡵࡵࡵࠢࡤࡪࡹ࡫ࡲࠡࡽࢀࡷࠥࡽࡨࡪ࡮ࡨࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡒࡦࡵࡸࡰࡹࡹࠢၰ").format(bstack1ll111111_opy_))
        except Exception as ex:
            logger.debug(bstack11l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡴࡨࡸࡷ࡯ࡥࡷ࡫ࡱ࡫ࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡻࡾ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠰ࠤࢀࢃࠢၱ").format(bstack1lll11l11_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack11ll11ll11_opy_, stage=STAGE.bstack11l1lllll_opy_, bstack111111ll1_opy_=bstack1111ll11l_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1l1111lll1_opy_
  bstack11ll11l11l_opy_ = not (bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၲ"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack11l1l11_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၳ"), None))
  bstack1lllll1l1l_opy_ = not (bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬၴ"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack11l1l11_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨၵ"), None))
  bstack1ll11ll1ll_opy_ = getattr(driver, bstack11l1l11_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧၶ"), None) != True
  if not bstack111l1lll_opy_.bstack11l11ll1l_opy_(CONFIG, bstack1l1111lll1_opy_) or (bstack1ll11ll1ll_opy_ and bstack11ll11l11l_opy_ and bstack1lllll1l1l_opy_):
    logger.warning(bstack11l1l11_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡷࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡩࡡ࡯࠰ࠥၷ"))
    return {}
  try:
    bstack1111ll1ll_opy_ = bstack11l1l11_opy_ (u"ࠩࡤࡴࡵ࠭ၸ") in CONFIG and CONFIG.get(bstack11l1l11_opy_ (u"ࠪࡥࡵࡶࠧၹ"), bstack11l1l11_opy_ (u"ࠫࠬၺ"))
    session_id = getattr(driver, bstack11l1l11_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩၻ"), None)
    if not session_id:
      logger.warning(bstack11l1l11_opy_ (u"ࠨࡎࡰࠢࡶࡩࡸࡹࡩࡰࡰࠣࡍࡉࠦࡦࡰࡷࡱࡨࠥ࡬࡯ࡳࠢࡧࡶ࡮ࡼࡥࡳࠤၼ"))
      return {bstack11l1l11_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨၽ"): bstack11l1l11_opy_ (u"ࠣࡐࡲࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡏࡄࠡࡨࡲࡹࡳࡪࠢၾ")}
    if bstack1111ll1ll_opy_:
      try:
        bstack11111l1l1l_opy_ = {
              bstack11l1l11_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ࠭ၿ"): os.environ.get(bstack11l1l11_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨႀ"), os.environ.get(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨႁ"), bstack11l1l11_opy_ (u"ࠬ࠭ႂ"))),
              bstack11l1l11_opy_ (u"࠭ࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩ࠭ႃ"): bstack1l1lll1l_opy_.current_test_uuid() if bstack1l1lll1l_opy_.current_test_uuid() else bstack1ll1l1ll_opy_.current_hook_uuid(),
              bstack11l1l11_opy_ (u"ࠧࡢࡷࡷ࡬ࡍ࡫ࡡࡥࡧࡵࠫႄ"): os.environ.get(bstack11l1l11_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ႅ")),
              bstack11l1l11_opy_ (u"ࠩࡶࡧࡦࡴࡔࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩႆ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack11l1l11_opy_ (u"ࠪࡸ࡭ࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨႇ"): os.environ.get(bstack11l1l11_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩႈ"), bstack11l1l11_opy_ (u"ࠬ࠭ႉ")),
              bstack11l1l11_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭ႊ"): kwargs.get(bstack11l1l11_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸ࡟ࡤࡱࡰࡱࡦࡴࡤࠨႋ"), None) or bstack11l1l11_opy_ (u"ࠨࠩႌ")
          }
        if not hasattr(thread_local, bstack11l1l11_opy_ (u"ࠩࡥࡥࡸ࡫࡟ࡢࡲࡳࡣࡦ࠷࠱ࡺࡡࡶࡧࡷ࡯ࡰࡵႍࠩ")):
            scripts = {bstack11l1l11_opy_ (u"ࠪࡷࡨࡧ࡮ࠨႎ"): bstack11l1ll11ll_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack1lll1l1ll1_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack1lll1l1ll1_opy_[bstack11l1l11_opy_ (u"ࠫࡸࡩࡡ࡯ࠩႏ")] = bstack1lll1l1ll1_opy_[bstack11l1l11_opy_ (u"ࠬࡹࡣࡢࡰࠪ႐")] % json.dumps(bstack11111l1l1l_opy_)
        bstack11l1ll11ll_opy_.bstack1ll11ll11l_opy_(bstack1lll1l1ll1_opy_)
        bstack11l1ll11ll_opy_.store()
        bstack1ll11l11ll_opy_ = driver.execute_script(bstack11l1ll11ll_opy_.perform_scan)
      except Exception as bstack11l1l111l_opy_:
        logger.info(bstack11l1l11_opy_ (u"ࠨࡁࡱࡲ࡬ࡹࡲࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡤࡣࡱࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࠨ႑") + str(bstack11l1l111l_opy_))
        bstack1ll11l11ll_opy_ = {bstack11l1l11_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨ႒"): str(bstack11l1l111l_opy_)}
    else:
      bstack1ll11l11ll_opy_ = driver.execute_async_script(bstack11l1ll11ll_opy_.perform_scan, {bstack11l1l11_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨ႓"): kwargs.get(bstack11l1l11_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࡡࡦࡳࡲࡳࡡ࡯ࡦࠪ႔"), None) or bstack11l1l11_opy_ (u"ࠪࠫ႕")})
    return bstack1ll11l11ll_opy_
  except Exception as err:
    logger.error(bstack11l1l11_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡳࡷࡱࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡩࡡ࡯࠰ࠣࡿࢂࠨ႖").format(str(err)))
    return {}