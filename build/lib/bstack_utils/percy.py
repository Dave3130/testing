# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
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
from bstack_utils.helper import bstack1lll111l1l_opy_
from bstack_utils.measure import measure
from bstack_utils.bstack11l1l1ll1_opy_ import bstack1l11111l1_opy_
class bstack11l1lll11_opy_:
  working_dir = os.getcwd()
  bstack11l1l1lll1_opy_ = False
  config = {}
  bstack111l1111ll1_opy_ = bstack11lll1_opy_ (u"ࠩࠪὃ")
  binary_path = bstack11lll1_opy_ (u"ࠪࠫὄ")
  bstack1lllllllll1l_opy_ = bstack11lll1_opy_ (u"ࠫࠬὅ")
  bstack11l1lllll_opy_ = False
  bstack1llllll11l11_opy_ = None
  bstack1lllll1ll1ll_opy_ = {}
  bstack1lllll1l11l1_opy_ = 300
  bstack1lllllllllll_opy_ = False
  logger = None
  bstack1llllll1l11l_opy_ = False
  bstack1ll1l11lll_opy_ = False
  percy_build_id = None
  bstack1llllll1l1l1_opy_ = bstack11lll1_opy_ (u"ࠬ࠭὆")
  bstack1lllll1l1l1l_opy_ = {
    bstack11lll1_opy_ (u"࠭ࡣࡩࡴࡲࡱࡪ࠭὇") : 1,
    bstack11lll1_opy_ (u"ࠧࡧ࡫ࡵࡩ࡫ࡵࡸࠨὈ") : 2,
    bstack11lll1_opy_ (u"ࠨࡧࡧ࡫ࡪ࠭Ὁ") : 3,
    bstack11lll1_opy_ (u"ࠩࡶࡥ࡫ࡧࡲࡪࠩὊ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1llllll111l1_opy_(self):
    bstack1lllll1llll1_opy_ = bstack11lll1_opy_ (u"ࠪࠫὋ")
    bstack1lllll1lll11_opy_ = sys.platform
    bstack1lllllll1l1l_opy_ = bstack11lll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࠪὌ")
    if re.match(bstack11lll1_opy_ (u"ࠧࡪࡡࡳࡹ࡬ࡲࢁࡳࡡࡤࠢࡲࡷࠧὍ"), bstack1lllll1lll11_opy_) != None:
      bstack1lllll1llll1_opy_ = bstack11l1l11lll1_opy_ + bstack11lll1_opy_ (u"ࠨ࠯ࡱࡧࡵࡧࡾ࠳࡯ࡴࡺ࠱ࡾ࡮ࡶࠢ὎")
      self.bstack1llllll1l1l1_opy_ = bstack11lll1_opy_ (u"ࠧ࡮ࡣࡦࠫ὏")
    elif re.match(bstack11lll1_opy_ (u"ࠣ࡯ࡶࡻ࡮ࡴࡼ࡮ࡵࡼࡷࢁࡳࡩ࡯ࡩࡺࢀࡨࡿࡧࡸ࡫ࡱࢀࡧࡩࡣࡸ࡫ࡱࢀࡼ࡯࡮ࡤࡧࡿࡩࡲࡩࡼࡸ࡫ࡱ࠷࠷ࠨὐ"), bstack1lllll1lll11_opy_) != None:
      bstack1lllll1llll1_opy_ = bstack11l1l11lll1_opy_ + bstack11lll1_opy_ (u"ࠤ࠲ࡴࡪࡸࡣࡺ࠯ࡺ࡭ࡳ࠴ࡺࡪࡲࠥὑ")
      bstack1lllllll1l1l_opy_ = bstack11lll1_opy_ (u"ࠥࡴࡪࡸࡣࡺ࠰ࡨࡼࡪࠨὒ")
      self.bstack1llllll1l1l1_opy_ = bstack11lll1_opy_ (u"ࠫࡼ࡯࡮ࠨὓ")
    else:
      bstack1lllll1llll1_opy_ = bstack11l1l11lll1_opy_ + bstack11lll1_opy_ (u"ࠧ࠵ࡰࡦࡴࡦࡽ࠲ࡲࡩ࡯ࡷࡻ࠲ࡿ࡯ࡰࠣὔ")
      self.bstack1llllll1l1l1_opy_ = bstack11lll1_opy_ (u"࠭࡬ࡪࡰࡸࡼࠬὕ")
    return bstack1lllll1llll1_opy_, bstack1lllllll1l1l_opy_
  def bstack1llllll11l1l_opy_(self):
    try:
      bstack1111111ll1l_opy_ = [os.path.join(expanduser(bstack11lll1_opy_ (u"ࠢࡿࠤὖ")), bstack11lll1_opy_ (u"ࠨ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠨὗ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack1111111ll1l_opy_:
        if(self.bstack1llllll1llll_opy_(path)):
          return path
      raise bstack11lll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨ὘")
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡦࡪࡰࡧࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡱࡣࡷ࡬ࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡹࠡࡦࡲࡻࡳࡲ࡯ࡢࡦ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠ࠮ࠢࡾࢁࠧὙ").format(e))
  def bstack1llllll1llll_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1111111111l_opy_(self, bstack1lllll1l1l11_opy_):
    return os.path.join(bstack1lllll1l1l11_opy_, self.bstack111l1111ll1_opy_ + bstack11lll1_opy_ (u"ࠦ࠳࡫ࡴࡢࡩࠥ὚"))
  def bstack1llllllll1ll_opy_(self, bstack1lllll1l1l11_opy_, bstack1llllllllll1_opy_):
    if not bstack1llllllllll1_opy_: return
    try:
      bstack1llllll11ll1_opy_ = self.bstack1111111111l_opy_(bstack1lllll1l1l11_opy_)
      with open(bstack1llllll11ll1_opy_, bstack11lll1_opy_ (u"ࠧࡽࠢὛ")) as f:
        f.write(bstack1llllllllll1_opy_)
        self.logger.debug(bstack11lll1_opy_ (u"ࠨࡓࡢࡸࡨࡨࠥࡴࡥࡸࠢࡈࡘࡦ࡭ࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡻࠥ὜"))
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡦࡼࡥࠡࡶ࡫ࡩࠥ࡫ࡴࡢࡩ࠯ࠤࡪࡸࡲࡰࡴ࠽ࠤࢀࢃࠢὝ").format(e))
  def bstack1lllllll1lll_opy_(self, bstack1lllll1l1l11_opy_):
    try:
      bstack1llllll11ll1_opy_ = self.bstack1111111111l_opy_(bstack1lllll1l1l11_opy_)
      if os.path.exists(bstack1llllll11ll1_opy_):
        with open(bstack1llllll11ll1_opy_, bstack11lll1_opy_ (u"ࠣࡴࠥ὞")) as f:
          bstack1llllllllll1_opy_ = f.read().strip()
          return bstack1llllllllll1_opy_ if bstack1llllllllll1_opy_ else None
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡉ࡙ࡧࡧ࠭ࠢࡨࡶࡷࡵࡲ࠻ࠢࡾࢁࠧὟ").format(e))
  def bstack1lllll11ll1l_opy_(self, bstack1lllll1l1l11_opy_, bstack1lllll1llll1_opy_):
    bstack1llllll1lll1_opy_ = self.bstack1lllllll1lll_opy_(bstack1lllll1l1l11_opy_)
    if bstack1llllll1lll1_opy_:
      try:
        bstack1lllll1l1lll_opy_ = self.bstack1lllll1lll1l_opy_(bstack1llllll1lll1_opy_, bstack1lllll1llll1_opy_)
        if not bstack1lllll1l1lll_opy_:
          self.logger.debug(bstack11lll1_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢ࡬ࡷࠥࡻࡰࠡࡶࡲࠤࡩࡧࡴࡦࠢࠫࡉ࡙ࡧࡧࠡࡷࡱࡧ࡭ࡧ࡮ࡨࡧࡧ࠭ࠧὠ"))
          return True
        self.logger.debug(bstack11lll1_opy_ (u"ࠦࡓ࡫ࡷࠡࡒࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨ࠰ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡹࡵࡪࡡࡵࡧࠥὡ"))
        return False
      except Exception as e:
        self.logger.warn(bstack11lll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡥ࡫ࡩࡨࡱࠠࡧࡱࡵࠤࡧ࡯࡮ࡢࡴࡼࠤࡺࡶࡤࡢࡶࡨࡷ࠱ࠦࡵࡴ࡫ࡱ࡫ࠥ࡫ࡸࡪࡵࡷ࡭ࡳ࡭ࠠࡣ࡫ࡱࡥࡷࡿ࠺ࠡࡽࢀࠦὢ").format(e))
    return False
  def bstack1lllll1lll1l_opy_(self, bstack1llllll1lll1_opy_, bstack1lllll1llll1_opy_):
    try:
      headers = {
        bstack11lll1_opy_ (u"ࠨࡉࡧ࠯ࡑࡳࡳ࡫࠭ࡎࡣࡷࡧ࡭ࠨὣ"): bstack1llllll1lll1_opy_
      }
      response = bstack1lll111l1l_opy_(bstack11lll1_opy_ (u"ࠧࡈࡇࡗࠫὤ"), bstack1lllll1llll1_opy_, {}, {bstack11lll1_opy_ (u"ࠣࡪࡨࡥࡩ࡫ࡲࡴࠤὥ"): headers})
      if response.status_code == 304:
        return False
      return True
    except Exception as e:
      raise(bstack11lll1_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡥ࡫ࡩࡨࡱࡩ࡯ࡩࠣࡪࡴࡸࠠࡑࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡵࡱࡦࡤࡸࡪࡹ࠺ࠡࡽࢀࠦὦ").format(e))
  @measure(event_name=EVENTS.bstack11l1l1111ll_opy_, stage=STAGE.bstack11ll1ll11_opy_)
  def bstack1lllllll11ll_opy_(self, bstack1lllll1llll1_opy_, bstack1lllllll1l1l_opy_):
    try:
      bstack1lllllll11l1_opy_ = self.bstack1llllll11l1l_opy_()
      bstack111111111ll_opy_ = os.path.join(bstack1lllllll11l1_opy_, bstack11lll1_opy_ (u"ࠪࡴࡪࡸࡣࡺ࠰ࡽ࡭ࡵ࠭ὧ"))
      bstack1lllllll111l_opy_ = os.path.join(bstack1lllllll11l1_opy_, bstack1lllllll1l1l_opy_)
      if self.bstack1lllll11ll1l_opy_(bstack1lllllll11l1_opy_, bstack1lllll1llll1_opy_): # if bstack11111111ll1_opy_, bstack1lllllll1ll_opy_ bstack1llllllllll1_opy_ is bstack1lllllll1111_opy_ to bstack111l111l1ll_opy_ version available (response 304)
        if os.path.exists(bstack1lllllll111l_opy_):
          self.logger.info(bstack11lll1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡴࡻ࡮ࡥࠢ࡬ࡲࠥࢁࡽ࠭ࠢࡶ࡯࡮ࡶࡰࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨὨ").format(bstack1lllllll111l_opy_))
          return bstack1lllllll111l_opy_
        if os.path.exists(bstack111111111ll_opy_):
          self.logger.info(bstack11lll1_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡿ࡯ࡰࠡࡨࡲࡹࡳࡪࠠࡪࡰࠣࡿࢂ࠲ࠠࡶࡰࡽ࡭ࡵࡶࡩ࡯ࡩࠥὩ").format(bstack111111111ll_opy_))
          return self.bstack1llllll1111l_opy_(bstack111111111ll_opy_, bstack1lllllll1l1l_opy_)
      self.logger.info(bstack11lll1_opy_ (u"ࠨࡄࡰࡹࡱࡰࡴࡧࡤࡪࡰࡪࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡪࡷࡵ࡭ࠡࡽࢀࠦὪ").format(bstack1lllll1llll1_opy_))
      response = bstack1lll111l1l_opy_(bstack11lll1_opy_ (u"ࠧࡈࡇࡗࠫὫ"), bstack1lllll1llll1_opy_, {}, {})
      if response.status_code == 200:
        bstack1llllll1l1ll_opy_ = response.headers.get(bstack11lll1_opy_ (u"ࠣࡇࡗࡥ࡬ࠨὬ"), bstack11lll1_opy_ (u"ࠤࠥὭ"))
        if bstack1llllll1l1ll_opy_:
          self.bstack1llllllll1ll_opy_(bstack1lllllll11l1_opy_, bstack1llllll1l1ll_opy_)
        with open(bstack111111111ll_opy_, bstack11lll1_opy_ (u"ࠪࡻࡧ࠭Ὦ")) as file:
          file.write(response.content)
        self.logger.info(bstack11lll1_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠠࡢࡰࡧࠤࡸࡧࡶࡦࡦࠣࡥࡹࠦࡻࡾࠤὯ").format(bstack111111111ll_opy_))
        return self.bstack1llllll1111l_opy_(bstack111111111ll_opy_, bstack1lllllll1l1l_opy_)
      else:
        raise(bstack11lll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠣࡸ࡭࡫ࠠࡧ࡫࡯ࡩ࠳ࠦࡓࡵࡣࡷࡹࡸࠦࡣࡰࡦࡨ࠾ࠥࢁࡽࠣὰ").format(response.status_code))
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡳࡼࡴ࡬ࡰࡣࡧࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻ࠽ࠤࢀࢃࠢά").format(e))
  def bstack1lllll1ll111_opy_(self, bstack1lllll1llll1_opy_, bstack1lllllll1l1l_opy_):
    try:
      retry = 2
      bstack1lllllll111l_opy_ = None
      bstack1lllll1l111l_opy_ = False
      while retry > 0:
        bstack1lllllll111l_opy_ = self.bstack1lllllll11ll_opy_(bstack1lllll1llll1_opy_, bstack1lllllll1l1l_opy_)
        bstack1lllll1l111l_opy_ = self.bstack1111111ll11_opy_(bstack1lllll1llll1_opy_, bstack1lllllll1l1l_opy_, bstack1lllllll111l_opy_)
        if bstack1lllll1l111l_opy_:
          break
        retry -= 1
      return bstack1lllllll111l_opy_, bstack1lllll1l111l_opy_
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣ࡫ࡪࡺࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠦࡰࡢࡶ࡫ࠦὲ").format(e))
    return bstack1lllllll111l_opy_, False
  def bstack1111111ll11_opy_(self, bstack1lllll1llll1_opy_, bstack1lllllll1l1l_opy_, bstack1lllllll111l_opy_, bstack11111111lll_opy_ = 0):
    if bstack11111111lll_opy_ > 1:
      return False
    if bstack1lllllll111l_opy_ == None or os.path.exists(bstack1lllllll111l_opy_) == False:
      self.logger.warn(bstack11lll1_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡱࡣࡷ࡬ࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡵࡩࡹࡸࡹࡪࡰࡪࠤࡩࡵࡷ࡯࡮ࡲࡥࡩࠨέ"))
      return False
    bstack1lllll1ll11l_opy_ = bstack11lll1_opy_ (u"ࡴࠥࡢ࠳࠰ࡀࡱࡧࡵࡧࡾ࠵ࡣ࡭࡫ࠣࡠࡩ࠱࡜࠯࡞ࡧ࠯ࡡ࠴࡜ࡥ࠭ࠥὴ")
    command = bstack11lll1_opy_ (u"ࠪࡿࢂࠦ࠭࠮ࡸࡨࡶࡸ࡯࡯࡯ࠩή").format(bstack1lllllll111l_opy_)
    bstack11111111l11_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1lllll1ll11l_opy_, bstack11111111l11_opy_) != None:
      return True
    else:
      self.logger.error(bstack11lll1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡺࡪࡸࡳࡪࡱࡱࠤࡨ࡮ࡥࡤ࡭ࠣࡪࡦ࡯࡬ࡦࡦࠥὶ"))
      return False
  def bstack1llllll1111l_opy_(self, bstack111111111ll_opy_, bstack1lllllll1l1l_opy_):
    try:
      working_dir = os.path.dirname(bstack111111111ll_opy_)
      shutil.unpack_archive(bstack111111111ll_opy_, working_dir)
      bstack1lllllll111l_opy_ = os.path.join(working_dir, bstack1lllllll1l1l_opy_)
      os.chmod(bstack1lllllll111l_opy_, 0o755)
      return bstack1lllllll111l_opy_
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡷࡱࡾ࡮ࡶࠠࡱࡧࡵࡧࡾࠦࡢࡪࡰࡤࡶࡾࠨί"))
  def bstack1111111l11l_opy_(self):
    try:
      bstack1llllllll1l1_opy_ = self.config.get(bstack11lll1_opy_ (u"࠭ࡰࡦࡴࡦࡽࠬὸ"))
      bstack1111111l11l_opy_ = bstack1llllllll1l1_opy_ or (bstack1llllllll1l1_opy_ is None and self.bstack11l1l1lll1_opy_)
      if not bstack1111111l11l_opy_ or self.config.get(bstack11lll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪό"), None) not in bstack11l11ll111l_opy_:
        return False
      self.bstack11l1lllll_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"ࠣࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡩ࡫ࡴࡦࡥࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥὺ").format(e))
  def bstack1111111l1ll_opy_(self):
    try:
      bstack1111111l1ll_opy_ = self.percy_capture_mode
      return bstack1111111l1ll_opy_
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡪࡥࡵࡧࡦࡸࠥࡶࡥࡳࡥࡼࠤࡨࡧࡰࡵࡷࡵࡩࠥࡳ࡯ࡥࡧ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥύ").format(e))
  def init(self, bstack11l1l1lll1_opy_, config, logger):
    self.bstack11l1l1lll1_opy_ = bstack11l1l1lll1_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1111111l11l_opy_():
      return
    self.bstack1lllll1ll1ll_opy_ = config.get(bstack11lll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࡑࡳࡸ࡮ࡵ࡮ࡴࠩὼ"), {})
    self.percy_capture_mode = config.get(bstack11lll1_opy_ (u"ࠫࡵ࡫ࡲࡤࡻࡆࡥࡵࡺࡵࡳࡧࡐࡳࡩ࡫ࠧώ"))
    try:
      bstack1lllll1llll1_opy_, bstack1lllllll1l1l_opy_ = self.bstack1llllll111l1_opy_()
      self.bstack111l1111ll1_opy_ = bstack1lllllll1l1l_opy_
      bstack1lllllll111l_opy_, bstack1lllll1l111l_opy_ = self.bstack1lllll1ll111_opy_(bstack1lllll1llll1_opy_, bstack1lllllll1l1l_opy_)
      if bstack1lllll1l111l_opy_:
        self.binary_path = bstack1lllllll111l_opy_
        thread = Thread(target=self.bstack1lllll1l11ll_opy_)
        thread.start()
      else:
        self.bstack1llllll1l11l_opy_ = True
        self.logger.error(bstack11lll1_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡰࡦࡴࡦࡽࠥࡶࡡࡵࡪࠣࡪࡴࡻ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡗࡱࡥࡧࡲࡥࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡔࡪࡸࡣࡺࠤ὾").format(bstack1lllllll111l_opy_))
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢ὿").format(e))
  def bstack1lllllll1ll1_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack11lll1_opy_ (u"ࠧ࡭ࡱࡪࠫᾀ"), bstack11lll1_opy_ (u"ࠨࡲࡨࡶࡨࡿ࠮࡭ࡱࡪࠫᾁ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack11lll1_opy_ (u"ࠤࡓࡹࡸ࡮ࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢ࡯ࡳ࡬ࡹࠠࡢࡶࠣࡿࢂࠨᾂ").format(logfile))
      self.bstack1lllllllll1l_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡳࡦࡶࠣࡴࡪࡸࡣࡺࠢ࡯ࡳ࡬ࠦࡰࡢࡶ࡫࠰ࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡽࢀࠦᾃ").format(e))
  @measure(event_name=EVENTS.bstack11l1l111lll_opy_, stage=STAGE.bstack11ll1ll11_opy_)
  def bstack1lllll1l11ll_opy_(self):
    bstack1llllll111ll_opy_ = self.bstack1lllll11ll11_opy_()
    if bstack1llllll111ll_opy_ == None:
      self.bstack1llllll1l11l_opy_ = True
      self.logger.error(bstack11lll1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡸࡴࡱࡥ࡯ࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠱ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡲࡨࡶࡨࡿࠢᾄ"))
      return False
    bstack1llllll11lll_opy_ = [bstack11lll1_opy_ (u"ࠧࡧࡰࡱ࠼ࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹࠨᾅ") if self.bstack11l1l1lll1_opy_ else bstack11lll1_opy_ (u"࠭ࡥࡹࡧࡦ࠾ࡸࡺࡡࡳࡶࠪᾆ")]
    bstack11111l1l1ll_opy_ = self.bstack1llllllll111_opy_()
    if bstack11111l1l1ll_opy_ != None:
      bstack1llllll11lll_opy_.append(bstack11lll1_opy_ (u"ࠢ࠮ࡥࠣࡿࢂࠨᾇ").format(bstack11111l1l1ll_opy_))
    env = os.environ.copy()
    env[bstack11lll1_opy_ (u"ࠣࡒࡈࡖࡈ࡟࡟ࡕࡑࡎࡉࡓࠨᾈ")] = bstack1llllll111ll_opy_
    env[bstack11lll1_opy_ (u"ࠤࡗࡌࡤࡈࡕࡊࡎࡇࡣ࡚࡛ࡉࡅࠤᾉ")] = os.environ.get(bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᾊ"), bstack11lll1_opy_ (u"ࠫࠬᾋ"))
    bstack1llllll11111_opy_ = [self.binary_path]
    self.bstack1lllllll1ll1_opy_()
    self.bstack1llllll11l11_opy_ = self.bstack1lllll11lll1_opy_(bstack1llllll11111_opy_ + bstack1llllll11lll_opy_, env)
    self.logger.debug(bstack11lll1_opy_ (u"࡙ࠧࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠨᾌ"))
    bstack11111111lll_opy_ = 0
    while self.bstack1llllll11l11_opy_.poll() == None:
      bstack1lllll1l1ll1_opy_ = self.bstack1111111l1l1_opy_()
      if bstack1lllll1l1ll1_opy_:
        self.logger.debug(bstack11lll1_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠤᾍ"))
        self.bstack1lllllllllll_opy_ = True
        return True
      bstack11111111lll_opy_ += 1
      self.logger.debug(bstack11lll1_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡒࡦࡶࡵࡽࠥ࠳ࠠࡼࡿࠥᾎ").format(bstack11111111lll_opy_))
      time.sleep(2)
    self.logger.error(bstack11lll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡉࡥ࡮ࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡽࢀࠤࡦࡺࡴࡦ࡯ࡳࡸࡸࠨᾏ").format(bstack11111111lll_opy_))
    self.bstack1llllll1l11l_opy_ = True
    return False
  def bstack1111111l1l1_opy_(self, bstack11111111lll_opy_ = 0):
    if bstack11111111lll_opy_ > 10:
      return False
    try:
      bstack1lllll1l1111_opy_ = os.environ.get(bstack11lll1_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡕࡈࡖ࡛ࡋࡒࡠࡃࡇࡈࡗࡋࡓࡔࠩᾐ"), bstack11lll1_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡰࡴࡩࡡ࡭ࡪࡲࡷࡹࡀ࠵࠴࠵࠻ࠫᾑ"))
      bstack1111111lll1_opy_ = bstack1lllll1l1111_opy_ + bstack11l1l1111l1_opy_
      response = requests.get(bstack1111111lll1_opy_)
      data = response.json()
      self.percy_build_id = data.get(bstack11lll1_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࠪᾒ"), {}).get(bstack11lll1_opy_ (u"ࠬ࡯ࡤࠨᾓ"), None)
      return True
    except:
      self.logger.debug(bstack11lll1_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡵࡣࡤࡷࡵࡶࡪࡪࠠࡸࡪ࡬ࡰࡪࠦࡰࡳࡱࡦࡩࡸࡹࡩ࡯ࡩࠣ࡬ࡪࡧ࡬ࡵࡪࠣࡧ࡭࡫ࡣ࡬ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠦᾔ"))
      return False
  def bstack1lllll11ll11_opy_(self):
    bstack1lllll11llll_opy_ = bstack11lll1_opy_ (u"ࠧࡢࡲࡳࠫᾕ") if self.bstack11l1l1lll1_opy_ else bstack11lll1_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵࡧࠪᾖ")
    bstack111111111l1_opy_ = bstack11lll1_opy_ (u"ࠤࡸࡲࡩ࡫ࡦࡪࡰࡨࡨࠧᾗ") if self.config.get(bstack11lll1_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᾘ")) is None else True
    bstack11ll11l11l1_opy_ = bstack11lll1_opy_ (u"ࠦࡦࡶࡩ࠰ࡣࡳࡴࡤࡶࡥࡳࡥࡼ࠳࡬࡫ࡴࡠࡲࡵࡳ࡯࡫ࡣࡵࡡࡷࡳࡰ࡫࡮ࡀࡰࡤࡱࡪࡃࡻࡾࠨࡷࡽࡵ࡫࠽ࡼࡿࠩࡴࡪࡸࡣࡺ࠿ࡾࢁࠧᾙ").format(self.config[bstack11lll1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᾚ")], bstack1lllll11llll_opy_, bstack111111111l1_opy_)
    if self.percy_capture_mode:
      bstack11ll11l11l1_opy_ += bstack11lll1_opy_ (u"ࠨࠦࡱࡧࡵࡧࡾࡥࡣࡢࡲࡷࡹࡷ࡫࡟࡮ࡱࡧࡩࡂࢁࡽࠣᾛ").format(self.percy_capture_mode)
    uri = bstack1l11111l1_opy_(bstack11ll11l11l1_opy_)
    try:
      response = bstack1lll111l1l_opy_(bstack11lll1_opy_ (u"ࠧࡈࡇࡗࠫᾜ"), uri, {}, {bstack11lll1_opy_ (u"ࠨࡣࡸࡸ࡭࠭ᾝ"): (self.config[bstack11lll1_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫᾞ")], self.config[bstack11lll1_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ᾟ")])})
      if response.status_code == 200:
        data = response.json()
        self.bstack11l1lllll_opy_ = data.get(bstack11lll1_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬᾠ"))
        self.percy_capture_mode = data.get(bstack11lll1_opy_ (u"ࠬࡶࡥࡳࡥࡼࡣࡨࡧࡰࡵࡷࡵࡩࡤࡳ࡯ࡥࡧࠪᾡ"))
        os.environ[bstack11lll1_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡅࡓࡅ࡜ࠫᾢ")] = str(self.bstack11l1lllll_opy_)
        os.environ[bstack11lll1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡆࡔࡆ࡝ࡤࡉࡁࡑࡖࡘࡖࡊࡥࡍࡐࡆࡈࠫᾣ")] = str(self.percy_capture_mode)
        if bstack111111111l1_opy_ == bstack11lll1_opy_ (u"ࠣࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧࠦᾤ") and str(self.bstack11l1lllll_opy_).lower() == bstack11lll1_opy_ (u"ࠤࡷࡶࡺ࡫ࠢᾥ"):
          self.bstack1ll1l11lll_opy_ = True
        if bstack11lll1_opy_ (u"ࠥࡸࡴࡱࡥ࡯ࠤᾦ") in data:
          return data[bstack11lll1_opy_ (u"ࠦࡹࡵ࡫ࡦࡰࠥᾧ")]
        else:
          raise bstack11lll1_opy_ (u"࡚ࠬ࡯࡬ࡧࡱࠤࡓࡵࡴࠡࡈࡲࡹࡳࡪࠠ࠮ࠢࡾࢁࠬᾨ").format(data)
      else:
        raise bstack11lll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡲࡨࡶࡨࡿࠠࡵࡱ࡮ࡩࡳ࠲ࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡶࡸࡦࡺࡵࡴࠢ࠰ࠤࢀࢃࠬࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡆࡴࡪࡹࠡ࠯ࠣࡿࢂࠨᾩ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡲࡨࡶࡨࡿࠠࡱࡴࡲ࡮ࡪࡩࡴࠣᾪ").format(e))
  def bstack1llllllll111_opy_(self):
    bstack1lllllll1l11_opy_ = os.path.join(tempfile.gettempdir(), bstack11lll1_opy_ (u"ࠣࡲࡨࡶࡨࡿࡃࡰࡰࡩ࡭࡬࠴ࡪࡴࡱࡱࠦᾫ"))
    try:
      if bstack11lll1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪᾬ") not in self.bstack1lllll1ll1ll_opy_:
        self.bstack1lllll1ll1ll_opy_[bstack11lll1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫᾭ")] = 2
      with open(bstack1lllllll1l11_opy_, bstack11lll1_opy_ (u"ࠫࡼ࠭ᾮ")) as fp:
        json.dump(self.bstack1lllll1ll1ll_opy_, fp)
      return bstack1lllllll1l11_opy_
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡥࡵࡩࡦࡺࡥࠡࡲࡨࡶࡨࡿࠠࡤࡱࡱࡪ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᾯ").format(e))
  def bstack1lllll11lll1_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack1llllll1l1l1_opy_ == bstack11lll1_opy_ (u"࠭ࡷࡪࡰࠪᾰ"):
        bstack1lllll1ll1l1_opy_ = [bstack11lll1_opy_ (u"ࠧࡤ࡯ࡧ࠲ࡪࡾࡥࠨᾱ"), bstack11lll1_opy_ (u"ࠨ࠱ࡦࠫᾲ")]
        cmd = bstack1lllll1ll1l1_opy_ + cmd
      cmd = bstack11lll1_opy_ (u"ࠩࠣࠫᾳ").join(cmd)
      self.logger.debug(bstack11lll1_opy_ (u"ࠥࡖࡺࡴ࡮ࡪࡰࡪࠤࢀࢃࠢᾴ").format(cmd))
      with open(self.bstack1lllllllll1l_opy_, bstack11lll1_opy_ (u"ࠦࡦࠨ᾵")) as bstack1llllll1l111_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack1llllll1l111_opy_, text=True, stderr=bstack1llllll1l111_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack1llllll1l11l_opy_ = True
      self.logger.error(bstack11lll1_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡷࡥࡷࡺࠠࡱࡧࡵࡧࡾࠦࡷࡪࡶ࡫ࠤࡨࡳࡤࠡ࠯ࠣࡿࢂ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰ࠽ࠤࢀࢃࠢᾶ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack1lllllllllll_opy_:
        self.logger.info(bstack11lll1_opy_ (u"ࠨࡓࡵࡱࡳࡴ࡮ࡴࡧࠡࡒࡨࡶࡨࡿࠢᾷ"))
        cmd = [self.binary_path, bstack11lll1_opy_ (u"ࠢࡦࡺࡨࡧ࠿ࡹࡴࡰࡲࠥᾸ")]
        self.bstack1lllll11lll1_opy_(cmd)
        self.bstack1lllllllllll_opy_ = False
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺ࡯ࡱࠢࡶࡩࡸࡹࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡥࡲࡱࡲࡧ࡮ࡥࠢ࠰ࠤࢀࢃࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱ࠾ࠥࢁࡽࠣᾹ").format(cmd, e))
  def bstack1l1l1111ll_opy_(self):
    if not self.bstack11l1lllll_opy_:
      return
    try:
      bstack11111111l1l_opy_ = 0
      while not self.bstack1lllllllllll_opy_ and bstack11111111l1l_opy_ < self.bstack1lllll1l11l1_opy_:
        if self.bstack1llllll1l11l_opy_:
          self.logger.info(bstack11lll1_opy_ (u"ࠤࡓࡩࡷࡩࡹࠡࡵࡨࡸࡺࡶࠠࡧࡣ࡬ࡰࡪࡪࠢᾺ"))
          return
        time.sleep(1)
        bstack11111111l1l_opy_ += 1
      os.environ[bstack11lll1_opy_ (u"ࠪࡔࡊࡘࡃ࡚ࡡࡅࡉࡘ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࠩΆ")] = str(self.bstack1llllllll11l_opy_())
      self.logger.info(bstack11lll1_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠧᾼ"))
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"࡛ࠧ࡮ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡵࡨࡸࡺࡶࠠࡱࡧࡵࡧࡾ࠲ࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡿࢂࠨ᾽").format(e))
  def bstack1llllllll11l_opy_(self):
    if self.bstack11l1l1lll1_opy_:
      return
    try:
      bstack1111111l111_opy_ = [platform[bstack11lll1_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠫι")].lower() for platform in self.config.get(bstack11lll1_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡵࠪ᾿"), [])]
      bstack1lllll1lllll_opy_ = sys.maxsize
      bstack1llllll1ll1l_opy_ = bstack11lll1_opy_ (u"ࠨࠩ῀")
      for browser in bstack1111111l111_opy_:
        if browser in self.bstack1lllll1l1l1l_opy_:
          bstack11111111111_opy_ = self.bstack1lllll1l1l1l_opy_[browser]
        if bstack11111111111_opy_ < bstack1lllll1lllll_opy_:
          bstack1lllll1lllll_opy_ = bstack11111111111_opy_
          bstack1llllll1ll1l_opy_ = browser
      return bstack1llllll1ll1l_opy_
    except Exception as e:
      self.logger.error(bstack11lll1_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡩ࡯ࡦࠣࡦࡪࡹࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥ῁").format(e))
  @classmethod
  def bstack1l1l1lllll_opy_(self):
    return os.getenv(bstack11lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡓࡉࡗࡉ࡙ࠨῂ"), bstack11lll1_opy_ (u"ࠫࡋࡧ࡬ࡴࡧࠪῃ")).lower()
  @classmethod
  def bstack11l1l11l1_opy_(self):
    return os.getenv(bstack11lll1_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡕࡋࡒࡄ࡛ࡢࡇࡆࡖࡔࡖࡔࡈࡣࡒࡕࡄࡆࠩῄ"), bstack11lll1_opy_ (u"࠭ࠧ῅"))
  @classmethod
  def bstack11lllll1l11_opy_(cls, value):
    cls.bstack1ll1l11lll_opy_ = value
  @classmethod
  def bstack1llllll1ll11_opy_(cls):
    return cls.bstack1ll1l11lll_opy_
  @classmethod
  def bstack11llll1ll1l_opy_(cls, value):
    cls.percy_build_id = value
  @classmethod
  def bstack1lllllllll11_opy_(cls):
    return cls.percy_build_id