# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
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
from browserstack_sdk.bstack1lll111l1l_opy_ import bstack1ll1l111l1_opy_
from browserstack_sdk.bstack1lll111ll_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack1l11ll1lll_opy_():
  global CONFIG
  headers = {
        bstack1l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨਙ"): bstack1l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ਚ"),
      }
  proxies = bstack1111ll1lll_opy_(CONFIG, bstack1l11ll11l1_opy_)
  try:
    response = requests.get(bstack1l11ll11l1_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l11l111l1_opy_ = response.json()[bstack1l1_opy_ (u"ࠫ࡭ࡻࡢࡴࠩਛ")]
      logger.debug(bstack1l11lll11_opy_.format(response.json()))
      return bstack1l11l111l1_opy_
    else:
      logger.debug(bstack11111l1l1l_opy_.format(bstack1l1_opy_ (u"ࠧࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡋࡕࡒࡒࠥࡶࡡࡳࡵࡨࠤࡪࡸࡲࡰࡴࠣࠦਜ")))
  except Exception as e:
    logger.debug(bstack11111l1l1l_opy_.format(e))
def bstack11l11ll111_opy_(hub_url):
  global CONFIG
  url = bstack1l1_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣਝ")+  hub_url + bstack1l1_opy_ (u"ࠢ࠰ࡥ࡫ࡩࡨࡱࠢਞ")
  headers = {
        bstack1l1_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧਟ"): bstack1l1_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬਠ"),
      }
  proxies = bstack1111ll1lll_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11l1l1l1l1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack11l1l1ll11_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack1111l1lll1_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
def bstack1l1lllll11_opy_():
  try:
    global bstack111111ll11_opy_
    bstack1l11l111l1_opy_ = bstack1l11ll1lll_opy_()
    bstack1l111l1ll_opy_ = []
    results = []
    for bstack1l111ll1l1_opy_ in bstack1l11l111l1_opy_:
      bstack1l111l1ll_opy_.append(bstack11111111l_opy_(target=bstack11l11ll111_opy_,args=(bstack1l111ll1l1_opy_,)))
    for t in bstack1l111l1ll_opy_:
      t.start()
    for t in bstack1l111l1ll_opy_:
      results.append(t.join())
    bstack1l1l11l111_opy_ = {}
    for item in results:
      hub_url = item[bstack1l1_opy_ (u"ࠪ࡬ࡺࡨ࡟ࡶࡴ࡯ࠫਡ")]
      latency = item[bstack1l1_opy_ (u"ࠫࡱࡧࡴࡦࡰࡦࡽࠬਢ")]
      bstack1l1l11l111_opy_[hub_url] = latency
    bstack11l1lll111_opy_ = min(bstack1l1l11l111_opy_, key= lambda x: bstack1l1l11l111_opy_[x])
    bstack111111ll11_opy_ = bstack11l1lll111_opy_
    logger.debug(bstack1ll1l1ll1l_opy_.format(bstack11l1lll111_opy_))
  except Exception as e:
    logger.debug(bstack1l11ll1l1l_opy_.format(e))
