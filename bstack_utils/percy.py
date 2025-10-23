# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
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
from bstack_utils.helper import bstack1l11l1ll1l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack1l1l11llll_opy_ import bstack11ll11l11_opy_
class bstack11lll11l1_opy_:
  working_dir = os.getcwd()
  bstack11l11lll1l_opy_ = False
  config = {}
  bstack1111ll1l111_opy_ = bstack111111l_opy_ (u"ࠬ࠭Ἔ")
  binary_path = bstack111111l_opy_ (u"࠭ࠧἝ")
  bstack1llllll11l11_opy_ = bstack111111l_opy_ (u"ࠧࠨ἞")
  bstack11l11l111l_opy_ = False
  bstack1llllll11lll_opy_ = None
  bstack1111111ll1l_opy_ = {}
  bstack111111l1l1l_opy_ = 300
  bstack1lllllll1ll1_opy_ = False
  logger = None
  bstack111111l1111_opy_ = False
  bstack1l1l111ll_opy_ = False
  percy_build_id = None
  bstack1lllllll1111_opy_ = bstack111111l_opy_ (u"ࠨࠩ἟")
  bstack1lllll1llll1_opy_ = {
    bstack111111l_opy_ (u"ࠩࡦ࡬ࡷࡵ࡭ࡦࠩἠ") : 1,
    bstack111111l_opy_ (u"ࠪࡪ࡮ࡸࡥࡧࡱࡻࠫἡ") : 2,
    bstack111111l_opy_ (u"ࠫࡪࡪࡧࡦࠩἢ") : 3,
    bstack111111l_opy_ (u"ࠬࡹࡡࡧࡣࡵ࡭ࠬἣ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1111111ll11_opy_(self):
    bstack1lllll1l1lll_opy_ = bstack111111l_opy_ (u"࠭ࠧἤ")
    bstack111111l111l_opy_ = sys.platform
    bstack1llllll111l1_opy_ = bstack111111l_opy_ (u"ࠧࡱࡧࡵࡧࡾ࠭ἥ")
    if re.match(bstack111111l_opy_ (u"ࠣࡦࡤࡶࡼ࡯࡮ࡽ࡯ࡤࡧࠥࡵࡳࠣἦ"), bstack111111l111l_opy_) != None:
      bstack1lllll1l1lll_opy_ = bstack11l1l1ll1l1_opy_ + bstack111111l_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯ࡲࡷࡽ࠴ࡺࡪࡲࠥἧ")
      self.bstack1lllllll1111_opy_ = bstack111111l_opy_ (u"ࠪࡱࡦࡩࠧἨ")
    elif re.match(bstack111111l_opy_ (u"ࠦࡲࡹࡷࡪࡰࡿࡱࡸࡿࡳࡽ࡯࡬ࡲ࡬ࡽࡼࡤࡻࡪࡻ࡮ࡴࡼࡣࡥࡦࡻ࡮ࡴࡼࡸ࡫ࡱࡧࡪࢂࡥ࡮ࡥࡿࡻ࡮ࡴ࠳࠳ࠤἩ"), bstack111111l111l_opy_) != None:
      bstack1lllll1l1lll_opy_ = bstack11l1l1ll1l1_opy_ + bstack111111l_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡽࡩ࡯࠰ࡽ࡭ࡵࠨἪ")
      bstack1llllll111l1_opy_ = bstack111111l_opy_ (u"ࠨࡰࡦࡴࡦࡽ࠳࡫ࡸࡦࠤἫ")
      self.bstack1lllllll1111_opy_ = bstack111111l_opy_ (u"ࠧࡸ࡫ࡱࠫἬ")
    else:
      bstack1lllll1l1lll_opy_ = bstack11l1l1ll1l1_opy_ + bstack111111l_opy_ (u"ࠣ࠱ࡳࡩࡷࡩࡹ࠮࡮࡬ࡲࡺࡾ࠮ࡻ࡫ࡳࠦἭ")
      self.bstack1lllllll1111_opy_ = bstack111111l_opy_ (u"ࠩ࡯࡭ࡳࡻࡸࠨἮ")
    return bstack1lllll1l1lll_opy_, bstack1llllll111l1_opy_
  def bstack1lllll1ll111_opy_(self):
    try:
      bstack1111111111l_opy_ = [os.path.join(expanduser(bstack111111l_opy_ (u"ࠥࢂࠧἯ")), bstack111111l_opy_ (u"ࠫ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠫἰ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1111111111l_opy_:
        if(self.bstack11111111lll_opy_(path)):
          return path
      raise bstack111111l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠤἱ")
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩ࡭ࡳࡪࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡴࡦࡺࡨࠡࡨࡲࡶࠥࡶࡥࡳࡥࡼࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࠱ࠥࢁࡽࠣἲ").format(e))
  def bstack11111111lll_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1111111llll_opy_(self, bstack11111111ll1_opy_):
    return os.path.join(bstack11111111ll1_opy_, self.bstack1111ll1l111_opy_ + bstack111111l_opy_ (u"ࠢ࠯ࡧࡷࡥ࡬ࠨἳ"))
  def bstack1lllll1ll1ll_opy_(self, bstack11111111ll1_opy_, bstack1lllllll11ll_opy_):
    if not bstack1lllllll11ll_opy_: return
    try:
      bstack1llllll1llll_opy_ = self.bstack1111111llll_opy_(bstack11111111ll1_opy_)
      with open(bstack1llllll1llll_opy_, bstack111111l_opy_ (u"ࠣࡹࠥἴ")) as f:
        f.write(bstack1lllllll11ll_opy_)
        self.logger.debug(bstack111111l_opy_ (u"ࠤࡖࡥࡻ࡫ࡤࠡࡰࡨࡻࠥࡋࡔࡢࡩࠣࡪࡴࡸࠠࡱࡧࡵࡧࡾࠨἵ"))
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡢࡸࡨࠤࡹ࡮ࡥࠡࡧࡷࡥ࡬࠲ࠠࡦࡴࡵࡳࡷࡀࠠࡼࡿࠥἶ").format(e))
  def bstack11111111111_opy_(self, bstack11111111ll1_opy_):
    try:
      bstack1llllll1llll_opy_ = self.bstack1111111llll_opy_(bstack11111111ll1_opy_)
      if os.path.exists(bstack1llllll1llll_opy_):
        with open(bstack1llllll1llll_opy_, bstack111111l_opy_ (u"ࠦࡷࠨἷ")) as f:
          bstack1lllllll11ll_opy_ = f.read().strip()
          return bstack1lllllll11ll_opy_ if bstack1lllllll11ll_opy_ else None
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡅࡕࡣࡪ࠰ࠥ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠣἸ").format(e))
  def bstack111111ll11l_opy_(self, bstack11111111ll1_opy_, bstack1lllll1l1lll_opy_):
    bstack1llllllll1ll_opy_ = self.bstack11111111111_opy_(bstack11111111ll1_opy_)
    if bstack1llllllll1ll_opy_:
      try:
        bstack1111111lll1_opy_ = self.bstack1lllllllll11_opy_(bstack1llllllll1ll_opy_, bstack1lllll1l1lll_opy_)
        if not bstack1111111lll1_opy_:
          self.logger.debug(bstack111111l_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡨࡩ࡯ࡣࡵࡽࠥ࡯ࡳࠡࡷࡳࠤࡹࡵࠠࡥࡣࡷࡩࠥ࠮ࡅࡕࡣࡪࠤࡺࡴࡣࡩࡣࡱ࡫ࡪࡪࠩࠣἹ"))
          return True
        self.logger.debug(bstack111111l_opy_ (u"ࠢࡏࡧࡺࠤࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡺࡪࡸࡳࡪࡱࡱࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠬࠡࡦࡲࡻࡳࡲ࡯ࡢࡦ࡬ࡲ࡬ࠦࡵࡱࡦࡤࡸࡪࠨἺ"))
        return False
      except Exception as e:
        self.logger.warn(bstack111111l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡨ࡮ࡥࡤ࡭ࠣࡪࡴࡸࠠࡣ࡫ࡱࡥࡷࡿࠠࡶࡲࡧࡥࡹ࡫ࡳ࠭ࠢࡸࡷ࡮ࡴࡧࠡࡧࡻ࡭ࡸࡺࡩ࡯ࡩࠣࡦ࡮ࡴࡡࡳࡻ࠽ࠤࢀࢃࠢἻ").format(e))
    return False
  def bstack1lllllllll11_opy_(self, bstack1llllllll1ll_opy_, bstack1lllll1l1lll_opy_):
    try:
      headers = {
        bstack111111l_opy_ (u"ࠤࡌࡪ࠲ࡔ࡯࡯ࡧ࠰ࡑࡦࡺࡣࡩࠤἼ"): bstack1llllllll1ll_opy_
      }
      response = bstack1l11l1ll1l_opy_(bstack111111l_opy_ (u"ࠪࡋࡊ࡚ࠧἽ"), bstack1lllll1l1lll_opy_, {}, {bstack111111l_opy_ (u"ࠦ࡭࡫ࡡࡥࡧࡵࡷࠧἾ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack111111l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡨ࡮ࡥࡤ࡭࡬ࡲ࡬ࠦࡦࡰࡴࠣࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡸࡴࡩࡧࡴࡦࡵ࠽ࠤࢀࢃࠢἿ").format(e))
  @measure(event_name=EVENTS.bstack11l1l11ll11_opy_, stage=STAGE.bstack11l11ll11_opy_)
  def bstack111111111l1_opy_(self, bstack1lllll1l1lll_opy_, bstack1llllll111l1_opy_):
    try:
      bstack1llllll11ll1_opy_ = self.bstack1lllll1ll111_opy_()
      bstack1llllllll1l1_opy_ = os.path.join(bstack1llllll11ll1_opy_, bstack111111l_opy_ (u"࠭ࡰࡦࡴࡦࡽ࠳ࢀࡩࡱࠩὀ"))
      bstack11111111l1l_opy_ = os.path.join(bstack1llllll11ll1_opy_, bstack1llllll111l1_opy_)
      if self.bstack111111ll11l_opy_(bstack1llllll11ll1_opy_, bstack1lllll1l1lll_opy_): # if bstack1llllll1ll11_opy_, bstack1llll1llll1_opy_ bstack1lllllll11ll_opy_ is bstack1llllllll111_opy_ to bstack1111ll1ll1l_opy_ version available (response 304)
        if os.path.exists(bstack11111111l1l_opy_):
          self.logger.info(bstack111111l_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡦࡰࡷࡱࡨࠥ࡯࡮ࠡࡽࢀ࠰ࠥࡹ࡫ࡪࡲࡳ࡭ࡳ࡭ࠠࡥࡱࡺࡲࡱࡵࡡࡥࠤὁ").format(bstack11111111l1l_opy_))
          return bstack11111111l1l_opy_
        if os.path.exists(bstack1llllllll1l1_opy_):
          self.logger.info(bstack111111l_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡻ࡫ࡳࠤ࡫ࡵࡵ࡯ࡦࠣ࡭ࡳࠦࡻࡾ࠮ࠣࡹࡳࢀࡩࡱࡲ࡬ࡲ࡬ࠨὂ").format(bstack1llllllll1l1_opy_))
          return self.bstack1llllllll11l_opy_(bstack1llllllll1l1_opy_, bstack1llllll111l1_opy_)
      self.logger.info(bstack111111l_opy_ (u"ࠤࡇࡳࡼࡴ࡬ࡰࡣࡧ࡭ࡳ࡭ࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡦࡳࡱࡰࠤࢀࢃࠢὃ").format(bstack1lllll1l1lll_opy_))
      response = bstack1l11l1ll1l_opy_(bstack111111l_opy_ (u"ࠪࡋࡊ࡚ࠧὄ"), bstack1lllll1l1lll_opy_, {}, {})
      if response.status_code == 200:
        bstack111111l1l11_opy_ = response.headers.get(bstack111111l_opy_ (u"ࠦࡊ࡚ࡡࡨࠤὅ"), bstack111111l_opy_ (u"ࠧࠨ὆"))
        if bstack111111l1l11_opy_:
          self.bstack1lllll1ll1ll_opy_(bstack1llllll11ll1_opy_, bstack111111l1l11_opy_)
        with open(bstack1llllllll1l1_opy_, bstack111111l_opy_ (u"࠭ࡷࡣࠩ὇")) as file:
          file.write(response.content)
        self.logger.info(bstack111111l_opy_ (u"ࠢࡅࡱࡺࡲࡱࡵࡡࡥࡧࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡥࡳࡪࠠࡴࡣࡹࡩࡩࠦࡡࡵࠢࡾࢁࠧὈ").format(bstack1llllllll1l1_opy_))
        return self.bstack1llllllll11l_opy_(bstack1llllllll1l1_opy_, bstack1llllll111l1_opy_)
      else:
        raise(bstack111111l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠦࡴࡩࡧࠣࡪ࡮ࡲࡥ࠯ࠢࡖࡸࡦࡺࡵࡴࠢࡦࡳࡩ࡫࠺ࠡࡽࢀࠦὉ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࡀࠠࡼࡿࠥὊ").format(e))
  def bstack1llllll11111_opy_(self, bstack1lllll1l1lll_opy_, bstack1llllll111l1_opy_):
    try:
      retry = 2
      bstack11111111l1l_opy_ = None
      bstack1llllll1l11l_opy_ = False
      while retry > 0:
        bstack11111111l1l_opy_ = self.bstack111111111l1_opy_(bstack1lllll1l1lll_opy_, bstack1llllll111l1_opy_)
        bstack1llllll1l11l_opy_ = self.bstack111111l11ll_opy_(bstack1lllll1l1lll_opy_, bstack1llllll111l1_opy_, bstack11111111l1l_opy_)
        if bstack1llllll1l11l_opy_:
          break
        retry -= 1
      return bstack11111111l1l_opy_, bstack1llllll1l11l_opy_
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡧࡦࡶࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡳࡥࡹ࡮ࠢὋ").format(e))
    return bstack11111111l1l_opy_, False
  def bstack111111l11ll_opy_(self, bstack1lllll1l1lll_opy_, bstack1llllll111l1_opy_, bstack11111111l1l_opy_, bstack1lllll1lll11_opy_ = 0):
    if bstack1lllll1lll11_opy_ > 1:
      return False
    if bstack11111111l1l_opy_ == None or os.path.exists(bstack11111111l1l_opy_) == False:
      self.logger.warn(bstack111111l_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡴࡦࡺࡨࠡࡰࡲࡸࠥ࡬࡯ࡶࡰࡧ࠰ࠥࡸࡥࡵࡴࡼ࡭ࡳ࡭ࠠࡥࡱࡺࡲࡱࡵࡡࡥࠤὌ"))
      return False
    bstack1lllll1lll1l_opy_ = bstack111111l_opy_ (u"ࡷࠨ࡞࠯ࠬࡃࡴࡪࡸࡣࡺ࠱ࡦࡰ࡮ࠦ࡜ࡥ࠭࡟࠲ࡡࡪࠫ࡝࠰࡟ࡨ࠰ࠨὍ")
    command = bstack111111l_opy_ (u"࠭ࡻࡾࠢ࠰࠱ࡻ࡫ࡲࡴ࡫ࡲࡲࠬ὎").format(bstack11111111l1l_opy_)
    bstack1lllllll111l_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lllll1lll1l_opy_, bstack1lllllll111l_opy_) != None:
      return True
    else:
      self.logger.error(bstack111111l_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡶࡦࡴࡶ࡭ࡴࡴࠠࡤࡪࡨࡧࡰࠦࡦࡢ࡫࡯ࡩࡩࠨ὏"))
      return False
  def bstack1llllllll11l_opy_(self, bstack1llllllll1l1_opy_, bstack1llllll111l1_opy_):
    try:
      working_dir = os.path.dirname(bstack1llllllll1l1_opy_)
      shutil.unpack_archive(bstack1llllllll1l1_opy_, working_dir)
      bstack11111111l1l_opy_ = os.path.join(working_dir, bstack1llllll111l1_opy_)
      os.chmod(bstack11111111l1l_opy_, 0o755)
      return bstack11111111l1l_opy_
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡺࡴࡺࡪࡲࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠤὐ"))
  def bstack1lllll1ll11l_opy_(self):
    try:
      bstack1llllll1l1ll_opy_ = self.config.get(bstack111111l_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨὑ"))
      bstack1lllll1ll11l_opy_ = bstack1llllll1l1ll_opy_ or (bstack1llllll1l1ll_opy_ is None and self.bstack11l11lll1l_opy_)
      if not bstack1lllll1ll11l_opy_ or self.config.get(bstack111111l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ὒ"), None) not in bstack11l1l1lll11_opy_:
        return False
      self.bstack11l11l111l_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡥࡧࡷࡩࡨࡺࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨὓ").format(e))
  def bstack1lllllllll1l_opy_(self):
    try:
      bstack1lllllllll1l_opy_ = self.percy_capture_mode
      return bstack1lllllllll1l_opy_
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡦࡨࡸࡪࡩࡴࠡࡲࡨࡶࡨࡿࠠࡤࡣࡳࡸࡺࡸࡥࠡ࡯ࡲࡨࡪ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨὔ").format(e))
  def init(self, bstack11l11lll1l_opy_, config, logger):
    self.bstack11l11lll1l_opy_ = bstack11l11lll1l_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllll1ll11l_opy_():
      return
    self.bstack1111111ll1l_opy_ = config.get(bstack111111l_opy_ (u"࠭ࡰࡦࡴࡦࡽࡔࡶࡴࡪࡱࡱࡷࠬὕ"), {})
    self.percy_capture_mode = config.get(bstack111111l_opy_ (u"ࠧࡱࡧࡵࡧࡾࡉࡡࡱࡶࡸࡶࡪࡓ࡯ࡥࡧࠪὖ"))
    try:
      bstack1lllll1l1lll_opy_, bstack1llllll111l1_opy_ = self.bstack1111111ll11_opy_()
      self.bstack1111ll1l111_opy_ = bstack1llllll111l1_opy_
      bstack11111111l1l_opy_, bstack1llllll1l11l_opy_ = self.bstack1llllll11111_opy_(bstack1lllll1l1lll_opy_, bstack1llllll111l1_opy_)
      if bstack1llllll1l11l_opy_:
        self.binary_path = bstack11111111l1l_opy_
        thread = Thread(target=self.bstack111111l1lll_opy_)
        thread.start()
      else:
        self.bstack111111l1111_opy_ = True
        self.logger.error(bstack111111l_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡳࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦࡦࡰࡷࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤ࡚ࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡐࡦࡴࡦࡽࠧὗ").format(bstack11111111l1l_opy_))
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥ὘").format(e))
  def bstack1111111l11l_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack111111l_opy_ (u"ࠪࡰࡴ࡭ࠧὙ"), bstack111111l_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡰࡴ࡭ࠧ὚"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack111111l_opy_ (u"ࠧࡖࡵࡴࡪ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࡵࠣࡥࡹࠦࡻࡾࠤὛ").format(logfile))
      self.bstack1llllll11l11_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࠢࡳࡥࡹ࡮ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢ὜").format(e))
  @measure(event_name=EVENTS.bstack11l1l1l1lll_opy_, stage=STAGE.bstack11l11ll11_opy_)
  def bstack111111l1lll_opy_(self):
    bstack111111ll111_opy_ = self.bstack1llllll1ll1l_opy_()
    if bstack111111ll111_opy_ == None:
      self.bstack111111l1111_opy_ = True
      self.logger.error(bstack111111l_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻࠥὝ"))
      return False
    bstack1111111l1ll_opy_ = [bstack111111l_opy_ (u"ࠣࡣࡳࡴ࠿࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠤ὞") if self.bstack11l11lll1l_opy_ else bstack111111l_opy_ (u"ࠩࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹ࠭Ὗ")]
    bstack11111ll1l1l_opy_ = self.bstack1llllll1l111_opy_()
    if bstack11111ll1l1l_opy_ != None:
      bstack1111111l1ll_opy_.append(bstack111111l_opy_ (u"ࠥ࠱ࡨࠦࡻࡾࠤὠ").format(bstack11111ll1l1l_opy_))
    env = os.environ.copy()
    env[bstack111111l_opy_ (u"ࠦࡕࡋࡒࡄ࡛ࡢࡘࡔࡑࡅࡏࠤὡ")] = bstack111111ll111_opy_
    env[bstack111111l_opy_ (u"࡚ࠧࡈࡠࡄࡘࡍࡑࡊ࡟ࡖࡗࡌࡈࠧὢ")] = os.environ.get(bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫὣ"), bstack111111l_opy_ (u"ࠧࠨὤ"))
    bstack1lllllll1l11_opy_ = [self.binary_path]
    self.bstack1111111l11l_opy_()
    self.bstack1llllll11lll_opy_ = self.bstack1lllll1ll1l1_opy_(bstack1lllllll1l11_opy_ + bstack1111111l1ll_opy_, env)
    self.logger.debug(bstack111111l_opy_ (u"ࠣࡕࡷࡥࡷࡺࡩ࡯ࡩࠣࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠤὥ"))
    bstack1lllll1lll11_opy_ = 0
    while self.bstack1llllll11lll_opy_.poll() == None:
      bstack1lllllll11l1_opy_ = self.bstack1lllllll1l1l_opy_()
      if bstack1lllllll11l1_opy_:
        self.logger.debug(bstack111111l_opy_ (u"ࠤࡋࡩࡦࡲࡴࡩࠢࡆ࡬ࡪࡩ࡫ࠡࡵࡸࡧࡨ࡫ࡳࡴࡨࡸࡰࠧὦ"))
        self.bstack1lllllll1ll1_opy_ = True
        return True
      bstack1lllll1lll11_opy_ += 1
      self.logger.debug(bstack111111l_opy_ (u"ࠥࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡕࡩࡹࡸࡹࠡ࠯ࠣࡿࢂࠨὧ").format(bstack1lllll1lll11_opy_))
      time.sleep(2)
    self.logger.error(bstack111111l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡰࡦࡴࡦࡽ࠱ࠦࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡌࡡࡪ࡮ࡨࡨࠥࡧࡦࡵࡧࡵࠤࢀࢃࠠࡢࡶࡷࡩࡲࡶࡴࡴࠤὨ").format(bstack1lllll1lll11_opy_))
    self.bstack111111l1111_opy_ = True
    return False
  def bstack1lllllll1l1l_opy_(self, bstack1lllll1lll11_opy_ = 0):
    if bstack1lllll1lll11_opy_ > 10:
      return False
    try:
      bstack111111l1ll1_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠬࡖࡅࡓࡅ࡜ࡣࡘࡋࡒࡗࡇࡕࡣࡆࡊࡄࡓࡇࡖࡗࠬὩ"), bstack111111l_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵࡬ࡰࡥࡤࡰ࡭ࡵࡳࡵ࠼࠸࠷࠸࠾ࠧὪ"))
      bstack1lllllllllll_opy_ = bstack111111l1ll1_opy_ + bstack11l1l11l1l1_opy_
      response = requests.get(bstack1lllllllllll_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack111111l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩ࠭Ὣ"), {}).get(bstack111111l_opy_ (u"ࠨ࡫ࡧࠫὬ"), None)
      return True
    except:
      self.logger.debug(bstack111111l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡱࡦࡧࡺࡸࡲࡦࡦࠣࡻ࡭࡯࡬ࡦࠢࡳࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡨࡦࡣ࡯ࡸ࡭ࠦࡣࡩࡧࡦ࡯ࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢὭ"))
      return False
  def bstack1llllll1ll1l_opy_(self):
    bstack111111111ll_opy_ = bstack111111l_opy_ (u"ࠪࡥࡵࡶࠧὮ") if self.bstack11l11lll1l_opy_ else bstack111111l_opy_ (u"ࠫࡦࡻࡴࡰ࡯ࡤࡸࡪ࠭Ὧ")
    bstack1111111l1l1_opy_ = bstack111111l_opy_ (u"ࠧࡻ࡮ࡥࡧࡩ࡭ࡳ࡫ࡤࠣὰ") if self.config.get(bstack111111l_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬά")) is None else True
    bstack11ll11ll111_opy_ = bstack111111l_opy_ (u"ࠢࡢࡲ࡬࠳ࡦࡶࡰࡠࡲࡨࡶࡨࡿ࠯ࡨࡧࡷࡣࡵࡸ࡯࡫ࡧࡦࡸࡤࡺ࡯࡬ࡧࡱࡃࡳࡧ࡭ࡦ࠿ࡾࢁࠫࡺࡹࡱࡧࡀࡿࢂࠬࡰࡦࡴࡦࡽࡂࢁࡽࠣὲ").format(self.config[bstack111111l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭έ")], bstack111111111ll_opy_, bstack1111111l1l1_opy_)
    if self.percy_capture_mode:
      bstack11ll11ll111_opy_ += bstack111111l_opy_ (u"ࠤࠩࡴࡪࡸࡣࡺࡡࡦࡥࡵࡺࡵࡳࡧࡢࡱࡴࡪࡥ࠾ࡽࢀࠦὴ").format(self.percy_capture_mode)
    uri = bstack11ll11l11_opy_(bstack11ll11ll111_opy_)
    try:
      response = bstack1l11l1ll1l_opy_(bstack111111l_opy_ (u"ࠪࡋࡊ࡚ࠧή"), uri, {}, {bstack111111l_opy_ (u"ࠫࡦࡻࡴࡩࠩὶ"): (self.config[bstack111111l_opy_ (u"ࠬࡻࡳࡦࡴࡑࡥࡲ࡫ࠧί")], self.config[bstack111111l_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸࡑࡥࡺࠩὸ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack11l11l111l_opy_ = data.get(bstack111111l_opy_ (u"ࠧࡴࡷࡦࡧࡪࡹࡳࠨό"))
        self.percy_capture_mode = data.get(bstack111111l_opy_ (u"ࠨࡲࡨࡶࡨࡿ࡟ࡤࡣࡳࡸࡺࡸࡥࡠ࡯ࡲࡨࡪ࠭ὺ"))
        os.environ[bstack111111l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒࡈࡖࡈ࡟ࠧύ")] = str(self.bstack11l11l111l_opy_)
        os.environ[bstack111111l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࡠࡅࡄࡔ࡙࡛ࡒࡆࡡࡐࡓࡉࡋࠧὼ")] = str(self.percy_capture_mode)
        if bstack1111111l1l1_opy_ == bstack111111l_opy_ (u"ࠦࡺࡴࡤࡦࡨ࡬ࡲࡪࡪࠢώ") and str(self.bstack11l11l111l_opy_).lower() == bstack111111l_opy_ (u"ࠧࡺࡲࡶࡧࠥ὾"):
          self.bstack1l1l111ll_opy_ = True
        if bstack111111l_opy_ (u"ࠨࡴࡰ࡭ࡨࡲࠧ὿") in data:
          return data[bstack111111l_opy_ (u"ࠢࡵࡱ࡮ࡩࡳࠨᾀ")]
        else:
          raise bstack111111l_opy_ (u"ࠨࡖࡲ࡯ࡪࡴࠠࡏࡱࡷࠤࡋࡵࡵ࡯ࡦࠣ࠱ࠥࢁࡽࠨᾁ").format(data)
      else:
        raise bstack111111l_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡵ࡫ࡲࡤࡻࠣࡸࡴࡱࡥ࡯࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥࡹࡴࡢࡶࡸࡷࠥ࠳ࠠࡼࡿ࠯ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡂࡰࡦࡼࠤ࠲ࠦࡻࡾࠤᾂ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡴࡷࡵࡪࡦࡥࡷࠦᾃ").format(e))
  def bstack1llllll1l111_opy_(self):
    bstack1111111l111_opy_ = os.path.join(tempfile.gettempdir(), bstack111111l_opy_ (u"ࠦࡵ࡫ࡲࡤࡻࡆࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠢᾄ"))
    try:
      if bstack111111l_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ᾅ") not in self.bstack1111111ll1l_opy_:
        self.bstack1111111ll1l_opy_[bstack111111l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧᾆ")] = 2
      with open(bstack1111111l111_opy_, bstack111111l_opy_ (u"ࠧࡸࠩᾇ")) as fp:
        json.dump(self.bstack1111111ll1l_opy_, fp)
      return bstack1111111l111_opy_
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡨࡸࡥࡢࡶࡨࠤࡵ࡫ࡲࡤࡻࠣࡧࡴࡴࡦ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᾈ").format(e))
  def bstack1lllll1ll1l1_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1lllllll1111_opy_ == bstack111111l_opy_ (u"ࠩࡺ࡭ࡳ࠭ᾉ"):
        bstack1lllllll1lll_opy_ = [bstack111111l_opy_ (u"ࠪࡧࡲࡪ࠮ࡦࡺࡨࠫᾊ"), bstack111111l_opy_ (u"ࠫ࠴ࡩࠧᾋ")]
        cmd = bstack1lllllll1lll_opy_ + cmd
      cmd = bstack111111l_opy_ (u"ࠬࠦࠧᾌ").join(cmd)
      self.logger.debug(bstack111111l_opy_ (u"ࠨࡒࡶࡰࡱ࡭ࡳ࡭ࠠࡼࡿࠥᾍ").format(cmd))
      with open(self.bstack1llllll11l11_opy_, bstack111111l_opy_ (u"ࠢࡢࠤᾎ")) as bstack111111l11l1_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack111111l11l1_opy_, text=True, stderr=bstack111111l11l1_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack111111l1111_opy_ = True
      self.logger.error(bstack111111l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺࠢࡺ࡭ࡹ࡮ࠠࡤ࡯ࡧࠤ࠲ࠦࡻࡾ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᾏ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1lllllll1ll1_opy_:
        self.logger.info(bstack111111l_opy_ (u"ࠤࡖࡸࡴࡶࡰࡪࡰࡪࠤࡕ࡫ࡲࡤࡻࠥᾐ"))
        cmd = [self.binary_path, bstack111111l_opy_ (u"ࠥࡩࡽ࡫ࡣ࠻ࡵࡷࡳࡵࠨᾑ")]
        self.bstack1lllll1ll1l1_opy_(cmd)
        self.bstack1lllllll1ll1_opy_ = False
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡲࡴࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡨࡵ࡭࡮ࡣࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦᾒ").format(cmd, e))
  def bstack111l11l1l_opy_(self):
    if not self.bstack11l11l111l_opy_:
      return
    try:
      bstack1llllll1l1l1_opy_ = 0
      while not self.bstack1lllllll1ll1_opy_ and bstack1llllll1l1l1_opy_ < self.bstack111111l1l1l_opy_:
        if self.bstack111111l1111_opy_:
          self.logger.info(bstack111111l_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡸ࡫ࡴࡶࡲࠣࡪࡦ࡯࡬ࡦࡦࠥᾓ"))
          return
        time.sleep(1)
        bstack1llllll1l1l1_opy_ += 1
      os.environ[bstack111111l_opy_ (u"࠭ࡐࡆࡔࡆ࡝ࡤࡈࡅࡔࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࠬᾔ")] = str(self.bstack1lllll1lllll_opy_())
      self.logger.info(bstack111111l_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡳࡦࡶࡸࡴࠥࡩ࡯࡮ࡲ࡯ࡩࡹ࡫ࡤࠣᾕ"))
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸ࡫ࡴࡶࡲࠣࡴࡪࡸࡣࡺ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡻࡾࠤᾖ").format(e))
  def bstack1lllll1lllll_opy_(self):
    if self.bstack11l11lll1l_opy_:
      return
    try:
      bstack1llllll1lll1_opy_ = [platform[bstack111111l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧᾗ")].lower() for platform in self.config.get(bstack111111l_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ᾘ"), [])]
      bstack1llllll11l1l_opy_ = sys.maxsize
      bstack1llllllllll1_opy_ = bstack111111l_opy_ (u"ࠫࠬᾙ")
      for browser in bstack1llllll1lll1_opy_:
        if browser in self.bstack1lllll1llll1_opy_:
          bstack1llllll111ll_opy_ = self.bstack1lllll1llll1_opy_[browser]
        if bstack1llllll111ll_opy_ < bstack1llllll11l1l_opy_:
          bstack1llllll11l1l_opy_ = bstack1llllll111ll_opy_
          bstack1llllllllll1_opy_ = browser
      return bstack1llllllllll1_opy_
    except Exception as e:
      self.logger.error(bstack111111l_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨ࡬ࡲࡩࠦࡢࡦࡵࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᾚ").format(e))
  @classmethod
  def bstack1111l1111_opy_(self):
    return os.getenv(bstack111111l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫᾛ"), bstack111111l_opy_ (u"ࠧࡇࡣ࡯ࡷࡪ࠭ᾜ")).lower()
  @classmethod
  def bstack111lll1l11_opy_(self):
    return os.getenv(bstack111111l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡑࡇࡕࡇ࡞ࡥࡃࡂࡒࡗ࡙ࡗࡋ࡟ࡎࡑࡇࡉࠬᾝ"), bstack111111l_opy_ (u"ࠩࠪᾞ"))
  @classmethod
  def bstack11llllll1ll_opy_(cls, value):
    cls.bstack1l1l111ll_opy_ = value
  @classmethod
  def bstack1llllll1111l_opy_(cls):
    return cls.bstack1l1l111ll_opy_
  @classmethod
  def bstack11llllll11l_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack11111111l11_opy_(cls):
    return cls.percy_build_id