# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack1111l1llll1_opy_, bstack1l1111111l_opy_, get_host_info, bstack1111l1l1lll_opy_, \
 bstack11l11l1ll_opy_, bstack1l1lll11_opy_, error_handler, bstack1111ll11l11_opy_, bstack11lllll1_opy_
import bstack_utils.accessibility as bstack1111l11l_opy_
from bstack_utils.bstack1111ll1l_opy_ import bstack1lll1l1ll_opy_
from bstack_utils.bstack11lll1ll_opy_ import bstack1lll1lll_opy_
from bstack_utils.percy import bstack1l11ll1ll1_opy_
from bstack_utils.config import Config
bstack11111l11_opy_ = Config.bstack111l11l1_opy_()
logger = logging.getLogger(__name__)
percy = bstack1l11ll1ll1_opy_()
@error_handler(class_method=False)
def bstack1llll11ll111_opy_(bs_config, bstack1lllll1lll_opy_):
  try:
    data = {
        bstack11l111_opy_ (u"ࠪࡪࡴࡸ࡭ࡢࡶࠪ∜"): bstack11l111_opy_ (u"ࠫ࡯ࡹ࡯࡯ࠩ∝"),
        bstack11l111_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡥ࡮ࡢ࡯ࡨࠫ∞"): bs_config.get(bstack11l111_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫ∟"), bstack11l111_opy_ (u"ࠧࠨ∠")),
        bstack11l111_opy_ (u"ࠨࡰࡤࡱࡪ࠭∡"): bs_config.get(bstack11l111_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ∢"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack11l111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭∣"): bs_config.get(bstack11l111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷ࠭∤")),
        bstack11l111_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ∥"): bs_config.get(bstack11l111_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩ∦"), bstack11l111_opy_ (u"ࠧࠨ∧")),
        bstack11l111_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬ∨"): bstack11lllll1_opy_(),
        bstack11l111_opy_ (u"ࠩࡷࡥ࡬ࡹࠧ∩"): bstack1111l1l1lll_opy_(bs_config),
        bstack11l111_opy_ (u"ࠪ࡬ࡴࡹࡴࡠ࡫ࡱࡪࡴ࠭∪"): get_host_info(),
        bstack11l111_opy_ (u"ࠫࡨ࡯࡟ࡪࡰࡩࡳࠬ∫"): bstack1l1111111l_opy_(),
        bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣࡷࡻ࡮ࡠ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠬ∬"): os.environ.get(bstack11l111_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠬ∭")),
        bstack11l111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࡥࡲࡦࡴࡸࡲࠬ∮"): os.environ.get(bstack11l111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡓࡇࡕ࡙ࡓ࠭∯"), False),
        bstack11l111_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࡢࡧࡴࡴࡴࡳࡱ࡯ࠫ∰"): bstack1111l1llll1_opy_(),
        bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ∱"): bstack1llll111l11l_opy_(bs_config),
        bstack11l111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡥࡧࡷࡥ࡮ࡲࡳࠨ∲"): bstack1llll111l1ll_opy_(bstack1lllll1lll_opy_),
        bstack11l111_opy_ (u"ࠬࡶࡲࡰࡦࡸࡧࡹࡥ࡭ࡢࡲࠪ∳"): bstack1llll1111l1l_opy_(bs_config, bstack1lllll1lll_opy_.get(bstack11l111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡸࡷࡪࡪࠧ∴"), bstack11l111_opy_ (u"ࠧࠨ∵"))),
        bstack11l111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠪ∶"): bstack11l11l1ll_opy_(bs_config),
        bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠧ∷"): bstack1llll11111ll_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack11l111_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡩࡲࡦࡣࡷ࡭ࡳ࡭ࠠࡱࡣࡼࡰࡴࡧࡤࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࠡࡽࢀࠦ∸").format(str(error)))
    return None
