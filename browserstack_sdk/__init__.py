# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
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
from browserstack_sdk.bstack1l111ll1ll_opy_ import bstack11l1l1111_opy_
from browserstack_sdk.bstack1lll11111_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.measure import measure
def bstack11111l1l11_opy_():
  global CONFIG
  headers = {
        bstack11l111_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧਦ"): bstack11l111_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬਧ"),
      }
  proxies = bstack11l11l1l11_opy_(CONFIG, bstack1111111l1_opy_)
  try:
    response = requests.get(bstack1111111l1_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1ll11l111l_opy_ = response.json()[bstack11l111_opy_ (u"ࠪ࡬ࡺࡨࡳࠨਨ")]
      logger.debug(bstack111111lll_opy_.format(response.json()))
      return bstack1ll11l111l_opy_
    else:
      logger.debug(bstack1l111l111l_opy_.format(bstack11l111_opy_ (u"ࠦࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡊࡔࡑࡑࠤࡵࡧࡲࡴࡧࠣࡩࡷࡸ࡯ࡳࠢࠥ਩")))
  except Exception as e:
    logger.debug(bstack1l111l111l_opy_.format(e))
def bstack1lllllll11_opy_(hub_url):
  global CONFIG
  url = bstack11l111_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢਪ")+  hub_url + bstack11l111_opy_ (u"ࠨ࠯ࡤࡪࡨࡧࡰࠨਫ")
  headers = {
        bstack11l111_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭ਬ"): bstack11l111_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫਭ"),
      }
  proxies = bstack11l11l1l11_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1l111lllll_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack111llllll1_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack11l1111ll_opy_, stage=STAGE.bstack1l11lll11_opy_)
def bstack1ll1ll1111_opy_():
  try:
    global bstack1111llll11_opy_
    bstack1ll11l111l_opy_ = bstack11111l1l11_opy_()
    bstack11l1111l1_opy_ = []
    results = []
    for bstack11ll11l1l_opy_ in bstack1ll11l111l_opy_:
      bstack11l1111l1_opy_.append(bstack11lll1l1l_opy_(target=bstack1lllllll11_opy_,args=(bstack11ll11l1l_opy_,)))
    for t in bstack11l1111l1_opy_:
      t.start()
    for t in bstack11l1111l1_opy_:
      results.append(t.join())
    bstack1111lll11_opy_ = {}
    for item in results:
      hub_url = item[bstack11l111_opy_ (u"ࠩ࡫ࡹࡧࡥࡵࡳ࡮ࠪਮ")]
      latency = item[bstack11l111_opy_ (u"ࠪࡰࡦࡺࡥ࡯ࡥࡼࠫਯ")]
      bstack1111lll11_opy_[hub_url] = latency
    bstack1l1ll1llll_opy_ = min(bstack1111lll11_opy_, key= lambda x: bstack1111lll11_opy_[x])
    bstack1111llll11_opy_ = bstack1l1ll1llll_opy_
    logger.debug(bstack111llll1ll_opy_.format(bstack1l1ll1llll_opy_))
  except Exception as e:
    logger.debug(bstack11l11llll1_opy_.format(e))
from browserstack_sdk.bstack1lll1ll1l_opy_ import *
from browserstack_sdk.bstack1111l111_opy_ import *
from browserstack_sdk.bstack11l11111_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack11l111l1ll_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack1l1ll1l11_opy_, stage=STAGE.bstack1l11lll11_opy_)
def bstack1ll1ll1ll_opy_():
    global bstack1111llll11_opy_
    try:
        bstack11l1ll1l11_opy_ = bstack1l1llll11_opy_()
        bstack1ll11lllll_opy_(bstack11l1ll1l11_opy_)
        hub_url = bstack11l1ll1l11_opy_.get(bstack11l111_opy_ (u"ࠦࡺࡸ࡬ࠣਰ"), bstack11l111_opy_ (u"ࠧࠨ਱"))
        if hub_url.endswith(bstack11l111_opy_ (u"࠭࠯ࡸࡦ࠲࡬ࡺࡨࠧਲ")):
            hub_url = hub_url.rsplit(bstack11l111_opy_ (u"ࠧ࠰ࡹࡧ࠳࡭ࡻࡢࠨਲ਼"), 1)[0]
        if hub_url.startswith(bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࠩ਴")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack11l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠫਵ")):
            hub_url = hub_url[8:]
        bstack1111llll11_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1l1llll11_opy_():
    global CONFIG
    bstack1111l1lll1_opy_ = CONFIG.get(bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧਸ਼"), {}).get(bstack11l111_opy_ (u"ࠫ࡬ࡸࡩࡥࡐࡤࡱࡪ࠭਷"), bstack11l111_opy_ (u"ࠬࡔࡏࡠࡉࡕࡍࡉࡥࡎࡂࡏࡈࡣࡕࡇࡓࡔࡇࡇࠫਸ"))
    if not isinstance(bstack1111l1lll1_opy_, str):
        raise ValueError(bstack11l111_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡍࡲࡪࡦࠣࡲࡦࡳࡥࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡤࠤࡻࡧ࡬ࡪࡦࠣࡷࡹࡸࡩ࡯ࡩࠥਹ"))
    try:
        bstack11l1ll1l11_opy_ = bstack1llllll1ll_opy_(bstack1111l1lll1_opy_)
        return bstack11l1ll1l11_opy_
    except Exception as e:
        logger.error(bstack11l111_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳࠡ࠼ࠣࡿࢂࠨ਺").format(str(e)))
        return {}
def bstack1llllll1ll_opy_(bstack1111l1lll1_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack11l111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ਻")] or not CONFIG[bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽ਼ࠬ")]:
            raise ValueError(bstack11l111_opy_ (u"ࠥࡑ࡮ࡹࡳࡪࡰࡪࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠥࡵࡲࠡࡣࡦࡧࡪࡹࡳࠡ࡭ࡨࡽࠧ਽"))
        url = bstack1l111lll1_opy_ + bstack1111l1lll1_opy_
        auth = (CONFIG[bstack11l111_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ਾ")], CONFIG[bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨਿ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1l1l111l11_opy_ = json.loads(response.text)
            return bstack1l1l111l11_opy_
    except ValueError as ve:
        logger.error(bstack11l111_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳࠡ࠼ࠣࡿࢂࠨੀ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack11l111_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢੁ").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1ll11lllll_opy_(bstack1l1lll111_opy_):
    global CONFIG
    if bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬੂ") not in CONFIG or str(CONFIG[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭੃")]).lower() == bstack11l111_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ੄"):
        CONFIG[bstack11l111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪ੅")] = False
    elif bstack11l111_opy_ (u"ࠬ࡯ࡳࡕࡴ࡬ࡥࡱࡍࡲࡪࡦࠪ੆") in bstack1l1lll111_opy_:
        bstack111lll111_opy_ = CONFIG.get(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪੇ"), {})
        logger.debug(bstack11l111_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡹ࡫ࡶࡸ࡮ࡴࡧࠡ࡮ࡲࡧࡦࡲࠠࡰࡲࡷ࡭ࡴࡴࡳ࠻ࠢࠨࡷࠧੈ"), bstack111lll111_opy_)
        bstack1l11ll111l_opy_ = bstack1l1lll111_opy_.get(bstack11l111_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡓࡧࡳࡩࡦࡺࡥࡳࡵࠥ੉"), [])
        bstack111l1111ll_opy_ = bstack11l111_opy_ (u"ࠤ࠯ࠦ੊").join(bstack1l11ll111l_opy_)
        logger.debug(bstack11l111_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡆࡹࡸࡺ࡯࡮ࠢࡵࡩࡵ࡫ࡡࡵࡧࡵࠤࡸࡺࡲࡪࡰࡪ࠾ࠥࠫࡳࠣੋ"), bstack111l1111ll_opy_)
        bstack11ll1lll1l_opy_ = {
            bstack11l111_opy_ (u"ࠦࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨੌ"): bstack11l111_opy_ (u"ࠧࡧࡴࡴ࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵ੍ࠦ"),
            bstack11l111_opy_ (u"ࠨࡦࡰࡴࡦࡩࡑࡵࡣࡢ࡮ࠥ੎"): bstack11l111_opy_ (u"ࠢࡵࡴࡸࡩࠧ੏"),
            bstack11l111_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭࠮ࡴࡨࡴࡪࡧࡴࡦࡴࠥ੐"): bstack111l1111ll_opy_
        }
        bstack111lll111_opy_.update(bstack11ll1lll1l_opy_)
        logger.debug(bstack11l111_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡗࡳࡨࡦࡺࡥࡥࠢ࡯ࡳࡨࡧ࡬ࠡࡱࡳࡸ࡮ࡵ࡮ࡴ࠼ࠣࠩࡸࠨੑ"), bstack111lll111_opy_)
        CONFIG[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ੒")] = bstack111lll111_opy_
        logger.debug(bstack11l111_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡊ࡮ࡴࡡ࡭ࠢࡆࡓࡓࡌࡉࡈ࠼ࠣࠩࡸࠨ੓"), CONFIG)
def bstack11ll1ll11l_opy_():
    bstack11l1ll1l11_opy_ = bstack1l1llll11_opy_()
    if not bstack11l1ll1l11_opy_[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡗࡵࡰࠬ੔")]:
      raise ValueError(bstack11l111_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡘࡶࡱࠦࡩࡴࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡷࡵ࡭ࠡࡩࡵ࡭ࡩࠦࡤࡦࡶࡤ࡭ࡱࡹ࠮ࠣ੕"))
    return bstack11l1ll1l11_opy_[bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠧ੖")] + bstack11l111_opy_ (u"ࠨࡁࡦࡥࡵࡹ࠽ࠨ੗")
@measure(event_name=EVENTS.bstack11llll11ll_opy_, stage=STAGE.bstack1l11lll11_opy_)
def bstack1111l111ll_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack11l111_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ੘")], CONFIG[bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ਖ਼")])
        url = bstack111ll111l_opy_
        logger.debug(bstack11l111_opy_ (u"ࠦࡆࡺࡴࡦ࡯ࡳࡸ࡮ࡴࡧࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡦࡺ࡯࡬ࡥࡵࠣࡪࡷࡵ࡭ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡕࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠤࡆࡖࡉࠣਗ਼"))
        try:
            response = requests.get(url, auth=auth, headers={bstack11l111_opy_ (u"ࠧࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠦਜ਼"): bstack11l111_opy_ (u"ࠨࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠤੜ")})
            if response.status_code == 200:
                bstack111lll1l11_opy_ = json.loads(response.text)
                bstack1l1llllll_opy_ = bstack111lll1l11_opy_.get(bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡹࠧ੝"), [])
                if bstack1l1llllll_opy_:
                    bstack1l11l1111_opy_ = bstack1l1llllll_opy_[0]
                    build_hashed_id = bstack1l11l1111_opy_.get(bstack11l111_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫਫ਼"))
                    bstack1l1111ll11_opy_ = bstack1l1l1ll11l_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1l1111ll11_opy_])
                    logger.info(bstack1111l11l11_opy_.format(bstack1l1111ll11_opy_))
                    bstack1l1lll11ll_opy_ = CONFIG[bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ੟")]
                    if bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ੠") in CONFIG:
                      bstack1l1lll11ll_opy_ += bstack11l111_opy_ (u"ࠫࠥ࠭੡") + CONFIG[bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ੢")]
                    if bstack1l1lll11ll_opy_ != bstack1l11l1111_opy_.get(bstack11l111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ੣")):
                      logger.debug(bstack1lll1ll1ll_opy_.format(bstack1l11l1111_opy_.get(bstack11l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ੤")), bstack1l1lll11ll_opy_))
                    return result
                else:
                    logger.debug(bstack11l111_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡏࡱࠣࡦࡺ࡯࡬ࡥࡵࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࡺࡨࡦࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠲ࠧ੥"))
            else:
                logger.debug(bstack11l111_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡦࡺ࡯࡬ࡥࡵ࠱ࠦ੦"))
        except Exception as e:
            logger.error(bstack11l111_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࡷࠥࡀࠠࡼࡿࠥ੧").format(str(e)))
    else:
        logger.debug(bstack11l111_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡇࡔࡔࡆࡊࡉࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡷࡪࡺ࠮ࠡࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡦࡺ࡯࡬ࡥࡵ࠱ࠦ੨"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1l11ll1l11_opy_ import bstack1l11ll1l11_opy_, Events, bstack11ll1l1l1_opy_, bstack1l1llll1l1_opy_
from bstack_utils.measure import bstack1111lll1l_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack11l11l11l1_opy_ import bstack11lllll1ll_opy_
from bstack_utils.messages import *
from bstack_utils import bstack11l111l1ll_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack11lll11l1l_opy_, bstack111l1llll1_opy_, bstack111111ll11_opy_, bstack1l1lll11_opy_, \
  bstack11l11l1ll_opy_, \
  Notset, bstack11ll1111ll_opy_, \
  bstack11l1lll1l1_opy_, bstack1ll11111l1_opy_, bstack1lll111ll1_opy_, bstack1l1111111l_opy_, bstack1ll11111ll_opy_, bstack11l1ll1111_opy_, \
  bstack1111l1l1ll_opy_, \
  bstack111l1l111_opy_, bstack1l111l11l1_opy_, bstack111ll111ll_opy_, bstack11l11ll1ll_opy_, \
  bstack111l11l11l_opy_, bstack11l1llll11_opy_, bstack1l1lll1ll1_opy_, bstack1111l11ll1_opy_
from bstack_utils.bstack1l1l1ll1ll_opy_ import bstack11l1l11l1_opy_
from bstack_utils.bstack111ll11l1l_opy_ import bstack1ll1l11ll1_opy_, bstack111lll1l1l_opy_
from bstack_utils.bstack111ll1ll1l_opy_ import bstack111l11l111_opy_
from bstack_utils.bstack1lll1l1l11_opy_ import bstack11ll11lll1_opy_, bstack1lll111lll_opy_
from bstack_utils.bstack111l1ll1l_opy_ import bstack111l1ll1l_opy_
from bstack_utils.bstack1l111ll11l_opy_ import bstack11l11ll11l_opy_
from bstack_utils.proxy import bstack11ll11lll_opy_, bstack11l11l1l11_opy_, bstack11l1llllll_opy_, bstack1lll1l1l1l_opy_
from bstack_utils.bstack1l11lll1l_opy_ import bstack1ll11l111_opy_
import bstack_utils.bstack1l11ll1l1_opy_ as bstack11ll111ll_opy_
import bstack_utils.bstack1l1l1l11l1_opy_ as bstack11l11l11ll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack1ll1l11l1l_opy_ import bstack1ll1ll1l1_opy_
from bstack_utils.bstack1111ll1l_opy_ import bstack1lll1l1ll_opy_
from bstack_utils.bstack111llll111_opy_ import bstack1l11111ll1_opy_
if os.getenv(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡊࡒࡓࡐ࡙ࠧ੩")):
  cli.bstack111lll1lll_opy_()
else:
  os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡋࡓࡔࡑࡓࠨ੪")] = bstack11l111_opy_ (u"ࠧࡵࡴࡸࡩࠬ੫")
bstack11111l1ll_opy_ = bstack11l111_opy_ (u"ࠨࠢࠣ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࠡࠢ࡬ࡪ࠭ࡶࡡࡨࡧࠣࡁࡂࡃࠠࡷࡱ࡬ࡨࠥ࠶ࠩࠡࡽ࡟ࡲࠥࠦࠠࡵࡴࡼࡿࡡࡴࠠࡤࡱࡱࡷࡹࠦࡦࡴࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࡢࠧࡧࡵ࡟ࠫ࠮ࡁ࡜࡯ࠢࠣࠤࠥࠦࡦࡴ࠰ࡤࡴࡵ࡫࡮ࡥࡈ࡬ࡰࡪ࡙ࡹ࡯ࡥࠫࡦࡸࡺࡡࡤ࡭ࡢࡴࡦࡺࡨ࠭ࠢࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡴࡤ࡯࡮ࡥࡧࡻ࠭ࠥ࠱ࠠࠣ࠼ࠥࠤ࠰ࠦࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡋࡕࡒࡒ࠳ࡶࡡࡳࡵࡨࠬ࠭ࡧࡷࡢ࡫ࡷࠤࡳ࡫ࡷࡑࡣࡪࡩ࠷࠴ࡥࡷࡣ࡯ࡹࡦࡺࡥࠩࠤࠫ࠭ࠥࡃ࠾ࠡࡽࢀࠦ࠱ࠦ࡜ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡩࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡉ࡫ࡴࡢ࡫࡯ࡷࠧࢃ࡜ࠨࠫࠬ࠭ࡠࠨࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠤࡠ࠭ࠥ࠱ࠠࠣ࠮࡟ࡠࡳࠨࠩ࡝ࡰࠣࠤࠥࠦࡽࡤࡣࡷࡧ࡭࠮ࡥࡹࠫࡾࡠࡳࠦࠠࠡࠢࢀࡠࡳࠦࠠࡾ࡞ࡱࠤࠥ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯ࠨ੬")
bstack11ll1l1ll_opy_ = bstack11l111_opy_ (u"ࠩ࡟ࡲ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬ࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴࡟࡟ࡲࡨࡵ࡮ࡴࡶࠣࡦࡸࡺࡡࡤ࡭ࡢࡧࡦࡶࡳࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠵ࡢࡢ࡮ࡤࡱࡱࡷࡹࠦࡰࡠ࡫ࡱࡨࡪࡾࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠵ࡡࡡࡴࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴ࡳ࡭࡫ࡦࡩ࠭࠶ࠬࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶࠭ࡡࡴࡣࡰࡰࡶࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭ࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ࠮ࡁ࡜࡯࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰ࠴ࡣࡩࡴࡲࡱ࡮ࡻ࡭࠯࡮ࡤࡹࡳࡩࡨࠡ࠿ࠣࡥࡸࡿ࡮ࡤࠢࠫࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵࠬࠤࡂࡄࠠࡼ࡞ࡱࡰࡪࡺࠠࡤࡣࡳࡷࡀࡢ࡮ࡵࡴࡼࠤࢀࡢ࡮ࡤࡣࡳࡷࠥࡃࠠࡋࡕࡒࡒ࠳ࡶࡡࡳࡵࡨࠬࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠫ࡟ࡲࠥࠦࡽࠡࡥࡤࡸࡨ࡮ࠨࡦࡺࠬࠤࢀࡢ࡮ࠡࠢࠣࠤࢂࡢ࡮ࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡤࡻࡦ࡯ࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰ࠴ࡣࡩࡴࡲࡱ࡮ࡻ࡭࠯ࡥࡲࡲࡳ࡫ࡣࡵࠪࡾࡠࡳࠦࠠࠡࠢࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹࡀࠠࡡࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠧࡿࡪࡴࡣࡰࡦࡨ࡙ࡗࡏࡃࡰ࡯ࡳࡳࡳ࡫࡮ࡵࠪࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡧࡦࡶࡳࠪࠫࢀࡤ࠱ࡢ࡮ࠡࠢࠣࠤ࠳࠴࠮࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹ࡜࡯ࠢࠣࢁ࠮ࡢ࡮ࡾ࡞ࡱ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࠨ੭")
from ._version import __version__
bstack1llll1lll1_opy_ = None
CONFIG = {}
bstack1ll11l1l11_opy_ = {}
bstack1111l111l1_opy_ = {}
bstack11lll1lll1_opy_ = None
bstack1ll111l1l_opy_ = None
bstack11lll111ll_opy_ = None
bstack1l1l11llll_opy_ = -1
bstack111l11llll_opy_ = 0
bstack1ll1l111ll_opy_ = bstack1111l1lll_opy_
bstack1lll1ll1l1_opy_ = 1
bstack1l11ll11l1_opy_ = False
bstack1ll1l11lll_opy_ = False
bstack1111l1l1l1_opy_ = bstack11l111_opy_ (u"ࠪࠫ੮")
bstack111l1lll11_opy_ = bstack11l111_opy_ (u"ࠫࠬ੯")
bstack11l11111l_opy_ = False
bstack11l1111l11_opy_ = True
bstack1l1l1l1lll_opy_ = bstack11l111_opy_ (u"ࠬ࠭ੰ")
bstack11l11l111_opy_ = []
bstack1l111l1l11_opy_ = threading.Lock()
bstack11ll1l11l_opy_ = threading.Lock()
bstack1111llll11_opy_ = bstack11l111_opy_ (u"࠭ࠧੱ")
bstack1lllllllll_opy_ = False
bstack1lll1l1ll1_opy_ = None
bstack1111l111l_opy_ = None
bstack11llll11l1_opy_ = None
bstack11lll11l1_opy_ = -1
bstack111111ll1l_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠧࡿࠩੲ")), bstack11l111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨੳ"), bstack11l111_opy_ (u"ࠩ࠱ࡶࡴࡨ࡯ࡵ࠯ࡵࡩࡵࡵࡲࡵ࠯࡫ࡩࡱࡶࡥࡳ࠰࡭ࡷࡴࡴࠧੴ"))
bstack11l1l11111_opy_ = 0
bstack1ll111l11l_opy_ = 0
bstack1l11l1l11_opy_ = []
bstack11lllllll_opy_ = []
bstack11111lllll_opy_ = []
bstack111ll11l1_opy_ = []
bstack1l11l1lll_opy_ = bstack11l111_opy_ (u"ࠪࠫੵ")
bstack1l11111l11_opy_ = bstack11l111_opy_ (u"ࠫࠬ੶")
bstack1ll111lll1_opy_ = False
bstack1ll1111l1_opy_ = False
bstack11l11l1lll_opy_ = {}
bstack1ll1l1lll1_opy_ = None
bstack11l1lll11_opy_ = None
bstack1ll1ll111l_opy_ = None
bstack11111ll1l_opy_ = None
bstack1ll1llll11_opy_ = None
bstack1l1l111l1_opy_ = None
bstack1l111llll1_opy_ = None
bstack1l11ll1ll_opy_ = None
bstack11ll1lllll_opy_ = None
bstack1l1l11lll1_opy_ = None
bstack1111111ll_opy_ = None
bstack111ll1ll1_opy_ = None
bstack1l1l11l1l1_opy_ = None
bstack1l111l1l1_opy_ = None
bstack11ll11llll_opy_ = None
bstack11l1111111_opy_ = None
bstack1ll1ll11l1_opy_ = None
bstack1l11l1ll1_opy_ = None
bstack11lll111l1_opy_ = None
bstack1ll111l111_opy_ = None
bstack1ll1lll111_opy_ = None
bstack11l1l111l_opy_ = None
bstack1llll1l111_opy_ = None
thread_local = threading.local()
bstack111l1l11l1_opy_ = False
bstack1111ll1l11_opy_ = bstack11l111_opy_ (u"ࠧࠨ੷")
logger = bstack11l111l1ll_opy_.get_logger(__name__, bstack1ll1l111ll_opy_)
bstack11111l11_opy_ = Config.bstack111l11l1_opy_()
percy = bstack1l11ll1ll1_opy_()
bstack11l1llll1_opy_ = bstack11lllll1ll_opy_()
bstack1llll11ll1_opy_ = bstack11l11111_opy_()
def bstack11l1lll1l_opy_():
  global CONFIG
  global bstack1ll111lll1_opy_
  global bstack11111l11_opy_
  testContextOptions = bstack1l11llll1l_opy_(CONFIG)
  if bstack11l11l1ll_opy_(CONFIG):
    if (bstack11l111_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ੸") in testContextOptions and str(testContextOptions[bstack11l111_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ੹")]).lower() == bstack11l111_opy_ (u"ࠨࡶࡵࡹࡪ࠭੺")):
      bstack1ll111lll1_opy_ = True
    bstack11111l11_opy_.bstack1lll11l1ll_opy_(testContextOptions.get(bstack11l111_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭੻"), False))
  else:
    bstack1ll111lll1_opy_ = True
    bstack11111l11_opy_.bstack1lll11l1ll_opy_(True)
def bstack1ll11lll1_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack1ll1l11ll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack111l111111_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11l111_opy_ (u"ࠥ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡧࡴࡴࡦࡪࡩࡩ࡭ࡱ࡫ࠢ੼") == args[i].lower() or bstack11l111_opy_ (u"ࠦ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡯ࡨ࡬࡫ࠧ੽") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1l1l1l1lll_opy_
      bstack1l1l1l1lll_opy_ += bstack11l111_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡉ࡯࡯ࡨ࡬࡫ࡋ࡯࡬ࡦࠢࠪ੾") + shlex.quote(path)
      return path
  return None
bstack1llllllll1_opy_ = re.compile(bstack11l111_opy_ (u"ࡸࠢ࠯ࠬࡂࡠࠩࢁࠨ࠯ࠬࡂ࠭ࢂ࠴ࠪࡀࠤ੿"))
def bstack1111ll1ll_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1llllllll1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11l111_opy_ (u"ࠢࠥࡽࠥ઀") + group + bstack11l111_opy_ (u"ࠣࡿࠥઁ"), os.environ.get(group))
  return value
def bstack1lll11l111_opy_():
  global bstack1llll1l111_opy_
  if bstack1llll1l111_opy_ is None:
        bstack1llll1l111_opy_ = bstack111l111111_opy_()
  bstack11l11l1111_opy_ = bstack1llll1l111_opy_
  if bstack11l11l1111_opy_ and os.path.exists(os.path.abspath(bstack11l11l1111_opy_)):
    fileName = bstack11l11l1111_opy_
  if bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࡠࡈࡌࡐࡊ࠭ં") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧઃ")])) and not bstack11l111_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࠭઄") in locals():
    fileName = os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆࠩઅ")]
  if bstack11l111_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨઆ") in locals():
    bstack11ll1ll_opy_ = os.path.abspath(fileName)
  else:
    bstack11ll1ll_opy_ = bstack11l111_opy_ (u"ࠧࠨઇ")
  bstack11ll11l1ll_opy_ = os.getcwd()
  bstack1l1111ll1_opy_ = bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫઈ")
  bstack1llll111l1_opy_ = bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡤࡱࡱ࠭ઉ")
  while (not os.path.exists(bstack11ll1ll_opy_)) and bstack11ll11l1ll_opy_ != bstack11l111_opy_ (u"ࠥࠦઊ"):
    bstack11ll1ll_opy_ = os.path.join(bstack11ll11l1ll_opy_, bstack1l1111ll1_opy_)
    if not os.path.exists(bstack11ll1ll_opy_):
      bstack11ll1ll_opy_ = os.path.join(bstack11ll11l1ll_opy_, bstack1llll111l1_opy_)
    if bstack11ll11l1ll_opy_ != os.path.dirname(bstack11ll11l1ll_opy_):
      bstack11ll11l1ll_opy_ = os.path.dirname(bstack11ll11l1ll_opy_)
    else:
      bstack11ll11l1ll_opy_ = bstack11l111_opy_ (u"ࠦࠧઋ")
  bstack1llll1l111_opy_ = bstack11ll1ll_opy_ if os.path.exists(bstack11ll1ll_opy_) else None
  return bstack1llll1l111_opy_
def bstack1ll111l1ll_opy_(config):
    if bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠬઌ") in config:
      config[bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪઍ")] = config[bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧ઎")]
    if bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࡐࡲࡷ࡭ࡴࡴࡳࠨએ") in config:
      config[bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ઐ")] = config[bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࡒࡴࡹ࡯࡯࡯ࡵࠪઑ")]
def bstack1l1l1l11ll_opy_():
  bstack11ll1ll_opy_ = bstack1lll11l111_opy_()
  if not os.path.exists(bstack11ll1ll_opy_):
    bstack1l1111l11_opy_(
      bstack111l1l11ll_opy_.format(os.getcwd()))
  try:
    with open(bstack11ll1ll_opy_, bstack11l111_opy_ (u"ࠫࡷ࠭઒")) as stream:
      yaml.add_implicit_resolver(bstack11l111_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨઓ"), bstack1llllllll1_opy_)
      yaml.add_constructor(bstack11l111_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢઔ"), bstack1111ll1ll_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1ll111l1ll_opy_(config)
      return config
  except:
    with open(bstack11ll1ll_opy_, bstack11l111_opy_ (u"ࠧࡳࠩક")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1ll111l1ll_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1l1111l11_opy_(bstack1l11lll111_opy_.format(str(exc)))
def bstack1l1111l11l_opy_(config):
  bstack1ll11l1lll_opy_ = bstack11lllllll1_opy_(config)
  for option in list(bstack1ll11l1lll_opy_):
    if option.lower() in bstack11l1l1ll1_opy_ and option != bstack11l1l1ll1_opy_[option.lower()]:
      bstack1ll11l1lll_opy_[bstack11l1l1ll1_opy_[option.lower()]] = bstack1ll11l1lll_opy_[option]
      del bstack1ll11l1lll_opy_[option]
  return config
def bstack1lll1l11l1_opy_():
  global bstack1111l111l1_opy_
  for key, bstack111lll11l_opy_ in bstack11111lll1l_opy_.items():
    if isinstance(bstack111lll11l_opy_, list):
      for var in bstack111lll11l_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1111l111l1_opy_[key] = os.environ[var]
          break
    elif bstack111lll11l_opy_ in os.environ and os.environ[bstack111lll11l_opy_] and str(os.environ[bstack111lll11l_opy_]).strip():
      bstack1111l111l1_opy_[key] = os.environ[bstack111lll11l_opy_]
  if bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪખ") in os.environ:
    bstack1111l111l1_opy_[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ગ")] = {}
    bstack1111l111l1_opy_[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઘ")][bstack11l111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ઙ")] = os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧચ")]
def bstack11lll1111l_opy_():
  global bstack1ll11l1l11_opy_
  global bstack1l1l1l1lll_opy_
  bstack11ll11l1l1_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack11l111_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩછ").lower() == val.lower():
      bstack1ll11l1l11_opy_[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫજ")] = {}
      bstack1ll11l1l11_opy_[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬઝ")][bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫઞ")] = sys.argv[idx + 1]
      bstack11ll11l1l1_opy_.extend([idx, idx + 1])
      break
  for key, bstack1ll1lll1ll_opy_ in bstack1l11l1l1ll_opy_.items():
    if isinstance(bstack1ll1lll1ll_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack1ll1lll1ll_opy_:
          if bstack11l111_opy_ (u"ࠪ࠱࠲࠭ટ") + var.lower() == val.lower() and key not in bstack1ll11l1l11_opy_:
            bstack1ll11l1l11_opy_[key] = sys.argv[idx + 1]
            bstack1l1l1l1lll_opy_ += bstack11l111_opy_ (u"ࠫࠥ࠳࠭ࠨઠ") + var + bstack11l111_opy_ (u"ࠬࠦࠧડ") + shlex.quote(sys.argv[idx + 1])
            bstack11ll11l1l1_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack11l111_opy_ (u"࠭࠭࠮ࠩઢ") + bstack1ll1lll1ll_opy_.lower() == val.lower() and key not in bstack1ll11l1l11_opy_:
          bstack1ll11l1l11_opy_[key] = sys.argv[idx + 1]
          bstack1l1l1l1lll_opy_ += bstack11l111_opy_ (u"ࠧࠡ࠯࠰ࠫણ") + bstack1ll1lll1ll_opy_ + bstack11l111_opy_ (u"ࠨࠢࠪત") + shlex.quote(sys.argv[idx + 1])
          bstack11ll11l1l1_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack11ll11l1l1_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack111lllllll_opy_(config):
  bstack1l1l11l1l_opy_ = config.keys()
  for bstack1l111lll11_opy_, bstack1l1ll1l1ll_opy_ in bstack1l111l11ll_opy_.items():
    if bstack1l1ll1l1ll_opy_ in bstack1l1l11l1l_opy_:
      config[bstack1l111lll11_opy_] = config[bstack1l1ll1l1ll_opy_]
      del config[bstack1l1ll1l1ll_opy_]
  for bstack1l111lll11_opy_, bstack1l1ll1l1ll_opy_ in bstack1l1l1lllll_opy_.items():
    if isinstance(bstack1l1ll1l1ll_opy_, list):
      for bstack1llllll1l1_opy_ in bstack1l1ll1l1ll_opy_:
        if bstack1llllll1l1_opy_ in bstack1l1l11l1l_opy_:
          config[bstack1l111lll11_opy_] = config[bstack1llllll1l1_opy_]
          del config[bstack1llllll1l1_opy_]
          break
    elif bstack1l1ll1l1ll_opy_ in bstack1l1l11l1l_opy_:
      config[bstack1l111lll11_opy_] = config[bstack1l1ll1l1ll_opy_]
      del config[bstack1l1ll1l1ll_opy_]
  for bstack1llllll1l1_opy_ in list(config):
    for bstack1l1l11ll11_opy_ in bstack1111l1ll1_opy_:
      if bstack1llllll1l1_opy_.lower() == bstack1l1l11ll11_opy_.lower() and bstack1llllll1l1_opy_ != bstack1l1l11ll11_opy_:
        config[bstack1l1l11ll11_opy_] = config[bstack1llllll1l1_opy_]
        del config[bstack1llllll1l1_opy_]
  bstack111l11111l_opy_ = [{}]
  if not config.get(bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬથ")):
    config[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭દ")] = [{}]
  bstack111l11111l_opy_ = config[bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧધ")]
  for platform in bstack111l11111l_opy_:
    for bstack1llllll1l1_opy_ in list(platform):
      for bstack1l1l11ll11_opy_ in bstack1111l1ll1_opy_:
        if bstack1llllll1l1_opy_.lower() == bstack1l1l11ll11_opy_.lower() and bstack1llllll1l1_opy_ != bstack1l1l11ll11_opy_:
          platform[bstack1l1l11ll11_opy_] = platform[bstack1llllll1l1_opy_]
          del platform[bstack1llllll1l1_opy_]
  for bstack1l111lll11_opy_, bstack1l1ll1l1ll_opy_ in bstack1l1l1lllll_opy_.items():
    for platform in bstack111l11111l_opy_:
      if isinstance(bstack1l1ll1l1ll_opy_, list):
        for bstack1llllll1l1_opy_ in bstack1l1ll1l1ll_opy_:
          if bstack1llllll1l1_opy_ in platform:
            platform[bstack1l111lll11_opy_] = platform[bstack1llllll1l1_opy_]
            del platform[bstack1llllll1l1_opy_]
            break
      elif bstack1l1ll1l1ll_opy_ in platform:
        platform[bstack1l111lll11_opy_] = platform[bstack1l1ll1l1ll_opy_]
        del platform[bstack1l1ll1l1ll_opy_]
  for bstack111l11l1l1_opy_ in bstack11111llll_opy_:
    if bstack111l11l1l1_opy_ in config:
      if not bstack11111llll_opy_[bstack111l11l1l1_opy_] in config:
        config[bstack11111llll_opy_[bstack111l11l1l1_opy_]] = {}
      config[bstack11111llll_opy_[bstack111l11l1l1_opy_]].update(config[bstack111l11l1l1_opy_])
      del config[bstack111l11l1l1_opy_]
  for platform in bstack111l11111l_opy_:
    for bstack111l11l1l1_opy_ in bstack11111llll_opy_:
      if bstack111l11l1l1_opy_ in list(platform):
        if not bstack11111llll_opy_[bstack111l11l1l1_opy_] in platform:
          platform[bstack11111llll_opy_[bstack111l11l1l1_opy_]] = {}
        platform[bstack11111llll_opy_[bstack111l11l1l1_opy_]].update(platform[bstack111l11l1l1_opy_])
        del platform[bstack111l11l1l1_opy_]
  config = bstack1l1111l11l_opy_(config)
  return config
def bstack1l1ll11l1l_opy_(config):
  global bstack111l1lll11_opy_
  bstack11l1ll1ll1_opy_ = False
  if bstack11l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩન") in config and str(config[bstack11l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ઩")]).lower() != bstack11l111_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭પ"):
    if bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬફ") not in config or str(config[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭બ")]).lower() == bstack11l111_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩભ"):
      config[bstack11l111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪમ")] = False
    else:
      bstack11l1ll1l11_opy_ = bstack1l1llll11_opy_()
      if bstack11l111_opy_ (u"ࠬ࡯ࡳࡕࡴ࡬ࡥࡱࡍࡲࡪࡦࠪય") in bstack11l1ll1l11_opy_:
        if not bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪર") in config:
          config[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ઱")] = {}
        config[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬલ")][bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫળ")] = bstack11l111_opy_ (u"ࠪࡥࡹࡹ࠭ࡳࡧࡳࡩࡦࡺࡥࡳࠩ઴")
        bstack11l1ll1ll1_opy_ = True
        bstack111l1lll11_opy_ = config[bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨવ")].get(bstack11l111_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧશ"))
  if bstack11l11l1ll_opy_(config) and bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪષ") in config and str(config[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫસ")]).lower() != bstack11l111_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧહ") and not bstack11l1ll1ll1_opy_:
    if not bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭઺") in config:
      config[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ઻")] = {}
    if not config[bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ઼")].get(bstack11l111_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩઽ")) and not bstack11l111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨા") in config[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫિ")]:
      bstack11lllll1_opy_ = datetime.datetime.now()
      bstack1l111llll_opy_ = bstack11lllll1_opy_.strftime(bstack11l111_opy_ (u"ࠨࠧࡧࡣࠪࡨ࡟ࠦࡊࠨࡑࠬી"))
      hostname = socket.gethostname()
      bstack11111111l_opy_ = bstack11l111_opy_ (u"ࠩࠪુ").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11l111_opy_ (u"ࠪࡿࢂࡥࡻࡾࡡࡾࢁࠬૂ").format(bstack1l111llll_opy_, hostname, bstack11111111l_opy_)
      config[bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨૃ")][bstack11l111_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૄ")] = identifier
    bstack111l1lll11_opy_ = config[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪૅ")].get(bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૆"))
  return config
def bstack1ll1l111l1_opy_():
  bstack111ll1l1l1_opy_ =  bstack1l1111111l_opy_()[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠧે")]
  return bstack111ll1l1l1_opy_ if bstack111ll1l1l1_opy_ else -1
def bstack11l11111l1_opy_(bstack111ll1l1l1_opy_):
  global CONFIG
  if not bstack11l111_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫૈ") in CONFIG[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૉ")]:
    return
  CONFIG[bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૊")] = CONFIG[bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧો")].replace(
    bstack11l111_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨૌ"),
    str(bstack111ll1l1l1_opy_)
  )
def bstack11111l1l1l_opy_():
  global CONFIG
  if not bstack11l111_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ્࠭") in CONFIG[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૎")]:
    return
  bstack11lllll1_opy_ = datetime.datetime.now()
  bstack1l111llll_opy_ = bstack11lllll1_opy_.strftime(bstack11l111_opy_ (u"ࠩࠨࡨ࠲ࠫࡢ࠮ࠧࡋ࠾ࠪࡓࠧ૏"))
  CONFIG[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૐ")] = CONFIG[bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૑")].replace(
    bstack11l111_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫ૒"),
    bstack1l111llll_opy_
  )
