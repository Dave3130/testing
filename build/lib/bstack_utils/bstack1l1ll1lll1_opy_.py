# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import os
import json
from bstack_utils.bstack11ll1l11l1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll111111_opy_(object):
  bstack1111llll1l_opy_ = os.path.join(os.path.expanduser(bstack11l1111_opy_ (u"ࠬࢄࠧῼ")), bstack11l1111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭´"))
  bstack1llll1llll11_opy_ = os.path.join(bstack1111llll1l_opy_, bstack11l1111_opy_ (u"ࠧࡤࡱࡰࡱࡦࡴࡤࡴ࠰࡭ࡷࡴࡴࠧ῾"))
  commands_to_wrap = None
  perform_scan = None
  bstack11llll11l_opy_ = None
  bstack11ll11lll1_opy_ = None
  bstack1llll1llll1l_opy_ = None
  bstack1lllll11111l_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11l1111_opy_ (u"ࠨ࡫ࡱࡷࡹࡧ࡮ࡤࡧࠪ῿")):
      cls.instance = super(bstack1lllll111111_opy_, cls).__new__(cls)
      cls.instance.bstack1llll1lllll1_opy_()
    return cls.instance
  def bstack1llll1lllll1_opy_(self):
    try:
      with open(self.bstack1llll1llll11_opy_, bstack11l1111_opy_ (u"ࠩࡵࠫ ")) as bstack1ll111l1ll_opy_:
        bstack1llll1lll1ll_opy_ = bstack1ll111l1ll_opy_.read()
        data = json.loads(bstack1llll1lll1ll_opy_)
        if bstack11l1111_opy_ (u"ࠪࡧࡴࡳ࡭ࡢࡰࡧࡷࠬ ") in data:
          self.bstack1llll1llllll_opy_(data[bstack11l1111_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ ")])
        if bstack11l1111_opy_ (u"ࠬࡹࡣࡳ࡫ࡳࡸࡸ࠭ ") in data:
          self.bstack1l11lll1l_opy_(data[bstack11l1111_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧ ")])
        if bstack11l1111_opy_ (u"ࠧ࡯ࡱࡱࡆࡘࡺࡡࡤ࡭ࡌࡲ࡫ࡸࡡࡂ࠳࠴ࡽࡈ࡮ࡲࡰ࡯ࡨࡓࡵࡺࡩࡰࡰࡶࠫ ") in data:
          self.bstack1lllll1111l1_opy_(data[bstack11l1111_opy_ (u"ࠨࡰࡲࡲࡇ࡙ࡴࡢࡥ࡮ࡍࡳ࡬ࡲࡢࡃ࠴࠵ࡾࡉࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬ ")])
    except:
      pass
  def bstack1lllll1111l1_opy_(self, bstack1lllll11111l_opy_):
    if bstack1lllll11111l_opy_ != None:
      self.bstack1lllll11111l_opy_ = bstack1lllll11111l_opy_
  def bstack1l11lll1l_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack11l1111_opy_ (u"ࠩࡶࡧࡦࡴࠧ "),bstack11l1111_opy_ (u"ࠪࠫ "))
      self.bstack11llll11l_opy_ = scripts.get(bstack11l1111_opy_ (u"ࠫ࡬࡫ࡴࡓࡧࡶࡹࡱࡺࡳࠨ "),bstack11l1111_opy_ (u"ࠬ࠭ "))
      self.bstack11ll11lll1_opy_ = scripts.get(bstack11l1111_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࡖࡹࡲࡳࡡࡳࡻࠪ​"),bstack11l1111_opy_ (u"ࠧࠨ‌"))
      self.bstack1llll1llll1l_opy_ = scripts.get(bstack11l1111_opy_ (u"ࠨࡵࡤࡺࡪࡘࡥࡴࡷ࡯ࡸࡸ࠭‍"),bstack11l1111_opy_ (u"ࠩࠪ‎"))
  def bstack1llll1llllll_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1llll1llll11_opy_, bstack11l1111_opy_ (u"ࠪࡻࠬ‏")) as file:
        json.dump({
          bstack11l1111_opy_ (u"ࠦࡨࡵ࡭࡮ࡣࡱࡨࡸࠨ‐"): self.commands_to_wrap,
          bstack11l1111_opy_ (u"ࠧࡹࡣࡳ࡫ࡳࡸࡸࠨ‑"): {
            bstack11l1111_opy_ (u"ࠨࡳࡤࡣࡱࠦ‒"): self.perform_scan,
            bstack11l1111_opy_ (u"ࠢࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࠦ–"): self.bstack11llll11l_opy_,
            bstack11l1111_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠧ—"): self.bstack11ll11lll1_opy_,
            bstack11l1111_opy_ (u"ࠤࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠢ―"): self.bstack1llll1llll1l_opy_
          },
          bstack11l1111_opy_ (u"ࠥࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠢ‖"): self.bstack1lllll11111l_opy_
        }, file)
    except Exception as e:
      logger.error(bstack11l1111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡶࡸࡴࡸࡩ࡯ࡩࠣࡧࡴࡳ࡭ࡢࡰࡧࡷ࠿ࠦࡻࡾࠤ‗").format(e))
      pass
  def bstack1ll1l11l1l_opy_(self, command_name):
    try:
      return any(command.get(bstack11l1111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ‘")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack1l1ll1lll1_opy_ = bstack1lllll111111_opy_()