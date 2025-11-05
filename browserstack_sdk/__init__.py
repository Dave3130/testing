# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
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
from browserstack_sdk.bstack1l11l1ll11_opy_ import bstack1l11llllll_opy_
from browserstack_sdk.bstack1ll1lll1l_opy_ import *
import time
import requests
from bstack_utils.constants import EVENTS, STAGE, bstack11llll1l1l_opy_
from bstack_utils.messages import bstack111l1l11l1_opy_, bstack11111lll11_opy_, bstack1l11l1lll1_opy_, bstack1l1lll111l_opy_, bstack1l1l1ll11_opy_, bstack11l1111lll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11111l1ll1_opy_ import get_logger
from bstack_utils.helper import bstack11l111l11_opy_
from browserstack_sdk.bstack1lll1111l_opy_ import bstack1ll1l111l_opy_
logger = get_logger(__name__)
def bstack1l1ll1l1l_opy_():
  global CONFIG
  headers = {
        bstack11ll1ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲ࡺࡹࡱࡧࠪਰ"): bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ਱"),
      }
  proxies = bstack11l111l11_opy_(CONFIG, bstack11llll1l1l_opy_)
  try:
    response = requests.get(bstack11llll1l1l_opy_, headers=headers, proxies=proxies, timeout=5)
    if response.json():
      bstack1l11ll1l11_opy_ = response.json()[bstack11ll1ll_opy_ (u"࠭ࡨࡶࡤࡶࠫਲ")]
      logger.debug(bstack111l1l11l1_opy_.format(response.json()))
      return bstack1l11ll1l11_opy_
    else:
      logger.debug(bstack11111lll11_opy_.format(bstack11ll1ll_opy_ (u"ࠢࡓࡧࡶࡴࡴࡴࡳࡦࠢࡍࡗࡔࡔࠠࡱࡣࡵࡷࡪࠦࡥࡳࡴࡲࡶࠥࠨਲ਼")))
  except Exception as e:
    logger.debug(bstack11111lll11_opy_.format(e))
def bstack1ll1l11111_opy_(hub_url):
  global CONFIG
  url = bstack11ll1ll_opy_ (u"ࠣࡪࡷࡸࡵࡹ࠺࠰࠱ࠥ਴")+  hub_url + bstack11ll1ll_opy_ (u"ࠤ࠲ࡧ࡭࡫ࡣ࡬ࠤਵ")
  headers = {
        bstack11ll1ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩਸ਼"): bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ਷"),
      }
  proxies = bstack11l111l11_opy_(CONFIG, url)
  try:
    start_time = time.perf_counter()
    requests.get(url, headers=headers, proxies=proxies, timeout=5)
    latency = time.perf_counter() - start_time
    logger.debug(bstack1l11l1lll1_opy_.format(hub_url, latency))
    return dict(hub_url=hub_url, latency=latency)
  except Exception as e:
    logger.debug(bstack1l1lll111l_opy_.format(hub_url, e))
@measure(event_name=EVENTS.bstack11ll111111_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
def bstack1111l1lll1_opy_():
  try:
    global bstack11lll11111_opy_
    global CONFIG
    if bstack11ll1ll_opy_ (u"ࠬ࡮ࡵࡣࡔࡨ࡫࡮ࡵ࡮ࠨਸ") in CONFIG and CONFIG[bstack11ll1ll_opy_ (u"࠭ࡨࡶࡤࡕࡩ࡬࡯࡯࡯ࠩਹ")]:
      from bstack_utils.constants import bstack1l1ll1l11_opy_
      bstack11l1lll1l_opy_ = CONFIG[bstack11ll1ll_opy_ (u"ࠧࡩࡷࡥࡖࡪ࡭ࡩࡰࡰࠪ਺")]
      if bstack11l1lll1l_opy_ in bstack1l1ll1l11_opy_:
        bstack11lll11111_opy_ = bstack1l1ll1l11_opy_[bstack11l1lll1l_opy_]
        logger.debug(bstack1l1l1ll11_opy_.format(bstack11lll11111_opy_))
        return
      else:
        logger.debug(bstack11ll1ll_opy_ (u"ࠣࡊࡸࡦࠥࡱࡥࡺࠢࠪࡿࢂ࠭ࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡈࡖࡄࡢ࡙ࡗࡒ࡟ࡎࡃࡓ࠰ࠥ࡬ࡡ࡭࡮࡬ࡲ࡬ࠦࡢࡢࡥ࡮ࠤࡹࡵࠠࡰࡲࡷ࡭ࡲࡧ࡬ࠡࡪࡸࡦࠥࡪࡥࡵࡧࡦࡸ࡮ࡵ࡮ࠣ਻").format(bstack11l1lll1l_opy_))
    bstack1l11ll1l11_opy_ = bstack1l1ll1l1l_opy_()
    bstack11111l1ll_opy_ = []
    results = []
    for bstack111lllll1_opy_ in bstack1l11ll1l11_opy_:
      bstack11111l1ll_opy_.append(bstack1ll1l111l_opy_(target=bstack1ll1l11111_opy_,args=(bstack111lllll1_opy_,)))
    for t in bstack11111l1ll_opy_:
      t.start()
    for t in bstack11111l1ll_opy_:
      results.append(t.join())
    bstack11l111ll1l_opy_ = {}
    for item in results:
      hub_url = item[bstack11ll1ll_opy_ (u"ࠩ࡫ࡹࡧࡥࡵࡳ࡮਼ࠪ")]
      latency = item[bstack11ll1ll_opy_ (u"ࠪࡰࡦࡺࡥ࡯ࡥࡼࠫ਽")]
      bstack11l111ll1l_opy_[hub_url] = latency
    bstack1lll111l11_opy_ = min(bstack11l111ll1l_opy_, key= lambda x: bstack11l111ll1l_opy_[x])
    bstack11lll11111_opy_ = bstack1lll111l11_opy_
    logger.debug(bstack1l1l1ll11_opy_.format(bstack1lll111l11_opy_))
  except Exception as e:
    logger.debug(bstack11l1111lll_opy_.format(e))
from browserstack_sdk.bstack1lllllll1_opy_ import *
from browserstack_sdk.bstack1lll1111l_opy_ import *
from browserstack_sdk.bstack11l1l11l_opy_ import *
import logging
import requests
from bstack_utils.constants import *
from bstack_utils.bstack11111l1ll1_opy_ import get_logger
from bstack_utils.measure import measure
logger = get_logger(__name__)
@measure(event_name=EVENTS.bstack111ll1llll_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
def bstack111ll1l11l_opy_():
    global bstack11lll11111_opy_
    try:
        bstack1111l11ll_opy_ = bstack1l1111111_opy_()
        bstack1l1l1llll1_opy_(bstack1111l11ll_opy_)
        hub_url = bstack1111l11ll_opy_.get(bstack11ll1ll_opy_ (u"ࠦࡺࡸ࡬ࠣਾ"), bstack11ll1ll_opy_ (u"ࠧࠨਿ"))
        if hub_url.endswith(bstack11ll1ll_opy_ (u"࠭࠯ࡸࡦ࠲࡬ࡺࡨࠧੀ")):
            hub_url = hub_url.rsplit(bstack11ll1ll_opy_ (u"ࠧ࠰ࡹࡧ࠳࡭ࡻࡢࠨੁ"), 1)[0]
        if hub_url.startswith(bstack11ll1ll_opy_ (u"ࠨࡪࡷࡸࡵࡀ࠯࠰ࠩੂ")):
            hub_url = hub_url[7:]
        elif hub_url.startswith(bstack11ll1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠫ੃")):
            hub_url = hub_url[8:]
        bstack11lll11111_opy_ = hub_url
    except Exception as e:
        raise RuntimeError(e)
def bstack1l1111111_opy_():
    global CONFIG
    bstack1l1111l111_opy_ = CONFIG.get(bstack11ll1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ੄"), {}).get(bstack11ll1ll_opy_ (u"ࠫ࡬ࡸࡩࡥࡐࡤࡱࡪ࠭੅"), bstack11ll1ll_opy_ (u"ࠬࡔࡏࡠࡉࡕࡍࡉࡥࡎࡂࡏࡈࡣࡕࡇࡓࡔࡇࡇࠫ੆"))
    if not isinstance(bstack1l1111l111_opy_, str):
        raise ValueError(bstack11ll1ll_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡍࡲࡪࡦࠣࡲࡦࡳࡥࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡤࠤࡻࡧ࡬ࡪࡦࠣࡷࡹࡸࡩ࡯ࡩࠥੇ"))
    try:
        bstack1111l11ll_opy_ = bstack1ll1lllll1_opy_(bstack1l1111l111_opy_)
        return bstack1111l11ll_opy_
    except Exception as e:
        logger.error(bstack11ll1ll_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳࠡ࠼ࠣࡿࢂࠨੈ").format(str(e)))
        return {}
def bstack1ll1lllll1_opy_(bstack1l1111l111_opy_):
    global CONFIG
    try:
        if not CONFIG[bstack11ll1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ੉")] or not CONFIG[bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ੊")]:
            raise ValueError(bstack11ll1ll_opy_ (u"ࠥࡑ࡮ࡹࡳࡪࡰࡪࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡹࡸ࡫ࡲ࡯ࡣࡰࡩࠥࡵࡲࠡࡣࡦࡧࡪࡹࡳࠡ࡭ࡨࡽࠧੋ"))
        url = bstack111111111_opy_ + bstack1l1111l111_opy_
        auth = (CONFIG[bstack11ll1ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ੌ")], CONFIG[bstack11ll1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨ੍")])
        response = requests.get(url, auth=auth)
        if response.status_code == 200 and response.text:
            bstack1l1l1lll1l_opy_ = json.loads(response.text)
            return bstack1l1l1lll1l_opy_
    except ValueError as ve:
        logger.error(bstack11ll1ll_opy_ (u"ࠨࡁࡕࡕࠣ࠾ࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡪࡶ࡮ࡪࠠࡥࡧࡷࡥ࡮ࡲࡳࠡ࠼ࠣࡿࢂࠨ੎").format(str(ve)))
        raise ValueError(ve)
    except Exception as e:
        logger.error(bstack11ll1ll_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣ࡫ࡷ࡯ࡤࠡࡦࡨࡸࡦ࡯࡬ࡴࠢ࠽ࠤࢀࢃࠢ੏").format(str(e)))
        raise RuntimeError(e)
    return {}
def bstack1l1l1llll1_opy_(bstack111l1l1l1l_opy_):
    global CONFIG
    if bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ੐") not in CONFIG or str(CONFIG[bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ੑ")]).lower() == bstack11ll1ll_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ੒"):
        CONFIG[bstack11ll1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪ੓")] = False
    elif bstack11ll1ll_opy_ (u"ࠬ࡯ࡳࡕࡴ࡬ࡥࡱࡍࡲࡪࡦࠪ੔") in bstack111l1l1l1l_opy_:
        bstack11111ll1l_opy_ = CONFIG.get(bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ੕"), {})
        logger.debug(bstack11ll1ll_opy_ (u"ࠢࡂࡖࡖࠤ࠿ࠦࡅࡹ࡫ࡶࡸ࡮ࡴࡧࠡ࡮ࡲࡧࡦࡲࠠࡰࡲࡷ࡭ࡴࡴࡳ࠻ࠢࠨࡷࠧ੖"), bstack11111ll1l_opy_)
        bstack11lll1llll_opy_ = bstack111l1l1l1l_opy_.get(bstack11ll1ll_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡓࡧࡳࡩࡦࡺࡥࡳࡵࠥ੗"), [])
        bstack1l1l111l1l_opy_ = bstack11ll1ll_opy_ (u"ࠤ࠯ࠦ੘").join(bstack11lll1llll_opy_)
        logger.debug(bstack11ll1ll_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡆࡹࡸࡺ࡯࡮ࠢࡵࡩࡵ࡫ࡡࡵࡧࡵࠤࡸࡺࡲࡪࡰࡪ࠾ࠥࠫࡳࠣਖ਼"), bstack1l1l111l1l_opy_)
        bstack11l111l11l_opy_ = {
            bstack11ll1ll_opy_ (u"ࠦࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨਗ਼"): bstack11ll1ll_opy_ (u"ࠧࡧࡴࡴ࠯ࡵࡩࡵ࡫ࡡࡵࡧࡵࠦਜ਼"),
            bstack11ll1ll_opy_ (u"ࠨࡦࡰࡴࡦࡩࡑࡵࡣࡢ࡮ࠥੜ"): bstack11ll1ll_opy_ (u"ࠢࡵࡴࡸࡩࠧ੝"),
            bstack11ll1ll_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭࠮ࡴࡨࡴࡪࡧࡴࡦࡴࠥਫ਼"): bstack1l1l111l1l_opy_
        }
        bstack11111ll1l_opy_.update(bstack11l111l11l_opy_)
        logger.debug(bstack11ll1ll_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡗࡳࡨࡦࡺࡥࡥࠢ࡯ࡳࡨࡧ࡬ࠡࡱࡳࡸ࡮ࡵ࡮ࡴ࠼ࠣࠩࡸࠨ੟"), bstack11111ll1l_opy_)
        CONFIG[bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ੠")] = bstack11111ll1l_opy_
        logger.debug(bstack11ll1ll_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡊ࡮ࡴࡡ࡭ࠢࡆࡓࡓࡌࡉࡈ࠼ࠣࠩࡸࠨ੡"), CONFIG)
def bstack1l11lll11_opy_():
    bstack1111l11ll_opy_ = bstack1l1111111_opy_()
    if not bstack1111l11ll_opy_[bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࡗࡵࡰࠬ੢")]:
      raise ValueError(bstack11ll1ll_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡘࡶࡱࠦࡩࡴࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡷࡵ࡭ࠡࡩࡵ࡭ࡩࠦࡤࡦࡶࡤ࡭ࡱࡹ࠮ࠣ੣"))
    return bstack1111l11ll_opy_[bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷ࡙ࡷࡲࠧ੤")] + bstack11ll1ll_opy_ (u"ࠨࡁࡦࡥࡵࡹ࠽ࠨ੥")
@measure(event_name=EVENTS.bstack11ll111ll1_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
def bstack1lllll11ll_opy_() -> list:
    global CONFIG
    result = []
    if CONFIG:
        auth = (CONFIG[bstack11ll1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫ੦")], CONFIG[bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭੧")])
        url = bstack1111l1111l_opy_
        logger.debug(bstack11ll1ll_opy_ (u"ࠦࡆࡺࡴࡦ࡯ࡳࡸ࡮ࡴࡧࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡦࡺ࡯࡬ࡥࡵࠣࡪࡷࡵ࡭ࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡕࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠤࡆࡖࡉࠣ੨"))
        try:
            response = requests.get(url, auth=auth, headers={bstack11ll1ll_opy_ (u"ࠧࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠦ੩"): bstack11ll1ll_opy_ (u"ࠨࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠤ੪")})
            if response.status_code == 200:
                bstack111l1l11ll_opy_ = json.loads(response.text)
                bstack11l1l1111_opy_ = bstack111l1l11ll_opy_.get(bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡹࠧ੫"), [])
                if bstack11l1l1111_opy_:
                    bstack1l1ll1lll1_opy_ = bstack11l1l1111_opy_[0]
                    build_hashed_id = bstack1l1ll1lll1_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫ੬"))
                    bstack11l1ll111l_opy_ = bstack111l111ll1_opy_ + build_hashed_id
                    result.extend([build_hashed_id, bstack11l1ll111l_opy_])
                    logger.info(bstack1ll1ll11l_opy_.format(bstack11l1ll111l_opy_))
                    bstack1l111l11l_opy_ = CONFIG[bstack11ll1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ੭")]
                    if bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ੮") in CONFIG:
                      bstack1l111l11l_opy_ += bstack11ll1ll_opy_ (u"ࠫࠥ࠭੯") + CONFIG[bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧੰ")]
                    if bstack1l111l11l_opy_ != bstack1l1ll1lll1_opy_.get(bstack11ll1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫੱ")):
                      logger.debug(bstack1llll1ll1l_opy_.format(bstack1l1ll1lll1_opy_.get(bstack11ll1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬੲ")), bstack1l111l11l_opy_))
                    return result
                else:
                    logger.debug(bstack11ll1ll_opy_ (u"ࠣࡃࡗࡗࠥࡀࠠࡏࡱࠣࡦࡺ࡯࡬ࡥࡵࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࡺࡨࡦࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠲ࠧੳ"))
            else:
                logger.debug(bstack11ll1ll_opy_ (u"ࠤࡄࡘࡘࠦ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡦࡺ࡯࡬ࡥࡵ࠱ࠦੴ"))
        except Exception as e:
            logger.error(bstack11ll1ll_opy_ (u"ࠥࡅ࡙࡙ࠠ࠻ࠢࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࡷࠥࡀࠠࡼࡿࠥੵ").format(str(e)))
    else:
        logger.debug(bstack11ll1ll_opy_ (u"ࠦࡆ࡚ࡓࠡ࠼ࠣࡇࡔࡔࡆࡊࡉࠣ࡭ࡸࠦ࡮ࡰࡶࠣࡷࡪࡺ࠮ࠡࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡦࡺ࡯࡬ࡥࡵ࠱ࠦ੶"))
    return [None, None]
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.bstack1l1llll11l_opy_ import bstack1l1llll11l_opy_, Events, bstack11l1l1l11l_opy_, bstack1l1ll11ll_opy_
from bstack_utils.measure import bstack111l11l111_opy_
from bstack_utils.measure import measure
from bstack_utils.percy import *
from bstack_utils.percy_sdk import PercySDK
from bstack_utils.bstack1l11llll1l_opy_ import bstack1l1l111l11_opy_
from bstack_utils.messages import *
from bstack_utils import bstack11111l1ll1_opy_
from bstack_utils.constants import *
from bstack_utils.helper import bstack111l1l1lll_opy_, bstack11ll11ll1l_opy_, bstack111l111l11_opy_, bstack1l1l1ll1_opy_, \
  bstack1ll1llll1l_opy_, \
  Notset, bstack1l11lllll_opy_, \
  bstack1ll1l1lll1_opy_, bstack1l1l111ll1_opy_, bstack1l1111111l_opy_, bstack11l1llll11_opy_, bstack1llllll1l1_opy_, bstack1111lll1l1_opy_, \
  bstack1ll11ll111_opy_, \
  bstack11l11ll1l1_opy_, bstack1l111111l1_opy_, bstack11ll1l111_opy_, bstack1l11ll1lll_opy_, \
  bstack1lllllll11_opy_, bstack1ll1l11ll_opy_, bstack11l1ll11l_opy_, bstack11l11ll11l_opy_
from bstack_utils.bstack1l1lll1lll_opy_ import bstack11l1l1l1l1_opy_
from bstack_utils.bstack111111l111_opy_ import bstack1ll111ll1l_opy_, bstack111l11111l_opy_
from bstack_utils.bstack1l1ll11l1l_opy_ import bstack11ll11llll_opy_
from bstack_utils.bstack11111111l_opy_ import bstack11l1l111ll_opy_, bstack1lll111ll1_opy_
from bstack_utils.bstack11lll1l1l_opy_ import bstack11lll1l1l_opy_
from bstack_utils.bstack11l111ll11_opy_ import bstack1ll11l111l_opy_
from bstack_utils.proxy import bstack1l11l1l111_opy_, bstack11l111l11_opy_, bstack1l111ll1ll_opy_, bstack1111lllll_opy_
from bstack_utils.bstack11111ll1l1_opy_ import bstack1ll1l11l11_opy_
import bstack_utils.bstack111111ll1l_opy_ as bstack1111llll11_opy_
import bstack_utils.bstack1ll111ll11_opy_ as bstack111lllllll_opy_
from browserstack_sdk.sdk_cli.cli import cli
from browserstack_sdk.sdk_cli.utils.bstack11ll1111l_opy_ import bstack1lll1l1ll1_opy_
from bstack_utils.bstack1111111l_opy_ import bstack1llllll11_opy_
from bstack_utils.bstack11lll1lll1_opy_ import bstack11llll111l_opy_
if os.getenv(bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡒࡉࡠࡊࡒࡓࡐ࡙ࠧ੷")):
  cli.bstack1lll1l1l11_opy_()
else:
  os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡉࡌࡊࡡࡋࡓࡔࡑࡓࠨ੸")] = bstack11ll1ll_opy_ (u"ࠧࡵࡴࡸࡩࠬ੹")
bstack1ll111lll1_opy_ = bstack11ll1ll_opy_ (u"ࠨࠢࠣ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࠡࠢ࡬ࡪ࠭ࡶࡡࡨࡧࠣࡁࡂࡃࠠࡷࡱ࡬ࡨࠥ࠶ࠩࠡࡽ࡟ࡲࠥࠦࠠࡵࡴࡼࡿࡡࡴࠠࡤࡱࡱࡷࡹࠦࡦࡴࠢࡀࠤࡷ࡫ࡱࡶ࡫ࡵࡩ࠭ࡢࠧࡧࡵ࡟ࠫ࠮ࡁ࡜࡯ࠢࠣࠤࠥࠦࡦࡴ࠰ࡤࡴࡵ࡫࡮ࡥࡈ࡬ࡰࡪ࡙ࡹ࡯ࡥࠫࡦࡸࡺࡡࡤ࡭ࡢࡴࡦࡺࡨ࠭ࠢࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡴࡤ࡯࡮ࡥࡧࡻ࠭ࠥ࠱ࠠࠣ࠼ࠥࠤ࠰ࠦࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡋࡕࡒࡒ࠳ࡶࡡࡳࡵࡨࠬ࠭ࡧࡷࡢ࡫ࡷࠤࡳ࡫ࡷࡑࡣࡪࡩ࠷࠴ࡥࡷࡣ࡯ࡹࡦࡺࡥࠩࠤࠫ࠭ࠥࡃ࠾ࠡࡽࢀࠦ࠱ࠦ࡜ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡩࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡉ࡫ࡴࡢ࡫࡯ࡷࠧࢃ࡜ࠨࠫࠬ࠭ࡠࠨࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠤࡠ࠭ࠥ࠱ࠠࠣ࠮࡟ࡠࡳࠨࠩ࡝ࡰࠣࠤࠥࠦࡽࡤࡣࡷࡧ࡭࠮ࡥࡹࠫࡾࡠࡳࠦࠠࠡࠢࢀࡠࡳࠦࠠࡾ࡞ࡱࠤࠥ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯ࠨ੺")
bstack111lll1ll1_opy_ = bstack11ll1ll_opy_ (u"ࠩ࡟ࡲ࠴࠰ࠠ࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࠤ࠯࠵࡜࡯ࡥࡲࡲࡸࡺࠠࡣࡵࡷࡥࡨࡱ࡟ࡱࡣࡷ࡬ࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻࡡࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠴࡟࡟ࡲࡨࡵ࡮ࡴࡶࠣࡦࡸࡺࡡࡤ࡭ࡢࡧࡦࡶࡳࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠵ࡢࡢ࡮ࡤࡱࡱࡷࡹࠦࡰࡠ࡫ࡱࡨࡪࡾࠠ࠾ࠢࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࡜ࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠵ࡡࡡࡴࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࠥࡃࠠࡱࡴࡲࡧࡪࡹࡳ࠯ࡣࡵ࡫ࡻ࠴ࡳ࡭࡫ࡦࡩ࠭࠶ࠬࠡࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡤࡶ࡬ࡼ࠮࡭ࡧࡱ࡫ࡹ࡮ࠠ࠮ࠢ࠶࠭ࡡࡴࡣࡰࡰࡶࡸࠥ࡯࡭ࡱࡱࡵࡸࡤࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵ࠶ࡢࡦࡸࡺࡡࡤ࡭ࠣࡁࠥࡸࡥࡲࡷ࡬ࡶࡪ࠮ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ࠮ࡁ࡜࡯࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰ࠴ࡣࡩࡴࡲࡱ࡮ࡻ࡭࠯࡮ࡤࡹࡳࡩࡨࠡ࠿ࠣࡥࡸࡿ࡮ࡤࠢࠫࡰࡦࡻ࡮ࡤࡪࡒࡴࡹ࡯࡯࡯ࡵࠬࠤࡂࡄࠠࡼ࡞ࡱࡰࡪࡺࠠࡤࡣࡳࡷࡀࡢ࡮ࡵࡴࡼࠤࢀࡢ࡮ࡤࡣࡳࡷࠥࡃࠠࡋࡕࡒࡒ࠳ࡶࡡࡳࡵࡨࠬࡧࡹࡴࡢࡥ࡮ࡣࡨࡧࡰࡴࠫ࡟ࡲࠥࠦࡽࠡࡥࡤࡸࡨ࡮ࠨࡦࡺࠬࠤࢀࡢ࡮ࠡࠢࠣࠤࢂࡢ࡮ࠡࠢࡵࡩࡹࡻࡲ࡯ࠢࡤࡻࡦ࡯ࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰ࠴ࡣࡩࡴࡲࡱ࡮ࡻ࡭࠯ࡥࡲࡲࡳ࡫ࡣࡵࠪࡾࡠࡳࠦࠠࠡࠢࡺࡷࡊࡴࡤࡱࡱ࡬ࡲࡹࡀࠠࡡࡹࡶࡷ࠿࠵࠯ࡤࡦࡳ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳ࠯ࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࡃࡨࡧࡰࡴ࠿ࠧࡿࡪࡴࡣࡰࡦࡨ࡙ࡗࡏࡃࡰ࡯ࡳࡳࡳ࡫࡮ࡵࠪࡍࡗࡔࡔ࠮ࡴࡶࡵ࡭ࡳ࡭ࡩࡧࡻࠫࡧࡦࡶࡳࠪࠫࢀࡤ࠱ࡢ࡮ࠡࠢࠣࠤ࠳࠴࠮࡭ࡣࡸࡲࡨ࡮ࡏࡱࡶ࡬ࡳࡳࡹ࡜࡯ࠢࠣࢁ࠮ࡢ࡮ࡾ࡞ࡱ࠳࠯ࠦ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࠣ࠮࠴ࡢ࡮ࠨ੻")
from ._version import __version__
bstack1111llll1l_opy_ = None
CONFIG = {}
bstack1lll1l111l_opy_ = {}
bstack111l1llll_opy_ = {}
bstack1111lll11l_opy_ = None
bstack11lll1l111_opy_ = None
bstack11l1l1llll_opy_ = None
bstack11111l11l_opy_ = -1
bstack11ll111ll_opy_ = 0
bstack11l111l1l_opy_ = bstack11l111lll_opy_
bstack1l111l111_opy_ = 1
bstack1llll11l11_opy_ = False
bstack111l111l1_opy_ = False
bstack1lllll1ll1_opy_ = bstack11ll1ll_opy_ (u"ࠪࠫ੼")
bstack11ll1lll1l_opy_ = bstack11ll1ll_opy_ (u"ࠫࠬ੽")
bstack11llll1l1_opy_ = False
bstack1l1ll11l11_opy_ = True
bstack1l1lll1l11_opy_ = bstack11ll1ll_opy_ (u"ࠬ࠭੾")
bstack11l1lll1l1_opy_ = []
bstack11ll11lll_opy_ = threading.Lock()
bstack1l1lll1l1l_opy_ = threading.Lock()
bstack11lll11111_opy_ = bstack11ll1ll_opy_ (u"࠭ࠧ੿")
bstack1l1ll111l1_opy_ = False
bstack11ll1l11l_opy_ = None
bstack1l11ll111_opy_ = None
bstack1l11l1ll1_opy_ = None
bstack1ll1ll111l_opy_ = -1
bstack1l1l1ll111_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠧࡿࠩ઀")), bstack11ll1ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨઁ"), bstack11ll1ll_opy_ (u"ࠩ࠱ࡶࡴࡨ࡯ࡵ࠯ࡵࡩࡵࡵࡲࡵ࠯࡫ࡩࡱࡶࡥࡳ࠰࡭ࡷࡴࡴࠧં"))
bstack11l1l1ll1l_opy_ = 0
bstack1l11lll1l_opy_ = 0
bstack1111ll1l1_opy_ = []
bstack11111ll111_opy_ = []
bstack111lll1lll_opy_ = []
bstack1l1l1111l_opy_ = []
bstack1l1ll1ll1_opy_ = bstack11ll1ll_opy_ (u"ࠪࠫઃ")
bstack11l1ll11ll_opy_ = bstack11ll1ll_opy_ (u"ࠫࠬ઄")
bstack111l11l1ll_opy_ = False
bstack1l1l1111l1_opy_ = False
bstack1l1111l1ll_opy_ = {}
bstack1l1ll1l111_opy_ = None
bstack1l1ll1111l_opy_ = None
bstack1ll111lll_opy_ = None
bstack11ll11ll11_opy_ = None
bstack1l11l11111_opy_ = None
bstack111l111lll_opy_ = None
bstack1ll1l11lll_opy_ = None
bstack1111l11l11_opy_ = None
bstack1ll1l1l1l_opy_ = None
bstack1111ll111_opy_ = None
bstack11lll11l1_opy_ = None
bstack11111llll_opy_ = None
bstack1ll1lll1l1_opy_ = None
bstack111llll1l1_opy_ = None
bstack1ll1l1l111_opy_ = None
bstack111lll11l1_opy_ = None
bstack1lll11111l_opy_ = None
bstack111ll111ll_opy_ = None
bstack1l111l11ll_opy_ = None
bstack1l1llllll_opy_ = None
bstack1l1ll1ll1l_opy_ = None
bstack11lll111l1_opy_ = None
bstack1l1l11lll_opy_ = None
thread_local = threading.local()
bstack1l1111ll1_opy_ = False
bstack1lll111111_opy_ = bstack11ll1ll_opy_ (u"ࠧࠨઅ")
logger = bstack11111l1ll1_opy_.get_logger(__name__, bstack11l111l1l_opy_)
bstack1llllll1l_opy_ = Config.bstack1lll11ll1_opy_()
percy = bstack1ll11l1ll_opy_()
bstack111llllll1_opy_ = bstack1l1l111l11_opy_()
bstack1111l1lll_opy_ = bstack11l1l11l_opy_()
def bstack1ll1llll11_opy_():
  global CONFIG
  global bstack111l11l1ll_opy_
  global bstack1llllll1l_opy_
  testContextOptions = bstack1111ll1l11_opy_(CONFIG)
  if bstack1ll1llll1l_opy_(CONFIG):
    if (bstack11ll1ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨઆ") in testContextOptions and str(testContextOptions[bstack11ll1ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩઇ")]).lower() == bstack11ll1ll_opy_ (u"ࠨࡶࡵࡹࡪ࠭ઈ")):
      bstack111l11l1ll_opy_ = True
    bstack1llllll1l_opy_.bstack1l1l1l111_opy_(testContextOptions.get(bstack11ll1ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭ઉ"), False))
  else:
    bstack111l11l1ll_opy_ = True
    bstack1llllll1l_opy_.bstack1l1l1l111_opy_(True)
def bstack1ll111l111_opy_():
  from appium.version import version as appium_version
  return version.parse(appium_version)
def bstack11llll1111_opy_():
  from selenium import webdriver
  return version.parse(webdriver.__version__)
def bstack11l1l1lll_opy_():
  args = sys.argv
  for i in range(len(args)):
    if bstack11ll1ll_opy_ (u"ࠥ࠱࠲ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡧࡴࡴࡦࡪࡩࡩ࡭ࡱ࡫ࠢઊ") == args[i].lower() or bstack11ll1ll_opy_ (u"ࠦ࠲࠳ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡯ࡨ࡬࡫ࠧઋ") == args[i].lower():
      path = args[i + 1]
      sys.argv.remove(args[i])
      sys.argv.remove(path)
      global bstack1l1lll1l11_opy_
      bstack1l1lll1l11_opy_ += bstack11ll1ll_opy_ (u"ࠬ࠳࠭ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡉ࡯࡯ࡨ࡬࡫ࡋ࡯࡬ࡦࠢࠪઌ") + shlex.quote(path)
      return path
  return None
bstack1ll1l1ll1_opy_ = re.compile(bstack11ll1ll_opy_ (u"ࡸࠢ࠯ࠬࡂࡠࠩࢁࠨ࠯ࠬࡂ࠭ࢂ࠴ࠪࡀࠤઍ"))
def bstack11111ll11_opy_(loader, node):
  value = loader.construct_scalar(node)
  for group in bstack1ll1l1ll1_opy_.findall(value):
    if group is not None and os.environ.get(group) is not None:
      value = value.replace(bstack11ll1ll_opy_ (u"ࠢࠥࡽࠥ઎") + group + bstack11ll1ll_opy_ (u"ࠣࡿࠥએ"), os.environ.get(group))
  return value
def bstack11llll1lll_opy_():
  global bstack1l1l11lll_opy_
  if bstack1l1l11lll_opy_ is None:
        bstack1l1l11lll_opy_ = bstack11l1l1lll_opy_()
  bstack111ll11l1_opy_ = bstack1l1l11lll_opy_
  if bstack111ll11l1_opy_ and os.path.exists(os.path.abspath(bstack111ll11l1_opy_)):
    fileName = bstack111ll11l1_opy_
  if bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࡠࡈࡌࡐࡊ࠭ઐ") in os.environ and os.path.exists(
          os.path.abspath(os.environ[bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡆࡓࡓࡌࡉࡈࡡࡉࡍࡑࡋࠧઑ")])) and not bstack11ll1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡐࡤࡱࡪ࠭઒") in locals():
    fileName = os.environ[bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡈࡕࡎࡇࡋࡊࡣࡋࡏࡌࡆࠩઓ")]
  if bstack11ll1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡒࡦࡳࡥࠨઔ") in locals():
    bstack1111lll_opy_ = os.path.abspath(fileName)
  else:
    bstack1111lll_opy_ = bstack11ll1ll_opy_ (u"ࠧࠨક")
  bstack111l1lllll_opy_ = os.getcwd()
  bstack1ll1111l1_opy_ = bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡺ࡯࡯ࠫખ")
  bstack111lll111l_opy_ = bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡻࡤࡱࡱ࠭ગ")
  while (not os.path.exists(bstack1111lll_opy_)) and bstack111l1lllll_opy_ != bstack11ll1ll_opy_ (u"ࠥࠦઘ"):
    bstack1111lll_opy_ = os.path.join(bstack111l1lllll_opy_, bstack1ll1111l1_opy_)
    if not os.path.exists(bstack1111lll_opy_):
      bstack1111lll_opy_ = os.path.join(bstack111l1lllll_opy_, bstack111lll111l_opy_)
    if bstack111l1lllll_opy_ != os.path.dirname(bstack111l1lllll_opy_):
      bstack111l1lllll_opy_ = os.path.dirname(bstack111l1lllll_opy_)
    else:
      bstack111l1lllll_opy_ = bstack11ll1ll_opy_ (u"ࠦࠧઙ")
  bstack1l1l11lll_opy_ = bstack1111lll_opy_ if os.path.exists(bstack1111lll_opy_) else None
  return bstack1l1l11lll_opy_
def bstack11l1llll1_opy_(config):
    if bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠬચ") in config:
      config[bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪછ")] = config[bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸࡗ࡫ࡰࡰࡴࡷ࡭ࡳ࡭ࠧજ")]
    if bstack11ll1ll_opy_ (u"ࠨࡶࡨࡷࡹࡘࡥࡱࡱࡵࡸ࡮ࡴࡧࡐࡲࡷ࡭ࡴࡴࡳࠨઝ") in config:
      config[bstack11ll1ll_opy_ (u"ࠩࡷࡩࡸࡺࡏࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ઞ")] = config[bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡓࡧࡳࡳࡷࡺࡩ࡯ࡩࡒࡴࡹ࡯࡯࡯ࡵࠪટ")]
def bstack11l111ll1_opy_():
  bstack1111lll_opy_ = bstack11llll1lll_opy_()
  if not os.path.exists(bstack1111lll_opy_):
    bstack1ll1ll11ll_opy_(
      bstack1l11llll11_opy_.format(os.getcwd()))
  try:
    with open(bstack1111lll_opy_, bstack11ll1ll_opy_ (u"ࠫࡷ࠭ઠ")) as stream:
      yaml.add_implicit_resolver(bstack11ll1ll_opy_ (u"ࠧࠧࡰࡢࡶ࡫ࡩࡽࠨડ"), bstack1ll1l1ll1_opy_)
      yaml.add_constructor(bstack11ll1ll_opy_ (u"ࠨࠡࡱࡣࡷ࡬ࡪࡾࠢઢ"), bstack11111ll11_opy_)
      config = yaml.load(stream, yaml.FullLoader)
      bstack11l1llll1_opy_(config)
      return config
  except:
    with open(bstack1111lll_opy_, bstack11ll1ll_opy_ (u"ࠧࡳࠩણ")) as stream:
      try:
        config = yaml.safe_load(stream)
        bstack11l1llll1_opy_(config)
        return config
      except yaml.YAMLError as exc:
        bstack1ll1ll11ll_opy_(bstack11l1ll1ll1_opy_.format(str(exc)))
def bstack111l11l1l1_opy_(config):
  bstack1111l111l1_opy_ = bstack1l1l1l1l1_opy_(config)
  for option in list(bstack1111l111l1_opy_):
    if option.lower() in bstack11ll111l11_opy_ and option != bstack11ll111l11_opy_[option.lower()]:
      bstack1111l111l1_opy_[bstack11ll111l11_opy_[option.lower()]] = bstack1111l111l1_opy_[option]
      del bstack1111l111l1_opy_[option]
  return config
def bstack1l111lllll_opy_():
  global bstack111l1llll_opy_
  for key, bstack11lll1lll_opy_ in bstack1l11lll1l1_opy_.items():
    if isinstance(bstack11lll1lll_opy_, list):
      for var in bstack11lll1lll_opy_:
        if var in os.environ and os.environ[var] and str(os.environ[var]).strip():
          bstack111l1llll_opy_[key] = os.environ[var]
          break
    elif bstack11lll1lll_opy_ in os.environ and os.environ[bstack11lll1lll_opy_] and str(os.environ[bstack11lll1lll_opy_]).strip():
      bstack111l1llll_opy_[key] = os.environ[bstack11lll1lll_opy_]
  if bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪત") in os.environ:
    bstack111l1llll_opy_[bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭થ")] = {}
    bstack111l1llll_opy_[bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧદ")][bstack11ll1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ધ")] = os.environ[bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧન")]
def bstack111ll11ll_opy_():
  global bstack1lll1l111l_opy_
  global bstack1l1lll1l11_opy_
  bstack1ll11ll11l_opy_ = []
  for idx, val in enumerate(sys.argv):
    if idx < len(sys.argv) - 1 and bstack11ll1ll_opy_ (u"࠭࠭࠮ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ઩").lower() == val.lower():
      bstack1lll1l111l_opy_[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫપ")] = {}
      bstack1lll1l111l_opy_[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬફ")][bstack11ll1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫબ")] = sys.argv[idx + 1]
      bstack1ll11ll11l_opy_.extend([idx, idx + 1])
      break
  for key, bstack11l11l11ll_opy_ in bstack1111l1ll1l_opy_.items():
    if isinstance(bstack11l11l11ll_opy_, list):
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        for var in bstack11l11l11ll_opy_:
          if bstack11ll1ll_opy_ (u"ࠪ࠱࠲࠭ભ") + var.lower() == val.lower() and key not in bstack1lll1l111l_opy_:
            bstack1lll1l111l_opy_[key] = sys.argv[idx + 1]
            bstack1l1lll1l11_opy_ += bstack11ll1ll_opy_ (u"ࠫࠥ࠳࠭ࠨમ") + var + bstack11ll1ll_opy_ (u"ࠬࠦࠧય") + shlex.quote(sys.argv[idx + 1])
            bstack1ll11ll11l_opy_.extend([idx, idx + 1])
            break
    else:
      for idx, val in enumerate(sys.argv):
        if idx >= len(sys.argv) - 1:
          continue
        if bstack11ll1ll_opy_ (u"࠭࠭࠮ࠩર") + bstack11l11l11ll_opy_.lower() == val.lower() and key not in bstack1lll1l111l_opy_:
          bstack1lll1l111l_opy_[key] = sys.argv[idx + 1]
          bstack1l1lll1l11_opy_ += bstack11ll1ll_opy_ (u"ࠧࠡ࠯࠰ࠫ઱") + bstack11l11l11ll_opy_ + bstack11ll1ll_opy_ (u"ࠨࠢࠪલ") + shlex.quote(sys.argv[idx + 1])
          bstack1ll11ll11l_opy_.extend([idx, idx + 1])
  for idx in sorted(set(bstack1ll11ll11l_opy_), reverse=True):
    if idx < len(sys.argv):
      del sys.argv[idx]
def bstack1ll111l11_opy_(config):
  bstack1ll11ll1l_opy_ = config.keys()
  for bstack11l11l11l1_opy_, bstack1llll1llll_opy_ in bstack1ll11l1l11_opy_.items():
    if bstack1llll1llll_opy_ in bstack1ll11ll1l_opy_:
      config[bstack11l11l11l1_opy_] = config[bstack1llll1llll_opy_]
      del config[bstack1llll1llll_opy_]
  for bstack11l11l11l1_opy_, bstack1llll1llll_opy_ in bstack111l1l111_opy_.items():
    if isinstance(bstack1llll1llll_opy_, list):
      for bstack1111l1llll_opy_ in bstack1llll1llll_opy_:
        if bstack1111l1llll_opy_ in bstack1ll11ll1l_opy_:
          config[bstack11l11l11l1_opy_] = config[bstack1111l1llll_opy_]
          del config[bstack1111l1llll_opy_]
          break
    elif bstack1llll1llll_opy_ in bstack1ll11ll1l_opy_:
      config[bstack11l11l11l1_opy_] = config[bstack1llll1llll_opy_]
      del config[bstack1llll1llll_opy_]
  for bstack1111l1llll_opy_ in list(config):
    for bstack1lll1ll1ll_opy_ in bstack1l1l1l11ll_opy_:
      if bstack1111l1llll_opy_.lower() == bstack1lll1ll1ll_opy_.lower() and bstack1111l1llll_opy_ != bstack1lll1ll1ll_opy_:
        config[bstack1lll1ll1ll_opy_] = config[bstack1111l1llll_opy_]
        del config[bstack1111l1llll_opy_]
  bstack1ll11111l1_opy_ = [{}]
  if not config.get(bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬળ")):
    config[bstack11ll1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭઴")] = [{}]
  bstack1ll11111l1_opy_ = config[bstack11ll1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧવ")]
  for platform in bstack1ll11111l1_opy_:
    for bstack1111l1llll_opy_ in list(platform):
      for bstack1lll1ll1ll_opy_ in bstack1l1l1l11ll_opy_:
        if bstack1111l1llll_opy_.lower() == bstack1lll1ll1ll_opy_.lower() and bstack1111l1llll_opy_ != bstack1lll1ll1ll_opy_:
          platform[bstack1lll1ll1ll_opy_] = platform[bstack1111l1llll_opy_]
          del platform[bstack1111l1llll_opy_]
  for bstack11l11l11l1_opy_, bstack1llll1llll_opy_ in bstack111l1l111_opy_.items():
    for platform in bstack1ll11111l1_opy_:
      if isinstance(bstack1llll1llll_opy_, list):
        for bstack1111l1llll_opy_ in bstack1llll1llll_opy_:
          if bstack1111l1llll_opy_ in platform:
            platform[bstack11l11l11l1_opy_] = platform[bstack1111l1llll_opy_]
            del platform[bstack1111l1llll_opy_]
            break
      elif bstack1llll1llll_opy_ in platform:
        platform[bstack11l11l11l1_opy_] = platform[bstack1llll1llll_opy_]
        del platform[bstack1llll1llll_opy_]
  for bstack1lll111l1l_opy_ in bstack11llllll11_opy_:
    if bstack1lll111l1l_opy_ in config:
      if not bstack11llllll11_opy_[bstack1lll111l1l_opy_] in config:
        config[bstack11llllll11_opy_[bstack1lll111l1l_opy_]] = {}
      config[bstack11llllll11_opy_[bstack1lll111l1l_opy_]].update(config[bstack1lll111l1l_opy_])
      del config[bstack1lll111l1l_opy_]
  for platform in bstack1ll11111l1_opy_:
    for bstack1lll111l1l_opy_ in bstack11llllll11_opy_:
      if bstack1lll111l1l_opy_ in list(platform):
        if not bstack11llllll11_opy_[bstack1lll111l1l_opy_] in platform:
          platform[bstack11llllll11_opy_[bstack1lll111l1l_opy_]] = {}
        platform[bstack11llllll11_opy_[bstack1lll111l1l_opy_]].update(platform[bstack1lll111l1l_opy_])
        del platform[bstack1lll111l1l_opy_]
  config = bstack111l11l1l1_opy_(config)
  return config
def bstack11l1l11l1l_opy_(config):
  global bstack11ll1lll1l_opy_
  bstack1l111l1111_opy_ = False
  if bstack11ll1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩશ") in config and str(config[bstack11ll1ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪષ")]).lower() != bstack11ll1ll_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭સ"):
    if bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬહ") not in config or str(config[bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭઺")]).lower() == bstack11ll1ll_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ઻"):
      config[bstack11ll1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮઼ࠪ")] = False
    else:
      bstack1111l11ll_opy_ = bstack1l1111111_opy_()
      if bstack11ll1ll_opy_ (u"ࠬ࡯ࡳࡕࡴ࡬ࡥࡱࡍࡲࡪࡦࠪઽ") in bstack1111l11ll_opy_:
        if not bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪા") in config:
          config[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫિ")] = {}
        config[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬી")][bstack11ll1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫુ")] = bstack11ll1ll_opy_ (u"ࠪࡥࡹࡹ࠭ࡳࡧࡳࡩࡦࡺࡥࡳࠩૂ")
        bstack1l111l1111_opy_ = True
        bstack11ll1lll1l_opy_ = config[bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨૃ")].get(bstack11ll1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧૄ"))
  if bstack1ll1llll1l_opy_(config) and bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪૅ") in config and str(config[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫ૆")]).lower() != bstack11ll1ll_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧે") and not bstack1l111l1111_opy_:
    if not bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ૈ") in config:
      config[bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧૉ")] = {}
    if not config[bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ૊")].get(bstack11ll1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠩો")) and not bstack11ll1ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨૌ") in config[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶ્ࠫ")]:
      bstack1ll111ll_opy_ = datetime.datetime.now()
      bstack111llllll_opy_ = bstack1ll111ll_opy_.strftime(bstack11ll1ll_opy_ (u"ࠨࠧࡧࡣࠪࡨ࡟ࠦࡊࠨࡑࠬ૎"))
      hostname = socket.gethostname()
      bstack1l1llll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠩࠪ૏").join(random.choices(string.ascii_lowercase + string.digits, k=4))
      identifier = bstack11ll1ll_opy_ (u"ࠪࡿࢂࡥࡻࡾࡡࡾࢁࠬૐ").format(bstack111llllll_opy_, hostname, bstack1l1llll1ll_opy_)
      config[bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ૑")][bstack11ll1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૒")] = identifier
    bstack11ll1lll1l_opy_ = config[bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ૓")].get(bstack11ll1ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ૔"))
  return config
def bstack111l1ll1ll_opy_():
  bstack111l11111_opy_ =  bstack11l1llll11_opy_()[bstack11ll1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠧ૕")]
  return bstack111l11111_opy_ if bstack111l11111_opy_ else -1
def bstack111ll1l1l_opy_(bstack111l11111_opy_):
  global CONFIG
  if not bstack11ll1ll_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫ૖") in CONFIG[bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૗")]:
    return
  CONFIG[bstack11ll1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૘")] = CONFIG[bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૙")].replace(
    bstack11ll1ll_opy_ (u"࠭ࠤࡼࡄࡘࡍࡑࡊ࡟ࡏࡗࡐࡆࡊࡘࡽࠨ૚"),
    str(bstack111l11111_opy_)
  )
def bstack111l11ll1l_opy_():
  global CONFIG
  if not bstack11ll1ll_opy_ (u"ࠧࠥࡽࡇࡅ࡙ࡋ࡟ࡕࡋࡐࡉࢂ࠭૛") in CONFIG[bstack11ll1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૜")]:
    return
  bstack1ll111ll_opy_ = datetime.datetime.now()
  bstack111llllll_opy_ = bstack1ll111ll_opy_.strftime(bstack11ll1ll_opy_ (u"ࠩࠨࡨ࠲ࠫࡢ࠮ࠧࡋ࠾ࠪࡓࠧ૝"))
  CONFIG[bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૞")] = CONFIG[bstack11ll1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭૟")].replace(
    bstack11ll1ll_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫૠ"),
    bstack111llllll_opy_
  )
def bstack1lll1l1l1l_opy_():
  global CONFIG
  if bstack11ll1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨૡ") in CONFIG and not bool(CONFIG[bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩૢ")]):
    del CONFIG[bstack11ll1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪૣ")]
    return
  if not bstack11ll1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૤") in CONFIG:
    CONFIG[bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૥")] = bstack11ll1ll_opy_ (u"ࠫࠨࠪࡻࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࢃࠧ૦")
  if bstack11ll1ll_opy_ (u"ࠬࠪࡻࡅࡃࡗࡉࡤ࡚ࡉࡎࡇࢀࠫ૧") in CONFIG[bstack11ll1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ૨")]:
    bstack111l11ll1l_opy_()
    os.environ[bstack11ll1ll_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑ࡟ࡄࡑࡐࡆࡎࡔࡅࡅࡡࡅ࡙ࡎࡒࡄࡠࡋࡇࠫ૩")] = CONFIG[bstack11ll1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ૪")]
  if not bstack11ll1ll_opy_ (u"ࠩࠧࡿࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࢀࠫ૫") in CONFIG[bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ૬")]:
    return
  bstack111l11111_opy_ = bstack11ll1ll_opy_ (u"ࠫࠬ૭")
  bstack11lll11ll1_opy_ = bstack111l1ll1ll_opy_()
  if bstack11lll11ll1_opy_ != -1:
    bstack111l11111_opy_ = bstack11ll1ll_opy_ (u"ࠬࡉࡉࠡࠩ૮") + str(bstack11lll11ll1_opy_)
  if bstack111l11111_opy_ == bstack11ll1ll_opy_ (u"࠭ࠧ૯"):
    bstack1ll1llllll_opy_ = bstack11111l1l1l_opy_(CONFIG[bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ૰")])
    if bstack1ll1llllll_opy_ != -1:
      bstack111l11111_opy_ = str(bstack1ll1llllll_opy_)
  if bstack111l11111_opy_:
    bstack111ll1l1l_opy_(bstack111l11111_opy_)
    os.environ[bstack11ll1ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡠࡅࡒࡑࡇࡏࡎࡆࡆࡢࡆ࡚ࡏࡌࡅࡡࡌࡈࠬ૱")] = CONFIG[bstack11ll1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૲")]
def bstack1ll1ll11l1_opy_(bstack111111l11_opy_, bstack1l1lll1111_opy_, path):
  json_data = {
    bstack11ll1ll_opy_ (u"ࠪ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ૳"): bstack1l1lll1111_opy_
  }
  if os.path.exists(path):
    bstack1l1llll1l1_opy_ = json.load(open(path, bstack11ll1ll_opy_ (u"ࠫࡷࡨࠧ૴")))
  else:
    bstack1l1llll1l1_opy_ = {}
  bstack1l1llll1l1_opy_[bstack111111l11_opy_] = json_data
  with open(path, bstack11ll1ll_opy_ (u"ࠧࡽࠫࠣ૵")) as outfile:
    json.dump(bstack1l1llll1l1_opy_, outfile)
def bstack11111l1l1l_opy_(bstack111111l11_opy_):
  bstack111111l11_opy_ = str(bstack111111l11_opy_)
  bstack1l111lll11_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"࠭ࡾࠨ૶")), bstack11ll1ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ૷"))
  try:
    if not os.path.exists(bstack1l111lll11_opy_):
      os.makedirs(bstack1l111lll11_opy_)
    file_path = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠨࢀࠪ૸")), bstack11ll1ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩૹ"), bstack11ll1ll_opy_ (u"ࠪ࠲ࡧࡻࡩ࡭ࡦ࠰ࡲࡦࡳࡥ࠮ࡥࡤࡧ࡭࡫࠮࡫ࡵࡲࡲࠬૺ"))
    if not os.path.isfile(file_path):
      with open(file_path, bstack11ll1ll_opy_ (u"ࠫࡼ࠭ૻ")):
        pass
      with open(file_path, bstack11ll1ll_opy_ (u"ࠧࡽࠫࠣૼ")) as outfile:
        json.dump({}, outfile)
    with open(file_path, bstack11ll1ll_opy_ (u"࠭ࡲࠨ૽")) as bstack1l11lllll1_opy_:
      bstack11l1lll1ll_opy_ = json.load(bstack1l11lllll1_opy_)
    if bstack111111l11_opy_ in bstack11l1lll1ll_opy_:
      bstack1l1lll1ll_opy_ = bstack11l1lll1ll_opy_[bstack111111l11_opy_][bstack11ll1ll_opy_ (u"ࠧࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ૾")]
      bstack1111l1l1l_opy_ = int(bstack1l1lll1ll_opy_) + 1
      bstack1ll1ll11l1_opy_(bstack111111l11_opy_, bstack1111l1l1l_opy_, file_path)
      return bstack1111l1l1l_opy_
    else:
      bstack1ll1ll11l1_opy_(bstack111111l11_opy_, 1, file_path)
      return 1
  except Exception as e:
    logger.warn(bstack1llll1111l_opy_.format(str(e)))
    return -1
def bstack11llll11l_opy_(config):
  if not config[bstack11ll1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ૿")] or not config[bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ଀")]:
    return True
  else:
    return False
def bstack11l1l1l111_opy_(config, index=0):
  global bstack11llll1l1_opy_
  bstack1l111l1l11_opy_ = {}
  caps = bstack11ll1llll1_opy_ + bstack1l11111ll1_opy_
  if config.get(bstack11ll1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧଁ"), False):
    bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨଂ")] = True
    bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩଃ")] = config.get(bstack11ll1ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ଄"), {})
  if bstack11llll1l1_opy_:
    caps += bstack1llll1l11l_opy_
  for key in config:
    if key in caps + [bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଅ")]:
      continue
    bstack1l111l1l11_opy_[key] = config[key]
  if bstack11ll1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଆ") in config:
    for bstack1lll1l11l1_opy_ in config[bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଇ")][index]:
      if bstack1lll1l11l1_opy_ in caps:
        continue
      bstack1l111l1l11_opy_[bstack1lll1l11l1_opy_] = config[bstack11ll1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଈ")][index][bstack1lll1l11l1_opy_]
  bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"ࠫ࡭ࡵࡳࡵࡐࡤࡱࡪ࠭ଉ")] = socket.gethostname()
  if bstack11ll1ll_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ଊ") in bstack1l111l1l11_opy_:
    del (bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧଋ")])
  return bstack1l111l1l11_opy_
def bstack11lll1l1l1_opy_(config):
  global bstack11llll1l1_opy_
  bstack111l1111l_opy_ = {}
  caps = bstack1l11111ll1_opy_
  if bstack11llll1l1_opy_:
    caps += bstack1llll1l11l_opy_
  for key in caps:
    if key in config:
      bstack111l1111l_opy_[key] = config[key]
  return bstack111l1111l_opy_
def bstack111l1l1ll1_opy_(bstack1l111l1l11_opy_, bstack111l1111l_opy_):
  bstack1lllll11l1_opy_ = {}
  for key in bstack1l111l1l11_opy_.keys():
    if key in bstack1ll11l1l11_opy_:
      bstack1lllll11l1_opy_[bstack1ll11l1l11_opy_[key]] = bstack1l111l1l11_opy_[key]
    else:
      bstack1lllll11l1_opy_[key] = bstack1l111l1l11_opy_[key]
  for key in bstack111l1111l_opy_:
    if key in bstack1ll11l1l11_opy_:
      bstack1lllll11l1_opy_[bstack1ll11l1l11_opy_[key]] = bstack111l1111l_opy_[key]
    else:
      bstack1lllll11l1_opy_[key] = bstack111l1111l_opy_[key]
  return bstack1lllll11l1_opy_
def bstack1ll111llll_opy_(config, index=0):
  global bstack11llll1l1_opy_
  caps = {}
  config = copy.deepcopy(config)
  bstack1l1111llll_opy_ = bstack111l1l1lll_opy_(bstack1l1l1l1111_opy_, config, logger)
  bstack111l1111l_opy_ = bstack11lll1l1l1_opy_(config)
  bstack11l11ll1l_opy_ = bstack1l11111ll1_opy_
  bstack11l11ll1l_opy_ += bstack11lll11l1l_opy_
  bstack111l1111l_opy_ = update(bstack111l1111l_opy_, bstack1l1111llll_opy_)
  if bstack11llll1l1_opy_:
    bstack11l11ll1l_opy_ += bstack1llll1l11l_opy_
  if bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଌ") in config:
    if bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭଍") in config[bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ଎")][index]:
      caps[bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨଏ")] = config[bstack11ll1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଐ")][index][bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ଑")]
    if bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ଒") in config[bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଓ")][index]:
      caps[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩଔ")] = str(config[bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬକ")][index][bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫଖ")])
    bstack11111lll1_opy_ = bstack111l1l1lll_opy_(bstack1l1l1l1111_opy_, config[bstack11ll1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧଗ")][index], logger)
    bstack11l11ll1l_opy_ += list(bstack11111lll1_opy_.keys())
    for bstack111lll1l1_opy_ in bstack11l11ll1l_opy_:
      if bstack111lll1l1_opy_ in config[bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨଘ")][index]:
        if bstack111lll1l1_opy_ == bstack11ll1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨଙ"):
          try:
            bstack11111lll1_opy_[bstack111lll1l1_opy_] = str(config[bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪଚ")][index][bstack111lll1l1_opy_] * 1.0)
          except:
            bstack11111lll1_opy_[bstack111lll1l1_opy_] = str(config[bstack11ll1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫଛ")][index][bstack111lll1l1_opy_])
        else:
          bstack11111lll1_opy_[bstack111lll1l1_opy_] = config[bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬଜ")][index][bstack111lll1l1_opy_]
        del (config[bstack11ll1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ଝ")][index][bstack111lll1l1_opy_])
    bstack111l1111l_opy_ = update(bstack111l1111l_opy_, bstack11111lll1_opy_)
  bstack1l111l1l11_opy_ = bstack11l1l1l111_opy_(config, index)
  for bstack1111l1llll_opy_ in bstack1l11111ll1_opy_ + list(bstack1l1111llll_opy_.keys()):
    if bstack1111l1llll_opy_ in bstack1l111l1l11_opy_:
      bstack111l1111l_opy_[bstack1111l1llll_opy_] = bstack1l111l1l11_opy_[bstack1111l1llll_opy_]
      del (bstack1l111l1l11_opy_[bstack1111l1llll_opy_])
  if bstack1l11lllll_opy_(config):
    bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"ࠫࡺࡹࡥࡘ࠵ࡆࠫଞ")] = True
    caps.update(bstack111l1111l_opy_)
    caps[bstack11ll1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ଟ")] = bstack1l111l1l11_opy_
  else:
    bstack1l111l1l11_opy_[bstack11ll1ll_opy_ (u"࠭ࡵࡴࡧ࡚࠷ࡈ࠭ଠ")] = False
    caps.update(bstack111l1l1ll1_opy_(bstack1l111l1l11_opy_, bstack111l1111l_opy_))
    if bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬଡ") in caps:
      caps[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩଢ")] = caps[bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧଣ")]
      del (caps[bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨତ")])
    if bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬଥ") in caps:
      caps[bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧଦ")] = caps[bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧଧ")]
      del (caps[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨନ")])
  return caps
def bstack111l1l1111_opy_():
  global bstack11lll11111_opy_
  global CONFIG
  if bstack11llll1111_opy_() <= version.parse(bstack11ll1ll_opy_ (u"ࠨ࠵࠱࠵࠸࠴࠰ࠨ଩")):
    if bstack11lll11111_opy_ != bstack11ll1ll_opy_ (u"ࠩࠪପ"):
      return bstack11ll1ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦଫ") + bstack11lll11111_opy_ + bstack11ll1ll_opy_ (u"ࠦ࠿࠾࠰࠰ࡹࡧ࠳࡭ࡻࡢࠣବ")
    return bstack1l1l1lllll_opy_
  if bstack11lll11111_opy_ != bstack11ll1ll_opy_ (u"ࠬ࠭ଭ"):
    return bstack11ll1ll_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࠣମ") + bstack11lll11111_opy_ + bstack11ll1ll_opy_ (u"ࠢ࠰ࡹࡧ࠳࡭ࡻࡢࠣଯ")
  return bstack11lll111ll_opy_
def bstack1l1l1lll11_opy_(options):
  return hasattr(options, bstack11ll1ll_opy_ (u"ࠨࡵࡨࡸࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡺࠩର"))
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
def bstack111111l11l_opy_(options, bstack1l111llll1_opy_):
  for bstack111ll11l1l_opy_ in bstack1l111llll1_opy_:
    if bstack111ll11l1l_opy_ in [bstack11ll1ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ଱"), bstack11ll1ll_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧଲ")]:
      continue
    if bstack111ll11l1l_opy_ in options._experimental_options:
      options._experimental_options[bstack111ll11l1l_opy_] = update(options._experimental_options[bstack111ll11l1l_opy_],
                                                         bstack1l111llll1_opy_[bstack111ll11l1l_opy_])
    else:
      options.add_experimental_option(bstack111ll11l1l_opy_, bstack1l111llll1_opy_[bstack111ll11l1l_opy_])
  if bstack11ll1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩଳ") in bstack1l111llll1_opy_:
    for arg in bstack1l111llll1_opy_[bstack11ll1ll_opy_ (u"ࠬࡧࡲࡨࡵࠪ଴")]:
      options.add_argument(arg)
    del (bstack1l111llll1_opy_[bstack11ll1ll_opy_ (u"࠭ࡡࡳࡩࡶࠫଵ")])
  if bstack11ll1ll_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫଶ") in bstack1l111llll1_opy_:
    for ext in bstack1l111llll1_opy_[bstack11ll1ll_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬଷ")]:
      try:
        options.add_extension(ext)
      except OSError:
        options.add_encoded_extension(ext)
    del (bstack1l111llll1_opy_[bstack11ll1ll_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ସ")])
def bstack11ll1l11ll_opy_(options, bstack1l11ll11l_opy_):
  if bstack11ll1ll_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩହ") in bstack1l11ll11l_opy_:
    for bstack11ll1ll11l_opy_ in bstack1l11ll11l_opy_[bstack11ll1ll_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ଺")]:
      if bstack11ll1ll11l_opy_ in options._preferences:
        options._preferences[bstack11ll1ll11l_opy_] = update(options._preferences[bstack11ll1ll11l_opy_], bstack1l11ll11l_opy_[bstack11ll1ll_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ଻")][bstack11ll1ll11l_opy_])
      else:
        options.set_preference(bstack11ll1ll11l_opy_, bstack1l11ll11l_opy_[bstack11ll1ll_opy_ (u"࠭ࡰࡳࡧࡩࡷ଼ࠬ")][bstack11ll1ll11l_opy_])
  if bstack11ll1ll_opy_ (u"ࠧࡢࡴࡪࡷࠬଽ") in bstack1l11ll11l_opy_:
    for arg in bstack1l11ll11l_opy_[bstack11ll1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ା")]:
      options.add_argument(arg)
def bstack1l1111l11l_opy_(options, bstack11l1llllll_opy_):
  if bstack11ll1ll_opy_ (u"ࠩࡺࡩࡧࡼࡩࡦࡹࠪି") in bstack11l1llllll_opy_:
    options.use_webview(bool(bstack11l1llllll_opy_[bstack11ll1ll_opy_ (u"ࠪࡻࡪࡨࡶࡪࡧࡺࠫୀ")]))
  bstack111111l11l_opy_(options, bstack11l1llllll_opy_)
def bstack1ll1111l1l_opy_(options, bstack11ll1l1111_opy_):
  for bstack111l11l1l_opy_ in bstack11ll1l1111_opy_:
    if bstack111l11l1l_opy_ in [bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡣࡩࡰࡲࡰࡴ࡭ࡹࡑࡴࡨࡺ࡮࡫ࡷࠨୁ"), bstack11ll1ll_opy_ (u"ࠬࡧࡲࡨࡵࠪୂ")]:
      continue
    options.set_capability(bstack111l11l1l_opy_, bstack11ll1l1111_opy_[bstack111l11l1l_opy_])
  if bstack11ll1ll_opy_ (u"࠭ࡡࡳࡩࡶࠫୃ") in bstack11ll1l1111_opy_:
    for arg in bstack11ll1l1111_opy_[bstack11ll1ll_opy_ (u"ࠧࡢࡴࡪࡷࠬୄ")]:
      options.add_argument(arg)
  if bstack11ll1ll_opy_ (u"ࠨࡶࡨࡧ࡭ࡴ࡯࡭ࡱࡪࡽࡕࡸࡥࡷ࡫ࡨࡻࠬ୅") in bstack11ll1l1111_opy_:
    options.bstack1llll11l1l_opy_(bool(bstack11ll1l1111_opy_[bstack11ll1ll_opy_ (u"ࠩࡷࡩࡨ࡮࡮ࡰ࡮ࡲ࡫ࡾࡖࡲࡦࡸ࡬ࡩࡼ࠭୆")]))
def bstack11l1l11ll_opy_(options, bstack11ll1ll1l1_opy_):
  for bstack1ll1l1lll_opy_ in bstack11ll1ll1l1_opy_:
    if bstack1ll1l1lll_opy_ in [bstack11ll1ll_opy_ (u"ࠪࡥࡩࡪࡩࡵ࡫ࡲࡲࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧେ"), bstack11ll1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩୈ")]:
      continue
    options._options[bstack1ll1l1lll_opy_] = bstack11ll1ll1l1_opy_[bstack1ll1l1lll_opy_]
  if bstack11ll1ll_opy_ (u"ࠬࡧࡤࡥ࡫ࡷ࡭ࡴࡴࡡ࡭ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୉") in bstack11ll1ll1l1_opy_:
    for bstack1lll11l1l1_opy_ in bstack11ll1ll1l1_opy_[bstack11ll1ll_opy_ (u"࠭ࡡࡥࡦ࡬ࡸ࡮ࡵ࡮ࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪ୊")]:
      options.bstack1lll1lllll_opy_(
        bstack1lll11l1l1_opy_, bstack11ll1ll1l1_opy_[bstack11ll1ll_opy_ (u"ࠧࡢࡦࡧ࡭ࡹ࡯࡯࡯ࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫୋ")][bstack1lll11l1l1_opy_])
  if bstack11ll1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭ୌ") in bstack11ll1ll1l1_opy_:
    for arg in bstack11ll1ll1l1_opy_[bstack11ll1ll_opy_ (u"ࠩࡤࡶ࡬ࡹ୍ࠧ")]:
      options.add_argument(arg)
def bstack11l1l11l11_opy_(options, caps):
  if not hasattr(options, bstack11ll1ll_opy_ (u"ࠪࡏࡊ࡟ࠧ୎")):
    return
  if options.KEY == bstack11ll1ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ୏"):
    options = bstack1lll11l11_opy_.bstack1ll1lll11l_opy_(bstack111ll1lll1_opy_=options, config=CONFIG)
  if options.KEY == bstack11ll1ll_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ୐") and options.KEY in caps:
    bstack111111l11l_opy_(options, caps[bstack11ll1ll_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ୑")])
  elif options.KEY == bstack11ll1ll_opy_ (u"ࠧ࡮ࡱࡽ࠾࡫࡯ࡲࡦࡨࡲࡼࡔࡶࡴࡪࡱࡱࡷࠬ୒") and options.KEY in caps:
    bstack11ll1l11ll_opy_(options, caps[bstack11ll1ll_opy_ (u"ࠨ࡯ࡲࡾ࠿࡬ࡩࡳࡧࡩࡳࡽࡕࡰࡵ࡫ࡲࡲࡸ࠭୓")])
  elif options.KEY == bstack11ll1ll_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪ࠰ࡲࡴࡹ࡯࡯࡯ࡵࠪ୔") and options.KEY in caps:
    bstack1ll1111l1l_opy_(options, caps[bstack11ll1ll_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫࠱ࡳࡵࡺࡩࡰࡰࡶࠫ୕")])
  elif options.KEY == bstack11ll1ll_opy_ (u"ࠫࡲࡹ࠺ࡦࡦࡪࡩࡔࡶࡴࡪࡱࡱࡷࠬୖ") and options.KEY in caps:
    bstack1l1111l11l_opy_(options, caps[bstack11ll1ll_opy_ (u"ࠬࡳࡳ࠻ࡧࡧ࡫ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ୗ")])
  elif options.KEY == bstack11ll1ll_opy_ (u"࠭ࡳࡦ࠼࡬ࡩࡔࡶࡴࡪࡱࡱࡷࠬ୘") and options.KEY in caps:
    bstack11l1l11ll_opy_(options, caps[bstack11ll1ll_opy_ (u"ࠧࡴࡧ࠽࡭ࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭୙")])
def bstack1ll1ll1ll1_opy_(caps):
  global bstack11llll1l1_opy_
  if isinstance(os.environ.get(bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡊࡕࡢࡅࡕࡖ࡟ࡂࡗࡗࡓࡒࡇࡔࡆࠩ୚")), str):
    bstack11llll1l1_opy_ = eval(os.getenv(bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪ୛")))
  if bstack11llll1l1_opy_:
    if bstack1ll111l111_opy_() < version.parse(bstack11ll1ll_opy_ (u"ࠪ࠶࠳࠹࠮࠱ࠩଡ଼")):
      return None
    else:
      from appium.options.common.base import AppiumOptions
      options = AppiumOptions().load_capabilities(caps)
      return options
  else:
    browser = bstack11ll1ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫଢ଼")
    if bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ୞") in caps:
      browser = caps[bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫୟ")]
    elif bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨୠ") in caps:
      browser = caps[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࠩୡ")]
    browser = str(browser).lower()
    if browser == bstack11ll1ll_opy_ (u"ࠩ࡬ࡴ࡭ࡵ࡮ࡦࠩୢ") or browser == bstack11ll1ll_opy_ (u"ࠪ࡭ࡵࡧࡤࠨୣ"):
      browser = bstack11ll1ll_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫ୤")
    if browser == bstack11ll1ll_opy_ (u"ࠬࡹࡡ࡮ࡵࡸࡲ࡬࠭୥"):
      browser = bstack11ll1ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭୦")
    if browser not in [bstack11ll1ll_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ୧"), bstack11ll1ll_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭୨"), bstack11ll1ll_opy_ (u"ࠩ࡬ࡩࠬ୩"), bstack11ll1ll_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪ୪"), bstack11ll1ll_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬ୫")]:
      return None
    try:
      package = bstack11ll1ll_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳ࠮ࡸࡧࡥࡨࡷ࡯ࡶࡦࡴ࠱ࡿࢂ࠴࡯ࡱࡶ࡬ࡳࡳࡹࠧ୬").format(browser)
      name = bstack11ll1ll_opy_ (u"࠭ࡏࡱࡶ࡬ࡳࡳࡹࠧ୭")
      browser_options = getattr(__import__(package, fromlist=[name]), name)
      options = browser_options()
      if not bstack1l1l1lll11_opy_(options):
        return None
      for bstack1111l1llll_opy_ in caps.keys():
        options.set_capability(bstack1111l1llll_opy_, caps[bstack1111l1llll_opy_])
      bstack11l1l11l11_opy_(options, caps)
      return options
    except Exception as e:
      logger.debug(str(e))
      return None
def bstack111l11l11_opy_(options, bstack1l11l11ll_opy_):
  if not bstack1l1l1lll11_opy_(options):
    return
  for bstack1111l1llll_opy_ in bstack1l11l11ll_opy_.keys():
    if bstack1111l1llll_opy_ in bstack11lll11l1l_opy_:
      continue
    if bstack1111l1llll_opy_ in options._caps and type(options._caps[bstack1111l1llll_opy_]) in [dict, list]:
      options._caps[bstack1111l1llll_opy_] = update(options._caps[bstack1111l1llll_opy_], bstack1l11l11ll_opy_[bstack1111l1llll_opy_])
    else:
      options.set_capability(bstack1111l1llll_opy_, bstack1l11l11ll_opy_[bstack1111l1llll_opy_])
  bstack11l1l11l11_opy_(options, bstack1l11l11ll_opy_)
  if bstack11ll1ll_opy_ (u"ࠧ࡮ࡱࡽ࠾ࡩ࡫ࡢࡶࡩࡪࡩࡷࡇࡤࡥࡴࡨࡷࡸ࠭୮") in options._caps:
    if options._caps[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭୯")] and options._caps[bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ୰")].lower() != bstack11ll1ll_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫୱ"):
      del options._caps[bstack11ll1ll_opy_ (u"ࠫࡲࡵࡺ࠻ࡦࡨࡦࡺ࡭ࡧࡦࡴࡄࡨࡩࡸࡥࡴࡵࠪ୲")]
def bstack11l11l111_opy_(proxy_config):
  if bstack11ll1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩ୳") in proxy_config:
    proxy_config[bstack11ll1ll_opy_ (u"࠭ࡳࡴ࡮ࡓࡶࡴࡾࡹࠨ୴")] = proxy_config[bstack11ll1ll_opy_ (u"ࠧࡩࡶࡷࡴࡸࡖࡲࡰࡺࡼࠫ୵")]
    del (proxy_config[bstack11ll1ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬ୶")])
  if bstack11ll1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡕࡻࡳࡩࠬ୷") in proxy_config and proxy_config[bstack11ll1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡖࡼࡴࡪ࠭୸")].lower() != bstack11ll1ll_opy_ (u"ࠫࡩ࡯ࡲࡦࡥࡷࠫ୹"):
    proxy_config[bstack11ll1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࡘࡾࡶࡥࠨ୺")] = bstack11ll1ll_opy_ (u"࠭࡭ࡢࡰࡸࡥࡱ࠭୻")
  if bstack11ll1ll_opy_ (u"ࠧࡱࡴࡲࡼࡾࡇࡵࡵࡱࡦࡳࡳ࡬ࡩࡨࡗࡵࡰࠬ୼") in proxy_config:
    proxy_config[bstack11ll1ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡔࡺࡲࡨࠫ୽")] = bstack11ll1ll_opy_ (u"ࠩࡳࡥࡨ࠭୾")
  return proxy_config
def bstack1l11l1lll_opy_(config, proxy):
  from selenium.webdriver.common.proxy import Proxy
  if not bstack11ll1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࠩ୿") in config:
    return proxy
  config[bstack11ll1ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࠪ஀")] = bstack11l11l111_opy_(config[bstack11ll1ll_opy_ (u"ࠬࡶࡲࡰࡺࡼࠫ஁")])
  if proxy == None:
    proxy = Proxy(config[bstack11ll1ll_opy_ (u"࠭ࡰࡳࡱࡻࡽࠬஂ")])
  return proxy
def bstack1llll11lll_opy_(self):
  global CONFIG
  global bstack11111llll_opy_
  try:
    proxy = bstack1l111ll1ll_opy_(CONFIG)
    if proxy:
      if proxy.endswith(bstack11ll1ll_opy_ (u"ࠧ࠯ࡲࡤࡧࠬஃ")):
        proxies = bstack1l11l1l111_opy_(proxy, bstack111l1l1111_opy_())
        if len(proxies) > 0:
          protocol, bstack11ll1l11l1_opy_ = proxies.popitem()
          if bstack11ll1ll_opy_ (u"ࠣ࠼࠲࠳ࠧ஄") in bstack11ll1l11l1_opy_:
            return bstack11ll1l11l1_opy_
          else:
            return bstack11ll1ll_opy_ (u"ࠤ࡫ࡸࡹࡶ࠺࠰࠱ࠥஅ") + bstack11ll1l11l1_opy_
      else:
        return proxy
  except Exception as e:
    logger.error(bstack11ll1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡰࡳࡱࡻࡽࠥࡻࡲ࡭ࠢ࠽ࠤࢀࢃࠢஆ").format(str(e)))
  return bstack11111llll_opy_(self)
def bstack1l1llllll1_opy_():
  global CONFIG
  return bstack1111lllll_opy_(CONFIG) and bstack1111lll1l1_opy_() and bstack11llll1111_opy_() >= version.parse(bstack111l1ll1l_opy_)
def bstack1ll1ll1lll_opy_():
  global CONFIG
  return (bstack11ll1ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧஇ") in CONFIG or bstack11ll1ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩஈ") in CONFIG) and bstack1ll11ll111_opy_()
def bstack1l1l1l1l1_opy_(config):
  bstack1111l111l1_opy_ = {}
  if bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࡒࡴࡹ࡯࡯࡯ࡵࠪஉ") in config:
    bstack1111l111l1_opy_ = config[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫஊ")]
  if bstack11ll1ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ஋") in config:
    bstack1111l111l1_opy_ = config[bstack11ll1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡐࡲࡷ࡭ࡴࡴࡳࠨ஌")]
  proxy = bstack1l111ll1ll_opy_(config)
  if proxy:
    if proxy.endswith(bstack11ll1ll_opy_ (u"ࠪ࠲ࡵࡧࡣࠨ஍")) and os.path.isfile(proxy):
      bstack1111l111l1_opy_[bstack11ll1ll_opy_ (u"ࠫ࠲ࡶࡡࡤ࠯ࡩ࡭ࡱ࡫ࠧஎ")] = proxy
    else:
      parsed_url = None
      if proxy.endswith(bstack11ll1ll_opy_ (u"ࠬ࠴ࡰࡢࡥࠪஏ")):
        proxies = bstack11l111l11_opy_(config, bstack111l1l1111_opy_())
        if len(proxies) > 0:
          protocol, bstack11ll1l11l1_opy_ = proxies.popitem()
          if bstack11ll1ll_opy_ (u"ࠨ࠺࠰࠱ࠥஐ") in bstack11ll1l11l1_opy_:
            parsed_url = urlparse(bstack11ll1l11l1_opy_)
          else:
            parsed_url = urlparse(protocol + bstack11ll1ll_opy_ (u"ࠢ࠻࠱࠲ࠦ஑") + bstack11ll1l11l1_opy_)
      else:
        parsed_url = urlparse(proxy)
      if parsed_url and parsed_url.hostname: bstack1111l111l1_opy_[bstack11ll1ll_opy_ (u"ࠨࡲࡵࡳࡽࡿࡈࡰࡵࡷࠫஒ")] = str(parsed_url.hostname)
      if parsed_url and parsed_url.port: bstack1111l111l1_opy_[bstack11ll1ll_opy_ (u"ࠩࡳࡶࡴࡾࡹࡑࡱࡵࡸࠬஓ")] = str(parsed_url.port)
      if parsed_url and parsed_url.username: bstack1111l111l1_opy_[bstack11ll1ll_opy_ (u"ࠪࡴࡷࡵࡸࡺࡗࡶࡩࡷ࠭ஔ")] = str(parsed_url.username)
      if parsed_url and parsed_url.password: bstack1111l111l1_opy_[bstack11ll1ll_opy_ (u"ࠫࡵࡸ࡯ࡹࡻࡓࡥࡸࡹࠧக")] = str(parsed_url.password)
  return bstack1111l111l1_opy_
def bstack1111ll1l11_opy_(config):
  if bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡆࡳࡳࡺࡥࡹࡶࡒࡴࡹ࡯࡯࡯ࡵࠪ஖") in config:
    return config[bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠫ஗")]
  return {}
def bstack1l1l1l11l1_opy_(caps):
  global bstack11ll1lll1l_opy_
  if bstack11ll1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ஘") in caps:
    caps[bstack11ll1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩங")][bstack11ll1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࠨச")] = True
    if bstack11ll1lll1l_opy_:
      caps[bstack11ll1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ஛")][bstack11ll1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ஜ")] = bstack11ll1lll1l_opy_
  else:
    caps[bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡱࡵࡣࡢ࡮ࠪ஝")] = True
    if bstack11ll1lll1l_opy_:
      caps[bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧஞ")] = bstack11ll1lll1l_opy_
@measure(event_name=EVENTS.bstack1l111l11l1_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1ll1l1llll_opy_():
  global CONFIG
  if not bstack1ll1llll1l_opy_(CONFIG) or cli.is_enabled(CONFIG):
    return
  if bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫட") in CONFIG and bstack11l1ll11l_opy_(CONFIG[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ஠")]):
    if (
      bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭஡") in CONFIG
      and bstack11l1ll11l_opy_(CONFIG[bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧ஢")].get(bstack11ll1ll_opy_ (u"ࠫࡸࡱࡩࡱࡄ࡬ࡲࡦࡸࡹࡊࡰ࡬ࡸ࡮ࡧ࡬ࡪࡵࡤࡸ࡮ࡵ࡮ࠨண")))
    ):
      logger.debug(bstack11ll1ll_opy_ (u"ࠧࡒ࡯ࡤࡣ࡯ࠤࡧ࡯࡮ࡢࡴࡼࠤࡳࡵࡴࠡࡵࡷࡥࡷࡺࡥࡥࠢࡤࡷࠥࡹ࡫ࡪࡲࡅ࡭ࡳࡧࡲࡺࡋࡱ࡭ࡹ࡯ࡡ࡭࡫ࡶࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠨத"))
      return
    bstack1111l111l1_opy_ = bstack1l1l1l1l1_opy_(CONFIG)
    bstack11l11lllll_opy_(CONFIG[bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩ஥")], bstack1111l111l1_opy_)
def bstack11l11lllll_opy_(key, bstack1111l111l1_opy_):
  global bstack1111llll1l_opy_
  logger.info(bstack1lllll1lll_opy_)
  try:
    bstack1111llll1l_opy_ = Local()
    bstack1ll111111l_opy_ = {bstack11ll1ll_opy_ (u"ࠧ࡬ࡧࡼࠫ஦"): key}
    bstack1ll111111l_opy_.update(bstack1111l111l1_opy_)
    logger.debug(bstack11l1l11ll1_opy_.format(str(bstack1ll111111l_opy_)).replace(key, bstack11ll1ll_opy_ (u"ࠨ࡝ࡕࡉࡉࡇࡃࡕࡇࡇࡡࠬ஧")))
    bstack1111llll1l_opy_.start(**bstack1ll111111l_opy_)
    if bstack1111llll1l_opy_.isRunning():
      logger.info(bstack1llll1l1l1_opy_)
  except Exception as e:
    bstack1ll1ll11ll_opy_(bstack11l11llll1_opy_.format(str(e)))
def bstack1ll11lll1l_opy_():
  global bstack1111llll1l_opy_
  if bstack1111llll1l_opy_.isRunning():
    logger.info(bstack111111l1l_opy_)
    bstack1111llll1l_opy_.stop()
  bstack1111llll1l_opy_ = None
def bstack1ll1111lll_opy_(bstack11ll1ll1ll_opy_=[]):
  global CONFIG
  bstack1l1l1llll_opy_ = []
  bstack1111lll111_opy_ = [bstack11ll1ll_opy_ (u"ࠩࡲࡷࠬந"), bstack11ll1ll_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ன"), bstack11ll1ll_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠨப"), bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ஫"), bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ஬"), bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ஭")]
  try:
    for err in bstack11ll1ll1ll_opy_:
      bstack11l1l1lll1_opy_ = {}
      for k in bstack1111lll111_opy_:
        val = CONFIG[bstack11ll1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫம")][int(err[bstack11ll1ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨய")])].get(k)
        if val:
          bstack11l1l1lll1_opy_[k] = val
      if(err[bstack11ll1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩர")] != bstack11ll1ll_opy_ (u"ࠫࠬற")):
        bstack11l1l1lll1_opy_[bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡶࠫல")] = {
          err[bstack11ll1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫள")]: err[bstack11ll1ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ழ")]
        }
        bstack1l1l1llll_opy_.append(bstack11l1l1lll1_opy_)
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡪࡴࡸ࡭ࡢࡶࡷ࡭ࡳ࡭ࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡨࡺࡪࡴࡴ࠻ࠢࠪவ") + str(e))
  finally:
    return bstack1l1l1llll_opy_
def bstack1l1ll1111_opy_(file_name):
  bstack1l1l11ll1_opy_ = []
  try:
    bstack111ll1l1l1_opy_ = os.path.join(tempfile.gettempdir(), file_name)
    if os.path.exists(bstack111ll1l1l1_opy_):
      with open(bstack111ll1l1l1_opy_) as f:
        bstack11l1lll11l_opy_ = json.load(f)
        bstack1l1l11ll1_opy_ = bstack11l1lll11l_opy_
      os.remove(bstack111ll1l1l1_opy_)
    return bstack1l1l11ll1_opy_
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤ࡫࡯࡮ࡥ࡫ࡱ࡫ࠥ࡫ࡲࡳࡱࡵࠤࡱ࡯ࡳࡵ࠼ࠣࠫஶ") + str(e))
    return bstack1l1l11ll1_opy_
def bstack111l1l111l_opy_():
  try:
      from bstack_utils.constants import bstack11lllll11_opy_, EVENTS
      from bstack_utils.helper import bstack11ll11ll1l_opy_, get_host_info, bstack1llllll1l_opy_
      from datetime import datetime
      from filelock import FileLock
      bstack111l1ll11l_opy_ = os.path.join(os.getcwd(), bstack11ll1ll_opy_ (u"ࠪࡰࡴ࡭ࠧஷ"), bstack11ll1ll_opy_ (u"ࠫࡰ࡫ࡹ࠮࡯ࡨࡸࡷ࡯ࡣࡴ࠰࡭ࡷࡴࡴࠧஸ"))
      lock = FileLock(bstack111l1ll11l_opy_+bstack11ll1ll_opy_ (u"ࠧ࠴࡬ࡰࡥ࡮ࠦஹ"))
      def bstack11llll1l_opy_():
          try:
              with lock:
                  with open(bstack111l1ll11l_opy_, bstack11ll1ll_opy_ (u"ࠨࡲࠣ஺"), encoding=bstack11ll1ll_opy_ (u"ࠢࡶࡶࡩ࠱࠽ࠨ஻")) as file:
                      data = json.load(file)
                      config = {
                          bstack11ll1ll_opy_ (u"ࠣࡪࡨࡥࡩ࡫ࡲࡴࠤ஼"): {
                              bstack11ll1ll_opy_ (u"ࠤࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠣ஽"): bstack11ll1ll_opy_ (u"ࠥࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳࠨா"),
                          }
                      }
                      bstack1l1ll11111_opy_ = datetime.utcnow()
                      bstack1ll111ll_opy_ = bstack1l1ll11111_opy_.strftime(bstack11ll1ll_opy_ (u"ࠦࠪ࡟࠭ࠦ࡯࠰ࠩࡩ࡚ࠥࡉ࠼ࠨࡑ࠿ࠫࡓ࠯ࠧࡩࠤ࡚࡚ࡃࠣி"))
                      test_id = os.environ.get(bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪீ")) if os.environ.get(bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫு")) else bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠢࡴࡦ࡮ࡖࡺࡴࡉࡥࠤூ"))
                      payload = {
                          bstack11ll1ll_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠧ௃"): bstack11ll1ll_opy_ (u"ࠤࡶࡨࡰࡥࡥࡷࡧࡱࡸࡸࠨ௄"),
                          bstack11ll1ll_opy_ (u"ࠥࡨࡦࡺࡡࠣ௅"): {
                              bstack11ll1ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡪࡸࡦࡤࡻࡵࡪࡦࠥெ"): test_id,
                              bstack11ll1ll_opy_ (u"ࠧࡩࡲࡦࡣࡷࡩࡩࡥࡤࡢࡻࠥே"): bstack1ll111ll_opy_,
                              bstack11ll1ll_opy_ (u"ࠨࡥࡷࡧࡱࡸࡤࡴࡡ࡮ࡧࠥை"): bstack11ll1ll_opy_ (u"ࠢࡔࡆࡎࡊࡪࡧࡴࡶࡴࡨࡔࡪࡸࡦࡰࡴࡰࡥࡳࡩࡥࠣ௉"),
                              bstack11ll1ll_opy_ (u"ࠣࡧࡹࡩࡳࡺ࡟࡫ࡵࡲࡲࠧொ"): {
                                  bstack11ll1ll_opy_ (u"ࠤࡰࡩࡦࡹࡵࡳࡧࡶࠦோ"): data,
                                  bstack11ll1ll_opy_ (u"ࠥࡷࡩࡱࡒࡶࡰࡌࡨࠧௌ"): bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠦࡸࡪ࡫ࡓࡷࡱࡍࡩࠨ்"))
                              },
                              bstack11ll1ll_opy_ (u"ࠧࡻࡳࡦࡴࡢࡨࡦࡺࡡࠣ௎"): bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠨࡵࡴࡧࡵࡒࡦࡳࡥࠣ௏")),
                              bstack11ll1ll_opy_ (u"ࠢࡩࡱࡶࡸࡤ࡯࡮ࡧࡱࠥௐ"): get_host_info()
                          }
                      }
                      bstack1111l1l111_opy_ = bstack111l111l11_opy_(cli.config, [bstack11ll1ll_opy_ (u"ࠣࡣࡳ࡭ࡸࠨ௑"), bstack11ll1ll_opy_ (u"ࠤࡨࡨࡸࡏ࡮ࡴࡶࡵࡹࡲ࡫࡮ࡵࡣࡷ࡭ࡴࡴࠢ௒"), bstack11ll1ll_opy_ (u"ࠥࡥࡵ࡯ࠢ௓")], bstack11lllll11_opy_)
                      response = bstack11ll11ll1l_opy_(bstack11ll1ll_opy_ (u"ࠦࡕࡕࡓࡕࠤ௔"), bstack1111l1l111_opy_, payload, config)
                      if(response.status_code >= 200 and response.status_code < 300):
                          logger.debug(bstack11ll1ll_opy_ (u"ࠧࡊࡡࡵࡣࠣࡷࡪࡴࡴࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࡱࡿࠠࡵࡱࠣࡿࢂࠦࡷࡪࡶ࡫ࠤࡩࡧࡴࡢࠢࡾࢁࠧ௕").format(bstack11lllll11_opy_, payload))
                      else:
                          logger.debug(bstack11ll1ll_opy_ (u"ࠨࡒࡦࡳࡸࡩࡸࡺࠠࡧࡣ࡬ࡰࡪࡪࠠࡧࡱࡵࠤࢀࢃࠠࡸ࡫ࡷ࡬ࠥࡪࡡࡵࡣࠣࡿࢂࠨ௖").format(bstack11lllll11_opy_, payload))
          except Exception as e:
              logger.debug(bstack11ll1ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡴࡤࠡ࡭ࡨࡽࠥࡳࡥࡵࡴ࡬ࡧࡸࠦࡤࡢࡶࡤࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡࡽࢀࠦௗ").format(e))
      bstack11llll1l_opy_()
      bstack1l1l111ll1_opy_(bstack111l1ll11l_opy_, logger)
  except:
    pass
def bstack1lll1l1111_opy_():
  global bstack1lll111111_opy_
  global bstack11l1lll1l1_opy_
  global bstack1111ll1l1_opy_
  global bstack11111ll111_opy_
  global bstack111lll1lll_opy_
  global bstack11l1ll11ll_opy_
  global CONFIG
  bstack1l1l11ll11_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩ௘"))
  if bstack1l1l11ll11_opy_ in [bstack11ll1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ௙"), bstack11ll1ll_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩ௚")]:
    bstack1l1l11l111_opy_()
  percy.shutdown()
  if bstack1lll111111_opy_:
    logger.warning(bstack11l1l111l1_opy_.format(str(bstack1lll111111_opy_)))
  else:
    try:
      bstack1l1llll1l1_opy_ = bstack1ll1l1lll1_opy_(bstack11ll1ll_opy_ (u"ࠫ࠳ࡨࡳࡵࡣࡦ࡯࠲ࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪ௛"), logger)
      if bstack1l1llll1l1_opy_.get(bstack11ll1ll_opy_ (u"ࠬࡴࡵࡥࡩࡨࡣࡱࡵࡣࡢ࡮ࠪ௜")) and bstack1l1llll1l1_opy_.get(bstack11ll1ll_opy_ (u"࠭࡮ࡶࡦࡪࡩࡤࡲ࡯ࡤࡣ࡯ࠫ௝")).get(bstack11ll1ll_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩ௞")):
        logger.warning(bstack11l1l111l1_opy_.format(str(bstack1l1llll1l1_opy_[bstack11ll1ll_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭௟")][bstack11ll1ll_opy_ (u"ࠩ࡫ࡳࡸࡺ࡮ࡢ࡯ࡨࠫ௠")])))
    except Exception as e:
      logger.error(e)
  if cli.is_running():
    bstack1l1llll11l_opy_.invoke(Events.bstack11lll1ll1l_opy_)
  logger.info(bstack11111lll1l_opy_)
  global bstack1111llll1l_opy_
  if bstack1111llll1l_opy_:
    bstack1ll11lll1l_opy_()
  try:
    with bstack11ll11lll_opy_:
      bstack1ll1lll111_opy_ = bstack11l1lll1l1_opy_.copy()
    for driver in bstack1ll1lll111_opy_:
      driver.quit()
  except Exception as e:
    pass
  logger.info(bstack11ll111l1_opy_)
  if bstack11l1ll11ll_opy_ == bstack11ll1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ௡"):
    bstack111lll1lll_opy_ = bstack1l1ll1111_opy_(bstack11ll1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺ࠮࡫ࡵࡲࡲࠬ௢"))
  if bstack11l1ll11ll_opy_ == bstack11ll1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ௣") and len(bstack11111ll111_opy_) == 0:
    bstack11111ll111_opy_ = bstack1l1ll1111_opy_(bstack11ll1ll_opy_ (u"࠭ࡰࡸࡡࡳࡽࡹ࡫ࡳࡵࡡࡨࡶࡷࡵࡲࡠ࡮࡬ࡷࡹ࠴ࡪࡴࡱࡱࠫ௤"))
    if len(bstack11111ll111_opy_) == 0:
      bstack11111ll111_opy_ = bstack1l1ll1111_opy_(bstack11ll1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࡟ࡱࡲࡳࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴ࠯࡬ࡶࡳࡳ࠭௥"))
  bstack1l1l111111_opy_ = bstack11ll1ll_opy_ (u"ࠨࠩ௦")
  if len(bstack1111ll1l1_opy_) > 0:
    bstack1l1l111111_opy_ = bstack1ll1111lll_opy_(bstack1111ll1l1_opy_)
  elif len(bstack11111ll111_opy_) > 0:
    bstack1l1l111111_opy_ = bstack1ll1111lll_opy_(bstack11111ll111_opy_)
  elif len(bstack111lll1lll_opy_) > 0:
    bstack1l1l111111_opy_ = bstack1ll1111lll_opy_(bstack111lll1lll_opy_)
  elif len(bstack1l1l1111l_opy_) > 0:
    bstack1l1l111111_opy_ = bstack1ll1111lll_opy_(bstack1l1l1111l_opy_)
  if bool(bstack1l1l111111_opy_):
    bstack1l11l111l_opy_(bstack1l1l111111_opy_)
  else:
    bstack1l11l111l_opy_()
  bstack1l1l111ll1_opy_(bstack1l1l111l1_opy_, logger)
  if bstack1l1l11ll11_opy_ not in [bstack11ll1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪ௧")]:
    bstack111l1l111l_opy_()
  bstack11111l1ll1_opy_.bstack1l1111ll_opy_(CONFIG)
  if len(bstack111lll1lll_opy_) > 0:
    sys.exit(len(bstack111lll1lll_opy_))
def bstack1l1lllll1l_opy_(bstack1ll11l1lll_opy_, frame):
  global bstack1llllll1l_opy_
  logger.error(bstack11ll11l111_opy_)
  bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡒࡴ࠭௨"), bstack1ll11l1lll_opy_)
  if hasattr(signal, bstack11ll1ll_opy_ (u"ࠫࡘ࡯ࡧ࡯ࡣ࡯ࡷࠬ௩")):
    bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"ࠬࡹࡤ࡬ࡍ࡬ࡰࡱ࡙ࡩࡨࡰࡤࡰࠬ௪"), signal.Signals(bstack1ll11l1lll_opy_).name)
  else:
    bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"࠭ࡳࡥ࡭ࡎ࡭ࡱࡲࡓࡪࡩࡱࡥࡱ࠭௫"), bstack11ll1ll_opy_ (u"ࠧࡔࡋࡊ࡙ࡓࡑࡎࡐ࡙ࡑࠫ௬"))
  if cli.is_running():
    bstack1l1llll11l_opy_.invoke(Events.bstack11lll1ll1l_opy_)
  bstack1l1l11ll11_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩ௭"))
  if bstack1l1l11ll11_opy_ == bstack11ll1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ௮") and not cli.is_enabled(CONFIG):
    bstack1ll1l111_opy_.stop(bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠪࡷࡩࡱࡋࡪ࡮࡯ࡗ࡮࡭࡮ࡢ࡮ࠪ௯")))
  bstack1lll1l1111_opy_()
  sys.exit(1)
def bstack1ll1ll11ll_opy_(err):
  logger.critical(bstack1l1l1111ll_opy_.format(str(err)))
  bstack1l11l111l_opy_(bstack1l1l1111ll_opy_.format(str(err)), True)
  atexit.unregister(bstack1lll1l1111_opy_)
  bstack1l1l11l111_opy_()
  sys.exit(1)
def bstack1lll11llll_opy_(error, message):
  logger.critical(str(error))
  logger.critical(message)
  bstack1l11l111l_opy_(message, True)
  atexit.unregister(bstack1lll1l1111_opy_)
  bstack1l1l11l111_opy_()
  sys.exit(1)
def bstack1llllll111_opy_():
  global CONFIG
  global bstack1lll1l111l_opy_
  global bstack111l1llll_opy_
  global bstack1l1ll11l11_opy_
  CONFIG = bstack11l111ll1_opy_()
  load_dotenv(CONFIG.get(bstack11ll1ll_opy_ (u"ࠫࡪࡴࡶࡇ࡫࡯ࡩࠬ௰")))
  bstack1l111lllll_opy_()
  bstack111ll11ll_opy_()
  CONFIG = bstack1ll111l11_opy_(CONFIG)
  update(CONFIG, bstack111l1llll_opy_)
  update(CONFIG, bstack1lll1l111l_opy_)
  if not cli.is_enabled(CONFIG):
    CONFIG = bstack11l1l11l1l_opy_(CONFIG)
  bstack1l1ll11l11_opy_ = bstack1ll1llll1l_opy_(CONFIG)
  os.environ[bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡆ࡛ࡔࡐࡏࡄࡘࡎࡕࡎࠨ௱")] = bstack1l1ll11l11_opy_.__str__().lower()
  bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡥࡳࡦࡵࡶ࡭ࡴࡴࠧ௲"), bstack1l1ll11l11_opy_)
  if (bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ௳") in CONFIG and bstack11ll1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ௴") in bstack1lll1l111l_opy_) or (
          bstack11ll1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௵") in CONFIG and bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭௶") not in bstack111l1llll_opy_):
    if os.getenv(bstack11ll1ll_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡣࡈࡕࡍࡃࡋࡑࡉࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠨ௷")):
      CONFIG[bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ௸")] = os.getenv(bstack11ll1ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡥࡃࡐࡏࡅࡍࡓࡋࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠪ௹"))
    else:
      if not CONFIG.get(bstack11ll1ll_opy_ (u"ࠢࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠥ௺"), bstack11ll1ll_opy_ (u"ࠣࠤ௻")) in bstack11l11111l1_opy_:
        bstack1lll1l1l1l_opy_()
  elif (bstack11ll1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ௼") not in CONFIG and bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ௽") in CONFIG) or (
          bstack11ll1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ௾") in bstack111l1llll_opy_ and bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ௿") not in bstack1lll1l111l_opy_):
    del (CONFIG[bstack11ll1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨఀ")])
  if bstack11llll11l_opy_(CONFIG):
    bstack1ll1ll11ll_opy_(bstack11ll1111ll_opy_)
  Config.bstack1lll11ll1_opy_().set_property(bstack11ll1ll_opy_ (u"ࠢࡶࡵࡨࡶࡓࡧ࡭ࡦࠤఁ"), CONFIG[bstack11ll1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪం")])
  bstack111l11lll_opy_()
  bstack11llll1ll_opy_()
  if bstack11llll1l1_opy_ and not CONFIG.get(bstack11ll1ll_opy_ (u"ࠤࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠧః"), bstack11ll1ll_opy_ (u"ࠥࠦఄ")) in bstack11l11111l1_opy_:
    CONFIG[bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰࠨఅ")] = bstack11lll1l11_opy_(CONFIG)
    logger.info(bstack1l11l1l11_opy_.format(CONFIG[bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱࠩఆ")]))
  if not bstack1l1ll11l11_opy_:
    CONFIG[bstack11ll1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩఇ")] = [{}]
def bstack111111llll_opy_(config, bstack1l11111ll_opy_):
  global CONFIG
  global bstack11llll1l1_opy_
  CONFIG = config
  bstack11llll1l1_opy_ = bstack1l11111ll_opy_
def bstack11llll1ll_opy_():
  global CONFIG
  global bstack11llll1l1_opy_
  if bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳࠫఈ") in CONFIG:
    try:
      from appium import version
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack1l1l11llll_opy_)
    bstack11llll1l1_opy_ = True
    bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧఉ"), True)
def bstack11lll1l11_opy_(config):
  bstack111111lll1_opy_ = bstack11ll1ll_opy_ (u"ࠩࠪఊ")
  app = config[bstack11ll1ll_opy_ (u"ࠪࡥࡵࡶࠧఋ")]
  if isinstance(app, str):
    if os.path.splitext(app)[1] in bstack1l11l1ll1l_opy_:
      if os.path.exists(app):
        bstack111111lll1_opy_ = bstack111ll1111l_opy_(config, app)
      elif bstack1lll1lll11_opy_(app):
        bstack111111lll1_opy_ = app
      else:
        bstack1ll1ll11ll_opy_(bstack1l1ll11ll1_opy_.format(app))
    else:
      if bstack1lll1lll11_opy_(app):
        bstack111111lll1_opy_ = app
      elif os.path.exists(app):
        bstack111111lll1_opy_ = bstack111ll1111l_opy_(app)
      else:
        bstack1ll1ll11ll_opy_(bstack1ll11l111_opy_)
  else:
    if len(app) > 2:
      bstack1ll1ll11ll_opy_(bstack11ll111lll_opy_)
    elif len(app) == 2:
      if bstack11ll1ll_opy_ (u"ࠫࡵࡧࡴࡩࠩఌ") in app and bstack11ll1ll_opy_ (u"ࠬࡩࡵࡴࡶࡲࡱࡤ࡯ࡤࠨ఍") in app:
        if os.path.exists(app[bstack11ll1ll_opy_ (u"࠭ࡰࡢࡶ࡫ࠫఎ")]):
          bstack111111lll1_opy_ = bstack111ll1111l_opy_(config, app[bstack11ll1ll_opy_ (u"ࠧࡱࡣࡷ࡬ࠬఏ")], app[bstack11ll1ll_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡠ࡫ࡧࠫఐ")])
        else:
          bstack1ll1ll11ll_opy_(bstack1l1ll11ll1_opy_.format(app))
      else:
        bstack1ll1ll11ll_opy_(bstack11ll111lll_opy_)
    else:
      for key in app:
        if key in bstack11l1l111l_opy_:
          if key == bstack11ll1ll_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ఑"):
            if os.path.exists(app[key]):
              bstack111111lll1_opy_ = bstack111ll1111l_opy_(config, app[key])
            else:
              bstack1ll1ll11ll_opy_(bstack1l1ll11ll1_opy_.format(app))
          else:
            bstack111111lll1_opy_ = app[key]
        else:
          bstack1ll1ll11ll_opy_(bstack11l1111111_opy_)
  return bstack111111lll1_opy_
def bstack1lll1lll11_opy_(bstack111111lll1_opy_):
  import re
  bstack1111l11ll1_opy_ = re.compile(bstack11ll1ll_opy_ (u"ࡵࠦࡣࡡࡡ࠮ࡼࡄ࠱࡟࠶࠭࠺࡞ࡢ࠲ࡡ࠳࡝ࠫࠦࠥఒ"))
  bstack111ll11lll_opy_ = re.compile(bstack11ll1ll_opy_ (u"ࡶࠧࡤ࡛ࡢ࠯ࡽࡅ࠲ࡠ࠰࠮࠻࡟ࡣ࠳ࡢ࠭࡞ࠬ࠲࡟ࡦ࠳ࡺࡂ࠯࡝࠴࠲࠿࡜ࡠ࠰࡟࠱ࡢ࠰ࠤࠣఓ"))
  if bstack11ll1ll_opy_ (u"ࠬࡨࡳ࠻࠱࠲ࠫఔ") in bstack111111lll1_opy_ or re.fullmatch(bstack1111l11ll1_opy_, bstack111111lll1_opy_) or re.fullmatch(bstack111ll11lll_opy_, bstack111111lll1_opy_):
    return True
  else:
    return False
@measure(event_name=EVENTS.bstack11l11lll1_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack111ll1111l_opy_(config, path, bstack1l1ll1ll11_opy_=None):
  import requests
  from requests_toolbelt.multipart.encoder import MultipartEncoder
  import hashlib
  md5_hash = hashlib.md5(open(os.path.abspath(path), bstack11ll1ll_opy_ (u"࠭ࡲࡣࠩక")).read()).hexdigest()
  bstack111ll1l111_opy_ = bstack1111ll1111_opy_(md5_hash)
  bstack111111lll1_opy_ = None
  if bstack111ll1l111_opy_:
    logger.info(bstack1l11ll11ll_opy_.format(bstack111ll1l111_opy_, md5_hash))
    return bstack111ll1l111_opy_
  bstack111111ll11_opy_ = datetime.datetime.now()
  multipart_data = MultipartEncoder(
    fields={
      bstack11ll1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࠬఖ"): (os.path.basename(path), open(os.path.abspath(path), bstack11ll1ll_opy_ (u"ࠨࡴࡥࠫగ")), bstack11ll1ll_opy_ (u"ࠩࡷࡩࡽࡺ࠯ࡱ࡮ࡤ࡭ࡳ࠭ఘ")),
      bstack11ll1ll_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡢ࡭ࡩ࠭ఙ"): bstack1l1ll1ll11_opy_
    }
  )
  response = requests.post(bstack1ll11llll1_opy_, data=multipart_data,
                           headers={bstack11ll1ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪచ"): multipart_data.content_type},
                           auth=(config[bstack11ll1ll_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧఛ")], config[bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩజ")]))
  try:
    res = json.loads(response.text)
    bstack111111lll1_opy_ = res[bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳࡣࡺࡸ࡬ࠨఝ")]
    logger.info(bstack111l1l1l1_opy_.format(bstack111111lll1_opy_))
    bstack1l11l1111l_opy_(md5_hash, bstack111111lll1_opy_)
    cli.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠣࡪࡷࡸࡵࡀࡵࡱ࡮ࡲࡥࡩࡥࡡࡱࡲࠥఞ"), datetime.datetime.now() - bstack111111ll11_opy_)
  except ValueError as err:
    bstack1ll1ll11ll_opy_(bstack11ll1ll111_opy_.format(str(err)))
  return bstack111111lll1_opy_
def bstack111l11lll_opy_(framework_name=None, args=None):
  global CONFIG
  global bstack1l111l111_opy_
  bstack1ll1lllll_opy_ = 1
  bstack11lllllll1_opy_ = 1
  if bstack11ll1ll_opy_ (u"ࠩࡳࡥࡷࡧ࡬࡭ࡧ࡯ࡷࡕ࡫ࡲࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩట") in CONFIG:
    bstack11lllllll1_opy_ = CONFIG[bstack11ll1ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪఠ")]
  else:
    bstack11lllllll1_opy_ = bstack1l111l111l_opy_(framework_name, args) or 1
  if bstack11ll1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧడ") in CONFIG:
    bstack1ll1lllll_opy_ = len(CONFIG[bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨఢ")])
  bstack1l111l111_opy_ = int(bstack11lllllll1_opy_) * int(bstack1ll1lllll_opy_)
def bstack1l111l111l_opy_(framework_name, args):
  if framework_name == bstack1l1111l1l_opy_ and args and bstack11ll1ll_opy_ (u"࠭࠭࠮ࡲࡵࡳࡨ࡫ࡳࡴࡧࡶࠫణ") in args:
      bstack111lll11ll_opy_ = args.index(bstack11ll1ll_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬత"))
      return int(args[bstack111lll11ll_opy_ + 1]) or 1
  return 1
def bstack1111ll1111_opy_(md5_hash):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡲ࡯ࡤ࡭ࠣࡲࡴࡺࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧ࠯ࠤࡺࡹࡩ࡯ࡩࠣࡦࡦࡹࡩࡤࠢࡩ࡭ࡱ࡫ࠠࡰࡲࡨࡶࡦࡺࡩࡰࡰࡶࠫథ"))
    bstack11l1lllll1_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠩࢁࠫద")), bstack11ll1ll_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪధ"), bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰࡖࡲ࡯ࡳࡦࡪࡍࡅ࠷ࡋࡥࡸ࡮࠮࡫ࡵࡲࡲࠬన"))
    if os.path.exists(bstack11l1lllll1_opy_):
      try:
        bstack11ll11lll1_opy_ = json.load(open(bstack11l1lllll1_opy_, bstack11ll1ll_opy_ (u"ࠬࡸࡢࠨ఩")))
        if md5_hash in bstack11ll11lll1_opy_:
          bstack1111l111l_opy_ = bstack11ll11lll1_opy_[md5_hash]
          bstack11l1ll1l1l_opy_ = datetime.datetime.now()
          bstack11ll1l1ll_opy_ = datetime.datetime.strptime(bstack1111l111l_opy_[bstack11ll1ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱࠩప")], bstack11ll1ll_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫఫ"))
          if (bstack11l1ll1l1l_opy_ - bstack11ll1l1ll_opy_).days > 30:
            return None
          elif version.parse(str(__version__)) > version.parse(bstack1111l111l_opy_[bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭బ")]):
            return None
          return bstack1111l111l_opy_[bstack11ll1ll_opy_ (u"ࠩ࡬ࡨࠬభ")]
      except Exception as e:
        logger.debug(bstack11ll1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡵࡩࡦࡪࡩ࡯ࡩࠣࡑࡉ࠻ࠠࡩࡣࡶ࡬ࠥ࡬ࡩ࡭ࡧ࠽ࠤࢀࢃࠧమ").format(str(e)))
    return None
  bstack11l1lllll1_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠫࢃ࠭య")), bstack11ll1ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬర"), bstack11ll1ll_opy_ (u"࠭ࡡࡱࡲࡘࡴࡱࡵࡡࡥࡏࡇ࠹ࡍࡧࡳࡩ࠰࡭ࡷࡴࡴࠧఱ"))
  lock_file = bstack11l1lllll1_opy_ + bstack11ll1ll_opy_ (u"ࠧ࠯࡮ࡲࡧࡰ࠭ల")
  try:
    with FileLock(lock_file, timeout=10):
      if os.path.exists(bstack11l1lllll1_opy_):
        with open(bstack11l1lllll1_opy_, bstack11ll1ll_opy_ (u"ࠨࡴࠪళ")) as f:
          content = f.read().strip()
          if content:
            bstack11ll11lll1_opy_ = json.loads(content)
            if md5_hash in bstack11ll11lll1_opy_:
              bstack1111l111l_opy_ = bstack11ll11lll1_opy_[md5_hash]
              bstack11l1ll1l1l_opy_ = datetime.datetime.now()
              bstack11ll1l1ll_opy_ = datetime.datetime.strptime(bstack1111l111l_opy_[bstack11ll1ll_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬఴ")], bstack11ll1ll_opy_ (u"ࠪࠩࡩ࠵ࠥ࡮࠱ࠨ࡝ࠥࠫࡈ࠻ࠧࡐ࠾࡙ࠪࠧవ"))
              if (bstack11l1ll1l1l_opy_ - bstack11ll1l1ll_opy_).days > 30:
                return None
              elif version.parse(str(__version__)) > version.parse(bstack1111l111l_opy_[bstack11ll1ll_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩశ")]):
                return None
              return bstack1111l111l_opy_[bstack11ll1ll_opy_ (u"ࠬ࡯ࡤࠨష")]
      return None
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥࡽࡩࡵࡪࠣࡪ࡮ࡲࡥࠡ࡮ࡲࡧࡰ࡯࡮ࡨࠢࡩࡳࡷࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨ࠻ࠢࡾࢁࠬస").format(str(e)))
    return None
def bstack1l11l1111l_opy_(md5_hash, bstack111111lll1_opy_):
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡱࡵࡣ࡬ࠢࡱࡳࡹࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡥࡥࡸ࡯ࡣࠡࡨ࡬ࡰࡪࠦ࡯ࡱࡧࡵࡥࡹ࡯࡯࡯ࡵࠪహ"))
    bstack1l111lll11_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠨࢀࠪ఺")), bstack11ll1ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ఻"))
    if not os.path.exists(bstack1l111lll11_opy_):
      os.makedirs(bstack1l111lll11_opy_)
    bstack11l1lllll1_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠪࢂ఼ࠬ")), bstack11ll1ll_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫఽ"), bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱࡗࡳࡰࡴࡧࡤࡎࡆ࠸ࡌࡦࡹࡨ࠯࡬ࡶࡳࡳ࠭ా"))
    bstack1111l1l11_opy_ = {
      bstack11ll1ll_opy_ (u"࠭ࡩࡥࠩి"): bstack111111lll1_opy_,
      bstack11ll1ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪీ"): datetime.datetime.strftime(datetime.datetime.now(), bstack11ll1ll_opy_ (u"ࠨࠧࡧ࠳ࠪࡳ࠯࡛ࠦࠣࠩࡍࡀࠥࡎ࠼ࠨࡗࠬు")),
      bstack11ll1ll_opy_ (u"ࠩࡶࡨࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧూ"): str(__version__)
    }
    try:
      bstack11ll11lll1_opy_ = {}
      if os.path.exists(bstack11l1lllll1_opy_):
        bstack11ll11lll1_opy_ = json.load(open(bstack11l1lllll1_opy_, bstack11ll1ll_opy_ (u"ࠪࡶࡧ࠭ృ")))
      bstack11ll11lll1_opy_[md5_hash] = bstack1111l1l11_opy_
      with open(bstack11l1lllll1_opy_, bstack11ll1ll_opy_ (u"ࠦࡼ࠱ࠢౄ")) as outfile:
        json.dump(bstack11ll11lll1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11ll1ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤࡺࡶࡤࡢࡶ࡬ࡲ࡬ࠦࡍࡅ࠷ࠣ࡬ࡦࡹࡨࠡࡨ࡬ࡰࡪࡀࠠࡼࡿࠪ౅").format(str(e)))
    return
  bstack1l111lll11_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"࠭ࡾࠨె")), bstack11ll1ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧే"))
  if not os.path.exists(bstack1l111lll11_opy_):
    os.makedirs(bstack1l111lll11_opy_)
  bstack11l1lllll1_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠨࢀࠪై")), bstack11ll1ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ౉"), bstack11ll1ll_opy_ (u"ࠪࡥࡵࡶࡕࡱ࡮ࡲࡥࡩࡓࡄ࠶ࡊࡤࡷ࡭࠴ࡪࡴࡱࡱࠫొ"))
  lock_file = bstack11l1lllll1_opy_ + bstack11ll1ll_opy_ (u"ࠫ࠳ࡲ࡯ࡤ࡭ࠪో")
  bstack1111l1l11_opy_ = {
    bstack11ll1ll_opy_ (u"ࠬ࡯ࡤࠨౌ"): bstack111111lll1_opy_,
    bstack11ll1ll_opy_ (u"࠭ࡴࡪ࡯ࡨࡷࡹࡧ࡭ࡱ్ࠩ"): datetime.datetime.strftime(datetime.datetime.now(), bstack11ll1ll_opy_ (u"ࠧࠦࡦ࠲ࠩࡲ࠵࡚ࠥࠢࠨࡌ࠿ࠫࡍ࠻ࠧࡖࠫ౎")),
    bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭౏"): str(__version__)
  }
  try:
    with FileLock(lock_file, timeout=10):
      bstack11ll11lll1_opy_ = {}
      if os.path.exists(bstack11l1lllll1_opy_):
        with open(bstack11l1lllll1_opy_, bstack11ll1ll_opy_ (u"ࠩࡵࠫ౐")) as f:
          content = f.read().strip()
          if content:
            bstack11ll11lll1_opy_ = json.loads(content)
      bstack11ll11lll1_opy_[md5_hash] = bstack1111l1l11_opy_
      with open(bstack11l1lllll1_opy_, bstack11ll1ll_opy_ (u"ࠥࡻࠧ౑")) as outfile:
        json.dump(bstack11ll11lll1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡻ࡮ࡺࡨࠡࡨ࡬ࡰࡪࠦ࡬ࡰࡥ࡮࡭ࡳ࡭ࠠࡧࡱࡵࠤࡒࡊ࠵ࠡࡪࡤࡷ࡭ࠦࡵࡱࡦࡤࡸࡪࡀࠠࡼࡿࠪ౒").format(str(e)))
def bstack1lllllll1l_opy_(self):
  return
def bstack11l11l1111_opy_(self):
  return
def bstack111l1lll1l_opy_():
  global bstack1l11l1ll1_opy_
  bstack1l11l1ll1_opy_ = True
@measure(event_name=EVENTS.bstack11l11l11l_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1ll11lll11_opy_(self):
  global bstack1lllll1ll1_opy_
  global bstack1111lll11l_opy_
  global bstack1l1ll1111l_opy_
  try:
    if bstack11ll1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ౓") in bstack1lllll1ll1_opy_ and self.session_id != None and bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡗࡹࡧࡴࡶࡵࠪ౔"), bstack11ll1ll_opy_ (u"ࠧࠨౕ")) != bstack11ll1ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥౖࠩ"):
      bstack1l11l1l1l_opy_ = bstack11ll1ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ౗") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack11ll1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪౘ")
      if bstack1l11l1l1l_opy_ == bstack11ll1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫౙ"):
        bstack1lllllll11_opy_(logger)
      if self != None:
        bstack11l1l111ll_opy_(self, bstack1l11l1l1l_opy_, bstack11ll1ll_opy_ (u"ࠬ࠲ࠠࠨౚ").join(threading.current_thread().bstackTestErrorMessages))
    threading.current_thread().testStatus = bstack11ll1ll_opy_ (u"࠭ࠧ౛")
    if bstack11ll1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ౜") in bstack1lllll1ll1_opy_ and getattr(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧౝ"), None):
      bstack1lll111l1_opy_.bstack11111lll_opy_(self, bstack1l1111l1ll_opy_, logger, wait=True)
    if bstack11ll1ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ౞") in bstack1lllll1ll1_opy_:
      if not threading.currentThread().behave_test_status:
        bstack11l1l111ll_opy_(self, bstack11ll1ll_opy_ (u"ࠥࡴࡦࡹࡳࡦࡦࠥ౟"))
      bstack111lllllll_opy_.bstack1ll1l11l1l_opy_(self)
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧౠ") + str(e))
  bstack1l1ll1111l_opy_(self)
  self.session_id = None
def bstack1l11111111_opy_(self, *args, **kwargs):
  try:
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    from bstack_utils.helper import bstack11llllll1l_opy_
    global bstack1lllll1ll1_opy_
    command_executor = kwargs.get(bstack11ll1ll_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡥࡥࡹࡧࡦࡹࡹࡵࡲࠨౡ"), bstack11ll1ll_opy_ (u"࠭ࠧౢ"))
    bstack1l111l1lll_opy_ = False
    if type(command_executor) == str and bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪౣ") in command_executor:
      bstack1l111l1lll_opy_ = True
    elif isinstance(command_executor, RemoteConnection) and bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡤࡱࡰࠫ౤") in str(getattr(command_executor, bstack11ll1ll_opy_ (u"ࠩࡢࡹࡷࡲࠧ౥"), bstack11ll1ll_opy_ (u"ࠪࠫ౦"))):
      bstack1l111l1lll_opy_ = True
    else:
      kwargs = bstack1lll11l11_opy_.bstack1ll1lll11l_opy_(bstack111ll1lll1_opy_=kwargs, config=CONFIG)
      return bstack1l1ll1l111_opy_(self, *args, **kwargs)
    if bstack1l111l1lll_opy_:
      bstack1ll11ll1l1_opy_ = bstack1111llll11_opy_.bstack111lll11l_opy_(CONFIG, bstack1lllll1ll1_opy_)
      if kwargs.get(bstack11ll1ll_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ౧")):
        kwargs[bstack11ll1ll_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭౨")] = bstack11llllll1l_opy_(kwargs[bstack11ll1ll_opy_ (u"࠭࡯ࡱࡶ࡬ࡳࡳࡹࠧ౩")], bstack1lllll1ll1_opy_, CONFIG, bstack1ll11ll1l1_opy_)
      elif kwargs.get(bstack11ll1ll_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ౪")):
        kwargs[bstack11ll1ll_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ౫")] = bstack11llllll1l_opy_(kwargs[bstack11ll1ll_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ౬")], bstack1lllll1ll1_opy_, CONFIG, bstack1ll11ll1l1_opy_)
  except Exception as e:
    logger.error(bstack11ll1ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬ࡪࡴࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤࡘࡊࡋࠡࡥࡤࡴࡸࡀࠠࡼࡿࠥ౭").format(str(e)))
  return bstack1l1ll1l111_opy_(self, *args, **kwargs)
@measure(event_name=EVENTS.bstack1l1l11l11l_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack11l1ll1l11_opy_(self, command_executor=bstack11ll1ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳࠶࠸࠷࠯࠲࠱࠴࠳࠷࠺࠵࠶࠷࠸ࠧ౮"), *args, **kwargs):
  global bstack1111lll11l_opy_
  global bstack11l1lll1l1_opy_
  bstack1ll1l1111_opy_ = bstack1l11111111_opy_(self, command_executor=command_executor, *args, **kwargs)
  if not bstack1l11l1l1_opy_.on():
    return bstack1ll1l1111_opy_
  try:
    logger.debug(bstack11ll1ll_opy_ (u"ࠬࡉ࡯࡮࡯ࡤࡲࡩࠦࡅࡹࡧࡦࡹࡹࡵࡲࠡࡹ࡫ࡩࡳࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢ࡬ࡷࠥ࡬ࡡ࡭ࡵࡨࠤ࠲ࠦࡻࡾࠩ౯").format(str(command_executor)))
    logger.debug(bstack11ll1ll_opy_ (u"࠭ࡈࡶࡤ࡙ࠣࡗࡒࠠࡪࡵࠣ࠱ࠥࢁࡽࠨ౰").format(str(command_executor._url)))
    from selenium.webdriver.remote.remote_connection import RemoteConnection
    if isinstance(command_executor, RemoteConnection) and bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡣࡰ࡯ࠪ౱") in command_executor._url:
      bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠࡵࡨࡷࡸ࡯࡯࡯ࠩ౲"), True)
  except:
    pass
  if (isinstance(command_executor, str) and bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ౳") in command_executor):
    bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡷࡪࡹࡳࡪࡱࡱࠫ౴"), True)
  threading.current_thread().bstackSessionDriver = self
  bstack11111l1l1_opy_ = getattr(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡘࡪࡹࡴࡎࡧࡷࡥࠬ౵"), None)
  bstack11llll111_opy_ = {}
  if self.capabilities is not None:
    bstack11llll111_opy_[bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫ౶")] = self.capabilities.get(bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ౷"))
    bstack11llll111_opy_[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ౸")] = self.capabilities.get(bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ౹"))
    bstack11llll111_opy_[bstack11ll1ll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࠪ౺")] = self.capabilities.get(bstack11ll1ll_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ౻"))
  if CONFIG.get(bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ౼"), False) and bstack1lll11l11_opy_.bstack1ll1l1l11_opy_(bstack11llll111_opy_):
    threading.current_thread().a11yPlatform = True
  if bstack11ll1ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ౽") in bstack1lllll1ll1_opy_ or bstack11ll1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ౾") in bstack1lllll1ll1_opy_:
    bstack1ll1l111_opy_.bstack11l1lllll_opy_(self)
  if bstack11ll1ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ౿") in bstack1lllll1ll1_opy_ and bstack11111l1l1_opy_ and bstack11111l1l1_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨಀ"), bstack11ll1ll_opy_ (u"ࠩࠪಁ")) == bstack11ll1ll_opy_ (u"ࠪࡴࡪࡴࡤࡪࡰࡪࠫಂ"):
    bstack1ll1l111_opy_.bstack11l1lllll_opy_(self)
  bstack1111lll11l_opy_ = self.session_id
  with bstack11ll11lll_opy_:
    bstack11l1lll1l1_opy_.append(self)
  return bstack1ll1l1111_opy_
def bstack1l11ll111l_opy_(args):
  return bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶࠬಃ") in str(args)
def bstack111l11ll11_opy_(self, driver_command, *args, **kwargs):
  global bstack1l1llllll_opy_
  global bstack1l1111ll1_opy_
  bstack1l1ll1l1ll_opy_ = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ಄"), None) and bstack1l1l1ll1_opy_(
          threading.current_thread(), bstack11ll1ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬಅ"), None)
  bstack1l11lll11l_opy_ = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧಆ"), None) and bstack1l1l1ll1_opy_(
          threading.current_thread(), bstack11ll1ll_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪಇ"), None)
  bstack1l111lll1l_opy_ = getattr(self, bstack11ll1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩಈ"), None) != None and getattr(self, bstack11ll1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪಉ"), None) == True
  if not bstack1l1111ll1_opy_ and bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫಊ") in CONFIG and CONFIG[bstack11ll1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬಋ")] == True and bstack11lll1l1l_opy_.bstack11l111l1ll_opy_(driver_command) and (bstack1l111lll1l_opy_ or bstack1l1ll1l1ll_opy_ or bstack1l11lll11l_opy_) and not bstack1l11ll111l_opy_(args):
    try:
      bstack1l1111ll1_opy_ = True
      logger.debug(bstack11ll1ll_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࢁࡽࠨಌ").format(driver_command))
      logger.debug(perform_scan(self, driver_command=driver_command))
    except Exception as err:
      logger.debug(bstack11ll1ll_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡴࡪࡸࡦࡰࡴࡰࠤࡸࡩࡡ࡯ࠢࡾࢁࠬ಍").format(str(err)))
    bstack1l1111ll1_opy_ = False
  response = bstack1l1llllll_opy_(self, driver_command, *args, **kwargs)
  if (bstack11ll1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧಎ") in str(bstack1lllll1ll1_opy_).lower() or bstack11ll1ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩಏ") in str(bstack1lllll1ll1_opy_).lower()) and bstack1l11l1l1_opy_.on():
    try:
      if driver_command == bstack11ll1ll_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧಐ"):
        bstack1ll1l111_opy_.bstack1ll11ll1ll_opy_({
            bstack11ll1ll_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࠪ಑"): response[bstack11ll1ll_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫಒ")],
            bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ಓ"): bstack1ll1l111_opy_.current_test_uuid() if bstack1ll1l111_opy_.current_test_uuid() else bstack1l11l1l1_opy_.current_hook_uuid()
        })
    except:
      pass
  return response
@measure(event_name=EVENTS.bstack11l11ll11_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1l1ll111ll_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None, *args, **kwargs):
  global CONFIG
  global bstack1111lll11l_opy_
  global bstack11111l11l_opy_
  global bstack11l1l1llll_opy_
  global bstack1llll11l11_opy_
  global bstack111l111l1_opy_
  global bstack1lllll1ll1_opy_
  global bstack1l1ll1l111_opy_
  global bstack11l1lll1l1_opy_
  global bstack1ll1ll111l_opy_
  global bstack1l1111l1ll_opy_
  if os.getenv(bstack11ll1ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬಔ")) is not None and bstack1lll11l11_opy_.bstack1l1l1l1l1l_opy_(CONFIG) is None:
    CONFIG[bstack11ll1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨಕ")] = True
  CONFIG[bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡔࡆࡎࠫಖ")] = str(bstack1lllll1ll1_opy_) + str(__version__)
  bstack1lll111lll_opy_ = os.environ[bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨಗ")]
  bstack1ll11ll1l1_opy_ = bstack1111llll11_opy_.bstack111lll11l_opy_(CONFIG, bstack1lllll1ll1_opy_)
  CONFIG[bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡪࡸࡦࡇࡻࡩ࡭ࡦࡘࡹ࡮ࡪࠧಘ")] = bstack1lll111lll_opy_
  CONFIG[bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡔࡷࡵࡤࡶࡥࡷࡑࡦࡶࠧಙ")] = bstack1ll11ll1l1_opy_
  if CONFIG.get(bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ಚ"),bstack11ll1ll_opy_ (u"ࠧࠨಛ")) and bstack11ll1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧಜ") in bstack1lllll1ll1_opy_:
    CONFIG[bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩಝ")].pop(bstack11ll1ll_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨಞ"), None)
    CONFIG[bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫಟ")].pop(bstack11ll1ll_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪಠ"), None)
  command_executor = bstack111l1l1111_opy_()
  logger.debug(bstack1ll11l11ll_opy_.format(command_executor))
  proxy = bstack1l11l1lll_opy_(CONFIG, proxy)
  bstack1l11111l1l_opy_ = 0 if bstack11111l11l_opy_ < 0 else bstack11111l11l_opy_
  try:
    if bstack1llll11l11_opy_ is True:
      bstack1l11111l1l_opy_ = int(multiprocessing.current_process().name)
    elif bstack111l111l1_opy_ is True:
      bstack1l11111l1l_opy_ = int(threading.current_thread().name)
  except:
    bstack1l11111l1l_opy_ = 0
  bstack1l11l11ll_opy_ = bstack1ll111llll_opy_(CONFIG, bstack1l11111l1l_opy_)
  logger.debug(bstack11l1111l1_opy_.format(str(bstack1l11l11ll_opy_)))
  if bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪಡ") in CONFIG and bstack11l1ll11l_opy_(CONFIG[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫಢ")]):
    bstack1l1l1l11l1_opy_(bstack1l11l11ll_opy_)
  if bstack1lll11l11_opy_.bstack1lll1ll1l1_opy_(CONFIG, bstack1l11111l1l_opy_) and bstack1lll11l11_opy_.bstack1ll1l11ll1_opy_(bstack1l11l11ll_opy_, options, desired_capabilities, CONFIG):
    threading.current_thread().a11yPlatform = True
    if (cli.accessibility is None or not cli.accessibility.is_enabled()):
      bstack1lll11l11_opy_.set_capabilities(bstack1l11l11ll_opy_, CONFIG)
  if desired_capabilities:
    bstack1l111l1l1_opy_ = bstack1ll111l11_opy_(desired_capabilities)
    bstack1l111l1l1_opy_[bstack11ll1ll_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨಣ")] = bstack1l11lllll_opy_(CONFIG)
    bstack1lll1lll1l_opy_ = bstack1ll111llll_opy_(bstack1l111l1l1_opy_)
    if bstack1lll1lll1l_opy_:
      bstack1l11l11ll_opy_ = update(bstack1lll1lll1l_opy_, bstack1l11l11ll_opy_)
    desired_capabilities = None
  if options:
    bstack111l11l11_opy_(options, bstack1l11l11ll_opy_)
  if not options:
    options = bstack1ll1ll1ll1_opy_(bstack1l11l11ll_opy_)
  bstack1l1111l1ll_opy_ = CONFIG.get(bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬತ"))[bstack1l11111l1l_opy_]
  if proxy and bstack11llll1111_opy_() >= version.parse(bstack11ll1ll_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪಥ")):
    options.proxy(proxy)
  if options and bstack11llll1111_opy_() >= version.parse(bstack11ll1ll_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪದ")):
    desired_capabilities = None
  if (
          not options and not desired_capabilities
  ) or (
          bstack11llll1111_opy_() < version.parse(bstack11ll1ll_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫಧ")) and not desired_capabilities
  ):
    desired_capabilities = {}
    desired_capabilities.update(bstack1l11l11ll_opy_)
  logger.info(bstack1lll1l11ll_opy_)
  bstack111l11l111_opy_.end(EVENTS.bstack11l1lll111_opy_.value, EVENTS.bstack11l1lll111_opy_.value + bstack11ll1ll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨನ"), EVENTS.bstack11l1lll111_opy_.value + bstack11ll1ll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ಩"), status=True, failure=None, test_name=bstack11l1l1llll_opy_)
  if bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡳࡶࡴ࡬ࡩ࡭ࡧࠪಪ") in kwargs:
    del kwargs[bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡴࡷࡵࡦࡪ࡮ࡨࠫಫ")]
  try:
    if bstack11llll1111_opy_() >= version.parse(bstack11ll1ll_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪಬ")):
      bstack1l1ll1l111_opy_(self, command_executor=command_executor,
                options=options, keep_alive=keep_alive, file_detector=file_detector, *args, **kwargs)
    elif bstack11llll1111_opy_() >= version.parse(bstack11ll1ll_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪಭ")):
      bstack1l1ll1l111_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities, options=options,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    elif bstack11llll1111_opy_() >= version.parse(bstack11ll1ll_opy_ (u"ࠬ࠸࠮࠶࠵࠱࠴ࠬಮ")):
      bstack1l1ll1l111_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive, file_detector=file_detector)
    else:
      bstack1l1ll1l111_opy_(self, command_executor=command_executor,
                desired_capabilities=desired_capabilities,
                browser_profile=browser_profile, proxy=proxy,
                keep_alive=keep_alive)
  except Exception as bstack111l111l1l_opy_:
    logger.error(bstack11l1l11lll_opy_.format(bstack11ll1ll_opy_ (u"࠭ࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠬಯ"), str(bstack111l111l1l_opy_)))
    raise bstack111l111l1l_opy_
  if bstack1lll11l11_opy_.bstack1lll1ll1l1_opy_(CONFIG, bstack1l11111l1l_opy_) and bstack1lll11l11_opy_.bstack1ll1l11ll1_opy_(self.caps, options, desired_capabilities):
    if CONFIG[bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡖࡲࡰࡦࡸࡧࡹࡓࡡࡱࠩರ")][bstack11ll1ll_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧಱ")] == True:
      threading.current_thread().appA11yPlatform = True
      if cli.accessibility is None or not cli.accessibility.is_enabled():
        bstack1lll11l11_opy_.set_capabilities(bstack1l11l11ll_opy_, CONFIG)
  try:
    bstack1l1l1l1l11_opy_ = bstack11ll1ll_opy_ (u"ࠩࠪಲ")
    if bstack11llll1111_opy_() >= version.parse(bstack11ll1ll_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࡤ࠴ࠫಳ")):
      if self.caps is not None:
        bstack1l1l1l1l11_opy_ = self.caps.get(bstack11ll1ll_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦ಴"))
    else:
      if self.capabilities is not None:
        bstack1l1l1l1l11_opy_ = self.capabilities.get(bstack11ll1ll_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧವ"))
    if bstack1l1l1l1l11_opy_:
      bstack11ll1l111_opy_(bstack1l1l1l1l11_opy_)
      if bstack11llll1111_opy_() <= version.parse(bstack11ll1ll_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ಶ")):
        self.command_executor._url = bstack11ll1ll_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣಷ") + bstack11lll11111_opy_ + bstack11ll1ll_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧಸ")
      else:
        self.command_executor._url = bstack11ll1ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦಹ") + bstack1l1l1l1l11_opy_ + bstack11ll1ll_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦ಺")
      logger.debug(bstack1lll1ll111_opy_.format(bstack1l1l1l1l11_opy_))
    else:
      logger.debug(bstack1ll1ll1111_opy_.format(bstack11ll1ll_opy_ (u"ࠦࡔࡶࡴࡪ࡯ࡤࡰࠥࡎࡵࡣࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧ಻")))
  except Exception as e:
    logger.debug(bstack1ll1ll1111_opy_.format(e))
  if bstack11ll1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷ಼ࠫ") in bstack1lllll1ll1_opy_:
    bstack1ll111l1l1_opy_(bstack11111l11l_opy_, bstack1ll1ll111l_opy_)
  bstack1111lll11l_opy_ = self.session_id
  if bstack11ll1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ಽ") in bstack1lllll1ll1_opy_ or bstack11ll1ll_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧಾ") in bstack1lllll1ll1_opy_ or bstack11ll1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧಿ") in bstack1lllll1ll1_opy_:
    threading.current_thread().bstackSessionId = self.session_id
    threading.current_thread().bstackSessionDriver = self
    threading.current_thread().bstackTestErrorMessages = []
  bstack11111l1l1_opy_ = getattr(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡖࡨࡷࡹࡓࡥࡵࡣࠪೀ"), None)
  if bstack11ll1ll_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪು") in bstack1lllll1ll1_opy_ or bstack11ll1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪೂ") in bstack1lllll1ll1_opy_:
    bstack1ll1l111_opy_.bstack11l1lllll_opy_(self)
  if bstack11ll1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬೃ") in bstack1lllll1ll1_opy_ and bstack11111l1l1_opy_ and bstack11111l1l1_opy_.get(bstack11ll1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ೄ"), bstack11ll1ll_opy_ (u"ࠧࠨ೅")) == bstack11ll1ll_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩೆ"):
    bstack1ll1l111_opy_.bstack11l1lllll_opy_(self)
  with bstack11ll11lll_opy_:
    bstack11l1lll1l1_opy_.append(self)
  if bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೇ") in CONFIG and bstack11ll1ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨೈ") in CONFIG[bstack11ll1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ೉")][bstack1l11111l1l_opy_]:
    bstack11l1l1llll_opy_ = CONFIG[bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨೊ")][bstack1l11111l1l_opy_][bstack11ll1ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫೋ")]
  logger.debug(bstack1lllll111l_opy_.format(bstack1111lll11l_opy_))
try:
  try:
    import Browser
    from subprocess import Popen
    from browserstack_sdk.__init__ import bstack1l11lll11_opy_
    def bstack1111l11lll_opy_(self, args, bufsize=-1, executable=None,
              stdin=None, stdout=None, stderr=None,
              preexec_fn=None, close_fds=True,
              shell=False, cwd=None, env=None, universal_newlines=None,
              startupinfo=None, creationflags=0,
              restore_signals=True, start_new_session=False,
              pass_fds=(), *, user=None, group=None, extra_groups=None,
              encoding=None, errors=None, text=None, umask=-1, pipesize=-1):
      global CONFIG
      global bstack1l1ll111l1_opy_
      if(bstack11ll1ll_opy_ (u"ࠢࡪࡰࡧࡩࡽ࠴ࡪࡴࠤೌ") in args[1]):
        with open(os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠨࢀ್ࠪ")), bstack11ll1ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩ೎"), bstack11ll1ll_opy_ (u"ࠪ࠲ࡸ࡫ࡳࡴ࡫ࡲࡲ࡮ࡪࡳ࠯ࡶࡻࡸࠬ೏")), bstack11ll1ll_opy_ (u"ࠫࡼ࠭೐")) as fp:
          fp.write(bstack11ll1ll_opy_ (u"ࠧࠨ೑"))
        if(not os.path.exists(os.path.join(os.path.dirname(args[1]), bstack11ll1ll_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣ೒")))):
          with open(args[1], bstack11ll1ll_opy_ (u"ࠧࡳࠩ೓")) as f:
            lines = f.readlines()
            index = next((i for i, line in enumerate(lines) if bstack11ll1ll_opy_ (u"ࠨࡣࡶࡽࡳࡩࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡢࡲࡪࡽࡐࡢࡩࡨࠬࡨࡵ࡮ࡵࡧࡻࡸ࠱ࠦࡰࡢࡩࡨࠤࡂࠦࡶࡰ࡫ࡧࠤ࠵࠯ࠧ೔") in line), None)
            if index is not None:
                lines.insert(index+2, bstack1ll111lll1_opy_)
            if bstack11ll1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ೕ") in CONFIG and str(CONFIG[bstack11ll1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧೖ")]).lower() != bstack11ll1ll_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ೗"):
                bstack1l11111l11_opy_ = bstack1l11lll11_opy_()
                bstack111lll1ll1_opy_ = bstack11ll1ll_opy_ (u"ࠬ࠭ࠧࠋ࠱࠭ࠤࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽ࠡࠬ࠲ࠎࡨࡵ࡮ࡴࡶࠣࡦࡸࡺࡡࡤ࡭ࡢࡴࡦࡺࡨࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࡝ࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶ࠯࡮ࡨࡲ࡬ࡺࡨࠡ࠯ࠣ࠷ࡢࡁࠊࡤࡱࡱࡷࡹࠦࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶࠤࡂࠦࡰࡳࡱࡦࡩࡸࡹ࠮ࡢࡴࡪࡺࡠࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠱࡞࠽ࠍࡧࡴࡴࡳࡵࠢࡳࡣ࡮ࡴࡤࡦࡺࠣࡁࠥࡶࡲࡰࡥࡨࡷࡸ࠴ࡡࡳࡩࡹ࡟ࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠸࡝࠼ࠌࡳࡶࡴࡩࡥࡴࡵ࠱ࡥࡷ࡭ࡶࠡ࠿ࠣࡴࡷࡵࡣࡦࡵࡶ࠲ࡦࡸࡧࡷ࠰ࡶࡰ࡮ࡩࡥࠩ࠲࠯ࠤࡵࡸ࡯ࡤࡧࡶࡷ࠳ࡧࡲࡨࡸ࠱ࡰࡪࡴࡧࡵࡪࠣ࠱ࠥ࠹ࠩ࠼ࠌࡦࡳࡳࡹࡴࠡ࡫ࡰࡴࡴࡸࡴࡠࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸ࠹ࡥࡢࡴࡶࡤࡧࡰࠦ࠽ࠡࡴࡨࡵࡺ࡯ࡲࡦࠪࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢࠪ࠽ࠍ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡰࡦࡻ࡮ࡤࡪࠣࡁࠥࡧࡳࡺࡰࡦࠤ࠭ࡲࡡࡶࡰࡦ࡬ࡔࡶࡴࡪࡱࡱࡷ࠮ࠦ࠽࠿ࠢࡾࡿࠏࠦࠠ࡭ࡧࡷࠤࡨࡧࡰࡴ࠽ࠍࠤࠥࡺࡲࡺࠢࡾࡿࠏࠦࠠࠡࠢࡦࡥࡵࡹࠠ࠾ࠢࡍࡗࡔࡔ࠮ࡱࡣࡵࡷࡪ࠮ࡢࡴࡶࡤࡧࡰࡥࡣࡢࡲࡶ࠭ࡀࠐࠠࠡࡿࢀࠤࡨࡧࡴࡤࡪࠣࠬࡪࡾࠩࠡࡽࡾࠎࠥࠦࠠࠡࡥࡲࡲࡸࡵ࡬ࡦ࠰ࡨࡶࡷࡵࡲࠩࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡶࡡࡳࡵࡨࠤࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ࠽ࠦ࠱ࠦࡥࡹࠫ࠾ࠎࠥࠦࡽࡾࠌࠣࠤࡷ࡫ࡴࡶࡴࡱࠤࡦࡽࡡࡪࡶࠣ࡭ࡲࡶ࡯ࡳࡶࡢࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺ࠴ࡠࡤࡶࡸࡦࡩ࡫࠯ࡥ࡫ࡶࡴࡳࡩࡶ࡯࠱ࡧࡴࡴ࡮ࡦࡥࡷࠬࢀࢁࠊࠡࠢࠣࠤࡼࡹࡅ࡯ࡦࡳࡳ࡮ࡴࡴ࠻ࠢࠪࡿࡨࡪࡰࡖࡴ࡯ࢁࠬࠦࠫࠡࡧࡱࡧࡴࡪࡥࡖࡔࡌࡇࡴࡳࡰࡰࡰࡨࡲࡹ࠮ࡊࡔࡑࡑ࠲ࡸࡺࡲࡪࡰࡪ࡭࡫ࡿࠨࡤࡣࡳࡷ࠮࠯ࠬࠋࠢࠣࠤࠥ࠴࠮࠯࡮ࡤࡹࡳࡩࡨࡐࡲࡷ࡭ࡴࡴࡳࠋࠢࠣࢁࢂ࠯࠻ࠋࡿࢀ࠿ࠏ࠵ࠪࠡ࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࡂࡃ࠽࠾࠿ࡀࡁࠥ࠰࠯ࠋࠩࠪࠫ೘").format(bstack1l11111l11_opy_=bstack1l11111l11_opy_)
            lines.insert(1, bstack111lll1ll1_opy_)
            f.seek(0)
            with open(os.path.join(os.path.dirname(args[1]), bstack11ll1ll_opy_ (u"ࠨࡩ࡯ࡦࡨࡼࡤࡨࡳࡵࡣࡦ࡯࠳ࡰࡳࠣ೙")), bstack11ll1ll_opy_ (u"ࠧࡸࠩ೚")) as bstack111ll111l1_opy_:
              bstack111ll111l1_opy_.writelines(lines)
        CONFIG[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡓࡅࡍࠪ೛")] = str(bstack1lllll1ll1_opy_) + str(__version__)
        bstack1lll111lll_opy_ = os.environ[bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ೜")]
        bstack1ll11ll1l1_opy_ = bstack1111llll11_opy_.bstack111lll11l_opy_(CONFIG, bstack1lllll1ll1_opy_)
        CONFIG[bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡩࡷࡥࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ೝ")] = bstack1lll111lll_opy_
        CONFIG[bstack11ll1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭ೞ")] = bstack1ll11ll1l1_opy_
        bstack1l11111l1l_opy_ = 0 if bstack11111l11l_opy_ < 0 else bstack11111l11l_opy_
        try:
          if bstack1llll11l11_opy_ is True:
            bstack1l11111l1l_opy_ = int(multiprocessing.current_process().name)
          elif bstack111l111l1_opy_ is True:
            bstack1l11111l1l_opy_ = int(threading.current_thread().name)
        except:
          bstack1l11111l1l_opy_ = 0
        CONFIG[bstack11ll1ll_opy_ (u"ࠧࡻࡳࡦ࡙࠶ࡇࠧ೟")] = False
        CONFIG[bstack11ll1ll_opy_ (u"ࠨࡩࡴࡒ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧೠ")] = True
        bstack1l11l11ll_opy_ = bstack1ll111llll_opy_(CONFIG, bstack1l11111l1l_opy_)
        logger.debug(bstack11l1111l1_opy_.format(str(bstack1l11l11ll_opy_)))
        if CONFIG.get(bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫೡ")):
          bstack1l1l1l11l1_opy_(bstack1l11l11ll_opy_)
        if bstack11ll1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫೢ") in CONFIG and bstack11ll1ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧೣ") in CONFIG[bstack11ll1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭೤")][bstack1l11111l1l_opy_]:
          bstack11l1l1llll_opy_ = CONFIG[bstack11ll1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ೥")][bstack1l11111l1l_opy_][bstack11ll1ll_opy_ (u"ࠬࡹࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪ೦")]
        args.append(os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"࠭ࡾࠨ೧")), bstack11ll1ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧ೨"), bstack11ll1ll_opy_ (u"ࠨ࠰ࡶࡩࡸࡹࡩࡰࡰ࡬ࡨࡸ࠴ࡴࡹࡶࠪ೩")))
        args.append(str(threading.get_ident()))
        args.append(json.dumps(bstack1l11l11ll_opy_))
        args[1] = os.path.join(os.path.dirname(args[1]), bstack11ll1ll_opy_ (u"ࠤ࡬ࡲࡩ࡫ࡸࡠࡤࡶࡸࡦࡩ࡫࠯࡬ࡶࠦ೪"))
      bstack1l1ll111l1_opy_ = True
      return bstack1ll1l1l111_opy_(self, args, bufsize=bufsize, executable=executable,
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
  def bstack1ll11l1111_opy_(self,
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
    global bstack11111l11l_opy_
    global bstack11l1l1llll_opy_
    global bstack1llll11l11_opy_
    global bstack111l111l1_opy_
    global bstack1lllll1ll1_opy_
    CONFIG[bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡕࡇࡏࠬ೫")] = str(bstack1lllll1ll1_opy_) + str(__version__)
    bstack1lll111lll_opy_ = os.environ[bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ೬")]
    bstack1ll11ll1l1_opy_ = bstack1111llll11_opy_.bstack111lll11l_opy_(CONFIG, bstack1lllll1ll1_opy_)
    CONFIG[bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶ࡫ࡹࡧࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨ೭")] = bstack1lll111lll_opy_
    CONFIG[bstack11ll1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨ೮")] = bstack1ll11ll1l1_opy_
    bstack1l11111l1l_opy_ = 0 if bstack11111l11l_opy_ < 0 else bstack11111l11l_opy_
    try:
      if bstack1llll11l11_opy_ is True:
        bstack1l11111l1l_opy_ = int(multiprocessing.current_process().name)
      elif bstack111l111l1_opy_ is True:
        bstack1l11111l1l_opy_ = int(threading.current_thread().name)
    except:
      bstack1l11111l1l_opy_ = 0
    CONFIG[bstack11ll1ll_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨ೯")] = True
    bstack1l11l11ll_opy_ = bstack1ll111llll_opy_(CONFIG, bstack1l11111l1l_opy_)
    logger.debug(bstack11l1111l1_opy_.format(str(bstack1l11l11ll_opy_)))
    if CONFIG.get(bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬ೰")):
      bstack1l1l1l11l1_opy_(bstack1l11l11ll_opy_)
    if bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬೱ") in CONFIG and bstack11ll1ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨೲ") in CONFIG[bstack11ll1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧೳ")][bstack1l11111l1l_opy_]:
      bstack11l1l1llll_opy_ = CONFIG[bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ೴")][bstack1l11111l1l_opy_][bstack11ll1ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫ೵")]
    import urllib
    import json
    if bstack11ll1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ೶") in CONFIG and str(CONFIG[bstack11ll1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ೷")]).lower() != bstack11ll1ll_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨ೸"):
        bstack11ll1ll11_opy_ = bstack1l11lll11_opy_()
        bstack1l11111l11_opy_ = bstack11ll1ll11_opy_ + urllib.parse.quote(json.dumps(bstack1l11l11ll_opy_))
    else:
        bstack1l11111l11_opy_ = bstack11ll1ll_opy_ (u"ࠪࡻࡸࡹ࠺࠰࠱ࡦࡨࡵ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮࠱ࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࡅࡣࡢࡲࡶࡁࠬ೹") + urllib.parse.quote(json.dumps(bstack1l11l11ll_opy_))
    browser = self.connect(bstack1l11111l11_opy_)
    return browser
except Exception as e:
    pass
def bstack11llll11l1_opy_():
    global bstack1l1ll111l1_opy_
    global bstack1lllll1ll1_opy_
    global CONFIG
    try:
        from playwright._impl._browser_type import BrowserType
        from bstack_utils.helper import bstack1l1ll1llll_opy_
        global bstack1llllll1l_opy_
        if not bstack1l1ll11l11_opy_:
          global bstack11lll111l1_opy_
          if not bstack11lll111l1_opy_:
            from bstack_utils.helper import bstack1lll11l1ll_opy_, bstack1llllllll1_opy_, bstack111ll111l_opy_
            bstack11lll111l1_opy_ = bstack1lll11l1ll_opy_()
            bstack1llllllll1_opy_(bstack1lllll1ll1_opy_)
            bstack1ll11ll1l1_opy_ = bstack1111llll11_opy_.bstack111lll11l_opy_(CONFIG, bstack1lllll1ll1_opy_)
            bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"ࠦࡕࡒࡁ࡚࡙ࡕࡍࡌࡎࡔࡠࡒࡕࡓࡉ࡛ࡃࡕࡡࡐࡅࡕࠨ೺"), bstack1ll11ll1l1_opy_)
          BrowserType.connect = bstack1l1ll1llll_opy_
          return
        BrowserType.launch = bstack1ll11l1111_opy_
        bstack1l1ll111l1_opy_ = True
    except Exception as e:
        pass
    try:
      import Browser
      from subprocess import Popen
      Popen.__init__ = bstack1111l11lll_opy_
      bstack1l1ll111l1_opy_ = True
    except Exception as e:
      pass
def bstack1ll11l11l1_opy_(context, bstack1l11l111l1_opy_):
  try:
    context.page.evaluate(bstack11ll1ll_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨ೻"), bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪ೼")+ json.dumps(bstack1l11l111l1_opy_) + bstack11ll1ll_opy_ (u"ࠢࡾࡿࠥ೽"))
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࡀࠠࡼࡿࠥ೾").format(str(e), traceback.format_exc()))
def bstack1l11l1l1l1_opy_(context, message, level):
  try:
    context.page.evaluate(bstack11ll1ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ೿"), bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨഀ") + json.dumps(message) + bstack11ll1ll_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧഁ") + json.dumps(level) + bstack11ll1ll_opy_ (u"ࠬࢃࡽࠨം"))
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾ࠼ࠣࡿࢂࠨഃ").format(str(e), traceback.format_exc()))
@measure(event_name=EVENTS.bstack1l1l11lll1_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack11l1l11111_opy_(self, url):
  global bstack111llll1l1_opy_
  try:
    bstack1llll1lll1_opy_(url)
  except Exception as err:
    logger.debug(bstack1llllll1ll_opy_.format(str(err)))
  try:
    bstack111llll1l1_opy_(self, url)
  except Exception as e:
    try:
      parsed_error = str(e)
      if any(err_msg in parsed_error for err_msg in bstack11lllll11l_opy_):
        bstack1llll1lll1_opy_(url, True)
    except Exception as err:
      logger.debug(bstack1llllll1ll_opy_.format(str(err)))
    raise e
def bstack111lllll1l_opy_(self):
  global bstack1l11ll111_opy_
  bstack1l11ll111_opy_ = self
  return
def bstack11l11111ll_opy_(self):
  global bstack11ll1l11l_opy_
  bstack11ll1l11l_opy_ = self
  return
def bstack111ll11ll1_opy_(test_name, bstack11111l111l_opy_):
  global CONFIG
  if percy.bstack11l1111ll_opy_() == bstack11ll1ll_opy_ (u"ࠢࡵࡴࡸࡩࠧഄ"):
    bstack1l111111ll_opy_ = os.path.relpath(bstack11111l111l_opy_, start=os.getcwd())
    suite_name, _ = os.path.splitext(bstack1l111111ll_opy_)
    bstack1111l1l1ll_opy_ = suite_name + bstack11ll1ll_opy_ (u"ࠣ࠯ࠥഅ") + test_name
    threading.current_thread().percySessionName = bstack1111l1l1ll_opy_
def bstack1111l11l1_opy_(self, test, *args, **kwargs):
  global bstack1ll111lll_opy_
  test_name = None
  bstack11111l111l_opy_ = None
  if test:
    test_name = str(test.name)
    bstack11111l111l_opy_ = str(test.source)
  bstack111ll11ll1_opy_(test_name, bstack11111l111l_opy_)
  bstack1ll111lll_opy_(self, test, *args, **kwargs)
@measure(event_name=EVENTS.bstack111l1l11l_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1111l1l11l_opy_(driver, bstack1111l1l1ll_opy_):
  if not bstack111l11l1ll_opy_ and bstack1111l1l1ll_opy_:
      bstack1ll1l1ll11_opy_ = {
          bstack11ll1ll_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩആ"): bstack11ll1ll_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫഇ"),
          bstack11ll1ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧഈ"): {
              bstack11ll1ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪഉ"): bstack1111l1l1ll_opy_
          }
      }
      bstack11l1ll1lll_opy_ = bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫഊ").format(json.dumps(bstack1ll1l1ll11_opy_))
      driver.execute_script(bstack11l1ll1lll_opy_)
  if bstack11lll1l111_opy_:
      bstack111l111111_opy_ = {
          bstack11ll1ll_opy_ (u"ࠧࡢࡥࡷ࡭ࡴࡴࠧഋ"): bstack11ll1ll_opy_ (u"ࠨࡣࡱࡲࡴࡺࡡࡵࡧࠪഌ"),
          bstack11ll1ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ഍"): {
              bstack11ll1ll_opy_ (u"ࠪࡨࡦࡺࡡࠨഎ"): bstack1111l1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠫࠥࡶࡡࡴࡵࡨࡨࠦ࠭ഏ"),
              bstack11ll1ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫഐ"): bstack11ll1ll_opy_ (u"࠭ࡩ࡯ࡨࡲࠫ഑")
          }
      }
      if bstack11lll1l111_opy_.status == bstack11ll1ll_opy_ (u"ࠧࡑࡃࡖࡗࠬഒ"):
          bstack1llll1l1ll_opy_ = bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࢂ࠭ഓ").format(json.dumps(bstack111l111111_opy_))
          driver.execute_script(bstack1llll1l1ll_opy_)
          bstack11l1l111ll_opy_(driver, bstack11ll1ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩഔ"))
      elif bstack11lll1l111_opy_.status == bstack11ll1ll_opy_ (u"ࠪࡊࡆࡏࡌࠨക"):
          reason = bstack11ll1ll_opy_ (u"ࠦࠧഖ")
          bstack1l111ll11_opy_ = bstack1111l1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠬࠦࡦࡢ࡫࡯ࡩࡩ࠭ഗ")
          if bstack11lll1l111_opy_.message:
              reason = str(bstack11lll1l111_opy_.message)
              bstack1l111ll11_opy_ = bstack1l111ll11_opy_ + bstack11ll1ll_opy_ (u"࠭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵ࠾ࠥ࠭ഘ") + reason
          bstack111l111111_opy_[bstack11ll1ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪങ")] = {
              bstack11ll1ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧച"): bstack11ll1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨഛ"),
              bstack11ll1ll_opy_ (u"ࠪࡨࡦࡺࡡࠨജ"): bstack1l111ll11_opy_
          }
          bstack1llll1l1ll_opy_ = bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩഝ").format(json.dumps(bstack111l111111_opy_))
          driver.execute_script(bstack1llll1l1ll_opy_)
          bstack11l1l111ll_opy_(driver, bstack11ll1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬഞ"), reason)
          bstack1ll1l11ll_opy_(reason, str(bstack11lll1l111_opy_), str(bstack11111l11l_opy_), logger)
@measure(event_name=EVENTS.bstack11l11l1lll_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack11lll1111_opy_(driver, test):
  if percy.bstack11l1111ll_opy_() == bstack11ll1ll_opy_ (u"ࠨࡴࡳࡷࡨࠦട") and percy.bstack11ll1l111l_opy_() == bstack11ll1ll_opy_ (u"ࠢࡵࡧࡶࡸࡨࡧࡳࡦࠤഠ"):
      bstack1l11111l1_opy_ = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫഡ"), None)
      bstack11ll1ll1l_opy_(driver, bstack1l11111l1_opy_, test)
  if (bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ഢ"), None) and
      bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩണ"), None)) or (
      bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫത"), None) and
      bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧഥ"), None)):
      logger.info(bstack11ll1ll_opy_ (u"ࠨࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠤࡕࡸ࡯ࡤࡧࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡩࡴࠢࡸࡲࡩ࡫ࡲࡸࡣࡼ࠲ࠥࠨദ"))
      bstack1lll11l11_opy_.bstack111ll1l1_opy_(driver, name=test.name, path=test.source)
def bstack111lll1l1l_opy_(test, bstack1111l1l1ll_opy_):
    try:
      bstack111111ll11_opy_ = datetime.datetime.now()
      data = {}
      if test:
        data[bstack11ll1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬധ")] = bstack1111l1l1ll_opy_
      if bstack11lll1l111_opy_:
        if bstack11lll1l111_opy_.status == bstack11ll1ll_opy_ (u"ࠨࡒࡄࡗࡘ࠭ന"):
          data[bstack11ll1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩഩ")] = bstack11ll1ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪപ")
        elif bstack11lll1l111_opy_.status == bstack11ll1ll_opy_ (u"ࠫࡋࡇࡉࡍࠩഫ"):
          data[bstack11ll1ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬബ")] = bstack11ll1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ഭ")
          if bstack11lll1l111_opy_.message:
            data[bstack11ll1ll_opy_ (u"ࠧࡳࡧࡤࡷࡴࡴࠧമ")] = str(bstack11lll1l111_opy_.message)
      user = CONFIG[bstack11ll1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪയ")]
      key = CONFIG[bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬര")]
      host = bstack111l111l11_opy_(cli.config, [bstack11ll1ll_opy_ (u"ࠥࡥࡵ࡯ࡳࠣറ"), bstack11ll1ll_opy_ (u"ࠦࡦࡻࡴࡰ࡯ࡤࡸࡪࠨല"), bstack11ll1ll_opy_ (u"ࠧࡧࡰࡪࠤള")], bstack11ll1ll_opy_ (u"ࠨࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡧࡴࡳࠢഴ"))
      url = bstack11ll1ll_opy_ (u"ࠧࡼࡿ࠲ࡥࡺࡺ࡯࡮ࡣࡷࡩ࠴ࡹࡥࡴࡵ࡬ࡳࡳࡹ࠯ࡼࡿ࠱࡮ࡸࡵ࡮ࠨവ").format(host, bstack1111lll11l_opy_)
      headers = {
        bstack11ll1ll_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡷࡽࡵ࡫ࠧശ"): bstack11ll1ll_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯࡫ࡵࡲࡲࠬഷ"),
      }
      if bool(data):
        requests.put(url, json=data, headers=headers, auth=(user, key))
        cli.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡷࡳࡨࡦࡺࡥࡠࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡶࡤࡸࡺࡹࠢസ"), datetime.datetime.now() - bstack111111ll11_opy_)
    except Exception as e:
      logger.error(bstack1l1ll1l1l1_opy_.format(str(e)))
def bstack1111ll1lll_opy_(test, bstack1111l1l1ll_opy_):
  global CONFIG
  global bstack11ll1l11l_opy_
  global bstack1l11ll111_opy_
  global bstack1111lll11l_opy_
  global bstack11lll1l111_opy_
  global bstack11l1l1llll_opy_
  global bstack11ll11ll11_opy_
  global bstack1l11l11111_opy_
  global bstack111l111lll_opy_
  global bstack1l1ll1ll1l_opy_
  global bstack11l1lll1l1_opy_
  global bstack1l1111l1ll_opy_
  global bstack1l1lll1l1l_opy_
  try:
    if not bstack1111lll11l_opy_:
      with bstack1l1lll1l1l_opy_:
        bstack1ll1lll11_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠫࢃ࠭ഹ")), bstack11ll1ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬഺ"), bstack11ll1ll_opy_ (u"࠭࠮ࡴࡧࡶࡷ࡮ࡵ࡮ࡪࡦࡶ࠲ࡹࡾࡴࠨ഻"))
        if os.path.exists(bstack1ll1lll11_opy_):
          with open(bstack1ll1lll11_opy_, bstack11ll1ll_opy_ (u"ࠧࡳ഼ࠩ")) as f:
            content = f.read().strip()
            if content:
              bstack1l11l11ll1_opy_ = json.loads(bstack11ll1ll_opy_ (u"ࠣࡽࠥഽ") + content + bstack11ll1ll_opy_ (u"ࠩࠥࡼࠧࡀࠠࠣࡻࠥࠫാ") + bstack11ll1ll_opy_ (u"ࠥࢁࠧി"))
              bstack1111lll11l_opy_ = bstack1l11l11ll1_opy_.get(str(threading.get_ident()))
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡶࡪࡧࡤࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡏࡄࡴࠢࡩ࡭ࡱ࡫࠺ࠡࠩീ") + str(e))
  if bstack11l1lll1l1_opy_:
    with bstack11ll11lll_opy_:
      bstack1111111l1_opy_ = bstack11l1lll1l1_opy_.copy()
    for driver in bstack1111111l1_opy_:
      if bstack1111lll11l_opy_ == driver.session_id:
        if test:
          bstack11lll1111_opy_(driver, test)
        bstack1111l1l11l_opy_(driver, bstack1111l1l1ll_opy_)
  elif bstack1111lll11l_opy_:
    bstack111lll1l1l_opy_(test, bstack1111l1l1ll_opy_)
  if bstack11ll1l11l_opy_:
    bstack1l11l11111_opy_(bstack11ll1l11l_opy_)
  if bstack1l11ll111_opy_:
    bstack111l111lll_opy_(bstack1l11ll111_opy_)
  if bstack1l11l1ll1_opy_:
    bstack1l1ll1ll1l_opy_()
def bstack11111lllll_opy_(self, test, *args, **kwargs):
  bstack1111l1l1ll_opy_ = None
  if test:
    bstack1111l1l1ll_opy_ = str(test.name)
  bstack1111ll1lll_opy_(test, bstack1111l1l1ll_opy_)
  bstack11ll11ll11_opy_(self, test, *args, **kwargs)
def bstack1l1l1lll1_opy_(self, parent, test, skip_on_failure=None, rpa=False):
  global bstack1ll1l11lll_opy_
  global CONFIG
  global bstack11l1lll1l1_opy_
  global bstack1111lll11l_opy_
  global bstack1l1lll1l1l_opy_
  bstack1l11l1l11l_opy_ = None
  try:
    if bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫു"), None) or bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨൂ"), None):
      try:
        if not bstack1111lll11l_opy_:
          bstack1ll1lll11_opy_ = os.path.join(os.path.expanduser(bstack11ll1ll_opy_ (u"ࠧࡿࠩൃ")), bstack11ll1ll_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨൄ"), bstack11ll1ll_opy_ (u"ࠩ࠱ࡷࡪࡹࡳࡪࡱࡱ࡭ࡩࡹ࠮ࡵࡺࡷࠫ൅"))
          with bstack1l1lll1l1l_opy_:
            if os.path.exists(bstack1ll1lll11_opy_):
              with open(bstack1ll1lll11_opy_, bstack11ll1ll_opy_ (u"ࠪࡶࠬെ")) as f:
                content = f.read().strip()
                if content:
                  bstack1l11l11ll1_opy_ = json.loads(bstack11ll1ll_opy_ (u"ࠦࢀࠨേ") + content + bstack11ll1ll_opy_ (u"ࠬࠨࡸࠣ࠼ࠣࠦࡾࠨࠧൈ") + bstack11ll1ll_opy_ (u"ࠨࡽࠣ൉"))
                  bstack1111lll11l_opy_ = bstack1l11l11ll1_opy_.get(str(threading.get_ident()))
      except Exception as e:
        logger.debug(bstack11ll1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡲࡦࡣࡧ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡋࡇࡷࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࠦࡴࡦࡵࡷࠤࡸࡺࡡࡵࡷࡶ࠾ࠥ࠭ൊ") + str(e))
      if bstack11l1lll1l1_opy_:
        with bstack11ll11lll_opy_:
          bstack1111111l1_opy_ = bstack11l1lll1l1_opy_.copy()
        for driver in bstack1111111l1_opy_:
          if bstack1111lll11l_opy_ == driver.session_id:
            bstack1l11l1l11l_opy_ = driver
    bstack1ll111l11l_opy_ = bstack1lll11l11_opy_.bstack11llll11ll_opy_(test.tags)
    if bstack1l11l1l11l_opy_:
      threading.current_thread().isA11yTest = bstack1lll11l11_opy_.bstack1ll1ll1l11_opy_(bstack1l11l1l11l_opy_, bstack1ll111l11l_opy_)
      threading.current_thread().isAppA11yTest = bstack1lll11l11_opy_.bstack1ll1ll1l11_opy_(bstack1l11l1l11l_opy_, bstack1ll111l11l_opy_)
    else:
      threading.current_thread().isA11yTest = bstack1ll111l11l_opy_
      threading.current_thread().isAppA11yTest = bstack1ll111l11l_opy_
  except:
    pass
  bstack1ll1l11lll_opy_(self, parent, test, skip_on_failure=skip_on_failure, rpa=rpa)
  global bstack11lll1l111_opy_
  try:
    bstack11lll1l111_opy_ = self._test
  except:
    bstack11lll1l111_opy_ = self.test
def bstack11l111llll_opy_():
  global bstack1l1l1ll111_opy_
  try:
    if os.path.exists(bstack1l1l1ll111_opy_):
      os.remove(bstack1l1l1ll111_opy_)
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡨࡪࡲࡥࡵ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫോ") + str(e))
def bstack1l11l1llll_opy_():
  global bstack1l1l1ll111_opy_
  bstack1l1llll1l1_opy_ = {}
  lock_file = bstack1l1l1ll111_opy_ + bstack11ll1ll_opy_ (u"ࠩ࠱ࡰࡴࡩ࡫ࠨൌ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll1ll_opy_ (u"ࠪࡪ࡮ࡲࡥ࡭ࡱࡦ࡯ࠥࡴ࡯ࡵࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥࡨࡡࡴ࡫ࡦࠤ࡫࡯࡬ࡦࠢࡲࡴࡪࡸࡡࡵ࡫ࡲࡲࡸ്࠭"))
    try:
      if not os.path.isfile(bstack1l1l1ll111_opy_):
        with open(bstack1l1l1ll111_opy_, bstack11ll1ll_opy_ (u"ࠫࡼ࠭ൎ")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1l1l1ll111_opy_):
        with open(bstack1l1l1ll111_opy_, bstack11ll1ll_opy_ (u"ࠬࡸࠧ൏")) as f:
          content = f.read().strip()
          if content:
            bstack1l1llll1l1_opy_ = json.loads(content)
    except Exception as e:
      logger.debug(bstack11ll1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡴࡨࡥࡩ࡯࡮ࡨࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨ൐") + str(e))
    return bstack1l1llll1l1_opy_
  try:
    os.makedirs(os.path.dirname(bstack1l1l1ll111_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      if not os.path.isfile(bstack1l1l1ll111_opy_):
        with open(bstack1l1l1ll111_opy_, bstack11ll1ll_opy_ (u"ࠧࡸࠩ൑")) as f:
          json.dump({}, f)
      if os.path.exists(bstack1l1l1ll111_opy_):
        with open(bstack1l1l1ll111_opy_, bstack11ll1ll_opy_ (u"ࠨࡴࠪ൒")) as f:
          content = f.read().strip()
          if content:
            bstack1l1llll1l1_opy_ = json.loads(content)
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡷ࡫ࡡࡥ࡫ࡱ࡫ࠥࡸ࡯ࡣࡱࡷࠤࡷ࡫ࡰࡰࡴࡷࠤ࡫࡯࡬ࡦ࠼ࠣࠫ൓") + str(e))
  finally:
    return bstack1l1llll1l1_opy_
def bstack1ll111l1l1_opy_(platform_index, item_index):
  global bstack1l1l1ll111_opy_
  lock_file = bstack1l1l1ll111_opy_ + bstack11ll1ll_opy_ (u"ࠪ࠲ࡱࡵࡣ࡬ࠩൔ")
  try:
    from filelock import FileLock
  except ImportError:
    logger.debug(bstack11ll1ll_opy_ (u"ࠫ࡫࡯࡬ࡦ࡮ࡲࡧࡰࠦ࡮ࡰࡶࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡢࡢࡵ࡬ࡧࠥ࡬ࡩ࡭ࡧࠣࡳࡵ࡫ࡲࡢࡶ࡬ࡳࡳࡹࠧൕ"))
    try:
      bstack1l1llll1l1_opy_ = {}
      if os.path.exists(bstack1l1l1ll111_opy_):
        with open(bstack1l1l1ll111_opy_, bstack11ll1ll_opy_ (u"ࠬࡸࠧൖ")) as f:
          content = f.read().strip()
          if content:
            bstack1l1llll1l1_opy_ = json.loads(content)
      bstack1l1llll1l1_opy_[item_index] = platform_index
      with open(bstack1l1l1ll111_opy_, bstack11ll1ll_opy_ (u"ࠨࡷࠣൗ")) as outfile:
        json.dump(bstack1l1llll1l1_opy_, outfile)
    except Exception as e:
      logger.debug(bstack11ll1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡺࡶ࡮ࡺࡩ࡯ࡩࠣࡸࡴࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠥ࡬ࡩ࡭ࡧ࠽ࠤࠬ൘") + str(e))
    return
  try:
    os.makedirs(os.path.dirname(bstack1l1l1ll111_opy_), exist_ok=True)
    with FileLock(lock_file, timeout=10):
      bstack1l1llll1l1_opy_ = {}
      if os.path.exists(bstack1l1l1ll111_opy_):
        with open(bstack1l1l1ll111_opy_, bstack11ll1ll_opy_ (u"ࠨࡴࠪ൙")) as f:
          content = f.read().strip()
          if content:
            bstack1l1llll1l1_opy_ = json.loads(content)
      bstack1l1llll1l1_opy_[item_index] = platform_index
      with open(bstack1l1l1ll111_opy_, bstack11ll1ll_opy_ (u"ࠤࡺࠦ൚")) as outfile:
        json.dump(bstack1l1llll1l1_opy_, outfile)
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡽࡲࡪࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡵࡳࡧࡵࡴࠡࡴࡨࡴࡴࡸࡴࠡࡨ࡬ࡰࡪࡀࠠࠨ൛") + str(e))
def bstack1l1l11l1l1_opy_(bstack1111111ll_opy_):
  global CONFIG
  bstack11lllll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠫࠬ൜")
  if not bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ൝") in CONFIG:
    logger.info(bstack11ll1ll_opy_ (u"࠭ࡎࡰࠢࡳࡰࡦࡺࡦࡰࡴࡰࡷࠥࡶࡡࡴࡵࡨࡨࠥࡻ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡩࡨࡲࡪࡸࡡࡵࡧࠣࡶࡪࡶ࡯ࡳࡶࠣࡪࡴࡸࠠࡓࡱࡥࡳࡹࠦࡲࡶࡰࠪ൞"))
  try:
    platform = CONFIG[bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪൟ")][bstack1111111ll_opy_]
    if bstack11ll1ll_opy_ (u"ࠨࡱࡶࠫൠ") in platform:
      bstack11lllll1ll_opy_ += str(platform[bstack11ll1ll_opy_ (u"ࠩࡲࡷࠬൡ")]) + bstack11ll1ll_opy_ (u"ࠪ࠰ࠥ࠭ൢ")
    if bstack11ll1ll_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧൣ") in platform:
      bstack11lllll1ll_opy_ += str(platform[bstack11ll1ll_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ൤")]) + bstack11ll1ll_opy_ (u"࠭ࠬࠡࠩ൥")
    if bstack11ll1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫ൦") in platform:
      bstack11lllll1ll_opy_ += str(platform[bstack11ll1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ൧")]) + bstack11ll1ll_opy_ (u"ࠩ࠯ࠤࠬ൨")
    if bstack11ll1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ൩") in platform:
      bstack11lllll1ll_opy_ += str(platform[bstack11ll1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳ࠭൪")]) + bstack11ll1ll_opy_ (u"ࠬ࠲ࠠࠨ൫")
    if bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ൬") in platform:
      bstack11lllll1ll_opy_ += str(platform[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ൭")]) + bstack11ll1ll_opy_ (u"ࠨ࠮ࠣࠫ൮")
    if bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ൯") in platform:
      bstack11lllll1ll_opy_ += str(platform[bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ൰")]) + bstack11ll1ll_opy_ (u"ࠫ࠱ࠦࠧ൱")
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"࡙ࠬ࡯࡮ࡧࠣࡩࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥ࡯ࡧࡵࡥࡹ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡺࡲࡪࡰࡪࠤ࡫ࡵࡲࠡࡴࡨࡴࡴࡸࡴࠡࡩࡨࡲࡪࡸࡡࡵ࡫ࡲࡲࠬ൲") + str(e))
  finally:
    if bstack11lllll1ll_opy_[len(bstack11lllll1ll_opy_) - 2:] == bstack11ll1ll_opy_ (u"࠭ࠬࠡࠩ൳"):
      bstack11lllll1ll_opy_ = bstack11lllll1ll_opy_[:-2]
    return bstack11lllll1ll_opy_
def bstack11l11111l_opy_(path, bstack11lllll1ll_opy_):
  try:
    import xml.etree.ElementTree as ET
    bstack1111ll11ll_opy_ = ET.parse(path)
    bstack1lllllllll_opy_ = bstack1111ll11ll_opy_.getroot()
    bstack1l11ll1ll_opy_ = None
    for suite in bstack1lllllllll_opy_.iter(bstack11ll1ll_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭൴")):
      if bstack11ll1ll_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ൵") in suite.attrib:
        suite.attrib[bstack11ll1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ൶")] += bstack11ll1ll_opy_ (u"ࠪࠤࠬ൷") + bstack11lllll1ll_opy_
        bstack1l11ll1ll_opy_ = suite
    bstack11111l11l1_opy_ = None
    for robot in bstack1lllllllll_opy_.iter(bstack11ll1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ൸")):
      bstack11111l11l1_opy_ = robot
    bstack1llllll11l_opy_ = len(bstack11111l11l1_opy_.findall(bstack11ll1ll_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫ൹")))
    if bstack1llllll11l_opy_ == 1:
      bstack11111l11l1_opy_.remove(bstack11111l11l1_opy_.findall(bstack11ll1ll_opy_ (u"࠭ࡳࡶ࡫ࡷࡩࠬൺ"))[0])
      bstack1ll11l11l_opy_ = ET.Element(bstack11ll1ll_opy_ (u"ࠧࡴࡷ࡬ࡸࡪ࠭ൻ"), attrib={bstack11ll1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ർ"): bstack11ll1ll_opy_ (u"ࠩࡖࡹ࡮ࡺࡥࡴࠩൽ"), bstack11ll1ll_opy_ (u"ࠪ࡭ࡩ࠭ൾ"): bstack11ll1ll_opy_ (u"ࠫࡸ࠶ࠧൿ")})
      bstack11111l11l1_opy_.insert(1, bstack1ll11l11l_opy_)
      bstack11ll11l11l_opy_ = None
      for suite in bstack11111l11l1_opy_.iter(bstack11ll1ll_opy_ (u"ࠬࡹࡵࡪࡶࡨࠫ඀")):
        bstack11ll11l11l_opy_ = suite
      bstack11ll11l11l_opy_.append(bstack1l11ll1ll_opy_)
      bstack1l11l1l1ll_opy_ = None
      for status in bstack1l11ll1ll_opy_.iter(bstack11ll1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ඁ")):
        bstack1l11l1l1ll_opy_ = status
      bstack11ll11l11l_opy_.append(bstack1l11l1l1ll_opy_)
    bstack1111ll11ll_opy_.write(path)
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡳ࡫ࡲࡢࡶ࡬ࡲ࡬ࠦࡲࡰࡤࡲࡸࠥࡸࡥࡱࡱࡵࡸࠬං") + str(e))
def bstack11l1111ll1_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name):
  global bstack111ll111ll_opy_
  global CONFIG
  if bstack11ll1ll_opy_ (u"ࠣࡲࡼࡸ࡭ࡵ࡮ࡱࡣࡷ࡬ࠧඃ") in options:
    del options[bstack11ll1ll_opy_ (u"ࠤࡳࡽࡹ࡮࡯࡯ࡲࡤࡸ࡭ࠨ඄")]
  json_data = bstack1l11l1llll_opy_()
  for item_id in json_data.keys():
    path = os.path.join(os.getcwd(), bstack11ll1ll_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࡡࡵࡩࡸࡻ࡬ࡵࡵࠪඅ"), str(item_id), bstack11ll1ll_opy_ (u"ࠫࡴࡻࡴࡱࡷࡷ࠲ࡽࡳ࡬ࠨආ"))
    bstack11l11111l_opy_(path, bstack1l1l11l1l1_opy_(json_data[item_id]))
  bstack11l111llll_opy_()
  return bstack111ll111ll_opy_(outs_dir, pabot_args, options, start_time_string, tests_root_name)
def bstack1llll1l111_opy_(self, ff_profile_dir):
  global bstack1111l11l11_opy_
  if not ff_profile_dir:
    return None
  return bstack1111l11l11_opy_(self, ff_profile_dir)
def bstack11ll1l1l11_opy_(datasources, opts_for_run, outs_dir, pabot_args, suite_group):
  from pabot.pabot import QueueItem
  global CONFIG
  global bstack11ll1lll1l_opy_
  bstack1111ll111l_opy_ = []
  if bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨඇ") in CONFIG:
    bstack1111ll111l_opy_ = CONFIG[bstack11ll1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩඈ")]
  return [
    QueueItem(
      datasources,
      outs_dir,
      opts_for_run,
      suite,
      pabot_args[bstack11ll1ll_opy_ (u"ࠢࡤࡱࡰࡱࡦࡴࡤࠣඉ")],
      pabot_args[bstack11ll1ll_opy_ (u"ࠣࡸࡨࡶࡧࡵࡳࡦࠤඊ")],
      argfile,
      pabot_args.get(bstack11ll1ll_opy_ (u"ࠤ࡫࡭ࡻ࡫ࠢඋ")),
      pabot_args[bstack11ll1ll_opy_ (u"ࠥࡴࡷࡵࡣࡦࡵࡶࡩࡸࠨඌ")],
      platform[0],
      bstack11ll1lll1l_opy_
    )
    for suite in suite_group
    for argfile in pabot_args[bstack11ll1ll_opy_ (u"ࠦࡦࡸࡧࡶ࡯ࡨࡲࡹ࡬ࡩ࡭ࡧࡶࠦඍ")] or [(bstack11ll1ll_opy_ (u"ࠧࠨඎ"), None)]
    for platform in enumerate(bstack1111ll111l_opy_)
  ]
def bstack1ll1ll111_opy_(self, datasources, outs_dir, options,
                        execution_item, command, verbose, argfile,
                        hive=None, processes=0, platform_index=0, bstack1l1l1ll1ll_opy_=bstack11ll1ll_opy_ (u"࠭ࠧඏ")):
  global bstack1111ll111_opy_
  self.platform_index = platform_index
  self.bstack111l1l1ll_opy_ = bstack1l1l1ll1ll_opy_
  bstack1111ll111_opy_(self, datasources, outs_dir, options,
                      execution_item, command, verbose, argfile, hive, processes)
def bstack1l1ll111l_opy_(caller_id, datasources, is_last, item, outs_dir):
  global bstack11lll11l1_opy_
  global bstack1l1lll1l11_opy_
  bstack11ll1lll11_opy_ = copy.deepcopy(item)
  if not bstack11ll1ll_opy_ (u"ࠧࡷࡣࡵ࡭ࡦࡨ࡬ࡦࠩඐ") in item.options:
    bstack11ll1lll11_opy_.options[bstack11ll1ll_opy_ (u"ࠨࡸࡤࡶ࡮ࡧࡢ࡭ࡧࠪඑ")] = []
  bstack1lllll1111_opy_ = bstack11ll1lll11_opy_.options[bstack11ll1ll_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫඒ")].copy()
  for v in bstack11ll1lll11_opy_.options[bstack11ll1ll_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬඓ")]:
    if bstack11ll1ll_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡔࡑࡇࡔࡇࡑࡕࡑࡎࡔࡄࡆ࡚ࠪඔ") in v:
      bstack1lllll1111_opy_.remove(v)
    if bstack11ll1ll_opy_ (u"ࠬࡈࡓࡕࡃࡆࡏࡈࡒࡉࡂࡔࡊࡗࠬඕ") in v:
      bstack1lllll1111_opy_.remove(v)
    if bstack11ll1ll_opy_ (u"࠭ࡂࡔࡖࡄࡇࡐࡊࡅࡇࡎࡒࡇࡆࡒࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪඖ") in v:
      bstack1lllll1111_opy_.remove(v)
  bstack1lllll1111_opy_.insert(0, bstack11ll1ll_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝ࡀࡻࡾࠩ඗").format(bstack11ll1lll11_opy_.platform_index))
  bstack1lllll1111_opy_.insert(0, bstack11ll1ll_opy_ (u"ࠨࡄࡖࡘࡆࡉࡋࡅࡇࡉࡐࡔࡉࡁࡍࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖ࠿ࢁࡽࠨ඘").format(bstack11ll1lll11_opy_.bstack111l1l1ll_opy_))
  bstack11ll1lll11_opy_.options[bstack11ll1ll_opy_ (u"ࠩࡹࡥࡷ࡯ࡡࡣ࡮ࡨࠫ඙")] = bstack1lllll1111_opy_
  if bstack1l1lll1l11_opy_:
    bstack11ll1lll11_opy_.options[bstack11ll1ll_opy_ (u"ࠪࡺࡦࡸࡩࡢࡤ࡯ࡩࠬක")].insert(0, bstack11ll1ll_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖ࠾ࢀࢃࠧඛ").format(bstack1l1lll1l11_opy_))
  return bstack11lll11l1_opy_(caller_id, datasources, is_last, bstack11ll1lll11_opy_, outs_dir)
def bstack1l1l1l111l_opy_(command, item_index):
  try:
    if bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡤࡹࡥࡴࡵ࡬ࡳࡳ࠭ග")):
      os.environ[bstack11ll1ll_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧඝ")] = json.dumps(CONFIG[bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪඞ")][item_index % bstack11ll111ll_opy_])
    global bstack1l1lll1l11_opy_
    if bstack1l1lll1l11_opy_:
      command[0] = command[0].replace(bstack11ll1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧඟ"), bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠮ࡵࡧ࡯ࠥࡸ࡯ࡣࡱࡷ࠱࡮ࡴࡴࡦࡴࡱࡥࡱࠦ࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢ࡭ࡳࡪࡥࡹࠢࠪච") + str(item_index % bstack11ll111ll_opy_) + bstack11ll1ll_opy_ (u"ࠪࠤ࠲࠳ࡢࡴࡶࡤࡧࡰࡥࡩࡵࡧࡰࡣ࡮ࡴࡤࡦࡺࠣࠫඡ") + str(
        item_index) + bstack11ll1ll_opy_ (u"ࠫࠥ࠭ජ") + bstack1l1lll1l11_opy_, 1)
    else:
      command[0] = command[0].replace(bstack11ll1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫඣ"),
                                      bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠲ࡹࡤ࡬ࠢࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠣ࠱࠲ࡨࡳࡵࡣࡦ࡯ࡤࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡪࡰࡧࡩࡽࠦࠧඤ") +  str(item_index % bstack11ll111ll_opy_) + bstack11ll1ll_opy_ (u"ࠧࠡ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢ࡭ࡹ࡫࡭ࡠ࡫ࡱࡨࡪࡾࠠࠨඥ") + str(item_index), 1)
  except Exception as e:
    logger.error(bstack11ll1ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠ࡮ࡱࡧ࡭࡫ࡿࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡢࡰࡧࠤ࡫ࡵࡲࠡࡲࡤࡦࡴࡺࠠࡳࡷࡱ࠾ࠥࢁࡽࠨඦ").format(str(e)))
def bstack1111llllll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index):
  global bstack1ll1l1l1l_opy_
  try:
    bstack1l1l1l111l_opy_(command, item_index)
    return bstack1ll1l1l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
  except Exception as e:
    logger.error(bstack11ll1ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡵࡧࡢࡰࡶࠣࡶࡺࡴ࠺ࠡࡽࢀࠫට").format(str(e)))
    raise e
def bstack11l1ll1ll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir):
  global bstack1ll1l1l1l_opy_
  try:
    bstack1l1l1l111l_opy_(command, item_index)
    return bstack1ll1l1l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
  except Exception as e:
    logger.error(bstack11ll1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠴࠱࠵࠸ࡀࠠࡼࡿࠪඨ").format(str(e)))
    try:
      return bstack1ll1l1l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index)
    except Exception as e2:
      logger.error(bstack11ll1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࠸࠮࠲࠵ࠣࡪࡦࡲ࡬ࡣࡣࡦ࡯࠿ࠦࡻࡾࠩඩ").format(str(e2)))
      raise e
def bstack1llll111l1_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout):
  global bstack1ll1l1l1l_opy_
  try:
    bstack1l1l1l111l_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    return bstack1ll1l1l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
  except Exception as e:
    logger.error(bstack11ll1ll_opy_ (u"ࠬࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡱࡣࡥࡳࡹࠦࡲࡶࡰࠣ࠶࠳࠷࠵࠻ࠢࡾࢁࠬඪ").format(str(e)))
    try:
      return bstack1ll1l1l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir)
    except Exception as e2:
      logger.error(bstack11ll1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡲࡤࡦࡴࡺࠠ࠳࠰࠴࠹ࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫණ").format(str(e2)))
      raise e
def _1111ll1ll1_opy_(bstack11l111111_opy_, item_index, process_timeout, sleep_before_start, bstack11l1l1111l_opy_):
  bstack1l1l1l111l_opy_(bstack11l111111_opy_, item_index)
  if process_timeout is None:
    process_timeout = 3600
  if sleep_before_start and sleep_before_start > 0:
    time.sleep(min(sleep_before_start, 5))
  return process_timeout
def bstack11l11lll1l_opy_(command, bstack111llll111_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1ll1l1l1l_opy_
  try:
    bstack1l1l1l111l_opy_(command, item_index)
    if process_timeout is None:
      process_timeout = 3600
    if sleep_before_start and sleep_before_start > 0:
      time.sleep(min(sleep_before_start, 5))
    return bstack1ll1l1l1l_opy_(command, bstack111llll111_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11ll1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡳࡥࡧࡵࡴࠡࡴࡸࡲࠥ࠻࠮࠱࠼ࠣࡿࢂ࠭ඬ").format(str(e)))
    try:
      return bstack1ll1l1l1l_opy_(command, bstack111llll111_opy_, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11ll1ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣࡴࡦࡨ࡯ࡵࠢࡩࡥࡱࡲࡢࡢࡥ࡮࠾ࠥࢁࡽࠨත").format(str(e2)))
      raise e
def bstack1l11l11lll_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start):
  global bstack1ll1l1l1l_opy_
  try:
    process_timeout = _1111ll1ll1_opy_(command, item_index, process_timeout, sleep_before_start, bstack11ll1ll_opy_ (u"ࠩ࠷࠲࠷࠭ථ"))
    return bstack1ll1l1l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout, sleep_before_start)
  except Exception as e:
    logger.error(bstack11ll1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡶࡡࡣࡱࡷࠤࡷࡻ࡮ࠡ࠶࠱࠶࠿ࠦࡻࡾࠩද").format(str(e)))
    try:
      return bstack1ll1l1l1l_opy_(command, stderr, stdout, item_name, verbose, pool_id, item_index, outs_dir, process_timeout)
    except Exception as e2:
      logger.error(bstack11ll1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡰࡢࡤࡲࡸࠥ࡬ࡡ࡭࡮ࡥࡥࡨࡱ࠺ࠡࡽࢀࠫධ").format(str(e2)))
      raise e
def is_driver_active(driver):
  return True if driver and driver.session_id else False
def bstack11ll1l1l1l_opy_(self, runner, quiet=False, capture=True):
  global bstack111llll1ll_opy_
  bstack11l1l11l1_opy_ = bstack111llll1ll_opy_(self, runner, quiet=quiet, capture=capture)
  if self.exception:
    if not hasattr(runner, bstack11ll1ll_opy_ (u"ࠬ࡫ࡸࡤࡧࡳࡸ࡮ࡵ࡮ࡠࡣࡵࡶࠬන")):
      runner.exception_arr = []
    if not hasattr(runner, bstack11ll1ll_opy_ (u"࠭ࡥࡹࡥࡢࡸࡷࡧࡣࡦࡤࡤࡧࡰࡥࡡࡳࡴࠪ඲")):
      runner.exc_traceback_arr = []
    runner.exception = self.exception
    runner.exc_traceback = self.exc_traceback
    runner.exception_arr.append(self.exception)
    runner.exc_traceback_arr.append(self.exc_traceback)
  return bstack11l1l11l1_opy_
def bstack11lll11ll_opy_(runner, hook_name, context, element, bstack111l1ll11_opy_, *args):
  try:
    if runner.hooks.get(hook_name):
      bstack1111l1lll_opy_.bstack11l11ll1_opy_(hook_name, element)
    bstack111l1ll11_opy_(runner, hook_name, context, *args)
    if runner.hooks.get(hook_name):
      bstack1111l1lll_opy_.bstack11l11l11_opy_(element)
      if hook_name not in [bstack11ll1ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࠫඳ"), bstack11ll1ll_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫප")] and args and hasattr(args[0], bstack11ll1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࡠ࡯ࡨࡷࡸࡧࡧࡦࠩඵ")):
        args[0].error_message = bstack11ll1ll_opy_ (u"ࠪࠫබ")
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡩࡣࡱࡨࡱ࡫ࠠࡩࡱࡲ࡯ࡸࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦ࠼ࠣࡿࢂ࠭භ").format(str(e)))
@measure(event_name=EVENTS.bstack11lll1l1ll_opy_, stage=STAGE.bstack11l11ll1ll_opy_, hook_type=bstack11ll1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡆࡲ࡬ࠣම"), bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1l111llll_opy_(runner, name, context, bstack111l1ll11_opy_, *args):
    if runner.hooks.get(bstack11ll1ll_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠥඹ")).__name__ != bstack11ll1ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡢ࡮࡯ࡣࡩ࡫ࡦࡢࡷ࡯ࡸࡤ࡮࡯ࡰ࡭ࠥය"):
      bstack11lll11ll_opy_(runner, name, context, runner, bstack111l1ll11_opy_, *args)
    try:
      threading.current_thread().bstackSessionDriver if bstack1llll111ll_opy_(bstack11ll1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧර")) else context.browser
      runner.driver_initialised = bstack11ll1ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨ඼")
    except Exception as e:
      logger.debug(bstack11ll1ll_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡨࡷ࡯ࡶࡦࡴࠣ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡸ࡫ࠠࡢࡶࡷࡶ࡮ࡨࡵࡵࡧ࠽ࠤࢀࢃࠧල").format(str(e)))
def bstack1l11l11l1_opy_(runner, name, context, bstack111l1ll11_opy_, *args):
    bstack11lll11ll_opy_(runner, name, context, context.feature, bstack111l1ll11_opy_, *args)
    try:
      if not bstack111l11l1ll_opy_:
        bstack1l11l1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1llll111ll_opy_(bstack11ll1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ඾")) else context.browser
        if is_driver_active(bstack1l11l1l11l_opy_):
          if runner.driver_initialised is None: runner.driver_initialised = bstack11ll1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤ࡬ࡥࡢࡶࡸࡶࡪࠨ඿")
          bstack1l11l111l1_opy_ = str(runner.feature.name)
          bstack1ll11l11l1_opy_(context, bstack1l11l111l1_opy_)
          bstack1l11l1l11l_opy_.execute_script(bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠣࠫව") + json.dumps(bstack1l11l111l1_opy_) + bstack11ll1ll_opy_ (u"ࠧࡾࡿࠪශ"))
    except Exception as e:
      logger.debug(bstack11ll1ll_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡱࡥࡲ࡫ࠠࡪࡰࠣࡦࡪ࡬࡯ࡳࡧࠣࡪࡪࡧࡴࡶࡴࡨ࠾ࠥࢁࡽࠨෂ").format(str(e)))
def bstack1l1111ll1l_opy_(runner, name, context, bstack111l1ll11_opy_, *args):
    if hasattr(context, bstack11ll1ll_opy_ (u"ࠩࡶࡧࡪࡴࡡࡳ࡫ࡲࠫස")):
        bstack1111l1lll_opy_.start_test(context)
    target = context.scenario if hasattr(context, bstack11ll1ll_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬහ")) else context.feature
    bstack11lll11ll_opy_(runner, name, context, target, bstack111l1ll11_opy_, *args)
@measure(event_name=EVENTS.bstack11lllll1l_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1l1l11111_opy_(runner, name, context, bstack111l1ll11_opy_, *args):
    if len(context.scenario.tags) == 0: bstack1111l1lll_opy_.start_test(context)
    bstack11lll11ll_opy_(runner, name, context, context.scenario, bstack111l1ll11_opy_, *args)
    threading.current_thread().a11y_stop = False
    bstack111lllllll_opy_.bstack11111l1l11_opy_(context, *args)
    try:
      bstack1l11l1l11l_opy_ = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪළ"), context.browser)
      if is_driver_active(bstack1l11l1l11l_opy_):
        bstack1ll1l111_opy_.bstack11l1lllll_opy_(bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫෆ"), {}))
        if runner.driver_initialised is None: runner.driver_initialised = bstack11ll1ll_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࡥࡳࡤࡧࡱࡥࡷ࡯࡯ࠣ෇")
        if (not bstack111l11l1ll_opy_):
          scenario_name = args[0].name
          feature_name = bstack1l11l111l1_opy_ = str(runner.feature.name)
          bstack1l11l111l1_opy_ = feature_name + bstack11ll1ll_opy_ (u"ࠧࠡ࠯ࠣࠫ෈") + scenario_name
          if runner.driver_initialised == bstack11ll1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡦࡩࡳࡧࡲࡪࡱࠥ෉"):
            bstack1ll11l11l1_opy_(context, bstack1l11l111l1_opy_)
            bstack1l11l1l11l_opy_.execute_script(bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨ࡮ࡢ࡯ࡨࠦ࠿්ࠦࠧ") + json.dumps(bstack1l11l111l1_opy_) + bstack11ll1ll_opy_ (u"ࠪࢁࢂ࠭෋"))
    except Exception as e:
      logger.debug(bstack11ll1ll_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣ࡭ࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡧࡱࡥࡷ࡯࡯࠻ࠢࡾࢁࠬ෌").format(str(e)))
@measure(event_name=EVENTS.bstack11lll1l1ll_opy_, stage=STAGE.bstack11l11ll1ll_opy_, hook_type=bstack11ll1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡘࡺࡥࡱࠤ෍"), bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1l1111lll1_opy_(runner, name, context, bstack111l1ll11_opy_, *args):
    bstack11lll11ll_opy_(runner, name, context, args[0], bstack111l1ll11_opy_, *args)
    try:
      bstack1l11l1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1llll111ll_opy_(bstack11ll1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ෎")) else context.browser
      if is_driver_active(bstack1l11l1l11l_opy_):
        if runner.driver_initialised is None: runner.driver_initialised = bstack11ll1ll_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫࡟ࡴࡶࡨࡴࠧා")
        bstack1111l1lll_opy_.bstack11l1l1ll_opy_(args[0])
        if runner.driver_initialised == bstack11ll1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨැ"):
          feature_name = bstack1l11l111l1_opy_ = str(runner.feature.name)
          bstack1l11l111l1_opy_ = feature_name + bstack11ll1ll_opy_ (u"ࠩࠣ࠱ࠥ࠭ෑ") + context.scenario.name
          bstack1l11l1l11l_opy_.execute_script(bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨි") + json.dumps(bstack1l11l111l1_opy_) + bstack11ll1ll_opy_ (u"ࠫࢂࢃࠧී"))
    except Exception as e:
      logger.debug(bstack11ll1ll_opy_ (u"ࠬࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠤ࡮ࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩු").format(str(e)))
@measure(event_name=EVENTS.bstack11lll1l1ll_opy_, stage=STAGE.bstack11l11ll1ll_opy_, hook_type=bstack11ll1ll_opy_ (u"ࠨࡡࡧࡶࡨࡶࡘࡺࡥࡱࠤ෕"), bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1lllll1l11_opy_(runner, name, context, bstack111l1ll11_opy_, *args):
  bstack1111l1lll_opy_.bstack11l1l111_opy_(args[0])
  try:
    step_status = args[0].status.name
    bstack1l11l1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack11ll1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ූ") in threading.current_thread().__dict__.keys() else context.browser
    if is_driver_active(bstack1l11l1l11l_opy_):
      if runner.driver_initialised is None:
        runner.driver_initialised  = bstack11ll1ll_opy_ (u"ࠨ࡫ࡱࡷࡹ࡫ࡰࠨ෗")
        feature_name = bstack1l11l111l1_opy_ = str(runner.feature.name)
        bstack1l11l111l1_opy_ = feature_name + bstack11ll1ll_opy_ (u"ࠩࠣ࠱ࠥ࠭ෘ") + context.scenario.name
        bstack1l11l1l11l_opy_.execute_script(bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢ࡯ࡣࡰࡩࠧࡀࠠࠨෙ") + json.dumps(bstack1l11l111l1_opy_) + bstack11ll1ll_opy_ (u"ࠫࢂࢃࠧේ"))
    if str(step_status).lower() == bstack11ll1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬෛ"):
      bstack1ll1111111_opy_ = bstack11ll1ll_opy_ (u"࠭ࠧො")
      bstack111lll1111_opy_ = bstack11ll1ll_opy_ (u"ࠧࠨෝ")
      bstack111l111ll_opy_ = bstack11ll1ll_opy_ (u"ࠨࠩෞ")
      try:
        import traceback
        bstack1ll1111111_opy_ = runner.exception.__class__.__name__
        bstack11l1111l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack111lll1111_opy_ = bstack11ll1ll_opy_ (u"ࠩࠣࠫෟ").join(bstack11l1111l_opy_)
        bstack111l111ll_opy_ = bstack11l1111l_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l1ll1lll_opy_.format(str(e)))
      bstack1ll1111111_opy_ += bstack111l111ll_opy_
      bstack1l11l1l1l1_opy_(context, json.dumps(str(args[0].name) + bstack11ll1ll_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ෠") + str(bstack111lll1111_opy_)),
                          bstack11ll1ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ෡"))
      if runner.driver_initialised == bstack11ll1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡴࡦࡲࠥ෢"):
        bstack1lll111ll1_opy_(getattr(context, bstack11ll1ll_opy_ (u"࠭ࡰࡢࡩࡨࠫ෣"), None), bstack11ll1ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢ෤"), bstack1ll1111111_opy_)
        bstack1l11l1l11l_opy_.execute_script(bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭෥") + json.dumps(str(args[0].name) + bstack11ll1ll_opy_ (u"ࠤࠣ࠱ࠥࡌࡡࡪ࡮ࡨࡨࠦࡢ࡮ࠣ෦") + str(bstack111lll1111_opy_)) + bstack11ll1ll_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣࡧࡵࡶࡴࡸࠢࡾࡿࠪ෧"))
      if runner.driver_initialised == bstack11ll1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡺࡥࡱࠤ෨"):
        bstack11l1l111ll_opy_(bstack1l11l1l11l_opy_, bstack11ll1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ෩"), bstack11ll1ll_opy_ (u"ࠨࡓࡤࡧࡱࡥࡷ࡯࡯ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥ෪") + str(bstack1ll1111111_opy_))
    else:
      bstack1l11l1l1l1_opy_(context, bstack11ll1ll_opy_ (u"ࠢࡑࡣࡶࡷࡪࡪࠡࠣ෫"), bstack11ll1ll_opy_ (u"ࠣ࡫ࡱࡪࡴࠨ෬"))
      if runner.driver_initialised == bstack11ll1ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡶࡸࡪࡶࠢ෭"):
        bstack1lll111ll1_opy_(getattr(context, bstack11ll1ll_opy_ (u"ࠪࡴࡦ࡭ࡥࠨ෮"), None), bstack11ll1ll_opy_ (u"ࠦࡵࡧࡳࡴࡧࡧࠦ෯"))
      bstack1l11l1l11l_opy_.execute_script(bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡨࡦࡺࡡࠣ࠼ࠪ෰") + json.dumps(str(args[0].name) + bstack11ll1ll_opy_ (u"ࠨࠠ࠮ࠢࡓࡥࡸࡹࡥࡥࠣࠥ෱")) + bstack11ll1ll_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡯࡮ࡧࡱࠥࢁࢂ࠭ෲ"))
      if runner.driver_initialised == bstack11ll1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨෳ"):
        bstack11l1l111ll_opy_(bstack1l11l1l11l_opy_, bstack11ll1ll_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤ෴"))
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦ࡭ࡢࡴ࡮ࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡹࡴࡢࡶࡸࡷࠥ࡯࡮ࠡࡣࡩࡸࡪࡸࠠࡴࡶࡨࡴ࠿ࠦࡻࡾࠩ෵").format(str(e)))
  bstack11lll11ll_opy_(runner, name, context, args[0], bstack111l1ll11_opy_, *args)
@measure(event_name=EVENTS.bstack11l1llll1l_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1l11ll1l1l_opy_(runner, name, context, bstack111l1ll11_opy_, *args):
  bstack1111l1lll_opy_.end_test(args[0])
  try:
    bstack11l11l1ll1_opy_ = args[0].status.name
    bstack1l11l1l11l_opy_ = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪ෶"), context.browser)
    bstack111lllllll_opy_.bstack1ll1l11l1l_opy_(bstack1l11l1l11l_opy_)
    if str(bstack11l11l1ll1_opy_).lower() == bstack11ll1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ෷"):
      bstack1ll1111111_opy_ = bstack11ll1ll_opy_ (u"࠭ࠧ෸")
      bstack111lll1111_opy_ = bstack11ll1ll_opy_ (u"ࠧࠨ෹")
      bstack111l111ll_opy_ = bstack11ll1ll_opy_ (u"ࠨࠩ෺")
      try:
        import traceback
        bstack1ll1111111_opy_ = runner.exception.__class__.__name__
        bstack11l1111l_opy_ = traceback.format_tb(runner.exc_traceback)
        bstack111lll1111_opy_ = bstack11ll1ll_opy_ (u"ࠩࠣࠫ෻").join(bstack11l1111l_opy_)
        bstack111l111ll_opy_ = bstack11l1111l_opy_[-1]
      except Exception as e:
        logger.debug(bstack1l1ll1lll_opy_.format(str(e)))
      bstack1ll1111111_opy_ += bstack111l111ll_opy_
      bstack1l11l1l1l1_opy_(context, json.dumps(str(args[0].name) + bstack11ll1ll_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤ෼") + str(bstack111lll1111_opy_)),
                          bstack11ll1ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ෽"))
      if runner.driver_initialised == bstack11ll1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢ෾") or runner.driver_initialised == bstack11ll1ll_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭෿"):
        bstack1lll111ll1_opy_(getattr(context, bstack11ll1ll_opy_ (u"ࠧࡱࡣࡪࡩࠬ฀"), None), bstack11ll1ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣก"), bstack1ll1111111_opy_)
        bstack1l11l1l11l_opy_.execute_script(bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡥࡣࡷࡥࠧࡀࠧข") + json.dumps(str(args[0].name) + bstack11ll1ll_opy_ (u"ࠥࠤ࠲ࠦࡆࡢ࡫࡯ࡩࡩࠧ࡜࡯ࠤฃ") + str(bstack111lll1111_opy_)) + bstack11ll1ll_opy_ (u"ࠫ࠱ࠦࠢ࡭ࡧࡹࡩࡱࠨ࠺ࠡࠤࡨࡶࡷࡵࡲࠣࡿࢀࠫค"))
      if runner.driver_initialised == bstack11ll1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵࠢฅ") or runner.driver_initialised == bstack11ll1ll_opy_ (u"࠭ࡩ࡯ࡵࡷࡩࡵ࠭ฆ"):
        bstack11l1l111ll_opy_(bstack1l11l1l11l_opy_, bstack11ll1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧง"), bstack11ll1ll_opy_ (u"ࠣࡕࡦࡩࡳࡧࡲࡪࡱࠣࡪࡦ࡯࡬ࡦࡦࠣࡻ࡮ࡺࡨ࠻ࠢ࡟ࡲࠧจ") + str(bstack1ll1111111_opy_))
    else:
      bstack1l11l1l1l1_opy_(context, bstack11ll1ll_opy_ (u"ࠤࡓࡥࡸࡹࡥࡥࠣࠥฉ"), bstack11ll1ll_opy_ (u"ࠥ࡭ࡳ࡬࡯ࠣช"))
      if runner.driver_initialised == bstack11ll1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨซ") or runner.driver_initialised == bstack11ll1ll_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬฌ"):
        bstack1lll111ll1_opy_(getattr(context, bstack11ll1ll_opy_ (u"࠭ࡰࡢࡩࡨࠫญ"), None), bstack11ll1ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢฎ"))
      bstack1l11l1l11l_opy_.execute_script(bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥ࠰ࠥࠨࡡࡳࡩࡸࡱࡪࡴࡴࡴࠤ࠽ࠤࢀࠨࡤࡢࡶࡤࠦ࠿࠭ฏ") + json.dumps(str(args[0].name) + bstack11ll1ll_opy_ (u"ࠤࠣ࠱ࠥࡖࡡࡴࡵࡨࡨࠦࠨฐ")) + bstack11ll1ll_opy_ (u"ࠪ࠰ࠥࠨ࡬ࡦࡸࡨࡰࠧࡀࠠࠣ࡫ࡱࡪࡴࠨࡽࡾࠩฑ"))
      if runner.driver_initialised == bstack11ll1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴࠨฒ") or runner.driver_initialised == bstack11ll1ll_opy_ (u"ࠬ࡯࡮ࡴࡶࡨࡴࠬณ"):
        bstack11l1l111ll_opy_(bstack1l11l1l11l_opy_, bstack11ll1ll_opy_ (u"ࠨࡰࡢࡵࡶࡩࡩࠨด"))
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡱࡦࡸ࡫ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢ࡬ࡲࠥࡧࡦࡵࡧࡵࠤ࡫࡫ࡡࡵࡷࡵࡩ࠿ࠦࡻࡾࠩต").format(str(e)))
  bstack11lll11ll_opy_(runner, name, context, context.scenario, bstack111l1ll11_opy_, *args)
  if len(context.scenario.tags) == 0: threading.current_thread().current_test_uuid = None
def bstack1l11llll1_opy_(runner, name, context, bstack111l1ll11_opy_, *args):
    target = context.scenario if hasattr(context, bstack11ll1ll_opy_ (u"ࠨࡵࡦࡩࡳࡧࡲࡪࡱࠪถ")) else context.feature
    bstack11lll11ll_opy_(runner, name, context, target, bstack111l1ll11_opy_, *args)
    threading.current_thread().current_test_uuid = None
def bstack1l1ll11lll_opy_(runner, name, context, bstack111l1ll11_opy_, *args):
    try:
      bstack1l11l1l11l_opy_ = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨท"), context.browser)
      bstack1ll1ll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠪࠫธ")
      if context.failed is True:
        bstack1llll11ll1_opy_ = []
        bstack11lll1ll1_opy_ = []
        bstack11l1l1l1l_opy_ = []
        try:
          import traceback
          for exc in runner.exception_arr:
            bstack1llll11ll1_opy_.append(exc.__class__.__name__)
          for exc_tb in runner.exc_traceback_arr:
            bstack11l1111l_opy_ = traceback.format_tb(exc_tb)
            bstack11l11ll111_opy_ = bstack11ll1ll_opy_ (u"ࠫࠥ࠭น").join(bstack11l1111l_opy_)
            bstack11lll1ll1_opy_.append(bstack11l11ll111_opy_)
            bstack11l1l1l1l_opy_.append(bstack11l1111l_opy_[-1])
        except Exception as e:
          logger.debug(bstack1l1ll1lll_opy_.format(str(e)))
        bstack1ll1111111_opy_ = bstack11ll1ll_opy_ (u"ࠬ࠭บ")
        for i in range(len(bstack1llll11ll1_opy_)):
          bstack1ll1111111_opy_ += bstack1llll11ll1_opy_[i] + bstack11l1l1l1l_opy_[i] + bstack11ll1ll_opy_ (u"࠭࡜࡯ࠩป")
        bstack1ll1ll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠧࠡࠩผ").join(bstack11lll1ll1_opy_)
        if runner.driver_initialised in [bstack11ll1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡨࡨࡥࡹࡻࡲࡦࠤฝ"), bstack11ll1ll_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࡡࡤࡰࡱࠨพ")]:
          bstack1l11l1l1l1_opy_(context, bstack1ll1ll1ll_opy_, bstack11ll1ll_opy_ (u"ࠥࡩࡷࡸ࡯ࡳࠤฟ"))
          bstack1lll111ll1_opy_(getattr(context, bstack11ll1ll_opy_ (u"ࠫࡵࡧࡧࡦࠩภ"), None), bstack11ll1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧม"), bstack1ll1111111_opy_)
          bstack1l11l1l11l_opy_.execute_script(bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡡ࡯ࡰࡲࡸࡦࡺࡥࠣ࠮ࠣࠦࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠢ࠻ࠢࡾࠦࡩࡧࡴࡢࠤ࠽ࠫย") + json.dumps(bstack1ll1ll1ll_opy_) + bstack11ll1ll_opy_ (u"ࠧ࠭ࠢࠥࡰࡪࡼࡥ࡭ࠤ࠽ࠤࠧ࡫ࡲࡳࡱࡵࠦࢂࢃࠧร"))
          bstack11l1l111ll_opy_(bstack1l11l1l11l_opy_, bstack11ll1ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣฤ"), bstack11ll1ll_opy_ (u"ࠤࡖࡳࡲ࡫ࠠࡴࡥࡨࡲࡦࡸࡩࡰࡵࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡡࡴࠢล") + str(bstack1ll1111111_opy_))
          bstack1l1lll1l1_opy_ = bstack1l11ll1lll_opy_(bstack1ll1ll1ll_opy_, runner.feature.name, logger)
          if (bstack1l1lll1l1_opy_ != None):
            bstack1l1l1111l_opy_.append(bstack1l1lll1l1_opy_)
      else:
        if runner.driver_initialised in [bstack11ll1ll_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨࠦฦ"), bstack11ll1ll_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࡣࡦࡲ࡬ࠣว")]:
          bstack1l11l1l1l1_opy_(context, bstack11ll1ll_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࡀࠠࠣศ") + str(runner.feature.name) + bstack11ll1ll_opy_ (u"ࠨࠠࡱࡣࡶࡷࡪࡪࠡࠣษ"), bstack11ll1ll_opy_ (u"ࠢࡪࡰࡩࡳࠧส"))
          bstack1lll111ll1_opy_(getattr(context, bstack11ll1ll_opy_ (u"ࠨࡲࡤ࡫ࡪ࠭ห"), None), bstack11ll1ll_opy_ (u"ࠤࡳࡥࡸࡹࡥࡥࠤฬ"))
          bstack1l11l1l11l_opy_.execute_script(bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨอ") + json.dumps(bstack11ll1ll_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩ࠿ࠦࠢฮ") + str(runner.feature.name) + bstack11ll1ll_opy_ (u"ࠧࠦࡰࡢࡵࡶࡩࡩࠧࠢฯ")) + bstack11ll1ll_opy_ (u"࠭ࠬࠡࠤ࡯ࡩࡻ࡫࡬ࠣ࠼ࠣࠦ࡮ࡴࡦࡰࠤࢀࢁࠬะ"))
          bstack11l1l111ll_opy_(bstack1l11l1l11l_opy_, bstack11ll1ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧั"))
          bstack1l1lll1l1_opy_ = bstack1l11ll1lll_opy_(bstack1ll1ll1ll_opy_, runner.feature.name, logger)
          if (bstack1l1lll1l1_opy_ != None):
            bstack1l1l1111l_opy_.append(bstack1l1lll1l1_opy_)
    except Exception as e:
      logger.debug(bstack11ll1ll_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡲࡧࡲ࡬ࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡬ࡥࡢࡶࡸࡶࡪࡀࠠࡼࡿࠪา").format(str(e)))
    bstack11lll11ll_opy_(runner, name, context, context.feature, bstack111l1ll11_opy_, *args)
@measure(event_name=EVENTS.bstack11lll1l1ll_opy_, stage=STAGE.bstack11l11ll1ll_opy_, hook_type=bstack11ll1ll_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࡂ࡮࡯ࠦำ"), bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1l11l1111_opy_(runner, name, context, bstack111l1ll11_opy_, *args):
    bstack11lll11ll_opy_(runner, name, context, runner, bstack111l1ll11_opy_, *args)
def bstack1l1lll11l1_opy_(self, name, context, *args):
  try:
    if bstack1l1ll11l11_opy_:
      platform_index = int(threading.current_thread()._name) % bstack11ll111ll_opy_
      bstack1ll11l1l1l_opy_ = CONFIG[bstack11ll1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ิ")][platform_index]
      os.environ[bstack11ll1ll_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬี")] = json.dumps(bstack1ll11l1l1l_opy_)
    global bstack111l1ll11_opy_
    if not hasattr(self, bstack11ll1ll_opy_ (u"ࠬࡪࡲࡪࡸࡨࡶࡤ࡯࡮ࡪࡶ࡬ࡥࡱ࡯ࡳࡦࡦࠪึ")):
      self.driver_initialised = None
    bstack1l1llll111_opy_ = {
        bstack11ll1ll_opy_ (u"࠭ࡢࡦࡨࡲࡶࡪࡥࡡ࡭࡮ࠪื"): bstack1l111llll_opy_,
        bstack11ll1ll_opy_ (u"ࠧࡣࡧࡩࡳࡷ࡫࡟ࡧࡧࡤࡸࡺࡸࡥࠨุ"): bstack1l11l11l1_opy_,
        bstack11ll1ll_opy_ (u"ࠨࡤࡨࡪࡴࡸࡥࡠࡶࡤ࡫ูࠬ"): bstack1l1111ll1l_opy_,
        bstack11ll1ll_opy_ (u"ࠩࡥࡩ࡫ࡵࡲࡦࡡࡶࡧࡪࡴࡡࡳ࡫ࡲฺࠫ"): bstack1l1l11111_opy_,
        bstack11ll1ll_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰࠨ฻"): bstack1l1111lll1_opy_,
        bstack11ll1ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡹ࡫ࡰࠨ฼"): bstack1lllll1l11_opy_,
        bstack11ll1ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭฽"): bstack1l11ll1l1l_opy_,
        bstack11ll1ll_opy_ (u"࠭ࡡࡧࡶࡨࡶࡤࡺࡡࡨࠩ฾"): bstack1l11llll1_opy_,
        bstack11ll1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡦࡦࡣࡷࡹࡷ࡫ࠧ฿"): bstack1l1ll11lll_opy_,
        bstack11ll1ll_opy_ (u"ࠨࡣࡩࡸࡪࡸ࡟ࡢ࡮࡯ࠫเ"): bstack1l11l1111_opy_
    }
    handler = bstack1l1llll111_opy_.get(name, bstack111l1ll11_opy_)
    try:
      handler(self, name, context, bstack111l1ll11_opy_, *args)
    except Exception as e:
      logger.debug(bstack11ll1ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨࠤ࡭ࡵ࡯࡬ࠢ࡫ࡥࡳࡪ࡬ࡦࡴࠣࡿࢂࡀࠠࡼࡿࠪแ").format(name, str(e)))
    if name in [bstack11ll1ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࡡࡩࡩࡦࡺࡵࡳࡧࠪโ"), bstack11ll1ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬใ"), bstack11ll1ll_opy_ (u"ࠬࡧࡦࡵࡧࡵࡣࡦࡲ࡬ࠨไ")]:
      try:
        bstack1l11l1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1llll111ll_opy_(bstack11ll1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬๅ")) else context.browser
        bstack1111111lll_opy_ = (
          (name == bstack11ll1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡡ࡭࡮ࠪๆ") and self.driver_initialised == bstack11ll1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡣ࡯ࡰࠧ็")) or
          (name == bstack11ll1ll_opy_ (u"ࠩࡤࡪࡹ࡫ࡲࡠࡨࡨࡥࡹࡻࡲࡦ่ࠩ") and self.driver_initialised == bstack11ll1ll_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࡢࡪࡪࡧࡴࡶࡴࡨ้ࠦ")) or
          (name == bstack11ll1ll_opy_ (u"ࠫࡦ࡬ࡴࡦࡴࡢࡷࡨ࡫࡮ࡢࡴ࡬ࡳ๊ࠬ") and self.driver_initialised in [bstack11ll1ll_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵ๋ࠢ"), bstack11ll1ll_opy_ (u"ࠨࡩ࡯ࡵࡷࡩࡵࠨ์")]) or
          (name == bstack11ll1ll_opy_ (u"ࠧࡢࡨࡷࡩࡷࡥࡳࡵࡧࡳࠫํ") and self.driver_initialised == bstack11ll1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࡠࡵࡷࡩࡵࠨ๎"))
        )
        if bstack1111111lll_opy_:
          self.driver_initialised = None
          if bstack1l11l1l11l_opy_ and hasattr(bstack1l11l1l11l_opy_, bstack11ll1ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩ࠭๏")):
            try:
              bstack1l11l1l11l_opy_.quit()
            except Exception as e:
              logger.debug(bstack11ll1ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢࡴࡹ࡮ࡺࡴࡪࡰࡪࠤࡩࡸࡩࡷࡧࡵࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫ࠠࡩࡱࡲ࡯࠿ࠦࡻࡾࠩ๐").format(str(e)))
      except Exception as e:
        logger.debug(bstack11ll1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡡࡧࡶࡨࡶࠥ࡮࡯ࡰ࡭ࠣࡧࡱ࡫ࡡ࡯ࡷࡳࠤ࡫ࡵࡲࠡࡽࢀ࠾ࠥࢁࡽࠨ๑").format(name, str(e)))
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠬࡉࡲࡪࡶ࡬ࡧࡦࡲࠠࡦࡴࡵࡳࡷࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦࠢࡵࡹࡳࠦࡨࡰࡱ࡮ࠤࢀࢃ࠺ࠡࡽࢀࠫ๒").format(name, str(e)))
    try:
      bstack111l1ll11_opy_(self, name, context, *args)
    except Exception as e2:
      logger.debug(bstack11ll1ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡨࡤࡰࡱࡨࡡࡤ࡭ࠣࡳࡷ࡯ࡧࡪࡰࡤࡰࠥࡨࡥࡩࡣࡹࡩࠥ࡮࡯ࡰ࡭ࠣࡿࢂࡀࠠࡼࡿࠪ๓").format(name, str(e2)))
def bstack111ll11l11_opy_(config, startdir):
  return bstack11ll1ll_opy_ (u"ࠢࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡽ࠳ࢁࠧ๔").format(bstack11ll1ll_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠢ๕"))
notset = Notset()
def bstack1l1llll11_opy_(self, name: str, default=notset, skip: bool = False):
  global bstack111lll11l1_opy_
  if str(name).lower() == bstack11ll1ll_opy_ (u"ࠩࡧࡶ࡮ࡼࡥࡳࠩ๖"):
    return bstack11ll1ll_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠤ๗")
  else:
    return bstack111lll11l1_opy_(self, name, default, skip)
def bstack11lllll1l1_opy_(item, when):
  global bstack1lll11111l_opy_
  try:
    bstack1lll11111l_opy_(item, when)
  except Exception as e:
    pass
def bstack11l11l1ll_opy_():
  return
def bstack11ll1111l1_opy_(type, name, status, reason, bstack111llll11l_opy_, bstack11ll11ll1_opy_):
  bstack1ll1l1ll11_opy_ = {
    bstack11ll1ll_opy_ (u"ࠫࡦࡩࡴࡪࡱࡱࠫ๘"): type,
    bstack11ll1ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ๙"): {}
  }
  if type == bstack11ll1ll_opy_ (u"࠭ࡡ࡯ࡰࡲࡸࡦࡺࡥࠨ๚"):
    bstack1ll1l1ll11_opy_[bstack11ll1ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ๛")][bstack11ll1ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧ๜")] = bstack111llll11l_opy_
    bstack1ll1l1ll11_opy_[bstack11ll1ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ๝")][bstack11ll1ll_opy_ (u"ࠪࡨࡦࡺࡡࠨ๞")] = json.dumps(str(bstack11ll11ll1_opy_))
  if type == bstack11ll1ll_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬ๟"):
    bstack1ll1l1ll11_opy_[bstack11ll1ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ๠")][bstack11ll1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ๡")] = name
  if type == bstack11ll1ll_opy_ (u"ࠧࡴࡧࡷࡗࡪࡹࡳࡪࡱࡱࡗࡹࡧࡴࡶࡵࠪ๢"):
    bstack1ll1l1ll11_opy_[bstack11ll1ll_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫ๣")][bstack11ll1ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ๤")] = status
    if status == bstack11ll1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ๥"):
      bstack1ll1l1ll11_opy_[bstack11ll1ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ๦")][bstack11ll1ll_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬ๧")] = json.dumps(str(reason))
  bstack11l1ll1lll_opy_ = bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫ๨").format(json.dumps(bstack1ll1l1ll11_opy_))
  return bstack11l1ll1lll_opy_
def bstack1l1lll111_opy_(driver_command, response):
    if driver_command == bstack11ll1ll_opy_ (u"ࠧࡴࡥࡵࡩࡪࡴࡳࡩࡱࡷࠫ๩"):
        bstack1ll1l111_opy_.bstack1ll11ll1ll_opy_({
            bstack11ll1ll_opy_ (u"ࠨ࡫ࡰࡥ࡬࡫ࠧ๪"): response[bstack11ll1ll_opy_ (u"ࠩࡹࡥࡱࡻࡥࠨ๫")],
            bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪ๬"): bstack1ll1l111_opy_.current_test_uuid()
        })
def bstack1l1111l1l1_opy_(item, call, rep):
  global bstack1l111l11ll_opy_
  global bstack11l1lll1l1_opy_
  global bstack111l11l1ll_opy_
  name = bstack11ll1ll_opy_ (u"ࠫࠬ๭")
  try:
    if rep.when == bstack11ll1ll_opy_ (u"ࠬࡩࡡ࡭࡮ࠪ๮"):
      bstack1111lll11l_opy_ = threading.current_thread().bstackSessionId
      try:
        if not bstack111l11l1ll_opy_:
          name = str(rep.nodeid)
          bstack11l1l1l11_opy_ = bstack11ll1111l1_opy_(bstack11ll1ll_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠧ๯"), name, bstack11ll1ll_opy_ (u"ࠧࠨ๰"), bstack11ll1ll_opy_ (u"ࠨࠩ๱"), bstack11ll1ll_opy_ (u"ࠩࠪ๲"), bstack11ll1ll_opy_ (u"ࠪࠫ๳"))
          threading.current_thread().bstack1l1l11l1l_opy_ = name
          for driver in bstack11l1lll1l1_opy_:
            if bstack1111lll11l_opy_ == driver.session_id:
              driver.execute_script(bstack11l1l1l11_opy_)
      except Exception as e:
        logger.debug(bstack11ll1ll_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ๴").format(str(e)))
      try:
        bstack1ll1l11l11_opy_(rep.outcome.lower())
        if rep.outcome.lower() != bstack11ll1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭๵"):
          status = bstack11ll1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭๶") if rep.outcome.lower() == bstack11ll1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ๷") else bstack11ll1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ๸")
          reason = bstack11ll1ll_opy_ (u"ࠩࠪ๹")
          if status == bstack11ll1ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ๺"):
            reason = rep.longrepr.reprcrash.message
            if (not threading.current_thread().bstackTestErrorMessages):
              threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(reason)
          level = bstack11ll1ll_opy_ (u"ࠫ࡮ࡴࡦࡰࠩ๻") if status == bstack11ll1ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ๼") else bstack11ll1ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ๽")
          data = name + bstack11ll1ll_opy_ (u"ࠧࠡࡲࡤࡷࡸ࡫ࡤࠢࠩ๾") if status == bstack11ll1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ๿") else name + bstack11ll1ll_opy_ (u"ࠩࠣࡪࡦ࡯࡬ࡦࡦࠤࠤࠬ຀") + reason
          bstack1l1l1l11l_opy_ = bstack11ll1111l1_opy_(bstack11ll1ll_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬກ"), bstack11ll1ll_opy_ (u"ࠫࠬຂ"), bstack11ll1ll_opy_ (u"ࠬ࠭຃"), bstack11ll1ll_opy_ (u"࠭ࠧຄ"), level, data)
          for driver in bstack11l1lll1l1_opy_:
            if bstack1111lll11l_opy_ == driver.session_id:
              driver.execute_script(bstack1l1l1l11l_opy_)
      except Exception as e:
        logger.debug(bstack11ll1ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱࠤࡨࡵ࡮ࡵࡧࡻࡸࠥ࡬࡯ࡳࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡳࡦࡵࡶ࡭ࡴࡴ࠺ࠡࡽࢀࠫ຅").format(str(e)))
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠨࡇࡵࡶࡴࡸࠠࡪࡰࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾࢁࠬຆ").format(str(e)))
  bstack1l111l11ll_opy_(item, call, rep)
def bstack11ll1ll1l_opy_(driver, bstack111l1111l1_opy_, test=None):
  global bstack11111l11l_opy_
  if test != None:
    bstack1ll1ll1l1l_opy_ = getattr(test, bstack11ll1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧງ"), None)
    bstack1l1l1ll11l_opy_ = getattr(test, bstack11ll1ll_opy_ (u"ࠪࡹࡺ࡯ࡤࠨຈ"), None)
    PercySDK.screenshot(driver, bstack111l1111l1_opy_, bstack1ll1ll1l1l_opy_=bstack1ll1ll1l1l_opy_, bstack1l1l1ll11l_opy_=bstack1l1l1ll11l_opy_, bstack111lll1ll_opy_=bstack11111l11l_opy_)
  else:
    PercySDK.screenshot(driver, bstack111l1111l1_opy_)
@measure(event_name=EVENTS.bstack1111ll1ll_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1l1llll1l_opy_(driver):
  if bstack111llllll1_opy_.bstack1ll1l1l1l1_opy_() is True or bstack111llllll1_opy_.capturing() is True:
    return
  bstack111llllll1_opy_.bstack11111ll11l_opy_()
  while not bstack111llllll1_opy_.bstack1ll1l1l1l1_opy_():
    bstack11llllll1_opy_ = bstack111llllll1_opy_.bstack11l11l1l1_opy_()
    bstack11ll1ll1l_opy_(driver, bstack11llllll1_opy_)
  bstack111llllll1_opy_.bstack1ll11ll11_opy_()
def bstack111l1lll1_opy_(sequence, driver_command, response = None, bstack1ll1111l11_opy_ = None, args = None):
    try:
      if sequence != bstack11ll1ll_opy_ (u"ࠫࡧ࡫ࡦࡰࡴࡨࠫຉ"):
        return
      if percy.bstack11l1111ll_opy_() == bstack11ll1ll_opy_ (u"ࠧ࡬ࡡ࡭ࡵࡨࠦຊ"):
        return
      bstack11llllll1_opy_ = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ຋"), None)
      for command in bstack111lllll11_opy_:
        if command == driver_command:
          with bstack11ll11lll_opy_:
            bstack1111111l1_opy_ = bstack11l1lll1l1_opy_.copy()
          for driver in bstack1111111l1_opy_:
            bstack1l1llll1l_opy_(driver)
      bstack11l111l1l1_opy_ = percy.bstack11ll1l111l_opy_()
      if driver_command in bstack1111lll1ll_opy_[bstack11l111l1l1_opy_]:
        bstack111llllll1_opy_.bstack111l11ll1_opy_(bstack11llllll1_opy_, driver_command)
    except Exception as e:
      pass
def bstack111l11lll1_opy_(framework_name):
  if bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟࡮ࡱࡧࡣࡨࡧ࡬࡭ࡧࡧࠫຌ")):
      return
  bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡠ࡯ࡲࡨࡤࡩࡡ࡭࡮ࡨࡨࠬຍ"), True)
  global bstack1lllll1ll1_opy_
  global bstack1l1ll111l1_opy_
  global bstack1l1l1111l1_opy_
  bstack1lllll1ll1_opy_ = framework_name
  logger.info(bstack11111ll1ll_opy_.format(bstack1lllll1ll1_opy_.split(bstack11ll1ll_opy_ (u"ࠩ࠰ࠫຎ"))[0]))
  bstack1ll1llll11_opy_()
  try:
    from selenium import webdriver
    from selenium.webdriver.common.service import Service
    from selenium.webdriver.remote.webdriver import WebDriver
    if bstack1l1ll11l11_opy_:
      Service.start = bstack1lllllll1l_opy_
      Service.stop = bstack11l11l1111_opy_
      webdriver.Remote.get = bstack11l1l11111_opy_
      WebDriver.quit = bstack1ll11lll11_opy_
      webdriver.Remote.__init__ = bstack1l1ll111ll_opy_
    if not bstack1l1ll11l11_opy_:
        webdriver.Remote.__init__ = bstack11l1ll1l11_opy_
    WebDriver.getAccessibilityResults = getAccessibilityResults
    WebDriver.get_accessibility_results = getAccessibilityResults
    WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
    WebDriver.get_accessibility_results_summary = getAccessibilityResultsSummary
    WebDriver.performScan = perform_scan
    WebDriver.perform_scan = perform_scan
    WebDriver.execute = bstack111l11ll11_opy_
    bstack1l1ll111l1_opy_ = True
  except Exception as e:
    pass
  try:
    if bstack1l1ll11l11_opy_:
      from QWeb.keywords import browser
      browser.close_browser = bstack111l1lll1l_opy_
  except Exception as e:
    pass
  bstack11llll11l1_opy_()
  if not bstack1l1ll111l1_opy_:
    bstack1lll11llll_opy_(bstack11ll1ll_opy_ (u"ࠥࡔࡦࡩ࡫ࡢࡩࡨࡷࠥࡴ࡯ࡵࠢ࡬ࡲࡸࡺࡡ࡭࡮ࡨࡨࠧຏ"), bstack11l11llll_opy_)
  if bstack1l1llllll1_opy_():
    try:
      from selenium.webdriver.remote.remote_connection import RemoteConnection
      if hasattr(RemoteConnection, bstack11ll1ll_opy_ (u"ࠫࡤ࡭ࡥࡵࡡࡳࡶࡴࡾࡹࡠࡷࡵࡰࠬຐ")) and callable(getattr(RemoteConnection, bstack11ll1ll_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ຑ"))):
        RemoteConnection._get_proxy_url = bstack1llll11lll_opy_
      else:
        from selenium.webdriver.remote.client_config import ClientConfig
        ClientConfig.get_proxy_url = bstack1llll11lll_opy_
    except Exception as e:
      logger.error(bstack1l1lll11ll_opy_.format(str(e)))
  if bstack1ll1ll1lll_opy_():
    bstack11l11ll1l1_opy_(CONFIG, logger)
  if (bstack11ll1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬຒ") in str(framework_name).lower()):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        if percy.bstack11l1111ll_opy_() == bstack11ll1ll_opy_ (u"ࠢࡵࡴࡸࡩࠧຓ"):
          bstack11ll11llll_opy_(bstack111l1lll1_opy_)
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        WebDriverCreator._get_ff_profile = bstack1llll1l111_opy_
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCache.close = bstack11l11111ll_opy_
      except Exception as e:
        logger.warn(bstack11l11l111l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        ApplicationCache.close = bstack111lllll1l_opy_
      except Exception as e:
        logger.debug(bstack1l111lll1_opy_ + str(e))
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack11l11l111l_opy_)
    Output.start_test = bstack1111l11l1_opy_
    Output.end_test = bstack11111lllll_opy_
    TestStatus.__init__ = bstack1l1l1lll1_opy_
    QueueItem.__init__ = bstack1ll1ll111_opy_
    pabot._create_items = bstack11ll1l1l11_opy_
    try:
      from pabot import __version__ as bstack1lll1111ll_opy_
      if version.parse(bstack1lll1111ll_opy_) >= version.parse(bstack11ll1ll_opy_ (u"ࠨ࠷࠱࠴࠳࠶ࠧດ")):
        pabot._run = bstack11l11lll1l_opy_
      elif version.parse(bstack1lll1111ll_opy_) >= version.parse(bstack11ll1ll_opy_ (u"ࠩ࠷࠲࠷࠴࠰ࠨຕ")):
        pabot._run = bstack1l11l11lll_opy_
      elif version.parse(bstack1lll1111ll_opy_) >= version.parse(bstack11ll1ll_opy_ (u"ࠪ࠶࠳࠷࠵࠯࠲ࠪຖ")):
        pabot._run = bstack1llll111l1_opy_
      elif version.parse(bstack1lll1111ll_opy_) >= version.parse(bstack11ll1ll_opy_ (u"ࠫ࠷࠴࠱࠴࠰࠳ࠫທ")):
        pabot._run = bstack11l1ll1ll_opy_
      else:
        pabot._run = bstack1111llllll_opy_
    except Exception as e:
      pabot._run = bstack1111llllll_opy_
    pabot._create_command_for_execution = bstack1l1ll111l_opy_
    pabot._report_results = bstack11l1111ll1_opy_
  if bstack11ll1ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬຘ") in str(framework_name).lower():
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack1l1l1ll1l1_opy_)
    Runner.run_hook = bstack1l1lll11l1_opy_
    Step.run = bstack11ll1l1l1l_opy_
  if bstack11ll1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ນ") in str(framework_name).lower():
    if not bstack1l1ll11l11_opy_:
      return
    try:
      from pytest_selenium import pytest_selenium
      from _pytest.config import Config
      pytest_selenium.pytest_report_header = bstack111ll11l11_opy_
      from pytest_selenium.drivers import browserstack
      browserstack.pytest_selenium_runtest_makereport = bstack11l11l1ll_opy_
      Config.getoption = bstack1l1llll11_opy_
    except Exception as e:
      pass
    try:
      from pytest_bdd import reporting
      reporting.runtest_makereport = bstack1l1111l1l1_opy_
    except Exception as e:
      pass
def bstack11ll1llll_opy_():
  global CONFIG
  if bstack11ll1ll_opy_ (u"ࠧࡱࡣࡵࡥࡱࡲࡥ࡭ࡵࡓࡩࡷࡖ࡬ࡢࡶࡩࡳࡷࡳࠧບ") in CONFIG and int(CONFIG[bstack11ll1ll_opy_ (u"ࠨࡲࡤࡶࡦࡲ࡬ࡦ࡮ࡶࡔࡪࡸࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨປ")]) > 1:
    logger.warn(bstack11ll11l11_opy_)
def bstack1ll1l11l1_opy_(arg, bstack1lll11l1l_opy_, bstack1l1l11ll1_opy_=None):
  global CONFIG
  global bstack11lll11111_opy_
  global bstack11llll1l1_opy_
  global bstack1l1ll11l11_opy_
  global bstack1llllll1l_opy_
  bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩຜ")
  if bstack1lll11l1l_opy_ and isinstance(bstack1lll11l1l_opy_, str):
    bstack1lll11l1l_opy_ = eval(bstack1lll11l1l_opy_)
  CONFIG = bstack1lll11l1l_opy_[bstack11ll1ll_opy_ (u"ࠪࡇࡔࡔࡆࡊࡉࠪຝ")]
  bstack11lll11111_opy_ = bstack1lll11l1l_opy_[bstack11ll1ll_opy_ (u"ࠫࡍ࡛ࡂࡠࡗࡕࡐࠬພ")]
  bstack11llll1l1_opy_ = bstack1lll11l1l_opy_[bstack11ll1ll_opy_ (u"ࠬࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧຟ")]
  bstack1l1ll11l11_opy_ = bstack1lll11l1l_opy_[bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡇࡕࡕࡑࡐࡅ࡙ࡏࡏࡏࠩຠ")]
  bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࠨມ"), bstack1l1ll11l11_opy_)
  os.environ[bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡇࡔࡄࡑࡊ࡝ࡏࡓࡍࠪຢ")] = bstack1l1l11ll11_opy_
  os.environ[bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡅࡒࡒࡋࡏࡇࠨຣ")] = json.dumps(CONFIG)
  os.environ[bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡋ࡙ࡇࡥࡕࡓࡎࠪ຤")] = bstack11lll11111_opy_
  os.environ[bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬລ")] = str(bstack11llll1l1_opy_)
  os.environ[bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕ࡟ࡔࡆࡕࡗࡣࡕࡒࡕࡈࡋࡑࠫ຦")] = str(True)
  if bstack1l1111111l_opy_(arg, [bstack11ll1ll_opy_ (u"࠭࠭࡯ࠩວ"), bstack11ll1ll_opy_ (u"ࠧ࠮࠯ࡱࡹࡲࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨຨ")]) != -1:
    os.environ[bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑ࡛ࡗࡉࡘ࡚࡟ࡑࡃࡕࡅࡑࡒࡅࡍࠩຩ")] = str(True)
  if len(sys.argv) <= 1:
    logger.critical(bstack1lll11lll1_opy_)
    return
  bstack1l1lll11l_opy_()
  global bstack1l111l111_opy_
  global bstack11111l11l_opy_
  global bstack11ll1lll1l_opy_
  global bstack1l1lll1l11_opy_
  global bstack11111ll111_opy_
  global bstack1l1l1111l1_opy_
  global bstack1llll11l11_opy_
  arg.append(bstack11ll1ll_opy_ (u"ࠤ࠰࡛ࠧສ"))
  arg.append(bstack11ll1ll_opy_ (u"ࠥ࡭࡬ࡴ࡯ࡳࡧ࠽ࡑࡴࡪࡵ࡭ࡧࠣࡥࡱࡸࡥࡢࡦࡼࠤ࡮ࡳࡰࡰࡴࡷࡩࡩࡀࡰࡺࡶࡨࡷࡹ࠴ࡐࡺࡶࡨࡷࡹ࡝ࡡࡳࡰ࡬ࡲ࡬ࠨຫ"))
  arg.append(bstack11ll1ll_opy_ (u"ࠦ࠲࡝ࠢຬ"))
  arg.append(bstack11ll1ll_opy_ (u"ࠧ࡯ࡧ࡯ࡱࡵࡩ࠿࡚ࡨࡦࠢ࡫ࡳࡴࡱࡩ࡮ࡲ࡯ࠦອ"))
  global bstack1l1ll1l111_opy_
  global bstack1l1ll1111l_opy_
  global bstack1l1llllll_opy_
  global bstack1ll1l11lll_opy_
  global bstack1111l11l11_opy_
  global bstack1111ll111_opy_
  global bstack11lll11l1_opy_
  global bstack1ll1lll1l1_opy_
  global bstack111llll1l1_opy_
  global bstack11111llll_opy_
  global bstack111lll11l1_opy_
  global bstack1lll11111l_opy_
  global bstack1l111l11ll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l1ll1l111_opy_ = webdriver.Remote.__init__
    bstack1l1ll1111l_opy_ = WebDriver.quit
    bstack1ll1lll1l1_opy_ = WebDriver.close
    bstack111llll1l1_opy_ = WebDriver.get
    bstack1l1llllll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  if bstack1111lllll_opy_(CONFIG) and bstack1111lll1l1_opy_():
    if bstack11llll1111_opy_() < version.parse(bstack111l1ll1l_opy_):
      logger.error(bstack1lll1111l1_opy_.format(bstack11llll1111_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11ll1ll_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧຮ")) and callable(getattr(RemoteConnection, bstack11ll1ll_opy_ (u"ࠧࡠࡩࡨࡸࡤࡶࡲࡰࡺࡼࡣࡺࡸ࡬ࠨຯ"))):
          bstack11111llll_opy_ = RemoteConnection._get_proxy_url
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          bstack11111llll_opy_ = ClientConfig.get_proxy_url
      except Exception as e:
        logger.error(bstack1l1lll11ll_opy_.format(str(e)))
  try:
    from _pytest.config import Config
    bstack111lll11l1_opy_ = Config.getoption
    from _pytest import runner
    bstack1lll11111l_opy_ = runner._update_current_test_var
  except Exception as e:
    logger.warn(e, bstack1111ll11_opy_)
  try:
    from pytest_bdd import reporting
    bstack1l111l11ll_opy_ = reporting.runtest_makereport
  except Exception as e:
    logger.debug(bstack11ll1ll_opy_ (u"ࠨࡒ࡯ࡩࡦࡹࡥࠡ࡫ࡱࡷࡹࡧ࡬࡭ࠢࡳࡽࡹ࡫ࡳࡵ࠯ࡥࡨࡩࠦࡴࡰࠢࡵࡹࡳࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡪࡹࡴࡴࠩະ"))
  bstack11ll1lll1l_opy_ = CONFIG.get(bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࡍࡱࡦࡥࡱࡕࡰࡵ࡫ࡲࡲࡸ࠭ັ"), {}).get(bstack11ll1ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬາ"))
  bstack1llll11l11_opy_ = True
  if cli.is_enabled(CONFIG):
    if cli.bstack1lllll1l1l_opy_():
      bstack1l1llll11l_opy_.invoke(Events.CONNECT, bstack1l1ll11ll_opy_())
    platform_index = int(os.environ.get(bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡏࡎࡅࡇ࡛ࠫຳ"), bstack11ll1ll_opy_ (u"ࠬ࠶ࠧິ")))
  else:
    bstack111l11lll1_opy_(bstack1ll11l1ll1_opy_)
  os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡛ࡓࡆࡔࡑࡅࡒࡋࠧີ")] = CONFIG[bstack11ll1ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩຶ")]
  os.environ[bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡅࡆࡉࡘ࡙࡟ࡌࡇ࡜ࠫື")] = CONFIG[bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽຸࠬ")]
  os.environ[bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡄ࡙࡙ࡕࡍࡂࡖࡌࡓࡓູ࠭")] = bstack1l1ll11l11_opy_.__str__()
  from _pytest.config import main as bstack11lll11lll_opy_
  bstack1llll11111_opy_ = []
  try:
    exit_code = bstack11lll11lll_opy_(arg)
    if cli.is_enabled(CONFIG):
      cli.bstack11l1lll11_opy_()
    if bstack11ll1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡣࡪࡸࡲࡰࡴࡢࡰ࡮ࡹࡴࠨ຺") in multiprocessing.current_process().__dict__.keys():
      for bstack11l1111l1l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1llll11111_opy_.append(bstack11l1111l1l_opy_)
    try:
      bstack1111l11l1l_opy_ = (bstack1llll11111_opy_, int(exit_code))
      bstack1l1l11ll1_opy_.append(bstack1111l11l1l_opy_)
    except:
      bstack1l1l11ll1_opy_.append((bstack1llll11111_opy_, exit_code))
  except Exception as e:
    logger.error(traceback.format_exc())
    bstack1llll11111_opy_.append({bstack11ll1ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪົ"): bstack11ll1ll_opy_ (u"࠭ࡐࡳࡱࡦࡩࡸࡹࠠࠨຼ") + os.environ.get(bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧຽ")), bstack11ll1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ຾"): traceback.format_exc(), bstack11ll1ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ຿"): int(os.environ.get(bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡎࡔࡄࡆ࡚ࠪເ")))})
    bstack1l1l11ll1_opy_.append((bstack1llll11111_opy_, 1))
def mod_behave_main(args, retries):
  try:
    from behave.configuration import Configuration
    from behave.__main__ import run_behave
    from browserstack_sdk.bstack_behave_runner import BehaveRunner
    config = Configuration(args)
    config.update_userdata({bstack11ll1ll_opy_ (u"ࠦࡷ࡫ࡴࡳ࡫ࡨࡷࠧແ"): str(retries)})
    return run_behave(config, runner_class=BehaveRunner)
  except Exception as e:
    bstack1l111l1ll_opy_ = e.__class__.__name__
    print(bstack11ll1ll_opy_ (u"ࠧࠫࡳ࠻ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡴࡸࡲࡳ࡯࡮ࡨࠢࡥࡩ࡭ࡧࡶࡦࠢࡷࡩࡸࡺࠠࠦࡵࠥໂ") % (bstack1l111l1ll_opy_, e))
    return 1
def bstack11lll1l11l_opy_(arg):
  global bstack1l11lll1l_opy_
  bstack111l11lll1_opy_(bstack11lll11l11_opy_)
  os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡏࡓࡠࡃࡓࡔࡤࡇࡕࡕࡑࡐࡅ࡙ࡋࠧໃ")] = str(bstack11llll1l1_opy_)
  retries = bstack1llllll11_opy_.bstack111l11ll_opy_(CONFIG)
  status_code = 0
  if bstack1llllll11_opy_.bstack1lll1llll_opy_(CONFIG):
    status_code = mod_behave_main(arg, retries)
  else:
    from behave.__main__ import main as bstack11lll1ll11_opy_
    status_code = bstack11lll1ll11_opy_(arg)
  if status_code != 0:
    bstack1l11lll1l_opy_ = status_code
def bstack111lll1l11_opy_():
  logger.info(bstack1111l1l1l1_opy_)
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument(bstack11ll1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ໄ"), help=bstack11ll1ll_opy_ (u"ࠨࡉࡨࡲࡪࡸࡡࡵࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠢࡦࡳࡳ࡬ࡩࡨࠩ໅"))
  parser.add_argument(bstack11ll1ll_opy_ (u"ࠩ࠰ࡹࠬໆ"), bstack11ll1ll_opy_ (u"ࠪ࠱࠲ࡻࡳࡦࡴࡱࡥࡲ࡫ࠧ໇"), help=bstack11ll1ll_opy_ (u"ࠫ࡞ࡵࡵࡳࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠡࡷࡶࡩࡷࡴࡡ࡮ࡧ່ࠪ"))
  parser.add_argument(bstack11ll1ll_opy_ (u"ࠬ࠳࡫ࠨ້"), bstack11ll1ll_opy_ (u"࠭࠭࠮࡭ࡨࡽ໊ࠬ"), help=bstack11ll1ll_opy_ (u"࡚ࠧࡱࡸࡶࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡦࡩࡣࡦࡵࡶࠤࡰ࡫ࡹࠨ໋"))
  parser.add_argument(bstack11ll1ll_opy_ (u"ࠨ࠯ࡩࠫ໌"), bstack11ll1ll_opy_ (u"ࠩ࠰࠱࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧໍ"), help=bstack11ll1ll_opy_ (u"ࠪ࡝ࡴࡻࡲࠡࡶࡨࡷࡹࠦࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ໎"))
  bstack1111lll11_opy_ = parser.parse_args()
  try:
    bstack11ll1lll1_opy_ = bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱࡫ࡪࡴࡥࡳ࡫ࡦ࠲ࡾࡳ࡬࠯ࡵࡤࡱࡵࡲࡥࠨ໏")
    if bstack1111lll11_opy_.framework and bstack1111lll11_opy_.framework not in (bstack11ll1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ໐"), bstack11ll1ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠹ࠧ໑")):
      bstack11ll1lll1_opy_ = bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡦࡳࡣࡰࡩࡼࡵࡲ࡬࠰ࡼࡱࡱ࠴ࡳࡢ࡯ࡳࡰࡪ࠭໒")
    bstack1l111l1ll1_opy_ = os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11ll1lll1_opy_)
    bstack1ll111ll1_opy_ = open(bstack1l111l1ll1_opy_, bstack11ll1ll_opy_ (u"ࠨࡴࠪ໓"))
    bstack111111l1ll_opy_ = bstack1ll111ll1_opy_.read()
    bstack1ll111ll1_opy_.close()
    if bstack1111lll11_opy_.username:
      bstack111111l1ll_opy_ = bstack111111l1ll_opy_.replace(bstack11ll1ll_opy_ (u"ࠩ࡜ࡓ࡚ࡘ࡟ࡖࡕࡈࡖࡓࡇࡍࡆࠩ໔"), bstack1111lll11_opy_.username)
    if bstack1111lll11_opy_.key:
      bstack111111l1ll_opy_ = bstack111111l1ll_opy_.replace(bstack11ll1ll_opy_ (u"ࠪ࡝ࡔ࡛ࡒࡠࡃࡆࡇࡊ࡙ࡓࡠࡍࡈ࡝ࠬ໕"), bstack1111lll11_opy_.key)
    if bstack1111lll11_opy_.framework:
      bstack111111l1ll_opy_ = bstack111111l1ll_opy_.replace(bstack11ll1ll_opy_ (u"ࠫ࡞ࡕࡕࡓࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ໖"), bstack1111lll11_opy_.framework)
    file_name = bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨ໗")
    file_path = os.path.abspath(file_name)
    bstack1l1l11ll1l_opy_ = open(file_path, bstack11ll1ll_opy_ (u"࠭ࡷࠨ໘"))
    bstack1l1l11ll1l_opy_.write(bstack111111l1ll_opy_)
    bstack1l1l11ll1l_opy_.close()
    logger.info(bstack11l111lll1_opy_)
    try:
      os.environ[bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡆࡓࡃࡐࡉ࡜ࡕࡒࡌࠩ໙")] = bstack1111lll11_opy_.framework if bstack1111lll11_opy_.framework != None else bstack11ll1ll_opy_ (u"ࠣࠤ໚")
      config = yaml.safe_load(bstack111111l1ll_opy_)
      config[bstack11ll1ll_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ໛")] = bstack11ll1ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠰ࡷࡪࡺࡵࡱࠩໜ")
      bstack11ll1l1ll1_opy_(bstack11lll1111l_opy_, config)
    except Exception as e:
      logger.debug(bstack11llllllll_opy_.format(str(e)))
  except Exception as e:
    logger.error(bstack111111l1l1_opy_.format(str(e)))
def bstack11ll1l1ll1_opy_(bstack11l1l1ll11_opy_, config, bstack1lll11ll1l_opy_={}):
  global bstack1l1ll11l11_opy_
  global bstack11l1ll11ll_opy_
  global bstack1llllll1l_opy_
  if not config:
    return
  bstack1111lll1l_opy_ = bstack1lll1llll1_opy_ if not bstack1l1ll11l11_opy_ else (
    bstack1l111ll1l1_opy_ if bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰࠨໝ") in config else (
        bstack11111l1111_opy_ if config.get(bstack11ll1ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩໞ")) else bstack11111llll1_opy_
    )
)
  bstack111llll11_opy_ = False
  bstack11l111l111_opy_ = False
  if bstack1l1ll11l11_opy_ is True:
      if bstack11ll1ll_opy_ (u"࠭ࡡࡱࡲࠪໟ") in config:
          bstack111llll11_opy_ = True
      else:
          bstack11l111l111_opy_ = True
  bstack1ll11ll1l1_opy_ = bstack1111llll11_opy_.bstack111lll11l_opy_(config, bstack11l1ll11ll_opy_)
  bstack111111ll1_opy_ = bstack111l11111l_opy_()
  data = {
    bstack11ll1ll_opy_ (u"ࠧࡶࡵࡨࡶࡓࡧ࡭ࡦࠩ໠"): config[bstack11ll1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ໡")],
    bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ໢"): config[bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭໣")],
    bstack11ll1ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨ໤"): bstack11l1l1ll11_opy_,
    bstack11ll1ll_opy_ (u"ࠬࡪࡥࡵࡧࡦࡸࡪࡪࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ໥"): os.environ.get(bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡌࡒࡂࡏࡈ࡛ࡔࡘࡋࠨ໦"), bstack11l1ll11ll_opy_),
    bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡨࡢࡵ࡫ࡩࡩࡥࡩࡥࠩ໧"): bstack1l1ll1ll1_opy_,
    bstack11ll1ll_opy_ (u"ࠨࡱࡳࡸ࡮ࡳࡡ࡭ࡡ࡫ࡹࡧࡥࡵࡳ࡮ࠪ໨"): bstack1l111111l1_opy_(),
    bstack11ll1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ໩"): {
      bstack11ll1ll_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ໪"): str(config[bstack11ll1ll_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ໫")]) if bstack11ll1ll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ໬") in config else bstack11ll1ll_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢ໭"),
      bstack11ll1ll_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࡘࡨࡶࡸ࡯࡯࡯ࠩ໮"): sys.version,
      bstack11ll1ll_opy_ (u"ࠨࡴࡨࡪࡪࡸࡲࡦࡴࠪ໯"): bstack1l11111lll_opy_(os.environ.get(bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡈࡕࡅࡒࡋࡗࡐࡔࡎࠫ໰"), bstack11l1ll11ll_opy_)),
      bstack11ll1ll_opy_ (u"ࠪࡰࡦࡴࡧࡶࡣࡪࡩࠬ໱"): bstack11ll1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ໲"),
      bstack11ll1ll_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹ࠭໳"): bstack1111lll1l_opy_,
      bstack11ll1ll_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ໴"): bstack1ll11ll1l1_opy_,
      bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸ࡭ࡻࡢࡠࡷࡸ࡭ࡩ࠭໵"): os.environ[bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭໶")],
      bstack11ll1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ໷"): os.environ.get(bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬ໸"), bstack11l1ll11ll_opy_),
      bstack11ll1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ໹"): bstack1ll111ll1l_opy_(os.environ.get(bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡋࡘࡁࡎࡇ࡚ࡓࡗࡑࠧ໺"), bstack11l1ll11ll_opy_)),
      bstack11ll1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ໻"): bstack111111ll1_opy_.get(bstack11ll1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ໼")),
      bstack11ll1ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ໽"): bstack111111ll1_opy_.get(bstack11ll1ll_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ໾")),
      bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭໿"): config[bstack11ll1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧༀ")] if config[bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ༁")] else bstack11ll1ll_opy_ (u"ࠨࡵ࡯࡭ࡱࡳࡼࡴࠢ༂"),
      bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩ༃"): str(config[bstack11ll1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ༄")]) if bstack11ll1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ༅") in config else bstack11ll1ll_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࠦ༆"),
      bstack11ll1ll_opy_ (u"ࠫࡴࡹࠧ༇"): sys.platform,
      bstack11ll1ll_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧ༈"): socket.gethostname(),
      bstack11ll1ll_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨ༉"): bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ༊"))
    }
  }
  if not bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯ࡐ࡯࡬࡭ࡕ࡬࡫ࡳࡧ࡬ࠨ་")) is None:
    data[bstack11ll1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ༌")][bstack11ll1ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡒ࡫ࡴࡢࡦࡤࡸࡦ࠭།")] = {
      bstack11ll1ll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫ༎"): bstack11ll1ll_opy_ (u"ࠬࡻࡳࡦࡴࡢ࡯࡮ࡲ࡬ࡦࡦࠪ༏"),
      bstack11ll1ll_opy_ (u"࠭ࡳࡪࡩࡱࡥࡱ࠭༐"): bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮ࡏ࡮ࡲ࡬ࡔ࡫ࡪࡲࡦࡲࠧ༑")),
      bstack11ll1ll_opy_ (u"ࠨࡵ࡬࡫ࡳࡧ࡬ࡏࡷࡰࡦࡪࡸࠧ༒"): bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠩࡶࡨࡰࡑࡩ࡭࡮ࡑࡳࠬ༓"))
    }
  if bstack11l1l1ll11_opy_ == bstack111ll1l11_opy_:
    data[bstack11ll1ll_opy_ (u"ࠪࡩࡻ࡫࡮ࡵࡡࡳࡶࡴࡶࡥࡳࡶ࡬ࡩࡸ࠭༔")][bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࡆࡳࡳ࡬ࡩࡨࠩ༕")] = bstack11l11ll11l_opy_(config)
    data[bstack11ll1ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ༖")][bstack11ll1ll_opy_ (u"࠭ࡩࡴࡒࡨࡶࡨࡿࡁࡶࡶࡲࡉࡳࡧࡢ࡭ࡧࡧࠫ༗")] = percy.bstack1l11ll1111_opy_
    data[bstack11ll1ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡰࡳࡱࡳࡩࡷࡺࡩࡦࡵ༘ࠪ")][bstack11ll1ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࡂࡶ࡫࡯ࡨࡎࡪ༙ࠧ")] = percy.percy_build_id
  if not bstack1llllll11_opy_.bstack111ll1lll_opy_(CONFIG):
    data[bstack11ll1ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡲࡵࡳࡵ࡫ࡲࡵ࡫ࡨࡷࠬ༚")][bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠧ༛")] = bstack1llllll11_opy_.bstack111ll1lll_opy_(CONFIG)
  bstack1lll1l111_opy_ = bstack111lll11_opy_.bstack1lll11ll1_opy_(CONFIG, logger)
  bstack1111111l_opy_ = bstack1llllll11_opy_.bstack1lll11ll1_opy_(config=CONFIG)
  if bstack1lll1l111_opy_ is not None and bstack1111111l_opy_ is not None and bstack1111111l_opy_.bstack1lll1l11l_opy_():
    data[bstack11ll1ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡴࡷࡵࡰࡦࡴࡷ࡭ࡪࡹࠧ༜")][bstack1111111l_opy_.bstack11l1ll1l1_opy_()] = bstack1lll1l111_opy_.bstack11111l11ll_opy_()
  update(data[bstack11ll1ll_opy_ (u"ࠬ࡫ࡶࡦࡰࡷࡣࡵࡸ࡯ࡱࡧࡵࡸ࡮࡫ࡳࠨ༝")], bstack1lll11ll1l_opy_)
  try:
    response = bstack11ll11ll1l_opy_(bstack11ll1ll_opy_ (u"࠭ࡐࡐࡕࡗࠫ༞"), bstack11l1l1l1l1_opy_(bstack1l11ll1ll1_opy_), data, {
      bstack11ll1ll_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ༟"): (config[bstack11ll1ll_opy_ (u"ࠨࡷࡶࡩࡷࡔࡡ࡮ࡧࠪ༠")], config[bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴࡍࡨࡽࠬ༡")])
    })
    if response:
      logger.debug(bstack1111ll11l_opy_.format(bstack11l1l1ll11_opy_, str(response.json())))
  except Exception as e:
    logger.debug(bstack1l1l1ll1l_opy_.format(str(e)))
def bstack1l11111lll_opy_(framework):
  return bstack11ll1ll_opy_ (u"ࠥࡿࢂ࠳ࡰࡺࡶ࡫ࡳࡳࡧࡧࡦࡰࡷ࠳ࢀࢃࠢ༢").format(str(framework), __version__) if framework else bstack11ll1ll_opy_ (u"ࠦࡵࡿࡴࡩࡱࡱࡥ࡬࡫࡮ࡵ࠱ࡾࢁࠧ༣").format(
    __version__)
def bstack1l1lll11l_opy_():
  global CONFIG
  global bstack11l111l1l_opy_
  if bool(CONFIG):
    return
  try:
    bstack1llllll111_opy_()
    logger.debug(bstack1l11lll1ll_opy_.format(str(CONFIG)))
    bstack11l111l1l_opy_ = bstack11111l1ll1_opy_.configure_logger(CONFIG, bstack11l111l1l_opy_)
    bstack1ll1llll11_opy_()
  except Exception as e:
    logger.error(bstack11ll1ll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࠤ༤") + str(e))
    sys.exit(1)
  sys.excepthook = bstack1l111l1l1l_opy_
  atexit.register(bstack1lll1l1111_opy_)
  signal.signal(signal.SIGINT, bstack1l1lllll1l_opy_)
  signal.signal(signal.SIGTERM, bstack1l1lllll1l_opy_)
def bstack1l111l1l1l_opy_(exctype, value, traceback):
  global bstack11l1lll1l1_opy_
  try:
    for driver in bstack11l1lll1l1_opy_:
      bstack11l1l111ll_opy_(driver, bstack11ll1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭༥"), bstack11ll1ll_opy_ (u"ࠢࡔࡧࡶࡷ࡮ࡵ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤࠡࡹ࡬ࡸ࡭ࡀࠠ࡝ࡰࠥ༦") + str(value))
  except Exception:
    pass
  logger.info(bstack111ll1111_opy_)
  bstack1l11l111l_opy_(value, True)
  sys.__excepthook__(exctype, value, traceback)
  sys.exit(1)
def bstack1l11l111l_opy_(message=bstack11ll1ll_opy_ (u"ࠨࠩ༧"), bstack1111llll1_opy_ = False):
  global CONFIG
  bstack1ll11llll_opy_ = bstack11ll1ll_opy_ (u"ࠩࡪࡰࡴࡨࡡ࡭ࡇࡻࡧࡪࡶࡴࡪࡱࡱࠫ༨") if bstack1111llll1_opy_ else bstack11ll1ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ༩")
  try:
    if message:
      bstack1lll11ll1l_opy_ = {
        bstack1ll11llll_opy_ : str(message)
      }
      bstack11ll1l1ll1_opy_(bstack111ll1l11_opy_, CONFIG, bstack1lll11ll1l_opy_)
    else:
      bstack11ll1l1ll1_opy_(bstack111ll1l11_opy_, CONFIG)
  except Exception as e:
    logger.debug(bstack11ll1lllll_opy_.format(str(e)))
def bstack1111lllll1_opy_(bstack1lll11l111_opy_, size):
  bstack1l11ll11l1_opy_ = []
  while len(bstack1lll11l111_opy_) > size:
    bstack11l1l1ll1_opy_ = bstack1lll11l111_opy_[:size]
    bstack1l11ll11l1_opy_.append(bstack11l1l1ll1_opy_)
    bstack1lll11l111_opy_ = bstack1lll11l111_opy_[size:]
  bstack1l11ll11l1_opy_.append(bstack1lll11l111_opy_)
  return bstack1l11ll11l1_opy_
def bstack11llll1ll1_opy_(args):
  if bstack11ll1ll_opy_ (u"ࠫ࠲ࡳࠧ༪") in args and bstack11ll1ll_opy_ (u"ࠬࡶࡤࡣࠩ༫") in args:
    return True
  return False
@measure(event_name=EVENTS.bstack11l1lll111_opy_, stage=STAGE.bstack1ll111111_opy_)
def run_on_browserstack(bstack1lll11l11l_opy_=None, bstack1l1l11ll1_opy_=None, bstack111ll1ll1l_opy_=False):
  global CONFIG
  global bstack11lll11111_opy_
  global bstack11llll1l1_opy_
  global bstack11l1ll11ll_opy_
  global bstack1llllll1l_opy_
  bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"࠭ࠧ༬")
  bstack1l1l111ll1_opy_(bstack1l1l111l1_opy_, logger)
  if bstack1lll11l11l_opy_ and isinstance(bstack1lll11l11l_opy_, str):
    bstack1lll11l11l_opy_ = eval(bstack1lll11l11l_opy_)
  if bstack1lll11l11l_opy_:
    CONFIG = bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧ༭")]
    bstack11lll11111_opy_ = bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩ༮")]
    bstack11llll1l1_opy_ = bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ༯")]
    bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"ࠪࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬ༰"), bstack11llll1l1_opy_)
    bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ༱")
  bstack1llllll1l_opy_.set_property(bstack11ll1ll_opy_ (u"ࠬࡹࡤ࡬ࡔࡸࡲࡎࡪࠧ༲"), uuid4().__str__())
  logger.info(bstack11ll1ll_opy_ (u"࠭ࡓࡅࡍࠣࡶࡺࡴࠠࡴࡶࡤࡶࡹ࡫ࡤࠡࡹ࡬ࡸ࡭ࠦࡩࡥ࠼ࠣࠫ༳") + bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮ࡖࡺࡴࡉࡥࠩ༴")));
  logger.debug(bstack11ll1ll_opy_ (u"ࠨࡵࡧ࡯ࡗࡻ࡮ࡊࡦࡀ༵ࠫ") + bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"ࠩࡶࡨࡰࡘࡵ࡯ࡋࡧࠫ༶")))
  if not bstack111ll1ll1l_opy_:
    if len(sys.argv) <= 1:
      logger.critical(bstack1lll11lll1_opy_)
      return
    if sys.argv[1] == bstack11ll1ll_opy_ (u"ࠪ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ༷࠭") or sys.argv[1] == bstack11ll1ll_opy_ (u"ࠫ࠲ࡼࠧ༸"):
      logger.info(bstack11ll1ll_opy_ (u"ࠬࡈࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡕࡿࡴࡩࡱࡱࠤࡘࡊࡋࠡࡸࡾࢁ༹ࠬ").format(__version__))
      return
    if sys.argv[1] == bstack11ll1ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬ༺"):
      bstack111lll1l11_opy_()
      return
  args = sys.argv
  bstack1l1lll11l_opy_()
  global bstack1l111l111_opy_
  global bstack11ll111ll_opy_
  global bstack1llll11l11_opy_
  global bstack111l111l1_opy_
  global bstack11111l11l_opy_
  global bstack11ll1lll1l_opy_
  global bstack1l1lll1l11_opy_
  global bstack1111ll1l1_opy_
  global bstack11111ll111_opy_
  global bstack1l1l1111l1_opy_
  global bstack11l1l1ll1l_opy_
  bstack11ll111ll_opy_ = len(CONFIG.get(bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ༻"), []))
  if not bstack1l1l11ll11_opy_:
    if args[1] == bstack11ll1ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ༼") or args[1] == bstack11ll1ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯࠵ࠪ༽"):
      bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ༾")
      args = args[2:]
    elif args[1] == bstack11ll1ll_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ༿"):
      bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫཀ")
      args = args[2:]
    elif args[1] == bstack11ll1ll_opy_ (u"࠭ࡰࡢࡤࡲࡸࠬཁ"):
      bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠧࡱࡣࡥࡳࡹ࠭ག")
      args = args[2:]
    elif args[1] == bstack11ll1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ࠩགྷ"):
      bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ࠪང")
      args = args[2:]
    elif args[1] == bstack11ll1ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪཅ"):
      bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫཆ")
      args = args[2:]
    elif args[1] == bstack11ll1ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬཇ"):
      bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭཈")
      args = args[2:]
    else:
      if not bstack11ll1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪཉ") in CONFIG or str(CONFIG[bstack11ll1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫཊ")]).lower() in [bstack11ll1ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩཋ"), bstack11ll1ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰ࠶ࠫཌ")]:
        bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫཌྷ")
        args = args[1:]
      elif str(CONFIG[bstack11ll1ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨཎ")]).lower() == bstack11ll1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬཏ"):
        bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭ཐ")
        args = args[1:]
      elif str(CONFIG[bstack11ll1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫད")]).lower() == bstack11ll1ll_opy_ (u"ࠩࡳࡥࡧࡵࡴࠨདྷ"):
        bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠪࡴࡦࡨ࡯ࡵࠩན")
        args = args[1:]
      elif str(CONFIG[bstack11ll1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧཔ")]).lower() == bstack11ll1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཕ"):
        bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭བ")
        args = args[1:]
      elif str(CONFIG[bstack11ll1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪབྷ")]).lower() == bstack11ll1ll_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨམ"):
        bstack1l1l11ll11_opy_ = bstack11ll1ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩཙ")
        args = args[1:]
      else:
        os.environ[bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬཚ")] = bstack1l1l11ll11_opy_
        bstack1ll1ll11ll_opy_(bstack1llll1ll11_opy_)
  os.environ[bstack11ll1ll_opy_ (u"ࠫࡋࡘࡁࡎࡇ࡚ࡓࡗࡑ࡟ࡖࡕࡈࡈࠬཛ")] = bstack1l1l11ll11_opy_
  bstack11l1ll11ll_opy_ = bstack1l1l11ll11_opy_
  if cli.is_enabled(CONFIG):
    try:
      bstack1l1lllll11_opy_ = bstack11l11l1l11_opy_[bstack11ll1ll_opy_ (u"ࠬࡖ࡙ࡕࡇࡖࡘ࠲ࡈࡄࡅࠩཛྷ")] if bstack1l1l11ll11_opy_ == bstack11ll1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ཝ") and bstack1llllll1l1_opy_() else bstack1l1l11ll11_opy_
      bstack1l1llll11l_opy_.invoke(Events.bstack111l1111ll_opy_, bstack11l1l1l11l_opy_(
        sdk_version=__version__,
        path_config=bstack11llll1lll_opy_(),
        path_project=os.getcwd(),
        test_framework=bstack1l1lllll11_opy_,
        frameworks=[bstack1l1lllll11_opy_],
        framework_versions={
          bstack1l1lllll11_opy_: bstack1ll111ll1l_opy_(bstack11ll1ll_opy_ (u"ࠧࡓࡱࡥࡳࡹ࠭ཞ") if bstack1l1l11ll11_opy_ in [bstack11ll1ll_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧཟ"), bstack11ll1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨའ"), bstack11ll1ll_opy_ (u"ࠪࡶࡴࡨ࡯ࡵ࠯࡬ࡲࡹ࡫ࡲ࡯ࡣ࡯ࠫཡ")] else bstack1l1l11ll11_opy_)
        },
        bs_config=CONFIG
      ))
      if cli.config.get(bstack11ll1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨར"), None):
        CONFIG[bstack11ll1ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢལ")] = cli.config.get(bstack11ll1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣཤ"), None)
    except Exception as e:
      bstack1l1llll11l_opy_.invoke(Events.bstack1ll11l1l1_opy_, e.__traceback__, 1)
    if bstack11llll1l1_opy_:
      CONFIG[bstack11ll1ll_opy_ (u"ࠢࡢࡲࡳࠦཥ")] = cli.config[bstack11ll1ll_opy_ (u"ࠣࡣࡳࡴࠧས")]
      logger.info(bstack1l11l1l11_opy_.format(CONFIG[bstack11ll1ll_opy_ (u"ࠩࡤࡴࡵ࠭ཧ")]))
  else:
    bstack1l1llll11l_opy_.clear()
  global bstack1ll1l1l111_opy_
  global bstack11lll111l1_opy_
  if bstack1lll11l11l_opy_:
    try:
      bstack111111ll11_opy_ = datetime.datetime.now()
      os.environ[bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡉࡖࡆࡓࡅࡘࡑࡕࡏࠬཨ")] = bstack1l1l11ll11_opy_
      bstack11ll1l1ll1_opy_(bstack1l1l11l11_opy_, CONFIG)
      cli.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼ࡶࡨࡰࡥࡴࡦࡵࡷࡣࡦࡺࡴࡦ࡯ࡳࡸࡪࡪࠢཀྵ"), datetime.datetime.now() - bstack111111ll11_opy_)
    except Exception as e:
      logger.debug(bstack1ll1l1l1ll_opy_.format(str(e)))
  global bstack1l1ll1l111_opy_
  global bstack1l1ll1111l_opy_
  global bstack1ll111lll_opy_
  global bstack11ll11ll11_opy_
  global bstack111l111lll_opy_
  global bstack1l11l11111_opy_
  global bstack1ll1l11lll_opy_
  global bstack1111l11l11_opy_
  global bstack1ll1l1l1l_opy_
  global bstack1111ll111_opy_
  global bstack11lll11l1_opy_
  global bstack1ll1lll1l1_opy_
  global bstack111l1ll11_opy_
  global bstack111llll1ll_opy_
  global bstack111llll1l1_opy_
  global bstack11111llll_opy_
  global bstack111lll11l1_opy_
  global bstack1lll11111l_opy_
  global bstack111ll111ll_opy_
  global bstack1l111l11ll_opy_
  global bstack1l1llllll_opy_
  try:
    from selenium import webdriver
    from selenium.webdriver.remote.webdriver import WebDriver
    bstack1l1ll1l111_opy_ = webdriver.Remote.__init__
    bstack1l1ll1111l_opy_ = WebDriver.quit
    bstack1ll1lll1l1_opy_ = WebDriver.close
    bstack111llll1l1_opy_ = WebDriver.get
    bstack1l1llllll_opy_ = WebDriver.execute
  except Exception as e:
    pass
  try:
    import Browser
    from subprocess import Popen
    bstack1ll1l1l111_opy_ = Popen.__init__
  except Exception as e:
    pass
  try:
    from bstack_utils.helper import bstack1lll11l1ll_opy_
    bstack11lll111l1_opy_ = bstack1lll11l1ll_opy_()
  except Exception as e:
    pass
  try:
    global bstack1l1ll1ll1l_opy_
    from QWeb.keywords import browser
    bstack1l1ll1ll1l_opy_ = browser.close_browser
  except Exception as e:
    pass
  if bstack1111lllll_opy_(CONFIG) and bstack1111lll1l1_opy_():
    if bstack11llll1111_opy_() < version.parse(bstack111l1ll1l_opy_):
      logger.error(bstack1lll1111l1_opy_.format(bstack11llll1111_opy_()))
    else:
      try:
        from selenium.webdriver.remote.remote_connection import RemoteConnection
        if hasattr(RemoteConnection, bstack11ll1ll_opy_ (u"ࠬࡥࡧࡦࡶࡢࡴࡷࡵࡸࡺࡡࡸࡶࡱ࠭ཪ")) and callable(getattr(RemoteConnection, bstack11ll1ll_opy_ (u"࠭࡟ࡨࡧࡷࡣࡵࡸ࡯ࡹࡻࡢࡹࡷࡲࠧཫ"))):
          RemoteConnection._get_proxy_url = bstack1llll11lll_opy_
        else:
          from selenium.webdriver.remote.client_config import ClientConfig
          ClientConfig.get_proxy_url = bstack1llll11lll_opy_
      except Exception as e:
        logger.error(bstack1l1lll11ll_opy_.format(str(e)))
  if not CONFIG.get(bstack11ll1ll_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩཬ"), False) and not bstack1lll11l11l_opy_:
    logger.info(bstack1lll11ll11_opy_)
  if not cli.is_enabled(CONFIG):
    if bstack11ll1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ཭") in CONFIG and str(CONFIG[bstack11ll1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭཮")]).lower() != bstack11ll1ll_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ཯"):
      bstack111ll1l11l_opy_()
    elif bstack1l1l11ll11_opy_ != bstack11ll1ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫ཰") or (bstack1l1l11ll11_opy_ == bstack11ll1ll_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲཱࠬ") and not bstack1lll11l11l_opy_):
      bstack1111l1lll1_opy_()
  if (bstack1l1l11ll11_opy_ in [bstack11ll1ll_opy_ (u"࠭ࡰࡢࡤࡲࡸིࠬ"), bstack11ll1ll_opy_ (u"ࠧࡳࡱࡥࡳࡹཱི࠭"), bstack11ll1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺ࠭ࡪࡰࡷࡩࡷࡴࡡ࡭ུࠩ")]):
    try:
      from robot import run_cli
      from robot.output import Output
      from robot.running.status import TestStatus
      from pabot.pabot import QueueItem
      from pabot import pabot
      try:
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCreator
        from SeleniumLibrary.keywords.webdrivertools.webdrivertools import WebDriverCache
        WebDriverCreator._get_ff_profile = bstack1llll1l111_opy_
        bstack1l11l11111_opy_ = WebDriverCache.close
      except Exception as e:
        logger.warn(bstack11l11l111l_opy_ + str(e))
      try:
        from AppiumLibrary.utils.applicationcache import ApplicationCache
        bstack111l111lll_opy_ = ApplicationCache.close
      except Exception as e:
        logger.debug(bstack1l111lll1_opy_ + str(e))
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack11l11l111l_opy_)
    if bstack1l1l11ll11_opy_ != bstack11ll1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ཱུࠪ"):
      bstack11l111llll_opy_()
    bstack1ll111lll_opy_ = Output.start_test
    bstack11ll11ll11_opy_ = Output.end_test
    bstack1ll1l11lll_opy_ = TestStatus.__init__
    bstack1ll1l1l1l_opy_ = pabot._run
    bstack1111ll111_opy_ = QueueItem.__init__
    bstack11lll11l1_opy_ = pabot._create_command_for_execution
    bstack111ll111ll_opy_ = pabot._report_results
  if bstack1l1l11ll11_opy_ == bstack11ll1ll_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪྲྀ"):
    try:
      from behave.runner import Runner
      from behave.model import Step
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack1l1l1ll1l1_opy_)
    bstack111l1ll11_opy_ = Runner.run_hook
    bstack111llll1ll_opy_ = Step.run
  if bstack1l1l11ll11_opy_ == bstack11ll1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫཷ"):
    try:
      from _pytest.config import Config
      bstack111lll11l1_opy_ = Config.getoption
      from _pytest import runner
      bstack1lll11111l_opy_ = runner._update_current_test_var
    except Exception as e:
      logger.warn(e, bstack1111ll11_opy_)
    try:
      from pytest_bdd import reporting
      bstack1l111l11ll_opy_ = reporting.runtest_makereport
    except Exception as e:
      logger.debug(bstack11ll1ll_opy_ (u"ࠬࡖ࡬ࡦࡣࡶࡩࠥ࡯࡮ࡴࡶࡤࡰࡱࠦࡰࡺࡶࡨࡷࡹ࠳ࡢࡥࡦࠣࡸࡴࠦࡲࡶࡰࠣࡴࡾࡺࡥࡴࡶ࠰ࡦࡩࡪࠠࡵࡧࡶࡸࡸ࠭ླྀ"))
  try:
    framework_name = bstack11ll1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬཹ") if bstack1l1l11ll11_opy_ in [bstack11ll1ll_opy_ (u"ࠧࡱࡣࡥࡳࡹེ࠭"), bstack11ll1ll_opy_ (u"ࠨࡴࡲࡦࡴࡺཻࠧ"), bstack11ll1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴ࠮࡫ࡱࡸࡪࡸ࡮ࡢ࡮ོࠪ")] else bstack11111l111_opy_(bstack1l1l11ll11_opy_)
    bstack111l11l11l_opy_ = {
      bstack11ll1ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨཽࠫ"): bstack11ll1ll_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷ࠱ࡨࡻࡣࡶ࡯ࡥࡩࡷ࠭ཾ") if bstack1l1l11ll11_opy_ == bstack11ll1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬཿ") and bstack1llllll1l1_opy_() else framework_name,
      bstack11ll1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡹࡩࡷࡹࡩࡰࡰྀࠪ"): bstack1ll111ll1l_opy_(framework_name),
      bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲཱྀࠬ"): __version__,
      bstack11ll1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩྂ"): bstack1l1l11ll11_opy_
    }
    if bstack1l1l11ll11_opy_ in bstack1ll1l111ll_opy_ + bstack1111l1ll11_opy_:
      if bstack1lll11l11_opy_.bstack11ll11111_opy_(CONFIG):
        if bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩྃ") in CONFIG:
          os.environ[bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏ྄ࠫ")] = os.getenv(bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ྅"), json.dumps(CONFIG[bstack11ll1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ྆")]))
          CONFIG[bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭྇")].pop(bstack11ll1ll_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬྈ"), None)
          CONFIG[bstack11ll1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨྉ")].pop(bstack11ll1ll_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧྊ"), None)
        bstack111l11l11l_opy_[bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪྋ")] = {
          bstack11ll1ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩྌ"): bstack11ll1ll_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧྍ"),
          bstack11ll1ll_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧྎ"): str(bstack11llll1111_opy_())
        }
    if bstack1l1l11ll11_opy_ not in [bstack11ll1ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠳ࡩ࡯ࡶࡨࡶࡳࡧ࡬ࠨྏ")] and not cli.is_running():
      bstack1ll1l1l11l_opy_, bstack1111l11111_opy_ = bstack1ll1l111_opy_.launch(CONFIG, bstack111l11l11l_opy_)
      if bstack1111l11111_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨྐ")) is not None and bstack1lll11l11_opy_.bstack1l1l1l1l1l_opy_(CONFIG) is None:
        value = bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩྑ")].get(bstack11ll1ll_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫྒ"))
        if value is not None:
            CONFIG[bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫྒྷ")] = value
        else:
          logger.debug(bstack11ll1ll_opy_ (u"ࠧࡔ࡯ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡦࡤࡸࡦࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥྔ"))
  except Exception as e:
    logger.debug(bstack11l1l11lll_opy_.format(bstack11ll1ll_opy_ (u"࠭ࡔࡦࡵࡷࡌࡺࡨࠧྕ"), str(e)))
  if bstack1l1l11ll11_opy_ == bstack11ll1ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧྖ"):
    bstack1llll11l11_opy_ = True
    if bstack1lll11l11l_opy_ and bstack111ll1ll1l_opy_:
      bstack11ll1lll1l_opy_ = CONFIG.get(bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࡌࡰࡥࡤࡰࡔࡶࡴࡪࡱࡱࡷࠬྗ"), {}).get(bstack11ll1ll_opy_ (u"ࠩ࡯ࡳࡨࡧ࡬ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ྘"))
      bstack111l11lll1_opy_(bstack1111l111ll_opy_)
    elif bstack1lll11l11l_opy_:
      bstack11ll1lll1l_opy_ = CONFIG.get(bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࡏࡱࡶ࡬ࡳࡳࡹࠧྙ"), {}).get(bstack11ll1ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭ྚ"))
      global bstack11l1lll1l1_opy_
      try:
        if bstack11llll1ll1_opy_(bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྛ")]) and multiprocessing.current_process().name == bstack11ll1ll_opy_ (u"࠭࠰ࠨྜ"):
          bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྜྷ")].remove(bstack11ll1ll_opy_ (u"ࠨ࠯ࡰࠫྞ"))
          bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྟ")].remove(bstack11ll1ll_opy_ (u"ࠪࡴࡩࡨࠧྠ"))
          bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྡ")] = bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྡྷ")][0]
          with open(bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྣ")], bstack11ll1ll_opy_ (u"ࠧࡳࠩྤ")) as f:
            file_content = f.read()
          bstack1ll1111ll_opy_ = bstack11ll1ll_opy_ (u"ࠣࠤࠥࡪࡷࡵ࡭ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡴࡦ࡮ࠤ࡮ࡳࡰࡰࡴࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢ࡭ࡳ࡯ࡴࡪࡣ࡯࡭ࡿ࡫࠻ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡪࡰ࡬ࡸ࡮ࡧ࡬ࡪࡼࡨࠬࢀࢃࠩ࠼ࠢࡩࡶࡴࡳࠠࡱࡦࡥࠤ࡮ࡳࡰࡰࡴࡷࠤࡕࡪࡢ࠼ࠢࡲ࡫ࡤࡪࡢࠡ࠿ࠣࡔࡩࡨ࠮ࡥࡱࡢࡦࡷ࡫ࡡ࡬࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡤࡦࡨࠣࡱࡴࡪ࡟ࡣࡴࡨࡥࡰ࠮ࡳࡦ࡮ࡩ࠰ࠥࡧࡲࡨ࠮ࠣࡸࡪࡳࡰࡰࡴࡤࡶࡾࠦ࠽ࠡ࠲ࠬ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡸࡷࡿ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡣࡵ࡫ࠥࡃࠠࡴࡶࡵࠬ࡮ࡴࡴࠩࡣࡵ࡫࠮࠱࠱࠱ࠫࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡧࡻࡧࡪࡶࡴࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡦࡹࠠࡦ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡴࡦࡹࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡯ࡨࡡࡧࡦ࠭ࡹࡥ࡭ࡨ࠯ࡥࡷ࡭ࠬࡵࡧࡰࡴࡴࡸࡡࡳࡻࠬࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡑࡦࡥ࠲ࡩࡵ࡟ࡣࠢࡀࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡔࡩࡨ࠮ࡥࡱࡢࡦࡷ࡫ࡡ࡬ࠢࡀࠤࡲࡵࡤࡠࡤࡵࡩࡦࡱࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡔࡩࡨࠨࠪ࠰ࡶࡩࡹࡥࡴࡳࡣࡦࡩ࠭࠯࡜࡯ࠤࠥࠦྥ").format(str(bstack1lll11l11l_opy_))
          bstack1l11lll111_opy_ = bstack1ll1111ll_opy_ + file_content
          bstack1l111ll111_opy_ = bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬྦ")] + bstack11ll1ll_opy_ (u"ࠪࡣࡧࡹࡴࡢࡥ࡮ࡣࡹ࡫࡭ࡱ࠰ࡳࡽࠬྦྷ")
          with open(bstack1l111ll111_opy_, bstack11ll1ll_opy_ (u"ࠫࡼ࠭ྨ")):
            pass
          with open(bstack1l111ll111_opy_, bstack11ll1ll_opy_ (u"ࠧࡽࠫࠣྩ")) as f:
            f.write(bstack1l11lll111_opy_)
          import subprocess
          process_data = subprocess.run([bstack11ll1ll_opy_ (u"ࠨࡰࡺࡶ࡫ࡳࡳࠨྪ"), bstack1l111ll111_opy_])
          if os.path.exists(bstack1l111ll111_opy_):
            os.unlink(bstack1l111ll111_opy_)
          os._exit(process_data.returncode)
        else:
          if bstack11llll1ll1_opy_(bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྫ")]):
            bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྫྷ")].remove(bstack11ll1ll_opy_ (u"ࠩ࠰ࡱࠬྭ"))
            bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ྮ")].remove(bstack11ll1ll_opy_ (u"ࠫࡵࡪࡢࠨྯ"))
            bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྰ")] = bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩྱ")][0]
          bstack111l11lll1_opy_(bstack1111l111ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪྲ")])))
          sys.argv = sys.argv[2:]
          mod_globals = globals()
          mod_globals[bstack11ll1ll_opy_ (u"ࠨࡡࡢࡲࡦࡳࡥࡠࡡࠪླ")] = bstack11ll1ll_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫྴ")
          mod_globals[bstack11ll1ll_opy_ (u"ࠪࡣࡤ࡬ࡩ࡭ࡧࡢࡣࠬྵ")] = os.path.abspath(bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧྶ")])
          exec(open(bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨྷ")]).read(), mod_globals)
      except BaseException as e:
        try:
          traceback.print_exc()
          logger.error(bstack11ll1ll_opy_ (u"࠭ࡃࡢࡷࡪ࡬ࡹࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯࠼ࠣࡿࢂ࠭ྸ").format(str(e)))
          for driver in bstack11l1lll1l1_opy_:
            bstack1l1l11ll1_opy_.append({
              bstack11ll1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬྐྵ"): bstack1lll11l11l_opy_[bstack11ll1ll_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫྺ")],
              bstack11ll1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨྻ"): str(e),
              bstack11ll1ll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩྼ"): multiprocessing.current_process().name
            })
            bstack11l1l111ll_opy_(driver, bstack11ll1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ྽"), bstack11ll1ll_opy_ (u"࡙ࠧࡥࡴࡵ࡬ࡳࡳࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࡢ࡮ࠣ྾") + str(e))
        except Exception:
          pass
      finally:
        try:
          for driver in bstack11l1lll1l1_opy_:
            driver.quit()
        except Exception as e:
          pass
    else:
      percy.init(bstack11llll1l1_opy_, CONFIG, logger)
      bstack1ll1l1llll_opy_()
      bstack11ll1llll_opy_()
      percy.bstack1ll1lll1ll_opy_()
      bstack1lll11l1l_opy_ = {
        bstack11ll1ll_opy_ (u"࠭ࡦࡪ࡮ࡨࡣࡳࡧ࡭ࡦࠩ྿"): args[0],
        bstack11ll1ll_opy_ (u"ࠧࡄࡑࡑࡊࡎࡍࠧ࿀"): CONFIG,
        bstack11ll1ll_opy_ (u"ࠨࡊࡘࡆࡤ࡛ࡒࡍࠩ࿁"): bstack11lll11111_opy_,
        bstack11ll1ll_opy_ (u"ࠩࡌࡗࡤࡇࡐࡑࡡࡄ࡙࡙ࡕࡍࡂࡖࡈࠫ࿂"): bstack11llll1l1_opy_
      }
      if bstack11ll1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭࿃") in CONFIG:
        bstack1l111ll11l_opy_ = bstack1l11llllll_opy_(args, logger, CONFIG, bstack1l1ll11l11_opy_, bstack11ll111ll_opy_)
        bstack1111ll1l1_opy_ = bstack1l111ll11l_opy_.bstack1lllll111_opy_(run_on_browserstack, bstack1lll11l1l_opy_, bstack11llll1ll1_opy_(args))
      else:
        if bstack11llll1ll1_opy_(args):
          bstack1lll11l1l_opy_[bstack11ll1ll_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧ࿄")] = args
          test = multiprocessing.Process(name=str(0),
                                         target=run_on_browserstack, args=(bstack1lll11l1l_opy_,))
          test.start()
          test.join()
        else:
          bstack111l11lll1_opy_(bstack1111l111ll_opy_)
          sys.path.append(os.path.dirname(os.path.abspath(args[0])))
          mod_globals = globals()
          mod_globals[bstack11ll1ll_opy_ (u"ࠬࡥ࡟࡯ࡣࡰࡩࡤࡥࠧ࿅")] = bstack11ll1ll_opy_ (u"࠭࡟ࡠ࡯ࡤ࡭ࡳࡥ࡟ࠨ࿆")
          mod_globals[bstack11ll1ll_opy_ (u"ࠧࡠࡡࡩ࡭ࡱ࡫࡟ࡠࠩ࿇")] = os.path.abspath(args[0])
          sys.argv = sys.argv[2:]
          exec(open(args[0]).read(), mod_globals)
  elif bstack1l1l11ll11_opy_ == bstack11ll1ll_opy_ (u"ࠨࡲࡤࡦࡴࡺࠧ࿈") or bstack1l1l11ll11_opy_ == bstack11ll1ll_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ࿉"):
    percy.init(bstack11llll1l1_opy_, CONFIG, logger)
    percy.bstack1ll1lll1ll_opy_()
    try:
      from pabot import pabot
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack11l11l111l_opy_)
    bstack1ll1l1llll_opy_()
    bstack111l11lll1_opy_(bstack1l1111l1l_opy_)
    if bstack1l1ll11l11_opy_:
      bstack111l11lll_opy_(bstack1l1111l1l_opy_, args)
      if bstack11ll1ll_opy_ (u"ࠪ࠱࠲ࡶࡲࡰࡥࡨࡷࡸ࡫ࡳࠨ࿊") in args:
        i = args.index(bstack11ll1ll_opy_ (u"ࠫ࠲࠳ࡰࡳࡱࡦࡩࡸࡹࡥࡴࠩ࿋"))
        args.pop(i)
        args.pop(i)
      if bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ࿌") not in CONFIG:
        CONFIG[bstack11ll1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ࿍")] = [{}]
        bstack11ll111ll_opy_ = 1
      if bstack1l111l111_opy_ == 0:
        bstack1l111l111_opy_ = 1
      args.insert(0, str(bstack1l111l111_opy_))
      args.insert(0, str(bstack11ll1ll_opy_ (u"ࠧ࠮࠯ࡳࡶࡴࡩࡥࡴࡵࡨࡷࠬ࿎")))
    if bstack1ll1l111_opy_.on():
      try:
        from robot.run import USAGE
        from robot.utils import ArgumentParser
        from pabot.arguments import _parse_pabot_args
        bstack111l1ll111_opy_, pabot_args = _parse_pabot_args(args)
        opts, bstack1l111111l_opy_ = ArgumentParser(
            USAGE,
            auto_pythonpath=False,
            auto_argumentfile=True,
            env_options=bstack11ll1ll_opy_ (u"ࠣࡔࡒࡆࡔ࡚࡟ࡐࡒࡗࡍࡔࡔࡓࠣ࿏"),
        ).parse_args(bstack111l1ll111_opy_)
        bstack1ll1l111l1_opy_ = args.index(bstack111l1ll111_opy_[0]) if len(bstack111l1ll111_opy_) > 0 else len(args)
        args.insert(bstack1ll1l111l1_opy_, str(bstack11ll1ll_opy_ (u"ࠩ࠰࠱ࡱ࡯ࡳࡵࡧࡱࡩࡷ࠭࿐")))
        args.insert(bstack1ll1l111l1_opy_ + 1, str(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11ll1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡶࡴࡨ࡯ࡵࡡ࡯࡭ࡸࡺࡥ࡯ࡧࡵ࠲ࡵࡿࠧ࿑"))))
        if bstack1llllll11_opy_.bstack1lll1llll_opy_(CONFIG):
          args.insert(bstack1ll1l111l1_opy_, str(bstack11ll1ll_opy_ (u"ࠫ࠲࠳࡬ࡪࡵࡷࡩࡳ࡫ࡲࠨ࿒")))
          args.insert(bstack1ll1l111l1_opy_ + 1, str(bstack11ll1ll_opy_ (u"ࠬࡘࡥࡵࡴࡼࡊࡦ࡯࡬ࡦࡦ࠽ࡿࢂ࠭࿓").format(bstack1llllll11_opy_.bstack111l11ll_opy_(CONFIG))))
        if bstack11l1ll11l_opy_(os.environ.get(bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠫ࿔"))) and str(os.environ.get(bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡒࡆࡔࡘࡒࡤ࡚ࡅࡔࡖࡖࠫ࿕"), bstack11ll1ll_opy_ (u"ࠨࡰࡸࡰࡱ࠭࿖"))) != bstack11ll1ll_opy_ (u"ࠩࡱࡹࡱࡲࠧ࿗"):
          for bstack1l1l1l1ll_opy_ in bstack1l111111l_opy_:
            args.remove(bstack1l1l1l1ll_opy_)
          test_files = os.environ.get(bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࡠࡖࡈࡗ࡙࡙ࠧ࿘")).split(bstack11ll1ll_opy_ (u"ࠫ࠱࠭࿙"))
          for bstack1ll1l1ll1l_opy_ in test_files:
            args.append(bstack1ll1l1ll1l_opy_)
      except Exception as e:
        logger.error(bstack11ll1ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡥࡹࡺࡡࡤࡪ࡬ࡲ࡬ࠦ࡬ࡪࡵࡷࡩࡳ࡫ࡲࠡࡨࡲࡶࠥࢁࡽ࠯ࠢࡈࡶࡷࡵࡲࠡ࠯ࠣࡿࢂࠨ࿚").format(bstack11ll1l1l1_opy_, e))
    pabot.main(args)
  elif bstack1l1l11ll11_opy_ == bstack11ll1ll_opy_ (u"࠭ࡲࡰࡤࡲࡸ࠲࡯࡮ࡵࡧࡵࡲࡦࡲࠧ࿛"):
    try:
      from robot import run_cli
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack11l11l111l_opy_)
    for a in args:
      if bstack11ll1ll_opy_ (u"ࠧࡃࡕࡗࡅࡈࡑࡐࡍࡃࡗࡊࡔࡘࡍࡊࡐࡇࡉ࡝࠭࿜") in a:
        bstack11111l11l_opy_ = int(a.split(bstack11ll1ll_opy_ (u"ࠨ࠼ࠪ࿝"))[1])
      if bstack11ll1ll_opy_ (u"ࠩࡅࡗ࡙ࡇࡃࡌࡆࡈࡊࡑࡕࡃࡂࡎࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭࿞") in a:
        bstack11ll1lll1l_opy_ = str(a.split(bstack11ll1ll_opy_ (u"ࠪ࠾ࠬ࿟"))[1])
      if bstack11ll1ll_opy_ (u"ࠫࡇ࡙ࡔࡂࡅࡎࡇࡑࡏࡁࡓࡉࡖࠫ࿠") in a:
        bstack1l1lll1l11_opy_ = str(a.split(bstack11ll1ll_opy_ (u"ࠬࡀࠧ࿡"))[1])
    bstack1lll1l1lll_opy_ = None
    bstack11l1ll11l1_opy_ = None
    if bstack11ll1ll_opy_ (u"࠭࠭࠮ࡤࡶࡸࡦࡩ࡫ࡠ࡫ࡷࡩࡲࡥࡩ࡯ࡦࡨࡼࠬ࿢") in args:
      i = args.index(bstack11ll1ll_opy_ (u"ࠧ࠮࠯ࡥࡷࡹࡧࡣ࡬ࡡ࡬ࡸࡪࡳ࡟ࡪࡰࡧࡩࡽ࠭࿣"))
      args.pop(i)
      bstack1lll1l1lll_opy_ = args.pop(i)
    if bstack11ll1ll_opy_ (u"ࠨ࠯࠰ࡦࡸࡺࡡࡤ࡭ࡢࡴࡱࡧࡴࡧࡱࡵࡱࡤ࡯࡮ࡥࡧࡻࠫ࿤") in args:
      i = args.index(bstack11ll1ll_opy_ (u"ࠩ࠰࠱ࡧࡹࡴࡢࡥ࡮ࡣࡵࡲࡡࡵࡨࡲࡶࡲࡥࡩ࡯ࡦࡨࡼࠬ࿥"))
      args.pop(i)
      bstack11l1ll11l1_opy_ = args.pop(i)
    if bstack1lll1l1lll_opy_ is not None:
      global bstack1ll1ll111l_opy_
      bstack1ll1ll111l_opy_ = bstack1lll1l1lll_opy_
    if bstack11l1ll11l1_opy_ is not None and int(bstack11111l11l_opy_) < 0:
      bstack11111l11l_opy_ = int(bstack11l1ll11l1_opy_)
    bstack111l11lll1_opy_(bstack1l1111l1l_opy_)
    run_cli(args)
    if bstack11ll1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡢࡩࡷࡸ࡯ࡳࡡ࡯࡭ࡸࡺࠧ࿦") in multiprocessing.current_process().__dict__.keys():
      for bstack11l1111l1l_opy_ in multiprocessing.current_process().bstack_error_list:
        bstack1l1l11ll1_opy_.append(bstack11l1111l1l_opy_)
  elif bstack1l1l11ll11_opy_ == bstack11ll1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ࿧"):
    bstack111ll1l1ll_opy_ = bstack1lll111l1_opy_(args, logger, CONFIG, bstack1l1ll11l11_opy_)
    bstack111ll1l1ll_opy_.bstack1lll1ll11_opy_()
    bstack1ll1l1llll_opy_()
    bstack111l111l1_opy_ = True
    bstack1l1l1111l1_opy_ = bstack111ll1l1ll_opy_.bstack111l1l1l_opy_()
    bstack111ll1l1ll_opy_.bstack1lll11l1l_opy_(bstack111l11l1ll_opy_)
    bstack111ll1l1ll_opy_.bstack1lll1ll1l_opy_()
    bstack11llll111l_opy_(bstack1l1l11ll11_opy_, CONFIG, bstack111ll1l1ll_opy_.bstack1llllllll_opy_())
    bstack1lll1ll11l_opy_ = bstack111ll1l1ll_opy_.bstack1lllll111_opy_(bstack1ll1l11l1_opy_, {
      bstack11ll1ll_opy_ (u"ࠬࡎࡕࡃࡡࡘࡖࡑ࠭࿨"): bstack11lll11111_opy_,
      bstack11ll1ll_opy_ (u"࠭ࡉࡔࡡࡄࡔࡕࡥࡁࡖࡖࡒࡑࡆ࡚ࡅࠨ࿩"): bstack11llll1l1_opy_,
      bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡁࡖࡖࡒࡑࡆ࡚ࡉࡐࡐࠪ࿪"): bstack1l1ll11l11_opy_
    })
    try:
      bstack1llll11111_opy_, bstack1ll1l1111l_opy_ = map(list, zip(*bstack1lll1ll11l_opy_))
      bstack11111ll111_opy_ = bstack1llll11111_opy_[0]
      for status_code in bstack1ll1l1111l_opy_:
        if status_code != 0:
          bstack11l1l1ll1l_opy_ = status_code
          break
    except Exception as e:
      logger.debug(bstack11ll1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡧࡶࡦࠢࡨࡶࡷࡵࡲࡴࠢࡤࡲࡩࠦࡳࡵࡣࡷࡹࡸࠦࡣࡰࡦࡨ࠲ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࠼ࠣࡿࢂࠨ࿫").format(str(e)))
  elif bstack1l1l11ll11_opy_ == bstack11ll1ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ࿬"):
    try:
      from behave.__main__ import main as bstack11lll1ll11_opy_
      from behave.configuration import Configuration
    except Exception as e:
      bstack1lll11llll_opy_(e, bstack1l1l1ll1l1_opy_)
    bstack1ll1l1llll_opy_()
    bstack111l111l1_opy_ = True
    bstack1llll11ll_opy_ = 1
    if bstack11ll1ll_opy_ (u"ࠪࡴࡦࡸࡡ࡭࡮ࡨࡰࡸࡖࡥࡳࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ࿭") in CONFIG:
      bstack1llll11ll_opy_ = CONFIG[bstack11ll1ll_opy_ (u"ࠫࡵࡧࡲࡢ࡮࡯ࡩࡱࡹࡐࡦࡴࡓࡰࡦࡺࡦࡰࡴࡰࠫ࿮")]
    if bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ࿯") in CONFIG:
      bstack11ll11l1l1_opy_ = int(bstack1llll11ll_opy_) * int(len(CONFIG[bstack11ll1ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ࿰")]))
    else:
      bstack11ll11l1l1_opy_ = int(bstack1llll11ll_opy_)
    config = Configuration(args)
    bstack11l1111l11_opy_ = config.paths
    if len(bstack11l1111l11_opy_) == 0:
      import glob
      pattern = bstack11ll1ll_opy_ (u"ࠧࠫࠬ࠲࠮࠳࡬ࡥࡢࡶࡸࡶࡪ࠭࿱")
      bstack1111ll1l1l_opy_ = glob.glob(pattern, recursive=True)
      args.extend(bstack1111ll1l1l_opy_)
      config = Configuration(args)
      bstack11l1111l11_opy_ = config.paths
    bstack111l1111_opy_ = [os.path.normpath(item) for item in bstack11l1111l11_opy_]
    bstack11lllllll_opy_ = [os.path.normpath(item) for item in args]
    bstack111ll1ll1_opy_ = [item for item in bstack11lllllll_opy_ if item not in bstack111l1111_opy_]
    import platform as pf
    if pf.system().lower() == bstack11ll1ll_opy_ (u"ࠨࡹ࡬ࡲࡩࡵࡷࡴࠩ࿲"):
      from pathlib import PureWindowsPath, PurePosixPath
      bstack111l1111_opy_ = [str(PurePosixPath(PureWindowsPath(bstack11l11l1l1l_opy_)))
                    for bstack11l11l1l1l_opy_ in bstack111l1111_opy_]
    bstack1lll1l1l1_opy_ = []
    for spec in bstack111l1111_opy_:
      bstack1lllll11l_opy_ = []
      bstack1lllll11l_opy_ += bstack111ll1ll1_opy_
      bstack1lllll11l_opy_.append(spec)
      bstack1lll1l1l1_opy_.append(bstack1lllll11l_opy_)
    execution_items = []
    for bstack1lllll11l_opy_ in bstack1lll1l1l1_opy_:
      if bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ࿳") in CONFIG:
        for index, _ in enumerate(CONFIG[bstack11ll1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭࿴")]):
          item = {}
          item[bstack11ll1ll_opy_ (u"ࠫࡦࡸࡧࠨ࿵")] = bstack11ll1ll_opy_ (u"ࠬࠦࠧ࿶").join(bstack1lllll11l_opy_)
          item[bstack11ll1ll_opy_ (u"࠭ࡩ࡯ࡦࡨࡼࠬ࿷")] = index
          execution_items.append(item)
      else:
        item = {}
        item[bstack11ll1ll_opy_ (u"ࠧࡢࡴࡪࠫ࿸")] = bstack11ll1ll_opy_ (u"ࠨࠢࠪ࿹").join(bstack1lllll11l_opy_)
        item[bstack11ll1ll_opy_ (u"ࠩ࡬ࡲࡩ࡫ࡸࠨ࿺")] = 0
        execution_items.append(item)
    bstack1111ll11l1_opy_ = bstack1111lllll1_opy_(execution_items, bstack11ll11l1l1_opy_)
    for execution_item in bstack1111ll11l1_opy_:
      bstack11111l11_opy_ = []
      for item in execution_item:
        bstack11111l11_opy_.append(bstack1ll1l111l_opy_(name=str(item[bstack11ll1ll_opy_ (u"ࠪ࡭ࡳࡪࡥࡹࠩ࿻")]),
                                             target=bstack11lll1l11l_opy_,
                                             args=(item[bstack11ll1ll_opy_ (u"ࠫࡦࡸࡧࠨ࿼")],)))
      for t in bstack11111l11_opy_:
        t.start()
      for t in bstack11111l11_opy_:
        t.join()
  else:
    bstack1ll1ll11ll_opy_(bstack1llll1ll11_opy_)
  if not bstack1lll11l11l_opy_:
    bstack1l1l11l111_opy_()
    if(bstack1l1l11ll11_opy_ in [bstack11ll1ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ࿽"), bstack11ll1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭࿾")]):
      bstack111l1l111l_opy_()
  bstack11111l1ll1_opy_.bstack1l1lll1ll1_opy_()
def browserstack_initialize(bstack11ll11111l_opy_=None):
  logger.info(bstack11ll1ll_opy_ (u"ࠧࡓࡷࡱࡲ࡮ࡴࡧࠡࡕࡇࡏࠥࡽࡩࡵࡪࠣࡥࡷ࡭ࡳ࠻ࠢࠪ࿿") + str(bstack11ll11111l_opy_))
  run_on_browserstack(bstack11ll11111l_opy_, None, True)
@measure(event_name=EVENTS.bstack1l1l1l1ll1_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1l1l11l111_opy_():
  global CONFIG
  global bstack11l1ll11ll_opy_
  global bstack11l1l1ll1l_opy_
  global bstack1l11lll1l_opy_
  global bstack1llllll1l_opy_
  bstack1lll1l1ll1_opy_.bstack1l11l11l1l_opy_()
  if cli.is_running():
    bstack1l1llll11l_opy_.invoke(Events.bstack11lll1ll1l_opy_)
  else:
    bstack1111111l_opy_ = bstack1llllll11_opy_.bstack1lll11ll1_opy_(config=CONFIG)
    bstack1111111l_opy_.bstack1ll11lll1_opy_(CONFIG)
  if bstack11l1ll11ll_opy_ == bstack11ll1ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨက"):
    if not cli.is_enabled(CONFIG):
      bstack1ll1l111_opy_.stop()
  else:
    bstack1ll1l111_opy_.stop()
  if not cli.is_enabled(CONFIG):
    bstack1l11l1l1_opy_.bstack1l1l11l1ll_opy_()
  if bstack11ll1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭ခ") in CONFIG and str(CONFIG[bstack11ll1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧဂ")]).lower() != bstack11ll1ll_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪဃ"):
    hashed_id, bstack11l1ll111l_opy_ = bstack1lllll11ll_opy_()
  else:
    hashed_id, bstack11l1ll111l_opy_ = get_build_link()
  bstack11llll1l11_opy_(hashed_id)
  logger.info(bstack11ll1ll_opy_ (u"࡙ࠬࡄࡌࠢࡵࡹࡳࠦࡥ࡯ࡦࡨࡨࠥ࡬࡯ࡳࠢ࡬ࡨ࠿࠭င") + bstack1llllll1l_opy_.get_property(bstack11ll1ll_opy_ (u"࠭ࡳࡥ࡭ࡕࡹࡳࡏࡤࠨစ"), bstack11ll1ll_opy_ (u"ࠧࠨဆ")) + bstack11ll1ll_opy_ (u"ࠨ࠮ࠣࡸࡪࡹࡴࡩࡷࡥࠤ࡮ࡪ࠺ࠡࠩဇ") + os.getenv(bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧဈ"), bstack11ll1ll_opy_ (u"ࠪࠫဉ")))
  if hashed_id is not None and bstack111l1ll1ll_opy_() != -1:
    sessions = bstack111l11llll_opy_(hashed_id)
    bstack1ll111l1ll_opy_(sessions, bstack11l1ll111l_opy_)
  if bstack11l1ll11ll_opy_ == bstack11ll1ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫည") and bstack11l1l1ll1l_opy_ != 0:
    sys.exit(bstack11l1l1ll1l_opy_)
  if bstack11l1ll11ll_opy_ == bstack11ll1ll_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬဋ") and bstack1l11lll1l_opy_ != 0:
    sys.exit(bstack1l11lll1l_opy_)
def bstack11llll1l11_opy_(new_id):
    global bstack1l1ll1ll1_opy_
    bstack1l1ll1ll1_opy_ = new_id
def bstack11111l111_opy_(bstack1l1l111ll_opy_):
  if bstack1l1l111ll_opy_:
    return bstack1l1l111ll_opy_.capitalize()
  else:
    return bstack11ll1ll_opy_ (u"࠭ࠧဌ")
@measure(event_name=EVENTS.bstack11ll11l1l_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1ll1ll1l1_opy_(bstack1l1111l11_opy_):
  if bstack11ll1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬဍ") in bstack1l1111l11_opy_ and bstack1l1111l11_opy_[bstack11ll1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ဎ")] != bstack11ll1ll_opy_ (u"ࠩࠪဏ"):
    return bstack1l1111l11_opy_[bstack11ll1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨတ")]
  else:
    bstack1111l1l1ll_opy_ = bstack11ll1ll_opy_ (u"ࠦࠧထ")
    if bstack11ll1ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࠬဒ") in bstack1l1111l11_opy_ and bstack1l1111l11_opy_[bstack11ll1ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ဓ")] != None:
      bstack1111l1l1ll_opy_ += bstack1l1111l11_opy_[bstack11ll1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧန")] + bstack11ll1ll_opy_ (u"ࠣ࠮ࠣࠦပ")
      if bstack1l1111l11_opy_[bstack11ll1ll_opy_ (u"ࠩࡲࡷࠬဖ")] == bstack11ll1ll_opy_ (u"ࠥ࡭ࡴࡹࠢဗ"):
        bstack1111l1l1ll_opy_ += bstack11ll1ll_opy_ (u"ࠦ࡮ࡕࡓࠡࠤဘ")
      bstack1111l1l1ll_opy_ += (bstack1l1111l11_opy_[bstack11ll1ll_opy_ (u"ࠬࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠩမ")] or bstack11ll1ll_opy_ (u"࠭ࠧယ"))
      return bstack1111l1l1ll_opy_
    else:
      bstack1111l1l1ll_opy_ += bstack11111l111_opy_(bstack1l1111l11_opy_[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨရ")]) + bstack11ll1ll_opy_ (u"ࠣࠢࠥလ") + (
              bstack1l1111l11_opy_[bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫဝ")] or bstack11ll1ll_opy_ (u"ࠪࠫသ")) + bstack11ll1ll_opy_ (u"ࠦ࠱ࠦࠢဟ")
      if bstack1l1111l11_opy_[bstack11ll1ll_opy_ (u"ࠬࡵࡳࠨဠ")] == bstack11ll1ll_opy_ (u"ࠨࡗࡪࡰࡧࡳࡼࡹࠢအ"):
        bstack1111l1l1ll_opy_ += bstack11ll1ll_opy_ (u"ࠢࡘ࡫ࡱࠤࠧဢ")
      bstack1111l1l1ll_opy_ += bstack1l1111l11_opy_[bstack11ll1ll_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬဣ")] or bstack11ll1ll_opy_ (u"ࠩࠪဤ")
      return bstack1111l1l1ll_opy_
@measure(event_name=EVENTS.bstack11l1l1l1ll_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack111l1lll11_opy_(bstack1l11l111ll_opy_):
  if bstack1l11l111ll_opy_ == bstack11ll1ll_opy_ (u"ࠥࡨࡴࡴࡥࠣဥ"):
    return bstack11ll1ll_opy_ (u"ࠫࡁࡺࡤࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨࠠࡴࡶࡼࡰࡪࡃࠢࡤࡱ࡯ࡳࡷࡀࡧࡳࡧࡨࡲࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡧࡳࡧࡨࡲࠧࡄࡃࡰ࡯ࡳࡰࡪࡺࡥࡥ࠾࠲ࡪࡴࡴࡴ࠿࠾࠲ࡸࡩࡄࠧဦ")
  elif bstack1l11l111ll_opy_ == bstack11ll1ll_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࠧဧ"):
    return bstack11ll1ll_opy_ (u"࠭࠼ࡵࡦࠣࡧࡱࡧࡳࡴ࠿ࠥࡦࡸࡺࡡࡤ࡭࠰ࡨࡦࡺࡡࠣࠢࡶࡸࡾࡲࡥ࠾ࠤࡦࡳࡱࡵࡲ࠻ࡴࡨࡨࡀࠨ࠾࠽ࡨࡲࡲࡹࠦࡣࡰ࡮ࡲࡶࡂࠨࡲࡦࡦࠥࡂࡋࡧࡩ࡭ࡧࡧࡀ࠴࡬࡯࡯ࡶࡁࡀ࠴ࡺࡤ࠿ࠩဨ")
  elif bstack1l11l111ll_opy_ == bstack11ll1ll_opy_ (u"ࠢࡱࡣࡶࡷࡪࡪࠢဩ"):
    return bstack11ll1ll_opy_ (u"ࠨ࠾ࡷࡨࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࠤࡸࡺࡹ࡭ࡧࡀࠦࡨࡵ࡬ࡰࡴ࠽࡫ࡷ࡫ࡥ࡯࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥ࡫ࡷ࡫ࡥ࡯ࠤࡁࡔࡦࡹࡳࡦࡦ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨဪ")
  elif bstack1l11l111ll_opy_ == bstack11ll1ll_opy_ (u"ࠤࡨࡶࡷࡵࡲࠣါ"):
    return bstack11ll1ll_opy_ (u"ࠪࡀࡹࡪࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࠦࡳࡵࡻ࡯ࡩࡂࠨࡣࡰ࡮ࡲࡶ࠿ࡸࡥࡥ࠽ࠥࡂࡁ࡬࡯࡯ࡶࠣࡧࡴࡲ࡯ࡳ࠿ࠥࡶࡪࡪࠢ࠿ࡇࡵࡶࡴࡸ࠼࠰ࡨࡲࡲࡹࡄ࠼࠰ࡶࡧࡂࠬာ")
  elif bstack1l11l111ll_opy_ == bstack11ll1ll_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧိ"):
    return bstack11ll1ll_opy_ (u"ࠬࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠢࠡࡵࡷࡽࡱ࡫࠽ࠣࡥࡲࡰࡴࡸ࠺ࠤࡧࡨࡥ࠸࠸࠶࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࠦࡩࡪࡧ࠳࠳࠸ࠥࡂ࡙࡯࡭ࡦࡱࡸࡸࡁ࠵ࡦࡰࡰࡷࡂࡁ࠵ࡴࡥࡀࠪီ")
  elif bstack1l11l111ll_opy_ == bstack11ll1ll_opy_ (u"ࠨࡲࡶࡰࡱ࡭ࡳ࡭ࠢု"):
    return bstack11ll1ll_opy_ (u"ࠧ࠽ࡶࡧࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࠣࡷࡹࡿ࡬ࡦ࠿ࠥࡧࡴࡲ࡯ࡳ࠼ࡥࡰࡦࡩ࡫࠼ࠤࡁࡀ࡫ࡵ࡮ࡵࠢࡦࡳࡱࡵࡲ࠾ࠤࡥࡰࡦࡩ࡫ࠣࡀࡕࡹࡳࡴࡩ࡯ࡩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨူ")
  else:
    return bstack11ll1ll_opy_ (u"ࠨ࠾ࡷࡨࠥࡧ࡬ࡪࡩࡱࡁࠧࡩࡥ࡯ࡶࡨࡶࠧࠦࡣ࡭ࡣࡶࡷࡂࠨࡢࡴࡶࡤࡧࡰ࠳ࡤࡢࡶࡤࠦࠥࡹࡴࡺ࡮ࡨࡁࠧࡩ࡯࡭ࡱࡵ࠾ࡧࡲࡡࡤ࡭࠾ࠦࡃࡂࡦࡰࡰࡷࠤࡨࡵ࡬ࡰࡴࡀࠦࡧࡲࡡࡤ࡭ࠥࡂࠬေ") + bstack11111l111_opy_(
      bstack1l11l111ll_opy_) + bstack11ll1ll_opy_ (u"ࠩ࠿࠳࡫ࡵ࡮ࡵࡀ࠿࠳ࡹࡪ࠾ࠨဲ")
def bstack1l1lllllll_opy_(session):
  return bstack11ll1ll_opy_ (u"ࠪࡀࡹࡸࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡳࡱࡺࠦࡃࡂࡴࡥࠢࡦࡰࡦࡹࡳ࠾ࠤࡥࡷࡹࡧࡣ࡬࠯ࡧࡥࡹࡧࠠࡴࡧࡶࡷ࡮ࡵ࡮࠮ࡰࡤࡱࡪࠨ࠾࠽ࡣࠣ࡬ࡷ࡫ࡦ࠾ࠤࡾࢁࠧࠦࡴࡢࡴࡪࡩࡹࡃࠢࡠࡤ࡯ࡥࡳࡱࠢ࠿ࡽࢀࡀ࠴ࡧ࠾࠽࠱ࡷࡨࡃࢁࡽࡼࡿ࠿ࡸࡩࠦࡡ࡭࡫ࡪࡲࡂࠨࡣࡦࡰࡷࡩࡷࠨࠠࡤ࡮ࡤࡷࡸࡃࠢࡣࡵࡷࡥࡨࡱ࠭ࡥࡣࡷࡥࠧࡄࡻࡾ࠾࠲ࡸࡩࡄ࠼ࡵࡦࠣࡥࡱ࡯ࡧ࡯࠿ࠥࡧࡪࡴࡴࡦࡴࠥࠤࡨࡲࡡࡴࡵࡀࠦࡧࡹࡴࡢࡥ࡮࠱ࡩࡧࡴࡢࠤࡁࡿࢂࡂ࠯ࡵࡦࡁࡀࡹࡪࠠࡢ࡮࡬࡫ࡳࡃࠢࡤࡧࡱࡸࡪࡸࠢࠡࡥ࡯ࡥࡸࡹ࠽ࠣࡤࡶࡸࡦࡩ࡫࠮ࡦࡤࡸࡦࠨ࠾ࡼࡿ࠿࠳ࡹࡪ࠾࠽ࡶࡧࠤࡦࡲࡩࡨࡰࡀࠦࡨ࡫࡮ࡵࡧࡵࠦࠥࡩ࡬ࡢࡵࡶࡁࠧࡨࡳࡵࡣࡦ࡯࠲ࡪࡡࡵࡣࠥࡂࢀࢃ࠼࠰ࡶࡧࡂࡁ࠵ࡴࡳࡀࠪဳ").format(
    session[bstack11ll1ll_opy_ (u"ࠫࡵࡻࡢ࡭࡫ࡦࡣࡺࡸ࡬ࠨဴ")], bstack1ll1ll1l1_opy_(session), bstack111l1lll11_opy_(session[bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡸࡺࡡࡵࡷࡶࠫဵ")]),
    bstack111l1lll11_opy_(session[bstack11ll1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭ံ")]),
    bstack11111l111_opy_(session[bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨ့")] or session[bstack11ll1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨး")] or bstack11ll1ll_opy_ (u"္ࠩࠪ")) + bstack11ll1ll_opy_ (u"ࠥࠤ်ࠧ") + (session[bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭ျ")] or bstack11ll1ll_opy_ (u"ࠬ࠭ြ")),
    session[bstack11ll1ll_opy_ (u"࠭࡯ࡴࠩွ")] + bstack11ll1ll_opy_ (u"ࠢࠡࠤှ") + session[bstack11ll1ll_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬဿ")], session[bstack11ll1ll_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࠫ၀")] or bstack11ll1ll_opy_ (u"ࠪࠫ၁"),
    session[bstack11ll1ll_opy_ (u"ࠫࡨࡸࡥࡢࡶࡨࡨࡤࡧࡴࠨ၂")] if session[bstack11ll1ll_opy_ (u"ࠬࡩࡲࡦࡣࡷࡩࡩࡥࡡࡵࠩ၃")] else bstack11ll1ll_opy_ (u"࠭ࠧ၄"))
@measure(event_name=EVENTS.bstack111ll11111_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def bstack1ll111l1ll_opy_(sessions, bstack11l1ll111l_opy_):
  try:
    bstack11ll11l1ll_opy_ = bstack11ll1ll_opy_ (u"ࠢࠣ၅")
    if not os.path.exists(bstack1l1l11111l_opy_):
      os.mkdir(bstack1l1l11111l_opy_)
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), bstack11ll1ll_opy_ (u"ࠨࡣࡶࡷࡪࡺࡳ࠰ࡴࡨࡴࡴࡸࡴ࠯ࡪࡷࡱࡱ࠭၆")), bstack11ll1ll_opy_ (u"ࠩࡵࠫ၇")) as f:
      bstack11ll11l1ll_opy_ = f.read()
    bstack11ll11l1ll_opy_ = bstack11ll11l1ll_opy_.replace(bstack11ll1ll_opy_ (u"ࠪࡿࠪࡘࡅࡔࡗࡏࡘࡘࡥࡃࡐࡗࡑࡘࠪࢃࠧ၈"), str(len(sessions)))
    bstack11ll11l1ll_opy_ = bstack11ll11l1ll_opy_.replace(bstack11ll1ll_opy_ (u"ࠫࢀࠫࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠧࢀࠫ၉"), bstack11l1ll111l_opy_)
    bstack11ll11l1ll_opy_ = bstack11ll11l1ll_opy_.replace(bstack11ll1ll_opy_ (u"ࠬࢁࠥࡃࡗࡌࡐࡉࡥࡎࡂࡏࡈࠩࢂ࠭၊"),
                                              sessions[0].get(bstack11ll1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡴࡡ࡮ࡧࠪ။")) if sessions[0] else bstack11ll1ll_opy_ (u"ࠧࠨ၌"))
    with open(os.path.join(bstack1l1l11111l_opy_, bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠭ࡳࡧࡳࡳࡷࡺ࠮ࡩࡶࡰࡰࠬ၍")), bstack11ll1ll_opy_ (u"ࠩࡺࠫ၎")) as stream:
      stream.write(bstack11ll11l1ll_opy_.split(bstack11ll1ll_opy_ (u"ࠪࡿ࡙ࠪࡅࡔࡕࡌࡓࡓ࡙࡟ࡅࡃࡗࡅࠪࢃࠧ၏"))[0])
      for session in sessions:
        stream.write(bstack1l1lllllll_opy_(session))
      stream.write(bstack11ll11l1ll_opy_.split(bstack11ll1ll_opy_ (u"ࠫࢀࠫࡓࡆࡕࡖࡍࡔࡔࡓࡠࡆࡄࡘࡆࠫࡽࠨၐ"))[1])
    logger.info(bstack11ll1ll_opy_ (u"ࠬࡍࡥ࡯ࡧࡵࡥࡹ࡫ࡤࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠠࡣࡷ࡬ࡰࡩࠦࡡࡳࡶ࡬ࡪࡦࡩࡴࡴࠢࡤࡸࠥࢁࡽࠨၑ").format(bstack1l1l11111l_opy_));
  except Exception as e:
    logger.debug(bstack11111l1lll_opy_.format(str(e)))
def bstack111l11llll_opy_(hashed_id):
  global CONFIG
  try:
    bstack111111ll11_opy_ = datetime.datetime.now()
    host = bstack11ll1ll_opy_ (u"࠭ࡨࡵࡶࡳࡷ࠿࠵࠯ࡢࡲ࡬࠱ࡨࡲ࡯ࡶࡦ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠭ၒ") if bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳࠫၓ") in CONFIG else bstack11ll1ll_opy_ (u"ࠨࡪࡷࡸࡵࡹ࠺࠰࠱ࡤࡴ࡮࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡩ࡯࡮ࠩၔ")
    user = CONFIG[bstack11ll1ll_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫၕ")]
    key = CONFIG[bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ၖ")]
    bstack1l1lllll1_opy_ = bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰ࠮ࡣࡸࡸࡴࡳࡡࡵࡧࠪၗ") if bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱࠩၘ") in CONFIG else (bstack11ll1ll_opy_ (u"࠭ࡴࡶࡴࡥࡳࡸࡩࡡ࡭ࡧࠪၙ") if CONFIG.get(bstack11ll1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫၚ")) else bstack11ll1ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪၛ"))
    host = bstack111l111l11_opy_(cli.config, [bstack11ll1ll_opy_ (u"ࠤࡤࡴ࡮ࡹࠢၜ"), bstack11ll1ll_opy_ (u"ࠥࡥࡵࡶࡁࡶࡶࡲࡱࡦࡺࡥࠣၝ"), bstack11ll1ll_opy_ (u"ࠦࡦࡶࡩࠣၞ")], host) if bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱࠩၟ") in CONFIG else bstack111l111l11_opy_(cli.config, [bstack11ll1ll_opy_ (u"ࠨࡡࡱ࡫ࡶࠦၠ"), bstack11ll1ll_opy_ (u"ࠢࡢࡷࡷࡳࡲࡧࡴࡦࠤၡ"), bstack11ll1ll_opy_ (u"ࠣࡣࡳ࡭ࠧၢ")], host)
    url = bstack11ll1ll_opy_ (u"ࠩࡾࢁ࠴ࢁࡽ࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸ࡫ࡳࡴ࡫ࡲࡲࡸ࠴ࡪࡴࡱࡱࠫၣ").format(host, bstack1l1lllll1_opy_, hashed_id)
    headers = {
      bstack11ll1ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩၤ"): bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧၥ"),
    }
    proxies = bstack11l111l11_opy_(CONFIG, url)
    response = requests.get(url, headers=headers, proxies=proxies, auth=(user, key))
    if response.json():
      cli.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࡫ࡪࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡴࡡ࡯࡭ࡸࡺࠢၦ"), datetime.datetime.now() - bstack111111ll11_opy_)
      return list(map(lambda session: session[bstack11ll1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࡢࡷࡪࡹࡳࡪࡱࡱࠫၧ")], response.json()))
  except Exception as e:
    logger.debug(bstack111llll1l_opy_.format(str(e)))
@measure(event_name=EVENTS.bstack111ll1ll11_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def get_build_link():
  global CONFIG
  global bstack1l1ll1ll1_opy_
  try:
    if bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪၨ") in CONFIG:
      bstack111111ll11_opy_ = datetime.datetime.now()
      host = bstack11ll1ll_opy_ (u"ࠨࡣࡳ࡭࠲ࡩ࡬ࡰࡷࡧࠫၩ") if bstack11ll1ll_opy_ (u"ࠩࡤࡴࡵ࠭ၪ") in CONFIG else bstack11ll1ll_opy_ (u"ࠪࡥࡵ࡯ࠧၫ")
      user = CONFIG[bstack11ll1ll_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ၬ")]
      key = CONFIG[bstack11ll1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨၭ")]
      bstack1l1lllll1_opy_ = bstack11ll1ll_opy_ (u"࠭ࡡࡱࡲ࠰ࡥࡺࡺ࡯࡮ࡣࡷࡩࠬၮ") if bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳࠫၯ") in CONFIG else bstack11ll1ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪၰ")
      url = bstack11ll1ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳ࠻࠱࠲ࡿࢂࡀࡻࡾࡂࡾࢁ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠲࡯ࡹ࡯࡯ࠩၱ").format(user, key, host, bstack1l1lllll1_opy_)
      if cli.is_enabled(CONFIG):
        bstack11l1ll111l_opy_, hashed_id = cli.bstack1l1ll1l11l_opy_()
        logger.info(bstack1ll1ll11l_opy_.format(bstack11l1ll111l_opy_))
        return [hashed_id, bstack11l1ll111l_opy_]
      else:
        headers = {
          bstack11ll1ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱ࡹࡿࡰࡦࠩၲ"): bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧၳ"),
        }
        if bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧၴ") in CONFIG:
          params = {bstack11ll1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫၵ"): CONFIG[bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪၶ")], bstack11ll1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫၷ"): CONFIG[bstack11ll1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫၸ")]}
        else:
          params = {bstack11ll1ll_opy_ (u"ࠪࡲࡦࡳࡥࠨၹ"): CONFIG[bstack11ll1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧၺ")]}
        proxies = bstack11l111l11_opy_(CONFIG, url)
        response = requests.get(url, params=params, headers=headers, proxies=proxies)
        if response.json():
          bstack11l11lll11_opy_ = response.json()[0][bstack11ll1ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡥࡹ࡮ࡲࡤࠨၻ")]
          if bstack11l11lll11_opy_:
            bstack11l1ll111l_opy_ = bstack11l11lll11_opy_[bstack11ll1ll_opy_ (u"࠭ࡰࡶࡤ࡯࡭ࡨࡥࡵࡳ࡮ࠪၼ")].split(bstack11ll1ll_opy_ (u"ࠧࡱࡷࡥࡰ࡮ࡩ࠭ࡣࡷ࡬ࡰࡩ࠭ၽ"))[0] + bstack11ll1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡳ࠰ࠩၾ") + bstack11l11lll11_opy_[
              bstack11ll1ll_opy_ (u"ࠩ࡫ࡥࡸ࡮ࡥࡥࡡ࡬ࡨࠬၿ")]
            logger.info(bstack1ll1ll11l_opy_.format(bstack11l1ll111l_opy_))
            bstack1l1ll1ll1_opy_ = bstack11l11lll11_opy_[bstack11ll1ll_opy_ (u"ࠪ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ႀ")]
            bstack1l111l11l_opy_ = CONFIG[bstack11ll1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧႁ")]
            if bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧႂ") in CONFIG:
              bstack1l111l11l_opy_ += bstack11ll1ll_opy_ (u"࠭ࠠࠨႃ") + CONFIG[bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩႄ")]
            if bstack1l111l11l_opy_ != bstack11l11lll11_opy_[bstack11ll1ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ႅ")]:
              logger.debug(bstack1llll1ll1l_opy_.format(bstack11l11lll11_opy_[bstack11ll1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧႆ")], bstack1l111l11l_opy_))
            cli.bstack11lllll111_opy_(bstack11ll1ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻ࡩࡨࡸࡤࡨࡵࡪ࡮ࡧࡣࡱ࡯࡮࡬ࠤႇ"), datetime.datetime.now() - bstack111111ll11_opy_)
            return [bstack11l11lll11_opy_[bstack11ll1ll_opy_ (u"ࠫ࡭ࡧࡳࡩࡧࡧࡣ࡮ࡪࠧႈ")], bstack11l1ll111l_opy_]
    else:
      logger.warn(bstack1l11ll1l1_opy_)
  except Exception as e:
    logger.debug(bstack1l1111lll_opy_.format(str(e)))
  return [None, None]
def bstack1llll1lll1_opy_(url, bstack1l1111ll11_opy_=False):
  global CONFIG
  global bstack1lll111111_opy_
  if not bstack1lll111111_opy_:
    hostname = bstack1111l1111_opy_(url)
    is_private = bstack1l111ll1l_opy_(hostname)
    if (bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩႉ") in CONFIG and not bstack11l1ll11l_opy_(CONFIG[bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡑࡵࡣࡢ࡮ࠪႊ")])) and (is_private or bstack1l1111ll11_opy_):
      bstack1lll111111_opy_ = hostname
def bstack1111l1111_opy_(url):
  return urlparse(url).hostname
def bstack1l111ll1l_opy_(hostname):
  for bstack11l1ll1111_opy_ in bstack11lll111l_opy_:
    regex = re.compile(bstack11l1ll1111_opy_)
    if regex.match(hostname):
      return True
  return False
def bstack1llll111ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
@measure(event_name=EVENTS.bstack1111111l1l_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def getAccessibilityResults(driver):
  global CONFIG
  global bstack11111l11l_opy_
  bstack1111111ll1_opy_ = not (bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫႋ"), None) and bstack1l1l1ll1_opy_(
          threading.current_thread(), bstack11ll1ll_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧႌ"), None))
  bstack1111l1ll1_opy_ = getattr(driver, bstack11ll1ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ႍࠩ"), None) != True
  bstack1l11lll11l_opy_ = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪႎ"), None) and bstack1l1l1ll1_opy_(
          threading.current_thread(), bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ႏ"), None)
  if bstack1l11lll11l_opy_:
    if not bstack111l1ll1l1_opy_():
      logger.warning(bstack11ll1ll_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡰࡱࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴࠬࠡࡥࡤࡲࡳࡵࡴࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡅࡵࡶࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳ࠯ࠤ႐"))
      return {}
    logger.debug(bstack11ll1ll_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪ႑"))
    logger.debug(perform_scan(driver, driver_command=bstack11ll1ll_opy_ (u"ࠧࡦࡺࡨࡧࡺࡺࡥࡔࡥࡵ࡭ࡵࡺࠧ႒")))
    results = bstack11ll111l1l_opy_(bstack11ll1ll_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡴࠤ႓"))
    if results is not None and results.get(bstack11ll1ll_opy_ (u"ࠤ࡬ࡷࡸࡻࡥࡴࠤ႔")) is not None:
        return results[bstack11ll1ll_opy_ (u"ࠥ࡭ࡸࡹࡵࡦࡵࠥ႕")]
    logger.error(bstack11ll1ll_opy_ (u"ࠦࡓࡵࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡓࡧࡶࡹࡱࡺࡳࠡࡹࡨࡶࡪࠦࡦࡰࡷࡱࡨ࠳ࠨ႖"))
    return []
  if not bstack1lll11l11_opy_.bstack1lll1ll1l1_opy_(CONFIG, bstack11111l11l_opy_) or (bstack1111l1ll1_opy_ and bstack1111111ll1_opy_):
    logger.warning(bstack11ll1ll_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹ࠮ࠣ႗"))
    return {}
  try:
    logger.debug(bstack11ll1ll_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡩࡨࡸࡹ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪ႘"))
    logger.debug(perform_scan(driver))
    results = driver.execute_async_script(bstack11lll1l1l_opy_.bstack1l1ll11l1_opy_)
    return results
  except Exception:
    logger.error(bstack11ll1ll_opy_ (u"ࠢࡏࡱࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡼ࡫ࡲࡦࠢࡩࡳࡺࡴࡤ࠯ࠤ႙"))
    return {}
@measure(event_name=EVENTS.bstack1l1l111lll_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def getAccessibilityResultsSummary(driver):
  global CONFIG
  global bstack11111l11l_opy_
  bstack1111111ll1_opy_ = not (bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬႚ"), None) and bstack1l1l1ll1_opy_(
          threading.current_thread(), bstack11ll1ll_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨႛ"), None))
  bstack1111l1ll1_opy_ = getattr(driver, bstack11ll1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭ࡄ࠵࠶ࡿࡓࡩࡱࡸࡰࡩ࡙ࡣࡢࡰࠪႜ"), None) != True
  bstack1l11lll11l_opy_ = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠫ࡮ࡹࡁࡱࡲࡄ࠵࠶ࡿࡔࡦࡵࡷࠫႝ"), None) and bstack1l1l1ll1_opy_(
          threading.current_thread(), bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱࡃ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧ႞"), None)
  if bstack1l11lll11l_opy_:
    if not bstack111l1ll1l1_opy_():
      logger.warning(bstack11ll1ll_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡱࡲࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠭ࠢࡦࡥࡳࡴ࡯ࡵࠢࡵࡩࡹࡸࡩࡦࡸࡨࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡶࡹࡲࡳࡡࡳࡻ࠱ࠦ႟"))
      return {}
    logger.debug(bstack11ll1ll_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡸࡻ࡭࡮ࡣࡵࡽࠬႠ"))
    logger.debug(perform_scan(driver, driver_command=bstack11ll1ll_opy_ (u"ࠨࡧࡻࡩࡨࡻࡴࡦࡕࡦࡶ࡮ࡶࡴࠨႡ")))
    results = bstack11ll111l1l_opy_(bstack11ll1ll_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡕࡸࡱࡲࡧࡲࡺࠤႢ"))
    if results is not None and results.get(bstack11ll1ll_opy_ (u"ࠥࡷࡺࡳ࡭ࡢࡴࡼࠦႣ")) is not None:
        return results[bstack11ll1ll_opy_ (u"ࠦࡸࡻ࡭࡮ࡣࡵࡽࠧႤ")]
    logger.error(bstack11ll1ll_opy_ (u"ࠧࡔ࡯ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡔࡨࡷࡺࡲࡴࡴࠢࡖࡹࡲࡳࡡࡳࡻࠣࡻࡦࡹࠠࡧࡱࡸࡲࡩ࠴ࠢႥ"))
    return {}
  if not bstack1lll11l11_opy_.bstack1lll1ll1l1_opy_(CONFIG, bstack11111l11l_opy_) or (bstack1111l1ll1_opy_ and bstack1111111ll1_opy_):
    logger.warning(bstack11ll1ll_opy_ (u"ࠨࡎࡰࡶࠣࡥࡳࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥࡩࡡ࡯ࡰࡲࡸࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡵࡸࡱࡲࡧࡲࡺ࠰ࠥႦ"))
    return {}
  try:
    logger.debug(bstack11ll1ll_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡸࡻ࡭࡮ࡣࡵࡽࠬႧ"))
    logger.debug(perform_scan(driver))
    bstack1l1l1l1lll_opy_ = driver.execute_async_script(bstack11lll1l1l_opy_.bstack11l1ll111_opy_)
    return bstack1l1l1l1lll_opy_
  except Exception:
    logger.error(bstack11ll1ll_opy_ (u"ࠣࡐࡲࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸࡻ࡭࡮ࡣࡵࡽࠥࡽࡡࡴࠢࡩࡳࡺࡴࡤ࠯ࠤႨ"))
    return {}
def bstack111l1ll1l1_opy_():
  global CONFIG
  global bstack11111l11l_opy_
  bstack1l11l11l11_opy_ = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩႩ"), None) and bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬႪ"), None)
  if not bstack1lll11l11_opy_.bstack1lll1ll1l1_opy_(CONFIG, bstack11111l11l_opy_) or not bstack1l11l11l11_opy_:
        logger.warning(bstack11ll1ll_opy_ (u"ࠦࡓࡵࡴࠡࡣࡱࠤࡆࡶࡰࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡹࡥࡴࡵ࡬ࡳࡳ࠲ࠠࡤࡣࡱࡲࡴࡺࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡵࡩࡸࡻ࡬ࡵࡵ࠱ࠦႫ"))
        return False
  return True
def bstack11ll111l1l_opy_(bstack1ll11111ll_opy_):
    bstack111lll111_opy_ = bstack1ll1l111_opy_.current_test_uuid() if bstack1ll1l111_opy_.current_test_uuid() else bstack1l11l1l1_opy_.current_hook_uuid()
    with ThreadPoolExecutor() as executor:
        future = executor.submit(bstack1ll11l111l_opy_(bstack111lll111_opy_, bstack1ll11111ll_opy_))
        try:
            return future.result(timeout=bstack11l111111l_opy_)
        except TimeoutError:
            logger.error(bstack11ll1ll_opy_ (u"࡚ࠧࡩ࡮ࡧࡲࡹࡹࠦࡡࡧࡶࡨࡶࠥࢁࡽࡴࠢࡺ࡬࡮ࡲࡥࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡖࡪࡹࡵ࡭ࡶࡶࠦႬ").format(bstack11l111111l_opy_))
        except Exception as ex:
            logger.debug(bstack11ll1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡸࡥࡵࡴ࡬ࡩࡻ࡯࡮ࡨࠢࡄࡴࡵࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡿࢂ࠴ࠠࡆࡴࡵࡳࡷࠦ࠭ࠡࡽࢀࠦႭ").format(bstack1ll11111ll_opy_, str(ex)))
    return {}
@measure(event_name=EVENTS.bstack111l1l1l11_opy_, stage=STAGE.bstack11l11ll1ll_opy_, bstack1111l1l1ll_opy_=bstack11l1l1llll_opy_)
def perform_scan(driver, *args, **kwargs):
  global CONFIG
  global bstack11111l11l_opy_
  bstack1111111ll1_opy_ = not (bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫႮ"), None) and bstack1l1l1ll1_opy_(
          threading.current_thread(), bstack11ll1ll_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧႯ"), None))
  bstack1ll11111l_opy_ = not (bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩႰ"), None) and bstack1l1l1ll1_opy_(
          threading.current_thread(), bstack11ll1ll_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬႱ"), None))
  bstack1111l1ll1_opy_ = getattr(driver, bstack11ll1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫႲ"), None) != True
  if not bstack1lll11l11_opy_.bstack1lll1ll1l1_opy_(CONFIG, bstack11111l11l_opy_) or (bstack1111l1ll1_opy_ and bstack1111111ll1_opy_ and bstack1ll11111l_opy_):
    logger.warning(bstack11ll1ll_opy_ (u"ࠧࡔ࡯ࡵࠢࡤࡲࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡩࡸࡹࡩࡰࡰ࠯ࠤࡨࡧ࡮࡯ࡱࡷࠤࡷࡻ࡮ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳ࠴ࠢႳ"))
    return {}
  try:
    bstack1ll111l1l_opy_ = bstack11ll1ll_opy_ (u"࠭ࡡࡱࡲࠪႴ") in CONFIG and CONFIG.get(bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳࠫႵ"), bstack11ll1ll_opy_ (u"ࠨࠩႶ"))
    session_id = getattr(driver, bstack11ll1ll_opy_ (u"ࠩࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩ࠭Ⴗ"), None)
    if not session_id:
      logger.warning(bstack11ll1ll_opy_ (u"ࠥࡒࡴࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡊࡆࠣࡪࡴࡻ࡮ࡥࠢࡩࡳࡷࠦࡤࡳ࡫ࡹࡩࡷࠨႸ"))
      return {bstack11ll1ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥႹ"): bstack11ll1ll_opy_ (u"ࠧࡔ࡯ࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡌࡈࠥ࡬࡯ࡶࡰࡧࠦႺ")}
    if bstack1ll111l1l_opy_:
      try:
        bstack111l1llll1_opy_ = {
              bstack11ll1ll_opy_ (u"࠭ࡴࡩࡌࡺࡸ࡙ࡵ࡫ࡦࡰࠪႻ"): os.environ.get(bstack11ll1ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬႼ"), os.environ.get(bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡌ࡚ࡘࠬႽ"), bstack11ll1ll_opy_ (u"ࠩࠪႾ"))),
              bstack11ll1ll_opy_ (u"ࠪࡸ࡭࡚ࡥࡴࡶࡕࡹࡳ࡛ࡵࡪࡦࠪႿ"): bstack1ll1l111_opy_.current_test_uuid() if bstack1ll1l111_opy_.current_test_uuid() else bstack1l11l1l1_opy_.current_hook_uuid(),
              bstack11ll1ll_opy_ (u"ࠫࡦࡻࡴࡩࡊࡨࡥࡩ࡫ࡲࠨჀ"): os.environ.get(bstack11ll1ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪჁ")),
              bstack11ll1ll_opy_ (u"࠭ࡳࡤࡣࡱࡘ࡮ࡳࡥࡴࡶࡤࡱࡵ࠭Ⴢ"): str(int(datetime.datetime.now().timestamp() * 1000)),
              bstack11ll1ll_opy_ (u"ࠧࡵࡪࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬჃ"): os.environ.get(bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭Ⴤ"), bstack11ll1ll_opy_ (u"ࠩࠪჅ")),
              bstack11ll1ll_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪ჆"): kwargs.get(bstack11ll1ll_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࡣࡨࡵ࡭࡮ࡣࡱࡨࠬჇ"), None) or bstack11ll1ll_opy_ (u"ࠬ࠭჈")
          }
        if not hasattr(thread_local, bstack11ll1ll_opy_ (u"࠭ࡢࡢࡵࡨࡣࡦࡶࡰࡠࡣ࠴࠵ࡾࡥࡳࡤࡴ࡬ࡴࡹ࠭჉")):
            scripts = {bstack11ll1ll_opy_ (u"ࠧࡴࡥࡤࡲࠬ჊"): bstack11lll1l1l_opy_.perform_scan}
            thread_local.base_app_a11y_script = scripts
        bstack111111lll_opy_ = copy.deepcopy(thread_local.base_app_a11y_script)
        bstack111111lll_opy_[bstack11ll1ll_opy_ (u"ࠨࡵࡦࡥࡳ࠭჋")] = bstack111111lll_opy_[bstack11ll1ll_opy_ (u"ࠩࡶࡧࡦࡴࠧ჌")] % json.dumps(bstack111l1llll1_opy_)
        bstack11lll1l1l_opy_.bstack1ll11lllll_opy_(bstack111111lll_opy_)
        bstack11lll1l1l_opy_.store()
        bstack11ll1l1lll_opy_ = driver.execute_script(bstack11lll1l1l_opy_.perform_scan)
      except Exception as bstack1ll1111ll1_opy_:
        logger.info(bstack11ll1ll_opy_ (u"ࠥࡅࡵࡶࡩࡶ࡯ࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡨࡧ࡮ࠡࡨࡤ࡭ࡱ࡫ࡤ࠻ࠢࠥჍ") + str(bstack1ll1111ll1_opy_))
        bstack11ll1l1lll_opy_ = {bstack11ll1ll_opy_ (u"ࠦࡪࡸࡲࡰࡴࠥ჎"): str(bstack1ll1111ll1_opy_)}
    else:
      bstack11ll1l1lll_opy_ = driver.execute_async_script(bstack11lll1l1l_opy_.perform_scan, {bstack11ll1ll_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࠬ჏"): kwargs.get(bstack11ll1ll_opy_ (u"࠭ࡤࡳ࡫ࡹࡩࡷࡥࡣࡰ࡯ࡰࡥࡳࡪࠧა"), None) or bstack11ll1ll_opy_ (u"ࠧࠨბ")})
    return bstack11ll1l1lll_opy_
  except Exception as err:
    logger.error(bstack11ll1ll_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡷࡻ࡮ࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡦࡥࡳ࠴ࠠࡼࡿࠥგ").format(str(err)))
    return {}