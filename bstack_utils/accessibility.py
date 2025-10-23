# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1llll1ll11ll_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l1l111l1l_opy_ as bstack1lllll11ll11_opy_, EVENTS
from bstack_utils.bstack11l1llll11_opy_ import bstack11l1llll11_opy_
from bstack_utils.helper import bstack1llll1ll_opy_, bstack1llll11l_opy_, bstack11l1l1l1ll_opy_, bstack1111ll1lll1_opy_, \
  bstack111l1l1111l_opy_, bstack111l11lll1_opy_, get_host_info, bstack111ll1111l1_opy_, bstack1l11l1ll1l_opy_, error_handler, bstack1111lll11l1_opy_, bstack111ll11111l_opy_, bstack1lll111l_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack11111ll111_opy_ import get_logger
from bstack_utils.bstack1l11ll11l1_opy_ import bstack1llllll1lll_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack1l11ll11l1_opy_ = bstack1llllll1lll_opy_()
@error_handler(class_method=False)
def _1llll1lll1l1_opy_(driver, bstack111ll11l_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack111111l_opy_ (u"ࠫࡴࡹ࡟࡯ࡣࡰࡩࠬᾼ"): caps.get(bstack111111l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫ᾽"), None),
        bstack111111l_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪι"): bstack111ll11l_opy_.get(bstack111111l_opy_ (u"ࠧࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠪ᾿"), None),
        bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧ῀"): caps.get(bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ῁"), None),
        bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬῂ"): caps.get(bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬῃ"), None)
    }
  except Exception as error:
    logger.debug(bstack111111l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࠦ࠺ࠡࠩῄ") + str(error))
  return response
def on():
    if os.environ.get(bstack111111l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫ῅"), None) is None or os.environ[bstack111111l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬῆ")] == bstack111111l_opy_ (u"ࠣࡰࡸࡰࡱࠨῇ"):
        return False
    return True