def bstack11ll1l111_opy_():
  global CONFIG
  if bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૓") in CONFIG and not bool(CONFIG[bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૔")]):
    del CONFIG[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૕")]
    return
  if not bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૖") in CONFIG:
    CONFIG[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૗")] = bstack11l111_opy_ (u"ࠫࠨࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧ૘")
  if bstack11l111_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫ૙") in CONFIG[bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૚")]:
    bstack11111l1l1l_opy_()
    os.environ[bstack11l111_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ૛")] = CONFIG[bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૜")]
  if not bstack11l111_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫ૝") in CONFIG[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૞")]:
    return
  bstack111ll1l1l1_opy_ = bstack11l111_opy_ (u"ࠫࠬ૟")
  bstack1l11ll1l1l_opy_ = bstack1ll1l111l1_opy_()
  if bstack1l11ll1l1l_opy_ != -1:
    bstack111ll1l1l1_opy_ = bstack11l111_opy_ (u"ࠬࡉࡉࠡࠩૠ") + str(bstack1l11ll1l1l_opy_)
  if bstack111ll1l1l1_opy_ == bstack11l111_opy_ (u"࠭ࠧૡ"):
    bstack111l1ll111_opy_ = bstack111111l11l_opy_(CONFIG[bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪૢ")])
    if bstack111l1ll111_opy_ != -1:
      bstack111ll1l1l1_opy_ = str(bstack111l1ll111_opy_)
  if bstack111ll1l1l1_opy_:
    bstack11l11111l1_opy_(bstack111ll1l1l1_opy_)
    os.environ[bstack11l111_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬૣ")] = CONFIG[bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૤")]
def bstack1l1ll1l111_opy_(bstack1l1ll111l_opy_, bstack11l1lllll_opy_, path):
  json_data = {
    bstack11l111_opy_ (u"ࠪ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૥"): bstack11l1lllll_opy_
  }
  if os.path.exists(path):
    bstack1lllll1l1l_opy_ = json.load(open(path, bstack11l111_opy_ (u"ࠫࡷࡨࠧ૦")))
  else:
    bstack1lllll1l1l_opy_ = {}
  bstack1lllll1l1l_opy_[bstack1l1ll111l_opy_] = json_data
  with open(path, bstack11l111_opy_ (u"ࠧࡽࠫࠣ૧")) as outfile:
    json.dump(bstack1lllll1l1l_opy_, outfile)
def bstack111111l11l_opy_(bstack1l1ll111l_opy_):
  bstack1l1ll111l_opy_ = str(bstack1l1ll111l_opy_)
  bstack11l1l1ll11_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"࠭ࡾࠨ૨")), bstack11l111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ૩"))
  try:
    if not os.path.exists(bstack11l1l1ll11_opy_):
      os.makedirs(bstack11l1l1ll11_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠨࢀࠪ૪")), bstack11l111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ૫"), bstack11l111_opy_ (u"ࠪ࠲ࡧࡻࡩ࡭ࡦ࠰ࡲࡦࡳࡥ࠮ࡥࡤࡧ࡭࡫࠮࡫ࡵࡲࡲࠬ૬"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11l111_opy_ (u"ࠫࡼ࠭૭")):
        pass
      with open(file_path, bstack11l111_opy_ (u"ࠧࡽࠫࠣ૮")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11l111_opy_ (u"࠭ࡲࠨ૯")) as bstack1lllll1111_opy_:
      bstack1l1l1llll1_opy_ = json.load(bstack1lllll1111_opy_)
    if bstack1l1ll111l_opy_ in bstack1l1l1llll1_opy_:
      bstack1l1l1lll1l_opy_ = bstack1l1l1llll1_opy_[bstack1l1ll111l_opy_][bstack11l111_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૰")]
      bstack11ll1ll1l1_opy_ = int(bstack1l1l1lll1l_opy_) + 1
      bstack1l1ll1l111_opy_(bstack1l1ll111l_opy_, bstack11ll1ll1l1_opy_, file_path)
      return bstack11ll1ll1l1_opy_
    else:
      bstack1l1ll1l111_opy_(bstack1l1ll111l_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack11llll1l11_opy_.format(str(e)))
    return -1
def bstack11l1l1l11l_opy_(config):
  if not config[bstack11l111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ૱")] or not config[bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ૲")]:
    return True
  else:
    return False
