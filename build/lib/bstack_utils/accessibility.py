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
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1l11ll1_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l11llll11_opy_ as bstack1llll1l1l1l1_opy_, EVENTS
from bstack_utils.bstack1l1ll1lll1_opy_ import bstack1l1ll1lll1_opy_
from bstack_utils.helper import bstack1ll11lll_opy_, bstack1l1l11ll_opy_, bstack1l11lllll1_opy_, bstack111l1l1111l_opy_, \
  bstack1111ll1l11l_opy_, bstack11l11l1lll_opy_, get_host_info, bstack111l11lll1l_opy_, bstack111ll1l111_opy_, error_handler, bstack111l11l1lll_opy_, bstack111l11l1l1l_opy_, bstack1llll11l_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack11ll1l11l1_opy_ import get_logger
from bstack_utils.bstack111111l1l1_opy_ import bstack1llll1l1111_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack111111l1l1_opy_ = bstack1llll1l1111_opy_()
@error_handler(class_method=False)
def _1llll1l11111_opy_(driver, bstack111l1111_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11l1111_opy_ (u"࠭࡯ࡴࡡࡱࡥࡲ࡫ࠧ’"): caps.get(bstack11l1111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭‚"), None),
        bstack11l1111_opy_ (u"ࠨࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ‛"): bstack111l1111_opy_.get(bstack11l1111_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬ“"), None),
        bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡳࡧ࡭ࡦࠩ”"): caps.get(bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩ„"), None),
        bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ‟"): caps.get(bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ†"), None)
    }
  except Exception as error:
    logger.debug(bstack11l1111_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡪࡺࡡࡪ࡮ࡶࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫ‡") + str(error))
  return response
def on():
    if os.environ.get(bstack11l1111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭•"), None) is None or os.environ[bstack11l1111_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ‣")] == bstack11l1111_opy_ (u"ࠥࡲࡺࡲ࡬ࠣ․"):
        return False
    return True
