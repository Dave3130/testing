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
import logging
import datetime
import threading
from bstack_utils.helper import bstack111l11ll1l1_opy_, bstack11l1lllll1_opy_, get_host_info, bstack1111lll1l11_opy_, \
 bstack11111lll1l_opy_, bstack1ll111ll_opy_, error_handler, bstack1111llll11l_opy_, bstack1l111lll_opy_
import bstack_utils.accessibility as bstack111ll1ll_opy_
from bstack_utils.bstack1lll1l11l_opy_ import bstack111l1l1l_opy_
from bstack_utils.bstack1l1l111l_opy_ import bstack1l11111l_opy_
from bstack_utils.percy import bstack11l11lll11_opy_
from bstack_utils.config import Config
bstack111ll1l1_opy_ = Config.bstack111l1111_opy_()
logger = logging.getLogger(__name__)
percy = bstack11l11lll11_opy_()
@error_handler(class_method=False)
def bstack1llll11ll111_opy_(bs_config, bstack111l11l1l1_opy_):
  try:
    data = {
        bstack1lll11l_opy_ (u"ࠬ࡬࡯ࡳ࡯ࡤࡸࠬ∳"): bstack1lll11l_opy_ (u"࠭ࡪࡴࡱࡱࠫ∴"),
        bstack1lll11l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡠࡰࡤࡱࡪ࠭∵"): bs_config.get(bstack1lll11l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭∶"), bstack1lll11l_opy_ (u"ࠩࠪ∷")),
        bstack1lll11l_opy_ (u"ࠪࡲࡦࡳࡥࠨ∸"): bs_config.get(bstack1lll11l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ∹"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack1lll11l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ∺"): bs_config.get(bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ∻")),
        bstack1lll11l_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ∼"): bs_config.get(bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ∽"), bstack1lll11l_opy_ (u"ࠩࠪ∾")),
        bstack1lll11l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ∿"): bstack1l111lll_opy_(),
        bstack1lll11l_opy_ (u"ࠫࡹࡧࡧࡴࠩ≀"): bstack1111lll1l11_opy_(bs_config),
        bstack1lll11l_opy_ (u"ࠬ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠨ≁"): get_host_info(),
        bstack1lll11l_opy_ (u"࠭ࡣࡪࡡ࡬ࡲ࡫ࡵࠧ≂"): bstack11l1lllll1_opy_(),
        bstack1lll11l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡲࡶࡰࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ≃"): os.environ.get(bstack1lll11l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ≄")),
        bstack1lll11l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡴࡨࡶࡺࡴࠧ≅"): os.environ.get(bstack1lll11l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠨ≆"), False),
        bstack1lll11l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡤࡩ࡯࡯ࡶࡵࡳࡱ࠭≇"): bstack111l11ll1l1_opy_(),
        bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ≈"): bstack1llll111l11l_opy_(bs_config),
        bstack1lll11l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡧࡩࡹࡧࡩ࡭ࡵࠪ≉"): bstack1llll1111l11_opy_(bstack111l11l1l1_opy_),
        bstack1lll11l_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ≊"): bstack1llll1111111_opy_(bs_config, bstack111l11l1l1_opy_.get(bstack1lll11l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩ≋"), bstack1lll11l_opy_ (u"ࠩࠪ≌"))),
        bstack1lll11l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ≍"): bstack11111lll1l_opy_(bs_config),
        bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠩ≎"): bstack1llll11111ll_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack1lll11l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡥࡾࡲ࡯ࡢࡦࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨ≏").format(str(error)))
    return None
def bstack1llll1111l11_opy_(framework):
  return {
    bstack1lll11l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭≐"): framework.get(bstack1lll11l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠨ≑"), bstack1lll11l_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ≒")),
    bstack1lll11l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ≓"): framework.get(bstack1lll11l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ≔")),
    bstack1lll11l_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ≕"): framework.get(bstack1lll11l_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ≖")),
    bstack1lll11l_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨ≗"): bstack1lll11l_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ≘"),
    bstack1lll11l_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ≙"): framework.get(bstack1lll11l_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ≚"))
  }
def bstack1llll11111ll_opy_(bs_config):
  bstack1lll11l_opy_ (u"ࠥࠦࠧࠐࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨࠥࡹࡴࡢࡴࡷ࠲ࠏࠦࠠࠣࠤࠥ≛")
  if not bs_config:
    return {}
  bstack111ll1l1l1l_opy_ = bstack111l1l1l_opy_(bs_config).bstack111lll1l111_opy_(bs_config)
  return bstack111ll1l1l1l_opy_
def bstack1ll1ll111_opy_(bs_config, framework):
  bstack1lll11llll_opy_ = False
  bstack1l1ll1lll1_opy_ = False
  bstack1lll1lllllll_opy_ = False
  if bstack1lll11l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ≜") in bs_config:
    bstack1lll1lllllll_opy_ = True
  elif bstack1lll11l_opy_ (u"ࠬࡧࡰࡱࠩ≝") in bs_config:
    bstack1lll11llll_opy_ = True
  else:
    bstack1l1ll1lll1_opy_ = True
  bstack11llll1l1_opy_ = {
    bstack1lll11l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭≞"): bstack1l11111l_opy_.bstack11l111lll1l_opy_(bs_config, framework),
    bstack1lll11l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ≟"): bstack111ll1ll_opy_.bstack1l1111lll1_opy_(bs_config),
    bstack1lll11l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ≠"): bs_config.get(bstack1lll11l_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ≡"), False),
    bstack1lll11l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ≢"): bstack1l1ll1lll1_opy_,
    bstack1lll11l_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪ≣"): bstack1lll11llll_opy_,
    bstack1lll11l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ≤"): bstack1lll1lllllll_opy_
  }
  return bstack11llll1l1_opy_
