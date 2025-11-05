# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll11lllll_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l11ll1111_opy_ as bstack1llll1lll1ll_opy_, EVENTS
from bstack_utils.bstack11l1lll1l_opy_ import bstack11l1lll1l_opy_
from bstack_utils.helper import bstack1l1lll11_opy_, bstack1lll11ll_opy_, bstack1l1lll1ll_opy_, bstack111l1l1111l_opy_, \
  bstack11111llllll_opy_, bstack111l1ll11_opy_, get_host_info, bstack1111l11l1ll_opy_, bstack1111ll1lll_opy_, error_handler, bstack111l111l111_opy_, bstack1111l1l1l11_opy_, bstack1lll1lll_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack111111l11l_opy_ import get_logger
from bstack_utils.bstack1ll11111ll_opy_ import bstack1llll1ll1l1_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack1ll11111ll_opy_ = bstack1llll1ll1l1_opy_()
@error_handler(class_method=False)
def _1llll1l1ll11_opy_(driver, bstack111l1l1l_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11111_opy_ (u"ࠧࡰࡵࡢࡲࡦࡳࡥࠨ‚"): caps.get(bstack11111_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧ‛"), None),
        bstack11111_opy_ (u"ࠩࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭“"): bstack111l1l1l_opy_.get(bstack11111_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭”"), None),
        bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪ„"): caps.get(bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ‟"), None),
        bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ†"): caps.get(bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ‡"), None)
    }
  except Exception as error:
    logger.debug(bstack11111_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢ࠽ࠤࠬ•") + str(error))
  return response
def on():
    if os.environ.get(bstack11111_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ‣"), None) is None or os.environ[bstack11111_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ․")] == bstack11111_opy_ (u"ࠦࡳࡻ࡬࡭ࠤ‥"):
        return False
    return True