def bstack11ll1l11ll_opy_(config):
  return config.get(bstack111111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩῈ"), False) or any([p.get(bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪΈ"), False) == True for p in config.get(bstack111111l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧῊ"), [])])
def bstack1l1l1l11l1_opy_(config, bstack1111ll111l_opy_):
  try:
    bstack1lllll11l1l1_opy_ = config.get(bstack111111l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬΉ"), False)
    if int(bstack1111ll111l_opy_) < len(config.get(bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩῌ"), [])) and config[bstack111111l_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ῍")][bstack1111ll111l_opy_]:
      bstack1lllll111l11_opy_ = config[bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ῎")][bstack1111ll111l_opy_].get(bstack111111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ῏"), None)
    else:
      bstack1lllll111l11_opy_ = config.get(bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪῐ"), None)
    if bstack1lllll111l11_opy_ != None:
      bstack1lllll11l1l1_opy_ = bstack1lllll111l11_opy_
    bstack1lllll11l111_opy_ = os.getenv(bstack111111l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩῑ")) is not None and len(os.getenv(bstack111111l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪῒ"))) > 0 and os.getenv(bstack111111l_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫΐ")) != bstack111111l_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬ῔")
    return bstack1lllll11l1l1_opy_ and bstack1lllll11l111_opy_
  except Exception as error:
    logger.debug(bstack111111l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡷࡧࡵ࡭࡫ࡿࡩ࡯ࡩࠣࡸ࡭࡫ࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡹ࡬ࡸ࡭ࠦࡥࡳࡴࡲࡶࠥࡀࠠࠨ῕") + str(error))
  return False
def bstack11l11ll11l_opy_(test_tags):
  bstack1l111l11ll1_opy_ = os.getenv(bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪῖ"))
  if bstack1l111l11ll1_opy_ is None:
    return True
  bstack1l111l11ll1_opy_ = json.loads(bstack1l111l11ll1_opy_)
  try:
    include_tags = bstack1l111l11ll1_opy_[bstack111111l_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨῗ")] if bstack111111l_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩῘ") in bstack1l111l11ll1_opy_ and isinstance(bstack1l111l11ll1_opy_[bstack111111l_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪῙ")], list) else []
    exclude_tags = bstack1l111l11ll1_opy_[bstack111111l_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫῚ")] if bstack111111l_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬΊ") in bstack1l111l11ll1_opy_ and isinstance(bstack1l111l11ll1_opy_[bstack111111l_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭῜")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack111111l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡹ࡫࡭ࡱ࡫ࠠࡷࡣ࡯࡭ࡩࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡧࡱࡵࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡩࡡ࡯ࡰ࡬ࡲ࡬࠴ࠠࡆࡴࡵࡳࡷࠦ࠺ࠡࠤ῝") + str(error))
  return False
def bstack1llll1llll1l_opy_(config, frameworkName, bstack1lllll11l1ll_opy_, bstack1llll1llll11_opy_):
  bstack1llll1llllll_opy_ = bstack1111ll1lll1_opy_(config)
  bstack1lllll11111l_opy_ = bstack111l1l1111l_opy_(config)
  if bstack1llll1llllll_opy_ is None or bstack1lllll11111l_opy_ is None:
    logger.error(bstack111111l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥࡸࡵ࡯ࠢࡩࡳࡷࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯࠼ࠣࡑ࡮ࡹࡳࡪࡰࡪࠤࡦࡻࡴࡩࡧࡱࡸ࡮ࡩࡡࡵ࡫ࡲࡲࠥࡺ࡯࡬ࡧࡱࠫ῞"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack111111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ῟"), bstack111111l_opy_ (u"ࠬࢁࡽࠨῠ")))
    data = {
        bstack111111l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫῡ"): config[bstack111111l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬῢ")],
        bstack111111l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫΰ"): config.get(bstack111111l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬῤ"), os.path.basename(os.getcwd())),
        bstack111111l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡖ࡬ࡱࡪ࠭ῥ"): bstack1llll1ll_opy_(),
        bstack111111l_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩῦ"): config.get(bstack111111l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡈࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨῧ"), bstack111111l_opy_ (u"࠭ࠧῨ")),
        bstack111111l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧῩ"): {
            bstack111111l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡒࡦࡳࡥࠨῪ"): frameworkName,
            bstack111111l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬΎ"): bstack1lllll11l1ll_opy_,
            bstack111111l_opy_ (u"ࠪࡷࡩࡱࡖࡦࡴࡶ࡭ࡴࡴࠧῬ"): __version__,
            bstack111111l_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭῭"): bstack111111l_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ΅"),
            bstack111111l_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭`"): bstack111111l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩ῰"),
            bstack111111l_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ῱"): bstack1llll1llll11_opy_
        },
        bstack111111l_opy_ (u"ࠩࡶࡩࡹࡺࡩ࡯ࡩࡶࠫῲ"): settings,
        bstack111111l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࡇࡴࡴࡴࡳࡱ࡯ࠫῳ"): bstack111ll1111l1_opy_(),
        bstack111111l_opy_ (u"ࠫࡨ࡯ࡉ࡯ࡨࡲࠫῴ"): bstack111l11lll1_opy_(),
        bstack111111l_opy_ (u"ࠬ࡮࡯ࡴࡶࡌࡲ࡫ࡵࠧ῵"): get_host_info(),
        bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨῶ"): bstack11l1l1l1ll_opy_(config)
    }
    headers = {
        bstack111111l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭ῷ"): bstack111111l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫῸ"),
    }
    config = {
        bstack111111l_opy_ (u"ࠩࡤࡹࡹ࡮ࠧΌ"): (bstack1llll1llllll_opy_, bstack1lllll11111l_opy_),
        bstack111111l_opy_ (u"ࠪ࡬ࡪࡧࡤࡦࡴࡶࠫῺ"): headers
    }
    response = bstack1l11l1ll1l_opy_(bstack111111l_opy_ (u"ࠫࡕࡕࡓࡕࠩΏ"), bstack1lllll11ll11_opy_ + bstack111111l_opy_ (u"ࠬ࠵ࡶ࠳࠱ࡷࡩࡸࡺ࡟ࡳࡷࡱࡷࠬῼ"), data, config)
    bstack1llll1lll111_opy_ = response.json()
    if bstack1llll1lll111_opy_[bstack111111l_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧ´")]:
      parsed = json.loads(os.getenv(bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ῾"), bstack111111l_opy_ (u"ࠨࡽࢀࠫ῿")))
      parsed[bstack111111l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ ")] = bstack1llll1lll111_opy_[bstack111111l_opy_ (u"ࠪࡨࡦࡺࡡࠨ ")][bstack111111l_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ ")]
      os.environ[bstack111111l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭ ")] = json.dumps(parsed)
      bstack11l1llll11_opy_.bstack1l1llll11l_opy_(bstack1llll1lll111_opy_[bstack111111l_opy_ (u"࠭ࡤࡢࡶࡤࠫ ")][bstack111111l_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨ ")])
      bstack11l1llll11_opy_.bstack1lllll11llll_opy_(bstack1llll1lll111_opy_[bstack111111l_opy_ (u"ࠨࡦࡤࡸࡦ࠭ ")][bstack111111l_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶࠫ ")])
      bstack11l1llll11_opy_.store()
      return bstack1llll1lll111_opy_[bstack111111l_opy_ (u"ࠪࡨࡦࡺࡡࠨ ")][bstack111111l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡘࡴࡱࡥ࡯ࠩ ")], bstack1llll1lll111_opy_[bstack111111l_opy_ (u"ࠬࡪࡡࡵࡣࠪ ")][bstack111111l_opy_ (u"࠭ࡩࡥࠩ​")]
    else:
      logger.error(bstack111111l_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡵࡹࡳࡴࡩ࡯ࡩࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࠨ‌") + bstack1llll1lll111_opy_[bstack111111l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ‍")])
      if bstack1llll1lll111_opy_[bstack111111l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ‎")] == bstack111111l_opy_ (u"ࠪࡍࡳࡼࡡ࡭࡫ࡧࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤࡵࡧࡳࡴࡧࡧ࠲ࠬ‏"):
        for bstack1lllll111l1l_opy_ in bstack1llll1lll111_opy_[bstack111111l_opy_ (u"ࠫࡪࡸࡲࡰࡴࡶࠫ‐")]:
          logger.error(bstack1lllll111l1l_opy_[bstack111111l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭‑")])
      return None, None
  except Exception as error:
    logger.error(bstack111111l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡴࡸࡲࠥ࡬࡯ࡳࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࠿ࠦࠢ‒") +  str(error))
    return None, None
def bstack1lllll11lll1_opy_():
  if os.getenv(bstack111111l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ–")) is None:
    return {
        bstack111111l_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨ—"): bstack111111l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨ―"),
        bstack111111l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ‖"): bstack111111l_opy_ (u"ࠫࡇࡻࡩ࡭ࡦࠣࡧࡷ࡫ࡡࡵ࡫ࡲࡲࠥ࡮ࡡࡥࠢࡩࡥ࡮ࡲࡥࡥ࠰ࠪ‗")
    }
  data = {bstack111111l_opy_ (u"ࠬ࡫࡮ࡥࡖ࡬ࡱࡪ࠭‘"): bstack1llll1ll_opy_()}
  headers = {
      bstack111111l_opy_ (u"࠭ࡁࡶࡶ࡫ࡳࡷ࡯ࡺࡢࡶ࡬ࡳࡳ࠭’"): bstack111111l_opy_ (u"ࠧࡃࡧࡤࡶࡪࡸࠠࠨ‚") + os.getenv(bstack111111l_opy_ (u"ࠣࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙ࠨ‛")),
      bstack111111l_opy_ (u"ࠩࡆࡳࡳࡺࡥ࡯ࡶ࠰ࡘࡾࡶࡥࠨ“"): bstack111111l_opy_ (u"ࠪࡥࡵࡶ࡬ࡪࡥࡤࡸ࡮ࡵ࡮࠰࡬ࡶࡳࡳ࠭”")
  }
  response = bstack1l11l1ll1l_opy_(bstack111111l_opy_ (u"ࠫࡕ࡛ࡔࠨ„"), bstack1lllll11ll11_opy_ + bstack111111l_opy_ (u"ࠬ࠵ࡴࡦࡵࡷࡣࡷࡻ࡮ࡴ࠱ࡶࡸࡴࡶࠧ‟"), data, { bstack111111l_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ†"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack111111l_opy_ (u"ࠢࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡘࡪࡹࡴࠡࡔࡸࡲࠥࡳࡡࡳ࡭ࡨࡨࠥࡧࡳࠡࡥࡲࡱࡵࡲࡥࡵࡧࡧࠤࡦࡺࠠࠣ‡") + bstack1llll11l_opy_().isoformat() + bstack111111l_opy_ (u"ࠨ࡜ࠪ•"))
      return {bstack111111l_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ‣"): bstack111111l_opy_ (u"ࠪࡷࡺࡩࡣࡦࡵࡶࠫ․"), bstack111111l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ‥"): bstack111111l_opy_ (u"ࠬ࠭…")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack111111l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡺ࡬࡮ࡲࡥࠡ࡯ࡤࡶࡰ࡯࡮ࡨࠢࡦࡳࡲࡶ࡬ࡦࡶ࡬ࡳࡳࠦ࡯ࡧࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲ࡚ࠥࡥࡴࡶࠣࡖࡺࡴ࠺ࠡࠤ‧") + str(error))
    return {
        bstack111111l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ "): bstack111111l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ "),
        bstack111111l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ‪"): str(error)
    }
def bstack1lllll111111_opy_(bstack1llll1ll1lll_opy_):
    return re.match(bstack111111l_opy_ (u"ࡵࠫࡣࡢࡤࠬࠪ࡟࠲ࡡࡪࠫࠪࡁࠧࠫ‫"), bstack1llll1ll1lll_opy_.strip()) is not None
def bstack1l1l1ll11_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1llll1ll1ll1_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1llll1ll1ll1_opy_ = desired_capabilities
        else:
          bstack1llll1ll1ll1_opy_ = {}
        bstack1l111lll1ll_opy_ = (bstack1llll1ll1ll1_opy_.get(bstack111111l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪ‬"), bstack111111l_opy_ (u"ࠬ࠭‭")).lower() or caps.get(bstack111111l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠬ‮"), bstack111111l_opy_ (u"ࠧࠨ ")).lower())
        if bstack1l111lll1ll_opy_ == bstack111111l_opy_ (u"ࠨ࡫ࡲࡷࠬ‰"):
            return True
        if bstack1l111lll1ll_opy_ == bstack111111l_opy_ (u"ࠩࡤࡲࡩࡸ࡯ࡪࡦࠪ‱"):
            bstack1l111l1l11l_opy_ = str(float(caps.get(bstack111111l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠬ′")) or bstack1llll1ll1ll1_opy_.get(bstack111111l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ″"), {}).get(bstack111111l_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨ‴"),bstack111111l_opy_ (u"࠭ࠧ‵"))))
            if bstack1l111lll1ll_opy_ == bstack111111l_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࠨ‶") and int(bstack1l111l1l11l_opy_.split(bstack111111l_opy_ (u"ࠨ࠰ࠪ‷"))[0]) < float(bstack11l1l111lll_opy_):
                logger.warning(str(bstack11l1l1l11ll_opy_))
                return False
            return True
        bstack1l1111ll1ll_opy_ = caps.get(bstack111111l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ‸"), {}).get(bstack111111l_opy_ (u"ࠪࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠧ‹"), caps.get(bstack111111l_opy_ (u"ࠫࡩ࡫ࡶࡪࡥࡨࠫ›"), bstack111111l_opy_ (u"ࠬ࠭※")))
        if bstack1l1111ll1ll_opy_:
            logger.warning(bstack111111l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡴࡸࡲࠥࡵ࡮࡭ࡻࠣࡳࡳࠦࡄࡦࡵ࡮ࡸࡴࡶࠠࡣࡴࡲࡻࡸ࡫ࡲࡴ࠰ࠥ‼"))
            return False
        browser = caps.get(bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ‽"), bstack111111l_opy_ (u"ࠨࠩ‾")).lower() or bstack1llll1ll1ll1_opy_.get(bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧ‿"), bstack111111l_opy_ (u"ࠪࠫ⁀")).lower()
        if browser != bstack111111l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫ⁁"):
            logger.warning(bstack111111l_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣ⁂"))
            return False
        browser_version = caps.get(bstack111111l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⁃")) or caps.get(bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ⁄")) or bstack1llll1ll1ll1_opy_.get(bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⁅")) or bstack1llll1ll1ll1_opy_.get(bstack111111l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁆"), {}).get(bstack111111l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ⁇")) or bstack1llll1ll1ll1_opy_.get(bstack111111l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ⁈"), {}).get(bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ⁉"))
        bstack1l1111l1ll1_opy_ = bstack1llll1ll11ll_opy_.bstack1l111l11l1l_opy_
        bstack1llll1ll1l1l_opy_ = False
        if config is not None:
          bstack1llll1ll1l1l_opy_ = bstack111111l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ⁊") in config and str(config[bstack111111l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ⁋")]).lower() != bstack111111l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧ⁌")
        if os.environ.get(bstack111111l_opy_ (u"ࠩࡌࡗࡤࡔࡏࡏࡡࡅࡗ࡙ࡇࡃࡌࡡࡌࡒࡋࡘࡁࡠࡃ࠴࠵࡞ࡥࡓࡆࡕࡖࡍࡔࡔࠧ⁍"), bstack111111l_opy_ (u"ࠪࠫ⁎")).lower() == bstack111111l_opy_ (u"ࠫࡹࡸࡵࡦࠩ⁏") or bstack1llll1ll1l1l_opy_:
          bstack1l1111l1ll1_opy_ = bstack1llll1ll11ll_opy_.bstack1l111lllll1_opy_
        if browser_version and browser_version != bstack111111l_opy_ (u"ࠬࡲࡡࡵࡧࡶࡸࠬ⁐") and int(browser_version.split(bstack111111l_opy_ (u"࠭࠮ࠨ⁑"))[0]) <= bstack1l1111l1ll1_opy_:
          logger.warning(bstack1llll1ll1_opy_ (u"ࠧࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡵࡹࡳࠦ࡯࡯࡮ࡼࠤࡴࡴࠠࡄࡪࡵࡳࡲ࡫ࠠࡣࡴࡲࡻࡸ࡫ࡲࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡪࡶࡪࡧࡴࡦࡴࠣࡸ࡭ࡧ࡮ࠡࡽࡰ࡭ࡳࡥࡡ࠲࠳ࡼࡣࡸࡻࡰࡱࡱࡵࡸࡪࡪ࡟ࡤࡪࡵࡳࡲ࡫࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࡾ࠰ࠪ⁒"))
          return False
        if not options:
          bstack1l111ll11ll_opy_ = caps.get(bstack111111l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⁓")) or bstack1llll1ll1ll1_opy_.get(bstack111111l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⁔"), {})
          if bstack111111l_opy_ (u"ࠪ࠱࠲࡮ࡥࡢࡦ࡯ࡩࡸࡹࠧ⁕") in bstack1l111ll11ll_opy_.get(bstack111111l_opy_ (u"ࠫࡦࡸࡧࡴࠩ⁖"), []):
              logger.warning(bstack111111l_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠ࡯ࡱࡷࠤࡷࡻ࡮ࠡࡱࡱࠤࡱ࡫ࡧࡢࡥࡼࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲࡙ࠥࡷࡪࡶࡦ࡬ࠥࡺ࡯ࠡࡰࡨࡻࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩࠥࡵࡲࠡࡣࡹࡳ࡮ࡪࠠࡶࡵ࡬ࡲ࡬ࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪ࠴ࠢ⁗"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack111111l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡡ࡭࡫ࡧࡥࡹ࡫ࠠࡢ࠳࠴ࡽࠥࡹࡵࡱࡲࡲࡶࡹࠦ࠺ࠣ⁘") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l1l1ll1l11_opy_ = config.get(bstack111111l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ⁙"), {})
    bstack1l1l1ll1l11_opy_[bstack111111l_opy_ (u"ࠨࡣࡸࡸ࡭࡚࡯࡬ࡧࡱࠫ⁚")] = os.getenv(bstack111111l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧ⁛"))
    bstack111l1ll1ll1_opy_ = json.loads(os.getenv(bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ⁜"), bstack111111l_opy_ (u"ࠫࢀࢃࠧ⁝"))).get(bstack111111l_opy_ (u"ࠬࡹࡣࡢࡰࡱࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁞"))
    if not config[bstack111111l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡕࡸ࡯ࡥࡷࡦࡸࡒࡧࡰࠨ ")].get(bstack111111l_opy_ (u"ࠢࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪࠨ⁠")):
      if bstack111111l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩ⁡") in caps:
        caps[bstack111111l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁢")][bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ⁣")] = bstack1l1l1ll1l11_opy_
        caps[bstack111111l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ⁤")][bstack111111l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ⁥")][bstack111111l_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⁦")] = bstack111l1ll1ll1_opy_
      else:
        caps[bstack111111l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭⁧")] = bstack1l1l1ll1l11_opy_
        caps[bstack111111l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧ⁨")][bstack111111l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ⁩")] = bstack111l1ll1ll1_opy_
  except Exception as error:
    logger.debug(bstack111111l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠰ࠣࡉࡷࡸ࡯ࡳ࠼ࠣࠦ⁪") +  str(error))
def bstack1l111111l1_opy_(driver, bstack1llll1lll11l_opy_):
  try:
    setattr(driver, bstack111111l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡅ࠶࠷ࡹࡔࡪࡲࡹࡱࡪࡓࡤࡣࡱࠫ⁫"), True)
    session = driver.session_id
    if session:
      bstack1llll1ll1l11_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1ll1l11_opy_ = False
      bstack1llll1ll1l11_opy_ = url.scheme in [bstack111111l_opy_ (u"ࠧ࡮ࡴࡵࡲࠥ⁬"), bstack111111l_opy_ (u"ࠨࡨࡵࡶࡳࡷࠧ⁭")]
      if bstack1llll1ll1l11_opy_:
        if bstack1llll1lll11l_opy_:
          logger.info(bstack111111l_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡦࡰࡴࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡭ࡧࡳࠡࡵࡷࡥࡷࡺࡥࡥ࠰ࠣࡅࡺࡺ࡯࡮ࡣࡷࡩࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠤࡼ࡯࡬࡭ࠢࡥࡩ࡬࡯࡮ࠡ࡯ࡲࡱࡪࡴࡴࡢࡴ࡬ࡰࡾ࠴ࠢ⁮"))
      return bstack1llll1lll11l_opy_
  except Exception as e:
    logger.error(bstack111111l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡶࡤࡶࡹ࡯࡮ࡨࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡳࡤࡣࡱࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦ࠼ࠣࠦ⁯") + str(e))
    return False
def bstack1lllllll1_opy_(driver, name, path):
  try:
    bstack1l111llll11_opy_ = {
        bstack111111l_opy_ (u"ࠩࡷ࡬࡙࡫ࡳࡵࡔࡸࡲ࡚ࡻࡩࡥࠩ⁰"): threading.current_thread().current_test_uuid,
        bstack111111l_opy_ (u"ࠪࡸ࡭ࡈࡵࡪ࡮ࡧ࡙ࡺ࡯ࡤࠨⁱ"): os.environ.get(bstack111111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ⁲"), bstack111111l_opy_ (u"ࠬ࠭⁳")),
        bstack111111l_opy_ (u"࠭ࡴࡩࡌࡺࡸ࡙ࡵ࡫ࡦࡰࠪ⁴"): os.environ.get(bstack111111l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡋ࡙ࡗࠫ⁵"), bstack111111l_opy_ (u"ࠨࠩ⁶"))
    }
    bstack1ll1l1ll1ll_opy_ = bstack1l11ll11l1_opy_.bstack1ll1l1l11ll_opy_(EVENTS.bstack11lll1llll_opy_.value)
    logger.debug(bstack111111l_opy_ (u"ࠩࡓࡩࡷ࡬࡯ࡳ࡯࡬ࡲ࡬ࠦࡳࡤࡣࡱࠤࡧ࡫ࡦࡰࡴࡨࠤࡸࡧࡶࡪࡰࡪࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠬ⁷"))
    try:
      if (bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ⁸"), None) and bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭⁹"), None)):
        scripts = {bstack111111l_opy_ (u"ࠬࡹࡣࡢࡰࠪ⁺"): bstack11l1llll11_opy_.perform_scan}
        bstack1lllll1111ll_opy_ = json.loads(scripts[bstack111111l_opy_ (u"ࠨࡳࡤࡣࡱࠦ⁻")].replace(bstack111111l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࠥ⁼"), bstack111111l_opy_ (u"ࠣࠤ⁽")))
        bstack1lllll1111ll_opy_[bstack111111l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ⁾")][bstack111111l_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪⁿ")] = None
        scripts[bstack111111l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ₀")] = bstack111111l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ₁") + json.dumps(bstack1lllll1111ll_opy_)
        bstack11l1llll11_opy_.bstack1l1llll11l_opy_(scripts)
        bstack11l1llll11_opy_.store()
        logger.debug(driver.execute_script(bstack11l1llll11_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11l1llll11_opy_.perform_scan, {bstack111111l_opy_ (u"ࠨ࡭ࡦࡶ࡫ࡳࡩࠨ₂"): name}))
      bstack1l11ll11l1_opy_.end(EVENTS.bstack11lll1llll_opy_.value, bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ₃"), bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ₄"), True, None)
    except Exception as error:
      bstack1l11ll11l1_opy_.end(EVENTS.bstack11lll1llll_opy_.value, bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ₅"), bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠥ࠾ࡪࡴࡤࠣ₆"), False, str(error))
    bstack1ll1l1ll1ll_opy_ = bstack1l11ll11l1_opy_.bstack11ll1ll111l_opy_(EVENTS.bstack1l111l1l111_opy_.value)
    bstack1l11ll11l1_opy_.mark(bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦ₇"))
    try:
      if (bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠬ࡯ࡳࡂࡲࡳࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ₈"), None) and bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"࠭ࡡࡱࡲࡄ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ₉"), None)):
        scripts = {bstack111111l_opy_ (u"ࠧࡴࡥࡤࡲࠬ₊"): bstack11l1llll11_opy_.perform_scan}
        bstack1lllll1111ll_opy_ = json.loads(scripts[bstack111111l_opy_ (u"ࠣࡵࡦࡥࡳࠨ₋")].replace(bstack111111l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࠧ₌"), bstack111111l_opy_ (u"ࠥࠦ₍")))
        bstack1lllll1111ll_opy_[bstack111111l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧ₎")][bstack111111l_opy_ (u"ࠬࡳࡥࡵࡪࡲࡨࠬ₏")] = None
        scripts[bstack111111l_opy_ (u"ࠨࡳࡤࡣࡱࠦₐ")] = bstack111111l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࠥₑ") + json.dumps(bstack1lllll1111ll_opy_)
        bstack11l1llll11_opy_.bstack1l1llll11l_opy_(scripts)
        bstack11l1llll11_opy_.store()
        logger.debug(driver.execute_script(bstack11l1llll11_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack11l1llll11_opy_.bstack1lllll1l111l_opy_, bstack1l111llll11_opy_))
      bstack1l11ll11l1_opy_.end(bstack1ll1l1ll1ll_opy_, bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣₒ"), bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢₓ"),True, None)
    except Exception as error:
      bstack1l11ll11l1_opy_.end(bstack1ll1l1ll1ll_opy_, bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥₔ"), bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤₕ"),False, str(error))
    logger.info(bstack111111l_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡺࡥࡴࡶ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨࠤ࡭ࡧࡳࠡࡧࡱࡨࡪࡪ࠮ࠣₖ"))
  except Exception as bstack1l111ll1l1l_opy_:
    logger.error(bstack111111l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡲࡦࡵࡸࡰࡹࡹࠠࡤࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡦࡪࠦࡰࡳࡱࡦࡩࡸࡹࡥࡥࠢࡩࡳࡷࠦࡴࡩࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࡀࠠࠣₗ") + str(path) + bstack111111l_opy_ (u"ࠢࠡࡇࡵࡶࡴࡸࠠ࠻ࠤₘ") + str(bstack1l111ll1l1l_opy_))
def bstack1lllll111ll1_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack111111l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢₙ")) and str(caps.get(bstack111111l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣₚ"))).lower() == bstack111111l_opy_ (u"ࠥࡥࡳࡪࡲࡰ࡫ࡧࠦₛ"):
        bstack1l111l1l11l_opy_ = caps.get(bstack111111l_opy_ (u"ࠦࡦࡶࡰࡪࡷࡰ࠾ࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨₜ")) or caps.get(bstack111111l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ₝"))
        if bstack1l111l1l11l_opy_ and int(str(bstack1l111l1l11l_opy_)) < bstack11l1l111lll_opy_:
            return False
    return True
def bstack11llll1l11_opy_(config):
  if bstack111111l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭₞") in config:
        return config[bstack111111l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ₟")]
  for platform in config.get(bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫ₠"), []):
      if bstack111111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ₡") in platform:
          return platform[bstack111111l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ₢")]
  return None
def bstack1ll11l1l11_opy_(bstack11111l111_opy_):
  try:
    browser_name = bstack11111l111_opy_[bstack111111l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡤࡴࡡ࡮ࡧࠪ₣")]
    browser_version = bstack11111l111_opy_[bstack111111l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ₤")]
    chrome_options = bstack11111l111_opy_[bstack111111l_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪࡥ࡯ࡱࡶ࡬ࡳࡳࡹࠧ₥")]
    try:
        bstack1lllll111lll_opy_ = int(browser_version.split(bstack111111l_opy_ (u"ࠧ࠯ࠩ₦"))[0])
    except ValueError as e:
        logger.error(bstack111111l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡸࡪ࡬ࡰࡪࠦࡣࡰࡰࡹࡩࡷࡺࡩ࡯ࡩࠣࡦࡷࡵࡷࡴࡧࡵࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠧ₧") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack111111l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩ₨")):
        logger.warning(bstack111111l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ₩"))
        return False
    if bstack1lllll111lll_opy_ < bstack1llll1ll11ll_opy_.bstack1l111lllll1_opy_:
        logger.warning(bstack1llll1ll1_opy_ (u"ࠫࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡴࡨࡵࡺ࡯ࡲࡦࡵࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡺࡪࡸࡳࡪࡱࡱࠤࢀࡉࡏࡏࡕࡗࡅࡓ࡚ࡓ࠯ࡏࡌࡒࡎࡓࡕࡎࡡࡑࡓࡓࡥࡂࡔࡖࡄࡇࡐࡥࡉࡏࡈࡕࡅࡤࡇ࠱࠲࡛ࡢࡗ࡚ࡖࡐࡐࡔࡗࡉࡉࡥࡃࡉࡔࡒࡑࡊࡥࡖࡆࡔࡖࡍࡔࡔࡽࠡࡱࡵࠤ࡭࡯ࡧࡩࡧࡵ࠲ࠬ₪"))
        return False
    if chrome_options and any(bstack111111l_opy_ (u"ࠬ࠳࠭ࡩࡧࡤࡨࡱ࡫ࡳࡴࠩ₫") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack111111l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡰࡲࡸࠥࡸࡵ࡯ࠢࡲࡲࠥࡲࡥࡨࡣࡦࡽࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠦࡓࡸ࡫ࡷࡧ࡭ࠦࡴࡰࠢࡱࡩࡼࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪࠦ࡯ࡳࠢࡤࡺࡴ࡯ࡤࠡࡷࡶ࡭ࡳ࡭ࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠣ€"))
        return False
    return True
  except Exception as e:
    logger.error(bstack111111l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡦ࡬ࡪࡩ࡫ࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡳࡶࡲࡳࡳࡷࡺࠠࡧࡱࡵࠤࡱࡵࡣࡢ࡮ࠣࡇ࡭ࡸ࡯࡮ࡧ࠽ࠤࠧ₭") + str(e))
    return False
def bstack1ll1l1ll11_opy_(bstack1l1lllll11_opy_, config):
    try:
      bstack1l1111l1lll_opy_ = bstack111111l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ₮") in config and config[bstack111111l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ₯")] == True
      bstack1llll1ll1l1l_opy_ = bstack111111l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ₰") in config and str(config[bstack111111l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ₱")]).lower() != bstack111111l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫ₲")
      if not (bstack1l1111l1lll_opy_ and (not bstack11l1l1l1ll_opy_(config) or bstack1llll1ll1l1l_opy_)):
        return bstack1l1lllll11_opy_
      bstack1llll1lllll1_opy_ = bstack11l1llll11_opy_.bstack1lllll1l1ll1_opy_
      if bstack1llll1lllll1_opy_ is None:
        logger.debug(bstack111111l_opy_ (u"ࠨࡇࡰࡱࡪࡰࡪࠦࡣࡩࡴࡲࡱࡪࠦ࡯ࡱࡶ࡬ࡳࡳࡹࠠࡢࡴࡨࠤࡓࡵ࡮ࡦࠤ₳"))
        return bstack1l1lllll11_opy_
      bstack1llll1ll11l1_opy_ = int(str(bstack111ll11111l_opy_()).split(bstack111111l_opy_ (u"ࠧ࠯ࠩ₴"))[0])
      logger.debug(bstack111111l_opy_ (u"ࠣࡕࡨࡰࡪࡴࡩࡶ࡯ࠣࡺࡪࡸࡳࡪࡱࡱࠤࡩ࡫ࡴࡦࡥࡷࡩࡩࡀࠠࠣ₵") + str(bstack1llll1ll11l1_opy_) + bstack111111l_opy_ (u"ࠤࠥ₶"))
      if bstack1llll1ll11l1_opy_ == 3 and isinstance(bstack1l1lllll11_opy_, dict) and bstack111111l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ₷") in bstack1l1lllll11_opy_ and bstack1llll1lllll1_opy_ is not None:
        if bstack111111l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ₸") not in bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ₹")]:
          bstack1l1lllll11_opy_[bstack111111l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭₺")][bstack111111l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ₻")] = {}
        if bstack111111l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭₼") in bstack1llll1lllll1_opy_:
          if bstack111111l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ₽") not in bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ₾")][bstack111111l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ₿")]:
            bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃀")][bstack111111l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃁")][bstack111111l_opy_ (u"ࠧࡢࡴࡪࡷࠬ⃂")] = []
          for arg in bstack1llll1lllll1_opy_[bstack111111l_opy_ (u"ࠨࡣࡵ࡫ࡸ࠭⃃")]:
            if arg not in bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴࠩ⃄")][bstack111111l_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃅")][bstack111111l_opy_ (u"ࠫࡦࡸࡧࡴࠩ⃆")]:
              bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃇")][bstack111111l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃈")][bstack111111l_opy_ (u"ࠧࡢࡴࡪࡷࠬ⃉")].append(arg)
        if bstack111111l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ⃊") in bstack1llll1lllll1_opy_:
          if bstack111111l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭⃋") not in bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃌")][bstack111111l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃍")]:
            bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃎")][bstack111111l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃏")][bstack111111l_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃐")] = []
          for ext in bstack1llll1lllll1_opy_[bstack111111l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬ⃑")]:
            if ext not in bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠩࡧࡩࡸ࡯ࡲࡦࡦࡢࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ⃒ࠩ")][bstack111111l_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨ⃓")][bstack111111l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃔")]:
              bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃕")][bstack111111l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃖")][bstack111111l_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃗")].append(ext)
        if bstack111111l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹ⃘ࠧ") in bstack1llll1lllll1_opy_:
          if bstack111111l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ⃙") not in bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃚ࠪ")][bstack111111l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃛")]:
            bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠬࡪࡥࡴ࡫ࡵࡩࡩࡥࡣࡢࡲࡤࡦ࡮ࡲࡩࡵ࡫ࡨࡷࠬ⃜")][bstack111111l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⃝")][bstack111111l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭⃞")] = {}
          bstack1111lll11l1_opy_(bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃟")][bstack111111l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃠")][bstack111111l_opy_ (u"ࠪࡴࡷ࡫ࡦࡴࠩ⃡")],
                    bstack1llll1lllll1_opy_[bstack111111l_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪ⃢")])
        os.environ[bstack111111l_opy_ (u"ࠬࡏࡓࡠࡐࡒࡒࡤࡈࡓࡕࡃࡆࡏࡤࡏࡎࡇࡔࡄࡣࡆ࠷࠱࡚ࡡࡖࡉࡘ࡙ࡉࡐࡐࠪ⃣")] = bstack111111l_opy_ (u"࠭ࡴࡳࡷࡨࠫ⃤")
        return bstack1l1lllll11_opy_
      else:
        chrome_options = None
        if isinstance(bstack1l1lllll11_opy_, ChromeOptions):
          chrome_options = bstack1l1lllll11_opy_
        elif isinstance(bstack1l1lllll11_opy_, dict):
          for value in bstack1l1lllll11_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack1l1lllll11_opy_, dict):
            bstack1l1lllll11_opy_[bstack111111l_opy_ (u"ࠧࡰࡲࡷ࡭ࡴࡴࡳࠨ⃥")] = chrome_options
          else:
            bstack1l1lllll11_opy_ = chrome_options
        if bstack1llll1lllll1_opy_ is not None:
          if bstack111111l_opy_ (u"ࠨࡣࡵ࡫ࡸ⃦࠭") in bstack1llll1lllll1_opy_:
                bstack1lllll11ll1l_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1lllll1_opy_[bstack111111l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ⃧")]
                for arg in new_args:
                    if arg not in bstack1lllll11ll1l_opy_:
                        chrome_options.add_argument(arg)
          if bstack111111l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹ⃨ࠧ") in bstack1llll1lllll1_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack111111l_opy_ (u"ࠫࡪࡾࡴࡦࡰࡶ࡭ࡴࡴࡳࠨ⃩"), [])
                bstack1lllll1111l1_opy_ = bstack1llll1lllll1_opy_[bstack111111l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴ⃪ࠩ")]
                for extension in bstack1lllll1111l1_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack111111l_opy_ (u"࠭ࡰࡳࡧࡩࡷ⃫ࠬ") in bstack1llll1lllll1_opy_:
                bstack1llll1lll1ll_opy_ = chrome_options.experimental_options.get(bstack111111l_opy_ (u"ࠧࡱࡴࡨࡪࡸ⃬࠭"), {})
                bstack1lllll11l11l_opy_ = bstack1llll1lllll1_opy_[bstack111111l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹ⃭ࠧ")]
                bstack1111lll11l1_opy_(bstack1llll1lll1ll_opy_, bstack1lllll11l11l_opy_)
                chrome_options.add_experimental_option(bstack111111l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨ⃮"), bstack1llll1lll1ll_opy_)
        os.environ[bstack111111l_opy_ (u"ࠪࡍࡘࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡇࡖࡗࡎࡕࡎࠨ⃯")] = bstack111111l_opy_ (u"ࠫࡹࡸࡵࡦࠩ⃰")
        return bstack1l1lllll11_opy_
    except Exception as e:
      logger.error(bstack111111l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡥࡩࡪࡩ࡯ࡩࠣࡲࡴࡴ࠭ࡃࡕࠣ࡭ࡳ࡬ࡲࡢࠢࡤ࠵࠶ࡿࠠࡤࡪࡵࡳࡲ࡫ࠠࡰࡲࡷ࡭ࡴࡴࡳ࠻ࠢࠥ⃱") + str(e))
      return bstack1l1lllll11_opy_