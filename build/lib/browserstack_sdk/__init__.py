# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
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
from browserstack_sdk.bstack1ll111l111_opy_ import bstack111ll1l11l_opy_
from browserstack_sdk.bstack1ll1lllll_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE, bstack1ll11ll1l_opy_
from bstack_utils.messages import bstack1ll1ll1l1_opy_, bstack11l1l11l1_opy_, bstack11l1l1l11_opy_, bstack11lll11111_opy_, bstack1111l1l1l1_opy_, bstack11l1llllll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11ll1l11l1_opy_ import get_logger
from bstack_utils.helper import bstack1111l1l111_opy_
from browserstack_sdk.bstack1111llll_opy_ import bstack111ll11ll_opy_
logger = get_logger(__name__)
def bstack11lll1ll1l_opy_():
  global CONFIG
  headers = {
        bstack11l1111_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩਯ"): bstack11l1111_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧਰ"),
      }
  proxies = bstack1111l1l111_opy_(CONFIG, bstack1ll11ll1l_opy_)
  try:
    response = requests.get(bstack1ll11ll1l_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack11lllllll1_opy_ = response.json()[bstack11l1111_opy_ (u"ࠬ࡮ࡵࡣࡵࠪ਱")]
      logger.debug(bstack1ll1ll1l1_opy_.format(response.json()))
      return bstack11lllllll1_opy_
    else:
      logger.debug(bstack11l1l11l1_opy_.format(bstack11l1111_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧਲ")))
  except Exception as e:
    logger.debug(bstack11l1l11l1_opy_.format(e))
def bstack1ll1ll11l_opy_(hub_url):
  global CONFIG
  url = bstack11l1111_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤਲ਼")+  hub_url + bstack11l1111_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣ਴")
  headers = {
        bstack11l1111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨਵ"): bstack11l1111_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ਸ਼"),
      }
  proxies = bstack1111l1l111_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11l1l1l11_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack11lll11111_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack1lll1l1l1l_opy_, stage=STAGE.bstack1111ll111_opy_)
def bstack11111l11l1_opy_():
  try:
    global bstack1l111l1ll1_opy_
    global CONFIG
    if bstack11l1111_opy_ (u"ࠫ࡭ࡻࡢࡓࡧࡪ࡭ࡴࡴࠧ਷") in CONFIG and CONFIG[bstack11l1111_opy_ (u"ࠬ࡮ࡵࡣࡔࡨ࡫࡮ࡵ࡮ࠨਸ")]:
      from bstack_utils.constants import bstack1l1l11l11_opy_
      bstack1111lllll_opy_ = CONFIG[bstack11l1111_opy_ (u"࠭ࡨࡶࡤࡕࡩ࡬࡯࡯࡯ࠩਹ")]
      if bstack1111lllll_opy_ in bstack1l1l11l11_opy_:
        bstack1l111l1ll1_opy_ = bstack1l1l11l11_opy_[bstack1111lllll_opy_]
        logger.debug(bstack1111l1l1l1_opy_.format(bstack1l111l1ll1_opy_))
        return
      else:
        logger.debug(bstack11l1111_opy_ (u"ࠢࡉࡷࡥࠤࡰ࡫ࡹࠡࠩࡾࢁࠬࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࡎࡕࡃࡡࡘࡖࡑࡥࡍࡂࡒ࠯ࠤ࡫ࡧ࡬࡭࡫ࡱ࡫ࠥࡨࡡࡤ࡭ࠣࡸࡴࠦ࡯ࡱࡶ࡬ࡱࡦࡲࠠࡩࡷࡥࠤࡩ࡫ࡴࡦࡥࡷ࡭ࡴࡴࠢ਺").format(bstack1111lllll_opy_))
    bstack11lllllll1_opy_ = bstack11lll1ll1l_opy_()
    bstack11l1l1l1l_opy_ = []
    results = []
    for bstack1l11l1llll_opy_ in bstack11lllllll1_opy_:
      bstack11l1l1l1l_opy_.append(bstack111ll11ll_opy_(target=bstack1ll1ll11l_opy_,args=(bstack1l11l1llll_opy_,)))
    for t in bstack11l1l1l1l_opy_:
      t.start()
    for t in bstack11l1l1l1l_opy_:
      results.append(t.join())
    bstack11111l1lll_opy_ = {}
    for item in results:
      hub_url = item[bstack11l1111_opy_ (u"ࠨࡪࡸࡦࡤࡻࡲ࡭ࠩ਻")]
      latency = item[bstack11l1111_opy_ (u"ࠩ࡯ࡥࡹ࡫࡮ࡤࡻ਼ࠪ")]
      bstack11111l1lll_opy_[hub_url] = latency
    bstack11lll11ll1_opy_ = min(bstack11111l1lll_opy_, key= lambda x: bstack11111l1lll_opy_[x])
    bstack1l111l1ll1_opy_ = bstack11lll11ll1_opy_
    logger.debug(bstack1111l1l1l1_opy_.format(bstack11lll11ll1_opy_))
  except Exception as e:
    logger.debug(bstack11l1llllll_opy_.format(e))
