# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
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
from browserstack_sdk.bstack1111ll1ll_opy_ import bstack11l1111ll_opy_
from browserstack_sdk.bstack1lll1l11l_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack11l1l111l1_opy_():
  global CONFIG
  headers = {
        bstack111111l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫ৹"): bstack111111l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ৺"),
      }
  proxies = bstack1l111111ll_opy_(CONFIG, bstack11111l11l_opy_)
  try:
    response = requests.get(bstack11111l11l_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l1l11111_opy_ = response.json()[bstack111111l_opy_ (u"ࠧࡩࡷࡥࡷࠬ৻")]
      logger.debug(bstack11l11l1l1_opy_.format(response.json()))
      return bstack1l1l11111_opy_
    else:
      logger.debug(bstack1ll11lll1_opy_.format(bstack111111l_opy_ (u"ࠣࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡎࡘࡕࡎࠡࡲࡤࡶࡸ࡫ࠠࡦࡴࡵࡳࡷࠦࠢৼ")))
  except Exception as e:
    logger.debug(bstack1ll11lll1_opy_.format(e))
def bstack11l1l111l_opy_(hub_url):
  global CONFIG
  url = bstack111111l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦ৽")+  hub_url + bstack111111l_opy_ (u"ࠥ࠳ࡨ࡮ࡥࡤ࡭ࠥ৾")
  headers = {
        bstack111111l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪ৿"): bstack111111l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ਀"),
      }
  proxies = bstack1l111111ll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1l1l111ll1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1ll11ll1l_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack1l1l11l1l1_opy_, stage=STAGE.bstack11l11ll11_opy_)
def bstack1ll1ll1l11_opy_():
  try:
    global bstack1lll1ll1ll_opy_
    bstack1l1l11111_opy_ = bstack11l1l111l1_opy_()
    bstack1111ll1l11_opy_ = []
    results = []
    for bstack1l11l11ll_opy_ in bstack1l1l11111_opy_:
      bstack1111ll1l11_opy_.append(bstack11llll111_opy_(target=bstack11l1l111l_opy_,args=(bstack1l11l11ll_opy_,)))
    for t in bstack1111ll1l11_opy_:
      t.start()
    for t in bstack1111ll1l11_opy_:
      results.append(t.join())
    bstack11l11llll1_opy_ = {}
    for item in results:
      hub_url = item[bstack111111l_opy_ (u"࠭ࡨࡶࡤࡢࡹࡷࡲࠧਁ")]
      latency = item[bstack111111l_opy_ (u"ࠧ࡭ࡣࡷࡩࡳࡩࡹࠨਂ")]
      bstack11l11llll1_opy_[hub_url] = latency
    bstack11111l1l1l_opy_ = min(bstack11l11llll1_opy_, key= lambda x: bstack11l11llll1_opy_[x])
    bstack1lll1ll1ll_opy_ = bstack11111l1l1l_opy_
    logger.debug(bstack1lll1l1111_opy_.format(bstack11111l1l1l_opy_))
  except Exception as e:
    logger.debug(bstack11l11l1111_opy_.format(e))
