# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import os
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack1l1l1l1l1l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1l1111llll_opy_ import bstack1l111l11l_opy_
class bstack11ll111l1l_opy_:
  working_dir = os.getcwd()
  bstack1l1111l1ll_opy_ = False
  config = {}
  bstack111l1l1l1l1_opy_ = bstack1l1lll1_opy_ (u"࠭ࠧἤ")
  binary_path = bstack1l1lll1_opy_ (u"ࠧࠨἥ")
  bstack1lllllll1lll_opy_ = bstack1l1lll1_opy_ (u"ࠨࠩἦ")
  bstack1l11l11l1l_opy_ = False
  bstack1llllll1llll_opy_ = None
  bstack1111111l11l_opy_ = {}
  bstack1llllll1lll1_opy_ = 300
  bstack1lllll1llll1_opy_ = False
  logger = None
  bstack1lllll1lllll_opy_ = False
  bstack1lll11l1ll_opy_ = False
  percy_build_id = None
  bstack1lllll1ll11l_opy_ = bstack1l1lll1_opy_ (u"ࠩࠪἧ")
  bstack1lllll1lll1l_opy_ = {
    bstack1l1lll1_opy_ (u"ࠪࡧ࡭ࡸ࡯࡮ࡧࠪἨ") : 1,
    bstack1l1lll1_opy_ (u"ࠫ࡫࡯ࡲࡦࡨࡲࡼࠬἩ") : 2,
    bstack1l1lll1_opy_ (u"ࠬ࡫ࡤࡨࡧࠪἪ") : 3,
    bstack1l1lll1_opy_ (u"࠭ࡳࡢࡨࡤࡶ࡮࠭Ἣ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1lllllll111l_opy_(self):
    bstack1llllll11l1l_opy_ = bstack1l1lll1_opy_ (u"ࠧࠨἬ")
    bstack1llllll111ll_opy_ = sys.platform
    bstack11111111111_opy_ = bstack1l1lll1_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧἭ")
    if re.match(bstack1l1lll1_opy_ (u"ࠤࡧࡥࡷࡽࡩ࡯ࡾࡰࡥࡨࠦ࡯ࡴࠤἮ"), bstack1llllll111ll_opy_) != None:
      bstack1llllll11l1l_opy_ = bstack11l1l1lll11_opy_ + bstack1l1lll1_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡳࡸࡾ࠮ࡻ࡫ࡳࠦἯ")
      self.bstack1lllll1ll11l_opy_ = bstack1l1lll1_opy_ (u"ࠫࡲࡧࡣࠨἰ")
    elif re.match(bstack1l1lll1_opy_ (u"ࠧࡳࡳࡸ࡫ࡱࢀࡲࡹࡹࡴࡾࡰ࡭ࡳ࡭ࡷࡽࡥࡼ࡫ࡼ࡯࡮ࡽࡤࡦࡧࡼ࡯࡮ࡽࡹ࡬ࡲࡨ࡫ࡼࡦ࡯ࡦࢀࡼ࡯࡮࠴࠴ࠥἱ"), bstack1llllll111ll_opy_) != None:
      bstack1llllll11l1l_opy_ = bstack11l1l1lll11_opy_ + bstack1l1lll1_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳ࡷࡪࡰ࠱ࡾ࡮ࡶࠢἲ")
      bstack11111111111_opy_ = bstack1l1lll1_opy_ (u"ࠢࡱࡧࡵࡧࡾ࠴ࡥࡹࡧࠥἳ")
      self.bstack1lllll1ll11l_opy_ = bstack1l1lll1_opy_ (u"ࠨࡹ࡬ࡲࠬἴ")
    else:
      bstack1llllll11l1l_opy_ = bstack11l1l1lll11_opy_ + bstack1l1lll1_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯࡯࡭ࡳࡻࡸ࠯ࡼ࡬ࡴࠧἵ")
      self.bstack1lllll1ll11l_opy_ = bstack1l1lll1_opy_ (u"ࠪࡰ࡮ࡴࡵࡹࠩἶ")
    return bstack1llllll11l1l_opy_, bstack11111111111_opy_
  def bstack111111l1111_opy_(self):
    try:
      bstack1llllll1l1ll_opy_ = [os.path.join(expanduser(bstack1l1lll1_opy_ (u"ࠦࢃࠨἷ")), bstack1l1lll1_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬἸ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1llllll1l1ll_opy_:
        if(self.bstack1111111lll1_opy_(path)):
          return path
      raise bstack1l1lll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠥἹ")
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪ࡮ࡴࡤࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨࠤࡵࡧࡴࡩࠢࡩࡳࡷࠦࡰࡦࡴࡦࡽࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࠲ࠦࡻࡾࠤἺ").format(e))
  def bstack1111111lll1_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1llllll1l11l_opy_(self, bstack1llllll1l1l1_opy_):
    return os.path.join(bstack1llllll1l1l1_opy_, self.bstack111l1l1l1l1_opy_ + bstack1l1lll1_opy_ (u"ࠣ࠰ࡨࡸࡦ࡭ࠢἻ"))
  def bstack1lllllllllll_opy_(self, bstack1llllll1l1l1_opy_, bstack1lllllll1111_opy_):
    if not bstack1lllllll1111_opy_: return
    try:
      bstack1lllll1l1ll1_opy_ = self.bstack1llllll1l11l_opy_(bstack1llllll1l1l1_opy_)
      with open(bstack1lllll1l1ll1_opy_, bstack1l1lll1_opy_ (u"ࠤࡺࠦἼ")) as f:
        f.write(bstack1lllllll1111_opy_)
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡗࡦࡼࡥࡥࠢࡱࡩࡼࠦࡅࡕࡣࡪࠤ࡫ࡵࡲࠡࡲࡨࡶࡨࡿࠢἽ"))
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡣࡹࡩࠥࡺࡨࡦࠢࡨࡸࡦ࡭ࠬࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦἾ").format(e))
  def bstack1llllll11ll1_opy_(self, bstack1llllll1l1l1_opy_):
    try:
      bstack1lllll1l1ll1_opy_ = self.bstack1llllll1l11l_opy_(bstack1llllll1l1l1_opy_)
      if os.path.exists(bstack1lllll1l1ll1_opy_):
        with open(bstack1lllll1l1ll1_opy_, bstack1l1lll1_opy_ (u"ࠧࡸࠢἿ")) as f:
          bstack1lllllll1111_opy_ = f.read().strip()
          return bstack1lllllll1111_opy_ if bstack1lllllll1111_opy_ else None
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡆࡖࡤ࡫࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤὀ").format(e))
  def bstack11111111l11_opy_(self, bstack1llllll1l1l1_opy_, bstack1llllll11l1l_opy_):
    bstack1lllllll1l11_opy_ = self.bstack1llllll11ll1_opy_(bstack1llllll1l1l1_opy_)
    if bstack1lllllll1l11_opy_:
      try:
        bstack1llllllll1ll_opy_ = self.bstack1lllll1l1l1l_opy_(bstack1lllllll1l11_opy_, bstack1llllll11l1l_opy_)
        if not bstack1llllllll1ll_opy_:
          self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡩࡴࠢࡸࡴࠥࡺ࡯ࠡࡦࡤࡸࡪࠦࠨࡆࡖࡤ࡫ࠥࡻ࡮ࡤࡪࡤࡲ࡬࡫ࡤࠪࠤὁ"))
          return True
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠣࡐࡨࡻࠥࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥ࠭ࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡶࡲࡧࡥࡹ࡫ࠢὂ"))
        return False
      except Exception as e:
        self.logger.warn(bstack1l1lll1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩࡨࡦࡥ࡮ࠤ࡫ࡵࡲࠡࡤ࡬ࡲࡦࡸࡹࠡࡷࡳࡨࡦࡺࡥࡴ࠮ࠣࡹࡸ࡯࡮ࡨࠢࡨࡼ࡮ࡹࡴࡪࡰࡪࠤࡧ࡯࡮ࡢࡴࡼ࠾ࠥࢁࡽࠣὃ").format(e))
    return False
  def bstack1lllll1l1l1l_opy_(self, bstack1lllllll1l11_opy_, bstack1llllll11l1l_opy_):
    try:
      headers = {
        bstack1l1lll1_opy_ (u"ࠥࡍ࡫࠳ࡎࡰࡰࡨ࠱ࡒࡧࡴࡤࡪࠥὄ"): bstack1lllllll1l11_opy_
      }
      response = bstack1l1l1l1l1l_opy_(bstack1l1lll1_opy_ (u"ࠫࡌࡋࡔࠨὅ"), bstack1llllll11l1l_opy_, {}, {bstack1l1lll1_opy_ (u"ࠧ࡮ࡥࡢࡦࡨࡶࡸࠨ὆"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack1l1lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡩࡨࡦࡥ࡮࡭ࡳ࡭ࠠࡧࡱࡵࠤࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡹࡵࡪࡡࡵࡧࡶ࠾ࠥࢁࡽࠣ὇").format(e))
  @measure(event_name=EVENTS.bstack11l1l111lll_opy_, stage=STAGE.bstack1111llll1l_opy_)
  def bstack1lllllll1ll1_opy_(self, bstack1llllll11l1l_opy_, bstack11111111111_opy_):
    try:
      bstack1lllllllll11_opy_ = self.bstack111111l1111_opy_()
      bstack1lllllll11l1_opy_ = os.path.join(bstack1lllllllll11_opy_, bstack1l1lll1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠴ࡺࡪࡲࠪὈ"))
      bstack1llllll11l11_opy_ = os.path.join(bstack1lllllllll11_opy_, bstack11111111111_opy_)
      if self.bstack11111111l11_opy_(bstack1lllllllll11_opy_, bstack1llllll11l1l_opy_): # if bstack11111111lll_opy_, bstack1lllll11l11_opy_ bstack1lllllll1111_opy_ is bstack1llllllll1l1_opy_ to bstack111l1l1l1ll_opy_ version available (response 304)
        if os.path.exists(bstack1llllll11l11_opy_):
          self.logger.info(bstack1l1lll1_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡳ࡬࡫ࡳࡴ࡮ࡴࡧࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠥὉ").format(bstack1llllll11l11_opy_))
          return bstack1llllll11l11_opy_
        if os.path.exists(bstack1lllllll11l1_opy_):
          self.logger.info(bstack1l1lll1_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡼ࡬ࡴࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡼࡿ࠯ࠤࡺࡴࡺࡪࡲࡳ࡭ࡳ࡭ࠢὊ").format(bstack1lllllll11l1_opy_))
          return self.bstack111111l11l1_opy_(bstack1lllllll11l1_opy_, bstack11111111111_opy_)
      self.logger.info(bstack1l1lll1_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨ࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡧࡴࡲࡱࠥࢁࡽࠣὋ").format(bstack1llllll11l1l_opy_))
      response = bstack1l1l1l1l1l_opy_(bstack1l1lll1_opy_ (u"ࠫࡌࡋࡔࠨὌ"), bstack1llllll11l1l_opy_, {}, {})
      if response.status_code == 200:
        bstack1lllll1ll1ll_opy_ = response.headers.get(bstack1l1lll1_opy_ (u"ࠧࡋࡔࡢࡩࠥὍ"), bstack1l1lll1_opy_ (u"ࠨࠢ὎"))
        if bstack1lllll1ll1ll_opy_:
          self.bstack1lllllllllll_opy_(bstack1lllllllll11_opy_, bstack1lllll1ll1ll_opy_)
        with open(bstack1lllllll11l1_opy_, bstack1l1lll1_opy_ (u"ࠧࡸࡤࠪ὏")) as file:
          file.write(response.content)
        self.logger.info(bstack1l1lll1_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦࡨࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡦࡴࡤࠡࡵࡤࡺࡪࡪࠠࡢࡶࠣࡿࢂࠨὐ").format(bstack1lllllll11l1_opy_))
        return self.bstack111111l11l1_opy_(bstack1lllllll11l1_opy_, bstack11111111111_opy_)
      else:
        raise(bstack1l1lll1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡵࡪࡨࠤ࡫࡯࡬ࡦ࠰ࠣࡗࡹࡧࡴࡶࡵࠣࡧࡴࡪࡥ࠻ࠢࡾࢁࠧὑ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿ࠺ࠡࡽࢀࠦὒ").format(e))
  def bstack1111111l1ll_opy_(self, bstack1llllll11l1l_opy_, bstack11111111111_opy_):
    try:
      retry = 2
      bstack1llllll11l11_opy_ = None
      bstack1llllll1ll11_opy_ = False
      while retry > 0:
        bstack1llllll11l11_opy_ = self.bstack1lllllll1ll1_opy_(bstack1llllll11l1l_opy_, bstack11111111111_opy_)
        bstack1llllll1ll11_opy_ = self.bstack1llllll1l111_opy_(bstack1llllll11l1l_opy_, bstack11111111111_opy_, bstack1llllll11l11_opy_)
        if bstack1llllll1ll11_opy_:
          break
        retry -= 1
      return bstack1llllll11l11_opy_, bstack1llllll1ll11_opy_
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡴࡦࡺࡨࠣὓ").format(e))
    return bstack1llllll11l11_opy_, False
  def bstack1llllll1l111_opy_(self, bstack1llllll11l1l_opy_, bstack11111111111_opy_, bstack1llllll11l11_opy_, bstack1lllll1lll11_opy_ = 0):
    if bstack1lllll1lll11_opy_ > 1:
      return False
    if bstack1llllll11l11_opy_ == None or os.path.exists(bstack1llllll11l11_opy_) == False:
      self.logger.warn(bstack1l1lll1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠱ࠦࡲࡦࡶࡵࡽ࡮ࡴࡧࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠥὔ"))
      return False
    bstack111111l1l1l_opy_ = bstack1l1lll1_opy_ (u"ࡸࠢ࡟࠰࠭ࡄࡵ࡫ࡲࡤࡻ࠲ࡧࡱ࡯ࠠ࡝ࡦ࠮ࡠ࠳ࡢࡤࠬ࡞࠱ࡠࡩ࠱ࠢὕ")
    command = bstack1l1lll1_opy_ (u"ࠧࡼࡿࠣ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ࠭ὖ").format(bstack1llllll11l11_opy_)
    bstack111111111l1_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack111111l1l1l_opy_, bstack111111111l1_opy_) != None:
      return True
    else:
      self.logger.error(bstack1l1lll1_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡥ࡫ࡩࡨࡱࠠࡧࡣ࡬ࡰࡪࡪࠢὗ"))
      return False
  def bstack111111l11l1_opy_(self, bstack1lllllll11l1_opy_, bstack11111111111_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllllll11l1_opy_)
      shutil.unpack_archive(bstack1lllllll11l1_opy_, working_dir)
      bstack1llllll11l11_opy_ = os.path.join(working_dir, bstack11111111111_opy_)
      os.chmod(bstack1llllll11l11_opy_, 0o755)
      return bstack1llllll11l11_opy_
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡻ࡮ࡻ࡫ࡳࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠥ὘"))
  def bstack1111111ll11_opy_(self):
    try:
      bstack1111111llll_opy_ = self.config.get(bstack1l1lll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩὙ"))
      bstack1111111ll11_opy_ = bstack1111111llll_opy_ or (bstack1111111llll_opy_ is None and self.bstack1l1111l1ll_opy_)
      if not bstack1111111ll11_opy_ or self.config.get(bstack1l1lll1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ὚"), None) not in bstack11l1l11111l_opy_:
        return False
      self.bstack1l11l11l1l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡩࡴࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢὛ").format(e))
  def bstack11111111ll1_opy_(self):
    try:
      bstack11111111ll1_opy_ = self.percy_capture_mode
      return bstack11111111ll1_opy_
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡣࡵࠢࡳࡩࡷࡩࡹࠡࡥࡤࡴࡹࡻࡲࡦࠢࡰࡳࡩ࡫ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢ὜").format(e))
  def init(self, bstack1l1111l1ll_opy_, config, logger):
    self.bstack1l1111l1ll_opy_ = bstack1l1111l1ll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1111111ll11_opy_():
      return
    self.bstack1111111l11l_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠧࡱࡧࡵࡧࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭Ὕ"), {})
    self.percy_capture_mode = config.get(bstack1l1lll1_opy_ (u"ࠨࡲࡨࡶࡨࡿࡃࡢࡲࡷࡹࡷ࡫ࡍࡰࡦࡨࠫ὞"))
    try:
      bstack1llllll11l1l_opy_, bstack11111111111_opy_ = self.bstack1lllllll111l_opy_()
      self.bstack111l1l1l1l1_opy_ = bstack11111111111_opy_
      bstack1llllll11l11_opy_, bstack1llllll1ll11_opy_ = self.bstack1111111l1ll_opy_(bstack1llllll11l1l_opy_, bstack11111111111_opy_)
      if bstack1llllll1ll11_opy_:
        self.binary_path = bstack1llllll11l11_opy_
        thread = Thread(target=self.bstack1llllll1111l_opy_)
        thread.start()
      else:
        self.bstack1lllll1lllll_opy_ = True
        self.logger.error(bstack1l1lll1_opy_ (u"ࠤࡌࡲࡻࡧ࡬ࡪࡦࠣࡴࡪࡸࡣࡺࠢࡳࡥࡹ࡮ࠠࡧࡱࡸࡲࡩࠦ࠭ࠡࡽࢀ࠰࡛ࠥ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡑࡧࡵࡧࡾࠨὟ").format(bstack1llllll11l11_opy_))
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦὠ").format(e))
  def bstack1llllll11111_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1l1lll1_opy_ (u"ࠫࡱࡵࡧࠨὡ"), bstack1l1lll1_opy_ (u"ࠬࡶࡥࡳࡥࡼ࠲ࡱࡵࡧࠨὢ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1l1lll1_opy_ (u"ࠨࡐࡶࡵ࡫࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦ࡬ࡰࡩࡶࠤࡦࡺࠠࡼࡿࠥὣ").format(logfile))
      self.bstack1lllllll1lll_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡪࡺࠠࡱࡧࡵࡧࡾࠦ࡬ࡰࡩࠣࡴࡦࡺࡨ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣὤ").format(e))
  @measure(event_name=EVENTS.bstack11l11ll1l11_opy_, stage=STAGE.bstack1111llll1l_opy_)
  def bstack1llllll1111l_opy_(self):
    bstack111111l11ll_opy_ = self.bstack1111111l111_opy_()
    if bstack111111l11ll_opy_ == None:
      self.bstack1lllll1lllll_opy_ = True
      self.logger.error(bstack1l1lll1_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡵࡱ࡮ࡩࡳࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠮ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼࠦὥ"))
      return False
    bstack111111l1l11_opy_ = [bstack1l1lll1_opy_ (u"ࠤࡤࡴࡵࡀࡥࡹࡧࡦ࠾ࡸࡺࡡࡳࡶࠥὦ") if self.bstack1l1111l1ll_opy_ else bstack1l1lll1_opy_ (u"ࠪࡩࡽ࡫ࡣ࠻ࡵࡷࡥࡷࡺࠧὧ")]
    bstack11111ll1l1l_opy_ = self.bstack1lllllll11ll_opy_()
    if bstack11111ll1l1l_opy_ != None:
      bstack111111l1l11_opy_.append(bstack1l1lll1_opy_ (u"ࠦ࠲ࡩࠠࡼࡿࠥὨ").format(bstack11111ll1l1l_opy_))
    env = os.environ.copy()
    env[bstack1l1lll1_opy_ (u"ࠧࡖࡅࡓࡅ࡜ࡣ࡙ࡕࡋࡆࡐࠥὩ")] = bstack111111l11ll_opy_
    env[bstack1l1lll1_opy_ (u"ࠨࡔࡉࡡࡅ࡙ࡎࡒࡄࡠࡗࡘࡍࡉࠨὪ")] = os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬὫ"), bstack1l1lll1_opy_ (u"ࠨࠩὬ"))
    bstack1llllll11lll_opy_ = [self.binary_path]
    self.bstack1llllll11111_opy_()
    self.bstack1llllll1llll_opy_ = self.bstack1111111ll1l_opy_(bstack1llllll11lll_opy_ + bstack111111l1l11_opy_, env)
    self.logger.debug(bstack1l1lll1_opy_ (u"ࠤࡖࡸࡦࡸࡴࡪࡰࡪࠤࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠥὭ"))
    bstack1lllll1lll11_opy_ = 0
    while self.bstack1llllll1llll_opy_.poll() == None:
      bstack1lllllllll1l_opy_ = self.bstack111111111ll_opy_()
      if bstack1lllllllll1l_opy_:
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡶࡹࡨࡩࡥࡴࡵࡩࡹࡱࠨὮ"))
        self.bstack1lllll1llll1_opy_ = True
        return True
      bstack1lllll1lll11_opy_ += 1
      self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡖࡪࡺࡲࡺࠢ࠰ࠤࢀࢃࠢὯ").format(bstack1lllll1lll11_opy_))
      time.sleep(2)
    self.logger.error(bstack1l1lll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡆࡢ࡫࡯ࡩࡩࠦࡡࡧࡶࡨࡶࠥࢁࡽࠡࡣࡷࡸࡪࡳࡰࡵࡵࠥὰ").format(bstack1lllll1lll11_opy_))
    self.bstack1lllll1lllll_opy_ = True
    return False
  def bstack111111111ll_opy_(self, bstack1lllll1lll11_opy_ = 0):
    if bstack1lllll1lll11_opy_ > 10:
      return False
    try:
      bstack1llllllll11l_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"࠭ࡐࡆࡔࡆ࡝ࡤ࡙ࡅࡓࡘࡈࡖࡤࡇࡄࡅࡔࡈࡗࡘ࠭ά"), bstack1l1lll1_opy_ (u"ࠧࡩࡶࡷࡴ࠿࠵࠯࡭ࡱࡦࡥࡱ࡮࡯ࡴࡶ࠽࠹࠸࠹࠸ࠨὲ"))
      bstack1lllll1ll111_opy_ = bstack1llllllll11l_opy_ + bstack11l11llllll_opy_
      response = requests.get(bstack1lllll1ll111_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1l1lll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࠧέ"), {}).get(bstack1l1lll1_opy_ (u"ࠩ࡬ࡨࠬὴ"), None)
      return True
    except:
      self.logger.debug(bstack1l1lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡲࡧࡨࡻࡲࡳࡧࡧࠤࡼ࡮ࡩ࡭ࡧࠣࡴࡷࡵࡣࡦࡵࡶ࡭ࡳ࡭ࠠࡩࡧࡤࡰࡹ࡮ࠠࡤࡪࡨࡧࡰࠦࡲࡦࡵࡳࡳࡳࡹࡥࠣή"))
      return False
  def bstack1111111l111_opy_(self):
    bstack1111111111l_opy_ = bstack1l1lll1_opy_ (u"ࠫࡦࡶࡰࠨὶ") if self.bstack1l1111l1ll_opy_ else bstack1l1lll1_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧί")
    bstack1111111l1l1_opy_ = bstack1l1lll1_opy_ (u"ࠨࡵ࡯ࡦࡨࡪ࡮ࡴࡥࡥࠤὸ") if self.config.get(bstack1l1lll1_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ό")) is None else True
    bstack11ll11l1l11_opy_ = bstack1l1lll1_opy_ (u"ࠣࡣࡳ࡭࠴ࡧࡰࡱࡡࡳࡩࡷࡩࡹ࠰ࡩࡨࡸࡤࡶࡲࡰ࡬ࡨࡧࡹࡥࡴࡰ࡭ࡨࡲࡄࡴࡡ࡮ࡧࡀࡿࢂࠬࡴࡺࡲࡨࡁࢀࢃࠦࡱࡧࡵࡧࡾࡃࡻࡾࠤὺ").format(self.config[bstack1l1lll1_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧύ")], bstack1111111111l_opy_, bstack1111111l1l1_opy_)
    if self.percy_capture_mode:
      bstack11ll11l1l11_opy_ += bstack1l1lll1_opy_ (u"ࠥࠪࡵ࡫ࡲࡤࡻࡢࡧࡦࡶࡴࡶࡴࡨࡣࡲࡵࡤࡦ࠿ࡾࢁࠧὼ").format(self.percy_capture_mode)
    uri = bstack1l111l11l_opy_(bstack11ll11l1l11_opy_)
    try:
      response = bstack1l1l1l1l1l_opy_(bstack1l1lll1_opy_ (u"ࠫࡌࡋࡔࠨώ"), uri, {}, {bstack1l1lll1_opy_ (u"ࠬࡧࡵࡵࡪࠪ὾"): (self.config[bstack1l1lll1_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨ὿")], self.config[bstack1l1lll1_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪᾀ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1l11l11l1l_opy_ = data.get(bstack1l1lll1_opy_ (u"ࠨࡵࡸࡧࡨ࡫ࡳࡴࠩᾁ"))
        self.percy_capture_mode = data.get(bstack1l1lll1_opy_ (u"ࠩࡳࡩࡷࡩࡹࡠࡥࡤࡴࡹࡻࡲࡦࡡࡰࡳࡩ࡫ࠧᾂ"))
        os.environ[bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࠨᾃ")] = str(self.bstack1l11l11l1l_opy_)
        os.environ[bstack1l1lll1_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࡡࡆࡅࡕ࡚ࡕࡓࡇࡢࡑࡔࡊࡅࠨᾄ")] = str(self.percy_capture_mode)
        if bstack1111111l1l1_opy_ == bstack1l1lll1_opy_ (u"ࠧࡻ࡮ࡥࡧࡩ࡭ࡳ࡫ࡤࠣᾅ") and str(self.bstack1l11l11l1l_opy_).lower() == bstack1l1lll1_opy_ (u"ࠨࡴࡳࡷࡨࠦᾆ"):
          self.bstack1lll11l1ll_opy_ = True
        if bstack1l1lll1_opy_ (u"ࠢࡵࡱ࡮ࡩࡳࠨᾇ") in data:
          return data[bstack1l1lll1_opy_ (u"ࠣࡶࡲ࡯ࡪࡴࠢᾈ")]
        else:
          raise bstack1l1lll1_opy_ (u"ࠩࡗࡳࡰ࡫࡮ࠡࡐࡲࡸࠥࡌ࡯ࡶࡰࡧࠤ࠲ࠦࡻࡾࠩᾉ").format(data)
      else:
        raise bstack1l1lll1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡶࡥࡳࡥࡼࠤࡹࡵ࡫ࡦࡰ࠯ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡳࡵࡣࡷࡹࡸࠦ࠭ࠡࡽࢀ࠰ࠥࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡃࡱࡧࡽࠥ࠳ࠠࡼࡿࠥᾊ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡧࡷ࡫ࡡࡵ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡵࡸ࡯࡫ࡧࡦࡸࠧᾋ").format(e))
  def bstack1lllllll11ll_opy_(self):
    bstack111111l111l_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠧࡶࡥࡳࡥࡼࡇࡴࡴࡦࡪࡩ࠱࡮ࡸࡵ࡮ࠣᾌ"))
    try:
      if bstack1l1lll1_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧᾍ") not in self.bstack1111111l11l_opy_:
        self.bstack1111111l11l_opy_[bstack1l1lll1_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨᾎ")] = 2
      with open(bstack111111l111l_opy_, bstack1l1lll1_opy_ (u"ࠨࡹࠪᾏ")) as fp:
        json.dump(self.bstack1111111l11l_opy_, fp)
      return bstack111111l111l_opy_
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡩࡲࡦࡣࡷࡩࠥࡶࡥࡳࡥࡼࠤࡨࡵ࡮ࡧ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾐ").format(e))
  def bstack1111111ll1l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lllll1ll11l_opy_ == bstack1l1lll1_opy_ (u"ࠪࡻ࡮ࡴࠧᾑ"):
        bstack1llllll111l1_opy_ = [bstack1l1lll1_opy_ (u"ࠫࡨࡳࡤ࠯ࡧࡻࡩࠬᾒ"), bstack1l1lll1_opy_ (u"ࠬ࠵ࡣࠨᾓ")]
        cmd = bstack1llllll111l1_opy_ + cmd
      cmd = bstack1l1lll1_opy_ (u"࠭ࠠࠨᾔ").join(cmd)
      self.logger.debug(bstack1l1lll1_opy_ (u"ࠢࡓࡷࡱࡲ࡮ࡴࡧࠡࡽࢀࠦᾕ").format(cmd))
      with open(self.bstack1lllllll1lll_opy_, bstack1l1lll1_opy_ (u"ࠣࡣࠥᾖ")) as bstack1llllll1ll1l_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1llllll1ll1l_opy_, text=True, stderr=bstack1llllll1ll1l_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lllll1lllll_opy_ = True
      self.logger.error(bstack1l1lll1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻࠣࡻ࡮ࡺࡨࠡࡥࡰࡨࠥ࠳ࠠࡼࡿ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦᾗ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1lllll1llll1_opy_:
        self.logger.info(bstack1l1lll1_opy_ (u"ࠥࡗࡹࡵࡰࡱ࡫ࡱ࡫ࠥࡖࡥࡳࡥࡼࠦᾘ"))
        cmd = [self.binary_path, bstack1l1lll1_opy_ (u"ࠦࡪࡾࡥࡤ࠼ࡶࡸࡴࡶࠢᾙ")]
        self.bstack1111111ll1l_opy_(cmd)
        self.bstack1lllll1llll1_opy_ = False
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡳࡵࠦࡳࡦࡵࡶ࡭ࡴࡴࠠࡸ࡫ࡷ࡬ࠥࡩ࡯࡮࡯ࡤࡲࡩࠦ࠭ࠡࡽࢀ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮࠻ࠢࡾࢁࠧᾚ").format(cmd, e))
  def bstack1l1llll11l_opy_(self):
    if not self.bstack1l11l11l1l_opy_:
      return
    try:
      bstack1lllll1ll1l1_opy_ = 0
      while not self.bstack1lllll1llll1_opy_ and bstack1lllll1ll1l1_opy_ < self.bstack1llllll1lll1_opy_:
        if self.bstack1lllll1lllll_opy_:
          self.logger.info(bstack1l1lll1_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡹࡥࡵࡷࡳࠤ࡫ࡧࡩ࡭ࡧࡧࠦᾛ"))
          return
        time.sleep(1)
        bstack1lllll1ll1l1_opy_ += 1
      os.environ[bstack1l1lll1_opy_ (u"ࠧࡑࡇࡕࡇ࡞ࡥࡂࡆࡕࡗࡣࡕࡒࡁࡕࡈࡒࡖࡒ࠭ᾜ")] = str(self.bstack1llllllllll1_opy_())
      self.logger.info(bstack1l1lll1_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡴࡧࡷࡹࡵࠦࡣࡰ࡯ࡳࡰࡪࡺࡥࡥࠤᾝ"))
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡥࡵࡷࡳࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᾞ").format(e))
  def bstack1llllllllll1_opy_(self):
    if self.bstack1l1111l1ll_opy_:
      return
    try:
      bstack1lllll1l1lll_opy_ = [platform[bstack1l1lll1_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠨᾟ")].lower() for platform in self.config.get(bstack1l1lll1_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᾠ"), [])]
      bstack11111111l1l_opy_ = sys.maxsize
      bstack111111l1lll_opy_ = bstack1l1lll1_opy_ (u"ࠬ࠭ᾡ")
      for browser in bstack1lllll1l1lll_opy_:
        if browser in self.bstack1lllll1lll1l_opy_:
          bstack1llllllll111_opy_ = self.bstack1lllll1lll1l_opy_[browser]
        if bstack1llllllll111_opy_ < bstack11111111l1l_opy_:
          bstack11111111l1l_opy_ = bstack1llllllll111_opy_
          bstack111111l1lll_opy_ = browser
      return bstack111111l1lll_opy_
    except Exception as e:
      self.logger.error(bstack1l1lll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡣࡧࡶࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᾢ").format(e))
  @classmethod
  def bstack111ll11l11_opy_(self):
    return os.getenv(bstack1l1lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࠬᾣ"), bstack1l1lll1_opy_ (u"ࠨࡈࡤࡰࡸ࡫ࠧᾤ")).lower()
  @classmethod
  def bstack11l1ll11l1_opy_(self):
    return os.getenv(bstack1l1lll1_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟࡟ࡄࡃࡓࡘ࡚ࡘࡅࡠࡏࡒࡈࡊ࠭ᾥ"), bstack1l1lll1_opy_ (u"ࠪࠫᾦ"))
  @classmethod
  def bstack11lllll1ll1_opy_(cls, value):
    cls.bstack1lll11l1ll_opy_ = value
  @classmethod
  def bstack1lllllll1l1l_opy_(cls):
    return cls.bstack1lll11l1ll_opy_
  @classmethod
  def bstack11lllllllll_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack111111l1ll1_opy_(cls):
    return cls.percy_build_id