from browserstack_sdk.bstack1111l1l1_opy_ import *
from browserstack_sdk.bstack1111llll_opy_ import *
from browserstack_sdk.bstack111llll1_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack11ll1l11l1_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack11l1llll1_opy_, stage=STAGE.bstack1111ll111_opy_)
def bstack1l1111llll_opy_():
    global bstack1l111l1ll1_opy_
    try:
        bstack1ll111111l_opy_ = bstack1111ll111l_opy_()
        bstack111lllllll_opy_(bstack1ll111111l_opy_)
        hub_url = bstack1ll111111l_opy_.get(bstack11l1111_opy_ (u"ࠥࡹࡷࡲࠢ਽"), bstack11l1111_opy_ (u"ࠦࠧਾ"))
        if hub_url.endswith(bstack11l1111_opy_ (u"ࠬ࠵ࡷࡥ࠱࡫ࡹࡧ࠭ਿ")):
            hub_url = hub_url.rsplit(bstack11l1111_opy_ (u"࠭࠯ࡸࡦ࠲࡬ࡺࡨࠧੀ"), 1)[0]
        if hub_url.startswith(bstack11l1111_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯ࠨੁ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack11l1111_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࠪੂ")):
            hub_url = hub_url[8:]
        bstack1l111l1ll1_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1111ll111l_opy_():
    global CONFIG
    bstack1l11llll1_opy_ = CONFIG.get(bstack11l1111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭੃"), {}).get(bstack11l1111_opy_ (u"ࠪ࡫ࡷ࡯ࡤࡏࡣࡰࡩࠬ੄"), bstack11l1111_opy_ (u"ࠫࡓࡕ࡟ࡈࡔࡌࡈࡤࡔࡁࡎࡇࡢࡔࡆ࡙ࡓࡆࡆࠪ੅"))
    if not isinstance(bstack1l11llll1_opy_, str):
        raise ValueError(bstack11l1111_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡌࡸࡩࡥࠢࡱࡥࡲ࡫ࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡣࠣࡺࡦࡲࡩࡥࠢࡶࡸࡷ࡯࡮ࡨࠤ੆"))
    try:
        bstack1ll111111l_opy_ = bstack1l1lll1l1_opy_(bstack1l11llll1_opy_)
        return bstack1ll111111l_opy_
    except Exception as e:
        logger.error(bstack11l1111_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡩࡵ࡭ࡩࠦࡤࡦࡶࡤ࡭ࡱࡹࠠ࠻ࠢࡾࢁࠧੇ").format(str(e)))
        return {}
def bstack1l1lll1l1_opy_(bstack1l11llll1_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack11l1111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩੈ")] or not CONFIG[bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ੉")]:
            raise ValueError(bstack11l1111_opy_ (u"ࠤࡐ࡭ࡸࡹࡩ࡯ࡩࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠤࡴࡸࠠࡢࡥࡦࡩࡸࡹࠠ࡬ࡧࡼࠦ੊"))
        url = bstack1ll11l11l_opy_ + bstack1l11llll1_opy_
        auth = (CONFIG[bstack11l1111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬੋ")], CONFIG[bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧੌ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack11l1111ll1_opy_ = json.loads(response.text)
            return bstack11l1111ll1_opy_
    except ValueError as ve:
        logger.error(bstack11l1111_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡩࡵ࡭ࡩࠦࡤࡦࡶࡤ࡭ࡱࡹࠠ࠻ࠢࡾࢁ੍ࠧ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack11l1111_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳࠡ࠼ࠣࡿࢂࠨ੎").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack111lllllll_opy_(bstack11l11l1ll_opy_):
    global CONFIG
    if bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ੏") not in CONFIG or str(CONFIG[bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ੐")]).lower() == bstack11l1111_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨੑ"):
        CONFIG[bstack11l1111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩ੒")] = False
    elif bstack11l1111_opy_ (u"ࠫ࡮ࡹࡔࡳ࡫ࡤࡰࡌࡸࡩࡥࠩ੓") in bstack11l11l1ll_opy_:
        bstack1ll111l11l_opy_ = CONFIG.get(bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ੔"), {})
        logger.debug(bstack11l1111_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡋࡸࡪࡵࡷ࡭ࡳ࡭ࠠ࡭ࡱࡦࡥࡱࠦ࡯ࡱࡶ࡬ࡳࡳࡹ࠺ࠡࠧࡶࠦ੕"), bstack1ll111l11l_opy_)
        bstack111l111lll_opy_ = bstack11l11l1ll_opy_.get(bstack11l1111_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡒࡦࡲࡨࡥࡹ࡫ࡲࡴࠤ੖"), [])
        bstack1l1l11ll11_opy_ = bstack11l1111_opy_ (u"ࠣ࠮ࠥ੗").join(bstack111l111lll_opy_)
        logger.debug(bstack11l1111_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡅࡸࡷࡹࡵ࡭ࠡࡴࡨࡴࡪࡧࡴࡦࡴࠣࡷࡹࡸࡩ࡯ࡩ࠽ࠤࠪࡹࠢ੘"), bstack1l1l11ll11_opy_)
        bstack1l1l1ll111_opy_ = {
            bstack11l1111_opy_ (u"ࠥࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧਖ਼"): bstack11l1111_opy_ (u"ࠦࡦࡺࡳ࠮ࡴࡨࡴࡪࡧࡴࡦࡴࠥਗ਼"),
            bstack11l1111_opy_ (u"ࠧ࡬࡯ࡳࡥࡨࡐࡴࡩࡡ࡭ࠤਜ਼"): bstack11l1111_opy_ (u"ࠨࡴࡳࡷࡨࠦੜ"),
            bstack11l1111_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳ࠭ࡳࡧࡳࡩࡦࡺࡥࡳࠤ੝"): bstack1l1l11ll11_opy_
        }
        bstack1ll111l11l_opy_.update(bstack1l1l1ll111_opy_)
        logger.debug(bstack11l1111_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡖࡲࡧࡥࡹ࡫ࡤࠡ࡮ࡲࡧࡦࡲࠠࡰࡲࡷ࡭ࡴࡴࡳ࠻ࠢࠨࡷࠧਫ਼"), bstack1ll111l11l_opy_)
        CONFIG[bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੟")] = bstack1ll111l11l_opy_
        logger.debug(bstack11l1111_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡉ࡭ࡳࡧ࡬ࠡࡅࡒࡒࡋࡏࡇ࠻ࠢࠨࡷࠧ੠"), CONFIG)
def bstack1111lll111_opy_():
    bstack1ll111111l_opy_ = bstack1111ll111l_opy_()
    if not bstack1ll111111l_opy_[bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡖࡴ࡯ࠫ੡")]:
      raise ValueError(bstack11l1111_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡗࡵࡰࠥ࡯ࡳࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡩࡶࡴࡳࠠࡨࡴ࡬ࡨࠥࡪࡥࡵࡣ࡬ࡰࡸ࠴ࠢ੢"))
    return bstack1ll111111l_opy_[bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡘࡶࡱ࠭੣")] + bstack11l1111_opy_ (u"ࠧࡀࡥࡤࡴࡸࡃࠧ੤")
@measure(event_name=EVENTS.bstack1l11111ll_opy_, stage=STAGE.bstack1111ll111_opy_)
def bstack1l11l11ll_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack11l1111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ੥")], CONFIG[bstack11l1111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ੦")])
        url = bstack11l11ll11_opy_
        logger.debug(bstack11l1111_opy_ (u"ࠥࡅࡹࡺࡥ࡮ࡲࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡥࡹ࡮ࡲࡤࡴࠢࡩࡶࡴࡳࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡔࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠣࡅࡕࡏࠢ੧"))
        try:
            response = requests.get(url, auth=auth, headers={bstack11l1111_opy_ (u"ࠦࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠥ੨"): bstack11l1111_opy_ (u"ࠧࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠣ੩")})
            if response.status_code == 200:
                bstack1ll1l11111_opy_ = json.loads(response.text)
                bstack1l1llll11l_opy_ = bstack1ll1l11111_opy_.get(bstack11l1111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡸ࠭੪"), [])
                if bstack1l1llll11l_opy_:
                    bstack111l1ll11_opy_ = bstack1l1llll11l_opy_[0]
                    build_hashed_id = bstack111l1ll11_opy_.get(bstack11l1111_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ੫"))
                    bstack11ll111ll_opy_ = bstack11ll1ll1l_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack11ll111ll_opy_])
                    logger.info(bstack1l1ll1l1l1_opy_.format(bstack11ll111ll_opy_))
                    bstack11111lllll_opy_ = CONFIG[bstack11l1111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ੬")]
                    if bstack11l1111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ੭") in CONFIG:
                      bstack11111lllll_opy_ += bstack11l1111_opy_ (u"ࠪࠤࠬ੮") + CONFIG[bstack11l1111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੯")]
                    if bstack11111lllll_opy_ != bstack111l1ll11_opy_.get(bstack11l1111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪੰ")):
                      logger.debug(bstack11lll11ll_opy_.format(bstack111l1ll11_opy_.get(bstack11l1111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫੱ")), bstack11111lllll_opy_))
                    return result
                else:
                    logger.debug(bstack11l1111_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡎࡰࠢࡥࡹ࡮ࡲࡤࡴࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࡹ࡮ࡥࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠱ࠦੲ"))
            else:
                logger.debug(bstack11l1111_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡥࡹ࡮ࡲࡤࡴ࠰ࠥੳ"))
        except Exception as e:
            logger.error(bstack11l1111_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࡶࠤ࠿ࠦࡻࡾࠤੴ").format(str(e)))
    else:
        logger.debug(bstack11l1111_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡆࡓࡓࡌࡉࡈࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡶࡩࡹ࠴ࠠࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡥࡹ࡮ࡲࡤࡴ࠰ࠥੵ"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack11lll1111l_opy_ import bstack11lll1111l_opy_, Events, bstack1111lll1ll_opy_, bstack11ll1l1ll_opy_
from bstack_utils.measure import bstack111111l1l1_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack11llll1111_opy_ import bstack1llllll11l_opy_
from bstack_utils.messages import *
from bstack_utils import bstack11ll1l11l1_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack1ll1111111_opy_, bstack111ll1l111_opy_, bstack11llll111_opy_, bstack1llll11l_opy_, \
  bstack1l11lllll1_opy_, \
  Notset, bstack11ll11l1ll_opy_, \
  bstack11l11ll11l_opy_, bstack11lll1l1l1_opy_, bstack1ll1111l1_opy_, bstack11l11l1lll_opy_, bstack1ll111ll1_opy_, bstack1l1l111111_opy_, \
  bstack111ll1llll_opy_, \
  bstack1l1111l11_opy_, bstack11l11l111l_opy_, bstack1l111111l_opy_, bstack11llll1l1_opy_, \
  bstack1lll11l1ll_opy_, bstack111l1l1l1_opy_, bstack1ll11lll11_opy_, bstack1l1l111lll_opy_
from bstack_utils.bstack11l1l1ll1l_opy_ import bstack1llll11l11_opy_
from bstack_utils.bstack111l111ll_opy_ import bstack11l1ll1111_opy_, bstack1l1ll11lll_opy_
from bstack_utils.bstack1l1lllll1_opy_ import bstack111111llll_opy_
from bstack_utils.bstack11ll1l111l_opy_ import bstack1llll1l111_opy_, bstack11l1ll11l_opy_
from bstack_utils.bstack1l1ll1lll1_opy_ import bstack1l1ll1lll1_opy_
from bstack_utils.bstack1111l11ll1_opy_ import bstack1ll1111ll_opy_
from bstack_utils.proxy import bstack1l1ll11ll_opy_, bstack1111l1l111_opy_, bstack111lll1ll_opy_, bstack111l1l1l11_opy_
from bstack_utils.bstack1l1ll1111_opy_ import bstack11l11l111_opy_
import bstack_utils.bstack111ll1111_opy_ as bstack11l1lll11l_opy_
import bstack_utils.bstack111l11l1l1_opy_ as bstack1ll111l1l_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack1ll1llllll_opy_ import bstack11l1l1l1ll_opy_
from bstack_utils.bstack1llllll11_opy_ import bstack1lllllll1_opy_
from bstack_utils.bstack11111lll1l_opy_ import bstack11ll1ll1ll_opy_
if os.getenv(bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡉࡑࡒࡏࡘ࠭੶")):
  cli.bstack111ll11111_opy_()
else:
  os.environ[bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡊࡒࡓࡐ࡙ࠧ੷")] = bstack11l1111_opy_ (u"࠭ࡴࡳࡷࡨࠫ੸")
bstack1lll1l1l11_opy_ = bstack11l1111_opy_ (u"ࠧࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࠠࠡ࡫ࡩࠬࡵࡧࡧࡦࠢࡀࡁࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠠࡼ࡞ࡱࠤࠥࠦࡴࡳࡻࡾࡠࡳࠦࡣࡰࡰࡶࡸࠥ࡬ࡳࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࡡ࠭ࡦࡴ࡞ࠪ࠭ࡀࡢ࡮ࠡࠢࠣࠤࠥ࡬ࡳ࠯ࡣࡳࡴࡪࡴࡤࡇ࡫࡯ࡩࡘࡿ࡮ࡤࠪࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠬࠡࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡳࡣ࡮ࡴࡤࡦࡺࠬࠤ࠰ࠦࠢ࠻ࠤࠣ࠯ࠥࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡊࡔࡑࡑ࠲ࡵࡧࡲࡴࡧࠫࠬࡦࡽࡡࡪࡶࠣࡲࡪࡽࡐࡢࡩࡨ࠶࠳࡫ࡶࡢ࡮ࡸࡥࡹ࡫ࠨࠣࠪࠬࠤࡂࡄࠠࡼࡿࠥ࠰ࠥࡢࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡨࡧࡷࡗࡪࡹࡳࡪࡱࡱࡈࡪࡺࡡࡪ࡮ࡶࠦࢂࡢࠧࠪࠫࠬ࡟ࠧ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠣ࡟ࠬࠤ࠰ࠦࠢ࠭࡞࡟ࡲࠧ࠯࡜࡯ࠢࠣࠤࠥࢃࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡽ࡝ࡰࠣࠤ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠧ੹")
bstack1111lll11l_opy_ = bstack11l1111_opy_ (u"ࠨ࡞ࡱ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡰࡢࡶ࡫ࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳࡞࡞ࡱࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠴ࡡࡡࡴࡣࡰࡰࡶࡸࠥࡶ࡟ࡪࡰࡧࡩࡽࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠴ࡠࡠࡳࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡹ࡬ࡪࡥࡨࠬ࠵࠲ࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࠬࡠࡳࡩ࡯࡯ࡵࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬ࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ࠭ࡀࡢ࡮ࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯࠳ࡩࡨࡳࡱࡰ࡭ࡺࡳ࠮࡭ࡣࡸࡲࡨ࡮ࠠ࠾ࠢࡤࡷࡾࡴࡣࠡࠪ࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴࠫࠣࡁࡃࠦࡻ࡝ࡰ࡯ࡩࡹࠦࡣࡢࡲࡶ࠿ࡡࡴࡴࡳࡻࠣࡿࡡࡴࡣࡢࡲࡶࠤࡂࠦࡊࡔࡑࡑ࠲ࡵࡧࡲࡴࡧࠫࡦࡸࡺࡡࡤ࡭ࡢࡧࡦࡶࡳࠪ࡞ࡱࠤࠥࢃࠠࡤࡣࡷࡧ࡭࠮ࡥࡹࠫࠣࡿࡡࡴࠠࠡࠢࠣࢁࡡࡴࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡣࡺࡥ࡮ࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯࠳ࡩࡨࡳࡱࡰ࡭ࡺࡳ࠮ࡤࡱࡱࡲࡪࡩࡴࠩࡽ࡟ࡲࠥࠦࠠࠡࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸ࠿ࠦࡠࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ࠦࡾࡩࡳࡩ࡯ࡥࡧࡘࡖࡎࡉ࡯࡮ࡲࡲࡲࡪࡴࡴࠩࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡦࡥࡵࡹࠩࠪࡿࡣ࠰ࡡࡴࠠࠡࠢࠣ࠲࠳࠴࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸࡢ࡮ࠡࠢࢀ࠭ࡡࡴࡽ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࠧ੺")
from ._version import __version__
bstack1l1l11l111_opy_ = None
CONFIG = {}
bstack1lll11ll1l_opy_ = {}
bstack111lllll1_opy_ = {}
bstack1l1l1lll1_opy_ = None
bstack1l1111111l_opy_ = None
bstack11lll111ll_opy_ = None
bstack1l1llllll1_opy_ = -1
bstack1l1l11l1ll_opy_ = 0
bstack1l1ll1ll11_opy_ = bstack1l11l11l1l_opy_
bstack1l11ll1ll1_opy_ = 1
bstack11l1111l11_opy_ = False
bstack1ll111111_opy_ = False
bstack1l11l1l1l1_opy_ = bstack11l1111_opy_ (u"ࠩࠪ੻")
bstack11ll1l1lll_opy_ = bstack11l1111_opy_ (u"ࠪࠫ੼")
bstack111l111111_opy_ = False
bstack111l11111_opy_ = True
bstack11ll1111l1_opy_ = bstack11l1111_opy_ (u"ࠫࠬ੽")
bstack1l1ll11111_opy_ = []
bstack11l1l1ll11_opy_ = threading.Lock()
bstack1ll11l1l1l_opy_ = threading.Lock()
bstack1l111l1ll1_opy_ = bstack11l1111_opy_ (u"ࠬ࠭੾")
bstack1111llll11_opy_ = False
bstack1l1lllllll_opy_ = None
bstack1lll1ll1l1_opy_ = None
bstack1ll111l1l1_opy_ = None
bstack1l1l1ll11_opy_ = -1
bstack11111ll1l1_opy_ = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"࠭ࡾࠨ੿")), bstack11l1111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ઀"), bstack11l1111_opy_ (u"ࠨ࠰ࡵࡳࡧࡵࡴ࠮ࡴࡨࡴࡴࡸࡴ࠮ࡪࡨࡰࡵ࡫ࡲ࠯࡬ࡶࡳࡳ࠭ઁ"))
bstack11l111111l_opy_ = 0
bstack11l1l1lll1_opy_ = 0
bstack111ll11l11_opy_ = []
bstack1ll11lll1l_opy_ = []
bstack111111lll1_opy_ = []
bstack1ll11llll1_opy_ = []
bstack11l11lll11_opy_ = bstack11l1111_opy_ (u"ࠩࠪં")
bstack1lllllllll_opy_ = bstack11l1111_opy_ (u"ࠪࠫઃ")
bstack11llll1ll_opy_ = False
bstack111111ll1_opy_ = False
bstack1ll1l111ll_opy_ = {}
bstack1111ll1l1_opy_ = None
bstack1111l111l_opy_ = None
bstack1llll11ll1_opy_ = None
bstack11l1l111l1_opy_ = None
bstack1111lllll1_opy_ = None
bstack1l11l111l_opy_ = None
bstack1l1l1l1l11_opy_ = None
bstack1l1l11ll1l_opy_ = None
bstack11ll11ll1l_opy_ = None
bstack11l1l1ll1_opy_ = None
bstack111llll11l_opy_ = None
bstack1lllll1l11_opy_ = None
bstack1ll111lll1_opy_ = None
bstack1l1l11llll_opy_ = None
bstack1lll11lll1_opy_ = None
bstack11ll11l11l_opy_ = None
bstack1lll1l1ll1_opy_ = None
bstack11111lll1_opy_ = None
bstack11l111l1l_opy_ = None
bstack111l1l11l1_opy_ = None
bstack1l11ll1ll_opy_ = None
bstack1l11l11l11_opy_ = None
bstack11111l1ll1_opy_ = None
thread_local = threading.local()
bstack1l1llll1l_opy_ = False
bstack1l1l1l1l1_opy_ = bstack11l1111_opy_ (u"ࠦࠧ઄")
logger = bstack11ll1l11l1_opy_.get_logger(__name__, bstack1l1ll1ll11_opy_)
bstack1llll11ll_opy_ = Config.bstack1llllllll_opy_()
percy = bstack11l1lll111_opy_()
bstack1l111ll11_opy_ = bstack1llllll11l_opy_()
bstack111llll1ll_opy_ = bstack111llll1_opy_()
def bstack1l1ll11l1_opy_():
  global CONFIG
  global bstack11llll1ll_opy_
  global bstack1llll11ll_opy_
  testContextOptions = bstack1l111l111l_opy_(CONFIG)
  if bstack1l11lllll1_opy_(CONFIG):
    if (bstack11l1111_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧઅ") in testContextOptions and str(testContextOptions[bstack11l1111_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨઆ")]).lower() == bstack11l1111_opy_ (u"ࠧࡵࡴࡸࡩࠬઇ")):
      bstack11llll1ll_opy_ = True
    bstack1llll11ll_opy_.bstack1111l11ll_opy_(testContextOptions.get(bstack11l1111_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬઈ"), False))
  else:
    bstack11llll1ll_opy_ = True
    bstack1llll11ll_opy_.bstack1111l11ll_opy_(True)
def bstack1ll11ll111_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11l1l1l111_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack1111l1111_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11l1111_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡦࡳࡳ࡬ࡩࡨࡨ࡬ࡰࡪࠨઉ") == args[i].lower() or bstack11l1111_opy_ (u"ࠥ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡮ࡧ࡫ࡪࠦઊ") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack11ll1111l1_opy_
      bstack11ll1111l1_opy_ += bstack11l1111_opy_ (u"ࠫ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡈࡵ࡮ࡧ࡫ࡪࡊ࡮ࡲࡥࠡࠩઋ") + shlex.quote(path)
      return path
  return None
bstack1ll1l1ll1_opy_ = re.compile(bstack11l1111_opy_ (u"ࡷࠨ࠮ࠫࡁ࡟ࠨࢀ࠮࠮ࠫࡁࠬࢁ࠳࠰࠿ࠣઌ"))
def bstack1ll1l1111_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1ll1l1ll1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11l1111_opy_ (u"ࠨࠤࡼࠤઍ") + group + bstack11l1111_opy_ (u"ࠢࡾࠤ઎"), os.environ.get(group))
  return value
def bstack1l1lll11ll_opy_():
  global bstack11111l1ll1_opy_
  if bstack11111l1ll1_opy_ is None:
        bstack11111l1ll1_opy_ = bstack1111l1111_opy_()
  bstack11l1l1l11l_opy_ = bstack11111l1ll1_opy_
  if bstack11l1l1l11l_opy_ and os.path.exists(os.path.abspath(bstack11l1l1l11l_opy_)):
    fileName = bstack11l1l1l11l_opy_
  if bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬએ") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࡠࡈࡌࡐࡊ࠭ઐ")])) and not bstack11l1111_opy_ (u"ࠪࡪ࡮ࡲࡥࡏࡣࡰࡩࠬઑ") in locals():
    fileName = os.environ[bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ઒")]
  if bstack11l1111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡑࡥࡲ࡫ࠧઓ") in locals():
    bstack1l1ll_opy_ = os.path.abspath(fileName)
  else:
    bstack1l1ll_opy_ = bstack11l1111_opy_ (u"࠭ࠧઔ")
  bstack1111ll1ll_opy_ = os.getcwd()
  bstack11111l111l_opy_ = bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪક")
  bstack11l11lllll_opy_ = bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺࡣࡰࡰࠬખ")
  while (not os.path.exists(bstack1l1ll_opy_)) and bstack1111ll1ll_opy_ != bstack11l1111_opy_ (u"ࠤࠥગ"):
    bstack1l1ll_opy_ = os.path.join(bstack1111ll1ll_opy_, bstack11111l111l_opy_)
    if not os.path.exists(bstack1l1ll_opy_):
      bstack1l1ll_opy_ = os.path.join(bstack1111ll1ll_opy_, bstack11l11lllll_opy_)
    if bstack1111ll1ll_opy_ != os.path.dirname(bstack1111ll1ll_opy_):
      bstack1111ll1ll_opy_ = os.path.dirname(bstack1111ll1ll_opy_)
    else:
      bstack1111ll1ll_opy_ = bstack11l1111_opy_ (u"ࠥࠦઘ")
  bstack11111l1ll1_opy_ = bstack1l1ll_opy_ if os.path.exists(bstack1l1ll_opy_) else None
  return bstack11111l1ll1_opy_
def bstack1ll11l1111_opy_(config):
    if bstack11l1111_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࠫઙ") in config:
      config[bstack11l1111_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩચ")] = config[bstack11l1111_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬࠭છ")]
    if bstack11l1111_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࡏࡱࡶ࡬ࡳࡳࡹࠧજ") in config:
      config[bstack11l1111_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬઝ")] = config[bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࡑࡳࡸ࡮ࡵ࡮ࡴࠩઞ")]
def bstack11l111l1ll_opy_():
  bstack1l1ll_opy_ = bstack1l1lll11ll_opy_()
  if not os.path.exists(bstack1l1ll_opy_):
    bstack1l1l1l111l_opy_(
      bstack1ll1l11lll_opy_.format(os.getcwd()))
  try:
    with open(bstack1l1ll_opy_, bstack11l1111_opy_ (u"ࠪࡶࠬટ")) as stream:
      yaml.add_implicit_resolver(bstack11l1111_opy_ (u"ࠦࠦࡶࡡࡵࡪࡨࡼࠧઠ"), bstack1ll1l1ll1_opy_)
      yaml.add_constructor(bstack11l1111_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨડ"), bstack1ll1l1111_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1ll11l1111_opy_(config)
      return config
  except:
    with open(bstack1l1ll_opy_, bstack11l1111_opy_ (u"࠭ࡲࠨઢ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1ll11l1111_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1l1l1l111l_opy_(bstack11l111llll_opy_.format(str(exc)))
def bstack11ll11111_opy_(config):
  bstack1l1ll1ll1_opy_ = bstack1ll1ll11l1_opy_(config)
  for option in list(bstack1l1ll1ll1_opy_):
    if option.lower() in bstack111llll1l1_opy_ and option != bstack111llll1l1_opy_[option.lower()]:
      bstack1l1ll1ll1_opy_[bstack111llll1l1_opy_[option.lower()]] = bstack1l1ll1ll1_opy_[option]
      del bstack1l1ll1ll1_opy_[option]
  return config
def bstack111l111l11_opy_():
  global bstack111lllll1_opy_
  for key, bstack111l11lll_opy_ in bstack11l1111l1l_opy_.items():
    if isinstance(bstack111l11lll_opy_, list):
      for var in bstack111l11lll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack111lllll1_opy_[key] = os.environ[var]
          break
    elif bstack111l11lll_opy_ in os.environ and os.environ[bstack111l11lll_opy_] and str(os.environ[bstack111l11lll_opy_]).strip():
      bstack111lllll1_opy_[key] = os.environ[bstack111l11lll_opy_]
  if bstack11l1111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩણ") in os.environ:
    bstack111lllll1_opy_[bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬત")] = {}
    bstack111lllll1_opy_[bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭થ")][bstack11l1111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬદ")] = os.environ[bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ધ")]
def bstack1l1l1llll_opy_():
  global bstack1lll11ll1l_opy_
  global bstack11ll1111l1_opy_
  bstack11l111111_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack11l1111_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨન").lower() == val.lower():
      bstack1lll11ll1l_opy_[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ઩")] = {}
      bstack1lll11ll1l_opy_[bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫપ")][bstack11l1111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪફ")] = sys.argv[idx + 1]
      bstack11l111111_opy_.extend([idx, idx + 1])
      break
  for key, bstack1l1lll111_opy_ in bstack11llllll1l_opy_.items():
    if isinstance(bstack1l1lll111_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack1l1lll111_opy_:
          if bstack11l1111_opy_ (u"ࠩ࠰࠱ࠬબ") + var.lower() == val.lower() and key not in bstack1lll11ll1l_opy_:
            bstack1lll11ll1l_opy_[key] = sys.argv[idx + 1]
            bstack11ll1111l1_opy_ += bstack11l1111_opy_ (u"ࠪࠤ࠲࠳ࠧભ") + var + bstack11l1111_opy_ (u"ࠫࠥ࠭મ") + shlex.quote(sys.argv[idx + 1])
            bstack11l111111_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack11l1111_opy_ (u"ࠬ࠳࠭ࠨય") + bstack1l1lll111_opy_.lower() == val.lower() and key not in bstack1lll11ll1l_opy_:
          bstack1lll11ll1l_opy_[key] = sys.argv[idx + 1]
          bstack11ll1111l1_opy_ += bstack11l1111_opy_ (u"࠭ࠠ࠮࠯ࠪર") + bstack1l1lll111_opy_ + bstack11l1111_opy_ (u"ࠧࠡࠩ઱") + shlex.quote(sys.argv[idx + 1])
          bstack11l111111_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack11l111111_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack1l11l1111l_opy_(config):
  bstack1l1l1111l_opy_ = config.keys()
  for bstack11l1l1111_opy_, bstack1l1111111_opy_ in bstack1lll111lll_opy_.items():
    if bstack1l1111111_opy_ in bstack1l1l1111l_opy_:
      config[bstack11l1l1111_opy_] = config[bstack1l1111111_opy_]
      del config[bstack1l1111111_opy_]
  for bstack11l1l1111_opy_, bstack1l1111111_opy_ in bstack1l1l1lll11_opy_.items():
    if isinstance(bstack1l1111111_opy_, list):
      for bstack1ll11ll11_opy_ in bstack1l1111111_opy_:
        if bstack1ll11ll11_opy_ in bstack1l1l1111l_opy_:
          config[bstack11l1l1111_opy_] = config[bstack1ll11ll11_opy_]
          del config[bstack1ll11ll11_opy_]
          break
    elif bstack1l1111111_opy_ in bstack1l1l1111l_opy_:
      config[bstack11l1l1111_opy_] = config[bstack1l1111111_opy_]
      del config[bstack1l1111111_opy_]
  for bstack1ll11ll11_opy_ in list(config):
    for bstack1111l1ll1_opy_ in bstack1lll11l111_opy_:
      if bstack1ll11ll11_opy_.lower() == bstack1111l1ll1_opy_.lower() and bstack1ll11ll11_opy_ != bstack1111l1ll1_opy_:
        config[bstack1111l1ll1_opy_] = config[bstack1ll11ll11_opy_]
        del config[bstack1ll11ll11_opy_]
  bstack1l1ll111ll_opy_ = [{}]
  if not config.get(bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫલ")):
    config[bstack11l1111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬળ")] = [{}]
  bstack1l1ll111ll_opy_ = config[bstack11l1111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭઴")]
  for platform in bstack1l1ll111ll_opy_:
    for bstack1ll11ll11_opy_ in list(platform):
      for bstack1111l1ll1_opy_ in bstack1lll11l111_opy_:
        if bstack1ll11ll11_opy_.lower() == bstack1111l1ll1_opy_.lower() and bstack1ll11ll11_opy_ != bstack1111l1ll1_opy_:
          platform[bstack1111l1ll1_opy_] = platform[bstack1ll11ll11_opy_]
          del platform[bstack1ll11ll11_opy_]
  for bstack11l1l1111_opy_, bstack1l1111111_opy_ in bstack1l1l1lll11_opy_.items():
    for platform in bstack1l1ll111ll_opy_:
      if isinstance(bstack1l1111111_opy_, list):
        for bstack1ll11ll11_opy_ in bstack1l1111111_opy_:
          if bstack1ll11ll11_opy_ in platform:
            platform[bstack11l1l1111_opy_] = platform[bstack1ll11ll11_opy_]
            del platform[bstack1ll11ll11_opy_]
            break
      elif bstack1l1111111_opy_ in platform:
        platform[bstack11l1l1111_opy_] = platform[bstack1l1111111_opy_]
        del platform[bstack1l1111111_opy_]
  for bstack1l11l1ll11_opy_ in bstack1llll1llll_opy_:
    if bstack1l11l1ll11_opy_ in config:
      if not bstack1llll1llll_opy_[bstack1l11l1ll11_opy_] in config:
        config[bstack1llll1llll_opy_[bstack1l11l1ll11_opy_]] = {}
      config[bstack1llll1llll_opy_[bstack1l11l1ll11_opy_]].update(config[bstack1l11l1ll11_opy_])
      del config[bstack1l11l1ll11_opy_]
  for platform in bstack1l1ll111ll_opy_:
    for bstack1l11l1ll11_opy_ in bstack1llll1llll_opy_:
      if bstack1l11l1ll11_opy_ in list(platform):
        if not bstack1llll1llll_opy_[bstack1l11l1ll11_opy_] in platform:
          platform[bstack1llll1llll_opy_[bstack1l11l1ll11_opy_]] = {}
        platform[bstack1llll1llll_opy_[bstack1l11l1ll11_opy_]].update(platform[bstack1l11l1ll11_opy_])
        del platform[bstack1l11l1ll11_opy_]
  config = bstack11ll11111_opy_(config)
  return config
def bstack1l11lll111_opy_(config):
  global bstack11ll1l1lll_opy_
  bstack1111ll11l_opy_ = False
  if bstack11l1111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨવ") in config and str(config[bstack11l1111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩશ")]).lower() != bstack11l1111_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬષ"):
    if bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫસ") not in config or str(config[bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬહ")]).lower() == bstack11l1111_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ઺"):
      config[bstack11l1111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩ઻")] = False
    else:
      bstack1ll111111l_opy_ = bstack1111ll111l_opy_()
      if bstack11l1111_opy_ (u"ࠫ࡮ࡹࡔࡳ࡫ࡤࡰࡌࡸࡩࡥ઼ࠩ") in bstack1ll111111l_opy_:
        if not bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩઽ") in config:
          config[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪા")] = {}
        config[bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫિ")][bstack11l1111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪી")] = bstack11l1111_opy_ (u"ࠩࡤࡸࡸ࠳ࡲࡦࡲࡨࡥࡹ࡫ࡲࠨુ")
        bstack1111ll11l_opy_ = True
        bstack11ll1l1lll_opy_ = config[bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧૂ")].get(bstack11l1111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ૃ"))
  if bstack1l11lllll1_opy_(config) and bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩૄ") in config and str(config[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪૅ")]).lower() != bstack11l1111_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭૆") and not bstack1111ll11l_opy_:
    if not bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬે") in config:
      config[bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ૈ")] = {}
    if not config[bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧૉ")].get(bstack11l1111_opy_ (u"ࠫࡸࡱࡩࡱࡄ࡬ࡲࡦࡸࡹࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡤࡸ࡮ࡵ࡮ࠨ૊")) and not bstack11l1111_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧો") in config[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪૌ")]:
      bstack1ll11lll_opy_ = datetime.datetime.now()
      bstack11ll1l111_opy_ = bstack1ll11lll_opy_.strftime(bstack11l1111_opy_ (u"ࠧࠦࡦࡢࠩࡧࡥࠥࡉࠧࡐ્ࠫ"))
      hostname = socket.gethostname()
      bstack11111l1111_opy_ = bstack11l1111_opy_ (u"ࠨࠩ૎").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11l1111_opy_ (u"ࠩࡾࢁࡤࢁࡽࡠࡽࢀࠫ૏").format(bstack11ll1l111_opy_, hostname, bstack11111l1111_opy_)
      config[bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧૐ")][bstack11l1111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૑")] = identifier
    bstack11ll1l1lll_opy_ = config[bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ૒")].get(bstack11l1111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૓"))
  return config
def bstack11l1l1l1l1_opy_():
  bstack1lll111l11_opy_ =  bstack11l11l1lll_opy_()[bstack11l1111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷ࠭૔")]
  return bstack1lll111l11_opy_ if bstack1lll111l11_opy_ else -1
def bstack1lll11l11l_opy_(bstack1lll111l11_opy_):
  global CONFIG
  if not bstack11l1111_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪ૕") in CONFIG[bstack11l1111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૖")]:
    return
  CONFIG[bstack11l1111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૗")] = CONFIG[bstack11l1111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૘")].replace(
    bstack11l1111_opy_ (u"ࠬࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧ૙"),
    str(bstack1lll111l11_opy_)
  )
def bstack1ll1111lll_opy_():
  global CONFIG
  if not bstack11l1111_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬ૚") in CONFIG[bstack11l1111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૛")]:
    return
  bstack1ll11lll_opy_ = datetime.datetime.now()
  bstack11ll1l111_opy_ = bstack1ll11lll_opy_.strftime(bstack11l1111_opy_ (u"ࠨࠧࡧ࠱ࠪࡨ࠭ࠦࡊ࠽ࠩࡒ࠭૜"))
  CONFIG[bstack11l1111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૝")] = CONFIG[bstack11l1111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૞")].replace(
    bstack11l1111_opy_ (u"ࠫࠩࢁࡄࡂࡖࡈࡣ࡙ࡏࡍࡆࡿࠪ૟"),
    bstack11ll1l111_opy_
  )
def bstack1lll1ll1ll_opy_():
  global CONFIG
  if bstack11l1111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૠ") in CONFIG and not bool(CONFIG[bstack11l1111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨૡ")]):
    del CONFIG[bstack11l1111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩૢ")]
    return
  if not bstack11l1111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪૣ") in CONFIG:
    CONFIG[bstack11l1111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૤")] = bstack11l1111_opy_ (u"ࠪࠧࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭૥")
  if bstack11l1111_opy_ (u"ࠫࠩࢁࡄࡂࡖࡈࡣ࡙ࡏࡍࡆࡿࠪ૦") in CONFIG[bstack11l1111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૧")]:
    bstack1ll1111lll_opy_()
    os.environ[bstack11l1111_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪ૨")] = CONFIG[bstack11l1111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૩")]
  if not bstack11l1111_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪ૪") in CONFIG[bstack11l1111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૫")]:
    return
  bstack1lll111l11_opy_ = bstack11l1111_opy_ (u"ࠪࠫ૬")
  bstack1111111l1_opy_ = bstack11l1l1l1l1_opy_()
  if bstack1111111l1_opy_ != -1:
    bstack1lll111l11_opy_ = bstack11l1111_opy_ (u"ࠫࡈࡏࠠࠨ૭") + str(bstack1111111l1_opy_)
  if bstack1lll111l11_opy_ == bstack11l1111_opy_ (u"ࠬ࠭૮"):
    bstack1l1l11111l_opy_ = bstack11ll11l111_opy_(CONFIG[bstack11l1111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ૯")])
    if bstack1l1l11111l_opy_ != -1:
      bstack1lll111l11_opy_ = str(bstack1l1l11111l_opy_)
  if bstack1lll111l11_opy_:
    bstack1lll11l11l_opy_(bstack1lll111l11_opy_)
    os.environ[bstack11l1111_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ૰")] = CONFIG[bstack11l1111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૱")]
def bstack1l1l1ll1ll_opy_(bstack1lll111111_opy_, bstack1llll111ll_opy_, path):
  json_data = {
    bstack11l1111_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૲"): bstack1llll111ll_opy_
  }
  if os.path.exists(path):
    bstack111lll1l1l_opy_ = json.load(open(path, bstack11l1111_opy_ (u"ࠪࡶࡧ࠭૳")))
  else:
    bstack111lll1l1l_opy_ = {}
  bstack111lll1l1l_opy_[bstack1lll111111_opy_] = json_data
  with open(path, bstack11l1111_opy_ (u"ࠦࡼ࠱ࠢ૴")) as outfile:
    json.dump(bstack111lll1l1l_opy_, outfile)
def bstack11ll11l111_opy_(bstack1lll111111_opy_):
  bstack1lll111111_opy_ = str(bstack1lll111111_opy_)
  bstack1111llll1l_opy_ = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠬࢄࠧ૵")), bstack11l1111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭૶"))
  try:
    if not os.path.exists(bstack1111llll1l_opy_):
      os.makedirs(bstack1111llll1l_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠧࡿࠩ૷")), bstack11l1111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ૸"), bstack11l1111_opy_ (u"ࠩ࠱ࡦࡺ࡯࡬ࡥ࠯ࡱࡥࡲ࡫࠭ࡤࡣࡦ࡬ࡪ࠴ࡪࡴࡱࡱࠫૹ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11l1111_opy_ (u"ࠪࡻࠬૺ")):
        pass
      with open(file_path, bstack11l1111_opy_ (u"ࠦࡼ࠱ࠢૻ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11l1111_opy_ (u"ࠬࡸࠧૼ")) as bstack1ll111l1ll_opy_:
      bstack1ll1lllll1_opy_ = json.load(bstack1ll111l1ll_opy_)
    if bstack1lll111111_opy_ in bstack1ll1lllll1_opy_:
      bstack1l1l1l1ll_opy_ = bstack1ll1lllll1_opy_[bstack1lll111111_opy_][bstack11l1111_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૽")]
      bstack1ll1ll1l11_opy_ = int(bstack1l1l1l1ll_opy_) + 1
      bstack1l1l1ll1ll_opy_(bstack1lll111111_opy_, bstack1ll1ll1l11_opy_, file_path)
      return bstack1ll1ll1l11_opy_
    else:
      bstack1l1l1ll1ll_opy_(bstack1lll111111_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack11ll1ll1l1_opy_.format(str(e)))
    return -1
def bstack1111ll1l1l_opy_(config):
  if not config[bstack11l1111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ૾")] or not config[bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ૿")]:
    return True
  else:
    return False
def bstack11lll11l1_opy_(config, index=0):
  global bstack111l111111_opy_
  bstack1l11lll1ll_opy_ = {}
  caps = bstack1ll11l1l1_opy_ + bstack11lll1lll1_opy_
  if config.get(bstack11l1111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭଀"), False):
    bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧଁ")] = True
    bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨଂ")] = config.get(bstack11l1111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩଃ"), {})
  if bstack111l111111_opy_:
    caps += bstack1l1lll11l_opy_
  for key in config:
    if key in caps + [bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ଄")]:
      continue
    bstack1l11lll1ll_opy_[key] = config[key]
  if bstack11l1111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଅ") in config:
    for bstack11ll111111_opy_ in config[bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଆ")][index]:
      if bstack11ll111111_opy_ in caps:
        continue
      bstack1l11lll1ll_opy_[bstack11ll111111_opy_] = config[bstack11l1111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଇ")][index][bstack11ll111111_opy_]
  bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"ࠪ࡬ࡴࡹࡴࡏࡣࡰࡩࠬଈ")] = socket.gethostname()
  if bstack11l1111_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬଉ") in bstack1l11lll1ll_opy_:
    del (bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ଊ")])
  return bstack1l11lll1ll_opy_
def bstack1l1l1l111_opy_(config):
  global bstack111l111111_opy_
  bstack1l11l11111_opy_ = {}
  caps = bstack11lll1lll1_opy_
  if bstack111l111111_opy_:
    caps += bstack1l1lll11l_opy_
  for key in caps:
    if key in config:
      bstack1l11l11111_opy_[key] = config[key]
  return bstack1l11l11111_opy_
def bstack1l11111lll_opy_(bstack1l11lll1ll_opy_, bstack1l11l11111_opy_):
  bstack1ll11llll_opy_ = {}
  for key in bstack1l11lll1ll_opy_.keys():
    if key in bstack1lll111lll_opy_:
      bstack1ll11llll_opy_[bstack1lll111lll_opy_[key]] = bstack1l11lll1ll_opy_[key]
    else:
      bstack1ll11llll_opy_[key] = bstack1l11lll1ll_opy_[key]
  for key in bstack1l11l11111_opy_:
    if key in bstack1lll111lll_opy_:
      bstack1ll11llll_opy_[bstack1lll111lll_opy_[key]] = bstack1l11l11111_opy_[key]
    else:
      bstack1ll11llll_opy_[key] = bstack1l11l11111_opy_[key]
  return bstack1ll11llll_opy_
def bstack1l11l1l11l_opy_(config, index=0):
  global bstack111l111111_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11ll11llll_opy_ = bstack1ll1111111_opy_(bstack1ll11lll1_opy_, config, logger)
  bstack1l11l11111_opy_ = bstack1l1l1l111_opy_(config)
  bstack1lll1ll11l_opy_ = bstack11lll1lll1_opy_
  bstack1lll1ll11l_opy_ += bstack11l1111ll_opy_
  bstack1l11l11111_opy_ = update(bstack1l11l11111_opy_, bstack11ll11llll_opy_)
  if bstack111l111111_opy_:
    bstack1lll1ll11l_opy_ += bstack1l1lll11l_opy_
  if bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩଋ") in config:
    if bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬଌ") in config[bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ଍")][index]:
      caps[bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ଎")] = config[bstack11l1111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଏ")][index][bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଐ")]
    if bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭଑") in config[bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ଒")][index]:
      caps[bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨଓ")] = str(config[bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଔ")][index][bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪକ")])
    bstack111lll1l11_opy_ = bstack1ll1111111_opy_(bstack1ll11lll1_opy_, config[bstack11l1111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଖ")][index], logger)
    bstack1lll1ll11l_opy_ += list(bstack111lll1l11_opy_.keys())
    for bstack1lllllll11_opy_ in bstack1lll1ll11l_opy_:
      if bstack1lllllll11_opy_ in config[bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଗ")][index]:
        if bstack1lllllll11_opy_ == bstack11l1111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧଘ"):
          try:
            bstack111lll1l11_opy_[bstack1lllllll11_opy_] = str(config[bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩଙ")][index][bstack1lllllll11_opy_] * 1.0)
          except:
            bstack111lll1l11_opy_[bstack1lllllll11_opy_] = str(config[bstack11l1111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଚ")][index][bstack1lllllll11_opy_])
        else:
          bstack111lll1l11_opy_[bstack1lllllll11_opy_] = config[bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଛ")][index][bstack1lllllll11_opy_]
        del (config[bstack11l1111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଜ")][index][bstack1lllllll11_opy_])
    bstack1l11l11111_opy_ = update(bstack1l11l11111_opy_, bstack111lll1l11_opy_)
  bstack1l11lll1ll_opy_ = bstack11lll11l1_opy_(config, index)
  for bstack1ll11ll11_opy_ in bstack11lll1lll1_opy_ + list(bstack11ll11llll_opy_.keys()):
    if bstack1ll11ll11_opy_ in bstack1l11lll1ll_opy_:
      bstack1l11l11111_opy_[bstack1ll11ll11_opy_] = bstack1l11lll1ll_opy_[bstack1ll11ll11_opy_]
      del (bstack1l11lll1ll_opy_[bstack1ll11ll11_opy_])
  if bstack11ll11l1ll_opy_(config):
    bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪଝ")] = True
    caps.update(bstack1l11l11111_opy_)
    caps[bstack11l1111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬଞ")] = bstack1l11lll1ll_opy_
  else:
    bstack1l11lll1ll_opy_[bstack11l1111_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬଟ")] = False
    caps.update(bstack1l11111lll_opy_(bstack1l11lll1ll_opy_, bstack1l11l11111_opy_))
    if bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫଠ") in caps:
      caps[bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨଡ")] = caps[bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ଢ")]
      del (caps[bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧଣ")])
    if bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫତ") in caps:
      caps[bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ଥ")] = caps[bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଦ")]
      del (caps[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧଧ")])
  return caps
def bstack1l11111111_opy_():
  global bstack1l111l1ll1_opy_
  global CONFIG
  if bstack11l1l1l111_opy_() <= version.parse(bstack11l1111_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧନ")):
    if bstack1l111l1ll1_opy_ != bstack11l1111_opy_ (u"ࠨࠩ଩"):
      return bstack11l1111_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥପ") + bstack1l111l1ll1_opy_ + bstack11l1111_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢଫ")
    return bstack1ll11l1lll_opy_
  if bstack1l111l1ll1_opy_ != bstack11l1111_opy_ (u"ࠫࠬବ"):
    return bstack11l1111_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢଭ") + bstack1l111l1ll1_opy_ + bstack11l1111_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢମ")
  return bstack1l111l111_opy_
def bstack11l11lll1l_opy_(options):
  return hasattr(options, bstack11l1111_opy_ (u"ࠧࡴࡧࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠨଯ"))
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
def bstack1l1lll1ll_opy_(options, bstack1l11ll11l1_opy_):
  for bstack1l1lll1lll_opy_ in bstack1l11ll11l1_opy_:
    if bstack1l1lll1lll_opy_ in [bstack11l1111_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ର"), bstack11l1111_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭଱")]:
      continue
    if bstack1l1lll1lll_opy_ in options._experimental_options:
      options._experimental_options[bstack1l1lll1lll_opy_] = update(options._experimental_options[bstack1l1lll1lll_opy_],
                                                         bstack1l11ll11l1_opy_[bstack1l1lll1lll_opy_])
    else:
      options.add_experimental_option(bstack1l1lll1lll_opy_, bstack1l11ll11l1_opy_[bstack1l1lll1lll_opy_])
  if bstack11l1111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଲ") in bstack1l11ll11l1_opy_:
    for arg in bstack1l11ll11l1_opy_[bstack11l1111_opy_ (u"ࠫࡦࡸࡧࡴࠩଳ")]:
      options.add_argument(arg)
    del (bstack1l11ll11l1_opy_[bstack11l1111_opy_ (u"ࠬࡧࡲࡨࡵࠪ଴")])
  if bstack11l1111_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪଵ") in bstack1l11ll11l1_opy_:
    for ext in bstack1l11ll11l1_opy_[bstack11l1111_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫଶ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l11ll11l1_opy_[bstack11l1111_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬଷ")])
def bstack1lllll11l1_opy_(options, bstack1111l1ll1l_opy_):
  if bstack11l1111_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨସ") in bstack1111l1ll1l_opy_:
    for bstack1l1111l1l1_opy_ in bstack1111l1ll1l_opy_[bstack11l1111_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩହ")]:
      if bstack1l1111l1l1_opy_ in options._preferences:
        options._preferences[bstack1l1111l1l1_opy_] = update(options._preferences[bstack1l1111l1l1_opy_], bstack1111l1ll1l_opy_[bstack11l1111_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ଺")][bstack1l1111l1l1_opy_])
      else:
        options.set_preference(bstack1l1111l1l1_opy_, bstack1111l1ll1l_opy_[bstack11l1111_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ଻")][bstack1l1111l1l1_opy_])
  if bstack11l1111_opy_ (u"࠭ࡡࡳࡩࡶ଼ࠫ") in bstack1111l1ll1l_opy_:
    for arg in bstack1111l1ll1l_opy_[bstack11l1111_opy_ (u"ࠧࡢࡴࡪࡷࠬଽ")]:
      options.add_argument(arg)
def bstack1ll1lll11_opy_(options, bstack1llll11111_opy_):
  if bstack11l1111_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࠩା") in bstack1llll11111_opy_:
    options.use_webview(bool(bstack1llll11111_opy_[bstack11l1111_opy_ (u"ࠩࡺࡩࡧࡼࡩࡦࡹࠪି")]))
  bstack1l1lll1ll_opy_(options, bstack1llll11111_opy_)
def bstack1l1l1l1111_opy_(options, bstack111l11ll1_opy_):
  for bstack11lllll11_opy_ in bstack111l11ll1_opy_:
    if bstack11lllll11_opy_ in [bstack11l1111_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧୀ"), bstack11l1111_opy_ (u"ࠫࡦࡸࡧࡴࠩୁ")]:
      continue
    options.set_capability(bstack11lllll11_opy_, bstack111l11ll1_opy_[bstack11lllll11_opy_])
  if bstack11l1111_opy_ (u"ࠬࡧࡲࡨࡵࠪୂ") in bstack111l11ll1_opy_:
    for arg in bstack111l11ll1_opy_[bstack11l1111_opy_ (u"࠭ࡡࡳࡩࡶࠫୃ")]:
      options.add_argument(arg)
  if bstack11l1111_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫୄ") in bstack111l11ll1_opy_:
    options.bstack1l1l11l11l_opy_(bool(bstack111l11ll1_opy_[bstack11l1111_opy_ (u"ࠨࡶࡨࡧ࡭ࡴ࡯࡭ࡱࡪࡽࡕࡸࡥࡷ࡫ࡨࡻࠬ୅")]))
def bstack1l11ll1lll_opy_(options, bstack1l1ll1l11_opy_):
  for bstack1111111l1l_opy_ in bstack1l1ll1l11_opy_:
    if bstack1111111l1l_opy_ in [bstack11l1111_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୆"), bstack11l1111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨେ")]:
      continue
    options._options[bstack1111111l1l_opy_] = bstack1l1ll1l11_opy_[bstack1111111l1l_opy_]
  if bstack11l1111_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨୈ") in bstack1l1ll1l11_opy_:
    for bstack1lll11ll11_opy_ in bstack1l1ll1l11_opy_[bstack11l1111_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୉")]:
      options.bstack11l11111ll_opy_(
        bstack1lll11ll11_opy_, bstack1l1ll1l11_opy_[bstack11l1111_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ୊")][bstack1lll11ll11_opy_])
  if bstack11l1111_opy_ (u"ࠧࡢࡴࡪࡷࠬୋ") in bstack1l1ll1l11_opy_:
    for arg in bstack1l1ll1l11_opy_[bstack11l1111_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ୌ")]:
      options.add_argument(arg)
def bstack1l11l111ll_opy_(options, caps):
  if not hasattr(options, bstack11l1111_opy_ (u"ࠩࡎࡉ࡞୍࠭")):
    return
  if options.KEY == bstack11l1111_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ୎"):
    options = bstack1111111l_opy_.bstack1l1lll1111_opy_(bstack1l1l111ll_opy_=options, config=CONFIG)
  if options.KEY == bstack11l1111_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୏") and options.KEY in caps:
    bstack1l1lll1ll_opy_(options, caps[bstack11l1111_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ୐")])
  elif options.KEY == bstack11l1111_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫ୑") and options.KEY in caps:
    bstack1lllll11l1_opy_(options, caps[bstack11l1111_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬ୒")])
  elif options.KEY == bstack11l1111_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ୓") and options.KEY in caps:
    bstack1l1l1l1111_opy_(options, caps[bstack11l1111_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪ୔")])
  elif options.KEY == bstack11l1111_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫ୕") and options.KEY in caps:
    bstack1ll1lll11_opy_(options, caps[bstack11l1111_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬୖ")])
  elif options.KEY == bstack11l1111_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫୗ") and options.KEY in caps:
    bstack1l11ll1lll_opy_(options, caps[bstack11l1111_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬ୘")])
def bstack111ll1l1ll_opy_(caps):
  global bstack111l111111_opy_
  if isinstance(os.environ.get(bstack11l1111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ୙")), str):
    bstack111l111111_opy_ = eval(os.getenv(bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ୚")))
  if bstack111l111111_opy_:
    if bstack1ll11ll111_opy_() < version.parse(bstack11l1111_opy_ (u"ࠩ࠵࠲࠸࠴࠰ࠨ୛")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11l1111_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪଡ଼")
    if bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଢ଼") in caps:
      browser = caps[bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ୞")]
    elif bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧୟ") in caps:
      browser = caps[bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨୠ")]
    browser = str(browser).lower()
    if browser == bstack11l1111_opy_ (u"ࠨ࡫ࡳ࡬ࡴࡴࡥࠨୡ") or browser == bstack11l1111_opy_ (u"ࠩ࡬ࡴࡦࡪࠧୢ"):
      browser = bstack11l1111_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪୣ")
    if browser == bstack11l1111_opy_ (u"ࠫࡸࡧ࡭ࡴࡷࡱ࡫ࠬ୤"):
      browser = bstack11l1111_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ୥")
    if browser not in [bstack11l1111_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭୦"), bstack11l1111_opy_ (u"ࠧࡦࡦࡪࡩࠬ୧"), bstack11l1111_opy_ (u"ࠨ࡫ࡨࠫ୨"), bstack11l1111_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩ୩"), bstack11l1111_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫ୪")]:
      return None
    try:
      package = bstack11l1111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡾࢁ࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭୫").format(browser)
      name = bstack11l1111_opy_ (u"ࠬࡕࡰࡵ࡫ࡲࡲࡸ࠭୬")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11l11lll1l_opy_(options):
        return None
      for bstack1ll11ll11_opy_ in caps.keys():
        options.set_capability(bstack1ll11ll11_opy_, caps[bstack1ll11ll11_opy_])
      bstack1l11l111ll_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack1l11llll1l_opy_(options, bstack11lllll1l_opy_):
  if not bstack11l11lll1l_opy_(options):
    return
  for bstack1ll11ll11_opy_ in bstack11lllll1l_opy_.keys():
    if bstack1ll11ll11_opy_ in bstack11l1111ll_opy_:
      continue
    if bstack1ll11ll11_opy_ in options._caps and type(options._caps[bstack1ll11ll11_opy_]) in [dict, list]:
      options._caps[bstack1ll11ll11_opy_] = update(options._caps[bstack1ll11ll11_opy_], bstack11lllll1l_opy_[bstack1ll11ll11_opy_])
    else:
      options.set_capability(bstack1ll11ll11_opy_, bstack11lllll1l_opy_[bstack1ll11ll11_opy_])
  bstack1l11l111ll_opy_(options, bstack11lllll1l_opy_)
  if bstack11l1111_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬ୭") in options._caps:
    if options._caps[bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ୮")] and options._caps[bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭୯")].lower() != bstack11l1111_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪ୰"):
      del options._caps[bstack11l1111_opy_ (u"ࠪࡱࡴࢀ࠺ࡥࡧࡥࡹ࡬࡭ࡥࡳࡃࡧࡨࡷ࡫ࡳࡴࠩୱ")]
def bstack111111111_opy_(proxy_config):
  if bstack11l1111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ୲") in proxy_config:
    proxy_config[bstack11l1111_opy_ (u"ࠬࡹࡳ࡭ࡒࡵࡳࡽࡿࠧ୳")] = proxy_config[bstack11l1111_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ୴")]
    del (proxy_config[bstack11l1111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ୵")])
  if bstack11l1111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ୶") in proxy_config and proxy_config[bstack11l1111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬ୷")].lower() != bstack11l1111_opy_ (u"ࠪࡨ࡮ࡸࡥࡤࡶࠪ୸"):
    proxy_config[bstack11l1111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧ୹")] = bstack11l1111_opy_ (u"ࠬࡳࡡ࡯ࡷࡤࡰࠬ୺")
  if bstack11l1111_opy_ (u"࠭ࡰࡳࡱࡻࡽࡆࡻࡴࡰࡥࡲࡲ࡫࡯ࡧࡖࡴ࡯ࠫ୻") in proxy_config:
    proxy_config[bstack11l1111_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪ୼")] = bstack11l1111_opy_ (u"ࠨࡲࡤࡧࠬ୽")
  return proxy_config
def bstack1l11lll11l_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11l1111_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨ୾") in config:
    return proxy
  config[bstack11l1111_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩ୿")] = bstack111111111_opy_(config[bstack11l1111_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ஀")])
  if proxy == None:
    proxy = Proxy(config[bstack11l1111_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ஁")])
  return proxy
def bstack111llll11_opy_(self):
  global CONFIG
  global bstack1lllll1l11_opy_
  try:
    proxy = bstack111lll1ll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11l1111_opy_ (u"࠭࠮ࡱࡣࡦࠫஂ")):
        proxies = bstack1l1ll11ll_opy_(proxy, bstack1l11111111_opy_())
        if len(proxies) > 0:
          protocol, bstack111l1111l_opy_ = proxies.popitem()
          if bstack11l1111_opy_ (u"ࠢ࠻࠱࠲ࠦஃ") in bstack111l1111l_opy_:
            return bstack111l1111l_opy_
          else:
            return bstack11l1111_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤ஄") + bstack111l1111l_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11l1111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨஅ").format(str(e)))
  return bstack1lllll1l11_opy_(self)
def bstack1llll1l1l1_opy_():
  global CONFIG
  return bstack111l1l1l11_opy_(CONFIG) and bstack1l1l111111_opy_() and bstack11l1l1l111_opy_() >= version.parse(bstack11l1l11ll_opy_)
def bstack1lllll1111_opy_():
  global CONFIG
  return (bstack11l1111_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ஆ") in CONFIG or bstack11l1111_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨஇ") in CONFIG) and bstack111ll1llll_opy_()
def bstack1ll1ll11l1_opy_(config):
  bstack1l1ll1ll1_opy_ = {}
  if bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩஈ") in config:
    bstack1l1ll1ll1_opy_ = config[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪஉ")]
  if bstack11l1111_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ஊ") in config:
    bstack1l1ll1ll1_opy_ = config[bstack11l1111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ஋")]
  proxy = bstack111lll1ll_opy_(config)
  if proxy:
    if proxy.endswith(bstack11l1111_opy_ (u"ࠩ࠱ࡴࡦࡩࠧ஌")) and os.path.isfile(proxy):
      bstack1l1ll1ll1_opy_[bstack11l1111_opy_ (u"ࠪ࠱ࡵࡧࡣ࠮ࡨ࡬ࡰࡪ࠭஍")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11l1111_opy_ (u"ࠫ࠳ࡶࡡࡤࠩஎ")):
        proxies = bstack1111l1l111_opy_(config, bstack1l11111111_opy_())
        if len(proxies) > 0:
          protocol, bstack111l1111l_opy_ = proxies.popitem()
          if bstack11l1111_opy_ (u"ࠧࡀ࠯࠰ࠤஏ") in bstack111l1111l_opy_:
            parsed_url = urlparse(bstack111l1111l_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11l1111_opy_ (u"ࠨ࠺࠰࠱ࠥஐ") + bstack111l1111l_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1l1ll1ll1_opy_[bstack11l1111_opy_ (u"ࠧࡱࡴࡲࡼࡾࡎ࡯ࡴࡶࠪ஑")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1l1ll1ll1_opy_[bstack11l1111_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡰࡴࡷࠫஒ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1l1ll1ll1_opy_[bstack11l1111_opy_ (u"ࠩࡳࡶࡴࡾࡹࡖࡵࡨࡶࠬஓ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1l1ll1ll1_opy_[bstack11l1111_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡤࡷࡸ࠭ஔ")] = str(parsed_url.password)
  return bstack1l1ll1ll1_opy_
def bstack1l111l111l_opy_(config):
  if bstack11l1111_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩக") in config:
    return config[bstack11l1111_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪ஖")]
  return {}
def bstack111l1l111_opy_(caps):
  global bstack11ll1l1lll_opy_
  if bstack11l1111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ஗") in caps:
    caps[bstack11l1111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ஘")][bstack11l1111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࠧங")] = True
    if bstack11ll1l1lll_opy_:
      caps[bstack11l1111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪச")][bstack11l1111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ஛")] = bstack11ll1l1lll_opy_
  else:
    caps[bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࠩஜ")] = True
    if bstack11ll1l1lll_opy_:
      caps[bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭஝")] = bstack11ll1l1lll_opy_
@measure(event_name=EVENTS.bstack1llll1ll1l_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack11ll1llll1_opy_():
  global CONFIG
  if not bstack1l11lllll1_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪஞ") in CONFIG and bstack1ll11lll11_opy_(CONFIG[bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫட")]):
    if (
      bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ஠") in CONFIG
      and bstack1ll11lll11_opy_(CONFIG[bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭஡")].get(bstack11l1111_opy_ (u"ࠪࡷࡰ࡯ࡰࡃ࡫ࡱࡥࡷࡿࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡣࡷ࡭ࡴࡴࠧ஢")))
    ):
      logger.debug(bstack11l1111_opy_ (u"ࠦࡑࡵࡣࡢ࡮ࠣࡦ࡮ࡴࡡࡳࡻࠣࡲࡴࡺࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡣࡶࠤࡸࡱࡩࡱࡄ࡬ࡲࡦࡸࡹࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࡪࡴࡡࡣ࡮ࡨࡨࠧண"))
      return
    bstack1l1ll1ll1_opy_ = bstack1ll1ll11l1_opy_(CONFIG)
    bstack11l1l111ll_opy_(CONFIG[bstack11l1111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨத")], bstack1l1ll1ll1_opy_)
def bstack11l1l111ll_opy_(key, bstack1l1ll1ll1_opy_):
  global bstack1l1l11l111_opy_
  logger.info(bstack111l11lll1_opy_)
  try:
    bstack1l1l11l111_opy_ = Local()
    bstack11ll11ll1_opy_ = {bstack11l1111_opy_ (u"࠭࡫ࡦࡻࠪ஥"): key}
    bstack11ll11ll1_opy_.update(bstack1l1ll1ll1_opy_)
    logger.debug(bstack1l1ll11ll1_opy_.format(str(bstack11ll11ll1_opy_)).replace(key, bstack11l1111_opy_ (u"ࠧ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫ஦")))
    bstack1l1l11l111_opy_.start(**bstack11ll11ll1_opy_)
    if bstack1l1l11l111_opy_.isRunning():
      logger.info(bstack111ll11l1_opy_)
  except Exception as e:
    bstack1l1l1l111l_opy_(bstack11lll111l1_opy_.format(str(e)))
def bstack11111l1ll_opy_():
  global bstack1l1l11l111_opy_
  if bstack1l1l11l111_opy_.isRunning():
    logger.info(bstack1llll1111l_opy_)
    bstack1l1l11l111_opy_.stop()
  bstack1l1l11l111_opy_ = None
def bstack11111l1l11_opy_(bstack1ll1l1lll_opy_=[]):
  global CONFIG
  bstack11ll1lll1_opy_ = []
  bstack11ll1111ll_opy_ = [bstack11l1111_opy_ (u"ࠨࡱࡶࠫ஧"), bstack11l1111_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬந"), bstack11l1111_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧன"), bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ப"), bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ஫"), bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ஬")]
  try:
    for err in bstack1ll1l1lll_opy_:
      bstack11l11llll1_opy_ = {}
      for k in bstack11ll1111ll_opy_:
        val = CONFIG[bstack11l1111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ஭")][int(err[bstack11l1111_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧம")])].get(k)
        if val:
          bstack11l11llll1_opy_[k] = val
      if(err[bstack11l1111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨய")] != bstack11l1111_opy_ (u"ࠪࠫர")):
        bstack11l11llll1_opy_[bstack11l1111_opy_ (u"ࠫࡹ࡫ࡳࡵࡵࠪற")] = {
          err[bstack11l1111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪல")]: err[bstack11l1111_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬள")]
        }
        bstack11ll1lll1_opy_.append(bstack11l11llll1_opy_)
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡳࡷࡳࡡࡵࡶ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺ࠺ࠡࠩழ") + str(e))
  finally:
    return bstack11ll1lll1_opy_
def bstack111l1ll1l1_opy_(file_name):
  bstack11lllllll_opy_ = []
  try:
    bstack11ll1ll111_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack11ll1ll111_opy_):
      with open(bstack11ll1ll111_opy_) as f:
        bstack11l111l1l1_opy_ = json.load(f)
        bstack11lllllll_opy_ = bstack11l111l1l1_opy_
      os.remove(bstack11ll1ll111_opy_)
    return bstack11lllllll_opy_
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪ࡮ࡴࡤࡪࡰࡪࠤࡪࡸࡲࡰࡴࠣࡰ࡮ࡹࡴ࠻ࠢࠪவ") + str(e))
    return bstack11lllllll_opy_
def bstack11l1ll1l11_opy_():
  try:
      from bstack_utils.constants import bstack1111l11l1_opy_, EVENTS
      from bstack_utils.helper import bstack111ll1l111_opy_, get_host_info, bstack1llll11ll_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack111l1111ll_opy_ = os.path.join(os.getcwd(), bstack11l1111_opy_ (u"ࠩ࡯ࡳ࡬࠭ஶ"), bstack11l1111_opy_ (u"ࠪ࡯ࡪࡿ࠭࡮ࡧࡷࡶ࡮ࡩࡳ࠯࡬ࡶࡳࡳ࠭ஷ"))
      lock = FileLock(bstack111l1111ll_opy_+bstack11l1111_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥஸ"))
      def bstack1l111111_opy_():
          try:
              with lock:
                  with open(bstack111l1111ll_opy_, bstack11l1111_opy_ (u"ࠧࡸࠢஹ"), encoding=bstack11l1111_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧ஺")) as file:
                      data = json.load(file)
                      config = {
                          bstack11l1111_opy_ (u"ࠢࡩࡧࡤࡨࡪࡸࡳࠣ஻"): {
                              bstack11l1111_opy_ (u"ࠣࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠢ஼"): bstack11l1111_opy_ (u"ࠤࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠧ஽"),
                          }
                      }
                      bstack11ll1l1l11_opy_ = datetime.utcnow()
                      bstack1ll11lll_opy_ = bstack11ll1l1l11_opy_.strftime(bstack11l1111_opy_ (u"ࠥࠩ࡞࠳ࠥ࡮࠯ࠨࡨ࡙ࠫࡈ࠻ࠧࡐ࠾࡙ࠪ࠮ࠦࡨ࡙࡙ࠣࡉࠢா"))
                      test_id = os.environ.get(bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩி")) if os.environ.get(bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪீ")) else bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣு"))
                      payload = {
                          bstack11l1111_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠦூ"): bstack11l1111_opy_ (u"ࠣࡵࡧ࡯ࡤ࡫ࡶࡦࡰࡷࡷࠧ௃"),
                          bstack11l1111_opy_ (u"ࠤࡧࡥࡹࡧࠢ௄"): {
                              bstack11l1111_opy_ (u"ࠥࡸࡪࡹࡴࡩࡷࡥࡣࡺࡻࡩࡥࠤ௅"): test_id,
                              bstack11l1111_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡨࡤࡪࡡࡺࠤெ"): bstack1ll11lll_opy_,
                              bstack11l1111_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࠤே"): bstack11l1111_opy_ (u"ࠨࡓࡅࡍࡉࡩࡦࡺࡵࡳࡧࡓࡩࡷ࡬࡯ࡳ࡯ࡤࡲࡨ࡫ࠢை"),
                              bstack11l1111_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡪࡴࡱࡱࠦ௉"): {
                                  bstack11l1111_opy_ (u"ࠣ࡯ࡨࡥࡸࡻࡲࡦࡵࠥொ"): data,
                                  bstack11l1111_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦோ"): bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠥࡷࡩࡱࡒࡶࡰࡌࡨࠧௌ"))
                              },
                              bstack11l1111_opy_ (u"ࠦࡺࡹࡥࡳࡡࡧࡥࡹࡧ்ࠢ"): bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠧࡻࡳࡦࡴࡑࡥࡲ࡫ࠢ௎")),
                              bstack11l1111_opy_ (u"ࠨࡨࡰࡵࡷࡣ࡮ࡴࡦࡰࠤ௏"): get_host_info()
                          }
                      }
                      bstack11l11llll_opy_ = bstack11llll111_opy_(cli.config, [bstack11l1111_opy_ (u"ࠢࡢࡲ࡬ࡷࠧௐ"), bstack11l1111_opy_ (u"ࠣࡧࡧࡷࡎࡴࡳࡵࡴࡸࡱࡪࡴࡴࡢࡶ࡬ࡳࡳࠨ௑"), bstack11l1111_opy_ (u"ࠤࡤࡴ࡮ࠨ௒")], bstack1111l11l1_opy_)
                      response = bstack111ll1l111_opy_(bstack11l1111_opy_ (u"ࠥࡔࡔ࡙ࡔࠣ௓"), bstack11l11llll_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack11l1111_opy_ (u"ࠦࡉࡧࡴࡢࠢࡶࡩࡳࡺࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡴࡰࠢࡾࢁࠥࡽࡩࡵࡪࠣࡨࡦࡺࡡࠡࡽࢀࠦ௔").format(bstack1111l11l1_opy_, payload))
                      else:
                          logger.debug(bstack11l1111_opy_ (u"ࠧࡘࡥࡲࡷࡨࡷࡹࠦࡦࡢ࡫࡯ࡩࡩࠦࡦࡰࡴࠣࡿࢂࠦࡷࡪࡶ࡫ࠤࡩࡧࡴࡢࠢࡾࢁࠧ௕").format(bstack1111l11l1_opy_, payload))
          except Exception as e:
              logger.debug(bstack11l1111_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡳࡪࠠ࡬ࡧࡼࠤࡲ࡫ࡴࡳ࡫ࡦࡷࠥࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠࡼࡿࠥ௖").format(e))
      bstack1l111111_opy_()
      bstack11lll1l1l1_opy_(bstack111l1111ll_opy_, logger)
  except:
    pass
def bstack1l111111ll_opy_():
  global bstack1l1l1l1l1_opy_
  global bstack1l1ll11111_opy_
  global bstack111ll11l11_opy_
  global bstack1ll11lll1l_opy_
  global bstack111111lll1_opy_
  global bstack1lllllllll_opy_
  global CONFIG
  bstack11lllll1l1_opy_ = os.environ.get(bstack11l1111_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨௗ"))
  if bstack11lllll1l1_opy_ in [bstack11l1111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ௘"), bstack11l1111_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ௙")]:
    bstack11ll11l1l1_opy_()
  percy.shutdown()
  if bstack1l1l1l1l1_opy_:
    logger.warning(bstack1l11lll11_opy_.format(str(bstack1l1l1l1l1_opy_)))
  else:
    try:
      bstack111lll1l1l_opy_ = bstack11l11ll11l_opy_(bstack11l1111_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩ௚"), logger)
      if bstack111lll1l1l_opy_.get(bstack11l1111_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩ௛")) and bstack111lll1l1l_opy_.get(bstack11l1111_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪ௜")).get(bstack11l1111_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ௝")):
        logger.warning(bstack1l11lll11_opy_.format(str(bstack111lll1l1l_opy_[bstack11l1111_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬ௞")][bstack11l1111_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪ௟")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack11lll1111l_opy_.invoke(Events.bstack1lll111l1l_opy_)
  logger.info(bstack11lll1ll11_opy_)
  global bstack1l1l11l111_opy_
  if bstack1l1l11l111_opy_:
    bstack11111l1ll_opy_()
  try:
    with bstack11l1l1ll11_opy_:
      bstack1ll11111ll_opy_ = bstack1l1ll11111_opy_.copy()
    for driver in bstack1ll11111ll_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack11111llll_opy_)
  if bstack1lllllllll_opy_ == bstack11l1111_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ௠"):
    bstack111111lll1_opy_ = bstack111l1ll1l1_opy_(bstack11l1111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫ௡"))
  if bstack1lllllllll_opy_ == bstack11l1111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ௢") and len(bstack1ll11lll1l_opy_) == 0:
    bstack1ll11lll1l_opy_ = bstack111l1ll1l1_opy_(bstack11l1111_opy_ (u"ࠬࡶࡷࡠࡲࡼࡸࡪࡹࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪ௣"))
    if len(bstack1ll11lll1l_opy_) == 0:
      bstack1ll11lll1l_opy_ = bstack111l1ll1l1_opy_(bstack11l1111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡰࡱࡲࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ௤"))
  bstack1ll11l1ll_opy_ = bstack11l1111_opy_ (u"ࠧࠨ௥")
  if len(bstack111ll11l11_opy_) > 0:
    bstack1ll11l1ll_opy_ = bstack11111l1l11_opy_(bstack111ll11l11_opy_)
  elif len(bstack1ll11lll1l_opy_) > 0:
    bstack1ll11l1ll_opy_ = bstack11111l1l11_opy_(bstack1ll11lll1l_opy_)
  elif len(bstack111111lll1_opy_) > 0:
    bstack1ll11l1ll_opy_ = bstack11111l1l11_opy_(bstack111111lll1_opy_)
  elif len(bstack1ll11llll1_opy_) > 0:
    bstack1ll11l1ll_opy_ = bstack11111l1l11_opy_(bstack1ll11llll1_opy_)
  if bool(bstack1ll11l1ll_opy_):
    bstack1l1l1lllll_opy_(bstack1ll11l1ll_opy_)
  else:
    bstack1l1l1lllll_opy_()
  bstack11lll1l1l1_opy_(bstack1l1ll1l111_opy_, logger)
  if bstack11lllll1l1_opy_ not in [bstack11l1111_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ௦")]:
    bstack11l1ll1l11_opy_()
  bstack11ll1l11l1_opy_.bstack11lll11l_opy_(CONFIG)
  if len(bstack111111lll1_opy_) > 0:
    sys.exit(len(bstack111111lll1_opy_))
def bstack1lll1l11ll_opy_(bstack1lll11111l_opy_, frame):
  global bstack1llll11ll_opy_
  logger.error(bstack1111l1111l_opy_)
  bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡑࡳࠬ௧"), bstack1lll11111l_opy_)
  if hasattr(signal, bstack11l1111_opy_ (u"ࠪࡗ࡮࡭࡮ࡢ࡮ࡶࠫ௨")):
    bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ௩"), signal.Signals(bstack1lll11111l_opy_).name)
  else:
    bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ௪"), bstack11l1111_opy_ (u"࠭ࡓࡊࡉࡘࡒࡐࡔࡏࡘࡐࠪ௫"))
  if cli.is_running():
    bstack11lll1111l_opy_.invoke(Events.bstack1lll111l1l_opy_)
  bstack11lllll1l1_opy_ = os.environ.get(bstack11l1111_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨ௬"))
  if bstack11lllll1l1_opy_ == bstack11l1111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ௭") and not cli.is_enabled(CONFIG):
    bstack1l11l1l1_opy_.stop(bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩ௮")))
  bstack1l111111ll_opy_()
  sys.exit(1)
def bstack1l1l1l111l_opy_(err):
  logger.critical(bstack1ll111llll_opy_.format(str(err)))
  bstack1l1l1lllll_opy_(bstack1ll111llll_opy_.format(str(err)), True)
  atexit.unregister(bstack1l111111ll_opy_)
  bstack11ll11l1l1_opy_()
  sys.exit(1)
def bstack1l111lll1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l1l1lllll_opy_(message, True)
  atexit.unregister(bstack1l111111ll_opy_)
  bstack11ll11l1l1_opy_()
  sys.exit(1)
def bstack111llll1l_opy_():
  global CONFIG
  global bstack1lll11ll1l_opy_
  global bstack111lllll1_opy_
  global bstack111l11111_opy_
  CONFIG = bstack11l111l1ll_opy_()
  load_dotenv(CONFIG.get(bstack11l1111_opy_ (u"ࠪࡩࡳࡼࡆࡪ࡮ࡨࠫ௯")))
  bstack111l111l11_opy_()
  bstack1l1l1llll_opy_()
  CONFIG = bstack1l11l1111l_opy_(CONFIG)
  update(CONFIG, bstack111lllll1_opy_)
  update(CONFIG, bstack1lll11ll1l_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1l11lll111_opy_(CONFIG)
  bstack111l11111_opy_ = bstack1l11lllll1_opy_(CONFIG)
  os.environ[bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ௰")] = bstack111l11111_opy_.__str__().lower()
  bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭௱"), bstack111l11111_opy_)
  if (bstack11l1111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௲") in CONFIG and bstack11l1111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ௳") in bstack1lll11ll1l_opy_) or (
          bstack11l1111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௴") in CONFIG and bstack11l1111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௵") not in bstack111lllll1_opy_):
    if os.getenv(bstack11l1111_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧ௶")):
      CONFIG[bstack11l1111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௷")] = os.getenv(bstack11l1111_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ௸"))
    else:
      if not CONFIG.get(bstack11l1111_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠤ௹"), bstack11l1111_opy_ (u"ࠢࠣ௺")) in bstack11llll1l1l_opy_:
        bstack1lll1ll1ll_opy_()
  elif (bstack11l1111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௻") not in CONFIG and bstack11l1111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ௼") in CONFIG) or (
          bstack11l1111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௽") in bstack111lllll1_opy_ and bstack11l1111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௾") not in bstack1lll11ll1l_opy_):
    del (CONFIG[bstack11l1111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ௿")])
  if bstack1111ll1l1l_opy_(CONFIG):
    bstack1l1l1l111l_opy_(bstack1l1ll1l1ll_opy_)
  Config.bstack1llllllll_opy_().set_property(bstack11l1111_opy_ (u"ࠨࡵࡴࡧࡵࡒࡦࡳࡥࠣఀ"), CONFIG[bstack11l1111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩఁ")])
  bstack1lll1lll11_opy_()
  bstack111l1111l1_opy_()
  if bstack111l111111_opy_ and not CONFIG.get(bstack11l1111_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠦం"), bstack11l1111_opy_ (u"ࠤࠥః")) in bstack11llll1l1l_opy_:
    CONFIG[bstack11l1111_opy_ (u"ࠪࡥࡵࡶࠧఄ")] = bstack111l11111l_opy_(CONFIG)
    logger.info(bstack1l1111l1ll_opy_.format(CONFIG[bstack11l1111_opy_ (u"ࠫࡦࡶࡰࠨఅ")]))
  if not bstack111l11111_opy_:
    CONFIG[bstack11l1111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఆ")] = [{}]
def bstack1llllll1ll_opy_(config, bstack1111l111ll_opy_):
  global CONFIG
  global bstack111l111111_opy_
  CONFIG = config
  bstack111l111111_opy_ = bstack1111l111ll_opy_
def bstack111l1111l1_opy_():
  global CONFIG
  global bstack111l111111_opy_
  if bstack11l1111_opy_ (u"࠭ࡡࡱࡲࠪఇ") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l111lll1l_opy_(e, bstack1l111lll11_opy_)
    bstack111l111111_opy_ = True
    bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ఈ"), True)
def bstack111l11111l_opy_(config):
  bstack11ll1ll11l_opy_ = bstack11l1111_opy_ (u"ࠨࠩఉ")
  app = config[bstack11l1111_opy_ (u"ࠩࡤࡴࡵ࠭ఊ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1111ll1lll_opy_:
      if os.path.exists(app):
        bstack11ll1ll11l_opy_ = bstack111l11l1ll_opy_(config, app)
      elif bstack11l1lllll1_opy_(app):
        bstack11ll1ll11l_opy_ = app
      else:
        bstack1l1l1l111l_opy_(bstack11llll1lll_opy_.format(app))
    else:
      if bstack11l1lllll1_opy_(app):
        bstack11ll1ll11l_opy_ = app
      elif os.path.exists(app):
        bstack11ll1ll11l_opy_ = bstack111l11l1ll_opy_(app)
      else:
        bstack1l1l1l111l_opy_(bstack1l1l1l11ll_opy_)
  else:
    if len(app) > 2:
      bstack1l1l1l111l_opy_(bstack1ll1111l1l_opy_)
    elif len(app) == 2:
      if bstack11l1111_opy_ (u"ࠪࡴࡦࡺࡨࠨఋ") in app and bstack11l1111_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧఌ") in app:
        if os.path.exists(app[bstack11l1111_opy_ (u"ࠬࡶࡡࡵࡪࠪ఍")]):
          bstack11ll1ll11l_opy_ = bstack111l11l1ll_opy_(config, app[bstack11l1111_opy_ (u"࠭ࡰࡢࡶ࡫ࠫఎ")], app[bstack11l1111_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪఏ")])
        else:
          bstack1l1l1l111l_opy_(bstack11llll1lll_opy_.format(app))
      else:
        bstack1l1l1l111l_opy_(bstack1ll1111l1l_opy_)
    else:
      for key in app:
        if key in bstack111ll1lll_opy_:
          if key == bstack11l1111_opy_ (u"ࠨࡲࡤࡸ࡭࠭ఐ"):
            if os.path.exists(app[key]):
              bstack11ll1ll11l_opy_ = bstack111l11l1ll_opy_(config, app[key])
            else:
              bstack1l1l1l111l_opy_(bstack11llll1lll_opy_.format(app))
          else:
            bstack11ll1ll11l_opy_ = app[key]
        else:
          bstack1l1l1l111l_opy_(bstack11l1111l1_opy_)
  return bstack11ll1ll11l_opy_
def bstack11l1lllll1_opy_(bstack11ll1ll11l_opy_):
  import re
  bstack1l1lll11l1_opy_ = re.compile(bstack11l1111_opy_ (u"ࡴࠥࡢࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪࠥࠤ఑"))
  bstack11ll1l1ll1_opy_ = re.compile(bstack11l1111_opy_ (u"ࡵࠦࡣࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫ࠱࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯ࠪࠢఒ"))
  if bstack11l1111_opy_ (u"ࠫࡧࡹ࠺࠰࠱ࠪఓ") in bstack11ll1ll11l_opy_ or re.fullmatch(bstack1l1lll11l1_opy_, bstack11ll1ll11l_opy_) or re.fullmatch(bstack11ll1l1ll1_opy_, bstack11ll1ll11l_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack1l1l1ll11l_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack111l11l1ll_opy_(config, path, bstack11l1l11111_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11l1111_opy_ (u"ࠬࡸࡢࠨఔ")).read()).hexdigest()
  bstack111ll1ll1l_opy_ = bstack1l1lll111l_opy_(md5_hash)
  bstack11ll1ll11l_opy_ = None
  if bstack111ll1ll1l_opy_:
    logger.info(bstack11111l11ll_opy_.format(bstack111ll1ll1l_opy_, md5_hash))
    return bstack111ll1ll1l_opy_
  bstack11ll111l1_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack11l1111_opy_ (u"࠭ࡦࡪ࡮ࡨࠫక"): (os.path.basename(path), open(os.path.abspath(path), bstack11l1111_opy_ (u"ࠧࡳࡤࠪఖ")), bstack11l1111_opy_ (u"ࠨࡶࡨࡼࡹ࠵ࡰ࡭ࡣ࡬ࡲࠬగ")),
      bstack11l1111_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬఘ"): bstack11l1l11111_opy_
    }
  )
  response = requests.post(bstack11l11ll1l_opy_, data=multipart_data,
                           headers={bstack11l1111_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩఙ"): multipart_data.content_type},
                           auth=(config[bstack11l1111_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭చ")], config[bstack11l1111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨఛ")]))
  try:
    res = json.loads(response.text)
    bstack11ll1ll11l_opy_ = res[bstack11l1111_opy_ (u"࠭ࡡࡱࡲࡢࡹࡷࡲࠧజ")]
    logger.info(bstack1l1l1ll1l_opy_.format(bstack11ll1ll11l_opy_))
    bstack1lll11llll_opy_(md5_hash, bstack11ll1ll11l_opy_)
    cli.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠢࡩࡶࡷࡴ࠿ࡻࡰ࡭ࡱࡤࡨࡤࡧࡰࡱࠤఝ"), datetime.datetime.now() - bstack11ll111l1_opy_)
  except ValueError as err:
    bstack1l1l1l111l_opy_(bstack1ll1ll1ll_opy_.format(str(err)))
  return bstack11ll1ll11l_opy_
def bstack1lll1lll11_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1l11ll1ll1_opy_
  bstack1ll1lll1l_opy_ = 1
  bstack11ll1111l_opy_ = 1
  if bstack11l1111_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨఞ") in CONFIG:
    bstack11ll1111l_opy_ = CONFIG[bstack11l1111_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩట")]
  else:
    bstack11ll1111l_opy_ = bstack1l111lllll_opy_(framework_name, args) or 1
  if bstack11l1111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ఠ") in CONFIG:
    bstack1ll1lll1l_opy_ = len(CONFIG[bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧడ")])
  bstack1l11ll1ll1_opy_ = int(bstack11ll1111l_opy_) * int(bstack1ll1lll1l_opy_)
def bstack1l111lllll_opy_(framework_name, args):
  if framework_name == bstack11111111l_opy_ and args and bstack11l1111_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪఢ") in args:
      bstack1l1ll1l1l_opy_ = args.index(bstack11l1111_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫణ"))
      return int(args[bstack1l1ll1l1l_opy_ + 1]) or 1
  return 1
def bstack1l1lll111l_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l1111_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠢࡱࡳࡹࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡥࡥࡸ࡯ࡣࠡࡨ࡬ࡰࡪࠦ࡯ࡱࡧࡵࡥࡹ࡯࡯࡯ࡵࠪత"))
    bstack11l1l11l1l_opy_ = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠨࢀࠪథ")), bstack11l1111_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩద"), bstack11l1111_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫధ"))
    if os.path.exists(bstack11l1l11l1l_opy_):
      try:
        bstack1llll1l11l_opy_ = json.load(open(bstack11l1l11l1l_opy_, bstack11l1111_opy_ (u"ࠫࡷࡨࠧన")))
        if md5_hash in bstack1llll1l11l_opy_:
          bstack111llllll_opy_ = bstack1llll1l11l_opy_[md5_hash]
          bstack11l11111l_opy_ = datetime.datetime.now()
          bstack11lll1l11l_opy_ = datetime.datetime.strptime(bstack111llllll_opy_[bstack11l1111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ఩")], bstack11l1111_opy_ (u"࠭ࠥࡥ࠱ࠨࡱ࠴࡙ࠫࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪప"))
          if (bstack11l11111l_opy_ - bstack11lll1l11l_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack111llllll_opy_[bstack11l1111_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬఫ")]):
            return None
          return bstack111llllll_opy_[bstack11l1111_opy_ (u"ࠨ࡫ࡧࠫబ")]
      except Exception as e:
        logger.debug(bstack11l1111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡐࡈ࠺ࠦࡨࡢࡵ࡫ࠤ࡫࡯࡬ࡦ࠼ࠣࡿࢂ࠭భ").format(str(e)))
    return None
  bstack11l1l11l1l_opy_ = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠪࢂࠬమ")), bstack11l1111_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫయ"), bstack11l1111_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ర"))
  lock_file = bstack11l1l11l1l_opy_ + bstack11l1111_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬఱ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack11l1l11l1l_opy_):
        with open(bstack11l1l11l1l_opy_, bstack11l1111_opy_ (u"ࠧࡳࠩల")) as f:
          content = f.read().strip()
          if content:
            bstack1llll1l11l_opy_ = json.loads(content)
            if md5_hash in bstack1llll1l11l_opy_:
              bstack111llllll_opy_ = bstack1llll1l11l_opy_[md5_hash]
              bstack11l11111l_opy_ = datetime.datetime.now()
              bstack11lll1l11l_opy_ = datetime.datetime.strptime(bstack111llllll_opy_[bstack11l1111_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫళ")], bstack11l1111_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ఴ"))
              if (bstack11l11111l_opy_ - bstack11lll1l11l_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack111llllll_opy_[bstack11l1111_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨవ")]):
                return None
              return bstack111llllll_opy_[bstack11l1111_opy_ (u"ࠫ࡮ࡪࠧశ")]
      return None
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡼ࡯ࡴࡩࠢࡩ࡭ࡱ࡫ࠠ࡭ࡱࡦ࡯࡮ࡴࡧࠡࡨࡲࡶࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮࠺ࠡࡽࢀࠫష").format(str(e)))
    return None
def bstack1lll11llll_opy_(md5_hash, bstack11ll1ll11l_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l1111_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩస"))
    bstack1111llll1l_opy_ = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠧࡿࠩహ")), bstack11l1111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ఺"))
    if not os.path.exists(bstack1111llll1l_opy_):
      os.makedirs(bstack1111llll1l_opy_)
    bstack11l1l11l1l_opy_ = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠩࢁࠫ఻")), bstack11l1111_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭఼ࠪ"), bstack11l1111_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬఽ"))
    bstack1l1llll1l1_opy_ = {
      bstack11l1111_opy_ (u"ࠬ࡯ࡤࠨా"): bstack11ll1ll11l_opy_,
      bstack11l1111_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩి"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l1111_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫీ")),
      bstack11l1111_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ు"): str(__version__)
    }
    try:
      bstack1llll1l11l_opy_ = {}
      if os.path.exists(bstack11l1l11l1l_opy_):
        bstack1llll1l11l_opy_ = json.load(open(bstack11l1l11l1l_opy_, bstack11l1111_opy_ (u"ࠩࡵࡦࠬూ")))
      bstack1llll1l11l_opy_[md5_hash] = bstack1l1llll1l1_opy_
      with open(bstack11l1l11l1l_opy_, bstack11l1111_opy_ (u"ࠥࡻ࠰ࠨృ")) as outfile:
        json.dump(bstack1llll1l11l_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11l1111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡹࡵࡪࡡࡵ࡫ࡱ࡫ࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮ࠠࡧ࡫࡯ࡩ࠿ࠦࡻࡾࠩౄ").format(str(e)))
    return
  bstack1111llll1l_opy_ = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠬࢄࠧ౅")), bstack11l1111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ె"))
  if not os.path.exists(bstack1111llll1l_opy_):
    os.makedirs(bstack1111llll1l_opy_)
  bstack11l1l11l1l_opy_ = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠧࡿࠩే")), bstack11l1111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨై"), bstack11l1111_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪ౉"))
  lock_file = bstack11l1l11l1l_opy_ + bstack11l1111_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩొ")
  bstack1l1llll1l1_opy_ = {
    bstack11l1111_opy_ (u"ࠫ࡮ࡪࠧో"): bstack11ll1ll11l_opy_,
    bstack11l1111_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨౌ"): datetime.datetime.strftime(datetime.datetime.now(), bstack11l1111_opy_ (u"࠭ࠥࡥ࠱ࠨࡱ࠴࡙ࠫࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕ్ࠪ")),
    bstack11l1111_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ౎"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1llll1l11l_opy_ = {}
      if os.path.exists(bstack11l1l11l1l_opy_):
        with open(bstack11l1l11l1l_opy_, bstack11l1111_opy_ (u"ࠨࡴࠪ౏")) as f:
          content = f.read().strip()
          if content:
            bstack1llll1l11l_opy_ = json.loads(content)
      bstack1llll1l11l_opy_[md5_hash] = bstack1l1llll1l1_opy_
      with open(bstack11l1l11l1l_opy_, bstack11l1111_opy_ (u"ࠤࡺࠦ౐")) as outfile:
        json.dump(bstack1llll1l11l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡺ࡭ࡹ࡮ࠠࡧ࡫࡯ࡩࠥࡲ࡯ࡤ࡭࡬ࡲ࡬ࠦࡦࡰࡴࠣࡑࡉ࠻ࠠࡩࡣࡶ࡬ࠥࡻࡰࡥࡣࡷࡩ࠿ࠦࡻࡾࠩ౑").format(str(e)))
def bstack1l1l1l11l_opy_(self):
  return
def bstack1ll1l1l1l_opy_(self):
  return
def bstack1l1l11lll_opy_():
  global bstack1ll111l1l1_opy_
  bstack1ll111l1l1_opy_ = True
@measure(event_name=EVENTS.bstack1l11llllll_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack1111l1l11_opy_(self):
  global bstack1l11l1l1l1_opy_
  global bstack1l1l1lll1_opy_
  global bstack1111l111l_opy_
  try:
    if bstack11l1111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ౒") in bstack1l11l1l1l1_opy_ and self.session_id != None and bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠬࡺࡥࡴࡶࡖࡸࡦࡺࡵࡴࠩ౓"), bstack11l1111_opy_ (u"࠭ࠧ౔")) != bstack11l1111_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨౕ"):
      bstack1l1lllll11_opy_ = bstack11l1111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨౖ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11l1111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ౗")
      if bstack1l1lllll11_opy_ == bstack11l1111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪౘ"):
        bstack1lll11l1ll_opy_(logger)
      if self != None:
        bstack1llll1l111_opy_(self, bstack1l1lllll11_opy_, bstack11l1111_opy_ (u"ࠫ࠱ࠦࠧౙ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11l1111_opy_ (u"ࠬ࠭ౚ")
    if bstack11l1111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭౛") in bstack1l11l1l1l1_opy_ and getattr(threading.current_thread(), bstack11l1111_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭౜"), None):
      bstack1lllll111_opy_.bstack1llll1l1l_opy_(self, bstack1ll1l111ll_opy_, logger, wait=True)
    if bstack11l1111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨౝ") in bstack1l11l1l1l1_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1llll1l111_opy_(self, bstack11l1111_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ౞"))
      bstack1ll111l1l_opy_.bstack1111ll1111_opy_(self)
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࠦ౟") + str(e))
  bstack1111l111l_opy_(self)
  self.session_id = None
def bstack1ll111lll_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack1lll1lllll_opy_
    global bstack1l11l1l1l1_opy_
    command_executor = kwargs.get(bstack11l1111_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠧౠ"), bstack11l1111_opy_ (u"ࠬ࠭ౡ"))
    bstack111l1l1111_opy_ = False
    if type(command_executor) == str and bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩౢ") in command_executor:
      bstack111l1l1111_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪౣ") in str(getattr(command_executor, bstack11l1111_opy_ (u"ࠨࡡࡸࡶࡱ࠭౤"), bstack11l1111_opy_ (u"ࠩࠪ౥"))):
      bstack111l1l1111_opy_ = True
    else:
      kwargs = bstack1111111l_opy_.bstack1l1lll1111_opy_(bstack1l1l111ll_opy_=kwargs, config=CONFIG)
      return bstack1111ll1l1_opy_(self, *args, **kwargs)
    if bstack111l1l1111_opy_:
      bstack111l1lll1_opy_ = bstack11l1lll11l_opy_.bstack11111llll1_opy_(CONFIG, bstack1l11l1l1l1_opy_)
      if kwargs.get(bstack11l1111_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ౦")):
        kwargs[bstack11l1111_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ౧")] = bstack1lll1lllll_opy_(kwargs[bstack11l1111_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭౨")], bstack1l11l1l1l1_opy_, CONFIG, bstack111l1lll1_opy_)
      elif kwargs.get(bstack11l1111_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭౩")):
        kwargs[bstack11l1111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ౪")] = bstack1lll1lllll_opy_(kwargs[bstack11l1111_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ౫")], bstack1l11l1l1l1_opy_, CONFIG, bstack111l1lll1_opy_)
  except Exception as e:
    logger.error(bstack11l1111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫ࡩࡳࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡗࡉࡑࠠࡤࡣࡳࡷ࠿ࠦࡻࡾࠤ౬").format(str(e)))
  return bstack1111ll1l1_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack11l1ll11l1_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack111ll11lll_opy_(self, command_executor=bstack11l1111_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲࠵࠷࠽࠮࠱࠰࠳࠲࠶ࡀ࠴࠵࠶࠷ࠦ౭"), *args, **kwargs):
  global bstack1l1l1lll1_opy_
  global bstack1l1ll11111_opy_
  bstack1ll1l11ll1_opy_ = bstack1ll111lll_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack11llll1l_opy_.on():
    return bstack1ll1l11ll1_opy_
  try:
    logger.debug(bstack11l1111_opy_ (u"ࠫࡈࡵ࡭࡮ࡣࡱࡨࠥࡋࡸࡦࡥࡸࡸࡴࡸࠠࡸࡪࡨࡲࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤ࡫ࡧ࡬ࡴࡧࠣ࠱ࠥࢁࡽࠨ౮").format(str(command_executor)))
    logger.debug(bstack11l1111_opy_ (u"ࠬࡎࡵࡣࠢࡘࡖࡑࠦࡩࡴࠢ࠰ࠤࢀࢃࠧ౯").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ౰") in command_executor._url:
      bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ౱"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ౲") in command_executor):
    bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ౳"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack111lll11ll_opy_ = getattr(threading.current_thread(), bstack11l1111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫ౴"), None)
  bstack111ll1ll1_opy_ = {}
  if self.capabilities is not None:
    bstack111ll1ll1_opy_[bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪ౵")] = self.capabilities.get(bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ౶"))
    bstack111ll1ll1_opy_[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ౷")] = self.capabilities.get(bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ౸"))
    bstack111ll1ll1_opy_[bstack11l1111_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡠࡱࡳࡸ࡮ࡵ࡮ࡴࠩ౹")] = self.capabilities.get(bstack11l1111_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ౺"))
  if CONFIG.get(bstack11l1111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ౻"), False) and bstack1111111l_opy_.bstack1l1lll1l11_opy_(bstack111ll1ll1_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack11l1111_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ౼") in bstack1l11l1l1l1_opy_ or bstack11l1111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ౽") in bstack1l11l1l1l1_opy_:
    bstack1l11l1l1_opy_.bstack11ll111lll_opy_(self)
  if bstack11l1111_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭౾") in bstack1l11l1l1l1_opy_ and bstack111lll11ll_opy_ and bstack111lll11ll_opy_.get(bstack11l1111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ౿"), bstack11l1111_opy_ (u"ࠨࠩಀ")) == bstack11l1111_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪಁ"):
    bstack1l11l1l1_opy_.bstack11ll111lll_opy_(self)
  bstack1l1l1lll1_opy_ = self.session_id
  with bstack11l1l1ll11_opy_:
    bstack1l1ll11111_opy_.append(self)
  return bstack1ll1l11ll1_opy_
def bstack11llllll1_opy_(args):
  return bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵࠫಂ") in str(args)
def bstack1l1l1l1ll1_opy_(self, driver_command, *args, **kwargs):
  global bstack111l1l11l1_opy_
  global bstack1l1llll1l_opy_
  bstack1l1l11l1l_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨಃ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack11l1111_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ಄"), None)
  bstack1111lll1l1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ಅ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack11l1111_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩಆ"), None)
  bstack11111l1l1l_opy_ = getattr(self, bstack11l1111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨಇ"), None) != None and getattr(self, bstack11l1111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩಈ"), None) == True
  if not bstack1l1llll1l_opy_ and bstack11l1111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪಉ") in CONFIG and CONFIG[bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫಊ")] == True and bstack1l1ll1lll1_opy_.bstack1ll1l11l1l_opy_(driver_command) and (bstack11111l1l1l_opy_ or bstack1l1l11l1l_opy_ or bstack1111lll1l1_opy_) and not bstack11llllll1_opy_(args):
    try:
      bstack1l1llll1l_opy_ = True
      logger.debug(bstack11l1111_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࢀࢃࠧಋ").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11l1111_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡷࡨࡧ࡮ࠡࡽࢀࠫಌ").format(str(err)))
    bstack1l1llll1l_opy_ = False
  response = bstack111l1l11l1_opy_(self, driver_command, *args, **kwargs)
  if (bstack11l1111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭಍") in str(bstack1l11l1l1l1_opy_).lower() or bstack11l1111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨಎ") in str(bstack1l11l1l1l1_opy_).lower()) and bstack11llll1l_opy_.on():
    try:
      if driver_command == bstack11l1111_opy_ (u"ࠩࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࠭ಏ"):
        bstack1l11l1l1_opy_.bstack1l11lllll_opy_({
            bstack11l1111_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩಐ"): response[bstack11l1111_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪ಑")],
            bstack11l1111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬಒ"): bstack1l11l1l1_opy_.current_test_uuid() if bstack1l11l1l1_opy_.current_test_uuid() else bstack11llll1l_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack1l111ll1ll_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack1ll11lllll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1l1l1lll1_opy_
  global bstack1l1llllll1_opy_
  global bstack11lll111ll_opy_
  global bstack11l1111l11_opy_
  global bstack1ll111111_opy_
  global bstack1l11l1l1l1_opy_
  global bstack1111ll1l1_opy_
  global bstack1l1ll11111_opy_
  global bstack1l1l1ll11_opy_
  global bstack1ll1l111ll_opy_
  if os.getenv(bstack11l1111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫಓ")) is not None and bstack1111111l_opy_.bstack11ll111ll1_opy_(CONFIG) is None:
    CONFIG[bstack11l1111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧಔ")] = True
  CONFIG[bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪಕ")] = str(bstack1l11l1l1l1_opy_) + str(__version__)
  bstack1ll1l1ll1l_opy_ = os.environ[bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧಖ")]
  bstack111l1lll1_opy_ = bstack11l1lll11l_opy_.bstack11111llll1_opy_(CONFIG, bstack1l11l1l1l1_opy_)
  CONFIG[bstack11l1111_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ಗ")] = bstack1ll1l1ll1l_opy_
  CONFIG[bstack11l1111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ಘ")] = bstack111l1lll1_opy_
  if CONFIG.get(bstack11l1111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬಙ"),bstack11l1111_opy_ (u"࠭ࠧಚ")) and bstack11l1111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ಛ") in bstack1l11l1l1l1_opy_:
    CONFIG[bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨಜ")].pop(bstack11l1111_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧಝ"), None)
    CONFIG[bstack11l1111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪಞ")].pop(bstack11l1111_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩಟ"), None)
  command_executor = bstack1l11111111_opy_()
  logger.debug(bstack11l111ll1_opy_.format(command_executor))
  proxy = bstack1l11lll11l_opy_(CONFIG, proxy)
  bstack11lll1111_opy_ = 0 if bstack1l1llllll1_opy_ < 0 else bstack1l1llllll1_opy_
  try:
    if bstack11l1111l11_opy_ is True:
      bstack11lll1111_opy_ = int(multiprocessing.current_process().name)
    elif bstack1ll111111_opy_ is True:
      bstack11lll1111_opy_ = int(threading.current_thread().name)
  except:
    bstack11lll1111_opy_ = 0
  bstack11lllll1l_opy_ = bstack1l11l1l11l_opy_(CONFIG, bstack11lll1111_opy_)
  logger.debug(bstack1l1l11l1l1_opy_.format(str(bstack11lllll1l_opy_)))
  if bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩಠ") in CONFIG and bstack1ll11lll11_opy_(CONFIG[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪಡ")]):
    bstack111l1l111_opy_(bstack11lllll1l_opy_)
  if bstack1111111l_opy_.bstack11lll11lll_opy_(CONFIG, bstack11lll1111_opy_) and bstack1111111l_opy_.bstack1l1l1l1l1l_opy_(bstack11lllll1l_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack1111111l_opy_.set_capabilities(bstack11lllll1l_opy_, CONFIG)
  if desired_capabilities:
    bstack11ll1l1l1l_opy_ = bstack1l11l1111l_opy_(desired_capabilities)
    bstack11ll1l1l1l_opy_[bstack11l1111_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧಢ")] = bstack11ll11l1ll_opy_(CONFIG)
    bstack1lll111ll1_opy_ = bstack1l11l1l11l_opy_(bstack11ll1l1l1l_opy_)
    if bstack1lll111ll1_opy_:
      bstack11lllll1l_opy_ = update(bstack1lll111ll1_opy_, bstack11lllll1l_opy_)
    desired_capabilities = None
  if options:
    bstack1l11llll1l_opy_(options, bstack11lllll1l_opy_)
  if not options:
    options = bstack111ll1l1ll_opy_(bstack11lllll1l_opy_)
  bstack1ll1l111ll_opy_ = CONFIG.get(bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಣ"))[bstack11lll1111_opy_]
  if proxy and bstack11l1l1l111_opy_() >= version.parse(bstack11l1111_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩತ")):
    options.proxy(proxy)
  if options and bstack11l1l1l111_opy_() >= version.parse(bstack11l1111_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩಥ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack11l1l1l111_opy_() < version.parse(bstack11l1111_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪದ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack11lllll1l_opy_)
  logger.info(bstack1ll111ll1l_opy_)
  bstack111111l1l1_opy_.end(EVENTS.bstack1l111l1lll_opy_.value, EVENTS.bstack1l111l1lll_opy_.value + bstack11l1111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧಧ"), EVENTS.bstack1l111l1lll_opy_.value + bstack11l1111_opy_ (u"ࠨ࠺ࡦࡰࡧࠦನ"), status=True, failure=None, test_name=bstack11lll111ll_opy_)
  if bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡲࡵࡳ࡫࡯࡬ࡦࠩ಩") in kwargs:
    del kwargs[bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡳࡶࡴ࡬ࡩ࡭ࡧࠪಪ")]
  try:
    if bstack11l1l1l111_opy_() >= version.parse(bstack11l1111_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩಫ")):
      bstack1111ll1l1_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack11l1l1l111_opy_() >= version.parse(bstack11l1111_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩಬ")):
      bstack1111ll1l1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11l1l1l111_opy_() >= version.parse(bstack11l1111_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫಭ")):
      bstack1111ll1l1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1111ll1l1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack11lll1l1ll_opy_:
    logger.error(bstack11lll1l111_opy_.format(bstack11l1111_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠫಮ"), str(bstack11lll1l1ll_opy_)))
    raise bstack11lll1l1ll_opy_
  if bstack1111111l_opy_.bstack11lll11lll_opy_(CONFIG, bstack11lll1111_opy_) and bstack1111111l_opy_.bstack1l1l1l1l1l_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack11l1111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨಯ")][bstack11l1111_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ರ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack1111111l_opy_.set_capabilities(bstack11lllll1l_opy_, CONFIG)
  try:
    bstack11111ll111_opy_ = bstack11l1111_opy_ (u"ࠨࠩಱ")
    if bstack11l1l1l111_opy_() >= version.parse(bstack11l1111_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࡣ࠳ࠪಲ")):
      if self.caps is not None:
        bstack11111ll111_opy_ = self.caps.get(bstack11l1111_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥಳ"))
    else:
      if self.capabilities is not None:
        bstack11111ll111_opy_ = self.capabilities.get(bstack11l1111_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦ಴"))
    if bstack11111ll111_opy_:
      bstack1l111111l_opy_(bstack11111ll111_opy_)
      if bstack11l1l1l111_opy_() <= version.parse(bstack11l1111_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬವ")):
        self.command_executor._url = bstack11l1111_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢಶ") + bstack1l111l1ll1_opy_ + bstack11l1111_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦಷ")
      else:
        self.command_executor._url = bstack11l1111_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥಸ") + bstack11111ll111_opy_ + bstack11l1111_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥಹ")
      logger.debug(bstack11111ll11_opy_.format(bstack11111ll111_opy_))
    else:
      logger.debug(bstack1ll1l1l11_opy_.format(bstack11l1111_opy_ (u"ࠥࡓࡵࡺࡩ࡮ࡣ࡯ࠤࡍࡻࡢࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦ಺")))
  except Exception as e:
    logger.debug(bstack1ll1l1l11_opy_.format(e))
  if bstack11l1111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ಻") in bstack1l11l1l1l1_opy_:
    bstack1l11l111l1_opy_(bstack1l1llllll1_opy_, bstack1l1l1ll11_opy_)
  bstack1l1l1lll1_opy_ = self.session_id
  if bstack11l1111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ಼ࠬ") in bstack1l11l1l1l1_opy_ or bstack11l1111_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ಽ") in bstack1l11l1l1l1_opy_ or bstack11l1111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ಾ") in bstack1l11l1l1l1_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack111lll11ll_opy_ = getattr(threading.current_thread(), bstack11l1111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡕࡧࡶࡸࡒ࡫ࡴࡢࠩಿ"), None)
  if bstack11l1111_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩೀ") in bstack1l11l1l1l1_opy_ or bstack11l1111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩು") in bstack1l11l1l1l1_opy_:
    bstack1l11l1l1_opy_.bstack11ll111lll_opy_(self)
  if bstack11l1111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫೂ") in bstack1l11l1l1l1_opy_ and bstack111lll11ll_opy_ and bstack111lll11ll_opy_.get(bstack11l1111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬೃ"), bstack11l1111_opy_ (u"࠭ࠧೄ")) == bstack11l1111_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ೅"):
    bstack1l11l1l1_opy_.bstack11ll111lll_opy_(self)
  with bstack11l1l1ll11_opy_:
    bstack1l1ll11111_opy_.append(self)
  if bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫೆ") in CONFIG and bstack11l1111_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧೇ") in CONFIG[bstack11l1111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ೈ")][bstack11lll1111_opy_]:
    bstack11lll111ll_opy_ = CONFIG[bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ೉")][bstack11lll1111_opy_][bstack11l1111_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪೊ")]
  logger.debug(bstack1l111ll111_opy_.format(bstack1l1l1lll1_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1111lll111_opy_
    def bstack11llll1l11_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1111llll11_opy_
      if(bstack11l1111_opy_ (u"ࠨࡩ࡯ࡦࡨࡼ࠳ࡰࡳࠣೋ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠧࡿࠩೌ")), bstack11l1111_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ್"), bstack11l1111_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ೎")), bstack11l1111_opy_ (u"ࠪࡻࠬ೏")) as fp:
          fp.write(bstack11l1111_opy_ (u"ࠦࠧ೐"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11l1111_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢ೑")))):
          with open(args[1], bstack11l1111_opy_ (u"࠭ࡲࠨ೒")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11l1111_opy_ (u"ࠧࡢࡵࡼࡲࡨࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡡࡱࡩࡼࡖࡡࡨࡧࠫࡧࡴࡴࡴࡦࡺࡷ࠰ࠥࡶࡡࡨࡧࠣࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮࠭೓") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1lll1l1l11_opy_)
            if bstack11l1111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ೔") in CONFIG and str(CONFIG[bstack11l1111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ೕ")]).lower() != bstack11l1111_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩೖ"):
                bstack1l111l1l11_opy_ = bstack1111lll111_opy_()
                bstack1111lll11l_opy_ = bstack11l1111_opy_ (u"ࠫࠬ࠭ࠊ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠍࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶ࡡࡀࠐࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠷࡝࠼ࠌࡦࡳࡳࡹࡴࠡࡲࡢ࡭ࡳࡪࡥࡹࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠷ࡣ࠻ࠋࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯ࡵ࡯࡭ࡨ࡫ࠨ࠱࠮ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸࠯࠻ࠋࡥࡲࡲࡸࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯ࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨࠩ࠼ࠌ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰࡯ࡥࡺࡴࡣࡩࠢࡀࠤࡦࡹࡹ࡯ࡥࠣࠬࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶ࠭ࠥࡃ࠾ࠡࡽࡾࠎࠥࠦ࡬ࡦࡶࠣࡧࡦࡶࡳ࠼ࠌࠣࠤࡹࡸࡹࠡࡽࡾࠎࠥࠦࠠࠡࡥࡤࡴࡸࠦ࠽ࠡࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠬ࠿ࠏࠦࠠࡾࡿࠣࡧࡦࡺࡣࡩࠢࠫࡩࡽ࠯ࠠࡼࡽࠍࠤࠥࠦࠠࡤࡱࡱࡷࡴࡲࡥ࠯ࡧࡵࡶࡴࡸࠨࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠼ࠥ࠰ࠥ࡫ࡸࠪ࠽ࠍࠤࠥࢃࡽࠋࠢࠣࡶࡪࡺࡵࡳࡰࠣࡥࡼࡧࡩࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰ࡦࡳࡳࡴࡥࡤࡶࠫࡿࢀࠐࠠࠡࠢࠣࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺ࠺ࠡࠩࡾࡧࡩࡶࡕࡳ࡮ࢀࠫࠥ࠱ࠠࡦࡰࡦࡳࡩ࡫ࡕࡓࡋࡆࡳࡲࡶ࡯࡯ࡧࡱࡸ࠭ࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡣࡢࡲࡶ࠭࠮࠲ࠊࠡࠢࠣࠤ࠳࠴࠮࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠊࠡࠢࢀࢁ࠮ࡁࠊࡾࡿ࠾ࠎ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠊࠨࠩࠪ೗").format(bstack1l111l1l11_opy_=bstack1l111l1l11_opy_)
            lines.insert(1, bstack1111lll11l_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11l1111_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢ೘")), bstack11l1111_opy_ (u"࠭ࡷࠨ೙")) as bstack111l111l1_opy_:
              bstack111l111l1_opy_.writelines(lines)
        CONFIG[bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩ೚")] = str(bstack1l11l1l1l1_opy_) + str(__version__)
        bstack1ll1l1ll1l_opy_ = os.environ[bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭೛")]
        bstack111l1lll1_opy_ = bstack11l1lll11l_opy_.bstack11111llll1_opy_(CONFIG, bstack1l11l1l1l1_opy_)
        CONFIG[bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬ೜")] = bstack1ll1l1ll1l_opy_
        CONFIG[bstack11l1111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬೝ")] = bstack111l1lll1_opy_
        bstack11lll1111_opy_ = 0 if bstack1l1llllll1_opy_ < 0 else bstack1l1llllll1_opy_
        try:
          if bstack11l1111l11_opy_ is True:
            bstack11lll1111_opy_ = int(multiprocessing.current_process().name)
          elif bstack1ll111111_opy_ is True:
            bstack11lll1111_opy_ = int(threading.current_thread().name)
        except:
          bstack11lll1111_opy_ = 0
        CONFIG[bstack11l1111_opy_ (u"ࠦࡺࡹࡥࡘ࠵ࡆࠦೞ")] = False
        CONFIG[bstack11l1111_opy_ (u"ࠧ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ೟")] = True
        bstack11lllll1l_opy_ = bstack1l11l1l11l_opy_(CONFIG, bstack11lll1111_opy_)
        logger.debug(bstack1l1l11l1l1_opy_.format(str(bstack11lllll1l_opy_)))
        if CONFIG.get(bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪೠ")):
          bstack111l1l111_opy_(bstack11lllll1l_opy_)
        if bstack11l1111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪೡ") in CONFIG and bstack11l1111_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ೢ") in CONFIG[bstack11l1111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೣ")][bstack11lll1111_opy_]:
          bstack11lll111ll_opy_ = CONFIG[bstack11l1111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭೤")][bstack11lll1111_opy_][bstack11l1111_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ೥")]
        args.append(os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠬࢄࠧ೦")), bstack11l1111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭೧"), bstack11l1111_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩ೨")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack11lllll1l_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11l1111_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥ೩"))
      bstack1111llll11_opy_ = True
      return bstack1lll11lll1_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack1l1ll111l1_opy_(self,
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
    global bstack1l1llllll1_opy_
    global bstack11lll111ll_opy_
    global bstack11l1111l11_opy_
    global bstack1ll111111_opy_
    global bstack1l11l1l1l1_opy_
    CONFIG[bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ೪")] = str(bstack1l11l1l1l1_opy_) + str(__version__)
    bstack1ll1l1ll1l_opy_ = os.environ[bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ೫")]
    bstack111l1lll1_opy_ = bstack11l1lll11l_opy_.bstack11111llll1_opy_(CONFIG, bstack1l11l1l1l1_opy_)
    CONFIG[bstack11l1111_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧ೬")] = bstack1ll1l1ll1l_opy_
    CONFIG[bstack11l1111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧ೭")] = bstack111l1lll1_opy_
    bstack11lll1111_opy_ = 0 if bstack1l1llllll1_opy_ < 0 else bstack1l1llllll1_opy_
    try:
      if bstack11l1111l11_opy_ is True:
        bstack11lll1111_opy_ = int(multiprocessing.current_process().name)
      elif bstack1ll111111_opy_ is True:
        bstack11lll1111_opy_ = int(threading.current_thread().name)
    except:
      bstack11lll1111_opy_ = 0
    CONFIG[bstack11l1111_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ೮")] = True
    bstack11lllll1l_opy_ = bstack1l11l1l11l_opy_(CONFIG, bstack11lll1111_opy_)
    logger.debug(bstack1l1l11l1l1_opy_.format(str(bstack11lllll1l_opy_)))
    if CONFIG.get(bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ೯")):
      bstack111l1l111_opy_(bstack11lllll1l_opy_)
    if bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ೰") in CONFIG and bstack11l1111_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧೱ") in CONFIG[bstack11l1111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ೲ")][bstack11lll1111_opy_]:
      bstack11lll111ll_opy_ = CONFIG[bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧೳ")][bstack11lll1111_opy_][bstack11l1111_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ೴")]
    import urllib
    import json
    if bstack11l1111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ೵") in CONFIG and str(CONFIG[bstack11l1111_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ೶")]).lower() != bstack11l1111_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ೷"):
        bstack1l1l11lll1_opy_ = bstack1111lll111_opy_()
        bstack1l111l1l11_opy_ = bstack1l1l11lll1_opy_ + urllib.parse.quote(json.dumps(bstack11lllll1l_opy_))
    else:
        bstack1l111l1l11_opy_ = bstack11l1111_opy_ (u"ࠩࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠫ೸") + urllib.parse.quote(json.dumps(bstack11lllll1l_opy_))
    browser = self.connect(bstack1l111l1l11_opy_)
    return browser
except Exception as e:
    pass
def bstack1l11l11l1_opy_():
    global bstack1111llll11_opy_
    global bstack1l11l1l1l1_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1111l11lll_opy_
        global bstack1llll11ll_opy_
        if not bstack111l11111_opy_:
          global bstack1l11l11l11_opy_
          if not bstack1l11l11l11_opy_:
            from bstack_utils.helper import bstack1l1ll1ll1l_opy_, bstack111l1l1lll_opy_, bstack1l11ll1l1l_opy_
            bstack1l11l11l11_opy_ = bstack1l1ll1ll1l_opy_()
            bstack111l1l1lll_opy_(bstack1l11l1l1l1_opy_)
            bstack111l1lll1_opy_ = bstack11l1lll11l_opy_.bstack11111llll1_opy_(CONFIG, bstack1l11l1l1l1_opy_)
            bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"ࠥࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡑࡔࡒࡈ࡚ࡉࡔࡠࡏࡄࡔࠧ೹"), bstack111l1lll1_opy_)
          BrowserType.connect = bstack1111l11lll_opy_
          return
        BrowserType.launch = bstack1l1ll111l1_opy_
        bstack1111llll11_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack11llll1l11_opy_
      bstack1111llll11_opy_ = True
    except Exception as e:
      pass
def bstack11lll111l_opy_(context, bstack1l1111ll1l_opy_):
  try:
    context.page.evaluate(bstack11l1111_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧ೺"), bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠩ೻")+ json.dumps(bstack1l1111ll1l_opy_) + bstack11l1111_opy_ (u"ࠨࡽࡾࠤ೼"))
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢࡾࢁ࠿ࠦࡻࡾࠤ೽").format(str(e), traceback.format_exc()))
def bstack111l1l11l_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11l1111_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ೾"), bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ೿") + json.dumps(message) + bstack11l1111_opy_ (u"ࠪ࠰ࠧࡲࡥࡷࡧ࡯ࠦ࠿࠭ഀ") + json.dumps(level) + bstack11l1111_opy_ (u"ࠫࢂࢃࠧഁ"))
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠥࢁࡽ࠻ࠢࡾࢁࠧം").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack11lllll1ll_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack1l11111ll1_opy_(self, url):
  global bstack1l1l11llll_opy_
  try:
    bstack1l1llll11_opy_(url)
  except Exception as err:
    logger.debug(bstack11l111l11l_opy_.format(str(err)))
  try:
    bstack1l1l11llll_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1111l11111_opy_):
        bstack1l1llll11_opy_(url, True)
    except Exception as err:
      logger.debug(bstack11l111l11l_opy_.format(str(err)))
    raise e
def bstack1ll1lll11l_opy_(self):
  global bstack1lll1ll1l1_opy_
  bstack1lll1ll1l1_opy_ = self
  return
def bstack1ll1ll1l1l_opy_(self):
  global bstack1l1lllllll_opy_
  bstack1l1lllllll_opy_ = self
  return
def bstack1l1l1ll1l1_opy_(test_name, bstack111ll1ll11_opy_):
  global CONFIG
  if percy.bstack1ll1111ll1_opy_() == bstack11l1111_opy_ (u"ࠨࡴࡳࡷࡨࠦഃ"):
    bstack11l1lll1ll_opy_ = os.path.relpath(bstack111ll1ll11_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack11l1lll1ll_opy_)
    bstack11lll11l1l_opy_ = suite_name + bstack11l1111_opy_ (u"ࠢ࠮ࠤഄ") + test_name
    threading.current_thread().percySessionName = bstack11lll11l1l_opy_
def bstack111111l111_opy_(self, test, *args, **kwargs):
  global bstack1llll11ll1_opy_
  test_name = None
  bstack111ll1ll11_opy_ = None
  if test:
    test_name = str(test.name)
    bstack111ll1ll11_opy_ = str(test.source)
  bstack1l1l1ll1l1_opy_(test_name, bstack111ll1ll11_opy_)
  bstack1llll11ll1_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l11ll11ll_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack1lll1111l1_opy_(driver, bstack11lll11l1l_opy_):
  if not bstack11llll1ll_opy_ and bstack11lll11l1l_opy_:
      bstack111l111ll1_opy_ = {
          bstack11l1111_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨഅ"): bstack11l1111_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪആ"),
          bstack11l1111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ഇ"): {
              bstack11l1111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩഈ"): bstack11lll11l1l_opy_
          }
      }
      bstack1111l111l1_opy_ = bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪഉ").format(json.dumps(bstack111l111ll1_opy_))
      driver.execute_script(bstack1111l111l1_opy_)
  if bstack1l1111111l_opy_:
      bstack111lll1lll_opy_ = {
          bstack11l1111_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭ഊ"): bstack11l1111_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩഋ"),
          bstack11l1111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫഌ"): {
              bstack11l1111_opy_ (u"ࠩࡧࡥࡹࡧࠧ഍"): bstack11lll11l1l_opy_ + bstack11l1111_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬഎ"),
              bstack11l1111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪഏ"): bstack11l1111_opy_ (u"ࠬ࡯࡮ࡧࡱࠪഐ")
          }
      }
      if bstack1l1111111l_opy_.status == bstack11l1111_opy_ (u"࠭ࡐࡂࡕࡖࠫ഑"):
          bstack1111ll1ll1_opy_ = bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬഒ").format(json.dumps(bstack111lll1lll_opy_))
          driver.execute_script(bstack1111ll1ll1_opy_)
          bstack1llll1l111_opy_(driver, bstack11l1111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨഓ"))
      elif bstack1l1111111l_opy_.status == bstack11l1111_opy_ (u"ࠩࡉࡅࡎࡒࠧഔ"):
          reason = bstack11l1111_opy_ (u"ࠥࠦക")
          bstack11lll1l1l_opy_ = bstack11lll11l1l_opy_ + bstack11l1111_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠬഖ")
          if bstack1l1111111l_opy_.message:
              reason = str(bstack1l1111111l_opy_.message)
              bstack11lll1l1l_opy_ = bstack11lll1l1l_opy_ + bstack11l1111_opy_ (u"ࠬࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࠬഗ") + reason
          bstack111lll1lll_opy_[bstack11l1111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩഘ")] = {
              bstack11l1111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ങ"): bstack11l1111_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧച"),
              bstack11l1111_opy_ (u"ࠩࡧࡥࡹࡧࠧഛ"): bstack11lll1l1l_opy_
          }
          bstack1111ll1ll1_opy_ = bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨജ").format(json.dumps(bstack111lll1lll_opy_))
          driver.execute_script(bstack1111ll1ll1_opy_)
          bstack1llll1l111_opy_(driver, bstack11l1111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫഝ"), reason)
          bstack111l1l1l1_opy_(reason, str(bstack1l1111111l_opy_), str(bstack1l1llllll1_opy_), logger)
@measure(event_name=EVENTS.bstack111l1lll1l_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack111l1l1l1l_opy_(driver, test):
  if percy.bstack1ll1111ll1_opy_() == bstack11l1111_opy_ (u"ࠧࡺࡲࡶࡧࠥഞ") and percy.bstack1lll1ll111_opy_() == bstack11l1111_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣട"):
      bstack11l11l1l1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠧࡱࡧࡵࡧࡾ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪഠ"), None)
      bstack1ll11l1l11_opy_(driver, bstack11l11l1l1_opy_, test)
  if (bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬഡ"), None) and
      bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨഢ"), None)) or (
      bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪണ"), None) and
      bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ത"), None)):
      logger.info(bstack11l1111_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠣࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡷࡱࡨࡪࡸࡷࡢࡻ࠱ࠤࠧഥ"))
      bstack1111111l_opy_.bstack1lll1l111_opy_(driver, name=test.name, path=test.source)
def bstack11ll11l11_opy_(test, bstack11lll11l1l_opy_):
    try:
      bstack11ll111l1_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack11l1111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫദ")] = bstack11lll11l1l_opy_
      if bstack1l1111111l_opy_:
        if bstack1l1111111l_opy_.status == bstack11l1111_opy_ (u"ࠧࡑࡃࡖࡗࠬധ"):
          data[bstack11l1111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨന")] = bstack11l1111_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩഩ")
        elif bstack1l1111111l_opy_.status == bstack11l1111_opy_ (u"ࠪࡊࡆࡏࡌࠨപ"):
          data[bstack11l1111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫഫ")] = bstack11l1111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬബ")
          if bstack1l1111111l_opy_.message:
            data[bstack11l1111_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ഭ")] = str(bstack1l1111111l_opy_.message)
      user = CONFIG[bstack11l1111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩമ")]
      key = CONFIG[bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫയ")]
      host = bstack11llll111_opy_(cli.config, [bstack11l1111_opy_ (u"ࠤࡤࡴ࡮ࡹࠢര"), bstack11l1111_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࠧറ"), bstack11l1111_opy_ (u"ࠦࡦࡶࡩࠣല")], bstack11l1111_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲࠨള"))
      url = bstack11l1111_opy_ (u"࠭ࡻࡾ࠱ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡸ࡫ࡳࡴ࡫ࡲࡲࡸ࠵ࡻࡾ࠰࡭ࡷࡴࡴࠧഴ").format(host, bstack1l1l1lll1_opy_)
      headers = {
        bstack11l1111_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭വ"): bstack11l1111_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫശ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡶࡲࡧࡥࡹ࡫࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡵࡣࡷࡹࡸࠨഷ"), datetime.datetime.now() - bstack11ll111l1_opy_)
    except Exception as e:
      logger.error(bstack1l1lll1l1l_opy_.format(str(e)))
def bstack11llll111l_opy_(test, bstack11lll11l1l_opy_):
  global CONFIG
  global bstack1l1lllllll_opy_
  global bstack1lll1ll1l1_opy_
  global bstack1l1l1lll1_opy_
  global bstack1l1111111l_opy_
  global bstack11lll111ll_opy_
  global bstack11l1l111l1_opy_
  global bstack1111lllll1_opy_
  global bstack1l11l111l_opy_
  global bstack1l11ll1ll_opy_
  global bstack1l1ll11111_opy_
  global bstack1ll1l111ll_opy_
  global bstack1ll11l1l1l_opy_
  try:
    if not bstack1l1l1lll1_opy_:
      with bstack1ll11l1l1l_opy_:
        bstack11ll1l11l_opy_ = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠪࢂࠬസ")), bstack11l1111_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫഹ"), bstack11l1111_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧഺ"))
        if os.path.exists(bstack11ll1l11l_opy_):
          with open(bstack11ll1l11l_opy_, bstack11l1111_opy_ (u"࠭ࡲࠨ഻")) as f:
            content = f.read().strip()
            if content:
              bstack1l1ll11l1l_opy_ = json.loads(bstack11l1111_opy_ (u"ࠢࡼࠤ഼") + content + bstack11l1111_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪഽ") + bstack11l1111_opy_ (u"ࠤࢀࠦാ"))
              bstack1l1l1lll1_opy_ = bstack1l1ll11l1l_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡎࡊࡳࠡࡨ࡬ࡰࡪࡀࠠࠨി") + str(e))
  if bstack1l1ll11111_opy_:
    with bstack11l1l1ll11_opy_:
      bstack11l1lllll_opy_ = bstack1l1ll11111_opy_.copy()
    for driver in bstack11l1lllll_opy_:
      if bstack1l1l1lll1_opy_ == driver.session_id:
        if test:
          bstack111l1l1l1l_opy_(driver, test)
        bstack1lll1111l1_opy_(driver, bstack11lll11l1l_opy_)
  elif bstack1l1l1lll1_opy_:
    bstack11ll11l11_opy_(test, bstack11lll11l1l_opy_)
  if bstack1l1lllllll_opy_:
    bstack1111lllll1_opy_(bstack1l1lllllll_opy_)
  if bstack1lll1ll1l1_opy_:
    bstack1l11l111l_opy_(bstack1lll1ll1l1_opy_)
  if bstack1ll111l1l1_opy_:
    bstack1l11ll1ll_opy_()
def bstack11l11ll1l1_opy_(self, test, *args, **kwargs):
  bstack11lll11l1l_opy_ = None
  if test:
    bstack11lll11l1l_opy_ = str(test.name)
  bstack11llll111l_opy_(test, bstack11lll11l1l_opy_)
  bstack11l1l111l1_opy_(self, test, *args, **kwargs)
def bstack111ll1111l_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1l1l1l1l11_opy_
  global CONFIG
  global bstack1l1ll11111_opy_
  global bstack1l1l1lll1_opy_
  global bstack1ll11l1l1l_opy_
  bstack1ll1ll111_opy_ = None
  try:
    if bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪീ"), None) or bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧു"), None):
      try:
        if not bstack1l1l1lll1_opy_:
          bstack11ll1l11l_opy_ = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"࠭ࡾࠨൂ")), bstack11l1111_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧൃ"), bstack11l1111_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪൄ"))
          with bstack1ll11l1l1l_opy_:
            if os.path.exists(bstack11ll1l11l_opy_):
              with open(bstack11ll1l11l_opy_, bstack11l1111_opy_ (u"ࠩࡵࠫ൅")) as f:
                content = f.read().strip()
                if content:
                  bstack1l1ll11l1l_opy_ = json.loads(bstack11l1111_opy_ (u"ࠥࡿࠧെ") + content + bstack11l1111_opy_ (u"ࠫࠧࡾࠢ࠻ࠢࠥࡽࠧ࠭േ") + bstack11l1111_opy_ (u"ࠧࢃࠢൈ"))
                  bstack1l1l1lll1_opy_ = bstack1l1ll11l1l_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack11l1111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࡶࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥࡺࡥࡴࡶࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠬ൉") + str(e))
      if bstack1l1ll11111_opy_:
        with bstack11l1l1ll11_opy_:
          bstack11l1lllll_opy_ = bstack1l1ll11111_opy_.copy()
        for driver in bstack11l1lllll_opy_:
          if bstack1l1l1lll1_opy_ == driver.session_id:
            bstack1ll1ll111_opy_ = driver
    bstack11l111ll11_opy_ = bstack1111111l_opy_.bstack1l11l11ll1_opy_(test.tags)
    if bstack1ll1ll111_opy_:
      threading.current_thread().isA11yTest = bstack1111111l_opy_.bstack111111ll11_opy_(bstack1ll1ll111_opy_, bstack11l111ll11_opy_)
      threading.current_thread().isAppA11yTest = bstack1111111l_opy_.bstack111111ll11_opy_(bstack1ll1ll111_opy_, bstack11l111ll11_opy_)
    else:
      threading.current_thread().isA11yTest = bstack11l111ll11_opy_
      threading.current_thread().isAppA11yTest = bstack11l111ll11_opy_
  except:
    pass
  bstack1l1l1l1l11_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1l1111111l_opy_
  try:
    bstack1l1111111l_opy_ = self._test
  except:
    bstack1l1111111l_opy_ = self.test
def bstack111l1ll11l_opy_():
  global bstack11111ll1l1_opy_
  try:
    if os.path.exists(bstack11111ll1l1_opy_):
      os.remove(bstack11111ll1l1_opy_)
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪൊ") + str(e))
def bstack111l1llll_opy_():
  global bstack11111ll1l1_opy_
  bstack111lll1l1l_opy_ = {}
  lock_file = bstack11111ll1l1_opy_ + bstack11l1111_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧോ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l1111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬൌ"))
    try:
      if not os.path.isfile(bstack11111ll1l1_opy_):
        with open(bstack11111ll1l1_opy_, bstack11l1111_opy_ (u"ࠪࡻ്ࠬ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack11111ll1l1_opy_):
        with open(bstack11111ll1l1_opy_, bstack11l1111_opy_ (u"ࠫࡷ࠭ൎ")) as f:
          content = f.read().strip()
          if content:
            bstack111lll1l1l_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack11l1111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧ൏") + str(e))
    return bstack111lll1l1l_opy_
  try:
    os.makedirs(os.path.dirname(bstack11111ll1l1_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack11111ll1l1_opy_):
        with open(bstack11111ll1l1_opy_, bstack11l1111_opy_ (u"࠭ࡷࠨ൐")) as f:
          json.dump({}, f)
      if os.path.exists(bstack11111ll1l1_opy_):
        with open(bstack11111ll1l1_opy_, bstack11l1111_opy_ (u"ࠧࡳࠩ൑")) as f:
          content = f.read().strip()
          if content:
            bstack111lll1l1l_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪࡧࡤࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪ൒") + str(e))
  finally:
    return bstack111lll1l1l_opy_
def bstack1l11l111l1_opy_(platform_index, item_index):
  global bstack11111ll1l1_opy_
  lock_file = bstack11111ll1l1_opy_ + bstack11l1111_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨ൓")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11l1111_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭ൔ"))
    try:
      bstack111lll1l1l_opy_ = {}
      if os.path.exists(bstack11111ll1l1_opy_):
        with open(bstack11111ll1l1_opy_, bstack11l1111_opy_ (u"ࠫࡷ࠭ൕ")) as f:
          content = f.read().strip()
          if content:
            bstack111lll1l1l_opy_ = json.loads(content)
      bstack111lll1l1l_opy_[item_index] = platform_index
      with open(bstack11111ll1l1_opy_, bstack11l1111_opy_ (u"ࠧࡽࠢൖ")) as outfile:
        json.dump(bstack111lll1l1l_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11l1111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡹࡵ࡭ࡹ࡯࡮ࡨࠢࡷࡳࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫൗ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack11111ll1l1_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack111lll1l1l_opy_ = {}
      if os.path.exists(bstack11111ll1l1_opy_):
        with open(bstack11111ll1l1_opy_, bstack11l1111_opy_ (u"ࠧࡳࠩ൘")) as f:
          content = f.read().strip()
          if content:
            bstack111lll1l1l_opy_ = json.loads(content)
      bstack111lll1l1l_opy_[item_index] = platform_index
      with open(bstack11111ll1l1_opy_, bstack11l1111_opy_ (u"ࠣࡹࠥ൙")) as outfile:
        json.dump(bstack111lll1l1l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡼࡸࡩࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧ൚") + str(e))
def bstack1l1l1llll1_opy_(bstack1l111l1l1_opy_):
  global CONFIG
  bstack11l1ll111l_opy_ = bstack11l1111_opy_ (u"ࠪࠫ൛")
  if not bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ൜") in CONFIG:
    logger.info(bstack11l1111_opy_ (u"ࠬࡔ࡯ࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠤࡵࡧࡳࡴࡧࡧࠤࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡱࡩࡷࡧࡴࡦࠢࡵࡩࡵࡵࡲࡵࠢࡩࡳࡷࠦࡒࡰࡤࡲࡸࠥࡸࡵ࡯ࠩ൝"))
  try:
    platform = CONFIG[bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ൞")][bstack1l111l1l1_opy_]
    if bstack11l1111_opy_ (u"ࠧࡰࡵࠪൟ") in platform:
      bstack11l1ll111l_opy_ += str(platform[bstack11l1111_opy_ (u"ࠨࡱࡶࠫൠ")]) + bstack11l1111_opy_ (u"ࠩ࠯ࠤࠬൡ")
    if bstack11l1111_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ൢ") in platform:
      bstack11l1ll111l_opy_ += str(platform[bstack11l1111_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧൣ")]) + bstack11l1111_opy_ (u"ࠬ࠲ࠠࠨ൤")
    if bstack11l1111_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ൥") in platform:
      bstack11l1ll111l_opy_ += str(platform[bstack11l1111_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ൦")]) + bstack11l1111_opy_ (u"ࠨ࠮ࠣࠫ൧")
    if bstack11l1111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ൨") in platform:
      bstack11l1ll111l_opy_ += str(platform[bstack11l1111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ൩")]) + bstack11l1111_opy_ (u"ࠫ࠱ࠦࠧ൪")
    if bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ൫") in platform:
      bstack11l1ll111l_opy_ += str(platform[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ൬")]) + bstack11l1111_opy_ (u"ࠧ࠭ࠢࠪ൭")
    if bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ൮") in platform:
      bstack11l1ll111l_opy_ += str(platform[bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ൯")]) + bstack11l1111_opy_ (u"ࠪ࠰ࠥ࠭൰")
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠫࡘࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡷࡹࡸࡩ࡯ࡩࠣࡪࡴࡸࠠࡳࡧࡳࡳࡷࡺࠠࡨࡧࡱࡩࡷࡧࡴࡪࡱࡱࠫ൱") + str(e))
  finally:
    if bstack11l1ll111l_opy_[len(bstack11l1ll111l_opy_) - 2:] == bstack11l1111_opy_ (u"ࠬ࠲ࠠࠨ൲"):
      bstack11l1ll111l_opy_ = bstack11l1ll111l_opy_[:-2]
    return bstack11l1ll111l_opy_
def bstack11llll11l1_opy_(path, bstack11l1ll111l_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l111ll1l1_opy_ = ET.parse(path)
    bstack111l11ll1l_opy_ = bstack1l111ll1l1_opy_.getroot()
    bstack1l111111l1_opy_ = None
    for suite in bstack111l11ll1l_opy_.iter(bstack11l1111_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൳")):
      if bstack11l1111_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ൴") in suite.attrib:
        suite.attrib[bstack11l1111_opy_ (u"ࠨࡰࡤࡱࡪ࠭൵")] += bstack11l1111_opy_ (u"ࠩࠣࠫ൶") + bstack11l1ll111l_opy_
        bstack1l111111l1_opy_ = suite
    bstack1lllll1ll1_opy_ = None
    for robot in bstack111l11ll1l_opy_.iter(bstack11l1111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ൷")):
      bstack1lllll1ll1_opy_ = robot
    bstack1111l1lll1_opy_ = len(bstack1lllll1ll1_opy_.findall(bstack11l1111_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪ൸")))
    if bstack1111l1lll1_opy_ == 1:
      bstack1lllll1ll1_opy_.remove(bstack1lllll1ll1_opy_.findall(bstack11l1111_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫ൹"))[0])
      bstack1ll1llll11_opy_ = ET.Element(bstack11l1111_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬൺ"), attrib={bstack11l1111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬൻ"): bstack11l1111_opy_ (u"ࠨࡕࡸ࡭ࡹ࡫ࡳࠨർ"), bstack11l1111_opy_ (u"ࠩ࡬ࡨࠬൽ"): bstack11l1111_opy_ (u"ࠪࡷ࠵࠭ൾ")})
      bstack1lllll1ll1_opy_.insert(1, bstack1ll1llll11_opy_)
      bstack11ll1l1111_opy_ = None
      for suite in bstack1lllll1ll1_opy_.iter(bstack11l1111_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪൿ")):
        bstack11ll1l1111_opy_ = suite
      bstack11ll1l1111_opy_.append(bstack1l111111l1_opy_)
      bstack111l11l111_opy_ = None
      for status in bstack1l111111l1_opy_.iter(bstack11l1111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ඀")):
        bstack111l11l111_opy_ = status
      bstack11ll1l1111_opy_.append(bstack111l11l111_opy_)
    bstack1l111ll1l1_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠫඁ") + str(e))
def bstack1ll11ll11l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack11111lll1_opy_
  global CONFIG
  if bstack11l1111_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࡰࡢࡶ࡫ࠦං") in options:
    del options[bstack11l1111_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬ࠧඃ")]
  json_data = bstack111l1llll_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack11l1111_opy_ (u"ࠩࡳࡥࡧࡵࡴࡠࡴࡨࡷࡺࡲࡴࡴࠩ඄"), str(item_id), bstack11l1111_opy_ (u"ࠪࡳࡺࡺࡰࡶࡶ࠱ࡼࡲࡲࠧඅ"))
    bstack11llll11l1_opy_(path, bstack1l1l1llll1_opy_(json_data[item_id]))
  bstack111l1ll11l_opy_()
  return bstack11111lll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1l1111lll1_opy_(self, ff_profile_dir):
  global bstack1l1l11ll1l_opy_
  if not ff_profile_dir:
    return None
  return bstack1l1l11ll1l_opy_(self, ff_profile_dir)
def bstack1l11ll1111_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack11ll1l1lll_opy_
  bstack111lllll11_opy_ = []
  if bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧආ") in CONFIG:
    bstack111lllll11_opy_ = CONFIG[bstack11l1111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨඇ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11l1111_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࠢඈ")],
      pabot_args[bstack11l1111_opy_ (u"ࠢࡷࡧࡵࡦࡴࡹࡥࠣඉ")],
      argfile,
      pabot_args.get(bstack11l1111_opy_ (u"ࠣࡪ࡬ࡺࡪࠨඊ")),
      pabot_args[bstack11l1111_opy_ (u"ࠤࡳࡶࡴࡩࡥࡴࡵࡨࡷࠧඋ")],
      platform[0],
      bstack11ll1l1lll_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11l1111_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࡫࡯࡬ࡦࡵࠥඌ")] or [(bstack11l1111_opy_ (u"ࠦࠧඍ"), None)]
    for platform in enumerate(bstack111lllll11_opy_)
  ]
def bstack111l1l111l_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1ll11ll1l1_opy_=bstack11l1111_opy_ (u"ࠬ࠭ඎ")):
  global bstack11l1l1ll1_opy_
  self.platform_index = platform_index
  self.bstack111l11ll11_opy_ = bstack1ll11ll1l1_opy_
  bstack11l1l1ll1_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1111l1llll_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack111llll11l_opy_
  global bstack11ll1111l1_opy_
  bstack1l1l1l11l1_opy_ = copy.deepcopy(item)
  if not bstack11l1111_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨඏ") in item.options:
    bstack1l1l1l11l1_opy_.options[bstack11l1111_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩඐ")] = []
  bstack111111l1l_opy_ = bstack1l1l1l11l1_opy_.options[bstack11l1111_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪඑ")].copy()
  for v in bstack1l1l1l11l1_opy_.options[bstack11l1111_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫඒ")]:
    if bstack11l1111_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙ࠩඓ") in v:
      bstack111111l1l_opy_.remove(v)
    if bstack11l1111_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫඔ") in v:
      bstack111111l1l_opy_.remove(v)
    if bstack11l1111_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡉࡋࡆࡍࡑࡆࡅࡑࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩඕ") in v:
      bstack111111l1l_opy_.remove(v)
  bstack111111l1l_opy_.insert(0, bstack11l1111_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜࠿ࢁࡽࠨඖ").format(bstack1l1l1l11l1_opy_.platform_index))
  bstack111111l1l_opy_.insert(0, bstack11l1111_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕ࠾ࢀࢃࠧ඗").format(bstack1l1l1l11l1_opy_.bstack111l11ll11_opy_))
  bstack1l1l1l11l1_opy_.options[bstack11l1111_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ඘")] = bstack111111l1l_opy_
  if bstack11ll1111l1_opy_:
    bstack1l1l1l11l1_opy_.options[bstack11l1111_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ඙")].insert(0, bstack11l1111_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕ࠽ࡿࢂ࠭ක").format(bstack11ll1111l1_opy_))
  return bstack111llll11l_opy_(caller_id, datasources, is_last, bstack1l1l1l11l1_opy_, outs_dir)
def bstack11ll11ll11_opy_(command, item_index):
  try:
    if bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬඛ")):
      os.environ[bstack11l1111_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭ග")] = json.dumps(CONFIG[bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩඝ")][item_index % bstack1l1l11l1ll_opy_])
    global bstack11ll1111l1_opy_
    if bstack11ll1111l1_opy_:
      command[0] = command[0].replace(bstack11l1111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ඞ"), bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡴࡦ࡮ࠤࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠥ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡ࡬ࡲࡩ࡫ࡸࠡࠩඟ") + str(item_index % bstack1l1l11l1ll_opy_) + bstack11l1111_opy_ (u"ࠩࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠢࠪච") + str(
        item_index) + bstack11l1111_opy_ (u"ࠪࠤࠬඡ") + bstack11ll1111l1_opy_, 1)
    else:
      command[0] = command[0].replace(bstack11l1111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪජ"),
                                      bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠱ࡸࡪ࡫ࠡࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠢ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࠥ࠭ඣ") +  str(item_index % bstack1l1l11l1ll_opy_) + bstack11l1111_opy_ (u"࠭ࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽࠦࠧඤ") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack11l1111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦ࡭ࡰࡦ࡬ࡪࡾ࡯࡮ࡨࠢࡦࡳࡲࡳࡡ࡯ࡦࠣࡪࡴࡸࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰ࠽ࠤࢀࢃࠧඥ").format(str(e)))
def bstack1ll1l1111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack11ll11ll1l_opy_
  try:
    bstack11ll11ll11_opy_(command, item_index)
    return bstack11ll11ll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack11l1111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࡀࠠࡼࡿࠪඦ").format(str(e)))
    raise e
def bstack1lll1l1111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack11ll11ll1l_opy_
  try:
    bstack11ll11ll11_opy_(command, item_index)
    return bstack11ll11ll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack11l1111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠳࠰࠴࠷࠿ࠦࡻࡾࠩට").format(str(e)))
    try:
      return bstack11ll11ll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack11l1111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࠷࠴࠱࠴ࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨඨ").format(str(e2)))
      raise e
def bstack111l1ll111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack11ll11ll1l_opy_
  try:
    bstack11ll11ll11_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack11ll11ll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack11l1111_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠵࠲࠶࠻࠺ࠡࡽࢀࠫඩ").format(str(e)))
    try:
      return bstack11ll11ll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack11l1111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦ࠲࠯࠳࠸ࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪඪ").format(str(e2)))
      raise e
def _111lll111l_opy_(bstack111ll1l1l1_opy_, item_index, process_timeout, sleep_before_start, bstack1l11l1l1l_opy_):
  bstack11ll11ll11_opy_(bstack111ll1l1l1_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack11llllll11_opy_(command, bstack1l1111l111_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11ll11ll1l_opy_
  try:
    bstack11ll11ll11_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack11ll11ll1l_opy_(command, bstack1l1111l111_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11l1111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠺࠴࠰࠻ࠢࡾࢁࠬණ").format(str(e)))
    try:
      return bstack11ll11ll1l_opy_(command, bstack1l1111l111_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11l1111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡨࡤࡰࡱࡨࡡࡤ࡭࠽ࠤࢀࢃࠧඬ").format(str(e2)))
      raise e
def bstack1l1l1111l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11ll11ll1l_opy_
  try:
    process_timeout = _111lll111l_opy_(command, item_index, process_timeout, sleep_before_start, bstack11l1111_opy_ (u"ࠨ࠶࠱࠶ࠬත"))
    return bstack11ll11ll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11l1111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠵࠰࠵࠾ࠥࢁࡽࠨථ").format(str(e)))
    try:
      return bstack11ll11ll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11l1111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪද").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack1l11ll1l11_opy_(self, runner, quiet=False, capture=True):
  global bstack1llll1ll11_opy_
  bstack1l11111l1_opy_ = bstack1llll1ll11_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11l1111_opy_ (u"ࠫࡪࡾࡣࡦࡲࡷ࡭ࡴࡴ࡟ࡢࡴࡵࠫධ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11l1111_opy_ (u"ࠬ࡫ࡸࡤࡡࡷࡶࡦࡩࡥࡣࡣࡦ࡯ࡤࡧࡲࡳࠩන")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1l11111l1_opy_
def bstack1l1lllll1l_opy_(runner, hook_name, context, element, bstack111ll1lll1_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack111llll1ll_opy_.bstack11l11111_opy_(hook_name, element)
    bstack111ll1lll1_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack111llll1ll_opy_.bstack11l111l1_opy_(element)
      if hook_name not in [bstack11l1111_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪ඲"), bstack11l1111_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪඳ")] and args and hasattr(args[0], bstack11l1111_opy_ (u"ࠨࡧࡵࡶࡴࡸ࡟࡮ࡧࡶࡷࡦ࡭ࡥࠨප")):
        args[0].error_message = bstack11l1111_opy_ (u"ࠩࠪඵ")
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡨࡢࡰࡧࡰࡪࠦࡨࡰࡱ࡮ࡷࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥ࠻ࠢࡾࢁࠬබ").format(str(e)))
@measure(event_name=EVENTS.bstack11l111l111_opy_, stage=STAGE.bstack1111ll111_opy_, hook_type=bstack11l1111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡅࡱࡲࠢභ"), bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack1llll11l1l_opy_(runner, name, context, bstack111ll1lll1_opy_, *args):
    if runner.hooks.get(bstack11l1111_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤම")).__name__ != bstack11l1111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࡢࡨࡪ࡬ࡡࡶ࡮ࡷࡣ࡭ࡵ࡯࡬ࠤඹ"):
      bstack1l1lllll1l_opy_(runner, name, context, runner, bstack111ll1lll1_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack111l11l1l_opy_(bstack11l1111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ය")) else context.browser
      runner.driver_initialised = bstack11l1111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧර")
    except Exception as e:
      logger.debug(bstack11l1111_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡧࡶ࡮ࡼࡥࡳࠢ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡪࠦࡡࡵࡶࡵ࡭ࡧࡻࡴࡦ࠼ࠣࡿࢂ࠭඼").format(str(e)))
def bstack111ll1l1l_opy_(runner, name, context, bstack111ll1lll1_opy_, *args):
    bstack1l1lllll1l_opy_(runner, name, context, context.feature, bstack111ll1lll1_opy_, *args)
    try:
      if not bstack11llll1ll_opy_:
        bstack1ll1ll111_opy_ = threading.current_thread().bstackSessionDriver if bstack111l11l1l_opy_(bstack11l1111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩල")) else context.browser
        if is_driver_active(bstack1ll1ll111_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack11l1111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧ඾")
          bstack1l1111ll1l_opy_ = str(runner.feature.name)
          bstack11lll111l_opy_(context, bstack1l1111ll1l_opy_)
          bstack1ll1ll111_opy_.execute_script(bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪ඿") + json.dumps(bstack1l1111ll1l_opy_) + bstack11l1111_opy_ (u"࠭ࡽࡾࠩව"))
    except Exception as e:
      logger.debug(bstack11l1111_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡰࡤࡱࡪࠦࡩ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧශ").format(str(e)))
def bstack1l111ll1l_opy_(runner, name, context, bstack111ll1lll1_opy_, *args):
    if hasattr(context, bstack11l1111_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪෂ")):
        bstack111llll1ll_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack11l1111_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫස")) else context.feature
    bstack1l1lllll1l_opy_(runner, name, context, target, bstack111ll1lll1_opy_, *args)
@measure(event_name=EVENTS.bstack11l11l11ll_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack11lllll111_opy_(runner, name, context, bstack111ll1lll1_opy_, *args):
    if len(context.scenario.tags) == 0: bstack111llll1ll_opy_.start_test(context)
    bstack1l1lllll1l_opy_(runner, name, context, context.scenario, bstack111ll1lll1_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1ll111l1l_opy_.bstack111l1ll1ll_opy_(context, *args)
    try:
      bstack1ll1ll111_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩහ"), context.browser)
      if is_driver_active(bstack1ll1ll111_opy_):
        bstack1l11l1l1_opy_.bstack11ll111lll_opy_(bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪළ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l1111_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢෆ")
        if (not bstack11llll1ll_opy_):
          scenario_name = args[0].name
          feature_name = bstack1l1111ll1l_opy_ = str(runner.feature.name)
          bstack1l1111ll1l_opy_ = feature_name + bstack11l1111_opy_ (u"࠭ࠠ࠮ࠢࠪ෇") + scenario_name
          if runner.driver_initialised == bstack11l1111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤ෈"):
            bstack11lll111l_opy_(context, bstack1l1111ll1l_opy_)
            bstack1ll1ll111_opy_.execute_script(bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡴࡡ࡮ࡧࠥ࠾ࠥ࠭෉") + json.dumps(bstack1l1111ll1l_opy_) + bstack11l1111_opy_ (u"ࠩࢀࢁ්ࠬ"))
    except Exception as e:
      logger.debug(bstack11l1111_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢ࡬ࡲࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡦࡰࡤࡶ࡮ࡵ࠺ࠡࡽࢀࠫ෋").format(str(e)))
@measure(event_name=EVENTS.bstack11l111l111_opy_, stage=STAGE.bstack1111ll111_opy_, hook_type=bstack11l1111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡗࡹ࡫ࡰࠣ෌"), bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack1l11111l1l_opy_(runner, name, context, bstack111ll1lll1_opy_, *args):
    bstack1l1lllll1l_opy_(runner, name, context, args[0], bstack111ll1lll1_opy_, *args)
    try:
      bstack1ll1ll111_opy_ = threading.current_thread().bstackSessionDriver if bstack111l11l1l_opy_(bstack11l1111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫ෍")) else context.browser
      if is_driver_active(bstack1ll1ll111_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack11l1111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦ෎")
        bstack111llll1ll_opy_.bstack11l11ll1_opy_(args[0])
        if runner.driver_initialised == bstack11l1111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧා"):
          feature_name = bstack1l1111ll1l_opy_ = str(runner.feature.name)
          bstack1l1111ll1l_opy_ = feature_name + bstack11l1111_opy_ (u"ࠨࠢ࠰ࠤࠬැ") + context.scenario.name
          bstack1ll1ll111_opy_.execute_script(bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧෑ") + json.dumps(bstack1l1111ll1l_opy_) + bstack11l1111_opy_ (u"ࠪࢁࢂ࠭ි"))
    except Exception as e:
      logger.debug(bstack11l1111_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡵࡧࡳ࠾ࠥࢁࡽࠨී").format(str(e)))
@measure(event_name=EVENTS.bstack11l111l111_opy_, stage=STAGE.bstack1111ll111_opy_, hook_type=bstack11l1111_opy_ (u"ࠧࡧࡦࡵࡧࡵࡗࡹ࡫ࡰࠣු"), bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack1111111ll_opy_(runner, name, context, bstack111ll1lll1_opy_, *args):
  bstack111llll1ll_opy_.bstack11l11l1l_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack1ll1ll111_opy_ = threading.current_thread().bstackSessionDriver if bstack11l1111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ෕") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1ll1ll111_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack11l1111_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧූ")
        feature_name = bstack1l1111ll1l_opy_ = str(runner.feature.name)
        bstack1l1111ll1l_opy_ = feature_name + bstack11l1111_opy_ (u"ࠨࠢ࠰ࠤࠬ෗") + context.scenario.name
        bstack1ll1ll111_opy_.execute_script(bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿ࠦࠧෘ") + json.dumps(bstack1l1111ll1l_opy_) + bstack11l1111_opy_ (u"ࠪࢁࢂ࠭ෙ"))
    if str(step_status).lower() == bstack11l1111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫේ"):
      bstack11lll1ll1_opy_ = bstack11l1111_opy_ (u"ࠬ࠭ෛ")
      bstack1l1111lll_opy_ = bstack11l1111_opy_ (u"࠭ࠧො")
      bstack111llllll1_opy_ = bstack11l1111_opy_ (u"ࠧࠨෝ")
      try:
        import traceback
        bstack11lll1ll1_opy_ = runner.exception.__class__.__name__
        bstack11l1111l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1l1111lll_opy_ = bstack11l1111_opy_ (u"ࠨࠢࠪෞ").join(bstack11l1111l_opy_)
        bstack111llllll1_opy_ = bstack11l1111l_opy_[-1]
      except Exception as e:
        logger.debug(bstack1lllll111l_opy_.format(str(e)))
      bstack11lll1ll1_opy_ += bstack111llllll1_opy_
      bstack111l1l11l_opy_(context, json.dumps(str(args[0].name) + bstack11l1111_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣෟ") + str(bstack1l1111lll_opy_)),
                          bstack11l1111_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ෠"))
      if runner.driver_initialised == bstack11l1111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤ෡"):
        bstack11l1ll11l_opy_(getattr(context, bstack11l1111_opy_ (u"ࠬࡶࡡࡨࡧࠪ෢"), None), bstack11l1111_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨ෣"), bstack11lll1ll1_opy_)
        bstack1ll1ll111_opy_.execute_script(bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬ෤") + json.dumps(str(args[0].name) + bstack11l1111_opy_ (u"ࠣࠢ࠰ࠤࡋࡧࡩ࡭ࡧࡧࠥࡡࡴࠢ෥") + str(bstack1l1111lll_opy_)) + bstack11l1111_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡦࡴࡵࡳࡷࠨࡽࡾࠩ෦"))
      if runner.driver_initialised == bstack11l1111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣ෧"):
        bstack1llll1l111_opy_(bstack1ll1ll111_opy_, bstack11l1111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ෨"), bstack11l1111_opy_ (u"࡙ࠧࡣࡦࡰࡤࡶ࡮ࡵࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤ෩") + str(bstack11lll1ll1_opy_))
    else:
      bstack111l1l11l_opy_(context, bstack11l1111_opy_ (u"ࠨࡐࡢࡵࡶࡩࡩࠧࠢ෪"), bstack11l1111_opy_ (u"ࠢࡪࡰࡩࡳࠧ෫"))
      if runner.driver_initialised == bstack11l1111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨ෬"):
        bstack11l1ll11l_opy_(getattr(context, bstack11l1111_opy_ (u"ࠩࡳࡥ࡬࡫ࠧ෭"), None), bstack11l1111_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ෮"))
      bstack1ll1ll111_opy_.execute_script(bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ෯") + json.dumps(str(args[0].name) + bstack11l1111_opy_ (u"ࠧࠦ࠭ࠡࡒࡤࡷࡸ࡫ࡤࠢࠤ෰")) + bstack11l1111_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬ෱"))
      if runner.driver_initialised == bstack11l1111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧෲ"):
        bstack1llll1l111_opy_(bstack1ll1ll111_opy_, bstack11l1111_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣෳ"))
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡳࡵࡧࡳ࠾ࠥࢁࡽࠨ෴").format(str(e)))
  bstack1l1lllll1l_opy_(runner, name, context, args[0], bstack111ll1lll1_opy_, *args)
@measure(event_name=EVENTS.bstack111l1lllll_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack111l111l1l_opy_(runner, name, context, bstack111ll1lll1_opy_, *args):
  bstack111llll1ll_opy_.end_test(args[0])
  try:
    bstack11l11l11l_opy_ = args[0].status.name
    bstack1ll1ll111_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ෵"), context.browser)
    bstack1ll111l1l_opy_.bstack1111ll1111_opy_(bstack1ll1ll111_opy_)
    if str(bstack11l11l11l_opy_).lower() == bstack11l1111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ෶"):
      bstack11lll1ll1_opy_ = bstack11l1111_opy_ (u"ࠬ࠭෷")
      bstack1l1111lll_opy_ = bstack11l1111_opy_ (u"࠭ࠧ෸")
      bstack111llllll1_opy_ = bstack11l1111_opy_ (u"ࠧࠨ෹")
      try:
        import traceback
        bstack11lll1ll1_opy_ = runner.exception.__class__.__name__
        bstack11l1111l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1l1111lll_opy_ = bstack11l1111_opy_ (u"ࠨࠢࠪ෺").join(bstack11l1111l_opy_)
        bstack111llllll1_opy_ = bstack11l1111l_opy_[-1]
      except Exception as e:
        logger.debug(bstack1lllll111l_opy_.format(str(e)))
      bstack11lll1ll1_opy_ += bstack111llllll1_opy_
      bstack111l1l11l_opy_(context, json.dumps(str(args[0].name) + bstack11l1111_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣ෻") + str(bstack1l1111lll_opy_)),
                          bstack11l1111_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤ෼"))
      if runner.driver_initialised == bstack11l1111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ෽") or runner.driver_initialised == bstack11l1111_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬ෾"):
        bstack11l1ll11l_opy_(getattr(context, bstack11l1111_opy_ (u"࠭ࡰࡢࡩࡨࠫ෿"), None), bstack11l1111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ฀"), bstack11lll1ll1_opy_)
        bstack1ll1ll111_opy_.execute_script(bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ก") + json.dumps(str(args[0].name) + bstack11l1111_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣข") + str(bstack1l1111lll_opy_)) + bstack11l1111_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪฃ"))
      if runner.driver_initialised == bstack11l1111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨค") or runner.driver_initialised == bstack11l1111_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬฅ"):
        bstack1llll1l111_opy_(bstack1ll1ll111_opy_, bstack11l1111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ฆ"), bstack11l1111_opy_ (u"ࠢࡔࡥࡨࡲࡦࡸࡩࡰࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦง") + str(bstack11lll1ll1_opy_))
    else:
      bstack111l1l11l_opy_(context, bstack11l1111_opy_ (u"ࠣࡒࡤࡷࡸ࡫ࡤࠢࠤจ"), bstack11l1111_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢฉ"))
      if runner.driver_initialised == bstack11l1111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧช") or runner.driver_initialised == bstack11l1111_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫซ"):
        bstack11l1ll11l_opy_(getattr(context, bstack11l1111_opy_ (u"ࠬࡶࡡࡨࡧࠪฌ"), None), bstack11l1111_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨญ"))
      bstack1ll1ll111_opy_.execute_script(bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬฎ") + json.dumps(str(args[0].name) + bstack11l1111_opy_ (u"ࠣࠢ࠰ࠤࡕࡧࡳࡴࡧࡧࠥࠧฏ")) + bstack11l1111_opy_ (u"ࠩ࠯ࠤࠧࡲࡥࡷࡧ࡯ࠦ࠿ࠦࠢࡪࡰࡩࡳࠧࢃࡽࠨฐ"))
      if runner.driver_initialised == bstack11l1111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧฑ") or runner.driver_initialised == bstack11l1111_opy_ (u"ࠫ࡮ࡴࡳࡵࡧࡳࠫฒ"):
        bstack1llll1l111_opy_(bstack1ll1ll111_opy_, bstack11l1111_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧณ"))
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡰࡥࡷࡱࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡ࡫ࡱࠤࡦ࡬ࡴࡦࡴࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨด").format(str(e)))
  bstack1l1lllll1l_opy_(runner, name, context, context.scenario, bstack111ll1lll1_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1ll1l1l11l_opy_(runner, name, context, bstack111ll1lll1_opy_, *args):
    target = context.scenario if hasattr(context, bstack11l1111_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩต")) else context.feature
    bstack1l1lllll1l_opy_(runner, name, context, target, bstack111ll1lll1_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1ll111ll11_opy_(runner, name, context, bstack111ll1lll1_opy_, *args):
    try:
      bstack1ll1ll111_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧถ"), context.browser)
      bstack1ll1l1llll_opy_ = bstack11l1111_opy_ (u"ࠩࠪท")
      if context.failed is True:
        bstack111l1ll1l_opy_ = []
        bstack11l1ll1l1_opy_ = []
        bstack1l1l11ll1_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack111l1ll1l_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l1111l_opy_ = traceback.format_tb(exc_tb)
            bstack11111l111_opy_ = bstack11l1111_opy_ (u"ࠪࠤࠬธ").join(bstack11l1111l_opy_)
            bstack11l1ll1l1_opy_.append(bstack11111l111_opy_)
            bstack1l1l11ll1_opy_.append(bstack11l1111l_opy_[-1])
        except Exception as e:
          logger.debug(bstack1lllll111l_opy_.format(str(e)))
        bstack11lll1ll1_opy_ = bstack11l1111_opy_ (u"ࠫࠬน")
        for i in range(len(bstack111l1ll1l_opy_)):
          bstack11lll1ll1_opy_ += bstack111l1ll1l_opy_[i] + bstack1l1l11ll1_opy_[i] + bstack11l1111_opy_ (u"ࠬࡢ࡮ࠨบ")
        bstack1ll1l1llll_opy_ = bstack11l1111_opy_ (u"࠭ࠠࠨป").join(bstack11l1ll1l1_opy_)
        if runner.driver_initialised in [bstack11l1111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣผ"), bstack11l1111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧฝ")]:
          bstack111l1l11l_opy_(context, bstack1ll1l1llll_opy_, bstack11l1111_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣพ"))
          bstack11l1ll11l_opy_(getattr(context, bstack11l1111_opy_ (u"ࠪࡴࡦ࡭ࡥࠨฟ"), None), bstack11l1111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦภ"), bstack11lll1ll1_opy_)
          bstack1ll1ll111_opy_.execute_script(bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪม") + json.dumps(bstack1ll1l1llll_opy_) + bstack11l1111_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦࡪࡸࡲࡰࡴࠥࢁࢂ࠭ย"))
          bstack1llll1l111_opy_(bstack1ll1ll111_opy_, bstack11l1111_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢร"), bstack11l1111_opy_ (u"ࠣࡕࡲࡱࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯ࡴࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࡠࡳࠨฤ") + str(bstack11lll1ll1_opy_))
          bstack11l111lll1_opy_ = bstack11llll1l1_opy_(bstack1ll1l1llll_opy_, runner.feature.name, logger)
          if (bstack11l111lll1_opy_ != None):
            bstack1ll11llll1_opy_.append(bstack11l111lll1_opy_)
      else:
        if runner.driver_initialised in [bstack11l1111_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥล"), bstack11l1111_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢฦ")]:
          bstack111l1l11l_opy_(context, bstack11l1111_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢว") + str(runner.feature.name) + bstack11l1111_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢศ"), bstack11l1111_opy_ (u"ࠨࡩ࡯ࡨࡲࠦษ"))
          bstack11l1ll11l_opy_(getattr(context, bstack11l1111_opy_ (u"ࠧࡱࡣࡪࡩࠬส"), None), bstack11l1111_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣห"))
          bstack1ll1ll111_opy_.execute_script(bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧฬ") + json.dumps(bstack11l1111_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨ࠾ࠥࠨอ") + str(runner.feature.name) + bstack11l1111_opy_ (u"ࠦࠥࡶࡡࡴࡵࡨࡨࠦࠨฮ")) + bstack11l1111_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣࡿࢀࠫฯ"))
          bstack1llll1l111_opy_(bstack1ll1ll111_opy_, bstack11l1111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ะ"))
          bstack11l111lll1_opy_ = bstack11llll1l1_opy_(bstack1ll1l1llll_opy_, runner.feature.name, logger)
          if (bstack11l111lll1_opy_ != None):
            bstack1ll11llll1_opy_.append(bstack11l111lll1_opy_)
    except Exception as e:
      logger.debug(bstack11l1111_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩั").format(str(e)))
    bstack1l1lllll1l_opy_(runner, name, context, context.feature, bstack111ll1lll1_opy_, *args)
@measure(event_name=EVENTS.bstack11l111l111_opy_, stage=STAGE.bstack1111ll111_opy_, hook_type=bstack11l1111_opy_ (u"ࠣࡣࡩࡸࡪࡸࡁ࡭࡮ࠥา"), bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack1lll1l111l_opy_(runner, name, context, bstack111ll1lll1_opy_, *args):
    bstack1l1lllll1l_opy_(runner, name, context, runner, bstack111ll1lll1_opy_, *args)
def bstack1ll1l111l1_opy_(self, name, context, *args):
  try:
    if bstack111l11111_opy_:
      platform_index = int(threading.current_thread()._name) % bstack1l1l11l1ll_opy_
      bstack1l11l1ll1l_opy_ = CONFIG[bstack11l1111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬำ")][platform_index]
      os.environ[bstack11l1111_opy_ (u"ࠪࡇ࡚ࡘࡒࡆࡐࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡄࡂࡖࡄࠫิ")] = json.dumps(bstack1l11l1ll1l_opy_)
    global bstack111ll1lll1_opy_
    if not hasattr(self, bstack11l1111_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡥࡥࠩี")):
      self.driver_initialised = None
    bstack1111l1lll_opy_ = {
        bstack11l1111_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠩึ"): bstack1llll11l1l_opy_,
        bstack11l1111_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠧื"): bstack111ll1l1l_opy_,
        bstack11l1111_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡵࡣࡪุࠫ"): bstack1l111ll1l_opy_,
        bstack11l1111_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱูࠪ"): bstack11lllll111_opy_,
        bstack11l1111_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶฺࠧ"): bstack1l11111l1l_opy_,
        bstack11l1111_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡸࡪࡶࠧ฻"): bstack1111111ll_opy_,
        bstack11l1111_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬ฼"): bstack111l111l1l_opy_,
        bstack11l1111_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡹࡧࡧࠨ฽"): bstack1ll1l1l11l_opy_,
        bstack11l1111_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭฾"): bstack1ll111ll11_opy_,
        bstack11l1111_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪ฿"): bstack1lll1l111l_opy_
    }
    handler = bstack1111l1lll_opy_.get(name, bstack111ll1lll1_opy_)
    try:
      handler(self, name, context, bstack111ll1lll1_opy_, *args)
    except Exception as e:
      logger.debug(bstack11l1111_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧࠣ࡬ࡴࡵ࡫ࠡࡪࡤࡲࡩࡲࡥࡳࠢࡾࢁ࠿ࠦࡻࡾࠩเ").format(name, str(e)))
    if name in [bstack11l1111_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦࠩแ"), bstack11l1111_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠫโ"), bstack11l1111_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧใ")]:
      try:
        bstack1ll1ll111_opy_ = threading.current_thread().bstackSessionDriver if bstack111l11l1l_opy_(bstack11l1111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫไ")) else context.browser
        bstack1lllll11ll_opy_ = (
          (name == bstack11l1111_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩๅ") and self.driver_initialised == bstack11l1111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦๆ")) or
          (name == bstack11l1111_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨ็") and self.driver_initialised == bstack11l1111_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧ่ࠥ")) or
          (name == bstack11l1111_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡶࡧࡪࡴࡡࡳ࡫ࡲ้ࠫ") and self.driver_initialised in [bstack11l1111_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨ๊"), bstack11l1111_opy_ (u"ࠧ࡯࡮ࡴࡶࡨࡴ๋ࠧ")]) or
          (name == bstack11l1111_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡴࡦࡲࠪ์") and self.driver_initialised == bstack11l1111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧํ"))
        )
        if bstack1lllll11ll_opy_:
          self.driver_initialised = None
          if bstack1ll1ll111_opy_ and hasattr(bstack1ll1ll111_opy_, bstack11l1111_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠬ๎")):
            try:
              bstack1ll1ll111_opy_.quit()
            except Exception as e:
              logger.debug(bstack11l1111_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡳࡸ࡭ࡹࡺࡩ࡯ࡩࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࠦࡨࡰࡱ࡮࠾ࠥࢁࡽࠨ๏").format(str(e)))
      except Exception as e:
        logger.debug(bstack11l1111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡭ࡵ࡯࡬ࠢࡦࡰࡪࡧ࡮ࡶࡲࠣࡪࡴࡸࠠࡼࡿ࠽ࠤࢀࢃࠧ๐").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠫࡈࡸࡩࡵ࡫ࡦࡥࡱࠦࡥࡳࡴࡲࡶࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥࠡࡴࡸࡲࠥ࡮࡯ࡰ࡭ࠣࡿࢂࡀࠠࡼࡿࠪ๑").format(name, str(e)))
    try:
      bstack111ll1lll1_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack11l1111_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬ࠢࡲࡶ࡮࡭ࡩ࡯ࡣ࡯ࠤࡧ࡫ࡨࡢࡸࡨࠤ࡭ࡵ࡯࡬ࠢࡾࢁ࠿ࠦࡻࡾࠩ๒").format(name, str(e2)))
def bstack1ll1lll111_opy_(config, startdir):
  return bstack11l1111_opy_ (u"ࠨࡤࡳ࡫ࡹࡩࡷࡀࠠࡼ࠲ࢀࠦ๓").format(bstack11l1111_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨ๔"))
notset = Notset()
def bstack1l1llll111_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack11ll11l11l_opy_
  if str(name).lower() == bstack11l1111_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࠨ๕"):
    return bstack11l1111_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠣ๖")
  else:
    return bstack11ll11l11l_opy_(self, name, default, skip)
def bstack11l111lll_opy_(item, when):
  global bstack1lll1l1ll1_opy_
  try:
    bstack1lll1l1ll1_opy_(item, when)
  except Exception as e:
    pass
def bstack11l1lll1l1_opy_():
  return
def bstack1l11ll11l_opy_(type, name, status, reason, bstack111lll1l1_opy_, bstack1l1llll1ll_opy_):
  bstack111l111ll1_opy_ = {
    bstack11l1111_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪ๗"): type,
    bstack11l1111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ๘"): {}
  }
  if type == bstack11l1111_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧ๙"):
    bstack111l111ll1_opy_[bstack11l1111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ๚")][bstack11l1111_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭๛")] = bstack111lll1l1_opy_
    bstack111l111ll1_opy_[bstack11l1111_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ๜")][bstack11l1111_opy_ (u"ࠩࡧࡥࡹࡧࠧ๝")] = json.dumps(str(bstack1l1llll1ll_opy_))
  if type == bstack11l1111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ๞"):
    bstack111l111ll1_opy_[bstack11l1111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ๟")][bstack11l1111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ๠")] = name
  if type == bstack11l1111_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ๡"):
    bstack111l111ll1_opy_[bstack11l1111_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ๢")][bstack11l1111_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ๣")] = status
    if status == bstack11l1111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ๤"):
      bstack111l111ll1_opy_[bstack11l1111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭๥")][bstack11l1111_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ๦")] = json.dumps(str(reason))
  bstack1111l111l1_opy_ = bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪ๧").format(json.dumps(bstack111l111ll1_opy_))
  return bstack1111l111l1_opy_
def bstack111lll11l1_opy_(driver_command, response):
    if driver_command == bstack11l1111_opy_ (u"࠭ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࠪ๨"):
        bstack1l11l1l1_opy_.bstack1l11lllll_opy_({
            bstack11l1111_opy_ (u"ࠧࡪ࡯ࡤ࡫ࡪ࠭๩"): response[bstack11l1111_opy_ (u"ࠨࡸࡤࡰࡺ࡫ࠧ๪")],
            bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩ๫"): bstack1l11l1l1_opy_.current_test_uuid()
        })
def bstack11ll11l1l_opy_(item, call, rep):
  global bstack11l111l1l_opy_
  global bstack1l1ll11111_opy_
  global bstack11llll1ll_opy_
  name = bstack11l1111_opy_ (u"ࠪࠫ๬")
  try:
    if rep.when == bstack11l1111_opy_ (u"ࠫࡨࡧ࡬࡭ࠩ๭"):
      bstack1l1l1lll1_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack11llll1ll_opy_:
          name = str(rep.nodeid)
          bstack1ll11l111_opy_ = bstack1l11ll11l_opy_(bstack11l1111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭๮"), name, bstack11l1111_opy_ (u"࠭ࠧ๯"), bstack11l1111_opy_ (u"ࠧࠨ๰"), bstack11l1111_opy_ (u"ࠨࠩ๱"), bstack11l1111_opy_ (u"ࠩࠪ๲"))
          threading.current_thread().bstack11l11l1ll1_opy_ = name
          for driver in bstack1l1ll11111_opy_:
            if bstack1l1l1lll1_opy_ == driver.session_id:
              driver.execute_script(bstack1ll11l111_opy_)
      except Exception as e:
        logger.debug(bstack11l1111_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪ๳").format(str(e)))
      try:
        bstack11l11l111_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11l1111_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ๴"):
          status = bstack11l1111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ๵") if rep.outcome.lower() == bstack11l1111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭๶") else bstack11l1111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ๷")
          reason = bstack11l1111_opy_ (u"ࠨࠩ๸")
          if status == bstack11l1111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ๹"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11l1111_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨ๺") if status == bstack11l1111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ๻") else bstack11l1111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ๼")
          data = name + bstack11l1111_opy_ (u"࠭ࠠࡱࡣࡶࡷࡪࡪࠡࠨ๽") if status == bstack11l1111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ๾") else name + bstack11l1111_opy_ (u"ࠨࠢࡩࡥ࡮ࡲࡥࡥࠣࠣࠫ๿") + reason
          bstack111l11l11l_opy_ = bstack1l11ll11l_opy_(bstack11l1111_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫ຀"), bstack11l1111_opy_ (u"ࠪࠫກ"), bstack11l1111_opy_ (u"ࠫࠬຂ"), bstack11l1111_opy_ (u"ࠬ࠭຃"), level, data)
          for driver in bstack1l1ll11111_opy_:
            if bstack1l1l1lll1_opy_ == driver.session_id:
              driver.execute_script(bstack111l11l11l_opy_)
      except Exception as e:
        logger.debug(bstack11l1111_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡧࡴࡴࡴࡦࡺࡷࠤ࡫ࡵࡲࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡹࡥࡴࡵ࡬ࡳࡳࡀࠠࡼࡿࠪຄ").format(str(e)))
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࠠࡴࡶࡤࡸࡺࡹ࠺ࠡࡽࢀࠫ຅").format(str(e)))
  bstack11l111l1l_opy_(item, call, rep)
def bstack1ll11l1l11_opy_(driver, bstack1llll1l1ll_opy_, test=None):
  global bstack1l1llllll1_opy_
  if test != None:
    bstack11l1l11ll1_opy_ = getattr(test, bstack11l1111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ຆ"), None)
    bstack1l1111ll1_opy_ = getattr(test, bstack11l1111_opy_ (u"ࠩࡸࡹ࡮ࡪࠧງ"), None)
    PercySDK.screenshot(driver, bstack1llll1l1ll_opy_, bstack11l1l11ll1_opy_=bstack11l1l11ll1_opy_, bstack1l1111ll1_opy_=bstack1l1111ll1_opy_, bstack1l1l111l11_opy_=bstack1l1llllll1_opy_)
  else:
    PercySDK.screenshot(driver, bstack1llll1l1ll_opy_)
@measure(event_name=EVENTS.bstack1l111llll1_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack1lll11l1l1_opy_(driver):
  if bstack1l111ll11_opy_.bstack1ll1ll1lll_opy_() is True or bstack1l111ll11_opy_.capturing() is True:
    return
  bstack1l111ll11_opy_.bstack111l11llll_opy_()
  while not bstack1l111ll11_opy_.bstack1ll1ll1lll_opy_():
    bstack1111111ll1_opy_ = bstack1l111ll11_opy_.bstack1l1l111l1_opy_()
    bstack1ll11l1l11_opy_(driver, bstack1111111ll1_opy_)
  bstack1l111ll11_opy_.bstack11l11l1l1l_opy_()
def bstack111ll111l1_opy_(sequence, driver_command, response = None, bstack1l11l1lll_opy_ = None, args = None):
    try:
      if sequence != bstack11l1111_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪຈ"):
        return
      if percy.bstack1ll1111ll1_opy_() == bstack11l1111_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥຉ"):
        return
      bstack1111111ll1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠬࡶࡥࡳࡥࡼࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨຊ"), None)
      for command in bstack1111l1l11l_opy_:
        if command == driver_command:
          with bstack11l1l1ll11_opy_:
            bstack11l1lllll_opy_ = bstack1l1ll11111_opy_.copy()
          for driver in bstack11l1lllll_opy_:
            bstack1lll11l1l1_opy_(driver)
      bstack1l11ll111l_opy_ = percy.bstack1lll1ll111_opy_()
      if driver_command in bstack11ll11111l_opy_[bstack1l11ll111l_opy_]:
        bstack1l111ll11_opy_.bstack11l1llll11_opy_(bstack1111111ll1_opy_, driver_command)
    except Exception as e:
      pass
def bstack111111ll1l_opy_(framework_name):
  if bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥ࡭ࡰࡦࡢࡧࡦࡲ࡬ࡦࡦࠪ຋")):
      return
  bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫຌ"), True)
  global bstack1l11l1l1l1_opy_
  global bstack1111llll11_opy_
  global bstack111111ll1_opy_
  bstack1l11l1l1l1_opy_ = framework_name
  logger.info(bstack1111ll1l11_opy_.format(bstack1l11l1l1l1_opy_.split(bstack11l1111_opy_ (u"ࠨ࠯ࠪຍ"))[0]))
  bstack1l1ll11l1_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack111l11111_opy_:
      Service.start = bstack1l1l1l11l_opy_
      Service.stop = bstack1ll1l1l1l_opy_
      webdriver.Remote.get = bstack1l11111ll1_opy_
      WebDriver.quit = bstack1111l1l11_opy_
      webdriver.Remote.__init__ = bstack1ll11lllll_opy_
    if not bstack111l11111_opy_:
        webdriver.Remote.__init__ = bstack111ll11lll_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack1l1l1l1ll1_opy_
    bstack1111llll11_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack111l11111_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1l1l11lll_opy_
  except Exception as e:
    pass
  bstack1l11l11l1_opy_()
  if not bstack1111llll11_opy_:
    bstack1l111lll1l_opy_(bstack11l1111_opy_ (u"ࠤࡓࡥࡨࡱࡡࡨࡧࡶࠤࡳࡵࡴࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠦຎ"), bstack1l11l1111_opy_)
  if bstack1llll1l1l1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack11l1111_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫຏ")) and callable(getattr(RemoteConnection, bstack11l1111_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬຐ"))):
        RemoteConnection._get_proxy_url = bstack111llll11_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack111llll11_opy_
    except Exception as e:
      logger.error(bstack1l11ll1l1_opy_.format(str(e)))
  if bstack1lllll1111_opy_():
    bstack1l1111l11_opy_(CONFIG, logger)
  if (bstack11l1111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫຑ") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1ll1111ll1_opy_() == bstack11l1111_opy_ (u"ࠨࡴࡳࡷࡨࠦຒ"):
          bstack111111llll_opy_(bstack111ll111l1_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1l1111lll1_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1ll1ll1l1l_opy_
      except Exception as e:
        logger.warn(bstack1l11l1l11_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1ll1lll11l_opy_
      except Exception as e:
        logger.debug(bstack111l11l11_opy_ + str(e))
    except Exception as e:
      bstack1l111lll1l_opy_(e, bstack1l11l1l11_opy_)
    Output.start_test = bstack111111l111_opy_
    Output.end_test = bstack11l11ll1l1_opy_
    TestStatus.__init__ = bstack111ll1111l_opy_
    QueueItem.__init__ = bstack111l1l111l_opy_
    pabot._create_items = bstack1l11ll1111_opy_
    try:
      from pabot import __version__ as bstack1l1lll1ll1_opy_
      if version.parse(bstack1l1lll1ll1_opy_) >= version.parse(bstack11l1111_opy_ (u"ࠧ࠶࠰࠳࠲࠵࠭ຓ")):
        pabot._run = bstack11llllll11_opy_
      elif version.parse(bstack1l1lll1ll1_opy_) >= version.parse(bstack11l1111_opy_ (u"ࠨ࠶࠱࠶࠳࠶ࠧດ")):
        pabot._run = bstack1l1l1111l1_opy_
      elif version.parse(bstack1l1lll1ll1_opy_) >= version.parse(bstack11l1111_opy_ (u"ࠩ࠵࠲࠶࠻࠮࠱ࠩຕ")):
        pabot._run = bstack111l1ll111_opy_
      elif version.parse(bstack1l1lll1ll1_opy_) >= version.parse(bstack11l1111_opy_ (u"ࠪ࠶࠳࠷࠳࠯࠲ࠪຖ")):
        pabot._run = bstack1lll1l1111_opy_
      else:
        pabot._run = bstack1ll1l1111l_opy_
    except Exception as e:
      pabot._run = bstack1ll1l1111l_opy_
    pabot._create_command_for_execution = bstack1111l1llll_opy_
    pabot._report_results = bstack1ll11ll11l_opy_
  if bstack11l1111_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫທ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l111lll1l_opy_(e, bstack1lllll1lll_opy_)
    Runner.run_hook = bstack1ll1l111l1_opy_
    Step.run = bstack1l11ll1l11_opy_
  if bstack11l1111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬຘ") in str(framework_name).lower():
    if not bstack111l11111_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1ll1lll111_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack11l1lll1l1_opy_
      Config.getoption = bstack1l1llll111_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack11ll11l1l_opy_
    except Exception as e:
      pass
def bstack111ll111ll_opy_():
  global CONFIG
  if bstack11l1111_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭ນ") in CONFIG and int(CONFIG[bstack11l1111_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧບ")]) > 1:
    logger.warn(bstack1l1ll111l_opy_)
def bstack1ll1l1l1ll_opy_(arg, bstack1111ll1l_opy_, bstack11lllllll_opy_=None):
  global CONFIG
  global bstack1l111l1ll1_opy_
  global bstack111l111111_opy_
  global bstack111l11111_opy_
  global bstack1llll11ll_opy_
  bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨປ")
  if bstack1111ll1l_opy_ and isinstance(bstack1111ll1l_opy_, str):
    bstack1111ll1l_opy_ = eval(bstack1111ll1l_opy_)
  CONFIG = bstack1111ll1l_opy_[bstack11l1111_opy_ (u"ࠩࡆࡓࡓࡌࡉࡈࠩຜ")]
  bstack1l111l1ll1_opy_ = bstack1111ll1l_opy_[bstack11l1111_opy_ (u"ࠪࡌ࡚ࡈ࡟ࡖࡔࡏࠫຝ")]
  bstack111l111111_opy_ = bstack1111ll1l_opy_[bstack11l1111_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ພ")]
  bstack111l11111_opy_ = bstack1111ll1l_opy_[bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨຟ")]
  bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧຠ"), bstack111l11111_opy_)
  os.environ[bstack11l1111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩມ")] = bstack11lllll1l1_opy_
  os.environ[bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠧຢ")] = json.dumps(CONFIG)
  os.environ[bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡊࡘࡆࡤ࡛ࡒࡍࠩຣ")] = bstack1l111l1ll1_opy_
  os.environ[bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ຤")] = str(bstack111l111111_opy_)
  os.environ[bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪລ")] = str(True)
  if bstack1ll1111l1_opy_(arg, [bstack11l1111_opy_ (u"ࠬ࠳࡮ࠨ຦"), bstack11l1111_opy_ (u"࠭࠭࠮ࡰࡸࡱࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧວ")]) != -1:
    os.environ[bstack11l1111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐ࡚ࡖࡈࡗ࡙ࡥࡐࡂࡔࡄࡐࡑࡋࡌࠨຨ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack11lll1llll_opy_)
    return
  bstack1l11111l11_opy_()
  global bstack1l11ll1ll1_opy_
  global bstack1l1llllll1_opy_
  global bstack11ll1l1lll_opy_
  global bstack11ll1111l1_opy_
  global bstack1ll11lll1l_opy_
  global bstack111111ll1_opy_
  global bstack11l1111l11_opy_
  arg.append(bstack11l1111_opy_ (u"ࠣ࠯࡚ࠦຩ"))
  arg.append(bstack11l1111_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦ࠼ࡐࡳࡩࡻ࡬ࡦࠢࡤࡰࡷ࡫ࡡࡥࡻࠣ࡭ࡲࡶ࡯ࡳࡶࡨࡨ࠿ࡶࡹࡵࡧࡶࡸ࠳ࡖࡹࡵࡧࡶࡸ࡜ࡧࡲ࡯࡫ࡱ࡫ࠧສ"))
  arg.append(bstack11l1111_opy_ (u"ࠥ࠱࡜ࠨຫ"))
  arg.append(bstack11l1111_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨ࠾࡙࡮ࡥࠡࡪࡲࡳࡰ࡯࡭ࡱ࡮ࠥຬ"))
  global bstack1111ll1l1_opy_
  global bstack1111l111l_opy_
  global bstack111l1l11l1_opy_
  global bstack1l1l1l1l11_opy_
  global bstack1l1l11ll1l_opy_
  global bstack11l1l1ll1_opy_
  global bstack111llll11l_opy_
  global bstack1ll111lll1_opy_
  global bstack1l1l11llll_opy_
  global bstack1lllll1l11_opy_
  global bstack11ll11l11l_opy_
  global bstack1lll1l1ll1_opy_
  global bstack11l111l1l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1111ll1l1_opy_ = webdriver.Remote.__init__
    bstack1111l111l_opy_ = WebDriver.quit
    bstack1ll111lll1_opy_ = WebDriver.close
    bstack1l1l11llll_opy_ = WebDriver.get
    bstack111l1l11l1_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack111l1l1l11_opy_(CONFIG) and bstack1l1l111111_opy_():
    if bstack11l1l1l111_opy_() < version.parse(bstack11l1l11ll_opy_):
      logger.error(bstack1ll11l1ll1_opy_.format(bstack11l1l1l111_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11l1111_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ອ")) and callable(getattr(RemoteConnection, bstack11l1111_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧຮ"))):
          bstack1lllll1l11_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1lllll1l11_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack1l11ll1l1_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack11ll11l11l_opy_ = Config.getoption
    from _pytest import runner
    bstack1lll1l1ll1_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1llllll1l_opy_)
  try:
    from pytest_bdd import reporting
    bstack11l111l1l_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11l1111_opy_ (u"ࠧࡑ࡮ࡨࡥࡸ࡫ࠠࡪࡰࡶࡸࡦࡲ࡬ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺ࡯ࠡࡴࡸࡲࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡩࡸࡺࡳࠨຯ"))
  bstack11ll1l1lll_opy_ = CONFIG.get(bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬະ"), {}).get(bstack11l1111_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫັ"))
  bstack11l1111l11_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack11l1l1111l_opy_():
      bstack11lll1111l_opy_.invoke(Events.CONNECT, bstack11ll1l1ll_opy_())
    platform_index = int(os.environ.get(bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪາ"), bstack11l1111_opy_ (u"ࠫ࠵࠭ຳ")))
  else:
    bstack111111ll1l_opy_(bstack1ll1lll1ll_opy_)
  os.environ[bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭ິ")] = CONFIG[bstack11l1111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨີ")]
  os.environ[bstack11l1111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡄࡅࡈࡗࡘࡥࡋࡆ࡛ࠪຶ")] = CONFIG[bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫື")]
  os.environ[bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒຸࠬ")] = bstack111l11111_opy_.__str__()
  from _pytest.config import main as bstack111lllll1l_opy_
  bstack111ll111l_opy_ = []
  try:
    exit_code = bstack111lllll1l_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1111ll11l1_opy_()
    if bstack11l1111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺູࠧ") in multiprocessing.current_process().__dict__.keys():
      for bstack11llll11ll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack111ll111l_opy_.append(bstack11llll11ll_opy_)
    try:
      bstack1ll1lll1l1_opy_ = (bstack111ll111l_opy_, int(exit_code))
      bstack11lllllll_opy_.append(bstack1ll1lll1l1_opy_)
    except:
      bstack11lllllll_opy_.append((bstack111ll111l_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack111ll111l_opy_.append({bstack11l1111_opy_ (u"ࠫࡳࡧ࡭ࡦ຺ࠩ"): bstack11l1111_opy_ (u"ࠬࡖࡲࡰࡥࡨࡷࡸࠦࠧົ") + os.environ.get(bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ຼ")), bstack11l1111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ຽ"): traceback.format_exc(), bstack11l1111_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ຾"): int(os.environ.get(bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡍࡓࡊࡅ࡙ࠩ຿")))})
    bstack11lllllll_opy_.append((bstack111ll111l_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack11l1111_opy_ (u"ࠥࡶࡪࡺࡲࡪࡧࡶࠦເ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack1ll111l11_opy_ = e.__class__.__name__
    print(bstack11l1111_opy_ (u"ࠦࠪࡹ࠺ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡤࡨ࡬ࡦࡼࡥࠡࡶࡨࡷࡹࠦࠥࡴࠤແ") % (bstack1ll111l11_opy_, e))
    return 1
def bstack111ll1l11_opy_(arg):
  global bstack11l1l1lll1_opy_
  bstack111111ll1l_opy_(bstack11l1111111_opy_)
  os.environ[bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ໂ")] = str(bstack111l111111_opy_)
  retries = bstack1lllllll1_opy_.bstack1lll111ll_opy_(CONFIG)
  status_code = 0
  if bstack1lllllll1_opy_.bstack1lll1llll_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack11l11l1l11_opy_
    status_code = bstack11l11l1l11_opy_(arg)
  if status_code != 0:
    bstack11l1l1lll1_opy_ = status_code
def bstack11111ll11l_opy_():
  logger.info(bstack1llll111l1_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11l1111_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬໃ"), help=bstack11l1111_opy_ (u"ࠧࡈࡧࡱࡩࡷࡧࡴࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡥࡲࡲ࡫࡯ࡧࠨໄ"))
  parser.add_argument(bstack11l1111_opy_ (u"ࠨ࠯ࡸࠫ໅"), bstack11l1111_opy_ (u"ࠩ࠰࠱ࡺࡹࡥࡳࡰࡤࡱࡪ࠭ໆ"), help=bstack11l1111_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡶࡵࡨࡶࡳࡧ࡭ࡦࠩ໇"))
  parser.add_argument(bstack11l1111_opy_ (u"ࠫ࠲ࡱ່ࠧ"), bstack11l1111_opy_ (u"ࠬ࠳࠭࡬ࡧࡼ້ࠫ"), help=bstack11l1111_opy_ (u"࡙࠭ࡰࡷࡵࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡥࡨࡩࡥࡴࡵࠣ࡯ࡪࡿ໊ࠧ"))
  parser.add_argument(bstack11l1111_opy_ (u"ࠧ࠮ࡨ໋ࠪ"), bstack11l1111_opy_ (u"ࠨ࠯࠰ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭໌"), help=bstack11l1111_opy_ (u"ࠩ࡜ࡳࡺࡸࠠࡵࡧࡶࡸࠥ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨໍ"))
  bstack1ll1l1l1l1_opy_ = parser.parse_args()
  try:
    bstack11l1ll1ll1_opy_ = bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡪࡩࡳ࡫ࡲࡪࡥ࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧ໎")
    if bstack1ll1l1l1l1_opy_.framework and bstack1ll1l1l1l1_opy_.framework not in (bstack11l1111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ໏"), bstack11l1111_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ࠸࠭໐")):
      bstack11l1ll1ll1_opy_ = bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫࠯ࡻࡰࡰ࠳ࡹࡡ࡮ࡲ࡯ࡩࠬ໑")
    bstack1l11l11lll_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1ll1ll1_opy_)
    bstack1l11llll11_opy_ = open(bstack1l11l11lll_opy_, bstack11l1111_opy_ (u"ࠧࡳࠩ໒"))
    bstack1ll1l1lll1_opy_ = bstack1l11llll11_opy_.read()
    bstack1l11llll11_opy_.close()
    if bstack1ll1l1l1l1_opy_.username:
      bstack1ll1l1lll1_opy_ = bstack1ll1l1lll1_opy_.replace(bstack11l1111_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨ໓"), bstack1ll1l1l1l1_opy_.username)
    if bstack1ll1l1l1l1_opy_.key:
      bstack1ll1l1lll1_opy_ = bstack1ll1l1lll1_opy_.replace(bstack11l1111_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫ໔"), bstack1ll1l1l1l1_opy_.key)
    if bstack1ll1l1l1l1_opy_.framework:
      bstack1ll1l1lll1_opy_ = bstack1ll1l1lll1_opy_.replace(bstack11l1111_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ໕"), bstack1ll1l1l1l1_opy_.framework)
    file_name = bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠧ໖")
    file_path = os.path.abspath(file_name)
    bstack11lll1lll_opy_ = open(file_path, bstack11l1111_opy_ (u"ࠬࡽࠧ໗"))
    bstack11lll1lll_opy_.write(bstack1ll1l1lll1_opy_)
    bstack11lll1lll_opy_.close()
    logger.info(bstack11l11lll1_opy_)
    try:
      os.environ[bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ໘")] = bstack1ll1l1l1l1_opy_.framework if bstack1ll1l1l1l1_opy_.framework != None else bstack11l1111_opy_ (u"ࠢࠣ໙")
      config = yaml.safe_load(bstack1ll1l1lll1_opy_)
      config[bstack11l1111_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ໚")] = bstack11l1111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠯ࡶࡩࡹࡻࡰࠨ໛")
      bstack11l1l11l11_opy_(bstack111l1l11ll_opy_, config)
    except Exception as e:
      logger.debug(bstack111l1l1ll1_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack11111ll1ll_opy_.format(str(e)))
def bstack11l1l11l11_opy_(bstack111ll11l1l_opy_, config, bstack1111lll11_opy_={}):
  global bstack111l11111_opy_
  global bstack1lllllllll_opy_
  global bstack1llll11ll_opy_
  if not config:
    return
  bstack1l1111l11l_opy_ = bstack111lll1ll1_opy_ if not bstack111l11111_opy_ else (
    bstack1lll1l1lll_opy_ if bstack11l1111_opy_ (u"ࠪࡥࡵࡶࠧໜ") in config else (
        bstack11l1l111l_opy_ if config.get(bstack11l1111_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨໝ")) else bstack1l1111l1l_opy_
    )
)
  bstack1ll1l111l_opy_ = False
  bstack11l11ll1ll_opy_ = False
  if bstack111l11111_opy_ is True:
      if bstack11l1111_opy_ (u"ࠬࡧࡰࡱࠩໞ") in config:
          bstack1ll1l111l_opy_ = True
      else:
          bstack11l11ll1ll_opy_ = True
  bstack111l1lll1_opy_ = bstack11l1lll11l_opy_.bstack11111llll1_opy_(config, bstack1lllllllll_opy_)
  bstack11ll111l11_opy_ = bstack1l1ll11lll_opy_()
  data = {
    bstack11l1111_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨໟ"): config[bstack11l1111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ໠")],
    bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ໡"): config[bstack11l1111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ໢")],
    bstack11l1111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡷࡽࡵ࡫ࠧ໣"): bstack111ll11l1l_opy_,
    bstack11l1111_opy_ (u"ࠫࡩ࡫ࡴࡦࡥࡷࡩࡩࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ໤"): os.environ.get(bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ໥"), bstack1lllllllll_opy_),
    bstack11l1111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨ໦"): bstack11l11lll11_opy_,
    bstack11l1111_opy_ (u"ࠧࡰࡲࡷ࡭ࡲࡧ࡬ࡠࡪࡸࡦࡤࡻࡲ࡭ࠩ໧"): bstack11l11l111l_opy_(),
    bstack11l1111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໨"): {
      bstack11l1111_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ໩"): str(config[bstack11l1111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ໪")]) if bstack11l1111_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ໫") in config else bstack11l1111_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨ໬"),
      bstack11l1111_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࡗࡧࡵࡷ࡮ࡵ࡮ࠨ໭"): sys.version,
      bstack11l1111_opy_ (u"ࠧࡳࡧࡩࡩࡷࡸࡥࡳࠩ໮"): bstack11111ll1l_opy_(os.environ.get(bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ໯"), bstack1lllllllll_opy_)),
      bstack11l1111_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ໰"): bstack11l1111_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ໱"),
      bstack11l1111_opy_ (u"ࠫࡵࡸ࡯ࡥࡷࡦࡸࠬ໲"): bstack1l1111l11l_opy_,
      bstack11l1111_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ໳"): bstack111l1lll1_opy_,
      bstack11l1111_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨ࡟ࡶࡷ࡬ࡨࠬ໴"): os.environ[bstack11l1111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ໵")],
      bstack11l1111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ໶"): os.environ.get(bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ໷"), bstack1lllllllll_opy_),
      bstack11l1111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭໸"): bstack11l1ll1111_opy_(os.environ.get(bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭໹"), bstack1lllllllll_opy_)),
      bstack11l1111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ໺"): bstack11ll111l11_opy_.get(bstack11l1111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ໻")),
      bstack11l1111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭໼"): bstack11ll111l11_opy_.get(bstack11l1111_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ໽")),
      bstack11l1111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ໾"): config[bstack11l1111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໿")] if config[bstack11l1111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧༀ")] else bstack11l1111_opy_ (u"ࠧࡻ࡮࡬ࡰࡲࡻࡳࠨ༁"),
      bstack11l1111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ༂"): str(config[bstack11l1111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ༃")]) if bstack11l1111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ༄") in config else bstack11l1111_opy_ (u"ࠤࡸࡲࡰࡴ࡯ࡸࡰࠥ༅"),
      bstack11l1111_opy_ (u"ࠪࡳࡸ࠭༆"): sys.platform,
      bstack11l1111_opy_ (u"ࠫ࡭ࡵࡳࡵࡰࡤࡱࡪ࠭༇"): socket.gethostname(),
      bstack11l1111_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ༈"): bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ༉"))
    }
  }
  if not bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ༊")) is None:
    data[bstack11l1111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ་")][bstack11l1111_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡑࡪࡺࡡࡥࡣࡷࡥࠬ༌")] = {
      bstack11l1111_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪ།"): bstack11l1111_opy_ (u"ࠫࡺࡹࡥࡳࡡ࡮࡭ࡱࡲࡥࡥࠩ༎"),
      bstack11l1111_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࠬ༏"): bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭༐")),
      bstack11l1111_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࡎࡶ࡯ࡥࡩࡷ࠭༑"): bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡐࡲࠫ༒"))
    }
  if bstack111ll11l1l_opy_ == bstack11l11111l1_opy_:
    data[bstack11l1111_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ༓")][bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡅࡲࡲ࡫࡯ࡧࠨ༔")] = bstack1l1l111lll_opy_(config)
    data[bstack11l1111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ༕")][bstack11l1111_opy_ (u"ࠬ࡯ࡳࡑࡧࡵࡧࡾࡇࡵࡵࡱࡈࡲࡦࡨ࡬ࡦࡦࠪ༖")] = percy.bstack11l1l11lll_opy_
    data[bstack11l1111_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ༗")][bstack11l1111_opy_ (u"ࠧࡱࡧࡵࡧࡾࡈࡵࡪ࡮ࡧࡍࡩ༘࠭")] = percy.percy_build_id
  if not bstack1lllllll1_opy_.bstack1111l1ll11_opy_(CONFIG):
    data[bstack11l1111_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶ༙ࠫ")][bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠭༚")] = bstack1lllllll1_opy_.bstack1111l1ll11_opy_(CONFIG)
  bstack1111ll11_opy_ = bstack1lll1ll11_opy_.bstack1llllllll_opy_(CONFIG, logger)
  bstack1llllll11_opy_ = bstack1lllllll1_opy_.bstack1llllllll_opy_(config=CONFIG)
  if bstack1111ll11_opy_ is not None and bstack1llllll11_opy_ is not None and bstack1llllll11_opy_.bstack1111lll1_opy_():
    data[bstack11l1111_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭༛")][bstack1llllll11_opy_.bstack1ll11ll1ll_opy_()] = bstack1111ll11_opy_.bstack111111l1ll_opy_()
  update(data[bstack11l1111_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ༜")], bstack1111lll11_opy_)
  try:
    response = bstack111ll1l111_opy_(bstack11l1111_opy_ (u"ࠬࡖࡏࡔࡖࠪ༝"), bstack1llll11l11_opy_(bstack11ll1l1l1_opy_), data, {
      bstack11l1111_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ༞"): (config[bstack11l1111_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ༟")], config[bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ༠")])
    })
    if response:
      logger.debug(bstack1ll1ll1111_opy_.format(bstack111ll11l1l_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack11ll1llll_opy_.format(str(e)))
def bstack11111ll1l_opy_(framework):
  return bstack11l1111_opy_ (u"ࠤࡾࢁ࠲ࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨ༡").format(str(framework), __version__) if framework else bstack11l1111_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦ༢").format(
    __version__)
def bstack1l11111l11_opy_():
  global CONFIG
  global bstack1l1ll1ll11_opy_
  if bool(CONFIG):
    return
  try:
    bstack111llll1l_opy_()
    logger.debug(bstack1ll1llll1l_opy_.format(str(CONFIG)))
    bstack1l1ll1ll11_opy_ = bstack11ll1l11l1_opy_.configure_logger(CONFIG, bstack1l1ll1ll11_opy_)
    bstack1l1ll11l1_opy_()
  except Exception as e:
    logger.error(bstack11l1111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࡹࡵ࠲ࠠࡦࡴࡵࡳࡷࡀࠠࠣ༣") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1ll1ll111l_opy_
  atexit.register(bstack1l111111ll_opy_)
  signal.signal(signal.SIGINT, bstack1lll1l11ll_opy_)
  signal.signal(signal.SIGTERM, bstack1lll1l11ll_opy_)
def bstack1ll1ll111l_opy_(exctype, value, traceback):
  global bstack1l1ll11111_opy_
  try:
    for driver in bstack1l1ll11111_opy_:
      bstack1llll1l111_opy_(driver, bstack11l1111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ༤"), bstack11l1111_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤ༥") + str(value))
  except Exception:
    pass
  logger.info(bstack1lllll1l1l_opy_)
  bstack1l1l1lllll_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l1l1lllll_opy_(message=bstack11l1111_opy_ (u"ࠧࠨ༦"), bstack1l11l1lll1_opy_ = False):
  global CONFIG
  bstack11l111ll1l_opy_ = bstack11l1111_opy_ (u"ࠨࡩ࡯ࡳࡧࡧ࡬ࡆࡺࡦࡩࡵࡺࡩࡰࡰࠪ༧") if bstack1l11l1lll1_opy_ else bstack11l1111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ༨")
  try:
    if message:
      bstack1111lll11_opy_ = {
        bstack11l111ll1l_opy_ : str(message)
      }
      bstack11l1l11l11_opy_(bstack11l11111l1_opy_, CONFIG, bstack1111lll11_opy_)
    else:
      bstack11l1l11l11_opy_(bstack11l11111l1_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1111lll1l_opy_.format(str(e)))
def bstack11l1l1llll_opy_(bstack11l1ll1l1l_opy_, size):
  bstack1ll11111l_opy_ = []
  while len(bstack11l1ll1l1l_opy_) > size:
    bstack1l11lll1l1_opy_ = bstack11l1ll1l1l_opy_[:size]
    bstack1ll11111l_opy_.append(bstack1l11lll1l1_opy_)
    bstack11l1ll1l1l_opy_ = bstack11l1ll1l1l_opy_[size:]
  bstack1ll11111l_opy_.append(bstack11l1ll1l1l_opy_)
  return bstack1ll11111l_opy_
def bstack1l11ll111_opy_(args):
  if bstack11l1111_opy_ (u"ࠪ࠱ࡲ࠭༩") in args and bstack11l1111_opy_ (u"ࠫࡵࡪࡢࠨ༪") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack1l111l1lll_opy_, stage=STAGE.bstack11l1llll1l_opy_)
def run_on_browserstack(bstack1ll11l11l1_opy_=None, bstack11lllllll_opy_=None, bstack1111l11l11_opy_=False):
  global CONFIG
  global bstack1l111l1ll1_opy_
  global bstack111l111111_opy_
  global bstack1lllllllll_opy_
  global bstack1llll11ll_opy_
  bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"ࠬ࠭༫")
  bstack11lll1l1l1_opy_(bstack1l1ll1l111_opy_, logger)
  if bstack1ll11l11l1_opy_ and isinstance(bstack1ll11l11l1_opy_, str):
    bstack1ll11l11l1_opy_ = eval(bstack1ll11l11l1_opy_)
  if bstack1ll11l11l1_opy_:
    CONFIG = bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭༬")]
    bstack1l111l1ll1_opy_ = bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ༭")]
    bstack111l111111_opy_ = bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ༮")]
    bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ༯"), bstack111l111111_opy_)
    bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༰")
  bstack1llll11ll_opy_.set_property(bstack11l1111_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭༱"), uuid4().__str__())
  logger.info(bstack11l1111_opy_ (u"࡙ࠬࡄࡌࠢࡵࡹࡳࠦࡳࡵࡣࡵࡸࡪࡪࠠࡸ࡫ࡷ࡬ࠥ࡯ࡤ࠻ࠢࠪ༲") + bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ༳")));
  logger.debug(bstack11l1111_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥ࠿ࠪ༴") + bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦ༵ࠪ")))
  if not bstack1111l11l11_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack11lll1llll_opy_)
      return
    if sys.argv[1] == bstack11l1111_opy_ (u"ࠩ࠰࠱ࡻ࡫ࡲࡴ࡫ࡲࡲࠬ༶") or sys.argv[1] == bstack11l1111_opy_ (u"ࠪ࠱ࡻ༷࠭"):
      logger.info(bstack11l1111_opy_ (u"ࠫࡇࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡔࡾࡺࡨࡰࡰࠣࡗࡉࡑࠠࡷࡽࢀࠫ༸").format(__version__))
      return
    if sys.argv[1] == bstack11l1111_opy_ (u"ࠬࡹࡥࡵࡷࡳ༹ࠫ"):
      bstack11111ll11l_opy_()
      return
  args = sys.argv
  bstack1l11111l11_opy_()
  global bstack1l11ll1ll1_opy_
  global bstack1l1l11l1ll_opy_
  global bstack11l1111l11_opy_
  global bstack1ll111111_opy_
  global bstack1l1llllll1_opy_
  global bstack11ll1l1lll_opy_
  global bstack11ll1111l1_opy_
  global bstack111ll11l11_opy_
  global bstack1ll11lll1l_opy_
  global bstack111111ll1_opy_
  global bstack11l111111l_opy_
  bstack1l1l11l1ll_opy_ = len(CONFIG.get(bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ༺"), []))
  if not bstack11lllll1l1_opy_:
    if args[1] == bstack11l1111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༻") or args[1] == bstack11l1111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮࠴ࠩ༼"):
      bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༽")
      args = args[2:]
    elif args[1] == bstack11l1111_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ༾"):
      bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༿")
      args = args[2:]
    elif args[1] == bstack11l1111_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫཀ"):
      bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬཁ")
      args = args[2:]
    elif args[1] == bstack11l1111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨག"):
      bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩགྷ")
      args = args[2:]
    elif args[1] == bstack11l1111_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩང"):
      bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪཅ")
      args = args[2:]
    elif args[1] == bstack11l1111_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫཆ"):
      bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬཇ")
      args = args[2:]
    else:
      if not bstack11l1111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ཈") in CONFIG or str(CONFIG[bstack11l1111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪཉ")]).lower() in [bstack11l1111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨཊ"), bstack11l1111_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪཋ")]:
        bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪཌ")
        args = args[1:]
      elif str(CONFIG[bstack11l1111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧཌྷ")]).lower() == bstack11l1111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫཎ"):
        bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬཏ")
        args = args[1:]
      elif str(CONFIG[bstack11l1111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪཐ")]).lower() == bstack11l1111_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧད"):
        bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨདྷ")
        args = args[1:]
      elif str(CONFIG[bstack11l1111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ན")]).lower() == bstack11l1111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫཔ"):
        bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཕ")
        args = args[1:]
      elif str(CONFIG[bstack11l1111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩབ")]).lower() == bstack11l1111_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧབྷ"):
        bstack11lllll1l1_opy_ = bstack11l1111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨམ")
        args = args[1:]
      else:
        os.environ[bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫཙ")] = bstack11lllll1l1_opy_
        bstack1l1l1l111l_opy_(bstack1l111l11l1_opy_)
  os.environ[bstack11l1111_opy_ (u"ࠪࡊࡗࡇࡍࡆ࡙ࡒࡖࡐࡥࡕࡔࡇࡇࠫཚ")] = bstack11lllll1l1_opy_
  bstack1lllllllll_opy_ = bstack11lllll1l1_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1l111lll1_opy_ = bstack11ll111l1l_opy_[bstack11l1111_opy_ (u"ࠫࡕ࡟ࡔࡆࡕࡗ࠱ࡇࡊࡄࠨཛ")] if bstack11lllll1l1_opy_ == bstack11l1111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཛྷ") and bstack1ll111ll1_opy_() else bstack11lllll1l1_opy_
      bstack11lll1111l_opy_.invoke(Events.bstack1111111lll_opy_, bstack1111lll1ll_opy_(
        sdk_version=__version__,
        path_config=bstack1l1lll11ll_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1l111lll1_opy_,
        frameworks=[bstack1l111lll1_opy_],
        framework_versions={
          bstack1l111lll1_opy_: bstack11l1ll1111_opy_(bstack11l1111_opy_ (u"࠭ࡒࡰࡤࡲࡸࠬཝ") if bstack11lllll1l1_opy_ in [bstack11l1111_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ཞ"), bstack11l1111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧཟ"), bstack11l1111_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪའ")] else bstack11lllll1l1_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack11l1111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧཡ"), None):
        CONFIG[bstack11l1111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨར")] = cli.config.get(bstack11l1111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢལ"), None)
    except Exception as e:
      bstack11lll1111l_opy_.invoke(Events.bstack11l11ll111_opy_, e.__traceback__, 1)
    if bstack111l111111_opy_:
      CONFIG[bstack11l1111_opy_ (u"ࠨࡡࡱࡲࠥཤ")] = cli.config[bstack11l1111_opy_ (u"ࠢࡢࡲࡳࠦཥ")]
      logger.info(bstack1l1111l1ll_opy_.format(CONFIG[bstack11l1111_opy_ (u"ࠨࡣࡳࡴࠬས")]))
  else:
    bstack11lll1111l_opy_.clear()
  global bstack1lll11lll1_opy_
  global bstack1l11l11l11_opy_
  if bstack1ll11l11l1_opy_:
    try:
      bstack11ll111l1_opy_ = datetime.datetime.now()
      os.environ[bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫཧ")] = bstack11lllll1l1_opy_
      bstack11l1l11l11_opy_(bstack11111lll11_opy_, CONFIG)
      cli.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡵࡧ࡯ࡤࡺࡥࡴࡶࡢࡥࡹࡺࡥ࡮ࡲࡷࡩࡩࠨཨ"), datetime.datetime.now() - bstack11ll111l1_opy_)
    except Exception as e:
      logger.debug(bstack1llll1lll1_opy_.format(str(e)))
  global bstack1111ll1l1_opy_
  global bstack1111l111l_opy_
  global bstack1llll11ll1_opy_
  global bstack11l1l111l1_opy_
  global bstack1l11l111l_opy_
  global bstack1111lllll1_opy_
  global bstack1l1l1l1l11_opy_
  global bstack1l1l11ll1l_opy_
  global bstack11ll11ll1l_opy_
  global bstack11l1l1ll1_opy_
  global bstack111llll11l_opy_
  global bstack1ll111lll1_opy_
  global bstack111ll1lll1_opy_
  global bstack1llll1ll11_opy_
  global bstack1l1l11llll_opy_
  global bstack1lllll1l11_opy_
  global bstack11ll11l11l_opy_
  global bstack1lll1l1ll1_opy_
  global bstack11111lll1_opy_
  global bstack11l111l1l_opy_
  global bstack111l1l11l1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1111ll1l1_opy_ = webdriver.Remote.__init__
    bstack1111l111l_opy_ = WebDriver.quit
    bstack1ll111lll1_opy_ = WebDriver.close
    bstack1l1l11llll_opy_ = WebDriver.get
    bstack111l1l11l1_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1lll11lll1_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1l1ll1ll1l_opy_
    bstack1l11l11l11_opy_ = bstack1l1ll1ll1l_opy_()
  except Exception as e:
    pass
  try:
    global bstack1l11ll1ll_opy_
    from QWeb.keywords import browser
    bstack1l11ll1ll_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack111l1l1l11_opy_(CONFIG) and bstack1l1l111111_opy_():
    if bstack11l1l1l111_opy_() < version.parse(bstack11l1l11ll_opy_):
      logger.error(bstack1ll11l1ll1_opy_.format(bstack11l1l1l111_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11l1111_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬཀྵ")) and callable(getattr(RemoteConnection, bstack11l1111_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ཪ"))):
          RemoteConnection._get_proxy_url = bstack111llll11_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack111llll11_opy_
      except Exception as e:
        logger.error(bstack1l11ll1l1_opy_.format(str(e)))
  if not CONFIG.get(bstack11l1111_opy_ (u"࠭ࡤࡪࡵࡤࡦࡱ࡫ࡁࡶࡶࡲࡇࡦࡶࡴࡶࡴࡨࡐࡴ࡭ࡳࠨཫ"), False) and not bstack1ll11l11l1_opy_:
    logger.info(bstack1111l1l1l_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack11l1111_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫཬ") in CONFIG and str(CONFIG[bstack11l1111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ཭")]).lower() != bstack11l1111_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ཮"):
      bstack1l1111llll_opy_()
    elif bstack11lllll1l1_opy_ != bstack11l1111_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ཯") or (bstack11lllll1l1_opy_ == bstack11l1111_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ཰") and not bstack1ll11l11l1_opy_):
      bstack11111l11l1_opy_()
  if (bstack11lllll1l1_opy_ in [bstack11l1111_opy_ (u"ࠬࡶࡡࡣࡱࡷཱࠫ"), bstack11l1111_opy_ (u"࠭ࡲࡰࡤࡲࡸིࠬ"), bstack11l1111_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨཱི")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1l1111lll1_opy_
        bstack1111lllll1_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1l11l1l11_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack1l11l111l_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack111l11l11_opy_ + str(e))
    except Exception as e:
      bstack1l111lll1l_opy_(e, bstack1l11l1l11_opy_)
    if bstack11lllll1l1_opy_ != bstack11l1111_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ུࠩ"):
      bstack111l1ll11l_opy_()
    bstack1llll11ll1_opy_ = Output.start_test
    bstack11l1l111l1_opy_ = Output.end_test
    bstack1l1l1l1l11_opy_ = TestStatus.__init__
    bstack11ll11ll1l_opy_ = pabot._run
    bstack11l1l1ll1_opy_ = QueueItem.__init__
    bstack111llll11l_opy_ = pabot._create_command_for_execution
    bstack11111lll1_opy_ = pabot._report_results
  if bstack11lllll1l1_opy_ == bstack11l1111_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦཱུࠩ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l111lll1l_opy_(e, bstack1lllll1lll_opy_)
    bstack111ll1lll1_opy_ = Runner.run_hook
    bstack1llll1ll11_opy_ = Step.run
  if bstack11lllll1l1_opy_ == bstack11l1111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪྲྀ"):
    try:
      from _pytest.config import Config
      bstack11ll11l11l_opy_ = Config.getoption
      from _pytest import runner
      bstack1lll1l1ll1_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1llllll1l_opy_)
    try:
      from pytest_bdd import reporting
      bstack11l111l1l_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11l1111_opy_ (u"ࠫࡕࡲࡥࡢࡵࡨࠤ࡮ࡴࡳࡵࡣ࡯ࡰࠥࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠢࡷࡳࠥࡸࡵ࡯ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡦࡵࡷࡷࠬཷ"))
  try:
    framework_name = bstack11l1111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫླྀ") if bstack11lllll1l1_opy_ in [bstack11l1111_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬཹ"), bstack11l1111_opy_ (u"ࠧࡳࡱࡥࡳࡹེ࠭"), bstack11l1111_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ཻࠩ")] else bstack1111ll11ll_opy_(bstack11lllll1l1_opy_)
    bstack111l1llll1_opy_ = {
      bstack11l1111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡴࡡ࡮ࡧོࠪ"): bstack11l1111_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶ࠰ࡧࡺࡩࡵ࡮ࡤࡨࡶཽࠬ") if bstack11lllll1l1_opy_ == bstack11l1111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫཾ") and bstack1ll111ll1_opy_() else framework_name,
      bstack11l1111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩཿ"): bstack11l1ll1111_opy_(framework_name),
      bstack11l1111_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱྀࠫ"): __version__,
      bstack11l1111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨཱྀ"): bstack11lllll1l1_opy_
    }
    if bstack11lllll1l1_opy_ in bstack11l111l11_opy_ + bstack1l1l1111ll_opy_:
      if bstack1111111l_opy_.bstack1l1llllll_opy_(CONFIG):
        if bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨྂ") in CONFIG:
          os.environ[bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪྃ")] = os.getenv(bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏ྄ࠫ"), json.dumps(CONFIG[bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ྅")]))
          CONFIG[bstack11l1111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ྆")].pop(bstack11l1111_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ྇"), None)
          CONFIG[bstack11l1111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧྈ")].pop(bstack11l1111_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ྉ"), None)
        bstack111l1llll1_opy_[bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩྊ")] = {
          bstack11l1111_opy_ (u"ࠪࡲࡦࡳࡥࠨྋ"): bstack11l1111_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭ྌ"),
          bstack11l1111_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ྍ"): str(bstack11l1l1l111_opy_())
        }
    if bstack11lllll1l1_opy_ not in [bstack11l1111_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧྎ")] and not cli.is_running():
      bstack111111lll_opy_, bstack1111llll1_opy_ = bstack1l11l1l1_opy_.launch(CONFIG, bstack111l1llll1_opy_)
      if bstack1111llll1_opy_.get(bstack11l1111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧྏ")) is not None and bstack1111111l_opy_.bstack11ll111ll1_opy_(CONFIG) is None:
        value = bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨྐ")].get(bstack11l1111_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪྑ"))
        if value is not None:
            CONFIG[bstack11l1111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪྒ")] = value
        else:
          logger.debug(bstack11l1111_opy_ (u"ࠦࡓࡵࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡥࡣࡷࡥࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤྒྷ"))
  except Exception as e:
    logger.debug(bstack11lll1l111_opy_.format(bstack11l1111_opy_ (u"࡚ࠬࡥࡴࡶࡋࡹࡧ࠭ྔ"), str(e)))
  if bstack11lllll1l1_opy_ == bstack11l1111_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ྕ"):
    bstack11l1111l11_opy_ = True
    if bstack1ll11l11l1_opy_ and bstack1111l11l11_opy_:
      bstack11ll1l1lll_opy_ = CONFIG.get(bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫྖ"), {}).get(bstack11l1111_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪྗ"))
      bstack111111ll1l_opy_(bstack1ll11l111l_opy_)
    elif bstack1ll11l11l1_opy_:
      bstack11ll1l1lll_opy_ = CONFIG.get(bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭྘"), {}).get(bstack11l1111_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬྙ"))
      global bstack1l1ll11111_opy_
      try:
        if bstack1l11ll111_opy_(bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྚ")]) and multiprocessing.current_process().name == bstack11l1111_opy_ (u"ࠬ࠶ࠧྛ"):
          bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྜ")].remove(bstack11l1111_opy_ (u"ࠧ࠮࡯ࠪྜྷ"))
          bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྞ")].remove(bstack11l1111_opy_ (u"ࠩࡳࡨࡧ࠭ྟ"))
          bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྠ")] = bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྡ")][0]
          with open(bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྡྷ")], bstack11l1111_opy_ (u"࠭ࡲࠨྣ")) as f:
            file_content = f.read()
          bstack1ll1l11ll_opy_ = bstack11l1111_opy_ (u"ࠢࠣࠤࡩࡶࡴࡳࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡥ࡭ࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡾࡪࡁࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡻࡧࠫࡿࢂ࠯࠻ࠡࡨࡵࡳࡲࠦࡰࡥࡤࠣ࡭ࡲࡶ࡯ࡳࡶࠣࡔࡩࡨ࠻ࠡࡱࡪࡣࡩࡨࠠ࠾ࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡥࡧࠢࡰࡳࡩࡥࡢࡳࡧࡤ࡯࠭ࡹࡥ࡭ࡨ࠯ࠤࡦࡸࡧ࠭ࠢࡷࡩࡲࡶ࡯ࡳࡣࡵࡽࠥࡃࠠ࠱ࠫ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡶࡾࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡢࡴࡪࠤࡂࠦࡳࡵࡴࠫ࡭ࡳࡺࠨࡢࡴࡪ࠭࠰࠷࠰ࠪࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡦࡺࡦࡩࡵࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡥࡸࠦࡥ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡳࡥࡸࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡵࡧࡠࡦࡥࠬࡸ࡫࡬ࡧ࠮ࡤࡶ࡬࠲ࡴࡦ࡯ࡳࡳࡷࡧࡲࡺࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡐࡥࡤ࠱ࡨࡴࡥࡢࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠴ࡤࡰࡡࡥࡶࡪࡧ࡫ࠡ࠿ࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡓࡨࡧ࠮ࠩ࠯ࡵࡨࡸࡤࡺࡲࡢࡥࡨࠬ࠮ࡢ࡮ࠣࠤࠥྤ").format(str(bstack1ll11l11l1_opy_))
          bstack1llll11lll_opy_ = bstack1ll1l11ll_opy_ + file_content
          bstack11lll11l11_opy_ = bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྥ")] + bstack11l1111_opy_ (u"ࠩࡢࡦࡸࡺࡡࡤ࡭ࡢࡸࡪࡳࡰ࠯ࡲࡼࠫྦ")
          with open(bstack11lll11l11_opy_, bstack11l1111_opy_ (u"ࠪࡻࠬྦྷ")):
            pass
          with open(bstack11lll11l11_opy_, bstack11l1111_opy_ (u"ࠦࡼ࠱ࠢྨ")) as f:
            f.write(bstack1llll11lll_opy_)
          import subprocess
          process_data = subprocess.run([bstack11l1111_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࠧྩ"), bstack11lll11l11_opy_])
          if os.path.exists(bstack11lll11l11_opy_):
            os.unlink(bstack11lll11l11_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack1l11ll111_opy_(bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྪ")]):
            bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྫ")].remove(bstack11l1111_opy_ (u"ࠨ࠯ࡰࠫྫྷ"))
            bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྭ")].remove(bstack11l1111_opy_ (u"ࠪࡴࡩࡨࠧྮ"))
            bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྯ")] = bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྰ")][0]
          bstack111111ll1l_opy_(bstack1ll11l111l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྱ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11l1111_opy_ (u"ࠧࡠࡡࡱࡥࡲ࡫࡟ࡠࠩྲ")] = bstack11l1111_opy_ (u"ࠨࡡࡢࡱࡦ࡯࡮ࡠࡡࠪླ")
          mod_globals[bstack11l1111_opy_ (u"ࠩࡢࡣ࡫࡯࡬ࡦࡡࡢࠫྴ")] = os.path.abspath(bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྵ")])
          exec(open(bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྶ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11l1111_opy_ (u"ࠬࡉࡡࡶࡩ࡫ࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠬྷ").format(str(e)))
          for driver in bstack1l1ll11111_opy_:
            bstack11lllllll_opy_.append({
              bstack11l1111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫྸ"): bstack1ll11l11l1_opy_[bstack11l1111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྐྵ")],
              bstack11l1111_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧྺ"): str(e),
              bstack11l1111_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨྻ"): multiprocessing.current_process().name
            })
            bstack1llll1l111_opy_(driver, bstack11l1111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪྼ"), bstack11l1111_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢ྽") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l1ll11111_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack111l111111_opy_, CONFIG, logger)
      bstack11ll1llll1_opy_()
      bstack111ll111ll_opy_()
      percy.bstack1ll1l11l11_opy_()
      bstack1111ll1l_opy_ = {
        bstack11l1111_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ྾"): args[0],
        bstack11l1111_opy_ (u"࠭ࡃࡐࡐࡉࡍࡌ࠭྿"): CONFIG,
        bstack11l1111_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ࿀"): bstack1l111l1ll1_opy_,
        bstack11l1111_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ࿁"): bstack111l111111_opy_
      }
      if bstack11l1111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ࿂") in CONFIG:
        bstack1l111l1111_opy_ = bstack111ll1l11l_opy_(args, logger, CONFIG, bstack111l11111_opy_, bstack1l1l11l1ll_opy_)
        bstack111ll11l11_opy_ = bstack1l111l1111_opy_.bstack1lll11lll_opy_(run_on_browserstack, bstack1111ll1l_opy_, bstack1l11ll111_opy_(args))
      else:
        if bstack1l11ll111_opy_(args):
          bstack1111ll1l_opy_[bstack11l1111_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭࿃")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1111ll1l_opy_,))
          test.start()
          test.join()
        else:
          bstack111111ll1l_opy_(bstack1ll11l111l_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11l1111_opy_ (u"ࠫࡤࡥ࡮ࡢ࡯ࡨࡣࡤ࠭࿄")] = bstack11l1111_opy_ (u"ࠬࡥ࡟࡮ࡣ࡬ࡲࡤࡥࠧ࿅")
          mod_globals[bstack11l1111_opy_ (u"࠭࡟ࡠࡨ࡬ࡰࡪࡥ࡟ࠨ࿆")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack11lllll1l1_opy_ == bstack11l1111_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭࿇") or bstack11lllll1l1_opy_ == bstack11l1111_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ࿈"):
    percy.init(bstack111l111111_opy_, CONFIG, logger)
    percy.bstack1ll1l11l11_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l111lll1l_opy_(e, bstack1l11l1l11_opy_)
    bstack11ll1llll1_opy_()
    bstack111111ll1l_opy_(bstack11111111l_opy_)
    if bstack111l11111_opy_:
      bstack1lll1lll11_opy_(bstack11111111l_opy_, args)
      if bstack11l1111_opy_ (u"ࠩ࠰࠱ࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠧ࿉") in args:
        i = args.index(bstack11l1111_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ࿊"))
        args.pop(i)
        args.pop(i)
      if bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ࿋") not in CONFIG:
        CONFIG[bstack11l1111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ࿌")] = [{}]
        bstack1l1l11l1ll_opy_ = 1
      if bstack1l11ll1ll1_opy_ == 0:
        bstack1l11ll1ll1_opy_ = 1
      args.insert(0, str(bstack1l11ll1ll1_opy_))
      args.insert(0, str(bstack11l1111_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫ࿍")))
    if bstack1l11l1l1_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack1lll1l11l1_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack11l1lll1l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11l1111_opy_ (u"ࠢࡓࡑࡅࡓ࡙ࡥࡏࡑࡖࡌࡓࡓ࡙ࠢ࿎"),
        ).parse_args(bstack1lll1l11l1_opy_)
        bstack1ll1111l11_opy_ = args.index(bstack1lll1l11l1_opy_[0]) if len(bstack1lll1l11l1_opy_) > 0 else len(args)
        args.insert(bstack1ll1111l11_opy_, str(bstack11l1111_opy_ (u"ࠨ࠯࠰ࡰ࡮ࡹࡴࡦࡰࡨࡶࠬ࿏")))
        args.insert(bstack1ll1111l11_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡵࡳࡧࡵࡴࡠ࡮࡬ࡷࡹ࡫࡮ࡦࡴ࠱ࡴࡾ࠭࿐"))))
        if bstack1lllllll1_opy_.bstack1lll1llll_opy_(CONFIG):
          args.insert(bstack1ll1111l11_opy_, str(bstack11l1111_opy_ (u"ࠪ࠱࠲ࡲࡩࡴࡶࡨࡲࡪࡸࠧ࿑")))
          args.insert(bstack1ll1111l11_opy_ + 1, str(bstack11l1111_opy_ (u"ࠫࡗ࡫ࡴࡳࡻࡉࡥ࡮ࡲࡥࡥ࠼ࡾࢁࠬ࿒").format(bstack1lllllll1_opy_.bstack1lll111ll_opy_(CONFIG))))
        if bstack1ll11lll11_opy_(os.environ.get(bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࠪ࿓"))) and str(os.environ.get(bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࡣ࡙ࡋࡓࡕࡕࠪ࿔"), bstack11l1111_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ࿕"))) != bstack11l1111_opy_ (u"ࠨࡰࡸࡰࡱ࠭࿖"):
          for bstack1111l1l1ll_opy_ in bstack11l1lll1l_opy_:
            args.remove(bstack1111l1l1ll_opy_)
          test_files = os.environ.get(bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔ࡟ࡕࡇࡖࡘࡘ࠭࿗")).split(bstack11l1111_opy_ (u"ࠪ࠰ࠬ࿘"))
          for bstack1ll1ll1ll1_opy_ in test_files:
            args.append(bstack1ll1ll1ll1_opy_)
      except Exception as e:
        logger.error(bstack11l1111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡤࡸࡹࡧࡣࡩ࡫ࡱ࡫ࠥࡲࡩࡴࡶࡨࡲࡪࡸࠠࡧࡱࡵࠤࢀࢃ࠮ࠡࡇࡵࡶࡴࡸࠠ࠮ࠢࡾࢁࠧ࿙").format(bstack1l111l11l_opy_, e))
    pabot.main(args)
  elif bstack11lllll1l1_opy_ == bstack11l1111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭࿚"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l111lll1l_opy_(e, bstack1l11l1l11_opy_)
    for a in args:
      if bstack11l1111_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜ࠬ࿛") in a:
        bstack1l1llllll1_opy_ = int(a.split(bstack11l1111_opy_ (u"ࠧ࠻ࠩ࿜"))[1])
      if bstack11l1111_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ࿝") in a:
        bstack11ll1l1lll_opy_ = str(a.split(bstack11l1111_opy_ (u"ࠩ࠽ࠫ࿞"))[1])
      if bstack11l1111_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕࠪ࿟") in a:
        bstack11ll1111l1_opy_ = str(a.split(bstack11l1111_opy_ (u"ࠫ࠿࠭࿠"))[1])
    bstack11ll1l11ll_opy_ = None
    bstack1lll1llll1_opy_ = None
    if bstack11l1111_opy_ (u"ࠬ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠫ࿡") in args:
      i = args.index(bstack11l1111_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬ࿢"))
      args.pop(i)
      bstack11ll1l11ll_opy_ = args.pop(i)
    if bstack11l1111_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࠪ࿣") in args:
      i = args.index(bstack11l1111_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࠫ࿤"))
      args.pop(i)
      bstack1lll1llll1_opy_ = args.pop(i)
    if bstack11ll1l11ll_opy_ is not None:
      global bstack1l1l1ll11_opy_
      bstack1l1l1ll11_opy_ = bstack11ll1l11ll_opy_
    if bstack1lll1llll1_opy_ is not None and int(bstack1l1llllll1_opy_) < 0:
      bstack1l1llllll1_opy_ = int(bstack1lll1llll1_opy_)
    bstack111111ll1l_opy_(bstack11111111l_opy_)
    run_cli(args)
    if bstack11l1111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠭࿥") in multiprocessing.current_process().__dict__.keys():
      for bstack11llll11ll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack11lllllll_opy_.append(bstack11llll11ll_opy_)
  elif bstack11lllll1l1_opy_ == bstack11l1111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ࿦"):
    bstack111111l11l_opy_ = bstack1lllll111_opy_(args, logger, CONFIG, bstack111l11111_opy_)
    bstack111111l11l_opy_.bstack111l111l_opy_()
    bstack11ll1llll1_opy_()
    bstack1ll111111_opy_ = True
    bstack111111ll1_opy_ = bstack111111l11l_opy_.bstack111ll1ll_opy_()
    bstack111111l11l_opy_.bstack1111ll1l_opy_(bstack11llll1ll_opy_)
    bstack111111l11l_opy_.bstack1lll1lll1_opy_()
    bstack11ll1ll1ll_opy_(bstack11lllll1l1_opy_, CONFIG, bstack111111l11l_opy_.bstack1lllll1ll_opy_())
    bstack1ll11111l1_opy_ = bstack111111l11l_opy_.bstack1lll11lll_opy_(bstack1ll1l1l1ll_opy_, {
      bstack11l1111_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬ࿧"): bstack1l111l1ll1_opy_,
      bstack11l1111_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧ࿨"): bstack111l111111_opy_,
      bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩ࿩"): bstack111l11111_opy_
    })
    try:
      bstack111ll111l_opy_, bstack11l1ll111_opy_ = map(list, zip(*bstack1ll11111l1_opy_))
      bstack1ll11lll1l_opy_ = bstack111ll111l_opy_[0]
      for status_code in bstack11l1ll111_opy_:
        if status_code != 0:
          bstack11l111111l_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11l1111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡦࡼࡥࠡࡧࡵࡶࡴࡸࡳࠡࡣࡱࡨࠥࡹࡴࡢࡶࡸࡷࠥࡩ࡯ࡥࡧ࠱ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠ࠻ࠢࡾࢁࠧ࿪").format(str(e)))
  elif bstack11lllll1l1_opy_ == bstack11l1111_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ࿫"):
    try:
      from behave.__main__ import main as bstack11l11l1l11_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l111lll1l_opy_(e, bstack1lllll1lll_opy_)
    bstack11ll1llll1_opy_()
    bstack1ll111111_opy_ = True
    bstack111lll1l_opy_ = 1
    if bstack11l1111_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ࿬") in CONFIG:
      bstack111lll1l_opy_ = CONFIG[bstack11l1111_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ࿭")]
    if bstack11l1111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ࿮") in CONFIG:
      bstack1l1ll11l11_opy_ = int(bstack111lll1l_opy_) * int(len(CONFIG[bstack11l1111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ࿯")]))
    else:
      bstack1l1ll11l11_opy_ = int(bstack111lll1l_opy_)
    config = Configuration(args)
    bstack11llll1ll1_opy_ = config.paths
    if len(bstack11llll1ll1_opy_) == 0:
      import glob
      pattern = bstack11l1111_opy_ (u"࠭ࠪࠫ࠱࠭࠲࡫࡫ࡡࡵࡷࡵࡩࠬ࿰")
      bstack1l1111ll11_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1l1111ll11_opy_)
      config = Configuration(args)
      bstack11llll1ll1_opy_ = config.paths
    bstack11111l1l_opy_ = [os.path.normpath(item) for item in bstack11llll1ll1_opy_]
    bstack111lll111_opy_ = [os.path.normpath(item) for item in args]
    bstack111l1l1ll_opy_ = [item for item in bstack111lll111_opy_ if item not in bstack11111l1l_opy_]
    import platform as pf
    if pf.system().lower() == bstack11l1111_opy_ (u"ࠧࡸ࡫ࡱࡨࡴࡽࡳࠨ࿱"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack11111l1l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1l1ll1lll_opy_)))
                    for bstack1l1ll1lll_opy_ in bstack11111l1l_opy_]
    bstack111l1l11_opy_ = []
    for spec in bstack11111l1l_opy_:
      bstack1llll1l11_opy_ = []
      bstack1llll1l11_opy_ += bstack111l1l1ll_opy_
      bstack1llll1l11_opy_.append(spec)
      bstack111l1l11_opy_.append(bstack1llll1l11_opy_)
    execution_items = []
    for bstack1llll1l11_opy_ in bstack111l1l11_opy_:
      if bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ࿲") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack11l1111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ࿳")]):
          item = {}
          item[bstack11l1111_opy_ (u"ࠪࡥࡷ࡭ࠧ࿴")] = bstack11l1111_opy_ (u"ࠫࠥ࠭࿵").join(bstack1llll1l11_opy_)
          item[bstack11l1111_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ࿶")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack11l1111_opy_ (u"࠭ࡡࡳࡩࠪ࿷")] = bstack11l1111_opy_ (u"ࠧࠡࠩ࿸").join(bstack1llll1l11_opy_)
        item[bstack11l1111_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ࿹")] = 0
        execution_items.append(item)
    bstack111111l11_opy_ = bstack11l1l1llll_opy_(execution_items, bstack1l1ll11l11_opy_)
    for execution_item in bstack111111l11_opy_:
      bstack1lll111l1_opy_ = []
      for item in execution_item:
        bstack1lll111l1_opy_.append(bstack111ll11ll_opy_(name=str(item[bstack11l1111_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ࿺")]),
                                             target=bstack111ll1l11_opy_,
                                             args=(item[bstack11l1111_opy_ (u"ࠪࡥࡷ࡭ࠧ࿻")],)))
      for t in bstack1lll111l1_opy_:
        t.start()
      for t in bstack1lll111l1_opy_:
        t.join()
  else:
    bstack1l1l1l111l_opy_(bstack1l111l11l1_opy_)
  if not bstack1ll11l11l1_opy_:
    bstack11ll11l1l1_opy_()
    if(bstack11lllll1l1_opy_ in [bstack11l1111_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ࿼"), bstack11l1111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ࿽")]):
      bstack11l1ll1l11_opy_()
  bstack11ll1l11l1_opy_.bstack111lll11l_opy_()
def browserstack_initialize(bstack1l11l1ll1_opy_=None):
  logger.info(bstack11l1111_opy_ (u"࠭ࡒࡶࡰࡱ࡭ࡳ࡭ࠠࡔࡆࡎࠤࡼ࡯ࡴࡩࠢࡤࡶ࡬ࡹ࠺ࠡࠩ࿾") + str(bstack1l11l1ll1_opy_))
  run_on_browserstack(bstack1l11l1ll1_opy_, None, True)
@measure(event_name=EVENTS.bstack1l11l1l1ll_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack11ll11l1l1_opy_():
  global CONFIG
  global bstack1lllllllll_opy_
  global bstack11l111111l_opy_
  global bstack11l1l1lll1_opy_
  global bstack1llll11ll_opy_
  bstack11l1l1l1ll_opy_.bstack111lll1111_opy_()
  if cli.is_running():
    bstack11lll1111l_opy_.invoke(Events.bstack1lll111l1l_opy_)
  else:
    bstack1llllll11_opy_ = bstack1lllllll1_opy_.bstack1llllllll_opy_(config=CONFIG)
    bstack1llllll11_opy_.bstack1llllllll1_opy_(CONFIG)
  if bstack1lllllllll_opy_ == bstack11l1111_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ࿿"):
    if not cli.is_enabled(CONFIG):
      bstack1l11l1l1_opy_.stop()
  else:
    bstack1l11l1l1_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack11llll1l_opy_.bstack11ll1lllll_opy_()
  if bstack11l1111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬက") in CONFIG and str(CONFIG[bstack11l1111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ခ")]).lower() != bstack11l1111_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩဂ"):
    hashed_id, bstack11ll111ll_opy_ = bstack1l11l11ll_opy_()
  else:
    hashed_id, bstack11ll111ll_opy_ = get_build_link()
  bstack11l1lll11_opy_(hashed_id)
  logger.info(bstack11l1111_opy_ (u"ࠫࡘࡊࡋࠡࡴࡸࡲࠥ࡫࡮ࡥࡧࡧࠤ࡫ࡵࡲࠡ࡫ࡧ࠾ࠬဃ") + bstack1llll11ll_opy_.get_property(bstack11l1111_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧင"), bstack11l1111_opy_ (u"࠭ࠧစ")) + bstack11l1111_opy_ (u"ࠧ࠭ࠢࡷࡩࡸࡺࡨࡶࡤࠣ࡭ࡩࡀࠠࠨဆ") + os.getenv(bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ဇ"), bstack11l1111_opy_ (u"ࠩࠪဈ")))
  if hashed_id is not None and bstack11l1l1l1l1_opy_() != -1:
    sessions = bstack11l1ll1lll_opy_(hashed_id)
    bstack11llllllll_opy_(sessions, bstack11ll111ll_opy_)
  if bstack1lllllllll_opy_ == bstack11l1111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪဉ") and bstack11l111111l_opy_ != 0:
    sys.exit(bstack11l111111l_opy_)
  if bstack1lllllllll_opy_ == bstack11l1111_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫည") and bstack11l1l1lll1_opy_ != 0:
    sys.exit(bstack11l1l1lll1_opy_)
def bstack11l1lll11_opy_(new_id):
    global bstack11l11lll11_opy_
    bstack11l11lll11_opy_ = new_id
def bstack1111ll11ll_opy_(bstack11lll1l11_opy_):
  if bstack11lll1l11_opy_:
    return bstack11lll1l11_opy_.capitalize()
  else:
    return bstack11l1111_opy_ (u"ࠬ࠭ဋ")
@measure(event_name=EVENTS.bstack1l1ll1llll_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack1l111llll_opy_(bstack1lll1lll1l_opy_):
  if bstack11l1111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫဌ") in bstack1lll1lll1l_opy_ and bstack1lll1lll1l_opy_[bstack11l1111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬဍ")] != bstack11l1111_opy_ (u"ࠨࠩဎ"):
    return bstack1lll1lll1l_opy_[bstack11l1111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧဏ")]
  else:
    bstack11lll11l1l_opy_ = bstack11l1111_opy_ (u"ࠥࠦတ")
    if bstack11l1111_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫထ") in bstack1lll1lll1l_opy_ and bstack1lll1lll1l_opy_[bstack11l1111_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬဒ")] != None:
      bstack11lll11l1l_opy_ += bstack1lll1lll1l_opy_[bstack11l1111_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ဓ")] + bstack11l1111_opy_ (u"ࠢ࠭ࠢࠥန")
      if bstack1lll1lll1l_opy_[bstack11l1111_opy_ (u"ࠨࡱࡶࠫပ")] == bstack11l1111_opy_ (u"ࠤ࡬ࡳࡸࠨဖ"):
        bstack11lll11l1l_opy_ += bstack11l1111_opy_ (u"ࠥ࡭ࡔ࡙ࠠࠣဗ")
      bstack11lll11l1l_opy_ += (bstack1lll1lll1l_opy_[bstack11l1111_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨဘ")] or bstack11l1111_opy_ (u"ࠬ࠭မ"))
      return bstack11lll11l1l_opy_
    else:
      bstack11lll11l1l_opy_ += bstack1111ll11ll_opy_(bstack1lll1lll1l_opy_[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧယ")]) + bstack11l1111_opy_ (u"ࠢࠡࠤရ") + (
              bstack1lll1lll1l_opy_[bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪလ")] or bstack11l1111_opy_ (u"ࠩࠪဝ")) + bstack11l1111_opy_ (u"ࠥ࠰ࠥࠨသ")
      if bstack1lll1lll1l_opy_[bstack11l1111_opy_ (u"ࠫࡴࡹࠧဟ")] == bstack11l1111_opy_ (u"ࠧ࡝ࡩ࡯ࡦࡲࡻࡸࠨဠ"):
        bstack11lll11l1l_opy_ += bstack11l1111_opy_ (u"ࠨࡗࡪࡰࠣࠦအ")
      bstack11lll11l1l_opy_ += bstack1lll1lll1l_opy_[bstack11l1111_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫဢ")] or bstack11l1111_opy_ (u"ࠨࠩဣ")
      return bstack11lll11l1l_opy_
@measure(event_name=EVENTS.bstack1ll11l11ll_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack11l1111lll_opy_(bstack1l1l111ll1_opy_):
  if bstack1l1l111ll1_opy_ == bstack11l1111_opy_ (u"ࠤࡧࡳࡳ࡫ࠢဤ"):
    return bstack11l1111_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿࡭ࡲࡦࡧࡱ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧ࡭ࡲࡦࡧࡱࠦࡃࡉ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ဥ")
  elif bstack1l1l111ll1_opy_ == bstack11l1111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦဦ"):
    return bstack11l1111_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡳࡧࡧ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡸࡥࡥࠤࡁࡊࡦ࡯࡬ࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨဧ")
  elif bstack1l1l111ll1_opy_ == bstack11l1111_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨဨ"):
    return bstack11l1111_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡪࡶࡪ࡫࡮࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡪࡶࡪ࡫࡮ࠣࡀࡓࡥࡸࡹࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧဩ")
  elif bstack1l1l111ll1_opy_ == bstack11l1111_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢဪ"):
    return bstack11l1111_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡷ࡫ࡤ࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡵࡩࡩࠨ࠾ࡆࡴࡵࡳࡷࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫါ")
  elif bstack1l1l111ll1_opy_ == bstack11l1111_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࠦာ"):
    return bstack11l1111_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࠣࡦࡧࡤ࠷࠷࠼࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࠥࡨࡩࡦ࠹࠲࠷ࠤࡁࡘ࡮ࡳࡥࡰࡷࡷࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩိ")
  elif bstack1l1l111ll1_opy_ == bstack11l1111_opy_ (u"ࠧࡸࡵ࡯ࡰ࡬ࡲ࡬ࠨီ"):
    return bstack11l1111_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡤ࡯ࡥࡨࡱ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡤ࡯ࡥࡨࡱࠢ࠿ࡔࡸࡲࡳ࡯࡮ࡨ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧု")
  else:
    return bstack11l1111_opy_ (u"ࠧ࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡦࡱࡧࡣ࡬࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡦࡱࡧࡣ࡬ࠤࡁࠫူ") + bstack1111ll11ll_opy_(
      bstack1l1l111ll1_opy_) + bstack11l1111_opy_ (u"ࠨ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧေ")
def bstack11111l11l_opy_(session):
  return bstack11l1111_opy_ (u"ࠩ࠿ࡸࡷࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡲࡰࡹࠥࡂࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠦࡳࡦࡵࡶ࡭ࡴࡴ࠭࡯ࡣࡰࡩࠧࡄ࠼ࡢࠢ࡫ࡶࡪ࡬࠽ࠣࡽࢀࠦࠥࡺࡡࡳࡩࡨࡸࡂࠨ࡟ࡣ࡮ࡤࡲࡰࠨ࠾ࡼࡿ࠿࠳ࡦࡄ࠼࠰ࡶࡧࡂࢀࢃࡻࡾ࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀ࠴ࡺࡲ࠿ࠩဲ").format(
    session[bstack11l1111_opy_ (u"ࠪࡴࡺࡨ࡬ࡪࡥࡢࡹࡷࡲࠧဳ")], bstack1l111llll_opy_(session), bstack11l1111lll_opy_(session[bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡷࡹࡧࡴࡶࡵࠪဴ")]),
    bstack11l1111lll_opy_(session[bstack11l1111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬဵ")]),
    bstack1111ll11ll_opy_(session[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧံ")] or session[bstack11l1111_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫့ࠧ")] or bstack11l1111_opy_ (u"ࠨࠩး")) + bstack11l1111_opy_ (u"ࠤ္ࠣࠦ") + (session[bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲ်ࠬ")] or bstack11l1111_opy_ (u"ࠫࠬျ")),
    session[bstack11l1111_opy_ (u"ࠬࡵࡳࠨြ")] + bstack11l1111_opy_ (u"ࠨࠠࠣွ") + session[bstack11l1111_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫှ")], session[bstack11l1111_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪဿ")] or bstack11l1111_opy_ (u"ࠩࠪ၀"),
    session[bstack11l1111_opy_ (u"ࠪࡧࡷ࡫ࡡࡵࡧࡧࡣࡦࡺࠧ၁")] if session[bstack11l1111_opy_ (u"ࠫࡨࡸࡥࡢࡶࡨࡨࡤࡧࡴࠨ၂")] else bstack11l1111_opy_ (u"ࠬ࠭၃"))
@measure(event_name=EVENTS.bstack1111llllll_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def bstack11llllllll_opy_(sessions, bstack11ll111ll_opy_):
  try:
    bstack1l1l1lll1l_opy_ = bstack11l1111_opy_ (u"ࠨࠢ၄")
    if not os.path.exists(bstack1l111ll11l_opy_):
      os.mkdir(bstack1l111ll11l_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11l1111_opy_ (u"ࠧࡢࡵࡶࡩࡹࡹ࠯ࡳࡧࡳࡳࡷࡺ࠮ࡩࡶࡰࡰࠬ၅")), bstack11l1111_opy_ (u"ࠨࡴࠪ၆")) as f:
      bstack1l1l1lll1l_opy_ = f.read()
    bstack1l1l1lll1l_opy_ = bstack1l1l1lll1l_opy_.replace(bstack11l1111_opy_ (u"ࠩࡾࠩࡗࡋࡓࡖࡎࡗࡗࡤࡉࡏࡖࡐࡗࠩࢂ࠭၇"), str(len(sessions)))
    bstack1l1l1lll1l_opy_ = bstack1l1l1lll1l_opy_.replace(bstack11l1111_opy_ (u"ࠪࡿࠪࡈࡕࡊࡎࡇࡣ࡚ࡘࡌࠦࡿࠪ၈"), bstack11ll111ll_opy_)
    bstack1l1l1lll1l_opy_ = bstack1l1l1lll1l_opy_.replace(bstack11l1111_opy_ (u"ࠫࢀࠫࡂࡖࡋࡏࡈࡤࡔࡁࡎࡇࠨࢁࠬ၉"),
                                              sessions[0].get(bstack11l1111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣࡳࡧ࡭ࡦࠩ၊")) if sessions[0] else bstack11l1111_opy_ (u"࠭ࠧ။"))
    with open(os.path.join(bstack1l111ll11l_opy_, bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡲࡦࡲࡲࡶࡹ࠴ࡨࡵ࡯࡯ࠫ၌")), bstack11l1111_opy_ (u"ࠨࡹࠪ၍")) as stream:
      stream.write(bstack1l1l1lll1l_opy_.split(bstack11l1111_opy_ (u"ࠩࡾࠩࡘࡋࡓࡔࡋࡒࡒࡘࡥࡄࡂࡖࡄࠩࢂ࠭၎"))[0])
      for session in sessions:
        stream.write(bstack11111l11l_opy_(session))
      stream.write(bstack1l1l1lll1l_opy_.split(bstack11l1111_opy_ (u"ࠪࡿ࡙ࠪࡅࡔࡕࡌࡓࡓ࡙࡟ࡅࡃࡗࡅࠪࢃࠧ၏"))[1])
    logger.info(bstack11l1111_opy_ (u"ࠫࡌ࡫࡮ࡦࡴࡤࡸࡪࡪࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡢࡶ࡫࡯ࡨࠥࡧࡲࡵ࡫ࡩࡥࡨࡺࡳࠡࡣࡷࠤࢀࢃࠧၐ").format(bstack1l111ll11l_opy_));
  except Exception as e:
    logger.debug(bstack11l11l11l1_opy_.format(str(e)))
def bstack11l1ll1lll_opy_(hashed_id):
  global CONFIG
  try:
    bstack11ll111l1_opy_ = datetime.datetime.now()
    host = bstack11l1111_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠰ࡧࡱࡵࡵࡥ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬၑ") if bstack11l1111_opy_ (u"࠭ࡡࡱࡲࠪၒ") in CONFIG else bstack11l1111_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨၓ")
    user = CONFIG[bstack11l1111_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪၔ")]
    key = CONFIG[bstack11l1111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬၕ")]
    bstack1ll1l1ll11_opy_ = bstack11l1111_opy_ (u"ࠪࡥࡵࡶ࠭ࡢࡷࡷࡳࡲࡧࡴࡦࠩၖ") if bstack11l1111_opy_ (u"ࠫࡦࡶࡰࠨၗ") in CONFIG else (bstack11l1111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩၘ") if CONFIG.get(bstack11l1111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪၙ")) else bstack11l1111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩၚ"))
    host = bstack11llll111_opy_(cli.config, [bstack11l1111_opy_ (u"ࠣࡣࡳ࡭ࡸࠨၛ"), bstack11l1111_opy_ (u"ࠤࡤࡴࡵࡇࡵࡵࡱࡰࡥࡹ࡫ࠢၜ"), bstack11l1111_opy_ (u"ࠥࡥࡵ࡯ࠢၝ")], host) if bstack11l1111_opy_ (u"ࠫࡦࡶࡰࠨၞ") in CONFIG else bstack11llll111_opy_(cli.config, [bstack11l1111_opy_ (u"ࠧࡧࡰࡪࡵࠥၟ"), bstack11l1111_opy_ (u"ࠨࡡࡶࡶࡲࡱࡦࡺࡥࠣၠ"), bstack11l1111_opy_ (u"ࠢࡢࡲ࡬ࠦၡ")], host)
    url = bstack11l1111_opy_ (u"ࠨࡽࢀ࠳ࢀࢃ࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡷࡪࡹࡳࡪࡱࡱࡷ࠳ࡰࡳࡰࡰࠪၢ").format(host, bstack1ll1l1ll11_opy_, hashed_id)
    headers = {
      bstack11l1111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨၣ"): bstack11l1111_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ၤ"),
    }
    proxies = bstack1111l1l111_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡪࡩࡹࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࡠ࡮࡬ࡷࡹࠨၥ"), datetime.datetime.now() - bstack11ll111l1_opy_)
      return list(map(lambda session: session[bstack11l1111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࠪၦ")], response.json()))
  except Exception as e:
    logger.debug(bstack11lllll11l_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack11l1ll1ll_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def get_build_link():
  global CONFIG
  global bstack11l11lll11_opy_
  try:
    if bstack11l1111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩၧ") in CONFIG:
      bstack11ll111l1_opy_ = datetime.datetime.now()
      host = bstack11l1111_opy_ (u"ࠧࡢࡲ࡬࠱ࡨࡲ࡯ࡶࡦࠪၨ") if bstack11l1111_opy_ (u"ࠨࡣࡳࡴࠬၩ") in CONFIG else bstack11l1111_opy_ (u"ࠩࡤࡴ࡮࠭ၪ")
      user = CONFIG[bstack11l1111_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬၫ")]
      key = CONFIG[bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧၬ")]
      bstack1ll1l1ll11_opy_ = bstack11l1111_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫၭ") if bstack11l1111_opy_ (u"࠭ࡡࡱࡲࠪၮ") in CONFIG else bstack11l1111_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩၯ")
      url = bstack11l1111_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡾࢁ࠿ࢁࡽࡁࡽࢀ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠱࡮ࡸࡵ࡮ࠨၰ").format(user, key, host, bstack1ll1l1ll11_opy_)
      if cli.is_enabled(CONFIG):
        bstack11ll111ll_opy_, hashed_id = cli.bstack1l1l1l1lll_opy_()
        logger.info(bstack1l1ll1l1l1_opy_.format(bstack11ll111ll_opy_))
        return [hashed_id, bstack11ll111ll_opy_]
      else:
        headers = {
          bstack11l1111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨၱ"): bstack11l1111_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ၲ"),
        }
        if bstack11l1111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ၳ") in CONFIG:
          params = {bstack11l1111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪၴ"): CONFIG[bstack11l1111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩၵ")], bstack11l1111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪၶ"): CONFIG[bstack11l1111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪၷ")]}
        else:
          params = {bstack11l1111_opy_ (u"ࠩࡱࡥࡲ࡫ࠧၸ"): CONFIG[bstack11l1111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ၹ")]}
        proxies = bstack1111l1l111_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack1l1ll1l11l_opy_ = response.json()[0][bstack11l1111_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࡠࡤࡸ࡭ࡱࡪࠧၺ")]
          if bstack1l1ll1l11l_opy_:
            bstack11ll111ll_opy_ = bstack1l1ll1l11l_opy_[bstack11l1111_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧࡤࡻࡲ࡭ࠩၻ")].split(bstack11l1111_opy_ (u"࠭ࡰࡶࡤ࡯࡭ࡨ࠳ࡢࡶ࡫࡯ࡨࠬၼ"))[0] + bstack11l1111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡹ࠯ࠨၽ") + bstack1l1ll1l11l_opy_[
              bstack11l1111_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫၾ")]
            logger.info(bstack1l1ll1l1l1_opy_.format(bstack11ll111ll_opy_))
            bstack11l11lll11_opy_ = bstack1l1ll1l11l_opy_[bstack11l1111_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬၿ")]
            bstack11111lllll_opy_ = CONFIG[bstack11l1111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ႀ")]
            if bstack11l1111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ႁ") in CONFIG:
              bstack11111lllll_opy_ += bstack11l1111_opy_ (u"ࠬࠦࠧႂ") + CONFIG[bstack11l1111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨႃ")]
            if bstack11111lllll_opy_ != bstack1l1ll1l11l_opy_[bstack11l1111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬႄ")]:
              logger.debug(bstack11lll11ll_opy_.format(bstack1l1ll1l11l_opy_[bstack11l1111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ႅ")], bstack11111lllll_opy_))
            cli.bstack1ll1l11l1_opy_(bstack11l1111_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡨࡧࡷࡣࡧࡻࡩ࡭ࡦࡢࡰ࡮ࡴ࡫ࠣႆ"), datetime.datetime.now() - bstack11ll111l1_opy_)
            return [bstack1l1ll1l11l_opy_[bstack11l1111_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ႇ")], bstack11ll111ll_opy_]
    else:
      logger.warn(bstack11l1ll11ll_opy_)
  except Exception as e:
    logger.debug(bstack11l1l1lll_opy_.format(str(e)))
  return [None, None]
def bstack1l1llll11_opy_(url, bstack11l11l1111_opy_=False):
  global CONFIG
  global bstack1l1l1l1l1_opy_
  if not bstack1l1l1l1l1_opy_:
    hostname = bstack11ll11lll_opy_(url)
    is_private = bstack11ll1ll11_opy_(hostname)
    if (bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨႈ") in CONFIG and not bstack1ll11lll11_opy_(CONFIG[bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩႉ")])) and (is_private or bstack11l11l1111_opy_):
      bstack1l1l1l1l1_opy_ = hostname
def bstack11ll11lll_opy_(url):
  return urlparse(url).hostname
def bstack11ll1ll11_opy_(hostname):
  for bstack1l111l1ll_opy_ in bstack1lllllll1l_opy_:
    regex = re.compile(bstack1l111l1ll_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack111l11l1l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1111l11l1l_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1l1llllll1_opy_
  bstack1l1ll1111l_opy_ = not (bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪႊ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack11l1111_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ႋ"), None))
  bstack1l1l11111_opy_ = getattr(driver, bstack11l1111_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨႌ"), None) != True
  bstack1111lll1l1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵႍࠩ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack11l1111_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬႎ"), None)
  if bstack1111lll1l1_opy_:
    if not bstack111llll111_opy_():
      logger.warning(bstack11l1111_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹ࠮ࠣႏ"))
      return {}
    logger.debug(bstack11l1111_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩ႐"))
    logger.debug(perform_scan(driver, driver_command=bstack11l1111_opy_ (u"࠭ࡥࡹࡧࡦࡹࡹ࡫ࡓࡤࡴ࡬ࡴࡹ࠭႑")))
    results = bstack111ll11ll1_opy_(bstack11l1111_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡳࠣ႒"))
    if results is not None and results.get(bstack11l1111_opy_ (u"ࠣ࡫ࡶࡷࡺ࡫ࡳࠣ႓")) is not None:
        return results[bstack11l1111_opy_ (u"ࠤ࡬ࡷࡸࡻࡥࡴࠤ႔")]
    logger.error(bstack11l1111_opy_ (u"ࠥࡒࡴࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡒࡦࡵࡸࡰࡹࡹࠠࡸࡧࡵࡩࠥ࡬࡯ࡶࡰࡧ࠲ࠧ႕"))
    return []
  if not bstack1111111l_opy_.bstack11lll11lll_opy_(CONFIG, bstack1l1llllll1_opy_) or (bstack1l1l11111_opy_ and bstack1l1ll1111l_opy_):
    logger.warning(bstack11l1111_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸ࠴ࠢ႖"))
    return {}
  try:
    logger.debug(bstack11l1111_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩ႗"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1l1ll1lll1_opy_.bstack11llll11l_opy_)
    return results
  except Exception:
    logger.error(bstack11l1111_opy_ (u"ࠨࡎࡰࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡻࡪࡸࡥࠡࡨࡲࡹࡳࡪ࠮ࠣ႘"))
    return {}
@measure(event_name=EVENTS.bstack1ll1ll11ll_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1l1llllll1_opy_
  bstack1l1ll1111l_opy_ = not (bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫ႙"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack11l1111_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧႚ"), None))
  bstack1l1l11111_opy_ = getattr(driver, bstack11l1111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩႛ"), None) != True
  bstack1111lll1l1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪႜ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack11l1111_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ႝ"), None)
  if bstack1111lll1l1_opy_:
    if not bstack111llll111_opy_():
      logger.warning(bstack11l1111_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺ࠰ࠥ႞"))
      return {}
    logger.debug(bstack11l1111_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼࠫ႟"))
    logger.debug(perform_scan(driver, driver_command=bstack11l1111_opy_ (u"ࠧࡦࡺࡨࡧࡺࡺࡥࡔࡥࡵ࡭ࡵࡺࠧႠ")))
    results = bstack111ll11ll1_opy_(bstack11l1111_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡔࡷࡰࡱࡦࡸࡹࠣႡ"))
    if results is not None and results.get(bstack11l1111_opy_ (u"ࠤࡶࡹࡲࡳࡡࡳࡻࠥႢ")) is not None:
        return results[bstack11l1111_opy_ (u"ࠥࡷࡺࡳ࡭ࡢࡴࡼࠦႣ")]
    logger.error(bstack11l1111_opy_ (u"ࠦࡓࡵࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡓࡧࡶࡹࡱࡺࡳࠡࡕࡸࡱࡲࡧࡲࡺࠢࡺࡥࡸࠦࡦࡰࡷࡱࡨ࠳ࠨႤ"))
    return {}
  if not bstack1111111l_opy_.bstack11lll11lll_opy_(CONFIG, bstack1l1llllll1_opy_) or (bstack1l1l11111_opy_ and bstack1l1ll1111l_opy_):
    logger.warning(bstack11l1111_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡴࡷࡰࡱࡦࡸࡹ࠯ࠤႥ"))
    return {}
  try:
    logger.debug(bstack11l1111_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼࠫႦ"))
    logger.debug(perform_scan(driver))
    bstack1lll1111ll_opy_ = driver.execute_async_script(bstack1l1ll1lll1_opy_.bstack11ll11lll1_opy_)
    return bstack1lll1111ll_opy_
  except Exception:
    logger.error(bstack11l1111_opy_ (u"ࠢࡏࡱࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡺࡳ࡭ࡢࡴࡼࠤࡼࡧࡳࠡࡨࡲࡹࡳࡪ࠮ࠣႧ"))
    return {}
def bstack111llll111_opy_():
  global CONFIG
  global bstack1l1llllll1_opy_
  bstack1l111l1l1l_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨႨ"), None) and bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫႩ"), None)
  if not bstack1111111l_opy_.bstack11lll11lll_opy_(CONFIG, bstack1l1llllll1_opy_) or not bstack1l111l1l1l_opy_:
        logger.warning(bstack11l1111_opy_ (u"ࠥࡒࡴࡺࠠࡢࡰࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡴࡨࡷࡺࡲࡴࡴ࠰ࠥႪ"))
        return False
  return True
def bstack111ll11ll1_opy_(bstack11111l1l1_opy_):
    bstack1l11l1l111_opy_ = bstack1l11l1l1_opy_.current_test_uuid() if bstack1l11l1l1_opy_.current_test_uuid() else bstack11llll1l_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack1ll1111ll_opy_(bstack1l11l1l111_opy_, bstack11111l1l1_opy_))
        try:
            return future.result(timeout=bstack1llllll1l1_opy_)
        except TimeoutError:
            logger.error(bstack11l1111_opy_ (u"࡙ࠦ࡯࡭ࡦࡱࡸࡸࠥࡧࡦࡵࡧࡵࠤࢀࢃࡳࠡࡹ࡫࡭ࡱ࡫ࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡕࡩࡸࡻ࡬ࡵࡵࠥႫ").format(bstack1llllll1l1_opy_))
        except Exception as ex:
            logger.debug(bstack11l1111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡷ࡫ࡴࡳ࡫ࡨࡺ࡮ࡴࡧࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡾࢁ࠳ࠦࡅࡳࡴࡲࡶࠥ࠳ࠠࡼࡿࠥႬ").format(bstack11111l1l1_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack1ll1l1l111_opy_, stage=STAGE.bstack1111ll111_opy_, bstack11lll11l1l_opy_=bstack11lll111ll_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1l1llllll1_opy_
  bstack1l1ll1111l_opy_ = not (bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪႭ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack11l1111_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭Ⴎ"), None))
  bstack11ll1lll11_opy_ = not (bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨႯ"), None) and bstack1llll11l_opy_(
          threading.current_thread(), bstack11l1111_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫႰ"), None))
  bstack1l1l11111_opy_ = getattr(driver, bstack11l1111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪႱ"), None) != True
  if not bstack1111111l_opy_.bstack11lll11lll_opy_(CONFIG, bstack1l1llllll1_opy_) or (bstack1l1l11111_opy_ and bstack1l1ll1111l_opy_ and bstack11ll1lll11_opy_):
    logger.warning(bstack11l1111_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡺࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲ࠳ࠨႲ"))
    return {}
  try:
    bstack1l111l11ll_opy_ = bstack11l1111_opy_ (u"ࠬࡧࡰࡱࠩႳ") in CONFIG and CONFIG.get(bstack11l1111_opy_ (u"࠭ࡡࡱࡲࠪႴ"), bstack11l1111_opy_ (u"ࠧࠨႵ"))
    session_id = getattr(driver, bstack11l1111_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠬႶ"), None)
    if not session_id:
      logger.warning(bstack11l1111_opy_ (u"ࠤࡑࡳࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࠢࡩࡳࡺࡴࡤࠡࡨࡲࡶࠥࡪࡲࡪࡸࡨࡶࠧႷ"))
      return {bstack11l1111_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤႸ"): bstack11l1111_opy_ (u"ࠦࡓࡵࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡋࡇࠤ࡫ࡵࡵ࡯ࡦࠥႹ")}
    if bstack1l111l11ll_opy_:
      try:
        bstack11ll1lll1l_opy_ = {
              bstack11l1111_opy_ (u"ࠬࡺࡨࡋࡹࡷࡘࡴࡱࡥ࡯ࠩႺ"): os.environ.get(bstack11l1111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫႻ"), os.environ.get(bstack11l1111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫႼ"), bstack11l1111_opy_ (u"ࠨࠩႽ"))),
              bstack11l1111_opy_ (u"ࠩࡷ࡬࡙࡫ࡳࡵࡔࡸࡲ࡚ࡻࡩࡥࠩႾ"): bstack1l11l1l1_opy_.current_test_uuid() if bstack1l11l1l1_opy_.current_test_uuid() else bstack11llll1l_opy_.current_hook_uuid(),
              bstack11l1111_opy_ (u"ࠪࡥࡺࡺࡨࡉࡧࡤࡨࡪࡸࠧႿ"): os.environ.get(bstack11l1111_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩჀ")),
              bstack11l1111_opy_ (u"ࠬࡹࡣࡢࡰࡗ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬჁ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack11l1111_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫჂ"): os.environ.get(bstack11l1111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬჃ"), bstack11l1111_opy_ (u"ࠨࠩჄ")),
              bstack11l1111_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥࠩჅ"): kwargs.get(bstack11l1111_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࡢࡧࡴࡳ࡭ࡢࡰࡧࠫ჆"), None) or bstack11l1111_opy_ (u"ࠫࠬჇ")
          }
        if not hasattr(thread_local, bstack11l1111_opy_ (u"ࠬࡨࡡࡴࡧࡢࡥࡵࡶ࡟ࡢ࠳࠴ࡽࡤࡹࡣࡳ࡫ࡳࡸࠬ჈")):
            scripts = {bstack11l1111_opy_ (u"࠭ࡳࡤࡣࡱࠫ჉"): bstack1l1ll1lll1_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack1llllll111_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack1llllll111_opy_[bstack11l1111_opy_ (u"ࠧࡴࡥࡤࡲࠬ჊")] = bstack1llllll111_opy_[bstack11l1111_opy_ (u"ࠨࡵࡦࡥࡳ࠭჋")] % json.dumps(bstack11ll1lll1l_opy_)
        bstack1l1ll1lll1_opy_.bstack1l11lll1l_opy_(bstack1llllll111_opy_)
        bstack1l1ll1lll1_opy_.store()
        bstack1l1l111l1l_opy_ = driver.execute_script(bstack1l1ll1lll1_opy_.perform_scan)
      except Exception as bstack111l1lll11_opy_:
        logger.info(bstack11l1111_opy_ (u"ࠤࡄࡴࡵ࡯ࡵ࡮ࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡧࡦࡴࠠࡧࡣ࡬ࡰࡪࡪ࠺ࠡࠤ჌") + str(bstack111l1lll11_opy_))
        bstack1l1l111l1l_opy_ = {bstack11l1111_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤჍ"): str(bstack111l1lll11_opy_)}
    else:
      bstack1l1l111l1l_opy_ = driver.execute_async_script(bstack1l1ll1lll1_opy_.perform_scan, {bstack11l1111_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࠫ჎"): kwargs.get(bstack11l1111_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤࡩ࡯࡮࡯ࡤࡲࡩ࠭჏"), None) or bstack11l1111_opy_ (u"࠭ࠧა")})
    return bstack1l1l111l1l_opy_
  except Exception as err:
    logger.error(bstack11l1111_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡶࡺࡴࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡥࡤࡲ࠳ࠦࡻࡾࠤბ").format(str(err)))
    return {}