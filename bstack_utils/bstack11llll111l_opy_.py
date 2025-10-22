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
import sys
import logging
import tarfile
import io
import os
import time
import requests
import re
from requests_toolbelt.multipart.encoder import MultipartEncoder
from bstack_utils.constants import bstack11l1l11lll1_opy_, bstack11l11l1lll1_opy_, bstack11l11llll11_opy_
import tempfile
import json
bstack11111ll11l1_opy_ = os.getenv(bstack1lllll1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡋࡤࡌࡉࡍࡇࠥễ"), None) or os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡧࡩࡧࡻࡧ࠯࡮ࡲ࡫ࠧỆ"))
bstack11111l111ll_opy_ = os.path.join(bstack1lllll1l_opy_ (u"ࠦࡱࡵࡧࠣệ"), bstack1lllll1l_opy_ (u"ࠬࡹࡤ࡬࠯ࡦࡰ࡮࠳ࡤࡦࡤࡸ࡫࠳ࡲ࡯ࡨࠩỈ"))
logging.Formatter.converter = time.gmtime
def get_logger(name=__name__, level=None):
  logger = logging.getLogger(name)
  if level:
    logging.basicConfig(
      level=level,
      format=bstack1lllll1l_opy_ (u"࠭ࠥࠩࡣࡶࡧࡹ࡯࡭ࡦࠫࡶࠤࡠࠫࠨ࡯ࡣࡰࡩ࠮ࡹ࡝࡜ࠧࠫࡰࡪࡼࡥ࡭ࡰࡤࡱࡪ࠯ࡳ࡞ࠢ࠰ࠤࠪ࠮࡭ࡦࡵࡶࡥ࡬࡫ࠩࡴࠩỉ"),
      datefmt=bstack1lllll1l_opy_ (u"࡛ࠧࠦ࠰ࠩࡲ࠳ࠥࡥࡖࠨࡌ࠿ࠫࡍ࠻ࠧࡖ࡞ࠬỊ"),
      stream=sys.stdout
    )
  return logger
def bstack1l1l11l11ll_opy_():
  bstack11111ll1lll_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡋࡑࡅࡗ࡟࡟ࡅࡇࡅ࡙ࡌࠨị"), bstack1lllll1l_opy_ (u"ࠤࡩࡥࡱࡹࡥࠣỌ"))
  return logging.DEBUG if bstack11111ll1lll_opy_.lower() == bstack1lllll1l_opy_ (u"ࠥࡸࡷࡻࡥࠣọ") else logging.INFO
def bstack1l1llll11l1_opy_():
  global bstack11111ll11l1_opy_
  if os.path.exists(bstack11111ll11l1_opy_):
    os.remove(bstack11111ll11l1_opy_)
  if os.path.exists(bstack11111l111ll_opy_):
    os.remove(bstack11111l111ll_opy_)
def bstack11ll11l1ll_opy_():
  for handler in logging.getLogger().handlers:
    logging.getLogger().removeHandler(handler)