def bstack11l1ll1ll_opy_(config, index=0):
  global bstack11l11111l_opy_
  bstack11l1111lll_opy_ = {}
  caps = bstack11lll11111_opy_ + bstack1l1l11111l_opy_
  if config.get(bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ૳"), False):
    bstack11l1111lll_opy_[bstack11l111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨ૴")] = True
    bstack11l1111lll_opy_[bstack11l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ૵")] = config.get(bstack11l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ૶"), {})
  if bstack11l11111l_opy_:
    caps += bstack1l111ll1l1_opy_
  for key in config:
    if key in caps + [bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૷")]:
      continue
    bstack11l1111lll_opy_[key] = config[key]
  if bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૸") in config:
    for bstack1lll1ll11l_opy_ in config[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬૹ")][index]:
      if bstack1lll1ll11l_opy_ in caps:
        continue
      bstack11l1111lll_opy_[bstack1lll1ll11l_opy_] = config[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ૺ")][index][bstack1lll1ll11l_opy_]
  bstack11l1111lll_opy_[bstack11l111_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ૻ")] = socket.gethostname()
  if bstack11l111_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ૼ") in bstack11l1111lll_opy_:
    del (bstack11l1111lll_opy_[bstack11l111_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧ૽")])
  return bstack11l1111lll_opy_
def bstack1lll1lll1l_opy_(config):
  global bstack11l11111l_opy_
  bstack1lllll111l_opy_ = {}
  caps = bstack1l1l11111l_opy_
  if bstack11l11111l_opy_:
    caps += bstack1l111ll1l1_opy_
  for key in caps:
    if key in config:
      bstack1lllll111l_opy_[key] = config[key]
  return bstack1lllll111l_opy_
def bstack1l11l1ll11_opy_(bstack11l1111lll_opy_, bstack1lllll111l_opy_):
  bstack1l11llll1_opy_ = {}
  for key in bstack11l1111lll_opy_.keys():
    if key in bstack1l111l11ll_opy_:
      bstack1l11llll1_opy_[bstack1l111l11ll_opy_[key]] = bstack11l1111lll_opy_[key]
    else:
      bstack1l11llll1_opy_[key] = bstack11l1111lll_opy_[key]
  for key in bstack1lllll111l_opy_:
    if key in bstack1l111l11ll_opy_:
      bstack1l11llll1_opy_[bstack1l111l11ll_opy_[key]] = bstack1lllll111l_opy_[key]
    else:
      bstack1l11llll1_opy_[key] = bstack1lllll111l_opy_[key]
  return bstack1l11llll1_opy_
def bstack11l111111_opy_(config, index=0):
  global bstack11l11111l_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11ll11ll11_opy_ = bstack11lll11l1l_opy_(bstack11lll11ll_opy_, config, logger)
  bstack1lllll111l_opy_ = bstack1lll1lll1l_opy_(config)
  bstack111l1lll1_opy_ = bstack1l1l11111l_opy_
  bstack111l1lll1_opy_ += bstack1l11l11111_opy_
  bstack1lllll111l_opy_ = update(bstack1lllll111l_opy_, bstack11ll11ll11_opy_)
  if bstack11l11111l_opy_:
    bstack111l1lll1_opy_ += bstack1l111ll1l1_opy_
  if bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ૾") in config:
    if bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭૿") in config[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ଀")][index]:
      caps[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଁ")] = config[bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଂ")][index][bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪଃ")]
    if bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ଄") in config[bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଅ")][index]:
      caps[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଆ")] = str(config[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଇ")][index][bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫଈ")])
    bstack11l1l111l1_opy_ = bstack11lll11l1l_opy_(bstack11lll11ll_opy_, config[bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଉ")][index], logger)
    bstack111l1lll1_opy_ += list(bstack11l1l111l1_opy_.keys())
    for bstack1l1ll11l11_opy_ in bstack111l1lll1_opy_:
      if bstack1l1ll11l11_opy_ in config[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଊ")][index]:
        if bstack1l1ll11l11_opy_ == bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨଋ"):
          try:
            bstack11l1l111l1_opy_[bstack1l1ll11l11_opy_] = str(config[bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଌ")][index][bstack1l1ll11l11_opy_] * 1.0)
          except:
            bstack11l1l111l1_opy_[bstack1l1ll11l11_opy_] = str(config[bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ଍")][index][bstack1l1ll11l11_opy_])
        else:
          bstack11l1l111l1_opy_[bstack1l1ll11l11_opy_] = config[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ଎")][index][bstack1l1ll11l11_opy_]
        del (config[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଏ")][index][bstack1l1ll11l11_opy_])
    bstack1lllll111l_opy_ = update(bstack1lllll111l_opy_, bstack11l1l111l1_opy_)
  bstack11l1111lll_opy_ = bstack11l1ll1ll_opy_(config, index)
  for bstack1llllll1l1_opy_ in bstack1l1l11111l_opy_ + list(bstack11ll11ll11_opy_.keys()):
    if bstack1llllll1l1_opy_ in bstack11l1111lll_opy_:
      bstack1lllll111l_opy_[bstack1llllll1l1_opy_] = bstack11l1111lll_opy_[bstack1llllll1l1_opy_]
      del (bstack11l1111lll_opy_[bstack1llllll1l1_opy_])
  if bstack11ll1111ll_opy_(config):
    bstack11l1111lll_opy_[bstack11l111_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫଐ")] = True
    caps.update(bstack1lllll111l_opy_)
    caps[bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭଑")] = bstack11l1111lll_opy_
  else:
    bstack11l1111lll_opy_[bstack11l111_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭଒")] = False
    caps.update(bstack1l11l1ll11_opy_(bstack11l1111lll_opy_, bstack1lllll111l_opy_))
    if bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬଓ") in caps:
      caps[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩଔ")] = caps[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧକ")]
      del (caps[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଖ")])
    if bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬଗ") in caps:
      caps[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧଘ")] = caps[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧଙ")]
      del (caps[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨଚ")])
  return caps
def bstack1111llll1_opy_():
  global bstack1111llll11_opy_
  global CONFIG
  if bstack1ll1l11ll_opy_() <= version.parse(bstack11l111_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨଛ")):
    if bstack1111llll11_opy_ != bstack11l111_opy_ (u"ࠩࠪଜ"):
      return bstack11l111_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦଝ") + bstack1111llll11_opy_ + bstack11l111_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣଞ")
    return bstack1ll1l1l1ll_opy_
  if bstack1111llll11_opy_ != bstack11l111_opy_ (u"ࠬ࠭ଟ"):
    return bstack11l111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣଠ") + bstack1111llll11_opy_ + bstack11l111_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣଡ")
  return bstack11ll11l11_opy_
def bstack1l1l111111_opy_(options):
  return hasattr(options, bstack11l111_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩଢ"))
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
def bstack11l1ll111l_opy_(options, bstack11lll1l11l_opy_):
  for bstack11l1ll11ll_opy_ in bstack11lll1l11l_opy_:
    if bstack11l1ll11ll_opy_ in [bstack11l111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧଣ"), bstack11l111_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧତ")]:
      continue
    if bstack11l1ll11ll_opy_ in options._experimental_options:
      options._experimental_options[bstack11l1ll11ll_opy_] = update(options._experimental_options[bstack11l1ll11ll_opy_],
                                                         bstack11lll1l11l_opy_[bstack11l1ll11ll_opy_])
    else:
      options.add_experimental_option(bstack11l1ll11ll_opy_, bstack11lll1l11l_opy_[bstack11l1ll11ll_opy_])
  if bstack11l111_opy_ (u"ࠫࡦࡸࡧࡴࠩଥ") in bstack11lll1l11l_opy_:
    for arg in bstack11lll1l11l_opy_[bstack11l111_opy_ (u"ࠬࡧࡲࡨࡵࠪଦ")]:
      options.add_argument(arg)
    del (bstack11lll1l11l_opy_[bstack11l111_opy_ (u"࠭ࡡࡳࡩࡶࠫଧ")])
  if bstack11l111_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫନ") in bstack11lll1l11l_opy_:
    for ext in bstack11lll1l11l_opy_[bstack11l111_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ଩")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack11lll1l11l_opy_[bstack11l111_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ପ")])
def bstack111ll11111_opy_(options, bstack1ll1ll1l11_opy_):
  if bstack11l111_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩଫ") in bstack1ll1ll1l11_opy_:
    for bstack1111lllll1_opy_ in bstack1ll1ll1l11_opy_[bstack11l111_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪବ")]:
      if bstack1111lllll1_opy_ in options._preferences:
        options._preferences[bstack1111lllll1_opy_] = update(options._preferences[bstack1111lllll1_opy_], bstack1ll1ll1l11_opy_[bstack11l111_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫଭ")][bstack1111lllll1_opy_])
      else:
        options.set_preference(bstack1111lllll1_opy_, bstack1ll1ll1l11_opy_[bstack11l111_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬମ")][bstack1111lllll1_opy_])
  if bstack11l111_opy_ (u"ࠧࡢࡴࡪࡷࠬଯ") in bstack1ll1ll1l11_opy_:
    for arg in bstack1ll1ll1l11_opy_[bstack11l111_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ର")]:
      options.add_argument(arg)
def bstack111l11ll11_opy_(options, bstack1l11111ll_opy_):
  if bstack11l111_opy_ (u"ࠩࡺࡩࡧࡼࡩࡦࡹࠪ଱") in bstack1l11111ll_opy_:
    options.use_webview(bool(bstack1l11111ll_opy_[bstack11l111_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫଲ")]))
  bstack11l1ll111l_opy_(options, bstack1l11111ll_opy_)
def bstack11l11l1ll1_opy_(options, bstack111ll1111_opy_):
  for bstack1l1l1l111_opy_ in bstack111ll1111_opy_:
    if bstack1l1l1l111_opy_ in [bstack11l111_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨଳ"), bstack11l111_opy_ (u"ࠬࡧࡲࡨࡵࠪ଴")]:
      continue
    options.set_capability(bstack1l1l1l111_opy_, bstack111ll1111_opy_[bstack1l1l1l111_opy_])
  if bstack11l111_opy_ (u"࠭ࡡࡳࡩࡶࠫଵ") in bstack111ll1111_opy_:
    for arg in bstack111ll1111_opy_[bstack11l111_opy_ (u"ࠧࡢࡴࡪࡷࠬଶ")]:
      options.add_argument(arg)
  if bstack11l111_opy_ (u"ࠨࡶࡨࡧ࡭ࡴ࡯࡭ࡱࡪࡽࡕࡸࡥࡷ࡫ࡨࡻࠬଷ") in bstack111ll1111_opy_:
    options.bstack111llllll_opy_(bool(bstack111ll1111_opy_[bstack11l111_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭ସ")]))
def bstack1lll1lllll_opy_(options, bstack11ll1l11l1_opy_):
  for bstack1l1l11ll1l_opy_ in bstack11ll1l11l1_opy_:
    if bstack1l1l11ll1l_opy_ in [bstack11l111_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧହ"), bstack11l111_opy_ (u"ࠫࡦࡸࡧࡴࠩ଺")]:
      continue
    options._options[bstack1l1l11ll1l_opy_] = bstack11ll1l11l1_opy_[bstack1l1l11ll1l_opy_]
  if bstack11l111_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ଻") in bstack11ll1l11l1_opy_:
    for bstack11l11l1l1_opy_ in bstack11ll1l11l1_opy_[bstack11l111_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵ଼ࠪ")]:
      options.bstack1l1111llll_opy_(
        bstack11l11l1l1_opy_, bstack11ll1l11l1_opy_[bstack11l111_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଽ")][bstack11l11l1l1_opy_])
  if bstack11l111_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ା") in bstack11ll1l11l1_opy_:
    for arg in bstack11ll1l11l1_opy_[bstack11l111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧି")]:
      options.add_argument(arg)
def bstack1ll1l11l1_opy_(options, caps):
  if not hasattr(options, bstack11l111_opy_ (u"ࠪࡏࡊ࡟ࠧୀ")):
    return
  if options.KEY == bstack11l111_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩୁ"):
    options = bstack1111l11l_opy_.bstack1ll1ll111_opy_(bstack11llllll11_opy_=options, config=CONFIG)
  if options.KEY == bstack11l111_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪୂ") and options.KEY in caps:
    bstack11l1ll111l_opy_(options, caps[bstack11l111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫୃ")])
  elif options.KEY == bstack11l111_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬୄ") and options.KEY in caps:
    bstack111ll11111_opy_(options, caps[bstack11l111_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭୅")])
  elif options.KEY == bstack11l111_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪ୆") and options.KEY in caps:
    bstack11l11l1ll1_opy_(options, caps[bstack11l111_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫେ")])
  elif options.KEY == bstack11l111_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬୈ") and options.KEY in caps:
    bstack111l11ll11_opy_(options, caps[bstack11l111_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭୉")])
  elif options.KEY == bstack11l111_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬ୊") and options.KEY in caps:
    bstack1lll1lllll_opy_(options, caps[bstack11l111_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ୋ")])
def bstack1111l1111_opy_(caps):
  global bstack11l11111l_opy_
  if isinstance(os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩୌ")), str):
    bstack11l11111l_opy_ = eval(os.getenv(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇ୍ࠪ")))
  if bstack11l11111l_opy_:
    if bstack1ll11lll1_opy_() < version.parse(bstack11l111_opy_ (u"ࠪ࠶࠳࠹࠮࠱ࠩ୎")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11l111_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫ୏")
    if bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ୐") in caps:
      browser = caps[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ୑")]
    elif bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ୒") in caps:
      browser = caps[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ୓")]
    browser = str(browser).lower()
    if browser == bstack11l111_opy_ (u"ࠩ࡬ࡴ࡭ࡵ࡮ࡦࠩ୔") or browser == bstack11l111_opy_ (u"ࠪ࡭ࡵࡧࡤࠨ୕"):
      browser = bstack11l111_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫୖ")
    if browser == bstack11l111_opy_ (u"ࠬࡹࡡ࡮ࡵࡸࡲ࡬࠭ୗ"):
      browser = bstack11l111_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭୘")
    if browser not in [bstack11l111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ୙"), bstack11l111_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭୚"), bstack11l111_opy_ (u"ࠩ࡬ࡩࠬ୛"), bstack11l111_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪଡ଼"), bstack11l111_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬଢ଼")]:
      return None
    try:
      package = bstack11l111_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡿࢂ࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧ୞").format(browser)
      name = bstack11l111_opy_ (u"࠭ࡏࡱࡶ࡬ࡳࡳࡹࠧୟ")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1l1l111111_opy_(options):
        return None
      for bstack1llllll1l1_opy_ in caps.keys():
        options.set_capability(bstack1llllll1l1_opy_, caps[bstack1llllll1l1_opy_])
      bstack1ll1l11l1_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1lll111l11_opy_(options, bstack11lll1ll1_opy_):
  if not bstack1l1l111111_opy_(options):
    return
  for bstack1llllll1l1_opy_ in bstack11lll1ll1_opy_.keys():
    if bstack1llllll1l1_opy_ in bstack1l11l11111_opy_:
      continue
    if bstack1llllll1l1_opy_ in options._caps and type(options._caps[bstack1llllll1l1_opy_]) in [dict, list]:
      options._caps[bstack1llllll1l1_opy_] = update(options._caps[bstack1llllll1l1_opy_], bstack11lll1ll1_opy_[bstack1llllll1l1_opy_])
    else:
      options.set_capability(bstack1llllll1l1_opy_, bstack11lll1ll1_opy_[bstack1llllll1l1_opy_])
  bstack1ll1l11l1_opy_(options, bstack11lll1ll1_opy_)
  if bstack11l111_opy_ (u"ࠧ࡮ࡱࡽ࠾ࡩ࡫ࡢࡶࡩࡪࡩࡷࡇࡤࡥࡴࡨࡷࡸ࠭ୠ") in options._caps:
    if options._caps[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ୡ")] and options._caps[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧୢ")].lower() != bstack11l111_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫୣ"):
      del options._caps[bstack11l111_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪ୤")]
def bstack1l11l111l1_opy_(proxy_config):
  if bstack11l111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ୥") in proxy_config:
    proxy_config[bstack11l111_opy_ (u"࠭ࡳࡴ࡮ࡓࡶࡴࡾࡹࠨ୦")] = proxy_config[bstack11l111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ୧")]
    del (proxy_config[bstack11l111_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ୨")])
  if bstack11l111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬ୩") in proxy_config and proxy_config[bstack11l111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭୪")].lower() != bstack11l111_opy_ (u"ࠫࡩ࡯ࡲࡦࡥࡷࠫ୫"):
    proxy_config[bstack11l111_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ୬")] = bstack11l111_opy_ (u"࠭࡭ࡢࡰࡸࡥࡱ࠭୭")
  if bstack11l111_opy_ (u"ࠧࡱࡴࡲࡼࡾࡇࡵࡵࡱࡦࡳࡳ࡬ࡩࡨࡗࡵࡰࠬ୮") in proxy_config:
    proxy_config[bstack11l111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ୯")] = bstack11l111_opy_ (u"ࠩࡳࡥࡨ࠭୰")
  return proxy_config
def bstack1lll11111l_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11l111_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩୱ") in config:
    return proxy
  config[bstack11l111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ୲")] = bstack1l11l111l1_opy_(config[bstack11l111_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ୳")])
  if proxy == None:
    proxy = Proxy(config[bstack11l111_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୴")])
  return proxy
def bstack1ll11ll11l_opy_(self):
  global CONFIG
  global bstack111ll1ll1_opy_
  try:
    proxy = bstack11l1llllll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11l111_opy_ (u"ࠧ࠯ࡲࡤࡧࠬ୵")):
        proxies = bstack11ll11lll_opy_(proxy, bstack1111llll1_opy_())
        if len(proxies) > 0:
          protocol, bstack1lll1111ll_opy_ = proxies.popitem()
          if bstack11l111_opy_ (u"ࠣ࠼࠲࠳ࠧ୶") in bstack1lll1111ll_opy_:
            return bstack1lll1111ll_opy_
          else:
            return bstack11l111_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥ୷") + bstack1lll1111ll_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢ୸").format(str(e)))
  return bstack111ll1ll1_opy_(self)
def bstack11l1l1l111_opy_():
  global CONFIG
  return bstack1lll1l1l1l_opy_(CONFIG) and bstack11l1ll1111_opy_() and bstack1ll1l11ll_opy_() >= version.parse(bstack11l11ll111_opy_)
def bstack1llll1ll1l_opy_():
  global CONFIG
  return (bstack11l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧ୹") in CONFIG or bstack11l111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ୺") in CONFIG) and bstack1111l1l1ll_opy_()
def bstack11lllllll1_opy_(config):
  bstack1ll11l1lll_opy_ = {}
  if bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ୻") in config:
    bstack1ll11l1lll_opy_ = config[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୼")]
  if bstack11l111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ୽") in config:
    bstack1ll11l1lll_opy_ = config[bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୾")]
  proxy = bstack11l1llllll_opy_(config)
  if proxy:
    if proxy.endswith(bstack11l111_opy_ (u"ࠪ࠲ࡵࡧࡣࠨ୿")) and os.path.isfile(proxy):
      bstack1ll11l1lll_opy_[bstack11l111_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧ஀")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11l111_opy_ (u"ࠬ࠴ࡰࡢࡥࠪ஁")):
        proxies = bstack11l11l1l11_opy_(config, bstack1111llll1_opy_())
        if len(proxies) > 0:
          protocol, bstack1lll1111ll_opy_ = proxies.popitem()
          if bstack11l111_opy_ (u"ࠨ࠺࠰࠱ࠥஂ") in bstack1lll1111ll_opy_:
            parsed_url = urlparse(bstack1lll1111ll_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11l111_opy_ (u"ࠢ࠻࠱࠲ࠦஃ") + bstack1lll1111ll_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1ll11l1lll_opy_[bstack11l111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫ஄")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1ll11l1lll_opy_[bstack11l111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬஅ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1ll11l1lll_opy_[bstack11l111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ஆ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1ll11l1lll_opy_[bstack11l111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧஇ")] = str(parsed_url.password)
  return bstack1ll11l1lll_opy_
def bstack1l11llll1l_opy_(config):
  if bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪஈ") in config:
    return config[bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫஉ")]
  return {}
def bstack11lll1llll_opy_(caps):
  global bstack111l1lll11_opy_
  if bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨஊ") in caps:
    caps[bstack11l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ஋")][bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨ஌")] = True
    if bstack111l1lll11_opy_:
      caps[bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ஍")][bstack11l111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭எ")] = bstack111l1lll11_opy_
  else:
    caps[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪஏ")] = True
    if bstack111l1lll11_opy_:
      caps[bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧஐ")] = bstack111l1lll11_opy_
@measure(event_name=EVENTS.bstack11111lll11_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack111lllll1_opy_():
  global CONFIG
  if not bstack11l11l1ll_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ஑") in CONFIG and bstack1l1lll1ll1_opy_(CONFIG[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬஒ")]):
    if (
      bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ஓ") in CONFIG
      and bstack1l1lll1ll1_opy_(CONFIG[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧஔ")].get(bstack11l111_opy_ (u"ࠫࡸࡱࡩࡱࡄ࡬ࡲࡦࡸࡹࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡤࡸ࡮ࡵ࡮ࠨக")))
    ):
      logger.debug(bstack11l111_opy_ (u"ࠧࡒ࡯ࡤࡣ࡯ࠤࡧ࡯࡮ࡢࡴࡼࠤࡳࡵࡴࠡࡵࡷࡥࡷࡺࡥࡥࠢࡤࡷࠥࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨ஖"))
      return
    bstack1ll11l1lll_opy_ = bstack11lllllll1_opy_(CONFIG)
    bstack111l1l1lll_opy_(CONFIG[bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ஗")], bstack1ll11l1lll_opy_)
def bstack111l1l1lll_opy_(key, bstack1ll11l1lll_opy_):
  global bstack1llll1lll1_opy_
  logger.info(bstack1lllll1l11_opy_)
  try:
    bstack1llll1lll1_opy_ = Local()
    bstack1ll11ll1l_opy_ = {bstack11l111_opy_ (u"ࠧ࡬ࡧࡼࠫ஘"): key}
    bstack1ll11ll1l_opy_.update(bstack1ll11l1lll_opy_)
    logger.debug(bstack11l1l1llll_opy_.format(str(bstack1ll11ll1l_opy_)).replace(key, bstack11l111_opy_ (u"ࠨ࡝ࡕࡉࡉࡇࡃࡕࡇࡇࡡࠬங")))
    bstack1llll1lll1_opy_.start(**bstack1ll11ll1l_opy_)
    if bstack1llll1lll1_opy_.isRunning():
      logger.info(bstack11l1ll11l1_opy_)
  except Exception as e:
    bstack1l1111l11_opy_(bstack1ll1lll11_opy_.format(str(e)))
def bstack1111lll1l1_opy_():
  global bstack1llll1lll1_opy_
  if bstack1llll1lll1_opy_.isRunning():
    logger.info(bstack1l111l1ll_opy_)
    bstack1llll1lll1_opy_.stop()
  bstack1llll1lll1_opy_ = None
def bstack1llllll11l_opy_(bstack1ll1lll1l_opy_=[]):
  global CONFIG
  bstack1l11llll11_opy_ = []
  bstack11l1llll1l_opy_ = [bstack11l111_opy_ (u"ࠩࡲࡷࠬச"), bstack11l111_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭஛"), bstack11l111_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨஜ"), bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ஝"), bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫஞ"), bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨட")]
  try:
    for err in bstack1ll1lll1l_opy_:
      bstack111l1ll1l1_opy_ = {}
      for k in bstack11l1llll1l_opy_:
        val = CONFIG[bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ஠")][int(err[bstack11l111_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ஡")])].get(k)
        if val:
          bstack111l1ll1l1_opy_[k] = val
      if(err[bstack11l111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ஢")] != bstack11l111_opy_ (u"ࠫࠬண")):
        bstack111l1ll1l1_opy_[bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶࡶࠫத")] = {
          err[bstack11l111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ஥")]: err[bstack11l111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭஦")]
        }
        bstack1l11llll11_opy_.append(bstack111l1ll1l1_opy_)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡴࡸ࡭ࡢࡶࡷ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴ࠻ࠢࠪ஧") + str(e))
  finally:
    return bstack1l11llll11_opy_
def bstack11111ll111_opy_(file_name):
  bstack1l1ll11ll1_opy_ = []
  try:
    bstack1l1111lll_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1l1111lll_opy_):
      with open(bstack1l1111lll_opy_) as f:
        bstack1111ll1ll1_opy_ = json.load(f)
        bstack1l1ll11ll1_opy_ = bstack1111ll1ll1_opy_
      os.remove(bstack1l1111lll_opy_)
    return bstack1l1ll11ll1_opy_
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫࡯࡮ࡥ࡫ࡱ࡫ࠥ࡫ࡲࡳࡱࡵࠤࡱ࡯ࡳࡵ࠼ࠣࠫந") + str(e))
    return bstack1l1ll11ll1_opy_
def bstack111lll11l1_opy_():
  try:
      from bstack_utils.constants import bstack111l111l11_opy_, EVENTS
      from bstack_utils.helper import bstack111l1llll1_opy_, get_host_info, bstack11111l11_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack111ll11lll_opy_ = os.path.join(os.getcwd(), bstack11l111_opy_ (u"ࠪࡰࡴ࡭ࠧன"), bstack11l111_opy_ (u"ࠫࡰ࡫ࡹ࠮࡯ࡨࡸࡷ࡯ࡣࡴ࠰࡭ࡷࡴࡴࠧப"))
      lock = FileLock(bstack111ll11lll_opy_+bstack11l111_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦ஫"))
      def bstack1ll11lll_opy_():
          try:
              with lock:
                  with open(bstack111ll11lll_opy_, bstack11l111_opy_ (u"ࠨࡲࠣ஬"), encoding=bstack11l111_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨ஭")) as file:
                      data = json.load(file)
                      config = {
                          bstack11l111_opy_ (u"ࠣࡪࡨࡥࡩ࡫ࡲࡴࠤம"): {
                              bstack11l111_opy_ (u"ࠤࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠣய"): bstack11l111_opy_ (u"ࠥࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳࠨர"),
                          }
                      }
                      bstack1l111ll11_opy_ = datetime.utcnow()
                      bstack11lllll1_opy_ = bstack1l111ll11_opy_.strftime(bstack11l111_opy_ (u"ࠦࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࠯ࠧࡩࠤ࡚࡚ࡃࠣற"))
                      test_id = os.environ.get(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪல")) if os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫள")) else bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤழ"))
                      payload = {
                          bstack11l111_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠧவ"): bstack11l111_opy_ (u"ࠤࡶࡨࡰࡥࡥࡷࡧࡱࡸࡸࠨஶ"),
                          bstack11l111_opy_ (u"ࠥࡨࡦࡺࡡࠣஷ"): {
                              bstack11l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡪࡸࡦࡤࡻࡵࡪࡦࠥஸ"): test_id,
                              bstack11l111_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡩࡥࡤࡢࡻࠥஹ"): bstack11lllll1_opy_,
                              bstack11l111_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࠥ஺"): bstack11l111_opy_ (u"ࠢࡔࡆࡎࡊࡪࡧࡴࡶࡴࡨࡔࡪࡸࡦࡰࡴࡰࡥࡳࡩࡥࠣ஻"),
                              bstack11l111_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟࡫ࡵࡲࡲࠧ஼"): {
                                  bstack11l111_opy_ (u"ࠤࡰࡩࡦࡹࡵࡳࡧࡶࠦ஽"): data,
                                  bstack11l111_opy_ (u"ࠥࡷࡩࡱࡒࡶࡰࡌࡨࠧா"): bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠦࡸࡪ࡫ࡓࡷࡱࡍࡩࠨி"))
                              },
                              bstack11l111_opy_ (u"ࠧࡻࡳࡦࡴࡢࡨࡦࡺࡡࠣீ"): bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠨࡵࡴࡧࡵࡒࡦࡳࡥࠣு")),
                              bstack11l111_opy_ (u"ࠢࡩࡱࡶࡸࡤ࡯࡮ࡧࡱࠥூ"): get_host_info()
                          }
                      }
                      bstack1111ll11ll_opy_ = bstack111111ll11_opy_(cli.config, [bstack11l111_opy_ (u"ࠣࡣࡳ࡭ࡸࠨ௃"), bstack11l111_opy_ (u"ࠤࡨࡨࡸࡏ࡮ࡴࡶࡵࡹࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴࠢ௄"), bstack11l111_opy_ (u"ࠥࡥࡵ࡯ࠢ௅")], bstack111l111l11_opy_)
                      response = bstack111l1llll1_opy_(bstack11l111_opy_ (u"ࠦࡕࡕࡓࡕࠤெ"), bstack1111ll11ll_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack11l111_opy_ (u"ࠧࡊࡡࡵࡣࠣࡷࡪࡴࡴࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡵࡱࠣࡿࢂࠦࡷࡪࡶ࡫ࠤࡩࡧࡴࡢࠢࡾࢁࠧே").format(bstack111l111l11_opy_, payload))
                      else:
                          logger.debug(bstack11l111_opy_ (u"ࠨࡒࡦࡳࡸࡩࡸࡺࠠࡧࡣ࡬ࡰࡪࡪࠠࡧࡱࡵࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡪࡡࡵࡣࠣࡿࢂࠨை").format(bstack111l111l11_opy_, payload))
          except Exception as e:
              logger.debug(bstack11l111_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡴࡤࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࠦࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡࡽࢀࠦ௉").format(e))
      bstack1ll11lll_opy_()
      bstack1ll11111l1_opy_(bstack111ll11lll_opy_, logger)
  except:
    pass
def bstack11lllll11l_opy_():
  global bstack1111ll1l11_opy_
  global bstack11l11l111_opy_
  global bstack1l11l1l11_opy_
  global bstack11lllllll_opy_
  global bstack11111lllll_opy_
  global bstack1l11111l11_opy_
  global CONFIG
  bstack111l11l11_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩொ"))
  if bstack111l11l11_opy_ in [bstack11l111_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨோ"), bstack11l111_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩௌ")]:
    bstack11lll1lll_opy_()
  percy.shutdown()
  if bstack1111ll1l11_opy_:
    logger.warning(bstack1lllll1ll1_opy_.format(str(bstack1111ll1l11_opy_)))
  else:
    try:
      bstack1lllll1l1l_opy_ = bstack11l1lll1l1_opy_(bstack11l111_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰ்ࠪ"), logger)
      if bstack1lllll1l1l_opy_.get(bstack11l111_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪ௎")) and bstack1lllll1l1l_opy_.get(bstack11l111_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫ௏")).get(bstack11l111_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩௐ")):
        logger.warning(bstack1lllll1ll1_opy_.format(str(bstack1lllll1l1l_opy_[bstack11l111_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭௑")][bstack11l111_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫ௒")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1l11ll1l11_opy_.invoke(Events.bstack1ll1l1111l_opy_)
  logger.info(bstack1111l1l11_opy_)
  global bstack1llll1lll1_opy_
  if bstack1llll1lll1_opy_:
    bstack1111lll1l1_opy_()
  try:
    with bstack1l111l1l11_opy_:
      bstack1ll11lll1l_opy_ = bstack11l11l111_opy_.copy()
    for driver in bstack1ll11lll1l_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack111ll1111l_opy_)
  if bstack1l11111l11_opy_ == bstack11l111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ௓"):
    bstack11111lllll_opy_ = bstack11111ll111_opy_(bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ௔"))
  if bstack1l11111l11_opy_ == bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ௕") and len(bstack11lllllll_opy_) == 0:
    bstack11lllllll_opy_ = bstack11111ll111_opy_(bstack11l111_opy_ (u"࠭ࡰࡸࡡࡳࡽࡹ࡫ࡳࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫ௖"))
    if len(bstack11lllllll_opy_) == 0:
      bstack11lllllll_opy_ = bstack11111ll111_opy_(bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡱࡲࡳࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ௗ"))
  bstack1ll11111l_opy_ = bstack11l111_opy_ (u"ࠨࠩ௘")
  if len(bstack1l11l1l11_opy_) > 0:
    bstack1ll11111l_opy_ = bstack1llllll11l_opy_(bstack1l11l1l11_opy_)
  elif len(bstack11lllllll_opy_) > 0:
    bstack1ll11111l_opy_ = bstack1llllll11l_opy_(bstack11lllllll_opy_)
  elif len(bstack11111lllll_opy_) > 0:
    bstack1ll11111l_opy_ = bstack1llllll11l_opy_(bstack11111lllll_opy_)
  elif len(bstack111ll11l1_opy_) > 0:
    bstack1ll11111l_opy_ = bstack1llllll11l_opy_(bstack111ll11l1_opy_)
  if bool(bstack1ll11111l_opy_):
    bstack111l111lll_opy_(bstack1ll11111l_opy_)
  else:
    bstack111l111lll_opy_()
  bstack1ll11111l1_opy_(bstack11111l11ll_opy_, logger)
  if bstack111l11l11_opy_ not in [bstack11l111_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ௙")]:
    bstack111lll11l1_opy_()
  bstack11l111l1ll_opy_.bstack1ll1l111_opy_(CONFIG)
  if len(bstack11111lllll_opy_) > 0:
    sys.exit(len(bstack11111lllll_opy_))
def bstack1ll1l1l111_opy_(bstack111l1l1l1_opy_, frame):
  global bstack11111l11_opy_
  logger.error(bstack1111lll11l_opy_)
  bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡒࡴ࠭௚"), bstack111l1l1l1_opy_)
  if hasattr(signal, bstack11l111_opy_ (u"ࠫࡘ࡯ࡧ࡯ࡣ࡯ࡷࠬ௛")):
    bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ௜"), signal.Signals(bstack111l1l1l1_opy_).name)
  else:
    bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭௝"), bstack11l111_opy_ (u"ࠧࡔࡋࡊ࡙ࡓࡑࡎࡐ࡙ࡑࠫ௞"))
  if cli.is_running():
    bstack1l11ll1l11_opy_.invoke(Events.bstack1ll1l1111l_opy_)
  bstack111l11l11_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩ௟"))
  if bstack111l11l11_opy_ == bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ௠") and not cli.is_enabled(CONFIG):
    bstack1lll111l_opy_.stop(bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪ௡")))
  bstack11lllll11l_opy_()
  sys.exit(1)
def bstack1l1111l11_opy_(err):
  logger.critical(bstack1llllll111_opy_.format(str(err)))
  bstack111l111lll_opy_(bstack1llllll111_opy_.format(str(err)), True)
  atexit.unregister(bstack11lllll11l_opy_)
  bstack11lll1lll_opy_()
  sys.exit(1)
def bstack11111l1l1_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack111l111lll_opy_(message, True)
  atexit.unregister(bstack11lllll11l_opy_)
  bstack11lll1lll_opy_()
  sys.exit(1)
def bstack111ll1ll11_opy_():
  global CONFIG
  global bstack1ll11l1l11_opy_
  global bstack1111l111l1_opy_
  global bstack11l1111l11_opy_
  CONFIG = bstack1l1l1l11ll_opy_()
  load_dotenv(CONFIG.get(bstack11l111_opy_ (u"ࠫࡪࡴࡶࡇ࡫࡯ࡩࠬ௢")))
  bstack1lll1l11l1_opy_()
  bstack11lll1111l_opy_()
  CONFIG = bstack111lllllll_opy_(CONFIG)
  update(CONFIG, bstack1111l111l1_opy_)
  update(CONFIG, bstack1ll11l1l11_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1l1ll11l1l_opy_(CONFIG)
  bstack11l1111l11_opy_ = bstack11l11l1ll_opy_(CONFIG)
  os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ௣")] = bstack11l1111l11_opy_.__str__().lower()
  bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ௤"), bstack11l1111l11_opy_)
  if (bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ௥") in CONFIG and bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௦") in bstack1ll11l1l11_opy_) or (
          bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௧") in CONFIG and bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௨") not in bstack1111l111l1_opy_):
    if os.getenv(bstack11l111_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨ௩")):
      CONFIG[bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ௪")] = os.getenv(bstack11l111_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪ௫"))
    else:
      if not CONFIG.get(bstack11l111_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠥ௬"), bstack11l111_opy_ (u"ࠣࠤ௭")) in bstack1l1lllll11_opy_:
        bstack11ll1l111_opy_()
  elif (bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௮") not in CONFIG and bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ௯") in CONFIG) or (
          bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௰") in bstack1111l111l1_opy_ and bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௱") not in bstack1ll11l1l11_opy_):
    del (CONFIG[bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ௲")])
  if bstack11l1l1l11l_opy_(CONFIG):
    bstack1l1111l11_opy_(bstack11l111ll1l_opy_)
  Config.bstack111l11l1_opy_().set_property(bstack11l111_opy_ (u"ࠢࡶࡵࡨࡶࡓࡧ࡭ࡦࠤ௳"), CONFIG[bstack11l111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ௴")])
  bstack11l1lll11l_opy_()
  bstack111111l1ll_opy_()
  if bstack11l11111l_opy_ and not CONFIG.get(bstack11l111_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠧ௵"), bstack11l111_opy_ (u"ࠥࠦ௶")) in bstack1l1lllll11_opy_:
    CONFIG[bstack11l111_opy_ (u"ࠫࡦࡶࡰࠨ௷")] = bstack1l11l11l1l_opy_(CONFIG)
    logger.info(bstack1ll11ll111_opy_.format(CONFIG[bstack11l111_opy_ (u"ࠬࡧࡰࡱࠩ௸")]))
  if not bstack11l1111l11_opy_:
    CONFIG[bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ௹")] = [{}]
def bstack111llll11l_opy_(config, bstack1l11l1111l_opy_):
  global CONFIG
  global bstack11l11111l_opy_
  CONFIG = config
  bstack11l11111l_opy_ = bstack1l11l1111l_opy_
def bstack111111l1ll_opy_():
  global CONFIG
  global bstack11l11111l_opy_
  if bstack11l111_opy_ (u"ࠧࡢࡲࡳࠫ௺") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack11111l1l1_opy_(e, bstack1l11111l1l_opy_)
    bstack11l11111l_opy_ = True
    bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ௻"), True)
def bstack1l11l11l1l_opy_(config):
  bstack1ll1111l1l_opy_ = bstack11l111_opy_ (u"ࠩࠪ௼")
  app = config[bstack11l111_opy_ (u"ࠪࡥࡵࡶࠧ௽")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1llll1l11l_opy_:
      if os.path.exists(app):
        bstack1ll1111l1l_opy_ = bstack1ll1ll11ll_opy_(config, app)
      elif bstack1l11l1llll_opy_(app):
        bstack1ll1111l1l_opy_ = app
      else:
        bstack1l1111l11_opy_(bstack1l1111l1ll_opy_.format(app))
    else:
      if bstack1l11l1llll_opy_(app):
        bstack1ll1111l1l_opy_ = app
      elif os.path.exists(app):
        bstack1ll1111l1l_opy_ = bstack1ll1ll11ll_opy_(app)
      else:
        bstack1l1111l11_opy_(bstack111ll1l11l_opy_)
  else:
    if len(app) > 2:
      bstack1l1111l11_opy_(bstack1l1l1ll111_opy_)
    elif len(app) == 2:
      if bstack11l111_opy_ (u"ࠫࡵࡧࡴࡩࠩ௾") in app and bstack11l111_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ௿") in app:
        if os.path.exists(app[bstack11l111_opy_ (u"࠭ࡰࡢࡶ࡫ࠫఀ")]):
          bstack1ll1111l1l_opy_ = bstack1ll1ll11ll_opy_(config, app[bstack11l111_opy_ (u"ࠧࡱࡣࡷ࡬ࠬఁ")], app[bstack11l111_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫం")])
        else:
          bstack1l1111l11_opy_(bstack1l1111l1ll_opy_.format(app))
      else:
        bstack1l1111l11_opy_(bstack1l1l1ll111_opy_)
    else:
      for key in app:
        if key in bstack1ll1l1ll1_opy_:
          if key == bstack11l111_opy_ (u"ࠩࡳࡥࡹ࡮ࠧః"):
            if os.path.exists(app[key]):
              bstack1ll1111l1l_opy_ = bstack1ll1ll11ll_opy_(config, app[key])
            else:
              bstack1l1111l11_opy_(bstack1l1111l1ll_opy_.format(app))
          else:
            bstack1ll1111l1l_opy_ = app[key]
        else:
          bstack1l1111l11_opy_(bstack1l11l11lll_opy_)
  return bstack1ll1111l1l_opy_
def bstack1l11l1llll_opy_(bstack1ll1111l1l_opy_):
  import re
  bstack1l1111ll1l_opy_ = re.compile(bstack11l111_opy_ (u"ࡵࠦࡣࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥఄ"))
  bstack111ll1l111_opy_ = re.compile(bstack11l111_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬ࠲࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰ࠤࠣఅ"))
  if bstack11l111_opy_ (u"ࠬࡨࡳ࠻࠱࠲ࠫఆ") in bstack1ll1111l1l_opy_ or re.fullmatch(bstack1l1111ll1l_opy_, bstack1ll1111l1l_opy_) or re.fullmatch(bstack111ll1l111_opy_, bstack1ll1111l1l_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack1ll1l1l1l1_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack1ll1ll11ll_opy_(config, path, bstack11l111l1l1_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11l111_opy_ (u"࠭ࡲࡣࠩఇ")).read()).hexdigest()
  bstack1l1l1ll11_opy_ = bstack1l11l111l_opy_(md5_hash)
  bstack1ll1111l1l_opy_ = None
  if bstack1l1l1ll11_opy_:
    logger.info(bstack1ll1111l11_opy_.format(bstack1l1l1ll11_opy_, md5_hash))
    return bstack1l1l1ll11_opy_
  bstack1l1ll1ll1_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack11l111_opy_ (u"ࠧࡧ࡫࡯ࡩࠬఈ"): (os.path.basename(path), open(os.path.abspath(path), bstack11l111_opy_ (u"ࠨࡴࡥࠫఉ")), bstack11l111_opy_ (u"ࠩࡷࡩࡽࡺ࠯ࡱ࡮ࡤ࡭ࡳ࠭ఊ")),
      bstack11l111_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭ఋ"): bstack11l111l1l1_opy_
    }
  )
  response = requests.post(bstack11l1l1lll_opy_, data=multipart_data,
                           headers={bstack11l111_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪఌ"): multipart_data.content_type},
                           auth=(config[bstack11l111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ఍")], config[bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩఎ")]))
  try:
    res = json.loads(response.text)
    bstack1ll1111l1l_opy_ = res[bstack11l111_opy_ (u"ࠧࡢࡲࡳࡣࡺࡸ࡬ࠨఏ")]
    logger.info(bstack1ll11l11l1_opy_.format(bstack1ll1111l1l_opy_))
    bstack1ll11ll11_opy_(md5_hash, bstack1ll1111l1l_opy_)
    cli.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠣࡪࡷࡸࡵࡀࡵࡱ࡮ࡲࡥࡩࡥࡡࡱࡲࠥఐ"), datetime.datetime.now() - bstack1l1ll1ll1_opy_)
  except ValueError as err:
    bstack1l1111l11_opy_(bstack111ll1l11_opy_.format(str(err)))
  return bstack1ll1111l1l_opy_
def bstack11l1lll11l_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1lll1ll1l1_opy_
  bstack1ll1llll1_opy_ = 1
  bstack1l11l11l11_opy_ = 1
  if bstack11l111_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ఑") in CONFIG:
    bstack1l11l11l11_opy_ = CONFIG[bstack11l111_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪఒ")]
  else:
    bstack1l11l11l11_opy_ = bstack11l1ll11l_opy_(framework_name, args) or 1
  if bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧఓ") in CONFIG:
    bstack1ll1llll1_opy_ = len(CONFIG[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఔ")])
  bstack1lll1ll1l1_opy_ = int(bstack1l11l11l11_opy_) * int(bstack1ll1llll1_opy_)
def bstack11l1ll11l_opy_(framework_name, args):
  if framework_name == bstack1l1ll1ll11_opy_ and args and bstack11l111_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫక") in args:
      bstack1ll11lll11_opy_ = args.index(bstack11l111_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬఖ"))
      return int(args[bstack1ll11lll11_opy_ + 1]) or 1
  return 1
def bstack1l11l111l_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l111_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫగ"))
    bstack11ll11l111_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠩࢁࠫఘ")), bstack11l111_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪఙ"), bstack11l111_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬచ"))
    if os.path.exists(bstack11ll11l111_opy_):
      try:
        bstack1111lllll_opy_ = json.load(open(bstack11ll11l111_opy_, bstack11l111_opy_ (u"ࠬࡸࡢࠨఛ")))
        if md5_hash in bstack1111lllll_opy_:
          bstack1l1l111l1l_opy_ = bstack1111lllll_opy_[md5_hash]
          bstack11llll1ll_opy_ = datetime.datetime.now()
          bstack111lll1111_opy_ = datetime.datetime.strptime(bstack1l1l111l1l_opy_[bstack11l111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩజ")], bstack11l111_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫఝ"))
          if (bstack11llll1ll_opy_ - bstack111lll1111_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack1l1l111l1l_opy_[bstack11l111_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ఞ")]):
            return None
          return bstack1l1l111l1l_opy_[bstack11l111_opy_ (u"ࠩ࡬ࡨࠬట")]
      except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡑࡉ࠻ࠠࡩࡣࡶ࡬ࠥ࡬ࡩ࡭ࡧ࠽ࠤࢀࢃࠧఠ").format(str(e)))
    return None
  bstack11ll11l111_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠫࢃ࠭డ")), bstack11l111_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬఢ"), bstack11l111_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧణ"))
  lock_file = bstack11ll11l111_opy_ + bstack11l111_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ࠭త")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack11ll11l111_opy_):
        with open(bstack11ll11l111_opy_, bstack11l111_opy_ (u"ࠨࡴࠪథ")) as f:
          content = f.read().strip()
          if content:
            bstack1111lllll_opy_ = json.loads(content)
            if md5_hash in bstack1111lllll_opy_:
              bstack1l1l111l1l_opy_ = bstack1111lllll_opy_[md5_hash]
              bstack11llll1ll_opy_ = datetime.datetime.now()
              bstack111lll1111_opy_ = datetime.datetime.strptime(bstack1l1l111l1l_opy_[bstack11l111_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬద")], bstack11l111_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧధ"))
              if (bstack11llll1ll_opy_ - bstack111lll1111_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack1l1l111l1l_opy_[bstack11l111_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩన")]):
                return None
              return bstack1l1l111l1l_opy_[bstack11l111_opy_ (u"ࠬ࡯ࡤࠨ఩")]
      return None
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡽࡩࡵࡪࠣࡪ࡮ࡲࡥࠡ࡮ࡲࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨ࠻ࠢࡾࢁࠬప").format(str(e)))
    return None
def bstack1ll11ll11_opy_(md5_hash, bstack1ll1111l1l_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l111_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠢࡱࡳࡹࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡥࡥࡸ࡯ࡣࠡࡨ࡬ࡰࡪࠦ࡯ࡱࡧࡵࡥࡹ࡯࡯࡯ࡵࠪఫ"))
    bstack11l1l1ll11_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠨࢀࠪబ")), bstack11l111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩభ"))
    if not os.path.exists(bstack11l1l1ll11_opy_):
      os.makedirs(bstack11l1l1ll11_opy_)
    bstack11ll11l111_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠪࢂࠬమ")), bstack11l111_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫయ"), bstack11l111_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ర"))
    bstack1l1ll111l1_opy_ = {
      bstack11l111_opy_ (u"࠭ࡩࡥࠩఱ"): bstack1ll1111l1l_opy_,
      bstack11l111_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪల"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l111_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬళ")),
      bstack11l111_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧఴ"): str(__version__)
    }
    try:
      bstack1111lllll_opy_ = {}
      if os.path.exists(bstack11ll11l111_opy_):
        bstack1111lllll_opy_ = json.load(open(bstack11ll11l111_opy_, bstack11l111_opy_ (u"ࠪࡶࡧ࠭వ")))
      bstack1111lllll_opy_[md5_hash] = bstack1l1ll111l1_opy_
      with open(bstack11ll11l111_opy_, bstack11l111_opy_ (u"ࠦࡼ࠱ࠢశ")) as outfile:
        json.dump(bstack1111lllll_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡺࡶࡤࡢࡶ࡬ࡲ࡬ࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨࠡࡨ࡬ࡰࡪࡀࠠࡼࡿࠪష").format(str(e)))
    return
  bstack11l1l1ll11_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"࠭ࡾࠨస")), bstack11l111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧహ"))
  if not os.path.exists(bstack11l1l1ll11_opy_):
    os.makedirs(bstack11l1l1ll11_opy_)
  bstack11ll11l111_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠨࢀࠪ఺")), bstack11l111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ఻"), bstack11l111_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱ఼ࠫ"))
  lock_file = bstack11ll11l111_opy_ + bstack11l111_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪఽ")
  bstack1l1ll111l1_opy_ = {
    bstack11l111_opy_ (u"ࠬ࡯ࡤࠨా"): bstack1ll1111l1l_opy_,
    bstack11l111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩి"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l111_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫీ")),
    bstack11l111_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ు"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1111lllll_opy_ = {}
      if os.path.exists(bstack11ll11l111_opy_):
        with open(bstack11ll11l111_opy_, bstack11l111_opy_ (u"ࠩࡵࠫూ")) as f:
          content = f.read().strip()
          if content:
            bstack1111lllll_opy_ = json.loads(content)
      bstack1111lllll_opy_[md5_hash] = bstack1l1ll111l1_opy_
      with open(bstack11ll11l111_opy_, bstack11l111_opy_ (u"ࠥࡻࠧృ")) as outfile:
        json.dump(bstack1111lllll_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡻ࡮ࡺࡨࠡࡨ࡬ࡰࡪࠦ࡬ࡰࡥ࡮࡭ࡳ࡭ࠠࡧࡱࡵࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࠦࡵࡱࡦࡤࡸࡪࡀࠠࡼࡿࠪౄ").format(str(e)))
def bstack1l1ll1l1l1_opy_(self):
  return
def bstack111lll1ll_opy_(self):
  return
def bstack1l1lll1l11_opy_():
  global bstack11llll11l1_opy_
  bstack11llll11l1_opy_ = True
@measure(event_name=EVENTS.bstack1l1l11lll_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack11l1l11l11_opy_(self):
  global bstack1111l1l1l1_opy_
  global bstack11lll1lll1_opy_
  global bstack11l1lll11_opy_
  try:
    if bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ౅") in bstack1111l1l1l1_opy_ and self.session_id != None and bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪె"), bstack11l111_opy_ (u"ࠧࠨే")) != bstack11l111_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩై"):
      bstack1ll11l1l1_opy_ = bstack11l111_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ౉") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪొ")
      if bstack1ll11l1l1_opy_ == bstack11l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫో"):
        bstack111l11l11l_opy_(logger)
      if self != None:
        bstack11ll11lll1_opy_(self, bstack1ll11l1l1_opy_, bstack11l111_opy_ (u"ࠬ࠲ࠠࠨౌ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11l111_opy_ (u"్࠭ࠧ")
    if bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ౎") in bstack1111l1l1l1_opy_ and getattr(threading.current_thread(), bstack11l111_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ౏"), None):
      bstack111lll11_opy_.bstack11111111_opy_(self, bstack11l11l1lll_opy_, logger, wait=True)
    if bstack11l111_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ౐") in bstack1111l1l1l1_opy_:
      if not threading.currentThread().behave_test_status:
        bstack11ll11lll1_opy_(self, bstack11l111_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ౑"))
      bstack11l11l11ll_opy_.bstack111ll1lll1_opy_(self)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧ౒") + str(e))
  bstack11l1lll11_opy_(self)
  self.session_id = None
def bstack1l111111l1_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack11l1l1l1l_opy_
    global bstack1111l1l1l1_opy_
    command_executor = kwargs.get(bstack11l111_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠨ౓"), bstack11l111_opy_ (u"࠭ࠧ౔"))
    bstack1ll11l1111_opy_ = False
    if type(command_executor) == str and bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ౕࠪ") in command_executor:
      bstack1ll11l1111_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰౖࠫ") in str(getattr(command_executor, bstack11l111_opy_ (u"ࠩࡢࡹࡷࡲࠧ౗"), bstack11l111_opy_ (u"ࠪࠫౘ"))):
      bstack1ll11l1111_opy_ = True
    else:
      kwargs = bstack1111l11l_opy_.bstack1ll1ll111_opy_(bstack11llllll11_opy_=kwargs, config=CONFIG)
      return bstack1ll1l1lll1_opy_(self, *args, **kwargs)
    if bstack1ll11l1111_opy_:
      bstack111ll111l1_opy_ = bstack11ll111ll_opy_.bstack1l1llll1ll_opy_(CONFIG, bstack1111l1l1l1_opy_)
      if kwargs.get(bstack11l111_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬౙ")):
        kwargs[bstack11l111_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ౚ")] = bstack11l1l1l1l_opy_(kwargs[bstack11l111_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ౛")], bstack1111l1l1l1_opy_, CONFIG, bstack111ll111l1_opy_)
      elif kwargs.get(bstack11l111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ౜")):
        kwargs[bstack11l111_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨౝ")] = bstack11l1l1l1l_opy_(kwargs[bstack11l111_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ౞")], bstack1111l1l1l1_opy_, CONFIG, bstack111ll111l1_opy_)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡘࡊࡋࠡࡥࡤࡴࡸࡀࠠࡼࡿࠥ౟").format(str(e)))
  return bstack1ll1l1lll1_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack111l11ll1l_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack11ll1l1111_opy_(self, command_executor=bstack11l111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳࠶࠸࠷࠯࠲࠱࠴࠳࠷࠺࠵࠶࠷࠸ࠧౠ"), *args, **kwargs):
  global bstack11lll1lll1_opy_
  global bstack11l11l111_opy_
  bstack1l1lll11l_opy_ = bstack1l111111l1_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1lll1lll_opy_.on():
    return bstack1l1lll11l_opy_
  try:
    logger.debug(bstack11l111_opy_ (u"ࠬࡉ࡯࡮࡯ࡤࡲࡩࠦࡅࡹࡧࡦࡹࡹࡵࡲࠡࡹ࡫ࡩࡳࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥ࡬ࡡ࡭ࡵࡨࠤ࠲ࠦࡻࡾࠩౡ").format(str(command_executor)))
    logger.debug(bstack11l111_opy_ (u"࠭ࡈࡶࡤ࡙ࠣࡗࡒࠠࡪࡵࠣ࠱ࠥࢁࡽࠨౢ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪౣ") in command_executor._url:
      bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ౤"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ౥") in command_executor):
    bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ౦"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1lll11lll1_opy_ = getattr(threading.current_thread(), bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥࠬ౧"), None)
  bstack1ll111ll11_opy_ = {}
  if self.capabilities is not None:
    bstack1ll111ll11_opy_[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫ౨")] = self.capabilities.get(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ౩"))
    bstack1ll111ll11_opy_[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ౪")] = self.capabilities.get(bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ౫"))
    bstack1ll111ll11_opy_[bstack11l111_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࠪ౬")] = self.capabilities.get(bstack11l111_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ౭"))
  if CONFIG.get(bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ౮"), False) and bstack1111l11l_opy_.bstack1l1ll1lll1_opy_(bstack1ll111ll11_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack11l111_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ౯") in bstack1111l1l1l1_opy_ or bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ౰") in bstack1111l1l1l1_opy_:
    bstack1lll111l_opy_.bstack11l1l1l11_opy_(self)
  if bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ౱") in bstack1111l1l1l1_opy_ and bstack1lll11lll1_opy_ and bstack1lll11lll1_opy_.get(bstack11l111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ౲"), bstack11l111_opy_ (u"ࠩࠪ౳")) == bstack11l111_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫ౴"):
    bstack1lll111l_opy_.bstack11l1l1l11_opy_(self)
  bstack11lll1lll1_opy_ = self.session_id
  with bstack1l111l1l11_opy_:
    bstack11l11l111_opy_.append(self)
  return bstack1l1lll11l_opy_
def bstack1l11111111_opy_(args):
  return bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠬ౵") in str(args)
def bstack1lll11ll1l_opy_(self, driver_command, *args, **kwargs):
  global bstack1ll111l111_opy_
  global bstack111l1l11l1_opy_
  bstack11l1l111ll_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ౶"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ౷"), None)
  bstack11l1lllll1_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ౸"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ౹"), None)
  bstack11ll1lll1_opy_ = getattr(self, bstack11l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩ౺"), None) != None and getattr(self, bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ౻"), None) == True
  if not bstack111l1l11l1_opy_ and bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ౼") in CONFIG and CONFIG[bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ౽")] == True and bstack111l1ll1l_opy_.bstack11lll11ll1_opy_(driver_command) and (bstack11ll1lll1_opy_ or bstack11l1l111ll_opy_ or bstack11l1lllll1_opy_) and not bstack1l11111111_opy_(args):
    try:
      bstack111l1l11l1_opy_ = True
      logger.debug(bstack11l111_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࢁࡽࠨ౾").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11l111_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡪࡸࡦࡰࡴࡰࠤࡸࡩࡡ࡯ࠢࡾࢁࠬ౿").format(str(err)))
    bstack111l1l11l1_opy_ = False
  response = bstack1ll111l111_opy_(self, driver_command, *args, **kwargs)
  if (bstack11l111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧಀ") in str(bstack1111l1l1l1_opy_).lower() or bstack11l111_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩಁ") in str(bstack1111l1l1l1_opy_).lower()) and bstack1lll1lll_opy_.on():
    try:
      if driver_command == bstack11l111_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧಂ"):
        bstack1lll111l_opy_.bstack111l11lll_opy_({
            bstack11l111_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࠪಃ"): response[bstack11l111_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫ಄")],
            bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ಅ"): bstack1lll111l_opy_.current_test_uuid() if bstack1lll111l_opy_.current_test_uuid() else bstack1lll1lll_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1ll1111ll1_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack1ll1l1l11l_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack11lll1lll1_opy_
  global bstack1l1l11llll_opy_
  global bstack11lll111ll_opy_
  global bstack1l11ll11l1_opy_
  global bstack1ll1l11lll_opy_
  global bstack1111l1l1l1_opy_
  global bstack1ll1l1lll1_opy_
  global bstack11l11l111_opy_
  global bstack11lll11l1_opy_
  global bstack11l11l1lll_opy_
  if os.getenv(bstack11l111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬಆ")) is not None and bstack1111l11l_opy_.bstack1l11l111ll_opy_(CONFIG) is None:
    CONFIG[bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨಇ")] = True
  CONFIG[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫಈ")] = str(bstack1111l1l1l1_opy_) + str(__version__)
  bstack11l11l1l1l_opy_ = os.environ[bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨಉ")]
  bstack111ll111l1_opy_ = bstack11ll111ll_opy_.bstack1l1llll1ll_opy_(CONFIG, bstack1111l1l1l1_opy_)
  CONFIG[bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧಊ")] = bstack11l11l1l1l_opy_
  CONFIG[bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧಋ")] = bstack111ll111l1_opy_
  if CONFIG.get(bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ಌ"),bstack11l111_opy_ (u"ࠧࠨ಍")) and bstack11l111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧಎ") in bstack1111l1l1l1_opy_:
    CONFIG[bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩಏ")].pop(bstack11l111_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨಐ"), None)
    CONFIG[bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ಑")].pop(bstack11l111_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪಒ"), None)
  command_executor = bstack1111llll1_opy_()
  logger.debug(bstack1111ll1l1_opy_.format(command_executor))
  proxy = bstack1lll11111l_opy_(CONFIG, proxy)
  bstack1l1lll111l_opy_ = 0 if bstack1l1l11llll_opy_ < 0 else bstack1l1l11llll_opy_
  try:
    if bstack1l11ll11l1_opy_ is True:
      bstack1l1lll111l_opy_ = int(multiprocessing.current_process().name)
    elif bstack1ll1l11lll_opy_ is True:
      bstack1l1lll111l_opy_ = int(threading.current_thread().name)
  except:
    bstack1l1lll111l_opy_ = 0
  bstack11lll1ll1_opy_ = bstack11l111111_opy_(CONFIG, bstack1l1lll111l_opy_)
  logger.debug(bstack1l11ll11l_opy_.format(str(bstack11lll1ll1_opy_)))
  if bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪಓ") in CONFIG and bstack1l1lll1ll1_opy_(CONFIG[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫಔ")]):
    bstack11lll1llll_opy_(bstack11lll1ll1_opy_)
  if bstack1111l11l_opy_.bstack11l111lll1_opy_(CONFIG, bstack1l1lll111l_opy_) and bstack1111l11l_opy_.bstack1111ll111_opy_(bstack11lll1ll1_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack1111l11l_opy_.set_capabilities(bstack11lll1ll1_opy_, CONFIG)
  if desired_capabilities:
    bstack11l1lll1ll_opy_ = bstack111lllllll_opy_(desired_capabilities)
    bstack11l1lll1ll_opy_[bstack11l111_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨಕ")] = bstack11ll1111ll_opy_(CONFIG)
    bstack11l111l11_opy_ = bstack11l111111_opy_(bstack11l1lll1ll_opy_)
    if bstack11l111l11_opy_:
      bstack11lll1ll1_opy_ = update(bstack11l111l11_opy_, bstack11lll1ll1_opy_)
    desired_capabilities = None
  if options:
    bstack1lll111l11_opy_(options, bstack11lll1ll1_opy_)
  if not options:
    options = bstack1111l1111_opy_(bstack11lll1ll1_opy_)
  bstack11l11l1lll_opy_ = CONFIG.get(bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಖ"))[bstack1l1lll111l_opy_]
  if proxy and bstack1ll1l11ll_opy_() >= version.parse(bstack11l111_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪಗ")):
    options.proxy(proxy)
  if options and bstack1ll1l11ll_opy_() >= version.parse(bstack11l111_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪಘ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack1ll1l11ll_opy_() < version.parse(bstack11l111_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫಙ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack11lll1ll1_opy_)
  logger.info(bstack111lll1l1_opy_)
  bstack1111lll1l_opy_.end(EVENTS.bstack1111llllll_opy_.value, EVENTS.bstack1111llllll_opy_.value + bstack11l111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨಚ"), EVENTS.bstack1111llllll_opy_.value + bstack11l111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧಛ"), status=True, failure=None, test_name=bstack11lll111ll_opy_)
  if bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡳࡶࡴ࡬ࡩ࡭ࡧࠪಜ") in kwargs:
    del kwargs[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡴࡷࡵࡦࡪ࡮ࡨࠫಝ")]
  try:
    if bstack1ll1l11ll_opy_() >= version.parse(bstack11l111_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪಞ")):
      bstack1ll1l1lll1_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack1ll1l11ll_opy_() >= version.parse(bstack11l111_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪಟ")):
      bstack1ll1l1lll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1ll1l11ll_opy_() >= version.parse(bstack11l111_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬಠ")):
      bstack1ll1l1lll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1ll1l1lll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack111111l1l1_opy_:
    logger.error(bstack1lllllll1l_opy_.format(bstack11l111_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠬಡ"), str(bstack111111l1l1_opy_)))
    raise bstack111111l1l1_opy_
  if bstack1111l11l_opy_.bstack11l111lll1_opy_(CONFIG, bstack1l1lll111l_opy_) and bstack1111l11l_opy_.bstack1111ll111_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩಢ")][bstack11l111_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧಣ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack1111l11l_opy_.set_capabilities(bstack11lll1ll1_opy_, CONFIG)
  try:
    bstack1l111ll111_opy_ = bstack11l111_opy_ (u"ࠩࠪತ")
    if bstack1ll1l11ll_opy_() >= version.parse(bstack11l111_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࡤ࠴ࠫಥ")):
      if self.caps is not None:
        bstack1l111ll111_opy_ = self.caps.get(bstack11l111_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦದ"))
    else:
      if self.capabilities is not None:
        bstack1l111ll111_opy_ = self.capabilities.get(bstack11l111_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧಧ"))
    if bstack1l111ll111_opy_:
      bstack111ll111ll_opy_(bstack1l111ll111_opy_)
      if bstack1ll1l11ll_opy_() <= version.parse(bstack11l111_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ನ")):
        self.command_executor._url = bstack11l111_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣ಩") + bstack1111llll11_opy_ + bstack11l111_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧಪ")
      else:
        self.command_executor._url = bstack11l111_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦಫ") + bstack1l111ll111_opy_ + bstack11l111_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦಬ")
      logger.debug(bstack1ll11l11ll_opy_.format(bstack1l111ll111_opy_))
    else:
      logger.debug(bstack1l1ll111ll_opy_.format(bstack11l111_opy_ (u"ࠦࡔࡶࡴࡪ࡯ࡤࡰࠥࡎࡵࡣࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧಭ")))
  except Exception as e:
    logger.debug(bstack1l1ll111ll_opy_.format(e))
  if bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫಮ") in bstack1111l1l1l1_opy_:
    bstack1l111l1lll_opy_(bstack1l1l11llll_opy_, bstack11lll11l1_opy_)
  bstack11lll1lll1_opy_ = self.session_id
  if bstack11l111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ಯ") in bstack1111l1l1l1_opy_ or bstack11l111_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧರ") in bstack1111l1l1l1_opy_ or bstack11l111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧಱ") in bstack1111l1l1l1_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1lll11lll1_opy_ = getattr(threading.current_thread(), bstack11l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪಲ"), None)
  if bstack11l111_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪಳ") in bstack1111l1l1l1_opy_ or bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ಴") in bstack1111l1l1l1_opy_:
    bstack1lll111l_opy_.bstack11l1l1l11_opy_(self)
  if bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬವ") in bstack1111l1l1l1_opy_ and bstack1lll11lll1_opy_ and bstack1lll11lll1_opy_.get(bstack11l111_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ಶ"), bstack11l111_opy_ (u"ࠧࠨಷ")) == bstack11l111_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩಸ"):
    bstack1lll111l_opy_.bstack11l1l1l11_opy_(self)
  with bstack1l111l1l11_opy_:
    bstack11l11l111_opy_.append(self)
  if bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬಹ") in CONFIG and bstack11l111_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ಺") in CONFIG[bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ಻")][bstack1l1lll111l_opy_]:
    bstack11lll111ll_opy_ = CONFIG[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ಼")][bstack1l1lll111l_opy_][bstack11l111_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫಽ")]
  logger.debug(bstack11l111lll_opy_.format(bstack11lll1lll1_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack11ll1ll11l_opy_
    def bstack1l1l111ll_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1lllllllll_opy_
      if(bstack11l111_opy_ (u"ࠢࡪࡰࡧࡩࡽ࠴ࡪࡴࠤಾ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠨࢀࠪಿ")), bstack11l111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩೀ"), bstack11l111_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬು")), bstack11l111_opy_ (u"ࠫࡼ࠭ೂ")) as fp:
          fp.write(bstack11l111_opy_ (u"ࠧࠨೃ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11l111_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣೄ")))):
          with open(args[1], bstack11l111_opy_ (u"ࠧࡳࠩ೅")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11l111_opy_ (u"ࠨࡣࡶࡽࡳࡩࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡢࡲࡪࡽࡐࡢࡩࡨࠬࡨࡵ࡮ࡵࡧࡻࡸ࠱ࠦࡰࡢࡩࡨࠤࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠧೆ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack11111l1ll_opy_)
            if bstack11l111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ೇ") in CONFIG and str(CONFIG[bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧೈ")]).lower() != bstack11l111_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ೉"):
                bstack1l1ll11l1_opy_ = bstack11ll1ll11l_opy_()
                bstack11ll1l1ll_opy_ = bstack11l111_opy_ (u"ࠬ࠭ࠧࠋ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࠎࡨࡵ࡮ࡴࡶࠣࡦࡸࡺࡡࡤ࡭ࡢࡴࡦࡺࡨࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷ࡢࡁࠊࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠱࡞࠽ࠍࡧࡴࡴࡳࡵࠢࡳࡣ࡮ࡴࡤࡦࡺࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠸࡝࠼ࠌࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰ࡶࡰ࡮ࡩࡥࠩ࠲࠯ࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹ࠩ࠼ࠌࡦࡳࡳࡹࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢࠪ࠽ࠍ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡰࡦࡻ࡮ࡤࡪࠣࡁࠥࡧࡳࡺࡰࡦࠤ࠭ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷ࠮ࠦ࠽࠿ࠢࡾࡿࠏࠦࠠ࡭ࡧࡷࠤࡨࡧࡰࡴ࠽ࠍࠤࠥࡺࡲࡺࠢࡾࡿࠏࠦࠠࠡࠢࡦࡥࡵࡹࠠ࠾ࠢࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶ࠭ࡀࠐࠠࠡࡿࢀࠤࡨࡧࡴࡤࡪࠣࠬࡪࡾࠩࠡࡽࡾࠎࠥࠦࠠࠡࡥࡲࡲࡸࡵ࡬ࡦ࠰ࡨࡶࡷࡵࡲࠩࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠽ࠦ࠱ࠦࡥࡹࠫ࠾ࠎࠥࠦࡽࡾࠌࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡦࡽࡡࡪࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡧࡴࡴ࡮ࡦࡥࡷࠬࢀࢁࠊࠡࠢࠣࠤࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴ࠻ࠢࠪࡿࡨࡪࡰࡖࡴ࡯ࢁࠬࠦࠫࠡࡧࡱࡧࡴࡪࡥࡖࡔࡌࡇࡴࡳࡰࡰࡰࡨࡲࡹ࠮ࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡤࡣࡳࡷ࠮࠯ࠬࠋࠢࠣࠤࠥ࠴࠮࠯࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠋࠢࠣࢁࢂ࠯࠻ࠋࡿࢀ࠿ࠏ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯ࠋࠩࠪࠫೊ").format(bstack1l1ll11l1_opy_=bstack1l1ll11l1_opy_)
            lines.insert(1, bstack11ll1l1ll_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11l111_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣೋ")), bstack11l111_opy_ (u"ࠧࡸࠩೌ")) as bstack1l1l111lll_opy_:
              bstack1l1l111lll_opy_.writelines(lines)
        CONFIG[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍ್ࠪ")] = str(bstack1111l1l1l1_opy_) + str(__version__)
        bstack11l11l1l1l_opy_ = os.environ[bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ೎")]
        bstack111ll111l1_opy_ = bstack11ll111ll_opy_.bstack1l1llll1ll_opy_(CONFIG, bstack1111l1l1l1_opy_)
        CONFIG[bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭೏")] = bstack11l11l1l1l_opy_
        CONFIG[bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭೐")] = bstack111ll111l1_opy_
        bstack1l1lll111l_opy_ = 0 if bstack1l1l11llll_opy_ < 0 else bstack1l1l11llll_opy_
        try:
          if bstack1l11ll11l1_opy_ is True:
            bstack1l1lll111l_opy_ = int(multiprocessing.current_process().name)
          elif bstack1ll1l11lll_opy_ is True:
            bstack1l1lll111l_opy_ = int(threading.current_thread().name)
        except:
          bstack1l1lll111l_opy_ = 0
        CONFIG[bstack11l111_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧ೑")] = False
        CONFIG[bstack11l111_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ೒")] = True
        bstack11lll1ll1_opy_ = bstack11l111111_opy_(CONFIG, bstack1l1lll111l_opy_)
        logger.debug(bstack1l11ll11l_opy_.format(str(bstack11lll1ll1_opy_)))
        if CONFIG.get(bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ೓")):
          bstack11lll1llll_opy_(bstack11lll1ll1_opy_)
        if bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ೔") in CONFIG and bstack11l111_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧೕ") in CONFIG[bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ೖ")][bstack1l1lll111l_opy_]:
          bstack11lll111ll_opy_ = CONFIG[bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ೗")][bstack1l1lll111l_opy_][bstack11l111_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ೘")]
        args.append(os.path.join(os.path.expanduser(bstack11l111_opy_ (u"࠭ࡾࠨ೙")), bstack11l111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ೚"), bstack11l111_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪ೛")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack11lll1ll1_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11l111_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦ೜"))
      bstack1lllllllll_opy_ = True
      return bstack11ll11llll_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack11l1ll1l1_opy_(self,
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
    global bstack1l1l11llll_opy_
    global bstack11lll111ll_opy_
    global bstack1l11ll11l1_opy_
    global bstack1ll1l11lll_opy_
    global bstack1111l1l1l1_opy_
    CONFIG[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬೝ")] = str(bstack1111l1l1l1_opy_) + str(__version__)
    bstack11l11l1l1l_opy_ = os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩೞ")]
    bstack111ll111l1_opy_ = bstack11ll111ll_opy_.bstack1l1llll1ll_opy_(CONFIG, bstack1111l1l1l1_opy_)
    CONFIG[bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ೟")] = bstack11l11l1l1l_opy_
    CONFIG[bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨೠ")] = bstack111ll111l1_opy_
    bstack1l1lll111l_opy_ = 0 if bstack1l1l11llll_opy_ < 0 else bstack1l1l11llll_opy_
    try:
      if bstack1l11ll11l1_opy_ is True:
        bstack1l1lll111l_opy_ = int(multiprocessing.current_process().name)
      elif bstack1ll1l11lll_opy_ is True:
        bstack1l1lll111l_opy_ = int(threading.current_thread().name)
    except:
      bstack1l1lll111l_opy_ = 0
    CONFIG[bstack11l111_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨೡ")] = True
    bstack11lll1ll1_opy_ = bstack11l111111_opy_(CONFIG, bstack1l1lll111l_opy_)
    logger.debug(bstack1l11ll11l_opy_.format(str(bstack11lll1ll1_opy_)))
    if CONFIG.get(bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬೢ")):
      bstack11lll1llll_opy_(bstack11lll1ll1_opy_)
    if bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೣ") in CONFIG and bstack11l111_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ೤") in CONFIG[bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ೥")][bstack1l1lll111l_opy_]:
      bstack11lll111ll_opy_ = CONFIG[bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ೦")][bstack1l1lll111l_opy_][bstack11l111_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ೧")]
    import urllib
    import json
    if bstack11l111_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ೨") in CONFIG and str(CONFIG[bstack11l111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ೩")]).lower() != bstack11l111_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ೪"):
        bstack1111ll11l_opy_ = bstack11ll1ll11l_opy_()
        bstack1l1ll11l1_opy_ = bstack1111ll11l_opy_ + urllib.parse.quote(json.dumps(bstack11lll1ll1_opy_))
    else:
        bstack1l1ll11l1_opy_ = bstack11l111_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬ೫") + urllib.parse.quote(json.dumps(bstack11lll1ll1_opy_))
    browser = self.connect(bstack1l1ll11l1_opy_)
    return browser
except Exception as e:
    pass
def bstack111l1l1l1l_opy_():
    global bstack1lllllllll_opy_
    global bstack1111l1l1l1_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1l11l1lll1_opy_
        global bstack11111l11_opy_
        if not bstack11l1111l11_opy_:
          global bstack11l1l111l_opy_
          if not bstack11l1l111l_opy_:
            from bstack_utils.helper import bstack1111ll1l1l_opy_, bstack1l11ll1lll_opy_, bstack1l1ll1l1l_opy_
            bstack11l1l111l_opy_ = bstack1111ll1l1l_opy_()
            bstack1l11ll1lll_opy_(bstack1111l1l1l1_opy_)
            bstack111ll111l1_opy_ = bstack11ll111ll_opy_.bstack1l1llll1ll_opy_(CONFIG, bstack1111l1l1l1_opy_)
            bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"ࠦࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡒࡕࡓࡉ࡛ࡃࡕࡡࡐࡅࡕࠨ೬"), bstack111ll111l1_opy_)
          BrowserType.connect = bstack1l11l1lll1_opy_
          return
        BrowserType.launch = bstack11l1ll1l1_opy_
        bstack1lllllllll_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1l1l111ll_opy_
      bstack1lllllllll_opy_ = True
    except Exception as e:
      pass
def bstack11l11ll1l_opy_(context, bstack1l1ll11111_opy_):
  try:
    context.page.evaluate(bstack11l111_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨ೭"), bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪ೮")+ json.dumps(bstack1l1ll11111_opy_) + bstack11l111_opy_ (u"ࠢࡾࡿࠥ೯"))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࡀࠠࡼࡿࠥ೰").format(str(e), traceback.format_exc()))
def bstack11ll11111_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11l111_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥೱ"), bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨೲ") + json.dumps(message) + bstack11l111_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧೳ") + json.dumps(level) + bstack11l111_opy_ (u"ࠬࢃࡽࠨ೴"))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾ࠼ࠣࡿࢂࠨ೵").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1ll1l1ll11_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack111l1lll1l_opy_(self, url):
  global bstack1l111l1l1_opy_
  try:
    bstack1ll1ll1l1l_opy_(url)
  except Exception as err:
    logger.debug(bstack11111ll11_opy_.format(str(err)))
  try:
    bstack1l111l1l1_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1l11l11l1_opy_):
        bstack1ll1ll1l1l_opy_(url, True)
    except Exception as err:
      logger.debug(bstack11111ll11_opy_.format(str(err)))
    raise e
def bstack11l11ll1l1_opy_(self):
  global bstack1111l111l_opy_
  bstack1111l111l_opy_ = self
  return
def bstack1llll11l1l_opy_(self):
  global bstack1lll1l1ll1_opy_
  bstack1lll1l1ll1_opy_ = self
  return
def bstack111l111l1_opy_(test_name, bstack1ll1llll1l_opy_):
  global CONFIG
  if percy.bstack1l1lllll1l_opy_() == bstack11l111_opy_ (u"ࠢࡵࡴࡸࡩࠧ೶"):
    bstack1llll1l1l1_opy_ = os.path.relpath(bstack1ll1llll1l_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1llll1l1l1_opy_)
    bstack11l111l1l_opy_ = suite_name + bstack11l111_opy_ (u"ࠣ࠯ࠥ೷") + test_name
    threading.current_thread().percySessionName = bstack11l111l1l_opy_
def bstack1l11l11ll1_opy_(self, test, *args, **kwargs):
  global bstack1ll1ll111l_opy_
  test_name = None
  bstack1ll1llll1l_opy_ = None
  if test:
    test_name = str(test.name)
    bstack1ll1llll1l_opy_ = str(test.source)
  bstack111l111l1_opy_(test_name, bstack1ll1llll1l_opy_)
  bstack1ll1ll111l_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack111111lll1_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack111l1l1ll1_opy_(driver, bstack11l111l1l_opy_):
  if not bstack1ll111lll1_opy_ and bstack11l111l1l_opy_:
      bstack1ll1111111_opy_ = {
          bstack11l111_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩ೸"): bstack11l111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ೹"),
          bstack11l111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ೺"): {
              bstack11l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ೻"): bstack11l111l1l_opy_
          }
      }
      bstack1l1l1l1111_opy_ = bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ೼").format(json.dumps(bstack1ll1111111_opy_))
      driver.execute_script(bstack1l1l1l1111_opy_)
  if bstack1ll111l1l_opy_:
      bstack1l1l11ll1_opy_ = {
          bstack11l111_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧ೽"): bstack11l111_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪ೾"),
          bstack11l111_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ೿"): {
              bstack11l111_opy_ (u"ࠪࡨࡦࡺࡡࠨഀ"): bstack11l111l1l_opy_ + bstack11l111_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭ഁ"),
              bstack11l111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫം"): bstack11l111_opy_ (u"࠭ࡩ࡯ࡨࡲࠫഃ")
          }
      }
      if bstack1ll111l1l_opy_.status == bstack11l111_opy_ (u"ࠧࡑࡃࡖࡗࠬഄ"):
          bstack11llll11l_opy_ = bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭അ").format(json.dumps(bstack1l1l11ll1_opy_))
          driver.execute_script(bstack11llll11l_opy_)
          bstack11ll11lll1_opy_(driver, bstack11l111_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩആ"))
      elif bstack1ll111l1l_opy_.status == bstack11l111_opy_ (u"ࠪࡊࡆࡏࡌࠨഇ"):
          reason = bstack11l111_opy_ (u"ࠦࠧഈ")
          bstack1ll1l1ll1l_opy_ = bstack11l111l1l_opy_ + bstack11l111_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩ࠭ഉ")
          if bstack1ll111l1l_opy_.message:
              reason = str(bstack1ll111l1l_opy_.message)
              bstack1ll1l1ll1l_opy_ = bstack1ll1l1ll1l_opy_ + bstack11l111_opy_ (u"࠭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥ࠭ഊ") + reason
          bstack1l1l11ll1_opy_[bstack11l111_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪഋ")] = {
              bstack11l111_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧഌ"): bstack11l111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ഍"),
              bstack11l111_opy_ (u"ࠪࡨࡦࡺࡡࠨഎ"): bstack1ll1l1ll1l_opy_
          }
          bstack11llll11l_opy_ = bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩഏ").format(json.dumps(bstack1l1l11ll1_opy_))
          driver.execute_script(bstack11llll11l_opy_)
          bstack11ll11lll1_opy_(driver, bstack11l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬഐ"), reason)
          bstack11l1llll11_opy_(reason, str(bstack1ll111l1l_opy_), str(bstack1l1l11llll_opy_), logger)
@measure(event_name=EVENTS.bstack1111ll11l1_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack11lll111l_opy_(driver, test):
  if percy.bstack1l1lllll1l_opy_() == bstack11l111_opy_ (u"ࠨࡴࡳࡷࡨࠦ഑") and percy.bstack1l1l1l111l_opy_() == bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤഒ"):
      bstack11lll1l1ll_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠨࡲࡨࡶࡨࡿࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫഓ"), None)
      bstack1l1lll1ll_opy_(driver, bstack11lll1l1ll_opy_, test)
  if (bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ഔ"), None) and
      bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩക"), None)) or (
      bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫഖ"), None) and
      bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧഗ"), None)):
      logger.info(bstack11l111_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠤࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡩࡴࠢࡸࡲࡩ࡫ࡲࡸࡣࡼ࠲ࠥࠨഘ"))
      bstack1111l11l_opy_.bstack1lllllll1_opy_(driver, name=test.name, path=test.source)
def bstack1ll11l1l1l_opy_(test, bstack11l111l1l_opy_):
    try:
      bstack1l1ll1ll1_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack11l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬങ")] = bstack11l111l1l_opy_
      if bstack1ll111l1l_opy_:
        if bstack1ll111l1l_opy_.status == bstack11l111_opy_ (u"ࠨࡒࡄࡗࡘ࠭ച"):
          data[bstack11l111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩഛ")] = bstack11l111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪജ")
        elif bstack1ll111l1l_opy_.status == bstack11l111_opy_ (u"ࠫࡋࡇࡉࡍࠩഝ"):
          data[bstack11l111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬഞ")] = bstack11l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ട")
          if bstack1ll111l1l_opy_.message:
            data[bstack11l111_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧഠ")] = str(bstack1ll111l1l_opy_.message)
      user = CONFIG[bstack11l111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪഡ")]
      key = CONFIG[bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬഢ")]
      host = bstack111111ll11_opy_(cli.config, [bstack11l111_opy_ (u"ࠥࡥࡵ࡯ࡳࠣണ"), bstack11l111_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨത"), bstack11l111_opy_ (u"ࠧࡧࡰࡪࠤഥ")], bstack11l111_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠢദ"))
      url = bstack11l111_opy_ (u"ࠧࡼࡿ࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠯ࡼࡿ࠱࡮ࡸࡵ࡮ࠨധ").format(host, bstack11lll1lll1_opy_)
      headers = {
        bstack11l111_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧന"): bstack11l111_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬഩ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡷࡳࡨࡦࡺࡥࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡶࡤࡸࡺࡹࠢപ"), datetime.datetime.now() - bstack1l1ll1ll1_opy_)
    except Exception as e:
      logger.error(bstack1l1ll1111l_opy_.format(str(e)))
def bstack1111lll111_opy_(test, bstack11l111l1l_opy_):
  global CONFIG
  global bstack1lll1l1ll1_opy_
  global bstack1111l111l_opy_
  global bstack11lll1lll1_opy_
  global bstack1ll111l1l_opy_
  global bstack11lll111ll_opy_
  global bstack11111ll1l_opy_
  global bstack1ll1llll11_opy_
  global bstack1l1l111l1_opy_
  global bstack1ll1lll111_opy_
  global bstack11l11l111_opy_
  global bstack11l11l1lll_opy_
  global bstack11ll1l11l_opy_
  try:
    if not bstack11lll1lll1_opy_:
      with bstack11ll1l11l_opy_:
        bstack1lll11l1l1_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠫࢃ࠭ഫ")), bstack11l111_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬബ"), bstack11l111_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨഭ"))
        if os.path.exists(bstack1lll11l1l1_opy_):
          with open(bstack1lll11l1l1_opy_, bstack11l111_opy_ (u"ࠧࡳࠩമ")) as f:
            content = f.read().strip()
            if content:
              bstack1l1l1111l1_opy_ = json.loads(bstack11l111_opy_ (u"ࠣࡽࠥയ") + content + bstack11l111_opy_ (u"ࠩࠥࡼࠧࡀࠠࠣࡻࠥࠫര") + bstack11l111_opy_ (u"ࠥࢁࠧറ"))
              bstack11lll1lll1_opy_ = bstack1l1l1111l1_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡶࡪࡧࡤࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡏࡄࡴࠢࡩ࡭ࡱ࡫࠺ࠡࠩല") + str(e))
  if bstack11l11l111_opy_:
    with bstack1l111l1l11_opy_:
      bstack1lll11llll_opy_ = bstack11l11l111_opy_.copy()
    for driver in bstack1lll11llll_opy_:
      if bstack11lll1lll1_opy_ == driver.session_id:
        if test:
          bstack11lll111l_opy_(driver, test)
        bstack111l1l1ll1_opy_(driver, bstack11l111l1l_opy_)
  elif bstack11lll1lll1_opy_:
    bstack1ll11l1l1l_opy_(test, bstack11l111l1l_opy_)
  if bstack1lll1l1ll1_opy_:
    bstack1ll1llll11_opy_(bstack1lll1l1ll1_opy_)
  if bstack1111l111l_opy_:
    bstack1l1l111l1_opy_(bstack1111l111l_opy_)
  if bstack11llll11l1_opy_:
    bstack1ll1lll111_opy_()
def bstack1l1ll11lll_opy_(self, test, *args, **kwargs):
  bstack11l111l1l_opy_ = None
  if test:
    bstack11l111l1l_opy_ = str(test.name)
  bstack1111lll111_opy_(test, bstack11l111l1l_opy_)
  bstack11111ll1l_opy_(self, test, *args, **kwargs)
def bstack1llll11l11_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1l111llll1_opy_
  global CONFIG
  global bstack11l11l111_opy_
  global bstack11lll1lll1_opy_
  global bstack11ll1l11l_opy_
  bstack111111l11_opy_ = None
  try:
    if bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫള"), None) or bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨഴ"), None):
      try:
        if not bstack11lll1lll1_opy_:
          bstack1lll11l1l1_opy_ = os.path.join(os.path.expanduser(bstack11l111_opy_ (u"ࠧࡿࠩവ")), bstack11l111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨശ"), bstack11l111_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫഷ"))
          with bstack11ll1l11l_opy_:
            if os.path.exists(bstack1lll11l1l1_opy_):
              with open(bstack1lll11l1l1_opy_, bstack11l111_opy_ (u"ࠪࡶࠬസ")) as f:
                content = f.read().strip()
                if content:
                  bstack1l1l1111l1_opy_ = json.loads(bstack11l111_opy_ (u"ࠦࢀࠨഹ") + content + bstack11l111_opy_ (u"ࠬࠨࡸࠣ࠼ࠣࠦࡾࠨࠧഺ") + bstack11l111_opy_ (u"ࠨࡽ഻ࠣ"))
                  bstack11lll1lll1_opy_ = bstack1l1l1111l1_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡋࡇࡷࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾഼ࠥ࠭") + str(e))
      if bstack11l11l111_opy_:
        with bstack1l111l1l11_opy_:
          bstack1lll11llll_opy_ = bstack11l11l111_opy_.copy()
        for driver in bstack1lll11llll_opy_:
          if bstack11lll1lll1_opy_ == driver.session_id:
            bstack111111l11_opy_ = driver
    bstack111l11ll1_opy_ = bstack1111l11l_opy_.bstack1llll111ll_opy_(test.tags)
    if bstack111111l11_opy_:
      threading.current_thread().isA11yTest = bstack1111l11l_opy_.bstack111llll11_opy_(bstack111111l11_opy_, bstack111l11ll1_opy_)
      threading.current_thread().isAppA11yTest = bstack1111l11l_opy_.bstack111llll11_opy_(bstack111111l11_opy_, bstack111l11ll1_opy_)
    else:
      threading.current_thread().isA11yTest = bstack111l11ll1_opy_
      threading.current_thread().isAppA11yTest = bstack111l11ll1_opy_
  except:
    pass
  bstack1l111llll1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1ll111l1l_opy_
  try:
    bstack1ll111l1l_opy_ = self._test
  except:
    bstack1ll111l1l_opy_ = self.test
def bstack111lllll11_opy_():
  global bstack111111ll1l_opy_
  try:
    if os.path.exists(bstack111111ll1l_opy_):
      os.remove(bstack111111ll1l_opy_)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫഽ") + str(e))
def bstack1ll1lll1l1_opy_():
  global bstack111111ll1l_opy_
  bstack1lllll1l1l_opy_ = {}
  lock_file = bstack111111ll1l_opy_ + bstack11l111_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨാ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l111_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭ി"))
    try:
      if not os.path.isfile(bstack111111ll1l_opy_):
        with open(bstack111111ll1l_opy_, bstack11l111_opy_ (u"ࠫࡼ࠭ീ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack111111ll1l_opy_):
        with open(bstack111111ll1l_opy_, bstack11l111_opy_ (u"ࠬࡸࠧു")) as f:
          content = f.read().strip()
          if content:
            bstack1lllll1l1l_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨൂ") + str(e))
    return bstack1lllll1l1l_opy_
  try:
    os.makedirs(os.path.dirname(bstack111111ll1l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack111111ll1l_opy_):
        with open(bstack111111ll1l_opy_, bstack11l111_opy_ (u"ࠧࡸࠩൃ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack111111ll1l_opy_):
        with open(bstack111111ll1l_opy_, bstack11l111_opy_ (u"ࠨࡴࠪൄ")) as f:
          content = f.read().strip()
          if content:
            bstack1lllll1l1l_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫ൅") + str(e))
  finally:
    return bstack1lllll1l1l_opy_
def bstack1l111l1lll_opy_(platform_index, item_index):
  global bstack111111ll1l_opy_
  lock_file = bstack111111ll1l_opy_ + bstack11l111_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩെ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l111_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧേ"))
    try:
      bstack1lllll1l1l_opy_ = {}
      if os.path.exists(bstack111111ll1l_opy_):
        with open(bstack111111ll1l_opy_, bstack11l111_opy_ (u"ࠬࡸࠧൈ")) as f:
          content = f.read().strip()
          if content:
            bstack1lllll1l1l_opy_ = json.loads(content)
      bstack1lllll1l1l_opy_[item_index] = platform_index
      with open(bstack111111ll1l_opy_, bstack11l111_opy_ (u"ࠨࡷࠣ൉")) as outfile:
        json.dump(bstack1lllll1l1l_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡺࡶ࡮ࡺࡩ࡯ࡩࠣࡸࡴࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬൊ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack111111ll1l_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack1lllll1l1l_opy_ = {}
      if os.path.exists(bstack111111ll1l_opy_):
        with open(bstack111111ll1l_opy_, bstack11l111_opy_ (u"ࠨࡴࠪോ")) as f:
          content = f.read().strip()
          if content:
            bstack1lllll1l1l_opy_ = json.loads(content)
      bstack1lllll1l1l_opy_[item_index] = platform_index
      with open(bstack111111ll1l_opy_, bstack11l111_opy_ (u"ࠤࡺࠦൌ")) as outfile:
        json.dump(bstack1lllll1l1l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡽࡲࡪࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨ്") + str(e))
def bstack11l111ll11_opy_(bstack1lll1lll11_opy_):
  global CONFIG
  bstack1l1l1111ll_opy_ = bstack11l111_opy_ (u"ࠫࠬൎ")
  if not bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ൏") in CONFIG:
    logger.info(bstack11l111_opy_ (u"࠭ࡎࡰࠢࡳࡰࡦࡺࡦࡰࡴࡰࡷࠥࡶࡡࡴࡵࡨࡨࠥࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡲࡪࡸࡡࡵࡧࠣࡶࡪࡶ࡯ࡳࡶࠣࡪࡴࡸࠠࡓࡱࡥࡳࡹࠦࡲࡶࡰࠪ൐"))
  try:
    platform = CONFIG[bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ൑")][bstack1lll1lll11_opy_]
    if bstack11l111_opy_ (u"ࠨࡱࡶࠫ൒") in platform:
      bstack1l1l1111ll_opy_ += str(platform[bstack11l111_opy_ (u"ࠩࡲࡷࠬ൓")]) + bstack11l111_opy_ (u"ࠪ࠰ࠥ࠭ൔ")
    if bstack11l111_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧൕ") in platform:
      bstack1l1l1111ll_opy_ += str(platform[bstack11l111_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨൖ")]) + bstack11l111_opy_ (u"࠭ࠬࠡࠩൗ")
    if bstack11l111_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ൘") in platform:
      bstack1l1l1111ll_opy_ += str(platform[bstack11l111_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ൙")]) + bstack11l111_opy_ (u"ࠩ࠯ࠤࠬ൚")
    if bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ൛") in platform:
      bstack1l1l1111ll_opy_ += str(platform[bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭൜")]) + bstack11l111_opy_ (u"ࠬ࠲ࠠࠨ൝")
    if bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ൞") in platform:
      bstack1l1l1111ll_opy_ += str(platform[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬൟ")]) + bstack11l111_opy_ (u"ࠨ࠮ࠣࠫൠ")
    if bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪൡ") in platform:
      bstack1l1l1111ll_opy_ += str(platform[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫൢ")]) + bstack11l111_opy_ (u"ࠫ࠱ࠦࠧൣ")
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"࡙ࠬ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡺࡲࡪࡰࡪࠤ࡫ࡵࡲࠡࡴࡨࡴࡴࡸࡴࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡲࡲࠬ൤") + str(e))
  finally:
    if bstack1l1l1111ll_opy_[len(bstack1l1l1111ll_opy_) - 2:] == bstack11l111_opy_ (u"࠭ࠬࠡࠩ൥"):
      bstack1l1l1111ll_opy_ = bstack1l1l1111ll_opy_[:-2]
    return bstack1l1l1111ll_opy_
def bstack111ll1l1l_opy_(path, bstack1l1l1111ll_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack11111l1111_opy_ = ET.parse(path)
    bstack111l111ll_opy_ = bstack11111l1111_opy_.getroot()
    bstack11l1l1111l_opy_ = None
    for suite in bstack111l111ll_opy_.iter(bstack11l111_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭൦")):
      if bstack11l111_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ൧") in suite.attrib:
        suite.attrib[bstack11l111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ൨")] += bstack11l111_opy_ (u"ࠪࠤࠬ൩") + bstack1l1l1111ll_opy_
        bstack11l1l1111l_opy_ = suite
    bstack11llll1lll_opy_ = None
    for robot in bstack111l111ll_opy_.iter(bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ൪")):
      bstack11llll1lll_opy_ = robot
    bstack111111ll1_opy_ = len(bstack11llll1lll_opy_.findall(bstack11l111_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫ൫")))
    if bstack111111ll1_opy_ == 1:
      bstack11llll1lll_opy_.remove(bstack11llll1lll_opy_.findall(bstack11l111_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൬"))[0])
      bstack1111l1ll1l_opy_ = ET.Element(bstack11l111_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭൭"), attrib={bstack11l111_opy_ (u"ࠨࡰࡤࡱࡪ࠭൮"): bstack11l111_opy_ (u"ࠩࡖࡹ࡮ࡺࡥࡴࠩ൯"), bstack11l111_opy_ (u"ࠪ࡭ࡩ࠭൰"): bstack11l111_opy_ (u"ࠫࡸ࠶ࠧ൱")})
      bstack11llll1lll_opy_.insert(1, bstack1111l1ll1l_opy_)
      bstack11ll1l1l11_opy_ = None
      for suite in bstack11llll1lll_opy_.iter(bstack11l111_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫ൲")):
        bstack11ll1l1l11_opy_ = suite
      bstack11ll1l1l11_opy_.append(bstack11l1l1111l_opy_)
      bstack1l1ll1lll_opy_ = None
      for status in bstack11l1l1111l_opy_.iter(bstack11l111_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭൳")):
        bstack1l1ll1lll_opy_ = status
      bstack11ll1l1l11_opy_.append(bstack1l1ll1lll_opy_)
    bstack11111l1111_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠬ൴") + str(e))
def bstack1l1llll11l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1l11l1ll1_opy_
  global CONFIG
  if bstack11l111_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬ࠧ൵") in options:
    del options[bstack11l111_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨ൶")]
  json_data = bstack1ll1lll1l1_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack11l111_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࡡࡵࡩࡸࡻ࡬ࡵࡵࠪ൷"), str(item_id), bstack11l111_opy_ (u"ࠫࡴࡻࡴࡱࡷࡷ࠲ࡽࡳ࡬ࠨ൸"))
    bstack111ll1l1l_opy_(path, bstack11l111ll11_opy_(json_data[item_id]))
  bstack111lllll11_opy_()
  return bstack1l11l1ll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1l11llllll_opy_(self, ff_profile_dir):
  global bstack1l11ll1ll_opy_
  if not ff_profile_dir:
    return None
  return bstack1l11ll1ll_opy_(self, ff_profile_dir)
def bstack1ll11llll1_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack111l1lll11_opy_
  bstack11ll111ll1_opy_ = []
  if bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ൹") in CONFIG:
    bstack11ll111ll1_opy_ = CONFIG[bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩൺ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11l111_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࠣൻ")],
      pabot_args[bstack11l111_opy_ (u"ࠣࡸࡨࡶࡧࡵࡳࡦࠤർ")],
      argfile,
      pabot_args.get(bstack11l111_opy_ (u"ࠤ࡫࡭ࡻ࡫ࠢൽ")),
      pabot_args[bstack11l111_opy_ (u"ࠥࡴࡷࡵࡣࡦࡵࡶࡩࡸࠨൾ")],
      platform[0],
      bstack111l1lll11_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11l111_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹ࡬ࡩ࡭ࡧࡶࠦൿ")] or [(bstack11l111_opy_ (u"ࠧࠨ඀"), None)]
    for platform in enumerate(bstack11ll111ll1_opy_)
  ]
def bstack11lll1ll1l_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack11lllll11_opy_=bstack11l111_opy_ (u"࠭ࠧඁ")):
  global bstack1l1l11lll1_opy_
  self.platform_index = platform_index
  self.bstack1ll1l111l_opy_ = bstack11lllll11_opy_
  bstack1l1l11lll1_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack11111l11l_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1111111ll_opy_
  global bstack1l1l1l1lll_opy_
  bstack111lll111l_opy_ = copy.deepcopy(item)
  if not bstack11l111_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩං") in item.options:
    bstack111lll111l_opy_.options[bstack11l111_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪඃ")] = []
  bstack1l1lll11l1_opy_ = bstack111lll111l_opy_.options[bstack11l111_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ඄")].copy()
  for v in bstack111lll111l_opy_.options[bstack11l111_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬඅ")]:
    if bstack11l111_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚ࠪආ") in v:
      bstack1l1lll11l1_opy_.remove(v)
    if bstack11l111_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬඇ") in v:
      bstack1l1lll11l1_opy_.remove(v)
    if bstack11l111_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡊࡅࡇࡎࡒࡇࡆࡒࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪඈ") in v:
      bstack1l1lll11l1_opy_.remove(v)
  bstack1l1lll11l1_opy_.insert(0, bstack11l111_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝ࡀࡻࡾࠩඉ").format(bstack111lll111l_opy_.platform_index))
  bstack1l1lll11l1_opy_.insert(0, bstack11l111_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖ࠿ࢁࡽࠨඊ").format(bstack111lll111l_opy_.bstack1ll1l111l_opy_))
  bstack111lll111l_opy_.options[bstack11l111_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫඋ")] = bstack1l1lll11l1_opy_
  if bstack1l1l1l1lll_opy_:
    bstack111lll111l_opy_.options[bstack11l111_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬඌ")].insert(0, bstack11l111_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖ࠾ࢀࢃࠧඍ").format(bstack1l1l1l1lll_opy_))
  return bstack1111111ll_opy_(caller_id, datasources, is_last, bstack111lll111l_opy_, outs_dir)
def bstack1ll1ll1lll_opy_(command, item_index):
  try:
    if bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ඎ")):
      os.environ[bstack11l111_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧඏ")] = json.dumps(CONFIG[bstack11l111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪඐ")][item_index % bstack111l11llll_opy_])
    global bstack1l1l1l1lll_opy_
    if bstack1l1l1l1lll_opy_:
      command[0] = command[0].replace(bstack11l111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧඑ"), bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡵࡧ࡯ࠥࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱࠦ࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠥ࠭ඒ") + str(
        item_index) + bstack11l111_opy_ (u"ࠪࠤࠬඓ") + bstack1l1l1l1lll_opy_, 1)
    else:
      command[0] = command[0].replace(bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪඔ"),
                                      bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡸࡪ࡫ࠡࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠢ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠡࠩඕ") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡳ࡯ࡥ࡫ࡩࡽ࡮ࡴࡧࠡࡥࡲࡱࡲࡧ࡮ࡥࠢࡩࡳࡷࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯࠼ࠣࡿࢂ࠭ඖ").format(str(e)))
def bstack1ll11ll1l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack11ll1lllll_opy_
  try:
    bstack1ll1ll1lll_opy_(command, item_index)
    return bstack11ll1lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲ࠿ࠦࡻࡾࠩ඗").format(str(e)))
    raise e
def bstack111l1llll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack11ll1lllll_opy_
  try:
    bstack1ll1ll1lll_opy_(command, item_index)
    return bstack11ll1lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࠦ࠲࠯࠳࠶࠾ࠥࢁࡽࠨ඘").format(str(e)))
    try:
      return bstack11ll1lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack11l111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣ࠶࠳࠷࠳ࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧ඙").format(str(e2)))
      raise e
def bstack1ll11l1ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack11ll1lllll_opy_
  try:
    bstack1ll1ll1lll_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack11ll1lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠴࠱࠵࠺ࡀࠠࡼࡿࠪක").format(str(e)))
    try:
      return bstack11ll1lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack11l111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࠸࠮࠲࠷ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩඛ").format(str(e2)))
      raise e
def _1l11lllll_opy_(bstack1lll11l11l_opy_, item_index, process_timeout, sleep_before_start, bstack1l1llll111_opy_):
  bstack1ll1ll1lll_opy_(bstack1lll11l11l_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack1ll1lllll1_opy_(command, bstack1111ll111l_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11ll1lllll_opy_
  try:
    bstack1ll1ll1lll_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack11ll1lllll_opy_(command, bstack1111ll111l_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰࠣ࠹࠳࠶࠺ࠡࡽࢀࠫග").format(str(e)))
    try:
      return bstack11ll1lllll_opy_(command, bstack1111ll111l_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11l111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࡿࢂ࠭ඝ").format(str(e2)))
      raise e
def bstack1l111l111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11ll1lllll_opy_
  try:
    process_timeout = _1l11lllll_opy_(command, item_index, process_timeout, sleep_before_start, bstack11l111_opy_ (u"ࠧ࠵࠰࠵ࠫඞ"))
    return bstack11ll1lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࠦ࠴࠯࠴࠽ࠤࢀࢃࠧඟ").format(str(e)))
    try:
      return bstack11ll1lllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11l111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩච").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack1l11l1l1l1_opy_(self, runner, quiet=False, capture=True):
  global bstack11l111111l_opy_
  bstack1111l11111_opy_ = bstack11l111111l_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11l111_opy_ (u"ࠪࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࡥࡡࡳࡴࠪඡ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11l111_opy_ (u"ࠫࡪࡾࡣࡠࡶࡵࡥࡨ࡫ࡢࡢࡥ࡮ࡣࡦࡸࡲࠨජ")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1111l11111_opy_
def bstack11l11lll1l_opy_(runner, hook_name, context, element, bstack11llllll1_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1llll11ll1_opy_.bstack11l111l1_opy_(hook_name, element)
    bstack11llllll1_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1llll11ll1_opy_.bstack111llll1_opy_(element)
      if hook_name not in [bstack11l111_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠩඣ"), bstack11l111_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩඤ")] and args and hasattr(args[0], bstack11l111_opy_ (u"ࠧࡦࡴࡵࡳࡷࡥ࡭ࡦࡵࡶࡥ࡬࡫ࠧඥ")):
        args[0].error_message = bstack11l111_opy_ (u"ࠨࠩඦ")
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡮ࡡ࡯ࡦ࡯ࡩࠥ࡮࡯ࡰ࡭ࡶࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫࠺ࠡࡽࢀࠫට").format(str(e)))
@measure(event_name=EVENTS.bstack1l1ll1111_opy_, stage=STAGE.bstack1l11lll11_opy_, hook_type=bstack11l111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡄࡰࡱࠨඨ"), bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack1111l11l1_opy_(runner, name, context, bstack11llllll1_opy_, *args):
    if runner.hooks.get(bstack11l111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣඩ")).__name__ != bstack11l111_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࡡࡧࡩ࡫ࡧࡵ࡭ࡶࡢ࡬ࡴࡵ࡫ࠣඪ"):
      bstack11l11lll1l_opy_(runner, name, context, runner, bstack11llllll1_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack111l1l11l_opy_(bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬණ")) else context.browser
      runner.driver_initialised = bstack11l111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦඬ")
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡩࠥࡧࡴࡵࡴ࡬ࡦࡺࡺࡥ࠻ࠢࡾࢁࠬත").format(str(e)))
def bstack11l1l11ll1_opy_(runner, name, context, bstack11llllll1_opy_, *args):
    bstack11l11lll1l_opy_(runner, name, context, context.feature, bstack11llllll1_opy_, *args)
    try:
      if not bstack1ll111lll1_opy_:
        bstack111111l11_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1l11l_opy_(bstack11l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨථ")) else context.browser
        if is_driver_active(bstack111111l11_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack11l111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦද")
          bstack1l1ll11111_opy_ = str(runner.feature.name)
          bstack11l11ll1l_opy_(context, bstack1l1ll11111_opy_)
          bstack111111l11_opy_.execute_script(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩධ") + json.dumps(bstack1l1ll11111_opy_) + bstack11l111_opy_ (u"ࠬࢃࡽࠨන"))
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭඲").format(str(e)))
def bstack111l1ll1ll_opy_(runner, name, context, bstack11llllll1_opy_, *args):
    if hasattr(context, bstack11l111_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩඳ")):
        bstack1llll11ll1_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack11l111_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪප")) else context.feature
    bstack11l11lll1l_opy_(runner, name, context, target, bstack11llllll1_opy_, *args)
@measure(event_name=EVENTS.bstack1l1111lll1_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack11l11lll1_opy_(runner, name, context, bstack11llllll1_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1llll11ll1_opy_.start_test(context)
    bstack11l11lll1l_opy_(runner, name, context, context.scenario, bstack11llllll1_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack11l11l11ll_opy_.bstack111l11l1ll_opy_(context, *args)
    try:
      bstack111111l11_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨඵ"), context.browser)
      if is_driver_active(bstack111111l11_opy_):
        bstack1lll111l_opy_.bstack11l1l1l11_opy_(bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩබ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨභ")
        if (not bstack1ll111lll1_opy_):
          scenario_name = args[0].name
          feature_name = bstack1l1ll11111_opy_ = str(runner.feature.name)
          bstack1l1ll11111_opy_ = feature_name + bstack11l111_opy_ (u"ࠬࠦ࠭ࠡࠩම") + scenario_name
          if runner.driver_initialised == bstack11l111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣඹ"):
            bstack11l11ll1l_opy_(context, bstack1l1ll11111_opy_)
            bstack111111l11_opy_.execute_script(bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬය") + json.dumps(bstack1l1ll11111_opy_) + bstack11l111_opy_ (u"ࠨࡿࢀࠫර"))
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡ࡫ࡱࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡩࡥ࡯ࡣࡵ࡭ࡴࡀࠠࡼࡿࠪ඼").format(str(e)))
@measure(event_name=EVENTS.bstack1l1ll1111_opy_, stage=STAGE.bstack1l11lll11_opy_, hook_type=bstack11l111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡖࡸࡪࡶࠢල"), bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack1ll1l11l11_opy_(runner, name, context, bstack11llllll1_opy_, *args):
    bstack11l11lll1l_opy_(runner, name, context, args[0], bstack11llllll1_opy_, *args)
    try:
      bstack111111l11_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1l11l_opy_(bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ඾")) else context.browser
      if is_driver_active(bstack111111l11_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l111_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥ඿")
        bstack1llll11ll1_opy_.bstack11l1l1l1_opy_(args[0])
        if runner.driver_initialised == bstack11l111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦව"):
          feature_name = bstack1l1ll11111_opy_ = str(runner.feature.name)
          bstack1l1ll11111_opy_ = feature_name + bstack11l111_opy_ (u"ࠧࠡ࠯ࠣࠫශ") + context.scenario.name
          bstack111111l11_opy_.execute_script(bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭ෂ") + json.dumps(bstack1l1ll11111_opy_) + bstack11l111_opy_ (u"ࠩࢀࢁࠬස"))
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡴࡦࡲ࠽ࠤࢀࢃࠧහ").format(str(e)))
@measure(event_name=EVENTS.bstack1l1ll1111_opy_, stage=STAGE.bstack1l11lll11_opy_, hook_type=bstack11l111_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࡖࡸࡪࡶࠢළ"), bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack11lll1111_opy_(runner, name, context, bstack11llllll1_opy_, *args):
  bstack1llll11ll1_opy_.bstack11l11l11_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack111111l11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫෆ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack111111l11_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack11l111_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෇")
        feature_name = bstack1l1ll11111_opy_ = str(runner.feature.name)
        bstack1l1ll11111_opy_ = feature_name + bstack11l111_opy_ (u"ࠧࠡ࠯ࠣࠫ෈") + context.scenario.name
        bstack111111l11_opy_.execute_script(bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭෉") + json.dumps(bstack1l1ll11111_opy_) + bstack11l111_opy_ (u"ࠩࢀࢁ්ࠬ"))
    if str(step_status).lower() == bstack11l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ෋"):
      bstack1l1lllllll_opy_ = bstack11l111_opy_ (u"ࠫࠬ෌")
      bstack11l1111ll1_opy_ = bstack11l111_opy_ (u"ࠬ࠭෍")
      bstack11l111l11l_opy_ = bstack11l111_opy_ (u"࠭ࠧ෎")
      try:
        import traceback
        bstack1l1lllllll_opy_ = runner.exception.__class__.__name__
        bstack11l1111l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11l1111ll1_opy_ = bstack11l111_opy_ (u"ࠧࠡࠩා").join(bstack11l1111l_opy_)
        bstack11l111l11l_opy_ = bstack11l1111l_opy_[-1]
      except Exception as e:
        logger.debug(bstack11lll1l111_opy_.format(str(e)))
      bstack1l1lllllll_opy_ += bstack11l111l11l_opy_
      bstack11ll11111_opy_(context, json.dumps(str(args[0].name) + bstack11l111_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢැ") + str(bstack11l1111ll1_opy_)),
                          bstack11l111_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣෑ"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣි"):
        bstack1lll111lll_opy_(getattr(context, bstack11l111_opy_ (u"ࠫࡵࡧࡧࡦࠩී"), None), bstack11l111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧු"), bstack1l1lllllll_opy_)
        bstack111111l11_opy_.execute_script(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ෕") + json.dumps(str(args[0].name) + bstack11l111_opy_ (u"ࠢࠡ࠯ࠣࡊࡦ࡯࡬ࡦࡦࠤࡠࡳࠨූ") + str(bstack11l1111ll1_opy_)) + bstack11l111_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨ෗"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢෘ"):
        bstack11ll11lll1_opy_(bstack111111l11_opy_, bstack11l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪෙ"), bstack11l111_opy_ (u"ࠦࡘࡩࡥ࡯ࡣࡵ࡭ࡴࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣේ") + str(bstack1l1lllllll_opy_))
    else:
      bstack11ll11111_opy_(context, bstack11l111_opy_ (u"ࠧࡖࡡࡴࡵࡨࡨࠦࠨෛ"), bstack11l111_opy_ (u"ࠨࡩ࡯ࡨࡲࠦො"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧෝ"):
        bstack1lll111lll_opy_(getattr(context, bstack11l111_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ෞ"), None), bstack11l111_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤෟ"))
      bstack111111l11_opy_.execute_script(bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ෠") + json.dumps(str(args[0].name) + bstack11l111_opy_ (u"ࠦࠥ࠳ࠠࡑࡣࡶࡷࡪࡪࠡࠣ෡")) + bstack11l111_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫ෢"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦ෣"):
        bstack11ll11lll1_opy_(bstack111111l11_opy_, bstack11l111_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ෤"))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥࡹࡴࡦࡲ࠽ࠤࢀࢃࠧ෥").format(str(e)))
  bstack11l11lll1l_opy_(runner, name, context, args[0], bstack11llllll1_opy_, *args)
@measure(event_name=EVENTS.bstack11111l1ll1_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack1llll11lll_opy_(runner, name, context, bstack11llllll1_opy_, *args):
  bstack1llll11ll1_opy_.end_test(args[0])
  try:
    bstack11lll1l1l1_opy_ = args[0].status.name
    bstack111111l11_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨ෦"), context.browser)
    bstack11l11l11ll_opy_.bstack111ll1lll1_opy_(bstack111111l11_opy_)
    if str(bstack11lll1l1l1_opy_).lower() == bstack11l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ෧"):
      bstack1l1lllllll_opy_ = bstack11l111_opy_ (u"ࠫࠬ෨")
      bstack11l1111ll1_opy_ = bstack11l111_opy_ (u"ࠬ࠭෩")
      bstack11l111l11l_opy_ = bstack11l111_opy_ (u"࠭ࠧ෪")
      try:
        import traceback
        bstack1l1lllllll_opy_ = runner.exception.__class__.__name__
        bstack11l1111l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack11l1111ll1_opy_ = bstack11l111_opy_ (u"ࠧࠡࠩ෫").join(bstack11l1111l_opy_)
        bstack11l111l11l_opy_ = bstack11l1111l_opy_[-1]
      except Exception as e:
        logger.debug(bstack11lll1l111_opy_.format(str(e)))
      bstack1l1lllllll_opy_ += bstack11l111l11l_opy_
      bstack11ll11111_opy_(context, json.dumps(str(args[0].name) + bstack11l111_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢ෬") + str(bstack11l1111ll1_opy_)),
                          bstack11l111_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣ෭"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ෮") or runner.driver_initialised == bstack11l111_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫ෯"):
        bstack1lll111lll_opy_(getattr(context, bstack11l111_opy_ (u"ࠬࡶࡡࡨࡧࠪ෰"), None), bstack11l111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ෱"), bstack1l1lllllll_opy_)
        bstack111111l11_opy_.execute_script(bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬෲ") + json.dumps(str(args[0].name) + bstack11l111_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢෳ") + str(bstack11l1111ll1_opy_)) + bstack11l111_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࡽࡾࠩ෴"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ෵") or runner.driver_initialised == bstack11l111_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫ෶"):
        bstack11ll11lll1_opy_(bstack111111l11_opy_, bstack11l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ෷"), bstack11l111_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥ෸") + str(bstack1l1lllllll_opy_))
    else:
      bstack11ll11111_opy_(context, bstack11l111_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣ෹"), bstack11l111_opy_ (u"ࠣ࡫ࡱࡪࡴࠨ෺"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦ෻") or runner.driver_initialised == bstack11l111_opy_ (u"ࠪ࡭ࡳࡹࡴࡦࡲࠪ෼"):
        bstack1lll111lll_opy_(getattr(context, bstack11l111_opy_ (u"ࠫࡵࡧࡧࡦࠩ෽"), None), bstack11l111_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧ෾"))
      bstack111111l11_opy_.execute_script(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ෿") + json.dumps(str(args[0].name) + bstack11l111_opy_ (u"ࠢࠡ࠯ࠣࡔࡦࡹࡳࡦࡦࠤࠦ฀")) + bstack11l111_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦࢂࢃࠧก"))
      if runner.driver_initialised == bstack11l111_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦข") or runner.driver_initialised == bstack11l111_opy_ (u"ࠪ࡭ࡳࡹࡴࡦࡲࠪฃ"):
        bstack11ll11lll1_opy_(bstack111111l11_opy_, bstack11l111_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦค"))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡪࡰࠣࡥ࡫ࡺࡥࡳࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧฅ").format(str(e)))
  bstack11l11lll1l_opy_(runner, name, context, context.scenario, bstack11llllll1_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack111l11l1l_opy_(runner, name, context, bstack11llllll1_opy_, *args):
    target = context.scenario if hasattr(context, bstack11l111_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨฆ")) else context.feature
    bstack11l11lll1l_opy_(runner, name, context, target, bstack11llllll1_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack11lll1ll11_opy_(runner, name, context, bstack11llllll1_opy_, *args):
    try:
      bstack111111l11_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ง"), context.browser)
      bstack1l11lll11l_opy_ = bstack11l111_opy_ (u"ࠨࠩจ")
      if context.failed is True:
        bstack1l1l1l1l1_opy_ = []
        bstack1ll1ll11l_opy_ = []
        bstack111l1ll11_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1l1l1l1l1_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l1111l_opy_ = traceback.format_tb(exc_tb)
            bstack1l1l1111l_opy_ = bstack11l111_opy_ (u"ࠩࠣࠫฉ").join(bstack11l1111l_opy_)
            bstack1ll1ll11l_opy_.append(bstack1l1l1111l_opy_)
            bstack111l1ll11_opy_.append(bstack11l1111l_opy_[-1])
        except Exception as e:
          logger.debug(bstack11lll1l111_opy_.format(str(e)))
        bstack1l1lllllll_opy_ = bstack11l111_opy_ (u"ࠪࠫช")
        for i in range(len(bstack1l1l1l1l1_opy_)):
          bstack1l1lllllll_opy_ += bstack1l1l1l1l1_opy_[i] + bstack111l1ll11_opy_[i] + bstack11l111_opy_ (u"ࠫࡡࡴࠧซ")
        bstack1l11lll11l_opy_ = bstack11l111_opy_ (u"ࠬࠦࠧฌ").join(bstack1ll1ll11l_opy_)
        if runner.driver_initialised in [bstack11l111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢญ"), bstack11l111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦฎ")]:
          bstack11ll11111_opy_(context, bstack1l11lll11l_opy_, bstack11l111_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢฏ"))
          bstack1lll111lll_opy_(getattr(context, bstack11l111_opy_ (u"ࠩࡳࡥ࡬࡫ࠧฐ"), None), bstack11l111_opy_ (u"ࠥࡪࡦ࡯࡬ࡦࡦࠥฑ"), bstack1l1lllllll_opy_)
          bstack111111l11_opy_.execute_script(bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩฒ") + json.dumps(bstack1l11lll11l_opy_) + bstack11l111_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤࢀࢁࠬณ"))
          bstack11ll11lll1_opy_(bstack111111l11_opy_, bstack11l111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨด"), bstack11l111_opy_ (u"ࠢࡔࡱࡰࡩࠥࡹࡣࡦࡰࡤࡶ࡮ࡵࡳࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢ࡟ࡲࠧต") + str(bstack1l1lllllll_opy_))
          bstack1l1lll1111_opy_ = bstack11l11ll1ll_opy_(bstack1l11lll11l_opy_, runner.feature.name, logger)
          if (bstack1l1lll1111_opy_ != None):
            bstack111ll11l1_opy_.append(bstack1l1lll1111_opy_)
      else:
        if runner.driver_initialised in [bstack11l111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤถ"), bstack11l111_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨท")]:
          bstack11ll11111_opy_(context, bstack11l111_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨ࠾ࠥࠨธ") + str(runner.feature.name) + bstack11l111_opy_ (u"ࠦࠥࡶࡡࡴࡵࡨࡨࠦࠨน"), bstack11l111_opy_ (u"ࠧ࡯࡮ࡧࡱࠥบ"))
          bstack1lll111lll_opy_(getattr(context, bstack11l111_opy_ (u"࠭ࡰࡢࡩࡨࠫป"), None), bstack11l111_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢผ"))
          bstack111111l11_opy_.execute_script(bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ฝ") + json.dumps(bstack11l111_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧ࠽ࠤࠧพ") + str(runner.feature.name) + bstack11l111_opy_ (u"ࠥࠤࡵࡧࡳࡴࡧࡧࠥࠧฟ")) + bstack11l111_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢࡾࡿࠪภ"))
          bstack11ll11lll1_opy_(bstack111111l11_opy_, bstack11l111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬม"))
          bstack1l1lll1111_opy_ = bstack11l11ll1ll_opy_(bstack1l11lll11l_opy_, runner.feature.name, logger)
          if (bstack1l1lll1111_opy_ != None):
            bstack111ll11l1_opy_.append(bstack1l1lll1111_opy_)
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨย").format(str(e)))
    bstack11l11lll1l_opy_(runner, name, context, context.feature, bstack11llllll1_opy_, *args)
@measure(event_name=EVENTS.bstack1l1ll1111_opy_, stage=STAGE.bstack1l11lll11_opy_, hook_type=bstack11l111_opy_ (u"ࠢࡢࡨࡷࡩࡷࡇ࡬࡭ࠤร"), bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack1111l1111l_opy_(runner, name, context, bstack11llllll1_opy_, *args):
    bstack11l11lll1l_opy_(runner, name, context, runner, bstack11llllll1_opy_, *args)
def bstack1l1l111ll1_opy_(self, name, context, *args):
  try:
    if bstack11l1111l11_opy_:
      platform_index = int(threading.current_thread()._name) % bstack111l11llll_opy_
      bstack1l111ll1l_opy_ = CONFIG[bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫฤ")][platform_index]
      os.environ[bstack11l111_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪล")] = json.dumps(bstack1l111ll1l_opy_)
    global bstack11llllll1_opy_
    if not hasattr(self, bstack11l111_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡸ࡫ࡤࠨฦ")):
      self.driver_initialised = None
    bstack1l1lll1lll_opy_ = {
        bstack11l111_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠨว"): bstack1111l11l1_opy_,
        bstack11l111_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ศ"): bstack11l1l11ll1_opy_,
        bstack11l111_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡴࡢࡩࠪษ"): bstack111l1ll1ll_opy_,
        bstack11l111_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩส"): bstack11l11lll1_opy_,
        bstack11l111_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵ࠭ห"): bstack1ll1l11l11_opy_,
        bstack11l111_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡷࡩࡵ࠭ฬ"): bstack11lll1111_opy_,
        bstack11l111_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫอ"): bstack1llll11lll_opy_,
        bstack11l111_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡸࡦ࡭ࠧฮ"): bstack111l11l1l_opy_,
        bstack11l111_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣ࡫࡫ࡡࡵࡷࡵࡩࠬฯ"): bstack11lll1ll11_opy_,
        bstack11l111_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩะ"): bstack1111l1111l_opy_
    }
    handler = bstack1l1lll1lll_opy_.get(name, bstack11llllll1_opy_)
    try:
      handler(self, name, context, bstack11llllll1_opy_, *args)
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦࠢ࡫ࡳࡴࡱࠠࡩࡣࡱࡨࡱ࡫ࡲࠡࡽࢀ࠾ࠥࢁࡽࠨั").format(name, str(e)))
    if name in [bstack11l111_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨา"), bstack11l111_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱࠪำ"), bstack11l111_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡤࡰࡱ࠭ิ")]:
      try:
        bstack111111l11_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1l11l_opy_(bstack11l111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪี")) else context.browser
        bstack1l111l1ll1_opy_ = (
          (name == bstack11l111_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨึ") and self.driver_initialised == bstack11l111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥื")) or
          (name == bstack11l111_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ุࠧ") and self.driver_initialised == bstack11l111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤู")) or
          (name == bstack11l111_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱฺࠪ") and self.driver_initialised in [bstack11l111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧ฻"), bstack11l111_opy_ (u"ࠦ࡮ࡴࡳࡵࡧࡳࠦ฼")]) or
          (name == bstack11l111_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡺࡥࡱࠩ฽") and self.driver_initialised == bstack11l111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦ฾"))
        )
        if bstack1l111l1ll1_opy_:
          self.driver_initialised = None
          if bstack111111l11_opy_ and hasattr(bstack111111l11_opy_, bstack11l111_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠫ฿")):
            try:
              bstack111111l11_opy_.quit()
            except Exception as e:
              logger.debug(bstack11l111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡲࡷ࡬ࡸࡹ࡯࡮ࡨࠢࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩࠥ࡮࡯ࡰ࡭࠽ࠤࢀࢃࠧเ").format(str(e)))
      except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣ࡬ࡴࡵ࡫ࠡࡥ࡯ࡩࡦࡴࡵࡱࠢࡩࡳࡷࠦࡻࡾ࠼ࠣࡿࢂ࠭แ").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"ࠪࡇࡷ࡯ࡴࡪࡥࡤࡰࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡳࡷࡱࠤ࡭ࡵ࡯࡬ࠢࡾࢁ࠿ࠦࡻࡾࠩโ").format(name, str(e)))
    try:
      bstack11llllll1_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack11l111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫ࠡࡱࡵ࡭࡬࡯࡮ࡢ࡮ࠣࡦࡪ࡮ࡡࡷࡧࠣ࡬ࡴࡵ࡫ࠡࡽࢀ࠾ࠥࢁࡽࠨใ").format(name, str(e2)))
def bstack1111l1l111_opy_(config, startdir):
  return bstack11l111_opy_ (u"ࠧࡪࡲࡪࡸࡨࡶ࠿ࠦࡻ࠱ࡿࠥไ").format(bstack11l111_opy_ (u"ࠨࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠧๅ"))
notset = Notset()
def bstack1lll1l111l_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack11l1111111_opy_
  if str(name).lower() == bstack11l111_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸࠧๆ"):
    return bstack11l111_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢ็")
  else:
    return bstack11l1111111_opy_(self, name, default, skip)
def bstack1l11ll111_opy_(item, when):
  global bstack1ll1ll11l1_opy_
  try:
    bstack1ll1ll11l1_opy_(item, when)
  except Exception as e:
    pass
def bstack11lll11lll_opy_():
  return
def bstack1ll1lll11l_opy_(type, name, status, reason, bstack11lll1l11_opy_, bstack1111l11l1l_opy_):
  bstack1ll1111111_opy_ = {
    bstack11l111_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯่ࠩ"): type,
    bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ้࠭"): {}
  }
  if type == bstack11l111_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ๊࠭"):
    bstack1ll1111111_opy_[bstack11l111_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ๋")][bstack11l111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ์")] = bstack11lll1l11_opy_
    bstack1ll1111111_opy_[bstack11l111_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪํ")][bstack11l111_opy_ (u"ࠨࡦࡤࡸࡦ࠭๎")] = json.dumps(str(bstack1111l11l1l_opy_))
  if type == bstack11l111_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ๏"):
    bstack1ll1111111_opy_[bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭๐")][bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ๑")] = name
  if type == bstack11l111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ๒"):
    bstack1ll1111111_opy_[bstack11l111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ๓")][bstack11l111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ๔")] = status
    if status == bstack11l111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ๕"):
      bstack1ll1111111_opy_[bstack11l111_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ๖")][bstack11l111_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ๗")] = json.dumps(str(reason))
  bstack1l1l1l1111_opy_ = bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩ๘").format(json.dumps(bstack1ll1111111_opy_))
  return bstack1l1l1l1111_opy_
def bstack11ll1lll11_opy_(driver_command, response):
    if driver_command == bstack11l111_opy_ (u"ࠬࡹࡣࡳࡧࡨࡲࡸ࡮࡯ࡵࠩ๙"):
        bstack1lll111l_opy_.bstack111l11lll_opy_({
            bstack11l111_opy_ (u"࠭ࡩ࡮ࡣࡪࡩࠬ๚"): response[bstack11l111_opy_ (u"ࠧࡷࡣ࡯ࡹࡪ࠭๛")],
            bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ๜"): bstack1lll111l_opy_.current_test_uuid()
        })
def bstack111ll1llll_opy_(item, call, rep):
  global bstack11lll111l1_opy_
  global bstack11l11l111_opy_
  global bstack1ll111lll1_opy_
  name = bstack11l111_opy_ (u"ࠩࠪ๝")
  try:
    if rep.when == bstack11l111_opy_ (u"ࠪࡧࡦࡲ࡬ࠨ๞"):
      bstack11lll1lll1_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1ll111lll1_opy_:
          name = str(rep.nodeid)
          bstack1l111l1l1l_opy_ = bstack1ll1lll11l_opy_(bstack11l111_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ๟"), name, bstack11l111_opy_ (u"ࠬ࠭๠"), bstack11l111_opy_ (u"࠭ࠧ๡"), bstack11l111_opy_ (u"ࠧࠨ๢"), bstack11l111_opy_ (u"ࠨࠩ๣"))
          threading.current_thread().bstack1llll1111l_opy_ = name
          for driver in bstack11l11l111_opy_:
            if bstack11lll1lll1_opy_ == driver.session_id:
              driver.execute_script(bstack1l111l1l1l_opy_)
      except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠩ๤").format(str(e)))
      try:
        bstack1ll11l111_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ๥"):
          status = bstack11l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ๦") if rep.outcome.lower() == bstack11l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ๧") else bstack11l111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭๨")
          reason = bstack11l111_opy_ (u"ࠧࠨ๩")
          if status == bstack11l111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ๪"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11l111_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧ๫") if status == bstack11l111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ๬") else bstack11l111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ๭")
          data = name + bstack11l111_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩࠧࠧ๮") if status == bstack11l111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭๯") else name + bstack11l111_opy_ (u"ࠧࠡࡨࡤ࡭ࡱ࡫ࡤࠢࠢࠪ๰") + reason
          bstack1ll11ll1ll_opy_ = bstack1ll1lll11l_opy_(bstack11l111_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪ๱"), bstack11l111_opy_ (u"ࠩࠪ๲"), bstack11l111_opy_ (u"ࠪࠫ๳"), bstack11l111_opy_ (u"ࠫࠬ๴"), level, data)
          for driver in bstack11l11l111_opy_:
            if bstack11lll1lll1_opy_ == driver.session_id:
              driver.execute_script(bstack1ll11ll1ll_opy_)
      except Exception as e:
        logger.debug(bstack11l111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡦࡳࡳࡺࡥࡹࡶࠣࡪࡴࡸࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠿ࠦࡻࡾࠩ๵").format(str(e)))
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡶࡸࡦࡺࡥࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࠦࡳࡵࡣࡷࡹࡸࡀࠠࡼࡿࠪ๶").format(str(e)))
  bstack11lll111l1_opy_(item, call, rep)
def bstack1l1lll1ll_opy_(driver, bstack11ll1ll1l_opy_, test=None):
  global bstack1l1l11llll_opy_
  if test != None:
    bstack1111l1ll11_opy_ = getattr(test, bstack11l111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ๷"), None)
    bstack1lll11ll11_opy_ = getattr(test, bstack11l111_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭๸"), None)
    PercySDK.screenshot(driver, bstack11ll1ll1l_opy_, bstack1111l1ll11_opy_=bstack1111l1ll11_opy_, bstack1lll11ll11_opy_=bstack1lll11ll11_opy_, bstack1ll1l1l11_opy_=bstack1l1l11llll_opy_)
  else:
    PercySDK.screenshot(driver, bstack11ll1ll1l_opy_)
@measure(event_name=EVENTS.bstack111lll1ll1_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack11l1l1ll1l_opy_(driver):
  if bstack11l1llll1_opy_.bstack111l1ll11l_opy_() is True or bstack11l1llll1_opy_.capturing() is True:
    return
  bstack11l1llll1_opy_.bstack11ll111l11_opy_()
  while not bstack11l1llll1_opy_.bstack111l1ll11l_opy_():
    bstack1l1111l111_opy_ = bstack11l1llll1_opy_.bstack111l1l1l11_opy_()
    bstack1l1lll1ll_opy_(driver, bstack1l1111l111_opy_)
  bstack11l1llll1_opy_.bstack111l1l1111_opy_()
def bstack1l1l1ll1l_opy_(sequence, driver_command, response = None, bstack11ll111111_opy_ = None, args = None):
    try:
      if sequence != bstack11l111_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࠩ๹"):
        return
      if percy.bstack1l1lllll1l_opy_() == bstack11l111_opy_ (u"ࠥࡪࡦࡲࡳࡦࠤ๺"):
        return
      bstack1l1111l111_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ๻"), None)
      for command in bstack11l11111ll_opy_:
        if command == driver_command:
          with bstack1l111l1l11_opy_:
            bstack1lll11llll_opy_ = bstack11l11l111_opy_.copy()
          for driver in bstack1lll11llll_opy_:
            bstack11l1l1ll1l_opy_(driver)
      bstack1ll1l1l1l_opy_ = percy.bstack1l1l1l111l_opy_()
      if driver_command in bstack1lll111111_opy_[bstack1ll1l1l1l_opy_]:
        bstack11l1llll1_opy_.bstack11ll1l1l1l_opy_(bstack1l1111l111_opy_, driver_command)
    except Exception as e:
      pass
def bstack11llll111_opy_(framework_name):
  if bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡳ࡯ࡥࡡࡦࡥࡱࡲࡥࡥࠩ๼")):
      return
  bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ๽"), True)
  global bstack1111l1l1l1_opy_
  global bstack1lllllllll_opy_
  global bstack1ll1111l1_opy_
  bstack1111l1l1l1_opy_ = framework_name
  logger.info(bstack11l11lllll_opy_.format(bstack1111l1l1l1_opy_.split(bstack11l111_opy_ (u"ࠧ࠮ࠩ๾"))[0]))
  bstack11l1lll1l_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack11l1111l11_opy_:
      Service.start = bstack1l1ll1l1l1_opy_
      Service.stop = bstack111lll1ll_opy_
      webdriver.Remote.get = bstack111l1lll1l_opy_
      WebDriver.quit = bstack11l1l11l11_opy_
      webdriver.Remote.__init__ = bstack1ll1l1l11l_opy_
    if not bstack11l1111l11_opy_:
        webdriver.Remote.__init__ = bstack11ll1l1111_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack1lll11ll1l_opy_
    bstack1lllllllll_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack11l1111l11_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1l1lll1l11_opy_
  except Exception as e:
    pass
  bstack111l1l1l1l_opy_()
  if not bstack1lllllllll_opy_:
    bstack11111l1l1_opy_(bstack11l111_opy_ (u"ࠣࡒࡤࡧࡰࡧࡧࡦࡵࠣࡲࡴࡺࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠥ๿"), bstack1ll11l1ll1_opy_)
  if bstack11l1l1l111_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack11l111_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪ຀")) and callable(getattr(RemoteConnection, bstack11l111_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫກ"))):
        RemoteConnection._get_proxy_url = bstack1ll11ll11l_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack1ll11ll11l_opy_
    except Exception as e:
      logger.error(bstack11ll1l1ll1_opy_.format(str(e)))
  if bstack1llll1ll1l_opy_():
    bstack111l1l111_opy_(CONFIG, logger)
  if (bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪຂ") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1l1lllll1l_opy_() == bstack11l111_opy_ (u"ࠧࡺࡲࡶࡧࠥ຃"):
          bstack111l11l111_opy_(bstack1l1l1ll1l_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1l11llllll_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1llll11l1l_opy_
      except Exception as e:
        logger.warn(bstack1l1111l1l1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack11l11ll1l1_opy_
      except Exception as e:
        logger.debug(bstack1ll111ll1l_opy_ + str(e))
    except Exception as e:
      bstack11111l1l1_opy_(e, bstack1l1111l1l1_opy_)
    Output.start_test = bstack1l11l11ll1_opy_
    Output.end_test = bstack1l1ll11lll_opy_
    TestStatus.__init__ = bstack1llll11l11_opy_
    QueueItem.__init__ = bstack11lll1ll1l_opy_
    pabot._create_items = bstack1ll11llll1_opy_
    try:
      from pabot import __version__ as bstack1ll1ll1ll1_opy_
      if version.parse(bstack1ll1ll1ll1_opy_) >= version.parse(bstack11l111_opy_ (u"࠭࠵࠯࠲࠱࠴ࠬຄ")):
        pabot._run = bstack1ll1lllll1_opy_
      elif version.parse(bstack1ll1ll1ll1_opy_) >= version.parse(bstack11l111_opy_ (u"ࠧ࠵࠰࠵࠲࠵࠭຅")):
        pabot._run = bstack1l111l111_opy_
      elif version.parse(bstack1ll1ll1ll1_opy_) >= version.parse(bstack11l111_opy_ (u"ࠨ࠴࠱࠵࠺࠴࠰ࠨຆ")):
        pabot._run = bstack1ll11l1ll_opy_
      elif version.parse(bstack1ll1ll1ll1_opy_) >= version.parse(bstack11l111_opy_ (u"ࠩ࠵࠲࠶࠹࠮࠱ࠩງ")):
        pabot._run = bstack111l1llll_opy_
      else:
        pabot._run = bstack1ll11ll1l1_opy_
    except Exception as e:
      pabot._run = bstack1ll11ll1l1_opy_
    pabot._create_command_for_execution = bstack11111l11l_opy_
    pabot._report_results = bstack1l1llll11l_opy_
  if bstack11l111_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪຈ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11111l1l1_opy_(e, bstack1ll1111ll_opy_)
    Runner.run_hook = bstack1l1l111ll1_opy_
    Step.run = bstack1l11l1l1l1_opy_
  if bstack11l111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫຉ") in str(framework_name).lower():
    if not bstack11l1111l11_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1111l1l111_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack11lll11lll_opy_
      Config.getoption = bstack1lll1l111l_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack111ll1llll_opy_
    except Exception as e:
      pass
def bstack11ll11ll1_opy_():
  global CONFIG
  if bstack11l111_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬຊ") in CONFIG and int(CONFIG[bstack11l111_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭຋")]) > 1:
    logger.warn(bstack11111l11l1_opy_)
def bstack11llllllll_opy_(arg, bstack111111l1_opy_, bstack1l1ll11ll1_opy_=None):
  global CONFIG
  global bstack1111llll11_opy_
  global bstack11l11111l_opy_
  global bstack11l1111l11_opy_
  global bstack11111l11_opy_
  bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧຌ")
  if bstack111111l1_opy_ and isinstance(bstack111111l1_opy_, str):
    bstack111111l1_opy_ = eval(bstack111111l1_opy_)
  CONFIG = bstack111111l1_opy_[bstack11l111_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨຍ")]
  bstack1111llll11_opy_ = bstack111111l1_opy_[bstack11l111_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪຎ")]
  bstack11l11111l_opy_ = bstack111111l1_opy_[bstack11l111_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬຏ")]
  bstack11l1111l11_opy_ = bstack111111l1_opy_[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧຐ")]
  bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ຑ"), bstack11l1111l11_opy_)
  os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨຒ")] = bstack111l11l11_opy_
  os.environ[bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡐࡐࡉࡍࡌ࠭ຓ")] = json.dumps(CONFIG)
  os.environ[bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡉࡗࡅࡣ࡚ࡘࡌࠨດ")] = bstack1111llll11_opy_
  os.environ[bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪຕ")] = str(bstack11l11111l_opy_)
  os.environ[bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓ࡝࡙ࡋࡓࡕࡡࡓࡐ࡚ࡍࡉࡏࠩຖ")] = str(True)
  if bstack1lll111ll1_opy_(arg, [bstack11l111_opy_ (u"ࠫ࠲ࡴࠧທ"), bstack11l111_opy_ (u"ࠬ࠳࠭࡯ࡷࡰࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ຘ")]) != -1:
    os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡁࡓࡃࡏࡐࡊࡒࠧນ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack11l1lll111_opy_)
    return
  bstack111lllll1l_opy_()
  global bstack1lll1ll1l1_opy_
  global bstack1l1l11llll_opy_
  global bstack111l1lll11_opy_
  global bstack1l1l1l1lll_opy_
  global bstack11lllllll_opy_
  global bstack1ll1111l1_opy_
  global bstack1l11ll11l1_opy_
  arg.append(bstack11l111_opy_ (u"ࠢ࠮࡙ࠥບ"))
  arg.append(bstack11l111_opy_ (u"ࠣ࡫ࡪࡲࡴࡸࡥ࠻ࡏࡲࡨࡺࡲࡥࠡࡣ࡯ࡶࡪࡧࡤࡺࠢ࡬ࡱࡵࡵࡲࡵࡧࡧ࠾ࡵࡿࡴࡦࡵࡷ࠲ࡕࡿࡴࡦࡵࡷ࡛ࡦࡸ࡮ࡪࡰࡪࠦປ"))
  arg.append(bstack11l111_opy_ (u"ࠤ࠰࡛ࠧຜ"))
  arg.append(bstack11l111_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧ࠽ࡘ࡭࡫ࠠࡩࡱࡲ࡯࡮ࡳࡰ࡭ࠤຝ"))
  global bstack1ll1l1lll1_opy_
  global bstack11l1lll11_opy_
  global bstack1ll111l111_opy_
  global bstack1l111llll1_opy_
  global bstack1l11ll1ll_opy_
  global bstack1l1l11lll1_opy_
  global bstack1111111ll_opy_
  global bstack1l1l11l1l1_opy_
  global bstack1l111l1l1_opy_
  global bstack111ll1ll1_opy_
  global bstack11l1111111_opy_
  global bstack1ll1ll11l1_opy_
  global bstack11lll111l1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll1l1lll1_opy_ = webdriver.Remote.__init__
    bstack11l1lll11_opy_ = WebDriver.quit
    bstack1l1l11l1l1_opy_ = WebDriver.close
    bstack1l111l1l1_opy_ = WebDriver.get
    bstack1ll111l111_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1lll1l1l1l_opy_(CONFIG) and bstack11l1ll1111_opy_():
    if bstack1ll1l11ll_opy_() < version.parse(bstack11l11ll111_opy_):
      logger.error(bstack11111l1lll_opy_.format(bstack1ll1l11ll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11l111_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬພ")) and callable(getattr(RemoteConnection, bstack11l111_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ຟ"))):
          bstack111ll1ll1_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack111ll1ll1_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack11ll1l1ll1_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack11l1111111_opy_ = Config.getoption
    from _pytest import runner
    bstack1ll1ll11l1_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1lll11l11_opy_)
  try:
    from pytest_bdd import reporting
    bstack11lll111l1_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11l111_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹࡵࠠࡳࡷࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࡹࠧຠ"))
  bstack111l1lll11_opy_ = CONFIG.get(bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫມ"), {}).get(bstack11l111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪຢ"))
  bstack1l11ll11l1_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack1l1ll1l11l_opy_():
      bstack1l11ll1l11_opy_.invoke(Events.CONNECT, bstack1l1llll1l1_opy_())
    platform_index = int(os.environ.get(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩຣ"), bstack11l111_opy_ (u"ࠪ࠴ࠬ຤")))
  else:
    bstack11llll111_opy_(bstack1l1l11l111_opy_)
  os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢ࡙ࡘࡋࡒࡏࡃࡐࡉࠬລ")] = CONFIG[bstack11l111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ຦")]
  os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩວ")] = CONFIG[bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪຨ")]
  os.environ[bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫຩ")] = bstack11l1111l11_opy_.__str__()
  from _pytest.config import main as bstack11ll11111l_opy_
  bstack1ll111lll_opy_ = []
  try:
    exit_code = bstack11ll11111l_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1l111l11l_opy_()
    if bstack11l111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭ສ") in multiprocessing.current_process().__dict__.keys():
      for bstack11ll1ll11_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1ll111lll_opy_.append(bstack11ll1ll11_opy_)
    try:
      bstack11llll1l1_opy_ = (bstack1ll111lll_opy_, int(exit_code))
      bstack1l1ll11ll1_opy_.append(bstack11llll1l1_opy_)
    except:
      bstack1l1ll11ll1_opy_.append((bstack1ll111lll_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1ll111lll_opy_.append({bstack11l111_opy_ (u"ࠪࡲࡦࡳࡥࠨຫ"): bstack11l111_opy_ (u"ࠫࡕࡸ࡯ࡤࡧࡶࡷࠥ࠭ຬ") + os.environ.get(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬອ")), bstack11l111_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬຮ"): traceback.format_exc(), bstack11l111_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ຯ"): int(os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨະ")))})
    bstack1l1ll11ll1_opy_.append((bstack1ll111lll_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack11l111_opy_ (u"ࠤࡵࡩࡹࡸࡩࡦࡵࠥັ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack11ll111l1l_opy_ = e.__class__.__name__
    print(bstack11l111_opy_ (u"ࠥࠩࡸࡀࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡵࡧࡶࡸࠥࠫࡳࠣາ") % (bstack11ll111l1l_opy_, e))
    return 1
def bstack1l1l1l11l_opy_(arg):
  global bstack1ll111l11l_opy_
  bstack11llll111_opy_(bstack11llll1ll1_opy_)
  os.environ[bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬຳ")] = str(bstack11l11111l_opy_)
  retries = bstack1lll1l1ll_opy_.bstack1lllll1l1_opy_(CONFIG)
  status_code = 0
  if bstack1lll1l1ll_opy_.bstack1lll111l1_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack1ll11llll_opy_
    status_code = bstack1ll11llll_opy_(arg)
  if status_code != 0:
    bstack1ll111l11l_opy_ = status_code
def bstack11llll111l_opy_():
  logger.info(bstack111l111l1l_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11l111_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫິ"), help=bstack11l111_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡤࡱࡱࡪ࡮࡭ࠧີ"))
  parser.add_argument(bstack11l111_opy_ (u"ࠧ࠮ࡷࠪຶ"), bstack11l111_opy_ (u"ࠨ࠯࠰ࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠬື"), help=bstack11l111_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡵࡴࡧࡵࡲࡦࡳࡥࠨຸ"))
  parser.add_argument(bstack11l111_opy_ (u"ࠪ࠱ࡰູ࠭"), bstack11l111_opy_ (u"ࠫ࠲࠳࡫ࡦࡻ຺ࠪ"), help=bstack11l111_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾ࠭ົ"))
  parser.add_argument(bstack11l111_opy_ (u"࠭࠭ࡧࠩຼ"), bstack11l111_opy_ (u"ࠧ࠮࠯ࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬຽ"), help=bstack11l111_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡴࡦࡵࡷࠤ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ຾"))
  bstack11ll1llll1_opy_ = parser.parse_args()
  try:
    bstack11l1l11ll_opy_ = bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡩࡨࡲࡪࡸࡩࡤ࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭຿")
    if bstack11ll1llll1_opy_.framework and bstack11ll1llll1_opy_.framework not in (bstack11l111_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪເ"), bstack11l111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬແ")):
      bstack11l1l11ll_opy_ = bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࠮ࡺ࡯࡯࠲ࡸࡧ࡭ࡱ࡮ࡨࠫໂ")
    bstack1l11ll11ll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1l11ll_opy_)
    bstack11ll1111l_opy_ = open(bstack1l11ll11ll_opy_, bstack11l111_opy_ (u"࠭ࡲࠨໃ"))
    bstack1111l11ll_opy_ = bstack11ll1111l_opy_.read()
    bstack11ll1111l_opy_.close()
    if bstack11ll1llll1_opy_.username:
      bstack1111l11ll_opy_ = bstack1111l11ll_opy_.replace(bstack11l111_opy_ (u"࡚ࠧࡑࡘࡖࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧໄ"), bstack11ll1llll1_opy_.username)
    if bstack11ll1llll1_opy_.key:
      bstack1111l11ll_opy_ = bstack1111l11ll_opy_.replace(bstack11l111_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪ໅"), bstack11ll1llll1_opy_.key)
    if bstack11ll1llll1_opy_.framework:
      bstack1111l11ll_opy_ = bstack1111l11ll_opy_.replace(bstack11l111_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪໆ"), bstack11ll1llll1_opy_.framework)
    file_name = bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡱࡱ࠭໇")
    file_path = os.path.abspath(file_name)
    bstack1l1l11l11_opy_ = open(file_path, bstack11l111_opy_ (u"ࠫࡼ່࠭"))
    bstack1l1l11l11_opy_.write(bstack1111l11ll_opy_)
    bstack1l1l11l11_opy_.close()
    logger.info(bstack1lll1llll1_opy_)
    try:
      os.environ[bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ້ࠧ")] = bstack11ll1llll1_opy_.framework if bstack11ll1llll1_opy_.framework != None else bstack11l111_opy_ (u"ࠨ໊ࠢ")
      config = yaml.safe_load(bstack1111l11ll_opy_)
      config[bstack11l111_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫໋ࠧ")] = bstack11l111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠮ࡵࡨࡸࡺࡶࠧ໌")
      bstack1lllll11l1_opy_(bstack1l1l11l1ll_opy_, config)
    except Exception as e:
      logger.debug(bstack11l11lll11_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1l1l1llll_opy_.format(str(e)))
def bstack1lllll11l1_opy_(bstack1ll111111l_opy_, config, bstack11ll1l111l_opy_={}):
  global bstack11l1111l11_opy_
  global bstack1l11111l11_opy_
  global bstack11111l11_opy_
  if not config:
    return
  bstack1ll1111lll_opy_ = bstack1l1llllll1_opy_ if not bstack11l1111l11_opy_ else (
    bstack1l11l11ll_opy_ if bstack11l111_opy_ (u"ࠩࡤࡴࡵ࠭ໍ") in config else (
        bstack1ll111111_opy_ if config.get(bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ໎")) else bstack11111l111_opy_
    )
)
  bstack1lll1111l1_opy_ = False
  bstack11111ll1ll_opy_ = False
  if bstack11l1111l11_opy_ is True:
      if bstack11l111_opy_ (u"ࠫࡦࡶࡰࠨ໏") in config:
          bstack1lll1111l1_opy_ = True
      else:
          bstack11111ll1ll_opy_ = True
  bstack111ll111l1_opy_ = bstack11ll111ll_opy_.bstack1l1llll1ll_opy_(config, bstack1l11111l11_opy_)
  bstack1l1l11111_opy_ = bstack111lll1l1l_opy_()
  data = {
    bstack11l111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ໐"): config[bstack11l111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ໑")],
    bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ໒"): config[bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ໓")],
    bstack11l111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭໔"): bstack1ll111111l_opy_,
    bstack11l111_opy_ (u"ࠪࡨࡪࡺࡥࡤࡶࡨࡨࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ໕"): os.environ.get(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭໖"), bstack1l11111l11_opy_),
    bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧ໗"): bstack1l11l1lll_opy_,
    bstack11l111_opy_ (u"࠭࡯ࡱࡶ࡬ࡱࡦࡲ࡟ࡩࡷࡥࡣࡺࡸ࡬ࠨ໘"): bstack1l111l11l1_opy_(),
    bstack11l111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ໙"): {
      bstack11l111_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࡢࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭໚"): str(config[bstack11l111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ໛")]) if bstack11l111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪໜ") in config else bstack11l111_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧໝ"),
      bstack11l111_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࡖࡦࡴࡶ࡭ࡴࡴࠧໞ"): sys.version,
      bstack11l111_opy_ (u"࠭ࡲࡦࡨࡨࡶࡷ࡫ࡲࠨໟ"): bstack11111ll11l_opy_(os.environ.get(bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ໠"), bstack1l11111l11_opy_)),
      bstack11l111_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪ໡"): bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ໢"),
      bstack11l111_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࠫ໣"): bstack1ll1111lll_opy_,
      bstack11l111_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࡤࡳࡡࡱࠩ໤"): bstack111ll111l1_opy_,
      bstack11l111_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡥࡵࡶ࡫ࡧࠫ໥"): os.environ[bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ໦")],
      bstack11l111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ໧"): os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ໨"), bstack1l11111l11_opy_),
      bstack11l111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ໩"): bstack1ll1l11ll1_opy_(os.environ.get(bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ໪"), bstack1l11111l11_opy_)),
      bstack11l111_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ໫"): bstack1l1l11111_opy_.get(bstack11l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ໬")),
      bstack11l111_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ໭"): bstack1l1l11111_opy_.get(bstack11l111_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ໮")),
      bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ໯"): config[bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ໰")] if config[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໱")] else bstack11l111_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧ໲"),
      bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ໳"): str(config[bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ໴")]) if bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ໵") in config else bstack11l111_opy_ (u"ࠣࡷࡱ࡯ࡳࡵࡷ࡯ࠤ໶"),
      bstack11l111_opy_ (u"ࠩࡲࡷࠬ໷"): sys.platform,
      bstack11l111_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬ໸"): socket.gethostname(),
      bstack11l111_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭໹"): bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ໺"))
    }
  }
  if not bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭໻")) is None:
    data[bstack11l111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ໼")][bstack11l111_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡐࡩࡹࡧࡤࡢࡶࡤࠫ໽")] = {
      bstack11l111_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩ໾"): bstack11l111_opy_ (u"ࠪࡹࡸ࡫ࡲࡠ࡭࡬ࡰࡱ࡫ࡤࠨ໿"),
      bstack11l111_opy_ (u"ࠫࡸ࡯ࡧ࡯ࡣ࡯ࠫༀ"): bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ༁")),
      bstack11l111_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱࡔࡵ࡮ࡤࡨࡶࠬ༂"): bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡏࡱࠪ༃"))
    }
  if bstack1ll111111l_opy_ == bstack11l1ll1l1l_opy_:
    data[bstack11l111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ༄")][bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡄࡱࡱࡪ࡮࡭ࠧ༅")] = bstack1111l11ll1_opy_(config)
    data[bstack11l111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭༆")][bstack11l111_opy_ (u"ࠫ࡮ࡹࡐࡦࡴࡦࡽࡆࡻࡴࡰࡇࡱࡥࡧࡲࡥࡥࠩ༇")] = percy.bstack111l11lll1_opy_
    data[bstack11l111_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ༈")][bstack11l111_opy_ (u"࠭ࡰࡦࡴࡦࡽࡇࡻࡩ࡭ࡦࡌࡨࠬ༉")] = percy.percy_build_id
  if not bstack1lll1l1ll_opy_.bstack1l1llll1l_opy_(CONFIG):
    data[bstack11l111_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ༊")][bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠬ་")] = bstack1lll1l1ll_opy_.bstack1l1llll1l_opy_(CONFIG)
  bstack1lll1ll11_opy_ = bstack11111lll_opy_.bstack111l11l1_opy_(CONFIG, logger)
  bstack1111ll1l_opy_ = bstack1lll1l1ll_opy_.bstack111l11l1_opy_(config=CONFIG)
  if bstack1lll1ll11_opy_ is not None and bstack1111ll1l_opy_ is not None and bstack1111ll1l_opy_.bstack1llllll11_opy_():
    data[bstack11l111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ༌")][bstack1111ll1l_opy_.bstack11ll1l11ll_opy_()] = bstack1lll1ll11_opy_.bstack1111lll1ll_opy_()
  update(data[bstack11l111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭།")], bstack11ll1l111l_opy_)
  try:
    response = bstack111l1llll1_opy_(bstack11l111_opy_ (u"ࠫࡕࡕࡓࡕࠩ༎"), bstack11l1l11l1_opy_(bstack1l11111lll_opy_), data, {
      bstack11l111_opy_ (u"ࠬࡧࡵࡵࡪࠪ༏"): (config[bstack11l111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ༐")], config[bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ༑")])
    })
    if response:
      logger.debug(bstack1l1l1l1ll1_opy_.format(bstack1ll111111l_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack111ll11ll_opy_.format(str(e)))
def bstack11111ll11l_opy_(framework):
  return bstack11l111_opy_ (u"ࠣࡽࢀ࠱ࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧ༒").format(str(framework), __version__) if framework else bstack11l111_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡣࡪࡩࡳࡺ࠯ࡼࡿࠥ༓").format(
    __version__)
def bstack111lllll1l_opy_():
  global CONFIG
  global bstack1ll1l111ll_opy_
  if bool(CONFIG):
    return
  try:
    bstack111ll1ll11_opy_()
    logger.debug(bstack11l1l1l1l1_opy_.format(str(CONFIG)))
    bstack1ll1l111ll_opy_ = bstack11l111l1ll_opy_.configure_logger(CONFIG, bstack1ll1l111ll_opy_)
    bstack11l1lll1l_opy_()
  except Exception as e:
    logger.error(bstack11l111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࡸࡴ࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࠢ༔") + str(e))
    sys.exit(1)
  sys.excepthook = bstack11l1l11lll_opy_
  atexit.register(bstack11lllll11l_opy_)
  signal.signal(signal.SIGINT, bstack1ll1l1l111_opy_)
  signal.signal(signal.SIGTERM, bstack1ll1l1l111_opy_)
def bstack11l1l11lll_opy_(exctype, value, traceback):
  global bstack11l11l111_opy_
  try:
    for driver in bstack11l11l111_opy_:
      bstack11ll11lll1_opy_(driver, bstack11l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ༕"), bstack11l111_opy_ (u"࡙ࠧࡥࡴࡵ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣ༖") + str(value))
  except Exception:
    pass
  logger.info(bstack111llll1l_opy_)
  bstack111l111lll_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack111l111lll_opy_(message=bstack11l111_opy_ (u"࠭ࠧ༗"), bstack11111llll1_opy_ = False):
  global CONFIG
  bstack11llll1l1l_opy_ = bstack11l111_opy_ (u"ࠧࡨ࡮ࡲࡦࡦࡲࡅࡹࡥࡨࡴࡹ࡯࡯࡯༘ࠩ") if bstack11111llll1_opy_ else bstack11l111_opy_ (u"ࠨࡧࡵࡶࡴࡸ༙ࠧ")
  try:
    if message:
      bstack11ll1l111l_opy_ = {
        bstack11llll1l1l_opy_ : str(message)
      }
      bstack1lllll11l1_opy_(bstack11l1ll1l1l_opy_, CONFIG, bstack11ll1l111l_opy_)
    else:
      bstack1lllll11l1_opy_(bstack11l1ll1l1l_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1ll1l1111_opy_.format(str(e)))
def bstack11l11l111l_opy_(bstack111111llll_opy_, size):
  bstack1111l1l1l_opy_ = []
  while len(bstack111111llll_opy_) > size:
    bstack1l11l1l1l_opy_ = bstack111111llll_opy_[:size]
    bstack1111l1l1l_opy_.append(bstack1l11l1l1l_opy_)
    bstack111111llll_opy_ = bstack111111llll_opy_[size:]
  bstack1111l1l1l_opy_.append(bstack111111llll_opy_)
  return bstack1111l1l1l_opy_
def bstack1l11l1l11l_opy_(args):
  if bstack11l111_opy_ (u"ࠩ࠰ࡱࠬ༚") in args and bstack11l111_opy_ (u"ࠪࡴࡩࡨࠧ༛") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack1111llllll_opy_, stage=STAGE.bstack1lll111l1l_opy_)
def run_on_browserstack(bstack11l1l1lll1_opy_=None, bstack1l1ll11ll1_opy_=None, bstack111ll1lll_opy_=False):
  global CONFIG
  global bstack1111llll11_opy_
  global bstack11l11111l_opy_
  global bstack1l11111l11_opy_
  global bstack11111l11_opy_
  bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠫࠬ༜")
  bstack1ll11111l1_opy_(bstack11111l11ll_opy_, logger)
  if bstack11l1l1lll1_opy_ and isinstance(bstack11l1l1lll1_opy_, str):
    bstack11l1l1lll1_opy_ = eval(bstack11l1l1lll1_opy_)
  if bstack11l1l1lll1_opy_:
    CONFIG = bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬ༝")]
    bstack1111llll11_opy_ = bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ༞")]
    bstack11l11111l_opy_ = bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ༟")]
    bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ༠"), bstack11l11111l_opy_)
    bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༡")
  bstack11111l11_opy_.set_property(bstack11l111_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ༢"), uuid4().__str__())
  logger.info(bstack11l111_opy_ (u"ࠫࡘࡊࡋࠡࡴࡸࡲࠥࡹࡴࡢࡴࡷࡩࡩࠦࡷࡪࡶ࡫ࠤ࡮ࡪ࠺ࠡࠩ༣") + bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ༤")));
  logger.debug(bstack11l111_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤ࠾ࠩ༥") + bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ༦")))
  if not bstack111ll1lll_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack11l1lll111_opy_)
      return
    if sys.argv[1] == bstack11l111_opy_ (u"ࠨ࠯࠰ࡺࡪࡸࡳࡪࡱࡱࠫ༧") or sys.argv[1] == bstack11l111_opy_ (u"ࠩ࠰ࡺࠬ༨"):
      logger.info(bstack11l111_opy_ (u"ࠪࡆࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡓࡽࡹ࡮࡯࡯ࠢࡖࡈࡐࠦࡶࡼࡿࠪ༩").format(__version__))
      return
    if sys.argv[1] == bstack11l111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ༪"):
      bstack11llll111l_opy_()
      return
  args = sys.argv
  bstack111lllll1l_opy_()
  global bstack1lll1ll1l1_opy_
  global bstack111l11llll_opy_
  global bstack1l11ll11l1_opy_
  global bstack1ll1l11lll_opy_
  global bstack1l1l11llll_opy_
  global bstack111l1lll11_opy_
  global bstack1l1l1l1lll_opy_
  global bstack1l11l1l11_opy_
  global bstack11lllllll_opy_
  global bstack1ll1111l1_opy_
  global bstack11l1l11111_opy_
  bstack111l11llll_opy_ = len(CONFIG.get(bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ༫"), []))
  if not bstack111l11l11_opy_:
    if args[1] == bstack11l111_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭༬") or args[1] == bstack11l111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨ༭"):
      bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ༮")
      args = args[2:]
    elif args[1] == bstack11l111_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ༯"):
      bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ༰")
      args = args[2:]
    elif args[1] == bstack11l111_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ༱"):
      bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ༲")
      args = args[2:]
    elif args[1] == bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ༳"):
      bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ༴")
      args = args[2:]
    elif args[1] == bstack11l111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ༵"):
      bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ༶")
      args = args[2:]
    elif args[1] == bstack11l111_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧ༷ࠪ"):
      bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ༸")
      args = args[2:]
    else:
      if not bstack11l111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ༹") in CONFIG or str(CONFIG[bstack11l111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༺")]).lower() in [bstack11l111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༻"), bstack11l111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩ༼")]:
        bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༽")
        args = args[1:]
      elif str(CONFIG[bstack11l111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭༾")]).lower() == bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༿"):
        bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫཀ")
        args = args[1:]
      elif str(CONFIG[bstack11l111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩཁ")]).lower() == bstack11l111_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ག"):
        bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧགྷ")
        args = args[1:]
      elif str(CONFIG[bstack11l111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬང")]).lower() == bstack11l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪཅ"):
        bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫཆ")
        args = args[1:]
      elif str(CONFIG[bstack11l111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨཇ")]).lower() == bstack11l111_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭཈"):
        bstack111l11l11_opy_ = bstack11l111_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧཉ")
        args = args[1:]
      else:
        os.environ[bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪཊ")] = bstack111l11l11_opy_
        bstack1l1111l11_opy_(bstack111111l1l_opy_)
  os.environ[bstack11l111_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪཋ")] = bstack111l11l11_opy_
  bstack1l11111l11_opy_ = bstack111l11l11_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1l1l1l1l1l_opy_ = bstack11l1111l1l_opy_[bstack11l111_opy_ (u"ࠪࡔ࡞࡚ࡅࡔࡖ࠰ࡆࡉࡊࠧཌ")] if bstack111l11l11_opy_ == bstack11l111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫཌྷ") and bstack1ll11111ll_opy_() else bstack111l11l11_opy_
      bstack1l11ll1l11_opy_.invoke(Events.bstack111l1111l_opy_, bstack11ll1l1l1_opy_(
        sdk_version=__version__,
        path_config=bstack1lll11l111_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1l1l1l1l1l_opy_,
        frameworks=[bstack1l1l1l1l1l_opy_],
        framework_versions={
          bstack1l1l1l1l1l_opy_: bstack1ll1l11ll1_opy_(bstack11l111_opy_ (u"ࠬࡘ࡯ࡣࡱࡷࠫཎ") if bstack111l11l11_opy_ in [bstack11l111_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬཏ"), bstack11l111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ཐ"), bstack11l111_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩད")] else bstack111l11l11_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack11l111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦདྷ"), None):
        CONFIG[bstack11l111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧན")] = cli.config.get(bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨཔ"), None)
    except Exception as e:
      bstack1l11ll1l11_opy_.invoke(Events.bstack1l1ll11ll_opy_, e.__traceback__, 1)
    if bstack11l11111l_opy_:
      CONFIG[bstack11l111_opy_ (u"ࠧࡧࡰࡱࠤཕ")] = cli.config[bstack11l111_opy_ (u"ࠨࡡࡱࡲࠥབ")]
      logger.info(bstack1ll11ll111_opy_.format(CONFIG[bstack11l111_opy_ (u"ࠧࡢࡲࡳࠫབྷ")]))
  else:
    bstack1l11ll1l11_opy_.clear()
  global bstack11ll11llll_opy_
  global bstack11l1l111l_opy_
  if bstack11l1l1lll1_opy_:
    try:
      bstack1l1ll1ll1_opy_ = datetime.datetime.now()
      os.environ[bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪམ")] = bstack111l11l11_opy_
      bstack1lllll11l1_opy_(bstack11ll11ll1l_opy_, CONFIG)
      cli.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡴࡦ࡮ࡣࡹ࡫ࡳࡵࡡࡤࡸࡹ࡫࡭ࡱࡶࡨࡨࠧཙ"), datetime.datetime.now() - bstack1l1ll1ll1_opy_)
    except Exception as e:
      logger.debug(bstack1l1l1lll11_opy_.format(str(e)))
  global bstack1ll1l1lll1_opy_
  global bstack11l1lll11_opy_
  global bstack1ll1ll111l_opy_
  global bstack11111ll1l_opy_
  global bstack1l1l111l1_opy_
  global bstack1ll1llll11_opy_
  global bstack1l111llll1_opy_
  global bstack1l11ll1ll_opy_
  global bstack11ll1lllll_opy_
  global bstack1l1l11lll1_opy_
  global bstack1111111ll_opy_
  global bstack1l1l11l1l1_opy_
  global bstack11llllll1_opy_
  global bstack11l111111l_opy_
  global bstack1l111l1l1_opy_
  global bstack111ll1ll1_opy_
  global bstack11l1111111_opy_
  global bstack1ll1ll11l1_opy_
  global bstack1l11l1ll1_opy_
  global bstack11lll111l1_opy_
  global bstack1ll111l111_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1ll1l1lll1_opy_ = webdriver.Remote.__init__
    bstack11l1lll11_opy_ = WebDriver.quit
    bstack1l1l11l1l1_opy_ = WebDriver.close
    bstack1l111l1l1_opy_ = WebDriver.get
    bstack1ll111l111_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack11ll11llll_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1111ll1l1l_opy_
    bstack11l1l111l_opy_ = bstack1111ll1l1l_opy_()
  except Exception as e:
    pass
  try:
    global bstack1ll1lll111_opy_
    from QWeb.keywords import browser
    bstack1ll1lll111_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1lll1l1l1l_opy_(CONFIG) and bstack11l1ll1111_opy_():
    if bstack1ll1l11ll_opy_() < version.parse(bstack11l11ll111_opy_):
      logger.error(bstack11111l1lll_opy_.format(bstack1ll1l11ll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11l111_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫཚ")) and callable(getattr(RemoteConnection, bstack11l111_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬཛ"))):
          RemoteConnection._get_proxy_url = bstack1ll11ll11l_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack1ll11ll11l_opy_
      except Exception as e:
        logger.error(bstack11ll1l1ll1_opy_.format(str(e)))
  if not CONFIG.get(bstack11l111_opy_ (u"ࠬࡪࡩࡴࡣࡥࡰࡪࡇࡵࡵࡱࡆࡥࡵࡺࡵࡳࡧࡏࡳ࡬ࡹࠧཛྷ"), False) and not bstack11l1l1lll1_opy_:
    logger.info(bstack11lllll1l_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack11l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪཝ") in CONFIG and str(CONFIG[bstack11l111_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫཞ")]).lower() != bstack11l111_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧཟ"):
      bstack1ll1ll1ll_opy_()
    elif bstack111l11l11_opy_ != bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩའ") or (bstack111l11l11_opy_ == bstack11l111_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪཡ") and not bstack11l1l1lll1_opy_):
      bstack1ll1ll1111_opy_()
  if (bstack111l11l11_opy_ in [bstack11l111_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪར"), bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫལ"), bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧཤ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1l11llllll_opy_
        bstack1ll1llll11_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1l1111l1l1_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1l1l111l1_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1ll111ll1l_opy_ + str(e))
    except Exception as e:
      bstack11111l1l1_opy_(e, bstack1l1111l1l1_opy_)
    if bstack111l11l11_opy_ != bstack11l111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨཥ"):
      bstack111lllll11_opy_()
    bstack1ll1ll111l_opy_ = Output.start_test
    bstack11111ll1l_opy_ = Output.end_test
    bstack1l111llll1_opy_ = TestStatus.__init__
    bstack11ll1lllll_opy_ = pabot._run
    bstack1l1l11lll1_opy_ = QueueItem.__init__
    bstack1111111ll_opy_ = pabot._create_command_for_execution
    bstack1l11l1ll1_opy_ = pabot._report_results
  if bstack111l11l11_opy_ == bstack11l111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨས"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack11111l1l1_opy_(e, bstack1ll1111ll_opy_)
    bstack11llllll1_opy_ = Runner.run_hook
    bstack11l111111l_opy_ = Step.run
  if bstack111l11l11_opy_ == bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩཧ"):
    try:
      from _pytest.config import Config
      bstack11l1111111_opy_ = Config.getoption
      from _pytest import runner
      bstack1ll1ll11l1_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1lll11l11_opy_)
    try:
      from pytest_bdd import reporting
      bstack11lll111l1_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"ࠪࡔࡱ࡫ࡡࡴࡧࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡲࠤࡷࡻ࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࡶࠫཨ"))
  try:
    framework_name = bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪཀྵ") if bstack111l11l11_opy_ in [bstack11l111_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫཪ"), bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬཫ"), bstack11l111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨཬ")] else bstack1l1l1l1l11_opy_(bstack111l11l11_opy_)
    bstack1lllll1lll_opy_ = {
      bstack11l111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠩ཭"): bstack11l111_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵ࠯ࡦࡹࡨࡻ࡭ࡣࡧࡵࠫ཮") if bstack111l11l11_opy_ == bstack11l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ཯") and bstack1ll11111ll_opy_() else framework_name,
      bstack11l111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ཰"): bstack1ll1l11ll1_opy_(framework_name),
      bstack11l111_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰཱࠪ"): __version__,
      bstack11l111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡸࡷࡪࡪིࠧ"): bstack111l11l11_opy_
    }
    if bstack111l11l11_opy_ in bstack111ll11l11_opy_ + bstack1lll1l11ll_opy_:
      if bstack1111l11l_opy_.bstack111ll1l1ll_opy_(CONFIG):
        if bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹཱིࠧ") in CONFIG:
          os.environ[bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍུࠩ")] = os.getenv(bstack11l111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎཱུࠪ"), json.dumps(CONFIG[bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪྲྀ")]))
          CONFIG[bstack11l111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫཷ")].pop(bstack11l111_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪླྀ"), None)
          CONFIG[bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ཹ")].pop(bstack11l111_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩེࠬ"), None)
        bstack1lllll1lll_opy_[bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨཻ")] = {
          bstack11l111_opy_ (u"ࠩࡱࡥࡲ࡫ོࠧ"): bstack11l111_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱཽࠬ"),
          bstack11l111_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬཾ"): str(bstack1ll1l11ll_opy_())
        }
    if bstack111l11l11_opy_ not in [bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ཿ")] and not cli.is_running():
      bstack1ll111l11_opy_, bstack1l11lll1l1_opy_ = bstack1lll111l_opy_.launch(CONFIG, bstack1lllll1lll_opy_)
      if bstack1l11lll1l1_opy_.get(bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾྀ࠭")) is not None and bstack1111l11l_opy_.bstack1l11l111ll_opy_(CONFIG) is None:
        value = bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿཱྀࠧ")].get(bstack11l111_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩྂ"))
        if value is not None:
            CONFIG[bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩྃ")] = value
        else:
          logger.debug(bstack11l111_opy_ (u"ࠥࡒࡴࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡤࡢࡶࡤࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡲࡦࡵࡳࡳࡳࡹࡥ྄ࠣ"))
  except Exception as e:
    logger.debug(bstack1lllllll1l_opy_.format(bstack11l111_opy_ (u"࡙ࠫ࡫ࡳࡵࡊࡸࡦࠬ྅"), str(e)))
  if bstack111l11l11_opy_ == bstack11l111_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ྆"):
    bstack1l11ll11l1_opy_ = True
    if bstack11l1l1lll1_opy_ and bstack111ll1lll_opy_:
      bstack111l1lll11_opy_ = CONFIG.get(bstack11l111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ྇"), {}).get(bstack11l111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩྈ"))
      bstack11llll111_opy_(bstack111l1111l1_opy_)
    elif bstack11l1l1lll1_opy_:
      bstack111l1lll11_opy_ = CONFIG.get(bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬྉ"), {}).get(bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫྊ"))
      global bstack11l11l111_opy_
      try:
        if bstack1l11l1l11l_opy_(bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྋ")]) and multiprocessing.current_process().name == bstack11l111_opy_ (u"ࠫ࠵࠭ྌ"):
          bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྍ")].remove(bstack11l111_opy_ (u"࠭࠭࡮ࠩྎ"))
          bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྏ")].remove(bstack11l111_opy_ (u"ࠨࡲࡧࡦࠬྐ"))
          bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྑ")] = bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྒ")][0]
          with open(bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྒྷ")], bstack11l111_opy_ (u"ࠬࡸࠧྔ")) as f:
            file_content = f.read()
          bstack111lll11ll_opy_ = bstack11l111_opy_ (u"ࠨࠢࠣࡨࡵࡳࡲࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡤ࡬ࠢ࡬ࡱࡵࡵࡲࡵࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩࡀࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡺࡦࠪࡾࢁ࠮ࡁࠠࡧࡴࡲࡱࠥࡶࡤࡣࠢ࡬ࡱࡵࡵࡲࡵࠢࡓࡨࡧࡁࠠࡰࡩࡢࡨࡧࠦ࠽ࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱ࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡫ࡦࠡ࡯ࡲࡨࡤࡨࡲࡦࡣ࡮ࠬࡸ࡫࡬ࡧ࠮ࠣࡥࡷ࡭ࠬࠡࡶࡨࡱࡵࡵࡲࡢࡴࡼࠤࡂࠦ࠰ࠪ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡵࡽ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡡࡳࡩࠣࡁࠥࡹࡴࡳࠪ࡬ࡲࡹ࠮ࡡࡳࡩࠬ࠯࠶࠶ࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡥࡹࡥࡨࡴࡹࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡤࡷࠥ࡫࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡲࡤࡷࡸࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡴ࡭࡟ࡥࡤࠫࡷࡪࡲࡦ࠭ࡣࡵ࡫࠱ࡺࡥ࡮ࡲࡲࡶࡦࡸࡹࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡖࡤࡣ࠰ࡧࡳࡤࡨࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࡵࡩࡦࡱࠠ࠾ࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡒࡧࡦ࠭࠯࠮ࡴࡧࡷࡣࡹࡸࡡࡤࡧࠫ࠭ࡡࡴࠢࠣࠤྕ").format(str(bstack11l1l1lll1_opy_))
          bstack1l111l1111_opy_ = bstack111lll11ll_opy_ + file_content
          bstack111l1l111l_opy_ = bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྖ")] + bstack11l111_opy_ (u"ࠨࡡࡥࡷࡹࡧࡣ࡬ࡡࡷࡩࡲࡶ࠮ࡱࡻࠪྗ")
          with open(bstack111l1l111l_opy_, bstack11l111_opy_ (u"ࠩࡺࠫ྘")):
            pass
          with open(bstack111l1l111l_opy_, bstack11l111_opy_ (u"ࠥࡻ࠰ࠨྙ")) as f:
            f.write(bstack1l111l1111_opy_)
          import subprocess
          process_data = subprocess.run([bstack11l111_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࠦྚ"), bstack111l1l111l_opy_])
          if os.path.exists(bstack111l1l111l_opy_):
            os.unlink(bstack111l1l111l_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack1l11l1l11l_opy_(bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྛ")]):
            bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྜ")].remove(bstack11l111_opy_ (u"ࠧ࠮࡯ࠪྜྷ"))
            bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྞ")].remove(bstack11l111_opy_ (u"ࠩࡳࡨࡧ࠭ྟ"))
            bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྠ")] = bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྡ")][0]
          bstack11llll111_opy_(bstack111l1111l1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྡྷ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11l111_opy_ (u"࠭࡟ࡠࡰࡤࡱࡪࡥ࡟ࠨྣ")] = bstack11l111_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩྤ")
          mod_globals[bstack11l111_opy_ (u"ࠨࡡࡢࡪ࡮ࡲࡥࡠࡡࠪྥ")] = os.path.abspath(bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྦ")])
          exec(open(bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྦྷ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11l111_opy_ (u"ࠫࡈࡧࡵࡨࡪࡷࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠫྨ").format(str(e)))
          for driver in bstack11l11l111_opy_:
            bstack1l1ll11ll1_opy_.append({
              bstack11l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪྩ"): bstack11l1l1lll1_opy_[bstack11l111_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྪ")],
              bstack11l111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ྫ"): str(e),
              bstack11l111_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧྫྷ"): multiprocessing.current_process().name
            })
            bstack11ll11lll1_opy_(driver, bstack11l111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩྭ"), bstack11l111_opy_ (u"ࠥࡗࡪࡹࡳࡪࡱࡱࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨྮ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack11l11l111_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11l11111l_opy_, CONFIG, logger)
      bstack111lllll1_opy_()
      bstack11ll11ll1_opy_()
      percy.bstack1111l11lll_opy_()
      bstack111111l1_opy_ = {
        bstack11l111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྯ"): args[0],
        bstack11l111_opy_ (u"ࠬࡉࡏࡏࡈࡌࡋࠬྰ"): CONFIG,
        bstack11l111_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧྱ"): bstack1111llll11_opy_,
        bstack11l111_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩྲ"): bstack11l11111l_opy_
      }
      if bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫླ") in CONFIG:
        bstack111111111_opy_ = bstack11l1l1111_opy_(args, logger, CONFIG, bstack11l1111l11_opy_, bstack111l11llll_opy_)
        bstack1l11l1l11_opy_ = bstack111111111_opy_.bstack1llll1ll1_opy_(run_on_browserstack, bstack111111l1_opy_, bstack1l11l1l11l_opy_(args))
      else:
        if bstack1l11l1l11l_opy_(args):
          bstack111111l1_opy_[bstack11l111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྴ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack111111l1_opy_,))
          test.start()
          test.join()
        else:
          bstack11llll111_opy_(bstack111l1111l1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11l111_opy_ (u"ࠪࡣࡤࡴࡡ࡮ࡧࡢࡣࠬྵ")] = bstack11l111_opy_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ྶ")
          mod_globals[bstack11l111_opy_ (u"ࠬࡥ࡟ࡧ࡫࡯ࡩࡤࡥࠧྷ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack111l11l11_opy_ == bstack11l111_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬྸ") or bstack111l11l11_opy_ == bstack11l111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ྐྵ"):
    percy.init(bstack11l11111l_opy_, CONFIG, logger)
    percy.bstack1111l11lll_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack11111l1l1_opy_(e, bstack1l1111l1l1_opy_)
    bstack111lllll1_opy_()
    bstack11llll111_opy_(bstack1l1ll1ll11_opy_)
    if bstack11l1111l11_opy_:
      bstack11l1lll11l_opy_(bstack1l1ll1ll11_opy_, args)
      if bstack11l111_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ྺ") in args:
        i = args.index(bstack11l111_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧྻ"))
        args.pop(i)
        args.pop(i)
      if bstack11l111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ྼ") not in CONFIG:
        CONFIG[bstack11l111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ྽")] = [{}]
        bstack111l11llll_opy_ = 1
      if bstack1lll1ll1l1_opy_ == 0:
        bstack1lll1ll1l1_opy_ = 1
      args.insert(0, str(bstack1lll1ll1l1_opy_))
      args.insert(0, str(bstack11l111_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪ྾")))
    if bstack1lll111l_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1l1lllll1_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack111ll11ll1_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11l111_opy_ (u"ࠨࡒࡐࡄࡒࡘࡤࡕࡐࡕࡋࡒࡒࡘࠨ྿"),
        ).parse_args(bstack1l1lllll1_opy_)
        bstack11l1l11l1l_opy_ = args.index(bstack1l1lllll1_opy_[0]) if len(bstack1l1lllll1_opy_) > 0 else len(args)
        args.insert(bstack11l1l11l1l_opy_, str(bstack11l111_opy_ (u"ࠧ࠮࠯࡯࡭ࡸࡺࡥ࡯ࡧࡵࠫ࿀")))
        args.insert(bstack11l1l11l1l_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡴࡲࡦࡴࡺ࡟࡭࡫ࡶࡸࡪࡴࡥࡳ࠰ࡳࡽࠬ࿁"))))
        if bstack1lll1l1ll_opy_.bstack1lll111l1_opy_(CONFIG):
          args.insert(bstack11l1l11l1l_opy_, str(bstack11l111_opy_ (u"ࠩ࠰࠱ࡱ࡯ࡳࡵࡧࡱࡩࡷ࠭࿂")))
          args.insert(bstack11l1l11l1l_opy_ + 1, str(bstack11l111_opy_ (u"ࠪࡖࡪࡺࡲࡺࡈࡤ࡭ࡱ࡫ࡤ࠻ࡽࢀࠫ࿃").format(bstack1lll1l1ll_opy_.bstack1lllll1l1_opy_(CONFIG))))
        if bstack1l1lll1ll1_opy_(os.environ.get(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠩ࿄"))) and str(os.environ.get(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠩ࿅"), bstack11l111_opy_ (u"࠭࡮ࡶ࡮࡯࿆ࠫ"))) != bstack11l111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ࿇"):
          for bstack11l11ll11_opy_ in bstack111ll11ll1_opy_:
            args.remove(bstack11l11ll11_opy_)
          test_files = os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬ࿈")).split(bstack11l111_opy_ (u"ࠩ࠯ࠫ࿉"))
          for bstack11ll1l1lll_opy_ in test_files:
            args.append(bstack11ll1l1lll_opy_)
      except Exception as e:
        logger.error(bstack11l111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡣࡷࡸࡦࡩࡨࡪࡰࡪࠤࡱ࡯ࡳࡵࡧࡱࡩࡷࠦࡦࡰࡴࠣࡿࢂ࠴ࠠࡆࡴࡵࡳࡷࠦ࠭ࠡࡽࢀࠦ࿊").format(bstack11l111l111_opy_, e))
    pabot.main(args)
  elif bstack111l11l11_opy_ == bstack11l111_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬ࿋"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack11111l1l1_opy_(e, bstack1l1111l1l1_opy_)
    for a in args:
      if bstack11l111_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫ࿌") in a:
        bstack1l1l11llll_opy_ = int(a.split(bstack11l111_opy_ (u"࠭࠺ࠨ࿍"))[1])
      if bstack11l111_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫ࿎") in a:
        bstack111l1lll11_opy_ = str(a.split(bstack11l111_opy_ (u"ࠨ࠼ࠪ࿏"))[1])
      if bstack11l111_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡅࡏࡍࡆࡘࡇࡔࠩ࿐") in a:
        bstack1l1l1l1lll_opy_ = str(a.split(bstack11l111_opy_ (u"ࠪ࠾ࠬ࿑"))[1])
    bstack1111l1llll_opy_ = None
    if bstack11l111_opy_ (u"ࠫ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠪ࿒") in args:
      i = args.index(bstack11l111_opy_ (u"ࠬ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠫ࿓"))
      args.pop(i)
      bstack1111l1llll_opy_ = args.pop(i)
    if bstack1111l1llll_opy_ is not None:
      global bstack11lll11l1_opy_
      bstack11lll11l1_opy_ = bstack1111l1llll_opy_
    bstack11llll111_opy_(bstack1l1ll1ll11_opy_)
    run_cli(args)
    if bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡥࡳࡴࡲࡶࡤࡲࡩࡴࡶࠪ࿔") in multiprocessing.current_process().__dict__.keys():
      for bstack11ll1ll11_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l1ll11ll1_opy_.append(bstack11ll1ll11_opy_)
  elif bstack111l11l11_opy_ == bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ࿕"):
    bstack111l11111_opy_ = bstack111lll11_opy_(args, logger, CONFIG, bstack11l1111l11_opy_)
    bstack111l11111_opy_.bstack1lll1l1l1_opy_()
    bstack111lllll1_opy_()
    bstack1ll1l11lll_opy_ = True
    bstack1ll1111l1_opy_ = bstack111l11111_opy_.bstack1llll111l_opy_()
    bstack111l11111_opy_.bstack111111l1_opy_(bstack1ll111lll1_opy_)
    bstack111l11111_opy_.bstack1111llll_opy_()
    bstack1l11111ll1_opy_(bstack111l11l11_opy_, CONFIG, bstack111l11111_opy_.bstack1lllll11l_opy_())
    bstack11l1ll111_opy_ = bstack111l11111_opy_.bstack1llll1ll1_opy_(bstack11llllllll_opy_, {
      bstack11l111_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩ࿖"): bstack1111llll11_opy_,
      bstack11l111_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ࿗"): bstack11l11111l_opy_,
      bstack11l111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭࿘"): bstack11l1111l11_opy_
    })
    try:
      bstack1ll111lll_opy_, bstack11ll1llll_opy_ = map(list, zip(*bstack11l1ll111_opy_))
      bstack11lllllll_opy_ = bstack1ll111lll_opy_[0]
      for status_code in bstack11ll1llll_opy_:
        if status_code != 0:
          bstack11l1l11111_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11l111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡣࡹࡩࠥ࡫ࡲࡳࡱࡵࡷࠥࡧ࡮ࡥࠢࡶࡸࡦࡺࡵࡴࠢࡦࡳࡩ࡫࠮ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࠿ࠦࡻࡾࠤ࿙").format(str(e)))
  elif bstack111l11l11_opy_ == bstack11l111_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ࿚"):
    try:
      from behave.__main__ import main as bstack1ll11llll_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack11111l1l1_opy_(e, bstack1ll1111ll_opy_)
    bstack111lllll1_opy_()
    bstack1ll1l11lll_opy_ = True
    bstack1lll1l111_opy_ = 1
    if bstack11l111_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭࿛") in CONFIG:
      bstack1lll1l111_opy_ = CONFIG[bstack11l111_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ࿜")]
    if bstack11l111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ࿝") in CONFIG:
      bstack11l111llll_opy_ = int(bstack1lll1l111_opy_) * int(len(CONFIG[bstack11l111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ࿞")]))
    else:
      bstack11l111llll_opy_ = int(bstack1lll1l111_opy_)
    config = Configuration(args)
    bstack1lllll11ll_opy_ = config.paths
    if len(bstack1lllll11ll_opy_) == 0:
      import glob
      pattern = bstack11l111_opy_ (u"ࠪ࠮࠯࠵ࠪ࠯ࡨࡨࡥࡹࡻࡲࡦࠩ࿟")
      bstack1l11111l1_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1l11111l1_opy_)
      config = Configuration(args)
      bstack1lllll11ll_opy_ = config.paths
    bstack1llll1l11_opy_ = [os.path.normpath(item) for item in bstack1lllll11ll_opy_]
    bstack1l1l11l11l_opy_ = [os.path.normpath(item) for item in args]
    bstack1111ll1lll_opy_ = [item for item in bstack1l1l11l11l_opy_ if item not in bstack1llll1l11_opy_]
    import platform as pf
    if pf.system().lower() == bstack11l111_opy_ (u"ࠫࡼ࡯࡮ࡥࡱࡺࡷࠬ࿠"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1llll1l11_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1ll111l1l1_opy_)))
                    for bstack1ll111l1l1_opy_ in bstack1llll1l11_opy_]
    bstack1llll11ll_opy_ = []
    for spec in bstack1llll1l11_opy_:
      bstack1111lll1_opy_ = []
      bstack1111lll1_opy_ += bstack1111ll1lll_opy_
      bstack1111lll1_opy_.append(spec)
      bstack1llll11ll_opy_.append(bstack1111lll1_opy_)
    execution_items = []
    for bstack1111lll1_opy_ in bstack1llll11ll_opy_:
      if bstack11l111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ࿡") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack11l111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ࿢")]):
          item = {}
          item[bstack11l111_opy_ (u"ࠧࡢࡴࡪࠫ࿣")] = bstack11l111_opy_ (u"ࠨࠢࠪ࿤").join(bstack1111lll1_opy_)
          item[bstack11l111_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ࿥")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack11l111_opy_ (u"ࠪࡥࡷ࡭ࠧ࿦")] = bstack11l111_opy_ (u"ࠫࠥ࠭࿧").join(bstack1111lll1_opy_)
        item[bstack11l111_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ࿨")] = 0
        execution_items.append(item)
    bstack111l1l1ll_opy_ = bstack11l11l111l_opy_(execution_items, bstack11l111llll_opy_)
    for execution_item in bstack111l1l1ll_opy_:
      bstack1llll1111_opy_ = []
      for item in execution_item:
        bstack1llll1111_opy_.append(bstack11lll1l1l_opy_(name=str(item[bstack11l111_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ࿩")]),
                                             target=bstack1l1l1l11l_opy_,
                                             args=(item[bstack11l111_opy_ (u"ࠧࡢࡴࡪࠫ࿪")],)))
      for t in bstack1llll1111_opy_:
        t.start()
      for t in bstack1llll1111_opy_:
        t.join()
  else:
    bstack1l1111l11_opy_(bstack111111l1l_opy_)
  if not bstack11l1l1lll1_opy_:
    bstack11lll1lll_opy_()
    if(bstack111l11l11_opy_ in [bstack11l111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ࿫"), bstack11l111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ࿬")]):
      bstack111lll11l1_opy_()
  bstack11l111l1ll_opy_.bstack11l1ll1lll_opy_()
def browserstack_initialize(bstack1llll1l1ll_opy_=None):
  logger.info(bstack11l111_opy_ (u"ࠪࡖࡺࡴ࡮ࡪࡰࡪࠤࡘࡊࡋࠡࡹ࡬ࡸ࡭ࠦࡡࡳࡩࡶ࠾ࠥ࠭࿭") + str(bstack1llll1l1ll_opy_))
  run_on_browserstack(bstack1llll1l1ll_opy_, None, True)
@measure(event_name=EVENTS.bstack11l111ll1_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack11lll1lll_opy_():
  global CONFIG
  global bstack1l11111l11_opy_
  global bstack11l1l11111_opy_
  global bstack1ll111l11l_opy_
  global bstack11111l11_opy_
  bstack1ll1ll1l1_opy_.bstack1111llll1l_opy_()
  if cli.is_running():
    bstack1l11ll1l11_opy_.invoke(Events.bstack1ll1l1111l_opy_)
  else:
    bstack1111ll1l_opy_ = bstack1lll1l1ll_opy_.bstack111l11l1_opy_(config=CONFIG)
    bstack1111ll1l_opy_.bstack111llll1l1_opy_(CONFIG)
  if bstack1l11111l11_opy_ == bstack11l111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ࿮"):
    if not cli.is_enabled(CONFIG):
      bstack1lll111l_opy_.stop()
  else:
    bstack1lll111l_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1lll1lll_opy_.bstack1l1l1ll1l1_opy_()
  if bstack11l111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ࿯") in CONFIG and str(CONFIG[bstack11l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ࿰")]).lower() != bstack11l111_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭࿱"):
    hashed_id, bstack1l1111ll11_opy_ = bstack1111l111ll_opy_()
  else:
    hashed_id, bstack1l1111ll11_opy_ = get_build_link()
  bstack1ll1l1llll_opy_(hashed_id)
  logger.info(bstack11l111_opy_ (u"ࠨࡕࡇࡏࠥࡸࡵ࡯ࠢࡨࡲࡩ࡫ࡤࠡࡨࡲࡶࠥ࡯ࡤ࠻ࠩ࿲") + bstack11111l11_opy_.get_property(bstack11l111_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ࿳"), bstack11l111_opy_ (u"ࠪࠫ࿴")) + bstack11l111_opy_ (u"ࠫ࠱ࠦࡴࡦࡵࡷ࡬ࡺࡨࠠࡪࡦ࠽ࠤࠬ࿵") + os.getenv(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ࿶"), bstack11l111_opy_ (u"࠭ࠧ࿷")))
  if hashed_id is not None and bstack1ll1l111l1_opy_() != -1:
    sessions = bstack1l11lll1ll_opy_(hashed_id)
    bstack11111ll1l1_opy_(sessions, bstack1l1111ll11_opy_)
  if bstack1l11111l11_opy_ == bstack11l111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ࿸") and bstack11l1l11111_opy_ != 0:
    sys.exit(bstack11l1l11111_opy_)
  if bstack1l11111l11_opy_ == bstack11l111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ࿹") and bstack1ll111l11l_opy_ != 0:
    sys.exit(bstack1ll111l11l_opy_)
def bstack1ll1l1llll_opy_(new_id):
    global bstack1l11l1lll_opy_
    bstack1l11l1lll_opy_ = new_id
def bstack1l1l1l1l11_opy_(bstack111l111ll1_opy_):
  if bstack111l111ll1_opy_:
    return bstack111l111ll1_opy_.capitalize()
  else:
    return bstack11l111_opy_ (u"ࠩࠪ࿺")
@measure(event_name=EVENTS.bstack1l111lll1l_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack11ll11l11l_opy_(bstack1l111111l_opy_):
  if bstack11l111_opy_ (u"ࠪࡲࡦࡳࡥࠨ࿻") in bstack1l111111l_opy_ and bstack1l111111l_opy_[bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ࿼")] != bstack11l111_opy_ (u"ࠬ࠭࿽"):
    return bstack1l111111l_opy_[bstack11l111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ࿾")]
  else:
    bstack11l111l1l_opy_ = bstack11l111_opy_ (u"ࠢࠣ࿿")
    if bstack11l111_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨက") in bstack1l111111l_opy_ and bstack1l111111l_opy_[bstack11l111_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩခ")] != None:
      bstack11l111l1l_opy_ += bstack1l111111l_opy_[bstack11l111_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪဂ")] + bstack11l111_opy_ (u"ࠦ࠱ࠦࠢဃ")
      if bstack1l111111l_opy_[bstack11l111_opy_ (u"ࠬࡵࡳࠨင")] == bstack11l111_opy_ (u"ࠨࡩࡰࡵࠥစ"):
        bstack11l111l1l_opy_ += bstack11l111_opy_ (u"ࠢࡪࡑࡖࠤࠧဆ")
      bstack11l111l1l_opy_ += (bstack1l111111l_opy_[bstack11l111_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬဇ")] or bstack11l111_opy_ (u"ࠩࠪဈ"))
      return bstack11l111l1l_opy_
    else:
      bstack11l111l1l_opy_ += bstack1l1l1l1l11_opy_(bstack1l111111l_opy_[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫဉ")]) + bstack11l111_opy_ (u"ࠦࠥࠨည") + (
              bstack1l111111l_opy_[bstack11l111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧဋ")] or bstack11l111_opy_ (u"࠭ࠧဌ")) + bstack11l111_opy_ (u"ࠢ࠭ࠢࠥဍ")
      if bstack1l111111l_opy_[bstack11l111_opy_ (u"ࠨࡱࡶࠫဎ")] == bstack11l111_opy_ (u"ࠤ࡚࡭ࡳࡪ࡯ࡸࡵࠥဏ"):
        bstack11l111l1l_opy_ += bstack11l111_opy_ (u"࡛ࠥ࡮ࡴࠠࠣတ")
      bstack11l111l1l_opy_ += bstack1l111111l_opy_[bstack11l111_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨထ")] or bstack11l111_opy_ (u"ࠬ࠭ဒ")
      return bstack11l111l1l_opy_
@measure(event_name=EVENTS.bstack1ll11l11l_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack11l11llll_opy_(bstack11lllll111_opy_):
  if bstack11lllll111_opy_ == bstack11l111_opy_ (u"ࠨࡤࡰࡰࡨࠦဓ"):
    return bstack11l111_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡪࡶࡪ࡫࡮࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡪࡶࡪ࡫࡮ࠣࡀࡆࡳࡲࡶ࡬ࡦࡶࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪန")
  elif bstack11lllll111_opy_ == bstack11l111_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣပ"):
    return bstack11l111_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡷ࡫ࡤ࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡵࡩࡩࠨ࠾ࡇࡣ࡬ࡰࡪࡪ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬဖ")
  elif bstack11lllll111_opy_ == bstack11l111_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥဗ"):
    return bstack11l111_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡧࡳࡧࡨࡲࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡧࡳࡧࡨࡲࠧࡄࡐࡢࡵࡶࡩࡩࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫဘ")
  elif bstack11lllll111_opy_ == bstack11l111_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦမ"):
    return bstack11l111_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡴࡨࡨࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡲࡦࡦࠥࡂࡊࡸࡲࡰࡴ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨယ")
  elif bstack11lllll111_opy_ == bstack11l111_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣရ"):
    return bstack11l111_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࠧࡪ࡫ࡡ࠴࠴࠹࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࠩࡥࡦࡣ࠶࠶࠻ࠨ࠾ࡕ࡫ࡰࡩࡴࡻࡴ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭လ")
  elif bstack11lllll111_opy_ == bstack11l111_opy_ (u"ࠤࡵࡹࡳࡴࡩ࡯ࡩࠥဝ"):
    return bstack11l111_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡨ࡬ࡢࡥ࡮࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡨ࡬ࡢࡥ࡮ࠦࡃࡘࡵ࡯ࡰ࡬ࡲ࡬ࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫသ")
  else:
    return bstack11l111_opy_ (u"ࠫࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡣ࡮ࡤࡧࡰࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡣ࡮ࡤࡧࡰࠨ࠾ࠨဟ") + bstack1l1l1l1l11_opy_(
      bstack11lllll111_opy_) + bstack11l111_opy_ (u"ࠬࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫဠ")
def bstack1l1111l1l_opy_(session):
  return bstack11l111_opy_ (u"࠭࠼ࡵࡴࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡶࡴࡽࠢ࠿࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠣࡷࡪࡹࡳࡪࡱࡱ࠱ࡳࡧ࡭ࡦࠤࡁࡀࡦࠦࡨࡳࡧࡩࡁࠧࢁࡽࠣࠢࡷࡥࡷ࡭ࡥࡵ࠿ࠥࡣࡧࡲࡡ࡯࡭ࠥࡂࢀࢃ࠼࠰ࡣࡁࡀ࠴ࡺࡤ࠿ࡽࢀࡿࢂࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽࠱ࡷࡶࡃ࠭အ").format(
    session[bstack11l111_opy_ (u"ࠧࡱࡷࡥࡰ࡮ࡩ࡟ࡶࡴ࡯ࠫဢ")], bstack11ll11l11l_opy_(session), bstack11l11llll_opy_(session[bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡶࡤࡸࡺࡹࠧဣ")]),
    bstack11l11llll_opy_(session[bstack11l111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩဤ")]),
    bstack1l1l1l1l11_opy_(session[bstack11l111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࠫဥ")] or session[bstack11l111_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫဦ")] or bstack11l111_opy_ (u"ࠬ࠭ဧ")) + bstack11l111_opy_ (u"ࠨࠠࠣဨ") + (session[bstack11l111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩဩ")] or bstack11l111_opy_ (u"ࠨࠩဪ")),
    session[bstack11l111_opy_ (u"ࠩࡲࡷࠬါ")] + bstack11l111_opy_ (u"ࠥࠤࠧာ") + session[bstack11l111_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨိ")], session[bstack11l111_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧီ")] or bstack11l111_opy_ (u"࠭ࠧု"),
    session[bstack11l111_opy_ (u"ࠧࡤࡴࡨࡥࡹ࡫ࡤࡠࡣࡷࠫူ")] if session[bstack11l111_opy_ (u"ࠨࡥࡵࡩࡦࡺࡥࡥࡡࡤࡸࠬေ")] else bstack11l111_opy_ (u"ࠩࠪဲ"))
@measure(event_name=EVENTS.bstack11ll111l1_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def bstack11111ll1l1_opy_(sessions, bstack1l1111ll11_opy_):
  try:
    bstack11llll1111_opy_ = bstack11l111_opy_ (u"ࠥࠦဳ")
    if not os.path.exists(bstack11lll11l11_opy_):
      os.mkdir(bstack11lll11l11_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l111_opy_ (u"ࠫࡦࡹࡳࡦࡶࡶ࠳ࡷ࡫ࡰࡰࡴࡷ࠲࡭ࡺ࡭࡭ࠩဴ")), bstack11l111_opy_ (u"ࠬࡸࠧဵ")) as f:
      bstack11llll1111_opy_ = f.read()
    bstack11llll1111_opy_ = bstack11llll1111_opy_.replace(bstack11l111_opy_ (u"࠭ࡻࠦࡔࡈࡗ࡚ࡒࡔࡔࡡࡆࡓ࡚ࡔࡔࠦࡿࠪံ"), str(len(sessions)))
    bstack11llll1111_opy_ = bstack11llll1111_opy_.replace(bstack11l111_opy_ (u"ࠧࡼࠧࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠪࢃ့ࠧ"), bstack1l1111ll11_opy_)
    bstack11llll1111_opy_ = bstack11llll1111_opy_.replace(bstack11l111_opy_ (u"ࠨࡽࠨࡆ࡚ࡏࡌࡅࡡࡑࡅࡒࡋࠥࡾࠩး"),
                                              sessions[0].get(bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡰࡤࡱࡪ္࠭")) if sessions[0] else bstack11l111_opy_ (u"်ࠪࠫ"))
    with open(os.path.join(bstack11lll11l11_opy_, bstack11l111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡶࡪࡶ࡯ࡳࡶ࠱࡬ࡹࡳ࡬ࠨျ")), bstack11l111_opy_ (u"ࠬࡽࠧြ")) as stream:
      stream.write(bstack11llll1111_opy_.split(bstack11l111_opy_ (u"࠭ࡻࠦࡕࡈࡗࡘࡏࡏࡏࡕࡢࡈࡆ࡚ࡁࠦࡿࠪွ"))[0])
      for session in sessions:
        stream.write(bstack1l1111l1l_opy_(session))
      stream.write(bstack11llll1111_opy_.split(bstack11l111_opy_ (u"ࠧࡼࠧࡖࡉࡘ࡙ࡉࡐࡐࡖࡣࡉࡇࡔࡂࠧࢀࠫှ"))[1])
    logger.info(bstack11l111_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵࡧࡧࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡦࡺ࡯࡬ࡥࠢࡤࡶࡹ࡯ࡦࡢࡥࡷࡷࠥࡧࡴࠡࡽࢀࠫဿ").format(bstack11lll11l11_opy_));
  except Exception as e:
    logger.debug(bstack1llll1ll11_opy_.format(str(e)))
def bstack1l11lll1ll_opy_(hashed_id):
  global CONFIG
  try:
    bstack1l1ll1ll1_opy_ = datetime.datetime.now()
    host = bstack11l111_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠭ࡤ࡮ࡲࡹࡩ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ၀") if bstack11l111_opy_ (u"ࠪࡥࡵࡶࠧ၁") in CONFIG else bstack11l111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡧࡰࡪ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ၂")
    user = CONFIG[bstack11l111_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ၃")]
    key = CONFIG[bstack11l111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ၄")]
    bstack11l1l1l1ll_opy_ = bstack11l111_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭၅") if bstack11l111_opy_ (u"ࠨࡣࡳࡴࠬ၆") in CONFIG else (bstack11l111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭၇") if CONFIG.get(bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧ၈")) else bstack11l111_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭၉"))
    host = bstack111111ll11_opy_(cli.config, [bstack11l111_opy_ (u"ࠧࡧࡰࡪࡵࠥ၊"), bstack11l111_opy_ (u"ࠨࡡࡱࡲࡄࡹࡹࡵ࡭ࡢࡶࡨࠦ။"), bstack11l111_opy_ (u"ࠢࡢࡲ࡬ࠦ၌")], host) if bstack11l111_opy_ (u"ࠨࡣࡳࡴࠬ၍") in CONFIG else bstack111111ll11_opy_(cli.config, [bstack11l111_opy_ (u"ࠤࡤࡴ࡮ࡹࠢ၎"), bstack11l111_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࠧ၏"), bstack11l111_opy_ (u"ࠦࡦࡶࡩࠣၐ")], host)
    url = bstack11l111_opy_ (u"ࠬࢁࡽ࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃ࠯ࡴࡧࡶࡷ࡮ࡵ࡮ࡴ࠰࡭ࡷࡴࡴࠧၑ").format(host, bstack11l1l1l1ll_opy_, hashed_id)
    headers = {
      bstack11l111_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬၒ"): bstack11l111_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪၓ"),
    }
    proxies = bstack11l11l1l11_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠣࡪࡷࡸࡵࡀࡧࡦࡶࡢࡷࡪࡹࡳࡪࡱࡱࡷࡤࡲࡩࡴࡶࠥၔ"), datetime.datetime.now() - bstack1l1ll1ll1_opy_)
      return list(map(lambda session: session[bstack11l111_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࠧၕ")], response.json()))
  except Exception as e:
    logger.debug(bstack11111l111l_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack1l1lll1l1l_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def get_build_link():
  global CONFIG
  global bstack1l11l1lll_opy_
  try:
    if bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ၖ") in CONFIG:
      bstack1l1ll1ll1_opy_ = datetime.datetime.now()
      host = bstack11l111_opy_ (u"ࠫࡦࡶࡩ࠮ࡥ࡯ࡳࡺࡪࠧၗ") if bstack11l111_opy_ (u"ࠬࡧࡰࡱࠩၘ") in CONFIG else bstack11l111_opy_ (u"࠭ࡡࡱ࡫ࠪၙ")
      user = CONFIG[bstack11l111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩၚ")]
      key = CONFIG[bstack11l111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫၛ")]
      bstack11l1l1l1ll_opy_ = bstack11l111_opy_ (u"ࠩࡤࡴࡵ࠳ࡡࡶࡶࡲࡱࡦࡺࡥࠨၜ") if bstack11l111_opy_ (u"ࠪࡥࡵࡶࠧၝ") in CONFIG else bstack11l111_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ၞ")
      url = bstack11l111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡻࡾ࠼ࡾࢁࡅࢁࡽ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠮࡫ࡵࡲࡲࠬၟ").format(user, key, host, bstack11l1l1l1ll_opy_)
      if cli.is_enabled(CONFIG):
        bstack1l1111ll11_opy_, hashed_id = cli.bstack1l11lllll1_opy_()
        logger.info(bstack1111l11l11_opy_.format(bstack1l1111ll11_opy_))
        return [hashed_id, bstack1l1111ll11_opy_]
      else:
        headers = {
          bstack11l111_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡵࡻࡳࡩࠬၠ"): bstack11l111_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪၡ"),
        }
        if bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪၢ") in CONFIG:
          params = {bstack11l111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧၣ"): CONFIG[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ၤ")], bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧၥ"): CONFIG[bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧၦ")]}
        else:
          params = {bstack11l111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫၧ"): CONFIG[bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪၨ")]}
        proxies = bstack11l11l1l11_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack1l11ll1111_opy_ = response.json()[0][bstack11l111_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡨࡵࡪ࡮ࡧࠫၩ")]
          if bstack1l11ll1111_opy_:
            bstack1l1111ll11_opy_ = bstack1l11ll1111_opy_[bstack11l111_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤࡡࡸࡶࡱ࠭ၪ")].split(bstack11l111_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥ࠰ࡦࡺ࡯࡬ࡥࠩၫ"))[0] + bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡶ࠳ࠬၬ") + bstack1l11ll1111_opy_[
              bstack11l111_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨၭ")]
            logger.info(bstack1111l11l11_opy_.format(bstack1l1111ll11_opy_))
            bstack1l11l1lll_opy_ = bstack1l11ll1111_opy_[bstack11l111_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩၮ")]
            bstack1l1lll11ll_opy_ = CONFIG[bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪၯ")]
            if bstack11l111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪၰ") in CONFIG:
              bstack1l1lll11ll_opy_ += bstack11l111_opy_ (u"ࠩࠣࠫၱ") + CONFIG[bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬၲ")]
            if bstack1l1lll11ll_opy_ != bstack1l11ll1111_opy_[bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩၳ")]:
              logger.debug(bstack1lll1ll1ll_opy_.format(bstack1l11ll1111_opy_[bstack11l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪၴ")], bstack1l1lll11ll_opy_))
            cli.bstack1l1lll1l1_opy_(bstack11l111_opy_ (u"ࠨࡨࡵࡶࡳ࠾࡬࡫ࡴࡠࡤࡸ࡭ࡱࡪ࡟࡭࡫ࡱ࡯ࠧၵ"), datetime.datetime.now() - bstack1l1ll1ll1_opy_)
            return [bstack1l11ll1111_opy_[bstack11l111_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪၶ")], bstack1l1111ll11_opy_]
    else:
      logger.warn(bstack11llllll1l_opy_)
  except Exception as e:
    logger.debug(bstack1l11l1ll1l_opy_.format(str(e)))
  return [None, None]
def bstack1ll1ll1l1l_opy_(url, bstack1ll111llll_opy_=False):
  global CONFIG
  global bstack1111ll1l11_opy_
  if not bstack1111ll1l11_opy_:
    hostname = bstack1ll1llllll_opy_(url)
    is_private = bstack11ll1ll111_opy_(hostname)
    if (bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬၷ") in CONFIG and not bstack1l1lll1ll1_opy_(CONFIG[bstack11l111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ၸ")])) and (is_private or bstack1ll111llll_opy_):
      bstack1111ll1l11_opy_ = hostname
def bstack1ll1llllll_opy_(url):
  return urlparse(url).hostname
def bstack11ll1ll111_opy_(hostname):
  for bstack1l11l1l111_opy_ in bstack1l1111111_opy_:
    regex = re.compile(bstack1l11l1l111_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack111l1l11l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1llll11111_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1l1l11llll_opy_
  bstack1111l1l11l_opy_ = not (bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧၹ"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪၺ"), None))
  bstack11l11l11l_opy_ = getattr(driver, bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬၻ"), None) != True
  bstack11l1lllll1_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ၼ"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩၽ"), None)
  if bstack11l1lllll1_opy_:
    if not bstack1l1l1l1ll_opy_():
      logger.warning(bstack11l111_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶ࠲ࠧၾ"))
      return {}
    logger.debug(bstack11l111_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ၿ"))
    logger.debug(perform_scan(driver, driver_command=bstack11l111_opy_ (u"ࠪࡩࡽ࡫ࡣࡶࡶࡨࡗࡨࡸࡩࡱࡶࠪႀ")))
    results = bstack1ll1l1lll_opy_(bstack11l111_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷࡷࠧႁ"))
    if results is not None and results.get(bstack11l111_opy_ (u"ࠧ࡯ࡳࡴࡷࡨࡷࠧႂ")) is not None:
        return results[bstack11l111_opy_ (u"ࠨࡩࡴࡵࡸࡩࡸࠨႃ")]
    logger.error(bstack11l111_opy_ (u"ࠢࡏࡱࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡖࡪࡹࡵ࡭ࡶࡶࠤࡼ࡫ࡲࡦࠢࡩࡳࡺࡴࡤ࠯ࠤႄ"))
    return []
  if not bstack1111l11l_opy_.bstack11l111lll1_opy_(CONFIG, bstack1l1l11llll_opy_) or (bstack11l11l11l_opy_ and bstack1111l1l11l_opy_):
    logger.warning(bstack11l111_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵ࠱ࠦႅ"))
    return {}
  try:
    logger.debug(bstack11l111_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸ࠭ႆ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack111l1ll1l_opy_.bstack11ll1ll1ll_opy_)
    return results
  except Exception:
    logger.error(bstack11l111_opy_ (u"ࠥࡒࡴࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡸࡧࡵࡩࠥ࡬࡯ࡶࡰࡧ࠲ࠧႇ"))
    return {}
@measure(event_name=EVENTS.bstack1111ll1111_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1l1l11llll_opy_
  bstack1111l1l11l_opy_ = not (bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨႈ"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫႉ"), None))
  bstack11l11l11l_opy_ = getattr(driver, bstack11l111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭ႊ"), None) != True
  bstack11l1lllll1_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧႋ"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪႌ"), None)
  if bstack11l1lllll1_opy_:
    if not bstack1l1l1l1ll_opy_():
      logger.warning(bstack11l111_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠴ႍࠢ"))
      return {}
    logger.debug(bstack11l111_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹࠨႎ"))
    logger.debug(perform_scan(driver, driver_command=bstack11l111_opy_ (u"ࠫࡪࡾࡥࡤࡷࡷࡩࡘࡩࡲࡪࡲࡷࠫႏ")))
    results = bstack1ll1l1lll_opy_(bstack11l111_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸࡘࡻ࡭࡮ࡣࡵࡽࠧ႐"))
    if results is not None and results.get(bstack11l111_opy_ (u"ࠨࡳࡶ࡯ࡰࡥࡷࡿࠢ႑")) is not None:
        return results[bstack11l111_opy_ (u"ࠢࡴࡷࡰࡱࡦࡸࡹࠣ႒")]
    logger.error(bstack11l111_opy_ (u"ࠣࡐࡲࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡗ࡫ࡳࡶ࡮ࡷࡷ࡙ࠥࡵ࡮࡯ࡤࡶࡾࠦࡷࡢࡵࠣࡪࡴࡻ࡮ࡥ࠰ࠥ႓"))
    return {}
  if not bstack1111l11l_opy_.bstack11l111lll1_opy_(CONFIG, bstack1l1l11llll_opy_) or (bstack11l11l11l_opy_ and bstack1111l1l11l_opy_):
    logger.warning(bstack11l111_opy_ (u"ࠤࡑࡳࡹࠦࡡ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡸࡻ࡭࡮ࡣࡵࡽ࠳ࠨ႔"))
    return {}
  try:
    logger.debug(bstack11l111_opy_ (u"ࠪࡔࡪࡸࡦࡰࡴࡰ࡭ࡳ࡭ࠠࡴࡥࡤࡲࠥࡨࡥࡧࡱࡵࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹࠨ႕"))
    logger.debug(perform_scan(driver))
    bstack1l1ll1ll1l_opy_ = driver.execute_async_script(bstack111l1ll1l_opy_.bstack1l111111ll_opy_)
    return bstack1l1ll1ll1l_opy_
  except Exception:
    logger.error(bstack11l111_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡷࡰࡱࡦࡸࡹࠡࡹࡤࡷࠥ࡬࡯ࡶࡰࡧ࠲ࠧ႖"))
    return {}
def bstack1l1l1l1ll_opy_():
  global CONFIG
  global bstack1l1l11llll_opy_
  bstack1lll1l1lll_opy_ = bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ႗"), None) and bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ႘"), None)
  if not bstack1111l11l_opy_.bstack11l111lll1_opy_(CONFIG, bstack1l1l11llll_opy_) or not bstack1lll1l1lll_opy_:
        logger.warning(bstack11l111_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡸࡥࡴࡷ࡯ࡸࡸ࠴ࠢ႙"))
        return False
  return True
def bstack1ll1l1lll_opy_(bstack11lllll1l1_opy_):
    bstack1ll111ll1_opy_ = bstack1lll111l_opy_.current_test_uuid() if bstack1lll111l_opy_.current_test_uuid() else bstack1lll1lll_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack11l11ll11l_opy_(bstack1ll111ll1_opy_, bstack11lllll1l1_opy_))
        try:
            return future.result(timeout=bstack1ll1l11111_opy_)
        except TimeoutError:
            logger.error(bstack11l111_opy_ (u"ࠣࡖ࡬ࡱࡪࡵࡵࡵࠢࡤࡪࡹ࡫ࡲࠡࡽࢀࡷࠥࡽࡨࡪ࡮ࡨࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡒࡦࡵࡸࡰࡹࡹࠢႚ").format(bstack1ll1l11111_opy_))
        except Exception as ex:
            logger.debug(bstack11l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡴࡨࡸࡷ࡯ࡥࡷ࡫ࡱ࡫ࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡻࡾ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠰ࠤࢀࢃࠢႛ").format(bstack11lllll1l1_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack11ll111lll_opy_, stage=STAGE.bstack1l11lll11_opy_, bstack11l111l1l_opy_=bstack11lll111ll_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1l1l11llll_opy_
  bstack1111l1l11l_opy_ = not (bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧႜ"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪႝ"), None))
  bstack11111lll1_opy_ = not (bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ႞"), None) and bstack1l1lll11_opy_(
          threading.current_thread(), bstack11l111_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ႟"), None))
  bstack11l11l11l_opy_ = getattr(driver, bstack11l111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧႠ"), None) != True
  if not bstack1111l11l_opy_.bstack11l111lll1_opy_(CONFIG, bstack1l1l11llll_opy_) or (bstack11l11l11l_opy_ and bstack1111l1l11l_opy_ and bstack11111lll1_opy_):
    logger.warning(bstack11l111_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡷࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡩࡡ࡯࠰ࠥႡ"))
    return {}
  try:
    bstack111l1lllll_opy_ = bstack11l111_opy_ (u"ࠩࡤࡴࡵ࠭Ⴂ") in CONFIG and CONFIG.get(bstack11l111_opy_ (u"ࠪࡥࡵࡶࠧႣ"), bstack11l111_opy_ (u"ࠫࠬႤ"))
    session_id = getattr(driver, bstack11l111_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠩႥ"), None)
    if not session_id:
      logger.warning(bstack11l111_opy_ (u"ࠨࡎࡰࠢࡶࡩࡸࡹࡩࡰࡰࠣࡍࡉࠦࡦࡰࡷࡱࡨࠥ࡬࡯ࡳࠢࡧࡶ࡮ࡼࡥࡳࠤႦ"))
      return {bstack11l111_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨႧ"): bstack11l111_opy_ (u"ࠣࡐࡲࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡏࡄࠡࡨࡲࡹࡳࡪࠢႨ")}
    if bstack111l1lllll_opy_:
      try:
        bstack11ll1111l1_opy_ = {
              bstack11l111_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ࠭Ⴉ"): os.environ.get(bstack11l111_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨႪ"), os.environ.get(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨႫ"), bstack11l111_opy_ (u"ࠬ࠭Ⴌ"))),
              bstack11l111_opy_ (u"࠭ࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩ࠭Ⴍ"): bstack1lll111l_opy_.current_test_uuid() if bstack1lll111l_opy_.current_test_uuid() else bstack1lll1lll_opy_.current_hook_uuid(),
              bstack11l111_opy_ (u"ࠧࡢࡷࡷ࡬ࡍ࡫ࡡࡥࡧࡵࠫႮ"): os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭Ⴏ")),
              bstack11l111_opy_ (u"ࠩࡶࡧࡦࡴࡔࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩႰ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack11l111_opy_ (u"ࠪࡸ࡭ࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨႱ"): os.environ.get(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩႲ"), bstack11l111_opy_ (u"ࠬ࠭Ⴓ")),
              bstack11l111_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭Ⴔ"): kwargs.get(bstack11l111_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸ࡟ࡤࡱࡰࡱࡦࡴࡤࠨႵ"), None) or bstack11l111_opy_ (u"ࠨࠩႶ")
          }
        if not hasattr(thread_local, bstack11l111_opy_ (u"ࠩࡥࡥࡸ࡫࡟ࡢࡲࡳࡣࡦ࠷࠱ࡺࡡࡶࡧࡷ࡯ࡰࡵࠩႷ")):
            scripts = {bstack11l111_opy_ (u"ࠪࡷࡨࡧ࡮ࠨႸ"): bstack111l1ll1l_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack1lll1l1111_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack1lll1l1111_opy_[bstack11l111_opy_ (u"ࠫࡸࡩࡡ࡯ࠩႹ")] = bstack1lll1l1111_opy_[bstack11l111_opy_ (u"ࠬࡹࡣࡢࡰࠪႺ")] % json.dumps(bstack11ll1111l1_opy_)
        bstack111l1ll1l_opy_.bstack1l1l1lll1_opy_(bstack1lll1l1111_opy_)
        bstack111l1ll1l_opy_.store()
        bstack1llll1llll_opy_ = driver.execute_script(bstack111l1ll1l_opy_.perform_scan)
      except Exception as bstack1lll1ll111_opy_:
        logger.info(bstack11l111_opy_ (u"ࠨࡁࡱࡲ࡬ࡹࡲࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡤࡣࡱࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࠨႻ") + str(bstack1lll1ll111_opy_))
        bstack1llll1llll_opy_ = {bstack11l111_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨႼ"): str(bstack1lll1ll111_opy_)}
    else:
      bstack1llll1llll_opy_ = driver.execute_async_script(bstack111l1ll1l_opy_.perform_scan, {bstack11l111_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨႽ"): kwargs.get(bstack11l111_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࡡࡦࡳࡲࡳࡡ࡯ࡦࠪႾ"), None) or bstack11l111_opy_ (u"ࠪࠫႿ")})
    return bstack1llll1llll_opy_
  except Exception as err:
    logger.error(bstack11l111_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡳࡷࡱࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡩࡡ࡯࠰ࠣࡿࢂࠨჀ").format(str(err)))
    return {}