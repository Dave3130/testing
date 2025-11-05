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
import logging
import datetime
import threading
from bstack_utils.helper import bstack111l1ll1111_opy_, bstack11l1llll11_opy_, get_host_info, bstack1111lll11l1_opy_, \
 bstack1ll1llll1l_opy_, bstack1l1l1ll1_opy_, error_handler, bstack111l11ll1l1_opy_, bstack1ll111ll_opy_
import bstack_utils.accessibility as bstack1lll11l11_opy_
from bstack_utils.bstack1111111l_opy_ import bstack1llllll11_opy_
from bstack_utils.bstack1lll1l1l_opy_ import bstack1l11l1l1_opy_
from bstack_utils.percy import bstack1ll11l1ll_opy_
from bstack_utils.config import Config
bstack1llllll1l_opy_ = Config.bstack1lll11ll1_opy_()
logger = logging.getLogger(__name__)
percy = bstack1ll11l1ll_opy_()
@error_handler(class_method=False)
def bstack1llll11l11l1_opy_(bs_config, bstack111l11l11l_opy_):
  try:
    data = {
        bstack11ll1ll_opy_ (u"ࠫ࡫ࡵࡲ࡮ࡣࡷࠫ≎"): bstack11ll1ll_opy_ (u"ࠬࡰࡳࡰࡰࠪ≏"),
        bstack11ll1ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺ࡟࡯ࡣࡰࡩࠬ≐"): bs_config.get(bstack11ll1ll_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬ≑"), bstack11ll1ll_opy_ (u"ࠨࠩ≒")),
        bstack11ll1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ≓"): bs_config.get(bstack11ll1ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭≔"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack11ll1ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ≕"): bs_config.get(bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ≖")),
        bstack11ll1ll_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ≗"): bs_config.get(bstack11ll1ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡊࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ≘"), bstack11ll1ll_opy_ (u"ࠨࠩ≙")),
        bstack11ll1ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭≚"): bstack1ll111ll_opy_(),
        bstack11ll1ll_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ≛"): bstack1111lll11l1_opy_(bs_config),
        bstack11ll1ll_opy_ (u"ࠫ࡭ࡵࡳࡵࡡ࡬ࡲ࡫ࡵࠧ≜"): get_host_info(),
        bstack11ll1ll_opy_ (u"ࠬࡩࡩࡠ࡫ࡱࡪࡴ࠭≝"): bstack11l1llll11_opy_(),
        bstack11ll1ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤࡸࡵ࡯ࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭≞"): os.environ.get(bstack11ll1ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗ࠭≟")),
        bstack11ll1ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹ࡟ࡳࡧࡵࡹࡳ࠭≠"): os.environ.get(bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡔࡈࡖ࡚ࡔࠧ≡"), False),
        bstack11ll1ll_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࡣࡨࡵ࡮ࡵࡴࡲࡰࠬ≢"): bstack111l1ll1111_opy_(),
        bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ≣"): bstack1lll1llllll1_opy_(bs_config),
        bstack11ll1ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡦࡨࡸࡦ࡯࡬ࡴࠩ≤"): bstack1llll1111l1l_opy_(bstack111l11l11l_opy_),
        bstack11ll1ll_opy_ (u"࠭ࡰࡳࡱࡧࡹࡨࡺ࡟࡮ࡣࡳࠫ≥"): bstack1llll1111l11_opy_(bs_config, bstack111l11l11l_opy_.get(bstack11ll1ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡹࡸ࡫ࡤࠨ≦"), bstack11ll1ll_opy_ (u"ࠨࠩ≧"))),
        bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫ≨"): bstack1ll1llll1l_opy_(bs_config),
        bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠨ≩"): bstack1lll1llll1l1_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack11ll1ll_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡤࡽࡱࡵࡡࡥࠢࡩࡳࡷࠦࡔࡦࡵࡷࡌࡺࡨ࠺ࠡࠢࡾࢁࠧ≪").format(str(error)))
    return None