def configure_logger(config, log_level):
  bstack11111l11ll1_opy_ = log_level
  if bstack1lllll1l_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭Ỏ") in config and config[bstack1lllll1l_opy_ (u"ࠬࡲ࡯ࡨࡎࡨࡺࡪࡲࠧỏ")] in bstack11l11l1lll1_opy_:
    bstack11111l11ll1_opy_ = bstack11l11l1lll1_opy_[config[bstack1lllll1l_opy_ (u"࠭࡬ࡰࡩࡏࡩࡻ࡫࡬ࠨỐ")]]
  if config.get(bstack1lllll1l_opy_ (u"ࠧࡥ࡫ࡶࡥࡧࡲࡥࡂࡷࡷࡳࡈࡧࡰࡵࡷࡵࡩࡑࡵࡧࡴࠩố"), False):
    logging.getLogger().setLevel(bstack11111l11ll1_opy_)
    return bstack11111l11ll1_opy_
  global bstack11111ll11l1_opy_
  bstack11ll11l1ll_opy_()
  bstack11111ll1111_opy_ = logging.Formatter(
    fmt=bstack1lllll1l_opy_ (u"ࠨࠧࠫࡥࡸࡩࡴࡪ࡯ࡨ࠭ࡸ࡛ࠦࠦࠪࡱࡥࡲ࡫ࠩࡴ࡟࡞ࠩ࠭ࡲࡥࡷࡧ࡯ࡲࡦࡳࡥࠪࡵࡠࠤ࠲ࠦࠥࠩ࡯ࡨࡷࡸࡧࡧࡦࠫࡶࠫỒ"),
    datefmt=bstack1lllll1l_opy_ (u"ࠩࠨ࡝࠲ࠫ࡭࠮ࠧࡧࡘࠪࡎ࠺ࠦࡏ࠽ࠩࡘࡠࠧồ"),
  )
  bstack11111ll1l1l_opy_ = logging.StreamHandler(sys.stdout)
  file_handler = logging.FileHandler(bstack11111ll11l1_opy_)
  file_handler.setFormatter(bstack11111ll1111_opy_)
  bstack11111ll1l1l_opy_.setFormatter(bstack11111ll1111_opy_)
  file_handler.setLevel(logging.DEBUG)
  bstack11111ll1l1l_opy_.setLevel(log_level)
  file_handler.addFilter(lambda r: r.name != bstack1lllll1l_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱ࠳ࡽࡥࡣࡦࡵ࡭ࡻ࡫ࡲ࠯ࡴࡨࡱࡴࡺࡥ࠯ࡴࡨࡱࡴࡺࡥࡠࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲࠬỔ"))
  logging.getLogger().setLevel(logging.DEBUG)
  bstack11111ll1l1l_opy_.setLevel(bstack11111l11ll1_opy_)
  logging.getLogger().addHandler(bstack11111ll1l1l_opy_)
  logging.getLogger().addHandler(file_handler)
  return bstack11111l11ll1_opy_
def bstack11111l111l1_opy_(config):
  try:
    bstack11111l1lll1_opy_ = set(bstack11l11llll11_opy_)
    bstack11111l11l1l_opy_ = bstack1lllll1l_opy_ (u"ࠫࠬổ")
    with open(bstack1lllll1l_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠨỖ")) as bstack11111l1l1ll_opy_:
      bstack11111ll111l_opy_ = bstack11111l1l1ll_opy_.read()
      bstack11111l11l1l_opy_ = re.sub(bstack1lllll1l_opy_ (u"ࡸࠧ࡟ࠪ࡟ࡷ࠰࠯࠿ࠤ࠰࠭ࠨࡡࡴࠧỗ"), bstack1lllll1l_opy_ (u"ࠧࠨỘ"), bstack11111ll111l_opy_, flags=re.M)
      bstack11111l11l1l_opy_ = re.sub(
        bstack1lllll1l_opy_ (u"ࡳࠩࡡࠬࡡࡹࠫࠪࡁࠫࠫộ") + bstack1lllll1l_opy_ (u"ࠩࡿࠫỚ").join(bstack11111l1lll1_opy_) + bstack1lllll1l_opy_ (u"ࠪ࠭࠳࠰ࠤࠨớ"),
        bstack1lllll1l_opy_ (u"ࡶࠬࡢ࠲࠻ࠢ࡞ࡖࡊࡊࡁࡄࡖࡈࡈࡢ࠭Ờ"),
        bstack11111l11l1l_opy_, flags=re.M | re.I
      )
    def bstack11111l11l11_opy_(dic):
      bstack11111ll11ll_opy_ = {}
      for key, value in dic.items():
        if key in bstack11111l1lll1_opy_:
          bstack11111ll11ll_opy_[key] = bstack1lllll1l_opy_ (u"ࠬࡡࡒࡆࡆࡄࡇ࡙ࡋࡄ࡞ࠩờ")
        else:
          if isinstance(value, dict):
            bstack11111ll11ll_opy_[key] = bstack11111l11l11_opy_(value)
          else:
            bstack11111ll11ll_opy_[key] = value
      return bstack11111ll11ll_opy_
    bstack11111ll11ll_opy_ = bstack11111l11l11_opy_(config)
    return {
      bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡿ࡭࡭ࠩỞ"): bstack11111l11l1l_opy_,
      bstack1lllll1l_opy_ (u"ࠧࡧ࡫ࡱࡥࡱࡩ࡯࡯ࡨ࡬࡫࠳ࡰࡳࡰࡰࠪở"): json.dumps(bstack11111ll11ll_opy_)
    }
  except Exception as e:
    return {}
def bstack11111l1llll_opy_(inipath, rootpath):
  log_dir = os.path.join(os.getcwd(), bstack1lllll1l_opy_ (u"ࠨ࡮ࡲ࡫ࠬỠ"))
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
  bstack11111l1ll1l_opy_ = os.path.join(log_dir, bstack1lllll1l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࡡࡦࡳࡳ࡬ࡩࡨࡵࠪỡ"))
  if not os.path.exists(bstack11111l1ll1l_opy_):
    bstack11111ll1l11_opy_ = {
      bstack1lllll1l_opy_ (u"ࠥ࡭ࡳ࡯ࡰࡢࡶ࡫ࠦỢ"): str(inipath),
      bstack1lllll1l_opy_ (u"ࠦࡷࡵ࡯ࡵࡲࡤࡸ࡭ࠨợ"): str(rootpath)
    }
    with open(os.path.join(log_dir, bstack1lllll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࡤࡩ࡯࡯ࡨ࡬࡫ࡸ࠴ࡪࡴࡱࡱࠫỤ")), bstack1lllll1l_opy_ (u"࠭ࡷࠨụ")) as bstack11111ll1ll1_opy_:
      bstack11111ll1ll1_opy_.write(json.dumps(bstack11111ll1l11_opy_))
def bstack11111l1ll11_opy_():
  try:
    bstack11111l1ll1l_opy_ = os.path.join(os.getcwd(), bstack1lllll1l_opy_ (u"ࠧ࡭ࡱࡪࠫỦ"), bstack1lllll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧủ"))
    if os.path.exists(bstack11111l1ll1l_opy_):
      with open(bstack11111l1ll1l_opy_, bstack1lllll1l_opy_ (u"ࠩࡵࠫỨ")) as bstack11111ll1ll1_opy_:
        bstack11111l1l1l1_opy_ = json.load(bstack11111ll1ll1_opy_)
      return bstack11111l1l1l1_opy_.get(bstack1lllll1l_opy_ (u"ࠪ࡭ࡳ࡯ࡰࡢࡶ࡫ࠫứ"), bstack1lllll1l_opy_ (u"ࠫࠬỪ")), bstack11111l1l1l1_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡸ࡯ࡰࡶࡳࡥࡹ࡮ࠧừ"), bstack1lllll1l_opy_ (u"࠭ࠧỬ"))
  except:
    pass
  return None, None
def bstack11111l1l11l_opy_():
  try:
    bstack11111l1ll1l_opy_ = os.path.join(os.getcwd(), bstack1lllll1l_opy_ (u"ࠧ࡭ࡱࡪࠫử"), bstack1lllll1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࡠࡥࡲࡲ࡫࡯ࡧࡴ࠰࡭ࡷࡴࡴࠧỮ"))
    if os.path.exists(bstack11111l1ll1l_opy_):
      os.remove(bstack11111l1ll1l_opy_)
  except:
    pass
def bstack1ll1llll_opy_(config):
  try:
    from bstack_utils.helper import bstack1lll1ll1l_opy_, bstack11l111l1ll_opy_
    from browserstack_sdk.sdk_cli.cli import cli
    global bstack11111ll11l1_opy_
    if config.get(bstack1lllll1l_opy_ (u"ࠩࡧ࡭ࡸࡧࡢ࡭ࡧࡄࡹࡹࡵࡃࡢࡲࡷࡹࡷ࡫ࡌࡰࡩࡶࠫữ"), False):
      return
    uuid = os.getenv(bstack1lllll1l_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨỰ")) if os.getenv(bstack1lllll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩự")) else bstack1lll1ll1l_opy_.get_property(bstack1lllll1l_opy_ (u"ࠧࡹࡤ࡬ࡔࡸࡲࡎࡪࠢỲ"))
    if not uuid or uuid == bstack1lllll1l_opy_ (u"࠭࡮ࡶ࡮࡯ࠫỳ"):
      return
    bstack11111l1l111_opy_ = [bstack1lllll1l_opy_ (u"ࠧࡳࡧࡴࡹ࡮ࡸࡥ࡮ࡧࡱࡸࡸ࠴ࡴࡹࡶࠪỴ"), bstack1lllll1l_opy_ (u"ࠨࡒ࡬ࡴ࡫࡯࡬ࡦࠩỵ"), bstack1lllll1l_opy_ (u"ࠩࡳࡽࡵࡸ࡯࡫ࡧࡦࡸ࠳ࡺ࡯࡮࡮ࠪỶ"), bstack11111ll11l1_opy_, bstack11111l111ll_opy_]
    bstack11111lll111_opy_, root_path = bstack11111l1ll11_opy_()
    if bstack11111lll111_opy_ != None:
      bstack11111l1l111_opy_.append(bstack11111lll111_opy_)
    if root_path != None:
      bstack11111l1l111_opy_.append(os.path.join(root_path, bstack1lllll1l_opy_ (u"ࠪࡧࡴࡴࡦࡵࡧࡶࡸ࠳ࡶࡹࠨỷ")))
    bstack11ll11l1ll_opy_()
    logging.shutdown()
    output_file = os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠱ࡱࡵࡧࡴ࠯ࠪỸ") + uuid + bstack1lllll1l_opy_ (u"ࠬ࠴ࡴࡢࡴ࠱࡫ࡿ࠭ỹ"))
    with tarfile.open(output_file, bstack1lllll1l_opy_ (u"ࠨࡷ࠻ࡩࡽࠦỺ")) as archive:
      for file in filter(lambda f: os.path.exists(f), bstack11111l1l111_opy_):
        try:
          archive.add(file,  arcname=os.path.basename(file))
        except:
          pass
      for name, data in bstack11111l111l1_opy_(config).items():
        tarinfo = tarfile.TarInfo(name)
        bstack11111l1111l_opy_ = data.encode()
        tarinfo.size = len(bstack11111l1111l_opy_)
        archive.addfile(tarinfo, io.BytesIO(bstack11111l1111l_opy_))
    multipart_data = MultipartEncoder(
      fields= {
        bstack1lllll1l_opy_ (u"ࠧࡥࡣࡷࡥࠬỻ"): (os.path.basename(output_file), open(os.path.abspath(output_file), bstack1lllll1l_opy_ (u"ࠨࡴࡥࠫỼ")), bstack1lllll1l_opy_ (u"ࠩࡤࡴࡵࡲࡩࡤࡣࡷ࡭ࡴࡴ࠯ࡹ࠯ࡪࡾ࡮ࡶࠧỽ")),
        bstack1lllll1l_opy_ (u"ࠪࡧࡱ࡯ࡥ࡯ࡶࡅࡹ࡮ࡲࡤࡖࡷ࡬ࡨࠬỾ"): uuid
      }
    )
    bstack11111l11lll_opy_ = bstack11l111l1ll_opy_(cli.config, [bstack1lllll1l_opy_ (u"ࠦࡦࡶࡩࡴࠤỿ"), bstack1lllll1l_opy_ (u"ࠧࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠧἀ"), bstack1lllll1l_opy_ (u"ࠨࡵࡱ࡮ࡲࡥࡩࠨἁ")], bstack11l1l11lll1_opy_)
    response = requests.post(
      bstack1lllll1l_opy_ (u"ࠢࡼࡿ࠲ࡧࡱ࡯ࡥ࡯ࡶ࠰ࡰࡴ࡭ࡳ࠰ࡷࡳࡰࡴࡧࡤࠣἂ").format(bstack11111l11lll_opy_),
      data=multipart_data,
      headers={bstack1lllll1l_opy_ (u"ࠨࡅࡲࡲࡹ࡫࡮ࡵ࠯ࡗࡽࡵ࡫ࠧἃ"): multipart_data.content_type},
      auth=(config[bstack1lllll1l_opy_ (u"ࠩࡸࡷࡪࡸࡎࡢ࡯ࡨࠫἄ")], config[bstack1lllll1l_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵࡎࡩࡾ࠭ἅ")])
    )
    os.remove(output_file)
    if response.status_code != 200:
      get_logger().debug(bstack1lllll1l_opy_ (u"ࠫࡊࡸࡲࡰࡴࠣࡹࡵࡲ࡯ࡢࡦࠣࡰࡴ࡭ࡳ࠻ࠢࠪἆ") + response.status_code)
  except Exception as e:
    get_logger().debug(bstack1lllll1l_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸ࡫࡮ࡥ࡫ࡱ࡫ࠥࡲ࡯ࡨࡵ࠽ࠫἇ") + str(e))
  finally:
    try:
      bstack1l1llll11l1_opy_()
      bstack11111l1l11l_opy_()
    except:
      pass