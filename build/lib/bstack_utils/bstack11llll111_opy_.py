# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack1111l1l1l11_opy_, bstack111llllll1_opy_, get_host_info, bstack111l1l11ll1_opy_, \
 bstack11l1l1ll1l_opy_, bstack1lll111l_opy_, error_handler, bstack111l1lll11l_opy_, bstack1l1111l1_opy_
import bstack_utils.accessibility as bstack111ll11l_opy_
from bstack_utils.bstack1lll1l1l1_opy_ import bstack11111lll_opy_
from bstack_utils.bstack1lll11l1_opy_ import bstack1ll11l11_opy_
from bstack_utils.percy import bstack11l1lll11_opy_
from bstack_utils.config import Config
bstack1lll1l11l_opy_ = Config.bstack111ll1l1_opy_()
logger = logging.getLogger(__name__)
percy = bstack11l1lll11_opy_()
@error_handler(class_method=False)
def bstack1llll11l111l_opy_(bs_config, bstack1ll1111ll1_opy_):
  try:
    data = {
        bstack11lll1_opy_ (u"ࠫ࡫ࡵࡲ࡮ࡣࡷࠫ∖"): bstack11lll1_opy_ (u"ࠬࡰࡳࡰࡰࠪ∗"),
        bstack11lll1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺ࡟࡯ࡣࡰࡩࠬ∘"): bs_config.get(bstack11lll1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬ∙"), bstack11lll1_opy_ (u"ࠨࠩ√")),
        bstack11lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ∛"): bs_config.get(bstack11lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭∜"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ∝"): bs_config.get(bstack11lll1_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ∞")),
        bstack11lll1_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ∟"): bs_config.get(bstack11lll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ∠"), bstack11lll1_opy_ (u"ࠨࠩ∡")),
        bstack11lll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭∢"): bstack1l1111l1_opy_(),
        bstack11lll1_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ∣"): bstack111l1l11ll1_opy_(bs_config),
        bstack11lll1_opy_ (u"ࠫ࡭ࡵࡳࡵࡡ࡬ࡲ࡫ࡵࠧ∤"): get_host_info(),
        bstack11lll1_opy_ (u"ࠬࡩࡩࡠ࡫ࡱࡪࡴ࠭∥"): bstack111llllll1_opy_(),
        bstack11lll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡸࡵ࡯ࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭∦"): os.environ.get(bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭∧")),
        bstack11lll1_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹ࡟ࡳࡧࡵࡹࡳ࠭∨"): os.environ.get(bstack11lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠧ∩"), False),
        bstack11lll1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࡣࡨࡵ࡮ࡵࡴࡲࡰࠬ∪"): bstack1111l1l1l11_opy_(),
        bstack11lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ∫"): bstack1llll111l1l1_opy_(bs_config),
        bstack11lll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡦࡨࡸࡦ࡯࡬ࡴࠩ∬"): bstack1llll11111ll_opy_(bstack1ll1111ll1_opy_),
        bstack11lll1_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ∭"): bstack1llll1111l11_opy_(bs_config, bstack1ll1111ll1_opy_.get(bstack11lll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨ∮"), bstack11lll1_opy_ (u"ࠨࠩ∯"))),
        bstack11lll1_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ∰"): bstack11l1l1ll1l_opy_(bs_config),
        bstack11lll1_opy_ (u"ࠪࡸࡪࡹࡴࡠࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠨ∱"): bstack1llll1111lll_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack11lll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡤࡽࡱࡵࡡࡥࠢࡩࡳࡷࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࠢࡾࢁࠧ∲").format(str(error)))
    return None
def bstack1llll11111ll_opy_(framework):
  return {
    bstack11lll1_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬ∳"): framework.get(bstack11lll1_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠧ∴"), bstack11lll1_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧ∵")),
    bstack11lll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ∶"): framework.get(bstack11lll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭∷")),
    bstack11lll1_opy_ (u"ࠪࡷࡩࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ∸"): framework.get(bstack11lll1_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ∹")),
    bstack11lll1_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧ∺"): bstack11lll1_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭∻"),
    bstack11lll1_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ∼"): framework.get(bstack11lll1_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ∽"))
  }
def bstack1llll1111lll_opy_(bs_config):
  bstack11lll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤࡸࡺࡡࡳࡶ࠱ࠎࠥࠦࠢࠣࠤ∾")
  if not bs_config:
    return {}
  bstack111ll1lll11_opy_ = bstack11111lll_opy_(bs_config).bstack11l1111l111_opy_(bs_config)
  return bstack111ll1lll11_opy_
def bstack1l1l11l11_opy_(bs_config, framework):
  bstack1l11l1ll1l_opy_ = False
  bstack1ll1l11l1_opy_ = False
  bstack1llll111ll1l_opy_ = False
  if bstack11lll1_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ∿") in bs_config:
    bstack1llll111ll1l_opy_ = True
  elif bstack11lll1_opy_ (u"ࠫࡦࡶࡰࠨ≀") in bs_config:
    bstack1l11l1ll1l_opy_ = True
  else:
    bstack1ll1l11l1_opy_ = True
  bstack111111l11l_opy_ = {
    bstack11lll1_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ≁"): bstack1ll11l11_opy_.bstack11l11l111l1_opy_(bs_config, framework),
    bstack11lll1_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭≂"): bstack111ll11l_opy_.bstack1111lll11l_opy_(bs_config),
    bstack11lll1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭≃"): bs_config.get(bstack11lll1_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ≄"), False),
    bstack11lll1_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ≅"): bstack1ll1l11l1_opy_,
    bstack11lll1_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ≆"): bstack1l11l1ll1l_opy_,
    bstack11lll1_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨ≇"): bstack1llll111ll1l_opy_
  }
  return bstack111111l11l_opy_
