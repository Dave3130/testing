# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import os
import json
import requests
import logging
import threading
import bstack_utils.constants as bstack1lllll111111_opy_
from urllib.parse import urlparse
from bstack_utils.constants import bstack11l1l111111_opy_ as bstack1llll1l1ll11_opy_, EVENTS
from bstack_utils.bstack111ll11l11_opy_ import bstack111ll11l11_opy_
from bstack_utils.helper import bstack1lllll11_opy_, bstack1l1ll111_opy_, bstack11l1l111l_opy_, bstack111l1ll111l_opy_, \
  bstack111l11l1l1l_opy_, bstack1l1l1llll1_opy_, get_host_info, bstack1111l11l111_opy_, bstack11llll111_opy_, error_handler, bstack111l111lll1_opy_, bstack1111l111ll1_opy_, bstack1l11l1ll_opy_
from browserstack_sdk._version import __version__
from bstack_utils.bstack1l11l1lll_opy_ import get_logger
from bstack_utils.bstack1l11l1l11_opy_ import bstack1llllll11ll_opy_
from selenium.webdriver.chrome.options import Options as ChromeOptions
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.constants import *
logger = get_logger(__name__)
bstack1l11l1l11_opy_ = bstack1llllll11ll_opy_()
@error_handler(class_method=False)
def _1llll1l1llll_opy_(driver, bstack1llll11l1_opy_):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack111l1l_opy_ (u"ࠩࡲࡷࡤࡴࡡ࡮ࡧࠪῤ"): caps.get(bstack111l1l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠩῥ"), None),
        bstack111l1l_opy_ (u"ࠫࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨῦ"): bstack1llll11l1_opy_.get(bstack111l1l_opy_ (u"ࠬࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠨῧ"), None),
        bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸ࡟࡯ࡣࡰࡩࠬῨ"): caps.get(bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬῩ"), None),
        bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠪῪ"): caps.get(bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪΎ"), None)
    }
  except Exception as error:
    logger.debug(bstack111l1l_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡦࡶࡤ࡭ࡱࡹࠠࡸ࡫ࡷ࡬ࠥ࡫ࡲࡳࡱࡵࠤ࠿ࠦࠧῬ") + str(error))
  return response
def on():
    if os.environ.get(bstack111l1l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩ῭"), None) is None or os.environ[bstack111l1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ΅")] == bstack111l1l_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦ`"):
        return False
    return True
def bstack1l1lllll1l_opy_(config):
  return config.get(bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ῰"), False) or any([p.get(bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ῱"), False) == True for p in config.get(bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬῲ"), [])])
def bstack1l1l1111l_opy_(config, bstack1l1lll11ll_opy_):
  try:
    bstack1llll1llll1l_opy_ = config.get(bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪῳ"), False)
    if int(bstack1l1lll11ll_opy_) < len(config.get(bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧῴ"), [])) and config[bstack111l1l_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨ῵")][bstack1l1lll11ll_opy_]:
      bstack1llll1lll1ll_opy_ = config[bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩῶ")][bstack1l1lll11ll_opy_].get(bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧῷ"), None)
    else:
      bstack1llll1lll1ll_opy_ = config.get(bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨῸ"), None)
    if bstack1llll1lll1ll_opy_ != None:
      bstack1llll1llll1l_opy_ = bstack1llll1lll1ll_opy_
    bstack1llll1ll11ll_opy_ = os.getenv(bstack111l1l_opy_ (u"ࠩࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠧΌ")) is not None and len(os.getenv(bstack111l1l_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨῺ"))) > 0 and os.getenv(bstack111l1l_opy_ (u"ࠫࡇ࡙࡟ࡂ࠳࠴࡝ࡤࡐࡗࡕࠩΏ")) != bstack111l1l_opy_ (u"ࠬࡴࡵ࡭࡮ࠪῼ")
    return bstack1llll1llll1l_opy_ and bstack1llll1ll11ll_opy_
  except Exception as error:
    logger.debug(bstack111l1l_opy_ (u"࠭ࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡼࡥࡳ࡫ࡩࡽ࡮ࡴࡧࠡࡶ࡫ࡩࠥࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡪࡸࡲࡰࡴࠣ࠾ࠥ࠭´") + str(error))
  return False
def bstack1l1ll11lll_opy_(test_tags):
  bstack1l1111lll1l_opy_ = os.getenv(bstack111l1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡣࡆࡉࡃࡆࡕࡖࡍࡇࡏࡌࡊࡖ࡜ࡣࡈࡕࡎࡇࡋࡊ࡙ࡗࡇࡔࡊࡑࡑࡣ࡞ࡓࡌࠨ῾"))
  if bstack1l1111lll1l_opy_ is None:
    return True
  bstack1l1111lll1l_opy_ = json.loads(bstack1l1111lll1l_opy_)
  try:
    include_tags = bstack1l1111lll1l_opy_[bstack111l1l_opy_ (u"ࠨ࡫ࡱࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ࠭῿")] if bstack111l1l_opy_ (u"ࠩ࡬ࡲࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ ") in bstack1l1111lll1l_opy_ and isinstance(bstack1l1111lll1l_opy_[bstack111l1l_opy_ (u"ࠪ࡭ࡳࡩ࡬ࡶࡦࡨࡘࡦ࡭ࡳࡊࡰࡗࡩࡸࡺࡩ࡯ࡩࡖࡧࡴࡶࡥࠨ ")], list) else []
    exclude_tags = bstack1l1111lll1l_opy_[bstack111l1l_opy_ (u"ࠫࡪࡾࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ ")] if bstack111l1l_opy_ (u"ࠬ࡫ࡸࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪ ") in bstack1l1111lll1l_opy_ and isinstance(bstack1l1111lll1l_opy_[bstack111l1l_opy_ (u"࠭ࡥࡹࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫ ")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack111l1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡷࡩ࡫࡯ࡩࠥࡼࡡ࡭࡫ࡧࡥࡹ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡬࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡧࡦࡴ࡮ࡪࡰࡪ࠲ࠥࡋࡲࡳࡱࡵࠤ࠿ࠦࠢ ") + str(error))
  return False
def bstack1llll1l11lll_opy_(config, frameworkName, bstack1llll1lll111_opy_, bstack1llll1ll11l1_opy_):
  bstack1llll1l1l11l_opy_ = bstack111l1ll111l_opy_(config)
  bstack1llll1llll11_opy_ = bstack111l11l1l1l_opy_(config)
  if bstack1llll1l1l11l_opy_ is None or bstack1llll1llll11_opy_ is None:
    logger.error(bstack111l1l_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡶࡺࡴࠠࡧࡱࡵࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩ "))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ "), bstack111l1l_opy_ (u"ࠪࡿࢂ࠭ ")))
    data = {
        bstack111l1l_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ "): config[bstack111l1l_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ ")],
        bstack111l1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ​"): config.get(bstack111l1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ‌"), os.path.basename(os.getcwd())),
        bstack111l1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡔࡪ࡯ࡨࠫ‍"): bstack1lllll11_opy_(),
        bstack111l1l_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ‎"): config.get(bstack111l1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡆࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭‏"), bstack111l1l_opy_ (u"ࠫࠬ‐")),
        bstack111l1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ‑"): {
            bstack111l1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭‒"): frameworkName,
            bstack111l1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ–"): bstack1llll1lll111_opy_,
            bstack111l1l_opy_ (u"ࠨࡵࡧ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ—"): __version__,
            bstack111l1l_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ―"): bstack111l1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ‖"),
            bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ‗"): bstack111l1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧ‘"),
            bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭’"): bstack1llll1ll11l1_opy_
        },
        bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡸ࡮ࡴࡧࡴࠩ‚"): settings,
        bstack111l1l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࡅࡲࡲࡹࡸ࡯࡭ࠩ‛"): bstack1111l11l111_opy_(),
        bstack111l1l_opy_ (u"ࠩࡦ࡭ࡎࡴࡦࡰࠩ“"): bstack1l1l1llll1_opy_(),
        bstack111l1l_opy_ (u"ࠪ࡬ࡴࡹࡴࡊࡰࡩࡳࠬ”"): get_host_info(),
        bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳ࠭„"): bstack11l1l111l_opy_(config)
    }
    headers = {
        bstack111l1l_opy_ (u"ࠬࡉ࡯࡯ࡶࡨࡲࡹ࠳ࡔࡺࡲࡨࠫ‟"): bstack111l1l_opy_ (u"࠭ࡡࡱࡲ࡯࡭ࡨࡧࡴࡪࡱࡱ࠳࡯ࡹ࡯࡯ࠩ†"),
    }
    config = {
        bstack111l1l_opy_ (u"ࠧࡢࡷࡷ࡬ࠬ‡"): (bstack1llll1l1l11l_opy_, bstack1llll1llll11_opy_),
        bstack111l1l_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩ•"): headers
    }
    response = bstack11llll111_opy_(bstack111l1l_opy_ (u"ࠩࡓࡓࡘ࡚ࠧ‣"), bstack1llll1l1ll11_opy_ + bstack111l1l_opy_ (u"ࠪ࠳ࡻ࠸࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵࠪ․"), data, config)
    bstack1llll1ll1ll1_opy_ = response.json()
    if bstack1llll1ll1ll1_opy_[bstack111l1l_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬ‥")]:
      parsed = json.loads(os.getenv(bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭…"), bstack111l1l_opy_ (u"࠭ࡻࡾࠩ‧")))
      parsed[bstack111l1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ ")] = bstack1llll1ll1ll1_opy_[bstack111l1l_opy_ (u"ࠨࡦࡤࡸࡦ࠭ ")][bstack111l1l_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪ‪")]
      os.environ[bstack111l1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫ‫")] = json.dumps(parsed)
      bstack111ll11l11_opy_.bstack11llll11l_opy_(bstack1llll1ll1ll1_opy_[bstack111l1l_opy_ (u"ࠫࡩࡧࡴࡢࠩ‬")][bstack111l1l_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭‭")])
      bstack111ll11l11_opy_.bstack1lllll11l11l_opy_(bstack1llll1ll1ll1_opy_[bstack111l1l_opy_ (u"࠭ࡤࡢࡶࡤࠫ‮")][bstack111l1l_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴࠩ ")])
      bstack111ll11l11_opy_.store()
      return bstack1llll1ll1ll1_opy_[bstack111l1l_opy_ (u"ࠨࡦࡤࡸࡦ࠭‰")][bstack111l1l_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡖࡲ࡯ࡪࡴࠧ‱")], bstack1llll1ll1ll1_opy_[bstack111l1l_opy_ (u"ࠪࡨࡦࡺࡡࠨ′")][bstack111l1l_opy_ (u"ࠫ࡮ࡪࠧ″")]
    else:
      logger.error(bstack111l1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡳࡷࡱࡲ࡮ࡴࡧࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱ࠾ࠥ࠭‴") + bstack1llll1ll1ll1_opy_[bstack111l1l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ‵")])
      if bstack1llll1ll1ll1_opy_[bstack111l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ‶")] == bstack111l1l_opy_ (u"ࠨࡋࡱࡺࡦࡲࡩࡥࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡳࡥࡸࡹࡥࡥ࠰ࠪ‷"):
        for bstack1llll1lll1l1_opy_ in bstack1llll1ll1ll1_opy_[bstack111l1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࡴࠩ‸")]:
          logger.error(bstack1llll1lll1l1_opy_[bstack111l1l_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ‹")])
      return None, None
  except Exception as error:
    logger.error(bstack111l1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࠧ›") +  str(error))
    return None, None
def bstack1llll1ll1111_opy_():
  if os.getenv(bstack111l1l_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪ※")) is None:
    return {
        bstack111l1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭‼"): bstack111l1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭‽"),
        bstack111l1l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ‾"): bstack111l1l_opy_ (u"ࠩࡅࡹ࡮ࡲࡤࠡࡥࡵࡩࡦࡺࡩࡰࡰࠣ࡬ࡦࡪࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠨ‿")
    }
  data = {bstack111l1l_opy_ (u"ࠪࡩࡳࡪࡔࡪ࡯ࡨࠫ⁀"): bstack1lllll11_opy_()}
  headers = {
      bstack111l1l_opy_ (u"ࠫࡆࡻࡴࡩࡱࡵ࡭ࡿࡧࡴࡪࡱࡱࠫ⁁"): bstack111l1l_opy_ (u"ࠬࡈࡥࡢࡴࡨࡶࠥ࠭⁂") + os.getenv(bstack111l1l_opy_ (u"ࠨࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠦ⁃")),
      bstack111l1l_opy_ (u"ࠧࡄࡱࡱࡸࡪࡴࡴ࠮ࡖࡼࡴࡪ࠭⁄"): bstack111l1l_opy_ (u"ࠨࡣࡳࡴࡱ࡯ࡣࡢࡶ࡬ࡳࡳ࠵ࡪࡴࡱࡱࠫ⁅")
  }
  response = bstack11llll111_opy_(bstack111l1l_opy_ (u"ࠩࡓ࡙࡙࠭⁆"), bstack1llll1l1ll11_opy_ + bstack111l1l_opy_ (u"ࠪ࠳ࡹ࡫ࡳࡵࡡࡵࡹࡳࡹ࠯ࡴࡶࡲࡴࠬ⁇"), data, { bstack111l1l_opy_ (u"ࠫ࡭࡫ࡡࡥࡧࡵࡷࠬ⁈"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack111l1l_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡖࡨࡷࡹࠦࡒࡶࡰࠣࡱࡦࡸ࡫ࡦࡦࠣࡥࡸࠦࡣࡰ࡯ࡳࡰࡪࡺࡥࡥࠢࡤࡸࠥࠨ⁉") + bstack1l1ll111_opy_().isoformat() + bstack111l1l_opy_ (u"࡚࠭ࠨ⁊"))
      return {bstack111l1l_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧ⁋"): bstack111l1l_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩ⁌"), bstack111l1l_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ⁍"): bstack111l1l_opy_ (u"ࠪࠫ⁎")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack111l1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡤࡱࡰࡴࡱ࡫ࡴࡪࡱࡱࠤࡴ࡬ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡘࡪࡹࡴࠡࡔࡸࡲ࠿ࠦࠢ⁏") + str(error))
    return {
        bstack111l1l_opy_ (u"ࠬࡹࡴࡢࡶࡸࡷࠬ⁐"): bstack111l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ⁑"),
        bstack111l1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ⁒"): str(error)
    }
def bstack1llll1l1l1ll_opy_(bstack1llll1l11ll1_opy_):
    return re.match(bstack111l1l_opy_ (u"ࡳࠩࡡࡠࡩ࠱ࠨ࡝࠰࡟ࡨ࠰࠯࠿ࠥࠩ⁓"), bstack1llll1l11ll1_opy_.strip()) is not None
def bstack1l1llll1ll_opy_(caps, options, desired_capabilities={}, config=None):
    try:
        if options:
          bstack1lllll11111l_opy_ = options.to_capabilities()
        elif desired_capabilities:
          bstack1lllll11111l_opy_ = desired_capabilities
        else:
          bstack1lllll11111l_opy_ = {}
        bstack1l11111lll1_opy_ = (bstack1lllll11111l_opy_.get(bstack111l1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠨ⁔"), bstack111l1l_opy_ (u"ࠪࠫ⁕")).lower() or caps.get(bstack111l1l_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠪ⁖"), bstack111l1l_opy_ (u"ࠬ࠭⁗")).lower())
        if bstack1l11111lll1_opy_ == bstack111l1l_opy_ (u"࠭ࡩࡰࡵࠪ⁘"):
            return True
        if bstack1l11111lll1_opy_ == bstack111l1l_opy_ (u"ࠧࡢࡰࡧࡶࡴ࡯ࡤࠨ⁙"):
            bstack1l1111l111l_opy_ = str(float(caps.get(bstack111l1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠪ⁚")) or bstack1lllll11111l_opy_.get(bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁛"), {}).get(bstack111l1l_opy_ (u"ࠪࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳ࠭⁜"),bstack111l1l_opy_ (u"ࠫࠬ⁝"))))
            if bstack1l11111lll1_opy_ == bstack111l1l_opy_ (u"ࠬࡧ࡮ࡥࡴࡲ࡭ࡩ࠭⁞") and int(bstack1l1111l111l_opy_.split(bstack111l1l_opy_ (u"࠭࠮ࠨ "))[0]) < float(bstack11l1l11l1ll_opy_):
                logger.warning(str(bstack11l1l11l1l1_opy_))
                return False
            return True
        bstack1l1111l11l1_opy_ = caps.get(bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁠"), {}).get(bstack111l1l_opy_ (u"ࠨࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠬ⁡"), caps.get(bstack111l1l_opy_ (u"ࠩࡧࡩࡻ࡯ࡣࡦࠩ⁢"), bstack111l1l_opy_ (u"ࠪࠫ⁣")))
        if bstack1l1111l11l1_opy_:
            logger.warning(bstack111l1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦࡲࡶࡰࠣࡳࡳࡲࡹࠡࡱࡱࠤࡉ࡫ࡳ࡬ࡶࡲࡴࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣ⁤"))
            return False
        browser = caps.get(bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠪ⁥"), bstack111l1l_opy_ (u"࠭ࠧ⁦")).lower() or bstack1lllll11111l_opy_.get(bstack111l1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬ⁧"), bstack111l1l_opy_ (u"ࠨࠩ⁨")).lower()
        if browser != bstack111l1l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩ⁩"):
            logger.warning(bstack111l1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡸࡵ࡯ࠢࡲࡲࡱࡿࠠࡰࡰࠣࡇ࡭ࡸ࡯࡮ࡧࠣࡦࡷࡵࡷࡴࡧࡵࡷ࠳ࠨ⁪"))
            return False
        browser_version = caps.get(bstack111l1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ⁫")) or caps.get(bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ⁬")) or bstack1lllll11111l_opy_.get(bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧ⁭")) or bstack1lllll11111l_opy_.get(bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ⁮"), {}).get(bstack111l1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠩ⁯")) or bstack1lllll11111l_opy_.get(bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ⁰"), {}).get(bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬⁱ"))
        bstack1l11111ll1l_opy_ = bstack1lllll111111_opy_.bstack1l111l1111l_opy_
        bstack1llll1ll1lll_opy_ = False
        if config is not None:
          bstack1llll1ll1lll_opy_ = bstack111l1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ⁲") in config and str(config[bstack111l1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡗࡨࡧ࡬ࡦࠩ⁳")]).lower() != bstack111l1l_opy_ (u"࠭ࡦࡢ࡮ࡶࡩࠬ⁴")
        if os.environ.get(bstack111l1l_opy_ (u"ࠧࡊࡕࡢࡒࡔࡔ࡟ࡃࡕࡗࡅࡈࡑ࡟ࡊࡐࡉࡖࡆࡥࡁ࠲࠳࡜ࡣࡘࡋࡓࡔࡋࡒࡒࠬ⁵"), bstack111l1l_opy_ (u"ࠨࠩ⁶")).lower() == bstack111l1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ⁷") or bstack1llll1ll1lll_opy_:
          bstack1l11111ll1l_opy_ = bstack1lllll111111_opy_.bstack1l111ll11l1_opy_
        if browser_version and browser_version != bstack111l1l_opy_ (u"ࠪࡰࡦࡺࡥࡴࡶࠪ⁸") and int(browser_version.split(bstack111l1l_opy_ (u"ࠫ࠳࠭⁹"))[0]) <= bstack1l11111ll1l_opy_:
          logger.warning(bstack1lll1llll1l_opy_ (u"ࠬࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡨࡴࡨࡥࡹ࡫ࡲࠡࡶ࡫ࡥࡳࠦࡻ࡮࡫ࡱࡣࡦ࠷࠱ࡺࡡࡶࡹࡵࡶ࡯ࡳࡶࡨࡨࡤࡩࡨࡳࡱࡰࡩࡤࡼࡥࡳࡵ࡬ࡳࡳࢃ࠮ࠨ⁺"))
          return False
        if not options:
          bstack1l111ll11ll_opy_ = caps.get(bstack111l1l_opy_ (u"࠭ࡧࡰࡱࡪ࠾ࡨ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ⁻")) or bstack1lllll11111l_opy_.get(bstack111l1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ⁼"), {})
          if bstack111l1l_opy_ (u"ࠨ࠯࠰࡬ࡪࡧࡤ࡭ࡧࡶࡷࠬ⁽") in bstack1l111ll11ll_opy_.get(bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡹࠧ⁾"), []):
              logger.warning(bstack111l1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡵࡹࡳࠦ࡯࡯ࠢ࡯ࡩ࡬ࡧࡣࡺࠢ࡫ࡩࡦࡪ࡬ࡦࡵࡶࠤࡲࡵࡤࡦ࠰ࠣࡗࡼ࡯ࡴࡤࡪࠣࡸࡴࠦ࡮ࡦࡹࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧࠣࡳࡷࠦࡡࡷࡱ࡬ࡨࠥࡻࡳࡪࡰࡪࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨ࠲ࠧⁿ"))
              return False
        return True
    except Exception as error:
        logger.debug(bstack111l1l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡺࡦࡲࡩࡥࡣࡷࡩࠥࡧ࠱࠲ࡻࠣࡷࡺࡶࡰࡰࡴࡷࠤ࠿ࠨ₀") + str(error))
        return False
def set_capabilities(caps, config):
  try:
    bstack1l11ll11l1l_opy_ = config.get(bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬ₁"), {})
    bstack1l11ll11l1l_opy_[bstack111l1l_opy_ (u"࠭ࡡࡶࡶ࡫ࡘࡴࡱࡥ࡯ࠩ₂")] = os.getenv(bstack111l1l_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ₃"))
    bstack1111ll11111_opy_ = json.loads(os.getenv(bstack111l1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡤࡇࡃࡄࡇࡖࡗࡎࡈࡉࡍࡋࡗ࡝ࡤࡉࡏࡏࡈࡌࡋ࡚ࡘࡁࡕࡋࡒࡒࡤ࡟ࡍࡍࠩ₄"), bstack111l1l_opy_ (u"ࠩࡾࢁࠬ₅"))).get(bstack111l1l_opy_ (u"ࠪࡷࡨࡧ࡮࡯ࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫ₆"))
    if not config[bstack111l1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡓࡶࡴࡪࡵࡤࡶࡐࡥࡵ࠭₇")].get(bstack111l1l_opy_ (u"ࠧࡧࡰࡱࡡࡤࡹࡹࡵ࡭ࡢࡶࡨࠦ₈")):
      if bstack111l1l_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧ₉") in caps:
        caps[bstack111l1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱ࠺ࡰࡲࡷ࡭ࡴࡴࡳࠨ₊")][bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨ₋")] = bstack1l11ll11l1l_opy_
        caps[bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ₌")][bstack111l1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ₍")][bstack111l1l_opy_ (u"ࠫࡸࡩࡡ࡯ࡰࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ₎")] = bstack1111ll11111_opy_
      else:
        caps[bstack111l1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࡓࡵࡺࡩࡰࡰࡶࠫ₏")] = bstack1l11ll11l1l_opy_
        caps[bstack111l1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬₐ")][bstack111l1l_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨₑ")] = bstack1111ll11111_opy_
  except Exception as error:
    logger.debug(bstack111l1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡪࡺࡴࡪࡰࡪࠤࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ࠮ࠡࡇࡵࡶࡴࡸ࠺ࠡࠤₒ") +  str(error))
def bstack1lll1lll11_opy_(driver, bstack1llll1l1lll1_opy_):
  try:
    setattr(driver, bstack111l1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡃ࠴࠵ࡾ࡙ࡨࡰࡷ࡯ࡨࡘࡩࡡ࡯ࠩₓ"), True)
    session = driver.session_id
    if session:
      bstack1llll1llllll_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1llll1llllll_opy_ = False
      bstack1llll1llllll_opy_ = url.scheme in [bstack111l1l_opy_ (u"ࠥ࡬ࡹࡺࡰࠣₔ"), bstack111l1l_opy_ (u"ࠦ࡭ࡺࡴࡱࡵࠥₕ")]
      if bstack1llll1llllll_opy_:
        if bstack1llll1l1lll1_opy_:
          logger.info(bstack111l1l_opy_ (u"࡙ࠧࡥࡵࡷࡳࠤ࡫ࡵࡲࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡶࡨࡷࡹ࡯࡮ࡨࠢ࡫ࡥࡸࠦࡳࡵࡣࡵࡸࡪࡪ࠮ࠡࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡣࡧࡪ࡭ࡳࠦ࡭ࡰ࡯ࡨࡲࡹࡧࡲࡪ࡮ࡼ࠲ࠧₖ"))
      return bstack1llll1l1lll1_opy_
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤࡸࡩࡡ࡯ࠢࡩࡳࡷࠦࡴࡩ࡫ࡶࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤₗ") + str(e))
    return False
def bstack111l11ll_opy_(driver, name, path):
  try:
    bstack1l111l111l1_opy_ = {
        bstack111l1l_opy_ (u"ࠧࡵࡪࡗࡩࡸࡺࡒࡶࡰࡘࡹ࡮ࡪࠧₘ"): threading.current_thread().current_test_uuid,
        bstack111l1l_opy_ (u"ࠨࡶ࡫ࡆࡺ࡯࡬ࡥࡗࡸ࡭ࡩ࠭ₙ"): os.environ.get(bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧₚ"), bstack111l1l_opy_ (u"ࠪࠫₛ")),
        bstack111l1l_opy_ (u"ࠫࡹ࡮ࡊࡸࡶࡗࡳࡰ࡫࡮ࠨₜ"): os.environ.get(bstack111l1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤࡐࡗࡕࠩ₝"), bstack111l1l_opy_ (u"࠭ࠧ₞"))
    }
    bstack1ll11l11lll_opy_ = bstack1l11l1l11_opy_.bstack1ll11lllll1_opy_(EVENTS.bstack1ll111l1l1_opy_.value)
    logger.debug(bstack111l1l_opy_ (u"ࠧࡑࡧࡵࡪࡴࡸ࡭ࡪࡰࡪࠤࡸࡩࡡ࡯ࠢࡥࡩ࡫ࡵࡲࡦࠢࡶࡥࡻ࡯࡮ࡨࠢࡵࡩࡸࡻ࡬ࡵࡵࠪ₟"))
    try:
      if (bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠨ࡫ࡶࡅࡵࡶࡁ࠲࠳ࡼࡘࡪࡹࡴࠨ₠"), None) and bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠩࡤࡴࡵࡇ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ₡"), None)):
        scripts = {bstack111l1l_opy_ (u"ࠪࡷࡨࡧ࡮ࠨ₢"): bstack111ll11l11_opy_.perform_scan}
        bstack1lllll1111l1_opy_ = json.loads(scripts[bstack111l1l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ₣")].replace(bstack111l1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ₤"), bstack111l1l_opy_ (u"ࠨࠢ₥")))
        bstack1lllll1111l1_opy_[bstack111l1l_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪ₦")][bstack111l1l_opy_ (u"ࠨ࡯ࡨࡸ࡭ࡵࡤࠨ₧")] = None
        scripts[bstack111l1l_opy_ (u"ࠤࡶࡧࡦࡴࠢ₨")] = bstack111l1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࠨ₩") + json.dumps(bstack1lllll1111l1_opy_)
        bstack111ll11l11_opy_.bstack11llll11l_opy_(scripts)
        bstack111ll11l11_opy_.store()
        logger.debug(driver.execute_script(bstack111ll11l11_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack111ll11l11_opy_.perform_scan, {bstack111l1l_opy_ (u"ࠦࡲ࡫ࡴࡩࡱࡧࠦ₪"): name}))
      bstack1l11l1l11_opy_.end(EVENTS.bstack1ll111l1l1_opy_.value, bstack1ll11l11lll_opy_ + bstack111l1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ₫"), bstack1ll11l11lll_opy_ + bstack111l1l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ€"), True, None)
    except Exception as error:
      bstack1l11l1l11_opy_.end(EVENTS.bstack1ll111l1l1_opy_.value, bstack1ll11l11lll_opy_ + bstack111l1l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ₭"), bstack1ll11l11lll_opy_ + bstack111l1l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ₮"), False, str(error))
    bstack1ll11l11lll_opy_ = bstack1l11l1l11_opy_.bstack11ll1l11ll1_opy_(EVENTS.bstack1l111ll111l_opy_.value)
    bstack1l11l1l11_opy_.mark(bstack1ll11l11lll_opy_ + bstack111l1l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ₯"))
    try:
      if (bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠪ࡭ࡸࡇࡰࡱࡃ࠴࠵ࡾ࡚ࡥࡴࡶࠪ₰"), None) and bstack1l11l1ll_opy_(threading.current_thread(), bstack111l1l_opy_ (u"ࠫࡦࡶࡰࡂ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭₱"), None)):
        scripts = {bstack111l1l_opy_ (u"ࠬࡹࡣࡢࡰࠪ₲"): bstack111ll11l11_opy_.perform_scan}
        bstack1lllll1111l1_opy_ = json.loads(scripts[bstack111l1l_opy_ (u"ࠨࡳࡤࡣࡱࠦ₳")].replace(bstack111l1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࠥ₴"), bstack111l1l_opy_ (u"ࠣࠤ₵")))
        bstack1lllll1111l1_opy_[bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ₶")][bstack111l1l_opy_ (u"ࠪࡱࡪࡺࡨࡰࡦࠪ₷")] = None
        scripts[bstack111l1l_opy_ (u"ࠦࡸࡩࡡ࡯ࠤ₸")] = bstack111l1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࠣ₹") + json.dumps(bstack1lllll1111l1_opy_)
        bstack111ll11l11_opy_.bstack11llll11l_opy_(scripts)
        bstack111ll11l11_opy_.store()
        logger.debug(driver.execute_script(bstack111ll11l11_opy_.perform_scan))
      else:
        logger.debug(driver.execute_async_script(bstack111ll11l11_opy_.bstack1lllll111l1l_opy_, bstack1l111l111l1_opy_))
      bstack1l11l1l11_opy_.end(bstack1ll11l11lll_opy_, bstack1ll11l11lll_opy_ + bstack111l1l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ₺"), bstack1ll11l11lll_opy_ + bstack111l1l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧ₻"),True, None)
    except Exception as error:
      bstack1l11l1l11_opy_.end(bstack1ll11l11lll_opy_, bstack1ll11l11lll_opy_ + bstack111l1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣ₼"), bstack1ll11l11lll_opy_ + bstack111l1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢ₽"),False, str(error))
    logger.info(bstack111l1l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡶ࡫࡭ࡸࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢ࡫ࡥࡸࠦࡥ࡯ࡦࡨࡨ࠳ࠨ₾"))
  except Exception as bstack1l11111llll_opy_:
    logger.error(bstack111l1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡷ࡫ࡳࡶ࡮ࡷࡷࠥࡩ࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤࡵࡸ࡯ࡤࡧࡶࡷࡪࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨ₿") + str(path) + bstack111l1l_opy_ (u"ࠧࠦࡅࡳࡴࡲࡶࠥࡀࠢ⃀") + str(bstack1l11111llll_opy_))
def bstack1llll1ll111l_opy_(driver):
    caps = driver.capabilities
    if caps.get(bstack111l1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ⃁")) and str(caps.get(bstack111l1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ⃂"))).lower() == bstack111l1l_opy_ (u"ࠣࡣࡱࡨࡷࡵࡩࡥࠤ⃃"):
        bstack1l1111l111l_opy_ = caps.get(bstack111l1l_opy_ (u"ࠤࡤࡴࡵ࡯ࡵ࡮࠼ࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ⃄")) or caps.get(bstack111l1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ⃅"))
        if bstack1l1111l111l_opy_ and int(str(bstack1l1111l111l_opy_)) < bstack11l1l11l1ll_opy_:
            return False
    return True
def bstack11ll1l1ll1_opy_(config):
  if bstack111l1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⃆") in config:
        return config[bstack111l1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ⃇")]
  for platform in config.get(bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩ⃈"), []):
      if bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃉") in platform:
          return platform[bstack111l1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ⃊")]
  return None
def bstack111111l1l_opy_(bstack1lll111l1l_opy_):
  try:
    browser_name = bstack1lll111l1l_opy_[bstack111l1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡲࡦࡳࡥࠨ⃋")]
    browser_version = bstack1lll111l1l_opy_[bstack111l1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ⃌")]
    chrome_options = bstack1lll111l1l_opy_[bstack111l1l_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࡣࡴࡶࡴࡪࡱࡱࡷࠬ⃍")]
    try:
        bstack1llll1l1ll1l_opy_ = int(browser_version.split(bstack111l1l_opy_ (u"ࠬ࠴ࠧ⃎"))[0])
    except ValueError as e:
        logger.error(bstack111l1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡨࡵ࡮ࡷࡧࡵࡸ࡮ࡴࡧࠡࡤࡵࡳࡼࡹࡥࡳࠢࡹࡩࡷࡹࡩࡰࡰࠥ⃏") + str(e))
        return False
    if not (browser_name and browser_name.lower() == bstack111l1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧ⃐")):
        logger.warning(bstack111l1l_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡅ࡫ࡶࡴࡳࡥࠡࡤࡵࡳࡼࡹࡥࡳࡵ࠱ࠦ⃑"))
        return False
    if bstack1llll1l1ll1l_opy_ < bstack1lllll111111_opy_.bstack1l111ll11l1_opy_:
        logger.warning(bstack1lll1llll1l_opy_ (u"ࠩࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡳࠡࡅ࡫ࡶࡴࡳࡥࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡾࡇࡔࡔࡓࡕࡃࡑࡘࡘ࠴ࡍࡊࡐࡌࡑ࡚ࡓ࡟ࡏࡑࡑࡣࡇ࡙ࡔࡂࡅࡎࡣࡎࡔࡆࡓࡃࡢࡅ࠶࠷࡙ࡠࡕࡘࡔࡕࡕࡒࡕࡇࡇࡣࡈࡎࡒࡐࡏࡈࡣ࡛ࡋࡒࡔࡋࡒࡒࢂࠦ࡯ࡳࠢ࡫࡭࡬࡮ࡥࡳ࠰⃒ࠪ"))
        return False
    if chrome_options and any(bstack111l1l_opy_ (u"ࠪ࠱࠲࡮ࡥࡢࡦ࡯ࡩࡸࡹ⃓ࠧ") in value for value in chrome_options.values() if isinstance(value, str)):
        logger.warning(bstack111l1l_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡶࡺࡴࠠࡰࡰࠣࡰࡪ࡭ࡡࡤࡻࠣ࡬ࡪࡧࡤ࡭ࡧࡶࡷࠥࡳ࡯ࡥࡧ࠱ࠤࡘࡽࡩࡵࡥ࡫ࠤࡹࡵࠠ࡯ࡧࡺࠤ࡭࡫ࡡࡥ࡮ࡨࡷࡸࠦ࡭ࡰࡦࡨࠤࡴࡸࠠࡢࡸࡲ࡭ࡩࠦࡵࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠨ⃔"))
        return False
    return True
  except Exception as e:
    logger.error(bstack111l1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡤࡪࡨࡧࡰ࡯࡮ࡨࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡸࡻࡰࡱࡱࡵࡸࠥ࡬࡯ࡳࠢ࡯ࡳࡨࡧ࡬ࠡࡅ࡫ࡶࡴࡳࡥ࠻ࠢࠥ⃕") + str(e))
    return False
def bstack11ll1llll1_opy_(bstack1ll111ll11_opy_, config):
    try:
      bstack1l11111l1ll_opy_ = bstack111l1l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭⃖") in config and config[bstack111l1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ⃗")] == True
      bstack1llll1ll1lll_opy_ = bstack111l1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩ⃘ࠬ") in config and str(config[bstack111l1l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ⃙࠭")]).lower() != bstack111l1l_opy_ (u"ࠪࡪࡦࡲࡳࡦ⃚ࠩ")
      if not (bstack1l11111l1ll_opy_ and (not bstack11l1l111l_opy_(config) or bstack1llll1ll1lll_opy_)):
        return bstack1ll111ll11_opy_
      bstack1llll1lll11l_opy_ = bstack111ll11l11_opy_.bstack1lllll111l11_opy_
      if bstack1llll1lll11l_opy_ is None:
        logger.debug(bstack111l1l_opy_ (u"ࠦࡌࡵ࡯ࡨ࡮ࡨࠤࡨ࡮ࡲࡰ࡯ࡨࠤࡴࡶࡴࡪࡱࡱࡷࠥࡧࡲࡦࠢࡑࡳࡳ࡫ࠢ⃛"))
        return bstack1ll111ll11_opy_
      bstack1llll1l1l1l1_opy_ = int(str(bstack1111l111ll1_opy_()).split(bstack111l1l_opy_ (u"ࠬ࠴ࠧ⃜"))[0])
      logger.debug(bstack111l1l_opy_ (u"ࠨࡓࡦ࡮ࡨࡲ࡮ࡻ࡭ࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡧࡩࡹ࡫ࡣࡵࡧࡧ࠾ࠥࠨ⃝") + str(bstack1llll1l1l1l1_opy_) + bstack111l1l_opy_ (u"ࠢࠣ⃞"))
      if bstack1llll1l1l1l1_opy_ == 3 and isinstance(bstack1ll111ll11_opy_, dict) and bstack111l1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃟") in bstack1ll111ll11_opy_ and bstack1llll1lll11l_opy_ is not None:
        if bstack111l1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃠") not in bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃡")]:
          bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠫࡩ࡫ࡳࡪࡴࡨࡨࡤࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫ⃢")][bstack111l1l_opy_ (u"ࠬ࡭࡯ࡰࡩ࠽ࡧ࡭ࡸ࡯࡮ࡧࡒࡴࡹ࡯࡯࡯ࡵࠪ⃣")] = {}
        if bstack111l1l_opy_ (u"࠭ࡡࡳࡩࡶࠫ⃤") in bstack1llll1lll11l_opy_:
          if bstack111l1l_opy_ (u"ࠧࡢࡴࡪࡷ⃥ࠬ") not in bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃦")][bstack111l1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃧")]:
            bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃨ࠪ")][bstack111l1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃩")][bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡵ⃪ࠪ")] = []
          for arg in bstack1llll1lll11l_opy_[bstack111l1l_opy_ (u"࠭ࡡࡳࡩࡶ⃫ࠫ")]:
            if arg not in bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹ⃬ࠧ")][bstack111l1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ⃭࠭")][bstack111l1l_opy_ (u"ࠩࡤࡶ࡬ࡹ⃮ࠧ")]:
              bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵ⃯ࠪ")][bstack111l1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃰")][bstack111l1l_opy_ (u"ࠬࡧࡲࡨࡵࠪ⃱")].append(arg)
        if bstack111l1l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃲") in bstack1llll1lll11l_opy_:
          if bstack111l1l_opy_ (u"ࠧࡦࡺࡷࡩࡳࡹࡩࡰࡰࡶࠫ⃳") not in bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨ⃴")][bstack111l1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ⃵")]:
            bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃶")][bstack111l1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃷")][bstack111l1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃸")] = []
          for ext in bstack1llll1lll11l_opy_[bstack111l1l_opy_ (u"࠭ࡥࡹࡶࡨࡲࡸ࡯࡯࡯ࡵࠪ⃹")]:
            if ext not in bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠧࡥࡧࡶ࡭ࡷ࡫ࡤࡠࡥࡤࡴࡦࡨࡩ࡭࡫ࡷ࡭ࡪࡹࠧ⃺")][bstack111l1l_opy_ (u"ࠨࡩࡲࡳ࡬ࡀࡣࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭⃻")][bstack111l1l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭⃼")]:
              bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ⃽")][bstack111l1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ⃾")][bstack111l1l_opy_ (u"ࠬ࡫ࡸࡵࡧࡱࡷ࡮ࡵ࡮ࡴࠩ⃿")].append(ext)
        if bstack111l1l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬ℀") in bstack1llll1lll11l_opy_:
          if bstack111l1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭℁") not in bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠨࡦࡨࡷ࡮ࡸࡥࡥࡡࡦࡥࡵࡧࡢࡪ࡮࡬ࡸ࡮࡫ࡳࠨℂ")][bstack111l1l_opy_ (u"ࠩࡪࡳࡴ࡭࠺ࡤࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧ℃")]:
            bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠪࡨࡪࡹࡩࡳࡧࡧࡣࡨࡧࡰࡢࡤ࡬ࡰ࡮ࡺࡩࡦࡵࠪ℄")][bstack111l1l_opy_ (u"ࠫ࡬ࡵ࡯ࡨ࠼ࡦ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠩ℅")][bstack111l1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ℆")] = {}
          bstack111l111lll1_opy_(bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"࠭ࡤࡦࡵ࡬ࡶࡪࡪ࡟ࡤࡣࡳࡥࡧ࡯࡬ࡪࡶ࡬ࡩࡸ࠭ℇ")][bstack111l1l_opy_ (u"ࠧࡨࡱࡲ࡫࠿ࡩࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ℈")][bstack111l1l_opy_ (u"ࠨࡲࡵࡩ࡫ࡹࠧ℉")],
                    bstack1llll1lll11l_opy_[bstack111l1l_opy_ (u"ࠩࡳࡶࡪ࡬ࡳࠨℊ")])
        os.environ[bstack111l1l_opy_ (u"ࠪࡍࡘࡥࡎࡐࡐࡢࡆࡘ࡚ࡁࡄࡍࡢࡍࡓࡌࡒࡂࡡࡄ࠵࠶࡟࡟ࡔࡇࡖࡗࡎࡕࡎࠨℋ")] = bstack111l1l_opy_ (u"ࠫࡹࡸࡵࡦࠩℌ")
        return bstack1ll111ll11_opy_
      else:
        chrome_options = None
        if isinstance(bstack1ll111ll11_opy_, ChromeOptions):
          chrome_options = bstack1ll111ll11_opy_
        elif isinstance(bstack1ll111ll11_opy_, dict):
          for value in bstack1ll111ll11_opy_.values():
            if isinstance(value, ChromeOptions):
              chrome_options = value
              break
        if chrome_options is None:
          chrome_options = ChromeOptions()
          if isinstance(bstack1ll111ll11_opy_, dict):
            bstack1ll111ll11_opy_[bstack111l1l_opy_ (u"ࠬࡵࡰࡵ࡫ࡲࡲࡸ࠭ℍ")] = chrome_options
          else:
            bstack1ll111ll11_opy_ = chrome_options
        if bstack1llll1lll11l_opy_ is not None:
          if bstack111l1l_opy_ (u"࠭ࡡࡳࡩࡶࠫℎ") in bstack1llll1lll11l_opy_:
                bstack1llll1l1l111_opy_ = chrome_options.arguments or []
                new_args = bstack1llll1lll11l_opy_[bstack111l1l_opy_ (u"ࠧࡢࡴࡪࡷࠬℏ")]
                for arg in new_args:
                    if arg not in bstack1llll1l1l111_opy_:
                        chrome_options.add_argument(arg)
          if bstack111l1l_opy_ (u"ࠨࡧࡻࡸࡪࡴࡳࡪࡱࡱࡷࠬℐ") in bstack1llll1lll11l_opy_:
                existing_extensions = chrome_options.experimental_options.get(bstack111l1l_opy_ (u"ࠩࡨࡼࡹ࡫࡮ࡴ࡫ࡲࡲࡸ࠭ℑ"), [])
                bstack1llll1ll1l11_opy_ = bstack1llll1lll11l_opy_[bstack111l1l_opy_ (u"ࠪࡩࡽࡺࡥ࡯ࡵ࡬ࡳࡳࡹࠧℒ")]
                for extension in bstack1llll1ll1l11_opy_:
                    if extension not in existing_extensions:
                        chrome_options.add_encoded_extension(extension)
          if bstack111l1l_opy_ (u"ࠫࡵࡸࡥࡧࡵࠪℓ") in bstack1llll1lll11l_opy_:
                bstack1llll1lllll1_opy_ = chrome_options.experimental_options.get(bstack111l1l_opy_ (u"ࠬࡶࡲࡦࡨࡶࠫ℔"), {})
                bstack1llll1ll1l1l_opy_ = bstack1llll1lll11l_opy_[bstack111l1l_opy_ (u"࠭ࡰࡳࡧࡩࡷࠬℕ")]
                bstack111l111lll1_opy_(bstack1llll1lllll1_opy_, bstack1llll1ll1l1l_opy_)
                chrome_options.add_experimental_option(bstack111l1l_opy_ (u"ࠧࡱࡴࡨࡪࡸ࠭№"), bstack1llll1lllll1_opy_)
        os.environ[bstack111l1l_opy_ (u"ࠨࡋࡖࡣࡓࡕࡎࡠࡄࡖࡘࡆࡉࡋࡠࡋࡑࡊࡗࡇ࡟ࡂ࠳࠴࡝ࡤ࡙ࡅࡔࡕࡌࡓࡓ࠭℗")] = bstack111l1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ℘")
        return bstack1ll111ll11_opy_
    except Exception as e:
      logger.error(bstack111l1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡣࡧࡨ࡮ࡴࡧࠡࡰࡲࡲ࠲ࡈࡓࠡ࡫ࡱࡪࡷࡧࠠࡢ࠳࠴ࡽࠥࡩࡨࡳࡱࡰࡩࠥࡵࡰࡵ࡫ࡲࡲࡸࡀࠠࠣℙ") + str(e))
      return bstack1ll111ll11_opy_