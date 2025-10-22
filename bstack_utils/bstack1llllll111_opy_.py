# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack111l11ll111_opy_, bstack1l1l1l1l1_opy_, get_host_info, bstack1111ll1l11l_opy_, \
 bstack1l11lllll1_opy_, bstack1l111l1l_opy_, error_handler, bstack111l11lllll_opy_, bstack1lllll11_opy_
import bstack_utils.accessibility as bstack1lllll1l1_opy_
from bstack_utils.bstack1llll1ll1_opy_ import bstack111ll1l1_opy_
from bstack_utils.bstack1lll11ll_opy_ import bstack1l1l11ll_opy_
from bstack_utils.percy import bstack111l1lll1l_opy_
from bstack_utils.config import Config
bstack111ll1ll_opy_ = Config.bstack1llll1lll_opy_()
logger = logging.getLogger(__name__)
percy = bstack111l1lll1l_opy_()
@error_handler(class_method=False)
def bstack1llll1l11111_opy_(bs_config, bstack11l1l111ll_opy_):
  try:
    data = {
        bstack11l1l11_opy_ (u"ࠫ࡫ࡵࡲ࡮ࡣࡷࠫ∖"): bstack11l1l11_opy_ (u"ࠬࡰࡳࡰࡰࠪ∗"),
        bstack11l1l11_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺ࡟࡯ࡣࡰࡩࠬ∘"): bs_config.get(bstack11l1l11_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬ∙"), bstack11l1l11_opy_ (u"ࠨࠩ√")),
        bstack11l1l11_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ∛"): bs_config.get(bstack11l1l11_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭∜"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack11l1l11_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ∝"): bs_config.get(bstack11l1l11_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ∞")),
        bstack11l1l11_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ∟"): bs_config.get(bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ∠"), bstack11l1l11_opy_ (u"ࠨࠩ∡")),
        bstack11l1l11_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭∢"): bstack1lllll11_opy_(),
        bstack11l1l11_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ∣"): bstack1111ll1l11l_opy_(bs_config),
        bstack11l1l11_opy_ (u"ࠫ࡭ࡵࡳࡵࡡ࡬ࡲ࡫ࡵࠧ∤"): get_host_info(),
        bstack11l1l11_opy_ (u"ࠬࡩࡩࡠ࡫ࡱࡪࡴ࠭∥"): bstack1l1l1l1l1_opy_(),
        bstack11l1l11_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡸࡵ࡯ࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭∦"): os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭∧")),
        bstack11l1l11_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹ࡟ࡳࡧࡵࡹࡳ࠭∨"): os.environ.get(bstack11l1l11_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠧ∩"), False),
        bstack11l1l11_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࡣࡨࡵ࡮ࡵࡴࡲࡰࠬ∪"): bstack111l11ll111_opy_(),
        bstack11l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ∫"): bstack1llll1111l11_opy_(bs_config),
        bstack11l1l11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡦࡨࡸࡦ࡯࡬ࡴࠩ∬"): bstack1llll1111l1l_opy_(bstack11l1l111ll_opy_),
        bstack11l1l11_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ∭"): bstack1llll1111ll1_opy_(bs_config, bstack11l1l111ll_opy_.get(bstack11l1l11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨ∮"), bstack11l1l11_opy_ (u"ࠨࠩ∯"))),
        bstack11l1l11_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ∰"): bstack1l11lllll1_opy_(bs_config),
        bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠨ∱"): bstack1llll11111ll_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack11l1l11_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡤࡽࡱࡵࡡࡥࠢࡩࡳࡷࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࠢࡾࢁࠧ∲").format(str(error)))
    return None
def bstack1llll1111l1l_opy_(framework):
  return {
    bstack11l1l11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬ∳"): framework.get(bstack11l1l11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠧ∴"), bstack11l1l11_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧ∵")),
    bstack11l1l11_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ∶"): framework.get(bstack11l1l11_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭∷")),
    bstack11l1l11_opy_ (u"ࠪࡷࡩࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ∸"): framework.get(bstack11l1l11_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ∹")),
    bstack11l1l11_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧ∺"): bstack11l1l11_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭∻"),
    bstack11l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ∼"): framework.get(bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ∽"))
  }
def bstack1llll11111ll_opy_(bs_config):
  bstack11l1l11_opy_ (u"ࠤࠥࠦࠏࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤࡸࡺࡡࡳࡶ࠱ࠎࠥࠦࠢࠣࠤ∾")
  if not bs_config:
    return {}
  bstack111llll11l1_opy_ = bstack111ll1l1_opy_(bs_config).bstack111llll1111_opy_(bs_config)
  return bstack111llll11l1_opy_
def bstack1ll11ll1l1_opy_(bs_config, framework):
  bstack11l1lllll_opy_ = False
  bstack11l111ll11_opy_ = False
  bstack1llll111ll1l_opy_ = False
  if bstack11l1l11_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ∿") in bs_config:
    bstack1llll111ll1l_opy_ = True
  elif bstack11l1l11_opy_ (u"ࠫࡦࡶࡰࠨ≀") in bs_config:
    bstack11l1lllll_opy_ = True
  else:
    bstack11l111ll11_opy_ = True
  bstack11111111l_opy_ = {
    bstack11l1l11_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ≁"): bstack1l1l11ll_opy_.bstack11l11l111l1_opy_(bs_config, framework),
    bstack11l1l11_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭≂"): bstack1lllll1l1_opy_.bstack111l1l1ll_opy_(bs_config),
    bstack11l1l11_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭≃"): bs_config.get(bstack11l1l11_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ≄"), False),
    bstack11l1l11_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ≅"): bstack11l111ll11_opy_,
    bstack11l1l11_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ≆"): bstack11l1lllll_opy_,
    bstack11l1l11_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨ≇"): bstack1llll111ll1l_opy_
  }
  return bstack11111111l_opy_
