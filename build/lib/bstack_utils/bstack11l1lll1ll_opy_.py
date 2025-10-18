# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack111l1l1l11l_opy_, bstack111l1l1l11_opy_, get_host_info, bstack111l1l1lll1_opy_, \
 bstack1ll11llll1_opy_, bstack1l1l11l1_opy_, error_handler, bstack1111l1l1111_opy_, bstack1lll1111_opy_
import bstack_utils.accessibility as bstack1111ll11_opy_
from bstack_utils.bstack11111lll_opy_ import bstack111ll1ll_opy_
from bstack_utils.bstack1l1ll1l1_opy_ import bstack1l1l111l_opy_
from bstack_utils.percy import bstack111l1l1ll1_opy_
from bstack_utils.config import Config
bstack1111l111_opy_ = Config.bstack11111ll1_opy_()
logger = logging.getLogger(__name__)
percy = bstack111l1l1ll1_opy_()
@error_handler(class_method=False)
def bstack1llll11l11l1_opy_(bs_config, bstack1l1l111l1l_opy_):
  try:
    data = {
        bstack11ll_opy_ (u"ࠬ࡬࡯ࡳ࡯ࡤࡸࠬ∞"): bstack11ll_opy_ (u"࠭ࡪࡴࡱࡱࠫ∟"),
        bstack11ll_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡠࡰࡤࡱࡪ࠭∠"): bs_config.get(bstack11ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭∡"), bstack11ll_opy_ (u"ࠩࠪ∢")),
        bstack11ll_opy_ (u"ࠪࡲࡦࡳࡥࠨ∣"): bs_config.get(bstack11ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ∤"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack11ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ∥"): bs_config.get(bstack11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨ∦")),
        bstack11ll_opy_ (u"ࠧࡥࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬ∧"): bs_config.get(bstack11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡄࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫ∨"), bstack11ll_opy_ (u"ࠩࠪ∩")),
        bstack11ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧ∪"): bstack1lll1111_opy_(),
        bstack11ll_opy_ (u"ࠫࡹࡧࡧࡴࠩ∫"): bstack111l1l1lll1_opy_(bs_config),
        bstack11ll_opy_ (u"ࠬ࡮࡯ࡴࡶࡢ࡭ࡳ࡬࡯ࠨ∬"): get_host_info(),
        bstack11ll_opy_ (u"࠭ࡣࡪࡡ࡬ࡲ࡫ࡵࠧ∭"): bstack111l1l1l11_opy_(),
        bstack11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡥࡲࡶࡰࡢ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧ∮"): os.environ.get(bstack11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠧ∯")),
        bstack11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡴࡨࡶࡺࡴࠧ∰"): os.environ.get(bstack11ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠨ∱"), False),
        bstack11ll_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࡤࡩ࡯࡯ࡶࡵࡳࡱ࠭∲"): bstack111l1l1l11l_opy_(),
        bstack11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ∳"): bstack1llll111l1l1_opy_(bs_config),
        bstack11ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡧࡩࡹࡧࡩ࡭ࡵࠪ∴"): bstack1llll1111ll1_opy_(bstack1l1l111l1l_opy_),
        bstack11ll_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࡠ࡯ࡤࡴࠬ∵"): bstack1llll1111l1l_opy_(bs_config, bstack1l1l111l1l_opy_.get(bstack11ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡺࡹࡥࡥࠩ∶"), bstack11ll_opy_ (u"ࠩࠪ∷"))),
        bstack11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬ∸"): bstack1ll11llll1_opy_(bs_config),
        bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠩ∹"): bstack1llll111l1ll_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack11ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡥࡾࡲ࡯ࡢࡦࠣࡪࡴࡸࠠࡕࡧࡶࡸࡍࡻࡢ࠻ࠢࠣࡿࢂࠨ∺").format(str(error)))
    return None
