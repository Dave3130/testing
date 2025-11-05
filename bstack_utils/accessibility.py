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
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1l1ll1l_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l11lll11l_opy_ as bstack1llll1l1111l_opy_, EVENTS
from bstack_utils.bstack11lll1l1l_opy_ import bstack11lll1l1l_opy_
from bstack_utils.helper import bstack1ll111ll_opy_, bstack1llll1l1_opy_, bstack1ll1llll1l_opy_, bstack111l11l1l11_opy_, \
  bstack111l111lll1_opy_, bstack11l1llll11_opy_, get_host_info, bstack111l1ll1111_opy_, bstack11ll11ll1l_opy_, error_handler, bstack1111ll111l1_opy_, bstack1111l1l1l11_opy_, bstack1l1l1ll1_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack11111l1ll1_opy_ import get_logger
from bstack_utils.bstack111l11l111_opy_ import bstack1llll11l11l_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack111l11l111_opy_ = bstack1llll11l11l_opy_()
@error_handler(class_method=False)
def _1llll1ll111l_opy_(driver, bstack1llll1l11_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack11ll1ll_opy_ (u"ࠨࡱࡶࡣࡳࡧ࡭ࡦࠩ‛"): caps.get(bstack11ll1ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨ“"), None),
        bstack11ll1ll_opy_ (u"ࠪࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ”"): bstack1llll1l11_opy_.get(bstack11ll1ll_opy_ (u"ࠫࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠧ„"), None),
        bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥ࡮ࡢ࡯ࡨࠫ‟"): caps.get(bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ†"), None),
        bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ‡"): caps.get(bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ•"), None)
    }
  except Exception as error:
    logger.debug(bstack11ll1ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡴࡱࡧࡴࡧࡱࡵࡱࠥࡪࡥࡵࡣ࡬ࡰࡸࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭‣") + str(error))
  return response
def on():
    if os.environ.get(bstack11ll1ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ․"), None) is None or os.environ[bstack11ll1ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ‥")] == bstack11ll1ll_opy_ (u"ࠧࡴࡵ࡭࡮ࠥ…"):
        return False
    return True
def bstack11ll11111_opy_(config):
  return config.get(bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭‧"), False) or any([p.get(bstack11ll1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ "), False) == True for p in config.get(bstack11ll1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ "), [])])
def bstack1lll1ll1l1_opy_(config, bstack1l11111l1l_opy_):
  try:
    bstack1llll1l1llll_opy_ = config.get(bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ‪"), False)
    if int(bstack1l11111l1l_opy_) < len(config.get(bstack11ll1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭‫"), [])) and config[bstack11ll1ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ‬")][bstack1l11111l1l_opy_]:
      bstack1llll1lll11l_opy_ = config[bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ‭")][bstack1l11111l1l_opy_].get(bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭‮"), None)
    else:
      bstack1llll1lll11l_opy_ = config.get(bstack11ll1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ "), None)
    if bstack1llll1lll11l_opy_ != None:
      bstack1llll1l1llll_opy_ = bstack1llll1lll11l_opy_
    bstack1llll1ll11ll_opy_ = os.getenv(bstack11ll1ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭‰")) is not None and len(os.getenv(bstack11ll1ll_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ‱"))) > 0 and os.getenv(bstack11ll1ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ′")) != bstack11ll1ll_opy_ (u"ࠫࡳࡻ࡬࡭ࠩ″")
    return bstack1llll1l1llll_opy_ and bstack1llll1ll11ll_opy_
  except Exception as error:
    logger.debug(bstack11ll1ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡻ࡫ࡲࡪࡨࡼ࡭ࡳ࡭ࠠࡵࡪࡨࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡩࡷࡸ࡯ࡳࠢ࠽ࠤࠬ‴") + str(error))
  return False
def bstack11llll11ll_opy_(test_tags):
  bstack1l1111ll111_opy_ = os.getenv(bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ‵"))
  if bstack1l1111ll111_opy_ is None:
    return True
  bstack1l1111ll111_opy_ = json.loads(bstack1l1111ll111_opy_)
  try:
    include_tags = bstack1l1111ll111_opy_[bstack11ll1ll_opy_ (u"ࠧࡪࡰࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬ‶")] if bstack11ll1ll_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭‷") in bstack1l1111ll111_opy_ and isinstance(bstack1l1111ll111_opy_[bstack11ll1ll_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ‸")], list) else []
    exclude_tags = bstack1l1111ll111_opy_[bstack11ll1ll_opy_ (u"ࠪࡩࡽࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ‹")] if bstack11ll1ll_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ›") in bstack1l1111ll111_opy_ and isinstance(bstack1l1111ll111_opy_[bstack11ll1ll_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ※")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack11ll1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡻࡧ࡬ࡪࡦࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤ࡫ࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡤࡨࡪࡴࡸࡥࠡࡵࡦࡥࡳࡴࡩ࡯ࡩ࠱ࠤࡊࡸࡲࡰࡴࠣ࠾ࠥࠨ‼") + str(error))
  return False