@error_handler(class_method=False)
def bstack1llll1111l11_opy_(bs_config):
  try:
    bstack1llll111l1l1_opy_ = json.loads(os.getenv(bstack11l1l11_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭≈"), bstack11l1l11_opy_ (u"࠭ࡻࡾࠩ≉")))
    bstack1llll111l1l1_opy_ = bstack1llll111l1ll_opy_(bs_config, bstack1llll111l1l1_opy_)
    return {
        bstack11l1l11_opy_ (u"ࠧࡴࡧࡷࡸ࡮ࡴࡧࡴࠩ≊"): bstack1llll111l1l1_opy_
    }
  except Exception as error:
    logger.error(bstack11l1l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡶࡩࡹࡺࡩ࡯ࡩࡶࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࠤࢀࢃࠢ≋").format(str(error)))
    return {}
def bstack1llll111l1ll_opy_(bs_config, bstack1llll111l1l1_opy_):
  if ((bstack11l1l11_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭≌") in bs_config or not bstack1l11lllll1_opy_(bs_config)) and bstack1lllll1l1_opy_.bstack111l1l1ll_opy_(bs_config)):
    bstack1llll111l1l1_opy_[bstack11l1l11_opy_ (u"ࠥ࡭ࡳࡩ࡬ࡶࡦࡨࡉࡳࡩ࡯ࡥࡧࡧࡉࡽࡺࡥ࡯ࡵ࡬ࡳࡳࠨ≍")] = True
  return bstack1llll111l1l1_opy_
def bstack1llll11llll1_opy_(array, bstack1llll111111l_opy_, bstack1llll111l11l_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll111111l_opy_]
    result[key] = o[bstack1llll111l11l_opy_]
  return result
def bstack1llll11l11ll_opy_(bstack1l1l11l1ll_opy_=bstack11l1l11_opy_ (u"ࠫࠬ≎")):
  bstack1llll111l111_opy_ = bstack1lllll1l1_opy_.on()
  bstack1llll11111l1_opy_ = bstack1l1l11ll_opy_.on()
  bstack1llll1111lll_opy_ = percy.bstack1l1l1111l1_opy_()
  if bstack1llll1111lll_opy_ and not bstack1llll11111l1_opy_ and not bstack1llll111l111_opy_:
    return bstack1l1l11l1ll_opy_ not in [bstack11l1l11_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩ≏"), bstack11l1l11_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ≐")]
  elif bstack1llll111l111_opy_ and not bstack1llll11111l1_opy_:
    return bstack1l1l11l1ll_opy_ not in [bstack11l1l11_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ≑"), bstack11l1l11_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ≒"), bstack11l1l11_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭≓")]
  return bstack1llll111l111_opy_ or bstack1llll11111l1_opy_ or bstack1llll1111lll_opy_
@error_handler(class_method=False)
def bstack1llll11ll111_opy_(bstack1l1l11l1ll_opy_, test=None):
  bstack1llll111ll11_opy_ = bstack1lllll1l1_opy_.on()
  if not bstack1llll111ll11_opy_ or bstack1l1l11l1ll_opy_ not in [bstack11l1l11_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ≔")] or test == None:
    return None
  return {
    bstack11l1l11_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ≕"): bstack1llll111ll11_opy_ and bstack1l111l1l_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ≖"), None) == True and bstack1lllll1l1_opy_.bstack1l111lll11_opy_(test[bstack11l1l11_opy_ (u"࠭ࡴࡢࡩࡶࠫ≗")])
  }
def bstack1llll1111ll1_opy_(bs_config, framework):
  bstack11l1lllll_opy_ = False
  bstack11l111ll11_opy_ = False
  bstack1llll111ll1l_opy_ = False
  if bstack11l1l11_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ≘") in bs_config:
    bstack1llll111ll1l_opy_ = True
  elif bstack11l1l11_opy_ (u"ࠨࡣࡳࡴࠬ≙") in bs_config:
    bstack11l1lllll_opy_ = True
  else:
    bstack11l111ll11_opy_ = True
  bstack11111111l_opy_ = {
    bstack11l1l11_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ≚"): bstack1l1l11ll_opy_.bstack11l11l111l1_opy_(bs_config, framework),
    bstack11l1l11_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ≛"): bstack1lllll1l1_opy_.bstack11lll1l1ll_opy_(bs_config),
    bstack11l1l11_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ≜"): bs_config.get(bstack11l1l11_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ≝"), False),
    bstack11l1l11_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ≞"): bstack11l111ll11_opy_,
    bstack11l1l11_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭≟"): bstack11l1lllll_opy_,
    bstack11l1l11_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬ≠"): bstack1llll111ll1l_opy_
  }
  return bstack11111111l_opy_