def bstack1l1llllll_opy_(config):
  return config.get(bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ‥"), False) or any([p.get(bstack11l1111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ…"), False) == True for p in config.get(bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ‧"), [])])
def bstack11lll11lll_opy_(config, bstack11lll1111_opy_):
  try:
    bstack1llll1l11l11_opy_ = config.get(bstack11l1111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ "), False)
    if int(bstack11lll1111_opy_) < len(config.get(bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ "), [])) and config[bstack11l1111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ‪")][bstack11lll1111_opy_]:
      bstack1llll1lll11l_opy_ = config[bstack11l1111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭‫")][bstack11lll1111_opy_].get(bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ‬"), None)
    else:
      bstack1llll1lll11l_opy_ = config.get(bstack11l1111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ‭"), None)
    if bstack1llll1lll11l_opy_ != None:
      bstack1llll1l11l11_opy_ = bstack1llll1lll11l_opy_
    bstack1llll11llll1_opy_ = os.getenv(bstack11l1111_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ‮")) is not None and len(os.getenv(bstack11l1111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ "))) > 0 and os.getenv(bstack11l1111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭‰")) != bstack11l1111_opy_ (u"ࠩࡱࡹࡱࡲࠧ‱")
    return bstack1llll1l11l11_opy_ and bstack1llll11llll1_opy_
  except Exception as error:
    logger.debug(bstack11l1111_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡩࡷ࡯ࡦࡺ࡫ࡱ࡫ࠥࡺࡨࡦࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸࠠ࠻ࠢࠪ′") + str(error))
  return False
def bstack1l11l11ll1_opy_(test_tags):
  bstack1l11111l1ll_opy_ = os.getenv(bstack11l1111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ″"))
  if bstack1l11111l1ll_opy_ is None:
    return True
  bstack1l11111l1ll_opy_ = json.loads(bstack1l11111l1ll_opy_)
  try:
    include_tags = bstack1l11111l1ll_opy_[bstack11l1111_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ‴")] if bstack11l1111_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ‵") in bstack1l11111l1ll_opy_ and isinstance(bstack1l11111l1ll_opy_[bstack11l1111_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ‶")], list) else []
    exclude_tags = bstack1l11111l1ll_opy_[bstack11l1111_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭‷")] if bstack11l1111_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ‸") in bstack1l11111l1ll_opy_ and isinstance(bstack1l11111l1ll_opy_[bstack11l1111_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ‹")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11l1111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡹࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡩࡳࡷࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡢࡦࡨࡲࡶࡪࠦࡳࡤࡣࡱࡲ࡮ࡴࡧ࠯ࠢࡈࡶࡷࡵࡲࠡ࠼ࠣࠦ›") + str(error))
  return False
def bstack1llll1ll1111_opy_(config, frameworkName, bstack1llll1lll111_opy_, bstack1llll1ll11l1_opy_):
  bstack1llll1lll1l1_opy_ = bstack111l1l1111l_opy_(config)
  bstack1llll1l11lll_opy_ = bstack1111ll1l11l_opy_(config)
  if bstack1llll1lll1l1_opy_ is None or bstack1llll1l11lll_opy_ is None:
    logger.error(bstack11l1111_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡳࡷࡱࠤ࡫ࡵࡲࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥࡓࡩࡴࡵ࡬ࡲ࡬ࠦࡡࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡵࡱ࡮ࡩࡳ࠭※"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ‼"), bstack11l1111_opy_ (u"ࠧࡼࡿࠪ‽")))
    data = {
        bstack11l1111_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭‾"): config[bstack11l1111_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ‿")],
        bstack11l1111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭⁀"): config.get(bstack11l1111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ⁁"), os.path.basename(os.getcwd())),
        bstack11l1111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡘ࡮ࡳࡥࠨ⁂"): bstack1ll11lll_opy_(),
        bstack11l1111_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ⁃"): config.get(bstack11l1111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ⁄"), bstack11l1111_opy_ (u"ࠨࠩ⁅")),
        bstack11l1111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ⁆"): {
            bstack11l1111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡔࡡ࡮ࡧࠪ⁇"): frameworkName,
            bstack11l1111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ⁈"): bstack1llll1lll111_opy_,
            bstack11l1111_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩ⁉"): __version__,
            bstack11l1111_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨ⁊"): bstack11l1111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ⁋"),
            bstack11l1111_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ⁌"): bstack11l1111_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫ⁍"),
            bstack11l1111_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ⁎"): bstack1llll1ll11l1_opy_
        },
        bstack11l1111_opy_ (u"ࠫࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭⁏"): settings,
        bstack11l1111_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡉ࡯࡯ࡶࡵࡳࡱ࠭⁐"): bstack111l11lll1l_opy_(),
        bstack11l1111_opy_ (u"࠭ࡣࡪࡋࡱࡪࡴ࠭⁑"): bstack11l11l1lll_opy_(),
        bstack11l1111_opy_ (u"ࠧࡩࡱࡶࡸࡎࡴࡦࡰࠩ⁒"): get_host_info(),
        bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ⁓"): bstack1l11lllll1_opy_(config)
    }
    headers = {
        bstack11l1111_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ⁔"): bstack11l1111_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭⁕"),
    }
    config = {
        bstack11l1111_opy_ (u"ࠫࡦࡻࡴࡩࠩ⁖"): (bstack1llll1lll1l1_opy_, bstack1llll1l11lll_opy_),
        bstack11l1111_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭⁗"): headers
    }
    response = bstack111ll1l111_opy_(bstack11l1111_opy_ (u"࠭ࡐࡐࡕࡗࠫ⁘"), bstack1llll1l1l1l1_opy_ + bstack11l1111_opy_ (u"ࠧ࠰ࡸ࠵࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹࠧ⁙"), data, config)
    bstack1llll1l1111l_opy_ = response.json()
    if bstack1llll1l1111l_opy_[bstack11l1111_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ⁚")]:
      parsed = json.loads(os.getenv(bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ⁛"), bstack11l1111_opy_ (u"ࠪࡿࢂ࠭⁜")))
      parsed[bstack11l1111_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁝")] = bstack1llll1l1111l_opy_[bstack11l1111_opy_ (u"ࠬࡪࡡࡵࡣࠪ⁞")][bstack11l1111_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ ")]
      os.environ[bstack11l1111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ⁠")] = json.dumps(parsed)
      bstack1l1ll1lll1_opy_.bstack1l11lll1l_opy_(bstack1llll1l1111l_opy_[bstack11l1111_opy_ (u"ࠨࡦࡤࡸࡦ࠭⁡")][bstack11l1111_opy_ (u"ࠩࡶࡧࡷ࡯ࡰࡵࡵࠪ⁢")])
      bstack1l1ll1lll1_opy_.bstack1llll1llllll_opy_(bstack1llll1l1111l_opy_[bstack11l1111_opy_ (u"ࠪࡨࡦࡺࡡࠨ⁣")][bstack11l1111_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭⁤")])
      bstack1l1ll1lll1_opy_.store()
      return bstack1llll1l1111l_opy_[bstack11l1111_opy_ (u"ࠬࡪࡡࡵࡣࠪ⁥")][bstack11l1111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࡚࡯࡬ࡧࡱࠫ⁦")], bstack1llll1l1111l_opy_[bstack11l1111_opy_ (u"ࠧࡥࡣࡷࡥࠬ⁧")][bstack11l1111_opy_ (u"ࠨ࡫ࡧࠫ⁨")]
    else:
      logger.error(bstack11l1111_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡷࡻ࡮࡯࡫ࡱ࡫ࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠪ⁩") + bstack1llll1l1111l_opy_[bstack11l1111_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⁪")])
      if bstack1llll1l1111l_opy_[bstack11l1111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⁫")] == bstack11l1111_opy_ (u"ࠬࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡰࡢࡵࡶࡩࡩ࠴ࠧ⁬"):
        for bstack1llll1ll1lll_opy_ in bstack1llll1l1111l_opy_[bstack11l1111_opy_ (u"࠭ࡥࡳࡴࡲࡶࡸ࠭⁭")]:
          logger.error(bstack1llll1ll1lll_opy_[bstack11l1111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⁮")])
      return None, None
  except Exception as error:
    logger.error(bstack11l1111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠤ⁯") +  str(error))
    return None, None
def bstack1llll1l1llll_opy_():
  if os.getenv(bstack11l1111_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ⁰")) is None:
    return {
        bstack11l1111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪⁱ"): bstack11l1111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ⁲"),
        bstack11l1111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⁳"): bstack11l1111_opy_ (u"࠭ࡂࡶ࡫࡯ࡨࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠࡩࡣࡧࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠬ⁴")
    }
  data = {bstack11l1111_opy_ (u"ࠧࡦࡰࡧࡘ࡮ࡳࡥࠨ⁵"): bstack1ll11lll_opy_()}
  headers = {
      bstack11l1111_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨ⁶"): bstack11l1111_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࠪ⁷") + os.getenv(bstack11l1111_opy_ (u"ࠥࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠣ⁸")),
      bstack11l1111_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ⁹"): bstack11l1111_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ⁺")
  }
  response = bstack111ll1l111_opy_(bstack11l1111_opy_ (u"࠭ࡐࡖࡖࠪ⁻"), bstack1llll1l1l1l1_opy_ + bstack11l1111_opy_ (u"ࠧ࠰ࡶࡨࡷࡹࡥࡲࡶࡰࡶ࠳ࡸࡺ࡯ࡱࠩ⁼"), data, { bstack11l1111_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ⁽"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11l1111_opy_ (u"ࠤࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࡚ࠥࡥࡴࡶࠣࡖࡺࡴࠠ࡮ࡣࡵ࡯ࡪࡪࠠࡢࡵࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠦࡡࡵࠢࠥ⁾") + bstack1l1l11ll_opy_().isoformat() + bstack11l1111_opy_ (u"ࠪ࡞ࠬⁿ"))
      return {bstack11l1111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ₀"): bstack11l1111_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭₁"), bstack11l1111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ₂"): bstack11l1111_opy_ (u"ࠧࠨ₃")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11l1111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡱࡦࡸ࡫ࡪࡰࡪࠤࡨࡵ࡭ࡱ࡮ࡨࡸ࡮ࡵ࡮ࠡࡱࡩࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯࠼ࠣࠦ₄") + str(error))
    return {
        bstack11l1111_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ₅"): bstack11l1111_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ₆"),
        bstack11l1111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ₇"): str(error)
    }
def bstack1llll1l111ll_opy_(bstack1llll1ll1l1l_opy_):
    return re.match(bstack11l1111_opy_ (u"ࡷ࠭࡞࡝ࡦ࠮ࠬࡡ࠴࡜ࡥ࠭ࠬࡃࠩ࠭₈"), bstack1llll1ll1l1l_opy_.strip()) is not None
def bstack1l1l1l1l1l_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1l1l1ll_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1l1l1ll_opy_ = desired_capabilities
        else:
          bstack1llll1l1l1ll_opy_ = {}
        bstack1l1111lll1l_opy_ = (bstack1llll1l1l1ll_opy_.get(bstack11l1111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬ₉"), bstack11l1111_opy_ (u"ࠧࠨ₊")).lower() or caps.get(bstack11l1111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧ₋"), bstack11l1111_opy_ (u"ࠩࠪ₌")).lower())
        if bstack1l1111lll1l_opy_ == bstack11l1111_opy_ (u"ࠪ࡭ࡴࡹࠧ₍"):
            return True
        if bstack1l1111lll1l_opy_ == bstack11l1111_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࠬ₎"):
            bstack1l1111l111l_opy_ = str(float(caps.get(bstack11l1111_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠧ₏")) or bstack1llll1l1l1ll_opy_.get(bstack11l1111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧₐ"), {}).get(bstack11l1111_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪₑ"),bstack11l1111_opy_ (u"ࠨࠩₒ"))))
            if bstack1l1111lll1l_opy_ == bstack11l1111_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࠪₓ") and int(bstack1l1111l111l_opy_.split(bstack11l1111_opy_ (u"ࠪ࠲ࠬₔ"))[0]) < float(bstack11l11ll1l11_opy_):
                logger.warning(str(bstack11l1l11l111_opy_))
                return False
            return True
        bstack1l1111llll1_opy_ = caps.get(bstack11l1111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬₕ"), {}).get(bstack11l1111_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩₖ"), caps.get(bstack11l1111_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ₗ"), bstack11l1111_opy_ (u"ࠧࠨₘ")))
        if bstack1l1111llll1_opy_:
            logger.warning(bstack11l1111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡆࡨࡷࡰࡺ࡯ࡱࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧₙ"))
            return False
        browser = caps.get(bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧₚ"), bstack11l1111_opy_ (u"ࠪࠫₛ")).lower() or bstack1llll1l1l1ll_opy_.get(bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩₜ"), bstack11l1111_opy_ (u"ࠬ࠭₝")).lower()
        if browser != bstack11l1111_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭₞"):
            logger.warning(bstack11l1111_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥ₟"))
            return False
        browser_version = caps.get(bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ₠")) or caps.get(bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ₡")) or bstack1llll1l1l1ll_opy_.get(bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ₢")) or bstack1llll1l1l1ll_opy_.get(bstack11l1111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ₣"), {}).get(bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭₤")) or bstack1llll1l1l1ll_opy_.get(bstack11l1111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ₥"), {}).get(bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ₦"))
        bstack1l1111ll1l1_opy_ = bstack1llll1l11ll1_opy_.bstack1l11111l11l_opy_
        bstack1llll1l1lll1_opy_ = False
        if config is not None:
          bstack1llll1l1lll1_opy_ = bstack11l1111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ₧") in config and str(config[bstack11l1111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭₨")]).lower() != bstack11l1111_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ₩")
        if os.environ.get(bstack11l1111_opy_ (u"ࠫࡎ࡙࡟ࡏࡑࡑࡣࡇ࡙ࡔࡂࡅࡎࡣࡎࡔࡆࡓࡃࡢࡅ࠶࠷࡙ࡠࡕࡈࡗࡘࡏࡏࡏࠩ₪"), bstack11l1111_opy_ (u"ࠬ࠭₫")).lower() == bstack11l1111_opy_ (u"࠭ࡴࡳࡷࡨࠫ€") or bstack1llll1l1lll1_opy_:
          bstack1l1111ll1l1_opy_ = bstack1llll1l11ll1_opy_.bstack1l111l11lll_opy_
        if browser_version and browser_version != bstack11l1111_opy_ (u"ࠧ࡭ࡣࡷࡩࡸࡺࠧ₭") and int(browser_version.split(bstack11l1111_opy_ (u"ࠨ࠰ࠪ₮"))[0]) <= bstack1l1111ll1l1_opy_:
          logger.warning(bstack1lll1ll1111_opy_ (u"ࠩࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࠣࡺࡪࡸࡳࡪࡱࡱࠤ࡬ࡸࡥࡢࡶࡨࡶࠥࡺࡨࡢࡰࠣࡿࡲ࡯࡮ࡠࡣ࠴࠵ࡾࡥࡳࡶࡲࡳࡳࡷࡺࡥࡥࡡࡦ࡬ࡷࡵ࡭ࡦࡡࡹࡩࡷࡹࡩࡰࡰࢀ࠲ࠬ₯"))
          return False
        if not options:
          bstack1l1111lll11_opy_ = caps.get(bstack11l1111_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ₰")) or bstack1llll1l1l1ll_opy_.get(bstack11l1111_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ₱"), {})
          if bstack11l1111_opy_ (u"ࠬ࠳࠭ࡩࡧࡤࡨࡱ࡫ࡳࡴࠩ₲") in bstack1l1111lll11_opy_.get(bstack11l1111_opy_ (u"࠭ࡡࡳࡩࡶࠫ₳"), []):
              logger.warning(bstack11l1111_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡱࡳࡹࠦࡲࡶࡰࠣࡳࡳࠦ࡬ࡦࡩࡤࡧࡾࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠠࡔࡹ࡬ࡸࡨ࡮ࠠࡵࡱࠣࡲࡪࡽࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫ࠠࡰࡴࠣࡥࡻࡵࡩࡥࠢࡸࡷ࡮ࡴࡧࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠤ₴"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack11l1111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡷࡣ࡯࡭ࡩࡧࡴࡦࠢࡤ࠵࠶ࡿࠠࡴࡷࡳࡴࡴࡸࡴࠡ࠼ࠥ₵") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l11ll1l11l_opy_ = config.get(bstack11l1111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ₶"), {})
    bstack1l11ll1l11l_opy_[bstack11l1111_opy_ (u"ࠪࡥࡺࡺࡨࡕࡱ࡮ࡩࡳ࠭₷")] = os.getenv(bstack11l1111_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ₸"))
    bstack1111ll1ll1l_opy_ = json.loads(os.getenv(bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭₹"), bstack11l1111_opy_ (u"࠭ࡻࡾࠩ₺"))).get(bstack11l1111_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ₻"))
    if not config[bstack11l1111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡐࡳࡱࡧࡹࡨࡺࡍࡢࡲࠪ₼")].get(bstack11l1111_opy_ (u"ࠤࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠣ₽")):
      if bstack11l1111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ₾") in caps:
        caps[bstack11l1111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ₿")][bstack11l1111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ⃀")] = bstack1l11ll1l11l_opy_
        caps[bstack11l1111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ⃁")][bstack11l1111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ⃂")][bstack11l1111_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⃃")] = bstack1111ll1ll1l_opy_
      else:
        caps[bstack11l1111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ⃄")] = bstack1l11ll1l11l_opy_
        caps[bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃅")][bstack11l1111_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⃆")] = bstack1111ll1ll1l_opy_
  except Exception as error:
    logger.debug(bstack11l1111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶ࠲ࠥࡋࡲࡳࡱࡵ࠾ࠥࠨ⃇") +  str(error))
def bstack111111ll11_opy_(driver, bstack1llll1l1ll11_opy_):
  try:
    setattr(driver, bstack11l1111_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡇ࠱࠲ࡻࡖ࡬ࡴࡻ࡬ࡥࡕࡦࡥࡳ࠭⃈"), True)
    session = driver.session_id
    if session:
      bstack1llll1ll1l11_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1ll1l11_opy_ = False
      bstack1llll1ll1l11_opy_ = url.scheme in [bstack11l1111_opy_ (u"ࠢࡩࡶࡷࡴࠧ⃉"), bstack11l1111_opy_ (u"ࠣࡪࡷࡸࡵࡹࠢ⃊")]
      if bstack1llll1ll1l11_opy_:
        if bstack1llll1l1ll11_opy_:
          logger.info(bstack11l1111_opy_ (u"ࠤࡖࡩࡹࡻࡰࠡࡨࡲࡶࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡨࡢࡵࠣࡷࡹࡧࡲࡵࡧࡧ࠲ࠥࡇࡵࡵࡱࡰࡥࡹ࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡧ࡫ࡧࡪࡰࠣࡱࡴࡳࡥ࡯ࡶࡤࡶ࡮ࡲࡹ࠯ࠤ⃋"))
      return bstack1llll1l1ll11_opy_
  except Exception as e:
    logger.error(bstack11l1111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡦࡸࡴࡪࡰࡪࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨ⃌") + str(e))
    return False
def bstack1lll1l111_opy_(driver, name, path):
  try:
    bstack1l111111l1l_opy_ = {
        bstack11l1111_opy_ (u"ࠫࡹ࡮ࡔࡦࡵࡷࡖࡺࡴࡕࡶ࡫ࡧࠫ⃍"): threading.current_thread().current_test_uuid,
        bstack11l1111_opy_ (u"ࠬࡺࡨࡃࡷ࡬ࡰࡩ࡛ࡵࡪࡦࠪ⃎"): os.environ.get(bstack11l1111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫ⃏"), bstack11l1111_opy_ (u"ࠧࠨ⃐")),
        bstack11l1111_opy_ (u"ࠨࡶ࡫ࡎࡼࡺࡔࡰ࡭ࡨࡲࠬ⃑"): os.environ.get(bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡍ⃒࡛࡙࠭"), bstack11l1111_opy_ (u"⃓ࠪࠫ"))
    }
    bstack1l1llll111l_opy_ = bstack111111l1l1_opy_.bstack1ll1111l111_opy_(EVENTS.bstack1ll1l1l111_opy_.value)
    logger.debug(bstack11l1111_opy_ (u"ࠫࡕ࡫ࡲࡧࡱࡵࡱ࡮ࡴࡧࠡࡵࡦࡥࡳࠦࡢࡦࡨࡲࡶࡪࠦࡳࡢࡸ࡬ࡲ࡬ࠦࡲࡦࡵࡸࡰࡹࡹࠧ⃔"))
    try:
      if (bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ⃕"), None) and bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ⃖"), None)):
        scripts = {bstack11l1111_opy_ (u"ࠧࡴࡥࡤࡲࠬ⃗"): bstack1l1ll1lll1_opy_.perform_scan}
        bstack1llll1l111l1_opy_ = json.loads(scripts[bstack11l1111_opy_ (u"ࠣࡵࡦࡥࡳࠨ⃘")].replace(bstack11l1111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤ⃙ࠧ"), bstack11l1111_opy_ (u"⃚ࠥࠦ")))
        bstack1llll1l111l1_opy_[bstack11l1111_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ⃛")][bstack11l1111_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࠬ⃜")] = None
        scripts[bstack11l1111_opy_ (u"ࠨࡳࡤࡣࡱࠦ⃝")] = bstack11l1111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࠥ⃞") + json.dumps(bstack1llll1l111l1_opy_)
        bstack1l1ll1lll1_opy_.bstack1l11lll1l_opy_(scripts)
        bstack1l1ll1lll1_opy_.store()
        logger.debug(driver.execute_script(bstack1l1ll1lll1_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1l1ll1lll1_opy_.perform_scan, {bstack11l1111_opy_ (u"ࠣ࡯ࡨࡸ࡭ࡵࡤࠣ⃟"): name}))
      bstack111111l1l1_opy_.end(EVENTS.bstack1ll1l1l111_opy_.value, bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ⃠"), bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣ⃡"), True, None)
    except Exception as error:
      bstack111111l1l1_opy_.end(EVENTS.bstack1ll1l1l111_opy_.value, bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦ⃢"), bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠧࡀࡥ࡯ࡦࠥ⃣"), False, str(error))
    bstack1l1llll111l_opy_ = bstack111111l1l1_opy_.bstack11ll11lllll_opy_(EVENTS.bstack1l11111ll11_opy_.value)
    bstack111111l1l1_opy_.mark(bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ⃤"))
    try:
      if (bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺ⃥ࠧ"), None) and bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯⃦ࠪ"), None)):
        scripts = {bstack11l1111_opy_ (u"ࠩࡶࡧࡦࡴࠧ⃧"): bstack1l1ll1lll1_opy_.perform_scan}
        bstack1llll1l111l1_opy_ = json.loads(scripts[bstack11l1111_opy_ (u"ࠥࡷࡨࡧ࡮⃨ࠣ")].replace(bstack11l1111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࠢ⃩"), bstack11l1111_opy_ (u"ࠧࠨ⃪")))
        bstack1llll1l111l1_opy_[bstack11l1111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴ⃫ࠩ")][bstack11l1111_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪ⃬ࠧ")] = None
        scripts[bstack11l1111_opy_ (u"ࠣࡵࡦࡥࡳࠨ⃭")] = bstack11l1111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤ⃮ࠧ") + json.dumps(bstack1llll1l111l1_opy_)
        bstack1l1ll1lll1_opy_.bstack1l11lll1l_opy_(scripts)
        bstack1l1ll1lll1_opy_.store()
        logger.debug(driver.execute_script(bstack1l1ll1lll1_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1l1ll1lll1_opy_.bstack1llll1llll1l_opy_, bstack1l111111l1l_opy_))
      bstack111111l1l1_opy_.end(bstack1l1llll111l_opy_, bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶ⃯ࠥ"), bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠦ࠿࡫࡮ࡥࠤ⃰"),True, None)
    except Exception as error:
      bstack111111l1l1_opy_.end(bstack1l1llll111l_opy_, bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ⃱"), bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ⃲"),False, str(error))
    logger.info(bstack11l1111_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡨࡢࡵࠣࡩࡳࡪࡥࡥ࠰ࠥ⃳"))
  except Exception as bstack1l1111lllll_opy_:
    logger.error(bstack11l1111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡴࡨࡷࡺࡲࡴࡴࠢࡦࡳࡺࡲࡤࠡࡰࡲࡸࠥࡨࡥࠡࡲࡵࡳࡨ࡫ࡳࡴࡧࡧࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥ࠻ࠢࠥ⃴") + str(path) + bstack11l1111_opy_ (u"ࠤࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠦ⃵") + str(bstack1l1111lllll_opy_))
def bstack1llll1ll1ll1_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack11l1111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤ⃶")) and str(caps.get(bstack11l1111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥ⃷"))).lower() == bstack11l1111_opy_ (u"ࠧࡧ࡮ࡥࡴࡲ࡭ࡩࠨ⃸"):
        bstack1l1111l111l_opy_ = caps.get(bstack11l1111_opy_ (u"ࠨࡡࡱࡲ࡬ࡹࡲࡀࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣ⃹")) or caps.get(bstack11l1111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤ⃺"))
        if bstack1l1111l111l_opy_ and int(str(bstack1l1111l111l_opy_)) < bstack11l11ll1l11_opy_:
            return False
    return True
def bstack11ll111ll1_opy_(config):
  if bstack11l1111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⃻") in config:
        return config[bstack11l1111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⃼")]
  for platform in config.get(bstack11l1111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭⃽"), []):
      if bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⃾") in platform:
          return platform[bstack11l1111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⃿")]
  return None
def bstack1l1lll1l11_opy_(bstack111ll1ll1_opy_):
  try:
    browser_name = bstack111ll1ll1_opy_[bstack11l1111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬ℀")]
    browser_version = bstack111ll1ll1_opy_[bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ℁")]
    chrome_options = bstack111ll1ll1_opy_[bstack11l1111_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࡠࡱࡳࡸ࡮ࡵ࡮ࡴࠩℂ")]
    try:
        bstack1llll1ll111l_opy_ = int(browser_version.split(bstack11l1111_opy_ (u"ࠩ࠱ࠫ℃"))[0])
    except ValueError as e:
        logger.error(bstack11l1111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡥࡲࡲࡻ࡫ࡲࡵ࡫ࡱ࡫ࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠢ℄") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack11l1111_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫ℅")):
        logger.warning(bstack11l1111_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣ℆"))
        return False
    if bstack1llll1ll111l_opy_ < bstack1llll1l11ll1_opy_.bstack1l111l11lll_opy_:
        logger.warning(bstack1lll1ll1111_opy_ (u"࠭ࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡶࡪࡷࡵࡪࡴࡨࡷࠥࡉࡨࡳࡱࡰࡩࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡻࡄࡑࡑࡗ࡙ࡇࡎࡕࡕ࠱ࡑࡎࡔࡉࡎࡗࡐࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡕࡑࡒࡒࡖ࡙ࡋࡄࡠࡅࡋࡖࡔࡓࡅࡠࡘࡈࡖࡘࡏࡏࡏࡿࠣࡳࡷࠦࡨࡪࡩ࡫ࡩࡷ࠴ࠧℇ"))
        return False
    if chrome_options and any(bstack11l1111_opy_ (u"ࠧ࠮࠯࡫ࡩࡦࡪ࡬ࡦࡵࡶࠫ℈") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack11l1111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥ℉"))
        return False
    return True
  except Exception as e:
    logger.error(bstack11l1111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡨ࡮ࡥࡤ࡭࡬ࡲ࡬ࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡵࡸࡴࡵࡵࡲࡵࠢࡩࡳࡷࠦ࡬ࡰࡥࡤࡰࠥࡉࡨࡳࡱࡰࡩ࠿ࠦࠢℊ") + str(e))
    return False
def bstack1l1lll1111_opy_(bstack1l1l111ll_opy_, config):
    try:
      bstack1l111l1111l_opy_ = bstack11l1111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪℋ") in config and config[bstack11l1111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫℌ")] == True
      bstack1llll1l1lll1_opy_ = bstack11l1111_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩℍ") in config and str(config[bstack11l1111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪℎ")]).lower() != bstack11l1111_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ℏ")
      if not (bstack1l111l1111l_opy_ and (not bstack1l11lllll1_opy_(config) or bstack1llll1l1lll1_opy_)):
        return bstack1l1l111ll_opy_
      bstack1llll1l11l1l_opy_ = bstack1l1ll1lll1_opy_.bstack1lllll11111l_opy_
      if bstack1llll1l11l1l_opy_ is None:
        logger.debug(bstack11l1111_opy_ (u"ࠣࡉࡲࡳ࡬ࡲࡥࠡࡥ࡫ࡶࡴࡳࡥࠡࡱࡳࡸ࡮ࡵ࡮ࡴࠢࡤࡶࡪࠦࡎࡰࡰࡨࠦℐ"))
        return bstack1l1l111ll_opy_
      bstack1llll1l1ll1l_opy_ = int(str(bstack111l11l1l1l_opy_()).split(bstack11l1111_opy_ (u"ࠩ࠱ࠫℑ"))[0])
      logger.debug(bstack11l1111_opy_ (u"ࠥࡗࡪࡲࡥ࡯࡫ࡸࡱࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡤࡦࡶࡨࡧࡹ࡫ࡤ࠻ࠢࠥℒ") + str(bstack1llll1l1ll1l_opy_) + bstack11l1111_opy_ (u"ࠦࠧℓ"))
      if bstack1llll1l1ll1l_opy_ == 3 and isinstance(bstack1l1l111ll_opy_, dict) and bstack11l1111_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ℔") in bstack1l1l111ll_opy_ and bstack1llll1l11l1l_opy_ is not None:
        if bstack11l1111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫℕ") not in bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ№")]:
          bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ℗")][bstack11l1111_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ℘")] = {}
        if bstack11l1111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨℙ") in bstack1llll1l11l1l_opy_:
          if bstack11l1111_opy_ (u"ࠫࡦࡸࡧࡴࠩℚ") not in bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬℛ")][bstack11l1111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫℜ")]:
            bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧℝ")][bstack11l1111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭℞")][bstack11l1111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ℟")] = []
          for arg in bstack1llll1l11l1l_opy_[bstack11l1111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ℠")]:
            if arg not in bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ℡")][bstack11l1111_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ™")][bstack11l1111_opy_ (u"࠭ࡡࡳࡩࡶࠫ℣")]:
              bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧℤ")][bstack11l1111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭℥")][bstack11l1111_opy_ (u"ࠩࡤࡶ࡬ࡹࠧΩ")].append(arg)
        if bstack11l1111_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ℧") in bstack1llll1l11l1l_opy_:
          if bstack11l1111_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨℨ") not in bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ℩")][bstack11l1111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫK")]:
            bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧÅ")][bstack11l1111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ℬ")][bstack11l1111_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ℭ")] = []
          for ext in bstack1llll1l11l1l_opy_[bstack11l1111_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ℮")]:
            if ext not in bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫℯ")][bstack11l1111_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪℰ")][bstack11l1111_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪℱ")]:
              bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧℲ")][bstack11l1111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ℳ")][bstack11l1111_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ℴ")].append(ext)
        if bstack11l1111_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩℵ") in bstack1llll1l11l1l_opy_:
          if bstack11l1111_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪℶ") not in bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬℷ")][bstack11l1111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫℸ")]:
            bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧℹ")][bstack11l1111_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭℺")][bstack11l1111_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ℻")] = {}
          bstack111l11l1lll_opy_(bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪℼ")][bstack11l1111_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩℽ")][bstack11l1111_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫℾ")],
                    bstack1llll1l11l1l_opy_[bstack11l1111_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬℿ")])
        os.environ[bstack11l1111_opy_ (u"ࠧࡊࡕࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘࡋࡓࡔࡋࡒࡒࠬ⅀")] = bstack11l1111_opy_ (u"ࠨࡶࡵࡹࡪ࠭⅁")
        return bstack1l1l111ll_opy_
      else:
        chrome_options = None
        if isinstance(bstack1l1l111ll_opy_, ChromeOptions):
          chrome_options = bstack1l1l111ll_opy_
        elif isinstance(bstack1l1l111ll_opy_, dict):
          for value in bstack1l1l111ll_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack1l1l111ll_opy_, dict):
            bstack1l1l111ll_opy_[bstack11l1111_opy_ (u"ࠩࡲࡴࡹ࡯࡯࡯ࡵࠪ⅂")] = chrome_options
          else:
            bstack1l1l111ll_opy_ = chrome_options
        if bstack1llll1l11l1l_opy_ is not None:
          if bstack11l1111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ⅃") in bstack1llll1l11l1l_opy_:
                bstack1llll1l1l11l_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1l11l1l_opy_[bstack11l1111_opy_ (u"ࠫࡦࡸࡧࡴࠩ⅄")]
                for arg in new_args:
                    if arg not in bstack1llll1l1l11l_opy_:
                        chrome_options.add_argument(arg)
          if bstack11l1111_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩⅅ") in bstack1llll1l11l1l_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack11l1111_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪⅆ"), [])
                bstack1llll1l1l111_opy_ = bstack1llll1l11l1l_opy_[bstack11l1111_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫⅇ")]
                for extension in bstack1llll1l1l111_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack11l1111_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧⅈ") in bstack1llll1l11l1l_opy_:
                bstack1llll1ll11ll_opy_ = chrome_options.experimental_options.get(bstack11l1111_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨⅉ"), {})
                bstack1llll11lllll_opy_ = bstack1llll1l11l1l_opy_[bstack11l1111_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ⅊")]
                bstack111l11l1lll_opy_(bstack1llll1ll11ll_opy_, bstack1llll11lllll_opy_)
                chrome_options.add_experimental_option(bstack11l1111_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⅋"), bstack1llll1ll11ll_opy_)
        os.environ[bstack11l1111_opy_ (u"ࠬࡏࡓࡠࡐࡒࡒࡤࡈࡓࡕࡃࡆࡏࡤࡏࡎࡇࡔࡄࡣࡆ࠷࠱࡚ࡡࡖࡉࡘ࡙ࡉࡐࡐࠪ⅌")] = bstack11l1111_opy_ (u"࠭ࡴࡳࡷࡨࠫ⅍")
        return bstack1l1l111ll_opy_
    except Exception as e:
      logger.error(bstack11l1111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡧࡤࡥ࡫ࡱ࡫ࠥࡴ࡯࡯࠯ࡅࡗࠥ࡯࡮ࡧࡴࡤࠤࡦ࠷࠱ࡺࠢࡦ࡬ࡷࡵ࡭ࡦࠢࡲࡴࡹ࡯࡯࡯ࡵ࠽ࠤࠧⅎ") + str(e))
      return bstack1l1l111ll_opy_