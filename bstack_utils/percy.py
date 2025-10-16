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
from bstack_utils.helper import bstack1l1111111_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11111ll1l_opy_ import bstack1lll1ll11l_opy_
class bstack1ll1l1ll1l_opy_:
  working_dir = os.getcwd()
  bstack11ll111ll_opy_ = False
  config = {}
  bstack1111llllll1_opy_ = bstack1lllll1_opy_ (u"ࠩࠪἧ")
  binary_path = bstack1lllll1_opy_ (u"ࠪࠫἨ")
  bstack1llllll11ll1_opy_ = bstack1lllll1_opy_ (u"ࠫࠬἩ")
  bstack11l1l11ll_opy_ = False
  bstack1111111l111_opy_ = None
  bstack111111111l1_opy_ = {}
  bstack1lllllll111l_opy_ = 300
  bstack1llllll1ll11_opy_ = False
  logger = None
  bstack1lllll1ll1l1_opy_ = False
  bstack11l1l11lll_opy_ = False
  percy_build_id = None
  bstack1llllll11l11_opy_ = bstack1lllll1_opy_ (u"ࠬ࠭Ἢ")
  bstack1llllll1l1ll_opy_ = {
    bstack1lllll1_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭Ἣ") : 1,
    bstack1lllll1_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨἬ") : 2,
    bstack1lllll1_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭Ἥ") : 3,
    bstack1lllll1_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩἮ") : 4
  }
  def __init__(self) -> None: pass
  def bstack111111l1l1l_opy_(self):
    bstack11111111111_opy_ = bstack1lllll1_opy_ (u"ࠪࠫἯ")
    bstack1lllllllllll_opy_ = sys.platform
    bstack11111111l11_opy_ = bstack1lllll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪἰ")
    if re.match(bstack1lllll1_opy_ (u"ࠧࡪࡡࡳࡹ࡬ࡲࢁࡳࡡࡤࠢࡲࡷࠧἱ"), bstack1lllllllllll_opy_) != None:
      bstack11111111111_opy_ = bstack11l1l11l11l_opy_ + bstack1lllll1_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡯ࡴࡺ࠱ࡾ࡮ࡶࠢἲ")
      self.bstack1llllll11l11_opy_ = bstack1lllll1_opy_ (u"ࠧ࡮ࡣࡦࠫἳ")
    elif re.match(bstack1lllll1_opy_ (u"ࠣ࡯ࡶࡻ࡮ࡴࡼ࡮ࡵࡼࡷࢁࡳࡩ࡯ࡩࡺࢀࡨࡿࡧࡸ࡫ࡱࢀࡧࡩࡣࡸ࡫ࡱࢀࡼ࡯࡮ࡤࡧࡿࡩࡲࡩࡼࡸ࡫ࡱ࠷࠷ࠨἴ"), bstack1lllllllllll_opy_) != None:
      bstack11111111111_opy_ = bstack11l1l11l11l_opy_ + bstack1lllll1_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯ࡺ࡭ࡳ࠴ࡺࡪࡲࠥἵ")
      bstack11111111l11_opy_ = bstack1lllll1_opy_ (u"ࠥࡴࡪࡸࡣࡺ࠰ࡨࡼࡪࠨἶ")
      self.bstack1llllll11l11_opy_ = bstack1lllll1_opy_ (u"ࠫࡼ࡯࡮ࠨἷ")
    else:
      bstack11111111111_opy_ = bstack11l1l11l11l_opy_ + bstack1lllll1_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡲࡩ࡯ࡷࡻ࠲ࡿ࡯ࡰࠣἸ")
      self.bstack1llllll11l11_opy_ = bstack1lllll1_opy_ (u"࠭࡬ࡪࡰࡸࡼࠬἹ")
    return bstack11111111111_opy_, bstack11111111l11_opy_
  def bstack111111l1ll1_opy_(self):
    try:
      bstack1llllll1llll_opy_ = [os.path.join(expanduser(bstack1lllll1_opy_ (u"ࠢࡿࠤἺ")), bstack1lllll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨἻ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1llllll1llll_opy_:
        if(self.bstack1llllllll11l_opy_(path)):
          return path
      raise bstack1lllll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨἼ")
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡪࡰࡧࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡹࠡࡦࡲࡻࡳࡲ࡯ࡢࡦ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠ࠮ࠢࡾࢁࠧἽ").format(e))
  def bstack1llllllll11l_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1111111lll1_opy_(self, bstack1lllll1llll1_opy_):
    return os.path.join(bstack1lllll1llll1_opy_, self.bstack1111llllll1_opy_ + bstack1lllll1_opy_ (u"ࠦ࠳࡫ࡴࡢࡩࠥἾ"))
  def bstack1lllllll11l1_opy_(self, bstack1lllll1llll1_opy_, bstack1llllll1ll1l_opy_):
    if not bstack1llllll1ll1l_opy_: return
    try:
      bstack111111l1l11_opy_ = self.bstack1111111lll1_opy_(bstack1lllll1llll1_opy_)
      with open(bstack111111l1l11_opy_, bstack1lllll1_opy_ (u"ࠧࡽࠢἿ")) as f:
        f.write(bstack1llllll1ll1l_opy_)
        self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡓࡢࡸࡨࡨࠥࡴࡥࡸࠢࡈࡘࡦ࡭ࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡻࠥὀ"))
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡦࡼࡥࠡࡶ࡫ࡩࠥ࡫ࡴࡢࡩ࠯ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢὁ").format(e))
  def bstack1lllll1lllll_opy_(self, bstack1lllll1llll1_opy_):
    try:
      bstack111111l1l11_opy_ = self.bstack1111111lll1_opy_(bstack1lllll1llll1_opy_)
      if os.path.exists(bstack111111l1l11_opy_):
        with open(bstack111111l1l11_opy_, bstack1lllll1_opy_ (u"ࠣࡴࠥὂ")) as f:
          bstack1llllll1ll1l_opy_ = f.read().strip()
          return bstack1llllll1ll1l_opy_ if bstack1llllll1ll1l_opy_ else None
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡉ࡙ࡧࡧ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧὃ").format(e))
  def bstack1llllll111ll_opy_(self, bstack1lllll1llll1_opy_, bstack11111111111_opy_):
    bstack1llllll11111_opy_ = self.bstack1lllll1lllll_opy_(bstack1lllll1llll1_opy_)
    if bstack1llllll11111_opy_:
      try:
        bstack1llllllllll1_opy_ = self.bstack1lllllll1l1l_opy_(bstack1llllll11111_opy_, bstack11111111111_opy_)
        if not bstack1llllllllll1_opy_:
          self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢ࡬ࡷࠥࡻࡰࠡࡶࡲࠤࡩࡧࡴࡦࠢࠫࡉ࡙ࡧࡧࠡࡷࡱࡧ࡭ࡧ࡮ࡨࡧࡧ࠭ࠧὄ"))
          return True
        self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡓ࡫ࡷࠡࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡹࡵࡪࡡࡵࡧࠥὅ"))
        return False
      except Exception as e:
        self.logger.warn(bstack1lllll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡥ࡫ࡩࡨࡱࠠࡧࡱࡵࠤࡧ࡯࡮ࡢࡴࡼࠤࡺࡶࡤࡢࡶࡨࡷ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥ࡫ࡸࡪࡵࡷ࡭ࡳ࡭ࠠࡣ࡫ࡱࡥࡷࡿ࠺ࠡࡽࢀࠦ὆").format(e))
    return False
  def bstack1lllllll1l1l_opy_(self, bstack1llllll11111_opy_, bstack11111111111_opy_):
    try:
      headers = {
        bstack1lllll1_opy_ (u"ࠨࡉࡧ࠯ࡑࡳࡳ࡫࠭ࡎࡣࡷࡧ࡭ࠨ὇"): bstack1llllll11111_opy_
      }
      response = bstack1l1111111_opy_(bstack1lllll1_opy_ (u"ࠧࡈࡇࡗࠫὈ"), bstack11111111111_opy_, {}, {bstack1lllll1_opy_ (u"ࠣࡪࡨࡥࡩ࡫ࡲࡴࠤὉ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack1lllll1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡥ࡫ࡩࡨࡱࡩ࡯ࡩࠣࡪࡴࡸࠠࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡵࡱࡦࡤࡸࡪࡹ࠺ࠡࡽࢀࠦὊ").format(e))
  @measure(event_name=EVENTS.bstack11l1l11111l_opy_, stage=STAGE.bstack11l1l111l1_opy_)
  def bstack1111111l11l_opy_(self, bstack11111111111_opy_, bstack11111111l11_opy_):
    try:
      bstack1111111ll11_opy_ = self.bstack111111l1ll1_opy_()
      bstack1llllll1l11l_opy_ = os.path.join(bstack1111111ll11_opy_, bstack1lllll1_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰ࡽ࡭ࡵ࠭Ὃ"))
      bstack1llllll11lll_opy_ = os.path.join(bstack1111111ll11_opy_, bstack11111111l11_opy_)
      if self.bstack1llllll111ll_opy_(bstack1111111ll11_opy_, bstack11111111111_opy_): # if bstack111111ll11l_opy_, bstack1llllll1111_opy_ bstack1llllll1ll1l_opy_ is bstack1llllll111l1_opy_ to bstack111l1lll11l_opy_ version available (response 304)
        if os.path.exists(bstack1llllll11lll_opy_):
          self.logger.info(bstack1lllll1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࢁࡽ࠭ࠢࡶ࡯࡮ࡶࡰࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨὌ").format(bstack1llllll11lll_opy_))
          return bstack1llllll11lll_opy_
        if os.path.exists(bstack1llllll1l11l_opy_):
          self.logger.info(bstack1lllll1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡿ࡯ࡰࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡶࡰࡽ࡭ࡵࡶࡩ࡯ࡩࠥὍ").format(bstack1llllll1l11l_opy_))
          return self.bstack1llllllll1l1_opy_(bstack1llllll1l11l_opy_, bstack11111111l11_opy_)
      self.logger.info(bstack1lllll1_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭ࠡࡽࢀࠦ὎").format(bstack11111111111_opy_))
      response = bstack1l1111111_opy_(bstack1lllll1_opy_ (u"ࠧࡈࡇࡗࠫ὏"), bstack11111111111_opy_, {}, {})
      if response.status_code == 200:
        bstack11111111l1l_opy_ = response.headers.get(bstack1lllll1_opy_ (u"ࠣࡇࡗࡥ࡬ࠨὐ"), bstack1lllll1_opy_ (u"ࠤࠥὑ"))
        if bstack11111111l1l_opy_:
          self.bstack1lllllll11l1_opy_(bstack1111111ll11_opy_, bstack11111111l1l_opy_)
        with open(bstack1llllll1l11l_opy_, bstack1lllll1_opy_ (u"ࠪࡻࡧ࠭ὒ")) as file:
          file.write(response.content)
        self.logger.info(bstack1lllll1_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡢࡰࡧࠤࡸࡧࡶࡦࡦࠣࡥࡹࠦࡻࡾࠤὓ").format(bstack1llllll1l11l_opy_))
        return self.bstack1llllllll1l1_opy_(bstack1llllll1l11l_opy_, bstack11111111l11_opy_)
      else:
        raise(bstack1lllll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡸ࡭࡫ࠠࡧ࡫࡯ࡩ࠳ࠦࡓࡵࡣࡷࡹࡸࠦࡣࡰࡦࡨ࠾ࠥࢁࡽࠣὔ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻ࠽ࠤࢀࢃࠢὕ").format(e))
  def bstack1lllll1ll11l_opy_(self, bstack11111111111_opy_, bstack11111111l11_opy_):
    try:
      retry = 2
      bstack1llllll11lll_opy_ = None
      bstack111111l1111_opy_ = False
      while retry > 0:
        bstack1llllll11lll_opy_ = self.bstack1111111l11l_opy_(bstack11111111111_opy_, bstack11111111l11_opy_)
        bstack111111l1111_opy_ = self.bstack1llllll11l1l_opy_(bstack11111111111_opy_, bstack11111111l11_opy_, bstack1llllll11lll_opy_)
        if bstack111111l1111_opy_:
          break
        retry -= 1
      return bstack1llllll11lll_opy_, bstack111111l1111_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡺࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡰࡢࡶ࡫ࠦὖ").format(e))
    return bstack1llllll11lll_opy_, False
  def bstack1llllll11l1l_opy_(self, bstack11111111111_opy_, bstack11111111l11_opy_, bstack1llllll11lll_opy_, bstack1llllllll1ll_opy_ = 0):
    if bstack1llllllll1ll_opy_ > 1:
      return False
    if bstack1llllll11lll_opy_ == None or os.path.exists(bstack1llllll11lll_opy_) == False:
      self.logger.warn(bstack1lllll1_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡱࡣࡷ࡬ࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡵࡩࡹࡸࡹࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨὗ"))
      return False
    bstack1lllll1ll111_opy_ = bstack1lllll1_opy_ (u"ࡴࠥࡢ࠳࠰ࡀࡱࡧࡵࡧࡾ࠵ࡣ࡭࡫ࠣࡠࡩ࠱࡜࠯࡞ࡧ࠯ࡡ࠴࡜ࡥ࠭ࠥ὘")
    command = bstack1lllll1_opy_ (u"ࠪࡿࢂࠦ࠭࠮ࡸࡨࡶࡸ࡯࡯࡯ࠩὙ").format(bstack1llllll11lll_opy_)
    bstack1lllllll1lll_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lllll1ll111_opy_, bstack1lllllll1lll_opy_) != None:
      return True
    else:
      self.logger.error(bstack1lllll1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡺࡪࡸࡳࡪࡱࡱࠤࡨ࡮ࡥࡤ࡭ࠣࡪࡦ࡯࡬ࡦࡦࠥ὚"))
      return False
  def bstack1llllllll1l1_opy_(self, bstack1llllll1l11l_opy_, bstack11111111l11_opy_):
    try:
      working_dir = os.path.dirname(bstack1llllll1l11l_opy_)
      shutil.unpack_archive(bstack1llllll1l11l_opy_, working_dir)
      bstack1llllll11lll_opy_ = os.path.join(working_dir, bstack11111111l11_opy_)
      os.chmod(bstack1llllll11lll_opy_, 0o755)
      return bstack1llllll11lll_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡷࡱࡾ࡮ࡶࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨὛ"))
  def bstack1lllllll1l11_opy_(self):
    try:
      bstack1lllllllll1l_opy_ = self.config.get(bstack1lllll1_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬ὜"))
      bstack1lllllll1l11_opy_ = bstack1lllllllll1l_opy_ or (bstack1lllllllll1l_opy_ is None and self.bstack11ll111ll_opy_)
      if not bstack1lllllll1l11_opy_ or self.config.get(bstack1lllll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪὝ"), None) not in bstack11l1l1lll1l_opy_:
        return False
      self.bstack11l1l11ll_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥ὞").format(e))
  def bstack1llllll1l1l1_opy_(self):
    try:
      bstack1llllll1l1l1_opy_ = self.percy_capture_mode
      return bstack1llllll1l1l1_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼࠤࡨࡧࡰࡵࡷࡵࡩࠥࡳ࡯ࡥࡧ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥὟ").format(e))
  def init(self, bstack11ll111ll_opy_, config, logger):
    self.bstack11ll111ll_opy_ = bstack11ll111ll_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1lllllll1l11_opy_():
      return
    self.bstack111111111l1_opy_ = config.get(bstack1lllll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩὠ"), {})
    self.percy_capture_mode = config.get(bstack1lllll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧὡ"))
    try:
      bstack11111111111_opy_, bstack11111111l11_opy_ = self.bstack111111l1l1l_opy_()
      self.bstack1111llllll1_opy_ = bstack11111111l11_opy_
      bstack1llllll11lll_opy_, bstack111111l1111_opy_ = self.bstack1lllll1ll11l_opy_(bstack11111111111_opy_, bstack11111111l11_opy_)
      if bstack111111l1111_opy_:
        self.binary_path = bstack1llllll11lll_opy_
        thread = Thread(target=self.bstack111111ll1l1_opy_)
        thread.start()
      else:
        self.bstack1lllll1ll1l1_opy_ = True
        self.logger.error(bstack1lllll1_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡰࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡪࡴࡻ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡔࡪࡸࡣࡺࠤὢ").format(bstack1llllll11lll_opy_))
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢὣ").format(e))
  def bstack1lllll1ll1ll_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack1lllll1_opy_ (u"ࠧ࡭ࡱࡪࠫὤ"), bstack1lllll1_opy_ (u"ࠨࡲࡨࡶࡨࡿ࠮࡭ࡱࡪࠫὥ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack1lllll1_opy_ (u"ࠤࡓࡹࡸ࡮ࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢ࡯ࡳ࡬ࡹࠠࡢࡶࠣࡿࢂࠨὦ").format(logfile))
      self.bstack1llllll11ll1_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡦࡶࠣࡴࡪࡸࡣࡺࠢ࡯ࡳ࡬ࠦࡰࡢࡶ࡫࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦὧ").format(e))
  @measure(event_name=EVENTS.bstack11l1l11l111_opy_, stage=STAGE.bstack11l1l111l1_opy_)
  def bstack111111ll1l1_opy_(self):
    bstack1111111111l_opy_ = self.bstack11111111lll_opy_()
    if bstack1111111111l_opy_ == None:
      self.bstack1lllll1ll1l1_opy_ = True
      self.logger.error(bstack1lllll1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡸࡴࡱࡥ࡯ࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠱ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠢὨ"))
      return False
    bstack1lllll1lll1l_opy_ = [bstack1lllll1_opy_ (u"ࠧࡧࡰࡱ࠼ࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹࠨὩ") if self.bstack11ll111ll_opy_ else bstack1lllll1_opy_ (u"࠭ࡥࡹࡧࡦ࠾ࡸࡺࡡࡳࡶࠪὪ")]
    bstack11111lll1l1_opy_ = self.bstack111111ll111_opy_()
    if bstack11111lll1l1_opy_ != None:
      bstack1lllll1lll1l_opy_.append(bstack1lllll1_opy_ (u"ࠢ࠮ࡥࠣࡿࢂࠨὫ").format(bstack11111lll1l1_opy_))
    env = os.environ.copy()
    env[bstack1lllll1_opy_ (u"ࠣࡒࡈࡖࡈ࡟࡟ࡕࡑࡎࡉࡓࠨὬ")] = bstack1111111111l_opy_
    env[bstack1lllll1_opy_ (u"ࠤࡗࡌࡤࡈࡕࡊࡎࡇࡣ࡚࡛ࡉࡅࠤὭ")] = os.environ.get(bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨὮ"), bstack1lllll1_opy_ (u"ࠫࠬὯ"))
    bstack1llllllll111_opy_ = [self.binary_path]
    self.bstack1lllll1ll1ll_opy_()
    self.bstack1111111l111_opy_ = self.bstack1lllllll1ll1_opy_(bstack1llllllll111_opy_ + bstack1lllll1lll1l_opy_, env)
    self.logger.debug(bstack1lllll1_opy_ (u"࡙ࠧࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠨὰ"))
    bstack1llllllll1ll_opy_ = 0
    while self.bstack1111111l111_opy_.poll() == None:
      bstack1llllll1l111_opy_ = self.bstack1111111l1ll_opy_()
      if bstack1llllll1l111_opy_:
        self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠤά"))
        self.bstack1llllll1ll11_opy_ = True
        return True
      bstack1llllllll1ll_opy_ += 1
      self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡒࡦࡶࡵࡽࠥ࠳ࠠࡼࡿࠥὲ").format(bstack1llllllll1ll_opy_))
      time.sleep(2)
    self.logger.error(bstack1lllll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡉࡥ࡮ࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡽࢀࠤࡦࡺࡴࡦ࡯ࡳࡸࡸࠨέ").format(bstack1llllllll1ll_opy_))
    self.bstack1lllll1ll1l1_opy_ = True
    return False
  def bstack1111111l1ll_opy_(self, bstack1llllllll1ll_opy_ = 0):
    if bstack1llllllll1ll_opy_ > 10:
      return False
    try:
      bstack111111l111l_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡕࡈࡖ࡛ࡋࡒࡠࡃࡇࡈࡗࡋࡓࡔࠩὴ"), bstack1lllll1_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡰࡴࡩࡡ࡭ࡪࡲࡷࡹࡀ࠵࠴࠵࠻ࠫή"))
      bstack1lllllllll11_opy_ = bstack111111l111l_opy_ + bstack11l11llll1l_opy_
      response = requests.get(bstack1lllllllll11_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack1lllll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࠪὶ"), {}).get(bstack1lllll1_opy_ (u"ࠬ࡯ࡤࠨί"), None)
      return True
    except:
      self.logger.debug(bstack1lllll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡶࡪࡪࠠࡸࡪ࡬ࡰࡪࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣ࡬ࡪࡧ࡬ࡵࡪࠣࡧ࡭࡫ࡣ࡬ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠦὸ"))
      return False
  def bstack11111111lll_opy_(self):
    bstack1lllll1lll11_opy_ = bstack1lllll1_opy_ (u"ࠧࡢࡲࡳࠫό") if self.bstack11ll111ll_opy_ else bstack1lllll1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪὺ")
    bstack111111l11ll_opy_ = bstack1lllll1_opy_ (u"ࠤࡸࡲࡩ࡫ࡦࡪࡰࡨࡨࠧύ") if self.config.get(bstack1lllll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩὼ")) is None else True
    bstack11ll11l1ll1_opy_ = bstack1lllll1_opy_ (u"ࠦࡦࡶࡩ࠰ࡣࡳࡴࡤࡶࡥࡳࡥࡼ࠳࡬࡫ࡴࡠࡲࡵࡳ࡯࡫ࡣࡵࡡࡷࡳࡰ࡫࡮ࡀࡰࡤࡱࡪࡃࡻࡾࠨࡷࡽࡵ࡫࠽ࡼࡿࠩࡴࡪࡸࡣࡺ࠿ࡾࢁࠧώ").format(self.config[bstack1lllll1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪ὾")], bstack1lllll1lll11_opy_, bstack111111l11ll_opy_)
    if self.percy_capture_mode:
      bstack11ll11l1ll1_opy_ += bstack1lllll1_opy_ (u"ࠨࠦࡱࡧࡵࡧࡾࡥࡣࡢࡲࡷࡹࡷ࡫࡟࡮ࡱࡧࡩࡂࢁࡽࠣ὿").format(self.percy_capture_mode)
    uri = bstack1lll1ll11l_opy_(bstack11ll11l1ll1_opy_)
    try:
      response = bstack1l1111111_opy_(bstack1lllll1_opy_ (u"ࠧࡈࡇࡗࠫᾀ"), uri, {}, {bstack1lllll1_opy_ (u"ࠨࡣࡸࡸ࡭࠭ᾁ"): (self.config[bstack1lllll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᾂ")], self.config[bstack1lllll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᾃ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack11l1l11ll_opy_ = data.get(bstack1lllll1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬᾄ"))
        self.percy_capture_mode = data.get(bstack1lllll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡣࡨࡧࡰࡵࡷࡵࡩࡤࡳ࡯ࡥࡧࠪᾅ"))
        os.environ[bstack1lllll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫᾆ")] = str(self.bstack11l1l11ll_opy_)
        os.environ[bstack1lllll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫᾇ")] = str(self.percy_capture_mode)
        if bstack111111l11ll_opy_ == bstack1lllll1_opy_ (u"ࠣࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧࠦᾈ") and str(self.bstack11l1l11ll_opy_).lower() == bstack1lllll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᾉ"):
          self.bstack11l1l11lll_opy_ = True
        if bstack1lllll1_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤᾊ") in data:
          return data[bstack1lllll1_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥᾋ")]
        else:
          raise bstack1lllll1_opy_ (u"࡚ࠬ࡯࡬ࡧࡱࠤࡓࡵࡴࠡࡈࡲࡹࡳࡪࠠ࠮ࠢࡾࢁࠬᾌ").format(data)
      else:
        raise bstack1lllll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡲࡨࡶࡨࡿࠠࡵࡱ࡮ࡩࡳ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡶࡸࡦࡺࡵࡴࠢ࠰ࠤࢀࢃࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡆࡴࡪࡹࠡ࠯ࠣࡿࢂࠨᾍ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠࡱࡴࡲ࡮ࡪࡩࡴࠣᾎ").format(e))
  def bstack111111ll111_opy_(self):
    bstack1lllllll1111_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠣࡲࡨࡶࡨࡿࡃࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠦᾏ"))
    try:
      if bstack1lllll1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪᾐ") not in self.bstack111111111l1_opy_:
        self.bstack111111111l1_opy_[bstack1lllll1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫᾑ")] = 2
      with open(bstack1lllllll1111_opy_, bstack1lllll1_opy_ (u"ࠫࡼ࠭ᾒ")) as fp:
        json.dump(self.bstack111111111l1_opy_, fp)
      return bstack1lllllll1111_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡥࡵࡩࡦࡺࡥࠡࡲࡨࡶࡨࡿࠠࡤࡱࡱࡪ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᾓ").format(e))
  def bstack1lllllll1ll1_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1llllll11l11_opy_ == bstack1lllll1_opy_ (u"࠭ࡷࡪࡰࠪᾔ"):
        bstack111111l1lll_opy_ = [bstack1lllll1_opy_ (u"ࠧࡤ࡯ࡧ࠲ࡪࡾࡥࠨᾕ"), bstack1lllll1_opy_ (u"ࠨ࠱ࡦࠫᾖ")]
        cmd = bstack111111l1lll_opy_ + cmd
      cmd = bstack1lllll1_opy_ (u"ࠩࠣࠫᾗ").join(cmd)
      self.logger.debug(bstack1lllll1_opy_ (u"ࠥࡖࡺࡴ࡮ࡪࡰࡪࠤࢀࢃࠢᾘ").format(cmd))
      with open(self.bstack1llllll11ll1_opy_, bstack1lllll1_opy_ (u"ࠦࡦࠨᾙ")) as bstack1lllllll11ll_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1lllllll11ll_opy_, text=True, stderr=bstack1lllllll11ll_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1lllll1ll1l1_opy_ = True
      self.logger.error(bstack1lllll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠦࡷࡪࡶ࡫ࠤࡨࡳࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢᾚ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1llllll1ll11_opy_:
        self.logger.info(bstack1lllll1_opy_ (u"ࠨࡓࡵࡱࡳࡴ࡮ࡴࡧࠡࡒࡨࡶࡨࡿࠢᾛ"))
        cmd = [self.binary_path, bstack1lllll1_opy_ (u"ࠢࡦࡺࡨࡧ࠿ࡹࡴࡰࡲࠥᾜ")]
        self.bstack1lllllll1ll1_opy_(cmd)
        self.bstack1llllll1ll11_opy_ = False
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺ࡯ࡱࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡥࡲࡱࡲࡧ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᾝ").format(cmd, e))
  def bstack1ll1l11ll1_opy_(self):
    if not self.bstack11l1l11ll_opy_:
      return
    try:
      bstack1llllll1lll1_opy_ = 0
      while not self.bstack1llllll1ll11_opy_ and bstack1llllll1lll1_opy_ < self.bstack1lllllll111l_opy_:
        if self.bstack1lllll1ll1l1_opy_:
          self.logger.info(bstack1lllll1_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡵࡨࡸࡺࡶࠠࡧࡣ࡬ࡰࡪࡪࠢᾞ"))
          return
        time.sleep(1)
        bstack1llllll1lll1_opy_ += 1
      os.environ[bstack1lllll1_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡅࡉࡘ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࠩᾟ")] = str(self.bstack111111111ll_opy_())
      self.logger.info(bstack1lllll1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠧᾠ"))
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨᾡ").format(e))
  def bstack111111111ll_opy_(self):
    if self.bstack11ll111ll_opy_:
      return
    try:
      bstack11111111ll1_opy_ = [platform[bstack1lllll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫᾢ")].lower() for platform in self.config.get(bstack1lllll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪᾣ"), [])]
      bstack1111111ll1l_opy_ = sys.maxsize
      bstack1111111l1l1_opy_ = bstack1lllll1_opy_ (u"ࠨࠩᾤ")
      for browser in bstack11111111ll1_opy_:
        if browser in self.bstack1llllll1l1ll_opy_:
          bstack111111l11l1_opy_ = self.bstack1llllll1l1ll_opy_[browser]
        if bstack111111l11l1_opy_ < bstack1111111ll1l_opy_:
          bstack1111111ll1l_opy_ = bstack111111l11l1_opy_
          bstack1111111l1l1_opy_ = browser
      return bstack1111111l1l1_opy_
    except Exception as e:
      self.logger.error(bstack1lllll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡦࡪࡹࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᾥ").format(e))
  @classmethod
  def bstack11lll11lll_opy_(self):
    return os.getenv(bstack1lllll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࠨᾦ"), bstack1lllll1_opy_ (u"ࠫࡋࡧ࡬ࡴࡧࠪᾧ")).lower()
  @classmethod
  def bstack1l1l1l1l1_opy_(self):
    return os.getenv(bstack1lllll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩᾨ"), bstack1lllll1_opy_ (u"࠭ࠧᾩ"))
  @classmethod
  def bstack11lllllll11_opy_(cls, value):
    cls.bstack11l1l11lll_opy_ = value
  @classmethod
  def bstack1111111llll_opy_(cls):
    return cls.bstack11l1l11lll_opy_
  @classmethod
  def bstack11lllllllll_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1llllll1111l_opy_(cls):
    return cls.percy_build_id