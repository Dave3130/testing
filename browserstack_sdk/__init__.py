# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
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
from browserstack_sdk.bstack1l1l1ll1ll_opy_ import bstack11l11l111l_opy_
from browserstack_sdk.bstack1ll1lll11_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE, bstack1ll111ll1_opy_
from bstack_utils.messages import bstack1l1lll1ll1_opy_, bstack11l11l1lll_opy_, bstack11111l1lll_opy_, bstack1111l1ll11_opy_, bstack1ll11llll1_opy_, bstack111l1111ll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1l11111111_opy_ import get_logger
from bstack_utils.helper import bstack1ll11ll1l_opy_
from browserstack_sdk.bstack1lll1ll11_opy_ import bstack11llll1l1l_opy_
logger = get_logger(__name__)
def bstack11l11lll1_opy_():
  global CONFIG
  headers = {
        bstack11ll1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩਯ"): bstack11ll1l_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧਰ"),
      }
  proxies = bstack1ll11ll1l_opy_(CONFIG, bstack1ll111ll1_opy_)
  try:
    response = requests.get(bstack1ll111ll1_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l1l1ll1l_opy_ = response.json()[bstack11ll1l_opy_ (u"ࠬ࡮ࡵࡣࡵࠪ਱")]
      logger.debug(bstack1l1lll1ll1_opy_.format(response.json()))
      return bstack1l1l1ll1l_opy_
    else:
      logger.debug(bstack11l11l1lll_opy_.format(bstack11ll1l_opy_ (u"ࠨࡒࡦࡵࡳࡳࡳࡹࡥࠡࡌࡖࡓࡓࠦࡰࡢࡴࡶࡩࠥ࡫ࡲࡳࡱࡵࠤࠧਲ")))
  except Exception as e:
    logger.debug(bstack11l11l1lll_opy_.format(e))
def bstack1llllll1ll_opy_(hub_url):
  global CONFIG
  url = bstack11ll1l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤਲ਼")+  hub_url + bstack11ll1l_opy_ (u"ࠣ࠱ࡦ࡬ࡪࡩ࡫ࠣ਴")
  headers = {
        bstack11ll1l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨਵ"): bstack11ll1l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ਸ਼"),
      }
  proxies = bstack1ll11ll1l_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack11111l1lll_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1111l1ll11_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack1l1l1lll11_opy_, stage=STAGE.bstack11ll11lll_opy_)
def bstack1l1lllll1l_opy_():
  try:
    global bstack11llll11l_opy_
    global CONFIG
    if bstack11ll1l_opy_ (u"ࠫ࡭ࡻࡢࡓࡧࡪ࡭ࡴࡴࠧ਷") in CONFIG and CONFIG[bstack11ll1l_opy_ (u"ࠬ࡮ࡵࡣࡔࡨ࡫࡮ࡵ࡮ࠨਸ")]:
      from bstack_utils.constants import bstack11l11l11l1_opy_
      bstack11llll1ll_opy_ = CONFIG[bstack11ll1l_opy_ (u"࠭ࡨࡶࡤࡕࡩ࡬࡯࡯࡯ࠩਹ")]
      if bstack11llll1ll_opy_ in bstack11l11l11l1_opy_:
        bstack11llll11l_opy_ = bstack11l11l11l1_opy_[bstack11llll1ll_opy_]
        logger.debug(bstack1ll11llll1_opy_.format(bstack11llll11l_opy_))
        return
      else:
        logger.debug(bstack11ll1l_opy_ (u"ࠢࡉࡷࡥࠤࡰ࡫ࡹࠡࠩࡾࢁࠬࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࡎࡕࡃࡡࡘࡖࡑࡥࡍࡂࡒ࠯ࠤ࡫ࡧ࡬࡭࡫ࡱ࡫ࠥࡨࡡࡤ࡭ࠣࡸࡴࠦ࡯ࡱࡶ࡬ࡱࡦࡲࠠࡩࡷࡥࠤࡩ࡫ࡴࡦࡥࡷ࡭ࡴࡴࠢ਺").format(bstack11llll1ll_opy_))
    bstack1l1l1ll1l_opy_ = bstack11l11lll1_opy_()
    bstack1l111llll1_opy_ = []
    results = []
    for bstack1ll111111l_opy_ in bstack1l1l1ll1l_opy_:
      bstack1l111llll1_opy_.append(bstack11llll1l1l_opy_(target=bstack1llllll1ll_opy_,args=(bstack1ll111111l_opy_,)))
    for t in bstack1l111llll1_opy_:
      t.start()
    for t in bstack1l111llll1_opy_:
      results.append(t.join())
    bstack11llllll11_opy_ = {}
    for item in results:
      hub_url = item[bstack11ll1l_opy_ (u"ࠨࡪࡸࡦࡤࡻࡲ࡭ࠩ਻")]
      latency = item[bstack11ll1l_opy_ (u"ࠩ࡯ࡥࡹ࡫࡮ࡤࡻ਼ࠪ")]
      bstack11llllll11_opy_[hub_url] = latency
    bstack11111l1ll1_opy_ = min(bstack11llllll11_opy_, key= lambda x: bstack11llllll11_opy_[x])
    bstack11llll11l_opy_ = bstack11111l1ll1_opy_
    logger.debug(bstack1ll11llll1_opy_.format(bstack11111l1ll1_opy_))
  except Exception as e:
    logger.debug(bstack111l1111ll_opy_.format(e))