@error_handler(class_method=False)
def bstack1llll111l11l_opy_(bs_config):
  try:
    bstack1llll11111l1_opy_ = json.loads(os.getenv(bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ≥"), bstack1lll11l_opy_ (u"ࠧࡼࡿࠪ≦")))
    bstack1llll11111l1_opy_ = bstack1llll1111lll_opy_(bs_config, bstack1llll11111l1_opy_)
    return {
        bstack1lll11l_opy_ (u"ࠨࡵࡨࡸࡹ࡯࡮ࡨࡵࠪ≧"): bstack1llll11111l1_opy_
    }
  except Exception as error:
    logger.error(bstack1lll11l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡷࡪࡺࡴࡪࡰࡪࡷࠥ࡬࡯ࡳࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࠥࢁࡽࠣ≨").format(str(error)))
    return {}
def bstack1llll1111lll_opy_(bs_config, bstack1llll11111l1_opy_):
  if ((bstack1lll11l_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ≩") in bs_config or not bstack11111lll1l_opy_(bs_config)) and bstack111ll1ll_opy_.bstack1l1111lll1_opy_(bs_config)):
    bstack1llll11111l1_opy_[bstack1lll11l_opy_ (u"ࠦ࡮ࡴࡣ࡭ࡷࡧࡩࡊࡴࡣࡰࡦࡨࡨࡊࡾࡴࡦࡰࡶ࡭ࡴࡴࠢ≪")] = True
  return bstack1llll11111l1_opy_
def bstack1llll11l1l11_opy_(array, bstack1llll111l111_opy_, bstack1llll1111ll1_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll111l111_opy_]
    result[key] = o[bstack1llll1111ll1_opy_]
  return result
def bstack1llll1l1111l_opy_(bstack11111l11ll_opy_=bstack1lll11l_opy_ (u"ࠬ࠭≫")):
  bstack1llll1111l1l_opy_ = bstack111ll1ll_opy_.on()
  bstack1lll1llllll1_opy_ = bstack1l11111l_opy_.on()
  bstack1llll111l1l1_opy_ = percy.bstack1ll1111ll1_opy_()
  if bstack1llll111l1l1_opy_ and not bstack1lll1llllll1_opy_ and not bstack1llll1111l1l_opy_:
    return bstack11111l11ll_opy_ not in [bstack1lll11l_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪ≬"), bstack1lll11l_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ≭")]
  elif bstack1llll1111l1l_opy_ and not bstack1lll1llllll1_opy_:
    return bstack11111l11ll_opy_ not in [bstack1lll11l_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ≮"), bstack1lll11l_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ≯"), bstack1lll11l_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧ≰")]
  return bstack1llll1111l1l_opy_ or bstack1lll1llllll1_opy_ or bstack1llll111l1l1_opy_
@error_handler(class_method=False)
def bstack1llll11l111l_opy_(bstack11111l11ll_opy_, test=None):
  bstack1llll111111l_opy_ = bstack111ll1ll_opy_.on()
  if not bstack1llll111111l_opy_ or bstack11111l11ll_opy_ not in [bstack1lll11l_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭≱")] or test == None:
    return None
  return {
    bstack1lll11l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ≲"): bstack1llll111111l_opy_ and bstack1ll111ll_opy_(threading.current_thread(), bstack1lll11l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ≳"), None) == True and bstack111ll1ll_opy_.bstack111111l1l1_opy_(test[bstack1lll11l_opy_ (u"ࠧࡵࡣࡪࡷࠬ≴")])
  }
def bstack1llll1111111_opy_(bs_config, framework):
  bstack1lll11llll_opy_ = False
  bstack1l1ll1lll1_opy_ = False
  bstack1lll1lllllll_opy_ = False
  if bstack1lll11l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ≵") in bs_config:
    bstack1lll1lllllll_opy_ = True
  elif bstack1lll11l_opy_ (u"ࠩࡤࡴࡵ࠭≶") in bs_config:
    bstack1lll11llll_opy_ = True
  else:
    bstack1l1ll1lll1_opy_ = True
  bstack11llll1l1_opy_ = {
    bstack1lll11l_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ≷"): bstack1l11111l_opy_.bstack11l111lll1l_opy_(bs_config, framework),
    bstack1lll11l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ≸"): bstack111ll1ll_opy_.bstack1111111l1_opy_(bs_config),
    bstack1lll11l_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ≹"): bs_config.get(bstack1lll11l_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ≺"), False),
    bstack1lll11l_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩ≻"): bstack1l1ll1lll1_opy_,
    bstack1lll11l_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ≼"): bstack1lll11llll_opy_,
    bstack1lll11l_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭≽"): bstack1lll1lllllll_opy_
  }
  return bstack11llll1l1_opy_