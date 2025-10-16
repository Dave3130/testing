# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
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
from bstack_utils.helper import bstack1ll1llll11_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11llll111l_opy_ import bstack11lllll11_opy_
class bstack1l1lll11ll_opy_:
  working_dir = os.getcwd()
  bstack111lll1lll_opy_ = False
  config = {}
  bstack1111l1l11l1_opy_ = bstack1l_opy_ (u"ࠫࠬἩ")
  binary_path = bstack1l_opy_ (u"ࠬ࠭Ἢ")
  bstack1llllll11111_opy_ = bstack1l_opy_ (u"࠭ࠧἫ")
  bstack1ll1ll1ll_opy_ = False
  bstack11111111111_opy_ = None
  bstack1llllll111l1_opy_ = {}
  bstack1llllll1l111_opy_ = 300
  bstack1llllll111ll_opy_ = False
  logger = None
  bstack1111111lll1_opy_ = False
  bstack11l11l11ll_opy_ = False
  percy_build_id = None
  bstack1lllllll11l1_opy_ = bstack1l_opy_ (u"ࠧࠨἬ")
  bstack1lllll1ll111_opy_ = {
    bstack1l_opy_ (u"ࠨࡥ࡫ࡶࡴࡳࡥࠨἭ") : 1,
    bstack1l_opy_ (u"ࠩࡩ࡭ࡷ࡫ࡦࡰࡺࠪἮ") : 2,
    bstack1l_opy_ (u"ࠪࡩࡩ࡭ࡥࠨἯ") : 3,
    bstack1l_opy_ (u"ࠫࡸࡧࡦࡢࡴ࡬ࠫἰ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1llllllll1l1_opy_(self):
    bstack111111ll111_opy_ = bstack1l_opy_ (u"ࠬ࠭ἱ")
    bstack1111111ll11_opy_ = sys.platform
    bstack11111111l11_opy_ = bstack1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬἲ")
    if re.match(bstack1l_opy_ (u"ࠢࡥࡣࡵࡻ࡮ࡴࡼ࡮ࡣࡦࠤࡴࡹࠢἳ"), bstack1111111ll11_opy_) != None:
      bstack111111ll111_opy_ = bstack11l1l11111l_opy_ + bstack1l_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮ࡱࡶࡼ࠳ࢀࡩࡱࠤἴ")
      self.bstack1lllllll11l1_opy_ = bstack1l_opy_ (u"ࠩࡰࡥࡨ࠭ἵ")
    elif re.match(bstack1l_opy_ (u"ࠥࡱࡸࡽࡩ࡯ࡾࡰࡷࡾࡹࡼ࡮࡫ࡱ࡫ࡼࢂࡣࡺࡩࡺ࡭ࡳࢂࡢࡤࡥࡺ࡭ࡳࢂࡷࡪࡰࡦࡩࢁ࡫࡭ࡤࡾࡺ࡭ࡳ࠹࠲ࠣἶ"), bstack1111111ll11_opy_) != None:
      bstack111111ll111_opy_ = bstack11l1l11111l_opy_ + bstack1l_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡼ࡯࡮࠯ࡼ࡬ࡴࠧἷ")
      bstack11111111l11_opy_ = bstack1l_opy_ (u"ࠧࡶࡥࡳࡥࡼ࠲ࡪࡾࡥࠣἸ")
      self.bstack1lllllll11l1_opy_ = bstack1l_opy_ (u"࠭ࡷࡪࡰࠪἹ")
    else:
      bstack111111ll111_opy_ = bstack11l1l11111l_opy_ + bstack1l_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭࡭࡫ࡱࡹࡽ࠴ࡺࡪࡲࠥἺ")
      self.bstack1lllllll11l1_opy_ = bstack1l_opy_ (u"ࠨ࡮࡬ࡲࡺࡾࠧἻ")
    return bstack111111ll111_opy_, bstack11111111l11_opy_
  def bstack1lllll1llll1_opy_(self):
    try:
      bstack11111111ll1_opy_ = [os.path.join(expanduser(bstack1l_opy_ (u"ࠤࢁࠦἼ")), bstack1l_opy_ (u"ࠪ࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠪἽ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack11111111ll1_opy_:
        if(self.bstack1lllll1ll1l1_opy_(path)):
          return path
      raise bstack1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡱࡺࡲࡱࡵࡡࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠣἾ")
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡳࡥࡹ࡮ࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡻࠣࡨࡴࡽ࡮࡭ࡱࡤࡨ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࠰ࠤࢀࢃࠢἿ").format(e))
  def bstack1lllll1ll1l1_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack111111l1lll_opy_(self, bstack1llllll1l11l_opy_):
    return os.path.join(bstack1llllll1l11l_opy_, self.bstack1111l1l11l1_opy_ + bstack1l_opy_ (u"ࠨ࠮ࡦࡶࡤ࡫ࠧὀ"))
  def bstack1llllll1l1l1_opy_(self, bstack1llllll1l11l_opy_, bstack111111l1ll1_opy_):
    if not bstack111111l1ll1_opy_: return
    try:
      bstack1lllllllll11_opy_ = self.bstack111111l1lll_opy_(bstack1llllll1l11l_opy_)
      with open(bstack1lllllllll11_opy_, bstack1l_opy_ (u"ࠢࡸࠤὁ")) as f:
        f.write(bstack111111l1ll1_opy_)
        self.logger.debug(bstack1l_opy_ (u"ࠣࡕࡤࡺࡪࡪࠠ࡯ࡧࡺࠤࡊ࡚ࡡࡨࠢࡩࡳࡷࠦࡰࡦࡴࡦࡽࠧὂ"))
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡡࡷࡧࠣࡸ࡭࡫ࠠࡦࡶࡤ࡫࠱ࠦࡥࡳࡴࡲࡶ࠿ࠦࡻࡾࠤὃ").format(e))
  def bstack1111111llll_opy_(self, bstack1llllll1l11l_opy_):
    try:
      bstack1lllllllll11_opy_ = self.bstack111111l1lll_opy_(bstack1llllll1l11l_opy_)
      if os.path.exists(bstack1lllllllll11_opy_):
        with open(bstack1lllllllll11_opy_, bstack1l_opy_ (u"ࠥࡶࠧὄ")) as f:
          bstack111111l1ll1_opy_ = f.read().strip()
          return bstack111111l1ll1_opy_ if bstack111111l1ll1_opy_ else None
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡋࡔࡢࡩ࠯ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢὅ").format(e))
  def bstack1lllllll1lll_opy_(self, bstack1llllll1l11l_opy_, bstack111111ll111_opy_):
    bstack111111l1l1l_opy_ = self.bstack1111111llll_opy_(bstack1llllll1l11l_opy_)
    if bstack111111l1l1l_opy_:
      try:
        bstack111111l111l_opy_ = self.bstack111111ll11l_opy_(bstack111111l1l1l_opy_, bstack111111ll111_opy_)
        if not bstack111111l111l_opy_:
          self.logger.debug(bstack1l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡮ࡹࠠࡶࡲࠣࡸࡴࠦࡤࡢࡶࡨࠤ࠭ࡋࡔࡢࡩࠣࡹࡳࡩࡨࡢࡰࡪࡩࡩ࠯ࠢ὆"))
          return True
        self.logger.debug(bstack1l_opy_ (u"ࠨࡎࡦࡹࠣࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡹࡩࡷࡹࡩࡰࡰࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪ࠲ࠠࡥࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡻࡰࡥࡣࡷࡩࠧ὇"))
        return False
      except Exception as e:
        self.logger.warn(bstack1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧ࡭࡫ࡣ࡬ࠢࡩࡳࡷࠦࡢࡪࡰࡤࡶࡾࠦࡵࡱࡦࡤࡸࡪࡹࠬࠡࡷࡶ࡭ࡳ࡭ࠠࡦࡺ࡬ࡷࡹ࡯࡮ࡨࠢࡥ࡭ࡳࡧࡲࡺ࠼ࠣࡿࢂࠨὈ").format(e))
    return False
  def bstack111111ll11l_opy_(self, bstack111111l1l1l_opy_, bstack111111ll111_opy_):
    try:
      headers = {
        bstack1l_opy_ (u"ࠣࡋࡩ࠱ࡓࡵ࡮ࡦ࠯ࡐࡥࡹࡩࡨࠣὉ"): bstack111111l1l1l_opy_
      }
      response = bstack1ll1llll11_opy_(bstack1l_opy_ (u"ࠩࡊࡉ࡙࠭Ὂ"), bstack111111ll111_opy_, {}, {bstack1l_opy_ (u"ࠥ࡬ࡪࡧࡤࡦࡴࡶࠦὋ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡧ࡭࡫ࡣ࡬࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡷࡳࡨࡦࡺࡥࡴ࠼ࠣࡿࢂࠨὌ").format(e))
  @measure(event_name=EVENTS.bstack11l1l1ll11l_opy_, stage=STAGE.bstack11ll111111_opy_)
  def bstack1lllll1lll11_opy_(self, bstack111111ll111_opy_, bstack11111111l11_opy_):
    try:
      bstack1lllllll1l1l_opy_ = self.bstack1lllll1llll1_opy_()
      bstack1llllll11ll1_opy_ = os.path.join(bstack1lllllll1l1l_opy_, bstack1l_opy_ (u"ࠬࡶࡥࡳࡥࡼ࠲ࡿ࡯ࡰࠨὍ"))
      bstack1llllll11l1l_opy_ = os.path.join(bstack1lllllll1l1l_opy_, bstack11111111l11_opy_)
      if self.bstack1lllllll1lll_opy_(bstack1lllllll1l1l_opy_, bstack111111ll111_opy_): # if bstack1llllll1ll1l_opy_, bstack1llllllllll_opy_ bstack111111l1ll1_opy_ is bstack11111111l1l_opy_ to bstack111l1llll11_opy_ version available (response 304)
        if os.path.exists(bstack1llllll11l1l_opy_):
          self.logger.info(bstack1l_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬࡯ࡶࡰࡧࠤ࡮ࡴࠠࡼࡿ࠯ࠤࡸࡱࡩࡱࡲ࡬ࡲ࡬ࠦࡤࡰࡹࡱࡰࡴࡧࡤࠣ὎").format(bstack1llllll11l1l_opy_))
          return bstack1llllll11l1l_opy_
        if os.path.exists(bstack1llllll11ll1_opy_):
          self.logger.info(bstack1l_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡺࡪࡲࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࢁࡽ࠭ࠢࡸࡲࡿ࡯ࡰࡱ࡫ࡱ࡫ࠧ὏").format(bstack1llllll11ll1_opy_))
          return self.bstack1lllllll1ll1_opy_(bstack1llllll11ll1_opy_, bstack11111111l11_opy_)
      self.logger.info(bstack1l_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥ࡬ࡲࡰ࡯ࠣࡿࢂࠨὐ").format(bstack111111ll111_opy_))
      response = bstack1ll1llll11_opy_(bstack1l_opy_ (u"ࠩࡊࡉ࡙࠭ὑ"), bstack111111ll111_opy_, {}, {})
      if response.status_code == 200:
        bstack1111111l1l1_opy_ = response.headers.get(bstack1l_opy_ (u"ࠥࡉ࡙ࡧࡧࠣὒ"), bstack1l_opy_ (u"ࠦࠧὓ"))
        if bstack1111111l1l1_opy_:
          self.bstack1llllll1l1l1_opy_(bstack1lllllll1l1l_opy_, bstack1111111l1l1_opy_)
        with open(bstack1llllll11ll1_opy_, bstack1l_opy_ (u"ࠬࡽࡢࠨὔ")) as file:
          file.write(response.content)
        self.logger.info(bstack1l_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡦࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡤࡲࡩࠦࡳࡢࡸࡨࡨࠥࡧࡴࠡࡽࢀࠦὕ").format(bstack1llllll11ll1_opy_))
        return self.bstack1lllllll1ll1_opy_(bstack1llllll11ll1_opy_, bstack11111111l11_opy_)
      else:
        raise(bstack1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡺࡨࡦࠢࡩ࡭ࡱ࡫࠮ࠡࡕࡷࡥࡹࡻࡳࠡࡥࡲࡨࡪࡀࠠࡼࡿࠥὖ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡰࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽ࠿ࠦࡻࡾࠤὗ").format(e))
  def bstack11111111lll_opy_(self, bstack111111ll111_opy_, bstack11111111l11_opy_):
    try:
      retry = 2
      bstack1llllll11l1l_opy_ = None
      bstack1111111l11l_opy_ = False
      while retry > 0:
        bstack1llllll11l1l_opy_ = self.bstack1lllll1lll11_opy_(bstack111111ll111_opy_, bstack11111111l11_opy_)
        bstack1111111l11l_opy_ = self.bstack1111111ll1l_opy_(bstack111111ll111_opy_, bstack11111111l11_opy_, bstack1llllll11l1l_opy_)
        if bstack1111111l11l_opy_:
          break
        retry -= 1
      return bstack1llllll11l1l_opy_, bstack1111111l11l_opy_
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡭ࡥࡵࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡲࡤࡸ࡭ࠨ὘").format(e))
    return bstack1llllll11l1l_opy_, False
  def bstack1111111ll1l_opy_(self, bstack111111ll111_opy_, bstack11111111l11_opy_, bstack1llllll11l1l_opy_, bstack1llllll1lll1_opy_ = 0):
    if bstack1llllll1lll1_opy_ > 1:
      return False
    if bstack1llllll11l1l_opy_ == None or os.path.exists(bstack1llllll11l1l_opy_) == False:
      self.logger.warn(bstack1l_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡳࡥࡹ࡮ࠠ࡯ࡱࡷࠤ࡫ࡵࡵ࡯ࡦ࠯ࠤࡷ࡫ࡴࡳࡻ࡬ࡲ࡬ࠦࡤࡰࡹࡱࡰࡴࡧࡤࠣὙ"))
      return False
    bstack1llllllll11l_opy_ = bstack1l_opy_ (u"ࡶࠧࡤ࠮ࠫࡂࡳࡩࡷࡩࡹ࠰ࡥ࡯࡭ࠥࡢࡤࠬ࡞࠱ࡠࡩ࠱࡜࠯࡞ࡧ࠯ࠧ὚")
    command = bstack1l_opy_ (u"ࠬࢁࡽࠡ࠯࠰ࡺࡪࡸࡳࡪࡱࡱࠫὛ").format(bstack1llllll11l1l_opy_)
    bstack1111111l1ll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1llllllll11l_opy_, bstack1111111l1ll_opy_) != None:
      return True
    else:
      self.logger.error(bstack1l_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡼࡥࡳࡵ࡬ࡳࡳࠦࡣࡩࡧࡦ࡯ࠥ࡬ࡡࡪ࡮ࡨࡨࠧ὜"))
      return False
  def bstack1lllllll1ll1_opy_(self, bstack1llllll11ll1_opy_, bstack11111111l11_opy_):
    try:
      working_dir = os.path.dirname(bstack1llllll11ll1_opy_)
      shutil.unpack_archive(bstack1llllll11ll1_opy_, working_dir)
      bstack1llllll11l1l_opy_ = os.path.join(working_dir, bstack11111111l11_opy_)
      os.chmod(bstack1llllll11l1l_opy_, 0o755)
      return bstack1llllll11l1l_opy_
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡹࡳࢀࡩࡱࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠣὝ"))
  def bstack1lllllll1111_opy_(self):
    try:
      bstack1llllllll111_opy_ = self.config.get(bstack1l_opy_ (u"ࠨࡲࡨࡶࡨࡿࠧ὞"))
      bstack1lllllll1111_opy_ = bstack1llllllll111_opy_ or (bstack1llllllll111_opy_ is None and self.bstack111lll1lll_opy_)
      if not bstack1lllllll1111_opy_ or self.config.get(bstack1l_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬὟ"), None) not in bstack11l1l1111ll_opy_:
        return False
      self.bstack1ll1ll1ll_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡧࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧὠ").format(e))
  def bstack1llllll1ll11_opy_(self):
    try:
      bstack1llllll1ll11_opy_ = self.percy_capture_mode
      return bstack1llllll1ll11_opy_
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡨࡺࠠࡱࡧࡵࡧࡾࠦࡣࡢࡲࡷࡹࡷ࡫ࠠ࡮ࡱࡧࡩ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧὡ").format(e))
  def init(self, bstack111lll1lll_opy_, config, logger):
    self.bstack111lll1lll_opy_ = bstack111lll1lll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllllll1111_opy_():
      return
    self.bstack1llllll111l1_opy_ = config.get(bstack1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࡓࡵࡺࡩࡰࡰࡶࠫὢ"), {})
    self.percy_capture_mode = config.get(bstack1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࡈࡧࡰࡵࡷࡵࡩࡒࡵࡤࡦࠩὣ"))
    try:
      bstack111111ll111_opy_, bstack11111111l11_opy_ = self.bstack1llllllll1l1_opy_()
      self.bstack1111l1l11l1_opy_ = bstack11111111l11_opy_
      bstack1llllll11l1l_opy_, bstack1111111l11l_opy_ = self.bstack11111111lll_opy_(bstack111111ll111_opy_, bstack11111111l11_opy_)
      if bstack1111111l11l_opy_:
        self.binary_path = bstack1llllll11l1l_opy_
        thread = Thread(target=self.bstack1llllllllll1_opy_)
        thread.start()
      else:
        self.bstack1111111lll1_opy_ = True
        self.logger.error(bstack1l_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡲࡨࡶࡨࡿࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡶࡰࡧࠤ࠲ࠦࡻࡾ࠮࡙ࠣࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡖࡥࡳࡥࡼࠦὤ").format(bstack1llllll11l1l_opy_))
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤὥ").format(e))
  def bstack1llllll1111l_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1l_opy_ (u"ࠩ࡯ࡳ࡬࠭ὦ"), bstack1l_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰࡯ࡳ࡬࠭ὧ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1l_opy_ (u"ࠦࡕࡻࡳࡩ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡱࡵࡧࡴࠢࡤࡸࠥࢁࡽࠣὨ").format(logfile))
      self.bstack1llllll11111_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡨࡸࠥࡶࡥࡳࡥࡼࠤࡱࡵࡧࠡࡲࡤࡸ࡭࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨὩ").format(e))
  @measure(event_name=EVENTS.bstack11l11lll1ll_opy_, stage=STAGE.bstack11ll111111_opy_)
  def bstack1llllllllll1_opy_(self):
    bstack111111111ll_opy_ = self.bstack111111l1l11_opy_()
    if bstack111111111ll_opy_ == None:
      self.bstack1111111lll1_opy_ = True
      self.logger.error(bstack1l_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡺ࡯࡬ࡧࡱࠤࡳࡵࡴࠡࡨࡲࡹࡳࡪࠬࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺࠤὪ"))
      return False
    bstack1llllllll1ll_opy_ = [bstack1l_opy_ (u"ࠢࡢࡲࡳ࠾ࡪࡾࡥࡤ࠼ࡶࡸࡦࡸࡴࠣὫ") if self.bstack111lll1lll_opy_ else bstack1l_opy_ (u"ࠨࡧࡻࡩࡨࡀࡳࡵࡣࡵࡸࠬὬ")]
    bstack1111l111111_opy_ = self.bstack1llllll1l1ll_opy_()
    if bstack1111l111111_opy_ != None:
      bstack1llllllll1ll_opy_.append(bstack1l_opy_ (u"ࠤ࠰ࡧࠥࢁࡽࠣὭ").format(bstack1111l111111_opy_))
    env = os.environ.copy()
    env[bstack1l_opy_ (u"ࠥࡔࡊࡘࡃ࡚ࡡࡗࡓࡐࡋࡎࠣὮ")] = bstack111111111ll_opy_
    env[bstack1l_opy_ (u"࡙ࠦࡎ࡟ࡃࡗࡌࡐࡉࡥࡕࡖࡋࡇࠦὯ")] = os.environ.get(bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪὰ"), bstack1l_opy_ (u"࠭ࠧά"))
    bstack1lllll1lllll_opy_ = [self.binary_path]
    self.bstack1llllll1111l_opy_()
    self.bstack11111111111_opy_ = self.bstack1llllll11l11_opy_(bstack1lllll1lllll_opy_ + bstack1llllllll1ll_opy_, env)
    self.logger.debug(bstack1l_opy_ (u"ࠢࡔࡶࡤࡶࡹ࡯࡮ࡨࠢࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠣὲ"))
    bstack1llllll1lll1_opy_ = 0
    while self.bstack11111111111_opy_.poll() == None:
      bstack1lllll1ll1ll_opy_ = self.bstack111111ll1l1_opy_()
      if bstack1lllll1ll1ll_opy_:
        self.logger.debug(bstack1l_opy_ (u"ࠣࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࠦέ"))
        self.bstack1llllll111ll_opy_ = True
        return True
      bstack1llllll1lll1_opy_ += 1
      self.logger.debug(bstack1l_opy_ (u"ࠤࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡔࡨࡸࡷࡿࠠ࠮ࠢࡾࢁࠧὴ").format(bstack1llllll1lll1_opy_))
      time.sleep(2)
    self.logger.error(bstack1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡎࡥࡢ࡮ࡷ࡬ࠥࡉࡨࡦࡥ࡮ࠤࡋࡧࡩ࡭ࡧࡧࠤࡦ࡬ࡴࡦࡴࠣࡿࢂࠦࡡࡵࡶࡨࡱࡵࡺࡳࠣή").format(bstack1llllll1lll1_opy_))
    self.bstack1111111lll1_opy_ = True
    return False
  def bstack111111ll1l1_opy_(self, bstack1llllll1lll1_opy_ = 0):
    if bstack1llllll1lll1_opy_ > 10:
      return False
    try:
      bstack1lllllllllll_opy_ = os.environ.get(bstack1l_opy_ (u"ࠫࡕࡋࡒࡄ࡛ࡢࡗࡊࡘࡖࡆࡔࡢࡅࡉࡊࡒࡆࡕࡖࠫὶ"), bstack1l_opy_ (u"ࠬ࡮ࡴࡵࡲ࠽࠳࠴ࡲ࡯ࡤࡣ࡯࡬ࡴࡹࡴ࠻࠷࠶࠷࠽࠭ί"))
      bstack111111l11ll_opy_ = bstack1lllllllllll_opy_ + bstack11l1l1ll1l1_opy_
      response = requests.get(bstack111111l11ll_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࠬὸ"), {}).get(bstack1l_opy_ (u"ࠧࡪࡦࠪό"), None)
      return True
    except:
      self.logger.debug(bstack1l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡰࡥࡦࡹࡷࡸࡥࡥࠢࡺ࡬࡮ࡲࡥࠡࡲࡵࡳࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥ࡮ࡥࡢ࡮ࡷ࡬ࠥࡩࡨࡦࡥ࡮ࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠨὺ"))
      return False
  def bstack111111l1l11_opy_(self):
    bstack1111111111l_opy_ = bstack1l_opy_ (u"ࠩࡤࡴࡵ࠭ύ") if self.bstack111lll1lll_opy_ else bstack1l_opy_ (u"ࠪࡥࡺࡺ࡯࡮ࡣࡷࡩࠬὼ")
    bstack111111l1111_opy_ = bstack1l_opy_ (u"ࠦࡺࡴࡤࡦࡨ࡬ࡲࡪࡪࠢώ") if self.config.get(bstack1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫ὾")) is None else True
    bstack11ll11ll111_opy_ = bstack1l_opy_ (u"ࠨࡡࡱ࡫࠲ࡥࡵࡶ࡟ࡱࡧࡵࡧࡾ࠵ࡧࡦࡶࡢࡴࡷࡵࡪࡦࡥࡷࡣࡹࡵ࡫ࡦࡰࡂࡲࡦࡳࡥ࠾ࡽࢀࠪࡹࡿࡰࡦ࠿ࡾࢁࠫࡶࡥࡳࡥࡼࡁࢀࢃࠢ὿").format(self.config[bstack1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᾀ")], bstack1111111111l_opy_, bstack111111l1111_opy_)
    if self.percy_capture_mode:
      bstack11ll11ll111_opy_ += bstack1l_opy_ (u"ࠣࠨࡳࡩࡷࡩࡹࡠࡥࡤࡴࡹࡻࡲࡦࡡࡰࡳࡩ࡫࠽ࡼࡿࠥᾁ").format(self.percy_capture_mode)
    uri = bstack11lllll11_opy_(bstack11ll11ll111_opy_)
    try:
      response = bstack1ll1llll11_opy_(bstack1l_opy_ (u"ࠩࡊࡉ࡙࠭ᾂ"), uri, {}, {bstack1l_opy_ (u"ࠪࡥࡺࡺࡨࠨᾃ"): (self.config[bstack1l_opy_ (u"ࠫࡺࡹࡥࡳࡐࡤࡱࡪ࠭ᾄ")], self.config[bstack1l_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷࡐ࡫ࡹࠨᾅ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack1ll1ll1ll_opy_ = data.get(bstack1l_opy_ (u"࠭ࡳࡶࡥࡦࡩࡸࡹࠧᾆ"))
        self.percy_capture_mode = data.get(bstack1l_opy_ (u"ࠧࡱࡧࡵࡧࡾࡥࡣࡢࡲࡷࡹࡷ࡫࡟࡮ࡱࡧࡩࠬᾇ"))
        os.environ[bstack1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞࠭ᾈ")] = str(self.bstack1ll1ll1ll_opy_)
        os.environ[bstack1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟࡟ࡄࡃࡓࡘ࡚ࡘࡅࡠࡏࡒࡈࡊ࠭ᾉ")] = str(self.percy_capture_mode)
        if bstack111111l1111_opy_ == bstack1l_opy_ (u"ࠥࡹࡳࡪࡥࡧ࡫ࡱࡩࡩࠨᾊ") and str(self.bstack1ll1ll1ll_opy_).lower() == bstack1l_opy_ (u"ࠦࡹࡸࡵࡦࠤᾋ"):
          self.bstack11l11l11ll_opy_ = True
        if bstack1l_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᾌ") in data:
          return data[bstack1l_opy_ (u"ࠨࡴࡰ࡭ࡨࡲࠧᾍ")]
        else:
          raise bstack1l_opy_ (u"ࠧࡕࡱ࡮ࡩࡳࠦࡎࡰࡶࠣࡊࡴࡻ࡮ࡥࠢ࠰ࠤࢀࢃࠧᾎ").format(data)
      else:
        raise bstack1l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡴࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡸࡺࡡࡵࡷࡶࠤ࠲ࠦࡻࡾ࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥࡈ࡯ࡥࡻࠣ࠱ࠥࢁࡽࠣᾏ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡳࡶࡴࡰࡥࡤࡶࠥᾐ").format(e))
  def bstack1llllll1l1ll_opy_(self):
    bstack1llllll11lll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l_opy_ (u"ࠥࡴࡪࡸࡣࡺࡅࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳࠨᾑ"))
    try:
      if bstack1l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᾒ") not in self.bstack1llllll111l1_opy_:
        self.bstack1llllll111l1_opy_[bstack1l_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ᾓ")] = 2
      with open(bstack1llllll11lll_opy_, bstack1l_opy_ (u"࠭ࡷࠨᾔ")) as fp:
        json.dump(self.bstack1llllll111l1_opy_, fp)
      return bstack1llllll11lll_opy_
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡧࡷ࡫ࡡࡵࡧࠣࡴࡪࡸࡣࡺࠢࡦࡳࡳ࡬ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᾕ").format(e))
  def bstack1llllll11l11_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lllllll11l1_opy_ == bstack1l_opy_ (u"ࠨࡹ࡬ࡲࠬᾖ"):
        bstack111111l11l1_opy_ = [bstack1l_opy_ (u"ࠩࡦࡱࡩ࠴ࡥࡹࡧࠪᾗ"), bstack1l_opy_ (u"ࠪ࠳ࡨ࠭ᾘ")]
        cmd = bstack111111l11l1_opy_ + cmd
      cmd = bstack1l_opy_ (u"ࠫࠥ࠭ᾙ").join(cmd)
      self.logger.debug(bstack1l_opy_ (u"ࠧࡘࡵ࡯ࡰ࡬ࡲ࡬ࠦࡻࡾࠤᾚ").format(cmd))
      with open(self.bstack1llllll11111_opy_, bstack1l_opy_ (u"ࠨࡡࠣᾛ")) as bstack111111111l1_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack111111111l1_opy_, text=True, stderr=bstack111111111l1_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1111111lll1_opy_ = True
      self.logger.error(bstack1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠡࡹ࡬ࡸ࡭ࠦࡣ࡮ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤᾜ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllll111ll_opy_:
        self.logger.info(bstack1l_opy_ (u"ࠣࡕࡷࡳࡵࡶࡩ࡯ࡩࠣࡔࡪࡸࡣࡺࠤᾝ"))
        cmd = [self.binary_path, bstack1l_opy_ (u"ࠤࡨࡼࡪࡩ࠺ࡴࡶࡲࡴࠧᾞ")]
        self.bstack1llllll11l11_opy_(cmd)
        self.bstack1llllll111ll_opy_ = False
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡱࡳࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡧࡴࡳ࡭ࡢࡰࡧࠤ࠲ࠦࡻࡾ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᾟ").format(cmd, e))
  def bstack1l11111111_opy_(self):
    if not self.bstack1ll1ll1ll_opy_:
      return
    try:
      bstack1lllll1lll1l_opy_ = 0
      while not self.bstack1llllll111ll_opy_ and bstack1lllll1lll1l_opy_ < self.bstack1llllll1l111_opy_:
        if self.bstack1111111lll1_opy_:
          self.logger.info(bstack1l_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡩࡥ࡮ࡲࡥࡥࠤᾠ"))
          return
        time.sleep(1)
        bstack1lllll1lll1l_opy_ += 1
      os.environ[bstack1l_opy_ (u"ࠬࡖࡅࡓࡅ࡜ࡣࡇࡋࡓࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࠫᾡ")] = str(self.bstack1lllllll11ll_opy_())
      self.logger.info(bstack1l_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡹࡥࡵࡷࡳࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠢᾢ"))
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡪࡺࡵࡱࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᾣ").format(e))
  def bstack1lllllll11ll_opy_(self):
    if self.bstack111lll1lll_opy_:
      return
    try:
      bstack1lllll1ll11l_opy_ = [platform[bstack1l_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᾤ")].lower() for platform in self.config.get(bstack1l_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᾥ"), [])]
      bstack1llllll1llll_opy_ = sys.maxsize
      bstack1lllllll1l11_opy_ = bstack1l_opy_ (u"ࠪࠫᾦ")
      for browser in bstack1lllll1ll11l_opy_:
        if browser in self.bstack1lllll1ll111_opy_:
          bstack1lllllll111l_opy_ = self.bstack1lllll1ll111_opy_[browser]
        if bstack1lllllll111l_opy_ < bstack1llllll1llll_opy_:
          bstack1llllll1llll_opy_ = bstack1lllllll111l_opy_
          bstack1lllllll1l11_opy_ = browser
      return bstack1lllllll1l11_opy_
    except Exception as e:
      self.logger.error(bstack1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡨࡥࡴࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᾧ").format(e))
  @classmethod
  def bstack111l11ll1l_opy_(self):
    return os.getenv(bstack1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࠪᾨ"), bstack1l_opy_ (u"࠭ࡆࡢ࡮ࡶࡩࠬᾩ")).lower()
  @classmethod
  def bstack11ll1l1ll_opy_(self):
    return os.getenv(bstack1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫᾪ"), bstack1l_opy_ (u"ࠨࠩᾫ"))
  @classmethod
  def bstack11llllll1l1_opy_(cls, value):
    cls.bstack11l11l11ll_opy_ = value
  @classmethod
  def bstack1lllllllll1l_opy_(cls):
    return cls.bstack11l11l11ll_opy_
  @classmethod
  def bstack1l111111111_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1111111l111_opy_(cls):
    return cls.percy_build_id