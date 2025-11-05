# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
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
from browserstack_sdk.bstack1lll1llll1_opy_ import bstack11ll1l11l_opy_
from browserstack_sdk.bstack1lll1111l_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE, bstack1llll1ll11_opy_
from bstack_utils.messages import bstack111111ll1l_opy_, bstack11l1llll1_opy_, bstack111ll1111_opy_, bstack1llll11ll1_opy_, bstack111ll1111l_opy_, bstack11lll11ll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11ll1111l_opy_ import get_logger
from bstack_utils.helper import bstack1lll1lll11_opy_
from browserstack_sdk.bstack1llllll1l_opy_ import bstack11ll11111_opy_
logger = get_logger(__name__)
def bstack1111l11lll_opy_():
  global CONFIG
  headers = {
        bstack1lll11l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡴࡺࡲࡨࠫਕ"): bstack1lll11l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩਖ"),
      }
  proxies = bstack1lll1lll11_opy_(CONFIG, bstack1llll1ll11_opy_)
  try:
    response = requests.get(bstack1llll1ll11_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack111ll11111_opy_ = response.json()[bstack1lll11l_opy_ (u"ࠧࡩࡷࡥࡷࠬਗ")]
      logger.debug(bstack111111ll1l_opy_.format(response.json()))
      return bstack111ll11111_opy_
    else:
      logger.debug(bstack11l1llll1_opy_.format(bstack1lll11l_opy_ (u"ࠣࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡎࡘࡕࡎࠡࡲࡤࡶࡸ࡫ࠠࡦࡴࡵࡳࡷࠦࠢਘ")))
  except Exception as e:
    logger.debug(bstack11l1llll1_opy_.format(e))
def bstack111lll11l1_opy_(hub_url):
  global CONFIG
  url = bstack1lll11l_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦਙ")+  hub_url + bstack1lll11l_opy_ (u"ࠥ࠳ࡨ࡮ࡥࡤ࡭ࠥਚ")
  headers = {
        bstack1lll11l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪਛ"): bstack1lll11l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨਜ"),
      }
  proxies = bstack1lll1lll11_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack111ll1111_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1llll11ll1_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack111lllll1_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
def bstack1lllll11l1_opy_():
  try:
    global bstack111l1llll_opy_
    global CONFIG
    if bstack1lll11l_opy_ (u"࠭ࡨࡶࡤࡕࡩ࡬࡯࡯࡯ࠩਝ") in CONFIG and CONFIG[bstack1lll11l_opy_ (u"ࠧࡩࡷࡥࡖࡪ࡭ࡩࡰࡰࠪਞ")]:
      from bstack_utils.constants import bstack1lll11l1l1_opy_
      bstack11111ll1l1_opy_ = CONFIG[bstack1lll11l_opy_ (u"ࠨࡪࡸࡦࡗ࡫ࡧࡪࡱࡱࠫਟ")]
      if bstack11111ll1l1_opy_ in bstack1lll11l1l1_opy_:
        bstack111l1llll_opy_ = bstack1lll11l1l1_opy_[bstack11111ll1l1_opy_]
        logger.debug(bstack111ll1111l_opy_.format(bstack111l1llll_opy_))
        return
      else:
        logger.debug(bstack1lll11l_opy_ (u"ࠤࡋࡹࡧࠦ࡫ࡦࡻࠣࠫࢀࢃࠧࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡉࡗࡅࡣ࡚ࡘࡌࡠࡏࡄࡔ࠱ࠦࡦࡢ࡮࡯࡭ࡳ࡭ࠠࡣࡣࡦ࡯ࠥࡺ࡯ࠡࡱࡳࡸ࡮ࡳࡡ࡭ࠢ࡫ࡹࡧࠦࡤࡦࡶࡨࡧࡹ࡯࡯࡯ࠤਠ").format(bstack11111ll1l1_opy_))
    bstack111ll11111_opy_ = bstack1111l11lll_opy_()
    bstack1ll1l11lll_opy_ = []
    results = []
    for bstack1111l1ll1l_opy_ in bstack111ll11111_opy_:
      bstack1ll1l11lll_opy_.append(bstack11ll11111_opy_(target=bstack111lll11l1_opy_,args=(bstack1111l1ll1l_opy_,)))
    for t in bstack1ll1l11lll_opy_:
      t.start()
    for t in bstack1ll1l11lll_opy_:
      results.append(t.join())
    bstack111lll1ll_opy_ = {}
    for item in results:
      hub_url = item[bstack1lll11l_opy_ (u"ࠪ࡬ࡺࡨ࡟ࡶࡴ࡯ࠫਡ")]
      latency = item[bstack1lll11l_opy_ (u"ࠫࡱࡧࡴࡦࡰࡦࡽࠬਢ")]
      bstack111lll1ll_opy_[hub_url] = latency
    bstack1l1ll111l1_opy_ = min(bstack111lll1ll_opy_, key= lambda x: bstack111lll1ll_opy_[x])
    bstack111l1llll_opy_ = bstack1l1ll111l1_opy_
    logger.debug(bstack111ll1111l_opy_.format(bstack1l1ll111l1_opy_))
  except Exception as e:
    logger.debug(bstack11lll11ll_opy_.format(e))
