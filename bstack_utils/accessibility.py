# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1l1l1ll_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l1l1111l1_opy_ as bstack1lllll1111l1_opy_, EVENTS
from bstack_utils.bstack1l1l1l1l1_opy_ import bstack1l1l1l1l1_opy_
from bstack_utils.helper import bstack1lll1111_opy_, bstack1l11llll_opy_, bstack1ll11llll1_opy_, bstack111l1l1l111_opy_, \
  bstack1111l1l111l_opy_, bstack111l1l1l11_opy_, get_host_info, bstack111l1l1l11l_opy_, bstack1ll1l1lll_opy_, error_handler, bstack111l1ll1ll1_opy_, bstack1111l1ll1l1_opy_, bstack1l1l11l1_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack11l1l1l1ll_opy_ import get_logger
from bstack_utils.bstack11l1l1ll11_opy_ import bstack1llll11ll11_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack11l1l1ll11_opy_ = bstack1llll11ll11_opy_()
@error_handler(class_method=False)
def _1llll1llll11_opy_(driver, bstack1lll1l1l1_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11ll_opy_ (u"ࠩࡲࡷࡤࡴࡡ࡮ࡧࠪΎ"): caps.get(bstack11ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩῬ"), None),
        bstack11ll_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ῭"): bstack1lll1l1l1_opy_.get(bstack11ll_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ΅"), None),
        bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬ`"): caps.get(bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ῰"), None),
        bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ῱"): caps.get(bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪῲ"), None)
    }
  except Exception as error:
    logger.debug(bstack11ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤ࠿ࠦࠧῳ") + str(error))
  return response
def on():
    if os.environ.get(bstack11ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩῴ"), None) is None or os.environ[bstack11ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ῵")] == bstack11ll_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦῶ"):
        return False
    return True
def bstack111ll1ll11_opy_(config):
  return config.get(bstack11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧῷ"), False) or any([p.get(bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨῸ"), False) == True for p in config.get(bstack11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬΌ"), [])])
def bstack1ll11l1ll_opy_(config, bstack1lll111ll1_opy_):
  try:
    bstack1llll1ll111l_opy_ = config.get(bstack11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪῺ"), False)
    if int(bstack1lll111ll1_opy_) < len(config.get(bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧΏ"), [])) and config[bstack11ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨῼ")][bstack1lll111ll1_opy_]:
      bstack1lllll1111ll_opy_ = config[bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ´")][bstack1lll111ll1_opy_].get(bstack11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ῾"), None)
    else:
      bstack1lllll1111ll_opy_ = config.get(bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ῿"), None)
    if bstack1lllll1111ll_opy_ != None:
      bstack1llll1ll111l_opy_ = bstack1lllll1111ll_opy_
    bstack1lllll111111_opy_ = os.getenv(bstack11ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ ")) is not None and len(os.getenv(bstack11ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ "))) > 0 and os.getenv(bstack11ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ ")) != bstack11ll_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ ")
    return bstack1llll1ll111l_opy_ and bstack1lllll111111_opy_
  except Exception as error:
    logger.debug(bstack11ll_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡥࡳ࡫ࡩࡽ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭ ") + str(error))
  return False
def bstack11l11lll1_opy_(test_tags):
  bstack1l1111l1l1l_opy_ = os.getenv(bstack11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ "))
  if bstack1l1111l1l1l_opy_ is None:
    return True
  bstack1l1111l1l1l_opy_ = json.loads(bstack1l1111l1l1l_opy_)
  try:
    include_tags = bstack1l1111l1l1l_opy_[bstack11ll_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭ ")] if bstack11ll_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ ") in bstack1l1111l1l1l_opy_ and isinstance(bstack1l1111l1l1l_opy_[bstack11ll_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ ")], list) else []
    exclude_tags = bstack1l1111l1l1l_opy_[bstack11ll_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ ")] if bstack11ll_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ ") in bstack1l1111l1l1l_opy_ and isinstance(bstack1l1111l1l1l_opy_[bstack11ll_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ​")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11ll_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡼࡡ࡭࡫ࡧࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡦࡴ࡮ࡪࡰࡪ࠲ࠥࡋࡲࡳࡱࡵࠤ࠿ࠦࠢ‌") + str(error))
  return False
def bstack1llll1lll1l1_opy_(config, frameworkName, bstack1llll1ll1111_opy_, bstack1lllll11111l_opy_):
  bstack1llll1ll11l1_opy_ = bstack111l1l1l111_opy_(config)
  bstack1llll1ll1lll_opy_ = bstack1111l1l111l_opy_(config)
  if bstack1llll1ll11l1_opy_ is None or bstack1llll1ll1lll_opy_ is None:
    logger.error(bstack11ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩ‍"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ‎"), bstack11ll_opy_ (u"ࠪࡿࢂ࠭‏")))
    data = {
        bstack11ll_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ‐"): config[bstack11ll_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ‑")],
        bstack11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ‒"): config.get(bstack11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ–"), os.path.basename(os.getcwd())),
        bstack11ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡔࡪ࡯ࡨࠫ—"): bstack1lll1111_opy_(),
        bstack11ll_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ―"): config.get(bstack11ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭‖"), bstack11ll_opy_ (u"ࠫࠬ‗")),
        bstack11ll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ‘"): {
            bstack11ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭’"): frameworkName,
            bstack11ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ‚"): bstack1llll1ll1111_opy_,
            bstack11ll_opy_ (u"ࠨࡵࡧ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ‛"): __version__,
            bstack11ll_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ“"): bstack11ll_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ”"),
            bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ„"): bstack11ll_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧ‟"),
            bstack11ll_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭†"): bstack1lllll11111l_opy_
        },
        bstack11ll_opy_ (u"ࠧࡴࡧࡷࡸ࡮ࡴࡧࡴࠩ‡"): settings,
        bstack11ll_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࡅࡲࡲࡹࡸ࡯࡭ࠩ•"): bstack111l1l1l11l_opy_(),
        bstack11ll_opy_ (u"ࠩࡦ࡭ࡎࡴࡦࡰࠩ‣"): bstack111l1l1l11_opy_(),
        bstack11ll_opy_ (u"ࠪ࡬ࡴࡹࡴࡊࡰࡩࡳࠬ․"): get_host_info(),
        bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭‥"): bstack1ll11llll1_opy_(config)
    }
    headers = {
        bstack11ll_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ…"): bstack11ll_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ‧"),
    }
    config = {
        bstack11ll_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ "): (bstack1llll1ll11l1_opy_, bstack1llll1ll1lll_opy_),
        bstack11ll_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ "): headers
    }
    response = bstack1ll1l1lll_opy_(bstack11ll_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ‪"), bstack1lllll1111l1_opy_ + bstack11ll_opy_ (u"ࠪ࠳ࡻ࠸࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵࠪ‫"), data, config)
    bstack1llll1lll111_opy_ = response.json()
    if bstack1llll1lll111_opy_[bstack11ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ‬")]:
      parsed = json.loads(os.getenv(bstack11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭‭"), bstack11ll_opy_ (u"࠭ࡻࡾࠩ‮")))
      parsed[bstack11ll_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ ")] = bstack1llll1lll111_opy_[bstack11ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭‰")][bstack11ll_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ‱")]
      os.environ[bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ′")] = json.dumps(parsed)
      bstack1l1l1l1l1_opy_.bstack1l11l11l1_opy_(bstack1llll1lll111_opy_[bstack11ll_opy_ (u"ࠫࡩࡧࡴࡢࠩ″")][bstack11ll_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭‴")])
      bstack1l1l1l1l1_opy_.bstack1lllll111lll_opy_(bstack1llll1lll111_opy_[bstack11ll_opy_ (u"࠭ࡤࡢࡶࡤࠫ‵")][bstack11ll_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩ‶")])
      bstack1l1l1l1l1_opy_.store()
      return bstack1llll1lll111_opy_[bstack11ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭‷")][bstack11ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡖࡲ࡯ࡪࡴࠧ‸")], bstack1llll1lll111_opy_[bstack11ll_opy_ (u"ࠪࡨࡦࡺࡡࠨ‹")][bstack11ll_opy_ (u"ࠫ࡮ࡪࠧ›")]
    else:
      logger.error(bstack11ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥ࠭※") + bstack1llll1lll111_opy_[bstack11ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ‼")])
      if bstack1llll1lll111_opy_[bstack11ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ‽")] == bstack11ll_opy_ (u"ࠨࡋࡱࡺࡦࡲࡩࡥࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡳࡥࡸࡹࡥࡥ࠰ࠪ‾"):
        for bstack1llll1ll1l1l_opy_ in bstack1llll1lll111_opy_[bstack11ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩ‿")]:
          logger.error(bstack1llll1ll1l1l_opy_[bstack11ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⁀")])
      return None, None
  except Exception as error:
    logger.error(bstack11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠧ⁁") +  str(error))
    return None, None
def bstack1llll1l1lll1_opy_():
  if os.getenv(bstack11ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ⁂")) is None:
    return {
        bstack11ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭⁃"): bstack11ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭⁄"),
        bstack11ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⁅"): bstack11ll_opy_ (u"ࠩࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣ࡬ࡦࡪࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠨ⁆")
    }
  data = {bstack11ll_opy_ (u"ࠪࡩࡳࡪࡔࡪ࡯ࡨࠫ⁇"): bstack1lll1111_opy_()}
  headers = {
      bstack11ll_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫ⁈"): bstack11ll_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥ࠭⁉") + os.getenv(bstack11ll_opy_ (u"ࠨࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠦ⁊")),
      bstack11ll_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭⁋"): bstack11ll_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ⁌")
  }
  response = bstack1ll1l1lll_opy_(bstack11ll_opy_ (u"ࠩࡓ࡙࡙࠭⁍"), bstack1lllll1111l1_opy_ + bstack11ll_opy_ (u"ࠪ࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹ࠯ࡴࡶࡲࡴࠬ⁎"), data, { bstack11ll_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ⁏"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11ll_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰࠣࡱࡦࡸ࡫ࡦࡦࠣࡥࡸࠦࡣࡰ࡯ࡳࡰࡪࡺࡥࡥࠢࡤࡸࠥࠨ⁐") + bstack1l11llll_opy_().isoformat() + bstack11ll_opy_ (u"࡚࠭ࠨ⁑"))
      return {bstack11ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⁒"): bstack11ll_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ⁓"), bstack11ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⁔"): bstack11ll_opy_ (u"ࠪࠫ⁕")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡤࡱࡰࡴࡱ࡫ࡴࡪࡱࡱࠤࡴ࡬ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡘࡪࡹࡴࠡࡔࡸࡲ࠿ࠦࠢ⁖") + str(error))
    return {
        bstack11ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⁗"): bstack11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ⁘"),
        bstack11ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⁙"): str(error)
    }
def bstack1llll1ll11ll_opy_(bstack1llll1l1ll1l_opy_):
    return re.match(bstack11ll_opy_ (u"ࡳࠩࡡࡠࡩ࠱ࠨ࡝࠰࡟ࡨ࠰࠯࠿ࠥࠩ⁚"), bstack1llll1l1ll1l_opy_.strip()) is not None
def bstack11ll1l1l1_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1l1l1l1_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1l1l1l1_opy_ = desired_capabilities
        else:
          bstack1llll1l1l1l1_opy_ = {}
        bstack1l111ll1111_opy_ = (bstack1llll1l1l1l1_opy_.get(bstack11ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨ⁛"), bstack11ll_opy_ (u"ࠪࠫ⁜")).lower() or caps.get(bstack11ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪ⁝"), bstack11ll_opy_ (u"ࠬ࠭⁞")).lower())
        if bstack1l111ll1111_opy_ == bstack11ll_opy_ (u"࠭ࡩࡰࡵࠪ "):
            return True
        if bstack1l111ll1111_opy_ == bstack11ll_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࠨ⁠"):
            bstack1l111l1l111_opy_ = str(float(caps.get(bstack11ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ⁡")) or bstack1llll1l1l1l1_opy_.get(bstack11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁢"), {}).get(bstack11ll_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁣"),bstack11ll_opy_ (u"ࠫࠬ⁤"))))
            if bstack1l111ll1111_opy_ == bstack11ll_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩ࠭⁥") and int(bstack1l111l1l111_opy_.split(bstack11ll_opy_ (u"࠭࠮ࠨ⁦"))[0]) < float(bstack11l11lll1ll_opy_):
                logger.warning(str(bstack11l1l111111_opy_))
                return False
            return True
        bstack1l111l11lll_opy_ = caps.get(bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁧"), {}).get(bstack11ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ⁨"), caps.get(bstack11ll_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ⁩"), bstack11ll_opy_ (u"ࠪࠫ⁪")))
        if bstack1l111l11lll_opy_:
            logger.warning(bstack11ll_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡉ࡫ࡳ࡬ࡶࡲࡴࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣ⁫"))
            return False
        browser = caps.get(bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ⁬"), bstack11ll_opy_ (u"࠭ࠧ⁭")).lower() or bstack1llll1l1l1l1_opy_.get(bstack11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ⁮"), bstack11ll_opy_ (u"ࠨࠩ⁯")).lower()
        if browser != bstack11ll_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩ⁰"):
            logger.warning(bstack11ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨⁱ"))
            return False
        browser_version = caps.get(bstack11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁲")) or caps.get(bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ⁳")) or bstack1llll1l1l1l1_opy_.get(bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⁴")) or bstack1llll1l1l1l1_opy_.get(bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁵"), {}).get(bstack11ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⁶")) or bstack1llll1l1l1l1_opy_.get(bstack11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁷"), {}).get(bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ⁸"))
        bstack1l1111lll11_opy_ = bstack1llll1l1l1ll_opy_.bstack1l11111llll_opy_
        bstack1llll1l1l111_opy_ = False
        if config is not None:
          bstack1llll1l1l111_opy_ = bstack11ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ⁹") in config and str(config[bstack11ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ⁺")]).lower() != bstack11ll_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ⁻")
        if os.environ.get(bstack11ll_opy_ (u"ࠧࡊࡕࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘࡋࡓࡔࡋࡒࡒࠬ⁼"), bstack11ll_opy_ (u"ࠨࠩ⁽")).lower() == bstack11ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⁾") or bstack1llll1l1l111_opy_:
          bstack1l1111lll11_opy_ = bstack1llll1l1l1ll_opy_.bstack1l11111lll1_opy_
        if browser_version and browser_version != bstack11ll_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪⁿ") and int(browser_version.split(bstack11ll_opy_ (u"ࠫ࠳࠭₀"))[0]) <= bstack1l1111lll11_opy_:
          logger.warning(bstack11l1llll_opy_ (u"ࠬࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦࡻ࡮࡫ࡱࡣࡦ࠷࠱ࡺࡡࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࡤࡩࡨࡳࡱࡰࡩࡤࡼࡥࡳࡵ࡬ࡳࡳࢃ࠮ࠨ₁"))
          return False
        if not options:
          bstack1l1111l11ll_opy_ = caps.get(bstack11ll_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ₂")) or bstack1llll1l1l1l1_opy_.get(bstack11ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ₃"), {})
          if bstack11ll_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬ₄") in bstack1l1111l11ll_opy_.get(bstack11ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ₅"), []):
              logger.warning(bstack11ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧ₆"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack11ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨ₇") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l1ll1l11_opy_ = config.get(bstack11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ₈"), {})
    bstack1l1l1ll1l11_opy_[bstack11ll_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠩ₉")] = os.getenv(bstack11ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ₊"))
    bstack111l11l1l1l_opy_ = json.loads(os.getenv(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ₋"), bstack11ll_opy_ (u"ࠩࡾࢁࠬ₌"))).get(bstack11ll_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ₍"))
    if not config[bstack11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭₎")].get(bstack11ll_opy_ (u"ࠧࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ₏")):
      if bstack11ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧₐ") in caps:
        caps[bstack11ll_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨₑ")][bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨₒ")] = bstack1l1l1ll1l11_opy_
        caps[bstack11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪₓ")][bstack11ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪₔ")][bstack11ll_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬₕ")] = bstack111l11l1l1l_opy_
      else:
        caps[bstack11ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫₖ")] = bstack1l1l1ll1l11_opy_
        caps[bstack11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬₗ")][bstack11ll_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨₘ")] = bstack111l11l1l1l_opy_
  except Exception as error:
    logger.debug(bstack11ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡪࡺࡴࡪࡰࡪࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠮ࠡࡇࡵࡶࡴࡸ࠺ࠡࠤₙ") +  str(error))
def bstack1ll11lll1_opy_(driver, bstack1llll1lll11l_opy_):
  try:
    setattr(driver, bstack11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩₚ"), True)
    session = driver.session_id
    if session:
      bstack1llll1l1llll_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1l1llll_opy_ = False
      bstack1llll1l1llll_opy_ = url.scheme in [bstack11ll_opy_ (u"ࠥ࡬ࡹࡺࡰࠣₛ"), bstack11ll_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥₜ")]
      if bstack1llll1l1llll_opy_:
        if bstack1llll1lll11l_opy_:
          logger.info(bstack11ll_opy_ (u"࡙ࠧࡥࡵࡷࡳࠤ࡫ࡵࡲࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡫ࡥࡸࠦࡳࡵࡣࡵࡸࡪࡪ࠮ࠡࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡣࡧࡪ࡭ࡳࠦ࡭ࡰ࡯ࡨࡲࡹࡧࡲࡪ࡮ࡼ࠲ࠧ₝"))
      return bstack1llll1lll11l_opy_
  except Exception as e:
    logger.error(bstack11ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤ₞") + str(e))
    return False
def bstack111ll1l1_opy_(driver, name, path):
  try:
    bstack1l1111l11l1_opy_ = {
        bstack11ll_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧ₟"): threading.current_thread().current_test_uuid,
        bstack11ll_opy_ (u"ࠨࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭₠"): os.environ.get(bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ₡"), bstack11ll_opy_ (u"ࠪࠫ₢")),
        bstack11ll_opy_ (u"ࠫࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠨ₣"): os.environ.get(bstack11ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ₤"), bstack11ll_opy_ (u"࠭ࠧ₥"))
    }
    bstack1ll111l11ll_opy_ = bstack11l1l1ll11_opy_.bstack1ll11l1ll1l_opy_(EVENTS.bstack1111lll11l_opy_.value)
    logger.debug(bstack11ll_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡥࡻ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪ₦"))
    try:
      if (bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ₧"), None) and bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ₨"), None)):
        scripts = {bstack11ll_opy_ (u"ࠪࡷࡨࡧ࡮ࠨ₩"): bstack1l1l1l1l1_opy_.perform_scan}
        bstack1llll1ll1l11_opy_ = json.loads(scripts[bstack11ll_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ₪")].replace(bstack11ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ₫"), bstack11ll_opy_ (u"ࠨࠢ€")))
        bstack1llll1ll1l11_opy_[bstack11ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ₭")][bstack11ll_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨ₮")] = None
        scripts[bstack11ll_opy_ (u"ࠤࡶࡧࡦࡴࠢ₯")] = bstack11ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨ₰") + json.dumps(bstack1llll1ll1l11_opy_)
        bstack1l1l1l1l1_opy_.bstack1l11l11l1_opy_(scripts)
        bstack1l1l1l1l1_opy_.store()
        logger.debug(driver.execute_script(bstack1l1l1l1l1_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1l1l1l1l1_opy_.perform_scan, {bstack11ll_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠦ₱"): name}))
      bstack11l1l1ll11_opy_.end(EVENTS.bstack1111lll11l_opy_.value, bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ₲"), bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ₳"), True, None)
    except Exception as error:
      bstack11l1l1ll11_opy_.end(EVENTS.bstack1111lll11l_opy_.value, bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ₴"), bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ₵"), False, str(error))
    bstack1ll111l11ll_opy_ = bstack11l1l1ll11_opy_.bstack11ll1l11lll_opy_(EVENTS.bstack1l111l11ll1_opy_.value)
    bstack11l1l1ll11_opy_.mark(bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ₶"))
    try:
      if (bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ₷"), None) and bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭₸"), None)):
        scripts = {bstack11ll_opy_ (u"ࠬࡹࡣࡢࡰࠪ₹"): bstack1l1l1l1l1_opy_.perform_scan}
        bstack1llll1ll1l11_opy_ = json.loads(scripts[bstack11ll_opy_ (u"ࠨࡳࡤࡣࡱࠦ₺")].replace(bstack11ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࠥ₻"), bstack11ll_opy_ (u"ࠣࠤ₼")))
        bstack1llll1ll1l11_opy_[bstack11ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ₽")][bstack11ll_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪ₾")] = None
        scripts[bstack11ll_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ₿")] = bstack11ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ⃀") + json.dumps(bstack1llll1ll1l11_opy_)
        bstack1l1l1l1l1_opy_.bstack1l11l11l1_opy_(scripts)
        bstack1l1l1l1l1_opy_.store()
        logger.debug(driver.execute_script(bstack1l1l1l1l1_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1l1l1l1l1_opy_.bstack1lllll11l1ll_opy_, bstack1l1111l11l1_opy_))
      bstack11l1l1ll11_opy_.end(bstack1ll111l11ll_opy_, bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ⃁"), bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ⃂"),True, None)
    except Exception as error:
      bstack11l1l1ll11_opy_.end(bstack1ll111l11ll_opy_, bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ⃃"), bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ⃄"),False, str(error))
    logger.info(bstack11ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨ⃅"))
  except Exception as bstack1l111l11l11_opy_:
    logger.error(bstack11ll_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨ⃆") + str(path) + bstack11ll_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢ⃇") + str(bstack1l111l11l11_opy_))
def bstack1llll1ll1ll1_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack11ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ⃈")) and str(caps.get(bstack11ll_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ⃉"))).lower() == bstack11ll_opy_ (u"ࠣࡣࡱࡨࡷࡵࡩࡥࠤ⃊"):
        bstack1l111l1l111_opy_ = caps.get(bstack11ll_opy_ (u"ࠤࡤࡴࡵ࡯ࡵ࡮࠼ࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ⃋")) or caps.get(bstack11ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ⃌"))
        if bstack1l111l1l111_opy_ and int(str(bstack1l111l1l111_opy_)) < bstack11l11lll1ll_opy_:
            return False
    return True
def bstack1111l1ll1l_opy_(config):
  if bstack11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⃍") in config:
        return config[bstack11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⃎")]
  for platform in config.get(bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⃏"), []):
      if bstack11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃐") in platform:
          return platform[bstack11ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⃑")]
  return None
def bstack1ll1l11ll1_opy_(bstack1l1111ll11_opy_):
  try:
    browser_name = bstack1l1111ll11_opy_[bstack11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨ⃒")]
    browser_version = bstack1l1111ll11_opy_[bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲ⃓ࠬ")]
    chrome_options = bstack1l1111ll11_opy_[bstack11ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡣࡴࡶࡴࡪࡱࡱࡷࠬ⃔")]
    try:
        bstack1llll1lll1ll_opy_ = int(browser_version.split(bstack11ll_opy_ (u"ࠬ࠴ࠧ⃕"))[0])
    except ValueError as e:
        logger.error(bstack11ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡨࡵ࡮ࡷࡧࡵࡸ࡮ࡴࡧࠡࡤࡵࡳࡼࡹࡥࡳࠢࡹࡩࡷࡹࡩࡰࡰࠥ⃖") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack11ll_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ⃗")):
        logger.warning(bstack11ll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱⃘ࠦ"))
        return False
    if bstack1llll1lll1ll_opy_ < bstack1llll1l1l1ll_opy_.bstack1l11111lll1_opy_:
        logger.warning(bstack11l1llll_opy_ (u"ࠩࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡳࠡࡅ࡫ࡶࡴࡳࡥࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡾࡇࡔࡔࡓࡕࡃࡑࡘࡘ࠴ࡍࡊࡐࡌࡑ࡚ࡓ࡟ࡏࡑࡑࡣࡇ࡙ࡔࡂࡅࡎࡣࡎࡔࡆࡓࡃࡢࡅ࠶࠷࡙ࡠࡕࡘࡔࡕࡕࡒࡕࡇࡇࡣࡈࡎࡒࡐࡏࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࢂࠦ࡯ࡳࠢ࡫࡭࡬࡮ࡥࡳ࠰⃙ࠪ"))
        return False
    if chrome_options and any(bstack11ll_opy_ (u"ࠪ࠱࠲࡮ࡥࡢࡦ࡯ࡩࡸࡹ⃚ࠧ") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack11ll_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡰࡰࠣࡰࡪ࡭ࡡࡤࡻࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠤࡘࡽࡩࡵࡥ࡫ࠤࡹࡵࠠ࡯ࡧࡺࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨࠤࡴࡸࠠࡢࡸࡲ࡭ࡩࠦࡵࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠨ⃛"))
        return False
    return True
  except Exception as e:
    logger.error(bstack11ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡤࡪࡨࡧࡰ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡻࡰࡱࡱࡵࡸࠥ࡬࡯ࡳࠢ࡯ࡳࡨࡧ࡬ࠡࡅ࡫ࡶࡴࡳࡥ࠻ࠢࠥ⃜") + str(e))
    return False
def bstack1l1l111111_opy_(bstack1l11ll1111_opy_, config):
    try:
      bstack1l1111l111l_opy_ = bstack11ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⃝") in config and config[bstack11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃞")] == True
      bstack1llll1l1l111_opy_ = bstack11ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ⃟") in config and str(config[bstack11ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭⃠")]).lower() != bstack11ll_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ⃡")
      if not (bstack1l1111l111l_opy_ and (not bstack1ll11llll1_opy_(config) or bstack1llll1l1l111_opy_)):
        return bstack1l11ll1111_opy_
      bstack1llll1l1l11l_opy_ = bstack1l1l1l1l1_opy_.bstack1lllll11l111_opy_
      if bstack1llll1l1l11l_opy_ is None:
        logger.debug(bstack11ll_opy_ (u"ࠦࡌࡵ࡯ࡨ࡮ࡨࠤࡨ࡮ࡲࡰ࡯ࡨࠤࡴࡶࡴࡪࡱࡱࡷࠥࡧࡲࡦࠢࡑࡳࡳ࡫ࠢ⃢"))
        return bstack1l11ll1111_opy_
      bstack1llll1lllll1_opy_ = int(str(bstack1111l1ll1l1_opy_()).split(bstack11ll_opy_ (u"ࠬ࠴ࠧ⃣"))[0])
      logger.debug(bstack11ll_opy_ (u"ࠨࡓࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡧࡩࡹ࡫ࡣࡵࡧࡧ࠾ࠥࠨ⃤") + str(bstack1llll1lllll1_opy_) + bstack11ll_opy_ (u"⃥ࠢࠣ"))
      if bstack1llll1lllll1_opy_ == 3 and isinstance(bstack1l11ll1111_opy_, dict) and bstack11ll_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃦") in bstack1l11ll1111_opy_ and bstack1llll1l1l11l_opy_ is not None:
        if bstack11ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃧") not in bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃨ࠪ")]:
          bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃩")][bstack11ll_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵ⃪ࠪ")] = {}
        if bstack11ll_opy_ (u"࠭ࡡࡳࡩࡶ⃫ࠫ") in bstack1llll1l1l11l_opy_:
          if bstack11ll_opy_ (u"ࠧࡢࡴࡪࡷ⃬ࠬ") not in bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃭")][bstack11ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹ⃮ࠧ")]:
            bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃯ࠪ")][bstack11ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃰")][bstack11ll_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃱")] = []
          for arg in bstack1llll1l1l11l_opy_[bstack11ll_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃲")]:
            if arg not in bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃳")][bstack11ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃴")][bstack11ll_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ⃵")]:
              bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃶")][bstack11ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃷")][bstack11ll_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃸")].append(arg)
        if bstack11ll_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃹") in bstack1llll1l1l11l_opy_:
          if bstack11ll_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃺") not in bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃻")][bstack11ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃼")]:
            bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃽")][bstack11ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃾")][bstack11ll_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃿")] = []
          for ext in bstack1llll1l1l11l_opy_[bstack11ll_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ℀")]:
            if ext not in bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ℁")][bstack11ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ℂ")][bstack11ll_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭℃")]:
              bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ℄")][bstack11ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ℅")][bstack11ll_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ℆")].append(ext)
        if bstack11ll_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬℇ") in bstack1llll1l1l11l_opy_:
          if bstack11ll_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭℈") not in bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ℉")][bstack11ll_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧℊ")]:
            bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪℋ")][bstack11ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩℌ")][bstack11ll_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫℍ")] = {}
          bstack111l1ll1ll1_opy_(bstack1l11ll1111_opy_[bstack11ll_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ℎ")][bstack11ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬℏ")][bstack11ll_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧℐ")],
                    bstack1llll1l1l11l_opy_[bstack11ll_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨℑ")])
        os.environ[bstack11ll_opy_ (u"ࠪࡍࡘࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡇࡖࡗࡎࡕࡎࠨℒ")] = bstack11ll_opy_ (u"ࠫࡹࡸࡵࡦࠩℓ")
        return bstack1l11ll1111_opy_
      else:
        chrome_options = None
        if isinstance(bstack1l11ll1111_opy_, ChromeOptions):
          chrome_options = bstack1l11ll1111_opy_
        elif isinstance(bstack1l11ll1111_opy_, dict):
          for value in bstack1l11ll1111_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack1l11ll1111_opy_, dict):
            bstack1l11ll1111_opy_[bstack11ll_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭℔")] = chrome_options
          else:
            bstack1l11ll1111_opy_ = chrome_options
        if bstack1llll1l1l11l_opy_ is not None:
          if bstack11ll_opy_ (u"࠭ࡡࡳࡩࡶࠫℕ") in bstack1llll1l1l11l_opy_:
                bstack1llll1l1ll11_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1l1l11l_opy_[bstack11ll_opy_ (u"ࠧࡢࡴࡪࡷࠬ№")]
                for arg in new_args:
                    if arg not in bstack1llll1l1ll11_opy_:
                        chrome_options.add_argument(arg)
          if bstack11ll_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ℗") in bstack1llll1l1l11l_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack11ll_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭℘"), [])
                bstack1llll1llllll_opy_ = bstack1llll1l1l11l_opy_[bstack11ll_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧℙ")]
                for extension in bstack1llll1llllll_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack11ll_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪℚ") in bstack1llll1l1l11l_opy_:
                bstack1llll1llll1l_opy_ = chrome_options.experimental_options.get(bstack11ll_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫℛ"), {})
                bstack1llll1l11lll_opy_ = bstack1llll1l1l11l_opy_[bstack11ll_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬℜ")]
                bstack111l1ll1ll1_opy_(bstack1llll1llll1l_opy_, bstack1llll1l11lll_opy_)
                chrome_options.add_experimental_option(bstack11ll_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ℝ"), bstack1llll1llll1l_opy_)
        os.environ[bstack11ll_opy_ (u"ࠨࡋࡖࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡅࡔࡕࡌࡓࡓ࠭℞")] = bstack11ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ℟")
        return bstack1l11ll1111_opy_
    except Exception as e:
      logger.error(bstack11ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡣࡧࡨ࡮ࡴࡧࠡࡰࡲࡲ࠲ࡈࡓࠡ࡫ࡱࡪࡷࡧࠠࡢ࠳࠴ࡽࠥࡩࡨࡳࡱࡰࡩࠥࡵࡰࡵ࡫ࡲࡲࡸࡀࠠࠣ℠") + str(e))
      return bstack1l11ll1111_opy_