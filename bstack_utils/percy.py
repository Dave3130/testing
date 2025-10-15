# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
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
from bstack_utils.helper import bstack1l11lllll_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l11lll11_opy_ import bstack1ll1ll11ll_opy_
class bstack1ll1llll1_opy_:
  working_dir = os.getcwd()
  bstack11lll1l111_opy_ = False
  config = {}
  bstack111l11l1l1l_opy_ = bstack1ll1l_opy_ (u"ࠪࠫἡ")
  binary_path = bstack1ll1l_opy_ (u"ࠫࠬἢ")
  bstack1llllll1111l_opy_ = bstack1ll1l_opy_ (u"ࠬ࠭ἣ")
  bstack11111l1l1_opy_ = False
  bstack111111l11l1_opy_ = None
  bstack111111ll111_opy_ = {}
  bstack1lllll1lll1l_opy_ = 300
  bstack1llllllll1ll_opy_ = False
  logger = None
  bstack111111l1lll_opy_ = False
  bstack11l1l11ll_opy_ = False
  percy_build_id = None
  bstack1lllllll1l11_opy_ = bstack1ll1l_opy_ (u"࠭ࠧἤ")
  bstack1lllllllllll_opy_ = {
    bstack1ll1l_opy_ (u"ࠧࡤࡪࡵࡳࡲ࡫ࠧἥ") : 1,
    bstack1ll1l_opy_ (u"ࠨࡨ࡬ࡶࡪ࡬࡯ࡹࠩἦ") : 2,
    bstack1ll1l_opy_ (u"ࠩࡨࡨ࡬࡫ࠧἧ") : 3,
    bstack1ll1l_opy_ (u"ࠪࡷࡦ࡬ࡡࡳ࡫ࠪἨ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1llllll1llll_opy_(self):
    bstack11111111lll_opy_ = bstack1ll1l_opy_ (u"ࠫࠬἩ")
    bstack1111111llll_opy_ = sys.platform
    bstack1lllllllll11_opy_ = bstack1ll1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࠫἪ")
    if re.match(bstack1ll1l_opy_ (u"ࠨࡤࡢࡴࡺ࡭ࡳࢂ࡭ࡢࡥࠣࡳࡸࠨἫ"), bstack1111111llll_opy_) != None:
      bstack11111111lll_opy_ = bstack11l11lll1ll_opy_ + bstack1ll1l_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡰࡵࡻ࠲ࡿ࡯ࡰࠣἬ")
      self.bstack1lllllll1l11_opy_ = bstack1ll1l_opy_ (u"ࠨ࡯ࡤࡧࠬἭ")
    elif re.match(bstack1ll1l_opy_ (u"ࠤࡰࡷࡼ࡯࡮ࡽ࡯ࡶࡽࡸࢂ࡭ࡪࡰࡪࡻࢁࡩࡹࡨࡹ࡬ࡲࢁࡨࡣࡤࡹ࡬ࡲࢁࡽࡩ࡯ࡥࡨࢀࡪࡳࡣࡽࡹ࡬ࡲ࠸࠸ࠢἮ"), bstack1111111llll_opy_) != None:
      bstack11111111lll_opy_ = bstack11l11lll1ll_opy_ + bstack1ll1l_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡻ࡮ࡴ࠮ࡻ࡫ࡳࠦἯ")
      bstack1lllllllll11_opy_ = bstack1ll1l_opy_ (u"ࠦࡵ࡫ࡲࡤࡻ࠱ࡩࡽ࡫ࠢἰ")
      self.bstack1lllllll1l11_opy_ = bstack1ll1l_opy_ (u"ࠬࡽࡩ࡯ࠩἱ")
    else:
      bstack11111111lll_opy_ = bstack11l11lll1ll_opy_ + bstack1ll1l_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡬ࡪࡰࡸࡼ࠳ࢀࡩࡱࠤἲ")
      self.bstack1lllllll1l11_opy_ = bstack1ll1l_opy_ (u"ࠧ࡭࡫ࡱࡹࡽ࠭ἳ")
    return bstack11111111lll_opy_, bstack1lllllllll11_opy_
  def bstack1111111l1ll_opy_(self):
    try:
      bstack111111ll11l_opy_ = [os.path.join(expanduser(bstack1ll1l_opy_ (u"ࠣࢀࠥἴ")), bstack1ll1l_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩἵ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack111111ll11l_opy_:
        if(self.bstack1lllll1ll111_opy_(path)):
          return path
      raise bstack1ll1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢἶ")
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡲࡤࡸ࡭ࠦࡦࡰࡴࠣࡴࡪࡸࡣࡺࠢࡧࡳࡼࡴ࡬ࡰࡣࡧ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࠯ࠣࡿࢂࠨἷ").format(e))
  def bstack1lllll1ll111_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1llllll1l111_opy_(self, bstack111111l1ll1_opy_):
    return os.path.join(bstack111111l1ll1_opy_, self.bstack111l11l1l1l_opy_ + bstack1ll1l_opy_ (u"ࠧ࠴ࡥࡵࡣࡪࠦἸ"))
  def bstack1llllll1ll1l_opy_(self, bstack111111l1ll1_opy_, bstack111111111ll_opy_):
    if not bstack111111111ll_opy_: return
    try:
      bstack1llllllll11l_opy_ = self.bstack1llllll1l111_opy_(bstack111111l1ll1_opy_)
      with open(bstack1llllllll11l_opy_, bstack1ll1l_opy_ (u"ࠨࡷࠣἹ")) as f:
        f.write(bstack111111111ll_opy_)
        self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡔࡣࡹࡩࡩࠦ࡮ࡦࡹࠣࡉ࡙ࡧࡧࠡࡨࡲࡶࠥࡶࡥࡳࡥࡼࠦἺ"))
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡧࡶࡦࠢࡷ࡬ࡪࠦࡥࡵࡣࡪ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣἻ").format(e))
  def bstack1111111ll11_opy_(self, bstack111111l1ll1_opy_):
    try:
      bstack1llllllll11l_opy_ = self.bstack1llllll1l111_opy_(bstack111111l1ll1_opy_)
      if os.path.exists(bstack1llllllll11l_opy_):
        with open(bstack1llllllll11l_opy_, bstack1ll1l_opy_ (u"ࠤࡵࠦἼ")) as f:
          bstack111111111ll_opy_ = f.read().strip()
          return bstack111111111ll_opy_ if bstack111111111ll_opy_ else None
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡰࡴࡧࡤࡪࡰࡪࠤࡊ࡚ࡡࡨ࠮ࠣࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨἽ").format(e))
  def bstack1111111lll1_opy_(self, bstack111111l1ll1_opy_, bstack11111111lll_opy_):
    bstack1llllllllll1_opy_ = self.bstack1111111ll11_opy_(bstack111111l1ll1_opy_)
    if bstack1llllllllll1_opy_:
      try:
        bstack11111111ll1_opy_ = self.bstack1lllllll1111_opy_(bstack1llllllllll1_opy_, bstack11111111lll_opy_)
        if not bstack11111111ll1_opy_:
          self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣ࡭ࡸࠦࡵࡱࠢࡷࡳࠥࡪࡡࡵࡧࠣࠬࡊ࡚ࡡࡨࠢࡸࡲࡨ࡮ࡡ࡯ࡩࡨࡨ࠮ࠨἾ"))
          return True
        self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡔࡥࡸࠢࡓࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩ࠱ࠦࡤࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡺࡶࡤࡢࡶࡨࠦἿ"))
        return False
      except Exception as e:
        self.logger.warn(bstack1ll1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡦ࡬ࡪࡩ࡫ࠡࡨࡲࡶࠥࡨࡩ࡯ࡣࡵࡽࠥࡻࡰࡥࡣࡷࡩࡸ࠲ࠠࡶࡵ࡬ࡲ࡬ࠦࡥࡹ࡫ࡶࡸ࡮ࡴࡧࠡࡤ࡬ࡲࡦࡸࡹ࠻ࠢࡾࢁࠧὀ").format(e))
    return False
  def bstack1lllllll1111_opy_(self, bstack1llllllllll1_opy_, bstack11111111lll_opy_):
    try:
      headers = {
        bstack1ll1l_opy_ (u"ࠢࡊࡨ࠰ࡒࡴࡴࡥ࠮ࡏࡤࡸࡨ࡮ࠢὁ"): bstack1llllllllll1_opy_
      }
      response = bstack1l11lllll_opy_(bstack1ll1l_opy_ (u"ࠨࡉࡈࡘࠬὂ"), bstack11111111lll_opy_, {}, {bstack1ll1l_opy_ (u"ࠤ࡫ࡩࡦࡪࡥࡳࡵࠥὃ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack1ll1l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡦ࡬ࡪࡩ࡫ࡪࡰࡪࠤ࡫ࡵࡲࠡࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡶࡲࡧࡥࡹ࡫ࡳ࠻ࠢࡾࢁࠧὄ").format(e))
  @measure(event_name=EVENTS.bstack11l11ll1ll1_opy_, stage=STAGE.bstack11lll11ll_opy_)
  def bstack1lllllll11ll_opy_(self, bstack11111111lll_opy_, bstack1lllllllll11_opy_):
    try:
      bstack1lllllll1ll1_opy_ = self.bstack1111111l1ll_opy_()
      bstack1lllll1lllll_opy_ = os.path.join(bstack1lllllll1ll1_opy_, bstack1ll1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡾ࡮ࡶࠧὅ"))
      bstack1llllllll111_opy_ = os.path.join(bstack1lllllll1ll1_opy_, bstack1lllllllll11_opy_)
      if self.bstack1111111lll1_opy_(bstack1lllllll1ll1_opy_, bstack11111111lll_opy_): # if bstack1llllll111ll_opy_, bstack1llllllllll_opy_ bstack111111111ll_opy_ is bstack1lllllll11l1_opy_ to bstack1111l1l11l1_opy_ version available (response 304)
        if os.path.exists(bstack1llllllll111_opy_):
          self.logger.info(bstack1ll1l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡻࡾ࠮ࠣࡷࡰ࡯ࡰࡱ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢ὆").format(bstack1llllllll111_opy_))
          return bstack1llllllll111_opy_
        if os.path.exists(bstack1lllll1lllll_opy_):
          self.logger.info(bstack1ll1l_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࢀࡩࡱࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡷࡱࡾ࡮ࡶࡰࡪࡰࡪࠦ὇").format(bstack1lllll1lllll_opy_))
          return self.bstack111111l111l_opy_(bstack1lllll1lllll_opy_, bstack1lllllllll11_opy_)
      self.logger.info(bstack1ll1l_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥ࡫ࡱ࡫ࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤ࡫ࡸ࡯࡮ࠢࡾࢁࠧὈ").format(bstack11111111lll_opy_))
      response = bstack1l11lllll_opy_(bstack1ll1l_opy_ (u"ࠨࡉࡈࡘࠬὉ"), bstack11111111lll_opy_, {}, {})
      if response.status_code == 200:
        bstack111111l1111_opy_ = response.headers.get(bstack1ll1l_opy_ (u"ࠤࡈࡘࡦ࡭ࠢὊ"), bstack1ll1l_opy_ (u"ࠥࠦὋ"))
        if bstack111111l1111_opy_:
          self.bstack1llllll1ll1l_opy_(bstack1lllllll1ll1_opy_, bstack111111l1111_opy_)
        with open(bstack1lllll1lllll_opy_, bstack1ll1l_opy_ (u"ࠫࡼࡨࠧὌ")) as file:
          file.write(response.content)
        self.logger.info(bstack1ll1l_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡥࡥࠢࡳࡩࡷࡩࡹࠡࡤ࡬ࡲࡦࡸࡹࠡࡣࡱࡨࠥࡹࡡࡷࡧࡧࠤࡦࡺࠠࡼࡿࠥὍ").format(bstack1lllll1lllll_opy_))
        return self.bstack111111l111l_opy_(bstack1lllll1lllll_opy_, bstack1lllllllll11_opy_)
      else:
        raise(bstack1ll1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡹ࡮ࡥࠡࡨ࡬ࡰࡪ࠴ࠠࡔࡶࡤࡸࡺࡹࠠࡤࡱࡧࡩ࠿ࠦࡻࡾࠤ὎").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼ࠾ࠥࢁࡽࠣ὏").format(e))
  def bstack11111111111_opy_(self, bstack11111111lll_opy_, bstack1lllllllll11_opy_):
    try:
      retry = 2
      bstack1llllllll111_opy_ = None
      bstack1lllll1ll1l1_opy_ = False
      while retry > 0:
        bstack1llllllll111_opy_ = self.bstack1lllllll11ll_opy_(bstack11111111lll_opy_, bstack1lllllllll11_opy_)
        bstack1lllll1ll1l1_opy_ = self.bstack1llllll111l1_opy_(bstack11111111lll_opy_, bstack1lllllllll11_opy_, bstack1llllllll111_opy_)
        if bstack1lllll1ll1l1_opy_:
          break
        retry -= 1
      return bstack1llllllll111_opy_, bstack1lllll1ll1l1_opy_
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤ࡬࡫ࡴࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡱࡣࡷ࡬ࠧὐ").format(e))
    return bstack1llllllll111_opy_, False
  def bstack1llllll111l1_opy_(self, bstack11111111lll_opy_, bstack1lllllllll11_opy_, bstack1llllllll111_opy_, bstack1llllll11l11_opy_ = 0):
    if bstack1llllll11l11_opy_ > 1:
      return False
    if bstack1llllllll111_opy_ == None or os.path.exists(bstack1llllllll111_opy_) == False:
      self.logger.warn(bstack1ll1l_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦ࡮ࡰࡶࠣࡪࡴࡻ࡮ࡥ࠮ࠣࡶࡪࡺࡲࡺ࡫ࡱ࡫ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠢὑ"))
      return False
    bstack111111l1l1l_opy_ = bstack1ll1l_opy_ (u"ࡵࠦࡣ࠴ࠪࡁࡲࡨࡶࡨࡿ࠯ࡤ࡮࡬ࠤࡡࡪࠫ࡝࠰࡟ࡨ࠰ࡢ࠮࡝ࡦ࠮ࠦὒ")
    command = bstack1ll1l_opy_ (u"ࠫࢀࢃࠠ࠮࠯ࡹࡩࡷࡹࡩࡰࡰࠪὓ").format(bstack1llllllll111_opy_)
    bstack111111l11ll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack111111l1l1l_opy_, bstack111111l11ll_opy_) != None:
      return True
    else:
      self.logger.error(bstack1ll1l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡻ࡫ࡲࡴ࡫ࡲࡲࠥࡩࡨࡦࡥ࡮ࠤ࡫ࡧࡩ࡭ࡧࡧࠦὔ"))
      return False
  def bstack111111l111l_opy_(self, bstack1lllll1lllll_opy_, bstack1lllllllll11_opy_):
    try:
      working_dir = os.path.dirname(bstack1lllll1lllll_opy_)
      shutil.unpack_archive(bstack1lllll1lllll_opy_, working_dir)
      bstack1llllllll111_opy_ = os.path.join(working_dir, bstack1lllllllll11_opy_)
      os.chmod(bstack1llllllll111_opy_, 0o755)
      return bstack1llllllll111_opy_
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡸࡲࡿ࡯ࡰࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢὕ"))
  def bstack1llllllll1l1_opy_(self):
    try:
      bstack1llllll11lll_opy_ = self.config.get(bstack1ll1l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ὖ"))
      bstack1llllllll1l1_opy_ = bstack1llllll11lll_opy_ or (bstack1llllll11lll_opy_ is None and self.bstack11lll1l111_opy_)
      if not bstack1llllllll1l1_opy_ or self.config.get(bstack1ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫὗ"), None) not in bstack11l1l1l1l1l_opy_:
        return False
      self.bstack11111l1l1_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦ὘").format(e))
  def bstack11111111l1l_opy_(self):
    try:
      bstack11111111l1l_opy_ = self.percy_capture_mode
      return bstack11111111l1l_opy_
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡦࡶࡨࡧࡹࠦࡰࡦࡴࡦࡽࠥࡩࡡࡱࡶࡸࡶࡪࠦ࡭ࡰࡦࡨ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦὙ").format(e))
  def init(self, bstack11lll1l111_opy_, config, logger):
    self.bstack11lll1l111_opy_ = bstack11lll1l111_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1llllllll1l1_opy_():
      return
    self.bstack111111ll111_opy_ = config.get(bstack1ll1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡒࡴࡹ࡯࡯࡯ࡵࠪ὚"), {})
    self.percy_capture_mode = config.get(bstack1ll1l_opy_ (u"ࠬࡶࡥࡳࡥࡼࡇࡦࡶࡴࡶࡴࡨࡑࡴࡪࡥࠨὛ"))
    try:
      bstack11111111lll_opy_, bstack1lllllllll11_opy_ = self.bstack1llllll1llll_opy_()
      self.bstack111l11l1l1l_opy_ = bstack1lllllllll11_opy_
      bstack1llllllll111_opy_, bstack1lllll1ll1l1_opy_ = self.bstack11111111111_opy_(bstack11111111lll_opy_, bstack1lllllllll11_opy_)
      if bstack1lllll1ll1l1_opy_:
        self.binary_path = bstack1llllllll111_opy_
        thread = Thread(target=self.bstack1llllll1l1l1_opy_)
        thread.start()
      else:
        self.bstack111111l1lll_opy_ = True
        self.logger.error(bstack1ll1l_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡾࠦࡰࡢࡶ࡫ࠤ࡫ࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡕ࡫ࡲࡤࡻࠥ὜").format(bstack1llllllll111_opy_))
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣὝ").format(e))
  def bstack1lllll1llll1_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1ll1l_opy_ (u"ࠨ࡮ࡲ࡫ࠬ὞"), bstack1ll1l_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯࡮ࡲ࡫ࠬὟ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1ll1l_opy_ (u"ࠥࡔࡺࡹࡨࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࡳࠡࡣࡷࠤࢀࢃࠢὠ").format(logfile))
      self.bstack1llllll1111l_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡰࡴ࡭ࠠࡱࡣࡷ࡬࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧὡ").format(e))
  @measure(event_name=EVENTS.bstack11l1l11l111_opy_, stage=STAGE.bstack11lll11ll_opy_)
  def bstack1llllll1l1l1_opy_(self):
    bstack1lllll1l1lll_opy_ = self.bstack1llllll11111_opy_()
    if bstack1lllll1l1lll_opy_ == None:
      self.bstack111111l1lll_opy_ = True
      self.logger.error(bstack1ll1l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡹࡵ࡫ࡦࡰࠣࡲࡴࡺࠠࡧࡱࡸࡲࡩ࠲ࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠣὢ"))
      return False
    bstack111111111l1_opy_ = [bstack1ll1l_opy_ (u"ࠨࡡࡱࡲ࠽ࡩࡽ࡫ࡣ࠻ࡵࡷࡥࡷࡺࠢὣ") if self.bstack11lll1l111_opy_ else bstack1ll1l_opy_ (u"ࠧࡦࡺࡨࡧ࠿ࡹࡴࡢࡴࡷࠫὤ")]
    bstack11111ll1lll_opy_ = self.bstack1lllll1ll1ll_opy_()
    if bstack11111ll1lll_opy_ != None:
      bstack111111111l1_opy_.append(bstack1ll1l_opy_ (u"ࠣ࠯ࡦࠤࢀࢃࠢὥ").format(bstack11111ll1lll_opy_))
    env = os.environ.copy()
    env[bstack1ll1l_opy_ (u"ࠤࡓࡉࡗࡉ࡙ࡠࡖࡒࡏࡊࡔࠢὦ")] = bstack1lllll1l1lll_opy_
    env[bstack1ll1l_opy_ (u"ࠥࡘࡍࡥࡂࡖࡋࡏࡈࡤ࡛ࡕࡊࡆࠥὧ")] = os.environ.get(bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩὨ"), bstack1ll1l_opy_ (u"ࠬ࠭Ὡ"))
    bstack1111111111l_opy_ = [self.binary_path]
    self.bstack1lllll1llll1_opy_()
    self.bstack111111l11l1_opy_ = self.bstack1lllllllll1l_opy_(bstack1111111111l_opy_ + bstack111111111l1_opy_, env)
    self.logger.debug(bstack1ll1l_opy_ (u"ࠨࡓࡵࡣࡵࡸ࡮ࡴࡧࠡࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠢὪ"))
    bstack1llllll11l11_opy_ = 0
    while self.bstack111111l11l1_opy_.poll() == None:
      bstack11111111l11_opy_ = self.bstack1llllll1l1ll_opy_()
      if bstack11111111l11_opy_:
        self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠥὫ"))
        self.bstack1llllllll1ll_opy_ = True
        return True
      bstack1llllll11l11_opy_ += 1
      self.logger.debug(bstack1ll1l_opy_ (u"ࠣࡊࡨࡥࡱࡺࡨࠡࡅ࡫ࡩࡨࡱࠠࡓࡧࡷࡶࡾࠦ࠭ࠡࡽࢀࠦὬ").format(bstack1llllll11l11_opy_))
      time.sleep(2)
    self.logger.error(bstack1ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡍ࡫ࡡ࡭ࡶ࡫ࠤࡈ࡮ࡥࡤ࡭ࠣࡊࡦ࡯࡬ࡦࡦࠣࡥ࡫ࡺࡥࡳࠢࡾࢁࠥࡧࡴࡵࡧࡰࡴࡹࡹࠢὭ").format(bstack1llllll11l11_opy_))
    self.bstack111111l1lll_opy_ = True
    return False
  def bstack1llllll1l1ll_opy_(self, bstack1llllll11l11_opy_ = 0):
    if bstack1llllll11l11_opy_ > 10:
      return False
    try:
      bstack1111111l111_opy_ = os.environ.get(bstack1ll1l_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡖࡉࡗ࡜ࡅࡓࡡࡄࡈࡉࡘࡅࡔࡕࠪὮ"), bstack1ll1l_opy_ (u"ࠫ࡭ࡺࡴࡱ࠼࠲࠳ࡱࡵࡣࡢ࡮࡫ࡳࡸࡺ࠺࠶࠵࠶࠼ࠬὯ"))
      bstack1llllll11l1l_opy_ = bstack1111111l111_opy_ + bstack11l1l11l1ll_opy_
      response = requests.get(bstack1llllll11l1l_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1ll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࠫὰ"), {}).get(bstack1ll1l_opy_ (u"࠭ࡩࡥࠩά"), None)
      return True
    except:
      self.logger.debug(bstack1ll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦ࡯ࡤࡥࡸࡶࡷ࡫ࡤࠡࡹ࡫࡭ࡱ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡪࡰࡪࠤ࡭࡫ࡡ࡭ࡶ࡫ࠤࡨ࡮ࡥࡤ࡭ࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧὲ"))
      return False
  def bstack1llllll11111_opy_(self):
    bstack1llllll11ll1_opy_ = bstack1ll1l_opy_ (u"ࠨࡣࡳࡴࠬέ") if self.bstack11lll1l111_opy_ else bstack1ll1l_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫὴ")
    bstack1lllllll1l1l_opy_ = bstack1ll1l_opy_ (u"ࠥࡹࡳࡪࡥࡧ࡫ࡱࡩࡩࠨή") if self.config.get(bstack1ll1l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪὶ")) is None else True
    bstack11ll11l1lll_opy_ = bstack1ll1l_opy_ (u"ࠧࡧࡰࡪ࠱ࡤࡴࡵࡥࡰࡦࡴࡦࡽ࠴࡭ࡥࡵࡡࡳࡶࡴࡰࡥࡤࡶࡢࡸࡴࡱࡥ࡯ࡁࡱࡥࡲ࡫࠽ࡼࡿࠩࡸࡾࡶࡥ࠾ࡽࢀࠪࡵ࡫ࡲࡤࡻࡀࡿࢂࠨί").format(self.config[bstack1ll1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫὸ")], bstack1llllll11ll1_opy_, bstack1lllllll1l1l_opy_)
    if self.percy_capture_mode:
      bstack11ll11l1lll_opy_ += bstack1ll1l_opy_ (u"ࠢࠧࡲࡨࡶࡨࡿ࡟ࡤࡣࡳࡸࡺࡸࡥࡠ࡯ࡲࡨࡪࡃࡻࡾࠤό").format(self.percy_capture_mode)
    uri = bstack1ll1ll11ll_opy_(bstack11ll11l1lll_opy_)
    try:
      response = bstack1l11lllll_opy_(bstack1ll1l_opy_ (u"ࠨࡉࡈࡘࠬὺ"), uri, {}, {bstack1ll1l_opy_ (u"ࠩࡤࡹࡹ࡮ࠧύ"): (self.config[bstack1ll1l_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬὼ")], self.config[bstack1ll1l_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧώ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack11111l1l1_opy_ = data.get(bstack1ll1l_opy_ (u"ࠬࡹࡵࡤࡥࡨࡷࡸ࠭὾"))
        self.percy_capture_mode = data.get(bstack1ll1l_opy_ (u"࠭ࡰࡦࡴࡦࡽࡤࡩࡡࡱࡶࡸࡶࡪࡥ࡭ࡰࡦࡨࠫ὿"))
        os.environ[bstack1ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࠬᾀ")] = str(self.bstack11111l1l1_opy_)
        os.environ[bstack1ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬᾁ")] = str(self.percy_capture_mode)
        if bstack1lllllll1l1l_opy_ == bstack1ll1l_opy_ (u"ࠤࡸࡲࡩ࡫ࡦࡪࡰࡨࡨࠧᾂ") and str(self.bstack11111l1l1_opy_).lower() == bstack1ll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣᾃ"):
          self.bstack11l1l11ll_opy_ = True
        if bstack1ll1l_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥᾄ") in data:
          return data[bstack1ll1l_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᾅ")]
        else:
          raise bstack1ll1l_opy_ (u"࠭ࡔࡰ࡭ࡨࡲࠥࡔ࡯ࡵࠢࡉࡳࡺࡴࡤࠡ࠯ࠣࡿࢂ࠭ᾆ").format(data)
      else:
        raise bstack1ll1l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡳࡩࡷࡩࡹࠡࡶࡲ࡯ࡪࡴࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡷࡹࡧࡴࡶࡵࠣ࠱ࠥࢁࡽ࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡇࡵࡤࡺࠢ࠰ࠤࢀࢃࠢᾇ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡤࡴࡨࡥࡹ࡯࡮ࡨࠢࡳࡩࡷࡩࡹࠡࡲࡵࡳ࡯࡫ࡣࡵࠤᾈ").format(e))
  def bstack1lllll1ll1ll_opy_(self):
    bstack1111111l1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1l_opy_ (u"ࠤࡳࡩࡷࡩࡹࡄࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠧᾉ"))
    try:
      if bstack1ll1l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫᾊ") not in self.bstack111111ll111_opy_:
        self.bstack111111ll111_opy_[bstack1ll1l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᾋ")] = 2
      with open(bstack1111111l1l1_opy_, bstack1ll1l_opy_ (u"ࠬࡽࠧᾌ")) as fp:
        json.dump(self.bstack111111ll111_opy_, fp)
      return bstack1111111l1l1_opy_
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡦࡶࡪࡧࡴࡦࠢࡳࡩࡷࡩࡹࠡࡥࡲࡲ࡫࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᾍ").format(e))
  def bstack1lllllllll1l_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lllllll1l11_opy_ == bstack1ll1l_opy_ (u"ࠧࡸ࡫ࡱࠫᾎ"):
        bstack1111111l11l_opy_ = [bstack1ll1l_opy_ (u"ࠨࡥࡰࡨ࠳࡫ࡸࡦࠩᾏ"), bstack1ll1l_opy_ (u"ࠩ࠲ࡧࠬᾐ")]
        cmd = bstack1111111l11l_opy_ + cmd
      cmd = bstack1ll1l_opy_ (u"ࠪࠤࠬᾑ").join(cmd)
      self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡗࡻ࡮࡯࡫ࡱ࡫ࠥࢁࡽࠣᾒ").format(cmd))
      with open(self.bstack1llllll1111l_opy_, bstack1ll1l_opy_ (u"ࠧࡧࠢᾓ")) as bstack1lllllll111l_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lllllll111l_opy_, text=True, stderr=bstack1lllllll111l_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack111111l1lll_opy_ = True
      self.logger.error(bstack1ll1l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠠࡸ࡫ࡷ࡬ࠥࡩ࡭ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᾔ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllllll1ll_opy_:
        self.logger.info(bstack1ll1l_opy_ (u"ࠢࡔࡶࡲࡴࡵ࡯࡮ࡨࠢࡓࡩࡷࡩࡹࠣᾕ"))
        cmd = [self.binary_path, bstack1ll1l_opy_ (u"ࠣࡧࡻࡩࡨࡀࡳࡵࡱࡳࠦᾖ")]
        self.bstack1lllllllll1l_opy_(cmd)
        self.bstack1llllllll1ll_opy_ = False
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡰࡲࠣࡷࡪࡹࡳࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡦࡳࡲࡳࡡ࡯ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤᾗ").format(cmd, e))
  def bstack1ll1111l1l_opy_(self):
    if not self.bstack11111l1l1_opy_:
      return
    try:
      bstack1lllllll1lll_opy_ = 0
      while not self.bstack1llllllll1ll_opy_ and bstack1lllllll1lll_opy_ < self.bstack1lllll1lll1l_opy_:
        if self.bstack111111l1lll_opy_:
          self.logger.info(bstack1ll1l_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡶࡩࡹࡻࡰࠡࡨࡤ࡭ࡱ࡫ࡤࠣᾘ"))
          return
        time.sleep(1)
        bstack1lllllll1lll_opy_ += 1
      os.environ[bstack1ll1l_opy_ (u"ࠫࡕࡋࡒࡄ࡛ࡢࡆࡊ࡙ࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࠪᾙ")] = str(self.bstack1lllll1ll11l_opy_())
      self.logger.info(bstack1ll1l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡧࡴࡳࡰ࡭ࡧࡷࡩࡩࠨᾚ"))
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࡻࡰࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᾛ").format(e))
  def bstack1lllll1ll11l_opy_(self):
    if self.bstack11lll1l111_opy_:
      return
    try:
      bstack1111111ll1l_opy_ = [platform[bstack1ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠬᾜ")].lower() for platform in self.config.get(bstack1ll1l_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᾝ"), [])]
      bstack1lllll1lll11_opy_ = sys.maxsize
      bstack1llllll1l11l_opy_ = bstack1ll1l_opy_ (u"ࠩࠪᾞ")
      for browser in bstack1111111ll1l_opy_:
        if browser in self.bstack1lllllllllll_opy_:
          bstack1llllll1lll1_opy_ = self.bstack1lllllllllll_opy_[browser]
        if bstack1llllll1lll1_opy_ < bstack1lllll1lll11_opy_:
          bstack1lllll1lll11_opy_ = bstack1llllll1lll1_opy_
          bstack1llllll1l11l_opy_ = browser
      return bstack1llllll1l11l_opy_
    except Exception as e:
      self.logger.error(bstack1ll1l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡪࡰࡧࠤࡧ࡫ࡳࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰ࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᾟ").format(e))
  @classmethod
  def bstack11llll11l_opy_(self):
    return os.getenv(bstack1ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔࡊࡘࡃ࡚ࠩᾠ"), bstack1ll1l_opy_ (u"ࠬࡌࡡ࡭ࡵࡨࠫᾡ")).lower()
  @classmethod
  def bstack11lllll1ll_opy_(self):
    return os.getenv(bstack1ll1l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࡣࡈࡇࡐࡕࡗࡕࡉࡤࡓࡏࡅࡇࠪᾢ"), bstack1ll1l_opy_ (u"ࠧࠨᾣ"))
  @classmethod
  def bstack11llllllll1_opy_(cls, value):
    cls.bstack11l1l11ll_opy_ = value
  @classmethod
  def bstack111111l1l11_opy_(cls):
    return cls.bstack11l1l11ll_opy_
  @classmethod
  def bstack11lllllllll_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1llllll1ll11_opy_(cls):
    return cls.percy_build_id