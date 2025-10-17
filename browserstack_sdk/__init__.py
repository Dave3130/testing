# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
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
from browserstack_sdk.bstack11l1l111l1_opy_ import bstack11l1lll1l1_opy_
from browserstack_sdk.bstack1lll1l11l_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack11lll1l111_opy_():
  global CONFIG
  headers = {
        bstack11l111_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬ৳"): bstack11l111_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ৴"),
      }
  proxies = bstack1llllll11l_opy_(CONFIG, bstack11lllll1ll_opy_)
  try:
    response = requests.get(bstack11lllll1ll_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack11l1l11lll_opy_ = response.json()[bstack11l111_opy_ (u"ࠨࡪࡸࡦࡸ࠭৵")]
      logger.debug(bstack1l111lll11_opy_.format(response.json()))
      return bstack11l1l11lll_opy_
    else:
      logger.debug(bstack111l11l111_opy_.format(bstack11l111_opy_ (u"ࠤࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡏ࡙ࡏࡏࠢࡳࡥࡷࡹࡥࠡࡧࡵࡶࡴࡸࠠࠣ৶")))
  except Exception as e:
    logger.debug(bstack111l11l111_opy_.format(e))
def bstack1l111ll1l1_opy_(hub_url):
  global CONFIG
  url = bstack11l111_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧ৷")+  hub_url + bstack11l111_opy_ (u"ࠦ࠴ࡩࡨࡦࡥ࡮ࠦ৸")
  headers = {
        bstack11l111_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫ৹"): bstack11l111_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ৺"),
      }
  proxies = bstack1llllll11l_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1l1ll1ll1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1l1ll1l1ll_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack11ll1ll1l_opy_, stage=STAGE.bstack1l111l11l_opy_)
def bstack11l11ll111_opy_():
  try:
    global bstack11111llll1_opy_
    bstack11l1l11lll_opy_ = bstack11lll1l111_opy_()
    bstack1ll11ll1ll_opy_ = []
    results = []
    for bstack11l11l111_opy_ in bstack11l1l11lll_opy_:
      bstack1ll11ll1ll_opy_.append(bstack111l11ll1l_opy_(target=bstack1l111ll1l1_opy_,args=(bstack11l11l111_opy_,)))
    for t in bstack1ll11ll1ll_opy_:
      t.start()
    for t in bstack1ll11ll1ll_opy_:
      results.append(t.join())
    bstack1ll111l11_opy_ = {}
    for item in results:
      hub_url = item[bstack11l111_opy_ (u"ࠧࡩࡷࡥࡣࡺࡸ࡬ࠨ৻")]
      latency = item[bstack11l111_opy_ (u"ࠨ࡮ࡤࡸࡪࡴࡣࡺࠩৼ")]
      bstack1ll111l11_opy_[hub_url] = latency
    bstack111l1ll11l_opy_ = min(bstack1ll111l11_opy_, key= lambda x: bstack1ll111l11_opy_[x])
    bstack11111llll1_opy_ = bstack111l1ll11l_opy_
    logger.debug(bstack1lll11l1l1_opy_.format(bstack111l1ll11l_opy_))
  except Exception as e:
    logger.debug(bstack1l11l11lll_opy_.format(e))
from browserstack_sdk.bstack11111l11_opy_ import *
from browserstack_sdk.bstack111l1lll_opy_ import *
from browserstack_sdk.bstack11l1l1ll_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack1lll11ll11_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack111ll111ll_opy_, stage=STAGE.bstack1l111l11l_opy_)
def bstack111l1l1l11_opy_():
    global bstack11111llll1_opy_
    try:
        bstack1l1ll1l11l_opy_ = bstack111lllllll_opy_()
        bstack1ll1lllll_opy_(bstack1l1ll1l11l_opy_)
        hub_url = bstack1l1ll1l11l_opy_.get(bstack11l111_opy_ (u"ࠤࡸࡶࡱࠨ৽"), bstack11l111_opy_ (u"ࠥࠦ৾"))
        if hub_url.endswith(bstack11l111_opy_ (u"ࠫ࠴ࡽࡤ࠰ࡪࡸࡦࠬ৿")):
            hub_url = hub_url.rsplit(bstack11l111_opy_ (u"ࠬ࠵ࡷࡥ࠱࡫ࡹࡧ࠭਀"), 1)[0]
        if hub_url.startswith(bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࠧਁ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack11l111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࠩਂ")):
            hub_url = hub_url[8:]
        bstack11111llll1_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack111lllllll_opy_():
    global CONFIG
    bstack11ll1l11l1_opy_ = CONFIG.get(bstack11l111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࡔࡶࡴࡪࡱࡱࡷࠬਃ"), {}).get(bstack11l111_opy_ (u"ࠩࡪࡶ࡮ࡪࡎࡢ࡯ࡨࠫ਄"), bstack11l111_opy_ (u"ࠪࡒࡔࡥࡇࡓࡋࡇࡣࡓࡇࡍࡆࡡࡓࡅࡘ࡙ࡅࡅࠩਅ"))
    if not isinstance(bstack11ll1l11l1_opy_, str):
        raise ValueError(bstack11l111_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡋࡷ࡯ࡤࠡࡰࡤࡱࡪࠦ࡭ࡶࡵࡷࠤࡧ࡫ࠠࡢࠢࡹࡥࡱ࡯ࡤࠡࡵࡷࡶ࡮ࡴࡧࠣਆ"))
    try:
        bstack1l1ll1l11l_opy_ = bstack1ll1l1l1l1_opy_(bstack11ll1l11l1_opy_)
        return bstack1l1ll1l11l_opy_
    except Exception as e:
        logger.error(bstack11l111_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡨࡴ࡬ࡨࠥࡪࡥࡵࡣ࡬ࡰࡸࠦ࠺ࠡࡽࢀࠦਇ").format(str(e)))
        return {}
def bstack1ll1l1l1l1_opy_(bstack11ll1l11l1_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack11l111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨਈ")] or not CONFIG[bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪਉ")]:
            raise ValueError(bstack11l111_opy_ (u"ࠣࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡷࡶࡩࡷࡴࡡ࡮ࡧࠣࡳࡷࠦࡡࡤࡥࡨࡷࡸࠦ࡫ࡦࡻࠥਊ"))
        url = bstack11l11l1lll_opy_ + bstack11ll1l11l1_opy_
        auth = (CONFIG[bstack11l111_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ਋")], CONFIG[bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭਌")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack11l1l1ll1_opy_ = json.loads(response.text)
            return bstack11l1l1ll1_opy_
    except ValueError as ve:
        logger.error(bstack11l111_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡨࡴ࡬ࡨࠥࡪࡥࡵࡣ࡬ࡰࡸࠦ࠺ࠡࡽࢀࠦ਍").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack11l111_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡩࡵ࡭ࡩࠦࡤࡦࡶࡤ࡭ࡱࡹࠠ࠻ࠢࡾࢁࠧ਎").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1ll1lllll_opy_(bstack1ll1l1111l_opy_):
    global CONFIG
    if bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪਏ") not in CONFIG or str(CONFIG[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫਐ")]).lower() == bstack11l111_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ਑"):
        CONFIG[bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨ਒")] = False
    elif bstack11l111_opy_ (u"ࠪ࡭ࡸ࡚ࡲࡪࡣ࡯ࡋࡷ࡯ࡤࠨਓ") in bstack1ll1l1111l_opy_:
        bstack1ll1l11ll_opy_ = CONFIG.get(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨਔ"), {})
        logger.debug(bstack11l111_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡾࡩࡴࡶ࡬ࡲ࡬ࠦ࡬ࡰࡥࡤࡰࠥࡵࡰࡵ࡫ࡲࡲࡸࡀࠠࠦࡵࠥਕ"), bstack1ll1l11ll_opy_)
        bstack1lll11l1ll_opy_ = bstack1ll1l1111l_opy_.get(bstack11l111_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲࡘࡥࡱࡧࡤࡸࡪࡸࡳࠣਖ"), [])
        bstack1l11l111l1_opy_ = bstack11l111_opy_ (u"ࠢ࠭ࠤਗ").join(bstack1lll11l1ll_opy_)
        logger.debug(bstack11l111_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡄࡷࡶࡸࡴࡳࠠࡳࡧࡳࡩࡦࡺࡥࡳࠢࡶࡸࡷ࡯࡮ࡨ࠼ࠣࠩࡸࠨਘ"), bstack1l11l111l1_opy_)
        bstack1l111111l1_opy_ = {
            bstack11l111_opy_ (u"ࠤ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦਙ"): bstack11l111_opy_ (u"ࠥࡥࡹࡹ࠭ࡳࡧࡳࡩࡦࡺࡥࡳࠤਚ"),
            bstack11l111_opy_ (u"ࠦ࡫ࡵࡲࡤࡧࡏࡳࡨࡧ࡬ࠣਛ"): bstack11l111_opy_ (u"ࠧࡺࡲࡶࡧࠥਜ"),
            bstack11l111_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࠳ࡲࡦࡲࡨࡥࡹ࡫ࡲࠣਝ"): bstack1l11l111l1_opy_
        }
        bstack1ll1l11ll_opy_.update(bstack1l111111l1_opy_)
        logger.debug(bstack11l111_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡕࡱࡦࡤࡸࡪࡪࠠ࡭ࡱࡦࡥࡱࠦ࡯ࡱࡶ࡬ࡳࡳࡹ࠺ࠡࠧࡶࠦਞ"), bstack1ll1l11ll_opy_)
        CONFIG[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬਟ")] = bstack1ll1l11ll_opy_
        logger.debug(bstack11l111_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡈ࡬ࡲࡦࡲࠠࡄࡑࡑࡊࡎࡍ࠺ࠡࠧࡶࠦਠ"), CONFIG)
def bstack1111l1111l_opy_():
    bstack1l1ll1l11l_opy_ = bstack111lllllll_opy_()
    if not bstack1l1ll1l11l_opy_[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࡕࡳ࡮ࠪਡ")]:
      raise ValueError(bstack11l111_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡖࡴ࡯ࠤ࡮ࡹࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡨࡵࡳࡲࠦࡧࡳ࡫ࡧࠤࡩ࡫ࡴࡢ࡫࡯ࡷ࠳ࠨਢ"))
    return bstack1l1ll1l11l_opy_[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡗࡵࡰࠬਣ")] + bstack11l111_opy_ (u"࠭࠿ࡤࡣࡳࡷࡂ࠭ਤ")
@measure(event_name=EVENTS.bstack1llll111l1_opy_, stage=STAGE.bstack1l111l11l_opy_)
def bstack1lll1llll1_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack11l111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩਥ")], CONFIG[bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫਦ")])
        url = bstack1l1llll11_opy_
        logger.debug(bstack11l111_opy_ (u"ࠤࡄࡸࡹ࡫࡭ࡱࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡤࡸ࡭ࡱࡪࡳࠡࡨࡵࡳࡲࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯࡚ࠥࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠢࡄࡔࡎࠨਧ"))
        try:
            response = requests.get(url, auth=auth, headers={bstack11l111_opy_ (u"ࠥࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠤਨ"): bstack11l111_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠢ਩")})
            if response.status_code == 200:
                bstack111l11llll_opy_ = json.loads(response.text)
                bstack1l1ll1l1l1_opy_ = bstack111l11llll_opy_.get(bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡷࠬਪ"), [])
                if bstack1l1ll1l1l1_opy_:
                    bstack1l1l1ll1l1_opy_ = bstack1l1ll1l1l1_opy_[0]
                    build_hashed_id = bstack1l1l1ll1l1_opy_.get(bstack11l111_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩਫ"))
                    bstack11lllll111_opy_ = bstack1l1lll111l_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack11lllll111_opy_])
                    logger.info(bstack11lll11l11_opy_.format(bstack11lllll111_opy_))
                    bstack11llll111_opy_ = CONFIG[bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪਬ")]
                    if bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪਭ") in CONFIG:
                      bstack11llll111_opy_ += bstack11l111_opy_ (u"ࠩࠣࠫਮ") + CONFIG[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬਯ")]
                    if bstack11llll111_opy_ != bstack1l1l1ll1l1_opy_.get(bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩਰ")):
                      logger.debug(bstack11l111111_opy_.format(bstack1l1l1ll1l1_opy_.get(bstack11l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ਱")), bstack11llll111_opy_))
                    return result
                else:
                    logger.debug(bstack11l111_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡔ࡯ࠡࡤࡸ࡭ࡱࡪࡳࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡸ࡭࡫ࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠰ࠥਲ"))
            else:
                logger.debug(bstack11l111_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡤࡸ࡭ࡱࡪࡳ࠯ࠤਲ਼"))
        except Exception as e:
            logger.error(bstack11l111_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࡵࠣ࠾ࠥࢁࡽࠣ਴").format(str(e)))
    else:
        logger.debug(bstack11l111_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡅࡒࡒࡋࡏࡇࠡ࡫ࡶࠤࡳࡵࡴࠡࡵࡨࡸ࠳ࠦࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡤࡸ࡭ࡱࡪࡳ࠯ࠤਵ"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1l1l111ll_opy_ import bstack1l1l111ll_opy_, Events, bstack1l1lll1l1_opy_, bstack11l11ll11l_opy_
from bstack_utils.measure import bstack1ll1111111_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1llll1l1ll_opy_ import bstack1l1llll11l_opy_
from bstack_utils.messages import *
from bstack_utils import bstack1lll11ll11_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1l1l11l1l1_opy_, bstack11ll11ll1l_opy_, bstack111l11l1l_opy_, bstack1l11lll1_opy_, \
  bstack1ll1l1l1ll_opy_, \
  Notset, bstack1l11ll1ll1_opy_, \
  bstack11l11ll11_opy_, bstack1l11ll111_opy_, bstack11l111lll_opy_, bstack1l11l111l_opy_, bstack11llll1l11_opy_, bstack1llll11l11_opy_, \
  bstack1l1111l1ll_opy_, \
  bstack11llllll11_opy_, bstack1l1l1llll1_opy_, bstack11ll11lll1_opy_, bstack111lll1l1l_opy_, \
  bstack11l11l1l1_opy_, bstack1ll1l1llll_opy_, bstack11lll1lll_opy_, bstack111lll1111_opy_
from bstack_utils.bstack11l111l11l_opy_ import bstack11ll1l1l1_opy_
from bstack_utils.bstack11l1ll1ll_opy_ import bstack11ll11l1l_opy_, bstack1lllll11l1_opy_
from bstack_utils.bstack1l1l111ll1_opy_ import bstack111l1lll1l_opy_
from bstack_utils.bstack1lll1111l_opy_ import bstack1ll1ll1l11_opy_, bstack1l11l11ll_opy_
from bstack_utils.bstack1l1l1ll111_opy_ import bstack1l1l1ll111_opy_
from bstack_utils.bstack111l11111l_opy_ import bstack11l111l111_opy_
from bstack_utils.proxy import bstack1111111ll_opy_, bstack1llllll11l_opy_, bstack11111ll11l_opy_, bstack11lll111l_opy_
from bstack_utils.bstack11l1111l11_opy_ import bstack1ll11l111_opy_
import bstack_utils.bstack1l1ll1l11_opy_ as bstack111ll1l11_opy_
import bstack_utils.bstack11l11lll1l_opy_ as bstack11111ll111_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack11lll1l1l_opy_ import bstack1l11l1ll1_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack1llllllll_opy_
from bstack_utils.bstack1ll11111ll_opy_ import bstack1111ll111l_opy_
if os.getenv(bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡐࡎࡥࡈࡐࡑࡎࡗࠬਸ਼")):
  cli.bstack1l1l11l11_opy_()
else:
  os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡉࡑࡒࡏࡘ࠭਷")] = bstack11l111_opy_ (u"ࠬࡺࡲࡶࡧࠪਸ")
bstack11lll1lll1_opy_ = bstack11l111_opy_ (u"࠭ࠠࠡ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳࠦࠠࡪࡨࠫࡴࡦ࡭ࡥࠡ࠿ࡀࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮ࠦࡻ࡝ࡰࠣࠤࠥࡺࡲࡺࡽ࡟ࡲࠥࡩ࡯࡯ࡵࡷࠤ࡫ࡹࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࡠࠬ࡬ࡳ࡝ࠩࠬ࠿ࡡࡴࠠࠡࠢࠣࠤ࡫ࡹ࠮ࡢࡲࡳࡩࡳࡪࡆࡪ࡮ࡨࡗࡾࡴࡣࠩࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭࠲ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡲࡢ࡭ࡳࡪࡥࡹࠫࠣ࠯ࠥࠨ࠺ࠣࠢ࠮ࠤࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࠫࡥࡼࡧࡩࡵࠢࡱࡩࡼࡖࡡࡨࡧ࠵࠲ࡪࡼࡡ࡭ࡷࡤࡸࡪ࠮ࠢࠩࠫࠣࡁࡃࠦࡻࡾࠤ࠯ࠤࡡ࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡧࡦࡶࡖࡩࡸࡹࡩࡰࡰࡇࡩࡹࡧࡩ࡭ࡵࠥࢁࡡ࠭ࠩࠪࠫ࡞ࠦ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠢ࡞ࠫࠣ࠯ࠥࠨࠬ࡝࡞ࡱࠦ࠮ࡢ࡮ࠡࠢࠣࠤࢂࡩࡡࡵࡥ࡫ࠬࡪࡾࠩࡼ࡞ࡱࠤࠥࠦࠠࡾ࡞ࡱࠤࠥࢃ࡜࡯ࠢࠣ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴࠭ਹ")
bstack11l1l1lll_opy_ = bstack11l111_opy_ (u"ࠧ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡶࡡࡵࡪࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹࡝࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡥࡤࡴࡸࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠳ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡵࡥࡩ࡯ࡦࡨࡼࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠳࡟࡟ࡲࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡸࡲࡩࡤࡧࠫ࠴࠱ࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴ࠫ࡟ࡲࡨࡵ࡮ࡴࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫ࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤࠬ࠿ࡡࡴࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴࡬ࡢࡷࡱࡧ࡭ࠦ࠽ࠡࡣࡶࡽࡳࡩࠠࠩ࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠪࠢࡀࡂࠥࢁ࡜࡯࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࡠࡳࡺࡲࡺࠢࡾࡠࡳࡩࡡࡱࡵࠣࡁࠥࡐࡓࡐࡐ࠱ࡴࡦࡸࡳࡦࠪࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠩ࡝ࡰࠣࠤࢂࠦࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࠢࡾࡠࡳࠦࠠࠡࠢࢀࡠࡳࠦࠠࡳࡧࡷࡹࡷࡴࠠࡢࡹࡤ࡭ࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮࠲ࡨ࡮ࡲࡰ࡯࡬ࡹࡲ࠴ࡣࡰࡰࡱࡩࡨࡺࠨࡼ࡞ࡱࠤࠥࠦࠠࡸࡵࡈࡲࡩࡶ࡯ࡪࡰࡷ࠾ࠥࡦࡷࡴࡵ࠽࠳࠴ࡩࡤࡱ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡁࡦࡥࡵࡹ࠽ࠥࡽࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩࡾࡢ࠯ࡠࡳࠦࠠࠡࠢ࠱࠲࠳ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷࡡࡴࠠࠡࡿࠬࡠࡳࢃ࡜࡯࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࡠࡳ࠭਺")
from ._version import __version__
bstack1l1l11111_opy_ = None
CONFIG = {}
bstack1ll111ll1l_opy_ = {}
bstack111ll11l1l_opy_ = {}
bstack1lll1ll11l_opy_ = None
bstack111l1ll1l1_opy_ = None
bstack1111llll11_opy_ = None
bstack11l1llll1_opy_ = -1
bstack1lll111l1_opy_ = 0
bstack11lllllll1_opy_ = bstack1llll11lll_opy_
bstack11l1l1l1l1_opy_ = 1
bstack1ll11ll111_opy_ = False
bstack1l1ll11l1l_opy_ = False
bstack1ll1ll1l1l_opy_ = bstack11l111_opy_ (u"ࠨࠩ਻")
bstack1l1111lll_opy_ = bstack11l111_opy_ (u"਼ࠩࠪ")
bstack1lll1l1l11_opy_ = False
bstack1l1111l11_opy_ = True
bstack11l11111l1_opy_ = bstack11l111_opy_ (u"ࠪࠫ਽")
bstack1l111ll1ll_opy_ = []
bstack11l1111ll1_opy_ = threading.Lock()
bstack1l1l1lll11_opy_ = threading.Lock()
bstack11111llll1_opy_ = bstack11l111_opy_ (u"ࠫࠬਾ")
bstack1ll11l11l1_opy_ = False
bstack1l111l1lll_opy_ = None
bstack11ll111l1_opy_ = None
bstack11l11l11l1_opy_ = None
bstack11ll111111_opy_ = -1
bstack1l1ll1lll_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠬࢄࠧਿ")), bstack11l111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ੀ"), bstack11l111_opy_ (u"ࠧ࠯ࡴࡲࡦࡴࡺ࠭ࡳࡧࡳࡳࡷࡺ࠭ࡩࡧ࡯ࡴࡪࡸ࠮࡫ࡵࡲࡲࠬੁ"))
bstack11l11ll1l1_opy_ = 0
bstack111l1ll111_opy_ = 0
bstack11111l1l1_opy_ = []
bstack1l1l1l111_opy_ = []
bstack1l111lllll_opy_ = []
bstack11lll1ll1l_opy_ = []
bstack1111ll111_opy_ = bstack11l111_opy_ (u"ࠨࠩੂ")
bstack1l1l11l1ll_opy_ = bstack11l111_opy_ (u"ࠩࠪ੃")
bstack11l1ll1lll_opy_ = False
bstack1lllll111l_opy_ = False
bstack1l1ll1l1l_opy_ = {}
bstack1ll1lllll1_opy_ = None
bstack11l11lll1_opy_ = None
bstack1111llllll_opy_ = None
bstack11ll1lll11_opy_ = None
bstack11l1llll1l_opy_ = None
bstack11l1l11111_opy_ = None
bstack11l1l11l1l_opy_ = None
bstack1lll111ll1_opy_ = None
bstack1l1llll1l_opy_ = None
bstack1111l11111_opy_ = None
bstack11lll1111l_opy_ = None
bstack1ll111llll_opy_ = None
bstack111l1l111_opy_ = None
bstack11l11l11ll_opy_ = None
bstack11l111ll11_opy_ = None
bstack111llll1l_opy_ = None
bstack11ll11llll_opy_ = None
bstack1l11l11ll1_opy_ = None
bstack1ll111l11l_opy_ = None
bstack11llllllll_opy_ = None
bstack1l11111l1_opy_ = None
bstack1111l1l1l1_opy_ = None
bstack1lll11111l_opy_ = None
thread_local = threading.local()
bstack1llll1111l_opy_ = False
bstack11ll1l1111_opy_ = bstack11l111_opy_ (u"ࠥࠦ੄")
logger = bstack1lll11ll11_opy_.get_logger(__name__, bstack11lllllll1_opy_)
bstack111ll111_opy_ = Config.bstack111ll1ll_opy_()
percy = bstack1ll1l1ll1l_opy_()
bstack11l1l1ll11_opy_ = bstack1l1llll11l_opy_()
bstack11lll11ll1_opy_ = bstack11l1l1ll_opy_()
def bstack1l1lll1ll_opy_():
  global CONFIG
  global bstack11l1ll1lll_opy_
  global bstack111ll111_opy_
  testContextOptions = bstack1l1l1l1lll_opy_(CONFIG)
  if bstack1ll1l1l1ll_opy_(CONFIG):
    if (bstack11l111_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭੅") in testContextOptions and str(testContextOptions[bstack11l111_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ੆")]).lower() == bstack11l111_opy_ (u"࠭ࡴࡳࡷࡨࠫੇ")):
      bstack11l1ll1lll_opy_ = True
    bstack111ll111_opy_.bstack1lll1l1111_opy_(testContextOptions.get(bstack11l111_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫੈ"), False))
  else:
    bstack11l1ll1lll_opy_ = True
    bstack111ll111_opy_.bstack1lll1l1111_opy_(True)
def bstack11ll1ll111_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1l11l1l11l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack11ll11lll_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11l111_opy_ (u"ࠣ࠯࠰ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡥࡲࡲ࡫࡯ࡧࡧ࡫࡯ࡩࠧ੉") == args[i].lower() or bstack11l111_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡴࡦࡪࡩࠥ੊") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack11l11111l1_opy_
      bstack11l11111l1_opy_ += bstack11l111_opy_ (u"ࠪ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࡉ࡭ࡱ࡫ࠠࠨੋ") + shlex.quote(path)
      return path
  return None
bstack111l11l11l_opy_ = re.compile(bstack11l111_opy_ (u"ࡶࠧ࠴ࠪࡀ࡞ࠧࡿ࠭࠴ࠪࡀࠫࢀ࠲࠯ࡅࠢੌ"))
def bstack11l11l111l_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack111l11l11l_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11l111_opy_ (u"ࠧࠪࡻ੍ࠣ") + group + bstack11l111_opy_ (u"ࠨࡽࠣ੎"), os.environ.get(group))
  return value
def bstack1l1lllll1l_opy_():
  global bstack1lll11111l_opy_
  if bstack1lll11111l_opy_ is None:
        bstack1lll11111l_opy_ = bstack11ll11lll_opy_()
  bstack1l1l1ll11_opy_ = bstack1lll11111l_opy_
  if bstack1l1l1ll11_opy_ and os.path.exists(os.path.abspath(bstack1l1l1ll11_opy_)):
    fileName = bstack1l1l1ll11_opy_
  if bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌࡥࡆࡊࡎࡈࠫ੏") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬ੐")])) and not bstack11l111_opy_ (u"ࠩࡩ࡭ࡱ࡫ࡎࡢ࡯ࡨࠫੑ") in locals():
    fileName = os.environ[bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧ੒")]
  if bstack11l111_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࠭੓") in locals():
    bstack11ll11_opy_ = os.path.abspath(fileName)
  else:
    bstack11ll11_opy_ = bstack11l111_opy_ (u"ࠬ࠭੔")
  bstack11l11111ll_opy_ = os.getcwd()
  bstack111lll1l1_opy_ = bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩ੕")
  bstack1l111l11l1_opy_ = bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹࡢ࡯࡯ࠫ੖")
  while (not os.path.exists(bstack11ll11_opy_)) and bstack11l11111ll_opy_ != bstack11l111_opy_ (u"ࠣࠤ੗"):
    bstack11ll11_opy_ = os.path.join(bstack11l11111ll_opy_, bstack111lll1l1_opy_)
    if not os.path.exists(bstack11ll11_opy_):
      bstack11ll11_opy_ = os.path.join(bstack11l11111ll_opy_, bstack1l111l11l1_opy_)
    if bstack11l11111ll_opy_ != os.path.dirname(bstack11l11111ll_opy_):
      bstack11l11111ll_opy_ = os.path.dirname(bstack11l11111ll_opy_)
    else:
      bstack11l11111ll_opy_ = bstack11l111_opy_ (u"ࠤࠥ੘")
  bstack1lll11111l_opy_ = bstack11ll11_opy_ if os.path.exists(bstack11ll11_opy_) else None
  return bstack1lll11111l_opy_
def bstack1lll111lll_opy_(config):
    if bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࠪਖ਼") in config:
      config[bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨਗ਼")] = config[bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠬਜ਼")]
    if bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬ࡕࡰࡵ࡫ࡲࡲࡸ࠭ੜ") in config:
      config[bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ੝")] = config[bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࡐࡲࡷ࡭ࡴࡴࡳࠨਫ਼")]
def bstack1l11lll1l_opy_():
  bstack11ll11_opy_ = bstack1l1lllll1l_opy_()
  if not os.path.exists(bstack11ll11_opy_):
    bstack1l111l1ll1_opy_(
      bstack11lll111ll_opy_.format(os.getcwd()))
  try:
    with open(bstack11ll11_opy_, bstack11l111_opy_ (u"ࠩࡵࠫ੟")) as stream:
      yaml.add_implicit_resolver(bstack11l111_opy_ (u"ࠥࠥࡵࡧࡴࡩࡧࡻࠦ੠"), bstack111l11l11l_opy_)
      yaml.add_constructor(bstack11l111_opy_ (u"ࠦࠦࡶࡡࡵࡪࡨࡼࠧ੡"), bstack11l11l111l_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1lll111lll_opy_(config)
      return config
  except:
    with open(bstack11ll11_opy_, bstack11l111_opy_ (u"ࠬࡸࠧ੢")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1lll111lll_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1l111l1ll1_opy_(bstack1lll1ll1ll_opy_.format(str(exc)))
def bstack111l111lll_opy_(config):
  bstack111l1111ll_opy_ = bstack1lllll1ll1_opy_(config)
  for option in list(bstack111l1111ll_opy_):
    if option.lower() in bstack11ll1l11l_opy_ and option != bstack11ll1l11l_opy_[option.lower()]:
      bstack111l1111ll_opy_[bstack11ll1l11l_opy_[option.lower()]] = bstack111l1111ll_opy_[option]
      del bstack111l1111ll_opy_[option]
  return config
def bstack111l1l11ll_opy_():
  global bstack111ll11l1l_opy_
  for key, bstack111lll11l1_opy_ in bstack11111l11ll_opy_.items():
    if isinstance(bstack111lll11l1_opy_, list):
      for var in bstack111lll11l1_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack111ll11l1l_opy_[key] = os.environ[var]
          break
    elif bstack111lll11l1_opy_ in os.environ and os.environ[bstack111lll11l1_opy_] and str(os.environ[bstack111lll11l1_opy_]).strip():
      bstack111ll11l1l_opy_[key] = os.environ[bstack111lll11l1_opy_]
  if bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨ੣") in os.environ:
    bstack111ll11l1l_opy_[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ੤")] = {}
    bstack111ll11l1l_opy_[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ੥")][bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ੦")] = os.environ[bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ੧")]
def bstack1ll1lll111_opy_():
  global bstack1ll111ll1l_opy_
  global bstack11l11111l1_opy_
  bstack1llll111ll_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack11l111_opy_ (u"ࠫ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ੨").lower() == val.lower():
      bstack1ll111ll1l_opy_[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ੩")] = {}
      bstack1ll111ll1l_opy_[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ੪")][bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ੫")] = sys.argv[idx + 1]
      bstack1llll111ll_opy_.extend([idx, idx + 1])
      break
  for key, bstack1ll1ll11l1_opy_ in bstack1l1111l1l1_opy_.items():
    if isinstance(bstack1ll1ll11l1_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack1ll1ll11l1_opy_:
          if bstack11l111_opy_ (u"ࠨ࠯࠰ࠫ੬") + var.lower() == val.lower() and key not in bstack1ll111ll1l_opy_:
            bstack1ll111ll1l_opy_[key] = sys.argv[idx + 1]
            bstack11l11111l1_opy_ += bstack11l111_opy_ (u"ࠩࠣ࠱࠲࠭੭") + var + bstack11l111_opy_ (u"ࠪࠤࠬ੮") + shlex.quote(sys.argv[idx + 1])
            bstack1llll111ll_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack11l111_opy_ (u"ࠫ࠲࠳ࠧ੯") + bstack1ll1ll11l1_opy_.lower() == val.lower() and key not in bstack1ll111ll1l_opy_:
          bstack1ll111ll1l_opy_[key] = sys.argv[idx + 1]
          bstack11l11111l1_opy_ += bstack11l111_opy_ (u"ࠬࠦ࠭࠮ࠩੰ") + bstack1ll1ll11l1_opy_ + bstack11l111_opy_ (u"࠭ࠠࠨੱ") + shlex.quote(sys.argv[idx + 1])
          bstack1llll111ll_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack1llll111ll_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack1l1l1lllll_opy_(config):
  bstack11111l111_opy_ = config.keys()
  for bstack1l111ll11l_opy_, bstack1l1llll1ll_opy_ in bstack1l11111ll1_opy_.items():
    if bstack1l1llll1ll_opy_ in bstack11111l111_opy_:
      config[bstack1l111ll11l_opy_] = config[bstack1l1llll1ll_opy_]
      del config[bstack1l1llll1ll_opy_]
  for bstack1l111ll11l_opy_, bstack1l1llll1ll_opy_ in bstack1l1ll1ll11_opy_.items():
    if isinstance(bstack1l1llll1ll_opy_, list):
      for bstack11l11ll1ll_opy_ in bstack1l1llll1ll_opy_:
        if bstack11l11ll1ll_opy_ in bstack11111l111_opy_:
          config[bstack1l111ll11l_opy_] = config[bstack11l11ll1ll_opy_]
          del config[bstack11l11ll1ll_opy_]
          break
    elif bstack1l1llll1ll_opy_ in bstack11111l111_opy_:
      config[bstack1l111ll11l_opy_] = config[bstack1l1llll1ll_opy_]
      del config[bstack1l1llll1ll_opy_]
  for bstack11l11ll1ll_opy_ in list(config):
    for bstack111l1llll1_opy_ in bstack1lll1l11ll_opy_:
      if bstack11l11ll1ll_opy_.lower() == bstack111l1llll1_opy_.lower() and bstack11l11ll1ll_opy_ != bstack111l1llll1_opy_:
        config[bstack111l1llll1_opy_] = config[bstack11l11ll1ll_opy_]
        del config[bstack11l11ll1ll_opy_]
  bstack1l11l1llll_opy_ = [{}]
  if not config.get(bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪੲ")):
    config[bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫੳ")] = [{}]
  bstack1l11l1llll_opy_ = config[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬੴ")]
  for platform in bstack1l11l1llll_opy_:
    for bstack11l11ll1ll_opy_ in list(platform):
      for bstack111l1llll1_opy_ in bstack1lll1l11ll_opy_:
        if bstack11l11ll1ll_opy_.lower() == bstack111l1llll1_opy_.lower() and bstack11l11ll1ll_opy_ != bstack111l1llll1_opy_:
          platform[bstack111l1llll1_opy_] = platform[bstack11l11ll1ll_opy_]
          del platform[bstack11l11ll1ll_opy_]
  for bstack1l111ll11l_opy_, bstack1l1llll1ll_opy_ in bstack1l1ll1ll11_opy_.items():
    for platform in bstack1l11l1llll_opy_:
      if isinstance(bstack1l1llll1ll_opy_, list):
        for bstack11l11ll1ll_opy_ in bstack1l1llll1ll_opy_:
          if bstack11l11ll1ll_opy_ in platform:
            platform[bstack1l111ll11l_opy_] = platform[bstack11l11ll1ll_opy_]
            del platform[bstack11l11ll1ll_opy_]
            break
      elif bstack1l1llll1ll_opy_ in platform:
        platform[bstack1l111ll11l_opy_] = platform[bstack1l1llll1ll_opy_]
        del platform[bstack1l1llll1ll_opy_]
  for bstack1111l1lll_opy_ in bstack11l1lll1ll_opy_:
    if bstack1111l1lll_opy_ in config:
      if not bstack11l1lll1ll_opy_[bstack1111l1lll_opy_] in config:
        config[bstack11l1lll1ll_opy_[bstack1111l1lll_opy_]] = {}
      config[bstack11l1lll1ll_opy_[bstack1111l1lll_opy_]].update(config[bstack1111l1lll_opy_])
      del config[bstack1111l1lll_opy_]
  for platform in bstack1l11l1llll_opy_:
    for bstack1111l1lll_opy_ in bstack11l1lll1ll_opy_:
      if bstack1111l1lll_opy_ in list(platform):
        if not bstack11l1lll1ll_opy_[bstack1111l1lll_opy_] in platform:
          platform[bstack11l1lll1ll_opy_[bstack1111l1lll_opy_]] = {}
        platform[bstack11l1lll1ll_opy_[bstack1111l1lll_opy_]].update(platform[bstack1111l1lll_opy_])
        del platform[bstack1111l1lll_opy_]
  config = bstack111l111lll_opy_(config)
  return config
def bstack11l11ll1l_opy_(config):
  global bstack1l1111lll_opy_
  bstack1l1lll1l11_opy_ = False
  if bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧੵ") in config and str(config[bstack11l111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ੶")]).lower() != bstack11l111_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ੷"):
    if bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ੸") not in config or str(config[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ੹")]).lower() == bstack11l111_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ੺"):
      config[bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨ੻")] = False
    else:
      bstack1l1ll1l11l_opy_ = bstack111lllllll_opy_()
      if bstack11l111_opy_ (u"ࠪ࡭ࡸ࡚ࡲࡪࡣ࡯ࡋࡷ࡯ࡤࠨ੼") in bstack1l1ll1l11l_opy_:
        if not bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੽") in config:
          config[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ੾")] = {}
        config[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ੿")][bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઀")] = bstack11l111_opy_ (u"ࠨࡣࡷࡷ࠲ࡸࡥࡱࡧࡤࡸࡪࡸࠧઁ")
        bstack1l1lll1l11_opy_ = True
        bstack1l1111lll_opy_ = config[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ં")].get(bstack11l111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬઃ"))
  if bstack1ll1l1l1ll_opy_(config) and bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ઄") in config and str(config[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩઅ")]).lower() != bstack11l111_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬઆ") and not bstack1l1lll1l11_opy_:
    if not bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫઇ") in config:
      config[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬઈ")] = {}
    if not config[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઉ")].get(bstack11l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡃ࡫ࡱࡥࡷࡿࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡣࡷ࡭ࡴࡴࠧઊ")) and not bstack11l111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ઋ") in config[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩઌ")]:
      bstack1llll111_opy_ = datetime.datetime.now()
      bstack1l11ll111l_opy_ = bstack1llll111_opy_.strftime(bstack11l111_opy_ (u"࠭ࠥࡥࡡࠨࡦࡤࠫࡈࠦࡏࠪઍ"))
      hostname = socket.gethostname()
      bstack1ll1ll1l1_opy_ = bstack11l111_opy_ (u"ࠧࠨ઎").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11l111_opy_ (u"ࠨࡽࢀࡣࢀࢃ࡟ࡼࡿࠪએ").format(bstack1l11ll111l_opy_, hostname, bstack1ll1ll1l1_opy_)
      config[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઐ")][bstack11l111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬઑ")] = identifier
    bstack1l1111lll_opy_ = config[bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ઒")].get(bstack11l111_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઓ"))
  return config
def bstack1l1llllll_opy_():
  bstack111l1l1ll1_opy_ =  bstack1l11l111l_opy_()[bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠬઔ")]
  return bstack111l1l1ll1_opy_ if bstack111l1l1ll1_opy_ else -1
def bstack11ll11l1l1_opy_(bstack111l1l1ll1_opy_):
  global CONFIG
  if not bstack11l111_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩક") in CONFIG[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪખ")]:
    return
  CONFIG[bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫગ")] = CONFIG[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬઘ")].replace(
    bstack11l111_opy_ (u"ࠫࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭ઙ"),
    str(bstack111l1l1ll1_opy_)
  )
def bstack11l1ll1l1l_opy_():
  global CONFIG
  if not bstack11l111_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫચ") in CONFIG[bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨછ")]:
    return
  bstack1llll111_opy_ = datetime.datetime.now()
  bstack1l11ll111l_opy_ = bstack1llll111_opy_.strftime(bstack11l111_opy_ (u"ࠧࠦࡦ࠰ࠩࡧ࠳ࠥࡉ࠼ࠨࡑࠬજ"))
  CONFIG[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪઝ")] = CONFIG[bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫઞ")].replace(
    bstack11l111_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩટ"),
    bstack1l11ll111l_opy_
  )
def bstack1ll11111l1_opy_():
  global CONFIG
  if bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ઠ") in CONFIG and not bool(CONFIG[bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧડ")]):
    del CONFIG[bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨઢ")]
    return
  if not bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩણ") in CONFIG:
    CONFIG[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪત")] = bstack11l111_opy_ (u"ࠩࠦࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬથ")
  if bstack11l111_opy_ (u"ࠪࠨࢀࡊࡁࡕࡇࡢࡘࡎࡓࡅࡾࠩદ") in CONFIG[bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ધ")]:
    bstack11l1ll1l1l_opy_()
    os.environ[bstack11l111_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩન")] = CONFIG[bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ઩")]
  if not bstack11l111_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩપ") in CONFIG[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪફ")]:
    return
  bstack111l1l1ll1_opy_ = bstack11l111_opy_ (u"ࠩࠪબ")
  bstack11lllllll_opy_ = bstack1l1llllll_opy_()
  if bstack11lllllll_opy_ != -1:
    bstack111l1l1ll1_opy_ = bstack11l111_opy_ (u"ࠪࡇࡎࠦࠧભ") + str(bstack11lllllll_opy_)
  if bstack111l1l1ll1_opy_ == bstack11l111_opy_ (u"ࠫࠬમ"):
    bstack1llll1llll_opy_ = bstack11l11lllll_opy_(CONFIG[bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨય")])
    if bstack1llll1llll_opy_ != -1:
      bstack111l1l1ll1_opy_ = str(bstack1llll1llll_opy_)
  if bstack111l1l1ll1_opy_:
    bstack11ll11l1l1_opy_(bstack111l1l1ll1_opy_)
    os.environ[bstack11l111_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪર")] = CONFIG[bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઱")]
def bstack1l11l1ll11_opy_(bstack1l1l1111l_opy_, bstack1lll1l1l1l_opy_, path):
  json_data = {
    bstack11l111_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬલ"): bstack1lll1l1l1l_opy_
  }
  if os.path.exists(path):
    bstack1ll11llll_opy_ = json.load(open(path, bstack11l111_opy_ (u"ࠩࡵࡦࠬળ")))
  else:
    bstack1ll11llll_opy_ = {}
  bstack1ll11llll_opy_[bstack1l1l1111l_opy_] = json_data
  with open(path, bstack11l111_opy_ (u"ࠥࡻ࠰ࠨ઴")) as outfile:
    json.dump(bstack1ll11llll_opy_, outfile)
def bstack11l11lllll_opy_(bstack1l1l1111l_opy_):
  bstack1l1l1111l_opy_ = str(bstack1l1l1111l_opy_)
  bstack11lllll11_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠫࢃ࠭વ")), bstack11l111_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬશ"))
  try:
    if not os.path.exists(bstack11lllll11_opy_):
      os.makedirs(bstack11lllll11_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"࠭ࡾࠨષ")), bstack11l111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧસ"), bstack11l111_opy_ (u"ࠨ࠰ࡥࡹ࡮ࡲࡤ࠮ࡰࡤࡱࡪ࠳ࡣࡢࡥ࡫ࡩ࠳ࡰࡳࡰࡰࠪહ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11l111_opy_ (u"ࠩࡺࠫ઺")):
        pass
      with open(file_path, bstack11l111_opy_ (u"ࠥࡻ࠰ࠨ઻")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11l111_opy_ (u"ࠫࡷ઼࠭")) as bstack11l1l111l_opy_:
      bstack1lll11l11_opy_ = json.load(bstack11l1l111l_opy_)
    if bstack1l1l1111l_opy_ in bstack1lll11l11_opy_:
      bstack11llll11l_opy_ = bstack1lll11l11_opy_[bstack1l1l1111l_opy_][bstack11l111_opy_ (u"ࠬ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩઽ")]
      bstack11l1l1l11_opy_ = int(bstack11llll11l_opy_) + 1
      bstack1l11l1ll11_opy_(bstack1l1l1111l_opy_, bstack11l1l1l11_opy_, file_path)
      return bstack11l1l1l11_opy_
    else:
      bstack1l11l1ll11_opy_(bstack1l1l1111l_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack111l11lll_opy_.format(str(e)))
    return -1
