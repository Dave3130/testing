# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1lllll111l1l_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l1l1l11l1_opy_ as bstack1llll1ll1l11_opy_, EVENTS
from bstack_utils.bstack1l1ll1lll1_opy_ import bstack1l1ll1lll1_opy_
from bstack_utils.helper import bstack1l1l1lll_opy_, bstack1ll1111l_opy_, bstack11l11ll11_opy_, bstack111l11l11l1_opy_, \
  bstack111l11ll11l_opy_, bstack1ll1l11l1_opy_, get_host_info, bstack1111l1ll1ll_opy_, bstack1l11lllll_opy_, error_handler, bstack111l1111l11_opy_, bstack1111llll11l_opy_, bstack1l1l1l1l_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack1ll1ll111_opy_ import get_logger
from bstack_utils.bstack111l11llll_opy_ import bstack1llll1l1l11_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack111l11llll_opy_ = bstack1llll1l1l11_opy_()
@error_handler(class_method=False)
def _1lllll111l11_opy_(driver, bstack111l11l1_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack1ll1l_opy_ (u"ࠩࡲࡷࡤࡴࡡ࡮ࡧࠪ῁"): caps.get(bstack1ll1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩῂ"), None),
        bstack1ll1l_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨῃ"): bstack111l11l1_opy_.get(bstack1ll1l_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨῄ"), None),
        bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬ῅"): caps.get(bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬῆ"), None),
        bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪῇ"): caps.get(bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪῈ"), None)
    }
  except Exception as error:
    logger.debug(bstack1ll1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤ࠿ࠦࠧΈ") + str(error))
  return response
def on():
    if os.environ.get(bstack1ll1l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩῊ"), None) is None or os.environ[bstack1ll1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪΉ")] == bstack1ll1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦῌ"):
        return False
    return True