def bstack1llll1ll1111_opy_(config, frameworkName, bstack1llll1lll1l1_opy_, bstack1llll1l1lll1_opy_):
  bstack1llll1l11lll_opy_ = bstack111l11l1l11_opy_(config)
  bstack1llll1l1l11l_opy_ = bstack111l111lll1_opy_(config)
  if bstack1llll1l11lll_opy_ is None or bstack1llll1l1l11l_opy_ is None:
    logger.error(bstack11ll1ll_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࡎ࡫ࡶࡷ࡮ࡴࡧࠡࡣࡸࡸ࡭࡫࡮ࡵ࡫ࡦࡥࡹ࡯࡯࡯ࠢࡷࡳࡰ࡫࡮ࠨ‽"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ‾"), bstack11ll1ll_opy_ (u"ࠩࡾࢁࠬ‿")))
    data = {
        bstack11ll1ll_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨ⁀"): config[bstack11ll1ll_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ⁁")],
        bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ⁂"): config.get(bstack11ll1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ⁃"), os.path.basename(os.getcwd())),
        bstack11ll1ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡚ࡩ࡮ࡧࠪ⁄"): bstack1ll111ll_opy_(),
        bstack11ll1ll_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭⁅"): config.get(bstack11ll1ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ⁆"), bstack11ll1ll_opy_ (u"ࠪࠫ⁇")),
        bstack11ll1ll_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ⁈"): {
            bstack11ll1ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬ⁉"): frameworkName,
            bstack11ll1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩ⁊"): bstack1llll1lll1l1_opy_,
            bstack11ll1ll_opy_ (u"ࠧࡴࡦ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ⁋"): __version__,
            bstack11ll1ll_opy_ (u"ࠨ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠪ⁌"): bstack11ll1ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩ⁍"),
            bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡇࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪ⁎"): bstack11ll1ll_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭⁏"),
            bstack11ll1ll_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁐"): bstack1llll1l1lll1_opy_
        },
        bstack11ll1ll_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨ⁑"): settings,
        bstack11ll1ll_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࡄࡱࡱࡸࡷࡵ࡬ࠨ⁒"): bstack111l1ll1111_opy_(),
        bstack11ll1ll_opy_ (u"ࠨࡥ࡬ࡍࡳ࡬࡯ࠨ⁓"): bstack11l1llll11_opy_(),
        bstack11ll1ll_opy_ (u"ࠩ࡫ࡳࡸࡺࡉ࡯ࡨࡲࠫ⁔"): get_host_info(),
        bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ⁕"): bstack1ll1llll1l_opy_(config)
    }
    headers = {
        bstack11ll1ll_opy_ (u"ࠫࡈࡵ࡮ࡵࡧࡱࡸ࠲࡚ࡹࡱࡧࠪ⁖"): bstack11ll1ll_opy_ (u"ࠬࡧࡰࡱ࡮࡬ࡧࡦࡺࡩࡰࡰ࠲࡮ࡸࡵ࡮ࠨ⁗"),
    }
    config = {
        bstack11ll1ll_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ⁘"): (bstack1llll1l11lll_opy_, bstack1llll1l1l11l_opy_),
        bstack11ll1ll_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨ⁙"): headers
    }
    response = bstack11ll11ll1l_opy_(bstack11ll1ll_opy_ (u"ࠨࡒࡒࡗ࡙࠭⁚"), bstack1llll1l1111l_opy_ + bstack11ll1ll_opy_ (u"ࠩ࠲ࡺ࠷࠵ࡴࡦࡵࡷࡣࡷࡻ࡮ࡴࠩ⁛"), data, config)
    bstack1llll1l11111_opy_ = response.json()
    if bstack1llll1l11111_opy_[bstack11ll1ll_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ⁜")]:
      parsed = json.loads(os.getenv(bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ⁝"), bstack11ll1ll_opy_ (u"ࠬࢁࡽࠨ⁞")))
      parsed[bstack11ll1ll_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ ")] = bstack1llll1l11111_opy_[bstack11ll1ll_opy_ (u"ࠧࡥࡣࡷࡥࠬ⁠")][bstack11ll1ll_opy_ (u"ࠨࡵࡦࡥࡳࡴࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⁡")]
      os.environ[bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ⁢")] = json.dumps(parsed)
      bstack11lll1l1l_opy_.bstack1ll11lllll_opy_(bstack1llll1l11111_opy_[bstack11ll1ll_opy_ (u"ࠪࡨࡦࡺࡡࠨ⁣")][bstack11ll1ll_opy_ (u"ࠫࡸࡩࡲࡪࡲࡷࡷࠬ⁤")])
      bstack11lll1l1l_opy_.bstack1lllll1111ll_opy_(bstack1llll1l11111_opy_[bstack11ll1ll_opy_ (u"ࠬࡪࡡࡵࡣࠪ⁥")][bstack11ll1ll_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨ⁦")])
      bstack11lll1l1l_opy_.store()
      return bstack1llll1l11111_opy_[bstack11ll1ll_opy_ (u"ࠧࡥࡣࡷࡥࠬ⁧")][bstack11ll1ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡕࡱ࡮ࡩࡳ࠭⁨")], bstack1llll1l11111_opy_[bstack11ll1ll_opy_ (u"ࠩࡧࡥࡹࡧࠧ⁩")][bstack11ll1ll_opy_ (u"ࠪ࡭ࡩ࠭⁪")]
    else:
      logger.error(bstack11ll1ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡲࡶࡰࡱ࡭ࡳ࡭ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠬ⁫") + bstack1llll1l11111_opy_[bstack11ll1ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭⁬")])
      if bstack1llll1l11111_opy_[bstack11ll1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⁭")] == bstack11ll1ll_opy_ (u"ࠧࡊࡰࡹࡥࡱ࡯ࡤࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡲࡤࡷࡸ࡫ࡤ࠯ࠩ⁮"):
        for bstack1llll1l11ll1_opy_ in bstack1llll1l11111_opy_[bstack11ll1ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࡳࠨ⁯")]:
          logger.error(bstack1llll1l11ll1_opy_[bstack11ll1ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⁰")])
      return None, None
  except Exception as error:
    logger.error(bstack11ll1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡸࡵ࡯ࠢࡩࡳࡷࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࠦⁱ") +  str(error))
    return None, None
def bstack1llll1l111l1_opy_():
  if os.getenv(bstack11ll1ll_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ⁲")) is None:
    return {
        bstack11ll1ll_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⁳"): bstack11ll1ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ⁴"),
        bstack11ll1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⁵"): bstack11ll1ll_opy_ (u"ࠨࡄࡸ࡭ࡱࡪࠠࡤࡴࡨࡥࡹ࡯࡯࡯ࠢ࡫ࡥࡩࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠧ⁶")
    }
  data = {bstack11ll1ll_opy_ (u"ࠩࡨࡲࡩ࡚ࡩ࡮ࡧࠪ⁷"): bstack1ll111ll_opy_()}
  headers = {
      bstack11ll1ll_opy_ (u"ࠪࡅࡺࡺࡨࡰࡴ࡬ࡾࡦࡺࡩࡰࡰࠪ⁸"): bstack11ll1ll_opy_ (u"ࠫࡇ࡫ࡡࡳࡧࡵࠤࠬ⁹") + os.getenv(bstack11ll1ll_opy_ (u"ࠧࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠥ⁺")),
      bstack11ll1ll_opy_ (u"࠭ࡃࡰࡰࡷࡩࡳࡺ࠭ࡕࡻࡳࡩࠬ⁻"): bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳࡰ࡮ࡩࡡࡵ࡫ࡲࡲ࠴ࡰࡳࡰࡰࠪ⁼")
  }
  response = bstack11ll11ll1l_opy_(bstack11ll1ll_opy_ (u"ࠨࡒࡘࡘࠬ⁽"), bstack1llll1l1111l_opy_ + bstack11ll1ll_opy_ (u"ࠩ࠲ࡸࡪࡹࡴࡠࡴࡸࡲࡸ࠵ࡳࡵࡱࡳࠫ⁾"), data, { bstack11ll1ll_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫⁿ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack11ll1ll_opy_ (u"ࠦࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡕࡧࡶࡸࠥࡘࡵ࡯ࠢࡰࡥࡷࡱࡥࡥࠢࡤࡷࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤࠡࡣࡷࠤࠧ₀") + bstack1llll1l1_opy_().isoformat() + bstack11ll1ll_opy_ (u"ࠬࡠࠧ₁"))
      return {bstack11ll1ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭₂"): bstack11ll1ll_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨ₃"), bstack11ll1ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ₄"): bstack11ll1ll_opy_ (u"ࠩࠪ₅")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack11ll1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡳࡡࡳ࡭࡬ࡲ࡬ࠦࡣࡰ࡯ࡳࡰࡪࡺࡩࡰࡰࠣࡳ࡫ࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡗࡩࡸࡺࠠࡓࡷࡱ࠾ࠥࠨ₆") + str(error))
    return {
        bstack11ll1ll_opy_ (u"ࠫࡸࡺࡡࡵࡷࡶࠫ₇"): bstack11ll1ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫ₈"),
        bstack11ll1ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ₉"): str(error)
    }
def bstack1llll1ll1l1l_opy_(bstack1llll1l1l1ll_opy_):
    return re.match(bstack11ll1ll_opy_ (u"ࡲࠨࡠ࡟ࡨ࠰࠮࡜࠯࡞ࡧ࠯࠮ࡅࠤࠨ₊"), bstack1llll1l1l1ll_opy_.strip()) is not None
def bstack1ll1l11ll1_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1l1l1l1_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1l1l1l1_opy_ = desired_capabilities
        else:
          bstack1llll1l1l1l1_opy_ = {}
        bstack1l1111lll11_opy_ = (bstack1llll1l1l1l1_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠧ₋"), bstack11ll1ll_opy_ (u"ࠩࠪ₌")).lower() or caps.get(bstack11ll1ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩ₍"), bstack11ll1ll_opy_ (u"ࠫࠬ₎")).lower())
        if bstack1l1111lll11_opy_ == bstack11ll1ll_opy_ (u"ࠬ࡯࡯ࡴࠩ₏"):
            return True
        if bstack1l1111lll11_opy_ == bstack11ll1ll_opy_ (u"࠭ࡡ࡯ࡦࡵࡳ࡮ࡪࠧₐ"):
            bstack1l111l11l1l_opy_ = str(float(caps.get(bstack11ll1ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩₑ")) or bstack1llll1l1l1l1_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩₒ"), {}).get(bstack11ll1ll_opy_ (u"ࠩࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠬₓ"),bstack11ll1ll_opy_ (u"ࠪࠫₔ"))))
            if bstack1l1111lll11_opy_ == bstack11ll1ll_opy_ (u"ࠫࡦࡴࡤࡳࡱ࡬ࡨࠬₕ") and int(bstack1l111l11l1l_opy_.split(bstack11ll1ll_opy_ (u"ࠬ࠴ࠧₖ"))[0]) < float(bstack11l11l11l1l_opy_):
                logger.warning(str(bstack11l1l111lll_opy_))
                return False
            return True
        bstack1l1111ll1ll_opy_ = caps.get(bstack11ll1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧₗ"), {}).get(bstack11ll1ll_opy_ (u"ࠧࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠫₘ"), caps.get(bstack11ll1ll_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࠨₙ"), bstack11ll1ll_opy_ (u"ࠩࠪₚ")))
        if bstack1l1111ll1ll_opy_:
            logger.warning(bstack11ll1ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡈࡪࡹ࡫ࡵࡱࡳࠤࡧࡸ࡯ࡸࡵࡨࡶࡸ࠴ࠢₛ"))
            return False
        browser = caps.get(bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠩₜ"), bstack11ll1ll_opy_ (u"ࠬ࠭₝")).lower() or bstack1llll1l1l1l1_opy_.get(bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫ₞"), bstack11ll1ll_opy_ (u"ࠧࠨ₟")).lower()
        if browser != bstack11ll1ll_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨ₠"):
            logger.warning(bstack11ll1ll_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧ₡"))
            return False
        browser_version = caps.get(bstack11ll1ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ₢")) or caps.get(bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭₣")) or bstack1llll1l1l1l1_opy_.get(bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭₤")) or bstack1llll1l1l1l1_opy_.get(bstack11ll1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ₥"), {}).get(bstack11ll1ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ₦")) or bstack1llll1l1l1l1_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ₧"), {}).get(bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ₨"))
        bstack1l11111l1l1_opy_ = bstack1llll1l1ll1l_opy_.bstack1l111ll1111_opy_
        bstack1llll1l11l11_opy_ = False
        if config is not None:
          bstack1llll1l11l11_opy_ = bstack11ll1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ₩") in config and str(config[bstack11ll1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ₪")]).lower() != bstack11ll1ll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ₫")
        if os.environ.get(bstack11ll1ll_opy_ (u"࠭ࡉࡔࡡࡑࡓࡓࡥࡂࡔࡖࡄࡇࡐࡥࡉࡏࡈࡕࡅࡤࡇ࠱࠲࡛ࡢࡗࡊ࡙ࡓࡊࡑࡑࠫ€"), bstack11ll1ll_opy_ (u"ࠧࠨ₭")).lower() == bstack11ll1ll_opy_ (u"ࠨࡶࡵࡹࡪ࠭₮") or bstack1llll1l11l11_opy_:
          bstack1l11111l1l1_opy_ = bstack1llll1l1ll1l_opy_.bstack1l111111lll_opy_
        if browser_version and browser_version != bstack11ll1ll_opy_ (u"ࠩ࡯ࡥࡹ࡫ࡳࡵࠩ₯") and int(browser_version.split(bstack11ll1ll_opy_ (u"ࠪ࠲ࠬ₰"))[0]) <= bstack1l11111l1l1_opy_:
          logger.warning(bstack1lll1ll1l11_opy_ (u"ࠫࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡈ࡮ࡲࡰ࡯ࡨࠤࡧࡸ࡯ࡸࡵࡨࡶࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡧࡳࡧࡤࡸࡪࡸࠠࡵࡪࡤࡲࠥࢁ࡭ࡪࡰࡢࡥ࠶࠷ࡹࡠࡵࡸࡴࡵࡵࡲࡵࡧࡧࡣࡨ࡮ࡲࡰ࡯ࡨࡣࡻ࡫ࡲࡴ࡫ࡲࡲࢂ࠴ࠧ₱"))
          return False
        if not options:
          bstack1l11111ll11_opy_ = caps.get(bstack11ll1ll_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ₲")) or bstack1llll1l1l1l1_opy_.get(bstack11ll1ll_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ₳"), {})
          if bstack11ll1ll_opy_ (u"ࠧ࠮࠯࡫ࡩࡦࡪ࡬ࡦࡵࡶࠫ₴") in bstack1l11111ll11_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭₵"), []):
              logger.warning(bstack11ll1ll_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡴࡸࡲࠥࡵ࡮ࠡ࡮ࡨ࡫ࡦࡩࡹࠡࡪࡨࡥࡩࡲࡥࡴࡵࠣࡱࡴࡪࡥ࠯ࠢࡖࡻ࡮ࡺࡣࡩࠢࡷࡳࠥࡴࡥࡸࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦࠢࡲࡶࠥࡧࡶࡰ࡫ࡧࠤࡺࡹࡩ࡯ࡩࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠦ₶"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack11ll1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡹࡥࡱ࡯ࡤࡢࡶࡨࠤࡦ࠷࠱ࡺࠢࡶࡹࡵࡶ࡯ࡳࡶࠣ࠾ࠧ₷") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l11l1ll1_opy_ = config.get(bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ₸"), {})
    bstack1l1l11l1ll1_opy_[bstack11ll1ll_opy_ (u"ࠬࡧࡵࡵࡪࡗࡳࡰ࡫࡮ࠨ₹")] = os.getenv(bstack11ll1ll_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ₺"))
    bstack1111l11ll11_opy_ = json.loads(os.getenv(bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ₻"), bstack11ll1ll_opy_ (u"ࠨࡽࢀࠫ₼"))).get(bstack11ll1ll_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ₽"))
    if not config[bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡒࡵࡳࡩࡻࡣࡵࡏࡤࡴࠬ₾")].get(bstack11ll1ll_opy_ (u"ࠦࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠥ₿")):
      if bstack11ll1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭⃀") in caps:
        caps[bstack11ll1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ⃁")][bstack11ll1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ⃂")] = bstack1l1l11l1ll1_opy_
        caps[bstack11ll1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⃃")][bstack11ll1ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃄")][bstack11ll1ll_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ⃅")] = bstack1111l11ll11_opy_
      else:
        caps[bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ⃆")] = bstack1l1l11l1ll1_opy_
        caps[bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ⃇")][bstack11ll1ll_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⃈")] = bstack1111l11ll11_opy_
  except Exception as error:
    logger.debug(bstack11ll1ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡶࡩࡹࡺࡩ࡯ࡩࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠴ࠠࡆࡴࡵࡳࡷࡀࠠࠣ⃉") +  str(error))
def bstack1ll1ll1l11_opy_(driver, bstack1llll1ll1lll_opy_):
  try:
    setattr(driver, bstack11ll1ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡂ࠳࠴ࡽࡘ࡮࡯ࡶ࡮ࡧࡗࡨࡧ࡮ࠨ⃊"), True)
    session = driver.session_id
    if session:
      bstack1llll1l1l111_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1l1l111_opy_ = False
      bstack1llll1l1l111_opy_ = url.scheme in [bstack11ll1ll_opy_ (u"ࠤ࡫ࡸࡹࡶࠢ⃋"), bstack11ll1ll_opy_ (u"ࠥ࡬ࡹࡺࡰࡴࠤ⃌")]
      if bstack1llll1l1l111_opy_:
        if bstack1llll1ll1lll_opy_:
          logger.info(bstack11ll1ll_opy_ (u"ࠦࡘ࡫ࡴࡶࡲࠣࡪࡴࡸࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡵࡧࡶࡸ࡮ࡴࡧࠡࡪࡤࡷࠥࡹࡴࡢࡴࡷࡩࡩ࠴ࠠࡂࡷࡷࡳࡲࡧࡴࡦࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡢࡦࡩ࡬ࡲࠥࡳ࡯࡮ࡧࡱࡸࡦࡸࡩ࡭ࡻ࠱ࠦ⃍"))
      return bstack1llll1ll1lll_opy_
  except Exception as e:
    logger.error(bstack11ll1ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸࡺࡡࡳࡶ࡬ࡲ࡬ࠦࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡡࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡷࡨࡧ࡮ࠡࡨࡲࡶࠥࡺࡨࡪࡵࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣ⃎") + str(e))
    return False
def bstack111ll1l1_opy_(driver, name, path):
  try:
    bstack1l1111lll1l_opy_ = {
        bstack11ll1ll_opy_ (u"࠭ࡴࡩࡖࡨࡷࡹࡘࡵ࡯ࡗࡸ࡭ࡩ࠭⃏"): threading.current_thread().current_test_uuid,
        bstack11ll1ll_opy_ (u"ࠧࡵࡪࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬ⃐"): os.environ.get(bstack11ll1ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭⃑"), bstack11ll1ll_opy_ (u"⃒ࠩࠪ")),
        bstack11ll1ll_opy_ (u"ࠪࡸ࡭ࡐࡷࡵࡖࡲ࡯ࡪࡴ⃓ࠧ"): os.environ.get(bstack11ll1ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣࡏ࡝ࡔࠨ⃔"), bstack11ll1ll_opy_ (u"ࠬ࠭⃕"))
    }
    bstack1l1lll1l1ll_opy_ = bstack111l11l111_opy_.bstack1l1lll1l111_opy_(EVENTS.bstack111l1l1l11_opy_.value)
    logger.debug(bstack11ll1ll_opy_ (u"࠭ࡐࡦࡴࡩࡳࡷࡳࡩ࡯ࡩࠣࡷࡨࡧ࡮ࠡࡤࡨࡪࡴࡸࡥࠡࡵࡤࡺ࡮ࡴࡧࠡࡴࡨࡷࡺࡲࡴࡴࠩ⃖"))
    try:
      if (bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠧࡪࡵࡄࡴࡵࡇ࠱࠲ࡻࡗࡩࡸࡺࠧ⃗"), None) and bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠨࡣࡳࡴࡆ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯⃘ࠪ"), None)):
        scripts = {bstack11ll1ll_opy_ (u"ࠩࡶࡧࡦࡴ⃙ࠧ"): bstack11lll1l1l_opy_.perform_scan}
        bstack1llll1lll111_opy_ = json.loads(scripts[bstack11ll1ll_opy_ (u"ࠥࡷࡨࡧ࡮⃚ࠣ")].replace(bstack11ll1ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࠢ⃛"), bstack11ll1ll_opy_ (u"ࠧࠨ⃜")))
        bstack1llll1lll111_opy_[bstack11ll1ll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ⃝")][bstack11ll1ll_opy_ (u"ࠧ࡮ࡧࡷ࡬ࡴࡪࠧ⃞")] = None
        scripts[bstack11ll1ll_opy_ (u"ࠣࡵࡦࡥࡳࠨ⃟")] = bstack11ll1ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࠧ⃠") + json.dumps(bstack1llll1lll111_opy_)
        bstack11lll1l1l_opy_.bstack1ll11lllll_opy_(scripts)
        bstack11lll1l1l_opy_.store()
        logger.debug(driver.execute_script(bstack11lll1l1l_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11lll1l1l_opy_.perform_scan, {bstack11ll1ll_opy_ (u"ࠥࡱࡪࡺࡨࡰࡦࠥ⃡"): name}))
      bstack111l11l111_opy_.end(EVENTS.bstack111l1l1l11_opy_.value, bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦ⃢"), bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠧࡀࡥ࡯ࡦࠥ⃣"), True, None)
    except Exception as error:
      bstack111l11l111_opy_.end(EVENTS.bstack111l1l1l11_opy_.value, bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ⃤"), bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠢ࠻ࡧࡱࡨ⃥ࠧ"), False, str(error))
    bstack1l1lll1l1ll_opy_ = bstack111l11l111_opy_.bstack11ll11lllll_opy_(EVENTS.bstack1l111l1l1ll_opy_.value)
    bstack111l11l111_opy_.mark(bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴ⃦ࠣ"))
    try:
      if (bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠩ࡬ࡷࡆࡶࡰࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩ⃧"), None) and bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠪࡥࡵࡶࡁ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱ⃨ࠬ"), None)):
        scripts = {bstack11ll1ll_opy_ (u"ࠫࡸࡩࡡ࡯ࠩ⃩"): bstack11lll1l1l_opy_.perform_scan}
        bstack1llll1lll111_opy_ = json.loads(scripts[bstack11ll1ll_opy_ (u"ࠧࡹࡣࡢࡰ⃪ࠥ")].replace(bstack11ll1ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࠤ⃫"), bstack11ll1ll_opy_ (u"⃬ࠢࠣ")))
        bstack1llll1lll111_opy_[bstack11ll1ll_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶ⃭ࠫ")][bstack11ll1ll_opy_ (u"ࠩࡰࡩࡹ࡮࡯ࡥ⃮ࠩ")] = None
        scripts[bstack11ll1ll_opy_ (u"ࠥࡷࡨࡧ࡮⃯ࠣ")] = bstack11ll1ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࠢ⃰") + json.dumps(bstack1llll1lll111_opy_)
        bstack11lll1l1l_opy_.bstack1ll11lllll_opy_(scripts)
        bstack11lll1l1l_opy_.store()
        logger.debug(driver.execute_script(bstack11lll1l1l_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11lll1l1l_opy_.bstack1llll1lllll1_opy_, bstack1l1111lll1l_opy_))
      bstack111l11l111_opy_.end(bstack1l1lll1l1ll_opy_, bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ⃱"), bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ⃲"),True, None)
    except Exception as error:
      bstack111l11l111_opy_.end(bstack1l1lll1l1ll_opy_, bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ⃳"), bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ⃴"),False, str(error))
    logger.info(bstack11ll1ll_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡵࡪ࡬ࡷࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡪࡤࡷࠥ࡫࡮ࡥࡧࡧ࠲ࠧ⃵"))
  except Exception as bstack1l111l11l11_opy_:
    logger.error(bstack11ll1ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡶࡪࡹࡵ࡭ࡶࡶࠤࡨࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣࡴࡷࡵࡣࡦࡵࡶࡩࡩࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡵࡧࡶࡸࠥࡩࡡࡴࡧ࠽ࠤࠧ⃶") + str(path) + bstack11ll1ll_opy_ (u"ࠦࠥࡋࡲࡳࡱࡵࠤ࠿ࠨ⃷") + str(bstack1l111l11l11_opy_))
def bstack1llll1ll1l11_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack11ll1ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ⃸")) and str(caps.get(bstack11ll1ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ⃹"))).lower() == bstack11ll1ll_opy_ (u"ࠢࡢࡰࡧࡶࡴ࡯ࡤࠣ⃺"):
        bstack1l111l11l1l_opy_ = caps.get(bstack11ll1ll_opy_ (u"ࠣࡣࡳࡴ࡮ࡻ࡭࠻ࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥ⃻")) or caps.get(bstack11ll1ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ⃼"))
        if bstack1l111l11l1l_opy_ and int(str(bstack1l111l11l1l_opy_)) < bstack11l11l11l1l_opy_:
            return False
    return True
def bstack1l1l1l1l1l_opy_(config):
  if bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⃽") in config:
        return config[bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⃾")]
  for platform in config.get(bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ⃿"), []):
      if bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭℀") in platform:
          return platform[bstack11ll1ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ℁")]
  return None
def bstack1ll1l1l11_opy_(bstack11llll111_opy_):
  try:
    browser_name = bstack11llll111_opy_[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧℂ")]
    browser_version = bstack11llll111_opy_[bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫ℃")]
    chrome_options = bstack11llll111_opy_[bstack11ll1ll_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࡢࡳࡵࡺࡩࡰࡰࡶࠫ℄")]
    try:
        bstack1llll1l11l1l_opy_ = int(browser_version.split(bstack11ll1ll_opy_ (u"ࠫ࠳࠭℅"))[0])
    except ValueError as e:
        logger.error(bstack11ll1ll_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡴࡴࡶࡦࡴࡷ࡭ࡳ࡭ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡸࡨࡶࡸ࡯࡯࡯ࠤ℆") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack11ll1ll_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭ℇ")):
        logger.warning(bstack11ll1ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥ℈"))
        return False
    if bstack1llll1l11l1l_opy_ < bstack1llll1l1ll1l_opy_.bstack1l111111lll_opy_:
        logger.warning(bstack1lll1ll1l11_opy_ (u"ࠨࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡸࡥࡲࡷ࡬ࡶࡪࡹࠠࡄࡪࡵࡳࡲ࡫ࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡽࡆࡓࡓ࡙ࡔࡂࡐࡗࡗ࠳ࡓࡉࡏࡋࡐ࡙ࡒࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡗࡓࡔࡔࡘࡔࡆࡆࡢࡇࡍࡘࡏࡎࡇࡢ࡚ࡊࡘࡓࡊࡑࡑࢁࠥࡵࡲࠡࡪ࡬࡫࡭࡫ࡲ࠯ࠩ℉"))
        return False
    if chrome_options and any(bstack11ll1ll_opy_ (u"ࠩ࠰࠱࡭࡫ࡡࡥ࡮ࡨࡷࡸ࠭ℊ") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack11ll1ll_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧℋ"))
        return False
    return True
  except Exception as e:
    logger.error(bstack11ll1ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣ࡭ࡳࠦࡣࡩࡧࡦ࡯࡮ࡴࡧࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡷࡺࡶࡰࡰࡴࡷࠤ࡫ࡵࡲࠡ࡮ࡲࡧࡦࡲࠠࡄࡪࡵࡳࡲ࡫࠺ࠡࠤℌ") + str(e))
    return False
def bstack1ll1lll11l_opy_(bstack111ll1lll1_opy_, config):
    try:
      bstack1l1111lllll_opy_ = bstack11ll1ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬℍ") in config and config[bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ℎ")] == True
      bstack1llll1l11l11_opy_ = bstack11ll1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫℏ") in config and str(config[bstack11ll1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬℐ")]).lower() != bstack11ll1ll_opy_ (u"ࠩࡩࡥࡱࡹࡥࠨℑ")
      if not (bstack1l1111lllll_opy_ and (not bstack1ll1llll1l_opy_(config) or bstack1llll1l11l11_opy_)):
        return bstack111ll1lll1_opy_
      bstack1llll11lllll_opy_ = bstack11lll1l1l_opy_.bstack1llll1llll11_opy_
      if bstack1llll11lllll_opy_ is None:
        logger.debug(bstack11ll1ll_opy_ (u"ࠥࡋࡴࡵࡧ࡭ࡧࠣࡧ࡭ࡸ࡯࡮ࡧࠣࡳࡵࡺࡩࡰࡰࡶࠤࡦࡸࡥࠡࡐࡲࡲࡪࠨℒ"))
        return bstack111ll1lll1_opy_
      bstack1llll1l1ll11_opy_ = int(str(bstack1111l1l1l11_opy_()).split(bstack11ll1ll_opy_ (u"ࠫ࠳࠭ℓ"))[0])
      logger.debug(bstack11ll1ll_opy_ (u"࡙ࠧࡥ࡭ࡧࡱ࡭ࡺࡳࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡦࡨࡸࡪࡩࡴࡦࡦ࠽ࠤࠧ℔") + str(bstack1llll1l1ll11_opy_) + bstack11ll1ll_opy_ (u"ࠨࠢℕ"))
      if bstack1llll1l1ll11_opy_ == 3 and isinstance(bstack111ll1lll1_opy_, dict) and bstack11ll1ll_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ№") in bstack111ll1lll1_opy_ and bstack1llll11lllll_opy_ is not None:
        if bstack11ll1ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭℗") not in bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ℘")]:
          bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪℙ")][bstack11ll1ll_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩℚ")] = {}
        if bstack11ll1ll_opy_ (u"ࠬࡧࡲࡨࡵࠪℛ") in bstack1llll11lllll_opy_:
          if bstack11ll1ll_opy_ (u"࠭ࡡࡳࡩࡶࠫℜ") not in bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧℝ")][bstack11ll1ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭℞")]:
            bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ℟")][bstack11ll1ll_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ℠")][bstack11ll1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩ℡")] = []
          for arg in bstack1llll11lllll_opy_[bstack11ll1ll_opy_ (u"ࠬࡧࡲࡨࡵࠪ™")]:
            if arg not in bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭℣")][bstack11ll1ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬℤ")][bstack11ll1ll_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭℥")]:
              bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩΩ")][bstack11ll1ll_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ℧")][bstack11ll1ll_opy_ (u"ࠫࡦࡸࡧࡴࠩℨ")].append(arg)
        if bstack11ll1ll_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ℩") in bstack1llll11lllll_opy_:
          if bstack11ll1ll_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪK") not in bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧÅ")][bstack11ll1ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ℬ")]:
            bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩℭ")][bstack11ll1ll_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ℮")][bstack11ll1ll_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨℯ")] = []
          for ext in bstack1llll11lllll_opy_[bstack11ll1ll_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩℰ")]:
            if ext not in bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ℱ")][bstack11ll1ll_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬℲ")][bstack11ll1ll_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬℳ")]:
              bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩℴ")][bstack11ll1ll_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨℵ")][bstack11ll1ll_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨℶ")].append(ext)
        if bstack11ll1ll_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫℷ") in bstack1llll11lllll_opy_:
          if bstack11ll1ll_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬℸ") not in bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧℹ")][bstack11ll1ll_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭℺")]:
            bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ℻")][bstack11ll1ll_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨℼ")][bstack11ll1ll_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪℽ")] = {}
          bstack1111ll111l1_opy_(bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬℾ")][bstack11ll1ll_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫℿ")][bstack11ll1ll_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭⅀")],
                    bstack1llll11lllll_opy_[bstack11ll1ll_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ⅁")])
        os.environ[bstack11ll1ll_opy_ (u"ࠩࡌࡗࡤࡔࡏࡏࡡࡅࡗ࡙ࡇࡃࡌࡡࡌࡒࡋࡘࡁࡠࡃ࠴࠵࡞ࡥࡓࡆࡕࡖࡍࡔࡔࠧ⅂")] = bstack11ll1ll_opy_ (u"ࠪࡸࡷࡻࡥࠨ⅃")
        return bstack111ll1lll1_opy_
      else:
        chrome_options = None
        if isinstance(bstack111ll1lll1_opy_, ChromeOptions):
          chrome_options = bstack111ll1lll1_opy_
        elif isinstance(bstack111ll1lll1_opy_, dict):
          for value in bstack111ll1lll1_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack111ll1lll1_opy_, dict):
            bstack111ll1lll1_opy_[bstack11ll1ll_opy_ (u"ࠫࡴࡶࡴࡪࡱࡱࡷࠬ⅄")] = chrome_options
          else:
            bstack111ll1lll1_opy_ = chrome_options
        if bstack1llll11lllll_opy_ is not None:
          if bstack11ll1ll_opy_ (u"ࠬࡧࡲࡨࡵࠪⅅ") in bstack1llll11lllll_opy_:
                bstack1llll1lll1ll_opy_ = chrome_options.arguments or []
                new_args = bstack1llll11lllll_opy_[bstack11ll1ll_opy_ (u"࠭ࡡࡳࡩࡶࠫⅆ")]
                for arg in new_args:
                    if arg not in bstack1llll1lll1ll_opy_:
                        chrome_options.add_argument(arg)
          if bstack11ll1ll_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫⅇ") in bstack1llll11lllll_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack11ll1ll_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬⅈ"), [])
                bstack1llll1l111ll_opy_ = bstack1llll11lllll_opy_[bstack11ll1ll_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ⅉ")]
                for extension in bstack1llll1l111ll_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack11ll1ll_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ⅊") in bstack1llll11lllll_opy_:
                bstack1llll1ll1ll1_opy_ = chrome_options.experimental_options.get(bstack11ll1ll_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⅋"), {})
                bstack1llll1ll11l1_opy_ = bstack1llll11lllll_opy_[bstack11ll1ll_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⅌")]
                bstack1111ll111l1_opy_(bstack1llll1ll1ll1_opy_, bstack1llll1ll11l1_opy_)
                chrome_options.add_experimental_option(bstack11ll1ll_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ⅍"), bstack1llll1ll1ll1_opy_)
        os.environ[bstack11ll1ll_opy_ (u"ࠧࡊࡕࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘࡋࡓࡔࡋࡒࡒࠬⅎ")] = bstack11ll1ll_opy_ (u"ࠨࡶࡵࡹࡪ࠭⅏")
        return bstack111ll1lll1_opy_
    except Exception as e:
      logger.error(bstack11ll1ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡢࡦࡧ࡭ࡳ࡭ࠠ࡯ࡱࡱ࠱ࡇ࡙ࠠࡪࡰࡩࡶࡦࠦࡡ࠲࠳ࡼࠤࡨ࡮ࡲࡰ࡯ࡨࠤࡴࡶࡴࡪࡱࡱࡷ࠿ࠦࠢ⅐") + str(e))
      return bstack111ll1lll1_opy_