def bstack1111l1l111_opy_(config):
  if not config[bstack11l111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨા")] or not config[bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪિ")]:
    return True
  else:
    return False
def bstack1lll11l1l_opy_(config, index=0):
  global bstack1lll1l1l11_opy_
  bstack1ll1l1lll1_opy_ = {}
  caps = bstack11llll1l1_opy_ + bstack11l1111l1l_opy_
  if config.get(bstack11l111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬી"), False):
    bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ુ")] = True
    bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧૂ")] = config.get(bstack11l111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨૃ"), {})
  if bstack1lll1l1l11_opy_:
    caps += bstack1ll11l1l11_opy_
  for key in config:
    if key in caps + [bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૄ")]:
      continue
    bstack1ll1l1lll1_opy_[key] = config[key]
  if bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩૅ") in config:
    for bstack111l1l1ll_opy_ in config[bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૆")][index]:
      if bstack111l1l1ll_opy_ in caps:
        continue
      bstack1ll1l1lll1_opy_[bstack111l1l1ll_opy_] = config[bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫે")][index][bstack111l1l1ll_opy_]
  bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"ࠩ࡫ࡳࡸࡺࡎࡢ࡯ࡨࠫૈ")] = socket.gethostname()
  if bstack11l111_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫૉ") in bstack1ll1l1lll1_opy_:
    del (bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬ૊")])
  return bstack1ll1l1lll1_opy_
def bstack111ll1lll_opy_(config):
  global bstack1lll1l1l11_opy_
  bstack11l111l1l1_opy_ = {}
  caps = bstack11l1111l1l_opy_
  if bstack1lll1l1l11_opy_:
    caps += bstack1ll11l1l11_opy_
  for key in caps:
    if key in config:
      bstack11l111l1l1_opy_[key] = config[key]
  return bstack11l111l1l1_opy_
def bstack1l1ll11lll_opy_(bstack1ll1l1lll1_opy_, bstack11l111l1l1_opy_):
  bstack1l1ll11ll1_opy_ = {}
  for key in bstack1ll1l1lll1_opy_.keys():
    if key in bstack1l11111ll1_opy_:
      bstack1l1ll11ll1_opy_[bstack1l11111ll1_opy_[key]] = bstack1ll1l1lll1_opy_[key]
    else:
      bstack1l1ll11ll1_opy_[key] = bstack1ll1l1lll1_opy_[key]
  for key in bstack11l111l1l1_opy_:
    if key in bstack1l11111ll1_opy_:
      bstack1l1ll11ll1_opy_[bstack1l11111ll1_opy_[key]] = bstack11l111l1l1_opy_[key]
    else:
      bstack1l1ll11ll1_opy_[key] = bstack11l111l1l1_opy_[key]
  return bstack1l1ll11ll1_opy_
def bstack1ll1111l1l_opy_(config, index=0):
  global bstack1lll1l1l11_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1l1lll1lll_opy_ = bstack1l1l11l1l1_opy_(bstack1ll1l1111_opy_, config, logger)
  bstack11l111l1l1_opy_ = bstack111ll1lll_opy_(config)
  bstack1l1l11ll1l_opy_ = bstack11l1111l1l_opy_
  bstack1l1l11ll1l_opy_ += bstack111l1111l_opy_
  bstack11l111l1l1_opy_ = update(bstack11l111l1l1_opy_, bstack1l1lll1lll_opy_)
  if bstack1lll1l1l11_opy_:
    bstack1l1l11ll1l_opy_ += bstack1ll11l1l11_opy_
  if bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨો") in config:
    if bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫૌ") in config[bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵ્ࠪ")][index]:
      caps[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭૎")] = config[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૏")][index][bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨૐ")]
    if bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ૑") in config[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૒")][index]:
      caps[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ૓")] = str(config[bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૔")][index][bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ૕")])
    bstack1l1l1l11l_opy_ = bstack1l1l11l1l1_opy_(bstack1ll1l1111_opy_, config[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૖")][index], logger)
    bstack1l1l11ll1l_opy_ += list(bstack1l1l1l11l_opy_.keys())
    for bstack1l111l11ll_opy_ in bstack1l1l11ll1l_opy_:
      if bstack1l111l11ll_opy_ in config[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૗")][index]:
        if bstack1l111l11ll_opy_ == bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭૘"):
          try:
            bstack1l1l1l11l_opy_[bstack1l111l11ll_opy_] = str(config[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૙")][index][bstack1l111l11ll_opy_] * 1.0)
          except:
            bstack1l1l1l11l_opy_[bstack1l111l11ll_opy_] = str(config[bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૚")][index][bstack1l111l11ll_opy_])
        else:
          bstack1l1l1l11l_opy_[bstack1l111l11ll_opy_] = config[bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૛")][index][bstack1l111l11ll_opy_]
        del (config[bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૜")][index][bstack1l111l11ll_opy_])
    bstack11l111l1l1_opy_ = update(bstack11l111l1l1_opy_, bstack1l1l1l11l_opy_)
  bstack1ll1l1lll1_opy_ = bstack1lll11l1l_opy_(config, index)
  for bstack11l11ll1ll_opy_ in bstack11l1111l1l_opy_ + list(bstack1l1lll1lll_opy_.keys()):
    if bstack11l11ll1ll_opy_ in bstack1ll1l1lll1_opy_:
      bstack11l111l1l1_opy_[bstack11l11ll1ll_opy_] = bstack1ll1l1lll1_opy_[bstack11l11ll1ll_opy_]
      del (bstack1ll1l1lll1_opy_[bstack11l11ll1ll_opy_])
  if bstack1l11ll1ll1_opy_(config):
    bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩ૝")] = True
    caps.update(bstack11l111l1l1_opy_)
    caps[bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ૞")] = bstack1ll1l1lll1_opy_
  else:
    bstack1ll1l1lll1_opy_[bstack11l111_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫ૟")] = False
    caps.update(bstack1l1ll11lll_opy_(bstack1ll1l1lll1_opy_, bstack11l111l1l1_opy_))
    if bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪૠ") in caps:
      caps[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧૡ")] = caps[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬૢ")]
      del (caps[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ૣ")])
    if bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ૤") in caps:
      caps[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ૥")] = caps[bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ૦")]
      del (caps[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭૧")])
  return caps
def bstack111l1111l1_opy_():
  global bstack11111llll1_opy_
  global CONFIG
  if bstack1l11l1l11l_opy_() <= version.parse(bstack11l111_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭૨")):
    if bstack11111llll1_opy_ != bstack11l111_opy_ (u"ࠧࠨ૩"):
      return bstack11l111_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤ૪") + bstack11111llll1_opy_ + bstack11l111_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨ૫")
    return bstack1l111lll1_opy_
  if bstack11111llll1_opy_ != bstack11l111_opy_ (u"ࠪࠫ૬"):
    return bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨ૭") + bstack11111llll1_opy_ + bstack11l111_opy_ (u"ࠧ࠵ࡷࡥ࠱࡫ࡹࡧࠨ૮")
  return bstack1l1l1l1l1_opy_
def bstack11llllll1_opy_(options):
  return hasattr(options, bstack11l111_opy_ (u"࠭ࡳࡦࡶࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹࡿࠧ૯"))
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
def bstack1111l111l_opy_(options, bstack111lll1l11_opy_):
  for bstack111l1ll11_opy_ in bstack111lll1l11_opy_:
    if bstack111l1ll11_opy_ in [bstack11l111_opy_ (u"ࠧࡢࡴࡪࡷࠬ૰"), bstack11l111_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ૱")]:
      continue
    if bstack111l1ll11_opy_ in options._experimental_options:
      options._experimental_options[bstack111l1ll11_opy_] = update(options._experimental_options[bstack111l1ll11_opy_],
                                                         bstack111lll1l11_opy_[bstack111l1ll11_opy_])
    else:
      options.add_experimental_option(bstack111l1ll11_opy_, bstack111lll1l11_opy_[bstack111l1ll11_opy_])
  if bstack11l111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ૲") in bstack111lll1l11_opy_:
    for arg in bstack111lll1l11_opy_[bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ૳")]:
      options.add_argument(arg)
    del (bstack111lll1l11_opy_[bstack11l111_opy_ (u"ࠫࡦࡸࡧࡴࠩ૴")])
  if bstack11l111_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ૵") in bstack111lll1l11_opy_:
    for ext in bstack111lll1l11_opy_[bstack11l111_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ૶")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack111lll1l11_opy_[bstack11l111_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ૷")])
def bstack11ll1l111l_opy_(options, bstack111ll11lll_opy_):
  if bstack11l111_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ૸") in bstack111ll11lll_opy_:
    for bstack11l11l1l11_opy_ in bstack111ll11lll_opy_[bstack11l111_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨૹ")]:
      if bstack11l11l1l11_opy_ in options._preferences:
        options._preferences[bstack11l11l1l11_opy_] = update(options._preferences[bstack11l11l1l11_opy_], bstack111ll11lll_opy_[bstack11l111_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩૺ")][bstack11l11l1l11_opy_])
      else:
        options.set_preference(bstack11l11l1l11_opy_, bstack111ll11lll_opy_[bstack11l111_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪૻ")][bstack11l11l1l11_opy_])
  if bstack11l111_opy_ (u"ࠬࡧࡲࡨࡵࠪૼ") in bstack111ll11lll_opy_:
    for arg in bstack111ll11lll_opy_[bstack11l111_opy_ (u"࠭ࡡࡳࡩࡶࠫ૽")]:
      options.add_argument(arg)
def bstack1llll1ll11_opy_(options, bstack111ll11l11_opy_):
  if bstack11l111_opy_ (u"ࠧࡸࡧࡥࡺ࡮࡫ࡷࠨ૾") in bstack111ll11l11_opy_:
    options.use_webview(bool(bstack111ll11l11_opy_[bstack11l111_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࠩ૿")]))
  bstack1111l111l_opy_(options, bstack111ll11l11_opy_)
def bstack11ll1l1lll_opy_(options, bstack1l111l111l_opy_):
  for bstack11111lll1l_opy_ in bstack1l111l111l_opy_:
    if bstack11111lll1l_opy_ in [bstack11l111_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭଀"), bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଁ")]:
      continue
    options.set_capability(bstack11111lll1l_opy_, bstack1l111l111l_opy_[bstack11111lll1l_opy_])
  if bstack11l111_opy_ (u"ࠫࡦࡸࡧࡴࠩଂ") in bstack1l111l111l_opy_:
    for arg in bstack1l111l111l_opy_[bstack11l111_opy_ (u"ࠬࡧࡲࡨࡵࠪଃ")]:
      options.add_argument(arg)
  if bstack11l111_opy_ (u"࠭ࡴࡦࡥ࡫ࡲࡴࡲ࡯ࡨࡻࡓࡶࡪࡼࡩࡦࡹࠪ଄") in bstack1l111l111l_opy_:
    options.bstack1ll1l111l_opy_(bool(bstack1l111l111l_opy_[bstack11l111_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫଅ")]))
def bstack1ll11l1ll_opy_(options, bstack11l1lll11_opy_):
  for bstack111111l1l_opy_ in bstack11l1lll11_opy_:
    if bstack111111l1l_opy_ in [bstack11l111_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬଆ"), bstack11l111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧଇ")]:
      continue
    options._options[bstack111111l1l_opy_] = bstack11l1lll11_opy_[bstack111111l1l_opy_]
  if bstack11l111_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧଈ") in bstack11l1lll11_opy_:
    for bstack11l1lll1l_opy_ in bstack11l1lll11_opy_[bstack11l111_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨଉ")]:
      options.bstack11lll1l1ll_opy_(
        bstack11l1lll1l_opy_, bstack11l1lll11_opy_[bstack11l111_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩଊ")][bstack11l1lll1l_opy_])
  if bstack11l111_opy_ (u"࠭ࡡࡳࡩࡶࠫଋ") in bstack11l1lll11_opy_:
    for arg in bstack11l1lll11_opy_[bstack11l111_opy_ (u"ࠧࡢࡴࡪࡷࠬଌ")]:
      options.add_argument(arg)
def bstack1111l1ll1_opy_(options, caps):
  if not hasattr(options, bstack11l111_opy_ (u"ࠨࡍࡈ࡝ࠬ଍")):
    return
  if options.KEY == bstack11l111_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ଎"):
    options = bstack11l111l1_opy_.bstack11l1l1l1l_opy_(bstack11llll1111_opy_=options, config=CONFIG)
  if options.KEY == bstack11l111_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨଏ") and options.KEY in caps:
    bstack1111l111l_opy_(options, caps[bstack11l111_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩଐ")])
  elif options.KEY == bstack11l111_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡩ࡭ࡷ࡫ࡦࡰࡺࡒࡴࡹ࡯࡯࡯ࡵࠪ଑") and options.KEY in caps:
    bstack11ll1l111l_opy_(options, caps[bstack11l111_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫ଒")])
  elif options.KEY == bstack11l111_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨଓ") and options.KEY in caps:
    bstack11ll1l1lll_opy_(options, caps[bstack11l111_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩଔ")])
  elif options.KEY == bstack11l111_opy_ (u"ࠩࡰࡷ࠿࡫ࡤࡨࡧࡒࡴࡹ࡯࡯࡯ࡵࠪକ") and options.KEY in caps:
    bstack1llll1ll11_opy_(options, caps[bstack11l111_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫଖ")])
  elif options.KEY == bstack11l111_opy_ (u"ࠫࡸ࡫࠺ࡪࡧࡒࡴࡹ࡯࡯࡯ࡵࠪଗ") and options.KEY in caps:
    bstack1ll11l1ll_opy_(options, caps[bstack11l111_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫଘ")])
def bstack1ll11l1111_opy_(caps):
  global bstack1lll1l1l11_opy_
  if isinstance(os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧଙ")), str):
    bstack1lll1l1l11_opy_ = eval(os.getenv(bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨଚ")))
  if bstack1lll1l1l11_opy_:
    if bstack11ll1ll111_opy_() < version.parse(bstack11l111_opy_ (u"ࠨ࠴࠱࠷࠳࠶ࠧଛ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11l111_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩଜ")
    if bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଝ") in caps:
      browser = caps[bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଞ")]
    elif bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࠭ଟ") in caps:
      browser = caps[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧଠ")]
    browser = str(browser).lower()
    if browser == bstack11l111_opy_ (u"ࠧࡪࡲ࡫ࡳࡳ࡫ࠧଡ") or browser == bstack11l111_opy_ (u"ࠨ࡫ࡳࡥࡩ࠭ଢ"):
      browser = bstack11l111_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩଣ")
    if browser == bstack11l111_opy_ (u"ࠪࡷࡦࡳࡳࡶࡰࡪࠫତ"):
      browser = bstack11l111_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫଥ")
    if browser not in [bstack11l111_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬଦ"), bstack11l111_opy_ (u"࠭ࡥࡥࡩࡨࠫଧ"), bstack11l111_opy_ (u"ࠧࡪࡧࠪନ"), bstack11l111_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩࠨ଩"), bstack11l111_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪପ")]:
      return None
    try:
      package = bstack11l111_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲ࠯ࡽࢀ࠲ࡴࡶࡴࡪࡱࡱࡷࠬଫ").format(browser)
      name = bstack11l111_opy_ (u"ࠫࡔࡶࡴࡪࡱࡱࡷࠬବ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11llllll1_opy_(options):
        return None
      for bstack11l11ll1ll_opy_ in caps.keys():
        options.set_capability(bstack11l11ll1ll_opy_, caps[bstack11l11ll1ll_opy_])
      bstack1111l1ll1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack11llll111l_opy_(options, bstack1l1l11lll1_opy_):
  if not bstack11llllll1_opy_(options):
    return
  for bstack11l11ll1ll_opy_ in bstack1l1l11lll1_opy_.keys():
    if bstack11l11ll1ll_opy_ in bstack111l1111l_opy_:
      continue
    if bstack11l11ll1ll_opy_ in options._caps and type(options._caps[bstack11l11ll1ll_opy_]) in [dict, list]:
      options._caps[bstack11l11ll1ll_opy_] = update(options._caps[bstack11l11ll1ll_opy_], bstack1l1l11lll1_opy_[bstack11l11ll1ll_opy_])
    else:
      options.set_capability(bstack11l11ll1ll_opy_, bstack1l1l11lll1_opy_[bstack11l11ll1ll_opy_])
  bstack1111l1ll1_opy_(options, bstack1l1l11lll1_opy_)
  if bstack11l111_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡧࡩࡧࡻࡧࡨࡧࡵࡅࡩࡪࡲࡦࡵࡶࠫଭ") in options._caps:
    if options._caps[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫମ")] and options._caps[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬଯ")].lower() != bstack11l111_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩର"):
      del options._caps[bstack11l111_opy_ (u"ࠩࡰࡳࡿࡀࡤࡦࡤࡸ࡫࡬࡫ࡲࡂࡦࡧࡶࡪࡹࡳࠨ଱")]
def bstack1ll1lll1l1_opy_(proxy_config):
  if bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧଲ") in proxy_config:
    proxy_config[bstack11l111_opy_ (u"ࠫࡸࡹ࡬ࡑࡴࡲࡼࡾ࠭ଳ")] = proxy_config[bstack11l111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ଴")]
    del (proxy_config[bstack11l111_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪଵ")])
  if bstack11l111_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪଶ") in proxy_config and proxy_config[bstack11l111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫଷ")].lower() != bstack11l111_opy_ (u"ࠩࡧ࡭ࡷ࡫ࡣࡵࠩସ"):
    proxy_config[bstack11l111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭ହ")] = bstack11l111_opy_ (u"ࠫࡲࡧ࡮ࡶࡣ࡯ࠫ଺")
  if bstack11l111_opy_ (u"ࠬࡶࡲࡰࡺࡼࡅࡺࡺ࡯ࡤࡱࡱࡪ࡮࡭ࡕࡳ࡮ࠪ଻") in proxy_config:
    proxy_config[bstack11l111_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦ଼ࠩ")] = bstack11l111_opy_ (u"ࠧࡱࡣࡦࠫଽ")
  return proxy_config
def bstack111111111_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11l111_opy_ (u"ࠨࡲࡵࡳࡽࡿࠧା") in config:
    return proxy
  config[bstack11l111_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨି")] = bstack1ll1lll1l1_opy_(config[bstack11l111_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩୀ")])
  if proxy == None:
    proxy = Proxy(config[bstack11l111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪୁ")])
  return proxy
def bstack1ll1l111ll_opy_(self):
  global CONFIG
  global bstack1ll111llll_opy_
  try:
    proxy = bstack11111ll11l_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11l111_opy_ (u"ࠬ࠴ࡰࡢࡥࠪୂ")):
        proxies = bstack1111111ll_opy_(proxy, bstack111l1111l1_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1l11111l_opy_ = proxies.popitem()
          if bstack11l111_opy_ (u"ࠨ࠺࠰࠱ࠥୃ") in bstack1l1l11111l_opy_:
            return bstack1l1l11111l_opy_
          else:
            return bstack11l111_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣୄ") + bstack1l1l11111l_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡵࡸ࡯ࡹࡻࠣࡹࡷࡲࠠ࠻ࠢࡾࢁࠧ୅").format(str(e)))
  return bstack1ll111llll_opy_(self)
def bstack1111l111ll_opy_():
  global CONFIG
  return bstack11lll111l_opy_(CONFIG) and bstack1llll11l11_opy_() and bstack1l11l1l11l_opy_() >= version.parse(bstack111111lll_opy_)
def bstack1l11llll11_opy_():
  global CONFIG
  return (bstack11l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡐࡳࡱࡻࡽࠬ୆") in CONFIG or bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࡒࡵࡳࡽࡿࠧେ") in CONFIG) and bstack1l1111l1ll_opy_()
def bstack1lllll1ll1_opy_(config):
  bstack111l1111ll_opy_ = {}
  if bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨୈ") in config:
    bstack111l1111ll_opy_ = config[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୉")]
  if bstack11l111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୊") in config:
    bstack111l1111ll_opy_ = config[bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ୋ")]
  proxy = bstack11111ll11l_opy_(config)
  if proxy:
    if proxy.endswith(bstack11l111_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭ୌ")) and os.path.isfile(proxy):
      bstack111l1111ll_opy_[bstack11l111_opy_ (u"ࠩ࠰ࡴࡦࡩ࠭ࡧ࡫࡯ࡩ୍ࠬ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11l111_opy_ (u"ࠪ࠲ࡵࡧࡣࠨ୎")):
        proxies = bstack1llllll11l_opy_(config, bstack111l1111l1_opy_())
        if len(proxies) > 0:
          protocol, bstack1l1l11111l_opy_ = proxies.popitem()
          if bstack11l111_opy_ (u"ࠦ࠿࠵࠯ࠣ୏") in bstack1l1l11111l_opy_:
            parsed_url = urlparse(bstack1l1l11111l_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11l111_opy_ (u"ࠧࡀ࠯࠰ࠤ୐") + bstack1l1l11111l_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack111l1111ll_opy_[bstack11l111_opy_ (u"࠭ࡰࡳࡱࡻࡽࡍࡵࡳࡵࠩ୑")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack111l1111ll_opy_[bstack11l111_opy_ (u"ࠧࡱࡴࡲࡼࡾࡖ࡯ࡳࡶࠪ୒")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack111l1111ll_opy_[bstack11l111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡕࡴࡧࡵࠫ୓")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack111l1111ll_opy_[bstack11l111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡣࡶࡷࠬ୔")] = str(parsed_url.password)
  return bstack111l1111ll_opy_
def bstack1l1l1l1lll_opy_(config):
  if bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡄࡱࡱࡸࡪࡾࡴࡐࡲࡷ࡭ࡴࡴࡳࠨ୕") in config:
    return config[bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩୖ")]
  return {}
def bstack1l1l1ll1ll_opy_(caps):
  global bstack1l1111lll_opy_
  if bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ୗ") in caps:
    caps[bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ୘")][bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱ࠭୙")] = True
    if bstack1l1111lll_opy_:
      caps[bstack11l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ୚")][bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ୛")] = bstack1l1111lll_opy_
  else:
    caps[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰࡯ࡳࡨࡧ࡬ࠨଡ଼")] = True
    if bstack1l1111lll_opy_:
      caps[bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬଢ଼")] = bstack1l1111lll_opy_
@measure(event_name=EVENTS.bstack111l111111_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack111lll11ll_opy_():
  global CONFIG
  if not bstack1ll1l1l1ll_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ୞") in CONFIG and bstack11lll1lll_opy_(CONFIG[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪୟ")]):
    if (
      bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫୠ") in CONFIG
      and bstack11lll1lll_opy_(CONFIG[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬୡ")].get(bstack11l111_opy_ (u"ࠩࡶ࡯࡮ࡶࡂࡪࡰࡤࡶࡾࡏ࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡢࡶ࡬ࡳࡳ࠭ୢ")))
    ):
      logger.debug(bstack11l111_opy_ (u"ࠥࡐࡴࡩࡡ࡭ࠢࡥ࡭ࡳࡧࡲࡺࠢࡱࡳࡹࠦࡳࡵࡣࡵࡸࡪࡪࠠࡢࡵࠣࡷࡰ࡯ࡰࡃ࡫ࡱࡥࡷࡿࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡣࡷ࡭ࡴࡴࠠࡪࡵࠣࡩࡳࡧࡢ࡭ࡧࡧࠦୣ"))
      return
    bstack111l1111ll_opy_ = bstack1lllll1ll1_opy_(CONFIG)
    bstack1111l1111_opy_(CONFIG[bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ୤")], bstack111l1111ll_opy_)
def bstack1111l1111_opy_(key, bstack111l1111ll_opy_):
  global bstack1l1l11111_opy_
  logger.info(bstack111l1l11l_opy_)
  try:
    bstack1l1l11111_opy_ = Local()
    bstack11l1l1llll_opy_ = {bstack11l111_opy_ (u"ࠬࡱࡥࡺࠩ୥"): key}
    bstack11l1l1llll_opy_.update(bstack111l1111ll_opy_)
    logger.debug(bstack1ll1llll1_opy_.format(str(bstack11l1l1llll_opy_)).replace(key, bstack11l111_opy_ (u"࡛࠭ࡓࡇࡇࡅࡈ࡚ࡅࡅ࡟ࠪ୦")))
    bstack1l1l11111_opy_.start(**bstack11l1l1llll_opy_)
    if bstack1l1l11111_opy_.isRunning():
      logger.info(bstack1l11111lll_opy_)
  except Exception as e:
    bstack1l111l1ll1_opy_(bstack111ll1111_opy_.format(str(e)))
def bstack1l11ll11ll_opy_():
  global bstack1l1l11111_opy_
  if bstack1l1l11111_opy_.isRunning():
    logger.info(bstack11111lll1_opy_)
    bstack1l1l11111_opy_.stop()
  bstack1l1l11111_opy_ = None
def bstack1l11l1lll_opy_(bstack1l11lllll1_opy_=[]):
  global CONFIG
  bstack1lllll1lll_opy_ = []
  bstack1l1ll1l111_opy_ = [bstack11l111_opy_ (u"ࠧࡰࡵࠪ୧"), bstack11l111_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫ୨"), bstack11l111_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭୩"), bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ୪"), bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ୫"), bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭୬")]
  try:
    for err in bstack1l11lllll1_opy_:
      bstack11ll11ll11_opy_ = {}
      for k in bstack1l1ll1l111_opy_:
        val = CONFIG[bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ୭")][int(err[bstack11l111_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭୮")])].get(k)
        if val:
          bstack11ll11ll11_opy_[k] = val
      if(err[bstack11l111_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ୯")] != bstack11l111_opy_ (u"ࠩࠪ୰")):
        bstack11ll11ll11_opy_[bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡴࠩୱ")] = {
          err[bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ୲")]: err[bstack11l111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ୳")]
        }
        bstack1lllll1lll_opy_.append(bstack11ll11ll11_opy_)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡲࡶࡲࡧࡴࡵ࡫ࡱ࡫ࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡦࡸࡨࡲࡹࡀࠠࠨ୴") + str(e))
  finally:
    return bstack1lllll1lll_opy_
def bstack1l11ll11l_opy_(file_name):
  bstack11lllll1l1_opy_ = []
  try:
    bstack1lll11llll_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1lll11llll_opy_):
      with open(bstack1lll11llll_opy_) as f:
        bstack1llll1l1l1_opy_ = json.load(f)
        bstack11lllll1l1_opy_ = bstack1llll1l1l1_opy_
      os.remove(bstack1lll11llll_opy_)
    return bstack11lllll1l1_opy_
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩ࡭ࡳࡪࡩ࡯ࡩࠣࡩࡷࡸ࡯ࡳࠢ࡯࡭ࡸࡺ࠺ࠡࠩ୵") + str(e))
    return bstack11lllll1l1_opy_
def bstack11lllll1l_opy_():
  try:
      from bstack_utils.constants import bstack11llll1l1l_opy_, EVENTS
      from bstack_utils.helper import bstack11ll11ll1l_opy_, get_host_info, bstack111ll111_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack11111l111l_opy_ = os.path.join(os.getcwd(), bstack11l111_opy_ (u"ࠨ࡮ࡲ࡫ࠬ୶"), bstack11l111_opy_ (u"ࠩ࡮ࡩࡾ࠳࡭ࡦࡶࡵ࡭ࡨࡹ࠮࡫ࡵࡲࡲࠬ୷"))
      lock = FileLock(bstack11111l111l_opy_+bstack11l111_opy_ (u"ࠥ࠲ࡱࡵࡣ࡬ࠤ୸"))
      def bstack1l1ll11l_opy_():
          try:
              with lock:
                  with open(bstack11111l111l_opy_, bstack11l111_opy_ (u"ࠦࡷࠨ୹"), encoding=bstack11l111_opy_ (u"ࠧࡻࡴࡧ࠯࠻ࠦ୺")) as file:
                      data = json.load(file)
                      config = {
                          bstack11l111_opy_ (u"ࠨࡨࡦࡣࡧࡩࡷࡹࠢ୻"): {
                              bstack11l111_opy_ (u"ࠢࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪࠨ୼"): bstack11l111_opy_ (u"ࠣࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠦ୽"),
                          }
                      }
                      bstack1ll11ll11_opy_ = datetime.utcnow()
                      bstack1llll111_opy_ = bstack1ll11ll11_opy_.strftime(bstack11l111_opy_ (u"ࠤࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠴ࠥࡧࠢࡘࡘࡈࠨ୾"))
                      test_id = os.environ.get(bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ୿")) if os.environ.get(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ஀")) else bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢ஁"))
                      payload = {
                          bstack11l111_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠥஂ"): bstack11l111_opy_ (u"ࠢࡴࡦ࡮ࡣࡪࡼࡥ࡯ࡶࡶࠦஃ"),
                          bstack11l111_opy_ (u"ࠣࡦࡤࡸࡦࠨ஄"): {
                              bstack11l111_opy_ (u"ࠤࡷࡩࡸࡺࡨࡶࡤࡢࡹࡺ࡯ࡤࠣஅ"): test_id,
                              bstack11l111_opy_ (u"ࠥࡧࡷ࡫ࡡࡵࡧࡧࡣࡩࡧࡹࠣஆ"): bstack1llll111_opy_,
                              bstack11l111_opy_ (u"ࠦࡪࡼࡥ࡯ࡶࡢࡲࡦࡳࡥࠣஇ"): bstack11l111_opy_ (u"࡙ࠧࡄࡌࡈࡨࡥࡹࡻࡲࡦࡒࡨࡶ࡫ࡵࡲ࡮ࡣࡱࡧࡪࠨஈ"),
                              bstack11l111_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡰࡳࡰࡰࠥஉ"): {
                                  bstack11l111_opy_ (u"ࠢ࡮ࡧࡤࡷࡺࡸࡥࡴࠤஊ"): data,
                                  bstack11l111_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥ஋"): bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦ஌"))
                              },
                              bstack11l111_opy_ (u"ࠥࡹࡸ࡫ࡲࡠࡦࡤࡸࡦࠨ஍"): bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠦࡺࡹࡥࡳࡐࡤࡱࡪࠨஎ")),
                              bstack11l111_opy_ (u"ࠧ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠣஏ"): get_host_info()
                          }
                      }
                      bstack1llll11ll1_opy_ = bstack111l11l1l_opy_(cli.config, [bstack11l111_opy_ (u"ࠨࡡࡱ࡫ࡶࠦஐ"), bstack11l111_opy_ (u"ࠢࡦࡦࡶࡍࡳࡹࡴࡳࡷࡰࡩࡳࡺࡡࡵ࡫ࡲࡲࠧ஑"), bstack11l111_opy_ (u"ࠣࡣࡳ࡭ࠧஒ")], bstack11llll1l1l_opy_)
                      response = bstack11ll11ll1l_opy_(bstack11l111_opy_ (u"ࠤࡓࡓࡘ࡚ࠢஓ"), bstack1llll11ll1_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack11l111_opy_ (u"ࠥࡈࡦࡺࡡࠡࡵࡨࡲࡹࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥࡺ࡯ࠡࡽࢀࠤࡼ࡯ࡴࡩࠢࡧࡥࡹࡧࠠࡼࡿࠥஔ").format(bstack11llll1l1l_opy_, payload))
                      else:
                          logger.debug(bstack11l111_opy_ (u"ࠦࡗ࡫ࡱࡶࡧࡶࡸࠥ࡬ࡡࡪ࡮ࡨࡨࠥ࡬࡯ࡳࠢࡾࢁࠥࡽࡩࡵࡪࠣࡨࡦࡺࡡࠡࡽࢀࠦக").format(bstack11llll1l1l_opy_, payload))
          except Exception as e:
              logger.debug(bstack11l111_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡲࡩࠦ࡫ࡦࡻࠣࡱࡪࡺࡲࡪࡥࡶࠤࡩࡧࡴࡢࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࠦࡻࡾࠤ஖").format(e))
      bstack1l1ll11l_opy_()
      bstack1l11ll111_opy_(bstack11111l111l_opy_, logger)
  except:
    pass
def bstack1l111llll1_opy_():
  global bstack11ll1l1111_opy_
  global bstack1l111ll1ll_opy_
  global bstack11111l1l1_opy_
  global bstack1l1l1l111_opy_
  global bstack1l111lllll_opy_
  global bstack1l1l11l1ll_opy_
  global CONFIG
  bstack11l1ll1ll1_opy_ = os.environ.get(bstack11l111_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧ஗"))
  if bstack11l1ll1ll1_opy_ in [bstack11l111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭஘"), bstack11l111_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧங")]:
    bstack1ll11l1lll_opy_()
  percy.shutdown()
  if bstack11ll1l1111_opy_:
    logger.warning(bstack1llllll111_opy_.format(str(bstack11ll1l1111_opy_)))
  else:
    try:
      bstack1ll11llll_opy_ = bstack11l11ll11_opy_(bstack11l111_opy_ (u"ࠩ࠱ࡦࡸࡺࡡࡤ࡭࠰ࡧࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠨச"), logger)
      if bstack1ll11llll_opy_.get(bstack11l111_opy_ (u"ࠪࡲࡺࡪࡧࡦࡡ࡯ࡳࡨࡧ࡬ࠨ஛")) and bstack1ll11llll_opy_.get(bstack11l111_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩஜ")).get(bstack11l111_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧ஝")):
        logger.warning(bstack1llllll111_opy_.format(str(bstack1ll11llll_opy_[bstack11l111_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫஞ")][bstack11l111_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩட")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1l1l111ll_opy_.invoke(Events.bstack111l111ll_opy_)
  logger.info(bstack111ll1ll1l_opy_)
  global bstack1l1l11111_opy_
  if bstack1l1l11111_opy_:
    bstack1l11ll11ll_opy_()
  try:
    with bstack11l1111ll1_opy_:
      bstack11ll1lll1l_opy_ = bstack1l111ll1ll_opy_.copy()
    for driver in bstack11ll1lll1l_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1111l1lll1_opy_)
  if bstack1l1l11l1ll_opy_ == bstack11l111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ஠"):
    bstack1l111lllll_opy_ = bstack1l11ll11l_opy_(bstack11l111_opy_ (u"ࠩࡵࡳࡧࡵࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪ஡"))
  if bstack1l1l11l1ll_opy_ == bstack11l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ஢") and len(bstack1l1l1l111_opy_) == 0:
    bstack1l1l1l111_opy_ = bstack1l11ll11l_opy_(bstack11l111_opy_ (u"ࠫࡵࡽ࡟ࡱࡻࡷࡩࡸࡺ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷ࠲࡯ࡹ࡯࡯ࠩண"))
    if len(bstack1l1l1l111_opy_) == 0:
      bstack1l1l1l111_opy_ = bstack1l11ll11l_opy_(bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡶࡰࡱࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫத"))
  bstack11l1l1l111_opy_ = bstack11l111_opy_ (u"࠭ࠧ஥")
  if len(bstack11111l1l1_opy_) > 0:
    bstack11l1l1l111_opy_ = bstack1l11l1lll_opy_(bstack11111l1l1_opy_)
  elif len(bstack1l1l1l111_opy_) > 0:
    bstack11l1l1l111_opy_ = bstack1l11l1lll_opy_(bstack1l1l1l111_opy_)
  elif len(bstack1l111lllll_opy_) > 0:
    bstack11l1l1l111_opy_ = bstack1l11l1lll_opy_(bstack1l111lllll_opy_)
  elif len(bstack11lll1ll1l_opy_) > 0:
    bstack11l1l1l111_opy_ = bstack1l11l1lll_opy_(bstack11lll1ll1l_opy_)
  if bool(bstack11l1l1l111_opy_):
    bstack11lll1111_opy_(bstack11l1l1l111_opy_)
  else:
    bstack11lll1111_opy_()
  bstack1l11ll111_opy_(bstack1111lll1ll_opy_, logger)
  if bstack11l1ll1ll1_opy_ not in [bstack11l111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ஦")]:
    bstack11lllll1l_opy_()
  bstack1lll11ll11_opy_.bstack11llllll_opy_(CONFIG)
  if len(bstack1l111lllll_opy_) > 0:
    sys.exit(len(bstack1l111lllll_opy_))
def bstack11111l1l11_opy_(bstack111l111l1_opy_, frame):
  global bstack111ll111_opy_
  logger.error(bstack11l11llll_opy_)
  bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡐࡲࠫ஧"), bstack111l111l1_opy_)
  if hasattr(signal, bstack11l111_opy_ (u"ࠩࡖ࡭࡬ࡴࡡ࡭ࡵࠪந")):
    bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪன"), signal.Signals(bstack111l111l1_opy_).name)
  else:
    bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫப"), bstack11l111_opy_ (u"࡙ࠬࡉࡈࡗࡑࡏࡓࡕࡗࡏࠩ஫"))
  if cli.is_running():
    bstack1l1l111ll_opy_.invoke(Events.bstack111l111ll_opy_)
  bstack11l1ll1ll1_opy_ = os.environ.get(bstack11l111_opy_ (u"࠭ࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࡡࡘࡗࡊࡊࠧ஬"))
  if bstack11l1ll1ll1_opy_ == bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ஭") and not cli.is_enabled(CONFIG):
    bstack1lll1l1l_opy_.stop(bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨம")))
  bstack1l111llll1_opy_()
  sys.exit(1)
def bstack1l111l1ll1_opy_(err):
  logger.critical(bstack111ll1lll1_opy_.format(str(err)))
  bstack11lll1111_opy_(bstack111ll1lll1_opy_.format(str(err)), True)
  atexit.unregister(bstack1l111llll1_opy_)
  bstack1ll11l1lll_opy_()
  sys.exit(1)
def bstack1ll1lll1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack11lll1111_opy_(message, True)
  atexit.unregister(bstack1l111llll1_opy_)
  bstack1ll11l1lll_opy_()
  sys.exit(1)
def bstack1l11lll11_opy_():
  global CONFIG
  global bstack1ll111ll1l_opy_
  global bstack111ll11l1l_opy_
  global bstack1l1111l11_opy_
  CONFIG = bstack1l11lll1l_opy_()
  load_dotenv(CONFIG.get(bstack11l111_opy_ (u"ࠩࡨࡲࡻࡌࡩ࡭ࡧࠪய")))
  bstack111l1l11ll_opy_()
  bstack1ll1lll111_opy_()
  CONFIG = bstack1l1l1lllll_opy_(CONFIG)
  update(CONFIG, bstack111ll11l1l_opy_)
  update(CONFIG, bstack1ll111ll1l_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack11l11ll1l_opy_(CONFIG)
  bstack1l1111l11_opy_ = bstack1ll1l1l1ll_opy_(CONFIG)
  os.environ[bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ர")] = bstack1l1111l11_opy_.__str__().lower()
  bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬற"), bstack1l1111l11_opy_)
  if (bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨல") in CONFIG and bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩள") in bstack1ll111ll1l_opy_) or (
          bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪழ") in CONFIG and bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫவ") not in bstack111ll11l1l_opy_):
    if os.getenv(bstack11l111_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭ஶ")):
      CONFIG[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬஷ")] = os.getenv(bstack11l111_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨஸ"))
    else:
      if not CONFIG.get(bstack11l111_opy_ (u"ࠧ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠣஹ"), bstack11l111_opy_ (u"ࠨࠢ஺")) in bstack1l111l1l11_opy_:
        bstack1ll11111l1_opy_()
  elif (bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ஻") not in CONFIG and bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ஼") in CONFIG) or (
          bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ஽") in bstack111ll11l1l_opy_ and bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ா") not in bstack1ll111ll1l_opy_):
    del (CONFIG[bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ி")])
  if bstack1111l1l111_opy_(CONFIG):
    bstack1l111l1ll1_opy_(bstack1l1l11llll_opy_)
  Config.bstack111ll1ll_opy_().set_property(bstack11l111_opy_ (u"ࠧࡻࡳࡦࡴࡑࡥࡲ࡫ࠢீ"), CONFIG[bstack11l111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨு")])
  bstack1llll1ll1l_opy_()
  bstack1lllll1111_opy_()
  if bstack1lll1l1l11_opy_ and not CONFIG.get(bstack11l111_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠥூ"), bstack11l111_opy_ (u"ࠣࠤ௃")) in bstack1l111l1l11_opy_:
    CONFIG[bstack11l111_opy_ (u"ࠩࡤࡴࡵ࠭௄")] = bstack1l1l1llll_opy_(CONFIG)
    logger.info(bstack1lll1ll1l1_opy_.format(CONFIG[bstack11l111_opy_ (u"ࠪࡥࡵࡶࠧ௅")]))
  if not bstack1l1111l11_opy_:
    CONFIG[bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧெ")] = [{}]
def bstack1111lll1l1_opy_(config, bstack11l1l1l11l_opy_):
  global CONFIG
  global bstack1lll1l1l11_opy_
  CONFIG = config
  bstack1lll1l1l11_opy_ = bstack11l1l1l11l_opy_
def bstack1lllll1111_opy_():
  global CONFIG
  global bstack1lll1l1l11_opy_
  if bstack11l111_opy_ (u"ࠬࡧࡰࡱࠩே") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1ll1lll1l_opy_(e, bstack1111l1l1ll_opy_)
    bstack1lll1l1l11_opy_ = True
    bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬை"), True)
def bstack1l1l1llll_opy_(config):
  bstack1lll11ll1l_opy_ = bstack11l111_opy_ (u"ࠧࠨ௉")
  app = config[bstack11l111_opy_ (u"ࠨࡣࡳࡴࠬொ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack11lll1ll11_opy_:
      if os.path.exists(app):
        bstack1lll11ll1l_opy_ = bstack1ll1111lll_opy_(config, app)
      elif bstack1ll11l1l1l_opy_(app):
        bstack1lll11ll1l_opy_ = app
      else:
        bstack1l111l1ll1_opy_(bstack111l1lll11_opy_.format(app))
    else:
      if bstack1ll11l1l1l_opy_(app):
        bstack1lll11ll1l_opy_ = app
      elif os.path.exists(app):
        bstack1lll11ll1l_opy_ = bstack1ll1111lll_opy_(app)
      else:
        bstack1l111l1ll1_opy_(bstack1ll11lllll_opy_)
  else:
    if len(app) > 2:
      bstack1l111l1ll1_opy_(bstack11l11l1111_opy_)
    elif len(app) == 2:
      if bstack11l111_opy_ (u"ࠩࡳࡥࡹ࡮ࠧோ") in app and bstack11l111_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭ௌ") in app:
        if os.path.exists(app[bstack11l111_opy_ (u"ࠫࡵࡧࡴࡩ்ࠩ")]):
          bstack1lll11ll1l_opy_ = bstack1ll1111lll_opy_(config, app[bstack11l111_opy_ (u"ࠬࡶࡡࡵࡪࠪ௎")], app[bstack11l111_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ௏")])
        else:
          bstack1l111l1ll1_opy_(bstack111l1lll11_opy_.format(app))
      else:
        bstack1l111l1ll1_opy_(bstack11l11l1111_opy_)
    else:
      for key in app:
        if key in bstack1l1l1lll1l_opy_:
          if key == bstack11l111_opy_ (u"ࠧࡱࡣࡷ࡬ࠬௐ"):
            if os.path.exists(app[key]):
              bstack1lll11ll1l_opy_ = bstack1ll1111lll_opy_(config, app[key])
            else:
              bstack1l111l1ll1_opy_(bstack111l1lll11_opy_.format(app))
          else:
            bstack1lll11ll1l_opy_ = app[key]
        else:
          bstack1l111l1ll1_opy_(bstack1ll11l1l1_opy_)
  return bstack1lll11ll1l_opy_
def bstack1ll11l1l1l_opy_(bstack1lll11ll1l_opy_):
  import re
  bstack11llll1ll1_opy_ = re.compile(bstack11l111_opy_ (u"ࡳࠤࡡ࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰ࠤࠣ௑"))
  bstack1l1ll11l11_opy_ = re.compile(bstack11l111_opy_ (u"ࡴࠥࡢࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪ࠰࡝ࡤ࠱ࡿࡇ࡛࠭࠲࠰࠽ࡡࡥ࠮࡝࠯ࡠ࠮ࠩࠨ௒"))
  if bstack11l111_opy_ (u"ࠪࡦࡸࡀ࠯࠰ࠩ௓") in bstack1lll11ll1l_opy_ or re.fullmatch(bstack11llll1ll1_opy_, bstack1lll11ll1l_opy_) or re.fullmatch(bstack1l1ll11l11_opy_, bstack1lll11ll1l_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack11111l1ll_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack1ll1111lll_opy_(config, path, bstack1ll1ll1ll1_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11l111_opy_ (u"ࠫࡷࡨࠧ௔")).read()).hexdigest()
  bstack1111ll1ll1_opy_ = bstack1l1l111l1_opy_(md5_hash)
  bstack1lll11ll1l_opy_ = None
  if bstack1111ll1ll1_opy_:
    logger.info(bstack11l11l11l_opy_.format(bstack1111ll1ll1_opy_, md5_hash))
    return bstack1111ll1ll1_opy_
  bstack1lll1l1ll1_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack11l111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࠪ௕"): (os.path.basename(path), open(os.path.abspath(path), bstack11l111_opy_ (u"࠭ࡲࡣࠩ௖")), bstack11l111_opy_ (u"ࠧࡵࡧࡻࡸ࠴ࡶ࡬ࡢ࡫ࡱࠫௗ")),
      bstack11l111_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫ௘"): bstack1ll1ll1ll1_opy_
    }
  )
  response = requests.post(bstack1111lll1l_opy_, data=multipart_data,
                           headers={bstack11l111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ௙"): multipart_data.content_type},
                           auth=(config[bstack11l111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ௚")], config[bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧ௛")]))
  try:
    res = json.loads(response.text)
    bstack1lll11ll1l_opy_ = res[bstack11l111_opy_ (u"ࠬࡧࡰࡱࡡࡸࡶࡱ࠭௜")]
    logger.info(bstack1l111l1l1_opy_.format(bstack1lll11ll1l_opy_))
    bstack1l11lll11l_opy_(md5_hash, bstack1lll11ll1l_opy_)
    cli.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠨࡨࡵࡶࡳ࠾ࡺࡶ࡬ࡰࡣࡧࡣࡦࡶࡰࠣ௝"), datetime.datetime.now() - bstack1lll1l1ll1_opy_)
  except ValueError as err:
    bstack1l111l1ll1_opy_(bstack1lllllllll_opy_.format(str(err)))
  return bstack1lll11ll1l_opy_
def bstack1llll1ll1l_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack11l1l1l1l1_opy_
  bstack1lll11lll_opy_ = 1
  bstack11ll11l111_opy_ = 1
  if bstack11l111_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ௞") in CONFIG:
    bstack11ll11l111_opy_ = CONFIG[bstack11l111_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ௟")]
  else:
    bstack11ll11l111_opy_ = bstack11llllll1l_opy_(framework_name, args) or 1
  if bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ௠") in CONFIG:
    bstack1lll11lll_opy_ = len(CONFIG[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭௡")])
  bstack11l1l1l1l1_opy_ = int(bstack11ll11l111_opy_) * int(bstack1lll11lll_opy_)
def bstack11llllll1l_opy_(framework_name, args):
  if framework_name == bstack11llll1ll_opy_ and args and bstack11l111_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ௢") in args:
      bstack1ll1l111l1_opy_ = args.index(bstack11l111_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ௣"))
      return int(args[bstack1ll1l111l1_opy_ + 1]) or 1
  return 1
def bstack1l1l111l1_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l111_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩ௤"))
    bstack11ll111l1l_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠧࡿࠩ௥")), bstack11l111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ௦"), bstack11l111_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪ௧"))
    if os.path.exists(bstack11ll111l1l_opy_):
      try:
        bstack1ll111111_opy_ = json.load(open(bstack11ll111l1l_opy_, bstack11l111_opy_ (u"ࠪࡶࡧ࠭௨")))
        if md5_hash in bstack1ll111111_opy_:
          bstack111ll1l1l_opy_ = bstack1ll111111_opy_[md5_hash]
          bstack11l111l1ll_opy_ = datetime.datetime.now()
          bstack1ll111111l_opy_ = datetime.datetime.strptime(bstack111ll1l1l_opy_[bstack11l111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧ௩")], bstack11l111_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩ௪"))
          if (bstack11l111l1ll_opy_ - bstack1ll111111l_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack111ll1l1l_opy_[bstack11l111_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫ௫")]):
            return None
          return bstack111ll1l1l_opy_[bstack11l111_opy_ (u"ࠧࡪࡦࠪ௬")]
      except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡏࡇ࠹ࠥ࡮ࡡࡴࡪࠣࡪ࡮ࡲࡥ࠻ࠢࡾࢁࠬ௭").format(str(e)))
    return None
  bstack11ll111l1l_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠩࢁࠫ௮")), bstack11l111_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ௯"), bstack11l111_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬ௰"))
  lock_file = bstack11ll111l1l_opy_ + bstack11l111_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫ௱")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack11ll111l1l_opy_):
        with open(bstack11ll111l1l_opy_, bstack11l111_opy_ (u"࠭ࡲࠨ௲")) as f:
          content = f.read().strip()
          if content:
            bstack1ll111111_opy_ = json.loads(content)
            if md5_hash in bstack1ll111111_opy_:
              bstack111ll1l1l_opy_ = bstack1ll111111_opy_[md5_hash]
              bstack11l111l1ll_opy_ = datetime.datetime.now()
              bstack1ll111111l_opy_ = datetime.datetime.strptime(bstack111ll1l1l_opy_[bstack11l111_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ௳")], bstack11l111_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬ௴"))
              if (bstack11l111l1ll_opy_ - bstack1ll111111l_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack111ll1l1l_opy_[bstack11l111_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ௵")]):
                return None
              return bstack111ll1l1l_opy_[bstack11l111_opy_ (u"ࠪ࡭ࡩ࠭௶")]
      return None
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡻ࡮ࡺࡨࠡࡨ࡬ࡰࡪࠦ࡬ࡰࡥ࡮࡭ࡳ࡭ࠠࡧࡱࡵࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࡀࠠࡼࡿࠪ௷").format(str(e)))
    return None
def bstack1l11lll11l_opy_(md5_hash, bstack1lll11ll1l_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l111_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨ௸"))
    bstack11lllll11_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"࠭ࡾࠨ௹")), bstack11l111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ௺"))
    if not os.path.exists(bstack11lllll11_opy_):
      os.makedirs(bstack11lllll11_opy_)
    bstack11ll111l1l_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠨࢀࠪ௻")), bstack11l111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ௼"), bstack11l111_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫ௽"))
    bstack1l1ll1ll1l_opy_ = {
      bstack11l111_opy_ (u"ࠫ࡮ࡪࠧ௾"): bstack1lll11ll1l_opy_,
      bstack11l111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ௿"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l111_opy_ (u"࠭ࠥࡥ࠱ࠨࡱ࠴࡙ࠫࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪఀ")),
      bstack11l111_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬఁ"): str(__version__)
    }
    try:
      bstack1ll111111_opy_ = {}
      if os.path.exists(bstack11ll111l1l_opy_):
        bstack1ll111111_opy_ = json.load(open(bstack11ll111l1l_opy_, bstack11l111_opy_ (u"ࠨࡴࡥࠫం")))
      bstack1ll111111_opy_[md5_hash] = bstack1l1ll1ll1l_opy_
      with open(bstack11ll111l1l_opy_, bstack11l111_opy_ (u"ࠤࡺ࠯ࠧః")) as outfile:
        json.dump(bstack1ll111111_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡸࡴࡩࡧࡴࡪࡰࡪࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࠦࡦࡪ࡮ࡨ࠾ࠥࢁࡽࠨఄ").format(str(e)))
    return
  bstack11lllll11_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠫࢃ࠭అ")), bstack11l111_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬఆ"))
  if not os.path.exists(bstack11lllll11_opy_):
    os.makedirs(bstack11lllll11_opy_)
  bstack11ll111l1l_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"࠭ࡾࠨఇ")), bstack11l111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧఈ"), bstack11l111_opy_ (u"ࠨࡣࡳࡴ࡚ࡶ࡬ࡰࡣࡧࡑࡉ࠻ࡈࡢࡵ࡫࠲࡯ࡹ࡯࡯ࠩఉ"))
  lock_file = bstack11ll111l1l_opy_ + bstack11l111_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨఊ")
  bstack1l1ll1ll1l_opy_ = {
    bstack11l111_opy_ (u"ࠪ࡭ࡩ࠭ఋ"): bstack1lll11ll1l_opy_,
    bstack11l111_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧఌ"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l111_opy_ (u"ࠬࠫࡤ࠰ࠧࡰ࠳ࠪ࡟ࠠࠦࡊ࠽ࠩࡒࡀࠥࡔࠩ఍")),
    bstack11l111_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫఎ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1ll111111_opy_ = {}
      if os.path.exists(bstack11ll111l1l_opy_):
        with open(bstack11ll111l1l_opy_, bstack11l111_opy_ (u"ࠧࡳࠩఏ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll111111_opy_ = json.loads(content)
      bstack1ll111111_opy_[md5_hash] = bstack1l1ll1ll1l_opy_
      with open(bstack11ll111l1l_opy_, bstack11l111_opy_ (u"ࠣࡹࠥఐ")) as outfile:
        json.dump(bstack1ll111111_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡹ࡬ࡸ࡭ࠦࡦࡪ࡮ࡨࠤࡱࡵࡣ࡬࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡐࡈ࠺ࠦࡨࡢࡵ࡫ࠤࡺࡶࡤࡢࡶࡨ࠾ࠥࢁࡽࠨ఑").format(str(e)))
def bstack1ll1l11lll_opy_(self):
  return
def bstack11l1lllll1_opy_(self):
  return
def bstack11l1lllll_opy_():
  global bstack11l11l11l1_opy_
  bstack11l11l11l1_opy_ = True
@measure(event_name=EVENTS.bstack1llllll1ll_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack11lllll11l_opy_(self):
  global bstack1ll1ll1l1l_opy_
  global bstack1lll1ll11l_opy_
  global bstack11l11lll1_opy_
  try:
    if bstack11l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪఒ") in bstack1ll1ll1l1l_opy_ and self.session_id != None and bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡕࡷࡥࡹࡻࡳࠨఓ"), bstack11l111_opy_ (u"ࠬ࠭ఔ")) != bstack11l111_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧక"):
      bstack1ll1llll11_opy_ = bstack11l111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧఖ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨగ")
      if bstack1ll1llll11_opy_ == bstack11l111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩఘ"):
        bstack11l11l1l1_opy_(logger)
      if self != None:
        bstack1ll1ll1l11_opy_(self, bstack1ll1llll11_opy_, bstack11l111_opy_ (u"ࠪ࠰ࠥ࠭ఙ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11l111_opy_ (u"ࠫࠬచ")
    if bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬఛ") in bstack1ll1ll1l1l_opy_ and getattr(threading.current_thread(), bstack11l111_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬజ"), None):
      bstack1111l1l1_opy_.bstack1lllllll1_opy_(self, bstack1l1ll1l1l_opy_, logger, wait=True)
    if bstack11l111_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧఝ") in bstack1ll1ll1l1l_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1ll1ll1l11_opy_(self, bstack11l111_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣఞ"))
      bstack11111ll111_opy_.bstack11l1111l1_opy_(self)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠ࡮ࡣࡵ࡯࡮ࡴࡧࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࠥట") + str(e))
  bstack11l11lll1_opy_(self)
  self.session_id = None
def bstack1l1lllll1_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack111llll1ll_opy_
    global bstack1ll1ll1l1l_opy_
    command_executor = kwargs.get(bstack11l111_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡣࡪࡾࡥࡤࡷࡷࡳࡷ࠭ఠ"), bstack11l111_opy_ (u"ࠫࠬడ"))
    bstack1ll11lll11_opy_ = False
    if type(command_executor) == str and bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨఢ") in command_executor:
      bstack1ll11lll11_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩణ") in str(getattr(command_executor, bstack11l111_opy_ (u"ࠧࡠࡷࡵࡰࠬత"), bstack11l111_opy_ (u"ࠨࠩథ"))):
      bstack1ll11lll11_opy_ = True
    else:
      kwargs = bstack11l111l1_opy_.bstack11l1l1l1l_opy_(bstack11llll1111_opy_=kwargs, config=CONFIG)
      return bstack1ll1lllll1_opy_(self, *args, **kwargs)
    if bstack1ll11lll11_opy_:
      bstack11l1ll1l1_opy_ = bstack111ll1l11_opy_.bstack1ll11lll1_opy_(CONFIG, bstack1ll1ll1l1l_opy_)
      if kwargs.get(bstack11l111_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪద")):
        kwargs[bstack11l111_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫధ")] = bstack111llll1ll_opy_(kwargs[bstack11l111_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬన")], bstack1ll1ll1l1l_opy_, CONFIG, bstack11l1ll1l1_opy_)
      elif kwargs.get(bstack11l111_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ఩")):
        kwargs[bstack11l111_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ప")] = bstack111llll1ll_opy_(kwargs[bstack11l111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧఫ")], bstack1ll1ll1l1l_opy_, CONFIG, bstack11l1ll1l1_opy_)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪࡨࡲࠥࡶࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡖࡈࡐࠦࡣࡢࡲࡶ࠾ࠥࢁࡽࠣబ").format(str(e)))
  return bstack1ll1lllll1_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack111llll11_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack1l11l11111_opy_(self, command_executor=bstack11l111_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱࠴࠶࠼࠴࠰࠯࠲࠱࠵࠿࠺࠴࠵࠶ࠥభ"), *args, **kwargs):
  global bstack1lll1ll11l_opy_
  global bstack1l111ll1ll_opy_
  bstack1l111111l_opy_ = bstack1l1lllll1_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1l1l11l1_opy_.on():
    return bstack1l111111l_opy_
  try:
    logger.debug(bstack11l111_opy_ (u"ࠪࡇࡴࡳ࡭ࡢࡰࡧࠤࡊࡾࡥࡤࡷࡷࡳࡷࠦࡷࡩࡧࡱࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡪࡵࠣࡪࡦࡲࡳࡦࠢ࠰ࠤࢀࢃࠧమ").format(str(command_executor)))
    logger.debug(bstack11l111_opy_ (u"ࠫࡍࡻࡢࠡࡗࡕࡐࠥ࡯ࡳࠡ࠯ࠣࡿࢂ࠭య").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨర") in command_executor._url:
      bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧఱ"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪల") in command_executor):
    bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩళ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1ll111l1l1_opy_ = getattr(threading.current_thread(), bstack11l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪఴ"), None)
  bstack111l1ll1l_opy_ = {}
  if self.capabilities is not None:
    bstack111l1ll1l_opy_[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩవ")] = self.capabilities.get(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩశ"))
    bstack111l1ll1l_opy_[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧష")] = self.capabilities.get(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧస"))
    bstack111l1ll1l_opy_[bstack11l111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫࡟ࡰࡲࡷ࡭ࡴࡴࡳࠨహ")] = self.capabilities.get(bstack11l111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭఺"))
  if CONFIG.get(bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ఻"), False) and bstack11l111l1_opy_.bstack111ll11ll1_opy_(bstack111l1ll1l_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack11l111_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧ఼ࠪ") in bstack1ll1ll1l1l_opy_ or bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪఽ") in bstack1ll1ll1l1l_opy_:
    bstack1lll1l1l_opy_.bstack1lll111l11_opy_(self)
  if bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬా") in bstack1ll1ll1l1l_opy_ and bstack1ll111l1l1_opy_ and bstack1ll111l1l1_opy_.get(bstack11l111_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ి"), bstack11l111_opy_ (u"ࠧࠨీ")) == bstack11l111_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩు"):
    bstack1lll1l1l_opy_.bstack1lll111l11_opy_(self)
  bstack1lll1ll11l_opy_ = self.session_id
  with bstack11l1111ll1_opy_:
    bstack1l111ll1ll_opy_.append(self)
  return bstack1l111111l_opy_
def bstack1l1lll11l1_opy_(args):
  return bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴࠪూ") in str(args)
def bstack1111ll1lll_opy_(self, driver_command, *args, **kwargs):
  global bstack11llllllll_opy_
  global bstack1llll1111l_opy_
  bstack1l1l1lll1_opy_ = bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧృ"), None) and bstack1l11lll1_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪౄ"), None)
  bstack1l1ll11l1_opy_ = bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ౅"), None) and bstack1l11lll1_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨె"), None)
  bstack1l1ll111l_opy_ = getattr(self, bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧే"), None) != None and getattr(self, bstack11l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨై"), None) == True
  if not bstack1llll1111l_opy_ and bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ౉") in CONFIG and CONFIG[bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪొ")] == True and bstack1l1l1ll111_opy_.bstack1111lll111_opy_(driver_command) and (bstack1l1ll111l_opy_ or bstack1l1l1lll1_opy_ or bstack1l1ll11l1_opy_) and not bstack1l1lll11l1_opy_(args):
    try:
      bstack1llll1111l_opy_ = True
      logger.debug(bstack11l111_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡿࢂ࠭ో").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11l111_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡲࡨࡶ࡫ࡵࡲ࡮ࠢࡶࡧࡦࡴࠠࡼࡿࠪౌ").format(str(err)))
    bstack1llll1111l_opy_ = False
  response = bstack11llllllll_opy_(self, driver_command, *args, **kwargs)
  if (bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸ్ࠬ") in str(bstack1ll1ll1l1l_opy_).lower() or bstack11l111_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ౎") in str(bstack1ll1ll1l1l_opy_).lower()) and bstack1l1l11l1_opy_.on():
    try:
      if driver_command == bstack11l111_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬ౏"):
        bstack1lll1l1l_opy_.bstack11ll1ll11_opy_({
            bstack11l111_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ౐"): response[bstack11l111_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ౑")],
            bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ౒"): bstack1lll1l1l_opy_.current_test_uuid() if bstack1lll1l1l_opy_.current_test_uuid() else bstack1l1l11l1_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack11l111lll1_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack11111ll11_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1lll1ll11l_opy_
  global bstack11l1llll1_opy_
  global bstack1111llll11_opy_
  global bstack1ll11ll111_opy_
  global bstack1l1ll11l1l_opy_
  global bstack1ll1ll1l1l_opy_
  global bstack1ll1lllll1_opy_
  global bstack1l111ll1ll_opy_
  global bstack11ll111111_opy_
  global bstack1l1ll1l1l_opy_
  if os.getenv(bstack11l111_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ౓")) is not None and bstack11l111l1_opy_.bstack1lll1l1lll_opy_(CONFIG) is None:
    CONFIG[bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭౔")] = True
  CONFIG[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌౕࠩ")] = str(bstack1ll1ll1l1l_opy_) + str(__version__)
  bstack1ll11111l_opy_ = os.environ[bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉౖ࠭")]
  bstack11l1ll1l1_opy_ = bstack111ll1l11_opy_.bstack1ll11lll1_opy_(CONFIG, bstack1ll1ll1l1l_opy_)
  CONFIG[bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬ౗")] = bstack1ll11111l_opy_
  CONFIG[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬౘ")] = bstack11l1ll1l1_opy_
  if CONFIG.get(bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫౙ"),bstack11l111_opy_ (u"ࠬ࠭ౚ")) and bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ౛") in bstack1ll1ll1l1l_opy_:
    CONFIG[bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ౜")].pop(bstack11l111_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ౝ"), None)
    CONFIG[bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ౞")].pop(bstack11l111_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ౟"), None)
  command_executor = bstack111l1111l1_opy_()
  logger.debug(bstack1l11l1l1l_opy_.format(command_executor))
  proxy = bstack111111111_opy_(CONFIG, proxy)
  bstack1l1lll1l1l_opy_ = 0 if bstack11l1llll1_opy_ < 0 else bstack11l1llll1_opy_
  try:
    if bstack1ll11ll111_opy_ is True:
      bstack1l1lll1l1l_opy_ = int(multiprocessing.current_process().name)
    elif bstack1l1ll11l1l_opy_ is True:
      bstack1l1lll1l1l_opy_ = int(threading.current_thread().name)
  except:
    bstack1l1lll1l1l_opy_ = 0
  bstack1l1l11lll1_opy_ = bstack1ll1111l1l_opy_(CONFIG, bstack1l1lll1l1l_opy_)
  logger.debug(bstack11l1ll11l1_opy_.format(str(bstack1l1l11lll1_opy_)))
  if bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨౠ") in CONFIG and bstack11lll1lll_opy_(CONFIG[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩౡ")]):
    bstack1l1l1ll1ll_opy_(bstack1l1l11lll1_opy_)
  if bstack11l111l1_opy_.bstack1ll1l1l111_opy_(CONFIG, bstack1l1lll1l1l_opy_) and bstack11l111l1_opy_.bstack11lll111l1_opy_(bstack1l1l11lll1_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack11l111l1_opy_.set_capabilities(bstack1l1l11lll1_opy_, CONFIG)
  if desired_capabilities:
    bstack1l1lll11l_opy_ = bstack1l1l1lllll_opy_(desired_capabilities)
    bstack1l1lll11l_opy_[bstack11l111_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ౢ")] = bstack1l11ll1ll1_opy_(CONFIG)
    bstack1l111ll111_opy_ = bstack1ll1111l1l_opy_(bstack1l1lll11l_opy_)
    if bstack1l111ll111_opy_:
      bstack1l1l11lll1_opy_ = update(bstack1l111ll111_opy_, bstack1l1l11lll1_opy_)
    desired_capabilities = None
  if options:
    bstack11llll111l_opy_(options, bstack1l1l11lll1_opy_)
  if not options:
    options = bstack1ll11l1111_opy_(bstack1l1l11lll1_opy_)
  bstack1l1ll1l1l_opy_ = CONFIG.get(bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪౣ"))[bstack1l1lll1l1l_opy_]
  if proxy and bstack1l11l1l11l_opy_() >= version.parse(bstack11l111_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨ౤")):
    options.proxy(proxy)
  if options and bstack1l11l1l11l_opy_() >= version.parse(bstack11l111_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨ౥")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1l11l1l11l_opy_() < version.parse(bstack11l111_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩ౦")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1l1l11lll1_opy_)
  logger.info(bstack11l1l111ll_opy_)
  bstack1ll1111111_opy_.end(EVENTS.bstack111llllll1_opy_.value, EVENTS.bstack111llllll1_opy_.value + bstack11l111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦ౧"), EVENTS.bstack111llllll1_opy_.value + bstack11l111_opy_ (u"ࠧࡀࡥ࡯ࡦࠥ౨"), status=True, failure=None, test_name=bstack1111llll11_opy_)
  if bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡱࡴࡲࡪ࡮ࡲࡥࠨ౩") in kwargs:
    del kwargs[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡲࡵࡳ࡫࡯࡬ࡦࠩ౪")]
  try:
    if bstack1l11l1l11l_opy_() >= version.parse(bstack11l111_opy_ (u"ࠨ࠶࠱࠵࠵࠴࠰ࠨ౫")):
      bstack1ll1lllll1_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack1l11l1l11l_opy_() >= version.parse(bstack11l111_opy_ (u"ࠩ࠶࠲࠽࠴࠰ࠨ౬")):
      bstack1ll1lllll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1l11l1l11l_opy_() >= version.parse(bstack11l111_opy_ (u"ࠪ࠶࠳࠻࠳࠯࠲ࠪ౭")):
      bstack1ll1lllll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1ll1lllll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack1lll111l1l_opy_:
    logger.error(bstack1l11l11l1l_opy_.format(bstack11l111_opy_ (u"ࠫࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠪ౮"), str(bstack1lll111l1l_opy_)))
    raise bstack1lll111l1l_opy_
  if bstack11l111l1_opy_.bstack1ll1l1l111_opy_(CONFIG, bstack1l1lll1l1l_opy_) and bstack11l111l1_opy_.bstack11lll111l1_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧ౯")][bstack11l111_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ౰")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack11l111l1_opy_.set_capabilities(bstack1l1l11lll1_opy_, CONFIG)
  try:
    bstack1l1lllll11_opy_ = bstack11l111_opy_ (u"ࠧࠨ౱")
    if bstack1l11l1l11l_opy_() >= version.parse(bstack11l111_opy_ (u"ࠨ࠶࠱࠴࠳࠶ࡢ࠲ࠩ౲")):
      if self.caps is not None:
        bstack1l1lllll11_opy_ = self.caps.get(bstack11l111_opy_ (u"ࠤࡲࡴࡹ࡯࡭ࡢ࡮ࡋࡹࡧ࡛ࡲ࡭ࠤ౳"))
    else:
      if self.capabilities is not None:
        bstack1l1lllll11_opy_ = self.capabilities.get(bstack11l111_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥ౴"))
    if bstack1l1lllll11_opy_:
      bstack11ll11lll1_opy_(bstack1l1lllll11_opy_)
      if bstack1l11l1l11l_opy_() <= version.parse(bstack11l111_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫ౵")):
        self.command_executor._url = bstack11l111_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࠨ౶") + bstack11111llll1_opy_ + bstack11l111_opy_ (u"ࠨ࠺࠹࠲࠲ࡻࡩ࠵ࡨࡶࡤࠥ౷")
      else:
        self.command_executor._url = bstack11l111_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤ౸") + bstack1l1lllll11_opy_ + bstack11l111_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤ౹")
      logger.debug(bstack1ll11ll11l_opy_.format(bstack1l1lllll11_opy_))
    else:
      logger.debug(bstack1ll1llllll_opy_.format(bstack11l111_opy_ (u"ࠤࡒࡴࡹ࡯࡭ࡢ࡮ࠣࡌࡺࡨࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠥ౺")))
  except Exception as e:
    logger.debug(bstack1ll1llllll_opy_.format(e))
  if bstack11l111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ౻") in bstack1ll1ll1l1l_opy_:
    bstack1l1l1ll11l_opy_(bstack11l1llll1_opy_, bstack11ll111111_opy_)
  bstack1lll1ll11l_opy_ = self.session_id
  if bstack11l111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ౼") in bstack1ll1ll1l1l_opy_ or bstack11l111_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ౽") in bstack1ll1ll1l1l_opy_ or bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ౾") in bstack1ll1ll1l1l_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1ll111l1l1_opy_ = getattr(threading.current_thread(), bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡔࡦࡵࡷࡑࡪࡺࡡࠨ౿"), None)
  if bstack11l111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨಀ") in bstack1ll1ll1l1l_opy_ or bstack11l111_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨಁ") in bstack1ll1ll1l1l_opy_:
    bstack1lll1l1l_opy_.bstack1lll111l11_opy_(self)
  if bstack11l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪಂ") in bstack1ll1ll1l1l_opy_ and bstack1ll111l1l1_opy_ and bstack1ll111l1l1_opy_.get(bstack11l111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫಃ"), bstack11l111_opy_ (u"ࠬ࠭಄")) == bstack11l111_opy_ (u"࠭ࡰࡦࡰࡧ࡭ࡳ࡭ࠧಅ"):
    bstack1lll1l1l_opy_.bstack1lll111l11_opy_(self)
  with bstack11l1111ll1_opy_:
    bstack1l111ll1ll_opy_.append(self)
  if bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪಆ") in CONFIG and bstack11l111_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ಇ") in CONFIG[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಈ")][bstack1l1lll1l1l_opy_]:
    bstack1111llll11_opy_ = CONFIG[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಉ")][bstack1l1lll1l1l_opy_][bstack11l111_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩಊ")]
  logger.debug(bstack111l11l11_opy_.format(bstack1lll1ll11l_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1111l1111l_opy_
    def bstack11lll1ll1_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1ll11l11l1_opy_
      if(bstack11l111_opy_ (u"ࠧ࡯࡮ࡥࡧࡻ࠲࡯ࡹࠢಋ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11l111_opy_ (u"࠭ࡾࠨಌ")), bstack11l111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ಍"), bstack11l111_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪಎ")), bstack11l111_opy_ (u"ࠩࡺࠫಏ")) as fp:
          fp.write(bstack11l111_opy_ (u"ࠥࠦಐ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11l111_opy_ (u"ࠦ࡮ࡴࡤࡦࡺࡢࡦࡸࡺࡡࡤ࡭࠱࡮ࡸࠨ಑")))):
          with open(args[1], bstack11l111_opy_ (u"ࠬࡸࠧಒ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11l111_opy_ (u"࠭ࡡࡴࡻࡱࡧࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡠࡰࡨࡻࡕࡧࡧࡦࠪࡦࡳࡳࡺࡥࡹࡶ࠯ࠤࡵࡧࡧࡦࠢࡀࠤࡻࡵࡩࡥࠢ࠳࠭ࠬಓ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack11lll1lll1_opy_)
            if bstack11l111_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫಔ") in CONFIG and str(CONFIG[bstack11l111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬಕ")]).lower() != bstack11l111_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨಖ"):
                bstack1ll1l11l11_opy_ = bstack1111l1111l_opy_()
                bstack11l1l1lll_opy_ = bstack11l111_opy_ (u"ࠪࠫࠬࠐ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠌࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭ࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࡠ࠿ࠏࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠶ࡣ࠻ࠋࡥࡲࡲࡸࡺࠠࡱࡡ࡬ࡲࡩ࡫ࡸࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠶ࡢࡁࠊࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮ࡴ࡮࡬ࡧࡪ࠮࠰࠭ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷࠮ࡁࠊࡤࡱࡱࡷࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮ࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ࠯࠻ࠋ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰ࠴ࡣࡩࡴࡲࡱ࡮ࡻ࡭࠯࡮ࡤࡹࡳࡩࡨࠡ࠿ࠣࡥࡸࡿ࡮ࡤࠢࠫࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵࠬࠤࡂࡄࠠࡼࡽࠍࠤࠥࡲࡥࡵࠢࡦࡥࡵࡹ࠻ࠋࠢࠣࡸࡷࡿࠠࡼࡽࠍࠤࠥࠦࠠࡤࡣࡳࡷࠥࡃࠠࡋࡕࡒࡒ࠳ࡶࡡࡳࡵࡨࠬࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠫ࠾ࠎࠥࠦࡽࡾࠢࡦࡥࡹࡩࡨࠡࠪࡨࡼ࠮ࠦࡻࡼࠌࠣࠤࠥࠦࡣࡰࡰࡶࡳࡱ࡫࠮ࡦࡴࡵࡳࡷ࠮ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡦࡸࡳࡦࠢࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳ࠻ࠤ࠯ࠤࡪࡾࠩ࠼ࠌࠣࠤࢂࢃࠊࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡤࡻࡦ࡯ࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰ࠴ࡣࡩࡴࡲࡱ࡮ࡻ࡭࠯ࡥࡲࡲࡳ࡫ࡣࡵࠪࡾࡿࠏࠦࠠࠡࠢࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹࡀࠠࠨࡽࡦࡨࡵ࡛ࡲ࡭ࡿࠪࠤ࠰ࠦࡥ࡯ࡥࡲࡨࡪ࡛ࡒࡊࡅࡲࡱࡵࡵ࡮ࡦࡰࡷࠬࡏ࡙ࡏࡏ࠰ࡶࡸࡷ࡯࡮ࡨ࡫ࡩࡽ࠭ࡩࡡࡱࡵࠬ࠭࠱ࠐࠠࠡࠢࠣ࠲࠳࠴࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸࠐࠠࠡࡿࢀ࠭ࡀࠐࡽࡾ࠽ࠍ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࠐࠧࠨࠩಗ").format(bstack1ll1l11l11_opy_=bstack1ll1l11l11_opy_)
            lines.insert(1, bstack11l1l1lll_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11l111_opy_ (u"ࠦ࡮ࡴࡤࡦࡺࡢࡦࡸࡺࡡࡤ࡭࠱࡮ࡸࠨಘ")), bstack11l111_opy_ (u"ࠬࡽࠧಙ")) as bstack1111lll11_opy_:
              bstack1111lll11_opy_.writelines(lines)
        CONFIG[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡘࡊࡋࠨಚ")] = str(bstack1ll1ll1l1l_opy_) + str(__version__)
        bstack1ll11111l_opy_ = os.environ[bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬಛ")]
        bstack11l1ll1l1_opy_ = bstack111ll1l11_opy_.bstack1ll11lll1_opy_(CONFIG, bstack1ll1ll1l1l_opy_)
        CONFIG[bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫಜ")] = bstack1ll11111l_opy_
        CONFIG[bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫಝ")] = bstack11l1ll1l1_opy_
        bstack1l1lll1l1l_opy_ = 0 if bstack11l1llll1_opy_ < 0 else bstack11l1llll1_opy_
        try:
          if bstack1ll11ll111_opy_ is True:
            bstack1l1lll1l1l_opy_ = int(multiprocessing.current_process().name)
          elif bstack1l1ll11l1l_opy_ is True:
            bstack1l1lll1l1l_opy_ = int(threading.current_thread().name)
        except:
          bstack1l1lll1l1l_opy_ = 0
        CONFIG[bstack11l111_opy_ (u"ࠥࡹࡸ࡫ࡗ࠴ࡅࠥಞ")] = False
        CONFIG[bstack11l111_opy_ (u"ࠦ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥಟ")] = True
        bstack1l1l11lll1_opy_ = bstack1ll1111l1l_opy_(CONFIG, bstack1l1lll1l1l_opy_)
        logger.debug(bstack11l1ll11l1_opy_.format(str(bstack1l1l11lll1_opy_)))
        if CONFIG.get(bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩಠ")):
          bstack1l1l1ll1ll_opy_(bstack1l1l11lll1_opy_)
        if bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಡ") in CONFIG and bstack11l111_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬಢ") in CONFIG[bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಣ")][bstack1l1lll1l1l_opy_]:
          bstack1111llll11_opy_ = CONFIG[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬತ")][bstack1l1lll1l1l_opy_][bstack11l111_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨಥ")]
        args.append(os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠫࢃ࠭ದ")), bstack11l111_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬಧ"), bstack11l111_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨನ")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1l1l11lll1_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11l111_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤ಩"))
      bstack1ll11l11l1_opy_ = True
      return bstack11l111ll11_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack1lll111ll_opy_(self,
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
    global bstack11l1llll1_opy_
    global bstack1111llll11_opy_
    global bstack1ll11ll111_opy_
    global bstack1l1ll11l1l_opy_
    global bstack1ll1ll1l1l_opy_
    CONFIG[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪಪ")] = str(bstack1ll1ll1l1l_opy_) + str(__version__)
    bstack1ll11111l_opy_ = os.environ[bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧಫ")]
    bstack11l1ll1l1_opy_ = bstack111ll1l11_opy_.bstack1ll11lll1_opy_(CONFIG, bstack1ll1ll1l1l_opy_)
    CONFIG[bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ಬ")] = bstack1ll11111l_opy_
    CONFIG[bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ಭ")] = bstack11l1ll1l1_opy_
    bstack1l1lll1l1l_opy_ = 0 if bstack11l1llll1_opy_ < 0 else bstack11l1llll1_opy_
    try:
      if bstack1ll11ll111_opy_ is True:
        bstack1l1lll1l1l_opy_ = int(multiprocessing.current_process().name)
      elif bstack1l1ll11l1l_opy_ is True:
        bstack1l1lll1l1l_opy_ = int(threading.current_thread().name)
    except:
      bstack1l1lll1l1l_opy_ = 0
    CONFIG[bstack11l111_opy_ (u"ࠧ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦಮ")] = True
    bstack1l1l11lll1_opy_ = bstack1ll1111l1l_opy_(CONFIG, bstack1l1lll1l1l_opy_)
    logger.debug(bstack11l1ll11l1_opy_.format(str(bstack1l1l11lll1_opy_)))
    if CONFIG.get(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪಯ")):
      bstack1l1l1ll1ll_opy_(bstack1l1l11lll1_opy_)
    if bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪರ") in CONFIG and bstack11l111_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ಱ") in CONFIG[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಲ")][bstack1l1lll1l1l_opy_]:
      bstack1111llll11_opy_ = CONFIG[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಳ")][bstack1l1lll1l1l_opy_][bstack11l111_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ಴")]
    import urllib
    import json
    if bstack11l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩವ") in CONFIG and str(CONFIG[bstack11l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪಶ")]).lower() != bstack11l111_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ಷ"):
        bstack1l1ll111l1_opy_ = bstack1111l1111l_opy_()
        bstack1ll1l11l11_opy_ = bstack1l1ll111l1_opy_ + urllib.parse.quote(json.dumps(bstack1l1l11lll1_opy_))
    else:
        bstack1ll1l11l11_opy_ = bstack11l111_opy_ (u"ࠨࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠪಸ") + urllib.parse.quote(json.dumps(bstack1l1l11lll1_opy_))
    browser = self.connect(bstack1ll1l11l11_opy_)
    return browser
except Exception as e:
    pass
def bstack1111l1l1l_opy_():
    global bstack1ll11l11l1_opy_
    global bstack1ll1ll1l1l_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1llllll1l1_opy_
        global bstack111ll111_opy_
        if not bstack1l1111l11_opy_:
          global bstack1111l1l1l1_opy_
          if not bstack1111l1l1l1_opy_:
            from bstack_utils.helper import bstack11ll1l11ll_opy_, bstack1111l11l11_opy_, bstack11ll1l1l11_opy_
            bstack1111l1l1l1_opy_ = bstack11ll1l11ll_opy_()
            bstack1111l11l11_opy_(bstack1ll1ll1l1l_opy_)
            bstack11l1ll1l1_opy_ = bstack111ll1l11_opy_.bstack1ll11lll1_opy_(CONFIG, bstack1ll1ll1l1l_opy_)
            bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"ࠤࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡐࡓࡑࡇ࡙ࡈ࡚࡟ࡎࡃࡓࠦಹ"), bstack11l1ll1l1_opy_)
          BrowserType.connect = bstack1llllll1l1_opy_
          return
        BrowserType.launch = bstack1lll111ll_opy_
        bstack1ll11l11l1_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack11lll1ll1_opy_
      bstack1ll11l11l1_opy_ = True
    except Exception as e:
      pass
def bstack1l1ll1lll1_opy_(context, bstack11l111llll_opy_):
  try:
    context.page.evaluate(bstack11l111_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ಺"), bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨ಻")+ json.dumps(bstack11l111llll_opy_) + bstack11l111_opy_ (u"ࠧࢃࡽ಼ࠣ"))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀ࠾ࠥࢁࡽࠣಽ").format(str(e), traceback.format_exc()))
def bstack1lllllll11_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11l111_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣಾ"), bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ಿ") + json.dumps(message) + bstack11l111_opy_ (u"ࠩ࠯ࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠬೀ") + json.dumps(level) + bstack11l111_opy_ (u"ࠪࢁࢂ࠭ು"))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡢࡰࡱࡳࡹࡧࡴࡪࡱࡱࠤࢀࢃ࠺ࠡࡽࢀࠦೂ").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1l11lll111_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack1111ll11ll_opy_(self, url):
  global bstack11l11l11ll_opy_
  try:
    bstack1l11111l1l_opy_(url)
  except Exception as err:
    logger.debug(bstack11l11l1l1l_opy_.format(str(err)))
  try:
    bstack11l11l11ll_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack11111111l_opy_):
        bstack1l11111l1l_opy_(url, True)
    except Exception as err:
      logger.debug(bstack11l11l1l1l_opy_.format(str(err)))
    raise e
def bstack1111ll1111_opy_(self):
  global bstack11ll111l1_opy_
  bstack11ll111l1_opy_ = self
  return
def bstack1l1111l111_opy_(self):
  global bstack1l111l1lll_opy_
  bstack1l111l1lll_opy_ = self
  return
def bstack1ll1lll11l_opy_(test_name, bstack1l1lll1ll1_opy_):
  global CONFIG
  if percy.bstack1111l11lll_opy_() == bstack11l111_opy_ (u"ࠧࡺࡲࡶࡧࠥೃ"):
    bstack11l1l1lll1_opy_ = os.path.relpath(bstack1l1lll1ll1_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack11l1l1lll1_opy_)
    bstack1l1l111l11_opy_ = suite_name + bstack11l111_opy_ (u"ࠨ࠭ࠣೄ") + test_name
    threading.current_thread().percySessionName = bstack1l1l111l11_opy_
def bstack11llll11ll_opy_(self, test, *args, **kwargs):
  global bstack1111llllll_opy_
  test_name = None
  bstack1l1lll1ll1_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1l1lll1ll1_opy_ = str(test.source)
  bstack1ll1lll11l_opy_(test_name, bstack1l1lll1ll1_opy_)
  bstack1111llllll_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1lll11lll1_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack1111llll1l_opy_(driver, bstack1l1l111l11_opy_):
  if not bstack11l1ll1lll_opy_ and bstack1l1l111l11_opy_:
      bstack11l1ll111l_opy_ = {
          bstack11l111_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ೅"): bstack11l111_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩೆ"),
          bstack11l111_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬೇ"): {
              bstack11l111_opy_ (u"ࠪࡲࡦࡳࡥࠨೈ"): bstack1l1l111l11_opy_
          }
      }
      bstack1111l11ll1_opy_ = bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ೉").format(json.dumps(bstack11l1ll111l_opy_))
      driver.execute_script(bstack1111l11ll1_opy_)
  if bstack111l1ll1l1_opy_:
      bstack1lllll11ll_opy_ = {
          bstack11l111_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬೊ"): bstack11l111_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨೋ"),
          bstack11l111_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪೌ"): {
              bstack11l111_opy_ (u"ࠨࡦࡤࡸࡦ್࠭"): bstack1l1l111l11_opy_ + bstack11l111_opy_ (u"ࠩࠣࡴࡦࡹࡳࡦࡦࠤࠫ೎"),
              bstack11l111_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩ೏"): bstack11l111_opy_ (u"ࠫ࡮ࡴࡦࡰࠩ೐")
          }
      }
      if bstack111l1ll1l1_opy_.status == bstack11l111_opy_ (u"ࠬࡖࡁࡔࡕࠪ೑"):
          bstack1ll1l11ll1_opy_ = bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ೒").format(json.dumps(bstack1lllll11ll_opy_))
          driver.execute_script(bstack1ll1l11ll1_opy_)
          bstack1ll1ll1l11_opy_(driver, bstack11l111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ೓"))
      elif bstack111l1ll1l1_opy_.status == bstack11l111_opy_ (u"ࠨࡈࡄࡍࡑ࠭೔"):
          reason = bstack11l111_opy_ (u"ࠤࠥೕ")
          bstack11lll11l1l_opy_ = bstack1l1l111l11_opy_ + bstack11l111_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠫೖ")
          if bstack111l1ll1l1_opy_.message:
              reason = str(bstack111l1ll1l1_opy_.message)
              bstack11lll11l1l_opy_ = bstack11lll11l1l_opy_ + bstack11l111_opy_ (u"ࠫࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳ࠼ࠣࠫ೗") + reason
          bstack1lllll11ll_opy_[bstack11l111_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ೘")] = {
              bstack11l111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ೙"): bstack11l111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭೚"),
              bstack11l111_opy_ (u"ࠨࡦࡤࡸࡦ࠭೛"): bstack11lll11l1l_opy_
          }
          bstack1ll1l11ll1_opy_ = bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧ೜").format(json.dumps(bstack1lllll11ll_opy_))
          driver.execute_script(bstack1ll1l11ll1_opy_)
          bstack1ll1ll1l11_opy_(driver, bstack11l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪೝ"), reason)
          bstack1ll1l1llll_opy_(reason, str(bstack111l1ll1l1_opy_), str(bstack11l1llll1_opy_), logger)
@measure(event_name=EVENTS.bstack11ll1l1ll1_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack111111l11_opy_(driver, test):
  if percy.bstack1111l11lll_opy_() == bstack11l111_opy_ (u"ࠦࡹࡸࡵࡦࠤೞ") and percy.bstack11l11l1ll_opy_() == bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡦࡥࡸ࡫ࠢ೟"):
      bstack11ll1lllll_opy_ = bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩೠ"), None)
      bstack11ll111ll_opy_(driver, bstack11ll1lllll_opy_, test)
  if (bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫೡ"), None) and
      bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧೢ"), None)) or (
      bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩೣ"), None) and
      bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ೤"), None)):
      logger.info(bstack11l111_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠢࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡮ࡹࠠࡶࡰࡧࡩࡷࡽࡡࡺ࠰ࠣࠦ೥"))
      bstack11l111l1_opy_.bstack11l11lll_opy_(driver, name=test.name, path=test.source)
def bstack1l111l1l1l_opy_(test, bstack1l1l111l11_opy_):
    try:
      bstack1lll1l1ll1_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack11l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ೦")] = bstack1l1l111l11_opy_
      if bstack111l1ll1l1_opy_:
        if bstack111l1ll1l1_opy_.status == bstack11l111_opy_ (u"࠭ࡐࡂࡕࡖࠫ೧"):
          data[bstack11l111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ೨")] = bstack11l111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ೩")
        elif bstack111l1ll1l1_opy_.status == bstack11l111_opy_ (u"ࠩࡉࡅࡎࡒࠧ೪"):
          data[bstack11l111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ೫")] = bstack11l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ೬")
          if bstack111l1ll1l1_opy_.message:
            data[bstack11l111_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ೭")] = str(bstack111l1ll1l1_opy_.message)
      user = CONFIG[bstack11l111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ೮")]
      key = CONFIG[bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ೯")]
      host = bstack111l11l1l_opy_(cli.config, [bstack11l111_opy_ (u"ࠣࡣࡳ࡭ࡸࠨ೰"), bstack11l111_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦೱ"), bstack11l111_opy_ (u"ࠥࡥࡵ࡯ࠢೲ")], bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠧೳ"))
      url = bstack11l111_opy_ (u"ࠬࢁࡽ࠰ࡣࡸࡸࡴࡳࡡࡵࡧ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠴ࢁࡽ࠯࡬ࡶࡳࡳ࠭೴").format(host, bstack1lll1ll11l_opy_)
      headers = {
        bstack11l111_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬ೵"): bstack11l111_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ೶"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠣࡪࡷࡸࡵࡀࡵࡱࡦࡤࡸࡪࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡴࡢࡶࡸࡷࠧ೷"), datetime.datetime.now() - bstack1lll1l1ll1_opy_)
    except Exception as e:
      logger.error(bstack1l111111ll_opy_.format(str(e)))
def bstack11l111ll1_opy_(test, bstack1l1l111l11_opy_):
  global CONFIG
  global bstack1l111l1lll_opy_
  global bstack11ll111l1_opy_
  global bstack1lll1ll11l_opy_
  global bstack111l1ll1l1_opy_
  global bstack1111llll11_opy_
  global bstack11ll1lll11_opy_
  global bstack11l1llll1l_opy_
  global bstack11l1l11111_opy_
  global bstack1l11111l1_opy_
  global bstack1l111ll1ll_opy_
  global bstack1l1ll1l1l_opy_
  global bstack1l1l1lll11_opy_
  try:
    if not bstack1lll1ll11l_opy_:
      with bstack1l1l1lll11_opy_:
        bstack1111l1l11l_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠩࢁࠫ೸")), bstack11l111_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ೹"), bstack11l111_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭೺"))
        if os.path.exists(bstack1111l1l11l_opy_):
          with open(bstack1111l1l11l_opy_, bstack11l111_opy_ (u"ࠬࡸࠧ೻")) as f:
            content = f.read().strip()
            if content:
              bstack11l11lll11_opy_ = json.loads(bstack11l111_opy_ (u"ࠨࡻࠣ೼") + content + bstack11l111_opy_ (u"ࠧࠣࡺࠥ࠾ࠥࠨࡹࠣࠩ೽") + bstack11l111_opy_ (u"ࠣࡿࠥ೾"))
              bstack1lll1ll11l_opy_ = bstack11l11lll11_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡍࡉࡹࠠࡧ࡫࡯ࡩ࠿ࠦࠧ೿") + str(e))
  if bstack1l111ll1ll_opy_:
    with bstack11l1111ll1_opy_:
      bstack11ll11l11l_opy_ = bstack1l111ll1ll_opy_.copy()
    for driver in bstack11ll11l11l_opy_:
      if bstack1lll1ll11l_opy_ == driver.session_id:
        if test:
          bstack111111l11_opy_(driver, test)
        bstack1111llll1l_opy_(driver, bstack1l1l111l11_opy_)
  elif bstack1lll1ll11l_opy_:
    bstack1l111l1l1l_opy_(test, bstack1l1l111l11_opy_)
  if bstack1l111l1lll_opy_:
    bstack11l1llll1l_opy_(bstack1l111l1lll_opy_)
  if bstack11ll111l1_opy_:
    bstack11l1l11111_opy_(bstack11ll111l1_opy_)
  if bstack11l11l11l1_opy_:
    bstack1l11111l1_opy_()
def bstack1l111l1111_opy_(self, test, *args, **kwargs):
  bstack1l1l111l11_opy_ = None
  if test:
    bstack1l1l111l11_opy_ = str(test.name)
  bstack11l111ll1_opy_(test, bstack1l1l111l11_opy_)
  bstack11ll1lll11_opy_(self, test, *args, **kwargs)
def bstack1l1llllll1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11l1l11l1l_opy_
  global CONFIG
  global bstack1l111ll1ll_opy_
  global bstack1lll1ll11l_opy_
  global bstack1l1l1lll11_opy_
  bstack11l1ll11ll_opy_ = None
  try:
    if bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩഀ"), None) or bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ഁ"), None):
      try:
        if not bstack1lll1ll11l_opy_:
          bstack1111l1l11l_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠬࢄࠧം")), bstack11l111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ഃ"), bstack11l111_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩഄ"))
          with bstack1l1l1lll11_opy_:
            if os.path.exists(bstack1111l1l11l_opy_):
              with open(bstack1111l1l11l_opy_, bstack11l111_opy_ (u"ࠨࡴࠪഅ")) as f:
                content = f.read().strip()
                if content:
                  bstack11l11lll11_opy_ = json.loads(bstack11l111_opy_ (u"ࠤࡾࠦആ") + content + bstack11l111_opy_ (u"ࠪࠦࡽࠨ࠺ࠡࠤࡼࠦࠬഇ") + bstack11l111_opy_ (u"ࠦࢂࠨഈ"))
                  bstack1lll1ll11l_opy_ = bstack11l11lll11_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࡵࠣࡪ࡮ࡲࡥࠡ࡫ࡱࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࠫഉ") + str(e))
      if bstack1l111ll1ll_opy_:
        with bstack11l1111ll1_opy_:
          bstack11ll11l11l_opy_ = bstack1l111ll1ll_opy_.copy()
        for driver in bstack11ll11l11l_opy_:
          if bstack1lll1ll11l_opy_ == driver.session_id:
            bstack11l1ll11ll_opy_ = driver
    bstack1ll1l1l11l_opy_ = bstack11l111l1_opy_.bstack1l11111ll_opy_(test.tags)
    if bstack11l1ll11ll_opy_:
      threading.current_thread().isA11yTest = bstack11l111l1_opy_.bstack111l11lll1_opy_(bstack11l1ll11ll_opy_, bstack1ll1l1l11l_opy_)
      threading.current_thread().isAppA11yTest = bstack11l111l1_opy_.bstack111l11lll1_opy_(bstack11l1ll11ll_opy_, bstack1ll1l1l11l_opy_)
    else:
      threading.current_thread().isA11yTest = bstack1ll1l1l11l_opy_
      threading.current_thread().isAppA11yTest = bstack1ll1l1l11l_opy_
  except:
    pass
  bstack11l1l11l1l_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack111l1ll1l1_opy_
  try:
    bstack111l1ll1l1_opy_ = self._test
  except:
    bstack111l1ll1l1_opy_ = self.test
def bstack11l1ll11l_opy_():
  global bstack1l1ll1lll_opy_
  try:
    if os.path.exists(bstack1l1ll1lll_opy_):
      os.remove(bstack1l1ll1lll_opy_)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩഊ") + str(e))
def bstack1l11llll1_opy_():
  global bstack1l1ll1lll_opy_
  bstack1ll11llll_opy_ = {}
  lock_file = bstack1l1ll1lll_opy_ + bstack11l111_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ࠭ഋ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l111_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫഌ"))
    try:
      if not os.path.isfile(bstack1l1ll1lll_opy_):
        with open(bstack1l1ll1lll_opy_, bstack11l111_opy_ (u"ࠩࡺࠫ഍")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1l1ll1lll_opy_):
        with open(bstack1l1ll1lll_opy_, bstack11l111_opy_ (u"ࠪࡶࠬഎ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll11llll_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ഏ") + str(e))
    return bstack1ll11llll_opy_
  try:
    os.makedirs(os.path.dirname(bstack1l1ll1lll_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack1l1ll1lll_opy_):
        with open(bstack1l1ll1lll_opy_, bstack11l111_opy_ (u"ࠬࡽࠧഐ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1l1ll1lll_opy_):
        with open(bstack1l1ll1lll_opy_, bstack11l111_opy_ (u"࠭ࡲࠨ഑")) as f:
          content = f.read().strip()
          if content:
            bstack1ll11llll_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩഒ") + str(e))
  finally:
    return bstack1ll11llll_opy_
def bstack1l1l1ll11l_opy_(platform_index, item_index):
  global bstack1l1ll1lll_opy_
  lock_file = bstack1l1ll1lll_opy_ + bstack11l111_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧഓ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬഔ"))
    try:
      bstack1ll11llll_opy_ = {}
      if os.path.exists(bstack1l1ll1lll_opy_):
        with open(bstack1l1ll1lll_opy_, bstack11l111_opy_ (u"ࠪࡶࠬക")) as f:
          content = f.read().strip()
          if content:
            bstack1ll11llll_opy_ = json.loads(content)
      bstack1ll11llll_opy_[item_index] = platform_index
      with open(bstack1l1ll1lll_opy_, bstack11l111_opy_ (u"ࠦࡼࠨഖ")) as outfile:
        json.dump(bstack1ll11llll_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡸࡴ࡬ࡸ࡮ࡴࡧࠡࡶࡲࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪഗ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack1l1ll1lll_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack1ll11llll_opy_ = {}
      if os.path.exists(bstack1l1ll1lll_opy_):
        with open(bstack1l1ll1lll_opy_, bstack11l111_opy_ (u"࠭ࡲࠨഘ")) as f:
          content = f.read().strip()
          if content:
            bstack1ll11llll_opy_ = json.loads(content)
      bstack1ll11llll_opy_[item_index] = platform_index
      with open(bstack1l1ll1lll_opy_, bstack11l111_opy_ (u"ࠢࡸࠤങ")) as outfile:
        json.dump(bstack1ll11llll_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡻࡷ࡯ࡴࡪࡰࡪࠤࡹࡵࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ച") + str(e))
def bstack1111l111l1_opy_(bstack111l11ll11_opy_):
  global CONFIG
  bstack11l11l1ll1_opy_ = bstack11l111_opy_ (u"ࠩࠪഛ")
  if not bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ജ") in CONFIG:
    logger.info(bstack11l111_opy_ (u"ࠫࡓࡵࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠣࡴࡦࡹࡳࡦࡦࠣࡹࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡧࡦࡰࡨࡶࡦࡺࡥࠡࡴࡨࡴࡴࡸࡴࠡࡨࡲࡶࠥࡘ࡯ࡣࡱࡷࠤࡷࡻ࡮ࠨഝ"))
  try:
    platform = CONFIG[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨഞ")][bstack111l11ll11_opy_]
    if bstack11l111_opy_ (u"࠭࡯ࡴࠩട") in platform:
      bstack11l11l1ll1_opy_ += str(platform[bstack11l111_opy_ (u"ࠧࡰࡵࠪഠ")]) + bstack11l111_opy_ (u"ࠨ࠮ࠣࠫഡ")
    if bstack11l111_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬഢ") in platform:
      bstack11l11l1ll1_opy_ += str(platform[bstack11l111_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ണ")]) + bstack11l111_opy_ (u"ࠫ࠱ࠦࠧത")
    if bstack11l111_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩഥ") in platform:
      bstack11l11l1ll1_opy_ += str(platform[bstack11l111_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪദ")]) + bstack11l111_opy_ (u"ࠧ࠭ࠢࠪധ")
    if bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪന") in platform:
      bstack11l11l1ll1_opy_ += str(platform[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫഩ")]) + bstack11l111_opy_ (u"ࠪ࠰ࠥ࠭പ")
    if bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩഫ") in platform:
      bstack11l11l1ll1_opy_ += str(platform[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪബ")]) + bstack11l111_opy_ (u"࠭ࠬࠡࠩഭ")
    if bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨമ") in platform:
      bstack11l11l1ll1_opy_ += str(platform[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩയ")]) + bstack11l111_opy_ (u"ࠩ࠯ࠤࠬര")
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠪࡗࡴࡳࡥࠡࡧࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡳ࡭ࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡶࡸࡷ࡯࡮ࡨࠢࡩࡳࡷࠦࡲࡦࡲࡲࡶࡹࠦࡧࡦࡰࡨࡶࡦࡺࡩࡰࡰࠪറ") + str(e))
  finally:
    if bstack11l11l1ll1_opy_[len(bstack11l11l1ll1_opy_) - 2:] == bstack11l111_opy_ (u"ࠫ࠱ࠦࠧല"):
      bstack11l11l1ll1_opy_ = bstack11l11l1ll1_opy_[:-2]
    return bstack11l11l1ll1_opy_
def bstack1l11111l11_opy_(path, bstack11l11l1ll1_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack111llllll_opy_ = ET.parse(path)
    bstack1l11l11l1_opy_ = bstack111llllll_opy_.getroot()
    bstack11l1l11l1_opy_ = None
    for suite in bstack1l11l11l1_opy_.iter(bstack11l111_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫള")):
      if bstack11l111_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ഴ") in suite.attrib:
        suite.attrib[bstack11l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬവ")] += bstack11l111_opy_ (u"ࠨࠢࠪശ") + bstack11l11l1ll1_opy_
        bstack11l1l11l1_opy_ = suite
    bstack1llll11l1l_opy_ = None
    for robot in bstack1l11l11l1_opy_.iter(bstack11l111_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨഷ")):
      bstack1llll11l1l_opy_ = robot
    bstack1l1l1l11l1_opy_ = len(bstack1llll11l1l_opy_.findall(bstack11l111_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩസ")))
    if bstack1l1l1l11l1_opy_ == 1:
      bstack1llll11l1l_opy_.remove(bstack1llll11l1l_opy_.findall(bstack11l111_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪഹ"))[0])
      bstack11lll11l1_opy_ = ET.Element(bstack11l111_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫഺ"), attrib={bstack11l111_opy_ (u"࠭࡮ࡢ࡯ࡨ഻ࠫ"): bstack11l111_opy_ (u"ࠧࡔࡷ࡬ࡸࡪࡹ഼ࠧ"), bstack11l111_opy_ (u"ࠨ࡫ࡧࠫഽ"): bstack11l111_opy_ (u"ࠩࡶ࠴ࠬാ")})
      bstack1llll11l1l_opy_.insert(1, bstack11lll11l1_opy_)
      bstack1l1l111l1l_opy_ = None
      for suite in bstack1llll11l1l_opy_.iter(bstack11l111_opy_ (u"ࠪࡷࡺ࡯ࡴࡦࠩി")):
        bstack1l1l111l1l_opy_ = suite
      bstack1l1l111l1l_opy_.append(bstack11l1l11l1_opy_)
      bstack11111ll1l1_opy_ = None
      for status in bstack11l1l11l1_opy_.iter(bstack11l111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫീ")):
        bstack11111ll1l1_opy_ = status
      bstack1l1l111l1l_opy_.append(bstack11111ll1l1_opy_)
    bstack111llllll_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡵࡷ࡮ࡴࡧࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡱࡩࡷࡧࡴࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠪു") + str(e))
def bstack1llllllll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1l11l11ll1_opy_
  global CONFIG
  if bstack11l111_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࡶࡡࡵࡪࠥൂ") in options:
    del options[bstack11l111_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࡰࡢࡶ࡫ࠦൃ")]
  json_data = bstack1l11llll1_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack11l111_opy_ (u"ࠨࡲࡤࡦࡴࡺ࡟ࡳࡧࡶࡹࡱࡺࡳࠨൄ"), str(item_id), bstack11l111_opy_ (u"ࠩࡲࡹࡹࡶࡵࡵ࠰ࡻࡱࡱ࠭൅"))
    bstack1l11111l11_opy_(path, bstack1111l111l1_opy_(json_data[item_id]))
  bstack11l1ll11l_opy_()
  return bstack1l11l11ll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1111lll11l_opy_(self, ff_profile_dir):
  global bstack1lll111ll1_opy_
  if not ff_profile_dir:
    return None
  return bstack1lll111ll1_opy_(self, ff_profile_dir)
def bstack1l1l1l1l11_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l1111lll_opy_
  bstack111lll111l_opy_ = []
  if bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭െ") in CONFIG:
    bstack111lll111l_opy_ = CONFIG[bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧേ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11l111_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࠨൈ")],
      pabot_args[bstack11l111_opy_ (u"ࠨࡶࡦࡴࡥࡳࡸ࡫ࠢ൉")],
      argfile,
      pabot_args.get(bstack11l111_opy_ (u"ࠢࡩ࡫ࡹࡩࠧൊ")),
      pabot_args[bstack11l111_opy_ (u"ࠣࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠦോ")],
      platform[0],
      bstack1l1111lll_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11l111_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡪ࡮ࡲࡥࡴࠤൌ")] or [(bstack11l111_opy_ (u"്ࠥࠦ"), None)]
    for platform in enumerate(bstack111lll111l_opy_)
  ]
def bstack1l111l111_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack11ll1ll1l1_opy_=bstack11l111_opy_ (u"ࠫࠬൎ")):
  global bstack1111l11111_opy_
  self.platform_index = platform_index
  self.bstack11ll1111l_opy_ = bstack11ll1ll1l1_opy_
  bstack1111l11111_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack111lll1ll_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack11lll1111l_opy_
  global bstack11l11111l1_opy_
  bstack1l11l111ll_opy_ = copy.deepcopy(item)
  if not bstack11l111_opy_ (u"ࠬࡼࡡࡳ࡫ࡤࡦࡱ࡫ࠧ൏") in item.options:
    bstack1l11l111ll_opy_.options[bstack11l111_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨ൐")] = []
  bstack1ll1lll1ll_opy_ = bstack1l11l111ll_opy_.options[bstack11l111_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ൑")].copy()
  for v in bstack1l11l111ll_opy_.options[bstack11l111_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ൒")]:
    if bstack11l111_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡒࡏࡅ࡙ࡌࡏࡓࡏࡌࡒࡉࡋࡘࠨ൓") in v:
      bstack1ll1lll1ll_opy_.remove(v)
    if bstack11l111_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕࠪൔ") in v:
      bstack1ll1lll1ll_opy_.remove(v)
    if bstack11l111_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡈࡊࡌࡌࡐࡅࡄࡐࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨൕ") in v:
      bstack1ll1lll1ll_opy_.remove(v)
  bstack1ll1lll1ll_opy_.insert(0, bstack11l111_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛࠾ࢀࢃࠧൖ").format(bstack1l11l111ll_opy_.platform_index))
  bstack1ll1lll1ll_opy_.insert(0, bstack11l111_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡊࡅࡇࡎࡒࡇࡆࡒࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔ࠽ࡿࢂ࠭ൗ").format(bstack1l11l111ll_opy_.bstack11ll1111l_opy_))
  bstack1l11l111ll_opy_.options[bstack11l111_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩ൘")] = bstack1ll1lll1ll_opy_
  if bstack11l11111l1_opy_:
    bstack1l11l111ll_opy_.options[bstack11l111_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ൙")].insert(0, bstack11l111_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡅࡏࡍࡆࡘࡇࡔ࠼ࡾࢁࠬ൚").format(bstack11l11111l1_opy_))
  return bstack11lll1111l_opy_(caller_id, datasources, is_last, bstack1l11l111ll_opy_, outs_dir)
def bstack11l1llllll_opy_(command, item_index):
  try:
    if bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ൛")):
      os.environ[bstack11l111_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬ൜")] = json.dumps(CONFIG[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ൝")][item_index % bstack1lll111l1_opy_])
    global bstack11l11111l1_opy_
    if bstack11l11111l1_opy_:
      command[0] = command[0].replace(bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ൞"), bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡳࡥ࡭ࠣࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠣࠫൟ") + str(
        item_index) + bstack11l111_opy_ (u"ࠨࠢࠪൠ") + bstack11l11111l1_opy_, 1)
    else:
      command[0] = command[0].replace(bstack11l111_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨൡ"),
                                      bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧൢ") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡱࡴࡪࡩࡧࡻ࡬ࡲ࡬ࠦࡣࡰ࡯ࡰࡥࡳࡪࠠࡧࡱࡵࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴ࠺ࠡࡽࢀࠫൣ").format(str(e)))
def bstack1ll1l11111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1l1llll1l_opy_
  try:
    bstack11l1llllll_opy_(command, item_index)
    return bstack1l1llll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰ࠽ࠤࢀࢃࠧ൤").format(str(e)))
    raise e
def bstack1l1111111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1l1llll1l_opy_
  try:
    bstack11l1llllll_opy_(command, item_index)
    return bstack1l1llll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠷࠴࠱࠴࠼ࠣࡿࢂ࠭൥").format(str(e)))
    try:
      return bstack1l1llll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack11l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡ࠴࠱࠵࠸ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࡾࢁࠬ൦").format(str(e2)))
      raise e
def bstack1l1lll11ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1l1llll1l_opy_
  try:
    bstack11l1llllll_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack1l1llll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࠦ࠲࠯࠳࠸࠾ࠥࢁࡽࠨ൧").format(str(e)))
    try:
      return bstack1l1llll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack11l111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣ࠶࠳࠷࠵ࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧ൨").format(str(e2)))
      raise e
def _1lll1ll111_opy_(bstack1llll1lll1_opy_, item_index, process_timeout, sleep_before_start, bstack11ll1l1l1l_opy_):
  bstack11l1llllll_opy_(bstack1llll1lll1_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack1l11lll1l1_opy_(command, bstack1l11l1lll1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1l1llll1l_opy_
  try:
    bstack11l1llllll_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack1l1llll1l_opy_(command, bstack1l11l1lll1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠷࠱࠴࠿ࠦࡻࡾࠩ൩").format(str(e)))
    try:
      return bstack1l1llll1l_opy_(command, bstack1l11l1lll1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11l111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫ൪").format(str(e2)))
      raise e
def bstack11l1ll1111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1l1llll1l_opy_
  try:
    process_timeout = _1lll1ll111_opy_(command, item_index, process_timeout, sleep_before_start, bstack11l111_opy_ (u"ࠬ࠺࠮࠳ࠩ൫"))
    return bstack1l1llll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠹࠴࠲࠻ࠢࡾࢁࠬ൬").format(str(e)))
    try:
      return bstack1l1llll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧ൭").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack11l1lll111_opy_(self, runner, quiet=False, capture=True):
  global bstack1l1ll1llll_opy_
  bstack1l11llll1l_opy_ = bstack1l1ll1llll_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11l111_opy_ (u"ࠨࡧࡻࡧࡪࡶࡴࡪࡱࡱࡣࡦࡸࡲࠨ൮")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11l111_opy_ (u"ࠩࡨࡼࡨࡥࡴࡳࡣࡦࡩࡧࡧࡣ࡬ࡡࡤࡶࡷ࠭൯")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1l11llll1l_opy_
def bstack1l111l1ll_opy_(runner, hook_name, context, element, bstack1l111lll1l_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack11lll11ll1_opy_.bstack11l1lll1_opy_(hook_name, element)
    bstack1l111lll1l_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack11lll11ll1_opy_.bstack11l1ll11_opy_(element)
      if hook_name not in [bstack11l111_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠧ൰"), bstack11l111_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧ൱")] and args and hasattr(args[0], bstack11l111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡣࡲ࡫ࡳࡴࡣࡪࡩࠬ൲")):
        args[0].error_message = bstack11l111_opy_ (u"࠭ࠧ൳")
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡬ࡦࡴࡤ࡭ࡧࠣ࡬ࡴࡵ࡫ࡴࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩ࠿ࠦࡻࡾࠩ൴").format(str(e)))
@measure(event_name=EVENTS.bstack1l11lllll_opy_, stage=STAGE.bstack1l111l11l_opy_, hook_type=bstack11l111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡂ࡮࡯ࠦ൵"), bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack11ll1ll1ll_opy_(runner, name, context, bstack1l111lll1l_opy_, *args):
    if runner.hooks.get(bstack11l111_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨ൶")).__name__ != bstack11l111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲ࡟ࡥࡧࡩࡥࡺࡲࡴࡠࡪࡲࡳࡰࠨ൷"):
      bstack1l111l1ll_opy_(runner, name, context, runner, bstack1l111lll1l_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack111l1ll1ll_opy_(bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ൸")) else context.browser
      runner.driver_initialised = bstack11l111_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤ൹")
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡤࡳ࡫ࡹࡩࡷࠦࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡧࠣࡥࡹࡺࡲࡪࡤࡸࡸࡪࡀࠠࡼࡿࠪൺ").format(str(e)))
def bstack1ll11l111l_opy_(runner, name, context, bstack1l111lll1l_opy_, *args):
    bstack1l111l1ll_opy_(runner, name, context, context.feature, bstack1l111lll1l_opy_, *args)
    try:
      if not bstack11l1ll1lll_opy_:
        bstack11l1ll11ll_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1ll1ll_opy_(bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ൻ")) else context.browser
        if is_driver_active(bstack11l1ll11ll_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack11l111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤർ")
          bstack11l111llll_opy_ = str(runner.feature.name)
          bstack1l1ll1lll1_opy_(context, bstack11l111llll_opy_)
          bstack11l1ll11ll_opy_.execute_script(bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧൽ") + json.dumps(bstack11l111llll_opy_) + bstack11l111_opy_ (u"ࠪࢁࢂ࠭ൾ"))
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫൿ").format(str(e)))
def bstack1ll1llll1l_opy_(runner, name, context, bstack1l111lll1l_opy_, *args):
    if hasattr(context, bstack11l111_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧ඀")):
        bstack11lll11ll1_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack11l111_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨඁ")) else context.feature
    bstack1l111l1ll_opy_(runner, name, context, target, bstack1l111lll1l_opy_, *args)
@measure(event_name=EVENTS.bstack1l1l1l111l_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack111l111ll1_opy_(runner, name, context, bstack1l111lll1l_opy_, *args):
    if len(context.scenario.tags) == 0: bstack11lll11ll1_opy_.start_test(context)
    bstack1l111l1ll_opy_(runner, name, context, context.scenario, bstack1l111lll1l_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack11111ll111_opy_.bstack1111111l1_opy_(context, *args)
    try:
      bstack11l1ll11ll_opy_ = bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ං"), context.browser)
      if is_driver_active(bstack11l1ll11ll_opy_):
        bstack1lll1l1l_opy_.bstack1lll111l11_opy_(bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧඃ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l111_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦ඄")
        if (not bstack11l1ll1lll_opy_):
          scenario_name = args[0].name
          feature_name = bstack11l111llll_opy_ = str(runner.feature.name)
          bstack11l111llll_opy_ = feature_name + bstack11l111_opy_ (u"ࠪࠤ࠲ࠦࠧඅ") + scenario_name
          if runner.driver_initialised == bstack11l111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨආ"):
            bstack1l1ll1lll1_opy_(context, bstack11l111llll_opy_)
            bstack11l1ll11ll_opy_.execute_script(bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪඇ") + json.dumps(bstack11l111llll_opy_) + bstack11l111_opy_ (u"࠭ࡽࡾࠩඈ"))
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡪࡴࡡࡳ࡫ࡲ࠾ࠥࢁࡽࠨඉ").format(str(e)))
@measure(event_name=EVENTS.bstack1l11lllll_opy_, stage=STAGE.bstack1l111l11l_opy_, hook_type=bstack11l111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡔࡶࡨࡴࠧඊ"), bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack111llll111_opy_(runner, name, context, bstack1l111lll1l_opy_, *args):
    bstack1l111l1ll_opy_(runner, name, context, args[0], bstack1l111lll1l_opy_, *args)
    try:
      bstack11l1ll11ll_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1ll1ll_opy_(bstack11l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨඋ")) else context.browser
      if is_driver_active(bstack11l1ll11ll_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣඌ")
        bstack11lll11ll1_opy_.bstack11ll111l_opy_(args[0])
        if runner.driver_initialised == bstack11l111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤඍ"):
          feature_name = bstack11l111llll_opy_ = str(runner.feature.name)
          bstack11l111llll_opy_ = feature_name + bstack11l111_opy_ (u"ࠬࠦ࠭ࠡࠩඎ") + context.scenario.name
          bstack11l1ll11ll_opy_.execute_script(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫඏ") + json.dumps(bstack11l111llll_opy_) + bstack11l111_opy_ (u"ࠧࡾࡿࠪඐ"))
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡹ࡫ࡰ࠻ࠢࡾࢁࠬඑ").format(str(e)))
@measure(event_name=EVENTS.bstack1l11lllll_opy_, stage=STAGE.bstack1l111l11l_opy_, hook_type=bstack11l111_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡔࡶࡨࡴࠧඒ"), bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack111l1l111l_opy_(runner, name, context, bstack1l111lll1l_opy_, *args):
  bstack11lll11ll1_opy_.bstack11ll1111_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack11l1ll11ll_opy_ = threading.current_thread().bstackSessionDriver if bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩඓ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack11l1ll11ll_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack11l111_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫඔ")
        feature_name = bstack11l111llll_opy_ = str(runner.feature.name)
        bstack11l111llll_opy_ = feature_name + bstack11l111_opy_ (u"ࠬࠦ࠭ࠡࠩඕ") + context.scenario.name
        bstack11l1ll11ll_opy_.execute_script(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫඖ") + json.dumps(bstack11l111llll_opy_) + bstack11l111_opy_ (u"ࠧࡾࡿࠪ඗"))
    if str(step_status).lower() == bstack11l111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ඘"):
      bstack11llll11l1_opy_ = bstack11l111_opy_ (u"ࠩࠪ඙")
      bstack1l1l1l1ll_opy_ = bstack11l111_opy_ (u"ࠪࠫක")
      bstack111lll1ll1_opy_ = bstack11l111_opy_ (u"ࠫࠬඛ")
      try:
        import traceback
        bstack11llll11l1_opy_ = runner.exception.__class__.__name__
        bstack11ll11l1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1l1l1l1ll_opy_ = bstack11l111_opy_ (u"ࠬࠦࠧග").join(bstack11ll11l1_opy_)
        bstack111lll1ll1_opy_ = bstack11ll11l1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1ll1lll11_opy_.format(str(e)))
      bstack11llll11l1_opy_ += bstack111lll1ll1_opy_
      bstack1lllllll11_opy_(context, json.dumps(str(args[0].name) + bstack11l111_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧඝ") + str(bstack1l1l1l1ll_opy_)),
                          bstack11l111_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨඞ"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨඟ"):
        bstack1l11l11ll_opy_(getattr(context, bstack11l111_opy_ (u"ࠩࡳࡥ࡬࡫ࠧච"), None), bstack11l111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥඡ"), bstack11llll11l1_opy_)
        bstack11l1ll11ll_opy_.execute_script(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩජ") + json.dumps(str(args[0].name) + bstack11l111_opy_ (u"ࠧࠦ࠭ࠡࡈࡤ࡭ࡱ࡫ࡤࠢ࡞ࡱࠦඣ") + str(bstack1l1l1l1ll_opy_)) + bstack11l111_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭ඤ"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧඥ"):
        bstack1ll1ll1l11_opy_(bstack11l1ll11ll_opy_, bstack11l111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨඦ"), bstack11l111_opy_ (u"ࠤࡖࡧࡪࡴࡡࡳ࡫ࡲࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨට") + str(bstack11llll11l1_opy_))
    else:
      bstack1lllllll11_opy_(context, bstack11l111_opy_ (u"ࠥࡔࡦࡹࡳࡦࡦࠤࠦඨ"), bstack11l111_opy_ (u"ࠦ࡮ࡴࡦࡰࠤඩ"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥඪ"):
        bstack1l11l11ll_opy_(getattr(context, bstack11l111_opy_ (u"࠭ࡰࡢࡩࡨࠫණ"), None), bstack11l111_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢඬ"))
      bstack11l1ll11ll_opy_.execute_script(bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ත") + json.dumps(str(args[0].name) + bstack11l111_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨථ")) + bstack11l111_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩද"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤධ"):
        bstack1ll1ll1l11_opy_(bstack11l1ll11ll_opy_, bstack11l111_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧන"))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡷࡹ࡫ࡰ࠻ࠢࡾࢁࠬ඲").format(str(e)))
  bstack1l111l1ll_opy_(runner, name, context, args[0], bstack1l111lll1l_opy_, *args)
@measure(event_name=EVENTS.bstack11l1ll1l11_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack1ll1l1l1l_opy_(runner, name, context, bstack1l111lll1l_opy_, *args):
  bstack11lll11ll1_opy_.end_test(args[0])
  try:
    bstack111l111l11_opy_ = args[0].status.name
    bstack11l1ll11ll_opy_ = bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ඳ"), context.browser)
    bstack11111ll111_opy_.bstack11l1111l1_opy_(bstack11l1ll11ll_opy_)
    if str(bstack111l111l11_opy_).lower() == bstack11l111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨප"):
      bstack11llll11l1_opy_ = bstack11l111_opy_ (u"ࠩࠪඵ")
      bstack1l1l1l1ll_opy_ = bstack11l111_opy_ (u"ࠪࠫබ")
      bstack111lll1ll1_opy_ = bstack11l111_opy_ (u"ࠫࠬභ")
      try:
        import traceback
        bstack11llll11l1_opy_ = runner.exception.__class__.__name__
        bstack11ll11l1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1l1l1l1ll_opy_ = bstack11l111_opy_ (u"ࠬࠦࠧම").join(bstack11ll11l1_opy_)
        bstack111lll1ll1_opy_ = bstack11ll11l1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1ll1lll11_opy_.format(str(e)))
      bstack11llll11l1_opy_ += bstack111lll1ll1_opy_
      bstack1lllllll11_opy_(context, json.dumps(str(args[0].name) + bstack11l111_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧඹ") + str(bstack1l1l1l1ll_opy_)),
                          bstack11l111_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨය"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥර") or runner.driver_initialised == bstack11l111_opy_ (u"ࠩ࡬ࡲࡸࡺࡥࡱࠩ඼"):
        bstack1l11l11ll_opy_(getattr(context, bstack11l111_opy_ (u"ࠪࡴࡦ࡭ࡥࠨල"), None), bstack11l111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ඾"), bstack11llll11l1_opy_)
        bstack11l1ll11ll_opy_.execute_script(bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ඿") + json.dumps(str(args[0].name) + bstack11l111_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧව") + str(bstack1l1l1l1ll_opy_)) + bstack11l111_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧශ"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥෂ") or runner.driver_initialised == bstack11l111_opy_ (u"ࠩ࡬ࡲࡸࡺࡥࡱࠩස"):
        bstack1ll1ll1l11_opy_(bstack11l1ll11ll_opy_, bstack11l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪහ"), bstack11l111_opy_ (u"ࠦࡘࡩࡥ࡯ࡣࡵ࡭ࡴࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣළ") + str(bstack11llll11l1_opy_))
    else:
      bstack1lllllll11_opy_(context, bstack11l111_opy_ (u"ࠧࡖࡡࡴࡵࡨࡨࠦࠨෆ"), bstack11l111_opy_ (u"ࠨࡩ࡯ࡨࡲࠦ෇"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤ෈") or runner.driver_initialised == bstack11l111_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨ෉"):
        bstack1l11l11ll_opy_(getattr(context, bstack11l111_opy_ (u"ࠩࡳࡥ࡬࡫්ࠧ"), None), bstack11l111_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ෋"))
      bstack11l1ll11ll_opy_.execute_script(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ෌") + json.dumps(str(args[0].name) + bstack11l111_opy_ (u"ࠧࠦ࠭ࠡࡒࡤࡷࡸ࡫ࡤࠢࠤ෍")) + bstack11l111_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬ෎"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤා") or runner.driver_initialised == bstack11l111_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨැ"):
        bstack1ll1ll1l11_opy_(bstack11l1ll11ll_opy_, bstack11l111_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤෑ"))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡧࡧࡤࡸࡺࡸࡥ࠻ࠢࡾࢁࠬි").format(str(e)))
  bstack1l111l1ll_opy_(runner, name, context, context.scenario, bstack1l111lll1l_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1l111ll1l_opy_(runner, name, context, bstack1l111lll1l_opy_, *args):
    target = context.scenario if hasattr(context, bstack11l111_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ී")) else context.feature
    bstack1l111l1ll_opy_(runner, name, context, target, bstack1l111lll1l_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack111l1l1l1l_opy_(runner, name, context, bstack1l111lll1l_opy_, *args):
    try:
      bstack11l1ll11ll_opy_ = bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫු"), context.browser)
      bstack11lll11111_opy_ = bstack11l111_opy_ (u"࠭ࠧ෕")
      if context.failed is True:
        bstack111l11ll1_opy_ = []
        bstack11ll11ll1_opy_ = []
        bstack1ll1111l1_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack111l11ll1_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11ll11l1_opy_ = traceback.format_tb(exc_tb)
            bstack1lllll1l11_opy_ = bstack11l111_opy_ (u"ࠧࠡࠩූ").join(bstack11ll11l1_opy_)
            bstack11ll11ll1_opy_.append(bstack1lllll1l11_opy_)
            bstack1ll1111l1_opy_.append(bstack11ll11l1_opy_[-1])
        except Exception as e:
          logger.debug(bstack1ll1lll11_opy_.format(str(e)))
        bstack11llll11l1_opy_ = bstack11l111_opy_ (u"ࠨࠩ෗")
        for i in range(len(bstack111l11ll1_opy_)):
          bstack11llll11l1_opy_ += bstack111l11ll1_opy_[i] + bstack1ll1111l1_opy_[i] + bstack11l111_opy_ (u"ࠩ࡟ࡲࠬෘ")
        bstack11lll11111_opy_ = bstack11l111_opy_ (u"ࠪࠤࠬෙ").join(bstack11ll11ll1_opy_)
        if runner.driver_initialised in [bstack11l111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧේ"), bstack11l111_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤෛ")]:
          bstack1lllllll11_opy_(context, bstack11lll11111_opy_, bstack11l111_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧො"))
          bstack1l11l11ll_opy_(getattr(context, bstack11l111_opy_ (u"ࠧࡱࡣࡪࡩࠬෝ"), None), bstack11l111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣෞ"), bstack11llll11l1_opy_)
          bstack11l1ll11ll_opy_.execute_script(bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧෟ") + json.dumps(bstack11lll11111_opy_) + bstack11l111_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪ෠"))
          bstack1ll1ll1l11_opy_(bstack11l1ll11ll_opy_, bstack11l111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ෡"), bstack11l111_opy_ (u"࡙ࠧ࡯࡮ࡧࠣࡷࡨ࡫࡮ࡢࡴ࡬ࡳࡸࠦࡦࡢ࡫࡯ࡩࡩࡀࠠ࡝ࡰࠥ෢") + str(bstack11llll11l1_opy_))
          bstack11lll1llll_opy_ = bstack111lll1l1l_opy_(bstack11lll11111_opy_, runner.feature.name, logger)
          if (bstack11lll1llll_opy_ != None):
            bstack11lll1ll1l_opy_.append(bstack11lll1llll_opy_)
      else:
        if runner.driver_initialised in [bstack11l111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢ෣"), bstack11l111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦ෤")]:
          bstack1lllllll11_opy_(context, bstack11l111_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦ࠼ࠣࠦ෥") + str(runner.feature.name) + bstack11l111_opy_ (u"ࠤࠣࡴࡦࡹࡳࡦࡦࠤࠦ෦"), bstack11l111_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣ෧"))
          bstack1l11l11ll_opy_(getattr(context, bstack11l111_opy_ (u"ࠫࡵࡧࡧࡦࠩ෨"), None), bstack11l111_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ෩"))
          bstack11l1ll11ll_opy_.execute_script(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ෪") + json.dumps(bstack11l111_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥ࠻ࠢࠥ෫") + str(runner.feature.name) + bstack11l111_opy_ (u"ࠣࠢࡳࡥࡸࡹࡥࡥࠣࠥ෬")) + bstack11l111_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧࢃࡽࠨ෭"))
          bstack1ll1ll1l11_opy_(bstack11l1ll11ll_opy_, bstack11l111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ෮"))
          bstack11lll1llll_opy_ = bstack111lll1l1l_opy_(bstack11lll11111_opy_, runner.feature.name, logger)
          if (bstack11lll1llll_opy_ != None):
            bstack11lll1ll1l_opy_.append(bstack11lll1llll_opy_)
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭෯").format(str(e)))
    bstack1l111l1ll_opy_(runner, name, context, context.feature, bstack1l111lll1l_opy_, *args)
@measure(event_name=EVENTS.bstack1l11lllll_opy_, stage=STAGE.bstack1l111l11l_opy_, hook_type=bstack11l111_opy_ (u"ࠧࡧࡦࡵࡧࡵࡅࡱࡲࠢ෰"), bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack1l11111111_opy_(runner, name, context, bstack1l111lll1l_opy_, *args):
    bstack1l111l1ll_opy_(runner, name, context, runner, bstack1l111lll1l_opy_, *args)
def bstack111ll111l1_opy_(self, name, context, *args):
  try:
    if bstack1l1111l11_opy_:
      platform_index = int(threading.current_thread()._name) % bstack1lll111l1_opy_
      bstack1l1111111l_opy_ = CONFIG[bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ෱")][platform_index]
      os.environ[bstack11l111_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨෲ")] = json.dumps(bstack1l1111111l_opy_)
    global bstack1l111lll1l_opy_
    if not hasattr(self, bstack11l111_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡩࡩ࠭ෳ")):
      self.driver_initialised = None
    bstack1l1l1111ll_opy_ = {
        bstack11l111_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱ࠭෴"): bstack11ll1ll1ll_opy_,
        bstack11l111_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠫ෵"): bstack1ll11l111l_opy_,
        bstack11l111_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡹࡧࡧࠨ෶"): bstack1ll1llll1l_opy_,
        bstack11l111_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧ෷"): bstack111l111ll1_opy_,
        bstack11l111_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠫ෸"): bstack111llll111_opy_,
        bstack11l111_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡵࡧࡳࠫ෹"): bstack111l1l111l_opy_,
        bstack11l111_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩ෺"): bstack1ll1l1l1l_opy_,
        bstack11l111_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡶࡤ࡫ࠬ෻"): bstack1l111ll1l_opy_,
        bstack11l111_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪ෼"): bstack111l1l1l1l_opy_,
        bstack11l111_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧ෽"): bstack1l11111111_opy_
    }
    handler = bstack1l1l1111ll_opy_.get(name, bstack1l111lll1l_opy_)
    try:
      handler(self, name, context, bstack1l111lll1l_opy_, *args)
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡩࡱࡲ࡯ࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࠦࡻࡾ࠼ࠣࡿࢂ࠭෾").format(name, str(e)))
    if name in [bstack11l111_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭෿"), bstack11l111_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ฀"), bstack11l111_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫก")]:
      try:
        bstack11l1ll11ll_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1ll1ll_opy_(bstack11l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨข")) else context.browser
        bstack11111l11l_opy_ = (
          (name == bstack11l111_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡤࡰࡱ࠭ฃ") and self.driver_initialised == bstack11l111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣค")) or
          (name == bstack11l111_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠬฅ") and self.driver_initialised == bstack11l111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢฆ")) or
          (name == bstack11l111_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨง") and self.driver_initialised in [bstack11l111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥจ"), bstack11l111_opy_ (u"ࠤ࡬ࡲࡸࡺࡥࡱࠤฉ")]) or
          (name == bstack11l111_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡸࡪࡶࠧช") and self.driver_initialised == bstack11l111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤซ"))
        )
        if bstack11111l11l_opy_:
          self.driver_initialised = None
          if bstack11l1ll11ll_opy_ and hasattr(bstack11l1ll11ll_opy_, bstack11l111_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩฌ")):
            try:
              bstack11l1ll11ll_opy_.quit()
            except Exception as e:
              logger.debug(bstack11l111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡷࡵࡪࡶࡷ࡭ࡳ࡭ࠠࡥࡴ࡬ࡺࡪࡸࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧࠣ࡬ࡴࡵ࡫࠻ࠢࡾࢁࠬญ").format(str(e)))
      except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡪࡲࡳࡰࠦࡣ࡭ࡧࡤࡲࡺࡶࠠࡧࡱࡵࠤࢀࢃ࠺ࠡࡽࢀࠫฎ").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠨࡅࡵ࡭ࡹ࡯ࡣࡢ࡮ࠣࡩࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩࠥࡸࡵ࡯ࠢ࡫ࡳࡴࡱࠠࡼࡿ࠽ࠤࢀࢃࠧฏ").format(name, str(e)))
    try:
      bstack1l111lll1l_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack11l111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࠦ࡯ࡳ࡫ࡪ࡭ࡳࡧ࡬ࠡࡤࡨ࡬ࡦࡼࡥࠡࡪࡲࡳࡰࠦࡻࡾ࠼ࠣࡿࢂ࠭ฐ").format(name, str(e2)))
def bstack1ll111lll1_opy_(config, startdir):
  return bstack11l111_opy_ (u"ࠥࡨࡷ࡯ࡶࡦࡴ࠽ࠤࢀ࠶ࡽࠣฑ").format(bstack11l111_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥฒ"))
notset = Notset()
def bstack11111l11l1_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack111llll1l_opy_
  if str(name).lower() == bstack11l111_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࠬณ"):
    return bstack11l111_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧด")
  else:
    return bstack111llll1l_opy_(self, name, default, skip)
def bstack1lll1lllll_opy_(item, when):
  global bstack11ll11llll_opy_
  try:
    bstack11ll11llll_opy_(item, when)
  except Exception as e:
    pass
def bstack1ll11lll1l_opy_():
  return
def bstack1ll11l11ll_opy_(type, name, status, reason, bstack1ll1l1l11_opy_, bstack1l11l1l1l1_opy_):
  bstack11l1ll111l_opy_ = {
    bstack11l111_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧต"): type,
    bstack11l111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫถ"): {}
  }
  if type == bstack11l111_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫท"):
    bstack11l1ll111l_opy_[bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ธ")][bstack11l111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪน")] = bstack1ll1l1l11_opy_
    bstack11l1ll111l_opy_[bstack11l111_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨบ")][bstack11l111_opy_ (u"࠭ࡤࡢࡶࡤࠫป")] = json.dumps(str(bstack1l11l1l1l1_opy_))
  if type == bstack11l111_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨผ"):
    bstack11l1ll111l_opy_[bstack11l111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫฝ")][bstack11l111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧพ")] = name
  if type == bstack11l111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ฟ"):
    bstack11l1ll111l_opy_[bstack11l111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧภ")][bstack11l111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬม")] = status
    if status == bstack11l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ย"):
      bstack11l1ll111l_opy_[bstack11l111_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪร")][bstack11l111_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨฤ")] = json.dumps(str(reason))
  bstack1111l11ll1_opy_ = bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧล").format(json.dumps(bstack11l1ll111l_opy_))
  return bstack1111l11ll1_opy_
def bstack1111l11l1_opy_(driver_command, response):
    if driver_command == bstack11l111_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧฦ"):
        bstack1lll1l1l_opy_.bstack11ll1ll11_opy_({
            bstack11l111_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࠪว"): response[bstack11l111_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫศ")],
            bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ษ"): bstack1lll1l1l_opy_.current_test_uuid()
        })
def bstack1lll1111ll_opy_(item, call, rep):
  global bstack1ll111l11l_opy_
  global bstack1l111ll1ll_opy_
  global bstack11l1ll1lll_opy_
  name = bstack11l111_opy_ (u"ࠧࠨส")
  try:
    if rep.when == bstack11l111_opy_ (u"ࠨࡥࡤࡰࡱ࠭ห"):
      bstack1lll1ll11l_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack11l1ll1lll_opy_:
          name = str(rep.nodeid)
          bstack1111l1l11_opy_ = bstack1ll11l11ll_opy_(bstack11l111_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪฬ"), name, bstack11l111_opy_ (u"ࠪࠫอ"), bstack11l111_opy_ (u"ࠫࠬฮ"), bstack11l111_opy_ (u"ࠬ࠭ฯ"), bstack11l111_opy_ (u"࠭ࠧะ"))
          threading.current_thread().bstack1ll1l11l1_opy_ = name
          for driver in bstack1l111ll1ll_opy_:
            if bstack1lll1ll11l_opy_ == driver.session_id:
              driver.execute_script(bstack1111l1l11_opy_)
      except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧั").format(str(e)))
      try:
        bstack1ll11l111_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11l111_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩา"):
          status = bstack11l111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩำ") if rep.outcome.lower() == bstack11l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪิ") else bstack11l111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫี")
          reason = bstack11l111_opy_ (u"ࠬ࠭ึ")
          if status == bstack11l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ื"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11l111_opy_ (u"ࠧࡪࡰࡩࡳุࠬ") if status == bstack11l111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨู") else bstack11l111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨฺ")
          data = name + bstack11l111_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬ฻") if status == bstack11l111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ฼") else name + bstack11l111_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩࠧࠠࠨ฽") + reason
          bstack11lll1l11_opy_ = bstack1ll11l11ll_opy_(bstack11l111_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ฾"), bstack11l111_opy_ (u"ࠧࠨ฿"), bstack11l111_opy_ (u"ࠨࠩเ"), bstack11l111_opy_ (u"ࠩࠪแ"), level, data)
          for driver in bstack1l111ll1ll_opy_:
            if bstack1lll1ll11l_opy_ == driver.session_id:
              driver.execute_script(bstack11lll1l11_opy_)
      except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡤࡱࡱࡸࡪࡾࡴࠡࡨࡲࡶࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡶࡩࡸࡹࡩࡰࡰ࠽ࠤࢀࢃࠧโ").format(str(e)))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡶࡤࡸࡪࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࢁࡽࠨใ").format(str(e)))
  bstack1ll111l11l_opy_(item, call, rep)
def bstack11ll111ll_opy_(driver, bstack111ll1l1l1_opy_, test=None):
  global bstack11l1llll1_opy_
  if test != None:
    bstack11ll1l111_opy_ = getattr(test, bstack11l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪไ"), None)
    bstack1ll11l1ll1_opy_ = getattr(test, bstack11l111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫๅ"), None)
    PercySDK.screenshot(driver, bstack111ll1l1l1_opy_, bstack11ll1l111_opy_=bstack11ll1l111_opy_, bstack1ll11l1ll1_opy_=bstack1ll11l1ll1_opy_, bstack11111lllll_opy_=bstack11l1llll1_opy_)
  else:
    PercySDK.screenshot(driver, bstack111ll1l1l1_opy_)
@measure(event_name=EVENTS.bstack111ll1111l_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack11ll11111l_opy_(driver):
  if bstack11l1l1ll11_opy_.bstack1ll1ll1ll_opy_() is True or bstack11l1l1ll11_opy_.capturing() is True:
    return
  bstack11l1l1ll11_opy_.bstack111l11l1ll_opy_()
  while not bstack11l1l1ll11_opy_.bstack1ll1ll1ll_opy_():
    bstack1l1l1l1ll1_opy_ = bstack11l1l1ll11_opy_.bstack1111lllll_opy_()
    bstack11ll111ll_opy_(driver, bstack1l1l1l1ll1_opy_)
  bstack11l1l1ll11_opy_.bstack1l1111l1l_opy_()
def bstack1111l11l1l_opy_(sequence, driver_command, response = None, bstack1lll1lll1l_opy_ = None, args = None):
    try:
      if sequence != bstack11l111_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫ࠧๆ"):
        return
      if percy.bstack1111l11lll_opy_() == bstack11l111_opy_ (u"ࠣࡨࡤࡰࡸ࡫ࠢ็"):
        return
      bstack1l1l1l1ll1_opy_ = bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩ่ࠬ"), None)
      for command in bstack1l1l1l11ll_opy_:
        if command == driver_command:
          with bstack11l1111ll1_opy_:
            bstack11ll11l11l_opy_ = bstack1l111ll1ll_opy_.copy()
          for driver in bstack11ll11l11l_opy_:
            bstack11ll11111l_opy_(driver)
      bstack11lll11ll_opy_ = percy.bstack11l11l1ll_opy_()
      if driver_command in bstack1ll1111ll1_opy_[bstack11lll11ll_opy_]:
        bstack11l1l1ll11_opy_.bstack1ll11ll1l1_opy_(bstack1l1l1l1ll1_opy_, driver_command)
    except Exception as e:
      pass
def bstack1111l1llll_opy_(framework_name):
  if bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡱࡴࡪ࡟ࡤࡣ࡯ࡰࡪࡪ้ࠧ")):
      return
  bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡲࡵࡤࡠࡥࡤࡰࡱ࡫ࡤࠨ๊"), True)
  global bstack1ll1ll1l1l_opy_
  global bstack1ll11l11l1_opy_
  global bstack1lllll111l_opy_
  bstack1ll1ll1l1l_opy_ = framework_name
  logger.info(bstack1l11l11l11_opy_.format(bstack1ll1ll1l1l_opy_.split(bstack11l111_opy_ (u"ࠬ࠳๋ࠧ"))[0]))
  bstack1l1lll1ll_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1l1111l11_opy_:
      Service.start = bstack1ll1l11lll_opy_
      Service.stop = bstack11l1lllll1_opy_
      webdriver.Remote.get = bstack1111ll11ll_opy_
      WebDriver.quit = bstack11lllll11l_opy_
      webdriver.Remote.__init__ = bstack11111ll11_opy_
    if not bstack1l1111l11_opy_:
        webdriver.Remote.__init__ = bstack1l11l11111_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack1111ll1lll_opy_
    bstack1ll11l11l1_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1l1111l11_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack11l1lllll_opy_
  except Exception as e:
    pass
  bstack1111l1l1l_opy_()
  if not bstack1ll11l11l1_opy_:
    bstack1ll1lll1l_opy_(bstack11l111_opy_ (u"ࠨࡐࡢࡥ࡮ࡥ࡬࡫ࡳࠡࡰࡲࡸࠥ࡯࡮ࡴࡶࡤࡰࡱ࡫ࡤࠣ์"), bstack1l11l1l1ll_opy_)
  if bstack1111l111ll_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack11l111_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨํ")) and callable(getattr(RemoteConnection, bstack11l111_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ๎"))):
        RemoteConnection._get_proxy_url = bstack1ll1l111ll_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack1ll1l111ll_opy_
    except Exception as e:
      logger.error(bstack111111ll1_opy_.format(str(e)))
  if bstack1l11llll11_opy_():
    bstack11llllll11_opy_(CONFIG, logger)
  if (bstack11l111_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ๏") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1111l11lll_opy_() == bstack11l111_opy_ (u"ࠥࡸࡷࡻࡥࠣ๐"):
          bstack111l1lll1l_opy_(bstack1111l11l1l_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1111lll11l_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l1111l111_opy_
      except Exception as e:
        logger.warn(bstack1l11ll1lll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1111ll1111_opy_
      except Exception as e:
        logger.debug(bstack111l11l1l1_opy_ + str(e))
    except Exception as e:
      bstack1ll1lll1l_opy_(e, bstack1l11ll1lll_opy_)
    Output.start_test = bstack11llll11ll_opy_
    Output.end_test = bstack1l111l1111_opy_
    TestStatus.__init__ = bstack1l1llllll1_opy_
    QueueItem.__init__ = bstack1l111l111_opy_
    pabot._create_items = bstack1l1l1l1l11_opy_
    try:
      from pabot import __version__ as bstack111lllll1_opy_
      if version.parse(bstack111lllll1_opy_) >= version.parse(bstack11l111_opy_ (u"ࠫ࠺࠴࠰࠯࠲ࠪ๑")):
        pabot._run = bstack1l11lll1l1_opy_
      elif version.parse(bstack111lllll1_opy_) >= version.parse(bstack11l111_opy_ (u"ࠬ࠺࠮࠳࠰࠳ࠫ๒")):
        pabot._run = bstack11l1ll1111_opy_
      elif version.parse(bstack111lllll1_opy_) >= version.parse(bstack11l111_opy_ (u"࠭࠲࠯࠳࠸࠲࠵࠭๓")):
        pabot._run = bstack1l1lll11ll_opy_
      elif version.parse(bstack111lllll1_opy_) >= version.parse(bstack11l111_opy_ (u"ࠧ࠳࠰࠴࠷࠳࠶ࠧ๔")):
        pabot._run = bstack1l1111111_opy_
      else:
        pabot._run = bstack1ll1l11111_opy_
    except Exception as e:
      pabot._run = bstack1ll1l11111_opy_
    pabot._create_command_for_execution = bstack111lll1ll_opy_
    pabot._report_results = bstack1llllllll1_opy_
  if bstack11l111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ๕") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll1lll1l_opy_(e, bstack11ll1llll_opy_)
    Runner.run_hook = bstack111ll111l1_opy_
    Step.run = bstack11l1lll111_opy_
  if bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ๖") in str(framework_name).lower():
    if not bstack1l1111l11_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1ll111lll1_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1ll11lll1l_opy_
      Config.getoption = bstack11111l11l1_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1lll1111ll_opy_
    except Exception as e:
      pass
def bstack1ll111l1l_opy_():
  global CONFIG
  if bstack11l111_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ๗") in CONFIG and int(CONFIG[bstack11l111_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ๘")]) > 1:
    logger.warn(bstack1l11llllll_opy_)
def bstack1l1111ll11_opy_(arg, bstack111l1111_opy_, bstack11lllll1l1_opy_=None):
  global CONFIG
  global bstack11111llll1_opy_
  global bstack1lll1l1l11_opy_
  global bstack1l1111l11_opy_
  global bstack111ll111_opy_
  bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ๙")
  if bstack111l1111_opy_ and isinstance(bstack111l1111_opy_, str):
    bstack111l1111_opy_ = eval(bstack111l1111_opy_)
  CONFIG = bstack111l1111_opy_[bstack11l111_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭๚")]
  bstack11111llll1_opy_ = bstack111l1111_opy_[bstack11l111_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ๛")]
  bstack1lll1l1l11_opy_ = bstack111l1111_opy_[bstack11l111_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ๜")]
  bstack1l1111l11_opy_ = bstack111l1111_opy_[bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬ๝")]
  bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ๞"), bstack1l1111l11_opy_)
  os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭๟")] = bstack11l1ll1ll1_opy_
  os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࠫ๠")] = json.dumps(CONFIG)
  os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡎࡕࡃࡡࡘࡖࡑ࠭๡")] = bstack11111llll1_opy_
  os.environ[bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ๢")] = str(bstack1lll1l1l11_opy_)
  os.environ[bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡎࡘࡋࡎࡔࠧ๣")] = str(True)
  if bstack11l111lll_opy_(arg, [bstack11l111_opy_ (u"ࠩ࠰ࡲࠬ๤"), bstack11l111_opy_ (u"ࠪ࠱࠲ࡴࡵ࡮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ๥")]) != -1:
    os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡆࡘࡁࡍࡎࡈࡐࠬ๦")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack111l1l1lll_opy_)
    return
  bstack111l1l11l1_opy_()
  global bstack11l1l1l1l1_opy_
  global bstack11l1llll1_opy_
  global bstack1l1111lll_opy_
  global bstack11l11111l1_opy_
  global bstack1l1l1l111_opy_
  global bstack1lllll111l_opy_
  global bstack1ll11ll111_opy_
  arg.append(bstack11l111_opy_ (u"ࠧ࠳ࡗࠣ๧"))
  arg.append(bstack11l111_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡀࡍࡰࡦࡸࡰࡪࠦࡡ࡭ࡴࡨࡥࡩࡿࠠࡪ࡯ࡳࡳࡷࡺࡥࡥ࠼ࡳࡽࡹ࡫ࡳࡵ࠰ࡓࡽࡹ࡫ࡳࡵ࡙ࡤࡶࡳ࡯࡮ࡨࠤ๨"))
  arg.append(bstack11l111_opy_ (u"ࠢ࠮࡙ࠥ๩"))
  arg.append(bstack11l111_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥ࠻ࡖ࡫ࡩࠥ࡮࡯ࡰ࡭࡬ࡱࡵࡲࠢ๪"))
  global bstack1ll1lllll1_opy_
  global bstack11l11lll1_opy_
  global bstack11llllllll_opy_
  global bstack11l1l11l1l_opy_
  global bstack1lll111ll1_opy_
  global bstack1111l11111_opy_
  global bstack11lll1111l_opy_
  global bstack111l1l111_opy_
  global bstack11l11l11ll_opy_
  global bstack1ll111llll_opy_
  global bstack111llll1l_opy_
  global bstack11ll11llll_opy_
  global bstack1ll111l11l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll1lllll1_opy_ = webdriver.Remote.__init__
    bstack11l11lll1_opy_ = WebDriver.quit
    bstack111l1l111_opy_ = WebDriver.close
    bstack11l11l11ll_opy_ = WebDriver.get
    bstack11llllllll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack11lll111l_opy_(CONFIG) and bstack1llll11l11_opy_():
    if bstack1l11l1l11l_opy_() < version.parse(bstack111111lll_opy_):
      logger.error(bstack11111l1l1l_opy_.format(bstack1l11l1l11l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11l111_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ๫")) and callable(getattr(RemoteConnection, bstack11l111_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ๬"))):
          bstack1ll111llll_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1ll111llll_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack111111ll1_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack111llll1l_opy_ = Config.getoption
    from _pytest import runner
    bstack11ll11llll_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack11l11ll1_opy_)
  try:
    from pytest_bdd import reporting
    bstack1ll111l11l_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬ๭"))
  bstack1l1111lll_opy_ = CONFIG.get(bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ๮"), {}).get(bstack11l111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ๯"))
  bstack1ll11ll111_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack1111ll1ll_opy_():
      bstack1l1l111ll_opy_.invoke(Events.CONNECT, bstack11l11ll11l_opy_())
    platform_index = int(os.environ.get(bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧ๰"), bstack11l111_opy_ (u"ࠨ࠲ࠪ๱")))
  else:
    bstack1111l1llll_opy_(bstack1ll1111ll_opy_)
  os.environ[bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡗࡖࡉࡗࡔࡁࡎࡇࠪ๲")] = CONFIG[bstack11l111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬ๳")]
  os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅࡈࡉࡅࡔࡕࡢࡏࡊ࡟ࠧ๴")] = CONFIG[bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ๵")]
  os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩ๶")] = bstack1l1111l11_opy_.__str__()
  from _pytest.config import main as bstack1lll1l111l_opy_
  bstack11l111l1l_opy_ = []
  try:
    exit_code = bstack1lll1l111l_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1111l1ll1l_opy_()
    if bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫ๷") in multiprocessing.current_process().__dict__.keys():
      for bstack11l1lll11l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11l111l1l_opy_.append(bstack11l1lll11l_opy_)
    try:
      bstack1l11l1l11_opy_ = (bstack11l111l1l_opy_, int(exit_code))
      bstack11lllll1l1_opy_.append(bstack1l11l1l11_opy_)
    except:
      bstack11lllll1l1_opy_.append((bstack11l111l1l_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack11l111l1l_opy_.append({bstack11l111_opy_ (u"ࠨࡰࡤࡱࡪ࠭๸"): bstack11l111_opy_ (u"ࠩࡓࡶࡴࡩࡥࡴࡵࠣࠫ๹") + os.environ.get(bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪ๺")), bstack11l111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ๻"): traceback.format_exc(), bstack11l111_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ๼"): int(os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭๽")))})
    bstack11lllll1l1_opy_.append((bstack11l111l1l_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack11l111_opy_ (u"ࠢࡳࡧࡷࡶ࡮࡫ࡳࠣ๾"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack11ll1llll1_opy_ = e.__class__.__name__
    print(bstack11l111_opy_ (u"ࠣࠧࡶ࠾ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠥࡨࡥࡩࡣࡹࡩࠥࡺࡥࡴࡶࠣࠩࡸࠨ๿") % (bstack11ll1llll1_opy_, e))
    return 1
def bstack1l1llll1l1_opy_(arg):
  global bstack111l1ll111_opy_
  bstack1111l1llll_opy_(bstack11l1111lll_opy_)
  os.environ[bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ຀")] = str(bstack1lll1l1l11_opy_)
  retries = bstack1llllllll_opy_.bstack111lll1l_opy_(CONFIG)
  status_code = 0
  if bstack1llllllll_opy_.bstack111l111l_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack11ll1111l1_opy_
    status_code = bstack11ll1111l1_opy_(arg)
  if status_code != 0:
    bstack111l1ll111_opy_ = status_code
def bstack111l1lllll_opy_():
  logger.info(bstack11ll1ll11l_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11l111_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩກ"), help=bstack11l111_opy_ (u"ࠫࡌ࡫࡮ࡦࡴࡤࡸࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡩ࡯࡯ࡨ࡬࡫ࠬຂ"))
  parser.add_argument(bstack11l111_opy_ (u"ࠬ࠳ࡵࠨ຃"), bstack11l111_opy_ (u"࠭࠭࠮ࡷࡶࡩࡷࡴࡡ࡮ࡧࠪຄ"), help=bstack11l111_opy_ (u"࡚ࠧࡱࡸࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡺࡹࡥࡳࡰࡤࡱࡪ࠭຅"))
  parser.add_argument(bstack11l111_opy_ (u"ࠨ࠯࡮ࠫຆ"), bstack11l111_opy_ (u"ࠩ࠰࠱ࡰ࡫ࡹࠨງ"), help=bstack11l111_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡢࡥࡦࡩࡸࡹࠠ࡬ࡧࡼࠫຈ"))
  parser.add_argument(bstack11l111_opy_ (u"ࠫ࠲࡬ࠧຉ"), bstack11l111_opy_ (u"ࠬ࠳࠭ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪຊ"), help=bstack11l111_opy_ (u"࡙࠭ࡰࡷࡵࠤࡹ࡫ࡳࡵࠢࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ຋"))
  bstack11ll11l11_opy_ = parser.parse_args()
  try:
    bstack11l1llll11_opy_ = bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡧࡦࡰࡨࡶ࡮ࡩ࠮ࡺ࡯࡯࠲ࡸࡧ࡭ࡱ࡮ࡨࠫຌ")
    if bstack11ll11l11_opy_.framework and bstack11ll11l11_opy_.framework not in (bstack11l111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨຍ"), bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪຎ")):
      bstack11l1llll11_opy_ = bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡩࡶࡦࡳࡥࡸࡱࡵ࡯࠳ࡿ࡭࡭࠰ࡶࡥࡲࡶ࡬ࡦࠩຏ")
    bstack111llll1l1_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1llll11_opy_)
    bstack1l1l11ll11_opy_ = open(bstack111llll1l1_opy_, bstack11l111_opy_ (u"ࠫࡷ࠭ຐ"))
    bstack1ll11l11l_opy_ = bstack1l1l11ll11_opy_.read()
    bstack1l1l11ll11_opy_.close()
    if bstack11ll11l11_opy_.username:
      bstack1ll11l11l_opy_ = bstack1ll11l11l_opy_.replace(bstack11l111_opy_ (u"ࠬ࡟ࡏࡖࡔࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬຑ"), bstack11ll11l11_opy_.username)
    if bstack11ll11l11_opy_.key:
      bstack1ll11l11l_opy_ = bstack1ll11l11l_opy_.replace(bstack11l111_opy_ (u"࡙࠭ࡐࡗࡕࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨຒ"), bstack11ll11l11_opy_.key)
    if bstack11ll11l11_opy_.framework:
      bstack1ll11l11l_opy_ = bstack1ll11l11l_opy_.replace(bstack11l111_opy_ (u"࡚ࠧࡑࡘࡖࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨຓ"), bstack11ll11l11_opy_.framework)
    file_name = bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫດ")
    file_path = os.path.abspath(file_name)
    bstack111lll1lll_opy_ = open(file_path, bstack11l111_opy_ (u"ࠩࡺࠫຕ"))
    bstack111lll1lll_opy_.write(bstack1ll11l11l_opy_)
    bstack111lll1lll_opy_.close()
    logger.info(bstack11l1ll111_opy_)
    try:
      os.environ[bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬຖ")] = bstack11ll11l11_opy_.framework if bstack11ll11l11_opy_.framework != None else bstack11l111_opy_ (u"ࠦࠧທ")
      config = yaml.safe_load(bstack1ll11l11l_opy_)
      config[bstack11l111_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬຘ")] = bstack11l111_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠳ࡳࡦࡶࡸࡴࠬນ")
      bstack1111ll11l1_opy_(bstack1l1lllllll_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll111ll1_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1ll11ll1l_opy_.format(str(e)))
def bstack1111ll11l1_opy_(bstack1ll1ll1lll_opy_, config, bstack1l1l11ll1_opy_={}):
  global bstack1l1111l11_opy_
  global bstack1l1l11l1ll_opy_
  global bstack111ll111_opy_
  if not config:
    return
  bstack1l11ll1l11_opy_ = bstack11ll11111_opy_ if not bstack1l1111l11_opy_ else (
    bstack1l1l1ll1l_opy_ if bstack11l111_opy_ (u"ࠧࡢࡲࡳࠫບ") in config else (
        bstack1l1111ll1l_opy_ if config.get(bstack11l111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬປ")) else bstack111ll1ll1_opy_
    )
)
  bstack111ll1ll11_opy_ = False
  bstack1ll111lll_opy_ = False
  if bstack1l1111l11_opy_ is True:
      if bstack11l111_opy_ (u"ࠩࡤࡴࡵ࠭ຜ") in config:
          bstack111ll1ll11_opy_ = True
      else:
          bstack1ll111lll_opy_ = True
  bstack11l1ll1l1_opy_ = bstack111ll1l11_opy_.bstack1ll11lll1_opy_(config, bstack1l1l11l1ll_opy_)
  bstack11lll11lll_opy_ = bstack1lllll11l1_opy_()
  data = {
    bstack11l111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬຝ"): config[bstack11l111_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ພ")],
    bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨຟ"): config[bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩຠ")],
    bstack11l111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫມ"): bstack1ll1ll1lll_opy_,
    bstack11l111_opy_ (u"ࠨࡦࡨࡸࡪࡩࡴࡦࡦࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬຢ"): os.environ.get(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫຣ"), bstack1l1l11l1ll_opy_),
    bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬ຤"): bstack1111ll111_opy_,
    bstack11l111_opy_ (u"ࠫࡴࡶࡴࡪ࡯ࡤࡰࡤ࡮ࡵࡣࡡࡸࡶࡱ࠭ລ"): bstack1l1l1llll1_opy_(),
    bstack11l111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ຦"): {
      bstack11l111_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࡠࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫວ"): str(config[bstack11l111_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧຨ")]) if bstack11l111_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨຩ") in config else bstack11l111_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥສ"),
      bstack11l111_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩ࡛࡫ࡲࡴ࡫ࡲࡲࠬຫ"): sys.version,
      bstack11l111_opy_ (u"ࠫࡷ࡫ࡦࡦࡴࡵࡩࡷ࠭ຬ"): bstack11ll1lll1_opy_(os.environ.get(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧອ"), bstack1l1l11l1ll_opy_)),
      bstack11l111_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨຮ"): bstack11l111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧຯ"),
      bstack11l111_opy_ (u"ࠨࡲࡵࡳࡩࡻࡣࡵࠩະ"): bstack1l11ll1l11_opy_,
      bstack11l111_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࡢࡱࡦࡶࠧັ"): bstack11l1ll1l1_opy_,
      bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡣࡺࡻࡩࡥࠩາ"): os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩຳ")],
      bstack11l111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨິ"): os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨີ"), bstack1l1l11l1ll_opy_),
      bstack11l111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪຶ"): bstack11ll11l1l_opy_(os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪື"), bstack1l1l11l1ll_opy_)),
      bstack11l111_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨຸ"): bstack11lll11lll_opy_.get(bstack11l111_opy_ (u"ࠪࡲࡦࡳࡥࠨູ")),
      bstack11l111_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰ຺ࠪ"): bstack11lll11lll_opy_.get(bstack11l111_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ົ")),
      bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩຼ"): config[bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪຽ")] if config[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ຾")] else bstack11l111_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥ຿"),
      bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬເ"): str(config[bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ແ")]) if bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧໂ") in config else bstack11l111_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢໃ"),
      bstack11l111_opy_ (u"ࠧࡰࡵࠪໄ"): sys.platform,
      bstack11l111_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪ໅"): socket.gethostname(),
      bstack11l111_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫໆ"): bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ໇"))
    }
  }
  if not bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯່ࠫ")) is None:
    data[bstack11l111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ້")][bstack11l111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡎࡧࡷࡥࡩࡧࡴࡢ໊ࠩ")] = {
      bstack11l111_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴ໋ࠧ"): bstack11l111_opy_ (u"ࠨࡷࡶࡩࡷࡥ࡫ࡪ࡮࡯ࡩࡩ࠭໌"),
      bstack11l111_opy_ (u"ࠩࡶ࡭࡬ࡴࡡ࡭ࠩໍ"): bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪ໎")),
      bstack11l111_opy_ (u"ࠫࡸ࡯ࡧ࡯ࡣ࡯ࡒࡺࡳࡢࡦࡴࠪ໏"): bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱࡔ࡯ࠨ໐"))
    }
  if bstack1ll1ll1lll_opy_ == bstack1111llll1_opy_:
    data[bstack11l111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ໑")][bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡉ࡯࡯ࡨ࡬࡫ࠬ໒")] = bstack111lll1111_opy_(config)
    data[bstack11l111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໓")][bstack11l111_opy_ (u"ࠩ࡬ࡷࡕ࡫ࡲࡤࡻࡄࡹࡹࡵࡅ࡯ࡣࡥࡰࡪࡪࠧ໔")] = percy.bstack11l1l1111l_opy_
    data[bstack11l111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໕")][bstack11l111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡅࡹ࡮ࡲࡤࡊࡦࠪ໖")] = percy.percy_build_id
  if not bstack1llllllll_opy_.bstack11lll1l1l1_opy_(CONFIG):
    data[bstack11l111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ໗")][bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠪ໘")] = bstack1llllllll_opy_.bstack11lll1l1l1_opy_(CONFIG)
  bstack1lllll111_opy_ = bstack111l11l1_opy_.bstack111ll1ll_opy_(CONFIG, logger)
  bstack1lll1l1l1_opy_ = bstack1llllllll_opy_.bstack111ll1ll_opy_(config=CONFIG)
  if bstack1lllll111_opy_ is not None and bstack1lll1l1l1_opy_ is not None and bstack1lll1l1l1_opy_.bstack1llll1lll_opy_():
    data[bstack11l111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ໙")][bstack1lll1l1l1_opy_.bstack1l1l1l1111_opy_()] = bstack1lllll111_opy_.bstack1l1l11l11l_opy_()
  update(data[bstack11l111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໚")], bstack1l1l11ll1_opy_)
  try:
    response = bstack11ll11ll1l_opy_(bstack11l111_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ໛"), bstack11ll1l1l1_opy_(bstack11111lll11_opy_), data, {
      bstack11l111_opy_ (u"ࠪࡥࡺࡺࡨࠨໜ"): (config[bstack11l111_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ໝ")], config[bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨໞ")])
    })
    if response:
      logger.debug(bstack1llll1l111_opy_.format(bstack1ll1ll1lll_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11l1l11l11_opy_.format(str(e)))
def bstack11ll1lll1_opy_(framework):
  return bstack11l111_opy_ (u"ࠨࡻࡾ࠯ࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࡼࡿࠥໟ").format(str(framework), __version__) if framework else bstack11l111_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴ࢁࡽࠣ໠").format(
    __version__)
def bstack111l1l11l1_opy_():
  global CONFIG
  global bstack11lllllll1_opy_
  if bool(CONFIG):
    return
  try:
    bstack1l11lll11_opy_()
    logger.debug(bstack11l11llll1_opy_.format(str(CONFIG)))
    bstack11lllllll1_opy_ = bstack1lll11ll11_opy_.configure_logger(CONFIG, bstack11lllllll1_opy_)
    bstack1l1lll1ll_opy_()
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࡶࡲ࠯ࠤࡪࡸࡲࡰࡴ࠽ࠤࠧ໡") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1l1111lll1_opy_
  atexit.register(bstack1l111llll1_opy_)
  signal.signal(signal.SIGINT, bstack11111l1l11_opy_)
  signal.signal(signal.SIGTERM, bstack11111l1l11_opy_)
def bstack1l1111lll1_opy_(exctype, value, traceback):
  global bstack1l111ll1ll_opy_
  try:
    for driver in bstack1l111ll1ll_opy_:
      bstack1ll1ll1l11_opy_(driver, bstack11l111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ໢"), bstack11l111_opy_ (u"ࠥࡗࡪࡹࡳࡪࡱࡱࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨ໣") + str(value))
  except Exception:
    pass
  logger.info(bstack11l1111ll_opy_)
  bstack11lll1111_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack11lll1111_opy_(message=bstack11l111_opy_ (u"ࠫࠬ໤"), bstack1l1ll11111_opy_ = False):
  global CONFIG
  bstack11lll1l11l_opy_ = bstack11l111_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠧ໥") if bstack1l1ll11111_opy_ else bstack11l111_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ໦")
  try:
    if message:
      bstack1l1l11ll1_opy_ = {
        bstack11lll1l11l_opy_ : str(message)
      }
      bstack1111ll11l1_opy_(bstack1111llll1_opy_, CONFIG, bstack1l1l11ll1_opy_)
    else:
      bstack1111ll11l1_opy_(bstack1111llll1_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1l11l1ll1l_opy_.format(str(e)))
def bstack111ll1l11l_opy_(bstack1ll1ll111_opy_, size):
  bstack111ll1l111_opy_ = []
  while len(bstack1ll1ll111_opy_) > size:
    bstack1ll1ll111l_opy_ = bstack1ll1ll111_opy_[:size]
    bstack111ll1l111_opy_.append(bstack1ll1ll111l_opy_)
    bstack1ll1ll111_opy_ = bstack1ll1ll111_opy_[size:]
  bstack111ll1l111_opy_.append(bstack1ll1ll111_opy_)
  return bstack111ll1l111_opy_
def bstack1l1llll111_opy_(args):
  if bstack11l111_opy_ (u"ࠧ࠮࡯ࠪ໧") in args and bstack11l111_opy_ (u"ࠨࡲࡧࡦࠬ໨") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack111llllll1_opy_, stage=STAGE.bstack11111l1ll1_opy_)
def run_on_browserstack(bstack1lll1l11l1_opy_=None, bstack11lllll1l1_opy_=None, bstack111ll11111_opy_=False):
  global CONFIG
  global bstack11111llll1_opy_
  global bstack1lll1l1l11_opy_
  global bstack1l1l11l1ll_opy_
  global bstack111ll111_opy_
  bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"ࠩࠪ໩")
  bstack1l11ll111_opy_(bstack1111lll1ll_opy_, logger)
  if bstack1lll1l11l1_opy_ and isinstance(bstack1lll1l11l1_opy_, str):
    bstack1lll1l11l1_opy_ = eval(bstack1lll1l11l1_opy_)
  if bstack1lll1l11l1_opy_:
    CONFIG = bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪ໪")]
    bstack11111llll1_opy_ = bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬ໫")]
    bstack1lll1l1l11_opy_ = bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ໬")]
    bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ໭"), bstack1lll1l1l11_opy_)
    bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ໮")
  bstack111ll111_opy_.set_property(bstack11l111_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪ໯"), uuid4().__str__())
  logger.info(bstack11l111_opy_ (u"ࠩࡖࡈࡐࠦࡲࡶࡰࠣࡷࡹࡧࡲࡵࡧࡧࠤࡼ࡯ࡴࡩࠢ࡬ࡨ࠿ࠦࠧ໰") + bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ໱")));
  logger.debug(bstack11l111_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩࡃࠧ໲") + bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ໳")))
  if not bstack111ll11111_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack111l1l1lll_opy_)
      return
    if sys.argv[1] == bstack11l111_opy_ (u"࠭࠭࠮ࡸࡨࡶࡸ࡯࡯࡯ࠩ໴") or sys.argv[1] == bstack11l111_opy_ (u"ࠧ࠮ࡸࠪ໵"):
      logger.info(bstack11l111_opy_ (u"ࠨࡄࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡑࡻࡷ࡬ࡴࡴࠠࡔࡆࡎࠤࡻࢁࡽࠨ໶").format(__version__))
      return
    if sys.argv[1] == bstack11l111_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨ໷"):
      bstack111l1lllll_opy_()
      return
  args = sys.argv
  bstack111l1l11l1_opy_()
  global bstack11l1l1l1l1_opy_
  global bstack1lll111l1_opy_
  global bstack1ll11ll111_opy_
  global bstack1l1ll11l1l_opy_
  global bstack11l1llll1_opy_
  global bstack1l1111lll_opy_
  global bstack11l11111l1_opy_
  global bstack11111l1l1_opy_
  global bstack1l1l1l111_opy_
  global bstack1lllll111l_opy_
  global bstack11l11ll1l1_opy_
  bstack1lll111l1_opy_ = len(CONFIG.get(bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭໸"), []))
  if not bstack11l1ll1ll1_opy_:
    if args[1] == bstack11l111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ໹") or args[1] == bstack11l111_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭໺"):
      bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭໻")
      args = args[2:]
    elif args[1] == bstack11l111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭໼"):
      bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ໽")
      args = args[2:]
    elif args[1] == bstack11l111_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ໾"):
      bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ໿")
      args = args[2:]
    elif args[1] == bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬༀ"):
      bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭༁")
      args = args[2:]
    elif args[1] == bstack11l111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭༂"):
      bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ༃")
      args = args[2:]
    elif args[1] == bstack11l111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ༄"):
      bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ༅")
      args = args[2:]
    else:
      if not bstack11l111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭༆") in CONFIG or str(CONFIG[bstack11l111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ༇")]).lower() in [bstack11l111_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ༈"), bstack11l111_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧ༉")]:
        bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༊")
        args = args[1:]
      elif str(CONFIG[bstack11l111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ་")]).lower() == bstack11l111_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ༌"):
        bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ།")
        args = args[1:]
      elif str(CONFIG[bstack11l111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ༎")]).lower() == bstack11l111_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ༏"):
        bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ༐")
        args = args[1:]
      elif str(CONFIG[bstack11l111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༑")]).lower() == bstack11l111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ༒"):
        bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ༓")
        args = args[1:]
      elif str(CONFIG[bstack11l111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭༔")]).lower() == bstack11l111_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ༕"):
        bstack11l1ll1ll1_opy_ = bstack11l111_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ༖")
        args = args[1:]
      else:
        os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ༗")] = bstack11l1ll1ll1_opy_
        bstack1l111l1ll1_opy_(bstack1l1ll1111l_opy_)
  os.environ[bstack11l111_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨ༘")] = bstack11l1ll1ll1_opy_
  bstack1l1l11l1ll_opy_ = bstack11l1ll1ll1_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack111ll11ll_opy_ = bstack11l1l11ll1_opy_[bstack11l111_opy_ (u"ࠨࡒ࡜ࡘࡊ࡙ࡔ࠮ࡄࡇࡈ༙ࠬ")] if bstack11l1ll1ll1_opy_ == bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ༚") and bstack11llll1l11_opy_() else bstack11l1ll1ll1_opy_
      bstack1l1l111ll_opy_.invoke(Events.bstack111ll1llll_opy_, bstack1l1lll1l1_opy_(
        sdk_version=__version__,
        path_config=bstack1l1lllll1l_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack111ll11ll_opy_,
        frameworks=[bstack111ll11ll_opy_],
        framework_versions={
          bstack111ll11ll_opy_: bstack11ll11l1l_opy_(bstack11l111_opy_ (u"ࠪࡖࡴࡨ࡯ࡵࠩ༛") if bstack11l1ll1ll1_opy_ in [bstack11l111_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ༜"), bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༝"), bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ༞")] else bstack11l1ll1ll1_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack11l111_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤ༟"), None):
        CONFIG[bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥ༠")] = cli.config.get(bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦ༡"), None)
    except Exception as e:
      bstack1l1l111ll_opy_.invoke(Events.bstack11111ll1ll_opy_, e.__traceback__, 1)
    if bstack1lll1l1l11_opy_:
      CONFIG[bstack11l111_opy_ (u"ࠥࡥࡵࡶࠢ༢")] = cli.config[bstack11l111_opy_ (u"ࠦࡦࡶࡰࠣ༣")]
      logger.info(bstack1lll1ll1l1_opy_.format(CONFIG[bstack11l111_opy_ (u"ࠬࡧࡰࡱࠩ༤")]))
  else:
    bstack1l1l111ll_opy_.clear()
  global bstack11l111ll11_opy_
  global bstack1111l1l1l1_opy_
  if bstack1lll1l11l1_opy_:
    try:
      bstack1lll1l1ll1_opy_ = datetime.datetime.now()
      os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ༥")] = bstack11l1ll1ll1_opy_
      bstack1111ll11l1_opy_(bstack1l1lll111_opy_, CONFIG)
      cli.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠢࡩࡶࡷࡴ࠿ࡹࡤ࡬ࡡࡷࡩࡸࡺ࡟ࡢࡶࡷࡩࡲࡶࡴࡦࡦࠥ༦"), datetime.datetime.now() - bstack1lll1l1ll1_opy_)
    except Exception as e:
      logger.debug(bstack11l1111111_opy_.format(str(e)))
  global bstack1ll1lllll1_opy_
  global bstack11l11lll1_opy_
  global bstack1111llllll_opy_
  global bstack11ll1lll11_opy_
  global bstack11l1l11111_opy_
  global bstack11l1llll1l_opy_
  global bstack11l1l11l1l_opy_
  global bstack1lll111ll1_opy_
  global bstack1l1llll1l_opy_
  global bstack1111l11111_opy_
  global bstack11lll1111l_opy_
  global bstack111l1l111_opy_
  global bstack1l111lll1l_opy_
  global bstack1l1ll1llll_opy_
  global bstack11l11l11ll_opy_
  global bstack1ll111llll_opy_
  global bstack111llll1l_opy_
  global bstack11ll11llll_opy_
  global bstack1l11l11ll1_opy_
  global bstack1ll111l11l_opy_
  global bstack11llllllll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll1lllll1_opy_ = webdriver.Remote.__init__
    bstack11l11lll1_opy_ = WebDriver.quit
    bstack111l1l111_opy_ = WebDriver.close
    bstack11l11l11ll_opy_ = WebDriver.get
    bstack11llllllll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack11l111ll11_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack11ll1l11ll_opy_
    bstack1111l1l1l1_opy_ = bstack11ll1l11ll_opy_()
  except Exception as e:
    pass
  try:
    global bstack1l11111l1_opy_
    from QWeb.keywords import browser
    bstack1l11111l1_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack11lll111l_opy_(CONFIG) and bstack1llll11l11_opy_():
    if bstack1l11l1l11l_opy_() < version.parse(bstack111111lll_opy_):
      logger.error(bstack11111l1l1l_opy_.format(bstack1l11l1l11l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11l111_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩ༧")) and callable(getattr(RemoteConnection, bstack11l111_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ༨"))):
          RemoteConnection._get_proxy_url = bstack1ll1l111ll_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack1ll1l111ll_opy_
      except Exception as e:
        logger.error(bstack111111ll1_opy_.format(str(e)))
  if not CONFIG.get(bstack11l111_opy_ (u"ࠪࡨ࡮ࡹࡡࡣ࡮ࡨࡅࡺࡺ࡯ࡄࡣࡳࡸࡺࡸࡥࡍࡱࡪࡷࠬ༩"), False) and not bstack1lll1l11l1_opy_:
    logger.info(bstack1l11l1l111_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack11l111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ༪") in CONFIG and str(CONFIG[bstack11l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ༫")]).lower() != bstack11l111_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ༬"):
      bstack111l1l1l11_opy_()
    elif bstack11l1ll1ll1_opy_ != bstack11l111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༭") or (bstack11l1ll1ll1_opy_ == bstack11l111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ༮") and not bstack1lll1l11l1_opy_):
      bstack11l11ll111_opy_()
  if (bstack11l1ll1ll1_opy_ in [bstack11l111_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༯"), bstack11l111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ༰"), bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ༱")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1111lll11l_opy_
        bstack11l1llll1l_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1l11ll1lll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack11l1l11111_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack111l11l1l1_opy_ + str(e))
    except Exception as e:
      bstack1ll1lll1l_opy_(e, bstack1l11ll1lll_opy_)
    if bstack11l1ll1ll1_opy_ != bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭༲"):
      bstack11l1ll11l_opy_()
    bstack1111llllll_opy_ = Output.start_test
    bstack11ll1lll11_opy_ = Output.end_test
    bstack11l1l11l1l_opy_ = TestStatus.__init__
    bstack1l1llll1l_opy_ = pabot._run
    bstack1111l11111_opy_ = QueueItem.__init__
    bstack11lll1111l_opy_ = pabot._create_command_for_execution
    bstack1l11l11ll1_opy_ = pabot._report_results
  if bstack11l1ll1ll1_opy_ == bstack11l111_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭༳"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1ll1lll1l_opy_(e, bstack11ll1llll_opy_)
    bstack1l111lll1l_opy_ = Runner.run_hook
    bstack1l1ll1llll_opy_ = Step.run
  if bstack11l1ll1ll1_opy_ == bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ༴"):
    try:
      from _pytest.config import Config
      bstack111llll1l_opy_ = Config.getoption
      from _pytest import runner
      bstack11ll11llll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack11l11ll1_opy_)
    try:
      from pytest_bdd import reporting
      bstack1ll111l11l_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴ༵ࠩ"))
  try:
    framework_name = bstack11l111_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ༶") if bstack11l1ll1ll1_opy_ in [bstack11l111_opy_ (u"ࠪࡴࡦࡨ࡯ࡵ༷ࠩ"), bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༸"), bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ༹࠭")] else bstack1l11lll1ll_opy_(bstack11l1ll1ll1_opy_)
    bstack1l11ll1ll_opy_ = {
      bstack11l111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠧ༺"): bstack11l111_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺ࠭ࡤࡷࡦࡹࡲࡨࡥࡳࠩ༻") if bstack11l1ll1ll1_opy_ == bstack11l111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ༼") and bstack11llll1l11_opy_() else framework_name,
      bstack11l111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭༽"): bstack11ll11l1l_opy_(framework_name),
      bstack11l111_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ༾"): __version__,
      bstack11l111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡶࡵࡨࡨࠬ༿"): bstack11l1ll1ll1_opy_
    }
    if bstack11l1ll1ll1_opy_ in bstack11111llll_opy_ + bstack1l11ll1l1_opy_:
      if bstack11l111l1_opy_.bstack1l1111llll_opy_(CONFIG):
        if bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬཀ") in CONFIG:
          os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧཁ")] = os.getenv(bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨག"), json.dumps(CONFIG[bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨགྷ")]))
          CONFIG[bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩང")].pop(bstack11l111_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨཅ"), None)
          CONFIG[bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫཆ")].pop(bstack11l111_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪཇ"), None)
        bstack1l11ll1ll_opy_[bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭཈")] = {
          bstack11l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬཉ"): bstack11l111_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪཊ"),
          bstack11l111_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪཋ"): str(bstack1l11l1l11l_opy_())
        }
    if bstack11l1ll1ll1_opy_ not in [bstack11l111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫཌ")] and not cli.is_running():
      bstack1l11ll1111_opy_, bstack1ll1ll11ll_opy_ = bstack1lll1l1l_opy_.launch(CONFIG, bstack1l11ll1ll_opy_)
      if bstack1ll1ll11ll_opy_.get(bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫཌྷ")) is not None and bstack11l111l1_opy_.bstack1lll1l1lll_opy_(CONFIG) is None:
        value = bstack1ll1ll11ll_opy_[bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬཎ")].get(bstack11l111_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧཏ"))
        if value is not None:
            CONFIG[bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧཐ")] = value
        else:
          logger.debug(bstack11l111_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡩࡧࡴࡢࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠨད"))
  except Exception as e:
    logger.debug(bstack1l11l11l1l_opy_.format(bstack11l111_opy_ (u"ࠩࡗࡩࡸࡺࡈࡶࡤࠪདྷ"), str(e)))
  if bstack11l1ll1ll1_opy_ == bstack11l111_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪན"):
    bstack1ll11ll111_opy_ = True
    if bstack1lll1l11l1_opy_ and bstack111ll11111_opy_:
      bstack1l1111lll_opy_ = CONFIG.get(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨཔ"), {}).get(bstack11l111_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧཕ"))
      bstack1111l1llll_opy_(bstack11llll1lll_opy_)
    elif bstack1lll1l11l1_opy_:
      bstack1l1111lll_opy_ = CONFIG.get(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪབ"), {}).get(bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩབྷ"))
      global bstack1l111ll1ll_opy_
      try:
        if bstack1l1llll111_opy_(bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫམ")]) and multiprocessing.current_process().name == bstack11l111_opy_ (u"ࠩ࠳ࠫཙ"):
          bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ཚ")].remove(bstack11l111_opy_ (u"ࠫ࠲ࡳࠧཛ"))
          bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨཛྷ")].remove(bstack11l111_opy_ (u"࠭ࡰࡥࡤࠪཝ"))
          bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪཞ")] = bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫཟ")][0]
          with open(bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬའ")], bstack11l111_opy_ (u"ࠪࡶࠬཡ")) as f:
            file_content = f.read()
          bstack1l1ll111ll_opy_ = bstack11l111_opy_ (u"ࠦࠧࠨࡦࡳࡱࡰࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡷࡩࡱࠠࡪ࡯ࡳࡳࡷࡺࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧ࠾ࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫ࠨࡼࡿࠬ࠿ࠥ࡬ࡲࡰ࡯ࠣࡴࡩࡨࠠࡪ࡯ࡳࡳࡷࡺࠠࡑࡦࡥ࠿ࠥࡵࡧࡠࡦࡥࠤࡂࠦࡐࡥࡤ࠱ࡨࡴࡥࡢࡳࡧࡤ࡯ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡧࡩ࡫ࠦ࡭ࡰࡦࡢࡦࡷ࡫ࡡ࡬ࠪࡶࡩࡱ࡬ࠬࠡࡣࡵ࡫࠱ࠦࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠢࡀࠤ࠵࠯࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡳࡻ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡦࡸࡧࠡ࠿ࠣࡷࡹࡸࠨࡪࡰࡷࠬࡦࡸࡧࠪ࠭࠴࠴࠮ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡪࡾࡣࡦࡲࡷࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡢࡵࠣࡩ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡰࡢࡵࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡲ࡫ࡤࡪࡢࠩࡵࡨࡰ࡫࠲ࡡࡳࡩ࠯ࡸࡪࡳࡰࡰࡴࡤࡶࡾ࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡔࡩࡨ࠮ࡥࡱࡢࡦࠥࡃࠠ࡮ࡱࡧࡣࡧࡸࡥࡢ࡭ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡥࡤ࠱ࡨࡴࡥࡢࡳࡧࡤ࡯ࠥࡃࠠ࡮ࡱࡧࡣࡧࡸࡥࡢ࡭ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡥࡤࠫ࠭࠳ࡹࡥࡵࡡࡷࡶࡦࡩࡥࠩࠫ࡟ࡲࠧࠨࠢར").format(str(bstack1lll1l11l1_opy_))
          bstack11l1l1111_opy_ = bstack1l1ll111ll_opy_ + file_content
          bstack1l1ll1111_opy_ = bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨལ")] + bstack11l111_opy_ (u"࠭࡟ࡣࡵࡷࡥࡨࡱ࡟ࡵࡧࡰࡴ࠳ࡶࡹࠨཤ")
          with open(bstack1l1ll1111_opy_, bstack11l111_opy_ (u"ࠧࡸࠩཥ")):
            pass
          with open(bstack1l1ll1111_opy_, bstack11l111_opy_ (u"ࠣࡹ࠮ࠦས")) as f:
            f.write(bstack11l1l1111_opy_)
          import subprocess
          process_data = subprocess.run([bstack11l111_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࠤཧ"), bstack1l1ll1111_opy_])
          if os.path.exists(bstack1l1ll1111_opy_):
            os.unlink(bstack1l1ll1111_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack1l1llll111_opy_(bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ཨ")]):
            bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཀྵ")].remove(bstack11l111_opy_ (u"ࠬ࠳࡭ࠨཪ"))
            bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩཫ")].remove(bstack11l111_opy_ (u"ࠧࡱࡦࡥࠫཬ"))
            bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ཭")] = bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ཮")][0]
          bstack1111l1llll_opy_(bstack11llll1lll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭཯")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11l111_opy_ (u"ࠫࡤࡥ࡮ࡢ࡯ࡨࡣࡤ࠭཰")] = bstack11l111_opy_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥཱࠧ")
          mod_globals[bstack11l111_opy_ (u"࠭࡟ࡠࡨ࡬ࡰࡪࡥ࡟ࠨི")] = os.path.abspath(bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧཱིࠪ")])
          exec(open(bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨུࠫ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11l111_opy_ (u"ࠩࡆࡥࡺ࡭ࡨࡵࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾཱུࠩ").format(str(e)))
          for driver in bstack1l111ll1ll_opy_:
            bstack11lllll1l1_opy_.append({
              bstack11l111_opy_ (u"ࠪࡲࡦࡳࡥࠨྲྀ"): bstack1lll1l11l1_opy_[bstack11l111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཷ")],
              bstack11l111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫླྀ"): str(e),
              bstack11l111_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬཹ"): multiprocessing.current_process().name
            })
            bstack1ll1ll1l11_opy_(driver, bstack11l111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪེࠧ"), bstack11l111_opy_ (u"ࠣࡕࡨࡷࡸ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱཻࠦ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l111ll1ll_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack1lll1l1l11_opy_, CONFIG, logger)
      bstack111lll11ll_opy_()
      bstack1ll111l1l_opy_()
      percy.bstack1111lllll1_opy_()
      bstack111l1111_opy_ = {
        bstack11l111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩོࠬ"): args[0],
        bstack11l111_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉཽࠪ"): CONFIG,
        bstack11l111_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬཾ"): bstack11111llll1_opy_,
        bstack11l111_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧཿ"): bstack1lll1l1l11_opy_
      }
      if bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴྀࠩ") in CONFIG:
        bstack1l1l111111_opy_ = bstack11l1lll1l1_opy_(args, logger, CONFIG, bstack1l1111l11_opy_, bstack1lll111l1_opy_)
        bstack11111l1l1_opy_ = bstack1l1l111111_opy_.bstack11111l1l_opy_(run_on_browserstack, bstack111l1111_opy_, bstack1l1llll111_opy_(args))
      else:
        if bstack1l1llll111_opy_(args):
          bstack111l1111_opy_[bstack11l111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧཱྀࠪ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack111l1111_opy_,))
          test.start()
          test.join()
        else:
          bstack1111l1llll_opy_(bstack11llll1lll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11l111_opy_ (u"ࠨࡡࡢࡲࡦࡳࡥࡠࡡࠪྂ")] = bstack11l111_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫྃ")
          mod_globals[bstack11l111_opy_ (u"ࠪࡣࡤ࡬ࡩ࡭ࡧࡢࡣ྄ࠬ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack11l1ll1ll1_opy_ == bstack11l111_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ྅") or bstack11l1ll1ll1_opy_ == bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ྆"):
    percy.init(bstack1lll1l1l11_opy_, CONFIG, logger)
    percy.bstack1111lllll1_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1ll1lll1l_opy_(e, bstack1l11ll1lll_opy_)
    bstack111lll11ll_opy_()
    bstack1111l1llll_opy_(bstack11llll1ll_opy_)
    if bstack1l1111l11_opy_:
      bstack1llll1ll1l_opy_(bstack11llll1ll_opy_, args)
      if bstack11l111_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ྇") in args:
        i = args.index(bstack11l111_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬྈ"))
        args.pop(i)
        args.pop(i)
      if bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫྉ") not in CONFIG:
        CONFIG[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྊ")] = [{}]
        bstack1lll111l1_opy_ = 1
      if bstack11l1l1l1l1_opy_ == 0:
        bstack11l1l1l1l1_opy_ = 1
      args.insert(0, str(bstack11l1l1l1l1_opy_))
      args.insert(0, str(bstack11l111_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨྋ")))
    if bstack1lll1l1l_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack11111l1lll_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack11111ll1l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11l111_opy_ (u"ࠦࡗࡕࡂࡐࡖࡢࡓࡕ࡚ࡉࡐࡐࡖࠦྌ"),
        ).parse_args(bstack11111l1lll_opy_)
        bstack1l1lll1111_opy_ = args.index(bstack11111l1lll_opy_[0]) if len(bstack11111l1lll_opy_) > 0 else len(args)
        args.insert(bstack1l1lll1111_opy_, str(bstack11l111_opy_ (u"ࠬ࠳࠭࡭࡫ࡶࡸࡪࡴࡥࡳࠩྍ")))
        args.insert(bstack1l1lll1111_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡲࡰࡤࡲࡸࡤࡲࡩࡴࡶࡨࡲࡪࡸ࠮ࡱࡻࠪྎ"))))
        if bstack1llllllll_opy_.bstack111l111l_opy_(CONFIG):
          args.insert(bstack1l1lll1111_opy_, str(bstack11l111_opy_ (u"ࠧ࠮࠯࡯࡭ࡸࡺࡥ࡯ࡧࡵࠫྏ")))
          args.insert(bstack1l1lll1111_opy_ + 1, str(bstack11l111_opy_ (u"ࠨࡔࡨࡸࡷࡿࡆࡢ࡫࡯ࡩࡩࡀࡻࡾࠩྐ").format(bstack1llllllll_opy_.bstack111lll1l_opy_(CONFIG))))
        if bstack11lll1lll_opy_(os.environ.get(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠧྑ"))) and str(os.environ.get(bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧྒ"), bstack11l111_opy_ (u"ࠫࡳࡻ࡬࡭ࠩྒྷ"))) != bstack11l111_opy_ (u"ࠬࡴࡵ࡭࡮ࠪྔ"):
          for bstack1lll11l11l_opy_ in bstack11111ll1l_opy_:
            args.remove(bstack1lll11l11l_opy_)
          test_files = os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠪྕ")).split(bstack11l111_opy_ (u"ࠧ࠭ࠩྖ"))
          for bstack111ll111l_opy_ in test_files:
            args.append(bstack111ll111l_opy_)
      except Exception as e:
        logger.error(bstack11l111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡡࡵࡶࡤࡧ࡭࡯࡮ࡨࠢ࡯࡭ࡸࡺࡥ࡯ࡧࡵࠤ࡫ࡵࡲࠡࡽࢀ࠲ࠥࡋࡲࡳࡱࡵࠤ࠲ࠦࡻࡾࠤྗ").format(bstack1l11ll1l1l_opy_, e))
    pabot.main(args)
  elif bstack11l1ll1ll1_opy_ == bstack11l111_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ྘"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1ll1lll1l_opy_(e, bstack1l11ll1lll_opy_)
    for a in args:
      if bstack11l111_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙ࠩྙ") in a:
        bstack11l1llll1_opy_ = int(a.split(bstack11l111_opy_ (u"ࠫ࠿࠭ྚ"))[1])
      if bstack11l111_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡉࡋࡆࡍࡑࡆࡅࡑࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩྛ") in a:
        bstack1l1111lll_opy_ = str(a.split(bstack11l111_opy_ (u"࠭࠺ࠨྜ"))[1])
      if bstack11l111_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡃࡍࡋࡄࡖࡌ࡙ࠧྜྷ") in a:
        bstack11l11111l1_opy_ = str(a.split(bstack11l111_opy_ (u"ࠨ࠼ࠪྞ"))[1])
    bstack1ll1l1lll_opy_ = None
    if bstack11l111_opy_ (u"ࠩ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠨྟ") in args:
      i = args.index(bstack11l111_opy_ (u"ࠪ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠩྠ"))
      args.pop(i)
      bstack1ll1l1lll_opy_ = args.pop(i)
    if bstack1ll1l1lll_opy_ is not None:
      global bstack11ll111111_opy_
      bstack11ll111111_opy_ = bstack1ll1l1lll_opy_
    bstack1111l1llll_opy_(bstack11llll1ll_opy_)
    run_cli(args)
    if bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨྡ") in multiprocessing.current_process().__dict__.keys():
      for bstack11l1lll11l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11lllll1l1_opy_.append(bstack11l1lll11l_opy_)
  elif bstack11l1ll1ll1_opy_ == bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬྡྷ"):
    bstack11ll1l1ll_opy_ = bstack1111l1l1_opy_(args, logger, CONFIG, bstack1l1111l11_opy_)
    bstack11ll1l1ll_opy_.bstack111ll1l1_opy_()
    bstack111lll11ll_opy_()
    bstack1l1ll11l1l_opy_ = True
    bstack1lllll111l_opy_ = bstack11ll1l1ll_opy_.bstack1111l11l_opy_()
    bstack11ll1l1ll_opy_.bstack111l1111_opy_(bstack11l1ll1lll_opy_)
    bstack11ll1l1ll_opy_.bstack1llllll1l_opy_()
    bstack1111ll111l_opy_(bstack11l1ll1ll1_opy_, CONFIG, bstack11ll1l1ll_opy_.bstack1111l111_opy_())
    bstack1ll1111l11_opy_ = bstack11ll1l1ll_opy_.bstack11111l1l_opy_(bstack1l1111ll11_opy_, {
      bstack11l111_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧྣ"): bstack11111llll1_opy_,
      bstack11l111_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩྤ"): bstack1lll1l1l11_opy_,
      bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫྥ"): bstack1l1111l11_opy_
    })
    try:
      bstack11l111l1l_opy_, bstack111l1lll1_opy_ = map(list, zip(*bstack1ll1111l11_opy_))
      bstack1l1l1l111_opy_ = bstack11l111l1l_opy_[0]
      for status_code in bstack111l1lll1_opy_:
        if status_code != 0:
          bstack11l11ll1l1_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡡࡷࡧࠣࡩࡷࡸ࡯ࡳࡵࠣࡥࡳࡪࠠࡴࡶࡤࡸࡺࡹࠠࡤࡱࡧࡩ࠳ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࠽ࠤࢀࢃࠢྦ").format(str(e)))
  elif bstack11l1ll1ll1_opy_ == bstack11l111_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪྦྷ"):
    try:
      from behave.__main__ import main as bstack11ll1111l1_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1ll1lll1l_opy_(e, bstack11ll1llll_opy_)
    bstack111lll11ll_opy_()
    bstack1l1ll11l1l_opy_ = True
    bstack1111111l_opy_ = 1
    if bstack11l111_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫྨ") in CONFIG:
      bstack1111111l_opy_ = CONFIG[bstack11l111_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬྩ")]
    if bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩྪ") in CONFIG:
      bstack111l1l1l1_opy_ = int(bstack1111111l_opy_) * int(len(CONFIG[bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪྫ")]))
    else:
      bstack111l1l1l1_opy_ = int(bstack1111111l_opy_)
    config = Configuration(args)
    bstack1l111ll11_opy_ = config.paths
    if len(bstack1l111ll11_opy_) == 0:
      import glob
      pattern = bstack11l111_opy_ (u"ࠨࠬ࠭࠳࠯࠴ࡦࡦࡣࡷࡹࡷ࡫ࠧྫྷ")
      bstack1111ll11l_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1111ll11l_opy_)
      config = Configuration(args)
      bstack1l111ll11_opy_ = config.paths
    bstack11l111ll_opy_ = [os.path.normpath(item) for item in bstack1l111ll11_opy_]
    bstack111lll11l_opy_ = [os.path.normpath(item) for item in args]
    bstack1llll11111_opy_ = [item for item in bstack111lll11l_opy_ if item not in bstack11l111ll_opy_]
    import platform as pf
    if pf.system().lower() == bstack11l111_opy_ (u"ࠩࡺ࡭ࡳࡪ࡯ࡸࡵࠪྭ"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack11l111ll_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1111ll1l1l_opy_)))
                    for bstack1111ll1l1l_opy_ in bstack11l111ll_opy_]
    bstack1lllll1l1_opy_ = []
    for spec in bstack11l111ll_opy_:
      bstack1111ll11_opy_ = []
      bstack1111ll11_opy_ += bstack1llll11111_opy_
      bstack1111ll11_opy_.append(spec)
      bstack1lllll1l1_opy_.append(bstack1111ll11_opy_)
    execution_items = []
    for bstack1111ll11_opy_ in bstack1lllll1l1_opy_:
      if bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྮ") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྯ")]):
          item = {}
          item[bstack11l111_opy_ (u"ࠬࡧࡲࡨࠩྰ")] = bstack11l111_opy_ (u"࠭ࠠࠨྱ").join(bstack1111ll11_opy_)
          item[bstack11l111_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ྲ")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack11l111_opy_ (u"ࠨࡣࡵ࡫ࠬླ")] = bstack11l111_opy_ (u"ࠩࠣࠫྴ").join(bstack1111ll11_opy_)
        item[bstack11l111_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩྵ")] = 0
        execution_items.append(item)
    bstack1l1l11l111_opy_ = bstack111ll1l11l_opy_(execution_items, bstack111l1l1l1_opy_)
    for execution_item in bstack1l1l11l111_opy_:
      bstack1111l1ll_opy_ = []
      for item in execution_item:
        bstack1111l1ll_opy_.append(bstack111l11ll1l_opy_(name=str(item[bstack11l111_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪྶ")]),
                                             target=bstack1l1llll1l1_opy_,
                                             args=(item[bstack11l111_opy_ (u"ࠬࡧࡲࡨࠩྷ")],)))
      for t in bstack1111l1ll_opy_:
        t.start()
      for t in bstack1111l1ll_opy_:
        t.join()
  else:
    bstack1l111l1ll1_opy_(bstack1l1ll1111l_opy_)
  if not bstack1lll1l11l1_opy_:
    bstack1ll11l1lll_opy_()
    if(bstack11l1ll1ll1_opy_ in [bstack11l111_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ྸ"), bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧྐྵ")]):
      bstack11lllll1l_opy_()
  bstack1lll11ll11_opy_.bstack111ll1l1ll_opy_()
def browserstack_initialize(bstack11l111l11_opy_=None):
  logger.info(bstack11l111_opy_ (u"ࠨࡔࡸࡲࡳ࡯࡮ࡨࠢࡖࡈࡐࠦࡷࡪࡶ࡫ࠤࡦࡸࡧࡴ࠼ࠣࠫྺ") + str(bstack11l111l11_opy_))
  run_on_browserstack(bstack11l111l11_opy_, None, True)
@measure(event_name=EVENTS.bstack11l1l1ll1l_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack1ll11l1lll_opy_():
  global CONFIG
  global bstack1l1l11l1ll_opy_
  global bstack11l11ll1l1_opy_
  global bstack111l1ll111_opy_
  global bstack111ll111_opy_
  bstack1l11l1ll1_opy_.bstack1ll1l1ll11_opy_()
  if cli.is_running():
    bstack1l1l111ll_opy_.invoke(Events.bstack111l111ll_opy_)
  else:
    bstack1lll1l1l1_opy_ = bstack1llllllll_opy_.bstack111ll1ll_opy_(config=CONFIG)
    bstack1lll1l1l1_opy_.bstack1l111llll_opy_(CONFIG)
  if bstack1l1l11l1ll_opy_ == bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩྻ"):
    if not cli.is_enabled(CONFIG):
      bstack1lll1l1l_opy_.stop()
  else:
    bstack1lll1l1l_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1l1l11l1_opy_.bstack1l1111ll1_opy_()
  if bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧྼ") in CONFIG and str(CONFIG[bstack11l111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ྽")]).lower() != bstack11l111_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ྾"):
    hashed_id, bstack11lllll111_opy_ = bstack1lll1llll1_opy_()
  else:
    hashed_id, bstack11lllll111_opy_ = get_build_link()
  bstack1lll111111_opy_(hashed_id)
  logger.info(bstack11l111_opy_ (u"࠭ࡓࡅࡍࠣࡶࡺࡴࠠࡦࡰࡧࡩࡩࠦࡦࡰࡴࠣ࡭ࡩࡀࠧ྿") + bstack111ll111_opy_.get_property(bstack11l111_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ࿀"), bstack11l111_opy_ (u"ࠨࠩ࿁")) + bstack11l111_opy_ (u"ࠩ࠯ࠤࡹ࡫ࡳࡵࡪࡸࡦࠥ࡯ࡤ࠻ࠢࠪ࿂") + os.getenv(bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ࿃"), bstack11l111_opy_ (u"ࠫࠬ࿄")))
  if hashed_id is not None and bstack1l1llllll_opy_() != -1:
    sessions = bstack1l11l1111_opy_(hashed_id)
    bstack1ll1ll1111_opy_(sessions, bstack11lllll111_opy_)
  if bstack1l1l11l1ll_opy_ == bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ࿅") and bstack11l11ll1l1_opy_ != 0:
    sys.exit(bstack11l11ll1l1_opy_)
  if bstack1l1l11l1ll_opy_ == bstack11l111_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࿆࠭") and bstack111l1ll111_opy_ != 0:
    sys.exit(bstack111l1ll111_opy_)
def bstack1lll111111_opy_(new_id):
    global bstack1111ll111_opy_
    bstack1111ll111_opy_ = new_id
def bstack1l11lll1ll_opy_(bstack1lll11l111_opy_):
  if bstack1lll11l111_opy_:
    return bstack1lll11l111_opy_.capitalize()
  else:
    return bstack11l111_opy_ (u"ࠧࠨ࿇")
@measure(event_name=EVENTS.bstack1ll1l11l1l_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack1ll11llll1_opy_(bstack11ll111ll1_opy_):
  if bstack11l111_opy_ (u"ࠨࡰࡤࡱࡪ࠭࿈") in bstack11ll111ll1_opy_ and bstack11ll111ll1_opy_[bstack11l111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ࿉")] != bstack11l111_opy_ (u"ࠪࠫ࿊"):
    return bstack11ll111ll1_opy_[bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ࿋")]
  else:
    bstack1l1l111l11_opy_ = bstack11l111_opy_ (u"ࠧࠨ࿌")
    if bstack11l111_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭࿍") in bstack11ll111ll1_opy_ and bstack11ll111ll1_opy_[bstack11l111_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ࿎")] != None:
      bstack1l1l111l11_opy_ += bstack11ll111ll1_opy_[bstack11l111_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ࿏")] + bstack11l111_opy_ (u"ࠤ࠯ࠤࠧ࿐")
      if bstack11ll111ll1_opy_[bstack11l111_opy_ (u"ࠪࡳࡸ࠭࿑")] == bstack11l111_opy_ (u"ࠦ࡮ࡵࡳࠣ࿒"):
        bstack1l1l111l11_opy_ += bstack11l111_opy_ (u"ࠧ࡯ࡏࡔࠢࠥ࿓")
      bstack1l1l111l11_opy_ += (bstack11ll111ll1_opy_[bstack11l111_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪ࿔")] or bstack11l111_opy_ (u"ࠧࠨ࿕"))
      return bstack1l1l111l11_opy_
    else:
      bstack1l1l111l11_opy_ += bstack1l11lll1ll_opy_(bstack11ll111ll1_opy_[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ࿖")]) + bstack11l111_opy_ (u"ࠤࠣࠦ࿗") + (
              bstack11ll111ll1_opy_[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ࿘")] or bstack11l111_opy_ (u"ࠫࠬ࿙")) + bstack11l111_opy_ (u"ࠧ࠲ࠠࠣ࿚")
      if bstack11ll111ll1_opy_[bstack11l111_opy_ (u"࠭࡯ࡴࠩ࿛")] == bstack11l111_opy_ (u"ࠢࡘ࡫ࡱࡨࡴࡽࡳࠣ࿜"):
        bstack1l1l111l11_opy_ += bstack11l111_opy_ (u"࡙ࠣ࡬ࡲࠥࠨ࿝")
      bstack1l1l111l11_opy_ += bstack11ll111ll1_opy_[bstack11l111_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭࿞")] or bstack11l111_opy_ (u"ࠪࠫ࿟")
      return bstack1l1l111l11_opy_
@measure(event_name=EVENTS.bstack111l1llll_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack111lllll1l_opy_(bstack1l1l11l1l_opy_):
  if bstack1l1l11l1l_opy_ == bstack11l111_opy_ (u"ࠦࡩࡵ࡮ࡦࠤ࿠"):
    return bstack11l111_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡨࡴࡨࡩࡳࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡨࡴࡨࡩࡳࠨ࠾ࡄࡱࡰࡴࡱ࡫ࡴࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨ࿡")
  elif bstack1l1l11l1l_opy_ == bstack11l111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ࿢"):
    return bstack11l111_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡵࡩࡩࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡳࡧࡧࠦࡃࡌࡡࡪ࡮ࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪ࿣")
  elif bstack1l1l11l1l_opy_ == bstack11l111_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ࿤"):
    return bstack11l111_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡕࡧࡳࡴࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ࿥")
  elif bstack1l1l11l1l_opy_ == bstack11l111_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ࿦"):
    return bstack11l111_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡈࡶࡷࡵࡲ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭࿧")
  elif bstack1l1l11l1l_opy_ == bstack11l111_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨ࿨"):
    return bstack11l111_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࠥࡨࡩࡦ࠹࠲࠷࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࠧࡪ࡫ࡡ࠴࠴࠹ࠦࡃ࡚ࡩ࡮ࡧࡲࡹࡹࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫ࿩")
  elif bstack1l1l11l1l_opy_ == bstack11l111_opy_ (u"ࠢࡳࡷࡱࡲ࡮ࡴࡧࠣ࿪"):
    return bstack11l111_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡦࡱࡧࡣ࡬࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡦࡱࡧࡣ࡬ࠤࡁࡖࡺࡴ࡮ࡪࡰࡪࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ࿫")
  else:
    return bstack11l111_opy_ (u"ࠩ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡨ࡬ࡢࡥ࡮࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡨ࡬ࡢࡥ࡮ࠦࡃ࠭࿬") + bstack1l11lll1ll_opy_(
      bstack1l1l11l1l_opy_) + bstack11l111_opy_ (u"ࠪࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩ࿭")
def bstack1ll1ll11l_opy_(session):
  return bstack11l111_opy_ (u"ࠫࡁࡺࡲࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡴࡲࡻࠧࡄ࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠡࡵࡨࡷࡸ࡯࡯࡯࠯ࡱࡥࡲ࡫ࠢ࠿࠾ࡤࠤ࡭ࡸࡥࡧ࠿ࠥࡿࢂࠨࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣࡡࡥࡰࡦࡴ࡫ࠣࡀࡾࢁࡁ࠵ࡡ࠿࠾࠲ࡸࡩࡄࡻࡾࡽࢀࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂ࠯ࡵࡴࡁࠫ࿮").format(
    session[bstack11l111_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧࡤࡻࡲ࡭ࠩ࿯")], bstack1ll11llll1_opy_(session), bstack111lllll1l_opy_(session[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡴࡢࡶࡸࡷࠬ࿰")]),
    bstack111lllll1l_opy_(session[bstack11l111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ࿱")]),
    bstack1l11lll1ll_opy_(session[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ࿲")] or session[bstack11l111_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ࿳")] or bstack11l111_opy_ (u"ࠪࠫ࿴")) + bstack11l111_opy_ (u"ࠦࠥࠨ࿵") + (session[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ࿶")] or bstack11l111_opy_ (u"࠭ࠧ࿷")),
    session[bstack11l111_opy_ (u"ࠧࡰࡵࠪ࿸")] + bstack11l111_opy_ (u"ࠣࠢࠥ࿹") + session[bstack11l111_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭࿺")], session[bstack11l111_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬ࿻")] or bstack11l111_opy_ (u"ࠫࠬ࿼"),
    session[bstack11l111_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩ࿽")] if session[bstack11l111_opy_ (u"࠭ࡣࡳࡧࡤࡸࡪࡪ࡟ࡢࡶࠪ࿾")] else bstack11l111_opy_ (u"ࠧࠨ࿿"))
@measure(event_name=EVENTS.bstack11l1l1l1ll_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def bstack1ll1ll1111_opy_(sessions, bstack11lllll111_opy_):
  try:
    bstack1l1111l11l_opy_ = bstack11l111_opy_ (u"ࠣࠤက")
    if not os.path.exists(bstack111lll111_opy_):
      os.mkdir(bstack111lll111_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l111_opy_ (u"ࠩࡤࡷࡸ࡫ࡴࡴ࠱ࡵࡩࡵࡵࡲࡵ࠰࡫ࡸࡲࡲࠧခ")), bstack11l111_opy_ (u"ࠪࡶࠬဂ")) as f:
      bstack1l1111l11l_opy_ = f.read()
    bstack1l1111l11l_opy_ = bstack1l1111l11l_opy_.replace(bstack11l111_opy_ (u"ࠫࢀࠫࡒࡆࡕࡘࡐ࡙࡙࡟ࡄࡑࡘࡒ࡙ࠫࡽࠨဃ"), str(len(sessions)))
    bstack1l1111l11l_opy_ = bstack1l1111l11l_opy_.replace(bstack11l111_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡕࡓࡎࠨࢁࠬင"), bstack11lllll111_opy_)
    bstack1l1111l11l_opy_ = bstack1l1111l11l_opy_.replace(bstack11l111_opy_ (u"࠭ࡻࠦࡄࡘࡍࡑࡊ࡟ࡏࡃࡐࡉࠪࢃࠧစ"),
                                              sessions[0].get(bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥ࡮ࡢ࡯ࡨࠫဆ")) if sessions[0] else bstack11l111_opy_ (u"ࠨࠩဇ"))
    with open(os.path.join(bstack111lll111_opy_, bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭ဈ")), bstack11l111_opy_ (u"ࠪࡻࠬဉ")) as stream:
      stream.write(bstack1l1111l11l_opy_.split(bstack11l111_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨည"))[0])
      for session in sessions:
        stream.write(bstack1ll1ll11l_opy_(session))
      stream.write(bstack1l1111l11l_opy_.split(bstack11l111_opy_ (u"ࠬࢁࠥࡔࡇࡖࡗࡎࡕࡎࡔࡡࡇࡅ࡙ࡇࠥࡾࠩဋ"))[1])
    logger.info(bstack11l111_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࡥࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡤࡸ࡭ࡱࡪࠠࡢࡴࡷ࡭࡫ࡧࡣࡵࡵࠣࡥࡹࠦࡻࡾࠩဌ").format(bstack111lll111_opy_));
  except Exception as e:
    logger.debug(bstack11l1l11ll_opy_.format(str(e)))
def bstack1l11l1111_opy_(hashed_id):
  global CONFIG
  try:
    bstack1lll1l1ll1_opy_ = datetime.datetime.now()
    host = bstack11l111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠲ࡩ࡬ࡰࡷࡧ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠧဍ") if bstack11l111_opy_ (u"ࠨࡣࡳࡴࠬဎ") in CONFIG else bstack11l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪဏ")
    user = CONFIG[bstack11l111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬတ")]
    key = CONFIG[bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧထ")]
    bstack1l1ll11ll_opy_ = bstack11l111_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫဒ") if bstack11l111_opy_ (u"࠭ࡡࡱࡲࠪဓ") in CONFIG else (bstack11l111_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫန") if CONFIG.get(bstack11l111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬပ")) else bstack11l111_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫဖ"))
    host = bstack111l11l1l_opy_(cli.config, [bstack11l111_opy_ (u"ࠥࡥࡵ࡯ࡳࠣဗ"), bstack11l111_opy_ (u"ࠦࡦࡶࡰࡂࡷࡷࡳࡲࡧࡴࡦࠤဘ"), bstack11l111_opy_ (u"ࠧࡧࡰࡪࠤမ")], host) if bstack11l111_opy_ (u"࠭ࡡࡱࡲࠪယ") in CONFIG else bstack111l11l1l_opy_(cli.config, [bstack11l111_opy_ (u"ࠢࡢࡲ࡬ࡷࠧရ"), bstack11l111_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࠥလ"), bstack11l111_opy_ (u"ࠤࡤࡴ࡮ࠨဝ")], host)
    url = bstack11l111_opy_ (u"ࠪࡿࢂ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠮࡫ࡵࡲࡲࠬသ").format(host, bstack1l1ll11ll_opy_, hashed_id)
    headers = {
      bstack11l111_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪဟ"): bstack11l111_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨဠ"),
    }
    proxies = bstack1llllll11l_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠨࡨࡵࡶࡳ࠾࡬࡫ࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࡢࡰ࡮ࡹࡴࠣအ"), datetime.datetime.now() - bstack1lll1l1ll1_opy_)
      return list(map(lambda session: session[bstack11l111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬဢ")], response.json()))
  except Exception as e:
    logger.debug(bstack1ll111l111_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack11ll111lll_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def get_build_link():
  global CONFIG
  global bstack1111ll111_opy_
  try:
    if bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫဣ") in CONFIG:
      bstack1lll1l1ll1_opy_ = datetime.datetime.now()
      host = bstack11l111_opy_ (u"ࠩࡤࡴ࡮࠳ࡣ࡭ࡱࡸࡨࠬဤ") if bstack11l111_opy_ (u"ࠪࡥࡵࡶࠧဥ") in CONFIG else bstack11l111_opy_ (u"ࠫࡦࡶࡩࠨဦ")
      user = CONFIG[bstack11l111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧဧ")]
      key = CONFIG[bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩဨ")]
      bstack1l1ll11ll_opy_ = bstack11l111_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ဩ") if bstack11l111_opy_ (u"ࠨࡣࡳࡴࠬဪ") in CONFIG else bstack11l111_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫါ")
      url = bstack11l111_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࢀࢃ࠺ࡼࡿࡃࡿࢂ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠳ࡰࡳࡰࡰࠪာ").format(user, key, host, bstack1l1ll11ll_opy_)
      if cli.is_enabled(CONFIG):
        bstack11lllll111_opy_, hashed_id = cli.bstack1l1l111lll_opy_()
        logger.info(bstack11lll11l11_opy_.format(bstack11lllll111_opy_))
        return [hashed_id, bstack11lllll111_opy_]
      else:
        headers = {
          bstack11l111_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪိ"): bstack11l111_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨီ"),
        }
        if bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨု") in CONFIG:
          params = {bstack11l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬူ"): CONFIG[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫေ")], bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬဲ"): CONFIG[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬဳ")]}
        else:
          params = {bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩဴ"): CONFIG[bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨဵ")]}
        proxies = bstack1llllll11l_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack1l1l1111l1_opy_ = response.json()[0][bstack11l111_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡦࡺ࡯࡬ࡥࠩံ")]
          if bstack1l1l1111l1_opy_:
            bstack11lllll111_opy_ = bstack1l1l1111l1_opy_[bstack11l111_opy_ (u"ࠧࡱࡷࡥࡰ࡮ࡩ࡟ࡶࡴ࡯့ࠫ")].split(bstack11l111_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣ࠮ࡤࡸ࡭ࡱࡪࠧး"))[0] + bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡴ࠱္ࠪ") + bstack1l1l1111l1_opy_[
              bstack11l111_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ်࠭")]
            logger.info(bstack11lll11l11_opy_.format(bstack11lllll111_opy_))
            bstack1111ll111_opy_ = bstack1l1l1111l1_opy_[bstack11l111_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧျ")]
            bstack11llll111_opy_ = CONFIG[bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨြ")]
            if bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨွ") in CONFIG:
              bstack11llll111_opy_ += bstack11l111_opy_ (u"ࠧࠡࠩှ") + CONFIG[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪဿ")]
            if bstack11llll111_opy_ != bstack1l1l1111l1_opy_[bstack11l111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ၀")]:
              logger.debug(bstack11l111111_opy_.format(bstack1l1l1111l1_opy_[bstack11l111_opy_ (u"ࠪࡲࡦࡳࡥࠨ၁")], bstack11llll111_opy_))
            cli.bstack1llll1l11l_opy_(bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡪࡩࡹࡥࡢࡶ࡫࡯ࡨࡤࡲࡩ࡯࡭ࠥ၂"), datetime.datetime.now() - bstack1lll1l1ll1_opy_)
            return [bstack1l1l1111l1_opy_[bstack11l111_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ၃")], bstack11lllll111_opy_]
    else:
      logger.warn(bstack1lll1lll11_opy_)
  except Exception as e:
    logger.debug(bstack1l1l11lll_opy_.format(str(e)))
  return [None, None]
def bstack1l11111l1l_opy_(url, bstack1lll11111_opy_=False):
  global CONFIG
  global bstack11ll1l1111_opy_
  if not bstack11ll1l1111_opy_:
    hostname = bstack1lllll1l1l_opy_(url)
    is_private = bstack1111ll1l11_opy_(hostname)
    if (bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪ၄") in CONFIG and not bstack11lll1lll_opy_(CONFIG[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ၅")])) and (is_private or bstack1lll11111_opy_):
      bstack11ll1l1111_opy_ = hostname
def bstack1lllll1l1l_opy_(url):
  return urlparse(url).hostname
def bstack1111ll1l11_opy_(hostname):
  for bstack11l11111l_opy_ in bstack1ll1l1ll1_opy_:
    regex = re.compile(bstack11l11111l_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack111l1ll1ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1ll111ll11_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack11l1llll1_opy_
  bstack1l1l1l1l1l_opy_ = not (bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ၆"), None) and bstack1l11lll1_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ၇"), None))
  bstack111ll11l1_opy_ = getattr(driver, bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ၈"), None) != True
  bstack1l1ll11l1_opy_ = bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫ၉"), None) and bstack1l11lll1_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ၊"), None)
  if bstack1l1ll11l1_opy_:
    if not bstack111lllll11_opy_():
      logger.warning(bstack11l111_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴ࠰ࠥ။"))
      return {}
    logger.debug(bstack11l111_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠫ၌"))
    logger.debug(perform_scan(driver, driver_command=bstack11l111_opy_ (u"ࠨࡧࡻࡩࡨࡻࡴࡦࡕࡦࡶ࡮ࡶࡴࠨ၍")))
    results = bstack111l11111_opy_(bstack11l111_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡵࠥ၎"))
    if results is not None and results.get(bstack11l111_opy_ (u"ࠥ࡭ࡸࡹࡵࡦࡵࠥ၏")) is not None:
        return results[bstack11l111_opy_ (u"ࠦ࡮ࡹࡳࡶࡧࡶࠦၐ")]
    logger.error(bstack11l111_opy_ (u"ࠧࡔ࡯ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡔࡨࡷࡺࡲࡴࡴࠢࡺࡩࡷ࡫ࠠࡧࡱࡸࡲࡩ࠴ࠢၑ"))
    return []
  if not bstack11l111l1_opy_.bstack1ll1l1l111_opy_(CONFIG, bstack11l1llll1_opy_) or (bstack111ll11l1_opy_ and bstack1l1l1l1l1l_opy_):
    logger.warning(bstack11l111_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤၒ"))
    return {}
  try:
    logger.debug(bstack11l111_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠫၓ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1l1l1ll111_opy_.bstack11l111111l_opy_)
    return results
  except Exception:
    logger.error(bstack11l111_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡽࡥࡳࡧࠣࡪࡴࡻ࡮ࡥ࠰ࠥၔ"))
    return {}
@measure(event_name=EVENTS.bstack1l11ll11l1_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack11l1llll1_opy_
  bstack1l1l1l1l1l_opy_ = not (bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ၕ"), None) and bstack1l11lll1_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩၖ"), None))
  bstack111ll11l1_opy_ = getattr(driver, bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫၗ"), None) != True
  bstack1l1ll11l1_opy_ = bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬၘ"), None) and bstack1l11lll1_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨၙ"), None)
  if bstack1l1ll11l1_opy_:
    if not bstack111lllll11_opy_():
      logger.warning(bstack11l111_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼ࠲ࠧၚ"))
      return {}
    logger.debug(bstack11l111_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠭ၛ"))
    logger.debug(perform_scan(driver, driver_command=bstack11l111_opy_ (u"ࠩࡨࡼࡪࡩࡵࡵࡧࡖࡧࡷ࡯ࡰࡵࠩၜ")))
    results = bstack111l11111_opy_(bstack11l111_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡖࡹࡲࡳࡡࡳࡻࠥၝ"))
    if results is not None and results.get(bstack11l111_opy_ (u"ࠦࡸࡻ࡭࡮ࡣࡵࡽࠧၞ")) is not None:
        return results[bstack11l111_opy_ (u"ࠧࡹࡵ࡮࡯ࡤࡶࡾࠨၟ")]
    logger.error(bstack11l111_opy_ (u"ࠨࡎࡰࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡕࡩࡸࡻ࡬ࡵࡵࠣࡗࡺࡳ࡭ࡢࡴࡼࠤࡼࡧࡳࠡࡨࡲࡹࡳࡪ࠮ࠣၠ"))
    return {}
  if not bstack11l111l1_opy_.bstack1ll1l1l111_opy_(CONFIG, bstack11l1llll1_opy_) or (bstack111ll11l1_opy_ and bstack1l1l1l1l1l_opy_):
    logger.warning(bstack11l111_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻ࠱ࠦၡ"))
    return {}
  try:
    logger.debug(bstack11l111_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠭ၢ"))
    logger.debug(perform_scan(driver))
    bstack11ll1111ll_opy_ = driver.execute_async_script(bstack1l1l1ll111_opy_.bstack1lllllll1l_opy_)
    return bstack11ll1111ll_opy_
  except Exception:
    logger.error(bstack11l111_opy_ (u"ࠤࡑࡳࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡵ࡮࡯ࡤࡶࡾࠦࡷࡢࡵࠣࡪࡴࡻ࡮ࡥ࠰ࠥၣ"))
    return {}
def bstack111lllll11_opy_():
  global CONFIG
  global bstack11l1llll1_opy_
  bstack1lll1111l1_opy_ = bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪၤ"), None) and bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ၥ"), None)
  if not bstack11l111l1_opy_.bstack1ll1l1l111_opy_(CONFIG, bstack11l1llll1_opy_) or not bstack1lll1111l1_opy_:
        logger.warning(bstack11l111_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡶࡪࡹࡵ࡭ࡶࡶ࠲ࠧၦ"))
        return False
  return True
def bstack111l11111_opy_(bstack1111l1ll11_opy_):
    bstack1111ll1l1_opy_ = bstack1lll1l1l_opy_.current_test_uuid() if bstack1lll1l1l_opy_.current_test_uuid() else bstack1l1l11l1_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack11l111l111_opy_(bstack1111ll1l1_opy_, bstack1111l1ll11_opy_))
        try:
            return future.result(timeout=bstack11ll111l11_opy_)
        except TimeoutError:
            logger.error(bstack11l111_opy_ (u"ࠨࡔࡪ࡯ࡨࡳࡺࡺࠠࡢࡨࡷࡩࡷࠦࡻࡾࡵࠣࡻ࡭࡯࡬ࡦࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡗ࡫ࡳࡶ࡮ࡷࡷࠧၧ").format(bstack11ll111l11_opy_))
        except Exception as ex:
            logger.debug(bstack11l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡲࡦࡶࡵ࡭ࡪࡼࡩ࡯ࡩࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࢀࢃ࠮ࠡࡇࡵࡶࡴࡸࠠ࠮ࠢࡾࢁࠧၨ").format(bstack1111l1ll11_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack111llll11l_opy_, stage=STAGE.bstack1l111l11l_opy_, bstack1l1l111l11_opy_=bstack1111llll11_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack11l1llll1_opy_
  bstack1l1l1l1l1l_opy_ = not (bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬၩ"), None) and bstack1l11lll1_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨၪ"), None))
  bstack1l11l1111l_opy_ = not (bstack1l11lll1_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪၫ"), None) and bstack1l11lll1_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ၬ"), None))
  bstack111ll11l1_opy_ = getattr(driver, bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬၭ"), None) != True
  if not bstack11l111l1_opy_.bstack1ll1l1l111_opy_(CONFIG, bstack11l1llll1_opy_) or (bstack111ll11l1_opy_ and bstack1l1l1l1l1l_opy_ and bstack1l11l1111l_opy_):
    logger.warning(bstack11l111_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡵ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡧࡦࡴ࠮ࠣၮ"))
    return {}
  try:
    bstack111l1l1111_opy_ = bstack11l111_opy_ (u"ࠧࡢࡲࡳࠫၯ") in CONFIG and CONFIG.get(bstack11l111_opy_ (u"ࠨࡣࡳࡴࠬၰ"), bstack11l111_opy_ (u"ࠩࠪၱ"))
    session_id = getattr(driver, bstack11l111_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧၲ"), None)
    if not session_id:
      logger.warning(bstack11l111_opy_ (u"ࠦࡓࡵࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡋࡇࠤ࡫ࡵࡵ࡯ࡦࠣࡪࡴࡸࠠࡥࡴ࡬ࡺࡪࡸࠢၳ"))
      return {bstack11l111_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦၴ"): bstack11l111_opy_ (u"ࠨࡎࡰࠢࡶࡩࡸࡹࡩࡰࡰࠣࡍࡉࠦࡦࡰࡷࡱࡨࠧၵ")}
    if bstack111l1l1111_opy_:
      try:
        bstack111l111l1l_opy_ = {
              bstack11l111_opy_ (u"ࠧࡵࡪࡍࡻࡹ࡚࡯࡬ࡧࡱࠫၶ"): os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭ၷ"), os.environ.get(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭ၸ"), bstack11l111_opy_ (u"ࠪࠫၹ"))),
              bstack11l111_opy_ (u"ࠫࡹ࡮ࡔࡦࡵࡷࡖࡺࡴࡕࡶ࡫ࡧࠫၺ"): bstack1lll1l1l_opy_.current_test_uuid() if bstack1lll1l1l_opy_.current_test_uuid() else bstack1l1l11l1_opy_.current_hook_uuid(),
              bstack11l111_opy_ (u"ࠬࡧࡵࡵࡪࡋࡩࡦࡪࡥࡳࠩၻ"): os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫၼ")),
              bstack11l111_opy_ (u"ࠧࡴࡥࡤࡲ࡙࡯࡭ࡦࡵࡷࡥࡲࡶࠧၽ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack11l111_opy_ (u"ࠨࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ၾ"): os.environ.get(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧၿ"), bstack11l111_opy_ (u"ࠪࠫႀ")),
              bstack11l111_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࠫႁ"): kwargs.get(bstack11l111_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤࡩ࡯࡮࡯ࡤࡲࡩ࠭ႂ"), None) or bstack11l111_opy_ (u"࠭ࠧႃ")
          }
        if not hasattr(thread_local, bstack11l111_opy_ (u"ࠧࡣࡣࡶࡩࡤࡧࡰࡱࡡࡤ࠵࠶ࡿ࡟ࡴࡥࡵ࡭ࡵࡺࠧႄ")):
            scripts = {bstack11l111_opy_ (u"ࠨࡵࡦࡥࡳ࠭ႅ"): bstack1l1l1ll111_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack1111l11ll_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack1111l11ll_opy_[bstack11l111_opy_ (u"ࠩࡶࡧࡦࡴࠧႆ")] = bstack1111l11ll_opy_[bstack11l111_opy_ (u"ࠪࡷࡨࡧ࡮ࠨႇ")] % json.dumps(bstack111l111l1l_opy_)
        bstack1l1l1ll111_opy_.bstack11ll11l1ll_opy_(bstack1111l11ll_opy_)
        bstack1l1l1ll111_opy_.store()
        bstack1ll111l1ll_opy_ = driver.execute_script(bstack1l1l1ll111_opy_.perform_scan)
      except Exception as bstack11l111ll1l_opy_:
        logger.info(bstack11l111_opy_ (u"ࠦࡆࡶࡰࡪࡷࡰࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡩࡡ࡯ࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࠦႈ") + str(bstack11l111ll1l_opy_))
        bstack1ll111l1ll_opy_ = {bstack11l111_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦႉ"): str(bstack11l111ll1l_opy_)}
    else:
      bstack1ll111l1ll_opy_ = driver.execute_async_script(bstack1l1l1ll111_opy_.perform_scan, {bstack11l111_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭ႊ"): kwargs.get(bstack11l111_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸ࡟ࡤࡱࡰࡱࡦࡴࡤࠨႋ"), None) or bstack11l111_opy_ (u"ࠨࠩႌ")})
    return bstack1ll111l1ll_opy_
  except Exception as err:
    logger.error(bstack11l111_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡸࡵ࡯ࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡧࡦࡴ࠮ࠡࡽࢀႍࠦ").format(str(err)))
    return {}