from browserstack_sdk.bstack11111ll1_opy_ import *
from browserstack_sdk.bstack1111111l_opy_ import *
from browserstack_sdk.bstack11l111ll_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack1ll1111l1_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack111111llll_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
def bstack11l1111l11_opy_():
    global bstack111111ll11_opy_
    try:
        bstack11l1lllll_opy_ = bstack11l11lll11_opy_()
        bstack1l1l11ll1l_opy_(bstack11l1lllll_opy_)
        hub_url = bstack11l1lllll_opy_.get(bstack1l1_opy_ (u"ࠧࡻࡲ࡭ࠤਣ"), bstack1l1_opy_ (u"ࠨࠢਤ"))
        if hub_url.endswith(bstack1l1_opy_ (u"ࠧ࠰ࡹࡧ࠳࡭ࡻࡢࠨਥ")):
            hub_url = hub_url.rsplit(bstack1l1_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩਦ"), 1)[0]
        if hub_url.startswith(bstack1l1_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱ࠪਧ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠬਨ")):
            hub_url = hub_url[8:]
        bstack111111ll11_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack11l11lll11_opy_():
    global CONFIG
    bstack11ll1llll1_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ਩"), {}).get(bstack1l1_opy_ (u"ࠬ࡭ࡲࡪࡦࡑࡥࡲ࡫ࠧਪ"), bstack1l1_opy_ (u"࠭ࡎࡐࡡࡊࡖࡎࡊ࡟ࡏࡃࡐࡉࡤࡖࡁࡔࡕࡈࡈࠬਫ"))
    if not isinstance(bstack11ll1llll1_opy_, str):
        raise ValueError(bstack1l1_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡇࡳ࡫ࡧࠤࡳࡧ࡭ࡦࠢࡰࡹࡸࡺࠠࡣࡧࠣࡥࠥࡼࡡ࡭࡫ࡧࠤࡸࡺࡲࡪࡰࡪࠦਬ"))
    try:
        bstack11l1lllll_opy_ = bstack1lll111111_opy_(bstack11ll1llll1_opy_)
        return bstack11l1lllll_opy_
    except Exception as e:
        logger.error(bstack1l1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢਭ").format(str(e)))
        return {}
def bstack1lll111111_opy_(bstack11ll1llll1_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫਮ")] or not CONFIG[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ਯ")]:
            raise ValueError(bstack1l1_opy_ (u"ࠦࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡺࡹࡥࡳࡰࡤࡱࡪࠦ࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾࠨਰ"))
        url = bstack111lll111l_opy_ + bstack11ll1llll1_opy_
        auth = (CONFIG[bstack1l1_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ਱")], CONFIG[bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩਲ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack11llllll11_opy_ = json.loads(response.text)
            return bstack11llllll11_opy_
    except ValueError as ve:
        logger.error(bstack1l1_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢਲ਼").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack1l1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣ਴").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1l1l11ll1l_opy_(bstack11l1l1lll_opy_):
    global CONFIG
    if bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ਵ") not in CONFIG or str(CONFIG[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧਸ਼")]).lower() == bstack1l1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ਷"):
        CONFIG[bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫਸ")] = False
    elif bstack1l1_opy_ (u"࠭ࡩࡴࡖࡵ࡭ࡦࡲࡇࡳ࡫ࡧࠫਹ") in bstack11l1l1lll_opy_:
        bstack11llll11l1_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ਺"), {})
        logger.debug(bstack1l1_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡺ࡬ࡷࡹ࡯࡮ࡨࠢ࡯ࡳࡨࡧ࡬ࠡࡱࡳࡸ࡮ࡵ࡮ࡴ࠼ࠣࠩࡸࠨ਻"), bstack11llll11l1_opy_)
        bstack111lll11ll_opy_ = bstack11l1l1lll_opy_.get(bstack1l1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡔࡨࡴࡪࡧࡴࡦࡴࡶ਼ࠦ"), [])
        bstack111l11l1l1_opy_ = bstack1l1_opy_ (u"ࠥ࠰ࠧ਽").join(bstack111lll11ll_opy_)
        logger.debug(bstack1l1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡇࡺࡹࡴࡰ࡯ࠣࡶࡪࡶࡥࡢࡶࡨࡶࠥࡹࡴࡳ࡫ࡱ࡫࠿ࠦࠥࡴࠤਾ"), bstack111l11l1l1_opy_)
        bstack111l111ll1_opy_ = {
            bstack1l1_opy_ (u"ࠧࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢਿ"): bstack1l1_opy_ (u"ࠨࡡࡵࡵ࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧੀ"),
            bstack1l1_opy_ (u"ࠢࡧࡱࡵࡧࡪࡒ࡯ࡤࡣ࡯ࠦੁ"): bstack1l1_opy_ (u"ࠣࡶࡵࡹࡪࠨੂ"),
            bstack1l1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠦ੃"): bstack111l11l1l1_opy_
        }
        bstack11llll11l1_opy_.update(bstack111l111ll1_opy_)
        logger.debug(bstack1l1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡘࡴࡩࡧࡴࡦࡦࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢ੄"), bstack11llll11l1_opy_)
        CONFIG[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੅")] = bstack11llll11l1_opy_
        logger.debug(bstack1l1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡋ࡯࡮ࡢ࡮ࠣࡇࡔࡔࡆࡊࡉ࠽ࠤࠪࡹࠢ੆"), CONFIG)
def bstack111lll1ll_opy_():
    bstack11l1lllll_opy_ = bstack11l11lll11_opy_()
    if not bstack11l1lllll_opy_[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡘࡶࡱ࠭ੇ")]:
      raise ValueError(bstack1l1_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠠࡪࡵࠣࡱ࡮ࡹࡳࡪࡰࡪࠤ࡫ࡸ࡯࡮ࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳ࠯ࠤੈ"))
    return bstack11l1lllll_opy_[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠨ੉")] + bstack1l1_opy_ (u"ࠩࡂࡧࡦࡶࡳ࠾ࠩ੊")
@measure(event_name=EVENTS.bstack1l11ll1ll_opy_, stage=STAGE.bstack1lllll1l1l_opy_)
def bstack1llllll1l1_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack1l1_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬੋ")], CONFIG[bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧੌ")])
        url = bstack1111ll111_opy_
        logger.debug(bstack1l1_opy_ (u"ࠧࡇࡴࡵࡧࡰࡴࡹ࡯࡮ࡨࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶࠤ࡫ࡸ࡯࡮ࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡖࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠥࡇࡐࡊࠤ੍"))
        try:
            response = requests.get(url, auth=auth, headers={bstack1l1_opy_ (u"ࠨࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠧ੎"): bstack1l1_opy_ (u"ࠢࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠥ੏")})
            if response.status_code == 200:
                bstack11lll1l11_opy_ = json.loads(response.text)
                bstack1l11111ll_opy_ = bstack11lll1l11_opy_.get(bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡳࠨ੐"), [])
                if bstack1l11111ll_opy_:
                    bstack11llll1111_opy_ = bstack1l11111ll_opy_[0]
                    build_hashed_id = bstack11llll1111_opy_.get(bstack1l1_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬੑ"))
                    bstack1ll1111lll_opy_ = bstack1l1ll1ll1_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1ll1111lll_opy_])
                    logger.info(bstack1l1l1ll1l_opy_.format(bstack1ll1111lll_opy_))
                    bstack11llllllll_opy_ = CONFIG[bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭੒")]
                    if bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੓") in CONFIG:
                      bstack11llllllll_opy_ += bstack1l1_opy_ (u"ࠬࠦࠧ੔") + CONFIG[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ੕")]
                    if bstack11llllllll_opy_ != bstack11llll1111_opy_.get(bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ੖")):
                      logger.debug(bstack1l11l1l1l_opy_.format(bstack11llll1111_opy_.get(bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭੗")), bstack11llllllll_opy_))
                    return result
                else:
                    logger.debug(bstack1l1_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡐࡲࠤࡧࡻࡩ࡭ࡦࡶࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡴࡩࡧࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠳ࠨ੘"))
            else:
                logger.debug(bstack1l1_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶ࠲ࠧਖ਼"))
        except Exception as e:
            logger.error(bstack1l1_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࡸࠦ࠺ࠡࡽࢀࠦਗ਼").format(str(e)))
    else:
        logger.debug(bstack1l1_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡕࡎࡇࡋࡊࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡸ࡫ࡴ࠯ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶ࠲ࠧਜ਼"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1llllll1ll_opy_ import bstack1llllll1ll_opy_, Events, bstack1l11l1111_opy_, bstack11llll111l_opy_
from bstack_utils.measure import bstack111l11l11_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack111l111lll_opy_ import bstack1lll1l11l1_opy_
from bstack_utils.messages import *
from bstack_utils import bstack1ll1111l1_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack111ll1111l_opy_, bstack1lll1l1l11_opy_, bstack11ll11llll_opy_, bstack11lll111_opy_, \
  bstack1lllllll11_opy_, \
  Notset, bstack1l1ll1l11l_opy_, \
  bstack11l1ll1111_opy_, bstack1ll1l1l111_opy_, bstack1l1l1l1ll1_opy_, bstack1ll11llll_opy_, bstack1l11l11ll_opy_, bstack1l111l11ll_opy_, \
  bstack1l11lll1l1_opy_, \
  bstack1l1l1l11l1_opy_, bstack1l1111l11l_opy_, bstack1l1l111l1l_opy_, bstack11l1ll11l_opy_, \
  bstack1111llllll_opy_, bstack1ll1ll1l1l_opy_, bstack1ll1111ll1_opy_, bstack111l1l1l11_opy_
from bstack_utils.bstack11l11l111l_opy_ import bstack11ll1ll1ll_opy_
from bstack_utils.bstack1ll1l111l_opy_ import bstack111lll1l11_opy_, bstack1l11llll1l_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack1l111l11l_opy_
from bstack_utils.bstack1l11l1llll_opy_ import bstack1l1ll11l11_opy_, bstack1ll1ll1l11_opy_
from bstack_utils.bstack11l1111ll_opy_ import bstack11l1111ll_opy_
from bstack_utils.bstack11lll11l1l_opy_ import bstack111l1ll111_opy_
from bstack_utils.proxy import bstack111l1ll1l_opy_, bstack1111ll1lll_opy_, bstack1l1l11lll1_opy_, bstack1l11l1lll1_opy_
from bstack_utils.bstack1l1l1l1ll_opy_ import bstack111111ll1_opy_
import bstack_utils.bstack1ll1ll111_opy_ as bstack1l111l111_opy_
import bstack_utils.bstack11l1ll11ll_opy_ as bstack11l111ll1_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack111llll11l_opy_ import bstack1111lll1l_opy_
from bstack_utils.bstack1111ll11_opy_ import bstack111lll1l_opy_
from bstack_utils.bstack11lll11l1_opy_ import bstack11l1ll1l1l_opy_
if os.getenv(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡋࡓࡔࡑࡓࠨੜ")):
  cli.bstack1111l1ll1_opy_()
else:
  os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡌࡔࡕࡋࡔࠩ੝")] = bstack1l1_opy_ (u"ࠨࡶࡵࡹࡪ࠭ਫ਼")
bstack111l1111l1_opy_ = bstack1l1_opy_ (u"ࠩࠣࠤ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࠢࠣ࡭࡫࠮ࡰࡢࡩࡨࠤࡂࡃ࠽ࠡࡸࡲ࡭ࡩࠦ࠰ࠪࠢࡾࡠࡳࠦࠠࠡࡶࡵࡽࢀࡢ࡮ࠡࡥࡲࡲࡸࡺࠠࡧࡵࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮࡜ࠨࡨࡶࡠࠬ࠯࠻࡝ࡰࠣࠤࠥࠦࠠࡧࡵ࠱ࡥࡵࡶࡥ࡯ࡦࡉ࡭ࡱ࡫ࡓࡺࡰࡦࠬࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩ࠮ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡵࡥࡩ࡯ࡦࡨࡼ࠮ࠦࠫࠡࠤ࠽ࠦࠥ࠱ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭࠮ࡡࡸࡣ࡬ࡸࠥࡴࡥࡸࡒࡤ࡫ࡪ࠸࠮ࡦࡸࡤࡰࡺࡧࡴࡦࠪࠥࠬ࠮ࠦ࠽࠿ࠢࡾࢁࠧ࠲ࠠ࡝ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡪࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡥࡵࡣ࡬ࡰࡸࠨࡽ࡝ࠩࠬ࠭࠮ࡡࠢࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠥࡡ࠮ࠦࠫࠡࠤ࠯ࡠࡡࡴࠢࠪ࡞ࡱࠤࠥࠦࠠࡾࡥࡤࡸࡨ࡮ࠨࡦࡺࠬࡿࡡࡴࠠࠡࠢࠣࢁࡡࡴࠠࠡࡿ࡟ࡲࠥࠦ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠩ੟")
bstack1l11lll1ll_opy_ = bstack1l1_opy_ (u"ࠪࡠࡳ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭ࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠶ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡱࡡ࡬ࡲࡩ࡫ࡸࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠶ࡢࡢ࡮ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮ࡴ࡮࡬ࡧࡪ࠮࠰࠭ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷࠮ࡢ࡮ࡤࡱࡱࡷࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮ࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ࠯࠻࡝ࡰ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰࡯ࡥࡺࡴࡣࡩࠢࡀࠤࡦࡹࡹ࡯ࡥࠣࠬࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶ࠭ࠥࡃ࠾ࠡࡽ࡟ࡲࡱ࡫ࡴࠡࡥࡤࡴࡸࡁ࡜࡯ࡶࡵࡽࠥࢁ࡜࡯ࡥࡤࡴࡸࠦ࠽ࠡࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠬࡠࡳࠦࠠࡾࠢࡦࡥࡹࡩࡨࠩࡧࡻ࠭ࠥࢁ࡜࡯ࠢࠣࠤࠥࢃ࡜࡯ࠢࠣࡶࡪࡺࡵࡳࡰࠣࡥࡼࡧࡩࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰ࡦࡳࡳࡴࡥࡤࡶࠫࡿࡡࡴࠠࠡࠢࠣࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺ࠺ࠡࡢࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠨࢀ࡫࡮ࡤࡱࡧࡩ࡚ࡘࡉࡄࡱࡰࡴࡴࡴࡥ࡯ࡶࠫࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡨࡧࡰࡴࠫࠬࢁࡥ࠲࡜࡯ࠢࠣࠤࠥ࠴࠮࠯࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳ࡝ࡰࠣࠤࢂ࠯࡜࡯ࡿ࡟ࡲ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࠩ੠")
from ._version import __version__
bstack1111l11lll_opy_ = None
CONFIG = {}
bstack1lll11111_opy_ = {}
bstack1ll11l1l1l_opy_ = {}
bstack11lll111l_opy_ = None
bstack1l11l1l11l_opy_ = None
bstack1l1l111ll1_opy_ = None
bstack1l1l11l1l_opy_ = -1
bstack11l1l111l_opy_ = 0
bstack11ll1l1lll_opy_ = bstack1l1ll111ll_opy_
bstack11lllllll1_opy_ = 1
bstack1l111ll111_opy_ = False
bstack1l1l1l11ll_opy_ = False
bstack1l1l11l11l_opy_ = bstack1l1_opy_ (u"ࠫࠬ੡")
bstack1l11lll1l_opy_ = bstack1l1_opy_ (u"ࠬ࠭੢")
bstack11l11ll1ll_opy_ = False
bstack1ll11ll1ll_opy_ = True
bstack11l1l1lll1_opy_ = bstack1l1_opy_ (u"࠭ࠧ੣")
bstack11lll11ll_opy_ = []
bstack11l1l111l1_opy_ = threading.Lock()
bstack1l111lll1_opy_ = threading.Lock()
bstack111111ll11_opy_ = bstack1l1_opy_ (u"ࠧࠨ੤")
bstack1111lll11l_opy_ = False
bstack11l11l1lll_opy_ = None
bstack1111ll1l1_opy_ = None
bstack1l111l111l_opy_ = None
bstack111lll1l1_opy_ = -1
bstack1111l111l1_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠨࢀࠪ੥")), bstack1l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ੦"), bstack1l1_opy_ (u"ࠪ࠲ࡷࡵࡢࡰࡶ࠰ࡶࡪࡶ࡯ࡳࡶ࠰࡬ࡪࡲࡰࡦࡴ࠱࡮ࡸࡵ࡮ࠨ੧"))
bstack11l111l11_opy_ = 0
bstack1ll1l1lll_opy_ = 0
bstack1ll11l11l1_opy_ = []
bstack11lllll11_opy_ = []
bstack1ll1l111ll_opy_ = []
bstack11ll11ll11_opy_ = []
bstack1ll111111_opy_ = bstack1l1_opy_ (u"ࠫࠬ੨")
bstack11lll1l1l1_opy_ = bstack1l1_opy_ (u"ࠬ࠭੩")
bstack1111llll11_opy_ = False
bstack11ll1l1l1l_opy_ = False
bstack1ll1ll1lll_opy_ = {}
bstack1ll1lll1l1_opy_ = None
bstack1111l1111l_opy_ = None
bstack1l1l111ll_opy_ = None
bstack11111ll1ll_opy_ = None
bstack1l1l1ll11l_opy_ = None
bstack11111l1l11_opy_ = None
bstack1ll1l1l1l_opy_ = None
bstack1ll1ll111l_opy_ = None
bstack11l1ll111l_opy_ = None
bstack1l111111ll_opy_ = None
bstack1lll11l11l_opy_ = None
bstack1ll1l11ll1_opy_ = None
bstack1l1lll11l_opy_ = None
bstack1llll1l1l1_opy_ = None
bstack1ll11l111_opy_ = None
bstack111ll11ll1_opy_ = None
bstack1l1111lll_opy_ = None
bstack1l1lllll1l_opy_ = None
bstack1111l1lll_opy_ = None
bstack11ll1ll11l_opy_ = None
bstack11lll1l111_opy_ = None
bstack1l1llll111_opy_ = None
bstack1l1ll1lll1_opy_ = None
thread_local = threading.local()
bstack111l11ll11_opy_ = False
bstack1ll1l1l1l1_opy_ = bstack1l1_opy_ (u"ࠨࠢ੪")
logger = bstack1ll1111l1_opy_.get_logger(__name__, bstack11ll1l1lll_opy_)
bstack11l11111_opy_ = Config.bstack1111ll1l_opy_()
percy = bstack111llll1l_opy_()
bstack1l11lllll_opy_ = bstack1lll1l11l1_opy_()
bstack111l1llll1_opy_ = bstack11l111ll_opy_()
def bstack1ll11llll1_opy_():
  global CONFIG
  global bstack1111llll11_opy_
  global bstack11l11111_opy_
  testContextOptions = bstack1ll11111l1_opy_(CONFIG)
  if bstack1lllllll11_opy_(CONFIG):
    if (bstack1l1_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ੫") in testContextOptions and str(testContextOptions[bstack1l1_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ੬")]).lower() == bstack1l1_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ੭")):
      bstack1111llll11_opy_ = True
    bstack11l11111_opy_.bstack1ll111ll1_opy_(testContextOptions.get(bstack1l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ੮"), False))
  else:
    bstack1111llll11_opy_ = True
    bstack11l11111_opy_.bstack1ll111ll1_opy_(True)
def bstack111ll11lll_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11llll111_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack11l111ll1l_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1l1_opy_ (u"ࠦ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡨࡵ࡮ࡧ࡫ࡪࡪ࡮ࡲࡥࠣ੯") == args[i].lower() or bstack1l1_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡩ࡭࡬ࠨੰ") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack11l1l1lll1_opy_
      bstack11l1l1lll1_opy_ += bstack1l1_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡃࡰࡰࡩ࡭࡬ࡌࡩ࡭ࡧࠣࠫੱ") + shlex.quote(path)
      return path
  return None
bstack1l1l1llll1_opy_ = re.compile(bstack1l1_opy_ (u"ࡲࠣ࠰࠭ࡃࡡࠪࡻࠩ࠰࠭ࡃ࠮ࢃ࠮ࠫࡁࠥੲ"))
def bstack111l11ll1l_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l1l1llll1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1l1_opy_ (u"ࠣࠦࡾࠦੳ") + group + bstack1l1_opy_ (u"ࠤࢀࠦੴ"), os.environ.get(group))
  return value
def bstack11l11lll1l_opy_():
  global bstack1l1ll1lll1_opy_
  if bstack1l1ll1lll1_opy_ is None:
        bstack1l1ll1lll1_opy_ = bstack11l111ll1l_opy_()
  bstack111lll11l1_opy_ = bstack1l1ll1lll1_opy_
  if bstack111lll11l1_opy_ and os.path.exists(os.path.abspath(bstack111lll11l1_opy_)):
    fileName = bstack111lll11l1_opy_
  if bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧੵ") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ੶")])) and not bstack1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡑࡥࡲ࡫ࠧ੷") in locals():
    fileName = os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࡤࡌࡉࡍࡇࠪ੸")]
  if bstack1l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡓࡧ࡭ࡦࠩ੹") in locals():
    bstack11l111l_opy_ = os.path.abspath(fileName)
  else:
    bstack11l111l_opy_ = bstack1l1_opy_ (u"ࠨࠩ੺")
  bstack111ll1l11_opy_ = os.getcwd()
  bstack1111l1l1l1_opy_ = bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬ੻")
  bstack11111l111_opy_ = bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡥࡲࡲࠧ੼")
  while (not os.path.exists(bstack11l111l_opy_)) and bstack111ll1l11_opy_ != bstack1l1_opy_ (u"ࠦࠧ੽"):
    bstack11l111l_opy_ = os.path.join(bstack111ll1l11_opy_, bstack1111l1l1l1_opy_)
    if not os.path.exists(bstack11l111l_opy_):
      bstack11l111l_opy_ = os.path.join(bstack111ll1l11_opy_, bstack11111l111_opy_)
    if bstack111ll1l11_opy_ != os.path.dirname(bstack111ll1l11_opy_):
      bstack111ll1l11_opy_ = os.path.dirname(bstack111ll1l11_opy_)
    else:
      bstack111ll1l11_opy_ = bstack1l1_opy_ (u"ࠧࠨ੾")
  bstack1l1ll1lll1_opy_ = bstack11l111l_opy_ if os.path.exists(bstack11l111l_opy_) else None
  return bstack1l1ll1lll1_opy_
def bstack1111111ll_opy_(config):
    if bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬࠭੿") in config:
      config[bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ઀")] = config[bstack1l1_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࠨઁ")]
    if bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࡑࡳࡸ࡮ࡵ࡮ࡴࠩં") in config:
      config[bstack1l1_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧઃ")] = config[bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࡓࡵࡺࡩࡰࡰࡶࠫ઄")]
def bstack111l1ll11_opy_():
  bstack11l111l_opy_ = bstack11l11lll1l_opy_()
  if not os.path.exists(bstack11l111l_opy_):
    bstack1ll1llll1l_opy_(
      bstack11lll11ll1_opy_.format(os.getcwd()))
  try:
    with open(bstack11l111l_opy_, bstack1l1_opy_ (u"ࠬࡸࠧઅ")) as stream:
      yaml.add_implicit_resolver(bstack1l1_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢઆ"), bstack1l1l1llll1_opy_)
      yaml.add_constructor(bstack1l1_opy_ (u"ࠢࠢࡲࡤࡸ࡭࡫ࡸࠣઇ"), bstack111l11ll1l_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1111111ll_opy_(config)
      return config
  except:
    with open(bstack11l111l_opy_, bstack1l1_opy_ (u"ࠨࡴࠪઈ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1111111ll_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1ll1llll1l_opy_(bstack11ll111l11_opy_.format(str(exc)))
def bstack1lllllllll_opy_(config):
  bstack1111ll1ll1_opy_ = bstack1l1l1l1l1l_opy_(config)
  for option in list(bstack1111ll1ll1_opy_):
    if option.lower() in bstack1111l1ll11_opy_ and option != bstack1111l1ll11_opy_[option.lower()]:
      bstack1111ll1ll1_opy_[bstack1111l1ll11_opy_[option.lower()]] = bstack1111ll1ll1_opy_[option]
      del bstack1111ll1ll1_opy_[option]
  return config
def bstack11111ll1l1_opy_():
  global bstack1ll11l1l1l_opy_
  for key, bstack1ll111lll1_opy_ in bstack111111111_opy_.items():
    if isinstance(bstack1ll111lll1_opy_, list):
      for var in bstack1ll111lll1_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1ll11l1l1l_opy_[key] = os.environ[var]
          break
    elif bstack1ll111lll1_opy_ in os.environ and os.environ[bstack1ll111lll1_opy_] and str(os.environ[bstack1ll111lll1_opy_]).strip():
      bstack1ll11l1l1l_opy_[key] = os.environ[bstack1ll111lll1_opy_]
  if bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫઉ") in os.environ:
    bstack1ll11l1l1l_opy_[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઊ")] = {}
    bstack1ll11l1l1l_opy_[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨઋ")][bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઌ")] = os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨઍ")]
def bstack1lllllll1l_opy_():
  global bstack1lll11111_opy_
  global bstack11l1l1lll1_opy_
  bstack11lll11lll_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack1l1_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ઎").lower() == val.lower():
      bstack1lll11111_opy_[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬએ")] = {}
      bstack1lll11111_opy_[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઐ")][bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬઑ")] = sys.argv[idx + 1]
      bstack11lll11lll_opy_.extend([idx, idx + 1])
      break
  for key, bstack111llll11_opy_ in bstack11llllll1l_opy_.items():
    if isinstance(bstack111llll11_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack111llll11_opy_:
          if bstack1l1_opy_ (u"ࠫ࠲࠳ࠧ઒") + var.lower() == val.lower() and key not in bstack1lll11111_opy_:
            bstack1lll11111_opy_[key] = sys.argv[idx + 1]
            bstack11l1l1lll1_opy_ += bstack1l1_opy_ (u"ࠬࠦ࠭࠮ࠩઓ") + var + bstack1l1_opy_ (u"࠭ࠠࠨઔ") + shlex.quote(sys.argv[idx + 1])
            bstack11lll11lll_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack1l1_opy_ (u"ࠧ࠮࠯ࠪક") + bstack111llll11_opy_.lower() == val.lower() and key not in bstack1lll11111_opy_:
          bstack1lll11111_opy_[key] = sys.argv[idx + 1]
          bstack11l1l1lll1_opy_ += bstack1l1_opy_ (u"ࠨࠢ࠰࠱ࠬખ") + bstack111llll11_opy_ + bstack1l1_opy_ (u"ࠩࠣࠫગ") + shlex.quote(sys.argv[idx + 1])
          bstack11lll11lll_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack11lll11lll_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack1l11l11ll1_opy_(config):
  bstack1ll11ll11l_opy_ = config.keys()
  for bstack111ll111l_opy_, bstack1l11ll1l11_opy_ in bstack1111llll1l_opy_.items():
    if bstack1l11ll1l11_opy_ in bstack1ll11ll11l_opy_:
      config[bstack111ll111l_opy_] = config[bstack1l11ll1l11_opy_]
      del config[bstack1l11ll1l11_opy_]
  for bstack111ll111l_opy_, bstack1l11ll1l11_opy_ in bstack1l11lllll1_opy_.items():
    if isinstance(bstack1l11ll1l11_opy_, list):
      for bstack111111ll1l_opy_ in bstack1l11ll1l11_opy_:
        if bstack111111ll1l_opy_ in bstack1ll11ll11l_opy_:
          config[bstack111ll111l_opy_] = config[bstack111111ll1l_opy_]
          del config[bstack111111ll1l_opy_]
          break
    elif bstack1l11ll1l11_opy_ in bstack1ll11ll11l_opy_:
      config[bstack111ll111l_opy_] = config[bstack1l11ll1l11_opy_]
      del config[bstack1l11ll1l11_opy_]
  for bstack111111ll1l_opy_ in list(config):
    for bstack1l1lll111_opy_ in bstack1ll1l11lll_opy_:
      if bstack111111ll1l_opy_.lower() == bstack1l1lll111_opy_.lower() and bstack111111ll1l_opy_ != bstack1l1lll111_opy_:
        config[bstack1l1lll111_opy_] = config[bstack111111ll1l_opy_]
        del config[bstack111111ll1l_opy_]
  bstack111l111111_opy_ = [{}]
  if not config.get(bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ઘ")):
    config[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧઙ")] = [{}]
  bstack111l111111_opy_ = config[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨચ")]
  for platform in bstack111l111111_opy_:
    for bstack111111ll1l_opy_ in list(platform):
      for bstack1l1lll111_opy_ in bstack1ll1l11lll_opy_:
        if bstack111111ll1l_opy_.lower() == bstack1l1lll111_opy_.lower() and bstack111111ll1l_opy_ != bstack1l1lll111_opy_:
          platform[bstack1l1lll111_opy_] = platform[bstack111111ll1l_opy_]
          del platform[bstack111111ll1l_opy_]
  for bstack111ll111l_opy_, bstack1l11ll1l11_opy_ in bstack1l11lllll1_opy_.items():
    for platform in bstack111l111111_opy_:
      if isinstance(bstack1l11ll1l11_opy_, list):
        for bstack111111ll1l_opy_ in bstack1l11ll1l11_opy_:
          if bstack111111ll1l_opy_ in platform:
            platform[bstack111ll111l_opy_] = platform[bstack111111ll1l_opy_]
            del platform[bstack111111ll1l_opy_]
            break
      elif bstack1l11ll1l11_opy_ in platform:
        platform[bstack111ll111l_opy_] = platform[bstack1l11ll1l11_opy_]
        del platform[bstack1l11ll1l11_opy_]
  for bstack11ll1ll11_opy_ in bstack1l1l1l1lll_opy_:
    if bstack11ll1ll11_opy_ in config:
      if not bstack1l1l1l1lll_opy_[bstack11ll1ll11_opy_] in config:
        config[bstack1l1l1l1lll_opy_[bstack11ll1ll11_opy_]] = {}
      config[bstack1l1l1l1lll_opy_[bstack11ll1ll11_opy_]].update(config[bstack11ll1ll11_opy_])
      del config[bstack11ll1ll11_opy_]
  for platform in bstack111l111111_opy_:
    for bstack11ll1ll11_opy_ in bstack1l1l1l1lll_opy_:
      if bstack11ll1ll11_opy_ in list(platform):
        if not bstack1l1l1l1lll_opy_[bstack11ll1ll11_opy_] in platform:
          platform[bstack1l1l1l1lll_opy_[bstack11ll1ll11_opy_]] = {}
        platform[bstack1l1l1l1lll_opy_[bstack11ll1ll11_opy_]].update(platform[bstack11ll1ll11_opy_])
        del platform[bstack11ll1ll11_opy_]
  config = bstack1lllllllll_opy_(config)
  return config
def bstack1lllll1lll_opy_(config):
  global bstack1l11lll1l_opy_
  bstack1ll11lll11_opy_ = False
  if bstack1l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪછ") in config and str(config[bstack1l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫજ")]).lower() != bstack1l1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧઝ"):
    if bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ઞ") not in config or str(config[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧટ")]).lower() == bstack1l1_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪઠ"):
      config[bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫડ")] = False
    else:
      bstack11l1lllll_opy_ = bstack11l11lll11_opy_()
      if bstack1l1_opy_ (u"࠭ࡩࡴࡖࡵ࡭ࡦࡲࡇࡳ࡫ࡧࠫઢ") in bstack11l1lllll_opy_:
        if not bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫણ") in config:
          config[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬત")] = {}
        config[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭થ")][bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬદ")] = bstack1l1_opy_ (u"ࠫࡦࡺࡳ࠮ࡴࡨࡴࡪࡧࡴࡦࡴࠪધ")
        bstack1ll11lll11_opy_ = True
        bstack1l11lll1l_opy_ = config[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩન")].get(bstack1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ઩"))
  if bstack1lllllll11_opy_(config) and bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫપ") in config and str(config[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬફ")]).lower() != bstack1l1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨબ") and not bstack1ll11lll11_opy_:
    if not bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧભ") in config:
      config[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨમ")] = {}
    if not config[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩય")].get(bstack1l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠪર")) and not bstack1l1_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઱") in config[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬલ")]:
      bstack1l1ll11l_opy_ = datetime.datetime.now()
      bstack1l1111111_opy_ = bstack1l1ll11l_opy_.strftime(bstack1l1_opy_ (u"ࠩࠨࡨࡤࠫࡢࡠࠧࡋࠩࡒ࠭ળ"))
      hostname = socket.gethostname()
      bstack1l1l111l11_opy_ = bstack1l1_opy_ (u"ࠪࠫ઴").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1l1_opy_ (u"ࠫࢀࢃ࡟ࡼࡿࡢࡿࢂ࠭વ").format(bstack1l1111111_opy_, hostname, bstack1l1l111l11_opy_)
      config[bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩશ")][bstack1l1_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨષ")] = identifier
    bstack1l11lll1l_opy_ = config[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫસ")].get(bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪહ"))
  return config
def bstack111ll111ll_opy_():
  bstack1l111llll1_opy_ =  bstack1ll11llll_opy_()[bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠨ઺")]
  return bstack1l111llll1_opy_ if bstack1l111llll1_opy_ else -1
def bstack1ll1l11l11_opy_(bstack1l111llll1_opy_):
  global CONFIG
  if not bstack1l1_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬ઻") in CONFIG[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ઼࠭")]:
    return
  CONFIG[bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઽ")] = CONFIG[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨા")].replace(
    bstack1l1_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩિ"),
    str(bstack1l111llll1_opy_)
  )
def bstack11llll1ll_opy_():
  global CONFIG
  if not bstack1l1_opy_ (u"ࠨࠦࡾࡈࡆ࡚ࡅࡠࡖࡌࡑࡊࢃࠧી") in CONFIG[bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫુ")]:
    return
  bstack1l1ll11l_opy_ = datetime.datetime.now()
  bstack1l1111111_opy_ = bstack1l1ll11l_opy_.strftime(bstack1l1_opy_ (u"ࠪࠩࡩ࠳ࠥࡣ࠯ࠨࡌ࠿ࠫࡍࠨૂ"))
  CONFIG[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ૃ")] = CONFIG[bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૄ")].replace(
    bstack1l1_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬૅ"),
    bstack1l1111111_opy_
  )
def bstack1lll11ll11_opy_():
  global CONFIG
  if bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૆") in CONFIG and not bool(CONFIG[bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪે")]):
    del CONFIG[bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫૈ")]
    return
  if not bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૉ") in CONFIG:
    CONFIG[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૊")] = bstack1l1_opy_ (u"ࠬࠩࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨો")
  if bstack1l1_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬૌ") in CONFIG[bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳ્ࠩ")]:
    bstack11llll1ll_opy_()
    os.environ[bstack1l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ૎")] = CONFIG[bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૏")]
  if not bstack1l1_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬૐ") in CONFIG[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૑")]:
    return
  bstack1l111llll1_opy_ = bstack1l1_opy_ (u"ࠬ࠭૒")
  bstack1ll1ll11ll_opy_ = bstack111ll111ll_opy_()
  if bstack1ll1ll11ll_opy_ != -1:
    bstack1l111llll1_opy_ = bstack1l1_opy_ (u"࠭ࡃࡊࠢࠪ૓") + str(bstack1ll1ll11ll_opy_)
  if bstack1l111llll1_opy_ == bstack1l1_opy_ (u"ࠧࠨ૔"):
    bstack1l1ll1l111_opy_ = bstack1l1ll1111l_opy_(CONFIG[bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ૕")])
    if bstack1l1ll1l111_opy_ != -1:
      bstack1l111llll1_opy_ = str(bstack1l1ll1l111_opy_)
  if bstack1l111llll1_opy_:
    bstack1ll1l11l11_opy_(bstack1l111llll1_opy_)
    os.environ[bstack1l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭૖")] = CONFIG[bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૗")]
def bstack1l1111l111_opy_(bstack1lll1lll11_opy_, bstack111l11ll1_opy_, path):
  json_data = {
    bstack1l1_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૘"): bstack111l11ll1_opy_
  }
  if os.path.exists(path):
    bstack11l11ll1l1_opy_ = json.load(open(path, bstack1l1_opy_ (u"ࠬࡸࡢࠨ૙")))
  else:
    bstack11l11ll1l1_opy_ = {}
  bstack11l11ll1l1_opy_[bstack1lll1lll11_opy_] = json_data
  with open(path, bstack1l1_opy_ (u"ࠨࡷࠬࠤ૚")) as outfile:
    json.dump(bstack11l11ll1l1_opy_, outfile)
def bstack1l1ll1111l_opy_(bstack1lll1lll11_opy_):
  bstack1lll1lll11_opy_ = str(bstack1lll1lll11_opy_)
  bstack1l1ll1ll1l_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠧࡿࠩ૛")), bstack1l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ૜"))
  try:
    if not os.path.exists(bstack1l1ll1ll1l_opy_):
      os.makedirs(bstack1l1ll1ll1l_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠩࢁࠫ૝")), bstack1l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ૞"), bstack1l1_opy_ (u"ࠫ࠳ࡨࡵࡪ࡮ࡧ࠱ࡳࡧ࡭ࡦ࠯ࡦࡥࡨ࡮ࡥ࠯࡬ࡶࡳࡳ࠭૟"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1l1_opy_ (u"ࠬࡽࠧૠ")):
        pass
      with open(file_path, bstack1l1_opy_ (u"ࠨࡷࠬࠤૡ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1l1_opy_ (u"ࠧࡳࠩૢ")) as bstack11llll1l1l_opy_:
      bstack11l11l1ll1_opy_ = json.load(bstack11llll1l1l_opy_)
    if bstack1lll1lll11_opy_ in bstack11l11l1ll1_opy_:
      bstack11l111l1ll_opy_ = bstack11l11l1ll1_opy_[bstack1lll1lll11_opy_][bstack1l1_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૣ")]
      bstack111l111l1_opy_ = int(bstack11l111l1ll_opy_) + 1
      bstack1l1111l111_opy_(bstack1lll1lll11_opy_, bstack111l111l1_opy_, file_path)
      return bstack111l111l1_opy_
    else:
      bstack1l1111l111_opy_(bstack1lll1lll11_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack111lllll11_opy_.format(str(e)))
    return -1
def bstack1111ll11ll_opy_(config):
  if not config[bstack1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ૤")] or not config[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭૥")]:
    return True
  else:
    return False
def bstack1ll1lll1l_opy_(config, index=0):
  global bstack11l11ll1ll_opy_
  bstack1l1lllll1_opy_ = {}
  caps = bstack11l1llll11_opy_ + bstack1lll11ll1l_opy_
  if config.get(bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ૦"), False):
    bstack1l1lllll1_opy_[bstack1l1_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ૧")] = True
    bstack1l1lllll1_opy_[bstack1l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ૨")] = config.get(bstack1l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ૩"), {})
  if bstack11l11ll1ll_opy_:
    caps += bstack1l1l11l1l1_opy_
  for key in config:
    if key in caps + [bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૪")]:
      continue
    bstack1l1lllll1_opy_[key] = config[key]
  if bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૫") in config:
    for bstack1l1111lll1_opy_ in config[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૬")][index]:
      if bstack1l1111lll1_opy_ in caps:
        continue
      bstack1l1lllll1_opy_[bstack1l1111lll1_opy_] = config[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૭")][index][bstack1l1111lll1_opy_]
  bstack1l1lllll1_opy_[bstack1l1_opy_ (u"ࠬ࡮࡯ࡴࡶࡑࡥࡲ࡫ࠧ૮")] = socket.gethostname()
  if bstack1l1_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧ૯") in bstack1l1lllll1_opy_:
    del (bstack1l1lllll1_opy_[bstack1l1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ૰")])
  return bstack1l1lllll1_opy_
def bstack1l1lll11ll_opy_(config):
  global bstack11l11ll1ll_opy_
  bstack11l111lll1_opy_ = {}
  caps = bstack1lll11ll1l_opy_
  if bstack11l11ll1ll_opy_:
    caps += bstack1l1l11l1l1_opy_
  for key in caps:
    if key in config:
      bstack11l111lll1_opy_[key] = config[key]
  return bstack11l111lll1_opy_
def bstack11lll1lll_opy_(bstack1l1lllll1_opy_, bstack11l111lll1_opy_):
  bstack1l11l1111l_opy_ = {}
  for key in bstack1l1lllll1_opy_.keys():
    if key in bstack1111llll1l_opy_:
      bstack1l11l1111l_opy_[bstack1111llll1l_opy_[key]] = bstack1l1lllll1_opy_[key]
    else:
      bstack1l11l1111l_opy_[key] = bstack1l1lllll1_opy_[key]
  for key in bstack11l111lll1_opy_:
    if key in bstack1111llll1l_opy_:
      bstack1l11l1111l_opy_[bstack1111llll1l_opy_[key]] = bstack11l111lll1_opy_[key]
    else:
      bstack1l11l1111l_opy_[key] = bstack11l111lll1_opy_[key]
  return bstack1l11l1111l_opy_
def bstack1ll11lll1_opy_(config, index=0):
  global bstack11l11ll1ll_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1111lll1ll_opy_ = bstack111ll1111l_opy_(bstack1l11l1l11_opy_, config, logger)
  bstack11l111lll1_opy_ = bstack1l1lll11ll_opy_(config)
  bstack111ll1111_opy_ = bstack1lll11ll1l_opy_
  bstack111ll1111_opy_ += bstack111llllll_opy_
  bstack11l111lll1_opy_ = update(bstack11l111lll1_opy_, bstack1111lll1ll_opy_)
  if bstack11l11ll1ll_opy_:
    bstack111ll1111_opy_ += bstack1l1l11l1l1_opy_
  if bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૱") in config:
    if bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ૲") in config[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૳")][index]:
      caps[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ૴")] = config[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૵")][index][bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ૶")]
    if bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ૷") in config[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૸")][index]:
      caps[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪૹ")] = str(config[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ૺ")][index][bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬૻ")])
    bstack1ll11l1lll_opy_ = bstack111ll1111l_opy_(bstack1l11l1l11_opy_, config[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૼ")][index], logger)
    bstack111ll1111_opy_ += list(bstack1ll11l1lll_opy_.keys())
    for bstack1lll11lll1_opy_ in bstack111ll1111_opy_:
      if bstack1lll11lll1_opy_ in config[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૽")][index]:
        if bstack1lll11lll1_opy_ == bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ૾"):
          try:
            bstack1ll11l1lll_opy_[bstack1lll11lll1_opy_] = str(config[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૿")][index][bstack1lll11lll1_opy_] * 1.0)
          except:
            bstack1ll11l1lll_opy_[bstack1lll11lll1_opy_] = str(config[bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ଀")][index][bstack1lll11lll1_opy_])
        else:
          bstack1ll11l1lll_opy_[bstack1lll11lll1_opy_] = config[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଁ")][index][bstack1lll11lll1_opy_]
        del (config[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଂ")][index][bstack1lll11lll1_opy_])
    bstack11l111lll1_opy_ = update(bstack11l111lll1_opy_, bstack1ll11l1lll_opy_)
  bstack1l1lllll1_opy_ = bstack1ll1lll1l_opy_(config, index)
  for bstack111111ll1l_opy_ in bstack1lll11ll1l_opy_ + list(bstack1111lll1ll_opy_.keys()):
    if bstack111111ll1l_opy_ in bstack1l1lllll1_opy_:
      bstack11l111lll1_opy_[bstack111111ll1l_opy_] = bstack1l1lllll1_opy_[bstack111111ll1l_opy_]
      del (bstack1l1lllll1_opy_[bstack111111ll1l_opy_])
  if bstack1l1ll1l11l_opy_(config):
    bstack1l1lllll1_opy_[bstack1l1_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬଃ")] = True
    caps.update(bstack11l111lll1_opy_)
    caps[bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ଄")] = bstack1l1lllll1_opy_
  else:
    bstack1l1lllll1_opy_[bstack1l1_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧଅ")] = False
    caps.update(bstack11lll1lll_opy_(bstack1l1lllll1_opy_, bstack11l111lll1_opy_))
    if bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ଆ") in caps:
      caps[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪଇ")] = caps[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଈ")]
      del (caps[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଉ")])
    if bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଊ") in caps:
      caps[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨଋ")] = caps[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨଌ")]
      del (caps[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ଍")])
  return caps
def bstack1lllll11l1_opy_():
  global bstack111111ll11_opy_
  global CONFIG
  if bstack11llll111_opy_() <= version.parse(bstack1l1_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩ଎")):
    if bstack111111ll11_opy_ != bstack1l1_opy_ (u"ࠪࠫଏ"):
      return bstack1l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧଐ") + bstack111111ll11_opy_ + bstack1l1_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤ଑")
    return bstack11l1ll11l1_opy_
  if bstack111111ll11_opy_ != bstack1l1_opy_ (u"࠭ࠧ଒"):
    return bstack1l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤଓ") + bstack111111ll11_opy_ + bstack1l1_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤଔ")
  return bstack1lll11l111_opy_
def bstack1ll111ll11_opy_(options):
  return hasattr(options, bstack1l1_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪକ"))
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
def bstack11l11lll1_opy_(options, bstack1l1ll11l1_opy_):
  for bstack11l111l1l1_opy_ in bstack1l1ll11l1_opy_:
    if bstack11l111l1l1_opy_ in [bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଖ"), bstack1l1_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨଗ")]:
      continue
    if bstack11l111l1l1_opy_ in options._experimental_options:
      options._experimental_options[bstack11l111l1l1_opy_] = update(options._experimental_options[bstack11l111l1l1_opy_],
                                                         bstack1l1ll11l1_opy_[bstack11l111l1l1_opy_])
    else:
      options.add_experimental_option(bstack11l111l1l1_opy_, bstack1l1ll11l1_opy_[bstack11l111l1l1_opy_])
  if bstack1l1_opy_ (u"ࠬࡧࡲࡨࡵࠪଘ") in bstack1l1ll11l1_opy_:
    for arg in bstack1l1ll11l1_opy_[bstack1l1_opy_ (u"࠭ࡡࡳࡩࡶࠫଙ")]:
      options.add_argument(arg)
    del (bstack1l1ll11l1_opy_[bstack1l1_opy_ (u"ࠧࡢࡴࡪࡷࠬଚ")])
  if bstack1l1_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬଛ") in bstack1l1ll11l1_opy_:
    for ext in bstack1l1ll11l1_opy_[bstack1l1_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ଜ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l1ll11l1_opy_[bstack1l1_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧଝ")])
def bstack1lll1l1lll_opy_(options, bstack1l1l1l111l_opy_):
  if bstack1l1_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪଞ") in bstack1l1l1l111l_opy_:
    for bstack1l11ll1l1_opy_ in bstack1l1l1l111l_opy_[bstack1l1_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫଟ")]:
      if bstack1l11ll1l1_opy_ in options._preferences:
        options._preferences[bstack1l11ll1l1_opy_] = update(options._preferences[bstack1l11ll1l1_opy_], bstack1l1l1l111l_opy_[bstack1l1_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬଠ")][bstack1l11ll1l1_opy_])
      else:
        options.set_preference(bstack1l11ll1l1_opy_, bstack1l1l1l111l_opy_[bstack1l1_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ଡ")][bstack1l11ll1l1_opy_])
  if bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଢ") in bstack1l1l1l111l_opy_:
    for arg in bstack1l1l1l111l_opy_[bstack1l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧଣ")]:
      options.add_argument(arg)
def bstack11ll11lll_opy_(options, bstack1ll1l1111l_opy_):
  if bstack1l1_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫତ") in bstack1ll1l1111l_opy_:
    options.use_webview(bool(bstack1ll1l1111l_opy_[bstack1l1_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬଥ")]))
  bstack11l11lll1_opy_(options, bstack1ll1l1111l_opy_)
def bstack1lllll11ll_opy_(options, bstack11ll1l1l1_opy_):
  for bstack11l1ll1l11_opy_ in bstack11ll1l1l1_opy_:
    if bstack11l1ll1l11_opy_ in [bstack1l1_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩଦ"), bstack1l1_opy_ (u"࠭ࡡࡳࡩࡶࠫଧ")]:
      continue
    options.set_capability(bstack11l1ll1l11_opy_, bstack11ll1l1l1_opy_[bstack11l1ll1l11_opy_])
  if bstack1l1_opy_ (u"ࠧࡢࡴࡪࡷࠬନ") in bstack11ll1l1l1_opy_:
    for arg in bstack11ll1l1l1_opy_[bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭଩")]:
      options.add_argument(arg)
  if bstack1l1_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭ପ") in bstack11ll1l1l1_opy_:
    options.bstack111lllll1l_opy_(bool(bstack11ll1l1l1_opy_[bstack1l1_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧଫ")]))
def bstack11l1lllll1_opy_(options, bstack11ll1ll1l_opy_):
  for bstack1l1lll1ll_opy_ in bstack11ll1ll1l_opy_:
    if bstack1l1lll1ll_opy_ in [bstack1l1_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨବ"), bstack1l1_opy_ (u"ࠬࡧࡲࡨࡵࠪଭ")]:
      continue
    options._options[bstack1l1lll1ll_opy_] = bstack11ll1ll1l_opy_[bstack1l1lll1ll_opy_]
  if bstack1l1_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪମ") in bstack11ll1ll1l_opy_:
    for bstack1l1111ll11_opy_ in bstack11ll1ll1l_opy_[bstack1l1_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଯ")]:
      options.bstack111l111ll_opy_(
        bstack1l1111ll11_opy_, bstack11ll1ll1l_opy_[bstack1l1_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬର")][bstack1l1111ll11_opy_])
  if bstack1l1_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ଱") in bstack11ll1ll1l_opy_:
    for arg in bstack11ll1ll1l_opy_[bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଲ")]:
      options.add_argument(arg)
def bstack1111lll111_opy_(options, caps):
  if not hasattr(options, bstack1l1_opy_ (u"ࠫࡐࡋ࡙ࠨଳ")):
    return
  if options.KEY == bstack1l1_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ଴"):
    options = bstack11l1111l_opy_.bstack111ll1l1ll_opy_(bstack111ll1lll1_opy_=options, config=CONFIG)
  if options.KEY == bstack1l1_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫଵ") and options.KEY in caps:
    bstack11l11lll1_opy_(options, caps[bstack1l1_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬଶ")])
  elif options.KEY == bstack1l1_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ଷ") and options.KEY in caps:
    bstack1lll1l1lll_opy_(options, caps[bstack1l1_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧସ")])
  elif options.KEY == bstack1l1_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫହ") and options.KEY in caps:
    bstack1lllll11ll_opy_(options, caps[bstack1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬ଺")])
  elif options.KEY == bstack1l1_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭଻") and options.KEY in caps:
    bstack11ll11lll_opy_(options, caps[bstack1l1_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹ଼ࠧ")])
  elif options.KEY == bstack1l1_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ଽ") and options.KEY in caps:
    bstack11l1lllll1_opy_(options, caps[bstack1l1_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧା")])
def bstack111ll1llll_opy_(caps):
  global bstack11l11ll1ll_opy_
  if isinstance(os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪି")), str):
    bstack11l11ll1ll_opy_ = eval(os.getenv(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫୀ")))
  if bstack11l11ll1ll_opy_:
    if bstack111ll11lll_opy_() < version.parse(bstack1l1_opy_ (u"ࠫ࠷࠴࠳࠯࠲ࠪୁ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1l1_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬୂ")
    if bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫୃ") in caps:
      browser = caps[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬୄ")]
    elif bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ୅") in caps:
      browser = caps[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪ୆")]
    browser = str(browser).lower()
    if browser == bstack1l1_opy_ (u"ࠪ࡭ࡵ࡮࡯࡯ࡧࠪେ") or browser == bstack1l1_opy_ (u"ࠫ࡮ࡶࡡࡥࠩୈ"):
      browser = bstack1l1_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬ୉")
    if browser == bstack1l1_opy_ (u"࠭ࡳࡢ࡯ࡶࡹࡳ࡭ࠧ୊"):
      browser = bstack1l1_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧୋ")
    if browser not in [bstack1l1_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨୌ"), bstack1l1_opy_ (u"ࠩࡨࡨ࡬࡫୍ࠧ"), bstack1l1_opy_ (u"ࠪ࡭ࡪ࠭୎"), bstack1l1_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫ୏"), bstack1l1_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭୐")]:
      return None
    try:
      package = bstack1l1_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࢀࢃ࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ୑").format(browser)
      name = bstack1l1_opy_ (u"ࠧࡐࡲࡷ࡭ࡴࡴࡳࠨ୒")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1ll111ll11_opy_(options):
        return None
      for bstack111111ll1l_opy_ in caps.keys():
        options.set_capability(bstack111111ll1l_opy_, caps[bstack111111ll1l_opy_])
      bstack1111lll111_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack111l1lll1_opy_(options, bstack1l11111l1l_opy_):
  if not bstack1ll111ll11_opy_(options):
    return
  for bstack111111ll1l_opy_ in bstack1l11111l1l_opy_.keys():
    if bstack111111ll1l_opy_ in bstack111llllll_opy_:
      continue
    if bstack111111ll1l_opy_ in options._caps and type(options._caps[bstack111111ll1l_opy_]) in [dict, list]:
      options._caps[bstack111111ll1l_opy_] = update(options._caps[bstack111111ll1l_opy_], bstack1l11111l1l_opy_[bstack111111ll1l_opy_])
    else:
      options.set_capability(bstack111111ll1l_opy_, bstack1l11111l1l_opy_[bstack111111ll1l_opy_])
  bstack1111lll111_opy_(options, bstack1l11111l1l_opy_)
  if bstack1l1_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧ୓") in options._caps:
    if options._caps[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ୔")] and options._caps[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ୕")].lower() != bstack1l1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬୖ"):
      del options._caps[bstack1l1_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡧࡩࡧࡻࡧࡨࡧࡵࡅࡩࡪࡲࡦࡵࡶࠫୗ")]
def bstack1111ll1l1l_opy_(proxy_config):
  if bstack1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ୘") in proxy_config:
    proxy_config[bstack1l1_opy_ (u"ࠧࡴࡵ࡯ࡔࡷࡵࡸࡺࠩ୙")] = proxy_config[bstack1l1_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ୚")]
    del (proxy_config[bstack1l1_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭୛")])
  if bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭ଡ଼") in proxy_config and proxy_config[bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧଢ଼")].lower() != bstack1l1_opy_ (u"ࠬࡪࡩࡳࡧࡦࡸࠬ୞"):
    proxy_config[bstack1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩୟ")] = bstack1l1_opy_ (u"ࠧ࡮ࡣࡱࡹࡦࡲࠧୠ")
  if bstack1l1_opy_ (u"ࠨࡲࡵࡳࡽࡿࡁࡶࡶࡲࡧࡴࡴࡦࡪࡩࡘࡶࡱ࠭ୡ") in proxy_config:
    proxy_config[bstack1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬୢ")] = bstack1l1_opy_ (u"ࠪࡴࡦࡩࠧୣ")
  return proxy_config
def bstack11ll1ll111_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ୤") in config:
    return proxy
  config[bstack1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ୥")] = bstack1111ll1l1l_opy_(config[bstack1l1_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୦")])
  if proxy == None:
    proxy = Proxy(config[bstack1l1_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭୧")])
  return proxy
def bstack1l1l111l1_opy_(self):
  global CONFIG
  global bstack1ll1l11ll1_opy_
  try:
    proxy = bstack1l1l11lll1_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1l1_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭୨")):
        proxies = bstack111l1ll1l_opy_(proxy, bstack1lllll11l1_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll1lll11_opy_ = proxies.popitem()
          if bstack1l1_opy_ (u"ࠤ࠽࠳࠴ࠨ୩") in bstack1ll1lll11_opy_:
            return bstack1ll1lll11_opy_
          else:
            return bstack1l1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ୪") + bstack1ll1lll11_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡱࡴࡲࡼࡾࠦࡵࡳ࡮ࠣ࠾ࠥࢁࡽࠣ୫").format(str(e)))
  return bstack1ll1l11ll1_opy_(self)
def bstack1l11l1l1l1_opy_():
  global CONFIG
  return bstack1l11l1lll1_opy_(CONFIG) and bstack1l111l11ll_opy_() and bstack11llll111_opy_() >= version.parse(bstack1llll11l1l_opy_)
def bstack11lll1lll1_opy_():
  global CONFIG
  return (bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ୬") in CONFIG or bstack1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ୭") in CONFIG) and bstack1l11lll1l1_opy_()
def bstack1l1l1l1l1l_opy_(config):
  bstack1111ll1ll1_opy_ = {}
  if bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୮") in config:
    bstack1111ll1ll1_opy_ = config[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୯")]
  if bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୰") in config:
    bstack1111ll1ll1_opy_ = config[bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩୱ")]
  proxy = bstack1l1l11lll1_opy_(config)
  if proxy:
    if proxy.endswith(bstack1l1_opy_ (u"ࠫ࠳ࡶࡡࡤࠩ୲")) and os.path.isfile(proxy):
      bstack1111ll1ll1_opy_[bstack1l1_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨ୳")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1l1_opy_ (u"࠭࠮ࡱࡣࡦࠫ୴")):
        proxies = bstack1111ll1lll_opy_(config, bstack1lllll11l1_opy_())
        if len(proxies) > 0:
          protocol, bstack1ll1lll11_opy_ = proxies.popitem()
          if bstack1l1_opy_ (u"ࠢ࠻࠱࠲ࠦ୵") in bstack1ll1lll11_opy_:
            parsed_url = urlparse(bstack1ll1lll11_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1l1_opy_ (u"ࠣ࠼࠲࠳ࠧ୶") + bstack1ll1lll11_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1111ll1ll1_opy_[bstack1l1_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬ୷")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1111ll1ll1_opy_[bstack1l1_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭୸")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1111ll1ll1_opy_[bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧ୹")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1111ll1ll1_opy_[bstack1l1_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨ୺")] = str(parsed_url.password)
  return bstack1111ll1ll1_opy_
def bstack1ll11111l1_opy_(config):
  if bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫ୻") in config:
    return config[bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬ୼")]
  return {}
def bstack11ll111l1l_opy_(caps):
  global bstack1l11lll1l_opy_
  if bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ୽") in caps:
    caps[bstack1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ୾")][bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩ୿")] = True
    if bstack1l11lll1l_opy_:
      caps[bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ஀")][bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ஁")] = bstack1l11lll1l_opy_
  else:
    caps[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫஂ")] = True
    if bstack1l11lll1l_opy_:
      caps[bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨஃ")] = bstack1l11lll1l_opy_
@measure(event_name=EVENTS.bstack111ll1ll11_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1ll1lllll_opy_():
  global CONFIG
  if not bstack1lllllll11_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ஄") in CONFIG and bstack1ll1111ll1_opy_(CONFIG[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭அ")]):
    if (
      bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧஆ") in CONFIG
      and bstack1ll1111ll1_opy_(CONFIG[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨஇ")].get(bstack1l1_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩஈ")))
    ):
      logger.debug(bstack1l1_opy_ (u"ࠨࡌࡰࡥࡤࡰࠥࡨࡩ࡯ࡣࡵࡽࠥࡴ࡯ࡵࠢࡶࡸࡦࡸࡴࡦࡦࠣࡥࡸࠦࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡥ࡯ࡣࡥࡰࡪࡪࠢஉ"))
      return
    bstack1111ll1ll1_opy_ = bstack1l1l1l1l1l_opy_(CONFIG)
    bstack11l111111_opy_(CONFIG[bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪஊ")], bstack1111ll1ll1_opy_)
def bstack11l111111_opy_(key, bstack1111ll1ll1_opy_):
  global bstack1111l11lll_opy_
  logger.info(bstack11lll1l1ll_opy_)
  try:
    bstack1111l11lll_opy_ = Local()
    bstack11lll1111l_opy_ = {bstack1l1_opy_ (u"ࠨ࡭ࡨࡽࠬ஋"): key}
    bstack11lll1111l_opy_.update(bstack1111ll1ll1_opy_)
    logger.debug(bstack111ll1l11l_opy_.format(str(bstack11lll1111l_opy_)).replace(key, bstack1l1_opy_ (u"ࠩ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭஌")))
    bstack1111l11lll_opy_.start(**bstack11lll1111l_opy_)
    if bstack1111l11lll_opy_.isRunning():
      logger.info(bstack1l1111ll1l_opy_)
  except Exception as e:
    bstack1ll1llll1l_opy_(bstack1lll1l1l1l_opy_.format(str(e)))
def bstack1l1l11l11_opy_():
  global bstack1111l11lll_opy_
  if bstack1111l11lll_opy_.isRunning():
    logger.info(bstack1l11l11l1_opy_)
    bstack1111l11lll_opy_.stop()
  bstack1111l11lll_opy_ = None
def bstack11l1l1111l_opy_(bstack11ll11ll1_opy_=[]):
  global CONFIG
  bstack1ll1l1ll1_opy_ = []
  bstack111ll1lll_opy_ = [bstack1l1_opy_ (u"ࠪࡳࡸ࠭஍"), bstack1l1_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧஎ"), bstack1l1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩஏ"), bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨஐ"), bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ஑"), bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩஒ")]
  try:
    for err in bstack11ll11ll1_opy_:
      bstack1l11111l11_opy_ = {}
      for k in bstack111ll1lll_opy_:
        val = CONFIG[bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬஓ")][int(err[bstack1l1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩஔ")])].get(k)
        if val:
          bstack1l11111l11_opy_[k] = val
      if(err[bstack1l1_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪக")] != bstack1l1_opy_ (u"ࠬ࠭஖")):
        bstack1l11111l11_opy_[bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡷࠬ஗")] = {
          err[bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ஘")]: err[bstack1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧங")]
        }
        bstack1ll1l1ll1_opy_.append(bstack1l11111l11_opy_)
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫ࡵࡲ࡮ࡣࡷࡸ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵ࠼ࠣࠫச") + str(e))
  finally:
    return bstack1ll1l1ll1_opy_
def bstack11lllll1ll_opy_(file_name):
  bstack1l1llll11l_opy_ = []
  try:
    bstack111l1111l_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack111l1111l_opy_):
      with open(bstack111l1111l_opy_) as f:
        bstack111l1l1ll_opy_ = json.load(f)
        bstack1l1llll11l_opy_ = bstack111l1l1ll_opy_
      os.remove(bstack111l1111l_opy_)
    return bstack1l1llll11l_opy_
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡩ࡯ࡦ࡬ࡲ࡬ࠦࡥࡳࡴࡲࡶࠥࡲࡩࡴࡶ࠽ࠤࠬ஛") + str(e))
    return bstack1l1llll11l_opy_
def bstack111l1ll1ll_opy_():
  try:
      from bstack_utils.constants import bstack11l1l11111_opy_, EVENTS
      from bstack_utils.helper import bstack1lll1l1l11_opy_, get_host_info, bstack11l11111_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack1ll1l11111_opy_ = os.path.join(os.getcwd(), bstack1l1_opy_ (u"ࠫࡱࡵࡧࠨஜ"), bstack1l1_opy_ (u"ࠬࡱࡥࡺ࠯ࡰࡩࡹࡸࡩࡤࡵ࠱࡮ࡸࡵ࡮ࠨ஝"))
      lock = FileLock(bstack1ll1l11111_opy_+bstack1l1_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧஞ"))
      def bstack1l11l1ll_opy_():
          try:
              with lock:
                  with open(bstack1ll1l11111_opy_, bstack1l1_opy_ (u"ࠢࡳࠤட"), encoding=bstack1l1_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢ஠")) as file:
                      data = json.load(file)
                      config = {
                          bstack1l1_opy_ (u"ࠤ࡫ࡩࡦࡪࡥࡳࡵࠥ஡"): {
                              bstack1l1_opy_ (u"ࠥࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠤ஢"): bstack1l1_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠢண"),
                          }
                      }
                      bstack11l11lllll_opy_ = datetime.utcnow()
                      bstack1l1ll11l_opy_ = bstack11l11lllll_opy_.strftime(bstack1l1_opy_ (u"࡙ࠧࠫ࠮ࠧࡰ࠱ࠪࡪࡔࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪ࡛ࠥࡔࡄࠤத"))
                      test_id = os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ஥")) if os.environ.get(bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ஦")) else bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥ஧"))
                      payload = {
                          bstack1l1_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࠨந"): bstack1l1_opy_ (u"ࠥࡷࡩࡱ࡟ࡦࡸࡨࡲࡹࡹࠢன"),
                          bstack1l1_opy_ (u"ࠦࡩࡧࡴࡢࠤப"): {
                              bstack1l1_opy_ (u"ࠧࡺࡥࡴࡶ࡫ࡹࡧࡥࡵࡶ࡫ࡧࠦ஫"): test_id,
                              bstack1l1_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡪ࡟ࡥࡣࡼࠦ஬"): bstack1l1ll11l_opy_,
                              bstack1l1_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࠦ஭"): bstack1l1_opy_ (u"ࠣࡕࡇࡏࡋ࡫ࡡࡵࡷࡵࡩࡕ࡫ࡲࡧࡱࡵࡱࡦࡴࡣࡦࠤம"),
                              bstack1l1_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠ࡬ࡶࡳࡳࠨய"): {
                                  bstack1l1_opy_ (u"ࠥࡱࡪࡧࡳࡶࡴࡨࡷࠧர"): data,
                                  bstack1l1_opy_ (u"ࠦࡸࡪ࡫ࡓࡷࡱࡍࡩࠨற"): bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢல"))
                              },
                              bstack1l1_opy_ (u"ࠨࡵࡴࡧࡵࡣࡩࡧࡴࡢࠤள"): bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠢࡶࡵࡨࡶࡓࡧ࡭ࡦࠤழ")),
                              bstack1l1_opy_ (u"ࠣࡪࡲࡷࡹࡥࡩ࡯ࡨࡲࠦவ"): get_host_info()
                          }
                      }
                      bstack1l1l1lll1l_opy_ = bstack11ll11llll_opy_(cli.config, [bstack1l1_opy_ (u"ࠤࡤࡴ࡮ࡹࠢஶ"), bstack1l1_opy_ (u"ࠥࡩࡩࡹࡉ࡯ࡵࡷࡶࡺࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠣஷ"), bstack1l1_opy_ (u"ࠦࡦࡶࡩࠣஸ")], bstack11l1l11111_opy_)
                      response = bstack1lll1l1l11_opy_(bstack1l1_opy_ (u"ࠧࡖࡏࡔࡖࠥஹ"), bstack1l1l1lll1l_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack1l1_opy_ (u"ࠨࡄࡢࡶࡤࠤࡸ࡫࡮ࡵࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡶࡲࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡪࡡࡵࡣࠣࡿࢂࠨ஺").format(bstack11l1l11111_opy_, payload))
                      else:
                          logger.debug(bstack1l1_opy_ (u"ࠢࡓࡧࡴࡹࡪࡹࡴࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡨࡲࡶࠥࢁࡽࠡࡹ࡬ࡸ࡭ࠦࡤࡢࡶࡤࠤࢀࢃࠢ஻").format(bstack11l1l11111_opy_, payload))
          except Exception as e:
              logger.debug(bstack1l1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫࡮ࡥࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢࡾࢁࠧ஼").format(e))
      bstack1l11l1ll_opy_()
      bstack1ll1l1l111_opy_(bstack1ll1l11111_opy_, logger)
  except:
    pass
def bstack1111l1l111_opy_():
  global bstack1ll1l1l1l1_opy_
  global bstack11lll11ll_opy_
  global bstack1ll11l11l1_opy_
  global bstack11lllll11_opy_
  global bstack1ll1l111ll_opy_
  global bstack11lll1l1l1_opy_
  global CONFIG
  bstack1ll11ll1l_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪ஽"))
  if bstack1ll11ll1l_opy_ in [bstack1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩா"), bstack1l1_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪி")]:
    bstack11ll1l111_opy_()
  percy.shutdown()
  if bstack1ll1l1l1l1_opy_:
    logger.warning(bstack11111llll1_opy_.format(str(bstack1ll1l1l1l1_opy_)))
  else:
    try:
      bstack11l11ll1l1_opy_ = bstack11l1ll1111_opy_(bstack1l1_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫீ"), logger)
      if bstack11l11ll1l1_opy_.get(bstack1l1_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫு")) and bstack11l11ll1l1_opy_.get(bstack1l1_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬூ")).get(bstack1l1_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪ௃")):
        logger.warning(bstack11111llll1_opy_.format(str(bstack11l11ll1l1_opy_[bstack1l1_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ௄")][bstack1l1_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬ௅")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1llllll1ll_opy_.invoke(Events.bstack111l1l11l_opy_)
  logger.info(bstack1111l11111_opy_)
  global bstack1111l11lll_opy_
  if bstack1111l11lll_opy_:
    bstack1l1l11l11_opy_()
  try:
    with bstack11l1l111l1_opy_:
      bstack1l1l1ll1ll_opy_ = bstack11lll11ll_opy_.copy()
    for driver in bstack1l1l1ll1ll_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack111l11lll1_opy_)
  if bstack11lll1l1l1_opy_ == bstack1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪெ"):
    bstack1ll1l111ll_opy_ = bstack11lllll1ll_opy_(bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ே"))
  if bstack11lll1l1l1_opy_ == bstack1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ை") and len(bstack11lllll11_opy_) == 0:
    bstack11lllll11_opy_ = bstack11lllll1ll_opy_(bstack1l1_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ௉"))
    if len(bstack11lllll11_opy_) == 0:
      bstack11lllll11_opy_ = bstack11lllll1ll_opy_(bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧொ"))
  bstack11ll111111_opy_ = bstack1l1_opy_ (u"ࠩࠪோ")
  if len(bstack1ll11l11l1_opy_) > 0:
    bstack11ll111111_opy_ = bstack11l1l1111l_opy_(bstack1ll11l11l1_opy_)
  elif len(bstack11lllll11_opy_) > 0:
    bstack11ll111111_opy_ = bstack11l1l1111l_opy_(bstack11lllll11_opy_)
  elif len(bstack1ll1l111ll_opy_) > 0:
    bstack11ll111111_opy_ = bstack11l1l1111l_opy_(bstack1ll1l111ll_opy_)
  elif len(bstack11ll11ll11_opy_) > 0:
    bstack11ll111111_opy_ = bstack11l1l1111l_opy_(bstack11ll11ll11_opy_)
  if bool(bstack11ll111111_opy_):
    bstack1lll1ll1l1_opy_(bstack11ll111111_opy_)
  else:
    bstack1lll1ll1l1_opy_()
  bstack1ll1l1l111_opy_(bstack11l1l1l111_opy_, logger)
  if bstack1ll11ll1l_opy_ not in [bstack1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫௌ")]:
    bstack111l1ll1ll_opy_()
  bstack1ll1111l1_opy_.bstack1l1lll1l_opy_(CONFIG)
  if len(bstack1ll1l111ll_opy_) > 0:
    sys.exit(len(bstack1ll1l111ll_opy_))
def bstack1l1l11lll_opy_(bstack1l11ll1ll1_opy_, frame):
  global bstack11l11111_opy_
  logger.error(bstack1l11l11111_opy_)
  bstack11l11111_opy_.set_property(bstack1l1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡓࡵ்ࠧ"), bstack1l11ll1ll1_opy_)
  if hasattr(signal, bstack1l1_opy_ (u"࡙ࠬࡩࡨࡰࡤࡰࡸ࠭௎")):
    bstack11l11111_opy_.set_property(bstack1l1_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭௏"), signal.Signals(bstack1l11ll1ll1_opy_).name)
  else:
    bstack11l11111_opy_.set_property(bstack1l1_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧௐ"), bstack1l1_opy_ (u"ࠨࡕࡌࡋ࡚ࡔࡋࡏࡑ࡚ࡒࠬ௑"))
  if cli.is_running():
    bstack1llllll1ll_opy_.invoke(Events.bstack111l1l11l_opy_)
  bstack1ll11ll1l_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪ௒"))
  if bstack1ll11ll1l_opy_ == bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ௓") and not cli.is_enabled(CONFIG):
    bstack1l11llll_opy_.stop(bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ௔")))
  bstack1111l1l111_opy_()
  sys.exit(1)
def bstack1ll1llll1l_opy_(err):
  logger.critical(bstack1111l1llll_opy_.format(str(err)))
  bstack1lll1ll1l1_opy_(bstack1111l1llll_opy_.format(str(err)), True)
  atexit.unregister(bstack1111l1l111_opy_)
  bstack11ll1l111_opy_()
  sys.exit(1)
def bstack1lll1lll1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1lll1ll1l1_opy_(message, True)
  atexit.unregister(bstack1111l1l111_opy_)
  bstack11ll1l111_opy_()
  sys.exit(1)
def bstack11l1111l1l_opy_():
  global CONFIG
  global bstack1lll11111_opy_
  global bstack1ll11l1l1l_opy_
  global bstack1ll11ll1ll_opy_
  CONFIG = bstack111l1ll11_opy_()
  load_dotenv(CONFIG.get(bstack1l1_opy_ (u"ࠬ࡫࡮ࡷࡈ࡬ࡰࡪ࠭௕")))
  bstack11111ll1l1_opy_()
  bstack1lllllll1l_opy_()
  CONFIG = bstack1l11l11ll1_opy_(CONFIG)
  update(CONFIG, bstack1ll11l1l1l_opy_)
  update(CONFIG, bstack1lll11111_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1lllll1lll_opy_(CONFIG)
  bstack1ll11ll1ll_opy_ = bstack1lllllll11_opy_(CONFIG)
  os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩ௖")] = bstack1ll11ll1ll_opy_.__str__().lower()
  bstack11l11111_opy_.set_property(bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨௗ"), bstack1ll11ll1ll_opy_)
  if (bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௘") in CONFIG and bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௙") in bstack1lll11111_opy_) or (
          bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௚") in CONFIG and bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௛") not in bstack1ll11l1l1l_opy_):
    if os.getenv(bstack1l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ௜")):
      CONFIG[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ௝")] = os.getenv(bstack1l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ௞"))
    else:
      if not CONFIG.get(bstack1l1_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠦ௟"), bstack1l1_opy_ (u"ࠤࠥ௠")) in bstack1ll1111l1l_opy_:
        bstack1lll11ll11_opy_()
  elif (bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௡") not in CONFIG and bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௢") in CONFIG) or (
          bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௣") in bstack1ll11l1l1l_opy_ and bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௤") not in bstack1lll11111_opy_):
    del (CONFIG[bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ௥")])
  if bstack1111ll11ll_opy_(CONFIG):
    bstack1ll1llll1l_opy_(bstack1l11ll11l_opy_)
  Config.bstack1111ll1l_opy_().set_property(bstack1l1_opy_ (u"ࠣࡷࡶࡩࡷࡔࡡ࡮ࡧࠥ௦"), CONFIG[bstack1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ௧")])
  bstack11ll111l1_opy_()
  bstack1ll1ll11l_opy_()
  if bstack11l11ll1ll_opy_ and not CONFIG.get(bstack1l1_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠨ௨"), bstack1l1_opy_ (u"ࠦࠧ௩")) in bstack1ll1111l1l_opy_:
    CONFIG[bstack1l1_opy_ (u"ࠬࡧࡰࡱࠩ௪")] = bstack111lll11l_opy_(CONFIG)
    logger.info(bstack11l1l11lll_opy_.format(CONFIG[bstack1l1_opy_ (u"࠭ࡡࡱࡲࠪ௫")]))
  if not bstack1ll11ll1ll_opy_:
    CONFIG[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ௬")] = [{}]
def bstack1l111lll11_opy_(config, bstack11ll11111_opy_):
  global CONFIG
  global bstack11l11ll1ll_opy_
  CONFIG = config
  bstack11l11ll1ll_opy_ = bstack11ll11111_opy_
def bstack1ll1ll11l_opy_():
  global CONFIG
  global bstack11l11ll1ll_opy_
  if bstack1l1_opy_ (u"ࠨࡣࡳࡴࠬ௭") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1lll1lll1l_opy_(e, bstack11llllll1_opy_)
    bstack11l11ll1ll_opy_ = True
    bstack11l11111_opy_.set_property(bstack1l1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ௮"), True)
def bstack111lll11l_opy_(config):
  bstack1l111l1111_opy_ = bstack1l1_opy_ (u"ࠪࠫ௯")
  app = config[bstack1l1_opy_ (u"ࠫࡦࡶࡰࠨ௰")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1lll11l1ll_opy_:
      if os.path.exists(app):
        bstack1l111l1111_opy_ = bstack1l11l1l1ll_opy_(config, app)
      elif bstack1l11l11l11_opy_(app):
        bstack1l111l1111_opy_ = app
      else:
        bstack1ll1llll1l_opy_(bstack1l1l1l1l1_opy_.format(app))
    else:
      if bstack1l11l11l11_opy_(app):
        bstack1l111l1111_opy_ = app
      elif os.path.exists(app):
        bstack1l111l1111_opy_ = bstack1l11l1l1ll_opy_(app)
      else:
        bstack1ll1llll1l_opy_(bstack1ll11l1l11_opy_)
  else:
    if len(app) > 2:
      bstack1ll1llll1l_opy_(bstack111ll11l1_opy_)
    elif len(app) == 2:
      if bstack1l1_opy_ (u"ࠬࡶࡡࡵࡪࠪ௱") in app and bstack1l1_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ௲") in app:
        if os.path.exists(app[bstack1l1_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ௳")]):
          bstack1l111l1111_opy_ = bstack1l11l1l1ll_opy_(config, app[bstack1l1_opy_ (u"ࠨࡲࡤࡸ࡭࠭௴")], app[bstack1l1_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬ௵")])
        else:
          bstack1ll1llll1l_opy_(bstack1l1l1l1l1_opy_.format(app))
      else:
        bstack1ll1llll1l_opy_(bstack111ll11l1_opy_)
    else:
      for key in app:
        if key in bstack11l11l111_opy_:
          if key == bstack1l1_opy_ (u"ࠪࡴࡦࡺࡨࠨ௶"):
            if os.path.exists(app[key]):
              bstack1l111l1111_opy_ = bstack1l11l1l1ll_opy_(config, app[key])
            else:
              bstack1ll1llll1l_opy_(bstack1l1l1l1l1_opy_.format(app))
          else:
            bstack1l111l1111_opy_ = app[key]
        else:
          bstack1ll1llll1l_opy_(bstack11l11ll11_opy_)
  return bstack1l111l1111_opy_
def bstack1l11l11l11_opy_(bstack1l111l1111_opy_):
  import re
  bstack11l1l11ll_opy_ = re.compile(bstack1l1_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬࠧࠦ௷"))
  bstack11ll1lll11_opy_ = re.compile(bstack1l1_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭࠳ࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪࠥࠤ௸"))
  if bstack1l1_opy_ (u"࠭ࡢࡴ࠼࠲࠳ࠬ௹") in bstack1l111l1111_opy_ or re.fullmatch(bstack11l1l11ll_opy_, bstack1l111l1111_opy_) or re.fullmatch(bstack11ll1lll11_opy_, bstack1l111l1111_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack1ll1l11ll_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1l11l1l1ll_opy_(config, path, bstack1ll11111l_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1l1_opy_ (u"ࠧࡳࡤࠪ௺")).read()).hexdigest()
  bstack11l11l1111_opy_ = bstack1lll1llll1_opy_(md5_hash)
  bstack1l111l1111_opy_ = None
  if bstack11l11l1111_opy_:
    logger.info(bstack111lll1lll_opy_.format(bstack11l11l1111_opy_, md5_hash))
    return bstack11l11l1111_opy_
  bstack1l1ll111l_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack1l1_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭௻"): (os.path.basename(path), open(os.path.abspath(path), bstack1l1_opy_ (u"ࠩࡵࡦࠬ௼")), bstack1l1_opy_ (u"ࠪࡸࡪࡾࡴ࠰ࡲ࡯ࡥ࡮ࡴࠧ௽")),
      bstack1l1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧ௾"): bstack1ll11111l_opy_
    }
  )
  response = requests.post(bstack111l1l111l_opy_, data=multipart_data,
                           headers={bstack1l1_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ௿"): multipart_data.content_type},
                           auth=(config[bstack1l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨఀ")], config[bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪఁ")]))
  try:
    res = json.loads(response.text)
    bstack1l111l1111_opy_ = res[bstack1l1_opy_ (u"ࠨࡣࡳࡴࡤࡻࡲ࡭ࠩం")]
    logger.info(bstack1l111llll_opy_.format(bstack1l111l1111_opy_))
    bstack111111lll_opy_(md5_hash, bstack1l111l1111_opy_)
    cli.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡶࡲ࡯ࡳࡦࡪ࡟ࡢࡲࡳࠦః"), datetime.datetime.now() - bstack1l1ll111l_opy_)
  except ValueError as err:
    bstack1ll1llll1l_opy_(bstack111ll1l1l_opy_.format(str(err)))
  return bstack1l111l1111_opy_
def bstack11ll111l1_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack11lllllll1_opy_
  bstack1lll11l11_opy_ = 1
  bstack1l1l1ll1l1_opy_ = 1
  if bstack1l1_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪఄ") in CONFIG:
    bstack1l1l1ll1l1_opy_ = CONFIG[bstack1l1_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫఅ")]
  else:
    bstack1l1l1ll1l1_opy_ = bstack11l1lll11l_opy_(framework_name, args) or 1
  if bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఆ") in CONFIG:
    bstack1lll11l11_opy_ = len(CONFIG[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩఇ")])
  bstack11lllllll1_opy_ = int(bstack1l1l1ll1l1_opy_) * int(bstack1lll11l11_opy_)
def bstack11l1lll11l_opy_(framework_name, args):
  if framework_name == bstack1111ll111l_opy_ and args and bstack1l1_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬఈ") in args:
      bstack11l1l1111_opy_ = args.index(bstack1l1_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ఉ"))
      return int(args[bstack11l1l1111_opy_ + 1]) or 1
  return 1
def bstack1lll1llll1_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬఊ"))
    bstack111ll1l1l1_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠪࢂࠬఋ")), bstack1l1_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఌ"), bstack1l1_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭఍"))
    if os.path.exists(bstack111ll1l1l1_opy_):
      try:
        bstack1l1llll1l_opy_ = json.load(open(bstack111ll1l1l1_opy_, bstack1l1_opy_ (u"࠭ࡲࡣࠩఎ")))
        if md5_hash in bstack1l1llll1l_opy_:
          bstack11lll1ll11_opy_ = bstack1l1llll1l_opy_[md5_hash]
          bstack1ll111l11_opy_ = datetime.datetime.now()
          bstack1ll111l1l_opy_ = datetime.datetime.strptime(bstack11lll1ll11_opy_[bstack1l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪఏ")], bstack1l1_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬఐ"))
          if (bstack1ll111l11_opy_ - bstack1ll111l1l_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack11lll1ll11_opy_[bstack1l1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ఑")]):
            return None
          return bstack11lll1ll11_opy_[bstack1l1_opy_ (u"ࠪ࡭ࡩ࠭ఒ")]
      except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡶࡪࡧࡤࡪࡰࡪࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࠦࡦࡪ࡮ࡨ࠾ࠥࢁࡽࠨఓ").format(str(e)))
    return None
  bstack111ll1l1l1_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠬࢄࠧఔ")), bstack1l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭క"), bstack1l1_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨఖ"))
  lock_file = bstack111ll1l1l1_opy_ + bstack1l1_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧగ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack111ll1l1l1_opy_):
        with open(bstack111ll1l1l1_opy_, bstack1l1_opy_ (u"ࠩࡵࠫఘ")) as f:
          content = f.read().strip()
          if content:
            bstack1l1llll1l_opy_ = json.loads(content)
            if md5_hash in bstack1l1llll1l_opy_:
              bstack11lll1ll11_opy_ = bstack1l1llll1l_opy_[md5_hash]
              bstack1ll111l11_opy_ = datetime.datetime.now()
              bstack1ll111l1l_opy_ = datetime.datetime.strptime(bstack11lll1ll11_opy_[bstack1l1_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ఙ")], bstack1l1_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨచ"))
              if (bstack1ll111l11_opy_ - bstack1ll111l1l_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack11lll1ll11_opy_[bstack1l1_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪఛ")]):
                return None
              return bstack11lll1ll11_opy_[bstack1l1_opy_ (u"࠭ࡩࡥࠩజ")]
      return None
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡷࡪࡶ࡫ࠤ࡫࡯࡬ࡦࠢ࡯ࡳࡨࡱࡩ࡯ࡩࠣࡪࡴࡸࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩ࠼ࠣࡿࢂ࠭ఝ").format(str(e)))
    return None
def bstack111111lll_opy_(md5_hash, bstack1l111l1111_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫఞ"))
    bstack1l1ll1ll1l_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠩࢁࠫట")), bstack1l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪఠ"))
    if not os.path.exists(bstack1l1ll1ll1l_opy_):
      os.makedirs(bstack1l1ll1ll1l_opy_)
    bstack111ll1l1l1_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠫࢃ࠭డ")), bstack1l1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬఢ"), bstack1l1_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧణ"))
    bstack1l1l11ll11_opy_ = {
      bstack1l1_opy_ (u"ࠧࡪࡦࠪత"): bstack1l111l1111_opy_,
      bstack1l1_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫథ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l1_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ద")),
      bstack1l1_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨధ"): str(__version__)
    }
    try:
      bstack1l1llll1l_opy_ = {}
      if os.path.exists(bstack111ll1l1l1_opy_):
        bstack1l1llll1l_opy_ = json.load(open(bstack111ll1l1l1_opy_, bstack1l1_opy_ (u"ࠫࡷࡨࠧన")))
      bstack1l1llll1l_opy_[md5_hash] = bstack1l1l11ll11_opy_
      with open(bstack111ll1l1l1_opy_, bstack1l1_opy_ (u"ࠧࡽࠫࠣ఩")) as outfile:
        json.dump(bstack1l1llll1l_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰࡥࡣࡷ࡭ࡳ࡭ࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩࠢࡩ࡭ࡱ࡫࠺ࠡࡽࢀࠫప").format(str(e)))
    return
  bstack1l1ll1ll1l_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠧࡿࠩఫ")), bstack1l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨబ"))
  if not os.path.exists(bstack1l1ll1ll1l_opy_):
    os.makedirs(bstack1l1ll1ll1l_opy_)
  bstack111ll1l1l1_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠩࢁࠫభ")), bstack1l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪమ"), bstack1l1_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬయ"))
  lock_file = bstack111ll1l1l1_opy_ + bstack1l1_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫర")
  bstack1l1l11ll11_opy_ = {
    bstack1l1_opy_ (u"࠭ࡩࡥࠩఱ"): bstack1l111l1111_opy_,
    bstack1l1_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪల"): datetime.datetime.strftime(datetime.datetime.now(), bstack1l1_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬళ")),
    bstack1l1_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧఴ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1l1llll1l_opy_ = {}
      if os.path.exists(bstack111ll1l1l1_opy_):
        with open(bstack111ll1l1l1_opy_, bstack1l1_opy_ (u"ࠪࡶࠬవ")) as f:
          content = f.read().strip()
          if content:
            bstack1l1llll1l_opy_ = json.loads(content)
      bstack1l1llll1l_opy_[md5_hash] = bstack1l1l11ll11_opy_
      with open(bstack111ll1l1l1_opy_, bstack1l1_opy_ (u"ࠦࡼࠨశ")) as outfile:
        json.dump(bstack1l1llll1l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡼ࡯ࡴࡩࠢࡩ࡭ࡱ࡫ࠠ࡭ࡱࡦ࡯࡮ࡴࡧࠡࡨࡲࡶࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮ࠠࡶࡲࡧࡥࡹ࡫࠺ࠡࡽࢀࠫష").format(str(e)))
def bstack11111l11ll_opy_(self):
  return
def bstack11ll11111l_opy_(self):
  return
def bstack1llllllll1_opy_():
  global bstack1l111l111l_opy_
  bstack1l111l111l_opy_ = True
@measure(event_name=EVENTS.bstack11111l1111_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack11l1ll1ll_opy_(self):
  global bstack1l1l11l11l_opy_
  global bstack11lll111l_opy_
  global bstack1111l1111l_opy_
  try:
    if bstack1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭స") in bstack1l1l11l11l_opy_ and self.session_id != None and bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫహ"), bstack1l1_opy_ (u"ࠨࠩ఺")) != bstack1l1_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ఻"):
      bstack1llll1ll11_opy_ = bstack1l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦ఼ࠪ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫఽ")
      if bstack1llll1ll11_opy_ == bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬా"):
        bstack1111llllll_opy_(logger)
      if self != None:
        bstack1l1ll11l11_opy_(self, bstack1llll1ll11_opy_, bstack1l1_opy_ (u"࠭ࠬࠡࠩి").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1l1_opy_ (u"ࠧࠨీ")
    if bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨు") in bstack1l1l11l11l_opy_ and getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨూ"), None):
      bstack111111ll_opy_.bstack1lllllll1_opy_(self, bstack1ll1ll1lll_opy_, logger, wait=True)
    if bstack1l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪృ") in bstack1l1l11l11l_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1l1ll11l11_opy_(self, bstack1l1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦౄ"))
      bstack11l111ll1_opy_.bstack1l1llllll1_opy_(self)
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨ౅") + str(e))
  bstack1111l1111l_opy_(self)
  self.session_id = None
def bstack1l11l1ll1_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1l11111lll_opy_
    global bstack1l1l11l11l_opy_
    command_executor = kwargs.get(bstack1l1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠩె"), bstack1l1_opy_ (u"ࠧࠨే"))
    bstack11ll1l11l1_opy_ = False
    if type(command_executor) == str and bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫై") in command_executor:
      bstack11ll1l11l1_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ౉") in str(getattr(command_executor, bstack1l1_opy_ (u"ࠪࡣࡺࡸ࡬ࠨొ"), bstack1l1_opy_ (u"ࠫࠬో"))):
      bstack11ll1l11l1_opy_ = True
    else:
      kwargs = bstack11l1111l_opy_.bstack111ll1l1ll_opy_(bstack111ll1lll1_opy_=kwargs, config=CONFIG)
      return bstack1ll1lll1l1_opy_(self, *args, **kwargs)
    if bstack11ll1l11l1_opy_:
      bstack11lllllll_opy_ = bstack1l111l111_opy_.bstack1lllll1111_opy_(CONFIG, bstack1l1l11l11l_opy_)
      if kwargs.get(bstack1l1_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ౌ")):
        kwargs[bstack1l1_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹ్ࠧ")] = bstack1l11111lll_opy_(kwargs[bstack1l1_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ౎")], bstack1l1l11l11l_opy_, CONFIG, bstack11lllllll_opy_)
      elif kwargs.get(bstack1l1_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ౏")):
        kwargs[bstack1l1_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ౐")] = bstack1l11111lll_opy_(kwargs[bstack1l1_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ౑")], bstack1l1l11l11l_opy_, CONFIG, bstack11lllllll_opy_)
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦ౒").format(str(e)))
  return bstack1ll1lll1l1_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l111l1ll1_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack111ll11ll_opy_(self, command_executor=bstack1l1_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴࠷࠲࠸࠰࠳࠲࠵࠴࠱࠻࠶࠷࠸࠹ࠨ౓"), *args, **kwargs):
  global bstack11lll111l_opy_
  global bstack11lll11ll_opy_
  bstack1llll1l1ll_opy_ = bstack1l11l1ll1_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1l111ll1_opy_.on():
    return bstack1llll1l1ll_opy_
  try:
    logger.debug(bstack1l1_opy_ (u"࠭ࡃࡰ࡯ࡰࡥࡳࡪࠠࡆࡺࡨࡧࡺࡺ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡦࡢ࡮ࡶࡩࠥ࠳ࠠࡼࡿࠪ౔").format(str(command_executor)))
    logger.debug(bstack1l1_opy_ (u"ࠧࡉࡷࡥࠤ࡚ࡘࡌࠡ࡫ࡶࠤ࠲ࠦࡻࡾౕࠩ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰౖࠫ") in command_executor._url:
      bstack11l11111_opy_.set_property(bstack1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ౗"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ౘ") in command_executor):
    bstack11l11111_opy_.set_property(bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬౙ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack11ll1l111l_opy_ = getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭ౚ"), None)
  bstack11111l111l_opy_ = {}
  if self.capabilities is not None:
    bstack11111l111l_opy_[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬ౛")] = self.capabilities.get(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ౜"))
    bstack11111l111l_opy_[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪౝ")] = self.capabilities.get(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ౞"))
    bstack11111l111l_opy_[bstack1l1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡢࡳࡵࡺࡩࡰࡰࡶࠫ౟")] = self.capabilities.get(bstack1l1_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩౠ"))
  if CONFIG.get(bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬౡ"), False) and bstack11l1111l_opy_.bstack111111l11_opy_(bstack11111l111l_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack1l1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ౢ") in bstack1l1l11l11l_opy_ or bstack1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ౣ") in bstack1l1l11l11l_opy_:
    bstack1l11llll_opy_.bstack1l1lll111l_opy_(self)
  if bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ౤") in bstack1l1l11l11l_opy_ and bstack11ll1l111l_opy_ and bstack11ll1l111l_opy_.get(bstack1l1_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ౥"), bstack1l1_opy_ (u"ࠪࠫ౦")) == bstack1l1_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ౧"):
    bstack1l11llll_opy_.bstack1l1lll111l_opy_(self)
  bstack11lll111l_opy_ = self.session_id
  with bstack11l1l111l1_opy_:
    bstack11lll11ll_opy_.append(self)
  return bstack1llll1l1ll_opy_
def bstack1ll11ll11_opy_(args):
  return bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷ࠭౨") in str(args)
def bstack11111ll1l_opy_(self, driver_command, *args, **kwargs):
  global bstack11ll1ll11l_opy_
  global bstack111l11ll11_opy_
  bstack1ll1ll1ll_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ౩"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭౪"), None)
  bstack11l11l11ll_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ౫"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ౬"), None)
  bstack11l1l11l1l_opy_ = getattr(self, bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ౭"), None) != None and getattr(self, bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ౮"), None) == True
  if not bstack111l11ll11_opy_ and bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ౯") in CONFIG and CONFIG[bstack1l1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭౰")] == True and bstack11l1111ll_opy_.bstack11l1llll1_opy_(driver_command) and (bstack11l1l11l1l_opy_ or bstack1ll1ll1ll_opy_ or bstack11l11l11ll_opy_) and not bstack1ll11ll11_opy_(args):
    try:
      bstack111l11ll11_opy_ = True
      logger.debug(bstack1l1_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡻࡾࠩ౱").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵ࡫ࡲࡧࡱࡵࡱࠥࡹࡣࡢࡰࠣࡿࢂ࠭౲").format(str(err)))
    bstack111l11ll11_opy_ = False
  response = bstack11ll1ll11l_opy_(self, driver_command, *args, **kwargs)
  if (bstack1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ౳") in str(bstack1l1l11l11l_opy_).lower() or bstack1l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ౴") in str(bstack1l1l11l11l_opy_).lower()) and bstack1l111ll1_opy_.on():
    try:
      if driver_command == bstack1l1_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨ౵"):
        bstack1l11llll_opy_.bstack1l1ll1lll_opy_({
            bstack1l1_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫ౶"): response[bstack1l1_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬ౷")],
            bstack1l1_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ౸"): bstack1l11llll_opy_.current_test_uuid() if bstack1l11llll_opy_.current_test_uuid() else bstack1l111ll1_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack11l1111l1_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1ll111l11l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack11lll111l_opy_
  global bstack1l1l11l1l_opy_
  global bstack1l1l111ll1_opy_
  global bstack1l111ll111_opy_
  global bstack1l1l1l11ll_opy_
  global bstack1l1l11l11l_opy_
  global bstack1ll1lll1l1_opy_
  global bstack11lll11ll_opy_
  global bstack111lll1l1_opy_
  global bstack1ll1ll1lll_opy_
  if os.getenv(bstack1l1_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭౹")) is not None and bstack11l1111l_opy_.bstack11111llll_opy_(CONFIG) is None:
    CONFIG[bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ౺")] = True
  CONFIG[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ౻")] = str(bstack1l1l11l11l_opy_) + str(__version__)
  bstack11111ll11l_opy_ = os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ౼")]
  bstack11lllllll_opy_ = bstack1l111l111_opy_.bstack1lllll1111_opy_(CONFIG, bstack1l1l11l11l_opy_)
  CONFIG[bstack1l1_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ౽")] = bstack11111ll11l_opy_
  CONFIG[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨ౾")] = bstack11lllllll_opy_
  if CONFIG.get(bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ౿"),bstack1l1_opy_ (u"ࠨࠩಀ")) and bstack1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨಁ") in bstack1l1l11l11l_opy_:
    CONFIG[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪಂ")].pop(bstack1l1_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩಃ"), None)
    CONFIG[bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ಄")].pop(bstack1l1_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫಅ"), None)
  command_executor = bstack1lllll11l1_opy_()
  logger.debug(bstack1l1llll11_opy_.format(command_executor))
  proxy = bstack11ll1ll111_opy_(CONFIG, proxy)
  bstack11111l1l1_opy_ = 0 if bstack1l1l11l1l_opy_ < 0 else bstack1l1l11l1l_opy_
  try:
    if bstack1l111ll111_opy_ is True:
      bstack11111l1l1_opy_ = int(multiprocessing.current_process().name)
    elif bstack1l1l1l11ll_opy_ is True:
      bstack11111l1l1_opy_ = int(threading.current_thread().name)
  except:
    bstack11111l1l1_opy_ = 0
  bstack1l11111l1l_opy_ = bstack1ll11lll1_opy_(CONFIG, bstack11111l1l1_opy_)
  logger.debug(bstack11111lll1l_opy_.format(str(bstack1l11111l1l_opy_)))
  if bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫಆ") in CONFIG and bstack1ll1111ll1_opy_(CONFIG[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬಇ")]):
    bstack11ll111l1l_opy_(bstack1l11111l1l_opy_)
  if bstack11l1111l_opy_.bstack1lll1l111l_opy_(CONFIG, bstack11111l1l1_opy_) and bstack11l1111l_opy_.bstack1l111l1l11_opy_(bstack1l11111l1l_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack11l1111l_opy_.set_capabilities(bstack1l11111l1l_opy_, CONFIG)
  if desired_capabilities:
    bstack11l111ll11_opy_ = bstack1l11l11ll1_opy_(desired_capabilities)
    bstack11l111ll11_opy_[bstack1l1_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩಈ")] = bstack1l1ll1l11l_opy_(CONFIG)
    bstack1llll11111_opy_ = bstack1ll11lll1_opy_(bstack11l111ll11_opy_)
    if bstack1llll11111_opy_:
      bstack1l11111l1l_opy_ = update(bstack1llll11111_opy_, bstack1l11111l1l_opy_)
    desired_capabilities = None
  if options:
    bstack111l1lll1_opy_(options, bstack1l11111l1l_opy_)
  if not options:
    options = bstack111ll1llll_opy_(bstack1l11111l1l_opy_)
  bstack1ll1ll1lll_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಉ"))[bstack11111l1l1_opy_]
  if proxy and bstack11llll111_opy_() >= version.parse(bstack1l1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫಊ")):
    options.proxy(proxy)
  if options and bstack11llll111_opy_() >= version.parse(bstack1l1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫಋ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack11llll111_opy_() < version.parse(bstack1l1_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬಌ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1l11111l1l_opy_)
  logger.info(bstack1lll1111l1_opy_)
  bstack111l11l11_opy_.end(EVENTS.bstack11ll11l11l_opy_.value, EVENTS.bstack11ll11l11l_opy_.value + bstack1l1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ಍"), EVENTS.bstack11ll11l11l_opy_.value + bstack1l1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨಎ"), status=True, failure=None, test_name=bstack1l1l111ll1_opy_)
  if bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡴࡷࡵࡦࡪ࡮ࡨࠫಏ") in kwargs:
    del kwargs[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡵࡸ࡯ࡧ࡫࡯ࡩࠬಐ")]
  try:
    if bstack11llll111_opy_() >= version.parse(bstack1l1_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫ಑")):
      bstack1ll1lll1l1_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack11llll111_opy_() >= version.parse(bstack1l1_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫಒ")):
      bstack1ll1lll1l1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11llll111_opy_() >= version.parse(bstack1l1_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭ಓ")):
      bstack1ll1lll1l1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1ll1lll1l1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack111l1lllll_opy_:
    logger.error(bstack11lllll11l_opy_.format(bstack1l1_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰ࠭ಔ"), str(bstack111l1lllll_opy_)))
    raise bstack111l1lllll_opy_
  if bstack11l1111l_opy_.bstack1lll1l111l_opy_(CONFIG, bstack11111l1l1_opy_) and bstack11l1111l_opy_.bstack1l111l1l11_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪಕ")][bstack1l1_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨಖ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack11l1111l_opy_.set_capabilities(bstack1l11111l1l_opy_, CONFIG)
  try:
    bstack11111lllll_opy_ = bstack1l1_opy_ (u"ࠪࠫಗ")
    if bstack11llll111_opy_() >= version.parse(bstack1l1_opy_ (u"ࠫ࠹࠴࠰࠯࠲ࡥ࠵ࠬಘ")):
      if self.caps is not None:
        bstack11111lllll_opy_ = self.caps.get(bstack1l1_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧಙ"))
    else:
      if self.capabilities is not None:
        bstack11111lllll_opy_ = self.capabilities.get(bstack1l1_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨಚ"))
    if bstack11111lllll_opy_:
      bstack1l1l111l1l_opy_(bstack11111lllll_opy_)
      if bstack11llll111_opy_() <= version.parse(bstack1l1_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧಛ")):
        self.command_executor._url = bstack1l1_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤಜ") + bstack111111ll11_opy_ + bstack1l1_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨಝ")
      else:
        self.command_executor._url = bstack1l1_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧಞ") + bstack11111lllll_opy_ + bstack1l1_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧಟ")
      logger.debug(bstack1lll1ll1ll_opy_.format(bstack11111lllll_opy_))
    else:
      logger.debug(bstack1l1l1l111_opy_.format(bstack1l1_opy_ (u"ࠧࡕࡰࡵ࡫ࡰࡥࡱࠦࡈࡶࡤࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠨಠ")))
  except Exception as e:
    logger.debug(bstack1l1l1l111_opy_.format(e))
  if bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಡ") in bstack1l1l11l11l_opy_:
    bstack11ll1l11l_opy_(bstack1l1l11l1l_opy_, bstack111lll1l1_opy_)
  bstack11lll111l_opy_ = self.session_id
  if bstack1l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧಢ") in bstack1l1l11l11l_opy_ or bstack1l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨಣ") in bstack1l1l11l11l_opy_ or bstack1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨತ") in bstack1l1l11l11l_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack11ll1l111l_opy_ = getattr(threading.current_thread(), bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫಥ"), None)
  if bstack1l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫದ") in bstack1l1l11l11l_opy_ or bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫಧ") in bstack1l1l11l11l_opy_:
    bstack1l11llll_opy_.bstack1l1lll111l_opy_(self)
  if bstack1l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ನ") in bstack1l1l11l11l_opy_ and bstack11ll1l111l_opy_ and bstack11ll1l111l_opy_.get(bstack1l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ಩"), bstack1l1_opy_ (u"ࠨࠩಪ")) == bstack1l1_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪಫ"):
    bstack1l11llll_opy_.bstack1l1lll111l_opy_(self)
  with bstack11l1l111l1_opy_:
    bstack11lll11ll_opy_.append(self)
  if bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಬ") in CONFIG and bstack1l1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩಭ") in CONFIG[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಮ")][bstack11111l1l1_opy_]:
    bstack1l1l111ll1_opy_ = CONFIG[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಯ")][bstack11111l1l1_opy_][bstack1l1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬರ")]
  logger.debug(bstack1l11l1l111_opy_.format(bstack11lll111l_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack111lll1ll_opy_
    def bstack1lll111lll_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1111lll11l_opy_
      if(bstack1l1_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࠮࡫ࡵࠥಱ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠩࢁࠫಲ")), bstack1l1_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪಳ"), bstack1l1_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭಴")), bstack1l1_opy_ (u"ࠬࡽࠧವ")) as fp:
          fp.write(bstack1l1_opy_ (u"ࠨࠢಶ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1l1_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤಷ")))):
          with open(args[1], bstack1l1_opy_ (u"ࠨࡴࠪಸ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1l1_opy_ (u"ࠩࡤࡷࡾࡴࡣࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡣࡳ࡫ࡷࡑࡣࡪࡩ࠭ࡩ࡯࡯ࡶࡨࡼࡹ࠲ࠠࡱࡣࡪࡩࠥࡃࠠࡷࡱ࡬ࡨࠥ࠶ࠩࠨಹ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack111l1111l1_opy_)
            if bstack1l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ಺") in CONFIG and str(CONFIG[bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ಻")]).lower() != bstack1l1_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨ಼ࠫ"):
                bstack111l1ll11l_opy_ = bstack111lll1ll_opy_()
                bstack1l11lll1ll_opy_ = bstack1l1_opy_ (u"࠭ࠧࠨࠌ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠏࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࠻ࠋࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࠾ࠎࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࠽ࠍࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࠽ࠍࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࠎ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡱࡧࡵ࡯ࡥ࡫ࠤࡂࠦࡡࡴࡻࡱࡧࠥ࠮࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸ࠯ࠠ࠾ࡀࠣࡿࢀࠐࠠࠡ࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࠎࠥࠦࡴࡳࡻࠣࡿࢀࠐࠠࠡࠢࠣࡧࡦࡶࡳࠡ࠿ࠣࡎࡘࡕࡎ࠯ࡲࡤࡶࡸ࡫ࠨࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷ࠮ࡁࠊࠡࠢࢀࢁࠥࡩࡡࡵࡥ࡫ࠤ࠭࡫ࡸࠪࠢࡾࡿࠏࠦࠠࠡࠢࡦࡳࡳࡹ࡯࡭ࡧ࠱ࡩࡷࡸ࡯ࡳࠪࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠾ࠧ࠲ࠠࡦࡺࠬ࠿ࠏࠦࠠࡾࡿࠍࠤࠥࡸࡥࡵࡷࡵࡲࠥࡧࡷࡢ࡫ࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡨࡵ࡮࡯ࡧࡦࡸ࠭ࢁࡻࠋࠢࠣࠤࠥࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵ࠼ࠣࠫࢀࡩࡤࡱࡗࡵࡰࢂ࠭ࠠࠬࠢࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩ࠭ࠌࠣࠤࠥࠦ࠮࠯࠰࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴࠌࠣࠤࢂࢃࠩ࠼ࠌࢀࢁࡀࠐ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠌࠪࠫࠬಽ").format(bstack111l1ll11l_opy_=bstack111l1ll11l_opy_)
            lines.insert(1, bstack1l11lll1ll_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1l1_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤಾ")), bstack1l1_opy_ (u"ࠨࡹࠪಿ")) as bstack1ll11l1l1_opy_:
              bstack1ll11l1l1_opy_.writelines(lines)
        CONFIG[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫೀ")] = str(bstack1l1l11l11l_opy_) + str(__version__)
        bstack11111ll11l_opy_ = os.environ[bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨು")]
        bstack11lllllll_opy_ = bstack1l111l111_opy_.bstack1lllll1111_opy_(CONFIG, bstack1l1l11l11l_opy_)
        CONFIG[bstack1l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧೂ")] = bstack11111ll11l_opy_
        CONFIG[bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧೃ")] = bstack11lllllll_opy_
        bstack11111l1l1_opy_ = 0 if bstack1l1l11l1l_opy_ < 0 else bstack1l1l11l1l_opy_
        try:
          if bstack1l111ll111_opy_ is True:
            bstack11111l1l1_opy_ = int(multiprocessing.current_process().name)
          elif bstack1l1l1l11ll_opy_ is True:
            bstack11111l1l1_opy_ = int(threading.current_thread().name)
        except:
          bstack11111l1l1_opy_ = 0
        CONFIG[bstack1l1_opy_ (u"ࠨࡵࡴࡧ࡚࠷ࡈࠨೄ")] = False
        CONFIG[bstack1l1_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨ೅")] = True
        bstack1l11111l1l_opy_ = bstack1ll11lll1_opy_(CONFIG, bstack11111l1l1_opy_)
        logger.debug(bstack11111lll1l_opy_.format(str(bstack1l11111l1l_opy_)))
        if CONFIG.get(bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬೆ")):
          bstack11ll111l1l_opy_(bstack1l11111l1l_opy_)
        if bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೇ") in CONFIG and bstack1l1_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨೈ") in CONFIG[bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ೉")][bstack11111l1l1_opy_]:
          bstack1l1l111ll1_opy_ = CONFIG[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨೊ")][bstack11111l1l1_opy_][bstack1l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫೋ")]
        args.append(os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠧࡿࠩೌ")), bstack1l1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ್"), bstack1l1_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ೎")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1l11111l1l_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1l1_opy_ (u"ࠥ࡭ࡳࡪࡥࡹࡡࡥࡷࡹࡧࡣ࡬࠰࡭ࡷࠧ೏"))
      bstack1111lll11l_opy_ = True
      return bstack1ll11l111_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack1ll1111ll_opy_(self,
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
    global bstack1l1l11l1l_opy_
    global bstack1l1l111ll1_opy_
    global bstack1l111ll111_opy_
    global bstack1l1l1l11ll_opy_
    global bstack1l1l11l11l_opy_
    CONFIG[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭೐")] = str(bstack1l1l11l11l_opy_) + str(__version__)
    bstack11111ll11l_opy_ = os.environ[bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ೑")]
    bstack11lllllll_opy_ = bstack1l111l111_opy_.bstack1lllll1111_opy_(CONFIG, bstack1l1l11l11l_opy_)
    CONFIG[bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩ೒")] = bstack11111ll11l_opy_
    CONFIG[bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ೓")] = bstack11lllllll_opy_
    bstack11111l1l1_opy_ = 0 if bstack1l1l11l1l_opy_ < 0 else bstack1l1l11l1l_opy_
    try:
      if bstack1l111ll111_opy_ is True:
        bstack11111l1l1_opy_ = int(multiprocessing.current_process().name)
      elif bstack1l1l1l11ll_opy_ is True:
        bstack11111l1l1_opy_ = int(threading.current_thread().name)
    except:
      bstack11111l1l1_opy_ = 0
    CONFIG[bstack1l1_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ೔")] = True
    bstack1l11111l1l_opy_ = bstack1ll11lll1_opy_(CONFIG, bstack11111l1l1_opy_)
    logger.debug(bstack11111lll1l_opy_.format(str(bstack1l11111l1l_opy_)))
    if CONFIG.get(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ೕ")):
      bstack11ll111l1l_opy_(bstack1l11111l1l_opy_)
    if bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ೖ") in CONFIG and bstack1l1_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ೗") in CONFIG[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ೘")][bstack11111l1l1_opy_]:
      bstack1l1l111ll1_opy_ = CONFIG[bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ೙")][bstack11111l1l1_opy_][bstack1l1_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ೚")]
    import urllib
    import json
    if bstack1l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ೛") in CONFIG and str(CONFIG[bstack1l1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭೜")]).lower() != bstack1l1_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩೝ"):
        bstack111ll111l1_opy_ = bstack111lll1ll_opy_()
        bstack111l1ll11l_opy_ = bstack111ll111l1_opy_ + urllib.parse.quote(json.dumps(bstack1l11111l1l_opy_))
    else:
        bstack111l1ll11l_opy_ = bstack1l1_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭ೞ") + urllib.parse.quote(json.dumps(bstack1l11111l1l_opy_))
    browser = self.connect(bstack111l1ll11l_opy_)
    return browser
except Exception as e:
    pass
def bstack111l111l1l_opy_():
    global bstack1111lll11l_opy_
    global bstack1l1l11l11l_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1ll1ll1ll1_opy_
        global bstack11l11111_opy_
        if not bstack1ll11ll1ll_opy_:
          global bstack1l1llll111_opy_
          if not bstack1l1llll111_opy_:
            from bstack_utils.helper import bstack1ll111llll_opy_, bstack1ll11l111l_opy_, bstack111llll1l1_opy_
            bstack1l1llll111_opy_ = bstack1ll111llll_opy_()
            bstack1ll11l111l_opy_(bstack1l1l11l11l_opy_)
            bstack11lllllll_opy_ = bstack1l111l111_opy_.bstack1lllll1111_opy_(CONFIG, bstack1l1l11l11l_opy_)
            bstack11l11111_opy_.set_property(bstack1l1_opy_ (u"ࠧࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡓࡖࡔࡊࡕࡄࡖࡢࡑࡆࡖࠢ೟"), bstack11lllllll_opy_)
          BrowserType.connect = bstack1ll1ll1ll1_opy_
          return
        BrowserType.launch = bstack1ll1111ll_opy_
        bstack1111lll11l_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1lll111lll_opy_
      bstack1111lll11l_opy_ = True
    except Exception as e:
      pass
def bstack1ll11ll111_opy_(context, bstack1111ll11l_opy_):
  try:
    context.page.evaluate(bstack1l1_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢೠ"), bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫೡ")+ json.dumps(bstack1111ll11l_opy_) + bstack1l1_opy_ (u"ࠣࡿࢀࠦೢ"))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃ࠺ࠡࡽࢀࠦೣ").format(str(e), traceback.format_exc()))
def bstack1lll111ll1_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1l1_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ೤"), bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ೥") + json.dumps(message) + bstack1l1_opy_ (u"ࠬ࠲ࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠨ೦") + json.dumps(level) + bstack1l1_opy_ (u"࠭ࡽࡾࠩ೧"))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠠࡼࡿ࠽ࠤࢀࢃࠢ೨").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1111l11l1l_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1l1l1l1111_opy_(self, url):
  global bstack1llll1l1l1_opy_
  try:
    bstack11llll1l11_opy_(url)
  except Exception as err:
    logger.debug(bstack1llll11ll1_opy_.format(str(err)))
  try:
    bstack1llll1l1l1_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1ll111l1l1_opy_):
        bstack11llll1l11_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1llll11ll1_opy_.format(str(err)))
    raise e
def bstack1ll1lll1ll_opy_(self):
  global bstack1111ll1l1_opy_
  bstack1111ll1l1_opy_ = self
  return
def bstack111l1ll1l1_opy_(self):
  global bstack11l11l1lll_opy_
  bstack11l11l1lll_opy_ = self
  return
def bstack1l1l1111l_opy_(test_name, bstack111l1111ll_opy_):
  global CONFIG
  if percy.bstack1l11l11l1l_opy_() == bstack1l1_opy_ (u"ࠣࡶࡵࡹࡪࠨ೩"):
    bstack11l11l11l1_opy_ = os.path.relpath(bstack111l1111ll_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack11l11l11l1_opy_)
    bstack1lll1ll111_opy_ = suite_name + bstack1l1_opy_ (u"ࠤ࠰ࠦ೪") + test_name
    threading.current_thread().percySessionName = bstack1lll1ll111_opy_
def bstack1ll1l1ll11_opy_(self, test, *args, **kwargs):
  global bstack1l1l111ll_opy_
  test_name = None
  bstack111l1111ll_opy_ = None
  if test:
    test_name = str(test.name)
    bstack111l1111ll_opy_ = str(test.source)
  bstack1l1l1111l_opy_(test_name, bstack111l1111ll_opy_)
  bstack1l1l111ll_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack11ll1111l_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack111l1lll1l_opy_(driver, bstack1lll1ll111_opy_):
  if not bstack1111llll11_opy_ and bstack1lll1ll111_opy_:
      bstack11lll1l1l_opy_ = {
          bstack1l1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪ೫"): bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ೬"),
          bstack1l1_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ೭"): {
              bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ೮"): bstack1lll1ll111_opy_
          }
      }
      bstack11111l1ll1_opy_ = bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ೯").format(json.dumps(bstack11lll1l1l_opy_))
      driver.execute_script(bstack11111l1ll1_opy_)
  if bstack1l11l1l11l_opy_:
      bstack1l1111l1l_opy_ = {
          bstack1l1_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨ೰"): bstack1l1_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫೱ"),
          bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ೲ"): {
              bstack1l1_opy_ (u"ࠫࡩࡧࡴࡢࠩೳ"): bstack1lll1ll111_opy_ + bstack1l1_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩࠧࠧ೴"),
              bstack1l1_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ೵"): bstack1l1_opy_ (u"ࠧࡪࡰࡩࡳࠬ೶")
          }
      }
      if bstack1l11l1l11l_opy_.status == bstack1l1_opy_ (u"ࠨࡒࡄࡗࡘ࠭೷"):
          bstack1l11ll111_opy_ = bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧ೸").format(json.dumps(bstack1l1111l1l_opy_))
          driver.execute_script(bstack1l11ll111_opy_)
          bstack1l1ll11l11_opy_(driver, bstack1l1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ೹"))
      elif bstack1l11l1l11l_opy_.status == bstack1l1_opy_ (u"ࠫࡋࡇࡉࡍࠩ೺"):
          reason = bstack1l1_opy_ (u"ࠧࠨ೻")
          bstack1111l111l_opy_ = bstack1lll1ll111_opy_ + bstack1l1_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠧ೼")
          if bstack1l11l1l11l_opy_.message:
              reason = str(bstack1l11l1l11l_opy_.message)
              bstack1111l111l_opy_ = bstack1111l111l_opy_ + bstack1l1_opy_ (u"ࠧࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶ࠿ࠦࠧ೽") + reason
          bstack1l1111l1l_opy_[bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ೾")] = {
              bstack1l1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ೿"): bstack1l1_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩഀ"),
              bstack1l1_opy_ (u"ࠫࡩࡧࡴࡢࠩഁ"): bstack1111l111l_opy_
          }
          bstack1l11ll111_opy_ = bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪം").format(json.dumps(bstack1l1111l1l_opy_))
          driver.execute_script(bstack1l11ll111_opy_)
          bstack1l1ll11l11_opy_(driver, bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ഃ"), reason)
          bstack1ll1ll1l1l_opy_(reason, str(bstack1l11l1l11l_opy_), str(bstack1l1l11l1l_opy_), logger)
@measure(event_name=EVENTS.bstack111llll1ll_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1ll1l1l11_opy_(driver, test):
  if percy.bstack1l11l11l1l_opy_() == bstack1l1_opy_ (u"ࠢࡵࡴࡸࡩࠧഄ") and percy.bstack111ll1l111_opy_() == bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥഅ"):
      bstack111l1l1ll1_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬആ"), None)
      bstack11l11111l1_opy_(driver, bstack111l1l1ll1_opy_, test)
  if (bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧഇ"), None) and
      bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪഈ"), None)) or (
      bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬഉ"), None) and
      bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨഊ"), None)):
      logger.info(bstack1l1_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠦࠢഋ"))
      bstack11l1111l_opy_.bstack111ll11l_opy_(driver, name=test.name, path=test.source)
def bstack1l1ll1ll11_opy_(test, bstack1lll1ll111_opy_):
    try:
      bstack1l1ll111l_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ഌ")] = bstack1lll1ll111_opy_
      if bstack1l11l1l11l_opy_:
        if bstack1l11l1l11l_opy_.status == bstack1l1_opy_ (u"ࠩࡓࡅࡘ࡙ࠧ഍"):
          data[bstack1l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪഎ")] = bstack1l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫഏ")
        elif bstack1l11l1l11l_opy_.status == bstack1l1_opy_ (u"ࠬࡌࡁࡊࡎࠪഐ"):
          data[bstack1l1_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭഑")] = bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧഒ")
          if bstack1l11l1l11l_opy_.message:
            data[bstack1l1_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨഓ")] = str(bstack1l11l1l11l_opy_.message)
      user = CONFIG[bstack1l1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫഔ")]
      key = CONFIG[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ക")]
      host = bstack11ll11llll_opy_(cli.config, [bstack1l1_opy_ (u"ࠦࡦࡶࡩࡴࠤഖ"), bstack1l1_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢഗ"), bstack1l1_opy_ (u"ࠨࡡࡱ࡫ࠥഘ")], bstack1l1_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠣങ"))
      url = bstack1l1_opy_ (u"ࠨࡽࢀ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠰ࡽࢀ࠲࡯ࡹ࡯࡯ࠩച").format(host, bstack11lll111l_opy_)
      headers = {
        bstack1l1_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨഛ"): bstack1l1_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ജ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡸࡴࡩࡧࡴࡦࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡷࡥࡹࡻࡳࠣഝ"), datetime.datetime.now() - bstack1l1ll111l_opy_)
    except Exception as e:
      logger.error(bstack1llll1l11l_opy_.format(str(e)))
def bstack1l11llllll_opy_(test, bstack1lll1ll111_opy_):
  global CONFIG
  global bstack11l11l1lll_opy_
  global bstack1111ll1l1_opy_
  global bstack11lll111l_opy_
  global bstack1l11l1l11l_opy_
  global bstack1l1l111ll1_opy_
  global bstack11111ll1ll_opy_
  global bstack1l1l1ll11l_opy_
  global bstack11111l1l11_opy_
  global bstack11lll1l111_opy_
  global bstack11lll11ll_opy_
  global bstack1ll1ll1lll_opy_
  global bstack1l111lll1_opy_
  try:
    if not bstack11lll111l_opy_:
      with bstack1l111lll1_opy_:
        bstack11ll1lllll_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠬࢄࠧഞ")), bstack1l1_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ട"), bstack1l1_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩഠ"))
        if os.path.exists(bstack11ll1lllll_opy_):
          with open(bstack11ll1lllll_opy_, bstack1l1_opy_ (u"ࠨࡴࠪഡ")) as f:
            content = f.read().strip()
            if content:
              bstack111l1llll_opy_ = json.loads(bstack1l1_opy_ (u"ࠤࡾࠦഢ") + content + bstack1l1_opy_ (u"ࠪࠦࡽࠨ࠺ࠡࠤࡼࠦࠬണ") + bstack1l1_opy_ (u"ࠦࢂࠨത"))
              bstack11lll111l_opy_ = bstack111l1llll_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࡵࠣࡪ࡮ࡲࡥ࠻ࠢࠪഥ") + str(e))
  if bstack11lll11ll_opy_:
    with bstack11l1l111l1_opy_:
      bstack1l11111111_opy_ = bstack11lll11ll_opy_.copy()
    for driver in bstack1l11111111_opy_:
      if bstack11lll111l_opy_ == driver.session_id:
        if test:
          bstack1ll1l1l11_opy_(driver, test)
        bstack111l1lll1l_opy_(driver, bstack1lll1ll111_opy_)
  elif bstack11lll111l_opy_:
    bstack1l1ll1ll11_opy_(test, bstack1lll1ll111_opy_)
  if bstack11l11l1lll_opy_:
    bstack1l1l1ll11l_opy_(bstack11l11l1lll_opy_)
  if bstack1111ll1l1_opy_:
    bstack11111l1l11_opy_(bstack1111ll1l1_opy_)
  if bstack1l111l111l_opy_:
    bstack11lll1l111_opy_()
def bstack11l1l111ll_opy_(self, test, *args, **kwargs):
  bstack1lll1ll111_opy_ = None
  if test:
    bstack1lll1ll111_opy_ = str(test.name)
  bstack1l11llllll_opy_(test, bstack1lll1ll111_opy_)
  bstack11111ll1ll_opy_(self, test, *args, **kwargs)
def bstack1l1ll11l1l_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1ll1l1l1l_opy_
  global CONFIG
  global bstack11lll11ll_opy_
  global bstack11lll111l_opy_
  global bstack1l111lll1_opy_
  bstack1l1ll1l1ll_opy_ = None
  try:
    if bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬദ"), None) or bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩധ"), None):
      try:
        if not bstack11lll111l_opy_:
          bstack11ll1lllll_opy_ = os.path.join(os.path.expanduser(bstack1l1_opy_ (u"ࠨࢀࠪന")), bstack1l1_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩഩ"), bstack1l1_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬപ"))
          with bstack1l111lll1_opy_:
            if os.path.exists(bstack11ll1lllll_opy_):
              with open(bstack11ll1lllll_opy_, bstack1l1_opy_ (u"ࠫࡷ࠭ഫ")) as f:
                content = f.read().strip()
                if content:
                  bstack111l1llll_opy_ = json.loads(bstack1l1_opy_ (u"ࠧࢁࠢബ") + content + bstack1l1_opy_ (u"࠭ࠢࡹࠤ࠽ࠤࠧࡿࠢࠨഭ") + bstack1l1_opy_ (u"ࠢࡾࠤമ"))
                  bstack11lll111l_opy_ = bstack111l1llll_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡌࡈࡸࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠧയ") + str(e))
      if bstack11lll11ll_opy_:
        with bstack11l1l111l1_opy_:
          bstack1l11111111_opy_ = bstack11lll11ll_opy_.copy()
        for driver in bstack1l11111111_opy_:
          if bstack11lll111l_opy_ == driver.session_id:
            bstack1l1ll1l1ll_opy_ = driver
    bstack11l1l1l1l_opy_ = bstack11l1111l_opy_.bstack1lll1111ll_opy_(test.tags)
    if bstack1l1ll1l1ll_opy_:
      threading.current_thread().isA11yTest = bstack11l1111l_opy_.bstack1l111111l_opy_(bstack1l1ll1l1ll_opy_, bstack11l1l1l1l_opy_)
      threading.current_thread().isAppA11yTest = bstack11l1111l_opy_.bstack1l111111l_opy_(bstack1l1ll1l1ll_opy_, bstack11l1l1l1l_opy_)
    else:
      threading.current_thread().isA11yTest = bstack11l1l1l1l_opy_
      threading.current_thread().isAppA11yTest = bstack11l1l1l1l_opy_
  except:
    pass
  bstack1ll1l1l1l_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1l11l1l11l_opy_
  try:
    bstack1l11l1l11l_opy_ = self._test
  except:
    bstack1l11l1l11l_opy_ = self.test
def bstack11l111lll_opy_():
  global bstack1111l111l1_opy_
  try:
    if os.path.exists(bstack1111l111l1_opy_):
      os.remove(bstack1111l111l1_opy_)
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬര") + str(e))
def bstack111ll11l11_opy_():
  global bstack1111l111l1_opy_
  bstack11l11ll1l1_opy_ = {}
  lock_file = bstack1111l111l1_opy_ + bstack1l1_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩറ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧല"))
    try:
      if not os.path.isfile(bstack1111l111l1_opy_):
        with open(bstack1111l111l1_opy_, bstack1l1_opy_ (u"ࠬࡽࠧള")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1111l111l1_opy_):
        with open(bstack1111l111l1_opy_, bstack1l1_opy_ (u"࠭ࡲࠨഴ")) as f:
          content = f.read().strip()
          if content:
            bstack11l11ll1l1_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩവ") + str(e))
    return bstack11l11ll1l1_opy_
  try:
    os.makedirs(os.path.dirname(bstack1111l111l1_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack1111l111l1_opy_):
        with open(bstack1111l111l1_opy_, bstack1l1_opy_ (u"ࠨࡹࠪശ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1111l111l1_opy_):
        with open(bstack1111l111l1_opy_, bstack1l1_opy_ (u"ࠩࡵࠫഷ")) as f:
          content = f.read().strip()
          if content:
            bstack11l11ll1l1_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬസ") + str(e))
  finally:
    return bstack11l11ll1l1_opy_
def bstack11ll1l11l_opy_(platform_index, item_index):
  global bstack1111l111l1_opy_
  lock_file = bstack1111l111l1_opy_ + bstack1l1_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪഹ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨഺ"))
    try:
      bstack11l11ll1l1_opy_ = {}
      if os.path.exists(bstack1111l111l1_opy_):
        with open(bstack1111l111l1_opy_, bstack1l1_opy_ (u"࠭ࡲࠨ഻")) as f:
          content = f.read().strip()
          if content:
            bstack11l11ll1l1_opy_ = json.loads(content)
      bstack11l11ll1l1_opy_[item_index] = platform_index
      with open(bstack1111l111l1_opy_, bstack1l1_opy_ (u"ࠢࡸࠤ഼")) as outfile:
        json.dump(bstack11l11ll1l1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡻࡷ࡯ࡴࡪࡰࡪࠤࡹࡵࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ഽ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack1111l111l1_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack11l11ll1l1_opy_ = {}
      if os.path.exists(bstack1111l111l1_opy_):
        with open(bstack1111l111l1_opy_, bstack1l1_opy_ (u"ࠩࡵࠫാ")) as f:
          content = f.read().strip()
          if content:
            bstack11l11ll1l1_opy_ = json.loads(content)
      bstack11l11ll1l1_opy_[item_index] = platform_index
      with open(bstack1111l111l1_opy_, bstack1l1_opy_ (u"ࠥࡻࠧി")) as outfile:
        json.dump(bstack11l11ll1l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡷࡳ࡫ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩീ") + str(e))
def bstack1ll111l111_opy_(bstack1l11llll11_opy_):
  global CONFIG
  bstack11l1ll1ll1_opy_ = bstack1l1_opy_ (u"ࠬ࠭ു")
  if not bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩൂ") in CONFIG:
    logger.info(bstack1l1_opy_ (u"ࠧࡏࡱࠣࡴࡱࡧࡴࡧࡱࡵࡱࡸࠦࡰࡢࡵࡶࡩࡩࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫ࡵࡲࠡࡔࡲࡦࡴࡺࠠࡳࡷࡱࠫൃ"))
  try:
    platform = CONFIG[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫൄ")][bstack1l11llll11_opy_]
    if bstack1l1_opy_ (u"ࠩࡲࡷࠬ൅") in platform:
      bstack11l1ll1ll1_opy_ += str(platform[bstack1l1_opy_ (u"ࠪࡳࡸ࠭െ")]) + bstack1l1_opy_ (u"ࠫ࠱ࠦࠧേ")
    if bstack1l1_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨൈ") in platform:
      bstack11l1ll1ll1_opy_ += str(platform[bstack1l1_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ൉")]) + bstack1l1_opy_ (u"ࠧ࠭ࠢࠪൊ")
    if bstack1l1_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬോ") in platform:
      bstack11l1ll1ll1_opy_ += str(platform[bstack1l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ൌ")]) + bstack1l1_opy_ (u"ࠪ࠰്ࠥ࠭")
    if bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ൎ") in platform:
      bstack11l1ll1ll1_opy_ += str(platform[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ൏")]) + bstack1l1_opy_ (u"࠭ࠬࠡࠩ൐")
    if bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ൑") in platform:
      bstack11l1ll1ll1_opy_ += str(platform[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭൒")]) + bstack1l1_opy_ (u"ࠩ࠯ࠤࠬ൓")
    if bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫൔ") in platform:
      bstack11l1ll1ll1_opy_ += str(platform[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬൕ")]) + bstack1l1_opy_ (u"ࠬ࠲ࠠࠨൖ")
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"࠭ࡓࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡰࡨࡶࡦࡺࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡹࡴࡳ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡵࡩࡵࡵࡲࡵࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡳࡳ࠭ൗ") + str(e))
  finally:
    if bstack11l1ll1ll1_opy_[len(bstack11l1ll1ll1_opy_) - 2:] == bstack1l1_opy_ (u"ࠧ࠭ࠢࠪ൘"):
      bstack11l1ll1ll1_opy_ = bstack11l1ll1ll1_opy_[:-2]
    return bstack11l1ll1ll1_opy_
def bstack1l1l1111ll_opy_(path, bstack11l1ll1ll1_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack11l1ll1lll_opy_ = ET.parse(path)
    bstack1ll1l1l1ll_opy_ = bstack11l1ll1lll_opy_.getroot()
    bstack11111ll11_opy_ = None
    for suite in bstack1ll1l1l1ll_opy_.iter(bstack1l1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧ൙")):
      if bstack1l1_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ൚") in suite.attrib:
        suite.attrib[bstack1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨ൛")] += bstack1l1_opy_ (u"ࠫࠥ࠭൜") + bstack11l1ll1ll1_opy_
        bstack11111ll11_opy_ = suite
    bstack11111l1lll_opy_ = None
    for robot in bstack1ll1l1l1ll_opy_.iter(bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ൝")):
      bstack11111l1lll_opy_ = robot
    bstack111llllll1_opy_ = len(bstack11111l1lll_opy_.findall(bstack1l1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൞")))
    if bstack111llllll1_opy_ == 1:
      bstack11111l1lll_opy_.remove(bstack11111l1lll_opy_.findall(bstack1l1_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ൟ"))[0])
      bstack1llllll11l_opy_ = ET.Element(bstack1l1_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧൠ"), attrib={bstack1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧൡ"): bstack1l1_opy_ (u"ࠪࡗࡺ࡯ࡴࡦࡵࠪൢ"), bstack1l1_opy_ (u"ࠫ࡮ࡪࠧൣ"): bstack1l1_opy_ (u"ࠬࡹ࠰ࠨ൤")})
      bstack11111l1lll_opy_.insert(1, bstack1llllll11l_opy_)
      bstack1llll11l11_opy_ = None
      for suite in bstack11111l1lll_opy_.iter(bstack1l1_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൥")):
        bstack1llll11l11_opy_ = suite
      bstack1llll11l11_opy_.append(bstack11111ll11_opy_)
      bstack11ll111ll1_opy_ = None
      for status in bstack11111ll11_opy_.iter(bstack1l1_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ൦")):
        bstack11ll111ll1_opy_ = status
      bstack1llll11l11_opy_.append(bstack11ll111ll1_opy_)
    bstack11l1ll1lll_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡸࡳࡪࡰࡪࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹ࠭൧") + str(e))
def bstack1l111lllll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1l1lllll1l_opy_
  global CONFIG
  if bstack1l1_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨ൨") in options:
    del options[bstack1l1_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢ൩")]
  json_data = bstack111ll11l11_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack1l1_opy_ (u"ࠫࡵࡧࡢࡰࡶࡢࡶࡪࡹࡵ࡭ࡶࡶࠫ൪"), str(item_id), bstack1l1_opy_ (u"ࠬࡵࡵࡵࡲࡸࡸ࠳ࡾ࡭࡭ࠩ൫"))
    bstack1l1l1111ll_opy_(path, bstack1ll111l111_opy_(json_data[item_id]))
  bstack11l111lll_opy_()
  return bstack1l1lllll1l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack11l1l1l11l_opy_(self, ff_profile_dir):
  global bstack1ll1ll111l_opy_
  if not ff_profile_dir:
    return None
  return bstack1ll1ll111l_opy_(self, ff_profile_dir)
def bstack1ll11l11l_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l11lll1l_opy_
  bstack11l1l1l1ll_opy_ = []
  if bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ൬") in CONFIG:
    bstack11l1l1l1ll_opy_ = CONFIG[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ൭")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1l1_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࠤ൮")],
      pabot_args[bstack1l1_opy_ (u"ࠤࡹࡩࡷࡨ࡯ࡴࡧࠥ൯")],
      argfile,
      pabot_args.get(bstack1l1_opy_ (u"ࠥ࡬࡮ࡼࡥࠣ൰")),
      pabot_args[bstack1l1_opy_ (u"ࠦࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠢ൱")],
      platform[0],
      bstack1l11lll1l_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1l1_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡦࡪ࡮ࡨࡷࠧ൲")] or [(bstack1l1_opy_ (u"ࠨࠢ൳"), None)]
    for platform in enumerate(bstack11l1l1l1ll_opy_)
  ]
def bstack1l1lll1ll1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack11l1llllll_opy_=bstack1l1_opy_ (u"ࠧࠨ൴")):
  global bstack1l111111ll_opy_
  self.platform_index = platform_index
  self.bstack1l1ll1l11_opy_ = bstack11l1llllll_opy_
  bstack1l111111ll_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1ll1l1111_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1lll11l11l_opy_
  global bstack11l1l1lll1_opy_
  bstack11lll111ll_opy_ = copy.deepcopy(item)
  if not bstack1l1_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ൵") in item.options:
    bstack11lll111ll_opy_.options[bstack1l1_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ൶")] = []
  bstack1111lllll_opy_ = bstack11lll111ll_opy_.options[bstack1l1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ൷")].copy()
  for v in bstack11lll111ll_opy_.options[bstack1l1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭൸")]:
    if bstack1l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫ൹") in v:
      bstack1111lllll_opy_.remove(v)
    if bstack1l1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭ൺ") in v:
      bstack1111lllll_opy_.remove(v)
    if bstack1l1_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫൻ") in v:
      bstack1111lllll_opy_.remove(v)
  bstack1111lllll_opy_.insert(0, bstack1l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞࠺ࡼࡿࠪർ").format(bstack11lll111ll_opy_.platform_index))
  bstack1111lllll_opy_.insert(0, bstack1l1_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࡀࡻࡾࠩൽ").format(bstack11lll111ll_opy_.bstack1l1ll1l11_opy_))
  bstack11lll111ll_opy_.options[bstack1l1_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬൾ")] = bstack1111lllll_opy_
  if bstack11l1l1lll1_opy_:
    bstack11lll111ll_opy_.options[bstack1l1_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ൿ")].insert(0, bstack1l1_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗ࠿ࢁࡽࠨ඀").format(bstack11l1l1lll1_opy_))
  return bstack1lll11l11l_opy_(caller_id, datasources, is_last, bstack11lll111ll_opy_, outs_dir)
def bstack1lllll111l_opy_(command, item_index):
  try:
    if bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧඁ")):
      os.environ[bstack1l1_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨං")] = json.dumps(CONFIG[bstack1l1_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫඃ")][item_index % bstack11l1l111l_opy_])
    global bstack11l1l1lll1_opy_
    if bstack11l1l1lll1_opy_:
      command[0] = command[0].replace(bstack1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ඄"), bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧඅ") + str(
        item_index) + bstack1l1_opy_ (u"ࠫࠥ࠭ආ") + bstack11l1l1lll1_opy_, 1)
    else:
      command[0] = command[0].replace(bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫඇ"),
                                      bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡹࡤ࡬ࠢࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠢࠪඈ") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦ࡭ࡰࡦ࡬ࡪࡾ࡯࡮ࡨࠢࡦࡳࡲࡳࡡ࡯ࡦࠣࡪࡴࡸࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰ࠽ࠤࢀࢃࠧඉ").format(str(e)))
def bstack1ll1l1llll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack11l1ll111l_opy_
  try:
    bstack1lllll111l_opy_(command, item_index)
    return bstack11l1ll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࡀࠠࡼࡿࠪඊ").format(str(e)))
    raise e
def bstack11111lll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack11l1ll111l_opy_
  try:
    bstack1lllll111l_opy_(command, item_index)
    return bstack11l1ll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠳࠰࠴࠷࠿ࠦࡻࡾࠩඋ").format(str(e)))
    try:
      return bstack11l1ll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack1l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࠷࠴࠱࠴ࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨඌ").format(str(e2)))
      raise e
def bstack11111l11l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack11l1ll111l_opy_
  try:
    bstack1lllll111l_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack11l1ll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠵࠲࠶࠻࠺ࠡࡽࢀࠫඍ").format(str(e)))
    try:
      return bstack11l1ll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack1l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦ࠲࠯࠳࠸ࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪඎ").format(str(e2)))
      raise e
def _1l1l1lll1_opy_(bstack1lll11llll_opy_, item_index, process_timeout, sleep_before_start, bstack1l1l1ll111_opy_):
  bstack1lllll111l_opy_(bstack1lll11llll_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack11llll11ll_opy_(command, bstack1l1lll1l1l_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11l1ll111l_opy_
  try:
    bstack1lllll111l_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack11l1ll111l_opy_(command, bstack1l1lll1l1l_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠺࠴࠰࠻ࠢࡾࢁࠬඏ").format(str(e)))
    try:
      return bstack11l1ll111l_opy_(command, bstack1l1lll1l1l_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧඐ").format(str(e2)))
      raise e
def bstack1l1l11llll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11l1ll111l_opy_
  try:
    process_timeout = _1l1l1lll1_opy_(command, item_index, process_timeout, sleep_before_start, bstack1l1_opy_ (u"ࠨ࠶࠱࠶ࠬඑ"))
    return bstack11l1ll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠵࠰࠵࠾ࠥࢁࡽࠨඒ").format(str(e)))
    try:
      return bstack11l1ll111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪඓ").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack11l111l111_opy_(self, runner, quiet=False, capture=True):
  global bstack1l11l1ll1l_opy_
  bstack1111ll1111_opy_ = bstack1l11l1ll1l_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack1l1_opy_ (u"ࠫࡪࡾࡣࡦࡲࡷ࡭ࡴࡴ࡟ࡢࡴࡵࠫඔ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1l1_opy_ (u"ࠬ࡫ࡸࡤࡡࡷࡶࡦࡩࡥࡣࡣࡦ࡯ࡤࡧࡲࡳࠩඕ")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1111ll1111_opy_
def bstack1l1llll1l1_opy_(runner, hook_name, context, element, bstack11l11ll1l_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack111l1llll1_opy_.bstack11l11lll_opy_(hook_name, element)
    bstack11l11ll1l_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack111l1llll1_opy_.bstack11l1lll1_opy_(element)
      if hook_name not in [bstack1l1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪඖ"), bstack1l1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪ඗")] and args and hasattr(args[0], bstack1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠨ඘")):
        args[0].error_message = bstack1l1_opy_ (u"ࠩࠪ඙")
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡨࡢࡰࡧࡰࡪࠦࡨࡰࡱ࡮ࡷࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥ࠻ࠢࡾࢁࠬක").format(str(e)))
@measure(event_name=EVENTS.bstack1l1l1l11l_opy_, stage=STAGE.bstack1lllll1l1l_opy_, hook_type=bstack1l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡅࡱࡲࠢඛ"), bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1llll1lll1_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    if runner.hooks.get(bstack1l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤග")).__name__ != bstack1l1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࡢࡨࡪ࡬ࡡࡶ࡮ࡷࡣ࡭ࡵ࡯࡬ࠤඝ"):
      bstack1l1llll1l1_opy_(runner, name, context, runner, bstack11l11ll1l_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack11llll1ll1_opy_(bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ඞ")) else context.browser
      runner.driver_initialised = bstack1l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧඟ")
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡪࠦࡡࡵࡶࡵ࡭ࡧࡻࡴࡦ࠼ࠣࡿࢂ࠭ච").format(str(e)))
def bstack111l11l111_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    bstack1l1llll1l1_opy_(runner, name, context, context.feature, bstack11l11ll1l_opy_, *args)
    try:
      if not bstack1111llll11_opy_:
        bstack1l1ll1l1ll_opy_ = threading.current_thread().bstackSessionDriver if bstack11llll1ll1_opy_(bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩඡ")) else context.browser
        if is_driver_active(bstack1l1ll1l1ll_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack1l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧජ")
          bstack1111ll11l_opy_ = str(runner.feature.name)
          bstack1ll11ll111_opy_(context, bstack1111ll11l_opy_)
          bstack1l1ll1l1ll_opy_.execute_script(bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪඣ") + json.dumps(bstack1111ll11l_opy_) + bstack1l1_opy_ (u"࠭ࡽࡾࠩඤ"))
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧඥ").format(str(e)))
def bstack1lll1l1111_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    if hasattr(context, bstack1l1_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪඦ")):
        bstack111l1llll1_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack1l1_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫට")) else context.feature
    bstack1l1llll1l1_opy_(runner, name, context, target, bstack11l11ll1l_opy_, *args)
@measure(event_name=EVENTS.bstack111111l1l_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1111ll1l11_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    if len(context.scenario.tags) == 0: bstack111l1llll1_opy_.start_test(context)
    bstack1l1llll1l1_opy_(runner, name, context, context.scenario, bstack11l11ll1l_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack11l111ll1_opy_.bstack1l11l111ll_opy_(context, *args)
    try:
      bstack1l1ll1l1ll_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩඨ"), context.browser)
      if is_driver_active(bstack1l1ll1l1ll_opy_):
        bstack1l11llll_opy_.bstack1l1lll111l_opy_(bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪඩ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack1l1_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢඪ")
        if (not bstack1111llll11_opy_):
          scenario_name = args[0].name
          feature_name = bstack1111ll11l_opy_ = str(runner.feature.name)
          bstack1111ll11l_opy_ = feature_name + bstack1l1_opy_ (u"࠭ࠠ࠮ࠢࠪණ") + scenario_name
          if runner.driver_initialised == bstack1l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤඬ"):
            bstack1ll11ll111_opy_(context, bstack1111ll11l_opy_)
            bstack1l1ll1l1ll_opy_.execute_script(bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭ත") + json.dumps(bstack1111ll11l_opy_) + bstack1l1_opy_ (u"ࠩࢀࢁࠬථ"))
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡦࡰࡤࡶ࡮ࡵ࠺ࠡࡽࢀࠫද").format(str(e)))
@measure(event_name=EVENTS.bstack1l1l1l11l_opy_, stage=STAGE.bstack1lllll1l1l_opy_, hook_type=bstack1l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡗࡹ࡫ࡰࠣධ"), bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1ll11l11ll_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    bstack1l1llll1l1_opy_(runner, name, context, args[0], bstack11l11ll1l_opy_, *args)
    try:
      bstack1l1ll1l1ll_opy_ = threading.current_thread().bstackSessionDriver if bstack11llll1ll1_opy_(bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫන")) else context.browser
      if is_driver_active(bstack1l1ll1l1ll_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack1l1_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦ඲")
        bstack111l1llll1_opy_.bstack11l11l11_opy_(args[0])
        if runner.driver_initialised == bstack1l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧඳ"):
          feature_name = bstack1111ll11l_opy_ = str(runner.feature.name)
          bstack1111ll11l_opy_ = feature_name + bstack1l1_opy_ (u"ࠨࠢ࠰ࠤࠬප") + context.scenario.name
          bstack1l1ll1l1ll_opy_.execute_script(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧඵ") + json.dumps(bstack1111ll11l_opy_) + bstack1l1_opy_ (u"ࠪࢁࢂ࠭බ"))
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡵࡧࡳ࠾ࠥࢁࡽࠨභ").format(str(e)))
@measure(event_name=EVENTS.bstack1l1l1l11l_opy_, stage=STAGE.bstack1lllll1l1l_opy_, hook_type=bstack1l1_opy_ (u"ࠧࡧࡦࡵࡧࡵࡗࡹ࡫ࡰࠣම"), bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1ll1l11l1l_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
  bstack111l1llll1_opy_.bstack11l1ll11_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack1l1ll1l1ll_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬඹ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1l1ll1l1ll_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack1l1_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧය")
        feature_name = bstack1111ll11l_opy_ = str(runner.feature.name)
        bstack1111ll11l_opy_ = feature_name + bstack1l1_opy_ (u"ࠨࠢ࠰ࠤࠬර") + context.scenario.name
        bstack1l1ll1l1ll_opy_.execute_script(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧ඼") + json.dumps(bstack1111ll11l_opy_) + bstack1l1_opy_ (u"ࠪࢁࢂ࠭ල"))
    if str(step_status).lower() == bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ඾"):
      bstack1ll1llllll_opy_ = bstack1l1_opy_ (u"ࠬ࠭඿")
      bstack11l1ll111_opy_ = bstack1l1_opy_ (u"࠭ࠧව")
      bstack111l11llll_opy_ = bstack1l1_opy_ (u"ࠧࠨශ")
      try:
        import traceback
        bstack1ll1llllll_opy_ = runner.exception.__class__.__name__
        bstack11l1l111_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11l1ll111_opy_ = bstack1l1_opy_ (u"ࠨࠢࠪෂ").join(bstack11l1l111_opy_)
        bstack111l11llll_opy_ = bstack11l1l111_opy_[-1]
      except Exception as e:
        logger.debug(bstack11l1111lll_opy_.format(str(e)))
      bstack1ll1llllll_opy_ += bstack111l11llll_opy_
      bstack1lll111ll1_opy_(context, json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣස") + str(bstack11l1ll111_opy_)),
                          bstack1l1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤහ"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤළ"):
        bstack1ll1ll1l11_opy_(getattr(context, bstack1l1_opy_ (u"ࠬࡶࡡࡨࡧࠪෆ"), None), bstack1l1_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ෇"), bstack1ll1llllll_opy_)
        bstack1l1ll1l1ll_opy_.execute_script(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ෈") + json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢ෉") + str(bstack11l1ll111_opy_)) + bstack1l1_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࡽࡾ්ࠩ"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣ෋"):
        bstack1l1ll11l11_opy_(bstack1l1ll1l1ll_opy_, bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ෌"), bstack1l1_opy_ (u"࡙ࠧࡣࡦࡰࡤࡶ࡮ࡵࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤ෍") + str(bstack1ll1llllll_opy_))
    else:
      bstack1lll111ll1_opy_(context, bstack1l1_opy_ (u"ࠨࡐࡢࡵࡶࡩࡩࠧࠢ෎"), bstack1l1_opy_ (u"ࠢࡪࡰࡩࡳࠧා"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨැ"):
        bstack1ll1ll1l11_opy_(getattr(context, bstack1l1_opy_ (u"ࠩࡳࡥ࡬࡫ࠧෑ"), None), bstack1l1_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥි"))
      bstack1l1ll1l1ll_opy_.execute_script(bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩී") + json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠧࠦ࠭ࠡࡒࡤࡷࡸ࡫ࡤࠢࠤු")) + bstack1l1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬ෕"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧූ"):
        bstack1l1ll11l11_opy_(bstack1l1ll1l1ll_opy_, bstack1l1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ෗"))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡳࡵࡧࡳ࠾ࠥࢁࡽࠨෘ").format(str(e)))
  bstack1l1llll1l1_opy_(runner, name, context, args[0], bstack11l11ll1l_opy_, *args)
@measure(event_name=EVENTS.bstack111l1lll11_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1l1lll1l11_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
  bstack111l1llll1_opy_.end_test(args[0])
  try:
    bstack1lll1l11ll_opy_ = args[0].status.name
    bstack1l1ll1l1ll_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩෙ"), context.browser)
    bstack11l111ll1_opy_.bstack1l1llllll1_opy_(bstack1l1ll1l1ll_opy_)
    if str(bstack1lll1l11ll_opy_).lower() == bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫේ"):
      bstack1ll1llllll_opy_ = bstack1l1_opy_ (u"ࠬ࠭ෛ")
      bstack11l1ll111_opy_ = bstack1l1_opy_ (u"࠭ࠧො")
      bstack111l11llll_opy_ = bstack1l1_opy_ (u"ࠧࠨෝ")
      try:
        import traceback
        bstack1ll1llllll_opy_ = runner.exception.__class__.__name__
        bstack11l1l111_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11l1ll111_opy_ = bstack1l1_opy_ (u"ࠨࠢࠪෞ").join(bstack11l1l111_opy_)
        bstack111l11llll_opy_ = bstack11l1l111_opy_[-1]
      except Exception as e:
        logger.debug(bstack11l1111lll_opy_.format(str(e)))
      bstack1ll1llllll_opy_ += bstack111l11llll_opy_
      bstack1lll111ll1_opy_(context, json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣෟ") + str(bstack11l1ll111_opy_)),
                          bstack1l1_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ෠"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ෡") or runner.driver_initialised == bstack1l1_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ෢"):
        bstack1ll1ll1l11_opy_(getattr(context, bstack1l1_opy_ (u"࠭ࡰࡢࡩࡨࠫ෣"), None), bstack1l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ෤"), bstack1ll1llllll_opy_)
        bstack1l1ll1l1ll_opy_.execute_script(bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭෥") + json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣ෦") + str(bstack11l1ll111_opy_)) + bstack1l1_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪ෧"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ෨") or runner.driver_initialised == bstack1l1_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ෩"):
        bstack1l1ll11l11_opy_(bstack1l1ll1l1ll_opy_, bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭෪"), bstack1l1_opy_ (u"ࠢࡔࡥࡨࡲࡦࡸࡩࡰࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦ෫") + str(bstack1ll1llllll_opy_))
    else:
      bstack1lll111ll1_opy_(context, bstack1l1_opy_ (u"ࠣࡒࡤࡷࡸ࡫ࡤࠢࠤ෬"), bstack1l1_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢ෭"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ෮") or runner.driver_initialised == bstack1l1_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫ෯"):
        bstack1ll1ll1l11_opy_(getattr(context, bstack1l1_opy_ (u"ࠬࡶࡡࡨࡧࠪ෰"), None), bstack1l1_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ෱"))
      bstack1l1ll1l1ll_opy_.execute_script(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬෲ") + json.dumps(str(args[0].name) + bstack1l1_opy_ (u"ࠣࠢ࠰ࠤࡕࡧࡳࡴࡧࡧࠥࠧෳ")) + bstack1l1_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧࢃࡽࠨ෴"))
      if runner.driver_initialised == bstack1l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ෵") or runner.driver_initialised == bstack1l1_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫ෶"):
        bstack1l1ll11l11_opy_(bstack1l1ll1l1ll_opy_, bstack1l1_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ෷"))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨ෸").format(str(e)))
  bstack1l1llll1l1_opy_(runner, name, context, context.scenario, bstack11l11ll1l_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1l1l1lll11_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    target = context.scenario if hasattr(context, bstack1l1_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩ෹")) else context.feature
    bstack1l1llll1l1_opy_(runner, name, context, target, bstack11l11ll1l_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack11lll11l11_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    try:
      bstack1l1ll1l1ll_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧ෺"), context.browser)
      bstack1111lll11_opy_ = bstack1l1_opy_ (u"ࠩࠪ෻")
      if context.failed is True:
        bstack11lll1l11l_opy_ = []
        bstack1lll111l11_opy_ = []
        bstack1l1ll1l1l_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack11lll1l11l_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l1l111_opy_ = traceback.format_tb(exc_tb)
            bstack1111ll11l1_opy_ = bstack1l1_opy_ (u"ࠪࠤࠬ෼").join(bstack11l1l111_opy_)
            bstack1lll111l11_opy_.append(bstack1111ll11l1_opy_)
            bstack1l1ll1l1l_opy_.append(bstack11l1l111_opy_[-1])
        except Exception as e:
          logger.debug(bstack11l1111lll_opy_.format(str(e)))
        bstack1ll1llllll_opy_ = bstack1l1_opy_ (u"ࠫࠬ෽")
        for i in range(len(bstack11lll1l11l_opy_)):
          bstack1ll1llllll_opy_ += bstack11lll1l11l_opy_[i] + bstack1l1ll1l1l_opy_[i] + bstack1l1_opy_ (u"ࠬࡢ࡮ࠨ෾")
        bstack1111lll11_opy_ = bstack1l1_opy_ (u"࠭ࠠࠨ෿").join(bstack1lll111l11_opy_)
        if runner.driver_initialised in [bstack1l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣ฀"), bstack1l1_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧก")]:
          bstack1lll111ll1_opy_(context, bstack1111lll11_opy_, bstack1l1_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣข"))
          bstack1ll1ll1l11_opy_(getattr(context, bstack1l1_opy_ (u"ࠪࡴࡦ࡭ࡥࠨฃ"), None), bstack1l1_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦค"), bstack1ll1llllll_opy_)
          bstack1l1ll1l1ll_opy_.execute_script(bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪฅ") + json.dumps(bstack1111lll11_opy_) + bstack1l1_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭ฆ"))
          bstack1l1ll11l11_opy_(bstack1l1ll1l1ll_opy_, bstack1l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢง"), bstack1l1_opy_ (u"ࠣࡕࡲࡱࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯ࡴࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡠࡳࠨจ") + str(bstack1ll1llllll_opy_))
          bstack1l11111ll1_opy_ = bstack11l1ll11l_opy_(bstack1111lll11_opy_, runner.feature.name, logger)
          if (bstack1l11111ll1_opy_ != None):
            bstack11ll11ll11_opy_.append(bstack1l11111ll1_opy_)
      else:
        if runner.driver_initialised in [bstack1l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥฉ"), bstack1l1_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢช")]:
          bstack1lll111ll1_opy_(context, bstack1l1_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢซ") + str(runner.feature.name) + bstack1l1_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢฌ"), bstack1l1_opy_ (u"ࠨࡩ࡯ࡨࡲࠦญ"))
          bstack1ll1ll1l11_opy_(getattr(context, bstack1l1_opy_ (u"ࠧࡱࡣࡪࡩࠬฎ"), None), bstack1l1_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣฏ"))
          bstack1l1ll1l1ll_opy_.execute_script(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧฐ") + json.dumps(bstack1l1_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨ࠾ࠥࠨฑ") + str(runner.feature.name) + bstack1l1_opy_ (u"ࠦࠥࡶࡡࡴࡵࡨࡨࠦࠨฒ")) + bstack1l1_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫณ"))
          bstack1l1ll11l11_opy_(bstack1l1ll1l1ll_opy_, bstack1l1_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ด"))
          bstack1l11111ll1_opy_ = bstack11l1ll11l_opy_(bstack1111lll11_opy_, runner.feature.name, logger)
          if (bstack1l11111ll1_opy_ != None):
            bstack11ll11ll11_opy_.append(bstack1l11111ll1_opy_)
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩต").format(str(e)))
    bstack1l1llll1l1_opy_(runner, name, context, context.feature, bstack11l11ll1l_opy_, *args)
@measure(event_name=EVENTS.bstack1l1l1l11l_opy_, stage=STAGE.bstack1lllll1l1l_opy_, hook_type=bstack1l1_opy_ (u"ࠣࡣࡩࡸࡪࡸࡁ࡭࡮ࠥถ"), bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1l1l11111l_opy_(runner, name, context, bstack11l11ll1l_opy_, *args):
    bstack1l1llll1l1_opy_(runner, name, context, runner, bstack11l11ll1l_opy_, *args)
def bstack1ll1l11l1_opy_(self, name, context, *args):
  try:
    if bstack1ll11ll1ll_opy_:
      platform_index = int(threading.current_thread()._name) % bstack11l1l111l_opy_
      bstack11llll1lll_opy_ = CONFIG[bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬท")][platform_index]
      os.environ[bstack1l1_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫธ")] = json.dumps(bstack11llll1lll_opy_)
    global bstack11l11ll1l_opy_
    if not hasattr(self, bstack1l1_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡥࡥࠩน")):
      self.driver_initialised = None
    bstack1ll11lllll_opy_ = {
        bstack1l1_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠩบ"): bstack1llll1lll1_opy_,
        bstack1l1_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠧป"): bstack111l11l111_opy_,
        bstack1l1_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡵࡣࡪࠫผ"): bstack1lll1l1111_opy_,
        bstack1l1_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪฝ"): bstack1111ll1l11_opy_,
        bstack1l1_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠧพ"): bstack1ll11l11ll_opy_,
        bstack1l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡸࡪࡶࠧฟ"): bstack1ll1l11l1l_opy_,
        bstack1l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬภ"): bstack1l1lll1l11_opy_,
        bstack1l1_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡹࡧࡧࠨม"): bstack1l1l1lll11_opy_,
        bstack1l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ย"): bstack11lll11l11_opy_,
        bstack1l1_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪร"): bstack1l1l11111l_opy_
    }
    handler = bstack1ll11lllll_opy_.get(name, bstack11l11ll1l_opy_)
    try:
      handler(self, name, context, bstack11l11ll1l_opy_, *args)
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧࠣ࡬ࡴࡵ࡫ࠡࡪࡤࡲࡩࡲࡥࡳࠢࡾࢁ࠿ࠦࡻࡾࠩฤ").format(name, str(e)))
    if name in [bstack1l1_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩล"), bstack1l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫฦ"), bstack1l1_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧว")]:
      try:
        bstack1l1ll1l1ll_opy_ = threading.current_thread().bstackSessionDriver if bstack11llll1ll1_opy_(bstack1l1_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫศ")) else context.browser
        bstack1111l111ll_opy_ = (
          (name == bstack1l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩษ") and self.driver_initialised == bstack1l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦส")) or
          (name == bstack1l1_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨห") and self.driver_initialised == bstack1l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥฬ")) or
          (name == bstack1l1_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫอ") and self.driver_initialised in [bstack1l1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨฮ"), bstack1l1_opy_ (u"ࠧ࡯࡮ࡴࡶࡨࡴࠧฯ")]) or
          (name == bstack1l1_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡴࡦࡲࠪะ") and self.driver_initialised == bstack1l1_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧั"))
        )
        if bstack1111l111ll_opy_:
          self.driver_initialised = None
          if bstack1l1ll1l1ll_opy_ and hasattr(bstack1l1ll1l1ll_opy_, bstack1l1_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠬา")):
            try:
              bstack1l1ll1l1ll_opy_.quit()
            except Exception as e:
              logger.debug(bstack1l1_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡳࡸ࡭ࡹࡺࡩ࡯ࡩࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࠦࡨࡰࡱ࡮࠾ࠥࢁࡽࠨำ").format(str(e)))
      except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡭ࡵ࡯࡬ࠢࡦࡰࡪࡧ࡮ࡶࡲࠣࡪࡴࡸࠠࡼࡿ࠽ࠤࢀࢃࠧิ").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠫࡈࡸࡩࡵ࡫ࡦࡥࡱࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥࠡࡴࡸࡲࠥ࡮࡯ࡰ࡭ࠣࡿࢂࡀࠠࡼࡿࠪี").format(name, str(e)))
    try:
      bstack11l11ll1l_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack1l1_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡲࡶ࡮࡭ࡩ࡯ࡣ࡯ࠤࡧ࡫ࡨࡢࡸࡨࠤ࡭ࡵ࡯࡬ࠢࡾࢁ࠿ࠦࡻࡾࠩึ").format(name, str(e2)))
def bstack11ll1l1l11_opy_(config, startdir):
  return bstack1l1_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࠲ࢀࠦื").format(bstack1l1_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨุ"))
notset = Notset()
def bstack11l1lll1l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack111ll11ll1_opy_
  if str(name).lower() == bstack1l1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨู"):
    return bstack1l1_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ฺࠣ")
  else:
    return bstack111ll11ll1_opy_(self, name, default, skip)
def bstack111l1l11ll_opy_(item, when):
  global bstack1l1111lll_opy_
  try:
    bstack1l1111lll_opy_(item, when)
  except Exception as e:
    pass
def bstack1l11ll11ll_opy_():
  return
def bstack1111l1111_opy_(type, name, status, reason, bstack1l1111ll1_opy_, bstack11l1lll11_opy_):
  bstack11lll1l1l_opy_ = {
    bstack1l1_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪ฻"): type,
    bstack1l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ฼"): {}
  }
  if type == bstack1l1_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ฽"):
    bstack11lll1l1l_opy_[bstack1l1_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ฾")][bstack1l1_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭฿")] = bstack1l1111ll1_opy_
    bstack11lll1l1l_opy_[bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫเ")][bstack1l1_opy_ (u"ࠩࡧࡥࡹࡧࠧแ")] = json.dumps(str(bstack11l1lll11_opy_))
  if type == bstack1l1_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫโ"):
    bstack11lll1l1l_opy_[bstack1l1_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧใ")][bstack1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪไ")] = name
  if type == bstack1l1_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩๅ"):
    bstack11lll1l1l_opy_[bstack1l1_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪๆ")][bstack1l1_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ็")] = status
    if status == bstack1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥ่ࠩ"):
      bstack11lll1l1l_opy_[bstack1l1_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ้࠭")][bstack1l1_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱ๊ࠫ")] = json.dumps(str(reason))
  bstack11111l1ll1_opy_ = bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿ๋ࠪ").format(json.dumps(bstack11lll1l1l_opy_))
  return bstack11111l1ll1_opy_
def bstack111ll1ll1l_opy_(driver_command, response):
    if driver_command == bstack1l1_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪ์"):
        bstack1l11llll_opy_.bstack1l1ll1lll_opy_({
            bstack1l1_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭ํ"): response[bstack1l1_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧ๎")],
            bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ๏"): bstack1l11llll_opy_.current_test_uuid()
        })
def bstack1ll1l1lll1_opy_(item, call, rep):
  global bstack1111l1lll_opy_
  global bstack11lll11ll_opy_
  global bstack1111llll11_opy_
  name = bstack1l1_opy_ (u"ࠪࠫ๐")
  try:
    if rep.when == bstack1l1_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ๑"):
      bstack11lll111l_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1111llll11_opy_:
          name = str(rep.nodeid)
          bstack11l1lll1l1_opy_ = bstack1111l1111_opy_(bstack1l1_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭๒"), name, bstack1l1_opy_ (u"࠭ࠧ๓"), bstack1l1_opy_ (u"ࠧࠨ๔"), bstack1l1_opy_ (u"ࠨࠩ๕"), bstack1l1_opy_ (u"ࠩࠪ๖"))
          threading.current_thread().bstack1l1lll1lll_opy_ = name
          for driver in bstack11lll11ll_opy_:
            if bstack11lll111l_opy_ == driver.session_id:
              driver.execute_script(bstack11l1lll1l1_opy_)
      except Exception as e:
        logger.debug(bstack1l1_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪ๗").format(str(e)))
      try:
        bstack111111ll1_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1l1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ๘"):
          status = bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ๙") if rep.outcome.lower() == bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭๚") else bstack1l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ๛")
          reason = bstack1l1_opy_ (u"ࠨࠩ๜")
          if status == bstack1l1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ๝"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1l1_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨ๞") if status == bstack1l1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ๟") else bstack1l1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ๠")
          data = name + bstack1l1_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨ๡") if status == bstack1l1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ๢") else name + bstack1l1_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠣࠣࠫ๣") + reason
          bstack1l11l1lll_opy_ = bstack1111l1111_opy_(bstack1l1_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫ๤"), bstack1l1_opy_ (u"ࠪࠫ๥"), bstack1l1_opy_ (u"ࠫࠬ๦"), bstack1l1_opy_ (u"ࠬ࠭๧"), level, data)
          for driver in bstack11lll11ll_opy_:
            if bstack11lll111l_opy_ == driver.session_id:
              driver.execute_script(bstack1l11l1lll_opy_)
      except Exception as e:
        logger.debug(bstack1l1_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡴࡴࡴࡦࡺࡷࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪ๨").format(str(e)))
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽࢀࠫ๩").format(str(e)))
  bstack1111l1lll_opy_(item, call, rep)
def bstack11l11111l1_opy_(driver, bstack1l1l11111_opy_, test=None):
  global bstack1l1l11l1l_opy_
  if test != None:
    bstack1ll1lll111_opy_ = getattr(test, bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭๪"), None)
    bstack11l11ll11l_opy_ = getattr(test, bstack1l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧ๫"), None)
    PercySDK.screenshot(driver, bstack1l1l11111_opy_, bstack1ll1lll111_opy_=bstack1ll1lll111_opy_, bstack11l11ll11l_opy_=bstack11l11ll11l_opy_, bstack111l1l1111_opy_=bstack1l1l11l1l_opy_)
  else:
    PercySDK.screenshot(driver, bstack1l1l11111_opy_)
@measure(event_name=EVENTS.bstack1l111ll11l_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack111ll11l1l_opy_(driver):
  if bstack1l11lllll_opy_.bstack1111l11l11_opy_() is True or bstack1l11lllll_opy_.capturing() is True:
    return
  bstack1l11lllll_opy_.bstack11lll1ll1_opy_()
  while not bstack1l11lllll_opy_.bstack1111l11l11_opy_():
    bstack1l111ll1l_opy_ = bstack1l11lllll_opy_.bstack1111l1l11l_opy_()
    bstack11l11111l1_opy_(driver, bstack1l111ll1l_opy_)
  bstack1l11lllll_opy_.bstack11ll11l111_opy_()
def bstack111lll1ll1_opy_(sequence, driver_command, response = None, bstack1l1ll11lll_opy_ = None, args = None):
    try:
      if sequence != bstack1l1_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪ๬"):
        return
      if percy.bstack1l11l11l1l_opy_() == bstack1l1_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥ๭"):
        return
      bstack1l111ll1l_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ๮"), None)
      for command in bstack1111l11l1_opy_:
        if command == driver_command:
          with bstack11l1l111l1_opy_:
            bstack1l11111111_opy_ = bstack11lll11ll_opy_.copy()
          for driver in bstack1l11111111_opy_:
            bstack111ll11l1l_opy_(driver)
      bstack111l1l1l1_opy_ = percy.bstack111ll1l111_opy_()
      if driver_command in bstack1l1l111lll_opy_[bstack111l1l1l1_opy_]:
        bstack1l11lllll_opy_.bstack1l111ll1ll_opy_(bstack1l111ll1l_opy_, driver_command)
    except Exception as e:
      pass
def bstack1ll11l1111_opy_(framework_name):
  if bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ๯")):
      return
  bstack11l11111_opy_.set_property(bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫ๰"), True)
  global bstack1l1l11l11l_opy_
  global bstack1111lll11l_opy_
  global bstack11ll1l1l1l_opy_
  bstack1l1l11l11l_opy_ = framework_name
  logger.info(bstack1l111l11l1_opy_.format(bstack1l1l11l11l_opy_.split(bstack1l1_opy_ (u"ࠨ࠯ࠪ๱"))[0]))
  bstack1ll11llll1_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1ll11ll1ll_opy_:
      Service.start = bstack11111l11ll_opy_
      Service.stop = bstack11ll11111l_opy_
      webdriver.Remote.get = bstack1l1l1l1111_opy_
      WebDriver.quit = bstack11l1ll1ll_opy_
      webdriver.Remote.__init__ = bstack1ll111l11l_opy_
    if not bstack1ll11ll1ll_opy_:
        webdriver.Remote.__init__ = bstack111ll11ll_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack11111ll1l_opy_
    bstack1111lll11l_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1ll11ll1ll_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1llllllll1_opy_
  except Exception as e:
    pass
  bstack111l111l1l_opy_()
  if not bstack1111lll11l_opy_:
    bstack1lll1lll1l_opy_(bstack1l1_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦ๲"), bstack1l11lll11l_opy_)
  if bstack1l11l1l1l1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack1l1_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫ๳")) and callable(getattr(RemoteConnection, bstack1l1_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬ๴"))):
        RemoteConnection._get_proxy_url = bstack1l1l111l1_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack1l1l111l1_opy_
    except Exception as e:
      logger.error(bstack11ll1l1ll1_opy_.format(str(e)))
  if bstack11lll1lll1_opy_():
    bstack1l1l1l11l1_opy_(CONFIG, logger)
  if (bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ๵") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1l11l11l1l_opy_() == bstack1l1_opy_ (u"ࠨࡴࡳࡷࡨࠦ๶"):
          bstack1l111l11l_opy_(bstack111lll1ll1_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack11l1l1l11l_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack111l1ll1l1_opy_
      except Exception as e:
        logger.warn(bstack111l11l11l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1ll1lll1ll_opy_
      except Exception as e:
        logger.debug(bstack1l1ll111l1_opy_ + str(e))
    except Exception as e:
      bstack1lll1lll1l_opy_(e, bstack111l11l11l_opy_)
    Output.start_test = bstack1ll1l1ll11_opy_
    Output.end_test = bstack11l1l111ll_opy_
    TestStatus.__init__ = bstack1l1ll11l1l_opy_
    QueueItem.__init__ = bstack1l1lll1ll1_opy_
    pabot._create_items = bstack1ll11l11l_opy_
    try:
      from pabot import __version__ as bstack111lllllll_opy_
      if version.parse(bstack111lllllll_opy_) >= version.parse(bstack1l1_opy_ (u"ࠧ࠶࠰࠳࠲࠵࠭๷")):
        pabot._run = bstack11llll11ll_opy_
      elif version.parse(bstack111lllllll_opy_) >= version.parse(bstack1l1_opy_ (u"ࠨ࠶࠱࠶࠳࠶ࠧ๸")):
        pabot._run = bstack1l1l11llll_opy_
      elif version.parse(bstack111lllllll_opy_) >= version.parse(bstack1l1_opy_ (u"ࠩ࠵࠲࠶࠻࠮࠱ࠩ๹")):
        pabot._run = bstack11111l11l1_opy_
      elif version.parse(bstack111lllllll_opy_) >= version.parse(bstack1l1_opy_ (u"ࠪ࠶࠳࠷࠳࠯࠲ࠪ๺")):
        pabot._run = bstack11111lll1_opy_
      else:
        pabot._run = bstack1ll1l1llll_opy_
    except Exception as e:
      pabot._run = bstack1ll1l1llll_opy_
    pabot._create_command_for_execution = bstack1ll1l1111_opy_
    pabot._report_results = bstack1l111lllll_opy_
  if bstack1l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ๻") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1lll1lll1l_opy_(e, bstack1lll1lllll_opy_)
    Runner.run_hook = bstack1ll1l11l1_opy_
    Step.run = bstack11l111l111_opy_
  if bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ๼") in str(framework_name).lower():
    if not bstack1ll11ll1ll_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack11ll1l1l11_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1l11ll11ll_opy_
      Config.getoption = bstack11l1lll1l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1ll1l1lll1_opy_
    except Exception as e:
      pass
def bstack1llll1111l_opy_():
  global CONFIG
  if bstack1l1_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭๽") in CONFIG and int(CONFIG[bstack1l1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ๾")]) > 1:
    logger.warn(bstack1ll1lll11l_opy_)
def bstack1l111ll11_opy_(arg, bstack1llllll1l_opy_, bstack1l1llll11l_opy_=None):
  global CONFIG
  global bstack111111ll11_opy_
  global bstack11l11ll1ll_opy_
  global bstack1ll11ll1ll_opy_
  global bstack11l11111_opy_
  bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ๿")
  if bstack1llllll1l_opy_ and isinstance(bstack1llllll1l_opy_, str):
    bstack1llllll1l_opy_ = eval(bstack1llllll1l_opy_)
  CONFIG = bstack1llllll1l_opy_[bstack1l1_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩ຀")]
  bstack111111ll11_opy_ = bstack1llllll1l_opy_[bstack1l1_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫກ")]
  bstack11l11ll1ll_opy_ = bstack1llllll1l_opy_[bstack1l1_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ຂ")]
  bstack1ll11ll1ll_opy_ = bstack1llllll1l_opy_[bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ຃")]
  bstack11l11111_opy_.set_property(bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧຄ"), bstack1ll11ll1ll_opy_)
  os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ຅")] = bstack1ll11ll1l_opy_
  os.environ[bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠧຆ")] = json.dumps(CONFIG)
  os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡊࡘࡆࡤ࡛ࡒࡍࠩງ")] = bstack111111ll11_opy_
  os.environ[bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫຈ")] = str(bstack11l11ll1ll_opy_)
  os.environ[bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪຉ")] = str(True)
  if bstack1l1l1l1ll1_opy_(arg, [bstack1l1_opy_ (u"ࠬ࠳࡮ࠨຊ"), bstack1l1_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ຋")]) != -1:
    os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡂࡔࡄࡐࡑࡋࡌࠨຌ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1l1l11ll1_opy_)
    return
  bstack1l11l1ll11_opy_()
  global bstack11lllllll1_opy_
  global bstack1l1l11l1l_opy_
  global bstack1l11lll1l_opy_
  global bstack11l1l1lll1_opy_
  global bstack11lllll11_opy_
  global bstack11ll1l1l1l_opy_
  global bstack1l111ll111_opy_
  arg.append(bstack1l1_opy_ (u"ࠣ࠯࡚ࠦຍ"))
  arg.append(bstack1l1_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦ࠼ࡐࡳࡩࡻ࡬ࡦࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡭ࡲࡶ࡯ࡳࡶࡨࡨ࠿ࡶࡹࡵࡧࡶࡸ࠳ࡖࡹࡵࡧࡶࡸ࡜ࡧࡲ࡯࡫ࡱ࡫ࠧຎ"))
  arg.append(bstack1l1_opy_ (u"ࠥ࠱࡜ࠨຏ"))
  arg.append(bstack1l1_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨ࠾࡙࡮ࡥࠡࡪࡲࡳࡰ࡯࡭ࡱ࡮ࠥຐ"))
  global bstack1ll1lll1l1_opy_
  global bstack1111l1111l_opy_
  global bstack11ll1ll11l_opy_
  global bstack1ll1l1l1l_opy_
  global bstack1ll1ll111l_opy_
  global bstack1l111111ll_opy_
  global bstack1lll11l11l_opy_
  global bstack1l1lll11l_opy_
  global bstack1llll1l1l1_opy_
  global bstack1ll1l11ll1_opy_
  global bstack111ll11ll1_opy_
  global bstack1l1111lll_opy_
  global bstack1111l1lll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll1lll1l1_opy_ = webdriver.Remote.__init__
    bstack1111l1111l_opy_ = WebDriver.quit
    bstack1l1lll11l_opy_ = WebDriver.close
    bstack1llll1l1l1_opy_ = WebDriver.get
    bstack11ll1ll11l_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1l11l1lll1_opy_(CONFIG) and bstack1l111l11ll_opy_():
    if bstack11llll111_opy_() < version.parse(bstack1llll11l1l_opy_):
      logger.error(bstack11l11111l_opy_.format(bstack11llll111_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1l1_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ຑ")) and callable(getattr(RemoteConnection, bstack1l1_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧຒ"))):
          bstack1ll1l11ll1_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1ll1l11ll1_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack11ll1l1ll1_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack111ll11ll1_opy_ = Config.getoption
    from _pytest import runner
    bstack1l1111lll_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1llll1l11_opy_)
  try:
    from pytest_bdd import reporting
    bstack1111l1lll_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1l1_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨຓ"))
  bstack1l11lll1l_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬດ"), {}).get(bstack1l1_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫຕ"))
  bstack1l111ll111_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack11l11l1l1l_opy_():
      bstack1llllll1ll_opy_.invoke(Events.CONNECT, bstack11llll111l_opy_())
    platform_index = int(os.environ.get(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪຖ"), bstack1l1_opy_ (u"ࠫ࠵࠭ທ")))
  else:
    bstack1ll11l1111_opy_(bstack1llll111ll_opy_)
  os.environ[bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭ຘ")] = CONFIG[bstack1l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨນ")]
  os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪບ")] = CONFIG[bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫປ")]
  os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬຜ")] = bstack1ll11ll1ll_opy_.__str__()
  from _pytest.config import main as bstack11ll11ll1l_opy_
  bstack1llll1ll1l_opy_ = []
  try:
    exit_code = bstack11ll11ll1l_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1l111lll1l_opy_()
    if bstack1l1_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧຝ") in multiprocessing.current_process().__dict__.keys():
      for bstack111l11l1l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1llll1ll1l_opy_.append(bstack111l11l1l_opy_)
    try:
      bstack11ll1l11ll_opy_ = (bstack1llll1ll1l_opy_, int(exit_code))
      bstack1l1llll11l_opy_.append(bstack11ll1l11ll_opy_)
    except:
      bstack1l1llll11l_opy_.append((bstack1llll1ll1l_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1llll1ll1l_opy_.append({bstack1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩພ"): bstack1l1_opy_ (u"ࠬࡖࡲࡰࡥࡨࡷࡸࠦࠧຟ") + os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ຠ")), bstack1l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ມ"): traceback.format_exc(), bstack1l1_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧຢ"): int(os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩຣ")))})
    bstack1l1llll11l_opy_.append((bstack1llll1ll1l_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack1l1_opy_ (u"ࠥࡶࡪࡺࡲࡪࡧࡶࠦ຤"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack1l1ll11ll_opy_ = e.__class__.__name__
    print(bstack1l1_opy_ (u"ࠦࠪࡹ࠺ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡤࡨ࡬ࡦࡼࡥࠡࡶࡨࡷࡹࠦࠥࡴࠤລ") % (bstack1l1ll11ll_opy_, e))
    return 1
def bstack111l11111l_opy_(arg):
  global bstack1ll1l1lll_opy_
  bstack1ll11l1111_opy_(bstack1ll1ll1111_opy_)
  os.environ[bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭຦")] = str(bstack11l11ll1ll_opy_)
  retries = bstack111lll1l_opy_.bstack111l1l11_opy_(CONFIG)
  status_code = 0
  if bstack111lll1l_opy_.bstack1lll1l11l_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack1lllll1l11_opy_
    status_code = bstack1lllll1l11_opy_(arg)
  if status_code != 0:
    bstack1ll1l1lll_opy_ = status_code
def bstack1l1l1111l1_opy_():
  logger.info(bstack1111l11ll1_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1l1_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬວ"), help=bstack1l1_opy_ (u"ࠧࡈࡧࡱࡩࡷࡧࡴࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡥࡲࡲ࡫࡯ࡧࠨຨ"))
  parser.add_argument(bstack1l1_opy_ (u"ࠨ࠯ࡸࠫຩ"), bstack1l1_opy_ (u"ࠩ࠰࠱ࡺࡹࡥࡳࡰࡤࡱࡪ࠭ສ"), help=bstack1l1_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡶࡵࡨࡶࡳࡧ࡭ࡦࠩຫ"))
  parser.add_argument(bstack1l1_opy_ (u"ࠫ࠲ࡱࠧຬ"), bstack1l1_opy_ (u"ࠬ࠳࠭࡬ࡧࡼࠫອ"), help=bstack1l1_opy_ (u"࡙࠭ࡰࡷࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿࠧຮ"))
  parser.add_argument(bstack1l1_opy_ (u"ࠧ࠮ࡨࠪຯ"), bstack1l1_opy_ (u"ࠨ࠯࠰ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ະ"), help=bstack1l1_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨັ"))
  bstack1l111l1l1_opy_ = parser.parse_args()
  try:
    bstack1ll1ll11l1_opy_ = bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡪࡩࡳ࡫ࡲࡪࡥ࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧາ")
    if bstack1l111l1l1_opy_.framework and bstack1l111l1l1_opy_.framework not in (bstack1l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫຳ"), bstack1l1_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭ິ")):
      bstack1ll1ll11l1_opy_ = bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠯ࡻࡰࡰ࠳ࡹࡡ࡮ࡲ࡯ࡩࠬີ")
    bstack11lllll1l1_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll1ll11l1_opy_)
    bstack1llll1llll_opy_ = open(bstack11lllll1l1_opy_, bstack1l1_opy_ (u"ࠧࡳࠩຶ"))
    bstack1111l1ll1l_opy_ = bstack1llll1llll_opy_.read()
    bstack1llll1llll_opy_.close()
    if bstack1l111l1l1_opy_.username:
      bstack1111l1ll1l_opy_ = bstack1111l1ll1l_opy_.replace(bstack1l1_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨື"), bstack1l111l1l1_opy_.username)
    if bstack1l111l1l1_opy_.key:
      bstack1111l1ll1l_opy_ = bstack1111l1ll1l_opy_.replace(bstack1l1_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ຸࠫ"), bstack1l111l1l1_opy_.key)
    if bstack1l111l1l1_opy_.framework:
      bstack1111l1ll1l_opy_ = bstack1111l1ll1l_opy_.replace(bstack1l1_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎູࠫ"), bstack1l111l1l1_opy_.framework)
    file_name = bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲ຺ࠧ")
    file_path = os.path.abspath(file_name)
    bstack11ll11l1l_opy_ = open(file_path, bstack1l1_opy_ (u"ࠬࡽࠧົ"))
    bstack11ll11l1l_opy_.write(bstack1111l1ll1l_opy_)
    bstack11ll11l1l_opy_.close()
    logger.info(bstack11l1l1l11_opy_)
    try:
      os.environ[bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨຼ")] = bstack1l111l1l1_opy_.framework if bstack1l111l1l1_opy_.framework != None else bstack1l1_opy_ (u"ࠢࠣຽ")
      config = yaml.safe_load(bstack1111l1ll1l_opy_)
      config[bstack1l1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ຾")] = bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠯ࡶࡩࡹࡻࡰࠨ຿")
      bstack11lll1llll_opy_(bstack111ll1ll1_opy_, config)
    except Exception as e:
      logger.debug(bstack1l11111l1_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1ll11l1ll_opy_.format(str(e)))
def bstack11lll1llll_opy_(bstack11ll11l11_opy_, config, bstack111llll111_opy_={}):
  global bstack1ll11ll1ll_opy_
  global bstack11lll1l1l1_opy_
  global bstack11l11111_opy_
  if not config:
    return
  bstack111l11111_opy_ = bstack1llllll111_opy_ if not bstack1ll11ll1ll_opy_ else (
    bstack1ll11ll1l1_opy_ if bstack1l1_opy_ (u"ࠪࡥࡵࡶࠧເ") in config else (
        bstack11ll111ll_opy_ if config.get(bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨແ")) else bstack1lll1l1ll1_opy_
    )
)
  bstack1l1lll1l1_opy_ = False
  bstack1ll111l1ll_opy_ = False
  if bstack1ll11ll1ll_opy_ is True:
      if bstack1l1_opy_ (u"ࠬࡧࡰࡱࠩໂ") in config:
          bstack1l1lll1l1_opy_ = True
      else:
          bstack1ll111l1ll_opy_ = True
  bstack11lllllll_opy_ = bstack1l111l111_opy_.bstack1lllll1111_opy_(config, bstack11lll1l1l1_opy_)
  bstack1l11l111l_opy_ = bstack1l11llll1l_opy_()
  data = {
    bstack1l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨໃ"): config[bstack1l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩໄ")],
    bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ໅"): config[bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬໆ")],
    bstack1l1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ໇"): bstack11ll11l11_opy_,
    bstack1l1_opy_ (u"ࠫࡩ࡫ࡴࡦࡥࡷࡩࡩࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ່"): os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ້ࠧ"), bstack11lll1l1l1_opy_),
    bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ໊"): bstack1ll111111_opy_,
    bstack1l1_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭໋ࠩ"): bstack1l1111l11l_opy_(),
    bstack1l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໌"): {
      bstack1l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧໍ"): str(config[bstack1l1_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ໎")]) if bstack1l1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ໏") in config else bstack1l1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨ໐"),
      bstack1l1_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࡗࡧࡵࡷ࡮ࡵ࡮ࠨ໑"): sys.version,
      bstack1l1_opy_ (u"ࠧࡳࡧࡩࡩࡷࡸࡥࡳࠩ໒"): bstack111l1l1l1l_opy_(os.environ.get(bstack1l1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ໓"), bstack11lll1l1l1_opy_)),
      bstack1l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ໔"): bstack1l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ໕"),
      bstack1l1_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬ໖"): bstack111l11111_opy_,
      bstack1l1_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ໗"): bstack11lllllll_opy_,
      bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡶࡷ࡬ࡨࠬ໘"): os.environ[bstack1l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ໙")],
      bstack1l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ໚"): os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ໛"), bstack11lll1l1l1_opy_),
      bstack1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ໜ"): bstack111lll1l11_opy_(os.environ.get(bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ໝ"), bstack11lll1l1l1_opy_)),
      bstack1l1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫໞ"): bstack1l11l111l_opy_.get(bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫໟ")),
      bstack1l1_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭໠"): bstack1l11l111l_opy_.get(bstack1l1_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ໡")),
      bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ໢"): config[bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໣")] if config[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ໤")] else bstack1l1_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨ໥"),
      bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ໦"): str(config[bstack1l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ໧")]) if bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໨") in config else bstack1l1_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥ໩"),
      bstack1l1_opy_ (u"ࠪࡳࡸ࠭໪"): sys.platform,
      bstack1l1_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭໫"): socket.gethostname(),
      bstack1l1_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ໬"): bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ໭"))
    }
  }
  if not bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ໮")) is None:
    data[bstack1l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໯")][bstack1l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡑࡪࡺࡡࡥࡣࡷࡥࠬ໰")] = {
      bstack1l1_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ໱"): bstack1l1_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩ໲"),
      bstack1l1_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬ໳"): bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭໴")),
      bstack1l1_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࡎࡶ࡯ࡥࡩࡷ࠭໵"): bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡐࡲࠫ໶"))
    }
  if bstack11ll11l11_opy_ == bstack11l1llll1l_opy_:
    data[bstack1l1_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໷")][bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡅࡲࡲ࡫࡯ࡧࠨ໸")] = bstack111l1l1l11_opy_(config)
    data[bstack1l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ໹")][bstack1l1_opy_ (u"ࠬ࡯ࡳࡑࡧࡵࡧࡾࡇࡵࡵࡱࡈࡲࡦࡨ࡬ࡦࡦࠪ໺")] = percy.bstack1ll1llll1_opy_
    data[bstack1l1_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ໻")][bstack1l1_opy_ (u"ࠧࡱࡧࡵࡧࡾࡈࡵࡪ࡮ࡧࡍࡩ࠭໼")] = percy.percy_build_id
  if not bstack111lll1l_opy_.bstack11l1l11ll1_opy_(CONFIG):
    data[bstack1l1_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໽")][bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠭໾")] = bstack111lll1l_opy_.bstack11l1l11ll1_opy_(CONFIG)
  bstack1llllll11_opy_ = bstack1llll111l_opy_.bstack1111ll1l_opy_(CONFIG, logger)
  bstack1111ll11_opy_ = bstack111lll1l_opy_.bstack1111ll1l_opy_(config=CONFIG)
  if bstack1llllll11_opy_ is not None and bstack1111ll11_opy_ is not None and bstack1111ll11_opy_.bstack1lll1llll_opy_():
    data[bstack1l1_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໿")][bstack1111ll11_opy_.bstack1ll111ll1l_opy_()] = bstack1llllll11_opy_.bstack1l1l111111_opy_()
  update(data[bstack1l1_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧༀ")], bstack111llll111_opy_)
  try:
    response = bstack1lll1l1l11_opy_(bstack1l1_opy_ (u"ࠬࡖࡏࡔࡖࠪ༁"), bstack11ll1ll1ll_opy_(bstack1l11lll111_opy_), data, {
      bstack1l1_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ༂"): (config[bstack1l1_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ༃")], config[bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ༄")])
    })
    if response:
      logger.debug(bstack1ll1lllll1_opy_.format(bstack11ll11l11_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11ll11l1ll_opy_.format(str(e)))
def bstack111l1l1l1l_opy_(framework):
  return bstack1l1_opy_ (u"ࠤࡾࢁ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨ༅").format(str(framework), __version__) if framework else bstack1l1_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦ༆").format(
    __version__)
def bstack1l11l1ll11_opy_():
  global CONFIG
  global bstack11ll1l1lll_opy_
  if bool(CONFIG):
    return
  try:
    bstack11l1111l1l_opy_()
    logger.debug(bstack11lll1ll1l_opy_.format(str(CONFIG)))
    bstack11ll1l1lll_opy_ = bstack1ll1111l1_opy_.configure_logger(CONFIG, bstack11ll1l1lll_opy_)
    bstack1ll11llll1_opy_()
  except Exception as e:
    logger.error(bstack1l1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵ࠲ࠠࡦࡴࡵࡳࡷࡀࠠࠣ༇") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1l111l1lll_opy_
  atexit.register(bstack1111l1l111_opy_)
  signal.signal(signal.SIGINT, bstack1l1l11lll_opy_)
  signal.signal(signal.SIGTERM, bstack1l1l11lll_opy_)
def bstack1l111l1lll_opy_(exctype, value, traceback):
  global bstack11lll11ll_opy_
  try:
    for driver in bstack11lll11ll_opy_:
      bstack1l1ll11l11_opy_(driver, bstack1l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ༈"), bstack1l1_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤ༉") + str(value))
  except Exception:
    pass
  logger.info(bstack11111ll111_opy_)
  bstack1lll1ll1l1_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1lll1ll1l1_opy_(message=bstack1l1_opy_ (u"ࠧࠨ༊"), bstack1111lllll1_opy_ = False):
  global CONFIG
  bstack11ll1l1ll_opy_ = bstack1l1_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡆࡺࡦࡩࡵࡺࡩࡰࡰࠪ་") if bstack1111lllll1_opy_ else bstack1l1_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ༌")
  try:
    if message:
      bstack111llll111_opy_ = {
        bstack11ll1l1ll_opy_ : str(message)
      }
      bstack11lll1llll_opy_(bstack11l1llll1l_opy_, CONFIG, bstack111llll111_opy_)
    else:
      bstack11lll1llll_opy_(bstack11l1llll1l_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack11lll111l1_opy_.format(str(e)))
def bstack11l1l1ll1_opy_(bstack11l11111ll_opy_, size):
  bstack1ll1llll11_opy_ = []
  while len(bstack11l11111ll_opy_) > size:
    bstack1111llll1_opy_ = bstack11l11111ll_opy_[:size]
    bstack1ll1llll11_opy_.append(bstack1111llll1_opy_)
    bstack11l11111ll_opy_ = bstack11l11111ll_opy_[size:]
  bstack1ll1llll11_opy_.append(bstack11l11111ll_opy_)
  return bstack1ll1llll11_opy_
def bstack11l1l11l1_opy_(args):
  if bstack1l1_opy_ (u"ࠪ࠱ࡲ࠭།") in args and bstack1l1_opy_ (u"ࠫࡵࡪࡢࠨ༎") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack11ll11l11l_opy_, stage=STAGE.bstack11l11l1ll_opy_)
def run_on_browserstack(bstack111lllll1_opy_=None, bstack1l1llll11l_opy_=None, bstack11lll11111_opy_=False):
  global CONFIG
  global bstack111111ll11_opy_
  global bstack11l11ll1ll_opy_
  global bstack11lll1l1l1_opy_
  global bstack11l11111_opy_
  bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"ࠬ࠭༏")
  bstack1ll1l1l111_opy_(bstack11l1l1l111_opy_, logger)
  if bstack111lllll1_opy_ and isinstance(bstack111lllll1_opy_, str):
    bstack111lllll1_opy_ = eval(bstack111lllll1_opy_)
  if bstack111lllll1_opy_:
    CONFIG = bstack111lllll1_opy_[bstack1l1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭༐")]
    bstack111111ll11_opy_ = bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ༑")]
    bstack11l11ll1ll_opy_ = bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ༒")]
    bstack11l11111_opy_.set_property(bstack1l1_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ༓"), bstack11l11ll1ll_opy_)
    bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༔")
  bstack11l11111_opy_.set_property(bstack1l1_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭༕"), uuid4().__str__())
  logger.info(bstack1l1_opy_ (u"࡙ࠬࡄࡌࠢࡵࡹࡳࠦࡳࡵࡣࡵࡸࡪࡪࠠࡸ࡫ࡷ࡬ࠥ࡯ࡤ࠻ࠢࠪ༖") + bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ༗")));
  logger.debug(bstack1l1_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥ࠿༘ࠪ") + bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦ༙ࠪ")))
  if not bstack11lll11111_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1l1l11ll1_opy_)
      return
    if sys.argv[1] == bstack1l1_opy_ (u"ࠩ࠰࠱ࡻ࡫ࡲࡴ࡫ࡲࡲࠬ༚") or sys.argv[1] == bstack1l1_opy_ (u"ࠪ࠱ࡻ࠭༛"):
      logger.info(bstack1l1_opy_ (u"ࠫࡇࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡔࡾࡺࡨࡰࡰࠣࡗࡉࡑࠠࡷࡽࢀࠫ༜").format(__version__))
      return
    if sys.argv[1] == bstack1l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ༝"):
      bstack1l1l1111l1_opy_()
      return
  args = sys.argv
  bstack1l11l1ll11_opy_()
  global bstack11lllllll1_opy_
  global bstack11l1l111l_opy_
  global bstack1l111ll111_opy_
  global bstack1l1l1l11ll_opy_
  global bstack1l1l11l1l_opy_
  global bstack1l11lll1l_opy_
  global bstack11l1l1lll1_opy_
  global bstack1ll11l11l1_opy_
  global bstack11lllll11_opy_
  global bstack11ll1l1l1l_opy_
  global bstack11l111l11_opy_
  bstack11l1l111l_opy_ = len(CONFIG.get(bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ༞"), []))
  if not bstack1ll11ll1l_opy_:
    if args[1] == bstack1l1_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༟") or args[1] == bstack1l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩ༠"):
      bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༡")
      args = args[2:]
    elif args[1] == bstack1l1_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ༢"):
      bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༣")
      args = args[2:]
    elif args[1] == bstack1l1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ༤"):
      bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬ༥")
      args = args[2:]
    elif args[1] == bstack1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ༦"):
      bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ༧")
      args = args[2:]
    elif args[1] == bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ༨"):
      bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ༩")
      args = args[2:]
    elif args[1] == bstack1l1_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ༪"):
      bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ༫")
      args = args[2:]
    else:
      if not bstack1l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༬") in CONFIG or str(CONFIG[bstack1l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༭")]).lower() in [bstack1l1_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ༮"), bstack1l1_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ༯")]:
        bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༰")
        args = args[1:]
      elif str(CONFIG[bstack1l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ༱")]).lower() == bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༲"):
        bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ༳")
        args = args[1:]
      elif str(CONFIG[bstack1l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ༴")]).lower() == bstack1l1_opy_ (u"ࠨࡲࡤࡦࡴࡺ༵ࠧ"):
        bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ༶")
        args = args[1:]
      elif str(CONFIG[bstack1l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ༷࠭")]).lower() == bstack1l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༸"):
        bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ༹ࠬ")
        args = args[1:]
      elif str(CONFIG[bstack1l1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༺")]).lower() == bstack1l1_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ༻"):
        bstack1ll11ll1l_opy_ = bstack1l1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ༼")
        args = args[1:]
      else:
        os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ༽")] = bstack1ll11ll1l_opy_
        bstack1ll1llll1l_opy_(bstack1l1ll11ll1_opy_)
  os.environ[bstack1l1_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫ༾")] = bstack1ll11ll1l_opy_
  bstack11lll1l1l1_opy_ = bstack1ll11ll1l_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack11l11l11l_opy_ = bstack1ll1ll1l1_opy_[bstack1l1_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗ࠱ࡇࡊࡄࠨ༿")] if bstack1ll11ll1l_opy_ == bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཀ") and bstack1l11l11ll_opy_() else bstack1ll11ll1l_opy_
      bstack1llllll1ll_opy_.invoke(Events.bstack1ll1111111_opy_, bstack1l11l1111_opy_(
        sdk_version=__version__,
        path_config=bstack11l11lll1l_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack11l11l11l_opy_,
        frameworks=[bstack11l11l11l_opy_],
        framework_versions={
          bstack11l11l11l_opy_: bstack111lll1l11_opy_(bstack1l1_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬཁ") if bstack1ll11ll1l_opy_ in [bstack1l1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ག"), bstack1l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧགྷ"), bstack1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪང")] else bstack1ll11ll1l_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack1l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧཅ"), None):
        CONFIG[bstack1l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨཆ")] = cli.config.get(bstack1l1_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢཇ"), None)
    except Exception as e:
      bstack1llllll1ll_opy_.invoke(Events.bstack1l1ll11111_opy_, e.__traceback__, 1)
    if bstack11l11ll1ll_opy_:
      CONFIG[bstack1l1_opy_ (u"ࠨࡡࡱࡲࠥ཈")] = cli.config[bstack1l1_opy_ (u"ࠢࡢࡲࡳࠦཉ")]
      logger.info(bstack11l1l11lll_opy_.format(CONFIG[bstack1l1_opy_ (u"ࠨࡣࡳࡴࠬཊ")]))
  else:
    bstack1llllll1ll_opy_.clear()
  global bstack1ll11l111_opy_
  global bstack1l1llll111_opy_
  if bstack111lllll1_opy_:
    try:
      bstack1l1ll111l_opy_ = datetime.datetime.now()
      os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫཋ")] = bstack1ll11ll1l_opy_
      bstack11lll1llll_opy_(bstack1l1111l1l1_opy_, CONFIG)
      cli.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡵࡧ࡯ࡤࡺࡥࡴࡶࡢࡥࡹࡺࡥ࡮ࡲࡷࡩࡩࠨཌ"), datetime.datetime.now() - bstack1l1ll111l_opy_)
    except Exception as e:
      logger.debug(bstack1111lll1l1_opy_.format(str(e)))
  global bstack1ll1lll1l1_opy_
  global bstack1111l1111l_opy_
  global bstack1l1l111ll_opy_
  global bstack11111ll1ll_opy_
  global bstack11111l1l11_opy_
  global bstack1l1l1ll11l_opy_
  global bstack1ll1l1l1l_opy_
  global bstack1ll1ll111l_opy_
  global bstack11l1ll111l_opy_
  global bstack1l111111ll_opy_
  global bstack1lll11l11l_opy_
  global bstack1l1lll11l_opy_
  global bstack11l11ll1l_opy_
  global bstack1l11l1ll1l_opy_
  global bstack1llll1l1l1_opy_
  global bstack1ll1l11ll1_opy_
  global bstack111ll11ll1_opy_
  global bstack1l1111lll_opy_
  global bstack1l1lllll1l_opy_
  global bstack1111l1lll_opy_
  global bstack11ll1ll11l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll1lll1l1_opy_ = webdriver.Remote.__init__
    bstack1111l1111l_opy_ = WebDriver.quit
    bstack1l1lll11l_opy_ = WebDriver.close
    bstack1llll1l1l1_opy_ = WebDriver.get
    bstack11ll1ll11l_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1ll11l111_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1ll111llll_opy_
    bstack1l1llll111_opy_ = bstack1ll111llll_opy_()
  except Exception as e:
    pass
  try:
    global bstack11lll1l111_opy_
    from QWeb.keywords import browser
    bstack11lll1l111_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1l11l1lll1_opy_(CONFIG) and bstack1l111l11ll_opy_():
    if bstack11llll111_opy_() < version.parse(bstack1llll11l1l_opy_):
      logger.error(bstack11l11111l_opy_.format(bstack11llll111_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1l1_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬཌྷ")) and callable(getattr(RemoteConnection, bstack1l1_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ཎ"))):
          RemoteConnection._get_proxy_url = bstack1l1l111l1_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack1l1l111l1_opy_
      except Exception as e:
        logger.error(bstack11ll1l1ll1_opy_.format(str(e)))
  if not CONFIG.get(bstack1l1_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨཏ"), False) and not bstack111lllll1_opy_:
    logger.info(bstack1l1lll11l1_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack1l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫཐ") in CONFIG and str(CONFIG[bstack1l1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬད")]).lower() != bstack1l1_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨདྷ"):
      bstack11l1111l11_opy_()
    elif bstack1ll11ll1l_opy_ != bstack1l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪན") or (bstack1ll11ll1l_opy_ == bstack1l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫཔ") and not bstack111lllll1_opy_):
      bstack1l1lllll11_opy_()
  if (bstack1ll11ll1l_opy_ in [bstack1l1_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫཕ"), bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬབ"), bstack1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨབྷ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack11l1l1l11l_opy_
        bstack1l1l1ll11l_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack111l11l11l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack11111l1l11_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1l1ll111l1_opy_ + str(e))
    except Exception as e:
      bstack1lll1lll1l_opy_(e, bstack111l11l11l_opy_)
    if bstack1ll11ll1l_opy_ != bstack1l1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩམ"):
      bstack11l111lll_opy_()
    bstack1l1l111ll_opy_ = Output.start_test
    bstack11111ll1ll_opy_ = Output.end_test
    bstack1ll1l1l1l_opy_ = TestStatus.__init__
    bstack11l1ll111l_opy_ = pabot._run
    bstack1l111111ll_opy_ = QueueItem.__init__
    bstack1lll11l11l_opy_ = pabot._create_command_for_execution
    bstack1l1lllll1l_opy_ = pabot._report_results
  if bstack1ll11ll1l_opy_ == bstack1l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩཙ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1lll1lll1l_opy_(e, bstack1lll1lllll_opy_)
    bstack11l11ll1l_opy_ = Runner.run_hook
    bstack1l11l1ll1l_opy_ = Step.run
  if bstack1ll11ll1l_opy_ == bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪཚ"):
    try:
      from _pytest.config import Config
      bstack111ll11ll1_opy_ = Config.getoption
      from _pytest import runner
      bstack1l1111lll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1llll1l11_opy_)
    try:
      from pytest_bdd import reporting
      bstack1111l1lll_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬཛ"))
  try:
    framework_name = bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫཛྷ") if bstack1ll11ll1l_opy_ in [bstack1l1_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬཝ"), bstack1l1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ཞ"), bstack1l1_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩཟ")] else bstack11l111111l_opy_(bstack1ll11ll1l_opy_)
    bstack1l1ll1llll_opy_ = {
      bstack1l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧࠪའ"): bstack1l1_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶࠬཡ") if bstack1ll11ll1l_opy_ == bstack1l1_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫར") and bstack1l11l11ll_opy_() else framework_name,
      bstack1l1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩལ"): bstack111lll1l11_opy_(framework_name),
      bstack1l1_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫཤ"): __version__,
      bstack1l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨཥ"): bstack1ll11ll1l_opy_
    }
    if bstack1ll11ll1l_opy_ in bstack1111l1l1l_opy_ + bstack1l1111llll_opy_:
      if bstack11l1111l_opy_.bstack1l1l1llll_opy_(CONFIG):
        if bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨས") in CONFIG:
          os.environ[bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪཧ")] = os.getenv(bstack1l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫཨ"), json.dumps(CONFIG[bstack1l1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫཀྵ")]))
          CONFIG[bstack1l1_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬཪ")].pop(bstack1l1_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫཫ"), None)
          CONFIG[bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧཬ")].pop(bstack1l1_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭཭"), None)
        bstack1l1ll1llll_opy_[bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ཮")] = {
          bstack1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨ཯"): bstack1l1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭཰"),
          bstack1l1_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳཱ࠭"): str(bstack11llll111_opy_())
        }
    if bstack1ll11ll1l_opy_ not in [bstack1l1_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲིࠧ")] and not cli.is_running():
      bstack1ll111111l_opy_, bstack11111l1ll_opy_ = bstack1l11llll_opy_.launch(CONFIG, bstack1l1ll1llll_opy_)
      if bstack11111l1ll_opy_.get(bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿཱིࠧ")) is not None and bstack11l1111l_opy_.bstack11111llll_opy_(CONFIG) is None:
        value = bstack11111l1ll_opy_[bstack1l1_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨུ")].get(bstack1l1_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵཱུࠪ"))
        if value is not None:
            CONFIG[bstack1l1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪྲྀ")] = value
        else:
          logger.debug(bstack1l1_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡥࡣࡷࡥࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤཷ"))
  except Exception as e:
    logger.debug(bstack11lllll11l_opy_.format(bstack1l1_opy_ (u"࡚ࠬࡥࡴࡶࡋࡹࡧ࠭ླྀ"), str(e)))
  if bstack1ll11ll1l_opy_ == bstack1l1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ཹ"):
    bstack1l111ll111_opy_ = True
    if bstack111lllll1_opy_ and bstack11lll11111_opy_:
      bstack1l11lll1l_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶེࠫ"), {}).get(bstack1l1_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴཻࠪ"))
      bstack1ll11l1111_opy_(bstack11l1lll1ll_opy_)
    elif bstack111lllll1_opy_:
      bstack1l11lll1l_opy_ = CONFIG.get(bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸོ࠭"), {}).get(bstack1l1_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶཽࠬ"))
      global bstack11lll11ll_opy_
      try:
        if bstack11l1l11l1_opy_(bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧཾ")]) and multiprocessing.current_process().name == bstack1l1_opy_ (u"ࠬ࠶ࠧཿ"):
          bstack111lllll1_opy_[bstack1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦྀࠩ")].remove(bstack1l1_opy_ (u"ࠧ࠮࡯ཱྀࠪ"))
          bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྂ")].remove(bstack1l1_opy_ (u"ࠩࡳࡨࡧ࠭ྃ"))
          bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ྄࠭")] = bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ྅")][0]
          with open(bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ྆")], bstack1l1_opy_ (u"࠭ࡲࠨ྇")) as f:
            file_content = f.read()
          bstack1l1l11l1ll_opy_ = bstack1l1_opy_ (u"ࠢࠣࠤࡩࡶࡴࡳࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡥ࡭ࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡁࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࠫࡿࢂ࠯࠻ࠡࡨࡵࡳࡲࠦࡰࡥࡤࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡔࡩࡨ࠻ࠡࡱࡪࡣࡩࡨࠠ࠾ࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡥࡧࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯࠭ࡹࡥ࡭ࡨ࠯ࠤࡦࡸࡧ࠭ࠢࡷࡩࡲࡶ࡯ࡳࡣࡵࡽࠥࡃࠠ࠱ࠫ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡶࡾࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡢࡴࡪࠤࡂࠦࡳࡵࡴࠫ࡭ࡳࡺࠨࡢࡴࡪ࠭࠰࠷࠰ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦࡺࡦࡩࡵࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡥࡸࠦࡥ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡸࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡵࡧࡠࡦࡥࠬࡸ࡫࡬ࡧ࠮ࡤࡶ࡬࠲ࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡥࡤ࠱ࡨࡴࡥࡢࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫ࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠮ࠩ࠯ࡵࡨࡸࡤࡺࡲࡢࡥࡨࠬ࠮ࡢ࡮ࠣࠤࠥྈ").format(str(bstack111lllll1_opy_))
          bstack111l11l1ll_opy_ = bstack1l1l11l1ll_opy_ + file_content
          bstack1lll11l1l1_opy_ = bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྉ")] + bstack1l1_opy_ (u"ࠩࡢࡦࡸࡺࡡࡤ࡭ࡢࡸࡪࡳࡰ࠯ࡲࡼࠫྊ")
          with open(bstack1lll11l1l1_opy_, bstack1l1_opy_ (u"ࠪࡻࠬྋ")):
            pass
          with open(bstack1lll11l1l1_opy_, bstack1l1_opy_ (u"ࠦࡼ࠱ࠢྌ")) as f:
            f.write(bstack111l11l1ll_opy_)
          import subprocess
          process_data = subprocess.run([bstack1l1_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧྍ"), bstack1lll11l1l1_opy_])
          if os.path.exists(bstack1lll11l1l1_opy_):
            os.unlink(bstack1lll11l1l1_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack11l1l11l1_opy_(bstack111lllll1_opy_[bstack1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྎ")]):
            bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྏ")].remove(bstack1l1_opy_ (u"ࠨ࠯ࡰࠫྐ"))
            bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྑ")].remove(bstack1l1_opy_ (u"ࠪࡴࡩࡨࠧྒ"))
            bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྒྷ")] = bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྔ")][0]
          bstack1ll11l1111_opy_(bstack11l1lll1ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack111lllll1_opy_[bstack1l1_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྕ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1l1_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩྖ")] = bstack1l1_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪྗ")
          mod_globals[bstack1l1_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫ྘")] = os.path.abspath(bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྙ")])
          exec(open(bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྚ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1l1_opy_ (u"ࠬࡉࡡࡶࡩ࡫ࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠬྛ").format(str(e)))
          for driver in bstack11lll11ll_opy_:
            bstack1l1llll11l_opy_.append({
              bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫྜ"): bstack111lllll1_opy_[bstack1l1_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྜྷ")],
              bstack1l1_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧྞ"): str(e),
              bstack1l1_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨྟ"): multiprocessing.current_process().name
            })
            bstack1l1ll11l11_opy_(driver, bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪྠ"), bstack1l1_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢྡ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack11lll11ll_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11l11ll1ll_opy_, CONFIG, logger)
      bstack1ll1lllll_opy_()
      bstack1llll1111l_opy_()
      percy.bstack1ll11111ll_opy_()
      bstack1llllll1l_opy_ = {
        bstack1l1_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྡྷ"): args[0],
        bstack1l1_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭ྣ"): CONFIG,
        bstack1l1_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨྤ"): bstack111111ll11_opy_,
        bstack1l1_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪྥ"): bstack11l11ll1ll_opy_
      }
      if bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬྦ") in CONFIG:
        bstack1111ll1ll_opy_ = bstack1ll1l111l1_opy_(args, logger, CONFIG, bstack1ll11ll1ll_opy_, bstack11l1l111l_opy_)
        bstack1ll11l11l1_opy_ = bstack1111ll1ll_opy_.bstack1lll11ll1_opy_(run_on_browserstack, bstack1llllll1l_opy_, bstack11l1l11l1_opy_(args))
      else:
        if bstack11l1l11l1_opy_(args):
          bstack1llllll1l_opy_[bstack1l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྦྷ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1llllll1l_opy_,))
          test.start()
          test.join()
        else:
          bstack1ll11l1111_opy_(bstack11l1lll1ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1l1_opy_ (u"ࠫࡤࡥ࡮ࡢ࡯ࡨࡣࡤ࠭ྨ")] = bstack1l1_opy_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧྩ")
          mod_globals[bstack1l1_opy_ (u"࠭࡟ࡠࡨ࡬ࡰࡪࡥ࡟ࠨྪ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1ll11ll1l_opy_ == bstack1l1_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ྫ") or bstack1ll11ll1l_opy_ == bstack1l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧྫྷ"):
    percy.init(bstack11l11ll1ll_opy_, CONFIG, logger)
    percy.bstack1ll11111ll_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1lll1lll1l_opy_(e, bstack111l11l11l_opy_)
    bstack1ll1lllll_opy_()
    bstack1ll11l1111_opy_(bstack1111ll111l_opy_)
    if bstack1ll11ll1ll_opy_:
      bstack11ll111l1_opy_(bstack1111ll111l_opy_, args)
      if bstack1l1_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧྭ") in args:
        i = args.index(bstack1l1_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨྮ"))
        args.pop(i)
        args.pop(i)
      if bstack1l1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྯ") not in CONFIG:
        CONFIG[bstack1l1_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨྰ")] = [{}]
        bstack11l1l111l_opy_ = 1
      if bstack11lllllll1_opy_ == 0:
        bstack11lllllll1_opy_ = 1
      args.insert(0, str(bstack11lllllll1_opy_))
      args.insert(0, str(bstack1l1_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫྱ")))
    if bstack1l11llll_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1l11ll1111_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack11ll1111l1_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1l1_opy_ (u"ࠢࡓࡑࡅࡓ࡙ࡥࡏࡑࡖࡌࡓࡓ࡙ࠢྲ"),
        ).parse_args(bstack1l11ll1111_opy_)
        bstack11ll1llll_opy_ = args.index(bstack1l11ll1111_opy_[0]) if len(bstack1l11ll1111_opy_) > 0 else len(args)
        args.insert(bstack11ll1llll_opy_, str(bstack1l1_opy_ (u"ࠨ࠯࠰ࡰ࡮ࡹࡴࡦࡰࡨࡶࠬླ")))
        args.insert(bstack11ll1llll_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡵࡳࡧࡵࡴࡠ࡮࡬ࡷࡹ࡫࡮ࡦࡴ࠱ࡴࡾ࠭ྴ"))))
        if bstack111lll1l_opy_.bstack1lll1l11l_opy_(CONFIG):
          args.insert(bstack11ll1llll_opy_, str(bstack1l1_opy_ (u"ࠪ࠱࠲ࡲࡩࡴࡶࡨࡲࡪࡸࠧྵ")))
          args.insert(bstack11ll1llll_opy_ + 1, str(bstack1l1_opy_ (u"ࠫࡗ࡫ࡴࡳࡻࡉࡥ࡮ࡲࡥࡥ࠼ࡾࢁࠬྶ").format(bstack111lll1l_opy_.bstack111l1l11_opy_(CONFIG))))
        if bstack1ll1111ll1_opy_(os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࠪྷ"))) and str(os.environ.get(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠪྸ"), bstack1l1_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬྐྵ"))) != bstack1l1_opy_ (u"ࠨࡰࡸࡰࡱ࠭ྺ"):
          for bstack1ll1111l11_opy_ in bstack11ll1111l1_opy_:
            args.remove(bstack1ll1111l11_opy_)
          test_files = os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘ࠭ྻ")).split(bstack1l1_opy_ (u"ࠪ࠰ࠬྼ"))
          for bstack11l1111111_opy_ in test_files:
            args.append(bstack11l1111111_opy_)
      except Exception as e:
        logger.error(bstack1l1_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡤࡸࡹࡧࡣࡩ࡫ࡱ࡫ࠥࡲࡩࡴࡶࡨࡲࡪࡸࠠࡧࡱࡵࠤࢀࢃ࠮ࠡࡇࡵࡶࡴࡸࠠ࠮ࠢࡾࢁࠧ྽").format(bstack1111111l1_opy_, e))
    pabot.main(args)
  elif bstack1ll11ll1l_opy_ == bstack1l1_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭྾"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1lll1lll1l_opy_(e, bstack111l11l11l_opy_)
    for a in args:
      if bstack1l1_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜ࠬ྿") in a:
        bstack1l1l11l1l_opy_ = int(a.split(bstack1l1_opy_ (u"ࠧ࠻ࠩ࿀"))[1])
      if bstack1l1_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ࿁") in a:
        bstack1l11lll1l_opy_ = str(a.split(bstack1l1_opy_ (u"ࠩ࠽ࠫ࿂"))[1])
      if bstack1l1_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕࠪ࿃") in a:
        bstack11l1l1lll1_opy_ = str(a.split(bstack1l1_opy_ (u"ࠫ࠿࠭࿄"))[1])
    bstack11ll1ll1l1_opy_ = None
    if bstack1l1_opy_ (u"ࠬ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠫ࿅") in args:
      i = args.index(bstack1l1_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼ࿆ࠬ"))
      args.pop(i)
      bstack11ll1ll1l1_opy_ = args.pop(i)
    if bstack11ll1ll1l1_opy_ is not None:
      global bstack111lll1l1_opy_
      bstack111lll1l1_opy_ = bstack11ll1ll1l1_opy_
    bstack1ll11l1111_opy_(bstack1111ll111l_opy_)
    run_cli(args)
    if bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡦࡴࡵࡳࡷࡥ࡬ࡪࡵࡷࠫ࿇") in multiprocessing.current_process().__dict__.keys():
      for bstack111l11l1l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l1llll11l_opy_.append(bstack111l11l1l_opy_)
  elif bstack1ll11ll1l_opy_ == bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ࿈"):
    bstack1l1lll1111_opy_ = bstack111111ll_opy_(args, logger, CONFIG, bstack1ll11ll1ll_opy_)
    bstack1l1lll1111_opy_.bstack1lllll1ll_opy_()
    bstack1ll1lllll_opy_()
    bstack1l1l1l11ll_opy_ = True
    bstack11ll1l1l1l_opy_ = bstack1l1lll1111_opy_.bstack1lll1lll1_opy_()
    bstack1l1lll1111_opy_.bstack1llllll1l_opy_(bstack1111llll11_opy_)
    bstack1l1lll1111_opy_.bstack111l11ll_opy_()
    bstack11l1ll1l1l_opy_(bstack1ll11ll1l_opy_, CONFIG, bstack1l1lll1111_opy_.bstack1llllllll_opy_())
    bstack1l1l1lllll_opy_ = bstack1l1lll1111_opy_.bstack1lll11ll1_opy_(bstack1l111ll11_opy_, {
      bstack1l1_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪ࿉"): bstack111111ll11_opy_,
      bstack1l1_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ࿊"): bstack11l11ll1ll_opy_,
      bstack1l1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ࿋"): bstack1ll11ll1ll_opy_
    })
    try:
      bstack1llll1ll1l_opy_, bstack1l111l1l1l_opy_ = map(list, zip(*bstack1l1l1lllll_opy_))
      bstack11lllll11_opy_ = bstack1llll1ll1l_opy_[0]
      for status_code in bstack1l111l1l1l_opy_:
        if status_code != 0:
          bstack11l111l11_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡤࡺࡪࠦࡥࡳࡴࡲࡶࡸࠦࡡ࡯ࡦࠣࡷࡹࡧࡴࡶࡵࠣࡧࡴࡪࡥ࠯ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡀࠠࡼࡿࠥ࿌").format(str(e)))
  elif bstack1ll11ll1l_opy_ == bstack1l1_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭࿍"):
    try:
      from behave.__main__ import main as bstack1lllll1l11_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1lll1lll1l_opy_(e, bstack1lll1lllll_opy_)
    bstack1ll1lllll_opy_()
    bstack1l1l1l11ll_opy_ = True
    bstack111l111l_opy_ = 1
    if bstack1l1_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ࿎") in CONFIG:
      bstack111l111l_opy_ = CONFIG[bstack1l1_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ࿏")]
    if bstack1l1_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ࿐") in CONFIG:
      bstack111ll11111_opy_ = int(bstack111l111l_opy_) * int(len(CONFIG[bstack1l1_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭࿑")]))
    else:
      bstack111ll11111_opy_ = int(bstack111l111l_opy_)
    config = Configuration(args)
    bstack1111l11ll_opy_ = config.paths
    if len(bstack1111l11ll_opy_) == 0:
      import glob
      pattern = bstack1l1_opy_ (u"ࠫ࠯࠰࠯ࠫ࠰ࡩࡩࡦࡺࡵࡳࡧࠪ࿒")
      bstack11lll1111_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11lll1111_opy_)
      config = Configuration(args)
      bstack1111l11ll_opy_ = config.paths
    bstack1lll1ll1l_opy_ = [os.path.normpath(item) for item in bstack1111l11ll_opy_]
    bstack1l11llll1_opy_ = [os.path.normpath(item) for item in args]
    bstack111lll1111_opy_ = [item for item in bstack1l11llll1_opy_ if item not in bstack1lll1ll1l_opy_]
    import platform as pf
    if pf.system().lower() == bstack1l1_opy_ (u"ࠬࡽࡩ࡯ࡦࡲࡻࡸ࠭࿓"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1lll1ll1l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11ll1lll1l_opy_)))
                    for bstack11ll1lll1l_opy_ in bstack1lll1ll1l_opy_]
    bstack1lll1l1l1_opy_ = []
    for spec in bstack1lll1ll1l_opy_:
      bstack111l1111_opy_ = []
      bstack111l1111_opy_ += bstack111lll1111_opy_
      bstack111l1111_opy_.append(spec)
      bstack1lll1l1l1_opy_.append(bstack111l1111_opy_)
    execution_items = []
    for bstack111l1111_opy_ in bstack1lll1l1l1_opy_:
      if bstack1l1_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ࿔") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿕")]):
          item = {}
          item[bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࠬ࿖")] = bstack1l1_opy_ (u"ࠩࠣࠫ࿗").join(bstack111l1111_opy_)
          item[bstack1l1_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ࿘")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack1l1_opy_ (u"ࠫࡦࡸࡧࠨ࿙")] = bstack1l1_opy_ (u"ࠬࠦࠧ࿚").join(bstack111l1111_opy_)
        item[bstack1l1_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ࿛")] = 0
        execution_items.append(item)
    bstack1l1llll1ll_opy_ = bstack11l1l1ll1_opy_(execution_items, bstack111ll11111_opy_)
    for execution_item in bstack1l1llll1ll_opy_:
      bstack111l1lll_opy_ = []
      for item in execution_item:
        bstack111l1lll_opy_.append(bstack11111111l_opy_(name=str(item[bstack1l1_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭࿜")]),
                                             target=bstack111l11111l_opy_,
                                             args=(item[bstack1l1_opy_ (u"ࠨࡣࡵ࡫ࠬ࿝")],)))
      for t in bstack111l1lll_opy_:
        t.start()
      for t in bstack111l1lll_opy_:
        t.join()
  else:
    bstack1ll1llll1l_opy_(bstack1l1ll11ll1_opy_)
  if not bstack111lllll1_opy_:
    bstack11ll1l111_opy_()
    if(bstack1ll11ll1l_opy_ in [bstack1l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ࿞"), bstack1l1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ࿟")]):
      bstack111l1ll1ll_opy_()
  bstack1ll1111l1_opy_.bstack1l1111l1ll_opy_()
def browserstack_initialize(bstack11111lll11_opy_=None):
  logger.info(bstack1l1_opy_ (u"ࠫࡗࡻ࡮࡯࡫ࡱ࡫࡙ࠥࡄࡌࠢࡺ࡭ࡹ࡮ࠠࡢࡴࡪࡷ࠿ࠦࠧ࿠") + str(bstack11111lll11_opy_))
  run_on_browserstack(bstack11111lll11_opy_, None, True)
@measure(event_name=EVENTS.bstack1l1llllll_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack11ll1l111_opy_():
  global CONFIG
  global bstack11lll1l1l1_opy_
  global bstack11l111l11_opy_
  global bstack1ll1l1lll_opy_
  global bstack11l11111_opy_
  bstack1111lll1l_opy_.bstack1ll11lll1l_opy_()
  if cli.is_running():
    bstack1llllll1ll_opy_.invoke(Events.bstack111l1l11l_opy_)
  else:
    bstack1111ll11_opy_ = bstack111lll1l_opy_.bstack1111ll1l_opy_(config=CONFIG)
    bstack1111ll11_opy_.bstack1l1lllllll_opy_(CONFIG)
  if bstack11lll1l1l1_opy_ == bstack1l1_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ࿡"):
    if not cli.is_enabled(CONFIG):
      bstack1l11llll_opy_.stop()
  else:
    bstack1l11llll_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1l111ll1_opy_.bstack11ll11l1l1_opy_()
  if bstack1l1_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ࿢") in CONFIG and str(CONFIG[bstack1l1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ࿣")]).lower() != bstack1l1_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ࿤"):
    hashed_id, bstack1ll1111lll_opy_ = bstack1llllll1l1_opy_()
  else:
    hashed_id, bstack1ll1111lll_opy_ = get_build_link()
  bstack11llll1l1_opy_(hashed_id)
  logger.info(bstack1l1_opy_ (u"ࠩࡖࡈࡐࠦࡲࡶࡰࠣࡩࡳࡪࡥࡥࠢࡩࡳࡷࠦࡩࡥ࠼ࠪ࿥") + bstack11l11111_opy_.get_property(bstack1l1_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ࿦"), bstack1l1_opy_ (u"ࠫࠬ࿧")) + bstack1l1_opy_ (u"ࠬ࠲ࠠࡵࡧࡶࡸ࡭ࡻࡢࠡ࡫ࡧ࠾ࠥ࠭࿨") + os.getenv(bstack1l1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ࿩"), bstack1l1_opy_ (u"ࠧࠨ࿪")))
  if hashed_id is not None and bstack111ll111ll_opy_() != -1:
    sessions = bstack11lllll111_opy_(hashed_id)
    bstack11l1111ll1_opy_(sessions, bstack1ll1111lll_opy_)
  if bstack11lll1l1l1_opy_ == bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ࿫") and bstack11l111l11_opy_ != 0:
    sys.exit(bstack11l111l11_opy_)
  if bstack11lll1l1l1_opy_ == bstack1l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ࿬") and bstack1ll1l1lll_opy_ != 0:
    sys.exit(bstack1ll1l1lll_opy_)
def bstack11llll1l1_opy_(new_id):
    global bstack1ll111111_opy_
    bstack1ll111111_opy_ = new_id
def bstack11l111111l_opy_(bstack1l1ll1l1l1_opy_):
  if bstack1l1ll1l1l1_opy_:
    return bstack1l1ll1l1l1_opy_.capitalize()
  else:
    return bstack1l1_opy_ (u"ࠪࠫ࿭")
@measure(event_name=EVENTS.bstack11ll11lll1_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1ll111lll_opy_(bstack11ll1l1111_opy_):
  if bstack1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ࿮") in bstack11ll1l1111_opy_ and bstack11ll1l1111_opy_[bstack1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ࿯")] != bstack1l1_opy_ (u"࠭ࠧ࿰"):
    return bstack11ll1l1111_opy_[bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ࿱")]
  else:
    bstack1lll1ll111_opy_ = bstack1l1_opy_ (u"ࠣࠤ࿲")
    if bstack1l1_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ࿳") in bstack11ll1l1111_opy_ and bstack11ll1l1111_opy_[bstack1l1_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪ࿴")] != None:
      bstack1lll1ll111_opy_ += bstack11ll1l1111_opy_[bstack1l1_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ࿵")] + bstack1l1_opy_ (u"ࠧ࠲ࠠࠣ࿶")
      if bstack11ll1l1111_opy_[bstack1l1_opy_ (u"࠭࡯ࡴࠩ࿷")] == bstack1l1_opy_ (u"ࠢࡪࡱࡶࠦ࿸"):
        bstack1lll1ll111_opy_ += bstack1l1_opy_ (u"ࠣ࡫ࡒࡗࠥࠨ࿹")
      bstack1lll1ll111_opy_ += (bstack11ll1l1111_opy_[bstack1l1_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭࿺")] or bstack1l1_opy_ (u"ࠪࠫ࿻"))
      return bstack1lll1ll111_opy_
    else:
      bstack1lll1ll111_opy_ += bstack11l111111l_opy_(bstack11ll1l1111_opy_[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬ࿼")]) + bstack1l1_opy_ (u"ࠧࠦࠢ࿽") + (
              bstack11ll1l1111_opy_[bstack1l1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ࿾")] or bstack1l1_opy_ (u"ࠧࠨ࿿")) + bstack1l1_opy_ (u"ࠣ࠮ࠣࠦက")
      if bstack11ll1l1111_opy_[bstack1l1_opy_ (u"ࠩࡲࡷࠬခ")] == bstack1l1_opy_ (u"࡛ࠥ࡮ࡴࡤࡰࡹࡶࠦဂ"):
        bstack1lll1ll111_opy_ += bstack1l1_opy_ (u"ࠦ࡜࡯࡮ࠡࠤဃ")
      bstack1lll1ll111_opy_ += bstack11ll1l1111_opy_[bstack1l1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩင")] or bstack1l1_opy_ (u"࠭ࠧစ")
      return bstack1lll1ll111_opy_
@measure(event_name=EVENTS.bstack111l1l111_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack1l1111111l_opy_(bstack11ll1111ll_opy_):
  if bstack11ll1111ll_opy_ == bstack1l1_opy_ (u"ࠢࡥࡱࡱࡩࠧဆ"):
    return bstack1l1_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽࡫ࡷ࡫ࡥ࡯࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥ࡫ࡷ࡫ࡥ࡯ࠤࡁࡇࡴࡳࡰ࡭ࡧࡷࡩࡩࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫဇ")
  elif bstack11ll1111ll_opy_ == bstack1l1_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤဈ"):
    return bstack1l1_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡸࡥࡥ࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡶࡪࡪࠢ࠿ࡈࡤ࡭ࡱ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ဉ")
  elif bstack11ll1111ll_opy_ == bstack1l1_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦည"):
    return bstack1l1_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡨࡴࡨࡩࡳࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡨࡴࡨࡩࡳࠨ࠾ࡑࡣࡶࡷࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬဋ")
  elif bstack11ll1111ll_opy_ == bstack1l1_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧဌ"):
    return bstack1l1_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡵࡩࡩࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡳࡧࡧࠦࡃࡋࡲࡳࡱࡵࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩဍ")
  elif bstack11ll1111ll_opy_ == bstack1l1_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࠤဎ"):
    return bstack1l1_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࠨ࡫ࡥࡢ࠵࠵࠺ࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࠣࡦࡧࡤ࠷࠷࠼ࠢ࠿ࡖ࡬ࡱࡪࡵࡵࡵ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧဏ")
  elif bstack11ll1111ll_opy_ == bstack1l1_opy_ (u"ࠥࡶࡺࡴ࡮ࡪࡰࡪࠦတ"):
    return bstack1l1_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡢ࡭ࡣࡦ࡯ࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡢ࡭ࡣࡦ࡯ࠧࡄࡒࡶࡰࡱ࡭ࡳ࡭࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬထ")
  else:
    return bstack1l1_opy_ (u"ࠬࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡤ࡯ࡥࡨࡱ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡤ࡯ࡥࡨࡱࠢ࠿ࠩဒ") + bstack11l111111l_opy_(
      bstack11ll1111ll_opy_) + bstack1l1_opy_ (u"࠭࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬဓ")
def bstack111lll111_opy_(session):
  return bstack1l1_opy_ (u"ࠧ࠽ࡶࡵࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡷࡵࡷࠣࡀ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠲ࡴࡡ࡮ࡧࠥࡂࡁࡧࠠࡩࡴࡨࡪࡂࠨࡻࡾࠤࠣࡸࡦࡸࡧࡦࡶࡀࠦࡤࡨ࡬ࡢࡰ࡮ࠦࡃࢁࡽ࠽࠱ࡤࡂࡁ࠵ࡴࡥࡀࡾࢁࢀࢃ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾࠲ࡸࡷࡄࠧန").format(
    session[bstack1l1_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣࡠࡷࡵࡰࠬပ")], bstack1ll111lll_opy_(session), bstack1l1111111l_opy_(session[bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡷࡥࡹࡻࡳࠨဖ")]),
    bstack1l1111111l_opy_(session[bstack1l1_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪဗ")]),
    bstack11l111111l_opy_(session[bstack1l1_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࠬဘ")] or session[bstack1l1_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬမ")] or bstack1l1_opy_ (u"࠭ࠧယ")) + bstack1l1_opy_ (u"ࠢࠡࠤရ") + (session[bstack1l1_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪလ")] or bstack1l1_opy_ (u"ࠩࠪဝ")),
    session[bstack1l1_opy_ (u"ࠪࡳࡸ࠭သ")] + bstack1l1_opy_ (u"ࠦࠥࠨဟ") + session[bstack1l1_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩဠ")], session[bstack1l1_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨအ")] or bstack1l1_opy_ (u"ࠧࠨဢ"),
    session[bstack1l1_opy_ (u"ࠨࡥࡵࡩࡦࡺࡥࡥࡡࡤࡸࠬဣ")] if session[bstack1l1_opy_ (u"ࠩࡦࡶࡪࡧࡴࡦࡦࡢࡥࡹ࠭ဤ")] else bstack1l1_opy_ (u"ࠪࠫဥ"))
@measure(event_name=EVENTS.bstack11l111llll_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def bstack11l1111ll1_opy_(sessions, bstack1ll1111lll_opy_):
  try:
    bstack1l1111l11_opy_ = bstack1l1_opy_ (u"ࠦࠧဦ")
    if not os.path.exists(bstack11l11llll1_opy_):
      os.mkdir(bstack11l11llll1_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l1_opy_ (u"ࠬࡧࡳࡴࡧࡷࡷ࠴ࡸࡥࡱࡱࡵࡸ࠳࡮ࡴ࡮࡮ࠪဧ")), bstack1l1_opy_ (u"࠭ࡲࠨဨ")) as f:
      bstack1l1111l11_opy_ = f.read()
    bstack1l1111l11_opy_ = bstack1l1111l11_opy_.replace(bstack1l1_opy_ (u"ࠧࡼࠧࡕࡉࡘ࡛ࡌࡕࡕࡢࡇࡔ࡛ࡎࡕࠧࢀࠫဩ"), str(len(sessions)))
    bstack1l1111l11_opy_ = bstack1l1111l11_opy_.replace(bstack1l1_opy_ (u"ࠨࡽࠨࡆ࡚ࡏࡌࡅࡡࡘࡖࡑࠫࡽࠨဪ"), bstack1ll1111lll_opy_)
    bstack1l1111l11_opy_ = bstack1l1111l11_opy_.replace(bstack1l1_opy_ (u"ࠩࡾࠩࡇ࡛ࡉࡍࡆࡢࡒࡆࡓࡅࠦࡿࠪါ"),
                                              sessions[0].get(bstack1l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡱࡥࡲ࡫ࠧာ")) if sessions[0] else bstack1l1_opy_ (u"ࠫࠬိ"))
    with open(os.path.join(bstack11l11llll1_opy_, bstack1l1_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡷ࡫ࡰࡰࡴࡷ࠲࡭ࡺ࡭࡭ࠩီ")), bstack1l1_opy_ (u"࠭ࡷࠨု")) as stream:
      stream.write(bstack1l1111l11_opy_.split(bstack1l1_opy_ (u"ࠧࡼࠧࡖࡉࡘ࡙ࡉࡐࡐࡖࡣࡉࡇࡔࡂࠧࢀࠫူ"))[0])
      for session in sessions:
        stream.write(bstack111lll111_opy_(session))
      stream.write(bstack1l1111l11_opy_.split(bstack1l1_opy_ (u"ࠨࡽࠨࡗࡊ࡙ࡓࡊࡑࡑࡗࡤࡊࡁࡕࡃࠨࢁࠬေ"))[1])
    logger.info(bstack1l1_opy_ (u"ࠩࡊࡩࡳ࡫ࡲࡢࡶࡨࡨࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡧࡻࡩ࡭ࡦࠣࡥࡷࡺࡩࡧࡣࡦࡸࡸࠦࡡࡵࠢࡾࢁࠬဲ").format(bstack11l11llll1_opy_));
  except Exception as e:
    logger.debug(bstack11ll111lll_opy_.format(str(e)))
def bstack11lllll111_opy_(hashed_id):
  global CONFIG
  try:
    bstack1l1ll111l_opy_ = datetime.datetime.now()
    host = bstack1l1_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪဳ") if bstack1l1_opy_ (u"ࠫࡦࡶࡰࠨဴ") in CONFIG else bstack1l1_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ဵ")
    user = CONFIG[bstack1l1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨံ")]
    key = CONFIG[bstack1l1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻ့ࠪ")]
    bstack11l11llll_opy_ = bstack1l1_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧး") if bstack1l1_opy_ (u"ࠩࡤࡴࡵ္࠭") in CONFIG else (bstack1l1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫်ࠧ") if CONFIG.get(bstack1l1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨျ")) else bstack1l1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧြ"))
    host = bstack11ll11llll_opy_(cli.config, [bstack1l1_opy_ (u"ࠨࡡࡱ࡫ࡶࠦွ"), bstack1l1_opy_ (u"ࠢࡢࡲࡳࡅࡺࡺ࡯࡮ࡣࡷࡩࠧှ"), bstack1l1_opy_ (u"ࠣࡣࡳ࡭ࠧဿ")], host) if bstack1l1_opy_ (u"ࠩࡤࡴࡵ࠭၀") in CONFIG else bstack11ll11llll_opy_(cli.config, [bstack1l1_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ၁"), bstack1l1_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ၂"), bstack1l1_opy_ (u"ࠧࡧࡰࡪࠤ၃")], host)
    url = bstack1l1_opy_ (u"࠭ࡻࡾ࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡵࡨࡷࡸ࡯࡯࡯ࡵ࠱࡮ࡸࡵ࡮ࠨ၄").format(host, bstack11l11llll_opy_, hashed_id)
    headers = {
      bstack1l1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭၅"): bstack1l1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ၆"),
    }
    proxies = bstack1111ll1lll_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡨࡧࡷࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡸࡥ࡬ࡪࡵࡷࠦ၇"), datetime.datetime.now() - bstack1l1ll111l_opy_)
      return list(map(lambda session: session[bstack1l1_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ၈")], response.json()))
  except Exception as e:
    logger.debug(bstack11l1l1ll1l_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack111l111l11_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def get_build_link():
  global CONFIG
  global bstack1ll111111_opy_
  try:
    if bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ၉") in CONFIG:
      bstack1l1ll111l_opy_ = datetime.datetime.now()
      host = bstack1l1_opy_ (u"ࠬࡧࡰࡪ࠯ࡦࡰࡴࡻࡤࠨ၊") if bstack1l1_opy_ (u"࠭ࡡࡱࡲࠪ။") in CONFIG else bstack1l1_opy_ (u"ࠧࡢࡲ࡬ࠫ၌")
      user = CONFIG[bstack1l1_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ၍")]
      key = CONFIG[bstack1l1_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ၎")]
      bstack11l11llll_opy_ = bstack1l1_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩ၏") if bstack1l1_opy_ (u"ࠫࡦࡶࡰࠨၐ") in CONFIG else bstack1l1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧၑ")
      url = bstack1l1_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡼࡿ࠽ࡿࢂࡆࡻࡾ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠯࡬ࡶࡳࡳ࠭ၒ").format(user, key, host, bstack11l11llll_opy_)
      if cli.is_enabled(CONFIG):
        bstack1ll1111lll_opy_, hashed_id = cli.bstack111lll1l1l_opy_()
        logger.info(bstack1l1l1ll1l_opy_.format(bstack1ll1111lll_opy_))
        return [hashed_id, bstack1ll1111lll_opy_]
      else:
        headers = {
          bstack1l1_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭ၓ"): bstack1l1_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫၔ"),
        }
        if bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫၕ") in CONFIG:
          params = {bstack1l1_opy_ (u"ࠪࡲࡦࡳࡥࠨၖ"): CONFIG[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧၗ")], bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨၘ"): CONFIG[bstack1l1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨၙ")]}
        else:
          params = {bstack1l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬၚ"): CONFIG[bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫၛ")]}
        proxies = bstack1111ll1lll_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack1l111111l1_opy_ = response.json()[0][bstack1l1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡢࡶ࡫࡯ࡨࠬၜ")]
          if bstack1l111111l1_opy_:
            bstack1ll1111lll_opy_ = bstack1l111111l1_opy_[bstack1l1_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧၝ")].split(bstack1l1_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦ࠱ࡧࡻࡩ࡭ࡦࠪၞ"))[0] + bstack1l1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡷ࠴࠭ၟ") + bstack1l111111l1_opy_[
              bstack1l1_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩၠ")]
            logger.info(bstack1l1l1ll1l_opy_.format(bstack1ll1111lll_opy_))
            bstack1ll111111_opy_ = bstack1l111111l1_opy_[bstack1l1_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪၡ")]
            bstack11llllllll_opy_ = CONFIG[bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫၢ")]
            if bstack1l1_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫၣ") in CONFIG:
              bstack11llllllll_opy_ += bstack1l1_opy_ (u"ࠪࠤࠬၤ") + CONFIG[bstack1l1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ၥ")]
            if bstack11llllllll_opy_ != bstack1l111111l1_opy_[bstack1l1_opy_ (u"ࠬࡴࡡ࡮ࡧࠪၦ")]:
              logger.debug(bstack1l11l1l1l_opy_.format(bstack1l111111l1_opy_[bstack1l1_opy_ (u"࠭࡮ࡢ࡯ࡨࠫၧ")], bstack11llllllll_opy_))
            cli.bstack111l1l11l1_opy_(bstack1l1_opy_ (u"ࠢࡩࡶࡷࡴ࠿࡭ࡥࡵࡡࡥࡹ࡮ࡲࡤࡠ࡮࡬ࡲࡰࠨၨ"), datetime.datetime.now() - bstack1l1ll111l_opy_)
            return [bstack1l111111l1_opy_[bstack1l1_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫၩ")], bstack1ll1111lll_opy_]
    else:
      logger.warn(bstack11l111l11l_opy_)
  except Exception as e:
    logger.debug(bstack11111l11l_opy_.format(str(e)))
  return [None, None]
def bstack11llll1l11_opy_(url, bstack1llll1l111_opy_=False):
  global CONFIG
  global bstack1ll1l1l1l1_opy_
  if not bstack1ll1l1l1l1_opy_:
    hostname = bstack1lll1ll11l_opy_(url)
    is_private = bstack1l1l1l1l11_opy_(hostname)
    if (bstack1l1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ၪ") in CONFIG and not bstack1ll1111ll1_opy_(CONFIG[bstack1l1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧၫ")])) and (is_private or bstack1llll1l111_opy_):
      bstack1ll1l1l1l1_opy_ = hostname
def bstack1lll1ll11l_opy_(url):
  return urlparse(url).hostname
def bstack1l1l1l1l11_opy_(hostname):
  for bstack1l11ll111l_opy_ in bstack1111l1l11_opy_:
    regex = re.compile(bstack1l11ll111l_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack11llll1ll1_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack11l111l1l_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1l1l11l1l_opy_
  bstack1llll111l1_opy_ = not (bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၬ"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၭ"), None))
  bstack111l1l1lll_opy_ = getattr(driver, bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ၮ"), None) != True
  bstack11l11l11ll_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၯ"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၰ"), None)
  if bstack11l11l11ll_opy_:
    if not bstack1ll11l1ll1_opy_():
      logger.warning(bstack1l1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷ࠳ࠨၱ"))
      return {}
    logger.debug(bstack1l1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧၲ"))
    logger.debug(perform_scan(driver, driver_command=bstack1l1_opy_ (u"ࠫࡪࡾࡥࡤࡷࡷࡩࡘࡩࡲࡪࡲࡷࠫၳ")))
    results = bstack11l1l11l11_opy_(bstack1l1_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸࡸࠨၴ"))
    if results is not None and results.get(bstack1l1_opy_ (u"ࠨࡩࡴࡵࡸࡩࡸࠨၵ")) is not None:
        return results[bstack1l1_opy_ (u"ࠢࡪࡵࡶࡹࡪࡹࠢၶ")]
    logger.error(bstack1l1_opy_ (u"ࠣࡐࡲࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡗ࡫ࡳࡶ࡮ࡷࡷࠥࡽࡥࡳࡧࠣࡪࡴࡻ࡮ࡥ࠰ࠥၷ"))
    return []
  if not bstack11l1111l_opy_.bstack1lll1l111l_opy_(CONFIG, bstack1l1l11l1l_opy_) or (bstack111l1l1lll_opy_ and bstack1llll111l1_opy_):
    logger.warning(bstack1l1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶ࠲ࠧၸ"))
    return {}
  try:
    logger.debug(bstack1l1_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧၹ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack11l1111ll_opy_.bstack111111lll1_opy_)
    return results
  except Exception:
    logger.error(bstack1l1_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡹࡨࡶࡪࠦࡦࡰࡷࡱࡨ࠳ࠨၺ"))
    return {}
@measure(event_name=EVENTS.bstack11l11l1l11_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1l1l11l1l_opy_
  bstack1llll111l1_opy_ = not (bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩၻ"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬၼ"), None))
  bstack111l1l1lll_opy_ = getattr(driver, bstack1l1_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧၽ"), None) != True
  bstack11l11l11ll_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨၾ"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫၿ"), None)
  if bstack11l11l11ll_opy_:
    if not bstack1ll11l1ll1_opy_():
      logger.warning(bstack1l1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡳࡶ࡯ࡰࡥࡷࡿ࠮ࠣႀ"))
      return {}
    logger.debug(bstack1l1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺࠩႁ"))
    logger.debug(perform_scan(driver, driver_command=bstack1l1_opy_ (u"ࠬ࡫ࡸࡦࡥࡸࡸࡪ࡙ࡣࡳ࡫ࡳࡸࠬႂ")))
    results = bstack11l1l11l11_opy_(bstack1l1_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡙ࡵ࡮࡯ࡤࡶࡾࠨႃ"))
    if results is not None and results.get(bstack1l1_opy_ (u"ࠢࡴࡷࡰࡱࡦࡸࡹࠣႄ")) is not None:
        return results[bstack1l1_opy_ (u"ࠣࡵࡸࡱࡲࡧࡲࡺࠤႅ")]
    logger.error(bstack1l1_opy_ (u"ࠤࡑࡳࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡘࡥࡴࡷ࡯ࡸࡸࠦࡓࡶ࡯ࡰࡥࡷࡿࠠࡸࡣࡶࠤ࡫ࡵࡵ࡯ࡦ࠱ࠦႆ"))
    return {}
  if not bstack11l1111l_opy_.bstack1lll1l111l_opy_(CONFIG, bstack1l1l11l1l_opy_) or (bstack111l1l1lll_opy_ and bstack1llll111l1_opy_):
    logger.warning(bstack1l1_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠴ࠢႇ"))
    return {}
  try:
    logger.debug(bstack1l1_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺࠩႈ"))
    logger.debug(perform_scan(driver))
    bstack11l1ll1l1_opy_ = driver.execute_async_script(bstack11l1111ll_opy_.bstack1lll11111l_opy_)
    return bstack11l1ll1l1_opy_
  except Exception:
    logger.error(bstack1l1_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡸࡱࡲࡧࡲࡺࠢࡺࡥࡸࠦࡦࡰࡷࡱࡨ࠳ࠨႉ"))
    return {}
def bstack1ll11l1ll1_opy_():
  global CONFIG
  global bstack1l1l11l1l_opy_
  bstack1lllll1ll1_opy_ = bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ႊ"), None) and bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩႋ"), None)
  if not bstack11l1111l_opy_.bstack1lll1l111l_opy_(CONFIG, bstack1l1l11l1l_opy_) or not bstack1lllll1ll1_opy_:
        logger.warning(bstack1l1_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡲࡦࡵࡸࡰࡹࡹ࠮ࠣႌ"))
        return False
  return True
def bstack11l1l11l11_opy_(bstack11lllll1l_opy_):
    bstack11l1l1llll_opy_ = bstack1l11llll_opy_.current_test_uuid() if bstack1l11llll_opy_.current_test_uuid() else bstack1l111ll1_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack111l1ll111_opy_(bstack11l1l1llll_opy_, bstack11lllll1l_opy_))
        try:
            return future.result(timeout=bstack1l11l11lll_opy_)
        except TimeoutError:
            logger.error(bstack1l1_opy_ (u"ࠤࡗ࡭ࡲ࡫࡯ࡶࡶࠣࡥ࡫ࡺࡥࡳࠢࡾࢁࡸࠦࡷࡩ࡫࡯ࡩࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡓࡧࡶࡹࡱࡺࡳႍࠣ").format(bstack1l11l11lll_opy_))
        except Exception as ex:
            logger.debug(bstack1l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡵࡩࡹࡸࡩࡦࡸ࡬ࡲ࡬ࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡼࡿ࠱ࠤࡊࡸࡲࡰࡴࠣ࠱ࠥࢁࡽࠣႎ").format(bstack11lllll1l_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack1111l1l1ll_opy_, stage=STAGE.bstack1lllll1l1l_opy_, bstack1lll1ll111_opy_=bstack1l1l111ll1_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1l1l11l1l_opy_
  bstack1llll111l1_opy_ = not (bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨႏ"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ႐"), None))
  bstack1llll11lll_opy_ = not (bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭႑"), None) and bstack11lll111_opy_(
          threading.current_thread(), bstack1l1_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ႒"), None))
  bstack111l1l1lll_opy_ = getattr(driver, bstack1l1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ႓"), None) != True
  if not bstack11l1111l_opy_.bstack1lll1l111l_opy_(CONFIG, bstack1l1l11l1l_opy_) or (bstack111l1l1lll_opy_ and bstack1llll111l1_opy_ and bstack1llll11lll_opy_):
    logger.warning(bstack1l1_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡸࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡣࡢࡰ࠱ࠦ႔"))
    return {}
  try:
    bstack1l1ll1111_opy_ = bstack1l1_opy_ (u"ࠪࡥࡵࡶࠧ႕") in CONFIG and CONFIG.get(bstack1l1_opy_ (u"ࠫࡦࡶࡰࠨ႖"), bstack1l1_opy_ (u"ࠬ࠭႗"))
    session_id = getattr(driver, bstack1l1_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠪ႘"), None)
    if not session_id:
      logger.warning(bstack1l1_opy_ (u"ࠢࡏࡱࠣࡷࡪࡹࡳࡪࡱࡱࠤࡎࡊࠠࡧࡱࡸࡲࡩࠦࡦࡰࡴࠣࡨࡷ࡯ࡶࡦࡴࠥ႙"))
      return {bstack1l1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢႚ"): bstack1l1_opy_ (u"ࠤࡑࡳࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࠢࡩࡳࡺࡴࡤࠣႛ")}
    if bstack1l1ll1111_opy_:
      try:
        bstack11ll1lll1_opy_ = {
              bstack1l1_opy_ (u"ࠪࡸ࡭ࡐࡷࡵࡖࡲ࡯ࡪࡴࠧႜ"): os.environ.get(bstack1l1_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩႝ"), os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ႞"), bstack1l1_opy_ (u"࠭ࠧ႟"))),
              bstack1l1_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧႠ"): bstack1l11llll_opy_.current_test_uuid() if bstack1l11llll_opy_.current_test_uuid() else bstack1l111ll1_opy_.current_hook_uuid(),
              bstack1l1_opy_ (u"ࠨࡣࡸࡸ࡭ࡎࡥࡢࡦࡨࡶࠬႡ"): os.environ.get(bstack1l1_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧႢ")),
              bstack1l1_opy_ (u"ࠪࡷࡨࡧ࡮ࡕ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪႣ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack1l1_opy_ (u"ࠫࡹ࡮ࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩႤ"): os.environ.get(bstack1l1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪႥ"), bstack1l1_opy_ (u"࠭ࠧႦ")),
              bstack1l1_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪࠧႧ"): kwargs.get(bstack1l1_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠࡥࡲࡱࡲࡧ࡮ࡥࠩႨ"), None) or bstack1l1_opy_ (u"ࠩࠪႩ")
          }
        if not hasattr(thread_local, bstack1l1_opy_ (u"ࠪࡦࡦࡹࡥࡠࡣࡳࡴࡤࡧ࠱࠲ࡻࡢࡷࡨࡸࡩࡱࡶࠪႪ")):
            scripts = {bstack1l1_opy_ (u"ࠫࡸࡩࡡ࡯ࠩႫ"): bstack11l1111ll_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack11llll11l_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack11llll11l_opy_[bstack1l1_opy_ (u"ࠬࡹࡣࡢࡰࠪႬ")] = bstack11llll11l_opy_[bstack1l1_opy_ (u"࠭ࡳࡤࡣࡱࠫႭ")] % json.dumps(bstack11ll1lll1_opy_)
        bstack11l1111ll_opy_.bstack1l1l1ll11_opy_(bstack11llll11l_opy_)
        bstack11l1111ll_opy_.store()
        bstack11l11l1l1_opy_ = driver.execute_script(bstack11l1111ll_opy_.perform_scan)
      except Exception as bstack111l11lll_opy_:
        logger.info(bstack1l1_opy_ (u"ࠢࡂࡲࡳ࡭ࡺࡳࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲࠥ࡬ࡡࡪ࡮ࡨࡨ࠿ࠦࠢႮ") + str(bstack111l11lll_opy_))
        bstack11l11l1l1_opy_ = {bstack1l1_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢႯ"): str(bstack111l11lll_opy_)}
    else:
      bstack11l11l1l1_opy_ = driver.execute_async_script(bstack11l1111ll_opy_.perform_scan, {bstack1l1_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࠩႰ"): kwargs.get(bstack1l1_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢࡧࡴࡳ࡭ࡢࡰࡧࠫႱ"), None) or bstack1l1_opy_ (u"ࠫࠬႲ")})
    return bstack11l11l1l1_opy_
  except Exception as err:
    logger.error(bstack1l1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡴࡸࡲࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡣࡢࡰ࠱ࠤࢀࢃࠢႳ").format(str(err)))
    return {}