def bstack111ll11ll1_opy_(config):
  return config.get(bstack1ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ῍"), False) or any([p.get(bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ῎"), False) == True for p in config.get(bstack1ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬ῏"), [])])
def bstack1l1l1ll1l_opy_(config, bstack111l1lll1_opy_):
  try:
    bstack1lllll11ll11_opy_ = config.get(bstack1ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪῐ"), False)
    if int(bstack111l1lll1_opy_) < len(config.get(bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧῑ"), [])) and config[bstack1ll1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨῒ")][bstack111l1lll1_opy_]:
      bstack1llll1lllll1_opy_ = config[bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩΐ")][bstack111l1lll1_opy_].get(bstack1ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ῔"), None)
    else:
      bstack1llll1lllll1_opy_ = config.get(bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ῕"), None)
    if bstack1llll1lllll1_opy_ != None:
      bstack1lllll11ll11_opy_ = bstack1llll1lllll1_opy_
    bstack1llll1ll1ll1_opy_ = os.getenv(bstack1ll1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧῖ")) is not None and len(os.getenv(bstack1ll1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨῗ"))) > 0 and os.getenv(bstack1ll1l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩῘ")) != bstack1ll1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪῙ")
    return bstack1lllll11ll11_opy_ and bstack1llll1ll1ll1_opy_
  except Exception as error:
    logger.debug(bstack1ll1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡥࡳ࡫ࡩࡽ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭Ὶ") + str(error))
  return False
def bstack1l11l1llll_opy_(test_tags):
  bstack1l111l1l1l1_opy_ = os.getenv(bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨΊ"))
  if bstack1l111l1l1l1_opy_ is None:
    return True
  bstack1l111l1l1l1_opy_ = json.loads(bstack1l111l1l1l1_opy_)
  try:
    include_tags = bstack1l111l1l1l1_opy_[bstack1ll1l_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭῜")] if bstack1ll1l_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ῝") in bstack1l111l1l1l1_opy_ and isinstance(bstack1l111l1l1l1_opy_[bstack1ll1l_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ῞")], list) else []
    exclude_tags = bstack1l111l1l1l1_opy_[bstack1ll1l_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ῟")] if bstack1ll1l_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪῠ") in bstack1l111l1l1l1_opy_ and isinstance(bstack1l111l1l1l1_opy_[bstack1ll1l_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫῡ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack1ll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡼࡡ࡭࡫ࡧࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡦࡴ࡮ࡪࡰࡪ࠲ࠥࡋࡲࡳࡱࡵࠤ࠿ࠦࠢῢ") + str(error))
  return False
def bstack1llll1ll1lll_opy_(config, frameworkName, bstack1lllll11lll1_opy_, bstack1lllll1111ll_opy_):
  bstack1lllll11l11l_opy_ = bstack111l11l11l1_opy_(config)
  bstack1llll1lll111_opy_ = bstack111l11ll11l_opy_(config)
  if bstack1lllll11l11l_opy_ is None or bstack1llll1lll111_opy_ is None:
    logger.error(bstack1ll1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩΰ"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack1ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪῤ"), bstack1ll1l_opy_ (u"ࠪࡿࢂ࠭ῥ")))
    data = {
        bstack1ll1l_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩῦ"): config[bstack1ll1l_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪῧ")],
        bstack1ll1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩῨ"): config.get(bstack1ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪῩ"), os.path.basename(os.getcwd())),
        bstack1ll1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡔࡪ࡯ࡨࠫῪ"): bstack1l1l1lll_opy_(),
        bstack1ll1l_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧΎ"): config.get(bstack1ll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭Ῥ"), bstack1ll1l_opy_ (u"ࠫࠬ῭")),
        bstack1ll1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ΅"): {
            bstack1ll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭`"): frameworkName,
            bstack1ll1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ῰"): bstack1lllll11lll1_opy_,
            bstack1ll1l_opy_ (u"ࠨࡵࡧ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ῱"): __version__,
            bstack1ll1l_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫῲ"): bstack1ll1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪῳ"),
            bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫῴ"): bstack1ll1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧ῵"),
            bstack1ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ῶ"): bstack1lllll1111ll_opy_
        },
        bstack1ll1l_opy_ (u"ࠧࡴࡧࡷࡸ࡮ࡴࡧࡴࠩῷ"): settings,
        bstack1ll1l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࡅࡲࡲࡹࡸ࡯࡭ࠩῸ"): bstack1111l1ll1ll_opy_(),
        bstack1ll1l_opy_ (u"ࠩࡦ࡭ࡎࡴࡦࡰࠩΌ"): bstack1ll1l11l1_opy_(),
        bstack1ll1l_opy_ (u"ࠪ࡬ࡴࡹࡴࡊࡰࡩࡳࠬῺ"): get_host_info(),
        bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭Ώ"): bstack11l11ll11_opy_(config)
    }
    headers = {
        bstack1ll1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫῼ"): bstack1ll1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ´"),
    }
    config = {
        bstack1ll1l_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ῾"): (bstack1lllll11l11l_opy_, bstack1llll1lll111_opy_),
        bstack1ll1l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ῿"): headers
    }
    response = bstack1l11lllll_opy_(bstack1ll1l_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ "), bstack1llll1ll1l11_opy_ + bstack1ll1l_opy_ (u"ࠪ࠳ࡻ࠸࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵࠪ "), data, config)
    bstack1lllll111111_opy_ = response.json()
    if bstack1lllll111111_opy_[bstack1ll1l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ ")]:
      parsed = json.loads(os.getenv(bstack1ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ "), bstack1ll1l_opy_ (u"࠭ࡻࡾࠩ ")))
      parsed[bstack1ll1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ ")] = bstack1lllll111111_opy_[bstack1ll1l_opy_ (u"ࠨࡦࡤࡸࡦ࠭ ")][bstack1ll1l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ ")]
      os.environ[bstack1ll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ ")] = json.dumps(parsed)
      bstack1l1ll1lll1_opy_.bstack1l11l111ll_opy_(bstack1lllll111111_opy_[bstack1ll1l_opy_ (u"ࠫࡩࡧࡴࡢࠩ ")][bstack1ll1l_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭ ")])
      bstack1l1ll1lll1_opy_.bstack1lllll1l111l_opy_(bstack1lllll111111_opy_[bstack1ll1l_opy_ (u"࠭ࡤࡢࡶࡤࠫ​")][bstack1ll1l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩ‌")])
      bstack1l1ll1lll1_opy_.store()
      return bstack1lllll111111_opy_[bstack1ll1l_opy_ (u"ࠨࡦࡤࡸࡦ࠭‍")][bstack1ll1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡖࡲ࡯ࡪࡴࠧ‎")], bstack1lllll111111_opy_[bstack1ll1l_opy_ (u"ࠪࡨࡦࡺࡡࠨ‏")][bstack1ll1l_opy_ (u"ࠫ࡮ࡪࠧ‐")]
    else:
      logger.error(bstack1ll1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥ࠭‑") + bstack1lllll111111_opy_[bstack1ll1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ‒")])
      if bstack1lllll111111_opy_[bstack1ll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ–")] == bstack1ll1l_opy_ (u"ࠨࡋࡱࡺࡦࡲࡩࡥࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡳࡥࡸࡹࡥࡥ࠰ࠪ—"):
        for bstack1llll1llllll_opy_ in bstack1lllll111111_opy_[bstack1ll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩ―")]:
          logger.error(bstack1llll1llllll_opy_[bstack1ll1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ‖")])
      return None, None
  except Exception as error:
    logger.error(bstack1ll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠧ‗") +  str(error))
    return None, None
def bstack1llll1lll1l1_opy_():
  if os.getenv(bstack1ll1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ‘")) is None:
    return {
        bstack1ll1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭’"): bstack1ll1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭‚"),
        bstack1ll1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ‛"): bstack1ll1l_opy_ (u"ࠩࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣ࡬ࡦࡪࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠨ“")
    }
  data = {bstack1ll1l_opy_ (u"ࠪࡩࡳࡪࡔࡪ࡯ࡨࠫ”"): bstack1l1l1lll_opy_()}
  headers = {
      bstack1ll1l_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫ„"): bstack1ll1l_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥ࠭‟") + os.getenv(bstack1ll1l_opy_ (u"ࠨࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠦ†")),
      bstack1ll1l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭‡"): bstack1ll1l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ•")
  }
  response = bstack1l11lllll_opy_(bstack1ll1l_opy_ (u"ࠩࡓ࡙࡙࠭‣"), bstack1llll1ll1l11_opy_ + bstack1ll1l_opy_ (u"ࠪ࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹ࠯ࡴࡶࡲࡴࠬ․"), data, { bstack1ll1l_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ‥"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack1ll1l_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰࠣࡱࡦࡸ࡫ࡦࡦࠣࡥࡸࠦࡣࡰ࡯ࡳࡰࡪࡺࡥࡥࠢࡤࡸࠥࠨ…") + bstack1ll1111l_opy_().isoformat() + bstack1ll1l_opy_ (u"࡚࠭ࠨ‧"))
      return {bstack1ll1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ "): bstack1ll1l_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ "), bstack1ll1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ‪"): bstack1ll1l_opy_ (u"ࠪࠫ‫")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack1ll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡤࡱࡰࡴࡱ࡫ࡴࡪࡱࡱࠤࡴ࡬ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡘࡪࡹࡴࠡࡔࡸࡲ࠿ࠦࠢ‬") + str(error))
    return {
        bstack1ll1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ‭"): bstack1ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ‮"),
        bstack1ll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ "): str(error)
    }
def bstack1lllll1111l1_opy_(bstack1llll1ll1l1l_opy_):
    return re.match(bstack1ll1l_opy_ (u"ࡳࠩࡡࡠࡩ࠱ࠨ࡝࠰࡟ࡨ࠰࠯࠿ࠥࠩ‰"), bstack1llll1ll1l1l_opy_.strip()) is not None
def bstack11l1llll1_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1lll1ll_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1lll1ll_opy_ = desired_capabilities
        else:
          bstack1llll1lll1ll_opy_ = {}
        bstack1l111l1l111_opy_ = (bstack1llll1lll1ll_opy_.get(bstack1ll1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨ‱"), bstack1ll1l_opy_ (u"ࠪࠫ′")).lower() or caps.get(bstack1ll1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪ″"), bstack1ll1l_opy_ (u"ࠬ࠭‴")).lower())
        if bstack1l111l1l111_opy_ == bstack1ll1l_opy_ (u"࠭ࡩࡰࡵࠪ‵"):
            return True
        if bstack1l111l1l111_opy_ == bstack1ll1l_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࠨ‶"):
            bstack1l111lll11l_opy_ = str(float(caps.get(bstack1ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ‷")) or bstack1llll1lll1ll_opy_.get(bstack1ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ‸"), {}).get(bstack1ll1l_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭‹"),bstack1ll1l_opy_ (u"ࠫࠬ›"))))
            if bstack1l111l1l111_opy_ == bstack1ll1l_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩ࠭※") and int(bstack1l111lll11l_opy_.split(bstack1ll1l_opy_ (u"࠭࠮ࠨ‼"))[0]) < float(bstack11l1l11l1l1_opy_):
                logger.warning(str(bstack11l1l1l1111_opy_))
                return False
            return True
        bstack1l1111ll11l_opy_ = caps.get(bstack1ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ‽"), {}).get(bstack1ll1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ‾"), caps.get(bstack1ll1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ‿"), bstack1ll1l_opy_ (u"ࠪࠫ⁀")))
        if bstack1l1111ll11l_opy_:
            logger.warning(bstack1ll1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡉ࡫ࡳ࡬ࡶࡲࡴࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣ⁁"))
            return False
        browser = caps.get(bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ⁂"), bstack1ll1l_opy_ (u"࠭ࠧ⁃")).lower() or bstack1llll1lll1ll_opy_.get(bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ⁄"), bstack1ll1l_opy_ (u"ࠨࠩ⁅")).lower()
        if browser != bstack1ll1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩ⁆"):
            logger.warning(bstack1ll1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ⁇"))
            return False
        browser_version = caps.get(bstack1ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁈")) or caps.get(bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ⁉")) or bstack1llll1lll1ll_opy_.get(bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⁊")) or bstack1llll1lll1ll_opy_.get(bstack1ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁋"), {}).get(bstack1ll1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⁌")) or bstack1llll1lll1ll_opy_.get(bstack1ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁍"), {}).get(bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ⁎"))
        bstack1l111l1l11l_opy_ = bstack1lllll111l1l_opy_.bstack1l111l11l11_opy_
        bstack1llll1ll11l1_opy_ = False
        if config is not None:
          bstack1llll1ll11l1_opy_ = bstack1ll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ⁏") in config and str(config[bstack1ll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ⁐")]).lower() != bstack1ll1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ⁑")
        if os.environ.get(bstack1ll1l_opy_ (u"ࠧࡊࡕࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘࡋࡓࡔࡋࡒࡒࠬ⁒"), bstack1ll1l_opy_ (u"ࠨࠩ⁓")).lower() == bstack1ll1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⁔") or bstack1llll1ll11l1_opy_:
          bstack1l111l1l11l_opy_ = bstack1lllll111l1l_opy_.bstack1l111ll1lll_opy_
        if browser_version and browser_version != bstack1ll1l_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪ⁕") and int(browser_version.split(bstack1ll1l_opy_ (u"ࠫ࠳࠭⁖"))[0]) <= bstack1l111l1l11l_opy_:
          logger.warning(bstack1lllll1l1_opy_ (u"ࠬࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦࡻ࡮࡫ࡱࡣࡦ࠷࠱ࡺࡡࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࡤࡩࡨࡳࡱࡰࡩࡤࡼࡥࡳࡵ࡬ࡳࡳࢃ࠮ࠨ⁗"))
          return False
        if not options:
          bstack1l111lll111_opy_ = caps.get(bstack1ll1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⁘")) or bstack1llll1lll1ll_opy_.get(bstack1ll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⁙"), {})
          if bstack1ll1l_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬ⁚") in bstack1l111lll111_opy_.get(bstack1ll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ⁛"), []):
              logger.warning(bstack1ll1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧ⁜"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack1ll1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨ⁝") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l1l11111_opy_ = config.get(bstack1ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ⁞"), {})
    bstack1l1l1l11111_opy_[bstack1ll1l_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠩ ")] = os.getenv(bstack1ll1l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ⁠"))
    bstack1111lll11ll_opy_ = json.loads(os.getenv(bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ⁡"), bstack1ll1l_opy_ (u"ࠩࡾࢁࠬ⁢"))).get(bstack1ll1l_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ⁣"))
    if not config[bstack1ll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭⁤")].get(bstack1ll1l_opy_ (u"ࠧࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ⁥")):
      if bstack1ll1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ⁦") in caps:
        caps[bstack1ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁧")][bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ⁨")] = bstack1l1l1l11111_opy_
        caps[bstack1ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁩")][bstack1ll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ⁪")][bstack1ll1l_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁫")] = bstack1111lll11ll_opy_
      else:
        caps[bstack1ll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ⁬")] = bstack1l1l1l11111_opy_
        caps[bstack1ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ⁭")][bstack1ll1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ⁮")] = bstack1111lll11ll_opy_
  except Exception as error:
    logger.debug(bstack1ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡪࡺࡴࡪࡰࡪࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠮ࠡࡇࡵࡶࡴࡸ࠺ࠡࠤ⁯") +  str(error))
def bstack1lll11ll11_opy_(driver, bstack1llll1ll11ll_opy_):
  try:
    setattr(driver, bstack1ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩ⁰"), True)
    session = driver.session_id
    if session:
      bstack1lllll11l1l1_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1lllll11l1l1_opy_ = False
      bstack1lllll11l1l1_opy_ = url.scheme in [bstack1ll1l_opy_ (u"ࠥ࡬ࡹࡺࡰࠣⁱ"), bstack1ll1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥ⁲")]
      if bstack1lllll11l1l1_opy_:
        if bstack1llll1ll11ll_opy_:
          logger.info(bstack1ll1l_opy_ (u"࡙ࠧࡥࡵࡷࡳࠤ࡫ࡵࡲࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡫ࡥࡸࠦࡳࡵࡣࡵࡸࡪࡪ࠮ࠡࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡣࡧࡪ࡭ࡳࠦ࡭ࡰ࡯ࡨࡲࡹࡧࡲࡪ࡮ࡼ࠲ࠧ⁳"))
      return bstack1llll1ll11ll_opy_
  except Exception as e:
    logger.error(bstack1ll1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤ⁴") + str(e))
    return False
def bstack1lllll111_opy_(driver, name, path):
  try:
    bstack1l111l11ll1_opy_ = {
        bstack1ll1l_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧ⁵"): threading.current_thread().current_test_uuid,
        bstack1ll1l_opy_ (u"ࠨࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭⁶"): os.environ.get(bstack1ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧ⁷"), bstack1ll1l_opy_ (u"ࠪࠫ⁸")),
        bstack1ll1l_opy_ (u"ࠫࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠨ⁹"): os.environ.get(bstack1ll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ⁺"), bstack1ll1l_opy_ (u"࠭ࠧ⁻"))
    }
    bstack1l1lllll111_opy_ = bstack111l11llll_opy_.bstack1ll1ll1111l_opy_(EVENTS.bstack111l1l1l11_opy_.value)
    logger.debug(bstack1ll1l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡥࡻ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪ⁼"))
    try:
      if (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ⁽"), None) and bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ⁾"), None)):
        scripts = {bstack1ll1l_opy_ (u"ࠪࡷࡨࡧ࡮ࠨⁿ"): bstack1l1ll1lll1_opy_.perform_scan}
        bstack1lllll11l111_opy_ = json.loads(scripts[bstack1ll1l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ₀")].replace(bstack1ll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ₁"), bstack1ll1l_opy_ (u"ࠨࠢ₂")))
        bstack1lllll11l111_opy_[bstack1ll1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ₃")][bstack1ll1l_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨ₄")] = None
        scripts[bstack1ll1l_opy_ (u"ࠤࡶࡧࡦࡴࠢ₅")] = bstack1ll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨ₆") + json.dumps(bstack1lllll11l111_opy_)
        bstack1l1ll1lll1_opy_.bstack1l11l111ll_opy_(scripts)
        bstack1l1ll1lll1_opy_.store()
        logger.debug(driver.execute_script(bstack1l1ll1lll1_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1l1ll1lll1_opy_.perform_scan, {bstack1ll1l_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠦ₇"): name}))
      bstack111l11llll_opy_.end(EVENTS.bstack111l1l1l11_opy_.value, bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ₈"), bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ₉"), True, None)
    except Exception as error:
      bstack111l11llll_opy_.end(EVENTS.bstack111l1l1l11_opy_.value, bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ₊"), bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ₋"), False, str(error))
    bstack1l1lllll111_opy_ = bstack111l11llll_opy_.bstack11ll1ll111l_opy_(EVENTS.bstack1l111ll1ll1_opy_.value)
    bstack111l11llll_opy_.mark(bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ₌"))
    try:
      if (bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ₍"), None) and bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭₎"), None)):
        scripts = {bstack1ll1l_opy_ (u"ࠬࡹࡣࡢࡰࠪ₏"): bstack1l1ll1lll1_opy_.perform_scan}
        bstack1lllll11l111_opy_ = json.loads(scripts[bstack1ll1l_opy_ (u"ࠨࡳࡤࡣࡱࠦₐ")].replace(bstack1ll1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࠥₑ"), bstack1ll1l_opy_ (u"ࠣࠤₒ")))
        bstack1lllll11l111_opy_[bstack1ll1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬₓ")][bstack1ll1l_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪₔ")] = None
        scripts[bstack1ll1l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤₕ")] = bstack1ll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣₖ") + json.dumps(bstack1lllll11l111_opy_)
        bstack1l1ll1lll1_opy_.bstack1l11l111ll_opy_(scripts)
        bstack1l1ll1lll1_opy_.store()
        logger.debug(driver.execute_script(bstack1l1ll1lll1_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack1l1ll1lll1_opy_.bstack1lllll1l1111_opy_, bstack1l111l11ll1_opy_))
      bstack111l11llll_opy_.end(bstack1l1lllll111_opy_, bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨₗ"), bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧₘ"),True, None)
    except Exception as error:
      bstack111l11llll_opy_.end(bstack1l1lllll111_opy_, bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣₙ"), bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢₚ"),False, str(error))
    logger.info(bstack1ll1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨₛ"))
  except Exception as bstack1l1111ll111_opy_:
    logger.error(bstack1ll1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨₜ") + str(path) + bstack1ll1l_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢ₝") + str(bstack1l1111ll111_opy_))
def bstack1llll1lll11l_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack1ll1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ₞")) and str(caps.get(bstack1ll1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ₟"))).lower() == bstack1ll1l_opy_ (u"ࠣࡣࡱࡨࡷࡵࡩࡥࠤ₠"):
        bstack1l111lll11l_opy_ = caps.get(bstack1ll1l_opy_ (u"ࠤࡤࡴࡵ࡯ࡵ࡮࠼ࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ₡")) or caps.get(bstack1ll1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ₢"))
        if bstack1l111lll11l_opy_ and int(str(bstack1l111lll11l_opy_)) < bstack11l1l11l1l1_opy_:
            return False
    return True
def bstack11l11lll1_opy_(config):
  if bstack1ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ₣") in config:
        return config[bstack1ll1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ₤")]
  for platform in config.get(bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ₥"), []):
      if bstack1ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ₦") in platform:
          return platform[bstack1ll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ₧")]
  return None
def bstack1ll1l11l1l_opy_(bstack1111l1l1l1_opy_):
  try:
    browser_name = bstack1111l1l1l1_opy_[bstack1ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨ₨")]
    browser_version = bstack1111l1l1l1_opy_[bstack1ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ₩")]
    chrome_options = bstack1111l1l1l1_opy_[bstack1ll1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡣࡴࡶࡴࡪࡱࡱࡷࠬ₪")]
    try:
        bstack1lllll11111l_opy_ = int(browser_version.split(bstack1ll1l_opy_ (u"ࠬ࠴ࠧ₫"))[0])
    except ValueError as e:
        logger.error(bstack1ll1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡨࡵ࡮ࡷࡧࡵࡸ࡮ࡴࡧࠡࡤࡵࡳࡼࡹࡥࡳࠢࡹࡩࡷࡹࡩࡰࡰࠥ€") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack1ll1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ₭")):
        logger.warning(bstack1ll1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ₮"))
        return False
    if bstack1lllll11111l_opy_ < bstack1lllll111l1l_opy_.bstack1l111ll1lll_opy_:
        logger.warning(bstack1lllll1l1_opy_ (u"ࠩࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡳࠡࡅ࡫ࡶࡴࡳࡥࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡾࡇࡔࡔࡓࡕࡃࡑࡘࡘ࠴ࡍࡊࡐࡌࡑ࡚ࡓ࡟ࡏࡑࡑࡣࡇ࡙ࡔࡂࡅࡎࡣࡎࡔࡆࡓࡃࡢࡅ࠶࠷࡙ࡠࡕࡘࡔࡕࡕࡒࡕࡇࡇࡣࡈࡎࡒࡐࡏࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࢂࠦ࡯ࡳࠢ࡫࡭࡬࡮ࡥࡳ࠰ࠪ₯"))
        return False
    if chrome_options and any(bstack1ll1l_opy_ (u"ࠪ࠱࠲࡮ࡥࡢࡦ࡯ࡩࡸࡹࠧ₰") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack1ll1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡰࡰࠣࡰࡪ࡭ࡡࡤࡻࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠤࡘࡽࡩࡵࡥ࡫ࠤࡹࡵࠠ࡯ࡧࡺࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨࠤࡴࡸࠠࡢࡸࡲ࡭ࡩࠦࡵࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠨ₱"))
        return False
    return True
  except Exception as e:
    logger.error(bstack1ll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡤࡪࡨࡧࡰ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡻࡰࡱࡱࡵࡸࠥ࡬࡯ࡳࠢ࡯ࡳࡨࡧ࡬ࠡࡅ࡫ࡶࡴࡳࡥ࠻ࠢࠥ₲") + str(e))
    return False
def bstack11l1llll1l_opy_(bstack1l1l1l111l_opy_, config):
    try:
      bstack1l1111l1ll1_opy_ = bstack1ll1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭₳") in config and config[bstack1ll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ₴")] == True
      bstack1llll1ll11l1_opy_ = bstack1ll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ₵") in config and str(config[bstack1ll1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭₶")]).lower() != bstack1ll1l_opy_ (u"ࠪࡪࡦࡲࡳࡦࠩ₷")
      if not (bstack1l1111l1ll1_opy_ and (not bstack11l11ll11_opy_(config) or bstack1llll1ll11l1_opy_)):
        return bstack1l1l1l111l_opy_
      bstack1llll1llll11_opy_ = bstack1l1ll1lll1_opy_.bstack1lllll11llll_opy_
      if bstack1llll1llll11_opy_ is None:
        logger.debug(bstack1ll1l_opy_ (u"ࠦࡌࡵ࡯ࡨ࡮ࡨࠤࡨ࡮ࡲࡰ࡯ࡨࠤࡴࡶࡴࡪࡱࡱࡷࠥࡧࡲࡦࠢࡑࡳࡳ࡫ࠢ₸"))
        return bstack1l1l1l111l_opy_
      bstack1lllll11l1ll_opy_ = int(str(bstack1111llll11l_opy_()).split(bstack1ll1l_opy_ (u"ࠬ࠴ࠧ₹"))[0])
      logger.debug(bstack1ll1l_opy_ (u"ࠨࡓࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡧࡩࡹ࡫ࡣࡵࡧࡧ࠾ࠥࠨ₺") + str(bstack1lllll11l1ll_opy_) + bstack1ll1l_opy_ (u"ࠢࠣ₻"))
      if bstack1lllll11l1ll_opy_ == 3 and isinstance(bstack1l1l1l111l_opy_, dict) and bstack1ll1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ₼") in bstack1l1l1l111l_opy_ and bstack1llll1llll11_opy_ is not None:
        if bstack1ll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ₽") not in bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ₾")]:
          bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ₿")][bstack1ll1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃀")] = {}
        if bstack1ll1l_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃁") in bstack1llll1llll11_opy_:
          if bstack1ll1l_opy_ (u"ࠧࡢࡴࡪࡷࠬ⃂") not in bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃃")][bstack1ll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃄")]:
            bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃅")][bstack1ll1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃆")][bstack1ll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃇")] = []
          for arg in bstack1llll1llll11_opy_[bstack1ll1l_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃈")]:
            if arg not in bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃉")][bstack1ll1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃊")][bstack1ll1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ⃋")]:
              bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃌")][bstack1ll1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃍")][bstack1ll1l_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃎")].append(arg)
        if bstack1ll1l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃏") in bstack1llll1llll11_opy_:
          if bstack1ll1l_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃐") not in bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃑")][bstack1ll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹ⃒ࠧ")]:
            bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃓ࠪ")][bstack1ll1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃔")][bstack1ll1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃕")] = []
          for ext in bstack1llll1llll11_opy_[bstack1ll1l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃖")]:
            if ext not in bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃗")][bstack1ll1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ⃘࠭")][bstack1ll1l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ⃙࠭")]:
              bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃚ࠪ")][bstack1ll1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃛")][bstack1ll1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃜")].append(ext)
        if bstack1ll1l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ⃝") in bstack1llll1llll11_opy_:
          if bstack1ll1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭⃞") not in bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃟")][bstack1ll1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃠")]:
            bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃡")][bstack1ll1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃢")][bstack1ll1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⃣")] = {}
          bstack111l1111l11_opy_(bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭⃤")][bstack1ll1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷ⃥ࠬ")][bstack1ll1l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹ⃦ࠧ")],
                    bstack1llll1llll11_opy_[bstack1ll1l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ⃧")])
        os.environ[bstack1ll1l_opy_ (u"ࠪࡍࡘࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡇࡖࡗࡎࡕࡎࠨ⃨")] = bstack1ll1l_opy_ (u"ࠫࡹࡸࡵࡦࠩ⃩")
        return bstack1l1l1l111l_opy_
      else:
        chrome_options = None
        if isinstance(bstack1l1l1l111l_opy_, ChromeOptions):
          chrome_options = bstack1l1l1l111l_opy_
        elif isinstance(bstack1l1l1l111l_opy_, dict):
          for value in bstack1l1l1l111l_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack1l1l1l111l_opy_, dict):
            bstack1l1l1l111l_opy_[bstack1ll1l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ⃪࠭")] = chrome_options
          else:
            bstack1l1l1l111l_opy_ = chrome_options
        if bstack1llll1llll11_opy_ is not None:
          if bstack1ll1l_opy_ (u"࠭ࡡࡳࡩࡶ⃫ࠫ") in bstack1llll1llll11_opy_:
                bstack1llll1llll1l_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1llll11_opy_[bstack1ll1l_opy_ (u"ࠧࡢࡴࡪࡷ⃬ࠬ")]
                for arg in new_args:
                    if arg not in bstack1llll1llll1l_opy_:
                        chrome_options.add_argument(arg)
          if bstack1ll1l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷ⃭ࠬ") in bstack1llll1llll11_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack1ll1l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ⃮࠭"), [])
                bstack1lllll111lll_opy_ = bstack1llll1llll11_opy_[bstack1ll1l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹ⃯ࠧ")]
                for extension in bstack1lllll111lll_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack1ll1l_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⃰") in bstack1llll1llll11_opy_:
                bstack1lllll11ll1l_opy_ = chrome_options.experimental_options.get(bstack1ll1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ⃱"), {})
                bstack1lllll111ll1_opy_ = bstack1llll1llll11_opy_[bstack1ll1l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ⃲")]
                bstack111l1111l11_opy_(bstack1lllll11ll1l_opy_, bstack1lllll111ll1_opy_)
                chrome_options.add_experimental_option(bstack1ll1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭⃳"), bstack1lllll11ll1l_opy_)
        os.environ[bstack1ll1l_opy_ (u"ࠨࡋࡖࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡅࡔࡕࡌࡓࡓ࠭⃴")] = bstack1ll1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⃵")
        return bstack1l1l1l111l_opy_
    except Exception as e:
      logger.error(bstack1ll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡣࡧࡨ࡮ࡴࡧࠡࡰࡲࡲ࠲ࡈࡓࠡ࡫ࡱࡪࡷࡧࠠࡢ࠳࠴ࡽࠥࡩࡨࡳࡱࡰࡩࠥࡵࡰࡵ࡫ࡲࡲࡸࡀࠠࠣ⃶") + str(e))
      return bstack1l1l1l111l_opy_