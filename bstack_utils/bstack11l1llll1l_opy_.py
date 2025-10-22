# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
import json
import logging
import datetime
import threading
from bstack_utils.helper import bstack1111lll1l1l_opy_, bstack1l1l11llll_opy_, get_host_info, bstack111l1lll11l_opy_, \
 bstack111l1lll11_opy_, bstack1l11l1l1_opy_, error_handler, bstack111l1lll1l1_opy_, bstack1l1111ll_opy_
import bstack_utils.accessibility as bstack1111ll1l_opy_
from bstack_utils.bstack111l1l1l_opy_ import bstack111l11ll_opy_
from bstack_utils.bstack1ll1ll11_opy_ import bstack1ll11l1l_opy_
from bstack_utils.percy import bstack11111lll1l_opy_
from bstack_utils.config import Config
bstack1lll1ll1l_opy_ = Config.bstack1111l1ll_opy_()
logger = logging.getLogger(__name__)
percy = bstack11111lll1l_opy_()
@error_handler(class_method=False)
def bstack1llll11l1lll_opy_(bs_config, bstack1l111l1111_opy_):
  try:
    data = {
        bstack1lllll1l_opy_ (u"ࠨࡨࡲࡶࡲࡧࡴࠨ√"): bstack1lllll1l_opy_ (u"ࠩ࡭ࡷࡴࡴࠧ∛"),
        bstack1lllll1l_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡣࡳࡧ࡭ࡦࠩ∜"): bs_config.get(bstack1lllll1l_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩ∝"), bstack1lllll1l_opy_ (u"ࠬ࠭∞")),
        bstack1lllll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ∟"): bs_config.get(bstack1lllll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪ∠"), os.path.basename(os.path.abspath(os.getcwd()))),
        bstack1lllll1l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ∡"): bs_config.get(bstack1lllll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠫ∢")),
        bstack1lllll1l_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨ∣"): bs_config.get(bstack1lllll1l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡇࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ∤"), bstack1lllll1l_opy_ (u"ࠬ࠭∥")),
        bstack1lllll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ∦"): bstack1l1111ll_opy_(),
        bstack1lllll1l_opy_ (u"ࠧࡵࡣࡪࡷࠬ∧"): bstack111l1lll11l_opy_(bs_config),
        bstack1lllll1l_opy_ (u"ࠨࡪࡲࡷࡹࡥࡩ࡯ࡨࡲࠫ∨"): get_host_info(),
        bstack1lllll1l_opy_ (u"ࠩࡦ࡭ࡤ࡯࡮ࡧࡱࠪ∩"): bstack1l1l11llll_opy_(),
        bstack1lllll1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡡࡵࡹࡳࡥࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪ∪"): os.environ.get(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠪ∫")),
        bstack1lllll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࡣࡷ࡫ࡲࡶࡰࠪ∬"): os.environ.get(bstack1lllll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡘࡅࡓࡗࡑࠫ∭"), False),
        bstack1lllll1l_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࡠࡥࡲࡲࡹࡸ࡯࡭ࠩ∮"): bstack1111lll1l1l_opy_(),
        bstack1lllll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ∯"): bstack1llll1111l1l_opy_(bs_config),
        bstack1lllll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡤࡪࡥࡵࡣ࡬ࡰࡸ࠭∰"): bstack1llll111ll1l_opy_(bstack1l111l1111_opy_),
        bstack1lllll1l_opy_ (u"ࠪࡴࡷࡵࡤࡶࡥࡷࡣࡲࡧࡰࠨ∱"): bstack1llll111llll_opy_(bs_config, bstack1l111l1111_opy_.get(bstack1lllll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡶࡵࡨࡨࠬ∲"), bstack1lllll1l_opy_ (u"ࠬ࠭∳"))),
        bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡆࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠨ∴"): bstack111l1lll11_opy_(bs_config),
        bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡤࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠬ∵"): bstack1llll11111ll_opy_(bs_config)
    }
    return data
  except Exception as error:
    logger.error(bstack1lllll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡶࡡࡺ࡮ࡲࡥࡩࠦࡦࡰࡴࠣࡘࡪࡹࡴࡉࡷࡥ࠾ࠥࠦࡻࡾࠤ∶").format(str(error)))
    return None
def bstack1llll111ll1l_opy_(framework):
  return {
    bstack1lllll1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡓࡧ࡭ࡦࠩ∷"): framework.get(bstack1lllll1l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰࡥ࡮ࡢ࡯ࡨࠫ∸"), bstack1lllll1l_opy_ (u"ࠫࡕࡿࡴࡦࡵࡷࠫ∹")),
    bstack1lllll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨ∺"): framework.get(bstack1lllll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡹࡩࡷࡹࡩࡰࡰࠪ∻")),
    bstack1lllll1l_opy_ (u"ࠧࡴࡦ࡮࡚ࡪࡸࡳࡪࡱࡱࠫ∼"): framework.get(bstack1lllll1l_opy_ (u"ࠨࡵࡧ࡯ࡤࡼࡥࡳࡵ࡬ࡳࡳ࠭∽")),
    bstack1lllll1l_opy_ (u"ࠩ࡯ࡥࡳ࡭ࡵࡢࡩࡨࠫ∾"): bstack1lllll1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪ∿"),
    bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡈࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫ≀"): framework.get(bstack1lllll1l_opy_ (u"ࠬࡺࡥࡴࡶࡉࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ≁"))
  }
