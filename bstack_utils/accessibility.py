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
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1l11l11_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l11l11lll_opy_ as bstack1llll1l11l1l_opy_, EVENTS
from bstack_utils.bstack11111ll1l_opy_ import bstack11111ll1l_opy_
from bstack_utils.helper import bstack1l111lll_opy_, bstack11llll11_opy_, bstack11111lll1l_opy_, bstack111l1ll1111_opy_, \
  bstack111l1l1lll1_opy_, bstack11l1lllll1_opy_, get_host_info, bstack111l11ll1l1_opy_, bstack1l11l1111_opy_, error_handler, bstack1111ll11l1l_opy_, bstack111l1ll11ll_opy_, bstack1ll111ll_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack11ll1111l_opy_ import get_logger
from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llll1l1l1l_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack1ll1ll1lll_opy_ = bstack1llll1l1l1l_opy_()
@error_handler(class_method=False)
def _1llll1llll1l_opy_(driver, bstack1111l1l1_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1lll11l_opy_ (u"ࠩࡲࡷࡤࡴࡡ࡮ࡧࠪ "): caps.get(bstack1lll11l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩ "), None),
        bstack1lll11l_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ "): bstack1111l1l1_opy_.get(bstack1lll11l_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ "), None),
        bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬ "): caps.get(bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ "), None),
        bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪ "): caps.get(bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ "), None)
    }
  except Exception as error:
    logger.debug(bstack1lll11l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤ࠿ࠦࠧ ") + str(error))
  return response
def on():
    if os.environ.get(bstack1lll11l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ "), None) is None or os.environ[bstack1lll11l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ ")] == bstack1lll11l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ​"):
        return False
    return True