def bstack1llll1111l1l_opy_(framework):
  return {
    bstack11ll1ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡏࡣࡰࡩࠬ≫"): framework.get(bstack11ll1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡱࡥࡲ࡫ࠧ≬"), bstack11ll1ll_opy_ (u"ࠧࡑࡻࡷࡩࡸࡺࠧ≭")),
    bstack11ll1ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ≮"): framework.get(bstack11ll1ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭≯")),
    bstack11ll1ll_opy_ (u"ࠪࡷࡩࡱࡖࡦࡴࡶ࡭ࡴࡴࠧ≰"): framework.get(bstack11ll1ll_opy_ (u"ࠫࡸࡪ࡫ࡠࡸࡨࡶࡸ࡯࡯࡯ࠩ≱")),
    bstack11ll1ll_opy_ (u"ࠬࡲࡡ࡯ࡩࡸࡥ࡬࡫ࠧ≲"): bstack11ll1ll_opy_ (u"࠭ࡰࡺࡶ࡫ࡳࡳ࠭≳"),
    bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ≴"): framework.get(bstack11ll1ll_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ≵"))
  }
def bstack1lll1llll1l1_opy_(bs_config):
  bstack11ll1ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡺࡥࡴࡶࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤࡸࡺࡡࡳࡶ࠱ࠎࠥࠦࠢࠣࠤ≶")
  if not bs_config:
    return {}
  bstack111ll1ll11l_opy_ = bstack1llllll11_opy_(bs_config).bstack11l1111111l_opy_(bs_config)
  return bstack111ll1ll11l_opy_
def bstack111lll11l_opy_(bs_config, framework):
  bstack111llll11_opy_ = False
  bstack11l111l111_opy_ = False
  bstack1lll1lllllll_opy_ = False
  if bstack11ll1ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ≷") in bs_config:
    bstack1lll1lllllll_opy_ = True
  elif bstack11ll1ll_opy_ (u"ࠫࡦࡶࡰࠨ≸") in bs_config:
    bstack111llll11_opy_ = True
  else:
    bstack11l111l111_opy_ = True
  bstack1ll11ll1l1_opy_ = {
    bstack11ll1ll_opy_ (u"ࠬࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬ≹"): bstack1l11l1l1_opy_.bstack11l111l1lll_opy_(bs_config, framework),
    bstack11ll1ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭≺"): bstack1lll11l11_opy_.bstack11ll11111_opy_(bs_config),
    bstack11ll1ll_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭≻"): bs_config.get(bstack11ll1ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ≼"), False),
    bstack11ll1ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫ≽"): bstack11l111l111_opy_,
    bstack11ll1ll_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ≾"): bstack111llll11_opy_,
    bstack11ll1ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡶࡧࡦࡲࡥࠨ≿"): bstack1lll1lllllll_opy_
  }
  return bstack1ll11ll1l1_opy_