from browserstack_sdk.bstack11111l11_opy_ import *
from browserstack_sdk.bstack1111l1ll_opy_ import *
from browserstack_sdk.bstack11ll11l1_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack11111ll111_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack11llllllll_opy_, stage=STAGE.bstack11l11ll11_opy_)
def bstack1111lll1l1_opy_():
    global bstack1lll1ll1ll_opy_
    try:
        bstack11l1l1111l_opy_ = bstack11ll1ll11_opy_()
        bstack11ll11l1l1_opy_(bstack11l1l1111l_opy_)
        hub_url = bstack11l1l1111l_opy_.get(bstack111111l_opy_ (u"ࠣࡷࡵࡰࠧਃ"), bstack111111l_opy_ (u"ࠤࠥ਄"))
        if hub_url.endswith(bstack111111l_opy_ (u"ࠪ࠳ࡼࡪ࠯ࡩࡷࡥࠫਅ")):
            hub_url = hub_url.rsplit(bstack111111l_opy_ (u"ࠫ࠴ࡽࡤ࠰ࡪࡸࡦࠬਆ"), 1)[0]
        if hub_url.startswith(bstack111111l_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴࠭ਇ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack111111l_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࠨਈ")):
            hub_url = hub_url[8:]
        bstack1lll1ll1ll_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack11ll1ll11_opy_():
    global CONFIG
    bstack11l11111l_opy_ = CONFIG.get(bstack111111l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫਉ"), {}).get(bstack111111l_opy_ (u"ࠨࡩࡵ࡭ࡩࡔࡡ࡮ࡧࠪਊ"), bstack111111l_opy_ (u"ࠩࡑࡓࡤࡍࡒࡊࡆࡢࡒࡆࡓࡅࡠࡒࡄࡗࡘࡋࡄࠨ਋"))
    if not isinstance(bstack11l11111l_opy_, str):
        raise ValueError(bstack111111l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡊࡶ࡮ࡪࠠ࡯ࡣࡰࡩࠥࡳࡵࡴࡶࠣࡦࡪࠦࡡࠡࡸࡤࡰ࡮ࡪࠠࡴࡶࡵ࡭ࡳ࡭ࠢ਌"))
    try:
        bstack11l1l1111l_opy_ = bstack1l111l11ll_opy_(bstack11l11111l_opy_)
        return bstack11l1l1111l_opy_
    except Exception as e:
        logger.error(bstack111111l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡧࡳ࡫ࡧࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡀࠠࡼࡿࠥ਍").format(str(e)))
        return {}
def bstack1l111l11ll_opy_(bstack11l11111l_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack111111l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ਎")] or not CONFIG[bstack111111l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩਏ")]:
            raise ValueError(bstack111111l_opy_ (u"ࠢࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡶࡵࡨࡶࡳࡧ࡭ࡦࠢࡲࡶࠥࡧࡣࡤࡧࡶࡷࠥࡱࡥࡺࠤਐ"))
        url = bstack111ll11ll1_opy_ + bstack11l11111l_opy_
        auth = (CONFIG[bstack111111l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ਑")], CONFIG[bstack111111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ਒")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack11lll11ll_opy_ = json.loads(response.text)
            return bstack11lll11ll_opy_
    except ValueError as ve:
        logger.error(bstack111111l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡧࡳ࡫ࡧࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡀࠠࡼࡿࠥਓ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack111111l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡨࡴ࡬ࡨࠥࡪࡥࡵࡣ࡬ࡰࡸࠦ࠺ࠡࡽࢀࠦਔ").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack11ll11l1l1_opy_(bstack111ll1ll1l_opy_):
    global CONFIG
    if bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩਕ") not in CONFIG or str(CONFIG[bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪਖ")]).lower() == bstack111111l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ਗ"):
        CONFIG[bstack111111l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࠧਘ")] = False
    elif bstack111111l_opy_ (u"ࠩ࡬ࡷ࡙ࡸࡩࡢ࡮ࡊࡶ࡮ࡪࠧਙ") in bstack111ll1ll1l_opy_:
        bstack111ll1l1l1_opy_ = CONFIG.get(bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧਚ"), {})
        logger.debug(bstack111111l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡽ࡯ࡳࡵ࡫ࡱ࡫ࠥࡲ࡯ࡤࡣ࡯ࠤࡴࡶࡴࡪࡱࡱࡷ࠿ࠦࠥࡴࠤਛ"), bstack111ll1l1l1_opy_)
        bstack1l111l111_opy_ = bstack111ll1ll1l_opy_.get(bstack111111l_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱࡗ࡫ࡰࡦࡣࡷࡩࡷࡹࠢਜ"), [])
        bstack1ll111l1l_opy_ = bstack111111l_opy_ (u"ࠨࠬࠣਝ").join(bstack1l111l111_opy_)
        logger.debug(bstack111111l_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡃࡶࡵࡷࡳࡲࠦࡲࡦࡲࡨࡥࡹ࡫ࡲࠡࡵࡷࡶ࡮ࡴࡧ࠻ࠢࠨࡷࠧਞ"), bstack1ll111l1l_opy_)
        bstack1lllll11l1_opy_ = {
            bstack111111l_opy_ (u"ࠣ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥਟ"): bstack111111l_opy_ (u"ࠤࡤࡸࡸ࠳ࡲࡦࡲࡨࡥࡹ࡫ࡲࠣਠ"),
            bstack111111l_opy_ (u"ࠥࡪࡴࡸࡣࡦࡎࡲࡧࡦࡲࠢਡ"): bstack111111l_opy_ (u"ࠦࡹࡸࡵࡦࠤਢ"),
            bstack111111l_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࠲ࡸࡥࡱࡧࡤࡸࡪࡸࠢਣ"): bstack1ll111l1l_opy_
        }
        bstack111ll1l1l1_opy_.update(bstack1lllll11l1_opy_)
        logger.debug(bstack111111l_opy_ (u"ࠨࡁࡕࡕࠣ࠾࡛ࠥࡰࡥࡣࡷࡩࡩࠦ࡬ࡰࡥࡤࡰࠥࡵࡰࡵ࡫ࡲࡲࡸࡀࠠࠦࡵࠥਤ"), bstack111ll1l1l1_opy_)
        CONFIG[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫਥ")] = bstack111ll1l1l1_opy_
        logger.debug(bstack111111l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡇ࡫ࡱࡥࡱࠦࡃࡐࡐࡉࡍࡌࡀࠠࠦࡵࠥਦ"), CONFIG)
def bstack111l11lll_opy_():
    bstack11l1l1111l_opy_ = bstack11ll1ll11_opy_()
    if not bstack11l1l1111l_opy_[bstack111111l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࡛ࡲ࡭ࠩਧ")]:
      raise ValueError(bstack111111l_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࡕࡳ࡮ࠣ࡭ࡸࠦ࡭ࡪࡵࡶ࡭ࡳ࡭ࠠࡧࡴࡲࡱࠥ࡭ࡲࡪࡦࠣࡨࡪࡺࡡࡪ࡮ࡶ࠲ࠧਨ"))
    return bstack11l1l1111l_opy_[bstack111111l_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡖࡴ࡯ࠫ਩")] + bstack111111l_opy_ (u"ࠬࡅࡣࡢࡲࡶࡁࠬਪ")
@measure(event_name=EVENTS.bstack1l1111l1l1_opy_, stage=STAGE.bstack11l11ll11_opy_)
def bstack1111ll1lll_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack111111l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨਫ")], CONFIG[bstack111111l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪਬ")])
        url = bstack1ll1l11lll_opy_
        logger.debug(bstack111111l_opy_ (u"ࠣࡃࡷࡸࡪࡳࡰࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡣࡷ࡬ࡰࡩࡹࠠࡧࡴࡲࡱࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤ࡙ࡻࡲࡣࡱࡖࡧࡦࡲࡥࠡࡃࡓࡍࠧਭ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack111111l_opy_ (u"ࠤࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠣਮ"): bstack111111l_opy_ (u"ࠥࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳࠨਯ")})
            if response.status_code == 200:
                bstack1ll11llll1_opy_ = json.loads(response.text)
                bstack1l1111llll_opy_ = bstack1ll11llll1_opy_.get(bstack111111l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡶࠫਰ"), [])
                if bstack1l1111llll_opy_:
                    bstack111lllll1_opy_ = bstack1l1111llll_opy_[0]
                    build_hashed_id = bstack111lllll1_opy_.get(bstack111111l_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ਱"))
                    bstack11l11l1l11_opy_ = bstack11l11l111_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack11l11l1l11_opy_])
                    logger.info(bstack1111l1l111_opy_.format(bstack11l11l1l11_opy_))
                    bstack11111ll1l1_opy_ = CONFIG[bstack111111l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩਲ")]
                    if bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩਲ਼") in CONFIG:
                      bstack11111ll1l1_opy_ += bstack111111l_opy_ (u"ࠨࠢࠪ਴") + CONFIG[bstack111111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫਵ")]
                    if bstack11111ll1l1_opy_ != bstack111lllll1_opy_.get(bstack111111l_opy_ (u"ࠪࡲࡦࡳࡥࠨਸ਼")):
                      logger.debug(bstack11ll11111l_opy_.format(bstack111lllll1_opy_.get(bstack111111l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ਷")), bstack11111ll1l1_opy_))
                    return result
                else:
                    logger.debug(bstack111111l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡓࡵࠠࡣࡷ࡬ࡰࡩࡹࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡷ࡬ࡪࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠯ࠤਸ"))
            else:
                logger.debug(bstack111111l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡣࡷ࡬ࡰࡩࡹ࠮ࠣਹ"))
        except Exception as e:
            logger.error(bstack111111l_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࡴࠢ࠽ࠤࢀࢃࠢ਺").format(str(e)))
    else:
        logger.debug(bstack111111l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡄࡑࡑࡊࡎࡍࠠࡪࡵࠣࡲࡴࡺࠠࡴࡧࡷ࠲࡛ࠥ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡣࡷ࡬ࡰࡩࡹ࠮ࠣ਻"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack111ll111l1_opy_ import bstack111ll111l1_opy_, Events, bstack1lll1l11ll_opy_, bstack1l111l11l_opy_
from bstack_utils.measure import bstack1l11ll11l1_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack11ll11l111_opy_ import bstack11l1l1111_opy_
from bstack_utils.messages import *
from bstack_utils import bstack11111ll111_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l1lll1l11_opy_, bstack1l11l1ll1l_opy_, bstack1lll1111l_opy_, bstack1lll111l_opy_, \
  bstack11l1l1l1ll_opy_, \
  Notset, bstack111ll11lll_opy_, \
  bstack1ll1l1ll1_opy_, bstack11l1lll11l_opy_, bstack1l1lll1111_opy_, bstack111l11lll1_opy_, bstack1ll11111l1_opy_, bstack11ll1l1lll_opy_, \
  bstack11lll111l1_opy_, \
  bstack1ll1ll1ll1_opy_, bstack11l1ll11ll_opy_, bstack111ll11l1_opy_, bstack1ll1l1ll1l_opy_, \
  bstack1l111ll1l_opy_, bstack1l11ll1ll_opy_, bstack1llll11lll_opy_, bstack1l11111lll_opy_
from bstack_utils.bstack1l1l11llll_opy_ import bstack11ll11l11_opy_
from bstack_utils.bstack11l11lll11_opy_ import bstack1l1ll1l11l_opy_, bstack1l1111l1ll_opy_
from bstack_utils.bstack11l1l1lll1_opy_ import bstack1l11ll1l1_opy_
from bstack_utils.bstack1l11111ll1_opy_ import bstack1ll111l1ll_opy_, bstack111ll1lll_opy_
from bstack_utils.bstack11l1llll11_opy_ import bstack11l1llll11_opy_
from bstack_utils.bstack1ll1ll1l1l_opy_ import bstack1l11111ll_opy_
from bstack_utils.proxy import bstack1111llll11_opy_, bstack1l111111ll_opy_, bstack1l1l1lllll_opy_, bstack1l1111ll1l_opy_
from bstack_utils.bstack11l1ll1l11_opy_ import bstack111l1111l1_opy_
import bstack_utils.bstack11ll111l1l_opy_ as bstack1l1l1l1l1_opy_
import bstack_utils.bstack11111l11ll_opy_ as bstack1l1111l1l_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack1ll1lll1ll_opy_ import bstack11ll1llll1_opy_
from bstack_utils.bstack1111l1l1_opy_ import bstack1lll1ll11_opy_
from bstack_utils.bstack1ll11l111_opy_ import bstack11l11ll1ll_opy_
if os.getenv(bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡏࡍࡤࡎࡏࡐࡍࡖ਼ࠫ")):
  cli.bstack11111llll_opy_()
else:
  os.environ[bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡈࡐࡑࡎࡗࠬ਽")] = bstack111111l_opy_ (u"ࠫࡹࡸࡵࡦࠩਾ")
bstack111l1ll1l1_opy_ = bstack111111l_opy_ (u"ࠬࠦࠠ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠥࠦࡩࡧࠪࡳࡥ࡬࡫ࠠ࠾࠿ࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠥࢁ࡜࡯ࠢࠣࠤࡹࡸࡹࡼ࡞ࡱࠤࡨࡵ࡮ࡴࡶࠣࡪࡸࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪ࡟ࠫ࡫ࡹ࡜ࠨࠫ࠾ࡠࡳࠦࠠࠡࠢࠣࡪࡸ࠴ࡡࡱࡲࡨࡲࡩࡌࡩ࡭ࡧࡖࡽࡳࡩࠨࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬࠱ࠦࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡱࡡ࡬ࡲࡩ࡫ࡸࠪࠢ࠮ࠤࠧࡀࠢࠡ࠭ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࠪࡤࡻࡦ࡯ࡴࠡࡰࡨࡻࡕࡧࡧࡦ࠴࠱ࡩࡻࡧ࡬ࡶࡣࡷࡩ࠭ࠨࠨࠪࠢࡀࡂࠥࢁࡽࠣ࠮ࠣࡠࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧ࡭ࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡆࡨࡸࡦ࡯࡬ࡴࠤࢀࡠࠬ࠯ࠩࠪ࡝ࠥ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩࠨ࡝ࠪࠢ࠮ࠤࠧ࠲࡜࡝ࡰࠥ࠭ࡡࡴࠠࠡࠢࠣࢁࡨࡧࡴࡤࡪࠫࡩࡽ࠯ࡻ࡝ࡰࠣࠤࠥࠦࡽ࡝ࡰࠣࠤࢂࡢ࡮ࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠬਿ")
bstack11111l1l11_opy_ = bstack111111l_opy_ (u"࠭࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࡟ࡲࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࡞ࡱࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࡞ࡱࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࡠࡳ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡲࡡࡶࡰࡦ࡬ࠥࡃࠠࡢࡵࡼࡲࡨࠦࠨ࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠩࠡ࠿ࡁࠤࢀࡢ࡮࡭ࡧࡷࠤࡨࡧࡰࡴ࠽࡟ࡲࡹࡸࡹࠡࡽ࡟ࡲࡨࡧࡰࡴࠢࡀࠤࡏ࡙ࡏࡏ࠰ࡳࡥࡷࡹࡥࠩࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸ࠯࡜࡯ࠢࠣࢁࠥࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࠡࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡲࡦࡶࡸࡶࡳࠦࡡࡸࡣ࡬ࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭࠱ࡧ࡭ࡸ࡯࡮࡫ࡸࡱ࠳ࡩ࡯࡯ࡰࡨࡧࡹ࠮ࡻ࡝ࡰࠣࠤࠥࠦࡷࡴࡇࡱࡨࡵࡵࡩ࡯ࡶ࠽ࠤࡥࡽࡳࡴ࠼࠲࠳ࡨࡪࡰ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡀࡥࡤࡴࡸࡃࠤࡼࡧࡱࡧࡴࡪࡥࡖࡔࡌࡇࡴࡳࡰࡰࡰࡨࡲࡹ࠮ࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡤࡣࡳࡷ࠮࠯ࡽࡡ࠮࡟ࡲࠥࠦࠠࠡ࠰࠱࠲ࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶࡠࡳࠦࠠࡾࠫ࡟ࡲࢂࡢ࡮࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱࡟ࡲࠬੀ")
from ._version import __version__
bstack1l11l1111l_opy_ = None
CONFIG = {}
bstack1l1111111_opy_ = {}
bstack1l11l1ll1_opy_ = {}
bstack1l1ll11lll_opy_ = None
bstack1ll1llll1l_opy_ = None
bstack1l11llll1_opy_ = None
bstack111lll111_opy_ = -1
bstack11l1l1l111_opy_ = 0
bstack1l11l11ll1_opy_ = bstack11111ll1l_opy_
bstack1l1llll1ll_opy_ = 1
bstack11111llll1_opy_ = False
bstack1ll11ll1ll_opy_ = False
bstack1l111111l_opy_ = bstack111111l_opy_ (u"ࠧࠨੁ")
bstack1ll1l1l111_opy_ = bstack111111l_opy_ (u"ࠨࠩੂ")
bstack1ll11lll11_opy_ = False
bstack1l11l11lll_opy_ = True
bstack1l1ll11ll_opy_ = bstack111111l_opy_ (u"ࠩࠪ੃")
bstack1111l11l1l_opy_ = []
bstack11l111l111_opy_ = threading.Lock()
bstack1l1ll1llll_opy_ = threading.Lock()
bstack1lll1ll1ll_opy_ = bstack111111l_opy_ (u"ࠪࠫ੄")
bstack111l111lll_opy_ = False
bstack11ll111ll_opy_ = None
bstack1l1ll11111_opy_ = None
bstack111l1llll1_opy_ = None
bstack1l1l11lll_opy_ = -1
bstack1ll111l111_opy_ = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠫࢃ࠭੅")), bstack111111l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬ੆"), bstack111111l_opy_ (u"࠭࠮ࡳࡱࡥࡳࡹ࠳ࡲࡦࡲࡲࡶࡹ࠳ࡨࡦ࡮ࡳࡩࡷ࠴ࡪࡴࡱࡱࠫੇ"))
bstack1lll11ll11_opy_ = 0
bstack1l111ll11l_opy_ = 0
bstack1ll1111l1l_opy_ = []
bstack111lll11l_opy_ = []
bstack11l1111lll_opy_ = []
bstack1ll111llll_opy_ = []
bstack1111l1lll_opy_ = bstack111111l_opy_ (u"ࠧࠨੈ")
bstack111l1ll1l_opy_ = bstack111111l_opy_ (u"ࠨࠩ੉")
bstack111llll11l_opy_ = False
bstack1lll1ll111_opy_ = False
bstack1l1l1l11l_opy_ = {}
bstack1ll1111lll_opy_ = None
bstack1lll1111ll_opy_ = None
bstack1l11ll11ll_opy_ = None
bstack11ll1l11l1_opy_ = None
bstack1ll1l1l1l1_opy_ = None
bstack1l1lll11l_opy_ = None
bstack1llllll11l_opy_ = None
bstack111ll111ll_opy_ = None
bstack1l111lllll_opy_ = None
bstack1lll1111l1_opy_ = None
bstack1l11ll1l11_opy_ = None
bstack1lll11l11_opy_ = None
bstack11l1l111ll_opy_ = None
bstack11l111111l_opy_ = None
bstack1l11l1l1l_opy_ = None
bstack1ll1lll1l1_opy_ = None
bstack1l11l1l11_opy_ = None
bstack11lll1111_opy_ = None
bstack1llll1llll_opy_ = None
bstack1l1ll1lll_opy_ = None
bstack1ll1ll11l_opy_ = None
bstack1111lllll1_opy_ = None
bstack1l1ll111l1_opy_ = None
thread_local = threading.local()
bstack111l111ll1_opy_ = False
bstack11ll1ll11l_opy_ = bstack111111l_opy_ (u"ࠤࠥ੊")
logger = bstack11111ll111_opy_.get_logger(__name__, bstack1l11l11ll1_opy_)
bstack11111lll_opy_ = Config.bstack111l111l_opy_()
percy = bstack11lll11l1_opy_()
bstack11l11l111l_opy_ = bstack11l1l1111_opy_()
bstack11l1l11lll_opy_ = bstack11ll11l1_opy_()
def bstack11llll1ll1_opy_():
  global CONFIG
  global bstack111llll11l_opy_
  global bstack11111lll_opy_
  testContextOptions = bstack11ll1lll1l_opy_(CONFIG)
  if bstack11l1l1l1ll_opy_(CONFIG):
    if (bstack111111l_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬੋ") in testContextOptions and str(testContextOptions[bstack111111l_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ੌ")]).lower() == bstack111111l_opy_ (u"ࠬࡺࡲࡶࡧ੍ࠪ")):
      bstack111llll11l_opy_ = True
    bstack11111lll_opy_.bstack1lllllll11_opy_(testContextOptions.get(bstack111111l_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪ੎"), False))
  else:
    bstack111llll11l_opy_ = True
    bstack11111lll_opy_.bstack1lllllll11_opy_(True)
def bstack111ll111l_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1ll1llllll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack11111lll1_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack111111l_opy_ (u"ࠢ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡤࡱࡱࡪ࡮࡭ࡦࡪ࡮ࡨࠦ੏") == args[i].lower() or bstack111111l_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡳ࡬ࡩࡨࠤ੐") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1l1ll11ll_opy_
      bstack1l1ll11ll_opy_ += bstack111111l_opy_ (u"ࠩ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡆࡳࡳ࡬ࡩࡨࡈ࡬ࡰࡪࠦࠧੑ") + shlex.quote(path)
      return path
  return None
bstack111l111111_opy_ = re.compile(bstack111111l_opy_ (u"ࡵࠦ࠳࠰࠿࡝ࠦࡾࠬ࠳࠰࠿ࠪࡿ࠱࠮ࡄࠨ੒"))
def bstack1111l1l1l_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack111l111111_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack111111l_opy_ (u"ࠦࠩࢁࠢ੓") + group + bstack111111l_opy_ (u"ࠧࢃࠢ੔"), os.environ.get(group))
  return value
def bstack11ll1l1l1_opy_():
  global bstack1l1ll111l1_opy_
  if bstack1l1ll111l1_opy_ is None:
        bstack1l1ll111l1_opy_ = bstack11111lll1_opy_()
  bstack111l1l1l1l_opy_ = bstack1l1ll111l1_opy_
  if bstack111l1l1l1l_opy_ and os.path.exists(os.path.abspath(bstack111l1l1l1l_opy_)):
    fileName = bstack111l1l1l1l_opy_
  if bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࡤࡌࡉࡍࡇࠪ੕") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ੖")])) and not bstack111111l_opy_ (u"ࠨࡨ࡬ࡰࡪࡔࡡ࡮ࡧࠪ੗") in locals():
    fileName = os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࡠࡈࡌࡐࡊ࠭੘")]
  if bstack111111l_opy_ (u"ࠪࡪ࡮ࡲࡥࡏࡣࡰࡩࠬਖ਼") in locals():
    bstack1111l1l_opy_ = os.path.abspath(fileName)
  else:
    bstack1111l1l_opy_ = bstack111111l_opy_ (u"ࠫࠬਗ਼")
  bstack11lll1l1l1_opy_ = os.getcwd()
  bstack11l111l11_opy_ = bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨਜ਼")
  bstack1111l11lll_opy_ = bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿࡡ࡮࡮ࠪੜ")
  while (not os.path.exists(bstack1111l1l_opy_)) and bstack11lll1l1l1_opy_ != bstack111111l_opy_ (u"ࠢࠣ੝"):
    bstack1111l1l_opy_ = os.path.join(bstack11lll1l1l1_opy_, bstack11l111l11_opy_)
    if not os.path.exists(bstack1111l1l_opy_):
      bstack1111l1l_opy_ = os.path.join(bstack11lll1l1l1_opy_, bstack1111l11lll_opy_)
    if bstack11lll1l1l1_opy_ != os.path.dirname(bstack11lll1l1l1_opy_):
      bstack11lll1l1l1_opy_ = os.path.dirname(bstack11lll1l1l1_opy_)
    else:
      bstack11lll1l1l1_opy_ = bstack111111l_opy_ (u"ࠣࠤਫ਼")
  bstack1l1ll111l1_opy_ = bstack1111l1l_opy_ if os.path.exists(bstack1111l1l_opy_) else None
  return bstack1l1ll111l1_opy_
def bstack1l1l1llll_opy_(config):
    if bstack111111l_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࠩ੟") in config:
      config[bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࠧ੠")] = config[bstack111111l_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࠫ੡")]
    if bstack111111l_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࡔࡶࡴࡪࡱࡱࡷࠬ੢") in config:
      config[bstack111111l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ੣")] = config[bstack111111l_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࡏࡱࡶ࡬ࡳࡳࡹࠧ੤")]
def bstack11111111l_opy_():
  bstack1111l1l_opy_ = bstack11ll1l1l1_opy_()
  if not os.path.exists(bstack1111l1l_opy_):
    bstack1ll111l11_opy_(
      bstack111l1lll1l_opy_.format(os.getcwd()))
  try:
    with open(bstack1111l1l_opy_, bstack111111l_opy_ (u"ࠨࡴࠪ੥")) as stream:
      yaml.add_implicit_resolver(bstack111111l_opy_ (u"ࠤࠤࡴࡦࡺࡨࡦࡺࠥ੦"), bstack111l111111_opy_)
      yaml.add_constructor(bstack111111l_opy_ (u"ࠥࠥࡵࡧࡴࡩࡧࡻࠦ੧"), bstack1111l1l1l_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1l1l1llll_opy_(config)
      return config
  except:
    with open(bstack1111l1l_opy_, bstack111111l_opy_ (u"ࠫࡷ࠭੨")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1l1l1llll_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1ll111l11_opy_(bstack111111l11_opy_.format(str(exc)))
def bstack11lll11ll1_opy_(config):
  bstack1l1l1l111_opy_ = bstack11ll11lll1_opy_(config)
  for option in list(bstack1l1l1l111_opy_):
    if option.lower() in bstack1lll111l11_opy_ and option != bstack1lll111l11_opy_[option.lower()]:
      bstack1l1l1l111_opy_[bstack1lll111l11_opy_[option.lower()]] = bstack1l1l1l111_opy_[option]
      del bstack1l1l1l111_opy_[option]
  return config
def bstack1l1lll11ll_opy_():
  global bstack1l11l1ll1_opy_
  for key, bstack1llllll1ll_opy_ in bstack111l11l111_opy_.items():
    if isinstance(bstack1llllll1ll_opy_, list):
      for var in bstack1llllll1ll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1l11l1ll1_opy_[key] = os.environ[var]
          break
    elif bstack1llllll1ll_opy_ in os.environ and os.environ[bstack1llllll1ll_opy_] and str(os.environ[bstack1llllll1ll_opy_]).strip():
      bstack1l11l1ll1_opy_[key] = os.environ[bstack1llllll1ll_opy_]
  if bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ੩") in os.environ:
    bstack1l11l1ll1_opy_[bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ੪")] = {}
    bstack1l11l1ll1_opy_[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ੫")][bstack111111l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ੬")] = os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫ੭")]
def bstack111l1l11ll_opy_():
  global bstack1l1111111_opy_
  global bstack1l1ll11ll_opy_
  bstack11l11l11l_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack111111l_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੮").lower() == val.lower():
      bstack1l1111111_opy_[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੯")] = {}
      bstack1l1111111_opy_[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩੰ")][bstack111111l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨੱ")] = sys.argv[idx + 1]
      bstack11l11l11l_opy_.extend([idx, idx + 1])
      break
  for key, bstack11111lll1l_opy_ in bstack1l1lll1lll_opy_.items():
    if isinstance(bstack11111lll1l_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack11111lll1l_opy_:
          if bstack111111l_opy_ (u"ࠧ࠮࠯ࠪੲ") + var.lower() == val.lower() and key not in bstack1l1111111_opy_:
            bstack1l1111111_opy_[key] = sys.argv[idx + 1]
            bstack1l1ll11ll_opy_ += bstack111111l_opy_ (u"ࠨࠢ࠰࠱ࠬੳ") + var + bstack111111l_opy_ (u"ࠩࠣࠫੴ") + shlex.quote(sys.argv[idx + 1])
            bstack11l11l11l_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack111111l_opy_ (u"ࠪ࠱࠲࠭ੵ") + bstack11111lll1l_opy_.lower() == val.lower() and key not in bstack1l1111111_opy_:
          bstack1l1111111_opy_[key] = sys.argv[idx + 1]
          bstack1l1ll11ll_opy_ += bstack111111l_opy_ (u"ࠫࠥ࠳࠭ࠨ੶") + bstack11111lll1l_opy_ + bstack111111l_opy_ (u"ࠬࠦࠧ੷") + shlex.quote(sys.argv[idx + 1])
          bstack11l11l11l_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack11l11l11l_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack1ll1l111l_opy_(config):
  bstack1111lll11_opy_ = config.keys()
  for bstack11l111ll11_opy_, bstack1ll111ll1_opy_ in bstack11llllll1_opy_.items():
    if bstack1ll111ll1_opy_ in bstack1111lll11_opy_:
      config[bstack11l111ll11_opy_] = config[bstack1ll111ll1_opy_]
      del config[bstack1ll111ll1_opy_]
  for bstack11l111ll11_opy_, bstack1ll111ll1_opy_ in bstack11ll11ll1_opy_.items():
    if isinstance(bstack1ll111ll1_opy_, list):
      for bstack1ll11ll1l1_opy_ in bstack1ll111ll1_opy_:
        if bstack1ll11ll1l1_opy_ in bstack1111lll11_opy_:
          config[bstack11l111ll11_opy_] = config[bstack1ll11ll1l1_opy_]
          del config[bstack1ll11ll1l1_opy_]
          break
    elif bstack1ll111ll1_opy_ in bstack1111lll11_opy_:
      config[bstack11l111ll11_opy_] = config[bstack1ll111ll1_opy_]
      del config[bstack1ll111ll1_opy_]
  for bstack1ll11ll1l1_opy_ in list(config):
    for bstack11l1ll1l1_opy_ in bstack1l11llllll_opy_:
      if bstack1ll11ll1l1_opy_.lower() == bstack11l1ll1l1_opy_.lower() and bstack1ll11ll1l1_opy_ != bstack11l1ll1l1_opy_:
        config[bstack11l1ll1l1_opy_] = config[bstack1ll11ll1l1_opy_]
        del config[bstack1ll11ll1l1_opy_]
  bstack11ll11l11l_opy_ = [{}]
  if not config.get(bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ੸")):
    config[bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ੹")] = [{}]
  bstack11ll11l11l_opy_ = config[bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ੺")]
  for platform in bstack11ll11l11l_opy_:
    for bstack1ll11ll1l1_opy_ in list(platform):
      for bstack11l1ll1l1_opy_ in bstack1l11llllll_opy_:
        if bstack1ll11ll1l1_opy_.lower() == bstack11l1ll1l1_opy_.lower() and bstack1ll11ll1l1_opy_ != bstack11l1ll1l1_opy_:
          platform[bstack11l1ll1l1_opy_] = platform[bstack1ll11ll1l1_opy_]
          del platform[bstack1ll11ll1l1_opy_]
  for bstack11l111ll11_opy_, bstack1ll111ll1_opy_ in bstack11ll11ll1_opy_.items():
    for platform in bstack11ll11l11l_opy_:
      if isinstance(bstack1ll111ll1_opy_, list):
        for bstack1ll11ll1l1_opy_ in bstack1ll111ll1_opy_:
          if bstack1ll11ll1l1_opy_ in platform:
            platform[bstack11l111ll11_opy_] = platform[bstack1ll11ll1l1_opy_]
            del platform[bstack1ll11ll1l1_opy_]
            break
      elif bstack1ll111ll1_opy_ in platform:
        platform[bstack11l111ll11_opy_] = platform[bstack1ll111ll1_opy_]
        del platform[bstack1ll111ll1_opy_]
  for bstack1l1lll1l1l_opy_ in bstack11ll11llll_opy_:
    if bstack1l1lll1l1l_opy_ in config:
      if not bstack11ll11llll_opy_[bstack1l1lll1l1l_opy_] in config:
        config[bstack11ll11llll_opy_[bstack1l1lll1l1l_opy_]] = {}
      config[bstack11ll11llll_opy_[bstack1l1lll1l1l_opy_]].update(config[bstack1l1lll1l1l_opy_])
      del config[bstack1l1lll1l1l_opy_]
  for platform in bstack11ll11l11l_opy_:
    for bstack1l1lll1l1l_opy_ in bstack11ll11llll_opy_:
      if bstack1l1lll1l1l_opy_ in list(platform):
        if not bstack11ll11llll_opy_[bstack1l1lll1l1l_opy_] in platform:
          platform[bstack11ll11llll_opy_[bstack1l1lll1l1l_opy_]] = {}
        platform[bstack11ll11llll_opy_[bstack1l1lll1l1l_opy_]].update(platform[bstack1l1lll1l1l_opy_])
        del platform[bstack1l1lll1l1l_opy_]
  config = bstack11lll11ll1_opy_(config)
  return config
def bstack1l1111l11l_opy_(config):
  global bstack1ll1l1l111_opy_
  bstack1lll1l1l11_opy_ = False
  if bstack111111l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭੻") in config and str(config[bstack111111l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ੼")]).lower() != bstack111111l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ੽"):
    if bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ੾") not in config or str(config[bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ੿")]).lower() == bstack111111l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭઀"):
      config[bstack111111l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࠧઁ")] = False
    else:
      bstack11l1l1111l_opy_ = bstack11ll1ll11_opy_()
      if bstack111111l_opy_ (u"ࠩ࡬ࡷ࡙ࡸࡩࡢ࡮ࡊࡶ࡮ࡪࠧં") in bstack11l1l1111l_opy_:
        if not bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઃ") in config:
          config[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ઄")] = {}
        config[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩઅ")][bstack111111l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨઆ")] = bstack111111l_opy_ (u"ࠧࡢࡶࡶ࠱ࡷ࡫ࡰࡦࡣࡷࡩࡷ࠭ઇ")
        bstack1lll1l1l11_opy_ = True
        bstack1ll1l1l111_opy_ = config[bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬઈ")].get(bstack111111l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫઉ"))
  if bstack11l1l1l1ll_opy_(config) and bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧઊ") in config and str(config[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨઋ")]).lower() != bstack111111l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫઌ") and not bstack1lll1l1l11_opy_:
    if not bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪઍ") in config:
      config[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ઎")] = {}
    if not config[bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬએ")].get(bstack111111l_opy_ (u"ࠩࡶ࡯࡮ࡶࡂࡪࡰࡤࡶࡾࡏ࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡢࡶ࡬ࡳࡳ࠭ઐ")) and not bstack111111l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬઑ") in config[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ઒")]:
      bstack1llll1ll_opy_ = datetime.datetime.now()
      bstack111l111l1_opy_ = bstack1llll1ll_opy_.strftime(bstack111111l_opy_ (u"ࠬࠫࡤࡠࠧࡥࡣࠪࡎࠥࡎࠩઓ"))
      hostname = socket.gethostname()
      bstack11l111lll_opy_ = bstack111111l_opy_ (u"࠭ࠧઔ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack111111l_opy_ (u"ࠧࡼࡿࡢࡿࢂࡥࡻࡾࠩક").format(bstack111l111l1_opy_, hostname, bstack11l111lll_opy_)
      config[bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬખ")][bstack111111l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫગ")] = identifier
    bstack1ll1l1l111_opy_ = config[bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઘ")].get(bstack111111l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ઙ"))
  return config
def bstack111llll111_opy_():
  bstack11l1111l1_opy_ =  bstack111l11lll1_opy_()[bstack111111l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠫચ")]
  return bstack11l1111l1_opy_ if bstack11l1111l1_opy_ else -1
def bstack1ll1l11l1l_opy_(bstack11l1111l1_opy_):
  global CONFIG
  if not bstack111111l_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨછ") in CONFIG[bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩજ")]:
    return
  CONFIG[bstack111111l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪઝ")] = CONFIG[bstack111111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫઞ")].replace(
    bstack111111l_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬટ"),
    str(bstack11l1111l1_opy_)
  )
def bstack1lll11lll1_opy_():
  global CONFIG
  if not bstack111111l_opy_ (u"ࠫࠩࢁࡄࡂࡖࡈࡣ࡙ࡏࡍࡆࡿࠪઠ") in CONFIG[bstack111111l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧડ")]:
    return
  bstack1llll1ll_opy_ = datetime.datetime.now()
  bstack111l111l1_opy_ = bstack1llll1ll_opy_.strftime(bstack111111l_opy_ (u"࠭ࠥࡥ࠯ࠨࡦ࠲ࠫࡈ࠻ࠧࡐࠫઢ"))
  CONFIG[bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩણ")] = CONFIG[bstack111111l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪત")].replace(
    bstack111111l_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨથ"),
    bstack111l111l1_opy_
  )
def bstack1lll1l1l1l_opy_():
  global CONFIG
  if bstack111111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬદ") in CONFIG and not bool(CONFIG[bstack111111l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ધ")]):
    del CONFIG[bstack111111l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧન")]
    return
  if not bstack111111l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ઩") in CONFIG:
    CONFIG[bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩપ")] = bstack111111l_opy_ (u"ࠨࠥࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫફ")
  if bstack111111l_opy_ (u"ࠩࠧࡿࡉࡇࡔࡆࡡࡗࡍࡒࡋࡽࠨબ") in CONFIG[bstack111111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬભ")]:
    bstack1lll11lll1_opy_()
    os.environ[bstack111111l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨમ")] = CONFIG[bstack111111l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧય")]
  if not bstack111111l_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨર") in CONFIG[bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઱")]:
    return
  bstack11l1111l1_opy_ = bstack111111l_opy_ (u"ࠨࠩલ")
  bstack1l1l111lll_opy_ = bstack111llll111_opy_()
  if bstack1l1l111lll_opy_ != -1:
    bstack11l1111l1_opy_ = bstack111111l_opy_ (u"ࠩࡆࡍࠥ࠭ળ") + str(bstack1l1l111lll_opy_)
  if bstack11l1111l1_opy_ == bstack111111l_opy_ (u"ࠪࠫ઴"):
    bstack11l11llll_opy_ = bstack1lll1lllll_opy_(CONFIG[bstack111111l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧવ")])
    if bstack11l11llll_opy_ != -1:
      bstack11l1111l1_opy_ = str(bstack11l11llll_opy_)
  if bstack11l1111l1_opy_:
    bstack1ll1l11l1l_opy_(bstack11l1111l1_opy_)
    os.environ[bstack111111l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩશ")] = CONFIG[bstack111111l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨષ")]
def bstack1ll11l1111_opy_(bstack1111l1ll1l_opy_, bstack111l1ll111_opy_, path):
  json_data = {
    bstack111111l_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫસ"): bstack111l1ll111_opy_
  }
  if os.path.exists(path):
    bstack1111l1lll1_opy_ = json.load(open(path, bstack111111l_opy_ (u"ࠨࡴࡥࠫહ")))
  else:
    bstack1111l1lll1_opy_ = {}
  bstack1111l1lll1_opy_[bstack1111l1ll1l_opy_] = json_data
  with open(path, bstack111111l_opy_ (u"ࠤࡺ࠯ࠧ઺")) as outfile:
    json.dump(bstack1111l1lll1_opy_, outfile)
def bstack1lll1lllll_opy_(bstack1111l1ll1l_opy_):
  bstack1111l1ll1l_opy_ = str(bstack1111l1ll1l_opy_)
  bstack1111l11l11_opy_ = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠪࢂࠬ઻")), bstack111111l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮઼ࠫ"))
  try:
    if not os.path.exists(bstack1111l11l11_opy_):
      os.makedirs(bstack1111l11l11_opy_)
    file_path = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠬࢄࠧઽ")), bstack111111l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ા"), bstack111111l_opy_ (u"ࠧ࠯ࡤࡸ࡭ࡱࡪ࠭࡯ࡣࡰࡩ࠲ࡩࡡࡤࡪࡨ࠲࡯ࡹ࡯࡯ࠩિ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack111111l_opy_ (u"ࠨࡹࠪી")):
        pass
      with open(file_path, bstack111111l_opy_ (u"ࠤࡺ࠯ࠧુ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack111111l_opy_ (u"ࠪࡶࠬૂ")) as bstack1l1ll1l111_opy_:
      bstack1lll11111_opy_ = json.load(bstack1l1ll1l111_opy_)
    if bstack1111l1ll1l_opy_ in bstack1lll11111_opy_:
      bstack111l11l1ll_opy_ = bstack1lll11111_opy_[bstack1111l1ll1l_opy_][bstack111111l_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨૃ")]
      bstack11ll1l111l_opy_ = int(bstack111l11l1ll_opy_) + 1
      bstack1ll11l1111_opy_(bstack1111l1ll1l_opy_, bstack11ll1l111l_opy_, file_path)
      return bstack11ll1l111l_opy_
    else:
      bstack1ll11l1111_opy_(bstack1111l1ll1l_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack11lll1lll_opy_.format(str(e)))
    return -1
def bstack1l1l1ll1ll_opy_(config):
  if not config[bstack111111l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧૄ")] or not config[bstack111111l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩૅ")]:
    return True
  else:
    return False
def bstack1ll11l11ll_opy_(config, index=0):
  global bstack1ll11lll11_opy_
  bstack1lllll111l_opy_ = {}
  caps = bstack1l1l11111l_opy_ + bstack1ll1ll1ll_opy_
  if config.get(bstack111111l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ૆"), False):
    bstack1lllll111l_opy_[bstack111111l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬે")] = True
    bstack1lllll111l_opy_[bstack111111l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ૈ")] = config.get(bstack111111l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧૉ"), {})
  if bstack1ll11lll11_opy_:
    caps += bstack11l1111ll1_opy_
  for key in config:
    if key in caps + [bstack111111l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૊")]:
      continue
    bstack1lllll111l_opy_[key] = config[key]
  if bstack111111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨો") in config:
    for bstack111ll1ll1_opy_ in config[bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩૌ")][index]:
      if bstack111ll1ll1_opy_ in caps:
        continue
      bstack1lllll111l_opy_[bstack111ll1ll1_opy_] = config[bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵ્ࠪ")][index][bstack111ll1ll1_opy_]
  bstack1lllll111l_opy_[bstack111111l_opy_ (u"ࠨࡪࡲࡷࡹࡔࡡ࡮ࡧࠪ૎")] = socket.gethostname()
  if bstack111111l_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ૏") in bstack1lllll111l_opy_:
    del (bstack1lllll111l_opy_[bstack111111l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫૐ")])
  return bstack1lllll111l_opy_
def bstack1l1l1lll11_opy_(config):
  global bstack1ll11lll11_opy_
  bstack1l1l11lll1_opy_ = {}
  caps = bstack1ll1ll1ll_opy_
  if bstack1ll11lll11_opy_:
    caps += bstack11l1111ll1_opy_
  for key in caps:
    if key in config:
      bstack1l1l11lll1_opy_[key] = config[key]
  return bstack1l1l11lll1_opy_
def bstack11l1ll11l1_opy_(bstack1lllll111l_opy_, bstack1l1l11lll1_opy_):
  bstack1l11ll1lll_opy_ = {}
  for key in bstack1lllll111l_opy_.keys():
    if key in bstack11llllll1_opy_:
      bstack1l11ll1lll_opy_[bstack11llllll1_opy_[key]] = bstack1lllll111l_opy_[key]
    else:
      bstack1l11ll1lll_opy_[key] = bstack1lllll111l_opy_[key]
  for key in bstack1l1l11lll1_opy_:
    if key in bstack11llllll1_opy_:
      bstack1l11ll1lll_opy_[bstack11llllll1_opy_[key]] = bstack1l1l11lll1_opy_[key]
    else:
      bstack1l11ll1lll_opy_[key] = bstack1l1l11lll1_opy_[key]
  return bstack1l11ll1lll_opy_
def bstack1l11ll1111_opy_(config, index=0):
  global bstack1ll11lll11_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11l11ll1l_opy_ = bstack1l1lll1l11_opy_(bstack1l1ll1lll1_opy_, config, logger)
  bstack1l1l11lll1_opy_ = bstack1l1l1lll11_opy_(config)
  bstack1lll111l1_opy_ = bstack1ll1ll1ll_opy_
  bstack1lll111l1_opy_ += bstack1l111l1ll1_opy_
  bstack1l1l11lll1_opy_ = update(bstack1l1l11lll1_opy_, bstack11l11ll1l_opy_)
  if bstack1ll11lll11_opy_:
    bstack1lll111l1_opy_ += bstack11l1111ll1_opy_
  if bstack111111l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૑") in config:
    if bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ૒") in config[bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૓")][index]:
      caps[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ૔")] = config[bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૕")][index][bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ૖")]
    if bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ૗") in config[bstack111111l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૘")][index]:
      caps[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭૙")] = str(config[bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૚")][index][bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ૛")])
    bstack1111llll1_opy_ = bstack1l1lll1l11_opy_(bstack1l1ll1lll1_opy_, config[bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૜")][index], logger)
    bstack1lll111l1_opy_ += list(bstack1111llll1_opy_.keys())
    for bstack1111l1111l_opy_ in bstack1lll111l1_opy_:
      if bstack1111l1111l_opy_ in config[bstack111111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૝")][index]:
        if bstack1111l1111l_opy_ == bstack111111l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ૞"):
          try:
            bstack1111llll1_opy_[bstack1111l1111l_opy_] = str(config[bstack111111l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૟")][index][bstack1111l1111l_opy_] * 1.0)
          except:
            bstack1111llll1_opy_[bstack1111l1111l_opy_] = str(config[bstack111111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૠ")][index][bstack1111l1111l_opy_])
        else:
          bstack1111llll1_opy_[bstack1111l1111l_opy_] = config[bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩૡ")][index][bstack1111l1111l_opy_]
        del (config[bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪૢ")][index][bstack1111l1111l_opy_])
    bstack1l1l11lll1_opy_ = update(bstack1l1l11lll1_opy_, bstack1111llll1_opy_)
  bstack1lllll111l_opy_ = bstack1ll11l11ll_opy_(config, index)
  for bstack1ll11ll1l1_opy_ in bstack1ll1ll1ll_opy_ + list(bstack11l11ll1l_opy_.keys()):
    if bstack1ll11ll1l1_opy_ in bstack1lllll111l_opy_:
      bstack1l1l11lll1_opy_[bstack1ll11ll1l1_opy_] = bstack1lllll111l_opy_[bstack1ll11ll1l1_opy_]
      del (bstack1lllll111l_opy_[bstack1ll11ll1l1_opy_])
  if bstack111ll11lll_opy_(config):
    bstack1lllll111l_opy_[bstack111111l_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨૣ")] = True
    caps.update(bstack1l1l11lll1_opy_)
    caps[bstack111111l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ૤")] = bstack1lllll111l_opy_
  else:
    bstack1lllll111l_opy_[bstack111111l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪ૥")] = False
    caps.update(bstack11l1ll11l1_opy_(bstack1lllll111l_opy_, bstack1l1l11lll1_opy_))
    if bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ૦") in caps:
      caps[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭૧")] = caps[bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ૨")]
      del (caps[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ૩")])
    if bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ૪") in caps:
      caps[bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ૫")] = caps[bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ૬")]
      del (caps[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ૭")])
  return caps
def bstack11l1l11ll1_opy_():
  global bstack1lll1ll1ll_opy_
  global CONFIG
  if bstack1ll1llllll_opy_() <= version.parse(bstack111111l_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬ૮")):
    if bstack1lll1ll1ll_opy_ != bstack111111l_opy_ (u"࠭ࠧ૯"):
      return bstack111111l_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣ૰") + bstack1lll1ll1ll_opy_ + bstack111111l_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧ૱")
    return bstack1ll1111111_opy_
  if bstack1lll1ll1ll_opy_ != bstack111111l_opy_ (u"ࠩࠪ૲"):
    return bstack111111l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧ૳") + bstack1lll1ll1ll_opy_ + bstack111111l_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧ૴")
  return bstack1l11111l1_opy_
def bstack1llll1lll1_opy_(options):
  return hasattr(options, bstack111111l_opy_ (u"ࠬࡹࡥࡵࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸࡾ࠭૵"))
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
def bstack1111l1l1ll_opy_(options, bstack111l1lllll_opy_):
  for bstack1llll11l1l_opy_ in bstack111l1lllll_opy_:
    if bstack1llll11l1l_opy_ in [bstack111111l_opy_ (u"࠭ࡡࡳࡩࡶࠫ૶"), bstack111111l_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ૷")]:
      continue
    if bstack1llll11l1l_opy_ in options._experimental_options:
      options._experimental_options[bstack1llll11l1l_opy_] = update(options._experimental_options[bstack1llll11l1l_opy_],
                                                         bstack111l1lllll_opy_[bstack1llll11l1l_opy_])
    else:
      options.add_experimental_option(bstack1llll11l1l_opy_, bstack111l1lllll_opy_[bstack1llll11l1l_opy_])
  if bstack111111l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭૸") in bstack111l1lllll_opy_:
    for arg in bstack111l1lllll_opy_[bstack111111l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧૹ")]:
      options.add_argument(arg)
    del (bstack111l1lllll_opy_[bstack111111l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨૺ")])
  if bstack111111l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨૻ") in bstack111l1lllll_opy_:
    for ext in bstack111l1lllll_opy_[bstack111111l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩૼ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack111l1lllll_opy_[bstack111111l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ૽")])
def bstack11llll111l_opy_(options, bstack1llll1ll11_opy_):
  if bstack111111l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭૾") in bstack1llll1ll11_opy_:
    for bstack111ll1l1ll_opy_ in bstack1llll1ll11_opy_[bstack111111l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ૿")]:
      if bstack111ll1l1ll_opy_ in options._preferences:
        options._preferences[bstack111ll1l1ll_opy_] = update(options._preferences[bstack111ll1l1ll_opy_], bstack1llll1ll11_opy_[bstack111111l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ଀")][bstack111ll1l1ll_opy_])
      else:
        options.set_preference(bstack111ll1l1ll_opy_, bstack1llll1ll11_opy_[bstack111111l_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩଁ")][bstack111ll1l1ll_opy_])
  if bstack111111l_opy_ (u"ࠫࡦࡸࡧࡴࠩଂ") in bstack1llll1ll11_opy_:
    for arg in bstack1llll1ll11_opy_[bstack111111l_opy_ (u"ࠬࡧࡲࡨࡵࠪଃ")]:
      options.add_argument(arg)
def bstack111ll11l11_opy_(options, bstack1l11ll111_opy_):
  if bstack111111l_opy_ (u"࠭ࡷࡦࡤࡹ࡭ࡪࡽࠧ଄") in bstack1l11ll111_opy_:
    options.use_webview(bool(bstack1l11ll111_opy_[bstack111111l_opy_ (u"ࠧࡸࡧࡥࡺ࡮࡫ࡷࠨଅ")]))
  bstack1111l1l1ll_opy_(options, bstack1l11ll111_opy_)
def bstack1111ll11l1_opy_(options, bstack11lll1ll1l_opy_):
  for bstack1ll1l1111_opy_ in bstack11lll1ll1l_opy_:
    if bstack1ll1l1111_opy_ in [bstack111111l_opy_ (u"ࠨࡶࡨࡧ࡭ࡴ࡯࡭ࡱࡪࡽࡕࡸࡥࡷ࡫ࡨࡻࠬଆ"), bstack111111l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧଇ")]:
      continue
    options.set_capability(bstack1ll1l1111_opy_, bstack11lll1ll1l_opy_[bstack1ll1l1111_opy_])
  if bstack111111l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଈ") in bstack11lll1ll1l_opy_:
    for arg in bstack11lll1ll1l_opy_[bstack111111l_opy_ (u"ࠫࡦࡸࡧࡴࠩଉ")]:
      options.add_argument(arg)
  if bstack111111l_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩଊ") in bstack11lll1ll1l_opy_:
    options.bstack11lll1l1l_opy_(bool(bstack11lll1ll1l_opy_[bstack111111l_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪଋ")]))
def bstack1l1l1l111l_opy_(options, bstack1ll1111ll1_opy_):
  for bstack1l1l11ll1_opy_ in bstack1ll1111ll1_opy_:
    if bstack1l1l11ll1_opy_ in [bstack111111l_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଌ"), bstack111111l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭଍")]:
      continue
    options._options[bstack1l1l11ll1_opy_] = bstack1ll1111ll1_opy_[bstack1l1l11ll1_opy_]
  if bstack111111l_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭଎") in bstack1ll1111ll1_opy_:
    for bstack111lll1ll1_opy_ in bstack1ll1111ll1_opy_[bstack111111l_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧଏ")]:
      options.bstack1lllll1ll1_opy_(
        bstack111lll1ll1_opy_, bstack1ll1111ll1_opy_[bstack111111l_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨଐ")][bstack111lll1ll1_opy_])
  if bstack111111l_opy_ (u"ࠬࡧࡲࡨࡵࠪ଑") in bstack1ll1111ll1_opy_:
    for arg in bstack1ll1111ll1_opy_[bstack111111l_opy_ (u"࠭ࡡࡳࡩࡶࠫ଒")]:
      options.add_argument(arg)
def bstack11lll11l1l_opy_(options, caps):
  if not hasattr(options, bstack111111l_opy_ (u"ࠧࡌࡇ࡜ࠫଓ")):
    return
  if options.KEY == bstack111111l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ଔ"):
    options = bstack1llll111l_opy_.bstack1ll1l1ll11_opy_(bstack1l1lllll11_opy_=options, config=CONFIG)
  if options.KEY == bstack111111l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧକ") and options.KEY in caps:
    bstack1111l1l1ll_opy_(options, caps[bstack111111l_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨଖ")])
  elif options.KEY == bstack111111l_opy_ (u"ࠫࡲࡵࡺ࠻ࡨ࡬ࡶࡪ࡬࡯ࡹࡑࡳࡸ࡮ࡵ࡮ࡴࠩଗ") and options.KEY in caps:
    bstack11llll111l_opy_(options, caps[bstack111111l_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪଘ")])
  elif options.KEY == bstack111111l_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧଙ") and options.KEY in caps:
    bstack1111ll11l1_opy_(options, caps[bstack111111l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨଚ")])
  elif options.KEY == bstack111111l_opy_ (u"ࠨ࡯ࡶ࠾ࡪࡪࡧࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩଛ") and options.KEY in caps:
    bstack111ll11l11_opy_(options, caps[bstack111111l_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪଜ")])
  elif options.KEY == bstack111111l_opy_ (u"ࠪࡷࡪࡀࡩࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩଝ") and options.KEY in caps:
    bstack1l1l1l111l_opy_(options, caps[bstack111111l_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪଞ")])
def bstack111l111l1l_opy_(caps):
  global bstack1ll11lll11_opy_
  if isinstance(os.environ.get(bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ଟ")), str):
    bstack1ll11lll11_opy_ = eval(os.getenv(bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧଠ")))
  if bstack1ll11lll11_opy_:
    if bstack111ll111l_opy_() < version.parse(bstack111111l_opy_ (u"ࠧ࠳࠰࠶࠲࠵࠭ଡ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack111111l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨଢ")
    if bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧଣ") in caps:
      browser = caps[bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨତ")]
    elif bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬଥ") in caps:
      browser = caps[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ଦ")]
    browser = str(browser).lower()
    if browser == bstack111111l_opy_ (u"࠭ࡩࡱࡪࡲࡲࡪ࠭ଧ") or browser == bstack111111l_opy_ (u"ࠧࡪࡲࡤࡨࠬନ"):
      browser = bstack111111l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨ଩")
    if browser == bstack111111l_opy_ (u"ࠩࡶࡥࡲࡹࡵ࡯ࡩࠪପ"):
      browser = bstack111111l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪଫ")
    if browser not in [bstack111111l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫବ"), bstack111111l_opy_ (u"ࠬ࡫ࡤࡨࡧࠪଭ"), bstack111111l_opy_ (u"࠭ࡩࡦࠩମ"), bstack111111l_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧଯ"), bstack111111l_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩର")]:
      return None
    try:
      package = bstack111111l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰ࠲ࡼ࡫ࡢࡥࡴ࡬ࡺࡪࡸ࠮ࡼࡿ࠱ࡳࡵࡺࡩࡰࡰࡶࠫ଱").format(browser)
      name = bstack111111l_opy_ (u"ࠪࡓࡵࡺࡩࡰࡰࡶࠫଲ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1llll1lll1_opy_(options):
        return None
      for bstack1ll11ll1l1_opy_ in caps.keys():
        options.set_capability(bstack1ll11ll1l1_opy_, caps[bstack1ll11ll1l1_opy_])
      bstack11lll11l1l_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1l11l11l11_opy_(options, bstack111l1l1l11_opy_):
  if not bstack1llll1lll1_opy_(options):
    return
  for bstack1ll11ll1l1_opy_ in bstack111l1l1l11_opy_.keys():
    if bstack1ll11ll1l1_opy_ in bstack1l111l1ll1_opy_:
      continue
    if bstack1ll11ll1l1_opy_ in options._caps and type(options._caps[bstack1ll11ll1l1_opy_]) in [dict, list]:
      options._caps[bstack1ll11ll1l1_opy_] = update(options._caps[bstack1ll11ll1l1_opy_], bstack111l1l1l11_opy_[bstack1ll11ll1l1_opy_])
    else:
      options.set_capability(bstack1ll11ll1l1_opy_, bstack111l1l1l11_opy_[bstack1ll11ll1l1_opy_])
  bstack11lll11l1l_opy_(options, bstack111l1l1l11_opy_)
  if bstack111111l_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪଳ") in options._caps:
    if options._caps[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ଴")] and options._caps[bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫଵ")].lower() != bstack111111l_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨଶ"):
      del options._caps[bstack111111l_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧଷ")]
def bstack1l11111111_opy_(proxy_config):
  if bstack111111l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ସ") in proxy_config:
    proxy_config[bstack111111l_opy_ (u"ࠪࡷࡸࡲࡐࡳࡱࡻࡽࠬହ")] = proxy_config[bstack111111l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ଺")]
    del (proxy_config[bstack111111l_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ଻")])
  if bstack111111l_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦ଼ࠩ") in proxy_config and proxy_config[bstack111111l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪଽ")].lower() != bstack111111l_opy_ (u"ࠨࡦ࡬ࡶࡪࡩࡴࠨା"):
    proxy_config[bstack111111l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬି")] = bstack111111l_opy_ (u"ࠪࡱࡦࡴࡵࡢ࡮ࠪୀ")
  if bstack111111l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡄࡹࡹࡵࡣࡰࡰࡩ࡭࡬࡛ࡲ࡭ࠩୁ") in proxy_config:
    proxy_config[bstack111111l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨୂ")] = bstack111111l_opy_ (u"࠭ࡰࡢࡥࠪୃ")
  return proxy_config
def bstack1l111llll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack111111l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭ୄ") in config:
    return proxy
  config[bstack111111l_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧ୅")] = bstack1l11111111_opy_(config[bstack111111l_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨ୆")])
  if proxy == None:
    proxy = Proxy(config[bstack111111l_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩେ")])
  return proxy
def bstack1l11lllll1_opy_(self):
  global CONFIG
  global bstack1lll11l11_opy_
  try:
    proxy = bstack1l1l1lllll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack111111l_opy_ (u"ࠫ࠳ࡶࡡࡤࠩୈ")):
        proxies = bstack1111llll11_opy_(proxy, bstack11l1l11ll1_opy_())
        if len(proxies) > 0:
          protocol, bstack11lllllll1_opy_ = proxies.popitem()
          if bstack111111l_opy_ (u"ࠧࡀ࠯࠰ࠤ୉") in bstack11lllllll1_opy_:
            return bstack11lllllll1_opy_
          else:
            return bstack111111l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢ୊") + bstack11lllllll1_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack111111l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡴࡷࡵࡸࡺࠢࡸࡶࡱࠦ࠺ࠡࡽࢀࠦୋ").format(str(e)))
  return bstack1lll11l11_opy_(self)
def bstack111l1111l_opy_():
  global CONFIG
  return bstack1l1111ll1l_opy_(CONFIG) and bstack11ll1l1lll_opy_() and bstack1ll1llllll_opy_() >= version.parse(bstack1l1ll1ll11_opy_)
def bstack111l11ll1_opy_():
  global CONFIG
  return (bstack111111l_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫୌ") in CONFIG or bstack111111l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ୍࠭") in CONFIG) and bstack11lll111l1_opy_()
def bstack11ll11lll1_opy_(config):
  bstack1l1l1l111_opy_ = {}
  if bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ୎") in config:
    bstack1l1l1l111_opy_ = config[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୏")]
  if bstack111111l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୐") in config:
    bstack1l1l1l111_opy_ = config[bstack111111l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୑")]
  proxy = bstack1l1l1lllll_opy_(config)
  if proxy:
    if proxy.endswith(bstack111111l_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ୒")) and os.path.isfile(proxy):
      bstack1l1l1l111_opy_[bstack111111l_opy_ (u"ࠨ࠯ࡳࡥࡨ࠳ࡦࡪ࡮ࡨࠫ୓")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack111111l_opy_ (u"ࠩ࠱ࡴࡦࡩࠧ୔")):
        proxies = bstack1l111111ll_opy_(config, bstack11l1l11ll1_opy_())
        if len(proxies) > 0:
          protocol, bstack11lllllll1_opy_ = proxies.popitem()
          if bstack111111l_opy_ (u"ࠥ࠾࠴࠵ࠢ୕") in bstack11lllllll1_opy_:
            parsed_url = urlparse(bstack11lllllll1_opy_)
          else:
            parsed_url = urlparse(protocol + bstack111111l_opy_ (u"ࠦ࠿࠵࠯ࠣୖ") + bstack11lllllll1_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1l1l1l111_opy_[bstack111111l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡌࡴࡹࡴࠨୗ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1l1l1l111_opy_[bstack111111l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡕࡵࡲࡵࠩ୘")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1l1l1l111_opy_[bstack111111l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡛ࡳࡦࡴࠪ୙")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1l1l1l111_opy_[bstack111111l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡢࡵࡶࠫ୚")] = str(parsed_url.password)
  return bstack1l1l1l111_opy_
def bstack11ll1lll1l_opy_(config):
  if bstack111111l_opy_ (u"ࠩࡷࡩࡸࡺࡃࡰࡰࡷࡩࡽࡺࡏࡱࡶ࡬ࡳࡳࡹࠧ୛") in config:
    return config[bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨଡ଼")]
  return {}
def bstack1lll1llll1_opy_(caps):
  global bstack1ll1l1l111_opy_
  if bstack111111l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬଢ଼") in caps:
    caps[bstack111111l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭୞")][bstack111111l_opy_ (u"࠭࡬ࡰࡥࡤࡰࠬୟ")] = True
    if bstack1ll1l1l111_opy_:
      caps[bstack111111l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨୠ")][bstack111111l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪୡ")] = bstack1ll1l1l111_opy_
  else:
    caps[bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࠧୢ")] = True
    if bstack1ll1l1l111_opy_:
      caps[bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫୣ")] = bstack1ll1l1l111_opy_
@measure(event_name=EVENTS.bstack111l1111ll_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1llll1l11l_opy_():
  global CONFIG
  if not bstack11l1l1l1ll_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ୤") in CONFIG and bstack1llll11lll_opy_(CONFIG[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ୥")]):
    if (
      bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ୦") in CONFIG
      and bstack1llll11lll_opy_(CONFIG[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୧")].get(bstack111111l_opy_ (u"ࠨࡵ࡮࡭ࡵࡈࡩ࡯ࡣࡵࡽࡎࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡡࡵ࡫ࡲࡲࠬ୨")))
    ):
      logger.debug(bstack111111l_opy_ (u"ࠤࡏࡳࡨࡧ࡬ࠡࡤ࡬ࡲࡦࡸࡹࠡࡰࡲࡸࠥࡹࡴࡢࡴࡷࡩࡩࠦࡡࡴࠢࡶ࡯࡮ࡶࡂࡪࡰࡤࡶࡾࡏ࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡢࡶ࡬ࡳࡳࠦࡩࡴࠢࡨࡲࡦࡨ࡬ࡦࡦࠥ୩"))
      return
    bstack1l1l1l111_opy_ = bstack11ll11lll1_opy_(CONFIG)
    bstack11l1llllll_opy_(CONFIG[bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭୪")], bstack1l1l1l111_opy_)
def bstack11l1llllll_opy_(key, bstack1l1l1l111_opy_):
  global bstack1l11l1111l_opy_
  logger.info(bstack111l1l1l1_opy_)
  try:
    bstack1l11l1111l_opy_ = Local()
    bstack11lll11l11_opy_ = {bstack111111l_opy_ (u"ࠫࡰ࡫ࡹࠨ୫"): key}
    bstack11lll11l11_opy_.update(bstack1l1l1l111_opy_)
    logger.debug(bstack1ll11111l_opy_.format(str(bstack11lll11l11_opy_)).replace(key, bstack111111l_opy_ (u"ࠬࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩ୬")))
    bstack1l11l1111l_opy_.start(**bstack11lll11l11_opy_)
    if bstack1l11l1111l_opy_.isRunning():
      logger.info(bstack1lll11l1ll_opy_)
  except Exception as e:
    bstack1ll111l11_opy_(bstack1ll1ll1111_opy_.format(str(e)))
def bstack1111l111ll_opy_():
  global bstack1l11l1111l_opy_
  if bstack1l11l1111l_opy_.isRunning():
    logger.info(bstack11l11l11ll_opy_)
    bstack1l11l1111l_opy_.stop()
  bstack1l11l1111l_opy_ = None
def bstack1l1l1l1l11_opy_(bstack111ll1l111_opy_=[]):
  global CONFIG
  bstack1ll1l11111_opy_ = []
  bstack1111l1llll_opy_ = [bstack111111l_opy_ (u"࠭࡯ࡴࠩ୭"), bstack111111l_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪ୮"), bstack111111l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ୯"), bstack111111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ୰"), bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨୱ"), bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ୲")]
  try:
    for err in bstack111ll1l111_opy_:
      bstack111l1lll11_opy_ = {}
      for k in bstack1111l1llll_opy_:
        val = CONFIG[bstack111111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ୳")][int(err[bstack111111l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ୴")])].get(k)
        if val:
          bstack111l1lll11_opy_[k] = val
      if(err[bstack111111l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭୵")] != bstack111111l_opy_ (u"ࠨࠩ୶")):
        bstack111l1lll11_opy_[bstack111111l_opy_ (u"ࠩࡷࡩࡸࡺࡳࠨ୷")] = {
          err[bstack111111l_opy_ (u"ࠪࡲࡦࡳࡥࠨ୸")]: err[bstack111111l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ୹")]
        }
        bstack1ll1l11111_opy_.append(bstack111l1lll11_opy_)
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡱࡵࡱࡦࡺࡴࡪࡰࡪࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡥࡷࡧࡱࡸ࠿ࠦࠧ୺") + str(e))
  finally:
    return bstack1ll1l11111_opy_
def bstack11llll1ll_opy_(file_name):
  bstack1lll1lll11_opy_ = []
  try:
    bstack1l1l111111_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1l1l111111_opy_):
      with open(bstack1l1l111111_opy_) as f:
        bstack1lll1ll11l_opy_ = json.load(f)
        bstack1lll1lll11_opy_ = bstack1lll1ll11l_opy_
      os.remove(bstack1l1l111111_opy_)
    return bstack1lll1lll11_opy_
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨ࡬ࡲࡩ࡯࡮ࡨࠢࡨࡶࡷࡵࡲࠡ࡮࡬ࡷࡹࡀࠠࠨ୻") + str(e))
    return bstack1lll1lll11_opy_
def bstack1l1l11ll1l_opy_():
  try:
      from bstack_utils.constants import bstack1llllll1l1_opy_, EVENTS
      from bstack_utils.helper import bstack1l11l1ll1l_opy_, get_host_info, bstack11111lll_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack1ll1l111l1_opy_ = os.path.join(os.getcwd(), bstack111111l_opy_ (u"ࠧ࡭ࡱࡪࠫ୼"), bstack111111l_opy_ (u"ࠨ࡭ࡨࡽ࠲ࡳࡥࡵࡴ࡬ࡧࡸ࠴ࡪࡴࡱࡱࠫ୽"))
      lock = FileLock(bstack1ll1l111l1_opy_+bstack111111l_opy_ (u"ࠤ࠱ࡰࡴࡩ࡫ࠣ୾"))
      def bstack1l11l1ll_opy_():
          try:
              with lock:
                  with open(bstack1ll1l111l1_opy_, bstack111111l_opy_ (u"ࠥࡶࠧ୿"), encoding=bstack111111l_opy_ (u"ࠦࡺࡺࡦ࠮࠺ࠥ஀")) as file:
                      data = json.load(file)
                      config = {
                          bstack111111l_opy_ (u"ࠧ࡮ࡥࡢࡦࡨࡶࡸࠨ஁"): {
                              bstack111111l_opy_ (u"ࠨࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠧஂ"): bstack111111l_opy_ (u"ࠢࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠥஃ"),
                          }
                      }
                      bstack1l1ll111l_opy_ = datetime.utcnow()
                      bstack1llll1ll_opy_ = bstack1l1ll111l_opy_.strftime(bstack111111l_opy_ (u"ࠣࠧ࡜࠱ࠪࡳ࠭ࠦࡦࡗࠩࡍࡀࠥࡎ࠼ࠨࡗ࠳ࠫࡦࠡࡗࡗࡇࠧ஄"))
                      test_id = os.environ.get(bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧஅ")) if os.environ.get(bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨஆ")) else bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠦࡸࡪ࡫ࡓࡷࡱࡍࡩࠨஇ"))
                      payload = {
                          bstack111111l_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦࠤஈ"): bstack111111l_opy_ (u"ࠨࡳࡥ࡭ࡢࡩࡻ࡫࡮ࡵࡵࠥஉ"),
                          bstack111111l_opy_ (u"ࠢࡥࡣࡷࡥࠧஊ"): {
                              bstack111111l_opy_ (u"ࠣࡶࡨࡷࡹ࡮ࡵࡣࡡࡸࡹ࡮ࡪࠢ஋"): test_id,
                              bstack111111l_opy_ (u"ࠤࡦࡶࡪࡧࡴࡦࡦࡢࡨࡦࡿࠢ஌"): bstack1llll1ll_opy_,
                              bstack111111l_opy_ (u"ࠥࡩࡻ࡫࡮ࡵࡡࡱࡥࡲ࡫ࠢ஍"): bstack111111l_opy_ (u"ࠦࡘࡊࡋࡇࡧࡤࡸࡺࡸࡥࡑࡧࡵࡪࡴࡸ࡭ࡢࡰࡦࡩࠧஎ"),
                              bstack111111l_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣ࡯ࡹ࡯࡯ࠤஏ"): {
                                  bstack111111l_opy_ (u"ࠨ࡭ࡦࡣࡶࡹࡷ࡫ࡳࠣஐ"): data,
                                  bstack111111l_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤ஑"): bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥஒ"))
                              },
                              bstack111111l_opy_ (u"ࠤࡸࡷࡪࡸ࡟ࡥࡣࡷࡥࠧஓ"): bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠥࡹࡸ࡫ࡲࡏࡣࡰࡩࠧஔ")),
                              bstack111111l_opy_ (u"ࠦ࡭ࡵࡳࡵࡡ࡬ࡲ࡫ࡵࠢக"): get_host_info()
                          }
                      }
                      bstack1ll111ll1l_opy_ = bstack1lll1111l_opy_(cli.config, [bstack111111l_opy_ (u"ࠧࡧࡰࡪࡵࠥ஖"), bstack111111l_opy_ (u"ࠨࡥࡥࡵࡌࡲࡸࡺࡲࡶ࡯ࡨࡲࡹࡧࡴࡪࡱࡱࠦ஗"), bstack111111l_opy_ (u"ࠢࡢࡲ࡬ࠦ஘")], bstack1llllll1l1_opy_)
                      response = bstack1l11l1ll1l_opy_(bstack111111l_opy_ (u"ࠣࡒࡒࡗ࡙ࠨங"), bstack1ll111ll1l_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack111111l_opy_ (u"ࠤࡇࡥࡹࡧࠠࡴࡧࡱࡸࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭࡮ࡼࠤࡹࡵࠠࡼࡿࠣࡻ࡮ࡺࡨࠡࡦࡤࡸࡦࠦࡻࡾࠤச").format(bstack1llllll1l1_opy_, payload))
                      else:
                          logger.debug(bstack111111l_opy_ (u"ࠥࡖࡪࡷࡵࡦࡵࡷࠤ࡫ࡧࡩ࡭ࡧࡧࠤ࡫ࡵࡲࠡࡽࢀࠤࡼ࡯ࡴࡩࠢࡧࡥࡹࡧࠠࡼࡿࠥ஛").format(bstack1llllll1l1_opy_, payload))
          except Exception as e:
              logger.debug(bstack111111l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡱࡨࠥࡱࡥࡺࠢࡰࡩࡹࡸࡩࡤࡵࠣࡨࡦࡺࡡࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶࠥࢁࡽࠣஜ").format(e))
      bstack1l11l1ll_opy_()
      bstack11l1lll11l_opy_(bstack1ll1l111l1_opy_, logger)
  except:
    pass
def bstack1ll11l1l1_opy_():
  global bstack11ll1ll11l_opy_
  global bstack1111l11l1l_opy_
  global bstack1ll1111l1l_opy_
  global bstack111lll11l_opy_
  global bstack11l1111lll_opy_
  global bstack111l1ll1l_opy_
  global CONFIG
  bstack1l1l111l1_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭஝"))
  if bstack1l1l111l1_opy_ in [bstack111111l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬஞ"), bstack111111l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ட")]:
    bstack1l1l11l11l_opy_()
  percy.shutdown()
  if bstack11ll1ll11l_opy_:
    logger.warning(bstack11l11l1ll1_opy_.format(str(bstack11ll1ll11l_opy_)))
  else:
    try:
      bstack1111l1lll1_opy_ = bstack1ll1l1ll1_opy_(bstack111111l_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧ஠"), logger)
      if bstack1111l1lll1_opy_.get(bstack111111l_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ஡")) and bstack1111l1lll1_opy_.get(bstack111111l_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨ஢")).get(bstack111111l_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭ண")):
        logger.warning(bstack11l11l1ll1_opy_.format(str(bstack1111l1lll1_opy_[bstack111111l_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪத")][bstack111111l_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ஥")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack111ll111l1_opy_.invoke(Events.bstack11l1l11l1_opy_)
  logger.info(bstack11ll1ll111_opy_)
  global bstack1l11l1111l_opy_
  if bstack1l11l1111l_opy_:
    bstack1111l111ll_opy_()
  try:
    with bstack11l111l111_opy_:
      bstack1111l11ll1_opy_ = bstack1111l11l1l_opy_.copy()
    for driver in bstack1111l11ll1_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1l1l11l1ll_opy_)
  if bstack111l1ll1l_opy_ == bstack111111l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭஦"):
    bstack11l1111lll_opy_ = bstack11llll1ll_opy_(bstack111111l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩ஧"))
  if bstack111l1ll1l_opy_ == bstack111111l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩந") and len(bstack111lll11l_opy_) == 0:
    bstack111lll11l_opy_ = bstack11llll1ll_opy_(bstack111111l_opy_ (u"ࠪࡴࡼࡥࡰࡺࡶࡨࡷࡹࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶ࠱࡮ࡸࡵ࡮ࠨன"))
    if len(bstack111lll11l_opy_) == 0:
      bstack111lll11l_opy_ = bstack11llll1ll_opy_(bstack111111l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࡣࡵࡶࡰࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪப"))
  bstack1ll1ll1lll_opy_ = bstack111111l_opy_ (u"ࠬ࠭஫")
  if len(bstack1ll1111l1l_opy_) > 0:
    bstack1ll1ll1lll_opy_ = bstack1l1l1l1l11_opy_(bstack1ll1111l1l_opy_)
  elif len(bstack111lll11l_opy_) > 0:
    bstack1ll1ll1lll_opy_ = bstack1l1l1l1l11_opy_(bstack111lll11l_opy_)
  elif len(bstack11l1111lll_opy_) > 0:
    bstack1ll1ll1lll_opy_ = bstack1l1l1l1l11_opy_(bstack11l1111lll_opy_)
  elif len(bstack1ll111llll_opy_) > 0:
    bstack1ll1ll1lll_opy_ = bstack1l1l1l1l11_opy_(bstack1ll111llll_opy_)
  if bool(bstack1ll1ll1lll_opy_):
    bstack1llll1l1ll_opy_(bstack1ll1ll1lll_opy_)
  else:
    bstack1llll1l1ll_opy_()
  bstack11l1lll11l_opy_(bstack1l11l1l1l1_opy_, logger)
  if bstack1l1l111l1_opy_ not in [bstack111111l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ஬")]:
    bstack1l1l11ll1l_opy_()
  bstack11111ll111_opy_.bstack1l11l1l1_opy_(CONFIG)
  if len(bstack11l1111lll_opy_) > 0:
    sys.exit(len(bstack11l1111lll_opy_))
def bstack1llll11ll1_opy_(bstack11111ll1ll_opy_, frame):
  global bstack11111lll_opy_
  logger.error(bstack111ll1l11_opy_)
  bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡏࡱࠪ஭"), bstack11111ll1ll_opy_)
  if hasattr(signal, bstack111111l_opy_ (u"ࠨࡕ࡬࡫ࡳࡧ࡬ࡴࠩம")):
    bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩய"), signal.Signals(bstack11111ll1ll_opy_).name)
  else:
    bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪர"), bstack111111l_opy_ (u"ࠫࡘࡏࡇࡖࡐࡎࡒࡔ࡝ࡎࠨற"))
  if cli.is_running():
    bstack111ll111l1_opy_.invoke(Events.bstack11l1l11l1_opy_)
  bstack1l1l111l1_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭ல"))
  if bstack1l1l111l1_opy_ == bstack111111l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ள") and not cli.is_enabled(CONFIG):
    bstack1ll1l111_opy_.stop(bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧழ")))
  bstack1ll11l1l1_opy_()
  sys.exit(1)
def bstack1ll111l11_opy_(err):
  logger.critical(bstack111ll1ll11_opy_.format(str(err)))
  bstack1llll1l1ll_opy_(bstack111ll1ll11_opy_.format(str(err)), True)
  atexit.unregister(bstack1ll11l1l1_opy_)
  bstack1l1l11l11l_opy_()
  sys.exit(1)
def bstack1l11l1lll1_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1llll1l1ll_opy_(message, True)
  atexit.unregister(bstack1ll11l1l1_opy_)
  bstack1l1l11l11l_opy_()
  sys.exit(1)
def bstack11ll111l1_opy_():
  global CONFIG
  global bstack1l1111111_opy_
  global bstack1l11l1ll1_opy_
  global bstack1l11l11lll_opy_
  CONFIG = bstack11111111l_opy_()
  load_dotenv(CONFIG.get(bstack111111l_opy_ (u"ࠨࡧࡱࡺࡋ࡯࡬ࡦࠩவ")))
  bstack1l1lll11ll_opy_()
  bstack111l1l11ll_opy_()
  CONFIG = bstack1ll1l111l_opy_(CONFIG)
  update(CONFIG, bstack1l11l1ll1_opy_)
  update(CONFIG, bstack1l1111111_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1l1111l11l_opy_(CONFIG)
  bstack1l11l11lll_opy_ = bstack11l1l1l1ll_opy_(CONFIG)
  os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬஶ")] = bstack1l11l11lll_opy_.__str__().lower()
  bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫஷ"), bstack1l11l11lll_opy_)
  if (bstack111111l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧஸ") in CONFIG and bstack111111l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨஹ") in bstack1l1111111_opy_) or (
          bstack111111l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ஺") in CONFIG and bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ஻") not in bstack1l11l1ll1_opy_):
    if os.getenv(bstack111111l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ஼")):
      CONFIG[bstack111111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ஽")] = os.getenv(bstack111111l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧா"))
    else:
      if not CONFIG.get(bstack111111l_opy_ (u"ࠦ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠢி"), bstack111111l_opy_ (u"ࠧࠨீ")) in bstack1111ll1ll1_opy_:
        bstack1lll1l1l1l_opy_()
  elif (bstack111111l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩு") not in CONFIG and bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩூ") in CONFIG) or (
          bstack111111l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௃") in bstack1l11l1ll1_opy_ and bstack111111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௄") not in bstack1l1111111_opy_):
    del (CONFIG[bstack111111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ௅")])
  if bstack1l1l1ll1ll_opy_(CONFIG):
    bstack1ll111l11_opy_(bstack111llll1ll_opy_)
  Config.bstack111l111l_opy_().set_property(bstack111111l_opy_ (u"ࠦࡺࡹࡥࡳࡐࡤࡱࡪࠨெ"), CONFIG[bstack111111l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧே")])
  bstack11l1l1ll11_opy_()
  bstack1l11lll11_opy_()
  if bstack1ll11lll11_opy_ and not CONFIG.get(bstack111111l_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠤை"), bstack111111l_opy_ (u"ࠢࠣ௉")) in bstack1111ll1ll1_opy_:
    CONFIG[bstack111111l_opy_ (u"ࠨࡣࡳࡴࠬொ")] = bstack1ll11llll_opy_(CONFIG)
    logger.info(bstack1ll111111l_opy_.format(CONFIG[bstack111111l_opy_ (u"ࠩࡤࡴࡵ࠭ோ")]))
  if not bstack1l11l11lll_opy_:
    CONFIG[bstack111111l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ௌ")] = [{}]
def bstack1ll1l1lll_opy_(config, bstack11l11lll1l_opy_):
  global CONFIG
  global bstack1ll11lll11_opy_
  CONFIG = config
  bstack1ll11lll11_opy_ = bstack11l11lll1l_opy_
def bstack1l11lll11_opy_():
  global CONFIG
  global bstack1ll11lll11_opy_
  if bstack111111l_opy_ (u"ࠫࡦࡶࡰࠨ்") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l11l1lll1_opy_(e, bstack1111llllll_opy_)
    bstack1ll11lll11_opy_ = True
    bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ௎"), True)
def bstack1ll11llll_opy_(config):
  bstack1l11l11111_opy_ = bstack111111l_opy_ (u"࠭ࠧ௏")
  app = config[bstack111111l_opy_ (u"ࠧࡢࡲࡳࠫௐ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1l1l11l11_opy_:
      if os.path.exists(app):
        bstack1l11l11111_opy_ = bstack1l11ll11l_opy_(config, app)
      elif bstack1l1l111l1l_opy_(app):
        bstack1l11l11111_opy_ = app
      else:
        bstack1ll111l11_opy_(bstack11l1ll111l_opy_.format(app))
    else:
      if bstack1l1l111l1l_opy_(app):
        bstack1l11l11111_opy_ = app
      elif os.path.exists(app):
        bstack1l11l11111_opy_ = bstack1l11ll11l_opy_(app)
      else:
        bstack1ll111l11_opy_(bstack1l11lll1l_opy_)
  else:
    if len(app) > 2:
      bstack1ll111l11_opy_(bstack1l1111111l_opy_)
    elif len(app) == 2:
      if bstack111111l_opy_ (u"ࠨࡲࡤࡸ࡭࠭௑") in app and bstack111111l_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬ௒") in app:
        if os.path.exists(app[bstack111111l_opy_ (u"ࠪࡴࡦࡺࡨࠨ௓")]):
          bstack1l11l11111_opy_ = bstack1l11ll11l_opy_(config, app[bstack111111l_opy_ (u"ࠫࡵࡧࡴࡩࠩ௔")], app[bstack111111l_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ௕")])
        else:
          bstack1ll111l11_opy_(bstack11l1ll111l_opy_.format(app))
      else:
        bstack1ll111l11_opy_(bstack1l1111111l_opy_)
    else:
      for key in app:
        if key in bstack111lll1l1_opy_:
          if key == bstack111111l_opy_ (u"࠭ࡰࡢࡶ࡫ࠫ௖"):
            if os.path.exists(app[key]):
              bstack1l11l11111_opy_ = bstack1l11ll11l_opy_(config, app[key])
            else:
              bstack1ll111l11_opy_(bstack11l1ll111l_opy_.format(app))
          else:
            bstack1l11l11111_opy_ = app[key]
        else:
          bstack1ll111l11_opy_(bstack11ll1l11l_opy_)
  return bstack1l11l11111_opy_
def bstack1l1l111l1l_opy_(bstack1l11l11111_opy_):
  import re
  bstack1l11llll11_opy_ = re.compile(bstack111111l_opy_ (u"ࡲࠣࡠ࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯ࠪࠢௗ"))
  bstack11111l1lll_opy_ = re.compile(bstack111111l_opy_ (u"ࡳࠤࡡ࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰࠯࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭ࠨࠧ௘"))
  if bstack111111l_opy_ (u"ࠩࡥࡷ࠿࠵࠯ࠨ௙") in bstack1l11l11111_opy_ or re.fullmatch(bstack1l11llll11_opy_, bstack1l11l11111_opy_) or re.fullmatch(bstack11111l1lll_opy_, bstack1l11l11111_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack111l1l1ll_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1l11ll11l_opy_(config, path, bstack11l11ll111_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack111111l_opy_ (u"ࠪࡶࡧ࠭௚")).read()).hexdigest()
  bstack1l1l1111ll_opy_ = bstack1l1ll11ll1_opy_(md5_hash)
  bstack1l11l11111_opy_ = None
  if bstack1l1l1111ll_opy_:
    logger.info(bstack1111llll1l_opy_.format(bstack1l1l1111ll_opy_, md5_hash))
    return bstack1l1l1111ll_opy_
  bstack1111ll111_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack111111l_opy_ (u"ࠫ࡫࡯࡬ࡦࠩ௛"): (os.path.basename(path), open(os.path.abspath(path), bstack111111l_opy_ (u"ࠬࡸࡢࠨ௜")), bstack111111l_opy_ (u"࠭ࡴࡦࡺࡷ࠳ࡵࡲࡡࡪࡰࠪ௝")),
      bstack111111l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪ௞"): bstack11l11ll111_opy_
    }
  )
  response = requests.post(bstack1ll11ll11l_opy_, data=multipart_data,
                           headers={bstack111111l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧ௟"): multipart_data.content_type},
                           auth=(config[bstack111111l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ௠")], config[bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭௡")]))
  try:
    res = json.loads(response.text)
    bstack1l11l11111_opy_ = res[bstack111111l_opy_ (u"ࠫࡦࡶࡰࡠࡷࡵࡰࠬ௢")]
    logger.info(bstack1111l111l_opy_.format(bstack1l11l11111_opy_))
    bstack1lllll1111_opy_(md5_hash, bstack1l11l11111_opy_)
    cli.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽ࡹࡵࡲ࡯ࡢࡦࡢࡥࡵࡶࠢ௣"), datetime.datetime.now() - bstack1111ll111_opy_)
  except ValueError as err:
    bstack1ll111l11_opy_(bstack11l111l1l1_opy_.format(str(err)))
  return bstack1l11l11111_opy_
def bstack11l1l1ll11_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1l1llll1ll_opy_
  bstack1lll1l111_opy_ = 1
  bstack1lll11l1l_opy_ = 1
  if bstack111111l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭௤") in CONFIG:
    bstack1lll11l1l_opy_ = CONFIG[bstack111111l_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ௥")]
  else:
    bstack1lll11l1l_opy_ = bstack111llllll1_opy_(framework_name, args) or 1
  if bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ௦") in CONFIG:
    bstack1lll1l111_opy_ = len(CONFIG[bstack111111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ௧")])
  bstack1l1llll1ll_opy_ = int(bstack1lll11l1l_opy_) * int(bstack1lll1l111_opy_)
def bstack111llllll1_opy_(framework_name, args):
  if framework_name == bstack1l1111l11_opy_ and args and bstack111111l_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ௨") in args:
      bstack11l1lll1l1_opy_ = args.index(bstack111111l_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ௩"))
      return int(args[bstack11l1lll1l1_opy_ + 1]) or 1
  return 1
def bstack1l1ll11ll1_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack111111l_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨ௪"))
    bstack111l1l111l_opy_ = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"࠭ࡾࠨ௫")), bstack111111l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ௬"), bstack111111l_opy_ (u"ࠨࡣࡳࡴ࡚ࡶ࡬ࡰࡣࡧࡑࡉ࠻ࡈࡢࡵ࡫࠲࡯ࡹ࡯࡯ࠩ௭"))
    if os.path.exists(bstack111l1l111l_opy_):
      try:
        bstack1ll11l11l1_opy_ = json.load(open(bstack111l1l111l_opy_, bstack111111l_opy_ (u"ࠩࡵࡦࠬ௮")))
        if md5_hash in bstack1ll11l11l1_opy_:
          bstack1l11lll11l_opy_ = bstack1ll11l11l1_opy_[md5_hash]
          bstack1111l11ll_opy_ = datetime.datetime.now()
          bstack111lll11ll_opy_ = datetime.datetime.strptime(bstack1l11lll11l_opy_[bstack111111l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭௯")], bstack111111l_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨ௰"))
          if (bstack1111l11ll_opy_ - bstack111lll11ll_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack1l11lll11l_opy_[bstack111111l_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ௱")]):
            return None
          return bstack1l11lll11l_opy_[bstack111111l_opy_ (u"࠭ࡩࡥࠩ௲")]
      except Exception as e:
        logger.debug(bstack111111l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩࠢࡩ࡭ࡱ࡫࠺ࠡࡽࢀࠫ௳").format(str(e)))
    return None
  bstack111l1l111l_opy_ = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠨࢀࠪ௴")), bstack111111l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ௵"), bstack111111l_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫ௶"))
  lock_file = bstack111l1l111l_opy_ + bstack111111l_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪ௷")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111l1l111l_opy_):
        with open(bstack111l1l111l_opy_, bstack111111l_opy_ (u"ࠬࡸࠧ௸")) as f:
          content = f.read().strip()
          if content:
            bstack1ll11l11l1_opy_ = json.loads(content)
            if md5_hash in bstack1ll11l11l1_opy_:
              bstack1l11lll11l_opy_ = bstack1ll11l11l1_opy_[md5_hash]
              bstack1111l11ll_opy_ = datetime.datetime.now()
              bstack111lll11ll_opy_ = datetime.datetime.strptime(bstack1l11lll11l_opy_[bstack111111l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩ௹")], bstack111111l_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫ௺"))
              if (bstack1111l11ll_opy_ - bstack111lll11ll_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack1l11lll11l_opy_[bstack111111l_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭௻")]):
                return None
              return bstack1l11lll11l_opy_[bstack111111l_opy_ (u"ࠩ࡬ࡨࠬ௼")]
      return None
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡺ࡭ࡹ࡮ࠠࡧ࡫࡯ࡩࠥࡲ࡯ࡤ࡭࡬ࡲ࡬ࠦࡦࡰࡴࠣࡑࡉ࠻ࠠࡩࡣࡶ࡬࠿ࠦࡻࡾࠩ௽").format(str(e)))
    return None
def bstack1lllll1111_opy_(md5_hash, bstack1l11l11111_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack111111l_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧ௾"))
    bstack1111l11l11_opy_ = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠬࢄࠧ௿")), bstack111111l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ఀ"))
    if not os.path.exists(bstack1111l11l11_opy_):
      os.makedirs(bstack1111l11l11_opy_)
    bstack111l1l111l_opy_ = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠧࡿࠩఁ")), bstack111111l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨం"), bstack111111l_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪః"))
    bstack1ll1l1l1ll_opy_ = {
      bstack111111l_opy_ (u"ࠪ࡭ࡩ࠭ఄ"): bstack1l11l11111_opy_,
      bstack111111l_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧఅ"): datetime.datetime.strftime(datetime.datetime.now(), bstack111111l_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩఆ")),
      bstack111111l_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫఇ"): str(__version__)
    }
    try:
      bstack1ll11l11l1_opy_ = {}
      if os.path.exists(bstack111l1l111l_opy_):
        bstack1ll11l11l1_opy_ = json.load(open(bstack111l1l111l_opy_, bstack111111l_opy_ (u"ࠧࡳࡤࠪఈ")))
      bstack1ll11l11l1_opy_[md5_hash] = bstack1ll1l1l1ll_opy_
      with open(bstack111l1l111l_opy_, bstack111111l_opy_ (u"ࠣࡹ࠮ࠦఉ")) as outfile:
        json.dump(bstack1ll11l11l1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack111111l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡷࡳࡨࡦࡺࡩ࡯ࡩࠣࡑࡉ࠻ࠠࡩࡣࡶ࡬ࠥ࡬ࡩ࡭ࡧ࠽ࠤࢀࢃࠧఊ").format(str(e)))
    return
  bstack1111l11l11_opy_ = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠪࢂࠬఋ")), bstack111111l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఌ"))
  if not os.path.exists(bstack1111l11l11_opy_):
    os.makedirs(bstack1111l11l11_opy_)
  bstack111l1l111l_opy_ = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠬࢄࠧ఍")), bstack111111l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ఎ"), bstack111111l_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨఏ"))
  lock_file = bstack111l1l111l_opy_ + bstack111111l_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧఐ")
  bstack1ll1l1l1ll_opy_ = {
    bstack111111l_opy_ (u"ࠩ࡬ࡨࠬ఑"): bstack1l11l11111_opy_,
    bstack111111l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ఒ"): datetime.datetime.strftime(datetime.datetime.now(), bstack111111l_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨఓ")),
    bstack111111l_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪఔ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1ll11l11l1_opy_ = {}
      if os.path.exists(bstack111l1l111l_opy_):
        with open(bstack111l1l111l_opy_, bstack111111l_opy_ (u"࠭ࡲࠨక")) as f:
          content = f.read().strip()
          if content:
            bstack1ll11l11l1_opy_ = json.loads(content)
      bstack1ll11l11l1_opy_[md5_hash] = bstack1ll1l1l1ll_opy_
      with open(bstack111l1l111l_opy_, bstack111111l_opy_ (u"ࠢࡸࠤఖ")) as outfile:
        json.dump(bstack1ll11l11l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡸ࡫ࡷ࡬ࠥ࡬ࡩ࡭ࡧࠣࡰࡴࡩ࡫ࡪࡰࡪࠤ࡫ࡵࡲࠡࡏࡇ࠹ࠥ࡮ࡡࡴࡪࠣࡹࡵࡪࡡࡵࡧ࠽ࠤࢀࢃࠧగ").format(str(e)))
def bstack1l1111l111_opy_(self):
  return
def bstack11111l1l1_opy_(self):
  return
def bstack111111lll_opy_():
  global bstack111l1llll1_opy_
  bstack111l1llll1_opy_ = True
@measure(event_name=EVENTS.bstack1ll1lll11_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1l111ll111_opy_(self):
  global bstack1l111111l_opy_
  global bstack1l1ll11lll_opy_
  global bstack1lll1111ll_opy_
  try:
    if bstack111111l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩఘ") in bstack1l111111l_opy_ and self.session_id != None and bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧఙ"), bstack111111l_opy_ (u"ࠫࠬచ")) != bstack111111l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ఛ"):
      bstack111llll11_opy_ = bstack111111l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭జ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111111l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧఝ")
      if bstack111llll11_opy_ == bstack111111l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨఞ"):
        bstack1l111ll1l_opy_(logger)
      if self != None:
        bstack1ll111l1ll_opy_(self, bstack111llll11_opy_, bstack111111l_opy_ (u"ࠩ࠯ࠤࠬట").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack111111l_opy_ (u"ࠪࠫఠ")
    if bstack111111l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫడ") in bstack1l111111l_opy_ and getattr(threading.current_thread(), bstack111111l_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫఢ"), None):
      bstack1llll1111_opy_.bstack111l1lll_opy_(self, bstack1l1l1l11l_opy_, logger, wait=True)
    if bstack111111l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ణ") in bstack1l111111l_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1ll111l1ll_opy_(self, bstack111111l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢత"))
      bstack1l1111l1l_opy_.bstack1l11l111l_opy_(self)
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࠤథ") + str(e))
  bstack1lll1111ll_opy_(self)
  self.session_id = None
def bstack11lllllll_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1l111l1l1l_opy_
    global bstack1l111111l_opy_
    command_executor = kwargs.get(bstack111111l_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠬద"), bstack111111l_opy_ (u"ࠪࠫధ"))
    bstack1l11l111l1_opy_ = False
    if type(command_executor) == str and bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧన") in command_executor:
      bstack1l11l111l1_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨ఩") in str(getattr(command_executor, bstack111111l_opy_ (u"࠭࡟ࡶࡴ࡯ࠫప"), bstack111111l_opy_ (u"ࠧࠨఫ"))):
      bstack1l11l111l1_opy_ = True
    else:
      kwargs = bstack1llll111l_opy_.bstack1ll1l1ll11_opy_(bstack1l1lllll11_opy_=kwargs, config=CONFIG)
      return bstack1ll1111lll_opy_(self, *args, **kwargs)
    if bstack1l11l111l1_opy_:
      bstack1l1l1l1ll_opy_ = bstack1l1l1l1l1_opy_.bstack1111111ll_opy_(CONFIG, bstack1l111111l_opy_)
      if kwargs.get(bstack111111l_opy_ (u"ࠨࡱࡳࡸ࡮ࡵ࡮ࡴࠩబ")):
        kwargs[bstack111111l_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪభ")] = bstack1l111l1l1l_opy_(kwargs[bstack111111l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫమ")], bstack1l111111l_opy_, CONFIG, bstack1l1l1l1ll_opy_)
      elif kwargs.get(bstack111111l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫయ")):
        kwargs[bstack111111l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬర")] = bstack1l111l1l1l_opy_(kwargs[bstack111111l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ఱ")], bstack1l111111l_opy_, CONFIG, bstack1l1l1l1ll_opy_)
  except Exception as e:
    logger.error(bstack111111l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩࡧࡱࠤࡵࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡕࡇࡏࠥࡩࡡࡱࡵ࠽ࠤࢀࢃࠢల").format(str(e)))
  return bstack1ll1111lll_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l1111ll11_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1l1l1ll111_opy_(self, command_executor=bstack111111l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰࠳࠵࠻࠳࠶࠮࠱࠰࠴࠾࠹࠺࠴࠵ࠤళ"), *args, **kwargs):
  global bstack1l1ll11lll_opy_
  global bstack1111l11l1l_opy_
  bstack1ll1llll1_opy_ = bstack11lllllll_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1ll1l1ll_opy_.on():
    return bstack1ll1llll1_opy_
  try:
    logger.debug(bstack111111l_opy_ (u"ࠩࡆࡳࡲࡳࡡ࡯ࡦࠣࡉࡽ࡫ࡣࡶࡶࡲࡶࠥࡽࡨࡦࡰࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡩࡴࠢࡩࡥࡱࡹࡥࠡ࠯ࠣࡿࢂ࠭ఴ").format(str(command_executor)))
    logger.debug(bstack111111l_opy_ (u"ࠪࡌࡺࡨࠠࡖࡔࡏࠤ࡮ࡹࠠ࠮ࠢࡾࢁࠬవ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧశ") in command_executor._url:
      bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ష"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩస") in command_executor):
    bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨహ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1ll11l1ll1_opy_ = getattr(threading.current_thread(), bstack111111l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡕࡧࡶࡸࡒ࡫ࡴࡢࠩ఺"), None)
  bstack11111l111_opy_ = {}
  if self.capabilities is not None:
    bstack11111l111_opy_[bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨ఻")] = self.capabilities.get(bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ఼"))
    bstack11111l111_opy_[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ఽ")] = self.capabilities.get(bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ా"))
    bstack11111l111_opy_[bstack111111l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡥ࡯ࡱࡶ࡬ࡳࡳࡹࠧి")] = self.capabilities.get(bstack111111l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬీ"))
  if CONFIG.get(bstack111111l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨు"), False) and bstack1llll111l_opy_.bstack1ll11l1l11_opy_(bstack11111l111_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack111111l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩూ") in bstack1l111111l_opy_ or bstack111111l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩృ") in bstack1l111111l_opy_:
    bstack1ll1l111_opy_.bstack1lll1l11l1_opy_(self)
  if bstack111111l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫౄ") in bstack1l111111l_opy_ and bstack1ll11l1ll1_opy_ and bstack1ll11l1ll1_opy_.get(bstack111111l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ౅"), bstack111111l_opy_ (u"࠭ࠧె")) == bstack111111l_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨే"):
    bstack1ll1l111_opy_.bstack1lll1l11l1_opy_(self)
  bstack1l1ll11lll_opy_ = self.session_id
  with bstack11l111l111_opy_:
    bstack1111l11l1l_opy_.append(self)
  return bstack1ll1llll1_opy_
def bstack111l1ll11l_opy_(args):
  return bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠩై") in str(args)
def bstack11l1l1l11l_opy_(self, driver_command, *args, **kwargs):
  global bstack1l1ll1lll_opy_
  global bstack111l111ll1_opy_
  bstack111l1l1ll1_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭౉"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack111111l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩొ"), None)
  bstack111lllll11_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫో"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack111111l_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧౌ"), None)
  bstack1ll1l1l1l_opy_ = getattr(self, bstack111111l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ్࠭"), None) != None and getattr(self, bstack111111l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ౎"), None) == True
  if not bstack111l111ll1_opy_ and bstack111111l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ౏") in CONFIG and CONFIG[bstack111111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ౐")] == True and bstack11l1llll11_opy_.bstack1ll111lll_opy_(driver_command) and (bstack1ll1l1l1l_opy_ or bstack111l1l1ll1_opy_ or bstack111lllll11_opy_) and not bstack111l1ll11l_opy_(args):
    try:
      bstack111l111ll1_opy_ = True
      logger.debug(bstack111111l_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥ࡬࡯ࡳࠢࡾࢁࠬ౑").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack111111l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡱࡧࡵࡪࡴࡸ࡭ࠡࡵࡦࡥࡳࠦࡻࡾࠩ౒").format(str(err)))
    bstack111l111ll1_opy_ = False
  response = bstack1l1ll1lll_opy_(self, driver_command, *args, **kwargs)
  if (bstack111111l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ౓") in str(bstack1l111111l_opy_).lower() or bstack111111l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭౔") in str(bstack1l111111l_opy_).lower()) and bstack1ll1l1ll_opy_.on():
    try:
      if driver_command == bstack111111l_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷౕࠫ"):
        bstack1ll1l111_opy_.bstack1l11ll111l_opy_({
            bstack111111l_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ౖࠧ"): response[bstack111111l_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨ౗")],
            bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪౘ"): bstack1ll1l111_opy_.current_test_uuid() if bstack1ll1l111_opy_.current_test_uuid() else bstack1ll1l1ll_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1111l1l11l_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1l1ll1ll1l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1l1ll11lll_opy_
  global bstack111lll111_opy_
  global bstack1l11llll1_opy_
  global bstack11111llll1_opy_
  global bstack1ll11ll1ll_opy_
  global bstack1l111111l_opy_
  global bstack1ll1111lll_opy_
  global bstack1111l11l1l_opy_
  global bstack1l1l11lll_opy_
  global bstack1l1l1l11l_opy_
  if os.getenv(bstack111111l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩౙ")) is not None and bstack1llll111l_opy_.bstack11llll1l11_opy_(CONFIG) is None:
    CONFIG[bstack111111l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬౚ")] = True
  CONFIG[bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨ౛")] = str(bstack1l111111l_opy_) + str(__version__)
  bstack11ll1lll1_opy_ = os.environ[bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ౜")]
  bstack1l1l1l1ll_opy_ = bstack1l1l1l1l1_opy_.bstack1111111ll_opy_(CONFIG, bstack1l111111l_opy_)
  CONFIG[bstack111111l_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫౝ")] = bstack11ll1lll1_opy_
  CONFIG[bstack111111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫ౞")] = bstack1l1l1l1ll_opy_
  if CONFIG.get(bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ౟"),bstack111111l_opy_ (u"ࠫࠬౠ")) and bstack111111l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫౡ") in bstack1l111111l_opy_:
    CONFIG[bstack111111l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ౢ")].pop(bstack111111l_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬౣ"), None)
    CONFIG[bstack111111l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ౤")].pop(bstack111111l_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ౥"), None)
  command_executor = bstack11l1l11ll1_opy_()
  logger.debug(bstack1ll1lllll1_opy_.format(command_executor))
  proxy = bstack1l111llll_opy_(CONFIG, proxy)
  bstack1111ll111l_opy_ = 0 if bstack111lll111_opy_ < 0 else bstack111lll111_opy_
  try:
    if bstack11111llll1_opy_ is True:
      bstack1111ll111l_opy_ = int(multiprocessing.current_process().name)
    elif bstack1ll11ll1ll_opy_ is True:
      bstack1111ll111l_opy_ = int(threading.current_thread().name)
  except:
    bstack1111ll111l_opy_ = 0
  bstack111l1l1l11_opy_ = bstack1l11ll1111_opy_(CONFIG, bstack1111ll111l_opy_)
  logger.debug(bstack1ll1ll11ll_opy_.format(str(bstack111l1l1l11_opy_)))
  if bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ౦") in CONFIG and bstack1llll11lll_opy_(CONFIG[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ౧")]):
    bstack1lll1llll1_opy_(bstack111l1l1l11_opy_)
  if bstack1llll111l_opy_.bstack1l1l1l11l1_opy_(CONFIG, bstack1111ll111l_opy_) and bstack1llll111l_opy_.bstack1l1l1ll11_opy_(bstack111l1l1l11_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack1llll111l_opy_.set_capabilities(bstack111l1l1l11_opy_, CONFIG)
  if desired_capabilities:
    bstack111111111_opy_ = bstack1ll1l111l_opy_(desired_capabilities)
    bstack111111111_opy_[bstack111111l_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬ౨")] = bstack111ll11lll_opy_(CONFIG)
    bstack111ll1l1l_opy_ = bstack1l11ll1111_opy_(bstack111111111_opy_)
    if bstack111ll1l1l_opy_:
      bstack111l1l1l11_opy_ = update(bstack111ll1l1l_opy_, bstack111l1l1l11_opy_)
    desired_capabilities = None
  if options:
    bstack1l11l11l11_opy_(options, bstack111l1l1l11_opy_)
  if not options:
    options = bstack111l111l1l_opy_(bstack111l1l1l11_opy_)
  bstack1l1l1l11l_opy_ = CONFIG.get(bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ౩"))[bstack1111ll111l_opy_]
  if proxy and bstack1ll1llllll_opy_() >= version.parse(bstack111111l_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧ౪")):
    options.proxy(proxy)
  if options and bstack1ll1llllll_opy_() >= version.parse(bstack111111l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ౫")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1ll1llllll_opy_() < version.parse(bstack111111l_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨ౬")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack111l1l1l11_opy_)
  logger.info(bstack11l1llll1l_opy_)
  bstack1l11ll11l1_opy_.end(EVENTS.bstack111ll11111_opy_.value, EVENTS.bstack111ll11111_opy_.value + bstack111111l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥ౭"), EVENTS.bstack111ll11111_opy_.value + bstack111111l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤ౮"), status=True, failure=None, test_name=bstack1l11llll1_opy_)
  if bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡰࡳࡱࡩ࡭ࡱ࡫ࠧ౯") in kwargs:
    del kwargs[bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡱࡴࡲࡪ࡮ࡲࡥࠨ౰")]
  try:
    if bstack1ll1llllll_opy_() >= version.parse(bstack111111l_opy_ (u"ࠧ࠵࠰࠴࠴࠳࠶ࠧ౱")):
      bstack1ll1111lll_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack1ll1llllll_opy_() >= version.parse(bstack111111l_opy_ (u"ࠨ࠵࠱࠼࠳࠶ࠧ౲")):
      bstack1ll1111lll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1ll1llllll_opy_() >= version.parse(bstack111111l_opy_ (u"ࠩ࠵࠲࠺࠹࠮࠱ࠩ౳")):
      bstack1ll1111lll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1ll1111lll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack1lll1l111l_opy_:
    logger.error(bstack1l111lll11_opy_.format(bstack111111l_opy_ (u"ࠪࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠩ౴"), str(bstack1lll1l111l_opy_)))
    raise bstack1lll1l111l_opy_
  if bstack1llll111l_opy_.bstack1l1l1l11l1_opy_(CONFIG, bstack1111ll111l_opy_) and bstack1llll111l_opy_.bstack1l1l1ll11_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack111111l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭౵")][bstack111111l_opy_ (u"ࠬࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ౶")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack1llll111l_opy_.set_capabilities(bstack111l1l1l11_opy_, CONFIG)
  try:
    bstack11l111l1ll_opy_ = bstack111111l_opy_ (u"࠭ࠧ౷")
    if bstack1ll1llllll_opy_() >= version.parse(bstack111111l_opy_ (u"ࠧ࠵࠰࠳࠲࠵ࡨ࠱ࠨ౸")):
      if self.caps is not None:
        bstack11l111l1ll_opy_ = self.caps.get(bstack111111l_opy_ (u"ࠣࡱࡳࡸ࡮ࡳࡡ࡭ࡊࡸࡦ࡚ࡸ࡬ࠣ౹"))
    else:
      if self.capabilities is not None:
        bstack11l111l1ll_opy_ = self.capabilities.get(bstack111111l_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤ౺"))
    if bstack11l111l1ll_opy_:
      bstack111ll11l1_opy_(bstack11l111l1ll_opy_)
      if bstack1ll1llllll_opy_() <= version.parse(bstack111111l_opy_ (u"ࠪ࠷࠳࠷࠳࠯࠲ࠪ౻")):
        self.command_executor._url = bstack111111l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧ౼") + bstack1lll1ll1ll_opy_ + bstack111111l_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤ౽")
      else:
        self.command_executor._url = bstack111111l_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣ౾") + bstack11l111l1ll_opy_ + bstack111111l_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣ౿")
      logger.debug(bstack1l1111ll1_opy_.format(bstack11l111l1ll_opy_))
    else:
      logger.debug(bstack1l1ll1ll1_opy_.format(bstack111111l_opy_ (u"ࠣࡑࡳࡸ࡮ࡳࡡ࡭ࠢࡋࡹࡧࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠤಀ")))
  except Exception as e:
    logger.debug(bstack1l1ll1ll1_opy_.format(e))
  if bstack111111l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨಁ") in bstack1l111111l_opy_:
    bstack11l1l1llll_opy_(bstack111lll111_opy_, bstack1l1l11lll_opy_)
  bstack1l1ll11lll_opy_ = self.session_id
  if bstack111111l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪಂ") in bstack1l111111l_opy_ or bstack111111l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫಃ") in bstack1l111111l_opy_ or bstack111111l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ಄") in bstack1l111111l_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1ll11l1ll1_opy_ = getattr(threading.current_thread(), bstack111111l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡚ࡥࡴࡶࡐࡩࡹࡧࠧಅ"), None)
  if bstack111111l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧಆ") in bstack1l111111l_opy_ or bstack111111l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧಇ") in bstack1l111111l_opy_:
    bstack1ll1l111_opy_.bstack1lll1l11l1_opy_(self)
  if bstack111111l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩಈ") in bstack1l111111l_opy_ and bstack1ll11l1ll1_opy_ and bstack1ll11l1ll1_opy_.get(bstack111111l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪಉ"), bstack111111l_opy_ (u"ࠫࠬಊ")) == bstack111111l_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭ಋ"):
    bstack1ll1l111_opy_.bstack1lll1l11l1_opy_(self)
  with bstack11l111l111_opy_:
    bstack1111l11l1l_opy_.append(self)
  if bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಌ") in CONFIG and bstack111111l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ಍") in CONFIG[bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಎ")][bstack1111ll111l_opy_]:
    bstack1l11llll1_opy_ = CONFIG[bstack111111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಏ")][bstack1111ll111l_opy_][bstack111111l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨಐ")]
  logger.debug(bstack1l111l1l11_opy_.format(bstack1l1ll11lll_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack111l11lll_opy_
    def bstack1111l111l1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack111l111lll_opy_
      if(bstack111111l_opy_ (u"ࠦ࡮ࡴࡤࡦࡺ࠱࡮ࡸࠨ಑") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠬࢄࠧಒ")), bstack111111l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ಓ"), bstack111111l_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩಔ")), bstack111111l_opy_ (u"ࠨࡹࠪಕ")) as fp:
          fp.write(bstack111111l_opy_ (u"ࠤࠥಖ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack111111l_opy_ (u"ࠥ࡭ࡳࡪࡥࡹࡡࡥࡷࡹࡧࡣ࡬࠰࡭ࡷࠧಗ")))):
          with open(args[1], bstack111111l_opy_ (u"ࠫࡷ࠭ಘ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack111111l_opy_ (u"ࠬࡧࡳࡺࡰࡦࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦ࡟࡯ࡧࡺࡔࡦ࡭ࡥࠩࡥࡲࡲࡹ࡫ࡸࡵ࠮ࠣࡴࡦ࡭ࡥࠡ࠿ࠣࡺࡴ࡯ࡤࠡ࠲ࠬࠫಙ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack111l1ll1l1_opy_)
            if bstack111111l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪಚ") in CONFIG and str(CONFIG[bstack111111l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫಛ")]).lower() != bstack111111l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧಜ"):
                bstack1l11111l1l_opy_ = bstack111l11lll_opy_()
                bstack11111l1l11_opy_ = bstack111111l_opy_ (u"ࠩࠪࠫࠏ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯ࠋࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬ࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴࡟࠾ࠎࡨࡵ࡮ࡴࡶࠣࡦࡸࡺࡡࡤ࡭ࡢࡧࡦࡶࡳࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠵ࡢࡁࠊࡤࡱࡱࡷࡹࠦࡰࡠ࡫ࡱࡨࡪࡾࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠵ࡡࡀࠐࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴ࡳ࡭࡫ࡦࡩ࠭࠶ࠬࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶࠭ࡀࠐࡣࡰࡰࡶࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭ࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ࠮ࡁࠊࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯࠳ࡩࡨࡳࡱࡰ࡭ࡺࡳ࠮࡭ࡣࡸࡲࡨ࡮ࠠ࠾ࠢࡤࡷࡾࡴࡣࠡࠪ࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴࠫࠣࡁࡃࠦࡻࡼࠌࠣࠤࡱ࡫ࡴࠡࡥࡤࡴࡸࡁࠊࠡࠢࡷࡶࡾࠦࡻࡼࠌࠣࠤࠥࠦࡣࡢࡲࡶࠤࡂࠦࡊࡔࡑࡑ࠲ࡵࡧࡲࡴࡧࠫࡦࡸࡺࡡࡤ࡭ࡢࡧࡦࡶࡳࠪ࠽ࠍࠤࠥࢃࡽࠡࡥࡤࡸࡨ࡮ࠠࠩࡧࡻ࠭ࠥࢁࡻࠋࠢࠣࠤࠥࡩ࡯࡯ࡵࡲࡰࡪ࠴ࡥࡳࡴࡲࡶ࠭ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡥࡷࡹࡥࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠺ࠣ࠮ࠣࡩࡽ࠯࠻ࠋࠢࠣࢁࢂࠐࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡣࡺࡥ࡮ࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯࠳ࡩࡨࡳࡱࡰ࡭ࡺࡳ࠮ࡤࡱࡱࡲࡪࡩࡴࠩࡽࡾࠎࠥࠦࠠࠡࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸ࠿ࠦࠧࡼࡥࡧࡴ࡚ࡸ࡬ࡾࠩࠣ࠯ࠥ࡫࡮ࡤࡱࡧࡩ࡚ࡘࡉࡄࡱࡰࡴࡴࡴࡥ࡯ࡶࠫࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡨࡧࡰࡴࠫࠬ࠰ࠏࠦࠠࠡࠢ࠱࠲࠳ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷࠏࠦࠠࡾࡿࠬ࠿ࠏࢃࡽ࠼ࠌ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠏ࠭ࠧࠨಝ").format(bstack1l11111l1l_opy_=bstack1l11111l1l_opy_)
            lines.insert(1, bstack11111l1l11_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack111111l_opy_ (u"ࠥ࡭ࡳࡪࡥࡹࡡࡥࡷࡹࡧࡣ࡬࠰࡭ࡷࠧಞ")), bstack111111l_opy_ (u"ࠫࡼ࠭ಟ")) as bstack11lll1l11_opy_:
              bstack11lll1l11_opy_.writelines(lines)
        CONFIG[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧಠ")] = str(bstack1l111111l_opy_) + str(__version__)
        bstack11ll1lll1_opy_ = os.environ[bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫಡ")]
        bstack1l1l1l1ll_opy_ = bstack1l1l1l1l1_opy_.bstack1111111ll_opy_(CONFIG, bstack1l111111l_opy_)
        CONFIG[bstack111111l_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪಢ")] = bstack11ll1lll1_opy_
        CONFIG[bstack111111l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪಣ")] = bstack1l1l1l1ll_opy_
        bstack1111ll111l_opy_ = 0 if bstack111lll111_opy_ < 0 else bstack111lll111_opy_
        try:
          if bstack11111llll1_opy_ is True:
            bstack1111ll111l_opy_ = int(multiprocessing.current_process().name)
          elif bstack1ll11ll1ll_opy_ is True:
            bstack1111ll111l_opy_ = int(threading.current_thread().name)
        except:
          bstack1111ll111l_opy_ = 0
        CONFIG[bstack111111l_opy_ (u"ࠤࡸࡷࡪ࡝࠳ࡄࠤತ")] = False
        CONFIG[bstack111111l_opy_ (u"ࠥ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤಥ")] = True
        bstack111l1l1l11_opy_ = bstack1l11ll1111_opy_(CONFIG, bstack1111ll111l_opy_)
        logger.debug(bstack1ll1ll11ll_opy_.format(str(bstack111l1l1l11_opy_)))
        if CONFIG.get(bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨದ")):
          bstack1lll1llll1_opy_(bstack111l1l1l11_opy_)
        if bstack111111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಧ") in CONFIG and bstack111111l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫನ") in CONFIG[bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ಩")][bstack1111ll111l_opy_]:
          bstack1l11llll1_opy_ = CONFIG[bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಪ")][bstack1111ll111l_opy_][bstack111111l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧಫ")]
        args.append(os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠪࢂࠬಬ")), bstack111111l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫಭ"), bstack111111l_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧಮ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack111l1l1l11_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack111111l_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣಯ"))
      bstack111l111lll_opy_ = True
      return bstack1l11l1l1l_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack11l1l11l1l_opy_(self,
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
    global bstack111lll111_opy_
    global bstack1l11llll1_opy_
    global bstack11111llll1_opy_
    global bstack1ll11ll1ll_opy_
    global bstack1l111111l_opy_
    CONFIG[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩರ")] = str(bstack1l111111l_opy_) + str(__version__)
    bstack11ll1lll1_opy_ = os.environ[bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ಱ")]
    bstack1l1l1l1ll_opy_ = bstack1l1l1l1l1_opy_.bstack1111111ll_opy_(CONFIG, bstack1l111111l_opy_)
    CONFIG[bstack111111l_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬಲ")] = bstack11ll1lll1_opy_
    CONFIG[bstack111111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬಳ")] = bstack1l1l1l1ll_opy_
    bstack1111ll111l_opy_ = 0 if bstack111lll111_opy_ < 0 else bstack111lll111_opy_
    try:
      if bstack11111llll1_opy_ is True:
        bstack1111ll111l_opy_ = int(multiprocessing.current_process().name)
      elif bstack1ll11ll1ll_opy_ is True:
        bstack1111ll111l_opy_ = int(threading.current_thread().name)
    except:
      bstack1111ll111l_opy_ = 0
    CONFIG[bstack111111l_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ಴")] = True
    bstack111l1l1l11_opy_ = bstack1l11ll1111_opy_(CONFIG, bstack1111ll111l_opy_)
    logger.debug(bstack1ll1ll11ll_opy_.format(str(bstack111l1l1l11_opy_)))
    if CONFIG.get(bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩವ")):
      bstack1lll1llll1_opy_(bstack111l1l1l11_opy_)
    if bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಶ") in CONFIG and bstack111111l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬಷ") in CONFIG[bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಸ")][bstack1111ll111l_opy_]:
      bstack1l11llll1_opy_ = CONFIG[bstack111111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಹ")][bstack1111ll111l_opy_][bstack111111l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ಺")]
    import urllib
    import json
    if bstack111111l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ಻") in CONFIG and str(CONFIG[bstack111111l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦ಼ࠩ")]).lower() != bstack111111l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬಽ"):
        bstack11111ll11l_opy_ = bstack111l11lll_opy_()
        bstack1l11111l1l_opy_ = bstack11111ll11l_opy_ + urllib.parse.quote(json.dumps(bstack111l1l1l11_opy_))
    else:
        bstack1l11111l1l_opy_ = bstack111111l_opy_ (u"ࠧࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ࠩಾ") + urllib.parse.quote(json.dumps(bstack111l1l1l11_opy_))
    browser = self.connect(bstack1l11111l1l_opy_)
    return browser
except Exception as e:
    pass
def bstack1l11l1l1ll_opy_():
    global bstack111l111lll_opy_
    global bstack1l111111l_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1l1l1lll1l_opy_
        global bstack11111lll_opy_
        if not bstack1l11l11lll_opy_:
          global bstack1111lllll1_opy_
          if not bstack1111lllll1_opy_:
            from bstack_utils.helper import bstack111ll1lll1_opy_, bstack111lll1111_opy_, bstack1l1111lll1_opy_
            bstack1111lllll1_opy_ = bstack111ll1lll1_opy_()
            bstack111lll1111_opy_(bstack1l111111l_opy_)
            bstack1l1l1l1ll_opy_ = bstack1l1l1l1l1_opy_.bstack1111111ll_opy_(CONFIG, bstack1l111111l_opy_)
            bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠣࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡖࡒࡐࡆࡘࡇ࡙ࡥࡍࡂࡒࠥಿ"), bstack1l1l1l1ll_opy_)
          BrowserType.connect = bstack1l1l1lll1l_opy_
          return
        BrowserType.launch = bstack11l1l11l1l_opy_
        bstack111l111lll_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1111l111l1_opy_
      bstack111l111lll_opy_ = True
    except Exception as e:
      pass
def bstack11l111l1l_opy_(context, bstack1l11l1l11l_opy_):
  try:
    context.page.evaluate(bstack111111l_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥೀ"), bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠧು")+ json.dumps(bstack1l11l1l11l_opy_) + bstack111111l_opy_ (u"ࠦࢂࢃࠢೂ"))
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡼࡿ࠽ࠤࢀࢃࠢೃ").format(str(e), traceback.format_exc()))
def bstack11l1l1ll1l_opy_(context, message, level):
  try:
    context.page.evaluate(bstack111111l_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢೄ"), bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ೅") + json.dumps(message) + bstack111111l_opy_ (u"ࠨ࠮ࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠫೆ") + json.dumps(level) + bstack111111l_opy_ (u"ࠩࢀࢁࠬೇ"))
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡡ࡯ࡰࡲࡸࡦࡺࡩࡰࡰࠣࡿࢂࡀࠠࡼࡿࠥೈ").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack11ll1l1ll1_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack11l1ll1lll_opy_(self, url):
  global bstack11l111111l_opy_
  try:
    bstack1111l1l11_opy_(url)
  except Exception as err:
    logger.debug(bstack1l1lll1ll1_opy_.format(str(err)))
  try:
    bstack11l111111l_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack11lllll11l_opy_):
        bstack1111l1l11_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1l1lll1ll1_opy_.format(str(err)))
    raise e
def bstack111l11ll11_opy_(self):
  global bstack1l1ll11111_opy_
  bstack1l1ll11111_opy_ = self
  return
def bstack1l11lllll_opy_(self):
  global bstack11ll111ll_opy_
  bstack11ll111ll_opy_ = self
  return
def bstack11lllll1l1_opy_(test_name, bstack111l1l11l1_opy_):
  global CONFIG
  if percy.bstack1111l1111_opy_() == bstack111111l_opy_ (u"ࠦࡹࡸࡵࡦࠤ೉"):
    bstack1l1lll11l1_opy_ = os.path.relpath(bstack111l1l11l1_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1l1lll11l1_opy_)
    bstack1l111l1ll_opy_ = suite_name + bstack111111l_opy_ (u"ࠧ࠳ࠢೊ") + test_name
    threading.current_thread().percySessionName = bstack1l111l1ll_opy_
def bstack11lll1l11l_opy_(self, test, *args, **kwargs):
  global bstack1l11ll11ll_opy_
  test_name = None
  bstack111l1l11l1_opy_ = None
  if test:
    test_name = str(test.name)
    bstack111l1l11l1_opy_ = str(test.source)
  bstack11lllll1l1_opy_(test_name, bstack111l1l11l1_opy_)
  bstack1l11ll11ll_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1ll1llll11_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack11l1111l1l_opy_(driver, bstack1l111l1ll_opy_):
  if not bstack111llll11l_opy_ and bstack1l111l1ll_opy_:
      bstack111ll1l11l_opy_ = {
          bstack111111l_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭ೋ"): bstack111111l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨೌ"),
          bstack111111l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶ್ࠫ"): {
              bstack111111l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ೎"): bstack1l111l1ll_opy_
          }
      }
      bstack11l1ll1111_opy_ = bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨ೏").format(json.dumps(bstack111ll1l11l_opy_))
      driver.execute_script(bstack11l1ll1111_opy_)
  if bstack1ll1llll1l_opy_:
      bstack11lllll1ll_opy_ = {
          bstack111111l_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫ೐"): bstack111111l_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ೑"),
          bstack111111l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ೒"): {
              bstack111111l_opy_ (u"ࠧࡥࡣࡷࡥࠬ೓"): bstack1l111l1ll_opy_ + bstack111111l_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪ೔"),
              bstack111111l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨೕ"): bstack111111l_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨೖ")
          }
      }
      if bstack1ll1llll1l_opy_.status == bstack111111l_opy_ (u"ࠫࡕࡇࡓࡔࠩ೗"):
          bstack1l1lll111_opy_ = bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪ೘").format(json.dumps(bstack11lllll1ll_opy_))
          driver.execute_script(bstack1l1lll111_opy_)
          bstack1ll111l1ll_opy_(driver, bstack111111l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭೙"))
      elif bstack1ll1llll1l_opy_.status == bstack111111l_opy_ (u"ࠧࡇࡃࡌࡐࠬ೚"):
          reason = bstack111111l_opy_ (u"ࠣࠤ೛")
          bstack1ll111l1l1_opy_ = bstack1l111l1ll_opy_ + bstack111111l_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠪ೜")
          if bstack1ll1llll1l_opy_.message:
              reason = str(bstack1ll1llll1l_opy_.message)
              bstack1ll111l1l1_opy_ = bstack1ll111l1l1_opy_ + bstack111111l_opy_ (u"ࠪࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲ࠻ࠢࠪೝ") + reason
          bstack11lllll1ll_opy_[bstack111111l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧೞ")] = {
              bstack111111l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ೟"): bstack111111l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬೠ"),
              bstack111111l_opy_ (u"ࠧࡥࡣࡷࡥࠬೡ"): bstack1ll111l1l1_opy_
          }
          bstack1l1lll111_opy_ = bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ೢ").format(json.dumps(bstack11lllll1ll_opy_))
          driver.execute_script(bstack1l1lll111_opy_)
          bstack1ll111l1ll_opy_(driver, bstack111111l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩೣ"), reason)
          bstack1l11ll1ll_opy_(reason, str(bstack1ll1llll1l_opy_), str(bstack111lll111_opy_), logger)
@measure(event_name=EVENTS.bstack1l11l11l1_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1ll1lll11l_opy_(driver, test):
  if percy.bstack1111l1111_opy_() == bstack111111l_opy_ (u"ࠥࡸࡷࡻࡥࠣ೤") and percy.bstack111lll1l11_opy_() == bstack111111l_opy_ (u"ࠦࡹ࡫ࡳࡵࡥࡤࡷࡪࠨ೥"):
      bstack11l1l11ll_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠬࡶࡥࡳࡥࡼࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ೦"), None)
      bstack1l1ll11l1_opy_(driver, bstack11l1l11ll_opy_, test)
  if (bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ೧"), None) and
      bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭೨"), None)) or (
      bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ೩"), None) and
      bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ೪"), None)):
      logger.info(bstack111111l_opy_ (u"ࠥࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠡࡒࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡭ࡸࠦࡵ࡯ࡦࡨࡶࡼࡧࡹ࠯ࠢࠥ೫"))
      bstack1llll111l_opy_.bstack1lllllll1_opy_(driver, name=test.name, path=test.source)
def bstack1ll1l1llll_opy_(test, bstack1l111l1ll_opy_):
    try:
      bstack1111ll111_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack111111l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ೬")] = bstack1l111l1ll_opy_
      if bstack1ll1llll1l_opy_:
        if bstack1ll1llll1l_opy_.status == bstack111111l_opy_ (u"ࠬࡖࡁࡔࡕࠪ೭"):
          data[bstack111111l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭೮")] = bstack111111l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ೯")
        elif bstack1ll1llll1l_opy_.status == bstack111111l_opy_ (u"ࠨࡈࡄࡍࡑ࠭೰"):
          data[bstack111111l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩೱ")] = bstack111111l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪೲ")
          if bstack1ll1llll1l_opy_.message:
            data[bstack111111l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫೳ")] = str(bstack1ll1llll1l_opy_.message)
      user = CONFIG[bstack111111l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ೴")]
      key = CONFIG[bstack111111l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ೵")]
      host = bstack1lll1111l_opy_(cli.config, [bstack111111l_opy_ (u"ࠢࡢࡲ࡬ࡷࠧ೶"), bstack111111l_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࠥ೷"), bstack111111l_opy_ (u"ࠤࡤࡴ࡮ࠨ೸")], bstack111111l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡶࡩ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠦ೹"))
      url = bstack111111l_opy_ (u"ࠫࢀࢃ࠯ࡢࡷࡷࡳࡲࡧࡴࡦ࠱ࡶࡩࡸࡹࡩࡰࡰࡶ࠳ࢀࢃ࠮࡫ࡵࡲࡲࠬ೺").format(host, bstack1l1ll11lll_opy_)
      headers = {
        bstack111111l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫ೻"): bstack111111l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ೼"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠢࡩࡶࡷࡴ࠿ࡻࡰࡥࡣࡷࡩࡤࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡺࡡࡵࡷࡶࠦ೽"), datetime.datetime.now() - bstack1111ll111_opy_)
    except Exception as e:
      logger.error(bstack11llll11l1_opy_.format(str(e)))
def bstack1ll1ll11l1_opy_(test, bstack1l111l1ll_opy_):
  global CONFIG
  global bstack11ll111ll_opy_
  global bstack1l1ll11111_opy_
  global bstack1l1ll11lll_opy_
  global bstack1ll1llll1l_opy_
  global bstack1l11llll1_opy_
  global bstack11ll1l11l1_opy_
  global bstack1ll1l1l1l1_opy_
  global bstack1l1lll11l_opy_
  global bstack1ll1ll11l_opy_
  global bstack1111l11l1l_opy_
  global bstack1l1l1l11l_opy_
  global bstack1l1ll1llll_opy_
  try:
    if not bstack1l1ll11lll_opy_:
      with bstack1l1ll1llll_opy_:
        bstack111l11111_opy_ = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠨࢀࠪ೾")), bstack111111l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ೿"), bstack111111l_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬഀ"))
        if os.path.exists(bstack111l11111_opy_):
          with open(bstack111l11111_opy_, bstack111111l_opy_ (u"ࠫࡷ࠭ഁ")) as f:
            content = f.read().strip()
            if content:
              bstack111l11l11_opy_ = json.loads(bstack111111l_opy_ (u"ࠧࢁࠢം") + content + bstack111111l_opy_ (u"࠭ࠢࡹࠤ࠽ࠤࠧࡿࠢࠨഃ") + bstack111111l_opy_ (u"ࠢࡾࠤഄ"))
              bstack1l1ll11lll_opy_ = bstack111l11l11_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡌࡈࡸࠦࡦࡪ࡮ࡨ࠾ࠥ࠭അ") + str(e))
  if bstack1111l11l1l_opy_:
    with bstack11l111l111_opy_:
      bstack1l1llll1l_opy_ = bstack1111l11l1l_opy_.copy()
    for driver in bstack1l1llll1l_opy_:
      if bstack1l1ll11lll_opy_ == driver.session_id:
        if test:
          bstack1ll1lll11l_opy_(driver, test)
        bstack11l1111l1l_opy_(driver, bstack1l111l1ll_opy_)
  elif bstack1l1ll11lll_opy_:
    bstack1ll1l1llll_opy_(test, bstack1l111l1ll_opy_)
  if bstack11ll111ll_opy_:
    bstack1ll1l1l1l1_opy_(bstack11ll111ll_opy_)
  if bstack1l1ll11111_opy_:
    bstack1l1lll11l_opy_(bstack1l1ll11111_opy_)
  if bstack111l1llll1_opy_:
    bstack1ll1ll11l_opy_()
def bstack1ll1lll111_opy_(self, test, *args, **kwargs):
  bstack1l111l1ll_opy_ = None
  if test:
    bstack1l111l1ll_opy_ = str(test.name)
  bstack1ll1ll11l1_opy_(test, bstack1l111l1ll_opy_)
  bstack11ll1l11l1_opy_(self, test, *args, **kwargs)
def bstack1l11ll1ll1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1llllll11l_opy_
  global CONFIG
  global bstack1111l11l1l_opy_
  global bstack1l1ll11lll_opy_
  global bstack1l1ll1llll_opy_
  bstack11l11l1lll_opy_ = None
  try:
    if bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨആ"), None) or bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬഇ"), None):
      try:
        if not bstack1l1ll11lll_opy_:
          bstack111l11111_opy_ = os.path.join(os.path.expanduser(bstack111111l_opy_ (u"ࠫࢃ࠭ഈ")), bstack111111l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬഉ"), bstack111111l_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨഊ"))
          with bstack1l1ll1llll_opy_:
            if os.path.exists(bstack111l11111_opy_):
              with open(bstack111l11111_opy_, bstack111111l_opy_ (u"ࠧࡳࠩഋ")) as f:
                content = f.read().strip()
                if content:
                  bstack111l11l11_opy_ = json.loads(bstack111111l_opy_ (u"ࠣࡽࠥഌ") + content + bstack111111l_opy_ (u"ࠩࠥࡼࠧࡀࠠࠣࡻࠥࠫ഍") + bstack111111l_opy_ (u"ࠥࢁࠧഎ"))
                  bstack1l1ll11lll_opy_ = bstack111l11l11_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack111111l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡶࡪࡧࡤࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡏࡄࡴࠢࡩ࡭ࡱ࡫ࠠࡪࡰࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࠪഏ") + str(e))
      if bstack1111l11l1l_opy_:
        with bstack11l111l111_opy_:
          bstack1l1llll1l_opy_ = bstack1111l11l1l_opy_.copy()
        for driver in bstack1l1llll1l_opy_:
          if bstack1l1ll11lll_opy_ == driver.session_id:
            bstack11l11l1lll_opy_ = driver
    bstack11lll1ll11_opy_ = bstack1llll111l_opy_.bstack11l11ll11l_opy_(test.tags)
    if bstack11l11l1lll_opy_:
      threading.current_thread().isA11yTest = bstack1llll111l_opy_.bstack1l111111l1_opy_(bstack11l11l1lll_opy_, bstack11lll1ll11_opy_)
      threading.current_thread().isAppA11yTest = bstack1llll111l_opy_.bstack1l111111l1_opy_(bstack11l11l1lll_opy_, bstack11lll1ll11_opy_)
    else:
      threading.current_thread().isA11yTest = bstack11lll1ll11_opy_
      threading.current_thread().isAppA11yTest = bstack11lll1ll11_opy_
  except:
    pass
  bstack1llllll11l_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1ll1llll1l_opy_
  try:
    bstack1ll1llll1l_opy_ = self._test
  except:
    bstack1ll1llll1l_opy_ = self.test
def bstack11ll1ll1l_opy_():
  global bstack1ll111l111_opy_
  try:
    if os.path.exists(bstack1ll111l111_opy_):
      os.remove(bstack1ll111l111_opy_)
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡥࡧ࡯ࡩࡹ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨഐ") + str(e))
def bstack11l1ll1ll1_opy_():
  global bstack1ll111l111_opy_
  bstack1111l1lll1_opy_ = {}
  lock_file = bstack1ll111l111_opy_ + bstack111111l_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬ഑")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack111111l_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠢࡱࡳࡹࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡥࡥࡸ࡯ࡣࠡࡨ࡬ࡰࡪࠦ࡯ࡱࡧࡵࡥࡹ࡯࡯࡯ࡵࠪഒ"))
    try:
      if not os.path.isfile(bstack1ll111l111_opy_):
        with open(bstack1ll111l111_opy_, bstack111111l_opy_ (u"ࠨࡹࠪഓ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1ll111l111_opy_):
        with open(bstack1ll111l111_opy_, bstack111111l_opy_ (u"ࠩࡵࠫഔ")) as f:
          content = f.read().strip()
          if content:
            bstack1111l1lll1_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack111111l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬക") + str(e))
    return bstack1111l1lll1_opy_
  try:
    os.makedirs(os.path.dirname(bstack1ll111l111_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack1ll111l111_opy_):
        with open(bstack1ll111l111_opy_, bstack111111l_opy_ (u"ࠫࡼ࠭ഖ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1ll111l111_opy_):
        with open(bstack1ll111l111_opy_, bstack111111l_opy_ (u"ࠬࡸࠧഗ")) as f:
          content = f.read().strip()
          if content:
            bstack1111l1lll1_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨഘ") + str(e))
  finally:
    return bstack1111l1lll1_opy_
def bstack11l1l1llll_opy_(platform_index, item_index):
  global bstack1ll111l111_opy_
  lock_file = bstack1ll111l111_opy_ + bstack111111l_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ࠭ങ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack111111l_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫച"))
    try:
      bstack1111l1lll1_opy_ = {}
      if os.path.exists(bstack1ll111l111_opy_):
        with open(bstack1ll111l111_opy_, bstack111111l_opy_ (u"ࠩࡵࠫഛ")) as f:
          content = f.read().strip()
          if content:
            bstack1111l1lll1_opy_ = json.loads(content)
      bstack1111l1lll1_opy_[item_index] = platform_index
      with open(bstack1ll111l111_opy_, bstack111111l_opy_ (u"ࠥࡻࠧജ")) as outfile:
        json.dump(bstack1111l1lll1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack111111l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡷࡳ࡫ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩഝ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack1ll111l111_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack1111l1lll1_opy_ = {}
      if os.path.exists(bstack1ll111l111_opy_):
        with open(bstack1ll111l111_opy_, bstack111111l_opy_ (u"ࠬࡸࠧഞ")) as f:
          content = f.read().strip()
          if content:
            bstack1111l1lll1_opy_ = json.loads(content)
      bstack1111l1lll1_opy_[item_index] = platform_index
      with open(bstack1ll111l111_opy_, bstack111111l_opy_ (u"ࠨࡷࠣട")) as outfile:
        json.dump(bstack1111l1lll1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡺࡶ࡮ࡺࡩ࡯ࡩࠣࡸࡴࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬഠ") + str(e))
def bstack1ll1lllll_opy_(bstack1l111llll1_opy_):
  global CONFIG
  bstack11llll11ll_opy_ = bstack111111l_opy_ (u"ࠨࠩഡ")
  if not bstack111111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬഢ") in CONFIG:
    logger.info(bstack111111l_opy_ (u"ࠪࡒࡴࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠢࡳࡥࡸࡹࡥࡥࠢࡸࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡫ࠠࡳࡧࡳࡳࡷࡺࠠࡧࡱࡵࠤࡗࡵࡢࡰࡶࠣࡶࡺࡴࠧണ"))
  try:
    platform = CONFIG[bstack111111l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧത")][bstack1l111llll1_opy_]
    if bstack111111l_opy_ (u"ࠬࡵࡳࠨഥ") in platform:
      bstack11llll11ll_opy_ += str(platform[bstack111111l_opy_ (u"࠭࡯ࡴࠩദ")]) + bstack111111l_opy_ (u"ࠧ࠭ࠢࠪധ")
    if bstack111111l_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫന") in platform:
      bstack11llll11ll_opy_ += str(platform[bstack111111l_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬഩ")]) + bstack111111l_opy_ (u"ࠪ࠰ࠥ࠭പ")
    if bstack111111l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨഫ") in platform:
      bstack11llll11ll_opy_ += str(platform[bstack111111l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩബ")]) + bstack111111l_opy_ (u"࠭ࠬࠡࠩഭ")
    if bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩമ") in platform:
      bstack11llll11ll_opy_ += str(platform[bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪയ")]) + bstack111111l_opy_ (u"ࠩ࠯ࠤࠬര")
    if bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨറ") in platform:
      bstack11llll11ll_opy_ += str(platform[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩല")]) + bstack111111l_opy_ (u"ࠬ࠲ࠠࠨള")
    if bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧഴ") in platform:
      bstack11llll11ll_opy_ += str(platform[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨവ")]) + bstack111111l_opy_ (u"ࠨ࠮ࠣࠫശ")
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠩࡖࡳࡲ࡫ࠠࡦࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡲ࡬ࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡵࡷࡶ࡮ࡴࡧࠡࡨࡲࡶࠥࡸࡥࡱࡱࡵࡸࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡯࡯ࠩഷ") + str(e))
  finally:
    if bstack11llll11ll_opy_[len(bstack11llll11ll_opy_) - 2:] == bstack111111l_opy_ (u"ࠪ࠰ࠥ࠭സ"):
      bstack11llll11ll_opy_ = bstack11llll11ll_opy_[:-2]
    return bstack11llll11ll_opy_
def bstack111llll1l1_opy_(path, bstack11llll11ll_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l1l1l1ll1_opy_ = ET.parse(path)
    bstack111llll1l_opy_ = bstack1l1l1l1ll1_opy_.getroot()
    bstack1ll11l1l1l_opy_ = None
    for suite in bstack111llll1l_opy_.iter(bstack111111l_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪഹ")):
      if bstack111111l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬഺ") in suite.attrib:
        suite.attrib[bstack111111l_opy_ (u"࠭࡮ࡢ࡯ࡨ഻ࠫ")] += bstack111111l_opy_ (u"഼ࠧࠡࠩ") + bstack11llll11ll_opy_
        bstack1ll11l1l1l_opy_ = suite
    bstack11lll11111_opy_ = None
    for robot in bstack111llll1l_opy_.iter(bstack111111l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧഽ")):
      bstack11lll11111_opy_ = robot
    bstack1llll1111l_opy_ = len(bstack11lll11111_opy_.findall(bstack111111l_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨാ")))
    if bstack1llll1111l_opy_ == 1:
      bstack11lll11111_opy_.remove(bstack11lll11111_opy_.findall(bstack111111l_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩി"))[0])
      bstack11ll1ll1ll_opy_ = ET.Element(bstack111111l_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪീ"), attrib={bstack111111l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪു"): bstack111111l_opy_ (u"࠭ࡓࡶ࡫ࡷࡩࡸ࠭ൂ"), bstack111111l_opy_ (u"ࠧࡪࡦࠪൃ"): bstack111111l_opy_ (u"ࠨࡵ࠳ࠫൄ")})
      bstack11lll11111_opy_.insert(1, bstack11ll1ll1ll_opy_)
      bstack1l11lll1l1_opy_ = None
      for suite in bstack11lll11111_opy_.iter(bstack111111l_opy_ (u"ࠩࡶࡹ࡮ࡺࡥࠨ൅")):
        bstack1l11lll1l1_opy_ = suite
      bstack1l11lll1l1_opy_.append(bstack1ll11l1l1l_opy_)
      bstack111l11llll_opy_ = None
      for status in bstack1ll11l1l1l_opy_.iter(bstack111111l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪെ")):
        bstack111l11llll_opy_ = status
      bstack1l11lll1l1_opy_.append(bstack111l11llll_opy_)
    bstack1l1l1l1ll1_opy_.write(path)
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡴࡶ࡭ࡳ࡭ࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡰࡨࡶࡦࡺࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠩേ") + str(e))
def bstack1111l11l1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack11lll1111_opy_
  global CONFIG
  if bstack111111l_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡵࡧࡴࡩࠤൈ") in options:
    del options[bstack111111l_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࡶࡡࡵࡪࠥ൉")]
  json_data = bstack11l1ll1ll1_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack111111l_opy_ (u"ࠧࡱࡣࡥࡳࡹࡥࡲࡦࡵࡸࡰࡹࡹࠧൊ"), str(item_id), bstack111111l_opy_ (u"ࠨࡱࡸࡸࡵࡻࡴ࠯ࡺࡰࡰࠬോ"))
    bstack111llll1l1_opy_(path, bstack1ll1lllll_opy_(json_data[item_id]))
  bstack11ll1ll1l_opy_()
  return bstack11lll1111_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1111l1l1l1_opy_(self, ff_profile_dir):
  global bstack111ll111ll_opy_
  if not ff_profile_dir:
    return None
  return bstack111ll111ll_opy_(self, ff_profile_dir)
def bstack11111lll11_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1ll1l1l111_opy_
  bstack1l1llll111_opy_ = []
  if bstack111111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬൌ") in CONFIG:
    bstack1l1llll111_opy_ = CONFIG[bstack111111l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ്࠭")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack111111l_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࠧൎ")],
      pabot_args[bstack111111l_opy_ (u"ࠧࡼࡥࡳࡤࡲࡷࡪࠨ൏")],
      argfile,
      pabot_args.get(bstack111111l_opy_ (u"ࠨࡨࡪࡸࡨࠦ൐")),
      pabot_args[bstack111111l_opy_ (u"ࠢࡱࡴࡲࡧࡪࡹࡳࡦࡵࠥ൑")],
      platform[0],
      bstack1ll1l1l111_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack111111l_opy_ (u"ࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡩ࡭ࡱ࡫ࡳࠣ൒")] or [(bstack111111l_opy_ (u"ࠤࠥ൓"), None)]
    for platform in enumerate(bstack1l1llll111_opy_)
  ]
def bstack111l11l11l_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack11l1lll1l_opy_=bstack111111l_opy_ (u"ࠪࠫൔ")):
  global bstack1lll1111l1_opy_
  self.platform_index = platform_index
  self.bstack11ll111111_opy_ = bstack11l1lll1l_opy_
  bstack1lll1111l1_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1l1ll1111l_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1l11ll1l11_opy_
  global bstack1l1ll11ll_opy_
  bstack11111l1ll1_opy_ = copy.deepcopy(item)
  if not bstack111111l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ൕ") in item.options:
    bstack11111l1ll1_opy_.options[bstack111111l_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧൖ")] = []
  bstack1lll1l1ll1_opy_ = bstack11111l1ll1_opy_.options[bstack111111l_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨൗ")].copy()
  for v in bstack11111l1ll1_opy_.options[bstack111111l_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ൘")]:
    if bstack111111l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞ࠧ൙") in v:
      bstack1lll1l1ll1_opy_.remove(v)
    if bstack111111l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡅࡏࡍࡆࡘࡇࡔࠩ൚") in v:
      bstack1lll1l1ll1_opy_.remove(v)
    if bstack111111l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ൛") in v:
      bstack1lll1l1ll1_opy_.remove(v)
  bstack1lll1l1ll1_opy_.insert(0, bstack111111l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚࠽ࡿࢂ࠭൜").format(bstack11111l1ll1_opy_.platform_index))
  bstack1lll1l1ll1_opy_.insert(0, bstack111111l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡉࡋࡆࡍࡑࡆࡅࡑࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓ࠼ࡾࢁࠬ൝").format(bstack11111l1ll1_opy_.bstack11ll111111_opy_))
  bstack11111l1ll1_opy_.options[bstack111111l_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ൞")] = bstack1lll1l1ll1_opy_
  if bstack1l1ll11ll_opy_:
    bstack11111l1ll1_opy_.options[bstack111111l_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩൟ")].insert(0, bstack111111l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡄࡎࡌࡅࡗࡍࡓ࠻ࡽࢀࠫൠ").format(bstack1l1ll11ll_opy_))
  return bstack1l11ll1l11_opy_(caller_id, datasources, is_last, bstack11111l1ll1_opy_, outs_dir)
def bstack111l1l1lll_opy_(command, item_index):
  try:
    if bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪൡ")):
      os.environ[bstack111111l_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫൢ")] = json.dumps(CONFIG[bstack111111l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧൣ")][item_index % bstack11l1l1l111_opy_])
    global bstack1l1ll11ll_opy_
    if bstack1l1ll11ll_opy_:
      command[0] = command[0].replace(bstack111111l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ൤"), bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡹࡤ࡬ࠢࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠢࠪ൥") + str(
        item_index) + bstack111111l_opy_ (u"ࠧࠡࠩ൦") + bstack1l1ll11ll_opy_, 1)
    else:
      command[0] = command[0].replace(bstack111111l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ൧"),
                                      bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡵࡧ࡯ࠥࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱࠦ࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠥ࠭൨") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack111111l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡰࡳࡩ࡯ࡦࡺ࡫ࡱ࡫ࠥࡩ࡯࡮࡯ࡤࡲࡩࠦࡦࡰࡴࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࡀࠠࡼࡿࠪ൩").format(str(e)))
def bstack1l1ll1l1ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1l111lllll_opy_
  try:
    bstack111l1l1lll_opy_(command, item_index)
    return bstack1l111lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack111111l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯࠼ࠣࡿࢂ࠭൪").format(str(e)))
    raise e
def bstack1l111l1111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1l111lllll_opy_
  try:
    bstack111l1l1lll_opy_(command, item_index)
    return bstack1l111lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack111111l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰࠣ࠶࠳࠷࠳࠻ࠢࡾࢁࠬ൫").format(str(e)))
    try:
      return bstack1l111lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack111111l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠ࠳࠰࠴࠷ࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫ൬").format(str(e2)))
      raise e
def bstack11ll1l1l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1l111lllll_opy_
  try:
    bstack111l1l1lll_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack1l111lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack111111l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲࠥ࠸࠮࠲࠷࠽ࠤࢀࢃࠧ൭").format(str(e)))
    try:
      return bstack1l111lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack111111l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢ࠵࠲࠶࠻ࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࡿࢂ࠭൮").format(str(e2)))
      raise e
def _1111l11111_opy_(bstack11l11111ll_opy_, item_index, process_timeout, sleep_before_start, bstack11l1ll11l_opy_):
  bstack111l1l1lll_opy_(bstack11l11111ll_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack11l1l11111_opy_(command, bstack1ll11l1ll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1l111lllll_opy_
  try:
    bstack111l1l1lll_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack1l111lllll_opy_(command, bstack1ll11l1ll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack111111l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠶࠰࠳࠾ࠥࢁࡽࠨ൯").format(str(e)))
    try:
      return bstack1l111lllll_opy_(command, bstack1ll11l1ll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack111111l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪ൰").format(str(e2)))
      raise e
def bstack1l1l1111l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1l111lllll_opy_
  try:
    process_timeout = _1111l11111_opy_(command, item_index, process_timeout, sleep_before_start, bstack111111l_opy_ (u"ࠫ࠹࠴࠲ࠨ൱"))
    return bstack1l111lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack111111l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰࠣ࠸࠳࠸࠺ࠡࡽࢀࠫ൲").format(str(e)))
    try:
      return bstack1l111lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack111111l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࡿࢂ࠭൳").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack1l11l111ll_opy_(self, runner, quiet=False, capture=True):
  global bstack1l11lll111_opy_
  bstack11lll1lll1_opy_ = bstack1l11lll111_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack111111l_opy_ (u"ࠧࡦࡺࡦࡩࡵࡺࡩࡰࡰࡢࡥࡷࡸࠧ൴")):
      runner.exception_arr = []
    if not hasattr(runner, bstack111111l_opy_ (u"ࠨࡧࡻࡧࡤࡺࡲࡢࡥࡨࡦࡦࡩ࡫ࡠࡣࡵࡶࠬ൵")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack11lll1lll1_opy_
def bstack11l1lll1ll_opy_(runner, hook_name, context, element, bstack11l111ll1_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack11l1l11lll_opy_.bstack11ll11ll_opy_(hook_name, element)
    bstack11l111ll1_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack11l1l11lll_opy_.bstack11ll1111_opy_(element)
      if hook_name not in [bstack111111l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱ࠭൶"), bstack111111l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡤࡰࡱ࠭൷")] and args and hasattr(args[0], bstack111111l_opy_ (u"ࠫࡪࡸࡲࡰࡴࡢࡱࡪࡹࡳࡢࡩࡨࠫ൸")):
        args[0].error_message = bstack111111l_opy_ (u"ࠬ࠭൹")
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢ࡫ࡥࡳࡪ࡬ࡦࠢ࡫ࡳࡴࡱࡳࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨ࠾ࠥࢁࡽࠨൺ").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1111ll_opy_, stage=STAGE.bstack11l11ll11_opy_, hook_type=bstack111111l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫ࡁ࡭࡮ࠥൻ"), bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1111l1ll11_opy_(runner, name, context, bstack11l111ll1_opy_, *args):
    if runner.hooks.get(bstack111111l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧർ")).__name__ != bstack111111l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࡥࡤࡦࡨࡤࡹࡱࡺ࡟ࡩࡱࡲ࡯ࠧൽ"):
      bstack11l1lll1ll_opy_(runner, name, context, runner, bstack11l111ll1_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1l111lll1l_opy_(bstack111111l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩൾ")) else context.browser
      runner.driver_initialised = bstack111111l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣൿ")
    except Exception as e:
      logger.debug(bstack111111l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡪࡲࡪࡸࡨࡶࠥ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡦࠢࡤࡸࡹࡸࡩࡣࡷࡷࡩ࠿ࠦࡻࡾࠩ඀").format(str(e)))
def bstack1111111l1_opy_(runner, name, context, bstack11l111ll1_opy_, *args):
    bstack11l1lll1ll_opy_(runner, name, context, context.feature, bstack11l111ll1_opy_, *args)
    try:
      if not bstack111llll11l_opy_:
        bstack11l11l1lll_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111lll1l_opy_(bstack111111l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඁ")) else context.browser
        if is_driver_active(bstack11l11l1lll_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack111111l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣං")
          bstack1l11l1l11l_opy_ = str(runner.feature.name)
          bstack11l111l1l_opy_(context, bstack1l11l1l11l_opy_)
          bstack11l11l1lll_opy_.execute_script(bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭ඃ") + json.dumps(bstack1l11l1l11l_opy_) + bstack111111l_opy_ (u"ࠩࢀࢁࠬ඄"))
    except Exception as e:
      logger.debug(bstack111111l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪඅ").format(str(e)))
def bstack1lll1l1lll_opy_(runner, name, context, bstack11l111ll1_opy_, *args):
    if hasattr(context, bstack111111l_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ආ")):
        bstack11l1l11lll_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack111111l_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧඇ")) else context.feature
    bstack11l1lll1ll_opy_(runner, name, context, target, bstack11l111ll1_opy_, *args)
@measure(event_name=EVENTS.bstack1ll11ll11_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack11l1lllll_opy_(runner, name, context, bstack11l111ll1_opy_, *args):
    if len(context.scenario.tags) == 0: bstack11l1l11lll_opy_.start_test(context)
    bstack11l1lll1ll_opy_(runner, name, context, context.scenario, bstack11l111ll1_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1l1111l1l_opy_.bstack11111ll11_opy_(context, *args)
    try:
      bstack11l11l1lll_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඈ"), context.browser)
      if is_driver_active(bstack11l11l1lll_opy_):
        bstack1ll1l111_opy_.bstack1lll1l11l1_opy_(bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ඉ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack111111l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥඊ")
        if (not bstack111llll11l_opy_):
          scenario_name = args[0].name
          feature_name = bstack1l11l1l11l_opy_ = str(runner.feature.name)
          bstack1l11l1l11l_opy_ = feature_name + bstack111111l_opy_ (u"ࠩࠣ࠱ࠥ࠭උ") + scenario_name
          if runner.driver_initialised == bstack111111l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧඌ"):
            bstack11l111l1l_opy_(context, bstack1l11l1l11l_opy_)
            bstack11l11l1lll_opy_.execute_script(bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩඍ") + json.dumps(bstack1l11l1l11l_opy_) + bstack111111l_opy_ (u"ࠬࢃࡽࠨඎ"))
    except Exception as e:
      logger.debug(bstack111111l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱ࠽ࠤࢀࢃࠧඏ").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1111ll_opy_, stage=STAGE.bstack11l11ll11_opy_, hook_type=bstack111111l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫ࡓࡵࡧࡳࠦඐ"), bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack11lllll111_opy_(runner, name, context, bstack11l111ll1_opy_, *args):
    bstack11l1lll1ll_opy_(runner, name, context, args[0], bstack11l111ll1_opy_, *args)
    try:
      bstack11l11l1lll_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111lll1l_opy_(bstack111111l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧඑ")) else context.browser
      if is_driver_active(bstack11l11l1lll_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack111111l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢඒ")
        bstack11l1l11lll_opy_.bstack11ll1l1l_opy_(args[0])
        if runner.driver_initialised == bstack111111l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣඓ"):
          feature_name = bstack1l11l1l11l_opy_ = str(runner.feature.name)
          bstack1l11l1l11l_opy_ = feature_name + bstack111111l_opy_ (u"ࠫࠥ࠳ࠠࠨඔ") + context.scenario.name
          bstack11l11l1lll_opy_.execute_script(bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪඕ") + json.dumps(bstack1l11l1l11l_opy_) + bstack111111l_opy_ (u"࠭ࡽࡾࠩඖ"))
    except Exception as e:
      logger.debug(bstack111111l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡸࡪࡶ࠺ࠡࡽࢀࠫ඗").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1111ll_opy_, stage=STAGE.bstack11l11ll11_opy_, hook_type=bstack111111l_opy_ (u"ࠣࡣࡩࡸࡪࡸࡓࡵࡧࡳࠦ඘"), bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1ll1l11ll_opy_(runner, name, context, bstack11l111ll1_opy_, *args):
  bstack11l1l11lll_opy_.bstack11ll1ll1_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack11l11l1lll_opy_ = threading.current_thread().bstackSessionDriver if bstack111111l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ඙") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack11l11l1lll_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack111111l_opy_ (u"ࠪ࡭ࡳࡹࡴࡦࡲࠪක")
        feature_name = bstack1l11l1l11l_opy_ = str(runner.feature.name)
        bstack1l11l1l11l_opy_ = feature_name + bstack111111l_opy_ (u"ࠫࠥ࠳ࠠࠨඛ") + context.scenario.name
        bstack11l11l1lll_opy_.execute_script(bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪග") + json.dumps(bstack1l11l1l11l_opy_) + bstack111111l_opy_ (u"࠭ࡽࡾࠩඝ"))
    if str(step_status).lower() == bstack111111l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧඞ"):
      bstack1l1l11l1l_opy_ = bstack111111l_opy_ (u"ࠨࠩඟ")
      bstack1ll111l11l_opy_ = bstack111111l_opy_ (u"ࠩࠪච")
      bstack1llll11l11_opy_ = bstack111111l_opy_ (u"ࠪࠫඡ")
      try:
        import traceback
        bstack1l1l11l1l_opy_ = runner.exception.__class__.__name__
        bstack11l1ll1l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1ll111l11l_opy_ = bstack111111l_opy_ (u"ࠫࠥ࠭ජ").join(bstack11l1ll1l_opy_)
        bstack1llll11l11_opy_ = bstack11l1ll1l_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l11llll1l_opy_.format(str(e)))
      bstack1l1l11l1l_opy_ += bstack1llll11l11_opy_
      bstack11l1l1ll1l_opy_(context, json.dumps(str(args[0].name) + bstack111111l_opy_ (u"ࠧࠦ࠭ࠡࡈࡤ࡭ࡱ࡫ࡤࠢ࡞ࡱࠦඣ") + str(bstack1ll111l11l_opy_)),
                          bstack111111l_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧඤ"))
      if runner.driver_initialised == bstack111111l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧඥ"):
        bstack111ll1lll_opy_(getattr(context, bstack111111l_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ඦ"), None), bstack111111l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤට"), bstack1l1l11l1l_opy_)
        bstack11l11l1lll_opy_.execute_script(bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨඨ") + json.dumps(str(args[0].name) + bstack111111l_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥඩ") + str(bstack1ll111l11l_opy_)) + bstack111111l_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤࢀࢁࠬඪ"))
      if runner.driver_initialised == bstack111111l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦණ"):
        bstack1ll111l1ll_opy_(bstack11l11l1lll_opy_, bstack111111l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧඬ"), bstack111111l_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧත") + str(bstack1l1l11l1l_opy_))
    else:
      bstack11l1l1ll1l_opy_(context, bstack111111l_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥථ"), bstack111111l_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣද"))
      if runner.driver_initialised == bstack111111l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤධ"):
        bstack111ll1lll_opy_(getattr(context, bstack111111l_opy_ (u"ࠬࡶࡡࡨࡧࠪන"), None), bstack111111l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ඲"))
      bstack11l11l1lll_opy_.execute_script(bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬඳ") + json.dumps(str(args[0].name) + bstack111111l_opy_ (u"ࠣࠢ࠰ࠤࡕࡧࡳࡴࡧࡧࠥࠧප")) + bstack111111l_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧࢃࡽࠨඵ"))
      if runner.driver_initialised == bstack111111l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣබ"):
        bstack1ll111l1ll_opy_(bstack11l11l1lll_opy_, bstack111111l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦභ"))
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡪࡰࠣࡥ࡫ࡺࡥࡳࠢࡶࡸࡪࡶ࠺ࠡࡽࢀࠫම").format(str(e)))
  bstack11l1lll1ll_opy_(runner, name, context, args[0], bstack11l111ll1_opy_, *args)
@measure(event_name=EVENTS.bstack1lll11ll1_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1l111lll1_opy_(runner, name, context, bstack11l111ll1_opy_, *args):
  bstack11l1l11lll_opy_.end_test(args[0])
  try:
    bstack1l111l1lll_opy_ = args[0].status.name
    bstack11l11l1lll_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඹ"), context.browser)
    bstack1l1111l1l_opy_.bstack1l11l111l_opy_(bstack11l11l1lll_opy_)
    if str(bstack1l111l1lll_opy_).lower() == bstack111111l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧය"):
      bstack1l1l11l1l_opy_ = bstack111111l_opy_ (u"ࠨࠩර")
      bstack1ll111l11l_opy_ = bstack111111l_opy_ (u"ࠩࠪ඼")
      bstack1llll11l11_opy_ = bstack111111l_opy_ (u"ࠪࠫල")
      try:
        import traceback
        bstack1l1l11l1l_opy_ = runner.exception.__class__.__name__
        bstack11l1ll1l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1ll111l11l_opy_ = bstack111111l_opy_ (u"ࠫࠥ࠭඾").join(bstack11l1ll1l_opy_)
        bstack1llll11l11_opy_ = bstack11l1ll1l_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l11llll1l_opy_.format(str(e)))
      bstack1l1l11l1l_opy_ += bstack1llll11l11_opy_
      bstack11l1l1ll1l_opy_(context, json.dumps(str(args[0].name) + bstack111111l_opy_ (u"ࠧࠦ࠭ࠡࡈࡤ࡭ࡱ࡫ࡤࠢ࡞ࡱࠦ඿") + str(bstack1ll111l11l_opy_)),
                          bstack111111l_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧව"))
      if runner.driver_initialised == bstack111111l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤශ") or runner.driver_initialised == bstack111111l_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨෂ"):
        bstack111ll1lll_opy_(getattr(context, bstack111111l_opy_ (u"ࠩࡳࡥ࡬࡫ࠧස"), None), bstack111111l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥහ"), bstack1l1l11l1l_opy_)
        bstack11l11l1lll_opy_.execute_script(bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩළ") + json.dumps(str(args[0].name) + bstack111111l_opy_ (u"ࠧࠦ࠭ࠡࡈࡤ࡭ࡱ࡫ࡤࠢ࡞ࡱࠦෆ") + str(bstack1ll111l11l_opy_)) + bstack111111l_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭෇"))
      if runner.driver_initialised == bstack111111l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤ෈") or runner.driver_initialised == bstack111111l_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨ෉"):
        bstack1ll111l1ll_opy_(bstack11l11l1lll_opy_, bstack111111l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥ්ࠩ"), bstack111111l_opy_ (u"ࠥࡗࡨ࡫࡮ࡢࡴ࡬ࡳࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢ෋") + str(bstack1l1l11l1l_opy_))
    else:
      bstack11l1l1ll1l_opy_(context, bstack111111l_opy_ (u"ࠦࡕࡧࡳࡴࡧࡧࠥࠧ෌"), bstack111111l_opy_ (u"ࠧ࡯࡮ࡧࡱࠥ෍"))
      if runner.driver_initialised == bstack111111l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣ෎") or runner.driver_initialised == bstack111111l_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧා"):
        bstack111ll1lll_opy_(getattr(context, bstack111111l_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ැ"), None), bstack111111l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤෑ"))
      bstack11l11l1lll_opy_.execute_script(bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨි") + json.dumps(str(args[0].name) + bstack111111l_opy_ (u"ࠦࠥ࠳ࠠࡑࡣࡶࡷࡪࡪࠡࠣී")) + bstack111111l_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫු"))
      if runner.driver_initialised == bstack111111l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣ෕") or runner.driver_initialised == bstack111111l_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧූ"):
        bstack1ll111l1ll_opy_(bstack11l11l1lll_opy_, bstack111111l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ෗"))
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫෘ").format(str(e)))
  bstack11l1lll1ll_opy_(runner, name, context, context.scenario, bstack11l111ll1_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack111l1l111_opy_(runner, name, context, bstack11l111ll1_opy_, *args):
    target = context.scenario if hasattr(context, bstack111111l_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬෙ")) else context.feature
    bstack11l1lll1ll_opy_(runner, name, context, target, bstack11l111ll1_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack11ll11ll11_opy_(runner, name, context, bstack11l111ll1_opy_, *args):
    try:
      bstack11l11l1lll_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪේ"), context.browser)
      bstack111l1ll1ll_opy_ = bstack111111l_opy_ (u"ࠬ࠭ෛ")
      if context.failed is True:
        bstack1111l1ll1_opy_ = []
        bstack1llll1l111_opy_ = []
        bstack1l1l11l111_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1111l1ll1_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l1ll1l_opy_ = traceback.format_tb(exc_tb)
            bstack1l1llllll_opy_ = bstack111111l_opy_ (u"࠭ࠠࠨො").join(bstack11l1ll1l_opy_)
            bstack1llll1l111_opy_.append(bstack1l1llllll_opy_)
            bstack1l1l11l111_opy_.append(bstack11l1ll1l_opy_[-1])
        except Exception as e:
          logger.debug(bstack1l11llll1l_opy_.format(str(e)))
        bstack1l1l11l1l_opy_ = bstack111111l_opy_ (u"ࠧࠨෝ")
        for i in range(len(bstack1111l1ll1_opy_)):
          bstack1l1l11l1l_opy_ += bstack1111l1ll1_opy_[i] + bstack1l1l11l111_opy_[i] + bstack111111l_opy_ (u"ࠨ࡞ࡱࠫෞ")
        bstack111l1ll1ll_opy_ = bstack111111l_opy_ (u"ࠩࠣࠫෟ").join(bstack1llll1l111_opy_)
        if runner.driver_initialised in [bstack111111l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦ෠"), bstack111111l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣ෡")]:
          bstack11l1l1ll1l_opy_(context, bstack111l1ll1ll_opy_, bstack111111l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦ෢"))
          bstack111ll1lll_opy_(getattr(context, bstack111111l_opy_ (u"࠭ࡰࡢࡩࡨࠫ෣"), None), bstack111111l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ෤"), bstack1l1l11l1l_opy_)
          bstack11l11l1lll_opy_.execute_script(bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭෥") + json.dumps(bstack111l1ll1ll_opy_) + bstack111111l_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࡽࡾࠩ෦"))
          bstack1ll111l1ll_opy_(bstack11l11l1lll_opy_, bstack111111l_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥ෧"), bstack111111l_opy_ (u"ࠦࡘࡵ࡭ࡦࠢࡶࡧࡪࡴࡡࡳ࡫ࡲࡷࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦ࡜࡯ࠤ෨") + str(bstack1l1l11l1l_opy_))
          bstack11l11lllll_opy_ = bstack1ll1l1ll1l_opy_(bstack111l1ll1ll_opy_, runner.feature.name, logger)
          if (bstack11l11lllll_opy_ != None):
            bstack1ll111llll_opy_.append(bstack11l11lllll_opy_)
      else:
        if runner.driver_initialised in [bstack111111l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨ෩"), bstack111111l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥ෪")]:
          bstack11l1l1ll1l_opy_(context, bstack111111l_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥ࠻ࠢࠥ෫") + str(runner.feature.name) + bstack111111l_opy_ (u"ࠣࠢࡳࡥࡸࡹࡥࡥࠣࠥ෬"), bstack111111l_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢ෭"))
          bstack111ll1lll_opy_(getattr(context, bstack111111l_opy_ (u"ࠪࡴࡦ࡭ࡥࠨ෮"), None), bstack111111l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦ෯"))
          bstack11l11l1lll_opy_.execute_script(bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ෰") + json.dumps(bstack111111l_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫࠺ࠡࠤ෱") + str(runner.feature.name) + bstack111111l_opy_ (u"ࠢࠡࡲࡤࡷࡸ࡫ࡤࠢࠤෲ")) + bstack111111l_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦࢂࢃࠧෳ"))
          bstack1ll111l1ll_opy_(bstack11l11l1lll_opy_, bstack111111l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ෴"))
          bstack11l11lllll_opy_ = bstack1ll1l1ll1l_opy_(bstack111l1ll1ll_opy_, runner.feature.name, logger)
          if (bstack11l11lllll_opy_ != None):
            bstack1ll111llll_opy_.append(bstack11l11lllll_opy_)
    except Exception as e:
      logger.debug(bstack111111l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡧࡧࡤࡸࡺࡸࡥ࠻ࠢࡾࢁࠬ෵").format(str(e)))
    bstack11l1lll1ll_opy_(runner, name, context, context.feature, bstack11l111ll1_opy_, *args)
@measure(event_name=EVENTS.bstack1ll1111ll_opy_, stage=STAGE.bstack11l11ll11_opy_, hook_type=bstack111111l_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࡄࡰࡱࠨ෶"), bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1l11l1ll11_opy_(runner, name, context, bstack11l111ll1_opy_, *args):
    bstack11l1lll1ll_opy_(runner, name, context, runner, bstack11l111ll1_opy_, *args)
def bstack11l11lll1_opy_(self, name, context, *args):
  try:
    if bstack1l11l11lll_opy_:
      platform_index = int(threading.current_thread()._name) % bstack11l1l1l111_opy_
      bstack11l1l1l11_opy_ = CONFIG[bstack111111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ෷")][platform_index]
      os.environ[bstack111111l_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧ෸")] = json.dumps(bstack11l1l1l11_opy_)
    global bstack11l111ll1_opy_
    if not hasattr(self, bstack111111l_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸ࡟ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡨࡨࠬ෹")):
      self.driver_initialised = None
    bstack11l1l11l11_opy_ = {
        bstack111111l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠬ෺"): bstack1111l1ll11_opy_,
        bstack111111l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠪ෻"): bstack1111111l1_opy_,
        bstack111111l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡸࡦ࡭ࠧ෼"): bstack1lll1l1lll_opy_,
        bstack111111l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭෽"): bstack11l1lllll_opy_,
        bstack111111l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠪ෾"): bstack11lllll111_opy_,
        bstack111111l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡴࡦࡲࠪ෿"): bstack1ll1l11ll_opy_,
        bstack111111l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ฀"): bstack1l111lll1_opy_,
        bstack111111l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡵࡣࡪࠫก"): bstack111l1l111_opy_,
        bstack111111l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩข"): bstack11ll11ll11_opy_,
        bstack111111l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡤࡰࡱ࠭ฃ"): bstack1l11l1ll11_opy_
    }
    handler = bstack11l1l11l11_opy_.get(name, bstack11l111ll1_opy_)
    try:
      handler(self, name, context, bstack11l111ll1_opy_, *args)
    except Exception as e:
      logger.debug(bstack111111l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࠦࡨࡰࡱ࡮ࠤ࡭ࡧ࡮ࡥ࡮ࡨࡶࠥࢁࡽ࠻ࠢࡾࢁࠬค").format(name, str(e)))
    if name in [bstack111111l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠬฅ"), bstack111111l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧฆ"), bstack111111l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪง")]:
      try:
        bstack11l11l1lll_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111lll1l_opy_(bstack111111l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧจ")) else context.browser
        bstack1ll1ll111_opy_ = (
          (name == bstack111111l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡣ࡯ࡰࠬฉ") and self.driver_initialised == bstack111111l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢช")) or
          (name == bstack111111l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡪࡪࡧࡴࡶࡴࡨࠫซ") and self.driver_initialised == bstack111111l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨฌ")) or
          (name == bstack111111l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧญ") and self.driver_initialised in [bstack111111l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤฎ"), bstack111111l_opy_ (u"ࠣ࡫ࡱࡷࡹ࡫ࡰࠣฏ")]) or
          (name == bstack111111l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡷࡩࡵ࠭ฐ") and self.driver_initialised == bstack111111l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣฑ"))
        )
        if bstack1ll1ll111_opy_:
          self.driver_initialised = None
          if bstack11l11l1lll_opy_ and hasattr(bstack11l11l1lll_opy_, bstack111111l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠨฒ")):
            try:
              bstack11l11l1lll_opy_.quit()
            except Exception as e:
              logger.debug(bstack111111l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡶࡻࡩࡵࡶ࡬ࡲ࡬ࠦࡤࡳ࡫ࡹࡩࡷࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦࠢ࡫ࡳࡴࡱ࠺ࠡࡽࢀࠫณ").format(str(e)))
      except Exception as e:
        logger.debug(bstack111111l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡩࡱࡲ࡯ࠥࡩ࡬ࡦࡣࡱࡹࡵࠦࡦࡰࡴࠣࡿࢂࡀࠠࡼࡿࠪด").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠧࡄࡴ࡬ࡸ࡮ࡩࡡ࡭ࠢࡨࡶࡷࡵࡲࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨࠤࡷࡻ࡮ࠡࡪࡲࡳࡰࠦࡻࡾ࠼ࠣࡿࢂ࠭ต").format(name, str(e)))
    try:
      bstack11l111ll1_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack111111l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯ࠥࡵࡲࡪࡩ࡬ࡲࡦࡲࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡩࡱࡲ࡯ࠥࢁࡽ࠻ࠢࡾࢁࠬถ").format(name, str(e2)))
def bstack111l1llll_opy_(config, startdir):
  return bstack111111l_opy_ (u"ࠤࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿ࠵ࢃࠢท").format(bstack111111l_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤธ"))
notset = Notset()
def bstack111l1lll1_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1ll1lll1l1_opy_
  if str(name).lower() == bstack111111l_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࠫน"):
    return bstack111111l_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦบ")
  else:
    return bstack1ll1lll1l1_opy_(self, name, default, skip)
def bstack1l1ll111ll_opy_(item, when):
  global bstack1l11l1l11_opy_
  try:
    bstack1l11l1l11_opy_(item, when)
  except Exception as e:
    pass
def bstack11llll1lll_opy_():
  return
def bstack111lllllll_opy_(type, name, status, reason, bstack1ll111lll1_opy_, bstack1l1l1lll1_opy_):
  bstack111ll1l11l_opy_ = {
    bstack111111l_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭ป"): type,
    bstack111111l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪผ"): {}
  }
  if type == bstack111111l_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪฝ"):
    bstack111ll1l11l_opy_[bstack111111l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬพ")][bstack111111l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩฟ")] = bstack1ll111lll1_opy_
    bstack111ll1l11l_opy_[bstack111111l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧภ")][bstack111111l_opy_ (u"ࠬࡪࡡࡵࡣࠪม")] = json.dumps(str(bstack1l1l1lll1_opy_))
  if type == bstack111111l_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧย"):
    bstack111ll1l11l_opy_[bstack111111l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪร")][bstack111111l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ฤ")] = name
  if type == bstack111111l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬล"):
    bstack111ll1l11l_opy_[bstack111111l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ฦ")][bstack111111l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫว")] = status
    if status == bstack111111l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬศ"):
      bstack111ll1l11l_opy_[bstack111111l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩษ")][bstack111111l_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧส")] = json.dumps(str(reason))
  bstack11l1ll1111_opy_ = bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ห").format(json.dumps(bstack111ll1l11l_opy_))
  return bstack11l1ll1111_opy_
def bstack1ll11111ll_opy_(driver_command, response):
    if driver_command == bstack111111l_opy_ (u"ࠩࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࠭ฬ"):
        bstack1ll1l111_opy_.bstack1l11ll111l_opy_({
            bstack111111l_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩอ"): response[bstack111111l_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪฮ")],
            bstack111111l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬฯ"): bstack1ll1l111_opy_.current_test_uuid()
        })
def bstack11l11111l1_opy_(item, call, rep):
  global bstack1llll1llll_opy_
  global bstack1111l11l1l_opy_
  global bstack111llll11l_opy_
  name = bstack111111l_opy_ (u"࠭ࠧะ")
  try:
    if rep.when == bstack111111l_opy_ (u"ࠧࡤࡣ࡯ࡰࠬั"):
      bstack1l1ll11lll_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack111llll11l_opy_:
          name = str(rep.nodeid)
          bstack11ll111lll_opy_ = bstack111lllllll_opy_(bstack111111l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩา"), name, bstack111111l_opy_ (u"ࠩࠪำ"), bstack111111l_opy_ (u"ࠪࠫิ"), bstack111111l_opy_ (u"ࠫࠬี"), bstack111111l_opy_ (u"ࠬ࠭ึ"))
          threading.current_thread().bstack111l11l1l1_opy_ = name
          for driver in bstack1111l11l1l_opy_:
            if bstack1l1ll11lll_opy_ == driver.session_id:
              driver.execute_script(bstack11ll111lll_opy_)
      except Exception as e:
        logger.debug(bstack111111l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭ื").format(str(e)))
      try:
        bstack111l1111l1_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack111111l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨุ"):
          status = bstack111111l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨู") if rep.outcome.lower() == bstack111111l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥฺࠩ") else bstack111111l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ฻")
          reason = bstack111111l_opy_ (u"ࠫࠬ฼")
          if status == bstack111111l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ฽"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack111111l_opy_ (u"࠭ࡩ࡯ࡨࡲࠫ฾") if status == bstack111111l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ฿") else bstack111111l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧเ")
          data = name + bstack111111l_opy_ (u"ࠩࠣࡴࡦࡹࡳࡦࡦࠤࠫแ") if status == bstack111111l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪโ") else name + bstack111111l_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠦࠦࠧใ") + reason
          bstack1111lll1ll_opy_ = bstack111lllllll_opy_(bstack111111l_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧไ"), bstack111111l_opy_ (u"࠭ࠧๅ"), bstack111111l_opy_ (u"ࠧࠨๆ"), bstack111111l_opy_ (u"ࠨࠩ็"), level, data)
          for driver in bstack1111l11l1l_opy_:
            if bstack1l1ll11lll_opy_ == driver.session_id:
              driver.execute_script(bstack1111lll1ll_opy_)
      except Exception as e:
        logger.debug(bstack111111l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡣࡰࡰࡷࡩࡽࡺࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ่࠭").format(str(e)))
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡵࡣࡷࡩࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࢀࢃ้ࠧ").format(str(e)))
  bstack1llll1llll_opy_(item, call, rep)
def bstack1l1ll11l1_opy_(driver, bstack11llllll11_opy_, test=None):
  global bstack111lll111_opy_
  if test != None:
    bstack1l1l1ll1l_opy_ = getattr(test, bstack111111l_opy_ (u"ࠫࡳࡧ࡭ࡦ๊ࠩ"), None)
    bstack11ll11lll_opy_ = getattr(test, bstack111111l_opy_ (u"ࠬࡻࡵࡪࡦ๋ࠪ"), None)
    PercySDK.screenshot(driver, bstack11llllll11_opy_, bstack1l1l1ll1l_opy_=bstack1l1l1ll1l_opy_, bstack11ll11lll_opy_=bstack11ll11lll_opy_, bstack11llllll1l_opy_=bstack111lll111_opy_)
  else:
    PercySDK.screenshot(driver, bstack11llllll11_opy_)
@measure(event_name=EVENTS.bstack111ll1111l_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack111l111l11_opy_(driver):
  if bstack11l11l111l_opy_.bstack1111ll1l1l_opy_() is True or bstack11l11l111l_opy_.capturing() is True:
    return
  bstack11l11l111l_opy_.bstack1l1lllllll_opy_()
  while not bstack11l11l111l_opy_.bstack1111ll1l1l_opy_():
    bstack111lll1ll_opy_ = bstack11l11l111l_opy_.bstack1lllll1l11_opy_()
    bstack1l1ll11l1_opy_(driver, bstack111lll1ll_opy_)
  bstack11l11l111l_opy_.bstack1111lll111_opy_()
def bstack11l1l1l1l_opy_(sequence, driver_command, response = None, bstack1l11111l11_opy_ = None, args = None):
    try:
      if sequence != bstack111111l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪ࠭์"):
        return
      if percy.bstack1111l1111_opy_() == bstack111111l_opy_ (u"ࠢࡧࡣ࡯ࡷࡪࠨํ"):
        return
      bstack111lll1ll_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠨࡲࡨࡶࡨࡿࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ๎"), None)
      for command in bstack1l1l1l1lll_opy_:
        if command == driver_command:
          with bstack11l111l111_opy_:
            bstack1l1llll1l_opy_ = bstack1111l11l1l_opy_.copy()
          for driver in bstack1l1llll1l_opy_:
            bstack111l111l11_opy_(driver)
      bstack1lll11l11l_opy_ = percy.bstack111lll1l11_opy_()
      if driver_command in bstack11ll1lllll_opy_[bstack1lll11l11l_opy_]:
        bstack11l11l111l_opy_.bstack1l1llll1l1_opy_(bstack111lll1ll_opy_, driver_command)
    except Exception as e:
      pass
def bstack1lll11l111_opy_(framework_name):
  if bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭๏")):
      return
  bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪࠧ๐"), True)
  global bstack1l111111l_opy_
  global bstack111l111lll_opy_
  global bstack1lll1ll111_opy_
  bstack1l111111l_opy_ = framework_name
  logger.info(bstack11ll11l1ll_opy_.format(bstack1l111111l_opy_.split(bstack111111l_opy_ (u"ࠫ࠲࠭๑"))[0]))
  bstack11llll1ll1_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1l11l11lll_opy_:
      Service.start = bstack1l1111l111_opy_
      Service.stop = bstack11111l1l1_opy_
      webdriver.Remote.get = bstack11l1ll1lll_opy_
      WebDriver.quit = bstack1l111ll111_opy_
      webdriver.Remote.__init__ = bstack1l1ll1ll1l_opy_
    if not bstack1l11l11lll_opy_:
        webdriver.Remote.__init__ = bstack1l1l1ll111_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack11l1l1l11l_opy_
    bstack111l111lll_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1l11l11lll_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack111111lll_opy_
  except Exception as e:
    pass
  bstack1l11l1l1ll_opy_()
  if not bstack111l111lll_opy_:
    bstack1l11l1lll1_opy_(bstack111111l_opy_ (u"ࠧࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡳࡵࡣ࡯ࡰࡪࡪࠢ๒"), bstack111ll1llll_opy_)
  if bstack111l1111l_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack111111l_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ๓")) and callable(getattr(RemoteConnection, bstack111111l_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ๔"))):
        RemoteConnection._get_proxy_url = bstack1l11lllll1_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack1l11lllll1_opy_
    except Exception as e:
      logger.error(bstack1l1ll1l1l_opy_.format(str(e)))
  if bstack111l11ll1_opy_():
    bstack1ll1ll1ll1_opy_(CONFIG, logger)
  if (bstack111111l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ๕") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1111l1111_opy_() == bstack111111l_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ๖"):
          bstack1l11ll1l1_opy_(bstack11l1l1l1l_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1111l1l1l1_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l11lllll_opy_
      except Exception as e:
        logger.warn(bstack1llll1ll1l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack111l11ll11_opy_
      except Exception as e:
        logger.debug(bstack1ll1111l1_opy_ + str(e))
    except Exception as e:
      bstack1l11l1lll1_opy_(e, bstack1llll1ll1l_opy_)
    Output.start_test = bstack11lll1l11l_opy_
    Output.end_test = bstack1ll1lll111_opy_
    TestStatus.__init__ = bstack1l11ll1ll1_opy_
    QueueItem.__init__ = bstack111l11l11l_opy_
    pabot._create_items = bstack11111lll11_opy_
    try:
      from pabot import __version__ as bstack1l1l1ll1l1_opy_
      if version.parse(bstack1l1l1ll1l1_opy_) >= version.parse(bstack111111l_opy_ (u"ࠪ࠹࠳࠶࠮࠱ࠩ๗")):
        pabot._run = bstack11l1l11111_opy_
      elif version.parse(bstack1l1l1ll1l1_opy_) >= version.parse(bstack111111l_opy_ (u"ࠫ࠹࠴࠲࠯࠲ࠪ๘")):
        pabot._run = bstack1l1l1111l1_opy_
      elif version.parse(bstack1l1l1ll1l1_opy_) >= version.parse(bstack111111l_opy_ (u"ࠬ࠸࠮࠲࠷࠱࠴ࠬ๙")):
        pabot._run = bstack11ll1l1l1l_opy_
      elif version.parse(bstack1l1l1ll1l1_opy_) >= version.parse(bstack111111l_opy_ (u"࠭࠲࠯࠳࠶࠲࠵࠭๚")):
        pabot._run = bstack1l111l1111_opy_
      else:
        pabot._run = bstack1l1ll1l1ll_opy_
    except Exception as e:
      pabot._run = bstack1l1ll1l1ll_opy_
    pabot._create_command_for_execution = bstack1l1ll1111l_opy_
    pabot._report_results = bstack1111l11l1_opy_
  if bstack111111l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ๛") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l11l1lll1_opy_(e, bstack1l1l1l1l1l_opy_)
    Runner.run_hook = bstack11l11lll1_opy_
    Step.run = bstack1l11l111ll_opy_
  if bstack111111l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ๜") in str(framework_name).lower():
    if not bstack1l11l11lll_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack111l1llll_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack11llll1lll_opy_
      Config.getoption = bstack111l1lll1_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack11l11111l1_opy_
    except Exception as e:
      pass
def bstack1l1l1l11ll_opy_():
  global CONFIG
  if bstack111111l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ๝") in CONFIG and int(CONFIG[bstack111111l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ๞")]) > 1:
    logger.warn(bstack1lllll1lll_opy_)
def bstack1l1lll111l_opy_(arg, bstack111ll1ll_opy_, bstack1lll1lll11_opy_=None):
  global CONFIG
  global bstack1lll1ll1ll_opy_
  global bstack1ll11lll11_opy_
  global bstack1l11l11lll_opy_
  global bstack11111lll_opy_
  bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ๟")
  if bstack111ll1ll_opy_ and isinstance(bstack111ll1ll_opy_, str):
    bstack111ll1ll_opy_ = eval(bstack111ll1ll_opy_)
  CONFIG = bstack111ll1ll_opy_[bstack111111l_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ๠")]
  bstack1lll1ll1ll_opy_ = bstack111ll1ll_opy_[bstack111111l_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ๡")]
  bstack1ll11lll11_opy_ = bstack111ll1ll_opy_[bstack111111l_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ๢")]
  bstack1l11l11lll_opy_ = bstack111ll1ll_opy_[bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ๣")]
  bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ๤"), bstack1l11l11lll_opy_)
  os.environ[bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ๥")] = bstack1l1l111l1_opy_
  os.environ[bstack111111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࠪ๦")] = json.dumps(CONFIG)
  os.environ[bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡍ࡛ࡂࡠࡗࡕࡐࠬ๧")] = bstack1lll1ll1ll_opy_
  os.environ[bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ๨")] = str(bstack1ll11lll11_opy_)
  os.environ[bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡍࡗࡊࡍࡓ࠭๩")] = str(True)
  if bstack1l1lll1111_opy_(arg, [bstack111111l_opy_ (u"ࠨ࠯ࡱࠫ๪"), bstack111111l_opy_ (u"ࠩ࠰࠱ࡳࡻ࡭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ๫")]) != -1:
    os.environ[bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡅࡗࡇࡌࡍࡇࡏࠫ๬")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack11ll1l1111_opy_)
    return
  bstack11l1llll1_opy_()
  global bstack1l1llll1ll_opy_
  global bstack111lll111_opy_
  global bstack1ll1l1l111_opy_
  global bstack1l1ll11ll_opy_
  global bstack111lll11l_opy_
  global bstack1lll1ll111_opy_
  global bstack11111llll1_opy_
  arg.append(bstack111111l_opy_ (u"ࠦ࠲࡝ࠢ๭"))
  arg.append(bstack111111l_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩ࠿ࡓ࡯ࡥࡷ࡯ࡩࠥࡧ࡬ࡳࡧࡤࡨࡾࠦࡩ࡮ࡲࡲࡶࡹ࡫ࡤ࠻ࡲࡼࡸࡪࡹࡴ࠯ࡒࡼࡸࡪࡹࡴࡘࡣࡵࡲ࡮ࡴࡧࠣ๮"))
  arg.append(bstack111111l_opy_ (u"ࠨ࠭ࡘࠤ๯"))
  arg.append(bstack111111l_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫࠺ࡕࡪࡨࠤ࡭ࡵ࡯࡬࡫ࡰࡴࡱࠨ๰"))
  global bstack1ll1111lll_opy_
  global bstack1lll1111ll_opy_
  global bstack1l1ll1lll_opy_
  global bstack1llllll11l_opy_
  global bstack111ll111ll_opy_
  global bstack1lll1111l1_opy_
  global bstack1l11ll1l11_opy_
  global bstack11l1l111ll_opy_
  global bstack11l111111l_opy_
  global bstack1lll11l11_opy_
  global bstack1ll1lll1l1_opy_
  global bstack1l11l1l11_opy_
  global bstack1llll1llll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll1111lll_opy_ = webdriver.Remote.__init__
    bstack1lll1111ll_opy_ = WebDriver.quit
    bstack11l1l111ll_opy_ = WebDriver.close
    bstack11l111111l_opy_ = WebDriver.get
    bstack1l1ll1lll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1l1111ll1l_opy_(CONFIG) and bstack11ll1l1lll_opy_():
    if bstack1ll1llllll_opy_() < version.parse(bstack1l1ll1ll11_opy_):
      logger.error(bstack1l1111lll_opy_.format(bstack1ll1llllll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack111111l_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ๱")) and callable(getattr(RemoteConnection, bstack111111l_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ๲"))):
          bstack1lll11l11_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1lll11l11_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack1l1ll1l1l_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1ll1lll1l1_opy_ = Config.getoption
    from _pytest import runner
    bstack1l11l1l11_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack11111111_opy_)
  try:
    from pytest_bdd import reporting
    bstack1llll1llll_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack111111l_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫ๳"))
  bstack1ll1l1l111_opy_ = CONFIG.get(bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ๴"), {}).get(bstack111111l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ๵"))
  bstack11111llll1_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack1111lllll_opy_():
      bstack111ll111l1_opy_.invoke(Events.CONNECT, bstack1l111l11l_opy_())
    platform_index = int(os.environ.get(bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭๶"), bstack111111l_opy_ (u"ࠧ࠱ࠩ๷")))
  else:
    bstack1lll11l111_opy_(bstack1111ll11ll_opy_)
  os.environ[bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩ๸")] = CONFIG[bstack111111l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ๹")]
  os.environ[bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞࠭๺")] = CONFIG[bstack111111l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ๻")]
  os.environ[bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ๼")] = bstack1l11l11lll_opy_.__str__()
  from _pytest.config import main as bstack1l1l1llll1_opy_
  bstack1l1llll11_opy_ = []
  try:
    exit_code = bstack1l1l1llll1_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack11lll111l_opy_()
    if bstack111111l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪ๽") in multiprocessing.current_process().__dict__.keys():
      for bstack1llll111l1_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l1llll11_opy_.append(bstack1llll111l1_opy_)
    try:
      bstack1l111l1l1_opy_ = (bstack1l1llll11_opy_, int(exit_code))
      bstack1lll1lll11_opy_.append(bstack1l111l1l1_opy_)
    except:
      bstack1lll1lll11_opy_.append((bstack1l1llll11_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1l1llll11_opy_.append({bstack111111l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ๾"): bstack111111l_opy_ (u"ࠨࡒࡵࡳࡨ࡫ࡳࡴࠢࠪ๿") + os.environ.get(bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ຀")), bstack111111l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩກ"): traceback.format_exc(), bstack111111l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪຂ"): int(os.environ.get(bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬ຃")))})
    bstack1lll1lll11_opy_.append((bstack1l1llll11_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack111111l_opy_ (u"ࠨࡲࡦࡶࡵ࡭ࡪࡹࠢຄ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack111l1l11l_opy_ = e.__class__.__name__
    print(bstack111111l_opy_ (u"ࠢࠦࡵ࠽ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡧ࡫ࡨࡢࡸࡨࠤࡹ࡫ࡳࡵࠢࠨࡷࠧ຅") % (bstack111l1l11l_opy_, e))
    return 1
def bstack11111lllll_opy_(arg):
  global bstack1l111ll11l_opy_
  bstack1lll11l111_opy_(bstack111l1ll11_opy_)
  os.environ[bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩຆ")] = str(bstack1ll11lll11_opy_)
  retries = bstack1lll1ll11_opy_.bstack1111111l_opy_(CONFIG)
  status_code = 0
  if bstack1lll1ll11_opy_.bstack1111lll1_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack1ll1l11ll1_opy_
    status_code = bstack1ll1l11ll1_opy_(arg)
  if status_code != 0:
    bstack1l111ll11l_opy_ = status_code
def bstack1ll1l11l11_opy_():
  logger.info(bstack1l1llllll1_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack111111l_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨງ"), help=bstack111111l_opy_ (u"ࠪࡋࡪࡴࡥࡳࡣࡷࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡨࡵ࡮ࡧ࡫ࡪࠫຈ"))
  parser.add_argument(bstack111111l_opy_ (u"ࠫ࠲ࡻࠧຉ"), bstack111111l_opy_ (u"ࠬ࠳࠭ࡶࡵࡨࡶࡳࡧ࡭ࡦࠩຊ"), help=bstack111111l_opy_ (u"࡙࠭ࡰࡷࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬ຋"))
  parser.add_argument(bstack111111l_opy_ (u"ࠧ࠮࡭ࠪຌ"), bstack111111l_opy_ (u"ࠨ࠯࠰࡯ࡪࡿࠧຍ"), help=bstack111111l_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡡࡤࡥࡨࡷࡸࠦ࡫ࡦࡻࠪຎ"))
  parser.add_argument(bstack111111l_opy_ (u"ࠪ࠱࡫࠭ຏ"), bstack111111l_opy_ (u"ࠫ࠲࠳ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩຐ"), help=bstack111111l_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡸࡪࡹࡴࠡࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫຑ"))
  bstack11ll111ll1_opy_ = parser.parse_args()
  try:
    bstack11l111l11l_opy_ = bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡭ࡥ࡯ࡧࡵ࡭ࡨ࠴ࡹ࡮࡮࠱ࡷࡦࡳࡰ࡭ࡧࠪຒ")
    if bstack11ll111ll1_opy_.framework and bstack11ll111ll1_opy_.framework not in (bstack111111l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧຓ"), bstack111111l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩດ")):
      bstack11l111l11l_opy_ = bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࠲ࡾࡳ࡬࠯ࡵࡤࡱࡵࡲࡥࠨຕ")
    bstack11l111lll1_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l111l11l_opy_)
    bstack1ll1lll1l_opy_ = open(bstack11l111lll1_opy_, bstack111111l_opy_ (u"ࠪࡶࠬຖ"))
    bstack1ll1l11l1_opy_ = bstack1ll1lll1l_opy_.read()
    bstack1ll1lll1l_opy_.close()
    if bstack11ll111ll1_opy_.username:
      bstack1ll1l11l1_opy_ = bstack1ll1l11l1_opy_.replace(bstack111111l_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫທ"), bstack11ll111ll1_opy_.username)
    if bstack11ll111ll1_opy_.key:
      bstack1ll1l11l1_opy_ = bstack1ll1l11l1_opy_.replace(bstack111111l_opy_ (u"ࠬ࡟ࡏࡖࡔࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧຘ"), bstack11ll111ll1_opy_.key)
    if bstack11ll111ll1_opy_.framework:
      bstack1ll1l11l1_opy_ = bstack1ll1l11l1_opy_.replace(bstack111111l_opy_ (u"࡙࠭ࡐࡗࡕࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧນ"), bstack11ll111ll1_opy_.framework)
    file_name = bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪບ")
    file_path = os.path.abspath(file_name)
    bstack11l1lll111_opy_ = open(file_path, bstack111111l_opy_ (u"ࠨࡹࠪປ"))
    bstack11l1lll111_opy_.write(bstack1ll1l11l1_opy_)
    bstack11l1lll111_opy_.close()
    logger.info(bstack1l11l11l1l_opy_)
    try:
      os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫຜ")] = bstack11ll111ll1_opy_.framework if bstack11ll111ll1_opy_.framework != None else bstack111111l_opy_ (u"ࠥࠦຝ")
      config = yaml.safe_load(bstack1ll1l11l1_opy_)
      config[bstack111111l_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫພ")] = bstack111111l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠲ࡹࡥࡵࡷࡳࠫຟ")
      bstack1lll11l1l1_opy_(bstack11ll1lll11_opy_, config)
    except Exception as e:
      logger.debug(bstack1l1l1111l_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack11lllll11_opy_.format(str(e)))
def bstack1lll11l1l1_opy_(bstack1111ll1l1_opy_, config, bstack1l111l111l_opy_={}):
  global bstack1l11l11lll_opy_
  global bstack111l1ll1l_opy_
  global bstack11111lll_opy_
  if not config:
    return
  bstack1lll111l1l_opy_ = bstack1lllllll1l_opy_ if not bstack1l11l11lll_opy_ else (
    bstack1lllll11ll_opy_ if bstack111111l_opy_ (u"࠭ࡡࡱࡲࠪຠ") in config else (
        bstack1ll1l1lll1_opy_ if config.get(bstack111111l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫມ")) else bstack1ll11lllll_opy_
    )
)
  bstack1l11lll1ll_opy_ = False
  bstack111111ll1_opy_ = False
  if bstack1l11l11lll_opy_ is True:
      if bstack111111l_opy_ (u"ࠨࡣࡳࡴࠬຢ") in config:
          bstack1l11lll1ll_opy_ = True
      else:
          bstack111111ll1_opy_ = True
  bstack1l1l1l1ll_opy_ = bstack1l1l1l1l1_opy_.bstack1111111ll_opy_(config, bstack111l1ll1l_opy_)
  bstack1l11ll1l1l_opy_ = bstack1l1111l1ll_opy_()
  data = {
    bstack111111l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫຣ"): config[bstack111111l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ຤")],
    bstack111111l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧລ"): config[bstack111111l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ຦")],
    bstack111111l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪວ"): bstack1111ll1l1_opy_,
    bstack111111l_opy_ (u"ࠧࡥࡧࡷࡩࡨࡺࡥࡥࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫຨ"): os.environ.get(bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪຩ"), bstack111l1ll1l_opy_),
    bstack111111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫສ"): bstack1111l1lll_opy_,
    bstack111111l_opy_ (u"ࠪࡳࡵࡺࡩ࡮ࡣ࡯ࡣ࡭ࡻࡢࡠࡷࡵࡰࠬຫ"): bstack11l1ll11ll_opy_(),
    bstack111111l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧຬ"): {
      bstack111111l_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫࡟ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪອ"): str(config[bstack111111l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ຮ")]) if bstack111111l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧຯ") in config else bstack111111l_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤະ"),
      bstack111111l_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨ࡚ࡪࡸࡳࡪࡱࡱࠫັ"): sys.version,
      bstack111111l_opy_ (u"ࠪࡶࡪ࡬ࡥࡳࡴࡨࡶࠬາ"): bstack1ll11l11l_opy_(os.environ.get(bstack111111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ຳ"), bstack111l1ll1l_opy_)),
      bstack111111l_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧິ"): bstack111111l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ີ"),
      bstack111111l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨຶ"): bstack1lll111l1l_opy_,
      bstack111111l_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࡡࡰࡥࡵ࠭ື"): bstack1l1l1l1ll_opy_,
      bstack111111l_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡢࡹࡺ࡯ࡤࠨຸ"): os.environ[bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨູ")],
      bstack111111l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ຺ࠧ"): os.environ.get(bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧົ"), bstack111l1ll1l_opy_),
      bstack111111l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩຼ"): bstack1l1ll1l11l_opy_(os.environ.get(bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩຽ"), bstack111l1ll1l_opy_)),
      bstack111111l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ຾"): bstack1l11ll1l1l_opy_.get(bstack111111l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ຿")),
      bstack111111l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩເ"): bstack1l11ll1l1l_opy_.get(bstack111111l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬແ")),
      bstack111111l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨໂ"): config[bstack111111l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩໃ")] if config[bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪໄ")] else bstack111111l_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤ໅"),
      bstack111111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫໆ"): str(config[bstack111111l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ໇")]) if bstack111111l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ່࠭") in config else bstack111111l_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨ້"),
      bstack111111l_opy_ (u"࠭࡯ࡴ໊ࠩ"): sys.platform,
      bstack111111l_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦ໋ࠩ"): socket.gethostname(),
      bstack111111l_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪ໌"): bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫໍ"))
    }
  }
  if not bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪ໎")) is None:
    data[bstack111111l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ໏")][bstack111111l_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪࡍࡦࡶࡤࡨࡦࡺࡡࠨ໐")] = {
      bstack111111l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭໑"): bstack111111l_opy_ (u"ࠧࡶࡵࡨࡶࡤࡱࡩ࡭࡮ࡨࡨࠬ໒"),
      bstack111111l_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࠨ໓"): bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩ໔")),
      bstack111111l_opy_ (u"ࠪࡷ࡮࡭࡮ࡢ࡮ࡑࡹࡲࡨࡥࡳࠩ໕"): bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡓࡵࠧ໖"))
    }
  if bstack1111ll1l1_opy_ == bstack1l1ll11l1l_opy_:
    data[bstack111111l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ໗")][bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡈࡵ࡮ࡧ࡫ࡪࠫ໘")] = bstack1l11111lll_opy_(config)
    data[bstack111111l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ໙")][bstack111111l_opy_ (u"ࠨ࡫ࡶࡔࡪࡸࡣࡺࡃࡸࡸࡴࡋ࡮ࡢࡤ࡯ࡩࡩ࠭໚")] = percy.bstack1l1l111ll_opy_
    data[bstack111111l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໛")][bstack111111l_opy_ (u"ࠪࡴࡪࡸࡣࡺࡄࡸ࡭ࡱࡪࡉࡥࠩໜ")] = percy.percy_build_id
  if not bstack1lll1ll11_opy_.bstack111l1l1111_opy_(CONFIG):
    data[bstack111111l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧໝ")][bstack111111l_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠩໞ")] = bstack1lll1ll11_opy_.bstack111l1l1111_opy_(CONFIG)
  bstack111lll11_opy_ = bstack11111ll1_opy_.bstack111l111l_opy_(CONFIG, logger)
  bstack1111l1l1_opy_ = bstack1lll1ll11_opy_.bstack111l111l_opy_(config=CONFIG)
  if bstack111lll11_opy_ is not None and bstack1111l1l1_opy_ is not None and bstack1111l1l1_opy_.bstack1111l111_opy_():
    data[bstack111111l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩໟ")][bstack1111l1l1_opy_.bstack111l111ll_opy_()] = bstack111lll11_opy_.bstack111ll11ll_opy_()
  update(data[bstack111111l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ໠")], bstack1l111l111l_opy_)
  try:
    response = bstack1l11l1ll1l_opy_(bstack111111l_opy_ (u"ࠨࡒࡒࡗ࡙࠭໡"), bstack11ll11l11_opy_(bstack111llllll_opy_), data, {
      bstack111111l_opy_ (u"ࠩࡤࡹࡹ࡮ࠧ໢"): (config[bstack111111l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ໣")], config[bstack111111l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ໤")])
    })
    if response:
      logger.debug(bstack11111l1ll_opy_.format(bstack1111ll1l1_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1lll111ll_opy_.format(str(e)))
def bstack1ll11l11l_opy_(framework):
  return bstack111111l_opy_ (u"ࠧࢁࡽ࠮ࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࡻࡾࠤ໥").format(str(framework), __version__) if framework else bstack111111l_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࢀࢃࠢ໦").format(
    __version__)
def bstack11l1llll1_opy_():
  global CONFIG
  global bstack1l11l11ll1_opy_
  if bool(CONFIG):
    return
  try:
    bstack11ll111l1_opy_()
    logger.debug(bstack1lll111lll_opy_.format(str(CONFIG)))
    bstack1l11l11ll1_opy_ = bstack11111ll111_opy_.configure_logger(CONFIG, bstack1l11l11ll1_opy_)
    bstack11llll1ll1_opy_()
  except Exception as e:
    logger.error(bstack111111l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࡵࡱ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠦ໧") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1ll1ll1l1_opy_
  atexit.register(bstack1ll11l1l1_opy_)
  signal.signal(signal.SIGINT, bstack1llll11ll1_opy_)
  signal.signal(signal.SIGTERM, bstack1llll11ll1_opy_)
def bstack1ll1ll1l1_opy_(exctype, value, traceback):
  global bstack1111l11l1l_opy_
  try:
    for driver in bstack1111l11l1l_opy_:
      bstack1ll111l1ll_opy_(driver, bstack111111l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ໨"), bstack111111l_opy_ (u"ࠤࡖࡩࡸࡹࡩࡰࡰࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧ໩") + str(value))
  except Exception:
    pass
  logger.info(bstack11ll1llll_opy_)
  bstack1llll1l1ll_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1llll1l1ll_opy_(message=bstack111111l_opy_ (u"ࠪࠫ໪"), bstack1l111ll1ll_opy_ = False):
  global CONFIG
  bstack1lll111111_opy_ = bstack111111l_opy_ (u"ࠫ࡬ࡲ࡯ࡣࡣ࡯ࡉࡽࡩࡥࡱࡶ࡬ࡳࡳ࠭໫") if bstack1l111ll1ll_opy_ else bstack111111l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ໬")
  try:
    if message:
      bstack1l111l111l_opy_ = {
        bstack1lll111111_opy_ : str(message)
      }
      bstack1lll11l1l1_opy_(bstack1l1ll11l1l_opy_, CONFIG, bstack1l111l111l_opy_)
    else:
      bstack1lll11l1l1_opy_(bstack1l1ll11l1l_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack11l1l1ll1_opy_.format(str(e)))
def bstack1l1ll1l1l1_opy_(bstack11lll111ll_opy_, size):
  bstack11l1ll1l1l_opy_ = []
  while len(bstack11lll111ll_opy_) > size:
    bstack1lll111ll1_opy_ = bstack11lll111ll_opy_[:size]
    bstack11l1ll1l1l_opy_.append(bstack1lll111ll1_opy_)
    bstack11lll111ll_opy_ = bstack11lll111ll_opy_[size:]
  bstack11l1ll1l1l_opy_.append(bstack11lll111ll_opy_)
  return bstack11l1ll1l1l_opy_
def bstack1ll1l1l11l_opy_(args):
  if bstack111111l_opy_ (u"࠭࠭࡮ࠩ໭") in args and bstack111111l_opy_ (u"ࠧࡱࡦࡥࠫ໮") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack111ll11111_opy_, stage=STAGE.bstack11l11l1l1l_opy_)
def run_on_browserstack(bstack1111lll1l_opy_=None, bstack1lll1lll11_opy_=None, bstack11l1111l11_opy_=False):
  global CONFIG
  global bstack1lll1ll1ll_opy_
  global bstack1ll11lll11_opy_
  global bstack111l1ll1l_opy_
  global bstack11111lll_opy_
  bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"ࠨࠩ໯")
  bstack11l1lll11l_opy_(bstack1l11l1l1l1_opy_, logger)
  if bstack1111lll1l_opy_ and isinstance(bstack1111lll1l_opy_, str):
    bstack1111lll1l_opy_ = eval(bstack1111lll1l_opy_)
  if bstack1111lll1l_opy_:
    CONFIG = bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ໰")]
    bstack1lll1ll1ll_opy_ = bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫ໱")]
    bstack1ll11lll11_opy_ = bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭໲")]
    bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ໳"), bstack1ll11lll11_opy_)
    bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭໴")
  bstack11111lll_opy_.set_property(bstack111111l_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ໵"), uuid4().__str__())
  logger.info(bstack111111l_opy_ (u"ࠨࡕࡇࡏࠥࡸࡵ࡯ࠢࡶࡸࡦࡸࡴࡦࡦࠣࡻ࡮ࡺࡨࠡ࡫ࡧ࠾ࠥ࠭໶") + bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ໷")));
  logger.debug(bstack111111l_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࡂ࠭໸") + bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭໹")))
  if not bstack11l1111l11_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack11ll1l1111_opy_)
      return
    if sys.argv[1] == bstack111111l_opy_ (u"ࠬ࠳࠭ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ໺") or sys.argv[1] == bstack111111l_opy_ (u"࠭࠭ࡷࠩ໻"):
      logger.info(bstack111111l_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡐࡺࡶ࡫ࡳࡳࠦࡓࡅࡍࠣࡺࢀࢃࠧ໼").format(__version__))
      return
    if sys.argv[1] == bstack111111l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧ໽"):
      bstack1ll1l11l11_opy_()
      return
  args = sys.argv
  bstack11l1llll1_opy_()
  global bstack1l1llll1ll_opy_
  global bstack11l1l1l111_opy_
  global bstack11111llll1_opy_
  global bstack1ll11ll1ll_opy_
  global bstack111lll111_opy_
  global bstack1ll1l1l111_opy_
  global bstack1l1ll11ll_opy_
  global bstack1ll1111l1l_opy_
  global bstack111lll11l_opy_
  global bstack1lll1ll111_opy_
  global bstack1lll11ll11_opy_
  bstack11l1l1l111_opy_ = len(CONFIG.get(bstack111111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ໾"), []))
  if not bstack1l1l111l1_opy_:
    if args[1] == bstack111111l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ໿") or args[1] == bstack111111l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬༀ"):
      bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ༁")
      args = args[2:]
    elif args[1] == bstack111111l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ༂"):
      bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭༃")
      args = args[2:]
    elif args[1] == bstack111111l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ༄"):
      bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༅")
      args = args[2:]
    elif args[1] == bstack111111l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ༆"):
      bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ༇")
      args = args[2:]
    elif args[1] == bstack111111l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ༈"):
      bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭༉")
      args = args[2:]
    elif args[1] == bstack111111l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ༊"):
      bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ་")
      args = args[2:]
    else:
      if not bstack111111l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ༌") in CONFIG or str(CONFIG[bstack111111l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭།")]).lower() in [bstack111111l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༎"), bstack111111l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭༏")]:
        bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭༐")
        args = args[1:]
      elif str(CONFIG[bstack111111l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༑")]).lower() == bstack111111l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ༒"):
        bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ༓")
        args = args[1:]
      elif str(CONFIG[bstack111111l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭༔")]).lower() == bstack111111l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ༕"):
        bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ༖")
        args = args[1:]
      elif str(CONFIG[bstack111111l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༗")]).lower() == bstack111111l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ༘ࠧ"):
        bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ༙")
        args = args[1:]
      elif str(CONFIG[bstack111111l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ༚")]).lower() == bstack111111l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ༛"):
        bstack1l1l111l1_opy_ = bstack111111l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ༜")
        args = args[1:]
      else:
        os.environ[bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ༝")] = bstack1l1l111l1_opy_
        bstack1ll111l11_opy_(bstack11lllll1l_opy_)
  os.environ[bstack111111l_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧ༞")] = bstack1l1l111l1_opy_
  bstack111l1ll1l_opy_ = bstack1l1l111l1_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack11llll11l_opy_ = bstack11l1ll1ll_opy_[bstack111111l_opy_ (u"ࠧࡑ࡛ࡗࡉࡘ࡚࠭ࡃࡆࡇࠫ༟")] if bstack1l1l111l1_opy_ == bstack111111l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ༠") and bstack1ll11111l1_opy_() else bstack1l1l111l1_opy_
      bstack111ll111l1_opy_.invoke(Events.bstack1l11l1llll_opy_, bstack1lll1l11ll_opy_(
        sdk_version=__version__,
        path_config=bstack11ll1l1l1_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack11llll11l_opy_,
        frameworks=[bstack11llll11l_opy_],
        framework_versions={
          bstack11llll11l_opy_: bstack1l1ll1l11l_opy_(bstack111111l_opy_ (u"ࠩࡕࡳࡧࡵࡴࠨ༡") if bstack1l1l111l1_opy_ in [bstack111111l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ༢"), bstack111111l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༣"), bstack111111l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭༤")] else bstack1l1l111l1_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack111111l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ༥"), None):
        CONFIG[bstack111111l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤ༦")] = cli.config.get(bstack111111l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥ༧"), None)
    except Exception as e:
      bstack111ll111l1_opy_.invoke(Events.bstack1llllllll1_opy_, e.__traceback__, 1)
    if bstack1ll11lll11_opy_:
      CONFIG[bstack111111l_opy_ (u"ࠤࡤࡴࡵࠨ༨")] = cli.config[bstack111111l_opy_ (u"ࠥࡥࡵࡶࠢ༩")]
      logger.info(bstack1ll111111l_opy_.format(CONFIG[bstack111111l_opy_ (u"ࠫࡦࡶࡰࠨ༪")]))
  else:
    bstack111ll111l1_opy_.clear()
  global bstack1l11l1l1l_opy_
  global bstack1111lllll1_opy_
  if bstack1111lll1l_opy_:
    try:
      bstack1111ll111_opy_ = datetime.datetime.now()
      os.environ[bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ༫")] = bstack1l1l111l1_opy_
      bstack1lll11l1l1_opy_(bstack11ll11111_opy_, CONFIG)
      cli.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠨࡨࡵࡶࡳ࠾ࡸࡪ࡫ࡠࡶࡨࡷࡹࡥࡡࡵࡶࡨࡱࡵࡺࡥࡥࠤ༬"), datetime.datetime.now() - bstack1111ll111_opy_)
    except Exception as e:
      logger.debug(bstack1l1lll1l1_opy_.format(str(e)))
  global bstack1ll1111lll_opy_
  global bstack1lll1111ll_opy_
  global bstack1l11ll11ll_opy_
  global bstack11ll1l11l1_opy_
  global bstack1l1lll11l_opy_
  global bstack1ll1l1l1l1_opy_
  global bstack1llllll11l_opy_
  global bstack111ll111ll_opy_
  global bstack1l111lllll_opy_
  global bstack1lll1111l1_opy_
  global bstack1l11ll1l11_opy_
  global bstack11l1l111ll_opy_
  global bstack11l111ll1_opy_
  global bstack1l11lll111_opy_
  global bstack11l111111l_opy_
  global bstack1lll11l11_opy_
  global bstack1ll1lll1l1_opy_
  global bstack1l11l1l11_opy_
  global bstack11lll1111_opy_
  global bstack1llll1llll_opy_
  global bstack1l1ll1lll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll1111lll_opy_ = webdriver.Remote.__init__
    bstack1lll1111ll_opy_ = WebDriver.quit
    bstack11l1l111ll_opy_ = WebDriver.close
    bstack11l111111l_opy_ = WebDriver.get
    bstack1l1ll1lll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1l11l1l1l_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack111ll1lll1_opy_
    bstack1111lllll1_opy_ = bstack111ll1lll1_opy_()
  except Exception as e:
    pass
  try:
    global bstack1ll1ll11l_opy_
    from QWeb.keywords import browser
    bstack1ll1ll11l_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1l1111ll1l_opy_(CONFIG) and bstack11ll1l1lll_opy_():
    if bstack1ll1llllll_opy_() < version.parse(bstack1l1ll1ll11_opy_):
      logger.error(bstack1l1111lll_opy_.format(bstack1ll1llllll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack111111l_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨ༭")) and callable(getattr(RemoteConnection, bstack111111l_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ༮"))):
          RemoteConnection._get_proxy_url = bstack1l11lllll1_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack1l11lllll1_opy_
      except Exception as e:
        logger.error(bstack1l1ll1l1l_opy_.format(str(e)))
  if not CONFIG.get(bstack111111l_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫ༯"), False) and not bstack1111lll1l_opy_:
    logger.info(bstack1ll1ll111l_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack111111l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ༰") in CONFIG and str(CONFIG[bstack111111l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ༱")]).lower() != bstack111111l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ༲"):
      bstack1111lll1l1_opy_()
    elif bstack1l1l111l1_opy_ != bstack111111l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭༳") or (bstack1l1l111l1_opy_ == bstack111111l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༴") and not bstack1111lll1l_opy_):
      bstack1ll1ll1l11_opy_()
  if (bstack1l1l111l1_opy_ in [bstack111111l_opy_ (u"ࠨࡲࡤࡦࡴࡺ༵ࠧ"), bstack111111l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ༶"), bstack111111l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯༷ࠫ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1111l1l1l1_opy_
        bstack1ll1l1l1l1_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1llll1ll1l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1l1lll11l_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1ll1111l1_opy_ + str(e))
    except Exception as e:
      bstack1l11l1lll1_opy_(e, bstack1llll1ll1l_opy_)
    if bstack1l1l111l1_opy_ != bstack111111l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ༸"):
      bstack11ll1ll1l_opy_()
    bstack1l11ll11ll_opy_ = Output.start_test
    bstack11ll1l11l1_opy_ = Output.end_test
    bstack1llllll11l_opy_ = TestStatus.__init__
    bstack1l111lllll_opy_ = pabot._run
    bstack1lll1111l1_opy_ = QueueItem.__init__
    bstack1l11ll1l11_opy_ = pabot._create_command_for_execution
    bstack11lll1111_opy_ = pabot._report_results
  if bstack1l1l111l1_opy_ == bstack111111l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩ༹ࠬ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l11l1lll1_opy_(e, bstack1l1l1l1l1l_opy_)
    bstack11l111ll1_opy_ = Runner.run_hook
    bstack1l11lll111_opy_ = Step.run
  if bstack1l1l111l1_opy_ == bstack111111l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭༺"):
    try:
      from _pytest.config import Config
      bstack1ll1lll1l1_opy_ = Config.getoption
      from _pytest import runner
      bstack1l11l1l11_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack11111111_opy_)
    try:
      from pytest_bdd import reporting
      bstack1llll1llll_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack111111l_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨ༻"))
  try:
    framework_name = bstack111111l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ༼") if bstack1l1l111l1_opy_ in [bstack111111l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༽"), bstack111111l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ༾"), bstack111111l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ༿")] else bstack1l11l1l111_opy_(bstack1l1l111l1_opy_)
    bstack11l1lll11_opy_ = {
      bstack111111l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭ཀ"): bstack111111l_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨཁ") if bstack1l1l111l1_opy_ == bstack111111l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧག") and bstack1ll11111l1_opy_() else framework_name,
      bstack111111l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬགྷ"): bstack1l1ll1l11l_opy_(framework_name),
      bstack111111l_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧང"): __version__,
      bstack111111l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡵࡴࡧࡧࠫཅ"): bstack1l1l111l1_opy_
    }
    if bstack1l1l111l1_opy_ in bstack11l11ll1l1_opy_ + bstack11l1ll111_opy_:
      if bstack1llll111l_opy_.bstack11ll1l11ll_opy_(CONFIG):
        if bstack111111l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫཆ") in CONFIG:
          os.environ[bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ཇ")] = os.getenv(bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ཈"), json.dumps(CONFIG[bstack111111l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧཉ")]))
          CONFIG[bstack111111l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨཊ")].pop(bstack111111l_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧཋ"), None)
          CONFIG[bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪཌ")].pop(bstack111111l_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩཌྷ"), None)
        bstack11l1lll11_opy_[bstack111111l_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬཎ")] = {
          bstack111111l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫཏ"): bstack111111l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩཐ"),
          bstack111111l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩད"): str(bstack1ll1llllll_opy_())
        }
    if bstack1l1l111l1_opy_ not in [bstack111111l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪདྷ")] and not cli.is_running():
      bstack11l111llll_opy_, bstack111ll1111_opy_ = bstack1ll1l111_opy_.launch(CONFIG, bstack11l1lll11_opy_)
      if bstack111ll1111_opy_.get(bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪན")) is not None and bstack1llll111l_opy_.bstack11llll1l11_opy_(CONFIG) is None:
        value = bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫཔ")].get(bstack111111l_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭ཕ"))
        if value is not None:
            CONFIG[bstack111111l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭བ")] = value
        else:
          logger.debug(bstack111111l_opy_ (u"ࠢࡏࡱࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡨࡦࡺࡡࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧབྷ"))
  except Exception as e:
    logger.debug(bstack1l111lll11_opy_.format(bstack111111l_opy_ (u"ࠨࡖࡨࡷࡹࡎࡵࡣࠩམ"), str(e)))
  if bstack1l1l111l1_opy_ == bstack111111l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩཙ"):
    bstack11111llll1_opy_ = True
    if bstack1111lll1l_opy_ and bstack11l1111l11_opy_:
      bstack1ll1l1l111_opy_ = CONFIG.get(bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧཚ"), {}).get(bstack111111l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ཛ"))
      bstack1lll11l111_opy_(bstack1ll111111_opy_)
    elif bstack1111lll1l_opy_:
      bstack1ll1l1l111_opy_ = CONFIG.get(bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩཛྷ"), {}).get(bstack111111l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨཝ"))
      global bstack1111l11l1l_opy_
      try:
        if bstack1ll1l1l11l_opy_(bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪཞ")]) and multiprocessing.current_process().name == bstack111111l_opy_ (u"ࠨ࠲ࠪཟ"):
          bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬའ")].remove(bstack111111l_opy_ (u"ࠪ࠱ࡲ࠭ཡ"))
          bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧར")].remove(bstack111111l_opy_ (u"ࠬࡶࡤࡣࠩལ"))
          bstack1111lll1l_opy_[bstack111111l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩཤ")] = bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪཥ")][0]
          with open(bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫས")], bstack111111l_opy_ (u"ࠩࡵࠫཧ")) as f:
            file_content = f.read()
          bstack1l1ll11l11_opy_ = bstack111111l_opy_ (u"ࠥࠦࠧ࡬ࡲࡰ࡯ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡶࡨࡰࠦࡩ࡮ࡲࡲࡶࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡦ࠽ࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪ࠮ࡻࡾࠫ࠾ࠤ࡫ࡸ࡯࡮ࠢࡳࡨࡧࠦࡩ࡮ࡲࡲࡶࡹࠦࡐࡥࡤ࠾ࠤࡴ࡭࡟ࡥࡤࠣࡁࠥࡖࡤࡣ࠰ࡧࡳࡤࡨࡲࡦࡣ࡮࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡦࡨࡪࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠩࡵࡨࡰ࡫࠲ࠠࡢࡴࡪ࠰ࠥࡺࡥ࡮ࡲࡲࡶࡦࡸࡹࠡ࠿ࠣ࠴࠮ࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺࡲࡺ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡥࡷ࡭ࠠ࠾ࠢࡶࡸࡷ࠮ࡩ࡯ࡶࠫࡥࡷ࡭ࠩࠬ࠳࠳࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡩࡽࡩࡥࡱࡶࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡡࡴࠢࡨ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡶࡡࡴࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡱࡪࡣࡩࡨࠨࡴࡧ࡯ࡪ࠱ࡧࡲࡨ࠮ࡷࡩࡲࡶ࡯ࡳࡣࡵࡽ࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࠤࡂࠦ࡭ࡰࡦࡢࡦࡷ࡫ࡡ࡬ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡖࡤࡣ࠰ࡧࡳࡤࡨࡲࡦࡣ࡮ࠤࡂࠦ࡭ࡰࡦࡢࡦࡷ࡫ࡡ࡬ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡖࡤࡣࠪࠬ࠲ࡸ࡫ࡴࡠࡶࡵࡥࡨ࡫ࠨࠪ࡞ࡱࠦࠧࠨཨ").format(str(bstack1111lll1l_opy_))
          bstack11ll1111l_opy_ = bstack1l1ll11l11_opy_ + file_content
          bstack1ll1l1l11_opy_ = bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཀྵ")] + bstack111111l_opy_ (u"ࠬࡥࡢࡴࡶࡤࡧࡰࡥࡴࡦ࡯ࡳ࠲ࡵࡿࠧཪ")
          with open(bstack1ll1l1l11_opy_, bstack111111l_opy_ (u"࠭ࡷࠨཫ")):
            pass
          with open(bstack1ll1l1l11_opy_, bstack111111l_opy_ (u"ࠢࡸ࠭ࠥཬ")) as f:
            f.write(bstack11ll1111l_opy_)
          import subprocess
          process_data = subprocess.run([bstack111111l_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࠣ཭"), bstack1ll1l1l11_opy_])
          if os.path.exists(bstack1ll1l1l11_opy_):
            os.unlink(bstack1ll1l1l11_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack1ll1l1l11l_opy_(bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ཮")]):
            bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭཯")].remove(bstack111111l_opy_ (u"ࠫ࠲ࡳࠧ཰"))
            bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཱ")].remove(bstack111111l_opy_ (u"࠭ࡰࡥࡤིࠪ"))
            bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧཱིࠪ")] = bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨུࠫ")][0]
          bstack1lll11l111_opy_(bstack1ll111111_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩཱུࠬ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack111111l_opy_ (u"ࠪࡣࡤࡴࡡ࡮ࡧࡢࡣࠬྲྀ")] = bstack111111l_opy_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ཷ")
          mod_globals[bstack111111l_opy_ (u"ࠬࡥ࡟ࡧ࡫࡯ࡩࡤࡥࠧླྀ")] = os.path.abspath(bstack1111lll1l_opy_[bstack111111l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩཹ")])
          exec(open(bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧེࠪ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack111111l_opy_ (u"ࠨࡅࡤࡹ࡬࡮ࡴࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠨཻ").format(str(e)))
          for driver in bstack1111l11l1l_opy_:
            bstack1lll1lll11_opy_.append({
              bstack111111l_opy_ (u"ࠩࡱࡥࡲ࡫ོࠧ"): bstack1111lll1l_opy_[bstack111111l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪཽ࠭")],
              bstack111111l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪཾ"): str(e),
              bstack111111l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫཿ"): multiprocessing.current_process().name
            })
            bstack1ll111l1ll_opy_(driver, bstack111111l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩྀ࠭"), bstack111111l_opy_ (u"ࠢࡔࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰཱྀࠥ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1111l11l1l_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1ll11lll11_opy_, CONFIG, logger)
      bstack1llll1l11l_opy_()
      bstack1l1l1l11ll_opy_()
      percy.bstack111l11l1l_opy_()
      bstack111ll1ll_opy_ = {
        bstack111111l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྂ"): args[0],
        bstack111111l_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩྃ"): CONFIG,
        bstack111111l_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏ྄ࠫ"): bstack1lll1ll1ll_opy_,
        bstack111111l_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭྅"): bstack1ll11lll11_opy_
      }
      if bstack111111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ྆") in CONFIG:
        bstack11ll1111l1_opy_ = bstack11l1111ll_opy_(args, logger, CONFIG, bstack1l11l11lll_opy_, bstack11l1l1l111_opy_)
        bstack1ll1111l1l_opy_ = bstack11ll1111l1_opy_.bstack1llllll11_opy_(run_on_browserstack, bstack111ll1ll_opy_, bstack1ll1l1l11l_opy_(args))
      else:
        if bstack1ll1l1l11l_opy_(args):
          bstack111ll1ll_opy_[bstack111111l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ྇")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack111ll1ll_opy_,))
          test.start()
          test.join()
        else:
          bstack1lll11l111_opy_(bstack1ll111111_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack111111l_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩྈ")] = bstack111111l_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪྉ")
          mod_globals[bstack111111l_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫྊ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1l1l111l1_opy_ == bstack111111l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩྋ") or bstack1l1l111l1_opy_ == bstack111111l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪྌ"):
    percy.init(bstack1ll11lll11_opy_, CONFIG, logger)
    percy.bstack111l11l1l_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l11l1lll1_opy_(e, bstack1llll1ll1l_opy_)
    bstack1llll1l11l_opy_()
    bstack1lll11l111_opy_(bstack1l1111l11_opy_)
    if bstack1l11l11lll_opy_:
      bstack11l1l1ll11_opy_(bstack1l1111l11_opy_, args)
      if bstack111111l_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪྍ") in args:
        i = args.index(bstack111111l_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫྎ"))
        args.pop(i)
        args.pop(i)
      if bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪྏ") not in CONFIG:
        CONFIG[bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫྐ")] = [{}]
        bstack11l1l1l111_opy_ = 1
      if bstack1l1llll1ll_opy_ == 0:
        bstack1l1llll1ll_opy_ = 1
      args.insert(0, str(bstack1l1llll1ll_opy_))
      args.insert(0, str(bstack111111l_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧྑ")))
    if bstack1ll1l111_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack11l11l1ll_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1lll11111l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack111111l_opy_ (u"ࠥࡖࡔࡈࡏࡕࡡࡒࡔ࡙ࡏࡏࡏࡕࠥྒ"),
        ).parse_args(bstack11l11l1ll_opy_)
        bstack1l1l11ll11_opy_ = args.index(bstack11l11l1ll_opy_[0]) if len(bstack11l11l1ll_opy_) > 0 else len(args)
        args.insert(bstack1l1l11ll11_opy_, str(bstack111111l_opy_ (u"ࠫ࠲࠳࡬ࡪࡵࡷࡩࡳ࡫ࡲࠨྒྷ")))
        args.insert(bstack1l1l11ll11_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111111l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡸ࡯ࡣࡱࡷࡣࡱ࡯ࡳࡵࡧࡱࡩࡷ࠴ࡰࡺࠩྔ"))))
        if bstack1lll1ll11_opy_.bstack1111lll1_opy_(CONFIG):
          args.insert(bstack1l1l11ll11_opy_, str(bstack111111l_opy_ (u"࠭࠭࠮࡮࡬ࡷࡹ࡫࡮ࡦࡴࠪྕ")))
          args.insert(bstack1l1l11ll11_opy_ + 1, str(bstack111111l_opy_ (u"ࠧࡓࡧࡷࡶࡾࡌࡡࡪ࡮ࡨࡨ࠿ࢁࡽࠨྖ").format(bstack1lll1ll11_opy_.bstack1111111l_opy_(CONFIG))))
        if bstack1llll11lll_opy_(os.environ.get(bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓ࠭ྗ"))) and str(os.environ.get(bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘ࠭྘"), bstack111111l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨྙ"))) != bstack111111l_opy_ (u"ࠫࡳࡻ࡬࡭ࠩྚ"):
          for bstack11lll1ll1_opy_ in bstack1lll11111l_opy_:
            args.remove(bstack11lll1ll1_opy_)
          test_files = os.environ.get(bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠩྛ")).split(bstack111111l_opy_ (u"࠭ࠬࠨྜ"))
          for bstack111l1l11_opy_ in test_files:
            args.append(bstack111l1l11_opy_)
      except Exception as e:
        logger.error(bstack111111l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡧࡴࡵࡣࡦ࡬࡮ࡴࡧࠡ࡮࡬ࡷࡹ࡫࡮ࡦࡴࠣࡪࡴࡸࠠࡼࡿ࠱ࠤࡊࡸࡲࡰࡴࠣ࠱ࠥࢁࡽࠣྜྷ").format(bstack11ll1ll1l1_opy_, e))
    pabot.main(args)
  elif bstack1l1l111l1_opy_ == bstack111111l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩྞ"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l11l1lll1_opy_(e, bstack1llll1ll1l_opy_)
    for a in args:
      if bstack111111l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘࠨྟ") in a:
        bstack111lll111_opy_ = int(a.split(bstack111111l_opy_ (u"ࠪ࠾ࠬྠ"))[1])
      if bstack111111l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡈࡊࡌࡌࡐࡅࡄࡐࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨྡ") in a:
        bstack1ll1l1l111_opy_ = str(a.split(bstack111111l_opy_ (u"ࠬࡀࠧྡྷ"))[1])
      if bstack111111l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭ྣ") in a:
        bstack1l1ll11ll_opy_ = str(a.split(bstack111111l_opy_ (u"ࠧ࠻ࠩྤ"))[1])
    bstack11llll1l1l_opy_ = None
    if bstack111111l_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠧྥ") in args:
      i = args.index(bstack111111l_opy_ (u"ࠩ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠨྦ"))
      args.pop(i)
      bstack11llll1l1l_opy_ = args.pop(i)
    if bstack11llll1l1l_opy_ is not None:
      global bstack1l1l11lll_opy_
      bstack1l1l11lll_opy_ = bstack11llll1l1l_opy_
    bstack1lll11l111_opy_(bstack1l1111l11_opy_)
    run_cli(args)
    if bstack111111l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧྦྷ") in multiprocessing.current_process().__dict__.keys():
      for bstack1llll111l1_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1lll1lll11_opy_.append(bstack1llll111l1_opy_)
  elif bstack1l1l111l1_opy_ == bstack111111l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫྨ"):
    bstack11ll11ll1l_opy_ = bstack1llll1111_opy_(args, logger, CONFIG, bstack1l11l11lll_opy_)
    bstack11ll11ll1l_opy_.bstack1111llll_opy_()
    bstack1llll1l11l_opy_()
    bstack1ll11ll1ll_opy_ = True
    bstack1lll1ll111_opy_ = bstack11ll11ll1l_opy_.bstack111l1l1l_opy_()
    bstack11ll11ll1l_opy_.bstack111ll1ll_opy_(bstack111llll11l_opy_)
    bstack11ll11ll1l_opy_.bstack111lll1l_opy_()
    bstack11l11ll1ll_opy_(bstack1l1l111l1_opy_, CONFIG, bstack11ll11ll1l_opy_.bstack11l1111l_opy_())
    bstack11ll1111ll_opy_ = bstack11ll11ll1l_opy_.bstack1llllll11_opy_(bstack1l1lll111l_opy_, {
      bstack111111l_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭ྩ"): bstack1lll1ll1ll_opy_,
      bstack111111l_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨྪ"): bstack1ll11lll11_opy_,
      bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪྫ"): bstack1l11l11lll_opy_
    })
    try:
      bstack1l1llll11_opy_, bstack1ll11lll1l_opy_ = map(list, zip(*bstack11ll1111ll_opy_))
      bstack111lll11l_opy_ = bstack1l1llll11_opy_[0]
      for status_code in bstack1ll11lll1l_opy_:
        if status_code != 0:
          bstack1lll11ll11_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack111111l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡧࡶࡦࠢࡨࡶࡷࡵࡲࡴࠢࡤࡲࡩࠦࡳࡵࡣࡷࡹࡸࠦࡣࡰࡦࡨ࠲ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࠼ࠣࡿࢂࠨྫྷ").format(str(e)))
  elif bstack1l1l111l1_opy_ == bstack111111l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩྭ"):
    try:
      from behave.__main__ import main as bstack1ll1l11ll1_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l11l1lll1_opy_(e, bstack1l1l1l1l1l_opy_)
    bstack1llll1l11l_opy_()
    bstack1ll11ll1ll_opy_ = True
    bstack1lll1ll1l_opy_ = 1
    if bstack111111l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪྮ") in CONFIG:
      bstack1lll1ll1l_opy_ = CONFIG[bstack111111l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫྯ")]
    if bstack111111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨྰ") in CONFIG:
      bstack1l1l111l11_opy_ = int(bstack1lll1ll1l_opy_) * int(len(CONFIG[bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩྱ")]))
    else:
      bstack1l1l111l11_opy_ = int(bstack1lll1ll1l_opy_)
    config = Configuration(args)
    bstack1l11l1111_opy_ = config.paths
    if len(bstack1l11l1111_opy_) == 0:
      import glob
      pattern = bstack111111l_opy_ (u"ࠧࠫࠬ࠲࠮࠳࡬ࡥࡢࡶࡸࡶࡪ࠭ྲ")
      bstack1lll11llll_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1lll11llll_opy_)
      config = Configuration(args)
      bstack1l11l1111_opy_ = config.paths
    bstack1llllll1l_opy_ = [os.path.normpath(item) for item in bstack1l11l1111_opy_]
    bstack1llll111ll_opy_ = [os.path.normpath(item) for item in args]
    bstack1ll11l111l_opy_ = [item for item in bstack1llll111ll_opy_ if item not in bstack1llllll1l_opy_]
    import platform as pf
    if pf.system().lower() == bstack111111l_opy_ (u"ࠨࡹ࡬ࡲࡩࡵࡷࡴࠩླ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1llllll1l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11lll1l111_opy_)))
                    for bstack11lll1l111_opy_ in bstack1llllll1l_opy_]
    bstack111llll1_opy_ = []
    for spec in bstack1llllll1l_opy_:
      bstack11l11l11_opy_ = []
      bstack11l11l11_opy_ += bstack1ll11l111l_opy_
      bstack11l11l11_opy_.append(spec)
      bstack111llll1_opy_.append(bstack11l11l11_opy_)
    execution_items = []
    for bstack11l11l11_opy_ in bstack111llll1_opy_:
      if bstack111111l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྴ") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack111111l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྵ")]):
          item = {}
          item[bstack111111l_opy_ (u"ࠫࡦࡸࡧࠨྶ")] = bstack111111l_opy_ (u"ࠬࠦࠧྷ").join(bstack11l11l11_opy_)
          item[bstack111111l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬྸ")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack111111l_opy_ (u"ࠧࡢࡴࡪࠫྐྵ")] = bstack111111l_opy_ (u"ࠨࠢࠪྺ").join(bstack11l11l11_opy_)
        item[bstack111111l_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨྻ")] = 0
        execution_items.append(item)
    bstack111lllll1l_opy_ = bstack1l1ll1l1l1_opy_(execution_items, bstack1l1l111l11_opy_)
    for execution_item in bstack111lllll1l_opy_:
      bstack11l11111_opy_ = []
      for item in execution_item:
        bstack11l11111_opy_.append(bstack11llll111_opy_(name=str(item[bstack111111l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩྼ")]),
                                             target=bstack11111lllll_opy_,
                                             args=(item[bstack111111l_opy_ (u"ࠫࡦࡸࡧࠨ྽")],)))
      for t in bstack11l11111_opy_:
        t.start()
      for t in bstack11l11111_opy_:
        t.join()
  else:
    bstack1ll111l11_opy_(bstack11lllll1l_opy_)
  if not bstack1111lll1l_opy_:
    bstack1l1l11l11l_opy_()
    if(bstack1l1l111l1_opy_ in [bstack111111l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ྾"), bstack111111l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭྿")]):
      bstack1l1l11ll1l_opy_()
  bstack11111ll111_opy_.bstack1l1l1l1111_opy_()
def browserstack_initialize(bstack111111l1l_opy_=None):
  logger.info(bstack111111l_opy_ (u"ࠧࡓࡷࡱࡲ࡮ࡴࡧࠡࡕࡇࡏࠥࡽࡩࡵࡪࠣࡥࡷ࡭ࡳ࠻ࠢࠪ࿀") + str(bstack111111l1l_opy_))
  run_on_browserstack(bstack111111l1l_opy_, None, True)
@measure(event_name=EVENTS.bstack11ll1l1ll_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1l1l11l11l_opy_():
  global CONFIG
  global bstack111l1ll1l_opy_
  global bstack1lll11ll11_opy_
  global bstack1l111ll11l_opy_
  global bstack11111lll_opy_
  bstack11ll1llll1_opy_.bstack111l11ll1l_opy_()
  if cli.is_running():
    bstack111ll111l1_opy_.invoke(Events.bstack11l1l11l1_opy_)
  else:
    bstack1111l1l1_opy_ = bstack1lll1ll11_opy_.bstack111l111l_opy_(config=CONFIG)
    bstack1111l1l1_opy_.bstack1111lll11l_opy_(CONFIG)
  if bstack111l1ll1l_opy_ == bstack111111l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ࿁"):
    if not cli.is_enabled(CONFIG):
      bstack1ll1l111_opy_.stop()
  else:
    bstack1ll1l111_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1ll1l1ll_opy_.bstack11l1l1l1l1_opy_()
  if bstack111111l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭࿂") in CONFIG and str(CONFIG[bstack111111l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ࿃")]).lower() != bstack111111l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ࿄"):
    hashed_id, bstack11l11l1l11_opy_ = bstack1111ll1lll_opy_()
  else:
    hashed_id, bstack11l11l1l11_opy_ = get_build_link()
  bstack1llll1l1l1_opy_(hashed_id)
  logger.info(bstack111111l_opy_ (u"࡙ࠬࡄࡌࠢࡵࡹࡳࠦࡥ࡯ࡦࡨࡨࠥ࡬࡯ࡳࠢ࡬ࡨ࠿࠭࿅") + bstack11111lll_opy_.get_property(bstack111111l_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ࿆"), bstack111111l_opy_ (u"ࠧࠨ࿇")) + bstack111111l_opy_ (u"ࠨ࠮ࠣࡸࡪࡹࡴࡩࡷࡥࠤ࡮ࡪ࠺ࠡࠩ࿈") + os.getenv(bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ࿉"), bstack111111l_opy_ (u"ࠪࠫ࿊")))
  if hashed_id is not None and bstack111llll111_opy_() != -1:
    sessions = bstack111lll1lll_opy_(hashed_id)
    bstack1ll11ll111_opy_(sessions, bstack11l11l1l11_opy_)
  if bstack111l1ll1l_opy_ == bstack111111l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ࿋") and bstack1lll11ll11_opy_ != 0:
    sys.exit(bstack1lll11ll11_opy_)
  if bstack111l1ll1l_opy_ == bstack111111l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ࿌") and bstack1l111ll11l_opy_ != 0:
    sys.exit(bstack1l111ll11l_opy_)
def bstack1llll1l1l1_opy_(new_id):
    global bstack1111l1lll_opy_
    bstack1111l1lll_opy_ = new_id
def bstack1l11l1l111_opy_(bstack1l1ll1111_opy_):
  if bstack1l1ll1111_opy_:
    return bstack1l1ll1111_opy_.capitalize()
  else:
    return bstack111111l_opy_ (u"࠭ࠧ࿍")
@measure(event_name=EVENTS.bstack1lll1ll1l1_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1l1lllll1l_opy_(bstack1l1lll1ll_opy_):
  if bstack111111l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ࿎") in bstack1l1lll1ll_opy_ and bstack1l1lll1ll_opy_[bstack111111l_opy_ (u"ࠨࡰࡤࡱࡪ࠭࿏")] != bstack111111l_opy_ (u"ࠩࠪ࿐"):
    return bstack1l1lll1ll_opy_[bstack111111l_opy_ (u"ࠪࡲࡦࡳࡥࠨ࿑")]
  else:
    bstack1l111l1ll_opy_ = bstack111111l_opy_ (u"ࠦࠧ࿒")
    if bstack111111l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬ࿓") in bstack1l1lll1ll_opy_ and bstack1l1lll1ll_opy_[bstack111111l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭࿔")] != None:
      bstack1l111l1ll_opy_ += bstack1l1lll1ll_opy_[bstack111111l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ࿕")] + bstack111111l_opy_ (u"ࠣ࠮ࠣࠦ࿖")
      if bstack1l1lll1ll_opy_[bstack111111l_opy_ (u"ࠩࡲࡷࠬ࿗")] == bstack111111l_opy_ (u"ࠥ࡭ࡴࡹࠢ࿘"):
        bstack1l111l1ll_opy_ += bstack111111l_opy_ (u"ࠦ࡮ࡕࡓࠡࠤ࿙")
      bstack1l111l1ll_opy_ += (bstack1l1lll1ll_opy_[bstack111111l_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ࿚")] or bstack111111l_opy_ (u"࠭ࠧ࿛"))
      return bstack1l111l1ll_opy_
    else:
      bstack1l111l1ll_opy_ += bstack1l11l1l111_opy_(bstack1l1lll1ll_opy_[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ࿜")]) + bstack111111l_opy_ (u"ࠣࠢࠥ࿝") + (
              bstack1l1lll1ll_opy_[bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ࿞")] or bstack111111l_opy_ (u"ࠪࠫ࿟")) + bstack111111l_opy_ (u"ࠦ࠱ࠦࠢ࿠")
      if bstack1l1lll1ll_opy_[bstack111111l_opy_ (u"ࠬࡵࡳࠨ࿡")] == bstack111111l_opy_ (u"ࠨࡗࡪࡰࡧࡳࡼࡹࠢ࿢"):
        bstack1l111l1ll_opy_ += bstack111111l_opy_ (u"ࠢࡘ࡫ࡱࠤࠧ࿣")
      bstack1l111l1ll_opy_ += bstack1l1lll1ll_opy_[bstack111111l_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ࿤")] or bstack111111l_opy_ (u"ࠩࠪ࿥")
      return bstack1l111l1ll_opy_
@measure(event_name=EVENTS.bstack1l1ll1l11_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1llllll111_opy_(bstack1l1lllll1_opy_):
  if bstack1l1lllll1_opy_ == bstack111111l_opy_ (u"ࠥࡨࡴࡴࡥࠣ࿦"):
    return bstack111111l_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡧࡳࡧࡨࡲࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡧࡳࡧࡨࡲࠧࡄࡃࡰ࡯ࡳࡰࡪࡺࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧ࿧")
  elif bstack1l1lllll1_opy_ == bstack111111l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ࿨"):
    return bstack111111l_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡴࡨࡨࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡲࡦࡦࠥࡂࡋࡧࡩ࡭ࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ࿩")
  elif bstack1l1lllll1_opy_ == bstack111111l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ࿪"):
    return bstack111111l_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽࡫ࡷ࡫ࡥ࡯࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥ࡫ࡷ࡫ࡥ࡯ࠤࡁࡔࡦࡹࡳࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ࿫")
  elif bstack1l1lllll1_opy_ == bstack111111l_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ࿬"):
    return bstack111111l_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡸࡥࡥ࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡶࡪࡪࠢ࠿ࡇࡵࡶࡴࡸ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬ࿭")
  elif bstack1l1lllll1_opy_ == bstack111111l_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧ࿮"):
    return bstack111111l_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࠤࡧࡨࡥ࠸࠸࠶࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࠦࡩࡪࡧ࠳࠳࠸ࠥࡂ࡙࡯࡭ࡦࡱࡸࡸࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ࿯")
  elif bstack1l1lllll1_opy_ == bstack111111l_opy_ (u"ࠨࡲࡶࡰࡱ࡭ࡳ࡭ࠢ࿰"):
    return bstack111111l_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࡕࡹࡳࡴࡩ࡯ࡩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ࿱")
  else:
    return bstack111111l_opy_ (u"ࠨ࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡧࡲࡡࡤ࡭࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡧࡲࡡࡤ࡭ࠥࡂࠬ࿲") + bstack1l11l1l111_opy_(
      bstack1l1lllll1_opy_) + bstack111111l_opy_ (u"ࠩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ࿳")
def bstack11llll1111_opy_(session):
  return bstack111111l_opy_ (u"ࠪࡀࡹࡸࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡳࡱࡺࠦࡃࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠠࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡰࡤࡱࡪࠨ࠾࠽ࡣࠣ࡬ࡷ࡫ࡦ࠾ࠤࡾࢁࠧࠦࡴࡢࡴࡪࡩࡹࡃࠢࡠࡤ࡯ࡥࡳࡱࠢ࠿ࡽࢀࡀ࠴ࡧ࠾࠽࠱ࡷࡨࡃࢁࡽࡼࡿ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁ࠵ࡴࡳࡀࠪ࿴").format(
    session[bstack111111l_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨ࿵")], bstack1l1lllll1l_opy_(session), bstack1llllll111_opy_(session[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡺࡡࡵࡷࡶࠫ࿶")]),
    bstack1llllll111_opy_(session[bstack111111l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭࿷")]),
    bstack1l11l1l111_opy_(session[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ࿸")] or session[bstack111111l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ࿹")] or bstack111111l_opy_ (u"ࠩࠪ࿺")) + bstack111111l_opy_ (u"ࠥࠤࠧ࿻") + (session[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭࿼")] or bstack111111l_opy_ (u"ࠬ࠭࿽")),
    session[bstack111111l_opy_ (u"࠭࡯ࡴࠩ࿾")] + bstack111111l_opy_ (u"ࠢࠡࠤ࿿") + session[bstack111111l_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬက")], session[bstack111111l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫခ")] or bstack111111l_opy_ (u"ࠪࠫဂ"),
    session[bstack111111l_opy_ (u"ࠫࡨࡸࡥࡢࡶࡨࡨࡤࡧࡴࠨဃ")] if session[bstack111111l_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩင")] else bstack111111l_opy_ (u"࠭ࠧစ"))
@measure(event_name=EVENTS.bstack111lll1l1l_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def bstack1ll11ll111_opy_(sessions, bstack11l11l1l11_opy_):
  try:
    bstack111lll111l_opy_ = bstack111111l_opy_ (u"ࠢࠣဆ")
    if not os.path.exists(bstack11ll111l11_opy_):
      os.mkdir(bstack11ll111l11_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack111111l_opy_ (u"ࠨࡣࡶࡷࡪࡺࡳ࠰ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭ဇ")), bstack111111l_opy_ (u"ࠩࡵࠫဈ")) as f:
      bstack111lll111l_opy_ = f.read()
    bstack111lll111l_opy_ = bstack111lll111l_opy_.replace(bstack111111l_opy_ (u"ࠪࡿࠪࡘࡅࡔࡗࡏࡘࡘࡥࡃࡐࡗࡑࡘࠪࢃࠧဉ"), str(len(sessions)))
    bstack111lll111l_opy_ = bstack111lll111l_opy_.replace(bstack111111l_opy_ (u"ࠫࢀࠫࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠧࢀࠫည"), bstack11l11l1l11_opy_)
    bstack111lll111l_opy_ = bstack111lll111l_opy_.replace(bstack111111l_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡎࡂࡏࡈࠩࢂ࠭ဋ"),
                                              sessions[0].get(bstack111111l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡴࡡ࡮ࡧࠪဌ")) if sessions[0] else bstack111111l_opy_ (u"ࠧࠨဍ"))
    with open(os.path.join(bstack11ll111l11_opy_, bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡳࡧࡳࡳࡷࡺ࠮ࡩࡶࡰࡰࠬဎ")), bstack111111l_opy_ (u"ࠩࡺࠫဏ")) as stream:
      stream.write(bstack111lll111l_opy_.split(bstack111111l_opy_ (u"ࠪࡿ࡙ࠪࡅࡔࡕࡌࡓࡓ࡙࡟ࡅࡃࡗࡅࠪࢃࠧတ"))[0])
      for session in sessions:
        stream.write(bstack11llll1111_opy_(session))
      stream.write(bstack111lll111l_opy_.split(bstack111111l_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨထ"))[1])
    logger.info(bstack111111l_opy_ (u"ࠬࡍࡥ࡯ࡧࡵࡥࡹ࡫ࡤࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡣࡷ࡬ࡰࡩࠦࡡࡳࡶ࡬ࡪࡦࡩࡴࡴࠢࡤࡸࠥࢁࡽࠨဒ").format(bstack11ll111l11_opy_));
  except Exception as e:
    logger.debug(bstack11llll1l1_opy_.format(str(e)))
def bstack111lll1lll_opy_(hashed_id):
  global CONFIG
  try:
    bstack1111ll111_opy_ = datetime.datetime.now()
    host = bstack111111l_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠱ࡨࡲ࡯ࡶࡦ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ဓ") if bstack111111l_opy_ (u"ࠧࡢࡲࡳࠫန") in CONFIG else bstack111111l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩပ")
    user = CONFIG[bstack111111l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫဖ")]
    key = CONFIG[bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ဗ")]
    bstack11lll1111l_opy_ = bstack111111l_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪဘ") if bstack111111l_opy_ (u"ࠬࡧࡰࡱࠩမ") in CONFIG else (bstack111111l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪယ") if CONFIG.get(bstack111111l_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫရ")) else bstack111111l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪလ"))
    host = bstack1lll1111l_opy_(cli.config, [bstack111111l_opy_ (u"ࠤࡤࡴ࡮ࡹࠢဝ"), bstack111111l_opy_ (u"ࠥࡥࡵࡶࡁࡶࡶࡲࡱࡦࡺࡥࠣသ"), bstack111111l_opy_ (u"ࠦࡦࡶࡩࠣဟ")], host) if bstack111111l_opy_ (u"ࠬࡧࡰࡱࠩဠ") in CONFIG else bstack1lll1111l_opy_(cli.config, [bstack111111l_opy_ (u"ࠨࡡࡱ࡫ࡶࠦအ"), bstack111111l_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࠤဢ"), bstack111111l_opy_ (u"ࠣࡣࡳ࡭ࠧဣ")], host)
    url = bstack111111l_opy_ (u"ࠩࡾࢁ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸ࡫ࡳࡴ࡫ࡲࡲࡸ࠴ࡪࡴࡱࡱࠫဤ").format(host, bstack11lll1111l_opy_, hashed_id)
    headers = {
      bstack111111l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩဥ"): bstack111111l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧဦ"),
    }
    proxies = bstack1l111111ll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࡫ࡪࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࡡ࡯࡭ࡸࡺࠢဧ"), datetime.datetime.now() - bstack1111ll111_opy_)
      return list(map(lambda session: session[bstack111111l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࠫဨ")], response.json()))
  except Exception as e:
    logger.debug(bstack1ll1l1111l_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack11ll1l111_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def get_build_link():
  global CONFIG
  global bstack1111l1lll_opy_
  try:
    if bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪဩ") in CONFIG:
      bstack1111ll111_opy_ = datetime.datetime.now()
      host = bstack111111l_opy_ (u"ࠨࡣࡳ࡭࠲ࡩ࡬ࡰࡷࡧࠫဪ") if bstack111111l_opy_ (u"ࠩࡤࡴࡵ࠭ါ") in CONFIG else bstack111111l_opy_ (u"ࠪࡥࡵ࡯ࠧာ")
      user = CONFIG[bstack111111l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ိ")]
      key = CONFIG[bstack111111l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨီ")]
      bstack11lll1111l_opy_ = bstack111111l_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬု") if bstack111111l_opy_ (u"ࠧࡢࡲࡳࠫူ") in CONFIG else bstack111111l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪေ")
      url = bstack111111l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡿࢂࡀࡻࡾࡂࡾࢁ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠲࡯ࡹ࡯࡯ࠩဲ").format(user, key, host, bstack11lll1111l_opy_)
      if cli.is_enabled(CONFIG):
        bstack11l11l1l11_opy_, hashed_id = cli.bstack1l111ll1l1_opy_()
        logger.info(bstack1111l1l111_opy_.format(bstack11l11l1l11_opy_))
        return [hashed_id, bstack11l11l1l11_opy_]
      else:
        headers = {
          bstack111111l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩဳ"): bstack111111l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧဴ"),
        }
        if bstack111111l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧဵ") in CONFIG:
          params = {bstack111111l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫံ"): CONFIG[bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧ့ࠪ")], bstack111111l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫး"): CONFIG[bstack111111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵ္ࠫ")]}
        else:
          params = {bstack111111l_opy_ (u"ࠪࡲࡦࡳࡥࠨ်"): CONFIG[bstack111111l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧျ")]}
        proxies = bstack1l111111ll_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack11l1111111_opy_ = response.json()[0][bstack111111l_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡥࡹ࡮ࡲࡤࠨြ")]
          if bstack11l1111111_opy_:
            bstack11l11l1l11_opy_ = bstack11l1111111_opy_[bstack111111l_opy_ (u"࠭ࡰࡶࡤ࡯࡭ࡨࡥࡵࡳ࡮ࠪွ")].split(bstack111111l_opy_ (u"ࠧࡱࡷࡥࡰ࡮ࡩ࠭ࡣࡷ࡬ࡰࡩ࠭ှ"))[0] + bstack111111l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡳ࠰ࠩဿ") + bstack11l1111111_opy_[
              bstack111111l_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ၀")]
            logger.info(bstack1111l1l111_opy_.format(bstack11l11l1l11_opy_))
            bstack1111l1lll_opy_ = bstack11l1111111_opy_[bstack111111l_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭၁")]
            bstack11111ll1l1_opy_ = CONFIG[bstack111111l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ၂")]
            if bstack111111l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ၃") in CONFIG:
              bstack11111ll1l1_opy_ += bstack111111l_opy_ (u"࠭ࠠࠨ၄") + CONFIG[bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ၅")]
            if bstack11111ll1l1_opy_ != bstack11l1111111_opy_[bstack111111l_opy_ (u"ࠨࡰࡤࡱࡪ࠭၆")]:
              logger.debug(bstack11ll11111l_opy_.format(bstack11l1111111_opy_[bstack111111l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ၇")], bstack11111ll1l1_opy_))
            cli.bstack11l1l1lll_opy_(bstack111111l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡩࡨࡸࡤࡨࡵࡪ࡮ࡧࡣࡱ࡯࡮࡬ࠤ၈"), datetime.datetime.now() - bstack1111ll111_opy_)
            return [bstack11l1111111_opy_[bstack111111l_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ၉")], bstack11l11l1l11_opy_]
    else:
      logger.warn(bstack11ll11l1l_opy_)
  except Exception as e:
    logger.debug(bstack1lllll1l1l_opy_.format(str(e)))
  return [None, None]
def bstack1111l1l11_opy_(url, bstack11ll1l1l11_opy_=False):
  global CONFIG
  global bstack11ll1ll11l_opy_
  if not bstack11ll1ll11l_opy_:
    hostname = bstack111ll11l1l_opy_(url)
    is_private = bstack111lll11l1_opy_(hostname)
    if (bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ၊") in CONFIG and not bstack1llll11lll_opy_(CONFIG[bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ။")])) and (is_private or bstack11ll1l1l11_opy_):
      bstack11ll1ll11l_opy_ = hostname
def bstack111ll11l1l_opy_(url):
  return urlparse(url).hostname
def bstack111lll11l1_opy_(hostname):
  for bstack1ll1l111ll_opy_ in bstack1l111ll11_opy_:
    regex = re.compile(bstack1ll1l111ll_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1l111lll1l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1ll11l1lll_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack111lll111_opy_
  bstack1lllllllll_opy_ = not (bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫ၌"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack111111l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ၍"), None))
  bstack1lll11ll1l_opy_ = getattr(driver, bstack111111l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩ၎"), None) != True
  bstack111lllll11_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ၏"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack111111l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ၐ"), None)
  if bstack111lllll11_opy_:
    if not bstack1ll1111l11_opy_():
      logger.warning(bstack111111l_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤၑ"))
      return {}
    logger.debug(bstack111111l_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪၒ"))
    logger.debug(perform_scan(driver, driver_command=bstack111111l_opy_ (u"ࠧࡦࡺࡨࡧࡺࡺࡥࡔࡥࡵ࡭ࡵࡺࠧၓ")))
    results = bstack1111ll1111_opy_(bstack111111l_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡴࠤၔ"))
    if results is not None and results.get(bstack111111l_opy_ (u"ࠤ࡬ࡷࡸࡻࡥࡴࠤၕ")) is not None:
        return results[bstack111111l_opy_ (u"ࠥ࡭ࡸࡹࡵࡦࡵࠥၖ")]
    logger.error(bstack111111l_opy_ (u"ࠦࡓࡵࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡓࡧࡶࡹࡱࡺࡳࠡࡹࡨࡶࡪࠦࡦࡰࡷࡱࡨ࠳ࠨၗ"))
    return []
  if not bstack1llll111l_opy_.bstack1l1l1l11l1_opy_(CONFIG, bstack111lll111_opy_) or (bstack1lll11ll1l_opy_ and bstack1lllllllll_opy_):
    logger.warning(bstack111111l_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹ࠮ࠣၘ"))
    return {}
  try:
    logger.debug(bstack111111l_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪၙ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack11l1llll11_opy_.bstack1ll111ll11_opy_)
    return results
  except Exception:
    logger.error(bstack111111l_opy_ (u"ࠢࡏࡱࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡼ࡫ࡲࡦࠢࡩࡳࡺࡴࡤ࠯ࠤၚ"))
    return {}
@measure(event_name=EVENTS.bstack1llll11111_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack111lll111_opy_
  bstack1lllllllll_opy_ = not (bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬၛ"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack111111l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨၜ"), None))
  bstack1lll11ll1l_opy_ = getattr(driver, bstack111111l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪၝ"), None) != True
  bstack111lllll11_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫၞ"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack111111l_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧၟ"), None)
  if bstack111lllll11_opy_:
    if not bstack1ll1111l11_opy_():
      logger.warning(bstack111111l_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻ࠱ࠦၠ"))
      return {}
    logger.debug(bstack111111l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡸࡻ࡭࡮ࡣࡵࡽࠬၡ"))
    logger.debug(perform_scan(driver, driver_command=bstack111111l_opy_ (u"ࠨࡧࡻࡩࡨࡻࡴࡦࡕࡦࡶ࡮ࡶࡴࠨၢ")))
    results = bstack1111ll1111_opy_(bstack111111l_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡕࡸࡱࡲࡧࡲࡺࠤၣ"))
    if results is not None and results.get(bstack111111l_opy_ (u"ࠥࡷࡺࡳ࡭ࡢࡴࡼࠦၤ")) is not None:
        return results[bstack111111l_opy_ (u"ࠦࡸࡻ࡭࡮ࡣࡵࡽࠧၥ")]
    logger.error(bstack111111l_opy_ (u"ࠧࡔ࡯ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡔࡨࡷࡺࡲࡴࡴࠢࡖࡹࡲࡳࡡࡳࡻࠣࡻࡦࡹࠠࡧࡱࡸࡲࡩ࠴ࠢၦ"))
    return {}
  if not bstack1llll111l_opy_.bstack1l1l1l11l1_opy_(CONFIG, bstack111lll111_opy_) or (bstack1lll11ll1l_opy_ and bstack1lllllllll_opy_):
    logger.warning(bstack111111l_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺ࠰ࠥၧ"))
    return {}
  try:
    logger.debug(bstack111111l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡸࡻ࡭࡮ࡣࡵࡽࠬၨ"))
    logger.debug(perform_scan(driver))
    bstack11l11l11l1_opy_ = driver.execute_async_script(bstack11l1llll11_opy_.bstack11lll11lll_opy_)
    return bstack11l11l11l1_opy_
  except Exception:
    logger.error(bstack111111l_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡻ࡭࡮ࡣࡵࡽࠥࡽࡡࡴࠢࡩࡳࡺࡴࡤ࠯ࠤၩ"))
    return {}
def bstack1ll1111l11_opy_():
  global CONFIG
  global bstack111lll111_opy_
  bstack1l1l1ll11l_opy_ = bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၪ"), None) and bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၫ"), None)
  if not bstack1llll111l_opy_.bstack1l1l1l11l1_opy_(CONFIG, bstack111lll111_opy_) or not bstack1l1l1ll11l_opy_:
        logger.warning(bstack111111l_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡵࡩࡸࡻ࡬ࡵࡵ࠱ࠦၬ"))
        return False
  return True
def bstack1111ll1111_opy_(bstack1111ll11l_opy_):
    bstack11lll1l1ll_opy_ = bstack1ll1l111_opy_.current_test_uuid() if bstack1ll1l111_opy_.current_test_uuid() else bstack1ll1l1ll_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack1l11111ll_opy_(bstack11lll1l1ll_opy_, bstack1111ll11l_opy_))
        try:
            return future.result(timeout=bstack1lll1lll1l_opy_)
        except TimeoutError:
            logger.error(bstack111111l_opy_ (u"࡚ࠧࡩ࡮ࡧࡲࡹࡹࠦࡡࡧࡶࡨࡶࠥࢁࡽࡴࠢࡺ࡬࡮ࡲࡥࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡖࡪࡹࡵ࡭ࡶࡶࠦၭ").format(bstack1lll1lll1l_opy_))
        except Exception as ex:
            logger.debug(bstack111111l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡸࡥࡵࡴ࡬ࡩࡻ࡯࡮ࡨࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡿࢂ࠴ࠠࡆࡴࡵࡳࡷࠦ࠭ࠡࡽࢀࠦၮ").format(bstack1111ll11l_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack11lll1llll_opy_, stage=STAGE.bstack11l11ll11_opy_, bstack1l111l1ll_opy_=bstack1l11llll1_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack111lll111_opy_
  bstack1lllllllll_opy_ = not (bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫၯ"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack111111l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧၰ"), None))
  bstack11l111ll1l_opy_ = not (bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၱ"), None) and bstack1lll111l_opy_(
          threading.current_thread(), bstack111111l_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၲ"), None))
  bstack1lll11ll1l_opy_ = getattr(driver, bstack111111l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫၳ"), None) != True
  if not bstack1llll111l_opy_.bstack1l1l1l11l1_opy_(CONFIG, bstack111lll111_opy_) or (bstack1lll11ll1l_opy_ and bstack1lllllllll_opy_ and bstack11l111ll1l_opy_):
    logger.warning(bstack111111l_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷࡻ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳ࠴ࠢၴ"))
    return {}
  try:
    bstack1l11l1lll_opy_ = bstack111111l_opy_ (u"࠭ࡡࡱࡲࠪၵ") in CONFIG and CONFIG.get(bstack111111l_opy_ (u"ࠧࡢࡲࡳࠫၶ"), bstack111111l_opy_ (u"ࠨࠩၷ"))
    session_id = getattr(driver, bstack111111l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩ࠭ၸ"), None)
    if not session_id:
      logger.warning(bstack111111l_opy_ (u"ࠥࡒࡴࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࠣࡪࡴࡻ࡮ࡥࠢࡩࡳࡷࠦࡤࡳ࡫ࡹࡩࡷࠨၹ"))
      return {bstack111111l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥၺ"): bstack111111l_opy_ (u"ࠧࡔ࡯ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡌࡈࠥ࡬࡯ࡶࡰࡧࠦၻ")}
    if bstack1l11l1lll_opy_:
      try:
        bstack1l111l11l1_opy_ = {
              bstack111111l_opy_ (u"࠭ࡴࡩࡌࡺࡸ࡙ࡵ࡫ࡦࡰࠪၼ"): os.environ.get(bstack111111l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬၽ"), os.environ.get(bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬၾ"), bstack111111l_opy_ (u"ࠩࠪၿ"))),
              bstack111111l_opy_ (u"ࠪࡸ࡭࡚ࡥࡴࡶࡕࡹࡳ࡛ࡵࡪࡦࠪႀ"): bstack1ll1l111_opy_.current_test_uuid() if bstack1ll1l111_opy_.current_test_uuid() else bstack1ll1l1ll_opy_.current_hook_uuid(),
              bstack111111l_opy_ (u"ࠫࡦࡻࡴࡩࡊࡨࡥࡩ࡫ࡲࠨႁ"): os.environ.get(bstack111111l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪႂ")),
              bstack111111l_opy_ (u"࠭ࡳࡤࡣࡱࡘ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ႃ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack111111l_opy_ (u"ࠧࡵࡪࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬႄ"): os.environ.get(bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ႅ"), bstack111111l_opy_ (u"ࠩࠪႆ")),
              bstack111111l_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪႇ"): kwargs.get(bstack111111l_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣࡨࡵ࡭࡮ࡣࡱࡨࠬႈ"), None) or bstack111111l_opy_ (u"ࠬ࠭ႉ")
          }
        if not hasattr(thread_local, bstack111111l_opy_ (u"࠭ࡢࡢࡵࡨࡣࡦࡶࡰࡠࡣ࠴࠵ࡾࡥࡳࡤࡴ࡬ࡴࡹ࠭ႊ")):
            scripts = {bstack111111l_opy_ (u"ࠧࡴࡥࡤࡲࠬႋ"): bstack11l1llll11_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack11l1lllll1_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack11l1lllll1_opy_[bstack111111l_opy_ (u"ࠨࡵࡦࡥࡳ࠭ႌ")] = bstack11l1lllll1_opy_[bstack111111l_opy_ (u"ࠩࡶࡧࡦࡴႍࠧ")] % json.dumps(bstack1l111l11l1_opy_)
        bstack11l1llll11_opy_.bstack1l1llll11l_opy_(bstack11l1lllll1_opy_)
        bstack11l1llll11_opy_.store()
        bstack11l111111_opy_ = driver.execute_script(bstack11l1llll11_opy_.perform_scan)
      except Exception as bstack111l11111l_opy_:
        logger.info(bstack111111l_opy_ (u"ࠥࡅࡵࡶࡩࡶ࡯ࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡨࡧ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢࠥႎ") + str(bstack111l11111l_opy_))
        bstack11l111111_opy_ = {bstack111111l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥႏ"): str(bstack111l11111l_opy_)}
    else:
      bstack11l111111_opy_ = driver.execute_async_script(bstack11l1llll11_opy_.perform_scan, {bstack111111l_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࠬ႐"): kwargs.get(bstack111111l_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷࡥࡣࡰ࡯ࡰࡥࡳࡪࠧ႑"), None) or bstack111111l_opy_ (u"ࠧࠨ႒")})
    return bstack11l111111_opy_
  except Exception as err:
    logger.error(bstack111111l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡷࡻ࡮ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳ࠴ࠠࡼࡿࠥ႓").format(str(err)))
    return {}