from browserstack_sdk.bstack1llll1lll_opy_ import *
from browserstack_sdk.bstack1lll1ll11_opy_ import *
from browserstack_sdk.bstack11l11111_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack1l11111111_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack1lll1lll11_opy_, stage=STAGE.bstack11ll11lll_opy_)
def bstack111ll1111l_opy_():
    global bstack11llll11l_opy_
    try:
        bstack1llllll1l1_opy_ = bstack111ll11111_opy_()
        bstack111lllll11_opy_(bstack1llllll1l1_opy_)
        hub_url = bstack1llllll1l1_opy_.get(bstack11ll1l_opy_ (u"ࠥࡹࡷࡲࠢ਽"), bstack11ll1l_opy_ (u"ࠦࠧਾ"))
        if hub_url.endswith(bstack11ll1l_opy_ (u"ࠬ࠵ࡷࡥ࠱࡫ࡹࡧ࠭ਿ")):
            hub_url = hub_url.rsplit(bstack11ll1l_opy_ (u"࠭࠯ࡸࡦ࠲࡬ࡺࡨࠧੀ"), 1)[0]
        if hub_url.startswith(bstack11ll1l_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯ࠨੁ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack11ll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࠪੂ")):
            hub_url = hub_url[8:]
        bstack11llll11l_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack111ll11111_opy_():
    global CONFIG
    bstack1l1111l1l1_opy_ = CONFIG.get(bstack11ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭੃"), {}).get(bstack11ll1l_opy_ (u"ࠪ࡫ࡷ࡯ࡤࡏࡣࡰࡩࠬ੄"), bstack11ll1l_opy_ (u"ࠫࡓࡕ࡟ࡈࡔࡌࡈࡤࡔࡁࡎࡇࡢࡔࡆ࡙ࡓࡆࡆࠪ੅"))
    if not isinstance(bstack1l1111l1l1_opy_, str):
        raise ValueError(bstack11ll1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡌࡸࡩࡥࠢࡱࡥࡲ࡫ࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡣࠣࡺࡦࡲࡩࡥࠢࡶࡸࡷ࡯࡮ࡨࠤ੆"))
    try:
        bstack1llllll1l1_opy_ = bstack1l1ll1111_opy_(bstack1l1111l1l1_opy_)
        return bstack1llllll1l1_opy_
    except Exception as e:
        logger.error(bstack11ll1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡩࡵ࡭ࡩࠦࡤࡦࡶࡤ࡭ࡱࡹࠠ࠻ࠢࡾࢁࠧੇ").format(str(e)))
        return {}
def bstack1l1ll1111_opy_(bstack1l1111l1l1_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack11ll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩੈ")] or not CONFIG[bstack11ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ੉")]:
            raise ValueError(bstack11ll1l_opy_ (u"ࠤࡐ࡭ࡸࡹࡩ࡯ࡩࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠤࡴࡸࠠࡢࡥࡦࡩࡸࡹࠠ࡬ࡧࡼࠦ੊"))
        url = bstack1l1ll1l11l_opy_ + bstack1l1111l1l1_opy_
        auth = (CONFIG[bstack11ll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬੋ")], CONFIG[bstack11ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧੌ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack11l11ll1l_opy_ = json.loads(response.text)
            return bstack11l11ll1l_opy_
    except ValueError as ve:
        logger.error(bstack11ll1l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡩࡵ࡭ࡩࠦࡤࡦࡶࡤ࡭ࡱࡹࠠ࠻ࠢࡾࢁ੍ࠧ").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack11ll1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳࠡ࠼ࠣࡿࢂࠨ੎").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack111lllll11_opy_(bstack11l1l111l_opy_):
    global CONFIG
    if bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ੏") not in CONFIG or str(CONFIG[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ੐")]).lower() == bstack11ll1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨੑ"):
        CONFIG[bstack11ll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩ੒")] = False
    elif bstack11ll1l_opy_ (u"ࠫ࡮ࡹࡔࡳ࡫ࡤࡰࡌࡸࡩࡥࠩ੓") in bstack11l1l111l_opy_:
        bstack1111ll11l1_opy_ = CONFIG.get(bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ੔"), {})
        logger.debug(bstack11ll1l_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡋࡸࡪࡵࡷ࡭ࡳ࡭ࠠ࡭ࡱࡦࡥࡱࠦ࡯ࡱࡶ࡬ࡳࡳࡹ࠺ࠡࠧࡶࠦ੕"), bstack1111ll11l1_opy_)
        bstack11l1l1llll_opy_ = bstack11l1l111l_opy_.get(bstack11ll1l_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡒࡦࡲࡨࡥࡹ࡫ࡲࡴࠤ੖"), [])
        bstack11111llll_opy_ = bstack11ll1l_opy_ (u"ࠣ࠮ࠥ੗").join(bstack11l1l1llll_opy_)
        logger.debug(bstack11ll1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡅࡸࡷࡹࡵ࡭ࠡࡴࡨࡴࡪࡧࡴࡦࡴࠣࡷࡹࡸࡩ࡯ࡩ࠽ࠤࠪࡹࠢ੘"), bstack11111llll_opy_)
        bstack111l1ll1l_opy_ = {
            bstack11ll1l_opy_ (u"ࠥࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧਖ਼"): bstack11ll1l_opy_ (u"ࠦࡦࡺࡳ࠮ࡴࡨࡴࡪࡧࡴࡦࡴࠥਗ਼"),
            bstack11ll1l_opy_ (u"ࠧ࡬࡯ࡳࡥࡨࡐࡴࡩࡡ࡭ࠤਜ਼"): bstack11ll1l_opy_ (u"ࠨࡴࡳࡷࡨࠦੜ"),
            bstack11ll1l_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳ࠭ࡳࡧࡳࡩࡦࡺࡥࡳࠤ੝"): bstack11111llll_opy_
        }
        bstack1111ll11l1_opy_.update(bstack111l1ll1l_opy_)
        logger.debug(bstack11ll1l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡖࡲࡧࡥࡹ࡫ࡤࠡ࡮ࡲࡧࡦࡲࠠࡰࡲࡷ࡭ࡴࡴࡳ࠻ࠢࠨࡷࠧਫ਼"), bstack1111ll11l1_opy_)
        CONFIG[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭੟")] = bstack1111ll11l1_opy_
        logger.debug(bstack11ll1l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡉ࡭ࡳࡧ࡬ࠡࡅࡒࡒࡋࡏࡇ࠻ࠢࠨࡷࠧ੠"), CONFIG)
def bstack1ll1l1llll_opy_():
    bstack1llllll1l1_opy_ = bstack111ll11111_opy_()
    if not bstack1llllll1l1_opy_[bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࡖࡴ࡯ࠫ੡")]:
      raise ValueError(bstack11ll1l_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡗࡵࡰࠥ࡯ࡳࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡩࡶࡴࡳࠠࡨࡴ࡬ࡨࠥࡪࡥࡵࡣ࡬ࡰࡸ࠴ࠢ੢"))
    return bstack1llllll1l1_opy_[bstack11ll1l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡘࡶࡱ࠭੣")] + bstack11ll1l_opy_ (u"ࠧࡀࡥࡤࡴࡸࡃࠧ੤")
@measure(event_name=EVENTS.bstack1ll1111l1_opy_, stage=STAGE.bstack11ll11lll_opy_)
def bstack1l11ll11ll_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack11ll1l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ੥")], CONFIG[bstack11ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ੦")])
        url = bstack1lll11l111_opy_
        logger.debug(bstack11ll1l_opy_ (u"ࠥࡅࡹࡺࡥ࡮ࡲࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡥࡹ࡮ࡲࡤࡴࠢࡩࡶࡴࡳࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡔࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠣࡅࡕࡏࠢ੧"))
        try:
            response = requests.get(url, auth=auth, headers={bstack11ll1l_opy_ (u"ࠦࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠥ੨"): bstack11ll1l_opy_ (u"ࠧࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠣ੩")})
            if response.status_code == 200:
                bstack1ll1l111ll_opy_ = json.loads(response.text)
                bstack11l11ll1ll_opy_ = bstack1ll1l111ll_opy_.get(bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡸ࠭੪"), [])
                if bstack11l11ll1ll_opy_:
                    bstack11llllllll_opy_ = bstack11l11ll1ll_opy_[0]
                    build_hashed_id = bstack11llllllll_opy_.get(bstack11ll1l_opy_ (u"ࠧࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ੫"))
                    bstack1ll1l1l11_opy_ = bstack111lll1l1l_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1ll1l1l11_opy_])
                    logger.info(bstack111l11l111_opy_.format(bstack1ll1l1l11_opy_))
                    bstack1111ll11l_opy_ = CONFIG[bstack11ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ੬")]
                    if bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ੭") in CONFIG:
                      bstack1111ll11l_opy_ += bstack11ll1l_opy_ (u"ࠪࠤࠬ੮") + CONFIG[bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੯")]
                    if bstack1111ll11l_opy_ != bstack11llllllll_opy_.get(bstack11ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪੰ")):
                      logger.debug(bstack1111lll1l_opy_.format(bstack11llllllll_opy_.get(bstack11ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫੱ")), bstack1111ll11l_opy_))
                    return result
                else:
                    logger.debug(bstack11ll1l_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡎࡰࠢࡥࡹ࡮ࡲࡤࡴࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࡹ࡮ࡥࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠱ࠦੲ"))
            else:
                logger.debug(bstack11ll1l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡥࡹ࡮ࡲࡤࡴ࠰ࠥੳ"))
        except Exception as e:
            logger.error(bstack11ll1l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࡶࠤ࠿ࠦࡻࡾࠤੴ").format(str(e)))
    else:
        logger.debug(bstack11ll1l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡆࡓࡓࡌࡉࡈࠢ࡬ࡷࠥࡴ࡯ࡵࠢࡶࡩࡹ࠴ࠠࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡥࡹ࡮ࡲࡤࡴ࠰ࠥੵ"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1l11l11111_opy_ import bstack1l11l11111_opy_, Events, bstack111l11111l_opy_, bstack1l11ll111l_opy_
from bstack_utils.measure import bstack1ll1l1lll_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack11ll11111_opy_ import bstack1l11l111l1_opy_
from bstack_utils.messages import *
from bstack_utils import bstack1l11111111_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack11l1l111ll_opy_, bstack1l1llllll_opy_, bstack1lll1l11l1_opy_, bstack1lllll11_opy_, \
  bstack11ll1l1l1_opy_, \
  Notset, bstack1ll1l111l_opy_, \
  bstack1111l1ll1_opy_, bstack1l1l1ll11_opy_, bstack11ll111l1l_opy_, bstack1l1ll1l1ll_opy_, bstack1111ll1ll_opy_, bstack11l11l1l11_opy_, \
  bstack1l11ll1l1_opy_, \
  bstack11llllll1l_opy_, bstack1111lll11_opy_, bstack11l1ll1lll_opy_, bstack1ll11111ll_opy_, \
  bstack1l1lll1111_opy_, bstack1l11111ll1_opy_, bstack1ll11lll11_opy_, bstack111ll11ll1_opy_
from bstack_utils.bstack111111ll11_opy_ import bstack1l1lll1l11_opy_
from bstack_utils.bstack1l111lll11_opy_ import bstack11111l1111_opy_, bstack1l1l1l1l1l_opy_
from bstack_utils.bstack1111l1l1ll_opy_ import bstack11l1llll11_opy_
from bstack_utils.bstack11ll111ll_opy_ import bstack1l11ll11l1_opy_, bstack1l1111l11_opy_
from bstack_utils.bstack1l1l111ll_opy_ import bstack1l1l111ll_opy_
from bstack_utils.bstack1lllll1ll1_opy_ import bstack1lllll1l11_opy_
from bstack_utils.proxy import bstack11l11lllll_opy_, bstack1ll11ll1l_opy_, bstack111lll1111_opy_, bstack1111ll111l_opy_
from bstack_utils.bstack111ll1l1ll_opy_ import bstack11l111l1ll_opy_
import bstack_utils.bstack11ll1ll1ll_opy_ as bstack1llll11l1l_opy_
import bstack_utils.bstack1lll111ll1_opy_ as bstack1l1l11ll11_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack1lllll1111_opy_ import bstack1111lll11l_opy_
from bstack_utils.bstack111l1111_opy_ import bstack1llllll11_opy_
from bstack_utils.bstack1111lll111_opy_ import bstack11l11111ll_opy_
if os.getenv(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡑࡏ࡟ࡉࡑࡒࡏࡘ࠭੶")):
  cli.bstack1111l1111_opy_()
else:
  os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡊࡒࡓࡐ࡙ࠧ੷")] = bstack11ll1l_opy_ (u"࠭ࡴࡳࡷࡨࠫ੸")
bstack1l1111lll_opy_ = bstack11ll1l_opy_ (u"ࠧࠡࠢ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࠠࠡ࡫ࡩࠬࡵࡧࡧࡦࠢࡀࡁࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠠࡼ࡞ࡱࠤࠥࠦࡴࡳࡻࡾࡠࡳࠦࡣࡰࡰࡶࡸࠥ࡬ࡳࠡ࠿ࠣࡶࡪࡷࡵࡪࡴࡨࠬࡡ࠭ࡦࡴ࡞ࠪ࠭ࡀࡢ࡮ࠡࠢࠣࠤࠥ࡬ࡳ࠯ࡣࡳࡴࡪࡴࡤࡇ࡫࡯ࡩࡘࡿ࡮ࡤࠪࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠬࠡࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡳࡣ࡮ࡴࡤࡦࡺࠬࠤ࠰ࠦࠢ࠻ࠤࠣ࠯ࠥࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡊࡔࡑࡑ࠲ࡵࡧࡲࡴࡧࠫࠬࡦࡽࡡࡪࡶࠣࡲࡪࡽࡐࡢࡩࡨ࠶࠳࡫ࡶࡢ࡮ࡸࡥࡹ࡫ࠨࠣࠪࠬࠤࡂࡄࠠࡼࡿࠥ࠰ࠥࡢࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡨࡧࡷࡗࡪࡹࡳࡪࡱࡱࡈࡪࡺࡡࡪ࡮ࡶࠦࢂࡢࠧࠪࠫࠬ࡟ࠧ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠣ࡟ࠬࠤ࠰ࠦࠢ࠭࡞࡟ࡲࠧ࠯࡜࡯ࠢࠣࠤࠥࢃࡣࡢࡶࡦ࡬࠭࡫ࡸࠪࡽ࡟ࡲࠥࠦࠠࠡࡿ࡟ࡲࠥࠦࡽ࡝ࡰࠣࠤ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠧ੹")
bstack11l1llll1l_opy_ = bstack11ll1l_opy_ (u"ࠨ࡞ࡱ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡰࡢࡶ࡫ࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳࡞࡞ࡱࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡦࡥࡵࡹࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠴ࡡࡡࡴࡣࡰࡰࡶࡸࠥࡶ࡟ࡪࡰࡧࡩࡽࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠴ࡠࡠࡳࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡹ࡬ࡪࡥࡨࠬ࠵࠲ࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࠬࡠࡳࡩ࡯࡯ࡵࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬ࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ࠭ࡀࡢ࡮ࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯࠳ࡩࡨࡳࡱࡰ࡭ࡺࡳ࠮࡭ࡣࡸࡲࡨ࡮ࠠ࠾ࠢࡤࡷࡾࡴࡣࠡࠪ࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴࠫࠣࡁࡃࠦࡻ࡝ࡰ࡯ࡩࡹࠦࡣࡢࡲࡶ࠿ࡡࡴࡴࡳࡻࠣࡿࡡࡴࡣࡢࡲࡶࠤࡂࠦࡊࡔࡑࡑ࠲ࡵࡧࡲࡴࡧࠫࡦࡸࡺࡡࡤ࡭ࡢࡧࡦࡶࡳࠪ࡞ࡱࠤࠥࢃࠠࡤࡣࡷࡧ࡭࠮ࡥࡹࠫࠣࡿࡡࡴࠠࠡࠢࠣࢁࡡࡴࠠࠡࡴࡨࡸࡺࡸ࡮ࠡࡣࡺࡥ࡮ࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯࠳ࡩࡨࡳࡱࡰ࡭ࡺࡳ࠮ࡤࡱࡱࡲࡪࡩࡴࠩࡽ࡟ࡲࠥࠦࠠࠡࡹࡶࡉࡳࡪࡰࡰ࡫ࡱࡸ࠿ࠦࡠࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ࠦࡾࡩࡳࡩ࡯ࡥࡧࡘࡖࡎࡉ࡯࡮ࡲࡲࡲࡪࡴࡴࠩࡌࡖࡓࡓ࠴ࡳࡵࡴ࡬ࡲ࡬࡯ࡦࡺࠪࡦࡥࡵࡹࠩࠪࡿࡣ࠰ࡡࡴࠠࠡࠢࠣ࠲࠳࠴࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸࡢ࡮ࠡࠢࢀ࠭ࡡࡴࡽ࡝ࡰ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࡡࡴࠧ੺")
from ._version import __version__
bstack11lll1ll1l_opy_ = None
CONFIG = {}
bstack1ll1l1ll11_opy_ = {}
bstack11ll1l11ll_opy_ = {}
bstack1ll11l1l1_opy_ = None
bstack111l1l11l1_opy_ = None
bstack1111ll1l1l_opy_ = None
bstack1l111l1111_opy_ = -1
bstack1lll11l1l1_opy_ = 0
bstack1l1l111l11_opy_ = bstack1l1l11l11_opy_
bstack1l11lll1l_opy_ = 1
bstack1lll111l11_opy_ = False
bstack1111l11l11_opy_ = False
bstack1l111lll1l_opy_ = bstack11ll1l_opy_ (u"ࠩࠪ੻")
bstack1l11l1ll11_opy_ = bstack11ll1l_opy_ (u"ࠪࠫ੼")
bstack11ll11l111_opy_ = False
bstack11lllll111_opy_ = True
bstack11111l11l_opy_ = bstack11ll1l_opy_ (u"ࠫࠬ੽")
bstack1l1lll1ll_opy_ = []
bstack11llll1111_opy_ = threading.Lock()
bstack1llll11lll_opy_ = threading.Lock()
bstack11llll11l_opy_ = bstack11ll1l_opy_ (u"ࠬ࠭੾")
bstack1l1l1ll111_opy_ = False
bstack11l11lll11_opy_ = None
bstack1l111lllll_opy_ = None
bstack11ll1l1ll_opy_ = None
bstack1l1ll11l1l_opy_ = -1
bstack1l1l11ll1_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"࠭ࡾࠨ੿")), bstack11ll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ઀"), bstack11ll1l_opy_ (u"ࠨ࠰ࡵࡳࡧࡵࡴ࠮ࡴࡨࡴࡴࡸࡴ࠮ࡪࡨࡰࡵ࡫ࡲ࠯࡬ࡶࡳࡳ࠭ઁ"))
bstack111lll1l11_opy_ = 0
bstack1111ll111_opy_ = 0
bstack11lll111l_opy_ = []
bstack11l11l1l1_opy_ = []
bstack1111lllll_opy_ = []
bstack11lll1111l_opy_ = []
bstack1ll11l111_opy_ = bstack11ll1l_opy_ (u"ࠩࠪં")
bstack1l1ll11lll_opy_ = bstack11ll1l_opy_ (u"ࠪࠫઃ")
bstack1lll1l1ll1_opy_ = False
bstack1l1ll1l11_opy_ = False
bstack1lll11l1ll_opy_ = {}
bstack111l111ll1_opy_ = None
bstack1l111l1l1l_opy_ = None
bstack11ll11l11_opy_ = None
bstack1ll111ll1l_opy_ = None
bstack11ll1l11l1_opy_ = None
bstack11l1l11lll_opy_ = None
bstack11l1l1111_opy_ = None
bstack111l1ll111_opy_ = None
bstack11ll1l1lll_opy_ = None
bstack1ll1l11111_opy_ = None
bstack111l11111_opy_ = None
bstack111ll1ll1l_opy_ = None
bstack111ll1ll11_opy_ = None
bstack11ll1lll1_opy_ = None
bstack1l11l1l11l_opy_ = None
bstack1l11ll1ll1_opy_ = None
bstack1ll1l11l1l_opy_ = None
bstack1l1l1lll1_opy_ = None
bstack1l111ll1l1_opy_ = None
bstack111l1l1l1_opy_ = None
bstack11l1ll1ll_opy_ = None
bstack1llll111ll_opy_ = None
bstack111ll11lll_opy_ = None
thread_local = threading.local()
bstack111l1l1l11_opy_ = False
bstack11l111l1l1_opy_ = bstack11ll1l_opy_ (u"ࠦࠧ઄")
logger = bstack1l11111111_opy_.get_logger(__name__, bstack1l1l111l11_opy_)
bstack111ll1l1_opy_ = Config.bstack111111ll_opy_()
percy = bstack11lll11l11_opy_()
bstack1l11l1l11_opy_ = bstack1l11l111l1_opy_()
bstack1l1ll1l111_opy_ = bstack11l11111_opy_()
def bstack1111l1l11_opy_():
  global CONFIG
  global bstack1lll1l1ll1_opy_
  global bstack111ll1l1_opy_
  testContextOptions = bstack111lllll1_opy_(CONFIG)
  if bstack11ll1l1l1_opy_(CONFIG):
    if (bstack11ll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧઅ") in testContextOptions and str(testContextOptions[bstack11ll1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨઆ")]).lower() == bstack11ll1l_opy_ (u"ࠧࡵࡴࡸࡩࠬઇ")):
      bstack1lll1l1ll1_opy_ = True
    bstack111ll1l1_opy_.bstack11l11l1111_opy_(testContextOptions.get(bstack11ll1l_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬઈ"), False))
  else:
    bstack1lll1l1ll1_opy_ = True
    bstack111ll1l1_opy_.bstack11l11l1111_opy_(True)
def bstack11l1ll1ll1_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack111llllll_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack111l1llll1_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11ll1l_opy_ (u"ࠤ࠰࠱ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡦࡳࡳ࡬ࡩࡨࡨ࡬ࡰࡪࠨઉ") == args[i].lower() or bstack11ll1l_opy_ (u"ࠥ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡮ࡧ࡫ࡪࠦઊ") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack11111l11l_opy_
      bstack11111l11l_opy_ += bstack11ll1l_opy_ (u"ࠫ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡈࡵ࡮ࡧ࡫ࡪࡊ࡮ࡲࡥࠡࠩઋ") + shlex.quote(path)
      return path
  return None
bstack1l111ll11l_opy_ = re.compile(bstack11ll1l_opy_ (u"ࡷࠨ࠮ࠫࡁ࡟ࠨࢀ࠮࠮ࠫࡁࠬࢁ࠳࠰࠿ࠣઌ"))
def bstack11l1ll1l1_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1l111ll11l_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11ll1l_opy_ (u"ࠨࠤࡼࠤઍ") + group + bstack11ll1l_opy_ (u"ࠢࡾࠤ઎"), os.environ.get(group))
  return value
def bstack111l111l1_opy_():
  global bstack111ll11lll_opy_
  if bstack111ll11lll_opy_ is None:
        bstack111ll11lll_opy_ = bstack111l1llll1_opy_()
  bstack111111ll1l_opy_ = bstack111ll11lll_opy_
  if bstack111111ll1l_opy_ and os.path.exists(os.path.abspath(bstack111111ll1l_opy_)):
    fileName = bstack111111ll1l_opy_
  if bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍ࡟ࡇࡋࡏࡉࠬએ") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࡠࡈࡌࡐࡊ࠭ઐ")])) and not bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡏࡣࡰࡩࠬઑ") in locals():
    fileName = os.environ[bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ઒")]
  if bstack11ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡑࡥࡲ࡫ࠧઓ") in locals():
    bstack1l1ll_opy_ = os.path.abspath(fileName)
  else:
    bstack1l1ll_opy_ = bstack11ll1l_opy_ (u"࠭ࠧઔ")
  bstack1l11l1111l_opy_ = os.getcwd()
  bstack111llll111_opy_ = bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡹ࡮࡮ࠪક")
  bstack11l111l111_opy_ = bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺࡣࡰࡰࠬખ")
  while (not os.path.exists(bstack1l1ll_opy_)) and bstack1l11l1111l_opy_ != bstack11ll1l_opy_ (u"ࠤࠥગ"):
    bstack1l1ll_opy_ = os.path.join(bstack1l11l1111l_opy_, bstack111llll111_opy_)
    if not os.path.exists(bstack1l1ll_opy_):
      bstack1l1ll_opy_ = os.path.join(bstack1l11l1111l_opy_, bstack11l111l111_opy_)
    if bstack1l11l1111l_opy_ != os.path.dirname(bstack1l11l1111l_opy_):
      bstack1l11l1111l_opy_ = os.path.dirname(bstack1l11l1111l_opy_)
    else:
      bstack1l11l1111l_opy_ = bstack11ll1l_opy_ (u"ࠥࠦઘ")
  bstack111ll11lll_opy_ = bstack1l1ll_opy_ if os.path.exists(bstack1l1ll_opy_) else None
  return bstack111ll11lll_opy_
def bstack1ll11l1ll1_opy_(config):
    if bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࠫઙ") in config:
      config[bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩચ")] = config[bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬࠭છ")]
    if bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࡏࡱࡶ࡬ࡳࡳࡹࠧજ") in config:
      config[bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬઝ")] = config[bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࡑࡳࡸ࡮ࡵ࡮ࡴࠩઞ")]
def bstack1l111l1l1_opy_():
  bstack1l1ll_opy_ = bstack111l111l1_opy_()
  if not os.path.exists(bstack1l1ll_opy_):
    bstack1l111llll_opy_(
      bstack11ll1lll1l_opy_.format(os.getcwd()))
  try:
    with open(bstack1l1ll_opy_, bstack11ll1l_opy_ (u"ࠪࡶࠬટ")) as stream:
      yaml.add_implicit_resolver(bstack11ll1l_opy_ (u"ࠦࠦࡶࡡࡵࡪࡨࡼࠧઠ"), bstack1l111ll11l_opy_)
      yaml.add_constructor(bstack11ll1l_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨડ"), bstack11l1ll1l1_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1ll11l1ll1_opy_(config)
      return config
  except:
    with open(bstack1l1ll_opy_, bstack11ll1l_opy_ (u"࠭ࡲࠨઢ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1ll11l1ll1_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1l111llll_opy_(bstack1l1l1l111l_opy_.format(str(exc)))
def bstack11ll111l1_opy_(config):
  bstack1ll1lllll1_opy_ = bstack1l1lll111l_opy_(config)
  for option in list(bstack1ll1lllll1_opy_):
    if option.lower() in bstack111111111_opy_ and option != bstack111111111_opy_[option.lower()]:
      bstack1ll1lllll1_opy_[bstack111111111_opy_[option.lower()]] = bstack1ll1lllll1_opy_[option]
      del bstack1ll1lllll1_opy_[option]
  return config
def bstack1l11111l1_opy_():
  global bstack11ll1l11ll_opy_
  for key, bstack11ll11ll1l_opy_ in bstack11ll1ll1l_opy_.items():
    if isinstance(bstack11ll11ll1l_opy_, list):
      for var in bstack11ll11ll1l_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack11ll1l11ll_opy_[key] = os.environ[var]
          break
    elif bstack11ll11ll1l_opy_ in os.environ and os.environ[bstack11ll11ll1l_opy_] and str(os.environ[bstack11ll11ll1l_opy_]).strip():
      bstack11ll1l11ll_opy_[key] = os.environ[bstack11ll11ll1l_opy_]
  if bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩણ") in os.environ:
    bstack11ll1l11ll_opy_[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬત")] = {}
    bstack11ll1l11ll_opy_[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭થ")][bstack11ll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬદ")] = os.environ[bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭ધ")]
def bstack1ll111l1l_opy_():
  global bstack1ll1l1ll11_opy_
  global bstack11111l11l_opy_
  bstack11llll111_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack11ll1l_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨન").lower() == val.lower():
      bstack1ll1l1ll11_opy_[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ઩")] = {}
      bstack1ll1l1ll11_opy_[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫપ")][bstack11ll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪફ")] = sys.argv[idx + 1]
      bstack11llll111_opy_.extend([idx, idx + 1])
      break
  for key, bstack111lll111l_opy_ in bstack111111l111_opy_.items():
    if isinstance(bstack111lll111l_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack111lll111l_opy_:
          if bstack11ll1l_opy_ (u"ࠩ࠰࠱ࠬબ") + var.lower() == val.lower() and key not in bstack1ll1l1ll11_opy_:
            bstack1ll1l1ll11_opy_[key] = sys.argv[idx + 1]
            bstack11111l11l_opy_ += bstack11ll1l_opy_ (u"ࠪࠤ࠲࠳ࠧભ") + var + bstack11ll1l_opy_ (u"ࠫࠥ࠭મ") + shlex.quote(sys.argv[idx + 1])
            bstack11llll111_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack11ll1l_opy_ (u"ࠬ࠳࠭ࠨય") + bstack111lll111l_opy_.lower() == val.lower() and key not in bstack1ll1l1ll11_opy_:
          bstack1ll1l1ll11_opy_[key] = sys.argv[idx + 1]
          bstack11111l11l_opy_ += bstack11ll1l_opy_ (u"࠭ࠠ࠮࠯ࠪર") + bstack111lll111l_opy_ + bstack11ll1l_opy_ (u"ࠧࠡࠩ઱") + shlex.quote(sys.argv[idx + 1])
          bstack11llll111_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack11llll111_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack1ll1111ll1_opy_(config):
  bstack11lll1lll_opy_ = config.keys()
  for bstack1lll11l11l_opy_, bstack1l11l11l1_opy_ in bstack11l11l1ll_opy_.items():
    if bstack1l11l11l1_opy_ in bstack11lll1lll_opy_:
      config[bstack1lll11l11l_opy_] = config[bstack1l11l11l1_opy_]
      del config[bstack1l11l11l1_opy_]
  for bstack1lll11l11l_opy_, bstack1l11l11l1_opy_ in bstack1ll1ll1l1_opy_.items():
    if isinstance(bstack1l11l11l1_opy_, list):
      for bstack1l1ll1lll1_opy_ in bstack1l11l11l1_opy_:
        if bstack1l1ll1lll1_opy_ in bstack11lll1lll_opy_:
          config[bstack1lll11l11l_opy_] = config[bstack1l1ll1lll1_opy_]
          del config[bstack1l1ll1lll1_opy_]
          break
    elif bstack1l11l11l1_opy_ in bstack11lll1lll_opy_:
      config[bstack1lll11l11l_opy_] = config[bstack1l11l11l1_opy_]
      del config[bstack1l11l11l1_opy_]
  for bstack1l1ll1lll1_opy_ in list(config):
    for bstack1ll1ll1111_opy_ in bstack1l1lllll11_opy_:
      if bstack1l1ll1lll1_opy_.lower() == bstack1ll1ll1111_opy_.lower() and bstack1l1ll1lll1_opy_ != bstack1ll1ll1111_opy_:
        config[bstack1ll1ll1111_opy_] = config[bstack1l1ll1lll1_opy_]
        del config[bstack1l1ll1lll1_opy_]
  bstack1l1l1l1ll1_opy_ = [{}]
  if not config.get(bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫલ")):
    config[bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬળ")] = [{}]
  bstack1l1l1l1ll1_opy_ = config[bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭઴")]
  for platform in bstack1l1l1l1ll1_opy_:
    for bstack1l1ll1lll1_opy_ in list(platform):
      for bstack1ll1ll1111_opy_ in bstack1l1lllll11_opy_:
        if bstack1l1ll1lll1_opy_.lower() == bstack1ll1ll1111_opy_.lower() and bstack1l1ll1lll1_opy_ != bstack1ll1ll1111_opy_:
          platform[bstack1ll1ll1111_opy_] = platform[bstack1l1ll1lll1_opy_]
          del platform[bstack1l1ll1lll1_opy_]
  for bstack1lll11l11l_opy_, bstack1l11l11l1_opy_ in bstack1ll1ll1l1_opy_.items():
    for platform in bstack1l1l1l1ll1_opy_:
      if isinstance(bstack1l11l11l1_opy_, list):
        for bstack1l1ll1lll1_opy_ in bstack1l11l11l1_opy_:
          if bstack1l1ll1lll1_opy_ in platform:
            platform[bstack1lll11l11l_opy_] = platform[bstack1l1ll1lll1_opy_]
            del platform[bstack1l1ll1lll1_opy_]
            break
      elif bstack1l11l11l1_opy_ in platform:
        platform[bstack1lll11l11l_opy_] = platform[bstack1l11l11l1_opy_]
        del platform[bstack1l11l11l1_opy_]
  for bstack1lll1lll1l_opy_ in bstack11lll1l1l1_opy_:
    if bstack1lll1lll1l_opy_ in config:
      if not bstack11lll1l1l1_opy_[bstack1lll1lll1l_opy_] in config:
        config[bstack11lll1l1l1_opy_[bstack1lll1lll1l_opy_]] = {}
      config[bstack11lll1l1l1_opy_[bstack1lll1lll1l_opy_]].update(config[bstack1lll1lll1l_opy_])
      del config[bstack1lll1lll1l_opy_]
  for platform in bstack1l1l1l1ll1_opy_:
    for bstack1lll1lll1l_opy_ in bstack11lll1l1l1_opy_:
      if bstack1lll1lll1l_opy_ in list(platform):
        if not bstack11lll1l1l1_opy_[bstack1lll1lll1l_opy_] in platform:
          platform[bstack11lll1l1l1_opy_[bstack1lll1lll1l_opy_]] = {}
        platform[bstack11lll1l1l1_opy_[bstack1lll1lll1l_opy_]].update(platform[bstack1lll1lll1l_opy_])
        del platform[bstack1lll1lll1l_opy_]
  config = bstack11ll111l1_opy_(config)
  return config
def bstack1l1l11lll_opy_(config):
  global bstack1l11l1ll11_opy_
  bstack1l11l1l1l1_opy_ = False
  if bstack11ll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨવ") in config and str(config[bstack11ll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩશ")]).lower() != bstack11ll1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬષ"):
    if bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫસ") not in config or str(config[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬહ")]).lower() == bstack11ll1l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ઺"):
      config[bstack11ll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩ઻")] = False
    else:
      bstack1llllll1l1_opy_ = bstack111ll11111_opy_()
      if bstack11ll1l_opy_ (u"ࠫ࡮ࡹࡔࡳ࡫ࡤࡰࡌࡸࡩࡥ઼ࠩ") in bstack1llllll1l1_opy_:
        if not bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩઽ") in config:
          config[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪા")] = {}
        config[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫિ")][bstack11ll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪી")] = bstack11ll1l_opy_ (u"ࠩࡤࡸࡸ࠳ࡲࡦࡲࡨࡥࡹ࡫ࡲࠨુ")
        bstack1l11l1l1l1_opy_ = True
        bstack1l11l1ll11_opy_ = config[bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧૂ")].get(bstack11ll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ૃ"))
  if bstack11ll1l1l1_opy_(config) and bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩૄ") in config and str(config[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪૅ")]).lower() != bstack11ll1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭૆") and not bstack1l11l1l1l1_opy_:
    if not bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬે") in config:
      config[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ૈ")] = {}
    if not config[bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧૉ")].get(bstack11ll1l_opy_ (u"ࠫࡸࡱࡩࡱࡄ࡬ࡲࡦࡸࡹࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡤࡸ࡮ࡵ࡮ࠨ૊")) and not bstack11ll1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧો") in config[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪૌ")]:
      bstack1l111ll1_opy_ = datetime.datetime.now()
      bstack1llll1111l_opy_ = bstack1l111ll1_opy_.strftime(bstack11ll1l_opy_ (u"ࠧࠦࡦࡢࠩࡧࡥࠥࡉࠧࡐ્ࠫ"))
      hostname = socket.gethostname()
      bstack1l1ll1ll1_opy_ = bstack11ll1l_opy_ (u"ࠨࠩ૎").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11ll1l_opy_ (u"ࠩࡾࢁࡤࢁࡽࡠࡽࢀࠫ૏").format(bstack1llll1111l_opy_, hostname, bstack1l1ll1ll1_opy_)
      config[bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧૐ")][bstack11ll1l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૑")] = identifier
    bstack1l11l1ll11_opy_ = config[bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ૒")].get(bstack11ll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૓"))
  return config
def bstack1111l1lll1_opy_():
  bstack1l1l111111_opy_ =  bstack1l1ll1l1ll_opy_()[bstack11ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷ࠭૔")]
  return bstack1l1l111111_opy_ if bstack1l1l111111_opy_ else -1
def bstack1l11ll1lll_opy_(bstack1l1l111111_opy_):
  global CONFIG
  if not bstack11ll1l_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪ૕") in CONFIG[bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૖")]:
    return
  CONFIG[bstack11ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૗")] = CONFIG[bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૘")].replace(
    bstack11ll1l_opy_ (u"ࠬࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧ૙"),
    str(bstack1l1l111111_opy_)
  )
def bstack1l111ll1l_opy_():
  global CONFIG
  if not bstack11ll1l_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬ૚") in CONFIG[bstack11ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૛")]:
    return
  bstack1l111ll1_opy_ = datetime.datetime.now()
  bstack1llll1111l_opy_ = bstack1l111ll1_opy_.strftime(bstack11ll1l_opy_ (u"ࠨࠧࡧ࠱ࠪࡨ࠭ࠦࡊ࠽ࠩࡒ࠭૜"))
  CONFIG[bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૝")] = CONFIG[bstack11ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૞")].replace(
    bstack11ll1l_opy_ (u"ࠫࠩࢁࡄࡂࡖࡈࡣ࡙ࡏࡍࡆࡿࠪ૟"),
    bstack1llll1111l_opy_
  )
def bstack1l1l1ll1l1_opy_():
  global CONFIG
  if bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૠ") in CONFIG and not bool(CONFIG[bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨૡ")]):
    del CONFIG[bstack11ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩૢ")]
    return
  if not bstack11ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪૣ") in CONFIG:
    CONFIG[bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૤")] = bstack11ll1l_opy_ (u"ࠪࠧࠩࢁࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࢂ࠭૥")
  if bstack11ll1l_opy_ (u"ࠫࠩࢁࡄࡂࡖࡈࡣ࡙ࡏࡍࡆࡿࠪ૦") in CONFIG[bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૧")]:
    bstack1l111ll1l_opy_()
    os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪ૨")] = CONFIG[bstack11ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૩")]
  if not bstack11ll1l_opy_ (u"ࠨࠦࡾࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࡈࡅࡓࡿࠪ૪") in CONFIG[bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૫")]:
    return
  bstack1l1l111111_opy_ = bstack11ll1l_opy_ (u"ࠪࠫ૬")
  bstack1l1l1111l1_opy_ = bstack1111l1lll1_opy_()
  if bstack1l1l1111l1_opy_ != -1:
    bstack1l1l111111_opy_ = bstack11ll1l_opy_ (u"ࠫࡈࡏࠠࠨ૭") + str(bstack1l1l1111l1_opy_)
  if bstack1l1l111111_opy_ == bstack11ll1l_opy_ (u"ࠬ࠭૮"):
    bstack1ll1ll11ll_opy_ = bstack11l1ll111l_opy_(CONFIG[bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ૯")])
    if bstack1ll1ll11ll_opy_ != -1:
      bstack1l1l111111_opy_ = str(bstack1ll1ll11ll_opy_)
  if bstack1l1l111111_opy_:
    bstack1l11ll1lll_opy_(bstack1l1l111111_opy_)
    os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ૰")] = CONFIG[bstack11ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૱")]
def bstack11l1ll1l1l_opy_(bstack11111l1l1l_opy_, bstack111l1l111_opy_, path):
  json_data = {
    bstack11ll1l_opy_ (u"ࠩ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૲"): bstack111l1l111_opy_
  }
  if os.path.exists(path):
    bstack1111l1111l_opy_ = json.load(open(path, bstack11ll1l_opy_ (u"ࠪࡶࡧ࠭૳")))
  else:
    bstack1111l1111l_opy_ = {}
  bstack1111l1111l_opy_[bstack11111l1l1l_opy_] = json_data
  with open(path, bstack11ll1l_opy_ (u"ࠦࡼ࠱ࠢ૴")) as outfile:
    json.dump(bstack1111l1111l_opy_, outfile)
def bstack11l1ll111l_opy_(bstack11111l1l1l_opy_):
  bstack11111l1l1l_opy_ = str(bstack11111l1l1l_opy_)
  bstack11lllll1l1_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠬࢄࠧ૵")), bstack11ll1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭૶"))
  try:
    if not os.path.exists(bstack11lllll1l1_opy_):
      os.makedirs(bstack11lllll1l1_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠧࡿࠩ૷")), bstack11ll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ૸"), bstack11ll1l_opy_ (u"ࠩ࠱ࡦࡺ࡯࡬ࡥ࠯ࡱࡥࡲ࡫࠭ࡤࡣࡦ࡬ࡪ࠴ࡪࡴࡱࡱࠫૹ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11ll1l_opy_ (u"ࠪࡻࠬૺ")):
        pass
      with open(file_path, bstack11ll1l_opy_ (u"ࠦࡼ࠱ࠢૻ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11ll1l_opy_ (u"ࠬࡸࠧૼ")) as bstack1l11ll1ll_opy_:
      bstack1ll1ll11l_opy_ = json.load(bstack1l11ll1ll_opy_)
    if bstack11111l1l1l_opy_ in bstack1ll1ll11l_opy_:
      bstack1l11lll1ll_opy_ = bstack1ll1ll11l_opy_[bstack11111l1l1l_opy_][bstack11ll1l_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૽")]
      bstack1ll11l1ll_opy_ = int(bstack1l11lll1ll_opy_) + 1
      bstack11l1ll1l1l_opy_(bstack11111l1l1l_opy_, bstack1ll11l1ll_opy_, file_path)
      return bstack1ll11l1ll_opy_
    else:
      bstack11l1ll1l1l_opy_(bstack11111l1l1l_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1l11l11l11_opy_.format(str(e)))
    return -1
def bstack11l11ll11l_opy_(config):
  if not config[bstack11ll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ૾")] or not config[bstack11ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫ૿")]:
    return True
  else:
    return False
def bstack1111ll1l1_opy_(config, index=0):
  global bstack11ll11l111_opy_
  bstack11ll11l1l_opy_ = {}
  caps = bstack1l11111lll_opy_ + bstack11lll1l11_opy_
  if config.get(bstack11ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭଀"), False):
    bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧଁ")] = True
    bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨଂ")] = config.get(bstack11ll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩଃ"), {})
  if bstack11ll11l111_opy_:
    caps += bstack111ll111l1_opy_
  for key in config:
    if key in caps + [bstack11ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ଄")]:
      continue
    bstack11ll11l1l_opy_[key] = config[key]
  if bstack11ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଅ") in config:
    for bstack1ll1l1l11l_opy_ in config[bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଆ")][index]:
      if bstack1ll1l1l11l_opy_ in caps:
        continue
      bstack11ll11l1l_opy_[bstack1ll1l1l11l_opy_] = config[bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଇ")][index][bstack1ll1l1l11l_opy_]
  bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"ࠪ࡬ࡴࡹࡴࡏࡣࡰࡩࠬଈ")] = socket.gethostname()
  if bstack11ll1l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬଉ") in bstack11ll11l1l_opy_:
    del (bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ଊ")])
  return bstack11ll11l1l_opy_
def bstack1ll1lll111_opy_(config):
  global bstack11ll11l111_opy_
  bstack1ll1l1111_opy_ = {}
  caps = bstack11lll1l11_opy_
  if bstack11ll11l111_opy_:
    caps += bstack111ll111l1_opy_
  for key in caps:
    if key in config:
      bstack1ll1l1111_opy_[key] = config[key]
  return bstack1ll1l1111_opy_
def bstack111111l1ll_opy_(bstack11ll11l1l_opy_, bstack1ll1l1111_opy_):
  bstack11l11111l_opy_ = {}
  for key in bstack11ll11l1l_opy_.keys():
    if key in bstack11l11l1ll_opy_:
      bstack11l11111l_opy_[bstack11l11l1ll_opy_[key]] = bstack11ll11l1l_opy_[key]
    else:
      bstack11l11111l_opy_[key] = bstack11ll11l1l_opy_[key]
  for key in bstack1ll1l1111_opy_:
    if key in bstack11l11l1ll_opy_:
      bstack11l11111l_opy_[bstack11l11l1ll_opy_[key]] = bstack1ll1l1111_opy_[key]
    else:
      bstack11l11111l_opy_[key] = bstack1ll1l1111_opy_[key]
  return bstack11l11111l_opy_
def bstack1ll11ll1l1_opy_(config, index=0):
  global bstack11ll11l111_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11ll1l1111_opy_ = bstack11l1l111ll_opy_(bstack1l1ll1111l_opy_, config, logger)
  bstack1ll1l1111_opy_ = bstack1ll1lll111_opy_(config)
  bstack1lll1l111l_opy_ = bstack11lll1l11_opy_
  bstack1lll1l111l_opy_ += bstack11l11111l1_opy_
  bstack1ll1l1111_opy_ = update(bstack1ll1l1111_opy_, bstack11ll1l1111_opy_)
  if bstack11ll11l111_opy_:
    bstack1lll1l111l_opy_ += bstack111ll111l1_opy_
  if bstack11ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩଋ") in config:
    if bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬଌ") in config[bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ଍")][index]:
      caps[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ଎")] = config[bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଏ")][index][bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଐ")]
    if bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭଑") in config[bstack11ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ଒")][index]:
      caps[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨଓ")] = str(config[bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଔ")][index][bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪକ")])
    bstack1ll1l1l1ll_opy_ = bstack11l1l111ll_opy_(bstack1l1ll1111l_opy_, config[bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଖ")][index], logger)
    bstack1lll1l111l_opy_ += list(bstack1ll1l1l1ll_opy_.keys())
    for bstack11111l11ll_opy_ in bstack1lll1l111l_opy_:
      if bstack11111l11ll_opy_ in config[bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଗ")][index]:
        if bstack11111l11ll_opy_ == bstack11ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧଘ"):
          try:
            bstack1ll1l1l1ll_opy_[bstack11111l11ll_opy_] = str(config[bstack11ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩଙ")][index][bstack11111l11ll_opy_] * 1.0)
          except:
            bstack1ll1l1l1ll_opy_[bstack11111l11ll_opy_] = str(config[bstack11ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଚ")][index][bstack11111l11ll_opy_])
        else:
          bstack1ll1l1l1ll_opy_[bstack11111l11ll_opy_] = config[bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଛ")][index][bstack11111l11ll_opy_]
        del (config[bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଜ")][index][bstack11111l11ll_opy_])
    bstack1ll1l1111_opy_ = update(bstack1ll1l1111_opy_, bstack1ll1l1l1ll_opy_)
  bstack11ll11l1l_opy_ = bstack1111ll1l1_opy_(config, index)
  for bstack1l1ll1lll1_opy_ in bstack11lll1l11_opy_ + list(bstack11ll1l1111_opy_.keys()):
    if bstack1l1ll1lll1_opy_ in bstack11ll11l1l_opy_:
      bstack1ll1l1111_opy_[bstack1l1ll1lll1_opy_] = bstack11ll11l1l_opy_[bstack1l1ll1lll1_opy_]
      del (bstack11ll11l1l_opy_[bstack1l1ll1lll1_opy_])
  if bstack1ll1l111l_opy_(config):
    bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"ࠪࡹࡸ࡫ࡗ࠴ࡅࠪଝ")] = True
    caps.update(bstack1ll1l1111_opy_)
    caps[bstack11ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬଞ")] = bstack11ll11l1l_opy_
  else:
    bstack11ll11l1l_opy_[bstack11ll1l_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬଟ")] = False
    caps.update(bstack111111l1ll_opy_(bstack11ll11l1l_opy_, bstack1ll1l1111_opy_))
    if bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫଠ") in caps:
      caps[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨଡ")] = caps[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ଢ")]
      del (caps[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧଣ")])
    if bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫତ") in caps:
      caps[bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ଥ")] = caps[bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଦ")]
      del (caps[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧଧ")])
  return caps
def bstack1llll1lll1_opy_():
  global bstack11llll11l_opy_
  global CONFIG
  if bstack111llllll_opy_() <= version.parse(bstack11ll1l_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧନ")):
    if bstack11llll11l_opy_ != bstack11ll1l_opy_ (u"ࠨࠩ଩"):
      return bstack11ll1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥପ") + bstack11llll11l_opy_ + bstack11ll1l_opy_ (u"ࠥ࠾࠽࠶࠯ࡸࡦ࠲࡬ࡺࡨࠢଫ")
    return bstack11111lll1l_opy_
  if bstack11llll11l_opy_ != bstack11ll1l_opy_ (u"ࠫࠬବ"):
    return bstack11ll1l_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢଭ") + bstack11llll11l_opy_ + bstack11ll1l_opy_ (u"ࠨ࠯ࡸࡦ࠲࡬ࡺࡨࠢମ")
  return bstack1l1llll1l_opy_
def bstack11111ll1l_opy_(options):
  return hasattr(options, bstack11ll1l_opy_ (u"ࠧࡴࡧࡷࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡹࠨଯ"))
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
def bstack11l111lll_opy_(options, bstack1l11l1111_opy_):
  for bstack111llll1l1_opy_ in bstack1l11l1111_opy_:
    if bstack111llll1l1_opy_ in [bstack11ll1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ର"), bstack11ll1l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭଱")]:
      continue
    if bstack111llll1l1_opy_ in options._experimental_options:
      options._experimental_options[bstack111llll1l1_opy_] = update(options._experimental_options[bstack111llll1l1_opy_],
                                                         bstack1l11l1111_opy_[bstack111llll1l1_opy_])
    else:
      options.add_experimental_option(bstack111llll1l1_opy_, bstack1l11l1111_opy_[bstack111llll1l1_opy_])
  if bstack11ll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଲ") in bstack1l11l1111_opy_:
    for arg in bstack1l11l1111_opy_[bstack11ll1l_opy_ (u"ࠫࡦࡸࡧࡴࠩଳ")]:
      options.add_argument(arg)
    del (bstack1l11l1111_opy_[bstack11ll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪ଴")])
  if bstack11ll1l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪଵ") in bstack1l11l1111_opy_:
    for ext in bstack1l11l1111_opy_[bstack11ll1l_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫଶ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l11l1111_opy_[bstack11ll1l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬଷ")])
def bstack111111l11_opy_(options, bstack1l1ll11ll1_opy_):
  if bstack11ll1l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨସ") in bstack1l1ll11ll1_opy_:
    for bstack1llll1ll1l_opy_ in bstack1l1ll11ll1_opy_[bstack11ll1l_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩହ")]:
      if bstack1llll1ll1l_opy_ in options._preferences:
        options._preferences[bstack1llll1ll1l_opy_] = update(options._preferences[bstack1llll1ll1l_opy_], bstack1l1ll11ll1_opy_[bstack11ll1l_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ଺")][bstack1llll1ll1l_opy_])
      else:
        options.set_preference(bstack1llll1ll1l_opy_, bstack1l1ll11ll1_opy_[bstack11ll1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ଻")][bstack1llll1ll1l_opy_])
  if bstack11ll1l_opy_ (u"࠭ࡡࡳࡩࡶ଼ࠫ") in bstack1l1ll11ll1_opy_:
    for arg in bstack1l1ll11ll1_opy_[bstack11ll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬଽ")]:
      options.add_argument(arg)
def bstack1111l1lll_opy_(options, bstack11111l111l_opy_):
  if bstack11ll1l_opy_ (u"ࠨࡹࡨࡦࡻ࡯ࡥࡸࠩା") in bstack11111l111l_opy_:
    options.use_webview(bool(bstack11111l111l_opy_[bstack11ll1l_opy_ (u"ࠩࡺࡩࡧࡼࡩࡦࡹࠪି")]))
  bstack11l111lll_opy_(options, bstack11111l111l_opy_)
def bstack1111l1l1l1_opy_(options, bstack11l11lll1l_opy_):
  for bstack1lllllll1l_opy_ in bstack11l11lll1l_opy_:
    if bstack1lllllll1l_opy_ in [bstack11ll1l_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧୀ"), bstack11ll1l_opy_ (u"ࠫࡦࡸࡧࡴࠩୁ")]:
      continue
    options.set_capability(bstack1lllllll1l_opy_, bstack11l11lll1l_opy_[bstack1lllllll1l_opy_])
  if bstack11ll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪୂ") in bstack11l11lll1l_opy_:
    for arg in bstack11l11lll1l_opy_[bstack11ll1l_opy_ (u"࠭ࡡࡳࡩࡶࠫୃ")]:
      options.add_argument(arg)
  if bstack11ll1l_opy_ (u"ࠧࡵࡧࡦ࡬ࡳࡵ࡬ࡰࡩࡼࡔࡷ࡫ࡶࡪࡧࡺࠫୄ") in bstack11l11lll1l_opy_:
    options.bstack1l11lllll1_opy_(bool(bstack11l11lll1l_opy_[bstack11ll1l_opy_ (u"ࠨࡶࡨࡧ࡭ࡴ࡯࡭ࡱࡪࡽࡕࡸࡥࡷ࡫ࡨࡻࠬ୅")]))
def bstack11ll111l11_opy_(options, bstack1ll1llllll_opy_):
  for bstack1ll1l1l1l1_opy_ in bstack1ll1llllll_opy_:
    if bstack1ll1l1l1l1_opy_ in [bstack11ll1l_opy_ (u"ࠩࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭୆"), bstack11ll1l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨେ")]:
      continue
    options._options[bstack1ll1l1l1l1_opy_] = bstack1ll1llllll_opy_[bstack1ll1l1l1l1_opy_]
  if bstack11ll1l_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨୈ") in bstack1ll1llllll_opy_:
    for bstack1111l1l1l_opy_ in bstack1ll1llllll_opy_[bstack11ll1l_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୉")]:
      options.bstack11lllll11_opy_(
        bstack1111l1l1l_opy_, bstack1ll1llllll_opy_[bstack11ll1l_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ୊")][bstack1111l1l1l_opy_])
  if bstack11ll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬୋ") in bstack1ll1llllll_opy_:
    for arg in bstack1ll1llllll_opy_[bstack11ll1l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ୌ")]:
      options.add_argument(arg)
def bstack1l1ll11111_opy_(options, caps):
  if not hasattr(options, bstack11ll1l_opy_ (u"ࠩࡎࡉ࡞୍࠭")):
    return
  if options.KEY == bstack11ll1l_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ୎"):
    options = bstack1lllll1l1_opy_.bstack1llll1l11l_opy_(bstack11lll1ll1_opy_=options, config=CONFIG)
  if options.KEY == bstack11ll1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୏") and options.KEY in caps:
    bstack11l111lll_opy_(options, caps[bstack11ll1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ୐")])
  elif options.KEY == bstack11ll1l_opy_ (u"࠭࡭ࡰࡼ࠽ࡪ࡮ࡸࡥࡧࡱࡻࡓࡵࡺࡩࡰࡰࡶࠫ୑") and options.KEY in caps:
    bstack111111l11_opy_(options, caps[bstack11ll1l_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬ୒")])
  elif options.KEY == bstack11ll1l_opy_ (u"ࠨࡵࡤࡪࡦࡸࡩ࠯ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ୓") and options.KEY in caps:
    bstack1111l1l1l1_opy_(options, caps[bstack11ll1l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪ୔")])
  elif options.KEY == bstack11ll1l_opy_ (u"ࠪࡱࡸࡀࡥࡥࡩࡨࡓࡵࡺࡩࡰࡰࡶࠫ୕") and options.KEY in caps:
    bstack1111l1lll_opy_(options, caps[bstack11ll1l_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬୖ")])
  elif options.KEY == bstack11ll1l_opy_ (u"ࠬࡹࡥ࠻࡫ࡨࡓࡵࡺࡩࡰࡰࡶࠫୗ") and options.KEY in caps:
    bstack11ll111l11_opy_(options, caps[bstack11ll1l_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬ୘")])
def bstack1ll11l11l_opy_(caps):
  global bstack11ll11l111_opy_
  if isinstance(os.environ.get(bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ୙")), str):
    bstack11ll11l111_opy_ = eval(os.getenv(bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ୚")))
  if bstack11ll11l111_opy_:
    if bstack11l1ll1ll1_opy_() < version.parse(bstack11ll1l_opy_ (u"ࠩ࠵࠲࠸࠴࠰ࠨ୛")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11ll1l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪଡ଼")
    if bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଢ଼") in caps:
      browser = caps[bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ୞")]
    elif bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࠧୟ") in caps:
      browser = caps[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨୠ")]
    browser = str(browser).lower()
    if browser == bstack11ll1l_opy_ (u"ࠨ࡫ࡳ࡬ࡴࡴࡥࠨୡ") or browser == bstack11ll1l_opy_ (u"ࠩ࡬ࡴࡦࡪࠧୢ"):
      browser = bstack11ll1l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪୣ")
    if browser == bstack11ll1l_opy_ (u"ࠫࡸࡧ࡭ࡴࡷࡱ࡫ࠬ୤"):
      browser = bstack11ll1l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ୥")
    if browser not in [bstack11ll1l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭୦"), bstack11ll1l_opy_ (u"ࠧࡦࡦࡪࡩࠬ୧"), bstack11ll1l_opy_ (u"ࠨ࡫ࡨࠫ୨"), bstack11ll1l_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩ୩"), bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫ୪")]:
      return None
    try:
      package = bstack11ll1l_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠴ࡷࡦࡤࡧࡶ࡮ࡼࡥࡳ࠰ࡾࢁ࠳ࡵࡰࡵ࡫ࡲࡲࡸ࠭୫").format(browser)
      name = bstack11ll1l_opy_ (u"ࠬࡕࡰࡵ࡫ࡲࡲࡸ࠭୬")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11111ll1l_opy_(options):
        return None
      for bstack1l1ll1lll1_opy_ in caps.keys():
        options.set_capability(bstack1l1ll1lll1_opy_, caps[bstack1l1ll1lll1_opy_])
      bstack1l1ll11111_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack111lll111_opy_(options, bstack1l11ll1l1l_opy_):
  if not bstack11111ll1l_opy_(options):
    return
  for bstack1l1ll1lll1_opy_ in bstack1l11ll1l1l_opy_.keys():
    if bstack1l1ll1lll1_opy_ in bstack11l11111l1_opy_:
      continue
    if bstack1l1ll1lll1_opy_ in options._caps and type(options._caps[bstack1l1ll1lll1_opy_]) in [dict, list]:
      options._caps[bstack1l1ll1lll1_opy_] = update(options._caps[bstack1l1ll1lll1_opy_], bstack1l11ll1l1l_opy_[bstack1l1ll1lll1_opy_])
    else:
      options.set_capability(bstack1l1ll1lll1_opy_, bstack1l11ll1l1l_opy_[bstack1l1ll1lll1_opy_])
  bstack1l1ll11111_opy_(options, bstack1l11ll1l1l_opy_)
  if bstack11ll1l_opy_ (u"࠭࡭ࡰࡼ࠽ࡨࡪࡨࡵࡨࡩࡨࡶࡆࡪࡤࡳࡧࡶࡷࠬ୭") in options._caps:
    if options._caps[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ୮")] and options._caps[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭୯")].lower() != bstack11ll1l_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪ୰"):
      del options._caps[bstack11ll1l_opy_ (u"ࠪࡱࡴࢀ࠺ࡥࡧࡥࡹ࡬࡭ࡥࡳࡃࡧࡨࡷ࡫ࡳࡴࠩୱ")]
def bstack1111llll11_opy_(proxy_config):
  if bstack11ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨ୲") in proxy_config:
    proxy_config[bstack11ll1l_opy_ (u"ࠬࡹࡳ࡭ࡒࡵࡳࡽࡿࠧ୳")] = proxy_config[bstack11ll1l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ୴")]
    del (proxy_config[bstack11ll1l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ୵")])
  if bstack11ll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ୶") in proxy_config and proxy_config[bstack11ll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬ୷")].lower() != bstack11ll1l_opy_ (u"ࠪࡨ࡮ࡸࡥࡤࡶࠪ୸"):
    proxy_config[bstack11ll1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧ୹")] = bstack11ll1l_opy_ (u"ࠬࡳࡡ࡯ࡷࡤࡰࠬ୺")
  if bstack11ll1l_opy_ (u"࠭ࡰࡳࡱࡻࡽࡆࡻࡴࡰࡥࡲࡲ࡫࡯ࡧࡖࡴ࡯ࠫ୻") in proxy_config:
    proxy_config[bstack11ll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࡚ࡹࡱࡧࠪ୼")] = bstack11ll1l_opy_ (u"ࠨࡲࡤࡧࠬ୽")
  return proxy_config
def bstack1l111l1ll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11ll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࠨ୾") in config:
    return proxy
  config[bstack11ll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩ୿")] = bstack1111llll11_opy_(config[bstack11ll1l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ஀")])
  if proxy == None:
    proxy = Proxy(config[bstack11ll1l_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ஁")])
  return proxy
def bstack1ll1ll1ll_opy_(self):
  global CONFIG
  global bstack111ll1ll1l_opy_
  try:
    proxy = bstack111lll1111_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11ll1l_opy_ (u"࠭࠮ࡱࡣࡦࠫஂ")):
        proxies = bstack11l11lllll_opy_(proxy, bstack1llll1lll1_opy_())
        if len(proxies) > 0:
          protocol, bstack1llllllll1_opy_ = proxies.popitem()
          if bstack11ll1l_opy_ (u"ࠢ࠻࠱࠲ࠦஃ") in bstack1llllllll1_opy_:
            return bstack1llllllll1_opy_
          else:
            return bstack11ll1l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤ஄") + bstack1llllllll1_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨஅ").format(str(e)))
  return bstack111ll1ll1l_opy_(self)
def bstack1111l11lll_opy_():
  global CONFIG
  return bstack1111ll111l_opy_(CONFIG) and bstack11l11l1l11_opy_() and bstack111llllll_opy_() >= version.parse(bstack11ll1lll11_opy_)
def bstack11111lllll_opy_():
  global CONFIG
  return (bstack11ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ஆ") in CONFIG or bstack11ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨஇ") in CONFIG) and bstack1l11ll1l1_opy_()
def bstack1l1lll111l_opy_(config):
  bstack1ll1lllll1_opy_ = {}
  if bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩஈ") in config:
    bstack1ll1lllll1_opy_ = config[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪஉ")]
  if bstack11ll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ஊ") in config:
    bstack1ll1lllll1_opy_ = config[bstack11ll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ஋")]
  proxy = bstack111lll1111_opy_(config)
  if proxy:
    if proxy.endswith(bstack11ll1l_opy_ (u"ࠩ࠱ࡴࡦࡩࠧ஌")) and os.path.isfile(proxy):
      bstack1ll1lllll1_opy_[bstack11ll1l_opy_ (u"ࠪ࠱ࡵࡧࡣ࠮ࡨ࡬ࡰࡪ࠭஍")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11ll1l_opy_ (u"ࠫ࠳ࡶࡡࡤࠩஎ")):
        proxies = bstack1ll11ll1l_opy_(config, bstack1llll1lll1_opy_())
        if len(proxies) > 0:
          protocol, bstack1llllllll1_opy_ = proxies.popitem()
          if bstack11ll1l_opy_ (u"ࠧࡀ࠯࠰ࠤஏ") in bstack1llllllll1_opy_:
            parsed_url = urlparse(bstack1llllllll1_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11ll1l_opy_ (u"ࠨ࠺࠰࠱ࠥஐ") + bstack1llllllll1_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1ll1lllll1_opy_[bstack11ll1l_opy_ (u"ࠧࡱࡴࡲࡼࡾࡎ࡯ࡴࡶࠪ஑")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1ll1lllll1_opy_[bstack11ll1l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡐࡰࡴࡷࠫஒ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1ll1lllll1_opy_[bstack11ll1l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡖࡵࡨࡶࠬஓ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1ll1lllll1_opy_[bstack11ll1l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡤࡷࡸ࠭ஔ")] = str(parsed_url.password)
  return bstack1ll1lllll1_opy_
def bstack111lllll1_opy_(config):
  if bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡅࡲࡲࡹ࡫ࡸࡵࡑࡳࡸ࡮ࡵ࡮ࡴࠩக") in config:
    return config[bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪ஖")]
  return {}
def bstack1l111l11ll_opy_(caps):
  global bstack1l11l1ll11_opy_
  if bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ஗") in caps:
    caps[bstack11ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ஘")][bstack11ll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࠧங")] = True
    if bstack1l11l1ll11_opy_:
      caps[bstack11ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪச")][bstack11ll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ஛")] = bstack1l11l1ll11_opy_
  else:
    caps[bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡰࡴࡩࡡ࡭ࠩஜ")] = True
    if bstack1l11l1ll11_opy_:
      caps[bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭஝")] = bstack1l11l1ll11_opy_
@measure(event_name=EVENTS.bstack1ll11l1lll_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack1111l11ll_opy_():
  global CONFIG
  if not bstack11ll1l1l1_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪஞ") in CONFIG and bstack1ll11lll11_opy_(CONFIG[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫட")]):
    if (
      bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ஠") in CONFIG
      and bstack1ll11lll11_opy_(CONFIG[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭஡")].get(bstack11ll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡃ࡫ࡱࡥࡷࡿࡉ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡣࡷ࡭ࡴࡴࠧ஢")))
    ):
      logger.debug(bstack11ll1l_opy_ (u"ࠦࡑࡵࡣࡢ࡮ࠣࡦ࡮ࡴࡡࡳࡻࠣࡲࡴࡺࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡣࡶࠤࡸࡱࡩࡱࡄ࡬ࡲࡦࡸࡹࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤࡪࡴࡡࡣ࡮ࡨࡨࠧண"))
      return
    bstack1ll1lllll1_opy_ = bstack1l1lll111l_opy_(CONFIG)
    bstack11l1lllll1_opy_(CONFIG[bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨத")], bstack1ll1lllll1_opy_)
def bstack11l1lllll1_opy_(key, bstack1ll1lllll1_opy_):
  global bstack11lll1ll1l_opy_
  logger.info(bstack1l1l11lll1_opy_)
  try:
    bstack11lll1ll1l_opy_ = Local()
    bstack11ll1111l1_opy_ = {bstack11ll1l_opy_ (u"࠭࡫ࡦࡻࠪ஥"): key}
    bstack11ll1111l1_opy_.update(bstack1ll1lllll1_opy_)
    logger.debug(bstack1l1l111lll_opy_.format(str(bstack11ll1111l1_opy_)).replace(key, bstack11ll1l_opy_ (u"ࠧ࡜ࡔࡈࡈࡆࡉࡔࡆࡆࡠࠫ஦")))
    bstack11lll1ll1l_opy_.start(**bstack11ll1111l1_opy_)
    if bstack11lll1ll1l_opy_.isRunning():
      logger.info(bstack1llllll11l_opy_)
  except Exception as e:
    bstack1l111llll_opy_(bstack1111l1ll1l_opy_.format(str(e)))
def bstack1l1lll1l1_opy_():
  global bstack11lll1ll1l_opy_
  if bstack11lll1ll1l_opy_.isRunning():
    logger.info(bstack1ll1l11ll_opy_)
    bstack11lll1ll1l_opy_.stop()
  bstack11lll1ll1l_opy_ = None
def bstack11l1lll1l_opy_(bstack1lll1ll1ll_opy_=[]):
  global CONFIG
  bstack1lll1ll11l_opy_ = []
  bstack11lllllll_opy_ = [bstack11ll1l_opy_ (u"ࠨࡱࡶࠫ஧"), bstack11ll1l_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬந"), bstack11ll1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧன"), bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ப"), bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ஫"), bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ஬")]
  try:
    for err in bstack1lll1ll1ll_opy_:
      bstack1l1l1lll1l_opy_ = {}
      for k in bstack11lllllll_opy_:
        val = CONFIG[bstack11ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ஭")][int(err[bstack11ll1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧம")])].get(k)
        if val:
          bstack1l1l1lll1l_opy_[k] = val
      if(err[bstack11ll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨய")] != bstack11ll1l_opy_ (u"ࠪࠫர")):
        bstack1l1l1lll1l_opy_[bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡵࠪற")] = {
          err[bstack11ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪல")]: err[bstack11ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬள")]
        }
        bstack1lll1ll11l_opy_.append(bstack1l1l1lll1l_opy_)
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡳࡷࡳࡡࡵࡶ࡬ࡲ࡬ࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡧࡹࡩࡳࡺ࠺ࠡࠩழ") + str(e))
  finally:
    return bstack1lll1ll11l_opy_
def bstack1111llll1l_opy_(file_name):
  bstack1l111111l_opy_ = []
  try:
    bstack1l111l111l_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1l111l111l_opy_):
      with open(bstack1l111l111l_opy_) as f:
        bstack11lll11111_opy_ = json.load(f)
        bstack1l111111l_opy_ = bstack11lll11111_opy_
      os.remove(bstack1l111l111l_opy_)
    return bstack1l111111l_opy_
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪ࡮ࡴࡤࡪࡰࡪࠤࡪࡸࡲࡰࡴࠣࡰ࡮ࡹࡴ࠻ࠢࠪவ") + str(e))
    return bstack1l111111l_opy_
def bstack1111lllll1_opy_():
  try:
      from bstack_utils.constants import bstack1l1111ll1_opy_, EVENTS
      from bstack_utils.helper import bstack1l1llllll_opy_, get_host_info, bstack111ll1l1_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack1llll11ll1_opy_ = os.path.join(os.getcwd(), bstack11ll1l_opy_ (u"ࠩ࡯ࡳ࡬࠭ஶ"), bstack11ll1l_opy_ (u"ࠪ࡯ࡪࡿ࠭࡮ࡧࡷࡶ࡮ࡩࡳ࠯࡬ࡶࡳࡳ࠭ஷ"))
      lock = FileLock(bstack1llll11ll1_opy_+bstack11ll1l_opy_ (u"ࠦ࠳ࡲ࡯ࡤ࡭ࠥஸ"))
      def bstack1lll1111_opy_():
          try:
              with lock:
                  with open(bstack1llll11ll1_opy_, bstack11ll1l_opy_ (u"ࠧࡸࠢஹ"), encoding=bstack11ll1l_opy_ (u"ࠨࡵࡵࡨ࠰࠼ࠧ஺")) as file:
                      data = json.load(file)
                      config = {
                          bstack11ll1l_opy_ (u"ࠢࡩࡧࡤࡨࡪࡸࡳࠣ஻"): {
                              bstack11ll1l_opy_ (u"ࠣࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠢ஼"): bstack11ll1l_opy_ (u"ࠤࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠧ஽"),
                          }
                      }
                      bstack1lllllllll_opy_ = datetime.utcnow()
                      bstack1l111ll1_opy_ = bstack1lllllllll_opy_.strftime(bstack11ll1l_opy_ (u"ࠥࠩ࡞࠳ࠥ࡮࠯ࠨࡨ࡙ࠫࡈ࠻ࠧࡐ࠾࡙ࠪ࠮ࠦࡨ࡙࡙ࠣࡉࠢா"))
                      test_id = os.environ.get(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩி")) if os.environ.get(bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪீ")) else bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠨࡳࡥ࡭ࡕࡹࡳࡏࡤࠣு"))
                      payload = {
                          bstack11ll1l_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠦூ"): bstack11ll1l_opy_ (u"ࠣࡵࡧ࡯ࡤ࡫ࡶࡦࡰࡷࡷࠧ௃"),
                          bstack11ll1l_opy_ (u"ࠤࡧࡥࡹࡧࠢ௄"): {
                              bstack11ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡩࡷࡥࡣࡺࡻࡩࡥࠤ௅"): test_id,
                              bstack11ll1l_opy_ (u"ࠦࡨࡸࡥࡢࡶࡨࡨࡤࡪࡡࡺࠤெ"): bstack1l111ll1_opy_,
                              bstack11ll1l_opy_ (u"ࠧ࡫ࡶࡦࡰࡷࡣࡳࡧ࡭ࡦࠤே"): bstack11ll1l_opy_ (u"ࠨࡓࡅࡍࡉࡩࡦࡺࡵࡳࡧࡓࡩࡷ࡬࡯ࡳ࡯ࡤࡲࡨ࡫ࠢை"),
                              bstack11ll1l_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥࡪࡴࡱࡱࠦ௉"): {
                                  bstack11ll1l_opy_ (u"ࠣ࡯ࡨࡥࡸࡻࡲࡦࡵࠥொ"): data,
                                  bstack11ll1l_opy_ (u"ࠤࡶࡨࡰࡘࡵ࡯ࡋࡧࠦோ"): bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠥࡷࡩࡱࡒࡶࡰࡌࡨࠧௌ"))
                              },
                              bstack11ll1l_opy_ (u"ࠦࡺࡹࡥࡳࡡࡧࡥࡹࡧ்ࠢ"): bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠧࡻࡳࡦࡴࡑࡥࡲ࡫ࠢ௎")),
                              bstack11ll1l_opy_ (u"ࠨࡨࡰࡵࡷࡣ࡮ࡴࡦࡰࠤ௏"): get_host_info()
                          }
                      }
                      bstack111lll1ll1_opy_ = bstack1lll1l11l1_opy_(cli.config, [bstack11ll1l_opy_ (u"ࠢࡢࡲ࡬ࡷࠧௐ"), bstack11ll1l_opy_ (u"ࠣࡧࡧࡷࡎࡴࡳࡵࡴࡸࡱࡪࡴࡴࡢࡶ࡬ࡳࡳࠨ௑"), bstack11ll1l_opy_ (u"ࠤࡤࡴ࡮ࠨ௒")], bstack1l1111ll1_opy_)
                      response = bstack1l1llllll_opy_(bstack11ll1l_opy_ (u"ࠥࡔࡔ࡙ࡔࠣ௓"), bstack111lll1ll1_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack11ll1l_opy_ (u"ࠦࡉࡧࡴࡢࠢࡶࡩࡳࡺࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡴࡰࠢࡾࢁࠥࡽࡩࡵࡪࠣࡨࡦࡺࡡࠡࡽࢀࠦ௔").format(bstack1l1111ll1_opy_, payload))
                      else:
                          logger.debug(bstack11ll1l_opy_ (u"ࠧࡘࡥࡲࡷࡨࡷࡹࠦࡦࡢ࡫࡯ࡩࡩࠦࡦࡰࡴࠣࡿࢂࠦࡷࡪࡶ࡫ࠤࡩࡧࡴࡢࠢࡾࢁࠧ௕").format(bstack1l1111ll1_opy_, payload))
          except Exception as e:
              logger.debug(bstack11ll1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡳࡪࠠ࡬ࡧࡼࠤࡲ࡫ࡴࡳ࡫ࡦࡷࠥࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠࡼࡿࠥ௖").format(e))
      bstack1lll1111_opy_()
      bstack1l1l1ll11_opy_(bstack1llll11ll1_opy_, logger)
  except:
    pass
def bstack111l1ll11l_opy_():
  global bstack11l111l1l1_opy_
  global bstack1l1lll1ll_opy_
  global bstack11lll111l_opy_
  global bstack11l11l1l1_opy_
  global bstack1111lllll_opy_
  global bstack1l1ll11lll_opy_
  global CONFIG
  bstack1ll1l1ll1_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨௗ"))
  if bstack1ll1l1ll1_opy_ in [bstack11ll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ௘"), bstack11ll1l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨ௙")]:
    bstack1l1llll111_opy_()
  percy.shutdown()
  if bstack11l111l1l1_opy_:
    logger.warning(bstack11l111l11_opy_.format(str(bstack11l111l1l1_opy_)))
  else:
    try:
      bstack1111l1111l_opy_ = bstack1111l1ll1_opy_(bstack11ll1l_opy_ (u"ࠪ࠲ࡧࡹࡴࡢࡥ࡮࠱ࡨࡵ࡮ࡧ࡫ࡪ࠲࡯ࡹ࡯࡯ࠩ௚"), logger)
      if bstack1111l1111l_opy_.get(bstack11ll1l_opy_ (u"ࠫࡳࡻࡤࡨࡧࡢࡰࡴࡩࡡ࡭ࠩ௛")) and bstack1111l1111l_opy_.get(bstack11ll1l_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪ௜")).get(bstack11ll1l_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ௝")):
        logger.warning(bstack11l111l11_opy_.format(str(bstack1111l1111l_opy_[bstack11ll1l_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬ௞")][bstack11ll1l_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪ௟")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1l11l11111_opy_.invoke(Events.bstack111lll1l1_opy_)
  logger.info(bstack1l11111l11_opy_)
  global bstack11lll1ll1l_opy_
  if bstack11lll1ll1l_opy_:
    bstack1l1lll1l1_opy_()
  try:
    with bstack11llll1111_opy_:
      bstack1lll11111l_opy_ = bstack1l1lll1ll_opy_.copy()
    for driver in bstack1lll11111l_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1l1l111l1_opy_)
  if bstack1l1ll11lll_opy_ == bstack11ll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ௠"):
    bstack1111lllll_opy_ = bstack1111llll1l_opy_(bstack11ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫ௡"))
  if bstack1l1ll11lll_opy_ == bstack11ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ௢") and len(bstack11l11l1l1_opy_) == 0:
    bstack11l11l1l1_opy_ = bstack1111llll1l_opy_(bstack11ll1l_opy_ (u"ࠬࡶࡷࡠࡲࡼࡸࡪࡹࡴࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸ࠳ࡰࡳࡰࡰࠪ௣"))
    if len(bstack11l11l1l1_opy_) == 0:
      bstack11l11l1l1_opy_ = bstack1111llll1l_opy_(bstack11ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹࡥࡰࡱࡲࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ௤"))
  bstack11l1lllll_opy_ = bstack11ll1l_opy_ (u"ࠧࠨ௥")
  if len(bstack11lll111l_opy_) > 0:
    bstack11l1lllll_opy_ = bstack11l1lll1l_opy_(bstack11lll111l_opy_)
  elif len(bstack11l11l1l1_opy_) > 0:
    bstack11l1lllll_opy_ = bstack11l1lll1l_opy_(bstack11l11l1l1_opy_)
  elif len(bstack1111lllll_opy_) > 0:
    bstack11l1lllll_opy_ = bstack11l1lll1l_opy_(bstack1111lllll_opy_)
  elif len(bstack11lll1111l_opy_) > 0:
    bstack11l1lllll_opy_ = bstack11l1lll1l_opy_(bstack11lll1111l_opy_)
  if bool(bstack11l1lllll_opy_):
    bstack1111ll1lll_opy_(bstack11l1lllll_opy_)
  else:
    bstack1111ll1lll_opy_()
  bstack1l1l1ll11_opy_(bstack1111111ll1_opy_, logger)
  if bstack1ll1l1ll1_opy_ not in [bstack11ll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩ௦")]:
    bstack1111lllll1_opy_()
  bstack1l11111111_opy_.bstack1lll1ll1_opy_(CONFIG)
  if len(bstack1111lllll_opy_) > 0:
    sys.exit(len(bstack1111lllll_opy_))
def bstack11lllll11l_opy_(bstack111llll1ll_opy_, frame):
  global bstack111ll1l1_opy_
  logger.error(bstack11l1l1lll1_opy_)
  bstack111ll1l1_opy_.set_property(bstack11ll1l_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡑࡳࠬ௧"), bstack111llll1ll_opy_)
  if hasattr(signal, bstack11ll1l_opy_ (u"ࠪࡗ࡮࡭࡮ࡢ࡮ࡶࠫ௨")):
    bstack111ll1l1_opy_.set_property(bstack11ll1l_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ௩"), signal.Signals(bstack111llll1ll_opy_).name)
  else:
    bstack111ll1l1_opy_.set_property(bstack11ll1l_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ௪"), bstack11ll1l_opy_ (u"࠭ࡓࡊࡉࡘࡒࡐࡔࡏࡘࡐࠪ௫"))
  if cli.is_running():
    bstack1l11l11111_opy_.invoke(Events.bstack111lll1l1_opy_)
  bstack1ll1l1ll1_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠧࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࡢ࡙ࡘࡋࡄࠨ௬"))
  if bstack1ll1l1ll1_opy_ == bstack11ll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ௭") and not cli.is_enabled(CONFIG):
    bstack1l1l1lll_opy_.stop(bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩ௮")))
  bstack111l1ll11l_opy_()
  sys.exit(1)
def bstack1l111llll_opy_(err):
  logger.critical(bstack1l111l1l11_opy_.format(str(err)))
  bstack1111ll1lll_opy_(bstack1l111l1l11_opy_.format(str(err)), True)
  atexit.unregister(bstack111l1ll11l_opy_)
  bstack1l1llll111_opy_()
  sys.exit(1)
def bstack1l11ll1111_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1111ll1lll_opy_(message, True)
  atexit.unregister(bstack111l1ll11l_opy_)
  bstack1l1llll111_opy_()
  sys.exit(1)
def bstack1l11l111ll_opy_():
  global CONFIG
  global bstack1ll1l1ll11_opy_
  global bstack11ll1l11ll_opy_
  global bstack11lllll111_opy_
  CONFIG = bstack1l111l1l1_opy_()
  load_dotenv(CONFIG.get(bstack11ll1l_opy_ (u"ࠪࡩࡳࡼࡆࡪ࡮ࡨࠫ௯")))
  bstack1l11111l1_opy_()
  bstack1ll111l1l_opy_()
  CONFIG = bstack1ll1111ll1_opy_(CONFIG)
  update(CONFIG, bstack11ll1l11ll_opy_)
  update(CONFIG, bstack1ll1l1ll11_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack1l1l11lll_opy_(CONFIG)
  bstack11lllll111_opy_ = bstack11ll1l1l1_opy_(CONFIG)
  os.environ[bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧ௰")] = bstack11lllll111_opy_.__str__().lower()
  bstack111ll1l1_opy_.set_property(bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭௱"), bstack11lllll111_opy_)
  if (bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௲") in CONFIG and bstack11ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ௳") in bstack1ll1l1ll11_opy_) or (
          bstack11ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௴") in CONFIG and bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௵") not in bstack11ll1l11ll_opy_):
    if os.getenv(bstack11ll1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡢࡇࡔࡓࡂࡊࡐࡈࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊࠧ௶")):
      CONFIG[bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௷")] = os.getenv(bstack11ll1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ௸"))
    else:
      if not CONFIG.get(bstack11ll1l_opy_ (u"ࠨࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠤ௹"), bstack11ll1l_opy_ (u"ࠢࠣ௺")) in bstack11ll11111l_opy_:
        bstack1l1l1ll1l1_opy_()
  elif (bstack11ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௻") not in CONFIG and bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ௼") in CONFIG) or (
          bstack11ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௽") in bstack11ll1l11ll_opy_ and bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௾") not in bstack1ll1l1ll11_opy_):
    del (CONFIG[bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ௿")])
  if bstack11l11ll11l_opy_(CONFIG):
    bstack1l111llll_opy_(bstack1111l1l11l_opy_)
  Config.bstack111111ll_opy_().set_property(bstack11ll1l_opy_ (u"ࠨࡵࡴࡧࡵࡒࡦࡳࡥࠣఀ"), CONFIG[bstack11ll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩఁ")])
  bstack1l11l11ll_opy_()
  bstack111l1lllll_opy_()
  if bstack11ll11l111_opy_ and not CONFIG.get(bstack11ll1l_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠦం"), bstack11ll1l_opy_ (u"ࠤࠥః")) in bstack11ll11111l_opy_:
    CONFIG[bstack11ll1l_opy_ (u"ࠪࡥࡵࡶࠧఄ")] = bstack111l11l11l_opy_(CONFIG)
    logger.info(bstack11l1111l1l_opy_.format(CONFIG[bstack11ll1l_opy_ (u"ࠫࡦࡶࡰࠨఅ")]))
  if not bstack11lllll111_opy_:
    CONFIG[bstack11ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఆ")] = [{}]
def bstack11lll1ll11_opy_(config, bstack1l1lll11ll_opy_):
  global CONFIG
  global bstack11ll11l111_opy_
  CONFIG = config
  bstack11ll11l111_opy_ = bstack1l1lll11ll_opy_
def bstack111l1lllll_opy_():
  global CONFIG
  global bstack11ll11l111_opy_
  if bstack11ll1l_opy_ (u"࠭ࡡࡱࡲࠪఇ") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l11ll1111_opy_(e, bstack111llll1l_opy_)
    bstack11ll11l111_opy_ = True
    bstack111ll1l1_opy_.set_property(bstack11ll1l_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ఈ"), True)
def bstack111l11l11l_opy_(config):
  bstack1l1111111_opy_ = bstack11ll1l_opy_ (u"ࠨࠩఉ")
  app = config[bstack11ll1l_opy_ (u"ࠩࡤࡴࡵ࠭ఊ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1l1l1l11l1_opy_:
      if os.path.exists(app):
        bstack1l1111111_opy_ = bstack1l1l1lllll_opy_(config, app)
      elif bstack1111ll1ll1_opy_(app):
        bstack1l1111111_opy_ = app
      else:
        bstack1l111llll_opy_(bstack1l1111111l_opy_.format(app))
    else:
      if bstack1111ll1ll1_opy_(app):
        bstack1l1111111_opy_ = app
      elif os.path.exists(app):
        bstack1l1111111_opy_ = bstack1l1l1lllll_opy_(app)
      else:
        bstack1l111llll_opy_(bstack11lll1111_opy_)
  else:
    if len(app) > 2:
      bstack1l111llll_opy_(bstack111ll11l11_opy_)
    elif len(app) == 2:
      if bstack11ll1l_opy_ (u"ࠪࡴࡦࡺࡨࠨఋ") in app and bstack11ll1l_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧఌ") in app:
        if os.path.exists(app[bstack11ll1l_opy_ (u"ࠬࡶࡡࡵࡪࠪ఍")]):
          bstack1l1111111_opy_ = bstack1l1l1lllll_opy_(config, app[bstack11ll1l_opy_ (u"࠭ࡰࡢࡶ࡫ࠫఎ")], app[bstack11ll1l_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳ࡟ࡪࡦࠪఏ")])
        else:
          bstack1l111llll_opy_(bstack1l1111111l_opy_.format(app))
      else:
        bstack1l111llll_opy_(bstack111ll11l11_opy_)
    else:
      for key in app:
        if key in bstack1l1l1l1111_opy_:
          if key == bstack11ll1l_opy_ (u"ࠨࡲࡤࡸ࡭࠭ఐ"):
            if os.path.exists(app[key]):
              bstack1l1111111_opy_ = bstack1l1l1lllll_opy_(config, app[key])
            else:
              bstack1l111llll_opy_(bstack1l1111111l_opy_.format(app))
          else:
            bstack1l1111111_opy_ = app[key]
        else:
          bstack1l111llll_opy_(bstack1ll1l111l1_opy_)
  return bstack1l1111111_opy_
def bstack1111ll1ll1_opy_(bstack1l1111111_opy_):
  import re
  bstack1l11ll11l_opy_ = re.compile(bstack11ll1l_opy_ (u"ࡴࠥࡢࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪࠥࠤ఑"))
  bstack11l111l1l_opy_ = re.compile(bstack11ll1l_opy_ (u"ࡵࠦࡣࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫ࠱࡞ࡥ࠲ࢀࡁ࠮࡜࠳࠱࠾ࡢ࡟࠯࡞࠰ࡡ࠯ࠪࠢఒ"))
  if bstack11ll1l_opy_ (u"ࠫࡧࡹ࠺࠰࠱ࠪఓ") in bstack1l1111111_opy_ or re.fullmatch(bstack1l11ll11l_opy_, bstack1l1111111_opy_) or re.fullmatch(bstack11l111l1l_opy_, bstack1l1111111_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack1llllll111_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack1l1l1lllll_opy_(config, path, bstack1l1ll11l11_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11ll1l_opy_ (u"ࠬࡸࡢࠨఔ")).read()).hexdigest()
  bstack1lll1lllll_opy_ = bstack11l1l1l1l1_opy_(md5_hash)
  bstack1l1111111_opy_ = None
  if bstack1lll1lllll_opy_:
    logger.info(bstack1l1111llll_opy_.format(bstack1lll1lllll_opy_, md5_hash))
    return bstack1lll1lllll_opy_
  bstack1ll11ll111_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack11ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࠫక"): (os.path.basename(path), open(os.path.abspath(path), bstack11ll1l_opy_ (u"ࠧࡳࡤࠪఖ")), bstack11ll1l_opy_ (u"ࠨࡶࡨࡼࡹ࠵ࡰ࡭ࡣ࡬ࡲࠬగ")),
      bstack11ll1l_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬఘ"): bstack1l1ll11l11_opy_
    }
  )
  response = requests.post(bstack1lll111111_opy_, data=multipart_data,
                           headers={bstack11ll1l_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩఙ"): multipart_data.content_type},
                           auth=(config[bstack11ll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭చ")], config[bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨఛ")]))
  try:
    res = json.loads(response.text)
    bstack1l1111111_opy_ = res[bstack11ll1l_opy_ (u"࠭ࡡࡱࡲࡢࡹࡷࡲࠧజ")]
    logger.info(bstack1l1ll1lll_opy_.format(bstack1l1111111_opy_))
    bstack1l1ll1l1l_opy_(md5_hash, bstack1l1111111_opy_)
    cli.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠢࡩࡶࡷࡴ࠿ࡻࡰ࡭ࡱࡤࡨࡤࡧࡰࡱࠤఝ"), datetime.datetime.now() - bstack1ll11ll111_opy_)
  except ValueError as err:
    bstack1l111llll_opy_(bstack111llll11l_opy_.format(str(err)))
  return bstack1l1111111_opy_
def bstack1l11l11ll_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1l11lll1l_opy_
  bstack1ll1lll1l_opy_ = 1
  bstack1l1lll11l1_opy_ = 1
  if bstack11ll1l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨఞ") in CONFIG:
    bstack1l1lll11l1_opy_ = CONFIG[bstack11ll1l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩట")]
  else:
    bstack1l1lll11l1_opy_ = bstack11l1111111_opy_(framework_name, args) or 1
  if bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ఠ") in CONFIG:
    bstack1ll1lll1l_opy_ = len(CONFIG[bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧడ")])
  bstack1l11lll1l_opy_ = int(bstack1l1lll11l1_opy_) * int(bstack1ll1lll1l_opy_)
def bstack11l1111111_opy_(framework_name, args):
  if framework_name == bstack11llll11l1_opy_ and args and bstack11ll1l_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪఢ") in args:
      bstack1l1lll1l1l_opy_ = args.index(bstack11ll1l_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫణ"))
      return int(args[bstack1l1lll1l1l_opy_ + 1]) or 1
  return 1
def bstack11l1l1l1l1_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠢࡱࡳࡹࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡥࡥࡸ࡯ࡣࠡࡨ࡬ࡰࡪࠦ࡯ࡱࡧࡵࡥࡹ࡯࡯࡯ࡵࠪత"))
    bstack11111ll1l1_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠨࢀࠪథ")), bstack11ll1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩద"), bstack11ll1l_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫధ"))
    if os.path.exists(bstack11111ll1l1_opy_):
      try:
        bstack1l11lll111_opy_ = json.load(open(bstack11111ll1l1_opy_, bstack11ll1l_opy_ (u"ࠫࡷࡨࠧన")))
        if md5_hash in bstack1l11lll111_opy_:
          bstack111ll11ll_opy_ = bstack1l11lll111_opy_[md5_hash]
          bstack1l11l1l1l_opy_ = datetime.datetime.now()
          bstack11l1l11ll1_opy_ = datetime.datetime.strptime(bstack111ll11ll_opy_[bstack11ll1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨ఩")], bstack11ll1l_opy_ (u"࠭ࠥࡥ࠱ࠨࡱ࠴࡙ࠫࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪప"))
          if (bstack1l11l1l1l_opy_ - bstack11l1l11ll1_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack111ll11ll_opy_[bstack11ll1l_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬఫ")]):
            return None
          return bstack111ll11ll_opy_[bstack11ll1l_opy_ (u"ࠨ࡫ࡧࠫబ")]
      except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡐࡈ࠺ࠦࡨࡢࡵ࡫ࠤ࡫࡯࡬ࡦ࠼ࠣࡿࢂ࠭భ").format(str(e)))
    return None
  bstack11111ll1l1_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠪࢂࠬమ")), bstack11ll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫయ"), bstack11ll1l_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ర"))
  lock_file = bstack11111ll1l1_opy_ + bstack11ll1l_opy_ (u"࠭࠮࡭ࡱࡦ࡯ࠬఱ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack11111ll1l1_opy_):
        with open(bstack11111ll1l1_opy_, bstack11ll1l_opy_ (u"ࠧࡳࠩల")) as f:
          content = f.read().strip()
          if content:
            bstack1l11lll111_opy_ = json.loads(content)
            if md5_hash in bstack1l11lll111_opy_:
              bstack111ll11ll_opy_ = bstack1l11lll111_opy_[md5_hash]
              bstack1l11l1l1l_opy_ = datetime.datetime.now()
              bstack11l1l11ll1_opy_ = datetime.datetime.strptime(bstack111ll11ll_opy_[bstack11ll1l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫళ")], bstack11ll1l_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ఴ"))
              if (bstack1l11l1l1l_opy_ - bstack11l1l11ll1_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack111ll11ll_opy_[bstack11ll1l_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨవ")]):
                return None
              return bstack111ll11ll_opy_[bstack11ll1l_opy_ (u"ࠫ࡮ࡪࠧశ")]
      return None
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡼ࡯ࡴࡩࠢࡩ࡭ࡱ࡫ࠠ࡭ࡱࡦ࡯࡮ࡴࡧࠡࡨࡲࡶࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮࠺ࠡࡽࢀࠫష").format(str(e)))
    return None
def bstack1l1ll1l1l_opy_(md5_hash, bstack1l1111111_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡰࡴࡩ࡫ࠡࡰࡲࡸࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡤࡤࡷ࡮ࡩࠠࡧ࡫࡯ࡩࠥࡵࡰࡦࡴࡤࡸ࡮ࡵ࡮ࡴࠩస"))
    bstack11lllll1l1_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠧࡿࠩహ")), bstack11ll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ఺"))
    if not os.path.exists(bstack11lllll1l1_opy_):
      os.makedirs(bstack11lllll1l1_opy_)
    bstack11111ll1l1_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠩࢁࠫ఻")), bstack11ll1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭఼ࠪ"), bstack11ll1l_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬఽ"))
    bstack1ll11l111l_opy_ = {
      bstack11ll1l_opy_ (u"ࠬ࡯ࡤࠨా"): bstack1l1111111_opy_,
      bstack11ll1l_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩి"): datetime.datetime.strftime(datetime.datetime.now(), bstack11ll1l_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫీ")),
      bstack11ll1l_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ు"): str(__version__)
    }
    try:
      bstack1l11lll111_opy_ = {}
      if os.path.exists(bstack11111ll1l1_opy_):
        bstack1l11lll111_opy_ = json.load(open(bstack11111ll1l1_opy_, bstack11ll1l_opy_ (u"ࠩࡵࡦࠬూ")))
      bstack1l11lll111_opy_[md5_hash] = bstack1ll11l111l_opy_
      with open(bstack11111ll1l1_opy_, bstack11ll1l_opy_ (u"ࠥࡻ࠰ࠨృ")) as outfile:
        json.dump(bstack1l11lll111_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡹࡵࡪࡡࡵ࡫ࡱ࡫ࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮ࠠࡧ࡫࡯ࡩ࠿ࠦࡻࡾࠩౄ").format(str(e)))
    return
  bstack11lllll1l1_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠬࢄࠧ౅")), bstack11ll1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ె"))
  if not os.path.exists(bstack11lllll1l1_opy_):
    os.makedirs(bstack11lllll1l1_opy_)
  bstack11111ll1l1_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠧࡿࠩే")), bstack11ll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨై"), bstack11ll1l_opy_ (u"ࠩࡤࡴࡵ࡛ࡰ࡭ࡱࡤࡨࡒࡊ࠵ࡉࡣࡶ࡬࠳ࡰࡳࡰࡰࠪ౉"))
  lock_file = bstack11111ll1l1_opy_ + bstack11ll1l_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩొ")
  bstack1ll11l111l_opy_ = {
    bstack11ll1l_opy_ (u"ࠫ࡮ࡪࠧో"): bstack1l1111111_opy_,
    bstack11ll1l_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨౌ"): datetime.datetime.strftime(datetime.datetime.now(), bstack11ll1l_opy_ (u"࠭ࠥࡥ࠱ࠨࡱ࠴࡙ࠫࠡࠧࡋ࠾ࠪࡓ࠺ࠦࡕ్ࠪ")),
    bstack11ll1l_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ౎"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1l11lll111_opy_ = {}
      if os.path.exists(bstack11111ll1l1_opy_):
        with open(bstack11111ll1l1_opy_, bstack11ll1l_opy_ (u"ࠨࡴࠪ౏")) as f:
          content = f.read().strip()
          if content:
            bstack1l11lll111_opy_ = json.loads(content)
      bstack1l11lll111_opy_[md5_hash] = bstack1ll11l111l_opy_
      with open(bstack11111ll1l1_opy_, bstack11ll1l_opy_ (u"ࠤࡺࠦ౐")) as outfile:
        json.dump(bstack1l11lll111_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡺ࡭ࡹ࡮ࠠࡧ࡫࡯ࡩࠥࡲ࡯ࡤ࡭࡬ࡲ࡬ࠦࡦࡰࡴࠣࡑࡉ࠻ࠠࡩࡣࡶ࡬ࠥࡻࡰࡥࡣࡷࡩ࠿ࠦࡻࡾࠩ౑").format(str(e)))
def bstack1ll11ll11l_opy_(self):
  return
def bstack111l111lll_opy_(self):
  return
def bstack1l1111l11l_opy_():
  global bstack11ll1l1ll_opy_
  bstack11ll1l1ll_opy_ = True
@measure(event_name=EVENTS.bstack11lll1l1ll_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack11111l1l1_opy_(self):
  global bstack1l111lll1l_opy_
  global bstack1ll11l1l1_opy_
  global bstack1l111l1l1l_opy_
  try:
    if bstack11ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ౒") in bstack1l111lll1l_opy_ and self.session_id != None and bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡖࡸࡦࡺࡵࡴࠩ౓"), bstack11ll1l_opy_ (u"࠭ࠧ౔")) != bstack11ll1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨౕ"):
      bstack11l1lll11l_opy_ = bstack11ll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨౖ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ౗")
      if bstack11l1lll11l_opy_ == bstack11ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪౘ"):
        bstack1l1lll1111_opy_(logger)
      if self != None:
        bstack1l11ll11l1_opy_(self, bstack11l1lll11l_opy_, bstack11ll1l_opy_ (u"ࠫ࠱ࠦࠧౙ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11ll1l_opy_ (u"ࠬ࠭ౚ")
    if bstack11ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭౛") in bstack1l111lll1l_opy_ and getattr(threading.current_thread(), bstack11ll1l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭౜"), None):
      bstack1111llll_opy_.bstack111l1l1l_opy_(self, bstack1lll11l1ll_opy_, logger, wait=True)
    if bstack11ll1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨౝ") in bstack1l111lll1l_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1l11ll11l1_opy_(self, bstack11ll1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ౞"))
      bstack1l1l11ll11_opy_.bstack1ll11lllll_opy_(self)
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࠦ౟") + str(e))
  bstack1l111l1l1l_opy_(self)
  self.session_id = None
def bstack11l1111ll1_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack111l1l1111_opy_
    global bstack1l111lll1l_opy_
    command_executor = kwargs.get(bstack11ll1l_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡤ࡫ࡸࡦࡥࡸࡸࡴࡸࠧౠ"), bstack11ll1l_opy_ (u"ࠬ࠭ౡ"))
    bstack1l1ll1l1l1_opy_ = False
    if type(command_executor) == str and bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩౢ") in command_executor:
      bstack1l1ll1l1l1_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪౣ") in str(getattr(command_executor, bstack11ll1l_opy_ (u"ࠨࡡࡸࡶࡱ࠭౤"), bstack11ll1l_opy_ (u"ࠩࠪ౥"))):
      bstack1l1ll1l1l1_opy_ = True
    else:
      kwargs = bstack1lllll1l1_opy_.bstack1llll1l11l_opy_(bstack11lll1ll1_opy_=kwargs, config=CONFIG)
      return bstack111l111ll1_opy_(self, *args, **kwargs)
    if bstack1l1ll1l1l1_opy_:
      bstack11111ll1ll_opy_ = bstack1llll11l1l_opy_.bstack11111ll11l_opy_(CONFIG, bstack1l111lll1l_opy_)
      if kwargs.get(bstack11ll1l_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ౦")):
        kwargs[bstack11ll1l_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ౧")] = bstack111l1l1111_opy_(kwargs[bstack11ll1l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭౨")], bstack1l111lll1l_opy_, CONFIG, bstack11111ll1ll_opy_)
      elif kwargs.get(bstack11ll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭౩")):
        kwargs[bstack11ll1l_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ౪")] = bstack111l1l1111_opy_(kwargs[bstack11ll1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ౫")], bstack1l111lll1l_opy_, CONFIG, bstack11111ll1ll_opy_)
  except Exception as e:
    logger.error(bstack11ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫ࡩࡳࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣࡗࡉࡑࠠࡤࡣࡳࡷ࠿ࠦࡻࡾࠤ౬").format(str(e)))
  return bstack111l111ll1_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l111ll11_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack11ll1111l_opy_(self, command_executor=bstack11ll1l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲࠵࠷࠽࠮࠱࠰࠳࠲࠶ࡀ࠴࠵࠶࠷ࠦ౭"), *args, **kwargs):
  global bstack1ll11l1l1_opy_
  global bstack1l1lll1ll_opy_
  bstack111lllll1l_opy_ = bstack11l1111ll1_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1ll1llll_opy_.on():
    return bstack111lllll1l_opy_
  try:
    logger.debug(bstack11ll1l_opy_ (u"ࠫࡈࡵ࡭࡮ࡣࡱࡨࠥࡋࡸࡦࡥࡸࡸࡴࡸࠠࡸࡪࡨࡲࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡ࡫ࡶࠤ࡫ࡧ࡬ࡴࡧࠣ࠱ࠥࢁࡽࠨ౮").format(str(command_executor)))
    logger.debug(bstack11ll1l_opy_ (u"ࠬࡎࡵࡣࠢࡘࡖࡑࠦࡩࡴࠢ࠰ࠤࢀࢃࠧ౯").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩ౰") in command_executor._url:
      bstack111ll1l1_opy_.set_property(bstack11ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨ౱"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ౲") in command_executor):
    bstack111ll1l1_opy_.set_property(bstack11ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ౳"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack11l11l111_opy_ = getattr(threading.current_thread(), bstack11ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫ౴"), None)
  bstack11ll1ll1l1_opy_ = {}
  if self.capabilities is not None:
    bstack11ll1ll1l1_opy_[bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪ౵")] = self.capabilities.get(bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ౶"))
    bstack11ll1ll1l1_opy_[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ౷")] = self.capabilities.get(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ౸"))
    bstack11ll1ll1l1_opy_[bstack11ll1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡠࡱࡳࡸ࡮ࡵ࡮ࡴࠩ౹")] = self.capabilities.get(bstack11ll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ౺"))
  if CONFIG.get(bstack11ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ౻"), False) and bstack1lllll1l1_opy_.bstack1l11111l1l_opy_(bstack11ll1ll1l1_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack11ll1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ౼") in bstack1l111lll1l_opy_ or bstack11ll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ౽") in bstack1l111lll1l_opy_:
    bstack1l1l1lll_opy_.bstack11ll11l11l_opy_(self)
  if bstack11ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭౾") in bstack1l111lll1l_opy_ and bstack11l11l111_opy_ and bstack11l11l111_opy_.get(bstack11ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ౿"), bstack11ll1l_opy_ (u"ࠨࠩಀ")) == bstack11ll1l_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪಁ"):
    bstack1l1l1lll_opy_.bstack11ll11l11l_opy_(self)
  bstack1ll11l1l1_opy_ = self.session_id
  with bstack11llll1111_opy_:
    bstack1l1lll1ll_opy_.append(self)
  return bstack111lllll1l_opy_
def bstack1llll1llll_opy_(args):
  return bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵࠫಂ") in str(args)
def bstack1ll11l11l1_opy_(self, driver_command, *args, **kwargs):
  global bstack111l1l1l1_opy_
  global bstack111l1l1l11_opy_
  bstack1l1l1l1l1_opy_ = bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨಃ"), None) and bstack1lllll11_opy_(
          threading.current_thread(), bstack11ll1l_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ಄"), None)
  bstack11l11ll111_opy_ = bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ಅ"), None) and bstack1lllll11_opy_(
          threading.current_thread(), bstack11ll1l_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩಆ"), None)
  bstack1lll1l1lll_opy_ = getattr(self, bstack11ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨಇ"), None) != None and getattr(self, bstack11ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩಈ"), None) == True
  if not bstack111l1l1l11_opy_ and bstack11ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪಉ") in CONFIG and CONFIG[bstack11ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫಊ")] == True and bstack1l1l111ll_opy_.bstack1111llllll_opy_(driver_command) and (bstack1lll1l1lll_opy_ or bstack1l1l1l1l1_opy_ or bstack11l11ll111_opy_) and not bstack1llll1llll_opy_(args):
    try:
      bstack111l1l1l11_opy_ = True
      logger.debug(bstack11ll1l_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࢀࢃࠧಋ").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11ll1l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡳࡩࡷ࡬࡯ࡳ࡯ࠣࡷࡨࡧ࡮ࠡࡽࢀࠫಌ").format(str(err)))
    bstack111l1l1l11_opy_ = False
  response = bstack111l1l1l1_opy_(self, driver_command, *args, **kwargs)
  if (bstack11ll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭಍") in str(bstack1l111lll1l_opy_).lower() or bstack11ll1l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨಎ") in str(bstack1l111lll1l_opy_).lower()) and bstack1ll1llll_opy_.on():
    try:
      if driver_command == bstack11ll1l_opy_ (u"ࠩࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹ࠭ಏ"):
        bstack1l1l1lll_opy_.bstack111l11lll1_opy_({
            bstack11ll1l_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩಐ"): response[bstack11ll1l_opy_ (u"ࠫࡻࡧ࡬ࡶࡧࠪ಑")],
            bstack11ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬಒ"): bstack1l1l1lll_opy_.current_test_uuid() if bstack1l1l1lll_opy_.current_test_uuid() else bstack1ll1llll_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack11llllll1_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack11ll11lll1_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1ll11l1l1_opy_
  global bstack1l111l1111_opy_
  global bstack1111ll1l1l_opy_
  global bstack1lll111l11_opy_
  global bstack1111l11l11_opy_
  global bstack1l111lll1l_opy_
  global bstack111l111ll1_opy_
  global bstack1l1lll1ll_opy_
  global bstack1l1ll11l1l_opy_
  global bstack1lll11l1ll_opy_
  if os.getenv(bstack11ll1l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫಓ")) is not None and bstack1lllll1l1_opy_.bstack111l1111l_opy_(CONFIG) is None:
    CONFIG[bstack11ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧಔ")] = True
  CONFIG[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪಕ")] = str(bstack1l111lll1l_opy_) + str(__version__)
  bstack1l1l111l1l_opy_ = os.environ[bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧಖ")]
  bstack11111ll1ll_opy_ = bstack1llll11l1l_opy_.bstack11111ll11l_opy_(CONFIG, bstack1l111lll1l_opy_)
  CONFIG[bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ಗ")] = bstack1l1l111l1l_opy_
  CONFIG[bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ಘ")] = bstack11111ll1ll_opy_
  if CONFIG.get(bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬಙ"),bstack11ll1l_opy_ (u"࠭ࠧಚ")) and bstack11ll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ಛ") in bstack1l111lll1l_opy_:
    CONFIG[bstack11ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨಜ")].pop(bstack11ll1l_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧಝ"), None)
    CONFIG[bstack11ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪಞ")].pop(bstack11ll1l_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩಟ"), None)
  command_executor = bstack1llll1lll1_opy_()
  logger.debug(bstack11lll11ll_opy_.format(command_executor))
  proxy = bstack1l111l1ll_opy_(CONFIG, proxy)
  bstack1l1llll1ll_opy_ = 0 if bstack1l111l1111_opy_ < 0 else bstack1l111l1111_opy_
  try:
    if bstack1lll111l11_opy_ is True:
      bstack1l1llll1ll_opy_ = int(multiprocessing.current_process().name)
    elif bstack1111l11l11_opy_ is True:
      bstack1l1llll1ll_opy_ = int(threading.current_thread().name)
  except:
    bstack1l1llll1ll_opy_ = 0
  bstack1l11ll1l1l_opy_ = bstack1ll11ll1l1_opy_(CONFIG, bstack1l1llll1ll_opy_)
  logger.debug(bstack11111lll1_opy_.format(str(bstack1l11ll1l1l_opy_)))
  if bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩಠ") in CONFIG and bstack1ll11lll11_opy_(CONFIG[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪಡ")]):
    bstack1l111l11ll_opy_(bstack1l11ll1l1l_opy_)
  if bstack1lllll1l1_opy_.bstack1111llll1_opy_(CONFIG, bstack1l1llll1ll_opy_) and bstack1lllll1l1_opy_.bstack1111l11l1_opy_(bstack1l11ll1l1l_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack1lllll1l1_opy_.set_capabilities(bstack1l11ll1l1l_opy_, CONFIG)
  if desired_capabilities:
    bstack1lllll1l1l_opy_ = bstack1ll1111ll1_opy_(desired_capabilities)
    bstack1lllll1l1l_opy_[bstack11ll1l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧಢ")] = bstack1ll1l111l_opy_(CONFIG)
    bstack11l1ll11l1_opy_ = bstack1ll11ll1l1_opy_(bstack1lllll1l1l_opy_)
    if bstack11l1ll11l1_opy_:
      bstack1l11ll1l1l_opy_ = update(bstack11l1ll11l1_opy_, bstack1l11ll1l1l_opy_)
    desired_capabilities = None
  if options:
    bstack111lll111_opy_(options, bstack1l11ll1l1l_opy_)
  if not options:
    options = bstack1ll11l11l_opy_(bstack1l11ll1l1l_opy_)
  bstack1lll11l1ll_opy_ = CONFIG.get(bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಣ"))[bstack1l1llll1ll_opy_]
  if proxy and bstack111llllll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩತ")):
    options.proxy(proxy)
  if options and bstack111llllll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩಥ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack111llllll_opy_() < version.parse(bstack11ll1l_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪದ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1l11ll1l1l_opy_)
  logger.info(bstack111l1ll1l1_opy_)
  bstack1ll1l1lll_opy_.end(EVENTS.bstack11111l1l11_opy_.value, EVENTS.bstack11111l1l11_opy_.value + bstack11ll1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧಧ"), EVENTS.bstack11111l1l11_opy_.value + bstack11ll1l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦನ"), status=True, failure=None, test_name=bstack1111ll1l1l_opy_)
  if bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡲࡵࡳ࡫࡯࡬ࡦࠩ಩") in kwargs:
    del kwargs[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡳࡶࡴ࡬ࡩ࡭ࡧࠪಪ")]
  try:
    if bstack111llllll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠩ࠷࠲࠶࠶࠮࠱ࠩಫ")):
      bstack111l111ll1_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack111llllll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠪ࠷࠳࠾࠮࠱ࠩಬ")):
      bstack111l111ll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack111llllll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠫ࠷࠴࠵࠴࠰࠳ࠫಭ")):
      bstack111l111ll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack111l111ll1_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack111ll11l1_opy_:
    logger.error(bstack1llll1l1ll_opy_.format(bstack11ll1l_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠫಮ"), str(bstack111ll11l1_opy_)))
    raise bstack111ll11l1_opy_
  if bstack1lllll1l1_opy_.bstack1111llll1_opy_(CONFIG, bstack1l1llll1ll_opy_) and bstack1lllll1l1_opy_.bstack1111l11l1_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨಯ")][bstack11ll1l_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ರ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack1lllll1l1_opy_.set_capabilities(bstack1l11ll1l1l_opy_, CONFIG)
  try:
    bstack11l111ll1l_opy_ = bstack11ll1l_opy_ (u"ࠨࠩಱ")
    if bstack111llllll_opy_() >= version.parse(bstack11ll1l_opy_ (u"ࠩ࠷࠲࠵࠴࠰ࡣ࠳ࠪಲ")):
      if self.caps is not None:
        bstack11l111ll1l_opy_ = self.caps.get(bstack11ll1l_opy_ (u"ࠥࡳࡵࡺࡩ࡮ࡣ࡯ࡌࡺࡨࡕࡳ࡮ࠥಳ"))
    else:
      if self.capabilities is not None:
        bstack11l111ll1l_opy_ = self.capabilities.get(bstack11ll1l_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦ಴"))
    if bstack11l111ll1l_opy_:
      bstack11l1ll1lll_opy_(bstack11l111ll1l_opy_)
      if bstack111llllll_opy_() <= version.parse(bstack11ll1l_opy_ (u"ࠬ࠹࠮࠲࠵࠱࠴ࠬವ")):
        self.command_executor._url = bstack11ll1l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢಶ") + bstack11llll11l_opy_ + bstack11ll1l_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦಷ")
      else:
        self.command_executor._url = bstack11ll1l_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥಸ") + bstack11l111ll1l_opy_ + bstack11ll1l_opy_ (u"ࠤ࠲ࡻࡩ࠵ࡨࡶࡤࠥಹ")
      logger.debug(bstack11l11ll1l1_opy_.format(bstack11l111ll1l_opy_))
    else:
      logger.debug(bstack1l11l11ll1_opy_.format(bstack11ll1l_opy_ (u"ࠥࡓࡵࡺࡩ࡮ࡣ࡯ࠤࡍࡻࡢࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠦ಺")))
  except Exception as e:
    logger.debug(bstack1l11l11ll1_opy_.format(e))
  if bstack11ll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ಻") in bstack1l111lll1l_opy_:
    bstack1l1111l111_opy_(bstack1l111l1111_opy_, bstack1l1ll11l1l_opy_)
  bstack1ll11l1l1_opy_ = self.session_id
  if bstack11ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ಼ࠬ") in bstack1l111lll1l_opy_ or bstack11ll1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ಽ") in bstack1l111lll1l_opy_ or bstack11ll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ಾ") in bstack1l111lll1l_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack11l11l111_opy_ = getattr(threading.current_thread(), bstack11ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡕࡧࡶࡸࡒ࡫ࡴࡢࠩಿ"), None)
  if bstack11ll1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩೀ") in bstack1l111lll1l_opy_ or bstack11ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩು") in bstack1l111lll1l_opy_:
    bstack1l1l1lll_opy_.bstack11ll11l11l_opy_(self)
  if bstack11ll1l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫೂ") in bstack1l111lll1l_opy_ and bstack11l11l111_opy_ and bstack11l11l111_opy_.get(bstack11ll1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬೃ"), bstack11ll1l_opy_ (u"࠭ࠧೄ")) == bstack11ll1l_opy_ (u"ࠧࡱࡧࡱࡨ࡮ࡴࡧࠨ೅"):
    bstack1l1l1lll_opy_.bstack11ll11l11l_opy_(self)
  with bstack11llll1111_opy_:
    bstack1l1lll1ll_opy_.append(self)
  if bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫೆ") in CONFIG and bstack11ll1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧೇ") in CONFIG[bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ೈ")][bstack1l1llll1ll_opy_]:
    bstack1111ll1l1l_opy_ = CONFIG[bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ೉")][bstack1l1llll1ll_opy_][bstack11ll1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪೊ")]
  logger.debug(bstack11l111111_opy_.format(bstack1ll11l1l1_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1ll1l1llll_opy_
    def bstack11ll11llll_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1l1l1ll111_opy_
      if(bstack11ll1l_opy_ (u"ࠨࡩ࡯ࡦࡨࡼ࠳ࡰࡳࠣೋ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠧࡿࠩೌ")), bstack11ll1l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ್"), bstack11ll1l_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ೎")), bstack11ll1l_opy_ (u"ࠪࡻࠬ೏")) as fp:
          fp.write(bstack11ll1l_opy_ (u"ࠦࠧ೐"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11ll1l_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢ೑")))):
          with open(args[1], bstack11ll1l_opy_ (u"࠭ࡲࠨ೒")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11ll1l_opy_ (u"ࠧࡢࡵࡼࡲࡨࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡡࡱࡩࡼࡖࡡࡨࡧࠫࡧࡴࡴࡴࡦࡺࡷ࠰ࠥࡶࡡࡨࡧࠣࡁࠥࡼ࡯ࡪࡦࠣ࠴࠮࠭೓") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1l1111lll_opy_)
            if bstack11ll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ೔") in CONFIG and str(CONFIG[bstack11ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ೕ")]).lower() != bstack11ll1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩೖ"):
                bstack11l1l11l11_opy_ = bstack1ll1l1llll_opy_()
                bstack11l1llll1l_opy_ = bstack11ll1l_opy_ (u"ࠫࠬ࠭ࠊ࠰ࠬࠣࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃࠠࠫ࠱ࠍࡧࡴࡴࡳࡵࠢࡥࡷࡹࡧࡣ࡬ࡡࡳࡥࡹ࡮ࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶ࡡࡀࠐࡣࡰࡰࡶࡸࠥࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠷࡝࠼ࠌࡦࡳࡳࡹࡴࠡࡲࡢ࡭ࡳࡪࡥࡹࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠷ࡣ࠻ࠋࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯ࡵ࡯࡭ࡨ࡫ࠨ࠱࠮ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸࠯࠻ࠋࡥࡲࡲࡸࡺࠠࡪ࡯ࡳࡳࡷࡺ࡟ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࠸ࡤࡨࡳࡵࡣࡦ࡯ࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨࠩ࠼ࠌ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰࡯ࡥࡺࡴࡣࡩࠢࡀࠤࡦࡹࡹ࡯ࡥࠣࠬࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶ࠭ࠥࡃ࠾ࠡࡽࡾࠎࠥࠦ࡬ࡦࡶࠣࡧࡦࡶࡳ࠼ࠌࠣࠤࡹࡸࡹࠡࡽࡾࠎࠥࠦࠠࠡࡥࡤࡴࡸࠦ࠽ࠡࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠬ࠿ࠏࠦࠠࡾࡿࠣࡧࡦࡺࡣࡩࠢࠫࡩࡽ࠯ࠠࡼࡽࠍࠤࠥࠦࠠࡤࡱࡱࡷࡴࡲࡥ࠯ࡧࡵࡶࡴࡸࠨࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵࡧࡲࡴࡧࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠼ࠥ࠰ࠥ࡫ࡸࠪ࠽ࠍࠤࠥࢃࡽࠋࠢࠣࡶࡪࡺࡵࡳࡰࠣࡥࡼࡧࡩࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰ࡦࡳࡳࡴࡥࡤࡶࠫࡿࢀࠐࠠࠡࠢࠣࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺ࠺ࠡࠩࡾࡧࡩࡶࡕࡳ࡮ࢀࠫࠥ࠱ࠠࡦࡰࡦࡳࡩ࡫ࡕࡓࡋࡆࡳࡲࡶ࡯࡯ࡧࡱࡸ࠭ࡐࡓࡐࡐ࠱ࡷࡹࡸࡩ࡯ࡩ࡬ࡪࡾ࠮ࡣࡢࡲࡶ࠭࠮࠲ࠊࠡࠢࠣࠤ࠳࠴࠮࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹࠊࠡࠢࢀࢁ࠮ࡁࠊࡾࡿ࠾ࠎ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵ࠊࠨࠩࠪ೗").format(bstack11l1l11l11_opy_=bstack11l1l11l11_opy_)
            lines.insert(1, bstack11l1llll1l_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11ll1l_opy_ (u"ࠧ࡯࡮ࡥࡧࡻࡣࡧࡹࡴࡢࡥ࡮࠲࡯ࡹࠢ೘")), bstack11ll1l_opy_ (u"࠭ࡷࠨ೙")) as bstack11l1llllll_opy_:
              bstack11l1llllll_opy_.writelines(lines)
        CONFIG[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࡙ࡄࡌࠩ೚")] = str(bstack1l111lll1l_opy_) + str(__version__)
        bstack1l1l111l1l_opy_ = os.environ[bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭೛")]
        bstack11111ll1ll_opy_ = bstack1llll11l1l_opy_.bstack11111ll11l_opy_(CONFIG, bstack1l111lll1l_opy_)
        CONFIG[bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺࡨࡶࡤࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬ೜")] = bstack1l1l111l1l_opy_
        CONFIG[bstack11ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬೝ")] = bstack11111ll1ll_opy_
        bstack1l1llll1ll_opy_ = 0 if bstack1l111l1111_opy_ < 0 else bstack1l111l1111_opy_
        try:
          if bstack1lll111l11_opy_ is True:
            bstack1l1llll1ll_opy_ = int(multiprocessing.current_process().name)
          elif bstack1111l11l11_opy_ is True:
            bstack1l1llll1ll_opy_ = int(threading.current_thread().name)
        except:
          bstack1l1llll1ll_opy_ = 0
        CONFIG[bstack11ll1l_opy_ (u"ࠦࡺࡹࡥࡘ࠵ࡆࠦೞ")] = False
        CONFIG[bstack11ll1l_opy_ (u"ࠧ࡯ࡳࡑ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ೟")] = True
        bstack1l11ll1l1l_opy_ = bstack1ll11ll1l1_opy_(CONFIG, bstack1l1llll1ll_opy_)
        logger.debug(bstack11111lll1_opy_.format(str(bstack1l11ll1l1l_opy_)))
        if CONFIG.get(bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪೠ")):
          bstack1l111l11ll_opy_(bstack1l11ll1l1l_opy_)
        if bstack11ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪೡ") in CONFIG and bstack11ll1l_opy_ (u"ࠨࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ೢ") in CONFIG[bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೣ")][bstack1l1llll1ll_opy_]:
          bstack1111ll1l1l_opy_ = CONFIG[bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭೤")][bstack1l1llll1ll_opy_][bstack11ll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ೥")]
        args.append(os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠬࢄࠧ೦")), bstack11ll1l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭೧"), bstack11ll1l_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩ೨")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1l11ll1l1l_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11ll1l_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࡟ࡣࡵࡷࡥࡨࡱ࠮࡫ࡵࠥ೩"))
      bstack1l1l1ll111_opy_ = True
      return bstack1l11l1l11l_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack11l1111lll_opy_(self,
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
    global bstack1l111l1111_opy_
    global bstack1111ll1l1l_opy_
    global bstack1lll111l11_opy_
    global bstack1111l11l11_opy_
    global bstack1l111lll1l_opy_
    CONFIG[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫ೪")] = str(bstack1l111lll1l_opy_) + str(__version__)
    bstack1l1l111l1l_opy_ = os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ೫")]
    bstack11111ll1ll_opy_ = bstack1llll11l1l_opy_.bstack11111ll11l_opy_(CONFIG, bstack1l111lll1l_opy_)
    CONFIG[bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧ೬")] = bstack1l1l111l1l_opy_
    CONFIG[bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧ೭")] = bstack11111ll1ll_opy_
    bstack1l1llll1ll_opy_ = 0 if bstack1l111l1111_opy_ < 0 else bstack1l111l1111_opy_
    try:
      if bstack1lll111l11_opy_ is True:
        bstack1l1llll1ll_opy_ = int(multiprocessing.current_process().name)
      elif bstack1111l11l11_opy_ is True:
        bstack1l1llll1ll_opy_ = int(threading.current_thread().name)
    except:
      bstack1l1llll1ll_opy_ = 0
    CONFIG[bstack11ll1l_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ೮")] = True
    bstack1l11ll1l1l_opy_ = bstack1ll11ll1l1_opy_(CONFIG, bstack1l1llll1ll_opy_)
    logger.debug(bstack11111lll1_opy_.format(str(bstack1l11ll1l1l_opy_)))
    if CONFIG.get(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ೯")):
      bstack1l111l11ll_opy_(bstack1l11ll1l1l_opy_)
    if bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ೰") in CONFIG and bstack11ll1l_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧೱ") in CONFIG[bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ೲ")][bstack1l1llll1ll_opy_]:
      bstack1111ll1l1l_opy_ = CONFIG[bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧೳ")][bstack1l1llll1ll_opy_][bstack11ll1l_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ೴")]
    import urllib
    import json
    if bstack11ll1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ೵") in CONFIG and str(CONFIG[bstack11ll1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ೶")]).lower() != bstack11ll1l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ೷"):
        bstack111llllll1_opy_ = bstack1ll1l1llll_opy_()
        bstack11l1l11l11_opy_ = bstack111llllll1_opy_ + urllib.parse.quote(json.dumps(bstack1l11ll1l1l_opy_))
    else:
        bstack11l1l11l11_opy_ = bstack11ll1l_opy_ (u"ࠩࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠫ೸") + urllib.parse.quote(json.dumps(bstack1l11ll1l1l_opy_))
    browser = self.connect(bstack11l1l11l11_opy_)
    return browser
except Exception as e:
    pass
def bstack11l1l11ll_opy_():
    global bstack1l1l1ll111_opy_
    global bstack1l111lll1l_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack111l11l1l_opy_
        global bstack111ll1l1_opy_
        if not bstack11lllll111_opy_:
          global bstack1llll111ll_opy_
          if not bstack1llll111ll_opy_:
            from bstack_utils.helper import bstack11l1ll1l11_opy_, bstack1111l111l_opy_, bstack111lll1ll_opy_
            bstack1llll111ll_opy_ = bstack11l1ll1l11_opy_()
            bstack1111l111l_opy_(bstack1l111lll1l_opy_)
            bstack11111ll1ll_opy_ = bstack1llll11l1l_opy_.bstack11111ll11l_opy_(CONFIG, bstack1l111lll1l_opy_)
            bstack111ll1l1_opy_.set_property(bstack11ll1l_opy_ (u"ࠥࡔࡑࡇ࡙ࡘࡔࡌࡋࡍ࡚࡟ࡑࡔࡒࡈ࡚ࡉࡔࡠࡏࡄࡔࠧ೹"), bstack11111ll1ll_opy_)
          BrowserType.connect = bstack111l11l1l_opy_
          return
        BrowserType.launch = bstack11l1111lll_opy_
        bstack1l1l1ll111_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack11ll11llll_opy_
      bstack1l1l1ll111_opy_ = True
    except Exception as e:
      pass
def bstack1l1l11llll_opy_(context, bstack1l1llll11l_opy_):
  try:
    context.page.evaluate(bstack11ll1l_opy_ (u"ࠦࡤࠦ࠽࠿ࠢࡾࢁࠧ೺"), bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠩ೻")+ json.dumps(bstack1l1llll11l_opy_) + bstack11ll1l_opy_ (u"ࠨࡽࡾࠤ೼"))
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦࠢࡾࢁ࠿ࠦࡻࡾࠤ೽").format(str(e), traceback.format_exc()))
def bstack1llll11111_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11ll1l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ೾"), bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ೿") + json.dumps(message) + bstack11ll1l_opy_ (u"ࠪ࠰ࠧࡲࡥࡷࡧ࡯ࠦ࠿࠭ഀ") + json.dumps(level) + bstack11ll1l_opy_ (u"ࠫࢂࢃࠧഁ"))
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠧ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠡࡣࡱࡲࡴࡺࡡࡵ࡫ࡲࡲࠥࢁࡽ࠻ࠢࡾࢁࠧം").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1l1l1l1ll_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack1ll1ll11l1_opy_(self, url):
  global bstack11ll1lll1_opy_
  try:
    bstack1l1l11l1l1_opy_(url)
  except Exception as err:
    logger.debug(bstack1l11l1lll1_opy_.format(str(err)))
  try:
    bstack11ll1lll1_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack1ll1lll11l_opy_):
        bstack1l1l11l1l1_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1l11l1lll1_opy_.format(str(err)))
    raise e
def bstack1l1llll1l1_opy_(self):
  global bstack1l111lllll_opy_
  bstack1l111lllll_opy_ = self
  return
def bstack111ll1l1l_opy_(self):
  global bstack11l11lll11_opy_
  bstack11l11lll11_opy_ = self
  return
def bstack111l11ll1_opy_(test_name, bstack11l1l1ll1l_opy_):
  global CONFIG
  if percy.bstack1l1l11111_opy_() == bstack11ll1l_opy_ (u"ࠨࡴࡳࡷࡨࠦഃ"):
    bstack1111111ll_opy_ = os.path.relpath(bstack11l1l1ll1l_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1111111ll_opy_)
    bstack11l111llll_opy_ = suite_name + bstack11ll1l_opy_ (u"ࠢ࠮ࠤഄ") + test_name
    threading.current_thread().percySessionName = bstack11l111llll_opy_
def bstack111l1l1ll1_opy_(self, test, *args, **kwargs):
  global bstack11ll11l11_opy_
  test_name = None
  bstack11l1l1ll1l_opy_ = None
  if test:
    test_name = str(test.name)
    bstack11l1l1ll1l_opy_ = str(test.source)
  bstack111l11ll1_opy_(test_name, bstack11l1l1ll1l_opy_)
  bstack11ll11l11_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1lll1111l1_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack1ll111lll1_opy_(driver, bstack11l111llll_opy_):
  if not bstack1lll1l1ll1_opy_ and bstack11l111llll_opy_:
      bstack1l1l11l11l_opy_ = {
          bstack11ll1l_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨഅ"): bstack11ll1l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪആ"),
          bstack11ll1l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ഇ"): {
              bstack11ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩഈ"): bstack11l111llll_opy_
          }
      }
      bstack1111111l1l_opy_ = bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪഉ").format(json.dumps(bstack1l1l11l11l_opy_))
      driver.execute_script(bstack1111111l1l_opy_)
  if bstack111l1l11l1_opy_:
      bstack11ll1l1l11_opy_ = {
          bstack11ll1l_opy_ (u"࠭ࡡࡤࡶ࡬ࡳࡳ࠭ഊ"): bstack11ll1l_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩഋ"),
          bstack11ll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫഌ"): {
              bstack11ll1l_opy_ (u"ࠩࡧࡥࡹࡧࠧ഍"): bstack11l111llll_opy_ + bstack11ll1l_opy_ (u"ࠪࠤࡵࡧࡳࡴࡧࡧࠥࠬഎ"),
              bstack11ll1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪഏ"): bstack11ll1l_opy_ (u"ࠬ࡯࡮ࡧࡱࠪഐ")
          }
      }
      if bstack111l1l11l1_opy_.status == bstack11ll1l_opy_ (u"࠭ࡐࡂࡕࡖࠫ഑"):
          bstack1111l11111_opy_ = bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬഒ").format(json.dumps(bstack11ll1l1l11_opy_))
          driver.execute_script(bstack1111l11111_opy_)
          bstack1l11ll11l1_opy_(driver, bstack11ll1l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨഓ"))
      elif bstack111l1l11l1_opy_.status == bstack11ll1l_opy_ (u"ࠩࡉࡅࡎࡒࠧഔ"):
          reason = bstack11ll1l_opy_ (u"ࠥࠦക")
          bstack11l111l11l_opy_ = bstack11l111llll_opy_ + bstack11ll1l_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠬഖ")
          if bstack111l1l11l1_opy_.message:
              reason = str(bstack111l1l11l1_opy_.message)
              bstack11l111l11l_opy_ = bstack11l111l11l_opy_ + bstack11ll1l_opy_ (u"ࠬࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴ࠽ࠤࠬഗ") + reason
          bstack11ll1l1l11_opy_[bstack11ll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩഘ")] = {
              bstack11ll1l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ങ"): bstack11ll1l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧച"),
              bstack11ll1l_opy_ (u"ࠩࡧࡥࡹࡧࠧഛ"): bstack11l111l11l_opy_
          }
          bstack1111l11111_opy_ = bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨജ").format(json.dumps(bstack11ll1l1l11_opy_))
          driver.execute_script(bstack1111l11111_opy_)
          bstack1l11ll11l1_opy_(driver, bstack11ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫഝ"), reason)
          bstack1l11111ll1_opy_(reason, str(bstack111l1l11l1_opy_), str(bstack1l111l1111_opy_), logger)
@measure(event_name=EVENTS.bstack111l11l1ll_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack1l11llllll_opy_(driver, test):
  if percy.bstack1l1l11111_opy_() == bstack11ll1l_opy_ (u"ࠧࡺࡲࡶࡧࠥഞ") and percy.bstack11l1l1111l_opy_() == bstack11ll1l_opy_ (u"ࠨࡴࡦࡵࡷࡧࡦࡹࡥࠣട"):
      bstack11ll1ll11l_opy_ = bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪഠ"), None)
      bstack1lll1l1111_opy_(driver, bstack11ll1ll11l_opy_, test)
  if (bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬഡ"), None) and
      bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨഢ"), None)) or (
      bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪണ"), None) and
      bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ത"), None)):
      logger.info(bstack11ll1l_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠣࡔࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡹ࡫ࡳࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡷࡱࡨࡪࡸࡷࡢࡻ࠱ࠤࠧഥ"))
      bstack1lllll1l1_opy_.bstack1lll111ll_opy_(driver, name=test.name, path=test.source)
def bstack11ll1l1ll1_opy_(test, bstack11l111llll_opy_):
    try:
      bstack1ll11ll111_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack11ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫദ")] = bstack11l111llll_opy_
      if bstack111l1l11l1_opy_:
        if bstack111l1l11l1_opy_.status == bstack11ll1l_opy_ (u"ࠧࡑࡃࡖࡗࠬധ"):
          data[bstack11ll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨന")] = bstack11ll1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩഩ")
        elif bstack111l1l11l1_opy_.status == bstack11ll1l_opy_ (u"ࠪࡊࡆࡏࡌࠨപ"):
          data[bstack11ll1l_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫഫ")] = bstack11ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬബ")
          if bstack111l1l11l1_opy_.message:
            data[bstack11ll1l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭ഭ")] = str(bstack111l1l11l1_opy_.message)
      user = CONFIG[bstack11ll1l_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩമ")]
      key = CONFIG[bstack11ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡌࡧࡼࠫയ")]
      host = bstack1lll1l11l1_opy_(cli.config, [bstack11ll1l_opy_ (u"ࠤࡤࡴ࡮ࡹࠢര"), bstack11ll1l_opy_ (u"ࠥࡥࡺࡺ࡯࡮ࡣࡷࡩࠧറ"), bstack11ll1l_opy_ (u"ࠦࡦࡶࡩࠣല")], bstack11ll1l_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡡࡱ࡫࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲࠨള"))
      url = bstack11ll1l_opy_ (u"࠭ࡻࡾ࠱ࡤࡹࡹࡵ࡭ࡢࡶࡨ࠳ࡸ࡫ࡳࡴ࡫ࡲࡲࡸ࠵ࡻࡾ࠰࡭ࡷࡴࡴࠧഴ").format(host, bstack1ll11l1l1_opy_)
      headers = {
        bstack11ll1l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡶࡼࡴࡪ࠭വ"): bstack11ll1l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫശ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡶࡲࡧࡥࡹ࡫࡟ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡵࡣࡷࡹࡸࠨഷ"), datetime.datetime.now() - bstack1ll11ll111_opy_)
    except Exception as e:
      logger.error(bstack1l1l11111l_opy_.format(str(e)))
def bstack1l1l1l1lll_opy_(test, bstack11l111llll_opy_):
  global CONFIG
  global bstack11l11lll11_opy_
  global bstack1l111lllll_opy_
  global bstack1ll11l1l1_opy_
  global bstack111l1l11l1_opy_
  global bstack1111ll1l1l_opy_
  global bstack1ll111ll1l_opy_
  global bstack11ll1l11l1_opy_
  global bstack11l1l11lll_opy_
  global bstack11l1ll1ll_opy_
  global bstack1l1lll1ll_opy_
  global bstack1lll11l1ll_opy_
  global bstack1llll11lll_opy_
  try:
    if not bstack1ll11l1l1_opy_:
      with bstack1llll11lll_opy_:
        bstack111l111ll_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"ࠪࢂࠬസ")), bstack11ll1l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫഹ"), bstack11ll1l_opy_ (u"ࠬ࠴ࡳࡦࡵࡶ࡭ࡴࡴࡩࡥࡵ࠱ࡸࡽࡺࠧഺ"))
        if os.path.exists(bstack111l111ll_opy_):
          with open(bstack111l111ll_opy_, bstack11ll1l_opy_ (u"࠭ࡲࠨ഻")) as f:
            content = f.read().strip()
            if content:
              bstack1ll111ll11_opy_ = json.loads(bstack11ll1l_opy_ (u"ࠢࡼࠤ഼") + content + bstack11ll1l_opy_ (u"ࠨࠤࡻࠦ࠿ࠦࠢࡺࠤࠪഽ") + bstack11ll1l_opy_ (u"ࠤࢀࠦാ"))
              bstack1ll11l1l1_opy_ = bstack1ll111ll11_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡎࡊࡳࠡࡨ࡬ࡰࡪࡀࠠࠨി") + str(e))
  if bstack1l1lll1ll_opy_:
    with bstack11llll1111_opy_:
      bstack111l11ll11_opy_ = bstack1l1lll1ll_opy_.copy()
    for driver in bstack111l11ll11_opy_:
      if bstack1ll11l1l1_opy_ == driver.session_id:
        if test:
          bstack1l11llllll_opy_(driver, test)
        bstack1ll111lll1_opy_(driver, bstack11l111llll_opy_)
  elif bstack1ll11l1l1_opy_:
    bstack11ll1l1ll1_opy_(test, bstack11l111llll_opy_)
  if bstack11l11lll11_opy_:
    bstack11ll1l11l1_opy_(bstack11l11lll11_opy_)
  if bstack1l111lllll_opy_:
    bstack11l1l11lll_opy_(bstack1l111lllll_opy_)
  if bstack11ll1l1ll_opy_:
    bstack11l1ll1ll_opy_()
def bstack11ll11l1ll_opy_(self, test, *args, **kwargs):
  bstack11l111llll_opy_ = None
  if test:
    bstack11l111llll_opy_ = str(test.name)
  bstack1l1l1l1lll_opy_(test, bstack11l111llll_opy_)
  bstack1ll111ll1l_opy_(self, test, *args, **kwargs)
def bstack1l11llll11_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack11l1l1111_opy_
  global CONFIG
  global bstack1l1lll1ll_opy_
  global bstack1ll11l1l1_opy_
  global bstack1llll11lll_opy_
  bstack111l1lll1_opy_ = None
  try:
    if bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪീ"), None) or bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧു"), None):
      try:
        if not bstack1ll11l1l1_opy_:
          bstack111l111ll_opy_ = os.path.join(os.path.expanduser(bstack11ll1l_opy_ (u"࠭ࡾࠨൂ")), bstack11ll1l_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧൃ"), bstack11ll1l_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪൄ"))
          with bstack1llll11lll_opy_:
            if os.path.exists(bstack111l111ll_opy_):
              with open(bstack111l111ll_opy_, bstack11ll1l_opy_ (u"ࠩࡵࠫ൅")) as f:
                content = f.read().strip()
                if content:
                  bstack1ll111ll11_opy_ = json.loads(bstack11ll1l_opy_ (u"ࠥࡿࠧെ") + content + bstack11ll1l_opy_ (u"ࠫࠧࡾࠢ࠻ࠢࠥࡽࠧ࠭േ") + bstack11ll1l_opy_ (u"ࠧࢃࠢൈ"))
                  bstack1ll11l1l1_opy_ = bstack1ll111ll11_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࡶࠤ࡫࡯࡬ࡦࠢ࡬ࡲࠥࡺࡥࡴࡶࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠬ൉") + str(e))
      if bstack1l1lll1ll_opy_:
        with bstack11llll1111_opy_:
          bstack111l11ll11_opy_ = bstack1l1lll1ll_opy_.copy()
        for driver in bstack111l11ll11_opy_:
          if bstack1ll11l1l1_opy_ == driver.session_id:
            bstack111l1lll1_opy_ = driver
    bstack1ll1ll111_opy_ = bstack1lllll1l1_opy_.bstack111l1ll11_opy_(test.tags)
    if bstack111l1lll1_opy_:
      threading.current_thread().isA11yTest = bstack1lllll1l1_opy_.bstack1l11llll1l_opy_(bstack111l1lll1_opy_, bstack1ll1ll111_opy_)
      threading.current_thread().isAppA11yTest = bstack1lllll1l1_opy_.bstack1l11llll1l_opy_(bstack111l1lll1_opy_, bstack1ll1ll111_opy_)
    else:
      threading.current_thread().isA11yTest = bstack1ll1ll111_opy_
      threading.current_thread().isAppA11yTest = bstack1ll1ll111_opy_
  except:
    pass
  bstack11l1l1111_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack111l1l11l1_opy_
  try:
    bstack111l1l11l1_opy_ = self._test
  except:
    bstack111l1l11l1_opy_ = self.test
def bstack1l111l111_opy_():
  global bstack1l1l11ll1_opy_
  try:
    if os.path.exists(bstack1l1l11ll1_opy_):
      os.remove(bstack1l1l11ll1_opy_)
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪൊ") + str(e))
def bstack111l11ll1l_opy_():
  global bstack1l1l11ll1_opy_
  bstack1111l1111l_opy_ = {}
  lock_file = bstack1l1l11ll1_opy_ + bstack11ll1l_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧോ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬൌ"))
    try:
      if not os.path.isfile(bstack1l1l11ll1_opy_):
        with open(bstack1l1l11ll1_opy_, bstack11ll1l_opy_ (u"ࠪࡻ്ࠬ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1l1l11ll1_opy_):
        with open(bstack1l1l11ll1_opy_, bstack11ll1l_opy_ (u"ࠫࡷ࠭ൎ")) as f:
          content = f.read().strip()
          if content:
            bstack1111l1111l_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack11ll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧ൏") + str(e))
    return bstack1111l1111l_opy_
  try:
    os.makedirs(os.path.dirname(bstack1l1l11ll1_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack1l1l11ll1_opy_):
        with open(bstack1l1l11ll1_opy_, bstack11ll1l_opy_ (u"࠭ࡷࠨ൐")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1l1l11ll1_opy_):
        with open(bstack1l1l11ll1_opy_, bstack11ll1l_opy_ (u"ࠧࡳࠩ൑")) as f:
          content = f.read().strip()
          if content:
            bstack1111l1111l_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡶࡪࡧࡤࡪࡰࡪࠤࡷࡵࡢࡰࡶࠣࡶࡪࡶ࡯ࡳࡶࠣࡪ࡮ࡲࡥ࠻ࠢࠪ൒") + str(e))
  finally:
    return bstack1111l1111l_opy_
def bstack1l1111l111_opy_(platform_index, item_index):
  global bstack1l1l11ll1_opy_
  lock_file = bstack1l1l11ll1_opy_ + bstack11ll1l_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨ൓")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ࠭ൔ"))
    try:
      bstack1111l1111l_opy_ = {}
      if os.path.exists(bstack1l1l11ll1_opy_):
        with open(bstack1l1l11ll1_opy_, bstack11ll1l_opy_ (u"ࠫࡷ࠭ൕ")) as f:
          content = f.read().strip()
          if content:
            bstack1111l1111l_opy_ = json.loads(content)
      bstack1111l1111l_opy_[item_index] = platform_index
      with open(bstack1l1l11ll1_opy_, bstack11ll1l_opy_ (u"ࠧࡽࠢൖ")) as outfile:
        json.dump(bstack1111l1111l_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11ll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡹࡵ࡭ࡹ࡯࡮ࡨࠢࡷࡳࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫൗ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack1l1l11ll1_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack1111l1111l_opy_ = {}
      if os.path.exists(bstack1l1l11ll1_opy_):
        with open(bstack1l1l11ll1_opy_, bstack11ll1l_opy_ (u"ࠧࡳࠩ൘")) as f:
          content = f.read().strip()
          if content:
            bstack1111l1111l_opy_ = json.loads(content)
      bstack1111l1111l_opy_[item_index] = platform_index
      with open(bstack1l1l11ll1_opy_, bstack11ll1l_opy_ (u"ࠣࡹࠥ൙")) as outfile:
        json.dump(bstack1111l1111l_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡼࡸࡩࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡴࡲࡦࡴࡺࠠࡳࡧࡳࡳࡷࡺࠠࡧ࡫࡯ࡩ࠿ࠦࠧ൚") + str(e))
def bstack1l1111l1l_opy_(bstack1llll1l1l1_opy_):
  global CONFIG
  bstack1l1ll111ll_opy_ = bstack11ll1l_opy_ (u"ࠪࠫ൛")
  if not bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ൜") in CONFIG:
    logger.info(bstack11ll1l_opy_ (u"ࠬࡔ࡯ࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠤࡵࡧࡳࡴࡧࡧࠤࡺࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡱࡩࡷࡧࡴࡦࠢࡵࡩࡵࡵࡲࡵࠢࡩࡳࡷࠦࡒࡰࡤࡲࡸࠥࡸࡵ࡯ࠩ൝"))
  try:
    platform = CONFIG[bstack11ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ൞")][bstack1llll1l1l1_opy_]
    if bstack11ll1l_opy_ (u"ࠧࡰࡵࠪൟ") in platform:
      bstack1l1ll111ll_opy_ += str(platform[bstack11ll1l_opy_ (u"ࠨࡱࡶࠫൠ")]) + bstack11ll1l_opy_ (u"ࠩ࠯ࠤࠬൡ")
    if bstack11ll1l_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ൢ") in platform:
      bstack1l1ll111ll_opy_ += str(platform[bstack11ll1l_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧൣ")]) + bstack11ll1l_opy_ (u"ࠬ࠲ࠠࠨ൤")
    if bstack11ll1l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪ൥") in platform:
      bstack1l1ll111ll_opy_ += str(platform[bstack11ll1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ൦")]) + bstack11ll1l_opy_ (u"ࠨ࠮ࠣࠫ൧")
    if bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠫ൨") in platform:
      bstack1l1ll111ll_opy_ += str(platform[bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ൩")]) + bstack11ll1l_opy_ (u"ࠫ࠱ࠦࠧ൪")
    if bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ൫") in platform:
      bstack1l1ll111ll_opy_ += str(platform[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ൬")]) + bstack11ll1l_opy_ (u"ࠧ࠭ࠢࠪ൭")
    if bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ൮") in platform:
      bstack1l1ll111ll_opy_ += str(platform[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ൯")]) + bstack11ll1l_opy_ (u"ࠪ࠰ࠥ࠭൰")
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠫࡘࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫࡮ࡦࡴࡤࡸ࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡷࡹࡸࡩ࡯ࡩࠣࡪࡴࡸࠠࡳࡧࡳࡳࡷࡺࠠࡨࡧࡱࡩࡷࡧࡴࡪࡱࡱࠫ൱") + str(e))
  finally:
    if bstack1l1ll111ll_opy_[len(bstack1l1ll111ll_opy_) - 2:] == bstack11ll1l_opy_ (u"ࠬ࠲ࠠࠨ൲"):
      bstack1l1ll111ll_opy_ = bstack1l1ll111ll_opy_[:-2]
    return bstack1l1ll111ll_opy_
def bstack111ll1lll_opy_(path, bstack1l1ll111ll_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1ll111l11l_opy_ = ET.parse(path)
    bstack11l11l1ll1_opy_ = bstack1ll111l11l_opy_.getroot()
    bstack11lll1l111_opy_ = None
    for suite in bstack11l11l1ll1_opy_.iter(bstack11ll1l_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൳")):
      if bstack11ll1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ൴") in suite.attrib:
        suite.attrib[bstack11ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭൵")] += bstack11ll1l_opy_ (u"ࠩࠣࠫ൶") + bstack1l1ll111ll_opy_
        bstack11lll1l111_opy_ = suite
    bstack1lllll11l1_opy_ = None
    for robot in bstack11l11l1ll1_opy_.iter(bstack11ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ൷")):
      bstack1lllll11l1_opy_ = robot
    bstack1l11ll1l11_opy_ = len(bstack1lllll11l1_opy_.findall(bstack11ll1l_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪ൸")))
    if bstack1l11ll1l11_opy_ == 1:
      bstack1lllll11l1_opy_.remove(bstack1lllll11l1_opy_.findall(bstack11ll1l_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫ൹"))[0])
      bstack1111ll1111_opy_ = ET.Element(bstack11ll1l_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬൺ"), attrib={bstack11ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬൻ"): bstack11ll1l_opy_ (u"ࠨࡕࡸ࡭ࡹ࡫ࡳࠨർ"), bstack11ll1l_opy_ (u"ࠩ࡬ࡨࠬൽ"): bstack11ll1l_opy_ (u"ࠪࡷ࠵࠭ൾ")})
      bstack1lllll11l1_opy_.insert(1, bstack1111ll1111_opy_)
      bstack1l1l1ll11l_opy_ = None
      for suite in bstack1lllll11l1_opy_.iter(bstack11ll1l_opy_ (u"ࠫࡸࡻࡩࡵࡧࠪൿ")):
        bstack1l1l1ll11l_opy_ = suite
      bstack1l1l1ll11l_opy_.append(bstack11lll1l111_opy_)
      bstack1l11l1ll1_opy_ = None
      for status in bstack11lll1l111_opy_.iter(bstack11ll1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ඀")):
        bstack1l11l1ll1_opy_ = status
      bstack1l1l1ll11l_opy_.append(bstack1l11l1ll1_opy_)
    bstack1ll111l11l_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡺ࡬࡮ࡲࡥࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠫඁ") + str(e))
def bstack11l1ll11l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1l1l1lll1_opy_
  global CONFIG
  if bstack11ll1l_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࡰࡢࡶ࡫ࠦං") in options:
    del options[bstack11ll1l_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬ࠧඃ")]
  json_data = bstack111l11ll1l_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack11ll1l_opy_ (u"ࠩࡳࡥࡧࡵࡴࡠࡴࡨࡷࡺࡲࡴࡴࠩ඄"), str(item_id), bstack11ll1l_opy_ (u"ࠪࡳࡺࡺࡰࡶࡶ࠱ࡼࡲࡲࠧඅ"))
    bstack111ll1lll_opy_(path, bstack1l1111l1l_opy_(json_data[item_id]))
  bstack1l111l111_opy_()
  return bstack1l1l1lll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack11ll1l111l_opy_(self, ff_profile_dir):
  global bstack111l1ll111_opy_
  if not ff_profile_dir:
    return None
  return bstack111l1ll111_opy_(self, ff_profile_dir)
def bstack111l111l11_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l11l1ll11_opy_
  bstack11111ll11_opy_ = []
  if bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧආ") in CONFIG:
    bstack11111ll11_opy_ = CONFIG[bstack11ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨඇ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11ll1l_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࠢඈ")],
      pabot_args[bstack11ll1l_opy_ (u"ࠢࡷࡧࡵࡦࡴࡹࡥࠣඉ")],
      argfile,
      pabot_args.get(bstack11ll1l_opy_ (u"ࠣࡪ࡬ࡺࡪࠨඊ")),
      pabot_args[bstack11ll1l_opy_ (u"ࠤࡳࡶࡴࡩࡥࡴࡵࡨࡷࠧඋ")],
      platform[0],
      bstack1l11l1ll11_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11ll1l_opy_ (u"ࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࡫࡯࡬ࡦࡵࠥඌ")] or [(bstack11ll1l_opy_ (u"ࠦࠧඍ"), None)]
    for platform in enumerate(bstack11111ll11_opy_)
  ]
def bstack1l1l1llll1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack11lll11l1_opy_=bstack11ll1l_opy_ (u"ࠬ࠭ඎ")):
  global bstack1ll1l11111_opy_
  self.platform_index = platform_index
  self.bstack111ll111l_opy_ = bstack11lll11l1_opy_
  bstack1ll1l11111_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1lll1l1l1l_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack111l11111_opy_
  global bstack11111l11l_opy_
  bstack11l1l1ll11_opy_ = copy.deepcopy(item)
  if not bstack11ll1l_opy_ (u"࠭ࡶࡢࡴ࡬ࡥࡧࡲࡥࠨඏ") in item.options:
    bstack11l1l1ll11_opy_.options[bstack11ll1l_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩඐ")] = []
  bstack11l111ll1_opy_ = bstack11l1l1ll11_opy_.options[bstack11ll1l_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪඑ")].copy()
  for v in bstack11l1l1ll11_opy_.options[bstack11ll1l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫඒ")]:
    if bstack11ll1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡓࡐࡆ࡚ࡆࡐࡔࡐࡍࡓࡊࡅ࡙ࠩඓ") in v:
      bstack11l111ll1_opy_.remove(v)
    if bstack11ll1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫඔ") in v:
      bstack11l111ll1_opy_.remove(v)
    if bstack11ll1l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡉࡋࡆࡍࡑࡆࡅࡑࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠩඕ") in v:
      bstack11l111ll1_opy_.remove(v)
  bstack11l111ll1_opy_.insert(0, bstack11ll1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡖࡌࡂࡖࡉࡓࡗࡓࡉࡏࡆࡈ࡜࠿ࢁࡽࠨඖ").format(bstack11l1l1ll11_opy_.platform_index))
  bstack11l111ll1_opy_.insert(0, bstack11ll1l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕ࠾ࢀࢃࠧ඗").format(bstack11l1l1ll11_opy_.bstack111ll111l_opy_))
  bstack11l1l1ll11_opy_.options[bstack11ll1l_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ඘")] = bstack11l111ll1_opy_
  if bstack11111l11l_opy_:
    bstack11l1l1ll11_opy_.options[bstack11ll1l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ඙")].insert(0, bstack11ll1l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡆࡐࡎࡇࡒࡈࡕ࠽ࡿࢂ࠭ක").format(bstack11111l11l_opy_))
  return bstack111l11111_opy_(caller_id, datasources, is_last, bstack11l1l1ll11_opy_, outs_dir)
def bstack1ll11111l1_opy_(command, item_index):
  try:
    if bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬඛ")):
      os.environ[bstack11ll1l_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭ග")] = json.dumps(CONFIG[bstack11ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩඝ")][item_index % bstack1lll11l1l1_opy_])
    global bstack11111l11l_opy_
    if bstack11111l11l_opy_:
      command[0] = command[0].replace(bstack11ll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ඞ"), bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡴࡦ࡮ࠤࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠥ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠤࠬඟ") + str(
        item_index) + bstack11ll1l_opy_ (u"ࠩࠣࠫච") + bstack11111l11l_opy_, 1)
    else:
      command[0] = command[0].replace(bstack11ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩඡ"),
                                      bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠰ࡷࡩࡱࠠࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨජ") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack11ll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡲࡵࡤࡪࡨࡼ࡭ࡳ࡭ࠠࡤࡱࡰࡱࡦࡴࡤࠡࡨࡲࡶࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮࠻ࠢࡾࢁࠬඣ").format(str(e)))
def bstack111ll1ll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack11ll1l1lll_opy_
  try:
    bstack1ll11111l1_opy_(command, item_index)
    return bstack11ll1l1lll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack11ll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱ࠾ࠥࢁࡽࠨඤ").format(str(e)))
    raise e
def bstack1lll1ll111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack11ll1l1lll_opy_
  try:
    bstack1ll11111l1_opy_(command, item_index)
    return bstack11ll1l1lll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack11ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲࠥ࠸࠮࠲࠵࠽ࠤࢀࢃࠧඥ").format(str(e)))
    try:
      return bstack11ll1l1lll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack11ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢ࠵࠲࠶࠹ࠠࡧࡣ࡯ࡰࡧࡧࡣ࡬࠼ࠣࡿࢂ࠭ඦ").format(str(e2)))
      raise e
def bstack1ll1l11ll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack11ll1l1lll_opy_
  try:
    bstack1ll11111l1_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack11ll1l1lll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack11ll1l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴࠠ࠳࠰࠴࠹࠿ࠦࡻࡾࠩට").format(str(e)))
    try:
      return bstack11ll1l1lll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack11ll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤ࠷࠴࠱࠶ࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨඨ").format(str(e2)))
      raise e
def _11ll1l1l1l_opy_(bstack1lll1llll1_opy_, item_index, process_timeout, sleep_before_start, bstack11l1l11l1_opy_):
  bstack1ll11111l1_opy_(bstack1lll1llll1_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack1lll1111ll_opy_(command, bstack1lllll1lll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11ll1l1lll_opy_
  try:
    bstack1ll11111l1_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack11ll1l1lll_opy_(command, bstack1lllll1lll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠸࠲࠵ࡀࠠࡼࡿࠪඩ").format(str(e)))
    try:
      return bstack11ll1l1lll_opy_(command, bstack1lllll1lll_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11ll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࡾࢁࠬඪ").format(str(e2)))
      raise e
def bstack1l11l111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack11ll1l1lll_opy_
  try:
    process_timeout = _11ll1l1l1l_opy_(command, item_index, process_timeout, sleep_before_start, bstack11ll1l_opy_ (u"࠭࠴࠯࠴ࠪණ"))
    return bstack11ll1l1lll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲࠥ࠺࠮࠳࠼ࠣࡿࢂ࠭ඬ").format(str(e)))
    try:
      return bstack11ll1l1lll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨත").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack1lll11ll1l_opy_(self, runner, quiet=False, capture=True):
  global bstack11lllllll1_opy_
  bstack11l1lll11_opy_ = bstack11lllllll1_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11ll1l_opy_ (u"ࠩࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࡤࡧࡲࡳࠩථ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11ll1l_opy_ (u"ࠪࡩࡽࡩ࡟ࡵࡴࡤࡧࡪࡨࡡࡤ࡭ࡢࡥࡷࡸࠧද")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack11l1lll11_opy_
def bstack111111l11l_opy_(runner, hook_name, context, element, bstack111l11llll_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1l1ll1l111_opy_.bstack11l111ll_opy_(hook_name, element)
    bstack111l11llll_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1l1ll1l111_opy_.bstack11l1l111_opy_(element)
      if hook_name not in [bstack11ll1l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠨධ"), bstack11ll1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨන")] and args and hasattr(args[0], bstack11ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࡤࡳࡥࡴࡵࡤ࡫ࡪ࠭඲")):
        args[0].error_message = bstack11ll1l_opy_ (u"ࠧࠨඳ")
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡭ࡧ࡮ࡥ࡮ࡨࠤ࡭ࡵ࡯࡬ࡵࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࡀࠠࡼࡿࠪප").format(str(e)))
@measure(event_name=EVENTS.bstack1l111lll1_opy_, stage=STAGE.bstack11ll11lll_opy_, hook_type=bstack11ll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡃ࡯ࡰࠧඵ"), bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack1lllll11ll_opy_(runner, name, context, bstack111l11llll_opy_, *args):
    if runner.hooks.get(bstack11ll1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢබ")).__name__ != bstack11ll1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࡠࡦࡨࡪࡦࡻ࡬ࡵࡡ࡫ࡳࡴࡱࠢභ"):
      bstack111111l11l_opy_(runner, name, context, runner, bstack111l11llll_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1ll1l11lll_opy_(bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫම")) else context.browser
      runner.driver_initialised = bstack11ll1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥඹ")
    except Exception as e:
      logger.debug(bstack11ll1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡥࡴ࡬ࡺࡪࡸࠠࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡨࠤࡦࡺࡴࡳ࡫ࡥࡹࡹ࡫࠺ࠡࡽࢀࠫය").format(str(e)))
def bstack1ll11ll11_opy_(runner, name, context, bstack111l11llll_opy_, *args):
    bstack111111l11l_opy_(runner, name, context, context.feature, bstack111l11llll_opy_, *args)
    try:
      if not bstack1lll1l1ll1_opy_:
        bstack111l1lll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1l11lll_opy_(bstack11ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧර")) else context.browser
        if is_driver_active(bstack111l1lll1_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack11ll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥ඼")
          bstack1l1llll11l_opy_ = str(runner.feature.name)
          bstack1l1l11llll_opy_(context, bstack1l1llll11l_opy_)
          bstack111l1lll1_opy_.execute_script(bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨල") + json.dumps(bstack1l1llll11l_opy_) + bstack11ll1l_opy_ (u"ࠫࢂࢃࠧ඾"))
    except Exception as e:
      logger.debug(bstack11ll1l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡧࡧࡤࡸࡺࡸࡥ࠻ࠢࡾࢁࠬ඿").format(str(e)))
def bstack111lll1lll_opy_(runner, name, context, bstack111l11llll_opy_, *args):
    if hasattr(context, bstack11ll1l_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨව")):
        bstack1l1ll1l111_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack11ll1l_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩශ")) else context.feature
    bstack111111l11l_opy_(runner, name, context, target, bstack111l11llll_opy_, *args)
@measure(event_name=EVENTS.bstack1lll111lll_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack111lllllll_opy_(runner, name, context, bstack111l11llll_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1l1ll1l111_opy_.start_test(context)
    bstack111111l11l_opy_(runner, name, context, context.scenario, bstack111l11llll_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack1l1l11ll11_opy_.bstack1lll11llll_opy_(context, *args)
    try:
      bstack111l1lll1_opy_ = bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧෂ"), context.browser)
      if is_driver_active(bstack111l1lll1_opy_):
        bstack1l1l1lll_opy_.bstack11ll11l11l_opy_(bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨස"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack11ll1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠧහ")
        if (not bstack1lll1l1ll1_opy_):
          scenario_name = args[0].name
          feature_name = bstack1l1llll11l_opy_ = str(runner.feature.name)
          bstack1l1llll11l_opy_ = feature_name + bstack11ll1l_opy_ (u"ࠫࠥ࠳ࠠࠨළ") + scenario_name
          if runner.driver_initialised == bstack11ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢෆ"):
            bstack1l1l11llll_opy_(context, bstack1l1llll11l_opy_)
            bstack111l1lll1_opy_.execute_script(bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫ෇") + json.dumps(bstack1l1llll11l_opy_) + bstack11ll1l_opy_ (u"ࠧࡾࡿࠪ෈"))
    except Exception as e:
      logger.debug(bstack11ll1l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡷࡨ࡫࡮ࡢࡴ࡬ࡳ࠿ࠦࡻࡾࠩ෉").format(str(e)))
@measure(event_name=EVENTS.bstack1l111lll1_opy_, stage=STAGE.bstack11ll11lll_opy_, hook_type=bstack11ll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡕࡷࡩࡵࠨ්"), bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack11l11l11l_opy_(runner, name, context, bstack111l11llll_opy_, *args):
    bstack111111l11l_opy_(runner, name, context, args[0], bstack111l11llll_opy_, *args)
    try:
      bstack111l1lll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1l11lll_opy_(bstack11ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ෋")) else context.browser
      if is_driver_active(bstack111l1lll1_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack11ll1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤ෌")
        bstack1l1ll1l111_opy_.bstack11l1l11l_opy_(args[0])
        if runner.driver_initialised == bstack11ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥ෍"):
          feature_name = bstack1l1llll11l_opy_ = str(runner.feature.name)
          bstack1l1llll11l_opy_ = feature_name + bstack11ll1l_opy_ (u"࠭ࠠ࠮ࠢࠪ෎") + context.scenario.name
          bstack111l1lll1_opy_.execute_script(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬා") + json.dumps(bstack1l1llll11l_opy_) + bstack11ll1l_opy_ (u"ࠨࡿࢀࠫැ"))
    except Exception as e:
      logger.debug(bstack11ll1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡ࡫ࡱࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡺࡥࡱ࠼ࠣࡿࢂ࠭ෑ").format(str(e)))
@measure(event_name=EVENTS.bstack1l111lll1_opy_, stage=STAGE.bstack11ll11lll_opy_, hook_type=bstack11ll1l_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࡕࡷࡩࡵࠨි"), bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack111llll11_opy_(runner, name, context, bstack111l11llll_opy_, *args):
  bstack1l1ll1l111_opy_.bstack111lll1l_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack111l1lll1_opy_ = threading.current_thread().bstackSessionDriver if bstack11ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪී") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack111l1lll1_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack11ll1l_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬු")
        feature_name = bstack1l1llll11l_opy_ = str(runner.feature.name)
        bstack1l1llll11l_opy_ = feature_name + bstack11ll1l_opy_ (u"࠭ࠠ࠮ࠢࠪ෕") + context.scenario.name
        bstack111l1lll1_opy_.execute_script(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬූ") + json.dumps(bstack1l1llll11l_opy_) + bstack11ll1l_opy_ (u"ࠨࡿࢀࠫ෗"))
    if str(step_status).lower() == bstack11ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩෘ"):
      bstack1ll11l1l11_opy_ = bstack11ll1l_opy_ (u"ࠪࠫෙ")
      bstack111ll1l11l_opy_ = bstack11ll1l_opy_ (u"ࠫࠬේ")
      bstack1ll111l1ll_opy_ = bstack11ll1l_opy_ (u"ࠬ࠭ෛ")
      try:
        import traceback
        bstack1ll11l1l11_opy_ = runner.exception.__class__.__name__
        bstack111llll1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack111ll1l11l_opy_ = bstack11ll1l_opy_ (u"࠭ࠠࠨො").join(bstack111llll1_opy_)
        bstack1ll111l1ll_opy_ = bstack111llll1_opy_[-1]
      except Exception as e:
        logger.debug(bstack11111l1ll_opy_.format(str(e)))
      bstack1ll11l1l11_opy_ += bstack1ll111l1ll_opy_
      bstack1llll11111_opy_(context, json.dumps(str(args[0].name) + bstack11ll1l_opy_ (u"ࠢࠡ࠯ࠣࡊࡦ࡯࡬ࡦࡦࠤࡠࡳࠨෝ") + str(bstack111ll1l11l_opy_)),
                          bstack11ll1l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢෞ"))
      if runner.driver_initialised == bstack11ll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢෟ"):
        bstack1l1111l11_opy_(getattr(context, bstack11ll1l_opy_ (u"ࠪࡴࡦ࡭ࡥࠨ෠"), None), bstack11ll1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࠦ෡"), bstack1ll11l1l11_opy_)
        bstack111l1lll1_opy_.execute_script(bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ෢") + json.dumps(str(args[0].name) + bstack11ll1l_opy_ (u"ࠨࠠ࠮ࠢࡉࡥ࡮ࡲࡥࡥࠣ࡟ࡲࠧ෣") + str(bstack111ll1l11l_opy_)) + bstack11ll1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧ෤"))
      if runner.driver_initialised == bstack11ll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨ෥"):
        bstack1l11ll11l1_opy_(bstack111l1lll1_opy_, bstack11ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ෦"), bstack11ll1l_opy_ (u"ࠥࡗࡨ࡫࡮ࡢࡴ࡬ࡳࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢ෧") + str(bstack1ll11l1l11_opy_))
    else:
      bstack1llll11111_opy_(context, bstack11ll1l_opy_ (u"ࠦࡕࡧࡳࡴࡧࡧࠥࠧ෨"), bstack11ll1l_opy_ (u"ࠧ࡯࡮ࡧࡱࠥ෩"))
      if runner.driver_initialised == bstack11ll1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦ෪"):
        bstack1l1111l11_opy_(getattr(context, bstack11ll1l_opy_ (u"ࠧࡱࡣࡪࡩࠬ෫"), None), bstack11ll1l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣ෬"))
      bstack111l1lll1_opy_.execute_script(bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ෭") + json.dumps(str(args[0].name) + bstack11ll1l_opy_ (u"ࠥࠤ࠲ࠦࡐࡢࡵࡶࡩࡩࠧࠢ෮")) + bstack11ll1l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢࡾࡿࠪ෯"))
      if runner.driver_initialised == bstack11ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥ෰"):
        bstack1l11ll11l1_opy_(bstack111l1lll1_opy_, bstack11ll1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨ෱"))
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤࡸࡺࡥࡱ࠼ࠣࡿࢂ࠭ෲ").format(str(e)))
  bstack111111l11l_opy_(runner, name, context, args[0], bstack111l11llll_opy_, *args)
@measure(event_name=EVENTS.bstack11l1lll1ll_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack11llll11ll_opy_(runner, name, context, bstack111l11llll_opy_, *args):
  bstack1l1ll1l111_opy_.end_test(args[0])
  try:
    bstack1l1llllll1_opy_ = args[0].status.name
    bstack111l1lll1_opy_ = bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧෳ"), context.browser)
    bstack1l1l11ll11_opy_.bstack1ll11lllll_opy_(bstack111l1lll1_opy_)
    if str(bstack1l1llllll1_opy_).lower() == bstack11ll1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ෴"):
      bstack1ll11l1l11_opy_ = bstack11ll1l_opy_ (u"ࠪࠫ෵")
      bstack111ll1l11l_opy_ = bstack11ll1l_opy_ (u"ࠫࠬ෶")
      bstack1ll111l1ll_opy_ = bstack11ll1l_opy_ (u"ࠬ࠭෷")
      try:
        import traceback
        bstack1ll11l1l11_opy_ = runner.exception.__class__.__name__
        bstack111llll1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack111ll1l11l_opy_ = bstack11ll1l_opy_ (u"࠭ࠠࠨ෸").join(bstack111llll1_opy_)
        bstack1ll111l1ll_opy_ = bstack111llll1_opy_[-1]
      except Exception as e:
        logger.debug(bstack11111l1ll_opy_.format(str(e)))
      bstack1ll11l1l11_opy_ += bstack1ll111l1ll_opy_
      bstack1llll11111_opy_(context, json.dumps(str(args[0].name) + bstack11ll1l_opy_ (u"ࠢࠡ࠯ࠣࡊࡦ࡯࡬ࡦࡦࠤࡠࡳࠨ෹") + str(bstack111ll1l11l_opy_)),
                          bstack11ll1l_opy_ (u"ࠣࡧࡵࡶࡴࡸࠢ෺"))
      if runner.driver_initialised == bstack11ll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦ෻") or runner.driver_initialised == bstack11ll1l_opy_ (u"ࠪ࡭ࡳࡹࡴࡦࡲࠪ෼"):
        bstack1l1111l11_opy_(getattr(context, bstack11ll1l_opy_ (u"ࠫࡵࡧࡧࡦࠩ෽"), None), bstack11ll1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧ෾"), bstack1ll11l1l11_opy_)
        bstack111l1lll1_opy_.execute_script(bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ෿") + json.dumps(str(args[0].name) + bstack11ll1l_opy_ (u"ࠢࠡ࠯ࠣࡊࡦ࡯࡬ࡦࡦࠤࡠࡳࠨ฀") + str(bstack111ll1l11l_opy_)) + bstack11ll1l_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨก"))
      if runner.driver_initialised == bstack11ll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦข") or runner.driver_initialised == bstack11ll1l_opy_ (u"ࠪ࡭ࡳࡹࡴࡦࡲࠪฃ"):
        bstack1l11ll11l1_opy_(bstack111l1lll1_opy_, bstack11ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫค"), bstack11ll1l_opy_ (u"࡙ࠧࡣࡦࡰࡤࡶ࡮ࡵࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤฅ") + str(bstack1ll11l1l11_opy_))
    else:
      bstack1llll11111_opy_(context, bstack11ll1l_opy_ (u"ࠨࡐࡢࡵࡶࡩࡩࠧࠢฆ"), bstack11ll1l_opy_ (u"ࠢࡪࡰࡩࡳࠧง"))
      if runner.driver_initialised == bstack11ll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥจ") or runner.driver_initialised == bstack11ll1l_opy_ (u"ࠩ࡬ࡲࡸࡺࡥࡱࠩฉ"):
        bstack1l1111l11_opy_(getattr(context, bstack11ll1l_opy_ (u"ࠪࡴࡦ࡭ࡥࠨช"), None), bstack11ll1l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦซ"))
      bstack111l1lll1_opy_.execute_script(bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪฌ") + json.dumps(str(args[0].name) + bstack11ll1l_opy_ (u"ࠨࠠ࠮ࠢࡓࡥࡸࡹࡥࡥࠣࠥญ")) + bstack11ll1l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭ฎ"))
      if runner.driver_initialised == bstack11ll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥฏ") or runner.driver_initialised == bstack11ll1l_opy_ (u"ࠩ࡬ࡲࡸࡺࡥࡱࠩฐ"):
        bstack1l11ll11l1_opy_(bstack111l1lll1_opy_, bstack11ll1l_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥฑ"))
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡨࡨࡥࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭ฒ").format(str(e)))
  bstack111111l11l_opy_(runner, name, context, context.scenario, bstack111l11llll_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack11l11llll1_opy_(runner, name, context, bstack111l11llll_opy_, *args):
    target = context.scenario if hasattr(context, bstack11ll1l_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧณ")) else context.feature
    bstack111111l11l_opy_(runner, name, context, target, bstack111l11llll_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1ll111l1l1_opy_(runner, name, context, bstack111l11llll_opy_, *args):
    try:
      bstack111l1lll1_opy_ = bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬด"), context.browser)
      bstack1llll11l11_opy_ = bstack11ll1l_opy_ (u"ࠧࠨต")
      if context.failed is True:
        bstack1ll11lll1l_opy_ = []
        bstack1l1l1111l_opy_ = []
        bstack1ll11l1111_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1ll11lll1l_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack111llll1_opy_ = traceback.format_tb(exc_tb)
            bstack1ll11l11ll_opy_ = bstack11ll1l_opy_ (u"ࠨࠢࠪถ").join(bstack111llll1_opy_)
            bstack1l1l1111l_opy_.append(bstack1ll11l11ll_opy_)
            bstack1ll11l1111_opy_.append(bstack111llll1_opy_[-1])
        except Exception as e:
          logger.debug(bstack11111l1ll_opy_.format(str(e)))
        bstack1ll11l1l11_opy_ = bstack11ll1l_opy_ (u"ࠩࠪท")
        for i in range(len(bstack1ll11lll1l_opy_)):
          bstack1ll11l1l11_opy_ += bstack1ll11lll1l_opy_[i] + bstack1ll11l1111_opy_[i] + bstack11ll1l_opy_ (u"ࠪࡠࡳ࠭ธ")
        bstack1llll11l11_opy_ = bstack11ll1l_opy_ (u"ࠫࠥ࠭น").join(bstack1l1l1111l_opy_)
        if runner.driver_initialised in [bstack11ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨบ"), bstack11ll1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥป")]:
          bstack1llll11111_opy_(context, bstack1llll11l11_opy_, bstack11ll1l_opy_ (u"ࠢࡦࡴࡵࡳࡷࠨผ"))
          bstack1l1111l11_opy_(getattr(context, bstack11ll1l_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ฝ"), None), bstack11ll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤพ"), bstack1ll11l1l11_opy_)
          bstack111l1lll1_opy_.execute_script(bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨฟ") + json.dumps(bstack1llll11l11_opy_) + bstack11ll1l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫภ"))
          bstack1l11ll11l1_opy_(bstack111l1lll1_opy_, bstack11ll1l_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧม"), bstack11ll1l_opy_ (u"ࠨࡓࡰ࡯ࡨࠤࡸࡩࡥ࡯ࡣࡵ࡭ࡴࡹࠠࡧࡣ࡬ࡰࡪࡪ࠺ࠡ࡞ࡱࠦย") + str(bstack1ll11l1l11_opy_))
          bstack11ll1llll1_opy_ = bstack1ll11111ll_opy_(bstack1llll11l11_opy_, runner.feature.name, logger)
          if (bstack11ll1llll1_opy_ != None):
            bstack11lll1111l_opy_.append(bstack11ll1llll1_opy_)
      else:
        if runner.driver_initialised in [bstack11ll1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣร"), bstack11ll1l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧฤ")]:
          bstack1llll11111_opy_(context, bstack11ll1l_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧ࠽ࠤࠧล") + str(runner.feature.name) + bstack11ll1l_opy_ (u"ࠥࠤࡵࡧࡳࡴࡧࡧࠥࠧฦ"), bstack11ll1l_opy_ (u"ࠦ࡮ࡴࡦࡰࠤว"))
          bstack1l1111l11_opy_(getattr(context, bstack11ll1l_opy_ (u"ࠬࡶࡡࡨࡧࠪศ"), None), bstack11ll1l_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨษ"))
          bstack111l1lll1_opy_.execute_script(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬส") + json.dumps(bstack11ll1l_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦ࠼ࠣࠦห") + str(runner.feature.name) + bstack11ll1l_opy_ (u"ࠤࠣࡴࡦࡹࡳࡦࡦࠤࠦฬ")) + bstack11ll1l_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩอ"))
          bstack1l11ll11l1_opy_(bstack111l1lll1_opy_, bstack11ll1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫฮ"))
          bstack11ll1llll1_opy_ = bstack1ll11111ll_opy_(bstack1llll11l11_opy_, runner.feature.name, logger)
          if (bstack11ll1llll1_opy_ != None):
            bstack11lll1111l_opy_.append(bstack11ll1llll1_opy_)
    except Exception as e:
      logger.debug(bstack11ll1l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡ࡯ࡤࡶࡰࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡴࡶࡤࡸࡺࡹࠠࡪࡰࠣࡥ࡫ࡺࡥࡳࠢࡩࡩࡦࡺࡵࡳࡧ࠽ࠤࢀࢃࠧฯ").format(str(e)))
    bstack111111l11l_opy_(runner, name, context, context.feature, bstack111l11llll_opy_, *args)
@measure(event_name=EVENTS.bstack1l111lll1_opy_, stage=STAGE.bstack11ll11lll_opy_, hook_type=bstack11ll1l_opy_ (u"ࠨࡡࡧࡶࡨࡶࡆࡲ࡬ࠣะ"), bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack1llll111l1_opy_(runner, name, context, bstack111l11llll_opy_, *args):
    bstack111111l11l_opy_(runner, name, context, runner, bstack111l11llll_opy_, *args)
def bstack11l1l111l1_opy_(self, name, context, *args):
  try:
    if bstack11lllll111_opy_:
      platform_index = int(threading.current_thread()._name) % bstack1lll11l1l1_opy_
      bstack11l1l11l1l_opy_ = CONFIG[bstack11ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪั")][platform_index]
      os.environ[bstack11ll1l_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩา")] = json.dumps(bstack11l1l11l1l_opy_)
    global bstack111l11llll_opy_
    if not hasattr(self, bstack11ll1l_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࡡ࡬ࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡪࡪࠧำ")):
      self.driver_initialised = None
    bstack11l111111l_opy_ = {
        bstack11ll1l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠧิ"): bstack1lllll11ll_opy_,
        bstack11ll1l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠬี"): bstack1ll11ll11_opy_,
        bstack11ll1l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࡤࡺࡡࡨࠩึ"): bstack111lll1lll_opy_,
        bstack11ll1l_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠨื"): bstack111lllllll_opy_,
        bstack11ll1l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴุࠬ"): bstack11l11l11l_opy_,
        bstack11ll1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡶࡨࡴูࠬ"): bstack111llll11_opy_,
        bstack11ll1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡵࡦࡩࡳࡧࡲࡪࡱฺࠪ"): bstack11llll11ll_opy_,
        bstack11ll1l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡷࡥ࡬࠭฻"): bstack11l11llll1_opy_,
        bstack11ll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡪࡪࡧࡴࡶࡴࡨࠫ฼"): bstack1ll111l1l1_opy_,
        bstack11ll1l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨ฽"): bstack1llll111l1_opy_
    }
    handler = bstack11l111111l_opy_.get(name, bstack111l11llll_opy_)
    try:
      handler(self, name, context, bstack111l11llll_opy_, *args)
    except Exception as e:
      logger.debug(bstack11ll1l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥࠡࡪࡲࡳࡰࠦࡨࡢࡰࡧࡰࡪࡸࠠࡼࡿ࠽ࠤࢀࢃࠧ฾").format(name, str(e)))
    if name in [bstack11ll1l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧ฿"), bstack11ll1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩเ"), bstack11ll1l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡣ࡯ࡰࠬแ")]:
      try:
        bstack111l1lll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1ll1l11lll_opy_(bstack11ll1l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩโ")) else context.browser
        bstack11l1l1l1ll_opy_ = (
          (name == bstack11ll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡥࡱࡲࠧใ") and self.driver_initialised == bstack11ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤไ")) or
          (name == bstack11ll1l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤ࡬ࡥࡢࡶࡸࡶࡪ࠭ๅ") and self.driver_initialised == bstack11ll1l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠣๆ")) or
          (name == bstack11ll1l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠩ็") and self.driver_initialised in [bstack11ll1l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲ่ࠦ"), bstack11ll1l_opy_ (u"ࠥ࡭ࡳࡹࡴࡦࡲ้ࠥ")]) or
          (name == bstack11ll1l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡹ࡫ࡰࠨ๊") and self.driver_initialised == bstack11ll1l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲ๋ࠥ"))
        )
        if bstack11l1l1l1ll_opy_:
          self.driver_initialised = None
          if bstack111l1lll1_opy_ and hasattr(bstack111l1lll1_opy_, bstack11ll1l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠪ์")):
            try:
              bstack111l1lll1_opy_.quit()
            except Exception as e:
              logger.debug(bstack11ll1l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡱࡶ࡫ࡷࡸ࡮ࡴࡧࠡࡦࡵ࡭ࡻ࡫ࡲࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨࠤ࡭ࡵ࡯࡬࠼ࠣࡿࢂ࠭ํ").format(str(e)))
      except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡥ࡫ࡺࡥࡳࠢ࡫ࡳࡴࡱࠠࡤ࡮ࡨࡥࡳࡻࡰࠡࡨࡲࡶࠥࢁࡽ࠻ࠢࡾࢁࠬ๎").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠩࡆࡶ࡮ࡺࡩࡤࡣ࡯ࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࠦࡲࡶࡰࠣ࡬ࡴࡵ࡫ࠡࡽࢀ࠾ࠥࢁࡽࠨ๏").format(name, str(e)))
    try:
      bstack111l11llll_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack11ll1l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱࠠࡰࡴ࡬࡫࡮ࡴࡡ࡭ࠢࡥࡩ࡭ࡧࡶࡦࠢ࡫ࡳࡴࡱࠠࡼࡿ࠽ࠤࢀࢃࠧ๐").format(name, str(e2)))
def bstack111111llll_opy_(config, startdir):
  return bstack11ll1l_opy_ (u"ࠦࡩࡸࡩࡷࡧࡵ࠾ࠥࢁ࠰ࡾࠤ๑").format(bstack11ll1l_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦ๒"))
notset = Notset()
def bstack1l1llll11_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1l11ll1ll1_opy_
  if str(name).lower() == bstack11ll1l_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷ࠭๓"):
    return bstack11ll1l_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠨ๔")
  else:
    return bstack1l11ll1ll1_opy_(self, name, default, skip)
def bstack1111ll1l11_opy_(item, when):
  global bstack1ll1l11l1l_opy_
  try:
    bstack1ll1l11l1l_opy_(item, when)
  except Exception as e:
    pass
def bstack1ll11lll1_opy_():
  return
def bstack1l1ll1llll_opy_(type, name, status, reason, bstack1ll1llll11_opy_, bstack111l1lll1l_opy_):
  bstack1l1l11l11l_opy_ = {
    bstack11ll1l_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨ๕"): type,
    bstack11ll1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ๖"): {}
  }
  if type == bstack11ll1l_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬ๗"):
    bstack1l1l11l11l_opy_[bstack11ll1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ๘")][bstack11ll1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ๙")] = bstack1ll1llll11_opy_
    bstack1l1l11l11l_opy_[bstack11ll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ๚")][bstack11ll1l_opy_ (u"ࠧࡥࡣࡷࡥࠬ๛")] = json.dumps(str(bstack111l1lll1l_opy_))
  if type == bstack11ll1l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ๜"):
    bstack1l1l11l11l_opy_[bstack11ll1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ๝")][bstack11ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ๞")] = name
  if type == bstack11ll1l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ๟"):
    bstack1l1l11l11l_opy_[bstack11ll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ๠")][bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭๡")] = status
    if status == bstack11ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ๢"):
      bstack1l1l11l11l_opy_[bstack11ll1l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ๣")][bstack11ll1l_opy_ (u"ࠩࡵࡩࡦࡹ࡯࡯ࠩ๤")] = json.dumps(str(reason))
  bstack1111111l1l_opy_ = bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࡽࠨ๥").format(json.dumps(bstack1l1l11l11l_opy_))
  return bstack1111111l1l_opy_
def bstack111111l1l_opy_(driver_command, response):
    if driver_command == bstack11ll1l_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨ๦"):
        bstack1l1l1lll_opy_.bstack111l11lll1_opy_({
            bstack11ll1l_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫ๧"): response[bstack11ll1l_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬ๨")],
            bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ๩"): bstack1l1l1lll_opy_.current_test_uuid()
        })
def bstack1ll1llll1l_opy_(item, call, rep):
  global bstack1l111ll1l1_opy_
  global bstack1l1lll1ll_opy_
  global bstack1lll1l1ll1_opy_
  name = bstack11ll1l_opy_ (u"ࠨࠩ๪")
  try:
    if rep.when == bstack11ll1l_opy_ (u"ࠩࡦࡥࡱࡲࠧ๫"):
      bstack1ll11l1l1_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1lll1l1ll1_opy_:
          name = str(rep.nodeid)
          bstack1111l1l111_opy_ = bstack1l1ll1llll_opy_(bstack11ll1l_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ๬"), name, bstack11ll1l_opy_ (u"ࠫࠬ๭"), bstack11ll1l_opy_ (u"ࠬ࠭๮"), bstack11ll1l_opy_ (u"࠭ࠧ๯"), bstack11ll1l_opy_ (u"ࠧࠨ๰"))
          threading.current_thread().bstack1ll1ll1ll1_opy_ = name
          for driver in bstack1l1lll1ll_opy_:
            if bstack1ll11l1l1_opy_ == driver.session_id:
              driver.execute_script(bstack1111l1l111_opy_)
      except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨ๱").format(str(e)))
      try:
        bstack11l111l1ll_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11ll1l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ๲"):
          status = bstack11ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ๳") if rep.outcome.lower() == bstack11ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ๴") else bstack11ll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ๵")
          reason = bstack11ll1l_opy_ (u"࠭ࠧ๶")
          if status == bstack11ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ๷"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11ll1l_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭๸") if status == bstack11ll1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ๹") else bstack11ll1l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ๺")
          data = name + bstack11ll1l_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭๻") if status == bstack11ll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ๼") else name + bstack11ll1l_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠡࠡࠩ๽") + reason
          bstack1l1ll1ll11_opy_ = bstack1l1ll1llll_opy_(bstack11ll1l_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩ๾"), bstack11ll1l_opy_ (u"ࠨࠩ๿"), bstack11ll1l_opy_ (u"ࠩࠪ຀"), bstack11ll1l_opy_ (u"ࠪࠫກ"), level, data)
          for driver in bstack1l1lll1ll_opy_:
            if bstack1ll11l1l1_opy_ == driver.session_id:
              driver.execute_script(bstack1l1ll1ll11_opy_)
      except Exception as e:
        logger.debug(bstack11ll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡥࡲࡲࡹ࡫ࡸࡵࠢࡩࡳࡷࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡷࡪࡹࡳࡪࡱࡱ࠾ࠥࢁࡽࠨຂ").format(str(e)))
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡵࡷࡥࡹ࡫ࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࡻࡾࠩ຃").format(str(e)))
  bstack1l111ll1l1_opy_(item, call, rep)
def bstack1lll1l1111_opy_(driver, bstack1l11l1l1ll_opy_, test=None):
  global bstack1l111l1111_opy_
  if test != None:
    bstack11ll1llll_opy_ = getattr(test, bstack11ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫຄ"), None)
    bstack1111111l1_opy_ = getattr(test, bstack11ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ຅"), None)
    PercySDK.screenshot(driver, bstack1l11l1l1ll_opy_, bstack11ll1llll_opy_=bstack11ll1llll_opy_, bstack1111111l1_opy_=bstack1111111l1_opy_, bstack1ll1l11l1_opy_=bstack1l111l1111_opy_)
  else:
    PercySDK.screenshot(driver, bstack1l11l1l1ll_opy_)
@measure(event_name=EVENTS.bstack111l111111_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack1lll1l11ll_opy_(driver):
  if bstack1l11l1l11_opy_.bstack1l1ll11l1_opy_() is True or bstack1l11l1l11_opy_.capturing() is True:
    return
  bstack1l11l1l11_opy_.bstack1l11l1l111_opy_()
  while not bstack1l11l1l11_opy_.bstack1l1ll11l1_opy_():
    bstack1l1lll11l_opy_ = bstack1l11l1l11_opy_.bstack11llll111l_opy_()
    bstack1lll1l1111_opy_(driver, bstack1l1lll11l_opy_)
  bstack1l11l1l11_opy_.bstack11lll111l1_opy_()
def bstack111l1lll11_opy_(sequence, driver_command, response = None, bstack1ll1l1l1l_opy_ = None, args = None):
    try:
      if sequence != bstack11ll1l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࠨຆ"):
        return
      if percy.bstack1l1l11111_opy_() == bstack11ll1l_opy_ (u"ࠤࡩࡥࡱࡹࡥࠣງ"):
        return
      bstack1l1lll11l_opy_ = bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠪࡴࡪࡸࡣࡺࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ຈ"), None)
      for command in bstack11ll11ll1_opy_:
        if command == driver_command:
          with bstack11llll1111_opy_:
            bstack111l11ll11_opy_ = bstack1l1lll1ll_opy_.copy()
          for driver in bstack111l11ll11_opy_:
            bstack1lll1l11ll_opy_(driver)
      bstack11lll1lll1_opy_ = percy.bstack11l1l1111l_opy_()
      if driver_command in bstack11ll111ll1_opy_[bstack11lll1lll1_opy_]:
        bstack1l11l1l11_opy_.bstack11l111ll11_opy_(bstack1l1lll11l_opy_, driver_command)
    except Exception as e:
      pass
def bstack1l111111ll_opy_(framework_name):
  if bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡲࡵࡤࡠࡥࡤࡰࡱ࡫ࡤࠨຉ")):
      return
  bstack111ll1l1_opy_.set_property(bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡳ࡯ࡥࡡࡦࡥࡱࡲࡥࡥࠩຊ"), True)
  global bstack1l111lll1l_opy_
  global bstack1l1l1ll111_opy_
  global bstack1l1ll1l11_opy_
  bstack1l111lll1l_opy_ = framework_name
  logger.info(bstack1l1111ll1l_opy_.format(bstack1l111lll1l_opy_.split(bstack11ll1l_opy_ (u"࠭࠭ࠨ຋"))[0]))
  bstack1111l1l11_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack11lllll111_opy_:
      Service.start = bstack1ll11ll11l_opy_
      Service.stop = bstack111l111lll_opy_
      webdriver.Remote.get = bstack1ll1ll11l1_opy_
      WebDriver.quit = bstack11111l1l1_opy_
      webdriver.Remote.__init__ = bstack11ll11lll1_opy_
    if not bstack11lllll111_opy_:
        webdriver.Remote.__init__ = bstack11ll1111l_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack1ll11l11l1_opy_
    bstack1l1l1ll111_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack11lllll111_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack1l1111l11l_opy_
  except Exception as e:
    pass
  bstack11l1l11ll_opy_()
  if not bstack1l1l1ll111_opy_:
    bstack1l11ll1111_opy_(bstack11ll1l_opy_ (u"ࠢࡑࡣࡦ࡯ࡦ࡭ࡥࡴࠢࡱࡳࡹࠦࡩ࡯ࡵࡷࡥࡱࡲࡥࡥࠤຌ"), bstack1ll1111ll_opy_)
  if bstack1111l11lll_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack11ll1l_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩຍ")) and callable(getattr(RemoteConnection, bstack11ll1l_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪຎ"))):
        RemoteConnection._get_proxy_url = bstack1ll1ll1ll_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack1ll1ll1ll_opy_
    except Exception as e:
      logger.error(bstack1ll1ll1lll_opy_.format(str(e)))
  if bstack11111lllll_opy_():
    bstack11llllll1l_opy_(CONFIG, logger)
  if (bstack11ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩຏ") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1l1l11111_opy_() == bstack11ll1l_opy_ (u"ࠦࡹࡸࡵࡦࠤຐ"):
          bstack11l1llll11_opy_(bstack111l1lll11_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack11ll1l111l_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack111ll1l1l_opy_
      except Exception as e:
        logger.warn(bstack1lll11ll11_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1l1llll1l1_opy_
      except Exception as e:
        logger.debug(bstack1l1l11l1ll_opy_ + str(e))
    except Exception as e:
      bstack1l11ll1111_opy_(e, bstack1lll11ll11_opy_)
    Output.start_test = bstack111l1l1ll1_opy_
    Output.end_test = bstack11ll11l1ll_opy_
    TestStatus.__init__ = bstack1l11llll11_opy_
    QueueItem.__init__ = bstack1l1l1llll1_opy_
    pabot._create_items = bstack111l111l11_opy_
    try:
      from pabot import __version__ as bstack11l1l1l11l_opy_
      if version.parse(bstack11l1l1l11l_opy_) >= version.parse(bstack11ll1l_opy_ (u"ࠬ࠻࠮࠱࠰࠳ࠫຑ")):
        pabot._run = bstack1lll1111ll_opy_
      elif version.parse(bstack11l1l1l11l_opy_) >= version.parse(bstack11ll1l_opy_ (u"࠭࠴࠯࠴࠱࠴ࠬຒ")):
        pabot._run = bstack1l11l111l_opy_
      elif version.parse(bstack11l1l1l11l_opy_) >= version.parse(bstack11ll1l_opy_ (u"ࠧ࠳࠰࠴࠹࠳࠶ࠧຓ")):
        pabot._run = bstack1ll1l11ll1_opy_
      elif version.parse(bstack11l1l1l11l_opy_) >= version.parse(bstack11ll1l_opy_ (u"ࠨ࠴࠱࠵࠸࠴࠰ࠨດ")):
        pabot._run = bstack1lll1ll111_opy_
      else:
        pabot._run = bstack111ll1ll1_opy_
    except Exception as e:
      pabot._run = bstack111ll1ll1_opy_
    pabot._create_command_for_execution = bstack1lll1l1l1l_opy_
    pabot._report_results = bstack11l1ll11l_opy_
  if bstack11ll1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩຕ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l11ll1111_opy_(e, bstack1ll111llll_opy_)
    Runner.run_hook = bstack11l1l111l1_opy_
    Step.run = bstack1lll11ll1l_opy_
  if bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪຖ") in str(framework_name).lower():
    if not bstack11lllll111_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack111111llll_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1ll11lll1_opy_
      Config.getoption = bstack1l1llll11_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1ll1llll1l_opy_
    except Exception as e:
      pass
def bstack11lll11lll_opy_():
  global CONFIG
  if bstack11ll1l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫທ") in CONFIG and int(CONFIG[bstack11ll1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬຘ")]) > 1:
    logger.warn(bstack11l1l1ll1_opy_)
def bstack11lll1l1l_opy_(arg, bstack111ll11l_opy_, bstack1l111111l_opy_=None):
  global CONFIG
  global bstack11llll11l_opy_
  global bstack11ll11l111_opy_
  global bstack11lllll111_opy_
  global bstack111ll1l1_opy_
  bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ນ")
  if bstack111ll11l_opy_ and isinstance(bstack111ll11l_opy_, str):
    bstack111ll11l_opy_ = eval(bstack111ll11l_opy_)
  CONFIG = bstack111ll11l_opy_[bstack11ll1l_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧບ")]
  bstack11llll11l_opy_ = bstack111ll11l_opy_[bstack11ll1l_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩປ")]
  bstack11ll11l111_opy_ = bstack111ll11l_opy_[bstack11ll1l_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫຜ")]
  bstack11lllll111_opy_ = bstack111ll11l_opy_[bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓ࠭ຝ")]
  bstack111ll1l1_opy_.set_property(bstack11ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬພ"), bstack11lllll111_opy_)
  os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧຟ")] = bstack1ll1l1ll1_opy_
  os.environ[bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࠬຠ")] = json.dumps(CONFIG)
  os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡈࡖࡄࡢ࡙ࡗࡒࠧມ")] = bstack11llll11l_opy_
  os.environ[bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩຢ")] = str(bstack11ll11l111_opy_)
  os.environ[bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡏ࡙ࡌࡏࡎࠨຣ")] = str(True)
  if bstack11ll111l1l_opy_(arg, [bstack11ll1l_opy_ (u"ࠪ࠱ࡳ࠭຤"), bstack11ll1l_opy_ (u"ࠫ࠲࠳࡮ࡶ࡯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬລ")]) != -1:
    os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡇࡒࡂࡎࡏࡉࡑ࠭຦")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack11l1l11111_opy_)
    return
  bstack1l111l11l_opy_()
  global bstack1l11lll1l_opy_
  global bstack1l111l1111_opy_
  global bstack1l11l1ll11_opy_
  global bstack11111l11l_opy_
  global bstack11l11l1l1_opy_
  global bstack1l1ll1l11_opy_
  global bstack1lll111l11_opy_
  arg.append(bstack11ll1l_opy_ (u"ࠨ࠭ࡘࠤວ"))
  arg.append(bstack11ll1l_opy_ (u"ࠢࡪࡩࡱࡳࡷ࡫࠺ࡎࡱࡧࡹࡱ࡫ࠠࡢ࡮ࡵࡩࡦࡪࡹࠡ࡫ࡰࡴࡴࡸࡴࡦࡦ࠽ࡴࡾࡺࡥࡴࡶ࠱ࡔࡾࡺࡥࡴࡶ࡚ࡥࡷࡴࡩ࡯ࡩࠥຨ"))
  arg.append(bstack11ll1l_opy_ (u"ࠣ࠯࡚ࠦຩ"))
  arg.append(bstack11ll1l_opy_ (u"ࠤ࡬࡫ࡳࡵࡲࡦ࠼ࡗ࡬ࡪࠦࡨࡰࡱ࡮࡭ࡲࡶ࡬ࠣສ"))
  global bstack111l111ll1_opy_
  global bstack1l111l1l1l_opy_
  global bstack111l1l1l1_opy_
  global bstack11l1l1111_opy_
  global bstack111l1ll111_opy_
  global bstack1ll1l11111_opy_
  global bstack111l11111_opy_
  global bstack111ll1ll11_opy_
  global bstack11ll1lll1_opy_
  global bstack111ll1ll1l_opy_
  global bstack1l11ll1ll1_opy_
  global bstack1ll1l11l1l_opy_
  global bstack1l111ll1l1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack111l111ll1_opy_ = webdriver.Remote.__init__
    bstack1l111l1l1l_opy_ = WebDriver.quit
    bstack111ll1ll11_opy_ = WebDriver.close
    bstack11ll1lll1_opy_ = WebDriver.get
    bstack111l1l1l1_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1111ll111l_opy_(CONFIG) and bstack11l11l1l11_opy_():
    if bstack111llllll_opy_() < version.parse(bstack11ll1lll11_opy_):
      logger.error(bstack11ll11ll11_opy_.format(bstack111llllll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11ll1l_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫຫ")) and callable(getattr(RemoteConnection, bstack11ll1l_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬຬ"))):
          bstack111ll1ll1l_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack111ll1ll1l_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack1ll1ll1lll_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1l11ll1ll1_opy_ = Config.getoption
    from _pytest import runner
    bstack1ll1l11l1l_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1111ll1l_opy_)
  try:
    from pytest_bdd import reporting
    bstack1l111ll1l1_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11ll1l_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡴࠦࡲࡶࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࡸ࠭ອ"))
  bstack1l11l1ll11_opy_ = CONFIG.get(bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪຮ"), {}).get(bstack11ll1l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩຯ"))
  bstack1lll111l11_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack111l1l111l_opy_():
      bstack1l11l11111_opy_.invoke(Events.CONNECT, bstack1l11ll111l_opy_())
    platform_index = int(os.environ.get(bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨະ"), bstack11ll1l_opy_ (u"ࠩ࠳ࠫັ")))
  else:
    bstack1l111111ll_opy_(bstack111l1l11ll_opy_)
  os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡘࡗࡊࡘࡎࡂࡏࡈࠫາ")] = CONFIG[bstack11ll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ຳ")]
  os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆࡉࡃࡆࡕࡖࡣࡐࡋ࡙ࠨິ")] = CONFIG[bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩີ")]
  os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪຶ")] = bstack11lllll111_opy_.__str__()
  from _pytest.config import main as bstack1l11ll111_opy_
  bstack1lll111l1l_opy_ = []
  try:
    exit_code = bstack1l11ll111_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack11111111l_opy_()
    if bstack11ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡧࡵࡶࡴࡸ࡟࡭࡫ࡶࡸࠬື") in multiprocessing.current_process().__dict__.keys():
      for bstack1l11lllll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1lll111l1l_opy_.append(bstack1l11lllll_opy_)
    try:
      bstack11l1111ll_opy_ = (bstack1lll111l1l_opy_, int(exit_code))
      bstack1l111111l_opy_.append(bstack11l1111ll_opy_)
    except:
      bstack1l111111l_opy_.append((bstack1lll111l1l_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1lll111l1l_opy_.append({bstack11ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ຸࠧ"): bstack11ll1l_opy_ (u"ࠪࡔࡷࡵࡣࡦࡵࡶࠤູࠬ") + os.environ.get(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ຺࡛ࠫ")), bstack11ll1l_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫົ"): traceback.format_exc(), bstack11ll1l_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬຼ"): int(os.environ.get(bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧຽ")))})
    bstack1l111111l_opy_.append((bstack1lll111l1l_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack11ll1l_opy_ (u"ࠣࡴࡨࡸࡷ࡯ࡥࡴࠤ຾"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack1l1ll11ll_opy_ = e.__class__.__name__
    print(bstack11ll1l_opy_ (u"ࠤࠨࡷ࠿ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡸࡵ࡯ࡰ࡬ࡲ࡬ࠦࡢࡦࡪࡤࡺࡪࠦࡴࡦࡵࡷࠤࠪࡹࠢ຿") % (bstack1l1ll11ll_opy_, e))
    return 1
def bstack1111ll11ll_opy_(arg):
  global bstack1111ll111_opy_
  bstack1l111111ll_opy_(bstack11lllll1l_opy_)
  os.environ[bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫເ")] = str(bstack11ll11l111_opy_)
  retries = bstack1llllll11_opy_.bstack1lllllll1_opy_(CONFIG)
  status_code = 0
  if bstack1llllll11_opy_.bstack1lllll111_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack1111l11ll1_opy_
    status_code = bstack1111l11ll1_opy_(arg)
  if status_code != 0:
    bstack1111ll111_opy_ = status_code
def bstack1ll111lll_opy_():
  logger.info(bstack11ll1lllll_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11ll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪແ"), help=bstack11ll1l_opy_ (u"ࠬࡍࡥ࡯ࡧࡵࡥࡹ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠦࡣࡰࡰࡩ࡭࡬࠭ໂ"))
  parser.add_argument(bstack11ll1l_opy_ (u"࠭࠭ࡶࠩໃ"), bstack11ll1l_opy_ (u"ࠧ࠮࠯ࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫໄ"), help=bstack11ll1l_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡻࡳࡦࡴࡱࡥࡲ࡫ࠧ໅"))
  parser.add_argument(bstack11ll1l_opy_ (u"ࠩ࠰࡯ࠬໆ"), bstack11ll1l_opy_ (u"ࠪ࠱࠲ࡱࡥࡺࠩ໇"), help=bstack11ll1l_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡣࡦࡧࡪࡹࡳࠡ࡭ࡨࡽ່ࠬ"))
  parser.add_argument(bstack11ll1l_opy_ (u"ࠬ࠳ࡦࠨ້"), bstack11ll1l_opy_ (u"࠭࠭࠮ࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮໊ࠫ"), help=bstack11ll1l_opy_ (u"࡚ࠧࡱࡸࡶࠥࡺࡥࡴࡶࠣࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ໋࠭"))
  bstack1ll1l11l11_opy_ = parser.parse_args()
  try:
    bstack1ll11111l_opy_ = bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡨࡧࡱࡩࡷ࡯ࡣ࠯ࡻࡰࡰ࠳ࡹࡡ࡮ࡲ࡯ࡩࠬ໌")
    if bstack1ll1l11l11_opy_.framework and bstack1ll1l11l11_opy_.framework not in (bstack11ll1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩໍ"), bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫ໎")):
      bstack1ll11111l_opy_ = bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠴ࡹ࡮࡮࠱ࡷࡦࡳࡰ࡭ࡧࠪ໏")
    bstack1ll1111111_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1ll11111l_opy_)
    bstack11ll1111ll_opy_ = open(bstack1ll1111111_opy_, bstack11ll1l_opy_ (u"ࠬࡸࠧ໐"))
    bstack1l1l11ll1l_opy_ = bstack11ll1111ll_opy_.read()
    bstack11ll1111ll_opy_.close()
    if bstack1ll1l11l11_opy_.username:
      bstack1l1l11ll1l_opy_ = bstack1l1l11ll1l_opy_.replace(bstack11ll1l_opy_ (u"࡙࠭ࡐࡗࡕࡣ࡚࡙ࡅࡓࡐࡄࡑࡊ࠭໑"), bstack1ll1l11l11_opy_.username)
    if bstack1ll1l11l11_opy_.key:
      bstack1l1l11ll1l_opy_ = bstack1l1l11ll1l_opy_.replace(bstack11ll1l_opy_ (u"࡚ࠧࡑࡘࡖࡤࡇࡃࡄࡇࡖࡗࡤࡑࡅ࡚ࠩ໒"), bstack1ll1l11l11_opy_.key)
    if bstack1ll1l11l11_opy_.framework:
      bstack1l1l11ll1l_opy_ = bstack1l1l11ll1l_opy_.replace(bstack11ll1l_opy_ (u"ࠨ࡛ࡒ࡙ࡗࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ໓"), bstack1ll1l11l11_opy_.framework)
    file_name = bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬ໔")
    file_path = os.path.abspath(file_name)
    bstack1l111ll111_opy_ = open(file_path, bstack11ll1l_opy_ (u"ࠪࡻࠬ໕"))
    bstack1l111ll111_opy_.write(bstack1l1l11ll1l_opy_)
    bstack1l111ll111_opy_.close()
    logger.info(bstack111l1l1ll_opy_)
    try:
      os.environ[bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭໖")] = bstack1ll1l11l11_opy_.framework if bstack1ll1l11l11_opy_.framework != None else bstack11ll1l_opy_ (u"ࠧࠨ໗")
      config = yaml.safe_load(bstack1l1l11ll1l_opy_)
      config[bstack11ll1l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭໘")] = bstack11ll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠭ࡴࡧࡷࡹࡵ࠭໙")
      bstack11lll11ll1_opy_(bstack111ll1lll1_opy_, config)
    except Exception as e:
      logger.debug(bstack111l1l11l_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1l111l1ll1_opy_.format(str(e)))
def bstack11lll11ll1_opy_(bstack1ll1ll1l11_opy_, config, bstack1111l1llll_opy_={}):
  global bstack11lllll111_opy_
  global bstack1l1ll11lll_opy_
  global bstack111ll1l1_opy_
  if not config:
    return
  bstack11llll1l1_opy_ = bstack1111lll1l1_opy_ if not bstack11lllll111_opy_ else (
    bstack11l1ll1111_opy_ if bstack11ll1l_opy_ (u"ࠨࡣࡳࡴࠬ໚") in config else (
        bstack11l1lll111_opy_ if config.get(bstack11ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭໛")) else bstack1ll111l11_opy_
    )
)
  bstack1ll1l1lll1_opy_ = False
  bstack1l1ll1ll1l_opy_ = False
  if bstack11lllll111_opy_ is True:
      if bstack11ll1l_opy_ (u"ࠪࡥࡵࡶࠧໜ") in config:
          bstack1ll1l1lll1_opy_ = True
      else:
          bstack1l1ll1ll1l_opy_ = True
  bstack11111ll1ll_opy_ = bstack1llll11l1l_opy_.bstack11111ll11l_opy_(config, bstack1l1ll11lll_opy_)
  bstack111lll11ll_opy_ = bstack1l1l1l1l1l_opy_()
  data = {
    bstack11ll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ໝ"): config[bstack11ll1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧໞ")],
    bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩໟ"): config[bstack11ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪ໠")],
    bstack11ll1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬ໡"): bstack1ll1ll1l11_opy_,
    bstack11ll1l_opy_ (u"ࠩࡧࡩࡹ࡫ࡣࡵࡧࡧࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭໢"): os.environ.get(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ໣"), bstack1l1ll11lll_opy_),
    bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭໤"): bstack1ll11l111_opy_,
    bstack11ll1l_opy_ (u"ࠬࡵࡰࡵ࡫ࡰࡥࡱࡥࡨࡶࡤࡢࡹࡷࡲࠧ໥"): bstack1111lll11_opy_(),
    bstack11ll1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ໦"): {
      bstack11ll1l_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࡡࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ໧"): str(config[bstack11ll1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ໨")]) if bstack11ll1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ໩") in config else bstack11ll1l_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦ໪"),
      bstack11ll1l_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࡜ࡥࡳࡵ࡬ࡳࡳ࠭໫"): sys.version,
      bstack11ll1l_opy_ (u"ࠬࡸࡥࡧࡧࡵࡶࡪࡸࠧ໬"): bstack111ll1llll_opy_(os.environ.get(bstack11ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ໭"), bstack1l1ll11lll_opy_)),
      bstack11ll1l_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩ໮"): bstack11ll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ໯"),
      bstack11ll1l_opy_ (u"ࠩࡳࡶࡴࡪࡵࡤࡶࠪ໰"): bstack11llll1l1_opy_,
      bstack11ll1l_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࡣࡲࡧࡰࠨ໱"): bstack11111ll1ll_opy_,
      bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡤࡻࡵࡪࡦࠪ໲"): os.environ[bstack11ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ໳")],
      bstack11ll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ໴"): os.environ.get(bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ໵"), bstack1l1ll11lll_opy_),
      bstack11ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ໶"): bstack11111l1111_opy_(os.environ.get(bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ໷"), bstack1l1ll11lll_opy_)),
      bstack11ll1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ໸"): bstack111lll11ll_opy_.get(bstack11ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ໹")),
      bstack11ll1l_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ໺"): bstack111lll11ll_opy_.get(bstack11ll1l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧ໻")),
      bstack11ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ໼"): config[bstack11ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ໽")] if config[bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ໾")] else bstack11ll1l_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦ໿"),
      bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ༀ"): str(config[bstack11ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ༁")]) if bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ༂") in config else bstack11ll1l_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࠣ༃"),
      bstack11ll1l_opy_ (u"ࠨࡱࡶࠫ༄"): sys.platform,
      bstack11ll1l_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫ༅"): socket.gethostname(),
      bstack11ll1l_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ༆"): bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭༇"))
    }
  }
  if not bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ༈")) is None:
    data[bstack11ll1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ༉")][bstack11ll1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡏࡨࡸࡦࡪࡡࡵࡣࠪ༊")] = {
      bstack11ll1l_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨ་"): bstack11ll1l_opy_ (u"ࠩࡸࡷࡪࡸ࡟࡬࡫࡯ࡰࡪࡪࠧ༌"),
      bstack11ll1l_opy_ (u"ࠪࡷ࡮࡭࡮ࡢ࡮ࠪ།"): bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ༎")),
      bstack11ll1l_opy_ (u"ࠬࡹࡩࡨࡰࡤࡰࡓࡻ࡭ࡣࡧࡵࠫ༏"): bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡎࡰࠩ༐"))
    }
  if bstack1ll1ll1l11_opy_ == bstack1l1lll111_opy_:
    data[bstack11ll1l_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵࠪ༑")][bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡃࡰࡰࡩ࡭࡬࠭༒")] = bstack111ll11ll1_opy_(config)
    data[bstack11ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ༓")][bstack11ll1l_opy_ (u"ࠪ࡭ࡸࡖࡥࡳࡥࡼࡅࡺࡺ࡯ࡆࡰࡤࡦࡱ࡫ࡤࠨ༔")] = percy.bstack11ll1l11l_opy_
    data[bstack11ll1l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ༕")][bstack11ll1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࡆࡺ࡯࡬ࡥࡋࡧࠫ༖")] = percy.percy_build_id
  if not bstack1llllll11_opy_.bstack11l1ll11ll_opy_(CONFIG):
    data[bstack11ll1l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ༗")][bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ༘ࠫ")] = bstack1llllll11_opy_.bstack11l1ll11ll_opy_(CONFIG)
  bstack1llllllll_opy_ = bstack1lll1l11l_opy_.bstack111111ll_opy_(CONFIG, logger)
  bstack111l1111_opy_ = bstack1llllll11_opy_.bstack111111ll_opy_(config=CONFIG)
  if bstack1llllllll_opy_ is not None and bstack111l1111_opy_ is not None and bstack111l1111_opy_.bstack1lll11l1l_opy_():
    data[bstack11ll1l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶ༙ࠫ")][bstack111l1111_opy_.bstack1l1lllll1_opy_()] = bstack1llllllll_opy_.bstack111l11lll_opy_()
  update(data[bstack11ll1l_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ༚")], bstack1111l1llll_opy_)
  try:
    response = bstack1l1llllll_opy_(bstack11ll1l_opy_ (u"ࠪࡔࡔ࡙ࡔࠨ༛"), bstack1l1lll1l11_opy_(bstack11l11ll11_opy_), data, {
      bstack11ll1l_opy_ (u"ࠫࡦࡻࡴࡩࠩ༜"): (config[bstack11ll1l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ༝")], config[bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ༞")])
    })
    if response:
      logger.debug(bstack11111l111_opy_.format(bstack1ll1ll1l11_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1l11l11lll_opy_.format(str(e)))
def bstack111ll1llll_opy_(framework):
  return bstack11ll1l_opy_ (u"ࠢࡼࡿ࠰ࡴࡾࡺࡨࡰࡰࡤ࡫ࡪࡴࡴ࠰ࡽࢀࠦ༟").format(str(framework), __version__) if framework else bstack11ll1l_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡢࡩࡨࡲࡹ࠵ࡻࡾࠤ༠").format(
    __version__)
def bstack1l111l11l_opy_():
  global CONFIG
  global bstack1l1l111l11_opy_
  if bool(CONFIG):
    return
  try:
    bstack1l11l111ll_opy_()
    logger.debug(bstack1lllllll11_opy_.format(str(CONFIG)))
    bstack1l1l111l11_opy_ = bstack1l11111111_opy_.configure_logger(CONFIG, bstack1l1l111l11_opy_)
    bstack1111l1l11_opy_()
  except Exception as e:
    logger.error(bstack11ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࡷࡳ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࠨ༡") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1l1ll111l_opy_
  atexit.register(bstack111l1ll11l_opy_)
  signal.signal(signal.SIGINT, bstack11lllll11l_opy_)
  signal.signal(signal.SIGTERM, bstack11lllll11l_opy_)
def bstack1l1ll111l_opy_(exctype, value, traceback):
  global bstack1l1lll1ll_opy_
  try:
    for driver in bstack1l1lll1ll_opy_:
      bstack1l11ll11l1_opy_(driver, bstack11ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ༢"), bstack11ll1l_opy_ (u"ࠦࡘ࡫ࡳࡴ࡫ࡲࡲࠥ࡬ࡡࡪ࡮ࡨࡨࠥࡽࡩࡵࡪ࠽ࠤࡡࡴࠢ༣") + str(value))
  except Exception:
    pass
  logger.info(bstack11l1111l1_opy_)
  bstack1111ll1lll_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1111ll1lll_opy_(message=bstack11ll1l_opy_ (u"ࠬ࠭༤"), bstack1l111l1lll_opy_ = False):
  global CONFIG
  bstack1l1l1l111_opy_ = bstack11ll1l_opy_ (u"࠭ࡧ࡭ࡱࡥࡥࡱࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠨ༥") if bstack1l111l1lll_opy_ else bstack11ll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭༦")
  try:
    if message:
      bstack1111l1llll_opy_ = {
        bstack1l1l1l111_opy_ : str(message)
      }
      bstack11lll11ll1_opy_(bstack1l1lll111_opy_, CONFIG, bstack1111l1llll_opy_)
    else:
      bstack11lll11ll1_opy_(bstack1l1lll111_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack11ll111111_opy_.format(str(e)))
def bstack1l1lllllll_opy_(bstack1l111111l1_opy_, size):
  bstack1l11l11l1l_opy_ = []
  while len(bstack1l111111l1_opy_) > size:
    bstack11ll11l1l1_opy_ = bstack1l111111l1_opy_[:size]
    bstack1l11l11l1l_opy_.append(bstack11ll11l1l1_opy_)
    bstack1l111111l1_opy_ = bstack1l111111l1_opy_[size:]
  bstack1l11l11l1l_opy_.append(bstack1l111111l1_opy_)
  return bstack1l11l11l1l_opy_
def bstack1l1l11l1l_opy_(args):
  if bstack11ll1l_opy_ (u"ࠨ࠯ࡰࠫ༧") in args and bstack11ll1l_opy_ (u"ࠩࡳࡨࡧ࠭༨") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack11111l1l11_opy_, stage=STAGE.bstack1ll11l1l1l_opy_)
def run_on_browserstack(bstack11l111lll1_opy_=None, bstack1l111111l_opy_=None, bstack1ll1l1ll1l_opy_=False):
  global CONFIG
  global bstack11llll11l_opy_
  global bstack11ll11l111_opy_
  global bstack1l1ll11lll_opy_
  global bstack111ll1l1_opy_
  bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠪࠫ༩")
  bstack1l1l1ll11_opy_(bstack1111111ll1_opy_, logger)
  if bstack11l111lll1_opy_ and isinstance(bstack11l111lll1_opy_, str):
    bstack11l111lll1_opy_ = eval(bstack11l111lll1_opy_)
  if bstack11l111lll1_opy_:
    CONFIG = bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫ༪")]
    bstack11llll11l_opy_ = bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭༫")]
    bstack11ll11l111_opy_ = bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ༬")]
    bstack111ll1l1_opy_.set_property(bstack11ll1l_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ༭"), bstack11ll11l111_opy_)
    bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ༮")
  bstack111ll1l1_opy_.set_property(bstack11ll1l_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ༯"), uuid4().__str__())
  logger.info(bstack11ll1l_opy_ (u"ࠪࡗࡉࡑࠠࡳࡷࡱࠤࡸࡺࡡࡳࡶࡨࡨࠥࡽࡩࡵࡪࠣ࡭ࡩࡀࠠࠨ༰") + bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠫࡸࡪ࡫ࡓࡷࡱࡍࡩ࠭༱")));
  logger.debug(bstack11ll1l_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪ࠽ࠨ༲") + bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ༳")))
  if not bstack1ll1l1ll1l_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack11l1l11111_opy_)
      return
    if sys.argv[1] == bstack11ll1l_opy_ (u"ࠧ࠮࠯ࡹࡩࡷࡹࡩࡰࡰࠪ༴") or sys.argv[1] == bstack11ll1l_opy_ (u"ࠨ࠯ࡹ༵ࠫ"):
      logger.info(bstack11ll1l_opy_ (u"ࠩࡅࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡒࡼࡸ࡭ࡵ࡮ࠡࡕࡇࡏࠥࡼࡻࡾࠩ༶").format(__version__))
      return
    if sys.argv[1] == bstack11ll1l_opy_ (u"ࠪࡷࡪࡺࡵࡱ༷ࠩ"):
      bstack1ll111lll_opy_()
      return
  args = sys.argv
  bstack1l111l11l_opy_()
  global bstack1l11lll1l_opy_
  global bstack1lll11l1l1_opy_
  global bstack1lll111l11_opy_
  global bstack1111l11l11_opy_
  global bstack1l111l1111_opy_
  global bstack1l11l1ll11_opy_
  global bstack11111l11l_opy_
  global bstack11lll111l_opy_
  global bstack11l11l1l1_opy_
  global bstack1l1ll1l11_opy_
  global bstack111lll1l11_opy_
  bstack1lll11l1l1_opy_ = len(CONFIG.get(bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ༸"), []))
  if not bstack1ll1l1ll1_opy_:
    if args[1] == bstack11ll1l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲ༹ࠬ") or args[1] == bstack11ll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧ༺"):
      bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ༻")
      args = args[2:]
    elif args[1] == bstack11ll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ༼"):
      bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ༽")
      args = args[2:]
    elif args[1] == bstack11ll1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ༾"):
      bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ༿")
      args = args[2:]
    elif args[1] == bstack11ll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱ࠭ཀ"):
      bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧཁ")
      args = args[2:]
    elif args[1] == bstack11ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧག"):
      bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨགྷ")
      args = args[2:]
    elif args[1] == bstack11ll1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩང"):
      bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪཅ")
      args = args[2:]
    else:
      if not bstack11ll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧཆ") in CONFIG or str(CONFIG[bstack11ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨཇ")]).lower() in [bstack11ll1l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭཈"), bstack11ll1l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨཉ")]:
        bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨཊ")
        args = args[1:]
      elif str(CONFIG[bstack11ll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬཋ")]).lower() == bstack11ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩཌ"):
        bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪཌྷ")
        args = args[1:]
      elif str(CONFIG[bstack11ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨཎ")]).lower() == bstack11ll1l_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬཏ"):
        bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ཐ")
        args = args[1:]
      elif str(CONFIG[bstack11ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫད")]).lower() == bstack11ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩདྷ"):
        bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪན")
        args = args[1:]
      elif str(CONFIG[bstack11ll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧཔ")]).lower() == bstack11ll1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬཕ"):
        bstack1ll1l1ll1_opy_ = bstack11ll1l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭བ")
        args = args[1:]
      else:
        os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩབྷ")] = bstack1ll1l1ll1_opy_
        bstack1l111llll_opy_(bstack111l11l11_opy_)
  os.environ[bstack11ll1l_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩམ")] = bstack1ll1l1ll1_opy_
  bstack1l1ll11lll_opy_ = bstack1ll1l1ll1_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1ll11llll_opy_ = bstack111ll1111_opy_[bstack11ll1l_opy_ (u"ࠩࡓ࡝࡙ࡋࡓࡕ࠯ࡅࡈࡉ࠭ཙ")] if bstack1ll1l1ll1_opy_ == bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪཚ") and bstack1111ll1ll_opy_() else bstack1ll1l1ll1_opy_
      bstack1l11l11111_opy_.invoke(Events.bstack111111ll1_opy_, bstack111l11111l_opy_(
        sdk_version=__version__,
        path_config=bstack111l111l1_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1ll11llll_opy_,
        frameworks=[bstack1ll11llll_opy_],
        framework_versions={
          bstack1ll11llll_opy_: bstack11111l1111_opy_(bstack11ll1l_opy_ (u"ࠫࡗࡵࡢࡰࡶࠪཛ") if bstack1ll1l1ll1_opy_ in [bstack11ll1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫཛྷ"), bstack11ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬཝ"), bstack11ll1l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨཞ")] else bstack1ll1l1ll1_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack11ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥཟ"), None):
        CONFIG[bstack11ll1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦའ")] = cli.config.get(bstack11ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧཡ"), None)
    except Exception as e:
      bstack1l11l11111_opy_.invoke(Events.bstack1llll1ll11_opy_, e.__traceback__, 1)
    if bstack11ll11l111_opy_:
      CONFIG[bstack11ll1l_opy_ (u"ࠦࡦࡶࡰࠣར")] = cli.config[bstack11ll1l_opy_ (u"ࠧࡧࡰࡱࠤལ")]
      logger.info(bstack11l1111l1l_opy_.format(CONFIG[bstack11ll1l_opy_ (u"࠭ࡡࡱࡲࠪཤ")]))
  else:
    bstack1l11l11111_opy_.clear()
  global bstack1l11l1l11l_opy_
  global bstack1llll111ll_opy_
  if bstack11l111lll1_opy_:
    try:
      bstack1ll11ll111_opy_ = datetime.datetime.now()
      os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩཥ")] = bstack1ll1l1ll1_opy_
      bstack11lll11ll1_opy_(bstack11l11l11ll_opy_, CONFIG)
      cli.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠣࡪࡷࡸࡵࡀࡳࡥ࡭ࡢࡸࡪࡹࡴࡠࡣࡷࡸࡪࡳࡰࡵࡧࡧࠦས"), datetime.datetime.now() - bstack1ll11ll111_opy_)
    except Exception as e:
      logger.debug(bstack1ll11ll1ll_opy_.format(str(e)))
  global bstack111l111ll1_opy_
  global bstack1l111l1l1l_opy_
  global bstack11ll11l11_opy_
  global bstack1ll111ll1l_opy_
  global bstack11l1l11lll_opy_
  global bstack11ll1l11l1_opy_
  global bstack11l1l1111_opy_
  global bstack111l1ll111_opy_
  global bstack11ll1l1lll_opy_
  global bstack1ll1l11111_opy_
  global bstack111l11111_opy_
  global bstack111ll1ll11_opy_
  global bstack111l11llll_opy_
  global bstack11lllllll1_opy_
  global bstack11ll1lll1_opy_
  global bstack111ll1ll1l_opy_
  global bstack1l11ll1ll1_opy_
  global bstack1ll1l11l1l_opy_
  global bstack1l1l1lll1_opy_
  global bstack1l111ll1l1_opy_
  global bstack111l1l1l1_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack111l111ll1_opy_ = webdriver.Remote.__init__
    bstack1l111l1l1l_opy_ = WebDriver.quit
    bstack111ll1ll11_opy_ = WebDriver.close
    bstack11ll1lll1_opy_ = WebDriver.get
    bstack111l1l1l1_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1l11l1l11l_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack11l1ll1l11_opy_
    bstack1llll111ll_opy_ = bstack11l1ll1l11_opy_()
  except Exception as e:
    pass
  try:
    global bstack11l1ll1ll_opy_
    from QWeb.keywords import browser
    bstack11l1ll1ll_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1111ll111l_opy_(CONFIG) and bstack11l11l1l11_opy_():
    if bstack111llllll_opy_() < version.parse(bstack11ll1lll11_opy_):
      logger.error(bstack11ll11ll11_opy_.format(bstack111llllll_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11ll1l_opy_ (u"ࠩࡢ࡫ࡪࡺ࡟ࡱࡴࡲࡼࡾࡥࡵࡳ࡮ࠪཧ")) and callable(getattr(RemoteConnection, bstack11ll1l_opy_ (u"ࠪࡣ࡬࡫ࡴࡠࡲࡵࡳࡽࡿ࡟ࡶࡴ࡯ࠫཨ"))):
          RemoteConnection._get_proxy_url = bstack1ll1ll1ll_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack1ll1ll1ll_opy_
      except Exception as e:
        logger.error(bstack1ll1ll1lll_opy_.format(str(e)))
  if not CONFIG.get(bstack11ll1l_opy_ (u"ࠫࡩ࡯ࡳࡢࡤ࡯ࡩࡆࡻࡴࡰࡅࡤࡴࡹࡻࡲࡦࡎࡲ࡫ࡸ࠭ཀྵ"), False) and not bstack11l111lll1_opy_:
    logger.info(bstack1l1l1llll_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack11ll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩཪ") in CONFIG and str(CONFIG[bstack11ll1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪཫ")]).lower() != bstack11ll1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ཬ"):
      bstack111ll1111l_opy_()
    elif bstack1ll1l1ll1_opy_ != bstack11ll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ཭") or (bstack1ll1l1ll1_opy_ == bstack11ll1l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ཮") and not bstack11l111lll1_opy_):
      bstack1l1lllll1l_opy_()
  if (bstack1ll1l1ll1_opy_ in [bstack11ll1l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ཯"), bstack11ll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ཰"), bstack11ll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱཱ࠭")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack11ll1l111l_opy_
        bstack11ll1l11l1_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1lll11ll11_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack11l1l11lll_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1l1l11l1ll_opy_ + str(e))
    except Exception as e:
      bstack1l11ll1111_opy_(e, bstack1lll11ll11_opy_)
    if bstack1ll1l1ll1_opy_ != bstack11ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲིࠧ"):
      bstack1l111l111_opy_()
    bstack11ll11l11_opy_ = Output.start_test
    bstack1ll111ll1l_opy_ = Output.end_test
    bstack11l1l1111_opy_ = TestStatus.__init__
    bstack11ll1l1lll_opy_ = pabot._run
    bstack1ll1l11111_opy_ = QueueItem.__init__
    bstack111l11111_opy_ = pabot._create_command_for_execution
    bstack1l1l1lll1_opy_ = pabot._report_results
  if bstack1ll1l1ll1_opy_ == bstack11ll1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ཱིࠧ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l11ll1111_opy_(e, bstack1ll111llll_opy_)
    bstack111l11llll_opy_ = Runner.run_hook
    bstack11lllllll1_opy_ = Step.run
  if bstack1ll1l1ll1_opy_ == bstack11ll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨུ"):
    try:
      from _pytest.config import Config
      bstack1l11ll1ll1_opy_ = Config.getoption
      from _pytest import runner
      bstack1ll1l11l1l_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1111ll1l_opy_)
    try:
      from pytest_bdd import reporting
      bstack1l111ll1l1_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11ll1l_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵཱུࠪ"))
  try:
    framework_name = bstack11ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩྲྀ") if bstack1ll1l1ll1_opy_ in [bstack11ll1l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪཷ"), bstack11ll1l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫླྀ"), bstack11ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧཹ")] else bstack11lll1llll_opy_(bstack1ll1l1ll1_opy_)
    bstack11lll11l1l_opy_ = {
      bstack11ll1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠨེ"): bstack11ll1l_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴ࠮ࡥࡸࡧࡺࡳࡢࡦࡴཻࠪ") if bstack1ll1l1ll1_opy_ == bstack11ll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵོࠩ") and bstack1111ll1ll_opy_() else framework_name,
      bstack11ll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴཽࠧ"): bstack11111l1111_opy_(framework_name),
      bstack11ll1l_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩཾ"): __version__,
      bstack11ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡷࡶࡩࡩ࠭ཿ"): bstack1ll1l1ll1_opy_
    }
    if bstack1ll1l1ll1_opy_ in bstack1l1l1l1l11_opy_ + bstack111ll1l11_opy_:
      if bstack1lllll1l1_opy_.bstack11111ll111_opy_(CONFIG):
        if bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸྀ࠭") in CONFIG:
          os.environ[bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨཱྀ")] = os.getenv(bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩྂ"), json.dumps(CONFIG[bstack11ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩྃ")]))
          CONFIG[bstack11ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵ྄ࠪ")].pop(bstack11ll1l_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ྅"), None)
          CONFIG[bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ྆")].pop(bstack11ll1l_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ྇"), None)
        bstack11lll11l1l_opy_[bstack11ll1l_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧྈ")] = {
          bstack11ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ྉ"): bstack11ll1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫྊ"),
          bstack11ll1l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫྋ"): str(bstack111llllll_opy_())
        }
    if bstack1ll1l1ll1_opy_ not in [bstack11ll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬྌ")] and not cli.is_running():
      bstack1lll1l1l11_opy_, bstack11ll1ll11_opy_ = bstack1l1l1lll_opy_.launch(CONFIG, bstack11lll11l1l_opy_)
      if bstack11ll1ll11_opy_.get(bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬྍ")) is not None and bstack1lllll1l1_opy_.bstack111l1111l_opy_(CONFIG) is None:
        value = bstack11ll1ll11_opy_[bstack11ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ྎ")].get(bstack11ll1l_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨྏ"))
        if value is not None:
            CONFIG[bstack11ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨྐ")] = value
        else:
          logger.debug(bstack11ll1l_opy_ (u"ࠤࡑࡳࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡪࡡࡵࡣࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢྑ"))
  except Exception as e:
    logger.debug(bstack1llll1l1ll_opy_.format(bstack11ll1l_opy_ (u"ࠪࡘࡪࡹࡴࡉࡷࡥࠫྒ"), str(e)))
  if bstack1ll1l1ll1_opy_ == bstack11ll1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫྒྷ"):
    bstack1lll111l11_opy_ = True
    if bstack11l111lll1_opy_ and bstack1ll1l1ll1l_opy_:
      bstack1l11l1ll11_opy_ = CONFIG.get(bstack11ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩྔ"), {}).get(bstack11ll1l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨྕ"))
      bstack1l111111ll_opy_(bstack1ll111l111_opy_)
    elif bstack11l111lll1_opy_:
      bstack1l11l1ll11_opy_ = CONFIG.get(bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫྖ"), {}).get(bstack11ll1l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪྗ"))
      global bstack1l1lll1ll_opy_
      try:
        if bstack1l1l11l1l_opy_(bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬ྘")]) and multiprocessing.current_process().name == bstack11ll1l_opy_ (u"ࠪ࠴ࠬྙ"):
          bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྚ")].remove(bstack11ll1l_opy_ (u"ࠬ࠳࡭ࠨྛ"))
          bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྜ")].remove(bstack11ll1l_opy_ (u"ࠧࡱࡦࡥࠫྜྷ"))
          bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྞ")] = bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྟ")][0]
          with open(bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྠ")], bstack11ll1l_opy_ (u"ࠫࡷ࠭ྡ")) as f:
            file_content = f.read()
          bstack111111lll1_opy_ = bstack11ll1l_opy_ (u"ࠧࠨࠢࡧࡴࡲࡱࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡪ࡫ࠡ࡫ࡰࡴࡴࡸࡴࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨ࠿ࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡥࠩࡽࢀ࠭ࡀࠦࡦࡳࡱࡰࠤࡵࡪࡢࠡ࡫ࡰࡴࡴࡸࡴࠡࡒࡧࡦࡀࠦ࡯ࡨࡡࡧࡦࠥࡃࠠࡑࡦࡥ࠲ࡩࡵ࡟ࡣࡴࡨࡥࡰࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡨࡪ࡬ࠠ࡮ࡱࡧࡣࡧࡸࡥࡢ࡭ࠫࡷࡪࡲࡦ࠭ࠢࡤࡶ࡬࠲ࠠࡵࡧࡰࡴࡴࡸࡡࡳࡻࠣࡁࠥ࠶ࠩ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡴࡼ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡧࡲࡨࠢࡀࠤࡸࡺࡲࠩ࡫ࡱࡸ࠭ࡧࡲࡨࠫ࠮࠵࠵࠯ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡫ࡸࡤࡧࡳࡸࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡣࡶࠤࡪࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡱࡣࡶࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡳ࡬ࡥࡤࡣࠪࡶࡩࡱ࡬ࠬࡢࡴࡪ࠰ࡹ࡫࡭ࡱࡱࡵࡥࡷࡿࠩࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡕࡪࡢ࠯ࡦࡲࡣࡧࠦ࠽ࠡ࡯ࡲࡨࡤࡨࡲࡦࡣ࡮ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡑࡦࡥ࠲ࡩࡵ࡟ࡣࡴࡨࡥࡰࠦ࠽ࠡ࡯ࡲࡨࡤࡨࡲࡦࡣ࡮ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡑࡦࡥࠬ࠮࠴ࡳࡦࡶࡢࡸࡷࡧࡣࡦࠪࠬࡠࡳࠨࠢࠣྡྷ").format(str(bstack11l111lll1_opy_))
          bstack111l11l1l1_opy_ = bstack111111lll1_opy_ + file_content
          bstack11lll1l11l_opy_ = bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྣ")] + bstack11ll1l_opy_ (u"ࠧࡠࡤࡶࡸࡦࡩ࡫ࡠࡶࡨࡱࡵ࠴ࡰࡺࠩྤ")
          with open(bstack11lll1l11l_opy_, bstack11ll1l_opy_ (u"ࠨࡹࠪྥ")):
            pass
          with open(bstack11lll1l11l_opy_, bstack11ll1l_opy_ (u"ࠤࡺ࠯ࠧྦ")) as f:
            f.write(bstack111l11l1l1_opy_)
          import subprocess
          process_data = subprocess.run([bstack11ll1l_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࠥྦྷ"), bstack11lll1l11l_opy_])
          if os.path.exists(bstack11lll1l11l_opy_):
            os.unlink(bstack11lll1l11l_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack1l1l11l1l_opy_(bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྨ")]):
            bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྩ")].remove(bstack11ll1l_opy_ (u"࠭࠭࡮ࠩྪ"))
            bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྫ")].remove(bstack11ll1l_opy_ (u"ࠨࡲࡧࡦࠬྫྷ"))
            bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྭ")] = bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྮ")][0]
          bstack1l111111ll_opy_(bstack1ll111l111_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྯ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11ll1l_opy_ (u"ࠬࡥ࡟࡯ࡣࡰࡩࡤࡥࠧྰ")] = bstack11ll1l_opy_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨྱ")
          mod_globals[bstack11ll1l_opy_ (u"ࠧࡠࡡࡩ࡭ࡱ࡫࡟ࡠࠩྲ")] = os.path.abspath(bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫླ")])
          exec(open(bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྴ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11ll1l_opy_ (u"ࠪࡇࡦࡻࡧࡩࡶࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠪྵ").format(str(e)))
          for driver in bstack1l1lll1ll_opy_:
            bstack1l111111l_opy_.append({
              bstack11ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩྶ"): bstack11l111lll1_opy_[bstack11ll1l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྷ")],
              bstack11ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬྸ"): str(e),
              bstack11ll1l_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭ྐྵ"): multiprocessing.current_process().name
            })
            bstack1l11ll11l1_opy_(driver, bstack11ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨྺ"), bstack11ll1l_opy_ (u"ࠤࡖࡩࡸࡹࡩࡰࡰࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧྻ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l1lll1ll_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11ll11l111_opy_, CONFIG, logger)
      bstack1111l11ll_opy_()
      bstack11lll11lll_opy_()
      percy.bstack1l1111lll1_opy_()
      bstack111ll11l_opy_ = {
        bstack11ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྼ"): args[0],
        bstack11ll1l_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫ྽"): CONFIG,
        bstack11ll1l_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭྾"): bstack11llll11l_opy_,
        bstack11ll1l_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ྿"): bstack11ll11l111_opy_
      }
      if bstack11ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿀") in CONFIG:
        bstack1l11lll11l_opy_ = bstack11l11l111l_opy_(args, logger, CONFIG, bstack11lllll111_opy_, bstack1lll11l1l1_opy_)
        bstack11lll111l_opy_ = bstack1l11lll11l_opy_.bstack1lll1l1l1_opy_(run_on_browserstack, bstack111ll11l_opy_, bstack1l1l11l1l_opy_(args))
      else:
        if bstack1l1l11l1l_opy_(args):
          bstack111ll11l_opy_[bstack11ll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫ࿁")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack111ll11l_opy_,))
          test.start()
          test.join()
        else:
          bstack1l111111ll_opy_(bstack1ll111l111_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11ll1l_opy_ (u"ࠩࡢࡣࡳࡧ࡭ࡦࡡࡢࠫ࿂")] = bstack11ll1l_opy_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣࠬ࿃")
          mod_globals[bstack11ll1l_opy_ (u"ࠫࡤࡥࡦࡪ࡮ࡨࡣࡤ࠭࿄")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1ll1l1ll1_opy_ == bstack11ll1l_opy_ (u"ࠬࡶࡡࡣࡱࡷࠫ࿅") or bstack1ll1l1ll1_opy_ == bstack11ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸ࿆ࠬ"):
    percy.init(bstack11ll11l111_opy_, CONFIG, logger)
    percy.bstack1l1111lll1_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l11ll1111_opy_(e, bstack1lll11ll11_opy_)
    bstack1111l11ll_opy_()
    bstack1l111111ll_opy_(bstack11llll11l1_opy_)
    if bstack11lllll111_opy_:
      bstack1l11l11ll_opy_(bstack11llll11l1_opy_, args)
      if bstack11ll1l_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬ࿇") in args:
        i = args.index(bstack11ll1l_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭࿈"))
        args.pop(i)
        args.pop(i)
      if bstack11ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ࿉") not in CONFIG:
        CONFIG[bstack11ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭࿊")] = [{}]
        bstack1lll11l1l1_opy_ = 1
      if bstack1l11lll1l_opy_ == 0:
        bstack1l11lll1l_opy_ = 1
      args.insert(0, str(bstack1l11lll1l_opy_))
      args.insert(0, str(bstack11ll1l_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ࿋")))
    if bstack1l1l1lll_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack11l1l1l111_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1111l111l1_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11ll1l_opy_ (u"ࠧࡘࡏࡃࡑࡗࡣࡔࡖࡔࡊࡑࡑࡗࠧ࿌"),
        ).parse_args(bstack11l1l1l111_opy_)
        bstack1l1l1111ll_opy_ = args.index(bstack11l1l1l111_opy_[0]) if len(bstack11l1l1l111_opy_) > 0 else len(args)
        args.insert(bstack1l1l1111ll_opy_, str(bstack11ll1l_opy_ (u"࠭࠭࠮࡮࡬ࡷࡹ࡫࡮ࡦࡴࠪ࿍")))
        args.insert(bstack1l1l1111ll_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡳࡱࡥࡳࡹࡥ࡬ࡪࡵࡷࡩࡳ࡫ࡲ࠯ࡲࡼࠫ࿎"))))
        if bstack1llllll11_opy_.bstack1lllll111_opy_(CONFIG):
          args.insert(bstack1l1l1111ll_opy_, str(bstack11ll1l_opy_ (u"ࠨ࠯࠰ࡰ࡮ࡹࡴࡦࡰࡨࡶࠬ࿏")))
          args.insert(bstack1l1l1111ll_opy_ + 1, str(bstack11ll1l_opy_ (u"ࠩࡕࡩࡹࡸࡹࡇࡣ࡬ࡰࡪࡪ࠺ࡼࡿࠪ࿐").format(bstack1llllll11_opy_.bstack1lllllll1_opy_(CONFIG))))
        if bstack1ll11lll11_opy_(os.environ.get(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠨ࿑"))) and str(os.environ.get(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠨ࿒"), bstack11ll1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ࿓"))) != bstack11ll1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫ࿔"):
          for bstack111l1l1lll_opy_ in bstack1111l111l1_opy_:
            args.remove(bstack111l1l1lll_opy_)
          test_files = os.environ.get(bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠫ࿕")).split(bstack11ll1l_opy_ (u"ࠨ࠮ࠪ࿖"))
          for bstack111lll11l1_opy_ in test_files:
            args.append(bstack111lll11l1_opy_)
      except Exception as e:
        logger.error(bstack11ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡢࡶࡷࡥࡨ࡮ࡩ࡯ࡩࠣࡰ࡮ࡹࡴࡦࡰࡨࡶࠥ࡬࡯ࡳࠢࡾࢁ࠳ࠦࡅࡳࡴࡲࡶࠥ࠳ࠠࡼࡿࠥ࿗").format(bstack1l11llll1_opy_, e))
    pabot.main(args)
  elif bstack1ll1l1ll1_opy_ == bstack11ll1l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ࿘"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l11ll1111_opy_(e, bstack1lll11ll11_opy_)
    for a in args:
      if bstack11ll1l_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚ࠪ࿙") in a:
        bstack1l111l1111_opy_ = int(a.split(bstack11ll1l_opy_ (u"ࠬࡀࠧ࿚"))[1])
      if bstack11ll1l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡊࡅࡇࡎࡒࡇࡆࡒࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪ࿛") in a:
        bstack1l11l1ll11_opy_ = str(a.split(bstack11ll1l_opy_ (u"ࠧ࠻ࠩ࿜"))[1])
      if bstack11ll1l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡄࡎࡌࡅࡗࡍࡓࠨ࿝") in a:
        bstack11111l11l_opy_ = str(a.split(bstack11ll1l_opy_ (u"ࠩ࠽ࠫ࿞"))[1])
    bstack1l11lll11_opy_ = None
    if bstack11ll1l_opy_ (u"ࠪ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤ࡯ࡴࡦ࡯ࡢ࡭ࡳࡪࡥࡹࠩ࿟") in args:
      i = args.index(bstack11ll1l_opy_ (u"ࠫ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠪ࿠"))
      args.pop(i)
      bstack1l11lll11_opy_ = args.pop(i)
    if bstack1l11lll11_opy_ is not None:
      global bstack1l1ll11l1l_opy_
      bstack1l1ll11l1l_opy_ = bstack1l11lll11_opy_
      bstack1l111l1111_opy_ = int(bstack1l11lll11_opy_)
    bstack1l111111ll_opy_(bstack11llll11l1_opy_)
    run_cli(args)
    if bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵࠩ࿡") in multiprocessing.current_process().__dict__.keys():
      for bstack1l11lllll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l111111l_opy_.append(bstack1l11lllll_opy_)
  elif bstack1ll1l1ll1_opy_ == bstack11ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭࿢"):
    bstack1l111l11l1_opy_ = bstack1111llll_opy_(args, logger, CONFIG, bstack11lllll111_opy_)
    bstack1l111l11l1_opy_.bstack1111l1l1_opy_()
    bstack1111l11ll_opy_()
    bstack1111l11l11_opy_ = True
    bstack1l1ll1l11_opy_ = bstack1l111l11l1_opy_.bstack11111111_opy_()
    bstack1l111l11l1_opy_.bstack111ll11l_opy_(bstack1lll1l1ll1_opy_)
    bstack1l111l11l1_opy_.bstack111l1l11_opy_()
    bstack11l11111ll_opy_(bstack1ll1l1ll1_opy_, CONFIG, bstack1l111l11l1_opy_.bstack1lll111l1_opy_())
    bstack11111l11l1_opy_ = bstack1l111l11l1_opy_.bstack1lll1l1l1_opy_(bstack11lll1l1l_opy_, {
      bstack11ll1l_opy_ (u"ࠧࡉࡗࡅࡣ࡚ࡘࡌࠨ࿣"): bstack11llll11l_opy_,
      bstack11ll1l_opy_ (u"ࠨࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ࿤"): bstack11ll11l111_opy_,
      bstack11ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡘࡘࡔࡓࡁࡕࡋࡒࡒࠬ࿥"): bstack11lllll111_opy_
    })
    try:
      bstack1lll111l1l_opy_, bstack11ll1ll111_opy_ = map(list, zip(*bstack11111l11l1_opy_))
      bstack11l11l1l1_opy_ = bstack1lll111l1l_opy_[0]
      for status_code in bstack11ll1ll111_opy_:
        if status_code != 0:
          bstack111lll1l11_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11ll1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡢࡸࡨࠤࡪࡸࡲࡰࡴࡶࠤࡦࡴࡤࠡࡵࡷࡥࡹࡻࡳࠡࡥࡲࡨࡪ࠴ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࠾ࠥࢁࡽࠣ࿦").format(str(e)))
  elif bstack1ll1l1ll1_opy_ == bstack11ll1l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ࿧"):
    try:
      from behave.__main__ import main as bstack1111l11ll1_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l11ll1111_opy_(e, bstack1ll111llll_opy_)
    bstack1111l11ll_opy_()
    bstack1111l11l11_opy_ = True
    bstack1111l111_opy_ = 1
    if bstack11ll1l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ࿨") in CONFIG:
      bstack1111l111_opy_ = CONFIG[bstack11ll1l_opy_ (u"࠭ࡰࡢࡴࡤࡰࡱ࡫࡬ࡴࡒࡨࡶࡕࡲࡡࡵࡨࡲࡶࡲ࠭࿩")]
    if bstack11ll1l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿪") in CONFIG:
      bstack1ll111111_opy_ = int(bstack1111l111_opy_) * int(len(CONFIG[bstack11ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ࿫")]))
    else:
      bstack1ll111111_opy_ = int(bstack1111l111_opy_)
    config = Configuration(args)
    bstack1l1lll1lll_opy_ = config.paths
    if len(bstack1l1lll1lll_opy_) == 0:
      import glob
      pattern = bstack11ll1l_opy_ (u"ࠩ࠭࠮࠴࠰࠮ࡧࡧࡤࡸࡺࡸࡥࠨ࿬")
      bstack111l1111l1_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack111l1111l1_opy_)
      config = Configuration(args)
      bstack1l1lll1lll_opy_ = config.paths
    bstack11111l11_opy_ = [os.path.normpath(item) for item in bstack1l1lll1lll_opy_]
    bstack1ll1111l11_opy_ = [os.path.normpath(item) for item in args]
    bstack11llll1ll1_opy_ = [item for item in bstack1ll1111l11_opy_ if item not in bstack11111l11_opy_]
    import platform as pf
    if pf.system().lower() == bstack11ll1l_opy_ (u"ࠪࡻ࡮ࡴࡤࡰࡹࡶࠫ࿭"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack11111l11_opy_ = [str(PurePosixPath(PureWindowsPath(bstack1ll1111l1l_opy_)))
                    for bstack1ll1111l1l_opy_ in bstack11111l11_opy_]
    bstack1lll1l1ll_opy_ = []
    for spec in bstack11111l11_opy_:
      bstack1llll11l1_opy_ = []
      bstack1llll11l1_opy_ += bstack11llll1ll1_opy_
      bstack1llll11l1_opy_.append(spec)
      bstack1lll1l1ll_opy_.append(bstack1llll11l1_opy_)
    execution_items = []
    for bstack1llll11l1_opy_ in bstack1lll1l1ll_opy_:
      if bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ࿮") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack11ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ࿯")]):
          item = {}
          item[bstack11ll1l_opy_ (u"࠭ࡡࡳࡩࠪ࿰")] = bstack11ll1l_opy_ (u"ࠧࠡࠩ࿱").join(bstack1llll11l1_opy_)
          item[bstack11ll1l_opy_ (u"ࠨ࡫ࡱࡨࡪࡾࠧ࿲")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack11ll1l_opy_ (u"ࠩࡤࡶ࡬࠭࿳")] = bstack11ll1l_opy_ (u"ࠪࠤࠬ࿴").join(bstack1llll11l1_opy_)
        item[bstack11ll1l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ࿵")] = 0
        execution_items.append(item)
    bstack11l1l1lll_opy_ = bstack1l1lllllll_opy_(execution_items, bstack1ll111111_opy_)
    for execution_item in bstack11l1l1lll_opy_:
      bstack1lll1llll_opy_ = []
      for item in execution_item:
        bstack1lll1llll_opy_.append(bstack11llll1l1l_opy_(name=str(item[bstack11ll1l_opy_ (u"ࠬ࡯࡮ࡥࡧࡻࠫ࿶")]),
                                             target=bstack1111ll11ll_opy_,
                                             args=(item[bstack11ll1l_opy_ (u"࠭ࡡࡳࡩࠪ࿷")],)))
      for t in bstack1lll1llll_opy_:
        t.start()
      for t in bstack1lll1llll_opy_:
        t.join()
  else:
    bstack1l111llll_opy_(bstack111l11l11_opy_)
  if not bstack11l111lll1_opy_:
    bstack1l1llll111_opy_()
    if(bstack1ll1l1ll1_opy_ in [bstack11ll1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ࿸"), bstack11ll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ࿹")]):
      bstack1111lllll1_opy_()
  bstack1l11111111_opy_.bstack1l1111ll11_opy_()
def browserstack_initialize(bstack11llll1l11_opy_=None):
  logger.info(bstack11ll1l_opy_ (u"ࠩࡕࡹࡳࡴࡩ࡯ࡩࠣࡗࡉࡑࠠࡸ࡫ࡷ࡬ࠥࡧࡲࡨࡵ࠽ࠤࠬ࿺") + str(bstack11llll1l11_opy_))
  run_on_browserstack(bstack11llll1l11_opy_, None, True)
@measure(event_name=EVENTS.bstack111l1llll_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack1l1llll111_opy_():
  global CONFIG
  global bstack1l1ll11lll_opy_
  global bstack111lll1l11_opy_
  global bstack1111ll111_opy_
  global bstack111ll1l1_opy_
  bstack1111lll11l_opy_.bstack111ll111ll_opy_()
  if cli.is_running():
    bstack1l11l11111_opy_.invoke(Events.bstack111lll1l1_opy_)
  else:
    bstack111l1111_opy_ = bstack1llllll11_opy_.bstack111111ll_opy_(config=CONFIG)
    bstack111l1111_opy_.bstack1l1l1l11l_opy_(CONFIG)
  if bstack1l1ll11lll_opy_ == bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ࿻"):
    if not cli.is_enabled(CONFIG):
      bstack1l1l1lll_opy_.stop()
  else:
    bstack1l1l1lll_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1ll1llll_opy_.bstack1l11l1ll1l_opy_()
  if bstack11ll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ࿼") in CONFIG and str(CONFIG[bstack11ll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ࿽")]).lower() != bstack11ll1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ࿾"):
    hashed_id, bstack1ll1l1l11_opy_ = bstack1l11ll11ll_opy_()
  else:
    hashed_id, bstack1ll1l1l11_opy_ = get_build_link()
  bstack1ll1ll1l1l_opy_(hashed_id)
  logger.info(bstack11ll1l_opy_ (u"ࠧࡔࡆࡎࠤࡷࡻ࡮ࠡࡧࡱࡨࡪࡪࠠࡧࡱࡵࠤ࡮ࡪ࠺ࠨ࿿") + bstack111ll1l1_opy_.get_property(bstack11ll1l_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪက"), bstack11ll1l_opy_ (u"ࠩࠪခ")) + bstack11ll1l_opy_ (u"ࠪ࠰ࠥࡺࡥࡴࡶ࡫ࡹࡧࠦࡩࡥ࠼ࠣࠫဂ") + os.getenv(bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩဃ"), bstack11ll1l_opy_ (u"ࠬ࠭င")))
  if hashed_id is not None and bstack1111l1lll1_opy_() != -1:
    sessions = bstack11llll1lll_opy_(hashed_id)
    bstack1l1111l1ll_opy_(sessions, bstack1ll1l1l11_opy_)
  if bstack1l1ll11lll_opy_ == bstack11ll1l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭စ") and bstack111lll1l11_opy_ != 0:
    sys.exit(bstack111lll1l11_opy_)
  if bstack1l1ll11lll_opy_ == bstack11ll1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧဆ") and bstack1111ll111_opy_ != 0:
    sys.exit(bstack1111ll111_opy_)
def bstack1ll1ll1l1l_opy_(new_id):
    global bstack1ll11l111_opy_
    bstack1ll11l111_opy_ = new_id
def bstack11lll1llll_opy_(bstack11l1ll111_opy_):
  if bstack11l1ll111_opy_:
    return bstack11l1ll111_opy_.capitalize()
  else:
    return bstack11ll1l_opy_ (u"ࠨࠩဇ")
@measure(event_name=EVENTS.bstack1llll1l111_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack11111llll1_opy_(bstack1l11lll1l1_opy_):
  if bstack11ll1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧဈ") in bstack1l11lll1l1_opy_ and bstack1l11lll1l1_opy_[bstack11ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨဉ")] != bstack11ll1l_opy_ (u"ࠫࠬည"):
    return bstack1l11lll1l1_opy_[bstack11ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪဋ")]
  else:
    bstack11l111llll_opy_ = bstack11ll1l_opy_ (u"ࠨࠢဌ")
    if bstack11ll1l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧဍ") in bstack1l11lll1l1_opy_ and bstack1l11lll1l1_opy_[bstack11ll1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨဎ")] != None:
      bstack11l111llll_opy_ += bstack1l11lll1l1_opy_[bstack11ll1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩဏ")] + bstack11ll1l_opy_ (u"ࠥ࠰ࠥࠨတ")
      if bstack1l11lll1l1_opy_[bstack11ll1l_opy_ (u"ࠫࡴࡹࠧထ")] == bstack11ll1l_opy_ (u"ࠧ࡯࡯ࡴࠤဒ"):
        bstack11l111llll_opy_ += bstack11ll1l_opy_ (u"ࠨࡩࡐࡕࠣࠦဓ")
      bstack11l111llll_opy_ += (bstack1l11lll1l1_opy_[bstack11ll1l_opy_ (u"ࠧࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠫန")] or bstack11ll1l_opy_ (u"ࠨࠩပ"))
      return bstack11l111llll_opy_
    else:
      bstack11l111llll_opy_ += bstack11lll1llll_opy_(bstack1l11lll1l1_opy_[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪဖ")]) + bstack11ll1l_opy_ (u"ࠥࠤࠧဗ") + (
              bstack1l11lll1l1_opy_[bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ဘ")] or bstack11ll1l_opy_ (u"ࠬ࠭မ")) + bstack11ll1l_opy_ (u"ࠨࠬࠡࠤယ")
      if bstack1l11lll1l1_opy_[bstack11ll1l_opy_ (u"ࠧࡰࡵࠪရ")] == bstack11ll1l_opy_ (u"࡙ࠣ࡬ࡲࡩࡵࡷࡴࠤလ"):
        bstack11l111llll_opy_ += bstack11ll1l_opy_ (u"ࠤ࡚࡭ࡳࠦࠢဝ")
      bstack11l111llll_opy_ += bstack1l11lll1l1_opy_[bstack11ll1l_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧသ")] or bstack11ll1l_opy_ (u"ࠫࠬဟ")
      return bstack11l111llll_opy_
@measure(event_name=EVENTS.bstack1ll1ll111l_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack1111111lll_opy_(bstack111l1l1l1l_opy_):
  if bstack111l1l1l1l_opy_ == bstack11ll1l_opy_ (u"ࠧࡪ࡯࡯ࡧࠥဠ"):
    return bstack11ll1l_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡩࡵࡩࡪࡴ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡩࡵࡩࡪࡴࠢ࠿ࡅࡲࡱࡵࡲࡥࡵࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩအ")
  elif bstack111l1l1l1l_opy_ == bstack11ll1l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢဢ"):
    return bstack11ll1l_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡶࡪࡪ࠻ࠣࡀ࠿ࡪࡴࡴࡴࠡࡥࡲࡰࡴࡸ࠽ࠣࡴࡨࡨࠧࡄࡆࡢ࡫࡯ࡩࡩࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫဣ")
  elif bstack111l1l1l1l_opy_ == bstack11ll1l_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤဤ"):
    return bstack11ll1l_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿࡭ࡲࡦࡧࡱ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧ࡭ࡲࡦࡧࡱࠦࡃࡖࡡࡴࡵࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪဥ")
  elif bstack111l1l1l1l_opy_ == bstack11ll1l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥဦ"):
    return bstack11ll1l_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡳࡧࡧ࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡸࡥࡥࠤࡁࡉࡷࡸ࡯ࡳ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧဧ")
  elif bstack111l1l1l1l_opy_ == bstack11ll1l_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢဨ"):
    return bstack11ll1l_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࠦࡩࡪࡧ࠳࠳࠸࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࠨ࡫ࡥࡢ࠵࠵࠺ࠧࡄࡔࡪ࡯ࡨࡳࡺࡺ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬဩ")
  elif bstack111l1l1l1l_opy_ == bstack11ll1l_opy_ (u"ࠣࡴࡸࡲࡳ࡯࡮ࡨࠤဪ"):
    return bstack11ll1l_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡧࡲࡡࡤ࡭࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡧࡲࡡࡤ࡭ࠥࡂࡗࡻ࡮࡯࡫ࡱ࡫ࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪါ")
  else:
    return bstack11ll1l_opy_ (u"ࠪࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡢ࡭ࡣࡦ࡯ࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡢ࡭ࡣࡦ࡯ࠧࡄࠧာ") + bstack11lll1llll_opy_(
      bstack111l1l1l1l_opy_) + bstack11ll1l_opy_ (u"ࠫࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪိ")
def bstack11ll111lll_opy_(session):
  return bstack11ll1l_opy_ (u"ࠬࡂࡴࡳࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡵࡳࡼࠨ࠾࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠢࡶࡩࡸࡹࡩࡰࡰ࠰ࡲࡦࡳࡥࠣࡀ࠿ࡥࠥ࡮ࡲࡦࡨࡀࠦࢀࢃࠢࠡࡶࡤࡶ࡬࡫ࡴ࠾ࠤࡢࡦࡱࡧ࡮࡬ࠤࡁࡿࢂࡂ࠯ࡢࡀ࠿࠳ࡹࡪ࠾ࡼࡿࡾࢁࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂࡴࡥࠢࡤࡰ࡮࡭࡮࠾ࠤࡦࡩࡳࡺࡥࡳࠤࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࡀࡾࢁࡁ࠵ࡴࡥࡀ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼࠰ࡶࡵࡂࠬီ").format(
    session[bstack11ll1l_opy_ (u"࠭ࡰࡶࡤ࡯࡭ࡨࡥࡵࡳ࡮ࠪု")], bstack11111llll1_opy_(session), bstack1111111lll_opy_(session[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡳࡵࡣࡷࡹࡸ࠭ူ")]),
    bstack1111111lll_opy_(session[bstack11ll1l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨေ")]),
    bstack11lll1llll_opy_(session[bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪဲ")] or session[bstack11ll1l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࠪဳ")] or bstack11ll1l_opy_ (u"ࠫࠬဴ")) + bstack11ll1l_opy_ (u"ࠧࠦࠢဵ") + (session[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨံ")] or bstack11ll1l_opy_ (u"ࠧࠨ့")),
    session[bstack11ll1l_opy_ (u"ࠨࡱࡶࠫး")] + bstack11ll1l_opy_ (u"ࠤ္ࠣࠦ") + session[bstack11ll1l_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴ်ࠧ")], session[bstack11ll1l_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ျ")] or bstack11ll1l_opy_ (u"ࠬ࠭ြ"),
    session[bstack11ll1l_opy_ (u"࠭ࡣࡳࡧࡤࡸࡪࡪ࡟ࡢࡶࠪွ")] if session[bstack11ll1l_opy_ (u"ࠧࡤࡴࡨࡥࡹ࡫ࡤࡠࡣࡷࠫှ")] else bstack11ll1l_opy_ (u"ࠨࠩဿ"))
@measure(event_name=EVENTS.bstack111111lll_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def bstack1l1111l1ll_opy_(sessions, bstack1ll1l1l11_opy_):
  try:
    bstack1ll1l1111l_opy_ = bstack11ll1l_opy_ (u"ࠤࠥ၀")
    if not os.path.exists(bstack1l1l1l11ll_opy_):
      os.mkdir(bstack1l1l1l11ll_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11ll1l_opy_ (u"ࠪࡥࡸࡹࡥࡵࡵ࠲ࡶࡪࡶ࡯ࡳࡶ࠱࡬ࡹࡳ࡬ࠨ၁")), bstack11ll1l_opy_ (u"ࠫࡷ࠭၂")) as f:
      bstack1ll1l1111l_opy_ = f.read()
    bstack1ll1l1111l_opy_ = bstack1ll1l1111l_opy_.replace(bstack11ll1l_opy_ (u"ࠬࢁࠥࡓࡇࡖ࡙ࡑ࡚ࡓࡠࡅࡒ࡙ࡓ࡚ࠥࡾࠩ၃"), str(len(sessions)))
    bstack1ll1l1111l_opy_ = bstack1ll1l1111l_opy_.replace(bstack11ll1l_opy_ (u"࠭ࡻࠦࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠩࢂ࠭၄"), bstack1ll1l1l11_opy_)
    bstack1ll1l1111l_opy_ = bstack1ll1l1111l_opy_.replace(bstack11ll1l_opy_ (u"ࠧࡼࠧࡅ࡙ࡎࡒࡄࡠࡐࡄࡑࡊࠫࡽࠨ၅"),
                                              sessions[0].get(bstack11ll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟࡯ࡣࡰࡩࠬ၆")) if sessions[0] else bstack11ll1l_opy_ (u"ࠩࠪ၇"))
    with open(os.path.join(bstack1l1l1l11ll_opy_, bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡵࡩࡵࡵࡲࡵ࠰࡫ࡸࡲࡲࠧ၈")), bstack11ll1l_opy_ (u"ࠫࡼ࠭၉")) as stream:
      stream.write(bstack1ll1l1111l_opy_.split(bstack11ll1l_opy_ (u"ࠬࢁࠥࡔࡇࡖࡗࡎࡕࡎࡔࡡࡇࡅ࡙ࡇࠥࡾࠩ၊"))[0])
      for session in sessions:
        stream.write(bstack11ll111lll_opy_(session))
      stream.write(bstack1ll1l1111l_opy_.split(bstack11ll1l_opy_ (u"࠭ࡻࠦࡕࡈࡗࡘࡏࡏࡏࡕࡢࡈࡆ࡚ࡁࠦࡿࠪ။"))[1])
    logger.info(bstack11ll1l_opy_ (u"ࠧࡈࡧࡱࡩࡷࡧࡴࡦࡦࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡥࡹ࡮ࡲࡤࠡࡣࡵࡸ࡮࡬ࡡࡤࡶࡶࠤࡦࡺࠠࡼࡿࠪ၌").format(bstack1l1l1l11ll_opy_));
  except Exception as e:
    logger.debug(bstack11l1llll1_opy_.format(str(e)))
def bstack11llll1lll_opy_(hashed_id):
  global CONFIG
  try:
    bstack1ll11ll111_opy_ = datetime.datetime.now()
    host = bstack11ll1l_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠳ࡣ࡭ࡱࡸࡨ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠨ၍") if bstack11ll1l_opy_ (u"ࠩࡤࡴࡵ࠭၎") in CONFIG else bstack11ll1l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࡦࡶࡩ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ၏")
    user = CONFIG[bstack11ll1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ၐ")]
    key = CONFIG[bstack11ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨၑ")]
    bstack11l1lll1l1_opy_ = bstack11ll1l_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬၒ") if bstack11ll1l_opy_ (u"ࠧࡢࡲࡳࠫၓ") in CONFIG else (bstack11ll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬၔ") if CONFIG.get(bstack11ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭ၕ")) else bstack11ll1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬၖ"))
    host = bstack1lll1l11l1_opy_(cli.config, [bstack11ll1l_opy_ (u"ࠦࡦࡶࡩࡴࠤၗ"), bstack11ll1l_opy_ (u"ࠧࡧࡰࡱࡃࡸࡸࡴࡳࡡࡵࡧࠥၘ"), bstack11ll1l_opy_ (u"ࠨࡡࡱ࡫ࠥၙ")], host) if bstack11ll1l_opy_ (u"ࠧࡢࡲࡳࠫၚ") in CONFIG else bstack1lll1l11l1_opy_(cli.config, [bstack11ll1l_opy_ (u"ࠣࡣࡳ࡭ࡸࠨၛ"), bstack11ll1l_opy_ (u"ࠤࡤࡹࡹࡵ࡭ࡢࡶࡨࠦၜ"), bstack11ll1l_opy_ (u"ࠥࡥࡵ࡯ࠢၝ")], host)
    url = bstack11ll1l_opy_ (u"ࠫࢀࢃ࠯ࡼࡿ࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠯࡬ࡶࡳࡳ࠭ၞ").format(host, bstack11l1lll1l1_opy_, hashed_id)
    headers = {
      bstack11ll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫၟ"): bstack11ll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩၠ"),
    }
    proxies = bstack1ll11ll1l_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠢࡩࡶࡷࡴ࠿࡭ࡥࡵࡡࡶࡩࡸࡹࡩࡰࡰࡶࡣࡱ࡯ࡳࡵࠤၡ"), datetime.datetime.now() - bstack1ll11ll111_opy_)
      return list(map(lambda session: session[bstack11ll1l_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ၢ")], response.json()))
  except Exception as e:
    logger.debug(bstack11l1l1l1l_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack1l11l1llll_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def get_build_link():
  global CONFIG
  global bstack1ll11l111_opy_
  try:
    if bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬၣ") in CONFIG:
      bstack1ll11ll111_opy_ = datetime.datetime.now()
      host = bstack11ll1l_opy_ (u"ࠪࡥࡵ࡯࠭ࡤ࡮ࡲࡹࡩ࠭ၤ") if bstack11ll1l_opy_ (u"ࠫࡦࡶࡰࠨၥ") in CONFIG else bstack11ll1l_opy_ (u"ࠬࡧࡰࡪࠩၦ")
      user = CONFIG[bstack11ll1l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨၧ")]
      key = CONFIG[bstack11ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪၨ")]
      bstack11l1lll1l1_opy_ = bstack11ll1l_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧၩ") if bstack11ll1l_opy_ (u"ࠩࡤࡴࡵ࠭ၪ") in CONFIG else bstack11ll1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬၫ")
      url = bstack11ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱࡵ࠽࠳࠴ࢁࡽ࠻ࡽࢀࡄࢀࢃ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡿࢂ࠵ࡢࡶ࡫࡯ࡨࡸ࠴ࡪࡴࡱࡱࠫၬ").format(user, key, host, bstack11l1lll1l1_opy_)
      if cli.is_enabled(CONFIG):
        bstack1ll1l1l11_opy_, hashed_id = cli.bstack1l111ll1ll_opy_()
        logger.info(bstack111l11l111_opy_.format(bstack1ll1l1l11_opy_))
        return [hashed_id, bstack1ll1l1l11_opy_]
      else:
        headers = {
          bstack11ll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫၭ"): bstack11ll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩၮ"),
        }
        if bstack11ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩၯ") in CONFIG:
          params = {bstack11ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ၰ"): CONFIG[bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬၱ")], bstack11ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ၲ"): CONFIG[bstack11ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ၳ")]}
        else:
          params = {bstack11ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪၴ"): CONFIG[bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩၵ")]}
        proxies = bstack1ll11ll1l_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack111l1ll1ll_opy_ = response.json()[0][bstack11ll1l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡧࡻࡩ࡭ࡦࠪၶ")]
          if bstack111l1ll1ll_opy_:
            bstack1ll1l1l11_opy_ = bstack111l1ll1ll_opy_[bstack11ll1l_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣࡠࡷࡵࡰࠬၷ")].split(bstack11ll1l_opy_ (u"ࠩࡳࡹࡧࡲࡩࡤ࠯ࡥࡹ࡮ࡲࡤࠨၸ"))[0] + bstack11ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡵ࠲ࠫၹ") + bstack111l1ll1ll_opy_[
              bstack11ll1l_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧၺ")]
            logger.info(bstack111l11l111_opy_.format(bstack1ll1l1l11_opy_))
            bstack1ll11l111_opy_ = bstack111l1ll1ll_opy_[bstack11ll1l_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨၻ")]
            bstack1111ll11l_opy_ = CONFIG[bstack11ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩၼ")]
            if bstack11ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩၽ") in CONFIG:
              bstack1111ll11l_opy_ += bstack11ll1l_opy_ (u"ࠨࠢࠪၾ") + CONFIG[bstack11ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫၿ")]
            if bstack1111ll11l_opy_ != bstack111l1ll1ll_opy_[bstack11ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨႀ")]:
              logger.debug(bstack1111lll1l_opy_.format(bstack111l1ll1ll_opy_[bstack11ll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩႁ")], bstack1111ll11l_opy_))
            cli.bstack1ll1lll1ll_opy_(bstack11ll1l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࡫ࡪࡺ࡟ࡣࡷ࡬ࡰࡩࡥ࡬ࡪࡰ࡮ࠦႂ"), datetime.datetime.now() - bstack1ll11ll111_opy_)
            return [bstack111l1ll1ll_opy_[bstack11ll1l_opy_ (u"࠭ࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩႃ")], bstack1ll1l1l11_opy_]
    else:
      logger.warn(bstack11lll111ll_opy_)
  except Exception as e:
    logger.debug(bstack111ll11l1l_opy_.format(str(e)))
  return [None, None]
def bstack1l1l11l1l1_opy_(url, bstack1111lll1ll_opy_=False):
  global CONFIG
  global bstack11l111l1l1_opy_
  if not bstack11l111l1l1_opy_:
    hostname = bstack111ll1l1l1_opy_(url)
    is_private = bstack11l1l1l11_opy_(hostname)
    if (bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫႄ") in CONFIG and not bstack1ll11lll11_opy_(CONFIG[bstack11ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬႅ")])) and (is_private or bstack1111lll1ll_opy_):
      bstack11l111l1l1_opy_ = hostname
def bstack111ll1l1l1_opy_(url):
  return urlparse(url).hostname
def bstack11l1l1l11_opy_(hostname):
  for bstack1l1l11l111_opy_ in bstack111ll1l111_opy_:
    regex = re.compile(bstack1l1l11l111_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1ll1l11lll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1111l111ll_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack1l111l1111_opy_
  bstack11l1111l11_opy_ = not (bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ႆ"), None) and bstack1lllll11_opy_(
          threading.current_thread(), bstack11ll1l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩႇ"), None))
  bstack1l11l1lll_opy_ = getattr(driver, bstack11ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫႈ"), None) != True
  bstack11l11ll111_opy_ = bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬႉ"), None) and bstack1lllll11_opy_(
          threading.current_thread(), bstack11ll1l_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨႊ"), None)
  if bstack11l11ll111_opy_:
    if not bstack1l1ll111l1_opy_():
      logger.warning(bstack11ll1l_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵ࠱ࠦႋ"))
      return {}
    logger.debug(bstack11ll1l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠬႌ"))
    logger.debug(perform_scan(driver, driver_command=bstack11ll1l_opy_ (u"ࠩࡨࡼࡪࡩࡵࡵࡧࡖࡧࡷ࡯ࡰࡵႍࠩ")))
    results = bstack111l111l1l_opy_(bstack11ll1l_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡶࠦႎ"))
    if results is not None and results.get(bstack11ll1l_opy_ (u"ࠦ࡮ࡹࡳࡶࡧࡶࠦႏ")) is not None:
        return results[bstack11ll1l_opy_ (u"ࠧ࡯ࡳࡴࡷࡨࡷࠧ႐")]
    logger.error(bstack11ll1l_opy_ (u"ࠨࡎࡰࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡕࡩࡸࡻ࡬ࡵࡵࠣࡻࡪࡸࡥࠡࡨࡲࡹࡳࡪ࠮ࠣ႑"))
    return []
  if not bstack1lllll1l1_opy_.bstack1111llll1_opy_(CONFIG, bstack1l111l1111_opy_) or (bstack1l11l1lll_opy_ and bstack11l1111l11_opy_):
    logger.warning(bstack11ll1l_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴ࠰ࠥ႒"))
    return {}
  try:
    logger.debug(bstack11ll1l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠬ႓"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack1l1l111ll_opy_.bstack11l11l1l1l_opy_)
    return results
  except Exception:
    logger.error(bstack11ll1l_opy_ (u"ࠤࡑࡳࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡷࡦࡴࡨࠤ࡫ࡵࡵ࡯ࡦ࠱ࠦ႔"))
    return {}
@measure(event_name=EVENTS.bstack11ll1l111_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack1l111l1111_opy_
  bstack11l1111l11_opy_ = not (bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ႕"), None) and bstack1lllll11_opy_(
          threading.current_thread(), bstack11ll1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ႖"), None))
  bstack1l11l1lll_opy_ = getattr(driver, bstack11ll1l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ႗"), None) != True
  bstack11l11ll111_opy_ = bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭႘"), None) and bstack1lllll11_opy_(
          threading.current_thread(), bstack11ll1l_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ႙"), None)
  if bstack11l11ll111_opy_:
    if not bstack1l1ll111l1_opy_():
      logger.warning(bstack11ll1l_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡳࡴࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡸࡻ࡭࡮ࡣࡵࡽ࠳ࠨႚ"))
      return {}
    logger.debug(bstack11ll1l_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡳࡶ࡯ࡰࡥࡷࡿࠧႛ"))
    logger.debug(perform_scan(driver, driver_command=bstack11ll1l_opy_ (u"ࠪࡩࡽ࡫ࡣࡶࡶࡨࡗࡨࡸࡩࡱࡶࠪႜ")))
    results = bstack111l111l1l_opy_(bstack11ll1l_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷࡗࡺࡳ࡭ࡢࡴࡼࠦႝ"))
    if results is not None and results.get(bstack11ll1l_opy_ (u"ࠧࡹࡵ࡮࡯ࡤࡶࡾࠨ႞")) is not None:
        return results[bstack11ll1l_opy_ (u"ࠨࡳࡶ࡯ࡰࡥࡷࡿࠢ႟")]
    logger.error(bstack11ll1l_opy_ (u"ࠢࡏࡱࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡖࡪࡹࡵ࡭ࡶࡶࠤࡘࡻ࡭࡮ࡣࡵࡽࠥࡽࡡࡴࠢࡩࡳࡺࡴࡤ࠯ࠤႠ"))
    return {}
  if not bstack1lllll1l1_opy_.bstack1111llll1_opy_(CONFIG, bstack1l111l1111_opy_) or (bstack1l11l1lll_opy_ and bstack11l1111l11_opy_):
    logger.warning(bstack11ll1l_opy_ (u"ࠣࡐࡲࡸࠥࡧ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼ࠲ࠧႡ"))
    return {}
  try:
    logger.debug(bstack11ll1l_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡸࡥࡴࡷ࡯ࡸࡸࠦࡳࡶ࡯ࡰࡥࡷࡿࠧႢ"))
    logger.debug(perform_scan(driver))
    bstack11l11llll_opy_ = driver.execute_async_script(bstack1l1l111ll_opy_.bstack1111l11l1l_opy_)
    return bstack11l11llll_opy_
  except Exception:
    logger.error(bstack11ll1l_opy_ (u"ࠥࡒࡴࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡳࡶ࡯ࡰࡥࡷࡿࠠࡸࡣࡶࠤ࡫ࡵࡵ࡯ࡦ࠱ࠦႣ"))
    return {}
def bstack1l1ll111l1_opy_():
  global CONFIG
  global bstack1l111l1111_opy_
  bstack111111l1l1_opy_ = bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫႤ"), None) and bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧႥ"), None)
  if not bstack1lllll1l1_opy_.bstack1111llll1_opy_(CONFIG, bstack1l111l1111_opy_) or not bstack111111l1l1_opy_:
        logger.warning(bstack11ll1l_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡷ࡫ࡳࡶ࡮ࡷࡷ࠳ࠨႦ"))
        return False
  return True
def bstack111l111l1l_opy_(bstack11lllll1ll_opy_):
    bstack1l11111ll_opy_ = bstack1l1l1lll_opy_.current_test_uuid() if bstack1l1l1lll_opy_.current_test_uuid() else bstack1ll1llll_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack1lllll1l11_opy_(bstack1l11111ll_opy_, bstack11lllll1ll_opy_))
        try:
            return future.result(timeout=bstack11111lll11_opy_)
        except TimeoutError:
            logger.error(bstack11ll1l_opy_ (u"ࠢࡕ࡫ࡰࡩࡴࡻࡴࠡࡣࡩࡸࡪࡸࠠࡼࡿࡶࠤࡼ࡮ࡩ࡭ࡧࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡘࡥࡴࡷ࡯ࡸࡸࠨႧ").format(bstack11111lll11_opy_))
        except Exception as ex:
            logger.debug(bstack11ll1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡳࡧࡷࡶ࡮࡫ࡶࡪࡰࡪࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࢁࡽ࠯ࠢࡈࡶࡷࡵࡲࠡ࠯ࠣࡿࢂࠨႨ").format(bstack11lllll1ll_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack1ll1111lll_opy_, stage=STAGE.bstack11ll11lll_opy_, bstack11l111llll_opy_=bstack1111ll1l1l_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack1l111l1111_opy_
  bstack11l1111l11_opy_ = not (bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭Ⴉ"), None) and bstack1lllll11_opy_(
          threading.current_thread(), bstack11ll1l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩႪ"), None))
  bstack1lll1ll1l1_opy_ = not (bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫႫ"), None) and bstack1lllll11_opy_(
          threading.current_thread(), bstack11ll1l_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧႬ"), None))
  bstack1l11l1lll_opy_ = getattr(driver, bstack11ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭Ⴍ"), None) != True
  if not bstack1lllll1l1_opy_.bstack1111llll1_opy_(CONFIG, bstack1l111l1111_opy_) or (bstack1l11l1lll_opy_ and bstack11l1111l11_opy_ and bstack1lll1ll1l1_opy_):
    logger.warning(bstack11ll1l_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡶࡰࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡨࡧ࡮࠯ࠤႮ"))
    return {}
  try:
    bstack1lllll111l_opy_ = bstack11ll1l_opy_ (u"ࠨࡣࡳࡴࠬႯ") in CONFIG and CONFIG.get(bstack11ll1l_opy_ (u"ࠩࡤࡴࡵ࠭Ⴐ"), bstack11ll1l_opy_ (u"ࠪࠫႱ"))
    session_id = getattr(driver, bstack11ll1l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠨႲ"), None)
    if not session_id:
      logger.warning(bstack11ll1l_opy_ (u"ࠧࡔ࡯ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡌࡈࠥ࡬࡯ࡶࡰࡧࠤ࡫ࡵࡲࠡࡦࡵ࡭ࡻ࡫ࡲࠣႳ"))
      return {bstack11ll1l_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧႴ"): bstack11ll1l_opy_ (u"ࠢࡏࡱࠣࡷࡪࡹࡳࡪࡱࡱࠤࡎࡊࠠࡧࡱࡸࡲࡩࠨႵ")}
    if bstack1lllll111l_opy_:
      try:
        bstack1ll1l1l111_opy_ = {
              bstack11ll1l_opy_ (u"ࠨࡶ࡫ࡎࡼࡺࡔࡰ࡭ࡨࡲࠬႶ"): os.environ.get(bstack11ll1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧႷ"), os.environ.get(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜࡚ࠧႸ"), bstack11ll1l_opy_ (u"ࠫࠬႹ"))),
              bstack11ll1l_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬႺ"): bstack1l1l1lll_opy_.current_test_uuid() if bstack1l1l1lll_opy_.current_test_uuid() else bstack1ll1llll_opy_.current_hook_uuid(),
              bstack11ll1l_opy_ (u"࠭ࡡࡶࡶ࡫ࡌࡪࡧࡤࡦࡴࠪႻ"): os.environ.get(bstack11ll1l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬႼ")),
              bstack11ll1l_opy_ (u"ࠨࡵࡦࡥࡳ࡚ࡩ࡮ࡧࡶࡸࡦࡳࡰࠨႽ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack11ll1l_opy_ (u"ࠩࡷ࡬ࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧႾ"): os.environ.get(bstack11ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨႿ"), bstack11ll1l_opy_ (u"ࠫࠬჀ")),
              bstack11ll1l_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࠬჁ"): kwargs.get(bstack11ll1l_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷࡥࡣࡰ࡯ࡰࡥࡳࡪࠧჂ"), None) or bstack11ll1l_opy_ (u"ࠧࠨჃ")
          }
        if not hasattr(thread_local, bstack11ll1l_opy_ (u"ࠨࡤࡤࡷࡪࡥࡡࡱࡲࡢࡥ࠶࠷ࡹࡠࡵࡦࡶ࡮ࡶࡴࠨჄ")):
            scripts = {bstack11ll1l_opy_ (u"ࠩࡶࡧࡦࡴࠧჅ"): bstack1l1l111ll_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack1lll11lll1_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack1lll11lll1_opy_[bstack11ll1l_opy_ (u"ࠪࡷࡨࡧ࡮ࠨ჆")] = bstack1lll11lll1_opy_[bstack11ll1l_opy_ (u"ࠫࡸࡩࡡ࡯ࠩჇ")] % json.dumps(bstack1ll1l1l111_opy_)
        bstack1l1l111ll_opy_.bstack111lll11l_opy_(bstack1lll11lll1_opy_)
        bstack1l1l111ll_opy_.store()
        bstack1ll1lll1l1_opy_ = driver.execute_script(bstack1l1l111ll_opy_.perform_scan)
      except Exception as bstack1l1l111ll1_opy_:
        logger.info(bstack11ll1l_opy_ (u"ࠧࡇࡰࡱ࡫ࡸࡱࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡣࡢࡰࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࠧ჈") + str(bstack1l1l111ll1_opy_))
        bstack1ll1lll1l1_opy_ = {bstack11ll1l_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧ჉"): str(bstack1l1l111ll1_opy_)}
    else:
      bstack1ll1lll1l1_opy_ = driver.execute_async_script(bstack1l1l111ll_opy_.perform_scan, {bstack11ll1l_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪࠧ჊"): kwargs.get(bstack11ll1l_opy_ (u"ࠨࡦࡵ࡭ࡻ࡫ࡲࡠࡥࡲࡱࡲࡧ࡮ࡥࠩ჋"), None) or bstack11ll1l_opy_ (u"ࠩࠪ჌")})
    return bstack1ll1lll1l1_opy_
  except Exception as err:
    logger.error(bstack11ll1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡲࡶࡰࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡨࡧ࡮࠯ࠢࡾࢁࠧჍ").format(str(err)))
    return {}