def bstack1llll11111ll_opy_(bs_config):
  bstack1lllll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࡗ࡫ࡴࡶࡴࡱࡷࠥࡺࡨࡦࠢࡷࡩࡸࡺࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡵࡷࡥࡷࡺ࠮ࠋࠢࠣࠦࠧࠨ≂")
  if not bs_config:
    return {}
  bstack111lll1l1l1_opy_ = bstack111l11ll_opy_(bs_config).bstack111lll1ll11_opy_(bs_config)
  return bstack111lll1l1l1_opy_
def bstack1l11111ll_opy_(bs_config, framework):
  bstack111l11l1l1_opy_ = False
  bstack11ll1ll1l1_opy_ = False
  bstack1llll111l1ll_opy_ = False
  if bstack1lllll1l_opy_ (u"ࠧࡵࡷࡵࡦࡴ࡙ࡣࡢ࡮ࡨࠫ≃") in bs_config:
    bstack1llll111l1ll_opy_ = True
  elif bstack1lllll1l_opy_ (u"ࠨࡣࡳࡴࠬ≄") in bs_config:
    bstack111l11l1l1_opy_ = True
  else:
    bstack11ll1ll1l1_opy_ = True
  bstack111l1lll1l_opy_ = {
    bstack1lllll1l_opy_ (u"ࠩࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩ≅"): bstack1ll11l1l_opy_.bstack11l111llll1_opy_(bs_config, framework),
    bstack1lllll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠪ≆"): bstack1111ll1l_opy_.bstack111ll111ll_opy_(bs_config),
    bstack1lllll1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪ≇"): bs_config.get(bstack1lllll1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ≈"), False),
    bstack1lllll1l_opy_ (u"࠭ࡡࡶࡶࡲࡱࡦࡺࡥࠨ≉"): bstack11ll1ll1l1_opy_,
    bstack1lllll1l_opy_ (u"ࠧࡢࡲࡳࡣࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭≊"): bstack111l11l1l1_opy_,
    bstack1lllll1l_opy_ (u"ࠨࡶࡸࡶࡧࡵࡳࡤࡣ࡯ࡩࠬ≋"): bstack1llll111l1ll_opy_
  }
  return bstack111l1lll1l_opy_