def bstack1llll1111ll1_opy_(framework):
  return {
    bstack11ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡐࡤࡱࡪ࠭∻"): framework.get(bstack11ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡢࡲࡦࡳࡥࠨ∼"), bstack11ll_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨ∽")),
    bstack11ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯࡛࡫ࡲࡴ࡫ࡲࡲࠬ∾"): framework.get(bstack11ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥࡶࡦࡴࡶ࡭ࡴࡴࠧ∿")),
    bstack11ll_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ≀"): framework.get(bstack11ll_opy_ (u"ࠬࡹࡤ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ≁")),
    bstack11ll_opy_ (u"࠭࡬ࡢࡰࡪࡹࡦ࡭ࡥࠨ≂"): bstack11ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧ≃"),
    bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡌࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ≄"): framework.get(bstack11ll_opy_ (u"ࠩࡷࡩࡸࡺࡆࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ≅"))
  }
def bstack1llll111l1ll_opy_(bs_config):
  bstack11ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡴࡦࡵࡷࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨࠥࡹࡴࡢࡴࡷ࠲ࠏࠦࠠࠣࠤࠥ≆")
  if not bs_config:
    return {}
  bstack11l11111l11_opy_ = bstack111ll1ll_opy_(bs_config).bstack111llll1l11_opy_(bs_config)
  return bstack11l11111l11_opy_
def bstack11llll11l_opy_(bs_config, framework):
  bstack1l111lll1_opy_ = False
  bstack1l1l1l1ll_opy_ = False
  bstack1llll1111l11_opy_ = False
  if bstack11ll_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ≇") in bs_config:
    bstack1llll1111l11_opy_ = True
  elif bstack11ll_opy_ (u"ࠬࡧࡰࡱࠩ≈") in bs_config:
    bstack1l111lll1_opy_ = True
  else:
    bstack1l1l1l1ll_opy_ = True
  bstack11lll1l1ll_opy_ = {
    bstack11ll_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭≉"): bstack1l1l111l_opy_.bstack11l111lll1l_opy_(bs_config, framework),
    bstack11ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ≊"): bstack1111ll11_opy_.bstack111ll1ll11_opy_(bs_config),
    bstack11ll_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ≋"): bs_config.get(bstack11ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ≌"), False),
    bstack11ll_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ≍"): bstack1l1l1l1ll_opy_,
    bstack11ll_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪ≎"): bstack1l111lll1_opy_,
    bstack11ll_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ≏"): bstack1llll1111l11_opy_
  }
  return bstack11lll1l1ll_opy_