def bstack1llll111l1ll_opy_(framework):
  return {
    bstack11l111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࡎࡢ࡯ࡨࠫ∹"): framework.get(bstack11l111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡰࡤࡱࡪ࠭∺"), bstack11l111_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠭∻")),
    bstack11l111_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭࡙ࡩࡷࡹࡩࡰࡰࠪ∼"): framework.get(bstack11l111_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ∽")),
    bstack11l111_opy_ (u"ࠩࡶࡨࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭∾"): framework.get(bstack11l111_opy_ (u"ࠪࡷࡩࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨ∿")),
    bstack11l111_opy_ (u"ࠫࡱࡧ࡮ࡨࡷࡤ࡫ࡪ࠭≀"): bstack11l111_opy_ (u"ࠬࡶࡹࡵࡪࡲࡲࠬ≁"),
    bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡊࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭≂"): framework.get(bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡋࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ≃"))
  }
def bstack1llll11111ll_opy_(bs_config):
  bstack11l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦࠣࡷࡹࡧࡲࡵ࠰ࠍࠤࠥࠨࠢࠣ≄")
  if not bs_config:
    return {}
  bstack111llll1lll_opy_ = bstack1lll1l1ll_opy_(bs_config).bstack111lll111l1_opy_(bs_config)
  return bstack111llll1lll_opy_
def bstack1l1llll1ll_opy_(bs_config, framework):
  bstack1lll1111l1_opy_ = False
  bstack11111ll1ll_opy_ = False
  bstack1llll111l111_opy_ = False
  if bstack11l111_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡔࡥࡤࡰࡪ࠭≅") in bs_config:
    bstack1llll111l111_opy_ = True
  elif bstack11l111_opy_ (u"ࠪࡥࡵࡶࠧ≆") in bs_config:
    bstack1lll1111l1_opy_ = True
  else:
    bstack11111ll1ll_opy_ = True
  bstack111ll111l1_opy_ = {
    bstack11l111_opy_ (u"ࠫࡴࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠫ≇"): bstack1lll1lll_opy_.bstack11l11l11l1l_opy_(bs_config, framework),
    bstack11l111_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ≈"): bstack1111l11l_opy_.bstack111ll1l1ll_opy_(bs_config),
    bstack11l111_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ≉"): bs_config.get(bstack11l111_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭≊"), False),
    bstack11l111_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪ≋"): bstack11111ll1ll_opy_,
    bstack11l111_opy_ (u"ࠩࡤࡴࡵࡥࡡࡶࡶࡲࡱࡦࡺࡥࠨ≌"): bstack1lll1111l1_opy_,
    bstack11l111_opy_ (u"ࠪࡸࡺࡸࡢࡰࡵࡦࡥࡱ࡫ࠧ≍"): bstack1llll111l111_opy_
  }
  return bstack111ll111l1_opy_