@error_handler(class_method=False)
def bstack1lll1llllll1_opy_(bs_config):
  try:
    bstack1llll1111ll1_opy_ = json.loads(os.getenv(bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭⊀"), bstack11ll1ll_opy_ (u"࠭ࡻࡾࠩ⊁")))
    bstack1llll1111ll1_opy_ = bstack1lll1lllll1l_opy_(bs_config, bstack1llll1111ll1_opy_)
    return {
        bstack11ll1ll_opy_ (u"ࠧࡴࡧࡷࡸ࡮ࡴࡧࡴࠩ⊂"): bstack1llll1111ll1_opy_
    }
  except Exception as error:
    logger.error(bstack11ll1ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥ࡭ࡥࡵࡡࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࡡࡶࡩࡹࡺࡩ࡯ࡩࡶࠤ࡫ࡵࡲࠡࡖࡨࡷࡹࡎࡵࡣ࠼ࠣࠤࢀࢃࠢ⊃").format(str(error)))
    return {}
def bstack1lll1lllll1l_opy_(bs_config, bstack1llll1111ll1_opy_):
  if ((bstack11ll1ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭⊄") in bs_config or not bstack1ll1llll1l_opy_(bs_config)) and bstack1lll11l11_opy_.bstack11ll11111_opy_(bs_config)):
    bstack1llll1111ll1_opy_[bstack11ll1ll_opy_ (u"ࠥ࡭ࡳࡩ࡬ࡶࡦࡨࡉࡳࡩ࡯ࡥࡧࡧࡉࡽࡺࡥ࡯ࡵ࡬ࡳࡳࠨ⊅")] = True
  return bstack1llll1111ll1_opy_
def bstack1llll111l11l_opy_(array, bstack1llll111111l_opy_, bstack1llll11111ll_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll111111l_opy_]
    result[key] = o[bstack1llll11111ll_opy_]
  return result
def bstack1llll11l1111_opy_(bstack11l1l1ll11_opy_=bstack11ll1ll_opy_ (u"ࠫࠬ⊆")):
  bstack1lll1lllll11_opy_ = bstack1lll11l11_opy_.on()
  bstack1lll1llll1ll_opy_ = bstack1l11l1l1_opy_.on()
  bstack1llll11111l1_opy_ = percy.bstack11l1111ll_opy_()
  if bstack1llll11111l1_opy_ and not bstack1lll1llll1ll_opy_ and not bstack1lll1lllll11_opy_:
    return bstack11l1l1ll11_opy_ not in [bstack11ll1ll_opy_ (u"ࠬࡉࡂࡕࡕࡨࡷࡸ࡯࡯࡯ࡅࡵࡩࡦࡺࡥࡥࠩ⊇"), bstack11ll1ll_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ⊈")]
  elif bstack1lll1lllll11_opy_ and not bstack1lll1llll1ll_opy_:
    return bstack11l1l1ll11_opy_ not in [bstack11ll1ll_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡔࡶࡤࡶࡹ࡫ࡤࠨ⊉"), bstack11ll1ll_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ⊊"), bstack11ll1ll_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭⊋")]
  return bstack1lll1lllll11_opy_ or bstack1lll1llll1ll_opy_ or bstack1llll11111l1_opy_
@error_handler(class_method=False)
def bstack1llll11llll1_opy_(bstack11l1l1ll11_opy_, test=None):
  bstack1llll1111111_opy_ = bstack1lll11l11_opy_.on()
  if not bstack1llll1111111_opy_ or bstack11l1l1ll11_opy_ not in [bstack11ll1ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬ⊌")] or test == None:
    return None
  return {
    bstack11ll1ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ⊍"): bstack1llll1111111_opy_ and bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫ⊎"), None) == True and bstack1lll11l11_opy_.bstack11llll11ll_opy_(test[bstack11ll1ll_opy_ (u"࠭ࡴࡢࡩࡶࠫ⊏")])
  }
def bstack1llll1111l11_opy_(bs_config, framework):
  bstack111llll11_opy_ = False
  bstack11l111l111_opy_ = False
  bstack1lll1lllllll_opy_ = False
  if bstack11ll1ll_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ⊐") in bs_config:
    bstack1lll1lllllll_opy_ = True
  elif bstack11ll1ll_opy_ (u"ࠨࡣࡳࡴࠬ⊑") in bs_config:
    bstack111llll11_opy_ = True
  else:
    bstack11l111l111_opy_ = True
  bstack1ll11ll1l1_opy_ = {
    bstack11ll1ll_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ⊒"): bstack1l11l1l1_opy_.bstack11l111l1lll_opy_(bs_config, framework),
    bstack11ll1ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ⊓"): bstack1lll11l11_opy_.bstack1l1l1l1l1l_opy_(bs_config),
    bstack11ll1ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ⊔"): bs_config.get(bstack11ll1ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ⊕"), False),
    bstack11ll1ll_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ⊖"): bstack11l111l111_opy_,
    bstack11ll1ll_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭⊗"): bstack111llll11_opy_,
    bstack11ll1ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬ⊘"): bstack1lll1lllllll_opy_
  }
  return bstack1ll11ll1l1_opy_