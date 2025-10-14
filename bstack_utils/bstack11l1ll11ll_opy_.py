# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import os
import json
from bstack_utils.bstack1ll1111ll_opy_ import get_logger
logger = get_logger(__name__)
class bstack1lllll1l1ll1_opy_(object):
  bstack1l1l1ll1l_opy_ = os.path.join(os.path.expanduser(bstack11l1l11_opy_ (u"࠭ࡾࠨᾢ")), bstack11l1l11_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᾣ"))
  bstack1lllll1l1l11_opy_ = os.path.join(bstack1l1l1ll1l_opy_, bstack11l1l11_opy_ (u"ࠨࡥࡲࡱࡲࡧ࡮ࡥࡵ࠱࡮ࡸࡵ࡮ࠨᾤ"))
  commands_to_wrap = None
  perform_scan = None
  bstack1ll1l1ll11_opy_ = None
  bstack1llllll111_opy_ = None
  bstack1lllll1l111l_opy_ = None
  bstack1lllll1l11ll_opy_ = None
  def __new__(cls):
    if not hasattr(cls, bstack11l1l11_opy_ (u"ࠩ࡬ࡲࡸࡺࡡ࡯ࡥࡨࠫᾥ")):
      cls.instance = super(bstack1lllll1l1ll1_opy_, cls).__new__(cls)
      cls.instance.bstack1lllll1l11l1_opy_()
    return cls.instance
  def bstack1lllll1l11l1_opy_(self):
    try:
      with open(self.bstack1lllll1l1l11_opy_, bstack11l1l11_opy_ (u"ࠪࡶࠬᾦ")) as bstack111lll1l1_opy_:
        bstack1lllll1l1l1l_opy_ = bstack111lll1l1_opy_.read()
        data = json.loads(bstack1lllll1l1l1l_opy_)
        if bstack11l1l11_opy_ (u"ࠫࡨࡵ࡭࡮ࡣࡱࡨࡸ࠭ᾧ") in data:
          self.bstack1lllll1l1111_opy_(data[bstack11l1l11_opy_ (u"ࠬࡩ࡯࡮࡯ࡤࡲࡩࡹࠧᾨ")])
        if bstack11l1l11_opy_ (u"࠭ࡳࡤࡴ࡬ࡴࡹࡹࠧᾩ") in data:
          self.bstack1ll11ll11l_opy_(data[bstack11l1l11_opy_ (u"ࠧࡴࡥࡵ࡭ࡵࡺࡳࠨᾪ")])
        if bstack11l1l11_opy_ (u"ࠨࡰࡲࡲࡇ࡙ࡴࡢࡥ࡮ࡍࡳ࡬ࡲࡢࡃ࠴࠵ࡾࡉࡨࡳࡱࡰࡩࡔࡶࡴࡪࡱࡱࡷࠬᾫ") in data:
          self.bstack1lllll11llll_opy_(data[bstack11l1l11_opy_ (u"ࠩࡱࡳࡳࡈࡓࡵࡣࡦ࡯ࡎࡴࡦࡳࡣࡄ࠵࠶ࡿࡃࡩࡴࡲࡱࡪࡕࡰࡵ࡫ࡲࡲࡸ࠭ᾬ")])
    except:
      pass
  def bstack1lllll11llll_opy_(self, bstack1lllll1l11ll_opy_):
    if bstack1lllll1l11ll_opy_ != None:
      self.bstack1lllll1l11ll_opy_ = bstack1lllll1l11ll_opy_
  def bstack1ll11ll11l_opy_(self, scripts):
    if scripts != None:
      self.perform_scan = scripts.get(bstack11l1l11_opy_ (u"ࠪࡷࡨࡧ࡮ࠨᾭ"),bstack11l1l11_opy_ (u"ࠫࠬᾮ"))
      self.bstack1ll1l1ll11_opy_ = scripts.get(bstack11l1l11_opy_ (u"ࠬ࡭ࡥࡵࡔࡨࡷࡺࡲࡴࡴࠩᾯ"),bstack11l1l11_opy_ (u"࠭ࠧᾰ"))
      self.bstack1llllll111_opy_ = scripts.get(bstack11l1l11_opy_ (u"ࠧࡨࡧࡷࡖࡪࡹࡵ࡭ࡶࡶࡗࡺࡳ࡭ࡢࡴࡼࠫᾱ"),bstack11l1l11_opy_ (u"ࠨࠩᾲ"))
      self.bstack1lllll1l111l_opy_ = scripts.get(bstack11l1l11_opy_ (u"ࠩࡶࡥࡻ࡫ࡒࡦࡵࡸࡰࡹࡹࠧᾳ"),bstack11l1l11_opy_ (u"ࠪࠫᾴ"))
  def bstack1lllll1l1111_opy_(self, commands_to_wrap):
    if commands_to_wrap != None and len(commands_to_wrap) != 0:
      self.commands_to_wrap = commands_to_wrap
  def store(self):
    try:
      with open(self.bstack1lllll1l1l11_opy_, bstack11l1l11_opy_ (u"ࠫࡼ࠭᾵")) as file:
        json.dump({
          bstack11l1l11_opy_ (u"ࠧࡩ࡯࡮࡯ࡤࡲࡩࡹࠢᾶ"): self.commands_to_wrap,
          bstack11l1l11_opy_ (u"ࠨࡳࡤࡴ࡬ࡴࡹࡹࠢᾷ"): {
            bstack11l1l11_opy_ (u"ࠢࡴࡥࡤࡲࠧᾸ"): self.perform_scan,
            bstack11l1l11_opy_ (u"ࠣࡩࡨࡸࡗ࡫ࡳࡶ࡮ࡷࡷࠧᾹ"): self.bstack1ll1l1ll11_opy_,
            bstack11l1l11_opy_ (u"ࠤࡪࡩࡹࡘࡥࡴࡷ࡯ࡸࡸ࡙ࡵ࡮࡯ࡤࡶࡾࠨᾺ"): self.bstack1llllll111_opy_,
            bstack11l1l11_opy_ (u"ࠥࡷࡦࡼࡥࡓࡧࡶࡹࡱࡺࡳࠣΆ"): self.bstack1lllll1l111l_opy_
          },
          bstack11l1l11_opy_ (u"ࠦࡳࡵ࡮ࡃࡕࡷࡥࡨࡱࡉ࡯ࡨࡵࡥࡆ࠷࠱ࡺࡅ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠣᾼ"): self.bstack1lllll1l11ll_opy_
        }, file)
    except Exception as e:
      logger.error(bstack11l1l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡼ࡮ࡩ࡭ࡧࠣࡷࡹࡵࡲࡪࡰࡪࠤࡨࡵ࡭࡮ࡣࡱࡨࡸࡀࠠࡼࡿࠥ᾽").format(e))
      pass
  def bstack1ll11l1l11_opy_(self, command_name):
    try:
      return any(command.get(bstack11l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫι")) == command_name for command in self.commands_to_wrap)
    except:
      return False
bstack11l1ll11ll_opy_ = bstack1lllll1l1ll1_opy_()