@error_handler(class_method=False)
def bstack1llll111l11l_opy_(bs_config):
  try:
    bstack1llll111ll1l_opy_ = json.loads(os.getenv(bstack11l111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬ≎"), bstack11l111_opy_ (u"ࠬࢁࡽࠨ≏")))
    bstack1llll111ll1l_opy_ = bstack1llll111l1l1_opy_(bs_config, bstack1llll111ll1l_opy_)
    return {
        bstack11l111_opy_ (u"࠭ࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠨ≐"): bstack1llll111ll1l_opy_
    }
  except Exception as error:
    logger.error(bstack11l111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤ࡬࡫ࡴࡠࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡠࡵࡨࡸࡹ࡯࡮ࡨࡵࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨ≑").format(str(error)))
    return {}
def bstack1llll111l1l1_opy_(bs_config, bstack1llll111ll1l_opy_):
  if ((bstack11l111_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ≒") in bs_config or not bstack11l11l1ll_opy_(bs_config)) and bstack1111l11l_opy_.bstack111ll1l1ll_opy_(bs_config)):
    bstack1llll111ll1l_opy_[bstack11l111_opy_ (u"ࠤ࡬ࡲࡨࡲࡵࡥࡧࡈࡲࡨࡵࡤࡦࡦࡈࡼࡹ࡫࡮ࡴ࡫ࡲࡲࠧ≓")] = True
  return bstack1llll111ll1l_opy_
def bstack1llll1l1111l_opy_(array, bstack1llll1111l11_opy_, bstack1llll1111ll1_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll1111l11_opy_]
    result[key] = o[bstack1llll1111ll1_opy_]
  return result
def bstack1llll11ll1l1_opy_(bstack1ll111111l_opy_=bstack11l111_opy_ (u"ࠪࠫ≔")):
  bstack1llll111ll11_opy_ = bstack1111l11l_opy_.on()
  bstack1llll111llll_opy_ = bstack1lll1lll_opy_.on()
  bstack1llll111lll1_opy_ = percy.bstack1l1lllll1l_opy_()
  if bstack1llll111lll1_opy_ and not bstack1llll111llll_opy_ and not bstack1llll111ll11_opy_:
    return bstack1ll111111l_opy_ not in [bstack11l111_opy_ (u"ࠫࡈࡈࡔࡔࡧࡶࡷ࡮ࡵ࡮ࡄࡴࡨࡥࡹ࡫ࡤࠨ≕"), bstack11l111_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩ≖")]
  elif bstack1llll111ll11_opy_ and not bstack1llll111llll_opy_:
    return bstack1ll111111l_opy_ not in [bstack11l111_opy_ (u"࠭ࡈࡰࡱ࡮ࡖࡺࡴࡓࡵࡣࡵࡸࡪࡪࠧ≗"), bstack11l111_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ≘"), bstack11l111_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬ≙")]
  return bstack1llll111ll11_opy_ or bstack1llll111llll_opy_ or bstack1llll111lll1_opy_
@error_handler(class_method=False)
def bstack1llll1l11ll1_opy_(bstack1ll111111l_opy_, test=None):
  bstack1llll1111lll_opy_ = bstack1111l11l_opy_.on()
  if not bstack1llll1111lll_opy_ or bstack1ll111111l_opy_ not in [bstack11l111_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ≚")] or test == None:
    return None
  return {
    bstack11l111_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ≛"): bstack1llll1111lll_opy_ and bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪ≜"), None) == True and bstack1111l11l_opy_.bstack1llll111ll_opy_(test[bstack11l111_opy_ (u"ࠬࡺࡡࡨࡵࠪ≝")])
  }
def bstack1llll1111l1l_opy_(bs_config, framework):
  bstack1lll1111l1_opy_ = False
  bstack11111ll1ll_opy_ = False
  bstack1llll111l111_opy_ = False
  if bstack11l111_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ≞") in bs_config:
    bstack1llll111l111_opy_ = True
  elif bstack11l111_opy_ (u"ࠧࡢࡲࡳࠫ≟") in bs_config:
    bstack1lll1111l1_opy_ = True
  else:
    bstack11111ll1ll_opy_ = True
  bstack111ll111l1_opy_ = {
    bstack11l111_opy_ (u"ࠨࡱࡥࡷࡪࡸࡶࡢࡤ࡬ࡰ࡮ࡺࡹࠨ≠"): bstack1lll1lll_opy_.bstack11l11l11l1l_opy_(bs_config, framework),
    bstack11l111_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩ≡"): bstack1111l11l_opy_.bstack1l11l111ll_opy_(bs_config),
    bstack11l111_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩ≢"): bs_config.get(bstack11l111_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ≣"), False),
    bstack11l111_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ≤"): bstack11111ll1ll_opy_,
    bstack11l111_opy_ (u"࠭ࡡࡱࡲࡢࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ≥"): bstack1lll1111l1_opy_,
    bstack11l111_opy_ (u"ࠧࡵࡷࡵࡦࡴࡹࡣࡢ࡮ࡨࠫ≦"): bstack1llll111l111_opy_
  }
  return bstack111ll111l1_opy_