def bstack1l1111lll1_opy_(config):
  return config.get(bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ‌"), False) or any([p.get(bstack1lll11l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ‍"), False) == True for p in config.get(bstack1lll11l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ‎"), [])])
def bstack1111l111l_opy_(config, bstack11lll1l11_opy_):
  try:
    bstack1llll1l11lll_opy_ = config.get(bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ‏"), False)
    if int(bstack11lll1l11_opy_) < len(config.get(bstack1lll11l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧ‐"), [])) and config[bstack1lll11l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ‑")][bstack11lll1l11_opy_]:
      bstack1llll1lll11l_opy_ = config[bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ‒")][bstack11lll1l11_opy_].get(bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ–"), None)
    else:
      bstack1llll1lll11l_opy_ = config.get(bstack1lll11l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ—"), None)
    if bstack1llll1lll11l_opy_ != None:
      bstack1llll1l11lll_opy_ = bstack1llll1lll11l_opy_
    bstack1llll1l1ll1l_opy_ = os.getenv(bstack1lll11l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ―")) is not None and len(os.getenv(bstack1lll11l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨ‖"))) > 0 and os.getenv(bstack1lll11l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ‗")) != bstack1lll11l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪ‘")
    return bstack1llll1l11lll_opy_ and bstack1llll1l1ll1l_opy_
  except Exception as error:
    logger.debug(bstack1lll11l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡥࡳ࡫ࡩࡽ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭’") + str(error))
  return False
def bstack111111l1l1_opy_(test_tags):
  bstack1l111l1llll_opy_ = os.getenv(bstack1lll11l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ‚"))
  if bstack1l111l1llll_opy_ is None:
    return True
  bstack1l111l1llll_opy_ = json.loads(bstack1l111l1llll_opy_)
  try:
    include_tags = bstack1l111l1llll_opy_[bstack1lll11l_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭‛")] if bstack1lll11l_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ“") in bstack1l111l1llll_opy_ and isinstance(bstack1l111l1llll_opy_[bstack1lll11l_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ”")], list) else []
    exclude_tags = bstack1l111l1llll_opy_[bstack1lll11l_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ„")] if bstack1lll11l_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ‟") in bstack1l111l1llll_opy_ and isinstance(bstack1l111l1llll_opy_[bstack1lll11l_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ†")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1lll11l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡼࡡ࡭࡫ࡧࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡦࡴ࡮ࡪࡰࡪ࠲ࠥࡋࡲࡳࡱࡵࠤ࠿ࠦࠢ‡") + str(error))
  return False
def bstack1llll1l11ll1_opy_(config, frameworkName, bstack1llll1lll1l1_opy_, bstack1llll1llll11_opy_):
  bstack1llll1ll111l_opy_ = bstack111l1ll1111_opy_(config)
  bstack1llll1lllll1_opy_ = bstack111l1l1lll1_opy_(config)
  if bstack1llll1ll111l_opy_ is None or bstack1llll1lllll1_opy_ is None:
    logger.error(bstack1lll11l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩ•"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ‣"), bstack1lll11l_opy_ (u"ࠪࡿࢂ࠭․")))
    data = {
        bstack1lll11l_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ‥"): config[bstack1lll11l_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ…")],
        bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ‧"): config.get(bstack1lll11l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ "), os.path.basename(os.getcwd())),
        bstack1lll11l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡔࡪ࡯ࡨࠫ "): bstack1l111lll_opy_(),
        bstack1lll11l_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ‪"): config.get(bstack1lll11l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭‫"), bstack1lll11l_opy_ (u"ࠫࠬ‬")),
        bstack1lll11l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ‭"): {
            bstack1lll11l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭‮"): frameworkName,
            bstack1lll11l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ "): bstack1llll1lll1l1_opy_,
            bstack1lll11l_opy_ (u"ࠨࡵࡧ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ‰"): __version__,
            bstack1lll11l_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ‱"): bstack1lll11l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ′"),
            bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ″"): bstack1lll11l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧ‴"),
            bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭‵"): bstack1llll1llll11_opy_
        },
        bstack1lll11l_opy_ (u"ࠧࡴࡧࡷࡸ࡮ࡴࡧࡴࠩ‶"): settings,
        bstack1lll11l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࡅࡲࡲࡹࡸ࡯࡭ࠩ‷"): bstack111l11ll1l1_opy_(),
        bstack1lll11l_opy_ (u"ࠩࡦ࡭ࡎࡴࡦࡰࠩ‸"): bstack11l1lllll1_opy_(),
        bstack1lll11l_opy_ (u"ࠪ࡬ࡴࡹࡴࡊࡰࡩࡳࠬ‹"): get_host_info(),
        bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭›"): bstack11111lll1l_opy_(config)
    }
    headers = {
        bstack1lll11l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ※"): bstack1lll11l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ‼"),
    }
    config = {
        bstack1lll11l_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ‽"): (bstack1llll1ll111l_opy_, bstack1llll1lllll1_opy_),
        bstack1lll11l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ‾"): headers
    }
    response = bstack1l11l1111_opy_(bstack1lll11l_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ‿"), bstack1llll1l11l1l_opy_ + bstack1lll11l_opy_ (u"ࠪ࠳ࡻ࠸࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵࠪ⁀"), data, config)
    bstack1llll1l1llll_opy_ = response.json()
    if bstack1llll1l1llll_opy_[bstack1lll11l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ⁁")]:
      parsed = json.loads(os.getenv(bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭⁂"), bstack1lll11l_opy_ (u"࠭ࡻࡾࠩ⁃")))
      parsed[bstack1lll11l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁄")] = bstack1llll1l1llll_opy_[bstack1lll11l_opy_ (u"ࠨࡦࡤࡸࡦ࠭⁅")][bstack1lll11l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⁆")]
      os.environ[bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ⁇")] = json.dumps(parsed)
      bstack11111ll1l_opy_.bstack1l11llllll_opy_(bstack1llll1l1llll_opy_[bstack1lll11l_opy_ (u"ࠫࡩࡧࡴࡢࠩ⁈")][bstack1lll11l_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭⁉")])
      bstack11111ll1l_opy_.bstack1lllll1111l1_opy_(bstack1llll1l1llll_opy_[bstack1lll11l_opy_ (u"࠭ࡤࡢࡶࡤࠫ⁊")][bstack1lll11l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩ⁋")])
      bstack11111ll1l_opy_.store()
      return bstack1llll1l1llll_opy_[bstack1lll11l_opy_ (u"ࠨࡦࡤࡸࡦ࠭⁌")][bstack1lll11l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡖࡲ࡯ࡪࡴࠧ⁍")], bstack1llll1l1llll_opy_[bstack1lll11l_opy_ (u"ࠪࡨࡦࡺࡡࠨ⁎")][bstack1lll11l_opy_ (u"ࠫ࡮ࡪࠧ⁏")]
    else:
      logger.error(bstack1lll11l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥ࠭⁐") + bstack1llll1l1llll_opy_[bstack1lll11l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ⁑")])
      if bstack1llll1l1llll_opy_[bstack1lll11l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⁒")] == bstack1lll11l_opy_ (u"ࠨࡋࡱࡺࡦࡲࡩࡥࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡳࡥࡸࡹࡥࡥ࠰ࠪ⁓"):
        for bstack1llll1l1lll1_opy_ in bstack1llll1l1llll_opy_[bstack1lll11l_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩ⁔")]:
          logger.error(bstack1llll1l1lll1_opy_[bstack1lll11l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ⁕")])
      return None, None
  except Exception as error:
    logger.error(bstack1lll11l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠧ⁖") +  str(error))
    return None, None
def bstack1llll1l1ll11_opy_():
  if os.getenv(bstack1lll11l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ⁗")) is None:
    return {
        bstack1lll11l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭⁘"): bstack1lll11l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭⁙"),
        bstack1lll11l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ⁚"): bstack1lll11l_opy_ (u"ࠩࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣ࡬ࡦࡪࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠨ⁛")
    }
  data = {bstack1lll11l_opy_ (u"ࠪࡩࡳࡪࡔࡪ࡯ࡨࠫ⁜"): bstack1l111lll_opy_()}
  headers = {
      bstack1lll11l_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫ⁝"): bstack1lll11l_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥ࠭⁞") + os.getenv(bstack1lll11l_opy_ (u"ࠨࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠦ ")),
      bstack1lll11l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭⁠"): bstack1lll11l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ⁡")
  }
  response = bstack1l11l1111_opy_(bstack1lll11l_opy_ (u"ࠩࡓ࡙࡙࠭⁢"), bstack1llll1l11l1l_opy_ + bstack1lll11l_opy_ (u"ࠪ࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹ࠯ࡴࡶࡲࡴࠬ⁣"), data, { bstack1lll11l_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ⁤"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1lll11l_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰࠣࡱࡦࡸ࡫ࡦࡦࠣࡥࡸࠦࡣࡰ࡯ࡳࡰࡪࡺࡥࡥࠢࡤࡸࠥࠨ⁥") + bstack11llll11_opy_().isoformat() + bstack1lll11l_opy_ (u"࡚࠭ࠨ⁦"))
      return {bstack1lll11l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⁧"): bstack1lll11l_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ⁨"), bstack1lll11l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⁩"): bstack1lll11l_opy_ (u"ࠪࠫ⁪")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1lll11l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡤࡱࡰࡴࡱ࡫ࡴࡪࡱࡱࠤࡴ࡬ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡘࡪࡹࡴࠡࡔࡸࡲ࠿ࠦࠢ⁫") + str(error))
    return {
        bstack1lll11l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⁬"): bstack1lll11l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ⁭"),
        bstack1lll11l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⁮"): str(error)
    }
def bstack1llll1ll11l1_opy_(bstack1llll1l1l1l1_opy_):
    return re.match(bstack1lll11l_opy_ (u"ࡳࠩࡡࡠࡩ࠱ࠨ࡝࠰࡟ࡨ࠰࠯࠿ࠥࠩ⁯"), bstack1llll1l1l1l1_opy_.strip()) is not None
def bstack111l1l1111_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1llllll_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1llllll_opy_ = desired_capabilities
        else:
          bstack1llll1llllll_opy_ = {}
        bstack1l1111l111l_opy_ = (bstack1llll1llllll_opy_.get(bstack1lll11l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨ⁰"), bstack1lll11l_opy_ (u"ࠪࠫⁱ")).lower() or caps.get(bstack1lll11l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪ⁲"), bstack1lll11l_opy_ (u"ࠬ࠭⁳")).lower())
        if bstack1l1111l111l_opy_ == bstack1lll11l_opy_ (u"࠭ࡩࡰࡵࠪ⁴"):
            return True
        if bstack1l1111l111l_opy_ == bstack1lll11l_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࠨ⁵"):
            bstack1l1111l1ll1_opy_ = str(float(caps.get(bstack1lll11l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ⁶")) or bstack1llll1llllll_opy_.get(bstack1lll11l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁷"), {}).get(bstack1lll11l_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁸"),bstack1lll11l_opy_ (u"ࠫࠬ⁹"))))
            if bstack1l1111l111l_opy_ == bstack1lll11l_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩ࠭⁺") and int(bstack1l1111l1ll1_opy_.split(bstack1lll11l_opy_ (u"࠭࠮ࠨ⁻"))[0]) < float(bstack11l1l11ll11_opy_):
                logger.warning(str(bstack11l11lll1ll_opy_))
                return False
            return True
        bstack1l111l1111l_opy_ = caps.get(bstack1lll11l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁼"), {}).get(bstack1lll11l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ⁽"), caps.get(bstack1lll11l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ⁾"), bstack1lll11l_opy_ (u"ࠪࠫⁿ")))
        if bstack1l111l1111l_opy_:
            logger.warning(bstack1lll11l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡉ࡫ࡳ࡬ࡶࡲࡴࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣ₀"))
            return False
        browser = caps.get(bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ₁"), bstack1lll11l_opy_ (u"࠭ࠧ₂")).lower() or bstack1llll1llllll_opy_.get(bstack1lll11l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ₃"), bstack1lll11l_opy_ (u"ࠨࠩ₄")).lower()
        if browser != bstack1lll11l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩ₅"):
            logger.warning(bstack1lll11l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ₆"))
            return False
        browser_version = caps.get(bstack1lll11l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ₇")) or caps.get(bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ₈")) or bstack1llll1llllll_opy_.get(bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ₉")) or bstack1llll1llllll_opy_.get(bstack1lll11l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ₊"), {}).get(bstack1lll11l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ₋")) or bstack1llll1llllll_opy_.get(bstack1lll11l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ₌"), {}).get(bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ₍"))
        bstack1l111l1l111_opy_ = bstack1llll1l11l11_opy_.bstack1l111l11l1l_opy_
        bstack1llll1ll1lll_opy_ = False
        if config is not None:
          bstack1llll1ll1lll_opy_ = bstack1lll11l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ₎") in config and str(config[bstack1lll11l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ₏")]).lower() != bstack1lll11l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬₐ")
        if os.environ.get(bstack1lll11l_opy_ (u"ࠧࡊࡕࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘࡋࡓࡔࡋࡒࡒࠬₑ"), bstack1lll11l_opy_ (u"ࠨࠩₒ")).lower() == bstack1lll11l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧₓ") or bstack1llll1ll1lll_opy_:
          bstack1l111l1l111_opy_ = bstack1llll1l11l11_opy_.bstack1l11111ll1l_opy_
        if browser_version and browser_version != bstack1lll11l_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪₔ") and int(browser_version.split(bstack1lll11l_opy_ (u"ࠫ࠳࠭ₕ"))[0]) <= bstack1l111l1l111_opy_:
          logger.warning(bstack1lll1ll1l11_opy_ (u"ࠬࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦࡻ࡮࡫ࡱࡣࡦ࠷࠱ࡺࡡࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࡤࡩࡨࡳࡱࡰࡩࡤࡼࡥࡳࡵ࡬ࡳࡳࢃ࠮ࠨₖ"))
          return False
        if not options:
          bstack1l1111ll11l_opy_ = caps.get(bstack1lll11l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫₗ")) or bstack1llll1llllll_opy_.get(bstack1lll11l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬₘ"), {})
          if bstack1lll11l_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬₙ") in bstack1l1111ll11l_opy_.get(bstack1lll11l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧₚ"), []):
              logger.warning(bstack1lll11l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧₛ"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack1lll11l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨₜ") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l11ll11lll_opy_ = config.get(bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ₝"), {})
    bstack1l11ll11lll_opy_[bstack1lll11l_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠩ₞")] = os.getenv(bstack1lll11l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ₟"))
    bstack1111ll11ll1_opy_ = json.loads(os.getenv(bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ₠"), bstack1lll11l_opy_ (u"ࠩࡾࢁࠬ₡"))).get(bstack1lll11l_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ₢"))
    if not config[bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭₣")].get(bstack1lll11l_opy_ (u"ࠧࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ₤")):
      if bstack1lll11l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ₥") in caps:
        caps[bstack1lll11l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ₦")][bstack1lll11l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ₧")] = bstack1l11ll11lll_opy_
        caps[bstack1lll11l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ₨")][bstack1lll11l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ₩")][bstack1lll11l_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ₪")] = bstack1111ll11ll1_opy_
      else:
        caps[bstack1lll11l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ₫")] = bstack1l11ll11lll_opy_
        caps[bstack1lll11l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ€")][bstack1lll11l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ₭")] = bstack1111ll11ll1_opy_
  except Exception as error:
    logger.debug(bstack1lll11l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡪࡺࡴࡪࡰࡪࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠮ࠡࡇࡵࡶࡴࡸ࠺ࠡࠤ₮") +  str(error))
def bstack1111l11l1l_opy_(driver, bstack1llll1l1l1ll_opy_):
  try:
    setattr(driver, bstack1lll11l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩ₯"), True)
    session = driver.session_id
    if session:
      bstack1llll1l1l111_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1l1l111_opy_ = False
      bstack1llll1l1l111_opy_ = url.scheme in [bstack1lll11l_opy_ (u"ࠥ࡬ࡹࡺࡰࠣ₰"), bstack1lll11l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥ₱")]
      if bstack1llll1l1l111_opy_:
        if bstack1llll1l1l1ll_opy_:
          logger.info(bstack1lll11l_opy_ (u"࡙ࠧࡥࡵࡷࡳࠤ࡫ࡵࡲࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡫ࡥࡸࠦࡳࡵࡣࡵࡸࡪࡪ࠮ࠡࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡣࡧࡪ࡭ࡳࠦ࡭ࡰ࡯ࡨࡲࡹࡧࡲࡪ࡮ࡼ࠲ࠧ₲"))
      return bstack1llll1l1l1ll_opy_
  except Exception as e:
    logger.error(bstack1lll11l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤ₳") + str(e))
    return False
def bstack111lll11_opy_(driver, name, path):
  try:
    bstack1l11111l11l_opy_ = {
        bstack1lll11l_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧ₴"): threading.current_thread().current_test_uuid,
        bstack1lll11l_opy_ (u"ࠨࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭₵"): os.environ.get(bstack1lll11l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ₶"), bstack1lll11l_opy_ (u"ࠪࠫ₷")),
        bstack1lll11l_opy_ (u"ࠫࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠨ₸"): os.environ.get(bstack1lll11l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ₹"), bstack1lll11l_opy_ (u"࠭ࠧ₺"))
    }
    bstack1ll111111l1_opy_ = bstack1ll1ll1lll_opy_.bstack1ll111l1ll1_opy_(EVENTS.bstack1l11111ll1_opy_.value)
    logger.debug(bstack1lll11l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡥࡻ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪ₻"))
    try:
      if (bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ₼"), None) and bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ₽"), None)):
        scripts = {bstack1lll11l_opy_ (u"ࠪࡷࡨࡧ࡮ࠨ₾"): bstack11111ll1l_opy_.perform_scan}
        bstack1llll1ll1l1l_opy_ = json.loads(scripts[bstack1lll11l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ₿")].replace(bstack1lll11l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ⃀"), bstack1lll11l_opy_ (u"ࠨࠢ⃁")))
        bstack1llll1ll1l1l_opy_[bstack1lll11l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ⃂")][bstack1lll11l_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨ⃃")] = None
        scripts[bstack1lll11l_opy_ (u"ࠤࡶࡧࡦࡴࠢ⃄")] = bstack1lll11l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨ⃅") + json.dumps(bstack1llll1ll1l1l_opy_)
        bstack11111ll1l_opy_.bstack1l11llllll_opy_(scripts)
        bstack11111ll1l_opy_.store()
        logger.debug(driver.execute_script(bstack11111ll1l_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11111ll1l_opy_.perform_scan, {bstack1lll11l_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠦ⃆"): name}))
      bstack1ll1ll1lll_opy_.end(EVENTS.bstack1l11111ll1_opy_.value, bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ⃇"), bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ⃈"), True, None)
    except Exception as error:
      bstack1ll1ll1lll_opy_.end(EVENTS.bstack1l11111ll1_opy_.value, bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ⃉"), bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ⃊"), False, str(error))
    bstack1ll111111l1_opy_ = bstack1ll1ll1lll_opy_.bstack11ll1l111ll_opy_(EVENTS.bstack1l1111ll111_opy_.value)
    bstack1ll1ll1lll_opy_.mark(bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ⃋"))
    try:
      if (bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ⃌"), None) and bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭⃍"), None)):
        scripts = {bstack1lll11l_opy_ (u"ࠬࡹࡣࡢࡰࠪ⃎"): bstack11111ll1l_opy_.perform_scan}
        bstack1llll1ll1l1l_opy_ = json.loads(scripts[bstack1lll11l_opy_ (u"ࠨࡳࡤࡣࡱࠦ⃏")].replace(bstack1lll11l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࠥ⃐"), bstack1lll11l_opy_ (u"ࠣࠤ⃑")))
        bstack1llll1ll1l1l_opy_[bstack1lll11l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷ⃒ࠬ")][bstack1lll11l_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦ⃓ࠪ")] = None
        scripts[bstack1lll11l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ⃔")] = bstack1lll11l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ⃕") + json.dumps(bstack1llll1ll1l1l_opy_)
        bstack11111ll1l_opy_.bstack1l11llllll_opy_(scripts)
        bstack11111ll1l_opy_.store()
        logger.debug(driver.execute_script(bstack11111ll1l_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11111ll1l_opy_.bstack1lllll111111_opy_, bstack1l11111l11l_opy_))
      bstack1ll1ll1lll_opy_.end(bstack1ll111111l1_opy_, bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ⃖"), bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ⃗"),True, None)
    except Exception as error:
      bstack1ll1ll1lll_opy_.end(bstack1ll111111l1_opy_, bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴ⃘ࠣ"), bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠤ࠽ࡩࡳࡪ⃙ࠢ"),False, str(error))
    logger.info(bstack1lll11l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨ⃚"))
  except Exception as bstack1l1111ll1ll_opy_:
    logger.error(bstack1lll11l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨ⃛") + str(path) + bstack1lll11l_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢ⃜") + str(bstack1l1111ll1ll_opy_))
def bstack1llll1ll11ll_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack1lll11l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ⃝")) and str(caps.get(bstack1lll11l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ⃞"))).lower() == bstack1lll11l_opy_ (u"ࠣࡣࡱࡨࡷࡵࡩࡥࠤ⃟"):
        bstack1l1111l1ll1_opy_ = caps.get(bstack1lll11l_opy_ (u"ࠤࡤࡴࡵ࡯ࡵ࡮࠼ࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ⃠")) or caps.get(bstack1lll11l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ⃡"))
        if bstack1l1111l1ll1_opy_ and int(str(bstack1l1111l1ll1_opy_)) < bstack11l1l11ll11_opy_:
            return False
    return True
def bstack1111111l1_opy_(config):
  if bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⃢") in config:
        return config[bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⃣")]
  for platform in config.get(bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⃤"), []):
      if bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿ⃥ࠧ") in platform:
          return platform[bstack1lll11l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⃦")]
  return None
def bstack1llll1l1l1_opy_(bstack11l111lll1_opy_):
  try:
    browser_name = bstack11l111lll1_opy_[bstack1lll11l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨ⃧")]
    browser_version = bstack11l111lll1_opy_[bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲ⃨ࠬ")]
    chrome_options = bstack11l111lll1_opy_[bstack1lll11l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡣࡴࡶࡴࡪࡱࡱࡷࠬ⃩")]
    try:
        bstack1llll1ll1l11_opy_ = int(browser_version.split(bstack1lll11l_opy_ (u"ࠬ࠴⃪ࠧ"))[0])
    except ValueError as e:
        logger.error(bstack1lll11l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡨࡵ࡮ࡷࡧࡵࡸ࡮ࡴࡧࠡࡤࡵࡳࡼࡹࡥࡳࠢࡹࡩࡷࡹࡩࡰࡰ⃫ࠥ") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack1lll11l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫⃬ࠧ")):
        logger.warning(bstack1lll11l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱⃭ࠦ"))
        return False
    if bstack1llll1ll1l11_opy_ < bstack1llll1l11l11_opy_.bstack1l11111ll1l_opy_:
        logger.warning(bstack1lll1ll1l11_opy_ (u"ࠩࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡳࠡࡅ࡫ࡶࡴࡳࡥࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡾࡇࡔࡔࡓࡕࡃࡑࡘࡘ࠴ࡍࡊࡐࡌࡑ࡚ࡓ࡟ࡏࡑࡑࡣࡇ࡙ࡔࡂࡅࡎࡣࡎࡔࡆࡓࡃࡢࡅ࠶࠷࡙ࡠࡕࡘࡔࡕࡕࡒࡕࡇࡇࡣࡈࡎࡒࡐࡏࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࢂࠦ࡯ࡳࠢ࡫࡭࡬࡮ࡥࡳ࠰⃮ࠪ"))
        return False
    if chrome_options and any(bstack1lll11l_opy_ (u"ࠪ࠱࠲࡮ࡥࡢࡦ࡯ࡩࡸࡹ⃯ࠧ") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack1lll11l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡰࡰࠣࡰࡪ࡭ࡡࡤࡻࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠤࡘࡽࡩࡵࡥ࡫ࠤࡹࡵࠠ࡯ࡧࡺࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨࠤࡴࡸࠠࡢࡸࡲ࡭ࡩࠦࡵࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠨ⃰"))
        return False
    return True
  except Exception as e:
    logger.error(bstack1lll11l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡤࡪࡨࡧࡰ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡻࡰࡱࡱࡵࡸࠥ࡬࡯ࡳࠢ࡯ࡳࡨࡧ࡬ࠡࡅ࡫ࡶࡴࡳࡥ࠻ࠢࠥ⃱") + str(e))
    return False
def bstack11l1ll11l_opy_(bstack11l1l11ll1_opy_, config):
    try:
      bstack1l1111l1lll_opy_ = bstack1lll11l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⃲") in config and config[bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃳")] == True
      bstack1llll1ll1lll_opy_ = bstack1lll11l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ⃴") in config and str(config[bstack1lll11l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭⃵")]).lower() != bstack1lll11l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ⃶")
      if not (bstack1l1111l1lll_opy_ and (not bstack11111lll1l_opy_(config) or bstack1llll1ll1lll_opy_)):
        return bstack11l1l11ll1_opy_
      bstack1llll1l1l11l_opy_ = bstack11111ll1l_opy_.bstack1lllll11111l_opy_
      if bstack1llll1l1l11l_opy_ is None:
        logger.debug(bstack1lll11l_opy_ (u"ࠦࡌࡵ࡯ࡨ࡮ࡨࠤࡨ࡮ࡲࡰ࡯ࡨࠤࡴࡶࡴࡪࡱࡱࡷࠥࡧࡲࡦࠢࡑࡳࡳ࡫ࠢ⃷"))
        return bstack11l1l11ll1_opy_
      bstack1llll1ll1ll1_opy_ = int(str(bstack111l1ll11ll_opy_()).split(bstack1lll11l_opy_ (u"ࠬ࠴ࠧ⃸"))[0])
      logger.debug(bstack1lll11l_opy_ (u"ࠨࡓࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡧࡩࡹ࡫ࡣࡵࡧࡧ࠾ࠥࠨ⃹") + str(bstack1llll1ll1ll1_opy_) + bstack1lll11l_opy_ (u"ࠢࠣ⃺"))
      if bstack1llll1ll1ll1_opy_ == 3 and isinstance(bstack11l1l11ll1_opy_, dict) and bstack1lll11l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃻") in bstack11l1l11ll1_opy_ and bstack1llll1l1l11l_opy_ is not None:
        if bstack1lll11l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃼") not in bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃽")]:
          bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃾")][bstack1lll11l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃿")] = {}
        if bstack1lll11l_opy_ (u"࠭ࡡࡳࡩࡶࠫ℀") in bstack1llll1l1l11l_opy_:
          if bstack1lll11l_opy_ (u"ࠧࡢࡴࡪࡷࠬ℁") not in bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨℂ")][bstack1lll11l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ℃")]:
            bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ℄")][bstack1lll11l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ℅")][bstack1lll11l_opy_ (u"ࠬࡧࡲࡨࡵࠪ℆")] = []
          for arg in bstack1llll1l1l11l_opy_[bstack1lll11l_opy_ (u"࠭ࡡࡳࡩࡶࠫℇ")]:
            if arg not in bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ℈")][bstack1lll11l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭℉")][bstack1lll11l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧℊ")]:
              bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪℋ")][bstack1lll11l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩℌ")][bstack1lll11l_opy_ (u"ࠬࡧࡲࡨࡵࠪℍ")].append(arg)
        if bstack1lll11l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪℎ") in bstack1llll1l1l11l_opy_:
          if bstack1lll11l_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫℏ") not in bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨℐ")][bstack1lll11l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧℑ")]:
            bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪℒ")][bstack1lll11l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩℓ")][bstack1lll11l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ℔")] = []
          for ext in bstack1llll1l1l11l_opy_[bstack1lll11l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪℕ")]:
            if ext not in bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ№")][bstack1lll11l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭℗")][bstack1lll11l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭℘")]:
              bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪℙ")][bstack1lll11l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩℚ")][bstack1lll11l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩℛ")].append(ext)
        if bstack1lll11l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬℜ") in bstack1llll1l1l11l_opy_:
          if bstack1lll11l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭ℝ") not in bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ℞")][bstack1lll11l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ℟")]:
            bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ℠")][bstack1lll11l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ℡")][bstack1lll11l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ™")] = {}
          bstack1111ll11l1l_opy_(bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭℣")][bstack1lll11l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬℤ")][bstack1lll11l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ℥")],
                    bstack1llll1l1l11l_opy_[bstack1lll11l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨΩ")])
        os.environ[bstack1lll11l_opy_ (u"ࠪࡍࡘࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡇࡖࡗࡎࡕࡎࠨ℧")] = bstack1lll11l_opy_ (u"ࠫࡹࡸࡵࡦࠩℨ")
        return bstack11l1l11ll1_opy_
      else:
        chrome_options = None
        if isinstance(bstack11l1l11ll1_opy_, ChromeOptions):
          chrome_options = bstack11l1l11ll1_opy_
        elif isinstance(bstack11l1l11ll1_opy_, dict):
          for value in bstack11l1l11ll1_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack11l1l11ll1_opy_, dict):
            bstack11l1l11ll1_opy_[bstack1lll11l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭℩")] = chrome_options
          else:
            bstack11l1l11ll1_opy_ = chrome_options
        if bstack1llll1l1l11l_opy_ is not None:
          if bstack1lll11l_opy_ (u"࠭ࡡࡳࡩࡶࠫK") in bstack1llll1l1l11l_opy_:
                bstack1llll1lll1ll_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1l1l11l_opy_[bstack1lll11l_opy_ (u"ࠧࡢࡴࡪࡷࠬÅ")]
                for arg in new_args:
                    if arg not in bstack1llll1lll1ll_opy_:
                        chrome_options.add_argument(arg)
          if bstack1lll11l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬℬ") in bstack1llll1l1l11l_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack1lll11l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ℭ"), [])
                bstack1llll1lll111_opy_ = bstack1llll1l1l11l_opy_[bstack1lll11l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧ℮")]
                for extension in bstack1llll1lll111_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack1lll11l_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪℯ") in bstack1llll1l1l11l_opy_:
                bstack1llll1ll1111_opy_ = chrome_options.experimental_options.get(bstack1lll11l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫℰ"), {})
                bstack1llll1l111ll_opy_ = bstack1llll1l1l11l_opy_[bstack1lll11l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬℱ")]
                bstack1111ll11l1l_opy_(bstack1llll1ll1111_opy_, bstack1llll1l111ll_opy_)
                chrome_options.add_experimental_option(bstack1lll11l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭Ⅎ"), bstack1llll1ll1111_opy_)
        os.environ[bstack1lll11l_opy_ (u"ࠨࡋࡖࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡅࡔࡕࡌࡓࡓ࠭ℳ")] = bstack1lll11l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧℴ")
        return bstack11l1l11ll1_opy_
    except Exception as e:
      logger.error(bstack1lll11l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡣࡧࡨ࡮ࡴࡧࠡࡰࡲࡲ࠲ࡈࡓࠡ࡫ࡱࡪࡷࡧࠠࡢ࠳࠴ࡽࠥࡩࡨࡳࡱࡰࡩࠥࡵࡰࡵ࡫ࡲࡲࡸࡀࠠࠣℵ") + str(e))
      return bstack11l1l11ll1_opy_