@error_handler(class_method=False)
def bstack1llll111l1l1_opy_(bs_config):
  try:
    bstack1llll111ll1l_opy_ = json.loads(os.getenv(bstack11ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡢࡅࡈࡉࡅࡔࡕࡌࡆࡎࡒࡉࡕ࡛ࡢࡇࡔࡔࡆࡊࡉࡘࡖࡆ࡚ࡉࡐࡐࡢ࡝ࡒࡒࠧ≐"), bstack11ll_opy_ (u"ࠧࡼࡿࠪ≑")))
    bstack1llll111ll1l_opy_ = bstack1llll111l111_opy_(bs_config, bstack1llll111ll1l_opy_)
    return {
        bstack11ll_opy_ (u"ࠨࡵࡨࡸࡹ࡯࡮ࡨࡵࠪ≒"): bstack1llll111ll1l_opy_
    }
  except Exception as error:
    logger.error(bstack11ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤࡨࡸࡥࡢࡶ࡬ࡲ࡬ࠦࡧࡦࡶࡢࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡢࡷࡪࡺࡴࡪࡰࡪࡷࠥ࡬࡯ࡳࠢࡗࡩࡸࡺࡈࡶࡤ࠽ࠤࠥࢁࡽࠣ≓").format(str(error)))
    return {}
def bstack1llll111l111_opy_(bs_config, bstack1llll111ll1l_opy_):
  if ((bstack11ll_opy_ (u"ࠪࡸࡺࡸࡢࡰࡕࡦࡥࡱ࡫ࠧ≔") in bs_config or not bstack1ll11llll1_opy_(bs_config)) and bstack1111ll11_opy_.bstack111ll1ll11_opy_(bs_config)):
    bstack1llll111ll1l_opy_[bstack11ll_opy_ (u"ࠦ࡮ࡴࡣ࡭ࡷࡧࡩࡊࡴࡣࡰࡦࡨࡨࡊࡾࡴࡦࡰࡶ࡭ࡴࡴࠢ≕")] = True
  return bstack1llll111ll1l_opy_
def bstack1llll11lll1l_opy_(array, bstack1llll11111ll_opy_, bstack1llll111lll1_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll11111ll_opy_]
    result[key] = o[bstack1llll111lll1_opy_]
  return result
def bstack1llll1l111ll_opy_(bstack11l11111l_opy_=bstack11ll_opy_ (u"ࠬ࠭≖")):
  bstack1llll111l11l_opy_ = bstack1111ll11_opy_.on()
  bstack1llll11111l1_opy_ = bstack1l1l111l_opy_.on()
  bstack1llll1111lll_opy_ = percy.bstack1l1llll1l1_opy_()
  if bstack1llll1111lll_opy_ and not bstack1llll11111l1_opy_ and not bstack1llll111l11l_opy_:
    return bstack11l11111l_opy_ not in [bstack11ll_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪ≗"), bstack11ll_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫ≘")]
  elif bstack1llll111l11l_opy_ and not bstack1llll11111l1_opy_:
    return bstack11l11111l_opy_ not in [bstack11ll_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩ≙"), bstack11ll_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫ≚"), bstack11ll_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧ≛")]
  return bstack1llll111l11l_opy_ or bstack1llll11111l1_opy_ or bstack1llll1111lll_opy_
@error_handler(class_method=False)
def bstack1llll11lllll_opy_(bstack11l11111l_opy_, test=None):
  bstack1llll111ll11_opy_ = bstack1111ll11_opy_.on()
  if not bstack1llll111ll11_opy_ or bstack11l11111l_opy_ not in [bstack11ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭≜")] or test == None:
    return None
  return {
    bstack11ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠬ≝"): bstack1llll111ll11_opy_ and bstack1l1l11l1_opy_(threading.current_thread(), bstack11ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ≞"), None) == True and bstack1111ll11_opy_.bstack11l11lll1_opy_(test[bstack11ll_opy_ (u"ࠧࡵࡣࡪࡷࠬ≟")])
  }
def bstack1llll1111l1l_opy_(bs_config, framework):
  bstack1l111lll1_opy_ = False
  bstack1l1l1l1ll_opy_ = False
  bstack1llll1111l11_opy_ = False
  if bstack11ll_opy_ (u"ࠨࡶࡸࡶࡧࡵࡓࡤࡣ࡯ࡩࠬ≠") in bs_config:
    bstack1llll1111l11_opy_ = True
  elif bstack11ll_opy_ (u"ࠩࡤࡴࡵ࠭≡") in bs_config:
    bstack1l111lll1_opy_ = True
  else:
    bstack1l1l1l1ll_opy_ = True
  bstack11lll1l1ll_opy_ = {
    bstack11ll_opy_ (u"ࠪࡳࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪ≢"): bstack1l1l111l_opy_.bstack11l111lll1l_opy_(bs_config, framework),
    bstack11ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫ≣"): bstack1111ll11_opy_.bstack1111l1ll1l_opy_(bs_config),
    bstack11ll_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ≤"): bs_config.get(bstack11ll_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ≥"), False),
    bstack11ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡦࠩ≦"): bstack1l1l1l1ll_opy_,
    bstack11ll_opy_ (u"ࠨࡣࡳࡴࡤࡧࡵࡵࡱࡰࡥࡹ࡫ࠧ≧"): bstack1l111lll1_opy_,
    bstack11ll_opy_ (u"ࠩࡷࡹࡷࡨ࡯ࡴࡥࡤࡰࡪ࠭≨"): bstack1llll1111l11_opy_
  }
  return bstack11lll1l1ll_opy_