@error_handler(class_method=False)
def bstack1llll111l1l1_opy_(bs_config):
  try:
    bstack1llll111ll11_opy_ = json.loads(os.getenv(bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭≈"), bstack11lll1_opy_ (u"࠭ࡻࡾࠩ≉")))
    bstack1llll111ll11_opy_ = bstack1llll111l1ll_opy_(bs_config, bstack1llll111ll11_opy_)
    return {
        bstack11lll1_opy_ (u"ࠧࡴࡧࡷࡸ࡮ࡴࡧࡴࠩ≊"): bstack1llll111ll11_opy_
    }
  except Exception as error:
    logger.error(bstack11lll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡶࡩࡹࡺࡩ࡯ࡩࡶࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࠤࢀࢃࠢ≋").format(str(error)))
    return {}
def bstack1llll111l1ll_opy_(bs_config, bstack1llll111ll11_opy_):
  if ((bstack11lll1_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭≌") in bs_config or not bstack11l1l1ll1l_opy_(bs_config)) and bstack111ll11l_opy_.bstack1111lll11l_opy_(bs_config)):
    bstack1llll111ll11_opy_[bstack11lll1_opy_ (u"ࠥ࡭ࡳࡩ࡬ࡶࡦࡨࡉࡳࡩ࡯ࡥࡧࡧࡉࡽࡺࡥ࡯ࡵ࡬ࡳࡳࠨ≍")] = True
  return bstack1llll111ll11_opy_
def bstack1llll11l1lll_opy_(array, bstack1llll1111l1l_opy_, bstack1llll1111ll1_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll1111l1l_opy_]
    result[key] = o[bstack1llll1111ll1_opy_]
  return result
def bstack1llll1l1111l_opy_(bstack1l11lll11l_opy_=bstack11lll1_opy_ (u"ࠫࠬ≎")):
  bstack1llll111lll1_opy_ = bstack111ll11l_opy_.on()
  bstack1llll111l11l_opy_ = bstack1ll11l11_opy_.on()
  bstack1llll111l111_opy_ = percy.bstack1l1l1lllll_opy_()
  if bstack1llll111l111_opy_ and not bstack1llll111l11l_opy_ and not bstack1llll111lll1_opy_:
    return bstack1l11lll11l_opy_ not in [bstack11lll1_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩ≏"), bstack11lll1_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ≐")]
  elif bstack1llll111lll1_opy_ and not bstack1llll111l11l_opy_:
    return bstack1l11lll11l_opy_ not in [bstack11lll1_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ≑"), bstack11lll1_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ≒"), bstack11lll1_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭≓")]
  return bstack1llll111lll1_opy_ or bstack1llll111l11l_opy_ or bstack1llll111l111_opy_
@error_handler(class_method=False)
def bstack1llll1l11l1l_opy_(bstack1l11lll11l_opy_, test=None):
  bstack1llll11111l1_opy_ = bstack111ll11l_opy_.on()
  if not bstack1llll11111l1_opy_ or bstack1l11lll11l_opy_ not in [bstack11lll1_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ≔")] or test == None:
    return None
  return {
    bstack11lll1_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ≕"): bstack1llll11111l1_opy_ and bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ≖"), None) == True and bstack111ll11l_opy_.bstack11111l1ll_opy_(test[bstack11lll1_opy_ (u"࠭ࡴࡢࡩࡶࠫ≗")])
  }
def bstack1llll1111l11_opy_(bs_config, framework):
  bstack1l11l1ll1l_opy_ = False
  bstack1ll1l11l1_opy_ = False
  bstack1llll111ll1l_opy_ = False
  if bstack11lll1_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ≘") in bs_config:
    bstack1llll111ll1l_opy_ = True
  elif bstack11lll1_opy_ (u"ࠨࡣࡳࡴࠬ≙") in bs_config:
    bstack1l11l1ll1l_opy_ = True
  else:
    bstack1ll1l11l1_opy_ = True
  bstack111111l11l_opy_ = {
    bstack11lll1_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ≚"): bstack1ll11l11_opy_.bstack11l11l111l1_opy_(bs_config, framework),
    bstack11lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ≛"): bstack111ll11l_opy_.bstack11lll1lll_opy_(bs_config),
    bstack11lll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ≜"): bs_config.get(bstack11lll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ≝"), False),
    bstack11lll1_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ≞"): bstack1ll1l11l1_opy_,
    bstack11lll1_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭≟"): bstack1l11l1ll1l_opy_,
    bstack11lll1_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬ≠"): bstack1llll111ll1l_opy_
  }
  return bstack111111l11l_opy_