from browserstack_sdk.bstack1llllllll_opy_ import *
from browserstack_sdk.bstack1llllll1l_opy_ import *
from browserstack_sdk.bstack11l1l111_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack11ll1111l_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack1l1ll1111l_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
def bstack111ll11ll_opy_():
    global bstack111l1llll_opy_
    try:
        bstack111l1ll1l1_opy_ = bstack11ll111l1_opy_()
        bstack1l1l111lll_opy_(bstack111l1ll1l1_opy_)
        hub_url = bstack111l1ll1l1_opy_.get(bstack1lll11l_opy_ (u"ࠧࡻࡲ࡭ࠤਣ"), bstack1lll11l_opy_ (u"ࠨࠢਤ"))
        if hub_url.endswith(bstack1lll11l_opy_ (u"ࠧ࠰ࡹࡧ࠳࡭ࡻࡢࠨਥ")):
            hub_url = hub_url.rsplit(bstack1lll11l_opy_ (u"ࠨ࠱ࡺࡨ࠴࡮ࡵࡣࠩਦ"), 1)[0]
        if hub_url.startswith(bstack1lll11l_opy_ (u"ࠩ࡫ࡸࡹࡶ࠺࠰࠱ࠪਧ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack1lll11l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠬਨ")):
            hub_url = hub_url[8:]
        bstack111l1llll_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack11ll111l1_opy_():
    global CONFIG
    bstack11ll1l1ll_opy_ = CONFIG.get(bstack1lll11l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ਩"), {}).get(bstack1lll11l_opy_ (u"ࠬ࡭ࡲࡪࡦࡑࡥࡲ࡫ࠧਪ"), bstack1lll11l_opy_ (u"࠭ࡎࡐࡡࡊࡖࡎࡊ࡟ࡏࡃࡐࡉࡤࡖࡁࡔࡕࡈࡈࠬਫ"))
    if not isinstance(bstack11ll1l1ll_opy_, str):
        raise ValueError(bstack1lll11l_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡇࡳ࡫ࡧࠤࡳࡧ࡭ࡦࠢࡰࡹࡸࡺࠠࡣࡧࠣࡥࠥࡼࡡ࡭࡫ࡧࠤࡸࡺࡲࡪࡰࡪࠦਬ"))
    try:
        bstack111l1ll1l1_opy_ = bstack111111lll1_opy_(bstack11ll1l1ll_opy_)
        return bstack111l1ll1l1_opy_
    except Exception as e:
        logger.error(bstack1lll11l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡪࡩࡹࡺࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢਭ").format(str(e)))
        return {}
def bstack111111lll1_opy_(bstack11ll1l1ll_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack1lll11l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫਮ")] or not CONFIG[bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ਯ")]:
            raise ValueError(bstack1lll11l_opy_ (u"ࠦࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡺࡹࡥࡳࡰࡤࡱࡪࠦ࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴࠢ࡮ࡩࡾࠨਰ"))
        url = bstack1l1ll11111_opy_ + bstack11ll1l1ll_opy_
        auth = (CONFIG[bstack1lll11l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧ਱")], CONFIG[bstack1lll11l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩਲ")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1ll11111ll_opy_ = json.loads(response.text)
            return bstack1ll11111ll_opy_
    except ValueError as ve:
        logger.error(bstack1lll11l_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢਲ਼").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack1lll11l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤ࡬ࡸࡩࡥࠢࡧࡩࡹࡧࡩ࡭ࡵࠣ࠾ࠥࢁࡽࠣ਴").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1l1l111lll_opy_(bstack1ll1llll1l_opy_):
    global CONFIG
    if bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ਵ") not in CONFIG or str(CONFIG[bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧਸ਼")]).lower() == bstack1lll11l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ਷"):
        CONFIG[bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫਸ")] = False
    elif bstack1lll11l_opy_ (u"࠭ࡩࡴࡖࡵ࡭ࡦࡲࡇࡳ࡫ࡧࠫਹ") in bstack1ll1llll1l_opy_:
        bstack1lll1l1lll_opy_ = CONFIG.get(bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ਺"), {})
        logger.debug(bstack1lll11l_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡆࡺ࡬ࡷࡹ࡯࡮ࡨࠢ࡯ࡳࡨࡧ࡬ࠡࡱࡳࡸ࡮ࡵ࡮ࡴ࠼ࠣࠩࡸࠨ਻"), bstack1lll1l1lll_opy_)
        bstack1ll11ll11_opy_ = bstack1ll1llll1l_opy_.get(bstack1lll11l_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡔࡨࡴࡪࡧࡴࡦࡴࡶ਼ࠦ"), [])
        bstack111l1l11l_opy_ = bstack1lll11l_opy_ (u"ࠥ࠰ࠧ਽").join(bstack1ll11ll11_opy_)
        logger.debug(bstack1lll11l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡇࡺࡹࡴࡰ࡯ࠣࡶࡪࡶࡥࡢࡶࡨࡶࠥࡹࡴࡳ࡫ࡱ࡫࠿ࠦࠥࡴࠤਾ"), bstack111l1l11l_opy_)
        bstack111llll1ll_opy_ = {
            bstack1lll11l_opy_ (u"ࠧࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢਿ"): bstack1lll11l_opy_ (u"ࠨࡡࡵࡵ࠰ࡶࡪࡶࡥࡢࡶࡨࡶࠧੀ"),
            bstack1lll11l_opy_ (u"ࠢࡧࡱࡵࡧࡪࡒ࡯ࡤࡣ࡯ࠦੁ"): bstack1lll11l_opy_ (u"ࠣࡶࡵࡹࡪࠨੂ"),
            bstack1lll11l_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠦ੃"): bstack111l1l11l_opy_
        }
        bstack1lll1l1lll_opy_.update(bstack111llll1ll_opy_)
        logger.debug(bstack1lll11l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡘࡴࡩࡧࡴࡦࡦࠣࡰࡴࡩࡡ࡭ࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠪࡹࠢ੄"), bstack1lll1l1lll_opy_)
        CONFIG[bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ੅")] = bstack1lll1l1lll_opy_
        logger.debug(bstack1lll11l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡋ࡯࡮ࡢ࡮ࠣࡇࡔࡔࡆࡊࡉ࠽ࠤࠪࡹࠢ੆"), CONFIG)
def bstack1l1111l11_opy_():
    bstack111l1ll1l1_opy_ = bstack11ll111l1_opy_()
    if not bstack111l1ll1l1_opy_[bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡘࡶࡱ࠭ੇ")]:
      raise ValueError(bstack1lll11l_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠠࡪࡵࠣࡱ࡮ࡹࡳࡪࡰࡪࠤ࡫ࡸ࡯࡮ࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳ࠯ࠤੈ"))
    return bstack111l1ll1l1_opy_[bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࡚ࡸ࡬ࠨ੉")] + bstack1lll11l_opy_ (u"ࠩࡂࡧࡦࡶࡳ࠾ࠩ੊")
@measure(event_name=EVENTS.bstack1111ll1lll_opy_, stage=STAGE.bstack1ll1l1l11_opy_)
def bstack11ll11lll_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack1lll11l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬੋ")], CONFIG[bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧੌ")])
        url = bstack1111ll1ll1_opy_
        logger.debug(bstack1lll11l_opy_ (u"ࠧࡇࡴࡵࡧࡰࡴࡹ࡯࡮ࡨࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶࠤ࡫ࡸ࡯࡮ࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡖࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠥࡇࡐࡊࠤ੍"))
        try:
            response = requests.get(url, auth=auth, headers={bstack1lll11l_opy_ (u"ࠨࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠧ੎"): bstack1lll11l_opy_ (u"ࠢࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠥ੏")})
            if response.status_code == 200:
                bstack1l11l1111l_opy_ = json.loads(response.text)
                bstack11l1ll11l1_opy_ = bstack1l11l1111l_opy_.get(bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡳࠨ੐"), [])
                if bstack11l1ll11l1_opy_:
                    bstack11l1l1ll1l_opy_ = bstack11l1ll11l1_opy_[0]
                    build_hashed_id = bstack11l1l1ll1l_opy_.get(bstack1lll11l_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬੑ"))
                    bstack1lll1l1l1l_opy_ = bstack11111111l_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack1lll1l1l1l_opy_])
                    logger.info(bstack11ll11111l_opy_.format(bstack1lll1l1l1l_opy_))
                    bstack11l1111lll_opy_ = CONFIG[bstack1lll11l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭੒")]
                    if bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭੓") in CONFIG:
                      bstack11l1111lll_opy_ += bstack1lll11l_opy_ (u"ࠬࠦࠧ੔") + CONFIG[bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ੕")]
                    if bstack11l1111lll_opy_ != bstack11l1l1ll1l_opy_.get(bstack1lll11l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ੖")):
                      logger.debug(bstack1ll11l1l11_opy_.format(bstack11l1l1ll1l_opy_.get(bstack1lll11l_opy_ (u"ࠨࡰࡤࡱࡪ࠭੗")), bstack11l1111lll_opy_))
                    return result
                else:
                    logger.debug(bstack1lll11l_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡐࡲࠤࡧࡻࡩ࡭ࡦࡶࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡴࡩࡧࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠳ࠨ੘"))
            else:
                logger.debug(bstack1lll11l_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶ࠲ࠧਖ਼"))
        except Exception as e:
            logger.error(bstack1lll11l_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࡸࠦ࠺ࠡࡽࢀࠦਗ਼").format(str(e)))
    else:
        logger.debug(bstack1lll11l_opy_ (u"ࠧࡇࡔࡔࠢ࠽ࠤࡈࡕࡎࡇࡋࡊࠤ࡮ࡹࠠ࡯ࡱࡷࠤࡸ࡫ࡴ࠯ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡧࡻࡩ࡭ࡦࡶ࠲ࠧਜ਼"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack11l1l1l1l_opy_ import bstack11l1l1l1l_opy_, Events, bstack1ll1111111_opy_, bstack111ll1l11_opy_
from bstack_utils.measure import bstack1ll1ll1lll_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1ll1l111l1_opy_ import bstack11lllll1ll_opy_
from bstack_utils.messages import *
from bstack_utils import bstack11ll1111l_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack111l111l1l_opy_, bstack1l11l1111_opy_, bstack11llll111_opy_, bstack1ll111ll_opy_, \
  bstack11111lll1l_opy_, \
  Notset, bstack1l1ll1111_opy_, \
  bstack11l111llll_opy_, bstack11l1l1ll11_opy_, bstack11lll1ll11_opy_, bstack11l1lllll1_opy_, bstack11llll111l_opy_, bstack111l1ll11_opy_, \
  bstack1ll1l1ll1l_opy_, \
  bstack111ll111l_opy_, bstack1l1lll111l_opy_, bstack1111l1l1ll_opy_, bstack111lll1l1_opy_, \
  bstack1111l1l11_opy_, bstack1l11l1l11_opy_, bstack111llll1l_opy_, bstack11lll1l1l1_opy_
from bstack_utils.bstack11l11ll111_opy_ import bstack11111lll11_opy_
from bstack_utils.bstack11lll111l1_opy_ import bstack1111ll11l_opy_, bstack11111ll11_opy_
from bstack_utils.bstack11l11l1ll1_opy_ import bstack11ll1l111l_opy_
from bstack_utils.bstack1lll11111l_opy_ import bstack1l1ll1l11l_opy_, bstack11ll1l1l1l_opy_
from bstack_utils.bstack11111ll1l_opy_ import bstack11111ll1l_opy_
from bstack_utils.bstack11l1l11lll_opy_ import bstack111l1lllll_opy_
from bstack_utils.proxy import bstack1llllllll1_opy_, bstack1lll1lll11_opy_, bstack1l11l11lll_opy_, bstack11ll1111ll_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack1ll1l1ll11_opy_
import bstack_utils.bstack1111ll11l1_opy_ as bstack11lll11lll_opy_
import bstack_utils.bstack1lll1ll1l1_opy_ as bstack11111lllll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack111l1111l1_opy_ import bstack1l11111111_opy_
from bstack_utils.bstack1lll1l11l_opy_ import bstack111l1l1l_opy_
from bstack_utils.bstack1111lllll_opy_ import bstack11l1ll1ll_opy_
if os.getenv(bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡋࡓࡔࡑࡓࠨੜ")):
  cli.bstack1l11lll1l_opy_()
else:
  os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡃࡍࡋࡢࡌࡔࡕࡋࡔࠩ੝")] = bstack1lll11l_opy_ (u"ࠨࡶࡵࡹࡪ࠭ਫ਼")
bstack1l1ll1l11_opy_ = bstack1lll11l_opy_ (u"ࠩࠣࠤ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࠢࠣ࡭࡫࠮ࡰࡢࡩࡨࠤࡂࡃ࠽ࠡࡸࡲ࡭ࡩࠦ࠰ࠪࠢࡾࡠࡳࠦࠠࠡࡶࡵࡽࢀࡢ࡮ࠡࡥࡲࡲࡸࡺࠠࡧࡵࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮࡜ࠨࡨࡶࡠࠬ࠯࠻࡝ࡰࠣࠤࠥࠦࠠࡧࡵ࠱ࡥࡵࡶࡥ࡯ࡦࡉ࡭ࡱ࡫ࡓࡺࡰࡦࠬࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩ࠮ࠣࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡵࡥࡩ࡯ࡦࡨࡼ࠮ࠦࠫࠡࠤ࠽ࠦࠥ࠱ࠠࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭࠮ࡡࡸࡣ࡬ࡸࠥࡴࡥࡸࡒࡤ࡫ࡪ࠸࠮ࡦࡸࡤࡰࡺࡧࡴࡦࠪࠥࠬ࠮ࠦ࠽࠿ࠢࡾࢁࠧ࠲ࠠ࡝ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡪࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡥࡵࡣ࡬ࡰࡸࠨࡽ࡝ࠩࠬ࠭࠮ࡡࠢࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠥࡡ࠮ࠦࠫࠡࠤ࠯ࡠࡡࡴࠢࠪ࡞ࡱࠤࠥࠦࠠࡾࡥࡤࡸࡨ࡮ࠨࡦࡺࠬࡿࡡࡴࠠࠡࠢࠣࢁࡡࡴࠠࠡࡿ࡟ࡲࠥࠦ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠩ੟")
bstack1lllll1lll_opy_ = bstack1lll11l_opy_ (u"ࠪࡠࡳ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯࡝ࡰࡦࡳࡳࡹࡴࠡࡤࡶࡸࡦࡩ࡫ࡠࡲࡤࡸ࡭ࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࡛ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴࡬ࡦࡰࡪࡸ࡭ࠦ࠭ࠡ࠵ࡠࡠࡳࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠶ࡣ࡜࡯ࡥࡲࡲࡸࡺࠠࡱࡡ࡬ࡲࡩ࡫ࡸࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠶ࡢࡢ࡮ࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࠦ࠽ࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮ࡴ࡮࡬ࡧࡪ࠮࠰࠭ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷࠮ࡢ࡮ࡤࡱࡱࡷࡹࠦࡩ࡮ࡲࡲࡶࡹࡥࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶ࠷ࡣࡧࡹࡴࡢࡥ࡮ࠤࡂࠦࡲࡦࡳࡸ࡭ࡷ࡫ࠨࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ࠯࠻࡝ࡰ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰࡯ࡥࡺࡴࡣࡩࠢࡀࠤࡦࡹࡹ࡯ࡥࠣࠬࡱࡧࡵ࡯ࡥ࡫ࡓࡵࡺࡩࡰࡰࡶ࠭ࠥࡃ࠾ࠡࡽ࡟ࡲࡱ࡫ࡴࠡࡥࡤࡴࡸࡁ࡜࡯ࡶࡵࡽࠥࢁ࡜࡯ࡥࡤࡴࡸࠦ࠽ࠡࡌࡖࡓࡓ࠴ࡰࡢࡴࡶࡩ࠭ࡨࡳࡵࡣࡦ࡯ࡤࡩࡡࡱࡵࠬࡠࡳࠦࠠࡾࠢࡦࡥࡹࡩࡨࠩࡧࡻ࠭ࠥࢁ࡜࡯ࠢࠣࠤࠥࢃ࡜࡯ࠢࠣࡶࡪࡺࡵࡳࡰࠣࡥࡼࡧࡩࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱ࠮ࡤࡪࡵࡳࡲ࡯ࡵ࡮࠰ࡦࡳࡳࡴࡥࡤࡶࠫࡿࡡࡴࠠࠡࠢࠣࡻࡸࡋ࡮ࡥࡲࡲ࡭ࡳࡺ࠺ࠡࡢࡺࡷࡸࡀ࠯࠰ࡥࡧࡴ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࡄࡩࡡࡱࡵࡀࠨࢀ࡫࡮ࡤࡱࡧࡩ࡚ࡘࡉࡄࡱࡰࡴࡴࡴࡥ࡯ࡶࠫࡎࡘࡕࡎ࠯ࡵࡷࡶ࡮ࡴࡧࡪࡨࡼࠬࡨࡧࡰࡴࠫࠬࢁࡥ࠲࡜࡯ࠢࠣࠤࠥ࠴࠮࠯࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳ࡝ࡰࠣࠤࢂ࠯࡜࡯ࡿ࡟ࡲ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࠩ੠")
from ._version import __version__
bstack111111ll1_opy_ = None
CONFIG = {}
bstack1l1111ll11_opy_ = {}
bstack1l1l11111l_opy_ = {}
bstack1l11l1l1ll_opy_ = None
bstack1lll11l111_opy_ = None
bstack11ll1lll1_opy_ = None
bstack11ll11ll1l_opy_ = -1
bstack1lllllll11_opy_ = 0
bstack111l11l1ll_opy_ = bstack11l11ll11_opy_
bstack1llll1lll1_opy_ = 1
bstack1l111l11l_opy_ = False
bstack1l11ll11ll_opy_ = False
bstack1l11l11ll_opy_ = bstack1lll11l_opy_ (u"ࠫࠬ੡")
bstack1l1lll111_opy_ = bstack1lll11l_opy_ (u"ࠬ࠭੢")
bstack11llllll1_opy_ = False
bstack111ll1llll_opy_ = True
bstack1llll1l111_opy_ = bstack1lll11l_opy_ (u"࠭ࠧ੣")
bstack1l1lll1ll_opy_ = []
bstack1ll111l111_opy_ = threading.Lock()
bstack1ll1lll1ll_opy_ = threading.Lock()
bstack111l1llll_opy_ = bstack1lll11l_opy_ (u"ࠧࠨ੤")
bstack1ll11llll_opy_ = False
bstack11llll1l11_opy_ = None
bstack111lllllll_opy_ = None
bstack1l1ll11l1l_opy_ = None
bstack1l1l1l11ll_opy_ = -1
bstack1l1l1ll111_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠨࢀࠪ੥")), bstack1lll11l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ੦"), bstack1lll11l_opy_ (u"ࠪ࠲ࡷࡵࡢࡰࡶ࠰ࡶࡪࡶ࡯ࡳࡶ࠰࡬ࡪࡲࡰࡦࡴ࠱࡮ࡸࡵ࡮ࠨ੧"))
bstack111l11llll_opy_ = 0
bstack11ll11l11l_opy_ = 0
bstack11l1ll1l1_opy_ = []
bstack11l1l111l_opy_ = []
bstack111ll1l1ll_opy_ = []
bstack1l1l1l1ll1_opy_ = []
bstack111l1111l_opy_ = bstack1lll11l_opy_ (u"ࠫࠬ੨")
bstack1l11111ll_opy_ = bstack1lll11l_opy_ (u"ࠬ࠭੩")
bstack1lll11lll1_opy_ = False
bstack1ll1111ll_opy_ = False
bstack111l11l11l_opy_ = {}
bstack1l11l1lll_opy_ = None
bstack11l1111ll1_opy_ = None
bstack1111lll11_opy_ = None
bstack1l11l1l1l_opy_ = None
bstack11lll111ll_opy_ = None
bstack11lll1111l_opy_ = None
bstack1l111ll1l1_opy_ = None
bstack1lll1ll1ll_opy_ = None
bstack111l11111l_opy_ = None
bstack1l1l111ll1_opy_ = None
bstack1ll1ll1ll_opy_ = None
bstack1ll1llll1_opy_ = None
bstack11l1l1l11l_opy_ = None
bstack1ll1l11l1_opy_ = None
bstack11l111ll1l_opy_ = None
bstack1ll111l11_opy_ = None
bstack1llll11lll_opy_ = None
bstack1lll111l1l_opy_ = None
bstack1lll11111_opy_ = None
bstack1llll11l1l_opy_ = None
bstack1ll11l1ll_opy_ = None
bstack1ll111llll_opy_ = None
bstack1ll1ll1l1_opy_ = None
thread_local = threading.local()
bstack1lll11l11l_opy_ = False
bstack1ll11l1111_opy_ = bstack1lll11l_opy_ (u"ࠨࠢ੪")
logger = bstack11ll1111l_opy_.get_logger(__name__, bstack111l11l1ll_opy_)
bstack111ll1l1_opy_ = Config.bstack111l1111_opy_()
percy = bstack11l11lll11_opy_()
bstack1ll11lll1l_opy_ = bstack11lllll1ll_opy_()
bstack111ll1l11l_opy_ = bstack11l1l111_opy_()
def bstack11ll1l11ll_opy_():
  global CONFIG
  global bstack1lll11lll1_opy_
  global bstack111ll1l1_opy_
  testContextOptions = bstack1l1ll1ll1_opy_(CONFIG)
  if bstack11111lll1l_opy_(CONFIG):
    if (bstack1lll11l_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ੫") in testContextOptions and str(testContextOptions[bstack1lll11l_opy_ (u"ࠨࡵ࡮࡭ࡵ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ੬")]).lower() == bstack1lll11l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ੭")):
      bstack1lll11lll1_opy_ = True
    bstack111ll1l1_opy_.bstack1l11ll11l_opy_(testContextOptions.get(bstack1lll11l_opy_ (u"ࠪࡷࡰ࡯ࡰࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ੮"), False))
  else:
    bstack1lll11lll1_opy_ = True
    bstack111ll1l1_opy_.bstack1l11ll11l_opy_(True)
def bstack11l11l11ll_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack111l1l111l_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack111ll111ll_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack1lll11l_opy_ (u"ࠦ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡨࡵ࡮ࡧ࡫ࡪࡪ࡮ࡲࡥࠣ੯") == args[i].lower() or bstack1lll11l_opy_ (u"ࠧ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰࡰࡩ࡭࡬ࠨੰ") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1llll1l111_opy_
      bstack1llll1l111_opy_ += bstack1lll11l_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡃࡰࡰࡩ࡭࡬ࡌࡩ࡭ࡧࠣࠫੱ") + shlex.quote(path)
      return path
  return None
bstack111l1l11l1_opy_ = re.compile(bstack1lll11l_opy_ (u"ࡲࠣ࠰࠭ࡃࡡࠪࡻࠩ࠰࠭ࡃ࠮ࢃ࠮ࠫࡁࠥੲ"))
def bstack1l1l1111l1_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack111l1l11l1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack1lll11l_opy_ (u"ࠣࠦࡾࠦੳ") + group + bstack1lll11l_opy_ (u"ࠤࢀࠦੴ"), os.environ.get(group))
  return value
def bstack11l11l1111_opy_():
  global bstack1ll1ll1l1_opy_
  if bstack1ll1ll1l1_opy_ is None:
        bstack1ll1ll1l1_opy_ = bstack111ll111ll_opy_()
  bstack1l1ll11l1_opy_ = bstack1ll1ll1l1_opy_
  if bstack1l1ll11l1_opy_ and os.path.exists(os.path.abspath(bstack1l1ll11l1_opy_)):
    fileName = bstack1l1ll11l1_opy_
  if bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧੵ") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡇࡔࡔࡆࡊࡉࡢࡊࡎࡒࡅࠨ੶")])) and not bstack1lll11l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡑࡥࡲ࡫ࠧ੷") in locals():
    fileName = os.environ[bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡏࡏࡈࡌࡋࡤࡌࡉࡍࡇࠪ੸")]
  if bstack1lll11l_opy_ (u"ࠧࡧ࡫࡯ࡩࡓࡧ࡭ࡦࠩ੹") in locals():
    bstack1ll111l_opy_ = os.path.abspath(fileName)
  else:
    bstack1ll111l_opy_ = bstack1lll11l_opy_ (u"ࠨࠩ੺")
  bstack111l1l1l1_opy_ = os.getcwd()
  bstack1l1lll1l11_opy_ = bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡰࡰࠬ੻")
  bstack1ll1l1111l_opy_ = bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡼࡥࡲࡲࠧ੼")
  while (not os.path.exists(bstack1ll111l_opy_)) and bstack111l1l1l1_opy_ != bstack1lll11l_opy_ (u"ࠦࠧ੽"):
    bstack1ll111l_opy_ = os.path.join(bstack111l1l1l1_opy_, bstack1l1lll1l11_opy_)
    if not os.path.exists(bstack1ll111l_opy_):
      bstack1ll111l_opy_ = os.path.join(bstack111l1l1l1_opy_, bstack1ll1l1111l_opy_)
    if bstack111l1l1l1_opy_ != os.path.dirname(bstack111l1l1l1_opy_):
      bstack111l1l1l1_opy_ = os.path.dirname(bstack111l1l1l1_opy_)
    else:
      bstack111l1l1l1_opy_ = bstack1lll11l_opy_ (u"ࠧࠨ੾")
  bstack1ll1ll1l1_opy_ = bstack1ll111l_opy_ if os.path.exists(bstack1ll111l_opy_) else None
  return bstack1ll1ll1l1_opy_
def bstack1l1l11l11_opy_(config):
    if bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡖࡪࡶ࡯ࡳࡶ࡬ࡲ࡬࠭੿") in config:
      config[bstack1lll11l_opy_ (u"ࠧࡵࡧࡶࡸࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ઀")] = config[bstack1lll11l_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࠨઁ")]
    if bstack1lll11l_opy_ (u"ࠩࡷࡩࡸࡺࡒࡦࡲࡲࡶࡹ࡯࡮ࡨࡑࡳࡸ࡮ࡵ࡮ࡴࠩં") in config:
      config[bstack1lll11l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡤࡶࡩࡷࡼࡡࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧઃ")] = config[bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࡓࡵࡺࡩࡰࡰࡶࠫ઄")]
def bstack111llllll1_opy_():
  bstack1ll111l_opy_ = bstack11l11l1111_opy_()
  if not os.path.exists(bstack1ll111l_opy_):
    bstack11l1ll1l1l_opy_(
      bstack11l1ll111_opy_.format(os.getcwd()))
  try:
    with open(bstack1ll111l_opy_, bstack1lll11l_opy_ (u"ࠬࡸࠧઅ")) as stream:
      yaml.add_implicit_resolver(bstack1lll11l_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢઆ"), bstack111l1l11l1_opy_)
      yaml.add_constructor(bstack1lll11l_opy_ (u"ࠢࠢࡲࡤࡸ࡭࡫ࡸࠣઇ"), bstack1l1l1111l1_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack1l1l11l11_opy_(config)
      return config
  except:
    with open(bstack1ll111l_opy_, bstack1lll11l_opy_ (u"ࠨࡴࠪઈ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack1l1l11l11_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack11l1ll1l1l_opy_(bstack1111llll1_opy_.format(str(exc)))
def bstack1l1llll1l1_opy_(config):
  bstack1llll11l11_opy_ = bstack11l1l1llll_opy_(config)
  for option in list(bstack1llll11l11_opy_):
    if option.lower() in bstack111l1l1lll_opy_ and option != bstack111l1l1lll_opy_[option.lower()]:
      bstack1llll11l11_opy_[bstack111l1l1lll_opy_[option.lower()]] = bstack1llll11l11_opy_[option]
      del bstack1llll11l11_opy_[option]
  return config
def bstack11ll11llll_opy_():
  global bstack1l1l11111l_opy_
  for key, bstack1111111ll_opy_ in bstack1ll1lllll1_opy_.items():
    if isinstance(bstack1111111ll_opy_, list):
      for var in bstack1111111ll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack1l1l11111l_opy_[key] = os.environ[var]
          break
    elif bstack1111111ll_opy_ in os.environ and os.environ[bstack1111111ll_opy_] and str(os.environ[bstack1111111ll_opy_]).strip():
      bstack1l1l11111l_opy_[key] = os.environ[bstack1111111ll_opy_]
  if bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫઉ") in os.environ:
    bstack1l1l11111l_opy_[bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧઊ")] = {}
    bstack1l1l11111l_opy_[bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨઋ")][bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઌ")] = os.environ[bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨઍ")]
def bstack1ll11l1l1_opy_():
  global bstack1l1111ll11_opy_
  global bstack1llll1l111_opy_
  bstack1l111l1lll_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack1lll11l_opy_ (u"ࠧ࠮࠯ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ઎").lower() == val.lower():
      bstack1l1111ll11_opy_[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬએ")] = {}
      bstack1l1111ll11_opy_[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ઐ")][bstack1lll11l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬઑ")] = sys.argv[idx + 1]
      bstack1l111l1lll_opy_.extend([idx, idx + 1])
      break
  for key, bstack1ll1111l11_opy_ in bstack11ll1l1ll1_opy_.items():
    if isinstance(bstack1ll1111l11_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack1ll1111l11_opy_:
          if bstack1lll11l_opy_ (u"ࠫ࠲࠳ࠧ઒") + var.lower() == val.lower() and key not in bstack1l1111ll11_opy_:
            bstack1l1111ll11_opy_[key] = sys.argv[idx + 1]
            bstack1llll1l111_opy_ += bstack1lll11l_opy_ (u"ࠬࠦ࠭࠮ࠩઓ") + var + bstack1lll11l_opy_ (u"࠭ࠠࠨઔ") + shlex.quote(sys.argv[idx + 1])
            bstack1l111l1lll_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack1lll11l_opy_ (u"ࠧ࠮࠯ࠪક") + bstack1ll1111l11_opy_.lower() == val.lower() and key not in bstack1l1111ll11_opy_:
          bstack1l1111ll11_opy_[key] = sys.argv[idx + 1]
          bstack1llll1l111_opy_ += bstack1lll11l_opy_ (u"ࠨࠢ࠰࠱ࠬખ") + bstack1ll1111l11_opy_ + bstack1lll11l_opy_ (u"ࠩࠣࠫગ") + shlex.quote(sys.argv[idx + 1])
          bstack1l111l1lll_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack1l111l1lll_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack1111ll1ll_opy_(config):
  bstack11l11l1lll_opy_ = config.keys()
  for bstack1l1111111_opy_, bstack1l11l1l1l1_opy_ in bstack1111lll11l_opy_.items():
    if bstack1l11l1l1l1_opy_ in bstack11l11l1lll_opy_:
      config[bstack1l1111111_opy_] = config[bstack1l11l1l1l1_opy_]
      del config[bstack1l11l1l1l1_opy_]
  for bstack1l1111111_opy_, bstack1l11l1l1l1_opy_ in bstack11lll11l1l_opy_.items():
    if isinstance(bstack1l11l1l1l1_opy_, list):
      for bstack1l1l11111_opy_ in bstack1l11l1l1l1_opy_:
        if bstack1l1l11111_opy_ in bstack11l11l1lll_opy_:
          config[bstack1l1111111_opy_] = config[bstack1l1l11111_opy_]
          del config[bstack1l1l11111_opy_]
          break
    elif bstack1l11l1l1l1_opy_ in bstack11l11l1lll_opy_:
      config[bstack1l1111111_opy_] = config[bstack1l11l1l1l1_opy_]
      del config[bstack1l11l1l1l1_opy_]
  for bstack1l1l11111_opy_ in list(config):
    for bstack1ll111l1l1_opy_ in bstack1l1lll1l1_opy_:
      if bstack1l1l11111_opy_.lower() == bstack1ll111l1l1_opy_.lower() and bstack1l1l11111_opy_ != bstack1ll111l1l1_opy_:
        config[bstack1ll111l1l1_opy_] = config[bstack1l1l11111_opy_]
        del config[bstack1l1l11111_opy_]
  bstack1l1llllll1_opy_ = [{}]
  if not config.get(bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ઘ")):
    config[bstack1lll11l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧઙ")] = [{}]
  bstack1l1llllll1_opy_ = config[bstack1lll11l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨચ")]
  for platform in bstack1l1llllll1_opy_:
    for bstack1l1l11111_opy_ in list(platform):
      for bstack1ll111l1l1_opy_ in bstack1l1lll1l1_opy_:
        if bstack1l1l11111_opy_.lower() == bstack1ll111l1l1_opy_.lower() and bstack1l1l11111_opy_ != bstack1ll111l1l1_opy_:
          platform[bstack1ll111l1l1_opy_] = platform[bstack1l1l11111_opy_]
          del platform[bstack1l1l11111_opy_]
  for bstack1l1111111_opy_, bstack1l11l1l1l1_opy_ in bstack11lll11l1l_opy_.items():
    for platform in bstack1l1llllll1_opy_:
      if isinstance(bstack1l11l1l1l1_opy_, list):
        for bstack1l1l11111_opy_ in bstack1l11l1l1l1_opy_:
          if bstack1l1l11111_opy_ in platform:
            platform[bstack1l1111111_opy_] = platform[bstack1l1l11111_opy_]
            del platform[bstack1l1l11111_opy_]
            break
      elif bstack1l11l1l1l1_opy_ in platform:
        platform[bstack1l1111111_opy_] = platform[bstack1l11l1l1l1_opy_]
        del platform[bstack1l11l1l1l1_opy_]
  for bstack1l11111l1_opy_ in bstack111l1l1ll_opy_:
    if bstack1l11111l1_opy_ in config:
      if not bstack111l1l1ll_opy_[bstack1l11111l1_opy_] in config:
        config[bstack111l1l1ll_opy_[bstack1l11111l1_opy_]] = {}
      config[bstack111l1l1ll_opy_[bstack1l11111l1_opy_]].update(config[bstack1l11111l1_opy_])
      del config[bstack1l11111l1_opy_]
  for platform in bstack1l1llllll1_opy_:
    for bstack1l11111l1_opy_ in bstack111l1l1ll_opy_:
      if bstack1l11111l1_opy_ in list(platform):
        if not bstack111l1l1ll_opy_[bstack1l11111l1_opy_] in platform:
          platform[bstack111l1l1ll_opy_[bstack1l11111l1_opy_]] = {}
        platform[bstack111l1l1ll_opy_[bstack1l11111l1_opy_]].update(platform[bstack1l11111l1_opy_])
        del platform[bstack1l11111l1_opy_]
  config = bstack1l1llll1l1_opy_(config)
  return config
def bstack11l11l111_opy_(config):
  global bstack1l1lll111_opy_
  bstack111ll11l11_opy_ = False
  if bstack1lll11l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪછ") in config and str(config[bstack1lll11l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫજ")]).lower() != bstack1lll11l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧઝ"):
    if bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ઞ") not in config or str(config[bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧટ")]).lower() == bstack1lll11l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪઠ"):
      config[bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫડ")] = False
    else:
      bstack111l1ll1l1_opy_ = bstack11ll111l1_opy_()
      if bstack1lll11l_opy_ (u"࠭ࡩࡴࡖࡵ࡭ࡦࡲࡇࡳ࡫ࡧࠫઢ") in bstack111l1ll1l1_opy_:
        if not bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫણ") in config:
          config[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬત")] = {}
        config[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭થ")][bstack1lll11l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬદ")] = bstack1lll11l_opy_ (u"ࠫࡦࡺࡳ࠮ࡴࡨࡴࡪࡧࡴࡦࡴࠪધ")
        bstack111ll11l11_opy_ = True
        bstack1l1lll111_opy_ = config[bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩન")].get(bstack1lll11l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ઩"))
  if bstack11111lll1l_opy_(config) and bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫપ") in config and str(config[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬફ")]).lower() != bstack1lll11l_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨબ") and not bstack111ll11l11_opy_:
    if not bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧભ") in config:
      config[bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨમ")] = {}
    if not config[bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩય")].get(bstack1lll11l_opy_ (u"࠭ࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠪર")) and not bstack1lll11l_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઱") in config[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬલ")]:
      bstack1l111lll_opy_ = datetime.datetime.now()
      bstack1l1l1ll11_opy_ = bstack1l111lll_opy_.strftime(bstack1lll11l_opy_ (u"ࠩࠨࡨࡤࠫࡢࡠࠧࡋࠩࡒ࠭ળ"))
      hostname = socket.gethostname()
      bstack1l1l11l1l1_opy_ = bstack1lll11l_opy_ (u"ࠪࠫ઴").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack1lll11l_opy_ (u"ࠫࢀࢃ࡟ࡼࡿࡢࡿࢂ࠭વ").format(bstack1l1l1ll11_opy_, hostname, bstack1l1l11l1l1_opy_)
      config[bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩશ")][bstack1lll11l_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨષ")] = identifier
    bstack1l1lll111_opy_ = config[bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫસ")].get(bstack1lll11l_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪહ"))
  return config
def bstack11lll1ll1l_opy_():
  bstack1ll11ll1ll_opy_ =  bstack11l1lllll1_opy_()[bstack1lll11l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠨ઺")]
  return bstack1ll11ll1ll_opy_ if bstack1ll11ll1ll_opy_ else -1
def bstack1l11l1llll_opy_(bstack1ll11ll1ll_opy_):
  global CONFIG
  if not bstack1lll11l_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬ઻") in CONFIG[bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ઼࠭")]:
    return
  CONFIG[bstack1lll11l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧઽ")] = CONFIG[bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨા")].replace(
    bstack1lll11l_opy_ (u"ࠧࠥࡽࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࡾࠩિ"),
    str(bstack1ll11ll1ll_opy_)
  )
def bstack1ll11ll1l1_opy_():
  global CONFIG
  if not bstack1lll11l_opy_ (u"ࠨࠦࡾࡈࡆ࡚ࡅࡠࡖࡌࡑࡊࢃࠧી") in CONFIG[bstack1lll11l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫુ")]:
    return
  bstack1l111lll_opy_ = datetime.datetime.now()
  bstack1l1l1ll11_opy_ = bstack1l111lll_opy_.strftime(bstack1lll11l_opy_ (u"ࠪࠩࡩ࠳ࠥࡣ࠯ࠨࡌ࠿ࠫࡍࠨૂ"))
  CONFIG[bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ૃ")] = CONFIG[bstack1lll11l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૄ")].replace(
    bstack1lll11l_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬૅ"),
    bstack1l1l1ll11_opy_
  )
def bstack11l11ll11l_opy_():
  global CONFIG
  if bstack1lll11l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૆") in CONFIG and not bool(CONFIG[bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪે")]):
    del CONFIG[bstack1lll11l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫૈ")]
    return
  if not bstack1lll11l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૉ") in CONFIG:
    CONFIG[bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૊")] = bstack1lll11l_opy_ (u"ࠬࠩࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨો")
  if bstack1lll11l_opy_ (u"࠭ࠤࡼࡆࡄࡘࡊࡥࡔࡊࡏࡈࢁࠬૌ") in CONFIG[bstack1lll11l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳ્ࠩ")]:
    bstack1ll11ll1l1_opy_()
    os.environ[bstack1lll11l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ૎")] = CONFIG[bstack1lll11l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૏")]
  if not bstack1lll11l_opy_ (u"ࠪࠨࢀࡈࡕࡊࡎࡇࡣࡓ࡛ࡍࡃࡇࡕࢁࠬૐ") in CONFIG[bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૑")]:
    return
  bstack1ll11ll1ll_opy_ = bstack1lll11l_opy_ (u"ࠬ࠭૒")
  bstack11111l1111_opy_ = bstack11lll1ll1l_opy_()
  if bstack11111l1111_opy_ != -1:
    bstack1ll11ll1ll_opy_ = bstack1lll11l_opy_ (u"࠭ࡃࡊࠢࠪ૓") + str(bstack11111l1111_opy_)
  if bstack1ll11ll1ll_opy_ == bstack1lll11l_opy_ (u"ࠧࠨ૔"):
    bstack1l1l1l1111_opy_ = bstack1111l1lll1_opy_(CONFIG[bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ૕")])
    if bstack1l1l1l1111_opy_ != -1:
      bstack1ll11ll1ll_opy_ = str(bstack1l1l1l1111_opy_)
  if bstack1ll11ll1ll_opy_:
    bstack1l11l1llll_opy_(bstack1ll11ll1ll_opy_)
    os.environ[bstack1lll11l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡡࡆࡓࡒࡈࡉࡏࡇࡇࡣࡇ࡛ࡉࡍࡆࡢࡍࡉ࠭૖")] = CONFIG[bstack1lll11l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૗")]
def bstack1l11l1l11l_opy_(bstack1l1ll11lll_opy_, bstack11ll1l1lll_opy_, path):
  json_data = {
    bstack1lll11l_opy_ (u"ࠫ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૘"): bstack11ll1l1lll_opy_
  }
  if os.path.exists(path):
    bstack111l1ll111_opy_ = json.load(open(path, bstack1lll11l_opy_ (u"ࠬࡸࡢࠨ૙")))
  else:
    bstack111l1ll111_opy_ = {}
  bstack111l1ll111_opy_[bstack1l1ll11lll_opy_] = json_data
  with open(path, bstack1lll11l_opy_ (u"ࠨࡷࠬࠤ૚")) as outfile:
    json.dump(bstack111l1ll111_opy_, outfile)
def bstack1111l1lll1_opy_(bstack1l1ll11lll_opy_):
  bstack1l1ll11lll_opy_ = str(bstack1l1ll11lll_opy_)
  bstack111lll1ll1_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠧࡿࠩ૛")), bstack1lll11l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ૜"))
  try:
    if not os.path.exists(bstack111lll1ll1_opy_):
      os.makedirs(bstack111lll1ll1_opy_)
    file_path = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠩࢁࠫ૝")), bstack1lll11l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪ૞"), bstack1lll11l_opy_ (u"ࠫ࠳ࡨࡵࡪ࡮ࡧ࠱ࡳࡧ࡭ࡦ࠯ࡦࡥࡨ࡮ࡥ࠯࡬ࡶࡳࡳ࠭૟"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack1lll11l_opy_ (u"ࠬࡽࠧૠ")):
        pass
      with open(file_path, bstack1lll11l_opy_ (u"ࠨࡷࠬࠤૡ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack1lll11l_opy_ (u"ࠧࡳࠩૢ")) as bstack111ll11lll_opy_:
      bstack11lll11111_opy_ = json.load(bstack111ll11lll_opy_)
    if bstack1l1ll11lll_opy_ in bstack11lll11111_opy_:
      bstack11111l1l1l_opy_ = bstack11lll11111_opy_[bstack1l1ll11lll_opy_][bstack1lll11l_opy_ (u"ࠨ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬૣ")]
      bstack11l1l1lll_opy_ = int(bstack11111l1l1l_opy_) + 1
      bstack1l11l1l11l_opy_(bstack1l1ll11lll_opy_, bstack11l1l1lll_opy_, file_path)
      return bstack11l1l1lll_opy_
    else:
      bstack1l11l1l11l_opy_(bstack1l1ll11lll_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1lll1111ll_opy_.format(str(e)))
    return -1
def bstack1lll111l11_opy_(config):
  if not config[bstack1lll11l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ૤")] or not config[bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭૥")]:
    return True
  else:
    return False
def bstack11111lll1_opy_(config, index=0):
  global bstack11llllll1_opy_
  bstack1l11ll1l1_opy_ = {}
  caps = bstack1l1ll11ll1_opy_ + bstack1l1llllll_opy_
  if config.get(bstack1lll11l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ૦"), False):
    bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ૧")] = True
    bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ૨")] = config.get(bstack1lll11l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࡓࡵࡺࡩࡰࡰࡶࠫ૩"), {})
  if bstack11llllll1_opy_:
    caps += bstack11lll1l1l_opy_
  for key in config:
    if key in caps + [bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૪")]:
      continue
    bstack1l11ll1l1_opy_[key] = config[key]
  if bstack1lll11l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ૫") in config:
    for bstack11l111l111_opy_ in config[bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૬")][index]:
      if bstack11l111l111_opy_ in caps:
        continue
      bstack1l11ll1l1_opy_[bstack11l111l111_opy_] = config[bstack1lll11l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ૭")][index][bstack11l111l111_opy_]
  bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"ࠬ࡮࡯ࡴࡶࡑࡥࡲ࡫ࠧ૮")] = socket.gethostname()
  if bstack1lll11l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧ૯") in bstack1l11ll1l1_opy_:
    del (bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ૰")])
  return bstack1l11ll1l1_opy_
def bstack1l1l111l11_opy_(config):
  global bstack11llllll1_opy_
  bstack111lll1l1l_opy_ = {}
  caps = bstack1l1llllll_opy_
  if bstack11llllll1_opy_:
    caps += bstack11lll1l1l_opy_
  for key in caps:
    if key in config:
      bstack111lll1l1l_opy_[key] = config[key]
  return bstack111lll1l1l_opy_
def bstack111ll1l1l1_opy_(bstack1l11ll1l1_opy_, bstack111lll1l1l_opy_):
  bstack1ll1lll111_opy_ = {}
  for key in bstack1l11ll1l1_opy_.keys():
    if key in bstack1111lll11l_opy_:
      bstack1ll1lll111_opy_[bstack1111lll11l_opy_[key]] = bstack1l11ll1l1_opy_[key]
    else:
      bstack1ll1lll111_opy_[key] = bstack1l11ll1l1_opy_[key]
  for key in bstack111lll1l1l_opy_:
    if key in bstack1111lll11l_opy_:
      bstack1ll1lll111_opy_[bstack1111lll11l_opy_[key]] = bstack111lll1l1l_opy_[key]
    else:
      bstack1ll1lll111_opy_[key] = bstack111lll1l1l_opy_[key]
  return bstack1ll1lll111_opy_
def bstack1llll11111_opy_(config, index=0):
  global bstack11llllll1_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack11l1l1l111_opy_ = bstack111l111l1l_opy_(bstack1l1l1ll1ll_opy_, config, logger)
  bstack111lll1l1l_opy_ = bstack1l1l111l11_opy_(config)
  bstack1l11llll1l_opy_ = bstack1l1llllll_opy_
  bstack1l11llll1l_opy_ += bstack1l1l1l1l1_opy_
  bstack111lll1l1l_opy_ = update(bstack111lll1l1l_opy_, bstack11l1l1l111_opy_)
  if bstack11llllll1_opy_:
    bstack1l11llll1l_opy_ += bstack11lll1l1l_opy_
  if bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૱") in config:
    if bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ૲") in config[bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭૳")][index]:
      caps[bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ૴")] = config[bstack1lll11l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ૵")][index][bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ૶")]
    if bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ૷") in config[bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૸")][index]:
      caps[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪૹ")] = str(config[bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ૺ")][index][bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬૻ")])
    bstack1lllll111l_opy_ = bstack111l111l1l_opy_(bstack1l1l1ll1ll_opy_, config[bstack1lll11l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨૼ")][index], logger)
    bstack1l11llll1l_opy_ += list(bstack1lllll111l_opy_.keys())
    for bstack11ll11ll1_opy_ in bstack1l11llll1l_opy_:
      if bstack11ll11ll1_opy_ in config[bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ૽")][index]:
        if bstack11ll11ll1_opy_ == bstack1lll11l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩ૾"):
          try:
            bstack1lllll111l_opy_[bstack11ll11ll1_opy_] = str(config[bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ૿")][index][bstack11ll11ll1_opy_] * 1.0)
          except:
            bstack1lllll111l_opy_[bstack11ll11ll1_opy_] = str(config[bstack1lll11l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ଀")][index][bstack11ll11ll1_opy_])
        else:
          bstack1lllll111l_opy_[bstack11ll11ll1_opy_] = config[bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଁ")][index][bstack11ll11ll1_opy_]
        del (config[bstack1lll11l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଂ")][index][bstack11ll11ll1_opy_])
    bstack111lll1l1l_opy_ = update(bstack111lll1l1l_opy_, bstack1lllll111l_opy_)
  bstack1l11ll1l1_opy_ = bstack11111lll1_opy_(config, index)
  for bstack1l1l11111_opy_ in bstack1l1llllll_opy_ + list(bstack11l1l1l111_opy_.keys()):
    if bstack1l1l11111_opy_ in bstack1l11ll1l1_opy_:
      bstack111lll1l1l_opy_[bstack1l1l11111_opy_] = bstack1l11ll1l1_opy_[bstack1l1l11111_opy_]
      del (bstack1l11ll1l1_opy_[bstack1l1l11111_opy_])
  if bstack1l1ll1111_opy_(config):
    bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"ࠬࡻࡳࡦ࡙࠶ࡇࠬଃ")] = True
    caps.update(bstack111lll1l1l_opy_)
    caps[bstack1lll11l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ଄")] = bstack1l11ll1l1_opy_
  else:
    bstack1l11ll1l1_opy_[bstack1lll11l_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧଅ")] = False
    caps.update(bstack111ll1l1l1_opy_(bstack1l11ll1l1_opy_, bstack111lll1l1l_opy_))
    if bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ଆ") in caps:
      caps[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪଇ")] = caps[bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଈ")]
      del (caps[bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩଉ")])
    if bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ଊ") in caps:
      caps[bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨଋ")] = caps[bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨଌ")]
      del (caps[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ଍")])
  return caps
def bstack11l11lll1l_opy_():
  global bstack111l1llll_opy_
  global CONFIG
  if bstack111l1l111l_opy_() <= version.parse(bstack1lll11l_opy_ (u"ࠩ࠶࠲࠶࠹࠮࠱ࠩ଎")):
    if bstack111l1llll_opy_ != bstack1lll11l_opy_ (u"ࠪࠫଏ"):
      return bstack1lll11l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧଐ") + bstack111l1llll_opy_ + bstack1lll11l_opy_ (u"ࠧࡀ࠸࠱࠱ࡺࡨ࠴࡮ࡵࡣࠤ଑")
    return bstack11l1l111ll_opy_
  if bstack111l1llll_opy_ != bstack1lll11l_opy_ (u"࠭ࠧ଒"):
    return bstack1lll11l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࠤଓ") + bstack111l1llll_opy_ + bstack1lll11l_opy_ (u"ࠣ࠱ࡺࡨ࠴࡮ࡵࡣࠤଔ")
  return bstack1ll1llllll_opy_
def bstack11l11l111l_opy_(options):
  return hasattr(options, bstack1lll11l_opy_ (u"ࠩࡶࡩࡹࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵࡻࠪକ"))
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
def bstack1l11ll1111_opy_(options, bstack111l1l11ll_opy_):
  for bstack1l1l1111l_opy_ in bstack111l1l11ll_opy_:
    if bstack1l1l1111l_opy_ in [bstack1lll11l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଖ"), bstack1lll11l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨଗ")]:
      continue
    if bstack1l1l1111l_opy_ in options._experimental_options:
      options._experimental_options[bstack1l1l1111l_opy_] = update(options._experimental_options[bstack1l1l1111l_opy_],
                                                         bstack111l1l11ll_opy_[bstack1l1l1111l_opy_])
    else:
      options.add_experimental_option(bstack1l1l1111l_opy_, bstack111l1l11ll_opy_[bstack1l1l1111l_opy_])
  if bstack1lll11l_opy_ (u"ࠬࡧࡲࡨࡵࠪଘ") in bstack111l1l11ll_opy_:
    for arg in bstack111l1l11ll_opy_[bstack1lll11l_opy_ (u"࠭ࡡࡳࡩࡶࠫଙ")]:
      options.add_argument(arg)
    del (bstack111l1l11ll_opy_[bstack1lll11l_opy_ (u"ࠧࡢࡴࡪࡷࠬଚ")])
  if bstack1lll11l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬଛ") in bstack111l1l11ll_opy_:
    for ext in bstack111l1l11ll_opy_[bstack1lll11l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ଜ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack111l1l11ll_opy_[bstack1lll11l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧଝ")])
def bstack1l11111lll_opy_(options, bstack1ll1l1l1l1_opy_):
  if bstack1lll11l_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪଞ") in bstack1ll1l1l1l1_opy_:
    for bstack11ll1lllll_opy_ in bstack1ll1l1l1l1_opy_[bstack1lll11l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫଟ")]:
      if bstack11ll1lllll_opy_ in options._preferences:
        options._preferences[bstack11ll1lllll_opy_] = update(options._preferences[bstack11ll1lllll_opy_], bstack1ll1l1l1l1_opy_[bstack1lll11l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬଠ")][bstack11ll1lllll_opy_])
      else:
        options.set_preference(bstack11ll1lllll_opy_, bstack1ll1l1l1l1_opy_[bstack1lll11l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ଡ")][bstack11ll1lllll_opy_])
  if bstack1lll11l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ଢ") in bstack1ll1l1l1l1_opy_:
    for arg in bstack1ll1l1l1l1_opy_[bstack1lll11l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧଣ")]:
      options.add_argument(arg)
def bstack11lll1llll_opy_(options, bstack1ll1l1l1l_opy_):
  if bstack1lll11l_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫତ") in bstack1ll1l1l1l_opy_:
    options.use_webview(bool(bstack1ll1l1l1l_opy_[bstack1lll11l_opy_ (u"ࠫࡼ࡫ࡢࡷ࡫ࡨࡻࠬଥ")]))
  bstack1l11ll1111_opy_(options, bstack1ll1l1l1l_opy_)
def bstack1111ll111l_opy_(options, bstack11l1l1lll1_opy_):
  for bstack11l1111ll_opy_ in bstack11l1l1lll1_opy_:
    if bstack11l1111ll_opy_ in [bstack1lll11l_opy_ (u"ࠬࡺࡥࡤࡪࡱࡳࡱࡵࡧࡺࡒࡵࡩࡻ࡯ࡥࡸࠩଦ"), bstack1lll11l_opy_ (u"࠭ࡡࡳࡩࡶࠫଧ")]:
      continue
    options.set_capability(bstack11l1111ll_opy_, bstack11l1l1lll1_opy_[bstack11l1111ll_opy_])
  if bstack1lll11l_opy_ (u"ࠧࡢࡴࡪࡷࠬନ") in bstack11l1l1lll1_opy_:
    for arg in bstack11l1l1lll1_opy_[bstack1lll11l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭଩")]:
      options.add_argument(arg)
  if bstack1lll11l_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭ପ") in bstack11l1l1lll1_opy_:
    options.bstack11lll11ll1_opy_(bool(bstack11l1l1lll1_opy_[bstack1lll11l_opy_ (u"ࠪࡸࡪࡩࡨ࡯ࡱ࡯ࡳ࡬ࡿࡐࡳࡧࡹ࡭ࡪࡽࠧଫ")]))
def bstack1l1l1l1l11_opy_(options, bstack1lll1l11ll_opy_):
  for bstack111l11lll1_opy_ in bstack1lll1l11ll_opy_:
    if bstack111l11lll1_opy_ in [bstack1lll11l_opy_ (u"ࠫࡦࡪࡤࡪࡶ࡬ࡳࡳࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨବ"), bstack1lll11l_opy_ (u"ࠬࡧࡲࡨࡵࠪଭ")]:
      continue
    options._options[bstack111l11lll1_opy_] = bstack1lll1l11ll_opy_[bstack111l11lll1_opy_]
  if bstack1lll11l_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪମ") in bstack1lll1l11ll_opy_:
    for bstack111ll1lll1_opy_ in bstack1lll1l11ll_opy_[bstack1lll11l_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫଯ")]:
      options.bstack11l111l11_opy_(
        bstack111ll1lll1_opy_, bstack1lll1l11ll_opy_[bstack1lll11l_opy_ (u"ࠨࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬର")][bstack111ll1lll1_opy_])
  if bstack1lll11l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ଱") in bstack1lll1l11ll_opy_:
    for arg in bstack1lll1l11ll_opy_[bstack1lll11l_opy_ (u"ࠪࡥࡷ࡭ࡳࠨଲ")]:
      options.add_argument(arg)
def bstack11l1l11l11_opy_(options, caps):
  if not hasattr(options, bstack1lll11l_opy_ (u"ࠫࡐࡋ࡙ࠨଳ")):
    return
  if options.KEY == bstack1lll11l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ଴"):
    options = bstack111ll1ll_opy_.bstack11l1ll11l_opy_(bstack11l1l11ll1_opy_=options, config=CONFIG)
  if options.KEY == bstack1lll11l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫଵ") and options.KEY in caps:
    bstack1l11ll1111_opy_(options, caps[bstack1lll11l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬଶ")])
  elif options.KEY == bstack1lll11l_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭ଷ") and options.KEY in caps:
    bstack1l11111lll_opy_(options, caps[bstack1lll11l_opy_ (u"ࠩࡰࡳࡿࡀࡦࡪࡴࡨࡪࡴࡾࡏࡱࡶ࡬ࡳࡳࡹࠧସ")])
  elif options.KEY == bstack1lll11l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫହ") and options.KEY in caps:
    bstack1111ll111l_opy_(options, caps[bstack1lll11l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬࠲ࡴࡶࡴࡪࡱࡱࡷࠬ଺")])
  elif options.KEY == bstack1lll11l_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭଻") and options.KEY in caps:
    bstack11lll1llll_opy_(options, caps[bstack1lll11l_opy_ (u"࠭࡭ࡴ࠼ࡨࡨ࡬࡫ࡏࡱࡶ࡬ࡳࡳࡹ଼ࠧ")])
  elif options.KEY == bstack1lll11l_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ଽ") and options.KEY in caps:
    bstack1l1l1l1l11_opy_(options, caps[bstack1lll11l_opy_ (u"ࠨࡵࡨ࠾࡮࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧା")])
def bstack1ll1l111ll_opy_(caps):
  global bstack11llllll1_opy_
  if isinstance(os.environ.get(bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪି")), str):
    bstack11llllll1_opy_ = eval(os.getenv(bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫୀ")))
  if bstack11llllll1_opy_:
    if bstack11l11l11ll_opy_() < version.parse(bstack1lll11l_opy_ (u"ࠫ࠷࠴࠳࠯࠲ࠪୁ")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack1lll11l_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬୂ")
    if bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫୃ") in caps:
      browser = caps[bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬୄ")]
    elif bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩ୅") in caps:
      browser = caps[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࠪ୆")]
    browser = str(browser).lower()
    if browser == bstack1lll11l_opy_ (u"ࠪ࡭ࡵ࡮࡯࡯ࡧࠪେ") or browser == bstack1lll11l_opy_ (u"ࠫ࡮ࡶࡡࡥࠩୈ"):
      browser = bstack1lll11l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬ୉")
    if browser == bstack1lll11l_opy_ (u"࠭ࡳࡢ࡯ࡶࡹࡳ࡭ࠧ୊"):
      browser = bstack1lll11l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧୋ")
    if browser not in [bstack1lll11l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨୌ"), bstack1lll11l_opy_ (u"ࠩࡨࡨ࡬࡫୍ࠧ"), bstack1lll11l_opy_ (u"ࠪ࡭ࡪ࠭୎"), bstack1lll11l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫ୏"), bstack1lll11l_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭୐")]:
      return None
    try:
      package = bstack1lll11l_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭࠯ࡹࡨࡦࡩࡸࡩࡷࡧࡵ࠲ࢀࢃ࠮ࡰࡲࡷ࡭ࡴࡴࡳࠨ୑").format(browser)
      name = bstack1lll11l_opy_ (u"ࠧࡐࡲࡷ࡭ࡴࡴࡳࠨ୒")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack11l11l111l_opy_(options):
        return None
      for bstack1l1l11111_opy_ in caps.keys():
        options.set_capability(bstack1l1l11111_opy_, caps[bstack1l1l11111_opy_])
      bstack11l1l11l11_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack11l1111l11_opy_(options, bstack1l1l1lll1l_opy_):
  if not bstack11l11l111l_opy_(options):
    return
  for bstack1l1l11111_opy_ in bstack1l1l1lll1l_opy_.keys():
    if bstack1l1l11111_opy_ in bstack1l1l1l1l1_opy_:
      continue
    if bstack1l1l11111_opy_ in options._caps and type(options._caps[bstack1l1l11111_opy_]) in [dict, list]:
      options._caps[bstack1l1l11111_opy_] = update(options._caps[bstack1l1l11111_opy_], bstack1l1l1lll1l_opy_[bstack1l1l11111_opy_])
    else:
      options.set_capability(bstack1l1l11111_opy_, bstack1l1l1lll1l_opy_[bstack1l1l11111_opy_])
  bstack11l1l11l11_opy_(options, bstack1l1l1lll1l_opy_)
  if bstack1lll11l_opy_ (u"ࠨ࡯ࡲࡾ࠿ࡪࡥࡣࡷࡪ࡫ࡪࡸࡁࡥࡦࡵࡩࡸࡹࠧ୓") in options._caps:
    if options._caps[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ୔")] and options._caps[bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨ୕")].lower() != bstack1lll11l_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬୖ"):
      del options._caps[bstack1lll11l_opy_ (u"ࠬࡳ࡯ࡻ࠼ࡧࡩࡧࡻࡧࡨࡧࡵࡅࡩࡪࡲࡦࡵࡶࠫୗ")]
def bstack11ll1l111_opy_(proxy_config):
  if bstack1lll11l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ୘") in proxy_config:
    proxy_config[bstack1lll11l_opy_ (u"ࠧࡴࡵ࡯ࡔࡷࡵࡸࡺࠩ୙")] = proxy_config[bstack1lll11l_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ୚")]
    del (proxy_config[bstack1lll11l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭୛")])
  if bstack1lll11l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭ଡ଼") in proxy_config and proxy_config[bstack1lll11l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡗࡽࡵ࡫ࠧଢ଼")].lower() != bstack1lll11l_opy_ (u"ࠬࡪࡩࡳࡧࡦࡸࠬ୞"):
    proxy_config[bstack1lll11l_opy_ (u"࠭ࡰࡳࡱࡻࡽ࡙ࡿࡰࡦࠩୟ")] = bstack1lll11l_opy_ (u"ࠧ࡮ࡣࡱࡹࡦࡲࠧୠ")
  if bstack1lll11l_opy_ (u"ࠨࡲࡵࡳࡽࡿࡁࡶࡶࡲࡧࡴࡴࡦࡪࡩࡘࡶࡱ࠭ୡ") in proxy_config:
    proxy_config[bstack1lll11l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬୢ")] = bstack1lll11l_opy_ (u"ࠪࡴࡦࡩࠧୣ")
  return proxy_config
def bstack1ll1l1lll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack1lll11l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ୤") in config:
    return proxy
  config[bstack1lll11l_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ୥")] = bstack11ll1l111_opy_(config[bstack1lll11l_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬ୦")])
  if proxy == None:
    proxy = Proxy(config[bstack1lll11l_opy_ (u"ࠧࡱࡴࡲࡼࡾ࠭୧")])
  return proxy
def bstack11l111l1l_opy_(self):
  global CONFIG
  global bstack1ll1llll1_opy_
  try:
    proxy = bstack1l11l11lll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack1lll11l_opy_ (u"ࠨ࠰ࡳࡥࡨ࠭୨")):
        proxies = bstack1llllllll1_opy_(proxy, bstack11l11lll1l_opy_())
        if len(proxies) > 0:
          protocol, bstack1111l11l1_opy_ = proxies.popitem()
          if bstack1lll11l_opy_ (u"ࠤ࠽࠳࠴ࠨ୩") in bstack1111l11l1_opy_:
            return bstack1111l11l1_opy_
          else:
            return bstack1lll11l_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦ୪") + bstack1111l11l1_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack1lll11l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡱࡴࡲࡼࡾࠦࡵࡳ࡮ࠣ࠾ࠥࢁࡽࠣ୫").format(str(e)))
  return bstack1ll1llll1_opy_(self)
def bstack1l111l11ll_opy_():
  global CONFIG
  return bstack11ll1111ll_opy_(CONFIG) and bstack111l1ll11_opy_() and bstack111l1l111l_opy_() >= version.parse(bstack111l1l111_opy_)
def bstack111llll11l_opy_():
  global CONFIG
  return (bstack1lll11l_opy_ (u"ࠬ࡮ࡴࡵࡲࡓࡶࡴࡾࡹࠨ୬") in CONFIG or bstack1lll11l_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪ୭") in CONFIG) and bstack1ll1l1ll1l_opy_()
def bstack11l1l1llll_opy_(config):
  bstack1llll11l11_opy_ = {}
  if bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫ୮") in config:
    bstack1llll11l11_opy_ = config[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬ୯")]
  if bstack1lll11l_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ୰") in config:
    bstack1llll11l11_opy_ = config[bstack1lll11l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩୱ")]
  proxy = bstack1l11l11lll_opy_(config)
  if proxy:
    if proxy.endswith(bstack1lll11l_opy_ (u"ࠫ࠳ࡶࡡࡤࠩ୲")) and os.path.isfile(proxy):
      bstack1llll11l11_opy_[bstack1lll11l_opy_ (u"ࠬ࠳ࡰࡢࡥ࠰ࡪ࡮ࡲࡥࠨ୳")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack1lll11l_opy_ (u"࠭࠮ࡱࡣࡦࠫ୴")):
        proxies = bstack1lll1lll11_opy_(config, bstack11l11lll1l_opy_())
        if len(proxies) > 0:
          protocol, bstack1111l11l1_opy_ = proxies.popitem()
          if bstack1lll11l_opy_ (u"ࠢ࠻࠱࠲ࠦ୵") in bstack1111l11l1_opy_:
            parsed_url = urlparse(bstack1111l11l1_opy_)
          else:
            parsed_url = urlparse(protocol + bstack1lll11l_opy_ (u"ࠣ࠼࠲࠳ࠧ୶") + bstack1111l11l1_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1llll11l11_opy_[bstack1lll11l_opy_ (u"ࠩࡳࡶࡴࡾࡹࡉࡱࡶࡸࠬ୷")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1llll11l11_opy_[bstack1lll11l_opy_ (u"ࠪࡴࡷࡵࡸࡺࡒࡲࡶࡹ࠭୸")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1llll11l11_opy_[bstack1lll11l_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡘࡷࡪࡸࠧ୹")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1llll11l11_opy_[bstack1lll11l_opy_ (u"ࠬࡶࡲࡰࡺࡼࡔࡦࡹࡳࠨ୺")] = str(parsed_url.password)
  return bstack1llll11l11_opy_
def bstack1l1ll1ll1_opy_(config):
  if bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫ୻") in config:
    return config[bstack1lll11l_opy_ (u"ࠧࡵࡧࡶࡸࡈࡵ࡮ࡵࡧࡻࡸࡔࡶࡴࡪࡱࡱࡷࠬ୼")]
  return {}
def bstack1ll1111l1_opy_(caps):
  global bstack1l1lll111_opy_
  if bstack1lll11l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ୽") in caps:
    caps[bstack1lll11l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ୾")][bstack1lll11l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩ୿")] = True
    if bstack1l1lll111_opy_:
      caps[bstack1lll11l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ஀")][bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ஁")] = bstack1l1lll111_opy_
  else:
    caps[bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫஂ")] = True
    if bstack1l1lll111_opy_:
      caps[bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨஃ")] = bstack1l1lll111_opy_
@measure(event_name=EVENTS.bstack1ll1l1lll1_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1l11lllll1_opy_():
  global CONFIG
  if not bstack11111lll1l_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ஄") in CONFIG and bstack111llll1l_opy_(CONFIG[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭அ")]):
    if (
      bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧஆ") in CONFIG
      and bstack111llll1l_opy_(CONFIG[bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨஇ")].get(bstack1lll11l_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩஈ")))
    ):
      logger.debug(bstack1lll11l_opy_ (u"ࠨࡌࡰࡥࡤࡰࠥࡨࡩ࡯ࡣࡵࡽࠥࡴ࡯ࡵࠢࡶࡸࡦࡸࡴࡦࡦࠣࡥࡸࠦࡳ࡬࡫ࡳࡆ࡮ࡴࡡࡳࡻࡌࡲ࡮ࡺࡩࡢ࡮࡬ࡷࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡥ࡯ࡣࡥࡰࡪࡪࠢஉ"))
      return
    bstack1llll11l11_opy_ = bstack11l1l1llll_opy_(CONFIG)
    bstack1111lll1ll_opy_(CONFIG[bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪஊ")], bstack1llll11l11_opy_)
def bstack1111lll1ll_opy_(key, bstack1llll11l11_opy_):
  global bstack111111ll1_opy_
  logger.info(bstack1l111lllll_opy_)
  try:
    bstack111111ll1_opy_ = Local()
    bstack1ll1ll1ll1_opy_ = {bstack1lll11l_opy_ (u"ࠨ࡭ࡨࡽࠬ஋"): key}
    bstack1ll1ll1ll1_opy_.update(bstack1llll11l11_opy_)
    logger.debug(bstack1ll11l1lll_opy_.format(str(bstack1ll1ll1ll1_opy_)).replace(key, bstack1lll11l_opy_ (u"ࠩ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭஌")))
    bstack111111ll1_opy_.start(**bstack1ll1ll1ll1_opy_)
    if bstack111111ll1_opy_.isRunning():
      logger.info(bstack11lllll1l1_opy_)
  except Exception as e:
    bstack11l1ll1l1l_opy_(bstack1111ll1l11_opy_.format(str(e)))
def bstack11l1llllll_opy_():
  global bstack111111ll1_opy_
  if bstack111111ll1_opy_.isRunning():
    logger.info(bstack111lllll1l_opy_)
    bstack111111ll1_opy_.stop()
  bstack111111ll1_opy_ = None
def bstack1l1l1l1ll_opy_(bstack1l11l111l1_opy_=[]):
  global CONFIG
  bstack11111l1ll_opy_ = []
  bstack1ll1l1llll_opy_ = [bstack1lll11l_opy_ (u"ࠪࡳࡸ࠭஍"), bstack1lll11l_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧஎ"), bstack1lll11l_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩஏ"), bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨஐ"), bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ஑"), bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩஒ")]
  try:
    for err in bstack1l11l111l1_opy_:
      bstack11llll11l_opy_ = {}
      for k in bstack1ll1l1llll_opy_:
        val = CONFIG[bstack1lll11l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬஓ")][int(err[bstack1lll11l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩஔ")])].get(k)
        if val:
          bstack11llll11l_opy_[k] = val
      if(err[bstack1lll11l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪக")] != bstack1lll11l_opy_ (u"ࠬ࠭஖")):
        bstack11llll11l_opy_[bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡷࠬ஗")] = {
          err[bstack1lll11l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ஘")]: err[bstack1lll11l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧங")]
        }
        bstack11111l1ll_opy_.append(bstack11llll11l_opy_)
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫ࡵࡲ࡮ࡣࡷࡸ࡮ࡴࡧࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡩࡻ࡫࡮ࡵ࠼ࠣࠫச") + str(e))
  finally:
    return bstack11111l1ll_opy_
def bstack11ll1lll1l_opy_(file_name):
  bstack1ll1ll11ll_opy_ = []
  try:
    bstack1l1l1llll1_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack1l1l1llll1_opy_):
      with open(bstack1l1l1llll1_opy_) as f:
        bstack1l11ll1ll1_opy_ = json.load(f)
        bstack1ll1ll11ll_opy_ = bstack1l11ll1ll1_opy_
      os.remove(bstack1l1l1llll1_opy_)
    return bstack1ll1ll11ll_opy_
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡬ࡩ࡯ࡦ࡬ࡲ࡬ࠦࡥࡳࡴࡲࡶࠥࡲࡩࡴࡶ࠽ࠤࠬ஛") + str(e))
    return bstack1ll1ll11ll_opy_
def bstack1ll11l11ll_opy_():
  try:
      from bstack_utils.constants import bstack1lll11ll11_opy_, EVENTS
      from bstack_utils.helper import bstack1l11l1111_opy_, get_host_info, bstack111ll1l1_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack11ll1ll11l_opy_ = os.path.join(os.getcwd(), bstack1lll11l_opy_ (u"ࠫࡱࡵࡧࠨஜ"), bstack1lll11l_opy_ (u"ࠬࡱࡥࡺ࠯ࡰࡩࡹࡸࡩࡤࡵ࠱࡮ࡸࡵ࡮ࠨ஝"))
      lock = FileLock(bstack11ll1ll11l_opy_+bstack1lll11l_opy_ (u"ࠨ࠮࡭ࡱࡦ࡯ࠧஞ"))
      def bstack1lll1l1l_opy_():
          try:
              with lock:
                  with open(bstack11ll1ll11l_opy_, bstack1lll11l_opy_ (u"ࠢࡳࠤட"), encoding=bstack1lll11l_opy_ (u"ࠣࡷࡷࡪ࠲࠾ࠢ஠")) as file:
                      data = json.load(file)
                      config = {
                          bstack1lll11l_opy_ (u"ࠤ࡫ࡩࡦࡪࡥࡳࡵࠥ஡"): {
                              bstack1lll11l_opy_ (u"ࠥࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠤ஢"): bstack1lll11l_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠢண"),
                          }
                      }
                      bstack111l111l1_opy_ = datetime.utcnow()
                      bstack1l111lll_opy_ = bstack111l111l1_opy_.strftime(bstack1lll11l_opy_ (u"࡙ࠧࠫ࠮ࠧࡰ࠱ࠪࡪࡔࠦࡊ࠽ࠩࡒࡀࠥࡔ࠰ࠨࡪ࡛ࠥࡔࡄࠤத"))
                      test_id = os.environ.get(bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ஥")) if os.environ.get(bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ஦")) else bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠣࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠥ஧"))
                      payload = {
                          bstack1lll11l_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪࠨந"): bstack1lll11l_opy_ (u"ࠥࡷࡩࡱ࡟ࡦࡸࡨࡲࡹࡹࠢன"),
                          bstack1lll11l_opy_ (u"ࠦࡩࡧࡴࡢࠤப"): {
                              bstack1lll11l_opy_ (u"ࠧࡺࡥࡴࡶ࡫ࡹࡧࡥࡵࡶ࡫ࡧࠦ஫"): test_id,
                              bstack1lll11l_opy_ (u"ࠨࡣࡳࡧࡤࡸࡪࡪ࡟ࡥࡣࡼࠦ஬"): bstack1l111lll_opy_,
                              bstack1lll11l_opy_ (u"ࠢࡦࡸࡨࡲࡹࡥ࡮ࡢ࡯ࡨࠦ஭"): bstack1lll11l_opy_ (u"ࠣࡕࡇࡏࡋ࡫ࡡࡵࡷࡵࡩࡕ࡫ࡲࡧࡱࡵࡱࡦࡴࡣࡦࠤம"),
                              bstack1lll11l_opy_ (u"ࠤࡨࡺࡪࡴࡴࡠ࡬ࡶࡳࡳࠨய"): {
                                  bstack1lll11l_opy_ (u"ࠥࡱࡪࡧࡳࡶࡴࡨࡷࠧர"): data,
                                  bstack1lll11l_opy_ (u"ࠦࡸࡪ࡫ࡓࡷࡱࡍࡩࠨற"): bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢல"))
                              },
                              bstack1lll11l_opy_ (u"ࠨࡵࡴࡧࡵࡣࡩࡧࡴࡢࠤள"): bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠢࡶࡵࡨࡶࡓࡧ࡭ࡦࠤழ")),
                              bstack1lll11l_opy_ (u"ࠣࡪࡲࡷࡹࡥࡩ࡯ࡨࡲࠦவ"): get_host_info()
                          }
                      }
                      bstack11l1l11111_opy_ = bstack11llll111_opy_(cli.config, [bstack1lll11l_opy_ (u"ࠤࡤࡴ࡮ࡹࠢஶ"), bstack1lll11l_opy_ (u"ࠥࡩࡩࡹࡉ࡯ࡵࡷࡶࡺࡳࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠣஷ"), bstack1lll11l_opy_ (u"ࠦࡦࡶࡩࠣஸ")], bstack1lll11ll11_opy_)
                      response = bstack1l11l1111_opy_(bstack1lll11l_opy_ (u"ࠧࡖࡏࡔࡖࠥஹ"), bstack11l1l11111_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack1lll11l_opy_ (u"ࠨࡄࡢࡶࡤࠤࡸ࡫࡮ࡵࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࡲࡹࠡࡶࡲࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡪࡡࡵࡣࠣࡿࢂࠨ஺").format(bstack1lll11ll11_opy_, payload))
                      else:
                          logger.debug(bstack1lll11l_opy_ (u"ࠢࡓࡧࡴࡹࡪࡹࡴࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡨࡲࡶࠥࢁࡽࠡࡹ࡬ࡸ࡭ࠦࡤࡢࡶࡤࠤࢀࢃࠢ஻").format(bstack1lll11ll11_opy_, payload))
          except Exception as e:
              logger.debug(bstack1lll11l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫࡮ࡥࠢ࡮ࡩࡾࠦ࡭ࡦࡶࡵ࡭ࡨࡹࠠࡥࡣࡷࡥࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢࡾࢁࠧ஼").format(e))
      bstack1lll1l1l_opy_()
      bstack11l1l1ll11_opy_(bstack11ll1ll11l_opy_, logger)
  except:
    pass
def bstack11l1lll1l_opy_():
  global bstack1ll11l1111_opy_
  global bstack1l1lll1ll_opy_
  global bstack11l1ll1l1_opy_
  global bstack11l1l111l_opy_
  global bstack111ll1l1ll_opy_
  global bstack1l11111ll_opy_
  global CONFIG
  bstack1l11l1lll1_opy_ = os.environ.get(bstack1lll11l_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪ஽"))
  if bstack1l11l1lll1_opy_ in [bstack1lll11l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩா"), bstack1lll11l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪி")]:
    bstack11llll1111_opy_()
  percy.shutdown()
  if bstack1ll11l1111_opy_:
    logger.warning(bstack111l11ll1_opy_.format(str(bstack1ll11l1111_opy_)))
  else:
    try:
      bstack111l1ll111_opy_ = bstack11l111llll_opy_(bstack1lll11l_opy_ (u"ࠬ࠴ࡢࡴࡶࡤࡧࡰ࠳ࡣࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠫீ"), logger)
      if bstack111l1ll111_opy_.get(bstack1lll11l_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫு")) and bstack111l1ll111_opy_.get(bstack1lll11l_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬூ")).get(bstack1lll11l_opy_ (u"ࠨࡪࡲࡷࡹࡴࡡ࡮ࡧࠪ௃")):
        logger.warning(bstack111l11ll1_opy_.format(str(bstack111l1ll111_opy_[bstack1lll11l_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ௄")][bstack1lll11l_opy_ (u"ࠪ࡬ࡴࡹࡴ࡯ࡣࡰࡩࠬ௅")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack11l1l1l1l_opy_.invoke(Events.bstack1l11l11l1l_opy_)
  logger.info(bstack1l1l1l11l1_opy_)
  global bstack111111ll1_opy_
  if bstack111111ll1_opy_:
    bstack11l1llllll_opy_()
  try:
    with bstack1ll111l111_opy_:
      bstack111111l1l_opy_ = bstack1l1lll1ll_opy_.copy()
    for driver in bstack111111l1l_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack1111l1ll1_opy_)
  if bstack1l11111ll_opy_ == bstack1lll11l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪெ"):
    bstack111ll1l1ll_opy_ = bstack11ll1lll1l_opy_(bstack1lll11l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭ே"))
  if bstack1l11111ll_opy_ == bstack1lll11l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ை") and len(bstack11l1l111l_opy_) == 0:
    bstack11l1l111l_opy_ = bstack11ll1lll1l_opy_(bstack1lll11l_opy_ (u"ࠧࡱࡹࡢࡴࡾࡺࡥࡴࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ௉"))
    if len(bstack11l1l111l_opy_) == 0:
      bstack11l1l111l_opy_ = bstack11ll1lll1l_opy_(bstack1lll11l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡲࡳࡴࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵ࠰࡭ࡷࡴࡴࠧொ"))
  bstack1ll111l1ll_opy_ = bstack1lll11l_opy_ (u"ࠩࠪோ")
  if len(bstack11l1ll1l1_opy_) > 0:
    bstack1ll111l1ll_opy_ = bstack1l1l1l1ll_opy_(bstack11l1ll1l1_opy_)
  elif len(bstack11l1l111l_opy_) > 0:
    bstack1ll111l1ll_opy_ = bstack1l1l1l1ll_opy_(bstack11l1l111l_opy_)
  elif len(bstack111ll1l1ll_opy_) > 0:
    bstack1ll111l1ll_opy_ = bstack1l1l1l1ll_opy_(bstack111ll1l1ll_opy_)
  elif len(bstack1l1l1l1ll1_opy_) > 0:
    bstack1ll111l1ll_opy_ = bstack1l1l1l1ll_opy_(bstack1l1l1l1ll1_opy_)
  if bool(bstack1ll111l1ll_opy_):
    bstack1l111l11l1_opy_(bstack1ll111l1ll_opy_)
  else:
    bstack1l111l11l1_opy_()
  bstack11l1l1ll11_opy_(bstack1111ll1l1_opy_, logger)
  if bstack1l11l1lll1_opy_ not in [bstack1lll11l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫௌ")]:
    bstack1ll11l11ll_opy_()
  bstack11ll1111l_opy_.bstack1l11llll_opy_(CONFIG)
  if len(bstack111ll1l1ll_opy_) > 0:
    sys.exit(len(bstack111ll1l1ll_opy_))
def bstack1llllll1l1_opy_(bstack111ll1l1l_opy_, frame):
  global bstack111ll1l1_opy_
  logger.error(bstack1l111llll1_opy_)
  bstack111ll1l1_opy_.set_property(bstack1lll11l_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡓࡵ்ࠧ"), bstack111ll1l1l_opy_)
  if hasattr(signal, bstack1lll11l_opy_ (u"࡙ࠬࡩࡨࡰࡤࡰࡸ࠭௎")):
    bstack111ll1l1_opy_.set_property(bstack1lll11l_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭௏"), signal.Signals(bstack111ll1l1l_opy_).name)
  else:
    bstack111ll1l1_opy_.set_property(bstack1lll11l_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧௐ"), bstack1lll11l_opy_ (u"ࠨࡕࡌࡋ࡚ࡔࡋࡏࡑ࡚ࡒࠬ௑"))
  if cli.is_running():
    bstack11l1l1l1l_opy_.invoke(Events.bstack1l11l11l1l_opy_)
  bstack1l11l1lll1_opy_ = os.environ.get(bstack1lll11l_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪ௒"))
  if bstack1l11l1lll1_opy_ == bstack1lll11l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ௓") and not cli.is_enabled(CONFIG):
    bstack1l111l1l_opy_.stop(bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠫࡸࡪ࡫ࡌ࡫࡯ࡰࡘ࡯ࡧ࡯ࡣ࡯ࠫ௔")))
  bstack11l1lll1l_opy_()
  sys.exit(1)
def bstack11l1ll1l1l_opy_(err):
  logger.critical(bstack11l11l1ll_opy_.format(str(err)))
  bstack1l111l11l1_opy_(bstack11l11l1ll_opy_.format(str(err)), True)
  atexit.unregister(bstack11l1lll1l_opy_)
  bstack11llll1111_opy_()
  sys.exit(1)
def bstack1l111ll1l_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l111l11l1_opy_(message, True)
  atexit.unregister(bstack11l1lll1l_opy_)
  bstack11llll1111_opy_()
  sys.exit(1)
def bstack1l1ll111ll_opy_():
  global CONFIG
  global bstack1l1111ll11_opy_
  global bstack1l1l11111l_opy_
  global bstack111ll1llll_opy_
  CONFIG = bstack111llllll1_opy_()
  load_dotenv(CONFIG.get(bstack1lll11l_opy_ (u"ࠬ࡫࡮ࡷࡈ࡬ࡰࡪ࠭௕")))
  bstack11ll11llll_opy_()
  bstack1ll11l1l1_opy_()
  CONFIG = bstack1111ll1ll_opy_(CONFIG)
  update(CONFIG, bstack1l1l11111l_opy_)
  update(CONFIG, bstack1l1111ll11_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack11l11l111_opy_(CONFIG)
  bstack111ll1llll_opy_ = bstack11111lll1l_opy_(CONFIG)
  os.environ[bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩ௖")] = bstack111ll1llll_opy_.__str__().lower()
  bstack111ll1l1_opy_.set_property(bstack1lll11l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨௗ"), bstack111ll1llll_opy_)
  if (bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௘") in CONFIG and bstack1lll11l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௙") in bstack1l1111ll11_opy_) or (
          bstack1lll11l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௚") in CONFIG and bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௛") not in bstack1l1l11111l_opy_):
    if os.getenv(bstack1lll11l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡤࡉࡏࡎࡄࡌࡒࡊࡊ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩ௜")):
      CONFIG[bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ௝")] = os.getenv(bstack1lll11l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ௞"))
    else:
      if not CONFIG.get(bstack1lll11l_opy_ (u"ࠣࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠦ௟"), bstack1lll11l_opy_ (u"ࠤࠥ௠")) in bstack1ll1llll11_opy_:
        bstack11l11ll11l_opy_()
  elif (bstack1lll11l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௡") not in CONFIG and bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭௢") in CONFIG) or (
          bstack1lll11l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௣") in bstack1l1l11111l_opy_ and bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ௤") not in bstack1l1111ll11_opy_):
    del (CONFIG[bstack1lll11l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ௥")])
  if bstack1lll111l11_opy_(CONFIG):
    bstack11l1ll1l1l_opy_(bstack11l1l1111l_opy_)
  Config.bstack111l1111_opy_().set_property(bstack1lll11l_opy_ (u"ࠣࡷࡶࡩࡷࡔࡡ࡮ࡧࠥ௦"), CONFIG[bstack1lll11l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ௧")])
  bstack11111l111_opy_()
  bstack1ll1l1111_opy_()
  if bstack11llllll1_opy_ and not CONFIG.get(bstack1lll11l_opy_ (u"ࠥࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࠨ௨"), bstack1lll11l_opy_ (u"ࠦࠧ௩")) in bstack1ll1llll11_opy_:
    CONFIG[bstack1lll11l_opy_ (u"ࠬࡧࡰࡱࠩ௪")] = bstack1lll1l1l11_opy_(CONFIG)
    logger.info(bstack11ll1l1111_opy_.format(CONFIG[bstack1lll11l_opy_ (u"࠭ࡡࡱࡲࠪ௫")]))
  if not bstack111ll1llll_opy_:
    CONFIG[bstack1lll11l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ௬")] = [{}]
def bstack11lllllll_opy_(config, bstack1l1ll1lll_opy_):
  global CONFIG
  global bstack11llllll1_opy_
  CONFIG = config
  bstack11llllll1_opy_ = bstack1l1ll1lll_opy_
def bstack1ll1l1111_opy_():
  global CONFIG
  global bstack11llllll1_opy_
  if bstack1lll11l_opy_ (u"ࠨࡣࡳࡴࠬ௭") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1l111ll1l_opy_(e, bstack1l1lllll1l_opy_)
    bstack11llllll1_opy_ = True
    bstack111ll1l1_opy_.set_property(bstack1lll11l_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ௮"), True)
def bstack1lll1l1l11_opy_(config):
  bstack11l111ll1_opy_ = bstack1lll11l_opy_ (u"ࠪࠫ௯")
  app = config[bstack1lll11l_opy_ (u"ࠫࡦࡶࡰࠨ௰")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1l1l1l1l1l_opy_:
      if os.path.exists(app):
        bstack11l111ll1_opy_ = bstack1l1111llll_opy_(config, app)
      elif bstack11l11lllll_opy_(app):
        bstack11l111ll1_opy_ = app
      else:
        bstack11l1ll1l1l_opy_(bstack1ll1l111l_opy_.format(app))
    else:
      if bstack11l11lllll_opy_(app):
        bstack11l111ll1_opy_ = app
      elif os.path.exists(app):
        bstack11l111ll1_opy_ = bstack1l1111llll_opy_(app)
      else:
        bstack11l1ll1l1l_opy_(bstack111lll1lll_opy_)
  else:
    if len(app) > 2:
      bstack11l1ll1l1l_opy_(bstack1l1llll111_opy_)
    elif len(app) == 2:
      if bstack1lll11l_opy_ (u"ࠬࡶࡡࡵࡪࠪ௱") in app and bstack1lll11l_opy_ (u"࠭ࡣࡶࡵࡷࡳࡲࡥࡩࡥࠩ௲") in app:
        if os.path.exists(app[bstack1lll11l_opy_ (u"ࠧࡱࡣࡷ࡬ࠬ௳")]):
          bstack11l111ll1_opy_ = bstack1l1111llll_opy_(config, app[bstack1lll11l_opy_ (u"ࠨࡲࡤࡸ࡭࠭௴")], app[bstack1lll11l_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡡ࡬ࡨࠬ௵")])
        else:
          bstack11l1ll1l1l_opy_(bstack1ll1l111l_opy_.format(app))
      else:
        bstack11l1ll1l1l_opy_(bstack1l1llll111_opy_)
    else:
      for key in app:
        if key in bstack1111l1lll_opy_:
          if key == bstack1lll11l_opy_ (u"ࠪࡴࡦࡺࡨࠨ௶"):
            if os.path.exists(app[key]):
              bstack11l111ll1_opy_ = bstack1l1111llll_opy_(config, app[key])
            else:
              bstack11l1ll1l1l_opy_(bstack1ll1l111l_opy_.format(app))
          else:
            bstack11l111ll1_opy_ = app[key]
        else:
          bstack11l1ll1l1l_opy_(bstack1ll1lll11l_opy_)
  return bstack11l111ll1_opy_
def bstack11l11lllll_opy_(bstack11l111ll1_opy_):
  import re
  bstack11lll11l1_opy_ = re.compile(bstack1lll11l_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬࠧࠦ௷"))
  bstack1l1lllll11_opy_ = re.compile(bstack1lll11l_opy_ (u"ࡷࠨ࡞࡜ࡣ࠰ࡾࡆ࠳࡚࠱࠯࠼ࡠࡤ࠴࡜࠮࡟࠭࠳ࡠࡧ࠭ࡻࡃ࠰࡞࠵࠳࠹࡝ࡡ࠱ࡠ࠲ࡣࠪࠥࠤ௸"))
  if bstack1lll11l_opy_ (u"࠭ࡢࡴ࠼࠲࠳ࠬ௹") in bstack11l111ll1_opy_ or re.fullmatch(bstack11lll11l1_opy_, bstack11l111ll1_opy_) or re.fullmatch(bstack1l1lllll11_opy_, bstack11l111ll1_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack1lll11ll1l_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1l1111llll_opy_(config, path, bstack111ll1ll1l_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack1lll11l_opy_ (u"ࠧࡳࡤࠪ௺")).read()).hexdigest()
  bstack111ll1lll_opy_ = bstack1l1llll11_opy_(md5_hash)
  bstack11l111ll1_opy_ = None
  if bstack111ll1lll_opy_:
    logger.info(bstack11lll1l1ll_opy_.format(bstack111ll1lll_opy_, md5_hash))
    return bstack111ll1lll_opy_
  bstack11ll11l1l_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack1lll11l_opy_ (u"ࠨࡨ࡬ࡰࡪ࠭௻"): (os.path.basename(path), open(os.path.abspath(path), bstack1lll11l_opy_ (u"ࠩࡵࡦࠬ௼")), bstack1lll11l_opy_ (u"ࠪࡸࡪࡾࡴ࠰ࡲ࡯ࡥ࡮ࡴࠧ௽")),
      bstack1lll11l_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡣ࡮ࡪࠧ௾"): bstack111ll1ll1l_opy_
    }
  )
  response = requests.post(bstack1l11llll11_opy_, data=multipart_data,
                           headers={bstack1lll11l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ௿"): multipart_data.content_type},
                           auth=(config[bstack1lll11l_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨఀ")], config[bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪఁ")]))
  try:
    res = json.loads(response.text)
    bstack11l111ll1_opy_ = res[bstack1lll11l_opy_ (u"ࠨࡣࡳࡴࡤࡻࡲ࡭ࠩం")]
    logger.info(bstack1l11l11l11_opy_.format(bstack11l111ll1_opy_))
    bstack1l1111l111_opy_(md5_hash, bstack11l111ll1_opy_)
    cli.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺ࡶࡲ࡯ࡳࡦࡪ࡟ࡢࡲࡳࠦః"), datetime.datetime.now() - bstack11ll11l1l_opy_)
  except ValueError as err:
    bstack11l1ll1l1l_opy_(bstack1llll1ll1l_opy_.format(str(err)))
  return bstack11l111ll1_opy_
def bstack11111l111_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1llll1lll1_opy_
  bstack1lll111l1_opy_ = 1
  bstack1ll11ll11l_opy_ = 1
  if bstack1lll11l_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪఄ") in CONFIG:
    bstack1ll11ll11l_opy_ = CONFIG[bstack1lll11l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫఅ")]
  else:
    bstack1ll11ll11l_opy_ = bstack1ll1l1ll1_opy_(framework_name, args) or 1
  if bstack1lll11l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఆ") in CONFIG:
    bstack1lll111l1_opy_ = len(CONFIG[bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩఇ")])
  bstack1llll1lll1_opy_ = int(bstack1ll11ll11l_opy_) * int(bstack1lll111l1_opy_)
def bstack1ll1l1ll1_opy_(framework_name, args):
  if framework_name == bstack111l11l1l_opy_ and args and bstack1lll11l_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬఈ") in args:
      bstack11ll11l11_opy_ = args.index(bstack1lll11l_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ఉ"))
      return int(args[bstack11ll11l11_opy_ + 1]) or 1
  return 1
def bstack1l1llll11_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lll11l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡬ࡰࡥ࡮ࠤࡳࡵࡴࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡻࡳࡪࡰࡪࠤࡧࡧࡳࡪࡥࠣࡪ࡮ࡲࡥࠡࡱࡳࡩࡷࡧࡴࡪࡱࡱࡷࠬఊ"))
    bstack11ll111ll1_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠪࢂࠬఋ")), bstack1lll11l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఌ"), bstack1lll11l_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭఍"))
    if os.path.exists(bstack11ll111ll1_opy_):
      try:
        bstack1lll111111_opy_ = json.load(open(bstack11ll111ll1_opy_, bstack1lll11l_opy_ (u"࠭ࡲࡣࠩఎ")))
        if md5_hash in bstack1lll111111_opy_:
          bstack1l1l1l11l_opy_ = bstack1lll111111_opy_[md5_hash]
          bstack1l11lll111_opy_ = datetime.datetime.now()
          bstack1111llll11_opy_ = datetime.datetime.strptime(bstack1l1l1l11l_opy_[bstack1lll11l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪఏ")], bstack1lll11l_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬఐ"))
          if (bstack1l11lll111_opy_ - bstack1111llll11_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack1l1l1l11l_opy_[bstack1lll11l_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ఑")]):
            return None
          return bstack1l1l1l11l_opy_[bstack1lll11l_opy_ (u"ࠪ࡭ࡩ࠭ఒ")]
      except Exception as e:
        logger.debug(bstack1lll11l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡶࡪࡧࡤࡪࡰࡪࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࠦࡦࡪ࡮ࡨ࠾ࠥࢁࡽࠨఓ").format(str(e)))
    return None
  bstack11ll111ll1_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠬࢄࠧఔ")), bstack1lll11l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭క"), bstack1lll11l_opy_ (u"ࠧࡢࡲࡳ࡙ࡵࡲ࡯ࡢࡦࡐࡈ࠺ࡎࡡࡴࡪ࠱࡮ࡸࡵ࡮ࠨఖ"))
  lock_file = bstack11ll111ll1_opy_ + bstack1lll11l_opy_ (u"ࠨ࠰࡯ࡳࡨࡱࠧగ")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack11ll111ll1_opy_):
        with open(bstack11ll111ll1_opy_, bstack1lll11l_opy_ (u"ࠩࡵࠫఘ")) as f:
          content = f.read().strip()
          if content:
            bstack1lll111111_opy_ = json.loads(content)
            if md5_hash in bstack1lll111111_opy_:
              bstack1l1l1l11l_opy_ = bstack1lll111111_opy_[md5_hash]
              bstack1l11lll111_opy_ = datetime.datetime.now()
              bstack1111llll11_opy_ = datetime.datetime.strptime(bstack1l1l1l11l_opy_[bstack1lll11l_opy_ (u"ࠪࡸ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭ఙ")], bstack1lll11l_opy_ (u"ࠫࠪࡪ࠯ࠦ࡯࠲ࠩ࡞ࠦࠥࡉ࠼ࠨࡑ࠿ࠫࡓࠨచ"))
              if (bstack1l11lll111_opy_ - bstack1111llll11_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack1l1l1l11l_opy_[bstack1lll11l_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪఛ")]):
                return None
              return bstack1l1l1l11l_opy_[bstack1lll11l_opy_ (u"࠭ࡩࡥࠩజ")]
      return None
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡷࡪࡶ࡫ࠤ࡫࡯࡬ࡦࠢ࡯ࡳࡨࡱࡩ࡯ࡩࠣࡪࡴࡸࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩ࠼ࠣࡿࢂ࠭ఝ").format(str(e)))
    return None
def bstack1l1111l111_opy_(md5_hash, bstack11l111ll1_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lll11l_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫఞ"))
    bstack111lll1ll1_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠩࢁࠫట")), bstack1lll11l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪఠ"))
    if not os.path.exists(bstack111lll1ll1_opy_):
      os.makedirs(bstack111lll1ll1_opy_)
    bstack11ll111ll1_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠫࢃ࠭డ")), bstack1lll11l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬఢ"), bstack1lll11l_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧణ"))
    bstack1ll1ll11l_opy_ = {
      bstack1lll11l_opy_ (u"ࠧࡪࡦࠪత"): bstack11l111ll1_opy_,
      bstack1lll11l_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫథ"): datetime.datetime.strftime(datetime.datetime.now(), bstack1lll11l_opy_ (u"ࠩࠨࡨ࠴ࠫ࡭࠰ࠧ࡜ࠤࠪࡎ࠺ࠦࡏ࠽ࠩࡘ࠭ద")),
      bstack1lll11l_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨధ"): str(__version__)
    }
    try:
      bstack1lll111111_opy_ = {}
      if os.path.exists(bstack11ll111ll1_opy_):
        bstack1lll111111_opy_ = json.load(open(bstack11ll111ll1_opy_, bstack1lll11l_opy_ (u"ࠫࡷࡨࠧన")))
      bstack1lll111111_opy_[md5_hash] = bstack1ll1ll11l_opy_
      with open(bstack11ll111ll1_opy_, bstack1lll11l_opy_ (u"ࠧࡽࠫࠣ఩")) as outfile:
        json.dump(bstack1lll111111_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1lll11l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡻࡰࡥࡣࡷ࡭ࡳ࡭ࠠࡎࡆ࠸ࠤ࡭ࡧࡳࡩࠢࡩ࡭ࡱ࡫࠺ࠡࡽࢀࠫప").format(str(e)))
    return
  bstack111lll1ll1_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠧࡿࠩఫ")), bstack1lll11l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨబ"))
  if not os.path.exists(bstack111lll1ll1_opy_):
    os.makedirs(bstack111lll1ll1_opy_)
  bstack11ll111ll1_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠩࢁࠫభ")), bstack1lll11l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪమ"), bstack1lll11l_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬయ"))
  lock_file = bstack11ll111ll1_opy_ + bstack1lll11l_opy_ (u"ࠬ࠴࡬ࡰࡥ࡮ࠫర")
  bstack1ll1ll11l_opy_ = {
    bstack1lll11l_opy_ (u"࠭ࡩࡥࠩఱ"): bstack11l111ll1_opy_,
    bstack1lll11l_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪల"): datetime.datetime.strftime(datetime.datetime.now(), bstack1lll11l_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬళ")),
    bstack1lll11l_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧఴ"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack1lll111111_opy_ = {}
      if os.path.exists(bstack11ll111ll1_opy_):
        with open(bstack11ll111ll1_opy_, bstack1lll11l_opy_ (u"ࠪࡶࠬవ")) as f:
          content = f.read().strip()
          if content:
            bstack1lll111111_opy_ = json.loads(content)
      bstack1lll111111_opy_[md5_hash] = bstack1ll1ll11l_opy_
      with open(bstack11ll111ll1_opy_, bstack1lll11l_opy_ (u"ࠦࡼࠨశ")) as outfile:
        json.dump(bstack1lll111111_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡼ࡯ࡴࡩࠢࡩ࡭ࡱ࡫ࠠ࡭ࡱࡦ࡯࡮ࡴࡧࠡࡨࡲࡶࠥࡓࡄ࠶ࠢ࡫ࡥࡸ࡮ࠠࡶࡲࡧࡥࡹ࡫࠺ࠡࡽࢀࠫష").format(str(e)))
def bstack1l1l1llll_opy_(self):
  return
def bstack11111l1l11_opy_(self):
  return
def bstack11lll111l_opy_():
  global bstack1l1ll11l1l_opy_
  bstack1l1ll11l1l_opy_ = True
@measure(event_name=EVENTS.bstack11ll111ll_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1111l111l1_opy_(self):
  global bstack1l11l11ll_opy_
  global bstack1l11l1l1ll_opy_
  global bstack11l1111ll1_opy_
  try:
    if bstack1lll11l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭స") in bstack1l11l11ll_opy_ and self.session_id != None and bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠧࡵࡧࡶࡸࡘࡺࡡࡵࡷࡶࠫహ"), bstack1lll11l_opy_ (u"ࠨࠩ఺")) != bstack1lll11l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ఻"):
      bstack1lll11l1ll_opy_ = bstack1lll11l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦ఼ࠪ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack1lll11l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫఽ")
      if bstack1lll11l1ll_opy_ == bstack1lll11l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬా"):
        bstack1111l1l11_opy_(logger)
      if self != None:
        bstack1l1ll1l11l_opy_(self, bstack1lll11l1ll_opy_, bstack1lll11l_opy_ (u"࠭ࠬࠡࠩి").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack1lll11l_opy_ (u"ࠧࠨీ")
    if bstack1lll11l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨు") in bstack1l11l11ll_opy_ and getattr(threading.current_thread(), bstack1lll11l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨూ"), None):
      bstack1111l111_opy_.bstack1lll1l111_opy_(self, bstack111l11l11l_opy_, logger, wait=True)
    if bstack1lll11l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪృ") in bstack1l11l11ll_opy_:
      if not threading.currentThread().behave_test_status:
        bstack1l1ll1l11l_opy_(self, bstack1lll11l_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦౄ"))
      bstack11111lllll_opy_.bstack11ll1ll1l1_opy_(self)
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡸࡺࡡࡵࡷࡶ࠾ࠥࠨ౅") + str(e))
  bstack11l1111ll1_opy_(self)
  self.session_id = None
def bstack1l1ll1l1l1_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack11111llll1_opy_
    global bstack1l11l11ll_opy_
    command_executor = kwargs.get(bstack1lll11l_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳࠩె"), bstack1lll11l_opy_ (u"ࠧࠨే"))
    bstack11l1l11l1l_opy_ = False
    if type(command_executor) == str and bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫై") in command_executor:
      bstack11l1l11l1l_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ౉") in str(getattr(command_executor, bstack1lll11l_opy_ (u"ࠪࡣࡺࡸ࡬ࠨొ"), bstack1lll11l_opy_ (u"ࠫࠬో"))):
      bstack11l1l11l1l_opy_ = True
    else:
      kwargs = bstack111ll1ll_opy_.bstack11l1ll11l_opy_(bstack11l1l11ll1_opy_=kwargs, config=CONFIG)
      return bstack1l11l1lll_opy_(self, *args, **kwargs)
    if bstack11l1l11l1l_opy_:
      bstack11llll1l1_opy_ = bstack11lll11lll_opy_.bstack1ll1ll111_opy_(CONFIG, bstack1l11l11ll_opy_)
      if kwargs.get(bstack1lll11l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ౌ")):
        kwargs[bstack1lll11l_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹ్ࠧ")] = bstack11111llll1_opy_(kwargs[bstack1lll11l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ౎")], bstack1l11l11ll_opy_, CONFIG, bstack11llll1l1_opy_)
      elif kwargs.get(bstack1lll11l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ౏")):
        kwargs[bstack1lll11l_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ౐")] = bstack11111llll1_opy_(kwargs[bstack1lll11l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ౑")], bstack1l11l11ll_opy_, CONFIG, bstack11llll1l1_opy_)
  except Exception as e:
    logger.error(bstack1lll11l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡫࡮ࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫࡙ࠥࡄࡌࠢࡦࡥࡵࡹ࠺ࠡࡽࢀࠦ౒").format(str(e)))
  return bstack1l11l1lll_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1ll11lllll_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1lll1lll1l_opy_(self, command_executor=bstack1lll11l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴࠷࠲࠸࠰࠳࠲࠵࠴࠱࠻࠶࠷࠸࠹ࠨ౓"), *args, **kwargs):
  global bstack1l11l1l1ll_opy_
  global bstack1l1lll1ll_opy_
  bstack1l1l111l1_opy_ = bstack1l1ll1l1l1_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1l11111l_opy_.on():
    return bstack1l1l111l1_opy_
  try:
    logger.debug(bstack1lll11l_opy_ (u"࠭ࡃࡰ࡯ࡰࡥࡳࡪࠠࡆࡺࡨࡧࡺࡺ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣ࡭ࡸࠦࡦࡢ࡮ࡶࡩࠥ࠳ࠠࡼࡿࠪ౔").format(str(command_executor)))
    logger.debug(bstack1lll11l_opy_ (u"ࠧࡉࡷࡥࠤ࡚ࡘࡌࠡ࡫ࡶࠤ࠲ࠦࡻࡾౕࠩ").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰౖࠫ") in command_executor._url:
      bstack111ll1l1_opy_.set_property(bstack1lll11l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪ౗"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ౘ") in command_executor):
    bstack111ll1l1_opy_.set_property(bstack1lll11l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬౙ"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack1111ll1l1l_opy_ = getattr(threading.current_thread(), bstack1lll11l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࡙࡫ࡳࡵࡏࡨࡸࡦ࠭ౚ"), None)
  bstack11l111lll1_opy_ = {}
  if self.capabilities is not None:
    bstack11l111lll1_opy_[bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬ౛")] = self.capabilities.get(bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ౜"))
    bstack11l111lll1_opy_[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪౝ")] = self.capabilities.get(bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ౞"))
    bstack11l111lll1_opy_[bstack1lll11l_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡢࡳࡵࡺࡩࡰࡰࡶࠫ౟")] = self.capabilities.get(bstack1lll11l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩౠ"))
  if CONFIG.get(bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬౡ"), False) and bstack111ll1ll_opy_.bstack1llll1l1l1_opy_(bstack11l111lll1_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack1lll11l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭ౢ") in bstack1l11l11ll_opy_ or bstack1lll11l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ౣ") in bstack1l11l11ll_opy_:
    bstack1l111l1l_opy_.bstack1ll11l1ll1_opy_(self)
  if bstack1lll11l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ౤") in bstack1l11l11ll_opy_ and bstack1111ll1l1l_opy_ and bstack1111ll1l1l_opy_.get(bstack1lll11l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ౥"), bstack1lll11l_opy_ (u"ࠪࠫ౦")) == bstack1lll11l_opy_ (u"ࠫࡵ࡫࡮ࡥ࡫ࡱ࡫ࠬ౧"):
    bstack1l111l1l_opy_.bstack1ll11l1ll1_opy_(self)
  bstack1l11l1l1ll_opy_ = self.session_id
  with bstack1ll111l111_opy_:
    bstack1l1lll1ll_opy_.append(self)
  return bstack1l1l111l1_opy_
def bstack11l1ll1111_opy_(args):
  return bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷ࠭౨") in str(args)
def bstack11111l111l_opy_(self, driver_command, *args, **kwargs):
  global bstack1llll11l1l_opy_
  global bstack1lll11l11l_opy_
  bstack111l11ll11_opy_ = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"࠭ࡩࡴࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ౩"), None) and bstack1ll111ll_opy_(
          threading.current_thread(), bstack1lll11l_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭౪"), None)
  bstack11l11l1l1_opy_ = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ౫"), None) and bstack1ll111ll_opy_(
          threading.current_thread(), bstack1lll11l_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ౬"), None)
  bstack1l1ll11l11_opy_ = getattr(self, bstack1lll11l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪ౭"), None) != None and getattr(self, bstack1lll11l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ౮"), None) == True
  if not bstack1lll11l11l_opy_ and bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ౯") in CONFIG and CONFIG[bstack1lll11l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭౰")] == True and bstack11111ll1l_opy_.bstack1ll111ll1l_opy_(driver_command) and (bstack1l1ll11l11_opy_ or bstack111l11ll11_opy_ or bstack11l11l1l1_opy_) and not bstack11l1ll1111_opy_(args):
    try:
      bstack1lll11l11l_opy_ = True
      logger.debug(bstack1lll11l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡻࡾࠩ౱").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack1lll11l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡵ࡫ࡲࡧࡱࡵࡱࠥࡹࡣࡢࡰࠣࡿࢂ࠭౲").format(str(err)))
    bstack1lll11l11l_opy_ = False
  response = bstack1llll11l1l_opy_(self, driver_command, *args, **kwargs)
  if (bstack1lll11l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ౳") in str(bstack1l11l11ll_opy_).lower() or bstack1lll11l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ౴") in str(bstack1l11l11ll_opy_).lower()) and bstack1l11111l_opy_.on():
    try:
      if driver_command == bstack1lll11l_opy_ (u"ࠫࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࠨ౵"):
        bstack1l111l1l_opy_.bstack1ll111lll1_opy_({
            bstack1lll11l_opy_ (u"ࠬ࡯࡭ࡢࡩࡨࠫ౶"): response[bstack1lll11l_opy_ (u"࠭ࡶࡢ࡮ࡸࡩࠬ౷")],
            bstack1lll11l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ౸"): bstack1l111l1l_opy_.current_test_uuid() if bstack1l111l1l_opy_.current_test_uuid() else bstack1l11111l_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack111ll111l1_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1l1ll1llll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1l11l1l1ll_opy_
  global bstack11ll11ll1l_opy_
  global bstack11ll1lll1_opy_
  global bstack1l111l11l_opy_
  global bstack1l11ll11ll_opy_
  global bstack1l11l11ll_opy_
  global bstack1l11l1lll_opy_
  global bstack1l1lll1ll_opy_
  global bstack1l1l1l11ll_opy_
  global bstack111l11l11l_opy_
  if os.getenv(bstack1lll11l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭౹")) is not None and bstack111ll1ll_opy_.bstack1111111l1_opy_(CONFIG) is None:
    CONFIG[bstack1lll11l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ౺")] = True
  CONFIG[bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ౻")] = str(bstack1l11l11ll_opy_) + str(__version__)
  bstack11l1lll11l_opy_ = os.environ[bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ౼")]
  bstack11llll1l1_opy_ = bstack11lll11lll_opy_.bstack1ll1ll111_opy_(CONFIG, bstack1l11l11ll_opy_)
  CONFIG[bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ౽")] = bstack11l1lll11l_opy_
  CONFIG[bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨ౾")] = bstack11llll1l1_opy_
  if CONFIG.get(bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ౿"),bstack1lll11l_opy_ (u"ࠨࠩಀ")) and bstack1lll11l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨಁ") in bstack1l11l11ll_opy_:
    CONFIG[bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪಂ")].pop(bstack1lll11l_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩಃ"), None)
    CONFIG[bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ಄")].pop(bstack1lll11l_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫಅ"), None)
  command_executor = bstack11l11lll1l_opy_()
  logger.debug(bstack1l111ll11_opy_.format(command_executor))
  proxy = bstack1ll1l1lll_opy_(CONFIG, proxy)
  bstack11lll1l11_opy_ = 0 if bstack11ll11ll1l_opy_ < 0 else bstack11ll11ll1l_opy_
  try:
    if bstack1l111l11l_opy_ is True:
      bstack11lll1l11_opy_ = int(multiprocessing.current_process().name)
    elif bstack1l11ll11ll_opy_ is True:
      bstack11lll1l11_opy_ = int(threading.current_thread().name)
  except:
    bstack11lll1l11_opy_ = 0
  bstack1l1l1lll1l_opy_ = bstack1llll11111_opy_(CONFIG, bstack11lll1l11_opy_)
  logger.debug(bstack1111l111ll_opy_.format(str(bstack1l1l1lll1l_opy_)))
  if bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫಆ") in CONFIG and bstack111llll1l_opy_(CONFIG[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬಇ")]):
    bstack1ll1111l1_opy_(bstack1l1l1lll1l_opy_)
  if bstack111ll1ll_opy_.bstack1111l111l_opy_(CONFIG, bstack11lll1l11_opy_) and bstack111ll1ll_opy_.bstack111l1l1111_opy_(bstack1l1l1lll1l_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack111ll1ll_opy_.set_capabilities(bstack1l1l1lll1l_opy_, CONFIG)
  if desired_capabilities:
    bstack111l11lll_opy_ = bstack1111ll1ll_opy_(desired_capabilities)
    bstack111l11lll_opy_[bstack1lll11l_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩಈ")] = bstack1l1ll1111_opy_(CONFIG)
    bstack1ll11lll1_opy_ = bstack1llll11111_opy_(bstack111l11lll_opy_)
    if bstack1ll11lll1_opy_:
      bstack1l1l1lll1l_opy_ = update(bstack1ll11lll1_opy_, bstack1l1l1lll1l_opy_)
    desired_capabilities = None
  if options:
    bstack11l1111l11_opy_(options, bstack1l1l1lll1l_opy_)
  if not options:
    options = bstack1ll1l111ll_opy_(bstack1l1l1lll1l_opy_)
  bstack111l11l11l_opy_ = CONFIG.get(bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಉ"))[bstack11lll1l11_opy_]
  if proxy and bstack111l1l111l_opy_() >= version.parse(bstack1lll11l_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫಊ")):
    options.proxy(proxy)
  if options and bstack111l1l111l_opy_() >= version.parse(bstack1lll11l_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫಋ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack111l1l111l_opy_() < version.parse(bstack1lll11l_opy_ (u"࠭࠳࠯࠺࠱࠴ࠬಌ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1l1l1lll1l_opy_)
  logger.info(bstack1ll111111_opy_)
  bstack1ll1ll1lll_opy_.end(EVENTS.bstack11l1llll11_opy_.value, EVENTS.bstack11l1llll11_opy_.value + bstack1lll11l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ಍"), EVENTS.bstack11l1llll11_opy_.value + bstack1lll11l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨಎ"), status=True, failure=None, test_name=bstack11ll1lll1_opy_)
  if bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡴࡷࡵࡦࡪ࡮ࡨࠫಏ") in kwargs:
    del kwargs[bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡵࡸ࡯ࡧ࡫࡯ࡩࠬಐ")]
  try:
    if bstack111l1l111l_opy_() >= version.parse(bstack1lll11l_opy_ (u"ࠫ࠹࠴࠱࠱࠰࠳ࠫ಑")):
      bstack1l11l1lll_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack111l1l111l_opy_() >= version.parse(bstack1lll11l_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫಒ")):
      bstack1l11l1lll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack111l1l111l_opy_() >= version.parse(bstack1lll11l_opy_ (u"࠭࠲࠯࠷࠶࠲࠵࠭ಓ")):
      bstack1l11l1lll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1l11l1lll_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack111ll1l111_opy_:
    logger.error(bstack1ll11lll11_opy_.format(bstack1lll11l_opy_ (u"ࠧࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰ࠭ಔ"), str(bstack111ll1l111_opy_)))
    raise bstack111ll1l111_opy_
  if bstack111ll1ll_opy_.bstack1111l111l_opy_(CONFIG, bstack11lll1l11_opy_) and bstack111ll1ll_opy_.bstack111l1l1111_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪಕ")][bstack1lll11l_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨಖ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack111ll1ll_opy_.set_capabilities(bstack1l1l1lll1l_opy_, CONFIG)
  try:
    bstack1l111111l1_opy_ = bstack1lll11l_opy_ (u"ࠪࠫಗ")
    if bstack111l1l111l_opy_() >= version.parse(bstack1lll11l_opy_ (u"ࠫ࠹࠴࠰࠯࠲ࡥ࠵ࠬಘ")):
      if self.caps is not None:
        bstack1l111111l1_opy_ = self.caps.get(bstack1lll11l_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧಙ"))
    else:
      if self.capabilities is not None:
        bstack1l111111l1_opy_ = self.capabilities.get(bstack1lll11l_opy_ (u"ࠨ࡯ࡱࡶ࡬ࡱࡦࡲࡈࡶࡤࡘࡶࡱࠨಚ"))
    if bstack1l111111l1_opy_:
      bstack1111l1l1ll_opy_(bstack1l111111l1_opy_)
      if bstack111l1l111l_opy_() <= version.parse(bstack1lll11l_opy_ (u"ࠧ࠴࠰࠴࠷࠳࠶ࠧಛ")):
        self.command_executor._url = bstack1lll11l_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤಜ") + bstack111l1llll_opy_ + bstack1lll11l_opy_ (u"ࠤ࠽࠼࠵࠵ࡷࡥ࠱࡫ࡹࡧࠨಝ")
      else:
        self.command_executor._url = bstack1lll11l_opy_ (u"ࠥ࡬ࡹࡺࡰࡴ࠼࠲࠳ࠧಞ") + bstack1l111111l1_opy_ + bstack1lll11l_opy_ (u"ࠦ࠴ࡽࡤ࠰ࡪࡸࡦࠧಟ")
      logger.debug(bstack1ll1lll1l_opy_.format(bstack1l111111l1_opy_))
    else:
      logger.debug(bstack1l1l1ll1l1_opy_.format(bstack1lll11l_opy_ (u"ࠧࡕࡰࡵ࡫ࡰࡥࡱࠦࡈࡶࡤࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩࠨಠ")))
  except Exception as e:
    logger.debug(bstack1l1l1ll1l1_opy_.format(e))
  if bstack1lll11l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬಡ") in bstack1l11l11ll_opy_:
    bstack1llll1111l_opy_(bstack11ll11ll1l_opy_, bstack1l1l1l11ll_opy_)
  bstack1l11l1l1ll_opy_ = self.session_id
  if bstack1lll11l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧಢ") in bstack1l11l11ll_opy_ or bstack1lll11l_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨಣ") in bstack1l11l11ll_opy_ or bstack1lll11l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨತ") in bstack1l11l11ll_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack1111ll1l1l_opy_ = getattr(threading.current_thread(), bstack1lll11l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡗࡩࡸࡺࡍࡦࡶࡤࠫಥ"), None)
  if bstack1lll11l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫದ") in bstack1l11l11ll_opy_ or bstack1lll11l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫಧ") in bstack1l11l11ll_opy_:
    bstack1l111l1l_opy_.bstack1ll11l1ll1_opy_(self)
  if bstack1lll11l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ನ") in bstack1l11l11ll_opy_ and bstack1111ll1l1l_opy_ and bstack1111ll1l1l_opy_.get(bstack1lll11l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ಩"), bstack1lll11l_opy_ (u"ࠨࠩಪ")) == bstack1lll11l_opy_ (u"ࠩࡳࡩࡳࡪࡩ࡯ࡩࠪಫ"):
    bstack1l111l1l_opy_.bstack1ll11l1ll1_opy_(self)
  with bstack1ll111l111_opy_:
    bstack1l1lll1ll_opy_.append(self)
  if bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ಬ") in CONFIG and bstack1lll11l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩಭ") in CONFIG[bstack1lll11l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨಮ")][bstack11lll1l11_opy_]:
    bstack11ll1lll1_opy_ = CONFIG[bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩಯ")][bstack11lll1l11_opy_][bstack1lll11l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬರ")]
  logger.debug(bstack111lll1111_opy_.format(bstack1l11l1l1ll_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1l1111l11_opy_
    def bstack1llll111ll_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1ll11llll_opy_
      if(bstack1lll11l_opy_ (u"ࠣ࡫ࡱࡨࡪࡾ࠮࡫ࡵࠥಱ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠩࢁࠫಲ")), bstack1lll11l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪಳ"), bstack1lll11l_opy_ (u"ࠫ࠳ࡹࡥࡴࡵ࡬ࡳࡳ࡯ࡤࡴ࠰ࡷࡼࡹ࠭಴")), bstack1lll11l_opy_ (u"ࠬࡽࠧವ")) as fp:
          fp.write(bstack1lll11l_opy_ (u"ࠨࠢಶ"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack1lll11l_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤಷ")))):
          with open(args[1], bstack1lll11l_opy_ (u"ࠨࡴࠪಸ")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack1lll11l_opy_ (u"ࠩࡤࡷࡾࡴࡣࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡣࡳ࡫ࡷࡑࡣࡪࡩ࠭ࡩ࡯࡯ࡶࡨࡼࡹ࠲ࠠࡱࡣࡪࡩࠥࡃࠠࡷࡱ࡬ࡨࠥ࠶ࠩࠨಹ") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1l1ll1l11_opy_)
            if bstack1lll11l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ಺") in CONFIG and str(CONFIG[bstack1lll11l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ಻")]).lower() != bstack1lll11l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨ಼ࠫ"):
                bstack111l111111_opy_ = bstack1l1111l11_opy_()
                bstack1lllll1lll_opy_ = bstack1lll11l_opy_ (u"࠭ࠧࠨࠌ࠲࠮ࠥࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾ࠢ࠭࠳ࠏࡩ࡯࡯ࡵࡷࠤࡧࡹࡴࡢࡥ࡮ࡣࡵࡧࡴࡩࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࡞ࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰࡯ࡩࡳ࡭ࡴࡩࠢ࠰ࠤ࠸ࡣ࠻ࠋࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࠾ࠎࡨࡵ࡮ࡴࡶࠣࡴࡤ࡯࡮ࡥࡧࡻࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠲࡞࠽ࠍࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷࠢࡀࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡷࡱ࡯ࡣࡦࠪ࠳࠰ࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠳ࠪ࠽ࠍࡧࡴࡴࡳࡵࠢ࡬ࡱࡵࡵࡲࡵࡡࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠺࡟ࡣࡵࡷࡥࡨࡱࠠ࠾ࠢࡵࡩࡶࡻࡩࡳࡧࠫࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣࠫ࠾ࠎ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡱࡧࡵ࡯ࡥ࡫ࠤࡂࠦࡡࡴࡻࡱࡧࠥ࠮࡬ࡢࡷࡱࡧ࡭ࡕࡰࡵ࡫ࡲࡲࡸ࠯ࠠ࠾ࡀࠣࡿࢀࠐࠠࠡ࡮ࡨࡸࠥࡩࡡࡱࡵ࠾ࠎࠥࠦࡴࡳࡻࠣࡿࢀࠐࠠࠡࠢࠣࡧࡦࡶࡳࠡ࠿ࠣࡎࡘࡕࡎ࠯ࡲࡤࡶࡸ࡫ࠨࡣࡵࡷࡥࡨࡱ࡟ࡤࡣࡳࡷ࠮ࡁࠊࠡࠢࢀࢁࠥࡩࡡࡵࡥ࡫ࠤ࠭࡫ࡸࠪࠢࡾࡿࠏࠦࠠࠡࠢࡦࡳࡳࡹ࡯࡭ࡧ࠱ࡩࡷࡸ࡯ࡳࠪࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡰࡢࡴࡶࡩࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠾ࠧ࠲ࠠࡦࡺࠬ࠿ࠏࠦࠠࡾࡿࠍࠤࠥࡸࡥࡵࡷࡵࡲࠥࡧࡷࡢ࡫ࡷࠤ࡮ࡳࡰࡰࡴࡷࡣࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴ࠵ࡡࡥࡷࡹࡧࡣ࡬࠰ࡦ࡬ࡷࡵ࡭ࡪࡷࡰ࠲ࡨࡵ࡮࡯ࡧࡦࡸ࠭ࢁࡻࠋࠢࠣࠤࠥࡽࡳࡆࡰࡧࡴࡴ࡯࡮ࡵ࠼ࠣࠫࢀࡩࡤࡱࡗࡵࡰࢂ࠭ࠠࠬࠢࡨࡲࡨࡵࡤࡦࡗࡕࡍࡈࡵ࡭ࡱࡱࡱࡩࡳࡺࠨࡋࡕࡒࡒ࠳ࡹࡴࡳ࡫ࡱ࡫࡮࡬ࡹࠩࡥࡤࡴࡸ࠯ࠩ࠭ࠌࠣࠤࠥࠦ࠮࠯࠰࡯ࡥࡺࡴࡣࡩࡑࡳࡸ࡮ࡵ࡮ࡴࠌࠣࠤࢂࢃࠩ࠼ࠌࢀࢁࡀࠐ࠯ࠫࠢࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࠦࠪ࠰ࠌࠪࠫࠬಽ").format(bstack111l111111_opy_=bstack111l111111_opy_)
            lines.insert(1, bstack1lllll1lll_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack1lll11l_opy_ (u"ࠢࡪࡰࡧࡩࡽࡥࡢࡴࡶࡤࡧࡰ࠴ࡪࡴࠤಾ")), bstack1lll11l_opy_ (u"ࠨࡹࠪಿ")) as bstack111l111ll_opy_:
              bstack111l111ll_opy_.writelines(lines)
        CONFIG[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫೀ")] = str(bstack1l11l11ll_opy_) + str(__version__)
        bstack11l1lll11l_opy_ = os.environ[bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨು")]
        bstack11llll1l1_opy_ = bstack11lll11lll_opy_.bstack1ll1ll111_opy_(CONFIG, bstack1l11l11ll_opy_)
        CONFIG[bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧೂ")] = bstack11l1lll11l_opy_
        CONFIG[bstack1lll11l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧೃ")] = bstack11llll1l1_opy_
        bstack11lll1l11_opy_ = 0 if bstack11ll11ll1l_opy_ < 0 else bstack11ll11ll1l_opy_
        try:
          if bstack1l111l11l_opy_ is True:
            bstack11lll1l11_opy_ = int(multiprocessing.current_process().name)
          elif bstack1l11ll11ll_opy_ is True:
            bstack11lll1l11_opy_ = int(threading.current_thread().name)
        except:
          bstack11lll1l11_opy_ = 0
        CONFIG[bstack1lll11l_opy_ (u"ࠨࡵࡴࡧ࡚࠷ࡈࠨೄ")] = False
        CONFIG[bstack1lll11l_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨ೅")] = True
        bstack1l1l1lll1l_opy_ = bstack1llll11111_opy_(CONFIG, bstack11lll1l11_opy_)
        logger.debug(bstack1111l111ll_opy_.format(str(bstack1l1l1lll1l_opy_)))
        if CONFIG.get(bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬೆ")):
          bstack1ll1111l1_opy_(bstack1l1l1lll1l_opy_)
        if bstack1lll11l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೇ") in CONFIG and bstack1lll11l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨೈ") in CONFIG[bstack1lll11l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ೉")][bstack11lll1l11_opy_]:
          bstack11ll1lll1_opy_ = CONFIG[bstack1lll11l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨೊ")][bstack11lll1l11_opy_][bstack1lll11l_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫೋ")]
        args.append(os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠧࡿࠩೌ")), bstack1lll11l_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨ್"), bstack1lll11l_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ೎")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1l1l1lll1l_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack1lll11l_opy_ (u"ࠥ࡭ࡳࡪࡥࡹࡡࡥࡷࡹࡧࡣ࡬࠰࡭ࡷࠧ೏"))
      bstack1ll11llll_opy_ = True
      return bstack11l111ll1l_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack1ll1ll11l1_opy_(self,
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
    global bstack11ll11ll1l_opy_
    global bstack11ll1lll1_opy_
    global bstack1l111l11l_opy_
    global bstack1l11ll11ll_opy_
    global bstack1l11l11ll_opy_
    CONFIG[bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡖࡈࡐ࠭೐")] = str(bstack1l11l11ll_opy_) + str(__version__)
    bstack11l1lll11l_opy_ = os.environ[bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ೑")]
    bstack11llll1l1_opy_ = bstack11lll11lll_opy_.bstack1ll1ll111_opy_(CONFIG, bstack1l11l11ll_opy_)
    CONFIG[bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷ࡬ࡺࡨࡂࡶ࡫࡯ࡨ࡚ࡻࡩࡥࠩ೒")] = bstack11l1lll11l_opy_
    CONFIG[bstack1lll11l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩ೓")] = bstack11llll1l1_opy_
    bstack11lll1l11_opy_ = 0 if bstack11ll11ll1l_opy_ < 0 else bstack11ll11ll1l_opy_
    try:
      if bstack1l111l11l_opy_ is True:
        bstack11lll1l11_opy_ = int(multiprocessing.current_process().name)
      elif bstack1l11ll11ll_opy_ is True:
        bstack11lll1l11_opy_ = int(threading.current_thread().name)
    except:
      bstack11lll1l11_opy_ = 0
    CONFIG[bstack1lll11l_opy_ (u"ࠣ࡫ࡶࡔࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ೔")] = True
    bstack1l1l1lll1l_opy_ = bstack1llll11111_opy_(CONFIG, bstack11lll1l11_opy_)
    logger.debug(bstack1111l111ll_opy_.format(str(bstack1l1l1lll1l_opy_)))
    if CONFIG.get(bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ೕ")):
      bstack1ll1111l1_opy_(bstack1l1l1lll1l_opy_)
    if bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ೖ") in CONFIG and bstack1lll11l_opy_ (u"ࠫࡸ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ೗") in CONFIG[bstack1lll11l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ೘")][bstack11lll1l11_opy_]:
      bstack11ll1lll1_opy_ = CONFIG[bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ೙")][bstack11lll1l11_opy_][bstack1lll11l_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ೚")]
    import urllib
    import json
    if bstack1lll11l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ೛") in CONFIG and str(CONFIG[bstack1lll11l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭೜")]).lower() != bstack1lll11l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩೝ"):
        bstack111llll11_opy_ = bstack1l1111l11_opy_()
        bstack111l111111_opy_ = bstack111llll11_opy_ + urllib.parse.quote(json.dumps(bstack1l1l1lll1l_opy_))
    else:
        bstack111l111111_opy_ = bstack1lll11l_opy_ (u"ࠫࡼࡹࡳ࠻࠱࠲ࡧࡩࡶ࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯࠲ࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠿ࡤࡣࡳࡷࡂ࠭ೞ") + urllib.parse.quote(json.dumps(bstack1l1l1lll1l_opy_))
    browser = self.connect(bstack111l111111_opy_)
    return browser
except Exception as e:
    pass
def bstack1l1l11l1ll_opy_():
    global bstack1ll11llll_opy_
    global bstack1l11l11ll_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack11ll1111l1_opy_
        global bstack111ll1l1_opy_
        if not bstack111ll1llll_opy_:
          global bstack1ll111llll_opy_
          if not bstack1ll111llll_opy_:
            from bstack_utils.helper import bstack111l11111_opy_, bstack1l11l111l_opy_, bstack1l111l1111_opy_
            bstack1ll111llll_opy_ = bstack111l11111_opy_()
            bstack1l11l111l_opy_(bstack1l11l11ll_opy_)
            bstack11llll1l1_opy_ = bstack11lll11lll_opy_.bstack1ll1ll111_opy_(CONFIG, bstack1l11l11ll_opy_)
            bstack111ll1l1_opy_.set_property(bstack1lll11l_opy_ (u"ࠧࡖࡌࡂ࡛࡚ࡖࡎࡍࡈࡕࡡࡓࡖࡔࡊࡕࡄࡖࡢࡑࡆࡖࠢ೟"), bstack11llll1l1_opy_)
          BrowserType.connect = bstack11ll1111l1_opy_
          return
        BrowserType.launch = bstack1ll1ll11l1_opy_
        bstack1ll11llll_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1llll111ll_opy_
      bstack1ll11llll_opy_ = True
    except Exception as e:
      pass
def bstack1l11l1ll11_opy_(context, bstack1ll1l11l11_opy_):
  try:
    context.page.evaluate(bstack1lll11l_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢೠ"), bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠫೡ")+ json.dumps(bstack1ll1l11l11_opy_) + bstack1lll11l_opy_ (u"ࠣࡿࢀࠦೢ"))
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠤࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤࢀࢃ࠺ࠡࡽࢀࠦೣ").format(str(e), traceback.format_exc()))
def bstack1l1ll11ll_opy_(context, message, level):
  try:
    context.page.evaluate(bstack1lll11l_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦ೤"), bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩ೥") + json.dumps(message) + bstack1lll11l_opy_ (u"ࠬ࠲ࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠨ೦") + json.dumps(level) + bstack1lll11l_opy_ (u"࠭ࡽࡾࠩ೧"))
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠢࡦࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡥࡳࡴ࡯ࡵࡣࡷ࡭ࡴࡴࠠࡼࡿ࠽ࠤࢀࢃࠢ೨").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1l1l1ll1l_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack111l1111ll_opy_(self, url):
  global bstack1ll1l11l1_opy_
  try:
    bstack11llll11ll_opy_(url)
  except Exception as err:
    logger.debug(bstack11lll1l111_opy_.format(str(err)))
  try:
    bstack1ll1l11l1_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack11ll11l1l1_opy_):
        bstack11llll11ll_opy_(url, True)
    except Exception as err:
      logger.debug(bstack11lll1l111_opy_.format(str(err)))
    raise e
def bstack1lll1ll111_opy_(self):
  global bstack111lllllll_opy_
  bstack111lllllll_opy_ = self
  return
def bstack1l1111l1l1_opy_(self):
  global bstack11llll1l11_opy_
  bstack11llll1l11_opy_ = self
  return
def bstack1ll1l11ll1_opy_(test_name, bstack11l1l11ll_opy_):
  global CONFIG
  if percy.bstack1ll1111ll1_opy_() == bstack1lll11l_opy_ (u"ࠣࡶࡵࡹࡪࠨ೩"):
    bstack11ll1ll111_opy_ = os.path.relpath(bstack11l1l11ll_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack11ll1ll111_opy_)
    bstack1l1llll1l_opy_ = suite_name + bstack1lll11l_opy_ (u"ࠤ࠰ࠦ೪") + test_name
    threading.current_thread().percySessionName = bstack1l1llll1l_opy_
def bstack11ll1ll11_opy_(self, test, *args, **kwargs):
  global bstack1111lll11_opy_
  test_name = None
  bstack11l1l11ll_opy_ = None
  if test:
    test_name = str(test.name)
    bstack11l1l11ll_opy_ = str(test.source)
  bstack1ll1l11ll1_opy_(test_name, bstack11l1l11ll_opy_)
  bstack1111lll11_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l1l11ll11_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1ll1l11l1l_opy_(driver, bstack1l1llll1l_opy_):
  if not bstack1lll11lll1_opy_ and bstack1l1llll1l_opy_:
      bstack11111ll11l_opy_ = {
          bstack1lll11l_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪ೫"): bstack1lll11l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ೬"),
          bstack1lll11l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ೭"): {
              bstack1lll11l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ೮"): bstack1l1llll1l_opy_
          }
      }
      bstack1l1111l1l_opy_ = bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬ೯").format(json.dumps(bstack11111ll11l_opy_))
      driver.execute_script(bstack1l1111l1l_opy_)
  if bstack1lll11l111_opy_:
      bstack1ll11111l1_opy_ = {
          bstack1lll11l_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨ೰"): bstack1lll11l_opy_ (u"ࠩࡤࡲࡳࡵࡴࡢࡶࡨࠫೱ"),
          bstack1lll11l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ೲ"): {
              bstack1lll11l_opy_ (u"ࠫࡩࡧࡴࡢࠩೳ"): bstack1l1llll1l_opy_ + bstack1lll11l_opy_ (u"ࠬࠦࡰࡢࡵࡶࡩࡩࠧࠧ೴"),
              bstack1lll11l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ೵"): bstack1lll11l_opy_ (u"ࠧࡪࡰࡩࡳࠬ೶")
          }
      }
      if bstack1lll11l111_opy_.status == bstack1lll11l_opy_ (u"ࠨࡒࡄࡗࡘ࠭೷"):
          bstack1l1l111111_opy_ = bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࢃࠧ೸").format(json.dumps(bstack1ll11111l1_opy_))
          driver.execute_script(bstack1l1l111111_opy_)
          bstack1l1ll1l11l_opy_(driver, bstack1lll11l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ೹"))
      elif bstack1lll11l111_opy_.status == bstack1lll11l_opy_ (u"ࠫࡋࡇࡉࡍࠩ೺"):
          reason = bstack1lll11l_opy_ (u"ࠧࠨ೻")
          bstack1ll111ll11_opy_ = bstack1l1llll1l_opy_ + bstack1lll11l_opy_ (u"࠭ࠠࡧࡣ࡬ࡰࡪࡪࠧ೼")
          if bstack1lll11l111_opy_.message:
              reason = str(bstack1lll11l111_opy_.message)
              bstack1ll111ll11_opy_ = bstack1ll111ll11_opy_ + bstack1lll11l_opy_ (u"ࠧࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶ࠿ࠦࠧ೽") + reason
          bstack1ll11111l1_opy_[bstack1lll11l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ೾")] = {
              bstack1lll11l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨ೿"): bstack1lll11l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩഀ"),
              bstack1lll11l_opy_ (u"ࠫࡩࡧࡴࡢࠩഁ"): bstack1ll111ll11_opy_
          }
          bstack1l1l111111_opy_ = bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪം").format(json.dumps(bstack1ll11111l1_opy_))
          driver.execute_script(bstack1l1l111111_opy_)
          bstack1l1ll1l11l_opy_(driver, bstack1lll11l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ഃ"), reason)
          bstack1l11l1l11_opy_(reason, str(bstack1lll11l111_opy_), str(bstack11ll11ll1l_opy_), logger)
@measure(event_name=EVENTS.bstack111llll111_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1ll1ll1l11_opy_(driver, test):
  if percy.bstack1ll1111ll1_opy_() == bstack1lll11l_opy_ (u"ࠢࡵࡴࡸࡩࠧഄ") and percy.bstack11lllll11_opy_() == bstack1lll11l_opy_ (u"ࠣࡶࡨࡷࡹࡩࡡࡴࡧࠥഅ"):
      bstack1l11lll11_opy_ = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠩࡳࡩࡷࡩࡹࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬആ"), None)
      bstack11ll111l11_opy_(driver, bstack1l11lll11_opy_, test)
  if (bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧഇ"), None) and
      bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪഈ"), None)) or (
      bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬഉ"), None) and
      bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨഊ"), None)):
      logger.info(bstack1lll11l_opy_ (u"ࠢࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠥࡖࡲࡰࡥࡨࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡪࡵࠣࡹࡳࡪࡥࡳࡹࡤࡽ࠳ࠦࠢഋ"))
      bstack111ll1ll_opy_.bstack111lll11_opy_(driver, name=test.name, path=test.source)
def bstack1ll1lll1l1_opy_(test, bstack1l1llll1l_opy_):
    try:
      bstack11ll11l1l_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack1lll11l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ഌ")] = bstack1l1llll1l_opy_
      if bstack1lll11l111_opy_:
        if bstack1lll11l111_opy_.status == bstack1lll11l_opy_ (u"ࠩࡓࡅࡘ࡙ࠧ഍"):
          data[bstack1lll11l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪഎ")] = bstack1lll11l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫഏ")
        elif bstack1lll11l111_opy_.status == bstack1lll11l_opy_ (u"ࠬࡌࡁࡊࡎࠪഐ"):
          data[bstack1lll11l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭഑")] = bstack1lll11l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧഒ")
          if bstack1lll11l111_opy_.message:
            data[bstack1lll11l_opy_ (u"ࠨࡴࡨࡥࡸࡵ࡮ࠨഓ")] = str(bstack1lll11l111_opy_.message)
      user = CONFIG[bstack1lll11l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫഔ")]
      key = CONFIG[bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ക")]
      host = bstack11llll111_opy_(cli.config, [bstack1lll11l_opy_ (u"ࠦࡦࡶࡩࡴࠤഖ"), bstack1lll11l_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡫ࠢഗ"), bstack1lll11l_opy_ (u"ࠨࡡࡱ࡫ࠥഘ")], bstack1lll11l_opy_ (u"ࠢࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭ࠣങ"))
      url = bstack1lll11l_opy_ (u"ࠨࡽࢀ࠳ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠵ࡳࡦࡵࡶ࡭ࡴࡴࡳ࠰ࡽࢀ࠲࡯ࡹ࡯࡯ࠩച").format(host, bstack1l11l1l1ll_opy_)
      headers = {
        bstack1lll11l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡸࡾࡶࡥࠨഛ"): bstack1lll11l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭ജ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡸࡴࡩࡧࡴࡦࡡࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡷࡥࡹࡻࡳࠣഝ"), datetime.datetime.now() - bstack11ll11l1l_opy_)
    except Exception as e:
      logger.error(bstack11ll111111_opy_.format(str(e)))
def bstack1l1ll1l1ll_opy_(test, bstack1l1llll1l_opy_):
  global CONFIG
  global bstack11llll1l11_opy_
  global bstack111lllllll_opy_
  global bstack1l11l1l1ll_opy_
  global bstack1lll11l111_opy_
  global bstack11ll1lll1_opy_
  global bstack1l11l1l1l_opy_
  global bstack11lll111ll_opy_
  global bstack11lll1111l_opy_
  global bstack1ll11l1ll_opy_
  global bstack1l1lll1ll_opy_
  global bstack111l11l11l_opy_
  global bstack1ll1lll1ll_opy_
  try:
    if not bstack1l11l1l1ll_opy_:
      with bstack1ll1lll1ll_opy_:
        bstack11l11ll1ll_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠬࢄࠧഞ")), bstack1lll11l_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ട"), bstack1lll11l_opy_ (u"ࠧ࠯ࡵࡨࡷࡸ࡯࡯࡯࡫ࡧࡷ࠳ࡺࡸࡵࠩഠ"))
        if os.path.exists(bstack11l11ll1ll_opy_):
          with open(bstack11l11ll1ll_opy_, bstack1lll11l_opy_ (u"ࠨࡴࠪഡ")) as f:
            content = f.read().strip()
            if content:
              bstack11ll111lll_opy_ = json.loads(bstack1lll11l_opy_ (u"ࠤࡾࠦഢ") + content + bstack1lll11l_opy_ (u"ࠪࠦࡽࠨ࠺ࠡࠤࡼࠦࠬണ") + bstack1lll11l_opy_ (u"ࠦࢂࠨത"))
              bstack1l11l1l1ll_opy_ = bstack11ll111lll_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡉࡅࡵࠣࡪ࡮ࡲࡥ࠻ࠢࠪഥ") + str(e))
  if bstack1l1lll1ll_opy_:
    with bstack1ll111l111_opy_:
      bstack1111l1l111_opy_ = bstack1l1lll1ll_opy_.copy()
    for driver in bstack1111l1l111_opy_:
      if bstack1l11l1l1ll_opy_ == driver.session_id:
        if test:
          bstack1ll1ll1l11_opy_(driver, test)
        bstack1ll1l11l1l_opy_(driver, bstack1l1llll1l_opy_)
  elif bstack1l11l1l1ll_opy_:
    bstack1ll1lll1l1_opy_(test, bstack1l1llll1l_opy_)
  if bstack11llll1l11_opy_:
    bstack11lll111ll_opy_(bstack11llll1l11_opy_)
  if bstack111lllllll_opy_:
    bstack11lll1111l_opy_(bstack111lllllll_opy_)
  if bstack1l1ll11l1l_opy_:
    bstack1ll11l1ll_opy_()
def bstack111111l1ll_opy_(self, test, *args, **kwargs):
  bstack1l1llll1l_opy_ = None
  if test:
    bstack1l1llll1l_opy_ = str(test.name)
  bstack1l1ll1l1ll_opy_(test, bstack1l1llll1l_opy_)
  bstack1l11l1l1l_opy_(self, test, *args, **kwargs)
def bstack111lll11l_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1l111ll1l1_opy_
  global CONFIG
  global bstack1l1lll1ll_opy_
  global bstack1l11l1l1ll_opy_
  global bstack1ll1lll1ll_opy_
  bstack1111l11111_opy_ = None
  try:
    if bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬദ"), None) or bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩധ"), None):
      try:
        if not bstack1l11l1l1ll_opy_:
          bstack11l11ll1ll_opy_ = os.path.join(os.path.expanduser(bstack1lll11l_opy_ (u"ࠨࢀࠪന")), bstack1lll11l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩഩ"), bstack1lll11l_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬപ"))
          with bstack1ll1lll1ll_opy_:
            if os.path.exists(bstack11l11ll1ll_opy_):
              with open(bstack11l11ll1ll_opy_, bstack1lll11l_opy_ (u"ࠫࡷ࠭ഫ")) as f:
                content = f.read().strip()
                if content:
                  bstack11ll111lll_opy_ = json.loads(bstack1lll11l_opy_ (u"ࠧࢁࠢബ") + content + bstack1lll11l_opy_ (u"࠭ࠢࡹࠤ࠽ࠤࠧࡿࠢࠨഭ") + bstack1lll11l_opy_ (u"ࠢࡾࠤമ"))
                  bstack1l11l1l1ll_opy_ = bstack11ll111lll_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack1lll11l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡳࡧࡤࡨ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡌࡈࡸࠦࡦࡪ࡮ࡨࠤ࡮ࡴࠠࡵࡧࡶࡸࠥࡹࡴࡢࡶࡸࡷ࠿ࠦࠧയ") + str(e))
      if bstack1l1lll1ll_opy_:
        with bstack1ll111l111_opy_:
          bstack1111l1l111_opy_ = bstack1l1lll1ll_opy_.copy()
        for driver in bstack1111l1l111_opy_:
          if bstack1l11l1l1ll_opy_ == driver.session_id:
            bstack1111l11111_opy_ = driver
    bstack11lll1lll1_opy_ = bstack111ll1ll_opy_.bstack111111l1l1_opy_(test.tags)
    if bstack1111l11111_opy_:
      threading.current_thread().isA11yTest = bstack111ll1ll_opy_.bstack1111l11l1l_opy_(bstack1111l11111_opy_, bstack11lll1lll1_opy_)
      threading.current_thread().isAppA11yTest = bstack111ll1ll_opy_.bstack1111l11l1l_opy_(bstack1111l11111_opy_, bstack11lll1lll1_opy_)
    else:
      threading.current_thread().isA11yTest = bstack11lll1lll1_opy_
      threading.current_thread().isAppA11yTest = bstack11lll1lll1_opy_
  except:
    pass
  bstack1l111ll1l1_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack1lll11l111_opy_
  try:
    bstack1lll11l111_opy_ = self._test
  except:
    bstack1lll11l111_opy_ = self.test
def bstack1111l11ll1_opy_():
  global bstack1l1l1ll111_opy_
  try:
    if os.path.exists(bstack1l1l1ll111_opy_):
      os.remove(bstack1l1l1ll111_opy_)
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡩ࡫࡬ࡦࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬര") + str(e))
def bstack1lll1l1ll1_opy_():
  global bstack1l1l1ll111_opy_
  bstack111l1ll111_opy_ = {}
  lock_file = bstack1l1l1ll111_opy_ + bstack1lll11l_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩറ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lll11l_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧല"))
    try:
      if not os.path.isfile(bstack1l1l1ll111_opy_):
        with open(bstack1l1l1ll111_opy_, bstack1lll11l_opy_ (u"ࠬࡽࠧള")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1l1l1ll111_opy_):
        with open(bstack1l1l1ll111_opy_, bstack1lll11l_opy_ (u"࠭ࡲࠨഴ")) as f:
          content = f.read().strip()
          if content:
            bstack111l1ll111_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack1lll11l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩവ") + str(e))
    return bstack111l1ll111_opy_
  try:
    os.makedirs(os.path.dirname(bstack1l1l1ll111_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack1l1l1ll111_opy_):
        with open(bstack1l1l1ll111_opy_, bstack1lll11l_opy_ (u"ࠨࡹࠪശ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1l1l1ll111_opy_):
        with open(bstack1l1l1ll111_opy_, bstack1lll11l_opy_ (u"ࠩࡵࠫഷ")) as f:
          content = f.read().strip()
          if content:
            bstack111l1ll111_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡸࡥࡢࡦ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬസ") + str(e))
  finally:
    return bstack111l1ll111_opy_
def bstack1llll1111l_opy_(platform_index, item_index):
  global bstack1l1l1ll111_opy_
  lock_file = bstack1l1l1ll111_opy_ + bstack1lll11l_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪഹ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack1lll11l_opy_ (u"ࠬ࡬ࡩ࡭ࡧ࡯ࡳࡨࡱࠠ࡯ࡱࡷࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡣࡣࡶ࡭ࡨࠦࡦࡪ࡮ࡨࠤࡴࡶࡥࡳࡣࡷ࡭ࡴࡴࡳࠨഺ"))
    try:
      bstack111l1ll111_opy_ = {}
      if os.path.exists(bstack1l1l1ll111_opy_):
        with open(bstack1l1l1ll111_opy_, bstack1lll11l_opy_ (u"࠭ࡲࠨ഻")) as f:
          content = f.read().strip()
          if content:
            bstack111l1ll111_opy_ = json.loads(content)
      bstack111l1ll111_opy_[item_index] = platform_index
      with open(bstack1l1l1ll111_opy_, bstack1lll11l_opy_ (u"ࠢࡸࠤ഼")) as outfile:
        json.dump(bstack111l1ll111_opy_, outfile)
    except Exception as e:
      logger.debug(bstack1lll11l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡻࡷ࡯ࡴࡪࡰࡪࠤࡹࡵࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹࠦࡦࡪ࡮ࡨ࠾ࠥ࠭ഽ") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack1l1l1ll111_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack111l1ll111_opy_ = {}
      if os.path.exists(bstack1l1l1ll111_opy_):
        with open(bstack1l1l1ll111_opy_, bstack1lll11l_opy_ (u"ࠩࡵࠫാ")) as f:
          content = f.read().strip()
          if content:
            bstack111l1ll111_opy_ = json.loads(content)
      bstack111l1ll111_opy_[item_index] = platform_index
      with open(bstack1l1l1ll111_opy_, bstack1lll11l_opy_ (u"ࠥࡻࠧി")) as outfile:
        json.dump(bstack111l1ll111_opy_, outfile)
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡷࡳ࡫ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࡶࡴࡨ࡯ࡵࠢࡵࡩࡵࡵࡲࡵࠢࡩ࡭ࡱ࡫࠺ࠡࠩീ") + str(e))
def bstack11ll1l11l1_opy_(bstack1lllll1l1l_opy_):
  global CONFIG
  bstack1l11ll1lll_opy_ = bstack1lll11l_opy_ (u"ࠬ࠭ു")
  if not bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩൂ") in CONFIG:
    logger.info(bstack1lll11l_opy_ (u"ࠧࡏࡱࠣࡴࡱࡧࡴࡧࡱࡵࡱࡸࠦࡰࡢࡵࡶࡩࡩࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡪࡩࡳ࡫ࡲࡢࡶࡨࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫ࡵࡲࠡࡔࡲࡦࡴࡺࠠࡳࡷࡱࠫൃ"))
  try:
    platform = CONFIG[bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫൄ")][bstack1lllll1l1l_opy_]
    if bstack1lll11l_opy_ (u"ࠩࡲࡷࠬ൅") in platform:
      bstack1l11ll1lll_opy_ += str(platform[bstack1lll11l_opy_ (u"ࠪࡳࡸ࠭െ")]) + bstack1lll11l_opy_ (u"ࠫ࠱ࠦࠧേ")
    if bstack1lll11l_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨൈ") in platform:
      bstack1l11ll1lll_opy_ += str(platform[bstack1lll11l_opy_ (u"࠭࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠩ൉")]) + bstack1lll11l_opy_ (u"ࠧ࠭ࠢࠪൊ")
    if bstack1lll11l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬോ") in platform:
      bstack1l11ll1lll_opy_ += str(platform[bstack1lll11l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪ࠭ൌ")]) + bstack1lll11l_opy_ (u"ࠪ࠰്ࠥ࠭")
    if bstack1lll11l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ൎ") in platform:
      bstack1l11ll1lll_opy_ += str(platform[bstack1lll11l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ൏")]) + bstack1lll11l_opy_ (u"࠭ࠬࠡࠩ൐")
    if bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ൑") in platform:
      bstack1l11ll1lll_opy_ += str(platform[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭൒")]) + bstack1lll11l_opy_ (u"ࠩ࠯ࠤࠬ൓")
    if bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫൔ") in platform:
      bstack1l11ll1lll_opy_ += str(platform[bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬൕ")]) + bstack1lll11l_opy_ (u"ࠬ࠲ࠠࠨൖ")
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"࠭ࡓࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡧࡦࡰࡨࡶࡦࡺࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡹࡴࡳ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡵࡩࡵࡵࡲࡵࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡳࡳ࠭ൗ") + str(e))
  finally:
    if bstack1l11ll1lll_opy_[len(bstack1l11ll1lll_opy_) - 2:] == bstack1lll11l_opy_ (u"ࠧ࠭ࠢࠪ൘"):
      bstack1l11ll1lll_opy_ = bstack1l11ll1lll_opy_[:-2]
    return bstack1l11ll1lll_opy_
def bstack11l1lll111_opy_(path, bstack1l11ll1lll_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1l11l1l111_opy_ = ET.parse(path)
    bstack1111llll1l_opy_ = bstack1l11l1l111_opy_.getroot()
    bstack1l1l111ll_opy_ = None
    for suite in bstack1111llll1l_opy_.iter(bstack1lll11l_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧ൙")):
      if bstack1lll11l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ൚") in suite.attrib:
        suite.attrib[bstack1lll11l_opy_ (u"ࠪࡲࡦࡳࡥࠨ൛")] += bstack1lll11l_opy_ (u"ࠫࠥ࠭൜") + bstack1l11ll1lll_opy_
        bstack1l1l111ll_opy_ = suite
    bstack111ll11ll1_opy_ = None
    for robot in bstack1111llll1l_opy_.iter(bstack1lll11l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ൝")):
      bstack111ll11ll1_opy_ = robot
    bstack1l1lll11ll_opy_ = len(bstack111ll11ll1_opy_.findall(bstack1lll11l_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൞")))
    if bstack1l1lll11ll_opy_ == 1:
      bstack111ll11ll1_opy_.remove(bstack111ll11ll1_opy_.findall(bstack1lll11l_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ൟ"))[0])
      bstack11l1lll1l1_opy_ = ET.Element(bstack1lll11l_opy_ (u"ࠨࡵࡸ࡭ࡹ࡫ࠧൠ"), attrib={bstack1lll11l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧൡ"): bstack1lll11l_opy_ (u"ࠪࡗࡺ࡯ࡴࡦࡵࠪൢ"), bstack1lll11l_opy_ (u"ࠫ࡮ࡪࠧൣ"): bstack1lll11l_opy_ (u"ࠬࡹ࠰ࠨ൤")})
      bstack111ll11ll1_opy_.insert(1, bstack11l1lll1l1_opy_)
      bstack1111l1llll_opy_ = None
      for suite in bstack111ll11ll1_opy_.iter(bstack1lll11l_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬ൥")):
        bstack1111l1llll_opy_ = suite
      bstack1111l1llll_opy_.append(bstack1l1l111ll_opy_)
      bstack1lll1l1111_opy_ = None
      for status in bstack1l1l111ll_opy_.iter(bstack1lll11l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ൦")):
        bstack1lll1l1111_opy_ = status
      bstack1111l1llll_opy_.append(bstack1lll1l1111_opy_)
    bstack1l11l1l111_opy_.write(path)
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡸࡳࡪࡰࡪࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡴࡥࡳࡣࡷ࡭ࡳ࡭ࠠࡳࡱࡥࡳࡹࠦࡲࡦࡲࡲࡶࡹ࠭൧") + str(e))
def bstack11llllllll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack1lll111l1l_opy_
  global CONFIG
  if bstack1lll11l_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨ൨") in options:
    del options[bstack1lll11l_opy_ (u"ࠥࡴࡾࡺࡨࡰࡰࡳࡥࡹ࡮ࠢ൩")]
  json_data = bstack1lll1l1ll1_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack1lll11l_opy_ (u"ࠫࡵࡧࡢࡰࡶࡢࡶࡪࡹࡵ࡭ࡶࡶࠫ൪"), str(item_id), bstack1lll11l_opy_ (u"ࠬࡵࡵࡵࡲࡸࡸ࠳ࡾ࡭࡭ࠩ൫"))
    bstack11l1lll111_opy_(path, bstack11ll1l11l1_opy_(json_data[item_id]))
  bstack1111l11ll1_opy_()
  return bstack1lll111l1l_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack11l11lll1_opy_(self, ff_profile_dir):
  global bstack1lll1ll1ll_opy_
  if not ff_profile_dir:
    return None
  return bstack1lll1ll1ll_opy_(self, ff_profile_dir)
def bstack11llll1ll_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack1l1lll111_opy_
  bstack1ll11ll1l_opy_ = []
  if bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ൬") in CONFIG:
    bstack1ll11ll1l_opy_ = CONFIG[bstack1lll11l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ൭")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack1lll11l_opy_ (u"ࠣࡥࡲࡱࡲࡧ࡮ࡥࠤ൮")],
      pabot_args[bstack1lll11l_opy_ (u"ࠤࡹࡩࡷࡨ࡯ࡴࡧࠥ൯")],
      argfile,
      pabot_args.get(bstack1lll11l_opy_ (u"ࠥ࡬࡮ࡼࡥࠣ൰")),
      pabot_args[bstack1lll11l_opy_ (u"ࠦࡵࡸ࡯ࡤࡧࡶࡷࡪࡹࠢ൱")],
      platform[0],
      bstack1l1lll111_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack1lll11l_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡦࡪ࡮ࡨࡷࠧ൲")] or [(bstack1lll11l_opy_ (u"ࠨࠢ൳"), None)]
    for platform in enumerate(bstack1ll11ll1l_opy_)
  ]
def bstack1ll11llll1_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1l1lll11l1_opy_=bstack1lll11l_opy_ (u"ࠧࠨ൴")):
  global bstack1l1l111ll1_opy_
  self.platform_index = platform_index
  self.bstack111ll1ll11_opy_ = bstack1l1lll11l1_opy_
  bstack1l1l111ll1_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1lll1l111l_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack1ll1ll1ll_opy_
  global bstack1llll1l111_opy_
  bstack1lllll11ll_opy_ = copy.deepcopy(item)
  if not bstack1lll11l_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪ൵") in item.options:
    bstack1lllll11ll_opy_.options[bstack1lll11l_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ൶")] = []
  bstack11llllll11_opy_ = bstack1lllll11ll_opy_.options[bstack1lll11l_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬ൷")].copy()
  for v in bstack1lllll11ll_opy_.options[bstack1lll11l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭൸")]:
    if bstack1lll11l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡕࡒࡁࡕࡈࡒࡖࡒࡏࡎࡅࡇ࡛ࠫ൹") in v:
      bstack11llllll11_opy_.remove(v)
    if bstack1lll11l_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡉࡌࡊࡃࡕࡋࡘ࠭ൺ") in v:
      bstack11llllll11_opy_.remove(v)
    if bstack1lll11l_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡄࡆࡈࡏࡓࡈࡇࡌࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠫൻ") in v:
      bstack11llllll11_opy_.remove(v)
  bstack11llllll11_opy_.insert(0, bstack1lll11l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞࠺ࡼࡿࠪർ").format(bstack1lllll11ll_opy_.platform_index))
  bstack11llllll11_opy_.insert(0, bstack1lll11l_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࡀࡻࡾࠩൽ").format(bstack1lllll11ll_opy_.bstack111ll1ll11_opy_))
  bstack1lllll11ll_opy_.options[bstack1lll11l_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬൾ")] = bstack11llllll11_opy_
  if bstack1llll1l111_opy_:
    bstack1lllll11ll_opy_.options[bstack1lll11l_opy_ (u"ࠫࡻࡧࡲࡪࡣࡥࡰࡪ࠭ൿ")].insert(0, bstack1lll11l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗ࠿ࢁࡽࠨ඀").format(bstack1llll1l111_opy_))
  return bstack1ll1ll1ll_opy_(caller_id, datasources, is_last, bstack1lllll11ll_opy_, outs_dir)
def bstack1llllll1ll_opy_(command, item_index):
  try:
    if bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧඁ")):
      os.environ[bstack1lll11l_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨං")] = json.dumps(CONFIG[bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫඃ")][item_index % bstack1lllllll11_opy_])
    global bstack1llll1l111_opy_
    if bstack1llll1l111_opy_:
      command[0] = command[0].replace(bstack1lll11l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ඄"), bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠯ࡶࡨࡰࠦࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠠ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡࡳࡰࡦࡺࡦࡰࡴࡰࡣ࡮ࡴࡤࡦࡺࠣࠫඅ") + str(item_index % bstack1lllllll11_opy_) + bstack1lll11l_opy_ (u"ࠫࠥ࠳࠭ࡣࡵࡷࡥࡨࡱ࡟ࡪࡶࡨࡱࡤ࡯࡮ࡥࡧࡻࠤࠬආ") + str(
        item_index) + bstack1lll11l_opy_ (u"ࠬࠦࠧඇ") + bstack1llll1l111_opy_, 1)
    else:
      command[0] = command[0].replace(bstack1lll11l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬඈ"),
                                      bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠳ࡳࡥ࡭ࠣࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨඉ") +  str(item_index % bstack1lllllll11_opy_) + bstack1lll11l_opy_ (u"ࠨࠢ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣ࡮ࡺࡥ࡮ࡡ࡬ࡲࡩ࡫ࡸࠡࠩඊ") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack1lll11l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡯ࡲࡨ࡮࡬ࡹࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࠥ࡬࡯ࡳࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲ࠿ࠦࡻࡾࠩඋ").format(str(e)))
def bstack1l11l11ll1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack111l11111l_opy_
  try:
    bstack1llllll1ll_opy_(command, item_index)
    return bstack111l11111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack1lll11l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮࠻ࠢࡾࢁࠬඌ").format(str(e)))
    raise e
def bstack11lllll1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack111l11111l_opy_
  try:
    bstack1llllll1ll_opy_(command, item_index)
    return bstack111l11111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack1lll11l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠵࠲࠶࠹࠺ࠡࡽࢀࠫඍ").format(str(e)))
    try:
      return bstack111l11111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack1lll11l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦ࠲࠯࠳࠶ࠤ࡫ࡧ࡬࡭ࡤࡤࡧࡰࡀࠠࡼࡿࠪඎ").format(str(e2)))
      raise e
def bstack111l1ll11l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack111l11111l_opy_
  try:
    bstack1llllll1ll_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack111l11111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack1lll11l_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱࠤ࠷࠴࠱࠶࠼ࠣࡿࢂ࠭ඏ").format(str(e)))
    try:
      return bstack111l11111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack1lll11l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡ࠴࠱࠵࠺ࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࡾࢁࠬඐ").format(str(e2)))
      raise e
def _11lllllll1_opy_(bstack11l1ll1lll_opy_, item_index, process_timeout, sleep_before_start, bstack1l111ll11l_opy_):
  bstack1llllll1ll_opy_(bstack11l1ll1lll_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack1llll111l1_opy_(command, bstack111ll1ll1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack111l11111l_opy_
  try:
    bstack1llllll1ll_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack111l11111l_opy_(command, bstack111ll1ll1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1lll11l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡵࡹࡳࠦ࠵࠯࠲࠽ࠤࢀࢃࠧඑ").format(str(e)))
    try:
      return bstack111l11111l_opy_(command, bstack111ll1ll1_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1lll11l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩඒ").format(str(e2)))
      raise e
def bstack1llllll111_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack111l11111l_opy_
  try:
    process_timeout = _11lllllll1_opy_(command, item_index, process_timeout, sleep_before_start, bstack1lll11l_opy_ (u"ࠪ࠸࠳࠸ࠧඓ"))
    return bstack111l11111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack1lll11l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥࡸࡵ࡯ࠢ࠷࠲࠷ࡀࠠࡼࡿࠪඔ").format(str(e)))
    try:
      return bstack111l11111l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack1lll11l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡦࡢ࡮࡯ࡦࡦࡩ࡫࠻ࠢࡾࢁࠬඕ").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack1ll1ll1l1l_opy_(self, runner, quiet=False, capture=True):
  global bstack11l111111l_opy_
  bstack1l1l1l111l_opy_ = bstack11l111111l_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack1lll11l_opy_ (u"࠭ࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࡡࡤࡶࡷ࠭ඖ")):
      runner.exception_arr = []
    if not hasattr(runner, bstack1lll11l_opy_ (u"ࠧࡦࡺࡦࡣࡹࡸࡡࡤࡧࡥࡥࡨࡱ࡟ࡢࡴࡵࠫ඗")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack1l1l1l111l_opy_
def bstack1ll11111l_opy_(runner, hook_name, context, element, bstack111l111lll_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack111ll1l11l_opy_.bstack11l1lll1_opy_(hook_name, element)
    bstack111l111lll_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack111ll1l11l_opy_.bstack11l11l11_opy_(element)
      if hook_name not in [bstack1lll11l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠬ඘"), bstack1lll11l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡣ࡯ࡰࠬ඙")] and args and hasattr(args[0], bstack1lll11l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࡡࡰࡩࡸࡹࡡࡨࡧࠪක")):
        args[0].error_message = bstack1lll11l_opy_ (u"ࠫࠬඛ")
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡪࡤࡲࡩࡲࡥࠡࡪࡲࡳࡰࡹࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧ࠽ࠤࢀࢃࠧග").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1l1l111_opy_, stage=STAGE.bstack1ll1l1l11_opy_, hook_type=bstack1lll11l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡇ࡬࡭ࠤඝ"), bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1l1111l11l_opy_(runner, name, context, bstack111l111lll_opy_, *args):
    if runner.hooks.get(bstack1lll11l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠦඞ")).__name__ != bstack1lll11l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࡤࡪࡥࡧࡣࡸࡰࡹࡥࡨࡰࡱ࡮ࠦඟ"):
      bstack1ll11111l_opy_(runner, name, context, runner, bstack111l111lll_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1l11111l1l_opy_(bstack1lll11l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨච")) else context.browser
      runner.driver_initialised = bstack1lll11l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢඡ")
    except Exception as e:
      logger.debug(bstack1lll11l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡩࡸࡩࡷࡧࡵࠤ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࡹࡥࠡࡣࡷࡸࡷ࡯ࡢࡶࡶࡨ࠾ࠥࢁࡽࠨජ").format(str(e)))
def bstack1l1l1lll1_opy_(runner, name, context, bstack111l111lll_opy_, *args):
    bstack1ll11111l_opy_(runner, name, context, context.feature, bstack111l111lll_opy_, *args)
    try:
      if not bstack1lll11lll1_opy_:
        bstack1111l11111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l11111l1l_opy_(bstack1lll11l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫඣ")) else context.browser
        if is_driver_active(bstack1111l11111_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack1lll11l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡦࡦࡣࡷࡹࡷ࡫ࠢඤ")
          bstack1ll1l11l11_opy_ = str(runner.feature.name)
          bstack1l11l1ll11_opy_(context, bstack1ll1l11l11_opy_)
          bstack1111l11111_opy_.execute_script(bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡳࡧ࡭ࡦࠤ࠽ࠤࠬඥ") + json.dumps(bstack1ll1l11l11_opy_) + bstack1lll11l_opy_ (u"ࠨࡿࢀࠫඦ"))
    except Exception as e:
      logger.debug(bstack1lll11l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡥࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡ࡫ࡱࠤࡧ࡫ࡦࡰࡴࡨࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩට").format(str(e)))
def bstack11ll1llll_opy_(runner, name, context, bstack111l111lll_opy_, *args):
    if hasattr(context, bstack1lll11l_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬඨ")):
        bstack111ll1l11l_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack1lll11l_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ඩ")) else context.feature
    bstack1ll11111l_opy_(runner, name, context, target, bstack111l111lll_opy_, *args)
@measure(event_name=EVENTS.bstack1l1l1ll11l_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack11l1l1l11_opy_(runner, name, context, bstack111l111lll_opy_, *args):
    if len(context.scenario.tags) == 0: bstack111ll1l11l_opy_.start_test(context)
    bstack1ll11111l_opy_(runner, name, context, context.scenario, bstack111l111lll_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack11111lllll_opy_.bstack1l1111ll1l_opy_(context, *args)
    try:
      bstack1111l11111_opy_ = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫඪ"), context.browser)
      if is_driver_active(bstack1111l11111_opy_):
        bstack1l111l1l_opy_.bstack1ll11l1ll1_opy_(bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬණ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack1lll11l_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡥࡨࡲࡦࡸࡩࡰࠤඬ")
        if (not bstack1lll11lll1_opy_):
          scenario_name = args[0].name
          feature_name = bstack1ll1l11l11_opy_ = str(runner.feature.name)
          bstack1ll1l11l11_opy_ = feature_name + bstack1lll11l_opy_ (u"ࠨࠢ࠰ࠤࠬත") + scenario_name
          if runner.driver_initialised == bstack1lll11l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲࠦථ"):
            bstack1l11l1ll11_opy_(context, bstack1ll1l11l11_opy_)
            bstack1111l11111_opy_.execute_script(bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨද") + json.dumps(bstack1ll1l11l11_opy_) + bstack1lll11l_opy_ (u"ࠫࢂࢃࠧධ"))
    except Exception as e:
      logger.debug(bstack1lll11l_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰ࠼ࠣࡿࢂ࠭න").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1l1l111_opy_, stage=STAGE.bstack1ll1l1l11_opy_, hook_type=bstack1lll11l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪ࡙ࡴࡦࡲࠥ඲"), bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1111l1111l_opy_(runner, name, context, bstack111l111lll_opy_, *args):
    bstack1ll11111l_opy_(runner, name, context, args[0], bstack111l111lll_opy_, *args)
    try:
      bstack1111l11111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l11111l1l_opy_(bstack1lll11l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ඳ")) else context.browser
      if is_driver_active(bstack1111l11111_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack1lll11l_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨප")
        bstack111ll1l11l_opy_.bstack11l1l1ll_opy_(args[0])
        if runner.driver_initialised == bstack1lll11l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢඵ"):
          feature_name = bstack1ll1l11l11_opy_ = str(runner.feature.name)
          bstack1ll1l11l11_opy_ = feature_name + bstack1lll11l_opy_ (u"ࠪࠤ࠲ࠦࠧබ") + context.scenario.name
          bstack1111l11111_opy_.execute_script(bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩභ") + json.dumps(bstack1ll1l11l11_opy_) + bstack1lll11l_opy_ (u"ࠬࢃࡽࠨම"))
    except Exception as e:
      logger.debug(bstack1lll11l_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳࡦࡵࡶ࡭ࡴࡴࠠ࡯ࡣࡰࡩࠥ࡯࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡷࡩࡵࡀࠠࡼࡿࠪඹ").format(str(e)))
@measure(event_name=EVENTS.bstack1ll1l1l111_opy_, stage=STAGE.bstack1ll1l1l11_opy_, hook_type=bstack1lll11l_opy_ (u"ࠢࡢࡨࡷࡩࡷ࡙ࡴࡦࡲࠥය"), bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1ll111l11l_opy_(runner, name, context, bstack111l111lll_opy_, *args):
  bstack111ll1l11l_opy_.bstack11l11l1l_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack1111l11111_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll11l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧර") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1111l11111_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack1lll11l_opy_ (u"ࠩ࡬ࡲࡸࡺࡥࡱࠩ඼")
        feature_name = bstack1ll1l11l11_opy_ = str(runner.feature.name)
        bstack1ll1l11l11_opy_ = feature_name + bstack1lll11l_opy_ (u"ࠪࠤ࠲ࠦࠧල") + context.scenario.name
        bstack1111l11111_opy_.execute_script(bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠡࠩ඾") + json.dumps(bstack1ll1l11l11_opy_) + bstack1lll11l_opy_ (u"ࠬࢃࡽࠨ඿"))
    if str(step_status).lower() == bstack1lll11l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ව"):
      bstack1l11lll1l1_opy_ = bstack1lll11l_opy_ (u"ࠧࠨශ")
      bstack1l1ll1ll11_opy_ = bstack1lll11l_opy_ (u"ࠨࠩෂ")
      bstack11l11111l1_opy_ = bstack1lll11l_opy_ (u"ࠩࠪස")
      try:
        import traceback
        bstack1l11lll1l1_opy_ = runner.exception.__class__.__name__
        bstack11l1l1l1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1l1ll1ll11_opy_ = bstack1lll11l_opy_ (u"ࠪࠤࠬහ").join(bstack11l1l1l1_opy_)
        bstack11l11111l1_opy_ = bstack11l1l1l1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1ll1l11111_opy_.format(str(e)))
      bstack1l11lll1l1_opy_ += bstack11l11111l1_opy_
      bstack1l1ll11ll_opy_(context, json.dumps(str(args[0].name) + bstack1lll11l_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥළ") + str(bstack1l1ll1ll11_opy_)),
                          bstack1lll11l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦෆ"))
      if runner.driver_initialised == bstack1lll11l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡵࡧࡳࠦ෇"):
        bstack11ll1l1l1l_opy_(getattr(context, bstack1lll11l_opy_ (u"ࠧࡱࡣࡪࡩࠬ෈"), None), bstack1lll11l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ෉"), bstack1l11lll1l1_opy_)
        bstack1111l11111_opy_.execute_script(bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀ්ࠧ") + json.dumps(str(args[0].name) + bstack1lll11l_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ෋") + str(bstack1l1ll1ll11_opy_)) + bstack1lll11l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫ෌"))
      if runner.driver_initialised == bstack1lll11l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥ෍"):
        bstack1l1ll1l11l_opy_(bstack1111l11111_opy_, bstack1lll11l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭෎"), bstack1lll11l_opy_ (u"ࠢࡔࡥࡨࡲࡦࡸࡩࡰࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦා") + str(bstack1l11lll1l1_opy_))
    else:
      bstack1l1ll11ll_opy_(context, bstack1lll11l_opy_ (u"ࠣࡒࡤࡷࡸ࡫ࡤࠢࠤැ"), bstack1lll11l_opy_ (u"ࠤ࡬ࡲ࡫ࡵࠢෑ"))
      if runner.driver_initialised == bstack1lll11l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠣි"):
        bstack11ll1l1l1l_opy_(getattr(context, bstack1lll11l_opy_ (u"ࠫࡵࡧࡧࡦࠩී"), None), bstack1lll11l_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧු"))
      bstack1111l11111_opy_.execute_script(bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫ෕") + json.dumps(str(args[0].name) + bstack1lll11l_opy_ (u"ࠢࠡ࠯ࠣࡔࡦࡹࡳࡦࡦࠤࠦූ")) + bstack1lll11l_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡩ࡯ࡨࡲࠦࢂࢃࠧ෗"))
      if runner.driver_initialised == bstack1lll11l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢෘ"):
        bstack1l1ll1l11l_opy_(bstack1111l11111_opy_, bstack1lll11l_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥෙ"))
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠ࡮ࡣࡵ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡳࡵࡣࡷࡹࡸࠦࡩ࡯ࠢࡤࡪࡹ࡫ࡲࠡࡵࡷࡩࡵࡀࠠࡼࡿࠪේ").format(str(e)))
  bstack1ll11111l_opy_(runner, name, context, args[0], bstack111l111lll_opy_, *args)
@measure(event_name=EVENTS.bstack1ll11l1l1l_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack11l111l1ll_opy_(runner, name, context, bstack111l111lll_opy_, *args):
  bstack111ll1l11l_opy_.end_test(args[0])
  try:
    bstack11l1l111l1_opy_ = args[0].status.name
    bstack1111l11111_opy_ = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫෛ"), context.browser)
    bstack11111lllll_opy_.bstack11ll1ll1l1_opy_(bstack1111l11111_opy_)
    if str(bstack11l1l111l1_opy_).lower() == bstack1lll11l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ො"):
      bstack1l11lll1l1_opy_ = bstack1lll11l_opy_ (u"ࠧࠨෝ")
      bstack1l1ll1ll11_opy_ = bstack1lll11l_opy_ (u"ࠨࠩෞ")
      bstack11l11111l1_opy_ = bstack1lll11l_opy_ (u"ࠩࠪෟ")
      try:
        import traceback
        bstack1l11lll1l1_opy_ = runner.exception.__class__.__name__
        bstack11l1l1l1_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack1l1ll1ll11_opy_ = bstack1lll11l_opy_ (u"ࠪࠤࠬ෠").join(bstack11l1l1l1_opy_)
        bstack11l11111l1_opy_ = bstack11l1l1l1_opy_[-1]
      except Exception as e:
        logger.debug(bstack1ll1l11111_opy_.format(str(e)))
      bstack1l11lll1l1_opy_ += bstack11l11111l1_opy_
      bstack1l1ll11ll_opy_(context, json.dumps(str(args[0].name) + bstack1lll11l_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥ෡") + str(bstack1l1ll1ll11_opy_)),
                          bstack1lll11l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦ෢"))
      if runner.driver_initialised == bstack1lll11l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣ෣") or runner.driver_initialised == bstack1lll11l_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧ෤"):
        bstack11ll1l1l1l_opy_(getattr(context, bstack1lll11l_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭෥"), None), bstack1lll11l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤ෦"), bstack1l11lll1l1_opy_)
        bstack1111l11111_opy_.execute_script(bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ෧") + json.dumps(str(args[0].name) + bstack1lll11l_opy_ (u"ࠦࠥ࠳ࠠࡇࡣ࡬ࡰࡪࡪࠡ࡝ࡰࠥ෨") + str(bstack1l1ll1ll11_opy_)) + bstack1lll11l_opy_ (u"ࠬ࠲ࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥࡩࡷࡸ࡯ࡳࠤࢀࢁࠬ෩"))
      if runner.driver_initialised == bstack1lll11l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣ෪") or runner.driver_initialised == bstack1lll11l_opy_ (u"ࠧࡪࡰࡶࡸࡪࡶࠧ෫"):
        bstack1l1ll1l11l_opy_(bstack1111l11111_opy_, bstack1lll11l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ෬"), bstack1lll11l_opy_ (u"ࠤࡖࡧࡪࡴࡡࡳ࡫ࡲࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡼ࡯ࡴࡩ࠼ࠣࡠࡳࠨ෭") + str(bstack1l11lll1l1_opy_))
    else:
      bstack1l1ll11ll_opy_(context, bstack1lll11l_opy_ (u"ࠥࡔࡦࡹࡳࡦࡦࠤࠦ෮"), bstack1lll11l_opy_ (u"ࠦ࡮ࡴࡦࡰࠤ෯"))
      if runner.driver_initialised == bstack1lll11l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ෰") or runner.driver_initialised == bstack1lll11l_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෱"):
        bstack11ll1l1l1l_opy_(getattr(context, bstack1lll11l_opy_ (u"ࠧࡱࡣࡪࡩࠬෲ"), None), bstack1lll11l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣෳ"))
      bstack1111l11111_opy_.execute_script(bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧ෴") + json.dumps(str(args[0].name) + bstack1lll11l_opy_ (u"ࠥࠤ࠲ࠦࡐࡢࡵࡶࡩࡩࠧࠢ෵")) + bstack1lll11l_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤ࡬ࡲ࡫ࡵࠢࡾࡿࠪ෶"))
      if runner.driver_initialised == bstack1lll11l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ෷") or runner.driver_initialised == bstack1lll11l_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෸"):
        bstack1l1ll1l11l_opy_(bstack1111l11111_opy_, bstack1lll11l_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢ෹"))
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪ෺").format(str(e)))
  bstack1ll11111l_opy_(runner, name, context, context.scenario, bstack111l111lll_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack111l1l1ll1_opy_(runner, name, context, bstack111l111lll_opy_, *args):
    target = context.scenario if hasattr(context, bstack1lll11l_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫ෻")) else context.feature
    bstack1ll11111l_opy_(runner, name, context, target, bstack111l111lll_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack11l111111_opy_(runner, name, context, bstack111l111lll_opy_, *args):
    try:
      bstack1111l11111_opy_ = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡖࡩࡸࡹࡩࡰࡰࡇࡶ࡮ࡼࡥࡳࠩ෼"), context.browser)
      bstack11ll1lll11_opy_ = bstack1lll11l_opy_ (u"ࠫࠬ෽")
      if context.failed is True:
        bstack11llllll1l_opy_ = []
        bstack11l111lll_opy_ = []
        bstack11111l1ll1_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack11llllll1l_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l1l1l1_opy_ = traceback.format_tb(exc_tb)
            bstack1111l11l11_opy_ = bstack1lll11l_opy_ (u"ࠬࠦࠧ෾").join(bstack11l1l1l1_opy_)
            bstack11l111lll_opy_.append(bstack1111l11l11_opy_)
            bstack11111l1ll1_opy_.append(bstack11l1l1l1_opy_[-1])
        except Exception as e:
          logger.debug(bstack1ll1l11111_opy_.format(str(e)))
        bstack1l11lll1l1_opy_ = bstack1lll11l_opy_ (u"࠭ࠧ෿")
        for i in range(len(bstack11llllll1l_opy_)):
          bstack1l11lll1l1_opy_ += bstack11llllll1l_opy_[i] + bstack11111l1ll1_opy_[i] + bstack1lll11l_opy_ (u"ࠧ࡝ࡰࠪ฀")
        bstack11ll1lll11_opy_ = bstack1lll11l_opy_ (u"ࠨࠢࠪก").join(bstack11l111lll_opy_)
        if runner.driver_initialised in [bstack1lll11l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡩࡩࡦࡺࡵࡳࡧࠥข"), bstack1lll11l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡥࡱࡲࠢฃ")]:
          bstack1l1ll11ll_opy_(context, bstack11ll1lll11_opy_, bstack1lll11l_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥค"))
          bstack11ll1l1l1l_opy_(getattr(context, bstack1lll11l_opy_ (u"ࠬࡶࡡࡨࡧࠪฅ"), None), bstack1lll11l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨฆ"), bstack1l11lll1l1_opy_)
          bstack1111l11111_opy_.execute_script(bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࠦࡦࡩࡴࡪࡱࡱࠦ࠿ࠦࠢࡢࡰࡱࡳࡹࡧࡴࡦࠤ࠯ࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࠧࡪࡡࡵࡣࠥ࠾ࠬง") + json.dumps(bstack11ll1lll11_opy_) + bstack1lll11l_opy_ (u"ࠨ࠮ࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧࢃࡽࠨจ"))
          bstack1l1ll1l11l_opy_(bstack1111l11111_opy_, bstack1lll11l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࠤฉ"), bstack1lll11l_opy_ (u"ࠥࡗࡴࡳࡥࠡࡵࡦࡩࡳࡧࡲࡪࡱࡶࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࡢ࡮ࠣช") + str(bstack1l11lll1l1_opy_))
          bstack111lll111l_opy_ = bstack111lll1l1_opy_(bstack11ll1lll11_opy_, runner.feature.name, logger)
          if (bstack111lll111l_opy_ != None):
            bstack1l1l1l1ll1_opy_.append(bstack111lll111l_opy_)
      else:
        if runner.driver_initialised in [bstack1lll11l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧซ"), bstack1lll11l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡧ࡬࡭ࠤฌ")]:
          bstack1l1ll11ll_opy_(context, bstack1lll11l_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫࠺ࠡࠤญ") + str(runner.feature.name) + bstack1lll11l_opy_ (u"ࠢࠡࡲࡤࡷࡸ࡫ࡤࠢࠤฎ"), bstack1lll11l_opy_ (u"ࠣ࡫ࡱࡪࡴࠨฏ"))
          bstack11ll1l1l1l_opy_(getattr(context, bstack1lll11l_opy_ (u"ࠩࡳࡥ࡬࡫ࠧฐ"), None), bstack1lll11l_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥฑ"))
          bstack1111l11111_opy_.execute_script(bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡦࡴ࡮ࡰࡶࡤࡸࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡧࡥࡹࡧࠢ࠻ࠩฒ") + json.dumps(bstack1lll11l_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣณ") + str(runner.feature.name) + bstack1lll11l_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣด")) + bstack1lll11l_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭ต"))
          bstack1l1ll1l11l_opy_(bstack1111l11111_opy_, bstack1lll11l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨถ"))
          bstack111lll111l_opy_ = bstack111lll1l1_opy_(bstack11ll1lll11_opy_, runner.feature.name, logger)
          if (bstack111lll111l_opy_ != None):
            bstack1l1l1l1ll1_opy_.append(bstack111lll111l_opy_)
    except Exception as e:
      logger.debug(bstack1lll11l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡦࡦࡣࡷࡹࡷ࡫࠺ࠡࡽࢀࠫท").format(str(e)))
    bstack1ll11111l_opy_(runner, name, context, context.feature, bstack111l111lll_opy_, *args)
@measure(event_name=EVENTS.bstack1ll1l1l111_opy_, stage=STAGE.bstack1ll1l1l11_opy_, hook_type=bstack1lll11l_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࡃ࡯ࡰࠧธ"), bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1l11ll11l1_opy_(runner, name, context, bstack111l111lll_opy_, *args):
    bstack1ll11111l_opy_(runner, name, context, runner, bstack111l111lll_opy_, *args)
def bstack11l1lll11_opy_(self, name, context, *args):
  try:
    if bstack111ll1llll_opy_:
      platform_index = int(threading.current_thread()._name) % bstack1lllllll11_opy_
      bstack1l11ll111l_opy_ = CONFIG[bstack1lll11l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧน")][platform_index]
      os.environ[bstack1lll11l_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭บ")] = json.dumps(bstack1l11ll111l_opy_)
    global bstack111l111lll_opy_
    if not hasattr(self, bstack1lll11l_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷࡥࡩ࡯࡫ࡷ࡭ࡦࡲࡩࡴࡧࡧࠫป")):
      self.driver_initialised = None
    bstack111111llll_opy_ = {
        bstack1lll11l_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫผ"): bstack1l1111l11l_opy_,
        bstack1lll11l_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠩฝ"): bstack1l1l1lll1_opy_,
        bstack1lll11l_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡷࡥ࡬࠭พ"): bstack11ll1llll_opy_,
        bstack1lll11l_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬฟ"): bstack11l1l1l11_opy_,
        bstack1lll11l_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠩภ"): bstack1111l1111l_opy_,
        bstack1lll11l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡺࡥࡱࠩม"): bstack1ll111l11l_opy_,
        bstack1lll11l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠧย"): bstack11l111l1ll_opy_,
        bstack1lll11l_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡴࡢࡩࠪร"): bstack111l1l1ll1_opy_,
        bstack1lll11l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡧࡧࡤࡸࡺࡸࡥࠨฤ"): bstack11l111111_opy_,
        bstack1lll11l_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡣ࡯ࡰࠬล"): bstack1l11ll11l1_opy_
    }
    handler = bstack111111llll_opy_.get(name, bstack111l111lll_opy_)
    try:
      handler(self, name, context, bstack111l111lll_opy_, *args)
    except Exception as e:
      logger.debug(bstack1lll11l_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩࠥ࡮࡯ࡰ࡭ࠣ࡬ࡦࡴࡤ࡭ࡧࡵࠤࢀࢃ࠺ࠡࡽࢀࠫฦ").format(name, str(e)))
    if name in [bstack1lll11l_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡪࡪࡧࡴࡶࡴࡨࠫว"), bstack1lll11l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ศ"), bstack1lll11l_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡧ࡬࡭ࠩษ")]:
      try:
        bstack1111l11111_opy_ = threading.current_thread().bstackSessionDriver if bstack1l11111l1l_opy_(bstack1lll11l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ส")) else context.browser
        bstack1ll111lll_opy_ = (
          (name == bstack1lll11l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫห") and self.driver_initialised == bstack1lll11l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨฬ")) or
          (name == bstack1lll11l_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪอ") and self.driver_initialised == bstack1lll11l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣ࡫࡫ࡡࡵࡷࡵࡩࠧฮ")) or
          (name == bstack1lll11l_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ฯ") and self.driver_initialised in [bstack1lll11l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣะ"), bstack1lll11l_opy_ (u"ࠢࡪࡰࡶࡸࡪࡶࠢั")]) or
          (name == bstack1lll11l_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡴࡶࡨࡴࠬา") and self.driver_initialised == bstack1lll11l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢำ"))
        )
        if bstack1ll111lll_opy_:
          self.driver_initialised = None
          if bstack1111l11111_opy_ and hasattr(bstack1111l11111_opy_, bstack1lll11l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧิ")):
            try:
              bstack1111l11111_opy_.quit()
            except Exception as e:
              logger.debug(bstack1lll11l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡵࡺ࡯ࡴࡵ࡫ࡱ࡫ࠥࡪࡲࡪࡸࡨࡶࠥ࡯࡮ࠡࡤࡨ࡬ࡦࡼࡥࠡࡪࡲࡳࡰࡀࠠࡼࡿࠪี").format(str(e)))
      except Exception as e:
        logger.debug(bstack1lll11l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡢࡨࡷࡩࡷࠦࡨࡰࡱ࡮ࠤࡨࡲࡥࡢࡰࡸࡴࠥ࡬࡯ࡳࠢࡾࢁ࠿ࠦࡻࡾࠩึ").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"࠭ࡃࡳ࡫ࡷ࡭ࡨࡧ࡬ࠡࡧࡵࡶࡴࡸࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧࠣࡶࡺࡴࠠࡩࡱࡲ࡯ࠥࢁࡽ࠻ࠢࡾࢁࠬื").format(name, str(e)))
    try:
      bstack111l111lll_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack1lll11l_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡩࡥࡱࡲࡢࡢࡥ࡮ࠤࡴࡸࡩࡨ࡫ࡱࡥࡱࠦࡢࡦࡪࡤࡺࡪࠦࡨࡰࡱ࡮ࠤࢀࢃ࠺ࠡࡽࢀุࠫ").format(name, str(e2)))
def bstack1ll1111l1l_opy_(config, startdir):
  return bstack1lll11l_opy_ (u"ࠣࡦࡵ࡭ࡻ࡫ࡲ࠻ࠢࡾ࠴ࢂࠨู").format(bstack1lll11l_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ฺࠣ"))
notset = Notset()
def bstack1l11111l11_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack1ll111l11_opy_
  if str(name).lower() == bstack1lll11l_opy_ (u"ࠪࡨࡷ࡯ࡶࡦࡴࠪ฻"):
    return bstack1lll11l_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠥ฼")
  else:
    return bstack1ll111l11_opy_(self, name, default, skip)
def bstack1ll111ll1_opy_(item, when):
  global bstack1llll11lll_opy_
  try:
    bstack1llll11lll_opy_(item, when)
  except Exception as e:
    pass
def bstack1l111111ll_opy_():
  return
def bstack111111ll11_opy_(type, name, status, reason, bstack1l11ll1l11_opy_, bstack111l11l11_opy_):
  bstack11111ll11l_opy_ = {
    bstack1lll11l_opy_ (u"ࠬࡧࡣࡵ࡫ࡲࡲࠬ฽"): type,
    bstack1lll11l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ฾"): {}
  }
  if type == bstack1lll11l_opy_ (u"ࠧࡢࡰࡱࡳࡹࡧࡴࡦࠩ฿"):
    bstack11111ll11l_opy_[bstack1lll11l_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫเ")][bstack1lll11l_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨแ")] = bstack1l11ll1l11_opy_
    bstack11111ll11l_opy_[bstack1lll11l_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭โ")][bstack1lll11l_opy_ (u"ࠫࡩࡧࡴࡢࠩใ")] = json.dumps(str(bstack111l11l11_opy_))
  if type == bstack1lll11l_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭ไ"):
    bstack11111ll11l_opy_[bstack1lll11l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩๅ")][bstack1lll11l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬๆ")] = name
  if type == bstack1lll11l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠫ็"):
    bstack11111ll11l_opy_[bstack1lll11l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷ่ࠬ")][bstack1lll11l_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵ้ࠪ")] = status
    if status == bstack1lll11l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧ๊ࠫ"):
      bstack11111ll11l_opy_[bstack1lll11l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ๋")][bstack1lll11l_opy_ (u"࠭ࡲࡦࡣࡶࡳࡳ࠭์")] = json.dumps(str(reason))
  bstack1l1111l1l_opy_ = bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࢁࠬํ").format(json.dumps(bstack11111ll11l_opy_))
  return bstack1l1111l1l_opy_
def bstack1llll1l1ll_opy_(driver_command, response):
    if driver_command == bstack1lll11l_opy_ (u"ࠨࡵࡦࡶࡪ࡫࡮ࡴࡪࡲࡸࠬ๎"):
        bstack1l111l1l_opy_.bstack1ll111lll1_opy_({
            bstack1lll11l_opy_ (u"ࠩ࡬ࡱࡦ࡭ࡥࠨ๏"): response[bstack1lll11l_opy_ (u"ࠪࡺࡦࡲࡵࡦࠩ๐")],
            bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫ๑"): bstack1l111l1l_opy_.current_test_uuid()
        })
def bstack1l11l11l1_opy_(item, call, rep):
  global bstack1lll11111_opy_
  global bstack1l1lll1ll_opy_
  global bstack1lll11lll1_opy_
  name = bstack1lll11l_opy_ (u"ࠬ࠭๒")
  try:
    if rep.when == bstack1lll11l_opy_ (u"࠭ࡣࡢ࡮࡯ࠫ๓"):
      bstack1l11l1l1ll_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack1lll11lll1_opy_:
          name = str(rep.nodeid)
          bstack1l111l1ll1_opy_ = bstack111111ll11_opy_(bstack1lll11l_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨ๔"), name, bstack1lll11l_opy_ (u"ࠨࠩ๕"), bstack1lll11l_opy_ (u"ࠩࠪ๖"), bstack1lll11l_opy_ (u"ࠪࠫ๗"), bstack1lll11l_opy_ (u"ࠫࠬ๘"))
          threading.current_thread().bstack1l11ll1ll_opy_ = name
          for driver in bstack1l1lll1ll_opy_:
            if bstack1l11l1l1ll_opy_ == driver.session_id:
              driver.execute_script(bstack1l111l1ll1_opy_)
      except Exception as e:
        logger.debug(bstack1lll11l_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ๙").format(str(e)))
      try:
        bstack1ll1l1ll11_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack1lll11l_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ๚"):
          status = bstack1lll11l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ๛") if rep.outcome.lower() == bstack1lll11l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ๜") else bstack1lll11l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ๝")
          reason = bstack1lll11l_opy_ (u"ࠪࠫ๞")
          if status == bstack1lll11l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ๟"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack1lll11l_opy_ (u"ࠬ࡯࡮ࡧࡱࠪ๠") if status == bstack1lll11l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭๡") else bstack1lll11l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭๢")
          data = name + bstack1lll11l_opy_ (u"ࠨࠢࡳࡥࡸࡹࡥࡥࠣࠪ๣") if status == bstack1lll11l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ๤") else name + bstack1lll11l_opy_ (u"ࠪࠤ࡫ࡧࡩ࡭ࡧࡧࠥࠥ࠭๥") + reason
          bstack1l1ll111l_opy_ = bstack111111ll11_opy_(bstack1lll11l_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭๦"), bstack1lll11l_opy_ (u"ࠬ࠭๧"), bstack1lll11l_opy_ (u"࠭ࠧ๨"), bstack1lll11l_opy_ (u"ࠧࠨ๩"), level, data)
          for driver in bstack1l1lll1ll_opy_:
            if bstack1l11l1l1ll_opy_ == driver.session_id:
              driver.execute_script(bstack1l1ll111l_opy_)
      except Exception as e:
        logger.debug(bstack1lll11l_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡷࡪࡺࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡩ࡯࡯ࡶࡨࡼࡹࠦࡦࡰࡴࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡴࡧࡶࡷ࡮ࡵ࡮࠻ࠢࡾࢁࠬ๪").format(str(e)))
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡴࡢࡶࡨࠤ࡮ࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࠢࡶࡸࡦࡺࡵࡴ࠼ࠣࡿࢂ࠭๫").format(str(e)))
  bstack1lll11111_opy_(item, call, rep)
def bstack11ll111l11_opy_(driver, bstack11111ll1ll_opy_, test=None):
  global bstack11ll11ll1l_opy_
  if test != None:
    bstack1ll111111l_opy_ = getattr(test, bstack1lll11l_opy_ (u"ࠪࡲࡦࡳࡥࠨ๬"), None)
    bstack11l1llll1l_opy_ = getattr(test, bstack1lll11l_opy_ (u"ࠫࡺࡻࡩࡥࠩ๭"), None)
    PercySDK.screenshot(driver, bstack11111ll1ll_opy_, bstack1ll111111l_opy_=bstack1ll111111l_opy_, bstack11l1llll1l_opy_=bstack11l1llll1l_opy_, bstack111l1lll1l_opy_=bstack11ll11ll1l_opy_)
  else:
    PercySDK.screenshot(driver, bstack11111ll1ll_opy_)
@measure(event_name=EVENTS.bstack1l1l11l11l_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1111l1l1l_opy_(driver):
  if bstack1ll11lll1l_opy_.bstack1ll11l11l1_opy_() is True or bstack1ll11lll1l_opy_.capturing() is True:
    return
  bstack1ll11lll1l_opy_.bstack1ll11l111l_opy_()
  while not bstack1ll11lll1l_opy_.bstack1ll11l11l1_opy_():
    bstack1l11l111ll_opy_ = bstack1ll11lll1l_opy_.bstack1lll1111l1_opy_()
    bstack11ll111l11_opy_(driver, bstack1l11l111ll_opy_)
  bstack1ll11lll1l_opy_.bstack11lll1l11l_opy_()
def bstack1l1lll1lll_opy_(sequence, driver_command, response = None, bstack11l1l11l1_opy_ = None, args = None):
    try:
      if sequence != bstack1lll11l_opy_ (u"ࠬࡨࡥࡧࡱࡵࡩࠬ๮"):
        return
      if percy.bstack1ll1111ll1_opy_() == bstack1lll11l_opy_ (u"ࠨࡦࡢ࡮ࡶࡩࠧ๯"):
        return
      bstack1l11l111ll_opy_ = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ๰"), None)
      for command in bstack1111ll11ll_opy_:
        if command == driver_command:
          with bstack1ll111l111_opy_:
            bstack1111l1l111_opy_ = bstack1l1lll1ll_opy_.copy()
          for driver in bstack1111l1l111_opy_:
            bstack1111l1l1l_opy_(driver)
      bstack1l1ll1l1l_opy_ = percy.bstack11lllll11_opy_()
      if driver_command in bstack11111l1lll_opy_[bstack1l1ll1l1l_opy_]:
        bstack1ll11lll1l_opy_.bstack1l11llll1_opy_(bstack1l11l111ll_opy_, driver_command)
    except Exception as e:
      pass
def bstack1ll1ll1111_opy_(framework_name):
  if bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬ๱")):
      return
  bstack111ll1l1_opy_.set_property(bstack1lll11l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡰࡳࡩࡥࡣࡢ࡮࡯ࡩࡩ࠭๲"), True)
  global bstack1l11l11ll_opy_
  global bstack1ll11llll_opy_
  global bstack1ll1111ll_opy_
  bstack1l11l11ll_opy_ = framework_name
  logger.info(bstack1l111ll111_opy_.format(bstack1l11l11ll_opy_.split(bstack1lll11l_opy_ (u"ࠪ࠱ࠬ๳"))[0]))
  bstack11ll1l11ll_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack111ll1llll_opy_:
      Service.start = bstack1l1l1llll_opy_
      Service.stop = bstack11111l1l11_opy_
      webdriver.Remote.get = bstack111l1111ll_opy_
      WebDriver.quit = bstack1111l111l1_opy_
      webdriver.Remote.__init__ = bstack1l1ll1llll_opy_
    if not bstack111ll1llll_opy_:
        webdriver.Remote.__init__ = bstack1lll1lll1l_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack11111l111l_opy_
    bstack1ll11llll_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack111ll1llll_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack11lll111l_opy_
  except Exception as e:
    pass
  bstack1l1l11l1ll_opy_()
  if not bstack1ll11llll_opy_:
    bstack1l111ll1l_opy_(bstack1lll11l_opy_ (u"ࠦࡕࡧࡣ࡬ࡣࡪࡩࡸࠦ࡮ࡰࡶࠣ࡭ࡳࡹࡴࡢ࡮࡯ࡩࡩࠨ๴"), bstack1l111l1l11_opy_)
  if bstack1l111l11ll_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack1lll11l_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭๵")) and callable(getattr(RemoteConnection, bstack1lll11l_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧ๶"))):
        RemoteConnection._get_proxy_url = bstack11l111l1l_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack11l111l1l_opy_
    except Exception as e:
      logger.error(bstack1llllll11l_opy_.format(str(e)))
  if bstack111llll11l_opy_():
    bstack111ll111l_opy_(CONFIG, logger)
  if (bstack1lll11l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭๷") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack1ll1111ll1_opy_() == bstack1lll11l_opy_ (u"ࠣࡶࡵࡹࡪࠨ๸"):
          bstack11ll1l111l_opy_(bstack1l1lll1lll_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack11l11lll1_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack1l1111l1l1_opy_
      except Exception as e:
        logger.warn(bstack1ll1111lll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack1lll1ll111_opy_
      except Exception as e:
        logger.debug(bstack1l111l111l_opy_ + str(e))
    except Exception as e:
      bstack1l111ll1l_opy_(e, bstack1ll1111lll_opy_)
    Output.start_test = bstack11ll1ll11_opy_
    Output.end_test = bstack111111l1ll_opy_
    TestStatus.__init__ = bstack111lll11l_opy_
    QueueItem.__init__ = bstack1ll11llll1_opy_
    pabot._create_items = bstack11llll1ll_opy_
    try:
      from pabot import __version__ as bstack1lll1l11l1_opy_
      if version.parse(bstack1lll1l11l1_opy_) >= version.parse(bstack1lll11l_opy_ (u"ࠩ࠸࠲࠵࠴࠰ࠨ๹")):
        pabot._run = bstack1llll111l1_opy_
      elif version.parse(bstack1lll1l11l1_opy_) >= version.parse(bstack1lll11l_opy_ (u"ࠪ࠸࠳࠸࠮࠱ࠩ๺")):
        pabot._run = bstack1llllll111_opy_
      elif version.parse(bstack1lll1l11l1_opy_) >= version.parse(bstack1lll11l_opy_ (u"ࠫ࠷࠴࠱࠶࠰࠳ࠫ๻")):
        pabot._run = bstack111l1ll11l_opy_
      elif version.parse(bstack1lll1l11l1_opy_) >= version.parse(bstack1lll11l_opy_ (u"ࠬ࠸࠮࠲࠵࠱࠴ࠬ๼")):
        pabot._run = bstack11lllll1l_opy_
      else:
        pabot._run = bstack1l11l11ll1_opy_
    except Exception as e:
      pabot._run = bstack1l11l11ll1_opy_
    pabot._create_command_for_execution = bstack1lll1l111l_opy_
    pabot._report_results = bstack11llllllll_opy_
  if bstack1lll11l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭๽") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l111ll1l_opy_(e, bstack1l1l1l111_opy_)
    Runner.run_hook = bstack11l1lll11_opy_
    Step.run = bstack1ll1ll1l1l_opy_
  if bstack1lll11l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ๾") in str(framework_name).lower():
    if not bstack111ll1llll_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack1ll1111l1l_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack1l111111ll_opy_
      Config.getoption = bstack1l11111l11_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1l11l11l1_opy_
    except Exception as e:
      pass
def bstack11ll11l1ll_opy_():
  global CONFIG
  if bstack1lll11l_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ๿") in CONFIG and int(CONFIG[bstack1lll11l_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ຀")]) > 1:
    logger.warn(bstack11l111l1l1_opy_)
def bstack1ll1lll11_opy_(arg, bstack1lllll1ll_opy_, bstack1ll1ll11ll_opy_=None):
  global CONFIG
  global bstack111l1llll_opy_
  global bstack11llllll1_opy_
  global bstack111ll1llll_opy_
  global bstack111ll1l1_opy_
  bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪກ")
  if bstack1lllll1ll_opy_ and isinstance(bstack1lllll1ll_opy_, str):
    bstack1lllll1ll_opy_ = eval(bstack1lllll1ll_opy_)
  CONFIG = bstack1lllll1ll_opy_[bstack1lll11l_opy_ (u"ࠫࡈࡕࡎࡇࡋࡊࠫຂ")]
  bstack111l1llll_opy_ = bstack1lllll1ll_opy_[bstack1lll11l_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭຃")]
  bstack11llllll1_opy_ = bstack1lllll1ll_opy_[bstack1lll11l_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨຄ")]
  bstack111ll1llll_opy_ = bstack1lllll1ll_opy_[bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪ຅")]
  bstack111ll1l1_opy_.set_property(bstack1lll11l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩຆ"), bstack111ll1llll_opy_)
  os.environ[bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫງ")] = bstack1l11l1lll1_opy_
  os.environ[bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࠩຈ")] = json.dumps(CONFIG)
  os.environ[bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡌ࡚ࡈ࡟ࡖࡔࡏࠫຉ")] = bstack111l1llll_opy_
  os.environ[bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭ຊ")] = str(bstack11llllll1_opy_)
  os.environ[bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖ࡙ࡕࡇࡖࡘࡤࡖࡌࡖࡉࡌࡒࠬ຋")] = str(True)
  if bstack11lll1ll11_opy_(arg, [bstack1lll11l_opy_ (u"ࠧ࠮ࡰࠪຌ"), bstack1lll11l_opy_ (u"ࠨ࠯࠰ࡲࡺࡳࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩຍ")]) != -1:
    os.environ[bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡄࡖࡆࡒࡌࡆࡎࠪຎ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1111l1l11l_opy_)
    return
  bstack1llll1l11l_opy_()
  global bstack1llll1lll1_opy_
  global bstack11ll11ll1l_opy_
  global bstack1l1lll111_opy_
  global bstack1llll1l111_opy_
  global bstack11l1l111l_opy_
  global bstack1ll1111ll_opy_
  global bstack1l111l11l_opy_
  arg.append(bstack1lll11l_opy_ (u"ࠥ࠱࡜ࠨຏ"))
  arg.append(bstack1lll11l_opy_ (u"ࠦ࡮࡭࡮ࡰࡴࡨ࠾ࡒࡵࡤࡶ࡮ࡨࠤࡦࡲࡲࡦࡣࡧࡽࠥ࡯࡭ࡱࡱࡵࡸࡪࡪ࠺ࡱࡻࡷࡩࡸࡺ࠮ࡑࡻࡷࡩࡸࡺࡗࡢࡴࡱ࡭ࡳ࡭ࠢຐ"))
  arg.append(bstack1lll11l_opy_ (u"ࠧ࠳ࡗࠣຑ"))
  arg.append(bstack1lll11l_opy_ (u"ࠨࡩࡨࡰࡲࡶࡪࡀࡔࡩࡧࠣ࡬ࡴࡵ࡫ࡪ࡯ࡳࡰࠧຒ"))
  global bstack1l11l1lll_opy_
  global bstack11l1111ll1_opy_
  global bstack1llll11l1l_opy_
  global bstack1l111ll1l1_opy_
  global bstack1lll1ll1ll_opy_
  global bstack1l1l111ll1_opy_
  global bstack1ll1ll1ll_opy_
  global bstack11l1l1l11l_opy_
  global bstack1ll1l11l1_opy_
  global bstack1ll1llll1_opy_
  global bstack1ll111l11_opy_
  global bstack1llll11lll_opy_
  global bstack1lll11111_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l11l1lll_opy_ = webdriver.Remote.__init__
    bstack11l1111ll1_opy_ = WebDriver.quit
    bstack11l1l1l11l_opy_ = WebDriver.close
    bstack1ll1l11l1_opy_ = WebDriver.get
    bstack1llll11l1l_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack11ll1111ll_opy_(CONFIG) and bstack111l1ll11_opy_():
    if bstack111l1l111l_opy_() < version.parse(bstack111l1l111_opy_):
      logger.error(bstack1l1llll1ll_opy_.format(bstack111l1l111l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1lll11l_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨຓ")) and callable(getattr(RemoteConnection, bstack1lll11l_opy_ (u"ࠨࡡࡪࡩࡹࡥࡰࡳࡱࡻࡽࡤࡻࡲ࡭ࠩດ"))):
          bstack1ll1llll1_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack1ll1llll1_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack1llllll11l_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack1ll111l11_opy_ = Config.getoption
    from _pytest import runner
    bstack1llll11lll_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1llll11ll_opy_)
  try:
    from pytest_bdd import reporting
    bstack1lll11111_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack1lll11l_opy_ (u"ࠩࡓࡰࡪࡧࡳࡦࠢ࡬ࡲࡸࡺࡡ࡭࡮ࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡱࠣࡶࡺࡴࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹ࡫ࡳࡵࡵࠪຕ"))
  bstack1l1lll111_opy_ = CONFIG.get(bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧຖ"), {}).get(bstack1lll11l_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ທ"))
  bstack1l111l11l_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack1l1111lll_opy_():
      bstack11l1l1l1l_opy_.invoke(Events.CONNECT, bstack111ll1l11_opy_())
    platform_index = int(os.environ.get(bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡒࡁࡕࡈࡒࡖࡒࡥࡉࡏࡆࡈ࡜ࠬຘ"), bstack1lll11l_opy_ (u"࠭࠰ࠨນ")))
  else:
    bstack1ll1ll1111_opy_(bstack1lllll1ll1_opy_)
  os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡕࡔࡇࡕࡒࡆࡓࡅࠨບ")] = CONFIG[bstack1lll11l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪປ")]
  os.environ[bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬຜ")] = CONFIG[bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ຝ")]
  os.environ[bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡅ࡚࡚ࡏࡎࡃࡗࡍࡔࡔࠧພ")] = bstack111ll1llll_opy_.__str__()
  from _pytest.config import main as bstack11111l11l_opy_
  bstack1llll1llll_opy_ = []
  try:
    exit_code = bstack11111l11l_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack1111l1111_opy_()
    if bstack1lll11l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤ࡫ࡲࡳࡱࡵࡣࡱ࡯ࡳࡵࠩຟ") in multiprocessing.current_process().__dict__.keys():
      for bstack1lll111lll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1llll1llll_opy_.append(bstack1lll111lll_opy_)
    try:
      bstack1l11l1ll1_opy_ = (bstack1llll1llll_opy_, int(exit_code))
      bstack1ll1ll11ll_opy_.append(bstack1l11l1ll1_opy_)
    except:
      bstack1ll1ll11ll_opy_.append((bstack1llll1llll_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1llll1llll_opy_.append({bstack1lll11l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫຠ"): bstack1lll11l_opy_ (u"ࠧࡑࡴࡲࡧࡪࡹࡳࠡࠩມ") + os.environ.get(bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡌࡒࡉࡋࡘࠨຢ")), bstack1lll11l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨຣ"): traceback.format_exc(), bstack1lll11l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ຤"): int(os.environ.get(bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫລ")))})
    bstack1ll1ll11ll_opy_.append((bstack1llll1llll_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack1lll11l_opy_ (u"ࠧࡸࡥࡵࡴ࡬ࡩࡸࠨ຦"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack11l1ll1l11_opy_ = e.__class__.__name__
    print(bstack1lll11l_opy_ (u"ࠨࠥࡴ࠼ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡵࡹࡳࡴࡩ࡯ࡩࠣࡦࡪ࡮ࡡࡷࡧࠣࡸࡪࡹࡴࠡࠧࡶࠦວ") % (bstack11l1ll1l11_opy_, e))
    return 1
def bstack111lll11ll_opy_(arg):
  global bstack11ll11l11l_opy_
  bstack1ll1ll1111_opy_(bstack1lll1lllll_opy_)
  os.environ[bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨຨ")] = str(bstack11llllll1_opy_)
  retries = bstack111l1l1l_opy_.bstack111l11ll_opy_(CONFIG)
  status_code = 0
  if bstack111l1l1l_opy_.bstack11111lll_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack111lllll11_opy_
    status_code = bstack111lllll11_opy_(arg)
  if status_code != 0:
    bstack11ll11l11l_opy_ = status_code
def bstack1l1l1lll11_opy_():
  logger.info(bstack11l1l1l1l1_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack1lll11l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧຩ"), help=bstack1lll11l_opy_ (u"ࠩࡊࡩࡳ࡫ࡲࡢࡶࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡧࡴࡴࡦࡪࡩࠪສ"))
  parser.add_argument(bstack1lll11l_opy_ (u"ࠪ࠱ࡺ࠭ຫ"), bstack1lll11l_opy_ (u"ࠫ࠲࠳ࡵࡴࡧࡵࡲࡦࡳࡥࠨຬ"), help=bstack1lll11l_opy_ (u"ࠬ࡟࡯ࡶࡴࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡸࡷࡪࡸ࡮ࡢ࡯ࡨࠫອ"))
  parser.add_argument(bstack1lll11l_opy_ (u"࠭࠭࡬ࠩຮ"), bstack1lll11l_opy_ (u"ࠧ࠮࠯࡮ࡩࡾ࠭ຯ"), help=bstack1lll11l_opy_ (u"ࠨ࡛ࡲࡹࡷࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡧࡣࡤࡧࡶࡷࠥࡱࡥࡺࠩະ"))
  parser.add_argument(bstack1lll11l_opy_ (u"ࠩ࠰ࡪࠬັ"), bstack1lll11l_opy_ (u"ࠪ࠱࠲࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨາ"), help=bstack1lll11l_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡷࡩࡸࡺࠠࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪຳ"))
  bstack1l11l1ll1l_opy_ = parser.parse_args()
  try:
    bstack1l11lll1ll_opy_ = bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲࡬࡫࡮ࡦࡴ࡬ࡧ࠳ࡿ࡭࡭࠰ࡶࡥࡲࡶ࡬ࡦࠩິ")
    if bstack1l11l1ll1l_opy_.framework and bstack1l11l1ll1l_opy_.framework not in (bstack1lll11l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭ີ"), bstack1lll11l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴ࠳ࠨຶ")):
      bstack1l11lll1ll_opy_ = bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࠱ࡽࡲࡲ࠮ࡴࡣࡰࡴࡱ࡫ࠧື")
    bstack1l1l111l1l_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1l11lll1ll_opy_)
    bstack11ll1ll1ll_opy_ = open(bstack1l1l111l1l_opy_, bstack1lll11l_opy_ (u"ࠩࡵຸࠫ"))
    bstack1l1111l1ll_opy_ = bstack11ll1ll1ll_opy_.read()
    bstack11ll1ll1ll_opy_.close()
    if bstack1l11l1ll1l_opy_.username:
      bstack1l1111l1ll_opy_ = bstack1l1111l1ll_opy_.replace(bstack1lll11l_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡗࡖࡉࡗࡔࡁࡎࡇູࠪ"), bstack1l11l1ll1l_opy_.username)
    if bstack1l11l1ll1l_opy_.key:
      bstack1l1111l1ll_opy_ = bstack1l1111l1ll_opy_.replace(bstack1lll11l_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡄࡇࡈࡋࡓࡔࡡࡎࡉ࡞຺࠭"), bstack1l11l1ll1l_opy_.key)
    if bstack1l11l1ll1l_opy_.framework:
      bstack1l1111l1ll_opy_ = bstack1l1111l1ll_opy_.replace(bstack1lll11l_opy_ (u"ࠬ࡟ࡏࡖࡔࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ົ"), bstack1l11l1ll1l_opy_.framework)
    file_name = bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩຼ")
    file_path = os.path.abspath(file_name)
    bstack1111l11ll_opy_ = open(file_path, bstack1lll11l_opy_ (u"ࠧࡸࠩຽ"))
    bstack1111l11ll_opy_.write(bstack1l1111l1ll_opy_)
    bstack1111l11ll_opy_.close()
    logger.info(bstack111l1l1l11_opy_)
    try:
      os.environ[bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪ຾")] = bstack1l11l1ll1l_opy_.framework if bstack1l11l1ll1l_opy_.framework != None else bstack1lll11l_opy_ (u"ࠤࠥ຿")
      config = yaml.safe_load(bstack1l1111l1ll_opy_)
      config[bstack1lll11l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪເ")] = bstack1lll11l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠱ࡸ࡫ࡴࡶࡲࠪແ")
      bstack11ll11lll1_opy_(bstack11llll1l1l_opy_, config)
    except Exception as e:
      logger.debug(bstack1ll111l1l_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack1lllll1l11_opy_.format(str(e)))
def bstack11ll11lll1_opy_(bstack11111l11ll_opy_, config, bstack1l111l1ll_opy_={}):
  global bstack111ll1llll_opy_
  global bstack1l11111ll_opy_
  global bstack111ll1l1_opy_
  if not config:
    return
  bstack1111l1l1l1_opy_ = bstack11l11l1l11_opy_ if not bstack111ll1llll_opy_ else (
    bstack11l1lllll_opy_ if bstack1lll11l_opy_ (u"ࠬࡧࡰࡱࠩໂ") in config else (
        bstack11l1l1l1ll_opy_ if config.get(bstack1lll11l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪໃ")) else bstack11l111l11l_opy_
    )
)
  bstack1lll11llll_opy_ = False
  bstack1l1ll1lll1_opy_ = False
  if bstack111ll1llll_opy_ is True:
      if bstack1lll11l_opy_ (u"ࠧࡢࡲࡳࠫໄ") in config:
          bstack1lll11llll_opy_ = True
      else:
          bstack1l1ll1lll1_opy_ = True
  bstack11llll1l1_opy_ = bstack11lll11lll_opy_.bstack1ll1ll111_opy_(config, bstack1l11111ll_opy_)
  bstack1l1l1111ll_opy_ = bstack11111ll11_opy_()
  data = {
    bstack1lll11l_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ໅"): config[bstack1lll11l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫໆ")],
    bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭໇"): config[bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿ່ࠧ")],
    bstack1lll11l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡹࡿࡰࡦ້ࠩ"): bstack11111l11ll_opy_,
    bstack1lll11l_opy_ (u"࠭ࡤࡦࡶࡨࡧࡹ࡫ࡤࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭໊ࠪ"): os.environ.get(bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌ໋ࠩ"), bstack1l11111ll_opy_),
    bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡩࡣࡶ࡬ࡪࡪ࡟ࡪࡦࠪ໌"): bstack111l1111l_opy_,
    bstack1lll11l_opy_ (u"ࠩࡲࡴࡹ࡯࡭ࡢ࡮ࡢ࡬ࡺࡨ࡟ࡶࡴ࡯ࠫໍ"): bstack1l1lll111l_opy_(),
    bstack1lll11l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໎"): {
      bstack1lll11l_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ໏"): str(config[bstack1lll11l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ໐")]) if bstack1lll11l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭໑") in config else bstack1lll11l_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࠣ໒"),
      bstack1lll11l_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧ࡙ࡩࡷࡹࡩࡰࡰࠪ໓"): sys.version,
      bstack1lll11l_opy_ (u"ࠩࡵࡩ࡫࡫ࡲࡳࡧࡵࠫ໔"): bstack1l1l1lllll_opy_(os.environ.get(bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ໕"), bstack1l11111ll_opy_)),
      bstack1lll11l_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭໖"): bstack1lll11l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ໗"),
      bstack1lll11l_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺࠧ໘"): bstack1111l1l1l1_opy_,
      bstack1lll11l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ໙"): bstack11llll1l1_opy_,
      bstack1lll11l_opy_ (u"ࠨࡶࡨࡷࡹ࡮ࡵࡣࡡࡸࡹ࡮ࡪࠧ໚"): os.environ[bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ໛")],
      bstack1lll11l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ໜ"): os.environ.get(bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ໝ"), bstack1l11111ll_opy_),
      bstack1lll11l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨໞ"): bstack1111ll11l_opy_(os.environ.get(bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨໟ"), bstack1l11111ll_opy_)),
      bstack1lll11l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭໠"): bstack1l1l1111ll_opy_.get(bstack1lll11l_opy_ (u"ࠨࡰࡤࡱࡪ࠭໡")),
      bstack1lll11l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ໢"): bstack1l1l1111ll_opy_.get(bstack1lll11l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫ໣")),
      bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ໤"): config[bstack1lll11l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ໥")] if config[bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ໦")] else bstack1lll11l_opy_ (u"ࠢࡶࡰ࡮ࡲࡴࡽ࡮ࠣ໧"),
      bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ໨"): str(config[bstack1lll11l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ໩")]) if bstack1lll11l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ໪") in config else bstack1lll11l_opy_ (u"ࠦࡺࡴ࡫࡯ࡱࡺࡲࠧ໫"),
      bstack1lll11l_opy_ (u"ࠬࡵࡳࠨ໬"): sys.platform,
      bstack1lll11l_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ໭"): socket.gethostname(),
      bstack1lll11l_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ໮"): bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࠪ໯"))
    }
  }
  if not bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡖ࡭࡬ࡴࡡ࡭ࠩ໰")) is None:
    data[bstack1lll11l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໱")][bstack1lll11l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡓࡥࡵࡣࡧࡥࡹࡧࠧ໲")] = {
      bstack1lll11l_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ໳"): bstack1lll11l_opy_ (u"࠭ࡵࡴࡧࡵࡣࡰ࡯࡬࡭ࡧࡧࠫ໴"),
      bstack1lll11l_opy_ (u"ࠧࡴ࡫ࡪࡲࡦࡲࠧ໵"): bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ໶")),
      bstack1lll11l_opy_ (u"ࠩࡶ࡭࡬ࡴࡡ࡭ࡐࡸࡱࡧ࡫ࡲࠨ໷"): bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡒࡴ࠭໸"))
    }
  if bstack11111l11ll_opy_ == bstack1lll111ll1_opy_:
    data[bstack1lll11l_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ໹")][bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࡇࡴࡴࡦࡪࡩࠪ໺")] = bstack11lll1l1l1_opy_(config)
    data[bstack1lll11l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ໻")][bstack1lll11l_opy_ (u"ࠧࡪࡵࡓࡩࡷࡩࡹࡂࡷࡷࡳࡊࡴࡡࡣ࡮ࡨࡨࠬ໼")] = percy.bstack11l1111l1l_opy_
    data[bstack1lll11l_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡱࡴࡲࡴࡪࡸࡴࡪࡧࡶࠫ໽")][bstack1lll11l_opy_ (u"ࠩࡳࡩࡷࡩࡹࡃࡷ࡬ࡰࡩࡏࡤࠨ໾")] = percy.percy_build_id
  if not bstack111l1l1l_opy_.bstack11ll1ll1l_opy_(CONFIG):
    data[bstack1lll11l_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭໿")][bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠨༀ")] = bstack111l1l1l_opy_.bstack11ll1ll1l_opy_(CONFIG)
  bstack1lll1llll_opy_ = bstack1lll1ll11_opy_.bstack111l1111_opy_(CONFIG, logger)
  bstack1lll1l11l_opy_ = bstack111l1l1l_opy_.bstack111l1111_opy_(config=CONFIG)
  if bstack1lll1llll_opy_ is not None and bstack1lll1l11l_opy_ is not None and bstack1lll1l11l_opy_.bstack1111llll_opy_():
    data[bstack1lll11l_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ༁")][bstack1lll1l11l_opy_.bstack11l11l11l1_opy_()] = bstack1lll1llll_opy_.bstack11lll1111_opy_()
  update(data[bstack1lll11l_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡶࡲࡰࡲࡨࡶࡹ࡯ࡥࡴࠩ༂")], bstack1l111l1ll_opy_)
  try:
    response = bstack1l11l1111_opy_(bstack1lll11l_opy_ (u"ࠧࡑࡑࡖࡘࠬ༃"), bstack11111lll11_opy_(bstack1l1111111l_opy_), data, {
      bstack1lll11l_opy_ (u"ࠨࡣࡸࡸ࡭࠭༄"): (config[bstack1lll11l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ༅")], config[bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭༆")])
    })
    if response:
      logger.debug(bstack1l1111ll1_opy_.format(bstack11111l11ll_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1111lll1l_opy_.format(str(e)))
def bstack1l1l1lllll_opy_(framework):
  return bstack1lll11l_opy_ (u"ࠦࢀࢃ࠭ࡱࡻࡷ࡬ࡴࡴࡡࡨࡧࡱࡸ࠴ࢁࡽࠣ༇").format(str(framework), __version__) if framework else bstack1lll11l_opy_ (u"ࠧࡶࡹࡵࡪࡲࡲࡦ࡭ࡥ࡯ࡶ࠲ࡿࢂࠨ༈").format(
    __version__)
def bstack1llll1l11l_opy_():
  global CONFIG
  global bstack111l11l1ll_opy_
  if bool(CONFIG):
    return
  try:
    bstack1l1ll111ll_opy_()
    logger.debug(bstack11l11111l_opy_.format(str(CONFIG)))
    bstack111l11l1ll_opy_ = bstack11ll1111l_opy_.configure_logger(CONFIG, bstack111l11l1ll_opy_)
    bstack11ll1l11ll_opy_()
  except Exception as e:
    logger.error(bstack1lll11l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࡻࡰ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࠥ༉") + str(e))
    sys.exit(1)
  sys.excepthook = bstack111llllll_opy_
  atexit.register(bstack11l1lll1l_opy_)
  signal.signal(signal.SIGINT, bstack1llllll1l1_opy_)
  signal.signal(signal.SIGTERM, bstack1llllll1l1_opy_)
def bstack111llllll_opy_(exctype, value, traceback):
  global bstack1l1lll1ll_opy_
  try:
    for driver in bstack1l1lll1ll_opy_:
      bstack1l1ll1l11l_opy_(driver, bstack1lll11l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ༊"), bstack1lll11l_opy_ (u"ࠣࡕࡨࡷࡸ࡯࡯࡯ࠢࡩࡥ࡮ࡲࡥࡥࠢࡺ࡭ࡹ࡮࠺ࠡ࡞ࡱࠦ་") + str(value))
  except Exception:
    pass
  logger.info(bstack111l111l11_opy_)
  bstack1l111l11l1_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l111l11l1_opy_(message=bstack1lll11l_opy_ (u"ࠩࠪ༌"), bstack111lll1l11_opy_ = False):
  global CONFIG
  bstack11ll1l1l1_opy_ = bstack1lll11l_opy_ (u"ࠪ࡫ࡱࡵࡢࡢ࡮ࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠬ།") if bstack111lll1l11_opy_ else bstack1lll11l_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ༎")
  try:
    if message:
      bstack1l111l1ll_opy_ = {
        bstack11ll1l1l1_opy_ : str(message)
      }
      bstack11ll11lll1_opy_(bstack1lll111ll1_opy_, CONFIG, bstack1l111l1ll_opy_)
    else:
      bstack11ll11lll1_opy_(bstack1lll111ll1_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack1l1l11lll_opy_.format(str(e)))
def bstack11111ll111_opy_(bstack1lll1ll11l_opy_, size):
  bstack1l1l1l1lll_opy_ = []
  while len(bstack1lll1ll11l_opy_) > size:
    bstack1l1lllllll_opy_ = bstack1lll1ll11l_opy_[:size]
    bstack1l1l1l1lll_opy_.append(bstack1l1lllllll_opy_)
    bstack1lll1ll11l_opy_ = bstack1lll1ll11l_opy_[size:]
  bstack1l1l1l1lll_opy_.append(bstack1lll1ll11l_opy_)
  return bstack1l1l1l1lll_opy_
def bstack111ll11l1_opy_(args):
  if bstack1lll11l_opy_ (u"ࠬ࠳࡭ࠨ༏") in args and bstack1lll11l_opy_ (u"࠭ࡰࡥࡤࠪ༐") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack11l1llll11_opy_, stage=STAGE.bstack1ll1lllll_opy_)
def run_on_browserstack(bstack111111lll_opy_=None, bstack1ll1ll11ll_opy_=None, bstack11ll1llll1_opy_=False):
  global CONFIG
  global bstack111l1llll_opy_
  global bstack11llllll1_opy_
  global bstack1l11111ll_opy_
  global bstack111ll1l1_opy_
  bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠧࠨ༑")
  bstack11l1l1ll11_opy_(bstack1111ll1l1_opy_, logger)
  if bstack111111lll_opy_ and isinstance(bstack111111lll_opy_, str):
    bstack111111lll_opy_ = eval(bstack111111lll_opy_)
  if bstack111111lll_opy_:
    CONFIG = bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨ༒")]
    bstack111l1llll_opy_ = bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪ༓")]
    bstack11llllll1_opy_ = bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ༔")]
    bstack111ll1l1_opy_.set_property(bstack1lll11l_opy_ (u"ࠫࡎ࡙࡟ࡂࡒࡓࡣࡆ࡛ࡔࡐࡏࡄࡘࡊ࠭༕"), bstack11llllll1_opy_)
    bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ༖")
  bstack111ll1l1_opy_.set_property(bstack1lll11l_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ༗"), uuid4().__str__())
  logger.info(bstack1lll11l_opy_ (u"ࠧࡔࡆࡎࠤࡷࡻ࡮ࠡࡵࡷࡥࡷࡺࡥࡥࠢࡺ࡭ࡹ࡮ࠠࡪࡦ࠽ࠤ༘ࠬ") + bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦ༙ࠪ")));
  logger.debug(bstack1lll11l_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࡁࠬ༚") + bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠪࡷࡩࡱࡒࡶࡰࡌࡨࠬ༛")))
  if not bstack11ll1llll1_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1111l1l11l_opy_)
      return
    if sys.argv[1] == bstack1lll11l_opy_ (u"ࠫ࠲࠳ࡶࡦࡴࡶ࡭ࡴࡴࠧ༜") or sys.argv[1] == bstack1lll11l_opy_ (u"ࠬ࠳ࡶࠨ༝"):
      logger.info(bstack1lll11l_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡖࡹࡵࡪࡲࡲ࡙ࠥࡄࡌࠢࡹࡿࢂ࠭༞").format(__version__))
      return
    if sys.argv[1] == bstack1lll11l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭༟"):
      bstack1l1l1lll11_opy_()
      return
  args = sys.argv
  bstack1llll1l11l_opy_()
  global bstack1llll1lll1_opy_
  global bstack1lllllll11_opy_
  global bstack1l111l11l_opy_
  global bstack1l11ll11ll_opy_
  global bstack11ll11ll1l_opy_
  global bstack1l1lll111_opy_
  global bstack1llll1l111_opy_
  global bstack11l1ll1l1_opy_
  global bstack11l1l111l_opy_
  global bstack1ll1111ll_opy_
  global bstack111l11llll_opy_
  bstack1lllllll11_opy_ = len(CONFIG.get(bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ༠"), []))
  if not bstack1l11l1lll1_opy_:
    if args[1] == bstack1lll11l_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ༡") or args[1] == bstack1lll11l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫ༢"):
      bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༣")
      args = args[2:]
    elif args[1] == bstack1lll11l_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ༤"):
      bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ༥")
      args = args[2:]
    elif args[1] == bstack1lll11l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭༦"):
      bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ༧")
      args = args[2:]
    elif args[1] == bstack1lll11l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ༨"):
      bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫ༩")
      args = args[2:]
    elif args[1] == bstack1lll11l_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ༪"):
      bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ༫")
      args = args[2:]
    elif args[1] == bstack1lll11l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭༬"):
      bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ༭")
      args = args[2:]
    else:
      if not bstack1lll11l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ༮") in CONFIG or str(CONFIG[bstack1lll11l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ༯")]).lower() in [bstack1lll11l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༰"), bstack1lll11l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱ࠷ࠬ༱")]:
        bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ༲")
        args = args[1:]
      elif str(CONFIG[bstack1lll11l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ༳")]).lower() == bstack1lll11l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭༴"):
        bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠨࡴࡲࡦࡴࡺ༵ࠧ")
        args = args[1:]
      elif str(CONFIG[bstack1lll11l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ༶")]).lower() == bstack1lll11l_opy_ (u"ࠪࡴࡦࡨ࡯ࡵ༷ࠩ"):
        bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠫࡵࡧࡢࡰࡶࠪ༸")
        args = args[1:]
      elif str(CONFIG[bstack1lll11l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ༹")]).lower() == bstack1lll11l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭༺"):
        bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ༻")
        args = args[1:]
      elif str(CONFIG[bstack1lll11l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ༼")]).lower() == bstack1lll11l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ༽"):
        bstack1l11l1lll1_opy_ = bstack1lll11l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ༾")
        args = args[1:]
      else:
        os.environ[bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭༿")] = bstack1l11l1lll1_opy_
        bstack11l1ll1l1l_opy_(bstack1l1ll1l111_opy_)
  os.environ[bstack1lll11l_opy_ (u"ࠬࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࡠࡗࡖࡉࡉ࠭ཀ")] = bstack1l11l1lll1_opy_
  bstack1l11111ll_opy_ = bstack1l11l1lll1_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1l111lll1l_opy_ = bstack1111ll1111_opy_[bstack1lll11l_opy_ (u"࠭ࡐ࡚ࡖࡈࡗ࡙࠳ࡂࡅࡆࠪཁ")] if bstack1l11l1lll1_opy_ == bstack1lll11l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧག") and bstack11llll111l_opy_() else bstack1l11l1lll1_opy_
      bstack11l1l1l1l_opy_.invoke(Events.bstack11l11ll1l1_opy_, bstack1ll1111111_opy_(
        sdk_version=__version__,
        path_config=bstack11l11l1111_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1l111lll1l_opy_,
        frameworks=[bstack1l111lll1l_opy_],
        framework_versions={
          bstack1l111lll1l_opy_: bstack1111ll11l_opy_(bstack1lll11l_opy_ (u"ࠨࡔࡲࡦࡴࡺࠧགྷ") if bstack1l11l1lll1_opy_ in [bstack1lll11l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨང"), bstack1lll11l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩཅ"), bstack1lll11l_opy_ (u"ࠫࡷࡵࡢࡰࡶ࠰࡭ࡳࡺࡥࡳࡰࡤࡰࠬཆ")] else bstack1l11l1lll1_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack1lll11l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢཇ"), None):
        CONFIG[bstack1lll11l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣ཈")] = cli.config.get(bstack1lll11l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤཉ"), None)
    except Exception as e:
      bstack11l1l1l1l_opy_.invoke(Events.bstack111l11ll1l_opy_, e.__traceback__, 1)
    if bstack11llllll1_opy_:
      CONFIG[bstack1lll11l_opy_ (u"ࠣࡣࡳࡴࠧཊ")] = cli.config[bstack1lll11l_opy_ (u"ࠤࡤࡴࡵࠨཋ")]
      logger.info(bstack11ll1l1111_opy_.format(CONFIG[bstack1lll11l_opy_ (u"ࠪࡥࡵࡶࠧཌ")]))
  else:
    bstack11l1l1l1l_opy_.clear()
  global bstack11l111ll1l_opy_
  global bstack1ll111llll_opy_
  if bstack111111lll_opy_:
    try:
      bstack11ll11l1l_opy_ = datetime.datetime.now()
      os.environ[bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡊࡗࡇࡍࡆ࡙ࡒࡖࡐ࠭ཌྷ")] = bstack1l11l1lll1_opy_
      bstack11ll11lll1_opy_(bstack11l11ll1l_opy_, CONFIG)
      cli.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽ࡷࡩࡱ࡟ࡵࡧࡶࡸࡤࡧࡴࡵࡧࡰࡴࡹ࡫ࡤࠣཎ"), datetime.datetime.now() - bstack11ll11l1l_opy_)
    except Exception as e:
      logger.debug(bstack1l1lll1l1l_opy_.format(str(e)))
  global bstack1l11l1lll_opy_
  global bstack11l1111ll1_opy_
  global bstack1111lll11_opy_
  global bstack1l11l1l1l_opy_
  global bstack11lll1111l_opy_
  global bstack11lll111ll_opy_
  global bstack1l111ll1l1_opy_
  global bstack1lll1ll1ll_opy_
  global bstack111l11111l_opy_
  global bstack1l1l111ll1_opy_
  global bstack1ll1ll1ll_opy_
  global bstack11l1l1l11l_opy_
  global bstack111l111lll_opy_
  global bstack11l111111l_opy_
  global bstack1ll1l11l1_opy_
  global bstack1ll1llll1_opy_
  global bstack1ll111l11_opy_
  global bstack1llll11lll_opy_
  global bstack1lll111l1l_opy_
  global bstack1lll11111_opy_
  global bstack1llll11l1l_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l11l1lll_opy_ = webdriver.Remote.__init__
    bstack11l1111ll1_opy_ = WebDriver.quit
    bstack11l1l1l11l_opy_ = WebDriver.close
    bstack1ll1l11l1_opy_ = WebDriver.get
    bstack1llll11l1l_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack11l111ll1l_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack111l11111_opy_
    bstack1ll111llll_opy_ = bstack111l11111_opy_()
  except Exception as e:
    pass
  try:
    global bstack1ll11l1ll_opy_
    from QWeb.keywords import browser
    bstack1ll11l1ll_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack11ll1111ll_opy_(CONFIG) and bstack111l1ll11_opy_():
    if bstack111l1l111l_opy_() < version.parse(bstack111l1l111_opy_):
      logger.error(bstack1l1llll1ll_opy_.format(bstack111l1l111l_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack1lll11l_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧཏ")) and callable(getattr(RemoteConnection, bstack1lll11l_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨཐ"))):
          RemoteConnection._get_proxy_url = bstack11l111l1l_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack11l111l1l_opy_
      except Exception as e:
        logger.error(bstack1llllll11l_opy_.format(str(e)))
  if not CONFIG.get(bstack1lll11l_opy_ (u"ࠨࡦ࡬ࡷࡦࡨ࡬ࡦࡃࡸࡸࡴࡉࡡࡱࡶࡸࡶࡪࡒ࡯ࡨࡵࠪད"), False) and not bstack111111lll_opy_:
    logger.info(bstack1l1l11l111_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack1lll11l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭དྷ") in CONFIG and str(CONFIG[bstack1lll11l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧན")]).lower() != bstack1lll11l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪཔ"):
      bstack111ll11ll_opy_()
    elif bstack1l11l1lll1_opy_ != bstack1lll11l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬཕ") or (bstack1l11l1lll1_opy_ == bstack1lll11l_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭བ") and not bstack111111lll_opy_):
      bstack1lllll11l1_opy_()
  if (bstack1l11l1lll1_opy_ in [bstack1lll11l_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭བྷ"), bstack1lll11l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧམ"), bstack1lll11l_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪཙ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack11l11lll1_opy_
        bstack11lll111ll_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack1ll1111lll_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack11lll1111l_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1l111l111l_opy_ + str(e))
    except Exception as e:
      bstack1l111ll1l_opy_(e, bstack1ll1111lll_opy_)
    if bstack1l11l1lll1_opy_ != bstack1lll11l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫཚ"):
      bstack1111l11ll1_opy_()
    bstack1111lll11_opy_ = Output.start_test
    bstack1l11l1l1l_opy_ = Output.end_test
    bstack1l111ll1l1_opy_ = TestStatus.__init__
    bstack111l11111l_opy_ = pabot._run
    bstack1l1l111ll1_opy_ = QueueItem.__init__
    bstack1ll1ll1ll_opy_ = pabot._create_command_for_execution
    bstack1lll111l1l_opy_ = pabot._report_results
  if bstack1l11l1lll1_opy_ == bstack1lll11l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫཛ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1l111ll1l_opy_(e, bstack1l1l1l111_opy_)
    bstack111l111lll_opy_ = Runner.run_hook
    bstack11l111111l_opy_ = Step.run
  if bstack1l11l1lll1_opy_ == bstack1lll11l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཛྷ"):
    try:
      from _pytest.config import Config
      bstack1ll111l11_opy_ = Config.getoption
      from _pytest import runner
      bstack1llll11lll_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1llll11ll_opy_)
    try:
      from pytest_bdd import reporting
      bstack1lll11111_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack1lll11l_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹࡵࠠࡳࡷࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࡹࠧཝ"))
  try:
    framework_name = bstack1lll11l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ཞ") if bstack1l11l1lll1_opy_ in [bstack1lll11l_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧཟ"), bstack1lll11l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨའ"), bstack1lll11l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫཡ")] else bstack11l1l1111_opy_(bstack1l11l1lll1_opy_)
    bstack111l11l1l1_opy_ = {
      bstack1lll11l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟࡯ࡣࡰࡩࠬར"): bstack1lll11l_opy_ (u"ࠬࡖࡹࡵࡧࡶࡸ࠲ࡩࡵࡤࡷࡰࡦࡪࡸࠧལ") if bstack1l11l1lll1_opy_ == bstack1lll11l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ཤ") and bstack11llll111l_opy_() else framework_name,
      bstack1lll11l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫཥ"): bstack1111ll11l_opy_(framework_name),
      bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ས"): __version__,
      bstack1lll11l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡻࡳࡦࡦࠪཧ"): bstack1l11l1lll1_opy_
    }
    if bstack1l11l1lll1_opy_ in bstack1l111lll1_opy_ + bstack11lllll11l_opy_:
      if bstack111ll1ll_opy_.bstack1l1111lll1_opy_(CONFIG):
        if bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪཨ") in CONFIG:
          os.environ[bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬཀྵ")] = os.getenv(bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ཪ"), json.dumps(CONFIG[bstack1lll11l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ཫ")]))
          CONFIG[bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧཬ")].pop(bstack1lll11l_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭཭"), None)
          CONFIG[bstack1lll11l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ཮")].pop(bstack1lll11l_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ཯"), None)
        bstack111l11l1l1_opy_[bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ཰")] = {
          bstack1lll11l_opy_ (u"ࠬࡴࡡ࡮ࡧཱࠪ"): bstack1lll11l_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨི"),
          bstack1lll11l_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨཱི"): str(bstack111l1l111l_opy_())
        }
    if bstack1l11l1lll1_opy_ not in [bstack1lll11l_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ུࠩ")] and not cli.is_running():
      bstack1ll1l11ll_opy_, bstack11llll1lll_opy_ = bstack1l111l1l_opy_.launch(CONFIG, bstack111l11l1l1_opy_)
      if bstack11llll1lll_opy_.get(bstack1lll11l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺཱུࠩ")) is not None and bstack111ll1ll_opy_.bstack1111111l1_opy_(CONFIG) is None:
        value = bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪྲྀ")].get(bstack1lll11l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬཷ"))
        if value is not None:
            CONFIG[bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬླྀ")] = value
        else:
          logger.debug(bstack1lll11l_opy_ (u"ࠨࡎࡰࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡧࡥࡹࡧࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠦཹ"))
  except Exception as e:
    logger.debug(bstack1ll11lll11_opy_.format(bstack1lll11l_opy_ (u"ࠧࡕࡧࡶࡸࡍࡻࡢࠨེ"), str(e)))
  if bstack1l11l1lll1_opy_ == bstack1lll11l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨཻ"):
    bstack1l111l11l_opy_ = True
    if bstack111111lll_opy_ and bstack11ll1llll1_opy_:
      bstack1l1lll111_opy_ = CONFIG.get(bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸོ࠭"), {}).get(bstack1lll11l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶཽࠬ"))
      bstack1ll1ll1111_opy_(bstack111l1llll1_opy_)
    elif bstack111111lll_opy_:
      bstack1l1lll111_opy_ = CONFIG.get(bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨཾ"), {}).get(bstack1lll11l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧཿ"))
      global bstack1l1lll1ll_opy_
      try:
        if bstack111ll11l1_opy_(bstack111111lll_opy_[bstack1lll11l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦྀࠩ")]) and multiprocessing.current_process().name == bstack1lll11l_opy_ (u"ࠧ࠱ཱྀࠩ"):
          bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྂ")].remove(bstack1lll11l_opy_ (u"ࠩ࠰ࡱࠬྃ"))
          bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ྄࠭")].remove(bstack1lll11l_opy_ (u"ࠫࡵࡪࡢࠨ྅"))
          bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨ྆")] = bstack111111lll_opy_[bstack1lll11l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ྇")][0]
          with open(bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྈ")], bstack1lll11l_opy_ (u"ࠨࡴࠪྉ")) as f:
            file_content = f.read()
          bstack11l11l11l_opy_ = bstack1lll11l_opy_ (u"ࠤࠥࠦ࡫ࡸ࡯࡮ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡵࡧ࡯ࠥ࡯࡭ࡱࡱࡵࡸࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣ࡮ࡴࡩࡵ࡫ࡤࡰ࡮ࢀࡥ࠼ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠ࡫ࡱ࡭ࡹ࡯ࡡ࡭࡫ࡽࡩ࠭ࢁࡽࠪ࠽ࠣࡪࡷࡵ࡭ࠡࡲࡧࡦࠥ࡯࡭ࡱࡱࡵࡸࠥࡖࡤࡣ࠽ࠣࡳ࡬ࡥࡤࡣࠢࡀࠤࡕࡪࡢ࠯ࡦࡲࡣࡧࡸࡥࡢ࡭࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥࡧࡩࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠨࡴࡧ࡯ࡪ࠱ࠦࡡࡳࡩ࠯ࠤࡹ࡫࡭ࡱࡱࡵࡥࡷࡿࠠ࠾ࠢ࠳࠭࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡹࡸࡹ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡤࡶ࡬ࠦ࠽ࠡࡵࡷࡶ࠭࡯࡮ࡵࠪࡤࡶ࡬࠯ࠫ࠲࠲ࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡨࡼࡨ࡫ࡰࡵࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡧࡳࠡࡧ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡵࡧࡳࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡰࡩࡢࡨࡧ࠮ࡳࡦ࡮ࡩ࠰ࡦࡸࡧ࠭ࡶࡨࡱࡵࡵࡲࡢࡴࡼ࠭ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡒࡧࡦ࠳ࡪ࡯ࡠࡤࠣࡁࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡕࡪࡢ࠯ࡦࡲࡣࡧࡸࡥࡢ࡭ࠣࡁࠥࡳ࡯ࡥࡡࡥࡶࡪࡧ࡫ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡕࡪࡢࠩࠫ࠱ࡷࡪࡺ࡟ࡵࡴࡤࡧࡪ࠮ࠩ࡝ࡰࠥࠦࠧྊ").format(str(bstack111111lll_opy_))
          bstack1ll1ll111l_opy_ = bstack11l11l11l_opy_ + file_content
          bstack11l11l1l1l_opy_ = bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྋ")] + bstack1lll11l_opy_ (u"ࠫࡤࡨࡳࡵࡣࡦ࡯ࡤࡺࡥ࡮ࡲ࠱ࡴࡾ࠭ྌ")
          with open(bstack11l11l1l1l_opy_, bstack1lll11l_opy_ (u"ࠬࡽࠧྍ")):
            pass
          with open(bstack11l11l1l1l_opy_, bstack1lll11l_opy_ (u"ࠨࡷࠬࠤྎ")) as f:
            f.write(bstack1ll1ll111l_opy_)
          import subprocess
          process_data = subprocess.run([bstack1lll11l_opy_ (u"ࠢࡱࡻࡷ࡬ࡴࡴࠢྏ"), bstack11l11l1l1l_opy_])
          if os.path.exists(bstack11l11l1l1l_opy_):
            os.unlink(bstack11l11l1l1l_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack111ll11l1_opy_(bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྐ")]):
            bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྑ")].remove(bstack1lll11l_opy_ (u"ࠪ࠱ࡲ࠭ྒ"))
            bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྒྷ")].remove(bstack1lll11l_opy_ (u"ࠬࡶࡤࡣࠩྔ"))
            bstack111111lll_opy_[bstack1lll11l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྕ")] = bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྖ")][0]
          bstack1ll1ll1111_opy_(bstack111l1llll1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྗ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack1lll11l_opy_ (u"ࠩࡢࡣࡳࡧ࡭ࡦࡡࡢࠫ྘")] = bstack1lll11l_opy_ (u"ࠪࡣࡤࡳࡡࡪࡰࡢࡣࠬྙ")
          mod_globals[bstack1lll11l_opy_ (u"ࠫࡤࡥࡦࡪ࡮ࡨࡣࡤ࠭ྚ")] = os.path.abspath(bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྛ")])
          exec(open(bstack111111lll_opy_[bstack1lll11l_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྜ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack1lll11l_opy_ (u"ࠧࡄࡣࡸ࡫࡭ࡺࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠧྜྷ").format(str(e)))
          for driver in bstack1l1lll1ll_opy_:
            bstack1ll1ll11ll_opy_.append({
              bstack1lll11l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ྞ"): bstack111111lll_opy_[bstack1lll11l_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྟ")],
              bstack1lll11l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩྠ"): str(e),
              bstack1lll11l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪྡ"): multiprocessing.current_process().name
            })
            bstack1l1ll1l11l_opy_(driver, bstack1lll11l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬྡྷ"), bstack1lll11l_opy_ (u"ࠨࡓࡦࡵࡶ࡭ࡴࡴࠠࡧࡣ࡬ࡰࡪࡪࠠࡸ࡫ࡷ࡬࠿ࠦ࡜࡯ࠤྣ") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack1l1lll1ll_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11llllll1_opy_, CONFIG, logger)
      bstack1l11lllll1_opy_()
      bstack11ll11l1ll_opy_()
      percy.bstack1l11ll1l1l_opy_()
      bstack1lllll1ll_opy_ = {
        bstack1lll11l_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྤ"): args[0],
        bstack1lll11l_opy_ (u"ࠨࡅࡒࡒࡋࡏࡇࠨྥ"): CONFIG,
        bstack1lll11l_opy_ (u"ࠩࡋ࡙ࡇࡥࡕࡓࡎࠪྦ"): bstack111l1llll_opy_,
        bstack1lll11l_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬྦྷ"): bstack11llllll1_opy_
      }
      if bstack1lll11l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧྨ") in CONFIG:
        bstack11lll11l11_opy_ = bstack11ll1l11l_opy_(args, logger, CONFIG, bstack111ll1llll_opy_, bstack1lllllll11_opy_)
        bstack11l1ll1l1_opy_ = bstack11lll11l11_opy_.bstack1llllll11_opy_(run_on_browserstack, bstack1lllll1ll_opy_, bstack111ll11l1_opy_(args))
      else:
        if bstack111ll11l1_opy_(args):
          bstack1lllll1ll_opy_[bstack1lll11l_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྩ")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1lllll1ll_opy_,))
          test.start()
          test.join()
        else:
          bstack1ll1ll1111_opy_(bstack111l1llll1_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack1lll11l_opy_ (u"࠭࡟ࡠࡰࡤࡱࡪࡥ࡟ࠨྪ")] = bstack1lll11l_opy_ (u"ࠧࡠࡡࡰࡥ࡮ࡴ࡟ࡠࠩྫ")
          mod_globals[bstack1lll11l_opy_ (u"ࠨࡡࡢࡪ࡮ࡲࡥࡠࡡࠪྫྷ")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1l11l1lll1_opy_ == bstack1lll11l_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨྭ") or bstack1l11l1lll1_opy_ == bstack1lll11l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩྮ"):
    percy.init(bstack11llllll1_opy_, CONFIG, logger)
    percy.bstack1l11ll1l1l_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1l111ll1l_opy_(e, bstack1ll1111lll_opy_)
    bstack1l11lllll1_opy_()
    bstack1ll1ll1111_opy_(bstack111l11l1l_opy_)
    if bstack111ll1llll_opy_:
      bstack11111l111_opy_(bstack111l11l1l_opy_, args)
      if bstack1lll11l_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩྯ") in args:
        i = args.index(bstack1lll11l_opy_ (u"ࠬ࠳࠭ࡱࡴࡲࡧࡪࡹࡳࡦࡵࠪྰ"))
        args.pop(i)
        args.pop(i)
      if bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩྱ") not in CONFIG:
        CONFIG[bstack1lll11l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪྲ")] = [{}]
        bstack1lllllll11_opy_ = 1
      if bstack1llll1lll1_opy_ == 0:
        bstack1llll1lll1_opy_ = 1
      args.insert(0, str(bstack1llll1lll1_opy_))
      args.insert(0, str(bstack1lll11l_opy_ (u"ࠨ࠯࠰ࡴࡷࡵࡣࡦࡵࡶࡩࡸ࠭ླ")))
    if bstack1l111l1l_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack11lll1lll_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack111111l11l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack1lll11l_opy_ (u"ࠤࡕࡓࡇࡕࡔࡠࡑࡓࡘࡎࡕࡎࡔࠤྴ"),
        ).parse_args(bstack11lll1lll_opy_)
        bstack1ll11l11l_opy_ = args.index(bstack11lll1lll_opy_[0]) if len(bstack11lll1lll_opy_) > 0 else len(args)
        args.insert(bstack1ll11l11l_opy_, str(bstack1lll11l_opy_ (u"ࠪ࠱࠲ࡲࡩࡴࡶࡨࡲࡪࡸࠧྵ")))
        args.insert(bstack1ll11l11l_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1lll11l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡷࡵࡢࡰࡶࡢࡰ࡮ࡹࡴࡦࡰࡨࡶ࠳ࡶࡹࠨྶ"))))
        if bstack111l1l1l_opy_.bstack11111lll_opy_(CONFIG):
          args.insert(bstack1ll11l11l_opy_, str(bstack1lll11l_opy_ (u"ࠬ࠳࠭࡭࡫ࡶࡸࡪࡴࡥࡳࠩྷ")))
          args.insert(bstack1ll11l11l_opy_ + 1, str(bstack1lll11l_opy_ (u"࠭ࡒࡦࡶࡵࡽࡋࡧࡩ࡭ࡧࡧ࠾ࢀࢃࠧྸ").format(bstack111l1l1l_opy_.bstack111l11ll_opy_(CONFIG))))
        if bstack111llll1l_opy_(os.environ.get(bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࠬྐྵ"))) and str(os.environ.get(bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓࡥࡔࡆࡕࡗࡗࠬྺ"), bstack1lll11l_opy_ (u"ࠩࡱࡹࡱࡲࠧྻ"))) != bstack1lll11l_opy_ (u"ࠪࡲࡺࡲ࡬ࠨྼ"):
          for bstack11l11llll_opy_ in bstack111111l11l_opy_:
            args.remove(bstack11l11llll_opy_)
          test_files = os.environ.get(bstack1lll11l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࡡࡗࡉࡘ࡚ࡓࠨ྽")).split(bstack1lll11l_opy_ (u"ࠬ࠲ࠧ྾"))
          for bstack11l1lll1ll_opy_ in test_files:
            args.append(bstack11l1lll1ll_opy_)
      except Exception as e:
        logger.error(bstack1lll11l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡦࡺࡴࡢࡥ࡫࡭ࡳ࡭ࠠ࡭࡫ࡶࡸࡪࡴࡥࡳࠢࡩࡳࡷࠦࡻࡾ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠰ࠤࢀࢃࠢ྿").format(bstack1l1llll11l_opy_, e))
    pabot.main(args)
  elif bstack1l11l1lll1_opy_ == bstack1lll11l_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨ࿀"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1l111ll1l_opy_(e, bstack1ll1111lll_opy_)
    for a in args:
      if bstack1lll11l_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡑࡎࡄࡘࡋࡕࡒࡎࡋࡑࡈࡊ࡞ࠧ࿁") in a:
        bstack11ll11ll1l_opy_ = int(a.split(bstack1lll11l_opy_ (u"ࠩ࠽ࠫ࿂"))[1])
      if bstack1lll11l_opy_ (u"ࠪࡆࡘ࡚ࡁࡄࡍࡇࡉࡋࡒࡏࡄࡃࡏࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ࿃") in a:
        bstack1l1lll111_opy_ = str(a.split(bstack1lll11l_opy_ (u"ࠫ࠿࠭࿄"))[1])
      if bstack1lll11l_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬ࿅") in a:
        bstack1llll1l111_opy_ = str(a.split(bstack1lll11l_opy_ (u"࠭࠺ࠨ࿆"))[1])
    bstack1111l1ll11_opy_ = None
    bstack1l1l11llll_opy_ = None
    if bstack1lll11l_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭࿇") in args:
      i = args.index(bstack1lll11l_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠧ࿈"))
      args.pop(i)
      bstack1111l1ll11_opy_ = args.pop(i)
    if bstack1lll11l_opy_ (u"ࠩ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࠬ࿉") in args:
      i = args.index(bstack1lll11l_opy_ (u"ࠪ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽ࠭࿊"))
      args.pop(i)
      bstack1l1l11llll_opy_ = args.pop(i)
    if bstack1111l1ll11_opy_ is not None:
      global bstack1l1l1l11ll_opy_
      bstack1l1l1l11ll_opy_ = bstack1111l1ll11_opy_
    if bstack1l1l11llll_opy_ is not None and int(bstack11ll11ll1l_opy_) < 0:
      bstack11ll11ll1l_opy_ = int(bstack1l1l11llll_opy_)
    bstack1ll1ll1111_opy_(bstack111l11l1l_opy_)
    run_cli(args)
    if bstack1lll11l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨ࿋") in multiprocessing.current_process().__dict__.keys():
      for bstack1lll111lll_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1ll1ll11ll_opy_.append(bstack1lll111lll_opy_)
  elif bstack1l11l1lll1_opy_ == bstack1lll11l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ࿌"):
    bstack1111lll111_opy_ = bstack1111l111_opy_(args, logger, CONFIG, bstack111ll1llll_opy_)
    bstack1111lll111_opy_.bstack111llll1_opy_()
    bstack1l11lllll1_opy_()
    bstack1l11ll11ll_opy_ = True
    bstack1ll1111ll_opy_ = bstack1111lll111_opy_.bstack1llll1l11_opy_()
    bstack1111lll111_opy_.bstack1lllll1ll_opy_(bstack1lll11lll1_opy_)
    bstack1111lll111_opy_.bstack1111l1ll_opy_()
    bstack11l1ll1ll_opy_(bstack1l11l1lll1_opy_, CONFIG, bstack1111lll111_opy_.bstack1111111l_opy_())
    bstack1l11l11111_opy_ = bstack1111lll111_opy_.bstack1llllll11_opy_(bstack1ll1lll11_opy_, {
      bstack1lll11l_opy_ (u"࠭ࡈࡖࡄࡢ࡙ࡗࡒࠧ࿍"): bstack111l1llll_opy_,
      bstack1lll11l_opy_ (u"ࠧࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ࿎"): bstack11llllll1_opy_,
      bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫ࿏"): bstack111ll1llll_opy_
    })
    try:
      bstack1llll1llll_opy_, bstack1ll1l1l1ll_opy_ = map(list, zip(*bstack1l11l11111_opy_))
      bstack11l1l111l_opy_ = bstack1llll1llll_opy_[0]
      for status_code in bstack1ll1l1l1ll_opy_:
        if status_code != 0:
          bstack111l11llll_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack1lll11l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡡࡷࡧࠣࡩࡷࡸ࡯ࡳࡵࠣࡥࡳࡪࠠࡴࡶࡤࡸࡺࡹࠠࡤࡱࡧࡩ࠳ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࠽ࠤࢀࢃࠢ࿐").format(str(e)))
  elif bstack1l11l1lll1_opy_ == bstack1lll11l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ࿑"):
    try:
      from behave.__main__ import main as bstack111lllll11_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1l111ll1l_opy_(e, bstack1l1l1l111_opy_)
    bstack1l11lllll1_opy_()
    bstack1l11ll11ll_opy_ = True
    bstack1111ll1l_opy_ = 1
    if bstack1lll11l_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ࿒") in CONFIG:
      bstack1111ll1l_opy_ = CONFIG[bstack1lll11l_opy_ (u"ࠬࡶࡡࡳࡣ࡯ࡰࡪࡲࡳࡑࡧࡵࡔࡱࡧࡴࡧࡱࡵࡱࠬ࿓")]
    if bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ࿔") in CONFIG:
      bstack11111l1l1_opy_ = int(bstack1111ll1l_opy_) * int(len(CONFIG[bstack1lll11l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ࿕")]))
    else:
      bstack11111l1l1_opy_ = int(bstack1111ll1l_opy_)
    config = Configuration(args)
    bstack11l1ll1ll1_opy_ = config.paths
    if len(bstack11l1ll1ll1_opy_) == 0:
      import glob
      pattern = bstack1lll11l_opy_ (u"ࠨࠬ࠭࠳࠯࠴ࡦࡦࡣࡷࡹࡷ࡫ࠧ࿖")
      bstack11111llll_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack11111llll_opy_)
      config = Configuration(args)
      bstack11l1ll1ll1_opy_ = config.paths
    bstack1llll111l_opy_ = [os.path.normpath(item) for item in bstack11l1ll1ll1_opy_]
    bstack1l11ll111_opy_ = [os.path.normpath(item) for item in args]
    bstack1l111111l_opy_ = [item for item in bstack1l11ll111_opy_ if item not in bstack1llll111l_opy_]
    import platform as pf
    if pf.system().lower() == bstack1lll11l_opy_ (u"ࠩࡺ࡭ࡳࡪ࡯ࡸࡵࠪ࿗"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack1llll111l_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11l11llll1_opy_)))
                    for bstack11l11llll1_opy_ in bstack1llll111l_opy_]
    bstack111l111l_opy_ = []
    for spec in bstack1llll111l_opy_:
      bstack111l1lll_opy_ = []
      bstack111l1lll_opy_ += bstack1l111111l_opy_
      bstack111l1lll_opy_.append(spec)
      bstack111l111l_opy_.append(bstack111l1lll_opy_)
    execution_items = []
    for bstack111l1lll_opy_ in bstack111l111l_opy_:
      if bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭࿘") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack1lll11l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ࿙")]):
          item = {}
          item[bstack1lll11l_opy_ (u"ࠬࡧࡲࡨࠩ࿚")] = bstack1lll11l_opy_ (u"࠭ࠠࠨ࿛").join(bstack111l1lll_opy_)
          item[bstack1lll11l_opy_ (u"ࠧࡪࡰࡧࡩࡽ࠭࿜")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack1lll11l_opy_ (u"ࠨࡣࡵ࡫ࠬ࿝")] = bstack1lll11l_opy_ (u"ࠩࠣࠫ࿞").join(bstack111l1lll_opy_)
        item[bstack1lll11l_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ࿟")] = 0
        execution_items.append(item)
    bstack1l111lll11_opy_ = bstack11111ll111_opy_(execution_items, bstack11111l1l1_opy_)
    for execution_item in bstack1l111lll11_opy_:
      bstack111ll111_opy_ = []
      for item in execution_item:
        bstack111ll111_opy_.append(bstack11ll11111_opy_(name=str(item[bstack1lll11l_opy_ (u"ࠫ࡮ࡴࡤࡦࡺࠪ࿠")]),
                                             target=bstack111lll11ll_opy_,
                                             args=(item[bstack1lll11l_opy_ (u"ࠬࡧࡲࡨࠩ࿡")],)))
      for t in bstack111ll111_opy_:
        t.start()
      for t in bstack111ll111_opy_:
        t.join()
  else:
    bstack11l1ll1l1l_opy_(bstack1l1ll1l111_opy_)
  if not bstack111111lll_opy_:
    bstack11llll1111_opy_()
    if(bstack1l11l1lll1_opy_ in [bstack1lll11l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭࿢"), bstack1lll11l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ࿣")]):
      bstack1ll11l11ll_opy_()
  bstack11ll1111l_opy_.bstack1ll11ll111_opy_()
def browserstack_initialize(bstack111l111ll1_opy_=None):
  logger.info(bstack1lll11l_opy_ (u"ࠨࡔࡸࡲࡳ࡯࡮ࡨࠢࡖࡈࡐࠦࡷࡪࡶ࡫ࠤࡦࡸࡧࡴ࠼ࠣࠫ࿤") + str(bstack111l111ll1_opy_))
  run_on_browserstack(bstack111l111ll1_opy_, None, True)
@measure(event_name=EVENTS.bstack11l1ll11ll_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack11llll1111_opy_():
  global CONFIG
  global bstack1l11111ll_opy_
  global bstack111l11llll_opy_
  global bstack11ll11l11l_opy_
  global bstack111ll1l1_opy_
  bstack1l11111111_opy_.bstack11ll111l1l_opy_()
  if cli.is_running():
    bstack11l1l1l1l_opy_.invoke(Events.bstack1l11l11l1l_opy_)
  else:
    bstack1lll1l11l_opy_ = bstack111l1l1l_opy_.bstack111l1111_opy_(config=CONFIG)
    bstack1lll1l11l_opy_.bstack11111l11l1_opy_(CONFIG)
  if bstack1l11111ll_opy_ == bstack1lll11l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ࿥"):
    if not cli.is_enabled(CONFIG):
      bstack1l111l1l_opy_.stop()
  else:
    bstack1l111l1l_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1l11111l_opy_.bstack11ll11l111_opy_()
  if bstack1lll11l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ࿦") in CONFIG and str(CONFIG[bstack1lll11l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ࿧")]).lower() != bstack1lll11l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ࿨"):
    hashed_id, bstack1lll1l1l1l_opy_ = bstack11ll11lll_opy_()
  else:
    hashed_id, bstack1lll1l1l1l_opy_ = get_build_link()
  bstack1l11lllll_opy_(hashed_id)
  logger.info(bstack1lll11l_opy_ (u"࠭ࡓࡅࡍࠣࡶࡺࡴࠠࡦࡰࡧࡩࡩࠦࡦࡰࡴࠣ࡭ࡩࡀࠧ࿩") + bstack111ll1l1_opy_.get_property(bstack1lll11l_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ࿪"), bstack1lll11l_opy_ (u"ࠨࠩ࿫")) + bstack1lll11l_opy_ (u"ࠩ࠯ࠤࡹ࡫ࡳࡵࡪࡸࡦࠥ࡯ࡤ࠻ࠢࠪ࿬") + os.getenv(bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ࿭"), bstack1lll11l_opy_ (u"ࠫࠬ࿮")))
  if hashed_id is not None and bstack11lll1ll1l_opy_() != -1:
    sessions = bstack1l111l1l1_opy_(hashed_id)
    bstack1lllllllll_opy_(sessions, bstack1lll1l1l1l_opy_)
  if bstack1l11111ll_opy_ == bstack1lll11l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ࿯") and bstack111l11llll_opy_ != 0:
    sys.exit(bstack111l11llll_opy_)
  if bstack1l11111ll_opy_ == bstack1lll11l_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭࿰") and bstack11ll11l11l_opy_ != 0:
    sys.exit(bstack11ll11l11l_opy_)
def bstack1l11lllll_opy_(new_id):
    global bstack111l1111l_opy_
    bstack111l1111l_opy_ = new_id
def bstack11l1l1111_opy_(bstack1l111l111_opy_):
  if bstack1l111l111_opy_:
    return bstack1l111l111_opy_.capitalize()
  else:
    return bstack1lll11l_opy_ (u"ࠧࠨ࿱")
@measure(event_name=EVENTS.bstack11lllll111_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1l1l11lll1_opy_(bstack11l11111ll_opy_):
  if bstack1lll11l_opy_ (u"ࠨࡰࡤࡱࡪ࠭࿲") in bstack11l11111ll_opy_ and bstack11l11111ll_opy_[bstack1lll11l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ࿳")] != bstack1lll11l_opy_ (u"ࠪࠫ࿴"):
    return bstack11l11111ll_opy_[bstack1lll11l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ࿵")]
  else:
    bstack1l1llll1l_opy_ = bstack1lll11l_opy_ (u"ࠧࠨ࿶")
    if bstack1lll11l_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭࿷") in bstack11l11111ll_opy_ and bstack11l11111ll_opy_[bstack1lll11l_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧ࿸")] != None:
      bstack1l1llll1l_opy_ += bstack11l11111ll_opy_[bstack1lll11l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨ࿹")] + bstack1lll11l_opy_ (u"ࠤ࠯ࠤࠧ࿺")
      if bstack11l11111ll_opy_[bstack1lll11l_opy_ (u"ࠪࡳࡸ࠭࿻")] == bstack1lll11l_opy_ (u"ࠦ࡮ࡵࡳࠣ࿼"):
        bstack1l1llll1l_opy_ += bstack1lll11l_opy_ (u"ࠧ࡯ࡏࡔࠢࠥ࿽")
      bstack1l1llll1l_opy_ += (bstack11l11111ll_opy_[bstack1lll11l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪ࿾")] or bstack1lll11l_opy_ (u"ࠧࠨ࿿"))
      return bstack1l1llll1l_opy_
    else:
      bstack1l1llll1l_opy_ += bstack11l1l1111_opy_(bstack11l11111ll_opy_[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩက")]) + bstack1lll11l_opy_ (u"ࠤࠣࠦခ") + (
              bstack11l11111ll_opy_[bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬဂ")] or bstack1lll11l_opy_ (u"ࠫࠬဃ")) + bstack1lll11l_opy_ (u"ࠧ࠲ࠠࠣင")
      if bstack11l11111ll_opy_[bstack1lll11l_opy_ (u"࠭࡯ࡴࠩစ")] == bstack1lll11l_opy_ (u"ࠢࡘ࡫ࡱࡨࡴࡽࡳࠣဆ"):
        bstack1l1llll1l_opy_ += bstack1lll11l_opy_ (u"࡙ࠣ࡬ࡲࠥࠨဇ")
      bstack1l1llll1l_opy_ += bstack11l11111ll_opy_[bstack1lll11l_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ဈ")] or bstack1lll11l_opy_ (u"ࠪࠫဉ")
      return bstack1l1llll1l_opy_
@measure(event_name=EVENTS.bstack1l111llll_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1l1lll1ll1_opy_(bstack1l1l11ll1l_opy_):
  if bstack1l1l11ll1l_opy_ == bstack1lll11l_opy_ (u"ࠦࡩࡵ࡮ࡦࠤည"):
    return bstack1lll11l_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࡨࡴࡨࡩࡳࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡨࡴࡨࡩࡳࠨ࠾ࡄࡱࡰࡴࡱ࡫ࡴࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨဋ")
  elif bstack1l1l11ll1l_opy_ == bstack1lll11l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࠨဌ"):
    return bstack1lll11l_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡵࡩࡩࡁࠢ࠿࠾ࡩࡳࡳࡺࠠࡤࡱ࡯ࡳࡷࡃࠢࡳࡧࡧࠦࡃࡌࡡࡪ࡮ࡨࡨࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪဍ")
  elif bstack1l1l11ll1l_opy_ == bstack1lll11l_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠣဎ"):
    return bstack1lll11l_opy_ (u"ࠩ࠿ࡸࡩࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾࡬ࡸࡥࡦࡰ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦ࡬ࡸࡥࡦࡰࠥࡂࡕࡧࡳࡴࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩဏ")
  elif bstack1l1l11ll1l_opy_ == bstack1lll11l_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤတ"):
    return bstack1lll11l_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡲࡦࡦ࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡷ࡫ࡤࠣࡀࡈࡶࡷࡵࡲ࠽࠱ࡩࡳࡳࡺ࠾࠽࠱ࡷࡨࡃ࠭ထ")
  elif bstack1l1l11ll1l_opy_ == bstack1lll11l_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨဒ"):
    return bstack1lll11l_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࠥࡨࡩࡦ࠹࠲࠷࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࠧࡪ࡫ࡡ࠴࠴࠹ࠦࡃ࡚ࡩ࡮ࡧࡲࡹࡹࡂ࠯ࡧࡱࡱࡸࡃࡂ࠯ࡵࡦࡁࠫဓ")
  elif bstack1l1l11ll1l_opy_ == bstack1lll11l_opy_ (u"ࠢࡳࡷࡱࡲ࡮ࡴࡧࠣန"):
    return bstack1lll11l_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽ࡦࡱࡧࡣ࡬࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡦࡱࡧࡣ࡬ࠤࡁࡖࡺࡴ࡮ࡪࡰࡪࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩပ")
  else:
    return bstack1lll11l_opy_ (u"ࠩ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡨ࡬ࡢࡥ࡮࠿ࠧࡄ࠼ࡧࡱࡱࡸࠥࡩ࡯࡭ࡱࡵࡁࠧࡨ࡬ࡢࡥ࡮ࠦࡃ࠭ဖ") + bstack11l1l1111_opy_(
      bstack1l1l11ll1l_opy_) + bstack1lll11l_opy_ (u"ࠪࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩဗ")
def bstack1ll11l111_opy_(session):
  return bstack1lll11l_opy_ (u"ࠫࡁࡺࡲࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡴࡲࡻࠧࡄ࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠡࡵࡨࡷࡸ࡯࡯࡯࠯ࡱࡥࡲ࡫ࠢ࠿࠾ࡤࠤ࡭ࡸࡥࡧ࠿ࠥࡿࢂࠨࠠࡵࡣࡵ࡫ࡪࡺ࠽ࠣࡡࡥࡰࡦࡴ࡫ࠣࡀࡾࢁࡁ࠵ࡡ࠿࠾࠲ࡸࡩࡄࡻࡾࡽࢀࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁࡺࡤࠡࡣ࡯࡭࡬ࡴ࠽ࠣࡥࡨࡲࡹ࡫ࡲࠣࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢ࠿ࡽࢀࡀ࠴ࡺࡤ࠿࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࡃࢁࡽ࠽࠱ࡷࡨࡃࡂ࠯ࡵࡴࡁࠫဘ").format(
    session[bstack1lll11l_opy_ (u"ࠬࡶࡵࡣ࡮࡬ࡧࡤࡻࡲ࡭ࠩမ")], bstack1l1l11lll1_opy_(session), bstack1l1lll1ll1_opy_(session[bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤࡹࡴࡢࡶࡸࡷࠬယ")]),
    bstack1l1lll1ll1_opy_(session[bstack1lll11l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧရ")]),
    bstack11l1l1111_opy_(session[bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩလ")] or session[bstack1lll11l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩဝ")] or bstack1lll11l_opy_ (u"ࠪࠫသ")) + bstack1lll11l_opy_ (u"ࠦࠥࠨဟ") + (session[bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧဠ")] or bstack1lll11l_opy_ (u"࠭ࠧအ")),
    session[bstack1lll11l_opy_ (u"ࠧࡰࡵࠪဢ")] + bstack1lll11l_opy_ (u"ࠣࠢࠥဣ") + session[bstack1lll11l_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ဤ")], session[bstack1lll11l_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࠬဥ")] or bstack1lll11l_opy_ (u"ࠫࠬဦ"),
    session[bstack1lll11l_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩဧ")] if session[bstack1lll11l_opy_ (u"࠭ࡣࡳࡧࡤࡸࡪࡪ࡟ࡢࡶࠪဨ")] else bstack1lll11l_opy_ (u"ࠧࠨဩ"))
@measure(event_name=EVENTS.bstack1l1l11ll1_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def bstack1lllllllll_opy_(sessions, bstack1lll1l1l1l_opy_):
  try:
    bstack111111l11_opy_ = bstack1lll11l_opy_ (u"ࠣࠤဪ")
    if not os.path.exists(bstack1l1l11l1l_opy_):
      os.mkdir(bstack1l1l11l1l_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack1lll11l_opy_ (u"ࠩࡤࡷࡸ࡫ࡴࡴ࠱ࡵࡩࡵࡵࡲࡵ࠰࡫ࡸࡲࡲࠧါ")), bstack1lll11l_opy_ (u"ࠪࡶࠬာ")) as f:
      bstack111111l11_opy_ = f.read()
    bstack111111l11_opy_ = bstack111111l11_opy_.replace(bstack1lll11l_opy_ (u"ࠫࢀࠫࡒࡆࡕࡘࡐ࡙࡙࡟ࡄࡑࡘࡒ࡙ࠫࡽࠨိ"), str(len(sessions)))
    bstack111111l11_opy_ = bstack111111l11_opy_.replace(bstack1lll11l_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡕࡓࡎࠨࢁࠬီ"), bstack1lll1l1l1l_opy_)
    bstack111111l11_opy_ = bstack111111l11_opy_.replace(bstack1lll11l_opy_ (u"࠭ࡻࠦࡄࡘࡍࡑࡊ࡟ࡏࡃࡐࡉࠪࢃࠧု"),
                                              sessions[0].get(bstack1lll11l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥ࡮ࡢ࡯ࡨࠫူ")) if sessions[0] else bstack1lll11l_opy_ (u"ࠨࠩေ"))
    with open(os.path.join(bstack1l1l11l1l_opy_, bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭ဲ")), bstack1lll11l_opy_ (u"ࠪࡻࠬဳ")) as stream:
      stream.write(bstack111111l11_opy_.split(bstack1lll11l_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨဴ"))[0])
      for session in sessions:
        stream.write(bstack1ll11l111_opy_(session))
      stream.write(bstack111111l11_opy_.split(bstack1lll11l_opy_ (u"ࠬࢁࠥࡔࡇࡖࡗࡎࡕࡎࡔࡡࡇࡅ࡙ࡇࠥࡾࠩဵ"))[1])
    logger.info(bstack1lll11l_opy_ (u"࠭ࡇࡦࡰࡨࡶࡦࡺࡥࡥࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡤࡸ࡭ࡱࡪࠠࡢࡴࡷ࡭࡫ࡧࡣࡵࡵࠣࡥࡹࠦࡻࡾࠩံ").format(bstack1l1l11l1l_opy_));
  except Exception as e:
    logger.debug(bstack11lll1ll1_opy_.format(str(e)))
def bstack1l111l1l1_opy_(hashed_id):
  global CONFIG
  try:
    bstack11ll11l1l_opy_ = datetime.datetime.now()
    host = bstack1lll11l_opy_ (u"ࠧࡩࡶࡷࡴࡸࡀ࠯࠰ࡣࡳ࡭࠲ࡩ࡬ࡰࡷࡧ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ့ࠧ") if bstack1lll11l_opy_ (u"ࠨࡣࡳࡴࠬး") in CONFIG else bstack1lll11l_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡥࡵ࡯࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯္ࠪ")
    user = CONFIG[bstack1lll11l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩ်ࠬ")]
    key = CONFIG[bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧျ")]
    bstack111l1ll1ll_opy_ = bstack1lll11l_opy_ (u"ࠬࡧࡰࡱ࠯ࡤࡹࡹࡵ࡭ࡢࡶࡨࠫြ") if bstack1lll11l_opy_ (u"࠭ࡡࡱࡲࠪွ") in CONFIG else (bstack1lll11l_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫှ") if CONFIG.get(bstack1lll11l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬဿ")) else bstack1lll11l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ၀"))
    host = bstack11llll111_opy_(cli.config, [bstack1lll11l_opy_ (u"ࠥࡥࡵ࡯ࡳࠣ၁"), bstack1lll11l_opy_ (u"ࠦࡦࡶࡰࡂࡷࡷࡳࡲࡧࡴࡦࠤ၂"), bstack1lll11l_opy_ (u"ࠧࡧࡰࡪࠤ၃")], host) if bstack1lll11l_opy_ (u"࠭ࡡࡱࡲࠪ၄") in CONFIG else bstack11llll111_opy_(cli.config, [bstack1lll11l_opy_ (u"ࠢࡢࡲ࡬ࡷࠧ၅"), bstack1lll11l_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵࡧࠥ၆"), bstack1lll11l_opy_ (u"ࠤࡤࡴ࡮ࠨ၇")], host)
    url = bstack1lll11l_opy_ (u"ࠪࡿࢂ࠵ࡻࡾ࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠮࡫ࡵࡲࡲࠬ၈").format(host, bstack111l1ll1ll_opy_, hashed_id)
    headers = {
      bstack1lll11l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪ၉"): bstack1lll11l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ၊"),
    }
    proxies = bstack1lll1lll11_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠨࡨࡵࡶࡳ࠾࡬࡫ࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡵࡢࡰ࡮ࡹࡴࠣ။"), datetime.datetime.now() - bstack11ll11l1l_opy_)
      return list(map(lambda session: session[bstack1lll11l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࠬ၌")], response.json()))
  except Exception as e:
    logger.debug(bstack11l1ll111l_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack11ll1l1l11_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def get_build_link():
  global CONFIG
  global bstack111l1111l_opy_
  try:
    if bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ၍") in CONFIG:
      bstack11ll11l1l_opy_ = datetime.datetime.now()
      host = bstack1lll11l_opy_ (u"ࠩࡤࡴ࡮࠳ࡣ࡭ࡱࡸࡨࠬ၎") if bstack1lll11l_opy_ (u"ࠪࡥࡵࡶࠧ၏") in CONFIG else bstack1lll11l_opy_ (u"ࠫࡦࡶࡩࠨၐ")
      user = CONFIG[bstack1lll11l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧၑ")]
      key = CONFIG[bstack1lll11l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩၒ")]
      bstack111l1ll1ll_opy_ = bstack1lll11l_opy_ (u"ࠧࡢࡲࡳ࠱ࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭ၓ") if bstack1lll11l_opy_ (u"ࠨࡣࡳࡴࠬၔ") in CONFIG else bstack1lll11l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫၕ")
      url = bstack1lll11l_opy_ (u"ࠪ࡬ࡹࡺࡰࡴ࠼࠲࠳ࢀࢃ࠺ࡼࡿࡃࡿࢂ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡾࢁ࠴ࡨࡵࡪ࡮ࡧࡷ࠳ࡰࡳࡰࡰࠪၖ").format(user, key, host, bstack111l1ll1ll_opy_)
      if cli.is_enabled(CONFIG):
        bstack1lll1l1l1l_opy_, hashed_id = cli.bstack111lll111_opy_()
        logger.info(bstack11ll11111l_opy_.format(bstack1lll1l1l1l_opy_))
        return [hashed_id, bstack1lll1l1l1l_opy_]
      else:
        headers = {
          bstack1lll11l_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪၗ"): bstack1lll11l_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨၘ"),
        }
        if bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨၙ") in CONFIG:
          params = {bstack1lll11l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬၚ"): CONFIG[bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫၛ")], bstack1lll11l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬၜ"): CONFIG[bstack1lll11l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬၝ")]}
        else:
          params = {bstack1lll11l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩၞ"): CONFIG[bstack1lll11l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨၟ")]}
        proxies = bstack1lll1lll11_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack1l111l1l1l_opy_ = response.json()[0][bstack1lll11l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡦࡺ࡯࡬ࡥࠩၠ")]
          if bstack1l111l1l1l_opy_:
            bstack1lll1l1l1l_opy_ = bstack1l111l1l1l_opy_[bstack1lll11l_opy_ (u"ࠧࡱࡷࡥࡰ࡮ࡩ࡟ࡶࡴ࡯ࠫၡ")].split(bstack1lll11l_opy_ (u"ࠨࡲࡸࡦࡱ࡯ࡣ࠮ࡤࡸ࡭ࡱࡪࠧၢ"))[0] + bstack1lll11l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡴ࠱ࠪၣ") + bstack1l111l1l1l_opy_[
              bstack1lll11l_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ၤ")]
            logger.info(bstack11ll11111l_opy_.format(bstack1lll1l1l1l_opy_))
            bstack111l1111l_opy_ = bstack1l111l1l1l_opy_[bstack1lll11l_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧၥ")]
            bstack11l1111lll_opy_ = CONFIG[bstack1lll11l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨၦ")]
            if bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨၧ") in CONFIG:
              bstack11l1111lll_opy_ += bstack1lll11l_opy_ (u"ࠧࠡࠩၨ") + CONFIG[bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪၩ")]
            if bstack11l1111lll_opy_ != bstack1l111l1l1l_opy_[bstack1lll11l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧၪ")]:
              logger.debug(bstack1ll11l1l11_opy_.format(bstack1l111l1l1l_opy_[bstack1lll11l_opy_ (u"ࠪࡲࡦࡳࡥࠨၫ")], bstack11l1111lll_opy_))
            cli.bstack111l1l1l1l_opy_(bstack1lll11l_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡪࡩࡹࡥࡢࡶ࡫࡯ࡨࡤࡲࡩ࡯࡭ࠥၬ"), datetime.datetime.now() - bstack11ll11l1l_opy_)
            return [bstack1l111l1l1l_opy_[bstack1lll11l_opy_ (u"ࠬ࡮ࡡࡴࡪࡨࡨࡤ࡯ࡤࠨၭ")], bstack1lll1l1l1l_opy_]
    else:
      logger.warn(bstack1lllllll1l_opy_)
  except Exception as e:
    logger.debug(bstack111l1lll11_opy_.format(str(e)))
  return [None, None]
def bstack11llll11ll_opy_(url, bstack1l1lllll1_opy_=False):
  global CONFIG
  global bstack1ll11l1111_opy_
  if not bstack1ll11l1111_opy_:
    hostname = bstack1111lllll1_opy_(url)
    is_private = bstack1l1lll1111_opy_(hostname)
    if (bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪၮ") in CONFIG and not bstack111llll1l_opy_(CONFIG[bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫၯ")])) and (is_private or bstack1l1lllll1_opy_):
      bstack1ll11l1111_opy_ = hostname
def bstack1111lllll1_opy_(url):
  return urlparse(url).hostname
def bstack1l1lll1111_opy_(hostname):
  for bstack111ll11l1l_opy_ in bstack1lllll1111_opy_:
    regex = re.compile(bstack111ll11l1l_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1l11111l1l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack11l1111l1_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack11ll11ll1l_opy_
  bstack11llll1ll1_opy_ = not (bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬၰ"), None) and bstack1ll111ll_opy_(
          threading.current_thread(), bstack1lll11l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨၱ"), None))
  bstack11ll11ll11_opy_ = getattr(driver, bstack1lll11l_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪၲ"), None) != True
  bstack11l11l1l1_opy_ = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫၳ"), None) and bstack1ll111ll_opy_(
          threading.current_thread(), bstack1lll11l_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧၴ"), None)
  if bstack11l11l1l1_opy_:
    if not bstack1l1lll11l_opy_():
      logger.warning(bstack1lll11l_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴ࠰ࠥၵ"))
      return {}
    logger.debug(bstack1lll11l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠫၶ"))
    logger.debug(perform_scan(driver, driver_command=bstack1lll11l_opy_ (u"ࠨࡧࡻࡩࡨࡻࡴࡦࡕࡦࡶ࡮ࡶࡴࠨၷ")))
    results = bstack1l1ll1ll1l_opy_(bstack1lll11l_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡵࠥၸ"))
    if results is not None and results.get(bstack1lll11l_opy_ (u"ࠥ࡭ࡸࡹࡵࡦࡵࠥၹ")) is not None:
        return results[bstack1lll11l_opy_ (u"ࠦ࡮ࡹࡳࡶࡧࡶࠦၺ")]
    logger.error(bstack1lll11l_opy_ (u"ࠧࡔ࡯ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡔࡨࡷࡺࡲࡴࡴࠢࡺࡩࡷ࡫ࠠࡧࡱࡸࡲࡩ࠴ࠢၻ"))
    return []
  if not bstack111ll1ll_opy_.bstack1111l111l_opy_(CONFIG, bstack11ll11ll1l_opy_) or (bstack11ll11ll11_opy_ and bstack11llll1ll1_opy_):
    logger.warning(bstack1lll11l_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤၼ"))
    return {}
  try:
    logger.debug(bstack1lll11l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠫၽ"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack11111ll1l_opy_.bstack11l1l1ll1_opy_)
    return results
  except Exception:
    logger.error(bstack1lll11l_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡽࡥࡳࡧࠣࡪࡴࡻ࡮ࡥ࠰ࠥၾ"))
    return {}
@measure(event_name=EVENTS.bstack111111111_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack11ll11ll1l_opy_
  bstack11llll1ll1_opy_ = not (bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ၿ"), None) and bstack1ll111ll_opy_(
          threading.current_thread(), bstack1lll11l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩႀ"), None))
  bstack11ll11ll11_opy_ = getattr(driver, bstack1lll11l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫႁ"), None) != True
  bstack11l11l1l1_opy_ = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬႂ"), None) and bstack1ll111ll_opy_(
          threading.current_thread(), bstack1lll11l_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨႃ"), None)
  if bstack11l11l1l1_opy_:
    if not bstack1l1lll11l_opy_():
      logger.warning(bstack1lll11l_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡲࡳࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡨࡷࡸ࡯࡯࡯࠮ࠣࡧࡦࡴ࡮ࡰࡶࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡷࡺࡳ࡭ࡢࡴࡼ࠲ࠧႄ"))
      return {}
    logger.debug(bstack1lll11l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠭ႅ"))
    logger.debug(perform_scan(driver, driver_command=bstack1lll11l_opy_ (u"ࠩࡨࡼࡪࡩࡵࡵࡧࡖࡧࡷ࡯ࡰࡵࠩႆ")))
    results = bstack1l1ll1ll1l_opy_(bstack1lll11l_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡖࡹࡲࡳࡡࡳࡻࠥႇ"))
    if results is not None and results.get(bstack1lll11l_opy_ (u"ࠦࡸࡻ࡭࡮ࡣࡵࡽࠧႈ")) is not None:
        return results[bstack1lll11l_opy_ (u"ࠧࡹࡵ࡮࡯ࡤࡶࡾࠨႉ")]
    logger.error(bstack1lll11l_opy_ (u"ࠨࡎࡰࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡕࡩࡸࡻ࡬ࡵࡵࠣࡗࡺࡳ࡭ࡢࡴࡼࠤࡼࡧࡳࠡࡨࡲࡹࡳࡪ࠮ࠣႊ"))
    return {}
  if not bstack111ll1ll_opy_.bstack1111l111l_opy_(CONFIG, bstack11ll11ll1l_opy_) or (bstack11ll11ll11_opy_ and bstack11llll1ll1_opy_):
    logger.warning(bstack1lll11l_opy_ (u"ࠢࡏࡱࡷࠤࡦࡴࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠱ࠦࡣࡢࡰࡱࡳࡹࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻ࠱ࠦႋ"))
    return {}
  try:
    logger.debug(bstack1lll11l_opy_ (u"ࠨࡒࡨࡶ࡫ࡵࡲ࡮࡫ࡱ࡫ࠥࡹࡣࡢࡰࠣࡦࡪ࡬࡯ࡳࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡹࡵ࡮࡯ࡤࡶࡾ࠭ႌ"))
    logger.debug(perform_scan(driver))
    bstack1111lll1l1_opy_ = driver.execute_async_script(bstack11111ll1l_opy_.bstack1l111ll1ll_opy_)
    return bstack1111lll1l1_opy_
  except Exception:
    logger.error(bstack1lll11l_opy_ (u"ࠤࡑࡳࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡵ࡮࡯ࡤࡶࡾࠦࡷࡢࡵࠣࡪࡴࡻ࡮ࡥ࠰ႍࠥ"))
    return {}
def bstack1l1lll11l_opy_():
  global CONFIG
  global bstack11ll11ll1l_opy_
  bstack11llll11l1_opy_ = bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪႎ"), None) and bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ႏ"), None)
  if not bstack111ll1ll_opy_.bstack1111l111l_opy_(CONFIG, bstack11ll11ll1l_opy_) or not bstack11llll11l1_opy_:
        logger.warning(bstack1lll11l_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡶࡪࡹࡵ࡭ࡶࡶ࠲ࠧ႐"))
        return False
  return True
def bstack1l1ll1ll1l_opy_(bstack111l11l111_opy_):
    bstack1111ll111_opy_ = bstack1l111l1l_opy_.current_test_uuid() if bstack1l111l1l_opy_.current_test_uuid() else bstack1l11111l_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack111l1lllll_opy_(bstack1111ll111_opy_, bstack111l11l111_opy_))
        try:
            return future.result(timeout=bstack1l11lll11l_opy_)
        except TimeoutError:
            logger.error(bstack1lll11l_opy_ (u"ࠨࡔࡪ࡯ࡨࡳࡺࡺࠠࡢࡨࡷࡩࡷࠦࡻࡾࡵࠣࡻ࡭࡯࡬ࡦࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡗ࡫ࡳࡶ࡮ࡷࡷࠧ႑").format(bstack1l11lll11l_opy_))
        except Exception as ex:
            logger.debug(bstack1lll11l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡲࡦࡶࡵ࡭ࡪࡼࡩ࡯ࡩࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࢀࢃ࠮ࠡࡇࡵࡶࡴࡸࠠ࠮ࠢࡾࢁࠧ႒").format(bstack111l11l111_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack1l11111ll1_opy_, stage=STAGE.bstack1ll1l1l11_opy_, bstack1l1llll1l_opy_=bstack11ll1lll1_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack11ll11ll1l_opy_
  bstack11llll1ll1_opy_ = not (bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ႓"), None) and bstack1ll111ll_opy_(
          threading.current_thread(), bstack1lll11l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ႔"), None))
  bstack11l1111111_opy_ = not (bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ႕"), None) and bstack1ll111ll_opy_(
          threading.current_thread(), bstack1lll11l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭႖"), None))
  bstack11ll11ll11_opy_ = getattr(driver, bstack1lll11l_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡆ࠷࠱ࡺࡕ࡫ࡳࡺࡲࡤࡔࡥࡤࡲࠬ႗"), None) != True
  if not bstack111ll1ll_opy_.bstack1111l111l_opy_(CONFIG, bstack11ll11ll1l_opy_) or (bstack11ll11ll11_opy_ and bstack11llll1ll1_opy_ and bstack11l1111111_opy_):
    logger.warning(bstack1lll11l_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡵ࡯ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡧࡦࡴ࠮ࠣ႘"))
    return {}
  try:
    bstack11l111ll11_opy_ = bstack1lll11l_opy_ (u"ࠧࡢࡲࡳࠫ႙") in CONFIG and CONFIG.get(bstack1lll11l_opy_ (u"ࠨࡣࡳࡴࠬႚ"), bstack1lll11l_opy_ (u"ࠩࠪႛ"))
    session_id = getattr(driver, bstack1lll11l_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠧႜ"), None)
    if not session_id:
      logger.warning(bstack1lll11l_opy_ (u"ࠦࡓࡵࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡋࡇࠤ࡫ࡵࡵ࡯ࡦࠣࡪࡴࡸࠠࡥࡴ࡬ࡺࡪࡸࠢႝ"))
      return {bstack1lll11l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦ႞"): bstack1lll11l_opy_ (u"ࠨࡎࡰࠢࡶࡩࡸࡹࡩࡰࡰࠣࡍࡉࠦࡦࡰࡷࡱࡨࠧ႟")}
    if bstack11l111ll11_opy_:
      try:
        bstack1111llllll_opy_ = {
              bstack1lll11l_opy_ (u"ࠧࡵࡪࡍࡻࡹ࡚࡯࡬ࡧࡱࠫႠ"): os.environ.get(bstack1lll11l_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭Ⴁ"), os.environ.get(bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ࡛࡙࠭Ⴂ"), bstack1lll11l_opy_ (u"ࠪࠫႣ"))),
              bstack1lll11l_opy_ (u"ࠫࡹ࡮ࡔࡦࡵࡷࡖࡺࡴࡕࡶ࡫ࡧࠫႤ"): bstack1l111l1l_opy_.current_test_uuid() if bstack1l111l1l_opy_.current_test_uuid() else bstack1l11111l_opy_.current_hook_uuid(),
              bstack1lll11l_opy_ (u"ࠬࡧࡵࡵࡪࡋࡩࡦࡪࡥࡳࠩႥ"): os.environ.get(bstack1lll11l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫႦ")),
              bstack1lll11l_opy_ (u"ࠧࡴࡥࡤࡲ࡙࡯࡭ࡦࡵࡷࡥࡲࡶࠧႧ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack1lll11l_opy_ (u"ࠨࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭Ⴈ"): os.environ.get(bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧႩ"), bstack1lll11l_opy_ (u"ࠪࠫႪ")),
              bstack1lll11l_opy_ (u"ࠫࡲ࡫ࡴࡩࡱࡧࠫႫ"): kwargs.get(bstack1lll11l_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤࡩ࡯࡮࡯ࡤࡲࡩ࠭Ⴌ"), None) or bstack1lll11l_opy_ (u"࠭ࠧႭ")
          }
        if not hasattr(thread_local, bstack1lll11l_opy_ (u"ࠧࡣࡣࡶࡩࡤࡧࡰࡱࡡࡤ࠵࠶ࡿ࡟ࡴࡥࡵ࡭ࡵࡺࠧႮ")):
            scripts = {bstack1lll11l_opy_ (u"ࠨࡵࡦࡥࡳ࠭Ⴏ"): bstack11111ll1l_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack111llll1l1_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack111llll1l1_opy_[bstack1lll11l_opy_ (u"ࠩࡶࡧࡦࡴࠧႰ")] = bstack111llll1l1_opy_[bstack1lll11l_opy_ (u"ࠪࡷࡨࡧ࡮ࠨႱ")] % json.dumps(bstack1111llllll_opy_)
        bstack11111ll1l_opy_.bstack1l11llllll_opy_(bstack111llll1l1_opy_)
        bstack11111ll1l_opy_.store()
        bstack111l1ll1l_opy_ = driver.execute_script(bstack11111ll1l_opy_.perform_scan)
      except Exception as bstack111l1lll1_opy_:
        logger.info(bstack1lll11l_opy_ (u"ࠦࡆࡶࡰࡪࡷࡰࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡩࡡ࡯ࠢࡩࡥ࡮ࡲࡥࡥ࠼ࠣࠦႲ") + str(bstack111l1lll1_opy_))
        bstack111l1ll1l_opy_ = {bstack1lll11l_opy_ (u"ࠧ࡫ࡲࡳࡱࡵࠦႳ"): str(bstack111l1lll1_opy_)}
    else:
      bstack111l1ll1l_opy_ = driver.execute_async_script(bstack11111ll1l_opy_.perform_scan, {bstack1lll11l_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭Ⴔ"): kwargs.get(bstack1lll11l_opy_ (u"ࠧࡥࡴ࡬ࡺࡪࡸ࡟ࡤࡱࡰࡱࡦࡴࡤࠨႵ"), None) or bstack1lll11l_opy_ (u"ࠨࠩႶ")})
    return bstack111l1ll1l_opy_
  except Exception as err:
    logger.error(bstack1lll11l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡸࡵ࡯ࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡧࡦࡴ࠮ࠡࡽࢀࠦႷ").format(str(err)))
    return {}