# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import json
from bstack_utils.bstack1ll11111l1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll1l1111_opy_(object):
  bstack1ll1l1l1l1_opy_ = os.path.join(os.path.expanduser(bstack1lllll1_opy_ (u"ࠧࡿࠩᾪ")), bstack1lllll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨᾫ"))
  bstack1lllll1l1ll1_opy_ = os.path.join(bstack1ll1l1l1l1_opy_, bstack1lllll1_opy_ (u"ࠩࡦࡳࡲࡳࡡ࡯ࡦࡶ࠲࡯ࡹ࡯࡯ࠩᾬ"))
  commands_to_wrap = None
  perform_scan = None
  bstack11l111111l_opy_ = None
  bstack1llll11111_opy_ = None
  bstack1lllll1l111l_opy_ = None
  bstack1lllll1l1l1l_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack1lllll1_opy_ (u"ࠪ࡭ࡳࡹࡴࡢࡰࡦࡩࠬᾭ")):
      cls.instance = super(bstack1lllll1l1111_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll1l11l1_opy_()
    return cls.instance
  def bstack1lllll1l11l1_opy_(self):
    try:
      with open(self.bstack1lllll1l1ll1_opy_, bstack1lllll1_opy_ (u"ࠫࡷ࠭ᾮ")) as bstack1ll1ll111_opy_:
        bstack1lllll1l1lll_opy_ = bstack1ll1ll111_opy_.read()
        data = json.loads(bstack1lllll1l1lll_opy_)
        if bstack1lllll1_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧᾯ") in data:
          self.bstack1lllll1l11ll_opy_(data[bstack1lllll1_opy_ (u"࠭ࡣࡰ࡯ࡰࡥࡳࡪࡳࠨᾰ")])
        if bstack1lllll1_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨᾱ") in data:
          self.bstack1111l1111_opy_(data[bstack1lllll1_opy_ (u"ࠨࡵࡦࡶ࡮ࡶࡴࡴࠩᾲ")])
        if bstack1lllll1_opy_ (u"ࠩࡱࡳࡳࡈࡓࡵࡣࡦ࡯ࡎࡴࡦࡳࡣࡄ࠵࠶ࡿࡃࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᾳ") in data:
          self.bstack1lllll1l1l11_opy_(data[bstack1lllll1_opy_ (u"ࠪࡲࡴࡴࡂࡔࡶࡤࡧࡰࡏ࡮ࡧࡴࡤࡅ࠶࠷ࡹࡄࡪࡵࡳࡲ࡫ࡏࡱࡶ࡬ࡳࡳࡹࠧᾴ")])
    except:
      pass
  def bstack1lllll1l1l11_opy_(self, bstack1lllll1l1l1l_opy_):
    if bstack1lllll1l1l1l_opy_ != None:
      self.bstack1lllll1l1l1l_opy_ = bstack1lllll1l1l1l_opy_
  def bstack1111l1111_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack1lllll1_opy_ (u"ࠫࡸࡩࡡ࡯ࠩ᾵"),bstack1lllll1_opy_ (u"ࠬ࠭ᾶ"))
      self.bstack11l111111l_opy_ = scripts.get(bstack1lllll1_opy_ (u"࠭ࡧࡦࡶࡕࡩࡸࡻ࡬ࡵࡵࠪᾷ"),bstack1lllll1_opy_ (u"ࠧࠨᾸ"))
      self.bstack1llll11111_opy_ = scripts.get(bstack1lllll1_opy_ (u"ࠨࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࡘࡻ࡭࡮ࡣࡵࡽࠬᾹ"),bstack1lllll1_opy_ (u"ࠩࠪᾺ"))
      self.bstack1lllll1l111l_opy_ = scripts.get(bstack1lllll1_opy_ (u"ࠪࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠨΆ"),bstack1lllll1_opy_ (u"ࠫࠬᾼ"))
  def bstack1lllll1l11ll_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll1l1ll1_opy_, bstack1lllll1_opy_ (u"ࠬࡽࠧ᾽")) as file:
        json.dump({
          bstack1lllll1_opy_ (u"ࠨࡣࡰ࡯ࡰࡥࡳࡪࡳࠣι"): self.commands_to_wrap,
          bstack1lllll1_opy_ (u"ࠢࡴࡥࡵ࡭ࡵࡺࡳࠣ᾿"): {
            bstack1lllll1_opy_ (u"ࠣࡵࡦࡥࡳࠨ῀"): self.perform_scan,
            bstack1lllll1_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸࠨ῁"): self.bstack11l111111l_opy_,
            bstack1lllll1_opy_ (u"ࠥ࡫ࡪࡺࡒࡦࡵࡸࡰࡹࡹࡓࡶ࡯ࡰࡥࡷࡿࠢῂ"): self.bstack1llll11111_opy_,
            bstack1lllll1_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤῃ"): self.bstack1lllll1l111l_opy_
          },
          bstack1lllll1_opy_ (u"ࠧࡴ࡯࡯ࡄࡖࡸࡦࡩ࡫ࡊࡰࡩࡶࡦࡇ࠱࠲ࡻࡆ࡬ࡷࡵ࡭ࡦࡑࡳࡸ࡮ࡵ࡮ࡴࠤῄ"): self.bstack1lllll1l1l1l_opy_
        }, file)
    except Exception as e:
      logger.error(bstack1lllll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡽࡨࡪ࡮ࡨࠤࡸࡺ࡯ࡳ࡫ࡱ࡫ࠥࡩ࡯࡮࡯ࡤࡲࡩࡹ࠺ࠡࡽࢀࠦ῅").format(e))
      pass
  def bstack1llllll1ll_opy_(self, command_name):
    try:
      return any(command.get(bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬῆ")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack1llll11l11_opy_ = bstack1lllll1l1111_opy_()