@error_handler(class_method=False)
def bstack1llll1111l1l_opy_(bs_config):
  try:
    bstack1llll111lll1_opy_ = json.loads(os.getenv(bstack1lllll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡥࡁࡄࡅࡈࡗࡘࡏࡂࡊࡎࡌࡘ࡞ࡥࡃࡐࡐࡉࡍࡌ࡛ࡒࡂࡖࡌࡓࡓࡥ࡙ࡎࡎࠪ≌"), bstack1lllll1l_opy_ (u"ࠪࡿࢂ࠭≍")))
    bstack1llll111lll1_opy_ = bstack1llll111l111_opy_(bs_config, bstack1llll111lll1_opy_)
    return {
        bstack1lllll1l_opy_ (u"ࠫࡸ࡫ࡴࡵ࡫ࡱ࡫ࡸ࠭≎"): bstack1llll111lll1_opy_
    }
  except Exception as error:
    logger.error(bstack1lllll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡪࡩࡹࡥࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡥࡳࡦࡶࡷ࡭ࡳ࡭ࡳࠡࡨࡲࡶ࡚ࠥࡥࡴࡶࡋࡹࡧࡀࠠࠡࡽࢀࠦ≏").format(str(error)))
    return {}
def bstack1llll111l111_opy_(bs_config, bstack1llll111lll1_opy_):
  if ((bstack1lllll1l_opy_ (u"࠭ࡴࡶࡴࡥࡳࡘࡩࡡ࡭ࡧࠪ≐") in bs_config or not bstack111l1lll11_opy_(bs_config)) and bstack1111ll1l_opy_.bstack111ll111ll_opy_(bs_config)):
    bstack1llll111lll1_opy_[bstack1lllll1l_opy_ (u"ࠢࡪࡰࡦࡰࡺࡪࡥࡆࡰࡦࡳࡩ࡫ࡤࡆࡺࡷࡩࡳࡹࡩࡰࡰࠥ≑")] = True
  return bstack1llll111lll1_opy_
def bstack1llll11l1l1l_opy_(array, bstack1llll1111ll1_opy_, bstack1llll111l1l1_opy_):
  result = {}
  for o in array:
    key = o[bstack1llll1111ll1_opy_]
    result[key] = o[bstack1llll111l1l1_opy_]
  return result
def bstack1llll1l111l1_opy_(bstack111l111lll_opy_=bstack1lllll1l_opy_ (u"ࠨࠩ≒")):
  bstack1llll111ll11_opy_ = bstack1111ll1l_opy_.on()
  bstack1llll111l11l_opy_ = bstack1ll11l1l_opy_.on()
  bstack1llll1111l11_opy_ = percy.bstack1lllll11l1_opy_()
  if bstack1llll1111l11_opy_ and not bstack1llll111l11l_opy_ and not bstack1llll111ll11_opy_:
    return bstack111l111lll_opy_ not in [bstack1lllll1l_opy_ (u"ࠩࡆࡆ࡙࡙ࡥࡴࡵ࡬ࡳࡳࡉࡲࡦࡣࡷࡩࡩ࠭≓"), bstack1lllll1l_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧ≔")]
  elif bstack1llll111ll11_opy_ and not bstack1llll111l11l_opy_:
    return bstack111l111lll_opy_ not in [bstack1lllll1l_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ≕"), bstack1lllll1l_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧ≖"), bstack1lllll1l_opy_ (u"࠭ࡌࡰࡩࡆࡶࡪࡧࡴࡦࡦࠪ≗")]
  return bstack1llll111ll11_opy_ or bstack1llll111l11l_opy_ or bstack1llll1111l11_opy_
@error_handler(class_method=False)
def bstack1llll11l111l_opy_(bstack111l111lll_opy_, test=None):
  bstack1llll1111lll_opy_ = bstack1111ll1l_opy_.on()
  if not bstack1llll1111lll_opy_ or bstack111l111lll_opy_ not in [bstack1lllll1l_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩ≘")] or test == None:
    return None
  return {
    bstack1lllll1l_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠨ≙"): bstack1llll1111lll_opy_ and bstack1l11l1l1_opy_(threading.current_thread(), bstack1lllll1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ≚"), None) == True and bstack1111ll1l_opy_.bstack1ll1l11ll_opy_(test[bstack1lllll1l_opy_ (u"ࠪࡸࡦ࡭ࡳࠨ≛")])
  }
def bstack1llll111llll_opy_(bs_config, framework):
  bstack111l11l1l1_opy_ = False
  bstack11ll1ll1l1_opy_ = False
  bstack1llll111l1ll_opy_ = False
  if bstack1lllll1l_opy_ (u"ࠫࡹࡻࡲࡣࡱࡖࡧࡦࡲࡥࠨ≜") in bs_config:
    bstack1llll111l1ll_opy_ = True
  elif bstack1lllll1l_opy_ (u"ࠬࡧࡰࡱࠩ≝") in bs_config:
    bstack111l11l1l1_opy_ = True
  else:
    bstack11ll1ll1l1_opy_ = True
  bstack111l1lll1l_opy_ = {
    bstack1lllll1l_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾ࠭≞"): bstack1ll11l1l_opy_.bstack11l111llll1_opy_(bs_config, framework),
    bstack1lllll1l_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧ≟"): bstack1111ll1l_opy_.bstack111l1l11l_opy_(bs_config),
    bstack1lllll1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ≠"): bs_config.get(bstack1lllll1l_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨ≡"), False),
    bstack1lllll1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬ≢"): bstack11ll1ll1l1_opy_,
    bstack1lllll1l_opy_ (u"ࠫࡦࡶࡰࡠࡣࡸࡸࡴࡳࡡࡵࡧࠪ≣"): bstack111l11l1l1_opy_,
    bstack1lllll1l_opy_ (u"ࠬࡺࡵࡳࡤࡲࡷࡨࡧ࡬ࡦࠩ≤"): bstack1llll111l1ll_opy_
  }
  return bstack111l1lll1l_opy_