def bstack111111l1l1_opy_(config):
  return config.get(bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ…"), False) or any([p.get(bstack11111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭‧"), False) == True for p in config.get(bstack11111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ "), [])])
def bstack1111ll1l1l_opy_(config, bstack11ll11lll_opy_):
  try:
    bstack1llll1ll1ll1_opy_ = config.get(bstack11111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ "), False)
    if int(bstack11ll11lll_opy_) < len(config.get(bstack11111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ‪"), [])) and config[bstack11111_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭‫")][bstack11ll11lll_opy_]:
      bstack1llll1l111l1_opy_ = config[bstack11111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ‬")][bstack11ll11lll_opy_].get(bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ‭"), None)
    else:
      bstack1llll1l111l1_opy_ = config.get(bstack11111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭‮"), None)
    if bstack1llll1l111l1_opy_ != None:
      bstack1llll1ll1ll1_opy_ = bstack1llll1l111l1_opy_
    bstack1llll1l11ll1_opy_ = os.getenv(bstack11111_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ ")) is not None and len(os.getenv(bstack11111_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭‰"))) > 0 and os.getenv(bstack11111_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ‱")) != bstack11111_opy_ (u"ࠪࡲࡺࡲ࡬ࠨ′")
    return bstack1llll1ll1ll1_opy_ and bstack1llll1l11ll1_opy_
  except Exception as error:
    logger.debug(bstack11111_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡪࡸࡩࡧࡻ࡬ࡲ࡬ࠦࡴࡩࡧࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡨࡶࡷࡵࡲࠡ࠼ࠣࠫ″") + str(error))
  return False
def bstack1llll1ll11_opy_(test_tags):
  bstack1l1111ll1l1_opy_ = os.getenv(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭‴"))
  if bstack1l1111ll1l1_opy_ is None:
    return True
  bstack1l1111ll1l1_opy_ = json.loads(bstack1l1111ll1l1_opy_)
  try:
    include_tags = bstack1l1111ll1l1_opy_[bstack11111_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ‵")] if bstack11111_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ‶") in bstack1l1111ll1l1_opy_ and isinstance(bstack1l1111ll1l1_opy_[bstack11111_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭‷")], list) else []
    exclude_tags = bstack1l1111ll1l1_opy_[bstack11111_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ‸")] if bstack11111_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ‹") in bstack1l1111ll1l1_opy_ and isinstance(bstack1l1111ll1l1_opy_[bstack11111_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ›")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡺࡦࡲࡩࡥࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧࠣࡪࡴࡸࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡥࡤࡲࡳ࡯࡮ࡨ࠰ࠣࡉࡷࡸ࡯ࡳࠢ࠽ࠤࠧ※") + str(error))
  return False
def bstack1llll1l111ll_opy_(config, frameworkName, bstack1llll1l1l1ll_opy_, bstack1llll1l11l1l_opy_):
  bstack1llll1ll1lll_opy_ = bstack111l1l1111l_opy_(config)
  bstack1llll1l1llll_opy_ = bstack11111llllll_opy_(config)
  if bstack1llll1ll1lll_opy_ is None or bstack1llll1l1llll_opy_ is None:
    logger.error(bstack11111_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡴࡸࡲࠥ࡬࡯ࡳࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠿ࠦࡍࡪࡵࡶ࡭ࡳ࡭ࠠࡢࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸ࡮ࡵ࡮ࠡࡶࡲ࡯ࡪࡴࠧ‼"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ‽"), bstack11111_opy_ (u"ࠨࡽࢀࠫ‾")))
    data = {
        bstack11111_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ‿"): config[bstack11111_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨ⁀")],
        bstack11111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ⁁"): config.get(bstack11111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ⁂"), os.path.basename(os.getcwd())),
        bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸ࡙࡯࡭ࡦࠩ⁃"): bstack1l1lll11_opy_(),
        bstack11111_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ⁄"): config.get(bstack11111_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ⁅"), bstack11111_opy_ (u"ࠩࠪ⁆")),
        bstack11111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ⁇"): {
            bstack11111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫ⁈"): frameworkName,
            bstack11111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁉"): bstack1llll1l1l1ll_opy_,
            bstack11111_opy_ (u"࠭ࡳࡥ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ⁊"): __version__,
            bstack11111_opy_ (u"ࠧ࡭ࡣࡱ࡫ࡺࡧࡧࡦࠩ⁋"): bstack11111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨ⁌"),
            bstack11111_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ⁍"): bstack11111_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ⁎"),
            bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ⁏"): bstack1llll1l11l1l_opy_
        },
        bstack11111_opy_ (u"ࠬࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠧ⁐"): settings,
        bstack11111_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࡃࡰࡰࡷࡶࡴࡲࠧ⁑"): bstack1111l11l1ll_opy_(),
        bstack11111_opy_ (u"ࠧࡤ࡫ࡌࡲ࡫ࡵࠧ⁒"): bstack111l1ll11_opy_(),
        bstack11111_opy_ (u"ࠨࡪࡲࡷࡹࡏ࡮ࡧࡱࠪ⁓"): get_host_info(),
        bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ⁔"): bstack1l1lll1ll_opy_(config)
    }
    headers = {
        bstack11111_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ⁕"): bstack11111_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ⁖"),
    }
    config = {
        bstack11111_opy_ (u"ࠬࡧࡵࡵࡪࠪ⁗"): (bstack1llll1ll1lll_opy_, bstack1llll1l1llll_opy_),
        bstack11111_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ⁘"): headers
    }
    response = bstack1111ll1lll_opy_(bstack11111_opy_ (u"ࠧࡑࡑࡖࡘࠬ⁙"), bstack1llll1lll1ll_opy_ + bstack11111_opy_ (u"ࠨ࠱ࡹ࠶࠴ࡺࡥࡴࡶࡢࡶࡺࡴࡳࠨ⁚"), data, config)
    bstack1llll1lll111_opy_ = response.json()
    if bstack1llll1lll111_opy_[bstack11111_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ⁛")]:
      parsed = json.loads(os.getenv(bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ⁜"), bstack11111_opy_ (u"ࠫࢀࢃࠧ⁝")))
      parsed[bstack11111_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁞")] = bstack1llll1lll111_opy_[bstack11111_opy_ (u"࠭ࡤࡢࡶࡤࠫ ")][bstack11111_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁠")]
      os.environ[bstack11111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ⁡")] = json.dumps(parsed)
      bstack11l1lll1l_opy_.bstack1l1lll11l_opy_(bstack1llll1lll111_opy_[bstack11111_opy_ (u"ࠩࡧࡥࡹࡧࠧ⁢")][bstack11111_opy_ (u"ࠪࡷࡨࡸࡩࡱࡶࡶࠫ⁣")])
      bstack11l1lll1l_opy_.bstack1lllll11111l_opy_(bstack1llll1lll111_opy_[bstack11111_opy_ (u"ࠫࡩࡧࡴࡢࠩ⁤")][bstack11111_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧ⁥")])
      bstack11l1lll1l_opy_.store()
      return bstack1llll1lll111_opy_[bstack11111_opy_ (u"࠭ࡤࡢࡶࡤࠫ⁦")][bstack11111_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡔࡰ࡭ࡨࡲࠬ⁧")], bstack1llll1lll111_opy_[bstack11111_opy_ (u"ࠨࡦࡤࡸࡦ࠭⁨")][bstack11111_opy_ (u"ࠩ࡬ࡨࠬ⁩")]
    else:
      logger.error(bstack11111_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡸࡵ࡯ࡰ࡬ࡲ࡬ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࠫ⁪") + bstack1llll1lll111_opy_[bstack11111_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ⁫")])
      if bstack1llll1lll111_opy_[bstack11111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⁬")] == bstack11111_opy_ (u"࠭ࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡱࡣࡶࡷࡪࡪ࠮ࠨ⁭"):
        for bstack1llll1l1l11l_opy_ in bstack1llll1lll111_opy_[bstack11111_opy_ (u"ࠧࡦࡴࡵࡳࡷࡹࠧ⁮")]:
          logger.error(bstack1llll1l1l11l_opy_[bstack11111_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⁯")])
      return None, None
  except Exception as error:
    logger.error(bstack11111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤࡷࡻ࡮ࠡࡨࡲࡶࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮࠻ࠢࠥ⁰") +  str(error))
    return None, None
def bstack1llll1ll111l_opy_():
  if os.getenv(bstack11111_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨⁱ")) is None:
    return {
        bstack11111_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ⁲"): bstack11111_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ⁳"),
        bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⁴"): bstack11111_opy_ (u"ࠧࡃࡷ࡬ࡰࡩࠦࡣࡳࡧࡤࡸ࡮ࡵ࡮ࠡࡪࡤࡨࠥ࡬ࡡࡪ࡮ࡨࡨ࠳࠭⁵")
    }
  data = {bstack11111_opy_ (u"ࠨࡧࡱࡨ࡙࡯࡭ࡦࠩ⁶"): bstack1l1lll11_opy_()}
  headers = {
      bstack11111_opy_ (u"ࠩࡄࡹࡹ࡮࡯ࡳ࡫ࡽࡥࡹ࡯࡯࡯ࠩ⁷"): bstack11111_opy_ (u"ࠪࡆࡪࡧࡲࡦࡴࠣࠫ⁸") + os.getenv(bstack11111_opy_ (u"ࠦࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠤ⁹")),
      bstack11111_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ⁺"): bstack11111_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ⁻")
  }
  response = bstack1111ll1lll_opy_(bstack11111_opy_ (u"ࠧࡑࡗࡗࠫ⁼"), bstack1llll1lll1ll_opy_ + bstack11111_opy_ (u"ࠨ࠱ࡷࡩࡸࡺ࡟ࡳࡷࡱࡷ࠴ࡹࡴࡰࡲࠪ⁽"), data, { bstack11111_opy_ (u"ࠩ࡫ࡩࡦࡪࡥࡳࡵࠪ⁾"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11111_opy_ (u"ࠥࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮ࠡ࡯ࡤࡶࡰ࡫ࡤࠡࡣࡶࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠠࡢࡶࠣࠦⁿ") + bstack1lll11ll_opy_().isoformat() + bstack11111_opy_ (u"ࠫ࡟࠭₀"))
      return {bstack11111_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ₁"): bstack11111_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧ₂"), bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ₃"): bstack11111_opy_ (u"ࠨࠩ₄")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡲࡧࡲ࡬࡫ࡱ࡫ࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡯࡯࡯ࠢࡲࡪࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰ࠽ࠤࠧ₅") + str(error))
    return {
        bstack11111_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪ₆"): bstack11111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ₇"),
        bstack11111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭₈"): str(error)
    }
def bstack1llll1l1l1l1_opy_(bstack1llll1ll1l11_opy_):
    return re.match(bstack11111_opy_ (u"ࡸࠧ࡟࡞ࡧ࠯࠭ࡢ࠮࡝ࡦ࠮࠭ࡄࠪࠧ₉"), bstack1llll1ll1l11_opy_.strip()) is not None
def bstack1111lllll1_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1l1ll1l_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1l1ll1l_opy_ = desired_capabilities
        else:
          bstack1llll1l1ll1l_opy_ = {}
        bstack1l11111ll1l_opy_ = (bstack1llll1l1ll1l_opy_.get(bstack11111_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪ࠭₊"), bstack11111_opy_ (u"ࠨࠩ₋")).lower() or caps.get(bstack11111_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨ₌"), bstack11111_opy_ (u"ࠪࠫ₍")).lower())
        if bstack1l11111ll1l_opy_ == bstack11111_opy_ (u"ࠫ࡮ࡵࡳࠨ₎"):
            return True
        if bstack1l11111ll1l_opy_ == bstack11111_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩ࠭₏"):
            bstack1l111l11l1l_opy_ = str(float(caps.get(bstack11111_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠨₐ")) or bstack1llll1l1ll1l_opy_.get(bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨₑ"), {}).get(bstack11111_opy_ (u"ࠨࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠫₒ"),bstack11111_opy_ (u"ࠩࠪₓ"))))
            if bstack1l11111ll1l_opy_ == bstack11111_opy_ (u"ࠪࡥࡳࡪࡲࡰ࡫ࡧࠫₔ") and int(bstack1l111l11l1l_opy_.split(bstack11111_opy_ (u"ࠫ࠳࠭ₕ"))[0]) < float(bstack11l11l1111l_opy_):
                logger.warning(str(bstack11l11l1l11l_opy_))
                return False
            return True
        bstack1l111l1ll11_opy_ = caps.get(bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭ₖ"), {}).get(bstack11111_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠪₗ"), caps.get(bstack11111_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࠧₘ"), bstack11111_opy_ (u"ࠨࠩₙ")))
        if bstack1l111l1ll11_opy_:
            logger.warning(bstack11111_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡇࡩࡸࡱࡴࡰࡲࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨₚ"))
            return False
        browser = caps.get(bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨₛ"), bstack11111_opy_ (u"ࠫࠬₜ")).lower() or bstack1llll1l1ll1l_opy_.get(bstack11111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ₝"), bstack11111_opy_ (u"࠭ࠧ₞")).lower()
        if browser != bstack11111_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ₟"):
            logger.warning(bstack11111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ₠"))
            return False
        browser_version = caps.get(bstack11111_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ₡")) or caps.get(bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ₢")) or bstack1llll1l1ll1l_opy_.get(bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ₣")) or bstack1llll1l1ll1l_opy_.get(bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭₤"), {}).get(bstack11111_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ₥")) or bstack1llll1l1ll1l_opy_.get(bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ₦"), {}).get(bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ₧"))
        bstack1l111111l1l_opy_ = bstack1llll11lllll_opy_.bstack1l1111lll11_opy_
        bstack1llll1l11lll_opy_ = False
        if config is not None:
          bstack1llll1l11lll_opy_ = bstack11111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭₨") in config and str(config[bstack11111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ₩")]).lower() != bstack11111_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ₪")
        if os.environ.get(bstack11111_opy_ (u"ࠬࡏࡓࡠࡐࡒࡒࡤࡈࡓࡕࡃࡆࡏࡤࡏࡎࡇࡔࡄࡣࡆ࠷࠱࡚ࡡࡖࡉࡘ࡙ࡉࡐࡐࠪ₫"), bstack11111_opy_ (u"࠭ࠧ€")).lower() == bstack11111_opy_ (u"ࠧࡵࡴࡸࡩࠬ₭") or bstack1llll1l11lll_opy_:
          bstack1l111111l1l_opy_ = bstack1llll11lllll_opy_.bstack1l1111l1lll_opy_
        if browser_version and browser_version != bstack11111_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨ₮") and int(browser_version.split(bstack11111_opy_ (u"ࠩ࠱ࠫ₯"))[0]) <= bstack1l111111l1l_opy_:
          logger.warning(bstack1lll1l1l111_opy_ (u"ࠪࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥ࡭ࡲࡦࡣࡷࡩࡷࠦࡴࡩࡣࡱࠤࢀࡳࡩ࡯ࡡࡤ࠵࠶ࡿ࡟ࡴࡷࡳࡴࡴࡸࡴࡦࡦࡢࡧ࡭ࡸ࡯࡮ࡧࡢࡺࡪࡸࡳࡪࡱࡱࢁ࠳࠭₰"))
          return False
        if not options:
          bstack1l111l1lll1_opy_ = caps.get(bstack11111_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ₱")) or bstack1llll1l1ll1l_opy_.get(bstack11111_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ₲"), {})
          if bstack11111_opy_ (u"࠭࠭࠮ࡪࡨࡥࡩࡲࡥࡴࡵࠪ₳") in bstack1l111l1lll1_opy_.get(bstack11111_opy_ (u"ࠧࡢࡴࡪࡷࠬ₴"), []):
              logger.warning(bstack11111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡳࡷࡱࠤࡴࡴࠠ࡭ࡧࡪࡥࡨࡿࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠡࡕࡺ࡭ࡹࡩࡨࠡࡶࡲࠤࡳ࡫ࡷࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥࠡࡱࡵࠤࡦࡼ࡯ࡪࡦࠣࡹࡸ࡯࡮ࡨࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠥ₵"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack11111_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡤࡰ࡮ࡪࡡࡵࡧࠣࡥ࠶࠷ࡹࠡࡵࡸࡴࡵࡵࡲࡵࠢ࠽ࠦ₶") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l11ll111l1_opy_ = config.get(bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ₷"), {})
    bstack1l11ll111l1_opy_[bstack11111_opy_ (u"ࠫࡦࡻࡴࡩࡖࡲ࡯ࡪࡴࠧ₸")] = os.getenv(bstack11111_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ₹"))
    bstack1111ll111ll_opy_ = json.loads(os.getenv(bstack11111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ₺"), bstack11111_opy_ (u"ࠧࡼࡿࠪ₻"))).get(bstack11111_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ₼"))
    if not config[bstack11111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡑࡴࡲࡨࡺࡩࡴࡎࡣࡳࠫ₽")].get(bstack11111_opy_ (u"ࠥࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠤ₾")):
      if bstack11111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ₿") in caps:
        caps[bstack11111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭⃀")][bstack11111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭⃁")] = bstack1l11ll111l1_opy_
        caps[bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⃂")][bstack11111_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ⃃")][bstack11111_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⃄")] = bstack1111ll111ll_opy_
      else:
        caps[bstack11111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃅")] = bstack1l11ll111l1_opy_
        caps[bstack11111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ⃆")][bstack11111_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⃇")] = bstack1111ll111ll_opy_
  except Exception as error:
    logger.debug(bstack11111_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷ࠳ࠦࡅࡳࡴࡲࡶ࠿ࠦࠢ⃈") +  str(error))
def bstack11l1lll11_opy_(driver, bstack1llll1l1l111_opy_):
  try:
    setattr(driver, bstack11111_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡁ࠲࠳ࡼࡗ࡭ࡵࡵ࡭ࡦࡖࡧࡦࡴࠧ⃉"), True)
    session = driver.session_id
    if session:
      bstack1llll1l1lll1_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1l1lll1_opy_ = False
      bstack1llll1l1lll1_opy_ = url.scheme in [bstack11111_opy_ (u"ࠣࡪࡷࡸࡵࠨ⃊"), bstack11111_opy_ (u"ࠤ࡫ࡸࡹࡶࡳࠣ⃋")]
      if bstack1llll1l1lll1_opy_:
        if bstack1llll1l1l111_opy_:
          logger.info(bstack11111_opy_ (u"ࠥࡗࡪࡺࡵࡱࠢࡩࡳࡷࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡩࡣࡶࠤࡸࡺࡡࡳࡶࡨࡨ࠳ࠦࡁࡶࡶࡲࡱࡦࡺࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡨࡥࡨ࡫ࡱࠤࡲࡵ࡭ࡦࡰࡷࡥࡷ࡯࡬ࡺ࠰ࠥ⃌"))
      return bstack1llll1l1l111_opy_
  except Exception as e:
    logger.error(bstack11111_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡹࡧࡲࡵ࡫ࡱ࡫ࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡶࡧࡦࡴࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩ࠿ࠦࠢ⃍") + str(e))
    return False
def bstack1lll1l1ll_opy_(driver, name, path):
  try:
    bstack1l111l1l11l_opy_ = {
        bstack11111_opy_ (u"ࠬࡺࡨࡕࡧࡶࡸࡗࡻ࡮ࡖࡷ࡬ࡨࠬ⃎"): threading.current_thread().current_test_uuid,
        bstack11111_opy_ (u"࠭ࡴࡩࡄࡸ࡭ࡱࡪࡕࡶ࡫ࡧࠫ⃏"): os.environ.get(bstack11111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬ⃐"), bstack11111_opy_ (u"ࠨࠩ⃑")),
        bstack11111_opy_ (u"ࠩࡷ࡬ࡏࡽࡴࡕࡱ࡮ࡩࡳ⃒࠭"): os.environ.get(bstack11111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢࡎ࡜⃓࡚ࠧ"), bstack11111_opy_ (u"ࠫࠬ⃔"))
    }
    bstack1ll11llll1l_opy_ = bstack1ll11111ll_opy_.bstack1ll1111lll1_opy_(EVENTS.bstack111111lll1_opy_.value)
    logger.debug(bstack11111_opy_ (u"ࠬࡖࡥࡳࡨࡲࡶࡲ࡯࡮ࡨࠢࡶࡧࡦࡴࠠࡣࡧࡩࡳࡷ࡫ࠠࡴࡣࡹ࡭ࡳ࡭ࠠࡳࡧࡶࡹࡱࡺࡳࠨ⃕"))
    try:
      if (bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"࠭ࡩࡴࡃࡳࡴࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭⃖"), None) and bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡢࡲࡳࡅ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ⃗"), None)):
        scripts = {bstack11111_opy_ (u"ࠨࡵࡦࡥࡳ⃘࠭"): bstack11l1lll1l_opy_.perform_scan}
        bstack1llll1l1111l_opy_ = json.loads(scripts[bstack11111_opy_ (u"ࠤࡶࡧࡦࡴ⃙ࠢ")].replace(bstack11111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨ⃚"), bstack11111_opy_ (u"ࠦࠧ⃛")))
        bstack1llll1l1111l_opy_[bstack11111_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ⃜")][bstack11111_opy_ (u"࠭࡭ࡦࡶ࡫ࡳࡩ࠭⃝")] = None
        scripts[bstack11111_opy_ (u"ࠢࡴࡥࡤࡲࠧ⃞")] = bstack11111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࠦ⃟") + json.dumps(bstack1llll1l1111l_opy_)
        bstack11l1lll1l_opy_.bstack1l1lll11l_opy_(scripts)
        bstack11l1lll1l_opy_.store()
        logger.debug(driver.execute_script(bstack11l1lll1l_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11l1lll1l_opy_.perform_scan, {bstack11111_opy_ (u"ࠤࡰࡩࡹ࡮࡯ࡥࠤ⃠"): name}))
      bstack1ll11111ll_opy_.end(EVENTS.bstack111111lll1_opy_.value, bstack1ll11llll1l_opy_ + bstack11111_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥ⃡"), bstack1ll11llll1l_opy_ + bstack11111_opy_ (u"ࠦ࠿࡫࡮ࡥࠤ⃢"), True, None)
    except Exception as error:
      bstack1ll11111ll_opy_.end(EVENTS.bstack111111lll1_opy_.value, bstack1ll11llll1l_opy_ + bstack11111_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ⃣"), bstack1ll11llll1l_opy_ + bstack11111_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ⃤"), False, str(error))
    bstack1ll11llll1l_opy_ = bstack1ll11111ll_opy_.bstack11ll11lllll_opy_(EVENTS.bstack1l1111lll1l_opy_.value)
    bstack1ll11111ll_opy_.mark(bstack1ll11llll1l_opy_ + bstack11111_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺ⃥ࠢ"))
    try:
      if (bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ⃦"), None) and bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ⃧"), None)):
        scripts = {bstack11111_opy_ (u"ࠪࡷࡨࡧ࡮ࠨ⃨"): bstack11l1lll1l_opy_.perform_scan}
        bstack1llll1l1111l_opy_ = json.loads(scripts[bstack11111_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ⃩")].replace(bstack11111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀ⃪ࠠࠣ"), bstack11111_opy_ (u"ࠨ⃫ࠢ")))
        bstack1llll1l1111l_opy_[bstack11111_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵ⃬ࠪ")][bstack11111_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨ⃭")] = None
        scripts[bstack11111_opy_ (u"ࠤࡶࡧࡦࡴ⃮ࠢ")] = bstack11111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨ⃯") + json.dumps(bstack1llll1l1111l_opy_)
        bstack11l1lll1l_opy_.bstack1l1lll11l_opy_(scripts)
        bstack11l1lll1l_opy_.store()
        logger.debug(driver.execute_script(bstack11l1lll1l_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11l1lll1l_opy_.bstack1llll1llllll_opy_, bstack1l111l1l11l_opy_))
      bstack1ll11111ll_opy_.end(bstack1ll11llll1l_opy_, bstack1ll11llll1l_opy_ + bstack11111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦ⃰"), bstack1ll11llll1l_opy_ + bstack11111_opy_ (u"ࠧࡀࡥ࡯ࡦࠥ⃱"),True, None)
    except Exception as error:
      bstack1ll11111ll_opy_.end(bstack1ll11llll1l_opy_, bstack1ll11llll1l_opy_ + bstack11111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ⃲"), bstack1ll11llll1l_opy_ + bstack11111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ⃳"),False, str(error))
    logger.info(bstack11111_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡩࡣࡶࠤࡪࡴࡤࡦࡦ࠱ࠦ⃴"))
  except Exception as bstack1l111l1ll1l_opy_:
    logger.error(bstack11111_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡵࡩࡸࡻ࡬ࡵࡵࠣࡧࡴࡻ࡬ࡥࠢࡱࡳࡹࠦࡢࡦࠢࡳࡶࡴࡩࡥࡴࡵࡨࡨࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦ࠼ࠣࠦ⃵") + str(path) + bstack11111_opy_ (u"ࠥࠤࡊࡸࡲࡰࡴࠣ࠾ࠧ⃶") + str(bstack1l111l1ll1l_opy_))
def bstack1llll1l11l11_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack11111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥ⃷")) and str(caps.get(bstack11111_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ⃸"))).lower() == bstack11111_opy_ (u"ࠨࡡ࡯ࡦࡵࡳ࡮ࡪࠢ⃹"):
        bstack1l111l11l1l_opy_ = caps.get(bstack11111_opy_ (u"ࠢࡢࡲࡳ࡭ࡺࡳ࠺ࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤ⃺")) or caps.get(bstack11111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥ⃻"))
        if bstack1l111l11l1l_opy_ and int(str(bstack1l111l11l1l_opy_)) < bstack11l11l1111l_opy_:
            return False
    return True
def bstack11l1l11ll1_opy_(config):
  if bstack11111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ⃼") in config:
        return config[bstack11111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⃽")]
  for platform in config.get(bstack11111_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ⃾"), []):
      if bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⃿") in platform:
          return platform[bstack11111_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭℀")]
  return None
def bstack1llll1ll1l_opy_(bstack1l1l1l111_opy_):
  try:
    browser_name = bstack1l1l1l111_opy_[bstack11111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡰࡤࡱࡪ࠭℁")]
    browser_version = bstack1l1l1l111_opy_[bstack11111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪℂ")]
    chrome_options = bstack1l1l1l111_opy_[bstack11111_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࡡࡲࡴࡹ࡯࡯࡯ࡵࠪ℃")]
    try:
        bstack1llll1ll11ll_opy_ = int(browser_version.split(bstack11111_opy_ (u"ࠪ࠲ࠬ℄"))[0])
    except ValueError as e:
        logger.error(bstack11111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡦࡳࡳࡼࡥࡳࡶ࡬ࡲ࡬ࠦࡢࡳࡱࡺࡷࡪࡸࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠣ℅") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack11111_opy_ (u"ࠬࡩࡨࡳࡱࡰࡩࠬ℆")):
        logger.warning(bstack11111_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡃࡩࡴࡲࡱࡪࠦࡢࡳࡱࡺࡷࡪࡸࡳ࠯ࠤℇ"))
        return False
    if bstack1llll1ll11ll_opy_ < bstack1llll11lllll_opy_.bstack1l1111l1lll_opy_:
        logger.warning(bstack1lll1l1l111_opy_ (u"ࠧࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡷ࡫ࡱࡶ࡫ࡵࡩࡸࠦࡃࡩࡴࡲࡱࡪࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡼࡅࡒࡒࡘ࡚ࡁࡏࡖࡖ࠲ࡒࡏࡎࡊࡏࡘࡑࡤࡔࡏࡏࡡࡅࡗ࡙ࡇࡃࡌࡡࡌࡒࡋࡘࡁࡠࡃ࠴࠵࡞ࡥࡓࡖࡒࡓࡓࡗ࡚ࡅࡅࡡࡆࡌࡗࡕࡍࡆࡡ࡙ࡉࡗ࡙ࡉࡐࡐࢀࠤࡴࡸࠠࡩ࡫ࡪ࡬ࡪࡸ࠮ࠨ℈"))
        return False
    if chrome_options and any(bstack11111_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬ℉") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack11111_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦℊ"))
        return False
    return True
  except Exception as e:
    logger.error(bstack11111_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥࡩࡨࡦࡥ࡮࡭ࡳ࡭ࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡶࡹࡵࡶ࡯ࡳࡶࠣࡪࡴࡸࠠ࡭ࡱࡦࡥࡱࠦࡃࡩࡴࡲࡱࡪࡀࠠࠣℋ") + str(e))
    return False
def bstack1l1l1111l_opy_(bstack1111l11111_opy_, config):
    try:
      bstack1l111l11111_opy_ = bstack11111_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫℌ") in config and config[bstack11111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬℍ")] == True
      bstack1llll1l11lll_opy_ = bstack11111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪℎ") in config and str(config[bstack11111_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫℏ")]).lower() != bstack11111_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧℐ")
      if not (bstack1l111l11111_opy_ and (not bstack1l1lll1ll_opy_(config) or bstack1llll1l11lll_opy_)):
        return bstack1111l11111_opy_
      bstack1llll1lll11l_opy_ = bstack11l1lll1l_opy_.bstack1lllll1111ll_opy_
      if bstack1llll1lll11l_opy_ is None:
        logger.debug(bstack11111_opy_ (u"ࠤࡊࡳࡴ࡭࡬ࡦࠢࡦ࡬ࡷࡵ࡭ࡦࠢࡲࡴࡹ࡯࡯࡯ࡵࠣࡥࡷ࡫ࠠࡏࡱࡱࡩࠧℑ"))
        return bstack1111l11111_opy_
      bstack1llll1ll11l1_opy_ = int(str(bstack1111l1l1l11_opy_()).split(bstack11111_opy_ (u"ࠪ࠲ࠬℒ"))[0])
      logger.debug(bstack11111_opy_ (u"ࠦࡘ࡫࡬ࡦࡰ࡬ࡹࡲࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡥࡧࡷࡩࡨࡺࡥࡥ࠼ࠣࠦℓ") + str(bstack1llll1ll11l1_opy_) + bstack11111_opy_ (u"ࠧࠨ℔"))
      if bstack1llll1ll11l1_opy_ == 3 and isinstance(bstack1111l11111_opy_, dict) and bstack11111_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ℕ") in bstack1111l11111_opy_ and bstack1llll1lll11l_opy_ is not None:
        if bstack11111_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ№") not in bstack1111l11111_opy_[bstack11111_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ℗")]:
          bstack1111l11111_opy_[bstack11111_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ℘")][bstack11111_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨℙ")] = {}
        if bstack11111_opy_ (u"ࠫࡦࡸࡧࡴࠩℚ") in bstack1llll1lll11l_opy_:
          if bstack11111_opy_ (u"ࠬࡧࡲࡨࡵࠪℛ") not in bstack1111l11111_opy_[bstack11111_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ℜ")][bstack11111_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬℝ")]:
            bstack1111l11111_opy_[bstack11111_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ℞")][bstack11111_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ℟")][bstack11111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ℠")] = []
          for arg in bstack1llll1lll11l_opy_[bstack11111_opy_ (u"ࠫࡦࡸࡧࡴࠩ℡")]:
            if arg not in bstack1111l11111_opy_[bstack11111_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ™")][bstack11111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ℣")][bstack11111_opy_ (u"ࠧࡢࡴࡪࡷࠬℤ")]:
              bstack1111l11111_opy_[bstack11111_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ℥")][bstack11111_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧΩ")][bstack11111_opy_ (u"ࠪࡥࡷ࡭ࡳࠨ℧")].append(arg)
        if bstack11111_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨℨ") in bstack1llll1lll11l_opy_:
          if bstack11111_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ℩") not in bstack1111l11111_opy_[bstack11111_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭K")][bstack11111_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬÅ")]:
            bstack1111l11111_opy_[bstack11111_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨℬ")][bstack11111_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧℭ")][bstack11111_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ℮")] = []
          for ext in bstack1llll1lll11l_opy_[bstack11111_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨℯ")]:
            if ext not in bstack1111l11111_opy_[bstack11111_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬℰ")][bstack11111_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫℱ")][bstack11111_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫℲ")]:
              bstack1111l11111_opy_[bstack11111_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨℳ")][bstack11111_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧℴ")][bstack11111_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧℵ")].append(ext)
        if bstack11111_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪℶ") in bstack1llll1lll11l_opy_:
          if bstack11111_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫℷ") not in bstack1111l11111_opy_[bstack11111_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ℸ")][bstack11111_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬℹ")]:
            bstack1111l11111_opy_[bstack11111_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ℺")][bstack11111_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ℻")][bstack11111_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩℼ")] = {}
          bstack111l111l111_opy_(bstack1111l11111_opy_[bstack11111_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫℽ")][bstack11111_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪℾ")][bstack11111_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬℿ")],
                    bstack1llll1lll11l_opy_[bstack11111_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭⅀")])
        os.environ[bstack11111_opy_ (u"ࠨࡋࡖࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡅࡔࡕࡌࡓࡓ࠭⅁")] = bstack11111_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⅂")
        return bstack1111l11111_opy_
      else:
        chrome_options = None
        if isinstance(bstack1111l11111_opy_, ChromeOptions):
          chrome_options = bstack1111l11111_opy_
        elif isinstance(bstack1111l11111_opy_, dict):
          for value in bstack1111l11111_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack1111l11111_opy_, dict):
            bstack1111l11111_opy_[bstack11111_opy_ (u"ࠪࡳࡵࡺࡩࡰࡰࡶࠫ⅃")] = chrome_options
          else:
            bstack1111l11111_opy_ = chrome_options
        if bstack1llll1lll11l_opy_ is not None:
          if bstack11111_opy_ (u"ࠫࡦࡸࡧࡴࠩ⅄") in bstack1llll1lll11l_opy_:
                bstack1llll1lll1l1_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1lll11l_opy_[bstack11111_opy_ (u"ࠬࡧࡲࡨࡵࠪⅅ")]
                for arg in new_args:
                    if arg not in bstack1llll1lll1l1_opy_:
                        chrome_options.add_argument(arg)
          if bstack11111_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪⅆ") in bstack1llll1lll11l_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack11111_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫⅇ"), [])
                bstack1llll1ll1l1l_opy_ = bstack1llll1lll11l_opy_[bstack11111_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬⅈ")]
                for extension in bstack1llll1ll1l1l_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack11111_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨⅉ") in bstack1llll1lll11l_opy_:
                bstack1llll1l11111_opy_ = chrome_options.experimental_options.get(bstack11111_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ⅊"), {})
                bstack1llll1ll1111_opy_ = bstack1llll1lll11l_opy_[bstack11111_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⅋")]
                bstack111l111l111_opy_(bstack1llll1l11111_opy_, bstack1llll1ll1111_opy_)
                chrome_options.add_experimental_option(bstack11111_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⅌"), bstack1llll1l11111_opy_)
        os.environ[bstack11111_opy_ (u"࠭ࡉࡔࡡࡑࡓࡓࡥࡂࡔࡖࡄࡇࡐࡥࡉࡏࡈࡕࡅࡤࡇ࠱࠲࡛ࡢࡗࡊ࡙ࡓࡊࡑࡑࠫ⅍")] = bstack11111_opy_ (u"ࠧࡵࡴࡸࡩࠬⅎ")
        return bstack1111l11111_opy_
    except Exception as e:
      logger.error(bstack11111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡡࡥࡦ࡬ࡲ࡬ࠦ࡮ࡰࡰ࠰ࡆࡘࠦࡩ࡯ࡨࡵࡥࠥࡧ࠱࠲ࡻࠣࡧ࡭ࡸ࡯࡮ࡧࠣࡳࡵࡺࡩࡰࡰࡶ࠾ࠥࠨ⅏") + str(e))
      return bstack1111l11111_opy_